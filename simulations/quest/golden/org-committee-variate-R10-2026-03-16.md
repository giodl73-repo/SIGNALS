# org:committee Variations — Round 10
Generated: 2026-03-16
Skill: org:committee
Rubric: v10 (C-30 fill rules phrased as imperative micro-instructions, not descriptive prose; aspirational pool 22 criteria, composite max 134)

R9 reference context: V-05 was the full synthesis targeting 132/132 — skeleton pre-declaration (C-28), INERTIA-FINDING named labels (C-27), intra-phase gate loops (C-29). The remaining gap to 134/134 is C-30: the STEP 2 fill rules in V-05 used descriptive prose ("Read .craft/roles/...", "Name the specific workflow...", "At least one participant must declare..."). C-30 formalizes what V-03's imperative-register variation surfaced as an excellence signal: fill rules must be verb-first imperative commands (PRINT, LOAD, VALIDATE, ENFORCE, REQUIRE, WRITE, CONFIRM) so the skeleton reads as a command set rather than a behavioral description. C-28 requires structural slots to exist as a pre-declared skeleton; C-30 requires each slot's fill instruction to carry a verb-first imperative so the instruction set has uniform normative force.

Variation axes selected:
- Single-axis V-01: Phrasing register — imperative fill rules only (minimal diff from R9 V-05: skeleton identical, STEP 2 fill rules converted to imperative commands)
- Single-axis V-02: Output format — flat imperative command sequence with no skeleton print step (tests whether C-30 is achievable outside the skeleton pattern)
- Single-axis V-03: Inertia framing — investigation as command-driven discovery protocol (C-30 applied specifically to INERTIA-FINDING fill rules)
- Combined V-04: Lifecycle emphasis + C-30 — phase-commit architecture where each phase header includes imperative commit validation
- Combined V-05: Full synthesis — skeleton + imperative fill rules + named labels + loop architecture + phase-commit (targets 134/134)

---

## V-01 — Single-axis: Phrasing Register — Imperative Fill Rules in Skeleton (C-30 primary)

**Variation axis**: Phrasing register — the skeleton structure from R9 V-05 is preserved exactly (same STEP 1, same slot labels, same skeleton layout); the only change is STEP 2's fill rules, which are rewritten as verb-first imperative micro-commands throughout. Every descriptive fill rule ("Read .craft/roles/ for the charter", "Name the specific workflow", "At least one participant must declare") is replaced with an imperative command (LOAD:, WRITE:, VALIDATE:, ENFORCE:, REQUIRE:, CONFIRM:, PRINT:). The skeleton itself is C-28-compliant; C-30 adds the imperative phrasing layer to the fill rule section that C-28 alone cannot enforce.

**Hypothesis**: R9 V-05's STEP 2 fill rules were semantically correct but descriptively phrased — "Name the specific workflow displaced" can be read as guidance while "WRITE: INERTIA-FINDING-A — name the specific workflow displaced" is a command that has exactly one interpretation. The slot is pre-declared (C-28 pass); C-30 requires the fill instruction to be an imperative so the command-set has uniform normative force. Converting STEP 2 descriptive prose to imperative micro-instructions makes the skeleton a complete instruction set: every slot has a pre-declared placeholder and a verb-first fill command. The hypothesis is that this minimal change from R9 V-05 produces a 134/134 score.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, and every `___` placeholder. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

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

[GATE-1 is NO → fill INVESTIGATION-ATTEMPT-2 block within Phase 1 — Phase 2 is unconditional]

