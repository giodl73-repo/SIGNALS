# org:committee Variations — Round 6
Generated: 2026-03-16
Skill: org:committee
Rubric: v6 (C-20 `CITE:` structural label; C-21 `RESPONDS-TO:` quote/paraphrase not generic; C-22 investigation gate enforces rewrite loop; C-23 re-entry path names owner + concrete trigger; aspirational pool 15 criteria, max 120)

---

## V-01 — Single-axis: CITE: Label-First Notation (C-20 Structural Enforcement)

**Variation axis**: Output format — specifically how the `CITE:` field enforces the investigation label reference. R5 required `(a)/(b)/(c)/(d)` in the instructions; V-01 makes the parenthesized label the *required first token* of the `CITE:` field value, using `CITE: (X) —` as the mandatory format where X is the letter and ` — ` is the separator before content.

**Hypothesis**: R5's CITE: instruction relied on the model including the investigation label somewhere in the field — it could drift into prose before the label appeared. C-20 requires the label to be the explicit structural marker: embedded prose citations do not pass even if the label eventually appears. Enforcing `CITE: (X) — [content]` as a rigid format — where the parenthesized letter is always first, always separated by ` — ` — creates a visible structural marker that either appears in the correct position or is absent. A CITE: field that opens with any prose before the `(X)` token fails C-20 regardless of label presence elsewhere.

---

You are simulating a committee meeting before the real one.

**Open with:**
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.roles/` for this committee type's charter. Load every named role. If no charter exists, use Signal defaults (PM, Architect, Inertia-Advocate) and state them explicitly.

**Investigate before anyone speaks.** Name what this proposal displaces:

```
## PRE-MEETING INVESTIGATION
(a) Current workflow: [specific task, tool, or process — name it, not generic]
(b) Integration dependencies: [named list of systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author did not anticipate]

GATE: [YES — finding (d) is non-obvious because [specific reason] / NO — revising]
```

**C-22 enforcement**: If you write GATE: NO, you must not continue to the sort. Output `INVESTIGATION-REVISION-1:` and rewrite all four fields. Then output a new `GATE:` line. Repeat with sequential labels (`INVESTIGATION-REVISION-2:`, etc.) until you can write GATE: YES. An output that writes GATE: NO and proceeds to the sort or voices fails C-22.

**Sort participants before writing voices:**

```
## PARTICIPANT SORT
Tier 1 (CHALLENGERS): [roles whose lens interrogates feasibility, risk, or disruption to existing systems]
Tier 2 (CONDITIONALS): [roles that approve with named conditions]
Tier 3 (ADVOCATES): [roles aligned with the proposal]
Tie-break: higher veto authority speaks first within a tier
```

**Sort validation.** Immediately after the sort block, output:

```
SORT-CHECK: [Tier 1 and Tier 2 both empty? YES — [role] mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceeding]
```

If SORT-CHECK is YES: re-output the corrected sort block before writing any voices. Do not write voices until SORT-CHECK is output.

**Write voices in tier order: Tier 1 → Tier 2 → Tier 3.**

Each voice:

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it. Tier 1: lead with the concern. Tier 2: name the specific condition. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: (X) — [where X is exactly one of: a, b, c, or d — the letter of the investigation finding, followed by the specific content from that finding that supports this endorsement]
RESPONDS-TO: "[quote or close paraphrase of the specific concern raised by [Role Name]]" — [one sentence: how this endorsement addresses that concern]
```

**CITE: format rule (C-20)**: The parenthesized label — `(a)`, `(b)`, `(c)`, or `(d)` — must be the first token after `CITE:`, immediately followed by ` — ` and then the finding content. A CITE: field that begins with any prose before the label fails C-20. The label is the structural load-bearing marker; content follows it.

**RESPONDS-TO: format rule (C-21)**: The content inside the quotation marks must quote or closely paraphrase the specific concern raised — attributed to its speaker by role name. `"There are concerns about integration"` fails; `"[Role]'s concern that [specific concern text]"` passes. A generic acknowledgment of opposition does not fill the quote slot.

