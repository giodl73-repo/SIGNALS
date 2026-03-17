Good. I have the R3 variate and a representative scorecard for context. R3's three axes were: phrasing register (pure imperative), table-first format, and lifecycle phases — but neither C-15 nor C-16 were criteria yet. R4 adds those two, so the new axes need to target them directly.

R3 gap on C-15: V-03's Phase 0 listed charter constraints as a *checklist step*, not as a gate that blocks Phase 1 entry. The upgrade is hard-gate enforcement.
R3 gap on C-16: V-02's tables covered roster/decisions/actions but the *discussion section remained prose*. The upgrade is a per-participant discussion grid where column absence = criterion violation.

---

```markdown
---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 4
rubric_version: 4
---

# corps-committee — Prompt Variations R4

## Variation Summary

| ID   | Axis                                                             | Hypothesis |
|------|------------------------------------------------------------------|------------|
| V-01 | Lifecycle — hard phase-gate preconditions                       | Making charter constraints (quorum, scope, escalation) into explicit GATE conditions that block Phase 1 entry — not checklist steps within Phase 0 — satisfies C-15: the test "can Phase 1 begin without charter constraints stated?" fails structurally, not by instruction. |
| V-02 | Output format — per-participant discussion grid                 | Replacing prose discussion with a per-participant grid (one row per participant, columns for Role / Contribution / Charter Drift / Dissent / Owner) satisfies C-16: a reviewer scanning column headers and cell presence can catch C-02, C-04, and C-05 violations without reading prose. |
| V-03 | Phrasing — imperative pre-skeleton with type fail conditions    | A BEFORE YOU START block that (a) appears before any skeleton or phase label, (b) states each committee type's primary obligation in imperative voice, and (c) names one natural-language fail condition per type that catches the most common output defect (e.g., "If there is no metric, you have not done a ROB") satisfies C-13 more reliably than R3 V-01, which embedded fail conditions inside step bodies rather than before the skeleton. |
| V-04 | Lifecycle gates + per-participant grid (C-15 + C-16 combined)  | Combining hard phase-gate preconditions (V-01) with a per-participant discussion grid (V-02) achieves C-15 PASS and C-16 PASS simultaneously without requiring either mechanism to carry the full compliance weight. |
| V-05 | Full synthesis + inertia framing                               | Imperative pre-skeleton (V-03) + phase gates (V-01) + per-participant grid (V-02) + an inertia hypothesis gate (what will the real committee rubber-stamp?) targets C-09 outside-in pass alongside C-13/C-15/C-16. |

---

## V-01 — Axis: Lifecycle (Hard Phase-Gate Preconditions)

**Axis:** Lifecycle emphasis
**Hypothesis:** Replacing Phase 0 checklist steps with hard gate conditions that explicitly block
Phase 1 entry satisfies C-15. The test criterion is: "Can Phase 1 begin without charter
constraints stated?" In V-01 the answer is structurally no — the gate output is required text
before the Phase 1 header is permitted. R3 V-03 had phases but charter constraints were Step 0.4
inside Phase 0; a model could produce a Phase 1 header after steps 0.1–0.3 and before 0.4.
V-01 closes this gap.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Produce formal meeting minutes. Read
participant charters from .craft/roles/. AMEND: add attendees, change scope.

---

## BEFORE YOU START

Identify your committee type and write this line before anything else:

> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic under review]

Type obligations:
- ROB: produce a readiness verdict backed by metric evidence
- SHIPROOM: produce a binary GO or NO-GO decision backed by a risk register
- ARCH-BOARD: produce an ADR with named trade-offs and a selected alternative

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL EVERY GATE BELOW APPEARS IN YOUR OUTPUT.

Each gate is a required output element, not a mental checklist. If a gate is missing from
your output when Phase 1 begins, Phase 1 is invalid.

**Gate 0-A | Committee type committed**
Write: > Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Participant charters loaded**
For each participant: read .craft/roles/. Output role title, primary decision scope, and any
veto or escalation rights. One line per participant.
If a required function has no charter role: [Injection required: [function] — pending Phase 1].
If injection is pending: mark attendee [Candidate: [function] — not yet confirmed].

FAILS: required function left uncovered without annotation — C-11 fail.
FAILS: injection pending but no [Candidate: ...] annotation in Phase 0 — C-12 fail.

**Gate 0-C | Quorum check**
State the quorum requirement from .craft/roles/ and whether it is met.
Write: > Quorum: [N required | N present | met / not met]

**Gate 0-D | Scope boundary**
State the meeting scope in one sentence. Any agenda item outside this boundary must be
flagged before Phase 1 begins.
Write: > Scope: [one sentence] | Out-of-scope flags: [items, or none]

**Gate 0-E | Escalation path**
Name the next body if this committee cannot reach a decision.
Write: > Escalation: [body name and trigger condition]

**Gate 0-F | Agenda locked**
List 3–5 agenda items appropriate to the committee type.
- ROB: readiness gates, metric review, blocking issues
- SHIPROOM: go/no-go criteria, risk register, release blockers
- ARCH-BOARD: decision context, named alternatives, ADR outcome

FAILS: fewer than three agenda items — C-06 partial.
FAILS: agenda items generic, not tied to committee type — C-07 fail.

*All six gate outputs must be present before the Phase 1 header.*

---

## PHASE 1 — SIMULATION

*Entry condition: Gates 0-A through 0-F all present in output.*

Simulate each participant in sequence. Each participant speaks from their charter scope only.

Role-voice discipline:
- PM: customer value, readiness, release timing. Does not lead deployment topology.
- SRE/Ops: reliability, SLOs, operational risk. Does not lead product vision.
- Architect: system design, trade-offs, constraints. Does not own the business case.
- Security: threat model, compliance gaps. Does not own the delivery schedule.
- Engineering Lead: implementation feasibility, technical debt. Does not own the customer narrative.

Committee-type depth (required in each contribution):
- ROB: participant references a specific metric or readiness indicator.
- SHIPROOM: participant names a risk or blocker explicitly.
- ARCH-BOARD: participant names a trade-off or architectural constraint.

One participant — the role best positioned for an outside-in view — raises the pre-mortem
risk before Phase 1 closes:
- Non-obvious: a competent internal reviewer would not automatically predict it.
- Outside-in: frame of reference external to the team.

Dissent: if any participant's charter position creates structural tension with the emerging
majority outcome, write a labeled Dissent entry. Do not smooth it over in prose.

FAILS: participant speaks outside charter scope without flagging — C-02 fail.
FAILS: contribution contains no type-specific evidence — C-07 fail.
FAILS: no pre-mortem risk raised before Phase 1 closes — C-09 fail.
FAILS: pre-mortem risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: role tension exists but no Dissent entry — C-05 fail.

---

## PHASE 2 — MINUTES

*Entry condition: All agenda items discussed, decisions and dissent recorded in Phase 1.*

Resolve all [Candidate: ...] annotations from Phase 0. For each:
- If charter coverage confirmed: record participant as Standing.
- If not confirmed: [Unrepresented — function not covered].

Produce formal minutes:

```
# [Type] Meeting Minutes — [Topic] — [Date]

