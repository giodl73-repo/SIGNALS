# org:committee Variations — Round 7
Generated: 2026-03-16
Skill: org:committee
Rubric: v7 (C-24 investigation rewrite attempts carry sequential labels; C-25 tier sort validation appears as a named discrete gate with explicit test condition and declared result; C-26 simulation organized into explicitly labeled sequential phases; aspirational pool 18 criteria, max 126)

---

## V-01 — Single-axis: Lifecycle Emphasis — Phase-First Architecture (C-26)

**Variation axis**: Lifecycle emphasis — the entire simulation is organized as six explicitly numbered, named phases where each phase output commits before the next phase begins. Prior rounds used step labels or section headers that could be reordered or merged; V-01 makes phase sequence the load-bearing skeleton. Every criterion belongs to a specific phase; gate criteria (C-16, C-22, C-24, C-25) become phase-internal checks that the phase cannot close without resolving.

**Hypothesis**: When phases are the organizing principle rather than a post-hoc label, C-26 compliance is structural rather than incidental. The phase-commit model makes retroactive softening visible as a phase-boundary violation: you cannot revise Phase 1 investigation findings after Phase 2 begins without reopening a committed phase. Similarly, gate criteria become phase-exit conditions: Phase 1 cannot close without GATE-N: YES (C-16/C-22/C-24); Phase 2 cannot close without SORT-CHECK: NO (C-25). The phase skeleton enforces all prior structural criteria by giving each one a fixed position in an ordered sequence.

---

You are running org:committee — a pre-meeting simulation. Execute the simulation in six explicitly labeled, sequential phases. Each phase must be written to completion before the next phase begins. Phase outputs are commitments — do not revise a prior phase once it is written.

---

### PHASE 0 — COMMITTEE DECLARATION

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter: [path to .craft/roles/ file used, or "Signal defaults — no charter found"]
Participants: [list each loaded role name with charter-defined orientation in parentheses]
```

Read `.craft/roles/` for this committee type's charter and load every named role. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state the fallback explicitly.

Phase 0 commits: committee type, charter source, participant roster, agenda item. Proceed to Phase 1.

---

### PHASE 1 — INVESTIGATION

Before any participant speaks, investigate what workflows, habits, and integrations the agenda item displaces. Begin the investigation labeled as INVESTIGATION-ATTEMPT-1.

```
INVESTIGATION-ATTEMPT-1:
(a) Current workflow: [specific task, tool, or process this proposal displaces — name it, not generic]
(b) Integration dependencies: [named systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author is unlikely to have anticipated]

