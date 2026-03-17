---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 18
rubric_version: 18
---

# corps-committee -- Prompt Variations R18

## Variation Summary

| ID   | Axis                                                                                          | Hypothesis |
|------|-----------------------------------------------------------------------------------------------|------------|
| V-01 | C-49 only -- BEFORE YOU START C-47 pre-flight cites "C-46 miss" with extended pair list      | Updating the C-47 pre-flight to name "C-46 miss" (the current governing criterion for C-44/C-45 template currency) and extending the pair list from "C-42, C-43, or any later pair" to "C-42, C-43, C-44, C-45, or any later pair" satisfies C-49 as a standalone change. The mechanism fires correctly and names the authoritative criterion. C-50 is NOT satisfied: the FAILS SYNTAX TEMPLATE carries entries through C-45 only -- no C-46, C-47, or C-48 entries. A reviewer inspecting the template for the C-47/C-48 triplet will find no canonical FAILS citation. |
| V-02 | C-50 only -- FAILS SYNTAX TEMPLATE extended with C-46/C-47/C-48 self-referential entries    | Adding CORRECT entries for C-46, C-47, and C-48 to the FAILS SYNTAX TEMPLATE satisfies C-50 (recursive currency extended to the R17 aspirational triplet). A reviewer encountering an ICB structural absence, a stale pre-flight citation, or a missing preamble pre-flight now has a canonical FAILS entry to cite. C-49 is NOT satisfied: BEFORE YOU START still carries the old pre-flight citing "C-44 miss" with the stale pair list "C-42, C-43, or any later pair." The halt fires but directs the reviewer to the wrong governing criterion. |
| V-03 | Output format axis -- Phase 3 prose blocks instead of table rows                             | Replacing the Phase 3 tier tables with labelled prose blocks (one block per participant) tests whether the table format is load-bearing for criteria satisfaction. Neither C-49 nor C-50 is satisfied in this variation: BEFORE YOU START retains the old "C-44 miss" citation and old pair list, and the FAILS SYNTAX TEMPLATE ends at C-45. The hypothesis: if criteria C-01 through C-48 can all pass with prose Phase 3, the table format is not structurally required; if they cannot, the table format is a load-bearing constraint. |
| V-04 | Combination: C-50 + C-49 partial -- correct citation, stale pair list                       | Pairing FAILS template extension with C-46/C-47/C-48 entries (C-50) with a C-47 pre-flight that names "C-46 miss" but retains the old pair list ("C-42, C-43, or any later pair") closes the template-currency gap and updates the governing criterion label but leaves the pair list stale. The halt fires; the citation is correct; but the pair list does not enumerate C-44 and C-45 explicitly. C-50 is satisfied. C-49 is partially satisfied: the criterion reference is correct but the pair list requires a reviewer to rely on "any later pair" inference rather than explicit enumeration. |
| V-05 | Full integration: C-49 precise + C-50 full -- all R18 criteria satisfied                    | All R18 additions applied: BEFORE YOU START C-47 pre-flight names "C-46 miss" AND lists "C-44, C-45" explicitly in the pair list (C-49 fully satisfied); FAILS SYNTAX TEMPLATE carries entries for C-46, C-47, and C-48 (C-50 fully satisfied). This is the only variation where: a reviewer encountering a stale pre-flight citation sees "C-46 miss" named as the governing criterion (not C-44); the pair list explicitly enumerates the criteria requiring entries so "any later pair" requires no inference; and a C-46, C-47, or C-48 violation has a canonical FAILS entry in the template. Remove either mechanism and a gap reopens. |

---

## V-01 -- BEFORE YOU START C-46 Citation Precision (C-49, single axis)

**Axis:** Update C-47 pre-flight to cite "C-46 miss" with extended pair list
**Hypothesis:** Updating the C-47 pre-flight to name "C-46 miss" (not "C-44 miss") and
extending the pair list to include C-44/C-45 explicitly satisfies C-49 as a standalone
change. C-50 is NOT satisfied: FAILS template ends at C-45 -- no C-46/C-47/C-48 entries.

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
If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added
  after C-39 (i.e., C-42, C-43, C-44, C-45, or any later pair): template not current; C-46 miss.
  Halt. [C-47]
