# org:committee Variations — Round 4
Generated: 2026-03-16
Skill: org:committee
Rubric: simulations/quest/rubrics/org-committee-rubric-v4-2026-03-16.md

---

## V-01 — Lifecycle Emphasis: Three-Tier Sort Base + Investigation Phase with C-16/C-17

**Variation axis**: Lifecycle emphasis — R3 V-01 (three-tier sort, STANCE:, TALLY, no investigation) upgraded with a pre-meeting investigation phase, an explicit C-16 self-check gate, and the C-17 advocate-citation requirement
**Hypothesis**: R3 V-01 passed C-11/C-13/C-14/C-15 but carried no investigation phase, so it likely failed C-12, C-16, and C-17. Adding the investigation with a formal gate and requiring Tier 3 voices to cite named investigation findings should add all three aspirationals to V-01's already-passing base without disrupting its clean three-tier sort spine.

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

**Step 3 — Pre-Meeting Investigation**

This step runs before any participant speaks. Investigate what this agenda item would displace:

**(a) Current workflow**: Name the specific task, tool, or process this proposal replaces or changes. Concrete — not "current tooling" but the actual name and usage pattern.

**(b) Integration dependencies**: What existing integrations, APIs, contracts, or downstream systems would need to change? List by name.

**(c) Habit and mental model disruption**: What cognitive habits or workflow patterns would the most affected team need to change? Name the team.

**(d) Non-obvious cost**: Identify at least one switching cost unlikely to appear in the original proposal — something the author probably did not anticipate.

Output:

```
## SWITCHING-COST INVESTIGATION
(a) Current workflow: [specific name or description]
(b) Integration dependencies: [named list]
(c) Habit disruption: [specific habit, specific affected team]
(d) Non-obvious cost: [the surprise]
```

**C-16 Gate — self-check before proceeding**: Does item (d) name something that would surprise the proposal author? Answer explicitly: "YES — this is non-obvious because [reason]" or "NO — revising." If NO, deepen (a)–(c) and rewrite (d) before continuing. Do not proceed to Phase A until you can answer YES.

**Step 4 — Three-Tier Sort**

Before writing any voices, sort all loaded participants into tiers. Output the tier assignment as a labeled block before the voices begin.

**Tier 1 — CHALLENGERS**: Roles whose documented orientation creates structural skepticism — security, compliance, architecture purity, operational burden, status-quo defense. A role is Tier 1 if its role file describes a lens that interrogates feasibility, risk, or disruption to existing systems.

**Tier 2 — CONDITIONALS**: Roles whose support depends on specific named conditions being met. They hold until resolution.

**Tier 3 — ADVOCATES**: Roles whose orientation aligns with the proposal's stated goals. Tier 3 voices must (1) address at least one concern raised by Tier 1 or Tier 2 and (2) explicitly cite at least one named finding from Step 3 (by label — (a), (b), (c), or (d)) in their contribution.

**Tie-break within a tier**: Higher institutional veto authority speaks first.

Output tier assignment before any voice:

```
Tier 1 (CHALLENGERS): [roles]
Tier 2 (CONDITIONALS): [roles]
Tier 3 (ADVOCATES): [roles]
```

## Phase A — Participant Voices

Write voices in strict tier order: all Tier 1 → all Tier 2 → all Tier 3.

For each participant, the `STANCE:` line is a structural declaration — it must appear as a standalone line before any prose. Prose elaboration follows and must not soften, qualify, or contradict it.

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Tier 1 voices lead with the concern, not a concession. Tier 3 voices cite at least one Step 3 finding by label AND address at least one Tier 1 or Tier 2 concern before endorsing.]
```

**Enforcement**: At least one participant must declare CONDITION or BLOCK. A minutes record where all voices declare APPROVE on first pass is not a useful simulation.

## Phase B — Vote Tally

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
- Re-entry path for non-approval: what must change, who reviews, what evidence triggers re-review

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

## V-02 — Output Format: Full Template with C-16 GATE Field and C-17 Structural Subfield

**Variation axis**: Output format — R3 V-03 (fill-in-the-blank template) upgraded with (1) a C-16 GATE field as a required template line inside the investigation section, and (2) a `CITE:` structural subfield beneath the `STANCE:` declaration in every Tier 3 voice block
**Hypothesis**: R3 V-03 enforced format criteria structurally but likely failed C-16 and C-17 because neither criterion was a template field — they were prose instructions. Making C-16 a required labeled line ("GATE: YES — non-obvious because [reason]") and C-17 a required `CITE:` subfield below each Tier 3 `STANCE:` declaration makes them impossible to skip: the model must fill in both fields or the template is visibly incomplete.

---

You are simulating a committee meeting before the real one. Populate the template below exactly. Do not skip sections. Do not reorder sections. Do not merge sections. Where a field shows `[...]`, fill it with the required content.

---

```
# Committee Meeting Simulation
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
Participants loaded from: [path to charter file, or "Signal defaults — no charter found"]
Roles: [list every participant role name]

