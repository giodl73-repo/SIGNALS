# org:committee Variations — Round 9
Generated: 2026-03-16
Skill: org:committee
Rubric: v9 (C-27 switching-cost findings carry named INERTIA-FINDING labels; C-28 all structural slots pre-declared as skeleton before content; C-29 phase gates are intra-phase retry loops not inter-phase execution prerequisites; aspirational pool 21 criteria, composite max 132)

R8 reference context: V-01 scored 129/130 — only deficiency was C-28 PARTIAL (labels emerged inline, not pre-declared). V-02 scored 24/60 essential — Phase 1 gate was written as inter-phase halt ("do not proceed to Phase 2"), making Phases 2–5 absent from the prompt and causing cascading failures on all voice, tally, and minutes criteria. C-29 formalizes this failure as a structural invariant: the gate-rewrite loop must run within Phase 1; Phase 2 begins unconditionally once the gate answers YES.

Variation axes selected:
- Single-axis V-01: Output format — full skeleton pre-declaration (C-28 primary + C-29)
- Single-axis V-02: Inertia framing — INERTIA-FINDING-* named labels as primary citation anchors (C-27 primary)
- Single-axis V-03: Phrasing register — imperative micro-instructions with loop constructs
- Combined V-04: Lifecycle emphasis + C-29 — phase architecture with explicit intra-phase loop diagrams
- Combined V-05: Full synthesis — skeleton + named labels + loop architecture + all criteria

---

## V-01 — Single-axis: Output Format — Skeleton-First Declaration (C-28)

**Variation axis**: Output format — the entire simulation is anchored by a pre-printed skeleton that names every structural slot before any content is generated. The skeleton is the first thing printed; all content fills named slots. Phase 2 and all subsequent phases appear in the skeleton unconditionally: the Phase 1 gate loop operates by iterating within Phase 1's named slots, not by conditionally including or excluding later phases. An unfilled slot in the skeleton is a visible gap; a skipped phase has a visible missing header.

**Hypothesis**: R8 V-01 scored 129/130 with C-28 PARTIAL because structural labels emerged correctly but inline, not pre-declared. The only fix needed is to print the full skeleton upfront. When every slot is pre-printed — INERTIA-FINDING-A through D, GATE-N, SORT-CHECK with Test/Result fields, STANCE:/CITE:/RESPONDS-TO: for each participant voice, TALLY, all DECISIONS/ACTION ITEMS/DISSENTING OPINIONS fields — the model fills slots rather than decides whether to include them. C-29 compliance follows structurally: Phase 2's header is already on the page, so the Phase 1 gate loop cannot terminate the simulation; it can only delay filling Phase 2 until the loop exits. The skeleton converts every structural criterion from a behavioral requirement into a transcription task.

---

You are running `org:committee`. Before generating any simulation content, print the complete skeleton below with all fields at their placeholder values. Then fill the skeleton top to bottom. Do not skip sections, do not reorder sections, do not merge sections. Every `___` is a required fill.

---

**STEP 1 — PRINT THIS SKELETON EXACTLY AS SHOWN:**

```
=== org:committee SIMULATION SKELETON ===

## PHASE 0 — COMMITTEE DECLARATION

Committee Type: ___
Agenda Item: ___
Charter Source: ___
Participants:
  - ___ — ___
  [one line per loaded role]

## PHASE 1 — INVESTIGATION

### INVESTIGATION-ATTEMPT-1

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-1:
  Question: Does at least one finding above reveal a non-obvious cost the proposal author is unlikely to have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[PHASE-1 LOOP INSTRUCTION — execute within Phase 1 before proceeding to Phase 2:
  → If GATE-1 Answer: YES → loop exits; Phase 2 fills unconditionally
  → If GATE-1 Answer: NO → output INVESTIGATION-ATTEMPT-2 block (same structure, rewritten fields, sequential label), output GATE-2 block, re-evaluate; repeat until a GATE-N Answer: YES appears; then Phase 2 fills unconditionally
  Phase 2 is always reached. The loop controls when, not whether.]

### INVESTIGATION-ATTEMPT-2 [fill only if GATE-1 is NO; otherwise omit]

INERTIA-FINDING-A: ___
INERTIA-FINDING-B: ___
INERTIA-FINDING-C: ___
INERTIA-FINDING-D: ___

GATE-2:
  Question: Does at least one finding above reveal a non-obvious cost the proposal author is unlikely to have anticipated?
  Answer: ___ [YES / NO]
  Basis: ___

[Continue as INVESTIGATION-ATTEMPT-3 / GATE-3 etc. if needed. Sequential label increments with each attempt.]

## PHASE 2 — TIER SORT

### TIER SORT

Tier 1 — CHALLENGERS: ___
Tier 2 — CONDITIONALS: ___
Tier 3 — ADVOCATES: ___
Tie-break: ___

### SORT-CHECK

  Test: Tier 1 and Tier 2 both empty?
  Result: ___ [YES — reassign: ___ to Tier ___ because ___; corrected sort follows / NO — valid sort]

[If Result YES: re-output TIER SORT block and new SORT-CHECK block above before Phase 3. Repeat until Result NO.]

## PHASE 3 — PARTICIPANT VOICES

[One block per participant, Tier 1 → Tier 2 → Tier 3]

### ___ — Tier ___

STANCE: ___
[Voice prose — 2–4 sentences from documented role orientation]
CITE: ___ — ___           [Tier 3 only — label first, content after dash]
RESPONDS-TO: "___" — ___  [Tier 3 only — quoted concern, then response]

[Repeat block for each participant]

## PHASE 4 — TALLY

TALLY: ___ APPROVE · ___ CONDITION · ___ BLOCK
OUTCOME: ___

## PHASE 5 — MINUTES

### DECISIONS

Verdict: ___
Conditions for full approval: ___
Re-entry path (if not approved):
  Owner: ___
  Trigger: ___

### ACTION ITEMS

___ — ___ — ___
[one line per item: Owner Role — specific action — deadline]

### DISSENTING OPINIONS

___
[one entry per dissent: Role — objection substance — resolution path — named authority — concrete trigger]
[If no dissent: "No dissent — [reason]"]

=== END SKELETON ===
```

