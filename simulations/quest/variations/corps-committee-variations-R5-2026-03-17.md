Written to `simulations/quest/variations/corps-committee-variations-R5-2026-03-17.md`.

---

## corps-committee R5 — Variation Summary

| ID | Axis | New Mechanism | Hypothesis |
|----|------|---------------|------------|
| V-01 | Inertia depth | NORM-A/B/C labeled normalization inventory | Replaces single-sentence Gate 0-B with an auditable multi-item inventory; each label is independently trackable through Phase 1 Inertia Challenge? cells and Phase 2 pre-mortem risk — closing the gap where R4 V-05 allows outcome restatement to pass C-17 |
| V-02 | Lifecycle | PRE-MORTEM CHAIN CHECK skeleton block at Phase 1→2 boundary | 3-checkbox skeleton gate (challenger identified / outside-in basis stated / risk drafted) prevents Phase 2 from opening without the inertia→challenge→risk chain confirmed; mirrors SYMMETRY CHECK at Phase 3→4 |
| V-03 | Role sequence | Designated Inertia Challenger pre-assigned with rationale and NORM obligation | Requires explicit designation of the one participant least likely to share the normalized assumption before Phase 0 begins; their Inertia Challenge? cell is a required non-None (not "at least one in grid"), transferring outside-in selection from simulation-time to setup-time |
| V-04 | Inertia depth + chain audit | V-01 NORM inventory + V-02 PRE-MORTEM CHAIN CHECK | Labels make the chain audit specific: CHAIN-1 requires a NORM-label citation, not just a non-None entry; CHAIN-3 draft names the same label — creating a precision amplifier the generic audit alone cannot provide |
| V-05 | Full synthesis | V-01 + V-02 + V-03 | Four-checkpoint end-to-end NORM label trace: Gate 0-B declaration → Phase 1 designated challenger row → CHAIN-3 draft → Phase 2 output; label mismatch at any checkpoint is detectable without prose reading |

**Base:** R4 V-05 (2026-03-17) — all C-01 through C-17 already satisfied.

**Three new v6-candidate patterns introduced:**
- **C-18 (cand.)** — NORM-* labeled inventory (V-01/V-04/V-05): converts inertia framing from single-assumption prompt into multi-item labeled checklist with end-to-end citation traceability
- **C-19 (cand.)** — PRE-MORTEM CHAIN CHECK skeleton gate (V-02/V-04/V-05): structural Phase 1→2 checkpoint closing the gap between inertia gate and pre-mortem risk output
- **C-20 (cand.)** — Designated Inertia Challenger with rationale + NORM assignment (V-03/V-05): role-level obligation for outside-in challenge, auditable by cell presence and label match rather than by grid-wide scan
tion before Phase 2 opens; the pre-mortem risk names both the NORM label and the challenger's outside-in basis. Three non-overlapping mechanisms that together close every residual gap left by R4 V-05. |

**Base for all R5 variations:** R4 V-05 (2026-03-17) — BEFORE YOU START with type fail conditions (C-13) + inertia hypothesis Gate 0-B (C-17) + hard phase gates 0-A through 0-F (C-15) + Participant Discussion Grid with Inertia Challenge? column (C-16) + traceable Pre-Mortem Risk (C-09).

---

## V-01 — Axis: Inertia Depth (NORM-* Labeled Normalization Inventory)

**Axis:** Inertia framing — depth of normalization enumeration
**Hypothesis:** R4 V-05's Gate 0-B asks for "the assumption being carried" as a single sentence.
This satisfies C-17 structurally but allows the model to restate the rubber-stamp outcome
in different words rather than naming the underlying normalized beliefs. A labeled NORM-*
inventory (NORM-A, NORM-B, optionally NORM-C) forces the model to enumerate distinct
assumptions — each independently challengeable. The Phase 1 Inertia Challenge? column entry
must cite a specific NORM label, converting the column from a boolean (challenged / not) into
a labeled citation. Phase 2 pre-mortem risk must name the NORM label it connects to, creating
end-to-end traceability: NORM-X declared → NORM-X cited in Phase 1 → NORM-X named in Phase 2.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .roles/.
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

**B. Build the normalization inventory.**

Organizational inertia is not one assumption — it is a set of beliefs the committee has stopped
questioning. Name 2–3 specific normalized assumptions below. Each must name a concrete belief
or behavior the real committee treats as given, which an outsider would push back on.

> NORM-A: [The committee assumes X without questioning it. Insiders cannot see this as a risk
>   because they share the assumption. One sentence — specific, not generic.]
> NORM-B: [A second normalized assumption. Must be distinct from NORM-A in subject matter.]
> NORM-C: [Optional — include only if genuinely distinct from NORM-A and NORM-B. Otherwise omit.]

Rules for NORM items:
- Each must name a specific belief, not a category ("team is too busy" is a category;
  "team has normalized 2-week release delays as acceptable" is a NORM item).
- At least one NORM item must target organizational behavior, not technical risk alone.
- NORM items are sealed when this block completes. They do not change in Phase 1 or Phase 2.

The rubber-stamp outcome: the real committee will proceed without challenging any of these
assumptions. At least one participant in Phase 1 must cite a NORM label in their
Inertia Challenge? cell. The pre-mortem risk in Phase 2 must name the specific NORM label it
connects to.

**C. Name every participant and their charter function.**

Read .roles/. For each participant: role title, primary decision scope, escalation rights.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation].

