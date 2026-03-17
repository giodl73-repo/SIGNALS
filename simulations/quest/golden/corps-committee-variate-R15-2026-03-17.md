---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 15
rubric_version: 15
---

# corps-committee -- Prompt Variations R15

## Variation Summary

| ID   | Axis                                                                 | Hypothesis |
|------|----------------------------------------------------------------------|------------|
| V-01 | C-42 only — register ambiguity elimination in BEFORE YOU START       | Removing every descriptive sentence from BEFORE YOU START — leaving only imperative fail conditions, halt directives, and enforcement commands — satisfies C-42 where R13 V-05 does not. The test: can every sentence in the block be verified as a command or fail condition with no sentence explaining what a committee type is or does? With V-01, yes. |
| V-02 | C-43 only — fill-rule echo of C-41 annotation                       | Adding a C-41 ECHO line inside the TOKEN TRACE CONFIRMATION fill rule section — explicitly referencing the forward annotation on PHASE-1-COMMIT — creates three-point traceability at a single inspection site. Without the echo, a reviewer evaluating TOKEN TRACE CONFIRMATION must traverse to PHASE-1-COMMIT to find the C-41 annotation; the echo surfaces all three dependency signals at the point of evaluation. BEFORE YOU START is unchanged from R13 V-05 (still descriptive; fails C-42). |
| V-03 | C-42 alternative — BEFORE YOU START as fail-condition table          | Converting BEFORE YOU START into a table with columns [Type / Fail condition / Halt trigger] eliminates descriptive framing by structural constraint: a table cell cannot contain a paragraph-form description. Register ambiguity is eliminated by format choice rather than editorial revision. This tests whether the C-42 requirement is satisfied by a different implementation path than V-01's prose-imperative approach. |
| V-04 | Combination: C-42 + C-43                                            | Pairing pure imperative BEFORE YOU START (C-42) with the TOKEN TRACE CONFIRMATION fill-rule echo (C-43) closes both R14 gaps simultaneously. The two changes operate at independent sites — BEFORE YOU START block vs PHASE 2 fill rules — with no interaction effects. This is the minimum change from R13 V-05 that satisfies both new criteria without adding further structural apparatus. |
| V-05 | Full integration: C-42 + C-43 + self-referential FAILS entries for new criteria | All R15 structural additions on the R13 V-05 baseline, plus: FAILS template extended with self-referential entries for C-42 and C-43, making register-ambiguity violations and missing fill-rule echoes detectable from the template itself. CO-DEPENDENCY PREAMBLE updated to declare the C-43 fill-rule echo as a three-point traceability requirement. This is the only variation where a register-ambiguity violation in BEFORE YOU START, a missing fill-rule echo, a FAILS entry without [C-NN], and a C-36-without-C-35 false positive each produce a structurally detectable signal from independent mechanisms. |

---

## V-01 -- Register Ambiguity Elimination (C-42, single axis)

**Axis:** Strip all descriptive framing from BEFORE YOU START; every sentence imperative
**Hypothesis:** A BEFORE YOU START block containing zero descriptive sentences — no "Produce a
readiness verdict...", no "participant speaking from wrong role..." explainers — satisfies C-42.
The block must speak in one voice throughout: every sentence is either a fail condition
("If there is no metric, you have not done a ROB") or a halt directive. No sentence describes
what a committee type is or what a role does.

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

If there is no metric cited in the discussion: you have not done a ROB. [C-01]
If there is no GO/NO-GO decision line in the verdict: you have not done a shiproom. [C-01]
If there are no named alternatives compared in the output: you have not done an arch-board. [C-01]
If a participant voice leads with a topic outside their charter orientation: C-02 miss. Halt.
If ROLE VOICE GUARD is absent from STEP 2: single-mechanism C-02 enforcement only. [C-37]
If a participant's STANCE token is qualified (e.g., CONDITION (pending)): C-02 miss. Halt.
If OWNERSHIP TALLY is absent from Phase 5 fill rules: single-mechanism C-04 enforcement only. [C-37]
Do not begin the skeleton until every line above is read.

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
=== org:committee SIMULATION -- SKELETON (V-01: Register Ambiguity Elimination) ===

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
| INERTIA CONTINUITY BRIDGE YES-affirmation     | REQUIRES: [Phase 2 TIER SORT complete] | YES is only verifiable after all participant orientations are assigned in TIER SORT. |

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