---

**STEP 2 — FILL THE SKELETON:**

Fill each `___` with the required content. Rules governing fill:

**PHASE 0**: Read `.roles/` for the charter matching this committee type. Load every named role. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and name them in Charter Source as: `"Signal defaults — no charter found"`.

**PHASE 1 — INERTIA-FINDING labels**: Each finding must carry its named label (`INERTIA-FINDING-A`, `INERTIA-FINDING-B`, `INERTIA-FINDING-C`, `INERTIA-FINDING-D`) as the structural entry label, not just a parenthesized letter. The label is the citation anchor for all downstream CITE: and RESPONDS-TO: references. A finding written as `(a) [content]` without the INERTIA-FINDING-* label passes the investigation but fails C-27.

**PHASE 1 — GATE loop (C-29)**: The gate is an intra-phase loop. The loop runs within Phase 1. Phase 2 is printed in the skeleton unconditionally — the gate controls when Phase 2 is filled, not whether Phase 2 exists. If GATE-N Answer is NO: fill the next INVESTIGATION-ATTEMPT-N+1 block (already in the skeleton or extended below it), fill GATE-N+1, re-evaluate. Each new attempt carries a sequential label that increments by 1. Phase 2 fills as soon as any GATE-N Answer is YES.

**PHASE 2 — SORT-CHECK**: Both `Test:` and `Result:` fields are required. The test condition is fixed: "Tier 1 and Tier 2 both empty?" The result must be YES or NO with the appropriate action. Correct tier ordering without a SORT-CHECK block containing both fields fails C-25.

**PHASE 3 — STANCE**: Each participant's stance appears as `STANCE: [APPROVE / CONDITION / BLOCK]` — a standalone labeled line before any prose. Prose must not soften, qualify, or contradict the declared stance. For Tier 3 participants: `CITE:` and `RESPONDS-TO:` are required fields.

**PHASE 3 — CITE (Tier 3 only)**: Format: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding that supports this endorsement]`. The named label must be the first element after `CITE:`. A citation that writes the content without the label identifier fails C-20/C-27.

**PHASE 3 — RESPONDS-TO (Tier 3 only)**: Format: `RESPONDS-TO: "[quote or close paraphrase of the specific concern — attributed as: 'INERTIA-FINDING-[A/B]' or '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that concern]`. The quoted string must attribute a specific concern by name and content. Generic acknowledgment ("inertia concerns have been noted") fails C-21.

**PHASE 3 — challenge requirement**: At least one participant must declare `STANCE: CONDITION` or `STANCE: BLOCK`. An all-APPROVE voice section is a sort error — reopen Phase 2, revise tier assignments, re-run SORT-CHECK.

**PHASE 4**: TALLY appears between the last voice block and PHASE 5. Do not embed in prose.

**PHASE 5 — re-entry path**: Both `Owner:` and `Trigger:` are required when the verdict is not APPROVED. Owner names the role responsible for satisfying the blocking condition. Trigger names the concrete deliverable or event that causes the committee to re-review. A path with only one of the two fields is incomplete.

**PHASE 5 — ACTION ITEMS**: Every item requires a named owner, a specific deliverable, and a deadline. "Investigate further" is not a specific deliverable.

---

## V-02 — Single-axis: Inertia Framing — INERTIA-FINDING Named Labels as Primary Citation Anchors (C-27)

**Variation axis**: Inertia framing — the switching-cost investigation produces named entry labels (`INERTIA-FINDING-A` through `INERTIA-FINDING-D`) that function as the committee record's citation anchors throughout the simulation. Every downstream reference — CITE:, RESPONDS-TO:, dissent resolution paths, re-entry triggers — traces back to a named INERTIA-FINDING entry. The letter references `(a)/(b)/(c)/(d)` are retired; label-name citations replace them at every cite point.

