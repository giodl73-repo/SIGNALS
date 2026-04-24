# program-plan — R7 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-14. All five variations inherit the R6 V-05 ceiling (185/185 under v7 rubric).
New axes: Stage Displacement Register (V-01), Stage Cohesion Audit Table (V-02), Skill Omission
Register (V-03), V-01+V-02 combined (V-04), V-01+V-02+V-03+Artifact Lineage Chain (V-05).

---

## V-01 — Stage Displacement Register

**Axis**: For every non-echo stage, explicitly state (a) why it cannot run before its predecessor and (b) what breaks if it fires one position earlier, in a dedicated Stage Displacement Register produced before YAML assembly.

**Hypothesis**: Adding a Stage Displacement Register analogous to the actor ordering table will produce program.yaml stage sequences where each stage boundary is architecturally justified rather than topologically sorted, generating detectable stage-level impossibility reasoning that is absent in V-02 (which audits gate cascades but not stage displacement) and V-03 (which audits skill grouping rationale but not displacement).

**R7 new elements vs R6 V-05 baseline**:
- Stage Displacement Register: required pre-YAML step naming per-stage displacement impossibility + consequence of firing one position earlier
- Distinct from actor ordering table (per-actor) and Gate Cascade Audit table (per-gate): this is per-stage
- Distinct from C-05 dependency ordering check: that checks the output; this pre-computes the justification before writing stages

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. The program is a plan, not an executor — every skill can run standalone without the program. Your job is to produce a program that a team could follow as a sequenced evidence-building arc.

**This variation defeats flat stage sequences that pass dependency order but contain no explicit justification for why each stage boundary is where it is — defeating that failure by requiring a Stage Displacement Register that pre-computes, for every non-echo stage, why it cannot fire one position earlier and what breaks if it does. This is the stage-level analogue of the actor ordering table, applied to stage sequence itself before YAML assembly.**

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

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the justification column must answer: **why this actor cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------------|----------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for. All artifact names and stage groupings should be coherent with this topic.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. You do not need to include every skill — the program is topic-specific. Record your selected skills as a flat list grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Each stage should represent a coherent phase of work. Name each stage with a human-readable label (e.g., `discovery`, `validation`, `depth`, `synthesis`). Do not use skill names as stage names.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage you proposed in Step 3, produce the following register. The register is a mandatory pre-computation step — do not skip it or merge it with YAML assembly.

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [reason: depends on artifact type from stage 1] | [consequence: artifact missing -> downstream effect -> arc-layer consequence] |
| [stage 3]  | 3        | [reason: depends on artifact type from stage 2] | [consequence: artifact missing -> downstream effect -> arc-layer consequence] |
| ... | ... | ... | ... |

Each "What breaks" entry must include a -> cascade of at least 2 ordered consequences crossing at least one arc-layer boundary. A displacement entry that names a single consequence (e.g., "no validated spec") without tracing the downstream propagation fails this register.

**Stage 1 displacement is always N/A (no predecessor). Stages 2 through N each require a displacement justification.**

---

#### Step 5 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

Before writing any gate string, pre-compute the cascade consequence for every non-echo gate in a structured audit table. This step ensures cross-gate cascade coherence — each cascade is aware of adjacent stage boundaries as a group, not computed in isolation during YAML assembly.

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2's cascade clause becomes ungrounded if gate 1 is absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 3's cascade clause becomes ungrounded if gate 2 is absent] |
| ... | ... | ... | ... | ... | ... |

The final column ("Adjacent gate N+1 loses") implements the gate-to-gate chain: for each non-echo gate, removing gate N explicitly names the consequence for gate N+1. The last non-echo gate's "Adjacent gate N+1 loses" entry names what the echo stage's arc-completion signal loses if that gate is absent.

---

#### Step 6 — Gate Format

Use this exact format for every non-echo stage gate string:

```
"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

The cascade-if-removed clause MUST use `->` arrow notation and MUST specify minimum cascade depth (2+ hops crossing arc-layer boundaries). The adjacent-gate consequence MUST be drawn from your Gate Cascade Audit Table (Step 5), not invented inline during YAML assembly.

---

#### Step 7 — Echo Stage Displacement Reasoning

Before writing the echo stage, provide explicit justification for why echo cannot run earlier than its last position:

- **(a) Arc-completion signal echo emits**: What signal does echo produce that no earlier stage can produce? Name the specific arc-completion assertion (e.g., "all signal namespaces have contributed at least one artifact — the topic is complete enough to be read as a whole").
- **(b) What breaks if echo fires at stage 2**: Name specifically what is ungrounded or false if echo fires before depth and synthesis layers have run (e.g., "arc-completion signal fires before flow/trace depth signals exist -> listen adoption simulation has no depth baseline -> synthesis targets unvalidated platform behavior -> echo marks topic complete with no evidence that platform behavior was validated").

Echo is architecturally last — not conventionally last. Its position is required by the evidence structure of the arc.

---

#### Step 8 — Arc Strategy

Before finalizing YAML, answer these questions:

1. What evidence arc does this program build? Name each stage's role in the arc (breadth -> depth -> validation -> synthesis -> closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed? Do not answer with "any gate" — name the scout handoff gate specifically and trace the cascade across all downstream arc layers.
3. What skills did you intentionally exclude, and why? (See Step 9 for the Skill Omission Register.)

---

#### Step 9 — YAML Assembly

Assemble the program.yaml using the stage groupings from Step 3, the gate strings from Step 6 (drawn verbatim from the Gate Cascade Audit Table in Step 5), the echo stage displacement reasoning from Step 7, and the arc strategy from Step 8.

Required YAML structure:

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
        - [namespace:skill]
      gate: "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

Constraints:
- Every skill in `skills` must be from the valid catalog above
- Every non-echo stage must have a `gate` value that is non-trivial
- Echo stage must be last, have `skills: []`, and `auto: true`
- No other stage may be named `echo`
- Skills must be ordered by namespace dependency layer (scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals)

---

### Verification Checklist

Before finalizing output:

- [ ] Stage Displacement Register complete: every non-echo stage 2+ has a justification row with 2+ hop cascade
- [ ] Gate Cascade Audit Table complete: every non-echo gate has a cascade row + adjacent-gate-loses column
- [ ] Every gate string uses the exact format from Step 6 with `->` notation and minimum depth specification
- [ ] Echo displacement reasoning provided: arc-completion signal named + consequence of early placement named
- [ ] Arc strategy answered: evidence arc named + first-gate (scout handoff) cascade traced
- [ ] All skills in YAML are valid catalog skills
- [ ] YAML is syntactically valid

---

## V-02 — Stage Cohesion Audit Table

**Axis**: Before YAML assembly, require a Stage Cohesion Audit Table: for each proposed stage, list (a) constituent skills, (b) the shared phase goal justifying this exact grouping, and (c) what breaks if any one skill is moved to a different stage.

**Hypothesis**: Adding a Stage Cohesion Audit Table will produce program.yaml stages where skill groupings are architecturally justified rather than heuristically assembled, generating per-skill displacement rationale that is absent in V-01 (Stage Displacement Register justifies stage boundaries, not individual skill groupings) and V-03 (Skill Omission Register justifies excluded skills, not included ones).

**R7 new elements vs R6 V-05 baseline**:
- Stage Cohesion Audit Table: required pre-YAML step listing per-stage skills, shared phase goal, and what breaks if any constituent skill is moved to a different stage
- Distinct from Stage Displacement Register (V-01): that justifies stage position; this justifies skill-grouping rationale within each stage
- Distinct from Skill Omission Register (V-03): that justifies exclusions; this justifies inclusions
- Distinct from C-06 (which checks whether output stages group meaningfully): this pre-computes the grouping rationale before any stage is written

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. The program is a plan, not an executor — every skill can run standalone without the program. Your job is to produce a program that a team could follow as a sequenced evidence-building arc.

**This variation defeats skill groupings that pass topological ordering but contain no explicit justification for why exactly these skills belong in exactly this stage together — defeating that failure by requiring a Stage Cohesion Audit Table that pre-computes, for every stage, the shared phase goal and the consequence of moving any constituent skill to a different stage. This is the skill-grouping parallel of the Gate Cascade Audit Table, applied to stage membership before YAML assembly.**

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

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the justification column must answer: **why this actor cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------------|----------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for. All artifact names and stage groupings should be coherent with this topic.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. You do not need to include every skill — the program is topic-specific. Record your selected skills as a flat list grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Each stage should represent a coherent phase of work. Name each stage with a human-readable label (e.g., `discovery`, `validation`, `depth`, `synthesis`). Do not use skill names as stage names.

---

#### Step 4 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage you proposed in Step 3, produce the following cohesion audit. This is a mandatory pre-computation step — do not skip it or merge it with YAML assembly.

| Stage Name | Constituent Skills | Shared Phase Goal (why exactly these skills together) | What breaks if [skill] is moved to a different stage |
|------------|-------------------|------------------------------------------------------|------------------------------------------------------|
| [stage 1]  | [skill A, skill B, skill C] | [The goal that all three skills jointly serve — name what evidence is incomplete if any one is missing from this stage] | Moving [skill A] earlier: [consequence]; Moving [skill B] later: [consequence]; Moving [skill C] later: [consequence] |
| [stage 2]  | [skill D, skill E] | [Shared phase goal] | Moving [skill D] earlier: [consequence]; Moving [skill E] earlier: [consequence] |
| ... | ... | ... | ... |

Each "What breaks" entry must name a specific consequence — not just "the stage is incomplete" but what downstream artifact or layer is degraded. At minimum: one displacement consequence per constituent skill.

**The shared phase goal is the test: if two skills do not jointly serve the same phase goal, they should not be in the same stage.**

---

#### Step 5 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

Before writing any gate string, pre-compute the cascade consequence for every non-echo gate in a structured audit table. This step ensures cross-gate cascade coherence — each cascade is aware of adjacent stage boundaries as a group, not computed in isolation during YAML assembly.

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2's cascade clause becomes ungrounded if gate 1 is absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 3's cascade clause becomes ungrounded if gate 2 is absent] |
| ... | ... | ... | ... | ... | ... |

The final column ("Adjacent gate N+1 loses") implements the gate-to-gate chain: for each non-echo gate, removing gate N explicitly names the consequence for gate N+1.

---

#### Step 6 — Gate Format

Use this exact format for every non-echo stage gate string:

```
"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