RECOMMIT MANIFEST after each invalidated phase re-executes.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND issued
```

---

## V-02 -- Fill-Rule Echo of C-41 Annotation (C-43, single axis)

**Axis:** Add C-41 ECHO inside TOKEN TRACE CONFIRMATION fill rules in STEP 2
**Hypothesis:** Adding a C-41 ECHO annotation inside the TOKEN TRACE CONFIRMATION fill rule
section creates three-point traceability at a single inspection site: REQUIRES: C-35 (C-39) +
forward annotation at source (C-41) + echo here (C-43). A reviewer evaluating TOKEN TRACE
CONFIRMATION sees all three dependency signals without traversing to PHASE-1-COMMIT.
BEFORE YOU START is unchanged from R13 V-05 — still contains descriptive framing — so C-42 fails.

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

[Skeleton identical to V-01 skeleton -- omitted for brevity; use V-01 skeleton verbatim]

=== org:committee SIMULATION -- SKELETON (V-02: Fill-Rule C-41 Echo) ===

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

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]

### TOKEN TRACE CONFIRMATION

[REQUIRES: C-35 -- row count = N is enforced by the explicit closed set in PHASE-1-COMMIT.
 Without that closed set, a dropped token produces no visible absence in this table.
 C-41 ECHO: PHASE-1-COMMIT carries the annotation "[This explicit closed set is the
 prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]". Three-point traceability:
 REQUIRES: C-35 here (C-39) + forward annotation at PHASE-1-COMMIT (C-41) + this echo (C-43).
 If C-41 annotation is absent from PHASE-1-COMMIT, the dependency is declared one-sided only;
 this echo does not substitute for the source annotation.]

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
  [ ] C-41 ECHO present in TOKEN TRACE CONFIRMATION header
  [ ] DROPPED = 0 or REPAIR RULE invoked
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

[REQUIRES: Phase 2 TIER SORT complete]

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## ROLE VOICE GUARD

[C-37 Mechanism 2 for C-02 -- independent of TIER-N-SEQUENCE-COMMIT gate below]

| Role              | In-scope domain                        | Forbidden-topic scope                  |
|-------------------|----------------------------------------|----------------------------------------|
| ___               | ___                                    | ___                                    |

ROLE VOICE SEAL: [locked] -- domains and forbidden-topic scopes committed.
  | ENFORCE: terminal position -- NO ROLE VOICE GUARD CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present. INERTIA CONTINUITY BRIDGE declared. ROLE VOICE GUARD sealed.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete. No Tier 2 voice before this line.

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable required]| INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete. No Tier 3 voice before this line.

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Primary endorsement.  | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] -- All voices complete in Tier 1 -> 2 -> 3 order.
  Sealed tokens: [list all role stances by name] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to this
  commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY derives from ## STANCE MANIFEST token count only. Phase 3 closed.
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

| Field                        | Value  |
|------------------------------|--------|
| Verdict                      | ___    |
| Conditions for full approval | ___    |
| Re-entry owner               | ___    |
| Re-entry trigger             | ___    |

### ACTION ITEMS

| Owner Role | Specific action | Deadline |
|------------|-----------------|----------|
| ___        | ___             | ___      |

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].

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

## CO-DEPENDENCY PREAMBLE

| Dependent criterion                           | REQUIRES:  | Nature of dependency |
|-----------------------------------------------|------------|----------------------|
| C-36 (three-way CONFIRMATION status)          | REQUIRES: C-35 | C-36 row count = N unenforceable without C-35 manifest. |
| INERTIA CONTINUITY BRIDGE YES-affirmation     | REQUIRES: [Phase 2 TIER SORT complete] | YES only verifiable after TIER SORT assigned. |

---

**PHASE 0 fill rules:**

LOAD charter. PRINT participant table. PRINT PHASE-0-COMMIT with Sealed tokens.
  FAILS [C-35]: Sealed tokens field absent
  FAILS [C-01]: Committee Type non-standard or unlabeled

---

**PHASE 1 fill rules:**

WRITE: INERTIA-FINDING-A through D with full token labels.
  FAILS [C-27]: parenthesized letter instead of full token label

WRITE: ## INERTIA RECORD with content anchors. WRITE: INERTIA INVARIANT.
  FAILS [C-35]: INERTIA INVARIANT absent or missing modification prohibition

PRINT: PHASE-1-COMMIT with Sealed tokens closed set [N=4] and bidirectionality.
  Note: this closed set is the C-35 prerequisite for C-36; C-41 annotation present above.
  FAILS [C-45]: bidirectionality clause one direction only

---

**PHASE 2 fill rules:**

SORT-CHECK: print Test and Result; loop until NO.
  FAILS [C-25]: SORT-CHECK gate absent

TOKEN TRACE CONFIRMATION fill rules:

REQUIRES: C-35
  Verify PHASE-1-COMMIT Sealed tokens are an explicit closed set before scoring C-36.

C-41 ECHO: PHASE-1-COMMIT annotation "[This explicit closed set is the prerequisite for C-36
  TOKEN TRACE CONFIRMATION row count = 4]" must be present. Three-point traceability:
  (1) REQUIRES: C-35 here [C-39] + (2) annotation at PHASE-1-COMMIT [C-41] + (3) this echo [C-43].
  FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no echo of C-41 annotation
  FAILS [C-41]: PHASE-1-COMMIT contains no forward annotation referencing C-36 row count

PRINT: four-row confirmation table. ASSIGN: CONSUMED | NOT-APPLICABLE | DROPPED.
  FAILS [C-36]: fewer than 4 rows
  FAILS [C-36]: binary vocabulary
  FAILS [C-39]: REQUIRES: C-35 annotation absent

---

**INERTIA CONTINUITY BRIDGE fill rule:**

REQUIRES: [Phase 2 TIER SORT complete]
INSPECT for inertia-oriented Tier 1/Tier 2 participant. CONFIRM YES or NO.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE
  FAILS [C-49]: YES declared without qualifying participant

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

PRINT ROLE VOICE GUARD table. ASSIGN In-scope and Forbidden-topic scope per role.
PRINT ROLE VOICE SEAL.
  FAILS [C-02]: Phase 3 voice leads with forbidden topic
  FAILS [C-37]: ROLE VOICE GUARD absent
  FAILS [C-37]: forbidden-topic scope cells empty

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE [C-37 Mechanism 1 for C-02]:
  FAILS [C-02]: Tier N+1 voice before TIER-N-SEQUENCE-COMMIT
  FAILS [C-25]: ordering correct but gate absent

STANCE cell: [BLOCK / CONDITION / APPROVE] only.
  FAILS [C-02]: stance in prose; no STANCE field

Tier 1: INERTIA-FINDING cite required. Tier 2: specific condition required.
  FAILS [C-07]: vague Tier 2 condition
Tier 3: RESPONDS-TO + CITE required.

WRITE ## STANCE MANIFEST. WRITE STANCE INVARIANT.
  FAILS [C-47]: STANCE INVARIANT absent
PRINT PHASE-3-COMMIT with bidirectionality.
  FAILS [C-45]: one direction only

---

**PHASE 4 fill rules:**

TALLY from ## STANCE MANIFEST token column only.

---

**PHASE 5 fill rules:**

Verdict matching OUTCOME. Specific condition deliverables.
  FAILS [C-23]: Owner or Trigger absent when not APPROVED

ACTION ITEMS: all three columns.
  FAILS [C-04]: Owner Role empty [Mechanism 1]
  FAILS [C-04]: Deadline absent

OWNERSHIP TALLY [C-37 Mechanism 2 for C-04]:
  FAILS [C-04]: Named owners < row count
  FAILS [C-37]: OWNERSHIP TALLY absent

DISSENTING OPINIONS per CONDITION/BLOCK stance.
  FAILS [C-05]: CONDITION/BLOCK holder missing dissent row

---

**AMEND fill rules:**

RECOMMIT MANIFEST after each invalidated phase.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream gates on v1 seal after AMEND
```

