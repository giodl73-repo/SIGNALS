---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-16
round: 6
rubric_version: 6
---

# corps-committee -- Prompt Variations R6

## Variation Summary

| ID   | Axis                                                              | Hypothesis |
|------|-------------------------------------------------------------------|------------|
| V-01 | Phase 3 Voice Completeness Check (lifecycle emphasis -- skeleton-embedded gate before STANCE MANIFEST) | A `## VOICE COMPLETENESS CHECK` block embedded in the skeleton after all participant voices but before `## STANCE MANIFEST` converts voice-element enforcement (currently only in fill-rule prose) into a structural gate that must be fully ticked before the manifest is written. Per-tier checklists -- STANCE: label, citation for Tier 1, specific condition for Tier 2, CITE: + RESPONDS-TO: for Tier 3 -- make missing voice elements visible as unfilled checkboxes rather than silent omissions. Applies the INERTIA CITATION AUDIT per-finding-enumeration pattern to voice structural completeness. |
| V-02 | Phase-tagged Constraints Table (output format -- numbered list replaced by phase-keyed table) | Replacing the CONSTRAINTS numbered list with a two-section phase-tagged table (one row per gate, columns: Gate / Phase / Halt Trigger) makes each constraint's governing phase explicit at a glance. Models reading ahead to a phase can identify applicable constraints without re-scanning 12 items in a flat list. Hypothesis: constraint-miss failures where a model correctly executes a phase but ignores a governing constraint are caused by the flat-list format decoupling constraint from phase; a phase-keyed table closes that coupling gap. |
| V-03 | Dissent Inertia Linkage (inertia framing -- 6th checkbox in MINUTES INTEGRITY CHECK) | Adding a 6th checkbox to `## MINUTES INTEGRITY CHECK` requiring at least one DISSENTING OPINIONS entry to explicitly cite an INERTIA-FINDING-* label by token form closes the Phase 1 -> Phase 5 traceability gap. The INERTIA CITATION AUDIT closes Phase 1 -> Phase 3 continuity; without a parallel Phase 5 requirement, Phase 1 findings can satisfy all structural checks while remaining absent from the final minutes record. The new checkbox mirrors how INERTIA CITATION AUDIT converted the audit into a per-finding enumeration -- it converts dissent inertia linkage from a prose best-practice into a structural halt condition. |
| V-04 | Voice Completeness + Dissent Inertia Linkage (V-01 + V-03)       | V-01 and V-03 target distinct phase-boundary gaps -- Phase 3 exit and Phase 5 inertia traceability -- with no structural interaction. Co-applying both provides additive coverage: voice completeness failures caught before STANCE MANIFEST, inertia traceability failures caught before Phase 5 is written. |
| V-05 | Full R6 Integration (V-01 + V-02 + V-03 on R5 V-05 foundation)  | All three R6 axes applied together: Voice Completeness Check (Phase 3 exit gate), phase-tagged constraints table (format), and Dissent Inertia Linkage (Phase 5 gate) layered on top of the complete R5 V-05 foundation (Committee Type Gate + Bridge expansion + Tally Ledger Protocol). Each axis targets a distinct structural gap with no overlap; together they extend skeleton-gating to every major phase boundary not yet covered. |

---

## V-01 -- Phase 3 Voice Completeness Check

**Axis:** Lifecycle emphasis -- skeleton-embedded `## VOICE COMPLETENESS CHECK` block between participant voices and STANCE MANIFEST
**Hypothesis:** A `## VOICE COMPLETENESS CHECK` block embedded in the Phase 3 skeleton after all participant voices but before `## STANCE MANIFEST` converts voice-element enforcement (currently only in Phase 3 fill-rule prose) into a structural gate. Per-tier checklists make missing STANCE: labels, Tier 1 citation omissions, Tier 2 generic conditions, and missing Tier 3 CITE:/RESPONDS-TO: fields visible as unfilled checkboxes rather than silent omissions. The pattern applies the INERTIA CITATION AUDIT per-finding enumeration mechanism to voice structural completeness -- the same structural defect that INERTIA CITATION AUDIT catches for finding coverage, this gate catches for voice element coverage.

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

