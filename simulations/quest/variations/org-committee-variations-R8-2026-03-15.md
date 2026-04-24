Good. I have all the context needed. Writing now.

---

# org:committee Variations — Round 8

**Generated**: 2026-03-16
**Skill**: `org:committee`
**Rubric**: v8 (C-27 adds named INERTIA-FINDING labels to Phase 1 investigation entries; C-28 adds pre-declared skeleton before any content generation; aspirational pool 20 criteria, composite max 130)

---

## V-01 — Single-axis: Lifecycle Emphasis — Named Labels Integrated into Phase Architecture (C-27 + C-26)

**Variation axis**: Lifecycle emphasis — same phase-first architecture as R7 V-01, but Phase 1 now uses `INERTIA-FINDING-A/B/C/D` named labels (C-27) instead of lettered sub-questions, making every Phase 1 finding a directly citable investigation-entry label. The CITE: field in Phase 3 Tier 3 voices must reference the named label, not an opaque `(a)/(b)/(c)/(d)` reference.

**Hypothesis**: R7 V-01 used `(a)/(b)/(c)/(d)` labels in Phase 1 and parenthesized references in CITE:. The citation was structural (first token after CITE:) but the cited entity was an anonymous letter. C-27 requires each Phase 1 finding to carry a named label so the citation is traceable to a specific, named investigation entry rather than a positional slot. When Phase 1 findings carry `INERTIA-FINDING-A` through `INERTIA-FINDING-D` as their labels, CITE: references in Phase 3 automatically name the finding entry — the label is load-bearing for C-17, C-20, and C-21 compliance in addition to C-27.

---

You are running org:committee — a pre-meeting simulation that finds surprises before the real meeting happens. Execute in six explicitly labeled, sequential phases. Label each phase header in your output. Complete and commit each phase before beginning the next. Phase outputs are commitments — do not revise a prior phase once it is written.

---

### PHASE 0 — COMMITTEE DECLARATION

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter: [path to .roles/ file used, or "Signal defaults — no charter found"]
Participants:
- [Role Name] — [charter-defined orientation in one phrase]
- [add one line per loaded role]
```

Read `.roles/` for this committee type's charter. Load every named role. If no charter exists, fall back to Signal defaults (PM, Engineering Lead, Design Lead, Inertia-Advocate) and state the fallback explicitly.

Phase 0 commits: committee type, charter source, participant roster. Proceed to Phase 1.

---

### PHASE 1 — SWITCHING-COST INVESTIGATION

Before any participant speaks, investigate what the proposal displaces. Each finding carries a named entry label — these labels are the citation targets for all downstream CITE: and RESPONDS-TO: references. Label this block `INVESTIGATION-ATTEMPT-1:`.

```
INVESTIGATION-ATTEMPT-1:
  INERTIA-FINDING-A: [workflow disruption — specific task, tool, or process displaced — name it, not generic]
  INERTIA-FINDING-B: [integration burden — named systems, APIs, or contracts affected]
  INERTIA-FINDING-C: [habit or culture cost — specific cognitive habit; specific affected team]
  INERTIA-FINDING-D: [reversal cost — what it costs to undo this decision if it proves wrong]

  GATE-1:
    Test: Does at least one INERTIA-FINDING represent a non-obvious switching cost?
    Answer: [YES — INERTIA-FINDING-[X] is non-obvious because [specific reason the proposal author would not have written this] / NO — insufficient: [brief explanation why no finding clears the threshold]]