**Hypothesis**: R7/R8 variations that used letter labels `(a)/(b)/(c)/(d)` in CITE: satisfied C-17 and C-20 mechanically but were fragile: a letter citation without context is ambiguous, and the model under pressure would sometimes cite `(d)` without connecting it to an INERTIA-FINDING label, producing a CITE: that fails C-27 (finding not labeled as a named entry). When the finding is named `INERTIA-FINDING-D` from the moment it is written, and CITE: must reference `INERTIA-FINDING-D` by that name, the label identity is maintained end-to-end. The named label also makes RESPONDS-TO: more specific by default: "INERTIA-FINDING-A argues that..." is a structurally named reference; "finding (a) suggests that..." is an implicit paraphrase that may not name the finding. C-27 is most naturally satisfied when the label is the primary identifier, not an annotation on a parenthesized letter.

---

You are running `org:committee`. Simulate a committee meeting before the real one.

---

### PHASE 0 — COMMITTEE DECLARATION

Open with:

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter: [path to .roles/ file used, or "Signal defaults — no charter found: [list fallback roles]"]
Participants:
- [Role Name 1] — [charter-defined orientation in one phrase]
- [Role Name 2] — [charter-defined orientation in one phrase]
[one line per loaded role]
```

Read `.roles/` for the charter matching this committee type. Load every named role. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state the fallback explicitly.

---

### PHASE 1 — SWITCHING-COST INVESTIGATION

Before any participant speaks, investigate what this agenda item displaces. The framing question is: **what does the status quo protect?** Label this block `INVESTIGATION-ATTEMPT-1`.

Each finding receives a named entry label. Named labels are the citation anchors for the entire simulation — downstream CITE: and RESPONDS-TO: fields reference findings by label name.

```
INVESTIGATION-ATTEMPT-1:

INERTIA-FINDING-A: [The specific workflow, tool, or process currently in production that this proposal displaces — name it precisely, not generically]
INERTIA-FINDING-B: [The named integration surface at risk — specific systems, APIs, contracts, or downstream consumers that would be broken or renegotiated]
INERTIA-FINDING-C: [The team whose cognitive habits would break — name the team and the specific decision-making habit they rely on today]
INERTIA-FINDING-D: [The non-obvious switching cost — the cost the proposal author almost certainly did not account for; name it with enough specificity that the author would say "I missed that"]

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious switching cost the proposal author is unlikely to have anticipated?
  Answer: [YES — INERTIA-FINDING-D is non-obvious because [specific reason the proposal author would not have written this finding themselves] / NO — insufficient: [why INERTIA-FINDING-D does not clear the non-obvious threshold]]
```

**PHASE-1 GATE LOOP (C-29 — intra-phase retry):**

The gate runs within Phase 1. Phase 2 is reached unconditionally once the gate answers YES. The gate does not control whether Phase 2 exists — it controls when Phase 1 releases.

```
GATE-1 Answer: YES  →  Phase 1 releases. Fill Phase 2.
GATE-1 Answer: NO   →  Output INVESTIGATION-ATTEMPT-2 (below), same structure,
                        all four INERTIA-FINDING-* labels rewritten with a different
                        angle. Output GATE-2. Re-evaluate.
                        Repeat as INVESTIGATION-ATTEMPT-N / GATE-N until a YES answer
                        appears. Each attempt carries a new sequential label.
                        Phase 2 fills unconditionally as soon as any GATE-N is YES.
```

Each rewrite attempt must produce a new labeled block:

```
INVESTIGATION-ATTEMPT-2:   [if GATE-1 is NO]

INERTIA-FINDING-A: [rewritten — different angle from Attempt 1]
INERTIA-FINDING-B: [rewritten]
INERTIA-FINDING-C: [rewritten]
INERTIA-FINDING-D: [rewritten — different non-obvious cost candidate]

GATE-2:
  Question: Does INERTIA-FINDING-D reveal a non-obvious switching cost the proposal author is unlikely to have anticipated?
  Answer: [YES / NO — with basis]
