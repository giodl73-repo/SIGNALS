Written to `simulations/quest/variations/draft-proposal-variations-R4-2026-03-14.md`.

**Summary of R4 variations:**

| ID | Axis | Predicted Score | Designed Fail |
|----|------|-----------------|---------------|
| V-01 | F-row 3-field template + F-ROW ANCHOR typed slot | 99.09 | C-18 |
| V-02 | PREREQUISITE GATE block before recommendation | 99.09 | C-18 |
| V-03 | Inertia-forward framing + INERTIA COST/OFFSET | 98.18 | C-15, C-18 |
| V-04 | V-01 + V-02 + project-specific anchors combined | 99.09 | C-18 |
| V-05 | Full integration + STRUCTURE GUARD cascade | 100.00 | -- |

**Key advances over R3:**

1. **F-ROW ANCHOR as typed slot** (V-01, V-04, V-05): R3 had "at least one references F-row by ID" as prose instruction. R4 makes it a named field in both PM and Architect sign-off — structurally mandatory.

2. **PREREQUISITE GATE** (V-02, V-04, V-05): C-17 was satisfied by phase ordering in R3. R4 adds a typed checklist block that must be filled before the recommendation can proceed — verifiable at a single point.

3. **INERTIA quantification** (V-03): Status quo gets a computable INERTIA COST (P*I per sprint) and alternatives must name their INERTIA OFFSET (sprints to crossover). Not a rubric criterion — seeds v5 quality metrics.

4. **T-GUARD cascade** (V-05): Single trigger covering all 5 new criteria simultaneously when any required structural block is absent. Advance over R3's Trigger K: named trigger IDs (T-01 through T-GUARD) make each amendment row traceable to its source rule by ID.
E GATE block immediately before the recommendation, confirming both registers are complete and precede it. Hypothesis: a single verifiable block makes C-17 auditable without document scan.
- **V-03 inertia-forward**: Option 0 elevated to INERTIA BASELINE with INERTIA COST (P*I per sprint) that alternatives must demonstrably offset. C-15 fails by design (no F-rows); C-18 fails by design (no front-loaded table). Tests framing axis independently of structural criteria.
- **V-04**: V-01 + V-02 + project-specific anchors combined. C-18 fails by design -- single controlled discriminator between V-04 and V-05.
- **V-05**: V-04 + front-loaded amendment table with STRUCTURE GUARD cascade (T-GUARD). Golden candidate.

**Predicted scorecard under v4** (formula: essential_pass/4*60 + recommended_pass/3*30 + aspirational_pass/11*10, max 100):

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total | Fails |
|-----------|---------------|-----------------|-------------------|-------|-------|
| V-01 | 60.0 (4/4) | 30.0 (3/3) | 9.09 (10/11) | **99.09** | C-18 |
| V-02 | 60.0 (4/4) | 30.0 (3/3) | 9.09 (10/11) | **99.09** | C-18 |
| V-03 | 60.0 (4/4) | 30.0 (3/3) | 8.18 (9/11) | **98.18** | C-15, C-18 |
| V-04 | 60.0 (4/4) | 30.0 (3/3) | 9.09 (10/11) | **99.09** | C-18 |
| V-05 | 60.0 (4/4) | 30.0 (3/3) | 10.0 (11/11) | **100.00** | -- |

---

## V-01: F-Row 3-Field Explicit Template

**Axis**: F-row failure mode field precision (single-axis)
**Hypothesis**: R3's Observable Event / Invalidates / Fallback table satisfies C-15 by analogy -- a reviewer must infer that Observable Event = trigger condition and Fallback = mitigation. Explicit field labels FAILURE MODE / TRIGGER CONDITION / MITIGATION map directly to C-15's three-part requirement, eliminating the inference step. The F-ROW ANCHOR typed slot in PM and Architect SIGN-OFF CONDITIONS makes F-row linkage structural -- the model cannot complete the recommendation without naming an F-row ID. C-18 fails by design (no front-loaded amendment table).

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
                       Do not write "soon," "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [What teams lose, incur, or are blocked by if the TEMPORAL ANCHOR
                       passes without a decision -- name it, do not assert generic risk.]
```

---

### Phase 4: Risk Scoring Guide

Define project-specific scoring anchors before writing any options. Each anchor must describe a named outcome in this project's context -- not a generic severity label. These anchors apply to all Risk fields and register entries.

```
PROBABILITY ANCHORS (this project, this decision):
  1 (rare):      [Named condition that makes this outcome unlikely for this specific project]
  3 (plausible): [Named typical-trouble outcome specific to this project -- not a generic category]
  5 (likely):    [Named condition making this outcome near-certain for this project]