---

## SWITCHING-COST INVESTIGATION

(a) Current workflow displaced: [specific task, tool, or process — name it]
(b) Integration dependencies: [named list of systems, APIs, contracts affected]
(c) Habit disruption: [specific cognitive habit; specific team affected]
(d) Non-obvious cost: [the surprise finding — something the author did not anticipate]

GATE: [YES — this finding is non-obvious because [reason] / NO — revising investigation]

[If GATE is NO: rewrite (a)–(d) until GATE is YES before proceeding.]

---

## PARTICIPANT SORT

Tier 1 (CHALLENGERS): [roles whose orientation interrogates feasibility, risk, or status-quo disruption]
Tier 2 (CONDITIONALS): [roles that approve with named conditions]
Tier 3 (ADVOCATES): [roles aligned with the proposal's goals]

Tie-break (within tier): higher veto authority speaks first

---

## PARTICIPANT VOICES

[Write one block per participant in tier order: Tier 1 → Tier 2 → Tier 3.]

---

### [Role Name 1] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. The STANCE: line is the declaration. Prose follows and must not contradict or hedge it. Tier 1 voices lead with the concern. Tier 2 voices name the specific condition. Tier 3 voices address at least one Tier 1/Tier 2 concern before endorsing.]
[For Tier 3 only:] CITE: [investigation finding label and content — (a), (b), (c), or (d) — that supports this endorsement]

---

### [Role Name 2] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences...]
[For Tier 3 only:] CITE: [investigation finding label and content]

---

[Repeat block for each participant. At minimum: one participant must declare CONDITION or BLOCK.]

---

## TALLY
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK

---

## DECISIONS

Verdict: [approved / approved with conditions / blocked / deferred]
Conditions for full approval: [named specifically, or "none"]
Re-entry path (if not approved): [Owner Role] must [specific action] — committee re-reviews when [concrete condition]

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
  Objection: [substance of the objection, citable to their STANCE: rationale]
  Resolution path: [concrete condition — [authority role] decides when [condition is met]]

[If no dissent:]
No dissent — [one sentence: why consensus emerged]

---
```

**Rules applied while filling the template:**

1. Load participants from `.roles/` using the charter for this committee type. State the fallback if no charter exists.
2. Every named participant must come from the charter or Signal role files — do not invent roles.
3. The GATE field is mandatory. If the gate answer is NO, rewrite the investigation before filling any subsequent field.
4. The `STANCE:` line is the declaration. It must be a standalone line, not embedded in prose.
5. The `CITE:` subfield is required for every Tier 3 participant. A Tier 3 voice without a `CITE:` line fails C-17.
6. The TALLY: line must appear between the last voice and DECISIONS. Do not skip it.
7. At minimum: one participant must declare CONDITION or BLOCK.

---

## V-03 — Phrasing Register: Minimal Imperative (C-16/C-17 Precision, Maximum Compression)

**Variation axis**: Phrasing register — all R4 structural requirements (investigation, C-16 gate, three-tier sort, STANCE:, C-17 advocate citation, TALLY, formal minutes) in the smallest possible instruction surface; direct commands, no phase headers, no hypothesis framing
**Hypothesis**: R3 V-02 was the best scorer but is verbose. Verbose instruction prose increases the chance the model dilutes attention across paragraphs and loses a structural requirement mid-prompt. A minimal-register prompt with the same logical requirements but ~50% fewer words should produce equivalent structural compliance. If it scores the same, the shorter prompt is strictly better; if it scores lower, that identifies which instruction weight was load-bearing.

---

You are simulating a committee meeting before the real one.

**Open with:**
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.roles/` for this committee type's charter. Load every named role. If no charter: use Signal defaults (PM, Architect, Inertia-Advocate) and state them.

**Investigate before anyone speaks.** Name what this proposal displaces:

```
(a) Current workflow: [specific name — not generic]
(b) Integrations affected: [named list]
(c) Habit disruption: [what habit, which team]
(d) Non-obvious cost: [the surprise the author missed]
GATE: YES — non-obvious because [reason]
```

If you cannot write GATE: YES honestly, rewrite (a)–(d) until you can. Do not continue until the gate is satisfied.

**Sort participants before writing voices:**

```
Tier 1 (CHALLENGERS): [roles whose lens interrogates risk, feasibility, or disruption]
Tier 2 (CONDITIONALS): [roles that approve with conditions]
Tier 3 (ADVOCATES): [roles aligned with the proposal]
```

Within a tier, higher veto authority speaks first.

**Write voices in tier order: Tier 1 → Tier 2 → Tier 3.**

Each voice format — STANCE: is a standalone labeled line, prose follows:

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. Tier 1: lead with the concern. Tier 2: name the specific condition. Tier 3: address a Tier 1/Tier 2 concern AND cite one investigation finding by label.]
```

Rules:
- At least one voice must be CONDITION or BLOCK. All-APPROVE means roles are mis-sorted — fix it.
- Tier 3 voices that endorse without citing (a)/(b)/(c)/(d) fail C-17.
- Prose must not introduce a new stance or soften the declared one.

**After the last voice, before anything else:**

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

**Then the formal record:**

### DECISIONS
- Verdict: approved / approved with conditions / blocked / deferred
- Conditions (if any): named specifically
- Re-entry path (if not approved): [Owner Role] delivers [specific artifact] — re-review when [condition]

### ACTION ITEMS
```
[Owner Role] — [specific action] — [deadline]
```
No vague items. Every line: owner, deliverable, deadline.

### DISSENTING OPINIONS
For each dissent:
- Role, substance, resolution path (concrete condition + named authority)

If none: "No dissent — [one sentence on why consensus emerged]."

---

## V-04 — Inertia Framing: Investigation-First + Inertia Voice Grounded in Findings + C-17 Extended to Inertia Tags

**Variation axis**: Inertia framing — R3 V-04 (inertia-first mandatory speaker) upgraded with (1) a formal investigation phase preceding the inertia voice, (2) the inertia voice required to ground its critique in named investigation findings, (3) C-16 gate on the investigation, (4) C-17 extended to allow Tier 3 advocates to cite either investigation findings OR named INERTIA-FINDING tags
**Hypothesis**: R3 V-04 used INERTIA-FINDING tags as a proxy investigation. That proxy was weaker because it produced findings through a single adversarial lens rather than systematic displacement analysis. Grounding the inertia voice in a formal investigation phase first makes the inertia critique data-driven rather than role-driven — and gives the full committee a richer, independently-sourced citation pool for C-17 compliance.

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

## Phase 1 — Pre-Meeting Investigation

This phase runs before any participant speaks, including the inertia-advocate. It produces labeled findings that all subsequent voices draw from.

Investigate four dimensions:

**(a) Current workflow displaced**: Name the specific task, tool, or workflow this proposal changes or replaces. Be concrete.

**(b) Integration surface**: What integrations, APIs, contracts, or downstream consumers would need to change? Name them.

**(c) Habit disruption**: What cognitive habits or workflow patterns would the most affected team need to change? Name the team.

**(d) Non-obvious cost**: Identify at least one switching cost unlikely to appear in the original proposal — something the author probably did not anticipate.

Output:

```
## PRE-MEETING INVESTIGATION
(a) Current workflow: [specific description]
(b) Integration surface: [named list]
(c) Habit disruption: [specific habit, specific team]
(d) Non-obvious cost: [the surprise finding]