FAILS: BEFORE YOU START block absent before Phase 0 header — C-13 fail.
FAILS: normalization inventory absent from BEFORE YOU START — C-17 fail.
FAILS: NORM items generic (category, not specific assumption) — C-17 partial.
FAILS: injection candidate not annotated before Phase 0 begins — C-12 fail.
FAILS: required function uncovered without annotation — C-11 fail.

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

**Gate 0-A | Type + obligation**
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Normalization inventory committed**
> NORM-A: [one sentence]
> NORM-B: [one sentence]
> NORM-C: [one sentence, or OMITTED]
> Rubber-stamp outcome: the real committee will proceed assuming [summary of NORM items].

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
FAILS: normalization inventory absent from Gate 0-B — C-17 fail (no labeled targets for Phase 1).
FAILS: NORM items not specific (generic concerns restated) — C-17 partial.

*Gates 0-A through 0-F must all appear before the Phase 1 header.*

---

## PHASE 1 — SIMULATION

*Entry condition: All Phase 0 gates present, including normalization inventory (Gate 0-B).*

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Inertia Challenge? | Dissent | Action | Owner |
|-------------|------|-------------------------------|----------------|-------------------|---------|--------|-------|

Column enforcement rules:
- **Contribution**: Charter-scoped, type-specific evidence required.
  ROB: metric or readiness indicator. SHIPROOM: risk or blocker. ARCH-BOARD: trade-off.
- **Charter Drift?**: YES — [scope] or None. Never blank.
- **Inertia Challenge?**: If this participant challenges a NORM item from Gate 0-B, write:
  "Challenges [NORM-A / NORM-B / NORM-C]: [one-sentence challenge statement]."
  Otherwise: None. Never blank.
  At least one row must cite a specific NORM label. A grid where no row names a NORM
  label means the inventory was declared but never engaged — the rubber-stamp stands
  unchallenged regardless of what the Inertia Challenge? cells contain.
- **Dissent**: Explicit tension statement or None. Never blank.
- **Action**: Open question or follow-up, or None.
- **Owner**: Name the owner if Action is non-None. Empty Owner when Action non-None = C-04 fail.

FAILS: Phase 1 header written before all Phase 0 gates present — C-15 fail.
FAILS: charter constraints appear only in Phase 1 prose, not as Phase 0 gates — C-10 partial, C-15 fail.
FAILS: Inertia Challenge? column all None — C-09 partial (inertia not challenged).
FAILS: Inertia Challenge? entries present but none cites a NORM label — C-17 partial (labeled
  inventory not engaged; generic challenge satisfied the column but not the criterion).
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
1. Raised by a specific participant in Phase 1 (traceable to a grid row with a non-None
   Inertia Challenge? entry citing a NORM label).
2. Not predictable by a competent internal reviewer — outside-in frame required.
3. Names the specific NORM label it connects to from Gate 0-B.

