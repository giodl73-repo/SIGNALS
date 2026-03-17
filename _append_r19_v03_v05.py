"""Append V-03, V-04, V-05 to org-committee-variate-R19-2026-03-16.md"""

TARGET = r"C:\src\sim\simulations\quest\golden\org-committee-variate-R19-2026-03-16.md"

V03 = r"""

---

## V-03 — Single-Axis: Phrasing Register — Conversational Mixed Register with C-44/C-45/C-46

**Variation axis**: Phrasing register — conversational framing with structured skeleton. The two-step skeleton architecture is preserved. ENFORCE and PRINT commands retain their imperative register. The guidance around C-44, C-45, and C-46 is written in an explanatory register: why three failure modes are needed, what a half-coupling means in practice, and why the Inertia-Advocate injection is a design choice rather than a fallback. Tests whether three-failure-mode enumeration, content-completeness VALIDATE, and SYNTHESIZE injection survive a mixed-register prompt without drifting into optionality.

**Hypothesis**: Conversational framing of C-44 and C-45 risks making the failure modes sound advisory. V-03 tests the threshold: the skeleton pre-declares all structural elements including the SYNTHESIZE CHECK section and INVARIANT placeholder lines; the fill rules use conversational scaffolding but still enumerate three named FAILS axes and the content-completeness VALIDATE. If the VALIDATE blocks retain their imperative ACCEPTABLE/FAILS structure, C-44 and C-45 survive the register shift. C-46 expressed as "the Inertia-Advocate must always have a Phase 3 voice" rather than "INJECT: if absent." Expected: 162-166/166.

---

You are running `org:committee` -- a pre-meeting simulation. The goal is to surface surprises before the real committee meets: what the proposal displaces, who will resist, and why. Work in two steps: first print the full structure you are about to produce; then fill it.

---

### STEP 1 -- PRINT THIS SKELETON

Before writing any simulation content, print the following structure with all headers, field labels, and blank slots visible. This lets you commit to the structure before populating it.

```
=== org:committee SIMULATION ===

## PHASE 0 -- COMMITTEE DECLARATION
Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___   [one line per participant: Role Name -- orientation]
PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION
### INVESTIGATION-ATTEMPT-1
INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___
GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___
[NO -> INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES]

## INERTIA RECORD
  INERTIA-FINDING-A: ___  [anchor]
  INERTIA-FINDING-B: ___  [anchor]
  INERTIA-FINDING-C: ___  [anchor]
  INERTIA-FINDING-D: ___  [anchor]
INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A-D locked.
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
[YES -> reassign; reprint corrected TIER SORT and SORT-CHECK; loop until NO]

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## SYNTHESIZE CHECK
Tier-sort inertia owner: ___ [YES -- natural owner found / NO -- Inertia-Advocate INJECTED]
  [NO -> Inertia-Advocate INJECTED -- Tier: 1 -- Orientation: switching-cost investigation from ## INERTIA RECORD]

---

## PHASE 3 -- PARTICIPANT VOICES
[Tier 1 -> Tier 2 -> Tier 3; Inertia-Advocate first in Tier 1 if INJECTED]

### ___ -- Tier ___
STANCE: ___
___
CITE: ___ -- ___           [Tier 3 only]
RESPONDS-TO: "___" -- ___  [Tier 3 only]
[Repeat per participant]

## STANCE MANIFEST
  [___] ___
  [repeat per participant -- format: [Role Name] STANCE-TOKEN]
STANCE INVARIANT: sealed at PHASE-3-COMMIT -- ___

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above -- modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted.
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
[Role -- objection citing INERTIA-FINDING-* -- resolution path -- named authority -- trigger]
[or: No dissent -- [reason]]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0** -- Load the committee and lock its identity.

Start by declaring the committee type -- ROB, shiproom, arch-board, or whatever the user specified. The committee type goes first; nothing else is output before it.

Load participants from `.craft/roles/` using the committee type as the key. If no charter file exists, note that in the Charter Source line and fall back to Signal defaults: PM, Architect, Inertia-Advocate. List each participant with their charter-documented orientation in one phrase.

PRINT: PHASE-0-COMMIT: [locked] -- Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1** -- Investigate what the proposal displaces.

Before participants speak, the simulation identifies what is currently in place and what it costs to leave it behind. This investigation runs as a labeled loop; it does not finish until INERTIA-FINDING-D names a cost the proposal author almost certainly did not account for.

Label the first attempt INVESTIGATION-ATTEMPT-1. Write all four findings with their full token labels as the first element on each line. Then evaluate: does INERTIA-FINDING-D name a non-obvious cost? Write the GATE answer and a one-sentence basis. If NO, increment to INVESTIGATION-ATTEMPT-2 and rewrite all four findings from a fresh angle, carrying the new sequential label.

After the loop exits, write the ## INERTIA RECORD section -- one-phrase anchors, independently readable without the surrounding investigation prose.

The last line of ## INERTIA RECORD is the INERTIA INVARIANT seal. Think of it as a two-part contract: part one names the phase-commit boundary; part two states the modification prohibition. Both parts must be present. A seal that names the commit but omits the prohibition is like a lock with no combination -- it looks sealed but the terms are unstated.

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed, or modified without reopening Phase 1.`
VALIDATE: both the commit reference and the modification prohibition must be present.
  ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed, or modified without reopening Phase 1.` -- both parts present; contract complete
  FAILS (a): `INERTIA INVARIANT: sealed at PHASE-1-COMMIT` -- commit reference there but the prohibition is absent; the contract is half-stated; axis (a): commit-present/prohibition-absent
  FAILS (b): `INERTIA INVARIANT: findings locked` -- the line exists but carries neither element; axis (b): both-elements-absent-in-present-line
  FAILS (c): [## INERTIA RECORD with correct findings but no INERTIA INVARIANT line at all] -- the seal is simply missing; a reader cannot tell from the section alone that it is frozen; axis (c): line-absent-entirely

PRINT: PHASE-1-COMMIT: [locked] -- Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A-D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

The PHASE-1-COMMIT bidirectionality clause links this commit and ## INERTIA RECORD as mutual obligations -- if the record changes, the commit must change; if the commit changes, the record must change. A one-direction clause ("the record owes the commit") leaves the reverse obligation unstated, which is a half-coupling: it reads as a pointer, not a contract.
VALIDATE: both directions explicitly named.
  ACCEPTABLE: `modifications to that record require updating this commit; modifications to this commit require updating that record` -- both directions present
  FAILS: `modifications to that record require updating this commit` -- one direction only; reverse obligation absent; fails C-45

---

**PHASE 2** -- Sort participants by their relationship to risk.

Assign each charter participant to a tier: Tier 1 (CHALLENGERS) for roles whose orientation maps to feasibility scrutiny or disruption analysis; Tier 2 (CONDITIONALS) for roles holding conditional approval; Tier 3 (ADVOCATES) for roles aligned with the proposal. Challengers first; advocates last. Tie-break by institutional veto authority within a tier.

Run the SORT-CHECK gate with both Test: and Result: fields visible. If Result is YES, reassign, reprint, and loop until NO.

PRINT: PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**SYNTHESIZE CHECK** -- confirm Phase 1 findings have a voice in Phase 3.

After the tier sort, look at who is going to speak. The Phase 1 investigation produced named findings about switching costs and disruption -- someone in Phase 3 must own those findings and argue from them. That is the inertia perspective.

If a charter participant's Tier 1 or Tier 2 orientation already maps to switching-cost investigation, record YES and proceed. If no one maps to that perspective, the simulation must supply it: record NO and inject an Inertia-Advocate into Phase 3 as a Tier 1 participant. The injected Inertia-Advocate speaks first among challengers, cites at least one INERTIA-FINDING-* label, and appears in ## STANCE MANIFEST. This is not a workaround -- it is the design: Phase 1 findings always have an owner-voice in Phase 3, regardless of charter composition.

VALIDATE:
  ACCEPTABLE: `Tier-sort inertia owner: YES` when a Tier 1/Tier 2 participant's charter orientation explicitly covers switching-cost analysis
  ACCEPTABLE: `Tier-sort inertia owner: NO` with Inertia-Advocate INJECTED -- design guarantee fires
  FAILS: Phase 3 begins without any SYNTHESIZE CHECK having run -- fails C-46
  FAILS: YES asserted when no participant maps to inertia analysis -- the check is wrong

---

**PHASE 3** -- Participant voices in tier order.

Every voice opens with a standalone STANCE: line declaring BLOCK, CONDITION, or APPROVE before any prose. Prose elaborates but may not soften the declared token.

Order: Tier 1 before Tier 2 before Tier 3. Injected Inertia-Advocate speaks first in Tier 1.

Tier 1 participants ground their concern in a named INERTIA-FINDING-* label. Tier 2 participants name their specific approval condition -- not "address concerns." Tier 3 participants write CITE: (opening with the named label) and RESPONDS-TO: (quoting a specific named concern) before any endorsement.

After all voices, write ## STANCE MANIFEST -- one entry per participant as [Role Name] STANCE-TOKEN.

The last line of ## STANCE MANIFEST is the STANCE INVARIANT seal -- same two-part contract as the INERTIA INVARIANT: commit reference and modification prohibition must both be present.

PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised without reopening Phase 3.`
VALIDATE:
  ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised without reopening Phase 3.` -- both parts present
  FAILS (a): `STANCE INVARIANT: sealed at PHASE-3-COMMIT` -- commit reference there but prohibition absent; axis (a): commit-present/prohibition-absent
  FAILS (b): `STANCE INVARIANT: stances locked` -- neither element present; axis (b): both-elements-absent-in-present-line
  FAILS (c): [## STANCE MANIFEST correct but no STANCE INVARIANT line] -- seal absent entirely; axis (c): line-absent-entirely

PRINT: PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above -- modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

The PHASE-3-COMMIT bidirectionality clause links this commit and ## STANCE MANIFEST as mutual obligations in both directions.
VALIDATE: both directions named.
  ACCEPTABLE: `modifications to that manifest require updating this commit; modifications to this commit require updating that manifest` -- both directions present
  FAILS: one direction only -- half-coupling; fails C-45

---

**PHASE 4** -- Count from the manifest.

PRINT: `TALLY: [N] APPROVE * [N] CONDITION * [N] BLOCK` -- count tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
Derive OUTCOME. Validate counts match manifest exactly.

PRINT: PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5** -- Write the minutes.

DECISIONS: Verdict matching OUTCOME exactly. Specific conditions for full approval -- not "address feedback." If not APPROVED: Owner (named role, not a team) and Trigger (named artifact with named recipient and named authority).

ACTION ITEMS: one line per item -- Owner Role, specific action, deadline. Each item names the question being answered, the output artifact, and who receives it.

DISSENTING OPINIONS: for each CONDITION or BLOCK -- specific objection citing INERTIA-FINDING-* where applicable, plus resolution path with named authority. If no dissent: `No dissent -- [reason]`.

PRINT: PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
"""

