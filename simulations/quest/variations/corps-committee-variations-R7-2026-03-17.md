# Quest Variate — corps-committee Round 7

5 complete, runnable skill body prompt variations. Single-axis for V-01 through V-03, combined for V-04 and V-05.

---

## V-01 — Axis: Output Format
**Hypothesis**: Replacing prose sections with per-criterion column grids makes violations structurally visible at scan time without reading prose content.

```markdown
# corps-committee

Simulate a committee meeting before the real one.
Types: ROB (product/service review) | shiproom (go/no-go) | arch-board (architecture decision review)
Read participant charters from `.roles/`. AMEND: add attendees, change scope.

---

## BEFORE YOU START

Commit these type obligations before generating any output:

- ROB: You must cite at least one metric or feature readiness signal. No metric = you have not done a ROB. If there is no metric, you have not done a ROB.
- Shiproom: You must state a go/no-go verdict with a blocking issues list. No blocking list = you have not done a shiproom.
- Arch-board: You must name at least two architectural trade-offs and produce an ADR summary. No trade-offs = you have not done an arch-board.

---

## DESIGNATED INERTIA CHALLENGER
> Standalone block — rendered before Phase 0 roster construction begins.

| Field | Value |
|-------|-------|
| Role | [role name from .roles/] |
| Rationale | [why this role's frame is least likely to reflect normalized assumptions] |
| NORM Obligation | [must challenge at least one NORM-* item by label in Phase 1 grid] |

If no qualifying participant exists: `[Inertia-Advocate — Candidate participant, not in standing roster. Confirmed or replaced in Phase 2.]`

---

## Phase 0 — Charter Setup

State these as entry conditions before Phase 1 begins:

| Constraint | Value | Source |
|------------|-------|--------|
| Committee Type | ROB / Shiproom / Arch-board | |
| Quorum Threshold | [n required] | `.roles/[charter]` |
| Scope Boundary | [what is in/out] | |
| Escalation Path | [path if blocked] | |

**NORM Inventory** (Gate 0-B) — decompose inertia into named beliefs:

| Label | Normalized Belief (specific, not a category) | Observable Behavior | Challenger |
|-------|----------------------------------------------|---------------------|------------|
| NORM-1 | [specific assumption the committee holds as default] | [how to observe it] | [role] |
| NORM-2 | [specific assumption] | [observable behavior] | [role] |
| NORM-3 | [specific assumption] | [observable behavior] | [role] |

Gate 0-B pass: ≥3 NORM items with observable behaviors. Category headings instead of specific beliefs = FAILS: C-18.

**Roster Table**:

| # | Participant | Role | Charter Function | NORM Obligation | Provisional? |
|---|-------------|------|------------------|-----------------|--------------|
| 1 | | | | None / NORM-* | No / [Candidate — confirmed or replaced in Phase 2] |

Inject a provisional candidate if no roster participant covers a required charter function. FAILS: asserting coverage without basis — C-11.

---

## PRE-MORTEM CHAIN CHECK — Gate 1→2

Complete all three before Phase 2 begins:

| # | Checkpoint | Requirement | Status |
|---|------------|-------------|--------|
| CHAIN-1 | Challenger identified | Non-None participant named | [ ] |
| CHAIN-2 | Outside-in basis stated | Not derivable from internal knowledge or general reasoning — circular basis explicitly fails | [ ] |
| CHAIN-3 | Risk draft recorded | Connected to a named NORM label | [ ] |

Phase 2 pre-mortem must expand CHAIN-3 draft. Inconsistency between CHAIN-3 and Phase 2 output = FAILS: C-19.

---

## Phase 1 — Simulation Grid

Sequence: Inertia Challenger → dissent-likely roles → domain experts → charter holder last.

| Participant | Role Frame | Primary Concern | Evidence Cited | Inertia Challenge? | Role-Consistent? |
|-------------|------------|-----------------|----------------|-------------------|------------------|
| [name] | [role framing] | [concern] | [metric/spec/clause] | NORM-* or None | Yes / FAILS: C-02 |

- PM primary concern must not be deployment topology. FAILS: role drift — C-02.
- SRE primary concern must not be product vision. FAILS: role drift — C-02.
- Designated Challenger's Inertia Challenge cell must be non-None. FAILS: C-20.

---

## Phase 2 — Minutes Output

**Header**

| Field | Value |
|-------|-------|
| Committee | [type] |
| Date | |
| Quorum | [n/N present — Met / Not Met] |
| Scope | [from charter] |
| Escalation | [path / N/A] |

**Decisions Table** (required):

| # | Decision | Outcome | Confidence | Condition |
|---|----------|---------|------------|-----------|
| 1 | | Approved / Rejected / Deferred / Conditional | | [if conditional] |

Empty Outcome cell = FAILS: C-03.

**Action Items Table** (Owner is a required column):

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | | [named person or role — not a team] | |

Empty Owner cell = FAILS: C-04.

**Dissent Table** (one row per participant who could plausibly dissent):

| Participant | Position | Basis | vs. Majority |
|-------------|----------|-------|--------------|
| [name] | Agree / Dissent / Conditional | | Aligned / Opposed / Conditional |

Missing row for a participant with grounds to dissent = FAILS: C-05. Missing Dissent cell = FAILS: C-22.

**Pre-Mortem Risk** (expand CHAIN-3):

| Risk | Outside-In Basis | NORM Source | Consequence if Ignored |
|------|-----------------|-------------|------------------------|
| [risk] | [external frame — not derivable from internal knowledge] | NORM-* | |

Circular or internal basis = FAILS: C-09.

**Charter Compliance**:

| Constraint | Honored? | Evidence |
|------------|----------|----------|
| Quorum | Yes / No | |
| Scope | Yes / No | |
| Veto | Yes / No / N/A | |
| Escalation | Yes / No / N/A | |

---

## AMEND Protocol

When AMEND is invoked: treat injection as default, not exception — C-11. Add provisional annotation for unconfirmed charter coverage. Re-run Phase 1 grid rows for injected participants.

---

## Fill-Rule FAIL Annotations

Annotate any non-compliant cell with its criterion ID:
`[MISSING OUTCOME — C-03]` | `[MISSING OWNER — C-04]` | `[ROLE DRIFT — C-02]` | `[NO METRIC — C-07]` | `[CIRCULAR BASIS — C-09]` | `[MISSING DISSENT ROW — C-05]`
```

