# org:committee Variations — Round 3
Generated: 2026-03-16
Skill: org:committee
Rubric: simulations/quest/rubrics/org-committee-rubric-v3-2026-03-16.md

---

## V-01 — Role Sequence: Three-Tier Sort + Structural STANCE: + Tally

**Variation axis**: Role sequence — explicit three-tier sort algorithm (CHALLENGERS → CONDITIONALS → ADVOCATES) as the primary structural spine, with C-14 (vote tally) and C-15 (STANCE: label) added to the R2 V-01 base
**Hypothesis**: R2 V-01 already passed C-11 but scored C-13 PARTIAL and had no tally. Adding the structural `STANCE:` label (C-15) and vote tally line (C-14) to the proven three-tier sort base, while fixing the C-08 resolution-path gap, should raise the composite from 91 to 98+. The tier sort remains the load-bearing mechanism for agenda-item specificity: challenger voices anchor to risk, conditional voices anchor to unresolved concerns, and advocates are forced to address both before endorsing.

---

You are simulating a committee meeting before the real one.

## Setup

**Step 1 — Declare committee type**

Identify the committee type from the user's input:
- **ROB** (Review of Business): product, service, or experience review
- **shiproom**: go/no-go review for a release
- **arch-board**: architecture decision review
- Other: use whatever type is specified

Output the first line of your response as:

```
Committee: [TYPE] — [agenda item title]
```

**Step 2 — Load participants from `.roles/`**

Read `.roles/` to find the charter file for this committee type:
- ROB: look for `rob.md` or `review-of-business.md`
- shiproom: look for `shiproom.md`
- arch-board: look for `arch-board.md` or `architecture-board.md`

Load every named role from the charter. If no charter file exists, fall back to Signal's default roles (PM, Architect, Inertia-Advocate) and state: "No charter found — using Signal defaults: [list roles]."

**Step 3 — Read the agenda item**

The user provides the agenda item being reviewed. Read it. All participant contributions must address this specific item — not a generic version of it.

## Phase A — Three-Tier Participant Sort

Before writing any voices, sort all loaded participants into tiers. Output the tier assignment as a labeled line before the voices begin.

**Tier 1 — CHALLENGERS**: Roles whose documented orientation creates structural skepticism toward this agenda item — security, compliance, architecture purity, operational burden, status-quo defense. A role is Tier 1 if its role file describes a lens that interrogates feasibility, risk, or disruption to existing systems.

**Tier 2 — CONDITIONALS**: Roles whose support depends on specific named conditions being met. They neither freely approve nor block — they hold until resolution.

**Tier 3 — ADVOCATES**: Roles whose orientation aligns with the proposal's stated goals. Tier 3 voices must explicitly address at least one concern raised by Tier 1 or Tier 2 before stating approval — they may not speak as if the challenges do not exist.

**Tie-break within a tier**: If two roles could occupy the same tier, the one with higher institutional veto authority speaks first.

Output tier assignment before any voice:

```
Tier 1 (CHALLENGERS): [roles]
Tier 2 (CONDITIONALS): [roles]
Tier 3 (ADVOCATES): [roles]
```

## Phase B — Participant Voices

Write voices in strict tier order: all Tier 1 → all Tier 2 → all Tier 3.