11. COMMITTEE TYPE GATE: Both checkboxes in the skeleton block must be ticked before
    PHASE-0-COMMIT seals. Any unticked box halts Phase 0. Acceptable types: ROB,
    shiproom, arch-board, or user-specified named type. Generic descriptions fail.

12. TALLY LEDGER PROTOCOL: Before writing TALLY, execute the named ledger protocol in
    Phase 4 fill rules. Ledger must enumerate each STANCE MANIFEST entry, assign tokens,
    sum independently, and cross-check against Phase 0 participant count. Discrepancy
    halts Phase 4.

13. VOICE COMPLETENESS CHECK: All applicable checkboxes in the skeleton block must be
    ticked before ## STANCE MANIFEST is written. Any unticked box halts Phase 3.
    Per-tier requirements: Tier 1 -- STANCE: label + named INERTIA-FINDING-* citation;
    Tier 2 -- STANCE: label + specific condition named; Tier 3 -- STANCE: label + CITE:
    field with INERTIA-FINDING-* label + RESPONDS-TO: field naming a specific concern.

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

LOAD: charter from `.craft/roles/` matching this committee type.
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

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:

  Step 1: Set `Inspection complete: YES`.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists:
    Set `Decision: YES -- inertia owner present`.
    Complete OWNER RECORD: name the qualifying participant and confirm inertia orientation.
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
    ## VOICE COMPLETENESS CHECK.
    Execute TIER SEQUENCE PROTOCOL again from the top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared. All-APPROVE reopens Phase 2.

After all voices are written, COMPLETE ## VOICE COMPLETENESS CHECK:
  For each Tier 1 voice: tick STANCE: label box; tick INERTIA-FINDING-* citation box.
  For each Tier 2 voice: tick STANCE: label box; tick specific-condition box.
  For each Tier 3 voice: tick STANCE: label box; tick CITE: box; tick RESPONDS-TO: box.
  Any unticked box -- halt. Identify the deficient voice. Revise it. Re-check.
  ## STANCE MANIFEST may not be written until all applicable boxes are ticked.

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
  Include: `VOICE COMPLETENESS CHECK ticked. INERTIA CITATION AUDIT RESULT is COMPLETE.`
VALIDATE: forward AND reverse directions both present.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton.
All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL block before printing TALLY line:
  ENUMERATE: each ## STANCE MANIFEST entry by participant name and token.
  COUNT: APPROVE tokens, CONDITION tokens, BLOCK tokens independently.
  CROSS-CHECK: total count equals participant count from Phase 0 roster.
  DECLARE: `TALLY RESULT: QUORUM MET` if total count correct.
    If count mismatch: `TALLY RESULT: COUNT MISMATCH -- halt`; identify discrepancy;
    do not proceed until resolved.
  ENFORCE: PHASE-4-COMMIT may not proceed until TALLY RESULT is declared.

PRINT: TALLY -- count from ## TALLY LEDGER PROTOCOL; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT -- include "TALLY LEDGER PROTOCOL complete, TALLY RESULT declared."

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block:
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

## V-02 -- Phase-tagged Constraints Table

**Axis:** Output format -- numbered CONSTRAINTS list replaced by phase-keyed structural table
**Hypothesis:** The numbered list format (1-12 items) requires models to mentally map each constraint to its governing phase. Constraint-miss failures occur when a model correctly executes a phase but ignores a governing constraint that appeared 8+ items earlier in the flat list. A phase-tagged table -- one row per gate, columns: Gate Name / Governs Phase(s) / Halt Trigger -- makes the phase coupling explicit and scannable. When filling Phase 3, the model can look up `Phase 3` rows directly rather than re-reading 12 items sequentially. The table format also eliminates the implicit ranking signal of numbered items (where lower-numbered constraints feel more important).

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