**CITE: and RESPONDS-TO: are required for every Tier 3 voice.** A Tier 3 block missing either field is incomplete and fails C-17 or C-19/C-21 respectively.

**Enforcement**: At least one voice must be CONDITION or BLOCK. All-APPROVE means roles are mis-sorted — return to the sort and reassign.

**After all voices:**
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

**Formal minutes:**

### DECISIONS
```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the condition]
  Trigger: [concrete deliverable, evidence, or event that causes committee re-review]
```

**C-23 enforcement**: Both Owner and Trigger are required. A re-entry path that names only a condition without an Owner, or names an Owner without a concrete Trigger, is a partial pass. Both parts must appear.

### ACTION ITEMS
```
[Owner Role] — [specific action] — [deadline]
```
Every item: named owner, specific deliverable, deadline. Vague items ("investigate further") fail.

### DISSENTING OPINIONS
For each dissent: dissenting role, substance of the objection, resolution path (concrete condition + named authority).

If none: "No dissent — [one sentence on the basis for consensus]."

---

## V-02 — Single-axis: RESPONDS-TO: Quote-Slot Template (C-21 Structural Enforcement)

**Variation axis**: Output format — specifically how the `RESPONDS-TO:` field enforces the quote/paraphrase requirement (C-21). R5 instructed the model to "quote or paraphrase the concern" but left the field as free text. V-02 upgrades the template by pre-printing quotation mark placeholders inside the `RESPONDS-TO:` field, making the quoted string a required slot the model must fill — not prose instruction it may paraphrase away.

**Hypothesis**: R5's RESPONDS-TO: relied on the instruction "quote or paraphrase the concern" to produce C-21 compliance. C-21's pass condition is explicit: generic acknowledgment fails even if factually accurate. Pre-printing `RESPONDS-TO: "[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]']" —` as a template field forces the model to fill the quoted string as a discrete token with attribution structure. An empty or unquoted RESPONDS-TO: has a visibly unfilled template slot. This is the same structural guarantee that made `CITE:` reliable: the model cannot elide what is pre-printed on the page.

---

You are simulating a committee meeting before the real one. Populate the template below exactly. Do not skip sections. Do not reorder sections. Where a field shows `[...]`, fill it with the required content. Where the template shows quotation marks around a placeholder — `"[...]"` — fill the quoted string and preserve the quotation marks.

---

```
# Committee Meeting Simulation
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter loaded from: [path to charter file, or "Signal defaults — no charter found: PM, Architect, Inertia-Advocate"]
Participants: [list all loaded role names]

---

## INVESTIGATION-ATTEMPT-1

(a) Current workflow displaced: [specific task, tool, or process — name it]
(b) Integration dependencies: [named list of systems, APIs, or contracts]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise the proposal author likely missed]

GATE-1: [YES — finding (d) is non-obvious because [specific reason] / NO — insufficient: [brief explanation why (d) does not qualify]]

[If GATE-1 is NO: output INVESTIGATION-ATTEMPT-2 with rewritten (a)–(d), then GATE-2. Continue with sequential labels until GATE-N is YES. Do not proceed to PARTICIPANT SORT until a GATE-N: YES line appears.]

---

## PARTICIPANT SORT

Tier 1 (CHALLENGERS): [roles whose lens interrogates feasibility, risk, or disruption]
Tier 2 (CONDITIONALS): [roles that hold approval pending named conditions]
Tier 3 (ADVOCATES): [roles whose orientation aligns with the proposal]
Tie-break within tier: higher institutional veto authority speaks first

SORT-CHECK: [Tier 1 and Tier 2 both empty? YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason]; corrected sort follows / NO — valid sort, proceed to voices]

[If SORT-CHECK is YES: re-output the corrected tier assignment above before any voice block.]

---

## PARTICIPANT VOICES

[Write one block per participant in tier order: Tier 1 → Tier 2 → Tier 3.]

---

### [Role Name 1] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften, qualify, or contradict it. Tier 1: lead with the concern. Tier 2: name the specific condition. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: ([a/b/c/d]) — [content of that investigation finding as it supports this endorsement]
RESPONDS-TO: "[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern]

---

### [Role Name 2] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences...]
CITE: ([a/b/c/d]) — [...]
RESPONDS-TO: "[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence response]

---

[Repeat block for each participant. CITE: and RESPONDS-TO: are required for every Tier 3 block. At minimum: one participant must declare CONDITION or BLOCK.]

---

## TALLY
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK

---

## DECISIONS

Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the condition]
  Trigger: [concrete deliverable or event that causes committee re-review]

---

## ACTION ITEMS

[Owner Role] — [specific action] — [deadline]
[Owner Role] — [specific action] — [deadline]
[add rows as needed]

Rule: every item has a named owner, a specific deliverable, and a deadline. "Investigate further" fails.

---

## DISSENTING OPINIONS

[If dissent:]
- Role: [dissenting role name]
  Objection: [substance of the objection — citable to STANCE: rationale]
  Resolution path: [concrete condition] — [authority role] confirms when [condition met]

[If no dissent:]
No dissent — [one sentence: why consensus emerged]

---
```

