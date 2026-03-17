The R1 variations file already exists with complete content from a prior session. Here is the variation set:

---

# draft-proposal — Variation Set R1

| ID | Axis | Hypothesis | Key criteria targeted |
|----|------|------------|-----------------------|
| **V-01** | Inertia framing | Option 0 mandatory first — all alternatives must beat it; C-04 cost-of-inaction forced before options structurally | C-01, C-04 |
| **V-02** | Role sequence (Architect-first) | Architect locks constraint envelope (C-NN labels) before PM names options; effort fields are grounded in real implementation complexity | C-02, C-06 |
| **V-03** | Output format — slot structure | Named key=value slots per option; model cannot produce the structure without filling risk + effort; direct C-02 defense | C-01, C-02, C-03 |
| **V-04** | Conversational register + compressed lifecycle | Second-person single-pass; faster essential coverage; C-08 at risk; baseline discriminator | C-01–C-04 |
| **V-05** | Inertia-first + Architect-first + Formal (combo) | Closes all four common failure modes; mandatory amend taxonomy (MISSING OPTION / UNWEIGHTED CRITERION / FOLLOW-UP) makes C-09 a self-check inside generation | C-01–C-09 |

---

**V-01 — Inertia-First Framing**

Single axis. Positions Do Nothing as Option 0 — the mandatory first option that all alternatives must beat. PM owns the decision frame (question, urgency, cost of inaction) and it must appear before options. Alternatives each explicitly address why they improve on Option 0's cons.

---

**V-02 — Architect-First Role Sequence**

Single axis. Architect runs before PM, locking a C-NN constraint envelope (stack, integration, timeline, failure modes). No option may violate a constraint without explicit justification. PM frames the decision only after the technical bounds are set. Recommendation requires both roles to sign.

---

**V-03 — Slot-Structure Output Format**

Single axis. Every option uses a fixed `OPTION / NAME / DESCRIPTION / PROS / CONS / RISK / EFFORT / ARCHITECT NOTE` slot template. The model cannot produce the structure without filling risk probability/impact and effort weeks. Structural defense against C-02 omissions.

---

**V-04 — Conversational Register + Compressed Lifecycle**

Combined axis (register + lifecycle). Second-person direct voice ("You're writing a proposal..."), fewer prescribed phases, lighter framing. Intended as a lower-bound baseline: if C-02 passes here, the criterion is not discriminating at this difficulty level. C-08 (registers) is most at risk.

---

**V-05 — Inertia-First + Architect-First + Formal (Combo)**

Combined axis (three). Combines V-01 + V-02 + formal imperative register. Phase 10 Amend mandates three explicit categories: MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP — making C-09 a self-check inside generation. Highest-ceiling candidate.

---

**Most likely golden candidate**: V-05 — combination closes every common failure mode. V-03 is the structural safety net if V-05 proves too verbose for practical use.

File written to: `simulations/quest/variations/draft-proposal-variations-R1-2026-03-14.md`
t)

Before generating alternatives, document what teams do today.

**Option 0: Do Nothing / Current State**

| Field | Content |
|-------|---------|
| Description | What teams do today to solve this problem (or how they avoid it) |
| Pros | Why teams stay here: low friction, familiarity, no migration cost |
| Cons | What they sacrifice by staying: capability gaps, scaling limits, maintenance burden |
| Risk | What deteriorates over time: named risk + PROBABILITY [L/M/H] + IMPACT [L/M/H] |
| Effort | 0 -- this is the baseline |

All alternatives are evaluated as improvements over Option 0. An option that does not improve on at least two of Option 0's cons is not worth including.

---

## Phase 3: Alternatives (Minimum 3)

Generate at least 3 alternatives to Option 0. For each:

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it differs from Option 0 |
| Pros | Concrete advantages over Option 0 |
| Cons | Concrete costs or limitations vs. Option 0 |
| Risk | Named risk + PROBABILITY (L/M/H) + IMPACT (L/M/H) |
| Effort | Weeks to implement + team size assumption |

After all options are documented, **Architect** adds a technical note for each: constraints, dependencies, or implementation risks not visible from the trade-off table alone.

