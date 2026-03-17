# program-plan — R9 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. All five variations inherit R8 V-05 ceiling (225/235 under v9 rubric).
New axes: Gate Entry Precondition (V-01), Semantic Gate Chain (V-02), Gate Assertion
Falsification (V-03), V-01+V-02 combined (V-04), V-01+V-02+V-03+Program-Level Evidence Arc
Assertion combined (V-05).

---

## V-01 — Gate Entry Precondition

**Axis**: Each non-echo gate must include a `requires:` clause stating the evidence pre-condition
that must be established before the gate threshold is meaningfully evaluable. This complements
C-35's `asserting:` (post-condition) with an explicit pre-condition, producing bidirectional gate
semantics: entry condition + exit condition.

**Hypothesis**: C-35 added semantic post-conditions to gates: `asserting:` states what becomes true
when a gate passes. But gates also carry implicit pre-conditions — the evidence state that must
already be established for the artifact count threshold to be meaningful. A gate requiring ">=2
scout signals" is only valid if the scouting question was properly scoped; without an explicit
pre-condition, those 2 signals might ground nothing. V-01 requires a `requires:` clause per gate
that states what must be true about the topic evidence state BEFORE the threshold count can be
meaningfully evaluated. Bidirectional gate semantics: `requires:` = entry condition (what must
hold before counting); `asserting:` = exit condition (what becomes true when counting passes).
The discriminating signal: V-01 outputs have `requires:` clauses in every non-echo gate string;
V-02/V-03 do not.

**R9 new elements vs R8 V-05 baseline**:
- Step 10a (new): Gate Entry Preconditions — per-gate table requiring explicit pre-condition
  evidence state statement; distinct from artifact count threshold
- Gate format updated: `requires: [pre-condition evidence state]` inserted between threshold
  and `asserting:` clause
- Verification Checklist: precondition completeness and non-triviality checks added
- Arc Strategy Q5: precondition coherence finding added
- Total steps: 17 (one more than R8 V-05's 16)

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into
staged phases with explicit handoff gates and topic tracking. The program is a plan, not an
executor — every skill can run standalone without the program. Your job is to produce a program
that a team could follow as a sequenced evidence-building arc.

**This variation defeats five orthogonal under-specification failures: (1) artifact lineage that
traces only the immediate gate consumer, hiding multi-stage dependencies — defeated by the
Artifact Consumer Map; (2) stages that are correctly positioned but whose arc contribution is
never stated — defeated by the Stage Arc-Uniqueness Register; (3) gate thresholds set by
convention rather than topic-specific reasoning — defeated by Gate Threshold Calibration; (4)
gate conditions that express artifact counts but not evidence meaning — defeated by the Semantic
Gate Claims (`asserting:` clause); and (5) gate semantic assertions that state post-conditions
but not pre-conditions, leaving the evaluability of the threshold implicit — defeated by requiring
a `requires:` clause that states the evidence pre-condition that must be established before the
threshold count is meaningful. The `requires:` and `asserting:` clauses together produce
bidirectional gate semantics: entry condition + exit condition.**

---

#### Valid Signal Plugin Skill Catalog (enumerate inline — no external references)

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate
skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the
justification column must answer: **why this actor cannot run earlier than its position — and what
cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream |
|-------|-----------------|------------------------------------------------------------------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for. All artifact names and stage groupings should be
coherent with this topic.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. Record your selected skills as
a flat list grouped by namespace. You do not need to include every skill — the program is
topic-specific.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Each stage should represent
a coherent phase of work. Name each stage with a human-readable label (e.g., `discovery`,
`validation`, `depth`, `synthesis`). Do not use skill names as stage names.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce a displacement justification row. Stage 1 is always N/A.

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [specific artifact dependency on stage 1 that does not exist one position earlier] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops crossing arc-layer boundary] |
| [stage 3]  | 3        | [specific artifact dependency on stage 2] | [cascade chain, minimum 2 hops, crossing arc-layer boundary] |
| ... | ... | ... | ... |