IMPACT ANCHORS (this project, this decision):
  1 (negligible): [Named concrete example of low impact in this project's context]
  3 (moderate):   [Named specific consequence representing medium impact here]
  5 (severe):     [Named outcome representing high impact -- not a severity label]
```

Every risk field and register entry uses separate P and I numeric scores grounded in these anchors. Holistic L/M/H labels fail.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they address or avoid this problem |
| Pros | Low switching cost, familiarity, zero migration risk -- specific to this domain |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. No implementation required. |
| Accumulation | [The metric that degrades per sprint/month/quarter -- name metric and rate of drift] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 6: Alternatives (Minimum 3)

For each alternative, all fields are required. Omitting any field fails the artifact.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Costs, limitations, trade-offs vs. Option 0 |
| Risk | P: [1-5 per Phase 4] x I: [1-5 per Phase 4] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: Compliance with all C-NN constraints from Phase 2. Name any violation and justification.

---

### Phase 7: Comparison Matrix

Joint PM/Architect table. Columns = all options. Rows = 4-6 dimensions. No empty cells. Required dimensions: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 entries. Validation plan must name a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action before commitment]

---

### Phase 9: Risk Register

Minimum 2 entries. Use Phase 4 anchors for all P and I scores.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Failure Mode Register

Minimum 2 entries. This register is distinct from the Risk Register (Phase 9). Failure modes describe conditions that would invalidate the recommendation -- not risk events that may occur during implementation.

Each entry must include all three named fields:

```
F-NN:
  FAILURE MODE:       [What goes wrong -- the specific failure, named precisely]
  TRIGGER CONDITION:  [The observable event or threshold that confirms this failure mode has
                       activated -- name who observes it, what signal they look for, and when]
  MITIGATION:         [Specific escalation path or fallback -- name an option letter or
                       next action; "reconsider" and "revisit" are not acceptable]
```

Each F-NN must cross-reference the assumption (A-NN) or risk (R-NN) entry it would invalidate.

---

### Phase 11: Recommendation -- Dual Signature Form

**PREREQUISITE**: Phases 8 (Assumption Register) and 9 (Risk Register) must be complete before writing this phase. The recommendation follows the registers; it does not precede them.

Both signature blocks are required. INCOMPLETE STATUS reads COMPLETE only when both blocks contain structurally distinct, non-interchangeable content. Architect silence is not endorsement.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name, or state "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation. Name the F-row and describe the condition.]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites before chosen option is viable -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named, or "none" only if
                         Architect fully concurs with zero reservations]
  CONSTRAINT VERIFIED:  [Confirm chosen option satisfies all Phase 2 C-NN constraints,
                         or name the exception with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode whose activation would cause Architect
                         to reassess or DISSENT. Name the F-row and condition.]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative recommendation]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry carries all three typed slots: OWNER, NEXT ACTION, and DEADLINE. DEADLINE must be a specific sprint name, named date, or named milestone -- "TBD," "soon," or blank fails.

#### MISSING OPTION

```
[Unexplored approach and why it matters]
OWNER:       [role/team]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted decision dimension and why it should be recalibrated]
OWNER:       [role/team]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite that must be resolved]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

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

## V-02: Prerequisite Verification Gate