## Attendees
[Role — Name | Charter status]

## Agenda
[Items as locked in Gate 0-F]

## Discussion
[Per-participant contributions, role-labeled, with type-specific evidence]

## Dissenting Opinions
[Labeled entries, or "None — unanimous"]

## Decisions
| Decision | Outcome | Conditions |
|----------|---------|------------|

## Action Items
| Action | Owner | Due |
|--------|-------|-----|

## Charter Constraints Honored
[At least two from Gates 0-C through 0-E: quorum, scope, escalation, veto]

## Next Steps
[Follow-up trigger, escalation path if deferred]
```

FAILS: Phase 1 simulation begins before any Gate 0 output is present — C-15 fail.
FAILS: charter constraints (quorum, scope, escalation) appear only in Phase 1 prose,
  not as Phase 0 gate outputs — C-10 partial, C-15 fail.
FAILS: action item without owner — C-04 fail.
FAILS: fewer than two charter constraints named in Charter Constraints Honored — C-10 partial.
FAILS: AMEND invoked but Phase 0 gates not re-executed from amended inputs — C-08 fail.
```

---

## V-02 — Axis: Output Format (Per-Participant Discussion Grid)

**Axis:** Output format
**Hypothesis:** Replacing the prose discussion section with a per-participant grid — one row
per participant, columns for Role / Contribution / Charter Drift? / Dissent / Action / Owner —
satisfies C-16. A reviewer scanning column headers and cell presence (without reading prose)
can catch C-02 violations (Charter Drift? = YES), C-04 violations (Owner empty when question
raised), and C-05 violations (Dissent blank rather than "None"). R3 V-02 had tables for
roster, decisions, and actions but kept discussion as prose blocks — violations required
close reading to detect.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Every enumerable output section uses a table.
Discussion output uses the Participant Grid format — violations produce visible structural
gaps, not subtle prose omissions. Read participant charters from .craft/roles/.
AMEND: add attendees, change scope.

