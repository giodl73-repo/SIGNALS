The R3 variations file already has complete content from a prior session. Here's what's there:

---

**draft-proposal — Variation Set R3** (`simulations/quest/variations/draft-proposal-variations-R3-2026-03-14.md`, 989 lines)

All 5 variations inherit R2 V-05 as the base (full integration, 100/100) and add v3 compliance (C-12/C-13 both satisfied in all variations via split TEMPORAL ANCHOR + INACTION CONSEQUENCE and OWNER in all three amend template slots).

| ID | Axis | Type | Primary target |
|----|------|------|----------------|
| **V-01** | Amend deadline completion — DEADLINE field on all three amend categories (MISSING OPTION + UNWEIGHTED CRITERION + FOLLOW-UP) | Single | C-14 (amend completeness) |
| **V-02** | Gate-citation phase annotations — `THIS PHASE CLOSES: [C-XX]` on every phase header | Single | Auditable criterion coverage |
| **V-03** | Numeric P*I risk scoring — 1/3/5 scoring guide before option tables, P × I compound in every Risk field and register | Single | Risk separation (seeds C-16) |
| **V-04** | Gate-citation + F-row failure mode register + lifecycle resequencing (registers before recommendation) | Combined | Failure mode traceability; F-rows must precede recommendation to inform it |
| **V-05** | Front-loaded amendment schema — amendment table initialized before Phase 1, auto-generate HIGH rows tied to criterion IDs when trigger conditions fire | Combined | In-document self-enforcement; reviewer verifies compliance from amendment table alone |

**Key structural bets in this round:**

- **V-04 lifecycle resequencing** — assumption/risk registers placed *before* the recommendation. F-rows written after a recommendation justify it retroactively; F-rows that precede it must inform it.
- **V-05 front-loaded amendment table** — auto-generate rules (TEMPORAL ANCHOR vague → C-12 row; INCOMPLETE STATUS absent → C-13 row; amend category missing OWNER/DEADLINE → C-14 row; F-row missing Fallback → C-15 row; holistic L/M/H risk → C-16 row) convert enforcement from external review into a live trail inside the document.

**Predicted discriminators under extended rubric:** V-03 introduces P*I but without pre-scoring anchor grounding (Phase 3b defines anchors but is a separate optional phase); V-04/V-05 add F-rows and gate-citation. Scorecard already shows these discriminators play out at C-14/C-15/C-16 criteria that V-03/V-04/V-05 were designed to seed.

**Most likely golden:** V-05 — the only variation where criterion compliance is verifiable from the amendment table alone without re-reading the full document.

## V-01: Amend Deadline Completion

**Axis**: Amend phase field completeness (single-axis)
**Hypothesis**: Adding DEADLINE as a required template field on MISSING OPTION and UNWEIGHTED CRITERION closes C-14. V-05 R2 had DEADLINE only in FOLLOW-UP; the other two categories had OWNER + NEXT ACTION without time-binding. C-14 requires all three categories to be ownership-assigned and deadline-bound. This is the minimum change from V-05 R2 that produces a C-14 pass.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact with: name, date, and key finding relevant to this decision. If none exist, state the gap and provide a 2-3 sentence inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options are named:
- Stack: language, runtime, platform, OS compatibility
- Integration: APIs, protocols, dependency limits
- Timeline: achievable windows at current team size
- Known failure modes: technical risks that could invalidate an option regardless of other merits

Label each constraint C-NN. These are fixed. Any option violating a constraint must include explicit justification.

---

### Phase 3: PM -- Decision Frame

**PM** fills all four fields before writing options. All four are required; omitting any field fails the artifact.

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, event, or deadline that closes the window.
                       E.g.: "Q2 planning cutoff 2026-04-01", "R3 feature freeze sprint".
                       Do not write "soon," "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [What teams lose, incur, or are blocked by if the TEMPORAL ANCHOR
                       passes without a decision -- name it, do not assert generic risk.]
