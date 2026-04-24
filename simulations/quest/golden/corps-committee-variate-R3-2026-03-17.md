---
skill: quest-variate
skill_target: corps-committee
date: 2026-03-17
round: 3
rubric_version: 3
---

# corps-committee -- Prompt Variations R3

## Variation Summary

| ID   | Axis                                                             | Hypothesis |
|------|------------------------------------------------------------------|------------|
| V-01 | Phrasing register (pure imperative)                             | Concentrated imperative voice throughout — not only in the BEFORE YOU START block — raises C-02 (role-voice discipline) by eliminating hedged participant contributions; "You must" framing provides no syntactic gap for the model to slip a PM into deployment topology. |
| V-02 | Output format (table-first)                                     | Mandating a table for every enumerable section (roster, decisions, actions, risks, charter) produces a self-auditing artifact where column violations are visually obvious; C-06 format compliance and C-04 action-owner coupling both benefit from structural constraints imposed by table grammar. |
| V-03 | Lifecycle emphasis (explicit phase boundaries)                  | Dividing execution into Phase 0 (setup), Phase 1 (simulation), Phase 2 (minutes) with hard entry/exit conditions prevents the most common failure mode — collapsed setup-and-simulation prose — and forces type-specific depth to be established before voices are simulated, raising C-07. |
| V-04 | Phrasing register + criterion annotation maximized              | Combining pure imperative voice with criterion ID annotations on every fill-rule FAIL (not just the minimum three) creates a fully traceable output; the model cannot satisfy any FAILS condition without simultaneously knowing which rubric criterion it is protecting, maximizing C-14 while preserving C-13 dominance. |
| V-05 | Table format + role sequence ordering + lifecycle phases        | Combining table-first output with an ordered role execution sequence (declared per committee type in the BEFORE YOU START table) and Phase 0/1/2 structure; role sequence makes C-02 violations visible by position, table grammar enforces C-04/C-06, and phases enforce C-07 type-specific depth before fill begins. |

---

## V-01 -- Phrasing Register (Pure Imperative)

**Axis:** Phrasing register
**Hypothesis:** Concentrated imperative framing throughout — "Do this. Never do that." — produces higher C-02 compliance (role-voice discipline) and fewer hedged decision entries. The BEFORE YOU START block is compact and punchy; all steps use command syntax rather than descriptive guidance.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Do not explain or summarize. Produce an
artifact that functions as a real record.

---

## BEFORE YOU START

Identify your committee type. State its obligation. Do not write a single line of minutes
until you have committed to one of these three:

**ROB (Product Review / Service Review)**
Obligation: Produce a readiness verdict backed by metric evidence.
Fail condition: If there is no metric in your output, you have not done a ROB. Stop.
Restart from this block. (C-01 fail)

**SHIPROOM (Go / No-Go)**
Obligation: Produce a binary GO or NO-GO decision backed by a risk register.
Fail condition: If your minutes contain no GO/NO-GO decision line, you produced a discussion
summary, not a shiproom record. Add the decision line before continuing. (C-01 fail, C-03 fail)

**ARCH-BOARD (Architecture Decision Review)**
Obligation: Produce an ADR with named trade-offs and a selected alternative.
Fail condition: If you list pros and cons without selecting a winner, you have not done an
arch-board. State the decision. (C-01 fail)

Write this line before proceeding:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic under review]

---

## STEP 1 -- ROSTER

Load .roles/ for this committee type. List every participant. For each participant,
name the single concern they own in this meeting. Assign no participant two concerns.

If a required function has no charter role, mark it:
  [Injection required: [function]]

If any injection is pending, annotate it in the roster before Phase 1 begins:
  [Candidate: [role function] -- pending confirmation]

FAILS: participant listed without a stated concern -- C-02 fail, C-06 partial.
FAILS: injection-required function present but not marked -- C-11 fail.
FAILS: injection pending but no candidate annotation in roster -- C-12 fail.

---

## STEP 2 -- AGENDA

State 3-5 agenda items. Every item must be type-specific. Do not write generic items.

ROB items: readiness gates, metric thresholds, blocking issues.
SHIPROOM items: go/no-go criteria, risk register items, named release blockers.
ARCH-BOARD items: named alternatives under consideration, decision criteria, ADR outcome.