```

**Phase 1 exit condition**: GATE-N Answer must be YES before Phase 1 closes. If GATE-1 Answer is NO: output `INVESTIGATION-ATTEMPT-2:` with freshly rewritten `INERTIA-FINDING-A` through `INERTIA-FINDING-D` at a different angle, then output `GATE-2:` with Test/Answer fields. Use sequential labels (`INVESTIGATION-ATTEMPT-N:` / `GATE-N:`) until Answer is YES. Each rewrite must carry a sequential attempt label (C-24) — a claimed revision with no new labeled block does not satisfy C-22. Do not proceed to Phase 2 until GATE-N Answer is YES.

Phase 1 commits when GATE-N Answer is YES. Proceed to Phase 2.

---

### PHASE 2 — TIER SORT

Sort all loaded participants into three tiers based on charter-defined orientations and Phase 1 findings. Participants whose roles are most affected by the named INERTIA-FINDINGs sort highest in Tier 1.

```
TIER SORT:
Tier 1 — CHALLENGERS: [roles whose documented lens interrogates feasibility, risk, or disruption — speak first]
Tier 2 — CONDITIONALS: [roles that hold approval pending specific named conditions]
Tier 3 — ADVOCATES: [roles whose orientation aligns with the proposal's stated goals]
Tie-break: higher institutional veto authority speaks first within tier

SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given the named INERTIA-FINDINGs]; corrected sort follows / NO — valid sort, Phase 2 commits]
```

If SORT-CHECK Result is YES: re-output the corrected TIER SORT block and a new SORT-CHECK. Repeat until Result is NO.

Phase 2 commits when SORT-CHECK Result is NO. Proceed to Phase 3.

---

### PHASE 3 — PARTICIPANT VOICES

Write one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3. All voices are Phase 3 content.

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration on its own line — prose follows on the next line and must not soften, qualify, or contradict the declared stance.]
[Tier 3 only] CITE: INERTIA-FINDING-[A/B/C/D] — [the named finding that grounds this endorsement — the INERTIA-FINDING label must be the first element after CITE:, immediately followed by " — " and the finding content; prose before the label fails]
[Tier 3 only] RESPONDS-TO: "[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]' or 'INERTIA-FINDING-[X]: [content]']" — [one sentence: how this endorsement addresses that concern — do not remove the quotation marks]
```

Requirements:
- `STANCE:` is a discrete labeled declaration. Prose follows on the next line; it may not revise the declared stance.
- Every Tier 3 block requires both `CITE:` and `RESPONDS-TO:`.
- `CITE:` format (C-20): the `INERTIA-FINDING-[X]` label must be the first element after `CITE:`. Any prose before the label fails.
- `RESPONDS-TO:` format (C-21): must quote or paraphrase a specific named concern by role name or finding label. Generic acknowledgment ("there are concerns") fails.
- At least one participant must declare CONDITION or BLOCK. An all-APPROVE Phase 3 means Phase 2 sort is invalid — reopen Phase 2, re-sort, re-evaluate SORT-CHECK.

Phase 3 commits when all participant voices are written. Proceed to Phase 4.

---

### PHASE 4 — TALLY

After all Phase 3 voices and before any formal minutes section:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

Phase 4 commits. Proceed to Phase 5.

---

### PHASE 5 — MINUTES

#### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the blocking condition]
  Trigger: [concrete deliverable or event that causes committee re-review — not vague]
```

Both Owner and Trigger are required fields (C-23). A path specifying only one fails.

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline required for every item. "Investigate further" fails.

#### DISSENTING OPINIONS

For each non-approving voice: dissenting role, substance of objection, resolution path (named owner + concrete trigger).

If no dissent: "No dissent — [one sentence on the basis for consensus]."

Phase 5 commits the simulation record.

---

## V-02 — Single-axis: Output Format — Table-Based Investigation with Named Labels as Structural Column (C-27)

**Variation axis**: Output format — the switching-cost investigation is presented as a markdown table where the first column is the named INERTIA-FINDING label. The table structure forces named labels architecturally: a row in the table cannot exist without its Label column being filled. This is a different structural enforcement mechanism for C-27 than V-01's prose block — the table column is the label's natural home, not a prefix to a finding sentence.

**Hypothesis**: R7 V-03 introduced INERTIA-FINDING tags but placed them in the Inertia-Advocate's voice block as committee-record summary tags, not in the Phase 1 investigation findings themselves. C-27 requires the finding labels to be on the investigation findings directly, so that CITE: references in Phase 3 can point to specific named investigation entries rather than paraphrase investigation content. A table format with a Label column makes this inevitable: each row is a named finding, and the row label is the INERTIA-FINDING tag. When the table exists, C-27 is satisfied without behavioral discipline — the column cannot be empty.

---

You are simulating a committee meeting before the real one.

**DECLARE**

Open with:
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**LOAD PARTICIPANTS**

Read `.roles/` for this committee type's charter. Load all named participants with their documented orientations. Disclose if falling back to Signal defaults (PM, Engineering Lead, Design Lead, Inertia-Advocate).

```
Participants:
- [Role Name] — [orientation in one phrase]
```

---

**SWITCHING-COST INVESTIGATION**

Before any participant speaks, map what the proposal displaces. Present findings as a labeled table — the Label column provides named entry tags that participant voices cite directly by label name.

```
### INVESTIGATION-ATTEMPT-1