```

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

The status quo is always Option 0 and always comes first.

**Option 0: Do Nothing / Status Quo**

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid this problem |
| Pros | Low switching cost, familiarity, zero migration risk -- be specific to this domain |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | PROBABILITY [L/M/H] × IMPACT [L/M/H] -- name the deteriorating condition |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [The metric that degrades per sprint/month/quarter -- name the metric and rate of drift] |

**Architect note**: Is this technically stable? Name any deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 5: Alternatives (Minimum 3)

For each alternative, all fields are required. Any omitted field fails the artifact.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | PROBABILITY [L/M/H] × IMPACT [L/M/H] -- name the risk |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: State compliance with all C-NN constraints. Name any violation and justification.

---

### Phase 6: Comparison Matrix

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells. Required dimensions: effort, team control, adoption friction, time to value. Add domain-specific dimensions as warranted.

---

### Phase 7: Recommendation -- Dual Signature Form

Both signature blocks required. INCOMPLETE STATUS reads COMPLETE only when both blocks contain structurally distinct, non-interchangeable content. Architect silence is not endorsement.

```
PM SIGN-OFF
  CHOSEN OPTION:   [letter + name]
  RATIONALE:       [2-3 sentences -- adoption, timeline, stakeholder fit.
                    Reference scout artifact by name or state "none found."]
  CONDITIONS:      [2-3 conditions that must hold for this recommendation to remain valid]
  CONFIDENCE:      [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named, or "none" only if Architect
                         fully concurs with no reservations]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints, or
                         name the exception with justification]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 8: Assumption Register

Minimum 2 entries. Validation plan must name a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Amend Phase

All three sections are required. Each entry requires OWNER, NEXT ACTION, and DEADLINE.

#### MISSING OPTION

`[Unexplored approach and why it matters] -- OWNER: [role/team] -- NEXT ACTION: [investigation step] -- DEADLINE: [named date or event]`

#### UNWEIGHTED CRITERION

`[Underweighted dimension + why] -- OWNER: [role/team] -- NEXT ACTION: [recalibration step] -- DEADLINE: [named date or event]`

#### FOLLOW-UP

`[Open question or prerequisite] -- OWNER: [role/team] -- NEXT ACTION: [specific step] -- DEADLINE: [named date or event]`

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-02: Gate-Citation Phase Annotations

**Axis**: Phase annotation with criterion-citation (single-axis)
**Hypothesis**: Annotating each phase header with `THIS PHASE CLOSES: [C-XX, C-YY]` makes criterion coverage auditable without re-evaluating the full document. A reviewer can confirm that C-12 was addressed by finding the Phase 3 annotation; C-13 by finding Phase 7; C-14 by finding Phase 10. The citation forces the model to establish the connection between output sections and rubric criteria at write time, not retroactively. V-01 demonstrates C-12/C-13/C-14 structurally; V-02 makes them verifiable by citation.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact. Each phase annotation (`THIS PHASE CLOSES:`) must name the criteria that phase satisfies.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory
**THIS PHASE CLOSES: [C-05, C-10]**

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact with: name, date, and key finding relevant to this decision. If none exist, state the gap and provide a 2-3 sentence inline assessment.

---

### Phase 2: Architect -- Constraint Inventory
**THIS PHASE CLOSES: [C-06 (partial)]**

**Architect** enumerates constraints before any options are named:
- Stack: language, runtime, platform, OS compatibility
- Integration: APIs, protocols, dependency limits
- Timeline: achievable windows at current team size
- Known failure modes: technical risks that could invalidate an option

Label each constraint C-NN. These are fixed. Any option violating a constraint must include explicit justification.

---

### Phase 3: PM -- Decision Frame
**THIS PHASE CLOSES: [C-04, C-12]**

**PM** fills all four fields before writing options. All four are required.

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, event, or deadline that closes the window.
                       Do not write "soon," "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [What teams lose, incur, or are blocked by if the TEMPORAL ANCHOR
                       passes without a decision -- name it, do not assert generic risk.]