FAILS: item applicable to any committee type without modification -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

---

## STEP 3 -- DISCUSSION

Simulate each participant in sequence. Each participant speaks exactly once. Each participant
speaks from their role function and no other.

Enforce these role-voice constraints hard:
- PM: speaks to customer value, readiness, and release timing. Never leads on deployment
  topology or system design trade-offs.
- SRE / Ops: speaks to reliability, SLOs, and operational risk. Never leads the product vision.
- Architect: speaks to system design constraints and trade-offs. Never owns the business case.
- Security: speaks to threat model and compliance gaps. Never owns the delivery schedule.
- Engineering Lead: speaks to implementation feasibility and technical debt. Never owns the
  customer narrative.

Include type-specific evidence in each contribution:
- ROB: participant references specific metric or readiness data.
- SHIPROOM: participant names a risk or blocker explicitly.
- ARCH-BOARD: participant names a trade-off or architectural constraint.

The final participant to speak raises the pre-mortem risk. This risk must be:
- Non-obvious -- a competent internal reviewer would not automatically predict it.
- Outside-in -- representing a frame of reference external to the team.

FAILS: any participant's primary contribution misaligns with their function -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.
FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: pre-mortem risk predictable by insiders -- C-09 outside-in gate not cleared.

---

## STEP 4 -- DECISIONS

Record every decision. State the outcome for each. Do not omit any agenda item that reached
a conclusion.

**Decisions**
- [decision text] -- [approved / rejected / deferred / conditional-approval]

FAILS: outcome absent for any decision -- C-03 fail.
FAILS: Decisions section absent entirely -- C-03 fail.
FAILS: agenda item discussed but unresolved with no explanation -- C-03 partial.

---

## STEP 5 -- ACTION ITEMS

Record every action. Name every owner. One line per action.

**Action Items**
- [action] -- Owner: [Name / Role]

FAILS: action item without an owner -- C-04 fail.
FAILS: no action items despite open questions raised in discussion -- C-04 fail.
FAILS: owner listed as "TBD" without an escalation path -- C-04 partial.

---

## STEP 6 -- DISSENT

Record dissent wherever role-based tension exists with the majority outcome. Do not smooth
it over.

**Dissenting Opinions**
- [Participant] ([Role]): [specific objection stated in role voice]

If all participants agreed, write: *No dissent recorded -- unanimous.*

FAILS: role-based tension exists but dissent section omitted -- C-05 fail.
FAILS: dissent present but not stated in the dissenting participant's role voice -- C-05 partial.
FAILS: dissent section absent entirely -- C-06 partial.

---

## STEP 7 -- CHARTER FIDELITY

Name at least two charter constraints from .roles/ that were honored in this meeting.
State each constraint explicitly:
- Quorum: [met / not met] -- [count required vs present]
- Veto: [exercised / waived] -- [role holding veto]
- Escalation: [named escalation path, if any decision was deferred]
- Scope: [boundary honored -- state what is out of scope]

FAILS: fewer than two charter constraints named -- C-10 partial.
FAILS: constraints named but not tied to charter language or role definition -- C-10 partial.

---

## STEP 8 -- AMEND (if invoked)

If the user specified AMEND, apply it before generating output -- not after.

AMEND attendees: add the named participant to the roster; include their contribution in
  the discussion at the appropriate position.