**Axis**: Explicit prerequisite gate before recommendation (single-axis)
**Hypothesis**: C-17 requires both assumption and risk registers to precede the recommendation in document sequence. R3 achieves this by phase ordering. A typed PREREQUISITE GATE block -- a mandatory checklist completed before writing the recommendation -- makes C-17 verifiable at a single point without document scan. The gate also pre-checks F-row anchor presence, catching C-15 omission at the gate rather than at review. F-row template uses R3 V-04 table format (not V-01's 3-field format -- one axis at a time). C-18 fails by design (no front-loaded amendment table).

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Complete the PREREQUISITE GATE before writing the recommendation. Role labels are mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none, state gap + inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options are named:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed.

---

### Phase 3: PM -- Decision Frame

```
THE QUESTION:         [One interrogative sentence]
WHY NOW:              [Specific event or cost pressure]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language]
INACTION CONSEQUENCE: [What teams lose or are blocked by if TEMPORAL ANCHOR passes]
```

---

### Phase 4: Risk Scoring Guide

Define project-specific P and I anchors before scoring any risks.

```
PROBABILITY (1-5, this project):
  1: [Named condition making this outcome unlikely for this project]
  3: [Named typical-trouble outcome specific to this project]
  5: [Named condition making this outcome near-certain here]

IMPACT (1-5, this project):
  1: [Named low-impact example in this project's context]
  3: [Named specific medium-impact consequence here]
  5: [Named high-impact outcome in this project]
```

---

### Phase 5: Option 0 -- Do Nothing / Status Quo

| Field | Content |
|-------|---------|
| Description | Current state |
| Pros | Low switching cost, familiarity |
| Cons | Specific capability gaps |
| Risk | P: [1-5] x I: [1-5] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. |
| Accumulation | [Metric + rate of drift per sprint/month] |

**Architect note**: Technical stability horizon.

---

### Phase 6: Alternatives (Minimum 3)

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What it does |
| Pros | Advantages over Option 0 |
| Cons | Costs vs. Option 0 |
| Risk | P: [1-5] x I: [1-5] = P*I: [N] -- [named risk] |
| Effort | N weeks + team + dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register

Minimum 2 entries. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action]

---

### Phase 10: Failure Mode Register

Minimum 2 F-rows. Distinct from Phase 9 Risk Register.

| F# | Observable Event (who / what / when) | Invalidates | Fallback |
|----|--------------------------------------|-------------|---------|
| F-01 | [Role] observes [specific event] [at/by timepoint] | A-NN or R-NN | [Named option or action] |
| F-02 | [Role] observes [specific event] [at/by timepoint] | A-NN or R-NN | [Named option or action] |

Rules: Observable Event names who monitors, what signal, and when. Invalidates cites A-NN or R-NN. Fallback names an option letter or action.

---

### PREREQUISITE GATE (Complete before Phase 11)

Before writing the recommendation, verify all prerequisites below. Write PASS or FAIL for each. If any item is FAIL, complete the missing element before proceeding.

```
PREREQUISITE GATE
  ASSUMPTION REGISTER COMPLETE:   [PASS / FAIL -- Phase 8, >= 2 entries with validation plans]
  RISK REGISTER COMPLETE:         [PASS / FAIL -- Phase 9, >= 2 entries with P, I, P*I]
  REGISTERS PRECEDE REC:          [PASS / FAIL -- Phases 8 and 9 appear before this gate]
  FAILURE MODE REGISTER COMPLETE: [PASS / FAIL -- Phase 10, >= 2 F-rows with Fallback named]
  F-ROW ANCHOR READY:             [F-NN: the F-row ID to cite in PM CONDITIONS sign-off]
  GATE STATUS:                    [OPEN / BLOCKED -- OPEN only when all items are PASS]
```

Do not write Phase 11 if GATE STATUS is BLOCKED.

---

### Phase 11: Recommendation -- Dual Signature Form

Both signatures required. INCOMPLETE STATUS reads COMPLETE only when both blocks are structurally distinct.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name or "none found."]
  CONDITIONS:       [2-3 conditions -- at least one must reference an F-row by ID]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [C-NN compliance or named exception]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 12: Amend Phase

All three sections required. Each entry: OWNER, NEXT ACTION, DEADLINE (specific sprint/date/milestone).

#### MISSING OPTION

```
[Unexplored approach]
OWNER:       [role/team]
NEXT ACTION: [investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted dimension + why]
OWNER:       [role/team]
NEXT ACTION: [recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

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

## V-03: Inertia-Forward Framing

**Axis**: Status-quo prominence and inertia cost quantification (single-axis)
**Hypothesis**: Most proposals treat Option 0 as one option among equals. Making it the INERTIA BASELINE -- computing an INERTIA COST (P*I per sprint) and requiring alternatives to name their INERTIA OFFSET (sprints until cumulative cost beats the baseline) -- forces the Accumulation field to be quantitative rather than descriptive and raises comparison matrix quality by adding a computable crossover dimension. C-15 fails by design (no F-row register). C-18 fails by design (no front-loaded amendment table). This is the most divergent single-axis variation: it tests a framing and format axis independently of the structural criteria.

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

List each found artifact: name, date, key finding. If none, state gap + inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before any options are named:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed.

---

### Phase 3: Risk Scoring Guide

Define project-specific anchors before scoring the Inertia Baseline or any alternative. Each anchor must describe a named outcome in this project's context.

```
PROBABILITY (1-5, this project):
  1: [Named condition making this outcome unlikely for this project]
  3: [Named typical-trouble outcome specific to this project]
  5: [Named condition making this outcome near-certain here]

