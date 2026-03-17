---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 13
rubric_version: 13
---

# corps-committee -- Prompt Variations R13

## Variation Summary

| ID   | Axis                                                                 | Hypothesis |
|------|----------------------------------------------------------------------|------------|
| V-01 | Dual-enforcement pairing for C-02 and C-04 (C-37, single axis)      | Adding a ROLE VOICE GUARD table before Phase 3 -- listing each participant's in-scope domain and forbidden-topic scope -- creates a second enforcement mechanism for C-02 that operates independently of the TIER-N-SEQUENCE-COMMIT gate. An OWNERSHIP TALLY after the ACTION ITEMS table creates a second enforcement mechanism for C-04 that operates independently of the Owner Role column. The test: can a C-02 violation be caught if the tier gate is removed? Can a C-04 violation be caught if the table column is removed? With dual-enforcement, yes -- each mechanism detects violations the other can independently confirm. |
| V-02 | FAILS syntax template with [C-NN] as positional required field (C-38, single axis) | Declaring a canonical FAILS template block before any fill rules -- with the explicit form `FAILS [C-NN]: <description>` and a statement that a FAILS entry missing [C-NN] is syntactically malformed -- converts C-14 from "encouraged" to "structurally required." C-14 required that annotations exist and be accurate; C-38 requires that the template makes omission detectable as malformation. When the canonical form is declared up front and all fill-rule FAILS entries conform to it, a reviewer can check compliance by structural pattern match rather than content audit. |
| V-03 | REQUIRES: annotations for co-dependent criteria (C-39, single axis) | Placing an explicit CO-DEPENDENCY PREAMBLE table before Phase 2 fill rules -- and a `REQUIRES: C-35` declaration immediately before the TOKEN TRACE CONFIRMATION fill rules -- makes the C-35/C-36 architectural dependency visible at the evaluation site. A reviewer who sees `REQUIRES: C-35` knows to verify C-35 before scoring C-36; without it, vocabulary presence (CONSUMED/NOT-APPLICABLE/DROPPED) can mask structural unenforceability. The test: if C-35 is PARTIAL (no closed-set manifest), is C-36 still scored as PASS? With REQUIRES: declared, no -- the prerequisite check blocks the false positive. |
| V-04 | Combination: dual-enforcement + FAILS syntax template (V-01 + V-02) | Pairing ROLE VOICE GUARD + OWNERSHIP TALLY (C-37) with the canonical FAILS template (C-38) addresses the two structural gaps most likely to co-occur: role voice mismatches and incomplete criterion annotations. Each operates in an orthogonal phase -- ROLE VOICE GUARD before Phase 3, FAILS template throughout all fill rules. No interaction effects expected; the combination closes both gaps simultaneously. |
| V-05 | Full integration: V-01 + V-02 + V-03 (all R13 axes)                | All three R13 structural additions applied simultaneously on the R12 V-05 baseline (tier gates + table output + phase ENTER/EXIT). This is the only variation where a role voice violation, an anonymous action item, an incomplete FAILS annotation, and a C-36-without-C-35 false positive each produce a structurally detectable signal from independent mechanisms before delivery -- ROLE VOICE GUARD + tier gate for C-02, Owner column + OWNERSHIP TALLY for C-04, canonical template for C-14/C-38, and REQUIRES: declaration blocking C-36 false positives. |

---

## V-01 -- Dual-Enforcement Pairing (C-37, single axis)

**Axis:** Dual-enforcement pairing for C-02 (role voice) and C-04 (action item ownership)
**Hypothesis:** ROLE VOICE GUARD table adds a second C-02 enforcement mechanism independent of
the tier gate. OWNERSHIP TALLY adds a second C-04 enforcement mechanism independent of the
table column. With both mechanisms active, a violation in either property produces a detectable
signal from two orthogonal structural positions simultaneously.

