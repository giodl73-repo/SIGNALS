# draft-proposal — Rubric v9 — Round 9 Variations

Generated: 2026-03-15
Rubric: v9 (C-01 through C-33, denominator /26)
New criteria targeted this round: C-32 (field-level role enforcement in option anatomy), C-33 (Phase 0 causal contract declaration)

---

## Variation Design Summary

| Var | Axis | Primary New Criteria | Hypothesis |
|-----|------|----------------------|------------|
| V-01 | Option anatomy field-level role enforcement | C-32 | Declaring `PM FRAMING:` and `ARCHITECT VALIDATION:` as typed slots in a Phase 0 option anatomy contract makes C-32 a structural initialization requirement rather than an option-authoring habit |
| V-02 | Phase 0 causal contract declaration | C-33 | Declaring the formula `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME` as a Phase 0 typed initialization contract with source phase attribution and T-GUARD routing converts inertia chain verification from retroactive scan to prospective enforcement |
| V-03 | Phrasing register — strict imperative contract language | structural reinforcement for C-32, C-33 | Shifting all phase instructions to SHALL/MUST/PROHIBITED register makes typed-slot omissions structurally feel like contract violations, reinforcing the enforcement discipline that C-32 and C-33 require |
| V-04 | C-32 + C-33 combined | C-32 + C-33 | Both new aspirational criteria are orthogonal additions — option anatomy contract and causal chain contract can coexist in Phase 0 without interference; combining them tests composability |
| V-05 | All six axes: C-28 through C-33 | C-28 + C-29 + C-30 + C-31 + C-32 + C-33 | A prompt incorporating all six axes — PM-first, table-dominant, phase manifest, DECISION LEAD TIME chain, option anatomy contract, and Phase 0 causal contract — should score 100.0 under v9 |

---

## V-01 — Option Anatomy Field-Level Role Enforcement (C-32)

**Variation axis:** Option anatomy — `PM FRAMING:` and `ARCHITECT VALIDATION:` declared as required typed slots in a Phase 0 option anatomy contract. Every option in Phase 4 inherits the contract. Phase 12 sign-off blocks carry the same typed slots as a third enforcement point.

**Hypothesis:** Declaring the option anatomy template at Phase 0 initialization — before any option is authored — makes C-32 a structural requirement rather than an authoring convention. The three enforcement points (template declaration at Phase 0, option body at Phase 4, sign-off at Phase 12) create independent verifiable traces. A reviewer confirms C-32 by reading the Phase 0 contract alone; no option scan required for template compliance.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). Both roles contribute distinct perspectives. Dual-role phases carry typed
role slots to enforce contribution independence.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize two artifacts before any content is authored. Both are live from this point.

── OPTION ANATOMY CONTRACT ──────────────────────────────────────────────
This contract governs every option entry in Phase 4 and every sign-off block in Phase 12.

Required typed slots in every option anatomy entry (Option 0 through Option N):

  DESCRIPTION:         [what this option does]
  PM FRAMING:          [business rationale, adoption path, key trade-offs — PM speaks]
  ARCHITECT VALIDATION:[technical feasibility, dependencies, constraints — responds to PM]
  PROS:                [bulleted list]
  CONS:                [bulleted list]
  RISK:                P: [1-5] x I: [1-5] = P*I: [score] — [description]
  EFFORT:              Timeline: [named sprint or milestone] | Team: [named role] | Dependencies: [any]

  [Option 0 (do-nothing) only:]
  INERTIA COST:        P: [1-5] x I: [1-5] = P*I: [score] per sprint

  [Each non-do-nothing option:]
  INERTIA OFFSET:      Sprint [N] — crossover sprint where cumulative implementation cost
                       equals cumulative INERTIA COST of not acting
  DECISION LEAD TIME:  [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
  ESCALATION FLAG:     [Required when DECISION LEAD TIME <= 0 — name the trap and escalation authority]

CONTRACT ENFORCEMENT: If PM FRAMING: or ARCHITECT VALIDATION: is absent from any option
anatomy entry, fire T-25. If either slot is absent from any Phase 12 sign-off block,
fire T-25. T-GUARD catches any other missing required typed slot not covered by a
numbered trigger.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────────
COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1 — sentinel-first ordering required):

| ID      | Scope    | Predicate — trigger fires when this condition is true                           |
|---------|----------|---------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document    |
| T-01    | Phase 1  | Scout artifact inventory absent or merged into another phase                    |
| T-02    | Phase 2  | TEMPORAL ANCHOR missing or contains vague language (soon, near term, etc.)      |
| T-03    | Phase 2  | INACTION CONSEQUENCE missing or uses missed-feature language                    |
| T-04    | Phase 3  | P*I scoring anchors not defined before any risk entry is scored                 |
| T-05    | Phase 4  | Fewer than 3 options, or do-nothing option absent                               |
| T-06    | Phase 4  | Any option missing a required anatomy field from the Phase 0 contract           |
| T-07    | Phase 4  | Do-nothing option missing typed INERTIA COST in P*I format                     |
| T-08    | Phase 4  | Any non-do-nothing alternative missing typed INERTIA OFFSET                    |
| T-09    | Phase 4  | Any non-do-nothing alternative missing typed DECISION LEAD TIME                 |
| T-10    | Phase 4  | Alternative with non-positive DECISION LEAD TIME missing typed ESCALATION FLAG  |
| T-11    | Phase 5  | PM perspective phase absent or merged with Architect                            |
| T-12    | Phase 6  | Architect perspective phase absent or merged with PM                            |
| T-13    | Phase 7  | Comparison table absent or dimensions inconsistent across options               |
| T-14    | Phase 8  | Assumption register absent, fewer than 2 A-NN entries, or not in table format  |
| T-15    | Phase 9  | Risk register absent, fewer than 2 R-NN entries, or not in table format        |
| T-16    | Phase 10 | Failure mode register absent, fewer than 2 F-NN entries, or not in table format|
| T-17    | Phase 11 | Assumption or risk register appears after recommendation phase                  |
| T-18    | Phase 11 | PREREQUISITE GATE block absent                                                  |
| T-19    | Phase 12 | PM sign-off block is not position 1 in the recommendation sign-off section     |
| T-20    | Phase 12 | PM sign-off block missing typed F-ROW ANCHOR slot                              |
| T-21    | Phase 12 | Architect sign-off block missing typed F-ROW ANCHOR slot                       |
| T-22    | Phase 12 | Recommendation CONDITIONS reference no F-NN ID                                 |
| T-23    | Phase 13 | OWNER typed slot absent from any amend entry category template                  |
| T-24    | Phase 13 | DEADLINE typed slot absent from any amend entry category template               |
| T-25    | Phase 4,12| PM FRAMING: or ARCHITECT VALIDATION: typed slot absent from any option entry
              or any sign-off block — option anatomy contract violation                  |

Amendment Rows (populated live — empty rows confirm T-GUARD enforcement):

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY
════════════════════════════════════════════

Inventory all scout artifacts available for this topic before any option is authored.
State what was found and what is absent. If no artifacts exist, state this explicitly
and substitute an inline assessment.

| Namespace          | Artifact Found? | Finding or Absence Note                                     |
|--------------------|-----------------|--------------------------------------------------------------|
| scout-feasibility  | yes / no        | [artifact name and key finding, or "absent — inline below"] |
| scout-requirements | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-market       | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-stakeholders | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-compliance   | yes / no        | [artifact name and key finding, or "absent"]                 |

If absent: INLINE ASSESSMENT: [feasibility, requirements, and constraints as direct assessment]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING
════════════════════════════════════════════

DECISION QUESTION: [the precise question being decided — one sentence]

TEMPORAL ANCHOR: [specific named date, sprint name, or event — vague language such as
"soon," "before it is too late," or "in the near term" is prohibited; use a named
specific deadline]

INACTION CONSEQUENCE: [a concrete named outcome if the decision is not made by
TEMPORAL ANCHOR — teams blocked, capability lost, or window closed. Missed-feature
statements do not qualify. Name the specific team or capability affected.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

Define project-specific anchors before any option is scored. These anchors apply to
the risk register (Phase 9) and all INERTIA COST calculations (Phase 4).

| P | Meaning for this project |
|---|--------------------------|
| 1 | [define P=1]             |
| 2 | [define P=2]             |
| 3 | [define P=3]             |
| 4 | [define P=4]             |
| 5 | [define P=5]             |

| I | Meaning for this project |
|---|--------------------------|
| 1 | [define I=1]             |
| 2 | [define I=2]             |
| 3 | [define I=3]             |
| 4 | [define I=4]             |
| 5 | [define I=5]             |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING
════════════════════════════════════════════

Minimum 3 options. Option 0 must be the do-nothing or status-quo option. Author each
option using the Phase 0 option anatomy contract exactly. PM FRAMING: and
ARCHITECT VALIDATION: are required typed slots in every entry — absence fires T-25.

─────────────────────────────────────────
OPTION 0: [Do-Nothing / Status Quo]
─────────────────────────────────────────
DESCRIPTION: [what the current state continues to be]

PM FRAMING: [why this is a legitimate business choice to consider; what it preserves
  and what it forfeits; adoption implications of inaction]
ARCHITECT VALIDATION: [technical assessment of the status quo; what accrues as debt;
  what constraints it avoids — responds to PM framing]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [risk of continuing status quo]
EFFORT: Timeline: N/A | Team: N/A | Dependencies: N/A

INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint
  (Per-sprint cost of inaction scored on Phase 3 P*I scale)
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 1: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, key trade-offs — PM speaks]
ARCHITECT VALIDATION: [technical feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [risk description using Phase 3 anchors]
EFFORT: Timeline: [named sprint or milestone] | Team: [named role or team] | Dependencies: [any]

INERTIA OFFSET: Sprint [N] — the sprint at which cumulative implementation cost equals
  cumulative INERTIA COST of not acting. Acting by this sprint is cost-neutral vs. do-nothing.
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint number] - [INERTIA OFFSET sprint number] = [N] sprints
  (Positive = lead time available. Zero or negative = inertia trap; see ESCALATION FLAG.)