If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain
  not declared as a unit; C-45 not satisfied. Halt. [C-48]
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
  CORRECT:   FAILS [C-42]: BEFORE YOU START contains descriptive sentence -- register not unified;
             every sentence must be a command or fail condition, not an explanation
  CORRECT:   FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no C-41 echo --
             three-point traceability incomplete; reviewer must traverse to source to find annotation
  CORRECT:   FAILS [C-44]: FAILS template omits CORRECT entry for C-42 or C-43 -- template not
             current after R15 added those criteria; C-40 pattern requires forward maintenance
  CORRECT:   FAILS [C-45]: CO-DEPENDENCY PREAMBLE omits C-43/C-41 three-leg row -- full
             traceability chain not declared as a unit; reviewer must reconstruct chain from
             three separate criterion definitions
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
=== org:committee SIMULATION -- SKELETON ===

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

[Result YES -> re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

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
| C-43 (fill-rule echo of C-41 annotation)         | REQUIRES: C-41 | C-43 echo is a dependent annotation -- meaningful only if PHASE-1-COMMIT carries the C-41 forward annotation. Three-leg chain: C-39 at consumption [C-39] -> C-41 at source [C-41] -> C-43 in fill rules [C-43]. All three legs must be verified as a unit; an echo without the source annotation creates the appearance of traceability without the substance. Verifying C-43 without first confirming C-41 is a false positive risk equivalent to scoring C-36 without verifying C-35. |

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
  FAILS [C-46-ICB]: Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS [C-49-ICB]: YES declared when no qualifying participant exists in completed TIER SORT

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
  FAILS [C-47-SI]: STANCE INVARIANT absent from ## STANCE MANIFEST

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

RECOMMIT MANIFEST after each invalidated phase re-executes.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND issued
```

---

## V-02 -- FAILS Template C-46/C-47/C-48 Extension (C-50, single axis)

**Axis:** Extend FAILS SYNTAX TEMPLATE with self-referential entries for C-46, C-47, and C-48
**Hypothesis:** Adding CORRECT entries for C-46, C-47, and C-48 to the FAILS SYNTAX TEMPLATE
satisfies C-50 (recursive currency extended to the R17 aspirational triplet). BEFORE YOU START
still carries the old C-44 citation and stale pair list -- C-49 is NOT satisfied.

The single axis: FAILS SYNTAX TEMPLATE gains three entries for C-46/C-47/C-48. BEFORE YOU
START, skeleton (STEP 1), and all STEP 2 fill rules are identical to V-01. Only the FAILS
SYNTAX TEMPLATE differs.

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
If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added
  after C-39 (i.e., C-42, C-43, or any later pair): template not current; C-44 miss. Halt. [C-47]
If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain
  not declared as a unit; C-45 not satisfied. Halt. [C-48]
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
  CORRECT:   FAILS [C-42]: BEFORE YOU START contains descriptive sentence -- register not unified;
             every sentence must be a command or fail condition, not an explanation
  CORRECT:   FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no C-41 echo --
             three-point traceability incomplete; reviewer must traverse to source to find annotation
  CORRECT:   FAILS [C-44]: FAILS template omits CORRECT entry for C-42 or C-43 -- template not
             current after R15 added those criteria; C-40 pattern requires forward maintenance
  CORRECT:   FAILS [C-45]: CO-DEPENDENCY PREAMBLE omits C-43/C-41 three-leg row -- full
             traceability chain not declared as a unit; reviewer must reconstruct chain from
             three separate criterion definitions
  CORRECT:   FAILS [C-46]: FAILS template omits CORRECT entry for C-44 or C-45 -- template not
             current after R17 added those criteria; C-40 pattern applied recursively to the
             C-44/C-45 pair requires forward maintenance of the template
  CORRECT:   FAILS [C-47]: BEFORE YOU START omits pre-flight halt for FAILS template currency --
             template staleness not detectable at session-open; C-44 miss visible only if reviewer
             inspects template directly
  CORRECT:   FAILS [C-48]: BEFORE YOU START omits pre-flight halt for CO-DEPENDENCY PREAMBLE
             completeness -- preamble three-leg omission not detectable at session-open; C-45 miss
             visible only if reviewer inspects preamble directly
  MALFORMED: FAILS: committee type absent              (missing [C-NN])
  MALFORMED: committee type absent -- C-01 miss         ([C-NN] at end, not positional)

This template applies to all FAILS entries below. Deviations are C-38 misses.

---

[Skeleton (STEP 1) and all STEP 2 fill rules identical to V-01.]
```

---

## V-03 -- Output Format Axis: Phase 3 Prose Blocks (neither C-49 nor C-50)

**Axis:** Phase 3 participant voices as labelled prose blocks instead of table rows
**Hypothesis:** Replacing the Phase 3 table-row format with prose blocks (one block per
participant, labelled with role name and tier) tests whether the table format is load-bearing
for criteria satisfaction. BEFORE YOU START retains the old "C-44 miss" citation and stale
pair list (C-49 NOT satisfied). FAILS SYNTAX TEMPLATE ends at C-45 (C-50 NOT satisfied).
The test: can C-01 through C-48 all pass with prose Phase 3? If yes, table format is not
structurally required; if no, the table row structure for STANCE/CITE/CONDITION is load-bearing.

The single axis: Phase 3 skeleton uses prose blocks; TIER-N-SEQUENCE-COMMITs remain. BEFORE
YOU START and FAILS SYNTAX TEMPLATE are identical to V-02. Fill rules for Phases 0-2 and 4-5
are identical to V-01. Phase 3 fill rules reflect the prose block format.

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
If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added
  after C-39 (i.e., C-42, C-43, or any later pair): template not current; C-44 miss. Halt. [C-47]
If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain
  not declared as a unit; C-45 not satisfied. Halt. [C-48]
Do not begin the skeleton until every line above is read.

---

## FAILS SYNTAX TEMPLATE

[Identical to V-01 FAILS SYNTAX TEMPLATE -- C-44/C-45 CORRECT entries present;
 C-46/C-47/C-48 CORRECT entries absent. C-50 not satisfied.]

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
  CORRECT:   FAILS [C-42]: BEFORE YOU START contains descriptive sentence -- register not unified;
             every sentence must be a command or fail condition, not an explanation
  CORRECT:   FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no C-41 echo --
             three-point traceability incomplete; reviewer must traverse to source to find annotation
  CORRECT:   FAILS [C-44]: FAILS template omits CORRECT entry for C-42 or C-43 -- template not
             current after R15 added those criteria; C-40 pattern requires forward maintenance
  CORRECT:   FAILS [C-45]: CO-DEPENDENCY PREAMBLE omits C-43/C-41 three-leg row -- full
             traceability chain not declared as a unit; reviewer must reconstruct chain from
             three separate criterion definitions
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
=== org:committee SIMULATION -- SKELETON (V-03: Prose Phase 3) ===

[PHASE 0 through PHASE 2 skeleton identical to V-01.]

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

**[Role Name] -- Tier 1**
STANCE: ___ [BLOCK / CONDITION / APPROVE]
Primary concern: ___
INERTIA-FINDING cite: INERTIA-FINDING-___

[One block per Tier 1 participant]

TIER-1-SEQUENCE-COMMIT: [locked] -- All Tier 1 voices complete.
  Stances committed: [list Tier 1 roles and STANCE tokens].
  No Tier 2 voice may appear before this line.
  [C-37 Mechanism 1 for C-02: ordering enforcement. Mechanism 2 is ROLE VOICE SEAL above.]
  | ENFORCE: terminal position in Tier 1 block.

### --- TIER 2: CONDITIONALS ---

**[Role Name] -- Tier 2**
STANCE: ___ [BLOCK / CONDITION / APPROVE]
Condition: ___ [specific deliverable -- "address concerns" fails]
INERTIA-FINDING cite: ___ [or: -- if no direct citation applies]

[One block per Tier 2 participant]

TIER-2-SEQUENCE-COMMIT: [locked] -- All Tier 2 voices complete.
  Stances committed: [list Tier 2 roles and STANCE tokens].
  No Tier 3 voice may appear before this line.
  | ENFORCE: terminal position in Tier 2 block.

### --- TIER 3: ADVOCATES ---

**[Role Name] -- Tier 3**
STANCE: ___ [BLOCK / CONDITION / APPROVE]
RESPONDS-TO: "[named concern from Tier 1 or Tier 2]"
CITE: INERTIA-FINDING-___ -- [content anchor]
Primary endorsement: ___

[One block per Tier 3 participant]

## STANCE MANIFEST

| Role              | STANCE-TOKEN |
|-------------------|--------------|
| ___               | ___          |
[repeat per participant]

STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised
  without reopening Phase 3.

PHASE-3-EXIT:
  [ ] All Tier 1 blocks before TIER-1-SEQUENCE-COMMIT; all Tier 2 before TIER-2-SEQUENCE-COMMIT
  [ ] Each voice complies with ROLE VOICE GUARD forbidden-topic scope
  [ ] Tier 1 INERTIA-FINDING cited; Tier 2 specific conditions; Tier 3 RESPONDS-TO + CITE present
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

[PHASE 4 and PHASE 5 skeleton identical to V-01.]

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

NOTE: All FAILS entries conform to `FAILS [C-NN]: <description>`. Deviations are C-38 misses.

[CO-DEPENDENCY PREAMBLE and PHASE 0, 1, 2 fill rules identical to V-01.]

---

**INERTIA CONTINUITY BRIDGE fill rule:**

[Identical to V-01.]

---

**ROLE VOICE GUARD fill rule [C-37 Mechanism 2 for C-02]:**

[Identical to V-01.]

---

**PHASE 3 fill rules (prose block format):**

SEQUENTIAL TIER GATE [C-37 Mechanism 1 for C-02]:
  FAILS [C-02]: Tier N+1 voice block appears before TIER-N-SEQUENCE-COMMIT
  FAILS [C-25]: tier ordering correct but TIER-N-SEQUENCE-COMMIT absent

VALIDATE STANCE: label on its own line; token is one of [BLOCK / CONDITION / APPROVE] only.
  FAILS [C-02]: STANCE label absent from block -- stance embedded in prose only
  FAILS [C-02]: qualified token like `CONDITION (pending)` used

Tier 1: INERTIA-FINDING cite line required in block.
Tier 2: Condition line required; "address concerns" fails.
  FAILS [C-07]: vague condition in Tier 2 block Condition line
Tier 3: RESPONDS-TO names specific concern; CITE line carries label.
  FAILS [C-02]: RESPONDS-TO absent from Tier 3 block

VALIDATE: at least one CONDITION or BLOCK; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST table. WRITE: STANCE INVARIANT.
  FAILS [C-47-SI]: STANCE INVARIANT absent from ## STANCE MANIFEST

PRINT: PHASE-3-COMMIT with bidirectionality clause.
  FAILS [C-45]: bidirectionality clause states only one direction

---

[PHASE 4, PHASE 5, and AMEND fill rules identical to V-01.]
```

---

## V-04 -- Combination: C-50 + C-49 Partial (correct citation, stale pair list)

**Axis:** FAILS template C-46/C-47/C-48 entries (C-50) + C-47 pre-flight cites "C-46 miss"
but retains old pair list without explicit C-44/C-45 enumeration
**Hypothesis:** Pairing FAILS template extension (C-50) with a C-47 pre-flight that names
"C-46 miss" as the governing criterion satisfies C-50 and functionally advances C-49 -- but
the pair list still reads "C-42, C-43, or any later pair" rather than explicitly naming C-44
and C-45. A reviewer encountering a stale template halt will see the correct criterion ("C-46
miss") but must infer C-44/C-45 from "any later pair" rather than reading them explicitly.
C-50 is satisfied. C-49 is partially satisfied: citation correct, pair list imprecise.

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
If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added
  after C-39 (i.e., C-42, C-43, or any later pair): template not current; C-46 miss. Halt. [C-47]
If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain
  not declared as a unit; C-45 not satisfied. Halt. [C-48]
Do not begin the skeleton until every line above is read.

---

## FAILS SYNTAX TEMPLATE

[C-50 satisfied: C-46/C-47/C-48 entries present. C-49 partially satisfied: pair list stale.]

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
  CORRECT:   FAILS [C-42]: BEFORE YOU START contains descriptive sentence -- register not unified;
             every sentence must be a command or fail condition, not an explanation
  CORRECT:   FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no C-41 echo --
             three-point traceability incomplete; reviewer must traverse to source to find annotation
  CORRECT:   FAILS [C-44]: FAILS template omits CORRECT entry for C-42 or C-43 -- template not
             current after R15 added those criteria; C-40 pattern requires forward maintenance
  CORRECT:   FAILS [C-45]: CO-DEPENDENCY PREAMBLE omits C-43/C-41 three-leg row -- full
             traceability chain not declared as a unit; reviewer must reconstruct chain from
             three separate criterion definitions
  CORRECT:   FAILS [C-46]: FAILS template omits CORRECT entry for C-44 or C-45 -- template not
             current after R17 added those criteria; C-40 pattern applied recursively to the
             C-44/C-45 pair requires forward maintenance of the template
  CORRECT:   FAILS [C-47]: BEFORE YOU START omits pre-flight halt for FAILS template currency --
             template staleness not detectable at session-open; C-44 miss visible only if reviewer
             inspects template directly
  CORRECT:   FAILS [C-48]: BEFORE YOU START omits pre-flight halt for CO-DEPENDENCY PREAMBLE
             completeness -- preamble three-leg omission not detectable at session-open; C-45 miss
             visible only if reviewer inspects preamble directly
  MALFORMED: FAILS: committee type absent              (missing [C-NN])
  MALFORMED: committee type absent -- C-01 miss         ([C-NN] at end, not positional)

This template applies to all FAILS entries below. Deviations are C-38 misses.

---

[Skeleton (STEP 1) and all STEP 2 fill rules identical to V-01.]
```

---

## V-05 -- Full Integration: C-49 Precise + C-50 Full (all R18 criteria satisfied)

**Axis:** All R18 additions on the R17 V-05 baseline
**Hypothesis:** Full integration: BEFORE YOU START C-47 pre-flight names "C-46 miss" as the
governing criterion AND explicitly lists "C-44, C-45" in the pair list (C-49 fully satisfied);
FAILS SYNTAX TEMPLATE carries entries for C-46, C-47, and C-48 (C-50 fully satisfied). This
is the only variation where:
- A reviewer encountering a stale-template halt sees "C-46 miss" as the governing criterion
  (not "C-44 miss") -- names the currently authoritative rubric reference
- The pair list explicitly enumerates C-44 and C-45 so no inference from "any later pair" is
  required -- pair list is self-updating with each new criterion pair
- A C-46, C-47, or C-48 violation has a canonical FAILS entry in the template for citation
Remove C-49: reviewer is directed to C-44 (an earlier criterion) when C-46 now governs. Remove
C-50: a C-47/C-48 violation has no template entry to cite. Both mechanisms are load-bearing.

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
If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added
  after C-39 (i.e., C-42, C-43, C-44, C-45, or any later pair): template not current; C-46 miss.
  Halt. [C-47]
If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain
  not declared as a unit; C-45 not satisfied. Halt. [C-48]
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
  CORRECT:   FAILS [C-42]: BEFORE YOU START contains descriptive sentence -- register not unified;
             every sentence must be a command or fail condition, not an explanation
  CORRECT:   FAILS [C-43]: TOKEN TRACE CONFIRMATION fill rules contain no C-41 echo --
             three-point traceability incomplete; reviewer must traverse to source to find annotation
  CORRECT:   FAILS [C-44]: FAILS template omits CORRECT entry for C-42 or C-43 -- template not
             current after R15 added those criteria; C-40 pattern requires forward maintenance
  CORRECT:   FAILS [C-45]: CO-DEPENDENCY PREAMBLE omits C-43/C-41 three-leg row -- full
             traceability chain not declared as a unit; reviewer must reconstruct chain from
             three separate criterion definitions
  CORRECT:   FAILS [C-46]: FAILS template omits CORRECT entry for C-44 or C-45 -- template not
             current after R17 added those criteria; C-40 pattern applied recursively to the
             C-44/C-45 pair requires forward maintenance of the template
  CORRECT:   FAILS [C-47]: BEFORE YOU START omits pre-flight halt for FAILS template currency --
             template staleness not detectable at session-open; C-46 miss visible only if reviewer
             inspects template directly
  CORRECT:   FAILS [C-48]: BEFORE YOU START omits pre-flight halt for CO-DEPENDENCY PREAMBLE
             completeness -- preamble three-leg omission not detectable at session-open; C-45 miss
             visible only if reviewer inspects preamble directly
  MALFORMED: FAILS: committee type absent              (missing [C-NN])
  MALFORMED: committee type absent -- C-01 miss         ([C-NN] at end, not positional)

This template applies to all FAILS entries below. Deviations are C-38 misses.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant. INERTIA CONTINUITY BRIDGE injects one if
no charter inertia owner exists.

---

[Skeleton (STEP 1) identical to V-01.]

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
| C-43 (fill-rule echo of C-41 annotation)         | REQUIRES: C-41 | C-43 echo is a dependent annotation -- meaningful only if PHASE-1-COMMIT carries the C-41 forward annotation. Three-leg chain: C-39 at consumption [C-39] -> C-41 at source [C-41] -> C-43 in fill rules [C-43]. All three legs must be verified as a unit; an echo without the source annotation creates the appearance of traceability without the substance. Verifying C-43 without first confirming C-41 is a false positive risk equivalent to scoring C-36 without verifying C-35. |

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
  FAILS [C-46-ICB]: Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS [C-49-ICB]: YES declared when no qualifying participant exists in completed TIER SORT

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
  FAILS [C-47-SI]: STANCE INVARIANT absent from ## STANCE MANIFEST

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

RECOMMIT MANIFEST after each invalidated phase re-executes.
  FAILS [C-34]: phase resumes without RECOMMIT MANIFEST
  FAILS [C-34]: downstream phase gates on v1 seal after AMEND issued
```