GATE: [YES — non-obvious because [reason] / NO — revising]
```

If GATE is NO: revise (a)–(d) and rewrite the block. Do not proceed until GATE is YES.

## Phase 2 — Inertia-Advocate Voice (Mandatory First Speaker)

The inertia-advocate speaks before all other participants. This is not optional.

The inertia-advocate's critique must be grounded in Phase 1 findings. Generic resistance that does not cite the investigation is insufficient — the inertia-advocate's role is to make the strongest evidence-based case for the status quo.

```
### Inertia-Advocate (Status-Quo Defense)
STANCE: [CONDITION / BLOCK — the inertia-advocate never freely approves on first pass]
[3-5 sentences building the specific case for doing nothing or delaying. Ground the critique in named Phase 1 findings — cite (a), (b), (c), or (d) by label. The inertia-advocate's voice sets the null hypothesis every other voice must beat.]

INERTIA-FINDING-A: [one-line summary of the strongest status-quo argument, traceable to Phase 1]
INERTIA-FINDING-B: [one-line summary of the second-strongest, traceable to Phase 1]
```

## Phase 3 — Remaining Participant Voices

After the inertia-advocate, all remaining participants speak. Sort them: skeptics before advocates within the remaining group (a role that interrogates risk speaks before a role that endorses).

For each participant:

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Must acknowledge at least one of INERTIA-FINDING-A or INERTIA-FINDING-B by name — rebutting it with specific evidence or conceding it as a condition. A voice that does not engage the inertia record has not done its job.]
```

**C-17 enforcement for Tier 3 (advocates)**: Tier 3 voices must additionally cite at least one Phase 1 investigation finding (by label — (a), (b), (c), or (d)) or one INERTIA-FINDING tag in their contribution. Endorsement that floats on generic role orientation without citing the investigation record fails.

**Enforcement**: At least one non-inertia participant must also declare CONDITION or BLOCK. The inertia-advocate alone does not satisfy the challenge requirement — the committee needs independent skepticism.

## Phase 4 — Vote Tally

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
- **Dissenting role**: named
- **Substance**: the specific objection
- **Resolution path**: concrete condition that resolves the objection, named authority who resolves it

The inertia-advocate's dissent must appear here if STANCE was CONDITION or BLOCK, with an explicit resolution path — what specifically satisfies the inertia case.

If no dissent: "No dissent — [one sentence explaining the consensus basis]."

---

## V-05 — Combined: Investigation with GATE Step + Three-Tier Sort + CITE: Subfield + Minimal Template + TALLY

**Variation axes**: Lifecycle emphasis (investigation + C-16 gate as a named GATE step) + role sequence (three-tier sort) + output format (structural `CITE:` subfield for Tier 3 per C-17) + phrasing register (minimal, no phase bloat)
**Hypothesis**: R3 V-05 was the full-combination attempt but predated C-16/C-17. Upgrading it with: (1) a visually distinct GATE step that outputs an explicit YES/NO before the sort, and (2) a `CITE:` structural subfield in each Tier 3 voice block — makes C-16 and C-17 as structurally enforced as C-15's `STANCE:` label. The GATE step cannot be elided without the output being visibly incomplete; the `CITE:` subfield cannot be skipped without leaving a labeled field blank. This is the 108-ceiling attempt.

---

You are simulating a committee meeting before the real one.

## Step 1 — Declare + Load

**Open with:**
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.roles/` for this committee type's charter. Load every named role. Fallback: Signal defaults (PM, Architect, Inertia-Advocate) — state them explicitly.

## Step 2 — Pre-Meeting Investigation

Before any participant speaks, investigate displacement:

```
## PRE-MEETING INVESTIGATION
(a) Current workflow: [specific name/description — not generic]
(b) Integration surface: [named list of affected systems, APIs, contracts]
(c) Habit disruption: [what changes, which team]
(d) Non-obvious cost: [the surprise — what the author likely missed]
```

## Step 3 — C-16 Gate

Immediately after the investigation block, output:

```
GATE: [YES — finding (d) is non-obvious because [specific reason it would not appear in a standard proposal] / NO — investigation insufficient, revising]
```

If GATE is NO: rewrite the investigation. Do not proceed to Step 4 until GATE is YES. This line is required; its absence means C-16 failed.

## Step 4 — Participant Sort

Sort all participants into three tiers. Output as a standalone block:

```
## PARTICIPANT SORT
Tier 1 (CHALLENGERS): [roles whose lens interrogates feasibility, risk, or disruption]
Tier 2 (CONDITIONALS): [roles that approve with named conditions]
Tier 3 (ADVOCATES): [roles aligned with the proposal]
Tie-break: within a tier, higher veto authority speaks first
```

## Step 5 — Participant Voices

Write voices in strict tier order: Tier 1 → Tier 2 → Tier 3.

**Voice format:**

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. Prose follows the STANCE: declaration; it must not introduce a new stance or hedge the declared one.
  Tier 1: lead with the specific concern; may reference investigation findings by label.
  Tier 2: name the specific condition; ground it in investigation findings or the agenda item.
  Tier 3: address at least one Tier 1/Tier 2 concern before endorsing.]
CITE: [Tier 3 only — investigation finding label (a/b/c/d) + brief content that supports the endorsement]
```

**Rules:**
- `CITE:` is required for every Tier 3 voice. A Tier 3 block without `CITE:` fails C-17.
- At minimum: one voice must be CONDITION or BLOCK. All-APPROVE → re-sort.
- Prose must not soften or contradict the `STANCE:` declaration above it.

## Step 6 — Vote Tally

After the last voice, before any other section, output exactly:

```
TALLY: [N] APPROVE · [N] CONDITION · [N] BLOCK
```

Do not skip. Do not embed in prose.

## Step 7 — Formal Minutes

### DECISIONS

```
Verdict: [approved / approved with conditions / blocked / deferred]
Conditions: [named specifically, or "none"]
Re-entry path: [Owner Role] delivers [specific artifact] — re-review when [concrete condition]
```

### ACTION ITEMS

```
[Owner Role] — [specific action] — [deadline]
[Owner Role] — [specific action] — [deadline]
```

Every item: named owner, specific deliverable, deadline. Vague items fail.

### DISSENTING OPINIONS

```
[If dissent:]
Role: [name]
Objection: [specific substance, citable to STANCE: rationale]
Resolution path: [concrete condition — [authority role] decides when [condition met]]

[If no dissent:]
No dissent — [one sentence: why consensus emerged]
```
