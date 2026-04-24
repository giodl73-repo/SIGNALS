---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-16
round: 3
rubric_version: 3
---

# corps-committee -- Prompt Variations R3

## Variation Summary

| ID   | Axis                                           | Hypothesis |
|------|------------------------------------------------|------------|
| V-01 | Pre-skeleton rule block (C-12)                 | Printing a compact CONSTRAINTS preamble before the skeleton loads the most critical non-negotiable rules into active context before any fill content is generated; fill-phase violations drop because the model never reaches Phase 1 without knowing the sealing contract, gate loop, and coupling integrity rules. |
| V-02 | Rewrite-before-proceed loop (C-13)             | Replacing "INCREMENT N; new label" with an explicit STOP-DISCARD-REWRITE instruction eliminates partial retry loops where the model appends revised findings to the old attempt rather than replacing them; the gate becomes a genuine restart signal. |
| V-03 | Coupling integrity symmetry declaration (C-14) | A single SYMMETRY DECLARATION block -- appearing once before Phase 1 fill rules -- that explicitly names both Phase-1 and Phase-3 coupling pairs and asserts they must be structurally identical forces symmetric coverage; the model cannot satisfy one commit's bidirectionality requirement while leaving the other as one-directional prose. |
| V-04 | Pre-skeleton rule block + Rewrite-before-proceed (C-12 + C-13) | Combining the CONSTRAINTS preamble with the STOP-DISCARD-REWRITE gate: the preamble activates constraints early; the explicit rewrite instruction prevents loop degradation. Hypothesis: co-presence eliminates both the front-of-fill knowledge gap and the incremental-append failure mode simultaneously. |
| V-05 | Full integration -- C-12 + C-13 + C-14        | All three v3 axes together: CONSTRAINTS preamble, STOP-DISCARD-REWRITE gate, and explicit SYMMETRY DECLARATION. Hypothesis: when all three mechanisms co-present the output earns all three new v3 aspirational criteria on top of the full essential and prior-round recommended pass set. |

---

## V-01 -- Pre-skeleton Rule Block

**Axis:** Pre-skeleton rule block
**Hypothesis:** Printing a compact CONSTRAINTS preamble before the skeleton loads the most critical non-negotiable rules into active context before any fill content is generated. Fill-phase violations drop because the model never reaches Phase 1 without knowing the sealing contract, gate loop, and coupling integrity rules.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

---

## CONSTRAINTS -- READ BEFORE PRINTING SKELETON

1. COMMIT PLACEMENT: Every PHASE-N-COMMIT is the terminal line of its phase.
   No content of any kind may appear after a commit line within the same phase.

2. INERTIA RECORD SEALING: The INERTIA INVARIANT line must contain both the commit
   reference ("sealed at PHASE-1-COMMIT") AND the modification prohibition ("findings
   may not be added, removed, or modified without reopening Phase 1"). Both elements
   required. Either element alone fails.

3. COUPLING INTEGRITY: PHASE-1-COMMIT carries a bidirectionality clause naming both
   coupling directions: (a) modifications to INERTIA RECORD require updating the commit,
   AND (b) modifications to the commit require updating INERTIA RECORD. One direction
   only fails. The same bidirectionality contract applies identically to PHASE-3-COMMIT
   and ## STANCE MANIFEST.

4. GATE LOOP: If GATE-N answers NO, write INVESTIGATION-ATTEMPT-(N+1) with entirely
   new findings before writing GATE-(N+1). Do not proceed past Phase 1 until a gate
   answers YES.

5. STANCE MANIFEST: One entry per participant in format [Role Name] STANCE-TOKEN.
   Phase 4 TALLY counts tokens in the manifest. Do not re-parse Phase 3 prose.

6. ACTION ITEMS: Every action item has exactly three fields -- Owner Role, specific
   action, deadline. Missing any field fails.

7. INERTIA CONTINUITY BRIDGE: Appears between Phase 2 and Phase 3. States YES (with
   qualifying role identified) or NO (with Inertia-Advocate INJECTED first in Tier 1).

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

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2 within Phase 1. Continue until YES.]

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

[Result YES -> re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective /
                                  NO -- Inertia-Advocate INJECTED]
  [NO -> Inertia-Advocate INJECTED -- Tier: 1 (speaks first) -- Orientation: switching-cost
   investigation from ## INERTIA RECORD -- CITE obligation: at least one INERTIA-FINDING-*
   label in Phase 3 voice]

---

## PHASE 3 -- PARTICIPANT VOICES

