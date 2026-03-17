# draft-proposal — Rubric v8 — Round 8 Variations

Generated: 2026-03-15
Rubric: v8 (C-01 through C-31, denominator /24)
New criteria targeted this round: C-28 (PM-first sign-off), C-29 (table-dominant registers), C-30 (phase manifest at Phase 0), C-31 (DECISION LEAD TIME + ESCALATION FLAG)

---

## Variation Design Summary

| Var | Axis | Primary New Criteria | Hypothesis |
|-----|------|----------------------|------------|
| V-01 | Role sequence — PM-first throughout | C-28 | PM-first ordering at every dual-role phase makes C-28 a byproduct of workflow, not a final-phase rule |
| V-02 | Output format — canonical table headers declared at Phase 0 | C-29 | Declaring canonical column headers at initialization makes C-29 violation structurally impossible |
| V-03 | Lifecycle emphasis — phase manifest at Phase 0 | C-30 | Phase manifest converts C-17 from document-scan to single-block audit and makes C-30 a structural initialization requirement |
| V-04 | PM-first + table-dominant | C-28 + C-29 | PM-first ordering and table-dominant registers reinforce each other — business frame anchors format discipline |
| V-05 | Lifecycle-heavy + inertia-forward | C-30 + C-31 | Phase manifest paired with DECISION LEAD TIME computation creates a causal chain from TEMPORAL ANCHOR to per-alternative urgency scores |

---

## V-01 — Role Sequence: PM-First Throughout

**Variation axis:** Role sequence — PM role leads every phase from framing through sign-off. Architect responds and validates throughout. PM sign-off appears as position 1 in the recommendation phase.

**Hypothesis:** Anchoring PM-first ordering at every dual-role phase (not only sign-off) makes C-28 a structural workflow property rather than a final-phase formatting rule, and produces more coherent business-anchored proposals where the technical evaluation always responds to an established business frame.

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

Initialize two artifacts before any content is authored. Both are live from this point.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────

COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1 — sentinel-first ordering required):

| ID      | Scope    | Predicate — trigger fires when this condition is true                          |
|---------|----------|--------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document   |
| T-01    | Phase 1  | Scout artifact inventory step is absent or merged into another phase           |
| T-02    | Phase 2  | TEMPORAL ANCHOR field missing or contains vague language (soon, near term, etc)|
| T-03    | Phase 2  | INACTION CONSEQUENCE field missing or uses missed-feature language             |
| T-04    | Phase 3  | P*I scoring anchors not defined before any risk entry is scored                |
| T-05    | Phase 4  | Fewer than 3 options, or do-nothing option absent                              |
| T-06    | Phase 4  | Any option missing a required anatomy field (description, pros/cons, risk, effort)|
| T-07    | Phase 4  | Do-nothing option missing typed INERTIA COST in P*I format                    |
| T-08    | Phase 4  | Any non-do-nothing alternative missing typed INERTIA OFFSET                   |
| T-09    | Phase 4  | Any non-do-nothing alternative missing typed DECISION LEAD TIME                |
| T-10    | Phase 4  | Alternative with non-positive DECISION LEAD TIME missing typed ESCALATION FLAG |
| T-11    | Phase 5  | PM perspective phase absent or merged with Architect                           |
| T-12    | Phase 6  | Architect perspective phase absent or merged with PM                           |
| T-13    | Phase 7  | Comparison table absent or dimensions inconsistent across options              |
| T-14    | Phase 8  | Assumption register absent, fewer than 2 A-NN entries, or not in table format |
| T-15    | Phase 9  | Risk register absent, fewer than 2 R-NN entries, or not in table format       |
| T-16    | Phase 10 | Failure mode register absent, fewer than 2 F-NN entries, or not in table format|
| T-17    | Phase 11 | Assumption or risk register appears after recommendation phase                 |
| T-18    | Phase 11 | PREREQUISITE GATE block absent                                                 |
| T-19    | Phase 12 | PM sign-off block is not position 1 in the recommendation sign-off section    |
| T-20    | Phase 12 | PM sign-off block missing typed F-ROW ANCHOR slot                             |
| T-21    | Phase 12 | Architect sign-off block missing typed F-ROW ANCHOR slot                      |
| T-22    | Phase 12 | Recommendation CONDITIONS reference no F-NN ID                                |
| T-23    | Phase 13 | OWNER typed slot absent from any amend entry category template                 |
| T-24    | Phase 13 | DEADLINE typed slot absent from any amend entry category template              |

Amendment Rows (populated live during writing — empty rows confirm T-GUARD enforcement):

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY [PM-led]
════════════════════════════════════════════

PM leads: inventory all scout artifacts available for this topic before any option is
authored. State what was found and what is absent. If no artifacts exist, state this
explicitly and substitute an inline assessment.

| Namespace          | Artifact Found? | Finding or Absence Note                                    |
|--------------------|-----------------|-------------------------------------------------------------|
| scout-feasibility  | yes / no        | [artifact name and key finding, or "absent — inline below"] |
| scout-requirements | yes / no        | [artifact name and key finding, or "absent"]                |
| scout-market       | yes / no        | [artifact name and key finding, or "absent"]                |
| scout-stakeholders | yes / no        | [artifact name and key finding, or "absent"]                |
| scout-compliance   | yes / no        | [artifact name and key finding, or "absent"]                |

If absent: INLINE ASSESSMENT: [feasibility, requirements, and constraints as PM assessment]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING [PM-led; Architect annotates technical constraints]
════════════════════════════════════════════

PM frames the decision using two separate typed fields. Architect may add a TECHNICAL
CONSTRAINT annotation but does not reframe the business question.

DECISION QUESTION: [the precise question being decided — one sentence]

TEMPORAL ANCHOR: [specific named date, sprint name, or event — vague language such as
"soon," "before it is too late," or "in the near term" is prohibited; use a named
specific deadline]

INACTION CONSEQUENCE: [a concrete named outcome if the decision is not made by
TEMPORAL ANCHOR — teams blocked, capability lost, or window closed. Missed-feature
statements do not qualify as consequences. Name the specific team or capability affected.]

ARCHITECT CONSTRAINT ANNOTATION: [technical constraint that bounds or accelerates the
decision — must respond to PM framing, not replace it]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

Define project-specific anchors before any option is scored. These anchors apply to
the risk register (C-16) and all INERTIA COST calculations (C-27).

Probability scale (P = 1–5) for this project:
| P | Meaning |
|---|---------|
| 1 | Remote — < 10% likelihood given current context |
| 2 | Unlikely — 10–25% |
| 3 | Possible — 25–50% |
| 4 | Likely — 50–75% |
| 5 | Near-certain — > 75% |

Impact scale (I = 1–5) for this project:
| I | Meaning |
|---|---------|
| 1 | Negligible — no user-visible or schedule effect |
| 2 | Minor — degraded experience, workaround available within same sprint |
| 3 | Moderate — feature unavailable or delayed one sprint |
| 4 | Significant — multi-sprint delay or stakeholder escalation |
| 5 | Critical — roadmap blocked, revenue or compliance impact |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING [PM frames; Architect validates]
════════════════════════════════════════════

Minimum 3 options. Option 0 must be the do-nothing or status-quo option. PM frames
each option's business context and trade-offs first. Architect validates feasibility
and effort, responding to the PM framing.

Use the following template for each option:

─────────────────────────────────────────
OPTION [N]: [Short Name]
─────────────────────────────────────────
DESCRIPTION: [what this option does]

PM FRAMING: [business rationale, adoption path, key trade-offs — PM speaks first]
ARCHITECT VALIDATION: [technical feasibility, dependencies, constraints — responds to PM]

PROS:
  - [pro 1]
  - [pro 2]

CONS:
  - [con 1]
  - [con 2]

RISK: P: [1-5] × I: [1-5] = P*I: [score] — [risk description using Phase 3 anchors]
EFFORT: Timeline: [named sprint or milestone] | Team: [named role or team] | Dependencies: [any]

[For Option 0 (do-nothing) only — add:]
INERTIA COST: P: [1-5] × I: [1-5] = P*I: [score] per sprint
  (This is the per-sprint cost of not acting, scored on the Phase 3 P*I scale.)

