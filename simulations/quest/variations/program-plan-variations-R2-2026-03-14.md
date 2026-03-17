Written to `simulations/quest/variations/program-plan-variations-R2-2026-03-14.md`.

---

## program-plan Round 2 — 5 Variations

All five target the v2 rubric's new aspirational criteria (C-11, C-12, C-13) and fix R1's C-03/C-11 blocker by embedding the full 46-skill catalog inline in every variation.

| ID | Axis | New criteria targeted | Predicted |
|----|------|----------------------|-----------|
| **V-01** | C-11 baseline — V-04 rebuilt | C-11 | 105/115, GOLDEN |
| **V-02** | Arc-First | C-09 + C-11 | 110/115, GOLDEN |
| **V-03** | Actor Handoff Gates | C-12 + C-11 | 110/115, GOLDEN |
| **V-04** | Syntax-Anchored Gates | C-13 + C-11 (prescribed format, not example) | 105/115, GOLDEN |
| **V-05** | Full Synthesis | All five: C-09 + C-10 + C-11 + C-12 + C-13 | 115/115, GOLDEN |

**Key structural decisions:**

- **V-01** is the clean rebuild of R1's golden (V-04) with the updated 46-skill catalog. All variations start from this floor.
- **V-02 vs V-03 vs V-04** are single-axis isolations — each adds exactly one new aspirational pattern. The scorecard will confirm which contributes most.
- **V-04** differentiates from V-01 by making `>=N artifact_type` a *required format* (not just an example): "A gate without a `>=N` threshold is incomplete — add the count." This is C-13's core test.
- **V-05** is the synthesis — R1 V-04's actor-ordering + V-05's inertia framing + arc strategy requirement (step 8) + handoff gate language + embedded `>=N` syntax. Targeting 115/115.

The R1 insight that drives everything: **C-12 is the new differentiator.** V-03 and V-05 are the only variations with actor handoff language. If C-12 scoring is strict, the gap between non-handoff (105) and handoff (110+) variations is the dominant R2 signal.
ition.** If V-05 reaches 115/115, the individual-axis
  variations confirm the decomposition. If V-05 degrades (too much instruction density),
  that isolates the signal.

- **The 46-skill catalog used:** scout (8), draft (3), review (4), flow (7), trace (7),
  prove (8), listen (3), topic (6). Program, quest, and trace-skill are meta-namespaces
  excluded from feature-investigation programs.

---

## V-01 -- V-04 Rebuilt for v2

**Axis**: C-11 baseline (V-04 updated with current 46-skill catalog and v2 rubric)
**Hypothesis**: The R1 golden pattern -- actor-ordering + inline catalog + quantified gate
syntax -- should reliably score golden under v2. Establishes the v2 floor before adding new
aspirational axes. Predicted: C-01 to C-08 PASS, C-09 FAIL, C-10 PASS, C-11 PASS, C-12 FAIL,
C-13 PASS -> 105/115, GOLDEN.

---

Signal assigns each namespace to a primary actor in the feature investigation workflow:

- `scout` -> PM proves the idea
- `draft` -> Architect/PM authors the design
- `review`, `prove` -> Team validates, researchers investigate
- `flow`, `trace` -> Domain dev and system dev simulate
- `listen` -> Team simulates post-ship feedback
- `topic` -> Anyone manages the narrative

A program plan sequences these actors in the order that makes evidence-building sense. You do
not schedule a review before there is something to review. You do not measure before there is
a design.

To build the plan:

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and any existing signal artifacts for
the topic. Note what has already been produced -- do not re-plan completed stages.

**Step 2 -- Assign actor order.** For this topic, list the actors in the sequence they should
engage: PM first (scout), then Architect/PM (draft), then Team (review/prove), then Dev
(flow/trace), then Team again (listen/topic).

**Step 3 -- Select skills per actor.** For each actor, choose only the Signal skills relevant
to this topic. The complete catalog -- no other skill names exist:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

If a skill name is not in this list, it does not exist. Do not invent names.

**Step 4 -- Write quantified gates.** For each non-echo stage, write a gate that:

- Names the specific artifact types that must exist (e.g., `scout-feasibility artifact present`).
- Specifies a minimum count using `>=N` syntax where meaningful:
  `>=2 scout artifacts present` or `scout-requirements artifact and draft-spec artifact both present`.