| Label | Domain | Finding |
|-------|--------|---------|
| INERTIA-FINDING-A | Workflow disruption | [specific task, tool, or process displaced — name it, not generic] |
| INERTIA-FINDING-B | Integration burden | [named systems, APIs, or contracts affected] |
| INERTIA-FINDING-C | Habit / culture cost | [specific cognitive habit; specific affected team] |
| INERTIA-FINDING-D | Reversal cost | [what it costs to undo this decision if it proves wrong] |

GATE-1:
  Test: Does at least one row represent a non-obvious switching cost?
  Answer: [YES — INERTIA-FINDING-[X] is non-obvious because [specific reason the proposal author would not have anticipated it] / NO — insufficient: [brief explanation why no row clears the threshold]]
```

If GATE-1 Answer is NO: output `### INVESTIGATION-ATTEMPT-2` with a fresh table (same column structure, different findings in each row) and a new `GATE-2:` block with Test/Answer fields. Use sequential attempt labels (`INVESTIGATION-ATTEMPT-N` / `GATE-N`) until Answer is YES. Each attempt must be a labeled table block — a prose summary without a new table header and sequential number does not satisfy C-24. Do not proceed to the tier sort until GATE-N Answer is YES.

---

**TIER SORT**

Sort all participants. When assigning tiers, reference the named INERTIA-FINDINGs: participants whose roles are most exposed to findings in the table sort highest in Tier 1.

```
TIER SORT:
Tier 1 (CHALLENGERS — speak first): [roles whose orientation interrogates risk, disruption, or feasibility]
Tier 2 (CONDITIONALS): [roles that approve with specific named conditions]
Tier 3 (ADVOCATES — speak last): [roles aligned with the proposal's stated goals]
Tie-break: higher veto authority speaks first within tier

SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] mis-sorted; reassigning to Tier [X] because [specific reason]; corrected sort follows / NO — proceed to voices]
```

If Result is YES: re-output the corrected TIER SORT block and a new SORT-CHECK. Repeat until Result is NO.

---

**PARTICIPANT VOICES** (Tier 1 → Tier 2 → Tier 3)

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a discrete labeled declaration — prose follows on the next line and must not soften or contradict it.]
[Tier 3 only] CITE: INERTIA-FINDING-[A/B/C/D] — [finding content from that table row — label is first element after CITE:]
[Tier 3 only] RESPONDS-TO: "[specific named concern — attributed by role name or finding label]" — [how this endorsement addresses it]
```

- `CITE:` format: the `INERTIA-FINDING-[X]` label from the investigation table must be the first element after `CITE:`, immediately followed by ` — ` and the finding content. Prose before the label fails.
- `RESPONDS-TO:` format: must name a specific concern by role name or `INERTIA-FINDING-[X]` label and paraphrase its content. Generic acknowledgment ("inertia concerns have been noted") fails.
- At least one participant must declare CONDITION or BLOCK.

---

**TALLY**

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

---

**FORMAL MINUTES**

**DECISIONS:**
```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the blocking condition]
  Trigger: [concrete deliverable or event that causes committee re-review]
```

Both Owner and Trigger required (C-23).

**ACTION ITEMS:**
```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. Vague items fail.

**DISSENTING OPINIONS:**

Each dissent with resolution path: [named owner role] satisfies this when [concrete, observable trigger]. If no dissent: "No dissent — [one sentence on the basis for consensus]."

---

## V-03 — Single-axis: Phrasing Register — Conversational Imperative (C-28 stress test)

**Variation axis**: Phrasing register — behavioral instructions in plain conversational language rather than template headers and pre-printed slot fields. The structural requirements are embedded as prose rules, not as blank fields the model must fill. Expected to achieve C-27 (named labels in investigation) through instruction compliance, and a partial pass on C-28 (labels emerge with content, not pre-declared) — which makes this variation the natural comparison point for V-05's architectural approach.

**Hypothesis**: Conversational register produces adequate structural compliance for most criteria but fails C-28's "skeleton pre-declared before content" requirement by design. This establishes a ceiling for behavioral approaches and a baseline for measuring C-28's marginal value: V-05 should outscore V-03 specifically on C-28 while matching it on all other criteria. The variation also tests whether C-27 is achievable through prose instruction alone ("name each finding INERTIA-FINDING-A through D") or requires structural pre-declaration to pass reliably.

---

You are running org:committee — a pre-meeting simulation that finds the surprises before the real meeting happens.

Start by declaring the committee type. Say whether it's a ROB (product or business review), a shiproom (go/no-go decision), an arch-board (architecture review), or something else. Then state the agenda item. If the context doesn't specify the committee type, infer it from the agenda item description.

