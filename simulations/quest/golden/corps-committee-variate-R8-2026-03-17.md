---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 8
rubric_version: 8
---

# corps-committee -- Prompt Variations R8

## Variation Summary

| ID   | Axis                                                                             | Hypothesis |
|------|----------------------------------------------------------------------------------|------------|
| V-01 | Outcome vocabulary contract (C-24)                                              | Pre-committing a named per-type vocabulary in a BEFORE YOU START registry table, then enforcing it at every downstream token site (STANCE, TALLY, Verdict), closes C-24 structurally: any wrong token produces an observable type mismatch rather than a subtle prose error. |
| V-02 | Tier-sequenced voice protocol (C-25)                                            | Pre-assigning each participant to Tier 1 (Challenger), Tier 2 (Conditional), or Tier 3 (Advocate) before Phase 0 roster, and enforcing Tier 1 -> Tier 2 -> Tier 3 discussion ordering as a hard structural constraint, closes C-25: an Advocate response before a Challenger concern is a detectable sequence violation, not invisible prose drift. |
| V-03 | Inertia-to-dissent token chain (C-27)                                           | Requiring every dissent table row -- and every CONDITION/BLOCK STANCE -- to cite a specific INERTIA-FINDING-N token by name closes C-27: a dissent assertion without a labeled inertia anchor is a missing cell, and a "No dissent" row without an inertia-resolution justification is also a missing cell. Inertia-to-dissent chain becomes end-to-end traceable. |
| V-04 | Per-tier voice completeness (C-26)                                              | Rendering the discussion grid as three structurally distinct tier grids -- each with a differentiated required column set (T1: STANCE + Inertia Citation; T2: STANCE + Conditions; T3: STANCE + CITE + RESPONDS-TO) -- closes C-26: a missing required field in any tier entry is a missing cell detectable by column scan, not a prose omission. |
| V-05 | Full integration (C-24 + C-25 + C-26 + C-27 + phase architecture + table-first) | Combining vocabulary contract, tier-sequenced voice, per-tier column grammar, and inertia token anchoring with the Phase 0/1/2 architecture and table-first output from R3 V-05 produces a fully integrated skill where all four new criteria enforce each other: vocabulary tokens appear in tier STANCE cells, inertia tokens appear in dissent cells, and per-tier column requirements make every omission structurally visible. |

---

## V-01 -- Outcome Vocabulary Contract

**Axis:** Outcome vocabulary contract (C-24)
**Hypothesis:** A BEFORE YOU START block that commits a named, per-type outcome vocabulary -- and explicitly states that all downstream STANCE, TALLY, and Verdict tokens must draw from it -- closes C-24 by making vocabulary mismatches structurally detectable. The vocabulary contract becomes the single source of truth for all decision tokens in the output.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BEFORE YOU START

### Step A -- Commit to your committee type

Identify your committee type. State its primary obligation and fail condition. Then commit
to its outcome vocabulary. Do not write a single discussion line or decision before
completing this block.

**ROB (Product Review / Service Review)**
Obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric in output = ROB not done. (C-01 fail)
OUTCOME VOCABULARY: APPROVED | APPROVED WITH CONDITIONS | BLOCKED | DEFERRED
All STANCE labels, TALLY entries, and the Verdict line must use these tokens only.

**SHIPROOM (Go / No-Go)**
Obligation: A binary GO or NO-GO decision backed by a risk register.
Fail condition: No GO or NO-GO decision line = shiproom not done. (C-01 fail, C-03 fail)
OUTCOME VOCABULARY: GO | NO-GO | HOLD
All STANCE labels, TALLY entries, and the Verdict line must use these tokens only.

**ARCH-BOARD (Architecture Decision Review)**
Obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: No ADR or no selected winner = arch-board not done. (C-01 fail)
OUTCOME VOCABULARY: ACCEPTED | REJECTED | DEFERRED
All STANCE labels, TALLY entries, and the Verdict line must use these tokens only.

### Step B -- Write the vocabulary lock

Write this line before any further output:

> VOCABULARY LOCK: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic] | Outcome tokens: [committed vocabulary]

FAILS: vocabulary lock line absent -- C-24 fail.
FAILS: any STANCE, TALLY, or Verdict token downstream is not from the committed vocabulary
  -- C-24 fail.
FAILS: vocabulary stated but not enforced at STANCE or Verdict sites -- C-24 partial.

---

## PHASE 0 -- SETUP

### 0.1 -- Participant Roster

Load .craft/roles/ for this committee type. List every participant.

| Seq | Participant | Role | Primary Concern This Meeting | Charter Status |
|-----|-------------|------|------------------------------|----------------|
| 1   | [name]      | [role from .craft/roles/] | [one concern] | [Standing / Candidate: function] |
| ... |             |                            |               |                                   |

For any required function without a charter role, set Charter Status to:
  [Candidate: [function] -- pending Phase 1 confirmation]

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: required function uncovered without annotation -- C-11 fail.
FAILS: injection candidate not annotated in Charter Status column -- C-12 fail.

### 0.2 -- Agenda

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item]      | [pass/fail condition] | [what must be present] |

FAILS: agenda items generic -- applicable to any committee type -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

### 0.3 -- Charter Constraints Identified

| Constraint  | Charter Requirement           | Must Honor in Phase 1 |
|-------------|-------------------------------|-----------------------|
| Quorum      | [from .craft/roles/]          | Yes                   |
| Veto        | [veto holder and conditions]  | Yes                   |
| Escalation  | [escalation path if deferred] | Yes                   |
| Scope       | [boundary out of scope]       | Yes                   |

FAILS: fewer than two constraints identified before Phase 0 exits -- C-10 partial.

*Phase 0 complete. Vocabulary locked. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 complete, vocabulary locked.*
*Exit: all agenda items discussed, decisions and dissent recorded.*

### 1.1 -- Discussion

Simulate each participant in sequence. Each participant speaks from their role function
exclusively. Each contribution must include type-specific evidence:
- ROB: cite a specific metric or readiness indicator.
- SHIPROOM: name a risk or blocker explicitly.
- ARCH-BOARD: name a trade-off or architectural constraint.

Each participant contribution includes a STANCE token drawn from the committed vocabulary.

