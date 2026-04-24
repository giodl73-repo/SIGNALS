# org:committee Variations — Round 11
Generated: 2026-03-16
Skill: org:committee
Rubric: v11 (C-31 phase transitions carry explicit commit declarations before the next phase begins; aspirational pool 23 criteria, composite max 136)

R10 reference context: V-05 was the R10 golden synthesis targeting 134/134 — skeleton pre-declaration (C-28), imperative fill rules (C-30), INERTIA-FINDING named labels (C-27), intra-phase gate loops (C-29). V-04 and V-05 both had `COMMIT Phase N:` statements. The gap to 136/136 is C-31: those COMMIT statements validated phase content but did not declare a structural lock. C-31 requires the commit to be a named terminal element (`PHASE-N-COMMIT:`, `COMMIT: Phase N complete — locked`) that makes retroactive modification of Phase N output architecturally impossible — without it, the boundary between "phase content generation complete" and "next phase begins" is defined only by the arrival of the next header, which subsequent phases can exploit to soften prior output without violating any existing rule.

Variation axes selected:
- Single-axis V-01: Lifecycle emphasis — PHASE-N-COMMIT: locked terminal markers (minimal diff from R10 V-05: skeleton and fill rules identical; only COMMIT lines upgraded to locked syntax + ENFORCE: terminal position rule)
- Single-axis V-02: Output format — flat command sequence with PHASE-N-COMMIT: terminal markers (no skeleton; tests whether C-31 is satisfiable outside the skeleton format)
- Single-axis V-03: Phrasing register — conversational framing with structured PHASE-N-COMMIT: locked blocks (tests C-31 compliance in a less rigid register)
- Combined V-04: Lifecycle emphasis + Inertia framing — PHASE-N-COMMIT: declarations enumerate locked INERTIA-FINDING citation anchors explicitly, making the inertia record part of the terminal lock
- Combined V-05: Full synthesis — skeleton + imperative fill rules + PHASE-N-COMMIT: locked terminal markers as terminal phase elements (targets 136/136)

---

## V-01 — Single-axis: Lifecycle Emphasis — PHASE-N-COMMIT: Locked Terminal Markers (C-31 primary)

**Variation axis**: Lifecycle emphasis — the R10 V-05 skeleton and fill rules are preserved exactly; the only change is upgrading all `COMMIT Phase N:` declarations to `PHASE-N-COMMIT: [locked]` syntax and adding an ENFORCE rule to each phase's fill instructions: the PHASE-N-COMMIT: marker is the terminal element; no Phase N content may appear after it; the next element after it is the Phase N+1 header. In the skeleton, each phase's commit line is replaced with the locked format showing what fields are being locked. In STEP 2, each `CONFIRM: COMMIT Phase N` is replaced with `ENFORCE: PHASE-N-COMMIT: is terminal + PRINT: PHASE-N-COMMIT: [locked] — [fields]`.