Next, load the participants. Read `.roles/` to find the charter for this committee type. List every named participant role with a one-phrase description of their role orientation. If there's no charter file, say so explicitly and use Signal's default committee roles: PM, Engineering Lead, Design Lead, and Inertia-Advocate.

Before anyone speaks, do a switching-cost investigation. The question is not "what are the risks?" — it's "what does the status quo protect?" You're looking for the actual disruption the proposal would impose on existing workflows, integrations, and team habits. Write four named findings, using exactly these labels:

- **INERTIA-FINDING-A** — the specific workflow or task the proposal would displace. Name the tool, process, or practice; don't say "existing processes."
- **INERTIA-FINDING-B** — the specific systems, APIs, or integrations that would require rework. Name them.
- **INERTIA-FINDING-C** — the specific cognitive habit or team norm that would need to change. Name the habit and the team.
- **INERTIA-FINDING-D** — the reversal cost. What would it take to undo this decision if it proves wrong?

After writing all four, evaluate: does at least one finding represent something the proposal author genuinely didn't anticipate? Write `GATE-1: YES` if yes, with a one-sentence explanation of why that finding would surprise the author. Write `GATE-1: NO` if no finding clears that bar, with a brief explanation. If GATE-1 is NO, label what you just wrote `INVESTIGATION-ATTEMPT-1`, then write `INVESTIGATION-ATTEMPT-2:` with four fresh findings at a different angle, and evaluate `GATE-2:` the same way. Keep going — `INVESTIGATION-ATTEMPT-N:` / `GATE-N:` — until you reach YES. Each attempt needs its own sequential label so the iteration is visible.

Now sort the participants into three tiers before anyone speaks. Tier 1 is the challengers — the people most likely to block or push back hard, especially based on what the INERTIA-FINDINGs revealed about whose domain this disrupts. Tier 2 is the conditionals — they'll approve but need something specific addressed first. Tier 3 is the advocates — they're aligned with the proposal's goals and will endorse it. Immediately after writing the sort, add a named check:

```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [who] mis-sorted; moving to Tier [X] because [specific reason]; corrected sort follows / NO — proceed]
```

If the result is YES, you've made an error — find which participant should be skeptical given the INERTIA-FINDINGs, re-classify them, and re-run the SORT-CHECK. Don't write any voice blocks until SORT-CHECK Result is NO.

Write each participant's voice in tier order: Tier 1 first, then Tier 2, then Tier 3. For each voice:

1. Write `STANCE:` on its own line — BLOCK, CONDITION, or APPROVE — before any prose. The prose that follows cannot revise or soften the declared stance.
2. Write 2–4 sentences from that participant's documented role orientation, responding to the specific agenda item. Be concrete — no generic positions.
3. For Tier 3 voices, add two required lines before any closing prose:
   - `CITE: INERTIA-FINDING-[A/B/C/D] — [the finding content that grounds this endorsement]` — the INERTIA-FINDING label is the first element after CITE:, no prose before it.
   - `RESPONDS-TO: "[specific named concern — by role name or finding label]" — [one sentence on how this endorsement addresses it]` — naming "INERTIA-FINDING-B" and paraphrasing its content satisfies this; "others have raised concerns" does not.

At least one participant must declare CONDITION or BLOCK. If every voice ends up APPROVE, your Phase 2 sort was wrong — go back and re-sort.

After all voices, write a one-line tally:
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

Then write the formal minutes. Three required sections:

**DECISIONS** — State the verdict (approved / approved with conditions / blocked / deferred), list any conditions for full approval, and if the item isn't approved, give a re-entry path that names both the owner role responsible for resolving the block and the concrete observable trigger that would bring the item back to committee. "Monitor and revisit" is not a trigger.

**ACTION ITEMS** — One line per item: `[Owner Role] — [specific action] — [deadline]`. Every item needs a named owner, a specific deliverable, and a deadline.

**DISSENTING OPINIONS** — For each dissent, name the dissenting role, state the objection substance, and give a resolution path: [named authority] confirms this condition is met when [specific observable event]. If there's no dissent, say "No dissent" and give one sentence on why consensus formed.

---

## V-04 — Combined: Lifecycle Emphasis + Output Format — Phase Architecture with Table-Based Investigation (C-26 + C-27)