Each "What breaks" entry must include a -> cascade of at least 2 ordered consequences crossing at
least one arc-layer boundary.

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce a cohesion justification row:

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved to a different stage |
|------------|-------------------|-------------------|--------------------------------------------------------|
| [stage 1]  | [skills] | [The specific evidence objective that ALL constituent skills jointly serve] | Moving [skill A]: [specific consequence for the stage's phase goal]; Moving [skill B]: [consequence] |
| [stage 2]  | [skills] | [Shared phase goal] | Moving [skill]: [consequence] |
| ... | ... | ... | ... |

---

#### Step 6 — Stage Arc-Uniqueness Register (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce an arc-uniqueness justification:

| Stage Name | Unique Arc Contribution | Arc Evidence Gap if Stage Removed (2+ hop consequence) |
|------------|------------------------|-------------------------------------------------------|
| [stage 1]  | [The specific evidence claim that becomes available when this stage completes — name the evidence assertion, not the skills list] | [Removed entirely: gap A -> downstream consequence B -> arc-layer consequence C, minimum 2 hops crossing arc-layer boundaries] |
| [stage 2]  | [Unique arc contribution — evidence assertion] | [2+ hop cascade of complete removal] |
| ... | ... | ... |

"Unique Arc Contribution" must name an evidence assertion (what becomes provably true about the
topic evidence state), not a skill list. "Arc Evidence Gap" must use -> notation with 2+ ordered
consequences crossing arc-layer boundaries.

---

#### Step 7 — Artifact Lineage Chain (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo gate, identify the specific producing skill:

| Gate | Producing Skill (in stage N) | Artifact Type Produced | Gate Threshold (draft) |
|------|------------------------------|------------------------|------------------------|
| [stage 1] -> [stage 2] | [namespace:skill] | [artifact_type] | >=? [artifact_type] |
| [stage 2] -> [stage 3] | [namespace:skill] | [artifact_type] | >=? [artifact_type] |
| ... | ... | ... | ... |

---

#### Step 8 — Artifact Consumer Map (REQUIRED BEFORE YAML ASSEMBLY)

For every artifact type identified in Step 7, trace ALL downstream stages and skills that consume
that artifact throughout the full program — not only the immediate next stage.

| Artifact Type | Producing Skill | Producing Stage | All Downstream Consumers |
|---------------|----------------|----------------|--------------------------|
| [artifact_type_1] | [namespace:skill] | [stage N] | Stage N+1: [skill A — purpose: grounding design intent]; Stage N+3: [skill B — purpose: scoping hypothesis] |
| [artifact_type_2] | [namespace:skill] | [stage N] | Stage N+1: [skill C — purpose: review target] (single-hop only — state this explicitly) |
| ... | ... | ... | ... |

Requirements:
- Every artifact type from Step 7 must have a Consumer Map entry.
- If an artifact is consumed only by the immediate next stage, state that explicitly.
- At least one artifact MUST be traced to a non-adjacent consumer stage.
- Flag long-reach dependencies explicitly with "long-reach:" note.

---

#### Step 9 — Gate Threshold Calibration (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Artifact Type | Minimum N for Valid Signal | Chosen N | Calibration Rationale |
|-----------------------------|--------------|---------------------------|----------|-----------------------|
| [stage 1] -> [stage 2] | [artifact_type] | >=1 ([topic-specific floor reason]) | >=N | [Topic-specific rationale: what characteristic of this topic makes the chosen N the right threshold] |
| [stage 2] -> [stage 3] | [artifact_type] | >=1 ([floor reason]) | >=N | [Topic-specific rationale] |
| ... | ... | ... | ... | ... |

Generic calibrations ("more is better", "standard practice") do not pass.

---

#### Step 10 — Semantic Gate Claims (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the semantic evidence claim asserted when the threshold is met.

| Gate (Stage N -> Stage N+1) | Semantic Evidence Claim |
|-----------------------------|-------------------------|
| [stage 1] -> [stage 2] | When this gate passes, we assert: [specific statement about what is now known or validated about the topic evidence state — phrased as an evidence claim, not an artifact count] |
| [stage 2] -> [stage 3] | When this gate passes, we assert: [evidence claim] |
| ... | ... |

Instructions:
- Claims that restate the artifact count ("2 scout signals are present") fail.
- Claims that name the evidence state transformation ("market boundaries are validated as
  groundable design constraints") pass.
- The claim must be topic-specific — not a generic statement about artifact types.
- This claim is embedded as the `asserting:` element in the gate format string.

---

#### Step 10a — Gate Entry Preconditions (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the evidence pre-condition that must be established before the gate
threshold count is meaningfully evaluable. This is NOT the artifact count itself — it is the
evidence state that makes counting the artifacts valid.

| Gate (Stage N -> Stage N+1) | Evidence Pre-Condition (requires:) |
|-----------------------------|-------------------------------------|
| [stage 1] -> [stage 2] | Before this gate can be meaningfully evaluated, the following must be true: [specific evidence state — what must be established about the topic for the threshold artifacts to be meaningful inputs. E.g.: "the feature scope is bounded and the evaluation question is specific enough that scout signals can be compared to a defined target space"] |
| [stage 2] -> [stage 3] | [pre-condition evidence state] |
| ... | ... |

**Instructions:**
- The pre-condition states what must be true about the evidence state BEFORE counting begins —
  not what must exist as artifacts (that is the threshold), but what must be established for those
  artifacts to be valid inputs.
- Pre-conditions that restate the prior stage's gate threshold (e.g., "stage 1 must be complete")
  fail — the pre-condition must state an EVIDENCE quality, not a process step.
- Example passing pre-condition: "evaluation question is scoped to a specific user population,
  so that interview signals can be compared against a defined baseline."
- Example failing pre-condition: "stage 2 must have run" (this is a sequencing condition, not
  an evidence pre-condition).
- This pre-condition is embedded as the `requires:` element in the gate format string.

---

#### Step 11 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2 loses if gate 1 absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 3 loses if gate 2 absent] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 12 — Gate Format

Use this exact format for every non-echo stage gate string. The Artifact Lineage Chain prefix
(from Step 7), the `requires:` clause (from Step 10a), and the `asserting:` clause (from Step 10)
are ALL REQUIRED. The threshold N is from Step 9:

```
"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- requires: [evidence pre-condition that must be established for this threshold to be meaningful] -- asserting: [semantic evidence claim] -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

Where:
- `[Skill X in stage N produces artifact_type]` is drawn verbatim from Step 7
- `>=N` is the calibrated threshold from Step 9
- `requires: [pre-condition]` is drawn verbatim from Step 10a
- `asserting: [semantic evidence claim]` is drawn verbatim from Step 10
- The cascade-if-removed clause MUST use `->` notation with minimum 2 hops crossing arc-layer
  boundaries
- The adjacent-gate consequence is drawn from Step 11

---

#### Step 13 — Echo Stage Displacement Reasoning

Before writing the echo stage:

- **(a) Arc-completion signal echo emits**: What specific arc-completion assertion does echo
  produce — what becomes true when echo fires that was not true at any earlier stage?
- **(b) What breaks if echo fires at stage 2**: Trace at least 2 hops crossing arc-layer
  boundaries — name specifically what is ungrounded, premature, or false.

Echo is architecturally last — not conventionally last.

---

#### Step 14 — Arc Strategy

1. Name each stage's role in the evidence arc (breadth -> depth -> validation -> synthesis ->
   closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)**
   is removed? Name the scout handoff gate, the producing skill (from Step 7), and trace the
   cascade across all downstream arc layers.
3. Consumer Map finding: name the artifact with non-adjacent consumers and explain the constraint
   implication for the producing stage.
4. Arc-Uniqueness finding: name one stage whose uniqueness entry confirmed or changed the program
   design.
5. Precondition finding: name one gate where the `requires:` clause states a pre-condition that
   would have been invisible without it — what assumption was implicit in the R8 gate format that
   V-01 makes explicit?

---

#### Step 15 — YAML Assembly

Assemble the program.yaml using stages validated by Steps 4, 5, and 6; gate strings from Step 12
(drawn from Steps 7, 9, 10, 10a, and 11); echo displacement from Step 13; arc strategy from
Step 14.

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
        - [namespace:skill]
      gate: "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- requires: [pre-condition evidence state] -- asserting: [semantic evidence claim] -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

Constraints: all skills from valid catalog; every non-echo stage has a non-trivial gate; echo
last with `skills: []` and `auto: true`; dependency ordering by namespace layer
(scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals).

---

#### Step 16 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Topic-specific reason — generic reasons ("not needed", "optional") do not pass. Reference a specific topic characteristic.] |

Every catalog skill not in the YAML must appear here. A skill cannot be silently absent.

---

### Verification Checklist

Before finalizing output:

- [ ] Stage Displacement Register: every non-echo stage 2+ has 2+ hop "What breaks" cascade
- [ ] Stage Cohesion Audit Table: every stage has shared phase goal + per-skill displacement
- [ ] Stage Arc-Uniqueness Register: every stage has evidence contribution statement + 2+ hop
  arc gap consequence; no skill-list entries
- [ ] Artifact Lineage Chain: every gate has producing skill identified
- [ ] Artifact Consumer Map: every artifact has consumer entry; at least one non-adjacent
  consumer traced; long-reach dependencies flagged
- [ ] Threshold Calibration: every gate has minimum N + chosen N + topic-specific rationale
- [ ] Semantic Gate Claims: every gate has evidence-state assertion distinct from artifact count
- [ ] **Gate Entry Preconditions: every non-echo gate has a `requires:` clause stating a
  non-trivial evidence pre-condition; no process-step entries ("prior stage must complete")**
- [ ] Gate Cascade Audit Table: every gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses lineage prefix + `requires:` clause + `asserting:` clause + exact
  format from Step 12 with `->` notation and depth floor
- [ ] Echo displacement: arc-completion signal named + 2+ hop consequence named
- [ ] Arc strategy: arc named + first-gate cascade traced + all five structural findings named
- [ ] Skill Omission Register: every excluded skill has topic-specific reason
- [ ] No skill silently absent (either in YAML or Omission Register)
- [ ] All skills valid catalog; YAML syntactically valid

---

## V-02 — Semantic Gate Chain

**Axis**: Each non-echo gate's `asserting:` clause must include a `grounded-in:` citation
referencing the prior gate's semantic assertion as the evidence foundation this gate builds upon.
This transforms isolated gate assertions (C-35) into a coherent semantic chain where each
evidence state declaration is explicitly grounded in the prior.

**Hypothesis**: C-35 gives each gate an independent `asserting:` clause. But a well-designed
program has evidence states that build on each other — the validation stage's assertion should
reference the discovery stage's assertion as its foundation. V-02 requires a `grounded-in:`
citation within each `asserting:` clause that names the prior gate's evidence assertion as the
foundation this gate's assertion is built upon. The first gate (no prior) cites the topic
statement and skill selection assumptions instead. This transforms isolated semantic claims into
a semantic chain: structural cascades (C-27) made parallel at the evidence-meaning level.
Discriminating signal: V-02 outputs have `grounded-in:` citations inside `asserting:` clauses
in every non-echo gate string; V-01/V-03 do not.

**R9 new elements vs R8 V-05 baseline**:
- Step 10 MODIFIED: Semantic Gate Claims table now requires a `grounded-in:` column
- Gate format updated: `asserting:` clause now contains `(grounded-in: [prior gate assertion])`
- First gate special case: `grounded-in: topic-scope assumptions — no prior gate`
- Verification Checklist: chain completeness and non-restatement checks added
- Arc Strategy Q5: semantic chain coherence finding added
- Total steps: 16 (same as R8 V-05)

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into
staged phases with explicit handoff gates and topic tracking. The program is a plan, not an
executor — every skill can run standalone without the program. Your job is to produce a program
that a team could follow as a sequenced evidence-building arc.

**This variation defeats five orthogonal under-specification failures: (1) artifact lineage that
traces only the immediate gate consumer — defeated by the Artifact Consumer Map; (2) stages with
unstated arc contribution — defeated by the Stage Arc-Uniqueness Register; (3) gate thresholds
set by convention — defeated by Gate Threshold Calibration; (4) gate conditions that express
artifact counts but not evidence meaning — defeated by Semantic Gate Claims (`asserting:`
clause); and (5) gate assertions that are semantically isolated — each gate's `asserting:` clause
standing independent of the prior gate's evidence state, hiding whether the evidence arc is
coherent or merely sequential — defeated by requiring a `grounded-in:` citation inside each
`asserting:` clause. The `grounded-in:` citation names the prior gate's evidence assertion as the
foundation this gate's assertion is built upon, creating a semantic chain: structural cascades
(C-27) are now paralleled by a chain of evidence-meaning declarations.**

---

#### Valid Signal Plugin Skill Catalog (enumerate inline — no external references)

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate
skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the
justification column must answer: **why this actor cannot run earlier than its position — and what
cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream |
|-------|-----------------|------------------------------------------------------------------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. Record your selected skills
grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Name each stage with a
human-readable label. Do not use skill names as stage names.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [specific artifact dependency on stage 1] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops] |
| [stage 3]  | 3        | [specific artifact dependency on stage 2] | [cascade chain, minimum 2 hops, crossing arc-layer boundary] |
| ... | ... | ... | ... |

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved to a different stage |
|------------|-------------------|-------------------|--------------------------------------------------------|
| [stage 1]  | [skills] | [Evidence objective all skills jointly serve] | Moving [skill A]: [consequence]; Moving [skill B]: [consequence] |
| [stage 2]  | [skills] | [Shared phase goal] | Moving [skill]: [consequence] |
| ... | ... | ... | ... |

---

#### Step 6 — Stage Arc-Uniqueness Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Unique Arc Contribution | Arc Evidence Gap if Stage Removed (2+ hop consequence) |
|------------|------------------------|-------------------------------------------------------|
| [stage 1]  | [Specific evidence claim uniquely enabled by this stage — name the evidence assertion, not the skills list] | [Removed entirely: gap A -> downstream consequence B -> arc-layer consequence C, minimum 2 hops] |
| [stage 2]  | [Unique arc contribution — evidence assertion] | [2+ hop cascade of complete removal] |
| ... | ... | ... |

---

#### Step 7 — Artifact Lineage Chain (REQUIRED BEFORE YAML ASSEMBLY)

| Gate | Producing Skill (in stage N) | Artifact Type Produced | Gate Threshold (draft) |
|------|------------------------------|------------------------|------------------------|
| [stage 1] -> [stage 2] | [namespace:skill] | [artifact_type] | >=? [artifact_type] |
| [stage 2] -> [stage 3] | [namespace:skill] | [artifact_type] | >=? [artifact_type] |
| ... | ... | ... | ... |

---

#### Step 8 — Artifact Consumer Map (REQUIRED BEFORE YAML ASSEMBLY)

| Artifact Type | Producing Skill | Producing Stage | All Downstream Consumers |
|---------------|----------------|----------------|--------------------------|
| [artifact_type_1] | [namespace:skill] | [stage N] | Stage N+1: [skill A — purpose]; Stage N+3: [skill B — purpose] |
| [artifact_type_2] | [namespace:skill] | [stage N] | Stage N+1: [skill C — purpose] (single-hop only — stated explicitly) |
| ... | ... | ... | ... |

At least one artifact MUST be traced to a non-adjacent consumer stage. Flag long-reach
dependencies explicitly.

---

#### Step 9 — Gate Threshold Calibration (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Artifact Type | Minimum N for Valid Signal | Chosen N | Calibration Rationale |
|-----------------------------|--------------|---------------------------|----------|-----------------------|
| [stage 1] -> [stage 2] | [artifact_type] | >=1 ([topic-specific floor reason]) | >=N | [Topic-specific rationale] |
| [stage 2] -> [stage 3] | [artifact_type] | >=1 ([floor reason]) | >=N | [Topic-specific rationale] |
| ... | ... | ... | ... | ... |

Generic calibrations do not pass.

---

#### Step 10 — Semantic Gate Claims with Chain (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the semantic evidence claim asserted when the threshold is met AND
the prior gate assertion this claim is grounded in. The `grounded-in:` citation creates a semantic
chain across gates.

| Gate (Stage N -> Stage N+1) | Semantic Evidence Claim (asserting:) | Evidence Foundation (grounded-in:) |
|-----------------------------|---------------------------------------|-------------------------------------|
| [stage 1] -> [stage 2] | [evidence state now true when threshold passes — not artifact count, but what is now known] | grounded-in: topic-scope assumptions — no prior gate. [State which topic-level assumptions make this first assertion valid] |
| [stage 2] -> [stage 3] | [evidence claim] | grounded-in: [quote or paraphrase the prior gate's asserting: clause and explain how this gate's assertion is built upon it — what the prior evidence state enables this gate to assert] |
| [stage 3] -> [stage 4] | [evidence claim] | grounded-in: [prior gate's assertion as foundation] |
| ... | ... | ... |

**Instructions:**
- `asserting:` claims that restate artifact counts fail.
- `grounded-in:` entries that simply say "prior stage complete" fail — they must name the
  specific prior evidence assertion and explain how it enables this gate's assertion.
- The first gate's `grounded-in:` cites topic-scope assumptions, not a prior gate.
- The chain tests semantic coherence: if you cannot explain how this gate's assertion is built on
  the prior, the program's evidence arc may not be coherent.
- Both fields are embedded in the gate format string.

---

#### Step 11 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2 loses if gate 1 absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C] | [what gate 3 loses] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 12 — Gate Format

Use this exact format for every non-echo stage gate string. The Artifact Lineage Chain prefix
(from Step 7), the `asserting:` clause with `grounded-in:` citation (from Step 10), and the
threshold N (from Step 9) are ALL REQUIRED:

```
"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- asserting: [semantic evidence claim] (grounded-in: [prior gate assertion or topic-scope assumptions for first gate]) -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

Where:
- `[Skill X in stage N produces artifact_type]` is drawn verbatim from Step 7
- `>=N` is the calibrated threshold from Step 9
- `asserting:` and `grounded-in:` are drawn verbatim from Step 10
- The cascade-if-removed clause MUST use `->` notation with 2+ hops crossing arc-layer boundaries
- The adjacent-gate consequence is drawn from Step 11

---

#### Step 13 — Echo Stage Displacement Reasoning

- **(a) Arc-completion signal echo emits**: What specific arc-completion assertion does echo
  produce — what becomes true when echo fires that was not true at any earlier stage?
- **(b) What breaks if echo fires at stage 2**: Trace at least 2 hops crossing arc-layer
  boundaries.

Echo is architecturally last — not conventionally last.

---

#### Step 14 — Arc Strategy

1. Name each stage's role in the evidence arc (breadth -> depth -> validation -> synthesis ->
   closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)**
   is removed? Name the scout handoff gate, the producing skill (from Step 7), and trace the
   cascade across all downstream arc layers.
3. Consumer Map finding: name the artifact with non-adjacent consumers and explain the constraint
   implication for the producing stage.
4. Arc-Uniqueness finding: name one stage whose uniqueness entry confirmed or changed the program
   design.
5. Semantic chain finding: read the full sequence of `asserting:` clauses as a narrative. Does
   the chain form a coherent evidence progression? Name the gate where the `grounded-in:`
   citation reveals the most important evidence dependency between consecutive assertions — what
   would be disconnected if the chain were broken there?

---

#### Step 15 — YAML Assembly

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
      gate: "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- asserting: [semantic evidence claim] (grounded-in: [prior gate assertion or topic-scope assumptions]) -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

---

#### Step 16 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Topic-specific reason — generic reasons do not pass.] |

---

### Verification Checklist

Before finalizing output:

- [ ] Stage Displacement Register: every non-echo stage 2+ has 2+ hop cascade
- [ ] Stage Cohesion Audit Table: every stage has shared phase goal + per-skill displacement
- [ ] Stage Arc-Uniqueness Register: every stage has evidence contribution + 2+ hop arc gap
- [ ] Artifact Lineage Chain: every gate has producing skill
- [ ] Artifact Consumer Map: every artifact has consumer entry; at least one non-adjacent consumer
- [ ] Threshold Calibration: every gate has minimum N + chosen N + topic-specific rationale
- [ ] **Semantic Gate Chain: every non-echo gate has both `asserting:` claim AND `grounded-in:`
  citation; first gate cites topic-scope assumptions; no gate has a `grounded-in:` entry that
  merely states "prior stage complete"**
- [ ] Gate Cascade Audit Table: every gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses lineage prefix + `asserting:` (with `grounded-in:`) + exact format
  from Step 12 with `->` notation and depth floor
- [ ] Echo displacement: arc-completion signal named + 2+ hop consequence named
- [ ] Arc strategy: arc named + first-gate cascade + Consumer Map + Arc-Uniqueness + chain
  coherence findings named
- [ ] Skill Omission Register: every excluded skill has topic-specific reason
- [ ] All skills valid catalog; YAML syntactically valid

---

## V-03 — Gate Assertion Falsification

**Axis**: Each non-echo gate's `asserting:` clause must include a `falsified-if:` companion
condition — the specific real-world event or evidence pattern that would invalidate the assertion
post-passage. This transforms C-35's one-directional claim (what is now true) into a falsifiable
assertion (what is now true AND what would make it false).

**Hypothesis**: C-35's `asserting:` clause states what is now true when a gate passes, but does
not state what would make it false. A semantic assertion without a falsification condition is a
declaration, not a testable claim. V-03 requires a `falsified-if:` sub-clause paired with every
`asserting:` entry — the specific condition that would invalidate the assertion post-passage.
This is not a metric threshold but an evidence invalidation condition: something that, if
discovered, would mean the assertion was wrong and the program would need to revisit prior stages.
Discriminating signal: V-03 outputs have `falsified-if:` clauses in every gate assertion block;
V-01/V-02 do not.

**R9 new elements vs R8 V-05 baseline**:
- Step 10 MODIFIED: Semantic Gate Claims table now requires a `falsified-if:` column
- Step 10a (new): Gate Assertion Falsification — separate step making falsification explicit
  before gate format assembly
- Gate format updated: `falsified-if: [invalidation condition]` appended after `asserting:`
- Verification Checklist: falsification completeness and non-triviality checks added
- Arc Strategy Q5: falsification finding added
- Total steps: 17

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into
staged phases with explicit handoff gates and topic tracking. The program is a plan, not an
executor — every skill can run standalone without the program. Your job is to produce a program
that a team could follow as a sequenced evidence-building arc.

**This variation defeats five orthogonal under-specification failures: (1) artifact lineage that
traces only the immediate gate consumer — defeated by the Artifact Consumer Map; (2) stages with
unstated arc contribution — defeated by the Stage Arc-Uniqueness Register; (3) gate thresholds
set by convention — defeated by Gate Threshold Calibration; (4) gate conditions that express
artifact counts but not evidence meaning — defeated by Semantic Gate Claims (`asserting:`
clause); and (5) semantic assertions that state post-conditions as declarations rather than
testable claims — defeated by requiring a `falsified-if:` condition that states what would
invalidate the assertion post-passage. An `asserting:` clause without a `falsified-if:` is a
declaration; with it, the assertion is testable. If the `falsified-if:` condition is discovered,
the program must revisit prior stages rather than continuing forward on false evidence.**

---

#### Valid Signal Plugin Skill Catalog (enumerate inline — no external references)

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate
skill names.

---

#### Actor Ordering Table

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream |
|-------|-----------------|------------------------------------------------------------------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. Record your selected skills
grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Name each stage with a
human-readable label. Do not use skill names as stage names.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [artifact dependency on stage 1] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops] |
| [stage 3]  | 3        | [artifact dependency on stage 2] | [cascade chain, minimum 2 hops] |
| ... | ... | ... | ... |

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved to a different stage |
|------------|-------------------|-------------------|--------------------------------------------------------|
| [stage 1]  | [skills] | [Evidence objective] | Moving [skill A]: [consequence]; Moving [skill B]: [consequence] |
| [stage 2]  | [skills] | [Phase goal] | Moving [skill]: [consequence] |
| ... | ... | ... | ... |

