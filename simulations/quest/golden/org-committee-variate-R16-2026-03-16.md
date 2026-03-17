# org:committee Variations — Round 16
Generated: 2026-03-16
Skill: org:committee
Rubric: v16 (C-40 named manifest sections carry explicit post-commit seal declarations; C-41 commit heading cross-references include explicit bidirectionality constraint statement; aspirational pool 33 criteria, composite max 156)

R15 reference context: V-05 was the R15 golden synthesis targeting 152/152 — skeleton pre-declaration (C-28), imperative fill rules (C-30), named INERTIA-FINDING labels (C-27), intra-phase gate loops (C-29), PHASE-N-COMMIT: [locked] terminal markers (C-31), active ENFORCE blocking assertions (C-32), PHASE-1-COMMIT citation-anchor manifest with content-anchor suffixes per entry (C-33, C-34), PHASE-3-COMMIT vote-anchor manifest enumerating per-participant stance tokens (C-35), bilateral ACCEPTABLE/FAILS pairs on all content-fill VALIDATE rules (C-36), INERTIA RECORD and STANCE MANIFEST as named first-class skeleton sections (C-37), commit blocks cross-reference manifest sections by named heading (C-38), bilateral VALIDATE at essential-criterion declaration checkpoints (C-39). The gap to 156/156 is C-40 and C-41.

C-40: R15 V-05 declares `## INERTIA RECORD` and `## STANCE MANIFEST` as named first-class skeleton sections (C-37) and has commit blocks reference them by heading (C-38), but neither section carries an explicit seal declaration asserting its own post-commit immutability. The section exists as an independently navigable artifact and a commit-referenced source, but a reviewer reading the section alone sees no stated lifecycle boundary. Adding a terminal `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1` line and a matching `STANCE INVARIANT: sealed at PHASE-3-COMMIT — ...` line to each manifest section makes immutability self-documenting at the artifact level.

C-41: R15 V-05's PHASE-1-COMMIT reads "Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked" and PHASE-3-COMMIT reads "Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked." Both commit blocks name the manifest section by heading (C-38), creating an implied bidirectional link. C-41 requires that implication to be stated: the commit must include an explicit coupling clause declaring that modifications to the named section require updating the commit and vice versa. Without the clause, the pointer is navigational; with the clause, it is a declared contract. Both C-40 and C-41 are surgical additions with no dependency conflicts — neither disturbs any passing criterion.

Variation axes selected:
- Single-axis V-01: Lifecycle emphasis — minimal diff from R15 V-01. Targeted upgrades: (1) INERTIA RECORD section gains terminal `INERTIA INVARIANT:` seal line (C-40); (2) STANCE MANIFEST section gains terminal `STANCE INVARIANT:` seal line (C-40); (3) PHASE-1-COMMIT cross-reference extended with explicit bidirectionality constraint clause (C-41); (4) PHASE-3-COMMIT cross-reference extended with explicit bidirectionality constraint clause (C-41).
- Single-axis V-02: Output format — flat command sequence without skeleton pre-declaration. Tests whether C-40 seal declarations and C-41 bidirectionality clauses are satisfiable outside the two-step skeleton architecture. INERTIA INVARIANT and STANCE INVARIANT PRINT instructions added as direct commands; commit cross-references extended with bidirectionality clauses.
- Single-axis V-03: Phrasing register — conversational framing with structured skeleton. C-40 seal and C-41 bidirectionality requirements woven into readable Phase 1 and Phase 3 guidance in a natural-language register. Tests whether seal declarations and coupling contracts survive mixed-register framing.
- Combined V-04: Lifecycle emphasis + Inertia framing — full skeleton with Inertia-Advocate as structural invariant (synthesized if absent from charter). C-40 expressed as the "Inertia Invariant" identity: the INERTIA RECORD's seal is framed as the investigation's contract, not merely a lifecycle marker. C-41 bidirectionality clause elevated to a named coupling contract with explicit violation semantics.
- Full synthesis V-05: All axes combined — skeleton + imperative fill rules + C-38 cross-reference enforcement + C-39 bilateral at every declaration checkpoint + C-40 seal declarations with VALIDATE coverage + C-41 bidirectionality clauses with VALIDATE coverage + role-sequence tie-break elevation + inertia-first investigation identity (targets 156/156).

---

## V-01 — Single-Axis: Lifecycle Emphasis — C-40 Seal Declarations + C-41 Bidirectionality Clauses

**Variation axis**: Lifecycle emphasis — minimal diff from R15 V-01. Four targeted upgrades from R15: (1) skeleton `## INERTIA RECORD` section gains a terminal `INERTIA INVARIANT: ___` placeholder line; (2) skeleton `## STANCE MANIFEST` section gains a terminal `STANCE INVARIANT: ___` placeholder line; (3) PHASE-1-COMMIT block's cross-reference clause is extended with an explicit bidirectionality constraint statement; (4) PHASE-3-COMMIT block's cross-reference clause is extended with an explicit bidirectionality constraint statement. Corresponding fill instructions added in Phase 1 and Phase 3 fill rules. All other elements preserved from R15 V-01 intact.

**Hypothesis**: R15 V-01 scored 152/152 against v15. Against v16, C-38 remains satisfied — commit blocks already name manifest sections by heading. C-40 and C-41 are the only gaps. The seal declaration adds one terminal line to each manifest section (already independently navigable); the bidirectionality clause extends the commit cross-reference sentence with a coupling obligation statement. Neither change touches C-28 (skeleton pre-declared), C-30 (imperative fill rules), C-36 (bilateral VALIDATE on content-fill criteria), C-37 (named first-class sections), or C-38 (heading cross-reference). Expected: 156/156.

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

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked.
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

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted.
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
VALIDATE: Committee Type is declared correctly in the opening position.
  ACCEPTABLE: `Committee Type — ROB` — recognized type declared before any other content; passes C-01
  ACCEPTABLE: `Committee Type — arch-board` — recognized type; declared in opening position
  FAILS: `Committee Type — unspecified` — type not named; a simulation that proceeds without declaring the committee type fails C-01
  FAILS: `Committee Type — product review meeting` — non-standard label; use ROB, shiproom, arch-board, or the user-specified type from the request
PRINT: Agenda Item — the specific item under review as stated in the request.
PRINT: Charter Source — `.craft/roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [charter-defined orientation in one phrase]`.
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

GATE-1 intra-phase retry loop:
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