---

## BEFORE YOU START

Identify your committee type and commit to its obligation:

| Type | Primary Obligation | Automatic Fail Condition |
|------|--------------------|--------------------------|
| ROB | Readiness verdict backed by metric evidence | No metric in output = ROB not done — C-01 fail |
| SHIPROOM | Binary GO/NO-GO decision backed by risk register | No GO/NO-GO decision line = shiproom not done — C-01 fail, C-03 fail |
| ARCH-BOARD | ADR with named trade-offs and selected alternative | Alternatives without a winner = arch-board not done — C-01 fail |

Write one line before proceeding:
> **Type:** [ROB / SHIPROOM / ARCH-BOARD] | **Topic:** [topic under review]

---

## Phase 0 — Setup

### Meeting Header

| Field | Value |
|-------|-------|
| Committee Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Simulated Date | [date] |
| Chair | [role name] |
| Quorum | [N required | N present | met / not met] |
| Escalation Path | [body name and trigger] |
| Scope | [one sentence] |

FAILS: Quorum row empty when charter defines a quorum requirement — C-10 partial.
FAILS: Escalation Path row empty — C-10 partial.

### Participant Roster

| # | Participant | Role | Primary Concern | Charter Status |
|---|-------------|------|-----------------|----------------|
| 1 | [name] | [role from .craft/roles/] | [one concern, one sentence] | [Standing] |
| 2 | [name] | [role] | [concern] | [Candidate: [function] — pending] |
| … |  |  |  |  |

Rules:
- Load .craft/roles/ for each participant.
- Primary Concern must align with role function only.
- Any required function without a charter role: Charter Status = [Candidate: [function] — pending Phase 1 confirmation].

FAILS: participant's Primary Concern mismatches their role function — C-02 fail (visible in row).
FAILS: injection pending but Charter Status column left blank — C-12 fail.
FAILS: required function left uncovered without annotation — C-11 fail.

### Agenda

| # | Item | Type-Specific Gate | Evidence Required |
|---|------|--------------------|-------------------|
| 1 | [item] | [pass/fail condition] | [what must appear] |
| 2 | [item] | [pass/fail condition] | [what must appear] |
| 3 | [item] | [pass/fail condition] | [what must appear] |

FAILS: agenda items generic — applicable to any meeting type — C-07 fail.
FAILS: fewer than three items — C-06 partial.

---

## Phase 1 — Simulation

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.
One row per participant. Every cell must be filled. An empty cell is a visible compliance
gap — it signals the criterion mapped to that column is not met for that participant.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Dissent | Action Raised | Owner |
|-------------|------|-------------------------------|----------------|---------|---------------|-------|

Column rules:
- **Contribution**: Must reflect charter scope and include type-specific evidence.
  - ROB: cite a specific metric or readiness indicator.
  - SHIPROOM: name a risk or blocker explicitly.
  - ARCH-BOARD: name a trade-off or architectural constraint.
  Do not leave Contribution as prose that could belong to any committee type.
- **Charter Drift?**: If participant spoke outside their charter scope, write YES — [topic].
  Otherwise: None. Do not leave blank.
- **Dissent**: If the participant's charter position creates tension with the majority outcome,
  state it here. Otherwise: None. Do not leave blank. A blank Dissent cell is a C-05
  compliance gap visible without reading prose.
- **Action Raised**: If the participant raised an open question or committed to follow-up,
  state the action. Otherwise: None.
- **Owner**: If an action was raised, name the owner here. An empty Owner cell when Action
  Raised is non-None is a C-04 fail visible as a missing cell.

Pre-mortem risk entry — add one row after all participants have spoken:

| PRE-MORTEM RISK | [Participant] ([Role]) | [Non-obvious, outside-in risk — must represent a frame of reference a competent internal reviewer would not automatically predict] | — | — | — | — |

FAILS: Contribution column contains content outside participant charter scope — C-02 fail, visible in row.
FAILS: Charter Drift? column left blank rather than "None" — C-16 partial.
FAILS: Dissent column left blank rather than "None" — C-05 ambiguous, C-16 partial.
FAILS: Owner column empty when Action Raised is non-None — C-04 fail, C-16 partial.
FAILS: no pre-mortem risk row — C-09 fail.
FAILS: pre-mortem risk predictable by insiders — C-09 outside-in gate not cleared.