> Pre-mortem risk: [risk statement]
> Raised by: [Participant] ([Role]) — Phase 1 row [#]
> Connected to: [NORM-A / NORM-B / NORM-C] — [one sentence linking risk to that assumption]

FAILS: pre-mortem risk not traceable to a Phase 1 grid row — C-09 fail.
FAILS: risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: risk does not name a NORM label — C-17 partial (inertia chain not closed end-to-end).
FAILS: NORM label cited differs from any label that appeared in Phase 1 grid — C-17 partial
  (chain broken between Phase 1 and Phase 2).

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
AMEND scope: update Gate 0-F; revise affected Contribution cells; re-evaluate normalization inventory
  if scope change affects what assumptions are being normalized.

FAILS: AMEND invoked but BEFORE YOU START not re-executed from amended inputs — C-08 fail.
```

---

## V-02 — Axis: Lifecycle (PRE-MORTEM CHAIN CHECK Skeleton Block)

**Axis:** Lifecycle emphasis — skeleton checkpoint at Phase 1→2 boundary
**Hypothesis:** R4 V-05 has the inertia hypothesis (Gate 0-B), the Inertia Challenge? column
in Phase 1, and a pre-mortem risk section in Phase 2. But there is no structural checkpoint
between Phase 1 closing and Phase 2 opening that verifies the chain is intact. A model can
complete Phase 1 (with Inertia Challenge? rows filled) and immediately produce the Decisions
table in Phase 2 without generating the pre-mortem risk block at all. The PRE-MORTEM CHAIN
CHECK, placed as a skeleton element between the last Phase 1 row and the Phase 2 header,
closes this gap: all three chain links (challenger identified, outside-in basis stated, risk
drafted) must be confirmed before Phase 2 content is generated.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .roles/.
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

This hypothesis is the simulation's pressure point. At least one participant in Phase 1 must
challenge it. The pre-mortem risk in Phase 2 must connect to it. The PRE-MORTEM CHAIN CHECK
block will verify this chain is intact before Phase 2 opens.

**C. Name every participant and their charter function.**

Read .roles/. For each participant: role title, primary decision scope, escalation rights.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation].

FAILS: BEFORE YOU START block absent before Phase 0 header — C-13 fail.
FAILS: inertia hypothesis absent from BEFORE YOU START — C-17 fail.
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
FAILS: inertia hypothesis not committed before Phase 1 begins — C-17 fail, C-09 miss.

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
  summarize the challenge in one sentence. Otherwise: None. Never blank.
  At least one row must be non-None. All-None means the inertia was confirmed, not tested.
- **Dissent**: Explicit tension statement or None. Never blank.
- **Action**: Open question or follow-up, or None.
- **Owner**: Name the owner if Action is non-None. Empty Owner when Action non-None = C-04 fail.

FAILS: Phase 1 header written before all Phase 0 gates present — C-15 fail.
FAILS: charter constraints appear only in Phase 1 prose, not as Phase 0 gates — C-10 partial, C-15 fail.
FAILS: Inertia Challenge? column all None — C-09 partial.
FAILS: Charter Drift? or Dissent column left blank (not None) — C-16 partial.
FAILS: Owner empty when Action non-None — C-04 fail, C-16 partial.
FAILS: Contribution outside charter scope — C-02 fail.
FAILS: Contribution contains no type-specific evidence — C-07 fail.

---

## PRE-MORTEM CHAIN CHECK

DO NOT WRITE THE PHASE 2 HEADER UNTIL ALL THREE BOXES BELOW ARE TICKED.

The chain from inertia to pre-mortem risk has three links. Confirm each before Phase 2 proceeds.

  [ ] CHAIN-1 — Challenger identified: at least one Inertia Challenge? row is non-None.
      Challenger: [Participant name] ([Role]) — Phase 1 row [#]

  [ ] CHAIN-2 — Outside-in basis confirmed: the challenge represents a frame of reference
      the real committee's insider members would not produce on their own.
      Basis: [one sentence explaining why this is outside-in, not insider-predictable]

  [ ] CHAIN-3 — Risk drafted: the risk is the forward projection of the inertia assumption
      if the real committee proceeds without challenging it.
      Draft: [one-sentence pre-mortem risk statement connecting to Gate 0-B assumption]

All three boxes ticked before Phase 2 content is generated.

FAILS: Phase 2 header written before PRE-MORTEM CHAIN CHECK appears — C-09 partial (chain
  not verified before close).
FAILS: any box unticked when Phase 2 header appears — C-09 partial.
FAILS: CHAIN-2 basis circular ("insiders would not predict this because it is non-obvious")
  — C-09 outside-in gate not structurally earned; state why specifically.
FAILS: CHAIN-3 draft not connected to Gate 0-B inertia assumption — C-17 partial
  (pre-mortem risk severed from inertia gate).

---

## PHASE 2 — CLOSE

*Entry condition: PRE-MORTEM CHAIN CHECK complete, all three boxes ticked.*

Resolve all [Candidate: ...] participants. Confirm coverage or record [Unrepresented].

### Pre-Mortem Risk

Expand the CHAIN-3 draft from PRE-MORTEM CHAIN CHECK into the full risk entry.

> Pre-mortem risk: [full risk statement — expands CHAIN-3 draft]
> Raised by: [Participant] ([Role]) — Phase 1 row [#] (same as CHAIN-1 challenger)
> Connected to inertia: [one sentence linking risk to Gate 0-B assumption]

FAILS: pre-mortem risk inconsistent with CHAIN-3 draft — C-09 fail (chain broken at Phase 2).
FAILS: risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: risk not connected to Gate 0-B inertia assumption — C-09 partial, C-17 partial.

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

AMEND attendees: re-enter BEFORE YOU START Part C; re-execute Phase 0 gates; add row to
  Phase 1 grid; re-run PRE-MORTEM CHAIN CHECK against updated grid.
AMEND scope: update Gate 0-F; revise affected Contribution cells; re-evaluate inertia
  hypothesis if scope change alters the rubber-stamp assumption.

FAILS: AMEND invoked but BEFORE YOU START not re-executed from amended inputs — C-08 fail.
FAILS: AMEND changes grid but PRE-MORTEM CHAIN CHECK not re-run — C-09 partial.
```

---

## V-03 — Axis: Role Sequence (Designated Inertia Challenger)

**Axis:** Role sequence — pre-assignment of challenger role before simulation
**Hypothesis:** R4 V-05 requires at least one non-None Inertia Challenge? grid cell, but
leaves which participant challenges the inertia to model discretion at simulation time. This
creates a failure mode: the model selects the most convenient participant (often the PM or
Architect, who are the most normalized insiders) rather than the one whose charter most
likely produces a genuinely outside-in view. Requiring explicit pre-assignment of the
Inertia Challenger — the participant with the most external frame of reference, designated
before Phase 0 begins — makes C-17's organizational normalization framing an obligation
on a specific role, not a generic instruction. The designation creates an auditable
commitment: the selected role must challenge, and the rationale for their selection must
explain why they are least likely to share the normalized assumption.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .roles/.
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

**B. State the inertia hypothesis and designate the Inertia Challenger.**

**B1. Inertia hypothesis:**

Answer: What is this committee's most likely rubber-stamp outcome? What assumption is the real
committee carrying in that a rigorous reviewer would force them to defend?

Write:
> Inertia hypothesis: The real committee is likely to [approve X / defer Y / accept Z] without
> challenge. The assumption being carried: [state it in one sentence].

**B2. Designate the Inertia Challenger:**

Organizational normalization works because insiders share the normalized assumption. The
challenger most likely to surface an outside-in risk is the participant whose charter most
directly represents a constituency external to the committee's standing membership.

Review the participant list from Part C and write:

> Inertia Challenger: [Role title]
> Rationale: [One sentence — why this role's frame of reference is least likely to reflect
>   the normalized assumption stated in B1]
> Obligation: This participant's Inertia Challenge? grid cell in Phase 1 must be non-None.

Challenger selection rules:
- Prefer the most externally-facing role (customer-facing, newly joined, external auditor,
  compliance function with an outside mandate).
- If no participant qualifies, inject an Inertia-Advocate:
  [Candidate: Inertia-Advocate — injected, outside-in frame required].
- Any participant may additionally challenge — but the designated one is required.
- A designation without a rationale fails: rationale is the structural proof that the role
  selection is principled, not arbitrary.

**C. Name every participant and their charter function.**

Read .roles/. For each participant: role title, primary decision scope, escalation rights.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation].