**Template rules applied while filling:**

1. Load participants from `.roles/` using the charter for this committee type. State fallback explicitly if no charter exists.
2. GATE-N fields are mandatory. If GATE-N is NO: do not fill PARTICIPANT SORT or any later section. Output a labeled rewrite attempt (INVESTIGATION-ATTEMPT-N+1) before proceeding.
3. The SORT-CHECK field is mandatory. If YES: re-output the corrected tier block before filling any voice block.
4. The `STANCE:` line is the structural declaration for each voice — standalone labeled line, not embedded in prose.
5. The `CITE:` subfield is required for every Tier 3 voice. Format: `CITE: ([a/b/c/d]) — [content]`. The parenthesized letter must be the first element after `CITE:`.
6. The `RESPONDS-TO:` subfield is required for every Tier 3 voice. The quoted string inside the `"[...]"` placeholder must attribute a specific concern by role name and paraphrase its content. A generic acknowledgment ("there are concerns about this approach") does not fill the quote slot and fails C-21.
7. The re-entry path in DECISIONS requires both Owner and Trigger. A path missing either part fails C-23.
8. The TALLY: line must appear between the last voice block and DECISIONS.

---

## V-03 — Single-axis: Lifecycle Emphasis — Investigation as Numbered Attempt Loop (C-22)

**Variation axis**: Lifecycle emphasis — specifically how the investigation gate enforces self-correction. R5 instructed "if GATE is NO, rewrite (a)–(d) before filling any subsequent field" — detection with a prose directive. C-22 requires active self-correction: the rewrite must be a visible output node with a new label, not a silent internal revision that the model can claim to have done. V-03 structures the investigation as a numbered attempt sequence where each rewrite is a labeled block the evaluator can count and inspect.

**Hypothesis**: R5's single GATE: field is adequate for C-16 detection but ambiguous for C-22 execution — the model knows it should rewrite, but there is no enforcement mechanism that makes a rewrite attempt visible as a distinct output element. C-22 requires the loop to be observable: INVESTIGATION-ATTEMPT-N produces a GATE-N, and if GATE-N is NO, INVESTIGATION-ATTEMPT-N+1 must appear as a labeled output before anything else. An output that writes GATE-N: NO and then immediately reaches the sort has skipped C-22's self-correction loop regardless of what the model claims it revised internally. The numbered attempt format makes compliance vs. violation immediately visible.

---

You are simulating a committee meeting before the real one.

## Phase 0 — Declare + Load

Open with:
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

Load participants from `.roles/` for this committee type. State every loaded role. Fallback: Signal defaults (PM, Architect, Inertia-Advocate) — state them explicitly.

## Phase 1 — Pre-Meeting Investigation (Numbered Attempt Loop)

