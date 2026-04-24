Now I have everything I need. The R6 rubric added C-17–C-20 (inertia hypothesis gate, NORM-\* labeled inventory, PRE-MORTEM CHAIN CHECK, Designated Inertia Challenger). The R3 variations covered phrasing register, table format, lifecycle phases, criterion annotation, and a combination. R6 variations should target the new inertia traceability chain structurally.

---

# corps-committee -- Prompt Variations R6

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Inertia framing — NORM-\* inventory as Phase 0 structural backbone | Anchoring a labeled NORM inventory (NORM-01..NORM-N) at Gate 0-B before any roster work forces the Phase 1 grid's Inertia Challenge? column to cite a NORM by name; C-18 end-to-end traceability becomes a structural property rather than a fill instruction, making circular or unsourced outside-in claims impossible to produce without visible omissions. |
| V-02 | Role pre-assignment — Designated Inertia Challenger locked before Phase 0 | Pre-assigning the Designated Inertia Challenger as an explicit named block — with rationale and NORM label obligation — before the Phase 0 roster is built makes C-20 a mandatory named slot, not a grid-wide suggestion satisfiable by any convenient participant. The model cannot begin Phase 0 without committing a specific role, a rationale, and a NORM citation obligation. |
| V-03 | Lifecycle emphasis — PRE-MORTEM CHAIN CHECK as a hard blocking gate | Isolating CHAIN-1/CHAIN-2/CHAIN-3 as a standalone structural gate with an explicit DO NOT PROCEED instruction and a fail-if-skipped annotation at the Phase 1→2 boundary — rather than embedding it as a fill rule inside Phase 2 — makes the checkpoint structurally impossible to bypass; C-19 compliance becomes a condition of output existence. |
| V-04 | Combined: NORM inventory + Designated Challenger + CHAIN CHECK (C-18/19/20 full integration) | Combining all three new R6 criteria into one skill creates a closed inertia traceability loop: NORM labels originate at Gate 0-B → Designated Challenger is assigned to a specific NORM obligation at pre-Phase-0 → CHAIN CHECK verifies the connection at Phase 1→2 → Phase 2 output cites the NORM by name. End-to-end traceability without a gap means no single criterion can be satisfied by a circular or generic claim. |
| V-05 | Combined: Table format (C-16) + NORM inventory + CHAIN CHECK + full criterion annotation (C-14) | Combining structural table grammar (violations appear as missing cells, not buried prose) with NORM-labeled inventory (C-18), the CHAIN CHECK gate (C-19), and criterion ID annotations on every FAILS entry (C-14) produces the most self-auditing artifact possible. A reviewer scanning column presence alone — without reading prose — can confirm C-18/C-19/C-20 compliance. |

---

## V-01 -- Inertia Framing (NORM-\* Inventory as Phase 0 Structural Backbone)

**Axis:** Inertia framing
**Hypothesis:** Anchoring a labeled NORM inventory at Gate 0-B before any roster or agenda work forces the Phase 1 discussion grid to cite NORM labels by name. The model cannot produce an Inertia Challenge? column entry without tracing it to a specific named organizational belief. C-18 traceability becomes structural rather than aspirational.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Execute in three phases.
The inertia inventory (NORM-*) must be completed before Phase 0 begins.
Do not simulate any participant voice until the NORM inventory is locked.

---

## BEFORE YOU START

Identify your committee type. Commit to its primary obligation and fail condition.

**ROB (Product Review / Service Review)**
Primary obligation: A readiness verdict backed by metric evidence.
Fail condition: If your output contains no metric, you have not done a ROB. Add the metric
before continuing. (C-01 fail)

**SHIPROOM (Go / No-Go)**
Primary obligation: A binary GO or NO-GO decision backed by a named risk register.
Fail condition: If your minutes contain no GO/NO-GO decision line, you produced a discussion
summary. Add the decision line. (C-01 fail, C-03 fail)

**ARCH-BOARD (Architecture Decision Review)**
Primary obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: Trade-off list without a selected winner = arch-board not done. Name the
decision. (C-01 fail)

Write before proceeding:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic under review]

---

## GATE 0-B -- INERTIA INVENTORY

Before building the roster, identify what this committee will rubber-stamp without challenge.

Answer: *What assumptions have become invisible to this committee because they have been
true for a long time, been built into prior decisions, or been accepted as default operating
conditions?*

Produce a labeled inventory. Each item must be a specific named organizational belief --
not a category heading. At least one item must reflect an observable organizational behavior.

| Label | Named Organizational Belief |
|-------|-----------------------------|
| NORM-01 | [specific assumption the committee holds as default] |
| NORM-02 | [specific assumption the committee holds as default] |
| NORM-03 | [specific assumption] |
| [add more as needed] | |

FAILS: inventory is a single sentence rather than labeled items -- C-18 fail.
FAILS: all items are generic risk categories rather than named beliefs -- C-18 fail.
FAILS: no item reflects an observable organizational behavior -- C-18 partial.
FAILS: NORM inventory absent when Phase 0 begins -- C-17 fail, C-18 fail.

*NORM inventory locked. Entering Phase 0.*

---

## PHASE 0 -- SETUP

*Entry: NORM inventory locked.*
*Exit: roster confirmed, agenda locked, charter constraints identified, NORM labels assigned
to the Inertia Challenger.*

### 0.1 -- Type and Topic Declaration

Write:
> Committee type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

### 0.2 -- Participant Roster

Load .roles/ for this committee type. List every participant with their role and
primary concern for this meeting.

For any required function without a charter role:
  [Candidate: [role function] -- pending Phase 1 confirmation]

| Seq | Participant | Role | Primary Concern | Charter Status | NORM Assignment |
|-----|-------------|------|-----------------|----------------|-----------------|
| 1 | [name] | [role] | [one concern] | [Standing / Candidate] | -- |
| 2 | [name] | [role] | [concern] | [Standing / Candidate] | -- |
| ... | | | | | |
| [N] | [Designated Inertia Challenger] | [role] | [concern] | [Standing / Candidate] | [NORM-XX, NORM-YY] |

The Designated Inertia Challenger is the participant whose frame is least likely to
reflect the normalized assumptions in the NORM inventory. Assign them the NORM labels
they are obligated to challenge. Their NORM Assignment cell must be non-empty.

FAILS: participant concern mismatches their role function -- C-02 fail.
FAILS: Designated Inertia Challenger has an empty NORM Assignment cell -- C-20 fail.
FAILS: no participant is designated as Inertia Challenger -- C-20 fail.
FAILS: injection candidate not annotated in Charter Status -- C-12 fail.
FAILS: required function left uncovered without annotation -- C-11 fail.

