---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-16
round: 4
rubric_version: 4
---

# corps-committee -- Prompt Variations R4

## Variation Summary

| ID   | Axis                                                        | Hypothesis |
|------|-------------------------------------------------------------|------------|
| V-01 | Skeleton-embedded Phase 5 integrity gate                    | A `## MINUTES INTEGRITY CHECK` block embedded in the skeleton between Phase 4 commit and Phase 5 mirrors C-15's skeleton-gating pattern at the Phase 5 boundary; Phase 5 completeness failures (missing Owner/Trigger, missing dissent, vague verdicts) occur because the model transitions directly from PHASE-4-COMMIT into Phase 5 fill without a structural checkpoint — embedding the check in the skeleton forces the completeness audit before any Phase 5 content is generated. |
| V-02 | Named self-referencing `*** TIER SEQUENCE PROTOCOL ***`     | Applying C-16's named-delimited-block-with-self-reference pattern to Phase 3 tier ordering and Inertia-Advocate injection closes a gap V-05 (R3) leaves open: the REWRITE PROTOCOL guards Phase 1 reattempts by name, but Phase 3 ordering violations (wrong tier interleaving, Inertia-Advocate not first) have no named restart signal; a named protocol that invokes itself on violation prevents drift across successive voice generations. |
| V-03 | Skeleton-embedded Inertia Citation Audit                    | An `## INERTIA CITATION AUDIT` block embedded in the skeleton between ## STANCE MANIFEST and PHASE-3-COMMIT enforces explicit traceability from INERTIA-FINDING-* labels through to Phase 3 voices; without a named audit structure in the skeleton, models generate voices that reference findings by description but omit the label-form citation — the audit block makes every finding's citation status visible before PHASE-3-COMMIT seals. |
| V-04 | Phase 5 integrity gate + Tier Sequence Protocol             | Combining V-01's MINUTES INTEGRITY CHECK with V-02's TIER SEQUENCE PROTOCOL: the two mechanisms address independent failure modes at independent phase boundaries (Phase 5 completeness vs. Phase 3 ordering) and do not interact, so co-presence provides additive coverage without redundancy. |
| V-05 | Full integration -- R4 Phase 5 gate + Tier Protocol + Citation Audit | All three R4 axes on top of the complete R3 V-05 foundation (C-12 + C-13 + C-14 + C-15 + C-16 + three new mechanisms). Each R4 axis targets a distinct uncovered failure mode; together they close the remaining mechanical gaps in Phase 3 voice ordering, Phase 3 citation traceability, and Phase 5 completeness. |

---

## V-01 -- Skeleton-Embedded Phase 5 Integrity Gate

**Axis:** Lifecycle emphasis -- skeleton-embedded Phase 5 completeness gate
**Hypothesis:** A `## MINUTES INTEGRITY CHECK` block embedded in the skeleton between PHASE-4-COMMIT and Phase 5 mirrors C-15's pattern at the Phase 5 boundary. Phase 5 completeness failures occur because the model transitions from Phase 4 into Phase 5 fill without a structural checkpoint; embedding the check in the skeleton forces the completeness audit before any Phase 5 content is generated, the same way SYMMETRY CHECK halts Phase 4 until coupling integrity is confirmed.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINTS -- READ BEFORE PRINTING SKELETON

1. COMMIT PLACEMENT: Every PHASE-N-COMMIT is the terminal line of its phase.
   No content of any kind may appear after a commit within the same phase.

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain (a) "sealed at
   PHASE-1-COMMIT" AND (b) the modification prohibition. Both required; either alone fails.

3. COUPLING INTEGRITY SYMMETRY: Two coupling contracts govern this simulation -- see
   SYMMETRY DECLARATION in Step 2. PHASE-1-COMMIT and PHASE-3-COMMIT each carry bilateral
   coupling clauses. One direction only fails. Both commits must carry this treatment
   identically.

4. GATE LOOP -- REWRITE PROTOCOL: If a gate answers NO, halt and rewrite. See Phase 1 fill
   rules for the explicit STOP-DISCARD-REWRITE instruction. Do not proceed past Phase 1
   until YES.

5. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

6. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

7. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
   qualifying participant named. YES without a qualifying participant is a distinct failure
   from structural absence.

8. MINUTES INTEGRITY CHECK: All four checkboxes in the skeleton block must be ticked
   before Phase 5 content is generated. Any unticked box halts Phase 5.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

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