The investigation runs before any participant speaks. It has a gate — the gate must be satisfied before you proceed to the sort. If the gate fails, rewrite the investigation. The rewrite is a visible output: each attempt is labeled.

**INVESTIGATION-ATTEMPT-1:**
```
(a) Current workflow: [specific task, tool, or process this proposal displaces — name it]
(b) Integration dependencies: [named list of systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author likely did not anticipate]
```

**GATE-1:**
```
GATE-1: [YES — finding (d) is non-obvious because [specific reason the proposal author would not have written this] / NO — insufficient: [why (d) does not genuinely surprise]]
```

**If GATE-1 is NO:** Output `INVESTIGATION-ATTEMPT-2:` and rewrite all four fields. Then output `GATE-2:`. Repeat using sequential labels — `INVESTIGATION-ATTEMPT-N:` / `GATE-N:` — until you produce a GATE-N that is YES.

**If GATE-1 is YES:** Proceed to Phase 2.

A GATE-N: NO followed by no labeled rewrite attempt fails C-22. A GATE-N: YES followed immediately by the sort passes and closes the investigation phase.

## Phase 2 — Participant Sort

After the investigation gate passes, sort all participants. Output as a standalone block:

```
## PARTICIPANT SORT
Tier 1 (CHALLENGERS): [roles whose documented lens interrogates feasibility, risk, or disruption]
Tier 2 (CONDITIONALS): [roles that approve with specific named conditions]
Tier 3 (ADVOCATES): [roles whose orientation aligns with the proposal]
Tie-break: higher institutional veto authority speaks first within a tier
```

**Sort validation.** Immediately after the sort block, output:

```
SORT-CHECK: [Tier 1 and Tier 2 both empty? YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed to voices]
```

If SORT-CHECK is YES: re-output the corrected PARTICIPANT SORT block. Do not write any voices until SORT-CHECK is output.

## Phase 3 — Participant Voices

Write voices in strict tier order: Tier 1 → Tier 2 → Tier 3.

Voice format:
```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone declaration on its own line — prose follows and must not soften or contradict it.
  Tier 1: lead with the specific concern.
  Tier 2: name the specific condition.
  Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: (X) — [X is one of: a, b, c, or d; content from that investigation finding supporting this endorsement]
RESPONDS-TO: "[quote or close paraphrase of the specific Tier 1/2 concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses it]
```

Enforcement:
- `CITE:` is required for every Tier 3 voice. The parenthesized label `(a)/(b)/(c)/(d)` must be the first element after `CITE:`. A CITE: that opens with prose before the label fails C-20.
- `RESPONDS-TO:` is required for every Tier 3 voice. The quoted string must paraphrase a specific named concern from a Tier 1 or Tier 2 voice — attributed by role name and concern content. Generic acknowledgment fails C-21.
- At least one participant must declare CONDITION or BLOCK.

## Phase 4 — Vote Tally

After all voices, before any formal section:
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

## Phase 5 — Formal Minutes

### DECISIONS
```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the condition]
  Trigger: [concrete deliverable or event that causes committee re-review — not vague]
```

**C-23 enforcement**: Both Owner and Trigger are required fields. A re-entry path with only a condition and no named Owner fails. A re-entry path with only an Owner and no concrete Trigger fails. Both parts must be present.

### ACTION ITEMS
```
[Owner Role] — [specific action] — [deadline]
```
Every item: named owner, specific deliverable, deadline. "Investigate further" fails.

### DISSENTING OPINIONS
For each dissent: dissenting role, substance, resolution path (concrete condition + named authority).

If none: "No dissent — [one sentence on the basis for consensus]."

---

## V-04 — Combined: Inertia Framing + C-23 Re-Entry Tied to INERTIA-FINDING Tags

**Variation axes**: Inertia framing (R5 V-04 base) + C-23 re-entry path structure. The inertia-advocate's named findings — `INERTIA-FINDING-A` and `INERTIA-FINDING-B` — serve as the natural named conditions in the re-entry path. The DECISIONS section references these tags directly: Owner resolves INERTIA-FINDING-A by [specific action] — re-review when [finding-based trigger].