---

## V-03 -- Register Ambiguity Elimination via Table Format (C-42, single axis)

**Axis:** Convert BEFORE YOU START to a fail-condition table; imperative register enforced structurally
**Hypothesis:** A table with columns [Type / Fail condition / C-tag] eliminates descriptive framing
by structural constraint: table cells cannot contain paragraph-form descriptions. Register ambiguity
is eliminated by format, not editorial choice. Every row is a testable fail condition; no row can
be a definition of what the type is. This tests a different implementation path to C-42 than V-01's
prose-imperative approach. Both should pass C-42; the distinction is whether format-enforced register
is superior to editorially-enforced register for downstream variation robustness.

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

| Type       | Fail condition                                                              | C-tag |
|------------|-----------------------------------------------------------------------------|-------|
| ROB        | If there is no metric cited in the discussion, you have not done a ROB.     | C-01  |
| SHIPROOM   | If there is no GO/NO-GO decision line in the verdict, you have not done a shiproom. | C-01 |
| ARCH-BOARD | If there are no named alternatives compared, you have not done an arch-board. | C-01 |
| ALL        | If a participant voice leads with a forbidden-topic, that is a C-02 miss.   | C-02  |
| ALL        | If ROLE VOICE GUARD is absent, C-02 has only one enforcement mechanism.     | C-37  |
| ALL        | If a STANCE token is qualified (e.g., CONDITION (pending)), that is a C-02 miss. | C-02 |
| ALL        | If OWNERSHIP TALLY is absent, C-04 has only one enforcement mechanism.      | C-37  |

Do not begin the skeleton until this table is read completely.

---

## FAILS SYNTAX TEMPLATE

Canonical form for ALL fill-rule FAILS entries in STEP 2:

  FAILS [C-NN]: <description of what fails and why>

[C-NN] is a POSITIONAL REQUIRED FIELD. A FAILS entry without [C-NN] is syntactically
malformed, not merely suboptimal. Entries deviating from this template are C-38 misses.

Examples:
  CORRECT:   FAILS [C-01]: committee type absent -- recognized label not declared
  CORRECT:   FAILS [C-02]: role voice mismatch -- PM raises deployment topology as primary
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

[Skeleton identical to V-01; substitute label "V-03: Register Ambiguity via Table Format"]

=== org:committee SIMULATION -- SKELETON (V-03: Register Ambiguity via Table Format) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |

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

| Token              | One-phrase anchor  |
|--------------------|--------------------|
| INERTIA-FINDING-A  | ___                |
| INERTIA-FINDING-B  | ___                |
| INERTIA-FINDING-C  | ___                |
| INERTIA-FINDING-D  | ___                |

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-EXIT:
  [ ] Each INERTIA-FINDING opens with full token label
  [ ] ## INERTIA RECORD populated with content anchors
  [ ] INERTIA INVARIANT present with commit reference and modification prohibition
  [ ] Sealed tokens enumeration prepared as explicit closed set [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  [This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS.
  C-35 pre-check: Sealed tokens enumerated as explicit closed set? [YES / NO] -- halt if NO.
  Entering Phase 2.

### TIER SORT

| Role | Tier | Rationale |
|------|------|-----------|
| ___  | ___  | ___       |

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]

### TOKEN TRACE CONFIRMATION

[REQUIRES: C-35 -- row count = N enforced by explicit closed set in PHASE-1-COMMIT.]

| Token              | Status | Tier Sort usage or charter citation |
|--------------------|--------|-------------------------------------|
| INERTIA-FINDING-A  | ___    | ___                                 |
| INERTIA-FINDING-B  | ___    | ___                                 |
| INERTIA-FINDING-C  | ___    | ___                                 |
| INERTIA-FINDING-D  | ___    | ___                                 |

CONFIRMATION INVARIANT: Row count = 4. DROPPED count: ___
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] SORT-CHECK printed; C-35 pre-check YES; 4-row CONFIRMATION; DROPPED count stated
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## ROLE VOICE GUARD

| Role | In-scope domain | Forbidden-topic scope |
|------|-----------------|-----------------------|
| ___  | ___             | ___                   |

ROLE VOICE SEAL: [locked] -- domains committed.
  | ENFORCE: terminal position -- NO ROLE VOICE GUARD CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER: Preconditions met. Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role | Tier | STANCE | Primary concern | INERTIA-FINDING cite |
|------|------|--------|-----------------|----------------------|
| ___  | 1    | ___    | ___             | INERTIA-FINDING-___  |