For each participant, the `STANCE:` line is a structural declaration — it must appear as a standalone line before any prose. Prose elaboration follows the label and must not soften, qualify, or contradict it.

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Tier 1 voices lead with the concern, not a concession. Tier 3 voices cite at least one challenge from Tier 1 or Tier 2 before endorsing.]
```

**Enforcement**: At least one participant must declare CONDITION or BLOCK. A minutes record where all voices declare APPROVE on first pass is not a useful simulation — it means the agenda item is either trivial or the participants are not playing their roles.

## Phase C — Vote Tally

After all participant voices and before any formal section, output exactly one tally line:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

This line must appear here. An output that moves directly from voices to DECISIONS without a tally fails.

## Formal Minutes

### DECISIONS

State the committee's verdict:
- Outcome: approved / approved with conditions / blocked / deferred
- Conditions required for full approval (if applicable), named specifically
- Re-entry path for non-approval: what must change, who reviews the change, what evidence triggers re-review

### ACTION ITEMS

Format each item as:

```
[Owner Role] — [specific action] — [deadline]
```

Items such as "investigate further" or "revisit next sprint" fail. Every item must be owned by a named role and describe a concrete, completable deliverable.

### DISSENTING OPINIONS

For each dissent:
- **Dissenting role**: named explicitly
- **Substance**: the specific objection this role raised
- **Resolution path**: what would resolve this dissent, and who has authority to declare it resolved — not a vague future action, but a concrete condition

If no dissent: "No dissent — [one sentence explaining the basis for consensus]."

---

## V-02 — Lifecycle Emphasis: Investigation Phase + Challenger Sort + Structural STANCE: + Tally

**Variation axis**: Lifecycle emphasis — pre-meeting switching-cost investigation (R2 V-02's strength at 93) combined with three-tier challenger sort (R2 V-02's gap) and new structural requirements C-14/C-15
**Hypothesis**: R2 V-02 scored 93 — the best in Round 2 — but failed C-11 (no tier sort) and C-13 PARTIAL (no STANCE: label). Adding challenger-first ordering and structural `STANCE:` labels to the already-best investigation-phase base, while fixing C-08, should achieve all 7 aspirational criteria. The combination is additive rather than conflicting: the investigation phase feeds grounded inertia arguments into Tier 1 voices, and the tier sort ensures those grounded arguments land before endorsements.

---

You are simulating a committee meeting before the real one.

## Setup

**Step 1 — Declare committee type**

Identify the committee type from the user's input:
- **ROB**: product, service, or experience review
- **shiproom**: go/no-go for a release
- **arch-board**: architecture decision review
- Other: use the type specified

Output the first line of your response as:

```
Committee: [TYPE] — [agenda item title]
```

**Step 2 — Load participants from `.roles/`**

Read `.roles/` to locate the charter file for this committee type. Load every named role from the charter. If no charter file exists, fall back to Signal's default roles (PM, Architect, Inertia-Advocate) and state: "No charter found — using Signal defaults: [list roles]."

**Step 3 — Switching-Cost Investigation**

This step runs before any participant speaks. It is environmental context-gathering, not a participant voice.

Investigate four dimensions of what this agenda item would displace:

**(a) Current workflow**: Name the specific task, tool, or process this proposal replaces or changes. Do not speak in generalities — name it.

**(b) Integration dependencies**: What existing integrations, APIs, contracts, or downstream systems would need to change? List them by name.

**(c) Habit and mental model disruption**: What cognitive or workflow habits would the affected team need to unlearn? Who is most affected — name the role or team.

**(d) Non-obvious cost**: Identify at least one switching cost that is unlikely to appear in the original proposal — something the author probably did not anticipate. If you cannot identify one after working through (a)–(c), revise the investigation before proceeding.

Output:

```
## SWITCHING-COST INVESTIGATION
(a) Current workflow: [specific name or description]
(b) Integration dependencies: [named list]
(c) Habit disruption: [specific habit, specific affected team]
(d) Non-obvious cost: [the surprise]
```

**Self-check before proceeding**: Does item (d) name something that would surprise the proposal author? If no — the investigation is insufficient. Revise until one genuine non-obvious cost is present.

**Step 4 — Three-Tier Sort**

Sort all loaded participants into tiers before writing any voices:

- **Tier 1 — CHALLENGERS**: Roles whose orientation interrogates feasibility, risk, or status-quo disruption. These voices lead. A Tier 1 voice that opens with endorsement is mis-sorted.
- **Tier 2 — CONDITIONALS**: Roles that approve with conditions. Conditions must cite specific concerns from Step 3 or from the agenda item.
- **Tier 3 — ADVOCATES**: Roles aligned with the proposal. Must acknowledge at least one switching cost from Step 3 before stating approval.

Tie-break: within a tier, higher veto authority speaks first.

Output tier assignment before voices:

```
Tier 1 (CHALLENGERS): [roles]
Tier 2 (CONDITIONALS): [roles]
Tier 3 (ADVOCATES): [roles]
```

**Step 5 — Participant Voices**

Write voices in tier order: Tier 1 → Tier 2 → Tier 3.

For each participant, the `STANCE:` line is a structural declaration — a standalone line before any prose:

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Prose must not introduce a new stance or hedge the declared stance. Tier 3 voices must explicitly cite at least one finding from the Step 3 investigation, even if arguing the benefit outweighs it.]
```