[For each non-do-nothing option — add:]
INERTIA OFFSET: Sprint [N] — the sprint at which cumulative implementation cost equals
  cumulative INERTIA COST of not acting. Acting by this sprint is cost-neutral vs. do-nothing.
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint number] − [INERTIA OFFSET sprint number] = [N] sprints
  (Positive = team has lead time. Zero or negative = inertia trap; see ESCALATION FLAG.)
ESCALATION FLAG: [Required only when DECISION LEAD TIME ≤ 0. State the inertia trap
  condition and name the authority to whom this must be escalated immediately.]
─────────────────────────────────────────

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE [PM-led]
════════════════════════════════════════════

PM provides a standalone business and adoption assessment across all options, independent
of the Architect perspective that follows.

PM RECOMMENDATION SIGNAL: [PM's preferred option based on business factors alone]
PM TRADE-OFF ANALYSIS: [for each non-trivial option, name the business condition under
  which it would be the right choice]
ADOPTION CONCERN: [primary adoption barrier for the PM-preferred option]
BUSINESS RISK: [the business condition that would most directly invalidate PM's signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE [Architect responds to PM framing]
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

Compare all options across consistent dimensions. Use a table. Every option must appear
in every row. PM-relevant dimensions precede technical dimensions.

| Dimension          | Option 0 (Do-Nothing) | Option 1: [Name] | Option 2: [Name] | [Option N] |
|--------------------|----------------------|------------------|------------------|------------|
| PM Signal          |                      |                  |                  |            |
| Architect Signal   |                      |                  |                  |            |
| Effort             |                      |                  |                  |            |
| Timeline           |                      |                  |                  |            |
| Risk P*I           |                      |                  |                  |            |
| Adoption Friction  |                      |                  |                  |            |
| Control            |                      |                  |                  |            |
| INERTIA COST/sprint| [P*I value]          | N/A              | N/A              | N/A        |
| INERTIA OFFSET     | N/A                  | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME | N/A                  | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

Document assumptions that, if invalidated, would change the recommendation.
Minimum 2 entries. Use exact table format with canonical column headers.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 | [assumption text] | [how and when this will be validated — name the method and sprint] |
| A-02 | [assumption text] | [validation method and sprint] |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

Document risks using the numeric P*I scoring defined in Phase 3.
Minimum 2 entries. Use exact table format with canonical column headers.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 | [risk description] | [1-5] | [1-5] | [P×I] | [mitigation action with owner] |
| R-02 | [risk description] | [1-5] | [1-5] | [P×I] | [mitigation action with owner] |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

Document failure modes distinct from the risk register. Use exact canonical field labels.
Minimum 2 entries. Use exact table format.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|-------------------|------------|
| F-01 | [failure mode description] | [the condition under which this failure triggers] | [mitigation or escalation path] |
| F-02 | [failure mode description] | [trigger condition] | [mitigation] |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

Confirm completeness before proceeding. Each item is a named binary: COMPLETE or
NOT COMPLETE. If any item is NOT COMPLETE, fire the corresponding trigger in the
amendment table before proceeding.

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ A-NN entries, table format | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ R-NN entries, table format, numeric P*I | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ F-NN entries, canonical labels, table format | COMPLETE / NOT COMPLETE |
| 4 | Both registers appear in document sequence before this gate | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST present on do-nothing option using Phase 3 P*I scale | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative carries typed INERTIA OFFSET | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives carry typed DECISION LEAD TIME | COMPLETE / NOT COMPLETE |
| 8 | All alternatives with DECISION LEAD TIME ≤ 0 carry typed ESCALATION FLAG | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION [PM sign-off first; Architect sign-off second]
════════════════════════════════════════════

PM sign-off appears at position 1. Business validation precedes technical commitment.

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this option wins — reference Phase 7 comparison dimensions, Phase 5 PM
  signal, and Phase 6 Architect validation]
CONDITIONS: [2–3 specific conditions that must hold for this recommendation to stand.
  Reference at least one F-row by ID (e.g., F-01 must not trigger).]

── PM SIGN-OFF (position 1 — first signatory) ──────────────────────
ROLE: PM
STATEMENT: [PM confirms this is the right business decision and that the expected value
  of acting exceeds the INERTIA COST of not acting]
CONDITIONS: [PM's conditions for this sign-off — must reference at least one F-NN ID]
F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates the PM's
  sign-off — e.g., F-01. This is the failure mode that would reverse the business case.]

── ARCHITECT SIGN-OFF (position 2 — second signatory) ──────────────
ROLE: Architect
STATEMENT: [Architect confirms technical soundness of the recommended option given the
  business decision PM has established]
CONDITIONS: [Architect's conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [the F-row whose trigger condition most directly invalidates the Architect's
  sign-off — may be same or different F-row from PM's anchor. Independence of structure
  is required; divergence of content is not.]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

Identify gaps in this proposal across all three categories. Every entry in every category
carries both an OWNER typed slot and a DEADLINE typed slot.

── MISSING OPTION ──────────────────────────────────────────────────
OPTION: [an option not explored in this proposal]
REASON NOT EXPLORED: [why it was excluded]
OWNER: [named role or person responsible for evaluating this option]
DEADLINE: [specific sprint name, named date, or named milestone — "TBD" and "soon" are
  not acceptable values]

── UNWEIGHTED CRITERION ────────────────────────────────────────────
CRITERION: [a decision dimension that was not weighted or was equally weighted]
RECALIBRATION NOTE: [why this criterion deserves different weighting in the next version]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ────────────────────────────────────────────────────────
ACTION: [specific follow-up action required before or after implementation]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

Review the amendment tracking table initialized in Phase 0. Confirm all open triggers.

If the amendment table contains no rows (all requirements were met during writing):
  COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.

If the amendment table contains rows:
  COMPLETION STATUS: [N] amendments logged — see rows above.

Update the COMPLETION STATUS field in Phase 0 to its terminal value now.
```

---

## V-02 — Output Format: Canonical Table Headers Declared at Phase 0

**Variation axis:** Output format — all three register formats (assumption, risk, failure mode) declared as canonical table requirements at Phase 0 initialization, with exact column headers spelled out before any register content is authored.

**Hypothesis:** Declaring canonical column headers as Phase 0 typed format contracts eliminates C-29 violations by making prose-format registers structurally impossible — the output format is constrained at initialization, not at the phase where the register appears.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). Contributions are distinct. PM addresses the business question; Architect
addresses the technical question.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize three artifacts before any content is authored. All are live from this point.

── REGISTER FORMAT CONTRACTS ─────────────────────────────────────────

The following table formats are the canonical formats for all three registers in this
document. No register may use prose blocks with embedded field labels. If a register
appears in prose format rather than in the canonical table format declared here, trigger
T-14, T-15, or T-16 immediately.

ASSUMPTION REGISTER FORMAT (canonical — use verbatim):
| A-NN | ASSUMPTION | VALIDATION PLAN |

RISK REGISTER FORMAT (canonical — use verbatim):
| R-NN | RISK | P | I | P*I | MITIGATION |

FAILURE MODE REGISTER FORMAT (canonical — use verbatim):
| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |

These column headers are format contracts, not suggestions. Any register using synonyms
("Observable Event" for TRIGGER CONDITION, "Fallback" for MITIGATION, embedded prose
for P/I scores) fails the format contract and triggers T-15 or T-16 as applicable.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────

COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1):

| ID      | Scope    | Predicate                                                                      |
|---------|----------|--------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document   |
| T-01    | Phase 1  | Scout artifact inventory step absent or merged into another phase              |
| T-02    | Phase 2  | TEMPORAL ANCHOR missing or contains vague language                             |
| T-03    | Phase 2  | INACTION CONSEQUENCE missing or uses missed-feature language                   |
| T-04    | Phase 3  | P*I scoring anchors not defined before any risk entry is scored                |
| T-05    | Phase 4  | Fewer than 3 options or do-nothing option absent                               |
| T-06    | Phase 4  | Any option missing required anatomy field                                      |
| T-07    | Phase 4  | Do-nothing option missing typed INERTIA COST                                   |
| T-08    | Phase 4  | Any non-do-nothing alternative missing typed INERTIA OFFSET                   |
| T-09    | Phase 4  | Any non-do-nothing alternative missing typed DECISION LEAD TIME                |
| T-10    | Phase 4  | Alternative with non-positive DECISION LEAD TIME missing typed ESCALATION FLAG |
| T-11    | Phase 5  | PM perspective phase absent or merged with Architect                           |
| T-12    | Phase 6  | Architect perspective phase absent or merged with PM                           |
| T-13    | Phase 7  | Comparison table absent or dimensions inconsistent across options              |
| T-14    | Phase 8  | Assumption register not in canonical table format (A-NN / ASSUMPTION / VALIDATION PLAN)|
| T-15    | Phase 9  | Risk register not in canonical table format (R-NN / RISK / P / I / P*I / MITIGATION)|
| T-16    | Phase 10 | Failure mode register not in canonical table format (F-NN / FAILURE MODE / TRIGGER CONDITION / MITIGATION)|
| T-17    | Phase 11 | Assumption or risk register appears after recommendation phase                 |
| T-18    | Phase 11 | PREREQUISITE GATE block absent                                                 |
| T-19    | Phase 12 | PM sign-off block not at position 1 in the recommendation sign-off section    |
| T-20    | Phase 12 | PM sign-off block missing typed F-ROW ANCHOR slot                             |
| T-21    | Phase 12 | Architect sign-off block missing typed F-ROW ANCHOR slot                      |
| T-22    | Phase 12 | Recommendation CONDITIONS reference no F-NN ID                                |
| T-23    | Phase 13 | OWNER typed slot absent from any amend entry category template                 |
| T-24    | Phase 13 | DEADLINE typed slot absent from any amend entry category template              |

Amendment Rows:

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY
════════════════════════════════════════════

Inventory all scout artifacts available for this topic. This is a discrete step before
option generation. State what was found and what is absent. If no artifacts exist, state
this explicitly and provide an inline assessment.

| Namespace          | Found? | Finding or Absence Note                                    |
|--------------------|--------|-------------------------------------------------------------|
| scout-feasibility  |        |                                                             |
| scout-requirements |        |                                                             |
| scout-market       |        |                                                             |
| scout-stakeholders |        |                                                             |
| scout-compliance   |        |                                                             |

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING
════════════════════════════════════════════

DECISION QUESTION: [the precise question being decided]

TEMPORAL ANCHOR: [specific named date, sprint, or event — vague language prohibited]

INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost, or
  window closed. Missed-feature statements do not qualify.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

Project-specific anchors (required before any risk entry is scored):

| P | Meaning for this project |   | I | Meaning for this project |
|---|--------------------------|   |---|--------------------------|
| 1 | [define P=1]             |   | 1 | [define I=1]             |
| 2 | [define P=2]             |   | 2 | [define I=2]             |
| 3 | [define P=3]             |   | 3 | [define I=3]             |
| 4 | [define P=4]             |   | 4 | [define I=4]             |
| 5 | [define P=5]             |   | 5 | [define I=5]             |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING
════════════════════════════════════════════

Minimum 3 options. Option 0 must be the do-nothing or status-quo option.

OPTION [N]: [Name]
DESCRIPTION: [what this option does]
PROS: [list]
CONS: [list]
RISK: P: [1-5] × I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: [sprint/milestone] | Team: [role/team] | Dependencies: [any]

[Option 0 only:]
INERTIA COST: P: [1-5] × I: [1-5] = P*I: [score] per sprint

[Non-do-nothing options:]
INERTIA OFFSET: Sprint [N] — crossover sprint where implementation cost equals inertia cost
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] − [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME ≤ 0 — name the trap and escalation authority]

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [PM preferred option on business factors]
PM TRADE-OFF ANALYSIS: [conditions under which each non-trivial option would be preferred]
ADOPTION CONCERN: [primary adoption barrier for PM-preferred option]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE
════════════════════════════════════════════

ARCHITECT VALIDATION: [confirms or challenges PM signal from technical standpoint]
TECHNICAL CONSTRAINT: [primary technical constraint bounding option selection]
DEPENDENCY NOTE: [blocking dependency for technically preferred option]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

| Dimension          | Option 0 | Option 1: [Name] | Option 2: [Name] | [Option N] |
|--------------------|----------|------------------|------------------|------------|
| Effort             |          |                  |                  |            |
| Timeline           |          |                  |                  |            |
| Risk P*I           |          |                  |                  |            |
| Control            |          |                  |                  |            |
| Adoption Friction  |          |                  |                  |            |
| INERTIA COST/sprint| [P*I]    | N/A              | N/A              | N/A        |
| INERTIA OFFSET     | N/A      | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME | N/A      | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

Use the canonical format declared in Phase 0. Minimum 2 entries.
Prose format with embedded field labels is not acceptable.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 |            |                 |
| A-02 |            |                 |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

Use the canonical format declared in Phase 0. Minimum 2 entries.
Scores use Phase 3 anchors. Holistic L/M/H labels are not acceptable.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 |      |   |   |     |            |
| R-02 |      |   |   |     |            |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

Use the canonical format declared in Phase 0. Minimum 2 entries.
The field labels FAILURE MODE, TRIGGER CONDITION, and MITIGATION are exact — synonyms
are not acceptable.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|-------------------|------------|
| F-01 |             |                   |            |
| F-02 |             |                   |            |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ A-NN entries, canonical table format (A-NN / ASSUMPTION / VALIDATION PLAN) | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ R-NN entries, canonical table format, numeric P*I | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ F-NN entries, canonical table format (F-NN / FAILURE MODE / TRIGGER CONDITION / MITIGATION) | COMPLETE / NOT COMPLETE |
| 4 | Both registers in document sequence before this gate | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST on do-nothing option | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative has INERTIA OFFSET | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives have DECISION LEAD TIME | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME ≤ 0 alternatives have ESCALATION FLAG | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this option wins — reference comparison dimensions and register findings]
CONDITIONS: [2–3 conditions that must hold; reference at least one F-NN ID]

── PM SIGN-OFF (position 1) ────────────────────────────────────────
ROLE: PM
STATEMENT: [business validation — this is the right decision]
CONDITIONS: [PM conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID whose trigger condition most directly invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2) ─────────────────────────────────
ROLE: Architect
STATEMENT: [technical validation — this is the right design given PM's decision]
CONDITIONS: [Architect conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID whose trigger condition most directly invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

All three categories required. OWNER and DEADLINE appear as typed slots in every entry
across all three categories.

── MISSING OPTION ──────────────────────────────────────────────────
OPTION: [option not explored]
REASON NOT EXPLORED: [why excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone — not "TBD" or "soon"]

── UNWEIGHTED CRITERION ────────────────────────────────────────────
CRITERION: [dimension not weighted or equally weighted]
RECALIBRATION NOTE: [why different weighting is warranted]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ────────────────────────────────────────────────────────
ACTION: [specific follow-up action]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no amendment rows were added (table is empty):
  COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.

If amendment rows exist:
  COMPLETION STATUS: [N] amendments logged — see rows above.

Update the COMPLETION STATUS field in Phase 0 to its terminal value.
```

---

## V-03 — Lifecycle Emphasis: Phase Manifest at Phase 0

**Variation axis:** Lifecycle emphasis — Phase 0 produces a phase manifest block listing every phase in the document by sequence number and name before any content is authored. The manifest enables single-block verification of lifecycle ordering.

**Hypothesis:** A phase manifest at Phase 0 converts C-30 compliance from an aspirational criterion into a structural initialization requirement, and converts C-17 lifecycle-ordering verification (registers precede recommendation) from a document scan into a single-block read. When the manifest is complete and accurate, a reviewer can confirm that register phases appear before the recommendation phase without scanning the document.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). Contributions are distinct.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize three artifacts before any content is authored. All are live from this point.