**Hypothesis**: R10 V-05 passed C-30 (imperative fill rules) and C-26 (labeled sequential phases) but the COMMIT Phase N: statements were framed as validation summaries rather than structural locks. C-31 is not satisfied by a validation summary that happens to appear at the end of a phase — it requires a named terminal element whose position enforces that Phase N output is closed. The difference is `COMMIT Phase 3: all voices written` (a summary, which can appear anywhere and doesn't prevent post-commit content) vs `PHASE-3-COMMIT: [locked] — Voices closed` (a terminal element that, by its label and ENFORCE rule, makes any subsequent Phase 3 content a structural violation). The minimal hypothesis: converting COMMIT to PHASE-N-COMMIT: [locked] + adding the ENFORCE: terminal position rule closes the C-31 gap while preserving the 134-pt score from all R10 criteria. Target: 136/136.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: marker. Do not fill any values in this step.

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

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES, INERTIA-FINDING-A through D active as citation anchors. Phase 1 closed.

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

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.

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

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed.

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
  IF GATE-N Answer: YES → CONFIRM loop exit; the PHASE-1-COMMIT: fills immediately; Phase 2 is unconditional.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with the same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block in output; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt; the label must appear in output.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name — not as parenthesized letters.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it; the next element after PHASE-1-COMMIT: is the Phase 2 header.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES, INERTIA-FINDING-A through D from attempt [N] active as citation anchors. Phase 1 closed.

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

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2–4 sentences per participant from their charter-documented role orientation responding to this specific agenda item.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label where relevant.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; prose before the label fails C-20; content without the named label fails C-27.

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

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each STANCE: declaration from Phase 3 — one tally entry per participant categorized by declared STANCE.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it; the next element after PHASE-4-COMMIT: is the Phase 5 header.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; ENFORCE: "address feedback" fails; REQUIRE: a specific deliverable or state.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role responsible for satisfying the blocking condition; ENFORCE: not a team; a specific role from the Phase 0 participant roster.
  WRITE: Trigger — concrete deliverable, evidence artifact, or event that causes committee re-review; ENFORCE: "sufficient progress" fails; a named artifact with named recipient and named authority passes.
VALIDATE: both Owner and Trigger present (C-23); a path missing either field is incomplete.

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts per item; "investigate" alone fails — WRITE: the investigation question, the output artifact, and who receives it.

DISSENTING OPINIONS fill rules:
WRITE: for each participant whose STANCE was CONDITION or BLOCK — dissent substance (specific objection, citing INERTIA-FINDING-* label where applicable) and resolution path (concrete condition + named authority who confirms when condition is met).
CONFIRM: resolution path names a concrete trigger, not a general condition.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining why all participants reached consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 — no Phase 5 content may appear after it; it is the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.

---

## V-02 — Single-axis: Output Format — Flat Command Sequence with PHASE-N-COMMIT: Terminal Markers (no skeleton)

**Variation axis**: Output format — the simulation is structured as a flat sequence of labeled phases, each containing verb-first imperative commands, with no skeleton print step. Each phase section ends with a `PHASE-N-COMMIT: [locked]` terminal marker before the next phase header. This is R10 V-02 extended with C-31 compliance: the flat command format is preserved exactly, and PHASE-N-COMMIT: markers are added as the terminal element of each phase block.

**Hypothesis**: R10 V-02 tested whether C-30 (imperative fill rules) could be satisfied without the skeleton format — it failed C-28 (no pre-declared skeleton) but passed C-30 (all instructions imperative). V-02 in R11 extends this: does a flat command sequence satisfy C-31 when PHASE-N-COMMIT: markers are added as terminal elements? The expected scoring profile: V-02 fails C-28 (no skeleton), passes C-30 (imperative commands throughout), passes C-31 (PHASE-N-COMMIT: terminal markers present and enforced). This confirms that C-31 is structurally independent of C-28: the commit marker mechanism works in both skeleton and flat-command formats, but the flat-command format cannot satisfy the pre-declaration requirement of C-28.

---

You are executing `org:committee`. Run the following phases in sequence. Each phase ends with a PHASE-N-COMMIT: terminal marker before the next phase begins.

---

**PHASE 0 — DECLARE**

LOAD: `.roles/` for the charter matching this committee type.
ENFORCE: if no charter file exists, LOAD Signal defaults: PM, Architect, Inertia-Advocate.
PRINT:
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item]
Charter: [.roles/ path, or "Signal defaults — no charter found: [roles listed]"]
Participants:
  [Role Name] — [charter-defined orientation in one phrase]
  [one line per loaded role]
```
VALIDATE: Committee Type is declared; an output that omits it fails.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0; no Phase 0 content may follow it.
PRINT: `PHASE-0-COMMIT: [locked] — Committee Type, Charter Source, and Participants roster declared. Phase 0 closed.`

---

**PHASE 1 — INVESTIGATE**

LABEL: `INVESTIGATION-ATTEMPT-1`

WRITE:
```
INERTIA-FINDING-A: [the production workflow this agenda item displaces — name it precisely]
INERTIA-FINDING-B: [the named integration surface at risk — specific systems, APIs, contracts]
INERTIA-FINDING-C: [the team whose cognitive habits break — name team and specific habit]
INERTIA-FINDING-D: [the non-obvious switching cost — the one the proposal author missed]
```

ENFORCE: each finding carries its INERTIA-FINDING-* label as the first token; parenthesized letters `(a)` without the label name fail C-27.

GATE:
```
GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [one sentence]
```

LOOP UNTIL: GATE-N Answer: YES

```
IF GATE-N Answer: YES → EXIT LOOP → PROCEED TO PHASE-1-COMMIT:

IF GATE-N Answer: NO
  → INCREMENT N
  → LABEL: INVESTIGATION-ATTEMPT-N
  → WRITE: INERTIA-FINDING-A through D (rewritten, different angle)
  → GATE: GATE-N (same question, re-evaluate)
  → REPEAT