GATE-1: [YES — finding (d) is non-obvious because [specific reason the proposal author would not have written this] / NO — insufficient: [brief explanation why (d) does not qualify as a genuine surprise]]
```

**Phase 1 gate rule**: If GATE-1 is NO, do not close Phase 1. Output `INVESTIGATION-ATTEMPT-2:` with freshly rewritten (a)–(d), then output `GATE-2:`. Repeat using sequential attempt labels (`INVESTIGATION-ATTEMPT-N:` / `GATE-N:`) until a gate answer of YES appears in the output. Each attempt must be a labeled output block — a claimed internal revision with no new labeled block does not satisfy C-22. The sequential label makes the iteration count visible and auditable (C-24).

Phase 1 closes when GATE-N: YES is produced. Proceed to Phase 2.

---

### PHASE 2 — TIER SORT

Sort all loaded participants into three tiers based on their charter-defined orientations and Phase 1 findings.

```
TIER SORT:
Tier 1 — CHALLENGERS: [roles whose documented lens interrogates feasibility, risk, or disruption to existing systems — speak first]
Tier 2 — CONDITIONALS: [roles that hold approval pending specific named conditions]
Tier 3 — ADVOCATES: [roles whose orientation aligns with the proposal's stated goals]
Tie-break: higher institutional veto authority speaks first within a tier

SORT-CHECK: Tier 1 and Tier 2 both empty? [YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed to Phase 3]
```

The `SORT-CHECK:` line is required. Its test condition and declared result must appear as a discrete, labeled gate line — correct tier ordering without a SORT-CHECK line does not satisfy C-25. The test condition is fixed: "Tier 1 and Tier 2 both empty?" The result must be declared as YES or NO with the appropriate follow-on.

If SORT-CHECK is YES: re-output the corrected TIER SORT block (including a new SORT-CHECK line) before proceeding. Do not write any voice block until SORT-CHECK produces a NO result.

Phase 2 commits: tier assignments, SORT-CHECK result. Proceed to Phase 3.

---

### PHASE 3 — PARTICIPANT VOICES

Write one voice block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3. All voices are Phase 3 content — do not intermix Phase 3 and Phase 4/5 content.

Voice format:

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration on its own line — prose follows on the next line and must not soften, qualify, or contradict the declared stance. Tier 1: lead with the specific concern. Tier 2: name the specific condition for approval. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: ([a/b/c/d]) — [content of that Phase 1 finding supporting this endorsement — parenthesized label must be the first token after CITE:]
RESPONDS-TO: "[quote or close paraphrase of the specific Tier 1 or Tier 2 concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern]
```

Requirements:
- `CITE:` and `RESPONDS-TO:` are required for every Tier 3 voice. A Tier 3 block missing either field is incomplete.
- `CITE:` format rule (C-20): parenthesized label `(a)/(b)/(c)/(d)` must be the first element after `CITE:`. Any prose before the label fails.
- `RESPONDS-TO:` format rule (C-21): the quoted string must attribute a specific concern by role name and paraphrase its substance. Generic acknowledgment ("there are concerns about this") fails.
- At least one participant must declare CONDITION or BLOCK. An all-APPROVE Phase 3 means the Phase 2 sort is invalid — close Phase 3, reopen Phase 2, revise tiers.

Phase 3 commits when all participant voices are written. Proceed to Phase 4.

---

### PHASE 4 — TALLY

After all Phase 3 voices and before any formal minutes section:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

Phase 4 commits: tally and outcome. Proceed to Phase 5.

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

Both Owner and Trigger are required fields. A re-entry path missing either part is incomplete (C-23).

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Every item: named owner, specific deliverable, deadline. "Investigate further" fails.

#### DISSENTING OPINIONS

For each non-approving voice: dissenting role, substance of the objection, resolution path (concrete condition + named authority who confirms when condition is met).

If no dissent: "No dissent — [one sentence on the basis for consensus]."

Phase 5 commits the simulation record.

---

## V-02 — Single-axis: Role Sequence — SORT-CHECK as Named Discrete Gate (C-25)

**Variation axis**: Role sequence — specifically how the tier sort validation is enforced. Prior rounds included sort validation as a prose directive ("reassign if all-approve") or as a conditional inline note. V-02 makes SORT-CHECK a named, discrete gate with a pre-printed two-field structure: an explicit test condition and a required declared result. The test condition is fixed text; the result field must be filled with YES or NO and the corresponding action.

**Hypothesis**: R6 V-01 and V-03 both included SORT-CHECK language but as inline one-liners where the test condition was embedded in the result prose. C-25's pass condition requires the test condition and the declared result to be discrete, labeled elements — not inferrable from correct output ordering alone. When SORT-CHECK is pre-printed as a two-field block with a fixed test question, the model cannot produce correct tier ordering without also producing a visible gate declaration. A simulation that sorts correctly but omits SORT-CHECK fails C-25; a simulation that sorts incorrectly but produces SORT-CHECK with YES → correction passes C-25. The gate is the enforcement mechanism for both C-11 (challenger-first ordering) and C-18 (all-approve self-correction) — making the gate visible makes both structural invariants auditable.

---

You are simulating a committee meeting before the real one.

**Declare committee type.** Open with:

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.craft/roles/` for this committee type's charter. Load every named role with their documented orientation. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state the fallback explicitly.

**Investigate before anyone speaks.** Name what this proposal displaces. Label this block `INVESTIGATION-ATTEMPT-1`.

```
INVESTIGATION-ATTEMPT-1:
(a) Current workflow: [specific task, tool, or process — name it, not generic]
(b) Integration dependencies: [named list of systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author did not anticipate]

GATE-1: [YES — finding (d) is non-obvious because [specific reason] / NO — insufficient: [brief explanation why (d) does not qualify]]
```

**C-22 enforcement**: If GATE-1 is NO, output `INVESTIGATION-ATTEMPT-2:` with rewritten (a)–(d), then output `GATE-2:`. Use sequential labels (`INVESTIGATION-ATTEMPT-N:` / `GATE-N:`) until the gate passes. Each rewrite must be a labeled output block with a sequential attempt number (C-24). Do not proceed to the tier sort until GATE-N: YES appears.

**Sort participants.** After the investigation passes:

```
TIER SORT:
Tier 1 (CHALLENGERS): [roles whose charter orientation interrogates feasibility, risk, or disruption — speak before all others]
Tier 2 (CONDITIONALS): [roles that hold approval pending specific named conditions]
Tier 3 (ADVOCATES): [roles whose orientation aligns with the proposal's stated goals]
Tie-break within tier: higher institutional veto authority speaks first
```

**SORT-CHECK gate (C-25).** Immediately after the tier sort block, output this gate. Both fields are required.

```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed to voices]
```

The `Test:` field contains the fixed test condition. The `Result:` field declares YES or NO with the required action. An output that produces correct tier ordering without a SORT-CHECK block containing both `Test:` and `Result:` fields fails C-25 regardless of ordering correctness.

If Result is YES: re-output the corrected TIER SORT block, then output a new SORT-CHECK gate. Repeat until Result is NO. Do not write any voice block until SORT-CHECK Result is NO.

**Write voices in tier order: Tier 1 → Tier 2 → Tier 3.**

Voice format:

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it. Tier 1: lead with the concern. Tier 2: name the specific condition. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: ([a/b/c/d]) — [content of that investigation finding supporting this endorsement — parenthesized label is first token after CITE:]
RESPONDS-TO: "[quote or close paraphrase of the specific concern raised — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern]
```

`CITE:` and `RESPONDS-TO:` are required for every Tier 3 voice. Parenthesized label must be the first element after `CITE:` (C-20). The quoted string must attribute a specific concern by role name and content — generic acknowledgment fails (C-21). At least one participant must declare CONDITION or BLOCK (C-05/C-18).

**Vote tally — required before minutes:**

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

**Formal minutes:**

#### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the blocking condition]
  Trigger: [concrete deliverable or event that causes committee re-review]
```

Both Owner and Trigger are required (C-23).

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. Vague items fail.

#### DISSENTING OPINIONS

For each dissent: dissenting role, substance, resolution path (concrete condition + named authority).

If none: "No dissent — [one sentence on the basis for consensus]."

---

## V-03 — Single-axis: Inertia Framing — Switching-Cost Investigation as Primary First Act (C-12)

**Variation axis**: Inertia framing — the investigation explicitly asks "what does the status quo protect?" rather than generically "what are the risks?" The inertia-advocate is the mandatory first speaker, established before all other participants, and their voice produces named INERTIA-FINDING tags that serve as the primary named concerns on the committee record. All subsequent Tier 3 voices must respond to a named INERTIA-FINDING tag, making C-21 compliance structurally natural: generic acknowledgment is ruled out by the tag-name requirement.

**Hypothesis**: Prior rounds ran the investigation as a generic risk scan. When the investigation is framed as a switching-cost audit — "what existing behavior, workflow, or integration would this proposal break?" — the model is more likely to surface a genuine non-obvious cost (C-09, C-16). The inertia framing also creates a higher bar for GATE-N: YES: the model must identify something the proposal author specifically overlooked, not just risks in general. When the gate fails (C-22), sequential rewrite attempts are more likely to produce genuinely different findings because the framing forces a different angle with each attempt (C-24). INERTIA-FINDING tags additionally give C-21 a structural anchor: `RESPONDS-TO:` targets are named committee-record entries, not generic paraphrases of a prior speaker.

---

You are simulating a committee meeting before the real one.

**Open with:**

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.craft/roles/` for this committee type's charter. Additionally, check `.craft/roles/` for `inertia-advocate.md` — if it exists and is not already in the charter, add the Inertia-Advocate as a mandatory first speaker. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state them.

---

**PHASE 1 — SWITCHING-COST INVESTIGATION**

Before any participant speaks, run a switching-cost audit. The question is not "what are the risks?" but "what does the status quo protect?" Label this block INVESTIGATION-ATTEMPT-1.

```
INVESTIGATION-ATTEMPT-1:
(a) Status-quo workflow protected: [name the specific task, tool, or process that currently works and would be displaced — not generic]
(b) Integration surface at risk: [named list of systems, APIs, contracts, or downstream consumers affected]
(c) Team whose habits would break: [specific cognitive habit and the specific team that owns it]
(d) Non-obvious switching cost: [the cost the proposal author almost certainly did not account for — name it with enough specificity that the author would say "I missed that"]

GATE-1: [YES — finding (d) is non-obvious because [specific reason the proposal author would not have written this] / NO — insufficient: [why (d) does not clear the non-obvious threshold]]
```

If GATE-1 is NO: do not proceed to the Inertia-Advocate voice. Output `INVESTIGATION-ATTEMPT-2:` with rewritten (a)–(d), asking a different switching-cost question in each field. Output `GATE-2:`. Repeat with sequential attempt labels (`INVESTIGATION-ATTEMPT-N:` / `GATE-N:`) until the gate passes. Every rewrite attempt must carry a sequential label — unlabeled rewrites do not satisfy C-24.

---

**PHASE 2 — INERTIA-ADVOCATE VOICE (Mandatory First Speaker)**

The Inertia-Advocate speaks before all other participants. This is not optional.

```
### Inertia-Advocate — Tier 1 (First Speaker)
STANCE: [CONDITION / BLOCK — the Inertia-Advocate does not freely approve on first pass]
[3-5 sentences building the evidence-based case for the status quo or for delay. Ground the critique in named Phase 1 findings — cite (a), (b), (c), or (d) by label. This voice sets the null hypothesis every subsequent speaker must address.]

INERTIA-FINDING-A: [one-line summary of the strongest status-quo argument — citable to a Phase 1 finding by label]
INERTIA-FINDING-B: [one-line summary of the second-strongest argument — citable to a Phase 1 finding by label]
```

INERTIA-FINDING-A and INERTIA-FINDING-B are the primary named concerns on the committee record. All subsequent voices must engage with at least one of them.

---

**PHASE 3 — REMAINING PARTICIPANT SORT**

Sort all remaining participants (excluding the Inertia-Advocate, who has already spoken):

```
REMAINING SORT:
Skeptics (speak next): [roles whose charter orientation interrogates risk, compliance, or feasibility]
Advocates (speak last): [roles aligned with the proposal's stated goals]
Tie-break: higher veto authority speaks first within group

SORT-CHECK: Tier 1 and Tier 2 both empty (all remaining participants are Advocates)? [YES — [role] mis-sorted; reassigning to Skeptics because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed to voices]
```

If SORT-CHECK is YES: re-output the corrected sort and run SORT-CHECK again. Do not write any remaining voice until SORT-CHECK is NO.

---

**PHASE 4 — REMAINING PARTICIPANT VOICES**

Write remaining voices in sort order: Skeptics → Advocates.

```
### [Role Name] — [Skeptic / Advocate]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it. Skeptic voices: name the specific concern; may ground in Phase 1 findings or name an INERTIA-FINDING tag. Advocate voices: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: ([a/b/c/d] or INERTIA-FINDING-A or INERTIA-FINDING-B) — [the finding label, immediately followed by the specific content from that finding that supports this endorsement — parenthesized label or tag name must be first token after CITE:]
RESPONDS-TO: "INERTIA-FINDING-[A/B]: [paraphrase of the tag's specific content]" — [one sentence: how this endorsement addresses that specific finding]
```

`CITE:` and `RESPONDS-TO:` are required for every Advocate voice.

- `CITE:` format rule (C-20): the label — `(a)/(b)/(c)/(d)` or `INERTIA-FINDING-A/B` — must be the first element after `CITE:`. Prose before the label fails.
- `RESPONDS-TO:` format rule (C-21): naming `INERTIA-FINDING-A` or `INERTIA-FINDING-B` by tag name and paraphrasing its content satisfies C-21 structurally. Generic acknowledgment ("inertia concerns have been noted") fails.
- At least one non-Inertia-Advocate participant must declare CONDITION or BLOCK — the Inertia-Advocate alone does not satisfy C-05.

---

**PHASE 5 — TALLY**

After all voices, before any formal section:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

---

**PHASE 6 — FORMAL MINUTES**

#### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for resolving the blocking finding]
  Resolves: [INERTIA-FINDING-A or INERTIA-FINDING-B — the tag this path addresses]
  Trigger: [concrete deliverable or event that causes committee re-review — traceable to the Resolves tag]
```

`Owner:` and `Trigger:` are both required (C-23). The `Resolves:` field names which INERTIA-FINDING tag is being addressed, grounding the trigger in a specific committee record entry rather than an invented condition.

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. Vague items fail.

#### DISSENTING OPINIONS

For each dissent: dissenting role, substance, resolution path (concrete condition + named authority). The Inertia-Advocate's dissent, if declared, must reference INERTIA-FINDING-A or INERTIA-FINDING-B explicitly.

If none: "No dissent — [one sentence on the basis for consensus]."

---

## V-04 — Combined: Lifecycle Emphasis + Role Sequence — Phase Architecture with SORT-CHECK as Phase-Exit Gate (C-26 + C-25)

**Variation axes**: Lifecycle emphasis (phase-first architecture, V-01 axis) + Role sequence (SORT-CHECK as named discrete gate, V-02 axis). V-04 combines the two structural enforcement mechanisms introduced in R7: phases as the organizing skeleton (C-26), and SORT-CHECK as a two-field gate that must appear within Phase 2 before the phase can close (C-25). Each gate criterion becomes a phase-exit condition: Phase 1 cannot close without GATE-N: YES (C-16/C-22/C-24); Phase 2 cannot close without SORT-CHECK Result: NO (C-25).

**Hypothesis**: V-01 positions phases as the primary structural skeleton and treats SORT-CHECK as one of several phase-internal requirements. V-02 positions SORT-CHECK as the primary structural gate and treats phases as context. V-04 combines them: the phase structure makes gate positions unambiguous (each gate is a specific phase's exit condition), and the SORT-CHECK two-field format makes the Phase 2 exit condition explicitly visible as a labeled gate. The combination produces tighter C-25/C-26 co-compliance than either axis alone, because the phase-boundary model requires SORT-CHECK to appear within a named phase, and the SORT-CHECK gate format requires the test condition and result to be discrete fields, not inferrable from downstream output.

---

You are running org:committee — a pre-meeting simulation. Execute in five explicitly numbered, named phases. Each phase must complete before the next begins. Phase outputs are commitments.

---

### PHASE 0 — COMMITTEE DECLARATION

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter: [path to .craft/roles/ file used, or "Signal defaults — no charter found"]
Participants: [list each loaded role name with charter-defined orientation in parentheses]
```

Read `.craft/roles/` for this committee type's charter. Load every named role. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state the fallback.

**Phase 0 commits.** Proceed to Phase 1.

---

### PHASE 1 — INVESTIGATION

Label the first investigation block `INVESTIGATION-ATTEMPT-1:`.

```
INVESTIGATION-ATTEMPT-1:
(a) Current workflow: [specific task, tool, or process this proposal displaces — name it]
(b) Integration dependencies: [named systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author did not anticipate]

GATE-1: [YES — finding (d) is non-obvious because [specific reason] / NO — insufficient: [brief explanation why (d) does not qualify]]
```

**Phase 1 exit condition**: GATE-N must be YES before Phase 1 closes. If GATE-1 is NO: output `INVESTIGATION-ATTEMPT-2:` with rewritten (a)–(d) and `GATE-2:`. Use sequential labels (`INVESTIGATION-ATTEMPT-N:` / `GATE-N:`) until the gate passes. Each rewrite attempt carries a sequential label (C-24) — a claimed revision with no labeled output block does not close Phase 1.

**Phase 1 commits when GATE-N: YES.** Proceed to Phase 2.

---

### PHASE 2 — TIER SORT

Sort all loaded participants:

```
TIER SORT:
Tier 1 — CHALLENGERS: [roles whose lens interrogates feasibility, risk, or disruption — speak first]
Tier 2 — CONDITIONALS: [roles that hold approval pending specific named conditions]
Tier 3 — ADVOCATES: [roles aligned with the proposal's stated goals]
Tie-break: higher institutional veto authority speaks first within a tier
```

**Phase 2 exit condition — SORT-CHECK gate (C-25)**. Immediately after the tier sort, output this gate. Both fields are required before Phase 2 can close:

```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, Phase 2 commits]
```

The `Test:` field is the fixed test condition. The `Result:` field is the declared gate result. An output that produces correct tier ordering without both fields appearing under a `SORT-CHECK:` header fails C-25. The test condition and declared result are the gate — correct ordering alone is not the gate.

If Result is YES: re-output the corrected TIER SORT block and output a new SORT-CHECK gate. Repeat until Result is NO.

**Phase 2 commits when SORT-CHECK Result is NO.** Proceed to Phase 3.

---

### PHASE 3 — PARTICIPANT VOICES

Write one voice block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3.

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it. Tier 1: lead with the specific concern. Tier 2: name the specific condition. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
CITE: ([a/b/c/d]) — [content of that Phase 1 finding supporting this endorsement — parenthesized label must be first token after CITE:]
RESPONDS-TO: "[quote or close paraphrase of the specific concern — attributed as: '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern]
```

Requirements:
- `CITE:` and `RESPONDS-TO:` are required for every Tier 3 voice.
- `CITE:` format: parenthesized label `(a)/(b)/(c)/(d)` is the first element after `CITE:` (C-20).
- `RESPONDS-TO:` format: quoted string attributes a specific concern by role name and content — generic acknowledgment fails (C-21).
- At least one participant must declare CONDITION or BLOCK. An all-APPROVE Phase 3 means Phase 2 sort is invalid — reopen Phase 2.

**Phase 3 commits when all voices are written.** Proceed to Phase 4.

---

### PHASE 4 — TALLY

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

**Phase 4 commits.** Proceed to Phase 5.

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

Both Owner and Trigger are required (C-23).

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. Vague items fail.

#### DISSENTING OPINIONS

For each dissent: dissenting role, substance, resolution path (concrete condition + named authority).

If none: "No dissent — [one sentence on the basis for consensus]."

**Phase 5 commits the simulation record.**

---

## V-05 — Combined: Lifecycle + Role Sequence + Inertia Framing — Golden Synthesis as Pre-Printed Template (C-24 + C-25 + C-26)

**Variation axes**: Output format (template-completion) + lifecycle emphasis (numbered phase skeleton) + role sequence (SORT-CHECK two-field gate) + inertia framing (INERTIA-FINDING tags as named committee-record concerns). All three new R7 criteria are enforced through pre-printed structural fields the model must fill — not through prose instruction that may be de-prioritized under attention pressure. INVESTIGATION-ATTEMPT-N/GATE-N are pre-printed slots with sequential numbering that must increment visibly on rewrite (C-24); SORT-CHECK is a pre-printed two-field gate block (C-25); Phase 0–5 headers are pre-printed skeleton (C-26); INERTIA-FINDING-A/B are pre-printed tags in the first-speaker block (inertia framing / C-12/C-21).

**Hypothesis**: R6 V-05 demonstrated that the golden synthesis approach — all aspirational criteria as pre-printed template fields — produces the highest composite score with the lowest model-behavior risk. V-05 applies the same principle to R7's three new criteria: each new criterion becomes a pre-printed slot the model fills, not a behavioral instruction the model follows. The template-completion model converts structural compliance from a generation task to a transcription task. An INVESTIGATION-ATTEMPT-2 block that is missing has a visible gap in the numbered sequence; a SORT-CHECK block with an unfilled Test: field has a visible blank; a Phase 2 that is unlabeled has a visible missing header. The model cannot produce the required structural pattern without the template producing the correct output — the pre-printed structure is the enforcement.

---

You are simulating a committee meeting before the real one. Populate the template below exactly. Do not skip sections. Do not reorder sections. Where a field shows `[...]`, fill it with the required content. Where the template shows quotation marks around a placeholder — `"[...]"` — fill the quoted string and preserve the quotation marks in the output.

---

```
# Committee Meeting Simulation

## PHASE 0 — COMMITTEE DECLARATION

Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter loaded from: [path to .craft/roles/ file, or "Signal defaults — no charter found: [list fallback roles]"]
Participants:
- [Role Name 1] — [charter-defined orientation in one phrase]
- [Role Name 2] — [charter-defined orientation in one phrase]
- [add one line per loaded role]

---

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

(a) Status-quo workflow protected: [specific task, tool, or process the proposal displaces — name it, not generic]
(b) Integration dependencies: [named list of systems, APIs, or contracts affected]
(c) Habit disruption: [specific cognitive habit; specific affected team]
(d) Non-obvious cost: [the surprise — something the proposal author almost certainly did not anticipate]

GATE-1: [YES — finding (d) is non-obvious because [specific reason the proposal author would not have written this] / NO — insufficient: [brief explanation why (d) does not clear the non-obvious threshold]]

[If GATE-1 is NO: output the INVESTIGATION-ATTEMPT-2 block below before proceeding. The next attempt must carry a sequential label. Do not fill PHASE 2 or any later section until a GATE-N: YES line appears.]

### INVESTIGATION-ATTEMPT-2 [fill only if GATE-1 is NO; omit if GATE-1 is YES]

(a) Status-quo workflow protected: [rewritten — different angle from Attempt 1]
(b) Integration dependencies: [rewritten]
(c) Habit disruption: [rewritten]
(d) Non-obvious cost: [rewritten — a different candidate non-obvious cost]

GATE-2: [YES — finding (d) is non-obvious because [specific reason] / NO — insufficient: [brief explanation]]

[If GATE-2 is NO: continue the sequence as INVESTIGATION-ATTEMPT-3 / GATE-3, etc. The sequential label (C-24) must increment with each attempt. Do not proceed to PHASE 2 until GATE-N: YES.]

---

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: [roles whose documented lens interrogates feasibility, risk, or disruption to existing systems — speak first]
Tier 2 — CONDITIONALS: [roles that hold approval pending specific named conditions]
Tier 3 — ADVOCATES: [roles whose orientation aligns with the proposal's stated goals]
Tie-break within tier: higher institutional veto authority speaks first

### SORT-CHECK [required — do not omit]

  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item]; corrected TIER SORT block follows / NO — valid sort, Phase 2 commits]

