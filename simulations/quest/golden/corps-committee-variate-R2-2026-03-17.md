---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 2
rubric_version: 2
---

# corps-committee — Prompt Variations R2

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Lifecycle emphasis | Adding a COMMITTEE-TYPE GATE as a Phase 0 extension — committing type-specific framing before Phase 1 begins — closes C-01/C-07 by making type-specific output a first-class structural commitment rather than a Phase 5 afterthought. |
| V-02 | Output format | Extracting charter constraints into a CHARTER CONSTRAINTS table in Phase 0 and requiring a CHARTER FIDELITY TRACE table in Phase 5 closes C-10 through structural completeness rather than passive honor. |
| V-03 | Phrasing register | Stating committee-type requirements as direct conversational imperatives ("for arch-board, you must…") produces better type-specific framing than formal gate syntax because the model receives clear action instructions without parsing conditional logic. |
| V-04 | Lifecycle emphasis + Inertia framing | Combining the committee-type gate with injection-as-default (C-11) and provisional Phase 0 annotation (C-12) in a unified Phase 0 extension closes C-01/C-07/C-11/C-12 while the combined structural weight makes all four commitments harder to skip. |
| V-05 | Full integration | Combining committee-type requirements, charter fidelity, injection-as-default, and provisional annotation into one coherent prompt achieves Gold by closing C-01, C-07, C-10, C-11, and C-12 without increasing total output length. |

---

## V-01 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis
**Hypothesis:** Adding a COMMITTEE-TYPE GATE as a named Phase 0 extension — requiring type-specific framing to be committed before inertia analysis begins — closes C-01/C-07 by making the type-specific output requirement a structural commitment rather than a Phase 5 afterthought.

```
You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins — verified for both structural presence and affirmation correctness.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

## COMMITTEE-TYPE GATE

Type: ___
Required framing: ___
Required output: ___

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. Type framing committed: ___, Required output: ___.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional.
 Continue INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

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
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
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

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]
  [NO → Inertia-Advocate INJECTED — Tier: 1 (speaks first) — Orientation: switching-cost
   investigation from ## INERTIA RECORD — CITE obligation: at least one INERTIA-FINDING-*
   label in Phase 3 voice]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by INERTIA CONTINUITY BRIDGE]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
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

### TYPE-SPECIFIC OUTPUT

[ROB]        Readiness Verdict: ___
[Shiproom]   Go/No-Go: ___
[Arch-board] ADR Summary:
  Decision: ___
  Rejected Alternative 1: ___ — Rationale: ___
  Rejected Alternative 2: ___ — Rationale: ___

[Populate only the section matching the declared committee type. Omit the others.]

### ACTION ITEMS

___ — ___ — ___
[one row per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS, and TYPE-SPECIFIC
  OUTPUT written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed.
  Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type — ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified` — type not named; fails C-01
  FAILS: `Committee Type: product review` — non-standard label; use recognized types
PRINT: Agenda Item, Charter Source, Participants (one line each, format: Role — orientation).

COMMITTEE-TYPE GATE fill rules:
IDENTIFY: the declared committee type and apply the corresponding framing requirement:
  ROB:        Required framing — feature/metric readiness evidence in discussion.
              Required output  — explicit readiness verdict (ready / not ready / conditional).
  Shiproom:   Required framing — risk register or blocking issues in discussion.
              Required output  — explicit go/no-go decision.
  Arch-board: Required framing — named architectural trade-offs (at least two alternatives).
              Required output  — ADR summary with rejected alternatives and rationale.

