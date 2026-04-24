# org:committee Variations — Round 14
Generated: 2026-03-16
Skill: org:committee
Rubric: v14 (C-36 VALIDATE rules carry ACCEPTABLE/FAILS worked examples; C-37 INERTIA RECORD and STANCE MANIFEST declared as named first-class sections in the pre-declared skeleton; aspirational pool 29 criteria, composite max 148)

R13 reference context: V-05 was the R13 golden synthesis targeting 144/144 — skeleton pre-declaration (C-28), imperative fill rules (C-30), INERTIA-FINDING named labels (C-27), intra-phase gate loops (C-29), PHASE-N-COMMIT: [locked] terminal markers (C-31), active ENFORCE blocking assertions (C-32), PHASE-1-COMMIT citation-anchor manifest with content-anchor suffixes per entry (C-33, C-34), PHASE-3-COMMIT vote-anchor manifest enumerating per-participant stance tokens (C-35). The gap to 148/148 is C-36 and C-37. C-36: R13 V-05 carries bilateral ACCEPTABLE/FAILS examples only on the RESPONDS-TO: VALIDATE rule; the VALIDATE rules for finding-label format (C-27), manifest content-anchor format (C-34), STANCE: label form (C-15), and CITE: citation structure (C-20) each carry a prohibition only — adding ACCEPTABLE/FAILS pairs to each closes C-36 unambiguously. C-37: R13 V-05 carries the INERTIA RECORD and STANCE MANIFEST content exclusively inside the PHASE-1-COMMIT and PHASE-3-COMMIT blocks respectively — manifests are embedded as commit attributes, not independently addressable sections. Adding named skeleton headers (`## INERTIA RECORD` within Phase 1 and `## STANCE MANIFEST` within Phase 3) as standalone sections before the commit blocks closes C-37: manifests are then navigable by section heading without locating the commit marker.

Variation axes selected:
- Single-axis V-01: Lifecycle emphasis — minimal diff from R13 V-05. Two targeted upgrades: (1) skeleton gains `## INERTIA RECORD` and `## STANCE MANIFEST` as named first-class sections before their respective commit blocks (C-37 primary); (2) VALIDATE rules for finding-label format, manifest content-anchor format, STANCE: label form, and CITE: citation structure each gain ACCEPTABLE/FAILS bilateral pairs (C-36 primary).
- Single-axis V-02: Output format — flat command sequence without skeleton pre-declaration. Tests whether C-36 and C-37 are satisfiable outside the two-step skeleton architecture. Adds bilateral VALIDATE examples and named manifest section headers as direct imperative commands.
- Single-axis V-03: Phrasing register — conversational framing with structured skeleton. C-37 manifest sections present as readable explanations alongside headers; C-36 bilateral examples woven into human-readable instructions. Tests whether a less mechanical register can carry the new structural requirements.
- Combined V-04: Lifecycle emphasis + Inertia framing — full skeleton with elevated inertia identity. INERTIA RECORD is a visually prominent named section with explicit first-class framing; Inertia-Advocate role position in the sort is made explicit. All VALIDATE rules carry bilateral worked examples (C-36). C-37 manifests are named sections.
- Full synthesis V-05: All axes combined — skeleton + imperative fill rules + C-32 ENFORCE + C-33/C-34 citation manifest + C-35 vote manifest + C-36 ACCEPTABLE/FAILS on every VALIDATE + C-37 named first-class sections + role-sequence tie-break elevation + inertia framing as a first-class investigation identity (targets 148/148).

---

## V-01 — Single-Axis: Lifecycle Emphasis — C-37 Named Manifest Sections + C-36 Bilateral VALIDATE

**Variation axis**: Lifecycle emphasis — minimal diff from R13 V-05. Two targeted upgrades: (1) skeleton Phase 1 gains a `## INERTIA RECORD` named section and Phase 3 gains a `## STANCE MANIFEST` named section, each as independent skeleton headers before their respective PHASE-N-COMMIT blocks; (2) four VALIDATE rules gain ACCEPTABLE/FAILS bilateral pairs replacing single-condition prohibitions.

**Hypothesis**: R13 V-05 scored 144/144 against v13 rubric. Against v14, C-37 fails because both manifests live only inside commit blocks — they are commit attributes, not navigable sections. C-36 fails for all VALIDATE rules except RESPONDS-TO (the only one already bilateral). Two surgical additions to the skeleton and four VALIDATE upgrades should reach 148/148 without disturbing any passing criteria.

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

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated there.
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

## STANCE MANIFEST

  [___] ___
  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
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

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type is declared before any other content; an output that proceeds without it fails C-01.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0 — no Phase 0 content may appear after it.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces.
  ENFORCE: precision required.
  VALIDATE: finding label is the first token on the line.
    ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow — the team currently routes all changes through...`
    FAILS: `(a) legacy-approval-workflow — the team currently routes...` — parenthesized letter instead of INERTIA-FINDING-A token
    FAILS: `Finding A: legacy-approval-workflow` — abbreviated label; full INERTIA-FINDING-A token required

WRITE: INERTIA-FINDING-B — name the integration surface at risk.
  REQUIRE: specific systems, APIs, contracts, or downstream consumers.
  VALIDATE: finding label is the first token on the line.
    ACCEPTABLE: `INERTIA-FINDING-B: webhook-contract — the Notification Service depends on...`
    FAILS: `(b) webhook-contract` — parenthesized letter, not the INERTIA-FINDING-B token

WRITE: INERTIA-FINDING-C — name the team whose cognitive habits would break and the specific decision-making habit they rely on today.
  ENFORCE: name both the team and the habit; generic attribution fails.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

GATE-1 intra-phase retry loop (C-29):
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → CONFIRM loop exit; fill ## INERTIA RECORD and PHASE-1-COMMIT immediately; Phase 2 is unconditional.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE: GATE-N+1 with the same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block; a rewrite without `INVESTIGATION-ATTEMPT-N+1` fails C-22 and C-24.
REQUIRE: sequential label increments by 1 with each attempt.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.

WRITE: ## INERTIA RECORD — fill the named section from the passing attempt's findings:
  PRINT: INERTIA-FINDING-A: [one-phrase anchor — the specific workflow or artifact named in this finding]
  PRINT: INERTIA-FINDING-B: [one-phrase anchor — the integration surface named in this finding]
  PRINT: INERTIA-FINDING-C: [one-phrase anchor — the team and habit named in this finding]
  PRINT: INERTIA-FINDING-D: [one-phrase anchor — the non-obvious switching cost named in this finding]
  VALIDATE: each ## INERTIA RECORD entry carries a content anchor readable without Phase 1 prose.
    ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption` — keyword identifies the finding
    ACCEPTABLE: `INERTIA-FINDING-B: re-training overhead` — two-word anchor identifies the cost
    FAILS: `INERTIA-FINDING-A:` — bare label with no following anchor text fails C-34
    FAILS: `INERTIA-FINDING-A: [one-phrase anchor]` — unfilled skeleton placeholder is not a real anchor; fails C-34