### INVESTIGATION-ATTEMPT-2   [fill only if GATE-1 is NO; omit if GATE-1 is YES]

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-2:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[Continue as INVESTIGATION-ATTEMPT-N / GATE-N until Answer: YES. Sequential label increments each time. Phase 2 fills once any GATE-N is YES.]

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

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

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
[one entry per dissent: Role — objection — resolution path — named authority — concrete trigger]
[or: No dissent — [reason]]

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative instructions below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role and its documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found` and LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type declared in the request.
PRINT: Agenda Item — the specific item under review, exactly as stated in the request.
VALIDATE: Committee Type is declared before any other content; an output that proceeds without it fails C-01.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.
WRITE: INERTIA-FINDING-A — the specific workflow, tool, or process currently in production that this agenda item displaces. ENFORCE: precision required — generic descriptions ("existing workflow") fail; name the production artifact.
WRITE: INERTIA-FINDING-B — the named integration surface at risk: specific systems, APIs, contracts, or downstream consumers that would break or require renegotiation.
WRITE: INERTIA-FINDING-C — the team whose cognitive habits would break, and the specific decision-making habit they rely on today. ENFORCE: name both the team and the habit; "teams in general" fails.
WRITE: INERTIA-FINDING-D — the non-obvious switching cost the proposal author almost certainly did not account for. REQUIRE: specific enough that the author would say "I missed that."
VALIDATE: each finding carries its named label (INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D) as the first token; a finding written as `(a) [content]` without the INERTIA-FINDING-* label fails C-27.

GATE-1 fill rule (intra-phase retry loop — C-29):
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer — YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → CONFIRM loop exit; WRITE Phase 2 (Phase 2 slot is pre-declared in the skeleton — it is already present; it is not conditional).
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with same question; re-evaluate.
REQUIRE: each rewrite produces a new labeled block in output; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block in output fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt; the label must appear in output.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record. ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) — roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems. ENFORCE: these roles speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) — roles that hold approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals. ENFORCE: these roles speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK fill rule:
PRINT: Test field as fixed string: `Tier 1 and Tier 2 both empty?`
CONFIRM: Result — YES or NO.
VALIDATE: if Result YES — REQUIRE reassignment: name the mis-sorted role, name the target tier, state the reason specific to this agenda item and active INERTIA-FINDING findings; RE-PRINT corrected TIER SORT block; RE-PRINT new SORT-CHECK block; LOOP until Result NO.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both `Test:` and `Result:` fields; correct tier ordering without a SORT-CHECK block fails C-25.
CONFIRM: Result NO is the Phase 2 exit condition; WRITE Phase 3 unconditionally once Result is NO.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE is a committed declaration — prose must not soften, qualify, or contradict it.
WRITE: 2–4 sentences per participant from their charter-documented role orientation.
REQUIRE: Tier 1 — ground concern in a named INERTIA-FINDING label where relevant.
REQUIRE: Tier 2 — name the specific approval condition precisely; "address concerns" fails.
REQUIRE: Tier 3 — fill CITE: and RESPONDS-TO: before any endorsement prose.

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

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2, revise tier assignments, RE-RUN SORT-CHECK.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice and before Phase 5.
COUNT: each STANCE: declaration from Phase 3 — one tally entry per participant categorized by declared STANCE.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions — name each condition explicitly; "address feedback" fails; REQUIRE: specific deliverable or state.
REQUIRE: Re-entry path when verdict is not APPROVED:
  WRITE: Owner — named role responsible for satisfying the blocking condition; ENFORCE: not a team; a specific role from the Phase 0 participant roster.
  WRITE: Trigger — concrete deliverable, evidence artifact, or event that causes committee re-review; ENFORCE: "sufficient progress" fails; a named artifact with named recipient and named authority passes.
VALIDATE: both Owner and Trigger are required (C-23); a path with only one field is incomplete.

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: named owner, specific deliverable, deadline; "investigate" alone fails — WRITE: the investigation question, the output artifact, and who receives it.

DISSENTING OPINIONS fill rules:
WRITE: for each participant whose STANCE was CONDITION or BLOCK — dissent substance (specific objection, citing INERTIA-FINDING-* label where applicable) and resolution path (concrete condition + named authority who confirms when condition is met).
CONFIRM: resolution path names a concrete trigger, not a general condition.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining why all participants reached consensus]`