── PHASE MANIFEST ────────────────────────────────────────────────────

Every phase in this document is listed below. The manifest is complete before Phase 1
begins. A reviewer can confirm lifecycle ordering by reading this manifest, not by
scanning the document.

| # | Phase Name | Purpose |
|---|------------|---------|
| 0  | Initialization | Amendment table, phase manifest, COMPLETION STATUS |
| 1  | Scout Artifact Inventory | List found and absent artifacts before option generation |
| 2  | Decision Framing | TEMPORAL ANCHOR + INACTION CONSEQUENCE before options |
| 3  | P*I Scoring Anchors | Project-specific probability and impact definitions |
| 4  | Options Authoring | 3+ options with complete anatomy, INERTIA fields, DECISION LEAD TIME |
| 5  | PM Perspective | Business and adoption assessment (standalone) |
| 6  | Architect Perspective | Technical constraint and feasibility assessment (standalone) |
| 7  | Comparison Table | Options compared on consistent dimensions |
| 8  | Assumption Register | A-NN entries with validation plans — BEFORE recommendation |
| 9  | Risk Register | R-NN entries with numeric P*I — BEFORE recommendation |
| 10 | Failure Mode Register | F-NN entries with canonical labels — BEFORE recommendation |
| 11 | Prerequisite Gate | Confirm register completeness and ordering before sign-off |
| 12 | Recommendation | PM sign-off (position 1), Architect sign-off (position 2) |
| 13 | Amend Phase | Three-category gaps: missing option, unweighted criterion, follow-up |
| 14 | Amendment Table Finalization | Update COMPLETION STATUS to terminal value |