[GATE-1 NO -> REWRITE PROTOCOL in Step 2 fill rules]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- qualifying participant: ___ /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___
RESPONDS-TO: "___" -- ___

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## SYMMETRY CHECK

  [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  [ ] Clause structure identical across both commits
  All three boxes ticked before Phase 4 proceeds.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE * ___ CONDITION * ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## MINUTES INTEGRITY CHECK

  [ ] Verdict matches OUTCOME from Phase 4 exactly (same token: APPROVED /
      APPROVED WITH CONDITIONS / BLOCKED / DEFERRED)
  [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  All five boxes ticked before Phase 5 content is generated.

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
[Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 -- FILL THE SKELETON

---

## SYMMETRY DECLARATION -- READ BEFORE PHASE 1 FILL

Two coupling contracts govern this simulation. They are structurally identical.

COUPLING PAIR A -- Phase 1:
  Subjects: ## INERTIA RECORD  <->  PHASE-1-COMMIT
  Forward:  modifications to ## INERTIA RECORD require updating PHASE-1-COMMIT
  Reverse:  modifications to PHASE-1-COMMIT require updating ## INERTIA RECORD
  Both directions required in PHASE-1-COMMIT body.

COUPLING PAIR B -- Phase 3:
  Subjects: ## STANCE MANIFEST  <->  PHASE-3-COMMIT
  Forward:  modifications to ## STANCE MANIFEST require updating PHASE-3-COMMIT
  Reverse:  modifications to PHASE-3-COMMIT require updating ## STANCE MANIFEST
  Both directions required in PHASE-3-COMMIT body.

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails coupling integrity.
  Satisfying Pair B and omitting Pair A also fails. Both pairs must be present and
  structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified`
  FAILS: `Committee Type -- product review`
PRINT: Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

EVALUATE GATE-N:
IF GATE-N ANSWER IS NO -- execute REWRITE PROTOCOL:
  *** REWRITE PROTOCOL ***
  STOP immediately. Do not write ## INERTIA RECORD.
  Discard all four findings from the current attempt entirely. They do not carry forward.
  Write: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings completely from scratch -- different workflow, different surface,
    different team, different switching cost. Not revised. Replaced.
  Write GATE-[N+1] and evaluate.
  If NO again -- execute REWRITE PROTOCOL again from the top.
  Repeat until YES.
  *** END REWRITE PROTOCOL ***

IF GATE-N ANSWER IS YES -- proceed:
WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt's findings only.
VALIDATE: each entry is a content anchor, not a bare label or placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: INERTIA INVARIANT -- both elements required:
  (1) "sealed at PHASE-1-COMMIT"
  (2) "findings may not be added, removed, or modified without reopening Phase 1"
VALIDATE: both present. Missing either fails on three independent axes:
  FAILS (a): commit reference present, prohibition absent
  FAILS (b): line present with neither element
  FAILS (c): line absent entirely

PRINT: PHASE-1-COMMIT -- COUPLING PAIR A per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present. One direction only fails.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny, risk, disruption; speak first.
ASSIGN: Tier 2 -- conditional approval; speak second.
ASSIGN: Tier 3 -- aligned with proposal goals; speak last.
SORT-CHECK: if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES -- [participant name]`.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists. YES without a qualifying
  participant is a distinct failure axis from structural absence.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: Inertia-Advocate FIRST in Tier 1 if INJECTED.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared.

WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required:
  (1) "sealed at PHASE-3-COMMIT"
  (2) "stance entries may not be revised without reopening Phase 3"
VALIDATE: both present. Missing either fails on three axes.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present. One direction only fails.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton:
  Tick [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  Tick [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  Tick [ ] Clause structure identical across both commits
  All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block in the skeleton:
  Tick [ ] Verdict matches OUTCOME from Phase 4 exactly
  Tick [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  Tick [ ] At least two ACTION ITEMS with all three fields each
  Tick [ ] DISSENTING OPINIONS complete or explicit No dissent
  Tick [ ] If not APPROVED: Owner and Trigger both planned
  All five checkboxes must be ticked. Any unticked box halts Phase 5.

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) AND Trigger (named artifact +
  recipient + authority). Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-02 -- Named Self-Referencing Tier Sequence Protocol

**Axis:** Role sequence -- named `*** TIER SEQUENCE PROTOCOL ***` with self-reference
**Hypothesis:** Applying C-16's pattern (named delimited block that re-invokes itself by name on failure) to Phase 3 tier ordering and Inertia-Advocate injection eliminates the failure mode where voices are generated in the wrong order or the injection rule is skipped. Currently Phase 3 ordering violations have no named restart signal; a self-referencing `*** TIER SEQUENCE PROTOCOL ***` mirrors the guarantee that `*** REWRITE PROTOCOL ***` provides for Phase 1, applied now to Phase 3.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINTS -- READ BEFORE PRINTING SKELETON

1. COMMIT PLACEMENT: Every PHASE-N-COMMIT is the terminal line of its phase.
   No content of any kind may appear after a commit within the same phase.

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain (a) "sealed at
   PHASE-1-COMMIT" AND (b) the modification prohibition. Both required; either alone fails.

3. COUPLING INTEGRITY SYMMETRY: Two coupling contracts govern this simulation -- see
   SYMMETRY DECLARATION in Step 2. PHASE-1-COMMIT and PHASE-3-COMMIT each carry bilateral
   coupling clauses. One direction only fails. Both commits must carry this treatment
   identically.

4. GATE LOOP -- REWRITE PROTOCOL: If a gate answers NO, halt and rewrite. See Phase 1 fill
   rules for the explicit STOP-DISCARD-REWRITE instruction. Do not proceed past Phase 1
   until YES.

5. TIER SEQUENCE PROTOCOL: Phase 3 voices must follow Tier 1 -> Tier 2 -> Tier 3. If
   INJECTED, Inertia-Advocate speaks first in Tier 1. See Phase 3 fill rules for the
   named TIER SEQUENCE PROTOCOL with self-referencing restart on violation.

6. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

7. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

8. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
   qualifying participant named. YES without a qualifying participant is a distinct failure
   from structural absence.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

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

[GATE-1 NO -> REWRITE PROTOCOL in Step 2 fill rules]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- qualifying participant: ___ /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___
RESPONDS-TO: "___" -- ___

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## SYMMETRY CHECK

  [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  [ ] Clause structure identical across both commits
  All three boxes ticked before Phase 4 proceeds.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE * ___ CONDITION * ___ BLOCK
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
[Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 -- FILL THE SKELETON

---

## SYMMETRY DECLARATION -- READ BEFORE PHASE 1 FILL

Two coupling contracts govern this simulation. They are structurally identical.

COUPLING PAIR A -- Phase 1:
  Subjects: ## INERTIA RECORD  <->  PHASE-1-COMMIT
  Forward:  modifications to ## INERTIA RECORD require updating PHASE-1-COMMIT
  Reverse:  modifications to PHASE-1-COMMIT require updating ## INERTIA RECORD
  Both directions required in PHASE-1-COMMIT body.

COUPLING PAIR B -- Phase 3:
  Subjects: ## STANCE MANIFEST  <->  PHASE-3-COMMIT
  Forward:  modifications to ## STANCE MANIFEST require updating PHASE-3-COMMIT
  Reverse:  modifications to PHASE-3-COMMIT require updating ## STANCE MANIFEST
  Both directions required in PHASE-3-COMMIT body.

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails coupling integrity.
  Satisfying Pair B and omitting Pair A also fails. Both pairs must be present and
  structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified`
  FAILS: `Committee Type -- product review`
PRINT: Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

EVALUATE GATE-N:
IF GATE-N ANSWER IS NO -- execute REWRITE PROTOCOL:
  *** REWRITE PROTOCOL ***
  STOP immediately. Do not write ## INERTIA RECORD.
  Discard all four findings from the current attempt entirely. They do not carry forward.
  Write: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings completely from scratch -- different workflow, different surface,
    different team, different switching cost. Not revised. Replaced.
  Write GATE-[N+1] and evaluate.
  If NO again -- execute REWRITE PROTOCOL again from the top.
  Repeat until YES.
  *** END REWRITE PROTOCOL ***

IF GATE-N ANSWER IS YES -- proceed:
WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt's findings only.
VALIDATE: each entry is a content anchor, not a bare label or placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: INERTIA INVARIANT -- both elements required:
  (1) "sealed at PHASE-1-COMMIT"
  (2) "findings may not be added, removed, or modified without reopening Phase 1"
VALIDATE: both present. Missing either fails on three independent axes.

PRINT: PHASE-1-COMMIT -- COUPLING PAIR A per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present. One direction only fails.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny, risk, disruption; speak first.
ASSIGN: Tier 2 -- conditional approval; speak second.
ASSIGN: Tier 3 -- aligned with proposal goals; speak last.
SORT-CHECK: if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES -- [participant name]`.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists. YES without a qualifying
  participant is a distinct failure axis from structural absence.

---

**PHASE 3 fill rules:**

Before generating any Phase 3 voice, execute the TIER SEQUENCE PROTOCOL:

  *** TIER SEQUENCE PROTOCOL ***
  Step 1: Determine voice sequence from INERTIA CONTINUITY BRIDGE decision and
    Phase 2 TIER SORT.
  Step 2: If Inertia-Advocate INJECTED (Bridge answered NO): Inertia-Advocate is
    voice position 1 within Tier 1. All other Tier 1 participants follow. Then
    all Tier 2 participants. Then all Tier 3 participants.
  Step 3: If Inertia-Advocate NOT INJECTED (Bridge answered YES): Tier 1
    participants in institutional veto order. Then Tier 2. Then Tier 3.
  Step 4: Write voices in this exact sequence. After each voice: confirm the
    current voice's tier equals or exceeds the previous voice's tier.
  Step 5: If any ordering violation detected -- STOP. Do not proceed to
    ## STANCE MANIFEST.
    Execute TIER SEQUENCE PROTOCOL again from the top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared. All-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required:
  (1) "sealed at PHASE-3-COMMIT"
  (2) "stance entries may not be revised without reopening Phase 3"
VALIDATE: both present. Missing either fails on three axes.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present. One direction only fails.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton:
  Tick [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  Tick [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  Tick [ ] Clause structure identical across both commits
  All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) AND Trigger (named artifact +
  recipient + authority). Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-03 -- Skeleton-Embedded Inertia Citation Audit

**Axis:** Inertia framing -- skeleton-embedded `## INERTIA CITATION AUDIT` block
**Hypothesis:** An `## INERTIA CITATION AUDIT` block embedded in the skeleton between ## STANCE MANIFEST and PHASE-3-COMMIT enforces traceability from each INERTIA-FINDING-* label through to at least one Phase 3 voice citation. Without a named audit structure, models generate voices that paraphrase findings without citing the label form; the skeleton block makes each finding's citation status an explicit structural output that must be filled before PHASE-3-COMMIT seals.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINTS -- READ BEFORE PRINTING SKELETON

1. COMMIT PLACEMENT: Every PHASE-N-COMMIT is the terminal line of its phase.
   No content of any kind may appear after a commit within the same phase.

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain (a) "sealed at
   PHASE-1-COMMIT" AND (b) the modification prohibition. Both required; either alone fails.

3. COUPLING INTEGRITY SYMMETRY: Two coupling contracts govern this simulation -- see
   SYMMETRY DECLARATION in Step 2. PHASE-1-COMMIT and PHASE-3-COMMIT each carry bilateral
   coupling clauses. One direction only fails. Both commits must carry this treatment
   identically.

4. GATE LOOP -- REWRITE PROTOCOL: If a gate answers NO, halt and rewrite. See Phase 1 fill
   rules for the explicit STOP-DISCARD-REWRITE instruction. Do not proceed past Phase 1
   until YES.

5. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must appear in the audit
   block between ## STANCE MANIFEST and PHASE-3-COMMIT. Each finding must be cited by
   at least one Phase 3 voice (label form), or declared UNCITED with justification.
   AUDIT RESULT must be COMPLETE before PHASE-3-COMMIT seals.

6. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

7. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

8. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
   qualifying participant named. YES without a qualifying participant is a distinct failure
   from structural absence.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

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

[GATE-1 NO -> REWRITE PROTOCOL in Step 2 fill rules]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- qualifying participant: ___ /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___
RESPONDS-TO: "___" -- ___

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

## INERTIA CITATION AUDIT

  INERTIA-FINDING-A: Cited by: ___
  INERTIA-FINDING-B: Cited by: ___
  INERTIA-FINDING-C: Cited by: ___
  INERTIA-FINDING-D: Cited by: ___

  [Any finding not cited by any Phase 3 voice: UNCITED: ___ -- [justification]]

  AUDIT RESULT: ___ [COMPLETE -- all findings cited or justified /
                      INCOMPLETE -- halt, revisit Phase 3 voices]

  PHASE-3-COMMIT halts until AUDIT RESULT is COMPLETE.

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order.
  INERTIA CITATION AUDIT RESULT is COMPLETE. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## SYMMETRY CHECK

  [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  [ ] Clause structure identical across both commits
  All three boxes ticked before Phase 4 proceeds.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE * ___ CONDITION * ___ BLOCK
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
[Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 -- FILL THE SKELETON

---

## SYMMETRY DECLARATION -- READ BEFORE PHASE 1 FILL

Two coupling contracts govern this simulation. They are structurally identical.

COUPLING PAIR A -- Phase 1:
  Subjects: ## INERTIA RECORD  <->  PHASE-1-COMMIT
  Forward:  modifications to ## INERTIA RECORD require updating PHASE-1-COMMIT
  Reverse:  modifications to PHASE-1-COMMIT require updating ## INERTIA RECORD
  Both directions required in PHASE-1-COMMIT body.

COUPLING PAIR B -- Phase 3:
  Subjects: ## STANCE MANIFEST  <->  PHASE-3-COMMIT
  Forward:  modifications to ## STANCE MANIFEST require updating PHASE-3-COMMIT
  Reverse:  modifications to PHASE-3-COMMIT require updating ## STANCE MANIFEST
  Both directions required in PHASE-3-COMMIT body.

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails coupling integrity.
  Satisfying Pair B and omitting Pair A also fails. Both pairs must be present and
  structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified`
  FAILS: `Committee Type -- product review`
PRINT: Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

EVALUATE GATE-N:
IF GATE-N ANSWER IS NO -- execute REWRITE PROTOCOL:
  *** REWRITE PROTOCOL ***
  STOP immediately. Do not write ## INERTIA RECORD.
  Discard all four findings from the current attempt entirely. They do not carry forward.
  Write: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings completely from scratch -- different workflow, different surface,
    different team, different switching cost. Not revised. Replaced.
  Write GATE-[N+1] and evaluate.
  If NO again -- execute REWRITE PROTOCOL again from the top.
  Repeat until YES.
  *** END REWRITE PROTOCOL ***

IF GATE-N ANSWER IS YES -- proceed:
WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt's findings only.
VALIDATE: each entry is a content anchor, not a bare label or placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: INERTIA INVARIANT -- both elements required:
  (1) "sealed at PHASE-1-COMMIT"
  (2) "findings may not be added, removed, or modified without reopening Phase 1"
VALIDATE: both present. Missing either fails on three independent axes.

PRINT: PHASE-1-COMMIT -- COUPLING PAIR A per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present. One direction only fails.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny, risk, disruption; speak first.
ASSIGN: Tier 2 -- conditional approval; speak second.
ASSIGN: Tier 3 -- aligned with proposal goals; speak last.
SORT-CHECK: if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES -- [participant name]`.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: Inertia-Advocate FIRST in Tier 1 if INJECTED.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared.

WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required:
  (1) "sealed at PHASE-3-COMMIT"
  (2) "stance entries may not be revised without reopening Phase 3"

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation (e.g., "INERTIA-FINDING-B").
    Enter the name of the role that cited it in the `Cited by:` field.
    If no voice cited the label by name: enter `UNCITED: [role closest in content] -- [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are either cited or justified.
  If AUDIT RESULT is INCOMPLETE: halt. Identify which Phase 3 voice should be revised to
    include the missing label citation. Revise that voice. Re-run the audit.
  PHASE-3-COMMIT may not be printed until AUDIT RESULT is COMPLETE.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
  Include: `INERTIA CITATION AUDIT RESULT is COMPLETE.`
VALIDATE: forward AND reverse directions both present. One direction only fails.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton:
  Tick [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  Tick [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  Tick [ ] Clause structure identical across both commits
  All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) AND Trigger (named artifact +
  recipient + authority). Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-04 -- Phase 5 Integrity Gate + Tier Sequence Protocol

**Axis:** Lifecycle emphasis + role sequence (C-15 pattern extended to Phase 5, C-16 pattern extended to Phase 3)
**Hypothesis:** The two most structurally independent Phase 5 and Phase 3 failure modes are addressed simultaneously: MINUTES INTEGRITY CHECK in skeleton prevents Phase 5 completeness misses; TIER SEQUENCE PROTOCOL with self-reference prevents Phase 3 ordering and injection drift. No interaction between the two mechanisms; co-presence provides additive coverage.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINTS -- READ BEFORE PRINTING SKELETON

1. COMMIT PLACEMENT: Every PHASE-N-COMMIT is the terminal line of its phase.
   No content of any kind may appear after a commit within the same phase.

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain (a) "sealed at
   PHASE-1-COMMIT" AND (b) the modification prohibition. Both required; either alone fails.

3. COUPLING INTEGRITY SYMMETRY: Two coupling contracts govern this simulation -- see
   SYMMETRY DECLARATION in Step 2. PHASE-1-COMMIT and PHASE-3-COMMIT each carry bilateral
   coupling clauses. One direction only fails. Both commits must carry this treatment
   identically.

4. GATE LOOP -- REWRITE PROTOCOL: If a gate answers NO, halt and rewrite. See Phase 1 fill
   rules for the explicit STOP-DISCARD-REWRITE instruction. Do not proceed past Phase 1
   until YES.

5. TIER SEQUENCE PROTOCOL: Phase 3 voices must follow Tier 1 -> Tier 2 -> Tier 3 with
   Inertia-Advocate first if INJECTED. See Phase 3 fill rules for the named
   TIER SEQUENCE PROTOCOL with self-referencing restart on violation.

6. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

7. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline.

8. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
   before Phase 5 content is generated. Any unticked box halts Phase 5.

9. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
   qualifying participant named.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

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

[GATE-1 NO -> REWRITE PROTOCOL in Step 2 fill rules]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- qualifying participant: ___ /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___
RESPONDS-TO: "___" -- ___

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## SYMMETRY CHECK

  [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  [ ] Clause structure identical across both commits
  All three boxes ticked before Phase 4 proceeds.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE * ___ CONDITION * ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## MINUTES INTEGRITY CHECK

  [ ] Verdict matches OUTCOME from Phase 4 exactly (same token: APPROVED /
      APPROVED WITH CONDITIONS / BLOCKED / DEFERRED)
  [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  All five boxes ticked before Phase 5 content is generated.

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
[Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 -- FILL THE SKELETON

---

## SYMMETRY DECLARATION -- READ BEFORE PHASE 1 FILL

Two coupling contracts govern this simulation. They are structurally identical.

COUPLING PAIR A -- Phase 1:
  Subjects: ## INERTIA RECORD  <->  PHASE-1-COMMIT
  Forward:  modifications to ## INERTIA RECORD require updating PHASE-1-COMMIT
  Reverse:  modifications to PHASE-1-COMMIT require updating ## INERTIA RECORD
  Both directions required in PHASE-1-COMMIT body.

COUPLING PAIR B -- Phase 3:
  Subjects: ## STANCE MANIFEST  <->  PHASE-3-COMMIT
  Forward:  modifications to ## STANCE MANIFEST require updating PHASE-3-COMMIT
  Reverse:  modifications to PHASE-3-COMMIT require updating ## STANCE MANIFEST
  Both directions required in PHASE-3-COMMIT body.

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails coupling integrity.
  Satisfying Pair B and omitting Pair A also fails. Both pairs must be present and
  structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified`
  FAILS: `Committee Type -- product review`
PRINT: Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

EVALUATE GATE-N:
IF GATE-N ANSWER IS NO -- execute REWRITE PROTOCOL:
  *** REWRITE PROTOCOL ***
  STOP immediately. Do not write ## INERTIA RECORD.
  Discard all four findings from the current attempt entirely. They do not carry forward.
  Write: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings completely from scratch -- different workflow, different surface,
    different team, different switching cost. Not revised. Replaced.
  Write GATE-[N+1] and evaluate.
  If NO again -- execute REWRITE PROTOCOL again from the top.
  Repeat until YES.
  *** END REWRITE PROTOCOL ***

IF GATE-N ANSWER IS YES -- proceed:
WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt's findings only.
VALIDATE: each entry is a content anchor, not a bare label or placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: INERTIA INVARIANT -- both elements required:
  (1) "sealed at PHASE-1-COMMIT"
  (2) "findings may not be added, removed, or modified without reopening Phase 1"
VALIDATE: both present. Missing either fails.

PRINT: PHASE-1-COMMIT -- COUPLING PAIR A per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny, risk, disruption; speak first.
ASSIGN: Tier 2 -- conditional approval; speak second.
ASSIGN: Tier 3 -- aligned with proposal goals; speak last.
SORT-CHECK: if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES -- [participant name]`.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists.

---

**PHASE 3 fill rules:**

Before generating any Phase 3 voice, execute the TIER SEQUENCE PROTOCOL:

  *** TIER SEQUENCE PROTOCOL ***
  Step 1: Determine voice sequence from INERTIA CONTINUITY BRIDGE decision and
    Phase 2 TIER SORT.
  Step 2: If Inertia-Advocate INJECTED (Bridge answered NO): Inertia-Advocate is
    voice position 1 within Tier 1. All other Tier 1 participants follow. Then
    all Tier 2 participants. Then all Tier 3 participants.
  Step 3: If Inertia-Advocate NOT INJECTED (Bridge answered YES): Tier 1
    participants in institutional veto order. Then Tier 2. Then Tier 3.
  Step 4: Write voices in this exact sequence. After each voice: confirm the
    current voice's tier equals or exceeds the previous voice's tier.
  Step 5: If any ordering violation detected -- STOP. Do not proceed to
    ## STANCE MANIFEST.
    Execute TIER SEQUENCE PROTOCOL again from the top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: before endorsement; RESPONDS-TO: named concern before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared.

WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required.
PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton:
  Tick [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  Tick [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  Tick [ ] Clause structure identical across both commits
  All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block in the skeleton:
  Tick [ ] Verdict matches OUTCOME from Phase 4 exactly
  Tick [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  Tick [ ] At least two ACTION ITEMS with all three fields each
  Tick [ ] DISSENTING OPINIONS complete or explicit No dissent
  Tick [ ] If not APPROVED: Owner and Trigger both planned
  All five checkboxes must be ticked. Any unticked box halts Phase 5.

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner AND Trigger. Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance with INERTIA-FINDING-* citation;
  OR `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-05 -- Full Integration (R4 Phase 5 Gate + Tier Protocol + Citation Audit)

**Axis:** Full R4 integration -- C-12 + C-13 + C-14 + C-15 + C-16 + Phase 5 skeleton gate + Tier Sequence Protocol + Inertia Citation Audit
**Hypothesis:** When all three R4 mechanisms co-present on top of the complete R3 V-05 foundation -- skeleton-embedded MINUTES INTEGRITY CHECK (extends C-15 to Phase 5), self-referencing `*** TIER SEQUENCE PROTOCOL ***` (extends C-16 to Phase 3 ordering), and skeleton-embedded `## INERTIA CITATION AUDIT` (closes the Phase 3 citation traceability gap) -- the output earns all three new R4 aspirational criteria on top of the full prior-round pass set. Each mechanism targets a distinct uncovered failure mode and none interact; co-presence is strictly additive.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINTS -- READ BEFORE PRINTING SKELETON

1. COMMIT PLACEMENT: Every PHASE-N-COMMIT is the terminal line of its phase.
   No content of any kind may appear after a commit within the same phase.

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain (a) "sealed at
   PHASE-1-COMMIT" AND (b) the modification prohibition. Both required; either alone fails.

3. COUPLING INTEGRITY SYMMETRY: Two coupling contracts govern this simulation -- see
   SYMMETRY DECLARATION in Step 2. PHASE-1-COMMIT and PHASE-3-COMMIT each carry bilateral
   coupling clauses. One direction only fails. Both commits must carry this treatment
   identically.

4. GATE LOOP -- REWRITE PROTOCOL: If a gate answers NO, halt and rewrite. See Phase 1 fill
   rules for the explicit STOP-DISCARD-REWRITE instruction. Do not proceed past Phase 1
   until YES.

5. TIER SEQUENCE PROTOCOL: Phase 3 voices must follow Tier 1 -> Tier 2 -> Tier 3 with
   Inertia-Advocate first if INJECTED. A named protocol with self-referencing restart
   governs Phase 3 ordering -- see Phase 3 fill rules.

6. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must appear in the audit
   block between ## STANCE MANIFEST and PHASE-3-COMMIT. Each finding must be cited by
   at least one Phase 3 voice (label form), or declared UNCITED with justification.
   AUDIT RESULT must be COMPLETE before PHASE-3-COMMIT seals.

7. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

8. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

9. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
   before Phase 5 content is generated. Any unticked box halts Phase 5.

10. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
    qualifying participant named. YES without qualification is a distinct failure from
    structural absence.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

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

[GATE-1 NO -> REWRITE PROTOCOL in Step 2 fill rules]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 -- TIER SORT

### TIER SORT

Tier 1 -- CHALLENGERS: ___
Tier 2 -- CONDITIONALS: ___
Tier 3 -- ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- qualifying participant: ___ /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___
RESPONDS-TO: "___" -- ___

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

## INERTIA CITATION AUDIT

  INERTIA-FINDING-A: Cited by: ___
  INERTIA-FINDING-B: Cited by: ___
  INERTIA-FINDING-C: Cited by: ___
  INERTIA-FINDING-D: Cited by: ___

  [Any finding not cited by any Phase 3 voice: UNCITED: ___ -- [justification]]

  AUDIT RESULT: ___ [COMPLETE -- all findings cited or justified /
                      INCOMPLETE -- halt, revisit Phase 3 voices]

  PHASE-3-COMMIT halts until AUDIT RESULT is COMPLETE.

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order.
  INERTIA CITATION AUDIT RESULT is COMPLETE. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## SYMMETRY CHECK

  [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  [ ] Clause structure identical across both commits
  All three boxes ticked before Phase 4 proceeds.

---

## PHASE 4 -- TALLY

TALLY: ___ APPROVE * ___ CONDITION * ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## MINUTES INTEGRITY CHECK

  [ ] Verdict matches OUTCOME from Phase 4 exactly (same token: APPROVED /
      APPROVED WITH CONDITIONS / BLOCKED / DEFERRED)
  [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  All five boxes ticked before Phase 5 content is generated.

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
[Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 -- FILL THE SKELETON

---

## SYMMETRY DECLARATION -- READ BEFORE PHASE 1 FILL

Two coupling contracts govern this simulation. They are structurally identical.

COUPLING PAIR A -- Phase 1:
  Subjects: ## INERTIA RECORD  <->  PHASE-1-COMMIT
  Forward:  modifications to ## INERTIA RECORD require updating PHASE-1-COMMIT
  Reverse:  modifications to PHASE-1-COMMIT require updating ## INERTIA RECORD
  Both directions required in PHASE-1-COMMIT body.

COUPLING PAIR B -- Phase 3:
  Subjects: ## STANCE MANIFEST  <->  PHASE-3-COMMIT
  Forward:  modifications to ## STANCE MANIFEST require updating PHASE-3-COMMIT
  Reverse:  modifications to PHASE-3-COMMIT require updating ## STANCE MANIFEST
  Both directions required in PHASE-3-COMMIT body.

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails coupling integrity.
  Satisfying Pair B and omitting Pair A also fails. Both pairs must be present and
  structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified`
  FAILS: `Committee Type -- product review`
PRINT: Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

EVALUATE GATE-N:
IF GATE-N ANSWER IS NO -- execute REWRITE PROTOCOL:
  *** REWRITE PROTOCOL ***
  STOP immediately. Do not write ## INERTIA RECORD.
  Discard all four findings from the current attempt entirely. They do not carry forward.
  Write: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings completely from scratch -- different workflow, different surface,
    different team, different switching cost. Not revised. Replaced.
  Write GATE-[N+1] and evaluate.
  If NO again -- execute REWRITE PROTOCOL again from the top.
  Repeat until YES.
  *** END REWRITE PROTOCOL ***

IF GATE-N ANSWER IS YES -- proceed:
WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt's findings only.
VALIDATE: each entry is a content anchor, not a bare label or placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: INERTIA INVARIANT -- both elements required:
  (1) "sealed at PHASE-1-COMMIT"
  (2) "findings may not be added, removed, or modified without reopening Phase 1"
VALIDATE: both present. Missing either fails on three independent axes:
  FAILS (a): commit reference present, prohibition absent
  FAILS (b): line present with neither element
  FAILS (c): line absent entirely

PRINT: PHASE-1-COMMIT -- COUPLING PAIR A per SYMMETRY DECLARATION. Both directions required.
VALIDATE: forward AND reverse directions both present. One direction only fails.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny, risk, disruption; speak first.
ASSIGN: Tier 2 -- conditional approval; speak second.
ASSIGN: Tier 3 -- aligned with proposal goals; speak last.
SORT-CHECK: if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES -- [participant name]`.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists. YES without a qualifying
  participant is a distinct failure axis from structural absence -- both axes independently
  required in a complete validation.

---

**PHASE 3 fill rules:**

Before generating any Phase 3 voice, execute the TIER SEQUENCE PROTOCOL:

  *** TIER SEQUENCE PROTOCOL ***
  Step 1: Determine voice sequence from INERTIA CONTINUITY BRIDGE decision and
    Phase 2 TIER SORT.
  Step 2: If Inertia-Advocate INJECTED (Bridge answered NO): Inertia-Advocate is
    voice position 1 within Tier 1. All other Tier 1 participants follow. Then
    all Tier 2 participants. Then all Tier 3 participants.
  Step 3: If Inertia-Advocate NOT INJECTED (Bridge answered YES): Tier 1
    participants in institutional veto order. Then Tier 2. Then Tier 3.
  Step 4: Write voices in this exact sequence. After each voice: confirm the
    current voice's tier equals or exceeds the previous voice's tier.
  Step 5: If any ordering violation detected -- STOP. Do not proceed to
    ## STANCE MANIFEST.
    Execute TIER SEQUENCE PROTOCOL again from the top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared. All-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required:
  (1) "sealed at PHASE-3-COMMIT"
  (2) "stance entries may not be revised without reopening Phase 3"
VALIDATE: both present. Missing either fails on three axes:
  FAILS (a): commit reference present, prohibition absent
  FAILS (b): line present with neither element
  FAILS (c): line absent entirely

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation (e.g., "INERTIA-FINDING-B").
    Enter the name of the role that cited it in the `Cited by:` field.
    If no voice cited the label by name: enter `UNCITED: [role closest in content] --
      [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are either cited or justified.
  If AUDIT RESULT is INCOMPLETE: halt. Identify which Phase 3 voice should be revised to
    include the missing label citation. Revise that voice. Re-run the audit.
  PHASE-3-COMMIT may not be printed until AUDIT RESULT is COMPLETE.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
  Include: `INERTIA CITATION AUDIT RESULT is COMPLETE.`
VALIDATE: forward AND reverse directions both present. One direction only fails.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton:
  Tick [ ] PHASE-1-COMMIT carries both coupling directions for ## INERTIA RECORD
  Tick [ ] PHASE-3-COMMIT carries both coupling directions for ## STANCE MANIFEST
  Tick [ ] Clause structure identical across both commits
  All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block in the skeleton:
  Tick [ ] Verdict matches OUTCOME from Phase 4 exactly
  Tick [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  Tick [ ] At least two ACTION ITEMS with all three fields each
  Tick [ ] DISSENTING OPINIONS complete or explicit No dissent
  Tick [ ] If not APPROVED: Owner and Trigger both planned
  All five checkboxes must be ticked. Any unticked box halts Phase 5.

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) AND Trigger (named artifact +
  recipient + authority). Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```