TIER-1-SEQUENCE-COMMIT: [locked] -- Tier 1 complete. No Tier 2 before this line.

### --- TIER 2: CONDITIONALS ---

| Role | Tier | STANCE | Condition: [specific deliverable] | INERTIA-FINDING cite |
|------|------|--------|-----------------------------------|----------------------|
| ___  | 2    | ___    | Condition: ___                    | --                   |

TIER-2-SEQUENCE-COMMIT: [locked] -- Tier 2 complete. No Tier 3 before this line.

### --- TIER 3: ADVOCATES ---

| Role | Tier | STANCE | RESPONDS-TO: "___". Endorsement. | CITE: INERTIA-FINDING-___ |
|------|------|--------|----------------------------------|---------------------------|
| ___  | 3    | ___    | ___                              | INERTIA-FINDING-___       |

## STANCE MANIFEST

| Role | STANCE-TOKEN |
|------|--------------|
| ___  | ___          |

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] -- All voices complete Tier 1 -> 2 -> 3.
  Sealed tokens: [list] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to this
  commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY from ## STANCE MANIFEST token count only. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

### DECISIONS

| Field                        | Value |
|------------------------------|-------|
| Verdict                      | ___   |
| Conditions for full approval | ___   |
| Re-entry owner               | ___   |
| Re-entry trigger             | ___   |

### ACTION ITEMS

| Owner Role | Specific action | Deadline |
|------------|-----------------|----------|
| ___        | ___             | ___      |

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- All sections complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

NOTE: All FAILS entries conform to `FAILS [C-NN]: <description>`. Deviations are C-38 misses.

---

## CO-DEPENDENCY PREAMBLE

| Dependent criterion                       | REQUIRES:  | Nature of dependency |
|-------------------------------------------|------------|----------------------|
| C-36 (three-way CONFIRMATION status)      | REQUIRES: C-35 | Row count = N unenforceable without closed-set manifest. |
| INERTIA CONTINUITY BRIDGE YES-affirmation | REQUIRES: [Phase 2 TIER SORT complete] | YES only verifiable after TIER SORT. |

---

**PHASE 0 fill rules:**

LOAD charter. PRINT participant table. PRINT PHASE-0-COMMIT with Sealed tokens.
  FAILS [C-35]: Sealed tokens field absent
  FAILS [C-01]: Committee Type non-standard

---

**PHASE 1 fill rules:**

WRITE findings with full token labels.
  FAILS [C-27]: abbreviated or parenthesized label

WRITE ## INERTIA RECORD table. WRITE INERTIA INVARIANT.
  FAILS [C-35]: INERTIA INVARIANT absent or missing prohibition

PRINT PHASE-1-COMMIT with closed set [N=4] and bidirectionality.
  Note: closed set is the C-35 prerequisite for C-36 (CO-DEPENDENCY PREAMBLE).
  FAILS [C-45]: one direction only

---

**PHASE 2 fill rules:**

SORT-CHECK: Test + Result; loop until NO.
  FAILS [C-25]: table correct but gate absent

TOKEN TRACE CONFIRMATION fill rules:

REQUIRES: C-35
  Verify PHASE-1-COMMIT Sealed tokens are explicit closed set before scoring C-36.
  If absent or abbreviated, row count = N is unenforceable.

PRINT four-row table. ASSIGN CONSUMED | NOT-APPLICABLE | DROPPED.
  FAILS [C-36]: fewer than 4 rows
  FAILS [C-36]: binary vocabulary
  FAILS [C-39]: REQUIRES: C-35 absent

---

**INERTIA CONTINUITY BRIDGE fill rule:**

REQUIRES: [Phase 2 TIER SORT complete]
INSPECT for inertia-oriented Tier 1/Tier 2 participant. CONFIRM and inject if NO.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE
  FAILS [C-49]: YES without qualifying participant

---

**ROLE VOICE GUARD fill rule:**

PRINT table per participant. ASSIGN In-scope and Forbidden-topic scope.
PRINT ROLE VOICE SEAL.
  FAILS [C-02]: voice leads with forbidden topic
  FAILS [C-37]: ROLE VOICE GUARD absent
  FAILS [C-37]: forbidden-topic cells empty

---

**PHASE 3 fill rules:**

TIER GATE: FAILS [C-02]: Tier N+1 before gate; FAILS [C-25]: gate absent
STANCE: [BLOCK / CONDITION / APPROVE] only. FAILS [C-02]: qualified or prose-only stance
Tier 1: cite required. Tier 2: specific condition. FAILS [C-07]: vague.
Tier 3: RESPONDS-TO + CITE.
STANCE MANIFEST + STANCE INVARIANT. FAILS [C-47]: invariant absent
PHASE-3-COMMIT bidirectionality. FAILS [C-45]: one direction

---

**PHASE 4 fill rules:**

TALLY from ## STANCE MANIFEST token column only.

---

**PHASE 5 fill rules:**

Verdict = OUTCOME. Specific conditions.
  FAILS [C-23]: Owner or Trigger absent when not APPROVED
ACTION ITEMS all three columns.
  FAILS [C-04]: Owner Role empty; FAILS [C-04]: Deadline absent
OWNERSHIP TALLY.
  FAILS [C-04]: Named owners < row count
  FAILS [C-37]: OWNERSHIP TALLY absent
DISSENTING OPINIONS per CONDITION/BLOCK.
  FAILS [C-05]: holder missing dissent row

---

**AMEND fill rules:**

