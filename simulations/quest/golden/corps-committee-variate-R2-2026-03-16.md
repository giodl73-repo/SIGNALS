---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-16
round: 2
rubric_version: 2
---

# corps-committee — Prompt Variations R2

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role-distinctive voices | Requiring each participant to open with an explicit `ORIENTATION-LENS:` line — quoting their charter phrase — forces voice differentiation that satisfies C-09; generic role-name opinions become structurally impossible. |
| V-02 | Structural-table format | Replacing the STANCE MANIFEST list and ACTION ITEMS list with Markdown tables (named columns, no blank cells) satisfies C-10; completeness is visually verifiable and token-counting errors drop. |
| V-03 | Injection-default framing | Declaring Inertia-Advocate as the always-present default and recasting the INERTIA CONTINUITY BRIDGE as a YES-gate (with explicit "YES without a qualifying participant fails" language) satisfies C-11 and eliminates the silent-absence failure. |
| V-04 | Role-distinctive voices + Table format | Combines V-01 and V-02 axes: `ORIENTATION-LENS:` anchoring for C-09 and Markdown tables for C-10. Single output that should score full points on both aspirational criteria simultaneously. |
| V-05 | Full integration (C-09 + C-10 + C-11) | Combines all three new aspirational axes into one prompt. Hypothesis: when all three mechanisms are co-present — orientation anchoring, table structure, and injection-default framing — the output earns all three aspirational criteria plus the full essential/recommended pass set. |

---

## V-01 — Role-Distinctive Voices

**Axis:** Role-distinctive voices
**Hypothesis:** An explicit `ORIENTATION-LENS:` line at the top of each Phase 3 voice block — quoting the participant's charter orientation phrase verbatim — makes it structurally impossible to write interchangeable voices. The orientation line acts as a public commitment; the prose that follows must be coherent with it.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — [orientation phrase from charter]
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded, orientation phrases extracted.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1. Continue until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

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

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED]

### ___ — Tier ___

ORIENTATION-LENS: [verbatim orientation phrase from Phase 0 participant list]
STANCE: ___
___  [2-4 sentences — must follow from ORIENTATION-LENS, not generic role opinion]
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
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
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type, Agenda Item, Charter Source.
PRINT: each participant on its own line as: [Role Name] — [orientation phrase from charter].
VALIDATE: orientation phrase is a verbatim or close-paraphrase of the charter field — not
  a summary invented at Phase 3. The Phase 0 list is the authoritative source for Phase 3
  ORIENTATION-LENS lines.
  ACCEPTABLE: `Program Manager — drives adoption and user value realization`
  FAILS: `Program Manager — manages the program` — generic label, not charter orientation

PRINT: PHASE-0-COMMIT including count of roles loaded and confirmation that orientation
  phrases were extracted.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; GATE-N+1; repeat.
ENFORCE: loop runs within Phase 1; Phase 2 reached unconditionally after any YES.

WRITE: ## INERTIA RECORD — one-phrase anchors from the passing attempt's findings.
VALIDATE: each entry carries a content anchor — not a bare label, not a placeholder.

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
VALIDATE: commit reference and modification prohibition both present.
  FAILS (a): commit reference present, prohibition absent
  FAILS (b): line present, neither element present
  FAILS (c): line absent entirely

PRINT: PHASE-1-COMMIT with bidirectionality clause — modifications to that record require
  updating this commit; modifications to this commit require updating that record.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) — charter roles whose orientation maps to feasibility scrutiny,
  risk, or disruption of existing systems; speak first.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding conditional approval; speak second.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with proposal goals; speak last.
ENFORCE: tie-break by institutional veto authority within a tier.

SORT-CHECK: Test: Tier 1 and Tier 2 both empty? Result: YES / NO.
IF YES: name mis-sorted role, target tier, reason; reprint corrected TIER SORT; loop until NO.

PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rules:**

INSPECT: Phase 2 TIER SORT — identify any Tier 1 or Tier 2 participant whose charter
  orientation maps to switching-cost investigation, status-quo defense, or cost-of-change analysis.
CONFIRM: `Inertia owner in tier sort: YES` if such a participant exists; proceed to Phase 3.
CONFIRM: `Inertia owner in tier sort: NO` if none exists:
  INJECT: Inertia-Advocate as Phase 3 Tier 1 participant — speaks first.
  ORIENTATION: investigates switching costs from ## INERTIA RECORD.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in their voice block.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.

