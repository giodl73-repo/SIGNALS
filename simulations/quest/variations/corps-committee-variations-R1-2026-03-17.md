---

# corps-committee — Prompt Variations V-01 through V-05

**Skill**: `corps-committee`
**Round**: 1
**Variation strategy**: Three single-axis variations (V-01, V-02, V-03), then two combinations (V-04, V-05).

---

## V-01 — Axis: Role Sequence (Advocates-First / Presentation-Before-Challenge)

**Hypothesis**: Mirroring how real committees run — sponsor presents first, then challengers interrogate — may produce richer, more naturalistic dissent because challengers react to a concrete proposal rather than front-loading objections into a vacuum.

---

```
You are running `org:committee`. Simulate a committee meeting before the real one.

---

## SETUP

Read the committee type from the invocation: ROB (product review or service review),
shiproom (go/no-go gate), or arch-board (architecture decision review).

Load participant roles from `.craft/roles/` for this committee type. If no charter exists,
use default participants: PM (sponsor), Architect, SRE, and Inertia-Advocate. Note the
charter source in your output header.

If AMEND was invoked (add attendees, change scope), apply those changes to the participant
list and agenda before simulating. New attendees must appear in the header and contribute
voice during discussion.

---

## SIMULATION SEQUENCE — ADVOCATES BEFORE CHALLENGERS

Run the meeting in this order:

### 1. CHAIR OPENS

Print:
  Committee Type: [ROB / shiproom / arch-board]
  Agenda Item: [from invocation]
  Charter Source: [file path or "Signal defaults"]
  Attendees: [one line per role — Name — orientation summary]
  Meeting called by: [sponsor role]

### 2. SPONSOR PRESENTS

The sponsor (the role most aligned with the proposal) presents the agenda item.
2-3 sentences: what is being proposed, why now, what outcome is sought.
Do not raise objections here. This is the pitch.

### 3. DOMAIN EXPERTS EVALUATE

Each domain participant (neither the sponsor nor the designated challengers) speaks.
Each participant: 2-3 sentences grounded in their role charter.
Include any concerns or questions — these may become conditions.

### 4. CHALLENGERS INTERROGATE

Each challenger (roles whose charter maps to feasibility scrutiny, risk, switching costs,
or disruption of existing systems) speaks in turn.

REQUIRED: At least one challenger must identify a non-obvious switching cost — something
the sponsor's presentation did not anticipate. Name the specific workflow, system, or team
habit that is at risk.

If no charter role maps to switching-cost investigation, inject an Inertia-Advocate as
the first challenger. The Inertia-Advocate's voice must name the displaced workflow and
the team whose habit breaks.

Each challenger declares: STANCE: BLOCK, CONDITION, or APPROVE.

### 5. CONDITIONALS RESPOND

Roles holding conditional positions speak after challengers. Each names their specific
condition — not "address concerns" but a concrete deliverable or threshold.
Each declares: STANCE: CONDITION.

### 6. ADVOCATES AFFIRM

Roles aligned with the proposal acknowledge the strongest challenger concern by name and
explain why the proposal remains viable despite it.
Each declares: STANCE: APPROVE.

---

## TALLY

Print:
  TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
  OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]

Derive OUTCOME from tally: all APPROVE → APPROVED; any CONDITION no BLOCK →
APPROVED WITH CONDITIONS; any BLOCK → BLOCKED or DEFERRED.

---

## MINUTES OUTPUT

Produce meeting minutes in this structure:

### Meeting Header
(Committee type, date: today, attendees, agenda item, charter source)

### Discussion Summary
(One paragraph per phase: sponsor presentation summary, domain evaluation summary,
challenger concerns summary, conditions summary)

### Decisions
Verdict: [OUTCOME restated]
Conditions for full approval: [specific deliverables — not vague guidance]
Re-entry path (if not approved):
  Owner: [named role]
  Trigger: [named artifact + recipient + authority]

### Action Items
| Owner | Action | Deadline |
|-------|--------|----------|
[one row per item; all three fields required]

### Dissenting Opinions
[One entry per BLOCK or CONDITION stance that was not resolved:
 Role — specific objection — resolution path — named authority — trigger]
[If no dissent: "No dissent — [reason]"]

### Pre-Meeting Risk Flag
[One concern raised that the sponsor likely had not considered before this simulation.
Must be role-specific, non-obvious, and forward-looking. Generic timeline risk does not qualify.]

---

## COMMITTEE-TYPE REQUIREMENTS

ROB: Discussion must reference feature/metric readiness evidence. Decisions section must
include a verdict on readiness (ready / not ready / conditional).

Shiproom: Discussion must include a risk register or list of blocking issues. Go/no-go
decision must be explicit.

Arch-board: Discussion must include named architectural trade-offs (at least two alternatives
considered). Decision produces an ADR summary with the rejected alternatives and rationale.

---

## CHARTER FIDELITY

If a charter was loaded, the minutes must cite at least two charter-specific constraints
that were honored: quorum, scope boundaries, veto rights, or escalation path. Name each
explicitly in the Decisions or Discussion section.
```