AMEND scope: revise the agenda items; revise affected discussion contributions.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.
FAILS: amendment applied after output generation rather than integrated from the start -- C-08 partial.
```

---

## V-02 -- Output Format (Table-First)

**Axis:** Output format
**Hypothesis:** Mandating tables for every enumerable output section forces structural compliance;
column schema violations are visually obvious, making C-04 (action-owner coupling) and C-06
(formal structure) easier to audit. Tables also make C-02 (role-voice discipline) checkable
per row rather than buried in prose.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Produce mock meeting minutes. Every section
that has multiple entries uses a table. Minimize prose. Maximize structure.

---

## BEFORE YOU START

Before writing any minutes, identify your committee type and commit to its obligation:

| Type | Primary Obligation | Automatic Fail Condition |
|------|--------------------|--------------------------|
| ROB | Readiness verdict backed by metric evidence | No metric present in output = ROB not done -- C-01 fail |
| SHIPROOM | Binary GO/NO-GO decision backed by risk register | No GO/NO-GO line in output = shiproom not done -- C-01 fail, C-03 fail |
| ARCH-BOARD | ADR with named trade-offs and selected alternative | Trade-off discussion without a decision = arch-board not done -- C-01 fail |

Write one line before proceeding:
> **Type:** [ROB / SHIPROOM / ARCH-BOARD] | **Topic:** [topic under review]

---

## SECTION 1 -- MEETING HEADER

| Field | Value |
|-------|-------|
| Committee Type | [ROB / Shiproom / Arch-Board] |
| Topic | [topic] |
| Simulated Date | [date] |
| Chair | [role name] |
| Quorum Status | [met / not met -- N required, N present] |

FAILS: header absent or Type field empty -- C-01 fail, C-06 partial.
FAILS: Quorum Status not stated when charter defines a quorum requirement -- C-10 partial.

---

## SECTION 2 -- PARTICIPANT ROSTER

| Sequence | Participant | Role | Primary Concern This Meeting | Charter Status |
|----------|-------------|------|------------------------------|----------------|
| 1 | [name] | [role from .roles/] | [their one concern, one sentence] | [Standing / Candidate: function] |
| 2 | [name] | [role] | [concern] | [Standing / Candidate: function] |
| ... | | | | |

Rules:
- Load .roles/ for this committee type.
- Every participant owns one concern that aligns with their role function only.
- If a required function has no charter role: set Charter Status to
  [Candidate: [function] -- pending Phase 1 confirmation].

FAILS: participant's stated concern mismatches their role function -- C-02 fail.
FAILS: injection pending but Charter Status column not used -- C-12 fail.
FAILS: required function left uncovered without annotation -- C-11 fail.

---

## SECTION 3 -- AGENDA

| # | Agenda Item | Type-Specific Gate | Evidence Required |
|---|-------------|-------------------|-------------------|
| 1 | [item] | [pass/fail condition] | [what must be present] |
| 2 | [item] | [pass/fail condition] | [what must be present] |
| 3 | [item] | [pass/fail condition] | [what must be present] |

Type-specific agenda requirements:
- ROB: include readiness gates and metric review items.
- SHIPROOM: include go/no-go criteria and risk register items.
- ARCH-BOARD: include trade-off review and ADR outcome item.

FAILS: agenda items generic -- applicable to any meeting type -- C-07 fail.
FAILS: fewer than three agenda items -- C-06 partial.

---

## SECTION 4 -- DISCUSSION

Simulate each participant in the order declared in Section 2. Each participant block:

**[Participant] ([Role]):** [Contribution -- must reference type-specific evidence]

Type-specific evidence requirements:
- ROB: cite specific metric or readiness data.
- SHIPROOM: name a risk or blocker explicitly.
- ARCH-BOARD: name a trade-off or architectural constraint.

After all participants have spoken, one participant raises the pre-mortem risk:

**PRE-MORTEM RISK -- [Participant] ([Role]):** [A non-obvious, outside-in risk. Must represent a
frame of reference a competent internal reviewer would not automatically predict.]

FAILS: participant contribution does not reference type-specific evidence -- C-07 fail.
FAILS: participant speaks outside their role domain -- C-02 fail.
FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: pre-mortem risk is predictable by insiders -- C-09 outside-in gate not cleared.

---

## SECTION 5 -- DECISIONS

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [decision text] | [approved / rejected / deferred / conditional-approval] | [conditions, or --] |

FAILS: Decisions table absent -- C-03 fail.
FAILS: Outcome column empty for any row -- C-03 fail.
FAILS: agenda item discussed in Section 4 but absent from this table without explanation -- C-03 partial.

---

## SECTION 6 -- ACTION ITEMS

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [action text] | [Name / Role] | [milestone or date] |

FAILS: Owner column empty for any row -- C-04 fail.
FAILS: table absent when Section 4 discussion raised open questions -- C-04 fail.
FAILS: owner listed as TBD without an escalation path -- C-04 partial.

---

## SECTION 7 -- DISSENTING OPINIONS

| Participant | Role | Objection |
|-------------|------|-----------|
| [name] | [role] | [objection in role voice] |

If unanimous: *No dissent recorded -- unanimous decision.*

FAILS: known role-based tension omitted from this table -- C-05 fail.
FAILS: objection not stated in the dissenting participant's role voice -- C-05 partial.

---

## SECTION 8 -- CHARTER CONSTRAINTS HONORED

| Constraint | Charter Requirement | Applied? | Notes |
|------------|---------------------|----------|-------|
| Quorum | [from .roles/] | Yes / No | [count] |
| Veto | [role with veto power] | Exercised / Waived | [outcome] |
| Escalation | [escalation target if deferred] | Applicable / N/A | [path] |
| Scope | [what is out of scope] | Honored | [boundary] |

Populate at least two rows with non-empty Notes.

FAILS: fewer than two rows populated with charter-sourced content -- C-10 partial.
FAILS: entries not tied to language or constraints from .roles/ -- C-10 partial.

---

## SECTION 9 -- AMEND (if invoked)

If the user specified AMEND, apply amendments before generating output:

- AMEND attendees: add a row to Section 2 roster; include their contribution in Section 4
  at the appropriate sequence position.
- AMEND scope: revise Section 3 agenda; revise affected Section 4 contributions.

FAILS: AMEND invoked but output tables reflect pre-amendment state -- C-08 fail.
```

