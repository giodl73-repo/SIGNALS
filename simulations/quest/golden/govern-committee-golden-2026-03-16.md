---
skill: quest-golden
skill_target: org-committee
date: 2026-03-15
rounds: 20
rubric_final: org-committee-rubric-v20-2026-03-16.md
score: 172
status: GOLDEN
---

# org:committee — Golden Prompt (R20, v20 rubric, 172/178)

## What Made It Golden

**V-04 (Combined: Lifecycle Emphasis + Inertia Framing)** reached 172/172 against the v19 rubric,
scoring the full composite maximum for that version. Five structural patterns distinguish it from
the baseline V-01, which also scored 172/172 but did so with inline ENFORCE postscripts and
positive-only symmetry contracts — the structural gaps C-50, C-51, and C-52 were designed to close.

**1. Named subsections for symmetry enforcement (C-51)**
V-04 organized C-47 and C-48 as first-class named subsections — `SEALING CONTRACT INTEGRITY
SYMMETRY — STANCE INVARIANT` and `COUPLING INTEGRITY SYMMETRY — PHASE-3-COMMIT bidirectionality
clause` — rather than ENFORCE postscripts appended to the tail of the parent fill rule. This
applies the same C-37/C-40 named-section principle to the symmetry layer: parity contracts are
independently navigable by heading, not discoverable only by reading through the parent rule's
full text.

**2. Explicit named violation conditions in symmetry ENFORCE clauses (C-50)**
Every symmetry ENFORCE clause in V-04 carries both a positive requirement and a named violation
boundary: "C-47 fails if INERTIA INVARIANT VALIDATE enumerates three axes and STANCE INVARIANT
VALIDATE enumerates fewer"; "C-48 fails if the half-coupling FAILS test appears in PHASE-1-COMMIT
fill rule but not in PHASE-3-COMMIT fill rule." V-01's ENFORCE stated only the compliant form
("must be structurally identical"). V-04's ENFORCE is a bidirectional contract — compliant form
anchored, violation form named — so the boundary is testable rather than inferential.

**3. INERTIA CONTINUITY BRIDGE as a named skeleton section (C-46, C-51)**
The Phase 2 → Phase 3 continuity guarantee is a named `## INERTIA CONTINUITY BRIDGE` section in
the skeleton, making C-46's structural purpose visible at the architectural level before any fill
occurs. The Inertia-Advocate injection is not a fill-time discipline; it is a pre-declared
skeleton slot with INSPECT/CONFIRM/INJECT instructions and its own bilateral VALIDATE.

**4. Independence principle in SYNTHESIZE VALIDATE ENFORCE (C-52)**
V-04's ENFORCE on the INERTIA CONTINUITY BRIDGE VALIDATE names the logical basis for two-axis
structure: "structural absence and incorrect affirmation are distinct testable violations." V-01's
ENFORCE was a quantity assertion — "both FAILS axes are independently required" — without naming
why independence is necessary. V-04's formulation converts the ENFORCE from a co-requirement list
into a logical statement: the axes cannot be collapsed because they test different failure modes
on different dimensions.

**5. Coupling integrity symmetry across both phase-commit fill rules (C-48)**
The content-completeness VALIDATE on the bidirectionality clause — ACCEPTABLE: both directions
stated / FAILS: one direction only (half-coupling) — appears in both the PHASE-1-COMMIT and
PHASE-3-COMMIT fill rules under a dedicated named subsection. V-01 carried the bilateral VALIDATE
on PHASE-1-COMMIT but not as a symmetry-enforced parallel on PHASE-3-COMMIT. V-04 closes the
gap and makes the symmetry explicit by ENFORCE.

---

## Golden Prompt

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