```

A rewrite that does not produce a new labeled `INVESTIGATION-ATTEMPT-N:` block with fresh INERTIA-FINDING-* labels fails C-22 and C-24 regardless of whether C-16's gate is described.

The final passing gate's `INERTIA-FINDING-A` through `INERTIA-FINDING-D` are the **active committee record** — these labels are the citation targets for all subsequent CITE: and RESPONDS-TO: fields.

---

### PHASE 2 — TIER SORT

Sort all loaded participants into three tiers using charter-defined orientations and the active INERTIA-FINDING findings.

```
TIER SORT:
Tier 1 — CHALLENGERS: [roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems — speak first; grounded in INERTIA-FINDING-* labels]
Tier 2 — CONDITIONALS: [roles that hold approval pending specific named conditions]
Tier 3 — ADVOCATES: [roles whose orientation aligns with the proposal's stated goals]
Tie-break: higher institutional veto authority speaks first within tier
```

**SORT-CHECK gate (C-25):**

```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES — [role] is mis-sorted; reassigning to Tier [X] because [specific reason given this agenda item and active INERTIA-FINDING findings]; corrected TIER SORT block follows / NO — valid sort, Phase 3 proceeds]
```

If Result YES: re-output corrected TIER SORT block, then new SORT-CHECK block. Repeat until Result NO. Phase 3 proceeds unconditionally once Result is NO.

---

### PHASE 3 — PARTICIPANT VOICES

Write one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3.

**Voice format for all tiers:**

```
### [Role Name] — Tier [1 / 2 / 3]
STANCE: [BLOCK / CONDITION / APPROVE]
[2–4 sentences from documented role orientation, responding to the active INERTIA-FINDING labels where relevant. STANCE: is a standalone labeled declaration — prose follows and must not soften, qualify, or contradict the declared stance. Tier 1: lead with the specific concern, grounding in a named INERTIA-FINDING label. Tier 2: name the specific condition for approval. Tier 3: complete CITE: and RESPONDS-TO: before any endorsement prose.]
```

**Additional required fields for Tier 3 participants:**

```
CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding that supports this endorsement — the named label is the first element after CITE:, followed by a dash and then content; no prose before the label]
RESPONDS-TO: "INERTIA-FINDING-[A or B]: [quote or close paraphrase of the finding's specific content as a concern, or '[Role Name]'s concern that [concern text]']" — [one sentence: how this endorsement addresses that named concern]
```

Enforcement:
- `CITE:` label rule (C-20/C-27): `INERTIA-FINDING-*` must be the first element after `CITE:`. A citation that writes content without naming the finding label fails C-27 even if the content is correct.
- `RESPONDS-TO:` label rule (C-21): the quoted string must name `INERTIA-FINDING-A` or `INERTIA-FINDING-B` (or a named challenger concern from Phase 3) and paraphrase its content. "Inertia concerns have been acknowledged" fails.
- At least one participant must declare `STANCE: CONDITION` or `STANCE: BLOCK` (C-05/C-18). All-APPROVE is a sort error — reopen Phase 2.

---

### PHASE 4 — TALLY

After all Phase 3 voices, before Phase 5:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

---

### PHASE 5 — MINUTES

#### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved):
  Owner: [named role responsible for resolving the blocking finding]
  Resolves: [INERTIA-FINDING-[A/B/C/D] — the named finding this path addresses]
  Trigger: [concrete deliverable or event that causes committee re-review — traceable to the Resolves label]
```

Both `Owner:` and `Trigger:` are required (C-23). `Resolves:` names the INERTIA-FINDING entry being satisfied, grounding the trigger in a specific committee record item.

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. Vague items fail.

#### DISSENTING OPINIONS

For each dissent: dissenting role, substance of objection (citing the relevant INERTIA-FINDING-* label if applicable), resolution path (concrete condition + named authority who confirms when condition is met).

If no dissent: `"No dissent — [one sentence: why consensus emerged]"`

---

## V-03 — Single-axis: Phrasing Register — Imperative Micro-Instructions with Loop Constructs

**Variation axis**: Phrasing register — each phase instruction is written as a tight imperative micro-command (`PRINT:`, `LABEL:`, `LOOP UNTIL:`, `GATE:`, `FILL:`) rather than as descriptive prose directives. Instructions are concise, command-style, and execution-ordered. The simulation reads as a program the model executes, not a guide the model follows.

**Hypothesis**: Prior rounds used prose instructions ("If GATE-1 is NO, rewrite the investigation and re-gate"). Prose instructions can be interpreted as descriptions of intended behavior rather than mandatory execution steps. Imperative micro-commands reduce interpretive latitude: `LOOP UNTIL: GATE-N: YES` does not admit the interpretation "if it fails once, stop." The loop construct makes Phase 1's gate structure visually and syntactically distinct from a conditional halt. For C-29, this is material: "do not proceed to Phase 2 until gate passes" reads as a conditional; `LOOP UNTIL: gate passes → CONTINUE TO PHASE 2` reads as a loop with an unconditional continuation. The register change also compacts the prompt, reducing attention dilution on lower-priority prose.

---

You are executing `org:committee`. Run each phase in sequence. Phase outputs are commitments.

---

**PHASE 0 — DECLARE**

PRINT:
```
Committee: [TYPE] — [agenda item]
Charter: [.roles/ path or "Signal defaults: [roles]"]
Participants:
  [Role] — [orientation]
  [repeat per participant]
```

LOAD: Read `.roles/` for this committee type. If absent: load PM, Architect, Inertia-Advocate; PRINT charter source as "Signal defaults — no charter found."

---

**PHASE 1 — INVESTIGATE**

LABEL: `INVESTIGATION-ATTEMPT-1`

FILL:
```
INERTIA-FINDING-A: [specific workflow displaced — name it]
INERTIA-FINDING-B: [integration surface at risk — named systems, APIs, contracts]
INERTIA-FINDING-C: [team whose habits break — specific team, specific habit]
INERTIA-FINDING-D: [non-obvious cost — the one the proposal author missed]
```

GATE:
```
GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [one sentence]
```

LOOP UNTIL: `GATE-N Answer: YES`

```
IF GATE-N Answer: YES
  → EXIT LOOP
  → CONTINUE TO PHASE 2 (unconditional — phase 2 always executes)

IF GATE-N Answer: NO
  → INCREMENT N
  → LABEL: INVESTIGATION-ATTEMPT-N
  → FILL: INERTIA-FINDING-A through D (rewritten, different angle)
  → GATE: GATE-N (re-evaluate with same question)
  → REPEAT
```

RULE: Each iteration produces a new labeled `INVESTIGATION-ATTEMPT-N` block. An internal rewrite without a new sequential label does not satisfy the loop — the label must appear in output (C-24). The loop runs within Phase 1. Phase 2 is not conditional on gate passage; it is unconditional on loop exit.

