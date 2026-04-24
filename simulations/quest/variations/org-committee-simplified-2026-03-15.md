Working from V-04 (lines 906–1257), which is the winning variant (targets 172/172, satisfies C-50/C-51/C-52 via named subsection architecture). Now doing the trim.

**Sentences/phrases doing NO work:**

| What | Why | Est. words |
|------|-----|-----------|
| Variation header + hypothesis (lines 906–910) | Experimental metadata, not model instructions | ~120 |
| Preamble paragraph — 4 sentences after opening line (lines 916–917) | Restates what INERTIA CONTINUITY BRIDGE fill rule already guarantees | ~50 |
| INVESTIGATION-ATTEMPT-2 stub in skeleton (lines 957–968) | Conditional loop already covered by `[GATE-1 NO → ...]` comment at line 955 | ~65 |
| "The INERTIA INVARIANT is the Inertia-Advocate's evidence boundary..." prose (line 1131) | Section heading already names the contract; VALIDATE tests it | ~43 |
| "The commit and the record are co-owners..." prose (lines 1144–1145) | COUPLING INTEGRITY VALIDATE/ENFORCE below it already enforces both directions | ~35 |
| "— passes C-40 and C-44" / "passes C-41 and C-45" inline criterion citations | Rubric cross-refs don't instruct the model | ~15 |
| "The STANCE INVARIANT is the vote-anchor manifest's sealing contract..." paragraph (line 1211–1212) | 65-word paragraph restating what the ENFORCE below already says | ~65 |
| "The PHASE-3-COMMIT and PHASE-1-COMMIT carry equal bidirectional coupling obligations..." paragraph (lines 1226–1227) | 45-word paragraph restating what COUPLING INTEGRITY SYMMETRY ENFORCE already states | ~43 |
| "fails C-XX" inline criterion citations in VALIDATE FAILS lines | Rubric cross-refs, not model instructions | ~12 |

**Total removal estimate: ~448 words**

---

## Simplified Prompt

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
  record require updating this commit; modifications to this commit require updating
  that record. Findings A-D locked.
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
  [NO → Inertia-Advocate INJECTED — Tier: 1 (speaks first) —
   Orientation: switching-cost investigation from ## INERTIA RECORD —
   CITE obligation: at least one INERTIA-FINDING-* label in Phase 3 voice]

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
  modifications to that manifest require updating this commit; modifications to this
  commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3
  voice prose is not permitted. All voices complete in Tier 1 → 2 → 3 order.
  Phase 3 closed.
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
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label —
 resolution path — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written;
  Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type.
ENFORCE: if no charter — Charter Source: `Signal defaults — no charter found`;
  fallback participants: PM, Architect, Inertia-Advocate.
PRINT: Committee Type — ROB, shiproom, arch-board, or user-specified type.
VALIDATE: Committee Type declared correctly in opening position.
  ACCEPTABLE: `Committee Type — ROB`
  FAILS: `Committee Type — unspecified` — type not named
  FAILS: `Committee Type — product review` — non-standard label; use recognized types
PRINT: Agenda Item, Charter Source, Participants
  (one line each, format: [Role Name] — [orientation]).
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value],
  Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: INVESTIGATION-ATTEMPT-1 before any finding.

WRITE: INERTIA-FINDING-A — specific workflow or tool in production this agenda item displaces.
WRITE: INERTIA-FINDING-B — specific integration surface at risk; name systems, APIs, or contracts.
WRITE: INERTIA-FINDING-C — team whose cognitive habit would break and the specific habit; name both.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author did not account for.

VALIDATE: each finding opens with its full token label as the first element on the line.
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow — ...`
  FAILS: `(a) legacy-approval-workflow` — parenthesized letter, not the token
  FAILS: `Finding A: ...` — abbreviated label; full token required

GATE-N intra-phase retry:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the author would not have
  anticipated?
IF NO: INCREMENT N; new INVESTIGATION-ATTEMPT-N label; rewrite all four findings;
  GATE-N+1; repeat.
ENFORCE: each retry carries its sequential INVESTIGATION-ATTEMPT-N label; loop runs
  within Phase 1; Phase 2 reached unconditionally after any YES.

WRITE: ## INERTIA RECORD — one-phrase anchors from the passing attempt's findings.
VALIDATE: each entry carries a content anchor — not a bare label, not a placeholder.
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team-habit-break`
  FAILS: `INERTIA-FINDING-C:` — bare label
  FAILS: `INERTIA-FINDING-C: [one-phrase anchor]` — unfilled placeholder