---

#### Step 6 — Stage Arc-Uniqueness Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Unique Arc Contribution | Arc Evidence Gap if Stage Removed (2+ hop consequence) |
|------------|------------------------|-------------------------------------------------------|
| [stage 1]  | [Evidence assertion uniquely enabled by this stage] | [gap A -> consequence B -> arc-layer consequence C, minimum 2 hops] |
| [stage 2]  | [Unique arc contribution] | [2+ hop cascade of complete removal] |
| ... | ... | ... |

---

#### Step 7 — Artifact Lineage Chain (REQUIRED BEFORE YAML ASSEMBLY)

| Gate | Producing Skill (in stage N) | Artifact Type Produced | Gate Threshold (draft) |
|------|------------------------------|------------------------|------------------------|
| [stage 1] -> [stage 2] | [namespace:skill] | [artifact_type] | >=? |
| [stage 2] -> [stage 3] | [namespace:skill] | [artifact_type] | >=? |
| ... | ... | ... | ... |

---

#### Step 8 — Artifact Consumer Map (REQUIRED BEFORE YAML ASSEMBLY)

| Artifact Type | Producing Skill | Producing Stage | All Downstream Consumers |
|---------------|----------------|----------------|--------------------------|
| [artifact_type_1] | [namespace:skill] | [stage N] | Stage N+1: [skill A — purpose]; Stage N+3: [skill B — purpose] |
| [artifact_type_2] | [namespace:skill] | [stage N] | Stage N+1: [skill C — purpose] (single-hop only) |
| ... | ... | ... | ... |