| Gate Name                    | Governs         | Halt Trigger                                              |
|------------------------------|-----------------|-----------------------------------------------------------|
| COMMIT PLACEMENT             | All phases      | Content found after any PHASE-N-COMMIT within same phase  |
| COMMITTEE TYPE GATE          | Phase 0         | Unticked checkbox before PHASE-0-COMMIT                   |
| INERTIA RECORD SEALING       | Phase 1         | INERTIA INVARIANT missing commit ref or modification ban  |
| COUPLING INTEGRITY -- P1     | Phase 1         | PHASE-1-COMMIT missing one coupling direction             |
| GATE LOOP / REWRITE PROTOCOL | Phase 1         | Phase 1 closes with GATE-N Answer: NO                     |
| INERTIA CONTINUITY BRIDGE    | Phase 2->3      | BRIDGE RESULT undeclared; YES with no qualifying owner    |
| TIER SEQUENCE PROTOCOL       | Phase 3         | Voice order violates Tier 1->2->3; Inertia-Advocate not first if INJECTED |
| INERTIA CITATION AUDIT       | Phase 3         | AUDIT RESULT not COMPLETE before PHASE-3-COMMIT           |
| COUPLING INTEGRITY -- P3     | Phase 3         | PHASE-3-COMMIT missing one coupling direction             |
| SYMMETRY CHECK               | Phase 3->4      | Unticked checkbox before Phase 4                          |
| STANCE MANIFEST              | Phase 3->4      | Entry missing or format not [Role Name] STANCE-TOKEN      |
| TALLY LEDGER PROTOCOL        | Phase 4         | Count mismatch or TALLY RESULT undeclared                 |
| MINUTES INTEGRITY CHECK      | Phase 4->5      | Unticked checkbox before Phase 5                          |
| ACTION ITEMS                 | Phase 5         | Item missing Owner Role, specific action, or deadline     |

All gates are mandatory. A gate that governs multiple phases must pass at each applicable boundary.

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

LOAD: charter from `.craft/roles/` matching this committee type.
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

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:

  Step 1: Set `Inspection complete: YES`.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists:
    Set `Decision: YES -- inertia owner present`.
    Complete OWNER RECORD: name the qualifying participant and confirm inertia orientation.
    Set `BRIDGE RESULT: OWNER-PRESENT`.
  Step 4: If no such participant exists:
    Set `Decision: NO -- Inertia-Advocate INJECTED`.
    Complete INJECTION RECORD and set `BRIDGE RESULT: INJECTED`.

VALIDATE: BRIDGE RESULT declared. Undeclared BRIDGE RESULT halts Phase 3.
VALIDATE: Decision is YES only when a qualifying participant actually exists.

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
  Step 5: If any ordering violation detected -- STOP. Do not proceed.
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

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block in the skeleton.
All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL block before printing TALLY line:
  ENUMERATE: each ## STANCE MANIFEST entry by participant name and token.
  COUNT: APPROVE tokens, CONDITION tokens, BLOCK tokens independently.
  CROSS-CHECK: total count equals participant count from Phase 0 roster.
  DECLARE: `TALLY RESULT: QUORUM MET` if total count correct; halt on mismatch.
  ENFORCE: PHASE-4-COMMIT may not proceed until TALLY RESULT is declared.

PRINT: TALLY -- count from ## TALLY LEDGER PROTOCOL; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT -- include "TALLY LEDGER PROTOCOL complete, TALLY RESULT declared."

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block:
  Tick all five boxes. Any unticked box halts Phase 5.

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

## V-03 -- Dissent Inertia Linkage

**Axis:** Inertia framing -- 6th checkbox in `## MINUTES INTEGRITY CHECK` requiring explicit INERTIA-FINDING-* citation in at least one DISSENTING OPINIONS entry
**Hypothesis:** The current 5-checkbox MINUTES INTEGRITY CHECK ensures dissent is structurally present but does not require that dissent trace back to Phase 1 inertia findings. Phase 1 and Phase 5 can each satisfy all structural checks while remaining semantically disconnected: Phase 1 findings are cited in Phase 3 voices (enforced by INERTIA CITATION AUDIT) but are not required to appear in the final minutes record. Adding a 6th checkbox -- at least one DISSENTING OPINIONS entry explicitly cites an INERTIA-FINDING-* label by token form, OR explicit No dissent with inertia linkage justification -- closes the Phase 1 -> Phase 5 traceability gap. The pattern mirrors INERTIA CITATION AUDIT's Phase 1 -> Phase 3 enforcement, extending the same label-token citation requirement into Phase 5.

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