**Variation axes**: Lifecycle emphasis (phase-first architecture, V-01 axis) + output format (table-based investigation, V-02 axis). The combination pairs phase-commit boundaries with the table investigation format: Phase 1 is a named-findings table, Phase 2 is a sort with SORT-CHECK, Phase 3 is voices with CITE: referencing named table labels. The phase structure makes gate positions unambiguous (Phase 1 cannot close without GATE-N YES; Phase 2 cannot close without SORT-CHECK NO), and the table structure makes C-27 label compliance architecturally unavoidable.

**Hypothesis**: V-01 enforces C-27 through prose instruction ("label this block INERTIA-FINDING-A"). V-02 enforces C-27 through table column structure (the Label column cannot be empty). V-04 combines the enforcement: the table column enforces C-27, and the phase-commit boundary enforces that the table is complete before downstream phases can begin. This eliminates two independent failure modes — a finding written without a named label (caught by the table column) and a Phase 3 voice citing an investigation that isn't committed (caught by the phase boundary).

---

You are running org:committee — a pre-meeting simulation. Execute in six explicitly labeled, sequential phases. Label each phase header in your output. Complete each phase before starting the next. Phase outputs are commitments.

---

### PHASE 0 — COMMITTEE DECLARATION

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter: [path to .roles/ file, or "Signal defaults — no charter found"]
Participants:
- [Role Name] — [charter-defined orientation in one phrase]
- [add one line per loaded role]
```

Read `.roles/` for the committee charter. Load every named role. Disclose fallback to Signal defaults (PM, Engineering Lead, Design Lead, Inertia-Advocate) if no charter file exists.

Phase 0 commits. Proceed to Phase 1.

---

### PHASE 1 — SWITCHING-COST INVESTIGATION

Map what the proposal displaces using a named-findings table. The Label column provides investigation-entry tags that Phase 3 voices cite by label. Each row is a named finding.

```
### INVESTIGATION-ATTEMPT-1

| Label | Domain | Finding |
|-------|--------|---------|
| INERTIA-FINDING-A | Workflow disruption | [specific task, tool, or process displaced — name it, not generic] |
| INERTIA-FINDING-B | Integration burden | [named systems, APIs, or contracts affected] |
| INERTIA-FINDING-C | Habit / culture cost | [specific cognitive habit; specific affected team] |
| INERTIA-FINDING-D | Reversal cost | [cost to undo this decision if it proves wrong] |

GATE-1:
  Test: Does at least one table row represent a non-obvious switching cost?
  Answer: [YES — INERTIA-FINDING-[X] is non-obvious because [specific reason the proposal author would not have written this] / NO — insufficient: [brief explanation why no row clears the threshold]]
```

**Phase 1 exit condition**: GATE-N Answer must be YES before Phase 1 closes. If GATE-1 Answer is NO: output `### INVESTIGATION-ATTEMPT-2` with a fresh four-row table (same Label column, different findings) and `GATE-2:` with Test/Answer fields. Use sequential attempt labels until Answer is YES. Each labeled attempt must be a full table block — a prose note without a new labeled table does not satisfy C-24. Do not fill Phase 2 until GATE-N Answer is YES.

Phase 1 commits when GATE-N Answer is YES. Proceed to Phase 2.

---

### PHASE 2 — TIER SORT

Sort all loaded participants. When assigning tiers, reference the Phase 1 named findings: participants whose roles are most exposed to the INERTIA-FINDINGs sort highest in Tier 1.

```
TIER SORT:
Tier 1 — CHALLENGERS (speak first): [roles whose orientation interrogates feasibility, risk, or disruption]
Tier 2 — CONDITIONALS: [roles that hold approval pending specific named conditions]
Tier 3 — ADVOCATES (speak last): [roles aligned with the proposal's stated goals]
Tie-break: higher institutional veto authority speaks first within tier

SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] mis-sorted; reassigning to Tier [X] because [specific reason given Phase 1 findings]; corrected sort follows / NO — valid sort, Phase 2 commits]
```

If SORT-CHECK Result is YES: re-output the corrected TIER SORT and a new SORT-CHECK. Repeat until Result is NO.

Phase 2 commits when SORT-CHECK Result is NO. Proceed to Phase 3.

---

### PHASE 3 — PARTICIPANT VOICES