At least one artifact MUST be traced to a non-adjacent consumer stage. Flag long-reach
dependencies explicitly.

---

#### Step 9 — Gate Threshold Calibration (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Artifact Type | Minimum N for Valid Signal | Chosen N | Calibration Rationale |
|-----------------------------|--------------|---------------------------|----------|-----------------------|
| [stage 1] -> [stage 2] | [artifact_type] | >=1 ([floor reason]) | >=N | [Topic-specific rationale] |
| ... | ... | ... | ... | ... |

Generic calibrations do not pass.

---

#### Step 10 — Semantic Gate Claims (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the semantic evidence claim asserted when the threshold is met.

| Gate (Stage N -> Stage N+1) | Semantic Evidence Claim (asserting:) |
|-----------------------------|---------------------------------------|
| [stage 1] -> [stage 2] | When this gate passes, we assert: [evidence state now true — not artifact count, but what is now known] |
| [stage 2] -> [stage 3] | When this gate passes, we assert: [evidence claim] |
| ... | ... |

Claims that restate artifact counts fail. Topic-specific evidence-state claims pass.

---

#### Step 10a — Gate Assertion Falsification (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the specific condition that would invalidate the gate's `asserting:`
claim post-passage. This is not a metric threshold or a process condition — it is a real-world
evidence event that, if discovered, would mean the assertion was wrong and the program would need
to revisit prior stages.

