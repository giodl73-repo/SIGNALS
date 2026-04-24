The R2 variations file already contains complete content from a prior session. The full set is ready.

---

**draft-proposal — Variation Set R2** written to `simulations/quest/variations/draft-proposal-variations-R2-2026-03-14.md`.

---

**Changes from R1:**

**Three new structural enforcement mechanisms:**

- **V-01 — Amend Header Structure + OWNER field** (`behavior`): Named sub-headers per amend category with required OWNER and NEXT ACTION fields. V-05 R1 required "at least one item per category" but produced entries without owners. This closes C-10's completeness gap without changing any other phase.

- **V-02 — Recommendation Dual-Signature Form** (`format`): Typed PM/ARCHITECT sign-off blocks with CONSTRAINT VERIFIED field and INCOMPLETE STATUS footer. A model cannot set status to COMPLETE with interchangeable prose under two role headers. CONSTRAINT VERIFIED ties the Architect back to Phase 2 C-NN labels explicitly.

- **V-03 — Temporal Anchor as Separate Typed Fields** (`format`): Splits WHY NOW into two required fields: TEMPORAL ANCHOR (specific named date/sprint/event) and INACTION CONSEQUENCE (concrete named outcome). V-05 R1's prohibition (`do not write "soon"`) could be satisfied with an anchor that is technically named but consequence-free. Two separate fields cannot.

| ID | Axis | Key criteria targeted |
|----|------|-----------------------|
| **V-01** | Amend phase: mandatory headers + OWNER field (single-axis) | C-10 |
| **V-02** | Recommendation: dual-signature form with INCOMPLETE STATUS (single-axis) | C-11 |
| **V-03** | Decision frame: split TEMPORAL ANCHOR + INACTION CONSEQUENCE (single-axis) | C-12 |
| **V-04** | Amend headers + temporal anchor in conversational register (combo) | C-10, C-12 |
| **V-05** | Full integration: all three mechanisms on V-05 R1 base (combo) | C-10, C-11, C-12 |

**Design principle for R2**: Each enforcement mechanism targets the "present but satisfiable with garbage" failure mode. V-05 R1 used prohibition; R2 uses form structure — you cannot fill `INCOMPLETE STATUS: COMPLETE` without distinct Architect content, you cannot fill `TEMPORAL ANCHOR` without a named date or event, you cannot leave the `MISSING OPTION` header empty without violating the section requirement.

**Most likely golden**: V-05.
**Open question**: V-04's C-11 — does the existing dual-role language satisfy C-11 without an explicit incompleteness clause? V-04 deliberately omits the clause to test whether it is load-bearing.
ry named sub-headers -- one per taxonomy category -- plus a required OWNER field per entry enforces two requirements simultaneously: (1) category labels appear structurally in the output, satisfying C-10's classification requirement; (2) owner or next action is a required entry field, satisfying C-10's completeness requirement that V-05 R1 lacked. V-05 R1 required "at least one item per category" but produced `- CATEGORY: description` without an owner. Under R2, that passes C-09 but fails C-10.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

Record for each found artifact: file name, date, and the single most relevant finding for this decision. If no artifacts exist, note the gap and proceed with inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** runs first. Enumerate all constraints that bound the solution space before any options are named:

- Stack constraints: language, runtime, platform, OS compatibility
- Integration constraints: existing APIs, protocols, dependency limits
- Timeline constraints: what is achievable in what window, at what team size
- Known failure modes: technical risks that could invalidate an option regardless of its other merits

Label each C-NN. These are fixed. No option may propose violating a constraint without an explicit justification. Record the count of constraints found.

---

### Phase 3: PM -- Decision Frame

With the constraint envelope established, **PM** frames the decision. This section appears verbatim in the output before any options:

1. **THE QUESTION**: The decision to be made, stated as a single interrogative sentence.
2. **WHY NOW**: The specific event, deadline, or cost pressure that makes deferral harmful. Name it explicitly. Do not use "soon," "eventually," or "in the near future."
3. **COST OF INACTION**: One sentence stating what accrues if no decision is made -- framed as a consequence teams will experience, not a feature they will miss.

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

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

### Phase 5: Alternatives (Minimum 3)

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

### Phase 6: Comparison Matrix