### 0.3 -- Agenda

List 3-5 agenda items appropriate to the committee type. Each item must be type-specific.

ROB: readiness gates, metric review, blocking issues.
SHIPROOM: go/no-go criteria, risk register items, named release blockers.
ARCH-BOARD: named alternatives under consideration, decision criteria, ADR outcome.

FAILS: agenda item applicable to any committee type without modification -- C-07 fail.
FAILS: agenda not locked before Phase 1 begins -- C-06 partial.

### 0.4 -- Charter Constraints

Identify at least two charter constraints from .roles/ that must be honored in Phase 1:
- Quorum requirement.
- Veto holder and conditions.
- Escalation path for deferred decisions.
- Scope boundary.

FAILS: fewer than two constraints identified at Phase 0 exit -- C-10 partial.

*Phase 0 complete. NORM labels assigned. Challenger designated. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 complete -- roster confirmed, NORM labels assigned.*
*Exit: all agenda items discussed, decisions recorded, dissent captured,
PRE-MORTEM CHAIN CHECK confirmed.*

### 1.1 -- Discussion Grid

Simulate each participant in the sequence declared in Phase 0.
Each participant speaks from their role function. No participant leads outside their domain.

For each contribution, record:
- Type-specific evidence (metric / risk / trade-off per committee type).
- Inertia Challenge? -- if this participant is the Designated Inertia Challenger, cite the
  NORM label(s) being challenged. For all other participants, record "--".

| Seq | Participant | Role | Contribution Summary | Evidence | Inertia Challenge? |
|-----|-------------|------|----------------------|----------|--------------------|
| 1 | [name] | [role] | [summary] | [evidence] | -- |
| 2 | [name] | [role] | [summary] | [evidence] | -- |
| ... | | | | | |
| [N] | [Challenger] | [role] | [summary] | [evidence] | [NORM-XX: outside-in basis] |

Prose expansion for each participant follows the grid:

**[Participant] ([Role]):** [Full contribution -- must reference type-specific evidence and
speak exclusively from their role domain.]

Role-voice constraints (enforce hard):
- PM: customer value, readiness, release timing. Never leads on deployment topology.
- SRE/Ops: reliability, SLOs, operational risk. Never leads the product vision.
- Architect: system design, trade-offs, constraints. Never owns the business case.
- Security: threat model, compliance gaps. Never owns the delivery schedule.
- Engineering Lead: implementation feasibility, technical debt. Never owns the customer narrative.

FAILS: participant contribution misaligns with role function -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.
FAILS: Inertia Challenge? cell is "--" for the Designated Challenger -- C-20 fail.
FAILS: NORM label cited but basis is circular (derived from internal knowledge) -- C-17 partial.

### 1.2 -- Decision Check

Record every decision reached:
- approved / rejected / deferred / conditional-approval

FAILS: agenda item discussed without a decision or deferral noted -- C-03 fail.
FAILS: deferred item has no escalation path -- C-10 partial.

### 1.3 -- Dissent Check

Identify any participant whose role creates tension with the majority outcome.

FAILS: role-based tension exists but dissent not recorded -- C-05 fail.

---

## PRE-MORTEM CHAIN CHECK

**DO NOT PROCEED TO PHASE 2 UNTIL ALL THREE CHECKPOINTS ARE CONFIRMED.**

This gate must appear between Phase 1 and Phase 2. A Phase 2 that begins before
this gate is confirmed is a criterion failure.

**CHAIN-1 -- Challenger is identified and non-None**
State: The Designated Inertia Challenger is: [participant name], [role].
Confirmed: [ ] Yes -- Challenger identified. [ ] FAIL -- no challenger = C-20 fail.

**CHAIN-2 -- Outside-in basis is stated and non-circular**
State: The outside-in basis for the pre-mortem risk is: [basis statement].
Test: Does this basis derive from internal organizational knowledge or general reasoning?
If yes, the basis is circular and does not satisfy C-17. Restate with an external frame.
Confirmed: [ ] Non-circular basis stated. [ ] FAIL -- circular basis = C-17 fail, C-19 fail.

**CHAIN-3 -- Risk draft connected to stated NORM label**
State: The pre-mortem risk is: [risk draft, one sentence].
State: This risk traces to: [NORM-XX]: [belief text from NORM inventory].
Confirmed: [ ] NORM citation present. [ ] FAIL -- no NORM trace = C-18 fail, C-19 fail.

Phase 2 may begin only after all three checkpoints are confirmed with no FAIL states.

FAILS: Phase 2 content inconsistent with CHAIN-3 risk draft -- C-19 fail.

*PRE-MORTEM CHAIN CHECK complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: PRE-MORTEM CHAIN CHECK confirmed.*
*Exit: formal minutes produced with all required sections.*

### Meeting Header

| Field | Value |
|-------|-------|
| Committee Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Simulated Date | [date] |
| Chair | [role name] |
| Quorum Status | [met / not met -- N required, N present] |

### Pre-Mortem Risk

**Raised by:** [Designated Inertia Challenger], [Role]
**NORM trace:** [NORM-XX] -- [belief text]
**Outside-in basis:** [basis statement from CHAIN-2]
**Risk:** [expanded from CHAIN-3 draft]

FAILS: pre-mortem risk absent -- C-09 fail.
FAILS: NORM trace absent or mismatched from CHAIN-3 -- C-18 fail.
FAILS: outside-in basis predictable by a competent internal reviewer -- C-09 outside-in gate not cleared.

### Decisions

**Decisions**
- [decision] -- [approved / rejected / deferred / conditional-approval]

FAILS: Decisions section absent -- C-03 fail.
FAILS: outcome absent for any decision -- C-03 fail.

### Action Items

**Action Items**
- [action] -- Owner: [Name / Role]

FAILS: action item without an owner -- C-04 fail.
FAILS: no action items despite open questions in Phase 1 -- C-04 fail.

### Dissenting Opinions

- [Participant] ([Role]): [objection in role voice]

Unanimous: *No dissent recorded -- unanimous.*

FAILS: role-based tension from Phase 1 omitted -- C-05 fail.

### Charter Constraints Honored

- Quorum: [met / not met] -- [count required vs. present]
- Veto: [exercised / waived] -- [role holding veto]
- Escalation: [named path, if any decision deferred]
- Scope: [boundary honored -- what is excluded]