Write one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3.

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows on the next line and must not soften, qualify, or contradict the declared stance. Tier 1: lead with the specific concern. Tier 2: name the specific approval condition. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
[Tier 3 only] CITE: INERTIA-FINDING-[A/B/C/D] — [finding content from that table row — INERTIA-FINDING label is first element after CITE:, followed by " — " and content; prose before the label fails]
[Tier 3 only] RESPONDS-TO: "[quoted or paraphrased concern — attributed as: 'INERTIA-FINDING-[X]: [paraphrase]' or '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern]
```

Requirements:
- `STANCE:` is a discrete labeled declaration. Prose follows; it does not revise.
- Every Tier 3 block: `CITE:` and `RESPONDS-TO:` required.
- `CITE:` format: `INERTIA-FINDING-[X]` label is first element after `CITE:` — no prose before the label.
- `RESPONDS-TO:` format: names a specific concern by role name or `INERTIA-FINDING-[X]` label and paraphrases its content. Generic acknowledgment fails.
- At least one participant must declare CONDITION or BLOCK. An all-APPROVE Phase 3 means Phase 2 is invalid — reopen Phase 2.

Phase 3 commits when all voices are written. Proceed to Phase 4.

---

### PHASE 4 — TALLY

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

Phase 4 commits. Proceed to Phase 5.

---

### PHASE 5 — MINUTES

#### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the blocking condition]
  Trigger: [concrete deliverable or event that causes committee re-review — not vague]
```

Both Owner and Trigger required (C-23).

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. Vague items fail.

#### DISSENTING OPINIONS

For each dissent: role, objection substance, resolution path (named owner + concrete trigger). If no dissent: "No dissent — [one sentence on the basis for consensus]."

Phase 5 commits the simulation record.

---

## V-05 — Golden Synthesis: Pre-Declared Skeleton as Architectural Enforcement (C-28 + all prior)

**Variation axes**: Output format (two-step skeleton/fill) + lifecycle emphasis (numbered phases) + inertia framing (INERTIA-FINDING labels in Phase 1 table) + role sequence (SORT-CHECK as phase-exit gate). All structural slot labels — phase headers, investigation-attempt blocks with named finding labels, SORT-CHECK with Test/Result fields, STANCE:, CITE:, RESPONDS-TO:, tally line, and re-entry path fields — appear as an explicit pre-declared skeleton with `[EMPTY]` placeholder values before any content generation begins. The model outputs the complete skeleton first, then fills each slot.

**Hypothesis**: R7 V-05 used a template-completion approach where structural slots existed as pre-printed fields in the prompt, and the model filled them. The model's output contained labels alongside generated content — "labels emerge from content generation" is the C-28 partial-pass condition. C-28's full-pass condition is harder: the skeleton must appear in the model's output, with empty values, before any content is generated. This two-step approach — print skeleton → fill skeleton — converts C-28 from a prompt-design property (the prompt has pre-printed slots) to an output-design property (the output shows an empty skeleton before filled content). A slot declared as `[EMPTY]` in the output cannot be forgotten when content is generated — it exists as a visible blank, not as a potential omission.

---

You are running org:committee — a pre-meeting simulation. This simulation uses a two-step approach: you will first print the complete structural skeleton with `[EMPTY]` placeholder values, then fill each slot with actual content. A slot that exists as a visible blank in the skeleton cannot be forgotten during content generation. Do not fill any slots during Step 1.

---

### STEP 1 — PRINT THE SKELETON

Before generating any content, print the following skeleton exactly. Expand participant rows, voice blocks, and action item rows to match the loaded roster count (you will not know this count until Step 2, so use the number of default roles for now and expand in Step 2). Replace participant count estimates with actual loaded roles in Step 2. Print the skeleton with `[EMPTY]` tokens; do not fill content yet.