The Inertia-Advocate is a structural participant in every org:committee simulation.
If the charter supplies no inertia owner, the INERTIA CONTINUITY BRIDGE injects one
before Phase 3 begins — verified for both structural presence and affirmation correctness.

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
PRINT: Committee Type — ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type — ROB`
  FAILS: `Committee Type — unspecified` — type not named; fails C-01
  FAILS: `Committee Type — product review` — non-standard label; use recognized types
PRINT: Agenda Item, Charter Source, Participants (one line each, format: [Role Name] — [orientation]).
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value],
  Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A — specific workflow or tool in production that this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label as the first element on the line.
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow — ...`
  FAILS: `(a) legacy-approval-workflow` — parenthesized letter, not the token; fails C-27
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
VALIDATE: commit reference and modification prohibition both present — three independent failure axes.
  ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added,
    removed, or modified without reopening Phase 1.` — both contract elements present
  FAILS (a): `INERTIA INVARIANT: sealed at PHASE-1-COMMIT` — commit reference present,
    prohibition absent; axis (a): commit-present/prohibition-absent
  FAILS (b): `INERTIA INVARIANT: findings frozen` — line exists but carries neither element;
    axis (b): both-elements-absent-in-present-line
  FAILS (c): [## INERTIA RECORD with correct findings but no INERTIA INVARIANT line] —
    contract absent; axis (c): line-absent-entirely

ENFORCE: ## INERTIA RECORD is independently addressable; appears before PHASE-1-COMMIT.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that
  record require updating this commit; modifications to this commit require updating that
  record. Findings A-D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

COUPLING INTEGRITY — PHASE-1-COMMIT bidirectionality clause:
VALIDATE: both coupling directions named.
  ACCEPTABLE: `modifications to that record require updating this commit; modifications to
    this commit require updating that record` — bilateral contract declared
  FAILS: `modifications to that record require updating this commit` — one direction only;
    half-coupling; reverse obligation absent; fails C-45

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
ENFORCE: SORT-CHECK as discrete labeled gate; correct ordering without the gate fails C-25.

PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first
  ordering confirmed. Phase 2 closed.
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

VALIDATE: INERTIA CONTINUITY BRIDGE guarantees Phase 1 → Phase 3 continuity — two independent
  FAILS axes required.
  ACCEPTABLE: `Inertia owner in tier sort: YES` when a charter Tier 1/Tier 2 participant
    explicitly covers inertia analysis
  ACCEPTABLE: `Inertia owner in tier sort: NO` with Inertia-Advocate INJECTED — design
    guarantee fires; Phase 1 → Phase 3 continuity ensured
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section —
    Phase 1 findings may have no owner-voice; fails C-46
  FAILS (incorrect affirmation): YES declared when no Tier 1/Tier 2 participant maps to
    inertia analysis — check answered incorrectly; inertia perspective silently absent
    without injection; fails C-49

ENFORCE: both FAILS axes are independently required — structural absence and incorrect
  affirmation are distinct testable violations; a VALIDATE listing only structural absence
  leaves the YES-without-qualification path unnamed.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED — Inertia-Advocate voice FIRST in Tier 1.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before any prose.
VALIDATE: STANCE: is a structural committed declaration — prose may not contradict it.
  ACCEPTABLE: `STANCE: BLOCK` alone on its own line
  FAILS: stance embedded in prose, no STANCE: label
  FAILS: `STANCE: BLOCK (pending)` — qualified token

WRITE: 2-4 sentences per participant from their charter orientation.
REQUIRE (Tier 1): cite named INERTIA-FINDING-* label from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): CITE: [INERTIA-FINDING-* label — content] before endorsement;
  RESPONDS-TO: "[named concern]" — [one sentence] before endorsement.
  VALIDATE CITE: label is first element after CITE:.
  VALIDATE RESPONDS-TO: names and quotes a specific concern.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST after all voices; one entry per participant: [Role Name] STANCE-TOKEN.

SEALING CONTRACT INTEGRITY SYMMETRY — STANCE INVARIANT:
PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
  without reopening Phase 3.`