---

## V-03 -- Lifecycle Emphasis (Explicit Phase Boundaries)

**Axis:** Lifecycle emphasis
**Hypothesis:** Dividing execution into three explicit phases -- Phase 0 (pre-meeting setup),
Phase 1 (live meeting simulation), Phase 2 (minutes finalization) -- with hard entry and exit
conditions prevents the most common failure mode: undifferentiated setup-and-simulation prose.
Forces type-specific depth to be committed before any voices are simulated, raising C-07. Also
raises C-12 by requiring injection candidates to be annotated at Phase 0 exit.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Execute in three phases. Each phase has
explicit entry and exit conditions. Do not advance to the next phase until the current phase
is complete.

---

## BEFORE YOU START

Before entering Phase 0, commit to one obligation. Do not write minutes until you have
selected and stated your type.

**ROB (Product Review / Service Review)**
Primary obligation: A readiness verdict backed by metric evidence.
Fail condition: If Phase 1 ends without metric evidence and a verdict, you have not done a
ROB. Return to Phase 1 and add the metric. (C-01 fail)

**SHIPROOM (Go / No-Go)**
Primary obligation: A binary GO or NO-GO decision with a named risk register.
Fail condition: If Phase 2 minutes contain no GO/NO-GO decision line, you produced a
discussion summary. Return to Phase 1 and produce the decision. (C-01 fail, C-03 fail)

**ARCH-BOARD (Architecture Decision Review)**
Primary obligation: An Architecture Decision Record with named trade-offs and a selected
alternative.
Fail condition: If Phase 2 contains no ADR, return to Phase 1 and produce one. (C-01 fail)

---

## PHASE 0 -- PRE-MEETING SETUP

*Entry: user provides committee type and topic.*
*Exit: participant roster confirmed, agenda locked, charter constraints identified.*

### 0.1 -- Type and Topic Declaration

Write:
> Committee type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic under review]

### 0.2 -- Participant Roster

Load .roles/ for this committee type. List every participant with their role and
their primary meeting function.

For any required function without a charter role, annotate:
  [Candidate: [role function] -- pending Phase 1 confirmation]

FAILS: required function left without annotation -- C-11 fail.
FAILS: injection candidate not annotated in Phase 0 roster -- C-12 fail.
FAILS: roster absent when Phase 0 exits -- C-06 partial.

### 0.3 -- Agenda Locked

List 3-5 agenda items appropriate to the committee type. Agenda items must be type-specific:
- ROB: readiness gates, metric review, blocking issues.
- SHIPROOM: go/no-go criteria, risk register, release blockers.
- ARCH-BOARD: decision context, alternatives under consideration, ADR.

FAILS: agenda not locked before Phase 1 begins -- C-06 partial.
FAILS: agenda items generic, not tied to committee type -- C-07 fail.

### 0.4 -- Charter Constraints Identified