Format per participant:
**[Participant] ([Role]) -- STANCE: [vocabulary token]**
[Contribution text including type-specific evidence]

FAILS: STANCE token not from the committed vocabulary -- C-24 fail.
FAILS: participant speaks outside their role domain -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.

### 1.2 -- Pre-Mortem Risk

One participant -- the role best suited to an outside-in perspective -- raises a
non-obvious, forward-looking risk. This risk must:
- Not be automatically predicted by a competent internal reviewer.
- Come from outside the team's normal frame of reference.

FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: risk is predictable by insiders -- C-09 outside-in gate not cleared.

### 1.3 -- Decision Tally

After discussion, record the tally using vocabulary tokens only:

| Stance Token   | Count | Participants |
|----------------|-------|--------------|
| [vocab token]  | N     | [names]      |
| [vocab token]  | N     | [names]      |

FAILS: tally uses tokens not from the committed vocabulary -- C-24 fail.

### 1.4 -- Dissent Check

| Participant | Role | In Tension with Majority? | Dissent Statement |
|-------------|------|--------------------------|-------------------|
| [name]      | [role] | Yes / No               | [objection in role voice, or --] |

FAILS: role-based tension exists but row marked No without basis -- C-05 fail.

*Phase 1 complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: Phase 1 complete.*
*Exit: all formal minutes sections present.*

### Decisions

The Outcome column must use only the committed vocabulary tokens from Step B.

| # | Decision | Outcome          | Conditions |
|---|----------|------------------|------------|
| 1 | [text]   | [vocabulary token] | [or --]  |

FAILS: Outcome column uses a token not in the committed vocabulary -- C-24 fail.
FAILS: Outcome column empty for any row -- C-03 fail.
FAILS: Decisions table absent -- C-03 fail.

### Verdict

The final Verdict line uses the committed vocabulary token only.

> **Verdict: [committed vocabulary token] -- [one-sentence rationale]**

FAILS: Verdict token not from the committed vocabulary -- C-24 fail.
FAILS: Verdict absent -- C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Name / Role] | [milestone] |

FAILS: Owner column empty for any row -- C-04 fail.
FAILS: table absent when Phase 1 raised open questions -- C-04 fail.

### Dissenting Opinions

| Participant | Role | Objection |
|-------------|------|-----------|
| [name]      | [role] | [objection in role voice] |

*No dissent -- unanimous.* (if applicable)

FAILS: known role-based tension from Phase 1 omitted -- C-05 fail.

### Charter Constraints Honored

| Constraint | Requirement   | Applied | Notes  |
|------------|---------------|---------|--------|
| Quorum     | [from Phase 0] | Yes / No | [count] |
| Veto       | [from Phase 0] | Exercised / Waived | [outcome] |

FAILS: fewer than two rows confirmed from Phase 0 constraints -- C-10 partial.

### AMEND (if invoked)

Apply amendment before generating output. Re-run from amended Phase 0.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-02 -- Tier-Sequenced Voice Protocol

**Axis:** Tier-sequenced voice protocol (C-25)
**Hypothesis:** Pre-assigning participants to Tier 1 (Challenger), Tier 2 (Conditional), or
Tier 3 (Advocate) before Phase 0 roster construction, and enforcing Tier 1 -> Tier 2 -> Tier 3
discussion ordering as a stated structural constraint, closes C-25. The ordering is not stylistic;
it is a production constraint. An Advocate voice appearing before a Challenger voice is a
detectable sequence violation.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BEFORE YOU START

### Step A -- Commit to your committee type

Identify your committee type and state its obligation and fail condition.

**ROB (Product Review / Service Review)**
Obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric in output = ROB not done. (C-01 fail)

**SHIPROOM (Go / No-Go)**
Obligation: A binary GO or NO-GO decision backed by a risk register.
Fail condition: No GO/NO-GO decision line = shiproom not done. (C-01 fail, C-03 fail)

**ARCH-BOARD (Architecture Decision Review)**
Obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: No ADR or no selected winner = arch-board not done. (C-01 fail)

Write:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

### Step B -- TIER SEQUENCE PROTOCOL

Before any participant speaks, assign every participant to a voice tier.

| Tier | Label       | Role in Discussion                                      |
|------|-------------|---------------------------------------------------------|
| T1   | Challenger  | Raises the primary challenge, concern, or objection.    |
|      |             | STANCE must be CHALLENGE, CONDITION, or BLOCK.          |
| T2   | Conditional | Raises concerns that are conditional on specific changes.|
|      |             | STANCE must be CONDITION or QUALIFIED-SUPPORT.          |
| T3   | Advocate    | Supports with evidence or endorsement.                  |
|      |             | STANCE must be SUPPORT or ENDORSE.                      |

**ORDERING CONSTRAINT (mandatory):**
All Tier 1 voices must appear before any Tier 2 voice.
All Tier 2 voices must appear before any Tier 3 voice.
A Tier 3 Advocate response appearing before a Tier 1 Challenger voice has been written
is a structural violation -- halt, reorder, and continue.

FAILS: Tier 3 voice appears before Tier 1 voice -- C-25 fail.
FAILS: tier assignment absent before Phase 0 begins -- C-25 fail.
FAILS: STANCE token mismatches the participant's assigned tier role -- C-25 partial.

---

## PHASE 0 -- SETUP

### 0.0 -- Tier Pre-Assignment

Before building the roster, assign each participant their tier. State the rationale.

| Participant | Role | Tier | Rationale |
|-------------|------|------|-----------|
| [name]      | [role] | T1 | [why their frame is challenger -- what they are most likely to question] |
| [name]      | [role] | T2 | [why conditional -- what change would move them to support] |
| [name]      | [role] | T3 | [why advocate -- what evidence they will endorse] |

FAILS: tier pre-assignment absent before Phase 0 roster -- C-25 fail.
FAILS: participant assigned T3 when their role charter would predict challenge -- C-25 partial.

### 0.1 -- Participant Roster (ordered by tier, then by role sequence within tier)

| Seq | Participant | Role | Tier | Primary Concern | Charter Status |
|-----|-------------|------|------|-----------------|----------------|
| 1   | [name]      | [role] | T1 | [concern]       | [Standing / Candidate: function] |
| 2   | [name]      | [role] | T1 | [concern]       | [Standing]      |
| 3   | [name]      | [role] | T2 | [concern]       | [Standing]      |
| 4   | [name]      | [role] | T3 | [concern]       | [Standing]      |

