# org:committee Variations — Round 12
Generated: 2026-03-16
Skill: org:committee
Rubric: v12 (C-32 commit markers carry explicit terminal-position enforcement rules; C-33 Phase 1 commit enumerates locked investigation tokens as a citation-anchor manifest; aspirational pool 25 criteria, composite max 140)

R11 reference context: V-05 was the R11 golden synthesis targeting 136/136 — skeleton pre-declaration (C-28), imperative fill rules (C-30), INERTIA-FINDING named labels (C-27), intra-phase gate loops (C-29), PHASE-N-COMMIT: [locked] terminal markers (C-31). The gap to 140/140 is C-32 and C-33. C-32: the PHASE-N-COMMIT: blocks carried `[locked]` declarations but not active blocking assertions — terminal position was a structural inference, not a stated rule. C-33: the PHASE-1-COMMIT: declared the investigation phase closed but did not enumerate the named INERTIA-FINDING labels it was locking — citation validity was derivable from Phase 1 prose, not anchored to the commit itself.

Variation axes selected:
- Single-axis V-01: Lifecycle emphasis — minimal diff from R11 V-05: upgrade every PHASE-N-COMMIT line in the skeleton from `[locked]` to `[locked] | ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE`, and add ENFORCE assertion to every commit-rule in STEP 2 (C-32 primary)
- Single-axis V-02: Output format — flat command sequence with C-32 ENFORCE assertions in each phase block (no skeleton; tests whether C-32 is satisfiable outside skeleton format)
- Single-axis V-03: Phrasing register — conversational register framing; `PHASE-N-COMMIT:` blocks retain ENFORCE blocking assertions in compact form (tests C-32 compliance in less rigid register)
- Combined V-04: Lifecycle emphasis + Inertia framing — PHASE-1-COMMIT enumerates locked INERTIA-FINDING labels by name as a citation-anchor manifest (C-33 primary; also includes C-32 ENFORCE assertions on all commit markers)
- Combined V-05: Full synthesis — skeleton + imperative fill rules + C-32 ENFORCE assertions in all COMMIT markers + C-33 citation-anchor manifest in PHASE-1-COMMIT (targets 140/140)

---

## V-01 — Single-axis: Lifecycle Emphasis — C-32 ENFORCE Blocking Assertions in PHASE-N-COMMIT Markers

**Variation axis**: Lifecycle emphasis — R11 V-05 skeleton and fill rules preserved exactly; the only change is upgrading every `PHASE-N-COMMIT: [locked]` line in the skeleton to include an explicit terminal-position enforcement rule, and adding an `ENFORCE:` blocking assertion to every commit fill rule in STEP 2. No other axis touched.

**Hypothesis**: R11 V-05 passed C-31 because `PHASE-N-COMMIT: [locked]` markers appeared before every next-phase header. C-32 is not satisfied by a lock declaration that appears at the end of a phase — it requires the commit block itself to state an active blocking rule so terminal position is declared, not inferred. The R11 gap: `PHASE-3-COMMIT: [locked] — All voices written` is a boundary marker (C-31 passes) but carries no prohibition on post-commit Phase 3 content (C-32 fails). The minimal fix: `PHASE-3-COMMIT: [locked] — All voices written | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE` converts the marker into an active blocker. Hypothesis: this single-line upgrade to each COMMIT marker closes C-32 with no other changes, moving score from 136 to 138. C-33 is the remaining gap (addressed in V-04 and V-05).

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded. | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO → fill INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]

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

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES, INERTIA-FINDING-A through D active. Phase 1 closed. | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → reassign: ___ to Tier ___ because ___; corrected TIER SORT follows / NO → valid]

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed. | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

PHASE-3-COMMIT: [locked] — All voices written in tier order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed. | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed. | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

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
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete. | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type is declared before any other content; an output that proceeds without it fails C-01.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0 — no Phase 0 content may appear after it; the next element after PHASE-0-COMMIT: is the Phase 1 header.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded. | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces.
  ENFORCE: precision required — "existing workflow" fails; name the production artifact.

WRITE: INERTIA-FINDING-B — name the integration surface at risk.
  REQUIRE: specific systems, APIs, contracts, or downstream consumers that would break or require renegotiation.