---

## V-02 — Single-axis: Output Format — Flat Imperative Command Sequence (no skeleton)

**Variation axis**: Output format — the simulation is structured as a flat sequence of verb-first imperative commands with no skeleton print step. Instead of a two-step (print skeleton, fill skeleton) flow, the simulation is organized as labeled phases whose contents are pure command sequences. Every instruction uses an imperative verb. No descriptive prose appears as an instruction. The phase structure is section headers; everything inside each section is an imperative command.

**Hypothesis**: V-01 tests whether imperative fill rules inside the skeleton format satisfy C-30. V-02 tests whether C-30 can be satisfied in a fundamentally different output format — flat imperative commands without the skeleton print step. If C-30 is a phrasing-register criterion rather than a structural-slot criterion, the same imperative verbs should produce a C-30 pass in a format that omits C-28's skeleton pre-declaration. This tests the independence of C-30 from C-28: C-28 requires a pre-declared skeleton; C-30 requires imperative fill rules within that skeleton; V-02 isolates whether imperative phrasing alone (without skeleton pre-declaration) produces a different scoring profile. Expected outcome: V-02 fails C-28 (no skeleton), passes C-30 (all instructions imperative), demonstrating that C-28 and C-30 are complementary but independent criteria.

---

You are executing `org:committee`. Run the following commands in sequence. Each command produces committed output before the next command executes.

---

**PHASE 0 — DECLARE**

LOAD: `.craft/roles/` for the charter matching this committee type.
ENFORCE: if no charter file exists, LOAD Signal defaults: PM, Architect, Inertia-Advocate.
PRINT:
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item]
Charter: [.craft/roles/ path, or "Signal defaults — no charter found: [roles listed]"]
Participants:
  [Role Name] — [charter-defined orientation in one phrase]
  [one line per loaded role]
```
VALIDATE: Committee Type is declared; an output that omits it fails.

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
IF GATE-N Answer: YES → EXIT LOOP → CONTINUE TO PHASE 2 (unconditional)

IF GATE-N Answer: NO
  → INCREMENT N
  → LABEL: INVESTIGATION-ATTEMPT-N
  → WRITE: INERTIA-FINDING-A through D (rewritten, different angle)
  → GATE: GATE-N (same question, re-evaluate)
  → REPEAT
```

ENFORCE: each iteration produces a new labeled `INVESTIGATION-ATTEMPT-N` block in output; a rewrite without a visible sequential label fails C-22 and C-24.
ENFORCE: Phase 2 executes unconditionally once any GATE-N answers YES; the loop controls when Phase 1 releases, not whether Phase 2 runs.
CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record and the citation anchors for all downstream CITE: and RESPONDS-TO: fields.

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
IF SORT-CHECK Result: NO → EXIT LOOP → CONTINUE TO PHASE 3 (unconditional)

IF SORT-CHECK Result: YES
  → REQUIRE: name the mis-sorted role, target tier, and specific reason given this agenda item and active INERTIA-FINDING findings
  → RE-PRINT corrected TIER SORT block
  → RE-GATE SORT-CHECK
  → REPEAT
```

ENFORCE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields; correct tier ordering without a SORT-CHECK block fails C-25.

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

---

**PHASE 4 — TALLY**

PRINT (after last Phase 3 voice, before Phase 5):
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

COUNT: one entry per participant from Phase 3 STANCE: declarations.
CONFIRM: TALLY is a standalone line, not embedded in prose.

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
[Role] — [objection citing INERTIA-FINDING-* label if applicable] — [resolution path: concrete condition + named authority]
[or: No dissent — [reason]]
```

CONFIRM: each dissent resolution path names a concrete trigger; a path that names only a condition without a trigger is incomplete.

---

## V-03 — Single-axis: Inertia Framing — Investigation as Command-Driven Discovery Protocol (C-30 applied to INERTIA-FINDING fill rules)