---

## Phase 2 — Decisions and Close

Resolve all [Candidate: ...] participants. For each:
- Confirmed: update Charter Status to Standing.
- Not confirmed: [Unrepresented — function not covered].

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [decision text] | [approved / rejected / deferred / conditional-approval] | [conditions, or —] |

FAILS: Outcome column empty for any row — C-03 fail.
FAILS: Decisions table absent — C-03 fail.
FAILS: agenda item discussed in Phase 1 but absent from this table without explanation — C-03 partial.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [action] | [Name / Role] | [milestone or date] |

FAILS: Owner column empty for any row — C-04 fail.
FAILS: table absent when Phase 1 Participant Grid raised open actions — C-04 fail.

### Charter Constraints Honored

| Constraint | Requirement | Applied? | Notes |
|------------|-------------|----------|-------|
| Quorum | [from .craft/roles/] | Yes / No | [count] |
| Escalation | [from .craft/roles/] | Applicable / N/A | [path] |
| [Veto / Scope] | [from .craft/roles/] | Honored | [boundary or outcome] |

FAILS: fewer than two rows populated with charter-sourced content — C-10 partial.

### AMEND (if invoked)

- AMEND attendees: add row to Participant Roster; insert their row in Participant Grid at the
  correct position.
- AMEND scope: update Agenda table; revise affected Contribution cells.

FAILS: AMEND invoked but Participant Grid reflects pre-amendment roster — C-08 fail.
```

---

## V-03 — Axis: Phrasing Register (Imperative Pre-Skeleton with Type Fail Conditions)

**Axis:** Phrasing register
**Hypothesis:** A BEFORE YOU START block that (a) appears before any phase header or skeleton
section, (b) states each type's primary obligation in direct imperative voice, and (c) names
one explicit natural-language fail condition per type that catches the most common output defect
satisfies C-13 more reliably than R3 V-01. R3 V-01's fail conditions were embedded inside step
bodies (Step 3, Step 4) — they were fill rules that happened to mention failure, not a
pre-skeleton block architecturally prior to all filling. V-03 makes the block's placement
structural: it must appear in output before any section header.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Produce meeting minutes. Read participant
charters from .craft/roles/. AMEND: add attendees, change scope.

---

## BEFORE YOU START

Work through this block completely. Do not write any phase header, section header, or
meeting content until this block appears in your output.

**Step 1: Name your committee type.**

Write this line:
> Running /corps-committee as: [ROB / SHIPROOM / ARCH-BOARD] for topic: [topic]

**Step 2: State your type's obligation and fail condition.**

Copy and complete the entry for your committee type. Do not paraphrase.

> **ROB**
> Obligation: I must produce a readiness verdict backed by metric evidence.
> Fail condition: If there is no metric in my output, I have not done a ROB. I have done a
> status update. I must add the metric before continuing.

> **SHIPROOM**
> Obligation: I must produce a binary GO or NO-GO decision backed by a risk register.
> Fail condition: If my output contains no GO or NO-GO decision line, I have not done a
> shiproom. I have done a chat. I must add the decision line before continuing.

> **ARCH-BOARD**
> Obligation: I must produce an Architecture Decision Record naming at least two alternatives
> with trade-offs and selecting one.
> Fail condition: If I listed alternatives without selecting one, I have not done an arch-board.
> I have recorded preferences. I must state the winner before continuing.

**Step 3: Identify every participant.**

Read .craft/roles/. For each participant, name the single concern they own in this meeting.

If a required function has no charter role: state [Injection required: [function]].
If injection is pending confirmation: annotate [Candidate: [function] — pending].

FAILS: participant listed without charter verification — C-02 risk, C-11 risk.
FAILS: injection candidate not annotated before any phase begins — C-12 fail.

**Step 4: Commit the charter constraints.**

Name at least two constraints from .craft/roles/ that must be honored:
- Quorum: [requirement and current headcount]
- Escalation: [next body if no decision is reached]
- Scope: [one sentence — what is out of scope]
- Veto: [role with veto rights and conditions, if any]

FAILS: fewer than two constraints committed in this block — C-10 partial.

**Step 5: Lock the agenda.**

List 3–5 agenda items. Each must be type-specific. Generic items (applicable to any meeting
type without modification) are not valid.

FAILS: agenda items generic — C-07 fail.

*This block is now complete. You may write the Phase 0 header.*

---

## Phase 0 — Pre-Meeting Record

Output the committed state from BEFORE YOU START:
- Type and obligation (as written in Step 2)
- Attendees with roles and charter concerns
- Charter constraints (from Step 4)
- Agenda items (from Step 5)

---

## Phase 1 — Simulation

Run the meeting. Simulate each participant in sequence. Each participant speaks from their
charter scope. Do not let a PM lead on deployment topology. Do not let an SRE lead on
product vision. If a participant speaks outside their charter, name the drift explicitly.

Include type-specific evidence in every contribution:
- ROB: metric or readiness data cited by name.
- SHIPROOM: risk or blocker named explicitly.
- ARCH-BOARD: trade-off or architectural constraint named.

A generic contribution that could belong to any committee type means you have failed Step 2.
Return to BEFORE YOU START, re-read your type's fail condition, and revise.

Dissent: if any participant's charter creates tension with the majority outcome, write a
labeled Dissent entry. Smoothing dissent over in prose defeats the simulation.

One participant — the role most positioned for an outside-in view — raises the pre-mortem
risk before Phase 1 closes. This risk must be non-obvious: a competent internal reviewer
would not automatically predict it.

FAILS: BEFORE YOU START block absent from output before this section — C-13 fail.
FAILS: type's fail condition present in BEFORE YOU START but output violates it — C-13 partial, C-01 fail / C-07 fail depending on type.
FAILS: participant speaks outside charter scope without explicit drift flag — C-02 fail.
FAILS: contribution contains no type-specific evidence — C-07 fail.
FAILS: no pre-mortem risk raised — C-09 fail.
FAILS: pre-mortem risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: role tension present but no Dissent entry — C-05 fail.

---

## Phase 2 — Minutes

Resolve all [Candidate: ...] participants. Confirm charter coverage or record [Unrepresented].

Produce formal minutes:

```
# [Type] Meeting Minutes — [Topic] — [Date]