VALIDATE: both FAILS axes required.
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS (incorrect affirmation): YES declared when no Tier 1/Tier 2 participant maps to inertia

---

**PHASE 3 fill rules — ORIENTATION-LENS is mandatory:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED — Inertia-Advocate voice FIRST in Tier 1.

PRINT: `ORIENTATION-LENS: [verbatim orientation phrase from Phase 0]` as the FIRST line of
  every voice block — before STANCE: and before any prose.
VALIDATE: ORIENTATION-LENS phrase matches the Phase 0 participant list entry for this role.
  ACCEPTABLE: exact or close-paraphrase match
  FAILS: orientation phrase invented at Phase 3 that was not declared in Phase 0
  FAILS: ORIENTATION-LENS line absent — C-09 fails for this voice

ROLE-DISTINCTIVENESS RULE:
VALIDATE: at least three voice blocks contain concerns that are visibly derived from their
  ORIENTATION-LENS phrase and could not be transplanted to a different participant without
  violating that participant's orientation.
  ACCEPTABLE: Risk Officer cites regulatory exposure specifically tied to "compliance and
    audit-trail oversight" orientation; Finance cites budget-cycle timing specifically tied
    to "cost governance and fiscal constraint" orientation — neither concern is generic
  FAILS: all voices raise "technical risk", "user confusion", "timeline slippage" —
    interchangeable concerns with no orientation anchor

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line after ORIENTATION-LENS,
  before prose.
WRITE: 2-4 sentences per participant. Prose must follow from ORIENTATION-LENS. If the concern
  cannot be explained by citing the ORIENTATION-LENS phrase, rewrite it.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label — content] and RESPONDS-TO: "[named concern]"
  before endorsement.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.
WRITE: ## STANCE MANIFEST — one entry per participant: [Role Name] STANCE-TOKEN.

PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.`
VALIDATE: commit reference and modification prohibition both present.
  FAILS (a): prohibition absent; FAILS (b): neither element; FAILS (c): line absent

PRINT: PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in ## STANCE MANIFEST.
WRITE: OUTCOME from TALLY rule.
VALIDATE: counts match ## STANCE MANIFEST exactly.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role) and Trigger (named artifact + recipient + authority).
PRINT: action items as [Owner Role] — [specific action] — [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority.
ENFORCE: if no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-02 — Structural-Table Format

**Axis:** Output format — structural tables for mechanical sections
**Hypothesis:** Rendering STANCE MANIFEST and ACTION ITEMS as Markdown tables with named columns makes completeness visually checkable. Missing cells are instantly visible. Token-counting errors that caused TALLY mismatches in R1 drop because the table rows make the count mechanical.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1. Continue until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

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

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED]

### ___ — Tier ___

STANCE: ___
___  [prose]
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

| Role | Stance |
|------|--------|
| ___ | ___ |
[repeat per participant — no blank cells]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice
  prose is not permitted.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
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

| Owner | Action | Deadline |
|-------|--------|----------|
| ___ | ___ | ___ |
[one row per item — no blank cells]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type, Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

GATE-N intra-phase retry:
IF NO: INCREMENT N; new label; rewrite all four findings; loop until YES.

WRITE: ## INERTIA RECORD — one-phrase anchors from the passing attempt.
VALIDATE: each entry has a content anchor — not a bare label, not a placeholder.

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
VALIDATE: commit reference and modification prohibition both present.
  FAILS (a): prohibition absent; FAILS (b): neither element; FAILS (c): line absent

PRINT: PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS), Tier 2 (CONDITIONALS), Tier 3 (ADVOCATES).
SORT-CHECK: Test: Tier 1 and Tier 2 both empty? Loop until NO.
PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rules:**

INSPECT: Tier 1/2 for switching-cost orientation. CONFIRM YES or NO.
NO: INJECT Inertia-Advocate as Tier 1 first speaker.
VALIDATE: structural absence and incorrect affirmation are distinct FAILS axes.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED — first in Tier 1.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: and RESPONDS-TO: before endorsement.
VALIDATE: at least one CONDITION or BLOCK; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST as a Markdown table:
  | Role | Stance |
  |------|--------|
  | [Role Name] | [STANCE-TOKEN] |
  [one row per participant — no blank cells — Role column and Stance column both filled]

VALIDATE: table has named columns `Role` and `Stance`. Every participant from Phase 0 has
  exactly one row. No row has a blank Role or blank Stance cell.
  ACCEPTABLE: all rows populated with Role and STANCE-TOKEN
  FAILS: participant missing from table
  FAILS: Stance cell blank or contains prose instead of APPROVE / CONDITION / BLOCK token

PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.`
VALIDATE: commit reference and modification prohibition both present.
  FAILS (a): prohibition absent; FAILS (b): neither element; FAILS (c): line absent