ACTIVE RECORD: The INERTIA-FINDING-A through D from the last passing attempt are the committee record's citation anchors.

---

**PHASE 2 — SORT**

FILL:
```
TIER SORT:
  Tier 1 — CHALLENGERS: [roles — speak first]
  Tier 2 — CONDITIONALS: [roles — speak second]
  Tier 3 — ADVOCATES: [roles — speak last]
  Tie-break: higher veto authority first within tier
```

GATE:
```
SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES / NO]
```

LOOP UNTIL: `SORT-CHECK Result: NO`

```
IF SORT-CHECK Result: NO → EXIT LOOP → CONTINUE TO PHASE 3 (unconditional)
IF SORT-CHECK Result: YES
  → REASSIGN: [role] to Tier [X] because [reason]
  → RE-FILL TIER SORT
  → RE-GATE SORT-CHECK
  → REPEAT
```

RULE: SORT-CHECK must appear as a discrete labeled gate with `Test:` and `Result:` fields. Correct tier ordering without a SORT-CHECK block fails C-25.

---

**PHASE 3 — VOICES**

EXECUTE: Tier 1 → Tier 2 → Tier 3

FOR EACH PARTICIPANT:

```
### [Role Name] — Tier [1 / 2 / 3]
STANCE: [BLOCK / CONDITION / APPROVE]
[2–4 sentences from role orientation. STANCE: is a standalone labeled declaration before prose. Prose must not contradict it.]
```

FOR TIER 3 ONLY — append after prose:

```
CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement — label is first element after CITE:, no prose before it]
RESPONDS-TO: "[named concern — 'INERTIA-FINDING-[A/B]: [paraphrase]' or '[Role]'s concern that [text]']" — [one sentence addressing it]
```

VALIDATE:
- `CITE:` label is the first token after `CITE:` — prose before label fails C-20/C-27
- `RESPONDS-TO:` quoted string names a specific finding or concern by label or role — generic fails C-21
- At least one STANCE: CONDITION or STANCE: BLOCK must appear — all-APPROVE triggers Phase 2 re-sort

---

**PHASE 4 — TALLY**

PRINT (after last voice, before Phase 5):
```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

---

**PHASE 5 — MINUTES**

PRINT:

```
### DECISIONS
Verdict: [verdict]
Conditions: [named, or "none"]
Re-entry path (if not approved):
  Owner: [named role]
  Trigger: [concrete deliverable or event — not vague]

### ACTION ITEMS
[Owner Role] — [specific action] — [deadline]

### DISSENTING OPINIONS
[Role] — [objection] — [resolution path] — [authority] — [concrete trigger]
[or: "No dissent — [reason]"]
```

VALIDATE:
- `Owner:` and `Trigger:` both required in re-entry path (C-23)
- Action items: named owner + specific deliverable + deadline — "investigate further" fails
- Dissents include resolution path with concrete trigger, not just objection statement

---

## V-04 — Combined: Lifecycle Emphasis + C-29 — Phase Architecture with Intra-Phase Loop Diagrams

**Variation axes**: Lifecycle emphasis (phase-first architecture with explicit phase-exit conditions) + C-29 (intra-phase gate loops visualized as explicit flow structures). V-04 makes C-29 the primary design constraint: each gate is expressed as an ASCII loop diagram showing the retry structure contained within its phase, with Phase 2 appearing as an unconditional successor at the bottom of the Phase 1 diagram. The phase architecture gives each gate a named home; the loop diagram makes the intra-phase scope visually unambiguous.

**Hypothesis**: C-29's failure mode in R8 V-02 was architectural: the prompt wrote the gate as an inter-phase condition, leaving Phase 2 absent. A loop diagram that shows Phase 2 at the bottom of the Phase 1 section — as the exit target of the loop — makes this architecture impossible: Phase 2 is present in the diagram before any gate evaluation, so the gate cannot eliminate Phase 2 from the output. The diagram form also makes the retry structure more recognizable as a loop (cyclic arrow back to investigation rewrite) versus a conditional (one-way branch to halt). Combined with explicit phase-exit conditions ("Phase N commits when X; proceed to Phase N+1"), the prompt encodes the unconditional pipeline commitment at both the diagram level and the prose instruction level.

---

You are running `org:committee` — a pre-meeting simulation. Execute in five explicitly numbered, named phases. Each phase produces a committed output before the next phase begins.

---

### PHASE 0 — COMMITTEE DECLARATION

```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Charter: [path to .roles/ file, or "Signal defaults — no charter found: [roles]"]
Participants:
  [Role Name] — [charter-defined orientation in one phrase]
  [one line per loaded role]
