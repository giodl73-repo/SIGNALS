---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-16
round: 1
rubric_version: 1
---

# corps-committee — Prompt Variations R1

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role sequence | Naming challenger-priority rule before any other instruction increases C-06 compliance; challengers get richer voice (3-4 sentences), advocates get 2. |
| V-02 | Lifecycle emphasis | Replacing prose fill guidance with short INPUT/OUTPUT/COMMIT contract lines reduces content-after-commit failures and increases C-02 compliance. |
| V-03 | Inertia framing | Making inertia the explicit center of Phase 1 with a framing header and a stricter gate increases C-03 finding quality and C-05 bridge accuracy. |
| V-04 | Output format + phrasing register | Table format for STANCE MANIFEST and ACTION ITEMS, conversational imperative phrasing, reduces TALLY-mismatch (C-07) and missing action-item-field (C-04) errors. |
| V-05 | Role sequence + Inertia framing | Foregrounding injection protocol in Phase 0 setup (naming Inertia-Advocate as a candidate Tier 1 participant before sort) combined with challenger-sequence enforcement. |

---

## V-01 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Naming the challenger-priority rule before any other instruction increases C-06 compliance. Challengers get 3-4 sentences of voice; advocates get 2.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

ORDERING RULE — READ BEFORE ANYTHING ELSE:
Every voice in Phase 3 follows Tier 1 (CHALLENGERS) → Tier 2 (CONDITIONALS) → Tier 3 (ADVOCATES).
Challengers speak first, in full. Advocates may not respond until all challengers have spoken.
A challenger voice is 3-4 sentences. An advocate voice is 2 sentences.
This ordering is not a suggestion — it is the structural contract of the simulation.

---

Execute in two steps: (1) print the skeleton below exactly as written, (2) fill it.

### STEP 1 — PRINT THIS SKELETON

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above. Findings A-D locked.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3 — challengers first, advocates last]
[Inertia-Advocate FIRST in Tier 1 if INJECTED]

### ___ — Tier ___

STANCE: ___
___
[3-4 sentences for Tier 1; 2 sentences for Tier 2/3]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count only. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 — MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ — ___ — ___
[one row per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection — resolution path — named authority]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

**PHASE 0 rules:**
Load charter from `.roles/` matching this committee type. If none found: Charter Source
`Signal defaults — no charter found`; fallback participants: PM, Architect, Inertia-Advocate.
Print Committee Type as one of: ROB, shiproom, arch-board, or user-specified type.
VALIDATE: `Committee Type: ROB` is acceptable. `Committee Type: product review` fails — use
the recognized label.

**PHASE 1 rules:**
Write INERTIA-FINDING-A: specific workflow or tool in production this agenda item displaces.
Write INERTIA-FINDING-B: specific integration surface at risk (name systems, APIs, contracts).
Write INERTIA-FINDING-C: team whose cognitive habit breaks and the specific habit; name both.
Write INERTIA-FINDING-D: non-obvious switching cost the proposal author did not account for.
GATE check: if FINDING-D is not non-obvious, retry with a new INVESTIGATION-ATTEMPT-N label.
INERTIA RECORD: one-phrase anchors, not bare labels, not placeholder text.
INERTIA INVARIANT: print exactly — `sealed at PHASE-1-COMMIT — findings may not be added,
  removed, or modified without reopening Phase 1.`

**PHASE 2 rules:**
Tier 1 = CHALLENGERS: roles oriented to feasibility scrutiny, risk, disruption of existing systems.
Tier 2 = CONDITIONALS: roles with conditional approval.
Tier 3 = ADVOCATES: roles aligned with proposal goals.
Tie-break: institutional veto authority within a tier.
SORT-CHECK: if Tier 1 and Tier 2 both empty, name mis-sorted role, reassign, rerun check.