WRITE: INERTIA-FINDING-C — name the team whose cognitive habits would break and the specific decision-making habit they rely on today.
  ENFORCE: name both the team and the habit; "teams in general" fails.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

VALIDATE: each finding carries its named label (INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D) as the first token.

GATE-1 intra-phase retry loop (C-29):
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → CONFIRM loop exit; PHASE-1-COMMIT: fills immediately; Phase 2 is unconditional.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with the same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block in output; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it; the next element after PHASE-1-COMMIT: is the Phase 2 header.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES, INERTIA-FINDING-A through D from attempt [N] active as citation anchors. Phase 1 closed. | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) — roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems.
  ENFORCE: these roles speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) — roles that hold approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals.
  ENFORCE: these roles speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK fill rule (intra-phase loop):
PRINT: Test field as fixed string: `Tier 1 and Tier 2 both empty?`
CONFIRM: Result — YES or NO.
VALIDATE: if Result YES — REQUIRE reassignment: name the mis-sorted role, name the target tier, state the reason; RE-PRINT corrected TIER SORT block; RE-PRINT new SORT-CHECK block; LOOP until Result NO.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both `Test:` and `Result:` fields.
CONFIRM: Result NO is the Phase 2 exit condition.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2 — no Phase 2 content may appear after it; the next element after PHASE-2-COMMIT: is the Phase 3 header.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed. | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2-4 sentences per participant from their charter-documented role orientation responding to this specific agenda item.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label where relevant.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; prose before the label fails C-20.

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific finding or concern — generic acknowledgment fails.

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK.
ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it; the next element after PHASE-3-COMMIT: is the Phase 4 header.
PRINT: PHASE-3-COMMIT: [locked] — All voices written in Tier 1 → 2 → 3 order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed. | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block.
COUNT: each STANCE: declaration from Phase 3 — one tally entry per participant categorized by declared STANCE.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it; the next element after PHASE-4-COMMIT: is the Phase 5 header.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed. | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; "address feedback" fails.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role from Phase 0 participant roster responsible for satisfying the blocking condition.
  WRITE: Trigger — concrete deliverable or event that causes committee re-review; "sufficient progress" fails.
VALIDATE: both Owner and Trigger present (C-23).

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts per item; "investigate" alone fails.

DISSENTING OPINIONS fill rules:
WRITE: for each participant whose STANCE was CONDITION or BLOCK — dissent substance citing INERTIA-FINDING-* label where applicable and resolution path with concrete trigger and named authority.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining why all participants reached consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 — no Phase 5 content may appear after it; it is the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete. | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-02 — Single-axis: Output Format — Flat Command Sequence with C-32 ENFORCE Assertions (no skeleton)

**Variation axis**: Output format — no skeleton print step. The simulation is structured as a flat sequence of labeled phase blocks, each containing verb-first imperative commands, with the PHASE-N-COMMIT: block at the end of each phase carrying an explicit blocking assertion. This tests whether C-32 is satisfiable outside the skeleton format, and whether the absence of a pre-printed skeleton (C-28) changes the character of the C-32 compliance.

**Hypothesis**: R11 V-02 (flat command sequence) was the non-skeleton variation used to test C-31 compliance without the skeleton format. It showed C-31 is satisfiable in a flat command format. C-32 adds the blocking assertion requirement: each PHASE-N-COMMIT: must include `ENFORCE: terminal position stated in every phase — no content may follow this commit within Phase N`. This is purely a phrasing addition to the commit block and should work identically in flat command format. The flat format also tests whether removing the skeleton (C-28 partial-pass territory) changes the C-32 compliance posture — hypothesis: C-32 passes even without a skeleton, because the blocking assertion is in the commit block text, not the skeleton structure. Expected score: 138/140 (C-33 not addressed; C-28 partial pass).

---

You are running `org:committee`. Generate the simulation phase by phase using the commands below.

---

**PHASE 0 — COMMITTEE DECLARATION**