---

## Phase 4: Structured Comparison

Build a dimension table with all options as columns (including Option 0). Rows are shared dimensions relevant to the decision (e.g., install friction, team control, time to value, customization). Every cell must be filled. No empty cells.

---

## Phase 5: Recommendation

**PM** states:
- The chosen option (letter + name)
- Why it wins over the alternatives (2-3 sentences referencing the comparison table)
- Confidence level: HIGH / MEDIUM / LOW
- Conditions: 2-3 specific things that must be true for this recommendation to hold

If a scout artifact exists (feasibility, competitors, requirements, stakeholders), reference it by name and note whether its findings confirm or complicate the recommendation.

---

## Phase 6: Assumption and Risk Registers

**Assumption register** (at least 2 entries):
- A-NN: [assumption] -- VALIDATION: [how to verify before commitment]

**Risk register** (at least 2 entries):
- R-NN: [risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [action]

---

## Phase 7: Amend

List 1-3 gaps in this proposal:
- Missing options not yet explored
- Decision criteria that need explicit weighting
- Follow-up work required before the decision can be finalized

---

## Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-02: Architect-First Role Sequence

**Axis**: Role sequence (single-axis)
**Hypothesis**: Running Architect first to enumerate technical constraints creates a locked constraint envelope that PM must work within. This prevents options from being technically unconstrained ideals and forces C-02 effort fields to be grounded in actual implementation complexity the Architect surfaced.

---

You are authoring a proposal artifact for the Signal plugin.

**Invocation**: `/draft-proposal "{topic}"`

---

## Step 1: Scout Artifact Inventory

Check for existing signal artifacts:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

List what was found. If nothing found, note "No scout artifacts -- inline assessment required."

---

## Step 2: Architect -- Constraint Envelope

**Architect** runs first. Before any options are named, enumerate the technical constraints that bound the solution space:

1. Stack constraints (language, runtime, platform, OS compatibility)
2. Integration constraints (existing APIs, protocols, dependencies)
3. Timeline constraints (what is achievable in what window, with what team size)
4. Known failure modes (technical risks that could invalidate an option regardless of its other merits)

Label each C-NN. These constraints are locked. No option may propose violating them without an explicit justification.

---

## Step 3: PM -- Decision Frame

With the constraint envelope established, **PM** frames the decision. This section appears before the options in the output:

1. **The Question**: What decision is being made?
2. **Why Now**: What event, deadline, or cost makes this urgent? Name it.
3. **Cost of Inaction**: What consequence accrues if no decision is made?

---

## Step 4: Options Generation

Generate at least 3 options. One must be a do-nothing / status-quo option. For each option, all fields are required -- omitting any field fails the proposal:

**Option [Letter]: [Name]**

- **Description**: What this approach is and how it works
- **Pros**: Specific advantages (reference constraint envelope where relevant)
- **Cons**: Specific costs, limitations, or trade-offs
- **Risk**: Named risk + PROBABILITY (LOW/MEDIUM/HIGH) + IMPACT (LOW/MEDIUM/HIGH)
- **Effort**: Estimated weeks to implement, team size assumption, key dependencies

**Architect constraint check** (per option): Does this option comply with all C-NN constraints? If a constraint is violated, state which and whether a justification overrides it.

---

## Step 5: Structured Comparison

PM and Architect produce a comparison matrix. Columns = options. Rows = 4-6 shared dimensions that reflect the decision's key trade-offs (e.g., effort, friction, control, timeline, risk). Every cell filled. Dimensions consistent across all options.

---

## Step 6: Recommendation

**PM** leads:
- Chosen option (letter + name)
- Business rationale: why this option serves adoption, timeline, and stakeholder needs
- Conditions: what must hold for this recommendation to remain valid
- Confidence: HIGH / MEDIUM / LOW

**Architect** confirms or qualifies:
- Technical confidence in the chosen option
- Implementation preconditions
- Any technical caveats on the PM recommendation

Both roles must speak. A recommendation signed by only one role is incomplete.

---

## Step 7: Registers

**Assumption register** (minimum 2):
- A-NN: [assumption] -- VALIDATION: [plan]

**Risk register** (minimum 2):
- R-NN: [risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [plan]

---

## Step 8: Amend Phase

Self-critique the proposal. Name at least one:
- Option not yet explored
- Decision criterion that needs explicit weighting
- Follow-up action required before this proposal can be finalized

---

## Output

Write to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-03: Slot-Structure Output Format

**Axis**: Output format (single-axis)
**Hypothesis**: Providing a per-option template with named key=value slots prevents structural omissions at generation time. A model cannot produce a slot-structured output without filling the risk and effort fields -- directly targeting C-02, the most discriminating criterion.

---

You are drafting a Signal proposal artifact. Strict slot structure is required -- every labeled field must be present in the output. Omitting any field fails the proposal.

**Invocation**: `/draft-proposal "{topic}"`

---

## SLOT: Decision Context

Fill all four slots before listing any options:

```
QUESTION:        [The decision being made -- one interrogative sentence]
URGENCY:         [Why this matters now -- deadline, cost, or event; no vague language]
INACTION COST:   [Consequence teams experience if no decision is reached -- one sentence, PM voice]
SCOUT ARTIFACTS: [List file names found at simulations/scout/*/; or "none -- inline assessment below"]
```

---

## SLOT: Option A -- Do Nothing / Status Quo (required, always first)

```
OPTION:       A
NAME:         Do Nothing / Status Quo
DESCRIPTION:  [What teams do today instead of adopting a solution]
PROS:         [Why teams stay here -- familiarity, zero switching cost, no migration risk]
CONS:         [Specific capability gaps or maintenance burdens teams accept]
RISK:         [Named risk] | PROBABILITY: [L/M/H] | IMPACT: [L/M/H]
EFFORT:       0 weeks -- no implementation required
```

---

## SLOT: Option B (required)

```
OPTION:           B
NAME:             [Name]
DESCRIPTION:      [What this approach is and how it works]
PROS:             [Specific advantages]
CONS:             [Specific costs or limitations]
RISK:             [Named risk] | PROBABILITY: [L/M/H] | IMPACT: [L/M/H]
EFFORT:           [N weeks] | TEAM: [size assumption] | DEPENDENCIES: [list or "none"]
ARCHITECT NOTE:   [Technical constraint check -- does this respect known stack/timeline constraints?]
```

---

## SLOT: Option C (required)

```
OPTION:           C
NAME:             [Name]
DESCRIPTION:      [What this approach is and how it works]
PROS:             [Specific advantages]
CONS:             [Specific costs or limitations]
RISK:             [Named risk] | PROBABILITY: [L/M/H] | IMPACT: [L/M/H]
EFFORT:           [N weeks] | TEAM: [size assumption] | DEPENDENCIES: [list or "none"]
ARCHITECT NOTE:   [Technical constraint check]
```

---

## SLOT: Option D+ (add as needed)

Use the same template as Option B/C for each additional option. Minimum total: 4 options (A through C plus at least one more).

---

## SLOT: Comparison Matrix

Build a table. Columns = all options. Rows = 4-6 shared dimensions. Every cell filled. No empty cells. Dimensions must be consistent across all columns.

| Dimension     | Option A | Option B | Option C | Option D |
|---------------|----------|----------|----------|----------|
| [dimension 1] |          |          |          |          |
| [dimension 2] |          |          |          |          |
| [dimension 3] |          |          |          |          |
| [dimension 4] |          |          |          |          |

---

## SLOT: Recommendation

```
PM RECOMMENDATION:
  CHOSEN OPTION:  [letter + name]
  RATIONALE:      [Why this option wins -- 2-3 sentences, reference comparison matrix]
  CONDITIONS:     [2-3 things that must hold for this recommendation to remain valid]
  CONFIDENCE:     [HIGH / MEDIUM / LOW]
  SCOUT SUPPORT:  [Scout artifact that confirms or complicates this; or "none found"]

ARCHITECT CONFIRMATION:
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Implementation prerequisites]
  QUALIFICATIONS:       [Technical caveats on the PM recommendation, or "none"]
```

---

## SLOT: Assumption Register

At least 2 entries:

```
A-01: [Assumption] -- VALIDATION: [How to verify before committing]
A-02: [Assumption] -- VALIDATION: [How to verify before committing]
```

---

## SLOT: Risk Register

At least 2 entries:

```
R-01: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Action]
R-02: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Action]
```

---

## SLOT: Amend

At least 1 entry:

```
AMEND-01: [Gap, missing option, unweighted criterion, or required follow-up action]
```

---

## Output

Write to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-04: Conversational Register + Compressed Lifecycle

**Axis**: Phrasing register + lifecycle emphasis (combined single-test)
**Hypothesis**: A shorter second-person prompt with fewer prescribed phases produces faster coverage of essential criteria with less structural overhead. C-01 through C-04 should still pass. C-08 (registers) is at risk because the lighter framing may produce shallow or omitted entries. Functions as a lower-bound baseline for discriminating which criteria require explicit enforcement vs. which emerge from lighter prompting.

---

You're writing a proposal for Signal. Keep it direct -- every section earns its place.

**Invocation**: `/draft-proposal "{topic}"`

---

Start by looking for scout work already done:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`

Note what you found at the top of the output. If nothing exists, say so and add a quick inline assessment.

---

**Frame the decision.** Three sentences max. PM writes this -- it goes first.

1. What decision is being made?
2. Why does it need to be made now?
3. What's the cost if it isn't made?

---

**List your options.** Minimum 4. One must be "do nothing."

For each option, fill out every field -- skipping risk or effort turns this into a list of ideas, not a proposal:

- **Name**: Short label
- **What it is**: One paragraph
- **Pros**: Bullet list
- **Cons**: Bullet list
- **Risk**: Named risk, probability (HIGH / MEDIUM / LOW), impact (HIGH / MEDIUM / LOW)
- **Effort**: Weeks to ship + team size assumption

After all options are listed, Architect adds a note per option: technical feasibility, constraints, or blockers not visible from pros/cons alone.

---

**Comparison table.** All options as columns. Pick 4-6 dimensions that matter for this decision. Fill every cell.

---

**Recommendation.** Name the option you'd go with. Say why it beats the alternatives in 2-3 sentences. Add 2-3 conditions that must hold for this to stay the right call. State your confidence (HIGH / MEDIUM / LOW). Architect confirms or adds a caveat. Reference any scout artifact you found -- does it support the recommendation?

---

**Registers.** Two quick lists:

Assumptions (at least 2):
- A-NN: what must be true -- how you'd validate it

Risks (at least 2):
- R-NN: what could go wrong -- probability, impact, mitigation

---

**Amend.** Before closing, name 1-3 things this proposal doesn't yet handle well: missing options, criteria that need weighting, or questions that need answers before the decision is final.

---

Write the full proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```

---

## V-05: Inertia-First + Architect-First + Formal Register (Combo)

**Axis**: Inertia framing + role sequence + phrasing register (combined)
**Hypothesis**: Combining Option-0-mandatory (V-01) with Architect-first constraint locking (V-02) and a formal imperative register produces the highest-ceiling output. The combination closes all four common failure modes simultaneously: Option 0 is structurally first (C-01), Architect constraint envelope forces real effort estimates (C-02), phased role contributions prevent interchangeable PM/Architect prose (C-06), and a mandatory amend taxonomy (MISSING OPTION / UNWEIGHTED CRITERION / FOLLOW-UP) makes C-09 a self-check inside generation rather than a post-hoc scoring criterion.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

## Phase 1: Scout Artifact Inventory

Scan for:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

Record for each found artifact: file name, date, and the single most relevant finding for this decision. If no artifacts exist, note the gap and proceed with inline assessment.

---

## Phase 2: Architect -- Constraint Inventory

**Architect** runs first. Enumerate all constraints that bound the solution space before any options are named:

- Stack constraints: language, runtime, platform, OS compatibility
- Integration constraints: existing APIs, protocols, dependency limits
- Timeline constraints: what is achievable in what window, at what team size
- Known failure modes: technical risks that could invalidate an option regardless of its other merits

Label each C-NN. These are fixed. No option may propose violating a constraint without an explicit justification. Record the count of constraints found.

---

## Phase 3: PM -- Decision Frame

With the constraint envelope established, **PM** frames the decision. This section appears verbatim in the output before any options:

1. **THE QUESTION**: The decision to be made, stated as a single interrogative sentence.
2. **WHY NOW**: The specific event, deadline, or cost pressure that makes deferral harmful. Name it explicitly. Do not use "soon," "eventually," or "in the near future."
3. **COST OF INACTION**: One sentence stating what accrues if no decision is made -- framed as a consequence teams will experience, not a feature they will miss.

---

## Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

The status quo is always Option 0 and always comes first. All alternatives are evaluated as improvements over it.

**Option 0: Do Nothing / Status Quo**

| Field | Content |
|-------|---------|
| Description | What teams do today to solve this problem, or how they avoid it entirely |
| Pros | Low switching cost, familiarity, zero migration risk -- be specific to this domain |
| Cons | Enumerate specific capability gaps or maintenance burdens teams accept by staying here |
| Risk | What deteriorates over time: named risk + PROBABILITY [L/M/H] + IMPACT [L/M/H] |
| Effort | 0 weeks. No implementation required. |

**Architect note**: Is the status quo technically stable? Are there deprecations, platform shifts, or scaling limits that will erode its viability on a visible timeline?

---

## Phase 5: Alternatives (Minimum 3)

For each alternative, complete all fields. Any omitted field disqualifies the proposal.

**Option [Letter]: [Name]**

| Field | Content |
|-------|---------|
| Description | What this approach is and how it works |
| Pros | Concrete advantages over Option 0 |
| Cons | Concrete costs, limitations, or trade-offs vs. Option 0 |
| Risk | Named risk + PROBABILITY [L/M/H] + IMPACT [L/M/H] |
| Effort | N weeks + team size assumption + key dependencies |

**Architect constraint check**: Does this option comply with all C-NN constraints? If any constraint is violated, state which, and whether a justification overrides it.

---

## Phase 6: Comparison Matrix

PM and Architect produce a joint comparison table. Columns = all options (0 through N). Rows = 4-6 dimensions chosen to represent the decision's core trade-offs. No empty cells. Dimensions must be consistent across all options. Required dimensions: effort, team control, adoption friction, time to value. Add domain-specific dimensions as warranted.

---

## Phase 7: Recommendation

**PM** leads with the business recommendation:

- CHOSEN OPTION: [letter + name]
- RATIONALE: Why this option serves adoption, timeline, and stakeholder needs. Reference at least one scout artifact finding if available; note absence if not.
- CONDITIONS: 2-3 specific conditions that must hold for this recommendation to remain valid.
- CONFIDENCE: HIGH / MEDIUM / LOW

**Architect** confirms or qualifies:

- TECHNICAL CONFIDENCE: HIGH / MEDIUM / LOW
- PRECONDITIONS: Implementation prerequisites that must be resolved before the chosen option is viable.
- QUALIFICATIONS: Any technical caveats on the PM recommendation. If none, state "none."

Both roles must contribute. A recommendation signed by only one role is incomplete.

---

## Phase 8: Assumption Register

At least 2 entries. Validation plans must specify a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- VALIDATION PLAN: [Specific action to verify this before commitment]

---

## Phase 9: Risk Register

At least 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

## Phase 10: Amend Phase

Self-critique this proposal before closing. Name at least one item per category:

- MISSING OPTION: An approach not yet explored that a skeptical reviewer would raise.
- UNWEIGHTED CRITERION: A dimension in the comparison matrix that likely deserves higher weight but was treated as equal to others.
- FOLLOW-UP: A question or prerequisite that must be resolved before this proposal can be finalized and acted on.

---

## Output

Write the complete proposal to: `simulations/draft/proposals/{topic}-proposal-{date}.md`

```yaml
---
skill: draft-proposal
topic: {topic}
date: {date}
---
```