```
---
name: org-committee
description: Committee meeting simulation for ROB, shiproom, or architecture board.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
depth: standard
# quick    -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep     -> exhaustive adversarial audit, 25+ findings, treat missing as failure

for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


## BEFORE YOU START

Type-specific primary obligations and fail conditions (C-13):

ROB: Produce a readiness verdict backed by named metric evidence.
  FAIL: "If there is no metric cited in the discussion, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with a stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line in the verdict, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives compared, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: Any participant speaking from the wrong role orientation = C-02 miss.
  FAILS: PM raises deployment topology as primary concern -- C-02
  FAILS: SRE leads product vision discussion -- C-02

Read this block fully. Do not begin the skeleton until this block is complete.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins -- verified for both structural presence and affirmation correctness.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
=== org:committee SIMULATION -- SKELETON (V-01: Dual-Enforcement Pairing) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |
[repeat per participant]

PHASE-0-EXIT:
  [ ] Committee Type declared using recognized label (ROB / shiproom / arch-board)
  [ ] Agenda Item stated
  [ ] Charter Source named or fallback declared
  [ ] Participant roster complete
  All checks: ___ [PASS / FAIL -- identify failing item]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present, EXIT checks PASS.
  If AMEND has occurred invalidating Phase 1: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt -- emit PHASE-1-RECOMMIT MANIFEST before proceeding.
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

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2 within Phase 1. Continue until YES.]

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
  [ ] Each INERTIA-FINDING opens with its full token label
  [ ] ## INERTIA RECORD populated with content anchors (no placeholders)
  [ ] INERTIA INVARIANT line present with commit reference and modification prohibition
  [ ] Sealed tokens enumeration prepared: INERTIA-FINDING-A, B, C, D [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Citation-anchor manifest declared in ## INERTIA RECORD above.
  Modifications to that record require updating this commit; modifications to this commit
  require updating that record. Findings A-D locked.
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
  Reassignment (if YES): ___

### TOKEN TRACE CONFIRMATION

| Token              | Status              | Tier Sort usage or charter citation       |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (must equal PHASE-1-COMMIT N=4). DROPPED count: ___
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] TIER SORT table complete, all participants assigned
  [ ] SORT-CHECK printed with explicit YES/NO Result
  [ ] TOKEN TRACE CONFIRMATION table has exactly 4 rows
  [ ] All status cells use CONSUMED / NOT-APPLICABLE / DROPPED vocabulary only
  [ ] DROPPED count stated; REPAIR RULE invoked if count > 0
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, CONFIRMATION complete.
  DROPPED count = ___. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective /
                                  NO -- Inertia-Advocate INJECTED]

---

## ROLE VOICE GUARD

[C-37 Mechanism 2 for C-02 -- independent of TIER-N-SEQUENCE-COMMIT gate]

| Role              | In-scope domain                        | Forbidden-topic scope                  |
|-------------------|----------------------------------------|----------------------------------------|
| ___               | ___                                    | ___                                    |
[repeat per participant]

ROLE VOICE SEAL: [locked] -- participant domains and forbidden-topic scopes committed.
  Any Phase 3 voice that leads with a forbidden-topic concern = C-02 miss, detectable
  from this table independently of tier gate status.
  | ENFORCE: terminal position -- NO ROLE VOICE GUARD CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS, INERTIA CONTINUITY BRIDGE
  declared, ROLE VOICE GUARD sealed.
  If AMEND has occurred invalidating Phase 3: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt -- emit PHASE-3-RECOMMIT MANIFEST before proceeding.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |
[Tier 1 rows -- all must appear before TIER-1-SEQUENCE-COMMIT]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete. Stances committed:
  [list each Tier 1 role and their STANCE token].
  No Tier 2 voice may appear before this line.
  | ENFORCE: terminal position in Tier 1 block.

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable required]| INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |
[Tier 2 rows -- all must appear before TIER-2-SEQUENCE-COMMIT]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete. Stances committed:
  [list each Tier 2 role and their STANCE token].
  No Tier 3 voice may appear before this line.
  | ENFORCE: terminal position in Tier 2 block.

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Primary endorsement.  | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |
[Tier 3 rows]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |
[repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] All Tier 1 voices complete before TIER-1-SEQUENCE-COMMIT
  [ ] All Tier 2 voices complete before TIER-2-SEQUENCE-COMMIT
  [ ] Each Tier 1 row: INERTIA-FINDING cite cell populated with named label
  [ ] Each Tier 2 row: Condition cell states specific deliverable (not "address concerns")
  [ ] Each Tier 3 row: RESPONDS-TO named concern + CITE label present
  [ ] Each voice complies with ROLE VOICE GUARD forbidden-topic scope
  [ ] At least one CONDITION or BLOCK in ## STANCE MANIFEST
  [ ] Sealed tokens enumeration prepared [N=K]
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order with
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both present.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications
  to this commit require updating ## STANCE MANIFEST.
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

| Field                        | Value                                              |
|------------------------------|----------------------------------------------------|
| Verdict                      | ___                                                |
| Conditions for full approval | ___                                                |
| Re-entry owner               | ___                                                |
| Re-entry trigger             | ___                                                |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |
[one row per item]

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].
  [C-37 Mechanism 2 for C-04 -- independent of Owner Role column structure]
  ENFORCE: action item count in TALLY must equal ACTION ITEMS table row count above.

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-EXIT:
  [ ] Verdict matches OUTCOME from Phase 4 exactly
  [ ] Conditions stated as specific deliverables (not "address feedback")
  [ ] Owner and Trigger present if verdict not APPROVED (named role, named artifact)
  [ ] Every action item: Owner Role, specific action, and deadline all populated
  [ ] OWNERSHIP TALLY count matches ACTION ITEMS row count; anonymous items = 0
  [ ] Every CONDITION/BLOCK role has a dissent row citing INERTIA-FINDING-* label
  All checks: ___ [PASS / FAIL]

PHASE-5-COMMIT: [locked] -- EXIT checks PASS. DECISIONS, ACTION ITEMS, OWNERSHIP TALLY,
  and DISSENTING OPINIONS complete. Owner and Trigger present if verdict not APPROVED.
  Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: participant table with Role and Orientation columns; one row per participant.
PRINT: PHASE-0-COMMIT with Sealed tokens enumerating four items explicitly.
  VALIDATE: all four token names present.
  FAILS: Sealed tokens field absent -- C-35
  FAILS: Committee Type declared as `product review` or unlabeled type -- C-01

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D. Each opens with its full token label as first element.
  A -- specific workflow or tool in production this agenda item displaces
  B -- specific integration surface at risk; name systems, APIs, or contracts
  C -- team whose cognitive habit would break; name team and the habit
  D -- non-obvious switching cost the proposal author did not account for
  FAILS: `(a) legacy-workflow` -- parenthesized letter, not the token; C-27
  FAILS: `Finding A:` -- abbreviated label; full token required; C-27

GATE-N retry: if INERTIA-FINDING-D is obvious, rerun all four. Loop until GATE-N = YES.

WRITE: ## INERTIA RECORD as table with Token and One-phrase anchor columns.
  FAILS: bare token with no anchor content -- C-35
  FAILS: placeholder text `[one-phrase anchor]` unfilled -- C-35

WRITE: INERTIA INVARIANT with both commit reference and modification prohibition.
  FAILS (a): commit reference present, prohibition absent -- C-35
  FAILS (b): neither element present -- C-35
  FAILS (c): line absent entirely -- C-35

PRINT: PHASE-1-COMMIT with Sealed tokens: INERTIA-FINDING-A, B, C, D [N=4].
  VALIDATE: token count explicitly stated.
  Bidirectionality clause required -- both coupling directions named.
  FAILS: one direction only -- C-45

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) -- roles with feasibility scrutiny, risk, or disruption orientation.
ASSIGN: Tier 2 (CONDITIONALS) -- roles holding conditional approval.
ASSIGN: Tier 3 (ADVOCATES) -- roles aligned with proposal goals.

SORT-CHECK:
PRINT: Test and Result. IF YES: name mis-sorted role, reprint corrected table; loop until NO.
  FAILS: correct table without SORT-CHECK gate -- C-25

TOKEN TRACE CONFIRMATION fill rules:
PRINT: four-row table with status for each PHASE-1-COMMIT sealed token.
ASSIGN status from vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED.
  CONSUMED: token cited in tier sort Rationale column.
  NOT-APPLICABLE: cite specific Phase 0 charter constraint; vague "not relevant" fails -- C-36
  DROPPED: triggers REPAIR RULE -- reopen Phase 1 for INVESTIGATION-ATTEMPT-N+1.
PRINT: CONFIRMATION INVARIANT with Row count = 4.
  VALIDATE: row count matches N=4 from PHASE-1-COMMIT.
  FAILS: fewer than 4 rows -- C-36
  FAILS: binary CONFIRMED/DROPOUT vocabulary -- three-way status required; C-36

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: TIER SORT table for Tier 1 or Tier 2 participant mapping to inertia orientation.
CONFIRM: YES if found; proceed to ROLE VOICE GUARD.
CONFIRM: NO if none found:
  INJECT: Inertia-Advocate as Tier 1, speaks first among all challengers.
  ENFORCE: cites at least one INERTIA-FINDING-* label in voice.
  ENFORCE: appears in ## STANCE MANIFEST.

VALIDATE:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE -- C-46
  FAILS (incorrect affirmation): YES declared when no qualifying participant exists -- C-49

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

PRINT: ROLE VOICE GUARD table -- one row per participant from Phase 0 roster.
ASSIGN: In-scope domain from charter orientation (what this role is chartered to examine).
ASSIGN: Forbidden-topic scope -- what this role must NOT lead as primary concern.
  Examples:
    PM: In-scope -- adoption, user value, competitive positioning
        Forbidden -- deployment topology, on-call operational burden
    SRE: In-scope -- reliability, on-call burden, incident surface
         Forbidden -- product vision, business strategy
    Architect: In-scope -- design trade-offs, technical debt, component boundaries
               Forbidden -- customer NPS, market positioning

PRINT: ROLE VOICE SEAL.
VALIDATE: each Phase 3 voice block complies with the forbidden-topic scope declared here.
  FAILS: PM voice raises deployment topology as primary concern -- C-02
    [C-37: detectable from ROLE VOICE GUARD table AND from TIER-N-SEQUENCE-COMMIT context]
  FAILS: ROLE VOICE GUARD table absent -- C-37 miss (single-mechanism C-02 enforcement only)
  FAILS: ROLE VOICE GUARD present but forbidden-topic scope cells empty -- C-37 miss

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE ENFORCEMENT [C-37 Mechanism 1 for C-02]:
ENFORCE: ALL Tier 1 voices must complete and TIER-1-SEQUENCE-COMMIT must be printed
  before any Tier 2 voice begins.
ENFORCE: ALL Tier 2 voices must complete and TIER-2-SEQUENCE-COMMIT must be printed
  before any Tier 3 voice begins.
  FAILS: Tier N+1 voice appearing before TIER-N-SEQUENCE-COMMIT -- C-02
  FAILS: TIER-N-SEQUENCE-COMMIT absent even if ordering appears correct -- C-25

VALIDATE STANCE cell: [BLOCK / CONDITION / APPROVE] -- no qualification.
  FAILS: stance embedded in prose, no STANCE field in table -- C-02
  FAILS: `CONDITION (pending)` in cell -- C-02

Tier 1 rows: INERTIA-FINDING cite cell required; named label from ## INERTIA RECORD.
Tier 2 rows: Condition cell must name specific approval condition; "address concerns" fails -- C-07.
Tier 3 rows: RESPONDS-TO: "[named concern]" opens Primary concern cell; CITE label in cite cell.

VALIDATE: at least one CONDITION or BLOCK row; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST table. WRITE: STANCE INVARIANT.
  FAILS: STANCE INVARIANT absent from ## STANCE MANIFEST -- C-47
PRINT: PHASE-3-COMMIT with bidirectionality clause.
  FAILS: one direction only -- C-45

---

**PHASE 4 fill rules:**

TALLY: count STANCE-TOKEN column in ## STANCE MANIFEST only; do not re-parse prose.
OUTCOME: all APPROVE -> APPROVED; any CONDITION no BLOCK -> APPROVED WITH CONDITIONS;
  any BLOCK -> BLOCKED or DEFERRED.
VALIDATE: counts match ## STANCE MANIFEST exactly.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) and Trigger (named artifact
  + recipient + authority). Missing either fails C-23.

PRINT: ACTION ITEMS table -- all three columns required per row.
  FAILS: missing Deadline cell -- C-04 [Mechanism 1: empty column cell]
  FAILS: missing Owner Role cell -- C-04 [Mechanism 1: empty column cell]

PRINT: OWNERSHIP TALLY [C-37 Mechanism 2 for C-04]:
  Format: "[N] action items. Named owners: [N]. Anonymous items: [0 required]."
  VALIDATE: total count in TALLY matches ACTION ITEMS table row count.
  VALIDATE: Anonymous items = 0; any nonzero count requires reopening Phase 5.
  FAILS: OWNERSHIP TALLY absent -- C-37 miss (single-mechanism C-04 enforcement only)
  FAILS: OWNERSHIP TALLY count < ACTION ITEMS row count -- C-04
    [C-37: both mechanisms detect: Owner column shows empty cell; Tally shows count gap]

WRITE: DISSENTING OPINIONS table -- one row per CONDITION/BLOCK stance.
ENFORCE: if no dissent -- single row: `[No dissent | [reason] | -- | -- | --]`

---

**AMEND fill rules (C-30, C-33, C-34):**

AMEND ROUTING TABLE:
  | Amendment Type           | Invalidates           | Re-execution scope  |
  |--------------------------|----------------------|---------------------|
  | Add attendee             | Phase 0, Phase 3     | Phase 0 -> Phase 3+ |
  | Change scope             | Phase 0 -> Phase 5   | Full re-execution   |
  | Change committee type    | Phase 0 -> Phase 5   | Full re-execution   |
  | Inject role post-Phase 2 | Phase 3 -> Phase 5   | Phase 3 -> Phase 5  |

AMEND-AFFECTED SITES: list each stale table cell before re-execution:
  [Phase -- table -- column -- token -- reason stale]

RECOMMIT MANIFEST (C-34): after each invalidated phase re-executes, before next phase resumes:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: cells added: [list], cells removed: [list], cells modified: [list]
    Version: v[K+1] supersedes v[K].
    Gate: downstream phases gate on this manifest only; original v1 seal is insufficient.
  FAILS: phase resumes without RECOMMIT MANIFEST -- C-34
  FAILS: downstream phase gates on v1 seal after AMEND -- C-34
```