FAILS: roster not ordered by tier -- C-25 fail.
FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: required function uncovered without annotation -- C-11 fail.

### 0.2 -- Agenda

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item]      | [pass/fail condition] | [what must be present] |

FAILS: agenda items generic -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

### 0.3 -- Charter Constraints Identified

| Constraint  | Charter Requirement           | Must Honor in Phase 1 |
|-------------|-------------------------------|-----------------------|
| Quorum      | [from .craft/roles/]          | Yes                   |
| Veto        | [veto holder and conditions]  | Yes                   |

FAILS: fewer than two constraints before Phase 0 exits -- C-10 partial.

*Phase 0 complete. Tiers locked. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: tier pre-assignment complete, Phase 0 complete.*
*Exit: all voices rendered in tier order, decisions and dissent recorded.*

### 1.1 -- Discussion (render in tier order: T1 -> T2 -> T3)

**Tier 1 Voices (render all before any Tier 2):**

**[T1 Participant] ([Role]) -- STANCE: [CHALLENGE / CONDITION / BLOCK]**
[Contribution with type-specific evidence]

[repeat for all T1 participants]

TIER BOUNDARY -- no Tier 2 voice before all Tier 1 voices are written.

**Tier 2 Voices (render all before any Tier 3):**

**[T2 Participant] ([Role]) -- STANCE: [CONDITION / QUALIFIED-SUPPORT]**
[Contribution with explicit conditions stated. Conditions must reference what would
change the participant's stance. Responds to: [T1 entry this responds to]]

[repeat for all T2 participants]

TIER BOUNDARY -- no Tier 3 voice before all Tier 2 voices are written.

**Tier 3 Voices:**

**[T3 Participant] ([Role]) -- STANCE: [SUPPORT / ENDORSE]**
[Contribution endorsing the proposal with cited evidence. Responds to: [T1 or T2 entry
this voice follows]]

[repeat for all T3 participants]

FAILS: any Tier 3 STANCE voice appears before a Tier 1 STANCE voice -- C-25 fail.
FAILS: any Tier 2 STANCE voice appears before all Tier 1 voices are present -- C-25 fail.
FAILS: participant speaks outside their role domain -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.

### 1.2 -- Pre-Mortem Risk

One participant -- the designated T1 Challenger or the role best suited to an outside-in
perspective -- raises a non-obvious, forward-looking risk.

FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: risk is predictable by insiders -- C-09 outside-in gate not cleared.

### 1.3 -- Agenda Decision Check

| Agenda Item | Discussed? | Decision Reached? | Deferred? |
|-------------|------------|-------------------|-----------|
| [item 1]    | Yes        | [outcome]         | No        |

FAILS: agenda item discussed without decision or deferral noted -- C-03 fail.

### 1.4 -- Dissent Check

| Participant | Role | Tier | In Tension with Majority? | Dissent Statement |
|-------------|------|------|--------------------------|-------------------|
| [name]      | [role] | T1 | Yes / No               | [objection in role voice, or --] |

FAILS: T1 Challenger in tension with majority but dissent omitted -- C-05 fail.

*Phase 1 complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: Phase 1 complete.*

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [text]   | [approved / rejected / deferred / conditional-approval] | [or --] |

FAILS: Outcome column empty -- C-03 fail.
FAILS: Decisions table absent -- C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Name / Role] | [milestone] |

FAILS: Owner column empty for any row -- C-04 fail.

### Dissenting Opinions

| Participant | Role | Tier | Objection |
|-------------|------|------|-----------|
| [name]      | [role] | T1 | [objection in role voice] |

*No dissent -- unanimous.* (if applicable)

FAILS: known T1 tension from Phase 1 omitted -- C-05 fail.

### Charter Constraints Honored

| Constraint | Requirement   | Applied | Notes  |
|------------|---------------|---------|--------|
| Quorum     | [from Phase 0] | Yes / No | [count] |

FAILS: fewer than two rows confirmed -- C-10 partial.

### AMEND (if invoked)

Re-run from Phase 0 tier pre-assignment with amended inputs.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-03 -- Inertia-to-Dissent Token Chain

**Axis:** Inertia-to-dissent token chain (C-27)
**Hypothesis:** Building a named INERTIA-FINDING-N inventory before simulation begins, then
requiring every dissent table row and every CONDITION/BLOCK stance to cite a specific token
by name, closes C-27. A dissent entry without a labeled inertia anchor is a missing required
field -- detectable by column scan. "No dissent" entries that do not state which inertia
concern was resolved are also incomplete. The inertia-to-dissent chain becomes end-to-end
traceable from the inventory to every dissenting stance.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.

---

## BEFORE YOU START

### Step A -- Commit to your committee type

Identify your committee type and state its obligation and fail condition.

**ROB (Product Review / Service Review)**
Obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric in output = ROB not done. (C-01 fail)

**SHIPROOM (Go / No-Go)**
Obligation: A binary GO or NO-GO decision backed by a risk register.
Fail condition: No GO/NO-GO decision line = shiproom not done. (C-01 fail, C-03 fail)

**ARCH-BOARD (Architecture Decision Review)**
Obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: No ADR or no selected winner = arch-board not done. (C-01 fail)

Write:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

### Step B -- INERTIA FINDING INVENTORY

Before the meeting begins, build the inertia inventory. These are the specific beliefs
the real committee holds as default -- assumptions that are normalized into invisibility
by the organization's prior decisions.

State at least three named inertia findings:

| Token             | Normalized Belief                                                   |
|-------------------|---------------------------------------------------------------------|
| INERTIA-FINDING-1 | [specific belief the committee accepts without challenge -- state   |
|                   |  an observable organizational behavior, not a generic risk class]  |
| INERTIA-FINDING-2 | [another specific default assumption]                               |
| INERTIA-FINDING-3 | [another specific default assumption]                               |
| [add more as needed] | [...]                                                            |

**CITATION OBLIGATION (mandatory for all downstream content):**
Every CONDITION or BLOCK STANCE must cite at least one INERTIA-FINDING-N token by name.
Every dissent entry must cite at least one INERTIA-FINDING-N token by name.
A "No dissent" entry must state: "Resolved: INERTIA-FINDING-N -- resolved by [evidence]."