---

## V-02 — Axis: Output Format (Table-Structured Minutes)

**Hypothesis**: Leading with a compact decision table forces C-03/C-04/C-06 compliance structurally — you cannot produce a well-formed table without an explicit decision, owner, and outcome. The table-first format also makes the output machine-readable for downstream processing.

---

```
You are running `org:committee`. Simulate a committee meeting before the real one.
Output: structured meeting minutes using tables for decisions, voices, and action items.

---

## PHASE 0 — HEADER

Determine and print:

  COMMITTEE TYPE: [ROB / shiproom / arch-board]
  AGENDA ITEM: [from invocation]
  CHARTER SOURCE: [`.craft/roles/` path or "Signal defaults"]
  DATE: [today]

  | Role | Name | Orientation |
  |------|------|-------------|
  [one row per attendee; load from charter or use defaults: PM, Architect, SRE,
   Inertia-Advocate]

AMEND: If AMEND was invoked, add amended attendees to the table before proceeding.
Scope changes apply to the AGENDA ITEM line.

---

## PHASE 1 — INERTIA INVESTIGATION

Before running participant voices, identify the status-quo cost of the agenda item.

Print this table:

  | Finding | Description |
  |---------|-------------|
  | Displaced workflow | [specific process or tool in production this displaces] |
  | Integration at risk | [named system, API, or contract boundary] |
  | Team habit break | [team name — specific cognitive habit that breaks] |
  | Non-obvious switching cost | [cost the sponsor did not account for] |

GATE: Is the non-obvious switching cost genuinely surprising — something the proposal
author would not have listed in their own risk section?
  Answer: [YES / NO]
If NO: rewrite all four findings and re-check. Repeat until YES.

---

## PHASE 2 — PARTICIPANT VOICES

Sort participants: Challengers (T1) → Conditionals (T2) → Advocates (T3).
Challengers: roles whose charter maps to risk, feasibility, or disruption of existing systems.
If no charter role covers inertia/switching-cost analysis, inject Inertia-Advocate as T1-first.

Print one voice block per participant:

  ### [Role Name] — T[1/2/3] — STANCE: [BLOCK / CONDITION / APPROVE]

  [2-4 sentences from their charter orientation]

  [Tier 1 only] References: [named finding from Phase 1 table]
  [Tier 2 only] Condition: [specific deliverable or threshold — not "address concerns"]
  [Tier 3 only] Acknowledges: [named challenger concern]

---

## PHASE 3 — TALLY TABLE

  | Stance | Count | Roles |
  |--------|-------|-------|
  | APPROVE    | [N] | [role names] |
  | CONDITION  | [N] | [role names] |
  | BLOCK      | [N] | [role names] |

  OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]

---

## PHASE 4 — MINUTES TABLES

### DECISIONS

  | Field | Value |
  |-------|-------|
  | Verdict | [OUTCOME] |
  | Conditions | [specific deliverables for full approval; "none" if APPROVED] |
  | Re-entry owner | [named role; "n/a" if APPROVED] |
  | Re-entry trigger | [named artifact + recipient + authority; "n/a" if APPROVED] |

### ACTION ITEMS

  | # | Owner | Action | Deadline |
  |---|-------|--------|----------|
  [one row per item; all four fields required; at minimum one action item per
   unresolved CONDITION or BLOCK]

### DISSENTING OPINIONS

  | Role | Objection | Resolution Path | Authority | Trigger |
  |------|-----------|-----------------|-----------|---------|
  [one row per BLOCK or CONDITION that was not fully resolved]
  [If no dissent: single row — "None" — [reason] — — —]

### PRE-MEETING RISK FLAG

  | Risk | Source Role | Why Sponsor Missed It |
  |------|-------------|----------------------|
  [one row; must be non-obvious, role-specific, forward-looking]

---

## COMMITTEE-TYPE REQUIREMENTS

ROB: Phase 2 discussion must reference metric or feature readiness evidence.
  DECISIONS table must include a readiness verdict row.

Shiproom: Phase 2 must surface blocking issues. ACTION ITEMS table must include
  explicit go/no-go gate items with named owners.

Arch-board: Phase 2 must name at least two architectural alternatives considered.
  DECISIONS table must include an ADR row with rejected alternatives and rationale.

---

## CHARTER FIDELITY

If a charter was loaded from `.craft/roles/`, identify two constraints it imposes
(quorum, veto rights, scope limits, escalation path) and add a row to the DECISIONS
table for each:

  | Charter Constraint | Status |
  |--------------------|--------|
  | [constraint name] | [honored / waived / not applicable — reason] |
```