LIFECYCLE ORDERING VERIFICATION (from manifest):
- Phase 8 (Assumption Register): before Phase 12 (Recommendation) ✓
- Phase 9 (Risk Register): before Phase 12 (Recommendation) ✓
- Phase 10 (Failure Mode Register): before Phase 12 (Recommendation) ✓
- Phase 11 (Prerequisite Gate): immediately before Phase 12 (Recommendation) ✓

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────

COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1):

| ID      | Scope    | Predicate                                                                      |
|---------|----------|--------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document   |
| T-01    | Phase 0  | Phase manifest absent from Phase 0 or missing any phase present in document   |
| T-02    | Phase 0  | Phase manifest lists a phase not present in the document                       |
| T-03    | Phase 1  | Scout artifact inventory step absent or merged into another phase              |
| T-04    | Phase 2  | TEMPORAL ANCHOR missing or contains vague language                             |
| T-05    | Phase 2  | INACTION CONSEQUENCE missing or uses missed-feature language                   |
| T-06    | Phase 3  | P*I scoring anchors not defined before any risk entry is scored                |
| T-07    | Phase 4  | Fewer than 3 options or do-nothing option absent                               |
| T-08    | Phase 4  | Any option missing required anatomy field                                      |
| T-09    | Phase 4  | Do-nothing option missing typed INERTIA COST                                   |
| T-10    | Phase 4  | Any non-do-nothing alternative missing typed INERTIA OFFSET                   |
| T-11    | Phase 4  | Any non-do-nothing alternative missing typed DECISION LEAD TIME                |
| T-12    | Phase 4  | Alternative with non-positive DECISION LEAD TIME missing typed ESCALATION FLAG |
| T-13    | Phase 5  | PM perspective phase absent or merged with Architect                           |
| T-14    | Phase 6  | Architect perspective phase absent or merged with PM                           |
| T-15    | Phase 7  | Comparison table absent or dimensions inconsistent                             |
| T-16    | Phase 8  | Assumption register absent, fewer than 2 entries, or not in table format      |
| T-17    | Phase 9  | Risk register absent, fewer than 2 entries, or not in table format            |
| T-18    | Phase 10 | Failure mode register absent, fewer than 2 entries, or not in table format    |
| T-19    | Phase 11 | Register appears after recommendation (manifest ordering violated)             |
| T-20    | Phase 11 | Prerequisite Gate block absent                                                 |
| T-21    | Phase 12 | PM sign-off not at position 1                                                  |
| T-22    | Phase 12 | PM sign-off missing typed F-ROW ANCHOR slot                                   |
| T-23    | Phase 12 | Architect sign-off missing typed F-ROW ANCHOR slot                            |
| T-24    | Phase 12 | Recommendation CONDITIONS reference no F-NN ID                                |
| T-25    | Phase 13 | OWNER typed slot absent from any amend category template                       |
| T-26    | Phase 13 | DEADLINE typed slot absent from any amend category template                    |

Amendment Rows:

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY
════════════════════════════════════════════

This is a discrete step (see Phase Manifest, Phase 1). Not merged with any other phase.

| Namespace          | Found? | Finding or Absence Note                                    |
|--------------------|--------|-------------------------------------------------------------|
| scout-feasibility  |        |                                                             |
| scout-requirements |        |                                                             |
| scout-market       |        |                                                             |
| scout-stakeholders |        |                                                             |
| scout-compliance   |        |                                                             |

If no artifacts found: INLINE ASSESSMENT: [substitute assessment here]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING
════════════════════════════════════════════

Both typed fields required before options section (see Phase Manifest lifecycle ordering).

DECISION QUESTION: [the precise question being decided]
TEMPORAL ANCHOR: [specific named date, sprint, or event — vague language prohibited]
INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost, or window
  closed. Missed-feature statements do not qualify.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

| P | Meaning | | I | Meaning |
|---|---------|  |---|---------|
| 1 | [P=1]   | | 1 | [I=1]   |
| 2 | [P=2]   | | 2 | [I=2]   |
| 3 | [P=3]   | | 3 | [I=3]   |
| 4 | [P=4]   | | 4 | [I=4]   |
| 5 | [P=5]   | | 5 | [I=5]   |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING
════════════════════════════════════════════

Minimum 3 options. Option 0 must be do-nothing.

OPTION [N]: [Name]
DESCRIPTION: [what this option does]
PROS: [list]
CONS: [list]
RISK: P: [1-5] × I: [1-5] = P*I: [score] — [description]
EFFORT: Timeline: [sprint/milestone] | Team: [role/team]

[Option 0 only:]
INERTIA COST: P: [1-5] × I: [1-5] = P*I: [score] per sprint

[Non-do-nothing options:]
INERTIA OFFSET: Sprint [N]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] − [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME ≤ 0]

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [PM preferred option]
PM TRADE-OFF ANALYSIS: [conditions favoring each non-trivial option]
ADOPTION CONCERN: [primary adoption barrier]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE
════════════════════════════════════════════

ARCHITECT VALIDATION: [confirms or challenges PM signal]
TECHNICAL CONSTRAINT: [primary technical constraint]
DEPENDENCY NOTE: [blocking dependency]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

| Dimension          | Option 0 | Option 1: [Name] | Option 2: [Name] | [Option N] |
|--------------------|----------|------------------|------------------|------------|
| Effort             |          |                  |                  |            |
| Timeline           |          |                  |                  |            |
| Risk P*I           |          |                  |                  |            |
| Control            |          |                  |                  |            |
| Adoption Friction  |          |                  |                  |            |
| INERTIA COST/sprint| [P*I]    | N/A              | N/A              | N/A        |
| INERTIA OFFSET     | N/A      | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME | N/A      | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

This phase precedes the recommendation phase (see Phase Manifest, Phase 8 before Phase 12).
Minimum 2 entries. Table format required.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 |            |                 |
| A-02 |            |                 |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

This phase precedes the recommendation phase (see Phase Manifest, Phase 9 before Phase 12).
Minimum 2 entries. Numeric P*I using Phase 3 anchors. Table format required.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 |      |   |   |     |            |
| R-02 |      |   |   |     |            |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

This phase precedes the recommendation phase (see Phase Manifest, Phase 10 before Phase 12).
Minimum 2 entries. Canonical labels required. Table format required.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|-------------------|------------|
| F-01 |             |                   |            |
| F-02 |             |                   |            |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

Immediately before Phase 12 (see Phase Manifest). Each item is a named binary.

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ A-NN, table format, before this gate | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ R-NN, numeric P*I, table format, before this gate | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ F-NN, canonical labels, table format, before this gate | COMPLETE / NOT COMPLETE |
| 4 | Phase manifest in Phase 0 lists all phases in document | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST on do-nothing option | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative has INERTIA OFFSET | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives have DECISION LEAD TIME | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME ≤ 0 alternatives have ESCALATION FLAG | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this option wins]
CONDITIONS: [2–3 conditions; reference at least one F-NN ID]