FAILS: inertia inventory absent before Phase 0 begins -- C-27 fail.
FAILS: fewer than three named INERTIA-FINDING-N entries -- C-17/C-18 partial.
FAILS: inventory uses generic category headings rather than specific named beliefs -- C-18 partial.

---

## PHASE 0 -- SETUP

### 0.1 -- Participant Roster

| Seq | Participant | Role | Primary Concern | Charter Status |
|-----|-------------|------|-----------------|----------------|
| 1   | [name]      | [role from .craft/roles/] | [one concern] | [Standing / Candidate: function] |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: required function uncovered without annotation -- C-11 fail.
FAILS: injection candidate not annotated -- C-12 fail.

### 0.2 -- Agenda

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item]      | [pass/fail condition] | [what must be present] |

FAILS: agenda items generic -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

### 0.3 -- Charter Constraints Identified

| Constraint  | Charter Requirement           | Must Honor in Phase 1 |
|-------------|-------------------------------|-----------------------|
| Quorum      | [from .craft/roles/]          | Yes                   |
| Veto        | [veto holder and conditions]  | Yes                   |

FAILS: fewer than two constraints -- C-10 partial.

*Phase 0 complete. Inertia inventory locked. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: inertia inventory locked, Phase 0 complete.*
*Exit: all agenda items discussed, decisions and dissent recorded with inertia citations.*

### 1.1 -- Discussion

Simulate each participant in sequence. Each participant speaks from their role function.
Each contribution includes type-specific evidence.

Participants who dissent or hold conditional stances must cite a specific INERTIA-FINDING-N
token in their contribution.

Format per participant:
**[Participant] ([Role]) -- STANCE: [SUPPORT / CONDITION / BLOCK]**
[Contribution text with type-specific evidence]
[If CONDITION or BLOCK: Inertia Basis: INERTIA-FINDING-N -- "[what the finding is"]

FAILS: CONDITION or BLOCK stance without INERTIA-FINDING-N citation -- C-27 fail.
FAILS: participant speaks outside their role domain -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.

### 1.2 -- Pre-Mortem Risk

The designated outside-in participant raises a non-obvious, forward-looking risk that
traces back to a specific inertia finding.

**PRE-MORTEM RISK -- [Participant] ([Role]):**
[Risk statement -- must be non-obvious and outside-in]
Inertia Basis: INERTIA-FINDING-N -- [the normalized belief that makes this risk invisible
to insiders]

FAILS: pre-mortem risk raises no inertia basis -- C-19/C-27 partial.
FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: risk predictable by insiders -- C-09 outside-in gate not cleared.

### 1.3 -- Agenda Decision Check

| Agenda Item | Discussed? | Decision Reached? | Deferred? |
|-------------|------------|-------------------|-----------|
| [item 1]    | Yes        | [outcome]         | No        |

FAILS: agenda item discussed without decision or deferral -- C-03 fail.

### 1.4 -- Dissent Collection

Collect every potential dissenting stance before Phase 2. For each participant who
could plausibly dissent:

| Participant | Role | STANCE | Dissent Statement | Inertia Token |
|-------------|------|--------|-------------------|---------------|
| [name]      | [role] | [CONDITION/BLOCK/SUPPORT] | [objection in role voice, or "No dissent"] | [INERTIA-FINDING-N, or "Resolved: INERTIA-FINDING-N -- [evidence]"] |

FAILS: any dissent row missing the Inertia Token column -- C-27 fail.
FAILS: "No dissent" row without inertia-resolution justification -- C-27 fail.
FAILS: CONDITION or BLOCK stance without INERTIA-FINDING-N citation -- C-27 fail.
FAILS: role-based tension exists but not captured here -- C-05 fail.

*Phase 1 complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: Phase 1 complete, dissent collection includes inertia tokens.*

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [text]   | [approved / rejected / deferred / conditional-approval] | [or --] |

FAILS: Outcome column empty -- C-03 fail.
FAILS: Decisions table absent -- C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Name / Role] | [milestone] |

FAILS: Owner column empty for any row -- C-04 fail.

### Dissenting Opinions

Every dissenting participant from Phase 1.4. Each row must carry an inertia token.

| Participant | Role | Objection | Inertia Token |
|-------------|------|-----------|---------------|
| [name]      | [role] | [objection in role voice] | [INERTIA-FINDING-N] |

*No dissent -- unanimous. Inertia concerns resolved:*
- INERTIA-FINDING-1 resolved by [evidence stated in discussion]

FAILS: dissent row without Inertia Token column -- C-27 fail.
FAILS: "No dissent" entry without inertia-resolution statement -- C-27 fail.
FAILS: known role-based tension omitted from this table -- C-05 fail.

### Charter Constraints Honored

| Constraint | Requirement   | Applied | Notes  |
|------------|---------------|---------|--------|
| Quorum     | [from Phase 0] | Yes / No | [count] |
| Veto       | [from Phase 0] | Exercised / Waived | [outcome] |

FAILS: fewer than two rows confirmed -- C-10 partial.

### AMEND (if invoked)

Re-run from Phase 0 with amended inputs. Inertia inventory re-evaluated for amendment scope.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-04 -- Per-Tier Voice Completeness

**Axis:** Per-tier voice completeness (C-26)
**Hypothesis:** Rendering the discussion as three structurally distinct tier grids -- each
with a differentiated required column set that varies by tier role -- closes C-26. Tier 1
(Challenger) requires STANCE + Inertia Citation. Tier 2 (Conditional) requires STANCE +
Conditions. Tier 3 (Advocate) requires STANCE + CITE + RESPONDS-TO. A missing required
field in any tier entry is a missing cell detectable by column scan, not a prose omission.
A skill that applies identical column requirements to all tiers does not satisfy C-26.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Produce mock meeting minutes.
Render the discussion using three distinct tier grids with per-tier required columns.

---

## BEFORE YOU START

### Step A -- Commit to your committee type

Identify your committee type and state its obligation and fail condition.

**ROB (Product Review / Service Review)**
Obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric = ROB not done. (C-01 fail)

**SHIPROOM (Go / No-Go)**
Obligation: Binary GO or NO-GO with risk register.
Fail condition: No GO/NO-GO line = shiproom not done. (C-01 fail, C-03 fail)