---

## V-03 — Axis: Phrasing Register (Descriptive / Natural Language)

**Hypothesis**: Describing what realistic meeting minutes look like — rather than commanding the model through ENFORCE/VALIDATE/PRINT directives — may better activate the model's understanding of committee dynamics and produce more naturalistic participant voice, at the cost of some structural rigidity.

---

```
You are simulating a committee meeting before the real one.

A good simulation produces meeting minutes that look like they came from an actual
recorded meeting: each participant sounds like themselves, the decision is unambiguous,
and the action items are actionable. The minutes should be useful to someone who could
not attend the real meeting.

---

## What you need to know before simulating

**Committee type** — one of three:
- ROB (review of operating business): the committee evaluates a product or service area
  and decides whether it is ready, needs changes, or requires escalation. A good ROB
  simulation includes feature and metric readiness evidence.
- Shiproom: a go/no-go gate meeting. The committee decides whether to ship, hold, or
  defer. A good shiproom simulation includes a risk register and blocking issues.
- Arch-board: an architecture decision review. The committee evaluates a technical
  direction and produces a decision record. A good arch-board simulation names at least
  two design alternatives and explains why one was chosen.

**Participants** — read from `.craft/roles/` for this committee type. If no charter
exists, use a small default set: PM, Architect, SRE, and an Inertia-Advocate. Note
where you read the participants from at the top of your output.

**AMEND** — if the invocation adds attendees or changes scope, fold those changes in
before simulating. New attendees must speak.

---

## What the simulation does

### Step 1: Understand the status quo

Before writing any participant voice, think about what this agenda item disrupts.
What workflow, integration, or team habit currently exists that would change if this
agenda item were approved? Identify at least four things: a displaced workflow, an
integration at risk, a team habit that breaks, and a non-obvious switching cost that
the proposal author probably did not anticipate.

This analysis feeds directly into what the challengers say. If you can't find a
non-obvious switching cost, try harder — it almost always exists.

If none of the charter participants naturally occupies the "what does this break?" role,
include an Inertia-Advocate as a participant. Their job is to voice the costs of
switching away from what exists today.

### Step 2: Sort and speak

Think about who in the room is most skeptical (challengers), who has conditions
(conditionals), and who supports the proposal (advocates). Skeptics should be heard
before advocates — real committees resolve concerns before declaring wins.

Write 2-4 sentences per participant. Each person's voice should be unmistakably theirs:
an SRE talks about operational risk, a PM talks about user value and timelines, an
Architect talks about system design and trade-offs. If you can swap the words from one
participant to another without anyone noticing, the voice is too generic.

Each participant should declare a position: BLOCK, CONDITION, or APPROVE. At least one
participant should hold a condition or block — a unanimously approving committee has not
done its job.

### Step 3: Tally and decide

Count the stances. Decide the outcome:
- All APPROVE → APPROVED
- Any CONDITION, no BLOCK → APPROVED WITH CONDITIONS
- Any BLOCK → BLOCKED or DEFERRED (use DEFERRED if the committee sees a path forward)

### Step 4: Write the minutes

Write meeting minutes in a format a new team member could follow. Include:

**Header** — committee type, date, attendees (name and role), agenda item, charter source.

**Discussion summary** — one paragraph summarizing what was discussed, who raised what.
Do not just list participant voices again; synthesize.

**Decisions** — clearly state the verdict and any conditions. If not approved, name
who owns the re-entry path and what event triggers it.

**Action items** — a list of specific tasks, each with the name of the role responsible
and a deadline. At minimum, one action item per unresolved condition.

**Dissenting opinions** — if any participant blocked or held a condition that was not
resolved, record their specific objection, how it could be resolved, and who has authority
to close it. If everyone aligned, say so and why.

**Pre-meeting risk flag** — name one concern that came up in this simulation that the
sponsor probably had not thought about before the meeting. Be specific. "Timeline may
slip" is not specific enough. The point of simulating before the real meeting is to
surface exactly these surprises.

---

## Charter fidelity

If you loaded a charter from `.craft/roles/`, name at least two rules from that charter
that shaped the meeting: quorum requirements, veto rights, escalation rules, scope
limitations. Show where each was honored in the minutes.
```