V04 = r"""

---

## V-04 -- Combined: Lifecycle Emphasis + Inertia Framing

**Variation axis**: Lifecycle emphasis + Inertia framing -- full skeleton with Inertia-Advocate elevated as a structural invariant. The SYNTHESIZE CHECK is renamed to "INERTIA CONTINUITY BRIDGE" in the skeleton, making C-46's purpose visible at the structural level. C-44 three-failure-mode VALIDATE expressed as the "sealing contract integrity test" -- the INVARIANT is framed as a contract that must carry both elements to be enforceable, with independent failure axes named. C-45 bidirectionality VALIDATE framed as "coupling integrity" -- the commit and manifest are co-owners of each other, and the clause must name both obligations to constitute a contract. Role sequence explicitly enforces Inertia-Advocate first within Tier 1 when injected.

**Hypothesis**: The combined axis tests whether lifecycle precision (explicit gate loops, skeleton pre-declaration, terminal ENFORCE blocks) and inertia-identity framing reinforce or undercut each other. If the Inertia-Advocate's structural elevation as Phase 1's owner-voice in Phase 3 is expressed as a named design principle rather than a conditional injection, C-46 is more likely to be correctly applied. The three-failure-mode VALIDATE for sealing contract integrity maps naturally to the inertia framing: the INERTIA INVARIANT is the Inertia-Advocate's evidence boundary, and its verification must cover all three ways it can fail. Expected: 166/166.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation. Phase 1 produces the evidence; the Inertia-Advocate owns it in Phase 3. If the charter supplies a natural inertia owner, use them. If not, the INERTIA CONTINUITY BRIDGE injects an Inertia-Advocate before Phase 3 begins. This is a design guarantee, not a fallback.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO -> INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]

### INVESTIGATION-ATTEMPT-2   [fill only if GATE-1 is NO; omit if GATE-1 is YES]

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-2:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[Continue as INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A-D locked.
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

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- charter role covers inertia perspective / NO -- Inertia-Advocate INJECTED]
  [NO -> Inertia-Advocate INJECTED -- Tier: 1 (speaks first) -- Orientation: switching-cost investigation from ## INERTIA RECORD -- CITE obligation: at least one INERTIA-FINDING-* label in Phase 3 voice]

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

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above -- modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted.
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
[Role -- objection citing INERTIA-FINDING-* label -- resolution path -- named authority -- concrete trigger]
[or: No dissent -- [reason]]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter -- Charter Source: `Signal defaults -- no charter found`; fallback participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type -- ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type -- ROB`
  FAILS: `Committee Type -- unspecified` -- type not named; fails C-01
  FAILS: `Committee Type -- product review` -- non-standard label; use recognized types
PRINT: Agenda Item, Charter Source, Participants (one line each, format: [Role Name] -- [orientation]).
PRINT: PHASE-0-COMMIT: [locked] -- Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C -- team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label as the first element on the line.
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow -- ...`
  FAILS: `(a) legacy-approval-workflow` -- parenthesized letter, not the token; fails C-27
  FAILS: `Finding A: ...` -- abbreviated label; full token required

GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; GATE-N+1; repeat.
ENFORCE: each retry carries its sequential INVESTIGATION-ATTEMPT-N label.
ENFORCE: loop runs within Phase 1; Phase 2 reached unconditionally after any YES.

WRITE: ## INERTIA RECORD -- one-phrase anchors from the passing attempt's findings.
VALIDATE: each entry carries a content anchor -- not a bare label, not a placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` -- bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` -- unfilled placeholder

SEALING CONTRACT INTEGRITY -- INERTIA INVARIANT:
The INERTIA INVARIANT is the Inertia-Advocate's evidence boundary. It declares two things: (1) the phase-commit at which the record is sealed, (2) that modifications are prohibited without reopening. Both elements must be present for the contract to be enforceable.

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed, or modified without reopening Phase 1.`
VALIDATE: commit reference and modification prohibition both present -- three independent failure axes.
  ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed, or modified without reopening Phase 1.` -- both contract elements present; passes C-40 and C-44
  FAILS (a): `INERTIA INVARIANT: sealed at PHASE-1-COMMIT` -- commit reference present, prohibition absent; contract half-stated; axis (a): commit-present/prohibition-absent
  FAILS (b): `INERTIA INVARIANT: findings frozen` -- line exists but carries neither element; both absent in a present line; axis (b): both-elements-absent-in-present-line
  FAILS (c): [## INERTIA RECORD with correct findings but no INERTIA INVARIANT line] -- the contract is simply not there; axis (c): line-absent-entirely

ENFORCE: ## INERTIA RECORD is independently addressable; appears before PHASE-1-COMMIT.
PRINT: PHASE-1-COMMIT: [locked] -- Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A-D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

COUPLING INTEGRITY -- PHASE-1-COMMIT bidirectionality clause:
The commit and the record are co-owners. The clause must name both obligations: what the record owes the commit and what the commit owes the record. One direction is a pointer; both directions are a contract.
VALIDATE: both coupling directions named.
  ACCEPTABLE: `modifications to that record require updating this commit; modifications to this commit require updating that record` -- bilateral contract declared; passes C-41 and C-45
  FAILS: `modifications to that record require updating this commit` -- one direction only; half-coupling; reverse obligation absent; fails C-45

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) -- charter roles whose orientation maps to feasibility scrutiny, risk, or disruption of existing systems; speak first.
ASSIGN: Tier 2 (CONDITIONALS) -- roles holding conditional approval; speak second.
ASSIGN: Tier 3 (ADVOCATES) -- roles aligned with proposal goals; speak last.
ENFORCE: tie-break by institutional veto authority within a tier.

SORT-CHECK:
PRINT: `Test: Tier 1 and Tier 2 both empty?` and `Result: YES / NO`.
IF YES: name mis-sorted role, target tier, reason specific to this agenda item; reprint corrected TIER SORT; reprint SORT-CHECK; loop until NO.
ENFORCE: SORT-CHECK as discrete labeled gate; correct ordering without the gate fails C-25.

PRINT: PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

INSPECT: Phase 2 TIER SORT -- identify any Tier 1 or Tier 2 participant whose charter orientation maps to switching-cost investigation, status-quo defense, or cost-of-change analysis.
CONFIRM: `Inertia owner in tier sort: YES` if such a participant exists; proceed to Phase 3.
CONFIRM: `Inertia owner in tier sort: NO` if none exists:
  INJECT: Inertia-Advocate as Phase 3 Tier 1 participant -- speaks first among all challengers.
  ORIENTATION: investigates switching costs from ## INERTIA RECORD; voices Phase 1 findings as Phase 3 objections.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in their voice block.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.
VALIDATE:
  ACCEPTABLE: `Inertia owner in tier sort: YES` when a charter Tier 1/Tier 2 participant explicitly covers inertia analysis
  ACCEPTABLE: `Inertia owner in tier sort: NO` with Inertia-Advocate INJECTED -- design guarantee fires; Phase 1 -> Phase 3 continuity ensured
  FAILS: Phase 3 begins without INERTIA CONTINUITY BRIDGE section -- Phase 1 findings may have no owner-voice; fails C-46
  FAILS: YES asserted when no Tier 1/Tier 2 participant maps to inertia analysis -- check answered incorrectly

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 -> Tier 2 -> Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED -- Inertia-Advocate voice FIRST in Tier 1.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before any prose.
VALIDATE: STANCE: is a structural committed declaration -- prose may not contradict it.
  ACCEPTABLE: `STANCE: BLOCK` alone on its own line
  FAILS: stance embedded in prose, no STANCE: label
  FAILS: `STANCE: BLOCK (pending)` -- qualified token

WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label -- content] before endorsement; RESPONDS-TO: "[named concern]" -- [one sentence] before endorsement.
  VALIDATE CITE: label is first element after CITE:.
  VALIDATE RESPONDS-TO: names and quotes a specific concern.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST after all voices; one entry per participant: [Role Name] STANCE-TOKEN.

SEALING CONTRACT INTEGRITY -- STANCE INVARIANT:
PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised without reopening Phase 3.`
VALIDATE: commit reference and modification prohibition both present.
  ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised without reopening Phase 3.`
  FAILS (a): `STANCE INVARIANT: sealed at PHASE-3-COMMIT` -- prohibition absent; axis (a)
  FAILS (b): `STANCE INVARIANT: stances immutable` -- neither element; axis (b)
  FAILS (c): [no STANCE INVARIANT line in ## STANCE MANIFEST] -- line absent; axis (c)

PRINT: PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above -- modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

COUPLING INTEGRITY -- PHASE-3-COMMIT bidirectionality clause:
VALIDATE: both coupling directions named.
  ACCEPTABLE: `modifications to that manifest require updating this commit; modifications to this commit require updating that manifest` -- bilateral; passes C-41 and C-45
  FAILS: one direction only -- half-coupling; fails C-45

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE * [N] CONDITION * [N] BLOCK` -- COUNT tokens in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY; all APPROVE -> APPROVED; any CONDITION no BLOCK -> APPROVED WITH CONDITIONS; any BLOCK -> BLOCKED or DEFERRED.
VALIDATE: counts match ## STANCE MANIFEST exactly.
PRINT: PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval -- specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster, not a team) and Trigger (named artifact + recipient + authority).
VALIDATE: both Owner and Trigger present when verdict not APPROVED; missing either fails C-23.
PRINT: action items as [Owner Role] -- [specific action] -- [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance -- specific objection citing INERTIA-FINDING-* label, resolution path, named authority.
ENFORCE: if no dissent -- `No dissent -- [reason]`.
PRINT: PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
"""

