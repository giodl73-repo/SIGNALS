# org:committee Variations — Round 13
Generated: 2026-03-16
Skill: org:committee
Rubric: v13 (C-34 Phase 1 commit manifest entries carry content-anchor suffixes; C-35 Phase 3 commit enumerates locked stance tokens as vote-anchor manifest; aspirational pool 27 criteria, composite max 144)

R12 reference context: V-05 was the R12 golden synthesis targeting 140/140 — skeleton pre-declaration (C-28), imperative fill rules (C-30), INERTIA-FINDING named labels (C-27), intra-phase gate loops (C-29), PHASE-N-COMMIT: [locked] terminal markers (C-31), active ENFORCE blocking assertions (C-32), PHASE-1-COMMIT citation-anchor manifest with one-phrase anchors per label (C-33). The gap to 144/144 is C-34 and C-35. C-34: R12 V-05 includes `[one-phrase locked anchor]` placeholders in the skeleton and fill rules but has no explicit VALIDATE rule enforcing that each manifest entry carries readable anchor content — adding that rule closes C-34 unambiguously. C-35: the PHASE-3-COMMIT commits only "at least one CONDITION or BLOCK confirmed" (a Boolean assertion, not a per-participant manifest) — adding a vote-anchor manifest enumerating every `[Role Name] STANCE-TOKEN` individually to the PHASE-3-COMMIT slot and fill rule closes C-35 and makes Phase 4 TALLY derivable from the commit declaration rather than re-parsed from Phase 3 prose.

Variation axes selected:
- Single-axis V-01: Lifecycle emphasis — minimal diff from R12 V-05: upgrade PHASE-3-COMMIT in skeleton and fill rules to enumerate per-participant stance tokens as vote-anchor manifest (C-35 primary); add VALIDATE for C-34 content-anchor specificity in PHASE-1 fill rules.
- Single-axis V-02: Output format — flat command sequence with C-35 vote-anchor manifest in PHASE-3 commit instruction (no skeleton pre-declaration; tests whether C-35 is satisfiable outside skeleton format).
- Single-axis V-03: Phrasing register — conversational framing with structured PHASE-N-COMMIT blocks; includes C-35 vote-anchor manifest requirement in PHASE-3-COMMIT (tests C-35 compliance in less rigid register).
- Combined V-04: Lifecycle emphasis + Inertia framing — full skeleton with elevated inertia framing; PHASE-1-COMMIT gets explicit VALIDATE for C-34 anchor content; PHASE-3-COMMIT gets vote-anchor manifest (C-35); the inertia record is treated as a first-class named artifact throughout.
- Full synthesis V-05: All axes combined — skeleton + imperative fill rules + C-32 ENFORCE + C-33 manifest + C-34 anchor VALIDATE + C-35 vote-anchor manifest + role sequence with explicit tie-break + inertia framing elevation (targets 144/144).

---

## V-01 — Single-Axis: Lifecycle Emphasis — C-35 Vote-Anchor Manifest + C-34 VALIDATE

**Variation axis**: Lifecycle emphasis — minimal diff from R12 V-05. Two targeted upgrades: (1) PHASE-3-COMMIT in skeleton and fill rules gains a per-participant stance manifest replacing the Boolean "at least one CONDITION or BLOCK confirmed" assertion; (2) PHASE-1 fill rules gain an explicit VALIDATE rule for C-34 content-anchor specificity.

**Hypothesis**: R12 V-05 scored 140/140 against v12 rubric. Against v13, it likely passes C-34 via the `[one-phrase locked anchor]` placeholder but lacks an explicit enforcement rule — the VALIDATE closes that gap cleanly. C-35 is definitively absent: PHASE-3-COMMIT needs a per-participant `[Role] STANCE-TOKEN` manifest. Two surgical additions to R12 V-05 should reach 144/144 without disturbing any passing criteria.

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