```

ENFORCE: each iteration produces a new labeled `INVESTIGATION-ATTEMPT-N` block in output; a rewrite without a visible sequential label fails C-22 and C-24.
ENFORCE: Phase 2 executes unconditionally once any GATE-N answers YES; the loop controls when Phase 1 releases, not whether Phase 2 runs.
CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active citation anchors for all downstream CITE: and RESPONDS-TO: fields.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1; no Phase 1 content may follow it.
PRINT: `PHASE-1-COMMIT: [locked] — INVESTIGATION-ATTEMPT-[N] complete, GATE-[N] YES, INERTIA-FINDING-A through D from attempt [N] active as citation anchors. Phase 1 closed.`

---

**PHASE 2 — SORT**

ASSIGN: all Phase 0 participants into three tiers:
  ASSIGN Tier 1 — CHALLENGERS: roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems. ENFORCE: these speak before all others.
  ASSIGN Tier 2 — CONDITIONALS: roles that hold approval pending specific named conditions.
  ASSIGN Tier 3 — ADVOCATES: roles aligned with the proposal's stated goals. ENFORCE: these speak last.
  ENFORCE: tie-break — higher institutional veto authority first within tier.

PRINT:
```
TIER SORT:
  Tier 1 — CHALLENGERS: [roles]
  Tier 2 — CONDITIONALS: [roles]
  Tier 3 — ADVOCATES: [roles]
  Tie-break: higher veto authority first within tier
```

GATE:
```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES / NO]
```

LOOP UNTIL: SORT-CHECK Result: NO

```
IF SORT-CHECK Result: NO → EXIT LOOP → PROCEED TO PHASE-2-COMMIT:

IF SORT-CHECK Result: YES
  → REQUIRE: name the mis-sorted role, target tier, and specific reason given this agenda item and active INERTIA-FINDING findings
  → RE-PRINT corrected TIER SORT block
  → RE-GATE SORT-CHECK
  → REPEAT
```

ENFORCE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields; correct tier ordering without a SORT-CHECK block fails C-25.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2; no Phase 2 content may follow it.
PRINT: `PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.`

---

**PHASE 3 — VOICES**

EXECUTE: one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3.

FOR EACH PARTICIPANT:

PRINT:
```
### [Role Name] — Tier [1 / 2 / 3]
STANCE: [BLOCK / CONDITION / APPROVE]
[2–4 sentences from charter-documented role orientation. Prose must not soften, qualify, or contradict STANCE:]
```

ENFORCE: STANCE: is a standalone labeled declaration before any prose; a stance that appears only within prose fails C-15.

FOR TIER 1 VOICES:
REQUIRE: ground concern in a named INERTIA-FINDING label where relevant.

FOR TIER 2 VOICES:
REQUIRE: name the specific approval condition precisely; "address concerns" fails.

FOR TIER 3 VOICES:
WRITE: CITE: and RESPONDS-TO: fields before any endorsement prose.

PRINT (Tier 3 only):
```
CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]
RESPONDS-TO: "[named concern — INERTIA-FINDING-[A/B]: [paraphrase] or [Role]'s concern that [text]]" — [one sentence addressing it]
```

ENFORCE: `CITE:` label is the first element after `CITE:`; prose before the label fails C-20.
ENFORCE: `RESPONDS-TO:` must quote a specific named finding or concern; generic acknowledgment fails C-21.
VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK declared; all-APPROVE triggers Phase 2 re-sort.
ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3; no Phase 3 content may follow it.
PRINT: `PHASE-3-COMMIT: [locked] — All voices written in Tier 1 → 2 → 3 order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed.`

---

**PHASE 4 — TALLY**

PRINT (after last Phase 3 voice, before Phase 5):
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

COUNT: one entry per participant from Phase 3 STANCE: declarations.
CONFIRM: TALLY is a standalone line, not embedded in prose.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4; no Phase 4 content may follow it.
PRINT: `PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.`

---

**PHASE 5 — MINUTES**

PRINT:
```
### DECISIONS
Verdict: [matches OUTCOME from Phase 4]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role from Phase 0 roster — not a team]
  Trigger: [concrete deliverable or event — "sufficient progress" fails]