PM and Architect produce a joint comparison table. Columns = all options (0 through N). Rows = 4-6 dimensions chosen to represent the decision's core trade-offs. No empty cells. Dimensions must be consistent across all options. Required dimensions: effort, team control, adoption friction, time to value. Add domain-specific dimensions as warranted.

---

### Phase 7: Recommendation

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

### Phase 8: Assumption Register

At least 2 entries. Validation plans must specify a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- VALIDATION PLAN: [Specific action to verify this before commitment]

---

### Phase 9: Risk Register

At least 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Amend Phase

Self-critique this proposal. Each section below is a required output section. Write at least one entry per section. Each entry must include a description and an OWNER (the role or team responsible for resolution).

#### MISSING OPTION

An approach not yet explored that a skeptical reviewer would raise.

`[Description of the unexplored option] -- OWNER: [role or team] -- NEXT ACTION: [what investigation would determine whether it belongs in a revised proposal]`

#### UNWEIGHTED CRITERION

A dimension in the comparison matrix that likely deserves higher weight than it received.

`[Which dimension and why it is underweighted] -- OWNER: [role or team] -- NEXT ACTION: [how to weight it explicitly and what effect that would have on the recommendation]`

#### FOLLOW-UP

A question or prerequisite that must be resolved before this proposal can be finalized and acted on.

`[The open question or prerequisite] -- OWNER: [role or team] -- DEADLINE: [named date or event by which this must be resolved]`

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

## V-02: Recommendation Dual-Signature Form

**Axis**: Recommendation section structure (single-axis)
**Hypothesis**: Replacing the prose-based recommendation with a typed dual-signature form containing an INCOMPLETE STATUS footer makes C-11 a mechanical completion requirement. A model producing interchangeable prose under two role headers cannot set INCOMPLETE STATUS to COMPLETE if the Architect block lacks distinct PRECONDITIONS and CONSTRAINT VERIFIED content. The CONSTRAINT VERIFIED field also ties the Architect signature back to the C-NN constraint work from Phase 2, reinforcing C-06 depth beyond what V-05 R1 required.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

Record for each found artifact: file name, date, and the single most relevant finding for this decision. If no artifacts exist, note the gap and proceed with inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** runs first. Enumerate all constraints that bound the solution space before any options are named:

- Stack constraints: language, runtime, platform, OS compatibility
- Integration constraints: existing APIs, protocols, dependency limits
- Timeline constraints: what is achievable in what window, at what team size
- Known failure modes: technical risks that could invalidate an option regardless of its other merits

Label each C-NN. These are fixed. No option may propose violating a constraint without an explicit justification. Record the count of constraints found.

---

### Phase 3: PM -- Decision Frame

With the constraint envelope established, **PM** frames the decision. This section appears verbatim in the output before any options:

1. **THE QUESTION**: The decision to be made, stated as a single interrogative sentence.
2. **WHY NOW**: The specific event, deadline, or cost pressure that makes deferral harmful. Name it explicitly. Do not use "soon," "eventually," or "in the near future."
3. **COST OF INACTION**: One sentence stating what accrues if no decision is made -- framed as a consequence teams will experience, not a feature they will miss.

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

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

### Phase 5: Alternatives (Minimum 3)

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

### Phase 6: Comparison Matrix

PM and Architect produce a joint comparison table. Columns = all options (0 through N). Rows = 4-6 dimensions chosen to represent the decision's core trade-offs. No empty cells. Dimensions must be consistent across all options. Required dimensions: effort, team control, adoption friction, time to value. Add domain-specific dimensions as warranted.

---

### Phase 7: Recommendation -- Dual Signature Form

Complete both signature blocks in full. INCOMPLETE STATUS must read COMPLETE only when both blocks contain distinct, non-interchangeable content. Interchangeable prose under two role headers is a fail.