10. MINUTES INTEGRITY CHECK: All six checkboxes in the skeleton block must be ticked
    before Phase 5 content is generated. Any unticked box halts Phase 5.

11. COMMITTEE TYPE GATE: Both checkboxes in the skeleton block must be ticked before
    PHASE-0-COMMIT seals. Any unticked box halts Phase 0. Acceptable types: ROB,
    shiproom, arch-board, or user-specified named type. Generic descriptions fail.

12. TALLY LEDGER PROTOCOL: Before writing TALLY, execute the named ledger protocol in
    Phase 4 fill rules. Ledger must enumerate each STANCE MANIFEST entry, assign tokens,
    sum independently, and cross-check against Phase 0 participant count. Discrepancy
    halts Phase 4.

13. DISSENT INERTIA LINKAGE: At least one DISSENTING OPINIONS entry must explicitly cite
    an INERTIA-FINDING-* label by token form -- OR dissent must be declared absent with
    explicit inertia linkage justification. The linkage checkbox in MINUTES INTEGRITY
    CHECK must be ticked before Phase 5 is written.

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
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  [ ] DISSENT INERTIA LINKAGE: at least one DISSENTING OPINIONS entry explicitly cites
      an INERTIA-FINDING-* label by token form -- OR "No dissent" declared with explicit
      "No inertia linkage required -- [justification]"
  All six boxes ticked before Phase 5 content is generated.

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
  Owner and Trigger present if verdict not APPROVED. DISSENT INERTIA LINKAGE ticked.
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

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails coupling integrity.
  Satisfying Pair B and omitting Pair A also fails. Both pairs must be present and
  structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified`
  FAILS: `Committee Type: product review`
PRINT: Agenda Item, Charter Source, Participants.
COMPLETE ## COMMITTEE TYPE GATE before printing PHASE-0-COMMIT:
  Tick both checkboxes. Any unticked box halts Phase 0.
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

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:
  Step 1: Set Inspection complete: YES.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists -- set Decision: YES; complete OWNER RECORD; set BRIDGE RESULT: OWNER-PRESENT.
  Step 4: If no such participant -- set Decision: NO; complete INJECTION RECORD; set BRIDGE RESULT: INJECTED.
VALIDATE: BRIDGE RESULT declared. Undeclared BRIDGE RESULT halts Phase 3.
VALIDATE: Decision is YES only when a qualifying participant actually exists.

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
    current voice tier equals or exceeds the previous voice tier.
  Step 5: If any ordering violation detected -- STOP. Execute TIER SEQUENCE PROTOCOL again.
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

COMPLETE ## INERTIA CITATION AUDIT before printing PHASE-3-COMMIT.
  Set AUDIT RESULT COMPLETE if all four labels cited or justified; halt if INCOMPLETE.

PRINT: PHASE-3-COMMIT -- COUPLING PAIR B per SYMMETRY DECLARATION. Both directions required.
  Include: `INERTIA CITATION AUDIT RESULT is COMPLETE.`

After PHASE-3-COMMIT, complete SYMMETRY CHECK. All three boxes must be ticked.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL block:
  ENUMERATE each ## STANCE MANIFEST entry. COUNT each token type independently.
  CROSS-CHECK total against Phase 0 participant count.
  DECLARE TALLY RESULT. PHASE-4-COMMIT may not proceed until TALLY RESULT declared.
PRINT: TALLY line. WRITE: OUTCOME. PRINT: PHASE-4-COMMIT.

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block:
  Tick first five boxes per standard rules.
  Tick sixth box -- DISSENT INERTIA LINKAGE:
    IF any DISSENTING OPINIONS entry: confirm at least one explicitly cites
      an INERTIA-FINDING-* label by token form.
      If none does: revise the most relevant dissent entry to add explicit label citation.
    IF no dissent: write `No dissent -- [reason] -- No inertia linkage required --
      [justification why inertia findings are moot in this decision]`.
  All six checkboxes must be ticked. Any unticked box halts Phase 5.

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role) AND Trigger (named artifact + recipient + authority).
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline].
WRITE: dissent per CONDITION/BLOCK stance -- citing INERTIA-FINDING-* label by token form,
  resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason] -- No inertia linkage required -- [justification]`.