ESCALATION FLAG: [Required only when DECISION LEAD TIME <= 0 — state the inertia trap
  condition and name the authority to whom this must be escalated immediately.]
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 2: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, key trade-offs — PM speaks]
ARCHITECT VALIDATION: [technical feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [risk description]
EFFORT: Timeline: [named sprint or milestone] | Team: [named role or team] | Dependencies: [any]

INERTIA OFFSET: Sprint [N]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0]
─────────────────────────────────────────

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE
════════════════════════════════════════════

PM provides a standalone business and adoption assessment independent of Architect.

PM RECOMMENDATION SIGNAL: [PM preferred option based on business factors alone]
PM TRADE-OFF ANALYSIS: [for each non-trivial option, name the business condition under
  which it would be the right choice]
ADOPTION CONCERN: [primary adoption barrier for the PM-preferred option]
BUSINESS RISK: [the business condition that would most directly invalidate PM's signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE
════════════════════════════════════════════

Architect provides a standalone technical constraint and feasibility assessment,
explicitly responding to the PM perspective from Phase 5.

ARCHITECT VALIDATION: [confirms or challenges PM recommendation signal from a technical
  standpoint — must reference PM's signal, not produce an independent proposal]
TECHNICAL CONSTRAINT: [the primary technical constraint that bounds option selection]
DEPENDENCY NOTE: [blocking dependency for the architecturally preferred option]
TECHNICAL RISK: [the technical condition that would most directly invalidate Architect's
  validation of the PM-preferred option]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

Compare all options across consistent dimensions. Every option appears in every row.

| Dimension           | Option 0 (Do-Nothing) | Option 1: [Name] | Option 2: [Name] | [Option N] |
|---------------------|-----------------------|------------------|------------------|------------|
| PM Signal           |                       |                  |                  |            |
| Architect Signal    |                       |                  |                  |            |
| Effort              |                       |                  |                  |            |
| Timeline            |                       |                  |                  |            |
| Risk P*I            |                       |                  |                  |            |
| Adoption Friction   |                       |                  |                  |            |
| Control             |                       |                  |                  |            |
| INERTIA COST/sprint | [P*I value]           | N/A              | N/A              | N/A        |
| INERTIA OFFSET      | N/A                   | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME  | N/A                   | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

Document assumptions that, if invalidated, would change the recommendation.
Minimum 2 entries. Table format required.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 | [assumption text] | [how and when — method and sprint] |
| A-02 | [assumption text] | [validation method and sprint]     |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

Document risks using the numeric P*I scoring defined in Phase 3.
Minimum 2 entries. Table format required.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 | [risk description] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |
| R-02 | [risk description] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

Document failure modes distinct from the risk register.
Minimum 2 entries. Canonical field labels required — synonyms are not acceptable.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|--------------|-------------------|------------|
| F-01 | [failure mode description] | [trigger condition] | [mitigation or escalation path] |
| F-02 | [failure mode description] | [trigger condition] | [mitigation] |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

Confirm completeness before proceeding. Binary: COMPLETE or NOT COMPLETE.
If any item is NOT COMPLETE, fire the corresponding trigger before proceeding.

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ A-NN entries, table format              | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ R-NN entries, table format, numeric P*I       | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ F-NN entries, canonical labels        | COMPLETE / NOT COMPLETE |
| 4 | Both registers appear before this gate in document sequence     | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST present on do-nothing option using Phase 3 P*I scale | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative carries typed INERTIA OFFSET           | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives carry typed DECISION LEAD TIME  | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME <= 0 alternatives carry ESCALATION FLAG  | COMPLETE / NOT COMPLETE |
| 9 | PM FRAMING: and ARCHITECT VALIDATION: present in every option   | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this option wins — reference Phase 7 comparison dimensions, Phase 5 PM
  signal, and Phase 6 Architect validation]
CONDITIONS: [2-3 specific conditions that must hold. Reference at least one F-row by ID.]

── PM SIGN-OFF (position 1 — first signatory) ──────────────────────────
ROLE: PM
PM FRAMING: [PM confirms this is the right business decision; expected value of acting
  exceeds INERTIA COST of not acting; adoption path is viable]
ARCHITECT VALIDATION: [PM's expectation of what Architect must confirm for this decision
  to stand — sets the validation frame the Architect sign-off must respond to]
CONDITIONS: [PM conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2 — second signatory) ──────────────────
ROLE: Architect
PM FRAMING: [Architect's acknowledgment of the business decision PM has established —
  confirms Architect is responding to PM's frame, not issuing an independent proposal]
ARCHITECT VALIDATION: [Architect confirms technical soundness of the recommended option
  given PM's decision. States the binding technical precondition.]
CONDITIONS: [Architect conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

All three categories required. OWNER and DEADLINE are typed slots in every entry.

── MISSING OPTION ───────────────────────────────────────────────────────
OPTION: [an option not explored in this proposal]
REASON NOT EXPLORED: [why it was excluded]
OWNER: [named role or person responsible for evaluating this option]
DEADLINE: [specific sprint name, named date, or named milestone — "TBD" and "soon"
  are not acceptable values]

── UNWEIGHTED CRITERION ─────────────────────────────────────────────────
CRITERION: [a decision dimension that was not weighted or was equally weighted]
RECALIBRATION NOTE: [why this criterion deserves different weighting in the next version]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ─────────────────────────────────────────────────────────────
ACTION: [specific follow-up action required before or after implementation]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

Review the amendment tracking table initialized in Phase 0. Confirm all open triggers.

If the amendment table contains no rows:
  COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.

If the amendment table contains rows:
  COMPLETION STATUS: [N] amendments logged — see rows above.

Update the COMPLETION STATUS field in Phase 0 to its terminal value now.
```

---

## V-02 — Phase 0 Causal Contract Declaration (C-33)

**Variation axis:** Phase 0 initialization — the formula `TEMPORAL ANCHOR - INERTIA OFFSET = DECISION LEAD TIME` is declared as a typed causal chain contract at Phase 0, with source phase attribution for each term and an explicit T-GUARD routing rule. No phase that contributes a term to the formula executes before the contract is declared.

**Hypothesis:** Declaring the causal chain formula at Phase 0 converts inertia chain verification from retroactive trace (reviewer scans Phase 2, Phase 4, then verifies the subtraction is present) to prospective enforcement (contract is visible at document open; each term's source phase is named; T-GUARD routing is pre-wired). A document authored under this prompt either satisfies the contract or fires a numbered trigger — there is no ambiguous middle state.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). Contributions are distinct.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize two artifacts before any content is authored. Both are live from this point.

── CAUSAL CHAIN CONTRACT ─────────────────────────────────────────────────

This document's urgency chain is governed by the following formula. This contract is
declared before any term-contributing phase executes.

  TEMPORAL ANCHOR - INERTIA OFFSET = DECISION LEAD TIME

Term source attribution:
  TEMPORAL ANCHOR:    contributed by Phase 2 (TEMPORAL ANCHOR field)
  INERTIA OFFSET:     contributed by Phase 4 (INERTIA OFFSET field on each non-do-nothing option)
  DECISION LEAD TIME: computed per option in Phase 4; surfaced in Phase 7 comparison table

T-GUARD routing:
  - If TEMPORAL ANCHOR is absent or vague in Phase 2, fire T-02. The formula cannot be
    evaluated; all DECISION LEAD TIME values in Phase 4 are invalid.
  - If INERTIA OFFSET is absent from any non-do-nothing option in Phase 4, fire T-08.
    The formula is incomplete for that option.
  - If DECISION LEAD TIME is absent from any non-do-nothing option in Phase 4, fire T-09.
    The formula result was not recorded.
  - If DECISION LEAD TIME <= 0 for any option and ESCALATION FLAG is absent, fire T-10.
  - If this causal chain contract block is absent from Phase 0, fire T-GUARD immediately.

Contract enforcement: This block is the single source of truth for the causal chain.
Reviewers verify C-33 compliance by reading this block — no phase scan required.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────────
COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1 — sentinel-first ordering required):

| ID      | Scope    | Predicate — trigger fires when this condition is true                           |
|---------|----------|---------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document    |
| T-01    | Phase 1  | Scout artifact inventory absent or merged into another phase                    |
| T-02    | Phase 2  | TEMPORAL ANCHOR missing or contains vague language (soon, near term, etc.)      |
|         |          | [CAUSAL CHAIN CONTRACT: if T-02 fires, all DECISION LEAD TIME values invalid]  |
| T-03    | Phase 2  | INACTION CONSEQUENCE missing or uses missed-feature language                    |
| T-04    | Phase 3  | P*I scoring anchors not defined before any risk entry is scored                 |
| T-05    | Phase 4  | Fewer than 3 options or do-nothing option absent                                |
| T-06    | Phase 4  | Any option missing a required anatomy field                                     |
| T-07    | Phase 4  | Do-nothing option missing typed INERTIA COST in P*I format                     |
| T-08    | Phase 4  | Any non-do-nothing alternative missing typed INERTIA OFFSET                    |
|         |          | [CAUSAL CHAIN CONTRACT: formula incomplete for that option]                     |
| T-09    | Phase 4  | Any non-do-nothing alternative missing typed DECISION LEAD TIME                 |
|         |          | [CAUSAL CHAIN CONTRACT: formula result not recorded for that option]            |
| T-10    | Phase 4  | Alternative with non-positive DECISION LEAD TIME missing typed ESCALATION FLAG  |
| T-11    | Phase 5  | PM perspective phase absent or merged with Architect                            |
| T-12    | Phase 6  | Architect perspective phase absent or merged with PM                            |
| T-13    | Phase 7  | Comparison table absent or dimensions inconsistent across options               |
| T-14    | Phase 8  | Assumption register absent, fewer than 2 A-NN entries, or not in table format  |
| T-15    | Phase 9  | Risk register absent, fewer than 2 R-NN entries, or not in table format        |
| T-16    | Phase 10 | Failure mode register absent, fewer than 2 F-NN entries, or not in table format|
| T-17    | Phase 11 | Assumption or risk register appears after recommendation phase                  |
| T-18    | Phase 11 | PREREQUISITE GATE block absent                                                  |
| T-19    | Phase 12 | PM sign-off block is not position 1 in the recommendation sign-off section     |
| T-20    | Phase 12 | PM sign-off block missing typed F-ROW ANCHOR slot                              |
| T-21    | Phase 12 | Architect sign-off block missing typed F-ROW ANCHOR slot                       |
| T-22    | Phase 12 | Recommendation CONDITIONS reference no F-NN ID                                 |
| T-23    | Phase 13 | OWNER typed slot absent from any amend entry category template                  |
| T-24    | Phase 13 | DEADLINE typed slot absent from any amend entry category template               |
| T-25    | Phase 0  | Causal chain contract block absent from Phase 0 (C-33 structural violation)    |

Amendment Rows (populated live — empty rows confirm T-GUARD enforcement):

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY
════════════════════════════════════════════

Inventory all scout artifacts available for this topic before any option is authored.
State what was found and what is absent.

| Namespace          | Artifact Found? | Finding or Absence Note                                     |
|--------------------|-----------------|--------------------------------------------------------------|
| scout-feasibility  | yes / no        | [artifact name and key finding, or "absent — inline below"] |
| scout-requirements | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-market       | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-stakeholders | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-compliance   | yes / no        | [artifact name and key finding, or "absent"]                 |

If absent: INLINE ASSESSMENT: [feasibility, requirements, and constraints as direct assessment]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING
════════════════════════════════════════════

Contributes TEMPORAL ANCHOR to the Phase 0 causal chain contract.

DECISION QUESTION: [the precise question being decided — one sentence]

TEMPORAL ANCHOR: [specific named date, sprint name, or event — vague language prohibited.
  This value is the minuend in the Phase 0 formula: TEMPORAL ANCHOR - INERTIA OFFSET = DECISION LEAD TIME.]

INACTION CONSEQUENCE: [a concrete named outcome if the decision is not made by TEMPORAL
  ANCHOR — teams blocked, capability lost, or window closed. Missed-feature statements
  do not qualify. Name the specific team or capability affected.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

Define project-specific anchors before any option is scored.

| P | Meaning for this project |
|---|--------------------------|
| 1 | [define P=1]             |
| 2 | [define P=2]             |
| 3 | [define P=3]             |
| 4 | [define P=4]             |
| 5 | [define P=5]             |

| I | Meaning for this project |
|---|--------------------------|
| 1 | [define I=1]             |
| 2 | [define I=2]             |
| 3 | [define I=3]             |
| 4 | [define I=4]             |
| 5 | [define I=5]             |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING
════════════════════════════════════════════

Minimum 3 options. Option 0 must be the do-nothing or status-quo option.

Each non-do-nothing option contributes INERTIA OFFSET to the Phase 0 causal chain
contract, and records the formula result as DECISION LEAD TIME.

─────────────────────────────────────────
OPTION 0: [Do-Nothing / Status Quo]
─────────────────────────────────────────
DESCRIPTION: [what the current state continues to be]
PROS:
  - [pro 1]
  - [pro 2]
CONS:
  - [con 1]
  - [con 2]
RISK: P: [1-5] x I: [1-5] = P*I: [score] — [risk of continuing status quo]
EFFORT: Timeline: N/A | Team: N/A | Dependencies: N/A
INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 1: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]
PROS:
  - [pro 1]
  - [pro 2]
CONS:
  - [con 1]
  - [con 2]
RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description using Phase 3 anchors]
EFFORT: Timeline: [named sprint or milestone] | Team: [named role or team] | Dependencies: [any]

INERTIA OFFSET: Sprint [N] — the sprint at which cumulative implementation cost equals
  cumulative INERTIA COST of not acting. [Phase 0 causal chain contract: this is the subtrahend.]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
  [Phase 0 formula result for this option. Positive = lead time. Zero/negative = inertia trap.]
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0 — inertia trap condition and
  escalation authority]
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 2: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]
PROS:
  - [pro 1]
  - [pro 2]
CONS:
  - [con 1]
  - [con 2]
RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: [named sprint or milestone] | Team: [named role or team] | Dependencies: [any]

INERTIA OFFSET: Sprint [N] [Phase 0 causal chain contract: subtrahend]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0]
─────────────────────────────────────────

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [PM preferred option based on business factors alone]
PM TRADE-OFF ANALYSIS: [for each non-trivial option, name the business condition under
  which it would be the right choice]
ADOPTION CONCERN: [primary adoption barrier for the PM-preferred option]
BUSINESS RISK: [the business condition that would most directly invalidate PM's signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE
════════════════════════════════════════════

ARCHITECT VALIDATION: [confirms or challenges PM signal from a technical standpoint —
  must reference PM's signal, not produce an independent proposal]
TECHNICAL CONSTRAINT: [the primary technical constraint that bounds option selection]
DEPENDENCY NOTE: [blocking dependency for the architecturally preferred option]
TECHNICAL RISK: [the technical condition that would most directly invalidate Architect's
  validation of the PM-preferred option]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

DECISION LEAD TIME appears as a row to surface the Phase 0 causal chain formula results
across all options in a single view.

| Dimension           | Option 0 (Do-Nothing) | Option 1: [Name] | Option 2: [Name] | [Option N] |
|---------------------|-----------------------|------------------|------------------|------------|
| PM Signal           |                       |                  |                  |            |
| Architect Signal    |                       |                  |                  |            |
| Effort              |                       |                  |                  |            |
| Timeline            |                       |                  |                  |            |
| Risk P*I            |                       |                  |                  |            |
| Adoption Friction   |                       |                  |                  |            |
| Control             |                       |                  |                  |            |
| INERTIA COST/sprint | [P*I value]           | N/A              | N/A              | N/A        |
| INERTIA OFFSET      | N/A                   | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME  | N/A                   | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

Minimum 2 entries. Table format required.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 | [assumption text] | [method and sprint] |
| A-02 | [assumption text] | [method and sprint] |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

Minimum 2 entries. Numeric P*I using Phase 3 anchors. Table format required.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 | [risk description] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |
| R-02 | [risk description] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

Minimum 2 entries. Canonical labels required.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|--------------|-------------------|------------|
| F-01 | [failure mode] | [trigger condition] | [mitigation] |
| F-02 | [failure mode] | [trigger condition] | [mitigation] |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ A-NN entries, table format              | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ R-NN entries, table format, numeric P*I       | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ F-NN entries, canonical labels        | COMPLETE / NOT COMPLETE |
| 4 | Both registers appear before this gate                          | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST on do-nothing using Phase 3 P*I scale              | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative carries typed INERTIA OFFSET           | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives carry typed DECISION LEAD TIME  | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME <= 0 alternatives carry ESCALATION FLAG  | COMPLETE / NOT COMPLETE |
| 9 | Phase 0 causal chain contract block is present with formula,    | COMPLETE / NOT COMPLETE |
|   | source attribution, and T-GUARD routing                         |                         |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this option wins — reference Phase 7 comparison dimensions, Phase 5 PM
  signal, Phase 6 Architect validation, and the DECISION LEAD TIME values from the
  Phase 0 causal chain contract]
CONDITIONS: [2-3 specific conditions that must hold. Reference at least one F-row by ID.]

── PM SIGN-OFF (position 1 — first signatory) ──────────────────────────
ROLE: PM
STATEMENT: [PM confirms this is the right business decision and that the expected value
  of acting exceeds the INERTIA COST of not acting]
CONDITIONS: [PM conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2 — second signatory) ──────────────────
ROLE: Architect
STATEMENT: [Architect confirms technical soundness of the recommended option given PM's
  business decision]
CONDITIONS: [Architect conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

All three categories required. OWNER and DEADLINE typed slots in every entry.

── MISSING OPTION ───────────────────────────────────────────────────────
OPTION: [option not explored]
REASON NOT EXPLORED: [why excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone — not "TBD" or "soon"]

── UNWEIGHTED CRITERION ─────────────────────────────────────────────────
CRITERION: [dimension not weighted or equally weighted]
RECALIBRATION NOTE: [why different weighting is warranted]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ─────────────────────────────────────────────────────────────
ACTION: [specific follow-up action]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no amendment rows: COMPLETION STATUS: T-GUARD enforced all requirements — no violations.
If amendment rows exist: COMPLETION STATUS: [N] amendments logged — see rows above.

Update the COMPLETION STATUS field in Phase 0 to its terminal value now.
```

---

## V-03 — Phrasing Register: Strict Imperative Contract Language

**Variation axis:** Phrasing register — all phase instructions are expressed as SHALL / MUST / PROHIBITED obligations. Each typed slot is a named requirement. Omission is a named contract violation, not an oversight.

**Hypothesis:** Shifting the register from descriptive ("use the following template") to imperative contract language ("each option body SHALL contain exactly the following typed slots — omission FIRES T-GUARD") creates an obligation register that reinforces the typed-slot discipline required by C-32 and C-33 without adding new structural elements. A model that reads its instructions as binding obligations is less likely to treat typed slots as optional.

---

```
You are executing the `draft-proposal` skill. You SHALL author a complete proposal or
ADR for the requested topic. Execution of this skill is a contract. Deviation from any
SHALL or MUST requirement fires T-GUARD or a numbered trigger.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). The roles ARE DISTINCT. A single perspective covering both frames is a
T-GUARD violation. PM addresses the business question. Architect addresses the technical
question.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Phase 0 SHALL be the first output produced. Two artifacts SHALL be initialized here
before any content is authored. Both are live for the duration of this document.

── OPTION ANATOMY CONTRACT ──────────────────────────────────────────────
Every option anatomy entry in Phase 4 SHALL contain the following typed slots.
Absence of any slot from any option FIRES T-25.

  DESCRIPTION:         [what this option does — REQUIRED]
  PM FRAMING:          [business rationale, adoption path, trade-offs — REQUIRED]
  ARCHITECT VALIDATION:[technical feasibility, dependencies, constraints — REQUIRED]
  PROS:                [bulleted list — REQUIRED; minimum one item]
  CONS:                [bulleted list — REQUIRED; minimum one item]
  RISK:                P: [1-5] x I: [1-5] = P*I: [score] — [description] — REQUIRED
  EFFORT:              Timeline: [sprint] | Team: [role] | Dependencies: [any] — REQUIRED

  Option 0 additionally SHALL contain:
  INERTIA COST:        P: [1-5] x I: [1-5] = P*I: [score] per sprint — REQUIRED

  Each non-do-nothing option additionally SHALL contain:
  INERTIA OFFSET:      Sprint [N] — REQUIRED; absent fires T-08
  DECISION LEAD TIME:  [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints — REQUIRED; absent fires T-09
  ESCALATION FLAG:     REQUIRED when DECISION LEAD TIME <= 0; absent fires T-10

── CAUSAL CHAIN CONTRACT ─────────────────────────────────────────────────
The following formula SHALL be declared here, before any term-contributing phase
executes. Absence of this block FIRES T-GUARD immediately.

  TEMPORAL ANCHOR - INERTIA OFFSET = DECISION LEAD TIME

  TEMPORAL ANCHOR:    SHALL be contributed by Phase 2. Vague language PROHIBITED.
  INERTIA OFFSET:     SHALL be contributed by Phase 4, per option.
  DECISION LEAD TIME: SHALL be computed and recorded per option in Phase 4; SHALL appear
                      in Phase 7 comparison table.

  T-GUARD routing (pre-wired):
  - T-02 fires if TEMPORAL ANCHOR is absent or vague in Phase 2.
  - T-08 fires if INERTIA OFFSET is absent from any non-do-nothing option.
  - T-09 fires if DECISION LEAD TIME is absent from any non-do-nothing option.
  - T-10 fires if DECISION LEAD TIME <= 0 and ESCALATION FLAG is absent.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────────
COMPLETION STATUS: PENDING

Trigger Definitions. T-GUARD SHALL be position 1. This ordering SHALL NOT be changed.

| ID      | Scope     | Predicate — this trigger SHALL fire when this condition is true                  |
|---------|-----------|----------------------------------------------------------------------------------|
| T-GUARD | Catch-all | Any required typed slot, phase block, or gate item ABSENT from the document      |
| T-01    | Phase 1   | Scout artifact inventory absent or merged — PROHIBITED                           |
| T-02    | Phase 2   | TEMPORAL ANCHOR absent or vague — PROHIBITED; causal chain invalid               |
| T-03    | Phase 2   | INACTION CONSEQUENCE absent or uses missed-feature language — PROHIBITED         |
| T-04    | Phase 3   | P*I anchors not defined before any risk entry — PROHIBITED                       |
| T-05    | Phase 4   | Fewer than 3 options or do-nothing absent — REQUIRED minimum not met             |
| T-06    | Phase 4   | Any option missing required anatomy field from Phase 0 contract                  |
| T-07    | Phase 4   | Do-nothing missing INERTIA COST — REQUIRED                                       |
| T-08    | Phase 4   | Non-do-nothing option missing INERTIA OFFSET — REQUIRED; causal chain incomplete |
| T-09    | Phase 4   | Non-do-nothing option missing DECISION LEAD TIME — REQUIRED; formula result absent|
| T-10    | Phase 4   | DECISION LEAD TIME <= 0 and ESCALATION FLAG absent — REQUIRED                    |
| T-11    | Phase 5   | PM perspective absent or merged with Architect — PROHIBITED                      |
| T-12    | Phase 6   | Architect perspective absent or merged with PM — PROHIBITED                      |
| T-13    | Phase 7   | Comparison table absent or dimensions inconsistent — REQUIRED                    |
| T-14    | Phase 8   | Assumption register absent, < 2 A-NN entries, or not table format — REQUIRED    |
| T-15    | Phase 9   | Risk register absent, < 2 R-NN entries, or not table format — REQUIRED           |
| T-16    | Phase 10  | Failure mode register absent, < 2 F-NN entries, or not table format — REQUIRED  |
| T-17    | Phase 11  | Register appears after recommendation — ordering contract VIOLATED               |
| T-18    | Phase 11  | Prerequisite Gate block absent — REQUIRED                                        |
| T-19    | Phase 12  | PM sign-off NOT at position 1 — REQUIRED                                         |
| T-20    | Phase 12  | PM sign-off missing F-ROW ANCHOR — REQUIRED typed slot                           |
| T-21    | Phase 12  | Architect sign-off missing F-ROW ANCHOR — REQUIRED typed slot                    |
| T-22    | Phase 12  | Recommendation CONDITIONS reference no F-NN ID — REQUIRED                        |
| T-23    | Phase 13  | OWNER absent from any amend category — REQUIRED typed slot                       |
| T-24    | Phase 13  | DEADLINE absent from any amend category — REQUIRED typed slot                    |
| T-25    | Phase 4,12| PM FRAMING: or ARCHITECT VALIDATION: absent from any option or sign-off block —
              option anatomy contract VIOLATED                                           |
| T-26    | Phase 0   | Causal chain contract block absent from Phase 0 — C-33 VIOLATED                  |

Amendment Rows:

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY [REQUIRED — SHALL NOT be merged]
════════════════════════════════════════════

This phase SHALL exist as a discrete step. It SHALL NOT be merged with Phase 2 or any
other phase (fires T-01). Inventory all scout artifacts before any option is authored.

| Namespace          | Found? | Finding or Absence Note                                     |
|--------------------|--------|--------------------------------------------------------------|
| scout-feasibility  |        |                                                              |
| scout-requirements |        |                                                              |
| scout-market       |        |                                                              |
| scout-stakeholders |        |                                                              |
| scout-compliance   |        |                                                              |

If absent: INLINE ASSESSMENT SHALL substitute: [feasibility, requirements, constraints]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING [contributes TEMPORAL ANCHOR to Phase 0 causal contract]
════════════════════════════════════════════

Three typed fields are REQUIRED. Vague language in TEMPORAL ANCHOR is PROHIBITED and
fires T-02, invalidating the Phase 0 causal chain contract.

DECISION QUESTION: [the precise question being decided — one sentence — REQUIRED]

TEMPORAL ANCHOR: [specific named date, sprint, or event — "soon," "near term," "before
it is too late" are PROHIBITED. This value is the minuend in the Phase 0 formula.]

INACTION CONSEQUENCE: [a concrete named outcome — teams blocked, capability lost,
window closed. Missed-feature statements are PROHIBITED as consequence statements.
Name the specific team or capability affected.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS [REQUIRED before any risk entry]
════════════════════════════════════════════

These anchors SHALL be defined before any option risk score or INERTIA COST is
computed. Computing a score without anchors fires T-04.

| P | Meaning for this project |   | I | Meaning for this project |
|---|--------------------------|   |---|--------------------------|
| 1 | [REQUIRED]               |   | 1 | [REQUIRED]               |
| 2 | [REQUIRED]               |   | 2 | [REQUIRED]               |
| 3 | [REQUIRED]               |   | 3 | [REQUIRED]               |
| 4 | [REQUIRED]               |   | 4 | [REQUIRED]               |
| 5 | [REQUIRED]               |   | 5 | [REQUIRED]               |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING [SHALL use Phase 0 option anatomy contract]
════════════════════════════════════════════

Minimum 3 options. Option 0 SHALL be do-nothing. Each option body SHALL contain exactly
the typed slots declared in the Phase 0 option anatomy contract. Absence fires T-25
(for PM FRAMING or ARCHITECT VALIDATION) or T-06 (for all other required slots).

─────────────────────────────────────────
OPTION 0: [Do-Nothing / Status Quo]
─────────────────────────────────────────
DESCRIPTION: [what the current state continues to be — REQUIRED]

PM FRAMING: [business rationale for continuing status quo; what it preserves and what
  it forfeits; adoption implications of inaction — REQUIRED. Absence fires T-25.]
ARCHITECT VALIDATION: [technical assessment of the status quo; what accrues as debt;
  what the current state avoids — REQUIRED. Absence fires T-25.]

PROS:
  - [REQUIRED; minimum one]

CONS:
  - [REQUIRED; minimum one]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description — REQUIRED]
EFFORT: Timeline: N/A | Team: N/A | Dependencies: N/A

INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint — REQUIRED; absence fires T-07
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 1: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does — REQUIRED]

PM FRAMING: [business rationale, adoption path, trade-offs — REQUIRED. Absence fires T-25.]
ARCHITECT VALIDATION: [feasibility, dependencies, constraints — REQUIRED. Absence fires T-25.]

PROS:
  - [REQUIRED; minimum one]

CONS:
  - [REQUIRED; minimum one]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description using Phase 3 anchors — REQUIRED]
EFFORT: Timeline: [named sprint] | Team: [named role] | Dependencies: [any] — REQUIRED

INERTIA OFFSET: Sprint [N] — REQUIRED; absence fires T-08
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints — REQUIRED; absence fires T-09
ESCALATION FLAG: REQUIRED when DECISION LEAD TIME <= 0 — name inertia trap and escalation authority
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 2: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does — REQUIRED]

PM FRAMING: [business rationale — REQUIRED. Absence fires T-25.]
ARCHITECT VALIDATION: [feasibility — REQUIRED. Absence fires T-25.]

PROS:
  - [REQUIRED]

CONS:
  - [REQUIRED]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description — REQUIRED]
EFFORT: Timeline: [sprint] | Team: [role] | Dependencies: [any] — REQUIRED

INERTIA OFFSET: Sprint [N] — REQUIRED
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints — REQUIRED
ESCALATION FLAG: REQUIRED when DECISION LEAD TIME <= 0
─────────────────────────────────────────

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE [SHALL be standalone — SHALL NOT be merged with Phase 6]
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [REQUIRED — PM preferred option on business factors alone]
PM TRADE-OFF ANALYSIS: [REQUIRED — for each non-trivial option, the business condition
  under which it would be the correct choice]
ADOPTION CONCERN: [REQUIRED — primary adoption barrier for PM-preferred option]
BUSINESS RISK: [REQUIRED — condition that most directly invalidates PM's signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE [SHALL be standalone — SHALL respond to Phase 5]
════════════════════════════════════════════

ARCHITECT VALIDATION: [REQUIRED — confirms or challenges PM signal from technical
  standpoint. SHALL reference PM's signal. Independent proposal PROHIBITED.]
TECHNICAL CONSTRAINT: [REQUIRED — primary technical constraint bounding option selection]
DEPENDENCY NOTE: [REQUIRED — blocking dependency for architecturally preferred option]
TECHNICAL RISK: [REQUIRED — condition that most directly invalidates Architect's validation]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE [REQUIRED — every option SHALL appear in every row]
════════════════════════════════════════════

| Dimension           | Option 0 (Do-Nothing) | Option 1: [Name] | Option 2: [Name] | [Option N] |
|---------------------|-----------------------|------------------|------------------|------------|
| PM Signal           |                       |                  |                  |            |
| Architect Signal    |                       |                  |                  |            |
| Effort              |                       |                  |                  |            |
| Timeline            |                       |                  |                  |            |
| Risk P*I            |                       |                  |                  |            |
| Adoption Friction   |                       |                  |                  |            |
| Control             |                       |                  |                  |            |
| INERTIA COST/sprint | [P*I value]           | N/A              | N/A              | N/A        |
| INERTIA OFFSET      | N/A                   | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME  | N/A                   | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER [REQUIRED — SHALL appear before Phase 12]
════════════════════════════════════════════

Minimum 2 entries. Table format REQUIRED. Prose format PROHIBITED.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 | [text]     | [method + sprint] |
| A-02 | [text]     | [method + sprint] |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER [REQUIRED — SHALL appear before Phase 12]
════════════════════════════════════════════

Minimum 2 entries. Numeric P*I REQUIRED. L/M/H labels PROHIBITED. Table format REQUIRED.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 | [text] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |
| R-02 | [text] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER [REQUIRED — SHALL appear before Phase 12]
════════════════════════════════════════════

Minimum 2 entries. Labels FAILURE MODE, TRIGGER CONDITION, MITIGATION are EXACT —
synonyms PROHIBITED. Table format REQUIRED.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|--------------|-------------------|------------|
| F-01 | [text]       | [trigger]         | [mitigation] |
| F-02 | [text]       | [trigger]         | [mitigation] |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE [REQUIRED — SHALL immediately precede Phase 12]
════════════════════════════════════════════

Each item is binary: COMPLETE or NOT COMPLETE. NOT COMPLETE FIRES the corresponding trigger.

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ entries, table format                   | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ entries, table format, numeric P*I            | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ entries, canonical labels             | COMPLETE / NOT COMPLETE |
| 4 | Registers appear before this gate in document sequence          | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST on do-nothing using Phase 3 scale                  | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative has INERTIA OFFSET                     | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives have DECISION LEAD TIME         | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME <= 0 alternatives have ESCALATION FLAG   | COMPLETE / NOT COMPLETE |
| 9 | PM FRAMING: and ARCHITECT VALIDATION: in every option           | COMPLETE / NOT COMPLETE |
|10 | Phase 0 causal chain contract present with formula and routing  | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION [PM sign-off SHALL be position 1]
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name — REQUIRED]
RATIONALE: [REQUIRED — reference Phase 7 dimensions, PM signal, Architect validation]
CONDITIONS: [REQUIRED — 2-3 conditions; SHALL reference at least one F-NN ID]

── PM SIGN-OFF (position 1 — SHALL be first signatory) ─────────────────
ROLE: PM
PM FRAMING: [PM business case confirmation — REQUIRED. Absence fires T-25.]
ARCHITECT VALIDATION: [PM's frame for what Architect must confirm — REQUIRED. Absence fires T-25.]
CONDITIONS: [SHALL reference at least one F-NN ID — REQUIRED]
F-ROW ANCHOR: [REQUIRED typed slot — absence fires T-20]

── ARCHITECT SIGN-OFF (position 2 — SHALL respond to PM frame) ─────────
ROLE: Architect
PM FRAMING: [Architect acknowledges PM's business decision — REQUIRED. Absence fires T-25.]
ARCHITECT VALIDATION: [Technical soundness confirmation — REQUIRED. Absence fires T-25.]
CONDITIONS: [SHALL reference at least one F-NN ID — REQUIRED]
F-ROW ANCHOR: [REQUIRED typed slot — absence fires T-21]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE [all three categories REQUIRED]
════════════════════════════════════════════

OWNER and DEADLINE are REQUIRED typed slots in every entry. Absence fires T-23 or T-24.

── MISSING OPTION ───────────────────────────────────────────────────────
OPTION: [option not explored — REQUIRED]
REASON NOT EXPLORED: [why excluded — REQUIRED]
OWNER: [named role or person — REQUIRED]
DEADLINE: [specific sprint, date, or milestone — "TBD" and "soon" PROHIBITED]

── UNWEIGHTED CRITERION ─────────────────────────────────────────────────
CRITERION: [dimension not weighted — REQUIRED]
RECALIBRATION NOTE: [why different weighting is warranted — REQUIRED]
OWNER: [named role — REQUIRED]
DEADLINE: [specific sprint, date, or milestone — REQUIRED]

── FOLLOW-UP ─────────────────────────────────────────────────────────────
ACTION: [specific action — REQUIRED]
OWNER: [named role — REQUIRED]
DEADLINE: [specific sprint, date, or milestone — REQUIRED]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no amendment rows: COMPLETION STATUS: T-GUARD enforced all requirements — no violations.
If amendment rows exist: COMPLETION STATUS: [N] amendments logged — see rows above.

Update COMPLETION STATUS in Phase 0 to its terminal value. This is REQUIRED.
```

---

## V-04 — Field-Level Role Enforcement + Phase 0 Causal Contract (C-32 + C-33)

**Variation axis:** Combined — Phase 0 declares both the option anatomy contract (C-32) and the causal chain contract (C-33). Both contracts are initialized before any term-contributing phase executes. Phase 4 inherits both. Phase 12 inherits the option anatomy contract.

**Hypothesis:** C-32 and C-33 are orthogonal Phase 0 additions — the option anatomy contract governs role-slot structure, the causal chain contract governs urgency formula structure. They do not interfere. Combining them in a single variation tests composability: can both contracts coexist in Phase 0 without ambiguity, and do they jointly produce the three role-enforcement points (Phase 0 template, Phase 4 options, Phase 12 sign-off) and the formula prospective enforcement?

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). Both roles contribute distinct perspectives.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize three artifacts before any content is authored. All are live from this point.

── OPTION ANATOMY CONTRACT ──────────────────────────────────────────────
This contract governs every option entry in Phase 4 and every sign-off block in Phase 12.
PM FRAMING: and ARCHITECT VALIDATION: are required typed slots in every option entry and
every sign-off block. Absence of either slot fires T-25.

Required typed slots in every option entry:

  DESCRIPTION:         [what this option does]
  PM FRAMING:          [business rationale, adoption path, trade-offs — PM speaks first]
  ARCHITECT VALIDATION:[technical feasibility, dependencies, constraints — responds to PM]
  PROS:                [bulleted list]
  CONS:                [bulleted list]
  RISK:                P: [1-5] x I: [1-5] = P*I: [score] — [description]
  EFFORT:              Timeline: [sprint] | Team: [role] | Dependencies: [any]

  Option 0 additionally: INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint
  Each non-do-nothing option additionally:
    INERTIA OFFSET:      Sprint [N]
    DECISION LEAD TIME:  [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
    ESCALATION FLAG:     Required when DECISION LEAD TIME <= 0

── CAUSAL CHAIN CONTRACT ─────────────────────────────────────────────────
The following formula governs urgency computation in this document. Declared before any
term-contributing phase executes. Absence of this block fires T-GUARD immediately.

  TEMPORAL ANCHOR - INERTIA OFFSET = DECISION LEAD TIME

  TEMPORAL ANCHOR:    contributed by Phase 2
  INERTIA OFFSET:     contributed by Phase 4, per option
  DECISION LEAD TIME: computed and recorded per option in Phase 4; surfaced in Phase 7

T-GUARD routing:
  - T-02 fires if TEMPORAL ANCHOR is absent or vague in Phase 2 (formula invalid)
  - T-08 fires if INERTIA OFFSET absent from any non-do-nothing option in Phase 4
  - T-09 fires if DECISION LEAD TIME absent from any non-do-nothing option in Phase 4
  - T-10 fires if DECISION LEAD TIME <= 0 and ESCALATION FLAG absent
  - T-25 fires if PM FRAMING: or ARCHITECT VALIDATION: absent from any option or sign-off
  - T-26 fires if this causal chain contract block is absent from Phase 0

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────────
COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1 — sentinel-first ordering required):

| ID      | Scope     | Predicate — trigger fires when this condition is true                           |
|---------|-----------|---------------------------------------------------------------------------------|
| T-GUARD | Catch-all | Any required typed slot, phase block, or gate item absent from the document     |
| T-01    | Phase 1   | Scout artifact inventory absent or merged into another phase                    |
| T-02    | Phase 2   | TEMPORAL ANCHOR missing or vague — causal chain contract invalidated            |
| T-03    | Phase 2   | INACTION CONSEQUENCE missing or uses missed-feature language                    |
| T-04    | Phase 3   | P*I anchors not defined before any risk entry is scored                         |
| T-05    | Phase 4   | Fewer than 3 options or do-nothing option absent                                |
| T-06    | Phase 4   | Any option missing required anatomy field from Phase 0 contract                 |
| T-07    | Phase 4   | Do-nothing missing typed INERTIA COST                                           |
| T-08    | Phase 4   | Non-do-nothing option missing INERTIA OFFSET — causal chain incomplete          |
| T-09    | Phase 4   | Non-do-nothing option missing DECISION LEAD TIME — formula result absent        |
| T-10    | Phase 4   | DECISION LEAD TIME <= 0 and ESCALATION FLAG absent                              |
| T-11    | Phase 5   | PM perspective absent or merged with Architect                                  |
| T-12    | Phase 6   | Architect perspective absent or merged with PM                                  |
| T-13    | Phase 7   | Comparison table absent or dimensions inconsistent                              |
| T-14    | Phase 8   | Assumption register absent, <2 entries, or not in table format                  |
| T-15    | Phase 9   | Risk register absent, <2 entries, or not in table format                        |
| T-16    | Phase 10  | Failure mode register absent, <2 entries, or not in table format                |
| T-17    | Phase 11  | Register appears after recommendation phase                                     |
| T-18    | Phase 11  | PREREQUISITE GATE block absent                                                  |
| T-19    | Phase 12  | PM sign-off not at position 1                                                   |
| T-20    | Phase 12  | PM sign-off missing typed F-ROW ANCHOR                                          |
| T-21    | Phase 12  | Architect sign-off missing typed F-ROW ANCHOR                                   |
| T-22    | Phase 12  | Recommendation CONDITIONS reference no F-NN ID                                  |
| T-23    | Phase 13  | OWNER absent from any amend entry category                                      |
| T-24    | Phase 13  | DEADLINE absent from any amend entry category                                   |
| T-25    | Phase 4,12| PM FRAMING: or ARCHITECT VALIDATION: absent from any option or sign-off block — option anatomy contract violated |
| T-26    | Phase 0   | Causal chain contract block absent from Phase 0 — C-33 violated                 |

Amendment Rows:

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY
════════════════════════════════════════════

Inventory all scout artifacts before any option is authored. Discrete step — not merged.

| Namespace          | Found? | Finding or Absence Note                                     |
|--------------------|--------|--------------------------------------------------------------|
| scout-feasibility  |        |                                                              |
| scout-requirements |        |                                                              |
| scout-market       |        |                                                              |
| scout-stakeholders |        |                                                              |
| scout-compliance   |        |                                                              |

If absent: INLINE ASSESSMENT: [feasibility, requirements, and constraints]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING [contributes TEMPORAL ANCHOR to Phase 0 causal contract]
════════════════════════════════════════════

DECISION QUESTION: [the precise question being decided — one sentence]

TEMPORAL ANCHOR: [specific named date, sprint, or event — vague language prohibited.
  Phase 0 causal chain contract: this value is the minuend.]

INACTION CONSEQUENCE: [a concrete named outcome — teams blocked, capability lost, or
  window closed. Missed-feature statements do not qualify.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

| P | Meaning |   | I | Meaning |
|---|---------|   |---|---------|
| 1 | [P=1]   |   | 1 | [I=1]   |
| 2 | [P=2]   |   | 2 | [I=2]   |
| 3 | [P=3]   |   | 3 | [I=3]   |
| 4 | [P=4]   |   | 4 | [I=4]   |
| 5 | [P=5]   |   | 5 | [I=5]   |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING [Phase 0 anatomy + causal contracts govern this phase]
════════════════════════════════════════════

Minimum 3 options. Option 0 must be do-nothing. Author each option using the Phase 0
option anatomy contract. PM FRAMING: and ARCHITECT VALIDATION: are required typed slots
in every entry (absence fires T-25). INERTIA OFFSET and DECISION LEAD TIME are required
on all non-do-nothing options per the Phase 0 causal chain contract.

─────────────────────────────────────────
OPTION 0: [Do-Nothing / Status Quo]
─────────────────────────────────────────
DESCRIPTION: [what the current state continues to be]

PM FRAMING: [business rationale for status quo; what it preserves and what it forfeits]
ARCHITECT VALIDATION: [technical assessment; debt accrual; what constraints it avoids]

PROS:
  - [pro 1]

CONS:
  - [con 1]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: N/A | Team: N/A | Dependencies: N/A
INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 1: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, trade-offs]
ARCHITECT VALIDATION: [feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]

CONS:
  - [con 1]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: [sprint] | Team: [role] | Dependencies: [any]

INERTIA OFFSET: Sprint [N] [Phase 0 causal contract: subtrahend]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0]
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 2: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, trade-offs]
ARCHITECT VALIDATION: [feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]

CONS:
  - [con 1]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: [sprint] | Team: [role] | Dependencies: [any]

INERTIA OFFSET: Sprint [N]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0]
─────────────────────────────────────────

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [PM preferred option based on business factors alone]
PM TRADE-OFF ANALYSIS: [business condition under which each non-trivial option would win]
ADOPTION CONCERN: [primary adoption barrier for PM-preferred option]
BUSINESS RISK: [condition that most directly invalidates PM's signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE
════════════════════════════════════════════

ARCHITECT VALIDATION: [confirms or challenges PM signal — must reference PM's signal]
TECHNICAL CONSTRAINT: [primary technical constraint bounding option selection]
DEPENDENCY NOTE: [blocking dependency for architecturally preferred option]
TECHNICAL RISK: [condition that most directly invalidates Architect's validation]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

DECISION LEAD TIME row surfaces the Phase 0 causal chain formula results across options.

| Dimension           | Option 0 (Do-Nothing) | Option 1: [Name] | Option 2: [Name] | [Option N] |
|---------------------|-----------------------|------------------|------------------|------------|
| PM Signal           |                       |                  |                  |            |
| Architect Signal    |                       |                  |                  |            |
| Effort              |                       |                  |                  |            |
| Timeline            |                       |                  |                  |            |
| Risk P*I            |                       |                  |                  |            |
| Adoption Friction   |                       |                  |                  |            |
| Control             |                       |                  |                  |            |
| INERTIA COST/sprint | [P*I]                 | N/A              | N/A              | N/A        |
| INERTIA OFFSET      | N/A                   | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME  | N/A                   | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

Minimum 2 entries. Table format required.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 | [text]     | [method + sprint] |
| A-02 | [text]     | [method + sprint] |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

Minimum 2 entries. Numeric P*I. Table format required.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 | [text] | [1-5] | [1-5] | [P*I] | [owner + action] |
| R-02 | [text] | [1-5] | [1-5] | [P*I] | [owner + action] |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

Minimum 2 entries. Canonical labels required.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|--------------|-------------------|------------|
| F-01 | [text]       | [trigger]         | [action]   |
| F-02 | [text]       | [trigger]         | [action]   |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

| # | Check | Status |
|---|-------|--------|
| 1  | Assumption register: 2+ entries, table format                  | COMPLETE / NOT COMPLETE |
| 2  | Risk register: 2+ entries, table format, numeric P*I           | COMPLETE / NOT COMPLETE |
| 3  | Failure mode register: 2+ entries, canonical labels            | COMPLETE / NOT COMPLETE |
| 4  | All registers appear before this gate                          | COMPLETE / NOT COMPLETE |
| 5  | INERTIA COST on do-nothing using Phase 3 P*I scale             | COMPLETE / NOT COMPLETE |
| 6  | At least one alternative has INERTIA OFFSET                    | COMPLETE / NOT COMPLETE |
| 7  | All non-do-nothing alternatives have DECISION LEAD TIME        | COMPLETE / NOT COMPLETE |
| 8  | All DECISION LEAD TIME <= 0 alternatives have ESCALATION FLAG  | COMPLETE / NOT COMPLETE |
| 9  | PM FRAMING: and ARCHITECT VALIDATION: in every option          | COMPLETE / NOT COMPLETE |
| 10 | Phase 0 option anatomy contract present                        | COMPLETE / NOT COMPLETE |
| 11 | Phase 0 causal chain contract present with formula, attribution, T-GUARD routing | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION [PM sign-off first; anatomy contract governs sign-off blocks]
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [references Phase 7 dimensions, Phase 5 PM signal, Phase 6 Architect validation,
  and Phase 0 causal chain DECISION LEAD TIME values]
CONDITIONS: [2-3 conditions; reference at least one F-NN ID]

── PM SIGN-OFF (position 1 — first signatory) ──────────────────────────
ROLE: PM
PM FRAMING: [PM confirms this is the right business decision; expected value of acting
  exceeds INERTIA COST of not acting; adoption path is viable]
ARCHITECT VALIDATION: [PM's expectation of what Architect must confirm for this to stand]
CONDITIONS: [must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID whose trigger most directly invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2 — second signatory) ──────────────────
ROLE: Architect
PM FRAMING: [Architect acknowledges PM's business frame — confirms responding to it]
ARCHITECT VALIDATION: [Architect confirms technical soundness of the recommended option]
CONDITIONS: [must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID whose trigger most directly invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

OWNER and DEADLINE typed slots in every entry across all three categories.

── MISSING OPTION ───────────────────────────────────────────────────────
OPTION: [option not explored]
REASON NOT EXPLORED: [why excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone — not "TBD" or "soon"]

── UNWEIGHTED CRITERION ─────────────────────────────────────────────────
CRITERION: [dimension not weighted]
RECALIBRATION NOTE: [why different weighting warranted]
OWNER: [named role]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ─────────────────────────────────────────────────────────────
ACTION: [specific follow-up action]
OWNER: [named role]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no rows: COMPLETION STATUS: T-GUARD enforced all requirements — no violations.
If rows exist: COMPLETION STATUS: [N] amendments logged — see rows above.

Update COMPLETION STATUS in Phase 0 to its terminal value now.
```

---

## V-05 — All Six Axes: C-28 through C-33 (Target: 100.0)

**Variation axis:** Maximum coverage — all six axes combined: PM-first role sequence (C-28), canonical table headers declared at Phase 0 (C-29), phase manifest at Phase 0 (C-30), DECISION LEAD TIME chain in Phase 4 and Phase 7 (C-31), option anatomy contract with typed role slots in Phase 0 (C-32), and causal chain contract in Phase 0 (C-33).

**Hypothesis:** A prompt incorporating all six axes simultaneously should score 100.0 under v9 (26/26 criteria). Phase 0 declares four initialization contracts (phase manifest, register format contracts, option anatomy contract, causal chain contract). PM-first ordering propagates through every dual-role phase. All three C-32 enforcement points are present: Phase 0 template declaration, Phase 4 every option, Phase 12 every sign-off block.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLE ORDERING: PM leads. Architect responds and validates. This ordering applies to every
dual-role phase: decision framing, option authoring, perspective phases, and sign-off.
PM speaks first. Architect extends or challenges from a technical standpoint.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize four artifacts before any content is authored. All are live from this point.

── PHASE MANIFEST ────────────────────────────────────────────────────────
Every phase in this document is listed here. A reviewer confirms lifecycle ordering
from this manifest without scanning the document.

| #  | Phase Name                  | Purpose                                                     |
|----|-----------------------------|-------------------------------------------------------------|
| 0  | Initialization              | Four contracts: phase manifest, register formats, option anatomy, causal chain |
| 1  | Scout Artifact Inventory    | Inventory found and absent artifacts before option generation — PM-led          |
| 2  | Decision Framing            | TEMPORAL ANCHOR + INACTION CONSEQUENCE — PM-led; Architect annotates constraint |
| 3  | P*I Scoring Anchors         | Project-specific probability and impact definitions                             |
| 4  | Options Authoring           | 3+ options; PM FRAMING + ARCHITECT VALIDATION per entry; inertia fields         |
| 5  | PM Perspective              | Business and adoption assessment (standalone)                                   |
| 6  | Architect Perspective       | Technical constraint and feasibility assessment (standalone, responds to PM)    |
| 7  | Comparison Table            | All options on consistent dimensions including DECISION LEAD TIME               |
| 8  | Assumption Register         | A-NN table — BEFORE recommendation                                              |
| 9  | Risk Register               | R-NN table, numeric P*I — BEFORE recommendation                                 |
| 10 | Failure Mode Register       | F-NN table, canonical labels — BEFORE recommendation                            |
| 11 | Prerequisite Gate           | Confirm all register and contract requirements before sign-off                  |
| 12 | Recommendation              | PM sign-off position 1; Architect sign-off position 2                           |
| 13 | Amend Phase                 | Three categories: missing option, unweighted criterion, follow-up               |
| 14 | Amendment Table Finalization| Update COMPLETION STATUS to terminal value                                      |

LIFECYCLE ORDERING (from manifest):
- Phase 8 (Assumption Register): before Phase 12 (Recommendation)
- Phase 9 (Risk Register): before Phase 12 (Recommendation)
- Phase 10 (Failure Mode Register): before Phase 12 (Recommendation)
- Phase 11 (Prerequisite Gate): immediately precedes Phase 12 (Recommendation)

── REGISTER FORMAT CONTRACTS ─────────────────────────────────────────────
The following are canonical table formats for the three registers. No register may
use prose blocks or synonym headers. Deviation fires the corresponding trigger.

ASSUMPTION REGISTER FORMAT (canonical — use verbatim):
| A-NN | ASSUMPTION | VALIDATION PLAN |

RISK REGISTER FORMAT (canonical — use verbatim):
| R-NN | RISK | P | I | P*I | MITIGATION |

FAILURE MODE REGISTER FORMAT (canonical — use verbatim):
| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |

Column headers are format contracts. Synonyms ("Observable Event" for TRIGGER CONDITION,
"Fallback" for MITIGATION, embedded prose for P/I) fire T-15 or T-16.

── OPTION ANATOMY CONTRACT ──────────────────────────────────────────────
Required typed slots in every option entry (Phase 4) and every sign-off block (Phase 12).
PM FRAMING: and ARCHITECT VALIDATION: are mandatory typed slots. Absence fires T-25.

  DESCRIPTION:         [what this option does]
  PM FRAMING:          [business rationale, adoption path, trade-offs — PM speaks first]
  ARCHITECT VALIDATION:[technical feasibility, dependencies, constraints — responds to PM]
  PROS:                [bulleted list]
  CONS:                [bulleted list]
  RISK:                P: [1-5] x I: [1-5] = P*I: [score] — [description]
  EFFORT:              Timeline: [sprint] | Team: [role] | Dependencies: [any]

  Option 0 additionally: INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint
  Non-do-nothing options additionally:
    INERTIA OFFSET:      Sprint [N]
    DECISION LEAD TIME:  [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
    ESCALATION FLAG:     Required when DECISION LEAD TIME <= 0

── CAUSAL CHAIN CONTRACT ─────────────────────────────────────────────────
Declared before any term-contributing phase executes. Absence fires T-27.

  TEMPORAL ANCHOR - INERTIA OFFSET = DECISION LEAD TIME

  TEMPORAL ANCHOR:    contributed by Phase 2 (TEMPORAL ANCHOR field)
  INERTIA OFFSET:     contributed by Phase 4 (INERTIA OFFSET field, per option)
  DECISION LEAD TIME: computed per option in Phase 4; surfaced in Phase 7 comparison table row

T-GUARD routing:
  - T-02: TEMPORAL ANCHOR absent or vague in Phase 2 (formula invalid — all DLT values void)
  - T-08: INERTIA OFFSET absent from any non-do-nothing option (formula incomplete)
  - T-09: DECISION LEAD TIME absent from any non-do-nothing option (formula result absent)
  - T-10: DECISION LEAD TIME <= 0 and ESCALATION FLAG absent
  - T-25: PM FRAMING: or ARCHITECT VALIDATION: absent from any option or sign-off block
  - T-27: This causal chain contract block absent from Phase 0

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────────
COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1 — sentinel-first ordering required):

| ID      | Scope     | Predicate — trigger fires when this condition is true                           |
|---------|-----------|---------------------------------------------------------------------------------|
| T-GUARD | Catch-all | Any required typed slot, phase block, or gate item absent from the document     |
| T-01    | Phase 1   | Scout artifact inventory absent or merged into another phase                    |
| T-02    | Phase 2   | TEMPORAL ANCHOR missing or vague — Phase 0 causal chain contract invalidated    |
| T-03    | Phase 2   | INACTION CONSEQUENCE missing or uses missed-feature language                    |
| T-04    | Phase 3   | P*I anchors not defined before any risk entry is scored                         |
| T-05    | Phase 4   | Fewer than 3 options or do-nothing absent                                       |
| T-06    | Phase 4   | Any option missing required anatomy field from Phase 0 contract                 |
| T-07    | Phase 4   | Do-nothing missing typed INERTIA COST                                           |
| T-08    | Phase 4   | Non-do-nothing option missing INERTIA OFFSET                                    |
| T-09    | Phase 4   | Non-do-nothing option missing DECISION LEAD TIME                                |
| T-10    | Phase 4   | DECISION LEAD TIME <= 0 and ESCALATION FLAG absent                              |
| T-11    | Phase 5   | PM perspective absent or merged with Architect                                  |
| T-12    | Phase 6   | Architect perspective absent or merged with PM                                  |
| T-13    | Phase 7   | Comparison table absent or dimensions inconsistent                              |
| T-14    | Phase 8   | Assumption register not in canonical format declared in Phase 0                 |
| T-15    | Phase 9   | Risk register not in canonical format declared in Phase 0                       |
| T-16    | Phase 10  | Failure mode register not in canonical format declared in Phase 0               |
| T-17    | Phase 11  | Any register appears after Phase 12 (manifest ordering violated)                |
| T-18    | Phase 11  | Prerequisite Gate block absent                                                  |
| T-19    | Phase 12  | PM sign-off not at position 1                                                   |
| T-20    | Phase 12  | PM sign-off missing typed F-ROW ANCHOR                                          |
| T-21    | Phase 12  | Architect sign-off missing typed F-ROW ANCHOR                                   |
| T-22    | Phase 12  | Recommendation CONDITIONS reference no F-NN ID                                  |
| T-23    | Phase 13  | OWNER absent from any amend category entry                                      |
| T-24    | Phase 13  | DEADLINE absent from any amend category entry                                   |
| T-25    | Phase 4,12| PM FRAMING: or ARCHITECT VALIDATION: absent from any option or sign-off block — option anatomy contract violated |
| T-26    | Phase 0   | Phase manifest absent or incomplete                                             |
| T-27    | Phase 0   | Causal chain contract absent from Phase 0                                       |

Amendment Rows (populated live — empty rows confirm T-GUARD enforcement):

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY [PM-led; discrete step — not merged]
════════════════════════════════════════════

PM leads: inventory all scout artifacts available for this topic before any option is
authored. State what was found and what is absent. Absence fires T-01 if this phase
is merged with Phase 2 or any other phase.

| Namespace          | Artifact Found? | Finding or Absence Note                                     |
|--------------------|-----------------|--------------------------------------------------------------|
| scout-feasibility  | yes / no        | [artifact name and key finding, or "absent — inline below"] |
| scout-requirements | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-market       | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-stakeholders | yes / no        | [artifact name and key finding, or "absent"]                 |
| scout-compliance   | yes / no        | [artifact name and key finding, or "absent"]                 |

If absent: INLINE ASSESSMENT: [PM's direct assessment of feasibility, requirements, constraints]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING [PM-led; Architect annotates technical constraint]
════════════════════════════════════════════

PM frames the decision using three typed fields. Architect adds a TECHNICAL CONSTRAINT
annotation that responds to PM framing but does not reframe the business question.

DECISION QUESTION: [the precise question being decided — one sentence]

TEMPORAL ANCHOR: [specific named date, sprint, or event — vague language prohibited.
  Phase 0 causal chain contract: this value is the minuend in the formula.]

INACTION CONSEQUENCE: [a concrete named outcome if the decision is not made by
  TEMPORAL ANCHOR — teams blocked, capability lost, or window closed. Missed-feature
  statements do not qualify as consequences. Name the specific team or capability.]

ARCHITECT CONSTRAINT ANNOTATION: [technical constraint that bounds or accelerates the
  decision — must respond to PM framing, not replace it]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

Define project-specific anchors before any option is scored. Applies to Phase 9 risk
register and all INERTIA COST calculations in Phase 4.

| P | Meaning for this project |
|---|--------------------------|
| 1 | [Remote — define threshold] |
| 2 | [Unlikely — define threshold] |
| 3 | [Possible — define threshold] |
| 4 | [Likely — define threshold] |
| 5 | [Near-certain — define threshold] |

| I | Meaning for this project |
|---|--------------------------|
| 1 | [Negligible — define scope] |
| 2 | [Minor — define scope] |
| 3 | [Moderate — define scope] |
| 4 | [Significant — define scope] |
| 5 | [Critical — define scope] |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING [PM-led; Phase 0 anatomy + causal contracts govern this phase]
════════════════════════════════════════════

Minimum 3 options. Option 0 must be do-nothing. PM frames each option's business
context first. Architect validates feasibility and effort, responding to PM.

PM FRAMING: and ARCHITECT VALIDATION: are required typed slots per Phase 0 option
anatomy contract. Absence of either slot fires T-25.

INERTIA OFFSET and DECISION LEAD TIME are required per Phase 0 causal chain contract
on all non-do-nothing options.

─────────────────────────────────────────
OPTION 0: [Do-Nothing / Status Quo]
─────────────────────────────────────────
DESCRIPTION: [what the current state continues to be]

PM FRAMING: [business rationale for considering status quo; what it preserves and
  what it forfeits; adoption implications of inaction — PM speaks]
ARCHITECT VALIDATION: [technical assessment: debt accrual, constraint avoidance,
  what the current state already costs — responds to PM framing]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [risk of continuing status quo]
EFFORT: Timeline: N/A | Team: N/A | Dependencies: N/A

INERTIA COST: P: [1-5] x I: [1-5] = P*I: [score] per sprint
  (Per-sprint cost of inaction on Phase 3 P*I scale)
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 1: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, key trade-offs — PM speaks]
ARCHITECT VALIDATION: [technical feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description using Phase 3 anchors]
EFFORT: Timeline: [named sprint or milestone] | Team: [named role or team] | Dependencies: [any]

INERTIA OFFSET: Sprint [N] — crossover sprint where cumulative implementation cost equals
  cumulative INERTIA COST of not acting. [Phase 0 causal chain: this is the subtrahend.]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
  [Phase 0 formula result. Positive = lead time. Zero or negative = inertia trap.]
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0 — name trap and escalation authority]
─────────────────────────────────────────

─────────────────────────────────────────
OPTION 2: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, key trade-offs — PM speaks]
ARCHITECT VALIDATION: [feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] x I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: [sprint] | Team: [role] | Dependencies: [any]

INERTIA OFFSET: Sprint [N] [Phase 0 causal chain: subtrahend]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] - [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME <= 0]
─────────────────────────────────────────

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE [PM-led; standalone — not merged with Phase 6]
════════════════════════════════════════════

PM provides a standalone business and adoption assessment across all options.

PM RECOMMENDATION SIGNAL: [PM preferred option based on business factors alone]
PM TRADE-OFF ANALYSIS: [for each non-trivial option, the business condition under
  which it would be the correct choice]
ADOPTION CONCERN: [primary adoption barrier for the PM-preferred option]
BUSINESS RISK: [the business condition that would most directly invalidate PM's signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE [responds to PM — standalone; not merged with Phase 5]
════════════════════════════════════════════

Architect provides a standalone technical assessment, explicitly responding to Phase 5.

ARCHITECT VALIDATION: [confirms or challenges PM recommendation signal from a technical
  standpoint — must reference PM's signal, not produce an independent proposal]
TECHNICAL CONSTRAINT: [the primary technical constraint bounding option selection]
DEPENDENCY NOTE: [blocking dependency for the architecturally preferred option]
TECHNICAL RISK: [the technical condition that would most directly invalidate Architect's
  validation of the PM-preferred option]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE [PM-relevant dimensions precede technical dimensions]
════════════════════════════════════════════

Every option appears in every row. DECISION LEAD TIME row surfaces Phase 0 causal chain
formula results. PM-relevant dimensions (PM Signal, Adoption Friction) appear before
technical dimensions (TECHNICAL CONSTRAINT, Dependencies).

| Dimension           | Option 0 (Do-Nothing) | Option 1: [Name] | Option 2: [Name] | [Option N] |
|---------------------|-----------------------|------------------|------------------|------------|
| PM Signal           |                       |                  |                  |            |
| Adoption Friction   |                       |                  |                  |            |
| Architect Signal    |                       |                  |                  |            |
| Effort              |                       |                  |                  |            |
| Timeline            |                       |                  |                  |            |
| Risk P*I            |                       |                  |                  |            |
| Control             |                       |                  |                  |            |
| INERTIA COST/sprint | [P*I value]           | N/A              | N/A              | N/A        |
| INERTIA OFFSET      | N/A                   | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME  | N/A                   | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER [use canonical format declared in Phase 0]
════════════════════════════════════════════

Use the Phase 0 canonical format. Prose blocks with embedded field labels fire T-14.
Minimum 2 entries.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 | [assumption text] | [method and sprint] |
| A-02 | [assumption text] | [method and sprint] |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER [use canonical format declared in Phase 0]
════════════════════════════════════════════

Use the Phase 0 canonical format. Holistic L/M/H labels are not acceptable — numeric
P*I using Phase 3 anchors is required. Minimum 2 entries.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 | [risk description] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |
| R-02 | [risk description] | [1-5] | [1-5] | [P*I] | [mitigation with owner] |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER [use canonical format declared in Phase 0]
════════════════════════════════════════════

Use the Phase 0 canonical format. FAILURE MODE, TRIGGER CONDITION, and MITIGATION are
exact labels — synonyms fire T-16. Minimum 2 entries.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|--------------|-------------------|------------|
| F-01 | [failure mode] | [trigger condition] | [mitigation] |
| F-02 | [failure mode] | [trigger condition] | [mitigation] |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE [immediately precedes Phase 12 per Phase 0 manifest]
════════════════════════════════════════════

Binary COMPLETE / NOT COMPLETE. NOT COMPLETE fires the corresponding trigger.

| #  | Check | Status |
|----|-------|--------|
| 1  | Assumption register: 2+ entries, canonical A-NN format                    | COMPLETE / NOT COMPLETE |
| 2  | Risk register: 2+ entries, canonical R-NN format, numeric P*I             | COMPLETE / NOT COMPLETE |
| 3  | Failure mode register: 2+ entries, canonical F-NN format                  | COMPLETE / NOT COMPLETE |
| 4  | All registers appear before Phase 12 (manifest ordering verified)         | COMPLETE / NOT COMPLETE |
| 5  | INERTIA COST on do-nothing using Phase 3 P*I scale                        | COMPLETE / NOT COMPLETE |
| 6  | At least one alternative carries INERTIA OFFSET                           | COMPLETE / NOT COMPLETE |
| 7  | All non-do-nothing alternatives carry DECISION LEAD TIME                  | COMPLETE / NOT COMPLETE |
| 8  | All DECISION LEAD TIME <= 0 alternatives carry ESCALATION FLAG            | COMPLETE / NOT COMPLETE |
| 9  | PM FRAMING: and ARCHITECT VALIDATION: present in every option             | COMPLETE / NOT COMPLETE |
| 10 | PM FRAMING: and ARCHITECT VALIDATION: present in both sign-off blocks     | COMPLETE / NOT COMPLETE |
| 11 | Phase 0 option anatomy contract block present                             | COMPLETE / NOT COMPLETE |
| 12 | Phase 0 causal chain contract with formula, attribution, T-GUARD routing  | COMPLETE / NOT COMPLETE |
| 13 | Phase 0 phase manifest present and all 15 phases listed                   | COMPLETE / NOT COMPLETE |
| 14 | Phase 0 register format contracts declared for all three register types   | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION [PM sign-off position 1; anatomy contract governs sign-offs]
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this option wins — reference Phase 7 comparison dimensions (PM-relevant
  first), Phase 5 PM signal, Phase 6 Architect validation, and Phase 0 causal chain
  DECISION LEAD TIME values for urgency framing]
CONDITIONS: [2-3 specific conditions that must hold. Reference at least one F-row by ID.]

── PM SIGN-OFF (position 1 — first signatory; business validation precedes technical) ──
ROLE: PM
PM FRAMING: [PM confirms this is the right business decision; expected value of acting
  exceeds INERTIA COST; adoption path is viable; names the TEMPORAL ANCHOR and confirms
  DECISION LEAD TIME is positive for the recommended option]
ARCHITECT VALIDATION: [PM's expectation of what Architect must confirm for this to stand —
  sets the validation frame that the Architect sign-off must respond to]
CONDITIONS: [PM conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row whose trigger condition most directly invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2 — responds to PM frame) ──────────────
ROLE: Architect
PM FRAMING: [Architect explicitly acknowledges PM's business decision and confirms they
  are responding to it, not issuing an independent technical proposal]
ARCHITECT VALIDATION: [Architect confirms technical soundness of the recommended option
  given PM's decision. States the binding technical precondition.]
CONDITIONS: [Architect conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row whose trigger condition most directly invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

All three categories required. OWNER and DEADLINE typed slots in every entry.

── MISSING OPTION ───────────────────────────────────────────────────────
OPTION: [an option not explored in this proposal]
REASON NOT EXPLORED: [why it was excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone — "TBD" and "soon" not acceptable]

── UNWEIGHTED CRITERION ─────────────────────────────────────────────────
CRITERION: [a dimension not weighted or equally weighted]
RECALIBRATION NOTE: [why different weighting is warranted in the next version]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ─────────────────────────────────────────────────────────────
ACTION: [specific follow-up action required]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

Review the amendment tracking table initialized in Phase 0.

If no amendment rows:
  COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.

If amendment rows exist:
  COMPLETION STATUS: [N] amendments logged — see rows above.

Update the COMPLETION STATUS field in Phase 0 to its terminal value now.
```

---

## Scoring Prediction (v9 rubric, /26 denominator)

| Var | Axes | C-32 | C-33 | Predicted score | Ceiling gap |
|-----|------|------|------|-----------------|-------------|
| V-01 | C-32 single | yes | no | ~96.2 | 0.385 short (C-33) |
| V-02 | C-33 single | no | yes | ~96.2 | 0.385 short (C-32) |
| V-03 | phrasing register | yes (via template) | yes (via Phase 0 contract) | ~100.0 | 0 — all six axes structurally enforced by register |
| V-04 | C-32 + C-33 | yes | yes | ~100.0 | 0 |
| V-05 | all six axes | yes | yes | 100.0 | 0 — maximum coverage |

**Note on V-03:** The strict imperative register variation declares both the option anatomy contract and the causal chain contract in Phase 0 (because SHALL/REQUIRED obligations require something to be obligated against). It incidentally covers C-32 and C-33 even though the primary axis is register tone. This is a useful composability signal: register shift and structural contract are not independent when the register shift requires explicit obligation anchors.