---

## V-02 — Axis: Phrasing Register
**Hypothesis**: Direct imperative voice with explicit FAIL conditions after every instruction produces more consistent enforcement than descriptive guidance — the model treats FAIL annotations as hard stops rather than suggestions.

```markdown
# corps-committee

YOU ARE SIMULATING A COMMITTEE MEETING BEFORE THE REAL ONE.

Select one type:
- **ROB** — product or service review. Produces a verdict on readiness.
- **Shiproom** — go/no-go gate. Produces a ship/hold decision.
- **Arch-board** — architecture decision review. Produces an ADR.

Read charters from `.roles/`. Honor every constraint you find there.

---

## BEFORE YOU START — READ ALL OF THIS FIRST

**ROB obligation**: Cite a metric. Find a readiness signal. If you write ROB minutes without a metric, you have not done a ROB — stop and find one.
FAIL IF: discussion section contains no quantitative evidence. → C-07.

**Shiproom obligation**: List the blocking issues. State the go/no-go verdict explicitly. If you do not state go or no-go, you have not run a shiproom.
FAIL IF: verdict is absent or paraphrased. → C-03, C-07.

**Arch-board obligation**: Name the trade-offs. Write the ADR title. If you list options without naming what you are trading, you have not run an arch-board.
FAIL IF: trade-offs are unlabeled or implicit. → C-07.

---

## STEP 1 — DESIGNATE THE INERTIA CHALLENGER

Do this before roster construction. Do not embed this in the roster.

State:
1. Which participant role is the Inertia Challenger.
2. Why their frame is least likely to reflect normalized committee assumptions.
3. Which NORM labels they are obligated to challenge.

FAIL IF: challenger is not named before the roster is built. → C-23.
FAIL IF: rationale is generic ("outside perspective"). → C-20.
FAIL IF: no qualifying participant exists and you do not inject a provisional candidate. → C-20.

---

## STEP 2 — BUILD THE NORM INVENTORY

Name the organizational beliefs the committee will rubber-stamp without challenge.

For each belief:
- Give it a label: NORM-1, NORM-2, NORM-3 (minimum three).
- State the belief specifically — not a category.
- State the observable behavior that reveals it.

FAIL IF: fewer than three NORM items. → C-18.
FAIL IF: items are category headings ("performance concerns") rather than named beliefs. → C-18.
FAIL IF: no observable behavior is listed. → C-18.

---

## STEP 3 — CHARTER VALIDATION

Read the charter. State these before simulation begins:

- Quorum: how many required, how many present.
- Scope: what is in scope. What is out.
- Escalation path: where does a blocked decision go.
- Veto: who holds it, under what condition.

FAIL IF: simulation begins before these are stated. → C-15.
FAIL IF: any constraint is listed as TBD. → C-10.

---

## STEP 4 — BUILD ROSTER

List every participant. For each:
- Name the role.
- State the charter function they guard.
- Assign their NORM obligation (which NORM label they must challenge, or None).
- Mark provisional if charter coverage is unconfirmed.

DO NOT assert that a role covers a function without evidence. If the charter does not cover a required function, inject a provisional candidate.

FAIL IF: you claim a participant covers a function that their charter does not mention. → C-11.
FAIL IF: a provisional participant lacks a forward-reference annotation. → C-12.

---

## STEP 5 — SIMULATE DISCUSSION

Run participants in this order: Inertia Challenger first. Then roles most likely to dissent. Then domain experts. Charter holder last.

For each participant:
- Speak from their role charter — not generically.
- A PM does not raise deployment topology as a primary concern.
- An SRE does not lead with product vision.
- The Inertia Challenger must challenge at least one NORM label by name.

FAIL IF: any participant's primary concern does not match their charter function. → C-02.
FAIL IF: the Inertia Challenger raises no NORM-specific challenge. → C-20.

---

## STEP 6 — CHAIN CHECK (required before writing decisions)

Answer these three questions before proceeding:

CHAIN-1: Who is the Inertia Challenger? (non-None required)
CHAIN-2: What is their outside-in basis? (internal knowledge or general reasoning fails — state why the basis is external)
CHAIN-3: What is the risk draft? (connected to which NORM label?)

FAIL IF: any chain item is None or unanswered. → C-19.
FAIL IF: CHAIN-2 basis is derivable from internal project knowledge. → C-19.

Phase 2 output must expand CHAIN-3. If Phase 2 risk differs from CHAIN-3 draft, you have broken the chain.

---

## STEP 7 — WRITE MINUTES

**Header**: Committee type, date, quorum met/not met, scope, escalation path.

**Decisions**: Table. One row per decision. Required columns: Decision, Outcome, Confidence, Condition.
FAIL IF: Outcome cell is blank. → C-03.
FAIL IF: Outcome is paraphrased rather than stated. → C-03.

**Action Items**: Table. Required columns: Action, Owner, Due.
DO NOT write a prose list.
FAIL IF: Owner cell is blank for any row. → C-04, C-21.
FAIL IF: open questions exist in minutes but no action item captures them. → C-04.

**Dissent**: Table. One row per participant who could plausibly dissent.
Required columns: Participant, Position, Basis, vs. Majority.
FAIL IF: a participant with grounds to dissent has no row. → C-05, C-22.
FAIL IF: all participants show "Agree" when discussion surfaced tension. → C-05.

**Pre-Mortem Risk**: Expand CHAIN-3 draft.
State the risk. State the outside-in basis (must not derive from internal knowledge). Name the NORM source.
FAIL IF: basis is circular. → C-09.
FAIL IF: risk is one the real committee would have predicted without the Challenger. → C-09.

**Charter Compliance**: Four rows: Quorum, Scope, Veto, Escalation. Honored / Not Honored / N/A.

---

## AMEND

When AMEND is invoked: inject the new participant as default. Do not treat injection as exceptional.
Add provisional annotation if charter coverage is uncertain.
Re-run Step 5 grid rows for the injected participant.

FAIL IF: you treat AMEND participants as guests rather than simulation participants. → C-11.
```