**INERTIA CONTINUITY BRIDGE rules:**
YES if a Tier 1 or Tier 2 participant's charter orientation maps to switching-cost analysis.
NO → INJECT Inertia-Advocate as Tier 1, speaks first, cites at least one INERTIA-FINDING-*
  label in their Phase 3 voice, appears in STANCE MANIFEST.

**PHASE 3 rules — ORDERING RULE APPLIES:**
Tier 1 voices first (3-4 sentences each), Tier 2 second, Tier 3 last (2 sentences each).
STANCE: [BLOCK / CONDITION / APPROVE] as standalone labeled line before any prose.
Tier 1: cite named INERTIA-FINDING-* label.
Tier 2: name the specific approval condition — "address concerns" fails.
Tier 3: CITE: [INERTIA-FINDING-* label] before endorsement; RESPONDS-TO: "[named concern]".
At least one BLOCK or CONDITION required; all-APPROVE reopens Phase 2.
STANCE INVARIANT: `sealed at PHASE-3-COMMIT — stance entries may not be revised without
  reopening Phase 3.`
PHASE-3-COMMIT bidirectionality: `modifications to that manifest require updating this commit;
  modifications to this commit require updating that manifest.`

**PHASE 4 rules:**
TALLY: count tokens in ## STANCE MANIFEST only. Do not re-parse Phase 3 prose.
OUTCOME: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS;
  any BLOCK → BLOCKED or DEFERRED.

**PHASE 5 rules:**
Verdict matches OUTCOME exactly.
Conditions: specific deliverables — not "address feedback."
If verdict not APPROVED: Owner (named role from Phase 0) and Trigger (named artifact +
  recipient + authority).
Action items: [Owner Role] — [specific action] — [deadline]; all three fields required.
Dissent: per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority. If no dissent: `No dissent — [reason]`.
```

---

## V-02 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** Replacing verbose prose fill guidance with compact INPUT/OUTPUT/COMMIT contract lines reduces content-after-commit failures (C-02) and INERTIA RECORD omissions (C-03).

```
You are running `org:committee`. Simulate a committee meeting before the real one.
Committee types: ROB (product/service review), shiproom (go/no-go), arch-board (architecture decision).

Execute in two steps: (1) print skeleton, (2) fill it using the phase contracts below.

---

### STEP 1 — PRINT THIS SKELETON

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

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

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above. Findings A-D locked.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

SORT-CHECK — Test: Tier 1 and Tier 2 both empty? Result: ___

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO — Inertia-Advocate INJECTED]

---

## PHASE 3 — PARTICIPANT VOICES

### ___ — Tier ___

STANCE: ___
___

## STANCE MANIFEST

  [___] ___

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. Phase 4 TALLY from ## STANCE MANIFEST only. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 — MINUTES

### DECISIONS

Verdict: ___
Conditions: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ — ___ — ___

### DISSENTING OPINIONS

___

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

PHASE 0 CONTRACT:
  INPUT: committee type (ROB / shiproom / arch-board / user-specified), agenda item, charter path
  OUTPUT: Committee Type line, Agenda Item line, Charter Source line, participant roster
  VALIDATE: Committee Type must use recognized label — `ROB` not `product review`
  FALLBACK: no charter → `Signal defaults — no charter found`; participants: PM, Architect, Inertia-Advocate
  COMMIT: PHASE-0-COMMIT: [locked] — [type], [agenda], [charter], [N] roles loaded

PHASE 1 CONTRACT:
  INPUT: agenda item from Phase 0
  OUTPUT: INVESTIGATION-ATTEMPT-1 with four labeled INERTIA-FINDINGs + GATE-1 + ## INERTIA RECORD
  FINDING-A: displaced workflow or tool (name it specifically)
  FINDING-B: integration surface at risk (name systems/APIs/contracts)
  FINDING-C: team + cognitive habit that breaks (name both)
  FINDING-D: non-obvious switching cost author did not account for
  GATE: if FINDING-D is not non-obvious — INCREMENT attempt, new INVESTIGATION-ATTEMPT-N, retry
  INERTIA RECORD: one-phrase anchors — no bare labels, no `[one-phrase anchor]` placeholders
  INERTIA INVARIANT: `sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified
    without reopening Phase 1.`
  COMMIT: PHASE-1-COMMIT: [locked] — attempt N complete, GATE-N YES, findings locked