```

Read `.roles/` for this committee type. Load every named role. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state the fallback.

**Phase 0 commits: committee type, charter source, participant roster. → Phase 1**

---

### PHASE 1 — INVESTIGATION

**Phase 1 contains an intra-phase gate loop. The loop runs entirely within Phase 1. Phase 2 is always reached — the loop controls when Phase 1 releases, not whether Phase 2 runs.**

Phase 1 gate loop structure:

```
┌─────────────────────────────────────────────────┐
│  PHASE 1: INVESTIGATION                         │
│                                                 │
│  INVESTIGATION-ATTEMPT-N:                       │
│    INERTIA-FINDING-A: [workflow displaced]      │
│    INERTIA-FINDING-B: [integration at risk]     │
│    INERTIA-FINDING-C: [habit disruption]        │
│    INERTIA-FINDING-D: [non-obvious cost]        │
│                                                 │
│  GATE-N:                                        │
│    Question: Does INERTIA-FINDING-D reveal a    │
│              non-obvious cost the author        │
│              would not have anticipated?        │
│    Answer: YES / NO                             │
│    Basis: [one sentence]                        │
│                                                 │
│  ┌─ Answer: NO ─────────────────────────────┐   │
│  │  INCREMENT N                              │   │
│  │  Label next attempt: INVESTIGATION-       │   │
│  │    ATTEMPT-N+1                            │   │
│  │  Rewrite all four INERTIA-FINDING-*       │   │
│  │    labels (different angle)               │   │
│  └──────────────────────────────────────────┘   │
│            ↑                                    │
│            └──── loop back to GATE-N ───────────┤
│                                                 │
│  Answer: YES → EXIT LOOP                        │
└─────────────────────────────────────────────────┘
                        │
                        ↓ (unconditional)
┌─────────────────────────────────────────────────┐
│  PHASE 2: TIER SORT                             │
└─────────────────────────────────────────────────┘
```

Execute:

```
INVESTIGATION-ATTEMPT-1:

INERTIA-FINDING-A: [specific workflow displaced — name it, not generic]
INERTIA-FINDING-B: [named integration surface at risk — systems, APIs, contracts]
INERTIA-FINDING-C: [specific team + specific cognitive habit that breaks]
INERTIA-FINDING-D: [the non-obvious cost — specific enough the author would say "I missed that"]

GATE-1:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [specific reason why (YES) or why insufficient (NO)]
```

If GATE-1 Answer: NO — output the next attempt within Phase 1:

```
INVESTIGATION-ATTEMPT-2:   [sequential label required — C-24]

INERTIA-FINDING-A: [rewritten — different status-quo protection angle]
INERTIA-FINDING-B: [rewritten]
INERTIA-FINDING-C: [rewritten]
INERTIA-FINDING-D: [rewritten — different non-obvious cost candidate]

GATE-2:
  Question: Does INERTIA-FINDING-D reveal a non-obvious cost the proposal author would not have anticipated?
  Answer: [YES / NO]
  Basis: [specific reason]
```

Continue (`INVESTIGATION-ATTEMPT-3` / `GATE-3`, etc.) until a gate answers YES. The sequential label must increment with each new attempt; an internal rewrite without a new labeled block does not satisfy C-22 and C-24.

**Active record**: The INERTIA-FINDING-A through D from the passing attempt are the committee record's named citation anchors.

**Phase 1 commits when GATE-N Answer: YES. → Phase 2 (unconditional)**

---

### PHASE 2 — TIER SORT

Phase 2 gate loop structure:

```
┌─────────────────────────────────────────────────┐
│  PHASE 2: TIER SORT                             │
│                                                 │
│  TIER SORT:                                     │
│    Tier 1 — CHALLENGERS: [...]                  │
│    Tier 2 — CONDITIONALS: [...]                 │
│    Tier 3 — ADVOCATES: [...]                    │
│                                                 │
│  SORT-CHECK:                                    │
│    Test: Tier 1 and Tier 2 both empty?          │
│    Result: YES / NO                             │
│                                                 │
│  ┌─ Result: YES ────────────────────────────┐   │
│  │  Reassign: [role] to Tier [X]            │   │
│  │  Reason: [specific reason]               │   │
│  │  Re-output corrected TIER SORT block     │   │
│  └──────────────────────────────────────────┘   │
│            ↑                                    │
│            └──── loop back to SORT-CHECK ───────┤
│                                                 │
│  Result: NO → EXIT LOOP                         │
└─────────────────────────────────────────────────┘
                        │
                        ↓ (unconditional)