## Attendees
[Role — Name]

## Agenda
[Items from BEFORE YOU START Step 5]

## Discussion
[Per-participant contributions, role-labeled, with type-specific evidence]

## Dissenting Opinions
[Explicit labeled entries, or "None — unanimous"]

## Decisions
[Outcomes: approved / rejected / deferred / conditional-approval, one per decision]

## Action Items
| Action | Owner | Due |
|--------|-------|-----|

## Charter Constraints Honored
[At least two, citing the constraints committed in BEFORE YOU START Step 4]

## Next Steps
```

FAILS: action item without owner — C-04 fail.
FAILS: fewer than two charter constraints cited in Charter Constraints Honored — C-10 partial.
FAILS: AMEND invoked but output not regenerated from amended BEFORE YOU START — C-08 fail.
```

---

## V-04 — Axis: Lifecycle Gates + Per-Participant Grid (C-15 + C-16 combined)

**Axis:** Lifecycle emphasis + output format
**Hypothesis:** Combining hard phase-gate preconditions (V-01) with a per-participant discussion
grid (V-02) achieves C-15 PASS and C-16 PASS simultaneously. Neither mechanism needs to carry
full compliance weight: gates close C-15 by making charter constraints unavoidable Phase 0
outputs; the grid closes C-16 by making criterion violations appear as missing cells. The two
mechanisms are complementary — gates protect setup correctness, the grid protects simulation
output correctness.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .craft/roles/.
AMEND: add attendees, change scope.

Output structure: Phase 0 uses gates. Phase 1 uses the Participant Grid. Phase 2 uses tables.

---

## BEFORE YOU START

Identify your committee type. Write this line:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic under review]

Type obligations and fail conditions:
- ROB: readiness verdict + metric evidence. No metric = ROB not done.
- SHIPROOM: GO/NO-GO decision + risk register. No GO/NO-GO line = shiproom not done.
- ARCH-BOARD: ADR with alternatives + winner selected. No selection = arch-board not done.

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

Charter constraints are Phase 0 exit conditions — they are required before simulation begins,
not post-hoc checks that appear inside simulation output.

**Gate 0-A | Type + obligation committed**
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Charters loaded**
For each participant: role title, primary decision scope, veto/escalation rights from .craft/roles/.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation]