PHASE-3-COMMIT: [locked] — Stance manifest (one entry per participant, derived from locked STANCE: declarations above):
  [___] ___
  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]
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

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.craft/roles/` path used, or fallback declaration.
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

VALIDATE: each manifest entry carries a content anchor — a keyword, title, or identifying fragment that makes the finding identifiable without reading Phase 1 prose; a bare-label entry (`INERTIA-FINDING-A:` with no following anchor text) fails C-34.

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

PRINT: PHASE-3-COMMIT: [locked] — Stance manifest (one entry per participant, derived from locked STANCE: declarations above):
  [Role Name] STANCE-TOKEN
  [Role Name] STANCE-TOKEN
  [one line per participant; format: [Role Name] BLOCK / CONDITION / APPROVE]
All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

VALIDATE: Phase 4 TALLY is derived by counting entries in this stance manifest by token; a tally that diverges from this manifest count is a C-35 citation error.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each entry in the Phase 3 stance manifest — one tally count per STANCE-TOKEN category.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
VALIDATE: TALLY counts match the Phase 3-COMMIT stance manifest exactly; mismatch fails C-35.
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

---

## V-02 — Single-Axis: Output Format — Flat Command Sequence with C-35 Vote-Anchor Manifest

**Variation axis**: Output format — flat command sequence without skeleton pre-declaration (no STEP 1 / STEP 2 split). All structural requirements — phases, labels, commit markers, ENFORCE assertions, manifest patterns — are expressed as direct imperative commands in a single execution sequence. Tests whether C-34 and C-35 are satisfiable without the skeleton pre-declaration architecture of C-28.

**Hypothesis**: C-28 (skeleton pre-declaration) is an aspirational criterion. V-02 tests whether the two new criteria — C-34 (content anchors in manifest entries) and C-35 (per-participant vote-anchor manifest in PHASE-3-COMMIT) — can be satisfied in the flat format that R12 V-02 and V-03 use. If the flat format cannot carry C-35, the score gap will isolate exactly which structural dependency C-35 has on the skeleton format. Expected: satisfies C-35 but misses C-28 (2 pts); net score ~142/144.

---

You are running `org:committee`. Execute the following phases in order. Complete each phase and print its PHASE-N-COMMIT: block before beginning the next phase.

---

**PHASE 0 — COMMITTEE DECLARATION**

PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type.
LOAD: charter from `.craft/roles/` matching this committee type; extract named roles with orientations.
ENFORCE: if no charter exists — use Signal defaults (PM, Architect, Inertia-Advocate) and declare fallback.
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — path used or fallback declaration.
PRINT: Participants — one line per role; format `[Role Name] — [charter-defined orientation in one phrase]`.

PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 — INVESTIGATION**

LABEL: `INVESTIGATION-ATTEMPT-1`
WRITE: INERTIA-FINDING-A — the specific workflow, tool, or process in production that this agenda item displaces; name the production artifact precisely.
WRITE: INERTIA-FINDING-B — the specific integration surface at risk; name systems, APIs, contracts, or downstream consumers.
WRITE: INERTIA-FINDING-C — the team whose cognitive habits would break and the specific decision habit they rely on today; name both the team and the habit.
WRITE: INERTIA-FINDING-D — the non-obvious switching cost the proposal author did not account for; specific enough that the author would say "I missed that."

GATE-1 — intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO and one-sentence basis.
IF NO: INCREMENT to INVESTIGATION-ATTEMPT-2; rewrite all four INERTIA-FINDING-* labels from a different angle; re-evaluate GATE-2; repeat until YES.
ENFORCE: each retry carries a new sequential INVESTIGATION-ATTEMPT-N label; a rewrite without the incremented label fails C-24.
ENFORCE: the loop runs within Phase 1; Phase 2 is unconditionally reached once any GATE-N answers YES.

PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES.
  Citation-anchor manifest — findings locked; downstream CITE: and RESPONDS-TO: valid only against labels listed here:
    INERTIA-FINDING-A: [keyword or title identifying this finding's claim]
    INERTIA-FINDING-B: [keyword or title identifying this finding's claim]
    INERTIA-FINDING-C: [keyword or title identifying this finding's claim]
    INERTIA-FINDING-D: [keyword or title identifying this finding's claim]
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.
VALIDATE: each manifest entry carries a content anchor readable without Phase 1 prose; bare label with no following text fails C-34.

---

**PHASE 2 — TIER SORT**

ASSIGN: Tier 1 (CHALLENGERS) — roles interrogating feasibility, risk, or disruption; these speak first.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending specific conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's goals; these speak last.
PRINT: TIER SORT listing all three tiers with assigned roles.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK:
PRINT: Test: `Tier 1 and Tier 2 both empty?`
PRINT: Result: YES or NO.
IF YES: name the mis-sorted role, target tier, and reason; reprint corrected TIER SORT; reprint SORT-CHECK; loop until NO.
ENFORCE: SORT-CHECK must appear with both `Test:` and `Result:` fields as a discrete labeled gate.

PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 — PARTICIPANT VOICES**

ENFORCE: Tier 1 voices before Tier 2 before Tier 3.

For each participant, in tier order:
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose.
VALIDATE: STANCE: is a committed declaration; no prose may soften or qualify it.
WRITE: 2-4 sentences from the participant's charter role orientation responding to the agenda item.
REQUIRE (Tier 1): cite a named INERTIA-FINDING-* label from the Phase 1 manifest in the concern.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3 only): PRINT `CITE: INERTIA-FINDING-[A/B/C/D] — [finding content]` before endorsement prose; named label must appear in Phase 1 manifest.
REQUIRE (Tier 3 only): PRINT `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`; named concern must quote or paraphrase a specific Tier 1 or Tier 2 concern; generic attribution fails.

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen and tier reassignment before continuing.

PRINT: PHASE-3-COMMIT: [locked] — Stance manifest (one entry per participant):
  [Role Name] STANCE-TOKEN
  [Role Name] STANCE-TOKEN
  [one line per participant — Role Name followed by BLOCK, CONDITION, or APPROVE]
All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.
VALIDATE: Phase 4 TALLY derived from this manifest by counting tokens; manifest is authoritative; re-parsing Phase 3 prose for the tally is not permitted.

---

**PHASE 4 — TALLY**

COUNT: each stance token in the Phase 3 stance manifest.
PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line.
DERIVE: OUTCOME — all APPROVE → APPROVED; any CONDITION, no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
PRINT: OUTCOME.

PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 — MINUTES**

DECISIONS:
WRITE: Verdict — must match Phase 4 OUTCOME exactly.
WRITE: Conditions for full approval — name each condition specifically; "address feedback" fails.
IF verdict is not APPROVED:
  WRITE: Owner — a specific named role (not a team) responsible for satisfying the blocking condition.
  WRITE: Trigger — the concrete deliverable or event that causes committee re-review; "sufficient progress" fails.
VALIDATE: both Owner and Trigger present when verdict is not APPROVED.

ACTION ITEMS:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item; all three parts required.

DISSENTING OPINIONS:
WRITE: for each CONDITION or BLOCK participant — the specific objection (citing INERTIA-FINDING-* label from the Phase 1 manifest) and the resolution path (concrete trigger + named authority).
IF no dissent: PRINT `No dissent — [one sentence explaining consensus]`.

PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-03 — Single-Axis: Phrasing Register — Conversational Framing with C-35 Vote-Anchor Manifest

**Variation axis**: Phrasing register — conversational and less-rigid framing throughout. Phase boundaries are described rather than commanded in most places; structural labels (STANCE:, CITE:, RESPONDS-TO:, PHASE-N-COMMIT:) remain mandatory but the fill rules around them are written in descriptive imperative rather than uppercase verb-first commands. Tests whether C-35's vote-anchor manifest can be satisfied under a reduced-formality register.

**Hypothesis**: C-35 requires a structural manifest — per-participant enumeration — that is format-specific regardless of register. A conversational prompt can satisfy C-35 if it explicitly describes what the PHASE-3-COMMIT must contain. C-34 requires anchor content per manifest entry, which is equally achievable in conversational phrasing. R12 V-03 scored well in prior rounds; adding the vote-anchor manifest to its PHASE-3-COMMIT should close C-35. Expected: 140–142/144 — may miss C-28 (skeleton pre-declaration requires pre-print step) and C-30 (imperative micro-instructions) since those are architecture choices, not phrasing; the conversational register intentionally sacrifices those two aspirational criteria to test whether C-35 is register-independent.

---

You are running `org:committee`. Work through the following phases in order. Finish each phase completely before starting the next.

---

**Phase 0 — Setting up the committee**

Start by identifying the committee type from the request — ROB, shiproom, arch-board, or whatever the user specified. Then look up the charter for that committee type in `.craft/roles/`. If you find it, load the named roles and their documented orientations. If you don't find it, note that you're using Signal defaults (PM, Architect, Inertia-Advocate) and proceed.

Write out: the committee type, the agenda item under review, the charter source you used, and a list of participants with each person's role name and their orientation in one phrase.

End Phase 0 with this commit block:

```
PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.
```

---

**Phase 1 — Investigating switching costs before anyone speaks**

Before you let any participant voice an opinion, investigate what the proposal would actually displace. You're looking for the friction the proposal author probably didn't model. Work through four findings:

- **INERTIA-FINDING-A** — which specific workflow, tool, or process currently in production does this proposal displace? Be specific; "existing workflow" is too vague.
- **INERTIA-FINDING-B** — which integration surface is at risk? Name the systems, APIs, contracts, or downstream consumers that would need renegotiation.
- **INERTIA-FINDING-C** — which team's cognitive habits would break, and what specific decision-making habit do they rely on today? Name both the team and the habit.
- **INERTIA-FINDING-D** — what's the non-obvious switching cost the proposal author almost certainly didn't account for? This should be something that would make them say "I missed that."

After writing all four, check yourself: does INERTIA-FINDING-D actually reveal a non-obvious cost the proposal author would not have anticipated? Answer YES or NO with one sentence of reasoning.

If NO, rewrite all four findings from a different angle — label the new block `INVESTIGATION-ATTEMPT-2` — and check again. Keep going, incrementing the attempt number each time, until you can honestly answer YES. Phase 2 always follows once you've answered YES.

Close Phase 1 with this commit block, filling in one-phrase content anchors per finding — a keyword or title that identifies each finding's claim without requiring a reader to go back and read the full Phase 1 text:

```
PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES.
  Citation-anchor manifest — findings locked for downstream citation:
    INERTIA-FINDING-A: [identifying keyword or title for this finding]
    INERTIA-FINDING-B: [identifying keyword or title for this finding]
    INERTIA-FINDING-C: [identifying keyword or title for this finding]
    INERTIA-FINDING-D: [identifying keyword or title for this finding]
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.
```

Important: each manifest entry must carry an anchor that makes the finding identifiable on its own — a bare label with nothing after it fails. Downstream CITE: and RESPONDS-TO: references are only valid if their label appears in this manifest.

---

**Phase 2 — Sorting participants by skepticism**

Now sort all the participants into three tiers before anyone speaks. Challengers (Tier 1) are the people most likely to interrogate feasibility, risk, or disruption to existing systems — they speak first. Conditionals (Tier 2) will approve if specific conditions are met — they speak second. Advocates (Tier 3) are aligned with the proposal's goals — they speak last. For a tie within a tier, the person with higher institutional veto authority goes first.

Write out the tier sort showing who is in each tier.

Then check it: are Tier 1 and Tier 2 both completely empty? If yes, you have a sorting error — reassign at least one participant to a challenger or conditional role (name the participant, the tier they're moving to, and why), redo the sort, and recheck. A unanimous-advocate sort is structurally invalid.

End Phase 2 with:

```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES / NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.
```

---

**Phase 3 — Participant voices**

Write each participant's contribution in tier order: Tier 1 first, then Tier 2, then Tier 3. For each participant, always write their `STANCE:` declaration as a separate labeled line — `STANCE: BLOCK`, `STANCE: CONDITION`, or `STANCE: APPROVE` — before any prose. Whatever comes after the STANCE: label is rationale; the STANCE: itself is the committed position and prose must not soften or reverse it.

For **Tier 1 participants**: ground at least one concern in a named INERTIA-FINDING-* label from the Phase 1 manifest.

For **Tier 2 participants**: name the specific condition for approval — "address the concerns" is not specific enough.

For **Tier 3 participants**: before any endorsement prose, write:
  `CITE: INERTIA-FINDING-[label] — [what that finding supports about this endorsement]`
  `RESPONDS-TO: "[specific concern quoted or named]" — [one sentence addressing it]`
  The CITE: label must appear in the Phase 1 manifest. The RESPONDS-TO: must quote or name a specific Tier 1 or Tier 2 concern — not acknowledge opposition in general.

If all participants end up at APPROVE, the tier sort is wrong. Reopen Phase 2, reassign, redo the sort, and continue from there.

End Phase 3 with this commit block — it must list every participant's role name and their locked stance token individually:

```
PHASE-3-COMMIT: [locked] — Stance manifest:
  [Role Name] BLOCK
  [Role Name] CONDITION
  [Role Name] APPROVE
  [one line per participant; include every participant from the Phase 0 roster]