PRINT: INERTIA INVARIANT — the terminal line of ## INERTIA RECORD, asserting the section's post-commit immutability.
  PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.`
  VALIDATE: seal declaration is present as a stated assertion in the section, not inferred from phase position.
    ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.`
    FAILS: section with correct entries but no INERTIA INVARIANT line — immutability is assumed from the phase boundary, not declared at the artifact level

ENFORCE: ## INERTIA RECORD is an independently addressable section; it appears before PHASE-1-COMMIT.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD. Phase 1 closed.
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
  ACCEPTABLE: `Result: NO — Tier 1 contains [Architect] and [Security Lead]; challenger-first ordering valid`
  FAILS: `Result: YES` followed by continuation without reassignment — SORT-CHECK gate answered YES but no reassignment performed; fails C-18 and C-22
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
ENFORCE: named label is the first element after `CITE:`; prose before the label fails C-20.
VALIDATE: CITE: references a named label from ## INERTIA RECORD.
  ACCEPTABLE: `CITE: INERTIA-FINDING-A — workflow-disruption: the migration plan directly addresses this cost by...`
  ACCEPTABLE: `CITE: INERTIA-FINDING-C — re-training overhead: the phased rollout reduces this because...`
  FAILS: `CITE: The workflow disruption finding supports adoption...` — finding referenced by paraphrase, no INERTIA-FINDING-* label
  FAILS: `CITE: (a) — workflow-disruption` — parenthesized letter, not the INERTIA-FINDING-A token

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
REQUIRE: quoted string names a specific finding or concern.
VALIDATE: RESPONDS-TO: names and quotes a specific concern — generic acknowledgment fails.
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-A: workflow-disruption" — the migration plan stages the transition to avoid hard cutover`
  ACCEPTABLE: `RESPONDS-TO: "[Architect]'s concern that the webhook contract will break" — the adapter layer preserves the existing contract`
  FAILS: `RESPONDS-TO: "Inertia concerns have been acknowledged"` — generic, no attribution
  FAILS: `RESPONDS-TO: "The challenger raised valid points"` — no specific attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE means Phase 2 sort is invalid — REOPEN Phase 2; RE-ASSIGN tiers; RE-PRINT corrected TIER SORT; RE-RUN SORT-CHECK.

WRITE: ## STANCE MANIFEST — fill the named section after all participant voices are written:
  PRINT one entry per participant in format `[Role Name] STANCE-TOKEN` — derived from locked STANCE: declarations above.
  ENFORCE: ## STANCE MANIFEST is an independently addressable section; it appears before PHASE-3-COMMIT.

PRINT: STANCE INVARIANT — the terminal line of ## STANCE MANIFEST, asserting the section's post-commit immutability.
  PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
  VALIDATE: seal declaration is present as a stated assertion in the section, not inferred from phase position.
    ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
    FAILS: section with correct entries but no STANCE INVARIANT line — immutability assumed, not declared

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` after the last Phase 3 voice block and before Phase 5.
COUNT: each entry in ## STANCE MANIFEST — one tally count per STANCE-TOKEN category.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
VALIDATE: TALLY counts match ## STANCE MANIFEST exactly; mismatch fails C-35.
  ACCEPTABLE: `TALLY: 2 APPROVE · 1 CONDITION · 1 BLOCK` when ## STANCE MANIFEST contains exactly 2 APPROVE, 1 CONDITION, 1 BLOCK entries
  FAILS: tally count differing from ## STANCE MANIFEST token count — mismatch indicates re-parsing Phase 3 prose rather than counting the manifest
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

## V-02 — Single-Axis: Output Format — Flat Command Sequence with C-40 Seal Declarations + C-41 Bidirectionality Clauses

**Variation axis**: Output format — flat command sequence without skeleton pre-declaration. All structural requirements are expressed as direct imperative commands in a single execution sequence. Tests whether C-40 seal declarations and C-41 bidirectionality constraint clauses are satisfiable outside the two-step skeleton architecture. INERTIA INVARIANT and STANCE INVARIANT appear as explicit PRINT instructions after their respective manifest-section writes. Commit cross-references are extended with bidirectionality constraint clauses inline.

**Hypothesis**: C-28 (skeleton pre-declaration) is aspirational and this axis tests C-40 and C-41 in isolation from it. The flat format can express both the INERTIA INVARIANT seal as a PRINT command after the ## INERTIA RECORD write and the STANCE INVARIANT seal as a PRINT command after the ## STANCE MANIFEST write. The commit bidirectionality clause is expressed as an extended commit PRINT instruction. Expected: satisfies C-40 and C-41 but misses C-28 (2 pts); ceiling ~154/156. Confirms that seal declarations and coupling contracts are phrasing requirements independent of architecture.

---

You are running `org:committee`. Execute the following phases in order. Complete each phase fully and print its PHASE-N-COMMIT: block before beginning the next phase.

---

**PHASE 0 — COMMITTEE DECLARATION**

PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
VALIDATE: Committee Type is declared correctly.
  ACCEPTABLE: `Committee Type — ROB` — recognized type declared in the opening line of output
  ACCEPTABLE: `Committee Type — shiproom` — recognized type; declared before any participant or investigation content
  FAILS: `Committee Type — unspecified` — type not named; simulation cannot proceed without a declared committee type
  FAILS: `Committee Type — weekly sync` — non-standard label; must be ROB, shiproom, arch-board, or the explicit user-specified type
LOAD: charter from `.craft/roles/` matching this committee type; extract named roles with documented orientations.
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

PRINT: terminal seal declaration as the last line of ## INERTIA RECORD before PHASE-1-COMMIT:
  `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.`
ENFORCE: `## INERTIA RECORD` is independently navigable by section heading; manifests embedded only in commit block text fail C-37.

PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked. Downstream CITE: and RESPONDS-TO: valid only against labels listed in ## INERTIA RECORD. Phase 1 closed.
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
  VALIDATE: RESPONDS-TO: names and quotes a specific concern.
    ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-C: team habit-break" — the training runway absorbs the transition cost`
    ACCEPTABLE: `RESPONDS-TO: "[Architect]'s concern that integration contracts will break" — the adapter layer preserves them`
    FAILS: `RESPONDS-TO: "the skeptics have been noted"` — generic, no attribution
    FAILS: `RESPONDS-TO: "concerns acknowledged"` — no specific attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen and tier reassignment.

WRITE: `## STANCE MANIFEST` as a named section header after all participant voices are written and before PHASE-3-COMMIT.
  PRINT under that header: one entry per participant in format `[Role Name] STANCE-TOKEN`
  ENFORCE: ## STANCE MANIFEST is independently navigable by section heading; manifests embedded only in commit block text fail C-37.