[Tier 1 -> Tier 2 -> Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by INERTIA CONTINUITY BRIDGE]

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___           [Tier 3 only]
RESPONDS-TO: "___" -- ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [___] ___
  [repeat per participant -- format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice
  prose is not permitted.
  All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

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
[one row per item: Owner Role -- specific action -- deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role -- objection citing INERTIA-FINDING-* label -- resolution path
 -- named authority -- concrete trigger]
[or: No dissent -- [reason]]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified` -- type not named; fails C-01
  FAILS: `Committee Type -- product review` -- non-standard label; use recognized types
PRINT: Agenda Item, Charter Source, Participants (one line each, format: [Role Name] -- [orientation]).
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

GATE-N evaluation:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: increment N; write INVESTIGATION-ATTEMPT-N label; rewrite all four findings; evaluate GATE-N;
  repeat until YES.
IF YES: proceed to ## INERTIA RECORD.

WRITE: ## INERTIA RECORD with one-phrase anchors for each finding from the passing attempt.
VALIDATE: each entry carries a content anchor -- not a bare label, not a placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: INERTIA INVARIANT -- both elements required:
  (1) commit reference: "sealed at PHASE-1-COMMIT"
  (2) modification prohibition: "findings may not be added, removed, or modified without
      reopening Phase 1"
VALIDATE: INERTIA INVARIANT carries both elements. Missing either fails.

PRINT: PHASE-1-COMMIT with bidirectionality clause:
  "modifications to that record require updating this commit; modifications to this commit
   require updating that record"
VALIDATE: both coupling directions present. One direction only fails.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- roles oriented to feasibility scrutiny, risk, or disruption; speak first.
ASSIGN: Tier 2 -- roles holding conditional approval; speak second.
ASSIGN: Tier 3 -- roles aligned with proposal goals; speak last.
ENFORCE: tie-break by institutional veto authority.

SORT-CHECK: print gate; if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES` -- name the qualifying participant.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate:
  -- Tier 1, speaks first -- orientation: switching costs from ## INERTIA RECORD
  -- ENFORCE: cites at least one INERTIA-FINDING-* label in Phase 3 voice
  -- ENFORCE: appears in ## STANCE MANIFEST

VALIDATE: INERTIA CONTINUITY BRIDGE present between Phase 2 and Phase 3. Missing section fails.
VALIDATE: YES declared only when a qualifying participant actually exists. YES without
  a qualifying participant fails -- this is a distinct failure axis from structural absence.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: Inertia-Advocate voice FIRST in Tier 1 if INJECTED.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before any prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST after all voices; one entry per participant: [Role Name] STANCE-TOKEN.
PRINT: STANCE INVARIANT -- both elements required:
  (1) "sealed at PHASE-3-COMMIT"
  (2) "stance entries may not be revised without reopening Phase 3"
VALIDATE: both elements present. Missing either fails.

PRINT: PHASE-3-COMMIT with bidirectionality clause:
  "modifications to that manifest require updating this commit; modifications to this commit
   require updating that manifest"
VALIDATE: both coupling directions present. One direction only fails.

---

**PHASE 4 fill rules:**

PRINT: TALLY line -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY counts.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) and Trigger (named artifact +
  recipient + authority). Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority, concrete trigger.
ENFORCE: if no dissent -- `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-02 -- Rewrite-before-Proceed Loop

**Axis:** Rewrite-before-proceed loop
**Hypothesis:** Replacing the implicit "increment and retry" instruction with an explicit STOP-DISCARD-REWRITE signal prevents the failure mode where the model appends revised findings below the old attempt rather than replacing them. The gate becomes a hard restart, not a soft continuation.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

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

[GATE-1 answer is NO -> see REWRITE PROTOCOL in Step 2 fill rules]

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

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___           [Tier 3 only]
RESPONDS-TO: "___" -- ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above --
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice
  prose is not permitted.
  All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

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

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified` -- type not named
  FAILS: `Committee Type -- product review` -- non-standard label
PRINT: Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT terminal line.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

EVALUATE GATE-N:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?

IF GATE-N ANSWER IS NO:
  *** REWRITE PROTOCOL ***
  STOP. Do not proceed to ## INERTIA RECORD.
  Discard all four findings from the current attempt entirely.
  Write a new header: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings (A, B, C, D) from scratch -- not revised, not extended: replaced.
  Write a new GATE-[N+1] block.
  Evaluate again. Repeat REWRITE PROTOCOL until a gate answers YES.
  *** END REWRITE PROTOCOL ***

IF GATE-N ANSWER IS YES:
  Proceed to ## INERTIA RECORD.

WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt's findings only.
VALIDATE: each entry carries a content anchor -- not a bare label, not a placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed,
  or modified without reopening Phase 1.`
VALIDATE: both elements present -- commit reference AND modification prohibition.
  FAILS (a): commit reference present, prohibition absent
  FAILS (b): line present but carries neither element
  FAILS (c): line absent entirely

PRINT: PHASE-1-COMMIT with bidirectionality clause naming both coupling directions.
VALIDATE: both directions present -- modifications to record require updating commit AND
  modifications to commit require updating record.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 -- feasibility scrutiny, risk, or disruption; speak first.
ASSIGN: Tier 2 -- conditional approval; speak second.
ASSIGN: Tier 3 -- aligned with proposal goals; speak last.
SORT-CHECK: print gate; if YES, reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES` -- name the qualifying participant.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists. YES without qualification fails
  as a distinct axis from structural absence.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: Inertia-Advocate FIRST in Tier 1 if INJECTED.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone line before any prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name specific approval condition.
REQUIRE (Tier 3): CITE: before endorsement; RESPONDS-TO: named concern before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared.
WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT with both elements.
PRINT: PHASE-3-COMMIT with bidirectionality clause. Both directions required.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions, Re-entry path (Owner + Trigger if not APPROVED).
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance; OR `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-03 -- Coupling Integrity Symmetry Declaration

**Axis:** Coupling integrity symmetry declaration
**Hypothesis:** A single named SYMMETRY DECLARATION block appearing before Phase 1 fill rules that explicitly pairs the INERTIA RECORD <-> PHASE-1-COMMIT coupling contract with the STANCE MANIFEST <-> PHASE-3-COMMIT coupling contract -- and asserts they must be structurally identical -- prevents asymmetric coverage. The model cannot satisfy one and skip the other when both are named together as a symmetric pair with a single validation gate.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

Execute in two steps: (1) print the skeleton, (2) fill it.

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

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2 within Phase 1. Continue until YES.]

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

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective /
                                  NO -- Inertia-Advocate INJECTED]

---

## PHASE 3 -- PARTICIPANT VOICES

### ___ -- Tier ___

STANCE: ___
___
CITE: ___ -- ___           [Tier 3 only]
RESPONDS-TO: "___" -- ___  [Tier 3 only]

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

## SYMMETRY DECLARATION -- READ BEFORE ANY PHASE FILL

This simulation uses two sealing contracts. They are structurally identical. Both must be present.
Both must carry both coupling directions. A partial implementation of either fails both.

COUPLING PAIR A -- Phase 1:
  Subjects: ## INERTIA RECORD  <->  PHASE-1-COMMIT
  Forward:  modifications to ## INERTIA RECORD require updating PHASE-1-COMMIT
  Reverse:  modifications to PHASE-1-COMMIT require updating ## INERTIA RECORD
  Both directions must appear verbatim in PHASE-1-COMMIT body.

COUPLING PAIR B -- Phase 3:
  Subjects: ## STANCE MANIFEST  <->  PHASE-3-COMMIT
  Forward:  modifications to ## STANCE MANIFEST require updating PHASE-3-COMMIT
  Reverse:  modifications to PHASE-3-COMMIT require updating ## STANCE MANIFEST
  Both directions must appear verbatim in PHASE-3-COMMIT body.

SYMMETRY CHECK -- after filling both commits, verify:
  [ ] PHASE-1-COMMIT contains both coupling directions for INERTIA RECORD
  [ ] PHASE-3-COMMIT contains both coupling directions for STANCE MANIFEST
  [ ] The structure of both clauses is identical -- same pattern, different subjects
  Any checkbox not ticked = coupling integrity failure.

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

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

GATE-N:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: increment N; write new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; new GATE-N; repeat.
IF YES: proceed.

WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt.
VALIDATE: each entry is a content anchor, not a bare label or placeholder.
PRINT: INERTIA INVARIANT -- both elements: commit reference AND modification prohibition.
PRINT: PHASE-1-COMMIT -- COUPLING PAIR A both directions required per SYMMETRY DECLARATION.
VALIDATE: forward and reverse directions both present.

---

**PHASE 2 fill rules:**

ASSIGN tiers per challenger-first rule.
SORT-CHECK: if YES, reassign and loop.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES` -- name the qualifying participant.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present. Missing fails.
VALIDATE: YES only when qualifying participant exists. YES without qualification is a
  distinct failure axis from structural absence.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: Inertia-Advocate FIRST in Tier 1 if INJECTED.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name specific approval condition.
REQUIRE (Tier 3): CITE: before endorsement; RESPONDS-TO: named concern before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared.
WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required.
PRINT: PHASE-3-COMMIT -- COUPLING PAIR B both directions required per SYMMETRY DECLARATION.
VALIDATE: forward and reverse directions both present.