---

## V-02 -- FAILS Syntax Template (C-38, single axis)

**Axis:** Canonical FAILS template with `[C-NN]` as positional required field
**Hypothesis:** Declaring a canonical FAILS template block before any fill rules -- with
`FAILS [C-NN]: <description>` as the required form and a statement that entries missing
`[C-NN]` are syntactically malformed -- converts criterion citation from convention to
structural requirement. This is the test for C-38: does the skill define the template, declare
omission as malformation, and include at least one example? A skill where `[C-NN]` is natural
(tables) but not required does not satisfy C-38.

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
  FAIL: "If there is no metric cited in the discussion, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with a stated blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO decision line in the verdict, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named architectural trade-offs and a selected alternative.
  FAIL: "If there are no named alternatives compared, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: Participant speaking from wrong role orientation = C-02 miss.

Read this block fully before beginning.

---

## FAILS SYNTAX TEMPLATE

Canonical form for ALL fill-rule FAILS entries in STEP 2 of this skill:

  FAILS [C-NN]: <description of what fails and why>

[C-NN] is a POSITIONAL REQUIRED FIELD. A FAILS entry without [C-NN] is syntactically
malformed -- not merely suboptimal. Any FAILS entry that deviates from this template is
treated as an incomplete annotation during scoring, regardless of the description content.

Examples:
  CORRECT:   FAILS [C-01]: committee type absent -- type not declared using recognized label
  CORRECT:   FAILS [C-02]: role voice mismatch -- PM raises deployment topology as primary
  CORRECT:   FAILS [C-04]: action item owner absent -- Owner Role cell empty in table row
  CORRECT:   FAILS [C-07]: vague condition -- "address concerns" is not a specific deliverable
  MALFORMED: FAILS: committee type absent              (missing [C-NN] entirely)
  MALFORMED: FAILS (C-01): committee type absent        ([C-NN] parenthesized, not positional)
  MALFORMED: FAILS -- committee type absent              (missing [C-NN] field)
  MALFORMED: committee type absent -- C-01 miss          (not FAILS-prefixed; C-01 at end)

This template applies to all FAILS entries that follow. An entry that deviates is a C-38 miss.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-02: FAILS Syntax Template) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |
[repeat per participant]

PHASE-0-EXIT:
  [ ] Committee Type declared using recognized label
  [ ] Agenda Item stated
  [ ] Charter Source named or fallback declared
  [ ] Participant roster complete
  All checks: ___ [PASS / FAIL]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present, EXIT checks PASS.
  If AMEND has occurred invalidating Phase 1: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt.
  Entering Phase 1.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2. Continue until YES.]

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
  [ ] Each INERTIA-FINDING opens with full token label
  [ ] ## INERTIA RECORD populated with content anchors
  [ ] INERTIA INVARIANT line present with commit reference and prohibition
  [ ] Sealed tokens enumeration prepared [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS, N=4 sealed tokens available.
  If AMEND has occurred invalidating Phase 2: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt.
  Entering Phase 2.

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

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] TIER SORT complete, all participants assigned
  [ ] SORT-CHECK printed with explicit Result
  [ ] TOKEN TRACE CONFIRMATION has 4 rows, three-way status vocabulary
  [ ] DROPPED count stated; REPAIR RULE invoked if > 0
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS, INERTIA CONTINUITY BRIDGE declared.
  If AMEND has occurred invalidating Phase 3: RECOMMIT MANIFEST v___ present? [YES / NO]
    If NO: halt.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |
[Tier 1 rows]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete.
  Stances committed: [list each Tier 1 role and STANCE token].
  No Tier 2 voice may appear before this line.

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable]         | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |
[Tier 2 rows]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete.
  Stances committed: [list each Tier 2 role and STANCE token].
  No Tier 3 voice may appear before this line.

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Primary endorsement.  | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |
[Tier 3 rows]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |
[repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] Tier 1 rows all before TIER-1-SEQUENCE-COMMIT
  [ ] Tier 2 rows all before TIER-2-SEQUENCE-COMMIT
  [ ] Tier 1 INERTIA-FINDING cite cells populated
  [ ] Tier 2 Condition cells specific (not "address concerns")
  [ ] Tier 3 RESPONDS-TO and CITE cells populated
  [ ] At least one CONDITION or BLOCK in ## STANCE MANIFEST
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to
  this commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

PHASE-4-ENTER:
  Precondition: PHASE-3-COMMIT present.
  Entering Phase 4.

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

PHASE-5-ENTER:
  Precondition: PHASE-4-COMMIT present.
  Entering Phase 5.

### DECISIONS

| Field                        | Value                                              |
|------------------------------|----------------------------------------------------|
| Verdict                      | ___                                                |
| Conditions for full approval | ___                                                |
| Re-entry owner               | ___                                                |
| Re-entry trigger             | ___                                                |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |
[one row per item]

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS complete.
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