PRINT: ## COMMITTEE-TYPE GATE with Type, Required framing, Required output populated.
ENFORCE: both Required framing and Required output fields committed in PHASE-0-COMMIT.
VALIDATE:
  ACCEPTABLE: `Type framing committed: feature/metric readiness evidence, Required output:
    readiness verdict`
  FAILS: framing field absent from PHASE-0-COMMIT — C-01 fail (type declared but framing
    not committed; structural commitment missing)

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label as the first element on the line.
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow — ...`
  FAILS: `(a) legacy-approval-workflow` — parenthesized letter, not the token
  FAILS: `Finding A: ...` — abbreviated label; full token required

GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; GATE-N+1; repeat.
ENFORCE: each retry carries its sequential INVESTIGATION-ATTEMPT-N label.
ENFORCE: loop runs within Phase 1; Phase 2 reached unconditionally after any YES.

WRITE: ## INERTIA RECORD — one-phrase anchors from the passing attempt's findings.
VALIDATE: each entry carries a content anchor — not a bare label, not a placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` — bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` — unfilled placeholder

SEALING CONTRACT INTEGRITY — INERTIA INVARIANT:
PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
ENFORCE: ## INERTIA RECORD is independently addressable; appears before PHASE-1-COMMIT.
PRINT: PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) — charter roles whose orientation maps to feasibility scrutiny,
  risk, or disruption of existing systems; speak first.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding conditional approval; speak second.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with proposal goals; speak last.
ENFORCE: tie-break by institutional veto authority within a tier.

SORT-CHECK:
PRINT: `Test: Tier 1 and Tier 2 both empty?` and `Result: YES / NO`.
IF YES: name mis-sorted role, target tier, reason specific to this agenda item; reprint
  corrected TIER SORT; reprint SORT-CHECK; loop until NO.

PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 → Phase 3):**

INSPECT: Phase 2 TIER SORT — identify any Tier 1 or Tier 2 participant whose charter
  orientation maps to switching-cost investigation, status-quo defense, or cost-of-change analysis.
CONFIRM: `Inertia owner in tier sort: YES` if such a participant exists; proceed to Phase 3.
CONFIRM: `Inertia owner in tier sort: NO` if none exists:
  INJECT: Inertia-Advocate as Phase 3 Tier 1 participant — speaks first among all challengers.
  ORIENTATION: investigates switching costs from ## INERTIA RECORD; voices Phase 1 findings
    as Phase 3 objections.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in their voice block.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED — Inertia-Advocate voice FIRST in Tier 1.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before any prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label] and RESPONDS-TO: [named concern] before endorsement.
VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.
WRITE: ## STANCE MANIFEST; STANCE INVARIANT; PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in ## STANCE MANIFEST;
  do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY; all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH
  CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
VALIDATE: counts match ## STANCE MANIFEST exactly.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster, not a team) and Trigger
  (named artifact + recipient + authority).

WRITE: TYPE-SPECIFIC OUTPUT section — match committee type declared in Phase 0:
  ROB → PRINT: `Readiness Verdict: [ready / not ready / conditional]`
    ENFORCE: cite at least one specific feature or metric named in Phase 3 discussion.
    VALIDATE:
      ACCEPTABLE: `Readiness Verdict: conditional — API latency SLA at 180ms vs 100ms target`
      FAILS: `Readiness Verdict: not ready` with no metric cited — C-07 partial
      FAILS: section absent for ROB — C-01 fail
  Shiproom → PRINT: `Go/No-Go: [GO / NO-GO / CONDITIONAL GO]`
    ENFORCE: cite the specific blocking issue or risk register item.
    VALIDATE:
      ACCEPTABLE: `Go/No-Go: NO-GO — rollback path not validated for 3-region deployment`
      FAILS: `Go/No-Go: NO-GO` with no blocking issue cited — C-07 partial
  Arch-board → PRINT: ADR Summary:
    ENFORCE: Decision named; Rejected Alternative 1 + Rationale; Rejected Alternative 2 + Rationale.
    VALIDATE:
      ACCEPTABLE: two named alternatives, each with a specific rejection rationale
      FAILS: one or zero alternatives named — C-01 fail
      FAILS: `Rejected because of concerns` — no specific rationale — C-07 partial

PRINT: action items as [Owner Role] — [specific action] — [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority.
ENFORCE: if no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-02 — Output Format

**Axis:** Output format
**Hypothesis:** Extracting charter constraints into a CHARTER CONSTRAINTS table in Phase 0 and requiring a CHARTER FIDELITY TRACE table in Phase 5 closes C-10 through structural completeness — four named rows that cannot be blank — rather than relying on the model to passively honor constraints embedded in charter prose.

```
You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins — verified for both structural presence and affirmation correctness.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

## CHARTER CONSTRAINTS

| Constraint | Value |
|------------|-------|
| Quorum     | ___   |
| Scope      | ___   |
| Veto       | ___   |
| Escalation | ___   |

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. Charter constraints declared: quorum ___, scope ___,
  veto ___, escalation ___.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional.
 Continue INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

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
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
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

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]
  [NO → Inertia-Advocate INJECTED — Tier: 1 (speaks first) — Orientation: switching-cost
   investigation from ## INERTIA RECORD — CITE obligation: at least one INERTIA-FINDING-*
   label in Phase 3 voice]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by INERTIA CONTINUITY BRIDGE]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
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

### CHARTER FIDELITY TRACE

| Constraint | Honored | Evidence |
|------------|---------|----------|
| Quorum     | ___     | ___      |
| Scope      | ___     | ___      |
| Veto       | ___     | ___      |
| Escalation | ___     | ___      |

### ACTION ITEMS