```

VALIDATE: both Owner and Trigger are present when verdict is not APPROVED; a path missing either field fails C-23.

PRINT:
```
### ACTION ITEMS
[Owner Role] — [specific action] — [deadline]
[one line per item]
```

REQUIRE: each item has named owner, specific deliverable, and deadline; "investigate further" alone fails.

PRINT:
```
### DISSENTING OPINIONS
[Role] — [objection citing INERTIA-FINDING-* label if applicable] — [resolution path: concrete condition + named confirming authority]
[or: No dissent — [reason]]
```

CONFIRM: each dissent resolution path names a concrete trigger; a path that names only a condition without a trigger is incomplete.
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the final element of the simulation; nothing may follow it.
PRINT: `PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Simulation complete.`

---

## V-03 — Single-axis: Phrasing Register — Conversational Frame with Structured PHASE-N-COMMIT: Locked Blocks

**Variation axis**: Phrasing register — the main simulation instructions use a more conversational, instructional register (describing what each phase does and why) rather than pure imperative micro-commands, while C-31 compliance is maintained through strictly structured `PHASE-N-COMMIT:` blocks at the terminal position of each phase. Each commit block uses a fixed format: `PHASE-N-COMMIT: [locked] — [summary] | NO PHASE N CONTENT MAY FOLLOW THIS LINE.` The imperative commands (`STANCE:`, `CITE:`, `RESPONDS-TO:`, `INERTIA-FINDING-*`) are preserved as structural slot labels; the surrounding guidance is more readable.

**Hypothesis**: The phrasing register axis tests whether C-31 compliance requires imperative fill rules (C-30) throughout, or whether the commit marker mechanism is structurally independent. A simulation prompt written in conversational register can still satisfy C-31 if the commit blocks are structurally formed and positioned correctly. Expected outcome: V-03 passes C-31 (commit blocks present, terminal, locked), partially passes C-30 (the commit blocks themselves are imperative but surrounding fill guidance uses descriptive prose), passes C-26 (labeled sequential phases). This tests the independence of C-31 from C-30: C-31 is a lifecycle-boundary criterion; C-30 is a fill-rule phrasing criterion; they are complementary but non-overlapping.

---

You are running `org:committee`. Simulate a committee meeting before the real one. Work through each phase below in sequence. Each phase ends with a PHASE-N-COMMIT: marker that locks its output — nothing from that phase may continue past the commit line.

---

### PHASE 0 — COMMITTEE DECLARATION

Start by identifying what kind of committee is meeting and who's in the room. Read `.roles/` to find the charter for this committee type. If no charter file exists, use Signal defaults: PM, Architect, and Inertia-Advocate.

Produce:
- **Committee Type**: ROB, shiproom, arch-board, or the type specified in the request
- **Agenda Item**: the specific item under review
- **Charter Source**: the file path you read, or `Signal defaults — no charter found`
- **Participants**: one line per role, formatted as `[Role Name] — [their orientation in one phrase]`

The committee type must be declared before anything else. An output that jumps straight to participant voices without declaring the committee type fails.

```
PHASE-0-COMMIT: [locked] — Committee Type: [value] | Agenda Item: [value] | Charter Source: [value] | Participants: [N] roles declared. | NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.
```

---

### PHASE 1 — SWITCHING-COST INVESTIGATION

Before anyone speaks, investigate the switching costs this agenda item creates. The goal is to find at least one non-obvious cost the proposal author probably did not account for.

Label your investigation block `INVESTIGATION-ATTEMPT-1`. Produce four findings, each with its named label as the first token:

- **INERTIA-FINDING-A**: the specific production workflow, tool, or process this agenda item displaces
- **INERTIA-FINDING-B**: the named integration surfaces at risk (specific systems, APIs, contracts, downstream consumers)
- **INERTIA-FINDING-C**: the team whose cognitive habits would break, and what specific habit
- **INERTIA-FINDING-D**: the non-obvious switching cost — the one the author missed

Then evaluate:

```
GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [one sentence]
```

**If GATE-1 is NO**: do not stop or wait — label a new block `INVESTIGATION-ATTEMPT-2`, rewrite all four findings from a different angle, and re-evaluate GATE-2 with the same question. Keep incrementing (INVESTIGATION-ATTEMPT-3, GATE-3, etc.) until a gate answers YES. Each attempt must produce a new labeled block visible in output. Phase 2 always runs — the loop controls when Phase 1 releases, not whether Phase 2 runs.

The INERTIA-FINDING-A through D from the passing attempt become the citation anchors for all participant voices downstream. All CITE: and RESPONDS-TO: references must name these labels explicitly (not parenthesized letters).

```
PHASE-1-COMMIT: [locked] — INVESTIGATION-ATTEMPT-[N] complete | GATE-[N]: YES | INERTIA-FINDING-A through D from attempt [N] are locked as citation anchors. | NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.
```

---

### PHASE 2 — TIER SORT

Sort all participants from Phase 0 into three challenger-first tiers based on their charter orientation and the active INERTIA-FINDING findings:

- **Tier 1 — CHALLENGERS**: roles whose orientation interrogates feasibility, risk, or disruption to existing systems. They speak first.
- **Tier 2 — CONDITIONALS**: roles that need specific conditions met before approving. They speak second.
- **Tier 3 — ADVOCATES**: roles aligned with the proposal's goals. They speak last.

Within any tier, higher institutional veto authority speaks first.

Print the sort:
```
TIER SORT:
  Tier 1 — CHALLENGERS: [roles]
  Tier 2 — CONDITIONALS: [roles]
  Tier 3 — ADVOCATES: [roles]
  Tie-break: higher veto authority first within tier