ENFORCE: ## INERTIA RECORD is an independently addressable section; it appears before PHASE-1-COMMIT.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated there. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

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
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2 — no Phase 2 content may appear after it.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed structural declaration — prose must not soften, qualify, or contradict it.
  ACCEPTABLE: `STANCE: BLOCK` on its own line, followed by rationale prose — label + single token, position unambiguous
  ACCEPTABLE: `STANCE: CONDITION` on its own line — declares conditional hold before any endorsement text
  FAILS: `The architect views this proposal as too risky to approve at this time` — stance embedded in prose, no STANCE: label
  FAILS: `STANCE: BLOCK (pending clarification)` — qualified token contradicts the declaration; parenthetical softens the structural commitment

WRITE: 2-4 sentences per participant from their charter-documented role orientation responding to this specific agenda item.
REQUIRE (Tier 1): ground concern in a named INERTIA-FINDING label from ## INERTIA RECORD where relevant.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`; prose before the label fails C-20; content without the named label fails C-27.
VALIDATE: CITE: references a named label from ## INERTIA RECORD.
  ACCEPTABLE: `CITE: INERTIA-FINDING-A — workflow-disruption: the migration plan directly addresses this cost by...`
  ACCEPTABLE: `CITE: INERTIA-FINDING-C — re-training overhead: the phased rollout reduces this because...`
  FAILS: `CITE: The workflow disruption finding supports adoption...` — finding referenced by paraphrase, no INERTIA-FINDING-* label
  FAILS: `CITE: (a) — workflow-disruption` — parenthesized letter, not the INERTIA-FINDING-A token

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific finding or concern:
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-A: workflow-disruption" — the migration plan stages the transition to avoid hard cutover`
  ACCEPTABLE: `RESPONDS-TO: "[Architect]'s concern that the webhook contract will break" — the adapter layer preserves the existing contract`
  FAILS: `RESPONDS-TO: "Inertia concerns have been acknowledged"` — generic, no attribution
  FAILS: `RESPONDS-TO: "The challenger raised valid points"` — no specific attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK.

WRITE: ## STANCE MANIFEST — fill the named section after all participant voices are written:
  PRINT one entry per participant in format `[Role Name] STANCE-TOKEN` — derived from locked STANCE: declarations above.
  ENFORCE: ## STANCE MANIFEST is an independently addressable section; it appears before PHASE-3-COMMIT.

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each entry in ## STANCE MANIFEST — one tally count per STANCE-TOKEN category.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
VALIDATE: TALLY counts match ## STANCE MANIFEST exactly; mismatch fails C-35.
WRITE: OUTCOME — derive from TALLY:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it.
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
WRITE: for each participant whose STANCE was CONDITION or BLOCK — dissent substance (specific objection, citing INERTIA-FINDING-* label from ## INERTIA RECORD where applicable) and resolution path (concrete condition + named authority who confirms when condition is met).
VALIDATE: cited INERTIA-FINDING-* labels in dissent text match labels enumerated in ## INERTIA RECORD.
CONFIRM: resolution path names a concrete trigger, not a general condition.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining why all participants reached consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 — no Phase 5 content may appear after it; it is the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-02 — Single-Axis: Output Format — Flat Command Sequence with C-36 Bilateral VALIDATE + C-37 Named Manifest Headers

**Variation axis**: Output format — flat command sequence without skeleton pre-declaration. All structural requirements — phase headers, labels, ENFORCE assertions, manifest sections, commit markers — are expressed as direct imperative commands in a single execution sequence. Tests whether C-36 bilateral VALIDATE examples and C-37 named first-class manifest sections are satisfiable without the two-step skeleton pre-declaration architecture (C-28).

**Hypothesis**: C-28 (skeleton pre-declaration) is aspirational. V-02 tests whether the two new criteria isolate cleanly: C-37 requires `## INERTIA RECORD` and `## STANCE MANIFEST` to exist as named sections — this is achievable by WRITE commands in the flat format. C-36 requires VALIDATE rules to carry ACCEPTABLE/FAILS pairs — these are expressible inline. Expected: satisfies C-36 and C-37 but misses C-28 (2 pts); net score ~146/148 ceiling, practically testing the isolation of the new criteria.

---

You are running `org:committee`. Execute the following phases in order. Complete each phase fully and print its PHASE-N-COMMIT: block before beginning the next phase.

---

**PHASE 0 — COMMITTEE DECLARATION**

PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type.
LOAD: charter from `.roles/` matching this committee type; extract named roles with documented orientations.
ENFORCE: if no charter exists — declare `Charter Source: Signal defaults — no charter found`; LOAD fallback participants (PM, Architect, Inertia-Advocate) with Signal-default orientations.
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — path used or fallback declaration.
PRINT: Participants — one line per role; format `[Role Name] — [charter-defined orientation in one phrase]`.

PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 — INVESTIGATION**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.
WRITE: INERTIA-FINDING-A — the specific workflow, tool, or process in production that this agenda item displaces; name the production artifact precisely.
WRITE: INERTIA-FINDING-B — the specific integration surface at risk; name systems, APIs, contracts, or downstream consumers.
WRITE: INERTIA-FINDING-C — the team whose cognitive habits would break and the specific decision habit they rely on today; name both the team and the habit.
WRITE: INERTIA-FINDING-D — the non-obvious switching cost the proposal author did not account for; specific enough that the author would say "I missed that."

VALIDATE: each finding opens with its named label as the first token on the line.
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-deploy-script — teams invoke it daily via...`
  FAILS: `(a) legacy-deploy-script` — parenthesized letter, not the INERTIA-FINDING-A token
  FAILS: `A: legacy-deploy-script` — abbreviated label; full token required

GATE-1 — intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO and one-sentence basis.
IF NO: INCREMENT to INVESTIGATION-ATTEMPT-2; rewrite all four INERTIA-FINDING-* labels from a different angle; GATE-2 same question; repeat until YES.
ENFORCE: each retry carries a new sequential `INVESTIGATION-ATTEMPT-N` label in output; a rewrite without the incremented label fails C-24.
ENFORCE: the loop runs within Phase 1; Phase 2 is unconditionally reached once any GATE-N answers YES.

WRITE: `## INERTIA RECORD` as a named section header after the passing attempt and before PHASE-1-COMMIT.
  PRINT under that header: one line per finding in format `INERTIA-FINDING-[A/B/C/D]: [one-phrase anchor]`
  VALIDATE: each entry carries a content anchor — not a bare label, not a placeholder.
    ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption` — keyword anchor makes finding identifiable without reading investigation prose
    ACCEPTABLE: `INERTIA-FINDING-D: undocumented-rollback-dependency` — two-word anchor names the non-obvious cost
    FAILS: `INERTIA-FINDING-A:` — bare label, no anchor; fails C-34
    FAILS: `INERTIA-FINDING-B: [one-phrase anchor]` — unfilled placeholder is not a real anchor; fails C-34
ENFORCE: `## INERTIA RECORD` is independently navigable by section heading; manifests embedded only in commit block text fail C-37.

PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above; all findings locked by label. Downstream CITE: and RESPONDS-TO: valid only against labels listed in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 — TIER SORT**

ASSIGN: Tier 1 (CHALLENGERS) — roles interrogating feasibility, risk, or disruption to existing systems; these speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's goals; these speak last.
PRINT: TIER SORT listing all three tiers with assigned roles.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK:
PRINT: `Test: Tier 1 and Tier 2 both empty?`
PRINT: `Result: YES or NO`
IF YES: name the mis-sorted role, target tier, and reason specific to this agenda item; reprint corrected TIER SORT; reprint SORT-CHECK; loop until NO.
ENFORCE: SORT-CHECK must appear with both `Test:` and `Result:` fields as a discrete labeled gate; correct ordering without the gate fails C-25.

PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 — PARTICIPANT VOICES**

ENFORCE: Tier 1 voices before Tier 2 before Tier 3.

For each participant in tier order:
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose.
VALIDATE: STANCE: is a structural committed declaration.
  ACCEPTABLE: `STANCE: BLOCK` on its own line — label + single token, stance unambiguous before any rationale
  FAILS: `The PM is conditionally approving this` — stance in prose, no STANCE: label
  FAILS: `STANCE: CONDITION — but leaning approve` — qualified token softens the declaration
WRITE: 2-4 sentences from the participant's charter role orientation responding to this specific agenda item.
REQUIRE (Tier 1): cite a named label from ## INERTIA RECORD in the concern.
REQUIRE (Tier 2): name the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3 only): PRINT `CITE: INERTIA-FINDING-[A/B/C/D] — [finding content]` before endorsement prose.
  VALIDATE: CITE: opens with the named INERTIA-FINDING-* label.
    ACCEPTABLE: `CITE: INERTIA-FINDING-B — webhook-contract: the adapter preserves the existing surface so...`
    FAILS: `CITE: The integration risk finding shows...` — finding referenced by description, no label
    FAILS: `CITE: (b) — webhook-contract` — parenthesized letter, not the INERTIA-FINDING-B token