___ — ___ — ___
[one row per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS, and CHARTER
  FIDELITY TRACE written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed.
  Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type — ROB, shiproom, arch-board, or user-specified type.
PRINT: Agenda Item, Charter Source, Participants (one line each, format: Role — orientation).

CHARTER CONSTRAINTS fill rules:
EXTRACT from charter (or signal defaults if no charter):
  Quorum: minimum attendance fraction required to reach a binding decision.
  Scope: what this committee is authorized to decide vs. what must be escalated.
  Veto: which roles hold unilateral veto authority and the conditions under which it applies.
  Escalation: the named path (authority, artifact, trigger) when the committee cannot decide.
PRINT: ## CHARTER CONSTRAINTS table with all four rows populated.
ENFORCE: if charter has no explicit value for a constraint — use `[Signal default: ___]`
  with a reasonable assumption; a blank cell is not acceptable.
ENFORCE: PHASE-0-COMMIT names all four constraint values in summary form.
VALIDATE:
  ACCEPTABLE: `quorum: 4 of 5 required, scope: feature-level decisions only, veto:
    Security Lead on compliance risk, escalation: VP Engineering via ADR`
  FAILS: any row blank — C-10 fail
  FAILS: `Quorum: [quorum]` — unfilled placeholder — C-10 fail
  FAILS: PHASE-0-COMMIT omits constraint summary — C-10 partial

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label as the first element on the line.
GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; GATE-N+1; repeat.
ENFORCE: each retry carries its sequential INVESTIGATION-ATTEMPT-N label.
ENFORCE: loop runs within Phase 1; Phase 2 reached unconditionally after any YES.

WRITE: ## INERTIA RECORD — one-phrase anchors from the passing attempt's findings.
SEALING CONTRACT INTEGRITY — INERTIA INVARIANT:
PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
PRINT: PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS), Tier 2 (CONDITIONALS), Tier 3 (ADVOCATES) by charter orientation.
ENFORCE: tie-break by institutional veto authority within a tier.
SORT-CHECK: Tier 1 and Tier 2 both empty? If YES — reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 → Phase 3):**

INSPECT: Phase 2 TIER SORT — identify any Tier 1 or Tier 2 participant whose charter
  orientation maps to switching-cost investigation, status-quo defense, or cost-of-change analysis.
CONFIRM: `Inertia owner in tier sort: YES` if such a participant exists; proceed to Phase 3.
CONFIRM: `Inertia owner in tier sort: NO` if none exists:
  INJECT: Inertia-Advocate as Phase 3 Tier 1 participant — speaks first among all challengers.
  ORIENTATION: investigates switching costs from ## INERTIA RECORD.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.

VALIDATE — two independent FAILS axes:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section.
  FAILS (incorrect affirmation): YES declared when no Tier 1/Tier 2 participant maps to
    inertia analysis — inertia perspective silently absent without injection.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order. Injected Inertia-Advocate FIRST in Tier 1.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before any prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: and RESPONDS-TO: before endorsement.
VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.
WRITE: ## STANCE MANIFEST; STANCE INVARIANT; PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in ## STANCE MANIFEST.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role) and Trigger (named artifact + recipient + authority).

WRITE: CHARTER FIDELITY TRACE table — for each constraint declared in Phase 0:
  Quorum row: Honored YES/NO — cite evidence (attendance count, quorum met or missed and why).
  Scope row: Honored YES/NO — cite evidence (decision falls within or outside declared scope).
  Veto row: Honored YES/NO — cite evidence (veto invoked / not applicable / veto-eligible stance).
  Escalation row: Honored YES/NO — cite evidence (escalation triggered or path noted if not reached).
VALIDATE:
  ACCEPTABLE: `Quorum | YES | 4 of 4 required roles present`
  FAILS: row absent — C-10 fail
  FAILS: `Honored: YES` with no evidence — C-10 partial (assertion without basis)
  FAILS: Escalation row shows YES without escalation triggered when verdict is BLOCKED — C-10 fail
  REQUIRE: at least two rows must cite charter-specific constraint language, not generic summary.