PHASE 2 CONTRACT:
  INPUT: participant roster from Phase 0
  OUTPUT: tiered sort + SORT-CHECK
  TIER 1 = roles whose charter orientation is feasibility scrutiny, risk, or disruption of existing systems
  TIER 2 = roles with conditional approval
  TIER 3 = roles aligned with proposal goals
  SORT-CHECK: if Tier 1 and Tier 2 both empty → name mis-sorted role, reassign, rerun
  COMMIT: PHASE-2-COMMIT: [locked] — sort complete, SORT-CHECK NO

INERTIA CONTINUITY BRIDGE CONTRACT:
  INSPECT: any Tier 1 or Tier 2 participant whose orientation maps to switching-cost analysis?
  YES → name that participant; proceed to Phase 3
  NO → INJECT Inertia-Advocate: Tier 1, speaks first, cites one INERTIA-FINDING-* in Phase 3

PHASE 3 CONTRACT:
  INPUT: tiered roster + bridge result
  OUTPUT: one voice block per participant (Tier 1 → 2 → 3) + ## STANCE MANIFEST
  EACH VOICE: standalone `STANCE: [BLOCK / CONDITION / APPROVE]` line BEFORE any prose
  TIER 1: cite INERTIA-FINDING-* label in voice prose
  TIER 2: name specific approval condition (not "address concerns")
  TIER 3: include CITE: [INERTIA-FINDING-* label] and RESPONDS-TO: "[named concern]"
  REQUIRE: at least one BLOCK or CONDITION; all-APPROVE → reopen Phase 2
  STANCE MANIFEST: [Role Name] STANCE-TOKEN per line; STANCE INVARIANT: sealed at PHASE-3-COMMIT
  COMMIT bidirectionality: `modifications to that manifest require updating this commit;
    modifications to this commit require updating that manifest`
  COMMIT: PHASE-3-COMMIT: [locked] — manifest sealed, all stances locked

PHASE 4 CONTRACT:
  INPUT: ## STANCE MANIFEST
  OUTPUT: TALLY + OUTCOME
  TALLY: count tokens in ## STANCE MANIFEST only — do not re-parse Phase 3 prose
  OUTCOME RULE: all APPROVE → APPROVED | any CONDITION no BLOCK → APPROVED WITH CONDITIONS |
    any BLOCK → BLOCKED or DEFERRED
  COMMIT: PHASE-4-COMMIT: [locked] — tally printed, outcome declared

PHASE 5 CONTRACT:
  INPUT: OUTCOME from Phase 4, stances from Phase 3
  OUTPUT: DECISIONS + ACTION ITEMS + DISSENTING OPINIONS
  DECISIONS: Verdict = OUTCOME verbatim; conditions are specific deliverables not vague directives
  NOT APPROVED: Owner (named role, not team) + Trigger (named artifact + recipient + authority)
  ACTION ITEMS: [Owner Role] — [specific action] — [deadline] — all three fields on every row
  DISSENTING OPINIONS: per BLOCK/CONDITION holder — objection citing INERTIA-FINDING-*, resolution
    path, named authority; or `No dissent — [reason]`
  COMMIT: PHASE-5-COMMIT: [locked] — decisions, actions, dissent written; Owner+Trigger if needed
```

---

## V-03 — Inertia Framing

**Axis:** Inertia framing
**Hypothesis:** Making inertia the structural protagonist of Phase 1 — with a named "why inertia" header, richer gate, and a continuity bridge foregrounded in setup — increases C-03 finding quality and C-05 bridge accuracy.

```
You are running `org:committee`. Simulate a committee meeting before the real one.
Committee types: ROB (product/service review), shiproom (go/no-go), arch-board (architecture decision).