IMPACT (1-5, this project):
  1: [Named low-impact example in this project]
  3: [Named specific medium-impact consequence here]
  5: [Named high-impact outcome in this project]
```

---

### Phase 4: Inertia Baseline (Option 0 -- Do Nothing / Status Quo)

Option 0 is the INERTIA BASELINE. It is the default that remains in force unless actively displaced. All alternatives are measured against it.

**PM** fills the decision frame:

```
THE QUESTION:         [One interrogative sentence]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language]
INACTION CONSEQUENCE: [What teams lose by TEMPORAL ANCHOR if no decision is made]
```

**INERTIA BASELINE**

| Field | Content |
|-------|---------|
| Description | What teams do today -- how they currently address or avoid this problem |
| Pros | Low switching cost, familiarity, zero migration risk -- specific to this domain |
| Cons | Capability gaps or maintenance burdens accepted by staying |
| Inertia Risk | P: [1-5 per Phase 3] x I: [1-5 per Phase 3] = P*I: [N] -- [named deteriorating condition] |
| Effort | 0 weeks. No implementation required. |
| INERTIA COST | [P*I per sprint -- name the metric and rate, e.g. "P*I = 9 per sprint; 3 blocked integrations x 3-sprint delay each"] |

**Architect note**: Deprecations, platform shifts, or scaling limits on the horizon.

---

### Phase 5: Alternatives (Minimum 3)

Each alternative must name its INERTIA OFFSET: sprints until its cumulative cost falls below the Inertia Cost. Show the math.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Inertia Baseline |
| Cons | Costs, limitations, trade-offs vs. Inertia Baseline |
| Risk | P: [1-5 per Phase 3] x I: [1-5 per Phase 3] = P*I: [N] -- [named risk] |
| Effort | N weeks + team size + key dependencies |
| INERTIA OFFSET | [Sprints until cumulative cost < Inertia Cost -- show the math] |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 6: Comparison Matrix

Columns = all options (including Inertia Baseline). Rows = 4-6 dimensions. No empty cells. Required: effort, inertia cost per sprint, inertia offset (sprints to crossover), team control, adoption friction, time to value.

---

### Phase 7: Assumption Register

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 8: Risk Register

Minimum 2 entries. Use Phase 3 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action]

---

### Phase 9: Recommendation -- Dual Signature Form

Both signatures required. INCOMPLETE STATUS reads COMPLETE only when both blocks are structurally distinct.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name or "none found."
                     Must address why chosen option's INERTIA OFFSET justifies its cost.]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  INERTIA OVERRIDE: [State that chosen option's INERTIA OFFSET beats INERTIA COST -- cite numbers]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [C-NN compliance or exception with justification]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 10: Amend Phase

All three sections required. Each entry: OWNER, NEXT ACTION, DEADLINE.

#### MISSING OPTION

```
[Unexplored approach]
OWNER:       [role/team]
NEXT ACTION: [investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted dimension + why]
OWNER:       [role/team]
NEXT ACTION: [recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

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

## V-04: F-Row Linkage + Prerequisite Gate + Project-Specific Anchors

**Axis**: C-15 + C-16 + C-17 combined
**Hypothesis**: V-01's 3-field F-row template with typed F-ROW ANCHOR slot (C-15) + V-02's PREREQUISITE GATE (C-17) + V-03's project-specific anchor precision (C-16) together cover the three most structurally demanding new v4 criteria. The PREREQUISITE GATE pre-verifies F-row anchor presence before the recommendation is written, catching C-15 omission at the gate rather than at review. C-14 inherited (DEADLINE typed in all 3 amend categories). C-18 fails by design -- the single controlled discriminator between V-04 and V-05.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Complete phases in order; the PREREQUISITE GATE must pass before writing Phase 12. Role labels are mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none, state gap + inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** enumerates constraints before options:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed.

---

### Phase 3: PM -- Decision Frame

```
THE QUESTION:         [One interrogative sentence]
WHY NOW:              [Specific event or cost pressure]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- no vague temporal language]
INACTION CONSEQUENCE: [What teams lose or are blocked by if TEMPORAL ANCHOR passes]
```

---

### Phase 4: Risk Scoring Guide

Project-specific anchors required. Each anchor describes a named outcome in this project's context. Anchors must be project-specific, not generic severity descriptions.

```
PROBABILITY (1-5, this project):
  1: [Named condition making outcome unlikely for this project]
  3: [Named typical-trouble outcome -- specific to this project, not a generic category]
  5: [Named condition making outcome near-certain here]

IMPACT (1-5, this project):
  1: [Named low-impact example in this project's context]
  3: [Named specific medium-impact consequence here]
  5: [Named high-impact outcome in this project]
```

Holistic L/M/H labels fail. Every risk field must carry P, I, and P*I.

---

### Phase 5: Option 0 -- Do Nothing / Status Quo

| Field | Content |
|-------|---------|
| Description | Current state |
| Pros | Low switching cost, familiarity |
| Cons | Specific capability gaps |
| Risk | P: [1-5] x I: [1-5] = P*I: [N] -- [named risk] |
| Effort | 0 weeks. |
| Accumulation | [Metric + rate of drift per sprint/month] |

**Architect note**: Technical stability horizon.

---

### Phase 6: Alternatives (Minimum 3)

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What it does |
| Pros | Advantages over Option 0 |
| Cons | Costs vs. Option 0 |
| Risk | P: [1-5] x I: [1-5] = P*I: [N] -- [named risk] |
| Effort | N weeks + team + dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register

Minimum 2 entries.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register

Minimum 2 entries. Use Phase 4 anchors.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action]