LOAD: committee charter from `.roles/` matching the requested committee type.
EXTRACT: every named role with documented orientation from the charter.
FALLBACK: if no charter exists — WRITE Charter Source: `Signal defaults — no charter found`; USE: PM, Architect, Inertia-Advocate as fallback participants.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or user-specified type.
PRINT: Agenda Item — the item under review exactly as stated in the request.
PRINT: Charter Source — `.roles/` path used or fallback declaration.
PRINT: Participants list — one line per loaded role: `[Role Name] — [charter orientation in one phrase]`.
VALIDATE: Committee Type appears as the first declared field before any simulation content.

COMMIT Phase 0:
PRINT: `PHASE-0-COMMIT: [locked] — Committee Type declared, [N] participants loaded from [source]. Phase 0 closed.`
ENFORCE: terminal position stated in Phase 0 — no Phase 0 content may follow this commit. The next line is the Phase 1 header.

---

**PHASE 1 — INVESTIGATION**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.
WRITE: INERTIA-FINDING-A — the specific workflow, tool, or process currently in production that this agenda item displaces. Precision required; generic naming fails.
WRITE: INERTIA-FINDING-B — the integration surface at risk: specific systems, APIs, contracts, or downstream consumers requiring renegotiation.
WRITE: INERTIA-FINDING-C — the team whose cognitive habits would break and the specific decision-making habit they rely on today. Name both.
WRITE: INERTIA-FINDING-D — the non-obvious switching cost the proposal author almost certainly did not account for. Specific enough that the author would say "I missed that."
VALIDATE: each finding carries its `INERTIA-FINDING-*` label as the first token.

GATE-1:
EVALUATE: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
PRINT: `GATE-1 Answer: [YES/NO] — [one-sentence basis]`
IF YES: proceed to PHASE-1-COMMIT.
IF NO: LABEL `INVESTIGATION-ATTEMPT-2`; REWRITE: all four INERTIA-FINDING-* entries from a different angle; GATE-2 with same question; INCREMENT attempt counter; REPEAT until YES.
REQUIRE: each rewrite labeled with INVESTIGATION-ATTEMPT-N+1; sequential label increments by 1.
CONFIRM: INERTIA-FINDING-A through D from the passing attempt are now the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: references use these named labels.

COMMIT Phase 1:
PRINT: `PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES, INERTIA-FINDING-A through D active. Phase 1 closed.`
ENFORCE: terminal position stated in Phase 1 — no Phase 1 content may follow this commit. The next line is the Phase 2 header.

---

**PHASE 2 — TIER SORT**

LOAD: full participant roster from Phase 0.
ASSIGN: Tier 1 (CHALLENGERS) — roles whose orientation interrogates feasibility, risk, or disruption.
ASSIGN: Tier 2 (CONDITIONALS) — roles that hold approval pending named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals.
ENFORCE: tie-break within a tier by institutional veto authority, highest first.

SORT-CHECK (intra-phase gate):
PRINT: `SORT-CHECK — Test: Tier 1 and Tier 2 both empty?`
CONFIRM: Result YES or NO.
IF YES: REASSIGN one role to Tier 1 or Tier 2; name the role, the target tier, and the reason. REPRINT corrected TIER SORT. REPRINT new SORT-CHECK. LOOP until Result NO.
IF NO: proceed to PHASE-2-COMMIT.

COMMIT Phase 2:
PRINT: `PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.`
ENFORCE: terminal position stated in Phase 2 — no Phase 2 content may follow this commit. The next line is the Phase 3 header.

---

**PHASE 3 — PARTICIPANT VOICES**

ENFORCE: generate voices in order: Tier 1 → Tier 2 → Tier 3.
FOR EACH participant:
  PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as the first line.
  WRITE: 2-4 sentences from their charter-documented orientation responding to this specific agenda item.
  REQUIRE (Tier 1): cite a named INERTIA-FINDING label in the concern.
  REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
  REQUIRE (Tier 3):
    PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding]`
    PRINT: `RESPONDS-TO: "[named concern from Tier 1 or Tier 2]" — [one sentence response]`

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK present.
IF all APPROVE: REOPEN Phase 2; REASSIGN tiers; REPRINT corrected TIER SORT; RERUN SORT-CHECK; REGENERATE Phase 3.

COMMIT Phase 3:
PRINT: `PHASE-3-COMMIT: [locked] — All voices written Tier 1 → 2 → 3, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: present. Phase 3 closed.`
ENFORCE: terminal position stated in Phase 3 — no Phase 3 content may follow this commit. The next line is the Phase 4 header.

---

**PHASE 4 — TALLY**

COUNT: each STANCE: from Phase 3 — one entry per participant by stance category.
PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK`
DERIVE: OUTCOME from TALLY: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
PRINT: `OUTCOME: [value]`