PRINT: terminal seal declaration as the last line of ## STANCE MANIFEST before PHASE-3-COMMIT:
  `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
ENFORCE: seal declaration is a stated assertion at the artifact level; absence fails C-40.

PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST token count; re-parsing Phase 3 prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
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

## V-03 — Single-Axis: Phrasing Register — Conversational Framing with C-40 Seal Declarations + C-41 Bidirectionality Clauses

**Variation axis**: Phrasing register — conversational framing with structured skeleton. The two-step skeleton architecture is preserved. Phase 1 and Phase 3 fill guidance is written in a readable explanatory register describing what the seal declarations mean and why the coupling clauses matter. ENFORCE and PRINT commands retain their imperative register; the explanatory guidance around C-40 and C-41 is conversational. Tests whether seal language and bidirectionality constraint requirements survive a mixed-register prompt without drifting into optionality.

**Hypothesis**: A conversational register for C-40 and C-41 risks making the seal and coupling language sound advisory rather than required. V-03 tests whether the distinction can be preserved when the surrounding instructions are written as guidance rather than commands. The skeleton already carries both INERTIA INVARIANT and STANCE INVARIANT placeholder lines plus extended commit language, so the structural declarations are pre-committed regardless of fill-rule register. Expected: passes C-40 and C-41; may score partial on C-30 (imperative micro-instructions) if the conversational framing for seal fill rules is read as descriptive. Net estimate: 152–156/156.

---

You are running `org:committee` — a pre-meeting simulation. The goal is to surface surprises before the real committee meets. Work in two steps: first print the full structure you are about to produce; then fill it.

---

### STEP 1 — PRINT THIS SKELETON

Before writing any simulation content, print the following structure with all headers, field labels, and blank slots visible.

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
  INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

PHASE-1-COMMIT: [locked] — Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked.
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
  STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
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

Work through each phase in order.

---

**Phase 0 — Who is in the room**

The first thing to establish is which type of committee is meeting. The recognized types are ROB (Review of Business), shiproom (go/no-go on a release), and arch-board (architecture decision review) — or whatever type the user specified in their request.

Declare the committee type clearly before anything else. Here is what a correct declaration looks like versus a problem:
  A correct opening: `Committee Type — ROB` — a recognized type stated in the first position
  A wrong opening: `Committee Type — unspecified` — no type declared; the simulation cannot proceed without knowing what room we are in
  Also wrong: `Committee Type — leadership meeting` — this is not a recognized type; use one of the three standard types or the user's explicitly named type

Load the charter file from `.craft/roles/` that matches this committee type. Pull every role with its documented orientation. If no charter exists, say so explicitly and fall back to Signal defaults (PM, Architect, Inertia-Advocate). Fill Committee Type, Agenda Item, Charter Source, and the Participants list.

ENFORCE: PHASE-0-COMMIT: is the last thing in Phase 0. Nothing follows it until the Phase 1 header.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded.
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 1 — What are we actually disrupting**

Before anyone speaks, investigate what the proposal is asking people to give up. Four named findings, labeled INERTIA-FINDING-A through D. Use the exact label tokens — not "(a)", not "Finding A" — as the first word on each line.

INERTIA-FINDING-A: name the specific production artifact or workflow being displaced.
INERTIA-FINDING-B: name the integration surface — systems, APIs, contracts, consumers.
INERTIA-FINDING-C: name the team and the specific cognitive habit they would lose.
INERTIA-FINDING-D: the most important one — the non-obvious cost the proposal author almost certainly did not see coming.

Run GATE-1. If INERTIA-FINDING-D passes the non-obviousness test, proceed. If not, label the whole block as INVESTIGATION-ATTEMPT-1, start INVESTIGATION-ATTEMPT-2, and repeat until a gate answers YES.

Fill the `## INERTIA RECORD` section with one line per finding, format `INERTIA-FINDING-[X]: [anchor]`. Each anchor must identify the finding without reading the investigation prose:
  Correct: `INERTIA-FINDING-A: legacy-deploy-script` — the finding is identifiable from the record alone
  Wrong: `INERTIA-FINDING-A:` — no anchor text; the record would be useless for citation verification
  Wrong: `INERTIA-FINDING-B: [anchor]` — placeholder was never filled; this is not a real entry

The last line of `## INERTIA RECORD` is the seal declaration. This is not optional — it is the line that makes the section self-documenting. Without it, a reviewer reading the record has no stated lifecycle boundary; they must infer immutability from the phase structure rather than reading it in the artifact. Fill the `INERTIA INVARIANT: ___` placeholder with:
  `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.`

ENFORCE: ## INERTIA RECORD appears before PHASE-1-COMMIT and is independently navigable.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked. Downstream CITE: and RESPONDS-TO: valid only against labels in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

The commit's cross-reference is not just a pointer — it is a contract. Notice that the commit names the section by heading and then states the coupling obligation in both directions. That clause is what converts the reference from navigational to governed: if the INERTIA RECORD changes, the commit must change; if the commit changes, the record must change. Both directions are stated explicitly.

---

**Phase 2 — Who is skeptical and who is aligned**

Assign every participant to one of three tiers: Tier 1 (CHALLENGERS) are the roles whose job is to interrogate risk — they speak first. Tier 2 (CONDITIONALS) hold approval pending specific conditions. Tier 3 (ADVOCATES) are the believers — they speak last. Run the SORT-CHECK gate. If the answer is YES (Tiers 1 and 2 are empty), name a challenger-appropriate role, reassign it, reprint the sort, and rerun the check until the answer is NO.

ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 3 — Voices**

Tier 1 speaks first, then Tier 2, then Tier 3. For each participant, the very first thing is a `STANCE:` line — standalone label, single token. No qualifications in the token; no stance buried in prose.

Tier 1 voices ground their concerns in named INERTIA-FINDING labels from ## INERTIA RECORD. Tier 2 voices name the specific approval condition precisely — "address concerns" fails. Tier 3 voices fill both `CITE:` and `RESPONDS-TO:` before any endorsement prose.

CITE: must open with the INERTIA-FINDING-* label token, not a paraphrase:
  Correct: `CITE: INERTIA-FINDING-B — webhook-contract: the adapter preserves...`
  Wrong: `CITE: The integration finding supports...` — no label token

RESPONDS-TO: must quote or name the specific concern:
  Correct: `RESPONDS-TO: "INERTIA-FINDING-C: team habit-break" — the training runway absorbs...`
  Wrong: `RESPONDS-TO: "concerns noted"` — generic acknowledgment, no attribution