The cascade-if-removed clause MUST use `->` arrow notation and MUST specify minimum cascade depth (2+ hops crossing arc-layer boundaries). The adjacent-gate consequence MUST be drawn from the Gate Cascade Audit Table (Step 5).

---

#### Step 7 — Echo Stage Displacement Reasoning

Before writing the echo stage, provide explicit justification for why echo cannot run earlier than its last position:

- **(a) Arc-completion signal echo emits**: What signal does echo produce that no earlier stage can produce? Name the specific arc-completion assertion.
- **(b) What breaks if echo fires at stage 2**: Name specifically what is ungrounded or false if echo fires before depth and synthesis layers have run.

Echo is architecturally last — not conventionally last.

---

#### Step 8 — Arc Strategy

Before finalizing YAML, answer these questions:

1. What evidence arc does this program build? Name each stage's role in the arc (breadth -> depth -> validation -> synthesis -> closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed? Do not answer with "any gate" — name the scout handoff gate specifically and trace the cascade across all downstream arc layers.
3. How does the Stage Cohesion Audit Table (Step 4) validate the stage groupings? Name one stage where the cohesion audit changed or confirmed a grouping decision.

---

#### Step 9 — YAML Assembly

Assemble the program.yaml using the stage groupings from Step 3 (validated by Step 4), the gate strings from Step 6 (drawn from Step 5), the echo displacement reasoning from Step 7, and the arc strategy from Step 8.

Required YAML structure:

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
        - [namespace:skill]
      gate: "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

Constraints:
- Every skill in `skills` must be from the valid catalog above
- Every non-echo stage must have a `gate` value that is non-trivial
- Echo stage must be last, have `skills: []`, and `auto: true`
- No other stage may be named `echo`
- Skills must be ordered by namespace dependency layer (scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals)

---

### Verification Checklist

Before finalizing output:

- [ ] Stage Cohesion Audit Table complete: every non-echo stage has a cohesion row with shared phase goal + per-skill displacement consequence
- [ ] Gate Cascade Audit Table complete: every non-echo gate has a cascade row + adjacent-gate-loses column
- [ ] Every gate string uses the exact format from Step 6 with `->` notation and minimum depth specification
- [ ] Echo displacement reasoning provided: arc-completion signal named + consequence of early placement named
- [ ] Arc strategy answered: evidence arc named + first-gate (scout handoff) cascade traced
- [ ] All skills in YAML are valid catalog skills
- [ ] YAML is syntactically valid

---

## V-03 — Skill Omission Register

**Axis**: After YAML assembly, produce an explicit Skill Omission Register listing every valid catalog skill NOT included in the program, each with a topic-specific exclusion reason.