```

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)
**THIS PHASE CLOSES: [C-01 (partial), C-02 (partial)]**

**Option 0: Do Nothing / Status Quo**

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid this problem |
| Pros | Low switching cost, familiarity, zero migration risk -- be specific to this domain |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | PROBABILITY [L/M/H] × IMPACT [L/M/H] -- name the deteriorating condition |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [The metric that degrades per sprint/month/quarter -- name the metric and rate] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 5: Alternatives (Minimum 3)
**THIS PHASE CLOSES: [C-01, C-02]**

For each alternative, all fields are required.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | PROBABILITY [L/M/H] × IMPACT [L/M/H] -- name the risk |
| Effort | N weeks + team size + key dependencies |

**Architect constraint check**: Compliance with all C-NN constraints or named exception with justification.

---

### Phase 6: Comparison Matrix
**THIS PHASE CLOSES: [C-07]**

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells. Required dimensions: effort, team control, adoption friction, time to value.

---

### Phase 7: Recommendation -- Dual Signature Form
**THIS PHASE CLOSES: [C-03, C-06, C-13]**

Both signature blocks required. INCOMPLETE STATUS reads COMPLETE only when both blocks contain structurally distinct, non-interchangeable content.

```
PM SIGN-OFF
  CHOSEN OPTION:   [letter + name]
  RATIONALE:       [2-3 sentences -- adoption, timeline, stakeholder fit.
                    Reference scout artifact by name or state "none found."]
  CONDITIONS:      [2-3 conditions that must hold for this recommendation to remain valid]
  CONFIDENCE:      [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named, or "none" only if fully concurs]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints,
                         or name exception with justification]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 8: Assumption Register
**THIS PHASE CLOSES: [C-08 (partial)]**

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register
**THIS PHASE CLOSES: [C-08]**

Minimum 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Amend Phase
**THIS PHASE CLOSES: [C-09, C-11, C-14]**

All three sections required. Each entry: OWNER + NEXT ACTION + DEADLINE.

#### MISSING OPTION

`[Unexplored approach] -- OWNER: [role/team] -- NEXT ACTION: [investigation step] -- DEADLINE: [named date or event]`

#### UNWEIGHTED CRITERION

`[Underweighted dimension + why] -- OWNER: [role/team] -- NEXT ACTION: [recalibration step] -- DEADLINE: [named date or event]`

#### FOLLOW-UP

`[Open question or prerequisite] -- OWNER: [role/team] -- NEXT ACTION: [specific step] -- DEADLINE: [named date or event]`

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-03: Numeric P*I Risk Scoring

**Axis**: Risk scoring granularity (single-axis)
**Hypothesis**: Replacing categorical L/M/H risk labels with 1-5 numeric scores (with 1/3/5 anchors defined before any scoring) and requiring P × I = P*I compound prevents holistic risk collapse. When Probability and Impact are separate numeric fields, a reviewer can verify whether a HIGH/HIGH risk actually scored 5×5=25 or was assigned 3×3=9 and labeled HIGH. V-01's L/M/H fields cannot discriminate within a tier. The midpoint anchor (score of 3) must describe a project-specific mediocre outcome, forcing the writer to reason about what "medium probability" means for this specific option before scoring.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact with: name, date, and key finding relevant to this decision. If none exist, state the gap and provide a 2-3 sentence inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options are named:
- Stack: language, runtime, platform, OS compatibility
- Integration: APIs, protocols, dependency limits
- Timeline: achievable windows at current team size
- Known failure modes: technical risks that could invalidate an option

Label each constraint C-NN. These are fixed.

---

### Phase 3: PM -- Decision Frame

**PM** fills all four fields before writing options. All four are required.

```
THE QUESTION:         [One interrogative sentence -- the specific decision being made]
WHY NOW:              [The specific event or cost pressure making deferral harmful]
TEMPORAL ANCHOR:      [Named date, sprint, event, or deadline that closes the window.
                       Do not write "soon," "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [What teams lose, incur, or are blocked by if the TEMPORAL ANCHOR
                       passes without a decision -- name it, do not assert generic risk.]
```

---

### Phase 3b: Risk Scoring Guide

