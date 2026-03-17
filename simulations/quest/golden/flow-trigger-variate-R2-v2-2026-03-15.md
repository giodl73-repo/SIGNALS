# Flow-Trigger Skill — Round 2 Variations (Rubric v2)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v2 (C-01 through C-13)
**Date**: 2026-03-15

---

## Variation Design Notes

Rubric v2 extracts 4 new aspirational criteria from analysis of R2/v1 variations. These criteria
were implicit or partially expressed in the earlier prompts; v2 makes them explicit and scorable.
The Round 2 / v2 variations are designed to drive each new criterion structurally, not narratively.

New criteria and their root failure modes:

| Criterion | Root Failure Mode | Previous Coverage |
|-----------|------------------|------------------|
| C-10 — Anomaly questions pre-opened | Post-hoc anomaly assembly | R1/V-01 partially addressed; R2/V-01 declared OPEN slots but didn't enforce pre-enumeration placement |
| C-11 — Cascade completeness | Cascade annotation without continuation (dangling side-effect note) | R2/V-04 cascade tree required rows; V-03 had cascade rule but not enforced as row-spawn |
| C-12 — Self-annotating non-conformance | Silent non-conformance (defects invisible without expert reviewer) | R2/V-05 introduced [NC: value] tags; others relied on narrative |
| C-13 — Evidence-anchored anomaly verdicts | Verdict-without-evidence (bare assertion) | R2/V-02/V-04/V-05 cited evidence but did not structurally block bare verdicts |

**Variation map**:

| Variation | Axis | Primary Criteria | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | Role sequence | C-10, C-13 | A two-phase output where Phase 0 MUST declare all three anomaly slots as OPEN before the Phase 1 enumeration begins makes post-hoc anomaly assembly structurally impossible — the model cannot write enumeration output before writing the open slots |
| V-02 | Output format | C-11, C-09 | A trigger entry format with a mandatory "Spawns row N+1?" decision cell — where YES requires the immediately following numbered entry to be the spawned trigger — makes cascade completeness a table constraint rather than a narrative instruction |
| V-03 | Phrasing register | C-12, C-13 | Formal EVIDENCE / VERDICT sub-structure for every anomaly verdict, where the EVIDENCE sub-section must name specific rows, combined with a tag vocabulary that must be applied inline, drives both self-annotation and evidence-anchoring at the sentence level |
| V-04 | Role sequence + output format | C-10, C-11 | Combining pre-opened anomaly slots (V-01 structure) with cascade-spawning rows (V-02 structure) creates two reinforcing mechanical constraints: anomaly slots are live during enumeration AND cascade fires are spawned as rows |
| V-05 | Phrasing register + inertia framing | C-12, C-13 | Naming all four C-10 through C-13 failure modes explicitly and pairing each with a formal SHALL requirement and its inline tag creates the strongest structural motivation for self-annotation and evidence-anchoring — the failure modes explain *why* each tag and each evidence block exists |

---

## V-01 — Role Sequence: Anomaly Slots Declared OPEN Before Enumeration

**Variation axis**: Role sequence
**Hypothesis**: R1/V-01 opened anomaly questions before enumeration but placed them inside Role A
alongside the candidate pre-scan — so the model could, in principle, write the candidate scan
first and treat the OPEN declarations as a warm-up header. V-01/v2 hardens this by making the
anomaly slot declarations a separate, named section (SECTION 0) that must appear in the output
before Section 1 (candidate scan) can begin. The output structure is: anomaly slots OPEN →
candidate scan → trigger enumeration → anomaly slot CLOSE. A model that jumps to enumeration
before writing SECTION 0 produces a structurally incomplete document; a model that writes
SECTION 0 last (post-hoc) produces a document that contradicts its own section numbering.
This structural sequencing makes C-10 a mechanical precondition, not an instruction to follow.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report following
the four-section output structure below. Sections are numbered 0 through 3. Section 0 must
appear in your output before Section 1. Section 1 must appear before Section 2. Section 2 must
appear before Section 3. Completing sections out of order is a structural protocol violation.

---

#### SECTION 0 — OPEN ANOMALY INVESTIGATION REGISTER

Before examining which triggers fire, declare all three anomaly investigations as OPEN.

Do not evaluate whether any anomaly exists yet. Do not scan the trigger registry yet.
The purpose of this section is to lock the investigation questions while the denominator is
still undeclared, so that no anomaly class can be silently bypassed later.