PRINT: PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT rows in STANCE MANIFEST table
  by Stance cell value. Do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY rule.
VALIDATE: row counts match exactly. OUTCOME matches tally rule.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME.
WRITE: Conditions — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner and Trigger both present.

WRITE: ### ACTION ITEMS as a Markdown table:
  | Owner | Action | Deadline |
  |-------|--------|----------|
  | [role] | [specific action] | [deadline] |
  [at least two rows — no blank cells]

VALIDATE: table has named columns `Owner`, `Action`, `Deadline`. Every row has all three
  cells populated. Generic actions ("address concerns", "follow up") fail the Action cell.
  ACCEPTABLE: `| PM | Revise onboarding spec to include rollback path | 2026-03-23 |`
  FAILS: `| PM | | 2026-03-23 |` — blank Action cell
  FAILS: `| PM | Address feedback | 2026-03-23 |` — vague Action

WRITE: dissent per CONDITION/BLOCK stance. ENFORCE no-dissent form if none.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-03 — Injection-Default Framing

**Axis:** Inertia framing — Inertia-Advocate as always-present default
**Hypothesis:** Recasting the INERTIA CONTINUITY BRIDGE as a YES-gate (not a NO-gate) makes the injection the structural default. The question becomes "Is there a charter role already covering inertia?" not "Should I inject?" YES requires named qualifying evidence and an explicit charter orientation quote. Adding "YES without a qualifying participant fails" language as a motivational principle surfaces the harder failure — incorrectly silencing the inertia voice.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

Execute in two steps: (1) print the skeleton, (2) fill it.

INERTIA-ADVOCATE STRUCTURAL DEFAULT:
The Inertia-Advocate is ALWAYS present in this simulation. It is injected by default.
The only path to removing it is a YES answer to the INERTIA CONTINUITY BRIDGE gate,
supported by a named charter role whose orientation explicitly covers switching-cost
analysis or status-quo defense. YES without that qualifying evidence fails. The reason
this matters: an incorrect YES silences the inertia voice without surfacing the silence —
that is the harder failure, not a missing section header.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2. Continue until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

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

DEFAULT: Inertia-Advocate is INJECTED.

YES-GATE: Does a charter participant already cover inertia?
  Qualifying role: ___ [name the role — or NONE]
  Qualifying orientation: ___ [quote the charter orientation phrase — or N/A]
  Gate answer: ___ [YES — Inertia-Advocate MERGED into qualifying role /
                     NO — Inertia-Advocate remains INJECTED as Tier 1 first speaker]

INJECTION STATUS: ___ [INJECTED / MERGED]

VALIDATE: YES without a named qualifying role and quoted orientation phrase FAILS this gate.
  YES is the exception path, not the default. Inertia-Advocate remains INJECTED unless
  the qualifying evidence is explicit.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED]

### ___ — Tier ___

STANCE: ___
___  [prose]
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice
  prose is not permitted.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
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
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type, Agenda Item, Charter Source, Participants.
PRINT: PHASE-0-COMMIT.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A — specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

GATE-N intra-phase retry:
IF NO: INCREMENT N; new label; rewrite all four findings; loop until YES.

WRITE: ## INERTIA RECORD — one-phrase anchors.
VALIDATE: each entry has a content anchor — not a bare label, not a placeholder.

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
VALIDATE: FAILS (a) prohibition absent; FAILS (b) neither element; FAILS (c) line absent.

PRINT: PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS), Tier 2 (CONDITIONALS), Tier 3 (ADVOCATES).
SORT-CHECK: loop until Result NO.
PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rules — injection-default protocol:**

ASSUME: Inertia-Advocate is INJECTED. This is the default. Do not override it without evidence.