FAILS: fewer than two constraints named with charter sourcing -- C-10 partial.

### AMEND (if invoked)

Apply before generating output.

AMEND attendees: add to Phase 0 roster; insert contribution in Phase 1 grid.
AMEND scope: revise Phase 0 agenda; revise affected Phase 1 contributions.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-02 -- Role Pre-Assignment (Designated Inertia Challenger Locked Before Phase 0)

**Axis:** Role pre-assignment
**Hypothesis:** Moving the Designated Inertia Challenger block to a mandatory pre-Phase-0 position — with an explicit rationale requirement and a named NORM obligation — prevents the model from satisfying C-20 with a grid-wide instruction. The outside-in obligation is a named slot that must be filled before simulation is permitted to begin.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Produce mock meeting minutes.

Before Phase 0 begins, you must designate the Inertia Challenger. This designation
cannot be deferred. The skill does not proceed until the Challenger is named.

---

## BEFORE YOU START

Commit to your committee type and its obligation.

**ROB:**
Obligation: Readiness verdict backed by metric evidence.
Fail: No metric in output = ROB not done. (C-01 fail)

**SHIPROOM:**
Obligation: Binary GO/NO-GO decision backed by a risk register.
Fail: No GO/NO-GO line in output = shiproom not done. (C-01 fail, C-03 fail)

**ARCH-BOARD:**
Obligation: ADR with named trade-offs and selected alternative.
Fail: Trade-off list without a winner = arch-board not done. (C-01 fail)

Write:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

---

## PRE-PHASE-0: INERTIA CHALLENGER DESIGNATION

Complete this block before building the roster.

### Step A -- Inertia Inventory

Identify what this committee will normalize without challenge. Name at least three
specific organizational beliefs -- not category headings.

| Label | Named Belief (specific, observable) |
|-------|--------------------------------------|
| NORM-01 | |
| NORM-02 | |
| NORM-03 | |

FAILS: fewer than three NORM items -- C-18 partial.
FAILS: items are generic risk categories rather than named beliefs -- C-18 fail.
FAILS: no NORM item reflects an observable organizational behavior -- C-18 partial.

### Step B -- Challenger Selection

Identify the participant whose perspective is least likely to reflect the NORM inventory.
Write:

**Designated Inertia Challenger:** [participant name], [role from .roles/]
**Rationale:** [Why is this participant's frame least likely to reflect the normalized
assumptions? Must name a specific structural reason -- industry position, external
accountability, technical domain independence, or similar. Saying "external perspective"
without a structural basis does not satisfy this criterion.]
**NORM Obligation:** This participant must challenge [NORM-XX] and [NORM-YY] in Phase 1.
Their Inertia Challenge? cell must not be None.

FAILS: Challenger not named before Phase 0 -- C-20 fail.
FAILS: rationale is generic ("external perspective") without structural basis -- C-20 partial.
FAILS: NORM obligation not stated -- C-20 fail, C-18 partial.
FAILS: no participant qualifies and no injection candidate is noted -- C-11 partial.

*Challenger designated. NORM obligations committed. Entering Phase 0.*

---

## PHASE 0 -- SETUP

*Entry: Challenger designated and NORM obligations committed.*
*Exit: roster confirmed, agenda locked, charter constraints identified.*

### Participant Roster

Load .roles/ for this committee type. List participants. The Designated Inertia
Challenger appears in the roster with their NORM obligation pre-populated.

For any required function without a charter role:
  [Candidate: [role function] -- pending Phase 1 confirmation]

| Seq | Participant | Role | Primary Concern | Charter Status | NORM Obligation |
|-----|-------------|------|-----------------|----------------|-----------------|
| [DIC row] | [Challenger name] | [role] | [concern] | Standing | [NORM-XX, NORM-YY] |
| [others] | | | | | -- |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: Challenger row absent or NORM Obligation empty -- C-20 fail.
FAILS: injection candidate present but Charter Status not annotated -- C-12 fail.

### Agenda

List 3-5 type-specific agenda items.

ROB: readiness gates, metric review, blocking issues.
SHIPROOM: go/no-go criteria, risk register items, named release blockers.
ARCH-BOARD: named alternatives, decision criteria, ADR outcome.

FAILS: item applicable to any committee type without modification -- C-07 fail.

### Charter Constraints

Name at least two charter constraints from .roles/ to honor in Phase 1:
- Quorum requirement.
- Veto holder and conditions.
- Escalation path.
- Scope boundary.

FAILS: fewer than two constraints before Phase 0 exits -- C-10 partial.

*Phase 0 complete. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 complete.*
*Exit: agenda discussed, decisions recorded, dissent captured, Challenger has challenged
their assigned NORM labels.*

Simulate each participant in sequence from the Phase 0 roster.
Each participant speaks from their role function and no other.

For each participant, produce:

**[Participant] ([Role]):** [Contribution]
- Evidence: [type-specific: metric / risk / trade-off]
- Inertia Challenge?: [NORM label + outside-in basis -- required for Designated Challenger;
  "--" for all others]

The Designated Inertia Challenger's contribution must:
1. Challenge the NORM labels assigned in Pre-Phase-0 Step B.
2. State an outside-in basis that does not derive from internal team knowledge.
3. Surface a risk the organization has normalized into invisibility.

Role-voice constraints:
- PM: customer value, readiness, release timing. Never leads on deployment topology.
- SRE/Ops: reliability, SLOs, operational risk. Never leads product vision.
- Architect: system design, trade-offs, constraints. Never owns the business case.
- Security: threat model, compliance gaps. Never owns the delivery schedule.
- Engineering Lead: implementation feasibility, technical debt. Never owns the customer narrative.

FAILS: participant speaks outside their role function -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.
FAILS: Challenger's Inertia Challenge? is "--" or None -- C-20 fail.
FAILS: Challenger's outside-in basis derives from internal knowledge -- C-17 fail.
FAILS: NORM label in Challenger's cell does not match a label from Pre-Phase-0 -- C-18 fail.

Decisions after each agenda item:
- Record outcome: approved / rejected / deferred / conditional-approval.

FAILS: agenda item discussed without a decision or deferral -- C-03 fail.

Dissent:
- Any participant in role-based tension with the majority outcome must be recorded.

FAILS: role-based tension exists but dissent absent -- C-05 fail.

---

## PRE-MORTEM CHAIN CHECK

Block Phase 2 until confirmed.

**CHAIN-1:** Challenger is identified and non-None.
> Challenger: [name], [role]. Confirmed: Yes / FAIL.