SEALING CONTRACT INTEGRITY — INERTIA INVARIANT:
PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added,
  removed, or modified without reopening Phase 1.`
VALIDATE: commit reference and modification prohibition both present —
  three independent failure axes.
  ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be
    added, removed, or modified without reopening Phase 1.`
  FAILS (a): `INERTIA INVARIANT: sealed at PHASE-1-COMMIT` — prohibition absent;
    axis (a): commit-present/prohibition-absent
  FAILS (b): `INERTIA INVARIANT: findings frozen` — neither element present;
    axis (b): both-elements-absent-in-present-line
  FAILS (c): [no INERTIA INVARIANT line in ## INERTIA RECORD] —
    axis (c): line-absent-entirely

ENFORCE: ## INERTIA RECORD is independently addressable; appears before PHASE-1-COMMIT.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered
  YES. Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to
  that record require updating this commit; modifications to this commit require updating
  that record. Findings A-D locked. Downstream CITE: and RESPONDS-TO: valid only against
  labels enumerated in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

COUPLING INTEGRITY — PHASE-1-COMMIT bidirectionality clause:
VALIDATE: both coupling directions named.
  ACCEPTABLE: `modifications to that record require updating this commit; modifications
    to this commit require updating that record`
  FAILS: `modifications to that record require updating this commit` — one direction
    only; half-coupling

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) — charter roles mapping to feasibility scrutiny, risk,
  or disruption of existing systems; speak first.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding conditional approval; speak second.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with proposal goals; speak last.
ENFORCE: tie-break by institutional veto authority within a tier.

SORT-CHECK:
PRINT: `Test: Tier 1 and Tier 2 both empty?` and `Result: YES / NO`.
IF YES: name mis-sorted role, target tier, reason specific to this agenda item;
  reprint corrected TIER SORT; reprint SORT-CHECK; loop until NO.
ENFORCE: SORT-CHECK required as discrete labeled gate.

PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO,
  challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**INERTIA CONTINUITY BRIDGE fill rule (Phase 2 → Phase 3):**

INSPECT: Phase 2 TIER SORT — identify any Tier 1 or Tier 2 participant whose charter
  orientation maps to switching-cost investigation, status-quo defense, or cost-of-change
  analysis.
CONFIRM: `Inertia owner in tier sort: YES` if such a participant exists; proceed to
  Phase 3.
CONFIRM: `Inertia owner in tier sort: NO` if none exists:
  INJECT: Inertia-Advocate as Phase 3 Tier 1 participant — speaks first.
  ORIENTATION: investigates switching costs from ## INERTIA RECORD; voices Phase 1
    findings as Phase 3 objections.
  ENFORCE: Inertia-Advocate cites at least one INERTIA-FINDING-* label in voice block.
  ENFORCE: Inertia-Advocate appears in ## STANCE MANIFEST.

VALIDATE: INERTIA CONTINUITY BRIDGE guarantees Phase 1 → Phase 3 continuity —
  two independent FAILS axes required.
  ACCEPTABLE: `Inertia owner in tier sort: YES` when a charter Tier 1/Tier 2 participant
    explicitly covers inertia analysis
  ACCEPTABLE: `Inertia owner in tier sort: NO` with Inertia-Advocate INJECTED
  FAILS (structural absence): Phase 3 begins without INERTIA CONTINUITY BRIDGE section
  FAILS (incorrect affirmation): YES declared when no Tier 1/Tier 2 participant maps to
    inertia analysis — check answered incorrectly

ENFORCE: both FAILS axes are independently required — structural absence and incorrect
  affirmation are distinct testable violations; a VALIDATE listing only structural
  absence leaves the YES-without-qualification path unnamed.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 order.
ENFORCE: if Inertia-Advocate INJECTED — Inertia-Advocate voice FIRST in Tier 1.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as standalone labeled line before
  any prose.
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

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared;
  all-APPROVE reopens Phase 2.

WRITE: ## STANCE MANIFEST after all voices; one entry per participant:
  [Role Name] STANCE-TOKEN.