| Gate (Stage N -> Stage N+1) | Falsification Condition (falsified-if:) |
|-----------------------------|----------------------------------------|
| [stage 1] -> [stage 2] | This assertion is invalidated if: [specific evidence discovery that would mean the asserting: claim was false. E.g.: "a previously unknown regulatory constraint is discovered post-gate that changes the competitive landscape entirely, making the scout signals collected invalid as design anchors"] |
| [stage 2] -> [stage 3] | [invalidation condition] |
| ... | ... |

**Instructions:**
- The falsification condition must be topic-specific — not "any new information" or "if scope
  changes" (too generic).
- The condition must name a specific class of evidence event, not a project management event.
- Conditions that restate the gate threshold ("if fewer than N artifacts exist") fail — those
  describe the gate not passing, not the assertion being wrong post-passage.
- A gate asserting "market boundaries are validated" might be falsified-if "primary user
  interviews reveal a completely different use-case framing than the scout signals assumed,
  invalidating the market boundary definition." This names the specific evidence event.
- This condition is embedded as `falsified-if:` in the gate format string.

---

#### Step 11 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|-------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N | [A -> B -> C, minimum 2 hops, arc-layer crossing] | [what gate 2 loses] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 12 — Gate Format

Use this exact format for every non-echo stage gate string. The lineage prefix (Step 7),
`asserting:` clause (Step 10), `falsified-if:` condition (Step 10a), and threshold N (Step 9)
are ALL REQUIRED:

```
"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- asserting: [semantic evidence claim] -- falsified-if: [specific condition that would invalidate this assertion post-passage] -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

Where:
- Lineage prefix verbatim from Step 7
- `>=N` calibrated threshold from Step 9
- `asserting:` verbatim from Step 10
- `falsified-if:` verbatim from Step 10a
- Cascade uses `->` notation with 2+ hops crossing arc-layer boundaries
- Adjacent-gate consequence from Step 11

---

#### Step 13 — Echo Stage Displacement Reasoning

- **(a) Arc-completion signal**: What becomes true when echo fires that was not true at any
  earlier stage?
- **(b) What breaks if echo fires at stage 2**: 2+ hops crossing arc-layer boundaries.

Echo is architecturally last — not conventionally last.

---

#### Step 14 — Arc Strategy

1. Name each stage's role in the evidence arc.
2. First-gate cascade: what is the multi-hop consequence if the scout handoff gate is removed?
3. Consumer Map finding: artifact with non-adjacent consumers and constraint implication.
4. Arc-Uniqueness finding: one stage whose uniqueness entry confirmed or changed the design.
5. Falsification finding: name one gate where the `falsified-if:` condition reveals a real-world
   risk that the `asserting:` clause alone would have hidden. What would a team do differently
   if they knew this invalidation condition in advance?

---

#### Step 15 — YAML Assembly

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
      gate: "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- asserting: [semantic evidence claim] -- falsified-if: [invalidation condition] -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

---

#### Step 16 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Topic-specific reason — generic reasons do not pass.] |

---

### Verification Checklist

- [ ] Stage Displacement Register: every non-echo stage 2+ has 2+ hop cascade
- [ ] Stage Cohesion Audit Table: every stage has shared phase goal + per-skill displacement
- [ ] Stage Arc-Uniqueness Register: every stage has evidence contribution + 2+ hop arc gap
- [ ] Artifact Lineage Chain: every gate has producing skill
- [ ] Artifact Consumer Map: every artifact has consumer entry; at least one non-adjacent consumer
- [ ] Threshold Calibration: every gate has minimum N + chosen N + topic-specific rationale
- [ ] Semantic Gate Claims: every gate has evidence-state assertion distinct from artifact count
- [ ] **Gate Assertion Falsification: every non-echo gate has a `falsified-if:` condition that
  names a specific evidence event (not a project event); no count-restatement entries**
- [ ] Gate Cascade Audit Table: every gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses lineage prefix + `asserting:` + `falsified-if:` + exact format from
  Step 12 with `->` notation and depth floor
- [ ] Echo displacement: arc-completion signal named + 2+ hop consequence named
- [ ] Arc strategy: five findings named including falsification finding
- [ ] Skill Omission Register: every excluded skill has topic-specific reason
- [ ] All skills valid catalog; YAML syntactically valid

---

## V-04 — Gate Entry Precondition + Semantic Gate Chain

**Axis**: V-01 + V-02 combined. Every gate has a `requires:` pre-condition clause (V-01) and its
`asserting:` clause carries a `grounded-in:` citation linking it to the prior gate's evidence
assertion (V-02).

**Hypothesis**: V-01's `requires:` and V-02's `grounded-in:` are orthogonal: `requires:` expresses
the evidence state that must be established for the threshold to be meaningful (entry condition);
`grounded-in:` expresses the evidence foundation the exit assertion is built upon (continuity
declaration). Together they make gate semantics complete in three directions: what must be true
before counting (requires:), what becomes true when counting passes (asserting:), and how this
gate's assertion connects to the prior gate's evidence state (grounded-in:). The discriminating
signal: V-04 has both `requires:` and `grounded-in:` in every gate; V-01 has only `requires:`;
V-02 has only `grounded-in:`; V-03 has neither.

**R9 new elements vs R8 V-05 baseline**:
- Step 10 MODIFIED: Semantic Gate Claims table requires `grounded-in:` column (from V-02)
- Step 10a (new): Gate Entry Preconditions table requires `requires:` column (from V-01)
- Gate format updated: `requires:` before `asserting: [claim] (grounded-in: [prior])`
- Verification Checklist: both precondition and chain checks added
- Arc Strategy Q5: both findings required
- Total steps: 17

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into
staged phases with explicit handoff gates and topic tracking. The program is a plan, not an
executor — every skill can run standalone without the program. Your job is to produce a program
that a team could follow as a sequenced evidence-building arc.

**This variation defeats six orthogonal under-specification failures: (1) artifact lineage
tracing only the immediate consumer — defeated by the Artifact Consumer Map; (2) stages with
unstated arc contribution — defeated by the Stage Arc-Uniqueness Register; (3) gate thresholds
set by convention — defeated by Gate Threshold Calibration; (4) gate conditions expressing
artifact counts but not evidence meaning — defeated by Semantic Gate Claims; (5) semantic
assertions without pre-conditions, leaving the evaluability of the threshold implicit — defeated
by `requires:` clauses (Gate Entry Preconditions); and (6) semantic assertions that are isolated
declarations, hiding whether the evidence arc is coherent — defeated by `grounded-in:` citations
(Semantic Gate Chain). The `requires:` + `asserting:` + `grounded-in:` triad produces fully
specified gate semantics: entry condition, exit condition, and continuity to the prior state.**

---

#### Valid Signal Plugin Skill Catalog (enumerate inline — no external references)

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate
skill names.

---

#### Actor Ordering Table

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream |
|-------|-----------------|------------------------------------------------------------------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. Record your selected skills
grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Name each stage with a
human-readable label. Do not use skill names as stage names.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [artifact dependency on stage 1] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops] |
| [stage 3]  | 3        | [artifact dependency on stage 2] | [cascade chain, minimum 2 hops, arc-layer crossing] |
| ... | ... | ... | ... |

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved to a different stage |
|------------|-------------------|-------------------|--------------------------------------------------------|
| [stage 1]  | [skills] | [Evidence objective] | Moving [skill A]: [consequence]; Moving [skill B]: [consequence] |
| [stage 2]  | [skills] | [Phase goal] | Moving [skill]: [consequence] |
| ... | ... | ... | ... |

---

#### Step 6 — Stage Arc-Uniqueness Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Unique Arc Contribution | Arc Evidence Gap if Stage Removed (2+ hop consequence) |
|------------|------------------------|-------------------------------------------------------|
| [stage 1]  | [Evidence assertion uniquely enabled by this stage] | [gap A -> consequence B -> arc-layer consequence C, minimum 2 hops] |
| [stage 2]  | [Unique arc contribution] | [2+ hop cascade] |
| ... | ... | ... |

---

#### Step 7 — Artifact Lineage Chain (REQUIRED BEFORE YAML ASSEMBLY)

| Gate | Producing Skill (in stage N) | Artifact Type Produced | Gate Threshold (draft) |
|------|------------------------------|------------------------|------------------------|
| [stage 1] -> [stage 2] | [namespace:skill] | [artifact_type] | >=? |
| [stage 2] -> [stage 3] | [namespace:skill] | [artifact_type] | >=? |
| ... | ... | ... | ... |

---

#### Step 8 — Artifact Consumer Map (REQUIRED BEFORE YAML ASSEMBLY)

| Artifact Type | Producing Skill | Producing Stage | All Downstream Consumers |
|---------------|----------------|----------------|--------------------------|
| [artifact_type_1] | [namespace:skill] | [stage N] | Stage N+1: [skill A — purpose]; Stage N+3: [skill B — purpose] |
| [artifact_type_2] | [namespace:skill] | [stage N] | Stage N+1: [skill C — purpose] (single-hop only) |
| ... | ... | ... | ... |

At least one artifact MUST be traced to a non-adjacent consumer stage. Flag long-reach
dependencies explicitly.

---

#### Step 9 — Gate Threshold Calibration (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Artifact Type | Minimum N for Valid Signal | Chosen N | Calibration Rationale |
|-----------------------------|--------------|---------------------------|----------|-----------------------|
| [stage 1] -> [stage 2] | [artifact_type] | >=1 ([floor reason]) | >=N | [Topic-specific rationale] |
| ... | ... | ... | ... | ... |

Generic calibrations do not pass.

---

#### Step 10 — Semantic Gate Chain (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state both the semantic evidence claim AND the evidence foundation it
is grounded in:

| Gate (Stage N -> Stage N+1) | Semantic Evidence Claim (asserting:) | Evidence Foundation (grounded-in:) |
|-----------------------------|---------------------------------------|-------------------------------------|
| [stage 1] -> [stage 2] | [evidence state now true — not artifact count] | grounded-in: topic-scope assumptions — no prior gate. [State which topic-level assumptions make this first assertion valid] |
| [stage 2] -> [stage 3] | [evidence claim] | grounded-in: [prior gate's asserting: clause and how it enables this gate's assertion] |
| ... | ... | ... |

`asserting:` claims that restate counts fail. `grounded-in:` entries that state only "prior stage
complete" fail — must name the specific prior evidence assertion and explain the enablement.

---

#### Step 10a — Gate Entry Preconditions (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the evidence pre-condition that must be established before the
threshold count is meaningfully evaluable:

| Gate (Stage N -> Stage N+1) | Evidence Pre-Condition (requires:) |
|-----------------------------|-------------------------------------|
| [stage 1] -> [stage 2] | Before this gate can be meaningfully evaluated: [evidence state — what must be established about the topic for the threshold artifacts to be meaningful inputs, not a process condition] |
| [stage 2] -> [stage 3] | [pre-condition evidence state] |
| ... | ... |

Pre-conditions that restate prior gate thresholds ("prior stage must complete") fail. Pre-conditions
must name an evidence quality, not a sequencing condition.

---

#### Step 11 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N | [A -> B -> C, minimum 2 hops] | [what gate 2 loses] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 12 — Gate Format

Use this exact format for every non-echo stage gate string. Lineage prefix (Step 7), `requires:`
(Step 10a), `asserting:` with `grounded-in:` (Step 10), and threshold N (Step 9) are ALL REQUIRED:

```
"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- requires: [evidence pre-condition] -- asserting: [semantic evidence claim] (grounded-in: [prior gate assertion or topic-scope assumptions for first gate]) -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
```

---

#### Step 13 — Echo Stage Displacement Reasoning

- **(a) Arc-completion signal**: What becomes true when echo fires that was not true at any
  earlier stage?
- **(b) What breaks if echo fires at stage 2**: 2+ hops crossing arc-layer boundaries.

Echo is architecturally last — not conventionally last.

---

#### Step 14 — Arc Strategy

1. Name each stage's role in the evidence arc.
2. First-gate cascade: multi-hop consequence if scout handoff gate removed.
3. Consumer Map finding: artifact with non-adjacent consumers and constraint implication.
4. Arc-Uniqueness finding: one stage whose uniqueness entry confirmed or changed the design.
5. Precondition finding: one gate where `requires:` reveals an implicit assumption that the R8
   gate format would have left unstated.
6. Semantic chain finding: one gate where `grounded-in:` reveals the most important evidence
   dependency between consecutive assertions.

---

#### Step 15 — YAML Assembly

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
      gate: "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- requires: [evidence pre-condition] -- asserting: [semantic evidence claim] (grounded-in: [prior gate assertion or topic-scope assumptions]) -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

---

#### Step 16 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Topic-specific reason — generic reasons do not pass.] |

---

### Verification Checklist

- [ ] Stage Displacement Register: every non-echo stage 2+ has 2+ hop cascade
- [ ] Stage Cohesion Audit Table: every stage has shared phase goal + per-skill displacement
- [ ] Stage Arc-Uniqueness Register: every stage has evidence contribution + 2+ hop arc gap
- [ ] Artifact Lineage Chain: every gate has producing skill
- [ ] Artifact Consumer Map: every artifact has consumer entry; at least one non-adjacent consumer
- [ ] Threshold Calibration: every gate has minimum N + chosen N + topic-specific rationale
- [ ] **Semantic Gate Chain: every non-echo gate has `asserting:` claim AND `grounded-in:`
  citation; first gate cites topic-scope assumptions; no "prior stage complete" entries**
- [ ] **Gate Entry Preconditions: every non-echo gate has `requires:` evidence pre-condition;
  no process-step entries**
- [ ] Gate Cascade Audit Table: every gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses lineage prefix + `requires:` + `asserting:` (with `grounded-in:`)
  + exact format from Step 12 with `->` notation and depth floor
- [ ] Echo displacement: arc-completion signal named + 2+ hop consequence named
- [ ] Arc strategy: six findings named
- [ ] Skill Omission Register: every excluded skill has topic-specific reason
- [ ] All skills valid catalog; YAML syntactically valid

---

## V-05 — Gate Entry Precondition + Semantic Gate Chain + Gate Assertion Falsification + Program-Level Evidence Arc Assertion

**Axis**: V-01 + V-02 + V-03 combined, plus a fourth axis: after YAML assembly, a top-level
`arc-asserts:` field is derived from all gate assertions, synthesizing the full sequence of
`asserting:` clauses into a single program-level evidence claim about what the program proves
when it runs to completion.

**Hypothesis**: V-01 adds pre-conditions; V-02 chains assertions; V-03 adds falsification
conditions. The fourth axis — Program-Level Evidence Arc Assertion — asks: if you read the full
sequence of `asserting:` clauses as an evidence narrative, what does the program as a whole
claim to prove about the topic? This synthesis transforms a sequence of gate-level claims into a
program-level proposition — the `arc-asserts:` field in the YAML. This is the program-level
analogue of C-35's gate-level `asserting:` clause: both ask "what is now true?" but at different
granularities (program vs. gate boundary). The `arc-asserts:` field is derivable from (and
constrained by) the sequence of `asserting:` clauses — if it contradicts or exceeds them, the
program's gate semantics are incoherent. Discriminating signal: V-05 outputs have an `arc-asserts:`
field in the top-level YAML; V-01/V-02/V-03/V-04 do not.

**R9 new elements vs R8 V-05 baseline**:
- Step 10 MODIFIED: Semantic Gate Chain (V-02 — `grounded-in:` citation)
- Step 10a (new): Gate Entry Preconditions (V-01 — `requires:` clause)
- Step 10b (new): Gate Assertion Falsification (V-03 — `falsified-if:` condition)
- Step 15a (new): Program-Level Evidence Arc Assertion — synthesize `asserting:` sequence into
  `arc-asserts:` field
- YAML template updated: `arc-asserts:` added to top-level program block
- Gate format: `requires:` + `asserting: (grounded-in:)` + `falsified-if:`
- Verification Checklist: all four new checks added
- Arc Strategy Q7: arc-asserts coherence finding added
- Total steps: 18

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into
staged phases with explicit handoff gates and topic tracking. The program is a plan, not an
executor — every skill can run standalone without the program. Your job is to produce a program
that a team could follow as a sequenced evidence-building arc.

**This variation defeats seven orthogonal under-specification failures: (1) artifact lineage
tracing only the immediate consumer — defeated by the Artifact Consumer Map; (2) stages with
unstated arc contribution — defeated by the Stage Arc-Uniqueness Register; (3) gate thresholds
set by convention — defeated by Gate Threshold Calibration; (4) gate conditions expressing
artifact counts but not evidence meaning — defeated by Semantic Gate Claims (`asserting:`
clause); (5) semantic assertions without pre-conditions — defeated by `requires:` clauses; (6)
semantic assertions that are isolated declarations hiding arc coherence — defeated by `grounded-in:`
citations; (7) gate assertion sequences that never synthesize into a program-level claim, leaving
the question "what does this program prove?" unanswered — defeated by the `arc-asserts:` field.
The `arc-asserts:` field is the program-level proposition derived from the full `asserting:`
sequence: what the program claims to prove when it runs to completion. If the `arc-asserts:`
claim cannot be derived from the `asserting:` sequence, the program's evidence arc is
incoherent.**

---

#### Valid Signal Plugin Skill Catalog (enumerate inline — no external references)

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate
skill names.

---

#### Actor Ordering Table

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream |
|-------|-----------------|------------------------------------------------------------------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. Record your selected skills
grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Name each stage with a
human-readable label. Do not use skill names as stage names.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [artifact dependency on stage 1] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops] |
| [stage 3]  | 3        | [artifact dependency on stage 2] | [cascade chain, minimum 2 hops, arc-layer crossing] |
| ... | ... | ... | ... |

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved to a different stage |
|------------|-------------------|-------------------|--------------------------------------------------------|
| [stage 1]  | [skills] | [Evidence objective] | Moving [skill A]: [consequence]; Moving [skill B]: [consequence] |
| [stage 2]  | [skills] | [Phase goal] | Moving [skill]: [consequence] |
| ... | ... | ... | ... |

---

#### Step 6 — Stage Arc-Uniqueness Register (REQUIRED BEFORE YAML ASSEMBLY)

| Stage Name | Unique Arc Contribution | Arc Evidence Gap if Stage Removed (2+ hop consequence) |
|------------|------------------------|-------------------------------------------------------|
| [stage 1]  | [Evidence assertion uniquely enabled by this stage] | [gap A -> consequence B -> arc-layer consequence C, minimum 2 hops] |
| [stage 2]  | [Unique arc contribution] | [2+ hop cascade] |
| ... | ... | ... |

---

#### Step 7 — Artifact Lineage Chain (REQUIRED BEFORE YAML ASSEMBLY)

| Gate | Producing Skill (in stage N) | Artifact Type Produced | Gate Threshold (draft) |
|------|------------------------------|------------------------|------------------------|
| [stage 1] -> [stage 2] | [namespace:skill] | [artifact_type] | >=? |
| [stage 2] -> [stage 3] | [namespace:skill] | [artifact_type] | >=? |
| ... | ... | ... | ... |

---

#### Step 8 — Artifact Consumer Map (REQUIRED BEFORE YAML ASSEMBLY)

| Artifact Type | Producing Skill | Producing Stage | All Downstream Consumers |
|---------------|----------------|----------------|--------------------------|
| [artifact_type_1] | [namespace:skill] | [stage N] | Stage N+1: [skill A — purpose]; Stage N+3: [skill B — purpose] |
| [artifact_type_2] | [namespace:skill] | [stage N] | Stage N+1: [skill C — purpose] (single-hop only) |
| ... | ... | ... | ... |

At least one artifact MUST be traced to a non-adjacent consumer stage. Flag long-reach
dependencies explicitly.

---

#### Step 9 — Gate Threshold Calibration (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Artifact Type | Minimum N for Valid Signal | Chosen N | Calibration Rationale |
|-----------------------------|--------------|---------------------------|----------|-----------------------|
| [stage 1] -> [stage 2] | [artifact_type] | >=1 ([floor reason]) | >=N | [Topic-specific rationale] |
| ... | ... | ... | ... | ... |

Generic calibrations do not pass.

---

#### Step 10 — Semantic Gate Chain (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state both the semantic evidence claim AND the prior gate assertion it
is grounded in:

| Gate (Stage N -> Stage N+1) | Semantic Evidence Claim (asserting:) | Evidence Foundation (grounded-in:) |
|-----------------------------|---------------------------------------|-------------------------------------|
| [stage 1] -> [stage 2] | [evidence state now true — not artifact count] | grounded-in: topic-scope assumptions — no prior gate. [Which assumptions make this first assertion valid] |
| [stage 2] -> [stage 3] | [evidence claim] | grounded-in: [prior gate's asserting: clause and how it enables this gate's claim] |
| ... | ... | ... |

`asserting:` claims that restate counts fail. `grounded-in:` entries that state only "prior stage
complete" fail.

---

#### Step 10a — Gate Entry Preconditions (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the evidence pre-condition that must be established before the
threshold count is meaningfully evaluable:

| Gate (Stage N -> Stage N+1) | Evidence Pre-Condition (requires:) |
|-----------------------------|-------------------------------------|
| [stage 1] -> [stage 2] | Before this gate can be meaningfully evaluated: [evidence state — what must be established for threshold artifacts to be meaningful inputs; not a process condition] |
| [stage 2] -> [stage 3] | [pre-condition evidence state] |
| ... | ... |

Pre-conditions that restate prior gate thresholds fail. Must name an evidence quality.

---

#### Step 10b — Gate Assertion Falsification (REQUIRED BEFORE GATE FORMAT ASSEMBLY)

For every non-echo gate, state the specific evidence event that would invalidate the gate's
`asserting:` claim post-passage:

| Gate (Stage N -> Stage N+1) | Falsification Condition (falsified-if:) |
|-----------------------------|----------------------------------------|
| [stage 1] -> [stage 2] | This assertion is invalidated if: [specific evidence discovery that would mean the asserting: claim was false — names a real-world evidence event, not a project management event] |
| [stage 2] -> [stage 3] | [invalidation condition] |
| ... | ... |

Conditions that restate the gate threshold ("if fewer than N artifacts") fail — they describe
the gate not passing, not the assertion being wrong post-passage. Must name a specific class of
evidence event.

---

#### Step 11 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N | [A -> B -> C, minimum 2 hops] | [what gate 2 loses] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 12 — Gate Format

Use this exact format for every non-echo stage gate string. Lineage prefix (Step 7), `requires:`
(Step 10a), `asserting:` with `grounded-in:` (Step 10), `falsified-if:` (Step 10b), and threshold
N (Step 9) are ALL REQUIRED:

```
"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- requires: [evidence pre-condition] -- asserting: [semantic evidence claim] (grounded-in: [prior gate assertion or topic-scope assumptions for first gate]) -- falsified-if: [specific evidence event that would invalidate this assertion post-passage] -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
```

---

#### Step 13 — Echo Stage Displacement Reasoning

- **(a) Arc-completion signal**: What becomes true when echo fires that was not true at any
  earlier stage?
- **(b) What breaks if echo fires at stage 2**: 2+ hops crossing arc-layer boundaries.

Echo is architecturally last — not conventionally last.

---

#### Step 14 — Arc Strategy

1. Name each stage's role in the evidence arc.
2. First-gate cascade: multi-hop consequence if scout handoff gate removed.
3. Consumer Map finding: artifact with non-adjacent consumers and constraint implication.
4. Arc-Uniqueness finding: one stage whose uniqueness entry confirmed or changed the design.
5. Precondition finding: one gate where `requires:` states an assumption that would have been
   invisible without it.
6. Semantic chain finding: one gate where `grounded-in:` reveals the most critical evidence
   dependency between consecutive assertions.
7. Falsification finding: one gate where `falsified-if:` reveals a real-world risk hidden by
   `asserting:` alone.

---

#### Step 15 — YAML Assembly

Assemble the program.yaml. Gate strings use the full format from Step 12.

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
      gate: "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- requires: [evidence pre-condition] -- asserting: [semantic evidence claim] (grounded-in: [prior gate assertion or topic-scope assumptions]) -- falsified-if: [invalidation condition] -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

---

#### Step 15a — Program-Level Evidence Arc Assertion (REQUIRED AFTER YAML ASSEMBLY)

Read the full sequence of `asserting:` clauses from all non-echo gates as an evidence narrative.
Derive a single `arc-asserts:` statement that synthesizes this sequence into the program-level
proposition: what does this program claim to prove about the topic when it runs to completion?

**Instructions:**
- The `arc-asserts:` statement must be derivable from the `asserting:` sequence — it synthesizes
  the cumulative evidence state after all gates pass, not a restatement of the topic name.
- If the `arc-asserts:` claim requires evidence not present in any `asserting:` clause, revise
  either the gates or the `arc-asserts:` claim for coherence.
- The statement is one to three sentences naming the evidence proposition the program establishes.
- Example: "This program establishes that the feature has a validated market position, a reviewed
  and depth-simulated design, and demonstrated adoption viability — sufficient evidence to commit
  to a production build."
- After writing the `arc-asserts:` statement, add it to the YAML as a top-level field under
  `program:`:

```yaml
topic: [topic-name]
program:
  arc-asserts: "[program-level evidence proposition derived from the asserting: sequence]"
  stages:
    # ... stages as assembled in Step 15 ...