RECOMMIT MANIFEST after each invalidated phase.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream gates on v1 seal after AMEND
```

---

## V-04 -- Combination: Register Ambiguity Elimination + Fill-Rule Echo (C-42 + C-43)

**Axis:** Pure imperative BEFORE YOU START (C-42) + TOKEN TRACE CONFIRMATION fill-rule echo (C-43)
**Hypothesis:** Pairing the two R15 structural additions closes both gaps simultaneously.
The changes are orthogonal: BEFORE YOU START is a preamble block; TOKEN TRACE CONFIRMATION
fill rules are mid-STEP-2 directives. No interaction effects. This is the minimum change from
R13 V-05 that passes both C-42 and C-43 without adding further structural apparatus.

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

If there is no metric cited in the discussion: you have not done a ROB. [C-01]
If there is no GO/NO-GO decision line in the verdict: you have not done a shiproom. [C-01]
If there are no named alternatives compared in the output: you have not done an arch-board. [C-01]
If a participant voice leads with a topic outside their charter orientation: C-02 miss. Halt.
If ROLE VOICE GUARD is absent from STEP 2: single-mechanism C-02 enforcement only. [C-37]
If a participant's STANCE token is qualified (e.g., CONDITION (pending)): C-02 miss. Halt.
If OWNERSHIP TALLY is absent from Phase 5 fill rules: single-mechanism C-04 enforcement only. [C-37]
Do not begin the skeleton until every line above is read.

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

=== org:committee SIMULATION -- SKELETON (V-04: C-42 + C-43 Combination) ===

## PHASE 0 -- COMMITTEE DECLARATION

PHASE-0-ENTER: No preconditions. First phase.

Committee Type: ___
Agenda Item: ___
Charter Source: ___

| Participant Role  | Orientation summary          |
|-------------------|------------------------------|
| ___               | ___                          |

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
  [ ] ## INERTIA RECORD populated with content anchors (no placeholders)
  [ ] INERTIA INVARIANT with commit reference and modification prohibition
  [ ] Sealed tokens enumeration as explicit closed set [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  [This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS.
  C-35 pre-check: PHASE-1-COMMIT Sealed tokens as explicit closed set? [YES / NO] -- halt if NO.
  If AMEND invalidated Phase 2: RECOMMIT MANIFEST v___ present? [YES / NO] -- halt if NO.
  Entering Phase 2.

### TIER SORT

| Role              | Tier  | Rationale (charter orientation -> tier assignment) |
|-------------------|-------|----------------------------------------------------|
| ___               | ___   | ___                                                |

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]

### TOKEN TRACE CONFIRMATION

[REQUIRES: C-35 -- row count = N enforced by explicit closed set in PHASE-1-COMMIT.
 C-41 ECHO: PHASE-1-COMMIT carries the annotation "[This explicit closed set is the
 prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]". Three-point traceability:
 REQUIRES: C-35 here (C-39) + forward annotation at PHASE-1-COMMIT (C-41) + this echo (C-43).]

| Token              | Status              | Tier Sort usage or charter citation       |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] TIER SORT complete; SORT-CHECK with explicit Result
  [ ] C-35 pre-check YES; 4-row CONFIRMATION; three-way vocabulary
  [ ] C-41 ECHO present in TOKEN TRACE CONFIRMATION header
  [ ] DROPPED = 0 or REPAIR RULE invoked
  All checks: ___ [PASS / FAIL]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK NO, CONFIRMATION complete.
  DROPPED count = ___.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

[REQUIRES: Phase 2 TIER SORT complete]

Inertia owner in tier sort: ___ [YES / NO -- Inertia-Advocate INJECTED if NO]

---

## ROLE VOICE GUARD

[C-37 Mechanism 2 for C-02 -- independent of TIER-N-SEQUENCE-COMMIT gate below]

| Role              | In-scope domain                        | Forbidden-topic scope                  |
|-------------------|----------------------------------------|----------------------------------------|
| ___               | ___                                    | ___                                    |

ROLE VOICE SEAL: [locked] -- domains committed.
  [C-37: two mechanisms for C-02 -- ROLE VOICE SEAL + TIER-N-SEQUENCE-COMMIT. Both load-bearing.]
  | ENFORCE: terminal position -- NO ROLE VOICE GUARD CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 -- PARTICIPANT VOICES [Tier 1 -> Tier 2 -> Tier 3]

PHASE-3-ENTER:
  Precondition: PHASE-2-COMMIT present. INERTIA CONTINUITY BRIDGE declared. ROLE VOICE GUARD sealed.
  Entering Phase 3.

### --- TIER 1: CHALLENGERS ---

| Role                | Tier | STANCE    | Primary concern (2-3 sentences)           | INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 1    | ___       | ___                                       | INERTIA-FINDING-___  |

TIER-1-SEQUENCE-COMMIT: [locked] -- Tier 1 complete. No Tier 2 before this line.
  [C-37 Mechanism 1 for C-02. Mechanism 2: ROLE VOICE SEAL above.]

### --- TIER 2: CONDITIONALS ---

| Role                | Tier | STANCE    | Condition: [specific deliverable required]| INERTIA-FINDING cite |
|---------------------|------|-----------|-------------------------------------------|----------------------|
| ___                 | 2    | ___       | Condition: ___                            | --                   |

TIER-2-SEQUENCE-COMMIT: [locked] -- Tier 2 complete. No Tier 3 before this line.

### --- TIER 3: ADVOCATES ---

| Role                | Tier | STANCE    | RESPONDS-TO: "___". Endorsement.          | CITE: INERTIA-FINDING-___ |
|---------------------|------|-----------|-------------------------------------------|---------------------------|
| ___                 | 3    | ___       | ___                                       | INERTIA-FINDING-___       |

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] Tier 1/Tier 2 sequencing gates present; each voice within ROLE VOICE GUARD scope
  [ ] Tier 1 cites; Tier 2 specific conditions; Tier 3 RESPONDS-TO + CITE
  [ ] STANCE INVARIANT present; at least one CONDITION or BLOCK
  All checks: ___ [PASS / FAIL]

PHASE-3-COMMIT: [locked] -- All voices complete Tier 1 -> 2 -> 3.
  Sealed tokens: [list] [N=___]
  Modifications to ## STANCE MANIFEST require updating this commit; modifications to this
  commit require updating ## STANCE MANIFEST.
  Phase 4 TALLY from ## STANCE MANIFEST token count only. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE . ___ CONDITION . ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY printed, OUTCOME declared.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 -- MINUTES

### DECISIONS

| Field                        | Value |
|------------------------------|-------|
| Verdict                      | ___   |
| Conditions for full approval | ___   |
| Re-entry owner               | ___   |
| Re-entry trigger             | ___   |

### ACTION ITEMS

| Owner Role | Specific action | Deadline |
|------------|-----------------|----------|
| ___        | ___             | ___      |

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].
  [C-37 Mechanism 2 for C-04.]

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-COMMIT: [locked] -- All sections complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

NOTE: All FAILS entries conform to `FAILS [C-NN]: <description>`. Deviations are C-38 misses.

---

## CO-DEPENDENCY PREAMBLE

| Dependent criterion                           | REQUIRES:  | Nature of dependency |
|-----------------------------------------------|------------|----------------------|
| C-36 (three-way CONFIRMATION status)          | REQUIRES: C-35 | Row count = N unenforceable without C-35 manifest. |
| INERTIA CONTINUITY BRIDGE YES-affirmation     | REQUIRES: [Phase 2 TIER SORT complete] | YES only verifiable after TIER SORT. |

---

**PHASE 0 fill rules:**

LOAD charter. PRINT participant table. PRINT PHASE-0-COMMIT with Sealed tokens.
  FAILS [C-35]: Sealed tokens field absent
  FAILS [C-01]: Committee Type non-standard or unlabeled

---

**PHASE 1 fill rules:**

WRITE findings with full token labels.
  FAILS [C-27]: parenthesized or abbreviated label

WRITE ## INERTIA RECORD with content anchors. WRITE INERTIA INVARIANT.
  FAILS [C-35]: INERTIA INVARIANT absent or missing prohibition

PRINT PHASE-1-COMMIT with Sealed tokens closed set [N=4] and bidirectionality.
  Note: this closed set is the C-35 prerequisite for C-36 (CO-DEPENDENCY PREAMBLE).
  FAILS [C-45]: bidirectionality clause one direction only

---

**PHASE 2 fill rules:**

SORT-CHECK: Test + Result; loop until NO.
  FAILS [C-25]: correct table but gate absent

TOKEN TRACE CONFIRMATION fill rules:

REQUIRES: C-35
  Verify PHASE-1-COMMIT Sealed tokens are an explicit closed set before scoring C-36.
  If Sealed tokens absent or abbreviated, row count = N is unenforceable.

C-41 ECHO: PHASE-1-COMMIT annotation "[This explicit closed set is the prerequisite for C-36
  TOKEN TRACE CONFIRMATION row count = 4]" must be present at source.
  Three-point traceability: REQUIRES: C-35 here [C-39] + annotation at source [C-41] + echo here [C-43].
  If C-41 annotation absent from PHASE-1-COMMIT, the dependency is one-sided; this echo does
  not substitute for the source annotation.
  FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no echo of C-41 annotation
  FAILS [C-41]: PHASE-1-COMMIT contains no forward annotation referencing C-36 row count

PRINT four-row confirmation table. ASSIGN CONSUMED | NOT-APPLICABLE | DROPPED.
  FAILS [C-36]: fewer than 4 rows
  FAILS [C-36]: binary vocabulary
  FAILS [C-39]: REQUIRES: C-35 annotation absent

---

**INERTIA CONTINUITY BRIDGE fill rule:**

REQUIRES: [Phase 2 TIER SORT complete]
INSPECT for inertia-oriented Tier 1/Tier 2. CONFIRM YES or NO. Inject if NO.
  FAILS [C-46]: Phase 3 begins without INERTIA CONTINUITY BRIDGE
  FAILS [C-49]: YES without qualifying participant

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

PRINT table per participant. ASSIGN In-scope and Forbidden-topic scope.
PRINT ROLE VOICE SEAL.
  FAILS [C-02]: voice leads with forbidden topic
  FAILS [C-37]: ROLE VOICE GUARD absent
  FAILS [C-37]: forbidden-topic cells empty

---

**PHASE 3 fill rules:**

SEQUENTIAL TIER GATE [C-37 Mechanism 1 for C-02]:
  FAILS [C-02]: Tier N+1 before gate
  FAILS [C-25]: ordering correct but gate absent

STANCE: [BLOCK / CONDITION / APPROVE] only.
  FAILS [C-02]: qualified token; FAILS [C-02]: prose-only stance

Tier 1: cite required. Tier 2: specific condition.
  FAILS [C-07]: vague condition
Tier 3: RESPONDS-TO + CITE.

WRITE ## STANCE MANIFEST. WRITE STANCE INVARIANT.
  FAILS [C-47]: STANCE INVARIANT absent

PRINT PHASE-3-COMMIT with bidirectionality.
  FAILS [C-45]: one direction only

---

**PHASE 4 fill rules:**

TALLY from ## STANCE MANIFEST token column only.

---

**PHASE 5 fill rules:**

Verdict = OUTCOME. Specific conditions only.
  FAILS [C-23]: Owner or Trigger absent when not APPROVED

ACTION ITEMS: all three columns.
  FAILS [C-04]: Owner Role empty; FAILS [C-04]: Deadline absent

OWNERSHIP TALLY [C-37 Mechanism 2 for C-04]:
  FAILS [C-04]: Named owners < row count
  FAILS [C-37]: OWNERSHIP TALLY absent

DISSENTING OPINIONS per CONDITION/BLOCK stance.
  FAILS [C-05]: CONDITION/BLOCK holder missing dissent row

---

**AMEND fill rules:**

RECOMMIT MANIFEST after each invalidated phase.
  FAILS [C-34]: resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream gates on v1 seal after AMEND
```