YES-GATE procedure:
SCAN: Phase 2 TIER SORT — does any Tier 1 or Tier 2 participant have a charter orientation
  that explicitly covers switching-cost analysis, status-quo defense, or cost-of-change?
IF YES:
  WRITE: `Qualifying role: [role name]`
  WRITE: `Qualifying orientation: "[verbatim charter orientation phrase]"`
  CONFIRM: the quoted phrase explicitly names switching cost, status-quo, or cost-of-change —
    "risk management" alone is not sufficient.
  VALIDATE: YES without both a qualifying role name AND a quoted orientation phrase FAILS.
    The reason: an unqualified YES silences the inertia voice without surfacing the silence.
    That is the harder failure — the output looks complete but the inertia perspective is absent.
  IF qualified YES: write `Gate answer: YES — Inertia-Advocate MERGED` and
    `INJECTION STATUS: MERGED`. The qualifying role carries inertia obligation in Phase 3.
IF NO (or YES not qualified):
  WRITE: `Qualifying role: NONE` and `Gate answer: NO — Inertia-Advocate remains INJECTED`
  WRITE: `INJECTION STATUS: INJECTED`
  INJECT: Inertia-Advocate as Phase 3 Tier 1 first speaker.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in their voice block.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.

VALIDATE both FAILS axes independently:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS (incorrect affirmation): YES declared without qualifying role and quoted orientation

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if INJECTED — Inertia-Advocate FIRST in Tier 1.
ENFORCE: if MERGED — qualifying role opens their voice with an inertia-oriented concern citing
  at least one INERTIA-FINDING-* label before raising their own orientation concerns.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: and RESPONDS-TO: before endorsement.
VALIDATE: at least one CONDITION or BLOCK; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST — one entry per participant: [Role Name] STANCE-TOKEN.

PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.`
VALIDATE: FAILS (a) prohibition absent; FAILS (b) neither element; FAILS (c) line absent.

PRINT: PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in ## STANCE MANIFEST.
WRITE: OUTCOME. VALIDATE counts match exactly.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME.
WRITE: Conditions — specific deliverables.
REQUIRE (not APPROVED): Owner and Trigger.
PRINT: action items as [Owner Role] — [specific action] — [deadline].
WRITE: dissent per CONDITION/BLOCK. ENFORCE no-dissent form if none.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-04 — Role-Distinctive Voices + Table Format

**Axis:** C-09 + C-10 combination
**Hypothesis:** When ORIENTATION-LENS anchoring (C-09) and Markdown table structure (C-10) are combined, each reinforces the other. The table makes STANCE MANIFEST and ACTION ITEMS mechanically complete; the ORIENTATION-LENS line makes voice content non-interchangeable. Two aspirational criteria earned simultaneously without overloading Phase 3 prose rules.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — [orientation phrase from charter]
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded, orientation phrases extracted.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2. Continue until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

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

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED]

### ___ — Tier ___

ORIENTATION-LENS: [verbatim orientation phrase from Phase 0 participant list]
STANCE: ___
___  [2-4 sentences — must follow from ORIENTATION-LENS]
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

| Role | Stance |
|------|--------|
| ___ | ___ |
[one row per participant — no blank cells]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice
  prose is not permitted.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
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

| Owner | Action | Deadline |
|-------|--------|----------|
| ___ | ___ | ___ |
[at least two rows — no blank cells]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type, Agenda Item, Charter Source.
PRINT: each participant as: [Role Name] — [orientation phrase from charter].
VALIDATE: orientation phrase is verbatim or close-paraphrase of charter field — not invented.
  The Phase 0 list is the authoritative source for Phase 3 ORIENTATION-LENS lines.
  ACCEPTABLE: `Risk Officer — identifies regulatory exposure and compliance constraints`
  FAILS: `Risk Officer — manages risk` — generic label, not charter orientation
PRINT: PHASE-0-COMMIT including orientation phrase extraction confirmation.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A through D (specific, named, non-obvious).
GATE-N retry until YES.
WRITE: ## INERTIA RECORD with content anchors.
PRINT: INERTIA INVARIANT. VALIDATE three FAILS axes.
PRINT: PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tiers. SORT-CHECK until NO. PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rules:**

INSPECT: Tier 1/2 for switching-cost orientation. CONFIRM YES or NO with evidence.
NO: INJECT Inertia-Advocate as Tier 1 first speaker with INERTIA-FINDING-* citation.
VALIDATE: structural absence and incorrect affirmation are distinct FAILS axes.

---

**PHASE 3 fill rules — ORIENTATION-LENS + TABLE MANIFEST:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED — first in Tier 1.

PRINT: `ORIENTATION-LENS: [verbatim orientation phrase from Phase 0]` as FIRST line of every
  voice block — before STANCE: and before any prose.
VALIDATE: ORIENTATION-LENS matches Phase 0 participant list.
  FAILS: phrase not declared in Phase 0; FAILS: ORIENTATION-LENS line absent

ROLE-DISTINCTIVENESS RULE:
VALIDATE: at least three voice blocks contain concerns visibly derived from their
  ORIENTATION-LENS phrase and non-transplantable to another participant.
  ACCEPTABLE: each concern is only coherent given the speaker's specific orientation phrase
  FAILS: all concerns are generic — "timeline risk", "user confusion", "technical debt" —
    interchangeable across roles regardless of orientation

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone line after ORIENTATION-LENS.
WRITE: 2-4 sentences. Prose must follow from ORIENTATION-LENS.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): specific approval condition.
REQUIRE (Tier 3): CITE: and RESPONDS-TO:.
VALIDATE: at least one CONDITION or BLOCK.

WRITE: ## STANCE MANIFEST as Markdown table:
  | Role | Stance |
  |------|--------|
  | [Role Name] | [STANCE-TOKEN] |
VALIDATE: named columns Role and Stance. Every Phase 0 participant has one row. No blank cells.
  FAILS: participant missing; FAILS: blank Stance cell; FAILS: prose in Stance cell

PRINT: STANCE INVARIANT with commit reference and modification prohibition.
PRINT: PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

COUNT rows in STANCE MANIFEST table by Stance cell value (do not re-parse Phase 3 prose).
PRINT TALLY. WRITE OUTCOME. VALIDATE. PRINT PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict, Conditions (specific), Re-entry if not APPROVED (Owner + Trigger).

WRITE: ### ACTION ITEMS as Markdown table:
  | Owner | Action | Deadline |
  |-------|--------|----------|
VALIDATE: named columns Owner, Action, Deadline. At least two rows. No blank cells.
  FAILS: vague Action; FAILS: missing deadline; FAILS: missing Owner

WRITE: dissent per CONDITION/BLOCK. ENFORCE no-dissent form if none.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-05 — Full Integration (C-09 + C-10 + C-11)

**Axis:** All three new aspirational criteria simultaneously
**Hypothesis:** When ORIENTATION-LENS anchoring (C-09), table structure (C-10), and injection-default framing (C-11) are all present in one prompt, the output should earn all three aspirational criteria plus the full essential/recommended pass set. The three mechanisms are mutually reinforcing: injection-default ensures the inertia voice is present; orientation anchoring ensures that voice — and every other — is distinctively grounded; table structure ensures the manifest and action items are mechanically complete.

```
You are running `org:committee`. Simulate a committee meeting before the real one.

Execute in two steps: (1) print the skeleton, (2) fill it.

THREE STRUCTURAL RULES — READ BEFORE ANY OTHER INSTRUCTION:

RULE 1 — INERTIA-ADVOCATE DEFAULT:
The Inertia-Advocate is ALWAYS present. It is injected by default.
The INERTIA CONTINUITY BRIDGE is a YES-gate: Inertia-Advocate is removed only when a
charter participant already covers switching-cost analysis and you can name both the role
and quote the orientation phrase that proves it. YES without that evidence fails.
Reason: an incorrect YES silences the inertia voice without surfacing the silence — that
is the harder failure.

RULE 2 — ORIENTATION-LENS ANCHORING:
Every Phase 3 voice block opens with ORIENTATION-LENS: [verbatim orientation phrase from
Phase 0]. The prose that follows must be coherent with that phrase. At least three voices
must raise concerns that are specific to their ORIENTATION-LENS and cannot be transplanted
to a different participant without violating their charter.