**Hypothesis**: The inertia framing creates named, labeled concerns on the committee record before the re-entry path must be written. C-23 requires the re-entry path to name both an Owner and a concrete Trigger. When the inertia-advocate's INERTIA-FINDING tags are the primary named blocking concerns, the DECISIONS section can satisfy C-23 by completing a reference to an already-labeled finding — the Owner is the role responsible for addressing the tag; the Trigger is the condition that resolves it. This produces stronger C-23 compliance than a generic re-entry path because the trigger is traceable to a specific committee record entry, not invented at the close of minutes. C-21 is additionally satisfied naturally: advocate voices that name INERTIA-FINDING-A or INERTIA-FINDING-B as their `RESPONDS-TO:` target are responding to a labeled, specific concern — generic acknowledgment is structurally ruled out by the tag name requirement.

---

You are simulating a committee meeting before the real one.

## Step 1 — Declare + Load

Open with:
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

Load participants from `.roles/` for this committee type. Additionally, check `.roles/` for an `inertia-advocate.md` file — if it exists and is not already in the charter, add it as a mandatory first speaker. Fallback: Signal defaults (PM, Architect, Inertia-Advocate) — state them.

## Step 2 — Pre-Meeting Investigation

Before any participant speaks, investigate what this proposal displaces:

```
## PRE-MEETING INVESTIGATION
(a) Current workflow: [specific task, tool, or process — name it]
(b) Integration surface: [named list of systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — what the proposal author likely missed]

GATE: [YES — non-obvious because [reason] / NO — revising]
```

**C-22 loop**: If GATE is NO, output `INVESTIGATION-REVISION-1:` and rewrite (a)–(d). Re-gate. Repeat with sequential revision labels until GATE is YES. Do not proceed until GATE: YES appears.

## Step 3 — Inertia-Advocate Voice (Mandatory First Speaker)

The inertia-advocate speaks before all other participants. This is not optional.

```
### Inertia-Advocate — Tier 1 (First Speaker)
STANCE: [CONDITION / BLOCK — inertia-advocate never freely approves on first pass]
[3-5 sentences building the evidence-based case for the status quo or delay. Ground the critique in named Step 2 findings — cite (a), (b), (c), or (d) by label. This voice sets the null hypothesis every subsequent speaker must address.]

INERTIA-FINDING-A: [one-line summary of the strongest status-quo argument — citable to a Step 2 finding label]
INERTIA-FINDING-B: [one-line summary of the second-strongest — citable to a Step 2 finding label]
```

These tags are the primary named concerns on the committee record. All subsequent voices must engage with at least one of them.

## Step 4 — Remaining Participant Sort

Sort all remaining participants (excluding the inertia-advocate, who has already spoken):

```
## REMAINING SORT
Skeptics (speak next): [roles whose lens interrogates risk, compliance, or feasibility]
Advocates (speak last): [roles aligned with the proposal]
Tie-break: higher veto authority speaks first within group
```

**Sort validation:**
```
REMAINING-SORT-CHECK: [All remaining participants are advocates (no Skeptics)? YES — [role] mis-sorted; reassigning to Skeptics because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed]
```

If REMAINING-SORT-CHECK is YES: re-output the corrected REMAINING SORT block before writing any remaining voices.

## Step 5 — Remaining Participant Voices

Voices in sort order: Skeptics → Advocates.

```
### [Role Name] — [Skeptic / Advocate]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it.
  Skeptic voices: name the specific concern; may ground it in Step 2 findings or the proposal itself.
  Advocate voices: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: (X) — [X is one of: a, b, c, d — the Step 2 finding label, followed by the specific finding content supporting this endorsement. Alternatively: cite INERTIA-FINDING-A or INERTIA-FINDING-B by tag, with the tag's content.]
RESPONDS-TO: "INERTIA-FINDING-[A/B]: [paraphrase of the tag's content]" — [one sentence: how this endorsement addresses that specific finding]
```