```
=== ORG:COMMITTEE SIMULATION SKELETON ===

PHASE 0 — COMMITTEE DECLARATION
  Committee: [EMPTY]
  Agenda Item: [EMPTY]
  Charter source: [EMPTY]
  Participants:
    - [Role]: [EMPTY]        ← one row per loaded participant; expand in Step 2

PHASE 1 — SWITCHING-COST INVESTIGATION
  INVESTIGATION-ATTEMPT-1:
    | Label              | Domain            | Finding  |
    |--------------------|-------------------|----------|
    | INERTIA-FINDING-A  | Workflow disruption | [EMPTY] |
    | INERTIA-FINDING-B  | Integration burden  | [EMPTY] |
    | INERTIA-FINDING-C  | Habit/culture cost  | [EMPTY] |
    | INERTIA-FINDING-D  | Reversal cost       | [EMPTY] |
  GATE-1:
    Test: Non-obvious finding present?
    Answer: [EMPTY]
  [INVESTIGATION-ATTEMPT-2 and GATE-2 if needed — expand here in Step 2]

PHASE 2 — TIER SORT
  TIER SORT:
    Tier 1 (CHALLENGERS): [EMPTY]
    Tier 2 (CONDITIONALS): [EMPTY]
    Tier 3 (ADVOCATES): [EMPTY]
  SORT-CHECK:
    Test: Tier 1 and Tier 2 both empty?
    Result: [EMPTY]

PHASE 3 — PARTICIPANT VOICES
  [One block per participant — expand to match roster; expand in Step 2]

  [Role Name — Tier 1]:
    STANCE: [EMPTY]
    [prose: EMPTY]

  [Role Name — Tier 2]:
    STANCE: [EMPTY]
    [prose: EMPTY]

  [Role Name — Tier 3]:
    STANCE: [EMPTY]
    [prose: EMPTY]
    CITE: [EMPTY]
    RESPONDS-TO: [EMPTY]

PHASE 4 — TALLY
  TALLY: [EMPTY] APPROVE · [EMPTY] CONDITION · [EMPTY] BLOCK
  OUTCOME: [EMPTY]

PHASE 5 — MINUTES
  DECISIONS:
    Verdict: [EMPTY]
    Conditions for full approval: [EMPTY]
    Re-entry path (if not approved):
      Owner: [EMPTY]
      Trigger: [EMPTY]
  ACTION ITEMS:
    - [Owner Role] — [action] — [deadline]    ← [EMPTY] for all three fields
  DISSENTING OPINIONS:
    - [EMPTY]    ← [role] | [objection] | Resolution path: [owner] when [trigger]

=== END SKELETON ===
```

Do not fill any slot during Step 1. The skeleton is the output. Proceed to Step 2.

---

### STEP 2 — FILL THE SKELETON

Fill each slot in the skeleton with actual content. Work through phases in strict order. Do not fill a later phase until the prior phase's content is committed.

**Filling Phase 0:**
Read `.roles/` for the committee charter matching the stated committee type. Extract committee type (ROB / shiproom / arch-board / other — infer from context if unspecified) and agenda item from context. Expand the Participants roster to one row per loaded participant, with their charter-defined orientation in one phrase. Disclose fallback to Signal defaults (PM, Engineering Lead, Design Lead, Inertia-Advocate) if no charter exists.

**Filling Phase 1:**
Fill each INERTIA-FINDING row in the table with a specific, named switching-cost finding — not generic risks. Each finding's Label cell is its citable name: `INERTIA-FINDING-A` through `INERTIA-FINDING-D`. Fill GATE-1 Answer:
- YES if at least one finding represents something the proposal author would not have anticipated (state which finding and why)
- NO if no finding clears that threshold (state briefly why)

If GATE-1 Answer is NO: expand the skeleton to include an `INVESTIGATION-ATTEMPT-2` table block (same structure, four rows with `INERTIA-FINDING-A` through `INERTIA-FINDING-D` labels, different findings at a different angle) and a `GATE-2:` block with Test/Answer fields. Fill Attempt 2. Re-evaluate GATE-2. Continue with sequential attempt numbers (`INVESTIGATION-ATTEMPT-N` / `GATE-N`) until Answer is YES. The sequential attempt label is required on every rewrite block — an unlabeled rewrite does not satisfy C-24. Do not fill Phase 2 with a NO in the most recent gate.

**Filling Phase 2:**
Assign each participant to Tier 1, 2, or 3. Participants whose roles are most exposed to the named Phase 1 INERTIA-FINDINGs sort highest in Tier 1. Fill SORT-CHECK Result:
- YES if Tiers 1 and 2 are both empty after the sort
- NO if at least one Tier 1 or Tier 2 participant is present

If SORT-CHECK Result is YES: re-examine each participant's exposure to Phase 1 INERTIA-FINDINGs, identify who should be skeptical, reassign them to Tier 1, and expand the skeleton to show the corrected TIER SORT and a new SORT-CHECK block. Repeat until Result is NO. Do not fill Phase 3 until SORT-CHECK Result is NO.

