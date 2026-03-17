# org:committee Variations — Round 5
Generated: 2026-03-16
Skill: org:committee
Rubric: v5 (C-18 all-approve self-correction diagnostic; C-19 Tier 3 addresses named Tier 1/2 concern; aspirational pool 11 criteria, max 112)

---

## V-01 — Lifecycle Emphasis: Sort Validation Gate + `RESPONDS-TO:` Subfield

**Variation axis**: Lifecycle emphasis — R4 V-01 base (investigation + GATE + three-tier sort + STANCE: + CITE: + TALLY) upgraded with (1) an explicit sort validation step between the tier sort and the first voice, and (2) a `RESPONDS-TO:` structural subfield paired with `CITE:` in each Tier 3 voice block
**Hypothesis**: R4 V-01 carried C-18 only as a prose enforcement note ("A minutes record where all voices declare APPROVE on first pass is not a useful simulation") and C-19 only as a voice instruction ("Tier 3 voices cite at least one Step 3 finding by label AND address at least one Tier 1 or Tier 2 concern"). Neither was a named checkpoint. Elevating C-18 to a named sort validation step — parallel in structure to the C-16 Gate — makes all-APPROVE detection a mandatory output line the model cannot skip. Elevating C-19 to a `RESPONDS-TO:` labeled subfield — parallel in structure to `CITE:` — makes peer-responsiveness as structurally enforced as investigation citation. Both additions follow the pattern established for C-15 (`STANCE:`), C-14 (TALLY), and C-16 (GATE): enforcement through labeled declarations the model cannot elide without leaving a visible blank.

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

**Step 2 — Load participants from `.craft/roles/`**

Read `.craft/roles/` to find the charter file for this committee type:
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

**C-16 Gate — self-check before proceeding**: Does item (d) name something that would surprise the proposal author? Answer explicitly: "YES — this is non-obvious because [reason]" or "NO — revising." If NO, deepen (a)–(c) and rewrite (d) before continuing. Do not proceed to Step 4 until you can answer YES.

**Step 4 — Three-Tier Sort**

Before writing any voices, sort all loaded participants into tiers. Output the tier assignment as a labeled block.

**Tier 1 — CHALLENGERS**: Roles whose documented orientation creates structural skepticism — security, compliance, architecture purity, operational burden, status-quo defense. A role is Tier 1 if its role file describes a lens that interrogates feasibility, risk, or disruption to existing systems.

**Tier 2 — CONDITIONALS**: Roles whose support depends on specific named conditions being met. They hold until resolution.

**Tier 3 — ADVOCATES**: Roles whose orientation aligns with the proposal's stated goals.

**Tie-break within a tier**: Higher institutional veto authority speaks first.

Output tier assignment:

```
Tier 1 (CHALLENGERS): [roles]
Tier 2 (CONDITIONALS): [roles]
Tier 3 (ADVOCATES): [roles]
```

**Step 4b — Sort Validation**

Immediately after the tier assignment block, output:

```
SORT-CHECK: [All-APPROVE detected — Tier 1 and Tier 2 both empty? YES — [role] is mis-sorted; reassigning to Tier [1/2] because [specific reason given this agenda item]; revised sort follows / NO — valid sort, proceeding]
```

If SORT-CHECK is YES: re-output the corrected tier assignment block before Phase A. Do not write any voices until SORT-CHECK confirms a valid sort (at least one Tier 1 or Tier 2 participant exists).

## Phase A — Participant Voices

Write voices in strict tier order: all Tier 1 → all Tier 2 → all Tier 3.