All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.
```

The tally in Phase 4 is computed from this manifest, not from re-reading the voices above.

---

**Phase 4 — Tally and outcome**

Count the stance tokens in the Phase 3 manifest and write the tally as a standalone line:
`TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK`

Then derive the outcome: all APPROVE is APPROVED; any CONDITION with no BLOCK is APPROVED WITH CONDITIONS; any BLOCK is BLOCKED or DEFERRED (use the convention for the committee type).

End Phase 4 with:

```
PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.
```

---

**Phase 5 — Minutes**

Write three sections:

**DECISIONS** — State the verdict (matching Phase 4 OUTCOME exactly). Name each condition for full approval specifically; "address feedback" is not enough. If the verdict is not APPROVED, name the Owner (a specific role, not a team) and the Trigger (the concrete deliverable or event that would bring this back to the committee) — both are required.

**ACTION ITEMS** — One line per item in the format `[Owner Role] — [specific action] — [deadline]`. All three parts required per item.

**DISSENTING OPINIONS** — For each participant who declared CONDITION or BLOCK, write the specific objection (citing the relevant INERTIA-FINDING-* label from the Phase 1 manifest) and the resolution path with a concrete trigger and the named authority who confirms it's been met. If there's no dissent, write `No dissent — [one sentence explaining how the group reached consensus]`.

End Phase 5 with:

```
PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
```

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing — Elevated Inertia Record + C-34 VALIDATE + C-35 Vote-Anchor Manifest

**Variation axes**: Lifecycle emphasis + Inertia framing — combined. The inertia record is elevated to a named first-class artifact: the PHASE-1-COMMIT citation-anchor manifest is referred to as the "INERTIA RECORD" in subsequent phases, making inertia-grounding traceable by artifact name rather than by label convention alone. C-34 gets an explicit VALIDATE rule with a worked-example format showing acceptable vs. failing entries. C-35 introduces the vote-anchor manifest in PHASE-3-COMMIT with an explicit derivation rule linking it to Phase 4 TALLY. The skeleton architecture (C-28) and imperative fill rules (C-30) from R12 V-05 are preserved.

**Hypothesis**: Elevating the inertia record as a named artifact (rather than an anonymous manifest) makes C-27, C-33, and C-34 harder to accidentally satisfy in degraded form — a named artifact requires deliberate citation, not incidental label use. The INERTIA RECORD naming also makes the C-35 vote-anchor manifest a structurally parallel artifact: the INERTIA RECORD is the artifact for Phase 1 findings; the STANCE MANIFEST is the artifact for Phase 3 stances. This parallel architecture makes both manifests easier to validate and harder to forget. Expected: 144/144 — all axes satisfied, both new criteria addressed.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block including both artifact manifests. Do not fill any values in this step.

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

## PHASE 1 — INERTIA RECORD

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

PHASE-1-COMMIT: [locked] — INERTIA RECORD sealed. Investigation attempt ___ complete, GATE-___ answered YES.
  INERTIA RECORD — citation-anchor manifest (content-anchored; each entry identifies its finding independently of Phase 1 prose):
    INERTIA-FINDING-A: ___  [keyword/title identifying this finding's claim]
    INERTIA-FINDING-B: ___  [keyword/title identifying this finding's claim]
    INERTIA-FINDING-C: ___  [keyword/title identifying this finding's claim]
    INERTIA-FINDING-D: ___  [keyword/title identifying this finding's claim]
  Valid citation targets for all downstream CITE: and RESPONDS-TO: fields: INERTIA-FINDING-A, B, C, D only.
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
CITE: ___ — ___           [Tier 3 only — label from INERTIA RECORD]
RESPONDS-TO: "___" — ___  [Tier 3 only — named Tier 1/2 concern]

[Repeat block per participant]

PHASE-3-COMMIT: [locked] — STANCE MANIFEST sealed.
  STANCE MANIFEST (one entry per participant — derived from locked STANCE: declarations above):
    [___] ___
    [___] ___
    [repeat per participant — format: [Role Name] STANCE-TOKEN]
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
[Derived from STANCE MANIFEST in PHASE-3-COMMIT]
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY derived from STANCE MANIFEST, OUTCOME declared. Phase 4 closed.
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
[one entry per dissent: Role — objection citing INERTIA RECORD label — resolution path — named authority — concrete trigger]
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

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.craft/roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type is declared before any other content.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules — INERTIA RECORD:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces.
  ENFORCE: "existing workflow" fails; name the production artifact.

WRITE: INERTIA-FINDING-B — name the integration surface at risk.
  REQUIRE: specific systems, APIs, contracts, or downstream consumers; generic "integrations" fails.

WRITE: INERTIA-FINDING-C — name the team whose cognitive habits would break and the specific decision-making habit they rely on today.
  ENFORCE: name both the team and the habit.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

VALIDATE: each finding carries its INERTIA-FINDING-* label as the first token; parenthesized-letter alternatives fail C-27.

GATE-N intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.
IF NO: INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; REWRITE all four findings from a different angle; GATE: GATE-N+1; REPEAT until YES.
ENFORCE: Phase 2 is unconditional once any gate answers YES; the loop is contained within Phase 1.
REQUIRE: each rewrite labeled INVESTIGATION-ATTEMPT-N+1 with sequential increment.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active INERTIA RECORD.

PRINT: PHASE-1-COMMIT: [locked] — INERTIA RECORD sealed. Investigation attempt [N] complete, GATE-[N] answered YES.
  INERTIA RECORD — citation-anchor manifest (content-anchored):
    INERTIA-FINDING-A: [keyword or title that identifies this finding's claim without reading Phase 1 prose]
    INERTIA-FINDING-B: [keyword or title that identifies this finding's claim without reading Phase 1 prose]
    INERTIA-FINDING-C: [keyword or title that identifies this finding's claim without reading Phase 1 prose]
    INERTIA-FINDING-D: [keyword or title that identifies this finding's claim without reading Phase 1 prose]
  Valid citation targets: INERTIA-FINDING-A, B, C, D only.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

VALIDATE (C-34): each INERTIA RECORD entry carries a content anchor.
  ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption`
  ACCEPTABLE: `INERTIA-FINDING-B: API-contract-breakage`
  FAILS: `INERTIA-FINDING-A:` with no following anchor text
  FAILS: comma-separated bare labels with no per-entry anchor
  A bare-label entry without an identifying anchor fails C-34 regardless of C-33 compliance.