After all voices, fill `## STANCE MANIFEST` — one entry per participant in format `[Role Name] STANCE-TOKEN`. The last line of the manifest is the seal declaration. Like the INERTIA INVARIANT in Phase 1, this line exists so that a reviewer reading the manifest knows it is closed. Fill the `STANCE INVARIANT: ___` placeholder with:
  `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`

ENFORCE: ## STANCE MANIFEST appears before PHASE-3-COMMIT and is independently navigable.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST token count; re-parsing Phase 3 prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 4 — Tally**

Count each stance token in ## STANCE MANIFEST. Print `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line. Derive OUTCOME from the tally.

ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**Phase 5 — Minutes**

Verdict matches OUTCOME exactly. Conditions for full approval must be specific deliverables. If verdict is not APPROVED, Owner and Trigger must both be present — a re-entry path missing either field is incomplete. Action items carry three fields every time: Owner Role, specific action, deadline. Dissenting opinions cite INERTIA-FINDING-* labels from ## INERTIA RECORD where applicable and name a concrete resolution trigger.

ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing — Inertia Invariant as Structural Identity

**Variation axis**: Lifecycle emphasis + Inertia framing — full skeleton with Inertia-Advocate synthesized as a mandatory participant if absent from charter. C-40 is framed as the "Inertia Invariant" structural identity: the INERTIA RECORD section's seal declaration is not merely a lifecycle marker — it is the investigation's contract with the simulation. The INERTIA INVARIANT line asserts that the switching-cost findings produced by Phase 1 are the fixed adversarial floor against which every advocate voice is tested. C-41 is expressed with maximum contractual force: the commit coupling clause is labeled as the bidirectionality contract, and violations in either direction are named as rule failures.

**Hypothesis**: Inertia framing elevates C-40 from a structural requirement to a design principle: the INERTIA INVARIANT is the reason the simulation has a commit architecture at all. This axis tests whether surfacing the invariant's purpose (not just its form) produces more reliable seal and coupling clause generation. The Inertia-Advocate role makes the inertia framing concrete — a named participant whose arguments are grounded in sealed findings. Expected: 156/156, with particularly strong C-12 and C-27 scores.

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
  - Inertia-Advocate — ___  [load from charter or synthesize: defends current-state workflow against disruption]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded (Inertia-Advocate confirmed present).
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___  [current-state workflow displaced]
INERTIA-FINDING-B: ___  [integration surface at risk]
INERTIA-FINDING-C: ___  [team + cognitive habit]
INERTIA-FINDING-D: ___  [non-obvious switching cost]

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[GATE-1 NO → INVESTIGATION-ATTEMPT-2 within Phase 1; Phase 2 is unconditional]

[Additional INVESTIGATION-ATTEMPT-N / GATE-N blocks as needed until YES]

## INERTIA RECORD

INERTIA-FINDING-A: ___  [one-phrase anchor]
INERTIA-FINDING-B: ___  [one-phrase anchor]
INERTIA-FINDING-C: ___  [one-phrase anchor]
INERTIA-FINDING-D: ___  [one-phrase anchor]

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1. These findings are the adversarial floor for all advocate voices.

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___  [Inertia-Advocate is always Tier 1]
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → reassign: ___ to Tier ___ because ___; corrected TIER SORT follows / NO → valid]

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, Inertia-Advocate in Tier 1, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

## PHASE 3 — PARTICIPANT VOICES

[Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
___
CITE: ___ — ___           [Tier 3 only]
RESPONDS-TO: "___" — ___  [Tier 3 only]

[Repeat block per participant; Inertia-Advocate block must reference INERTIA-FINDING-D explicitly]

## STANCE MANIFEST

  [___] ___
  [___] ___
  [repeat per participant — format: [Role Name] STANCE-TOKEN]

STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted.
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
CONFIRM: Inertia-Advocate role is present in the participant list — the role whose function is to defend the current-state workflow against the proposal.
ENFORCE: if no charter file exists — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback participants: PM, Architect, Inertia-Advocate with Signal-default orientations.
ENFORCE: if charter exists but contains no role matching Inertia-Advocate function — SYNTHESIZE an Inertia-Advocate role with orientation `defends current-state workflow against disruption`; add to participant list; note `[synthesized — no charter role with inertia function found]`.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
VALIDATE: Committee Type is declared correctly in the opening position.
  ACCEPTABLE: `Committee Type — ROB` — recognized type declared before any other content; passes C-01
  ACCEPTABLE: `Committee Type — arch-board` — recognized type; declared in opening position
  FAILS: `Committee Type — unspecified` — type not named; simulation cannot proceed; fails C-01
  FAILS: `Committee Type — product review meeting` — non-standard label; use ROB, shiproom, arch-board, or user-specified type
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — `.craft/roles/` path used, or fallback declaration.
PRINT: Participants — one line per loaded role; format `[Role Name] — [orientation in one phrase]`.
CONFIRM: Inertia-Advocate appears in the Participants list before PHASE-0-COMMIT.
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded (Inertia-Advocate confirmed present).
  | ENFORCE: terminal position — NO PHASE 0 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 1 fill rules — Investigation as the Inertia-Advocate's brief:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process in production that this agenda item displaces; this is what the Inertia-Advocate is defending.
  ENFORCE: precision required; a generic "current process" fails.
  VALIDATE: finding label is the first token on the line.
    ACCEPTABLE: `INERTIA-FINDING-A: legacy-approval-workflow — the team currently routes all changes through...`
    FAILS: `(a) legacy-approval-workflow` — parenthesized letter, not the INERTIA-FINDING-A token

WRITE: INERTIA-FINDING-B — name the integration surface at risk; specific systems, APIs, contracts, or downstream consumers.
  VALIDATE: finding label is the first token on the line.
    ACCEPTABLE: `INERTIA-FINDING-B: webhook-contract — the Notification Service depends on...`
    FAILS: `(b) webhook-contract` — parenthesized letter

WRITE: INERTIA-FINDING-C — name the team whose cognitive habits would break and the specific decision-making habit they rely on today.
  ENFORCE: name both the team and the habit; generic attribution fails.

WRITE: INERTIA-FINDING-D — the non-obvious switching cost the proposal author almost certainly did not account for; specific enough that the author would say "I missed that." This finding is the Inertia-Advocate's primary argument.

GATE-1 intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → fill ## INERTIA RECORD and PHASE-1-COMMIT; Phase 2 is unconditional.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels from a different angle; re-evaluate; REPEAT.

WRITE: ## INERTIA RECORD — the Inertia-Advocate's sealed brief:
  PRINT: INERTIA-FINDING-A: [one-phrase anchor]
  PRINT: INERTIA-FINDING-B: [one-phrase anchor]
  PRINT: INERTIA-FINDING-C: [one-phrase anchor]
  PRINT: INERTIA-FINDING-D: [one-phrase anchor]
  VALIDATE: each entry carries a content anchor readable without Phase 1 prose.
    ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption` — keyword identifies the finding
    ACCEPTABLE: `INERTIA-FINDING-D: undocumented-cache-dependency` — names the non-obvious cost
    FAILS: `INERTIA-FINDING-A:` — bare label, no anchor; fails C-34
    FAILS: `INERTIA-FINDING-A: [one-phrase anchor]` — unfilled placeholder; fails C-34

PRINT: the INERTIA INVARIANT seal declaration as the terminal line of ## INERTIA RECORD:
  ENFORCE: this line is not optional — it is the structural declaration that makes ## INERTIA RECORD self-documenting.
  PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1. These findings are the adversarial floor for all advocate voices.`
  VALIDATE: seal declaration is an explicit assertion in the section, not inferred from phase position.
    ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1. These findings are the adversarial floor for all advocate voices.`
    FAILS: ## INERTIA RECORD with correct entries but no INERTIA INVARIANT line — immutability is assumed, not declared; fails C-40

ENFORCE: ## INERTIA RECORD is an independently addressable section; it appears before PHASE-1-COMMIT.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: terminal position — NO PHASE 1 CONTENT MAY FOLLOW THIS LINE.

ENFORCE: the bidirectionality clause in PHASE-1-COMMIT is a declared contract — "modifications to that record require updating this commit; modifications to this commit require updating that record" — both directions stated, not implied.
VALIDATE: bidirectionality clause is present as stated text in the PHASE-1-COMMIT block.
  ACCEPTABLE: PHASE-1-COMMIT includes "modifications to that record require updating this commit; modifications to this commit require updating that record" — coupling obligation stated in both directions
  FAILS: PHASE-1-COMMIT reads only "Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked" — navigational pointer, no coupling contract; fails C-41

---

**PHASE 2 fill rules:**

ASSIGN: Tier 1 (CHALLENGERS) — roles interrogating feasibility, risk, or disruption; ENFORCE: Inertia-Advocate is always Tier 1.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals; ENFORCE: speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first.

SORT-CHECK (intra-phase loop):
PRINT: `Test: Tier 1 and Tier 2 both empty?`
CONFIRM: Result YES or NO.
  IF YES: reassign a challenger-appropriate role (prioritize roles grounded in INERTIA-FINDING findings); RE-PRINT TIER SORT; RE-PRINT SORT-CHECK; LOOP until NO.
  ACCEPTABLE: `Result: NO — Tier 1 contains [Inertia-Advocate] and [Security Lead]; ordering valid`
  FAILS: `Result: YES` with no reassignment; fails C-18 and C-22
CONFIRM: Result NO is the Phase 2 exit condition.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, Inertia-Advocate in Tier 1, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: terminal position — NO PHASE 2 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 before Tier 3.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose.
VALIDATE: STANCE: is a committed structural declaration.
  ACCEPTABLE: `STANCE: BLOCK` on its own line — unambiguous before any rationale
  FAILS: `The architect views this as too risky` — stance in prose, no label
  FAILS: `STANCE: BLOCK (pending clarification)` — qualified token softens the declaration

WRITE: 2-4 sentences per participant from charter orientation.
REQUIRE (Tier 1 / Inertia-Advocate): ENFORCE Inertia-Advocate explicitly references INERTIA-FINDING-D by label — the non-obvious finding is the Inertia-Advocate's primary argument.
REQUIRE (Tier 1 other): ground concern in named INERTIA-FINDING labels.
REQUIRE (Tier 2): name specific approval condition; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [finding content]`
ENFORCE: named label is the first element after CITE:.
VALIDATE:
  ACCEPTABLE: `CITE: INERTIA-FINDING-A — workflow-disruption: the migration plan addresses this by...`
  FAILS: `CITE: The workflow finding supports adoption...` — no label token
  FAILS: `CITE: (a) — workflow-disruption` — parenthesized letter

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence]`
VALIDATE:
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-D: [cost]" — the mitigation plan accounts for this by...`
  ACCEPTABLE: `RESPONDS-TO: "[Inertia-Advocate]'s concern that [X]" — the adapter layer addresses it`
  FAILS: `RESPONDS-TO: "concerns have been noted"` — generic

VALIDATE: at least one CONDITION or BLOCK stance; all-APPROVE triggers Phase 2 reopen.

WRITE: ## STANCE MANIFEST — fill after all voices:
  PRINT one entry per participant: `[Role Name] STANCE-TOKEN`
  ENFORCE: independently addressable section; appears before PHASE-3-COMMIT.

PRINT: STANCE INVARIANT seal declaration as the terminal line of ## STANCE MANIFEST:
  PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
  VALIDATE:
    ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
    FAILS: ## STANCE MANIFEST with correct entries but no STANCE INVARIANT line — fails C-40

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: terminal position — NO PHASE 3 CONTENT MAY FOLLOW THIS LINE.

ENFORCE: bidirectionality clause is present in PHASE-3-COMMIT — "modifications to that manifest require updating this commit; modifications to this commit require updating that manifest."
VALIDATE:
  ACCEPTABLE: PHASE-3-COMMIT includes bidirectionality clause naming both directions of coupling obligation
  FAILS: PHASE-3-COMMIT reads only "Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked" — pointer without coupling contract; fails C-41

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line.
COUNT: each token in ## STANCE MANIFEST — one count per STANCE-TOKEN category.
VALIDATE:
  ACCEPTABLE: `TALLY: 2 APPROVE · 1 CONDITION · 1 BLOCK` matching ## STANCE MANIFEST exactly
  FAILS: tally differing from manifest token count
WRITE: OUTCOME — all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: terminal position — NO PHASE 4 CONTENT MAY FOLLOW THIS LINE.

---

**PHASE 5 fill rules:**

WRITE: Verdict — matches OUTCOME exactly.
WRITE: Conditions — specific deliverables; "address feedback" fails.
REQUIRE (not APPROVED): Owner (named role, not team) and Trigger (named artifact or event); both fields required.
VALIDATE: both Owner and Trigger present; path missing either field is incomplete; fails C-23.

PRINT: `[Owner Role] — [specific action] — [deadline]` per action item.
REQUIRE: all three fields; "investigate further" without specifying question, artifact, and recipient fails.

WRITE: dissent per CONDITION or BLOCK stance — objection citing INERTIA-FINDING-* label, resolution path, concrete trigger, named authority.
ENFORCE: if no dissent — PRINT: `No dissent — [reason]`.
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: terminal position — NO PHASE 5 CONTENT MAY FOLLOW THIS LINE.