**ARCH-BOARD (Architecture Decision Review)**
Obligation: ADR with named trade-offs and a selected alternative.
Fail condition: No ADR or no winner selected = arch-board not done. (C-01 fail)

Write:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

### Step B -- TIER VOICE COMPLETENESS CONTRACT

The discussion uses three separate grids. Each grid has a different required column set.

| Tier | Label      | Required Columns                                                        |
|------|------------|-------------------------------------------------------------------------|
| T1   | Challenger | Participant, Role, STANCE, Inertia Citation, Challenge Statement        |
| T2   | Conditional| Participant, Role, STANCE, Conditions, Condition Basis                  |
| T3   | Advocate   | Participant, Role, STANCE, CITE, RESPONDS-TO, Support Statement         |

A missing cell in any required column is a structural gap -- C-26 fail for that tier entry.

**ORDERING CONSTRAINT:**
T1 grid is rendered first and fully before T2 grid begins.
T2 grid is rendered fully before T3 grid begins.

FAILS: all tiers use the same column schema -- C-26 fail.
FAILS: any T1 row missing the Inertia Citation column -- C-26 fail.
FAILS: any T2 row missing Conditions -- C-26 fail.
FAILS: any T3 row missing CITE or RESPONDS-TO -- C-26 fail.

---

## PHASE 0 -- SETUP

### 0.1 -- Tier Pre-Assignment

Assign each participant to a tier before building the roster.

| Participant | Role | Tier | Assignment Rationale |
|-------------|------|------|----------------------|
| [name]      | [role] | T1 | [why this role is challenger] |
| [name]      | [role] | T2 | [why this role is conditional] |
| [name]      | [role] | T3 | [why this role is advocate] |

FAILS: tier assignment absent before roster -- C-25 fail, C-26 fail.

### 0.2 -- Participant Roster (ordered by tier)

| Seq | Participant | Role | Tier | Primary Concern | Charter Status |
|-----|-------------|------|------|-----------------|----------------|
| 1   | [name]      | [role] | T1 | [one concern]   | [Standing / Candidate: function] |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: required function uncovered without annotation -- C-11 fail.

### 0.3 -- Inertia Inventory (required for T1 Inertia Citation column)

| Token             | Normalized Belief |
|-------------------|-------------------|
| INERTIA-FINDING-1 | [specific organizational belief normalized into invisibility] |
| INERTIA-FINDING-2 | [specific normalized belief] |
| INERTIA-FINDING-3 | [specific normalized belief] |

FAILS: inventory absent when T1 participants are present -- C-26 fail (T1 Inertia Citation
  column cannot be populated without a named inventory to draw from).

### 0.4 -- Agenda

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item]      | [pass/fail condition] | [what must be present] |

FAILS: agenda items generic -- C-07 fail.

### 0.5 -- Charter Constraints

| Constraint  | Charter Requirement           | Must Honor in Phase 1 |
|-------------|-------------------------------|-----------------------|
| Quorum      | [from .craft/roles/]          | Yes                   |
| Veto        | [veto holder and conditions]  | Yes                   |

*Phase 0 complete. Tier grids ready. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION (three tier grids)

*Entry: tier pre-assignment complete, inertia inventory built, Phase 0 complete.*
*Exit: all three tier grids populated in order.*

### TIER 1 GRID -- Challengers

Required columns: Participant | Role | STANCE | Inertia Citation | Challenge Statement

| Participant | Role | STANCE | Inertia Citation | Challenge Statement |
|-------------|------|--------|-----------------|---------------------|
| [name]      | [role] | CHALLENGE / CONDITION / BLOCK | INERTIA-FINDING-N | [challenge in role voice with type-specific evidence] |

FAILS: Inertia Citation column empty for any T1 row -- C-26 fail.
FAILS: Inertia Citation does not reference a named token from the inventory -- C-26 fail.
FAILS: STANCE not from the T1 permitted set -- C-25 partial.
FAILS: Challenge Statement contains no type-specific evidence -- C-07 fail.
FAILS: participant speaks outside their role domain -- C-02 fail.

[Complete all T1 entries before rendering any T2 entry.]

---

### TIER 2 GRID -- Conditional

Required columns: Participant | Role | STANCE | Conditions | Condition Basis

| Participant | Role | STANCE | Conditions | Condition Basis |
|-------------|------|--------|------------|-----------------|
| [name]      | [role] | CONDITION / QUALIFIED-SUPPORT | [specific change required for support] | [what evidence or action would satisfy this condition] |

FAILS: Conditions column empty for any T2 row -- C-26 fail.
FAILS: Condition is a restatement of the concern rather than an actionable change -- C-26 partial.
FAILS: STANCE not from the T2 permitted set -- C-25 partial.

[Complete all T2 entries before rendering any T3 entry.]

---

### TIER 3 GRID -- Advocates

Required columns: Participant | Role | STANCE | CITE | RESPONDS-TO | Support Statement

| Participant | Role | STANCE | CITE | RESPONDS-TO | Support Statement |
|-------------|------|--------|------|-------------|-------------------|
| [name]      | [role] | SUPPORT / ENDORSE | [evidence or data cited] | [T1 or T2 entry this responds to, by participant name] | [endorsement in role voice with type-specific evidence] |

FAILS: CITE column empty for any T3 row -- C-26 fail.
FAILS: RESPONDS-TO column empty or None for any T3 row -- C-26 fail.
FAILS: RESPONDS-TO does not reference an actual prior T1 or T2 entry -- C-26 fail.
FAILS: STANCE not from the T3 permitted set -- C-25 partial.

---

### Pre-Mortem Risk

One participant -- the T1 Challenger or the role most suited to outside-in perspective --
raises a non-obvious, forward-looking risk.

**PRE-MORTEM RISK -- [Participant] ([Role]):**
[Risk statement -- non-obvious, outside-in, not predictable by insiders]
Inertia Basis: INERTIA-FINDING-N

FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: risk predictable by insiders -- C-09 outside-in gate not cleared.

### Agenda Decision Check

| Agenda Item | Discussed? | Decision Reached? | Deferred? |
|-------------|------------|-------------------|-----------|
| [item]      | Yes        | [outcome]         | No        |