PRINT: PHASE-5-COMMIT -- include "DISSENT INERTIA LINKAGE ticked."
```

---

## V-04 -- Voice Completeness + Dissent Inertia Linkage (V-01 + V-03)

**Axis:** Lifecycle emphasis + inertia framing -- VOICE COMPLETENESS CHECK gate at Phase 3 exit combined with DISSENT INERTIA LINKAGE as 6th MINUTES INTEGRITY CHECK checkbox
**Hypothesis:** V-01 and V-03 target distinct structural gaps at different phase boundaries (Phase 3 exit and Phase 5 inertia traceability) with no mechanism overlap. V-01 catches voice element omissions before STANCE MANIFEST is written; V-03 catches Phase 1 -> Phase 5 traceability breaks before Phase 5 content is generated. Co-applying both provides additive coverage across the two unguarded transitions. Neither gate interacts with the other: VOICE COMPLETENESS CHECK governs voice structure within Phase 3; DISSENT INERTIA LINKAGE governs Phase 1 finding carrythrough into Phase 5 minutes.

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

10. MINUTES INTEGRITY CHECK: All six checkboxes in the skeleton block must be ticked
    before Phase 5 content is generated. Any unticked box halts Phase 5.

11. COMMITTEE TYPE GATE: Both checkboxes in the skeleton block must be ticked before
    PHASE-0-COMMIT seals. Any unticked box halts Phase 0. Acceptable types: ROB,
    shiproom, arch-board, or user-specified named type. Generic descriptions fail.

12. TALLY LEDGER PROTOCOL: Before writing TALLY, execute the named ledger protocol in
    Phase 4 fill rules. Ledger must enumerate each STANCE MANIFEST entry, assign tokens,
    sum independently, and cross-check against Phase 0 participant count. Discrepancy
    halts Phase 4.

13. VOICE COMPLETENESS CHECK: All applicable checkboxes in the skeleton block must be
    ticked before ## STANCE MANIFEST is written. Any unticked box halts Phase 3.
    Per-tier requirements: Tier 1 -- STANCE: label + named INERTIA-FINDING-* citation;
    Tier 2 -- STANCE: label + specific condition named; Tier 3 -- STANCE: label + CITE:
    field with INERTIA-FINDING-* label + RESPONDS-TO: field naming a specific concern.

14. DISSENT INERTIA LINKAGE: At least one DISSENTING OPINIONS entry must explicitly cite
    an INERTIA-FINDING-* label by token form -- OR dissent must be declared absent with
    explicit inertia linkage justification. The linkage checkbox in MINUTES INTEGRITY
    CHECK must be ticked before Phase 5 is written.

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
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  [ ] DISSENT INERTIA LINKAGE: at least one DISSENTING OPINIONS entry explicitly cites
      an INERTIA-FINDING-* label by token form -- OR "No dissent" declared with explicit
      "No inertia linkage required -- [justification]"
  All six boxes ticked before Phase 5 content is generated.

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
  Owner and Trigger present if verdict not APPROVED. DISSENT INERTIA LINKAGE ticked.
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

SYMMETRY RULE: satisfying Pair A and omitting Pair B fails. Both pairs must be present
  and structurally parallel.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified` / `Committee Type: product review`
