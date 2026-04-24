---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-16
round: 5
rubric_version: 5
---

# corps-committee -- Prompt Variations R5

## Variation Summary

| ID   | Axis                                                        | Hypothesis |
|------|-------------------------------------------------------------|------------|
| V-01 | Phase 0 Committee-Type Gate (skeleton-embedded)             | A `## COMMITTEE TYPE GATE` block embedded in the skeleton between the Participants list and PHASE-0-COMMIT converts fill-rule validation (currently only prose instructions) into a structural output gate that must be ticked before Phase 0 seals. Applies the SYMMETRY CHECK / MINUTES INTEGRITY CHECK skeleton-gating pattern at the earliest phase boundary; Committee Type vocabulary errors caught at Phase 0 propagate silently through all five phases. |
| V-02 | Structured INERTIA CONTINUITY BRIDGE (skeleton-embedded multi-field block) | Expanding the INERTIA CONTINUITY BRIDGE from a single prose line into a skeleton block with explicit structural fields (inspection complete, decision YES/NO, injection record if NO, BRIDGE RESULT declaration with halt clause) converts a declaration that models can summarize in a phrase into a multi-field structural output requiring explicit completion before Phase 3 begins. The single-line form allows models to answer YES without completing the inspection — the expanded form makes that failure visible as an unfilled field. |
| V-03 | TALLY LEDGER PROTOCOL (named Phase 4 ledger with self-referencing count validation) | A named `*** TALLY LEDGER PROTOCOL ***` in Phase 4 fill rules — requiring explicit enumeration of each STANCE MANIFEST entry, per-token category assignment, independent summation, and participant-count cross-check before TALLY is written — applies the REWRITE PROTOCOL / TIER SEQUENCE PROTOCOL self-referencing named-block pattern to Phase 4 counting. Phase 4 miscounts are the quietest failure mode: TALLY can diverge from STANCE MANIFEST with no structural signal; the ledger makes count divergence a halt event. |
| V-04 | Phase 0 Gate + Structured Bridge (V-01 + V-02)             | The two earliest phase-boundary gaps share the same failure mode: a structural decision (committee type, bridge resolution) is made in fill prose without a skeleton checkpoint, allowing models to move forward with a wrong or unverified declaration. Co-applying the skeleton-block gate pattern at Phase 0 and the Bridge provides additive coverage for both decision points without interaction. |
| V-05 | Full R5 Integration (V-01 + V-02 + V-03 on R4 V-05 foundation) | All three R5 mechanisms on top of the complete R4 V-05 foundation (C-17 + C-18 + C-19 already present). Each R5 axis targets a distinct phase boundary — Phase 0, the Bridge, Phase 4 — that remains unguarded in R4 V-05. Together they close the structural gaps before, between, and after Phase 3 that skeleton-embedded gating had not yet reached. |

---

## V-01 -- Phase 0 Committee-Type Gate

**Axis:** Lifecycle emphasis -- skeleton-embedded `## COMMITTEE TYPE GATE` at Phase 0 boundary
**Hypothesis:** A `## COMMITTEE TYPE GATE` block embedded in the skeleton between the Participants list and PHASE-0-COMMIT converts fill-rule vocabulary validation into a structural gate that must be filled before Phase 0 seals. Committee Type vocabulary errors (e.g., "product review" instead of "ROB") currently propagate silently through all five phases because validation lives only in fill-rule prose. Embedding the gate in the skeleton makes a wrong type a visible unfilled checkbox rather than a silent classification error.

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

6. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must be cited by label form
   in at least one Phase 3 voice, or declared UNCITED with justification. AUDIT RESULT
   must be COMPLETE before PHASE-3-COMMIT seals.

7. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

8. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

9. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
   qualifying participant named. YES without a qualifying participant is a distinct failure
   from structural absence.

10. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
    before Phase 5 content is generated. Any unticked box halts Phase 5.

11. COMMITTEE TYPE GATE: Both checkboxes in the skeleton block must be ticked before
    PHASE-0-COMMIT seals. Any unticked box halts Phase 0. Acceptable types: ROB,
    shiproom, arch-board, or user-specified named type. Generic descriptions fail.

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