PRINT: action items as [Owner Role] — [specific action] — [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK — objection citing INERTIA-FINDING-* label, resolution path,
  named authority. If no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-03 — Phrasing Register

**Axis:** Phrasing register (conversational imperative)
**Hypothesis:** Stating committee-type requirements as direct "you must" imperatives per type — rather than formal gate syntax — produces better type-specific framing because the model receives unambiguous action instructions without needing to parse conditional gate logic.

```
You are running `org:committee`. Your job: simulate a committee meeting before the real one.
Write it so the product team can walk in knowing exactly where the friction will be.

The Inertia-Advocate shows up to every meeting. If nobody on the charter roster covers
switching-cost analysis, inject one — they speak first among all challengers.

---

BEFORE YOU START: note the committee type and apply the right framing.

For ROB — your job is to assess readiness. The discussion must reference at least one
  specific feature or metric. The Decisions section must end with a clear readiness verdict:
  ready, not ready, or conditional. If there is no metric, you have not done a ROB.

For Shiproom — your job is to decide whether to ship. The discussion must name any blocking
  issues. The Decisions section must end with GO, NO-GO, or CONDITIONAL GO. Name the specific
  issue that could block it. If there is no blocking issue named, the go/no-go is incomplete.

For Arch-board — your job is to pick an architecture and record why the alternatives lost.
  The discussion must lay out at least two rejected alternatives. The Decisions section must
  include an ADR summary: decision made, rejected alternatives named, rationale for each
  rejection. If there are fewer than two rejected alternatives, the ADR is incomplete.

---

Execute in two steps: (1) print the skeleton, (2) fill it.

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional.
 Continue INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

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
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
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

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

Inertia owner in tier sort: ___ [YES — charter role maps to inertia perspective /
                                  NO — Inertia-Advocate INJECTED]
  [NO → Inertia-Advocate INJECTED — Tier: 1 (speaks first) — Orientation: switching-cost
   investigation from ## INERTIA RECORD — CITE obligation: at least one INERTIA-FINDING-*
   label in Phase 3 voice]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by INERTIA CONTINUITY BRIDGE]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
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

### COMMITTEE OUTPUT

[Fill only the section that matches your committee type. Leave the others blank.]

ROB — Readiness Verdict: ___

Shiproom — Go/No-Go: ___

Arch-board — ADR Summary:
  Decision: ___
  Rejected Alternative 1: ___ — Rationale: ___
  Rejected Alternative 2: ___ — Rationale: ___

### ACTION ITEMS

___ — ___ — ___
[one row per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS, and COMMITTEE
  OUTPUT written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed.
  Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

Load the charter from `.craft/roles/` matching the committee type. If there is no charter,
note `Signal defaults — no charter found` and fall back to PM, Architect, and Inertia-Advocate.
Name the committee type using the standard labels: ROB, shiproom, or arch-board.
List each participant with their orientation — one line per participant.
Print the PHASE-0-COMMIT line.

---

**PHASE 1 fill rules:**

Label your first pass INVESTIGATION-ATTEMPT-1.

Find four inertia findings:
- INERTIA-FINDING-A: name the specific workflow or tool this proposal would displace.
- INERTIA-FINDING-B: name the specific integration surface at risk — the system, API, or contract.
- INERTIA-FINDING-C: name the team whose working habits would change and describe the exact habit.
- INERTIA-FINDING-D: name a switching cost the proposal author did not factor in.

For FINDING-D: ask yourself whether a sharp analyst reviewing the proposal would have
flagged this already. If yes, that is not FINDING-D — find something they would miss.

Answer GATE-1: YES or NO.
If NO: run INVESTIGATION-ATTEMPT-2 with all four findings rewritten. Keep going until YES.

Once you have a YES, write the INERTIA RECORD (one-phrase anchor per finding).
Write the INERTIA INVARIANT line.
Print PHASE-1-COMMIT with the bidirectionality clause.

---

**PHASE 2 fill rules:**

Sort participants into tiers based on their charter orientation:
- Tier 1: roles oriented toward scrutiny, risk, or disruption to existing systems.
- Tier 2: roles whose approval depends on specific conditions being met.
- Tier 3: roles aligned with the proposal goals.

Tie-break: by institutional veto authority within a tier.

Run the SORT-CHECK. If Tier 1 and Tier 2 are both empty, that is wrong — reassign at least
one role and re-sort. Show your work. Loop until SORT-CHECK Result is NO.

Print PHASE-2-COMMIT.

---

**INERTIA CONTINUITY BRIDGE fill rules:**

Look at your Tier 1 and Tier 2 participants. Does any of them cover switching-cost analysis
by charter — investigating costs, defending the status quo, or quantifying cost of change?

If yes: state `Inertia owner in tier sort: YES` and name the role. Move to Phase 3.
If no: state `Inertia owner in tier sort: NO` and inject the Inertia-Advocate.
  The Inertia-Advocate speaks first in Tier 1. Their voice draws from the INERTIA RECORD
  and must cite at least one INERTIA-FINDING-* label. They must appear in the STANCE MANIFEST.

---

**PHASE 3 fill rules:**

Run voices in Tier 1 → Tier 2 → Tier 3 order. Injected Inertia-Advocate goes first in Tier 1.

Each participant:
- Print STANCE: BLOCK, CONDITION, or APPROVE on its own line before any prose.
- Write 2-4 sentences from their perspective and charter role.
- Tier 1 voices: cite a named INERTIA-FINDING-* label.
- Tier 2 voices: name the specific condition — "address concerns" is not a condition.
- Tier 3 voices: CITE: a finding label and RESPONDS-TO: a named concern before endorsing.

Make sure at least one voice is BLOCK or CONDITION. If everyone approves, go back to Phase 2.

Write the STANCE MANIFEST (one entry per participant: [Role Name] STANCE-TOKEN).
Write the STANCE INVARIANT line.
Print PHASE-3-COMMIT with the bidirectionality clause.

---

**PHASE 4 fill rules:**

Count the tokens in the STANCE MANIFEST. Print:
  TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK

Derive OUTCOME:
- All APPROVE → APPROVED
- Any CONDITION, no BLOCK → APPROVED WITH CONDITIONS
- Any BLOCK → BLOCKED or DEFERRED

Print PHASE-4-COMMIT.

---

**PHASE 5 fill rules:**

Write Verdict — match the OUTCOME word-for-word.
Write Conditions for full approval — specific deliverables only, not "address the feedback."
If not APPROVED: name the Owner (a role from the roster, not a team) and the Trigger
  (named artifact + recipient + authority who must sign off).

Write the COMMITTEE OUTPUT section — fill only the section that matches your committee type:

For ROB: write `Readiness Verdict: [ready / not ready / conditional]`.
  You must name at least one specific feature or metric from the Phase 3 discussion.
  "Not ready" without a metric is incomplete.

For Shiproom: write `Go/No-Go: [GO / NO-GO / CONDITIONAL GO]`.
  You must name the specific blocking issue or risk that drove the decision.
  "NO-GO" without a blocking issue is incomplete.

For Arch-board: write an ADR Summary:
  - Decision: what was chosen.
  - Rejected Alternative 1: name it, then one sentence on why it lost.
  - Rejected Alternative 2: name it, then one sentence on why it lost.
  You need at least two rejected alternatives. One is not enough.

Write action items: Owner Role — specific action — deadline. All three fields required.
Write dissent for every CONDITION or BLOCK voice: cite the INERTIA-FINDING-* label, name
  the resolution path and the authority. If no dissent: `No dissent — [reason]`.
Print PHASE-5-COMMIT.
```

---

## V-04 — Lifecycle Emphasis + Inertia Framing

**Axis:** Lifecycle emphasis + Inertia framing
**Hypothesis:** Combining the committee-type gate (closes C-01/C-07) with injection-as-default cognitive burden-flip (C-11) and provisional Phase 0 annotation (C-12) in a unified Phase 0 extension makes all four commitments structurally simultaneous — the type framing, the injection proof, and the forward-reference annotation are all locked at PHASE-0-COMMIT before Phase 1 begins.

```
You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

INJECTION IS THE DEFAULT. The Inertia-Advocate participates in every org:committee
simulation unless a charter participant can be proven to cover switching-cost analysis.
The burden of proof is: cite the charter role and the specific orientation clause.
A YES without that citation is an incorrect affirmation — treat as NO and inject.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___  [or: ___ — ___ [PROVISIONAL — inertia coverage unconfirmed; confirmed or
                               replaced by INERTIA CONTINUITY BRIDGE in Phase 2]]
  [repeat per participant]

## COMMITTEE-TYPE GATE

Type: ___
Required framing: ___
Required output: ___

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. Type framing committed: ___, Required output: ___.
  Injection default active — Inertia-Advocate is assumed present until bridge proves otherwise.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional.
 Continue INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

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
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
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

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

INJECTION-PROOF:
  Candidate charter role: ___
  Orientation clause: ___
  Covers switching-cost analysis: ___ [YES — injection waived / NO — INJECT]

Inertia owner in tier sort: ___ [YES — proven by citation above /
                                  NO — Inertia-Advocate INJECTED]
  [NO → Inertia-Advocate INJECTED — Tier: 1 (speaks first) — Orientation: switching-cost
   investigation from ## INERTIA RECORD — CITE obligation: at least one INERTIA-FINDING-*
   label in Phase 3 voice]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by INERTIA CONTINUITY BRIDGE]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
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

### TYPE-SPECIFIC OUTPUT

[ROB]        Readiness Verdict: ___
[Shiproom]   Go/No-Go: ___
[Arch-board] ADR Summary:
  Decision: ___
  Rejected Alternative 1: ___ — Rationale: ___
  Rejected Alternative 2: ___ — Rationale: ___

[Populate only the section matching the declared committee type. Omit the others.]

### ACTION ITEMS

___ — ___ — ___
[one row per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS, and TYPE-SPECIFIC
  OUTPUT written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed.
  Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type — ROB, shiproom, arch-board, or user-specified type.
PRINT: Agenda Item, Charter Source, Participants.

PROVISIONAL ANNOTATION fill rule:
INSPECT: each participant for potential inertia coverage.
IF: inertia coverage is unresolved (charter orientation is ambiguous or absent):
  ANNOTATE: the participant line with `[PROVISIONAL — inertia coverage unconfirmed;
    confirmed or replaced by INERTIA CONTINUITY BRIDGE in Phase 2]`
IF: inertia coverage is clearly absent across all participants:
  ANNOTATE: the last participant line OR add a standalone line:
    `[Note: Inertia-Advocate is a candidate participant — confirmed or replaced by bridge in Phase 2]`
ENFORCE: at least one PROVISIONAL annotation or bridge candidate note in Phase 0 when inertia
  coverage status is unresolved at charter-load time.

COMMITTEE-TYPE GATE fill rules:
IDENTIFY: the declared committee type and apply the corresponding framing:
  ROB:        Required framing — feature/metric readiness evidence.
              Required output  — readiness verdict (ready / not ready / conditional).
  Shiproom:   Required framing — risk register or blocking issues.
              Required output  — explicit go/no-go decision.
  Arch-board: Required framing — named architectural trade-offs (at least two alternatives).
              Required output  — ADR summary with rejected alternatives and rationale.
PRINT: ## COMMITTEE-TYPE GATE with Type, Required framing, Required output populated.
ENFORCE: both fields committed in PHASE-0-COMMIT.

PRINT: PHASE-0-COMMIT — include `Injection default active — Inertia-Advocate is assumed
  present until bridge proves otherwise.`
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label as the first element on the line.
GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; GATE-N+1; repeat.
WRITE: ## INERTIA RECORD — one-phrase anchors.
PRINT: INERTIA INVARIANT; PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS), Tier 2 (CONDITIONALS), Tier 3 (ADVOCATES) by charter orientation.
ENFORCE: tie-break by institutional veto authority within a tier.
SORT-CHECK: both tiers empty? If YES — reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule — INJECTION IS DEFAULT:**

RULE 1: Injection is the default state. The bridge begins with Inertia-Advocate INJECTED.
RULE 2: To waive injection and answer YES, you must cite:
  (a) the specific charter role name, AND
  (b) the specific orientation clause in that role's charter that covers switching-cost analysis.
  Claiming YES without both citations is an incorrect affirmation — treat as NO and inject.

PRINT: INJECTION-PROOF block:
  Candidate charter role: [role name or "none"]
  Orientation clause: [quoted or paraphrased charter text, or "none found"]
  Covers switching-cost analysis: YES (if both citations present) / NO (inject)

CONFIRM: `Inertia owner in tier sort: YES — proven by citation above` or
         `Inertia owner in tier sort: NO — Inertia-Advocate INJECTED`

IF INJECTED:
  ENFORCE: Inertia-Advocate is Tier 1, speaks first.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.
  RESOLVE: any PROVISIONAL annotation from Phase 0 — print `[PROVISIONAL resolved:
    Inertia-Advocate injected as Tier 1]` adjacent to the annotated participant or in bridge section.

IF NOT INJECTED (YES proved):
  RESOLVE: PROVISIONAL annotation — print `[PROVISIONAL resolved: [role name] confirmed
    as inertia owner via [orientation clause]]`.

VALIDATE — two independent FAILS axes:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section.
  FAILS (incorrect affirmation): YES declared without both citation elements present.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order. Injected Inertia-Advocate FIRST in Tier 1.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone line before prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label.
REQUIRE (Tier 2): name the specific approval condition.
REQUIRE (Tier 3): CITE: and RESPONDS-TO: before endorsement.
VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared.
WRITE: ## STANCE MANIFEST; STANCE INVARIANT; PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` from ## STANCE MANIFEST token count.
WRITE: OUTCOME. PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME. Conditions for full approval (specific deliverables).
REQUIRE (not APPROVED): Owner (named role) and Trigger (artifact + recipient + authority).

WRITE: TYPE-SPECIFIC OUTPUT — match committee type from Phase 0:
  ROB → `Readiness Verdict: [ready / not ready / conditional]` — cite at least one named metric.
  Shiproom → `Go/No-Go: [GO / NO-GO / CONDITIONAL GO]` — cite the specific blocking issue.
  Arch-board → ADR Summary: Decision; Rejected Alternative 1 + Rationale; Rejected Alternative
    2 + Rationale; minimum two rejected alternatives required.
VALIDATE: TYPE-SPECIFIC OUTPUT present, matches type, and contains type-specific evidence.
  FAILS: section absent — C-01 fail
  FAILS: section present but no evidence (no metric / no blocking issue / no alternatives) — C-07 partial

PRINT: action items as [Owner Role] — [specific action] — [deadline].
WRITE: dissent per CONDITION/BLOCK citing INERTIA-FINDING-* label. If none — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-05 — Full Integration

**Axis:** Full integration (committee-type gate + charter fidelity + injection-as-default + provisional annotation)
**Hypothesis:** Integrating all four R2 axes — COMMITTEE-TYPE GATE (C-01/C-07), CHARTER CONSTRAINTS table (C-10), injection-as-default with INJECTION-PROOF (C-11), and provisional Phase 0 annotation (C-12) — into one coherent prompt achieves Gold threshold by closing every systematic R1 gap without increasing structural overhead relative to individual fixes.

```
You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

INJECTION IS THE DEFAULT. The Inertia-Advocate participates in every org:committee
simulation unless a charter participant can be proven to cover switching-cost analysis.
Proof requires: (a) the charter role name AND (b) the specific orientation clause.
A YES without both citations is an incorrect affirmation — treat as NO and inject.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content.

=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___  [or: ___ — ___ [PROVISIONAL — inertia coverage unconfirmed; confirmed or
                               replaced by INERTIA CONTINUITY BRIDGE in Phase 2]]
  [repeat per participant]

## COMMITTEE-TYPE GATE

Type: ___
Required framing: ___
Required output: ___

## CHARTER CONSTRAINTS

| Constraint | Value |
|------------|-------|
| Quorum     | ___   |
| Scope      | ___   |
| Veto       | ___   |
| Escalation | ___   |

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___,
  Participants: ___ roles loaded. Type framing committed: ___, Required output: ___.
  Charter constraints declared: quorum ___, scope ___, veto ___, escalation ___.
  Injection default active — Inertia-Advocate is assumed present until bridge proves otherwise.
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional.
 Continue INVESTIGATION-ATTEMPT-N / GATE-N until YES.]

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
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
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

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## INERTIA CONTINUITY BRIDGE

INJECTION-PROOF:
  Candidate charter role: ___
  Orientation clause: ___
  Covers switching-cost analysis: ___ [YES — injection waived / NO — INJECT]

Inertia owner in tier sort: ___ [YES — proven by citation above /
                                  NO — Inertia-Advocate INJECTED]
  [NO → Inertia-Advocate INJECTED — Tier: 1 (speaks first) — Orientation: switching-cost
   investigation from ## INERTIA RECORD — CITE obligation: at least one INERTIA-FINDING-*
   label in Phase 3 voice]
  [PROVISIONAL resolved: ___]

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]
[Inertia-Advocate FIRST in Tier 1 if INJECTED by INERTIA CONTINUITY BRIDGE]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

## STANCE MANIFEST

  [___] ___
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

### TYPE-SPECIFIC OUTPUT

[ROB]        Readiness Verdict: ___
[Shiproom]   Go/No-Go: ___
[Arch-board] ADR Summary:
  Decision: ___
  Rejected Alternative 1: ___ — Rationale: ___
  Rejected Alternative 2: ___ — Rationale: ___

[Populate only the section matching the declared committee type. Omit the others.]

### CHARTER FIDELITY TRACE

| Constraint | Honored | Evidence |
|------------|---------|----------|
| Quorum     | ___     | ___      |
| Scope      | ___     | ___      |
| Veto       | ___     | ___      |
| Escalation | ___     | ___      |

### ACTION ITEMS

___ — ___ — ___
[one row per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path
 — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS, TYPE-SPECIFIC
  OUTPUT, and CHARTER FIDELITY TRACE written; Owner and Trigger present if verdict not
  APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`; fallback
  participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type — ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly.
  ACCEPTABLE: `Committee Type: ROB`
  FAILS: `Committee Type: unspecified` — C-01 fail
  FAILS: `Committee Type: product review` — non-standard label; use recognized types
PRINT: Agenda Item, Charter Source, Participants.

PROVISIONAL ANNOTATION fill rule:
INSPECT: each participant for potential inertia coverage.
IF: inertia coverage is unresolved or absent — annotate affected participant(s) with:
  `[PROVISIONAL — inertia coverage unconfirmed; confirmed or replaced by INERTIA
   CONTINUITY BRIDGE in Phase 2]`
ENFORCE: annotation present whenever any participant's inertia coverage is uncertain at Phase 0.

COMMITTEE-TYPE GATE fill rules:
IDENTIFY: the declared committee type:
  ROB:        Required framing — feature/metric readiness evidence.
              Required output  — readiness verdict (ready / not ready / conditional).
  Shiproom:   Required framing — risk register or blocking issues.
              Required output  — explicit go/no-go decision.
  Arch-board: Required framing — named architectural trade-offs (at least two alternatives).
              Required output  — ADR summary with rejected alternatives and rationale.
PRINT: ## COMMITTEE-TYPE GATE with all three fields populated.
ENFORCE: Required framing and Required output committed in PHASE-0-COMMIT.

CHARTER CONSTRAINTS fill rules:
EXTRACT from charter (or signal defaults):
  Quorum: minimum attendance fraction for binding decisions.
  Scope: authorized decision domain vs. escalation boundary.
  Veto: roles with unilateral veto and triggering conditions.
  Escalation: named path (authority + artifact + trigger) when committee cannot decide.
PRINT: ## CHARTER CONSTRAINTS table — all four rows populated; no blank cells.
ENFORCE: PHASE-0-COMMIT names all four constraint values.
VALIDATE:
  ACCEPTABLE: all four rows populated with specific values
  FAILS: any row blank or unfilled placeholder — C-10 fail
  FAILS: PHASE-0-COMMIT missing constraint summary — C-10 partial

PRINT: PHASE-0-COMMIT including type framing, constraint summary, and injection default notice.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.
WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label.
GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings; GATE-N+1; repeat.
ENFORCE: each retry carries its sequential INVESTIGATION-ATTEMPT-N label.

WRITE: ## INERTIA RECORD — one-phrase anchors from the passing attempt's findings.
PRINT: INERTIA INVARIANT: `sealed at PHASE-1-COMMIT — findings may not be added, removed,
  or modified without reopening Phase 1.`
PRINT: PHASE-1-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS), Tier 2 (CONDITIONALS), Tier 3 (ADVOCATES) by charter orientation.
ENFORCE: tie-break by institutional veto authority within a tier.
SORT-CHECK: both tiers empty? If YES — reassign, reprint, loop until NO.
PRINT: PHASE-2-COMMIT.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule — INJECTION IS DEFAULT:**