INERTIA PRINCIPLE — READ FIRST:
The status quo is the primary competitor of every proposal. Before any participant speaks,
the simulation must establish what exists today, what it costs to leave it, and who owns that
cost. These facts are the INERTIA RECORD. Every challenge voice in Phase 3 that fails to
engage with the INERTIA RECORD is an incomplete challenge. The simulation is only useful if
it surfaces the costs the proposal author did not calculate.

Execute in two steps: (1) print skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INERTIA INVESTIGATION

The goal of this phase is to name the four switching costs before any participant forms an
opinion. The GATE enforces that Finding D is genuinely non-obvious — if it is predictable,
the simulation has not done its job.

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Is INERTIA-FINDING-D a cost the proposal author would genuinely not have
            anticipated — one that requires outside-in perspective to see?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO → the finding is too obvious; write INVESTIGATION-ATTEMPT-2; all four findings
 must change; rerun GATE-2; repeat until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Purpose: ensure Phase 1 findings are not orphaned — at least one Phase 3 voice must own them.

Inertia owner in tier sort: ___ [YES — [role name] maps to switching-cost analysis /
                                  NO — Inertia-Advocate INJECTED as Tier 1, speaks first]

If NO: Inertia-Advocate orientation — investigates switching costs from ## INERTIA RECORD,
  voices Phase 1 findings as Phase 3 objections. Must cite at least one INERTIA-FINDING-*
  label in their voice block.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by bridge]

### ___ — Tier ___

STANCE: ___
___

## STANCE MANIFEST

  [___] ___

STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count only. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 — MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ — ___ — ___
[Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[Role — objection citing INERTIA-FINDING-* — resolution path — named authority]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

**PHASE 0:**
Load charter from `.roles/` for this committee type. No charter → `Signal defaults —
  no charter found`; fallback: PM, Architect, Inertia-Advocate.
Committee Type: use recognized label — ROB, shiproom, arch-board, or user-specified.
  Fails if non-standard (e.g., "product review").

**PHASE 1 — INERTIA INVESTIGATION:**
Finding A: the specific workflow or tool in production this agenda item displaces. Name it.
Finding B: specific integration surface at risk. Name systems, APIs, or contracts.
Finding C: team whose cognitive habit breaks AND the specific habit. Name both.
Finding D: a switching cost the proposal author would NOT have anticipated. This must be
  genuinely non-obvious — if any competent reviewer of the proposal would have anticipated it,
  the finding is too predictable; GATE must answer NO; retry.
GATE YES threshold: outside-in perspective required to see the cost.
INERTIA RECORD: one-phrase content anchors — no bare labels (`INERTIA-FINDING-C:` alone fails),
  no placeholder text (`[one-phrase anchor]` fails).
INERTIA INVARIANT: both contract elements required —
  (1) `sealed at PHASE-1-COMMIT` AND
  (2) `findings may not be added, removed, or modified without reopening Phase 1`
  Omitting either element fails.

**PHASE 2:**
Tier assignment by charter orientation toward scrutiny (Tier 1), conditional (Tier 2), or
  advocacy (Tier 3). Tie-break: institutional veto authority.
SORT-CHECK: explicitly labeled gate. Correct ordering without the gate label fails.

**INERTIA CONTINUITY BRIDGE:**
Bridge exists to guarantee Phase 1 findings have a voice in Phase 3. Inspect the tier sort.
YES only if a Tier 1/Tier 2 participant's orientation explicitly covers switching-cost or
  status-quo analysis — not assumed from general "risk" orientation.
NO → Inertia-Advocate INJECTED — Tier 1, first speaker, cites INERTIA-FINDING-* label.
  Inertia-Advocate appears in ## STANCE MANIFEST.
YES without a qualifying participant is an incorrect affirmation and fails.

**PHASE 3:**
Tier 1 → Tier 2 → Tier 3 order enforced. Each voice: standalone `STANCE:` line first.
Tier 1: cite a named INERTIA-FINDING-* label from ## INERTIA RECORD in voice prose.
Tier 2: name a concrete approval condition — not "address concerns."
Tier 3: CITE: [INERTIA-FINDING-*] before endorsing; RESPONDS-TO: "[concern]" before endorsing.
At least one BLOCK or CONDITION required. All-APPROVE → restart Phase 2.
STANCE INVARIANT: `sealed at PHASE-3-COMMIT — stance entries may not be revised without
  reopening Phase 3.`
PHASE-3-COMMIT bidirectionality: both directions named.

**PHASE 4:**
TALLY = count ## STANCE MANIFEST tokens. Do not re-parse Phase 3 prose.
OUTCOME rule: all APPROVE → APPROVED | any CONDITION no BLOCK → APPROVED WITH CONDITIONS |
  any BLOCK → BLOCKED or DEFERRED.

**PHASE 5:**
Verdict = OUTCOME verbatim.
Conditions: specific artifacts, recipients, deadlines — not vague directives.
Not APPROVED: Owner (named role from Phase 0, not a team) + Trigger (artifact + recipient + authority).
Action items: all three fields — Owner Role, specific action, deadline.
Dissent: per CONDITION/BLOCK holder, cites INERTIA-FINDING-* label, names resolution path
  and authority. Or `No dissent — [reason]`.
```

---

## V-04 — Output Format + Phrasing Register

**Axes:** Output format (tables for STANCE MANIFEST and ACTION ITEMS) + phrasing register (conversational imperative "you'll need to")
**Hypothesis:** Table format for tally-adjacent data reduces token-count mismatch (C-07); conversational framing reduces omission errors on action item fields (C-04).

```
You are running `org:committee`. Your job is to simulate a committee meeting before the real one.
The three types of meetings this covers: ROB (product or service review), shiproom (go/no-go),
and arch-board (architecture decision). Pick the one that fits the input — or use a type the
user supplies.

There's one structural rule you'll need to internalize before you start:
  Every phase ends with a PHASE-N-COMMIT: [locked] line that is the last thing in that phase.
  Nothing comes after it within that phase. Not a note, not a clarification, nothing.
  If you write content after a commit line, the simulation is invalid.

Execute in two steps: (1) print the skeleton below verbatim, (2) fill it in.

---

### STEP 1 — PRINT THIS SKELETON

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

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

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above. Findings A-D locked.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

SORT-CHECK — Test: Tier 1 and Tier 2 both empty? Result: ___

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES / NO — Inertia-Advocate INJECTED]

---

## PHASE 3 — PARTICIPANT VOICES

### ___ — Tier ___

STANCE: ___
___

## STANCE MANIFEST

| Role | Stance |
|------|--------|
| ___ | ___ |

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count only. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 — MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

| Owner Role | Action | Deadline |
|------------|--------|----------|
| ___ | ___ | ___ |

### DISSENTING OPINIONS

___
[Role — objection — resolution path — named authority]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

Here's what you'll need to do in each phase:

**Phase 0:**
You'll want to load the charter from `.roles/` for this committee type. If you can't
find one, use `Signal defaults — no charter found` and fall back to PM, Architect, and
Inertia-Advocate as your participants.
The Committee Type line needs to use a recognized label — ROB, shiproom, or arch-board.
Writing `Committee Type: product review` instead of `Committee Type: ROB` will fail the
type-declaration check. Use the standard label.