Identify at least two charter constraints from .roles/ that must be honored during
Phase 1:
- Quorum requirement.
- Veto holder and conditions.
- Escalation path (for deferred decisions).
- Scope boundary.

FAILS: fewer than two constraints identified at Phase 0 exit -- C-10 partial.

*Phase 0 complete. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: roster confirmed, agenda locked, charter constraints identified.*
*Exit: all agenda items discussed, decisions made, dissent recorded.*

### 1.1 -- Discussion

Simulate each participant in sequence, working through the agenda. Each participant speaks
from their role function. No participant may lead a concern outside their function domain.

For each participant contribution, include type-specific evidence:
- ROB: metric or readiness data referenced.
- SHIPROOM: risk or blocker named explicitly.
- ARCH-BOARD: trade-off or architectural constraint named.

FAILS: participant speaks outside their role domain -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.

### 1.2 -- Pre-Mortem Risk

Before closing discussion, one participant -- the role best suited to an outside-in
perspective -- raises a non-obvious, forward-looking risk. This risk must:
- Not be automatically predicted by a competent internal reviewer.
- Come from outside the team's normal frame of reference.

FAILS: no pre-mortem risk raised before Phase 1 closes -- C-09 fail.
FAILS: risk is predictable by insiders -- C-09 outside-in gate not cleared.

### 1.3 -- Decision Point

Record every decision reached during discussion. Each decision must state an outcome:
- approved / rejected / deferred / conditional-approval

FAILS: agenda item discussed without a decision or deferral recorded -- C-03 fail.
FAILS: outcome not stated for any decision -- C-03 fail.

### 1.4 -- Dissent Check

After decisions are recorded: identify any participant whose role creates tension with the
majority outcome. Record their dissent explicitly. If all agree, note unanimous.

FAILS: role-based tension exists but no dissent recorded at Phase 1 exit -- C-05 fail.

*Phase 1 complete. All agenda items covered, decisions recorded, dissent captured.
Entering Phase 2.*

---

## PHASE 2 -- MINUTES FINALIZATION

*Entry: Phase 1 complete -- all decisions and dissent recorded.*
*Exit: formal minutes produced with all required sections.*

### 2.1 -- Minutes Structure

Produce the final meeting minutes with all sections present:

1. **Meeting Header** -- type, topic, simulated date, quorum status, chair
2. **Participants** -- roster with roles and functions
3. **Agenda** -- items as locked in Phase 0
4. **Discussion Summary** -- per-participant contributions with type-specific evidence
5. **Decisions** -- labeled with outcomes
6. **Action Items** -- each with owner
7. **Dissenting Opinions** -- or "unanimous"
8. **Charter Constraints Honored** -- at least two, per Phase 0 identification
9. **Next Steps** -- follow-up meeting, escalation path, or milestone trigger

FAILS: any section from 1-7 missing -- C-06 fail.
FAILS: fewer than two charter constraints honored and named -- C-10 partial.

### 2.2 -- Action Items

Every action item must name both the action and the responsible party.

FAILS: action item without an owner -- C-04 fail.
FAILS: no action items despite open questions raised in Phase 1 -- C-04 fail.

### 2.3 -- AMEND (if invoked)

If the user invoked AMEND before running the skill:

- AMEND attendees: re-enter Phase 0.2 with the amended roster; re-run Phase 1 with the
  new participant at the appropriate position.
- AMEND scope: re-enter Phase 0.3 with updated agenda; re-run affected Phase 1 discussion.

FAILS: AMEND invoked but output not regenerated from amended Phase 0 -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```

---

## V-04 -- Combined: Phrasing Register + Criterion Annotation Maximized

**Axis:** Phrasing register + criterion annotation
**Hypothesis:** Combining pure imperative voice with criterion ID annotations on every
fill-rule FAIL (not just the minimum three required for C-14) creates a fully traceable
artifact. The model cannot satisfy any FAILS condition without simultaneously holding the
criterion ID it protects. C-13 dominance from V-01's BEFORE YOU START block + C-14
maximization produces the highest rubric traceability composite.

```
You are running /corps-committee.

Simulate the committee meeting. Produce the minutes. Do not explain. Do not hedge.
Produce an artifact.

---

## BEFORE YOU START

State your type. State your obligation. Do not write minutes until you have written these
two lines.