**Variation axis**: Inertia framing — the switching-cost investigation is structured as a four-command discovery protocol where each INERTIA-FINDING-* slot has a dedicated imperative discovery command specifying what class of switching cost to find. Instead of a single block of findings, each finding has its own DISCOVER: command with an explicit search directive, a REQUIRE: specificity constraint, and a LABEL: assignment. The investigation section is a named protocol with four command-driven slots and a gate, not a fill-in-the-blanks block.

**Hypothesis**: The inertia framing axis tests how prominently the status-quo competitor is featured. A command-driven discovery protocol makes the investigation's four-slot structure explicit as four distinct search operations, each with its own imperative verb and specificity requirement. INERTIA-FINDING-D — the non-obvious cost — gets a special compound command: `DISCOVER + REQUIRE non-obvious threshold + CONFIRM author-surprise test`. This makes the gate question not an after-the-fact evaluation but a natural conclusion of FINDING-D's own discovery command. Combined with C-30's imperative fill rule requirement, the discovery protocol both features inertia framing prominently (each finding has its own command-level attention) and uses imperative register throughout.

---

You are running `org:committee`. Simulate a committee meeting before the real one. Execute all phases in sequence.

---

### PHASE 0 — COMMITTEE DECLARATION

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role and its documented orientation.
ENFORCE: if no charter exists — LOAD Signal defaults (PM, Architect, Inertia-Advocate); PRINT Charter Source as `Signal defaults — no charter found`.
PRINT: Committee Type (ROB / shiproom / arch-board / other), Agenda Item, Charter Source, Participants roster.

---

### PHASE 1 — SWITCHING-COST INVESTIGATION

Before any participant speaks, execute the four-command discovery protocol below. Label this block `INVESTIGATION-ATTEMPT-1`.

**Discovery Protocol — four commands:**

DISCOVER: `INERTIA-FINDING-A` — the production workflow, tool, or named process this agenda item makes obsolete.
  REQUIRE: name the production artifact precisely; "existing workflow" or "current process" are insufficient.

DISCOVER: `INERTIA-FINDING-B` — the named integration surface at risk.
  REQUIRE: name specific systems, APIs, contracts, or downstream consumers that would break or require renegotiation.

DISCOVER: `INERTIA-FINDING-C` — the team whose cognitive decision-making habits would break.
  REQUIRE: name both the team and the specific habit; "teams in general" fails.

DISCOVER: `INERTIA-FINDING-D` — the non-obvious switching cost.
  REQUIRE: specific enough that the proposal author would say "I missed that."
  ENFORCE: this finding must reveal something the proposal author almost certainly did not account for; a cost that appears in the proposal itself fails the non-obvious threshold.

CONFIRM: `GATE-1` — does INERTIA-FINDING-D clear the non-obvious threshold?
```
GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [one sentence: why this cost clears or fails the non-obvious threshold]
```

**Intra-phase retry loop (C-29):**

ENFORCE: the gate loop runs within Phase 1; Phase 2 executes unconditionally once any GATE-N answers YES.

```
GATE-N Answer: YES → EXIT LOOP; WRITE Phase 2.
GATE-N Answer: NO  → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N; RE-EXECUTE discovery protocol (all four commands, different search angle); CONFIRM: GATE-N; REPEAT.
```

REQUIRE: each retry produces a new labeled `INVESTIGATION-ATTEMPT-N` block in output; a rewrite without a visible sequential label fails C-24.
REQUIRE: each INERTIA-FINDING-* label appears as the first token of its finding line; parenthesized letters without the label name fail C-27.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record and the citation anchors for all downstream references.

---

### PHASE 2 — TIER SORT