┌─────────────────────────────────────────────────┐
│  PHASE 3: PARTICIPANT VOICES                    │
└─────────────────────────────────────────────────┘
```

Execute:

```
TIER SORT:
  Tier 1 — CHALLENGERS: [roles whose charter orientation interrogates feasibility, risk, or disruption — speak first]
  Tier 2 — CONDITIONALS: [roles that hold approval pending named conditions]
  Tier 3 — ADVOCATES: [roles aligned with the proposal's stated goals]
  Tie-break: higher institutional veto authority first within tier

SORT-CHECK:
  Test: Tier 1 and Tier 2 both empty?
  Result: [YES / NO — with action]
```

If Result YES: re-output corrected TIER SORT, new SORT-CHECK. Repeat until Result NO.

**Phase 2 commits when SORT-CHECK Result: NO. → Phase 3 (unconditional)**

---

### PHASE 3 — PARTICIPANT VOICES

Write one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3.

```
### [Role Name] — Tier [1 / 2 / 3]
STANCE: [BLOCK / CONDITION / APPROVE]
[2–4 sentences from documented role orientation. STANCE: is a standalone labeled declaration — prose follows and must not soften or contradict it. Tier 1: ground concern in a named INERTIA-FINDING label. Tier 2: name the specific condition. Tier 3: CITE: and RESPONDS-TO: required before endorsement prose.]
CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding — label is first element after CITE:]
RESPONDS-TO: "[named concern — 'INERTIA-FINDING-[A/B]: [paraphrase]' or '[Role]'s concern that [text]']" — [one sentence: how this endorsement addresses that concern]
```

`CITE:` and `RESPONDS-TO:` are required for every Tier 3 participant. At least one participant must declare STANCE: CONDITION or STANCE: BLOCK — all-APPROVE is a Phase 2 sort error; reopen Phase 2.

**Phase 3 commits when all voices are written. → Phase 4 (unconditional)**

---

### PHASE 4 — TALLY

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

**Phase 4 commits. → Phase 5 (unconditional)**

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

Both `Owner:` and `Trigger:` required (C-23).

#### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Named owner, specific deliverable, deadline. "Investigate further" fails.

#### DISSENTING OPINIONS

For each dissent: dissenting role, substance (citing INERTIA-FINDING label if applicable), resolution path (concrete condition + named authority confirms when condition is met).

If no dissent: `"No dissent — [one sentence: why consensus emerged]"`

**Phase 5 commits the simulation record.**

---

## V-05 — Combined: Full Synthesis — Skeleton + Named Labels + Loop Architecture + All Criteria

**Variation axes**: Output format (skeleton pre-declaration — C-28) + inertia framing (INERTIA-FINDING named labels — C-27) + lifecycle emphasis + C-29 (intra-phase loops) + phrasing register (imperative fill commands). This is the golden synthesis for R9: all structural slot labels pre-declared as an upfront skeleton, all INERTIA-FINDING-* labels used as primary citation anchors, all phase gates implemented as explicitly described intra-phase loops, and all fill instructions in imperative register. The skeleton is the enforcement mechanism: every criterion has a slot; every slot appears unconditionally; loop and gate behavior is described within each slot's instructions rather than as inter-phase conditionals.

**Hypothesis**: R8 V-01 scored 129/130 — the only gap was C-28 PARTIAL (labels present but not pre-declared). V-05 corrects that by making skeleton pre-declaration the opening act. The skeleton additionally makes C-29 structurally enforced: Phase 2's skeleton section appears on the page before any Phase 1 gate evaluation begins, so the gate loop cannot make Phase 2 absent. INERTIA-FINDING-* labels in the skeleton give C-27 a structural anchor from slot-declaration forward. Imperative register within each slot's instructions reduces behavioral interpretation latitude. This variation targets 132/132.

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

[Continue as INVESTIGATION-ATTEMPT-N / GATE-N until Answer: YES. Sequential label increments each time. Phase 2 fills once any GATE-N Answer: YES.]

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

[Result YES → re-output corrected TIER SORT block + new SORT-CHECK block; repeat until NO]

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
[one row per item]

### DISSENTING OPINIONS

___
[one entry per dissent, or "No dissent — [reason]"]

=== END SKELETON ===
```

---

### STEP 2 — FILL THE SKELETON

Fill each `___` top to bottom. Rules:

---

**PHASE 0 — fill rules:**

- Read `.roles/` for the charter matching this committee type. Load every named role with charter-defined orientation.
- If no charter file exists: Charter Source = `"Signal defaults — no charter found"`; Participants = PM, Architect, Inertia-Advocate.
- Committee Type must be declared: ROB, shiproom, arch-board, or the user-specified type.

---

**PHASE 1 — fill rules:**

**INERTIA-FINDING labels**: Each finding receives its named label (`INERTIA-FINDING-A`, `INERTIA-FINDING-B`, `INERTIA-FINDING-C`, `INERTIA-FINDING-D`). The label is the primary identifier — not an annotation on a letter. These labels are the citation anchors for all downstream CITE: and RESPONDS-TO: fields.

Fill guidance:
- `INERTIA-FINDING-A`: Name the specific workflow, tool, or process currently in production that this agenda item displaces. Precision required — "existing workflow" fails.
- `INERTIA-FINDING-B`: Name the integration surface at risk — specific systems, APIs, contracts, or downstream consumers that would break or require renegotiation.
- `INERTIA-FINDING-C`: Name the team whose cognitive habits would break, and the specific decision-making habit they rely on today.
- `INERTIA-FINDING-D`: Name the non-obvious switching cost — the cost the proposal author almost certainly did not account for, specific enough that the author would say "I missed that."

**GATE-1 fill rule — intra-phase loop (C-29):**

```
GATE-1 Answer: YES
  → Phase 1 loop exits.
  → Phase 2 fills unconditionally. (Phase 2 is already in the skeleton — it is not conditional.)

GATE-1 Answer: NO
  → Phase 1 loop continues within Phase 1.
  → Fill INVESTIGATION-ATTEMPT-2 block (already in skeleton).
  → Fill GATE-2. Re-evaluate with same question.
  → If GATE-2 Answer: YES → Phase 1 loop exits → Phase 2 fills.
  → If GATE-2 Answer: NO → extend skeleton with INVESTIGATION-ATTEMPT-3 / GATE-3.
  → Repeat. Sequential label increments each attempt (N, N+1, N+2...).
  → Phase 2 fills as soon as any GATE-N Answer: YES appears.
  → Phase 2 is always reached. The loop controls when, not whether.
```