RULE 3 — TABLE STRUCTURE FOR MECHANICAL SECTIONS:
STANCE MANIFEST and ACTION ITEMS are both rendered as Markdown tables with named columns.
No blank cells. STANCE MANIFEST columns: Role | Stance. ACTION ITEMS columns: Owner | Action | Deadline.
Phase 4 TALLY counts rows in the STANCE MANIFEST table by Stance cell value.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — [orientation phrase from charter]
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded, orientation phrases extracted.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2. Continue until YES.]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

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

DEFAULT: Inertia-Advocate is INJECTED.

YES-GATE: Does a charter participant already cover inertia?
  Qualifying role: ___ [name — or NONE]
  Qualifying orientation: ___ [verbatim charter phrase covering switching cost — or N/A]
  Gate answer: ___ [YES — MERGED / NO — remains INJECTED]

INJECTION STATUS: ___ [INJECTED / MERGED]

VALIDATE: YES without both qualifying role name AND quoted orientation phrase FAILS.
  YES is the exception path. Inertia-Advocate remains INJECTED unless qualifying evidence
  is explicit.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED]

### ___ — Tier ___

ORIENTATION-LENS: [verbatim orientation phrase from Phase 0 participant list]
STANCE: ___
___  [2-4 sentences — must follow from ORIENTATION-LENS — concern must be non-transplantable]
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

| Role | Stance |
|------|--------|
| ___ | ___ |
[one row per participant — no blank cells]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST table by row count per Stance value;
  re-parsing Phase 3 voice prose is not permitted.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
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

| Owner | Action | Deadline |
|-------|--------|----------|
| ___ | ___ | ___ |
[at least two rows — no blank cells]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type, Agenda Item, Charter Source.
PRINT: each participant as: [Role Name] — [orientation phrase from charter].
VALIDATE: orientation phrase is verbatim or close-paraphrase of charter field — not
  invented at Phase 3. Phase 0 list is the authoritative source for ORIENTATION-LENS lines.
  ACCEPTABLE: `Finance Lead — cost governance and fiscal constraint analysis`
  FAILS: `Finance Lead — financial role` — generic summary, not orientation phrase
PRINT: PHASE-0-COMMIT with orientation phrase extraction confirmed.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A — specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

GATE-N intra-phase retry until YES. Each retry carries its sequential INVESTIGATION-ATTEMPT-N label.

WRITE: ## INERTIA RECORD — one-phrase content anchors from the passing attempt.
VALIDATE: each entry has a content anchor — not a bare label, not `[one-phrase anchor]` placeholder.

PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
VALIDATE: commit reference and modification prohibition both present.
  FAILS (a): commit-present / prohibition-absent
  FAILS (b): line present, neither element present
  FAILS (c): line absent entirely

PRINT: PHASE-1-COMMIT with bidirectionality clause — modifications to that record require
  updating this commit; modifications to this commit require updating that record.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) — scrutiny/risk/disruption orientation.
ASSIGN: Tier 2 (CONDITIONALS) — conditional approval orientation.
ASSIGN: Tier 3 (ADVOCATES) — proposal-aligned orientation.
ENFORCE: tie-break by institutional veto authority.

SORT-CHECK: Test: Tier 1 and Tier 2 both empty? Loop until NO.
PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rules — injection-default protocol:**

ASSUME: Inertia-Advocate is INJECTED. Do not override without qualifying evidence.

YES-GATE procedure:
SCAN: Phase 2 Tier 1/2 — does any participant have a charter orientation explicitly covering
  switching-cost analysis, status-quo defense, or cost-of-change?
IF YES candidate found:
  WRITE: `Qualifying role: [name]`
  WRITE: `Qualifying orientation: "[verbatim charter phrase]"`
  CONFIRM: phrase explicitly names switching cost, status-quo, or cost-of-change.
    "risk" or "governance" alone does not qualify.
  IF qualified: `Gate answer: YES — Inertia-Advocate MERGED` → `INJECTION STATUS: MERGED`
    ENFORCE: qualifying role opens their Phase 3 voice with an inertia-oriented concern
      citing at least one INERTIA-FINDING-* label before their own orientation concerns.
  IF not qualified (phrase too general): treat as NO.
IF NO (or unqualified YES):
  WRITE: `Qualifying role: NONE` → `Gate answer: NO` → `INJECTION STATUS: INJECTED`
  INJECT: Inertia-Advocate as Phase 3 Tier 1 first speaker.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in voice block.
  ENFORCE: Inertia-Advocate has a row in ## STANCE MANIFEST table.