---

## V-03 — Axis: Inertia Framing
**Hypothesis**: Making the NORM inventory and Challenger designation the *first structural elements* — before committee type selection — forces outside-in framing as a prerequisite rather than an enhancement layer. The committee type then fills into an already-established inertia frame.

```markdown
# corps-committee

Simulate a committee meeting before the real one. This simulation has one structural goal above all others: surface the risk the real committee will normalize into invisibility.

Everything else — the agenda, the decisions, the minutes — follows from that.

---

## PART 0 — WHAT WILL THEY RUBBER-STAMP?

Before you select a committee type. Before you read the charter. Answer this:

> "This committee has been meeting for some time. They have prior decisions, standing assumptions, and shared defaults. What have they stopped questioning? What will they approve without challenge?"

Name at least three specific normalized beliefs. Each belief must be:
- Specific (a named assumption the committee holds, not a category)
- Observable (there is a behavior that reveals the committee holds it)
- Non-obvious (a competent external reviewer would not predict it from the spec alone)

| Label | Normalized Belief | Observable Behavior |
|-------|-------------------|---------------------|
| NORM-1 | | |
| NORM-2 | | |
| NORM-3 | | |

This inventory is the inertia frame. Every other section is built on top of it.

---

## PART 1 — DESIGNATED INERTIA CHALLENGER

From the roster (read `.roles/`), designate one participant as the Inertia Challenger:

- Their role frame must be least likely to hold the normalized assumption.
- State explicitly why: what about their charter puts them outside the inertia?
- Assign them a NORM label obligation: they must challenge at least one NORM item by label during simulation.

| Field | Value |
|-------|-------|
| Designated Challenger | [role] |
| Why outside-in | [specific rationale — not "they have an external perspective"] |
| NORM Obligation | NORM-* (at least one) |

If no qualifying participant exists in `.roles/`, inject a provisional Inertia-Advocate:
`[Inertia-Advocate — Candidate participant, not in standing roster. Confirmed or replaced in Phase 2.]`

This block is complete before the charter is read. It is not part of the roster. It is not a Phase 0 annotation.

---

## PART 2 — COMMITTEE TYPE AND CHARTER

Now select the committee type and read the charter.

**Type**:
- ROB → produces a product/service review verdict. Must cite metrics. Must show feature readiness evidence.
- Shiproom → produces a go/no-go decision. Must include a blocking issues register.
- Arch-board → produces an ADR. Must name architectural trade-offs explicitly.

**Charter Constraints** (from `.roles/`):

State these as Phase 1 entry conditions:

| Constraint | Value | Charter Source |
|------------|-------|----------------|
| Quorum | | |
| Scope | | |
| Escalation Path | | |
| Veto Authority | | |

**Roster**:

| # | Participant | Role | Charter Function | NORM Obligation | Provisional? |
|---|-------------|------|------------------|-----------------|--------------|
| 1 | | | | None / NORM-* | No / Candidate |

---

## PART 3 — SIMULATION (Inertia-First Sequencing)

Run simulation in this order, because this order maximizes inertia challenge before consensus solidifies:

1. **Inertia Challenger** — challenges NORM item(s) by label. States the outside-in risk.
2. **Dissent-likely roles** — roles whose charter creates structural tension with the majority.
3. **Domain experts** — raise evidence relevant to committee type.
4. **Charter holder** — states the scope and escalation constraints.

For each participant, the NORM challenge column is non-optional for the Challenger. All others may challenge or state None.

| Participant | Primary Concern | Evidence | NORM Challenge | Role Consistent? |
|-------------|-----------------|----------|----------------|-----------------|
| [Challenger] | | | NORM-* (required) | Yes |
| [Other] | | | NORM-* or None | Yes / No |

Role consistent = the concern matches the charter function. A PM does not own deployment topology. An SRE does not own product vision.

---

## PART 4 — PRE-MORTEM CHAIN CHECK

Before writing minutes:

| Checkpoint | Requirement | Met? |
|------------|-------------|------|
| CHAIN-1 | Challenger is a non-None participant | |
| CHAIN-2 | Outside-in basis does not derive from internal knowledge — state the external frame explicitly | |
| CHAIN-3 | Risk draft connected to a named NORM label | |

CHAIN-3 is the seed of the Phase 2 pre-mortem risk. Phase 2 expands it — it does not replace it.

---

## PART 5 — MINUTES OUTPUT

**Header**: Committee type, date, quorum met/not met, scope, escalation path.

**Discussion Summary**: Per agenda item. Include type-specific evidence (ROB: metrics; Shiproom: blocking issues; Arch-board: trade-offs).

**Decisions**:

| # | Decision | Outcome | Confidence | Condition |
|---|----------|---------|------------|-----------|
| | | Approved / Rejected / Deferred / Conditional | | |

**Action Items** (Owner column required — empty owner = structural fail):

| # | Action | Owner | Due |
|---|--------|-------|-----|

**Dissent** (one row per participant with grounds to dissent):

| Participant | Position | Basis | vs. Majority |
|-------------|----------|-------|--------------|

**Pre-Mortem Risk** (expansion of CHAIN-3):

> *The risk the real committee will not surface because NORM-[*] has made it invisible:*

State the risk. State why the outside-in basis is non-circular. Name the NORM source.

**Charter Compliance**:

| Constraint | Honored? | Evidence |
|------------|----------|----------|
| Quorum | | |
| Scope | | |
| Veto | N/A / | |
| Escalation | N/A / | |

---

## AMEND

When AMEND adds participants: treat as default simulation participants. Apply provisional annotation if charter coverage is unconfirmed. Re-run their row in the simulation grid.

---

## ANNOTATION PROTOCOL

When a required section is missing, empty, or non-compliant, annotate the gap with the criterion it would fail:

`[MISSING OUTCOME — C-03]` `[MISSING OWNER — C-04]` `[ROLE DRIFT — C-02]` `[NO METRIC — C-07]` `[CIRCULAR INERTIA BASIS — C-09]` `[NORM LABELS TOO GENERIC — C-18]`
```