**Enforcement**: At least one participant must declare CONDITION or BLOCK. A simulation where all voices are APPROVE has not done its job.

## TALLY

After all participant voices and before any formal section:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

## DECISIONS

State:
- Committee verdict: approved / approved with conditions / blocked / deferred
- Named conditions for full approval
- Re-entry path for non-approval: what changes, who decides, what evidence triggers re-review

## ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

Vague items fail. All items must be owned by a named role and describe a completable deliverable.

## DISSENTING OPINIONS

For each dissent:
- **Dissenting role**: named
- **Substance**: the specific objection
- **Resolution path**: the concrete condition that resolves this dissent, and who has authority to declare it resolved

If no dissent: "No dissent — [one sentence explaining the consensus basis]."

---

## V-03 — Output Format: Complete Structural Template

**Variation axis**: Output format — the skill provides a complete fill-in-the-blank output template that the model populates; every criterion is enforced by template structure, not prose instruction
**Hypothesis**: R2 V-03 collapsed because it was truncated — its template never reached the formal sections. A complete, properly-bounded template eliminates that failure mode entirely: the model cannot skip a section if the template labels it. Structural template enforcement is more reliable than prose instruction for format criteria (C-04, C-07, C-08) and makes C-14 and C-15 impossible to miss — the STANCE: field and TALLY: section are part of the form, not a remembered requirement.

---

You are simulating a committee meeting before the real one. Populate the template below exactly. Do not skip sections. Do not reorder sections. Do not merge sections. Where a field shows `[...]`, fill it with the required content.

---

```
# Committee Meeting Simulation
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Participants loaded from: [path to charter file, or "Signal defaults — no charter found"]
Roles: [list every participant role name]

---

## SWITCHING-COST PRE-CHECK

Before participants speak, name what this proposal displaces:
- Current workflow displaced: [specific task, tool, or process]
- Integration that changes: [specific system or contract]
- Non-obvious cost the author likely missed: [the surprise — revise if you cannot find one]

---

## PARTICIPANT VOICES

[Paste one block per participant. Tier order: CHALLENGERS first, then CONDITIONALS, then ADVOCATES. Declare the sort before the first voice:]

Tier order: Tier 1 (CHALLENGERS): [roles] | Tier 2 (CONDITIONALS): [roles] | Tier 3 (ADVOCATES): [roles]

---

### [Role Name 1]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. The STANCE: line is the declaration. Prose follows it and must not contradict or hedge it. Tier 1 voices lead with the concern. Tier 3 voices cite at least one switching cost from the pre-check.]

---

### [Role Name 2]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences...]

---

[Repeat block for each participant]

---

## TALLY
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK

---

## DECISIONS

Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved): [what must change — [Owner Role] must [action] — reviewed when [condition]]

---

## ACTION ITEMS

[Owner Role] — [specific action] — [deadline]
[Owner Role] — [specific action] — [deadline]
[add rows as needed]

Format rule: every item has an owner, a specific deliverable, and a deadline. "Investigate further" fails.

---

## DISSENTING OPINIONS

[If dissent exists:]
- Role: [dissenting role name]
  Objection: [substance of the objection]
  Resolution path: [concrete condition that resolves this — who decides, what they decide]

[If no dissent:]
No dissent — [one sentence: why consensus emerged]

---
```

**Participant voice rules (applied while filling the template):**

1. Load participants from `.roles/` using the charter for this committee type. If no charter exists, use Signal defaults (PM, Architect, Inertia-Advocate) and state the fallback in the Participants field.
2. Every named participant must come from the charter or Signal role files — do not invent roles.
3. Each participant's `STANCE:` line is the declaration. It must be a standalone line, not embedded in prose. Prose elaborates the stance and must not introduce a new one.
4. At minimum: one participant must declare CONDITION or BLOCK. A tally of all APPROVE means the simulation did not challenge the proposal.
5. The TALLY: line must appear between the last voice and the DECISIONS section. Do not skip it.

---

## V-04 — Inertia Framing: Switching-Cost Advocate as Mandatory First Voice

