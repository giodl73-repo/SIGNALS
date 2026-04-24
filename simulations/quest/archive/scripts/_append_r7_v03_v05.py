"""Append V-03 through V-05 to corps-committee R7 variate file."""

TARGET = r"C:\src\sim\simulations\quest\golden\corps-committee-variate-R7-2026-03-16.md"

V03 = r"""
## V-03 -- Committee-Type-Aware Outcome Vocabulary

**Axis:** Output format -- OUTCOME tokens declared in Phase 0 and keyed to committee type; Phase 4 and Phase 5 consume the declared vocabulary
**Hypothesis:** The TALLY OUTCOME vocabulary is currently fixed: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED. This vocabulary is correct for ROB but semantically wrong for shiproom (GO / NO-GO / HOLD) and arch-board (ACCEPTED / ACCEPTED WITH REVISIONS / REJECTED / DEFERRED). A model running a shiproom simulation can output APPROVED and pass all structural checks despite using the wrong vocabulary. Declaring OUTCOME-VOCABULARY as a third COMMITTEE TYPE GATE checkbox at Phase 0 makes vocabulary a Phase 0 structural commitment. Phase 4 consumes the declared vocabulary for OUTCOME; Phase 5 validates Verdict against it. A Verdict using a token not matching the declared type is a structural defect caught before PHASE-5-COMMIT.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINT REGISTRY -- READ BEFORE PRINTING SKELETON

Each gate below governs the phase(s) listed. The halt trigger fires if the gate condition
is not met before proceeding past that phase boundary.

| Gate Name                    | Governs           | Halt Trigger                                                                        |
|------------------------------|-------------------|-------------------------------------------------------------------------------------|
| COMMIT PLACEMENT             | All phases        | Content found after any PHASE-N-COMMIT within same phase                            |
| COMMITTEE TYPE GATE          | Phase 0           | Unticked checkbox (incl. OUTCOME-VOCABULARY) before PHASE-0-COMMIT                  |
| INERTIA RECORD SEALING       | Phase 1           | INERTIA INVARIANT missing commit ref or modification prohibition                    |
| COUPLING INTEGRITY -- P1     | Phase 1           | PHASE-1-COMMIT missing one coupling direction                                       |
| GATE LOOP / REWRITE PROTOCOL | Phase 1           | Phase 1 closes with GATE-N Answer: NO                                               |
| INERTIA CONTINUITY BRIDGE    | Phase 2->3        | BRIDGE RESULT undeclared; or YES with no qualifying owner                           |
| TIER SEQUENCE PROTOCOL       | Phase 3           | Voice order violates Tier 1->2->3; Inertia-Advocate not first if INJECTED           |
| VOICE COMPLETENESS CHECK     | Phase 3           | Unticked per-tier checkbox before ## STANCE MANIFEST                                |
| INERTIA CITATION AUDIT       | Phase 3           | AUDIT RESULT not COMPLETE before PHASE-3-COMMIT                                     |
| COUPLING INTEGRITY -- P3     | Phase 3           | PHASE-3-COMMIT missing one coupling direction                                       |
| SYMMETRY CHECK               | Phase 3->4        | Unticked checkbox before Phase 4                                                    |
| STANCE MANIFEST              | Phase 3->4        | Entry missing or format not [Role Name] STANCE-TOKEN                                |
| TALLY LEDGER PROTOCOL        | Phase 4           | Count mismatch or TALLY RESULT undeclared                                           |
| OUTCOME VOCABULARY           | Phase 4, Phase 5  | OUTCOME or Verdict token not matching Phase 0 declared vocabulary                   |
| MINUTES INTEGRITY CHECK      | Phase 4->5        | Unticked checkbox (incl. DISSENT INERTIA LINKAGE) before Phase 5                    |
| DISSENT INERTIA LINKAGE      | Phase 5           | No INERTIA-FINDING-* token cited in dissent; no linkage justification               |
| ACTION ITEMS                 | Phase 5           | Item missing Owner Role, specific action, or deadline                               |

All gates are mandatory. A gate governing multiple phases must pass at each applicable boundary.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Outcome Vocabulary: ___  [ROB: APPROVED/APPROVED WITH CONDITIONS/BLOCKED/DEFERRED |
                          shiproom: GO/NO-GO/HOLD |
                          arch-board: ACCEPTED/ACCEPTED WITH REVISIONS/REJECTED/DEFERRED |
                          user-specified: declare vocabulary here]
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

## COMMITTEE TYPE GATE

  [ ] Committee Type matches accepted vocabulary: ROB / shiproom / arch-board /
      user-specified named type (not a generic description)
  [ ] Agenda Item names a specific subject, not a category
  [ ] Outcome Vocabulary declared and matched to Committee Type; tokens listed explicitly
  All three boxes ticked before PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Outcome Vocabulary: ___, Agenda Item: ___,
  Charter Source: ___, Participants: ___ roles loaded. COMMITTEE TYPE GATE ticked.
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

## VOICE COMPLETENESS CHECK

  Tier 1 completeness:
    [ ] Each Tier 1 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 1 voice cites a named INERTIA-FINDING-* label from ## INERTIA RECORD

  Tier 2 completeness:
    [ ] Each Tier 2 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 2 voice names a specific approval condition (not "address concerns")

  Tier 3 completeness:
    [ ] Each Tier 3 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 3 voice contains a CITE: field with a named INERTIA-FINDING-* label
    [ ] Each Tier 3 voice contains a RESPONDS-TO: field naming a specific concern

  All applicable boxes ticked before ## STANCE MANIFEST is written. Any unticked box halts Phase 3.

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
  VOICE COMPLETENESS CHECK ticked.
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

## TALLY LEDGER PROTOCOL

  Participant count from Phase 0 roster: ___
  Active outcome vocabulary: ___  [from Phase 0 Outcome Vocabulary declaration]
  STANCE MANIFEST entries:
    ___ -- [token per declared vocabulary]
    [repeat per participant]
  Count per token: ___
  Total: ___  [must equal participant count]

  TALLY RESULT: ___  [QUORUM MET / COUNT MISMATCH -- halt]
  VOCABULARY CHECK: OUTCOME token matches Phase 0 declared vocabulary? ___ [YES / NO]
  PHASE-4-COMMIT may not proceed until TALLY RESULT declared and VOCABULARY CHECK is YES.

TALLY: ___ [token-1] * ___ [token-2] * ___ [token-3]
OUTCOME: ___  [must use declared vocabulary token]

PHASE-4-COMMIT: [locked] -- TALLY LEDGER PROTOCOL complete, TALLY RESULT declared,
  OUTCOME declared using Phase 0 vocabulary. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## MINUTES INTEGRITY CHECK

  [ ] Verdict matches OUTCOME from Phase 4 exactly (same token from Phase 0 declared vocabulary)
  [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per non-full-approval stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not the full-approval token: Owner and Trigger both present in Re-entry path
  [ ] DISSENT INERTIA LINKAGE: at least one DISSENTING OPINIONS entry explicitly cites
      an INERTIA-FINDING-* label by token form -- OR "No dissent" declared with explicit
      "No inertia linkage required -- [justification]"
  All six boxes ticked before Phase 5 content is generated.

---

## PHASE 5 -- MINUTES

### DECISIONS

Verdict: ___  [must use Phase 0 declared vocabulary token]
Conditions for full approval: ___
Re-entry path (if verdict is not full-approval token):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ -- ___ -- ___
[Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Verdict uses Phase 0 declared vocabulary. Owner and Trigger present if verdict not full-approval.
  DISSENT INERTIA LINKAGE ticked. Phase 5 closed. Simulation complete.
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

SYMMETRY RULE: both pairs required and structurally parallel. One pair only fails.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.

DECLARE: Outcome Vocabulary keyed to Committee Type:
  ROB        -> APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
  shiproom   -> GO / NO-GO / HOLD
  arch-board -> ACCEPTED / ACCEPTED WITH REVISIONS / REJECTED / DEFERRED
  user-specified -> declare vocabulary tokens explicitly in the Outcome Vocabulary field
VALIDATE: tokens are specific named tokens, not descriptions.
  ACCEPTABLE: `Outcome Vocabulary: GO / NO-GO / HOLD`
  FAILS: `Outcome Vocabulary: standard approval terms`
  FAILS: `Outcome Vocabulary: ___` -- unfilled placeholder

PRINT: Agenda Item, Charter Source, Participants.
COMPLETE ## COMMITTEE TYPE GATE -- tick all three boxes. Any unticked halts Phase 0.
PRINT: PHASE-0-COMMIT -- include "Outcome Vocabulary: ___" and "COMMITTEE TYPE GATE ticked."

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A through D per standard rules.

EVALUATE GATE-N. IF NO -- REWRITE PROTOCOL (stop, discard, rewrite from scratch, repeat until YES).

IF YES:
WRITE: ## INERTIA RECORD (one-phrase anchors, passing attempt only).
VALIDATE: content anchors only.
PRINT: INERTIA INVARIANT (both elements: commit ref + modification prohibition).
PRINT: PHASE-1-COMMIT -- COUPLING PAIR A, both directions.

---

**PHASE 2 fill rules:**

ASSIGN tiers. SORT-CHECK. PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

Step 1 YES. Inspect TIER SORT. OWNER-PRESENT if qualifying participant found. INJECTED if not.
VALIDATE: BRIDGE RESULT declared. YES requires qualifying participant in OWNER RECORD.

---

**PHASE 3 fill rules:**

Execute TIER SEQUENCE PROTOCOL before any voice.
  *** TIER SEQUENCE PROTOCOL ***
  Determine sequence: INJECTED -> Inertia-Advocate first in Tier 1, then Tier 1, Tier 2, Tier 3.
  OWNER-PRESENT -> Tier 1 veto order, then Tier 2, Tier 3.
  After each voice: confirm tier >= previous. Violation -> restart from top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT STANCE: line using Phase 0 declared vocabulary token.
WRITE 2-4 sentences. REQUIRE Tier 1 INERTIA-FINDING-* citation. REQUIRE Tier 2 specific condition.
REQUIRE Tier 3 CITE: + RESPONDS-TO:.
VALIDATE: at least one non-full-approval stance. All-full-approval reopens Phase 2.

COMPLETE ## VOICE COMPLETENESS CHECK (all applicable boxes).
WRITE ## STANCE MANIFEST (Phase 0 declared vocabulary tokens).
VALIDATE: tokens match declared vocabulary.
PRINT: STANCE INVARIANT (both elements).
COMPLETE ## INERTIA CITATION AUDIT (AUDIT RESULT must be COMPLETE).
PRINT: PHASE-3-COMMIT -- COUPLING PAIR B, both directions; include VOICE CHECK and AUDIT RESULT.
Complete SYMMETRY CHECK.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL:
  LOAD declared vocabulary from Phase 0. ENUMERATE STANCE MANIFEST entries.
  VALIDATE: each token matches declared vocabulary. Mismatch: halt, correct.
  COUNT tokens. CROSS-CHECK vs Phase 0 participant count.
  DECLARE TALLY RESULT and VOCABULARY CHECK: YES.
  PHASE-4-COMMIT waits for both.
PRINT TALLY (declared vocabulary tokens). WRITE OUTCOME (declared vocabulary token).
PRINT PHASE-4-COMMIT including "OUTCOME declared using Phase 0 vocabulary."

---

**PHASE 5 fill rules:**

Complete MINUTES INTEGRITY CHECK -- all six boxes:
  Box 1: Verdict matches OUTCOME AND uses Phase 0 declared vocabulary. Wrong vocabulary fails.
  Boxes 2-5: standard rules.
  Box 6 (DISSENT INERTIA LINKAGE): confirm or add INERTIA-FINDING-* citation; or No dissent.
  All six ticked before Phase 5 content written.

WRITE Verdict (Phase 0 declared vocabulary token exactly).
VALIDATE: token matches declared vocabulary. Wrong token: halt, correct.
WRITE Conditions. REQUIRE Owner + Trigger if verdict not full-approval token.
PRINT action items (all three fields).
WRITE dissent with INERTIA-FINDING-* token citation. OR No dissent + No inertia linkage.
PRINT PHASE-5-COMMIT -- include "Verdict uses Phase 0 declared vocabulary. DISSENT INERTIA LINKAGE ticked."
```

---

## V-04 -- Action-Attribution + Inertia Resolution (V-01 + V-02)

**Axis:** Lifecycle emphasis + inertia framing -- Origin field on ACTION ITEMS (V-01) combined with INERTIA RESOLUTION SUMMARY block (V-02) on R6 V-05 foundation
**Hypothesis:** V-01 targets Phase 3->5 action traceability: each action must name the participant whose concern prompted it. V-02 targets Phase 1->5 finding accountability: each INERTIA-FINDING-* must declare whether an action addresses it or no action is needed. No structural interaction -- the Origin validation and the INERTIA RESOLUTION SUMMARY are independent checks on independent outputs. Co-applying both closes both gaps simultaneously: a correct simulation must attribute every action to a voice AND account for every inertia finding in a structured summary.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINT REGISTRY -- READ BEFORE PRINTING SKELETON

Each gate below governs the phase(s) listed. The halt trigger fires if the gate condition
is not met before proceeding past that phase boundary.

| Gate Name                    | Governs         | Halt Trigger                                                                        |
|------------------------------|-----------------|-------------------------------------------------------------------------------------|
| COMMIT PLACEMENT             | All phases      | Content found after any PHASE-N-COMMIT within same phase                            |
| COMMITTEE TYPE GATE          | Phase 0         | Unticked checkbox before PHASE-0-COMMIT                                             |
| INERTIA RECORD SEALING       | Phase 1         | INERTIA INVARIANT missing commit ref or modification prohibition                    |
| COUPLING INTEGRITY -- P1     | Phase 1         | PHASE-1-COMMIT missing one coupling direction                                       |
| GATE LOOP / REWRITE PROTOCOL | Phase 1         | Phase 1 closes with GATE-N Answer: NO                                               |
| INERTIA CONTINUITY BRIDGE    | Phase 2->3      | BRIDGE RESULT undeclared; or YES with no qualifying owner                           |
| TIER SEQUENCE PROTOCOL       | Phase 3         | Voice order violates Tier 1->2->3; Inertia-Advocate not first if INJECTED           |
| VOICE COMPLETENESS CHECK     | Phase 3         | Unticked per-tier checkbox before ## STANCE MANIFEST                                |
| INERTIA CITATION AUDIT       | Phase 3         | AUDIT RESULT not COMPLETE before PHASE-3-COMMIT                                     |
| COUPLING INTEGRITY -- P3     | Phase 3         | PHASE-3-COMMIT missing one coupling direction                                       |
| SYMMETRY CHECK               | Phase 3->4      | Unticked checkbox before Phase 4                                                    |
| STANCE MANIFEST              | Phase 3->4      | Entry missing or format not [Role Name] STANCE-TOKEN                                |
| TALLY LEDGER PROTOCOL        | Phase 4         | Count mismatch or TALLY RESULT undeclared                                           |
| MINUTES INTEGRITY CHECK      | Phase 4->5      | Unticked checkbox (incl. DISSENT INERTIA LINKAGE + INERTIA RESOLUTION SUMMARY)      |
| DISSENT INERTIA LINKAGE      | Phase 5         | No INERTIA-FINDING-* token cited in dissent; no linkage justification               |
| INERTIA RESOLUTION SUMMARY   | Phase 5         | Any INERTIA-FINDING-* label missing Addressed-by or No-action entry                 |
| ACTION ITEMS                 | Phase 5         | Item missing Owner Role, specific action, deadline, or Origin field                 |
| ACTION ATTRIBUTION           | Phase 5         | Origin names a participant absent from Phase 3 STANCE MANIFEST                      |

All gates are mandatory.

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
    Qualifying participant: ___
    Inertia orientation confirmed: ___

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

## VOICE COMPLETENESS CHECK

  Tier 1 completeness:
    [ ] Each Tier 1 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 1 voice cites a named INERTIA-FINDING-* label from ## INERTIA RECORD

  Tier 2 completeness:
    [ ] Each Tier 2 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 2 voice names a specific approval condition (not "address concerns")

  Tier 3 completeness:
    [ ] Each Tier 3 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 3 voice contains a CITE: field with a named INERTIA-FINDING-* label
    [ ] Each Tier 3 voice contains a RESPONDS-TO: field naming a specific concern

  All applicable boxes ticked before ## STANCE MANIFEST is written. Any unticked box halts Phase 3.

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

## INERTIA CITATION AUDIT

  INERTIA-FINDING-A: Cited by: ___
  INERTIA-FINDING-B: Cited by: ___
  INERTIA-FINDING-C: Cited by: ___
  INERTIA-FINDING-D: Cited by: ___

  [Any finding not cited: UNCITED: ___ -- [justification]]

  AUDIT RESULT: ___ [COMPLETE / INCOMPLETE -- halt]
  PHASE-3-COMMIT halts until AUDIT RESULT is COMPLETE.

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order.
  VOICE COMPLETENESS CHECK ticked.
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

## TALLY LEDGER PROTOCOL

  Participant count from Phase 0 roster: ___
  STANCE MANIFEST entries:
    ___ -- [APPROVE / CONDITION / BLOCK]
    [repeat per participant]
  APPROVE count: ___
  CONDITION count: ___
  BLOCK count: ___
  Total: ___  [must equal participant count]

  TALLY RESULT: ___  [QUORUM MET / COUNT MISMATCH -- halt]
  PHASE-4-COMMIT may not proceed until TALLY RESULT is declared.

TALLY: ___ APPROVE * ___ CONDITION * ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] -- TALLY LEDGER PROTOCOL complete, TALLY RESULT declared,
  TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## MINUTES INTEGRITY CHECK

  [ ] Verdict matches OUTCOME from Phase 4 exactly (same token: APPROVED /
      APPROVED WITH CONDITIONS / BLOCKED / DEFERRED)
  [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  [ ] At least two ACTION ITEMS, each with all four fields: Owner Role, specific action,
      deadline, Origin (Phase 3 STANCE MANIFEST participant whose concern prompted this action)
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  [ ] DISSENT INERTIA LINKAGE: at least one DISSENTING OPINIONS entry explicitly cites
      an INERTIA-FINDING-* label by token form -- OR "No dissent" declared with explicit
      "No inertia linkage required -- [justification]"
  [ ] INERTIA RESOLUTION SUMMARY complete: all four INERTIA-FINDING-* labels present,
      each with either "Addressed by: [action item]" or "No action needed: [justification]"
  All seven boxes ticked before Phase 5 content is generated.

---

## PHASE 5 -- MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ -- ___ -- ___ -- Origin: ___
[Owner Role -- specific action -- deadline -- Origin: Phase 3 participant whose concern prompted this action]

### DISSENTING OPINIONS

___

### INERTIA RESOLUTION SUMMARY

  INERTIA-FINDING-A: ___ [Addressed by: ___ / No action needed: ___]
  INERTIA-FINDING-B: ___ [Addressed by: ___ / No action needed: ___]
  INERTIA-FINDING-C: ___ [Addressed by: ___ / No action needed: ___]
  INERTIA-FINDING-D: ___ [Addressed by: ___ / No action needed: ___]

  RESOLUTION RESULT: ___ [COMPLETE / INCOMPLETE -- halt]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. DISSENT INERTIA LINKAGE ticked.
  ACTION ATTRIBUTION validated: all Origin fields name Phase 3 STANCE MANIFEST participants.
  INERTIA RESOLUTION SUMMARY complete, RESOLUTION RESULT declared.
  Phase 5 closed. Simulation complete.
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

SYMMETRY RULE: both pairs required and structurally parallel. One pair only fails.

---

**PHASE 0 fill rules:**

LOAD charter. ENFORCE fallback if absent.
PRINT: Committee Type, Agenda Item, Charter Source, Participants.
COMPLETE ## COMMITTEE TYPE GATE (both boxes). PRINT PHASE-0-COMMIT.

---

**PHASE 1 fill rules:**

LABEL INVESTIGATION-ATTEMPT-1. WRITE findings A-D.
EVALUATE GATE-N. IF NO: REWRITE PROTOCOL (discard, rewrite from scratch, repeat until YES).
IF YES: WRITE ## INERTIA RECORD (content anchors). PRINT INERTIA INVARIANT (both elements).
PRINT PHASE-1-COMMIT (COUPLING PAIR A, both directions).

---

**PHASE 2 fill rules:**

ASSIGN tiers. SORT-CHECK. PRINT PHASE-2-COMMIT.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

Complete block. OWNER-PRESENT if qualifying Tier 1/2 participant. INJECTED if not.
VALIDATE: BRIDGE RESULT declared, YES has qualifying participant in OWNER RECORD.

---

**PHASE 3 fill rules:**

Execute TIER SEQUENCE PROTOCOL (INJECTED: Inertia-Advocate first; OWNER-PRESENT: veto order).
Verify tier order after each voice. Restart on violation.

PRINT STANCE: line. WRITE 2-4 sentences. REQUIRE Tier 1 citation, Tier 2 condition, Tier 3 CITE+RESPONDS-TO.
VALIDATE: at least one CONDITION or BLOCK.

COMPLETE ## VOICE COMPLETENESS CHECK. WRITE ## STANCE MANIFEST. PRINT STANCE INVARIANT.
COMPLETE ## INERTIA CITATION AUDIT (all four labels cited or justified).
PRINT PHASE-3-COMMIT (COUPLING PAIR B, both directions; include VOICE CHECK and AUDIT RESULT).
Complete SYMMETRY CHECK.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL (enumerate, count, cross-check, declare TALLY RESULT).
PRINT TALLY. WRITE OUTCOME. PRINT PHASE-4-COMMIT.

---

**PHASE 5 fill rules:**

Complete MINUTES INTEGRITY CHECK -- all seven boxes:
  Box 1: Verdict matches OUTCOME exactly.
  Box 2: all three sections present.
  Box 3: four-field ACTION ITEMS (Origin field required for each).
  Box 4: DISSENTING OPINIONS complete or No dissent.
  Box 5: Re-entry path if verdict not APPROVED.
  Box 6 (DISSENT INERTIA LINKAGE): at least one INERTIA-FINDING-* token in dissent; or No dissent justification.
  Box 7 (INERTIA RESOLUTION SUMMARY): all four findings planned before writing Phase 5 content.
  All seven ticked before Phase 5 content written.

WRITE Verdict. WRITE Conditions. REQUIRE Owner + Trigger if not APPROVED.

PRINT action items -- four fields required:
  [Owner Role] -- [specific action] -- [deadline] -- Origin: [Phase 3 STANCE MANIFEST participant]
  VALIDATE: Origin must be a name from the Phase 3 STANCE MANIFEST. Not found: halt, correct.

WRITE dissent with INERTIA-FINDING-* token citation. OR No dissent + No inertia linkage justification.

COMPLETE ## INERTIA RESOLUTION SUMMARY:
  For INERTIA-FINDING-A through D: inspect ACTION ITEMS for content match.
    If match found: `Addressed by: [Owner Role] -- [action description]`.
    If no match: `No action needed: [justification]`.
  DECLARE: RESOLUTION RESULT: COMPLETE when all four filled. INCOMPLETE -> halt.
  PHASE-5-COMMIT may not print until RESOLUTION RESULT is COMPLETE.

PRINT PHASE-5-COMMIT -- include "DISSENT INERTIA LINKAGE ticked. ACTION ATTRIBUTION validated.
  INERTIA RESOLUTION SUMMARY complete, RESOLUTION RESULT declared."
```

---

## V-05 -- Full R7 Integration (V-01 + V-02 + V-03 on R6 V-05 foundation)

**Axis:** All three R7 axes combined on R6 V-05 foundation: Action-Attribution Linkage (lifecycle emphasis) + Inertia Resolution Summary (inertia framing) + Committee-Type-Aware Outcome Vocabulary (output format)
**Hypothesis:** Each R7 axis targets a distinct structural gap with no mechanical interaction. V-01 closes Phase 3->5 action traceability (Origin field). V-02 closes Phase 1->5 finding accountability (INERTIA RESOLUTION SUMMARY). V-03 closes Phase 0->4->5 vocabulary consistency (declared vocabulary gate). All R6 criteria carry forward. A correct R7 simulation: declares the right vocabulary at Phase 0, attributes every action to a Phase 3 voice, and accounts for every inertia finding in the Phase 5 summary.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINT REGISTRY -- READ BEFORE PRINTING SKELETON

Each gate below governs the phase(s) listed. The halt trigger fires if the gate condition
is not met before proceeding past that phase boundary.

| Gate Name                    | Governs           | Halt Trigger                                                                        |
|------------------------------|-------------------|-------------------------------------------------------------------------------------|
| COMMIT PLACEMENT             | All phases        | Content found after any PHASE-N-COMMIT within same phase                            |
| COMMITTEE TYPE GATE          | Phase 0           | Unticked checkbox (incl. OUTCOME-VOCABULARY) before PHASE-0-COMMIT                  |
| INERTIA RECORD SEALING       | Phase 1           | INERTIA INVARIANT missing commit ref or modification prohibition                    |
| COUPLING INTEGRITY -- P1     | Phase 1           | PHASE-1-COMMIT missing one coupling direction                                       |
| GATE LOOP / REWRITE PROTOCOL | Phase 1           | Phase 1 closes with GATE-N Answer: NO                                               |
| INERTIA CONTINUITY BRIDGE    | Phase 2->3        | BRIDGE RESULT undeclared; or YES with no qualifying owner                           |
| TIER SEQUENCE PROTOCOL       | Phase 3           | Voice order violates Tier 1->2->3; Inertia-Advocate not first if INJECTED           |
| VOICE COMPLETENESS CHECK     | Phase 3           | Unticked per-tier checkbox before ## STANCE MANIFEST                                |
| INERTIA CITATION AUDIT       | Phase 3           | AUDIT RESULT not COMPLETE before PHASE-3-COMMIT                                     |
| COUPLING INTEGRITY -- P3     | Phase 3           | PHASE-3-COMMIT missing one coupling direction                                       |
| SYMMETRY CHECK               | Phase 3->4        | Unticked checkbox before Phase 4                                                    |
| STANCE MANIFEST              | Phase 3->4        | Entry missing or format not [Role Name] STANCE-TOKEN                                |
| TALLY LEDGER PROTOCOL        | Phase 4           | Count mismatch or TALLY RESULT undeclared                                           |
| OUTCOME VOCABULARY           | Phase 4, Phase 5  | OUTCOME or Verdict token not matching Phase 0 declared vocabulary                   |
| MINUTES INTEGRITY CHECK      | Phase 4->5        | Unticked checkbox (incl. DISSENT INERTIA LINKAGE + INERTIA RESOLUTION SUMMARY)      |
| DISSENT INERTIA LINKAGE      | Phase 5           | No INERTIA-FINDING-* token cited in dissent; no linkage justification               |
| INERTIA RESOLUTION SUMMARY   | Phase 5           | Any INERTIA-FINDING-* label missing Addressed-by or No-action entry                 |
| ACTION ITEMS                 | Phase 5           | Item missing Owner Role, specific action, deadline, or Origin field                 |
| ACTION ATTRIBUTION           | Phase 5           | Origin names a participant absent from Phase 3 STANCE MANIFEST                      |

All gates are mandatory. A gate governing multiple phases must pass at each applicable boundary.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Outcome Vocabulary: ___  [ROB: APPROVED/APPROVED WITH CONDITIONS/BLOCKED/DEFERRED |
                          shiproom: GO/NO-GO/HOLD |
                          arch-board: ACCEPTED/ACCEPTED WITH REVISIONS/REJECTED/DEFERRED |
                          user-specified: declare vocabulary here]
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

## COMMITTEE TYPE GATE

  [ ] Committee Type matches accepted vocabulary: ROB / shiproom / arch-board /
      user-specified named type (not a generic description)
  [ ] Agenda Item names a specific subject, not a category
  [ ] Outcome Vocabulary declared and matched to Committee Type; tokens listed explicitly
  All three boxes ticked before PHASE-0-COMMIT seals. Any unticked box halts Phase 0.

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Outcome Vocabulary: ___, Agenda Item: ___,
  Charter Source: ___, Participants: ___ roles loaded. COMMITTEE TYPE GATE ticked.
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
    Qualifying participant: ___
    Inertia orientation confirmed: ___

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

## VOICE COMPLETENESS CHECK

  Tier 1 completeness:
    [ ] Each Tier 1 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 1 voice cites a named INERTIA-FINDING-* label from ## INERTIA RECORD

  Tier 2 completeness:
    [ ] Each Tier 2 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 2 voice names a specific approval condition (not "address concerns")

  Tier 3 completeness:
    [ ] Each Tier 3 voice has STANCE: label on a standalone line before prose
    [ ] Each Tier 3 voice contains a CITE: field with a named INERTIA-FINDING-* label
    [ ] Each Tier 3 voice contains a RESPONDS-TO: field naming a specific concern

  All applicable boxes ticked before ## STANCE MANIFEST is written. Any unticked box halts Phase 3.

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

## INERTIA CITATION AUDIT

  INERTIA-FINDING-A: Cited by: ___
  INERTIA-FINDING-B: Cited by: ___
  INERTIA-FINDING-C: Cited by: ___
  INERTIA-FINDING-D: Cited by: ___

  [Any finding not cited: UNCITED: ___ -- [justification]]

  AUDIT RESULT: ___ [COMPLETE / INCOMPLETE -- halt]
  PHASE-3-COMMIT halts until AUDIT RESULT is COMPLETE.

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 -> 2 -> 3 order.
  VOICE COMPLETENESS CHECK ticked.
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

## TALLY LEDGER PROTOCOL

  Participant count from Phase 0 roster: ___
  Active outcome vocabulary: ___  [from Phase 0 Outcome Vocabulary declaration]
  STANCE MANIFEST entries:
    ___ -- [token per declared vocabulary]
    [repeat per participant]
  Count per token: ___
  Total: ___  [must equal participant count]

  TALLY RESULT: ___  [QUORUM MET / COUNT MISMATCH -- halt]
  VOCABULARY CHECK: OUTCOME token matches Phase 0 declared vocabulary? ___ [YES / NO]
  PHASE-4-COMMIT may not proceed until TALLY RESULT declared and VOCABULARY CHECK is YES.

TALLY: ___ [token-1] * ___ [token-2] * ___ [token-3]
OUTCOME: ___  [must use declared vocabulary token]

PHASE-4-COMMIT: [locked] -- TALLY LEDGER PROTOCOL complete, TALLY RESULT declared,
  OUTCOME declared using Phase 0 vocabulary. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## MINUTES INTEGRITY CHECK

  [ ] Verdict matches OUTCOME from Phase 4 exactly (same token from Phase 0 declared vocabulary)
  [ ] All three sections present: DECISIONS, ACTION ITEMS, DISSENTING OPINIONS
  [ ] At least two ACTION ITEMS, each with all four fields: Owner Role, specific action,
      deadline, Origin (Phase 3 STANCE MANIFEST participant whose concern prompted this action)
  [ ] DISSENTING OPINIONS complete: one entry per non-full-approval stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not the full-approval token: Owner and Trigger both present in Re-entry path
  [ ] DISSENT INERTIA LINKAGE: at least one DISSENTING OPINIONS entry explicitly cites
      an INERTIA-FINDING-* label by token form -- OR "No dissent" declared with explicit
      "No inertia linkage required -- [justification]"
  [ ] INERTIA RESOLUTION SUMMARY complete: all four INERTIA-FINDING-* labels present,
      each with either "Addressed by: [action item]" or "No action needed: [justification]"
  All seven boxes ticked before Phase 5 content is generated.

---

## PHASE 5 -- MINUTES

### DECISIONS

Verdict: ___  [must use Phase 0 declared vocabulary token]
Conditions for full approval: ___
Re-entry path (if verdict is not full-approval token):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ -- ___ -- ___ -- Origin: ___
[Owner Role -- specific action -- deadline -- Origin: Phase 3 participant whose concern prompted this action]

### DISSENTING OPINIONS

___

### INERTIA RESOLUTION SUMMARY

  INERTIA-FINDING-A: ___ [Addressed by: ___ / No action needed: ___]
  INERTIA-FINDING-B: ___ [Addressed by: ___ / No action needed: ___]
  INERTIA-FINDING-C: ___ [Addressed by: ___ / No action needed: ___]
  INERTIA-FINDING-D: ___ [Addressed by: ___ / No action needed: ___]

  RESOLUTION RESULT: ___ [COMPLETE / INCOMPLETE -- halt]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Verdict uses Phase 0 declared vocabulary. Owner and Trigger present if verdict not full-approval.
  DISSENT INERTIA LINKAGE ticked. ACTION ATTRIBUTION validated: all Origin fields name
  Phase 3 STANCE MANIFEST participants. INERTIA RESOLUTION SUMMARY complete, RESOLUTION RESULT declared.
  Phase 5 closed. Simulation complete.
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

SYMMETRY RULE: both pairs required and structurally parallel. One pair only fails.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.

DECLARE: Outcome Vocabulary keyed to Committee Type:
  ROB        -> APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
  shiproom   -> GO / NO-GO / HOLD
  arch-board -> ACCEPTED / ACCEPTED WITH REVISIONS / REJECTED / DEFERRED
  user-specified -> declare vocabulary tokens explicitly
VALIDATE: tokens are specific named tokens, not descriptions.
  ACCEPTABLE: `Outcome Vocabulary: GO / NO-GO / HOLD`
  FAILS: `Outcome Vocabulary: standard approval terms`

PRINT: Agenda Item, Charter Source, Participants.
COMPLETE ## COMMITTEE TYPE GATE -- all three boxes. Any unticked halts Phase 0.
PRINT: PHASE-0-COMMIT -- include "Outcome Vocabulary: ___" and "COMMITTEE TYPE GATE ticked."

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A through D per standard four-slot rules.

EVALUATE GATE-N. IF NO:
  *** REWRITE PROTOCOL ***
  STOP. Discard all four findings. Write INVESTIGATION-ATTEMPT-[N+1].
  Rewrite all four completely from scratch. Evaluate GATE-[N+1]. Repeat until YES.
  *** END REWRITE PROTOCOL ***

IF YES:
WRITE: ## INERTIA RECORD (one-phrase anchors, passing attempt only).
VALIDATE: content anchors -- not bare labels or placeholders.
PRINT: INERTIA INVARIANT (both elements: "sealed at PHASE-1-COMMIT" + modification prohibition).
PRINT: PHASE-1-COMMIT -- COUPLING PAIR A per SYMMETRY DECLARATION. Both directions required.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny; Tier 2 -- conditional; Tier 3 -- advocates.
SORT-CHECK: if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

Complete block. Inspect Tier 1/2 for inertia-oriented participant.
OWNER-PRESENT if found; INJECTED if not.
VALIDATE: BRIDGE RESULT declared; YES has qualifying participant in OWNER RECORD.

---

**PHASE 3 fill rules:**

Execute TIER SEQUENCE PROTOCOL before any voice:
  *** TIER SEQUENCE PROTOCOL ***
  Determine sequence: INJECTED -> Inertia-Advocate first in Tier 1, other Tier 1, Tier 2, Tier 3.
  OWNER-PRESENT -> Tier 1 veto order, Tier 2, Tier 3.
  After each voice: confirm tier >= previous. Violation -> restart from top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT STANCE: token per Phase 0 declared vocabulary, standalone line before prose.
WRITE 2-4 sentences per participant from charter orientation.
REQUIRE (Tier 1): named INERTIA-FINDING-* citation.
REQUIRE (Tier 2): specific approval condition ("address concerns" fails).
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] + RESPONDS-TO: [named concern].
VALIDATE: at least one non-full-approval stance. All-full-approval reopens Phase 2.

COMPLETE ## VOICE COMPLETENESS CHECK (all applicable per-tier checkboxes).
WRITE ## STANCE MANIFEST ([Role Name] STANCE-TOKEN per participant, declared vocabulary tokens).
VALIDATE: each token matches declared vocabulary. Wrong vocabulary: halt, correct.
PRINT: STANCE INVARIANT (both elements: sealed at PHASE-3-COMMIT + revision prohibition).
COMPLETE ## INERTIA CITATION AUDIT (all four labels cited or justified, AUDIT RESULT COMPLETE).
PRINT: PHASE-3-COMMIT -- COUPLING PAIR B, both directions.
  Include: `VOICE COMPLETENESS CHECK ticked. INERTIA CITATION AUDIT RESULT is COMPLETE.`
Complete SYMMETRY CHECK (all three boxes).

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL:
  LOAD declared vocabulary. ENUMERATE STANCE MANIFEST entries.
  VALIDATE: each token matches declared vocabulary. Mismatch: halt, correct.
  COUNT tokens by type. CROSS-CHECK vs Phase 0 participant count.
  DECLARE TALLY RESULT: QUORUM MET (or COUNT MISMATCH -- halt).
  DECLARE VOCABULARY CHECK: YES (or halt if any token mismatches).
  PHASE-4-COMMIT waits for both TALLY RESULT and VOCABULARY CHECK: YES.
PRINT TALLY (declared vocabulary tokens). WRITE OUTCOME (declared vocabulary token).
PRINT PHASE-4-COMMIT including "TALLY LEDGER PROTOCOL complete, TALLY RESULT declared,
  OUTCOME declared using Phase 0 vocabulary."

---

**PHASE 5 fill rules:**

Complete MINUTES INTEGRITY CHECK -- all seven boxes:
  Box 1: Verdict matches OUTCOME AND uses Phase 0 declared vocabulary token.
    Wrong vocabulary fails even if it matches OUTCOME.
  Box 2: all three sections present (DECISIONS, ACTION ITEMS, DISSENTING OPINIONS).
  Box 3: at least two ACTION ITEMS, each with four fields (including Origin).
  Box 4: DISSENTING OPINIONS complete or No dissent.
  Box 5: Re-entry path (Owner + Trigger) if verdict not full-approval token.
  Box 6 (DISSENT INERTIA LINKAGE): at least one INERTIA-FINDING-* token in dissent.
    If absent: revise most relevant entry to add. If no dissent: No dissent + justification.
  Box 7 (INERTIA RESOLUTION SUMMARY): confirm all four findings are planned before writing.
    Any label with no planned entry halts Phase 5.
  All seven ticked before Phase 5 content written.

WRITE: Verdict -- Phase 0 declared vocabulary token exactly.
  VALIDATE: token matches declared vocabulary. Wrong token: halt, correct.
WRITE: Conditions for full approval (specific deliverables).
REQUIRE (verdict not full-approval token): Owner (named role) AND Trigger (artifact + recipient + authority).

PRINT: action items -- four fields required per item:
  [Owner Role] -- [specific action] -- [deadline] -- Origin: [Phase 3 STANCE MANIFEST participant]
  VALIDATE: Origin names a participant present in Phase 3 STANCE MANIFEST.
    Not found: halt, identify, correct.

WRITE: dissent per non-full-approval stance -- specific objection citing INERTIA-FINDING-* label
  by token form, resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason] -- No inertia linkage required -- [justification]`.

COMPLETE ## INERTIA RESOLUTION SUMMARY:
  For INERTIA-FINDING-A through D:
    INSPECT ACTION ITEMS: does any item address this finding's content area?
      If YES: `Addressed by: [Owner Role] -- [action description]`.
      If NO: `No action needed: [justification why no action is required]`.
  DECLARE RESOLUTION RESULT: COMPLETE when all four entries filled.
    Any blank entry: RESOLUTION RESULT: INCOMPLETE -- halt; identify; fill.
  PHASE-5-COMMIT may not print until RESOLUTION RESULT is COMPLETE.

PRINT: PHASE-5-COMMIT -- include:
  "Verdict uses Phase 0 declared vocabulary. DISSENT INERTIA LINKAGE ticked.
  ACTION ATTRIBUTION validated. INERTIA RESOLUTION SUMMARY complete, RESOLUTION RESULT declared."
```
"""

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(V03)

print(f"Done. Lines now: {sum(1 for _ in open(TARGET, encoding='utf-8'))}")