REQUIRE (Tier 3 only): PRINT `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-C: team habit-break" — the training runway absorbs the transition cost`
  ACCEPTABLE: `RESPONDS-TO: "[Architect]'s concern that integration contracts will break" — the adapter layer preserves them`
  FAILS: `RESPONDS-TO: "the skeptics have been noted"` — generic, no attribution
  FAILS: `RESPONDS-TO: "concerns acknowledged"` — no specific attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen and tier reassignment.

WRITE: `## STANCE MANIFEST` as a named section header after all participant voices are written and before PHASE-3-COMMIT.
  PRINT under that header: one entry per participant in format `[Role Name] STANCE-TOKEN`
  ENFORCE: ## STANCE MANIFEST is independently navigable by section heading; manifests embedded only in commit block text fail C-37.

PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST token count; re-parsing Phase 3 prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 — TALLY**

COUNT: each stance token in ## STANCE MANIFEST.
PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line.
DERIVE: OUTCOME — all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
PRINT: OUTCOME.
VALIDATE: TALLY counts match ## STANCE MANIFEST token counts exactly; mismatch fails C-35.

PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 — MINUTES**

DECISIONS:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; "address feedback" fails; a specific deliverable or named state passes.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role from Phase 0 roster; ENFORCE: not a team, a specific role.
  WRITE: Trigger — concrete deliverable or event that causes committee re-review; "sufficient progress" fails; a named artifact with named recipient passes.
VALIDATE: both Owner and Trigger present when verdict is not APPROVED; a re-entry path missing either fails C-23.

ACTION ITEMS:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three fields; "investigate" without specifying the question, artifact, and recipient fails.