FAILS: injection pending but [Candidate: ...] annotation absent from Phase 0 — C-12 fail.
FAILS: required function uncovered without annotation — C-11 fail.

**Gate 0-C | Quorum**
> Quorum: [N required | N present | met / not met]

**Gate 0-D | Scope**
> Scope: [one sentence] | Out-of-scope flags: [items, or none]

**Gate 0-E | Escalation**
> Escalation: [next body] — triggered when: [condition]

**Gate 0-F | Agenda**
| # | Item | Type-Specific Gate | Evidence Required |
|---|------|--------------------|-------------------|
| 1 | [item] | [condition] | [what must appear] |
| 2 | [item] | [condition] | [what must appear] |
| 3 | [item] | [condition] | [what must appear] |

FAILS: fewer than three agenda items — C-06 partial.
FAILS: items generic, not type-specific — C-07 fail.

*Gates 0-A through 0-F must all appear before the Phase 1 header is written.*

---

## PHASE 1 — SIMULATION

*Entry condition: All Phase 0 gates present in output.*

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.
One row per participant. Every cell filled. Empty cell = visible criterion gap.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Dissent | Action | Owner |
|-------------|------|-------------------------------|----------------|---------|--------|-------|

Column enforcement rules:
- **Contribution**: Charter-scoped only. Must include type-specific evidence:
  ROB: metric or readiness indicator. SHIPROOM: risk or blocker. ARCH-BOARD: trade-off or constraint.
  A contribution that could belong to any committee type fails C-07.
- **Charter Drift?**: YES — [topic drift] if participant spoke outside charter scope.
  Otherwise: None. Never leave blank — a blank is a C-02 audit gap, C-16 partial.
- **Dissent**: Explicit tension statement if participant's charter position conflicts with
  majority outcome. Otherwise: None. Never blank — blank Dissent is a C-05 gap, C-16 partial.
- **Action**: Open question or follow-up committed by participant. Otherwise: None.
- **Owner**: If Action is non-None, name the owner. Empty Owner when Action is non-None
  = C-04 fail, visible as missing cell without reading prose.

After all participant rows, add one row for the pre-mortem risk:

| PRE-MORTEM RISK | [Participant] ([Role]) | [Non-obvious, outside-in risk. A competent internal reviewer would not predict this.] | — | — | — | — |

FAILS: Phase 1 header written before any Gate 0 output appears — C-15 fail.
FAILS: charter constraints (quorum, scope, escalation) appear only in Phase 1 grid prose,
  not as Gate 0 outputs — C-10 partial, C-15 fail.
FAILS: Contribution outside participant's charter scope — C-02 fail, visible in Charter Drift? column.
FAILS: Charter Drift? column blank rather than None — C-16 partial.
FAILS: Dissent column blank rather than None — C-05 ambiguous, C-16 partial.
FAILS: Owner empty when Action non-None — C-04 fail, visible as missing cell, C-16 partial.
FAILS: no pre-mortem risk row — C-09 fail.
FAILS: pre-mortem risk predictable by insiders — C-09 outside-in gate not cleared.

---

## PHASE 2 — CLOSE

Resolve all [Candidate: ...] annotations from Gate 0-B. Confirm coverage or record [Unrepresented].

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [decision text] | [approved / rejected / deferred / conditional-approval] | [or —] |

FAILS: Outcome empty for any row — C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [action] | [Name / Role] | [milestone or date] |

FAILS: Owner column empty for any row — C-04 fail.
FAILS: table absent when Phase 1 grid raised actions — C-04 fail.

### Charter Constraints Honored

| Constraint | Gate Source | Applied? | Notes |
|------------|-------------|----------|-------|
| Quorum | Gate 0-C | Yes / No | [count] |
| Scope | Gate 0-D | Honored | [boundary] |
| Escalation | Gate 0-E | Applicable / N/A | [path, if deferred] |

FAILS: fewer than two rows confirmed from Phase 0 gates — C-10 partial.

### AMEND (if invoked)

AMEND attendees: re-enter Phase 0 Gate 0-B with new participant; add their row to Phase 1 grid.
AMEND scope: update Gate 0-F agenda; revise affected Contribution cells.