NOTE: All FAILS entries below conform to the canonical template declared above:
  `FAILS [C-NN]: <description>`. Any deviation is a C-38 miss.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/`.
ENFORCE: fallback participants if no charter: PM, Architect, Inertia-Advocate.
PRINT: participant table. PRINT: PHASE-0-COMMIT with Sealed tokens field.
  FAILS [C-35]: Sealed tokens field absent from PHASE-0-COMMIT
  FAILS [C-01]: Committee Type declared as unlabeled or non-standard type (e.g., "product review")

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D, each opening with full token label.
  FAILS [C-27]: parenthesized letter `(a)` used instead of full token label
  FAILS [C-27]: abbreviated `Finding A:` used instead of `INERTIA-FINDING-A:`

GATE-N retry: if INERTIA-FINDING-D is obvious, rerun all four findings. Loop until YES.

WRITE: ## INERTIA RECORD table. WRITE: INERTIA INVARIANT.
  FAILS [C-35]: bare token with no anchor content in INERTIA RECORD table
  FAILS [C-35]: INERTIA INVARIANT absent or missing modification prohibition

PRINT: PHASE-1-COMMIT with Sealed tokens [N=4] and bidirectionality clause.
  FAILS [C-45]: bidirectionality clause states only one coupling direction

---

**PHASE 2 fill rules:**

ASSIGN tiers by charter orientation. Print TIER SORT table.
SORT-CHECK: print Test and Result; if YES -- reprint corrected table, loop until NO.
  FAILS [C-25]: correct table present but no SORT-CHECK gate printed

TOKEN TRACE CONFIRMATION:
PRINT: four-row table per PHASE-1-COMMIT sealed tokens.
ASSIGN: CONSUMED | NOT-APPLICABLE | DROPPED per token.
  NOT-APPLICABLE: cite specific charter constraint; vague justification fails.
  FAILS [C-36]: fewer than 4 rows in confirmation table -- count mismatch
  FAILS [C-36]: binary vocabulary used instead of three-way status
  DROPPED: invoke REPAIR RULE -- reopen Phase 1 before Phase 2 closes.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: TIER SORT table for inertia-oriented participant.
CONFIRM YES or NO; inject Inertia-Advocate if NO.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS [C-49]: YES declared when no qualifying Tier 1/Tier 2 participant exists

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE ENFORCEMENT:
  FAILS [C-02]: Tier N+1 voice row appears before TIER-N-SEQUENCE-COMMIT
  FAILS [C-25]: tier ordering appears correct but TIER-N-SEQUENCE-COMMIT absent

VALIDATE STANCE cell: [BLOCK / CONDITION / APPROVE] -- no qualification.
  FAILS [C-02]: stance embedded in prose only, no STANCE field in table row
  FAILS [C-02]: qualified token like `CONDITION (pending)` in STANCE cell

Tier 1: INERTIA-FINDING cite cell required.
Tier 2: Condition cell must name specific deliverable.
  FAILS [C-07]: Condition cell states "address concerns" without specifying the artifact
Tier 3: RESPONDS-TO: "[named concern]" opens Primary concern; CITE in cite cell.

VALIDATE: at least one CONDITION or BLOCK; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST and STANCE INVARIANT.
  FAILS [C-47]: STANCE INVARIANT absent from ## STANCE MANIFEST

PRINT: PHASE-3-COMMIT with bidirectionality clause.
  FAILS [C-45]: bidirectionality clause states only one direction

---

**PHASE 4 fill rules:**

TALLY: count STANCE-TOKEN column in ## STANCE MANIFEST only.
  FAILS [C-NN where N=tally criterion]: TALLY counts do not match ## STANCE MANIFEST

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions, Re-entry Owner and Trigger.
  FAILS [C-23]: Owner or Trigger absent when verdict is not APPROVED

ACTION ITEMS table: all three columns required per row.
  FAILS [C-04]: Owner Role cell empty in any action item row
  FAILS [C-04]: Deadline cell absent from any action item row

DISSENTING OPINIONS: one row per CONDITION/BLOCK stance.
  FAILS [C-05]: CONDITION or BLOCK stance holder has no dissent row

---

**AMEND fill rules (C-30, C-33, C-34):**

AMEND ROUTING TABLE: [as in V-01 above]

RECOMMIT MANIFEST: after each invalidated phase re-executes:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]: Delta, Version, Gate.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND issued
```

---

## V-03 -- REQUIRES: Annotations (C-39, single axis)

**Axis:** Co-dependent criteria declared with `REQUIRES:` annotations
**Hypothesis:** A CO-DEPENDENCY PREAMBLE table at the start of STEP 2 -- listing each
co-dependent criterion pair -- plus a `REQUIRES: C-35` declaration immediately before the
TOKEN TRACE CONFIRMATION fill rules, converts the latent C-35/C-36 trap into a visible
pre-check. Without the declaration, vocabulary presence (CONSUMED/NOT-APPLICABLE/DROPPED)
masks structural unenforceability; with it, a reviewer must verify C-35 before scoring C-36,
making the false-positive path detectable before delivery.

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
  FAIL: "If there is no metric cited, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO line in the verdict, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named alternatives and a selected option.
  FAIL: "If there are no named alternatives, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: participant speaking from wrong role orientation = C-02 miss.

Read this block fully before beginning.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one if
no charter inertia owner exists.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-03: REQUIRES: Annotations) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |
[repeat per participant]

PHASE-0-EXIT:
  [ ] Committee Type declared using recognized label
  [ ] Agenda Item stated; Charter Source named
  [ ] Participant roster complete
  All checks: ___ [PASS / FAIL]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present, EXIT checks PASS.
  If AMEND invalidated Phase 1: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 1.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not anticipate?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2. Continue until YES.]

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
  [ ] Each INERTIA-FINDING opens with full token label
  [ ] ## INERTIA RECORD populated with content anchors
  [ ] INERTIA INVARIANT present with commit reference and modification prohibition
  [ ] Sealed tokens enumeration prepared [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS, N=4 sealed tokens available.
  [REQUIRES: C-35 pre-check -- verify PHASE-1-COMMIT enumerates an explicit Sealed tokens
   closed set before proceeding to TOKEN TRACE CONFIRMATION below. If Sealed tokens are
   not enumerated as a closed set, TOKEN TRACE CONFIRMATION row count = N is unenforceable.]
  If AMEND invalidated Phase 2: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 2.

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

[REQUIRES: C-35 -- the closed-set token manifest in PHASE-1-COMMIT is the source of truth
 for this table's row count. Row count = N is only enforceable because PHASE-1-COMMIT
 enumerates an explicit closed set. Without that closed set, a dropped token produces no
 detectable absence here.]

| Token              | Status              | Tier Sort usage or charter citation       |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4).
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] TIER SORT complete; SORT-CHECK printed with explicit Result
  [ ] C-35 pre-check at PHASE-2-ENTER: PHASE-1-COMMIT Sealed tokens closed set confirmed
  [ ] TOKEN TRACE CONFIRMATION has 4 rows; three-way status vocabulary; DROPPED count stated
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS, INERTIA CONTINUITY BRIDGE declared.
  If AMEND invalidated Phase 3: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |
[Tier 1 rows]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete. No Tier 2 voice before this line.

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable]         | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |
[Tier 2 rows]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete. No Tier 3 voice before this line.

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Endorsement.          | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |
[Tier 3 rows]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |
[repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to this
  commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

PHASE-4-ENTER: Precondition: PHASE-3-COMMIT present. Entering Phase 4.

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

PHASE-5-ENTER: Precondition: PHASE-4-COMMIT present. Entering Phase 5.

### DECISIONS

| Field                        | Value                                              |
|------------------------------|----------------------------------------------------|
| Verdict                      | ___                                                |
| Conditions for full approval | ___                                                |
| Re-entry owner               | ___                                                |
| Re-entry trigger             | ___                                                |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |
[one row per item]

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- All sections complete. Owner and Trigger present if not APPROVED.
  Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

## CO-DEPENDENCY PREAMBLE

The following criterion dependencies are declared before evaluation begins.
Verify prerequisite criteria are satisfied before evaluating dependent criteria.

| Dependent criterion                           | REQUIRES:  | Nature of dependency                                                              |
|-----------------------------------------------|------------|-----------------------------------------------------------------------------------|
| C-36 (three-way CONFIRMATION status)          | REQUIRES: C-35 | C-36 row count = N invariant is unenforceable without C-35's closed-set manifest. Vocabulary (CONSUMED/NOT-APPLICABLE/DROPPED) may be present; count reconciliation requires the explicit closed set. A skill passing C-36 vocabulary without C-35 manifest achieves PARTIAL at best. |
| INERTIA CONTINUITY BRIDGE YES-affirmation     | REQUIRES: [Phase 2 TIER SORT complete] | YES is only valid if TIER SORT table has been printed and each participant's orientation verified. Affirmation without TIER SORT review is structurally unverified. |

---

**PHASE 0 fill rules:**

LOAD charter. PRINT participant table. PRINT PHASE-0-COMMIT with Sealed tokens field.
  FAILS: Sealed tokens field absent -- C-35
  FAILS: Committee Type declared as non-standard label -- C-01

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D opening with full token label.
  FAILS: parenthesized letter instead of full token -- C-27
  FAILS: abbreviated label -- C-27

WRITE: ## INERTIA RECORD table. WRITE: INERTIA INVARIANT.
  FAILS: bare token, no anchor content -- C-35
  FAILS: INERTIA INVARIANT missing modification prohibition -- C-35

PRINT: PHASE-1-COMMIT with Sealed tokens closed set [N=4] and bidirectionality clause.
  Note: this closed set is the prerequisite for C-36 evaluation (see CO-DEPENDENCY PREAMBLE).
  FAILS: bidirectionality clause one direction only -- C-45

---

**PHASE 2 fill rules:**

ASSIGN tiers. Print TIER SORT table.
SORT-CHECK: print Test and Result; loop until NO.
  FAILS: correct table without SORT-CHECK gate -- C-25

TOKEN TRACE CONFIRMATION fill rules:

REQUIRES: C-35
  Verify PHASE-1-COMMIT contains an explicit Sealed tokens enumeration (closed set) before
  evaluating TOKEN TRACE CONFIRMATION. If PHASE-1-COMMIT Sealed tokens are absent or
  abbreviated ("findings A-D"), the row count = N invariant below is unenforceable.
  Scoring C-36 as PASS without C-35's closed set is a false positive.

PRINT: four-row confirmation table.
ASSIGN: CONSUMED | NOT-APPLICABLE | DROPPED.
  NOT-APPLICABLE: cite specific charter constraint.
  DROPPED: invoke REPAIR RULE -- reopen Phase 1.
PRINT: CONFIRMATION INVARIANT with Row count = 4.
  FAILS: fewer than 4 rows -- C-36
  FAILS: binary vocabulary -- C-36

---

**INERTIA CONTINUITY BRIDGE fill rule:**

REQUIRES: [Phase 2 TIER SORT complete]
  Verify TIER SORT table is printed and all participant orientations are assigned before
  evaluating whether the YES affirmation is correct. Affirmation without completed TIER SORT
  is structurally unverifiable.

INSPECT: TIER SORT for inertia-oriented Tier 1/Tier 2 participant.
CONFIRM YES or NO; inject Inertia-Advocate if NO.
  FAILS: Phase 3 begins without INERTIA CONTINUITY BRIDGE -- C-46
  FAILS: YES declared without qualifying participant -- C-49

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE: TIER-N-SEQUENCE-COMMIT gates required before next tier begins.
  FAILS: Tier N+1 voice before TIER-N-SEQUENCE-COMMIT -- C-02
  FAILS: TIER-N-SEQUENCE-COMMIT absent even with correct order -- C-25

VALIDATE STANCE cell: [BLOCK / CONDITION / APPROVE] -- no qualification.
  FAILS: stance in prose only -- C-02

Tier 1: INERTIA-FINDING cite cell required.
Tier 2: specific condition required; "address concerns" fails -- C-07.
Tier 3: RESPONDS-TO named concern; CITE label in cite cell.

WRITE: ## STANCE MANIFEST table. WRITE: STANCE INVARIANT.
  FAILS: STANCE INVARIANT absent -- C-47
PRINT: PHASE-3-COMMIT with bidirectionality clause.
  FAILS: one direction only -- C-45

---

**PHASE 4 fill rules:**

TALLY from ## STANCE MANIFEST token column only. OUTCOME from TALLY rules.

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions, Re-entry Owner and Trigger.
  FAILS: Owner or Trigger absent when verdict not APPROVED -- C-23
ACTION ITEMS: all three columns required.
  FAILS: Owner Role or Deadline cell empty -- C-04
DISSENTING OPINIONS: one row per CONDITION/BLOCK stance.
  FAILS: CONDITION/BLOCK holder has no dissent row -- C-05

---

**AMEND fill rules (C-30, C-33, C-34):**

AMEND ROUTING TABLE:
  | Add attendee | Phase 0, Phase 3 | Phase 0 -> Phase 3+ |
  | Change scope | Phase 0 -> Phase 5 | Full |
  | Change type  | Phase 0 -> Phase 5 | Full |

RECOMMIT MANIFEST: after each invalidated phase re-executes.
  FAILS: phase resumes without RECOMMIT MANIFEST -- C-34
  FAILS: downstream phase gates on v1 seal after AMEND -- C-34
```

---

## V-04 -- Combination: Dual-Enforcement + FAILS Template (V-01 + V-02)

**Axis:** Dual-enforcement pairing (C-37) + FAILS syntax template (C-38)
**Hypothesis:** Pairing ROLE VOICE GUARD + OWNERSHIP TALLY with the canonical FAILS template
addresses the two most orthogonal R13 structural gaps simultaneously. ROLE VOICE GUARD and
OWNERSHIP TALLY enforce correctness properties at runtime simulation sites (Phases 3 and 5).
The FAILS template enforces annotation completeness at fill-rule definition sites throughout
STEP 2. No interaction effects -- they operate at different structural levels. Together they
close C-37 and C-38 without requiring the REQUIRES: annotation apparatus of C-39.

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
  FAIL: "If there is no metric cited, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO line, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named alternatives and a selected option.
  FAIL: "If there are no named alternatives, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: participant speaking from wrong role orientation = C-02 miss.

Read this block fully before beginning.

---

## FAILS SYNTAX TEMPLATE

Canonical form for ALL fill-rule FAILS entries in STEP 2:

  FAILS [C-NN]: <description of what fails and why>

[C-NN] is a POSITIONAL REQUIRED FIELD. A FAILS entry without [C-NN] is syntactically
malformed. Entries deviating from this template are C-38 misses during scoring.

Examples:
  CORRECT:   FAILS [C-01]: committee type absent -- type not declared using recognized label
  CORRECT:   FAILS [C-02]: role voice mismatch -- PM raises deployment topology as primary
  CORRECT:   FAILS [C-04]: action item owner absent -- Owner Role cell empty
  CORRECT:   FAILS [C-37]: ROLE VOICE GUARD absent -- single-mechanism C-02 enforcement only
  MALFORMED: FAILS: committee type absent              (missing [C-NN])
  MALFORMED: FAILS (C-01): committee type absent        (parenthesized, not positional)

This template applies to all FAILS entries below. Deviations are C-38 misses.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one if
no charter inertia owner exists.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-04: Dual-Enforcement + FAILS Template) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |
[repeat per participant]

PHASE-0-EXIT:
  [ ] Committee Type declared using recognized label
  [ ] Agenda Item stated; Charter Source named
  [ ] Participant roster complete
  All checks: ___ [PASS / FAIL]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present, EXIT checks PASS.
  If AMEND invalidated Phase 1: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 1.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not anticipate?
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

PHASE-1-EXIT:
  [ ] Each INERTIA-FINDING opens with full token label
  [ ] ## INERTIA RECORD table populated with content anchors
  [ ] INERTIA INVARIANT present with commit reference and prohibition
  [ ] Sealed tokens enumeration prepared [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS, N=4 sealed tokens available.
  If AMEND invalidated Phase 2: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 2.

### TIER SORT

| Role              | Tier  | Rationale                                          |
|-------------------|-------|----------------------------------------------------|
| ___               | ___   | ___                                                |

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

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___

PHASE-2-EXIT:
  [ ] TIER SORT table complete; SORT-CHECK printed
  [ ] TOKEN TRACE CONFIRMATION has 4 rows; three-way vocabulary; DROPPED stated
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## ROLE VOICE GUARD

[C-37 Mechanism 2 for C-02 -- independent of TIER-N-SEQUENCE-COMMIT gate]

| Role              | In-scope domain                        | Forbidden-topic scope                  |
|-------------------|----------------------------------------|----------------------------------------|
| ___               | ___                                    | ___                                    |
[repeat per participant]

ROLE VOICE SEAL: [locked] -- participant forbidden-topic scopes committed. Any Phase 3 voice
  leading with a forbidden topic = C-02 miss, detectable here independent of tier gate status.
  | ENFORCE: terminal position in ROLE VOICE GUARD.

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS, INERTIA CONTINUITY BRIDGE and
  ROLE VOICE GUARD both sealed.
  If AMEND invalidated Phase 3: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |
[Tier 1 rows]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete. No Tier 2 voice before this line.
  Stances committed: [list Tier 1 roles and STANCE tokens].

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable]         | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |
[Tier 2 rows]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete. No Tier 3 voice before this line.
  Stances committed: [list Tier 2 roles and STANCE tokens].

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Endorsement.          | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |
[Tier 3 rows]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- entries may not be revised without reopening.

PHASE-3-EXIT:
  [ ] Tier 1 rows all before TIER-1-SEQUENCE-COMMIT; Tier 2 before TIER-2-SEQUENCE-COMMIT
  [ ] Each voice complies with ROLE VOICE GUARD forbidden-topic scope
  [ ] Tier 1 INERTIA-FINDING cite cells populated; Tier 2 Condition cells specific
  [ ] Tier 3 RESPONDS-TO and CITE cells populated
  [ ] At least one CONDITION or BLOCK in ## STANCE MANIFEST
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to this
  commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY from ## STANCE MANIFEST only. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

PHASE-4-ENTER: Precondition: PHASE-3-COMMIT present. Entering Phase 4.

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

PHASE-5-ENTER: Precondition: PHASE-4-COMMIT present. Entering Phase 5.

### DECISIONS

| Field                        | Value                                              |
|------------------------------|----------------------------------------------------|
| Verdict                      | ___                                                |
| Conditions for full approval | ___                                                |
| Re-entry owner               | ___                                                |
| Re-entry trigger             | ___                                                |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |
[one row per item]

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].
  [C-37 Mechanism 2 for C-04 -- independent of Owner Role column]
  ENFORCE: TALLY count must equal ACTION ITEMS row count.

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- All sections complete. Owner and Trigger present if not APPROVED.
  Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

NOTE: All FAILS entries conform to `FAILS [C-NN]: <description>`. Deviations are C-38 misses.

---

**PHASE 0 fill rules:**

LOAD charter. PRINT participant table. PRINT PHASE-0-COMMIT.
  FAILS [C-35]: Sealed tokens field absent from PHASE-0-COMMIT
  FAILS [C-01]: Committee Type declared as unlabeled or non-standard

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D with full token labels.
  FAILS [C-27]: parenthesized letter used instead of full token
  FAILS [C-27]: abbreviated label used

WRITE: ## INERTIA RECORD table. WRITE: INERTIA INVARIANT.
  FAILS [C-35]: bare token in INERTIA RECORD table
  FAILS [C-35]: INERTIA INVARIANT missing prohibition element

PRINT: PHASE-1-COMMIT [N=4] with bidirectionality clause.
  FAILS [C-45]: one direction only in bidirectionality clause

---

**PHASE 2 fill rules:**

ASSIGN tiers. SORT-CHECK gate.
  FAILS [C-25]: correct table without SORT-CHECK gate

TOKEN TRACE CONFIRMATION:
PRINT: four-row table. ASSIGN: CONSUMED | NOT-APPLICABLE | DROPPED.
  FAILS [C-36]: fewer than 4 rows
  FAILS [C-36]: binary vocabulary
  DROPPED: invoke REPAIR RULE.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT TIER SORT. Confirm YES or NO. Inject if NO.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE
  FAILS [C-49]: YES declared without qualifying participant

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

PRINT: ROLE VOICE GUARD table -- one row per participant.
ASSIGN: In-scope domain from charter. Forbidden-topic scope: what this role must not lead.
PRINT: ROLE VOICE SEAL.
  FAILS [C-02]: Phase 3 voice leads with forbidden topic per ROLE VOICE GUARD -- detected
    independently of tier gate: tier gate fires on ordering; ROLE VOICE GUARD fires on domain
  FAILS [C-37]: ROLE VOICE GUARD absent -- only one C-02 enforcement mechanism present
  FAILS [C-37]: forbidden-topic scope cells left empty -- guard present but unenforceable

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE [C-37 Mechanism 1 for C-02]:
  FAILS [C-02]: Tier N+1 voice row before TIER-N-SEQUENCE-COMMIT
  FAILS [C-25]: tier ordering correct but TIER-N-SEQUENCE-COMMIT absent

STANCE cell: [BLOCK / CONDITION / APPROVE] only.
  FAILS [C-02]: stance in prose only; no STANCE field in table row

Tier 1: INERTIA-FINDING cite required.
Tier 2: specific condition required; "address concerns" fails.
  FAILS [C-07]: vague condition in Tier 2 row
Tier 3: RESPONDS-TO named concern; CITE label present.

WRITE: ## STANCE MANIFEST table. WRITE: STANCE INVARIANT.
  FAILS [C-47]: STANCE INVARIANT absent
PRINT: PHASE-3-COMMIT with bidirectionality clause.
  FAILS [C-45]: one direction only

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions, Re-entry Owner and Trigger.
  FAILS [C-23]: Owner or Trigger absent when verdict not APPROVED

ACTION ITEMS: all three columns required.
  FAILS [C-04]: Owner Role cell empty -- C-04 [Mechanism 1: column structure]
  FAILS [C-04]: Deadline cell absent

OWNERSHIP TALLY [C-37 Mechanism 2 for C-04]:
  FAILS [C-04]: TALLY count < ACTION ITEMS row count -- anonymous item detected via count gap
    [C-37: Owner column shows empty cell; TALLY shows Named owners < total: two signals]
  FAILS [C-37]: OWNERSHIP TALLY absent -- single-mechanism C-04 enforcement only

DISSENTING OPINIONS: one row per CONDITION/BLOCK stance.
  FAILS [C-05]: CONDITION/BLOCK holder missing dissent row

---

**AMEND fill rules:**

RECOMMIT MANIFEST after each invalidated phase re-executes.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND
```

---

## V-05 -- Full Integration (V-01 + V-02 + V-03, all R13 axes)

**Axis:** Dual-enforcement (C-37) + FAILS syntax template (C-38) + REQUIRES: annotations (C-39)
**Hypothesis:** All three R13 structural additions applied simultaneously on the R12 V-05
baseline. This is the only variation where:
- A C-02 violation produces detectable signals from both ROLE VOICE GUARD and TIER-N-SEQUENCE-COMMIT independently
- A C-04 violation produces detectable signals from both Owner column and OWNERSHIP TALLY independently
- A FAILS annotation missing [C-NN] is structurally malformed, not merely suboptimal
- A C-36 PASS without C-35's closed-set manifest is blocked as a false positive by the REQUIRES: declaration

The test for V-05: remove any one mechanism -- a violation escapes. All four mechanisms are load-bearing.

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
  FAIL: "If there is no metric cited, you have not done a ROB." -- C-01 miss

SHIPROOM: Produce a binary GO / NO-GO decision with blocking condition if NO-GO.
  FAIL: "If there is no GO/NO-GO line, you have not done a shiproom." -- C-01 miss

ARCH-BOARD: Produce an ADR with named alternatives and a selected option.
  FAIL: "If there are no named alternatives, you have not done an arch-board." -- C-01 miss

COMMON ROLE FAIL: participant speaking from wrong role orientation = C-02 miss.
  TWO-MECHANISM CHECK: role voice violations are caught by ROLE VOICE GUARD (domain
  mismatch) AND by TIER-N-SEQUENCE-COMMIT (ordering enforcement). Both must be satisfied.

Read this block fully before beginning.

---

## FAILS SYNTAX TEMPLATE

Canonical form for ALL fill-rule FAILS entries in STEP 2:

  FAILS [C-NN]: <description of what fails and why>

[C-NN] is a POSITIONAL REQUIRED FIELD. A FAILS entry without [C-NN] is syntactically
malformed, not merely suboptimal. Entries deviating from this template are C-38 misses.

Examples:
  CORRECT:   FAILS [C-01]: committee type absent -- recognized label not declared
  CORRECT:   FAILS [C-02]: role voice mismatch -- PM raises deployment topology as primary
  CORRECT:   FAILS [C-04]: action item owner absent -- Owner Role cell empty in table
  CORRECT:   FAILS [C-37]: ROLE VOICE GUARD absent -- single-mechanism C-02 enforcement only
  CORRECT:   FAILS [C-38]: FAILS entry missing [C-NN] -- template violation, syntactically malformed
  CORRECT:   FAILS [C-39]: REQUIRES: C-35 absent before TOKEN TRACE CONFIRMATION fill rule
  MALFORMED: FAILS: committee type absent              (missing [C-NN])
  MALFORMED: committee type absent -- C-01 miss         ([C-NN] at end, not positional)

This template applies to all FAILS entries below.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one if
no charter inertia owner exists.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-05: Full R13 Integration) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |
[repeat per participant]