For each participant, the `STANCE:` line is a structural declaration — it must appear as a standalone line before any prose. Prose elaboration follows and must not soften, qualify, or contradict it.

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Tier 1 voices lead with the concern, not a concession. Tier 2 voices name the specific condition. Tier 3 voices must complete both subfields below before any endorsement prose.]
[Tier 3 only:] CITE: [investigation finding label — (a), (b), (c), or (d) — and the specific content that supports this endorsement]
[Tier 3 only:] RESPONDS-TO: [name the specific Tier 1 or Tier 2 concern being addressed — quote or paraphrase the concern, then state in one sentence how this endorsement addresses it]
```

**Enforcement**: At least one participant must declare CONDITION or BLOCK. If the draft produces all-APPROVE, at least one participant is mis-sorted — return to Step 4 and reassign.

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

## V-02 — Output Format: Template with `SORT-CHECK:` Field + `RESPONDS-TO:` Subfield

**Variation axis**: Output format — R4 V-02 template base (GATE field + CITE: subfield already structural) upgraded with (1) a `SORT-CHECK:` template field inserted between the PARTICIPANT SORT block and the PARTICIPANT VOICES section, and (2) a `RESPONDS-TO:` subfield added to the Tier 3 voice template block alongside the existing `CITE:` subfield
**Hypothesis**: R4 V-02 proved that making a criterion a template field — not a prose instruction — is the most reliable enforcement mechanism. The GATE field enforced C-16; the CITE: field enforced C-17. C-18 and C-19 receive the same treatment here. `SORT-CHECK:` is a required template line between the sort and voices: the model must fill it or the template is visibly incomplete. `RESPONDS-TO:` is a required subfield in every Tier 3 block: a Tier 3 block missing it has an unfilled template field. Both additions preserve R4 V-02's structural enforcement philosophy while targeting the two new aspirational criteria with maximum precision.

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

SORT-CHECK: [Tier 1 and Tier 2 both empty (all-APPROVE)? YES — [role] is mis-sorted; correcting to Tier [1/2] because [reason]; revised sort below / NO — valid sort, proceed]

[If SORT-CHECK is YES: re-output the corrected tier block above before any voice block.]

---

## PARTICIPANT VOICES

[Write one block per participant in tier order: Tier 1 → Tier 2 → Tier 3.]

---

### [Role Name 1] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. The STANCE: line is the declaration. Prose follows and must not contradict or hedge it. Tier 1 voices lead with the concern. Tier 2 voices name the specific condition. Tier 3 voices must complete both CITE: and RESPONDS-TO: before any endorsement prose.]
[For Tier 3 only:] CITE: [investigation finding label and content — (a), (b), (c), or (d) — that supports this endorsement]
[For Tier 3 only:] RESPONDS-TO: [name the Tier 1 or Tier 2 concern being addressed — quote or paraphrase the specific concern, then state how this endorsement responds to it]

---

### [Role Name 2] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences...]
[For Tier 3 only:] CITE: [investigation finding label and content]
[For Tier 3 only:] RESPONDS-TO: [Tier 1 or Tier 2 concern name and response]

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

1. Load participants from `.craft/roles/` using the charter for this committee type. State the fallback if no charter exists.
2. Every named participant must come from the charter or Signal role files — do not invent roles.
3. The GATE field is mandatory. If GATE is NO, rewrite the investigation before filling any subsequent field.
4. The SORT-CHECK field is mandatory. If SORT-CHECK is YES, revise the sort and re-output the tier block before filling any voice blocks.
5. The `STANCE:` line is the declaration. It must be a standalone line, not embedded in prose.
6. The `CITE:` subfield is required for every Tier 3 participant. A Tier 3 voice without `CITE:` fails C-17.
7. The `RESPONDS-TO:` subfield is required for every Tier 3 participant. It must name a specific concern raised by a Tier 1 or Tier 2 voice — a generic acknowledgment of opposition does not pass. A Tier 3 voice without `RESPONDS-TO:` fails C-19.
8. The TALLY: line must appear between the last voice and DECISIONS. Do not skip it.
9. At minimum: one participant must declare CONDITION or BLOCK.

---

## V-03 — Phrasing Register: Minimal Imperative with Inline C-18/C-19 Commands

**Variation axis**: Phrasing register — R4 V-03 (all structural requirements in minimal-register prose) upgraded with C-18 as a named inline diagnostic command appended to the sort instruction, and C-19 as a compact dual-requirement in the Tier 3 voice line
**Hypothesis**: R4 V-03 demonstrated that minimal-register prompts achieve structural compliance equivalent to verbose prompts. C-18 and C-19 are small enough additions that they do not materially grow the instruction surface: C-18 becomes a single diagnostic command after the sort block ("All-APPROVE means mis-sorted — detect it, name the mis-sorted role, revise the tier block, output SORT-CHECK before proceeding"), and C-19 becomes a two-part requirement appended to the Tier 3 instruction ("cite one investigation finding AND name + respond to a Tier 1/2 concern"). The minimal register prevents attention dilution; the inline placement makes both requirements visible in context rather than buried in rules sections the model may deprioritize.

---

You are simulating a committee meeting before the real one.

**Open with:**
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.craft/roles/` for this committee type's charter. Load every named role. If no charter: use Signal defaults (PM, Architect, Inertia-Advocate) and state them.

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

**Sort validation.** After outputting the sort, check: are Tier 1 and Tier 2 both empty? If yes — all participants are advocates and the sort is structurally wrong. Identify which role most naturally interrogates risk or requires conditions for this specific agenda item. Reassign it. Re-output the tier block. Then output:

```
SORT-CHECK: [role reassigned to Tier [1/2] — [reason specific to this agenda item] / NO all-APPROVE — valid sort, proceed]
```

Do not write any voices until SORT-CHECK is output.

**Write voices in tier order: Tier 1 → Tier 2 → Tier 3.**

Each voice format — `STANCE:` is a standalone labeled line, prose follows:

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. Prose follows STANCE:; it must not introduce a new stance or soften the declared one.
  Tier 1: lead with the concern.
  Tier 2: name the specific condition.
  Tier 3: (1) cite one investigation finding by label — (a), (b), (c), or (d) — AND (2) name a specific Tier 1 or Tier 2 concern and state how this endorsement responds to it.]
```

Rules:
- At least one voice must be CONDITION or BLOCK. All-APPROVE means roles are mis-sorted — fix it.
- Tier 3 voices that endorse without citing an investigation finding fail C-17.
- Tier 3 voices that endorse without naming and responding to a Tier 1/2 concern fail C-19.
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

## V-04 — Inertia Framing: Inertia Finding Tags as C-19 Anchor + Remaining Sort Validation

**Variation axis**: Inertia framing — R4 V-04 base (inertia-advocate mandatory first speaker + formal investigation + GATE + C-17 extended to inertia tags) upgraded with (1) C-18 applied as a validation check on the remaining-participants sort after the inertia-advocate speaks, and (2) the inertia-advocate's INERTIA-FINDING tags made the primary named Tier 1 concerns that all advocate voices must explicitly address for C-19
**Hypothesis**: The inertia framing creates a natural C-19 anchor without requiring a separate `RESPONDS-TO:` subfield. The inertia-advocate's INERTIA-FINDING-A and INERTIA-FINDING-B tags are already named, labeled concerns on the committee record. If advocate voices are required to name and respond to at least one tag by label, C-19 is satisfied through the inertia architecture — and arguably produces richer C-19 passes because advocates are responding to the strongest adversarial case rather than the most convenient Tier 2 condition. C-18 is applied to the remaining-participants sort (excluding the inertia-advocate, who always speaks first): if no remaining participant is sorted as a skeptic, that is a structural sorting error requiring correction before any remaining voice is written.

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

**Step 2 — Load participants from `.craft/roles/`**

Read `.craft/roles/` to locate the charter file for this committee type. Load every named role from the charter.

Additionally: check whether an `inertia-advocate` role exists in `.craft/roles/`. If it does and is not already in the charter, add it as a mandatory participant — it always speaks first regardless of charter order.

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

The inertia-advocate's critique must be grounded in Phase 1 findings. Generic resistance that does not cite the investigation is insufficient — the inertia-advocate makes the strongest evidence-based case for the status quo.

```
### Inertia-Advocate (Status-Quo Defense)
STANCE: [CONDITION / BLOCK — the inertia-advocate never freely approves on first pass]
[3-5 sentences building the specific case for doing nothing or delaying. Ground the critique in named Phase 1 findings — cite (a), (b), (c), or (d) by label. The inertia-advocate's voice sets the null hypothesis every other voice must beat.]

INERTIA-FINDING-A: [one-line summary of the strongest status-quo argument, traceable to a Phase 1 finding by label]
INERTIA-FINDING-B: [one-line summary of the second-strongest, traceable to a Phase 1 finding by label]
```

These tags are the primary named concerns on the committee record. All subsequent voices must engage with them.

## Phase 3 — Remaining Participant Sort

After the inertia-advocate, sort all remaining participants. Within the remaining group: skeptics before advocates (roles that interrogate risk speak before roles that endorse).

Output:

```
## REMAINING SORT
Skeptics (speak next): [roles]
Advocates (speak last): [roles]
```

**Sort validation**: If all remaining participants land in the Advocates group — no skeptics among them — this is a sorting error. The inertia-advocate provides the Tier 1 challenge, but at least one additional participant must independently interrogate risk or hold a condition. Identify which remaining role most naturally challenges the proposal given this agenda item. Reassign it.

Output:

```
REMAINING-SORT-CHECK: [All remaining participants are advocates? YES — [role] reassigned to Skeptics because [specific reason]; revised sort above / NO — proceed]
```

Do not write remaining participant voices until REMAINING-SORT-CHECK is output.

## Phase 4 — Remaining Participant Voices

After the inertia-advocate, remaining participants speak in sort order: Skeptics → Advocates.

```
### [Role Name]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from this role's documented orientation. Must name at least one of INERTIA-FINDING-A or INERTIA-FINDING-B by tag and respond to it — either rebutting it with specific evidence or conceding it as a condition. A voice that does not name an inertia finding tag has not engaged with the committee record.]
```

**C-17 enforcement for advocate voices**: Advocate voices must additionally cite at least one Phase 1 investigation finding (by label — (a), (b), (c), or (d)) or one INERTIA-FINDING tag in their contribution. Endorsement that does not trace to the investigation record fails.

**C-19 enforcement for advocate voices**: Naming and responding to INERTIA-FINDING-A or INERTIA-FINDING-B by tag satisfies C-19 — these tags are the named Tier 1/2 concerns on the committee record. An advocate voice that cites a Phase 1 finding for C-17 but does not name an inertia tag does not satisfy C-19.

**Enforcement**: At least one non-inertia participant must also declare CONDITION or BLOCK. The inertia-advocate alone does not satisfy C-05 — the committee needs independent challenge.

## Phase 5 — Vote Tally

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

## V-05 — Combined: Investigation GATE + Sort Validation Step + `CITE:` + `RESPONDS-TO:` + TALLY

**Variation axes**: Lifecycle emphasis (investigation + named GATE step + named Sort Validation step) + role sequence (three-tier sort) + output format (`STANCE:` + `CITE:` + `RESPONDS-TO:` structural subfields + TALLY) + phrasing register (formal named step boundaries, no prose bloat)
**Hypothesis**: R4 V-05 targeted the 108-point ceiling by making C-16 a named step (Step 3), C-17 a structural `CITE:` subfield, and C-15 the load-bearing `STANCE:` label. Adding C-18 as a named Step 4b (Sort Validation) and C-19 as a `RESPONDS-TO:` structural subfield in each Tier 3 voice block should reach the 112-point ceiling. The architecture is: every aspirational criterion that can be made structural is made structural. Five labeled declarations the model cannot skip without a visible blank: GATE (C-16), SORT-CHECK (C-18), STANCE: (C-15/C-13), CITE: (C-17), RESPONDS-TO: (C-19). The named-step boundary structure (Steps 1–7) reduces attention dilution by giving each enforcement mechanism its own heading rather than embedding it in a paragraph.

---

You are simulating a committee meeting before the real one.

## Step 1 — Declare + Load

**Open with:**
```
Committee: [TYPE: ROB / shiproom / arch-board / other] — [agenda item title]
```

**Load participants.** Read `.craft/roles/` for this committee type's charter. Load every named role. Fallback: Signal defaults (PM, Architect, Inertia-Advocate) — state them explicitly.

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

## Step 4b — Sort Validation

Immediately after the sort block, output:

```
SORT-CHECK: [Tier 1 and Tier 2 both empty (all-APPROVE)? YES — [role] is mis-sorted; reassigning to Tier [1/2] because [specific reason given this agenda item]; corrected sort follows / NO — valid sort, proceed to voices]
```

If SORT-CHECK is YES: re-output the corrected PARTICIPANT SORT block before Step 5. Do not begin voices until SORT-CHECK is NO. This line is required; its absence means C-18 failed.

## Step 5 — Participant Voices

Write voices in strict tier order: Tier 1 → Tier 2 → Tier 3.

**Voice format:**

```
### [Role Name] — Tier [1/2/3]
STANCE: [APPROVE / CONDITION / BLOCK]
[2-4 sentences from documented role orientation. Prose follows the STANCE: declaration; it must not introduce a new stance or hedge the declared one.
  Tier 1: lead with the specific concern; may reference investigation findings by label.
  Tier 2: name the specific condition; ground it in investigation findings or the agenda item.
  Tier 3: see CITE: and RESPONDS-TO: subfields below — complete both before any endorsement prose.]
CITE: [Tier 3 only — investigation finding label (a/b/c/d) + the specific content from that finding that supports the endorsement]
RESPONDS-TO: [Tier 3 only — name the specific Tier 1 or Tier 2 concern being addressed (quote or paraphrase it); then state in one sentence how this endorsement addresses it]
```

**Rules:**
- `CITE:` is required for every Tier 3 voice. A Tier 3 block without `CITE:` fails C-17.
- `RESPONDS-TO:` is required for every Tier 3 voice. It must reference a specific named concern from a Tier 1 or Tier 2 voice — "I acknowledge there are concerns" does not pass. A Tier 3 block without `RESPONDS-TO:` fails C-19.
- At minimum: one voice must be CONDITION or BLOCK. All-APPROVE → return to Step 4b and re-sort.
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