**If ROB:**
Obligation: A readiness verdict backed by metric evidence.
Fail condition: No metric in output = ROB not done = stop, add metric. (C-01 fail)

**If SHIPROOM:**
Obligation: A binary GO or NO-GO decision backed by a risk register.
Fail condition: No GO/NO-GO decision line in output = discussion summary, not shiproom
minutes = add the decision line before continuing. (C-01 fail, C-03 fail)

**If ARCH-BOARD:**
Obligation: An ADR with named trade-offs and a selected alternative.
Fail condition: Trade-off list without a stated winner = arch-board not done = name the
decision. (C-01 fail)

Write:
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Topic: [topic]

---

## 1. ROSTER

Load .roles/. List every participant. State the one concern each participant owns.
Assign no participant two concerns.

Mark any required function without a charter role: [Injection required: [function]] -- C-11.
Mark any injection pending confirmation: [Candidate: [function] -- pending] -- C-12.

FAILS: participant listed without stated concern -- C-02 fail, C-06 partial.
FAILS: participant concern mismatches role function -- C-02 fail.
FAILS: injection-required function not marked -- C-11 fail.
FAILS: injection candidate present but no annotation in roster -- C-12 fail.

---

## 2. AGENDA

State 3-5 items. Every item is type-specific. No generic items.

ROB: readiness gates, metric thresholds, blocking bugs -- C-07.
SHIPROOM: go/no-go criteria, risk register entries, named release blockers -- C-07.
ARCH-BOARD: named alternatives, decision criteria, ADR outcome -- C-07.

FAILS: any item applicable to any committee type without modification -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

---

## 3. DISCUSSION

Simulate each participant. Each speaks once. Each speaks from their role function only.

Role-voice constraints (enforce hard):
- PM: customer value, readiness, release timing. Never leads on deployment topology -- C-02.
- SRE/Ops: reliability, SLOs, operational risk. Never leads product vision -- C-02.
- Architect: system design, trade-offs, constraints. Never owns the business case -- C-02.
- Security: threat model, compliance gaps. Never owns the delivery schedule -- C-02.
- Engineering Lead: implementation feasibility, technical debt. Never owns customer
  narrative -- C-02.

Include type-specific evidence in each contribution -- C-07:
- ROB: participant cites a specific metric or readiness indicator.
- SHIPROOM: participant names a risk or blocker.
- ARCH-BOARD: participant names a trade-off or design constraint.

Final speaker raises the pre-mortem risk:
- Non-obvious: insiders would not predict it automatically -- C-09.
- Outside-in: external frame of reference -- C-09.

FAILS: participant's primary contribution misaligns with role function -- C-02 fail.
FAILS: contribution contains no type-specific evidence -- C-07 fail.
FAILS: no pre-mortem risk raised -- C-09 fail.
FAILS: pre-mortem risk predictable by insiders -- C-09 outside-in gate not cleared.
FAILS: pre-mortem risk represents only internal concerns reframed as external -- C-09 partial.

---

## 4. DECISIONS

Record every decision. State the outcome. Omit nothing that reached a conclusion.

**Decisions**
- [decision] -- [approved / rejected / deferred / conditional-approval]

FAILS: outcome absent for any decision -- C-03 fail.
FAILS: Decisions section absent -- C-03 fail.
FAILS: agenda item discussed but unresolved with no stated explanation -- C-03 partial.
FAILS: deferred item has no owner or trigger for re-entry -- C-04 partial, C-10 partial.

---

## 5. ACTION ITEMS

Record every action. Name every owner. One line per action.

**Action Items**
- [action] -- Owner: [Name / Role]

FAILS: action without owner -- C-04 fail.
FAILS: no actions despite open questions in discussion -- C-04 fail.
FAILS: owner listed as TBD without escalation path -- C-04 partial.
FAILS: action item vague enough to be untestable at follow-up -- C-04 partial.

---

## 6. DISSENT

Record dissent wherever role-based tension exists. Never smooth it over.

**Dissenting Opinions**
- [Participant] ([Role]): [objection in role voice]

Unanimous: *No dissent recorded -- unanimous.*