**CHAIN-2:** Outside-in basis is stated and non-circular.
> Basis: [statement]. Does this derive from internal knowledge? If yes: restate.
> Confirmed: Non-circular / FAIL.

**CHAIN-3:** Risk draft is connected to a NORM label.
> Risk: [one-sentence draft].
> Traces to: [NORM-XX]: [belief text].
> Confirmed: NORM cited / FAIL.

Phase 2 may not begin if any checkpoint is FAIL.

FAILS: any CHAIN checkpoint is FAIL at Phase 2 entry -- C-19 fail.
FAILS: Phase 2 pre-mortem risk inconsistent with CHAIN-3 draft -- C-19 fail.

*CHAIN CHECK complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: PRE-MORTEM CHAIN CHECK confirmed.*

Produce formal minutes with all sections:

1. **Meeting Header** -- type, topic, simulated date, chair, quorum status.
2. **Participants** -- roster with roles and concerns.
3. **Agenda** -- as locked in Phase 0.
4. **Discussion Summary** -- per-participant contributions with type-specific evidence.
5. **Pre-Mortem Risk** -- Challenger's full contribution; cite NORM trace and outside-in basis.
6. **Decisions** -- labeled with outcomes.
7. **Action Items** -- each with owner.
8. **Dissenting Opinions** -- or "unanimous."
9. **Charter Constraints Honored** -- at least two, per Phase 0 identification.
10. **Next Steps**.

FAILS: any section from 1-7 absent -- C-06 fail.
FAILS: pre-mortem risk section absent or NORM trace missing -- C-09 fail, C-18 fail.
FAILS: action item without owner -- C-04 fail.
FAILS: fewer than two charter constraints named -- C-10 partial.

### AMEND (if invoked)

Apply before generating output. Re-enter Pre-Phase-0 if the Challenger role changes.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-03 -- Lifecycle Emphasis (PRE-MORTEM CHAIN CHECK as Hard Blocking Gate)

**Axis:** Lifecycle emphasis
**Hypothesis:** Isolating the PRE-MORTEM CHAIN CHECK as a standalone structural gate with a hard DO NOT PROCEED instruction, explicit fail-state labeling per checkpoint, and a consistency test between CHAIN-3 and Phase 2 output makes the checkpoint impossible to embed, defer, or subsume into prose fill rules. C-19 compliance becomes observable as a structural requirement, not an aspirational annotation.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. The skill has four structural stages:
STAGE-0 (commit), STAGE-1 (setup), STAGE-2 (simulate), STAGE-3 (minutes).
Each stage has a hard entry gate. STAGE-3 has an additional blocking gate:
the PRE-MORTEM CHAIN CHECK. Do not advance past any gate without completing it.

---

## STAGE-0 -- TYPE COMMIT

**BEFORE ANY OTHER WORK,** write these two lines:

> Committee type: [ROB / SHIPROOM / ARCH-BOARD]
> Primary obligation: [state it in one sentence from the table below]

| Type | Primary Obligation | Automatic Fail |
|------|--------------------|----------------|
| ROB | Readiness verdict backed by metric evidence | No metric in output = C-01 fail |
| SHIPROOM | Binary GO/NO-GO decision backed by a risk register | No GO/NO-GO line = C-01 fail, C-03 fail |
| ARCH-BOARD | ADR with named trade-offs and selected alternative | No ADR with decision = C-01 fail |

Do not proceed to STAGE-1 until both lines are written.

---

## STAGE-1 -- SETUP

*Gate: STAGE-0 complete.*

### 1.1 -- Inertia Inventory (Gate 0-B)

Before building the roster: identify what this committee will accept without challenge.

Ask: *What have the committee's prior decisions, standing assumptions, and operational
defaults made invisible to the people in this room?*

Name at least three specific organizational beliefs. Each must be independently citeable.
At least one must reflect a behavioral pattern, not just a technical assumption.

| Label | Named Belief |
|-------|--------------|
| NORM-01 | [specific assumption held as default] |
| NORM-02 | [specific assumption held as default] |
| NORM-03 | [specific assumption held as default] |

FAILS: inventory present but labels are category headings -- C-18 fail.
FAILS: inventory absent -- C-17 fail, C-18 fail.
FAILS: no item reflects an observable behavioral pattern -- C-18 partial.

### 1.2 -- Designated Inertia Challenger

Identify the participant who is least likely to share the NORM inventory assumptions.
Name them. State why their frame is structurally distinct. Assign their NORM obligation.

**Designated Inertia Challenger:** [name], [role]
**Structural rationale:** [specific reason their frame differs -- not generic]
**NORM obligation:** Must challenge [NORM-XX] in STAGE-2.

FAILS: Challenger not designated in STAGE-1 -- C-20 fail.
FAILS: rationale is non-structural -- C-20 partial.
FAILS: NORM obligation not assigned -- C-18 fail.

### 1.3 -- Participant Roster

Load .roles/ for this committee type.

| Seq | Participant | Role | Primary Concern | Charter Status |
|-----|-------------|------|-----------------|----------------|
| [DIC] | [Challenger] | [role] | [concern] | Standing |
| ... | | | | |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: required function without annotation -- C-11 fail.
FAILS: injection pending but Charter Status not annotated -- C-12 fail.

### 1.4 -- Agenda

3-5 type-specific agenda items.

FAILS: item generic, not type-specific -- C-07 fail.

### 1.5 -- Charter Constraints

At least two from .roles/:

| Constraint | Requirement | Honor condition |
|------------|-------------|-----------------|
| [quorum / veto / escalation / scope] | [from charter] | [how Phase 2 satisfies it] |

FAILS: fewer than two constraints before STAGE-2 -- C-10 partial.

*STAGE-1 complete. Entering STAGE-2.*

---

## STAGE-2 -- SIMULATION

*Gate: STAGE-1 complete. NORM inventory locked. Challenger designated.*

Simulate each participant in roster sequence. Each speaks from their role function only.

**[Participant] ([Role]):**
Contribution: [full contribution -- type-specific evidence required]
Evidence type: [metric / risk / trade-off]
Inertia Challenge? [-- for most; NORM-XX + outside-in basis for Designated Challenger]

Type-specific evidence required per contribution:
- ROB: specific metric or readiness indicator.
- SHIPROOM: named risk or release blocker.
- ARCH-BOARD: named trade-off or architectural constraint.

Role-voice constraints (hard):
- PM: customer value, readiness, release timing. Not deployment topology.
- SRE/Ops: reliability, SLOs, operational risk. Not product vision.
- Architect: system design, trade-offs. Not business case.
- Security: threat model, compliance. Not delivery schedule.
- Engineering Lead: feasibility, tech debt. Not customer narrative.