```

**Coherence test**: Read the `arc-asserts:` statement and then re-read each gate's `asserting:`
clause. Every component of `arc-asserts:` must be traceable to at least one gate's assertion.
If a component is not traceable, either add a gate or revise `arc-asserts:`.

---

#### Step 16 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Topic-specific reason — generic reasons do not pass.] |

---

### Verification Checklist

- [ ] Stage Displacement Register: every non-echo stage 2+ has 2+ hop cascade
- [ ] Stage Cohesion Audit Table: every stage has shared phase goal + per-skill displacement
- [ ] Stage Arc-Uniqueness Register: every stage has evidence contribution + 2+ hop arc gap
- [ ] Artifact Lineage Chain: every gate has producing skill
- [ ] Artifact Consumer Map: every artifact has consumer entry; at least one non-adjacent consumer
- [ ] Threshold Calibration: every gate has minimum N + chosen N + topic-specific rationale
- [ ] **Semantic Gate Chain: every non-echo gate has `asserting:` claim AND `grounded-in:`
  citation; first gate cites topic-scope assumptions; no "prior stage complete" entries**
- [ ] **Gate Entry Preconditions: every non-echo gate has `requires:` evidence pre-condition;
  no process-step entries**
- [ ] **Gate Assertion Falsification: every non-echo gate has `falsified-if:` naming a specific
  evidence event; no count-restatement or project-event entries**
- [ ] Gate Cascade Audit Table: every gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses full format from Step 12: lineage prefix + `requires:` +
  `asserting:` (with `grounded-in:`) + `falsified-if:` + cascade + adjacent-gate-loses
- [ ] **Program-Level Evidence Arc Assertion: `arc-asserts:` field present in YAML; every
  component traceable to at least one gate's `asserting:` clause; no component requires
  evidence not established by any gate**
- [ ] Echo displacement: arc-completion signal named + 2+ hop consequence named
- [ ] Arc strategy: seven findings named
- [ ] Skill Omission Register: every excluded skill has topic-specific reason
- [ ] All skills valid catalog; YAML syntactically valid