FAILS: AMEND invoked but Phase 0 gates and Phase 1 grid not re-executed from amended inputs — C-08 fail.
```

---

## V-05 — Axis: Full Synthesis + Inertia Framing

**Axis:** Imperative pre-skeleton + lifecycle gates + per-participant grid + inertia framing
**Hypothesis:** Adding an inertia hypothesis gate (what will the real committee rubber-stamp
that it should be forced to defend?) surfaces C-09 outside-in risk through a structural mechanism
rather than an instruction. The real committee's status-quo assumption becomes the simulation's
explicit pressure point — at least one participant must challenge it, and the pre-mortem risk in
Phase 2 must connect back to it. This provides a traceable mechanism for C-09 that prior
variations left to model discretion.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .craft/roles/.
AMEND: add attendees, change scope.

---

## BEFORE YOU START

Work through this block completely. Do not write any phase header or meeting content until
this block appears in your output.

**A. Commit your committee type and its obligation + fail condition.**

> I am running /corps-committee as: [ROB / SHIPROOM / ARCH-BOARD] for topic: [topic]

Copy and complete the entry for your type:

**ROB**
Obligation: I must produce a readiness verdict backed by metric evidence.
Fail condition: If there is no metric in my output, I have not done a ROB. I must add the
metric before writing any further output.

**SHIPROOM**
Obligation: I must produce a binary GO or NO-GO decision backed by a risk register.
Fail condition: If my output contains no GO/NO-GO decision line, I have not done a shiproom.
I must add the decision line before writing any further output.

**ARCH-BOARD**
Obligation: I must produce an ADR naming at least two alternatives with trade-offs and
selecting one.
Fail condition: If I listed alternatives without selecting one, I have not done an arch-board.
I must name the winner before writing any further output.

**B. State the inertia hypothesis.**

Before simulating, answer: What is this committee's most likely rubber-stamp outcome? What
assumption is the real committee carrying in that a rigorous reviewer would force them to defend?

Write:
> Inertia hypothesis: The real committee is likely to [approve X / defer Y / accept Z] without
> challenge. The assumption being carried: [state it in one sentence].

This hypothesis is not a prediction — it is the simulation's pressure point. At least one
participant in Phase 1 must challenge it. The pre-mortem risk in Phase 2 must connect to it.

**C. Name every participant and their charter function.**

Read .craft/roles/. For each participant: role title, primary decision scope, escalation rights.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation].

FAILS: BEFORE YOU START block absent before Phase 0 header — C-13 fail.
FAILS: injection candidate not annotated before Phase 0 begins — C-12 fail.
FAILS: required function uncovered without annotation — C-11 fail.

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

**Gate 0-A | Type + obligation**
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Inertia hypothesis committed**
> Inertia: [rubber-stamp outcome] | Assumption: [one sentence]

**Gate 0-C | Quorum**
> Quorum: [N required | N present | met / not met]

**Gate 0-D | Scope**
> Scope: [one sentence] | Out-of-scope flags: [items, or none]

**Gate 0-E | Escalation**
> Escalation: [next body] — triggered when: [condition]

**Gate 0-F | Agenda**
| # | Item | Type-Specific Gate | Evidence Required |
|---|------|--------------------|-------------------|
| 1 | [item] | [condition] | [what must appear] |
| 2 | [item] | [condition] | [what must appear] |
| 3 | [item] | [condition] | [what must appear] |

FAILS: fewer than three type-specific agenda items — C-06 partial, C-07 fail.
FAILS: inertia hypothesis not committed before Phase 1 begins — C-09 miss (no target to challenge).

*Gates 0-A through 0-F must all appear before the Phase 1 header.*

---

## PHASE 1 — SIMULATION

*Entry condition: All Phase 0 gates present, including inertia hypothesis (Gate 0-B).*

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Inertia Challenge? | Dissent | Action | Owner |
|-------------|------|-------------------------------|----------------|-------------------|---------|--------|-------|

Column enforcement rules:
- **Contribution**: Charter-scoped, type-specific evidence required.
  ROB: metric or readiness indicator. SHIPROOM: risk or blocker. ARCH-BOARD: trade-off.
- **Charter Drift?**: YES — [scope] or None. Never blank.
- **Inertia Challenge?**: If this participant challenges the inertia hypothesis from Gate 0-B,
  summarize the challenge in one sentence. Otherwise: None.
  At least one participant row must have a non-None Inertia Challenge entry. A grid with all
  None in this column means the inertia was never challenged — the simulation confirmed the
  rubber stamp rather than stress-testing it.
- **Dissent**: Explicit tension statement or None. Never blank.
- **Action**: Open question or follow-up, or None.
- **Owner**: Name the owner if Action is non-None. Empty Owner when Action non-None = C-04 fail.

FAILS: Phase 1 header written before all Phase 0 gates present — C-15 fail.
FAILS: charter constraints appear only in Phase 1 prose, not as Phase 0 gates — C-10 partial, C-15 fail.
FAILS: Inertia Challenge? column all None — C-09 partial (inertia not challenged).
FAILS: Charter Drift? or Dissent column left blank (not None) — C-16 partial.
FAILS: Owner empty when Action non-None — C-04 fail, C-16 partial.
FAILS: Contribution outside charter scope — C-02 fail.
FAILS: Contribution contains no type-specific evidence — C-07 fail.

---

## PHASE 2 — CLOSE

Resolve all [Candidate: ...] participants. Confirm coverage or record [Unrepresented].

### Pre-Mortem Risk

Name the one risk the real committee is most likely to miss.

Requirements:
1. Raised by a specific participant in Phase 1 (traceable to a grid row with non-None Inertia Challenge?).
2. Not predictable by a competent internal reviewer (outside-in frame required).
3. Connects to the inertia hypothesis from Gate 0-B — the risk is latent in the rubber-stamp outcome.

> Pre-mortem risk: [risk statement]
> Raised by: [Participant] ([Role]) — Phase 1 row [#]
> Connected to inertia: [one sentence linking risk to Gate 0-B assumption]

FAILS: pre-mortem risk not traceable to a Phase 1 grid row — C-09 fail.
FAILS: risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: risk not connected to inertia hypothesis — C-09 partial (outside-in, but not structurally earned).

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [decision text] | [approved / rejected / deferred / conditional-approval] | [or —] |

FAILS: Outcome column empty for any row — C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [action] | [Name / Role] | [milestone or date] |

FAILS: Owner column empty for any row — C-04 fail.

### Charter Constraints Honored

| Constraint | Gate Source | Applied? | Notes |
|------------|-------------|----------|-------|
| Quorum | Gate 0-C | Yes / No | [count] |
| Scope | Gate 0-D | Honored | [boundary] |
| Escalation | Gate 0-E | Applicable / N/A | [path] |

FAILS: fewer than two rows confirmed from Phase 0 gates — C-10 partial.

### AMEND (if invoked)

AMEND attendees: re-enter BEFORE YOU START Part C; re-execute Phase 0 gates; add row to Phase 1 grid.
AMEND scope: update Gate 0-F; revise affected Contribution cells and re-evaluate inertia hypothesis.

FAILS: AMEND invoked but BEFORE YOU START not re-executed from amended inputs — C-08 fail.
```