FAILS: role-based tension exists but dissent omitted -- C-05 fail.
FAILS: dissent present but not in the dissenting participant's role voice -- C-05 partial.
FAILS: dissent section absent entirely (even when unanimous is the outcome) -- C-06 partial.

---

## 7. CHARTER CONSTRAINTS

Name two or more constraints from .roles/ that were honored. State each explicitly.

- Quorum: [met / not met] -- [count required vs. present] -- C-10
- Veto: [exercised / waived] -- [role holding veto] -- C-10
- Escalation: [named path if any decision deferred] -- C-10
- Scope: [boundary honored -- what is excluded] -- C-10

FAILS: fewer than two constraints named -- C-10 partial.
FAILS: constraints named but not sourced from charter language or role definition -- C-10 partial.
FAILS: quorum status omitted when charter defines quorum requirement -- C-10 partial.

---

## 8. AMEND (if invoked)

Apply the amendment. Start from the amended state. Do not generate pre-amendment output
and then patch it.

AMEND attendees: add participant to roster; include their contribution in discussion.
AMEND scope: revise agenda; revise affected discussion contributions.

FAILS: AMEND invoked but output reflects pre-amendment state -- C-08 fail.
FAILS: amendment applied post-generation rather than integrated from the start -- C-08 partial.
```

---

## V-05 -- Combined: Table Format + Role Sequence Ordering + Lifecycle Phases

**Axis:** Output format + role sequence + lifecycle
**Hypothesis:** Combining table-first output with a committee-type-specific role execution
sequence (declared upfront in the BEFORE YOU START table) and Phase 0/1/2 lifecycle structure
produces the most auditable artifact. Role sequence makes C-02 violations detectable by
position; table grammar enforces C-04/C-06 coupling; phases force C-07 type-specific depth
before any simulation begins.

```
You are running /corps-committee.

Simulate the committee meeting before it happens. Use tables for every enumerable section.
Execute participants in the role sequence declared for the committee type. Work in three
phases.

---

## BEFORE YOU START

Identify your committee type. Commit to its obligation, role sequence, and fail condition.

| Type | Primary Obligation | Role Sequence | Automatic Fail Condition |
|------|--------------------|---------------|--------------------------|
| ROB | Readiness verdict backed by metric evidence | PM -> Eng Lead -> SRE -> Security -> Architect | No metric present = ROB not done -- C-01 fail |
| SHIPROOM | Binary GO/NO-GO decision backed by risk register | Eng Lead -> SRE -> Security -> PM -> Architect | No GO/NO-GO line in output = shiproom not done -- C-01 fail, C-03 fail |
| ARCH-BOARD | ADR with named trade-offs and selected winner | Architect -> Eng Lead -> Security -> SRE -> PM | No ADR = arch-board not done -- C-01 fail |

Write:
> **Type:** [ROB / SHIPROOM / ARCH-BOARD] | **Topic:** [topic] | **Role Sequence:** [from table above]

---

## PHASE 0 -- SETUP

*Entry: user provides committee type and topic.*
*Exit: roster confirmed, agenda locked, charter constraints identified, role sequence declared.*

### Participant Roster

| Seq | Participant | Role | Primary Concern | Charter Status |
|-----|-------------|------|-----------------|----------------|
| 1 | [name] | [role from .roles/] | [one concern -- one sentence] | [Standing / Candidate: function] |
| 2 | [name] | [role] | [concern] | [Standing / Candidate: function] |
| ... | | | | |

Rules:
- Load .roles/ for this committee type.
- Sequence positions follow the role sequence declared above.
- Any required function without a charter role: Charter Status = [Candidate: [function] --
  pending Phase 1 confirmation].

FAILS: participant concern misaligns with role function -- C-02 fail.
FAILS: candidate not annotated in Charter Status column -- C-12 fail.
FAILS: required function left uncovered without annotation -- C-11 fail.

### Agenda

| # | Item | Type-Specific Gate | Evidence Required |
|---|------|--------------------|-------------------|
| 1 | [item] | [pass/fail condition] | [what must be present] |
| 2 | [item] | [pass/fail condition] | [what must be present] |
| 3 | [item] | [pass/fail condition] | [what must be present] |

FAILS: agenda items generic -- not tied to committee type -- C-07 fail.
FAILS: fewer than three items -- C-06 partial.