PRINT: Agenda Item, Charter Source, Participants.
COMPLETE ## COMMITTEE TYPE GATE -- tick both boxes. Any unticked box halts Phase 0.
PRINT: PHASE-0-COMMIT -- include "COMMITTEE TYPE GATE ticked."

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE four INERTIA-FINDING labels (A specific workflow; B integration surface; C team + habit; D non-obvious cost).
EVALUATE GATE-N. IF NO: execute REWRITE PROTOCOL (STOP, discard, new attempt, repeat until YES).
IF YES: WRITE ## INERTIA RECORD (one-phrase anchors, no bare labels or placeholders).
PRINT INERTIA INVARIANT (both elements: commit ref + prohibition).
PRINT PHASE-1-COMMIT (COUPLING PAIR A, both directions).

---

**PHASE 2 fill rules:**

ASSIGN tiers. SORT-CHECK. Loop until NO. PRINT PHASE-2-COMMIT terminal line.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:
  Inspection: YES. INSPECT for inertia-oriented Tier 1/2 participant.
  Decision: YES (OWNER-PRESENT) or NO (INJECTED). Declare BRIDGE RESULT.
VALIDATE: BRIDGE RESULT declared. YES requires qualifying participant in OWNER RECORD.

---

**PHASE 3 fill rules:**

Execute TIER SEQUENCE PROTOCOL before any voice:
  *** TIER SEQUENCE PROTOCOL ***
  Determine sequence from BRIDGE RESULT and TIER SORT.
  INJECTED: Inertia-Advocate first in Tier 1; others follow; then Tier 2; then Tier 3.
  OWNER-PRESENT: Tier 1 institutional veto order; Tier 2; Tier 3.
  After each voice: confirm tier >= previous tier. Violation -> STOP; restart protocol.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT STANCE: standalone line. WRITE 2-4 sentences from charter orientation.
Tier 1: cite named INERTIA-FINDING-* label. Tier 2: name specific condition.
Tier 3: CITE: [label -- content]; RESPONDS-TO: "[concern]" -- [one sentence].
VALIDATE: at least one CONDITION or BLOCK.

After all voices, COMPLETE ## VOICE COMPLETENESS CHECK:
  Tick all applicable per-tier boxes. Any unticked box -- halt; revise deficient voice; re-check.
  ## STANCE MANIFEST may not be written until all applicable boxes are ticked.

WRITE ## STANCE MANIFEST. PRINT STANCE INVARIANT (both elements).
COMPLETE ## INERTIA CITATION AUDIT. Set AUDIT RESULT COMPLETE or halt.
PRINT PHASE-3-COMMIT (COUPLING PAIR B; include "VOICE COMPLETENESS CHECK ticked. INERTIA CITATION AUDIT RESULT is COMPLETE.").
Complete SYMMETRY CHECK. All three boxes must be ticked.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL: enumerate entries, count tokens, cross-check total, declare TALLY RESULT.
PRINT TALLY. WRITE OUTCOME. PRINT PHASE-4-COMMIT.

---

**PHASE 5 fill rules:**

Complete MINUTES INTEGRITY CHECK -- all six boxes:
  Boxes 1-5: standard rules.
  Box 6 (DISSENT INERTIA LINKAGE): if dissent exists -- confirm INERTIA-FINDING-* token cited;
    if not -- revise to add. If no dissent -- write No dissent + No inertia linkage required + justification.
  All six ticked before Phase 5 content written.