DISSENTING OPINIONS:
WRITE: for each CONDITION or BLOCK stance — the specific objection (citing a label from ## INERTIA RECORD where applicable) and resolution path (concrete condition + named authority).
ENFORCE: if no dissent — PRINT: `No dissent — [reason]`

PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-03 — Single-Axis: Phrasing Register — Conversational Framing with C-36 + C-37

**Variation axis**: Phrasing register — conversational framing with structured skeleton. The two-step skeleton architecture is preserved for structural reliability, but fill rules and VALIDATE instructions are written in a more readable register: explanatory prose accompanies each structural requirement. C-37 manifest sections are introduced with natural-language framing. C-36 ACCEPTABLE/FAILS pairs are woven into readable guidance rather than bare command lists. Tests whether the less mechanical register reduces structural completeness or can carry all 29 aspirational criteria.

**Hypothesis**: Conversational register typically scores well on essential and recommended criteria but risks partial passes on structural criteria (C-28, C-30) because fill rules drift toward description. V-03 tests whether C-36 and C-37 hold in a mixed-register prompt that uses imperative commands for gates and commit markers but conversational framing elsewhere. Expected: passes C-36 and C-37 but may score partial on C-30 (imperative micro-instructions requirement) if explanation text is read as softening the commands. Net score estimate: 144–147/148.

---

You are running `org:committee` — a pre-meeting simulation. The goal is to surface surprises before the real committee meets, not to rubber-stamp a proposal. Work in two steps: first, print the full structure you are about to produce; then fill it.

---

### STEP 1 — PRINT THIS SKELETON

Before writing any simulation content, print the following structure with all headers, field labels, and blank slots visible. Think of this as the table of contents and form you are about to fill in.

```
=== org:committee SIMULATION ===

## PHASE 0 — COMMITTEE DECLARATION
Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___   [one line per participant: Role Name — orientation]
PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles.
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
[NO → INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES]

## INERTIA RECORD
  INERTIA-FINDING-A: ___  [anchor]
  INERTIA-FINDING-B: ___  [anchor]
  INERTIA-FINDING-C: ___  [anchor]
  INERTIA-FINDING-D: ___  [anchor]

PHASE-1-COMMIT: [locked] — Citation-anchor manifest in ## INERTIA RECORD above; findings locked.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT
Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → correct and re-sort / NO → proceed]
PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 — PARTICIPANT VOICES
### ___ — Tier ___
STANCE: ___
[2-4 sentences from role orientation]
CITE: ___  [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]
[repeat per participant in Tier 1 → 2 → 3 order]

## STANCE MANIFEST
  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

PHASE-3-COMMIT: [locked] — Vote-anchor manifest in ## STANCE MANIFEST above; stances locked.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY
TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___
PHASE-4-COMMIT: [locked] — TALLY and OUTCOME declared. Phase 4 closed.
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
___ — ___ — ___  [Owner Role — specific action — deadline]
### DISSENTING OPINIONS
___  [Role — specific objection — resolution path — named authority — concrete trigger]
PHASE-5-COMMIT: [locked] — Minutes complete; re-entry path present if not approved. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Work through each phase in order. Each instruction below is a requirement, not a suggestion.

---

**Phase 0 — Who is in the room**

Load the charter file from `.roles/` that matches the committee type the user named. Pull every role with its documented orientation — this is who speaks and what lens they use. If no charter exists, declare that and fall back to the Signal defaults (PM, Architect, Inertia-Advocate). Fill Committee Type, Agenda Item, Charter Source, and the Participants list. Then print the PHASE-0-COMMIT: block exactly as shown in the skeleton, substituting real values.

ENFORCE: PHASE-0-COMMIT: is the last thing in Phase 0. Nothing follows it until the Phase 1 header.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 1 — What are we actually disrupting**

Before anyone speaks, investigate what the proposal is asking people to give up. Four named findings, labeled INERTIA-FINDING-A through D. Use the exact label tokens — not "(a)", not "Finding A" — as the first word on each line.

Here is what a correctly labeled finding looks like versus a violation:
  ACCEPTABLE: `INERTIA-FINDING-A: legacy-deploy-script — daily invocation by release engineers relies on...`
  FAILS: `(a) legacy-deploy-script — daily invocation...` — parenthesized letter is not the INERTIA-FINDING-A token

INERTIA-FINDING-A should name the specific production artifact or workflow being displaced.
INERTIA-FINDING-B should name the integration surface — systems, APIs, contracts, consumers.
INERTIA-FINDING-C should name the team and the specific cognitive habit they would lose.
INERTIA-FINDING-D is the most important one: the non-obvious cost the proposal author almost certainly did not see coming. Specific enough that they would say "I missed that."

After writing the four findings, run the GATE-1 self-check: does INERTIA-FINDING-D pass the non-obviousness test? If YES, move on. If NO, relabel the attempt as INVESTIGATION-ATTEMPT-1 and start a new labeled block (INVESTIGATION-ATTEMPT-2) with fresh findings and a new GATE-2. Keep going until a gate answers YES. Each retry needs its own labeled attempt block.

Once the gate is satisfied, fill the `## INERTIA RECORD` section — this is the findings' permanent home in the document, independently navigable by section heading. One line per finding, format `INERTIA-FINDING-[X]: [anchor]`. The anchor must be a real keyword or phrase, not a placeholder:

  ACCEPTABLE: `INERTIA-FINDING-A: legacy-deploy-script` — someone reading this section knows which finding it is
  ACCEPTABLE: `INERTIA-FINDING-D: undocumented-cache-invalidation` — the non-obvious cost is identifiable by label alone
  FAILS: `INERTIA-FINDING-A:` — no anchor; the section is a bare index that tells downstream phases nothing
  FAILS: `INERTIA-FINDING-B: [anchor]` — the placeholder was never filled; this is not a real entry

ENFORCE: ## INERTIA RECORD appears before PHASE-1-COMMIT; it is a named section, not just commit-block text.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 2 — Who is skeptical and who is aligned**

Assign every participant from Phase 0 to one of three tiers: Tier 1 (CHALLENGERS) are the roles whose job is to interrogate risk and feasibility — they speak first. Tier 2 (CONDITIONALS) hold approval pending specific conditions. Tier 3 (ADVOCATES) are the believers — they speak last. If everyone lands in Tier 3, something is wrong with the sort; run the SORT-CHECK to catch it.

Print the SORT-CHECK gate exactly as it appears in the skeleton. If the answer is YES (both Tier 1 and Tier 2 are empty), name a role that should be a challenger or conditional given the specific findings in ## INERTIA RECORD, reassign it, reprint the sort, and rerun the check. Keep looping until the answer is NO.

ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 3 — Voices**

Tier 1 speaks first, then Tier 2, then Tier 3. For each participant, the very first thing printed for their turn is a STANCE: line — a standalone label followed by exactly one token (BLOCK, CONDITION, or APPROVE). No qualifications in the token; no stance embedded in prose.

What a clean STANCE: declaration looks like versus a violation:
  ACCEPTABLE: `STANCE: CONDITION` on its own line, then 2-4 sentences of rationale
  FAILS: `The security lead is leaning toward conditional approval...` — stance buried in prose, no label

Tier 1 voices should ground their concern in a named label from ## INERTIA RECORD. Tier 2 voices must name their specific condition — "address concerns" is not a condition. Tier 3 voices (advocates) must fill two structural fields before any endorsement prose:

CITE: — reference a specific label from ## INERTIA RECORD by name:
  ACCEPTABLE: `CITE: INERTIA-FINDING-A — legacy-deploy-script: the migration plan retires this path cleanly`
  FAILS: `CITE: There are integration risks that this proposal addresses` — no label, finding referenced by description
  FAILS: `CITE: (c) — the team habit cost` — parenthesized letter, not the INERTIA-FINDING-C token

RESPONDS-TO: — name and quote the specific concern being addressed:
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-D: cache-invalidation" — the proposal's warm-cache strategy eliminates cold-start risk`
  ACCEPTABLE: `RESPONDS-TO: "[Security Lead]'s concern that audit logs will break" — the adapter preserves them`
  FAILS: `RESPONDS-TO: "concerns have been noted"` — no attribution
  FAILS: `RESPONDS-TO: "the skeptics raised good points"` — generic, no named concern

If all voices end up APPROVE, the tier sort in Phase 2 was wrong. Go back, fix the sort, run the SORT-CHECK, and redo Phase 3 from the corrected order.

After all voices, fill the `## STANCE MANIFEST` section — one line per participant, format `[Role Name] STANCE-TOKEN`. This section must have its own header, not just appear inside the commit block.

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 4 — Count the votes**

Count the tokens in ## STANCE MANIFEST. Print the TALLY line and OUTCOME. The tally must match the manifest exactly — do not re-read Phase 3 prose.

PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 5 — Minutes**

Write DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS. The verdict must match the OUTCOME from Phase 4. If the verdict is not APPROVED, a re-entry path is required — an Owner (a specific named role from Phase 0, not a team) and a Trigger (a concrete deliverable or event, not "sufficient progress"). Action items must have three parts: who, what specifically, and by when. Dissents must cite a specific objection and name a resolution condition with an authority who can confirm it.

PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing — C-36 + C-37 with Elevated Inertia Identity

**Variation axis**: Lifecycle emphasis + Inertia framing. Full skeleton architecture with two elevations: (1) the INERTIA RECORD is given a visually prominent named section header in the skeleton with explicit framing as a first-class investigation artifact (C-37 primary); (2) Inertia-Advocate role assignment in Phase 2 is made an explicit rule — if no Inertia-Advocate exists in the charter, one is synthesized with Signal-default orientation and placed in Tier 1 unconditionally. All VALIDATE rules carry bilateral ACCEPTABLE/FAILS examples (C-36 primary).

**Hypothesis**: The elevated inertia framing hypothesis: making the Inertia-Advocate a structural invariant (not an optional charter participant) strengthens C-11 and C-12 compliance — the investigation always has an adversarial anchor role, and the tier sort always has at least one Tier 1 challenger. Combined with C-36 bilateral VALIDATEs and C-37 named manifest sections, this should reach 148/148 while also testing whether the inertia elevation opens new scoring advantages beyond the new criteria.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below, every header, every field, every placeholder. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]
  - Inertia-Advocate — [status: charter-loaded or Signal-default-synthesized]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded, Inertia-Advocate: [charter/synthesized].
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

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; repeat until YES]