**Hypothesis**: Requiring a Skill Omission Register will produce programs where excluded skills are deliberate topic-scoped decisions (e.g., "scout:competitors — no competing implementations in identified market segment") rather than accidental omissions, generating an exclusion-rationale artifact that is absent in V-01 (which registers stage displacement) and V-02 (which registers grouping cohesion) — and making catalog selection visible as a two-sided decision (inclusions + exclusions) rather than a one-sided list.

**R7 new elements vs R6 V-05 baseline**:
- Skill Omission Register: required post-YAML step listing every excluded catalog skill with a topic-specific reason
- Distinct from C-03 (which checks that included skills are valid catalog skills): this requires justification for what was excluded
- Distinct from C-11 (which requires the catalog to be listed inline): the catalog is already listed inline; the omission register forces deliberate selection by making exclusions as visible as inclusions

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. The program is a plan, not an executor — every skill can run standalone without the program. Your job is to produce a program that a team could follow as a sequenced evidence-building arc.

**This variation defeats accidental skill omissions — programs where skills are left out not by design but because the planner never considered them — by requiring an explicit Skill Omission Register after YAML assembly that names every catalog skill not included, each with a topic-specific reason. This makes catalog selection a two-sided decision: inclusions (in the YAML) and exclusions (in the register) are both visible and both deliberate.**

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

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the justification column must answer: **why this actor cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------------|----------------|
| PM / Strategist | Breadth (scout) | No prerequisites; all downstream work requires validated landscape. Moved later: draft-spec encodes undifferentiated assumptions -> review evaluates design not anchored in validated space -> prove tests hypotheses with no market grounding. |
| Architect + PM | Design (draft) | Requires >=2 scout artifacts to ground spec intent. Moved later: spec encodes undifferentiated requirements -> review critiques design detached from validated problem space -> prove prototype targets wrong system boundaries. |
| Team / Researcher | Validation (review + prove) | Requires draft-spec artifact as review target. Moved later: depth simulation runs against unreviewed spec -> prove synthesizes with no validation baseline -> listen simulates adoption of unvalidated design. |
| Domain Dev / System Dev | Depth (flow + trace) | Requires >=1 review-design artifact as simulation baseline. Moved later: flow models process with no validated boundary conditions -> trace hand-compiles paths not grounded in reviewed spec -> prove cannot cross-validate against platform simulation. |
| Team / Field | Synthesis (listen) | Requires depth-simulation artifacts as feedback basis. Moved later: listen simulates adoption of platform not yet validated by depth layer -> feedback surfaces issues trace would have caught -> synthesis inherits ungrounded adoption predictions. |
| Lead / Anyone | Arc closure (metrics + goals) | Requires all evidence layers. Moved earlier: metrics aggregate over incomplete evidence base -> goals commit targets based on partial signal coverage -> leadership brief cites predictions with no supporting signal chain. |

---

#### Step 1 — Topic

State the topic name you are planning for. All artifact names and stage groupings should be coherent with this topic.

---

#### Step 2 — Skill Selection

From the catalog above, select the skills relevant to this topic. You do not need to include every skill — the program is topic-specific. Record your selected skills as a flat list grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Each stage should represent a coherent phase of work. Name each stage with a human-readable label (e.g., `discovery`, `validation`, `depth`, `synthesis`). Do not use skill names as stage names.

---

#### Step 4 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

Before writing any gate string, pre-compute the cascade consequence for every non-echo gate in a structured audit table. This step ensures cross-gate cascade coherence — each cascade is aware of adjacent stage boundaries as a group, not computed in isolation during YAML assembly.

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2's cascade clause becomes ungrounded if gate 1 is absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 3's cascade clause becomes ungrounded if gate 2 is absent] |
| ... | ... | ... | ... | ... | ... |

The final column ("Adjacent gate N+1 loses") implements the gate-to-gate chain: for each non-echo gate, removing gate N explicitly names the consequence for gate N+1.

---

#### Step 5 — Gate Format

Use this exact format for every non-echo stage gate string:

```
"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

The cascade-if-removed clause MUST use `->` arrow notation and MUST specify minimum cascade depth (2+ hops crossing arc-layer boundaries). The adjacent-gate consequence MUST be drawn from the Gate Cascade Audit Table (Step 4).

---

#### Step 6 — Echo Stage Displacement Reasoning

Before writing the echo stage, provide explicit justification for why echo cannot run earlier than its last position:

- **(a) Arc-completion signal echo emits**: What signal does echo produce that no earlier stage can produce? Name the specific arc-completion assertion.
- **(b) What breaks if echo fires at stage 2**: Name specifically what is ungrounded or false if echo fires before depth and synthesis layers have run.

Echo is architecturally last — not conventionally last.

---

#### Step 7 — Arc Strategy

Before finalizing YAML, answer these questions:

1. What evidence arc does this program build? Name each stage's role in the arc (breadth -> depth -> validation -> synthesis -> closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed? Do not answer with "any gate" — name the scout handoff gate specifically and trace the cascade across all downstream arc layers.

---

#### Step 8 — YAML Assembly

Assemble the program.yaml using the stage groupings from Step 3, the gate strings from Step 5 (drawn verbatim from the Gate Cascade Audit Table in Step 4), and the echo displacement reasoning from Step 6.

Required YAML structure:

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
        - [namespace:skill]
      gate: "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

---

#### Step 9 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

After assembling the YAML, produce the Skill Omission Register. List every skill from the catalog above that does NOT appear in the program, with a topic-specific reason for its exclusion.

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Why this skill is not relevant to this topic — name the specific topic characteristic that makes this skill out of scope. Generic reasons ("not needed", "optional") do not pass — the reason must reference the topic.] |

**Every catalog skill not in the YAML must appear in this register. A skill cannot be silently absent — it is either included (in the YAML) or excluded (in the register with a reason). The register confirms that catalog selection was deliberate, not accidental.**

Example entries:
- `scout:competitors — not in scope; topic has no competing implementations in the identified market segment`
- `trace:migration — not in scope; topic is a new feature with no existing schema to migrate`
- `listen:adoption — deferred; topic is pre-launch and adoption metrics are not yet measurable`

---

### Verification Checklist

Before finalizing output:

- [ ] Gate Cascade Audit Table complete: every non-echo gate has a cascade row + adjacent-gate-loses column
- [ ] Every gate string uses the exact format from Step 5 with `->` notation and minimum depth specification
- [ ] Echo displacement reasoning provided: arc-completion signal named + consequence of early placement named
- [ ] Arc strategy answered: evidence arc named + first-gate (scout handoff) cascade traced
- [ ] Skill Omission Register complete: every catalog skill not in YAML has a topic-specific exclusion reason
- [ ] No skill is silently absent (either in YAML or in the Omission Register)
- [ ] All skills in YAML are valid catalog skills
- [ ] YAML is syntactically valid

---

## V-04 — Stage Displacement Register + Stage Cohesion Audit Table

**Axis**: V-01 + V-02 combined: Stage Displacement Register (per-stage position justification) AND Stage Cohesion Audit Table (per-stage skill-grouping justification), both required before YAML assembly.

**Hypothesis**: Combining Stage Displacement Register (V-01) and Stage Cohesion Audit Table (V-02) will produce programs where both stage boundaries (why stage N follows stage N-1) and stage memberships (why skill A belongs in stage N rather than stage N+1) are architecturally pre-justified, generating a stronger structural grounding signal than either register alone — while introducing no measurable interference between the two pre-computation steps since they target orthogonal dimensions of stage design (boundary vs. membership).

**R7 new elements vs R6 V-05 baseline**:
- Stage Displacement Register from V-01: why each non-echo stage cannot fire one position earlier + cascade if it does
- Stage Cohesion Audit Table from V-02: shared phase goal per stage + consequence of moving any constituent skill
- Both registers required before YAML assembly; both are orthogonal (displacement is stage-level, cohesion is skill-level)
- Combined interaction: displacement register justifies boundaries; cohesion table justifies memberships — together they make the full stage-design decision explicit before any YAML is written

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. The program is a plan, not an executor — every skill can run standalone without the program. Your job is to produce a program that a team could follow as a sequenced evidence-building arc.

**This variation defeats two orthogonal under-specification failures: (1) stage sequences that pass topological ordering but contain no justification for why each boundary is where it is, and (2) skill groupings that seem coherent but have no explicit phase goal tying constituent skills together. It defeats both by requiring, before YAML assembly, a Stage Displacement Register (why each non-echo stage cannot fire one position earlier + what breaks if it does) AND a Stage Cohesion Audit Table (what shared phase goal justifies each exact skill grouping + what breaks if any skill is moved). The two registers are orthogonal: displacement justifies stage-level boundaries; cohesion justifies skill-level memberships.**

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

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the justification column must answer: **why this actor cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------------|----------------|
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

From the catalog above, select the skills relevant to this topic. Record your selected skills grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Name each stage with a human-readable label.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce a displacement justification row. Stage 1 is always N/A (no predecessor). Stages 2 through N each require:

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [depends on artifact type from stage 1 that does not yet exist one position earlier] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops crossing arc-layer boundary] |
| [stage 3]  | 3        | [depends on artifact from stage 2] | [consequence A -> consequence B -> consequence C] |
| ... | ... | ... | ... |

"What breaks" must include a -> cascade of at least 2 ordered consequences crossing at least one arc-layer boundary. A single consequence is insufficient.

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce a cohesion justification row:

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved to a different stage |
|------------|-------------------|-------------------|--------------------------------------------------------|
| [stage 1]  | [skills] | [The specific evidence objective that ALL constituent skills jointly serve] | Moving [skill]: [specific consequence for the stage's phase goal] |
| [stage 2]  | [skills] | [Shared phase goal] | Moving [skill]: [consequence]; Moving [skill]: [consequence] |
| ... | ... | ... | ... |

The shared phase goal is the structural test: if two skills do not jointly serve a single nameable phase goal, they should not be in the same stage.

---

#### Step 6 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

Pre-compute ALL non-echo gate cascades before writing any gate string:

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2 loses if gate 1 absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 3 loses if gate 2 absent] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 7 — Gate Format

Use this exact format for every non-echo stage gate string:

```
"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