[If Result is YES: re-output a corrected TIER SORT block and a new SORT-CHECK block above before filling Phase 3. Repeat until Result is NO. Do not write any voice block until SORT-CHECK Result is NO.]

---

## PHASE 3 — PARTICIPANT VOICES

[Write one block per participant in tier order: Tier 1 → Tier 2 → Tier 3. For Tier 3 voices: CITE: and RESPONDS-TO: are required fields — do not omit them. First Tier 1 speaker must be the Inertia-Advocate if present in the charter.]

---

### [Inertia-Advocate or first Tier 1 Role] — Tier 1

STANCE: [CONDITION / BLOCK]
[3-5 sentences. Ground the critique in named Phase 1 findings — cite (a), (b), (c), or (d) by label. This voice sets the null hypothesis every subsequent speaker must address.]

INERTIA-FINDING-A: [one-line summary of the strongest status-quo argument — citable to a Phase 1 finding label]
INERTIA-FINDING-B: [one-line summary of the second-strongest argument — citable to a Phase 1 finding label]

---

### [Role Name — subsequent Tier 1 participant, if any] — Tier 1

STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it. Lead with the specific concern.]

---

### [Role Name — Tier 2 participant] — Tier 2

STANCE: [CONDITION]
[2-4 sentences. Name the specific condition for approval. STANCE: is a standalone labeled declaration.]