- Never uses vague terms: "done", "ready", "complete" are not valid gate values.

**Step 5 -- Produce the YAML.** Group actor-phases into 3-6 named stages. The final stage is
always `echo` with `skills: []` and `auto: true`. No other stage is named `echo`. Save to
`simulations/program/plans/{topic}-plan-{date}.md`.

**Step 6 -- Summarize.** List actor-to-stage mapping in a table. Flag any actor group with no
skills selected for this topic.

---

## V-02 -- Arc-First Structure

**Axis**: C-09 single axis (evidence arc named and explicitly argued, on top of V-01 baseline)
**Hypothesis**: Requiring the model to state the arc strategy (what the plan prioritizes early,
defers, and protects against) after producing the YAML adds C-09 without disrupting V-01's
passing criteria. The arc framing also strengthens C-06 stage grouping.
Predicted: C-01 to C-08 PASS, C-09 PASS, C-10 PASS, C-11 PASS, C-12 FAIL, C-13 PASS ->
110/115, GOLDEN.

---

A program plan is an evidence arc: the team starts broad (breadth signals), then narrows to
depth (validation and simulation), then synthesizes into a decision. This arc is not a
suggestion -- it is why gates exist. Each gate protects the next stage from starting before
it has material to work with.

Signal assigns each namespace to an arc layer and a primary actor:

| Layer | Namespaces | Actor | Why this position |
|-------|-----------|-------|------------------|
| Breadth | `scout` | PM | Landscape signals; nothing downstream is productive without them |
| Design | `draft` | Architect/PM | Authored intent anchored in breadth signals |
| Depth | `review`, `prove`, `flow`, `trace` | Team, Dev | Validation requires a design to evaluate |
| Synthesis | `listen`, `topic` | Team | Conclusions require depth signals to draw from |

To build the plan:

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts.
Identify the decision this investigation must answer before the team can commit.

**Step 2 -- Select skills by arc layer.** For each layer, choose only the Signal skills this
topic needs. Not every skill applies to every topic. The complete catalog -- no other names
exist:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

**Step 3 -- Write artifact-grounded gates.** Each gate states what artifact types from the
prior arc layer must exist before the next layer can start:

- Reference artifact types by name (e.g., `scout-requirements artifact and draft-spec artifact present`).
- Specify a minimum signal count using `>=N` syntax where meaningful: `>=2 scout signals present`.
- "Done", "ready", "complete" are not gates -- name what must exist.

**Step 4 -- Group into named stages.** 3-6 stages. Stage names reflect arc layer intent:
`discovery`, `design`, `validation`, `synthesis` -- not skill names, not `stage1`.

**Step 5 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 6 -- Produce the YAML.** Valid `program.yaml` with topic, stages (name, skills, gate),
and the echo stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 7 -- State the arc strategy.** After the YAML, write 2 sentences: what this plan
prioritizes early, what it defers, and what the gates are protecting against.

---

## V-03 -- Actor Handoff Gates

**Axis**: C-12 single axis (gate conditions written as role-transition handoff language, on top
of V-01 baseline)
**Hypothesis**: Framing every gate as a "delivering actor -> receiving actor" handoff condition
forces role-meaningful, artifact-specific gate text (C-12) and grounds stage boundaries in
workflow transitions (C-07, C-05). Does not explicitly require arc framing (C-09 tested
separately in V-02).
Predicted: C-01 to C-08 PASS, C-09 FAIL, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS ->
110/115, GOLDEN.

---

Signal assigns each namespace to a primary actor:

- `scout` -> PM proves the idea
- `draft` -> Architect/PM authors the design
- `review`, `prove` -> Team validates, researchers investigate
- `flow`, `trace` -> Domain dev and system dev simulate
- `listen` -> Team simulates post-ship feedback
- `topic` -> Anyone manages the narrative

A program plan is a handoff sequence. Each stage ends when one actor has produced what the
next actor needs. A gate is the handoff condition: what must actor A have produced before
actor B can meaningfully begin?

To build the plan:

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and any existing signal artifacts
for the topic.

**Step 2 -- Assign actor sequence.** For this topic, list actors in order: PM -> Architect/PM
-> Team -> Dev -> Team. Skip actor groups with no relevant skills for this topic.

**Step 3 -- Select skills per actor.** Choose only the skills this topic needs. The complete
catalog -- no other names exist:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