COMMIT Phase 4:
PRINT: `PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.`
ENFORCE: terminal position stated in Phase 4 — no Phase 4 content may follow this commit. The next line is the Phase 5 header.

---

**PHASE 5 — MINUTES**

WRITE: `### DECISIONS`
  WRITE: Verdict — match OUTCOME from Phase 4 exactly.
  WRITE: Conditions for full approval — name each condition explicitly; "address feedback" fails.
  REQUIRE if verdict not APPROVED:
    WRITE: Owner — named role from Phase 0 roster.
    WRITE: Trigger — concrete deliverable or event; "sufficient progress" fails.

WRITE: `### ACTION ITEMS`
  PRINT: one line per item: `[Owner Role] — [specific action] — [deadline]`
  REQUIRE: all three parts; vague actions fail.

WRITE: `### DISSENTING OPINIONS`
  FOR EACH CONDITION or BLOCK stance: WRITE objection citing INERTIA-FINDING-* label, resolution path with concrete trigger and named authority who confirms.
  IF no dissent: PRINT: `No dissent — [one sentence explaining consensus]`

COMMIT Phase 5:
PRINT: `PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.`
ENFORCE: terminal position stated in Phase 5 — no Phase 5 content may follow this commit. This is the final line of the simulation.

---

## V-03 — Single-axis: Phrasing Register — Conversational Framing with C-32 ENFORCE Blocks

**Variation axis**: Phrasing register — the simulation is described in a conversational register ("Here is how this works", "Before we start", "Once everyone has spoken"). The structural machinery — PHASE-N-COMMIT: markers, INERTIA-FINDING labels, STANCE:, CITE:, RESPONDS-TO: — is preserved intact but embedded in less rigid framing. Each PHASE-N-COMMIT: block includes the C-32 blocking assertion in compact inline form.

**Hypothesis**: C-32 requires the commit block to carry an active blocking assertion. The hypothesis is that this assertion can be expressed concisely (`ENFORCE: no Phase N content after this point`) in a conversational-register prompt without requiring the full imperative format of V-01/V-02. The conversational framing tests whether judges reward structural compliance in a more accessible register or penalize the lighter phrasing. Expected score: 138/140 (C-32 satisfied; C-33 not addressed; C-30 partial pass because fill rules are not uniformly verb-first imperative in the conversational register).

---

You are running `org:committee`. Here is how to run this simulation.

---

**Before you start — Phase 0: Committee Declaration**

First, find the committee charter. Look in `.roles/` for a file matching the committee type in the request (ROB, shiproom, or arch-board). Load every named role from that charter and note their documented orientation. If no charter exists, say so and fall back to three Signal defaults: PM, Architect, and an Inertia-Advocate.

Write down:
- Committee Type
- Agenda Item
- Charter Source (the file you loaded, or the fallback note)
- Participants (one per line: `[Role] — [their orientation]`)

Then close this phase:
`PHASE-0-COMMIT: [locked] — Committee Type: [value], [N] participants loaded. Phase 0 closed. ENFORCE: no Phase 0 content after this point.`

---

**Phase 1 — Find the switching costs**

This is the most important phase. Before anyone speaks, you need to understand what the proposal would displace.

Label this block `INVESTIGATION-ATTEMPT-1` and write four named findings:

- `INERTIA-FINDING-A` — What specific workflow, tool, or process currently in production does this agenda item replace? (Be precise — "the existing workflow" fails.)
- `INERTIA-FINDING-B` — What integration surface is at risk? Name the specific systems, APIs, contracts, or downstream consumers.
- `INERTIA-FINDING-C` — Which team's cognitive habits would break, and what specific decision habit do they rely on today? (Name both.)
- `INERTIA-FINDING-D` — What non-obvious switching cost would the proposal author almost certainly have missed? (Specific enough that they would say "I missed that.")

After writing the four findings, check: does INERTIA-FINDING-D genuinely reveal something the author would not have anticipated? Write `GATE-1 Answer: YES` or `GATE-1 Answer: NO` with a one-sentence basis.