Before writing any options, define the 1/3/5 scoring anchors for this specific decision. These anchors apply to all Risk fields in Phases 4, 5, and 9.

```
PROBABILITY ANCHORS (for this topic):
  1 (rare):      [Project-specific description -- what would make this unlikely]
  3 (plausible): [Project-specific mediocre outcome -- what "middle" probability looks like here]
  5 (likely):    [Project-specific description -- what would make this near-certain]

IMPACT ANCHORS (for this topic):
  1 (negligible): [Project-specific description -- what "low impact" means here]
  3 (moderate):   [Project-specific description -- what "medium impact" looks like here]
  5 (severe):     [Project-specific description -- what "high impact" means here]
```

Use these anchors for every risk field. P*I = Probability × Impact. Report all three values.

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

**Option 0: Do Nothing / Status Quo**

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid this problem |
| Pros | Low switching cost, familiarity, zero migration risk -- be specific |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | P: [1-5 per anchor] × I: [1-5 per anchor] = P*I: [N] -- [named risk description] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [The metric that degrades per sprint/month/quarter -- name the metric and rate] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 5: Alternatives (Minimum 3)

For each alternative, all fields are required.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | P: [1-5 per anchor] × I: [1-5 per anchor] = P*I: [N] -- [named risk description] |
| Effort | N weeks + team size + key dependencies |

**Architect constraint check**: Compliance with all C-NN constraints or named exception with justification.

---

### Phase 6: Comparison Matrix

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells.
Risk row uses P*I score (not categorical label). Required dimensions: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 7: Recommendation -- Dual Signature Form

Both signature blocks required. INCOMPLETE STATUS reads COMPLETE only when both blocks contain structurally distinct content.