### Charter Constraints Identified

| Constraint | Charter Requirement | Must Honor in Phase 1 |
|------------|--------------------|-----------------------|
| Quorum | [requirement from .roles/] | Yes |
| Veto | [veto holder and conditions] | Yes |
| [additional] | [constraint] | Yes |

Identify at least two rows.

FAILS: fewer than two constraints identified before Phase 0 exits -- C-10 partial.

*Phase 0 complete. Role sequence locked. Entering Phase 1.*

---

## PHASE 1 -- MEETING SIMULATION

*Entry: Phase 0 complete.*
*Exit: all agenda items discussed, decisions and dissent recorded.*

Participants speak in the role sequence declared in BEFORE YOU START. Each participant:
1. References at least one piece of type-specific evidence.
2. Speaks from their role function exclusively.
3. Raises their primary concern from the Phase 0 roster.

**[Seq 1] [Participant] ([Role]):**
[Contribution -- cite type-specific evidence]

**[Seq 2] [Participant] ([Role]):**
[Contribution -- cite type-specific evidence]

[...repeat per participant...]

**PRE-MORTEM RISK -- [Designated Participant] ([Role]):**
[A non-obvious, outside-in risk. Must represent a frame of reference a competent internal
reviewer would not automatically predict. Final contribution of Phase 1.]

FAILS: participant contribution missing type-specific evidence -- C-07 fail.
FAILS: participant speaks outside their role function -- C-02 fail.
FAILS: participant speaks out of declared role sequence without justification -- C-02 partial.
FAILS: no pre-mortem risk raised before Phase 1 closes -- C-09 fail.
FAILS: pre-mortem risk predictable by insiders -- C-09 outside-in gate not cleared.

Decision check after each agenda item:

| Agenda Item | Discussed? | Decision Reached? | Deferred? |
|-------------|------------|-------------------|-----------|
| [item 1] | Yes | [outcome] | No |
| [item 2] | Yes | [outcome] | Yes -- escalation: [path] |
| [item 3] | Yes | [outcome] | No |

FAILS: agenda item discussed without decision or deferral noted -- C-03 fail.

Dissent check:

| Participant | Role | In Tension with Majority? | Dissent Statement |
|-------------|------|--------------------------|-------------------|
| [name] | [role] | Yes / No | [objection in role voice, or --] |

FAILS: known tension exists but row marked No without basis -- C-05 fail.

*Phase 1 complete. Entering Phase 2.*

---

## PHASE 2 -- MINUTES

*Entry: Phase 1 complete.*
*Exit: all formal minutes sections present.*

### Decisions

| # | Decision | Outcome | Conditions |
|---|----------|---------|------------|
| 1 | [decision] | [approved / rejected / deferred / conditional-approval] | [conditions or --] |

FAILS: Outcome column empty for any row -- C-03 fail.
FAILS: Decisions table absent -- C-03 fail.

### Action Items

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [action] | [Name / Role] | [milestone or date] |

FAILS: Owner column empty for any row -- C-04 fail.
FAILS: table absent when Phase 1 raised open questions -- C-04 fail.

### Dissenting Opinions

| Participant | Role | Objection |
|-------------|------|-----------|
| [name] | [role] | [objection in role voice] |

*No dissent -- unanimous.* (if applicable)

FAILS: known role-based tension from Phase 1 omitted -- C-05 fail.

### Charter Constraints Honored

| Constraint | Requirement | Applied | Notes |
|------------|-------------|---------|-------|
| Quorum | [from Phase 0] | Yes / No | [count] |
| Veto | [from Phase 0] | Exercised / Waived | [outcome] |
| [additional] | [from Phase 0] | Honored | [boundary] |

FAILS: fewer than two rows confirmed from Phase 0 constraints -- C-10 partial.

### AMEND (if invoked)

If AMEND was invoked:
- AMEND attendees: re-run Phase 0 roster with new participant; insert their contribution
  in Phase 1 at the correct sequence position.
- AMEND scope: update Phase 0 agenda; re-run affected Phase 1 discussion items.

FAILS: AMEND invoked but Phase 0 and Phase 1 not re-executed from amended inputs -- C-08 fail.

*Phase 2 complete. Minutes produced.*
```