Each new attempt must produce a new labeled block in output. A claimed internal rewrite without a visible `INVESTIGATION-ATTEMPT-N+1:` block fails C-22 and C-24.

**Active INERTIA-FINDING record**: The four INERTIA-FINDING-* labels from the passing attempt are the committee record's citation anchors for the rest of the simulation.

---

**PHASE 2 — fill rules:**

Assign all loaded participants to tiers based on charter-defined orientations and active INERTIA-FINDING findings.

- Tier 1 (CHALLENGERS): roles whose charter orientation interrogates feasibility, risk, or disruption to existing systems. Speak before all others.
- Tier 2 (CONDITIONALS): roles that hold approval pending specific named conditions.
- Tier 3 (ADVOCATES): roles aligned with the proposal's stated goals. Speak last.
- Tie-break: higher institutional veto authority speaks first within tier.

**SORT-CHECK fill rule:**

```
Test: [fixed — "Tier 1 and Tier 2 both empty?"]
Result: YES or NO, followed by the required action:
  YES: name the mis-sorted role, the target tier, and the reason given this agenda item and active INERTIA-FINDING findings. Re-output corrected TIER SORT block. Fill new SORT-CHECK block.
  NO: valid sort — Phase 3 fills.
```

SORT-CHECK Result NO is the Phase 2 exit condition. Phase 3 fills unconditionally once Result is NO.

---

**PHASE 3 — fill rules:**

Fill one block per participant in strict tier order: Tier 1 → Tier 2 → Tier 3.

**STANCE fill rule (C-15)**: Fill `STANCE: [BLOCK / CONDITION / APPROVE]` as a standalone labeled line before any prose. The prose that follows must not soften, qualify, or contradict the declared stance.

**Tier 1 voice fill guidance**: Lead with the specific concern. Ground in a named INERTIA-FINDING label where relevant.

**Tier 2 voice fill guidance**: Name the specific condition for approval. State it precisely — "address concerns" is not a specific condition.

**Tier 3 voice fill guidance**: Fill `CITE:` and `RESPONDS-TO:` before writing endorsement prose.

**CITE fill rule (C-20/C-27)**:

Format: `CITE: INERTIA-FINDING-[A/B/C/D] — [content of that finding supporting this endorsement]`

The named label (`INERTIA-FINDING-A`, `INERTIA-FINDING-B`, `INERTIA-FINDING-C`, or `INERTIA-FINDING-D`) must be the first element after `CITE:`, followed by ` — ` and then the content. Prose before the label fails C-20. A citation without the named label (only the content) fails C-27.

**RESPONDS-TO fill rule (C-21)**:

Format: `RESPONDS-TO: "[named concern]" — [one sentence addressing it]`

The quoted string must name a specific finding or concern:
- Acceptable: `"INERTIA-FINDING-A: [paraphrase of finding content]"`
- Acceptable: `"[Role Name]'s concern that [specific concern text]"`
- Fails: `"Inertia concerns have been acknowledged"` (generic — no name, no content)
- Fails: `"The challenger raised valid points"` (no specific attribution)

**Challenge requirement (C-05/C-18)**: At least one participant must declare `STANCE: CONDITION` or `STANCE: BLOCK`. An all-APPROVE fill means Phase 2 sort is invalid — reopen Phase 2, revise tier assignments, re-run SORT-CHECK.

---

**PHASE 4 — fill rules:**

Fill TALLY after the last Phase 3 voice block and before Phase 5. Count each STANCE: declaration from Phase 3 — one tally entry per participant, categorized by their declared STANCE. Do not embed in prose.

OUTCOME derives from TALLY:
- All APPROVE → APPROVED
- Any CONDITION, no BLOCK → APPROVED WITH CONDITIONS
- Any BLOCK → BLOCKED or DEFERRED (per committee type convention)

---

**PHASE 5 — fill rules:**

**DECISIONS fill rule:**
- Verdict: matches OUTCOME from Phase 4.
- Conditions: name each condition explicitly — "address feedback" is not a named condition.
- Re-entry path (required when verdict is not APPROVED):
  - `Owner:` — the named role responsible for satisfying the blocking condition. Not a team; a specific role from the Phase 0 participant roster.
  - `Trigger:` — the concrete deliverable, evidence artifact, or event that causes the committee to re-review. "Sufficient progress" fails. "Prototype demonstrating [specific behavior] reviewed by [specific authority]" passes.
  - Both fields required (C-23).

**ACTION ITEMS fill rule:**

Format: `[Owner Role] — [specific action] — [deadline]`

All three parts required per item. "Investigate" is not a specific action — name the investigation question, the output artifact, and who receives it.

**DISSENTING OPINIONS fill rule:**

For each participant whose STANCE was CONDITION or BLOCK: capture their dissent substance (the specific objection, citing INERTIA-FINDING-* label where applicable), and their resolution path (the concrete condition they require + the named authority who will confirm when the condition is met).

If no dissent: `"No dissent — [one sentence explaining why all participants reached consensus]"`