---

### Phase 10: Failure Mode Register

Minimum 2 entries. Distinct from Phase 9 Risk Register. Failure modes describe conditions that would invalidate the recommendation -- not risk events during implementation. Each entry must include all three named fields.

```
F-NN:
  FAILURE MODE:       [What goes wrong -- the specific failure, named precisely]
  TRIGGER CONDITION:  [Observable event or threshold that confirms this failure mode has
                       activated -- name who observes it, what signal, and when]
  MITIGATION:         [Specific escalation path or fallback -- name an option letter or
                       next action; "reconsider" and "revisit" are not acceptable]
```

Each F-NN must cross-reference A-NN or R-NN by ID.

---

### Phase 11: Prerequisite Gate

Complete before writing Phase 12. Do not write the recommendation if GATE STATUS is BLOCKED.

```
PREREQUISITE GATE
  ASSUMPTION REGISTER:   [COMPLETE / INCOMPLETE -- Phase 8, >= 2 entries]
  RISK REGISTER:         [COMPLETE / INCOMPLETE -- Phase 9, >= 2 entries]
  FAILURE MODE REGISTER: [COMPLETE / INCOMPLETE -- Phase 10, >= 2 F-rows]
  REGISTERS PRECEDE REC: [YES / NO -- Phases 8 and 9 appear before this gate]
  F-ROW ANCHOR READY:    [F-NN: the F-row ID to cite in PM CONDITIONS]
  GATE STATUS:           [OPEN / BLOCKED]
```

---

### Phase 12: Recommendation -- Dual Signature Form

Both signatures required. INCOMPLETE STATUS reads COMPLETE only when both blocks are structurally distinct.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name or "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation. Name the F-row and condition.]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [C-NN compliance or exception with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode that would cause Architect reassessment]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 13: Amend Phase

All three sections required. Each entry: OWNER, NEXT ACTION, DEADLINE (specific -- "TBD" fails).

#### MISSING OPTION

```
[Unexplored approach]
OWNER:       [role/team]
NEXT ACTION: [investigation step]
DEADLINE:    [named sprint, date, or milestone]
```

#### UNWEIGHTED CRITERION

```
[Underweighted dimension + why]
OWNER:       [role/team]
NEXT ACTION: [recalibration step]
DEADLINE:    [named sprint, date, or milestone]
```

#### FOLLOW-UP

```
[Open question or prerequisite]
OWNER:       [role/team]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone]
```

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

## V-05: Full v4 Integration + STRUCTURE GUARD Cascade