---

## INERTIA RECORD
[First-class investigation artifact — independently addressable; cited by label in all downstream phases]

INERTIA-FINDING-A: ___  [anchor: specific workflow or artifact]
INERTIA-FINDING-B: ___  [anchor: integration surface]
INERTIA-FINDING-C: ___  [anchor: team and habit]
INERTIA-FINDING-D: ___  [anchor: non-obvious switching cost]

---

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked.
  All downstream CITE:, RESPONDS-TO:, and dissent citations valid only against labels listed in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS (INERTIA-ADVOCATE always Tier 1): ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → reassign / NO → proceed]
  Inertia-Advocate check: Inertia-Advocate in Tier 1? ___ [YES / NO — if NO, state overriding reason]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, Inertia-Advocate in Tier 1 confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3; Inertia-Advocate speaks in Tier 1]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant]

---

## STANCE MANIFEST
[First-class vote record — independently addressable; Phase 4 TALLY derives from this section]

  [___] ___
  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

---

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 prose is not permitted.
  Voices complete in Tier 1 → 2 → 3 order; Inertia-Advocate spoke in Tier 1. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY and OUTCOME declared from ## STANCE MANIFEST. Phase 4 closed.
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
[Role — specific objection citing ## INERTIA RECORD label — resolution path — named authority — concrete trigger]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; re-entry path present if not approved. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter exists — WRITE Charter Source: `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate.
REQUIRE: Inertia-Advocate is always present in the participant roster.
  ENFORCE: if the charter does not include an explicit Inertia-Advocate role — SYNTHESIZE one with orientation "represents the status-quo investment, existing workflows, and switching costs of the current production system" and declare status `Signal-default-synthesized`.
  ENFORCE: if the charter includes an Inertia-Advocate — declare status `charter-loaded`.
PRINT: Committee Type, Agenda Item, Charter Source, Participants list, Inertia-Advocate status.
VALIDATE: Committee Type declared before any other content.
  ACCEPTABLE: `Committee Type: shiproom` — type declared as the first field in Phase 0
  FAILS: [proceeding to Agenda Item without declaring Committee Type] — structural ordering violation
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded, Inertia-Advocate: [charter/synthesized].
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces. The Inertia-Advocate's primary evidence.
  ENFORCE: precision required.
  VALIDATE: INERTIA-FINDING-A label is the first token on the line.
    ACCEPTABLE: `INERTIA-FINDING-A: nightly-batch-export — operations team relies on this for...`
    FAILS: `(a) nightly-batch-export` — parenthesized letter is not the INERTIA-FINDING-A token; fails C-27
    FAILS: `A. nightly-batch-export` — abbreviated form; full INERTIA-FINDING-A token required

WRITE: INERTIA-FINDING-B — name the integration surface at risk; specific systems, APIs, contracts, consumers.
  VALIDATE: INERTIA-FINDING-B label is the first token.
    ACCEPTABLE: `INERTIA-FINDING-B: downstream-billing-webhook — three consumer services depend on this format...`
    FAILS: `(b) downstream-billing-webhook` — fails C-27

WRITE: INERTIA-FINDING-C — name the team and the specific decision-making habit they rely on today.
  ENFORCE: name both; "teams in general" fails.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

GATE-1 intra-phase retry loop (C-29):
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.
ENFORCE: loop runs within Phase 1; Phase 2 is always reached:
  IF YES → fill ## INERTIA RECORD and PHASE-1-COMMIT; Phase 2 is unconditional.
  IF NO → INCREMENT N; LABEL INVESTIGATION-ATTEMPT-N+1; WRITE four new INERTIA-FINDING-* labels from a different angle; GATE-N+1; repeat.
REQUIRE: each rewrite carries a sequential `INVESTIGATION-ATTEMPT-N` label; unlabeled rewrites fail C-24.

WRITE: ## INERTIA RECORD section — fill as a named first-class section, not inside the commit block:
  PRINT label `## INERTIA RECORD` as a standalone section header.
  PRINT: [First-class investigation artifact — independently addressable by section heading]
  PRINT: INERTIA-FINDING-A: [one-phrase anchor from passing attempt]
  PRINT: INERTIA-FINDING-B: [one-phrase anchor from passing attempt]
  PRINT: INERTIA-FINDING-C: [one-phrase anchor from passing attempt]
  PRINT: INERTIA-FINDING-D: [one-phrase anchor from passing attempt]
  VALIDATE: each ## INERTIA RECORD entry carries a real content anchor — readable without Phase 1 prose.
    ACCEPTABLE: `INERTIA-FINDING-A: nightly-batch-export` — two-word anchor identifies finding by claim
    ACCEPTABLE: `INERTIA-FINDING-D: undocumented-failover-path` — anchor names the non-obvious cost
    FAILS: `INERTIA-FINDING-A:` — bare label; no anchor; fails C-34
    FAILS: `INERTIA-FINDING-C: [anchor: team and habit]` — skeleton placeholder not filled; fails C-34

ENFORCE: ## INERTIA RECORD is independently navigable; content that exists only inside PHASE-1-COMMIT block text fails C-37.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
REQUIRE: Inertia-Advocate is assigned Tier 1 unconditionally.
  ENFORCE: the only valid exception is if the charter explicitly documents a reason for the Inertia-Advocate to hold a conditional or advocate stance — REQUIRE: this exception to be declared in the SORT-CHECK Inertia-Advocate check field with the charter-cited reason.
ASSIGN: Tier 1 (CHALLENGERS) — roles interrogating feasibility, risk, or disruption; Inertia-Advocate always here.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending specific conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's goals.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK fill rule (intra-phase loop):
PRINT: `Test: Tier 1 and Tier 2 both empty?`
CONFIRM: Result YES or NO.
PRINT: `Inertia-Advocate check: Inertia-Advocate in Tier 1?` — YES or NO with reason if NO.
VALIDATE: if Result YES — REQUIRE reassignment grounded in specific INERTIA-FINDING labels from ## INERTIA RECORD; re-print corrected TIER SORT; re-print SORT-CHECK; loop until NO.
ENFORCE: SORT-CHECK must carry both `Test:` / `Result:` and `Inertia-Advocate check:` fields as a named gate.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, Inertia-Advocate in Tier 1 confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 before Tier 3; Inertia-Advocate speaks first in Tier 1.
PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose.
VALIDATE: STANCE: is a structural committed declaration.
  ACCEPTABLE: `STANCE: BLOCK` on its own line before any rationale — label + single token; no qualification
  ACCEPTABLE: `STANCE: CONDITION` on its own line — holds approval pending a named condition
  FAILS: `The inertia advocate conditionally accepts this` — stance in prose without a STANCE: label
  FAILS: `STANCE: BLOCK — unless the migration timeline is extended` — qualifier appended to token softens declaration
WRITE: 2-4 sentences per participant from their charter orientation responding specifically to this agenda item.
REQUIRE (Inertia-Advocate, Tier 1): grounds concern in at least two named labels from ## INERTIA RECORD.
REQUIRE (other Tier 1): grounds concern in at least one named label from ## INERTIA RECORD.
REQUIRE (Tier 2): names the specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting endorsement]`
ENFORCE: named INERTIA-FINDING-* label is the first element after CITE:.
VALIDATE: citation opens with a valid label from ## INERTIA RECORD.
  ACCEPTABLE: `CITE: INERTIA-FINDING-B — downstream-billing-webhook: the adapter contract preserves this format...`
  ACCEPTABLE: `CITE: INERTIA-FINDING-D — undocumented-failover-path: the proposal's warm-standby addresses this...`
  FAILS: `CITE: The integration risk is mitigated by...` — no label; reference by prose description fails C-20
  FAILS: `CITE: (b) — billing webhook` — parenthesized letter; INERTIA-FINDING-B token required

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: names a specific concern from Tier 1 or Tier 2.
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-A: nightly-batch-export" — the migration scheduler preserves this path through Q3`
  ACCEPTABLE: `RESPONDS-TO: "[Inertia-Advocate]'s concern that the failover path will break" — the standby topology is pre-validated`
  FAILS: `RESPONDS-TO: "Concerns have been noted and will be addressed"` — generic, no attribution
  FAILS: `RESPONDS-TO: "The challenger's objections"` — refers to class of concern, not a specific named concern

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen.