ASSIGN: all participants from Phase 0 into three challenger-first tiers:
  ASSIGN Tier 1 (CHALLENGERS): roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems grounded in active INERTIA-FINDING findings.
  ASSIGN Tier 2 (CONDITIONALS): roles that require specific named conditions before approving.
  ASSIGN Tier 3 (ADVOCATES): roles aligned with the proposal's stated goals.
  ENFORCE: Tier 1 voices precede Tier 2; Tier 2 precede Tier 3. Within tier, higher veto authority first.

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
  Result: [YES — reassign [role] to Tier [X] because [reason]; corrected TIER SORT follows / NO — valid]
```

LOOP UNTIL: SORT-CHECK Result: NO — then WRITE Phase 3 unconditionally.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields.

---

### PHASE 3 — PARTICIPANT VOICES

EXECUTE: one block per participant; Tier 1 before Tier 2 before Tier 3.

Voice format:
```
### [Role Name] — Tier [1 / 2 / 3]
STANCE: [BLOCK / CONDITION / APPROVE]
[2–4 sentences from charter-documented role orientation responding to the agenda item]
```

ENFORCE: STANCE: is a standalone labeled declaration before prose; prose must not soften or contradict it.
REQUIRE Tier 1: ground concern in a named INERTIA-FINDING label.
REQUIRE Tier 2: name the specific approval condition.
REQUIRE Tier 3: write CITE: and RESPONDS-TO: before endorsement prose:

```
CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]
RESPONDS-TO: "[INERTIA-FINDING-[A/B]: paraphrase, or [Role]'s concern that [text]]" — [one sentence addressing it]
```

ENFORCE: CITE: label is first element after `CITE:`; RESPONDS-TO: must name and quote a specific concern, not acknowledge generically.
VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 re-sort.

---

### PHASE 4 — TALLY

PRINT (after last Phase 3 voice, before Phase 5):
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

COUNT: one entry per participant from their Phase 3 STANCE: declaration.

---

### PHASE 5 — MINUTES

PRINT:
```
### DECISIONS
Verdict: [OUTCOME from Phase 4]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role from Phase 0 roster]
  Trigger: [concrete deliverable or event — not vague]
```

VALIDATE: both Owner and Trigger required when verdict is not APPROVED (C-23).

PRINT:
```
### ACTION ITEMS
[Owner Role] — [specific action] — [deadline]
[one line per item]
```

REQUIRE: named owner, specific deliverable, deadline per item.

PRINT:
```
### DISSENTING OPINIONS
[Role] — [objection citing INERTIA-FINDING-* label if applicable] — [resolution path: concrete condition + named confirming authority]
[or: No dissent — [reason]]
```

---

## V-04 — Combined: Lifecycle Emphasis + C-30 — Phase-Commit Architecture with Imperative Fill Rules

**Variation axes**: Lifecycle emphasis (explicit phase-commit architecture where each phase ends with a named COMMIT: statement declaring what was produced) + C-30 (all fill instructions are imperative micro-commands). V-04 makes the phase-commit structure the primary design axis: each phase header is followed by imperative fill commands, and each phase ends with a `COMMIT Phase N:` statement that imperatively validates what was written before releasing to the next phase. The COMMIT: statement serves as both a phase boundary marker (C-26) and a structural validation (bridges C-30 with C-26's sequential labeled phase requirement).

**Hypothesis**: Phase-commit architecture addresses a failure mode distinct from skeleton omission: a simulation that produces all required content but blurs phase boundaries or omits a phase header. The COMMIT: statement at the end of each phase imperatively declares the phase's contribution — `COMMIT Phase 0: Committee Type printed, Charter Source printed, Participants roster printed` — making both C-26 (sequential labeled phases) and C-30 (imperative instruction register) structurally enforced within the same mechanism. If the COMMIT: statement is itself an imperative command that names what was produced, the model must have produced it to write the commit. Combined with imperative fill rules throughout, this variant creates a self-auditing simulation: every phase instructs with verbs and commits with verbs.

---

You are running `org:committee`. Execute five phases in sequence. Each phase ends with a COMMIT: statement. Phase outputs are commitments.

---

### PHASE 0 — COMMITTEE DECLARATION

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter exists — LOAD Signal defaults (PM, Architect, Inertia-Advocate); WRITE Charter Source as `Signal defaults — no charter found`.
PRINT: Committee Type (ROB / shiproom / arch-board / other).
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — path used or fallback declaration.
PRINT: Participants — one line per role; format `[Role Name] — [charter-defined orientation]`.
VALIDATE: Committee Type declared; proceeding without it fails C-01.

COMMIT Phase 0: Committee Type, Agenda Item, Charter Source, and Participants roster are written.

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
  IF YES → EXIT LOOP; proceed to COMMIT Phase 1.
  IF NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N; WRITE: four new INERTIA-FINDING-* labels (different angle); GATE: GATE-N; re-evaluate; REPEAT.

REQUIRE: each retry produces a new labeled `INVESTIGATION-ATTEMPT-N` block in output; a rewrite without a visible sequential label fails C-24.
CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.

COMMIT Phase 1: INVESTIGATION-ATTEMPT-N complete, GATE-N answered YES, INERTIA-FINDING-A through D active as committee record citation anchors.

---

### PHASE 2 — TIER SORT

ENFORCE: Phase 2 contains an intra-phase sort validation loop. Phase 3 is always reached once SORT-CHECK answers NO.

ASSIGN: all Phase 0 participants into tiers using charter orientations and active INERTIA-FINDING findings:
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
  Result: [YES — reassign [role] to Tier [X] because [reason specific to this agenda item and active findings]; corrected TIER SORT follows / NO — valid]
```