```
PM SIGN-OFF
  CHOSEN OPTION:   [letter + name]
  RATIONALE:       [2-3 sentences -- adoption, timeline, stakeholder fit.
                    Reference scout artifact by name or state "none found."]
  CONDITIONS:      [2-3 conditions that must hold for this recommendation to remain valid]
  CONFIDENCE:      [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 8: Assumption Register

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register

Minimum 2 entries. Use scoring anchors from Phase 3b.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency]

---

### Phase 10: Amend Phase

All three sections required. Each entry: OWNER + NEXT ACTION + DEADLINE.

#### MISSING OPTION

`[Unexplored approach] -- OWNER: [role/team] -- NEXT ACTION: [investigation step] -- DEADLINE: [named date or event]`

#### UNWEIGHTED CRITERION

`[Underweighted dimension + why] -- OWNER: [role/team] -- NEXT ACTION: [recalibration step] -- DEADLINE: [named date or event]`

#### FOLLOW-UP

`[Open question or prerequisite] -- OWNER: [role/team] -- NEXT ACTION: [specific step] -- DEADLINE: [named date or event]`

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-04: Gate-Citation + F-Row Failure Mode Register

**Axis**: Gate-citation + failure mode register with lifecycle resequencing (combined)
**Hypothesis**: Two structural changes together: (1) gate-citation annotations (`THIS PHASE CLOSES: [C-XX]`) make criterion coverage auditable; (2) an F-row failure mode register placed after the risk register and before the recommendation forces failure modes to be articulated before the recommendation is made, not as retrospective anti-conditions. The lifecycle resequencing (registers before recommendation) is the discriminating axis here -- registers built before the recommendation must inform it, not justify it retroactively. An F-row that references A#/R# by ID creates a traceable link between failure modes and the evidence base. The combination answers: "how would a reviewer verify that the recommendation would survive its most likely failure mode?"

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Each phase annotation must name the criteria that phase satisfies.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory
**THIS PHASE CLOSES: [C-05, C-10]**

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact with: name, date, and key finding. If none, state gap + inline assessment.

---

### Phase 2: Architect -- Constraint Inventory
**THIS PHASE CLOSES: [C-06 (partial)]**

**Architect** enumerates constraints before options:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed.

---

### Phase 3: PM -- Decision Frame
**THIS PHASE CLOSES: [C-04, C-12]**

```
THE QUESTION:         [One interrogative sentence]
WHY NOW:              [Specific event or cost pressure]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language]
INACTION CONSEQUENCE: [What teams lose or are blocked by if TEMPORAL ANCHOR passes]
```

---

### Phase 4: Option 0 -- Do Nothing / Status Quo
**THIS PHASE CLOSES: [C-01 (partial), C-02 (partial)]**

| Field | Content |
|-------|---------|
| Description | Current state |
| Pros | Low switching cost, familiarity |
| Cons | Specific capability gaps |
| Risk | PROBABILITY [L/M/H] × IMPACT [L/M/H] -- named risk |
| Effort | 0 weeks. |
| Accumulation | [Metric + rate of drift per sprint/month] |

**Architect note**: Technical stability horizon.

---

### Phase 5: Alternatives (Minimum 3)
**THIS PHASE CLOSES: [C-01, C-02]**

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What it does |
| Pros | Advantages over Option 0 |
| Cons | Costs vs. Option 0 |
| Risk | PROBABILITY [L/M/H] × IMPACT [L/M/H] -- named risk |
| Effort | N weeks + team + dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 6: Comparison Matrix
**THIS PHASE CLOSES: [C-07]**

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value.

---

### Phase 7: Assumption Register
**THIS PHASE CLOSES: [C-08 (partial)]**

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 8: Risk Register
**THIS PHASE CLOSES: [C-08]**

Minimum 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action]

---

### Phase 9: Failure Mode Register

For each significant failure mode, complete one F-row. Minimum 2 rows. Each row must name: who looks for the observable event, what they look for, and when they look.

| F# | Observable Event (who / what / when) | Invalidates | Fallback |
|----|--------------------------------------|-------------|---------|
| F-01 | [Role] observes [specific metric or event] [at/by timepoint] | A-NN or R-NN | [Specific option or next action if this F-row fires] |
| F-02 | [Role] observes [specific metric or event] [at/by timepoint] | A-NN or R-NN | [Specific option or next action] |

Rules:
- Observable Event must name who is monitoring, what signal they look for, and when
- Invalidates must reference a specific A-NN or R-NN entry by ID
- Fallback must name a specific option letter or next action -- not "reconsider" or "revisit"

---

### Phase 10: Recommendation -- Dual Signature Form
**THIS PHASE CLOSES: [C-03, C-06, C-13]**

Both signatures required. Both must reference at least one F-row entry. INCOMPLETE STATUS reads COMPLETE only when both blocks are distinct and non-interchangeable.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name or "none found."]
  CONDITIONS:       [2-3 conditions that must hold for this to remain valid --
                     at least one condition must reference an F-row by ID]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 11: Amend Phase
**THIS PHASE CLOSES: [C-09, C-11, C-14]**

All three sections required. Each entry: OWNER + NEXT ACTION + DEADLINE.

#### MISSING OPTION

`[Unexplored approach] -- OWNER: [role/team] -- NEXT ACTION: [investigation step] -- DEADLINE: [named date or event]`

#### UNWEIGHTED CRITERION

`[Underweighted dimension + why] -- OWNER: [role/team] -- NEXT ACTION: [recalibration step] -- DEADLINE: [named date or event]`

#### FOLLOW-UP

`[Open question or prerequisite] -- OWNER: [role/team] -- NEXT ACTION: [specific step] -- DEADLINE: [named date or event]`

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-05: Front-Loaded Amendment Schema

**Axis**: Front-loaded self-enforcement + gate-citation + F-rows + P*I (full integration)
**Hypothesis**: Initializing the amendment table before Phase 1 -- with named auto-generate conditions tied to specific criterion IDs and sections -- converts the amendment section from a retrospective editorial sweep into a live enforcement trail. The key property: each auto-generated row names the criterion ID and the section where enforcement failed. A reviewer can confirm rubric compliance by reading the amendment table alone. This is qualitatively different from gate-citation (which shows what a phase was supposed to close) and from F-rows (which show when a decision should be reopened): the front-loaded schema shows what criteria were not enforced during writing and who is accountable for closing them. When combined with gate-citation and F-rows, the three mechanisms form a complete enforcement pipeline -- gate-citation before writing, F-rows during recommendation, amendment trail after completion.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Initialize the amendment table first; update it throughout writing.

**Invocation**: `/draft-proposal "{topic}"`

---

### AMENDMENT TABLE (Initialize First)

Before writing Phase 1, initialize this table. During writing, auto-generate HIGH rows when the trigger conditions below are met. At Phase 11 (Amend), review this table and complete any OWNER and DEADLINE fields still blank.

| # | Priority | Gap | Criterion | Section | OWNER | DEADLINE |
|---|----------|-----|-----------|---------|-------|----------|
| [auto-populated during writing] | | | | | | |

**Auto-generate rules** (add a HIGH row when triggered):

| Trigger | Criterion | Required row content |
|---------|-----------|---------------------|
| TEMPORAL ANCHOR is absent or contains "soon" / "eventually" | C-12 | "TEMPORAL ANCHOR missing or vague in Phase 3" |
| INCOMPLETE STATUS is not present in Phase 7 | C-13 | "Dual-signature gate absent in Phase 7" |
| Any amend category lacks OWNER or DEADLINE | C-14 | "Amend [category] missing OWNER or DEADLINE in Phase 11" |
| Any F-row in Phase 9 lacks a named Fallback | C-15* | "F-row F-[n] missing Fallback in Phase 9" |
| Risk field uses holistic L/M/H without P and I separate | C-16* | "Holistic risk label in [Option/R-NN] -- P and I not separated" |

*C-15 and C-16 are forward-looking targets; rows auto-generated here seed the next rubric iteration.

---

### Phase 1: Scout Artifact Inventory
**THIS PHASE CLOSES: [C-05, C-10]**

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none, state gap + inline assessment.

If scout inventory is skipped: auto-generate HIGH row "Scout inventory absent, C-05 and C-10 unverified."

---

### Phase 2: Architect -- Constraint Inventory
**THIS PHASE CLOSES: [C-06 (partial)]**

**Architect** enumerates constraints:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed.

---

### Phase 3: PM -- Decision Frame
**THIS PHASE CLOSES: [C-04, C-12]**

```
THE QUESTION:         [One interrogative sentence]
WHY NOW:              [Specific event or cost pressure]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language.
                       Trigger: if this field is absent or vague, auto-generate HIGH row C-12.]