WRITE: ## STANCE MANIFEST section — fill as a named first-class section after all participant voices:
  PRINT label `## STANCE MANIFEST` as a standalone section header.
  PRINT: [First-class vote record — independently addressable by section heading; Phase 4 TALLY derives from here]
  PRINT: one entry per participant in format `[Role Name] STANCE-TOKEN`
  ENFORCE: ## STANCE MANIFEST is independently navigable; manifest embedded only in PHASE-3-COMMIT text fails C-37.

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked. Inertia-Advocate BLOCK or CONDITION confirmed. Phase 4 TALLY derives from ## STANCE MANIFEST; re-parsing Phase 3 prose not permitted. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

COUNT: each stance token in ## STANCE MANIFEST.
PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line.
VALIDATE: TALLY matches ## STANCE MANIFEST count exactly.
  ACCEPTABLE: manifest shows [Inertia-Advocate] BLOCK, [PM] CONDITION, [Architect] APPROVE → `TALLY: 1 APPROVE · 1 CONDITION · 1 BLOCK`
  FAILS: manifest shows three entries but TALLY reports different counts — manifest is authoritative; re-counting Phase 3 prose is not permitted
WRITE: OUTCOME — all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] — TALLY and OUTCOME declared from ## STANCE MANIFEST. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS: WRITE Verdict (matches Phase 4 OUTCOME exactly); WRITE Conditions for full approval (specific deliverables, not "address feedback"); REQUIRE when not APPROVED: Owner (specific named role, not team) + Trigger (concrete deliverable or event, not "sufficient progress").
VALIDATE: both Owner and Trigger present when verdict is not APPROVED.
  ACCEPTABLE: `Owner: Inertia-Advocate | Trigger: written sign-off on the failover topology from Ops Lead before next shiproom`
  FAILS: `Owner: the team | Trigger: sufficient progress` — team is not a role; "sufficient progress" is not a trigger