FAILS: agenda item without decision or deferral -- C-03 fail.

*Phase 1 complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: Phase 1 complete.*

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [text]   | [approved / rejected / deferred / conditional-approval] | [or --] |

FAILS: Outcome column empty -- C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Name / Role] | [milestone] |

FAILS: Owner column empty -- C-04 fail.

### Dissenting Opinions

Carry forward T1 and T2 dissenting stances from Phase 1.

| Participant | Role | Tier | Objection | Inertia Token |
|-------------|------|------|-----------|---------------|
| [name]      | [role] | T1 | [objection] | [INERTIA-FINDING-N] |

*No dissent -- unanimous.* (if applicable, state resolved inertia findings)

FAILS: known dissent from T1 grid omitted -- C-05 fail.

### Charter Constraints Honored

| Constraint | Requirement   | Applied | Notes  |
|------------|---------------|---------|--------|
| Quorum     | [from Phase 0] | Yes / No | [count] |
| Veto       | [from Phase 0] | Exercised / Waived | [outcome] |

FAILS: fewer than two rows confirmed -- C-10 partial.

### AMEND (if invoked)

Re-run from Phase 0 tier pre-assignment with amended inputs.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-05 -- Full Integration

**Axis:** Outcome vocabulary contract + tier-sequenced voice + per-tier voice completeness +
inertia-to-dissent token chain + phase architecture + table-first
**Hypothesis:** Combining all four new criteria (C-24 through C-27) with the Phase 0/1/2
architecture and table-first output from R3 V-05 produces a fully integrated skill where
each new criterion enforces the others: vocabulary tokens appear in tier STANCE cells
(C-24 + C-25), inertia tokens appear in T1 Inertia Citation cells and dissent Inertia Token
cells (C-26 + C-27), and the three-grid structure makes every omission detectable by column
scan. The pre-committed vocabulary contract, the tier sequence protocol, the per-tier column
grammar, and the inertia-to-dissent chain are interdependent structural properties of a
single coherent artifact.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Execute in three phases. Use tables for
every enumerable section. Render the discussion in three tier grids. All tokens (STANCE,
TALLY, Verdict, Inertia) must trace back to pre-committed registries built before Phase 0.

---

## BEFORE YOU START

Complete all four blocks in this section before Phase 0 begins. Do not generate any
meeting content until all four blocks are written.

### Block 1 -- COMMITTEE TYPE AND OUTCOME VOCABULARY CONTRACT

Identify your committee type. Commit its outcome vocabulary. All STANCE tokens, TALLY
entries, and the Verdict line downstream must draw from the committed vocabulary only.

| Type        | Primary Obligation                                | Outcome Vocabulary                                                  | Automatic Fail Condition |
|-------------|---------------------------------------------------|---------------------------------------------------------------------|--------------------------|
| ROB         | Readiness verdict backed by metric evidence       | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED            | No metric = ROB not done -- C-01 fail |
| SHIPROOM    | Binary GO or NO-GO backed by risk register        | GO / NO-GO / HOLD                                                   | No GO/NO-GO line = shiproom not done -- C-01 fail, C-03 fail |
| ARCH-BOARD  | ADR with named trade-offs and a selected winner   | ACCEPTED / REJECTED / DEFERRED                                      | No ADR or no winner = arch-board not done -- C-01 fail |

Write:
> VOCABULARY LOCK: [type] | Topic: [topic] | Outcome tokens: [committed vocabulary]

FAILS: vocabulary lock absent -- C-24 fail.
FAILS: any STANCE, TALLY, or Verdict token downstream not from committed vocabulary -- C-24 fail.

### Block 2 -- TIER SEQUENCE PROTOCOL

Assign every participant to a voice tier before Phase 0 begins.

| Tier | Label       | Permitted STANCE Tokens          | Required Grid Columns                           | Ordering Constraint |
|------|-------------|----------------------------------|-------------------------------------------------|---------------------|
| T1   | Challenger  | CHALLENGE, CONDITION, BLOCK      | Participant, Role, STANCE, Inertia Citation, Challenge Statement | First -- all T1 before any T2 |
| T2   | Conditional | CONDITION, QUALIFIED-SUPPORT     | Participant, Role, STANCE, Conditions, Condition Basis | After all T1 -- all T2 before any T3 |
| T3   | Advocate    | SUPPORT, ENDORSE                 | Participant, Role, STANCE, CITE, RESPONDS-TO, Support Statement | Last -- after all T1 and T2 |

**ORDERING CONSTRAINT (hard structural rule):**
A T3 voice appearing before a T1 voice is a sequence violation -- C-25 fail.
A T2 voice appearing before all T1 voices are written is a sequence violation -- C-25 fail.

Tier pre-assignment:

| Participant | Role | Tier | Assignment Rationale |
|-------------|------|------|----------------------|
| [name]      | [role] | T1 | [why challenger -- what they are most likely to question, and why their frame is least normalized] |
| [name]      | [role] | T2 | [why conditional -- what change would shift them to support] |
| [name]      | [role] | T3 | [why advocate -- what evidence base they will endorse] |

FAILS: tier pre-assignment absent -- C-25 fail.
FAILS: any T1 row uses a T3 STANCE token -- C-25 partial.

### Block 3 -- INERTIA FINDING INVENTORY

State at least three specific organizational beliefs the real committee holds as default --
normalized assumptions the committee has accepted without challenge.

| Token             | Normalized Belief (must be an observable organizational behavior, not a generic risk class) |
|-------------------|---------------------------------------------------------------------------------------------|
| INERTIA-FINDING-1 | [specific belief, e.g., "The security review is a checkbox because no prior release was blocked by it"] |
| INERTIA-FINDING-2 | [specific belief] |
| INERTIA-FINDING-3 | [specific belief] |

**CITATION MANDATE:**
Every T1 Inertia Citation cell must reference a named token from this inventory.
Every CONDITION or BLOCK STANCE must cite at least one token by name.
Every dissent row must carry a named token. "No dissent" rows must state: "Resolved:
INERTIA-FINDING-N -- [evidence that resolved it]."

FAILS: inventory absent -- C-17/C-18/C-27 fail.
FAILS: inventory uses category headings rather than specific named beliefs -- C-18 partial.
FAILS: T1 Inertia Citation references a non-inventory token -- C-26 fail, C-27 partial.