The cascade-if-removed clause MUST use `->` arrow notation and MUST specify minimum cascade depth (2+ hops crossing arc-layer boundaries). Gate strings are drawn verbatim from Step 6.

---

#### Step 8 — Echo Stage Displacement Reasoning

Before writing the echo stage, provide explicit justification for why echo cannot run earlier:

- **(a) Arc-completion signal echo emits**: Name the specific arc-completion assertion echo produces that no earlier stage can produce.
- **(b) What breaks if echo fires at stage 2**: Name specifically what is ungrounded if echo fires before depth and synthesis layers have run.

Echo is architecturally last — not conventionally last.

---

#### Step 9 — Arc Strategy

1. Name each stage's role in the evidence arc (breadth -> depth -> validation -> synthesis -> closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed? Name the scout handoff gate specifically and trace the cascade across all downstream arc layers.

---

#### Step 10 — YAML Assembly

Assemble the program.yaml using stages validated by Steps 4 and 5, gate strings from Step 7 (drawn from Step 6), echo displacement from Step 8, and arc strategy from Step 9.

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
      gate: "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

Constraints: all skills from valid catalog; every non-echo stage has a non-trivial gate; echo last with `skills: []` and `auto: true`; dependency ordering by namespace layer.

---

### Verification Checklist

- [ ] Stage Displacement Register complete: every non-echo stage 2+ has 2+ hop cascade in "What breaks"
- [ ] Stage Cohesion Audit Table complete: every non-echo stage has shared phase goal + per-skill displacement consequence
- [ ] Gate Cascade Audit Table complete: every non-echo gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses the exact format from Step 7 with `->` notation and depth floor
- [ ] Echo displacement reasoning: arc-completion signal named + consequence of early placement named
- [ ] Arc strategy: evidence arc named + first-gate (scout handoff) cascade traced
- [ ] All skills in YAML are valid catalog skills; YAML syntactically valid

---

## V-05 — Stage Displacement Register + Stage Cohesion Audit Table + Skill Omission Register + Artifact Lineage Chain

**Axis**: V-01 + V-02 + V-03 combined, plus a fourth axis: each gate threshold must trace the specific producing skill in the preceding stage via an extended Artifact Lineage Chain gate format.

**Hypothesis**: Adding the Artifact Lineage Chain gate format — "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]" — will produce gates where every threshold is traceable to a specific skill rather than an abstract namespace-level artifact count, generating a lineage-grounded gate vocabulary absent in V-01 through V-04. The Stage Displacement Register and Stage Cohesion Audit Table will produce no measurable interference with the lineage chain (they address stage-level and skill-grouping decisions; lineage addresses artifact provenance within gates).

**R7 new elements vs R6 V-05 baseline**:
- Stage Displacement Register from V-01: per-stage position justification before YAML
- Stage Cohesion Audit Table from V-02: per-stage skill-grouping justification before YAML
- Skill Omission Register from V-03: per-excluded-skill topic-specific reason after YAML
- Artifact Lineage Chain (new fourth axis): gate format string prefixed with "[Skill X in stage N produces artifact_type]" — ties each threshold to the specific producing skill rather than an abstract artifact count

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. The program is a plan, not an executor — every skill can run standalone without the program. Your job is to produce a program that a team could follow as a sequenced evidence-building arc.