```

Then run the sort check:
```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES / NO]
```

If Result is YES, the sort produced an all-advocate lineup, which is a structural error. Reassign at least one participant to Tier 1 or Tier 2 — name the role, the target tier, and the specific reason given this agenda item and the active findings. Re-print the corrected sort and re-run the SORT-CHECK. Repeat until Result is NO.

```
PHASE-2-COMMIT: [locked] — TIER SORT complete | SORT-CHECK Result: NO | Challenger-first ordering confirmed. | NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.
```

---

### PHASE 3 — PARTICIPANT VOICES

Write one block per participant, strictly in Tier 1 → Tier 2 → Tier 3 order.

For each participant, the block must follow this structure:
```
### [Role Name] — Tier [1 / 2 / 3]
STANCE: [BLOCK / CONDITION / APPROVE]
[2–4 sentences from their charter orientation, responding to the specific agenda item]
```

`STANCE:` is a committed declaration — it appears as a labeled line before prose, and the prose must not soften, qualify, or reverse it.

**Tier 1 participants**: ground at least one concern in a named INERTIA-FINDING label.

**Tier 2 participants**: name the specific approval condition. "Address concerns" is not a condition.

**Tier 3 participants**: before any endorsement prose, write:
```
CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding that supports this endorsement]
RESPONDS-TO: "[INERTIA-FINDING-[X]: paraphrase, or [Role]'s concern that [text]]" — [one sentence addressing it]
```

If all participants land in APPROVE — no CONDITION, no BLOCK — Phase 2 sort is invalid. Go back to Phase 2, reassign tiers, re-run SORT-CHECK, then re-run Phase 3.

```
PHASE-3-COMMIT: [locked] — All voices written in Tier 1 → 2 → 3 order | At least one CONDITION or BLOCK confirmed | Tier 3 CITE: and RESPONDS-TO: fields present. | NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.
```

---

### PHASE 4 — TALLY

After the last Phase 3 voice and before the minutes, print the vote tally:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

Count one entry per participant from their Phase 3 STANCE: declaration. The tally is a standalone line — not buried in prose.

```
PHASE-4-COMMIT: [locked] — TALLY line printed | OUTCOME declared. | NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.
```

---

### PHASE 5 — MINUTES

Produce three sections:

**DECISIONS**: Verdict (must match OUTCOME from Phase 4 exactly), conditions for full approval (name them specifically), and if the verdict is not APPROVED, a re-entry path with a named owner role (from the Phase 0 roster) and a concrete trigger event or deliverable. Both owner and trigger are required — a path missing either is incomplete.

**ACTION ITEMS**: One line per item, formatted `[Owner Role] — [specific action] — [deadline]`. All three parts required. "Investigate further" alone is not a specific action.

**DISSENTING OPINIONS**: For each participant who declared CONDITION or BLOCK: the specific objection (citing INERTIA-FINDING-* label if applicable), and a resolution path naming a concrete trigger and the authority who confirms it is met. If no dissent: write `No dissent — [one sentence explaining why]`.

```
PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written | Owner and Trigger present if verdict not APPROVED. | NO PHASE 5 CONTENT MAY FOLLOW THIS LINE. Simulation complete.
```

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing — PHASE-N-COMMIT: Declarations Enumerate Locked Citation Anchors

**Variation axes**: Lifecycle emphasis (PHASE-N-COMMIT: terminal markers with locked syntax throughout) + inertia framing (the PHASE-1-COMMIT: declaration explicitly enumerates the locked INERTIA-FINDING citation anchors by name, making the investigation record part of the structural commit rather than merely implied by the gate answer). The Phase 1 commit becomes a citation-anchor manifest: `PHASE-1-COMMIT: [locked] — INERTIA-FINDING-A: [brief content token], INERTIA-FINDING-B: [brief content token], INERTIA-FINDING-C: [brief content token], INERTIA-FINDING-D: [brief content token] — all four locked as citation anchors. Phase 1 closed.` Phase 3's commit references which INERTIA-FINDING labels were cited by Tier 3 voices, making the inertia record traceable through the full commit chain.

**Hypothesis**: C-31 requires the commit to be a structural lock on the phase's output. For Phase 1, the output is the INERTIA-FINDING citation record. If the PHASE-1-COMMIT: enumerates the locked findings by name and brief token, a downstream phase cannot silently substitute different findings without the Phase 1 commit being visibly wrong. The inertia-framing axis tests whether this explicit enumeration in the commit marker strengthens both C-31 (commit is unambiguously tied to specific output) and C-12/C-27 (investigation findings are prominently featured throughout the lifecycle, not just in the investigation block). The Phase 3 commit's reference to which INERTIA-FINDING labels were cited creates an end-to-end traceable citation chain: finding → commit → voice citation → phase commit reference.

---

You are running `org:committee`. Execute five phases in sequence. Each phase ends with a PHASE-N-COMMIT: terminal marker. Phase outputs are locked at the commit line — no content from Phase N may appear after its PHASE-N-COMMIT: marker.

---

### PHASE 0 — COMMITTEE DECLARATION

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter exists — LOAD Signal defaults (PM, Architect, Inertia-Advocate); WRITE Charter Source as `Signal defaults — no charter found`.
PRINT: Committee Type (ROB / shiproom / arch-board / other).
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — path used or fallback declaration.
PRINT: Participants — one line per role; format `[Role Name] — [charter-defined orientation]`.
VALIDATE: Committee Type declared before any other content; proceeding without it fails C-01.

ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0 — no Phase 0 content may follow it.
PRINT: `PHASE-0-COMMIT: [locked] — Committee: [type] | Item: [agenda item abbreviated] | Participants: [N] roles loaded from [charter source]. Phase 0 closed.`

---

### PHASE 1 — INVESTIGATION

ENFORCE: Phase 1 contains an intra-phase gate loop. The loop runs entirely within Phase 1. Phase 2 is always reached — the loop controls when Phase 1 releases, not whether Phase 2 runs.

LABEL: `INVESTIGATION-ATTEMPT-1`

WRITE: INERTIA-FINDING-A — specific workflow, tool, or process this agenda item displaces. ENFORCE: production artifact name required; generic descriptions fail.
WRITE: INERTIA-FINDING-B — named integration surface at risk. REQUIRE: specific systems, APIs, contracts, or downstream consumers.
WRITE: INERTIA-FINDING-C — team whose cognitive habits break and the specific habit. REQUIRE: name both team and habit.
WRITE: INERTIA-FINDING-D — non-obvious switching cost the proposal author missed. REQUIRE: specific enough the author would say "I missed that."
VALIDATE: each finding carries its INERTIA-FINDING-* label as the first token; findings without the label name fail C-27.

GATE:
```
GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [one sentence]
```

LOOP UNTIL: GATE-N Answer: YES:
  IF YES → EXIT LOOP; proceed to PHASE-1-COMMIT:.
  IF NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N; WRITE: four new INERTIA-FINDING-* labels (different angle); GATE: GATE-N; re-evaluate; REPEAT.

REQUIRE: each retry produces a new labeled `INVESTIGATION-ATTEMPT-N` block in output; a rewrite without a visible sequential label fails C-24.

ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may follow it.
PRINT: `PHASE-1-COMMIT: [locked] — Attempt [N] | Gate [N]: YES | Anchors locked: INERTIA-FINDING-A: [3-word token], INERTIA-FINDING-B: [3-word token], INERTIA-FINDING-C: [3-word token], INERTIA-FINDING-D: [3-word token]. These four findings are the exclusive citation anchors for all Phase 3 CITE: and RESPONDS-TO: fields. Phase 1 closed.`

---

### PHASE 2 — TIER SORT

ENFORCE: Phase 2 contains an intra-phase sort validation loop. Phase 3 is always reached once SORT-CHECK answers NO.

ASSIGN: all Phase 0 participants into tiers using charter orientations and active INERTIA-FINDING findings from the PHASE-1-COMMIT: anchor record:
  ASSIGN Tier 1 (CHALLENGERS): roles interrogating feasibility, risk, or disruption. ENFORCE: speak first.
  ASSIGN Tier 2 (CONDITIONALS): roles holding approval pending named conditions. ENFORCE: speak second.
  ASSIGN Tier 3 (ADVOCATES): roles aligned with proposal goals. ENFORCE: speak last.
  ENFORCE: tie-break — higher institutional veto authority first within tier.

PRINT:
```
TIER SORT:
  Tier 1 — CHALLENGERS: [roles]
  Tier 2 — CONDITIONALS: [roles]
  Tier 3 — ADVOCATES: [roles]
  Tie-break: higher institutional veto authority first within tier