FAILS: BEFORE YOU START block absent before Phase 0 header — C-13 fail.
FAILS: inertia hypothesis absent — C-17 fail.
FAILS: Inertia Challenger designation absent — C-17 partial (hypothesis stated but
  responsibility for challenging it unassigned).
FAILS: Challenger designation present but rationale absent — C-17 partial (designation
  without basis is not a structural guarantee).
FAILS: injection candidate not annotated before Phase 0 begins — C-12 fail.
FAILS: required function uncovered without annotation — C-11 fail.

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

**Gate 0-A | Type + obligation**
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Inertia hypothesis + designated challenger committed**
> Inertia: [rubber-stamp outcome] | Assumption: [one sentence]
> Designated Challenger: [Role] | Rationale: [one sentence]

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
FAILS: inertia hypothesis absent from Gate 0-B — C-17 fail, C-09 miss.
FAILS: designated challenger absent from Gate 0-B — C-17 partial.

*Gates 0-A through 0-F must all appear before the Phase 1 header.*

---

## PHASE 1 — SIMULATION

*Entry condition: All Phase 0 gates present, including inertia hypothesis and designated
challenger (Gate 0-B).*

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Inertia Challenge? | Dissent | Action | Owner |
|-------------|------|-------------------------------|----------------|-------------------|---------|--------|-------|

Column enforcement rules:
- **Contribution**: Charter-scoped, type-specific evidence required.
  ROB: metric or readiness indicator. SHIPROOM: risk or blocker. ARCH-BOARD: trade-off.
- **Charter Drift?**: YES — [scope] or None. Never blank.
- **Inertia Challenge?**: For the designated Inertia Challenger from Gate 0-B, this cell
  MUST be non-None — challenging is required, not optional, for the designated role.
  For all other participants: fill if they challenge; otherwise None. Never blank.
  When non-None: "[Challenge summary] — connects to assumption: [Gate 0-B assumption word]"
  A grid where the designated challenger's cell reads None is a C-17 enforcement failure:
  the obligation was declared in BEFORE YOU START and committed in Gate 0-B, but not
  honored in simulation.
- **Dissent**: Explicit tension statement or None. Never blank.
- **Action**: Open question or follow-up, or None.
- **Owner**: Name the owner if Action is non-None. Empty Owner when Action non-None = C-04 fail.

FAILS: Phase 1 header written before all Phase 0 gates present — C-15 fail.
FAILS: charter constraints appear only in Phase 1 prose, not as Phase 0 gates — C-10 partial, C-15 fail.
FAILS: designated challenger's Inertia Challenge? cell is None — C-17 fail (obligation declared
  but not honored; designation as a structural guarantee is broken).
FAILS: Inertia Challenge? column all None — C-09 partial.
FAILS: Charter Drift? or Dissent left blank (not None) — C-16 partial.
FAILS: Owner empty when Action non-None — C-04 fail, C-16 partial.
FAILS: Contribution outside charter scope — C-02 fail.
FAILS: Contribution contains no type-specific evidence — C-07 fail.

---

## PHASE 2 — CLOSE

Resolve all [Candidate: ...] participants. Confirm coverage or record [Unrepresented].

### Pre-Mortem Risk

Name the one risk the real committee is most likely to miss.

Requirements:
1. Raised by the designated Inertia Challenger from Gate 0-B (traceable to their Phase 1
   grid row, which must be non-None per the designation obligation).
2. Not predictable by a competent internal reviewer — the challenger's rationale from
   Gate 0-B explains why their specific frame of reference surfaces this risk.
3. Connects to the Gate 0-B inertia assumption — the risk is latent in the rubber-stamp
   outcome.