**Filling Phase 3:**
Expand voice blocks to match the full participant roster. Fill one block per participant in tier order: Tier 1 → Tier 2 → Tier 3. For each block:
- Fill `STANCE:` as a discrete labeled declaration on its own line — APPROVE, CONDITION, or BLOCK. The prose that follows in `[prose]` must not soften, revise, or contradict the declared stance.
- Fill `[prose]` with 2–4 sentences grounded in the participant's documented role orientation and the specific agenda item.
- For Tier 3 voices: fill `CITE:` with an `INERTIA-FINDING-[X]` label as the first element after `CITE:`, followed by ` — ` and the finding content from the Phase 1 table row. Any prose before the `INERTIA-FINDING-[X]` label fails C-20. Fill `RESPONDS-TO:` with a quoted or paraphrased specific concern attributed by role name or `INERTIA-FINDING-[X]` label — filling `RESPONDS-TO:` with "others have raised concerns" fails C-21.
- For Tier 1 and Tier 2 voices: leave `CITE:` and `RESPONDS-TO:` as `N/A`.
- At least one voice across the simulation must fill `STANCE:` with CONDITION or BLOCK. If all voices fill STANCE: with APPROVE, Phase 2 sort was invalid — return to Phase 2, re-sort, re-evaluate SORT-CHECK, expand the corrected Phase 2 blocks, then re-fill Phase 3.

**Filling Phase 4:**
Count the STANCE: values from the filled Phase 3 voice blocks. Fill each count in the TALLY line. Fill OUTCOME based on the tally: APPROVED (all APPROVE), APPROVED WITH CONDITIONS (at least one CONDITION, no BLOCK), BLOCKED (at least one BLOCK), or DEFERRED (explicit deferral condition).

**Filling Phase 5:**
- Fill Verdict, Conditions, and (if not approved) re-entry path. Both Owner and Trigger are required — a path specifying only one fails C-23. "Monitor and revisit" is not a Trigger; `[Owner Role] presents [specific deliverable] at next [committee type]` passes.
- Fill ACTION ITEMS — one line per item with named owner, specific action, and deadline. "Investigate further" fails.
- Fill DISSENTING OPINIONS — for each non-approving voice: role name, objection substance, resolution path with named authority and concrete observable trigger. If no voices filled CONDITION or BLOCK (which should not occur if Phase 3 was validly filled), fill with "No dissent — [one sentence on the basis for consensus]."

---

**Structural enforcement rules (active during both steps):**

1. Phase headers PHASE 0 through PHASE 5 must appear in the output. A simulation that produces all required content without labeled phase headers fails C-26. A single unlabeled phase or two phases merged under one header is a partial pass.
2. Every `INVESTIGATION-ATTEMPT-N` block must carry a sequential label. The label increments with each rewrite — `INVESTIGATION-ATTEMPT-2`, `INVESTIGATION-ATTEMPT-3`, etc. An unlabeled rewrite block does not satisfy C-24.
3. The `SORT-CHECK:` block with both `Test:` and `Result:` fields is mandatory within Phase 2. Correct tier ordering without a SORT-CHECK block fails C-25.
4. `STANCE:` is a structural declaration — a standalone labeled line preceding prose. A stance embedded within prose does not pass C-15, even if the position is unambiguous.
5. `CITE:` is required for every Tier 3 voice. The `INERTIA-FINDING-[X]` label must be the first element after `CITE:`. The named label is the load-bearing element (C-20/C-27) — `CITE:` referencing a positional slot `(a)` or paraphrasing investigation content without a named label fails both C-20 and C-27.
6. `RESPONDS-TO:` is required for every Tier 3 voice. The quoted string must name a specific concern by role name or `INERTIA-FINDING-[X]` label. Generic acknowledgment does not fill the attribution slot (C-21).
7. `Owner:` and `Trigger:` are both required in the re-entry path when the outcome is not approved. The re-entry path specifying only one field fails C-23.
8. The TALLY line must appear within Phase 4, between the last Phase 3 voice and Phase 5 — not embedded in prose or placed after minutes.
9. The skeleton declared in Step 1 must appear in the output before any filled content. An output that skips Step 1 and goes directly to filled Phase 0 content is a partial pass on C-28 — the skeleton labels emerged from content generation rather than being pre-declared as empty containers.

---

**Variation axis summary:**

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Lifecycle emphasis | Phase-first + C-27 labels | — | — | Phase-first | Phase-first |
| Output format | Prose block | **Table** | Prose | **Table** | Table + skeleton |
| Phrasing register | Formal/imperative | Formal | **Conversational** | Formal | Formal |
| Inertia framing | Named labels in Phase 1 | Named labels in table | Named labels by instruction | Named labels in table | Named labels in Phase 1 table |
| C-27 mechanism | Prose prefix instruction | Table column (structural) | Prose instruction | Table column (structural) | Table column in skeleton |
| C-28 mechanism | Partial (labels emerge) | Partial (labels emerge) | Partial (behavioral only) | Partial (labels emerge) | **Full (two-step: skeleton → fill)** |