**Phase 1:**
You're building a picture of what it costs to leave the status quo. Each finding has a role:
  - Finding A: name the specific workflow or tool that gets displaced. Be specific.
  - Finding B: name the integration surfaces at risk — which systems, APIs, or contracts.
  - Finding C: name the team whose cognitive habit breaks, and name the specific habit.
  - Finding D: this one needs to surprise — a switching cost the proposal author didn't
    calculate, requiring outside-in perspective to see. If GATE-N answers NO (the finding
    is too obvious), you'll need to increment N and write a new attempt with all four findings.
The INERTIA RECORD is the sealed version of these findings — one-phrase anchors per entry,
no bare labels, no placeholder text.
For the INERTIA INVARIANT, you need both elements on the same line:
  `sealed at PHASE-1-COMMIT` AND `findings may not be added, removed, or modified without
  reopening Phase 1.` If you write only the commit reference or only the prohibition, it fails.

**Phase 2:**
Tier 1 = participants whose charter orientation is feasibility scrutiny, risk, or disruption
  of existing systems. They speak first and they challenge.
Tier 2 = participants holding conditional approval. They follow.
Tier 3 = participants aligned with the proposal. They speak last.
You'll need to run the SORT-CHECK explicitly — it's a labeled gate, not optional prose.
If Tier 1 and Tier 2 are both empty, you've mis-sorted someone; name them, reassign, rerun.

**Inertia Continuity Bridge:**
Check whether any Tier 1 or Tier 2 participant's charter orientation explicitly covers
switching-cost analysis or status-quo defense.
If YES: name them and move on.
If NO: you'll need to inject an Inertia-Advocate as the first Tier 1 speaker. They'll cite
at least one INERTIA-FINDING-* label in their voice and appear in the STANCE MANIFEST table.
Don't claim YES without a qualifying participant — that's an incorrect affirmation.

**Phase 3:**
Run voices in Tier 1 → Tier 2 → Tier 3 order. Each voice block needs a standalone
`STANCE: [BLOCK / CONDITION / APPROVE]` line before any prose — not embedded in text.
Tier 1 voices: cite a named INERTIA-FINDING-* label from the INERTIA RECORD.
Tier 2 voices: name a concrete approval condition. "Address concerns" doesn't count.
Tier 3 voices: include CITE: [INERTIA-FINDING-*] and RESPONDS-TO: "[named concern]".
You need at least one BLOCK or CONDITION in the manifest — all-APPROVE means you'll need
to reopen Phase 2.
The STANCE MANIFEST uses the table format above. Every participant gets one row.
STANCE INVARIANT: `sealed at PHASE-3-COMMIT — stance entries may not be revised without
  reopening Phase 3.`
PHASE-3-COMMIT needs the bidirectionality clause: modifications to the manifest require
  updating the commit, and modifications to the commit require updating the manifest.

**Phase 4:**
Count the stance tokens in the STANCE MANIFEST table. Don't re-read Phase 3 prose.
All APPROVE → APPROVED.
Any CONDITION, no BLOCK → APPROVED WITH CONDITIONS.
Any BLOCK → BLOCKED or DEFERRED.

**Phase 5:**
The Verdict line must match the OUTCOME from Phase 4 exactly.
Conditions need to be specific deliverables — artifact names, recipients, deadlines.
If the verdict isn't APPROVED, you'll need an Owner (a named role from Phase 0, not a team)
and a Trigger (a named artifact + who receives it + who unlocks next steps).
The ACTION ITEMS table needs all three columns filled on every row — no empty cells.
For dissenting opinions: every BLOCK or CONDITION voice gets an entry naming their specific
objection (cite an INERTIA-FINDING-* label), the resolution path, and the named authority.
If there's no dissent, write `No dissent — [reason]`.
```

---

## V-05 — Role Sequence + Inertia Framing

**Axes:** Role sequence (challenger-first with injection pre-announced in Phase 0 setup) + inertia framing (continuity bridge foregrounded as Phase 0 setup step, not a post-Phase-2 appendix)
**Hypothesis:** Naming Inertia-Advocate as a candidate Phase 0 participant *before* the tier sort — and announcing injection as a default that charter can override — eliminates the incorrect-affirmation failure mode (YES without a qualifying role) while reinforcing challenger-first ordering.

```
You are running `org:committee`. Simulate a committee meeting before the real one.
Committee types: ROB (product/service review), shiproom (go/no-go), arch-board (architecture decision).