VALIDATE: commit reference and modification prohibition both present — three independent failure
  axes, identical to INERTIA INVARIANT axis labeling.
  ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised
    without reopening Phase 3.`
  FAILS (a): `STANCE INVARIANT: sealed at PHASE-3-COMMIT` — prohibition absent;
    axis (a): commit-present/prohibition-absent
  FAILS (b): `STANCE INVARIANT: stances immutable` — neither element;
    axis (b): both-elements-absent-in-present-line
  FAILS (c): [no STANCE INVARIANT line in ## STANCE MANIFEST] — line absent;
    axis (c): line-absent-entirely

ENFORCE: sealing contract integrity symmetry — STANCE INVARIANT VALIDATE must carry all three
  (a)/(b)/(c) axes with coverage identical to INERTIA INVARIANT VALIDATE. C-47 fails if
  INERTIA INVARIANT VALIDATE enumerates three axes and STANCE INVARIANT VALIDATE enumerates fewer.

PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above —
  modifications to that manifest require updating this commit; modifications to this commit
  require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice
  prose is not permitted.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

COUPLING INTEGRITY SYMMETRY — PHASE-3-COMMIT bidirectionality clause:
VALIDATE: both coupling directions named.
  ACCEPTABLE: `modifications to that manifest require updating this commit; modifications to
    this commit require updating that manifest` — bilateral
  FAILS: one direction only — half-coupling; fails C-45

ENFORCE: coupling integrity symmetry — PHASE-3-COMMIT bidirectionality VALIDATE is structurally
  identical to PHASE-1-COMMIT bidirectionality VALIDATE. C-48 fails if the half-coupling FAILS
  test appears in PHASE-1-COMMIT fill rule but not in PHASE-3-COMMIT fill rule.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in ## STANCE MANIFEST;
  do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY; all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH
  CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
VALIDATE: counts match ## STANCE MANIFEST exactly.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster, not a team) and Trigger
  (named artifact + recipient + authority).
VALIDATE: both Owner and Trigger present when verdict not APPROVED; missing either fails C-23.
PRINT: action items as [Owner Role] — [specific action] — [deadline]; all three fields required.
WRITE: dissent per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-* label,
  resolution path, named authority.
ENFORCE: if no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## Final Rubric Criteria Summary (v20 — 178 pts max)

### Essential — 60 pts (5 x 12 pts; any fail = rubric fail)

| ID | Criterion |
|----|-----------|
| C-01 | Committee type declared correctly in output opening |
| C-02 | Participants loaded from `.craft/roles/`; graceful fallback with disclosure |
| C-03 | Each participant speaks from their charter role lens |
| C-04 | Output includes all three sections: decisions, action items, dissenting opinions |
| C-05 | At least one challenge, condition, or block surfaced |

### Recommended — 30 pts (3 x 10 pts)

| ID | Criterion |
|----|-----------|
| C-06 | Agenda item specificity — simulation responds to prior concerns, not generic positions |
| C-07 | Action items owned and actionable — `[Owner Role] -- [action] -- [deadline]` |
| C-08 | Dissents include resolution paths and re-entry conditions |

### Aspirational — 88 pts (44 x 2 pts)

| Range | Description |
|-------|-------------|
| C-09 to C-13 | Non-obvious surprise; decision-complete outcome; challenger-first sort; switching-cost investigation precedes simulation; stance declared before prose |
| C-14 to C-18 | Vote tally before minutes; STANCE: as structural label; BLOCK gate check; advocates cite Phase 1 findings; conditions include measurable acceptance criteria |
| C-19 to C-23 | SORT-CHECK validates tier assignment; Phase 2 unconditional; LOAD instruction explicit; gate loop intra-Phase 1; commit blocks terminal |
| C-24 to C-28 | Commit blocks carry terminal-position ENFORCE; Phase 3 VALIDATE checks stance completeness; CONFIRM after LOAD; Phase 1 findings carry citable labels; skeleton pre-declared in Step 1 |
| C-29 to C-35 | Gate loop bounded in Phase 1; every fill rule imperative verb-first; named commit blocks per phase; commit blocks carry named ENFORCE sub-instruction; PHASE-1-COMMIT seals INERTIA RECORD; PHASE-3-COMMIT seals STANCE MANIFEST; commit blocks cross-reference manifest headings |
| C-36 to C-43 | Bilateral VALIDATE on all content-fill rules; manifests as named section headings; commit cross-references name exact heading; bilateral VALIDATE on committee-type checkpoint; manifest sections carry explicit seal declarations; commit cross-references include explicit bidirectionality constraint; bilateral VALIDATE on INVARIANT seal fill rules; bidirectionality clauses pre-declared as skeleton placeholders with dedicated fill rules |
| C-44 to C-49 | INVARIANT VALIDATE enumerates three independent seal-element failure axes; bidirectionality VALIDATE tests both-directions content completeness; Inertia-Advocate structurally guaranteed via SYNTHESIZE instruction; three-axis INVARIANT VALIDATE coverage symmetric across both seals; bidirectionality VALIDATE symmetric across both phase-commit fill rules; SYNTHESIZE VALIDATE includes incorrect-affirmation FAILS axis |
| C-50 to C-52 | Symmetry ENFORCE clauses include named violation condition (not positive-only); symmetry enforcement blocks organized as named skeleton subsections; SYNTHESIZE VALIDATE ENFORCE names the independence principle for its two FAILS axes |

**Score bands**: 178 = full compliance; 172-177 = v19-perfect (C-50/C-51/C-52 cluster gaps only);
162-171 = one recommended gap or two-three aspirational gaps outside the new cluster;
below 136 = foundational gaps.