## COMMITTEE TYPE GATE

  [ ] Committee Type matches accepted vocabulary: ROB / shiproom / arch-board /
      user-specified named type (not a generic description)
  [ ] Agenda Item names a specific subject, not a category
  Both boxes ticked before PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. COMMITTEE TYPE GATE ticked.
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
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified`
  FAILS: `Committee Type: product review`
PRINT: Agenda Item, Charter Source, Participants.

COMPLETE ## COMMITTEE TYPE GATE before printing PHASE-0-COMMIT:
  Tick [ ] Committee Type matches accepted vocabulary
  Tick [ ] Agenda Item names a specific subject
  Both checkboxes must be ticked. Any unticked box halts Phase 0.

PRINT: PHASE-0-COMMIT -- include "COMMITTEE TYPE GATE ticked." in commit body.

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

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation (e.g., "INERTIA-FINDING-B").
    Enter the name of the role that cited it in the `Cited by:` field.
    If no voice cited the label by name: enter `UNCITED: [role closest in content] -- [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are either cited or justified.
  If AUDIT RESULT is INCOMPLETE: halt. Identify which Phase 3 voice should be revised.
  Revise that voice. Re-run the audit. PHASE-3-COMMIT may not print until COMPLETE.

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

---

## V-02 -- Structured INERTIA CONTINUITY BRIDGE

**Axis:** Inertia framing -- INERTIA CONTINUITY BRIDGE expanded from single prose line to multi-field skeleton block with BRIDGE RESULT halt gate
**Hypothesis:** The single-line Bridge format (`Inertia owner in tier sort: YES/NO`) allows models to write YES without completing the inspection or naming a qualifying participant (the C-08 failure mode). Expanding to a multi-field skeleton block with explicit inspection, decision, injection record, and BRIDGE RESULT with halting clause converts a prose declaration into a structural output requiring each field to be filled. The pattern mirrors how INERTIA CITATION AUDIT converted single-sentence audit instructions into a per-finding checklist.

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

6. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must be cited by label form
   in at least one Phase 3 voice, or declared UNCITED with justification. AUDIT RESULT
   must be COMPLETE before PHASE-3-COMMIT seals.

7. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

8. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

9. INERTIA CONTINUITY BRIDGE: The full skeleton block must be completed before Phase 3
   begins. BRIDGE RESULT must be declared. Undeclared BRIDGE RESULT halts Phase 3.
   YES decision requires a qualifying participant named in the OWNER RECORD field.
   YES without a qualifying participant is a distinct failure from structural absence.

10. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
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

  Inspection complete: ___  [YES -- inspection performed against Phase 2 TIER SORT]

  Decision: ___  [YES -- inertia owner present / NO -- Inertia-Advocate INJECTED]

  [If Decision is YES -- OWNER RECORD:]
    Qualifying participant: ___  [named role from Phase 2 Tier 1 or Tier 2]
    Inertia orientation confirmed: ___  [switching-cost / status-quo-defense / cost-of-change]

  [If Decision is NO -- INJECTION RECORD:]
    Injected participant: Inertia-Advocate
    Tier assignment: Tier 1 -- voice position 1
    STANCE MANIFEST placeholder confirmed: ___  [YES]
    Citation requirement: must cite at least one INERTIA-FINDING-* label in Phase 3 voice

  BRIDGE RESULT: ___  [OWNER-PRESENT / INJECTED]
  Undeclared BRIDGE RESULT halts Phase 3.

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
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified`
  FAILS: `Committee Type: product review`
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

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:

  Step 1: Set `Inspection complete: YES`.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists:
    Set `Decision: YES -- inertia owner present`.
    Complete OWNER RECORD: name the qualifying participant and confirm their inertia
    orientation (switching-cost / status-quo-defense / cost-of-change).
    Set `BRIDGE RESULT: OWNER-PRESENT`.
  Step 4: If no such participant exists:
    Set `Decision: NO -- Inertia-Advocate INJECTED`.
    Complete INJECTION RECORD: Inertia-Advocate, Tier 1 position 1, STANCE MANIFEST
    placeholder YES, citation requirement stated.
    Set `BRIDGE RESULT: INJECTED`.

VALIDATE: BRIDGE RESULT declared. Undeclared BRIDGE RESULT halts Phase 3.
VALIDATE: Decision is YES only when a qualifying participant actually exists.
  YES without a qualifying participant in OWNER RECORD is a distinct failure axis.

---

**PHASE 3 fill rules:**

Before generating any Phase 3 voice, execute the TIER SEQUENCE PROTOCOL:

  *** TIER SEQUENCE PROTOCOL ***
  Step 1: Determine voice sequence from INERTIA CONTINUITY BRIDGE BRIDGE RESULT and
    Phase 2 TIER SORT.
  Step 2: If BRIDGE RESULT is INJECTED: Inertia-Advocate is voice position 1 within
    Tier 1. All other Tier 1 participants follow. Then all Tier 2. Then all Tier 3.
  Step 3: If BRIDGE RESULT is OWNER-PRESENT: Tier 1 participants in institutional
    veto order. Then Tier 2. Then Tier 3.
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

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation.
    Enter citing role in `Cited by:` field.
    If uncited: `UNCITED: [role closest in content] -- [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are cited or justified.
  If INCOMPLETE: halt, revise the deficient voice, re-run audit.
  PHASE-3-COMMIT may not print until AUDIT RESULT is COMPLETE.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
  Include: `INERTIA CITATION AUDIT RESULT is COMPLETE.`
VALIDATE: forward AND reverse directions both present.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton.
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

## V-03 -- TALLY LEDGER PROTOCOL

**Axis:** Output format -- named `*** TALLY LEDGER PROTOCOL ***` in Phase 4 with explicit per-token ledger and participant-count cross-check
**Hypothesis:** Phase 4 TALLY miscounts are structurally silent: if the TALLY line diverges from STANCE MANIFEST, no existing gate catches the discrepancy before OUTCOME is declared. A named TALLY LEDGER PROTOCOL -- enumerating each STANCE MANIFEST entry line-by-line, assigning APPROVE/CONDITION/BLOCK per token, summing each category, and cross-checking the sum against the Phase 0 participant count -- applies the self-referencing named-block pattern (used in REWRITE PROTOCOL and TIER SEQUENCE PROTOCOL) to Phase 4, making count divergence a visible halt event rather than a propagated error.

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

6. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must be cited by label form
   in at least one Phase 3 voice, or declared UNCITED with justification. AUDIT RESULT
   must be COMPLETE before PHASE-3-COMMIT seals.

7. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

8. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

9. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
   qualifying participant named. YES without a qualifying participant is a distinct failure
   from structural absence.

10. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
    before Phase 5 content is generated. Any unticked box halts Phase 5.

11. TALLY LEDGER PROTOCOL: Before writing TALLY, execute the named ledger protocol in
    Phase 4 fill rules. Ledger must enumerate each STANCE MANIFEST entry, assign tokens,
    sum independently, and cross-check against Phase 0 participant count. Discrepancy
    halts Phase 4.

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

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. TALLY LEDGER confirmed.
  Phase 4 closed.
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
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified`
  FAILS: `Committee Type: product review`
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

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation.
    Enter citing role in `Cited by:` field.
    If uncited: `UNCITED: [role closest in content] -- [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are cited or justified.
  If INCOMPLETE: halt, revise the deficient voice, re-run audit.
  PHASE-3-COMMIT may not print until AUDIT RESULT is COMPLETE.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
  Include: `INERTIA CITATION AUDIT RESULT is COMPLETE.`
VALIDATE: forward AND reverse directions both present.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton.
All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

Before writing TALLY, execute the TALLY LEDGER PROTOCOL:

  *** TALLY LEDGER PROTOCOL ***
  Step 1: Read ## STANCE MANIFEST. List every entry one per line:
    [Role Name] -- [STANCE-TOKEN]
    (Include Inertia-Advocate if INJECTED; include all participants from Phase 0.)
  Step 2: Assign category to each token:
    APPROVE, CONDITION, or BLOCK.
  Step 3: Sum each category independently:
    APPROVE count: ___
    CONDITION count: ___
    BLOCK count: ___
    TOTAL: ___
  Step 4: Cross-check TOTAL against Phase 0 participant count.
    If TOTAL does not equal Phase 0 participant count (including any INJECTED participant):
    STOP. Identify the discrepancy -- missing entry, duplicate, or miscategorized token.
    Correct ## STANCE MANIFEST or recount. Execute TALLY LEDGER PROTOCOL again from the top.
  Step 5: Write TALLY from the verified ledger sums.
  *** END TALLY LEDGER PROTOCOL ***

WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT -- include "TALLY LEDGER confirmed." in commit body.

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

## V-04 -- Phase 0 Gate + Structured Bridge

**Axis:** Lifecycle emphasis + inertia framing (V-01 + V-02 on R4 V-05 foundation)
**Hypothesis:** Both V-01 and V-02 target phase-entry decisions that are currently validated only in fill-rule prose: Committee Type at Phase 0 entry and Bridge resolution at Phase 3 entry. The failure modes are structurally identical (a decision is made without a skeleton checkpoint), and the remedies are structurally parallel (a skeleton block with a halt gate). Co-applying both provides additive coverage at the two earliest phase-entry boundaries without interaction.

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

6. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must be cited by label form
   in at least one Phase 3 voice, or declared UNCITED with justification. AUDIT RESULT
   must be COMPLETE before PHASE-3-COMMIT seals.

7. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

8. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

9. INERTIA CONTINUITY BRIDGE: The full skeleton block must be completed before Phase 3
   begins. BRIDGE RESULT must be declared. Undeclared BRIDGE RESULT halts Phase 3.
   YES decision requires a qualifying participant named. YES without a qualifying
   participant is a distinct failure from structural absence.

10. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
    before Phase 5 content is generated. Any unticked box halts Phase 5.

11. COMMITTEE TYPE GATE: Both checkboxes in the skeleton block must be ticked before
    PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

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

## COMMITTEE TYPE GATE

  [ ] Committee Type matches accepted vocabulary: ROB / shiproom / arch-board /
      user-specified named type (not a generic description)
  [ ] Agenda Item names a specific subject, not a category
  Both boxes ticked before PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. COMMITTEE TYPE GATE ticked.
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

  Inspection complete: ___  [YES -- inspection performed against Phase 2 TIER SORT]

  Decision: ___  [YES -- inertia owner present / NO -- Inertia-Advocate INJECTED]

  [If Decision is YES -- OWNER RECORD:]
    Qualifying participant: ___  [named role from Phase 2 Tier 1 or Tier 2]
    Inertia orientation confirmed: ___  [switching-cost / status-quo-defense / cost-of-change]

  [If Decision is NO -- INJECTION RECORD:]
    Injected participant: Inertia-Advocate
    Tier assignment: Tier 1 -- voice position 1
    STANCE MANIFEST placeholder confirmed: ___  [YES]
    Citation requirement: must cite at least one INERTIA-FINDING-* label in Phase 3 voice

  BRIDGE RESULT: ___  [OWNER-PRESENT / INJECTED]
  Undeclared BRIDGE RESULT halts Phase 3.

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
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified`
  FAILS: `Committee Type: product review`
PRINT: Agenda Item, Charter Source, Participants.

COMPLETE ## COMMITTEE TYPE GATE before printing PHASE-0-COMMIT:
  Tick [ ] Committee Type matches accepted vocabulary
  Tick [ ] Agenda Item names a specific subject
  Both checkboxes must be ticked. Any unticked box halts Phase 0.

PRINT: PHASE-0-COMMIT -- include "COMMITTEE TYPE GATE ticked." in commit body.

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

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:

  Step 1: Set `Inspection complete: YES`.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists:
    Set `Decision: YES -- inertia owner present`.
    Complete OWNER RECORD: name the qualifying participant; confirm inertia orientation.
    Set `BRIDGE RESULT: OWNER-PRESENT`.
  Step 4: If no such participant exists:
    Set `Decision: NO -- Inertia-Advocate INJECTED`.
    Complete INJECTION RECORD: all four fields required.
    Set `BRIDGE RESULT: INJECTED`.

VALIDATE: BRIDGE RESULT declared. Undeclared BRIDGE RESULT halts Phase 3.
VALIDATE: Decision is YES only when qualifying participant actually exists.

---

**PHASE 3 fill rules:**

Before generating any Phase 3 voice, execute the TIER SEQUENCE PROTOCOL:

  *** TIER SEQUENCE PROTOCOL ***
  Step 1: Determine voice sequence from INERTIA CONTINUITY BRIDGE BRIDGE RESULT and
    Phase 2 TIER SORT.
  Step 2: If BRIDGE RESULT is INJECTED: Inertia-Advocate is voice position 1 within
    Tier 1. All other Tier 1 participants follow. Then all Tier 2. Then all Tier 3.
  Step 3: If BRIDGE RESULT is OWNER-PRESENT: Tier 1 participants in institutional
    veto order. Then Tier 2. Then Tier 3.
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

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation.
    Enter citing role in `Cited by:` field.
    If uncited: `UNCITED: [role closest in content] -- [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are cited or justified.
  If INCOMPLETE: halt, revise the deficient voice, re-run audit.
  PHASE-3-COMMIT may not print until AUDIT RESULT is COMPLETE.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
  Include: `INERTIA CITATION AUDIT RESULT is COMPLETE.`

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block.
All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block in the skeleton:
  Tick all five checkboxes. Any unticked box halts Phase 5.

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner AND Trigger. Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance with INERTIA-FINDING-* citation;
  OR `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-05 -- Full R5 Integration

**Axis:** Full R5 integration -- Phase 0 Gate + Structured Bridge + TALLY LEDGER PROTOCOL on R4 V-05 foundation
**Hypothesis:** All three R5 mechanisms co-applied on top of the complete R4 V-05 foundation (C-17 + C-18 + C-19 already present). Each mechanism targets a distinct phase boundary not guarded in R4 V-05: COMMITTEE TYPE GATE (Phase 0 exit), structured INERTIA CONTINUITY BRIDGE (Phase 3 entry), TALLY LEDGER PROTOCOL (Phase 4 counting integrity). Together they extend the skeleton-gating pattern across all six phase transitions; the three mechanisms do not interact and provide strictly additive coverage.

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

6. INERTIA CITATION AUDIT: All four INERTIA-FINDING-* labels must be cited by label form
   in at least one Phase 3 voice, or declared UNCITED with justification. AUDIT RESULT
   must be COMPLETE before PHASE-3-COMMIT seals.

7. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Phase 4 TALLY
   counts tokens here; do not re-parse Phase 3 prose.

8. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

9. INERTIA CONTINUITY BRIDGE: The full skeleton block must be completed before Phase 3
   begins. BRIDGE RESULT must be declared. Undeclared BRIDGE RESULT halts Phase 3.
   YES decision requires a qualifying participant named. YES without a qualifying
   participant is a distinct failure from structural absence.

10. MINUTES INTEGRITY CHECK: All five checkboxes in the skeleton block must be ticked
    before Phase 5 content is generated. Any unticked box halts Phase 5.

11. COMMITTEE TYPE GATE: Both checkboxes in the skeleton block must be ticked before
    PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

12. TALLY LEDGER PROTOCOL: Before writing TALLY, execute the named ledger protocol in
    Phase 4 fill rules. Ledger must enumerate each STANCE MANIFEST entry, assign tokens,
    sum independently, and cross-check against Phase 0 participant count. Discrepancy
    halts Phase 4.

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

## COMMITTEE TYPE GATE

  [ ] Committee Type matches accepted vocabulary: ROB / shiproom / arch-board /
      user-specified named type (not a generic description)
  [ ] Agenda Item names a specific subject, not a category
  Both boxes ticked before PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. COMMITTEE TYPE GATE ticked.
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

  Inspection complete: ___  [YES -- inspection performed against Phase 2 TIER SORT]

  Decision: ___  [YES -- inertia owner present / NO -- Inertia-Advocate INJECTED]

  [If Decision is YES -- OWNER RECORD:]
    Qualifying participant: ___  [named role from Phase 2 Tier 1 or Tier 2]
    Inertia orientation confirmed: ___  [switching-cost / status-quo-defense / cost-of-change]

  [If Decision is NO -- INJECTION RECORD:]
    Injected participant: Inertia-Advocate
    Tier assignment: Tier 1 -- voice position 1
    STANCE MANIFEST placeholder confirmed: ___  [YES]
    Citation requirement: must cite at least one INERTIA-FINDING-* label in Phase 3 voice

  BRIDGE RESULT: ___  [OWNER-PRESENT / INJECTED]
  Undeclared BRIDGE RESULT halts Phase 3.

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

PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. TALLY LEDGER confirmed.
  Phase 4 closed.
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
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified`
  FAILS: `Committee Type: product review`
PRINT: Agenda Item, Charter Source, Participants.

COMPLETE ## COMMITTEE TYPE GATE before printing PHASE-0-COMMIT:
  Tick [ ] Committee Type matches accepted vocabulary
  Tick [ ] Agenda Item names a specific subject
  Both checkboxes must be ticked. Any unticked box halts Phase 0.

PRINT: PHASE-0-COMMIT -- include "COMMITTEE TYPE GATE ticked." in commit body.

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

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:

  Step 1: Set `Inspection complete: YES`.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists:
    Set `Decision: YES -- inertia owner present`.
    Complete OWNER RECORD: name the qualifying participant; confirm inertia orientation.
    Set `BRIDGE RESULT: OWNER-PRESENT`.
  Step 4: If no such participant exists:
    Set `Decision: NO -- Inertia-Advocate INJECTED`.
    Complete INJECTION RECORD: all four fields required.
    Set `BRIDGE RESULT: INJECTED`.

VALIDATE: BRIDGE RESULT declared. Undeclared BRIDGE RESULT halts Phase 3.
VALIDATE: Decision is YES only when qualifying participant actually exists.
  YES without a qualifying participant in OWNER RECORD is a distinct failure axis.

---

**PHASE 3 fill rules:**

Before generating any Phase 3 voice, execute the TIER SEQUENCE PROTOCOL:

  *** TIER SEQUENCE PROTOCOL ***
  Step 1: Determine voice sequence from INERTIA CONTINUITY BRIDGE BRIDGE RESULT and
    Phase 2 TIER SORT.
  Step 2: If BRIDGE RESULT is INJECTED: Inertia-Advocate is voice position 1 within
    Tier 1. All other Tier 1 participants follow. Then all Tier 2. Then all Tier 3.
  Step 3: If BRIDGE RESULT is OWNER-PRESENT: Tier 1 participants in institutional
    veto order. Then Tier 2. Then Tier 3.
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

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT:
  For each label INERTIA-FINDING-A through INERTIA-FINDING-D:
    Scan Phase 3 voices for explicit label-form citation.
    Enter citing role in `Cited by:` field.
    If uncited: `UNCITED: [role closest in content] -- [justification]`.
  Set AUDIT RESULT to COMPLETE if all four labels are cited or justified.
  If INCOMPLETE: halt, revise the deficient voice, re-run audit.
  PHASE-3-COMMIT may not print until AUDIT RESULT is COMPLETE.

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

Before writing TALLY, execute the TALLY LEDGER PROTOCOL:

  *** TALLY LEDGER PROTOCOL ***
  Step 1: Read ## STANCE MANIFEST. List every entry one per line:
    [Role Name] -- [STANCE-TOKEN]
    (Include Inertia-Advocate if INJECTED; include all participants from Phase 0.)
  Step 2: Assign category to each token:
    APPROVE, CONDITION, or BLOCK.
  Step 3: Sum each category independently:
    APPROVE count: ___
    CONDITION count: ___
    BLOCK count: ___
    TOTAL: ___
  Step 4: Cross-check TOTAL against Phase 0 participant count.
    If TOTAL does not equal Phase 0 participant count (including any INJECTED participant):
    STOP. Identify the discrepancy -- missing entry, duplicate, or miscategorized token.
    Correct ## STANCE MANIFEST or recount. Execute TALLY LEDGER PROTOCOL again from the top.
  Step 5: Write TALLY from the verified ledger sums.
  *** END TALLY LEDGER PROTOCOL ***

WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT -- include "TALLY LEDGER confirmed." in commit body.

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

## R5 Excellence Signals to Watch

Each R5 variation introduces a new mechanism. Scoring against rubric v5 will not yet reveal a score delta because v5 criteria (C-17, C-18, C-19) are already satisfied by all R5 variations (they inherit R4 V-05). The signal to watch is whether any R5 mechanism produces output patterns that become C-20, C-21, or C-22:

| Mechanism | Candidate criterion | Failure mode it closes |
|---|---|---|
| COMMITTEE TYPE GATE (V-01) | C-20 -- Phase 0 Vocabulary Gate | Committee Type misclassification propagates silently through all phases |
| Structured BRIDGE (V-02) | C-21 -- Bridge Completeness Record | YES without qualifying participant, or injection without STANCE MANIFEST placeholder |
| TALLY LEDGER PROTOCOL (V-03) | C-22 -- Ledger-Verified TALLY | TALLY diverges from STANCE MANIFEST with no structural signal |

V-05 is the candidate for the next rubric-upgrade round if scoring reveals one or more of these patterns passing consistently.