```
PM SIGN-OFF
  CHOSEN OPTION:   [letter + name]
  RATIONALE:       [Why this option serves adoption, timeline, and stakeholder needs --
                    2-3 sentences. Reference scout artifact by name if available;
                    state "none found" if not.]
  CONDITIONS:      [2-3 specific conditions that must hold for this recommendation
                    to remain valid]
  CONFIDENCE:      [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Implementation prerequisites that must be resolved before
                         the chosen option is viable -- at least one named item,
                         not "none"]
  QUALIFICATIONS:       [Technical caveats on the PM recommendation -- at least one
                         named item, or "none" only if the Architect fully concurs
                         with no technical reservations]
  CONSTRAINT VERIFIED:  [Confirm chosen option complies with all Phase 2 C-NN
                         constraints, or identify which constraint requires exception
                         and state the justification]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

---

### Phase 8: Assumption Register

At least 2 entries. Validation plans must specify a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- VALIDATION PLAN: [Specific action to verify this before commitment]

---

### Phase 9: Risk Register

At least 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Amend Phase

Self-critique this proposal before closing. Name at least one item per category:

- MISSING OPTION: An approach not yet explored that a skeptical reviewer would raise.
- UNWEIGHTED CRITERION: A dimension in the comparison matrix that likely deserves higher weight but was treated as equal to others.
- FOLLOW-UP: A question or prerequisite that must be resolved before this proposal can be finalized and acted on.

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

## V-03: Temporal Anchor as Separate Typed Fields

**Axis**: Decision frame field granularity (single-axis)
**Hypothesis**: Splitting WHY NOW into two required fields -- TEMPORAL ANCHOR (a specific named date, sprint, or event) and INACTION CONSEQUENCE (a concrete named outcome) -- enforces C-12 at the field level rather than the paragraph level. V-05 R1 prohibited vague temporal language but placed anchor and consequence in a single WHY NOW statement. A model can satisfy the prohibition with an anchor that is technically named but consequence-free ("the Q2 planning window opens"). Two separate mandatory fields cannot be satisfied without producing both a specific anchor and a distinct concrete consequence.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

Record for each found artifact: file name, date, and the single most relevant finding for this decision. If no artifacts exist, note the gap and proceed with inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** runs first. Enumerate all constraints that bound the solution space before any options are named:

- Stack constraints: language, runtime, platform, OS compatibility
- Integration constraints: existing APIs, protocols, dependency limits
- Timeline constraints: what is achievable in what window, at what team size
- Known failure modes: technical risks that could invalidate an option regardless of its other merits

Label each C-NN. These are fixed. No option may propose violating a constraint without an explicit justification. Record the count of constraints found.

---

### Phase 3: PM -- Decision Frame

With the constraint envelope established, **PM** fills all four fields. All four are required; omitting any field fails the proposal. This section appears verbatim in the output before any options.

```
THE QUESTION:         [The decision to be made -- one interrogative sentence]
WHY NOW:              [The event or cost pressure that makes deferral harmful --
                       one sentence, no vague temporal language]
TEMPORAL ANCHOR:      [A specific, named date, sprint number, event name, or deadline.
                       Examples: "Q2 planning cutoff 2026-04-01", "R3 feature freeze
                       sprint", "all-hands 2026-05-15". Do not write "soon,"
                       "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [The concrete outcome that accrues if no decision is made by the
                       TEMPORAL ANCHOR. Must name what teams will lose, incur, or be
                       blocked by -- not a feature they will miss, not an abstract risk.]
```

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

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

### Phase 5: Alternatives (Minimum 3)

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

### Phase 6: Comparison Matrix

PM and Architect produce a joint comparison table. Columns = all options (0 through N). Rows = 4-6 dimensions chosen to represent the decision's core trade-offs. No empty cells. Dimensions must be consistent across all options. Required dimensions: effort, team control, adoption friction, time to value. Add domain-specific dimensions as warranted.

---

### Phase 7: Recommendation

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

### Phase 8: Assumption Register

At least 2 entries. Validation plans must specify a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- VALIDATION PLAN: [Specific action to verify this before commitment]

---

### Phase 9: Risk Register

At least 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Amend Phase

Self-critique this proposal before closing. Name at least one item per category:

- MISSING OPTION: An approach not yet explored that a skeptical reviewer would raise.
- UNWEIGHTED CRITERION: A dimension in the comparison matrix that likely deserves higher weight but was treated as equal to others.
- FOLLOW-UP: A question or prerequisite that must be resolved before this proposal can be finalized and acted on.

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

## V-04: Amend Headers + Temporal Anchor in Conversational Register (Combo)

**Axis**: Amend phase structure + decision frame granularity, conversational register (combined)
**Hypothesis**: Adding (1) named amend sub-headers with OWNER field and (2) split TEMPORAL ANCHOR / INACTION CONSEQUENCE fields to V-04 R1's conversational base produces C-10 and C-12 coverage at low overhead. C-11 is deliberately not targeted -- the existing V-04 R1 language ("Architect confirms or adds a caveat") is preserved without an explicit incompleteness clause. If C-11 fails here, the clause is load-bearing; if it passes, the dual-role structure is sufficient without explicit enforcement language.

---

You're writing a proposal for Signal. Keep it direct -- every section earns its place.

**Invocation**: `/draft-proposal "{topic}"`

---

Start by looking for scout work already done:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`