LOOP UNTIL: SORT-CHECK Result: NO:
  IF NO → EXIT LOOP; proceed to COMMIT Phase 2.
  IF YES → REQUIRE reassignment with role name, target tier, and specific reason; RE-PRINT corrected TIER SORT block; RE-GATE SORT-CHECK; REPEAT.

ENFORCE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields.

COMMIT Phase 2: TIER SORT and SORT-CHECK complete, Result is NO, challenger-first ordering confirmed.

---

### PHASE 3 — PARTICIPANT VOICES

EXECUTE: one voice block per participant; Tier 1 → Tier 2 → Tier 3.

For each participant:

PRINT: `### [Role Name] — Tier [1 / 2 / 3]`
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before prose.
VALIDATE: STANCE: is a committed declaration; prose must not soften, qualify, or contradict it.
WRITE: 2–4 sentences from charter-documented role orientation responding to this agenda item and relevant INERTIA-FINDING labels.

REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label.
REQUIRE (Tier 2): name the specific condition for approval; "address concerns" fails.
REQUIRE (Tier 3): write CITE: and RESPONDS-TO: before endorsement prose:
  PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [finding content supporting endorsement]`
  PRINT: `RESPONDS-TO: "[INERTIA-FINDING-[A/B]: paraphrase or [Role]'s concern that [text]]" — [one sentence addressing it]`
  ENFORCE: CITE: label is first element after `CITE:`; prose before label fails C-20.
  ENFORCE: RESPONDS-TO: must quote a specific named concern; generic acknowledgment fails C-21.

VALIDATE: at least one STANCE: CONDITION or STANCE: BLOCK in Phase 3; all-APPROVE triggers Phase 2 re-sort.

COMMIT Phase 3: all participant voices written in Tier 1 → 2 → 3 order; at least one CONDITION or BLOCK confirmed; CITE: and RESPONDS-TO: fields present for all Tier 3 participants.

---

### PHASE 4 — TALLY

PRINT (after last Phase 3 voice):
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

COUNT: one entry per participant from Phase 3 STANCE: declarations.
CONFIRM: TALLY appears as a standalone line before Phase 5; not embedded in prose.

COMMIT Phase 4: TALLY line printed, OUTCOME declared.

---

### PHASE 5 — MINUTES

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4.
WRITE: Conditions for full approval — name each condition explicitly; "address feedback" fails.
REQUIRE: when verdict is not APPROVED — write both:
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
REQUIRE: all three parts per item; "investigate further" alone is not a specific action.

DISSENTING OPINIONS fill rules:
WRITE: for each CONDITION or BLOCK STANCE: dissent substance (specific objection citing INERTIA-FINDING-* label if applicable) and resolution path (concrete condition + named confirming authority).
CONFIRM: resolution path names a concrete trigger.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence: why consensus emerged]`