ENFORCE: all downstream CITE: fields must reference a label from this INERTIA RECORD manifest; an unlisted label is a citation error.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) — roles interrogating feasibility, risk, or disruption; these speak first.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with proposal goals; these speak last.
ENFORCE: tie-break — higher institutional veto authority within tier speaks first.

SORT-CHECK intra-phase loop:
PRINT: Test: `Tier 1 and Tier 2 both empty?`
CONFIRM: Result YES or NO.
IF YES: REASSIGN — name the role, target tier, and reason grounded in INERTIA RECORD findings; REPRINT corrected TIER SORT; REPRINT new SORT-CHECK; LOOP until Result NO.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields.

PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 → Tier 2 → Tier 3 voice order.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before prose for each participant.
VALIDATE: STANCE: is the committed position; prose follows; prose must not soften or reverse it.
WRITE: 2-4 sentences per participant from charter role orientation responding to the agenda item.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING-* label from the INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; label must appear in the INERTIA RECORD manifest.

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific Tier 1/2 concern; generic attribution fails.

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen.

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3.

PRINT: PHASE-3-COMMIT: [locked] — STANCE MANIFEST sealed.
  STANCE MANIFEST (one entry per participant — derived from locked STANCE: declarations above):
    [Role Name] BLOCK (or CONDITION or APPROVE)
    [Role Name] CONDITION
    [Role Name] APPROVE
    [format: [Role Name] STANCE-TOKEN — one line per participant from the Phase 0 roster]
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