### Block 4 -- DESIGNATED INERTIA CHALLENGER

Before any phase begins, designate one participant as the Inertia Challenger.

> INERTIA CHALLENGER: [role name] -- [rationale: why their frame is least likely to
> reflect the normalized assumptions in the inventory] -- NORM obligation: must cite
> at least one INERTIA-FINDING-N from the inventory in their T1 contribution.

This participant's T1 Inertia Citation cell is required non-None.
The Phase 2 pre-mortem risk must trace back to this participant's inertia citation.

If no qualifying participant exists among standing roster members, state:
> INJECTION REQUIRED: [function] -- [role function needed for outside-in perspective]

FAILS: Challenger designation absent before Phase 0 -- C-20/C-23 fail.
FAILS: Challenger's Inertia Citation cell is empty -- C-20 fail.
FAILS: Phase 2 pre-mortem risk does not trace to Challenger's inertia citation -- C-19/C-20 partial.

*All four blocks complete. Entering Phase 0.*

---

## PHASE 0 -- SETUP

*Entry: all four BEFORE YOU START blocks complete.*
*Exit: roster confirmed, agenda locked, charter constraints identified.*

### Participant Roster (ordered by tier, then by declared role sequence within tier)

| Seq | Participant | Role | Tier | Primary Concern | Charter Status |
|-----|-------------|------|------|-----------------|----------------|
| 1   | [name]      | [role from .craft/roles/] | T1 | [one concern aligned with role function] | [Standing / Candidate: function -- pending confirmation] |
| 2   | [name]      | [role] | T1 | [one concern] | [Standing] |
| 3   | [name]      | [role] | T2 | [one concern] | [Standing] |
| 4   | [name]      | [role] | T3 | [one concern] | [Standing] |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: required function uncovered without annotation -- C-11 fail.
FAILS: injection candidate not annotated in Charter Status -- C-12 fail.
FAILS: roster sequence does not follow tier ordering -- C-25 fail.

### Agenda

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item]      | [pass/fail condition] | [what must be present in discussion] |
| 2 | [item]      | [pass/fail condition] | [what must be present] |
| 3 | [item]      | [pass/fail condition] | [what must be present] |

FAILS: agenda items generic -- applicable to any committee type -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

### Charter Constraints

| Constraint  | Charter Requirement           | Must Honor in Phase 1 |
|-------------|-------------------------------|-----------------------|
| Quorum      | [from .craft/roles/]          | Yes                   |
| Veto        | [veto holder and conditions]  | Yes                   |
| Escalation  | [path if any decision deferred] | Yes                 |
| Scope       | [what is explicitly out of scope] | Yes              |

FAILS: fewer than two constraints identified -- C-10 partial.
FAILS: charter constraints not sourced from .craft/roles/ language -- C-10 partial.

*Phase 0 complete. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 complete, all registries locked.*
*Exit: all three tier grids populated in order, decisions and dissent captured.*

### PRE-MORTEM CHAIN CHECK

Before generating any discussion grid content, confirm the three chain checkpoints:

CHAIN-1 -- Challenger: [name of designated Inertia Challenger from Block 4] -- non-None? [Yes / No -- if No, halt and inject]

CHAIN-2 -- Outside-in basis: [state the outside-in frame of reference -- must not derive from internal knowledge or general reasoning; if it does, this check fails]
  Internal basis check: would a competent internal reviewer reach this framing independently? [If Yes, the basis is circular -- revise]

CHAIN-3 -- Risk draft: [draft the pre-mortem risk, connected to INERTIA-FINDING-N]
  Risk: [draft statement]
  Connected inertia finding: INERTIA-FINDING-N

Phase 2 pre-mortem content must expand CHAIN-3. Inconsistency between CHAIN-3 and Phase 2
output is a C-19 fail.

FAILS: any chain checkpoint is None or blank -- C-19 fail.
FAILS: CHAIN-2 basis derives from internal knowledge -- C-19 fail, C-09 outside-in gate not cleared.
FAILS: CHAIN-3 risk draft not connected to a named inertia finding -- C-19 fail.

*Chain check passed. Rendering tier grids.*

---

### TIER 1 GRID -- Challengers (render all before any Tier 2)

Required columns: Participant | Role | STANCE | Inertia Citation | Challenge Statement

| Participant | Role | STANCE | Inertia Citation | Challenge Statement |
|-------------|------|--------|-----------------|---------------------|
| [name]      | [role] | CHALLENGE / CONDITION / BLOCK | INERTIA-FINDING-N | [challenge in role voice; type-specific evidence cited; one sentence per claim] |

Type-specific evidence in Challenge Statement:
- ROB: cite a specific metric or readiness indicator.
- SHIPROOM: name a risk or blocker explicitly.
- ARCH-BOARD: name a trade-off or architectural constraint.

FAILS: STANCE token not from T1 permitted set -- C-25 partial.
FAILS: STANCE token not from committed vocabulary (Block 1) -- C-24 fail.
FAILS: Inertia Citation column empty for any T1 row -- C-26 fail.
FAILS: Inertia Citation references a token not in the Block 3 inventory -- C-26 fail.
FAILS: Challenge Statement contains no type-specific evidence -- C-07 fail.
FAILS: participant speaks outside their role domain -- C-02 fail.

TIER BOUNDARY: All T1 rows complete before any T2 row is written.

---

### TIER 2 GRID -- Conditionals (render all before any Tier 3)

Required columns: Participant | Role | STANCE | Conditions | Condition Basis

| Participant | Role | STANCE | Conditions | Condition Basis |
|-------------|------|--------|------------|-----------------|
| [name]      | [role] | CONDITION / QUALIFIED-SUPPORT | [specific actionable change required for support] | [what evidence or action would satisfy this condition; reference INERTIA-FINDING-N if applicable] |

FAILS: STANCE token not from T2 permitted set -- C-25 partial.
FAILS: STANCE token not from committed vocabulary (Block 1) -- C-24 fail.
FAILS: Conditions column empty for any T2 row -- C-26 fail.
FAILS: Condition is a restatement of concern rather than an actionable change -- C-26 partial.
FAILS: Condition or Qualified-Support STANCE without Condition Basis -- C-26 fail.

TIER BOUNDARY: All T2 rows complete before any T3 row is written.