The Designated Inertia Challenger must:
- Cite the NORM label they are challenging.
- State an outside-in basis that is non-circular (not derived from internal knowledge).
- Surface a risk the committee's prior decisions have made invisible.

Record decisions after each agenda item. Record dissent for any role in tension with
the majority outcome.

FAILS: participant speaks outside role domain -- C-02 fail.
FAILS: contribution lacks type-specific evidence -- C-07 fail.
FAILS: Challenger's Inertia Challenge? is "--" -- C-20 fail.
FAILS: Challenger's outside-in basis is circular -- C-17 fail.
FAILS: NORM label in Challenger cell not in STAGE-1 inventory -- C-18 fail.
FAILS: agenda item without decision or deferral -- C-03 fail.
FAILS: role-based tension unrecorded -- C-05 fail.

---

## PRE-MORTEM CHAIN CHECK

**THIS IS A HARD BLOCKING GATE. STAGE-3 MAY NOT BEGIN UNTIL ALL THREE CHAINS CONFIRM.**

If any chain confirms FAIL, the failure must be resolved before writing a single line
of STAGE-3 output. A STAGE-3 that begins with an unconfirmed chain is a C-19 criterion
failure regardless of the output's content.

---

**CHAIN-1: Designated Inertia Challenger is identified and non-None**

State:
> Challenger: [name], [role].
> Status: CONFIRMED / FAIL

If FAIL: return to STAGE-1.2 and designate a Challenger. Do not advance.

---

**CHAIN-2: Outside-in basis is stated and non-circular**

State:
> Outside-in basis: [one sentence describing the external frame of reference].
> Is this basis derived from the team's internal knowledge or general domain reasoning?
>   If yes: CIRCULAR FAIL. Restate from an external vantage point. Do not advance.
>   If no: CONFIRMED.

Circular examples that fail this gate:
- "The SRE will surface reliability concerns from their operational experience." (internal)
- "The Architect raises a general scalability concern." (general reasoning)

Non-circular examples that pass:
- "The external auditor's independence from the delivery chain means their prior finding
  on [specific constraint] is not visible to the team." (structural external vantage)

---

**CHAIN-3: Risk draft is connected to a NORM label**

State:
> Risk draft: [one sentence].
> Traces to: [NORM-XX]: [exact belief text from STAGE-1 inventory].
> Status: CONFIRMED / FAIL

If FAIL: return to STAGE-2 and produce a risk that traces to a NORM label.

---

*All three chains confirmed. Entering STAGE-3.*

FAILS: STAGE-3 output inconsistent with CHAIN-3 risk draft -- C-19 fail.
FAILS: any chain was in FAIL state at STAGE-3 entry -- C-19 fail.

---

## STAGE-3 -- MINUTES

*Gate: PRE-MORTEM CHAIN CHECK confirmed on all three chains.*

Produce formal meeting minutes:

**Meeting Header**
| Field | Value |
|-------|-------|
| Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Date | [simulated date] |
| Chair | [role] |
| Quorum | [met / not met -- N required, N present] |

**Participants** -- roster as in STAGE-1.

**Agenda** -- items as locked in STAGE-1.

**Discussion Summary** -- per-participant contributions with evidence.

**Pre-Mortem Risk**
- Raised by: [Challenger name], [role]
- NORM trace: [NORM-XX] -- [belief text]
- Outside-in basis: [from CHAIN-2]
- Risk: [expanded from CHAIN-3 draft]

FAILS: pre-mortem risk section absent -- C-09 fail.
FAILS: NORM trace absent or mismatched -- C-18 fail.
FAILS: risk predictable by insiders without NORM context -- C-09 partial.

**Decisions**
- [decision] -- [approved / rejected / deferred / conditional-approval]

FAILS: Decisions section absent -- C-03 fail.
FAILS: outcome missing for any item -- C-03 fail.

**Action Items**
- [action] -- Owner: [Name / Role]

FAILS: action without owner -- C-04 fail.
FAILS: no items when STAGE-2 raised open questions -- C-04 fail.

**Dissenting Opinions**
- [Participant] ([Role]): [objection in role voice]
OR: *No dissent -- unanimous.*

FAILS: dissent absent when role-based tension exists -- C-05 fail.

**Charter Constraints Honored**
- [constraint] -- [requirement] -- [honored how]
(At least two, sourced from STAGE-1.5)

FAILS: fewer than two named -- C-10 partial.

**AMEND (if invoked)**
Apply before generating output. Re-enter STAGE-1 if the Challenger changes.

FAILS: AMEND invoked but output not regenerated -- C-08 fail.