---

## V-05 -- Full Integration: C-42 + C-43 + Self-Referential FAILS for New Criteria

**Axis:** All R15 structural additions on R13 V-05 baseline, plus FAILS template extended with
self-referential entries for C-42 and C-43; CO-DEPENDENCY PREAMBLE updated with C-43 dependency.
**Hypothesis:** All R15 structural additions applied simultaneously. This is the only variation where:
- BEFORE YOU START contains zero descriptive sentences — every line is a fail condition or halt
  directive (C-42)
- TOKEN TRACE CONFIRMATION fill rules carry an explicit C-41 ECHO — three-point traceability
  visible at the evaluation site (C-43)
- FAILS template includes self-referential entries for C-42 and C-43, teaching reviewers what
  to cite when the BEFORE YOU START block contains descriptive framing or the fill-rule echo is absent
- CO-DEPENDENCY PREAMBLE declares C-43 as a fill-rule-level dependency on C-41
- All prior R13 V-05 structure preserved: dual-enforcement (C-37), FAILS template (C-38),
  REQUIRES: annotations (C-39), forward annotation (C-41), self-referential entries (C-40)

The test for V-05: remove any one mechanism and a gap reopens. All mechanisms are load-bearing.

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

If there is no metric cited in the discussion: you have not done a ROB. [C-01]
If there is no GO/NO-GO decision line in the verdict: you have not done a shiproom. [C-01]
If there are no named alternatives compared in the output: you have not done an arch-board. [C-01]
If a participant voice leads with a topic outside their charter orientation: C-02 miss. Halt.
If ROLE VOICE GUARD is absent from STEP 2: single-mechanism C-02 enforcement only. [C-37]
If a participant's STANCE token is qualified (e.g., CONDITION (pending)): C-02 miss. Halt.
If OWNERSHIP TALLY is absent from Phase 5 fill rules: single-mechanism C-04 enforcement only. [C-37]
If the BEFORE YOU START block contains any descriptive sentence (one that explains rather than
  commands): register ambiguity present; block fails C-42. [C-42]