After filling PHASE-3-COMMIT, run SYMMETRY CHECK from SYMMETRY DECLARATION above.
All three checkboxes must be ticked before proceeding to Phase 4.

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions, Re-entry path (Owner + Trigger if not APPROVED).
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance with INERTIA-FINDING-* citation.
  OR: `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-04 -- Pre-skeleton Rule Block + Rewrite-before-Proceed Loop

**Axis:** C-12 + C-13 combination
**Hypothesis:** The CONSTRAINTS preamble activates the most critical rules before the skeleton is printed; the STOP-DISCARD-REWRITE protocol in Phase 1 prevents incremental-append loop failures. Together they close two failure modes that operate independently: front-of-fill knowledge gap (preamble) and partial retry loop (rewrite protocol).

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

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain both (a) "sealed at
   PHASE-1-COMMIT" and (b) the modification prohibition. Both required; either alone fails.

3. COUPLING INTEGRITY: PHASE-1-COMMIT carries both coupling directions for INERTIA RECORD.
   PHASE-3-COMMIT carries both coupling directions for STANCE MANIFEST. One direction only
   fails. Both commits require this treatment.

4. GATE LOOP -- REWRITE PROTOCOL: If a gate answers NO, halt and fully rewrite all four
   findings from scratch before proceeding. See Phase 1 fill rules for the explicit
   STOP-DISCARD-REWRITE instruction.

5. STANCE MANIFEST: One entry per participant -- [Role Name] STANCE-TOKEN. Tally counts
   tokens here; do not re-parse Phase 3 prose.

6. ACTION ITEMS: Three fields per item -- Owner Role, specific action, deadline. Missing
   any field fails.

7. INERTIA CONTINUITY BRIDGE: Present between Phase 2 and Phase 3. YES requires a
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

[GATE-1 NO -> REWRITE PROTOCOL -- see Step 2 fill rules]

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

Inertia owner in tier sort: ___ [YES / NO -- with consequence]

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
  STOP immediately. Do not write ## INERTIA RECORD. Do not proceed past Phase 1.
  Discard all four findings from the current attempt entirely. They do not carry forward.
  Write: ### INVESTIGATION-ATTEMPT-[N+1]
  Rewrite all four findings completely from scratch -- different workflow, different surface,
    different team, different switching cost. Not revised. Not extended. Replaced.
  Write GATE-[N+1] and evaluate.
  If NO again -- execute REWRITE PROTOCOL again from the top.
  Repeat until a gate answers YES.
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
PRINT: PHASE-1-COMMIT with both coupling directions for INERTIA RECORD (per CONSTRAINTS rule 3).

---

**PHASE 2 fill rules:**

ASSIGN tiers per challenger-first rule.
SORT-CHECK: if YES, reassign and loop.
PRINT: PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule:**

INSPECT: Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to switching-cost
  investigation, status-quo defense, or cost-of-change analysis.
IF YES: confirm `Inertia owner in tier sort: YES` -- name the qualifying participant.
IF NO: confirm `Inertia owner in tier sort: NO` and INJECT Inertia-Advocate as Tier 1,
  speaks first; cites at least one INERTIA-FINDING-* label; appears in ## STANCE MANIFEST.

VALIDATE: bridge present between Phase 2 and Phase 3.
VALIDATE: YES only when qualifying participant actually exists. YES without qualification
  is a distinct failure axis from structural absence.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: Inertia-Advocate FIRST in Tier 1 if INJECTED.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name specific approval condition.
REQUIRE (Tier 3): CITE: before endorsement; RESPONDS-TO: named concern before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared.
WRITE: ## STANCE MANIFEST -- [Role Name] STANCE-TOKEN per participant.
PRINT: STANCE INVARIANT -- both elements required.
PRINT: PHASE-3-COMMIT with both coupling directions for STANCE MANIFEST (per CONSTRAINTS rule 3).

---

**PHASE 4 fill rules:**

PRINT: TALLY -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME.
PRINT: PHASE-4-COMMIT terminal line.

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions, Re-entry path (Owner + Trigger if not APPROVED).
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance; OR `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT terminal line.
```

---

## V-05 -- Full Integration (C-12 + C-13 + C-14)

**Axis:** C-12 + C-13 + C-14 full integration
**Hypothesis:** When all three v3 mechanisms co-present -- CONSTRAINTS preamble (C-12), STOP-DISCARD-REWRITE gate (C-13), and SYMMETRY DECLARATION with post-Phase-3 symmetry check (C-14) -- the output earns all three new v3 aspirational criteria on top of the full essential and prior-round recommended pass set. Each mechanism targets a distinct failure mode; together they form a non-redundant coverage set.

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

2. INERTIA RECORD SEALING: INERTIA INVARIANT must contain (a) "sealed at PHASE-1-COMMIT"
   AND (b) the modification prohibition. Both required; either alone fails.

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
VALIDATE: both present. Missing either fails on three axes:
  FAILS (a): commit reference present, prohibition absent
  FAILS (b): line present with neither element
  FAILS (c): line absent entirely

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