VALIDATE: every participant from the Phase 0 roster has exactly one entry in the STANCE MANIFEST; a missing participant fails C-35.
VALIDATE: Phase 4 TALLY counts are derived from this STANCE MANIFEST by token; counts that diverge from this manifest are a C-35 violation.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK`
COUNT: each STANCE-TOKEN in the Phase 3 STANCE MANIFEST — one count per token category.
CONFIRM: TALLY matches STANCE MANIFEST counts exactly.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] — TALLY derived from STANCE MANIFEST, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each specifically; "address feedback" fails.
REQUIRE (verdict not APPROVED): Owner (named role, not team) + Trigger (concrete deliverable or event for re-review).
VALIDATE: both Owner and Trigger present.

ACTION ITEMS:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item; all three parts required.

DISSENTING OPINIONS:
WRITE: for each CONDITION or BLOCK participant — objection citing INERTIA RECORD label + resolution path (concrete trigger + named authority).
VALIDATE: cited labels match entries in the INERTIA RECORD manifest.
IF no dissent: PRINT: `No dissent — [one sentence explaining consensus]`

ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-05 — Full Synthesis: Skeleton + Imperative Fill Rules + C-32 ENFORCE + C-33 Manifest + C-34 Anchor VALIDATE + C-35 Vote-Anchor Manifest + Elevated Inertia Framing (targets 144/144)

**Variation axes**: All axes combined — lifecycle emphasis (skeleton + labeled phases + PHASE-N-COMMIT: terminal markers with ENFORCE blocking assertions), imperative phrasing register (verb-first micro-instructions throughout), inertia framing (INERTIA RECORD as named first-class artifact; explicit C-34 VALIDATE with worked examples), output format (skeleton pre-print + fill sequence), role sequence (Tier 1 → Tier 2 → Tier 3 challenger-first with SORT-CHECK gate and tie-break rule).

**Hypothesis**: R12 V-05 scored 140/140 against v12, satisfying C-01 through C-33. The two remaining gaps are C-34 (explicit VALIDATE with format examples for manifest entry anchors) and C-35 (per-participant vote-anchor manifest in PHASE-3-COMMIT — both skeleton slot and fill rule). V-05 adds both to the R12 V-05 foundation:
1. PHASE-1-COMMIT skeleton slot and PHASE-1 fill rules: add explicit VALIDATE with ACCEPTABLE/FAILS examples for C-34 anchor specificity.
2. PHASE-3-COMMIT skeleton slot: replace Boolean assertion with structured `STANCE MANIFEST: [Role] TOKEN` enumeration placeholder.
3. PHASE-3 fill rule PRINT instruction: enumerate per-participant stances by role name and token; add VALIDATE linking TALLY derivation to the manifest.
Full synthesis targeting 144/144.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block including both manifest structures. Do not fill any values in this step.

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
  Citation-anchor manifest — findings locked; each entry carries a content anchor identifying the finding independently of Phase 1 prose:
    INERTIA-FINDING-A: ___  [keyword or title anchor]
    INERTIA-FINDING-B: ___  [keyword or title anchor]
    INERTIA-FINDING-C: ___  [keyword or title anchor]
    INERTIA-FINDING-D: ___  [keyword or title anchor]
  Valid citation targets: INERTIA-FINDING-A, B, C, D only. Phase 1 closed.
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

PHASE-3-COMMIT: [locked] — Stance manifest (one entry per participant — derived from locked STANCE: declarations above):
  [___] ___
  [___] ___
  [repeat per participant — format: [Role Name] BLOCK / CONDITION / APPROVE]
All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
[Counts derived from Phase 3 stance manifest]
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY derived from Phase 3 stance manifest, OUTCOME declared. Phase 4 closed.
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

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.craft/roles/` path used, or fallback declaration.
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