---

### TIER 3 GRID -- Advocates

Required columns: Participant | Role | STANCE | CITE | RESPONDS-TO | Support Statement

| Participant | Role | STANCE | CITE | RESPONDS-TO | Support Statement |
|-------------|------|--------|------|-------------|-------------------|
| [name]      | [role] | SUPPORT / ENDORSE | [evidence or data cited by name] | [T1 or T2 participant name this entry directly responds to] | [endorsement in role voice; type-specific evidence; one sentence per claim] |

FAILS: STANCE token not from T3 permitted set -- C-25 partial.
FAILS: STANCE token not from committed vocabulary (Block 1) -- C-24 fail.
FAILS: CITE column empty for any T3 row -- C-26 fail.
FAILS: RESPONDS-TO column empty or None -- C-26 fail.
FAILS: RESPONDS-TO references a participant not present in T1 or T2 grids -- C-26 fail.

---

### Agenda Decision Check

| Agenda Item | Discussed? | Decision Reached? | Outcome Token | Deferred? |
|-------------|------------|-------------------|---------------|-----------|
| [item 1]    | Yes        | Yes               | [vocab token] | No        |
| [item 2]    | Yes        | Yes               | [vocab token] | Yes -- escalation: [path] |

FAILS: Outcome Token not from committed vocabulary -- C-24 fail.
FAILS: agenda item discussed without decision or deferral -- C-03 fail.

### Dissent Collection

For every participant who could plausibly dissent -- regardless of tier:

| Participant | Role | Tier | STANCE | Dissent Statement | Inertia Token |
|-------------|------|------|--------|-------------------|---------------|
| [name]      | [role] | T1 | BLOCK  | [objection in role voice] | INERTIA-FINDING-N |
| [name]      | [role] | T2 | CONDITION | [conditional objection] | INERTIA-FINDING-N |
| [name]      | [role] | T3 | SUPPORT | No dissent | Resolved: INERTIA-FINDING-N -- [what resolved it] |

FAILS: Inertia Token column empty for any row -- C-27 fail.
FAILS: "No dissent" row without resolved inertia justification -- C-27 fail.
FAILS: BLOCK or CONDITION STANCE without named inertia token -- C-27 fail.
FAILS: role-based tension exists but participant marked SUPPORT without basis -- C-05 fail.

*Phase 1 complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: Phase 1 complete, all grids populated, chain check passed.*
*Exit: all formal minutes sections present, all tokens traceable to registries.*

### Meeting Header

| Field | Value |
|-------|-------|
| Committee Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Simulated Date | [date] |
| Chair | [role] |
| Quorum Status | [met / not met -- N required, N present] |
| Vocabulary Contract | [committed vocabulary tokens] |

FAILS: header absent or Type field empty -- C-01 fail, C-06 partial.

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [text]   | [vocabulary token only] | [or --] |

FAILS: Outcome token not from committed vocabulary -- C-24 fail.
FAILS: Outcome column empty -- C-03 fail.
FAILS: Decisions table absent -- C-03 fail.

### Verdict

> **Verdict: [committed vocabulary token] -- [one-sentence rationale citing key T1/T2 findings]**

FAILS: Verdict token not from committed vocabulary -- C-24 fail.
FAILS: Verdict absent -- C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [text] | [Name / Role] | [milestone or date] |

FAILS: Owner column empty for any row -- C-04 fail.
FAILS: table absent when Phase 1 raised open questions -- C-04 fail.
FAILS: owner listed as TBD without escalation path -- C-04 partial.

### Dissenting Opinions

Carry forward from Phase 1 Dissent Collection. All rows must retain Inertia Token.

| Participant | Role | Tier | Objection | Inertia Token |
|-------------|------|------|-----------|---------------|
| [name]      | [role] | T1 | [objection in role voice] | INERTIA-FINDING-N |

*No dissent -- unanimous.*
*Inertia concerns resolved: INERTIA-FINDING-N -- [evidence stated in Phase 1]*

FAILS: dissent row without Inertia Token -- C-27 fail.
FAILS: "No dissent" without inertia-resolution statement -- C-27 fail.
FAILS: known role-based tension from Phase 1 omitted -- C-05 fail.

### Pre-Mortem Risk (expansion of CHAIN-3)

The pre-mortem risk stated here must expand the CHAIN-3 draft from the Phase 1 chain check.
Inconsistency between CHAIN-3 and this section is a C-19 fail.

**PRE-MORTEM RISK -- [Designated Inertia Challenger from Block 4] ([Role]):**
[Full risk statement -- non-obvious, outside-in]
Outside-in basis: [state explicitly why a competent internal reviewer would not predict this]
Inertia basis: INERTIA-FINDING-N -- "[the normalized belief that makes this risk invisible]"

FAILS: pre-mortem risk not from designated Challenger -- C-20 partial.
FAILS: outside-in basis circular (derives from internal knowledge) -- C-09/C-19 fail.
FAILS: no inertia token cited -- C-27 partial.
FAILS: inconsistency with CHAIN-3 draft -- C-19 fail.

### Charter Constraints Honored

| Constraint | Requirement (from Phase 0) | Applied | Notes |
|------------|---------------------------|---------|-------|
| Quorum     | [from Phase 0]             | Yes / No | [count required vs present] |
| Veto       | [from Phase 0]             | Exercised / Waived | [outcome] |
| Escalation | [from Phase 0]             | Applicable / N/A | [path] |
| Scope      | [from Phase 0]             | Honored | [boundary] |

FAILS: fewer than two rows confirmed from Phase 0 constraints -- C-10 partial.

### AMEND (if invoked)

If AMEND was invoked:
- AMEND attendees: re-run Block 2 tier pre-assignment; re-run Phase 0 roster; re-run
  Phase 1 grids with new participant inserted at the correct tier position.
- AMEND scope: re-run Phase 0 agenda; re-run affected Phase 1 discussion items.
- Re-evaluate Block 3 inertia inventory if AMEND changes the committee composition.

FAILS: AMEND invoked but Blocks or Phase 0 not re-executed from amended inputs -- C-08 fail.
FAILS: amendment applied only to Phase 2 output without re-running Phase 1 grids -- C-08 partial.

*Phase 2 complete. Minutes produced. All tokens traceable to pre-committed registries.*
```