If NO: try again. Label the new block `INVESTIGATION-ATTEMPT-2`, rewrite all four findings from a different angle, and check again with `GATE-2`. Keep incrementing the attempt label until you get a YES. Do all of this within Phase 1 before moving forward.

Once you have a YES, the INERTIA-FINDING-A through D labels from that passing attempt are the committee's active record. All downstream CITE: and RESPONDS-TO: references must use these named labels.

Close the phase:
`PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] YES, INERTIA-FINDING-A through D active. Phase 1 closed. ENFORCE: no Phase 1 content after this point.`

---

**Phase 2 — Sort the participants**

Now sort everyone from Phase 0 into three tiers:

- **Tier 1 — CHALLENGERS**: roles whose charter orientation is to interrogate feasibility, risk, or disruption. They speak first.
- **Tier 2 — CONDITIONALS**: roles that would approve only under specific named conditions.
- **Tier 3 — ADVOCATES**: roles aligned with the proposal's goals. They speak last.

Within a tier, break ties by institutional veto authority (higher veto speaks first).

Then run a SORT-CHECK:
```
SORT-CHECK — Test: Tier 1 and Tier 2 both empty?
Result: [YES / NO]
```

If YES, someone is mis-sorted. Name the role, the correct tier, and the reason tied to this specific agenda item and the INERTIA-FINDING findings. Reprint the corrected TIER SORT and run SORT-CHECK again. Repeat until Result is NO.

Close the phase:
`PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO. Phase 2 closed. ENFORCE: no Phase 2 content after this point.`

---

**Phase 3 — Let everyone speak**

Generate participant voices in tier order: Tier 1 first, then Tier 2, then Tier 3.

For each participant, start with a declared stance — a standalone line before any prose:
`STANCE: BLOCK` or `STANCE: CONDITION` or `STANCE: APPROVE`

Then write 2-4 sentences from their charter-documented perspective on this specific agenda item. Their prose cannot soften, qualify, or contradict the declared stance.

For Tier 1 voices: ground the concern in a named INERTIA-FINDING label where relevant.
For Tier 2 voices: name the specific condition required for approval. "Address concerns" is not specific enough.
For Tier 3 voices, add two additional fields before the endorsement prose:
- `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding that supports the endorsement]`
- `RESPONDS-TO: "[specific named concern]" — [one sentence addressing it]`

If all voices end up as APPROVE — that is a signal the Phase 2 sort was wrong. Reopen Phase 2, fix the tier assignments, rerun the SORT-CHECK, and regenerate Phase 3 voices.

At least one STANCE: CONDITION or STANCE: BLOCK must be present.

Close the phase:
`PHASE-3-COMMIT: [locked] — All voices written Tier 1 → 2 → 3, one or more CONDITION/BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: present. Phase 3 closed. ENFORCE: no Phase 3 content after this point.`

---

**Phase 4 — Count the votes**

After the last voice, print a standalone tally line:
`TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK`

Count one entry per participant by their declared STANCE. Derive the outcome:
- All APPROVE → APPROVED
- Any CONDITION, no BLOCK → APPROVED WITH CONDITIONS
- Any BLOCK → BLOCKED or DEFERRED

Print: `OUTCOME: [value]`

Close the phase:
`PHASE-4-COMMIT: [locked] — TALLY printed, OUTCOME declared. Phase 4 closed. ENFORCE: no Phase 4 content after this point.`

---

**Phase 5 — Write the minutes**

### DECISIONS
Write the Verdict matching the Phase 4 OUTCOME exactly. List each condition for full approval with a specific deliverable or state — "address feedback" fails. If the verdict is not APPROVED, add:
- Owner: a named role from the Phase 0 participant roster
- Trigger: a concrete deliverable or event that causes the committee to re-review

### ACTION ITEMS
One line per item: `[Owner Role] — [specific action] — [deadline]`
All three parts required. Vague actions fail.

### DISSENTING OPINIONS
For each CONDITION or BLOCK stance: write the specific objection (cite INERTIA-FINDING-* by label where applicable), the resolution path (concrete condition + named authority who confirms it is satisfied).
If no dissent: `No dissent — [one sentence explaining why consensus was reached]`