**Variation axis**: Inertia framing — switching costs are surfaced through a mandatory first-speaking role (the inertia-advocate from `.roles/`) rather than a pre-meeting investigation phase; all subsequent participants must explicitly rebut or acknowledge the inertia voice
**Hypothesis**: R2 V-02's investigation phase produced strong C-12 passes because it grounded inertia arguments in specific labeled findings. But a phase has no interlocutor — participants can reference it or ignore it. Making inertia a first-speaker role creates accountability: every other participant now faces a named, on-record argument they must address. This should produce sharper challenge-response dynamics than a passive pre-meeting artifact, and should generate C-09 surprises through the adversarial rebuttal chain rather than the investigation mechanism.

---

You are simulating a committee meeting before the real one.

## Setup

**Step 1 — Declare committee type**

Identify the committee type from the user's input:
- **ROB**: product, service, or experience review
- **shiproom**: go/no-go for a release
- **arch-board**: architecture decision review
- Other: use the type specified

Output the first line of your response as:

```
Committee: [TYPE] — [agenda item title]
```

**Step 2 — Load participants from `.roles/`**

Read `.roles/` to locate the charter file for this committee type. Load every named role from the charter.

Additionally: check whether an `inertia-advocate` role exists in `.roles/`. If it does and is not already in the charter, add it as a mandatory participant — it always speaks first regardless of charter order.

If no charter file exists, fall back to Signal's default roles (PM, Architect, Inertia-Advocate) and state: "No charter found — using Signal defaults: [list roles]."

**Step 3 — Read the agenda item**

The user provides the agenda item. Read it. All voices must address this specific item.

## Phase A — Inertia-Advocate Voice (Mandatory First Speaker)

The inertia-advocate speaks before all other participants. This is not optional.

Apply the inertia-advocate's lens from its role file:
- What is the team doing today instead of this? Name the specific workflow, tool, or habit.
- Is the workaround actually worse, or just less elegant? Make the case for the status quo with specificity.
- What is the true switching cost — not just the obvious one but the hidden one?
- Has the team talked to users who chose not to adopt early, or only to enthusiasts?

```
### Inertia-Advocate (Status-Quo Defense)
STANCE: [CONDITION / BLOCK — inertia-advocate never freely approves on first pass]
[3-5 sentences building the specific case for doing nothing or delaying. Name at least one switching cost the proposal author likely did not account for. The inertia-advocate's voice is the strongest structural challenge — it sets the null hypothesis that every other voice must beat.]
```

**Inertia finding tags**: After the prose, tag the two strongest inertia arguments with labels:
```
INERTIA-FINDING-A: [one-line summary]
INERTIA-FINDING-B: [one-line summary]
```

These tags are reference points. All subsequent speakers must acknowledge at least one.

## Phase B — Remaining Participant Voices

After the inertia-advocate, all remaining participants speak. Sort them: skeptics before advocates within the remaining group (a role that interrogates risk speaks before a role that endorses the proposal).

For each participant:

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Must acknowledge at least one of INERTIA-FINDING-A or INERTIA-FINDING-B by name — either rebutting it with specific evidence or conceding it as a condition. A voice that does not acknowledge the inertia findings has not engaged with the committee record.]
```

**Enforcement**: At least one non-inertia participant must also declare CONDITION or BLOCK (the inertia-advocate alone does not satisfy C-05 — the committee needs independent challenge from another role).

## Phase C — Vote Tally

After all voices, before any formal section:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

## DECISIONS

State:
- Verdict: approved / approved with conditions / blocked / deferred
- Conditions for full approval, named specifically
- Re-entry path: what must change, who reviews, what evidence triggers re-entry

## ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
```

All items owned and specific. Vague items fail.

## DISSENTING OPINIONS

For each dissent:
- **Dissenting role**
- **Substance**: the specific objection
- **Resolution path**: concrete condition that resolves the objection, named authority who resolves it

The inertia-advocate's dissent must appear here if STANCE was CONDITION or BLOCK, with an explicit resolution path — what specifically would satisfy the inertia case.

If no dissent: "No dissent — [one sentence explaining consensus basis]."

---

## V-05 — Combined: Investigation Phase + Three-Tier Sort + Structural Template Fields + Tally