---

## V-05 — Full Synthesis: All Axes — C-40 + C-41 + Full Rubric Compliance

**Variation axis**: All axes combined — skeleton pre-declaration (C-28), imperative fill rules (C-30), named INERTIA-FINDING labels with content anchors (C-27, C-34), intra-phase gate loops (C-29), PHASE-N-COMMIT: terminal markers with ENFORCE blocking assertions (C-31, C-32), Phase 1 citation-anchor manifest (C-33, C-34), Phase 3 vote-anchor manifest (C-35), bilateral ACCEPTABLE/FAILS pairs on all content-fill VALIDATE rules (C-36), INERTIA RECORD and STANCE MANIFEST as named first-class skeleton sections (C-37), commit blocks cross-reference manifest sections by heading (C-38), bilateral VALIDATE at essential-criterion declaration checkpoints (C-39), explicit INERTIA INVARIANT and STANCE INVARIANT seal declarations in each manifest section (C-40), explicit bidirectionality constraint clauses in both PHASE-1-COMMIT and PHASE-3-COMMIT cross-references (C-41), Inertia-Advocate as mandatory participant (C-12 maximized), role-sequence tie-break stated explicitly (C-11).

**Hypothesis**: The synthesis combines every structural, phrasing, and lifecycle requirement into the tightest compliant prompt. C-40 and C-41 add two discrete fill instructions and two discrete VALIDATE rules. The seal declarations are PRINT instructions at the terminal position of each manifest section; the bidirectionality clauses are ENFORCE instructions following each commit PRINT. No existing criterion is disturbed. Expected: 156/156.

---

You are running `org:committee`. Execute in two steps: (1) print the skeleton, (2) fill it.

---

### STEP 1 — PRINT THIS SKELETON

Print the complete skeleton below before generating any simulation content. Print every section header, field label, `___` placeholder, PHASE-N-COMMIT: block, and INERTIA/STANCE INVARIANT slot. Do not fill any values in this step.

```
=== org:committee SIMULATION — SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [repeat per participant]
  [Inertia-Advocate — ___ : synthesize if absent from charter]

PHASE-0-COMMIT: [locked] — Committee Type: ___, Agenda Item: ___, Charter Source: ___, Participants: ___ roles loaded (Inertia-Advocate confirmed present).
  | ENFORCE: this marker is the terminal element of Phase 0; no Phase 0 content may follow this line.

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

INERTIA INVARIANT: sealed at PHASE-1-COMMIT — ___

PHASE-1-COMMIT: [locked] — Investigation attempt ___ complete, GATE-___ answered YES.
  Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked.
  Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD.
  Phase 1 closed.
  | ENFORCE: this marker is the terminal element of Phase 1; no Phase 1 content may follow this line.

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___  [Inertia-Advocate is always Tier 1]
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___  [higher veto authority speaks first within tier]

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES → reassign: ___ to Tier ___ because ___; corrected TIER SORT follows / NO → valid]

[Result YES → re-output corrected TIER SORT + new SORT-CHECK; repeat until NO]

PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, Inertia-Advocate in Tier 1, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: this marker is the terminal element of Phase 2; no Phase 2 content may follow this line.

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

STANCE INVARIANT: sealed at PHASE-3-COMMIT — ___

PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked.
  Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted.
  All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: this marker is the terminal element of Phase 3; no Phase 3 content may follow this line.

---

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: this marker is the terminal element of Phase 4; no Phase 4 content may follow this line.

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
  | ENFORCE: this marker is the terminal element of Phase 5; no Phase 5 content may follow this line.

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom using the imperative fill rules below.

---

**PHASE 0 fill rules:**

LOAD: charter from `.craft/roles/` matching this committee type; extract every named role with documented orientation.
CONFIRM: Inertia-Advocate role present — role whose function is defending the current-state workflow against disruption.
ENFORCE: if no charter — WRITE Charter Source as `Signal defaults — no charter found`; LOAD fallback: PM, Architect, Inertia-Advocate.
ENFORCE: if charter has no Inertia-function role — SYNTHESIZE Inertia-Advocate with orientation `defends current-state workflow against disruption`; append `[synthesized]` to participant entry.
PRINT: Committee Type — one of ROB, shiproom, arch-board, or the user-specified type from the request.
VALIDATE: Committee Type is declared correctly in the opening position.
  ACCEPTABLE: `Committee Type — ROB` — recognized type declared before any other content; passes C-01
  ACCEPTABLE: `Committee Type — arch-board` — recognized type; declared in opening position
  FAILS: `Committee Type — unspecified` — type not named; simulation cannot proceed without declared committee type; fails C-01
  FAILS: `Committee Type — product review meeting` — non-standard label; use ROB, shiproom, arch-board, or user-specified type from request
PRINT: Agenda Item — the specific item under review.
PRINT: Charter Source — `.craft/roles/` path, or fallback declaration.
PRINT: Participants — one line per role; format `[Role Name] — [orientation in one phrase]`.
VALIDATE: Participants list includes Inertia-Advocate; absence fails C-02.
  ACCEPTABLE: participant list includes `Inertia-Advocate — defends current-state workflow against disruption` (or equivalent charter role)
  FAILS: participant list with no role covering inertia function — the committee has no current-state defender; fails C-02 and C-12
ENFORCE: PHASE-0-COMMIT: is the terminal element of Phase 0 — no Phase 0 content may appear after it.
PRINT: PHASE-0-COMMIT: [locked] — Committee Type: [value], Agenda Item: [value], Charter Source: [value], Participants: [N] roles loaded (Inertia-Advocate confirmed present).
  | ENFORCE: this marker is the terminal element of Phase 0; no Phase 0 content may follow this line.

---

**PHASE 1 fill rules:**

LABEL: `INVESTIGATION-ATTEMPT-1` before writing any finding.

WRITE: INERTIA-FINDING-A — name the specific workflow, tool, or process currently in production that this agenda item displaces; this is what the Inertia-Advocate is defending.
  ENFORCE: precision required; generic "current process" fails.
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

WRITE: INERTIA-FINDING-D — name the non-obvious switching cost the proposal author almost certainly did not account for; the Inertia-Advocate's primary argument.
  REQUIRE: specific enough that the author would say "I missed that."

GATE-1 intra-phase retry loop:
CONFIRM: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
WRITE: Answer YES or NO with one-sentence basis.

ENFORCE: the gate loop runs within Phase 1; Phase 2 is always reached:
  IF GATE-N Answer: YES → fill ## INERTIA RECORD and PHASE-1-COMMIT immediately; Phase 2 is unconditional.
  IF GATE-N Answer: NO → INCREMENT N; LABEL: INVESTIGATION-ATTEMPT-N+1; WRITE: four new INERTIA-FINDING-* labels rewritten from a different angle; GATE-N+1 same question; re-evaluate; REPEAT.

REQUIRE: each rewrite produces a new labeled block with incremented INVESTIGATION-ATTEMPT-N label; unlabeled rewrite fails C-22 and C-24.

CONFIRM: INERTIA-FINDING-A through D from the passing attempt are the active committee record.

WRITE: ## INERTIA RECORD — fill from the passing attempt's findings:
  PRINT: INERTIA-FINDING-A: [one-phrase anchor]
  PRINT: INERTIA-FINDING-B: [one-phrase anchor]
  PRINT: INERTIA-FINDING-C: [one-phrase anchor]
  PRINT: INERTIA-FINDING-D: [one-phrase anchor]
  VALIDATE: each entry carries a content anchor readable without Phase 1 prose.
    ACCEPTABLE: `INERTIA-FINDING-A: workflow-disruption` — keyword identifies the finding
    ACCEPTABLE: `INERTIA-FINDING-B: re-training overhead` — two-word anchor identifies the cost
    FAILS: `INERTIA-FINDING-A:` — bare label with no anchor; fails C-34
    FAILS: `INERTIA-FINDING-A: [one-phrase anchor]` — unfilled skeleton placeholder; fails C-34

PRINT: INERTIA INVARIANT seal declaration as the terminal line of ## INERTIA RECORD:
  ENFORCE: this line is required — it makes the section's post-commit immutability self-documenting.
  PRINT: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.`
  VALIDATE: seal declaration is an explicit assertion in the section body.
    ACCEPTABLE: `INERTIA INVARIANT: sealed at PHASE-1-COMMIT — findings may not be added, removed, or modified without reopening Phase 1.`
    FAILS: ## INERTIA RECORD with correct anchor entries but no INERTIA INVARIANT line — section is navigable and cited but carries no stated lifecycle boundary; fails C-40