Close the phase:
`PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written; Owner and Trigger present if not APPROVED. Phase 5 closed. Simulation complete. ENFORCE: no Phase 5 content after this point.`

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing — C-33 Citation-Anchor Manifest in PHASE-1-COMMIT

**Variation axes**: Lifecycle emphasis + Inertia framing — combined. C-33 is the primary gap: the PHASE-1-COMMIT must enumerate by name every INERTIA-FINDING label it is locking, producing a citation-anchor manifest that downstream CITE: and RESPONDS-TO: references can be verified against. Inertia framing is elevated: the PHASE-1-COMMIT manifest section gives each finding's label plus a one-phrase content anchor, making the inertia record a first-class locked contract at the phase boundary. C-32 ENFORCE assertions are also present on all commit markers (from V-01).

**Hypothesis**: R11 V-04 showed `Phase 1 commit enumerates locked INERTIA-FINDING tokens by name (citation-anchor manifest)` as a positive excellence signal not captured by any v11 criterion. C-33 codifies this: the PHASE-1-COMMIT must not just say "findings A through D active" — it must list them by name with their locked content. This makes citation authority traceable to the commit itself. The V-04 hypothesis is that making the manifest part of both the skeleton's PHASE-1-COMMIT slot and the PHASE-1 fill rule PRINT instruction is sufficient to satisfy C-33. Combined with C-32 ENFORCE assertions, expected score: 140/140 (C-33 manifest covers the Phase 1 finding enumeration; C-32 ENFORCE covers all commit markers; all other R11 V-05 criteria preserved).

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block including the manifest structure in PHASE-1-COMMIT. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded. | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO → fill INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]

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

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES. Citation-anchor manifest (findings locked for downstream CITE: and RESPONDS-TO: reference):
  INERTIA-FINDING-A: ___  [one-phrase anchor]
  INERTIA-FINDING-B: ___  [one-phrase anchor]
  INERTIA-FINDING-C: ___  [one-phrase anchor]
  INERTIA-FINDING-D: ___  [one-phrase anchor]
Phase 1 closed. | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → reassign: ___ to Tier ___ because ___; corrected TIER SORT follows / NO → valid]

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed. | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

PHASE-3-COMMIT: [locked] — All voices written in tier order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed. | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed. | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

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
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete. | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type is declared before any other content.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0 — no Phase 0 content may appear after it; the next element after PHASE-0-COMMIT: is the Phase 1 header.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded. | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces.
  ENFORCE: precision required — "existing workflow" fails; name the production artifact.

WRITE: INERTIA-FINDING-B — name the integration surface at risk.
  REQUIRE: specific systems, APIs, contracts, or downstream consumers that would break or require renegotiation.

WRITE: INERTIA-FINDING-C — name the team whose cognitive habits would break and the specific decision-making habit they rely on today.
  ENFORCE: name both the team and the habit.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

VALIDATE: each finding carries its named label (INERTIA-FINDING-A through INERTIA-FINDING-D) as the first token.

GATE-1 intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → CONFIRM loop exit; PHASE-1-COMMIT: fills immediately.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1; REPEAT.

REQUIRE: each rewrite labeled with INVESTIGATION-ATTEMPT-N+1; sequential label increments by 1.
CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it.

PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest (findings locked for downstream CITE: and RESPONDS-TO: reference):
  INERTIA-FINDING-A: [one-phrase anchor summarizing the locked finding]
  INERTIA-FINDING-B: [one-phrase anchor summarizing the locked finding]
  INERTIA-FINDING-C: [one-phrase anchor summarizing the locked finding]
  INERTIA-FINDING-D: [one-phrase anchor summarizing the locked finding]
Phase 1 closed. | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

  NOTE: The citation-anchor manifest enumerates every INERTIA-FINDING label by name. Downstream CITE: and RESPONDS-TO: fields are valid only if the named label appears in this manifest. A CITE: reference to a label not listed in the manifest is a citation error.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) — roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems. These roles speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) — roles that hold approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals. These roles speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK fill rule:
PRINT: Test field: `Tier 1 and Tier 2 both empty?`
CONFIRM: Result YES or NO.
IF YES: REASSIGN; name role, target tier, reason tied to active INERTIA-FINDING findings; REPRINT corrected TIER SORT; REPRINT new SORT-CHECK; LOOP until Result NO.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both `Test:` and `Result:` fields.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2 — no Phase 2 content may appear after it.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed. | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2-4 sentences per participant from their charter-documented role orientation.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label from the Phase 1 manifest.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; label must appear in the Phase 1 citation-anchor manifest.

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific finding or concern — generic acknowledgment fails.

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK.
IF all APPROVE: REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK.
ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it.
PRINT: PHASE-3-COMMIT: [locked] — All voices written Tier 1 → 2 → 3, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: present. Phase 3 closed. | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK`
COUNT: each STANCE: from Phase 3 — one entry per participant.
CONFIRM: TALLY is a standalone line.
WRITE: OUTCOME from TALLY; ENFORCE derivation rules.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed. | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; "address feedback" fails.
REQUIRE (verdict not APPROVED): Owner (named role) + Trigger (concrete deliverable or event).
VALIDATE: both Owner and Trigger present.

ACTION ITEMS:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts; vague actions fail.

DISSENTING OPINIONS:
WRITE: dissent substance (cite INERTIA-FINDING-* label from Phase 1 manifest) + resolution path (concrete trigger + named authority).
IF no dissent: PRINT: `No dissent — [one sentence explaining consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete. | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-05 — Full Synthesis: Skeleton + Imperative Fill Rules + C-32 ENFORCE + C-33 Citation-Anchor Manifest (targets 140/140)

**Variation axes**: All axes combined — lifecycle emphasis (skeleton + labeled phases + PHASE-N-COMMIT: terminal markers), imperative phrasing register (verb-first micro-instructions), inertia framing (PHASE-1-COMMIT citation-anchor manifest enumerating all findings), output format (skeleton pre-print + fill sequence), role sequence (Tier 1 → Tier 2 → Tier 3 challenger-first with SORT-CHECK gate).

**Hypothesis**: R11 V-05 scored 136/136 with PHASE-N-COMMIT: [locked] markers (C-31) and imperative fill rules (C-30). The two remaining gaps are C-32 (commit markers need an explicit blocking assertion) and C-33 (PHASE-1-COMMIT needs to enumerate locked INERTIA-FINDING labels as a citation-anchor manifest). V-05 adds both to the R11 V-05 foundation:
1. Every PHASE-N-COMMIT: block in the skeleton and every commit PRINT instruction in the fill rules appends `| ENFORCE: terminal position — NO PHASE N CONTENT MAY FOLLOW THIS LINE` (C-32).
2. The PHASE-1-COMMIT slot in the skeleton contains a citation-anchor manifest structure with INERTIA-FINDING-A through D as named fields; the PHASE-1 fill rule PRINT instruction enumerates all four labels with one-phrase anchors (C-33).
Full synthesis targeting 140/140.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO → fill INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]

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

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest — findings locked; downstream CITE: and RESPONDS-TO: valid only against labels listed here:
    INERTIA-FINDING-A: ___  [one-phrase locked anchor]
    INERTIA-FINDING-B: ___  [one-phrase locked anchor]
    INERTIA-FINDING-C: ___  [one-phrase locked anchor]
    INERTIA-FINDING-D: ___  [one-phrase locked anchor]
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
  Result: ___ [YES → reassign: ___ to Tier ___ because ___; corrected TIER SORT follows / NO → valid]

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