---

### [Role Name — Tier 3 participant] — Tier 3

STANCE: [APPROVE]
[2-4 sentences from documented role orientation. Complete CITE: and RESPONDS-TO: before any endorsement prose. STANCE: is a standalone labeled declaration.]
CITE: ([a/b/c/d] or INERTIA-FINDING-A or INERTIA-FINDING-B) — [the label must be the first element after CITE:, immediately followed by " — " and then the finding content that supports this endorsement — no prose before the label]
RESPONDS-TO: "[quoted or paraphrased concern — attributed as: 'INERTIA-FINDING-[A/B]: [paraphrase of tag content]' or '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern — do not remove the quotation marks]

---

[Repeat Tier 3 block for each Tier 3 participant. Each Tier 3 block must include CITE: and RESPONDS-TO: fields. At minimum: one participant across the simulation must declare CONDITION or BLOCK.]

---

## PHASE 4 — TALLY

TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]

---

## PHASE 5 — MINUTES

### DECISIONS

Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for satisfying the blocking condition]
  Resolves: [INERTIA-FINDING-A or INERTIA-FINDING-B, or the specific named condition — the committee record entry this path addresses]
  Trigger: [concrete deliverable or event that causes committee re-review — traceable to the Resolves entry]

### ACTION ITEMS