WRITE Verdict. WRITE Conditions. REQUIRE Owner + Trigger if not APPROVED.
PRINT action items (all three fields). WRITE dissent with INERTIA-FINDING-* label citation.
PRINT PHASE-5-COMMIT -- include "DISSENT INERTIA LINKAGE ticked."
```

---

## V-05 -- Full R6 Integration (V-01 + V-02 + V-03)

**Axis:** All three R6 axes combined: Voice Completeness Check (lifecycle emphasis) + Phase-tagged Constraints Table (output format) + Dissent Inertia Linkage (inertia framing), layered on the R5 V-05 foundation
**Hypothesis:** V-01 targets Phase 3 exit (voice completeness), V-02 targets the constraint-discovery mechanism (phase-tagged table), and V-03 targets Phase 5 inertia traceability. None of these axes interacts with the others mechanically. V-02 replaces the format of the constraint declaration block only; the skeleton and fill rules are identical to V-04. Together the three axes: close the Phase 3 voice-element gap (V-01), improve per-phase constraint recall (V-02), and close the Phase 1 -> Phase 5 inertia traceability gap (V-03). This variation earns all three R6 criteria plus carries all R5 criteria.

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

| Gate Name                    | Governs         | Halt Trigger                                                             |
|------------------------------|-----------------|--------------------------------------------------------------------------|
| COMMIT PLACEMENT             | All phases      | Content found after any PHASE-N-COMMIT within same phase                 |
| COMMITTEE TYPE GATE          | Phase 0         | Unticked checkbox before PHASE-0-COMMIT                                  |
| INERTIA RECORD SEALING       | Phase 1         | INERTIA INVARIANT missing commit ref or modification prohibition          |
| COUPLING INTEGRITY -- P1     | Phase 1         | PHASE-1-COMMIT missing one coupling direction                            |
| GATE LOOP / REWRITE PROTOCOL | Phase 1         | Phase 1 closes with GATE-N Answer: NO                                    |
| INERTIA CONTINUITY BRIDGE    | Phase 2->3      | BRIDGE RESULT undeclared; or YES with no qualifying owner                |
| TIER SEQUENCE PROTOCOL       | Phase 3         | Voice order violates Tier 1->2->3; Inertia-Advocate not first if INJECTED|
| VOICE COMPLETENESS CHECK     | Phase 3         | Unticked per-tier checkbox before ## STANCE MANIFEST                     |
| INERTIA CITATION AUDIT       | Phase 3         | AUDIT RESULT not COMPLETE before PHASE-3-COMMIT                          |
| COUPLING INTEGRITY -- P3     | Phase 3         | PHASE-3-COMMIT missing one coupling direction                            |
| SYMMETRY CHECK               | Phase 3->4      | Unticked checkbox before Phase 4                                         |
| STANCE MANIFEST              | Phase 3->4      | Entry missing or format not [Role Name] STANCE-TOKEN                     |
| TALLY LEDGER PROTOCOL        | Phase 4         | Count mismatch or TALLY RESULT undeclared                                |
| MINUTES INTEGRITY CHECK      | Phase 4->5      | Unticked checkbox (incl. DISSENT INERTIA LINKAGE) before Phase 5         |
| DISSENT INERTIA LINKAGE      | Phase 5         | No INERTIA-FINDING-* token cited in dissent; no linkage justification    |
| ACTION ITEMS                 | Phase 5         | Item missing Owner Role, specific action, or deadline                    |

All gates are mandatory. A gate governing multiple phases must pass at each applicable boundary.

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
  [ ] At least two ACTION ITEMS, each with all three fields: Owner Role, specific action,
      deadline
  [ ] DISSENTING OPINIONS complete: one entry per CONDITION or BLOCK stance citing an
      INERTIA-FINDING-* label, OR explicit "No dissent -- [reason]"
  [ ] If verdict is not APPROVED: Owner and Trigger both present in Re-entry path
  [ ] DISSENT INERTIA LINKAGE: at least one DISSENTING OPINIONS entry explicitly cites
      an INERTIA-FINDING-* label by token form -- OR "No dissent" declared with explicit
      "No inertia linkage required -- [justification]"
  All six boxes ticked before Phase 5 content is generated.

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
  Owner and Trigger present if verdict not APPROVED. DISSENT INERTIA LINKAGE ticked.
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

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified named type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified` / `Committee Type: product review`
PRINT: Agenda Item, Charter Source, Participants.
COMPLETE ## COMMITTEE TYPE GATE -- tick both boxes. Any unticked box halts Phase 0.
PRINT: PHASE-0-COMMIT -- include "COMMITTEE TYPE GATE ticked."

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
WRITE: ## INERTIA RECORD with one-phrase anchors from the passing attempt only.
VALIDATE: each entry is a content anchor -- not a bare label, not a placeholder.

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

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