**This variation defeats four orthogonal under-specification failures: (1) stage sequences with no justification for boundary placement, (2) skill groupings with no explicit phase goal, (3) accidental skill exclusions with no topic-specific reason, and (4) gate thresholds that reference abstract artifact counts without naming the producing skill. It defeats all four by requiring: a Stage Displacement Register (pre-YAML), a Stage Cohesion Audit Table (pre-YAML), a Skill Omission Register (post-YAML), and an Artifact Lineage Chain gate format that prefixes every gate threshold with "[Skill X in stage N produces artifact_type]" to tie every threshold to the specific producing skill.**

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

Only skills from this catalog may appear in any stage's `skills` list. Do not invent or abbreviate skill names.

---

#### Actor Ordering Table

Before designing stages, produce the following actor ordering table. For each actor, the justification column must answer: **why this actor cannot run earlier than its position — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)**

| Actor | Namespace Layer | Why this actor cannot run earlier — and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries) |
|-------|-----------------|----------------|
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

From the catalog above, select the skills relevant to this topic. Record your selected skills grouped by namespace.

---

#### Step 3 — Stage Grouping Proposal

Group your selected skills into 3–6 proposed stages (excluding echo). Name each stage with a human-readable label.

---

#### Step 4 — Stage Displacement Register (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce a displacement justification row. Stage 1 is always N/A.

| Stage Name | Position | Why it cannot fire one position earlier | What breaks if it fires one position earlier |
|------------|----------|-----------------------------------------|----------------------------------------------|
| [stage 1]  | 1        | N/A — first stage, no predecessor      | N/A                                          |
| [stage 2]  | 2        | [specific dependency on stage 1 artifact] | [consequence A -> consequence B -> arc-layer consequence, minimum 2 hops] |
| [stage 3]  | 3        | [specific dependency on stage 2 artifact] | [cascade chain, minimum 2 hops, crossing arc-layer boundary] |
| ... | ... | ... | ... |

---

#### Step 5 — Stage Cohesion Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo stage, produce a cohesion justification row:

| Stage Name | Constituent Skills | Shared Phase Goal | What breaks if any skill is moved |
|------------|-------------------|-------------------|-----------------------------------|
| [stage 1]  | [skills] | [The specific evidence objective all constituent skills jointly serve] | Moving [skill]: [consequence for the stage's phase goal completion] |
| [stage 2]  | [skills] | [Shared phase goal] | Moving [skill]: [consequence]; Moving [skill]: [consequence] |
| ... | ... | ... | ... |

---

#### Step 6 — Artifact Lineage Chain (REQUIRED BEFORE YAML ASSEMBLY)

For every non-echo gate, identify the specific skill in the preceding stage that produces the artifact type named in the gate threshold. This is the artifact lineage chain: each gate threshold is traceable to a specific producing skill, not only to a namespace or stage-level count.

| Gate | Producing Skill (in stage N) | Artifact Type Produced | Gate Threshold |
|------|------------------------------|------------------------|----------------|
| [stage 1] -> [stage 2] | [namespace:skill] | [artifact_type] | >=N [artifact_type] |
| [stage 2] -> [stage 3] | [namespace:skill] | [artifact_type] | >=N [artifact_type] |
| ... | ... | ... | ... |

If multiple skills in a stage contribute to a single artifact type, list the primary skill. If the gate threshold aggregates across skills, name the skill most directly responsible for the threshold artifact.

---

#### Step 7 — Gate Cascade Audit Table (REQUIRED BEFORE YAML ASSEMBLY)

Pre-compute ALL non-echo gate cascades before writing any gate string:

| Gate (Stage N -> Stage N+1) | Delivering Actor | Receiving Actor | Threshold | Cascade if removed (-> notation, 2+ hops, arc-layer crossing) | Adjacent gate N+1 loses |
|-----------------------------|-----------------|-----------------|-----------|---------------------------------------------------------------|-------------------------|
| [stage 1] -> [stage 2] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 2 loses if gate 1 absent] |
| [stage 2] -> [stage 3] | [actor] | [actor] | >=N artifact_type | [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] | [what gate 3 loses if gate 2 absent] |
| ... | ... | ... | ... | ... | ... |