**CITE: rule (C-20)**: The first element after `CITE:` must be the label — `(a)`, `(b)`, `(c)`, `(d)`, `INERTIA-FINDING-A`, or `INERTIA-FINDING-B`. No prose before the label. Content follows.

**RESPONDS-TO: rule (C-21)**: Naming `INERTIA-FINDING-A` or `INERTIA-FINDING-B` by tag and paraphrasing its content satisfies both C-19 and C-21. Generic acknowledgment ("the inertia concerns have been noted") fails — the tag name and paraphrase must appear.

**C-05 enforcement**: At least one non-inertia participant must declare CONDITION or BLOCK. The inertia-advocate alone does not satisfy C-05.

## Step 6 — Vote Tally

After all voices, before any other section:
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

## Step 7 — Formal Minutes

### DECISIONS
```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for resolving the blocking finding]
  Resolves: [INERTIA-FINDING-A or INERTIA-FINDING-B — the specific tag this path addresses]
  Trigger: [concrete deliverable or event that causes committee re-review — traceable to the Resolves tag]
```

**C-23 enforcement**: Owner and Trigger are both required. The `Resolves:` field names which INERTIA-FINDING tag is being addressed — this grounds the trigger in a specific committee record entry rather than an invented condition. A re-entry path that names only a condition without an Owner, or names an Owner without a concrete Trigger, is a partial pass.

### ACTION ITEMS
```
[Owner Role] — [specific action] — [deadline]
```
All items: named owner, specific deliverable, deadline. Vague items fail.

### DISSENTING OPINIONS

For each dissent: dissenting role, substance of the objection, resolution path (concrete condition + named authority).

The inertia-advocate's dissent must appear here if STANCE was CONDITION or BLOCK — resolution path must reference INERTIA-FINDING-A or INERTIA-FINDING-B explicitly.

If none: "No dissent — [one sentence on the basis for consensus]."

---

## V-05 — Combined: All Four New Criteria as Pre-Printed Template Fields (Golden Synthesis)

**Variation axes**: Output format (template-completion) + lifecycle emphasis (numbered attempt loop for GATE) + all four R6 new criteria (C-20, C-21, C-22, C-23) as pre-printed structural fields. Every new criterion is enforced through a pre-printed template slot the model must fill — not through prose instruction the model may de-prioritize under attention pressure.

**Hypothesis**: R5 V-05 demonstrated that the golden synthesis approach — making every aspirational criterion a labeled structural field — produces the highest composite score with the lowest model-behavior risk. V-01 through V-04 each target one or two of the new R6 criteria with a dedicated enforcement mechanism on a single axis. V-05 applies all four simultaneously as pre-printed fields: `CITE: ([a/b/c/d]) —` prefix notation (C-20); `RESPONDS-TO: "[...]" —` with pre-printed quotation marks (C-21); `INVESTIGATION-ATTEMPT-N:` / `GATE-N:` numbered sequence (C-22); `Owner:` / `Trigger:` two-field re-entry structure (C-23). The model fills slots, not free-form text — structural compliance becomes a transcription task, not a generation task.

---

You are simulating a committee meeting before the real one. Populate the template below exactly. Do not skip sections. Do not reorder sections. Where a field shows `[...]`, fill it with the required content. Where the template shows quotation marks around a placeholder — `"[...]"` — fill the quoted string and preserve the quotation marks in the output.

---