**Step 4 -- Write handoff gates.** Each gate is a handoff condition from one actor to the
next. Gate format: "[Delivering actor] hands off to [Receiving actor] when [artifact condition]."

Rules:
- Name the delivering actor and the receiving actor explicitly.
- Name the specific artifact type(s) being handed off: `scout-feasibility artifact`,
  `draft-spec artifact` -- not "signal", not "artifact" in the abstract.
- Quantify with `>=N` syntax where a count is meaningful:
  `PM hands off to Architect when >=2 scout artifacts including scout-requirements are present`.
- "Done", "ready", "complete" are not handoff conditions -- state what the receiving actor
  needs to begin productive work.

**Step 5 -- Produce the YAML.** Group actor stages into 3-6 named stages (arc phase names,
not actor names: `discovery`, `design`, `validation`). Final stage is always `echo` with
`skills: []` and `auto: true`. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 6 -- Summarize.** Show the handoff chain as a table:

| Stage | Delivering actor | Gate condition | Receiving actor |
|-------|-----------------|----------------|----------------|

---

## V-04 -- Syntax-Anchored Gates

**Axis**: C-13 single axis (prescribed `>=N artifact_type` format required in every gate, on
top of V-01 baseline)
**Hypothesis**: Making `>=N artifact_type` a required format -- not an optional illustration --
drives machine-checkable thresholds in every gate (C-10, C-13). No handoff language (C-12
tested separately in V-03); no arc strategy (C-09 tested separately in V-02).
Predicted: C-01 to C-08 PASS, C-09 FAIL, C-10 PASS, C-11 PASS, C-12 FAIL, C-13 PASS ->
105/115, GOLDEN.

---

Signal assigns each namespace to a primary actor in the feature investigation workflow:

- `scout` -> PM proves the idea
- `draft` -> Architect/PM authors the design
- `review`, `prove` -> Team validates, researchers investigate
- `flow`, `trace` -> Domain dev and system dev simulate
- `listen` -> Team simulates post-ship feedback
- `topic` -> Anyone manages the narrative

A program plan sequences these actors in evidence-building order. Gates are what make the
sequence meaningful: they prevent later-stage skills from running before the artifacts they
need to evaluate exist.

To build the plan:

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and any existing signal artifacts
for the topic.

**Step 2 -- Assign actor order.** PM first (scout), then Architect/PM (draft), then Team
(review/prove), then Dev (flow/trace), then Team (listen/topic). Note which actor groups
have no relevant skills for this topic.

**Step 3 -- Select skills per actor.** Choose only the skills this topic needs. The complete
catalog -- no other names exist:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

**Step 4 -- Write `>=N` gates.** Every non-echo gate must use this format:

  `gate: ">=N artifact_type [optional qualifier]"`

Examples:
- `gate: ">=2 scout artifacts including scout-requirements"`
- `gate: ">=1 draft-spec artifact present"`
- `gate: ">=3 depth signals (review or prove artifacts) and draft-spec artifact present"`

Rules:
- The `>=N` count prefix is required. A gate without a `>=N` threshold is incomplete -- add
  the count.
- The artifact type must be a real Signal artifact name, not "signal" or "artifact" in the
  abstract.
- "Done", "ready", "complete" are not gates. Replace every instance with a `>=N` threshold.

**Step 5 -- Produce the YAML.** Group actor-phases into 3-6 named stages. The final stage is
always `echo` with `skills: []` and `auto: true`. No other stage may be named `echo`. Save
to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 6 -- Summarize.** List actor-to-stage mapping and show each gate with its `>=N`
threshold. Flag any gate that could not be quantified and explain why.

---

## V-05 -- Full Synthesis

**Axes**: All five aspirational criteria combined: arc strategy (C-09) + quantified gates (C-10) +
inline catalog (C-11) + actor handoff language (C-12) + embedded `>=N` syntax (C-13)
**Hypothesis**: The union of R1 V-04's actor-ordering + inline catalog (golden, 95/100), R1
V-05's inertia framing (highest aspirational score), and the two new C-12/C-13 patterns
produces a prompt that reliably passes all 13 criteria. Full synthesis targets 115/115.
Predicted: All 13 criteria PASS -> 115/115, GOLDEN.

---