ACTION ITEMS: PRINT `[Owner Role] — [specific action] — [deadline]`; three fields required per item.
DISSENTING OPINIONS: for each CONDITION or BLOCK stance — specific objection (citing ## INERTIA RECORD label where applicable) + resolution path (named authority + concrete trigger).
ENFORCE: if no dissent — PRINT `No dissent — [reason]`.
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written; re-entry path present if not approved. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-05 — Full Synthesis: All Axes — Targets 148/148

**Variation axis**: All axes combined — skeleton + imperative fill rules + C-32 ENFORCE terminal assertions + C-33/C-34 citation manifest + C-35 vote manifest + C-36 ACCEPTABLE/FAILS on every VALIDATE rule + C-37 named first-class sections for both manifests + role-sequence tie-break with Inertia-Advocate invariant + elevated inertia framing throughout.

**Hypothesis**: Full synthesis integrating all 14 previous rounds' accumulated requirements. C-36 is satisfied by bilateral worked examples on every VALIDATE rule. C-37 is satisfied by `## INERTIA RECORD` and `## STANCE MANIFEST` as named skeleton sections with their own headers before their respective commit blocks. Every aspiration criterion C-09 through C-37 is structurally enforced by at least one named gate, label requirement, or validation pair. Target: 148/148.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, every field label, every `___` placeholder, and every PHASE-N-COMMIT: block exactly as written. Do not fill any values in this step.

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

[Continue as INVESTIGATION-ATTEMPT-N / GATE-N until YES; sequential label increments each attempt]

---

## INERTIA RECORD
[Named first-class investigation artifact — independently addressable by section heading]
[Downstream CITE: and RESPONDS-TO: valid only against labels listed here]

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

---

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked by label.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break rule: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → reassign: ___ to Tier ___ because ___; corrected TIER SORT follows / NO → proceed]

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

---

## STANCE MANIFEST
[Named first-class vote record — independently addressable by section heading]
[Phase 4 TALLY derives from token counts in this section]

  [___] ___
  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