V05 = r"""

---

## V-05 -- Full Synthesis: All Axes -- Skeleton + Imperative Fill + Three-Mode VALIDATE + Content-Complete Bidirectionality VALIDATE + SYNTHESIZE Guarantee + Inertia-First Identity (Targets 166/166)

**Variation axis**: All axes combined -- skeleton pre-declaration (C-28) + imperative fill rules (C-30) + three-failure-mode VALIDATE on both INVARIANT seals (C-44) + content-completeness VALIDATE on both bidirectionality clauses (C-45) + INERTIA CONTINUITY BRIDGE as structural Phase 3 guarantee with precise injection rules (C-46) + inertia-first identity throughout + role-sequence enforcement with Inertia-Advocate always first in Tier 1 when injected + output format enforced by skeleton + lifecycle emphasis with all gate loops and terminal ENFORCE blocks.

**Hypothesis**: All prior gaps addressed; no axis left untested. C-44 three-failure-mode VALIDATE on INERTIA INVARIANT and STANCE INVARIANT covers all three independent axes (a/b/c). C-45 content-completeness VALIDATE on both PHASE-1-COMMIT and PHASE-3-COMMIT bidirectionality clauses covers the half-coupling failure mode. C-46 INERTIA CONTINUITY BRIDGE section in skeleton with precise YES/NO fill rule and Tier 1 injection covers the Phase 1 -> Phase 3 continuity guarantee. Inertia-Advocate elevated as structural identity: first in Phase 1 investigation (evidence producer), first in Tier 1 Phase 3 voices (evidence owner) when injected. Expected: 166/166.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural identity in every org:committee simulation. Phase 1 produces the evidence base. The INERTIA CONTINUITY BRIDGE guarantees that evidence base has a designated owner-voice in Phase 3 regardless of charter composition. When the charter supplies a natural inertia owner, that role fills the identity. When it does not, the simulation injects an Inertia-Advocate into Tier 1 before any Phase 3 voices begin.

---

### STEP 1 -- PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block. Do not fill any values in this step.

```
=== org:committee SIMULATION -- SKELETON ===

## PHASE 0 -- COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ -- ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] -- Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 -- INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO -> fill INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]

### INVESTIGATION-ATTEMPT-2   [fill only if GATE-1 is NO; omit if GATE-1 is YES]

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-2:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[Continue as INVESTIGATION-ATTEMPT-N / GATE-N until YES. Sequential label increments each time.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- ___

PHASE-1-COMMIT: [locked] -- Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A-D locked.
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

PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES -- charter role maps to inertia perspective / NO -- Inertia-Advocate INJECTED]
  [NO -> Inertia-Advocate INJECTED -- Tier: 1 (first voice) -- Orientation: switching-cost investigation from ## INERTIA RECORD -- CITE: at least one INERTIA-FINDING-* label required]

---

## PHASE 3 -- PARTICIPANT VOICES

[Tier 1 -> Tier 2 -> Tier 3]
[INJECTED Inertia-Advocate: FIRST in Tier 1 before any other Tier 1 voice]

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

PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above -- modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted.
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
[one entry per dissent: Role -- objection citing INERTIA-FINDING-* label -- resolution path -- named authority -- concrete trigger]
[or: No dissent -- [reason]]

PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 -- FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists -- WRITE Charter Source: `Signal defaults -- no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type -- one of ROB, shiproom, arch-board, or the user-specified type from the request.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type -- ROB` -- recognized type declared before any other content
  ACCEPTABLE: `Committee Type -- arch-board` -- recognized type in opening position
  FAILS: `Committee Type -- unspecified` -- type not named; fails C-01
  FAILS: `Committee Type -- product review` -- non-standard label; use ROB, shiproom, arch-board, or user-specified type
PRINT: Agenda Item, Charter Source, Participants (one line per role: [Role Name] -- [orientation]).
ENFORCE: PHASE-0-COMMIT: is terminal element of Phase 0.
PRINT: PHASE-0-COMMIT: [locked] -- Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position -- NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A -- specific workflow or tool in production displaced by this agenda item; name precisely.
  VALIDATE: full token label is first element on the line.
    ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-pipeline -- ...`
    FAILS: `(a) legacy-approval-pipeline` -- parenthesized letter; fails C-27
    FAILS: `Finding A: ...` -- abbreviated label; full INERTIA-FINDING-A token required

WRITE: INERTIA-FINDING-B -- specific integration surface at risk; name systems, APIs, contracts, or downstream consumers.
  VALIDATE: full token label is first element.
    ACCEPTABLE: `INERTIA-FINDING-B: webhook-contract -- the Notification Service depends on...`
    FAILS: `(b) webhook-contract` -- parenthesized letter

WRITE: INERTIA-FINDING-C -- team whose cognitive decision habit would break and the specific habit; name both.
  ENFORCE: generic attribution fails.

WRITE: INERTIA-FINDING-D -- non-obvious switching cost the proposal author did not account for.
  REQUIRE: specific enough the author would say "I missed that."

GATE-N intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
WRITE: Answer YES or NO; one-sentence basis.
IF NO: INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels from a different angle; GATE: GATE-N+1; re-evaluate; REPEAT.
ENFORCE: each retry carries its INVESTIGATION-ATTEMPT-N+1 label; rewrite without the label fails C-22 and C-24.
ENFORCE: loop runs within Phase 1; Phase 2 reached unconditionally after any YES.

WRITE: ## INERTIA RECORD -- one-phrase anchors from the passing attempt's findings.
  PRINT: INERTIA-FINDING-[A/B/C/D]: [anchor] for each finding.
  VALIDATE: each entry carries a content anchor -- not a bare label, not a placeholder.
    ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption`
    ACCEPTABLE: `INERTIA-FINDING-D: undocumented-rollback-dependency`
    FAILS: `INERTIA-FINDING-A:` -- bare label; fails C-34
    FAILS: `INERTIA-FINDING-B: [one-phrase anchor]` -- unfilled placeholder; fails C-34

PRINT: INERTIA INVARIANT -- terminal line of ## INERTIA RECORD.
  PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed, or modified without reopening Phase 1.`
  VALIDATE: seal carries both the commit reference and the modification prohibition -- three independent failure axes.
    ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT -- findings may not be added, removed, or modified without reopening Phase 1.` -- both contract elements present; passes C-40 and C-44
    FAILS (a): `INERTIA INVARIANT: sealed at PHASE-1-COMMIT` -- commit reference present, prohibition absent; the Inertia-Advocate's evidence boundary is half-stated; axis (a): commit-present/prohibition-absent
    FAILS (b): `INERTIA INVARIANT: findings frozen` -- line present but neither commit reference nor prohibition clause carried; both elements absent in a non-empty line; axis (b): both-elements-absent-in-present-line
    FAILS (c): [## INERTIA RECORD with correct findings but no INERTIA INVARIANT line] -- seal absent entirely; Phase 1 findings have no stated boundary; axis (c): line-absent-entirely

ENFORCE: ## INERTIA RECORD is independently addressable by section heading; appears before PHASE-1-COMMIT.
ENFORCE: PHASE-1-COMMIT: is terminal element of Phase 1.
PRINT: PHASE-1-COMMIT: [locked] -- Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above -- modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A-D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position -- NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

VALIDATE: PHASE-1-COMMIT bidirectionality clause names both coupling directions.
  ACCEPTABLE: `modifications to that record require updating this commit; modifications to this commit require updating that record` -- both directions stated; bilateral coupling contract declared; passes C-41 and C-45
  FAILS: `modifications to that record require updating this commit` -- one direction named; reverse obligation absent; half-coupling; fails C-45

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) -- roles whose charter orientation interrogates feasibility, risk, or disruption of existing systems; these speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) -- roles holding approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) -- roles aligned with proposal goals; these speak last.
ENFORCE: tie-break within any tier -- higher institutional veto authority speaks first.

SORT-CHECK fill rule (intra-phase loop):
PRINT: `Test: Tier 1 and Tier 2 both empty?` and `Result: YES or NO`.
VALIDATE: if YES -- name mis-sorted role, target tier, reason specific to agenda item and INERTIA-FINDING findings; RE-PRINT corrected TIER SORT; RE-PRINT new SORT-CHECK; LOOP until NO.
  ACCEPTABLE: `Result: NO -- Tier 1 contains [Architect] and [Security Lead]; valid`
  FAILS: `Result: YES` with no reassignment -- fails C-18 and C-22
ENFORCE: SORT-CHECK as discrete labeled gate with both Test: and Result: fields; correct ordering without the gate fails C-25.
ENFORCE: PHASE-2-COMMIT: is terminal element of Phase 2.
PRINT: PHASE-2-COMMIT: [locked] -- TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position -- NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 -> Phase 3):**

INSPECT: Phase 2 TIER SORT -- scan all assigned participants for any whose charter-documented Tier 1 or Tier 2 orientation maps to switching-cost investigation, status-quo defense, or cost-of-change analysis.
CONFIRM: `Inertia owner in tier sort: YES` if such a participant exists; no injection required; proceed to Phase 3.
CONFIRM: `Inertia owner in tier sort: NO` if no such participant exists:
  INJECT: Inertia-Advocate as Phase 3 Tier 1 participant.
  POSITION: FIRST voice in Tier 1 -- before any other Tier 1 participant.
  ORIENTATION: investigates switching costs from ## INERTIA RECORD; voices Phase 1 findings as Phase 3 objections.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label from ## INERTIA RECORD in their Phase 3 voice block.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.
VALIDATE: INERTIA CONTINUITY BRIDGE is a structural guarantee.
  ACCEPTABLE: `Inertia owner in tier sort: YES` when a charter Tier 1 or Tier 2 participant's orientation explicitly covers switching-cost investigation
  ACCEPTABLE: `Inertia owner in tier sort: NO` with Inertia-Advocate INJECTED, Tier 1 first position -- Phase 1 -> Phase 3 continuity ensured
  FAILS: Phase 3 voices begin without INERTIA CONTINUITY BRIDGE section having been output -- Phase 1 findings may have no owner-voice; fails C-46
  FAILS: `Inertia owner in tier sort: YES` asserted when no charter participant maps to inertia analysis -- check incorrectly answered; Phase 1 findings silently unargued from inertia perspective

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
ENFORCE: if Inertia-Advocate INJECTED by INERTIA CONTINUITY BRIDGE -- Inertia-Advocate is FIRST voice within Tier 1 before any other Tier 1 participant speaks.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed structural declaration.
  ACCEPTABLE: `STANCE: BLOCK` on its own line -- unambiguous before rationale
  ACCEPTABLE: `STANCE: CONDITION` on its own line -- declares conditional hold before any endorsement
  FAILS: stance embedded in prose -- no STANCE: label; fails C-13
  FAILS: `STANCE: BLOCK (pending clarification)` -- qualified token; fails C-13

WRITE: 2-4 sentences per participant from charter-documented role orientation responding to this agenda item.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD; fails C-16 if absent.
REQUIRE (Tier 2): name specific approval condition precisely; "address concerns" fails C-19.
REQUIRE (Tier 3): CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] -- [content]`
ENFORCE: named label is first element after CITE:.
VALIDATE:
  ACCEPTABLE: `CITE: INERTIA-FINDING-A -- workflow-disruption: the migration plan directly addresses...`
  FAILS: `CITE: The workflow disruption finding...` -- paraphrase, no label; fails C-20
  FAILS: `CITE: (a) -- workflow-disruption` -- parenthesized letter

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" -- [one sentence]`
VALIDATE:
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-A: workflow-disruption" -- the migration plan stages the transition`
  ACCEPTABLE: `RESPONDS-TO: "[Architect]'s concern that integration contracts break" -- the adapter preserves them`
  FAILS: `RESPONDS-TO: "concerns acknowledged"` -- generic; no attribution; fails C-21

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2; re-assigns tiers.

WRITE: ## STANCE MANIFEST after all participant voices.
  PRINT one entry per participant: [Role Name] STANCE-TOKEN.
  ENFORCE: ## STANCE MANIFEST is independently addressable; appears before PHASE-3-COMMIT.

PRINT: STANCE INVARIANT -- terminal line of ## STANCE MANIFEST.
  PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised without reopening Phase 3.`
  VALIDATE: seal carries both commit reference and modification prohibition -- three independent failure axes.
    ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT -- stance entries may not be revised without reopening Phase 3.` -- both elements present; passes C-40 and C-44
    FAILS (a): `STANCE INVARIANT: sealed at PHASE-3-COMMIT` -- commit reference present, prohibition absent; axis (a): commit-present/prohibition-absent
    FAILS (b): `STANCE INVARIANT: stances frozen` -- neither element present in a non-empty line; axis (b): both-elements-absent-in-present-line
    FAILS (c): [## STANCE MANIFEST correct entries but no STANCE INVARIANT line] -- seal absent entirely; axis (c): line-absent-entirely

ENFORCE: PHASE-3-COMMIT: is terminal element of Phase 3.
PRINT: PHASE-3-COMMIT: [locked] -- Vote-anchor manifest declared in ## STANCE MANIFEST above -- modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 -> 2 -> 3 order. Phase 3 closed.
  | ENFORCE: terminal position -- NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

VALIDATE: PHASE-3-COMMIT bidirectionality clause names both coupling directions.
  ACCEPTABLE: `modifications to that manifest require updating this commit; modifications to this commit require updating that manifest` -- both directions stated; passes C-41 and C-45
  FAILS: `modifications to that manifest require updating this commit` -- one direction only; half-coupling; reverse obligation absent; fails C-45

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE * [N] CONDITION * [N] BLOCK` -- COUNT each token in ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME -- all APPROVE -> APPROVED; any CONDITION no BLOCK -> APPROVED WITH CONDITIONS; any BLOCK -> BLOCKED or DEFERRED per committee type.
VALIDATE: TALLY counts match ## STANCE MANIFEST exactly; mismatch fails C-35.
  ACCEPTABLE: `TALLY: 2 APPROVE * 1 CONDITION * 1 BLOCK` when ## STANCE MANIFEST shows exactly those tokens
  FAILS: count differing from manifest -- re-parsing Phase 3 prose rather than counting the manifest
ENFORCE: PHASE-4-COMMIT: is terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] -- TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position -- NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS:
WRITE: Verdict -- matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval -- name each condition explicitly; "address feedback" fails; specific deliverable or named state passes.
REQUIRE (not APPROVED): Owner -- named role from Phase 0 roster; not a team.
REQUIRE (not APPROVED): Trigger -- concrete deliverable or event causing re-review; "sufficient progress" fails; named artifact + named recipient + named authority passes.
VALIDATE: both Owner and Trigger present when verdict not APPROVED; missing either fails C-23.

ACTION ITEMS:
PRINT: `[Owner Role] -- [specific action] -- [deadline]` one line per item.
REQUIRE: all three fields; "investigate" without specifying question, artifact, and recipient fails.

DISSENTING OPINIONS:
WRITE: for each CONDITION or BLOCK -- specific objection citing INERTIA-FINDING-* label from ## INERTIA RECORD where applicable; resolution path with concrete condition and named authority.
VALIDATE: cited INERTIA-FINDING-* labels match labels enumerated in ## INERTIA RECORD.
ENFORCE: if no dissent -- `No dissent -- [reason]`.
ENFORCE: PHASE-5-COMMIT: is terminal element of Phase 5 and final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] -- DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position -- NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
"""

with open(TARGET, "a", encoding="utf-8") as f:
    f.write(V03)
    f.write(V04)
    f.write(V05)

print("Done. Appended V-03, V-04, V-05.")