> Pre-mortem risk: [risk statement]
> Raised by: [Designated Challenger] ([Role]) — Phase 1 row [#]
> Connected to inertia: [one sentence linking risk to Gate 0-B assumption]
> Outside-in basis: [one sentence — derived from the challenger's rationale in Gate 0-B,
>   not a generic "insider would not predict this" statement]

FAILS: pre-mortem risk raised by participant other than designated challenger without
  explanation of why the designated challenger did not produce the stronger risk — C-17
  partial (designation chain broken).
FAILS: risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: risk not connected to Gate 0-B assumption — C-09 partial.
FAILS: outside-in basis is generic rather than derived from the challenger's rationale — C-17
  partial (the rationale exists but is not load-bearing).

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

AMEND attendees: re-enter BEFORE YOU START; re-execute Phase 0 gates; if new participant is
  more external-facing than the current designated challenger, re-designate; add row to Phase 1 grid.
AMEND scope: update Gate 0-F; revise affected Contribution cells; re-evaluate inertia
  hypothesis if scope change affects what is being normalized.

FAILS: AMEND invoked but BEFORE YOU START not re-executed from amended inputs — C-08 fail.
FAILS: new participant added who is more external-facing than current challenger, but
  challenger designation not reconsidered — C-17 partial.
```

---

## V-04 — Axes A + B: Normalization Inventory + Chain Audit

**Axis:** Inertia depth + lifecycle checkpoint
**Hypothesis:** V-01's NORM-* labeled inventory and V-02's PRE-MORTEM CHAIN CHECK compose
without redundancy and with a precision amplifier: when the inventory provides named labels,
the chain audit checkboxes become label citations rather than generic confirmations. CHAIN-1
verifies "at least one Inertia Challenge? row cites a NORM label" rather than "at least one
row is non-None" — the distinction is that a model can produce a non-None challenge that
does not engage the inventory, which CHAIN-1 with label-citation requirement catches.
CHAIN-3 drafts a risk statement and names the NORM label it connects to, making the
NORM-to-risk chain auditable in one block rather than across two phases.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .roles/.
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

**B. Build the normalization inventory.**

Enumerate 2–3 specific normalized assumptions below. Each must name a concrete belief or
behavior the real committee treats as given, which an outsider would challenge.

> NORM-A: [specific normalized assumption — one sentence]
> NORM-B: [distinct second assumption — one sentence]
> NORM-C: [optional third — include only if distinct from NORM-A and NORM-B, else omit]

Rules:
- Each NORM item names a specific belief, not a generic concern.
- At least one must target organizational behavior, not technical risk alone.
- NORM items are sealed when this block completes. They do not change in Phases 1 or 2.
- The rubber-stamp outcome: the real committee will proceed assuming all NORM items hold.
- At least one Phase 1 Inertia Challenge? cell must cite a NORM label.
- The Phase 2 pre-mortem risk must name the NORM label it connects to.

**C. Name every participant and their charter function.**

Read .roles/. For each participant: role title, primary decision scope, escalation rights.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation].

FAILS: BEFORE YOU START block absent before Phase 0 header — C-13 fail.
FAILS: normalization inventory absent from BEFORE YOU START — C-17 fail.
FAILS: NORM items generic (category, not specific belief) — C-17 partial.
FAILS: injection candidate not annotated before Phase 0 begins — C-12 fail.
FAILS: required function uncovered without annotation — C-11 fail.

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

**Gate 0-A | Type + obligation**
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Normalization inventory committed**
> NORM-A: [one sentence]
> NORM-B: [one sentence]
> NORM-C: [one sentence, or OMITTED]
> Rubber-stamp outcome: the real committee will proceed assuming [summary].

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
FAILS: normalization inventory absent from Gate 0-B — C-17 fail.

*Gates 0-A through 0-F must all appear before the Phase 1 header.*

---

## PHASE 1 — SIMULATION

*Entry condition: All Phase 0 gates present, including normalization inventory (Gate 0-B).*

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Inertia Challenge? | Dissent | Action | Owner |
|-------------|------|-------------------------------|----------------|-------------------|---------|--------|-------|

Column enforcement rules:
- **Contribution**: Charter-scoped, type-specific evidence required.
  ROB: metric or readiness indicator. SHIPROOM: risk or blocker. ARCH-BOARD: trade-off.
- **Charter Drift?**: YES — [scope] or None. Never blank.
- **Inertia Challenge?**: If this participant challenges a NORM item, write:
  "Challenges [NORM-A / NORM-B / NORM-C]: [one-sentence challenge]."
  Otherwise: None. Never blank. At least one row must cite a NORM label — a grid with
  no NORM label cited means the inventory was declared but never engaged.
- **Dissent**: Explicit tension statement or None. Never blank.
- **Action**: Open question or follow-up, or None.
- **Owner**: Name the owner if Action is non-None. Empty Owner when Action non-None = C-04 fail.

FAILS: Phase 1 header written before all Phase 0 gates present — C-15 fail.
FAILS: charter constraints appear only in Phase 1 prose, not as Phase 0 gates — C-10 partial, C-15 fail.
FAILS: Inertia Challenge? entries present but none cites a NORM label — C-17 partial.
FAILS: Inertia Challenge? column all None — C-09 partial.
FAILS: Charter Drift? or Dissent left blank (not None) — C-16 partial.
FAILS: Owner empty when Action non-None — C-04 fail, C-16 partial.
FAILS: Contribution outside charter scope — C-02 fail.
FAILS: Contribution contains no type-specific evidence — C-07 fail.

---

## PRE-MORTEM CHAIN CHECK

DO NOT WRITE THE PHASE 2 HEADER UNTIL ALL THREE BOXES ARE TICKED.

  [ ] CHAIN-1 — Inventory engaged: at least one Inertia Challenge? row cites a NORM label
      (NORM-A / NORM-B / NORM-C — not just a non-None entry).
      Label cited: [NORM-A / NORM-B / NORM-C]
      Challenger: [Participant name] ([Role]) — Phase 1 row [#]

  [ ] CHAIN-2 — Outside-in basis confirmed: the challenge from CHAIN-1 represents a frame of
      reference the real committee's insider members would not produce on their own.
      Basis: [one sentence — why this specific challenger's frame is outside-in, not generic]

  [ ] CHAIN-3 — Risk drafted and label named: the risk is the forward projection of the cited
      NORM item if the real committee proceeds without addressing it.
      NORM label: [same as CHAIN-1]
      Draft: [one-sentence pre-mortem risk statement]

All three boxes ticked before Phase 2 content is generated.

FAILS: Phase 2 header written before PRE-MORTEM CHAIN CHECK appears — C-09 partial.
FAILS: any box unticked when Phase 2 header appears — C-09 partial.
FAILS: CHAIN-1 cites a non-None challenge entry that does not name a NORM label — C-17
  partial (inventory stated but chain uses generic challenge, not labeled citation).
FAILS: CHAIN-3 NORM label differs from CHAIN-1 NORM label — C-17 partial (chain cites
  different labels at commit and draft; end-to-end traceability broken).
FAILS: CHAIN-3 draft not connected to Gate 0-B rubber-stamp outcome — C-17 partial.

---

## PHASE 2 — CLOSE

*Entry condition: PRE-MORTEM CHAIN CHECK complete, all three boxes ticked.*

Resolve all [Candidate: ...] participants. Confirm coverage or record [Unrepresented].

### Pre-Mortem Risk

Expand CHAIN-3 draft from PRE-MORTEM CHAIN CHECK into the full risk entry.

> Pre-mortem risk: [full risk statement — expands CHAIN-3 draft]
> Raised by: [Participant] ([Role]) — Phase 1 row [#] (same as CHAIN-1 challenger)
> Connected to: [NORM-A / NORM-B / NORM-C] — [one sentence linking risk to that assumption]

FAILS: NORM label in Pre-Mortem Risk differs from CHAIN-1 and CHAIN-3 labels — C-17 partial
  (label chain breaks between audit block and final output).
FAILS: risk inconsistent with CHAIN-3 draft — C-09 fail (chain broken at Phase 2 fill).
FAILS: risk predictable by insiders — C-09 outside-in gate not cleared.

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

AMEND attendees: re-enter BEFORE YOU START Part C; re-execute Phase 0 gates; add row to Phase 1
  grid; re-run PRE-MORTEM CHAIN CHECK against updated grid.
AMEND scope: update Gate 0-F; revise affected Contribution cells; re-evaluate normalization
  inventory if scope change affects what assumptions are being normalized.

FAILS: AMEND invoked but BEFORE YOU START not re-executed from amended inputs — C-08 fail.
FAILS: AMEND changes grid and PRE-MORTEM CHAIN CHECK is not re-run — C-09 partial.
```

---

## V-05 — Full Synthesis: NORM Inventory + Chain Audit + Designated Challenger

**Axis:** All three R5 axes on top of the complete R4 V-05 foundation
**Hypothesis:** Three mechanisms, each targeting a distinct residual gap in R4 V-05:
(1) NORM-* labeled inventory converts C-17's single-sentence inertia framing into an
auditable multi-item checklist — each assumption independently trackable through Phase 1
and Phase 2; (2) PRE-MORTEM CHAIN CHECK closes the Phase 1→2 transition gap — no Phase 2
content until the chain from NORM label to outside-in basis to risk draft is confirmed in
a skeleton block; (3) Designated Inertia Challenger makes C-17's "organizational
normalization" framing a role obligation, not a general instruction — one participant
is selected before Phase 0, justified by rationale, required to challenge in Phase 1,
and named in the chain audit. The three mechanisms compose: the designated challenger is
required to cite a NORM label (not just produce a non-None entry), the chain audit checks
that the cited NORM label from the designated challenger's row propagates to the CHAIN-3
draft, and the Phase 2 pre-mortem risk names the same label — creating a closed end-to-end
trace from normalization assumption declaration to outside-in risk output.

```
You are running /corps-committee.

Simulate a committee meeting before it happens. Read participant charters from .roles/.
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

**B. Build the normalization inventory and designate the Inertia Challenger.**

**B1. Normalization inventory:**

Name 2–3 specific normalized assumptions the real committee carries. Each must identify
a concrete belief the committee treats as given, which an outsider would push back on.

> NORM-A: [specific normalized assumption — one sentence]
> NORM-B: [distinct second assumption — one sentence]
> NORM-C: [optional third — omit if not genuinely distinct]

Rules:
- Each NORM item names a specific belief, not a category of concern.
- At least one must target organizational behavior, not technical risk alone.
- NORM items are sealed at this block. They do not change in Phases 1 or 2.
- The rubber-stamp outcome: the real committee will proceed assuming all NORM items hold.

**B2. Designate the Inertia Challenger:**

Organizational normalization works because insiders share the normalized assumption.
Identify the participant whose charter most directly represents a constituency external
to the committee's standing membership.

Write:
> Inertia Challenger: [Role title]
> Rationale: [One sentence — why this role is least likely to share the normalized
>   assumptions in B1]
> Primary obligation: Challenge [NORM-A / NORM-B / NORM-C] (whichever this role is
>   best positioned to surface as external risk) in Phase 1.
> Required: this participant's Inertia Challenge? grid cell must cite their assigned NORM label.

Challenger selection rules:
- Prefer the most externally-facing role (customer advocate, compliance function with
  external mandate, newly joined team member, external auditor).
- If no participant qualifies, inject an Inertia-Advocate:
  [Candidate: Inertia-Advocate — injected, designated challenger for NORM-* coverage].
- Any participant may additionally challenge — but the designated one must challenge their
  assigned NORM item.
- Designation without rationale fails. Rationale without assigned NORM label fails.

**C. Name every participant and their charter function.**

Read .roles/. For each participant: role title, primary decision scope, escalation rights.
Injection candidates: [Candidate: [function] — pending Phase 1 confirmation].

FAILS: BEFORE YOU START block absent before Phase 0 header — C-13 fail.
FAILS: normalization inventory absent — C-17 fail.
FAILS: NORM items generic (category, not specific belief) — C-17 partial.
FAILS: Inertia Challenger designation absent — C-17 partial.
FAILS: designation present but rationale absent — C-17 partial.
FAILS: designation present but no NORM label assigned — C-17 partial (obligation unspecified).
FAILS: injection candidate not annotated — C-12 fail.
FAILS: required function uncovered without annotation — C-11 fail.

---

## PHASE 0 — GATE BLOCK

YOU MAY NOT WRITE THE PHASE 1 HEADER UNTIL ALL GATES APPEAR IN YOUR OUTPUT.

**Gate 0-A | Type + obligation**
> Type: [ROB / SHIPROOM / ARCH-BOARD] | Obligation: [one sentence]

**Gate 0-B | Normalization inventory + designated challenger committed**
> NORM-A: [one sentence]
> NORM-B: [one sentence]
> NORM-C: [one sentence, or OMITTED]
> Rubber-stamp outcome: the real committee will proceed assuming [summary].
> Designated Challenger: [Role] | Assigned NORM: [NORM-A / NORM-B / NORM-C]
> Rationale: [one sentence — why this role's frame is outside-in for the assigned NORM item]

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
FAILS: normalization inventory absent from Gate 0-B — C-17 fail.
FAILS: designated challenger or assigned NORM label absent from Gate 0-B — C-17 partial.

*Gates 0-A through 0-F must all appear before the Phase 1 header.*

---

## PHASE 1 — SIMULATION

*Entry condition: All Phase 0 gates present, including normalization inventory and
designated challenger (Gate 0-B).*

ALL DISCUSSION OUTPUT USES THE PARTICIPANT GRID.

### Participant Discussion Grid

| Participant | Role | Contribution (charter-scoped) | Charter Drift? | Inertia Challenge? | Dissent | Action | Owner |
|-------------|------|-------------------------------|----------------|-------------------|---------|--------|-------|

Column enforcement rules:
- **Contribution**: Charter-scoped, type-specific evidence required.
  ROB: metric or readiness indicator. SHIPROOM: risk or blocker. ARCH-BOARD: trade-off.
- **Charter Drift?**: YES — [scope] or None. Never blank.
- **Inertia Challenge?**: For the designated Inertia Challenger from Gate 0-B, this cell
  MUST be non-None AND must cite their assigned NORM label:
  "Challenges [assigned NORM label]: [one-sentence challenge statement]."
  For all other participants: if they challenge any NORM item, write:
  "Challenges [NORM-A / NORM-B / NORM-C]: [challenge]." Otherwise: None. Never blank.
  A grid where the designated challenger's cell is None, or where no row cites any NORM
  label, fails the inertia chain at its first link.
- **Dissent**: Explicit tension statement or None. Never blank.
- **Action**: Open question or follow-up, or None.
- **Owner**: Name the owner if Action is non-None. Empty Owner when Action non-None = C-04 fail.

FAILS: Phase 1 header written before all Phase 0 gates present — C-15 fail.
FAILS: charter constraints appear only in Phase 1 prose, not as Phase 0 gates — C-10 partial, C-15 fail.
FAILS: designated challenger's Inertia Challenge? cell is None — C-17 fail (obligation declared
  and committed, not honored).
FAILS: designated challenger's cell is non-None but does not cite the assigned NORM label — C-17
  partial (challenger challenges something, but not their assigned normalization item).
FAILS: no row cites any NORM label — C-17 partial (inventory declared, never engaged).
FAILS: Inertia Challenge? column all None — C-09 partial.
FAILS: Charter Drift? or Dissent left blank (not None) — C-16 partial.
FAILS: Owner empty when Action non-None — C-04 fail, C-16 partial.
FAILS: Contribution outside charter scope — C-02 fail.
FAILS: Contribution contains no type-specific evidence — C-07 fail.

---

## PRE-MORTEM CHAIN CHECK

DO NOT WRITE THE PHASE 2 HEADER UNTIL ALL THREE BOXES ARE TICKED.

  [ ] CHAIN-1 — Designated challenger honored with NORM label: the designated challenger's
      Inertia Challenge? cell cites their assigned NORM label.
      NORM label cited: [NORM-A / NORM-B / NORM-C] (must match assigned NORM in Gate 0-B)
      Challenger: [Participant name] ([Role]) — Phase 1 row [#]

  [ ] CHAIN-2 — Outside-in basis derived from rationale: the challenger's rationale from
      Gate 0-B explains why their specific frame surfaces the cited NORM item as external risk,
      not just as a generic non-obvious concern.
      Basis: [one sentence — derived from Gate 0-B rationale, not restated generically]

  [ ] CHAIN-3 — Risk drafted and NORM label named: the risk is the forward projection of
      the CHAIN-1 NORM item if the real committee proceeds without challenging it.
      NORM label: [same as CHAIN-1 — must match]
      Draft: [one-sentence pre-mortem risk statement]

All three boxes ticked before Phase 2 content is generated.

FAILS: Phase 2 header written before PRE-MORTEM CHAIN CHECK appears — C-09 partial.
FAILS: any box unticked when Phase 2 header appears — C-09 partial.
FAILS: CHAIN-1 NORM label differs from the assigned NORM in Gate 0-B — C-17 fail
  (designated challenger challenged a different assumption than assigned).
FAILS: CHAIN-2 basis is generic ("insiders would not predict this") rather than derived
  from the Gate 0-B rationale — C-17 partial (rationale not load-bearing).
FAILS: CHAIN-3 NORM label differs from CHAIN-1 label — C-17 partial (label chain breaks
  between grid and draft).
FAILS: CHAIN-3 draft not connected to Gate 0-B rubber-stamp outcome — C-17 partial.

---

## PHASE 2 — CLOSE

*Entry condition: PRE-MORTEM CHAIN CHECK complete, all three boxes ticked.*

Resolve all [Candidate: ...] participants. Confirm coverage or record [Unrepresented].

### Pre-Mortem Risk

Expand the CHAIN-3 draft from PRE-MORTEM CHAIN CHECK into the full risk entry.

> Pre-mortem risk: [full risk statement — expands CHAIN-3 draft]
> Raised by: [Designated Challenger] ([Role]) — Phase 1 row [#] (same as CHAIN-1 challenger)
> Connected to: [NORM-A / NORM-B / NORM-C] — [one sentence linking risk to that assumption]
>   (must match CHAIN-1 and CHAIN-3 labels end-to-end)
> Outside-in basis: [one sentence — derived from the challenger's Gate 0-B rationale,
>   connecting why their frame of reference specifically surfaces this risk]

FAILS: NORM label in Pre-Mortem Risk differs from CHAIN-1 / CHAIN-3 labels — C-17 partial
  (label chain broken between audit block and final output).
FAILS: risk inconsistent with CHAIN-3 draft — C-09 fail (chain broken at Phase 2 fill).
FAILS: risk predictable by insiders — C-09 outside-in gate not cleared.
FAILS: outside-in basis is generic rather than derived from the designated challenger's
  Gate 0-B rationale — C-17 partial (the designation exists but does not explain the risk).

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

AMEND attendees: re-enter BEFORE YOU START; re-execute Phase 0 gates; if new participant is
  more external-facing, re-designate challenger and re-assign NORM label; add row to Phase 1
  grid; re-run PRE-MORTEM CHAIN CHECK against updated grid.
AMEND scope: update Gate 0-F; revise Contribution cells; re-evaluate normalization inventory
  and re-check whether assigned NORM item is still the strongest inertia target.

FAILS: AMEND invoked but BEFORE YOU START not re-executed from amended inputs — C-08 fail.
FAILS: new participant added who is more external-facing, but challenger designation not
  reconsidered — C-17 partial (designation selection not re-evaluated against new roster).
FAILS: AMEND changes grid and PRE-MORTEM CHAIN CHECK not re-run — C-09 partial.
```

---

## Design Notes for Scorer

### Axis A — NORM-* labeled inventory vs. single-sentence inertia hypothesis

R4 V-05's Gate 0-B asks: "The assumption being carried: [one sentence]." This satisfies
C-17's structural requirement — the inertia gate is present before Phase 1. But a single
sentence allows the model to restate the rubber-stamp outcome in different words, producing
a hypothesis that is descriptively equivalent to the outcome itself (e.g., "The committee
assumes the current approach is sufficient" paraphrases "The committee will approve without
challenge"). The labeled NORM-* inventory forces enumeration of distinct underlying beliefs
rather than outcome restatement. The label granularity (NORM-A vs. NORM-B vs. NORM-C) also
creates a new dimension of Phase 1 grid compliance: "did the grid engage the inventory?" is
now auditable by column scan (does any Inertia Challenge? cell cite a NORM label?) rather
than by content reading.

### Axis B — PRE-MORTEM CHAIN CHECK as Phase 1→2 skeleton gate

R4 V-05 has inertia framing at Phase 0 (Gate 0-B) and pre-mortem risk at Phase 2. The
Inertia Challenge? column bridges them through Phase 1. But there is no skeleton element at
the Phase 1→2 boundary that verifies the bridge is intact before Phase 2 opens. A model can
complete a syntactically correct Phase 1 grid (including at least one non-None Inertia
Challenge? row) and then write Decisions and Action Items in Phase 2 without ever generating
the Pre-Mortem Risk section. The PRE-MORTEM CHAIN CHECK block — inserted as a skeleton
element between the last Phase 1 row and the Phase 2 header — closes this gap: three
checkbox confirmations (challenger identified, basis stated, risk drafted) must appear in
the output before the Phase 2 header is permitted.

### Axis C — Designated challenger as role-level C-17 obligation

C-17's test is whether the skill distinguishes between risks a competent insider would spot
and risks normalized into invisibility. R4 V-05 enforces this through the Inertia Challenge?
column: at least one non-None entry, and the pre-mortem risk must connect to Gate 0-B.
But the model selects which participant challenges at simulation time — defaulting to the
participant generating the most compelling voice, not necessarily the one whose charter is
most outside-in. Explicit pre-assignment of the Inertia Challenger — with rationale explaining
why that specific role is least normalized — transfers the outside-in selection obligation
from the simulation phase to the setup phase. The selected role's Inertia Challenge? cell is
a required non-None (not just "at least one" in the grid), and the Phase 2 outside-in basis
must derive from the stated rationale rather than a generic claim.

### V-04 precision amplifier: NORM label citation in PRE-MORTEM CHAIN CHECK

When NORM labels exist (V-01/V-04/V-05), CHAIN-1 can be specific: "at least one row cites
a NORM label" is a higher bar than "at least one row is non-None." A non-None challenge that
says "the proposal assumes team capacity" does not cite NORM-B ("team has normalized 60%
capacity utilization as safe headroom") — it is a generic concern that could appear in any
committee simulation regardless of the inventory. Label citation forces the grid entry to
engage the specific normalized belief, not just produce a challenge-shaped output.

### V-05 closed-loop end-to-end trace

V-05 creates a traceable path with four named checkpoints:

  Gate 0-B (NORM label declared) →
  Phase 1 grid designated challenger row (NORM label cited) →
  PRE-MORTEM CHAIN CHECK CHAIN-3 (NORM label in draft) →
  Phase 2 Pre-Mortem Risk (NORM label in final output)

Each checkpoint names the same NORM label. A failure at any checkpoint is detectable by
label mismatch without reading the surrounding prose. This is a different property from
C-16 (violations visible by column scan) — it is end-to-end label consistency across
four output locations, which is a new scoreable signal distinct from column-structural
compliance.
```