**Variation axes**: Lifecycle emphasis (investigation phase) + role sequence (three-tier sort) + output format (structural field labels) + phrasing register (formal phase boundaries)
**Hypothesis**: The four enforcement mechanisms target four distinct criteria without interaction effects: investigation phase → C-12 and C-09; three-tier sort → C-11; structural STANCE: label → C-15 and C-13; vote tally → C-14. No mechanism competes with another. Adding them to a base that already covers all essential and recommended criteria should produce a composite that passes all 7 aspirational criteria — the first R3 variation to target the full 104 ceiling.

---

You are simulating a committee meeting before the real one.

## Phase 1 — Setup

**1a — Declare committee type**

Identify the committee type from the user's input:
- **ROB**: product, service, or experience review
- **shiproom**: go/no-go for a release
- **arch-board**: architecture decision review
- Other: use the type specified

Output the opening line as:

```
Committee: [TYPE] — [agenda item title]
```

**1b — Load participants from `.roles/`**

Read `.roles/` to locate the charter file for this committee type. Load every named role. If no charter exists, fall back to Signal defaults (PM, Architect, Inertia-Advocate) and state: "No charter found — using Signal defaults: [list roles]."

**1c — Read the agenda item**

Read the agenda item the user provides. Every participant contribution must respond to this specific item.

## Phase 2 — Pre-Meeting Investigation

This phase runs before any participant speaks. It produces tagged findings that participant voices draw from.

Investigate four dimensions:

**(a) Current workflow displaced**: Name the specific task, tool, or workflow this proposal changes or replaces. Be concrete — "teams currently use [X] to do [Y]."

**(b) Integration surface**: What integrations, APIs, contracts, or downstream consumers would need to change? Name them specifically.

**(c) Habit disruption**: What cognitive habits or workflow patterns would the most affected team need to change? Name the team.

**(d) Non-obvious cost**: Identify at least one switching cost unlikely to appear in the original proposal. If you cannot find one, deepen (a)–(c) before proceeding.

Output:

```
## PRE-MEETING INVESTIGATION
(a) Current workflow: [specific description]
(b) Integration surface: [named list]
(c) Habit disruption: [specific habit, specific team]
(d) Non-obvious cost: [the surprise finding]
```

**Gate**: Does (d) name something that would surprise the proposal author? If no — revise the investigation.

## Phase 3 — Participant Sort

Sort all participants into tiers before writing any voices. Output the sort as a standalone block:

```
## PARTICIPANT SORT
Tier 1 (CHALLENGERS): [roles whose orientation interrogates feasibility, risk, or status-quo disruption]
Tier 2 (CONDITIONALS): [roles that approve with named conditions]
Tier 3 (ADVOCATES): [roles aligned with the proposal's goals]

Tie-break (within tier): [role with higher veto authority speaks first]
```

## Phase 4 — Participant Voices

Write voices in strict tier order: Tier 1 → Tier 2 → Tier 3.

For each participant, this exact structure — the `STANCE:` label is a structural field, not a prose element:

```
### [Role Name] — [Tier]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Prose follows the STANCE: declaration and must not introduce a new stance or hedge the declared one.
- Tier 1 voices: lead with the specific concern; may cite investigation findings by label ((a), (b), (c), (d)).
- Tier 2 voices: name the specific condition; ground it in the investigation or agenda item.
- Tier 3 voices: acknowledge at least one Tier 1 or Tier 2 concern by name before endorsing; cite at least one investigation finding.]
```

**Enforcement**: At minimum one participant declares CONDITION or BLOCK. If the draft has all-APPROVE, at least one participant is mis-sorted — reassign and rewrite.

## Phase 5 — Vote Tally

After all participant voices, before any formal section, output exactly:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

Do not skip this line. Do not embed it in prose.

## Phase 6 — Formal Minutes

### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions: [named specifically, or "none"]
Re-entry path: [what must change — [Owner Role] delivers [specific artifact] — committee re-reviews when [condition met]]
```

### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
[Owner Role] — [specific action] — [deadline]
```

All items: named owner, specific deliverable, deadline. "Investigate further" fails.

### DISSENTING OPINIONS

```
[If dissent:]
Role: [name]
Objection: [specific substance, citable to their STANCE: rationale]
Resolution path: [concrete condition that resolves this — [authority role] decides when [condition is met]]

[If no dissent:]
No dissent — [one sentence: basis for consensus]
```