COMMIT Phase 5: DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present in re-entry path if applicable.

---

## V-05 — Combined: Full Synthesis — Skeleton + Imperative Fill Rules + Named Labels + Loop Architecture + Phase-Commit (targets 134/134)

**Variation axes**: Output format (skeleton pre-declaration — C-28) + phrasing register (imperative micro-instructions throughout all fill rules — C-30) + inertia framing (INERTIA-FINDING named labels as primary citation anchors — C-27) + lifecycle emphasis (intra-phase gate loops — C-29) + phase-commit (COMMIT: statements validate each phase's output). V-05 is the R10 golden synthesis: the skeleton pre-declares every structural slot (C-28); every slot's fill rule is a verb-first imperative command (C-30); INERTIA-FINDING-* labels are the primary citation anchors from discovery through dissent (C-27); phase gates are intra-phase retry loops that cannot terminate the simulation (C-29); COMMIT: statements validate each phase before releasing to the next.

**Hypothesis**: R9 V-05 was the R9 golden synthesis targeting 132/132. The only gap to 134/134 was C-30: the skeleton's STEP 2 fill rules were semantically correct but descriptively phrased. V-05 replaces all STEP 2 descriptive fill rules with imperative micro-commands (PRINT:, LOAD:, VALIDATE:, ENFORCE:, REQUIRE:, WRITE:, CONFIRM:) while preserving the entire STEP 1 skeleton structure. Additionally, V-05 adds COMMIT: statements to each phase as an imperative validation that bridges C-26 (sequential labeled phases) and C-30 (imperative register). The hypothesis is that this is the minimal change from R9 V-05 needed to close the C-30 gap and that the COMMIT: additions also strengthen C-26 scoring. Target: 134/134.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every COMMIT: statement. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]

COMMIT Phase 0: Committee Type ___, Agenda Item ___, Charter Source ___, Participants roster printed.

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

COMMIT Phase 1: INVESTIGATION-ATTEMPT-___ complete, GATE-___ answered YES, INERTIA-FINDING-A through D active as citation anchors.

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

COMMIT Phase 2: TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

COMMIT Phase 3: all voices written in tier order, at least one CONDITION or BLOCK confirmed, Tier 3 CITE: and RESPONDS-TO: fields present.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

COMMIT Phase 4: TALLY line printed, OUTCOME declared.

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

COMMIT Phase 5: DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.craft/roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type is declared before any other content; an output that proceeds without it fails C-01.
CONFIRM: COMMIT Phase 0 — write the commit line with each field populated.

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
  IF GATE-N Answer: YES → CONFIRM loop exit; WRITE Phase 2 (Phase 2 is pre-declared in the skeleton — it is present unconditionally; the gate controls when Phase 1 releases, not whether Phase 2 runs).
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with the same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block in output; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt; the label must appear in output, not only in reasoning.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name — not as parenthesized letters.
CONFIRM: COMMIT Phase 1 — write the commit line with attempt number and gate number populated.

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
CONFIRM: COMMIT Phase 2 — write the commit line.

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
CONFIRM: COMMIT Phase 3 — write the commit line, confirming at least one CONDITION or BLOCK and Tier 3 fields present.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each STANCE: declaration from Phase 3 — one tally entry per participant categorized by declared STANCE.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
CONFIRM: COMMIT Phase 4 — write the commit line.

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
CONFIRM: COMMIT Phase 5 — write the commit line.