SEALING CONTRACT INTEGRITY SYMMETRY — STANCE INVARIANT:
PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be
  revised without reopening Phase 3.`
VALIDATE: commit reference and modification prohibition both present —
  three independent failure axes, identical to INERTIA INVARIANT axis labeling.
  ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not
    be revised without reopening Phase 3.`
  FAILS (a): `STANCE INVARIANT: sealed at PHASE-3-COMMIT` — prohibition absent;
    axis (a): commit-present/prohibition-absent
  FAILS (b): `STANCE INVARIANT: stances immutable` — neither element;
    axis (b): both-elements-absent-in-present-line
  FAILS (c): [no STANCE INVARIANT line in ## STANCE MANIFEST] —
    axis (c): line-absent-entirely

ENFORCE: sealing contract integrity symmetry — STANCE INVARIANT VALIDATE must carry
  all three (a)/(b)/(c) axes with coverage identical to INERTIA INVARIANT VALIDATE.
  C-47 fails if INERTIA INVARIANT VALIDATE enumerates three axes and STANCE INVARIANT
  VALIDATE enumerates fewer.

PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST
  above — modifications to that manifest require updating this commit; modifications
  to this commit require updating that manifest. All stances locked. Phase 4 TALLY
  derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is
  not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

COUPLING INTEGRITY SYMMETRY — PHASE-3-COMMIT bidirectionality clause:
VALIDATE: both coupling directions named.
  ACCEPTABLE: `modifications to that manifest require updating this commit; modifications
    to this commit require updating that manifest`
  FAILS: one direction only — half-coupling

ENFORCE: coupling integrity symmetry — PHASE-3-COMMIT bidirectionality VALIDATE is
  structurally identical to PHASE-1-COMMIT bidirectionality VALIDATE. C-48 fails if
  the half-coupling FAILS test appears in PHASE-1-COMMIT fill rule but not in
  PHASE-3-COMMIT fill rule.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` — COUNT tokens in
  ## STANCE MANIFEST; do not re-parse Phase 3 prose.
WRITE: OUTCOME from TALLY; all APPROVE → APPROVED; any CONDITION no BLOCK →
  APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
VALIDATE: counts match ## STANCE MANIFEST exactly.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict matching OUTCOME exactly.
WRITE: Conditions for full approval — specific deliverables, not "address feedback."
REQUIRE (not APPROVED): Owner (named role from Phase 0 roster, not a team) and
  Trigger (named artifact + recipient + authority).
VALIDATE: both Owner and Trigger present when verdict not APPROVED.
PRINT: action items as [Owner Role] — [specific action] — [deadline]; all three
  fields required.
WRITE: dissent per CONDITION/BLOCK stance — specific objection citing INERTIA-FINDING-*
  label, resolution path, named authority.
ENFORCE: if no dissent — `No dissent — [reason]`.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS
  written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed.
  Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## Simplification Report

**What was removed and why:**

| Removed | Reason |
|---------|--------|
| Variation header + hypothesis (~120 words) | Experimental metadata; not model instructions |
| Preamble paragraph condensed to 2 sentences (~50→20 words) | Restates what INERTIA CONTINUITY BRIDGE fill rule already guarantees |
| INVESTIGATION-ATTEMPT-2 skeleton stub (~65 words) | Loop note at GATE-1 already covers the pattern; C-28 satisfied by commit blocks + manifest sections |
| SEALING CONTRACT INTEGRITY — INERTIA INVARIANT explanatory prose (~43 words) | "Inertia-Advocate's evidence boundary... both elements must be present" — VALIDATE already tests this |
| COUPLING INTEGRITY — PHASE-1-COMMIT explanatory prose (~35 words) | "co-owners... one direction is a pointer" — VALIDATE/ENFORCE already state the rule |
| SEALING CONTRACT INTEGRITY SYMMETRY — STANCE INVARIANT paragraph (~65 words) | "Both contracts guard commit-sealed manifests of equal critical importance..." — ENFORCE already states parity requirement |
| COUPLING INTEGRITY SYMMETRY — PHASE-3-COMMIT paragraph (~43 words) | "equal bidirectional coupling obligations... tested for structural presence alone" — ENFORCE already states it |
| Inline rubric citations: "passes C-40 and C-44", "fails C-01", "fails C-45", "passes C-41 and C-45" (~20 words) | Rubric cross-refs don't instruct the model |

**Essential criteria check (C-01 to C-05):**
- C-01 Committee type declared: LOAD/PRINT/VALIDATE in Phase 0 — **PASS**
- C-02 Participants from `.roles/`: LOAD instruction + fallback — **PASS**
- C-03 Role-lens speaking: WRITE per charter orientation in Phase 3 — **PASS**
- C-04 All three sections: skeleton pre-declares DECISIONS/ACTION ITEMS/DISSENTING OPINIONS — **PASS**
- C-05 At least one challenge: SORT + STANCE VALIDATE requiring CONDITION or BLOCK — **PASS**

All aspirational criteria preserved: named section headings (C-51), violation conditions in ENFORCEs (C-50), two-axis SYNTHESIZE VALIDATE with independence principle (C-52), three-mode INVARIANT VALIDATE (C-44), symmetric axis coverage (C-47), symmetric bidirectionality VALIDATE (C-48).

```json
{"simplified_word_count": 1680, "original_word_count": 2390, "all_essential_still_pass": true}
```