The naive program plan runs all skills at once with no ordering and no gates. Its failure mode
is well-known: review skills run before there is a design to review; trace skills run before
there is a spec to follow; prove skills launch hypothesis investigations without scout context
to anchor them. The result is noise, not signal.

Your job is to build the plan that defeats the naive approach. The plan is an **evidence arc**:
a staged handoff sequence where each actor produces exactly what the next actor needs. Every
gate you write is a handoff condition -- what must actor A have delivered before actor B can
begin meaningful work?

**The competitor you are designing against is unsequenced skill execution.**

---

**Actor assignments** -- each namespace belongs to a primary actor:

| Actor | Namespaces | Arc layer | Why this position |
|-------|-----------|-----------|------------------|
| PM | `scout` | Breadth | Landscape signals establish what is worth building |
| Architect/PM | `draft` | Design | Design artifacts anchor what is being validated |
| Team, Researcher | `review`, `prove` | Depth | Validation and investigation require a design to evaluate |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Simulation requires both a spec and a process to model |
| Team | `listen` | Synthesis | Post-ship simulation requires depth signals to interpret |
| Anyone | `topic` | Synthesis | Narrative and readiness require all prior signals |

**Evidence arc** -- actors engage in this order because each layer produces inputs for the next:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth signals.
3. **Depth** (review, prove, flow, trace): Stress-testing the design and the system.
4. **Synthesis** (listen, topic): Post-signal conclusions and readiness.

---

**Complete skill catalog** -- no other skill names exist. Any name not in this list is invalid:

- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

---

**To build the program plan:**

**Step 1 -- Read context.** Read `simulations/TOPICS.md` and existing signal artifacts for
the topic. Identify the decision this investigation must answer before the team can commit.

**Step 2 -- Select skills.** For each actor group, choose only the Signal skills this topic
needs. Not every skill applies to every topic. Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer (Breadth -> Design
-> Depth -> Synthesis). This mapping determines stage grouping and gate positions.

**Step 4 -- Write handoff gates using `>=N` syntax.** For each non-echo stage, write the gate
as a handoff condition in this form:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name the delivering actor and the receiving actor.
- Name specific artifact types: `scout-feasibility`, `draft-spec` -- not "signal" in the abstract.
- The `>=N` threshold is required in every gate where a count is meaningful.
- "Done", "ready", "complete" are not gates -- replace every instance with a specific threshold.

**Step 5 -- Group into 3-6 named stages.** Stage names communicate arc layer intent:
`discovery`, `design`, `validation`, `synthesis` -- not generic (`stage1`), not skill names.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
The echo surfaces what the signals revealed that was not in the original plan. No other stage
may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages` (name, skills,
gate), and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** After the YAML, write 2-3 sentences: what the plan
prioritizes early, what it defers, and what the gates are protecting against -- specifically,
what happens if any gate is removed.

---

## Predicted Score Summary

| ID | Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Total | Golden |
|----|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | Baseline (V-04 rebuilt) | P | P | P | P | P | P | P | P | F | P | P | F | P | **105** | YES |
| V-02 | Arc-First | P | P | P | P | P | P | P | P | P | P | P | F | P | **110** | YES |
| V-03 | Actor Handoff Gates | P | P | P | P | P | P | P | P | F | P | P | P | P | **110** | YES |
| V-04 | Syntax-Anchored Gates | P | P | P | P | P | P | P | P | F | P | P | F | P | **105** | YES |
| V-05 | Full Synthesis | P | P | P | P | P | P | P | P | P | P | P | P | P | **115** | YES |

Points: Essential 12 pts x 5 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 5 = 25 | Total max 115 | Golden = all essential pass AND composite >=92.

**V-01 vs V-04:** Both predict 105, through different paths. V-01 relies on V-04's R1 actor-role
structure for C-07; V-04 prescribes `>=N` as a required format rather than an example. Both
fail C-12. The scorecard will confirm whether prescription vs example matters for C-13.

**C-12 is the new R2 differentiator.** V-03 and V-05 are the only variations that address it.
If C-12 scoring is strict, the gap between V-01/V-04 (105) and V-03 (110) is large.

**C-09 remains the hardest aspirational to pass.** V-02 and V-05 are the only variations that
explicitly require an arc-strategy statement. If C-09 scoring is lenient (implied arc from
actor ordering counts), V-01/V-03/V-04 may also pass it, compressing the score distribution.