---

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY and OUTCOME declared from ## STANCE MANIFEST. Phase 4 closed.
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
[Role — specific objection citing ## INERTIA RECORD label — resolution path — named authority — concrete trigger]
[or: No dissent — [reason]]

PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below. Every ENFORCE and VALIDATE is a constraint, not a preference.

---

**PHASE 0 fill rules:**

LOAD: charter from `.roles/` matching this committee type; extract every named role with documented orientation.
ENFORCE: if no charter file exists — WRITE Charter Source: `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type.
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — `.roles/` path or fallback declaration.
PRINT: Participants — one line per role; format `[Role Name] — [charter-defined orientation in one phrase]`.
VALIDATE: Committee Type declared before any other content in Phase 0.
  ACCEPTABLE: opening line of Phase 0 is `Committee Type: shiproom` — type is the first declared field
  FAILS: Phase 0 begins with Agenda Item before Committee Type — structural ordering violation; fails C-01
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0; no Phase 0 content may appear after it.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces.
  ENFORCE: precision required; generic references fail.
  VALIDATE: INERTIA-FINDING-A label is the first token on the line.
    ACCEPTABLE: `INERTIA-FINDING-A: release-gate-script — the on-call team invokes this manually every deploy to...`
    FAILS: `(a) release-gate-script — the on-call team...` — parenthesized letter substituted for INERTIA-FINDING-A token; fails C-27
    FAILS: `Finding A: release-gate-script` — abbreviated label; full INERTIA-FINDING-A token required; fails C-27

WRITE: INERTIA-FINDING-B — name the integration surface at risk; specific systems, APIs, contracts, or downstream consumers.
  VALIDATE: INERTIA-FINDING-B label is the first token.
    ACCEPTABLE: `INERTIA-FINDING-B: audit-log-consumer — the Compliance team's reconciliation service reads from...`
    FAILS: `(b) audit-log-consumer` — parenthesized letter; fails C-27

WRITE: INERTIA-FINDING-C — name the team and the specific decision-making habit they rely on today.
  ENFORCE: name both team and habit; "teams in general" fails.

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for.
  REQUIRE: specific enough that the author would say "I missed that."

GATE-1 intra-phase retry loop (C-29):
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is unconditionally reached:
  IF GATE-N Answer YES → fill ## INERTIA RECORD; PHASE-1-COMMIT immediately; Phase 2 is unconditional.
  IF GATE-N Answer NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE-N+1; re-evaluate; REPEAT.
REQUIRE: each rewrite labeled `INVESTIGATION-ATTEMPT-N+1` — a rewrite without the incremented label fails C-22 and C-24.
REQUIRE: sequential label increments by 1 each attempt.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.
ENFORCE: all downstream CITE:, RESPONDS-TO:, and dissent citations reference these labels by name — not parenthesized letters.

WRITE: ## INERTIA RECORD section — this is a named first-class section, not text inside the commit block:
  PRINT the header `## INERTIA RECORD` as a standalone section label.
  PRINT: [Named first-class investigation artifact — independently addressable by section heading]
  PRINT: [Downstream CITE: and RESPONDS-TO: valid only against labels listed here]
  PRINT: INERTIA-FINDING-A: [one-phrase anchor — the specific workflow or artifact named in this finding]
  PRINT: INERTIA-FINDING-B: [one-phrase anchor — the integration surface named in this finding]
  PRINT: INERTIA-FINDING-C: [one-phrase anchor — the team and habit named in this finding]
  PRINT: INERTIA-FINDING-D: [one-phrase anchor — the non-obvious switching cost named in this finding]
  VALIDATE: each ## INERTIA RECORD entry carries a content anchor readable without Phase 1 prose.
    ACCEPTABLE: `INERTIA-FINDING-A: release-gate-script` — keyword identifies the finding by claim
    ACCEPTABLE: `INERTIA-FINDING-D: hidden-cache-warm-dependency` — anchor names the non-obvious cost
    FAILS: `INERTIA-FINDING-A:` — bare label with no anchor text; fails C-34
    FAILS: `INERTIA-FINDING-B: [one-phrase anchor]` — skeleton placeholder not replaced with real content; fails C-34
  ENFORCE: ## INERTIA RECORD is independently navigable by section heading; content that exists only inside PHASE-1-COMMIT block text fails C-37.

ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1; no Phase 1 content may appear after it.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked by label. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster into tier assignments.
ASSIGN: Tier 1 (CHALLENGERS) — roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems.
  ENFORCE: these roles speak before all others.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals.
  ENFORCE: these roles speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first; if veto authority equal — role that appears first in `.roles/` charter speaks first.

SORT-CHECK fill rule (intra-phase loop):
PRINT: `Test: Tier 1 and Tier 2 both empty?` — fixed string, print verbatim.
CONFIRM: Result YES or NO.
VALIDATE: if Result YES — REQUIRE reassignment grounded in specific INERTIA-FINDING labels from ## INERTIA RECORD.
  ACCEPTABLE: `Result: YES → [Risk Lead] moved to Tier 1 because INERTIA-FINDING-D names a risk within their domain; corrected sort follows`
  FAILS: `Result: YES → moving a participant to Tier 1 for balance` — vague reason not grounded in ## INERTIA RECORD
RE-PRINT corrected TIER SORT block; RE-PRINT new SORT-CHECK block; LOOP until Result NO.
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both `Test:` and `Result:` fields; correct tier ordering without a named SORT-CHECK gate fails C-25.
CONFIRM: Result NO is the Phase 2 exit condition; Phase 3 fills unconditionally once Result is NO.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2; no Phase 2 content may appear after it.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 voices before Tier 3 voices.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed structural declaration; prose must not soften, qualify, or contradict it.
  ACCEPTABLE: `STANCE: BLOCK` on its own line, followed by rationale prose — label + single unqualified token
  ACCEPTABLE: `STANCE: CONDITION` on its own line — conditional hold before any endorsement or caveat
  FAILS: `The security lead is conditionally blocking pending clarification` — stance buried in prose, no STANCE: label; fails C-15
  FAILS: `STANCE: BLOCK (for now)` — parenthetical qualifies the token; structural declaration compromised; fails C-15

WRITE: 2-4 sentences per participant from their charter-documented role orientation responding to this specific agenda item.
REQUIRE (Tier 1): ground concern in at least one named label from ## INERTIA RECORD where relevant.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before any endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named INERTIA-FINDING-* label is the first element after `CITE:`.
VALIDATE: CITE: opens with a named label from ## INERTIA RECORD.
  ACCEPTABLE: `CITE: INERTIA-FINDING-A — release-gate-script: the migration plan retires this path in Phase 2, not Phase 1`
  ACCEPTABLE: `CITE: INERTIA-FINDING-D — hidden-cache-warm-dependency: the proposal's warm-standby eliminates cold-start risk`
  FAILS: `CITE: The integration surface finding supports this approach because...` — referenced by prose description, no named label; fails C-20
  FAILS: `CITE: (a) — release-gate-script` — parenthesized letter substituted for INERTIA-FINDING-A token; fails C-20 and C-27

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific concern raised by a Tier 1 or Tier 2 participant.
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-A: release-gate-script" — the migration retires this in Phase 2 with a hard cutover gate`
  ACCEPTABLE: `RESPONDS-TO: "[Architect]'s concern that the audit-log consumer format will break" — the adapter preserves the existing schema`
  FAILS: `RESPONDS-TO: "The skeptics have been acknowledged"` — generic; no named attribution; fails C-21
  FAILS: `RESPONDS-TO: "concerns noted"` — no specific concern named; fails C-21

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK.
  ACCEPTABLE: lineup of BLOCK, CONDITION, APPROVE, APPROVE — at least one non-approve present; proceed
  FAILS: all-APPROVE lineup detected — Phase 2 sort is structurally invalid; REOPEN Phase 2; REASSIGN at least one role to Tier 1 or Tier 2 grounded in ## INERTIA RECORD findings; RE-RUN SORT-CHECK; RE-PRINT corrected Phase 3

WRITE: ## STANCE MANIFEST section — fill as a named first-class section after all participant voices:
  PRINT the header `## STANCE MANIFEST` as a standalone section label.
  PRINT: [Named first-class vote record — independently addressable by section heading]
  PRINT: [Phase 4 TALLY derives from token counts in this section]
  PRINT: one entry per participant in format `[Role Name] STANCE-TOKEN`
  ENFORCE: ## STANCE MANIFEST is independently navigable by section heading; manifest embedded only inside PHASE-3-COMMIT block text fails C-37.
  VALIDATE: every participant from Phase 0 roster has exactly one entry; missing entries fail C-35.
    ACCEPTABLE: four participants → four entries, each `[Role Name] BLOCK/CONDITION/APPROVE`
    FAILS: four participants → three entries in manifest (one omitted) — manifest is incomplete; fails C-35

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3; no Phase 3 content may appear after it.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

COUNT: each stance token in ## STANCE MANIFEST — one count per APPROVE, CONDITION, BLOCK token.
PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line, not embedded in prose.
VALIDATE: TALLY counts match ## STANCE MANIFEST entry counts exactly.
  ACCEPTABLE: ## STANCE MANIFEST has `[PM] APPROVE`, `[Architect] BLOCK`, `[Risk Lead] CONDITION` → `TALLY: 1 APPROVE · 1 CONDITION · 1 BLOCK`
  FAILS: ## STANCE MANIFEST has three entries but TALLY reports `2 APPROVE · 1 BLOCK` — count mismatch; manifest is authoritative; fails C-35
WRITE: OUTCOME:
  ENFORCE: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] — TALLY and OUTCOME declared from ## STANCE MANIFEST. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly.
  ENFORCE: "address feedback" fails; REQUIRE: a specific deliverable or named state.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role from Phase 0 participant roster; ENFORCE: not a team or group; a specific named role.
  WRITE: Trigger — concrete deliverable, evidence artifact, or event that causes committee re-review.
    ENFORCE: "sufficient progress" fails.
VALIDATE: both Owner and Trigger present when verdict is not APPROVED.
  ACCEPTABLE: `Owner: Architect | Trigger: updated ADR with audit-log adapter contract reviewed and signed by Compliance Lead before next ROB`
  FAILS: `Owner: the development team | Trigger: when ready` — team not a role; "when ready" not a concrete trigger; fails C-23

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three fields per item.
  ENFORCE: "investigate further" alone fails — WRITE: what is investigated, the output artifact, and who receives it.

DISSENTING OPINIONS fill rules:
WRITE: for each CONDITION or BLOCK stance — dissent substance (specific objection, citing a label from ## INERTIA RECORD where applicable) and resolution path (concrete condition + named authority who confirms when satisfied).
VALIDATE: INERTIA-FINDING-* labels cited in dissents match labels in ## INERTIA RECORD.
  ACCEPTABLE: `[Architect] BLOCK — INERTIA-FINDING-B: audit-log-consumer will break on schema change; resolved when Compliance Lead confirms adapter contract` — label cites ## INERTIA RECORD, authority named
  FAILS: `[Architect] is blocking because the integration concerns have not been addressed` — no label citation, no named authority, no concrete resolution trigger; fails C-08 and C-23
CONFIRM: resolution path names a concrete trigger and a named authority.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining consensus]`.
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.