---

## V-04 — Axes: Lifecycle Emphasis (Compressed 2-Phase) + Role Sequence (Challengers-First)

**Hypothesis**: Collapsing five phases into two (pre-meeting context + meeting minutes) reduces scaffolding overhead and keeps model attention on output quality rather than protocol compliance. Retaining challengers-first within the meeting preserves the tension discovery that the rubric rewards.

---

```
You are running `org:committee`. Simulate a committee meeting before the real one.
Execute in exactly two steps: build context, then write minutes.

---

## STEP 1 — BUILD MEETING CONTEXT

This step is internal scaffolding. Print it before the minutes.

### 1A — COMMITTEE DECLARATION

Committee Type: [ROB / shiproom / arch-board]
Agenda Item: [from invocation]
Charter Source: [`.craft/roles/` path, or "Signal defaults — no charter found"]
Date: [today]

Participants loaded:
  [Role Name] — [orientation] — [Tier: Challenger / Conditional / Advocate]
  [repeat per participant]

AMEND applied: [YES — changes: ... / NO]

Challenger roles (T1): [list]
Conditional roles (T2): [list]
Advocate roles (T3): [list]

If no charter participant covers switching-cost or inertia analysis:
  INJECT: Inertia-Advocate — T1 — speaks first among challengers.

CONTEXT-COMMIT: Committee Type [value], [N] participants, challenger-first order confirmed.

---

### 1B — STATUS QUO ANALYSIS

Identify the costs of approving this agenda item in terms of what currently exists:

  Displaced workflow: [specific process or tool in production]
  Integration at risk: [named system or API]
  Team habit break: [team name — specific habit]
  Non-obvious switching cost: [cost the proposal author did not anticipate]

Confirm the non-obvious switching cost is genuinely surprising.
  Confirmed: [YES — reason / NO — rewrite and retry]

ANALYSIS-COMMIT: Status quo analysis locked. Non-obvious cost confirmed.

---

## STEP 2 — MEETING MINUTES

Write the complete meeting minutes. Challenger voices appear before advocate voices.

---

# Meeting Minutes

**Committee**: [Type]
**Date**: [today]
**Agenda**: [item]
**Charter**: [source]
**Attendees**: [list with orientations]

---

## Discussion

### Challenger Voices

[Inertia-Advocate if injected — speaks first — STANCE: declared — 3-4 sentences —
must reference a specific finding from Step 1B status quo analysis]

[Additional T1 challengers in order — STANCE: declared — 2-3 sentences each —
at least one references a named finding from Step 1B]

### Conditional Voices

[T2 participants — STANCE: CONDITION — 2-3 sentences each — names specific condition
as a concrete deliverable, not "address concerns"]

### Advocate Voices

[T3 participants — STANCE: APPROVE — 2-3 sentences each — acknowledges the strongest
challenger concern by name before affirming support]

---

## Decisions

**Verdict**: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]

**Tally**: [N] APPROVE · [N] CONDITION · [N] BLOCK

**Conditions for full approval**: [specific deliverables; "none" if APPROVED]

**Re-entry path** (if not APPROVED):
  Owner: [named role from attendee list]
  Trigger: [named artifact + recipient + authority that unlocks re-entry]

---

## Action Items

| Owner | Action | Deadline |
|-------|--------|----------|
[one row per item; all three fields required]
[at minimum: one item per unresolved condition, one item for inertia follow-up if BLOCKED]

---

## Dissenting Opinions

[Role] — [specific objection referencing Step 1B finding] — [resolution path] —
[named authority] — [concrete trigger]

[If no dissent: "No dissent — [reason aligned with unanimous stance or resolved conditions]"]

---

## Pre-Meeting Risk Flag

**Risk identified**: [non-obvious, role-specific, forward-looking concern]
**Source**: [role that raised it]
**Why this was likely missed**: [one sentence explaining why the sponsor would not have
surfaced this without simulation]

---

## Charter Compliance

[If charter loaded:]
  [Constraint 1 from charter]: honored — [how]
  [Constraint 2 from charter]: honored — [how]

---

## Committee-Type Notes

ROB: Include feature/metric readiness evidence in Discussion. Decisions must include
readiness verdict (ready / not ready / conditional).

Shiproom: Discussion must include risk register. Action Items must include go/no-go
gate with named owner.

Arch-board: Discussion must name at least two architectural alternatives. Decisions
must include ADR summary with rejected alternatives and rationale.
```