---

## Design Notes for Scorer

### New mechanisms targeting C-15 (V-01, V-04, V-05)

The shared pattern across V-01/V-04/V-05:

> YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

This differs from R3 V-03's Phase 0 in a precise way: R3 listed charter constraints as
**step 0.4 inside Phase 0** — a checklist item the model could complete in any order and
then advance. V-01/V-04/V-05 make charter constraints **named gate outputs** with an explicit
prohibition on Phase 1 beginning before they appear. The test: "Can Phase 1 begin without
charter constraints stated?" Answer is structurally no — the prohibition is in the prompt
surface.

### New mechanism targeting C-16 (V-02, V-04, V-05)

The shared pattern: per-participant discussion grid with columns explicitly mapped to
rubric criteria:

| Column | Criterion enforced |
|--------|--------------------|
| Charter Drift? | C-02 — role voice discipline |
| Owner | C-04 — action items with owners |
| Dissent | C-05 — dissenting opinion |

Each column rule includes an explicit note that a blank cell (rather than "None") is itself
a compliance gap. This makes the distinction: a cell reading "None" means the criterion was
evaluated and found vacuously satisfied; a blank cell means the criterion was not evaluated.
The former is auditable; the latter is a C-16 partial.

### Inertia framing as C-09 structural mechanism (V-05)

R3 found that asking the final participant to raise a pre-mortem risk is instruction-dependent —
the model can satisfy it with an obvious concern restated as if non-obvious. V-05 adds a
structural anchor: Gate 0-B commits the inertia hypothesis before simulation begins. The
pre-mortem risk in Phase 2 must connect back to that hypothesis. This creates a traceable
chain: inertia stated → challenged by a specific grid row → pre-mortem risk connects to
the same assumption. A generic risk cannot satisfy this without the chain being auditable.
```