INACTION CONSEQUENCE: [What teams lose or are blocked by if TEMPORAL ANCHOR passes]
```

---

### Phase 4: Risk Scoring Guide
**THIS PHASE CLOSES: [C-16* prep]**

Define 1/3/5 anchors before scoring any risks. Write project-specific descriptions for each anchor.

```
PROBABILITY (1-5):
  1 (rare):      [What makes this event unlikely for this specific project]
  3 (plausible): [What a mediocre-probability event looks like here -- be specific, not generic]
  5 (likely):    [What makes this event near-certain]

IMPACT (1-5):
  1 (negligible): [What low impact looks like for this project]
  3 (moderate):   [What medium impact means here -- name a concrete consequence]
  5 (severe):     [What high impact looks like -- name a concrete outcome]
```

---

### Phase 5: Option 0 -- Do Nothing / Status Quo
**THIS PHASE CLOSES: [C-01 (partial), C-02 (partial)]**

| Field | Content |
|-------|---------|
| Description | Current state |
| Pros | Low switching cost, familiarity |
| Cons | Specific capability gaps |
| Risk | P: [1-5] × I: [1-5] = P*I: [N] -- [named risk; if L/M/H used instead, auto-generate C-16 row] |
| Effort | 0 weeks. |
| Accumulation | [Metric + rate of drift per sprint/month] |

**Architect note**: Technical stability horizon.

---

### Phase 6: Alternatives (Minimum 3)
**THIS PHASE CLOSES: [C-01, C-02]**

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What it does |
| Pros | Advantages over Option 0 |
| Cons | Costs vs. Option 0 |
| Risk | P: [1-5] × I: [1-5] = P*I: [N] -- [named risk] |
| Effort | N weeks + team + dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix
**THIS PHASE CLOSES: [C-07]**

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register
**THIS PHASE CLOSES: [C-08 (partial)]**

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register
**THIS PHASE CLOSES: [C-08]**

Minimum 2 entries. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action]

If any entry uses holistic L/M/H instead of separate P and I: auto-generate HIGH amendment row for C-16.

---

### Phase 10: Failure Mode Register
**THIS PHASE CLOSES: [C-15*]**

Minimum 2 F-rows. Observable Event must name who monitors, what signal, and when.

| F# | Observable Event (who / what / when) | Invalidates | Fallback |
|----|--------------------------------------|-------------|---------|
| F-01 | | A-NN or R-NN | |
| F-02 | | A-NN or R-NN | |

If any Fallback is blank: auto-generate HIGH amendment row "F-[n] missing Fallback, C-15."

---

### Phase 11: Recommendation -- Dual Signature Form
**THIS PHASE CLOSES: [C-03, C-06, C-13]**

Both signatures required. INCOMPLETE STATUS trigger: if absent, auto-generate HIGH amendment row "Dual-signature gate absent, C-13."

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name or "none found."
                     At least one condition must reference an F-row by ID.]
  CONDITIONS:       [2-3 conditions that must hold -- at least one references F-row by ID]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

If INCOMPLETE STATUS is absent: auto-generate HIGH amendment row for C-13.

---

### Phase 12: Amend Phase
**THIS PHASE CLOSES: [C-09, C-11, C-14]**

Merge any auto-generated rows from the AMENDMENT TABLE into the appropriate category below. Add at least one entry per category not already covered by auto-generated rows. Each entry: OWNER + NEXT ACTION + DEADLINE.

If any category lacks OWNER or DEADLINE: auto-generate HIGH row for C-14.

#### MISSING OPTION

`[Unexplored approach] -- OWNER: [role/team] -- NEXT ACTION: [investigation step] -- DEADLINE: [named date or event]`

#### UNWEIGHTED CRITERION

`[Underweighted dimension + why] -- OWNER: [role/team] -- NEXT ACTION: [recalibration step] -- DEADLINE: [named date or event]`

#### FOLLOW-UP

`[Open question or prerequisite] -- OWNER: [role/team] -- NEXT ACTION: [specific step] -- DEADLINE: [named date or event]`

---

### Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## Most Likely Golden Candidate

**V-05** -- front-loaded amendment schema converts enforcement from external review to in-document tracking. A reviewer reading only the amendment table can identify which criteria passed, which failed, and who owns each gap. No other variation makes criterion compliance verifiable from a single section.

**V-04** is the strongest single-artifact advance: lifecycle resequencing (registers before recommendation) is the highest-value structural change in R3. F-rows that precede the recommendation must inform it; F-rows written after a recommendation only justify it.

**Risk assessments**:
- V-01: Safe minimum viable improvement. Passes C-14 with zero risk of degrading other criteria.
- V-02: Gate-citation is additive and lossless. No existing criterion can fail by adding phase annotations.
- V-03: P*I scoring changes the format of risk fields across all phases -- any evaluator running V-03 against a rubric expecting L/M/H labels will see divergence. This is intentional: V-03 seeds C-16.
- V-04: Lifecycle resequencing is the discriminating experiment. If registers-before-recommendation produces higher-quality recommendations (better F-row attribution, more analytically grounded conditions), this is a structural advance. If it increases cognitive load without quality gain, V-01's ordering is sufficient.
- V-05: Most ambitious. The amendment table must be initialized before writing begins, which requires the model to understand all trigger conditions upfront. Risk: over-specification produces mechanical compliance rather than genuine self-critique. The quality gate is whether auto-generated rows in the AMENDMENT TABLE at Phase 12 reflect real enforcement failures or are empty (indicating the prompt worked as designed).