[Owner Role] — [specific action] — [deadline]
[Owner Role] — [specific action] — [deadline]
[add rows as needed — every item has a named owner, specific deliverable, and deadline; "investigate further" fails]

### DISSENTING OPINIONS

[If dissent:]
- Role: [dissenting role name]
  Objection: [substance of the objection — citable to STANCE: rationale above]
  Resolution path: [concrete condition] — [authority role] confirms when [specific condition met]

[If no dissent:]
No dissent — [one sentence: why consensus emerged]

---
```

**Template enforcement rules applied while filling:**

1. Load participants from `.craft/roles/` using the charter for this committee type. State fallback explicitly if no charter exists.
2. Phase headers (PHASE 0 through PHASE 5) are required. A simulation that produces all required content without phase labels fails C-26. A single unlabeled phase or two phases merged under one header is a partial pass.
3. GATE-N fields are mandatory. If GATE-N is NO: do not fill PHASE 2 or any later section. Output a new labeled `INVESTIGATION-ATTEMPT-N+1` block with rewritten (a)–(d) and a new `GATE-N+1:` line. The sequential number must increment (C-24) — a rewrite attempt without a new sequential label does not satisfy C-24 regardless of whether C-22 is satisfied.
4. The SORT-CHECK block is mandatory within PHASE 2. Both `Test:` and `Result:` fields must appear under the `SORT-CHECK` header. An output whose tier sort produces correct ordering without a SORT-CHECK block containing both fields fails C-25.
5. `STANCE:` is a structural declaration — a standalone labeled line, not embedded in prose.
6. `CITE:` is required for every Tier 3 voice. The label — `([a/b/c/d])` or `INERTIA-FINDING-A/B` — must be the first element after `CITE:`, followed by ` — ` and then content. Prose before the label fails C-20.
7. `RESPONDS-TO:` is required for every Tier 3 voice. The quoted string inside `"[...]"` must attribute a specific concern by role name or tag name and paraphrase its content. Generic acknowledgment does not fill the attribution slot and fails C-21. Preserve the quotation marks.
8. `Owner:` and `Trigger:` are both required in the re-entry path. `Resolves:` names the committee record entry being addressed, grounding the trigger. A path missing Owner or Trigger fails C-23.
9. The TALLY line must appear within PHASE 4, between the last voice block and PHASE 5. Do not skip or embed in prose.