ENFORCE: ## INERTIA RECORD is an independently addressable section; it appears before PHASE-1-COMMIT.
ENFORCE: PHASE-1-COMMIT: is the terminal element of Phase 1 — no Phase 1 content may appear after it.
PRINT: PHASE-1-COMMIT: [locked] — Investigation attempt [N] complete, GATE-[N] answered YES. Citation-anchor manifest declared in ## INERTIA RECORD above — modifications to that record require updating this commit; modifications to this commit require updating that record. Findings A–D locked. Downstream CITE: and RESPONDS-TO: valid only against labels enumerated in ## INERTIA RECORD. Phase 1 closed.
  | ENFORCE: this marker is the terminal element of Phase 1; no Phase 1 content may follow this line.

VALIDATE: bidirectionality clause is present in PHASE-1-COMMIT block.
  ACCEPTABLE: PHASE-1-COMMIT includes "modifications to that record require updating this commit; modifications to this commit require updating that record" — coupling obligation declared in both directions; passes C-41
  FAILS: PHASE-1-COMMIT reads only "Citation-anchor manifest declared in ## INERTIA RECORD above; findings A–D locked" — heading cross-reference present but coupling obligation unstated; passes C-38, fails C-41

---

**PHASE 2 fill rules:**

LOAD: all participants from Phase 0 roster.
ASSIGN: Tier 1 (CHALLENGERS) — roles interrogating feasibility, risk, or disruption; ENFORCE: Inertia-Advocate is always Tier 1.
ASSIGN: Tier 2 (CONDITIONALS) — roles holding approval pending specific named conditions.
ASSIGN: Tier 3 (ADVOCATES) — roles aligned with the proposal's stated goals; ENFORCE: speak last.
ENFORCE: tie-break within any tier — higher institutional veto authority speaks first; state tie-break rule explicitly in Tie-break field.

SORT-CHECK fill rule (intra-phase loop):
PRINT: Test field as fixed string: `Tier 1 and Tier 2 both empty?`
CONFIRM: Result — YES or NO.
VALIDATE: if Result YES — REQUIRE reassignment: name the mis-sorted role, name the target tier, state the reason grounded in INERTIA-FINDING labels; RE-PRINT corrected TIER SORT; RE-PRINT new SORT-CHECK; LOOP until Result NO.
  ACCEPTABLE: `Result: NO — Tier 1 contains [Inertia-Advocate] and [Security Lead]; challenger-first ordering valid`
  FAILS: `Result: YES` followed by continuation without reassignment — fails C-18 and C-22
ENFORCE: SORT-CHECK must appear as a discrete labeled gate with both `Test:` and `Result:` fields; correct ordering without the gate fails C-25.
CONFIRM: Result NO is the Phase 2 exit condition; Phase 3 fills unconditionally.
ENFORCE: PHASE-2-COMMIT: is the terminal element of Phase 2 — no Phase 2 content may appear after it.
PRINT: PHASE-2-COMMIT: [locked] — TIER SORT complete, SORT-CHECK Result NO, Inertia-Advocate in Tier 1, challenger-first ordering confirmed. Phase 2 closed.
  | ENFORCE: this marker is the terminal element of Phase 2; no Phase 2 content may follow this line.

---

**PHASE 3 fill rules:**

ENFORCE: Tier 1 voices before Tier 2 before Tier 3.

PRINT: `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose for each participant.
VALIDATE: STANCE: is a committed structural declaration — prose must not soften, qualify, or contradict it.
  ACCEPTABLE: `STANCE: BLOCK` on its own line — label + single token, unambiguous before rationale
  ACCEPTABLE: `STANCE: CONDITION` — declares conditional hold before any endorsement text
  FAILS: `The architect views this proposal as too risky to approve at this time` — stance in prose, no STANCE: label
  FAILS: `STANCE: BLOCK (pending clarification)` — qualified token; parenthetical softens the commitment

WRITE: 2-4 sentences per participant from charter orientation responding to this specific agenda item.
REQUIRE (Tier 1 / Inertia-Advocate): ENFORCE reference to INERTIA-FINDING-D by label — this is the Inertia-Advocate's primary argument.
REQUIRE (Tier 1 other): ground concern in named INERTIA-FINDING labels from ## INERTIA RECORD.
REQUIRE (Tier 2): name the specific approval condition precisely; "address concerns" fails.
REQUIRE (Tier 3): fill CITE: and RESPONDS-TO: before endorsement prose.

CITE fill rule (Tier 3 only):
PRINT: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`
ENFORCE: named label is the first element after `CITE:`.
VALIDATE: CITE: references a named label from ## INERTIA RECORD.
  ACCEPTABLE: `CITE: INERTIA-FINDING-A — workflow-disruption: the migration plan directly addresses this cost by...`
  ACCEPTABLE: `CITE: INERTIA-FINDING-C — re-training overhead: the phased rollout reduces this because...`
  FAILS: `CITE: The workflow disruption finding supports adoption...` — paraphrase, no label
  FAILS: `CITE: (a) — workflow-disruption` — parenthesized letter