RULE 1: Begin with Inertia-Advocate INJECTED.
RULE 2: To waive injection, print the INJECTION-PROOF block and cite:
  (a) Candidate charter role — specific role name from Phase 0 roster.
  (b) Orientation clause — the specific text from that role's charter covering switching-cost analysis.
  Both required. Missing either = treat as NO. Claiming YES without citations is an incorrect
  affirmation; the inertia perspective is then silently absent without injection.
RULE 3: `Covers switching-cost analysis: YES` is only valid when both (a) and (b) are populated
  with specific, non-generic content.

CONFIRM: `Inertia owner in tier sort: YES — proven by citation above` (if waived) or
         `Inertia owner in tier sort: NO — Inertia-Advocate INJECTED` (default).

IF INJECTED:
  ENFORCE: Inertia-Advocate is Tier 1, speaks first among all challengers.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.
  PRINT: `[PROVISIONAL resolved: Inertia-Advocate injected as Tier 1 challenger]`

IF NOT INJECTED:
  PRINT: `[PROVISIONAL resolved: [role name] confirmed as inertia owner via [orientation clause]]`

VALIDATE — two independent FAILS axes:
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section.
  FAILS (incorrect affirmation): YES declared without both (a) and (b) citations present.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order. Injected Inertia-Advocate FIRST in Tier 1.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone line before any prose.
WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label] and RESPONDS-TO: [named concern] before endorsement.
VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST; STANCE INVARIANT; PHASE-3-COMMIT with bidirectionality clause.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in ## STANCE MANIFEST.
WRITE: OUTCOME from TALLY.
PRINT: PHASE-4-COMMIT.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster) and Trigger (artifact + recipient
  + authority).

WRITE: TYPE-SPECIFIC OUTPUT — match committee type declared in Phase 0:
  ROB → `Readiness Verdict: [ready / not ready / conditional]` — cite at least one named metric.
    FAILS: section absent — C-01 fail
    FAILS: verdict present but no metric — C-07 partial
  Shiproom → `Go/No-Go: [GO / NO-GO / CONDITIONAL GO]` — cite the specific blocking issue.
    FAILS: section absent — C-01 fail
    FAILS: decision present but no blocking issue — C-07 partial
  Arch-board → ADR Summary: Decision; Rejected Alternative 1 + Rationale; Rejected Alternative
    2 + Rationale. Minimum two alternatives required.
    FAILS: section absent — C-01 fail
    FAILS: fewer than two alternatives — C-01 fail

WRITE: CHARTER FIDELITY TRACE table — for each constraint declared in Phase 0:
  Quorum: Honored YES/NO — cite evidence.
  Scope: Honored YES/NO — cite evidence.
  Veto: Honored YES/NO — cite evidence.
  Escalation: Honored YES/NO — cite evidence (escalation path noted if verdict is not APPROVED).
VALIDATE:
  ACCEPTABLE: all four rows populated with YES/NO + specific evidence
  FAILS: row absent — C-10 fail
  FAILS: `YES` with no evidence — C-10 partial (assertion without basis)
  REQUIRE: at least two rows cite charter-specific constraint language.

PRINT: action items as [Owner Role] — [specific action] — [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK — objection citing INERTIA-FINDING-* label, resolution path,
  named authority. If no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```