If TOKEN TRACE CONFIRMATION fill rules contain no echo of the PHASE-1-COMMIT C-41 annotation:
  three-point traceability incomplete; fill rules fail C-43. [C-43]
Do not begin the skeleton until every line above is read.

---

## FAILS SYNTAX TEMPLATE

Canonical form for ALL fill-rule FAILS entries in STEP 2:

  FAILS [C-NN]: <description of what fails and why>

[C-NN] is a POSITIONAL REQUIRED FIELD. A FAILS entry without [C-NN] is syntactically
malformed, not merely suboptimal. Entries deviating from this template are C-38 misses.

Examples:
  CORRECT:   FAILS [C-01]: committee type absent -- recognized label not declared
  CORRECT:   FAILS [C-02]: role voice mismatch -- PM raises deployment topology as primary concern
  CORRECT:   FAILS [C-04]: action item owner absent -- Owner Role cell empty in table
  CORRECT:   FAILS [C-37]: ROLE VOICE GUARD absent -- single-mechanism C-02 enforcement only
  CORRECT:   FAILS [C-38]: FAILS entry missing [C-NN] -- template violation, syntactically malformed
  CORRECT:   FAILS [C-39]: REQUIRES: C-35 absent before TOKEN TRACE CONFIRMATION fill rule
  CORRECT:   FAILS [C-42]: BEFORE YOU START contains descriptive sentence -- register not unified
  CORRECT:   FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no C-41 echo -- three-point
             traceability incomplete; C-39 and C-41 both present but echo absent at evaluation site
  MALFORMED: FAILS: committee type absent              (missing [C-NN])
  MALFORMED: committee type absent -- C-01 miss         ([C-NN] at end, not positional)

This template applies to all FAILS entries below. Deviations are C-38 misses.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one if
no charter inertia owner exists.

---

### STEP 1 -- PRINT THIS SKELETON