Note what you found at the top of the output. If nothing exists, say so and add a quick inline assessment.

---

**Frame the decision.** PM writes this -- it goes first. Fill all four fields before writing options:

```
QUESTION:             [What decision is being made -- one sentence]
WHY NOW:              [Why it needs to be made now -- no vague temporal language allowed]
TEMPORAL ANCHOR:      [Specific date, sprint number, or named event that creates urgency.
                       Do not write "soon," "eventually," or "in the near future."]
INACTION CONSEQUENCE: [What teams will lose, be blocked by, or incur if no decision is
                       made by the TEMPORAL ANCHOR -- not a feature they will miss]
```

---

**List your options.** Minimum 4. One must be "do nothing."

For each option, fill every field -- skipping risk or effort turns this into a list of ideas, not a proposal:

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

**Amend.** Before closing, use these three headers. Write at least one entry under each. Each entry must name who owns it.

**MISSING OPTION**
An approach you didn't explore.
Format: `[What it is] -- OWNER: [who investigates] -- NEXT ACTION: [what question to answer first]`

**UNWEIGHTED CRITERION**
A comparison dimension that deserved more weight than it got.
Format: `[Which dimension and why] -- OWNER: [who re-weights it] -- NEXT ACTION: [how re-weighting changes the recommendation]`

**FOLLOW-UP**
A question that must be answered before this proposal is acted on.
Format: `[The question] -- OWNER: [who answers it] -- DEADLINE: [named date or event]`

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

## V-05: Full Integration -- All Three C-10/C-11/C-12 Enforcement Mechanisms

**Axis**: Amend header structure + dual-signature form + split temporal anchor + V-05 R1 base (full combination)
**Hypothesis**: Integrating all three R2 enforcement mechanisms -- typed amend headers with OWNER field (C-10), dual-signature form with INCOMPLETE STATUS (C-11), and split TEMPORAL ANCHOR / INACTION CONSEQUENCE fields (C-12) -- into V-05 R1's phase structure produces the first prompt that enforces all five aspirational criteria structurally rather than instructionally. V-05 R1 enforced C-10/C-11/C-12 via prohibition and instruction; V-05 R2 enforces them via form structures that cannot be satisfied without producing the required content. The key assertion: instructional enforcement fails under adversarial inputs; structural enforcement does not.

---

You are authoring a Signal proposal artifact. This is a structured decision document. All phases are required. Role labels are mandatory in the output. Omitting any field on any option fails the artifact.

**Invocation**: `/draft-proposal "{topic}"`

---

### Phase 1: Scout Artifact Inventory

Scan for:
- `simulations/scout/feasibility/{topic}-feasibility-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`
- `simulations/scout/stakeholders/{topic}-stakeholders-*.md`

Record for each found artifact: file name, date, and the single most relevant finding for this decision. If no artifacts exist, note the gap and proceed with inline assessment.

---

### Phase 2: Architect -- Constraint Inventory

**Architect** runs first. Enumerate all constraints that bound the solution space before any options are named:

- Stack constraints: language, runtime, platform, OS compatibility
- Integration constraints: existing APIs, protocols, dependency limits
- Timeline constraints: what is achievable in what window, at what team size
- Known failure modes: technical risks that could invalidate an option regardless of its other merits

Label each C-NN. These are fixed. No option may propose violating a constraint without an explicit justification. Record the count of constraints found.

---

### Phase 3: PM -- Decision Frame

With the constraint envelope established, **PM** fills all four fields. All four are required; omitting any field fails the proposal. This section appears verbatim in the output before any options.