REQUIRE: each rewrite produces a new labeled block; a rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt; the label must appear in output.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE: and RESPONDS-TO: fields reference these labels by name — not as parenthesized letters.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it; the next element after PHASE-1-COMMIT: is the Phase 2 header.

PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES.
  Citation-anchor manifest — findings locked; each entry carries a content anchor identifying the finding independently of Phase 1 prose:
    INERTIA-FINDING-A: [keyword or title that identifies this finding without reading Phase 1 prose]
    INERTIA-FINDING-B: [keyword or title that identifies this finding without reading Phase 1 prose]
    INERTIA-FINDING-C: [keyword or title that identifies this finding without reading Phase 1 prose]
    INERTIA-FINDING-D: [keyword or title that identifies this finding without reading Phase 1 prose]
  Valid citation targets: INERTIA-FINDING-A, B, C, D only. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

VALIDATE (C-34): each manifest entry carries a content anchor readable without Phase 1 prose.
  ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption`
  ACCEPTABLE: `INERTIA-FINDING-B: API-contract-breakage`
  ACCEPTABLE: `INERTIA-FINDING-C: ops-team / rollback-habit`
  FAILS: `INERTIA-FINDING-A:` — bare label with no anchor
  FAILS: `INERTIA-FINDING-A, INERTIA-FINDING-B, INERTIA-FINDING-C, INERTIA-FINDING-D` — comma-separated labels with no per-entry anchor
  A manifest entry that cannot be verified against a downstream CITE: label without reading Phase 1 prose fails C-34 regardless of C-33 compliance.

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

PRINT: PHASE-3-COMMIT: [locked] — Stance manifest (one entry per participant — derived from locked STANCE: declarations above):
  [Role Name] BLOCK (or CONDITION or APPROVE)
  [Role Name] CONDITION
  [Role Name] APPROVE
  [format: [Role Name] STANCE-TOKEN — one line per participant; include every participant from the Phase 0 roster]
All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

VALIDATE: every participant from the Phase 0 roster appears exactly once in the stance manifest; a missing participant fails C-35.
VALIDATE: Phase 4 TALLY is derived by counting tokens in this stance manifest; any tally that diverges from this manifest count is a C-35 violation; re-parsing Phase 3 voice prose for the tally is not permitted.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line after the last Phase 3 voice block.
COUNT: each STANCE-TOKEN in the Phase 3 stance manifest — one count per token category (APPROVE, CONDITION, BLOCK).
CONFIRM: TALLY counts match the Phase 3 stance manifest exactly; mismatch is a C-35 violation.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it; the next element after PHASE-4-COMMIT: is the Phase 5 header.
PRINT: PHASE-4-COMMIT: [locked] — TALLY derived from Phase 3 stance manifest, OUTCOME declared. Phase 4 closed.
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