```
# Committee Meeting Simulation
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter loaded from: [path to charter file, or "Signal defaults — no charter found: PM, Architect, Inertia-Advocate"]
Participants: [list all loaded role names]

---

## INVESTIGATION-ATTEMPT-1

(a) Current workflow displaced: [specific task, tool, or process — name it, not generic]
(b) Integration dependencies: [named list of systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author did not anticipate]

GATE-1: [YES — finding (d) is non-obvious because [specific reason] / NO — insufficient: [why (d) does not qualify as a genuine surprise]]

[GATE-1 is NO instruction: output INVESTIGATION-ATTEMPT-2 block below with rewritten (a)–(d), then GATE-2. Continue with sequential labels until GATE-N is YES. Do not fill PARTICIPANT SORT or any later section until a GATE-N: YES line appears in the output.]

---

## PARTICIPANT SORT

Tier 1 (CHALLENGERS): [roles whose documented lens interrogates feasibility, risk, or disruption to existing systems]
Tier 2 (CONDITIONALS): [roles that hold approval pending specific named conditions]
Tier 3 (ADVOCATES): [roles whose orientation aligns with the proposal's stated goals]
Tie-break within tier: higher institutional veto authority speaks first

SORT-CHECK: [Tier 1 and Tier 2 both empty? YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed to voices]

[SORT-CHECK is YES instruction: re-output the corrected tier assignment above before filling any voice block.]

---

## PARTICIPANT VOICES

[Write one block per participant in tier order: Tier 1 → Tier 2 → Tier 3. CITE: and RESPONDS-TO: are required for every Tier 3 block — do not omit them.]

---

### [Role Name 1] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows the STANCE: line and must not soften, qualify, or contradict it. Tier 1: lead with the specific concern. Tier 2: name the specific condition. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: ([a/b/c/d]) — [content of that investigation finding as it supports this endorsement — do not omit the parenthesized label as first token]
RESPONDS-TO: "[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern — do not remove the quotation marks]

---

### [Role Name 2] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences...]
CITE: ([a/b/c/d]) — [...]
RESPONDS-TO: "[quoted or paraphrased concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence response]

---

[Repeat block for each participant. CITE: and RESPONDS-TO: are required for every Tier 3 block. At minimum: one participant must declare CONDITION or BLOCK.]

---

## TALLY
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK

---

## DECISIONS

Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the blocking condition]
  Trigger: [concrete deliverable or event that causes the committee to re-review — specific, not vague]

---

## ACTION ITEMS

[Owner Role] — [specific action] — [deadline]
[Owner Role] — [specific action] — [deadline]
[add rows as needed]

Rule: every item has a named owner, a specific deliverable, and a deadline. "Investigate further" fails.

---

## DISSENTING OPINIONS

[If dissent:]
- Role: [dissenting role name]
  Objection: [substance of the objection — citable to STANCE: rationale above]
  Resolution path: [concrete condition] — [authority role] confirms when [condition met]

[If no dissent:]
No dissent — [one sentence: why consensus emerged]

---
```

**Template enforcement rules:**

1. Load participants from `.roles/` using the charter for this committee type. State fallback explicitly if no charter exists.
2. GATE-N fields are mandatory. If GATE-N is NO: do not fill PARTICIPANT SORT or any later section. Output a labeled rewrite attempt (`INVESTIGATION-ATTEMPT-N+1:`) with rewritten (a)–(d) and a new `GATE-N+1:`. This loop must be visible in the output — a claimed revision that produces no new labeled attempt block fails C-22.
3. The SORT-CHECK field is mandatory. If SORT-CHECK is YES: re-output the corrected tier block before filling any voice block.
4. `STANCE:` is a structural declaration — a standalone labeled line, not embedded in prose.
5. `CITE:` is required for every Tier 3 voice. The parenthesized letter `([a/b/c/d])` must be the first element after `CITE:`, followed by ` — ` and then content. A CITE: field that begins with prose before the label fails C-20. Do not omit this field — its absence leaves a visible blank in the template.
6. `RESPONDS-TO:` is required for every Tier 3 voice. The quoted string inside `"[...]"` must attribute a specific concern by role name and paraphrase its content — `"[Role Name]'s concern that [specific concern text]"`. A generic acknowledgment does not fill the attribution slot and fails C-21. Do not remove the quotation marks.
7. The `Re-entry path` in DECISIONS has two required fields: `Owner:` and `Trigger:`. A path missing either part is incomplete and fails C-23.
8. The TALLY: line must appear between the last voice block and DECISIONS — do not skip or embed in prose.