*STAGE-3 complete. Minutes produced.*
```

---

## V-04 -- Combined: NORM Inventory + Designated Challenger + CHAIN CHECK (C-18/19/20 Full Integration)

**Axis:** Inertia framing + role pre-assignment + lifecycle gate
**Hypothesis:** Combining C-18, C-19, and C-20 into a single skill creates a closed inertia traceability loop with no gap: NORM labels are named at Gate 0-B → the Designated Challenger is bound to specific NORM labels before Phase 0 → the CHAIN CHECK verifies the Challenger-to-NORM-to-risk connection at the Phase 1-to-2 boundary → Phase 2 output cites the NORM by name. Every criterion in the chain has a structural predecessor, making vacuous satisfactions structurally impossible.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. The skill enforces a closed
inertia-traceability chain: every pre-mortem risk in the output must trace back
to a named organizational belief (NORM label) through a designated role holder whose
outside-in basis has been verified as non-circular before simulation begins.

Execute in three phases. Complete the CHALLENGER DESIGNATION block before Phase 0.

---

## BEFORE YOU START

Commit to your committee type.

| Type | Primary Obligation | Automatic Fail Condition |
|------|--------------------|--------------------------|
| ROB | Readiness verdict backed by metric evidence | No metric = ROB not done (C-01) |
| SHIPROOM | Binary GO/NO-GO decision backed by a risk register | No GO/NO-GO line = shiproom not done (C-01, C-03) |
| ARCH-BOARD | ADR with named trade-offs and selected alternative | Trade-offs without decision = arch-board not done (C-01) |

Write:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

---

## INERTIA SETUP (before Phase 0)

Complete both blocks below before building the roster. These outputs govern the entire
simulation. Do not defer them to Phase 1.

### Block A -- NORM Inventory

Identify what this committee has normalized. Answer: *Which specific assumptions have
been accepted as default by this committee's prior decisions, standing practices, or
organizational context -- and are therefore no longer visible as assumptions?*

Produce a labeled inventory. Each item names a specific belief. At least one must
name an observable organizational behavior.

| Label | Named Belief | Behavioral? |
|-------|--------------|-------------|
| NORM-01 | [specific assumption held as default] | Yes / No |
| NORM-02 | [specific assumption held as default] | Yes / No |
| NORM-03 | [specific assumption] | Yes / No |
| [add as needed] | | |

FAILS: labels are category headings, not named beliefs -- C-18 fail.
FAILS: no behavioral item present -- C-18 partial.
FAILS: inventory absent before Phase 0 -- C-17 fail, C-18 fail.

### Block B -- Designated Inertia Challenger

Select the participant whose frame is structurally least likely to replicate the NORM
inventory. Make the following commitments:

**Designated Inertia Challenger:** [name], [role from .roles/]

**Structural rationale:** [Why is this participant's frame structurally distinct from
the committee's normalized assumptions? State a structural reason -- their organizational
position, accountability structure, external domain, or role independence. A claim of
"external perspective" without a structural basis fails this criterion.]

**Assigned NORM obligations:**
- Must challenge: [NORM-XX] -- [brief belief text]
- Must challenge: [NORM-YY] -- [brief belief text] (if applicable)

**Phase 1 commitment:** The Challenger's Inertia Challenge? cell must be non-None.
The Phase 2 pre-mortem risk must expand the CHAIN-3 draft -- not diverge from it.

FAILS: Challenger not designated before Phase 0 -- C-20 fail.
FAILS: rationale is non-structural -- C-20 partial.
FAILS: NORM obligations not assigned -- C-18 fail, C-20 fail.
FAILS: no qualifying participant exists and no injection candidate noted -- C-11 partial.

*NORM inventory locked. Challenger designated. Entering Phase 0.*

---

## PHASE 0 -- SETUP

*Entry: NORM inventory and Challenger designation complete.*
*Exit: roster confirmed, agenda locked, charter constraints identified.*

### Participant Roster

Load .roles/ for this committee type.

| Seq | Participant | Role | Primary Concern | Charter Status | NORM Obligation |
|-----|-------------|------|-----------------|----------------|-----------------|
| [DIC pos] | [Challenger] | [role] | [concern] | Standing | [NORM-XX, NORM-YY] |
| [others] | | | | [Standing / Candidate] | -- |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: Challenger row absent or NORM Obligation empty -- C-20 fail.
FAILS: injection candidate not annotated -- C-12 fail.
FAILS: required function uncovered without annotation -- C-11 fail.

### Agenda

3-5 type-specific items.

ROB: readiness gates, metric review, blocking issues.
SHIPROOM: go/no-go criteria, risk register items, named release blockers.
ARCH-BOARD: named alternatives, decision criteria, ADR outcome.

FAILS: item generic, not type-specific -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

### Charter Constraints

At least two from .roles/:
- Quorum requirement.
- Veto holder and conditions.
- Escalation path.
- Scope boundary.

FAILS: fewer than two constraints before Phase 0 exits -- C-10 partial.

*Phase 0 complete. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 complete.*
*Exit: all agenda items discussed, decisions recorded, dissent captured,
Challenger has challenged their assigned NORM labels.*

Simulate each participant in the Phase 0 sequence. Each speaks from their role function.

For each participant:

**[Participant] ([Role]):** [Contribution -- type-specific evidence required]
**Evidence:** [metric / risk / trade-off per type]
**Inertia Challenge?** [For Challenger: NORM-XX -- [outside-in basis]. For others: --]

Type-specific evidence:
- ROB: specific metric or readiness indicator cited.
- SHIPROOM: named risk or release blocker.
- ARCH-BOARD: named trade-off or architectural constraint.

Role-voice constraints:
- PM: customer value, readiness, release timing. Never leads on deployment topology.
- SRE/Ops: reliability, SLOs, operational risk. Never leads product vision.
- Architect: system design, trade-offs. Never owns the business case.
- Security: threat model, compliance. Never owns the delivery schedule.
- Engineering Lead: feasibility, tech debt. Never owns the customer narrative.

The Designated Inertia Challenger must:
- Cite the NORM label assigned in Block B.
- State an outside-in basis structurally derived from their rationale (not general reasoning).
- Surface a risk the NORM belief has made invisible to the committee.

Decisions per agenda item: approved / rejected / deferred / conditional-approval.
Dissent: record for any participant in role-based tension with the majority outcome.

FAILS: participant speaks outside role domain -- C-02 fail.
FAILS: contribution lacks type-specific evidence -- C-07 fail.
FAILS: Challenger Inertia Challenge? is "--" -- C-20 fail.
FAILS: Challenger outside-in basis is circular -- C-17 fail.
FAILS: NORM label in Challenger cell absent from Block A inventory -- C-18 fail.
FAILS: agenda item without decision or deferral -- C-03 fail.
FAILS: role-based tension unrecorded -- C-05 fail.

---

## PRE-MORTEM CHAIN CHECK

**HARD BLOCK: Phase 2 may not begin until all three chains are confirmed.**

Producing any Phase 2 output before this gate is confirmed is a C-19 fail.

**CHAIN-1 -- Challenger confirmed**
> Challenger: [name], [role]. Source: Block B.
> Confirmed: Yes / FAIL (return to Block B if FAIL)

**CHAIN-2 -- Outside-in basis confirmed as non-circular**
> Basis: [statement].
> Test: Does this basis derive from the team's own knowledge domain or general reasoning?
> Yes = CIRCULAR. Restate using the structural rationale from Block B. Do not advance.
> No = CONFIRMED.

**CHAIN-3 -- Risk draft linked to NORM label**
> Risk draft: [one sentence from Phase 1 Challenger contribution].
> Traces to: [NORM-XX]: [exact belief text from Block A].
> NORM present in Block A: Yes / FAIL (if FAIL: NORM label was not declared -- C-18 fail)

**All three confirmed. Phase 2 may begin.**

FAILS: any chain is in FAIL state at Phase 2 entry -- C-19 fail.
FAILS: Phase 2 pre-mortem risk diverges from CHAIN-3 draft -- C-19 fail.

*CHAIN CHECK complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: PRE-MORTEM CHAIN CHECK confirmed.*

**Meeting Header**

| Field | Value |
|-------|-------|
| Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Simulated Date | [date] |
| Chair | [role] |
| Quorum | [met / not met -- N required, N present] |

**Discussion Summary** -- per-participant contributions with type-specific evidence.

**Pre-Mortem Risk**
- Raised by: [Challenger], [role]
- NORM trace: [NORM-XX] -- [belief text from Block A]
- Outside-in basis: [from CHAIN-2]
- Risk: [expanded from CHAIN-3 draft -- must not contradict CHAIN-3]

FAILS: pre-mortem risk absent -- C-09 fail.
FAILS: NORM trace absent or cites a label not in Block A -- C-18 fail.
FAILS: risk represents only internal concerns reframed externally -- C-09 partial.

**Decisions**
- [decision] -- [outcome]

FAILS: Decisions section absent -- C-03 fail.
FAILS: outcome absent for any item -- C-03 fail.

**Action Items**
- [action] -- Owner: [Name / Role]

FAILS: action without owner -- C-04 fail.
FAILS: no items when Phase 1 left open questions -- C-04 fail.

**Dissenting Opinions**
- [Participant] ([Role]): [objection in role voice]
OR: *Unanimous.*

FAILS: dissent absent when role-based tension exists -- C-05 fail.

**Charter Constraints Honored**

| Constraint | Requirement | Applied | Notes |
|------------|-------------|---------|-------|
| [quorum/veto/escalation/scope] | [from charter] | Yes / No | [detail] |

(At least two rows non-empty)

FAILS: fewer than two constraints named -- C-10 partial.

**AMEND (if invoked)**

If AMEND changes the Challenger role: re-execute Inertia Setup Block B.
If AMEND changes the roster or scope: re-execute Phase 0 and Phase 1 from the amended state.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-05 -- Combined: Table Format + NORM Inventory + CHAIN CHECK + Full Criterion Annotation (C-14/16/18/19)

**Axis:** Output format + inertia framing + lifecycle gate + criterion annotation
**Hypothesis:** Combining structural table grammar (missing cells signal violations without reading prose) with a NORM-labeled inventory (C-18), the PRE-MORTEM CHAIN CHECK blocking gate (C-19), and criterion ID annotations on every FAILS entry (C-14) produces the most self-auditing artifact. A reviewer can confirm C-18/C-19/C-20 compliance by scanning column headers and cell presence alone. No violation hides in prose.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Use tables for every enumerable section.
Every FAILS entry cites the rubric criterion ID it protects. The inertia chain
(NORM inventory → Designated Challenger → PRE-MORTEM CHAIN CHECK) is structural:
its outputs appear as table rows and named checkpoints, not prose annotations.

---

## BEFORE YOU START

Identify your committee type. Commit to its obligation, fail condition, and role sequence.

| Type | Primary Obligation | Role Sequence | Automatic Fail |
|------|--------------------|---------------|----------------|
| ROB | Readiness verdict backed by metric evidence | PM → Eng Lead → SRE → Security → Architect | No metric = C-01 fail |
| SHIPROOM | GO/NO-GO decision backed by risk register | Eng Lead → SRE → Security → PM → Architect | No GO/NO-GO line = C-01, C-03 fail |
| ARCH-BOARD | ADR with named trade-offs and selected alternative | Architect → Eng Lead → Security → SRE → PM | No ADR decision = C-01 fail |

Write:
> **Type:** [ROB / SHIPROOM / ARCH-BOARD] | **Topic:** [topic] | **Sequence:** [from table]

---

## PHASE 0 -- SETUP

*Entry: Type and sequence committed.*
*Exit: NORM inventory locked, Challenger designated, roster confirmed, agenda locked,
charter constraints identified.*

### Table 0-A: NORM Inventory

What will this committee normalize without challenge?

| Label | Named Belief | Behavioral? |
|-------|--------------|-------------|
| NORM-01 | [specific assumption held as default] | Yes / No |
| NORM-02 | [specific assumption held as default] | Yes / No |
| NORM-03 | [specific assumption] | Yes / No |

FAILS: labels are category headings, not named beliefs -- C-18 fail.
FAILS: no Behavioral? = Yes row -- C-18 partial.
FAILS: table absent before Phase 0 exits -- C-17 fail, C-18 fail.

### Table 0-B: Designated Inertia Challenger

| Field | Value |
|-------|-------|
| Name | [participant name] |
| Role | [role from .roles/] |
| Structural Rationale | [why their frame is least likely to share NORM assumptions -- structural reason required] |
| NORM Obligation | [NORM-XX, NORM-YY] |
| Phase 1 Requirement | Inertia Challenge? cell must not be None; CHAIN-3 must cite this row's NORM Obligation |

FAILS: Challenger row absent -- C-20 fail.
FAILS: Structural Rationale is generic ("external perspective") -- C-20 partial.
FAILS: NORM Obligation cell empty -- C-18 fail, C-20 fail.

### Table 0-C: Participant Roster

| Seq | Participant | Role | Primary Concern | Charter Status | NORM Obligation |
|-----|-------------|------|-----------------|----------------|-----------------|
| [DIC pos] | [Challenger] | [role] | [concern] | Standing | [NORM-XX, NORM-YY] |
| [others] | | | [concern] | [Standing / Candidate: function] | -- |

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: Challenger row absent or NORM Obligation empty -- C-20 fail.
FAILS: injection candidate not annotated in Charter Status -- C-12 fail.
FAILS: required function uncovered without annotation -- C-11 fail.

### Table 0-D: Agenda

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item] | [pass/fail condition] | [what must be present] |
| 2 | [item] | [pass/fail condition] | [what must be present] |
| 3 | [item] | [pass/fail condition] | [what must be present] |

FAILS: item generic, not type-specific -- C-07 fail.
FAILS: fewer than three rows -- C-06 partial.

### Table 0-E: Charter Constraints

| Constraint | Requirement from .roles/ | Honor Condition |
|------------|-------------------------------|-----------------|
| Quorum | [requirement] | [how Phase 1 satisfies] |
| Veto | [holder and conditions] | [how Phase 1 satisfies] |
| [additional] | [constraint] | [how] |

FAILS: fewer than two rows populated -- C-10 partial.

*Phase 0 complete. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 tables complete. Sequence declared.*

### Table 1-A: Discussion Grid

| Seq | Participant | Role | Contribution Summary | Evidence | Inertia Challenge? |
|-----|-------------|------|----------------------|----------|--------------------|
| [1] | [name] | [role] | [summary] | [type-specific evidence] | -- |
| [2] | [name] | [role] | [summary] | [evidence] | -- |
| [DIC pos] | [Challenger] | [role] | [summary] | [evidence] | [NORM-XX: outside-in basis] |

Inertia Challenge? rules:
- All non-Challenger rows: "--" (if not "--": verify role function is consistent)
- Challenger row: cite the NORM label from Table 0-B; state the outside-in basis;
  confirm the basis is non-circular (not derived from team's internal knowledge domain)

Prose contributions follow the grid in sequence order:

**[Seq] [Participant] ([Role]):** [Full contribution]

Role-voice constraints (each row in Table 1-A is independently auditable against this):
- PM: customer value, readiness, release timing. Not deployment topology.
- SRE/Ops: reliability, SLOs, operational risk. Not product vision.
- Architect: system design, trade-offs. Not business case.
- Security: threat model, compliance. Not delivery schedule.
- Engineering Lead: feasibility, tech debt. Not customer narrative.

FAILS: participant's Contribution Summary misaligns with role function (detectable per row) -- C-02 fail.
FAILS: Evidence cell empty for any row -- C-07 fail.
FAILS: Challenger Inertia Challenge? is "--" -- C-20 fail.
FAILS: Challenger's outside-in basis is circular (internal knowledge) -- C-17 fail.
FAILS: NORM label in Challenger cell not in Table 0-A -- C-18 fail.

### Table 1-B: Decision Tracker

| # | Agenda Item | Discussed? | Outcome | Deferred? | Escalation Path |
|---|-------------|------------|---------|-----------|-----------------|
| 1 | [item] | Yes | [approved / rejected / conditional] | No | -- |
| 2 | [item] | Yes | [outcome] | Yes | [escalation path] |

FAILS: Outcome cell empty for any row -- C-03 fail.
FAILS: Deferred = Yes but Escalation Path is "--" -- C-10 partial.

### Table 1-C: Dissent Register

| Participant | Role | In Tension with Majority? | Dissent Statement |
|-------------|------|--------------------------|-------------------|
| [name] | [role] | Yes / No | [objection in role voice, or --] |

FAILS: tension exists but row marked No without basis -- C-05 fail.
FAILS: Dissent Statement not in the dissenting participant's role voice -- C-05 partial.

*Phase 1 complete.*

---

## PRE-MORTEM CHAIN CHECK

**BLOCKING GATE: DO NOT PROCEED TO PHASE 2 UNTIL ALL THREE CHAINS CONFIRM.**

Any Phase 2 output produced before this gate is a C-19 fail, regardless of content.

### Table CHAIN-CHECK

| Chain | Requirement | Value | Status |
|-------|-------------|-------|--------|
| CHAIN-1 | Challenger identified (non-None) | [name from Table 0-B] | CONFIRMED / FAIL |
| CHAIN-2 | Outside-in basis stated and non-circular | [basis statement] | CONFIRMED / FAIL |
| CHAIN-3 | Risk draft connected to NORM label | [risk draft] → [NORM-XX from Table 0-A] | CONFIRMED / FAIL |

CHAIN-2 circular test: if the basis derives from the committee's own domain knowledge,
standard industry practice, or general reasoning -- it is circular. Restate from the
structural rationale in Table 0-B.

CHAIN-3 citation test: the NORM label must appear verbatim in Table 0-A. If not: C-18 fail.

FAILS: any row in Status = FAIL -- C-19 fail.
FAILS: Phase 2 pre-mortem risk contradicts CHAIN-3 risk draft -- C-19 fail.

*All chains confirmed. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: PRE-MORTEM CHAIN CHECK confirmed.*

### Table 2-A: Meeting Header

| Field | Value |
|-------|-------|
| Committee Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Simulated Date | [date] |
| Chair | [role] |
| Quorum Status | [met / not met -- N required, N present] |

FAILS: Type or Topic cells empty -- C-01 fail, C-06 partial.
FAILS: Quorum Status absent when charter defines quorum requirement -- C-10 partial.

### Pre-Mortem Risk Block

| Field | Value |
|-------|-------|
| Raised by | [Challenger name], [role] |
| NORM trace | [NORM-XX] -- [belief text from Table 0-A] |
| Outside-in basis | [from CHAIN-2] |
| Risk | [expanded from CHAIN-3 draft] |

FAILS: section absent -- C-09 fail.
FAILS: NORM trace cell empty or cites label not in Table 0-A -- C-18 fail.
FAILS: risk predictable by insiders without NORM context -- C-09 partial.

### Table 2-B: Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [decision text] | [approved / rejected / deferred / conditional-approval] | [or --] |

FAILS: table absent -- C-03 fail.
FAILS: Outcome column empty for any row -- C-03 fail.
FAILS: Table 1-B item discussed but absent here without explanation -- C-03 partial.

### Table 2-C: Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [action text] | [Name / Role] | [milestone or date] |

FAILS: Owner cell empty for any row -- C-04 fail.
FAILS: table absent when Table 1-B raised deferred items -- C-04 fail.
FAILS: Owner = TBD without escalation path -- C-04 partial.

### Table 2-D: Dissenting Opinions

| Participant | Role | Objection |
|-------------|------|-----------|
| [name] | [role] | [objection in role voice] |

If unanimous: *No dissent recorded -- unanimous.*

FAILS: Table 1-C tension entries absent here without reconciliation -- C-05 fail.
FAILS: table structurally absent (even for unanimous outcome) -- C-06 partial.

### Table 2-E: Charter Constraints Honored

| Constraint | Requirement | Applied | Notes |
|------------|-------------|---------|-------|
| Quorum | [from Table 0-E] | Yes / No | [count] |
| Veto | [from Table 0-E] | Exercised / Waived | [outcome] |
| [additional] | [from Table 0-E] | Honored | [boundary] |

FAILS: fewer than two rows confirmed from Table 0-E -- C-10 partial.
FAILS: entries not traceable to Table 0-E -- C-10 partial.

### AMEND (if invoked)

| Amendment Type | What Changes | Re-entry Point |
|----------------|--------------|----------------|
| Attendees | Add row to Table 0-C; insert contribution in Table 1-A | Phase 0.3 |
| Scope | Revise Table 0-D; revise affected Table 1-A rows | Phase 0.4 |
| Challenger | Re-execute Tables 0-A, 0-B, and CHAIN-CHECK | Phase 0 (Inertia Setup) |

FAILS: AMEND invoked but tables reflect pre-amendment state -- C-08 fail.
FAILS: Challenger-role amendment did not re-execute CHAIN-CHECK -- C-19 fail.

*Phase 2 complete. Minutes produced.*
```