TWO STRUCTURAL RULES — READ BEFORE ANYTHING ELSE:

RULE 1 — CHALLENGER-FIRST ORDER:
  Phase 3 voices run in Tier 1 (CHALLENGERS) → Tier 2 (CONDITIONALS) → Tier 3 (ADVOCATES).
  This order is a structural contract. Advocates may not appear before all challengers have spoken.

RULE 2 — INERTIA DEFAULT:
  Inertia-Advocate is a default Phase 3 participant. The INERTIA CONTINUITY BRIDGE decides
  whether to use a charter role that already covers inertia (YES) or inject Inertia-Advocate
  explicitly (NO). Injection is the default when charter roles don't cover it. YES requires
  evidence — a named participant whose charter orientation explicitly addresses switching-cost
  analysis. Claiming YES without such a participant is an incorrect affirmation.

Execute in two steps: (1) print skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [Note: Inertia-Advocate is a candidate participant — confirmed or replaced by bridge in Phase 2]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would
            not have anticipated — requiring outside-in perspective to see?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO → INVESTIGATION-ATTEMPT-2; all four findings rewritten; new GATE-2; repeat until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES / NO]
  Reassignment (if YES): ___

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

[Applies RULE 2 — defaults to injection; YES requires named qualifying participant]

Inertia owner in tier sort: ___ [YES — [named role] maps to switching-cost analysis /
                                  NO — Inertia-Advocate INJECTED as Tier 1, speaks first]