RESPONDS-TO fill rule (Tier 3 only):
PRINT: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`
VALIDATE: RESPONDS-TO: names and quotes a specific concern.
  ACCEPTABLE: `RESPONDS-TO: "INERTIA-FINDING-D: [switching cost]" — the mitigation plan accounts for this by...`
  ACCEPTABLE: `RESPONDS-TO: "[Inertia-Advocate]'s concern that [X]" — the adapter layer preserves the existing contract`
  FAILS: `RESPONDS-TO: "Inertia concerns have been acknowledged"` — generic
  FAILS: `RESPONDS-TO: "The challenger raised valid points"` — no attribution

VALIDATE: at least one participant declares STANCE: CONDITION or STANCE: BLOCK; all-APPROVE triggers Phase 2 reopen and tier reassignment.

WRITE: ## STANCE MANIFEST — fill after all participant voices:
  PRINT one entry per participant: `[Role Name] STANCE-TOKEN`
  ENFORCE: independently addressable section; appears before PHASE-3-COMMIT.

PRINT: STANCE INVARIANT seal declaration as the terminal line of ## STANCE MANIFEST:
  ENFORCE: required — makes the stance record's post-commit immutability self-documenting.
  PRINT: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
  VALIDATE: seal declaration is an explicit assertion in the section body.
    ACCEPTABLE: `STANCE INVARIANT: sealed at PHASE-3-COMMIT — stance entries may not be revised without reopening Phase 3.`
    FAILS: ## STANCE MANIFEST with correct entries but no STANCE INVARIANT line — immutability assumed, not declared; fails C-40

ENFORCE: PHASE-3-COMMIT: is the terminal element of Phase 3 — no Phase 3 content may appear after it.
PRINT: PHASE-3-COMMIT: [locked] — Vote-anchor manifest declared in ## STANCE MANIFEST above — modifications to that manifest require updating this commit; modifications to this commit require updating that manifest. All stances locked. Phase 4 TALLY derives from ## STANCE MANIFEST by token count; re-parsing Phase 3 voice prose is not permitted. All voices complete in Tier 1 → 2 → 3 order. Phase 3 closed.
  | ENFORCE: this marker is the terminal element of Phase 3; no Phase 3 content may follow this line.

VALIDATE: bidirectionality clause is present in PHASE-3-COMMIT block.
  ACCEPTABLE: PHASE-3-COMMIT includes "modifications to that manifest require updating this commit; modifications to this commit require updating that manifest" — coupling declared in both directions; passes C-41
  FAILS: PHASE-3-COMMIT reads only "Vote-anchor manifest declared in ## STANCE MANIFEST above; all stances locked" — heading cross-reference present but coupling obligation unstated; passes C-38, fails C-41

---

**PHASE 4 fill rules:**

PRINT: `TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK` as a standalone line after the last Phase 3 voice block.
COUNT: each entry in ## STANCE MANIFEST — one tally count per STANCE-TOKEN category.
CONFIRM: TALLY appears as a standalone line, not embedded in prose.
VALIDATE: TALLY counts match ## STANCE MANIFEST exactly.
  ACCEPTABLE: `TALLY: 2 APPROVE · 1 CONDITION · 1 BLOCK` when ## STANCE MANIFEST contains exactly those tokens
  FAILS: tally count differing from manifest token count — indicates re-parsing Phase 3 prose; fails C-35
WRITE: OUTCOME — all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED per committee type convention.
ENFORCE: PHASE-4-COMMIT: is the terminal element of Phase 4 — no Phase 4 content may appear after it.
PRINT: PHASE-4-COMMIT: [locked] — TALLY line printed, OUTCOME declared. Phase 4 closed.
  | ENFORCE: this marker is the terminal element of Phase 4; no Phase 4 content may follow this line.

---

**PHASE 5 fill rules:**

DECISIONS fill rules:
WRITE: Verdict — matches OUTCOME from Phase 4 exactly.
WRITE: Conditions for full approval — name each condition explicitly; ENFORCE: "address feedback" fails; REQUIRE: a specific deliverable or named state.
REQUIRE (when verdict is not APPROVED):
  WRITE: Owner — named role from Phase 0 roster responsible for satisfying the blocking condition; ENFORCE: not a team; a specific role.
  WRITE: Trigger — concrete deliverable, evidence artifact, or event causing committee re-review; ENFORCE: "sufficient progress" fails; named artifact with named recipient and named authority passes.
VALIDATE: both Owner and Trigger present when verdict is not APPROVED; path missing either field fails C-23.
  ACCEPTABLE: Owner = `[PM Lead]`, Trigger = `signed load-test report at >99.9% SLA delivered to Arch-Board chair` — named role, named artifact, named recipient
  FAILS: Owner = `[PM Lead]`, Trigger = `address scalability concerns` — trigger is a condition, not a concrete event; fails C-23

ACTION ITEMS fill rules:
PRINT: `[Owner Role] — [specific action] — [deadline]` one line per item.
REQUIRE: all three parts; "investigate" alone fails — WRITE: the question, the output artifact, and who receives it.

DISSENTING OPINIONS fill rules:
WRITE: for each CONDITION or BLOCK stance — dissent substance citing INERTIA-FINDING-* label from ## INERTIA RECORD where applicable, plus resolution path (concrete condition + named authority confirming when condition is met).
VALIDATE: cited INERTIA-FINDING-* labels match labels enumerated in ## INERTIA RECORD.
CONFIRM: resolution path names a concrete trigger, not a general condition.
ENFORCE: if no dissent — PRINT: `No dissent — [one sentence explaining consensus]`
ENFORCE: PHASE-5-COMMIT: is the terminal element of Phase 5 and the final element of the simulation.
PRINT: PHASE-5-COMMIT: [locked] — DECISIONS, ACTION ITEMS, and DISSENTING OPINIONS written; Owner and Trigger present if verdict not APPROVED. Phase 5 closed. Simulation complete.
  | ENFORCE: this marker is the terminal element of Phase 5; no Phase 5 content may follow this line.