```

GATE:
```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — reassign [role] to Tier [X] because [reason specific to this agenda item and active PHASE-1-COMMIT: anchors]; corrected TIER SORT follows / NO — valid]
```

LOOP UNTIL: SORT-CHECK Result: NO:
  IF NO → EXIT LOOP; proceed to PHASE-2-COMMIT:.
  IF YES → REQUIRE reassignment with role name, target tier, and specific reason; RE-PRINT corrected TIER SORT block; RE-GATE SORT-CHECK; REPEAT.

ENFORCE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2 — no Phase 2 content may follow it.
PRINT: `PHASE-2-COMMIT: [locked] — TIER SORT complete | SORT-CHECK Result: NO | Order: [Tier1 roles] → [Tier2 roles] → [Tier3 roles]. Phase 2 closed.`

---

### PHASE 3 — PARTICIPANT VOICES

EXECUTE: one voice block per participant; Tier 1 → Tier 2 → Tier 3.

For each participant:

PRINT: `### [Role Name] — Tier [1 / 2 / 3]`
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before prose.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2–4 sentences from charter-documented role orientation responding to this agenda item and the locked PHASE-1-COMMIT: anchor findings.

REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label from the PHASE-1-COMMIT: anchor record.
REQUIRE (Tier 2): name the specific condition for approval; "address concerns" fails.
REQUIRE (Tier 3): write CITE: and RESPONDS-TO: before endorsement prose:
  PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [finding content from PHASE-1-COMMIT: anchor record supporting endorsement]`
  PRINT: `RESPONDS-TO: "[INERTIA-FINDING-[X]: paraphrase from PHASE-1-COMMIT: anchor record, or [Role]'s concern that [text]]" — [one sentence addressing it]`
  ENFORCE: CITE: label is first element after `CITE:`; prose before label fails C-20.
  ENFORCE: RESPONDS-TO: must quote a specific named concern from the PHASE-1-COMMIT: anchor record; generic acknowledgment fails C-21.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK in Phase 3; all-APPROVE triggers Phase 2 re-sort and Phase 3 re-run.

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may follow it.
PRINT: `PHASE-3-COMMIT: [locked] — All voices written in Tier 1 → 2 → 3 order | At least one CONDITION or BLOCK confirmed | Tier 3 cited: [list INERTIA-FINDING labels cited in CITE: fields]. Phase 3 closed.`

---

### PHASE 4 — TALLY

PRINT (after last Phase 3 voice):
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

COUNT: one entry per participant from Phase 3 STANCE: declarations.
CONFIRM: TALLY appears as a standalone line before Phase 5.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may follow it.
PRINT: `PHASE-4-COMMIT: [locked] — TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK | OUTCOME: [value]. Phase 4 closed.`

---

### PHASE 5 — MINUTES

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4.
WRITE: Conditions for full approval — name each condition explicitly; "address feedback" fails.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role from Phase 0 roster responsible for satisfying the blocking condition.
  WRITE: Trigger — concrete deliverable or event causing committee re-review; "sufficient progress" fails.
VALIDATE: Owner and Trigger both present (C-23); a path missing either field is incomplete.

PRINT:
```
### DECISIONS
Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___
```

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts per item.

DISSENTING OPINIONS fill rules:
WRITE: for each CONDITION or BLOCK STANCE: dissent substance (specific objection citing INERTIA-FINDING-* label from PHASE-1-COMMIT: anchor record if applicable) and resolution path (concrete condition + named confirming authority).
CONFIRM: resolution path names a concrete trigger.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence: why consensus emerged]`

ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the final element of the simulation — nothing may follow it.
PRINT: `PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written | Owner and Trigger present if verdict not APPROVED | Simulation complete.`