**Axis**: All 5 new criteria (C-14 + C-15 + C-16 + C-17 + C-18) with STRUCTURE GUARD cascade (full integration)
**Hypothesis**: V-04 satisfies C-14 through C-17 but fails C-18. The difference is the front-loaded amendment table -- initialized before Phase 1 with auto-generate trigger rules (T-01 through T-GUARD) naming criterion IDs and conditions. The critical new mechanism over R3 V-05: T-GUARD (STRUCTURE GUARD). A single cascade trigger fires when any of the 5 required structural blocks is absent or bypassed, generating HIGH rows for C-14/C-15/C-16/C-17/C-18 simultaneously. No structural omission can be silent. A reviewer verifies v4 compliance from the AMENDMENT TABLE alone -- if T-GUARD fired, all 5 new criteria are at risk; if ENFORCED-CLEAN is declared, all 5 passed during writing.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Initialize the AMENDMENT TABLE before writing Phase 1. Role labels are mandatory. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### AMENDMENT TABLE (Initialize Before Phase 1)

Initialize this table before writing any phase. During writing, add HIGH rows when trigger conditions fire. At the Amend phase, complete any OWNER and DEADLINE fields. At document completion, either HIGH rows are present (enforcement failures caught) or write ENFORCED-CLEAN.

| # | Priority | Gap | Criterion | Section | OWNER | DEADLINE |
|---|----------|-----|-----------|---------|-------|----------|
| [auto-populated] | | | | | | |

**Trigger Chain** (add a HIGH row when triggered):

| Trigger ID | Condition | Criterion | Row content |
|------------|-----------|-----------|-------------|
| T-01 | TEMPORAL ANCHOR absent or contains vague language ("soon", "eventually", "near future") | C-13 | "TEMPORAL ANCHOR missing or vague -- Phase 3" |
| T-02 | INACTION CONSEQUENCE absent or states generic risk without naming teams blocked or capability lost | C-13 | "INACTION CONSEQUENCE generic or absent -- Phase 3" |
| T-03 | Any amend category (MISSING OPTION / UNWEIGHTED CRITERION / FOLLOW-UP) lacks OWNER typed slot | C-12 | "OWNER slot absent in [category] -- Amend phase" |
| T-04 | Any amend category lacks DEADLINE typed slot, or DEADLINE is TBD / blank | C-14 | "DEADLINE absent or TBD in [category] -- Amend phase" |
| T-05 | Risk field uses holistic L/M/H without separate numeric P and I | C-16 | "Holistic risk label in [phase/option] -- P and I not separated" |
| T-06 | P*I anchors are generic (no named project-specific outcomes) | C-16 | "Risk anchors are generic -- Phase 4 must describe this project's outcomes" |
| T-07 | Failure mode register absent or fewer than 2 F-rows | C-15 | "Failure mode register missing or incomplete -- Phase 10" |
| T-08 | Any F-row missing FAILURE MODE or TRIGGER CONDITION or MITIGATION field | C-15 | "F-row F-[n] missing required field -- Phase 10" |
| T-09 | PM SIGN-OFF CONDITIONS lacks F-ROW ANCHOR typed slot, or slot is blank | C-15 | "F-ROW ANCHOR absent in PM CONDITIONS -- Phase 12" |
| T-10 | Assumption register or risk register appears AFTER recommendation in document sequence | C-17 | "Registers appear after recommendation -- C-17 violated" |
| T-11 | PREREQUISITE GATE absent, BLOCKED, or bypassed before recommendation | C-17 | "Prerequisite gate missing or blocked -- Phase 11" |
| T-12 | INCOMPLETE STATUS absent from recommendation | C-13 | "Dual-signature gate absent -- Phase 12" |
| T-GUARD | Any of Phase 8 (Assumption Register), Phase 9 (Risk Register), Phase 10 (Failure Mode Register), Phase 11 (Prerequisite Gate), or this AMENDMENT TABLE is absent or bypassed | C-14, C-15, C-16, C-17, C-18 | "STRUCTURE GUARD: required structural block absent or bypassed -- C-14/C-15/C-16/C-17/C-18 all at risk" |

**ENFORCED-CLEAN declaration** (write at document completion only if no HIGH rows were generated):
> "AMENDMENT TABLE ENFORCED-CLEAN: all trigger conditions monitored during writing; no enforcement failures detected."

---

### Phase 1: Scout Artifact Inventory
**THIS PHASE CLOSES: C-05, C-10**

Scan for scout artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List each found artifact: name, date, key finding. If none, state gap + inline assessment. If scout inventory is skipped: fire T-GUARD.

---

### Phase 2: Architect -- Constraint Inventory
**THIS PHASE CLOSES: C-06 (partial)**

**Architect** enumerates constraints:
- Stack, integration, timeline, known failure modes