── PM SIGN-OFF (position 1) ────────────────────────────────────────
ROLE: PM
STATEMENT: [business validation]
CONDITIONS: [PM conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID that invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2) ─────────────────────────────────
ROLE: Architect
STATEMENT: [technical validation]
CONDITIONS: [Architect conditions — must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID that invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

── MISSING OPTION ──────────────────────────────────────────────────
OPTION: [option not explored]
REASON NOT EXPLORED: [why excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── UNWEIGHTED CRITERION ────────────────────────────────────────────
CRITERION: [dimension not weighted]
RECALIBRATION NOTE: [why different weighting is warranted]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ────────────────────────────────────────────────────────
ACTION: [specific follow-up action]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no amendment rows:
  COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.
If amendment rows exist:
  COMPLETION STATUS: [N] amendments logged — see rows above.

Update Phase 0 COMPLETION STATUS to terminal value.
```

---

## V-04 — PM-First + Table-Dominant (C-28 + C-29 Combination)

**Variation axis:** Role sequence + Output format — PM leads every phase from framing through sign-off; all three register formats declared as canonical table contracts at Phase 0 initialization.

**Hypothesis:** PM-first ordering and table-dominant registers reinforce each other. When PM leads the framing phase, the business question is established before format decisions are made. Declaring canonical table column headers at Phase 0 as format contracts — before any register content is authored — means the format discipline is live from the moment PM frames the decision. C-28 and C-29 are structurally coupled rather than independent patches.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLE ORDERING: PM leads. Architect responds and validates. This ordering applies throughout:
decision framing, option authoring, perspective phases, and sign-off. PM speaks first.
Architect extends or challenges. PM sign-off is position 1 in every sign-off section.

REGISTER FORMAT CONTRACTS: All three registers use canonical table format. The column
headers below are exact — prose blocks with embedded field labels are not acceptable.

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

── REGISTER FORMAT CONTRACTS (declared at initialization — live from Phase 0) ────────

Assumption register: | A-NN | ASSUMPTION | VALIDATION PLAN |
Risk register:       | R-NN | RISK | P | I | P*I | MITIGATION |
Failure mode register:| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |

These are format contracts. Any register using prose format or synonym column headers
triggers T-14, T-15, or T-16 immediately.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────

COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1):

| ID      | Scope    | Predicate                                                                      |
|---------|----------|--------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document   |
| T-01    | Phase 1  | Scout artifact inventory step absent or merged into another phase              |
| T-02    | Phase 2  | TEMPORAL ANCHOR missing or vague                                               |
| T-03    | Phase 2  | INACTION CONSEQUENCE missing or uses missed-feature language                   |
| T-04    | Phase 3  | P*I anchors not defined before scoring begins                                  |
| T-05    | Phase 4  | Fewer than 3 options or do-nothing absent                                      |
| T-06    | Phase 4  | Any option missing required anatomy field                                      |
| T-07    | Phase 4  | Do-nothing missing INERTIA COST                                                |
| T-08    | Phase 4  | Alternative missing INERTIA OFFSET                                             |
| T-09    | Phase 4  | Alternative missing DECISION LEAD TIME                                         |
| T-10    | Phase 4  | DECISION LEAD TIME ≤ 0 alternative missing ESCALATION FLAG                    |
| T-11    | Phase 5  | PM perspective absent or merged                                                |
| T-12    | Phase 6  | Architect perspective absent or merged                                         |
| T-13    | Phase 7  | Comparison table absent or inconsistent dimensions                             |
| T-14    | Phase 8  | Assumption register not in canonical table (A-NN / ASSUMPTION / VALIDATION PLAN)|
| T-15    | Phase 9  | Risk register not in canonical table (R-NN / RISK / P / I / P*I / MITIGATION) |
| T-16    | Phase 10 | Failure mode register not in canonical table (F-NN / FAILURE MODE / TRIGGER CONDITION / MITIGATION)|
| T-17    | Phase 11 | Register appears after recommendation                                          |
| T-18    | Phase 11 | Prerequisite Gate absent                                                       |
| T-19    | Phase 12 | PM sign-off not at position 1                                                  |
| T-20    | Phase 12 | PM sign-off missing F-ROW ANCHOR slot                                          |
| T-21    | Phase 12 | Architect sign-off missing F-ROW ANCHOR slot                                   |
| T-22    | Phase 12 | CONDITIONS reference no F-NN ID                                                |
| T-23    | Phase 13 | OWNER slot absent from any amend category template                             |
| T-24    | Phase 13 | DEADLINE slot absent from any amend category template                          |

Amendment Rows:

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY [PM-led]
════════════════════════════════════════════

PM leads inventory. Discrete step before option generation.

| Namespace          | Found? | Finding or Absence Note |
|--------------------|--------|--------------------------|
| scout-feasibility  |        |                          |
| scout-requirements |        |                          |
| scout-market       |        |                          |
| scout-stakeholders |        |                          |
| scout-compliance   |        |                          |

If absent: INLINE ASSESSMENT: [PM-led inline assessment]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING [PM leads; Architect annotates constraints]
════════════════════════════════════════════

DECISION QUESTION: [the precise question]
TEMPORAL ANCHOR: [specific named date, sprint, or event]
INACTION CONSEQUENCE: [concrete named outcome — not a missed-feature statement]
ARCHITECT CONSTRAINT ANNOTATION: [technical constraint responding to PM framing]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

| P | Meaning | | I | Meaning |
|---|---------|  |---|---------|
| 1 | [P=1]   | | 1 | [I=1]   |
| 2 | [P=2]   | | 2 | [I=2]   |
| 3 | [P=3]   | | 3 | [I=3]   |
| 4 | [P=4]   | | 4 | [I=4]   |
| 5 | [P=5]   | | 5 | [I=5]   |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING [PM frames; Architect validates]
════════════════════════════════════════════

Minimum 3 options. Option 0 is do-nothing.

OPTION [N]: [Name]
DESCRIPTION: [what this option does]
PM FRAMING: [business rationale — PM speaks first]
ARCHITECT VALIDATION: [technical feasibility — responds to PM]
PROS: [list]
CONS: [list]
RISK: P: [1-5] × I: [1-5] = P*I: [score] — [description using Phase 3 anchors]
EFFORT: Timeline: [sprint/milestone] | Team: [role/team] | Dependencies: [any]

[Option 0 only:]
INERTIA COST: P: [1-5] × I: [1-5] = P*I: [score] per sprint

[Non-do-nothing options:]
INERTIA OFFSET: Sprint [N]
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint] − [INERTIA OFFSET sprint] = [N] sprints
ESCALATION FLAG: [Required when DECISION LEAD TIME ≤ 0]

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE [PM-led]
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [preferred option on business factors]
PM TRADE-OFF ANALYSIS: [conditions favoring each non-trivial option]
ADOPTION CONCERN: [primary adoption barrier]
BUSINESS RISK: [condition most likely to reverse PM signal]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE [Architect responds to PM]
════════════════════════════════════════════

ARCHITECT VALIDATION: [confirms or challenges PM recommendation signal]
TECHNICAL CONSTRAINT: [primary technical constraint]
DEPENDENCY NOTE: [blocking dependency]
TECHNICAL RISK: [condition most likely to reverse Architect validation]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

PM-relevant dimensions first, then technical dimensions.

| Dimension          | Option 0 | Option 1: [Name] | Option 2: [Name] | [Option N] |
|--------------------|----------|------------------|------------------|------------|
| PM Signal          |          |                  |                  |            |
| Architect Signal   |          |                  |                  |            |
| Adoption Friction  |          |                  |                  |            |
| Effort             |          |                  |                  |            |
| Timeline           |          |                  |                  |            |
| Risk P*I           |          |                  |                  |            |
| Control            |          |                  |                  |            |
| INERTIA COST/sprint| [P*I]    | N/A              | N/A              | N/A        |
| INERTIA OFFSET     | N/A      | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME | N/A      | [N] sprints      | [N] sprints      | [N] sprints|

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

Canonical format (declared Phase 0). Prose format not acceptable. Minimum 2 entries.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 |            |                 |
| A-02 |            |                 |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

Canonical format (declared Phase 0). Numeric P*I only. Minimum 2 entries.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 |      |   |   |     |            |
| R-02 |      |   |   |     |            |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

Canonical format (declared Phase 0). Exact labels: FAILURE MODE / TRIGGER CONDITION /
MITIGATION. Minimum 2 entries.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|-------------------|------------|
| F-01 |             |                   |            |
| F-02 |             |                   |            |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ entries, canonical table format | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ entries, canonical table format, numeric P*I | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ entries, canonical table format | COMPLETE / NOT COMPLETE |
| 4 | All three registers before this gate in document sequence | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST on do-nothing option | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative has INERTIA OFFSET | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives have DECISION LEAD TIME | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME ≤ 0 alternatives have ESCALATION FLAG | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION [PM sign-off position 1; Architect position 2]
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this wins — reference PM signal, Architect validation, and Phase 7 table]
CONDITIONS: [2–3 conditions; reference at least one F-NN ID]

── PM SIGN-OFF (position 1 — business validation first) ─────────────
ROLE: PM
STATEMENT: [PM confirms this is the right business decision — PM-first ordering reflects
  causal priority: whether to act precedes how to act]
CONDITIONS: [PM conditions; must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID whose trigger most directly invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2 — technical commitment follows) ───
ROLE: Architect
STATEMENT: [Architect confirms technical soundness given PM's established decision]
CONDITIONS: [Architect conditions; must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID whose trigger most directly invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

── MISSING OPTION ──────────────────────────────────────────────────
OPTION: [option not explored]
REASON NOT EXPLORED: [why excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── UNWEIGHTED CRITERION ────────────────────────────────────────────
CRITERION: [dimension not weighted]
RECALIBRATION NOTE: [recalibration rationale]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ────────────────────────────────────────────────────────
ACTION: [specific follow-up action]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no rows: COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.
If rows exist: COMPLETION STATUS: [N] amendments logged — see rows above.
Update Phase 0 COMPLETION STATUS now.
```

---

## V-05 — Lifecycle-Heavy + Inertia-Forward (C-30 + C-31 Combination)

**Variation axis:** Lifecycle emphasis + Inertia framing — Phase 0 produces a complete phase manifest listing all phases, and DECISION LEAD TIME is treated as a Phase 0 declared output requirement alongside the phase manifest. INERTIA COST, INERTIA OFFSET, and DECISION LEAD TIME form a causal chain declared at initialization, not assembled retrospectively.

**Hypothesis:** Pairing the phase manifest (C-30) with DECISION LEAD TIME declared as a mandatory Phase 4 output (C-31) creates a structural causal chain from TEMPORAL ANCHOR (Phase 2) through INERTIA OFFSET (Phase 4) to DECISION LEAD TIME (Phase 4 computed field). When both are declared at Phase 0, they reinforce each other: the phase manifest makes the lifecycle ordering auditable, and the inertia-chain declaration ensures DECISION LEAD TIME computation is a structural requirement rather than an optional depth signal.

---

```
You are executing the `draft-proposal` skill. Author a complete proposal or ADR for the
requested topic.

ROLES: PM (business and adoption trade-offs) and Architect (technical constraints and
feasibility). Contributions are distinct.

INERTIA-CHAIN CONTRACT: Every proposal must surface the computable urgency of each
alternative. The chain is: TEMPORAL ANCHOR (Phase 2) → INERTIA OFFSET (Phase 4) →
DECISION LEAD TIME (Phase 4 computed) → ESCALATION FLAG (Phase 4 when non-positive).
This chain is declared at Phase 0 and must be complete by Phase 11 (Prerequisite Gate).

════════════════════════════════════════════
PHASE 0 — INITIALIZATION
════════════════════════════════════════════

Initialize four artifacts before any content is authored. All are live from this point.

── PHASE MANIFEST ────────────────────────────────────────────────────

Every phase in this document is listed below. Completeness required: every phase that
appears in the document must appear here; no phase listed here may be absent from the
document. Lifecycle ordering (C-17) is verifiable by reading this manifest.

| # | Phase Name | Purpose | Lifecycle Role |
|---|------------|---------|----------------|
| 0  | Initialization | Phase manifest, inertia-chain contract, amendment table | Setup |
| 1  | Scout Artifact Inventory | Found and absent artifacts — discrete step | Before options |
| 2  | Decision Framing | TEMPORAL ANCHOR + INACTION CONSEQUENCE | Before options |
| 3  | P*I Scoring Anchors | Project-specific P and I definitions | Before scoring |
| 4  | Options Authoring | 3+ options; INERTIA COST (Option 0); INERTIA OFFSET, DECISION LEAD TIME (alternatives) | Options |
| 5  | PM Perspective | Standalone business and adoption assessment | Analysis |
| 6  | Architect Perspective | Standalone technical constraint assessment | Analysis |
| 7  | Comparison Table | All options on consistent dimensions including inertia fields | Analysis |
| 8  | Assumption Register | A-NN entries — PRECEDES recommendation | Register |
| 9  | Risk Register | R-NN entries, numeric P*I — PRECEDES recommendation | Register |
| 10 | Failure Mode Register | F-NN entries, canonical labels — PRECEDES recommendation | Register |
| 11 | Prerequisite Gate | Confirm register ordering and inertia-chain completeness | Gate |
| 12 | Recommendation | PM sign-off (position 1), Architect sign-off (position 2) | Decision |
| 13 | Amend Phase | Three-category gaps with OWNER and DEADLINE | Self-audit |
| 14 | Amendment Table Finalization | COMPLETION STATUS terminal value | Close |

LIFECYCLE ORDERING (from manifest — no document scan required):
- Phases 8, 9, 10 (registers) precede Phase 12 (recommendation) ✓
- Phase 11 (gate) immediately precedes Phase 12 (recommendation) ✓

── INERTIA-CHAIN DECLARATION ─────────────────────────────────────────

The inertia chain links the named deadline (TEMPORAL ANCHOR, Phase 2) to the per-
alternative urgency score (DECISION LEAD TIME, Phase 4). The chain is:

  INERTIA COST (Option 0)  = P × I per sprint [using Phase 3 anchors]
  INERTIA OFFSET (Options 1+) = Sprint N where cumulative implementation cost = cumulative inertia cost
  DECISION LEAD TIME       = TEMPORAL ANCHOR sprint − INERTIA OFFSET sprint
  ESCALATION FLAG          = Required when DECISION LEAD TIME ≤ 0 (inertia trap)

Every non-do-nothing alternative must complete this chain at Phase 4. The Prerequisite
Gate (Phase 11) confirms chain completeness before sign-off.

── AMENDMENT TRACKING TABLE ──────────────────────────────────────────

COMPLETION STATUS: PENDING

Trigger Definitions (T-GUARD is position 1):

| ID      | Scope    | Predicate                                                                      |
|---------|----------|--------------------------------------------------------------------------------|
| T-GUARD | Catch-all| Any required typed slot, phase block, or gate item absent from the document   |
| T-01    | Phase 0  | Phase manifest absent from Phase 0 or structurally incomplete (missing/added phase)|
| T-02    | Phase 1  | Scout artifact inventory absent or merged into another phase                   |
| T-03    | Phase 2  | TEMPORAL ANCHOR missing or vague                                               |
| T-04    | Phase 2  | INACTION CONSEQUENCE missing or uses missed-feature language                   |
| T-05    | Phase 3  | P*I anchors not defined before scoring                                         |
| T-06    | Phase 4  | Fewer than 3 options or do-nothing absent                                      |
| T-07    | Phase 4  | Any option missing required anatomy field                                      |
| T-08    | Phase 4  | Do-nothing missing INERTIA COST (inertia-chain break: cost)                   |
| T-09    | Phase 4  | Any alternative missing INERTIA OFFSET (inertia-chain break: crossover)       |
| T-10    | Phase 4  | Any alternative missing DECISION LEAD TIME (inertia-chain break: lead time)   |
| T-11    | Phase 4  | DECISION LEAD TIME ≤ 0 alternative missing ESCALATION FLAG (inertia-chain break: trap)|
| T-12    | Phase 5  | PM perspective absent or merged with Architect                                 |
| T-13    | Phase 6  | Architect perspective absent or merged with PM                                 |
| T-14    | Phase 7  | Comparison table absent or dimensions inconsistent                             |
| T-15    | Phase 8  | Assumption register absent, fewer than 2 entries, or not in table format      |
| T-16    | Phase 9  | Risk register absent, fewer than 2 entries, or not in table format            |
| T-17    | Phase 10 | Failure mode register absent, fewer than 2 entries, or not in table format    |
| T-18    | Phase 11 | Register sequence violated (phase manifest ordering violated)                  |
| T-19    | Phase 11 | Prerequisite Gate absent                                                       |
| T-20    | Phase 12 | PM sign-off not at position 1                                                  |
| T-21    | Phase 12 | PM sign-off missing F-ROW ANCHOR slot                                          |
| T-22    | Phase 12 | Architect sign-off missing F-ROW ANCHOR slot                                   |
| T-23    | Phase 12 | CONDITIONS reference no F-NN ID                                                |
| T-24    | Phase 13 | OWNER slot absent from any amend category template                             |
| T-25    | Phase 13 | DEADLINE slot absent from any amend category template                          |

Amendment Rows:

| Row ID | TRIGGER | Phase | Description |
|--------|---------|-------|-------------|
|        |         |       |             |

════════════════════════════════════════════
PHASE 1 — SCOUT ARTIFACT INVENTORY
════════════════════════════════════════════

Discrete step (Phase Manifest, Phase 1). Inventory before option generation.

| Namespace          | Found? | Finding or Absence Note |
|--------------------|--------|--------------------------|
| scout-feasibility  |        |                          |
| scout-requirements |        |                          |
| scout-market       |        |                          |
| scout-stakeholders |        |                          |
| scout-compliance   |        |                          |

If absent: INLINE ASSESSMENT: [substitute here]

════════════════════════════════════════════
PHASE 2 — DECISION FRAMING
════════════════════════════════════════════

TEMPORAL ANCHOR provides the deadline for DECISION LEAD TIME computation in Phase 4.
Both typed fields required before options.

DECISION QUESTION: [the precise question]
TEMPORAL ANCHOR: [specific named date, sprint, or event — this value feeds the
  DECISION LEAD TIME computation: DECISION LEAD TIME = TEMPORAL ANCHOR sprint − INERTIA OFFSET sprint]
INACTION CONSEQUENCE: [concrete named outcome — teams blocked, capability lost, or
  window closed. Not a missed-feature statement.]

════════════════════════════════════════════
PHASE 3 — P*I SCORING ANCHORS
════════════════════════════════════════════

Anchors apply to both risk register entries and INERTIA COST computations.

| P | Meaning | | I | Meaning |
|---|---------|  |---|---------|
| 1 | [P=1]   | | 1 | [I=1]   |
| 2 | [P=2]   | | 2 | [I=2]   |
| 3 | [P=3]   | | 3 | [I=3]   |
| 4 | [P=4]   | | 4 | [I=4]   |
| 5 | [P=5]   | | 5 | [I=5]   |

════════════════════════════════════════════
PHASE 4 — OPTIONS AUTHORING
════════════════════════════════════════════

Complete the inertia chain for every option. Option 0 provides INERTIA COST.
Each non-do-nothing option provides INERTIA OFFSET and DECISION LEAD TIME.

OPTION [N]: [Name]
DESCRIPTION: [what this option does]
PROS: [list]
CONS: [list]
RISK: P: [1-5] × I: [1-5] = P*I: [score] — [description using Phase 3 anchors]
EFFORT: Timeline: [sprint/milestone] | Team: [role/team] | Dependencies: [any]

[Option 0 only — INERTIA COST fills the cost-baseline position in the chain:]
INERTIA COST: P: [1-5] × I: [1-5] = P*I: [score] per sprint
  Using Phase 3 anchors. This is the per-sprint cost the project pays by not acting.

[Non-do-nothing options — complete the inertia chain:]
INERTIA OFFSET: Sprint [N]
  The sprint at which cumulative implementation cost equals cumulative INERTIA COST.
  Acting before this sprint is cost-advantaged relative to do-nothing.
DECISION LEAD TIME: [TEMPORAL ANCHOR sprint number from Phase 2] − [INERTIA OFFSET sprint] = [N] sprints
  Positive: team has lead time. Zero or negative: inertia trap (see ESCALATION FLAG).
  Computation must be explicit — listing TEMPORAL ANCHOR and INERTIA OFFSET without
  computing DECISION LEAD TIME does not satisfy this field.
ESCALATION FLAG: [Required when DECISION LEAD TIME ≤ 0. Name the inertia trap condition
  (e.g., "crossover point is past TEMPORAL ANCHOR") and the authority to escalate to.
  Required field — a zero or negative lead time with no ESCALATION FLAG breaks the chain.]

════════════════════════════════════════════
PHASE 5 — PM PERSPECTIVE
════════════════════════════════════════════

PM RECOMMENDATION SIGNAL: [preferred option on business factors]
PM TRADE-OFF ANALYSIS: [conditions favoring each non-trivial option]
ADOPTION CONCERN: [primary adoption barrier]

════════════════════════════════════════════
PHASE 6 — ARCHITECT PERSPECTIVE
════════════════════════════════════════════

ARCHITECT VALIDATION: [confirms or challenges PM signal]
TECHNICAL CONSTRAINT: [primary technical constraint]
DEPENDENCY NOTE: [blocking dependency]

════════════════════════════════════════════
PHASE 7 — COMPARISON TABLE
════════════════════════════════════════════

| Dimension          | Option 0 | Option 1: [Name] | Option 2: [Name] | [Option N] |
|--------------------|----------|------------------|------------------|------------|
| Effort             |          |                  |                  |            |
| Timeline           |          |                  |                  |            |
| Risk P*I           |          |                  |                  |            |
| Control            |          |                  |                  |            |
| Adoption Friction  |          |                  |                  |            |
| INERTIA COST/sprint| [P*I]    | N/A              | N/A              | N/A        |
| INERTIA OFFSET     | N/A      | Sprint [N]       | Sprint [N]       | Sprint [N] |
| DECISION LEAD TIME | N/A      | [N] sprints      | [N] sprints      | [N] sprints|
| ESCALATION FLAG    | N/A      | [yes/no]         | [yes/no]         | [yes/no]   |

════════════════════════════════════════════
PHASE 8 — ASSUMPTION REGISTER
════════════════════════════════════════════

(Phase Manifest: Phase 8 precedes Phase 12.) Minimum 2 entries. Table format required.

| A-NN | ASSUMPTION | VALIDATION PLAN |
|------|------------|-----------------|
| A-01 |            |                 |
| A-02 |            |                 |

════════════════════════════════════════════
PHASE 9 — RISK REGISTER
════════════════════════════════════════════

(Phase Manifest: Phase 9 precedes Phase 12.) Minimum 2 entries. Numeric P*I. Table required.

| R-NN | RISK | P | I | P*I | MITIGATION |
|------|------|---|---|-----|------------|
| R-01 |      |   |   |     |            |
| R-02 |      |   |   |     |            |

════════════════════════════════════════════
PHASE 10 — FAILURE MODE REGISTER
════════════════════════════════════════════

(Phase Manifest: Phase 10 precedes Phase 12.) Minimum 2 entries. Canonical labels. Table required.

| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |
|------|-------------|-------------------|------------|
| F-01 |             |                   |            |
| F-02 |             |                   |            |

════════════════════════════════════════════
PHASE 11 — PREREQUISITE GATE
════════════════════════════════════════════

(Phase Manifest: Phase 11 immediately precedes Phase 12.)

| # | Check | Status |
|---|-------|--------|
| 1 | Assumption register: 2+ A-NN, table format, before this gate | COMPLETE / NOT COMPLETE |
| 2 | Risk register: 2+ R-NN, numeric P*I, table format, before this gate | COMPLETE / NOT COMPLETE |
| 3 | Failure mode register: 2+ F-NN, canonical labels, table format, before this gate | COMPLETE / NOT COMPLETE |
| 4 | Phase manifest in Phase 0 lists all phases; ordering matches document | COMPLETE / NOT COMPLETE |
| 5 | INERTIA COST on do-nothing using Phase 3 P*I scale | COMPLETE / NOT COMPLETE |
| 6 | At least one alternative has INERTIA OFFSET | COMPLETE / NOT COMPLETE |
| 7 | All non-do-nothing alternatives have typed DECISION LEAD TIME (computation explicit) | COMPLETE / NOT COMPLETE |
| 8 | All DECISION LEAD TIME ≤ 0 alternatives have typed ESCALATION FLAG | COMPLETE / NOT COMPLETE |

════════════════════════════════════════════
PHASE 12 — RECOMMENDATION
════════════════════════════════════════════

RECOMMENDED OPTION: [Option N — Name]
RATIONALE: [why this wins]
CONDITIONS: [2–3 conditions; reference at least one F-NN ID]

── PM SIGN-OFF (position 1) ────────────────────────────────────────
ROLE: PM
STATEMENT: [business validation — this is the right decision]
CONDITIONS: [PM conditions; must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID that invalidates PM sign-off]

── ARCHITECT SIGN-OFF (position 2) ─────────────────────────────────
ROLE: Architect
STATEMENT: [technical validation]
CONDITIONS: [Architect conditions; must reference at least one F-NN ID]
F-ROW ANCHOR: [F-row ID that invalidates Architect sign-off]

════════════════════════════════════════════
PHASE 13 — AMEND PHASE
════════════════════════════════════════════

── MISSING OPTION ──────────────────────────────────────────────────
OPTION: [option not explored]
REASON NOT EXPLORED: [why excluded]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── UNWEIGHTED CRITERION ────────────────────────────────────────────
CRITERION: [dimension not weighted]
RECALIBRATION NOTE: [recalibration rationale]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

── FOLLOW-UP ────────────────────────────────────────────────────────
ACTION: [specific follow-up]
OWNER: [named role or person]
DEADLINE: [specific sprint, date, or milestone]

════════════════════════════════════════════
PHASE 14 — AMENDMENT TABLE FINALIZATION
════════════════════════════════════════════

If no amendment rows:
  COMPLETION STATUS: T-GUARD enforced all requirements successfully — no violations detected.
If amendment rows exist:
  COMPLETION STATUS: [N] amendments logged — see rows above.

Update Phase 0 COMPLETION STATUS to terminal value.
```

---

## Predicted Criterion Coverage

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Source |
|-----------|------|------|------|------|------|--------|
| C-01 Options coverage | PASS | PASS | PASS | PASS | PASS | Phase 4 template |
| C-02 Option anatomy | PASS | PASS | PASS | PASS | PASS | Phase 4 template |
| C-03 Recommendation | PASS | PASS | PASS | PASS | PASS | Phase 12 template |
| C-04 Decision framing | PASS | PASS | PASS | PASS | PASS | Phase 2 template |
| C-05 Scout surfacing | PASS | PASS | PASS | PASS | PASS | Phase 1 discrete step |
| C-06 Dual-role | PASS | PASS | PASS | PASS | PASS | Phases 5+6 |
| C-07 Comparison table | PASS | PASS | PASS | PASS | PASS | Phase 7 template |
| C-08 Registers | PASS | PASS | PASS | PASS | PASS | Phases 8+9 |
| C-09 Amend self-critique | PASS | PASS | PASS | PASS | PASS | Phase 13 |
| C-10 Scout inventory step | PASS | PASS | PASS | PASS | PASS | Phase 1 discrete |
| C-11 Per-category amend | PASS | PASS | PASS | PASS | PASS | Phase 13 three categories |
| C-12 OWNER structural slot | PASS | PASS | PASS | PASS | PASS | Phase 13 all three |
| C-13 Split temporal anchor | PASS | PASS | PASS | PASS | PASS | Phase 2 two typed fields |
| C-14 DEADLINE structural slot | PASS | PASS | PASS | PASS | PASS | Phase 13 all three |
| C-15 F-row + sign-off linkage | PASS | PASS | PASS | PASS | PASS | Phase 10 + Phase 12 CONDITIONS |
| C-16 Numeric P*I + anchors | PASS | PASS | PASS | PASS | PASS | Phase 3 + Phase 9 |
| C-17 Registers before rec | PASS | PASS | PASS | PASS | PASS | Phase ordering (8,9,10 < 12) |
| C-18 Front-loaded amendment | PASS | PASS | PASS | PASS | PASS | Phase 0 table init |
| C-19 Canonical F-row labels | PASS | PASS | PASS | PASS | PASS | Phase 10 exact labels |
| C-20 PREREQUISITE GATE | PASS | PASS | PASS | PASS | PASS | Phase 11 |
| C-21 Dual-signatory F-ROW ANCHOR | PASS | PASS | PASS | PASS | PASS | Phase 12 PM+Arch each |
| C-22 Named trigger IDs + back-ref | PASS | PASS | PASS | PASS | PASS | Phase 0 T-NN IDs |
| C-23 T-GUARD sentinel | PASS | PASS | PASS | PASS | PASS | Phase 0 T-GUARD defined |
| C-24 Empty-table completion | PASS | PASS | PASS | PASS | PASS | Phase 14 declaration |
| C-25 Sentinel-first ordering | PASS | PASS | PASS | PASS | PASS | T-GUARD at position 1 |
| C-26 COMPLETION STATUS Phase 0 slot | PASS | PASS | PASS | PASS | PASS | Phase 0 PENDING slot |
| C-27 INERTIA COST + OFFSET + GATE | PASS | PASS | PASS | PASS | PASS | Phase 4 + Phase 11 gate items |
| **C-28** PM-first sign-off | **PASS** | PASS | PASS | **PASS** | PASS | V-01 axis: PM pos-1 throughout |
| **C-29** Table-dominant registers | PASS | **PASS** | PASS | **PASS** | PASS | V-02 axis: Phase 0 format contracts |
| **C-30** Phase manifest | PASS | PASS | **PASS** | PASS | **PASS** | V-03 axis: Phase 0 manifest block |
| **C-31** DECISION LEAD TIME | PASS | PASS | PASS | PASS | **PASS** | V-05 axis: Phase 0 inertia-chain contract |

**Predicted composite:** All 5 variations predicted at 100.0 (31/31 criteria, denominator 24/24 aspirational).

---

## Discriminator Hypotheses for Scoring

**C-28 discriminator test (V-01):** V-01's PM-first ordering is enforced at every dual-role phase (framing, option authoring, perspective phases), not only sign-off. The question for scoring: does enforcing PM-first throughout the document produce more reliable C-28 compliance than declaring PM-first only in Phase 12? If V-01 produces consistent PM-first sign-off without triggering T-19, the hypothesis is confirmed.

**C-29 discriminator test (V-02):** V-02 declares all three register format contracts at Phase 0 initialization with exact column headers. The question: does a Phase 0 format declaration prevent prose-format register production more reliably than per-phase format instructions? If V-02 produces all three registers in canonical table format without triggering T-14, T-15, or T-16, the hypothesis is confirmed.

**C-30 discriminator test (V-03):** V-03's phase manifest lists all 15 phases by number and name in Phase 0. The question: does a phase manifest with a LIFECYCLE ORDERING VERIFICATION note (explicitly confirming registers precede recommendation) produce more reliable C-17 + C-30 compliance than a prompt that implicitly sequences phases? If V-03's manifest is complete and accurate, C-30 passes and C-17 is confirmed without document scanning.

**C-31 discriminator test (V-05):** V-05 declares the inertia chain as a Phase 0 contract (INERTIA COST → INERTIA OFFSET → DECISION LEAD TIME → ESCALATION FLAG) and repeats the computation formula in Phase 4. The question: does the Phase 0 chain declaration make DECISION LEAD TIME explicit computation more reliable than Phase 4 instructions alone? V-03 and V-04 also carry DECISION LEAD TIME in Phase 4 (baseline), so the marginal contribution of the Phase 0 inertia-chain declaration is testable by comparing V-05 to V-03/V-04 on C-31 compliance.

**C-28 + C-29 combination test (V-04):** Do PM-first ordering and table-dominant formats reinforce each other? V-04 includes both axes. If V-04 scores identically to V-01 and V-02 on their respective new criteria, the axes are independent. If V-04 produces a structurally more coherent document (PM framing anchors format discipline), the combination has positive interaction.

**C-30 + C-31 combination test (V-05):** Does phase manifest initialization alongside inertia-chain declaration produce stronger C-31 compliance than Phase 4 instructions alone? V-05's Phase 0 inertia-chain contract names TEMPORAL ANCHOR as the deadline source — linking Phase 2 to Phase 4 explicitly. This creates a cross-phase dependency declaration that Phase 4 instructions cannot provide alone.