PHASE-0-EXIT:
  [ ] Committee Type declared using recognized label (ROB / shiproom / arch-board)
  [ ] Agenda Item stated; Charter Source named or fallback declared
  [ ] Participant roster complete
  All checks: ___ [PASS / FAIL]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  Sealed tokens: Committee-Type, Agenda-Item, Charter-Source, Participant-roster
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INERTIA INVESTIGATION

PHASE-1-ENTER:
  Precondition: PHASE-0-COMMIT present, EXIT checks PASS.
  If AMEND invalidated Phase 1: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 1.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not anticipate?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2. Continue until YES.]

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
  [ ] Each INERTIA-FINDING opens with full token label
  [ ] ## INERTIA RECORD table populated with content anchors (no placeholders)
  [ ] INERTIA INVARIANT present with commit reference and modification prohibition
  [ ] Sealed tokens enumeration prepared as explicit closed set [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  [This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS.
  C-35 pre-check: PHASE-1-COMMIT Sealed tokens enumerated as explicit closed set? [YES / NO]
    If NO: halt -- TOKEN TRACE CONFIRMATION row count = N is unenforceable without it.
  If AMEND invalidated Phase 2: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 2.

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
  Reassignment (if YES): ___

### TOKEN TRACE CONFIRMATION

[REQUIRES: C-35 -- row count = N is enforced by the explicit closed set in PHASE-1-COMMIT.
 Without that closed set, a dropped token produces no visible absence in this table.]

| Token              | Status              | Tier Sort usage or charter citation       |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] TIER SORT complete; SORT-CHECK printed with explicit Result
  [ ] C-35 pre-check at PHASE-2-ENTER confirmed YES
  [ ] TOKEN TRACE CONFIRMATION has 4 rows; three-way status; DROPPED count stated
  [ ] DROPPED = 0 or REPAIR RULE invoked
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

[REQUIRES: Phase 2 TIER SORT complete -- YES affirmation requires completed TIER SORT table
 with all participant orientations verified before this check can be evaluated correctly.]

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective /
                                  NO -- Inertia-Advocate INJECTED]