```
INVESTIGATION 1 — TRIGGER STORM
Status: OPEN
Question: Does this change event cause more than 3 distinct trigger executions, or cause any
  single trigger to execute more than once within the same transaction or polling cycle?
Evidence required to close: total distinct trigger names from Section 2; re-entry check
  result for each side-effect field write from Section 2.
Verdict placeholder: [ will be filled in Section 3 ]

INVESTIGATION 2 — MISSING TRIGGERS
Status: OPEN
Question: Is any automation that is expected to fire for this change event absent from the
  firing set?
Evidence required to close: candidate list (declared in Section 1); per-candidate resolution
  (FIRED / CONFIRMED ABSENT / FLAGGED GAP) from Section 2.
Verdict placeholder: [ will be filled in Section 3 ]

INVESTIGATION 3 — CIRCULAR TRIGGERS
Status: OPEN
Question: Does any trigger write a field that directly or transitively causes one of the
  already-fired triggers to fire again, creating a cycle?
Evidence required to close: directed edge set constructed from Section 2 side-effect writes;
  graph property determination (DAG / CYCLIC).
Verdict placeholder: [ will be filled in Section 3 ]
```

All three investigations remain OPEN until Section 3. Closing any investigation before
Section 3 is a structural protocol violation.

---

#### SECTION 1 — CANDIDATE PRE-SCAN

List every automation that could fire for this change event based on entity, field, and trigger
type alone. Do not evaluate conditions. Do not determine which triggers actually fire.

| Candidate ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | | |

PA Flow Type must be one of: `Automated – Dataverse` / `Automated – SharePoint` /
`Automated – HTTP` / `Instant` / `Scheduled`.

Denominator count: N. This count governs Section 2 reconciliation.

---

#### SECTION 2 — TRIGGER ENUMERATION

List every trigger that fires, in order. Sync triggers before async. Number each entry
continuously. For each trigger that fires and produces a side-effect field write with
downstream automation potential, the immediately following numbered entry must be the
downstream trigger (cascade rule — see "Spawns?" field below).

For each firing trigger:

**[#] [Trigger Name]**
- **Candidate ref**: C-NN from Section 1, or `[NOT IN CANDIDATES: reason]`
- **PA flow type**: exact term from Section 1 vocabulary (non-conforming: mark `[VOCAB FAIL: actual text]`)
- **Execution tier**: `Sync (blocks transaction)` or `Async (~N min [standard|premium] tier)`
- **Condition**: `No condition` or: `Evaluates [condition text]. Taken: [branch] because [reason]. Skipped: [branch] because [reason].`
- **Reads**: `{Entity}.{Field}` per field consumed (non-conforming descriptions: mark `[VOCAB FAIL: actual text]`)
- **Produces**: opens with `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to` + connector + target + resulting state (non-conforming: mark `[VOCAB FAIL: actual text]`)
- **Writes (side effects)**: `{Entity}.{Field} = {value}` per field written, or `None`
- **Spawns?**: `NO` if Writes = None or no downstream automation applies; `YES → entry #[N+1]: [trigger name]` if a side-effect write causes a downstream trigger — the downstream trigger MUST be entry #[N+1]

---

#### SECTION 3 — CLOSE ANOMALY INVESTIGATIONS

Close each investigation opened in Section 0 by replacing its verdict placeholder with findings
grounded in Section 2 evidence.

Each verdict block must contain two sub-sections:

**EVIDENCE** — cite specific items from Section 2 (entry numbers, trigger names, field writes,
row counts). A verdict block with no EVIDENCE sub-section is structurally incomplete and must be
marked `[BARE ASSERTION — evidence sub-section missing]`.

**VERDICT** — a single verdict sentence that begins with the word `CLEARED` or the name of the
detected anomaly. The verdict must follow from the cited evidence.

---

**INVESTIGATION 1 — TRIGGER STORM**
Status: ~~OPEN~~ → CLOSED

EVIDENCE:
- [ cite total firing count from Section 2 by entry number and name ]
- [ cite re-entry check results: for each Writes field in Section 2, state whether it matches
    any Section 1 candidate's trigger condition ]

VERDICT: `CLEARED (count = N, no re-entry)` or `STORM DETECTED (count = N; group: [names]; re-entry: [path])`

---

**INVESTIGATION 2 — MISSING TRIGGERS**
Status: ~~OPEN~~ → CLOSED

EVIDENCE:
- [ list each Section 1 candidate with its resolution: FIRED / CONFIRMED ABSENT (reason) / FLAGGED GAP (reason) ]

VERDICT: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or
`MISSING TRIGGER: [name — gap cause — risk level]`

---

**INVESTIGATION 3 — CIRCULAR TRIGGERS**
Status: ~~OPEN~~ → CLOSED

EVIDENCE:
- [ list every directed edge: Trigger A writes {Entity.Field} → fires Trigger B ]
- [ state graph property: DAG / CYCLIC ]

VERDICT: `CLEARED (DAG confirmed; edge set: {listed})` or `CIRCULAR TRIGGER: [full cycle path]`

---

Now receive the scenario and trigger registry. Begin with Section 0. Do not write Section 1
before Section 0 is complete.

---

## V-02 — Output Format: Cascade-Spawning Row Protocol

**Variation axis**: Output format
**Hypothesis**: Every prior variation treated cascade completeness as a narrative instruction:
"if a side-effect write causes another trigger to fire, trace it." Instructions can be
selectively applied; the model decides when a downstream fire is worth tracing. V-02 eliminates
this discretion by making cascade continuation a mandatory field in the trigger entry format.
Every entry — without exception — must answer "Spawns row N+1?" with YES or NO and a reason.
A YES answer creates an obligation: the next numbered entry MUST be the spawned trigger, not
the next independent trigger in sequence. The model cannot skip a cascade without writing a
visible NO that a reviewer can check. This structural design drives C-11 as a table constraint
and produces C-09 (trigger map) as a natural output of the numbered entry sequence.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report for the
change event below. Follow the five-section format exactly.

---

#### SECTION 1 — SCOPE PIN

State the change event:
> **Scope**: `{Entity}` — `{Field}` changed from `{old value}` to `{new value}` (context: `{action}`)

All analysis is scoped to this entity + field change. Triggers that do not respond to this
combination are out of scope and must not appear in the firing set.

---

#### SECTION 2 — CANDIDATE LIST

List every trigger that *could* fire for this change based on entity, field, and trigger type
alone. Do not evaluate conditions.

| Candidate ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | | |

**PA Flow Type vocabulary** (use exactly): `Automated – Dataverse` / `Automated – SharePoint` /
`Automated – HTTP` / `Instant` / `Scheduled`

Denominator count: N

---

#### SECTION 3 — CASCADE-LINKED FIRING SEQUENCE

List every trigger that fires. Sync triggers before async. Number entries starting at 1.

**Cascade rule**: Every entry includes a mandatory "Spawns row N+1?" field. If the answer is
YES, the next numbered entry — entry #[current + 1] — MUST be the spawned downstream trigger,
not the next independent trigger in the firing sequence. Independent triggers resume after the
cascade chain terminates with a NO.

Use this entry template for every firing trigger:

---

**Entry #[N]: [Trigger Name]**

| Field | Value |
|---|---|
| Candidate ref | C-NN (from Section 2), or `[NOT IN CANDIDATES: reason]` |
| PA flow type | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` — one exact term |
| Execution tier | `Sync (blocks transaction)` or `Async (~N min [standard\|premium] tier)` |
| Condition | `No condition` or: condition text + `Taken: [branch] — [reason]` + `Skipped: [branch] — [reason]` |
| Reads | `{Entity}.{Field}` per consumed field, comma-separated |
| Produces | Opens with `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to` + connector + target + result |
| Side-effect writes | `{Entity}.{Field} = {value}` per field written, or `None` |
| Spawns row #[N+1]? | `NO — side-effect writes have no downstream automation potential` OR `YES → Row #[N+1] will be: [downstream trigger name]` (if YES, the immediately following entry must be that trigger) |

---

Rules for the Spawns field:
- "Spawns?" is **never optional**. Leaving it blank is a structural gap equivalent to an empty
  named slot.
- If Side-effect writes = None: Spawns must be `NO — no writes`.
- If Side-effect writes are present but no downstream automation applies: Spawns must be
  `NO — [field] write does not match any Section 2 candidate's trigger condition`.
- If a downstream trigger fires: Spawns must be `YES → Row #[N+1]: [trigger name]`, and
  Row #[N+1] must be that trigger.
- A YES that is not followed by the named trigger in the next entry is a cascade gap.

---

#### SECTION 4 — CANDIDATE RECONCILIATION

Resolve every Section 2 candidate:

| Candidate ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (entry #N)` / `CONFIRMED ABSENT — [specific reason]` /
`FLAGGED GAP — [reason expected but absent]`

Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 5 — PATHOLOGY VERDICTS

Address all three classes. Each verdict must cite a specific entry number or candidate ID from
Sections 3–4 as its evidence.

**Trigger Storm**
- Firing count: N (entries #1 through #N, list names)
- Storm threshold: > 3 executions per change event
- Re-entry evidence: [for each YES → Spawns chain in Section 3, does the spawned trigger feed
  back to an entry already in the firing set?]
- Verdict: `CLEARED (count = N, no re-entry)` or `STORM DETECTED (entries: [#N, ...]; re-entry: [path])`

**Missing Triggers**
- Flagged gaps from Section 4: [list or "none"]
- Per-gap: trigger name, gap cause, risk
- Verdict: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or
  `MISSING TRIGGER: [name — gap cause — risk]`

**Circular Triggers**
- Directed edges from Section 3 side-effect writes: `Entry #N writes {Field} → fires {Trigger}`
- Graph: DAG / CYCLIC
- Verdict: `CLEARED (DAG confirmed; edges: {listed})` or `CIRCULAR TRIGGER: [cycle path]`

---

#### TRIGGER MAP (Section 5 Appendix)

| Entry # | Trigger Name | Tier | Spawns | Anomaly Flag |
|---|---|---|---|---|
| | | Sync/Async | YES/NO | None / Storm / Cycle / Gap |

---

Now receive the scenario and trigger registry, then produce the full report.

---

## V-03 — Phrasing Register: Evidence-Before-Verdict (EBV) Protocol

**Variation axis**: Phrasing register (formal specification + mandatory sub-structure)
**Hypothesis**: Prior variations required evidence-anchored verdicts through instruction ("each
verdict must cite specific evidence") but did not structurally prevent a bare verdict. A model
can write "CLEARED — no circular triggers" and satisfy a loose reading of the instruction.
V-03 introduces a two-part sub-structure — EVIDENCE BLOCK followed by VERDICT SENTENCE — for
every anomaly verdict, where the EVIDENCE BLOCK is a required named section with fill-in-the-
blank citations. A missing EVIDENCE BLOCK is not a style choice; it is a structurally visible
gap (an empty named section). Additionally, any vocabulary violation, empty named slot, or
structural gap encountered during enumeration must be tagged inline using a four-token
vocabulary. This makes C-12 and C-13 observable without an expert reviewer.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This document specifies an Evidence-
Before-Verdict (EBV) analysis protocol for trigger fire reports. Apply it exactly.

---

#### INLINE TAG VOCABULARY

These four tags must be used wherever their condition applies. Do not paraphrase or substitute.

| Tag | Apply when |
|---|---|
| `[VOCAB FAIL: {actual text}]` | A cell or sentence uses a non-conforming term where a governed vocabulary term is required (PA flow type, input payload format, output action lead word) |
| `[INSUFFICIENT]` | A named slot exists but its content does not meet the minimum specificity requirement (e.g., a Condition cell that says only "checks status" without stating branches, or an Output cell that says "updates the record") |
| `[FLAGGED GAP]` | A candidate expected to fire is absent from the firing set with no explanation |
| `[BARE ASSERTION]` | A verdict sentence appears without a preceding EVIDENCE BLOCK — i.e., the verdict sub-section is present but the evidence sub-section is missing or empty |

These tags must appear inline at the point of defect, not in a summary at the end.

---

#### STEP 1 — CANDIDATE PRE-SCAN

Before determining which triggers fire, list all candidates:

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | |

*PA Flow Type is a governed vocabulary. Any other term: apply `[VOCAB FAIL: actual text]`.*

Denominator: N

---

#### STEP 2 — TRIGGER ENUMERATION

For each firing trigger, produce a numbered entry using the template below. Apply tags inline as
needed; do not defer defects to a closing section.

---

**[#] [Trigger Name]** *(C-ID: ___)*

**Identity**: `[Automated – Dataverse | Automated – SharePoint | Automated – HTTP | Instant | Scheduled]` — executes in `[Sync (blocks transaction) | Async (~N min standard tier | ~N min premium tier)]`
*Apply `[VOCAB FAIL]` if the flow type term deviates. Apply `[VOCAB FAIL]` if the tier term is absent or non-specific.*

**Condition**:
`No condition`
— or —
`Evaluates: [condition text]`
`Taken: [branch name] — [reason the condition evaluates to this branch for this change]`
`Skipped: [branch name] — [reason the other branch does not apply]`
*A Condition entry that names only one branch: apply `[INSUFFICIENT]` after the entry.*

**Reads**: `{Entity}.{Field}` for each consumed field, comma-separated.
*Any reference that omits entity or field name: apply `[VOCAB FAIL: actual text]`.*

**Produces**: [lead word from: `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to`] + connector + specific target + resulting state.
*Any output description that opens with a non-governed lead word: apply `[VOCAB FAIL: actual text]`.*
*Any output description that omits connector or target: apply `[INSUFFICIENT]`.*

**Side-effect writes**: `{Entity}.{Field} = {value}` per write, or `None`.
*If a write carries downstream automation potential (i.e., matches any C-ID candidate's trigger condition), the downstream trigger MUST be the immediately following numbered entry.*

---

#### STEP 3 — CANDIDATE RECONCILIATION

| C-ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution codes: `FIRED (#N)` / `CONFIRMED ABSENT ([reason])` / `FLAGGED GAP` (apply `[FLAGGED GAP]` tag)

---

#### STEP 4 — EVIDENCE-BEFORE-VERDICT ANOMALY ASSESSMENT

For each of the three anomaly classes, the output must contain an EVIDENCE BLOCK followed by a
VERDICT SENTENCE. The EVIDENCE BLOCK must name specific triggers, entry numbers, or field writes
from Steps 2–3. A VERDICT SENTENCE that appears without a preceding EVIDENCE BLOCK must be
tagged `[BARE ASSERTION]`.

---

**ANOMALY CLASS 1: TRIGGER STORM**

**EVIDENCE BLOCK**:
> Total firing count: N (entries: #___, #___, ...)
> Re-entry check: [for each side-effect write in Step 2, state whether it matches any C-ID candidate]
> Re-entry found: YES / NO

**VERDICT**: *(must follow the EVIDENCE BLOCK; a verdict appearing without the above evidence is `[BARE ASSERTION]`)*
`CLEARED (count = N, no re-entry)` or `STORM DETECTED (count = N; group: entries #___; re-entry: [path])`

---

**ANOMALY CLASS 2: MISSING TRIGGERS**

**EVIDENCE BLOCK**:
> Section 3 resolutions: [list each C-ID with FIRED / CONFIRMED ABSENT / FLAGGED GAP]
> FLAGGED GAP entries: [list, or "none"]

**VERDICT**: *(must follow the EVIDENCE BLOCK)*
`CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or
`MISSING TRIGGER: [name — gap cause — risk]`

---

**ANOMALY CLASS 3: CIRCULAR TRIGGERS**

**EVIDENCE BLOCK**:
> Directed edge set: `{Trigger} writes {Entity.Field} → fires {Trigger}` for each side-effect write in Step 2
> Graph property: DAG / CYCLIC

**VERDICT**: *(must follow the EVIDENCE BLOCK)*
`CLEARED (DAG confirmed; edges: {listed})` or `CIRCULAR TRIGGER: [cycle path]`

---

Now receive the scenario and trigger registry. Apply this protocol. Use the tag vocabulary
inline throughout; do not accumulate defects for a closing summary.

---

## V-04 — Combined: Pre-Opened Anomaly Slots + Cascade-Spawning Rows

**Variation axis**: Role sequence + output format
**Hypothesis**: V-01 targets C-10 by requiring Section 0 (anomaly slots OPEN) before any
enumeration. V-02 targets C-11 by requiring a "Spawns?" decision cell in every trigger entry.
This combination asks whether the two mechanisms reinforce each other: the pre-opened anomaly
slots create live questions that the cascade-spawning rows must fill as they are written.
Specifically, the open Storm investigation slot motivates the enumerator to watch re-entry paths
as it writes each Spawns? cell; the open Circular investigation slot motivates the enumerator to
build the edge set incrementally. The hypothesis is that live anomaly questions + cascade-linked
rows produce more complete coverage of C-10, C-11, and C-13 simultaneously than either
mechanism alone.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report in four
phases. Phases are ordered; do not begin a later phase before completing an earlier one.

---

#### PHASE 0 — OPEN ANOMALY REGISTER (complete before Phase 1)

Declare all three anomaly investigations as OPEN. These declarations must appear in your output
before any trigger is enumerated. Fill in the evidence slots during Phase 2 as you encounter
relevant information; do not leave them empty at Phase 3.

```
┌─────────────────────────────────────────────────────────────────────────┐
│ ANOMALY REGISTER — all slots OPEN at Phase 0                            │
├─────────────────────────────────────────────────────────────────────────┤
│ SLOT 1 — TRIGGER STORM                                                  │
│   Status: OPEN                                                          │
│   Watching for: total firing count > 3; re-entry paths from side-effect │
│     writes back to any trigger condition                                │
│   Evidence accumulating: [ will be populated during Phase 2 ]           │
│   Verdict: [ will be stated at Phase 3 ]                                │
├─────────────────────────────────────────────────────────────────────────┤
│ SLOT 2 — MISSING TRIGGERS                                               │
│   Status: OPEN                                                          │
│   Watching for: candidates from Phase 1 that do not appear in Phase 2  │
│     firing set without a confirmed reason for absence                   │
│   Evidence accumulating: [ will be populated during Phase 2 ]           │
│   Verdict: [ will be stated at Phase 3 ]                                │
├─────────────────────────────────────────────────────────────────────────┤
│ SLOT 3 — CIRCULAR TRIGGERS                                              │
│   Status: OPEN                                                          │
│   Watching for: directed edges from side-effect writes that form cycles │
│   Evidence accumulating: [ will be populated during Phase 2 ]           │
│   Verdict: [ will be stated at Phase 3 ]                                │
└─────────────────────────────────────────────────────────────────────────┘
```

---

#### PHASE 1 — CANDIDATE PRE-SCAN

List all triggers that could fire based on entity, field, and trigger type. Evaluate no
conditions; determine no outcomes.

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | |

Denominator: N. Every C-ID must be resolved in Phase 2.

---

#### PHASE 2 — CASCADE-LINKED FIRING SEQUENCE

List firing triggers in order. Sync before async. Use the entry format below.

**Cascade rule — Spawns? cell**: This field is mandatory for every entry.
- `NO — [reason: no writes / write does not match any Phase 1 candidate]`
- `YES → ENTRY #[N+1]: [downstream trigger name]` — if YES, that named trigger MUST be entry
  #[N+1] before any independent trigger continues the sequence

Additionally, update the anomaly register slots during this phase. After each YES-Spawns entry,
append one line to SLOT 1's "Evidence accumulating" block naming the potential re-entry path.
After each edge that is constructed (from Side-effect writes), append it to SLOT 3's "Evidence
accumulating" block.

---

**ENTRY #[N]: [Trigger Name]**

| Field | Value |
|---|---|
| C-ID ref | C-NN or `[NOT IN PHASE 1: reason]` |
| PA flow type | exact term from Phase 1 vocabulary |
| Execution tier | `Sync (blocks transaction)` or `Async (~N min [standard\|premium] tier)` |
| Condition | `No condition` or: `Evaluates: [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason].` |
| Reads | `{Entity}.{Field}` per consumed field |
| Produces | [lead word] + connector + target + resulting state |
| Side-effect writes | `{Entity}.{Field} = {value}` per write, or `None` |
| Spawns? | `NO — [reason]` or `YES → ENTRY #[N+1]: [trigger name]` |

*After each entry: update ANOMALY REGISTER SLOT 3 if a new edge is identified.*

---

**Candidate reconciliation (after last entry)**:

| C-ID | Resolution | Reason |
|---|---|---|

Resolution: `FIRED (entry #N)` / `CONFIRMED ABSENT — [reason]` / `FLAGGED GAP — [reason]`

*After reconciliation: update ANOMALY REGISTER SLOT 2 with the final candidate resolution list.*

---

#### PHASE 3 — CLOSE ANOMALY REGISTER

Close each slot by replacing its verdict placeholder. Each closure must state:
1. The evidence accumulated during Phase 2 (cite entry numbers and field names)
2. The verdict sentence (begins `CLEARED` or names the detected anomaly)

A verdict with no phase-2 evidence cited is a `[BARE ASSERTION]`.

---

**SLOT 1 — TRIGGER STORM** — Status: CLOSED

Evidence from Phase 2:
- Firing count: N (entries #___)
- Re-entry paths identified: [from Spawns? YES entries — list paths, or "none"]

Verdict: `CLEARED (count = N, no re-entry)` or `STORM DETECTED (count = N; entries: [#N]; re-entry: [path])`

---

**SLOT 2 — MISSING TRIGGERS** — Status: CLOSED

Evidence from Phase 2:
- Candidate reconciliation: [from Phase 2 table — list each C-ID resolution]

Verdict: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or
`MISSING TRIGGER: [name — gap cause — risk level]`

---

**SLOT 3 — CIRCULAR TRIGGERS** — Status: CLOSED

Evidence from Phase 2:
- Directed edge set: [from Phase 2 side-effect writes — list each edge]
- Graph property: DAG / CYCLIC

Verdict: `CLEARED (DAG confirmed; edges: {listed})` or `CIRCULAR TRIGGER: [cycle path]`

---

Now receive the scenario and trigger registry. Begin with Phase 0.

---

## V-05 — Combined: Named Failure Modes + Self-Annotation Protocol

**Variation axis**: Phrasing register (formal normative) + inertia framing
**Hypothesis**: R2/V-05 named three failure modes (Undeclared Denominator, Closed-Set Pathology
Scan, Vocabulary Drift) and mapped them to criteria C-01/C-04/C-08. Those failure modes drove
strong structural compliance for criteria up through C-09. Rubric v2 adds four more criteria
(C-10 through C-13) whose failure modes were not yet named. V-05/v2 extends the inertia framing
with four new named failure modes that map precisely to the new criteria, then pairs each failure
mode with (a) its formal SHALL requirement and (b) its required inline tag. The hypothesis is
that naming failure modes + specifying their tags in the same section creates the strongest
motivation for self-annotation: the model knows not just *what* to tag but *why* the tag exists.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert conducting a trigger fire analysis.

---

#### SEVEN FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

Before the protocol, review seven failure modes that informal analysis cannot prevent. Each maps
to a specific criterion and is addressed by a specific protocol requirement with an inline tag.

---

**Failure Mode 1 — Undeclared Denominator**
The analysis begins by listing what fires. Triggers that were never considered leave silence,
not a visible gap. A reviewer cannot distinguish "considered and excluded" from "never
considered." Maps to: C-01 (complete trigger enumeration).
*Protocol response: candidate pre-scan runs before any outcome determination. Denominator count
is declared and locked. All candidates must be resolved.*

**Failure Mode 2 — Closed-Set Pathology Scan**
Pathology identification happens after the firing set locks in. There is no obligation to
compare the set against a denominator. Anomaly classes with no instances are silently omitted.
Maps to: C-04 (all three anomaly classes assessed).
*Protocol response: all three anomaly investigations are declared OPEN in Section 0 before
enumeration begins. An anomaly class may be CLEARED but not silently omitted.*

**Failure Mode 3 — Vocabulary Drift**
Descriptions like "sends a notification" or "cloud flow" pass informal review. Only an expert
reviewer catches the violation. Maps to: C-07 (platform grounding).
*Protocol response: governed term sets defined at Section 0. Non-conforming values:
apply `[VOCAB FAIL: actual text]` inline.*

**Failure Mode 4 — Branch Amnesia**
Conditional triggers document only the branch that fires. The skipped branch — which reveals
when the automation will NOT fire — is omitted. Maps to: C-06 (trigger conditions stated).
*Protocol response: every conditional trigger SHALL declare both branches with reasons. A
single-branch declaration: apply `[INSUFFICIENT: only taken branch declared]` inline.*

**Failure Mode 5 — Latency Blindness**
Sync and async triggers are mixed without tier labeling. Async latency is omitted. Stakeholders
misunderstand whether automations are blocking or fire-and-forget. Maps to: C-03 (inputs and
outputs per trigger) — specifically the execution context.
*Protocol response: every trigger SHALL declare Sync/Async tier; Async triggers SHALL include
numeric latency. Missing tier: apply `[INSUFFICIENT: tier undeclared]` inline.*

**Failure Mode 6 — Post-Hoc Anomaly Assembly**
All three anomaly slots are opened only after the firing set is complete, in a closing summary.
This is structurally equivalent to Closed-Set Pathology Scan — the anomaly questions are
answered against a fixed list rather than held open during enumeration. Maps to: C-10 (anomaly
questions pre-opened).
*Protocol response: anomaly investigations SHALL be declared OPEN in Section 0 before Section 1
(candidate scan). A Section 0 that appears after enumeration output fails C-10 regardless of
content. Anomaly findings that appear only in a closing summary without pre-enumeration framing:
apply `[POST-HOC: anomaly section appeared after enumeration]`.*

**Failure Mode 7 — Cascade Annotation Without Continuation**
A side-effect field write with downstream automation potential is noted in the side-effects
column but does not spawn a new trigger row. The cascade chain terminates at the annotation.
Maps to: C-11 (cascade completeness).
*Protocol response: any side-effect write that matches a candidate's trigger condition SHALL
produce the downstream trigger as the immediately following numbered entry. An annotation that
does not produce a next row: apply `[CASCADE GAP: {trigger name} write noted but not continued]`.*

**Failure Mode 8 — Verdict-Without-Evidence**
An anomaly verdict is stated as a direct assertion ("No circular triggers detected") without
citing specific evidence from the enumeration. A reviewer cannot verify the verdict without
re-running the analysis. Maps to: C-13 (evidence-anchored anomaly verdicts).
*Protocol response: every anomaly verdict SHALL be preceded by an EVIDENCE BLOCK naming
specific entries, field writes, or row counts from the enumeration. A verdict without an EVIDENCE
BLOCK: apply `[BARE ASSERTION: verdict stated without preceding evidence]`.*

The protocol below addresses each failure mode at its structural root.

---

#### SECTION 0 — GOVERNED TERM SETS + OPEN ANOMALY REGISTER

**Term Set A — PA Flow Type** (governed; non-conforming: `[VOCAB FAIL: actual]`)

| Code | Term |
|---|---|
| A-01 | `Automated – Dataverse` |
| A-02 | `Automated – SharePoint` |
| A-03 | `Automated – HTTP` |
| A-04 | `Instant` |
| A-05 | `Scheduled` |

**Term Set B — Execution Tier** (governed; non-conforming: `[INSUFFICIENT: tier undeclared]`)

| Code | Term | Timing |
|---|---|---|
| B-01 | `Sync` | `Inline (blocks transaction)` |
| B-02 | `Async` | `~N min [standard\|premium] tier` — N must be numeric |

**Term Set C — Input Payload** (governed; non-conforming: `[VOCAB FAIL: actual]`)
Pattern: `{TableName}.{ColumnName}`. References that omit table or column name are non-conforming.

**Term Set D — Output Action Lead** (governed; non-conforming: `[VOCAB FAIL: actual]`)
First word of output action cell must be one of: `Sets` / `Creates` / `Deletes` /
`Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to`.

**Term Set E — Branch Coverage** (governed; non-conforming: `[INSUFFICIENT: only taken branch declared]`)
For conditional triggers:
- `Taken: [branch name] — [reason this branch fires for this change]`
- `Skipped: [branch name] — [reason this branch does not fire]`
For unconditional triggers: `No condition`.

**ANOMALY INVESTIGATIONS — declared OPEN (addresses Failure Mode 6)**

```
INVESTIGATION A — TRIGGER STORM          Status: OPEN
INVESTIGATION B — MISSING TRIGGERS       Status: OPEN
INVESTIGATION C — CIRCULAR TRIGGERS      Status: OPEN
```

These investigations remain OPEN until Section 4. Any investigation closed before Section 4 is
a protocol violation. Any investigation that appears only in Section 4 without this Section 0
declaration: apply `[POST-HOC: anomaly section appeared after enumeration]`.

---

#### SECTION 1 — CANDIDATE PRE-SCAN (addresses Failure Mode 1)

Enumerate all candidates before evaluating any condition.

| C-ID | Trigger Name | Type (Term Set A) | Matching Basis |
|---|---|---|---|
| C-01 | | | |

Denominator: N. All C-IDs SHALL be resolved in Section 3.

---

#### SECTION 2 — TRIGGER ENUMERATION (addresses Failure Modes 3, 4, 5, 7)

List firing triggers in order. Sync before async. For each trigger:

| Field | Requirement |
|---|---|
| **# / C-ID ref** | Entry number; C-ID from Section 1, or `[NOT IN DENOMINATOR: reason]` |
| **PA flow type** | Term Set A — apply `[VOCAB FAIL]` on deviation |
| **Execution tier** | Term Set B — apply `[INSUFFICIENT: tier undeclared]` if absent |
| **Condition** | Term Set E — apply `[INSUFFICIENT: only taken branch declared]` if single-branch |
| **Reads** | Term Set C — apply `[VOCAB FAIL]` on non-conforming references |
| **Produces** | Term Set D lead word + connector + target + state — apply `[VOCAB FAIL]` or `[INSUFFICIENT]` as needed |
| **Side-effect writes** | `{Entity}.{Field} = {value}` or `None` |
| **Cascade continuation** | If a side-effect write matches any Section 1 candidate's trigger condition: the downstream trigger MUST be entry #[N+1]. If not continued: apply `[CASCADE GAP: {trigger name} write not continued]` |

---

#### SECTION 3 — CANDIDATE RECONCILIATION (addresses Failure Mode 2)

| C-ID | Trigger Name | Resolution | Reason |
|---|---|---|---|

Resolution: `FIRED (entry #N)` / `CONFIRMED ABSENT — [specific condition that blocked firing]` /
`FLAGGED GAP — [reason expected]`

Non-resolved candidates (no entry in this table) are structural gaps equivalent to
`[FLAGGED GAP]`.

---

#### SECTION 4 — EVIDENCE-BEFORE-VERDICT PATHOLOGY ASSESSMENT (addresses Failure Modes 2, 8)

Each anomaly investigation is closed using an EVIDENCE BLOCK followed by a VERDICT. The
EVIDENCE BLOCK must cite specific entries, C-IDs, or field writes from Sections 2–3. A VERDICT
with no preceding EVIDENCE BLOCK: apply `[BARE ASSERTION: verdict stated without preceding evidence]`.

---

**INVESTIGATION A — TRIGGER STORM** — Status: CLOSED

EVIDENCE BLOCK:
> Firing count from Section 2: N (entries #___)
> Re-entry check: for each side-effect write in Section 2, state whether that field appears in
>   any Section 1 candidate's trigger condition (yes/no per field)

VERDICT: `CLEARED (count = N, threshold not reached, no re-entry)` or
`STORM DETECTED (count = N; entry group: [#N, ...]; re-entry path: [field → trigger])`
Mitigation if STORM DETECTED: [debounce / condition / re-entry guard]

---

**INVESTIGATION B — MISSING TRIGGERS** — Status: CLOSED

EVIDENCE BLOCK:
> Section 3 reconciliation results: [list each C-ID with FIRED / CONFIRMED ABSENT / FLAGGED GAP]

VERDICT: `CLEARED (N candidates: N fired, N confirmed absent, 0 flagged gaps)` or
`MISSING TRIGGER: [name — gap cause — risk level]`
Mitigation if MISSING TRIGGER: [registration fix / condition correction]

---

**INVESTIGATION C — CIRCULAR TRIGGERS** — Status: CLOSED

EVIDENCE BLOCK:
> Directed edges from Section 2 side-effect writes:
>   `Entry #N [Trigger A] writes {Entity.Field} → fires [Trigger B]`
>   (list all edges; if none: "No side-effect writes with downstream automation potential")
> Graph property: DAG / CYCLIC

VERDICT: `CLEARED (DAG confirmed; edge set: {listed})` or
`CIRCULAR TRIGGER: [full cycle path with entry numbers]`
Mitigation if CIRCULAR TRIGGER: [cycle-break condition / run-once flag / depth limit]

---

Now receive the scenario and trigger registry. Begin with Section 0. Apply all tags inline.

---