---

## V-05 — Combined: Full Synthesis — Skeleton + Imperative Fill Rules + PHASE-N-COMMIT: Locked Terminal Markers (targets 136/136)

**Variation axes**: Output format (skeleton pre-declaration — C-28) + phrasing register (imperative micro-instructions throughout all fill rules — C-30) + inertia framing (INERTIA-FINDING named labels as primary citation anchors — C-27) + lifecycle emphasis (intra-phase gate loops — C-29) + phase-commit (PHASE-N-COMMIT: [locked] terminal markers as the final element of each phase — C-31). V-05 is the R11 golden synthesis: the skeleton pre-declares every structural slot including PHASE-N-COMMIT: markers with locked syntax (C-28 + C-31 pre-declaration); every slot's fill rule is a verb-first imperative command (C-30); INERTIA-FINDING-* labels are the primary citation anchors (C-27); phase gates are intra-phase retry loops (C-29); PHASE-N-COMMIT: [locked] markers terminate each phase with an explicit structural lock that prevents retroactive modification.

**Hypothesis**: R10 V-05 targeted 134/134 by combining all R10 criteria. The only gap was C-31: the `COMMIT Phase N:` lines were validation summaries positioned at the end of phases but not framed as structural locks. C-31 is the lifecycle-completeness criterion: C-26 requires labeled phases; C-31 requires each phase to carry a terminal lock so the boundary between "phase complete" and "next phase begins" is a named structural element, not a header gap. V-05 closes this by: (1) upgrading all COMMIT Phase N: lines in the skeleton to PHASE-N-COMMIT: [locked] format, (2) adding ENFORCE: PHASE-N-COMMIT: is the terminal element — no Phase N content may follow it, (3) making the PHASE-N-COMMIT: fill rule itself an imperative PRINT: command so C-30 and C-31 are jointly satisfied by the same mechanism. Target: 136/136.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: marker with its [locked] syntax. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded. Phase 0 closed.

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