---

## ROLE VOICE GUARD

[C-37 Mechanism 2 for C-02 -- independent of TIER-N-SEQUENCE-COMMIT gate below]

| Role              | In-scope domain                        | Forbidden-topic scope                  |
|-------------------|----------------------------------------|----------------------------------------|
| ___               | ___                                    | ___                                    |
[repeat per participant]

ROLE VOICE SEAL: [locked] -- participant domains and forbidden-topic scopes committed.
  Phase 3 voice leading with a forbidden topic = C-02 miss, detectable from this table
  independently of tier gate status.
  [C-37: two mechanisms for C-02 -- ROLE VOICE SEAL (domain scope) + TIER-N-SEQUENCE-COMMIT
   (ordering). A C-02 violation produces a detectable signal from both independently.]
  | ENFORCE: terminal position -- NO ROLE VOICE GUARD CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present, EXIT checks PASS.
  INERTIA CONTINUITY BRIDGE declared? [YES / NO] -- halt if NO.
  ROLE VOICE GUARD sealed? [YES / NO] -- halt if NO.
  If AMEND invalidated Phase 3: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |
[Tier 1 rows -- all must complete before TIER-1-SEQUENCE-COMMIT]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete.
  Stances committed: [list Tier 1 roles and STANCE tokens].
  No Tier 2 voice may appear before this line.
  [C-37 Mechanism 1 for C-02: ordering enforcement. Mechanism 2 is ROLE VOICE SEAL above.]
  | ENFORCE: terminal position in Tier 1 block.

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable required]| INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |
[Tier 2 rows]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete.
  Stances committed: [list Tier 2 roles and STANCE tokens].
  No Tier 3 voice may appear before this line.
  | ENFORCE: terminal position in Tier 2 block.

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Primary endorsement.  | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |
[Tier 3 rows]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |
[repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] All Tier 1 rows before TIER-1-SEQUENCE-COMMIT; all Tier 2 before TIER-2-SEQUENCE-COMMIT
  [ ] Each voice complies with ROLE VOICE GUARD forbidden-topic scope
  [ ] Tier 1 INERTIA-FINDING cite cells populated; Tier 2 Condition cells specific
  [ ] Tier 3 RESPONDS-TO and CITE cells populated
  [ ] At least one CONDITION or BLOCK in ## STANCE MANIFEST
  [ ] STANCE INVARIANT present; bidirectionality clause prepared
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order with
  TIER-1-SEQUENCE-COMMIT and TIER-2-SEQUENCE-COMMIT both present.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to this
  commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only.
  Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

PHASE-4-ENTER:
  Precondition: PHASE-3-COMMIT present, EXIT checks PASS.
  If AMEND invalidated Phase 4: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 4.

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

PHASE-5-ENTER:
  Precondition: PHASE-4-COMMIT present.
  If AMEND invalidated Phase 5: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 5.

### DECISIONS

| Field                        | Value                                              |
|------------------------------|----------------------------------------------------|
| Verdict                      | ___                                                |
| Conditions for full approval | ___                                                |
| Re-entry owner               | ___                                                |
| Re-entry trigger             | ___                                                |

### ACTION ITEMS

| Owner Role | Specific action                        | Deadline |
|------------|----------------------------------------|----------|
| ___        | ___                                    | ___      |
[one row per item]

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].
  [C-37 Mechanism 2 for C-04 -- independent of Owner Role column.
   C-37: two mechanisms for C-04 -- Owner column (empty cell) + TALLY (count gap).
   A missing owner produces a detectable signal from both independently.]
  ENFORCE: TALLY count must equal ACTION ITEMS row count. Anonymous items must be 0.

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-EXIT:
  [ ] Verdict matches OUTCOME from Phase 4 exactly
  [ ] Conditions stated as specific deliverables
  [ ] Owner and Trigger present if verdict not APPROVED
  [ ] Every action item: Owner Role, specific action, deadline -- all populated
  [ ] OWNERSHIP TALLY count matches ACTION ITEMS row count; anonymous items = 0
  [ ] Every CONDITION/BLOCK role has a dissent row citing INERTIA-FINDING-* label
  All checks: ___ [PASS / FAIL]

PHASE-5-COMMIT: [locked] -- EXIT checks PASS. All sections complete.
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

NOTE: All FAILS entries conform to `FAILS [C-NN]: <description>`. Deviations are C-38 misses.

---

## CO-DEPENDENCY PREAMBLE

Verify prerequisite criteria before evaluating dependent criteria:

| Dependent criterion                           | REQUIRES:  | Nature of dependency                                                              |
|-----------------------------------------------|------------|-----------------------------------------------------------------------------------|
| C-36 (three-way CONFIRMATION status)          | REQUIRES: C-35 | C-36 row count = N is unenforceable without C-35's explicit closed-set manifest. Vocabulary presence does not establish count reconciliation. |
| INERTIA CONTINUITY BRIDGE YES-affirmation     | REQUIRES: [Phase 2 TIER SORT complete] | YES is only verifiable after all participant orientations are assigned in TIER SORT. Affirmation without completed table is unverified. |