Label each C-NN. Fixed.

---

### Phase 3: PM -- Decision Frame
**THIS PHASE CLOSES: C-04, C-13**

```
THE QUESTION:         [One interrogative sentence -- fire T-01/T-02 if next two fields are absent or vague]
WHY NOW:              [Specific event or cost pressure]
TEMPORAL ANCHOR:      [Named date, sprint, or event -- fire T-01 if absent or vague]
INACTION CONSEQUENCE: [What teams lose or are blocked -- fire T-02 if generic]
```

---

### Phase 4: Risk Scoring Guide
**THIS PHASE CLOSES: C-16 (prep)**

Project-specific anchors required. Each anchor describes a concrete named outcome in this project's context. Fire T-06 if anchors are generic.

```
PROBABILITY (1-5, this project):
  1: [Named condition making outcome unlikely for this project]
  3: [Named typical-trouble outcome -- specific to this project, not a generic severity]
  5: [Named condition making outcome near-certain here]

IMPACT (1-5, this project):
  1: [Named low-impact example in this project]
  3: [Named specific medium-impact consequence here]
  5: [Named high-impact outcome in this project]
```

---

### Phase 5: Option 0 -- Do Nothing / Status Quo
**THIS PHASE CLOSES: C-01 (partial), C-02 (partial)**

| Field | Content |
|-------|---------|
| Description | Current state |
| Pros | Low switching cost, familiarity |
| Cons | Specific capability gaps |
| Risk | P: [1-5] x I: [1-5] = P*I: [N] -- [named risk; fire T-05 if L/M/H used] |
| Effort | 0 weeks. |
| Accumulation | [Metric + rate of drift per sprint/month] |

**Architect note**: Technical stability horizon.

---

### Phase 6: Alternatives (Minimum 3)
**THIS PHASE CLOSES: C-01, C-02**

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What it does |
| Pros | Advantages over Option 0 |
| Cons | Costs vs. Option 0 |
| Risk | P: [1-5] x I: [1-5] = P*I: [N] -- [named risk; fire T-05 if L/M/H used] |
| Effort | N weeks + team + dependencies |

**Architect constraint check**: C-NN compliance or named exception.

---

### Phase 7: Comparison Matrix
**THIS PHASE CLOSES: C-07**

Columns = all options. Rows = 4-6 dimensions. No empty cells. Required: effort, team control, adoption friction, time to value, risk P*I.

---

### Phase 8: Assumption Register
**THIS PHASE CLOSES: C-08 (partial)**

Minimum 2 entries. Fire T-GUARD if this phase is absent.

- A-NN: [Assumption] -- OWNER: [PM/Architect] -- VALIDATION PLAN: [Specific verification action]

---

### Phase 9: Risk Register
**THIS PHASE CLOSES: C-08, C-16**

Minimum 2 entries. Use Phase 4 anchors. Fire T-05 for any holistic label. Fire T-10 if written after Phase 12. Fire T-GUARD if this phase is absent.

- R-NN: [Risk] -- P: [1-5] -- I: [1-5] -- P*I: [N] -- OWNER: [PM/Architect] -- MITIGATION: [Specific action]

---

### Phase 10: Failure Mode Register
**THIS PHASE CLOSES: C-15**

Minimum 2 entries. Distinct from Risk Register. Each entry requires all three named fields. Fire T-07 if absent. Fire T-08 for any entry missing a required field. Fire T-GUARD if this phase is absent.

```
F-NN:
  FAILURE MODE:       [What goes wrong -- the specific failure, named precisely]
  TRIGGER CONDITION:  [Observable event or threshold -- who observes it, what signal, when]
  MITIGATION:         [Specific escalation path or fallback -- option letter or named action]
```

Each F-NN must reference A-NN or R-NN by ID.

---

### Phase 11: Prerequisite Gate
**THIS PHASE CLOSES: C-17**

Complete before writing Phase 12. Fire T-11 if gate is absent or BLOCKED. Fire T-GUARD if this phase is bypassed.

```
PREREQUISITE GATE
  ASSUMPTION REGISTER:   [COMPLETE / INCOMPLETE -- Phase 8, >= 2 entries]
  RISK REGISTER:         [COMPLETE / INCOMPLETE -- Phase 9, >= 2 entries]
  FAILURE MODE REGISTER: [COMPLETE / INCOMPLETE -- Phase 10, >= 2 F-rows]
  REGISTERS PRECEDE REC: [YES / NO -- Phases 8 and 9 appear before this gate]
  F-ROW ANCHOR READY:    [F-NN: the F-row to cite in PM CONDITIONS]
  GATE STATUS:           [OPEN / BLOCKED]
```