PHASE-1-COMMIT: [locked] — INVESTIGATION-ATTEMPT-___ complete, GATE-___ answered YES, INERTIA-FINDING-A through D from attempt ___ active as citation anchors. Phase 1 closed.

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

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.

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

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Simulation complete.

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
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded. Phase 0 closed.

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
  IF GATE-N Answer: YES → CONFIRM loop exit; WRITE PHASE-1-COMMIT: (Phase 2 is pre-declared in the skeleton — it is present unconditionally; the gate controls when Phase 1 releases, not whether Phase 2 runs).
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with the same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block in output; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt; the label must appear in output, not only in reasoning.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name — not as parenthesized letters.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it; the next element after PHASE-1-COMMIT: is the Phase 2 header.
PRINT: PHASE-1-COMMIT: [locked] — INVESTIGATION-ATTEMPT-[N] complete, GATE-[N] answered YES, INERTIA-FINDING-A through D from attempt [N] active as citation anchors. Phase 1 closed.

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

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2–4 sentences per participant from their charter-documented role orientation responding to this specific agenda item.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label where relevant.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; prose before the label fails C-20; content without the named label fails C-27.

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific finding or concern:
  ACCEPTABLE: `INERTIA-FINDING-A: [paraphrase of finding content]`
  ACCEPTABLE: `[Role Name]'s concern that [specific concern text]`
  FAILS: `Inertia concerns have been acknowledged` — generic, no attribution
  FAILS: `The challenger raised valid points` — no specific attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK; RE-EXECUTE Phase 3.
ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it; the next element after PHASE-3-COMMIT: is the Phase 4 header.
PRINT: PHASE-3-COMMIT: [locked] — All voices written in Tier 1 → 2 → 3 order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present. Phase 3 closed.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each STANCE: declaration from Phase 3 — one tally entry per participant categorized by declared STANCE.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it; the next element after PHASE-4-COMMIT: is the Phase 5 header.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; ENFORCE: "address feedback" fails; REQUIRE: a specific deliverable or state.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role responsible for satisfying the blocking condition; ENFORCE: not a team; a specific role from the Phase 0 participant roster.
  WRITE: Trigger — concrete deliverable, evidence artifact, or event that causes committee re-review; ENFORCE: "sufficient progress" fails; a named artifact with named recipient and named authority passes.
VALIDATE: both Owner and Trigger present (C-23); a path missing either field is incomplete.

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts per item; "investigate" alone fails — WRITE: the investigation question, the output artifact, and who receives it.

DISSENTING OPINIONS fill rules:
WRITE: for each participant whose STANCE was CONDITION or BLOCK — dissent substance (specific objection, citing INERTIA-FINDING-* label where applicable) and resolution path (concrete condition + named authority who confirms when condition is met).
CONFIRM: resolution path names a concrete trigger, not a general condition.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining why all participants reached consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the final element of the simulation — no content may appear after it.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Simulation complete.