VALIDATE both FAILS axes independently:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS (incorrect affirmation): YES declared without qualifying role name AND quoted orientation

---

**PHASE 3 fill rules — ORIENTATION-LENS + TABLE MANIFEST + INJECTION-DEFAULT:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if INJECTED — Inertia-Advocate FIRST in Tier 1.
ENFORCE: if MERGED — qualifying role leads voice with inertia concern citing INERTIA-FINDING-*.

PRINT: `ORIENTATION-LENS: [verbatim orientation phrase from Phase 0]` as FIRST line of every
  voice block — before STANCE: and before prose.
VALIDATE: phrase matches Phase 0 list. FAILS: phrase absent; FAILS: phrase not in Phase 0.

ROLE-DISTINCTIVENESS RULE:
After writing all Phase 3 voices, verify:
  PASS: at least 3 voices contain a concern that (a) cites or implies their ORIENTATION-LENS
    phrase and (b) would be incoherent in a different participant's voice.
  FAIL: voices raise generic concerns (timeline, user confusion, technical risk) with no
    visible connection to their orientation phrase — interchangeable across participants.
  IF FAIL: rewrite the failing voices before proceeding to STANCE MANIFEST.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line after ORIENTATION-LENS.
WRITE: 2-4 sentences of orientation-coherent prose per participant.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): specific approval condition — not "address concerns."
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label] and RESPONDS-TO: "[named concern]" before endorsement.
VALIDATE: at least one CONDITION or BLOCK in Phase 3; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST as Markdown table:
  | Role | Stance |
  |------|--------|
  | [Role Name] | [STANCE-TOKEN] |
  [one row per participant from Phase 0 — Inertia-Advocate if INJECTED]
VALIDATE: named columns Role and Stance. All participants present. No blank cells.
  FAILS: participant row missing; FAILS: blank cell; FAILS: prose instead of token

PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.`
VALIDATE: commit reference and modification prohibition both present.
  FAILS (a): prohibition absent; FAILS (b): neither element; FAILS (c): line absent

PRINT: PHASE-3-COMMIT with bidirectionality clause — modifications to that manifest require
  updating this commit; modifications to this commit require updating that manifest.
COUPLING INTEGRITY SYMMETRY: PHASE-3-COMMIT bidirectionality VALIDATE is structurally
  identical to PHASE-1-COMMIT bidirectionality VALIDATE.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

COUNT rows in ## STANCE MANIFEST table by Stance cell value.
Do not re-parse Phase 3 voice prose.
PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK`
WRITE: OUTCOME — all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS;
  any BLOCK → BLOCKED or DEFERRED.
VALIDATE: row counts match table exactly. OUTCOME matches tally rule.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval — specific deliverables naming artifacts, recipients,
  and triggering authorities. "Address concerns" fails.
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) and Trigger (named artifact
  + recipient + authority who unlocks next step).
VALIDATE: both Owner and Trigger present when verdict not APPROVED.

WRITE: ### ACTION ITEMS as Markdown table:
  | Owner | Action | Deadline |
  |-------|--------|----------|
  [at least two rows — no blank cells]
VALIDATE: Owner is a named role (not "team"). Action is specific (not "address feedback",
  not "follow up"). Deadline is a concrete date or milestone.
  ACCEPTABLE: `| PM | Publish revised spec with rollback procedure to arch-board@signal | 2026-03-30 |`
  FAILS: `| PM | Address feedback | TBD |` — vague action, vague deadline

WRITE: dissent per CONDITION/BLOCK stance holder from ## STANCE MANIFEST:
  Each dissent entry: Role — specific objection citing INERTIA-FINDING-* label — resolution
  path — named authority who resolves — concrete trigger that closes the dissent.
ENFORCE: if no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## Scoring Predictions vs R2 Rubric

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | Predicted Score |
|-----------|------|------|------|------|------|------|------|------|------|------|------|----------------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | MISS | MISS | ~90 |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | MISS | PASS | MISS | ~90 |
| V-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | MISS | MISS | PASS | ~90 |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | MISS | ~93 |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | ~97 |

**Key uncertainty:** C-09 PASS requires the model to actually produce non-interchangeable voices, not just include the ORIENTATION-LENS line. V-01/V-04/V-05 create structural pressure for distinctiveness; whether the model follows through is the open question for quest-score.