---

**PHASE 0 fill rules:**

LOAD charter. PRINT participant table. PRINT PHASE-0-COMMIT with Sealed tokens field.
  FAILS [C-35]: Sealed tokens field absent from PHASE-0-COMMIT
  FAILS [C-01]: Committee Type declared as non-standard or unlabeled

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D with full token labels.
  FAILS [C-27]: parenthesized letter `(a)` instead of full token label
  FAILS [C-27]: abbreviated `Finding A:` instead of `INERTIA-FINDING-A:`

GATE-N retry: rerun all four findings if INERTIA-FINDING-D is obvious. Continue until YES.

WRITE: ## INERTIA RECORD table with content anchors (no placeholders or bare labels).
  FAILS [C-35]: bare token with no anchor in INERTIA RECORD
  FAILS [C-35]: INERTIA INVARIANT absent or missing modification prohibition

PRINT: PHASE-1-COMMIT with Sealed tokens as explicit closed set [N=4] and bidirectionality.
  Note: this closed set is the C-35 prerequisite for C-36 evaluation (CO-DEPENDENCY PREAMBLE).
  FAILS [C-45]: bidirectionality clause states only one direction

---

**PHASE 2 fill rules:**

ASSIGN tiers by charter orientation. Print TIER SORT table.
SORT-CHECK: print Test and Result; loop until NO.
  FAILS [C-25]: correct table present but SORT-CHECK gate absent

TOKEN TRACE CONFIRMATION fill rules:

REQUIRES: C-35
  Verify PHASE-1-COMMIT Sealed tokens are an explicit closed set before scoring C-36.
  If Sealed tokens are absent or abbreviated, row count = N is unenforceable regardless
  of vocabulary presence. Scoring C-36 as PASS without C-35 satisfied is a false positive.
  A skill that passes C-36 vocabulary without a C-35 manifest achieves PARTIAL at best.

PRINT: four-row confirmation table. ASSIGN: CONSUMED | NOT-APPLICABLE | DROPPED.
  NOT-APPLICABLE: cite specific charter constraint -- vague "not relevant" fails.
  DROPPED: invoke REPAIR RULE -- reopen Phase 1 before Phase 2 closes.
  FAILS [C-36]: fewer than 4 rows in confirmation table
  FAILS [C-36]: binary CONFIRMED/DROPOUT vocabulary used
  FAILS [C-39]: REQUIRES: C-35 annotation absent before TOKEN TRACE CONFIRMATION fill rule

---

**INERTIA CONTINUITY BRIDGE fill rule:**

REQUIRES: [Phase 2 TIER SORT complete]
  Verify TIER SORT table is complete and all orientations assigned before evaluating
  whether YES affirmation is correct. Affirmation without completed table is structurally
  unverifiable and creates latent C-49 false-positive risk.

INSPECT TIER SORT for inertia-oriented Tier 1/Tier 2 participant.
CONFIRM YES or NO. Inject Inertia-Advocate if NO.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS [C-49]: YES declared when no qualifying participant exists in completed TIER SORT

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

PRINT: ROLE VOICE GUARD table -- one row per participant from Phase 0 roster.
ASSIGN: In-scope domain from charter orientation.
ASSIGN: Forbidden-topic scope -- what this role must NOT lead as primary concern.
  PM: In-scope -- adoption, user value, competitive positioning
      Forbidden -- deployment topology, on-call operational burden
  SRE: In-scope -- reliability, incident surface, on-call burden
       Forbidden -- product vision, business strategy, market positioning
  Architect: In-scope -- design trade-offs, technical debt, component boundaries
             Forbidden -- customer NPS, market sizing

PRINT: ROLE VOICE SEAL.
  FAILS [C-02]: Phase 3 voice leads with forbidden topic per ROLE VOICE GUARD
    [C-37: two independent detections -- ROLE VOICE GUARD fires on domain; TIER-N-SEQUENCE-COMMIT
     fires on ordering. Removing either mechanism degrades C-02 coverage]
  FAILS [C-37]: ROLE VOICE GUARD absent -- only TIER-N-SEQUENCE-COMMIT enforces C-02
  FAILS [C-37]: forbidden-topic scope cells empty -- guard present but non-enforceable

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE [C-37 Mechanism 1 for C-02]:
  FAILS [C-02]: Tier N+1 voice row appears before TIER-N-SEQUENCE-COMMIT
  FAILS [C-25]: tier ordering correct but TIER-N-SEQUENCE-COMMIT absent

VALIDATE STANCE cell: [BLOCK / CONDITION / APPROVE] only.
  FAILS [C-02]: stance embedded in prose only; no STANCE field in table row
  FAILS [C-02]: qualified token like `CONDITION (pending)` in STANCE cell

Tier 1: INERTIA-FINDING cite cell required.
Tier 2: specific condition required; "address concerns" fails.
  FAILS [C-07]: vague condition in Tier 2 row Condition cell
Tier 3: RESPONDS-TO named concern; CITE label in cite cell.

VALIDATE: at least one CONDITION or BLOCK; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST table. WRITE: STANCE INVARIANT.
  FAILS [C-47]: STANCE INVARIANT absent from ## STANCE MANIFEST

PRINT: PHASE-3-COMMIT with bidirectionality clause.
  FAILS [C-45]: bidirectionality clause states only one direction

---

**PHASE 4 fill rules:**

TALLY: count STANCE-TOKEN column in ## STANCE MANIFEST only; do not re-parse prose.
OUTCOME: all APPROVE -> APPROVED; any CONDITION no BLOCK -> APPROVED WITH CONDITIONS;
  any BLOCK -> BLOCKED or DEFERRED.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME. Conditions: specific deliverables only.
REQUIRE (not APPROVED): Owner (named role) and Trigger (named artifact + recipient + authority).
  FAILS [C-23]: Owner or Trigger absent when verdict not APPROVED

ACTION ITEMS: all three columns required per row.
  FAILS [C-04]: Owner Role cell empty [Mechanism 1: column structure makes absence visible]
  FAILS [C-04]: Deadline cell absent

OWNERSHIP TALLY [C-37 Mechanism 2 for C-04]:
  Format: "[N] action items. Named owners: [N]. Anonymous items: [0]."
  VALIDATE: TALLY total = ACTION ITEMS row count; Anonymous items = 0.
  FAILS [C-04]: TALLY Named owners < ACTION ITEMS row count -- anonymous item detected
    [C-37: Owner column shows empty cell; TALLY shows count deficit: two independent signals]
  FAILS [C-37]: OWNERSHIP TALLY absent -- single-mechanism C-04 enforcement only

DISSENTING OPINIONS: one row per CONDITION/BLOCK stance; cite INERTIA-FINDING-* label.
  FAILS [C-05]: CONDITION or BLOCK holder has no dissent row

---

**AMEND fill rules (C-30, C-33, C-34):**

AMEND ROUTING TABLE:
  | Amendment Type           | Invalidates           | Re-execution scope  |
  |--------------------------|----------------------|---------------------|
  | Add attendee             | Phase 0, Phase 3     | Phase 0 -> Phase 3+ |
  | Change scope             | Phase 0 -> Phase 5   | Full re-execution   |
  | Change committee type    | Phase 0 -> Phase 5   | Full re-execution   |
  | Inject role post-Phase 2 | Phase 3 -> Phase 5   | Phase 3 -> Phase 5  |

AMEND-AFFECTED SITES: list each stale table cell before re-execution:
  [Phase -- table -- column -- token -- reason stale]

RECOMMIT MANIFEST (C-34): after each invalidated phase re-executes, before next phase resumes:
  PHASE-[N]-RECOMMIT MANIFEST v[K+1]:
    Delta: cells added: [list], cells removed: [list], cells modified: [list]
    Version: v[K+1] supersedes v[K].
    Gate: downstream phases gate on this manifest only; original v1 seal is insufficient.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND issued
```