---

### Phase 12: Recommendation -- Dual Signature Form
**THIS PHASE CLOSES: C-03, C-06, C-13, C-15**

Both signatures required. Fire T-12 if INCOMPLETE STATUS is absent. Fire T-09 if F-ROW ANCHOR absent from PM CONDITIONS.

```
PM SIGN-OFF
  CHOSEN OPTION:    [letter + name]
  RATIONALE:        [2-3 sentences -- adoption, timeline, stakeholder fit.
                     Reference scout artifact by name or "none found."]
  CONDITIONS:       [2-3 conditions under which this recommendation remains valid]
  F-ROW ANCHOR:     [F-NN: the failure mode whose activation most directly invalidates
                     this recommendation -- fire T-09 if absent]
  CONFIDENCE:       [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Prerequisites -- at least one named]
  QUALIFICATIONS:       [Technical caveats -- at least one named]
  CONSTRAINT VERIFIED:  [C-NN compliance or exception with justification]
  F-ROW ANCHOR:         [F-NN: the failure mode that would cause Architect reassessment]
  ENDORSE / DISSENT:    [ENDORSE: [reason] | DISSENT: [reason + alternative]]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 13: Amend Phase
**THIS PHASE CLOSES: C-09, C-11, C-12, C-14**

Merge any AMENDMENT TABLE rows into appropriate categories. Each entry carries all three typed slots. Fire T-03 for any category missing OWNER. Fire T-04 if DEADLINE is TBD or blank.

#### MISSING OPTION

```
[Unexplored approach]
OWNER:       [role/team -- fire T-03 if absent]
NEXT ACTION: [specific investigation step]
DEADLINE:    [named sprint, date, or milestone -- fire T-04 if TBD or blank]
```

#### UNWEIGHTED CRITERION

```
[Underweighted dimension + why]
OWNER:       [role/team -- fire T-03 if absent]
NEXT ACTION: [specific recalibration step]
DEADLINE:    [named sprint, date, or milestone -- fire T-04 if TBD or blank]
```

#### FOLLOW-UP

```
[Open question or prerequisite]
OWNER:       [role/team -- fire T-03 if absent]
NEXT ACTION: [specific step]
DEADLINE:    [named sprint, date, or milestone -- fire T-04 if TBD or blank]
```

At document completion: review AMENDMENT TABLE. If no HIGH rows were generated, write ENFORCED-CLEAN declaration.

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

## Most Likely Golden

**V-05** -- the only variation where all 5 new v4 criteria (C-14 through C-18) are enforced by independent structural mechanisms. T-GUARD ensures no required structural block can be silently absent: a single missing block fires HIGH rows covering all 5 criteria simultaneously. A reviewer verifies v4 compliance from the AMENDMENT TABLE alone.

**V-04** is the strongest combination advance: 3-field F-row template + prerequisite gate + project-specific anchors covers C-15, C-16, C-17 structurally. C-18 is the single deliberate omission -- the controlled discriminator between V-04 and V-05.

**Risk assessments**:
- V-01: Safe single-axis advance. 3-field F-row template directly satisfies C-15's three-part requirement; F-ROW ANCHOR typed slot in both PM and Architect CONDITIONS closes the instruction-vs-structure gap from R3. C-18 fails by design.
- V-02: Prerequisite gate is additive and lossless -- a checklist block before recommendation cannot degrade any existing criterion. C-18 fails by design.
- V-03: Most divergent variation. INERTIA COST and INERTIA OFFSET quantify the status-quo cost in a way the rubric does not yet test. C-15 and C-18 fail by design. Value: seeds quality-level metrics (computable inertia crossover) for v5 criteria candidates.
- V-04: Controlled combination. C-18 deliberately omitted to test whether the front-loaded amendment table is genuinely required vs. redundant given the prerequisite gate. If V-04 produces equivalent quality outputs to V-05 in practice, the front-loaded table adds overhead without additional compliance gain.
- V-05: Most ambitious. T-GUARD fires when any required structural block is absent; named trigger IDs (T-01 through T-GUARD) make each amendment row traceable to its source rule. ENFORCED-CLEAN at document completion is the positive signal: all 13 trigger conditions were monitored and none fired.