PHASE-3-COMMIT: [locked] — All voices written in tier order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed.
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
[one entry per dissent: Role — objection citing INERTIA-FINDING-* label — resolution path — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type is declared before any other content; an output that proceeds without it fails C-01.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0 — no Phase 0 content may appear after it; the next element after PHASE-0-COMMIT: is the Phase 1 header.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces.
  ENFORCE: precision required — "existing workflow" fails; name the production artifact.

WRITE: INERTIA-FINDING-B — name the integration surface at risk.
  REQUIRE: specific systems, APIs, contracts, or downstream consumers that would break or require renegotiation.

WRITE: INERTIA-FINDING-C — name the team whose cognitive habits would break and the specific decision-making habit they rely on today.
  ENFORCE: name both the team and the habit; "teams in general" fails.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

VALIDATE: each finding carries its named label (INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D) as the first token; a finding written as `(a) [content]` without the INERTIA-FINDING-* label fails C-27.

GATE-1 intra-phase retry loop (C-29):
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → CONFIRM loop exit; PHASE-1-COMMIT: fills immediately; Phase 2 is unconditional.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with the same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block in output; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt; the label must appear in output.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name — not as parenthesized letters.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it; the next element after PHASE-1-COMMIT: is the Phase 2 header.

PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES.
  Citation-anchor manifest — findings locked; downstream CITE: and RESPONDS-TO: valid only against labels listed here:
    INERTIA-FINDING-A: [one-phrase locked anchor — the specific workflow or artifact named in this finding]
    INERTIA-FINDING-B: [one-phrase locked anchor — the integration surface named in this finding]
    INERTIA-FINDING-C: [one-phrase locked anchor — the team and habit named in this finding]
    INERTIA-FINDING-D: [one-phrase locked anchor — the non-obvious switching cost named in this finding]
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

  VALIDATE: every INERTIA-FINDING-* label used in downstream CITE: or RESPONDS-TO: fields must appear in this manifest; a reference to an unlisted label is a citation error.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) — roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems.
  ENFORCE: these roles speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) — roles that hold approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals.
  ENFORCE: these roles speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK fill rule (intra-phase loop):
PRINT: Test field as fixed string: `Tier 1 and Tier 2 both empty?`
CONFIRM: Result — YES or NO.
VALIDATE: if Result YES — REQUIRE reassignment: name the mis-sorted role, name the target tier, state the reason specific to this agenda item and active INERTIA-FINDING findings; RE-PRINT corrected TIER SORT block; RE-PRINT new SORT-CHECK block; LOOP until Result NO.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both `Test:` and `Result:` fields; correct tier ordering without a SORT-CHECK block fails C-25.
CONFIRM: Result NO is the Phase 2 exit condition; Phase 3 fills unconditionally once Result is NO.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2 — no Phase 2 content may appear after it; the next element after PHASE-2-COMMIT: is the Phase 3 header.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2-4 sentences per participant from their charter-documented role orientation responding to this specific agenda item.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label from the Phase 1 citation-anchor manifest where relevant.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; prose before the label fails C-20; content without the named label fails C-27.
VALIDATE: the cited label must appear in the Phase 1 citation-anchor manifest; an unlisted label fails C-33 downstream validation.

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific finding or concern:
  ACCEPTABLE: `INERTIA-FINDING-A: [paraphrase of finding content]`
  ACCEPTABLE: `[Role Name]'s concern that [specific concern text]`
  FAILS: `Inertia concerns have been acknowledged` — generic, no attribution
  FAILS: `The challenger raised valid points` — no specific attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK.
ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it; the next element after PHASE-3-COMMIT: is the Phase 4 header.
PRINT: PHASE-3-COMMIT: [locked] — All voices written in Tier 1 → 2 → 3 order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each STANCE: declaration from Phase 3 — one tally entry per participant categorized by declared STANCE.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it; the next element after PHASE-4-COMMIT: is the Phase 5 header.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; ENFORCE: "address feedback" fails; REQUIRE: a specific deliverable or state.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role from the Phase 0 participant roster responsible for satisfying the blocking condition; ENFORCE: not a team; a specific role.
  WRITE: Trigger — concrete deliverable, evidence artifact, or event that causes committee re-review; ENFORCE: "sufficient progress" fails; a named artifact with named recipient and named authority passes.
VALIDATE: both Owner and Trigger present (C-23); a path missing either field is incomplete.

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts per item; "investigate" alone fails — WRITE: the investigation question, the output artifact, and who receives it.

DISSENTING OPINIONS fill rules:
WRITE: for each participant whose STANCE was CONDITION or BLOCK — dissent substance (specific objection, citing INERTIA-FINDING-* label from the Phase 1 citation-anchor manifest where applicable) and resolution path (concrete condition + named authority who confirms when condition is met).
VALIDATE: cited INERTIA-FINDING-* labels in dissent text match labels enumerated in the Phase 1 citation-anchor manifest.
CONFIRM: resolution path names a concrete trigger, not a general condition.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining why all participants reached consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 — no Phase 5 content may appear after it; it is the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