---

#### Step 8 — Gate Format

Use this exact format for every non-echo stage gate string. The Artifact Lineage Chain prefix is REQUIRED:

```
"[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence if this gate is removed]"
```

Where:
- `[Skill X in stage N produces artifact_type]` is drawn verbatim from the Artifact Lineage Chain (Step 6)
- The delivering/receiving actors and threshold are drawn from the Gate Cascade Audit Table (Step 7)
- The cascade-if-removed clause MUST use `->` notation and MUST specify minimum cascade depth (2+ hops crossing arc-layer boundaries)
- The adjacent-gate consequence is drawn verbatim from Step 7

---

#### Step 9 — Echo Stage Displacement Reasoning

Before writing the echo stage, provide explicit justification for why echo cannot run earlier:

- **(a) Arc-completion signal echo emits**: What specific arc-completion assertion does echo produce? Name what becomes true when echo fires that was not true at any earlier stage.
- **(b) What breaks if echo fires at stage 2**: Name specifically what is ungrounded, premature, or false if echo fires before depth and synthesis layers have run — trace the consequence at least 2 hops (e.g., "echo marks arc-complete before flow/trace depth signals exist -> listen adoption simulation has no validated platform baseline -> synthesis inherits ungrounded adoption predictions").

Echo is architecturally last — not conventionally last.

---

#### Step 10 — Arc Strategy

1. Name each stage's role in the evidence arc (breadth -> depth -> validation -> synthesis -> closure).
2. Specifically: what is the multi-hop consequence cascade if the **first gate (scout handoff)** is removed? Name the scout handoff gate specifically, name the producing skill (from Step 6), and trace the cascade across all downstream arc layers.
3. What does the Artifact Lineage Chain (Step 6) reveal about the evidence arc? Name one gate where the lineage chain disambiguated which skill is the primary artifact producer.

---

#### Step 11 — YAML Assembly

Assemble the program.yaml using stages validated by Steps 4 and 5, gate strings from Step 8 (drawn from Steps 6 and 7), echo displacement from Step 9, and arc strategy from Step 10.

```yaml
topic: [topic-name]
program:
  stages:
    - name: [stage-name]
      skills:
        - [namespace:skill]
      gate: "[Skill X in stage N produces artifact_type]; [Delivering actor] hands off to [Receiving actor] when >=N artifact_type present -- removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries] -- and gate N+1 loses: [adjacent consequence]"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
```

Constraints: all skills from valid catalog; every non-echo stage has a non-trivial gate; echo last with `skills: []` and `auto: true`; dependency ordering by namespace layer.

---

#### Step 12 — Skill Omission Register (REQUIRED AFTER YAML ASSEMBLY)

List every skill from the catalog above that does NOT appear in the program:

| Skill | Namespace | Exclusion Reason (topic-specific) |
|-------|-----------|----------------------------------|
| [skill] | [namespace] | [Why this skill is not relevant to this topic — reference a specific topic characteristic. Generic reasons do not pass.] |

Every catalog skill not in the YAML must appear here. A skill cannot be silently absent — it is either included (in YAML) or excluded (in register with a reason).

Example entries:
- `scout:competitors — not in scope; topic has no competing implementations in the identified market segment`
- `trace:migration — not in scope; topic is a new feature with no existing schema to migrate`
- `goals:sla — deferred; topic SLA targets not yet defined; no baseline to commit against`

---

### Verification Checklist

Before finalizing output:

- [ ] Stage Displacement Register complete: every non-echo stage 2+ has 2+ hop cascade in "What breaks"
- [ ] Stage Cohesion Audit Table complete: every non-echo stage has shared phase goal + per-skill displacement consequence
- [ ] Artifact Lineage Chain complete: every non-echo gate has a producing skill identified
- [ ] Gate Cascade Audit Table complete: every non-echo gate has cascade + adjacent-gate-loses
- [ ] Every gate string uses Artifact Lineage Chain prefix + exact format from Step 8 with `->` notation and depth floor
- [ ] Echo displacement reasoning: arc-completion signal named + 2+ hop consequence of early placement named
- [ ] Arc strategy: evidence arc named + first-gate (scout handoff) cascade traced with producing skill named
- [ ] Skill Omission Register complete: every excluded catalog skill has a topic-specific reason
- [ ] No skill is silently absent (either in YAML or in the Omission Register)
- [ ] All skills in YAML are valid catalog skills; YAML syntactically valid