```
THE QUESTION:         [The decision to be made -- one interrogative sentence]
WHY NOW:              [The event or cost pressure that makes deferral harmful --
                       one sentence, no vague temporal language]
TEMPORAL ANCHOR:      [A specific, named date, sprint number, event name, or deadline.
                       Examples: "Q2 planning cutoff 2026-04-01", "R3 feature freeze
                       sprint", "all-hands 2026-05-15". Do not write "soon,"
                       "eventually," "shortly," or "in the near future."]
INACTION CONSEQUENCE: [Concrete outcome that accrues if no decision is made by the
                       TEMPORAL ANCHOR. Must name what teams will lose, incur, or be
                       blocked by -- not a feature they will miss, not an abstract risk.]
```

---

### Phase 4: Option 0 -- Do Nothing / Status Quo (Mandatory, Always First)

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

### Phase 5: Alternatives (Minimum 3)

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

### Phase 6: Comparison Matrix

PM and Architect produce a joint comparison table. Columns = all options (0 through N). Rows = 4-6 dimensions chosen to represent the decision's core trade-offs. No empty cells. Dimensions must be consistent across all options. Required dimensions: effort, team control, adoption friction, time to value. Add domain-specific dimensions as warranted.

---

### Phase 7: Recommendation -- Dual Signature Form

Complete both signature blocks in full. INCOMPLETE STATUS must read COMPLETE only when both blocks contain distinct, non-interchangeable content.

```
PM SIGN-OFF
  CHOSEN OPTION:   [letter + name]
  RATIONALE:       [Why this option serves adoption, timeline, and stakeholder needs --
                    2-3 sentences. Reference scout artifact by name if available;
                    state "none found" if not.]
  CONDITIONS:      [2-3 specific conditions that must hold for this recommendation
                    to remain valid]
  CONFIDENCE:      [HIGH / MEDIUM / LOW]

ARCHITECT SIGN-OFF
  TECHNICAL CONFIDENCE: [HIGH / MEDIUM / LOW]
  PRECONDITIONS:        [Implementation prerequisites that must be resolved before
                         the chosen option is viable -- at least one named item,
                         not "none"]
  QUALIFICATIONS:       [Technical caveats on the PM recommendation -- at least one
                         named item, or "none" only if the Architect fully concurs
                         with no technical reservations]
  CONSTRAINT VERIFIED:  [Confirm chosen option complies with all Phase 2 C-NN
                         constraints, or identify which constraint requires exception
                         and state the justification]

INCOMPLETE STATUS: [COMPLETE / INCOMPLETE]
```

A recommendation signed by only one role is incomplete. Interchangeable prose under two role headers is a fail.

---

### Phase 8: Assumption Register

At least 2 entries. Validation plans must specify a concrete action, not a monitoring posture.

- A-NN: [Assumption] -- VALIDATION PLAN: [Specific action to verify this before commitment]

---

### Phase 9: Risk Register

At least 2 entries.

- R-NN: [Risk] -- PROBABILITY: [L/M/H] -- IMPACT: [L/M/H] -- MITIGATION: [Specific action or contingency, not "monitor closely"]

---

### Phase 10: Amend Phase

Self-critique this proposal. Each section below is a required output section. Write at least one entry per section. Each entry must include a description and an OWNER.

#### MISSING OPTION

An approach not yet explored that a skeptical reviewer would raise.

`[Description of the unexplored option] -- OWNER: [role or team] -- NEXT ACTION: [what investigation would determine whether it belongs in a revised proposal]`

#### UNWEIGHTED CRITERION

A dimension in the comparison matrix that likely deserves higher weight than it received.

`[Which dimension and why it is underweighted] -- OWNER: [role or team] -- NEXT ACTION: [how to weight it explicitly and what effect that would have on the recommendation]`

#### FOLLOW-UP

A question or prerequisite that must be resolved before this proposal can be finalized and acted on.

`[The open question or prerequisite] -- OWNER: [role or team] -- DEADLINE: [named date or event by which this must be resolved]`

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

**V-05** -- combines all three structural enforcement mechanisms. Only variation that makes all five aspirational criteria impossible to fail through instructional shortcuts.

**V-01** is the safest single-axis upgrade from R1: minimal change, targets the one C-10 gap (missing OWNER field) that V-05 R1 had.

**Risk assessment**:
- V-04 (conversational): C-11 is the open question. Dual-role language is present but no incompleteness clause. C-11 may pass (role contributions are structurally distinct) or fail (single-voice interchangeability not blocked). This is the discriminating test for R2.
- V-02 and V-03 (single-axis): Both likely golden since they inherit V-05 R1's full phase structure with a single high-value upgrade. Neither weakens existing criteria.