---

## V-04 — Axis: Lifecycle Emphasis
**Hypothesis**: Explicit numbered GATE blocks with checkbox completion requirements produce cleaner phase boundaries than prose phase descriptions — a model that must fill checkboxes before proceeding cannot skip charter validation or pre-mortem chain commitment.

```markdown
# corps-committee

Simulate a committee meeting before the real one.
Types: ROB | Shiproom | Arch-board
Read charters from `.roles/`. AMEND: add attendees or change scope.

This skill uses a gated lifecycle. Each gate must be complete before the next phase begins.
Gates are not suggestions. A gate with an unchecked item means the simulation cannot proceed.

---

## BEFORE YOU START

**ROB**: A meeting without a metric is not a ROB. Find one or the gate will not close.
**Shiproom**: A meeting without a go/no-go verdict is not a shiproom. Block until it resolves.
**Arch-board**: A meeting without named trade-offs is not an arch-board. Name them before continuing.

---

## ◆ GATE 0-A — Challenger Commitment

Complete this gate before reading the charter or building the roster.

```
[ ] Designated Inertia Challenger: [role name from .roles/]
[ ] Outside-in rationale: [why this role's frame is least likely to hold the normalized assumption]
[ ] NORM obligation: [which NORM labels this role must challenge in Phase 1]
[ ] If no qualifying participant: [Inertia-Advocate — Candidate, confirmed or replaced in Phase 2]
```

**Gate 0-A pass condition**: All four items complete. Challenger role is named, rationale is specific (not "external perspective"), NORM obligation is pre-assigned.

This gate produces a standalone block. It is not embedded in the roster.

---

## ◆ GATE 0-B — NORM Inventory

Complete before charter constraints are stated.

```
[ ] NORM-1: [specific normalized belief] — Observable: [behavior]
[ ] NORM-2: [specific normalized belief] — Observable: [behavior]
[ ] NORM-3: [specific normalized belief] — Observable: [behavior]
```

**Gate 0-B pass condition**: Three or more NORM items. Each has a named belief (not a category) and an observable behavior. Category headings do not close this gate.

---

## ◆ GATE 0-C — Charter Validation

State these as entry conditions before any simulation begins.

```
[ ] Committee type: ROB / Shiproom / Arch-board
[ ] Quorum threshold: [n required / n present — Met / Not Met]
[ ] Scope: [in scope / out of scope boundary]
[ ] Escalation path: [where blocked decisions go]
[ ] Veto authority: [role / N/A]
```

**Gate 0-C pass condition**: All five items complete. No TBD entries permitted — a TBD is an open gate.

---

## ◆ GATE 0-D — Roster Completion

```
[ ] All participants listed with role and charter function
[ ] Designated Challenger marked in roster
[ ] NORM obligation assigned per participant (None permitted for non-Challengers)
[ ] Provisional annotation applied to any participant lacking confirmed charter coverage
```

**Gate 0-D pass condition**: No participant has an empty charter function. No provisional participant lacks a forward-reference annotation.
If no charter participant covers a required function: inject a Candidate. Do not assert coverage.

---

## Phase 1 — Simulation

Gates 0-A through 0-D must all be complete. Do not begin Phase 1 until they are.

Run participants in sequence: Inertia Challenger → dissent-likely → domain experts → charter holder.

For each participant, produce one row:

| Participant | Role Frame | Concern | Evidence | NORM Challenge | Consistent? |
|-------------|------------|---------|----------|----------------|-------------|
| [Challenger] | | | | NORM-* required | |
| [Other] | | | | NORM-* or None | |

Role consistent: concern matches charter function. PM primary ≠ deployment topology. SRE primary ≠ product vision.

---

## ◆ GATE 1→2 — PRE-MORTEM CHAIN CHECK

Do not begin Phase 2 until all three checkpoints are complete.

```
[ ] CHAIN-1: Challenger is identified — [name the participant role here]
[ ] CHAIN-2: Outside-in basis is stated — [state it here. Derivation from internal knowledge fails. State why the basis is external.]
[ ] CHAIN-3: Risk draft — [state the risk here. Name the NORM label it connects to.]
```

**Gate 1→2 pass condition**: All three items complete, non-None, non-circular.

Phase 2 pre-mortem must expand CHAIN-3. It may not contradict it. Contradiction = gate retroactively fails.

---

## Phase 2 — Minutes Output

**Header**: Committee type | Date | Quorum | Scope | Escalation path

**Discussion Summary** (one item per agenda topic):
- ROB: include metric evidence per item.
- Shiproom: include blocking issues register.
- Arch-board: include trade-off table per item.

**Decisions Table**:

| # | Decision | Outcome | Confidence | Condition |
|---|----------|---------|------------|-----------|

Approved / Rejected / Deferred / Conditional. Empty Outcome = `[MISSING OUTCOME — C-03]`.

**Action Items Table**:

| # | Action | Owner | Due |
|---|--------|-------|-----|

Owner is a required column. Empty Owner = `[MISSING OWNER — C-04]`.

**Dissent Table**:

| Participant | Position | Basis | vs. Majority |
|-------------|----------|-------|--------------|

One row per participant with grounds to dissent. Missing row = `[MISSING DISSENT ROW — C-05]`.

**Pre-Mortem Risk** (CHAIN-3 expansion):

| Risk | Outside-In Basis | NORM Source | Consequence |
|------|-----------------|-------------|-------------|

Circular basis = `[CIRCULAR BASIS — C-09]`. Risk predictable by internal reviewer = `[NOT OUTSIDE-IN — C-09]`.

**Charter Compliance**:

| Constraint | Honored? | Evidence |
|------------|----------|----------|
| Quorum | | |
| Scope | | |
| Veto | | |
| Escalation | | |

---

## ◆ GATE 2 — Output Completeness Check

```
[ ] Decisions table present with at least one non-empty Outcome cell
[ ] Action items table present with all Owner cells non-empty
[ ] Dissent table present with rows for all plausible dissenters
[ ] Pre-mortem risk traces to a NORM label
[ ] Charter compliance table complete
```

Gate 2 fail = annotate the missing element with its criterion ID and surface it to the user.

---

## AMEND

When AMEND is invoked: treat injected participants as default, not exceptional. Apply Gate 0-D checks to new participants. Add provisional annotation if charter coverage is unconfirmed. Re-run their Phase 1 row.
```

---

## V-05 — Combined Axes: Role Sequence + Output Format + Lifecycle Emphasis
**Hypothesis**: The combination of (1) challenger-first role sequencing, (2) per-criterion columnar output for every structured section, and (3) explicit gate-syntax lifecycle produces the highest rubric coverage — each structural element enforces a specific criterion, and the combination leaves no compliance gap coverable by prose.

```markdown
# corps-committee

Simulate a committee meeting before the real one.
Types: ROB (product/service review) | Shiproom (go/no-go) | Arch-board (architecture decision review)
Charters: `.roles/`. AMEND: add attendees or change scope.

---

## BEFORE YOU START — TYPE-SPECIFIC OBLIGATIONS

Read this block before generating any output. Each type has one obligation that, if unmet, means you have not run that committee.

| Type | Obligation | Structural Fail Condition |
|------|------------|--------------------------|
| ROB | Cite at least one metric or readiness signal | No metric present in discussion → FAILS C-07 |
| Shiproom | State a go/no-go verdict and a blocking issues list | No verdict or no blocking list → FAILS C-03, C-07 |
| Arch-board | Name ≥2 trade-offs and produce an ADR title | No named trade-offs → FAILS C-07 |

---

## ┌ CHALLENGER BLOCK ┐
## Rendered first — before roster construction — standalone

| Field | Value |
|-------|-------|
| Designated Inertia Challenger | [role from `.roles/`] |
| Outside-in rationale | [specific: what about this role's charter puts them outside the committee's normalized frame] |
| NORM Obligation | [NORM labels this role must challenge by name in Phase 1] |
| If no qualifying participant | `[Inertia-Advocate — Candidate, not in standing roster. Confirmed or replaced in Phase 2.]` |

This block is complete before Phase 0. It is not a row in the roster. It does not share space with charter constraints.

## └─────────────────┘

---

## ◆ GATE 0-A — NORM Inventory
> Does not open until Challenger Block is complete.

Decompose the inertia hypothesis into named, independently citable beliefs:

| Label | Normalized Belief (specific — not a category) | Observable Behavior (how you detect the committee holds it) | Challenger Assigned |
|-------|-----------------------------------------------|-------------------------------------------------------------|---------------------|
| NORM-1 | | | [Designated Challenger role] |
| NORM-2 | | | |
| NORM-3 | | | |

Gate 0-A pass: ≥3 rows, each with a specific belief and observable behavior. Category headings fail.

---

## ◆ GATE 0-B — Charter Constraints
> Entry conditions for Phase 1. Must be complete before simulation begins.

| Constraint | Value | Source Clause |
|------------|-------|---------------|
| Committee Type | ROB / Shiproom / Arch-board | |
| Quorum | [required / present — Met / Not Met] | |
| Scope | [in / out boundary] | |
| Escalation | [path] | |
| Veto Authority | [role / N/A] | |

Gate 0-B pass: all cells non-empty, no TBD.

---

## ◆ GATE 0-C — Roster
> Injection is default. Do not assert charter coverage without basis.

| # | Participant | Role | Charter Function | NORM Obligation | Provisional? |
|---|-------------|------|------------------|-----------------|--------------|
| 1 | [Designated Challenger] | | | NORM-* (required) | No |
| 2 | [Dissent-likely role] | | | NORM-* or None | |
| … | [Domain experts] | | | None | |
| n | [Charter holder] | | | None | |

Provisional annotation for unconfirmed coverage: `[Candidate — confirmed or replaced in Phase 2]`.

Gate 0-C pass: no empty Charter Function cells, no unconfirmed participants without provisional annotation.

---

## Phase 1 — Simulation
> Gates 0-A, 0-B, 0-C must all be complete.

**Role Sequence Rationale**: Challenger speaks first to establish the inertia frame before consensus forms. Dissent-likely roles follow while tension is active. Domain experts contextualize. Charter holder closes — their scope constraint lands on a fully formed discussion.

**Per-Participant Grid** (every cell required):

| # | Participant | Role Frame | Primary Concern | Evidence Cited | Inertia Challenge? | Role-Consistent? |
|---|-------------|------------|-----------------|----------------|-------------------|------------------|
| 1 | [Challenger] | [charter frame] | [concern] | [metric/spec/clause] | NORM-* (required non-None) | Yes |
| 2 | [Dissent role] | | | | NORM-* or None | Yes / FAILS C-02 |
| 3 | [Expert] | | | | NORM-* or None | Yes / FAILS C-02 |
| n | [Charter holder] | | | | None | Yes |

Role-Consistent check:
- PM primary ≠ deployment topology → FAILS C-02
- SRE primary ≠ product vision → FAILS C-02
- Any role concern outside charter function → FAILS C-02

---

## ◆ GATE 1→2 — PRE-MORTEM CHAIN CHECK
> Phase 2 does not begin until all three are complete and non-circular.

| Checkpoint | Requirement | Status | Value |
|------------|-------------|--------|-------|
| CHAIN-1 | Challenger identified — non-None | [ ] | [role] |
| CHAIN-2 | Outside-in basis stated — external frame, not derivable from internal knowledge | [ ] | [state why it is external] |
| CHAIN-3 | Risk draft connected to a NORM label | [ ] | [risk draft + NORM-*] |

Gate 1→2 pass: all three complete. CHAIN-2 with internal derivation = gate does not close.

Phase 2 pre-mortem expands CHAIN-3. Inconsistency = retroactive gate failure.

---

## Phase 2 — Minutes Output

**Header Table**:

| Field | Value |
|-------|-------|
| Committee | [type] |
| Date | |
| Quorum | [Met / Not Met — n/N] |
| Scope | |
| Escalation | |

**Agenda Summary** (one row per item, type-specific evidence required):

| # | Item | Summary | Type Evidence |
|---|------|---------|---------------|
| 1 | | | [ROB: metric | Shiproom: blocking issue | Arch-board: trade-off] |

**Decisions Table**:

| # | Decision | Outcome | Confidence | Condition |
|---|----------|---------|------------|-----------|
| | | Approved / Rejected / Deferred / Conditional | High / Med / Low | |

Empty Outcome cell → annotate `[MISSING OUTCOME — C-03]`.

**Action Items Table** (Owner is a structural required column):

| # | Action | Owner | Due |
|---|--------|-------|-----|
| | | [named person or role — not a team label] | |

Empty Owner cell → annotate `[MISSING OWNER — C-04, C-21]`.

**Dissent Table** (one row per participant with grounds to dissent — omission is structurally visible):

| Participant | Position | Basis | vs. Majority |
|-------------|----------|-------|--------------|
| | Agree / Dissent / Conditional | | Aligned / Opposed / Conditional |

Missing row for a participant with grounds to dissent → annotate `[MISSING DISSENT ROW — C-05, C-22]`.

**Pre-Mortem Risk** (CHAIN-3 expansion):

| Risk | Outside-In Basis | NORM Source | Likelihood if Normalized |
|------|-----------------|-------------|--------------------------|
| [from CHAIN-3] | [external frame — not derivable from internal knowledge or general reasoning] | NORM-* | |

Circular basis → `[CIRCULAR BASIS — C-09]`. Risk predictable by a competent internal reviewer → `[NOT OUTSIDE-IN — C-09]`.

**Charter Compliance**:

| Constraint | Honored? | Evidence |
|------------|----------|----------|
| Quorum | Yes / No | |
| Scope | Yes / No | |
| Veto | Yes / No / N/A | |
| Escalation | Yes / No / N/A | |

---

## ◆ GATE 2 — Output Completeness
```
[ ] Decisions table: at least one Outcome cell non-empty
[ ] Action items table: all Owner cells non-empty
[ ] Dissent table: row present for every participant with grounds to dissent
[ ] Pre-mortem risk: non-circular outside-in basis, NORM label cited
[ ] Charter compliance: all four rows complete
```

Gate 2 fail → annotate the gap with its criterion ID and surface it.

---

## AMEND Protocol

AMEND participants are default simulation participants — not guests.
Apply GATE 0-C checks to injected roles.
Add provisional annotation if charter coverage unconfirmed.
Re-run Phase 1 grid row for each injected participant.
FAILS: asserting coverage without charter evidence → C-11.

---

## Fill-Rule Annotation Key

| Annotation | Criterion |
|------------|-----------|
| `[MISSING OUTCOME]` | C-03 |
| `[MISSING OWNER]` | C-04, C-21 |
| `[ROLE DRIFT]` | C-02 |
| `[MISSING DISSENT ROW]` | C-05, C-22 |
| `[NO METRIC]` | C-07 |
| `[NO TRADE-OFFS]` | C-07 |
| `[CIRCULAR BASIS]` | C-09 |
| `[NOT OUTSIDE-IN]` | C-09 |
| `[NORM TOO GENERIC]` | C-18 |
| `[COVERAGE ASSERTED WITHOUT BASIS]` | C-11 |
| `[PROVISIONAL ANNOTATION MISSING]` | C-12 |
```

---

## Variation Summary

| # | Axis | Hypothesis | Key Structural Bet |
|---|------|------------|--------------------|
| V-01 | Output format | Column grids catch violations at scan time | Every section is a table with criterion-mapped columns; prose is eliminated from structured sections |
| V-02 | Phrasing register | FAIL conditions after every instruction are treated as hard stops | Direct imperative voice + "FAIL IF" after each rule; model cannot soften enforcement through prose framing |
| V-03 | Inertia framing | NORM inventory before type selection forces outside-in as prerequisite | Section 1 is the NORM inventory — committee type slots into an already-established inertia frame |
| V-04 | Lifecycle emphasis | Gate checkboxes produce cleaner phase boundaries than prose phases | Five named gates (0-A, 0-B, 0-C, 0-D, 1→2, 2) with explicit checkbox completion requirements |
| V-05 | Combined (sequence + format + lifecycle) | Each structural element enforces a specific criterion; combination leaves no prose-coverable gap | Challenger block standalone first; role sequence by challenge angle; columnar output; gate syntax; NORM inventory in Phase 0 |