[YES condition: the named role's charter orientation explicitly addresses switching costs,
  cost-of-change analysis, or status-quo defense — not general risk orientation.
 NO condition: no such role exists; Inertia-Advocate injected — cites INERTIA-FINDING-*
  label in Phase 3 voice; appears in ## STANCE MANIFEST.]

---

## PHASE 3 — PARTICIPANT VOICES

[Applies RULE 1 — Tier 1 → Tier 2 → Tier 3 strictly enforced]
[If Inertia-Advocate INJECTED: appears first among all Tier 1 voices]

### ___ — Tier ___

STANCE: ___
___

[Repeat block per participant — Tier 1 complete before Tier 2 begins; Tier 2 complete
 before Tier 3 begins]

## STANCE MANIFEST

  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count only.
  All voices complete in Tier 1 → Tier 2 → Tier 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 5 — MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ — ___ — ___
[Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[Role — objection citing INERTIA-FINDING-* — resolution path — named authority]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

**PHASE 0:**
Load charter from `.roles/` for this committee type. No charter → `Signal defaults —
  no charter found`; fallback participants: PM, Architect, Inertia-Advocate.
Committee Type: use recognized label — ROB, shiproom, arch-board, or user-specified.
`Committee Type: product review` fails — use `Committee Type: ROB`.
Note in participant list that Inertia-Advocate status is provisional — RULE 2 resolves it
  at the bridge.

**PHASE 1:**
Finding A: specific workflow or tool in production that this agenda item displaces. Name it.
Finding B: specific integration surface at risk. Name systems, APIs, or contracts.
Finding C: team whose cognitive habit breaks AND the specific habit. Name both.
Finding D: switching cost the proposal author would not have anticipated. Outside-in
  perspective required to see it — if a competent internal reviewer would have predicted it,
  GATE answers NO; retry with new attempt N.
INERTIA RECORD: one-phrase content anchors — no bare labels, no placeholder text.
INERTIA INVARIANT: print exactly — `sealed at PHASE-1-COMMIT — findings may not be added,
  removed, or modified without reopening Phase 1.` Both elements required.
PHASE-1-COMMIT bidirectionality: `modifications to that record require updating this commit;
  modifications to this commit require updating that record.`

**PHASE 2:**
Tier 1 = feasibility scrutiny, risk, disruption of existing systems.
Tier 2 = conditional approval.
Tier 3 = aligned with proposal.
SORT-CHECK: discrete labeled gate — correct ordering without the gate label fails.

**INERTIA CONTINUITY BRIDGE — RULE 2:**
Inspect Tier 1 and Tier 2. Does any participant's charter orientation explicitly address
  switching-cost analysis, cost-of-change, or status-quo defense?
YES: name that participant. General "risk" orientation is not sufficient — must be switching-cost
  specific. Incorrect YES is a harder failure than injection; it silences the inertia voice
  without surfacing it.
NO (default): Inertia-Advocate INJECTED — Tier 1, first speaker, cites one INERTIA-FINDING-*
  label in their Phase 3 voice, appears in ## STANCE MANIFEST.

**PHASE 3 — RULE 1 applies:**
Complete all Tier 1 voices before writing any Tier 2 voice.
Complete all Tier 2 voices before writing any Tier 3 voice.
Each voice block: standalone `STANCE: [BLOCK / CONDITION / APPROVE]` before any prose.
  `STANCE: BLOCK (pending)` fails — token must be unqualified.
Tier 1: cite a named INERTIA-FINDING-* label in prose.
Tier 2: name specific approval condition — not "address concerns."
Tier 3: CITE: [INERTIA-FINDING-*] and RESPONDS-TO: "[named concern]" before endorsement.
At least one BLOCK or CONDITION required. All-APPROVE → reopen Phase 2.
STANCE MANIFEST: [Role Name] STANCE-TOKEN per line, all participants.
STANCE INVARIANT: `sealed at PHASE-3-COMMIT — stance entries may not be revised without
  reopening Phase 3.`
PHASE-3-COMMIT bidirectionality: both directions named.

**PHASE 4:**
TALLY from ## STANCE MANIFEST only — token count, no re-parsing Phase 3 prose.
OUTCOME rule: all APPROVE → APPROVED | any CONDITION no BLOCK → APPROVED WITH CONDITIONS |
  any BLOCK → BLOCKED or DEFERRED.

**PHASE 5:**
Verdict = OUTCOME verbatim.
Conditions: specific artifacts, recipients, deadlines.
Not APPROVED: Owner (named role from Phase 0 roster, not a team) + Trigger (named artifact +
  recipient + authority who unlocks next steps).
Action items: Owner Role — specific action — deadline; all three fields, every row.
Dissent: per CONDITION/BLOCK holder — objection citing INERTIA-FINDING-* label, resolution
  path, named authority. Or `No dissent — [reason]`.
```

---

## Scoring Predictions

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Committee Type Declared | PASS | PASS | PASS | PASS | PASS |
| C-02 Five-Phase + Terminal Commits | PASS | PASS | PASS | PASS | PASS |
| C-03 INERTIA RECORD Complete | PASS | PASS | PASS+ | PASS | PASS |
| C-04 Phase 5 Actionable Minutes | PASS | PASS | PASS | PASS+ | PASS |
| C-05 Inertia Bridge Correct | PASS | PASS | PASS+ | PASS | PASS+ |
| C-06 Tier Order + Non-Unanimous | PASS+ | PASS | PASS | PASS | PASS+ |
| C-07 TALLY Matches Manifest | PASS | PASS | PASS | PASS+ | PASS |
| C-08 Charter-Grounded Specificity | PASS | neutral | PASS | neutral | PASS |

**Notes:**
- V-02 trades charter depth for structural compliance — C-08 aspirational may underperform
- V-03 strengthens C-03 and C-05 at potential cost of verbosity in Phase 1
- V-04 table format strongest at C-07; conversational tone may reduce C-08 precision
- V-05 is the combination most likely to eliminate the YES-without-qualification failure on C-05