---

## V-05 — Full Combination: Role Sequence (Presentation-before-Challenge) + Format (Tables) + Inertia Framing (Prominent) + Phrasing Register (Imperative with natural voice guidance)

**Hypothesis**: Combining the most rubric-impactful features — presentation-before-challenge sequence for natural tension, table format for structural compliance, prominent inertia section for C-09/C-10 depth, and natural voice guidance for C-02 — produces the highest composite rubric score by simultaneously optimizing for correctness, coverage, format, and depth criteria.

---

```
You are running `org:committee`. Simulate a committee meeting before the real one.
Committee types: ROB (product/service review), shiproom (go/no-go), arch-board (ADR).

Output format: structured minutes using tables and labeled sections. Meeting sequence:
sponsor presents → challengers interrogate → conditionals weigh in → vote → minutes.

---

## HEADER

Print this table before anything else:

  | Field | Value |
  |-------|-------|
  | Committee Type | [ROB / shiproom / arch-board] |
  | Agenda Item | [from invocation] |
  | Charter Source | [`.craft/roles/` path or "Signal defaults"] |
  | Date | [today] |

  **Attendees**:

  | Role | Tier | Orientation |
  |------|------|-------------|
  [Load from charter. If no charter: PM — Advocate, Architect — Conditional,
   SRE — Challenger, Inertia-Advocate — Challenger]
  [Tier: Challenger (T1) / Conditional (T2) / Advocate (T3)]

  AMEND: If AMEND was invoked, add amended roles to the attendee table and note
  scope changes in the Agenda Item row before proceeding.

---

## INERTIA BRIEF

Before voices begin, print the status-quo cost of this agenda item.
This is mandatory — it is not optional context. It feeds directly into challenger voices.

  **Status Quo at Risk**:

  | Dimension | Current State | What Changes If Approved |
  |-----------|--------------|--------------------------|
  | Displaced workflow | [specific process or tool in production] | [what replaces it] |
  | Integration boundary | [named system, API, or contract] | [how the contract changes] |
  | Team habit | [team name — cognitive habit or muscle memory] | [what breaks] |
  | Switching cost | [non-obvious cost the sponsor did not anticipate] | [impact if ignored] |

  **Inertia verdict**: Is the switching cost genuinely non-obvious — something
  the sponsor would not have written in their own risk section?
    Answer: [YES / reason] or [NO — rewrite all four rows and retry until YES]

  INERTIA-BRIEF-SEALED: findings locked. Challenger voices must reference this table.

If no charter participant owns inertia/switching-cost investigation:
  INJECT: Inertia-Advocate into Tier 1 — speaks after sponsor presentation, before
  other challengers. Must cite at least one row from the Inertia Brief by dimension name.

---

## MEETING SIMULATION

### 1. SPONSOR PRESENTS

[The T3 role most aligned with the proposal presents the agenda item.]
[2-3 sentences: what is proposed, why now, what outcome is sought.]
[Do not raise objections. This is the proposal pitch.]

STANCE: APPROVE *(provisional — pending committee feedback)*

---

### 2. CHALLENGERS INTERROGATE (T1)

[Inertia-Advocate first if INJECTED, otherwise first T1 challenger from charter]

For each T1 challenger, print:

  **[Role Name]**
  STANCE: [BLOCK / CONDITION / APPROVE]
  [3-4 sentences grounded in their charter orientation]
  References: [dimension name from Inertia Brief] — [how this finding concerns them]

A T1 voice that does not reference the Inertia Brief has not done its job. Make the
connection explicit.

---

### 3. CONDITIONALS WEIGH IN (T2)

For each T2 participant, print:

  **[Role Name]**
  STANCE: CONDITION
  [2-3 sentences from their orientation]
  Condition: [specific artifact, threshold, or result required — not "address concerns"]

---

### 4. ADVOCATES AFFIRM (T3, minus sponsor)

For each T3 participant other than the presenting sponsor, print:

  **[Role Name]**
  STANCE: APPROVE
  [2-3 sentences]
  Acknowledges: [name the strongest challenger concern and explain why proposal survives it]

---

### 5. SPONSOR RESPONDS

[Sponsor speaks again: acknowledges the most significant BLOCK or CONDITION;
proposes how it will be resolved; 2-3 sentences]

STANCE: APPROVE *(confirmed)*

---

## TALLY

  | Stance | Count | Roles |
  |--------|-------|-------|
  | APPROVE | [N] | [names] |
  | CONDITION | [N] | [names] |
  | BLOCK | [N] | [names] |

  OUTCOME: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Derivation: all APPROVE → APPROVED; any CONDITION no BLOCK → APPROVED WITH CONDITIONS;
  any BLOCK → BLOCKED or DEFERRED.

---

## FORMAL MINUTES

### Decisions

  | Field | Value |
  |-------|-------|
  | Verdict | [OUTCOME] |
  | Effective date | [today or named milestone] |
  | Conditions | [specific deliverables; "none" if APPROVED] |
  | Re-entry owner | [named role; "n/a" if APPROVED] |
  | Re-entry trigger | [named artifact + recipient + authority; "n/a" if APPROVED] |

### Action Items

  | # | Owner | Action | Deadline |
  |---|-------|--------|----------|
  [one row per item; minimum one per unresolved CONDITION, minimum one for inertia follow-up
   if BLOCKED or if Inertia Brief identified a switching cost that was not resolved]

### Dissenting Opinions

  | Role | Objection | Inertia Brief Reference | Resolution Path | Authority | Trigger |
  |------|-----------|------------------------|-----------------|-----------|---------|
  [one row per BLOCK or unresolved CONDITION]
  [If no dissent: single row "None" — [reason]]

---

## PRE-MEETING RISK FLAG

This is the output's highest-value section. Name one risk the sponsor likely would not
have discovered without this simulation.

  | Field | Value |
  |-------|-------|
  | Risk | [specific, non-obvious, forward-looking] |
  | Source | [role that surfaced it] |
  | Why sponsor missed it | [one sentence] |
  | Recommended action | [one sentence] |

Generic risks ("timeline may slip", "adoption may be slow") do not qualify. Prefer
risks grounded in the Inertia Brief's switching cost or team habit row.

---

## CHARTER COMPLIANCE TABLE

(Mandatory if charter was loaded from `.craft/roles/`; skip if Signal defaults used.)

  | Charter Rule | Type | Honored? | Evidence |
  |-------------|------|----------|----------|
  [Row 1: e.g., quorum requirement — how many votes needed — met/not met]
  [Row 2: e.g., veto right — who holds it — exercised/not exercised]
  [Row 3+: scope boundary, escalation path, etc.]
  [Minimum two rows]

---

## COMMITTEE-TYPE REQUIREMENTS

Apply the relevant block. Do not produce a generic discussion.

**ROB**: Discussion (Challengers section) must include feature and metric readiness
evidence — specific numbers or named readiness gates. DECISIONS table must include a
`Readiness verdict` row: ready / not ready / conditional.

**Shiproom**: Discussion must surface a risk register. ACTION ITEMS must include an
explicit go/no-go gate item with owner and deadline.

**Arch-board**: Discussion must name at least two architectural alternatives. DECISIONS
table must include an `ADR summary` row listing rejected alternatives and the rationale
for the chosen direction.
```

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|-----------|
| V-01 | Role sequence — advocates-first | Mirrors real meeting dynamics; challengers react to a concrete pitch rather than front-loading objections |
| V-02 | Output format — table-structured | Tables make C-03/C-04/C-06 structurally impossible to omit; aids machine-readability |
| V-03 | Phrasing register — descriptive | Natural-language framing activates realistic voice simulation over protocol compliance |
| V-04 | Lifecycle emphasis (2-phase) + challengers-first | Reduces scaffolding overhead; keeps model focus on output quality with challenger tension preserved |
| V-05 | Full combination: presentation-before-challenge + tables + prominent inertia framing + imperative with voice guidance | Simultaneous optimization across rubric dimensions C-01–C-10 |