COMPLETE the ## INERTIA CONTINUITY BRIDGE skeleton block:
  Step 1: Set Inspection complete: YES.
  Step 2: INSPECT Phase 2 TIER SORT for any Tier 1 or Tier 2 participant oriented to
    switching-cost investigation, status-quo defense, or cost-of-change analysis.
  Step 3: If such participant exists:
    Set Decision: YES. Complete OWNER RECORD (name + inertia orientation).
    Set BRIDGE RESULT: OWNER-PRESENT.
  Step 4: If no such participant:
    Set Decision: NO. Complete INJECTION RECORD (Inertia-Advocate, Tier 1 position 1,
    STANCE MANIFEST placeholder YES, citation requirement).
    Set BRIDGE RESULT: INJECTED.
VALIDATE: BRIDGE RESULT declared. YES requires qualifying participant in OWNER RECORD.
  YES without qualifying participant is a distinct failure axis from structural absence.

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
    current voice tier equals or exceeds the previous voice tier.
  Step 5: If any ordering violation detected -- STOP. Do not proceed.
    Execute TIER SEQUENCE PROTOCOL again from the top.
  *** END TIER SEQUENCE PROTOCOL ***

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement;
  RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
VALIDATE: at least one CONDITION or BLOCK declared. All-APPROVE reopens Phase 2.

After all voices, COMPLETE ## VOICE COMPLETENESS CHECK:
  For each Tier 1 voice: tick STANCE: label box; tick INERTIA-FINDING-* citation box.
  For each Tier 2 voice: tick STANCE: label box; tick specific-condition box.
  For each Tier 3 voice: tick STANCE: label box; tick CITE: box; tick RESPONDS-TO: box.
  Any unticked box -- halt. Identify deficient voice. Revise. Re-check.
  ## STANCE MANIFEST may not be written until all applicable boxes are ticked.

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
  Include: `VOICE COMPLETENESS CHECK ticked. INERTIA CITATION AUDIT RESULT is COMPLETE.`
VALIDATE: forward AND reverse directions both present.

After writing PHASE-3-COMMIT, complete the SYMMETRY CHECK block.
All three checkboxes must be ticked. Any unticked box halts Phase 4.

---

**PHASE 4 fill rules:**

COMPLETE ## TALLY LEDGER PROTOCOL block before printing TALLY line:
  ENUMERATE: each ## STANCE MANIFEST entry by participant name and token.
  COUNT: APPROVE tokens, CONDITION tokens, BLOCK tokens independently.
  CROSS-CHECK: total count equals participant count from Phase 0 roster.
  DECLARE: `TALLY RESULT: QUORUM MET` if correct; `COUNT MISMATCH -- halt` if not.
  ENFORCE: PHASE-4-COMMIT may not proceed until TALLY RESULT is declared.

PRINT: TALLY -- count from ## TALLY LEDGER PROTOCOL; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT -- include "TALLY LEDGER PROTOCOL complete, TALLY RESULT declared."

---

**PHASE 5 fill rules:**

Before writing any Phase 5 content, complete the MINUTES INTEGRITY CHECK block:
  Tick boxes 1-5 per standard rules.
  Tick box 6 -- DISSENT INERTIA LINKAGE:
    IF any DISSENTING OPINIONS entry exists: confirm at least one explicitly cites
      an INERTIA-FINDING-* label by token form (e.g., "INERTIA-FINDING-B").
      If no entry cites by token form: revise the most relevant dissent entry to add
      explicit label citation before ticking this box.
    IF no dissent: write `No dissent -- [reason] -- No inertia linkage required --
      [justification explaining why inertia findings are moot in this decision]`.
  All six checkboxes must be ticked. Any unticked box halts Phase 5.

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) AND Trigger (named artifact +
  recipient + authority). Both required; missing either fails.
PRINT: action items -- [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label
  by token form, resolution path, named authority, concrete trigger.
  OR: `No dissent -- [reason] -- No inertia linkage required -- [justification]`.
PRINT: PHASE-5-COMMIT -- include "DISSENT INERTIA LINKAGE ticked."
```