```
=== org:committee SIMULATION -- SKELETON (V-05: Full R15 Integration) ===

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
  [ ] ## INERTIA RECORD populated with content anchors (no placeholders)
  [ ] INERTIA INVARIANT with commit reference and modification prohibition
  [ ] Sealed tokens enumeration as explicit closed set [N=4]
  All checks: ___ [PASS / FAIL]

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE answered YES.
  Sealed tokens: INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D [N=4]
  [This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]
  Modifications to ## INERTIA RECORD require updating this commit; modifications to this
  commit require updating ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT + TOKEN TRACE CONFIRMATION

PHASE-2-ENTER:
  Precondition: PHASE-1-COMMIT present, EXIT checks PASS.
  C-35 pre-check: PHASE-1-COMMIT Sealed tokens as explicit closed set? [YES / NO] -- halt if NO.
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

[REQUIRES: C-35 -- row count = N enforced by the explicit closed set in PHASE-1-COMMIT.
 Without that closed set, a dropped token produces no visible absence in this table.
 C-41 ECHO: PHASE-1-COMMIT carries the annotation "[This explicit closed set is the
 prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]". Three-point traceability:
 REQUIRES: C-35 here (C-39) + forward annotation at PHASE-1-COMMIT (C-41) + this echo (C-43).
 If C-41 annotation is absent from PHASE-1-COMMIT, the dependency is one-sided; this echo
 does not substitute for the source annotation.]

| Token              | Status              | Tier Sort usage or charter citation       |
|--------------------|---------------------|-------------------------------------------|
| INERTIA-FINDING-A  | ___                 | ___                                       |
| INERTIA-FINDING-B  | ___                 | ___                                       |
| INERTIA-FINDING-C  | ___                 | ___                                       |
| INERTIA-FINDING-D  | ___                 | ___                                       |

CONFIRMATION INVARIANT: Row count = 4 (= PHASE-1-COMMIT N=4). DROPPED count: ___
  Status vocabulary: CONSUMED | NOT-APPLICABLE | DROPPED

PHASE-2-EXIT:
  [ ] TIER SORT complete; SORT-CHECK with explicit Result
  [ ] C-35 pre-check YES; 4-row CONFIRMATION; three-way vocabulary; DROPPED count stated
  [ ] C-41 ECHO present in TOKEN TRACE CONFIRMATION header
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
  Phase 3 voice leading with a forbidden topic = C-02 miss, detectable independently of tier gate.
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
  [ ] Tier 1 cites; Tier 2 specific conditions; Tier 3 RESPONDS-TO + CITE
  [ ] At least one CONDITION or BLOCK; STANCE INVARIANT present
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

OWNERSHIP TALLY: ___ action items. Named owners: ___. Anonymous items: ___ [must be 0].
  [C-37 Mechanism 2 for C-04 -- independent of Owner Role column.
   A missing owner produces a detectable signal from both independently.]
  ENFORCE: TALLY count = ACTION ITEMS row count. Anonymous items = 0.

### DISSENTING OPINIONS

| Role | Objection + INERTIA-FINDING cite | Resolution path | Named authority | Trigger |
|------|----------------------------------|-----------------|-----------------|---------|
| ___  | ___                              | ___             | ___             | ___     |

PHASE-5-EXIT:
  [ ] Verdict matches OUTCOME exactly
  [ ] Conditions stated as specific deliverables; Owner + Trigger if not APPROVED
  [ ] All action items: Owner Role, action, deadline; TALLY count matches; anonymous = 0
  [ ] Every CONDITION/BLOCK role has dissent row with INERTIA-FINDING-* cite
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

| Dependent criterion                              | REQUIRES:  | Nature of dependency                                                              |
|--------------------------------------------------|------------|-----------------------------------------------------------------------------------|
| C-36 (three-way CONFIRMATION status)             | REQUIRES: C-35 | C-36 row count = N unenforceable without C-35's explicit closed-set manifest. Vocabulary presence does not establish count reconciliation. |
| INERTIA CONTINUITY BRIDGE YES-affirmation        | REQUIRES: [Phase 2 TIER SORT complete] | YES only verifiable after all participant orientations assigned in TIER SORT. |
| C-43 (fill-rule echo of C-41 annotation)         | REQUIRES: C-41 | C-43 echo is a dependent annotation -- the echo is meaningful only if PHASE-1-COMMIT carries the C-41 forward annotation. An echo without a source annotation creates the appearance of traceability without the substance; C-41 must be verified before crediting C-43. |

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
  [This forward annotation is required by C-41 and is echoed in TOKEN TRACE CONFIRMATION fill
   rules below (C-43). Three-point traceability: source annotation here + REQUIRES: C-35 at
   consumption + echo in fill rules.]
  FAILS [C-45]: bidirectionality clause states only one direction
  FAILS [C-41]: PHASE-1-COMMIT contains no forward annotation referencing C-36 row count

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

C-41 ECHO: PHASE-1-COMMIT annotation "[This explicit closed set is the prerequisite for C-36
  TOKEN TRACE CONFIRMATION row count = 4]" must be present at source. Three-point traceability:
  (1) REQUIRES: C-35 here [C-39] + (2) forward annotation at PHASE-1-COMMIT [C-41] + (3) this
  echo in fill rules [C-43]. Each point independently surfaces the dependency. Removing any one:
  -- Without C-39: reviewer scores C-36 without verifying C-35 (false positive risk)
  -- Without C-41: reviewer passes PHASE-1-COMMIT without registering C-36 consequence
  -- Without C-43: reviewer evaluating fill rules cannot confirm C-41 without traversing to source
  FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no echo of C-41 annotation
  FAILS [C-41]: PHASE-1-COMMIT contains no forward annotation referencing C-36 row count
  FAILS [C-39]: REQUIRES: C-35 annotation absent before TOKEN TRACE CONFIRMATION fill rule

PRINT: four-row confirmation table. ASSIGN: CONSUMED | NOT-APPLICABLE | DROPPED.
  NOT-APPLICABLE: cite specific charter constraint -- vague "not relevant" fails.
  DROPPED: invoke REPAIR RULE -- reopen Phase 1 before Phase 2 closes.
  FAILS [C-36]: fewer than 4 rows in confirmation table
  FAILS [C-36]: binary CONFIRMED/DROPOUT vocabulary used

---

**INERTIA CONTINUITY BRIDGE fill rule:**

REQUIRES: [Phase 2 TIER SORT complete]
  Verify TIER SORT table is complete and all orientations assigned before evaluating
  whether YES affirmation is correct.

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

RECOMMIT MANIFEST after each invalidated phase re-executes.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND issued
```
