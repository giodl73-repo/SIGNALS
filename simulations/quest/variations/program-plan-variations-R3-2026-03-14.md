Written to `simulations/quest/variations/program-plan-variations-R3-2026-03-14.md`.

---

## program-plan R3 — 5 Variations

**Gap from R2:** R2 V-05 retroactively scores 125/135. Both missing criteria (C-14, C-15) were present in R2 V-05 as _implicit_ patterns — the rubric v3 now requires them to be _explicit_.

| ID | Axis | C-14 | C-15 | Predicted |
|----|------|------|------|-----------|
| **V-01** | Explicit contrast opener only | **P** | F | 130/135, GOLDEN |
| **V-02** | Causal actor table only | F | **P** | 130/135, GOLDEN |
| **V-03** | Both, minimal form | **P** | **P** | 135/135, GOLDEN |
| **V-04** | Both, role-pedagogy register | **P** | **P** | 135/135, GOLDEN |
| **V-05** | Full synthesis maximum | **P** | **P** | 135/135, GOLDEN |

**What each new criterion requires:**

**C-14 (explicit contrast opener)** — R2 V-05 said "The competitor you are designing against is unsequenced skill execution." The v3 rubric requires an explicit "this variation defeats that by [structural choice]" sentence. V-01 and V-05 use: *"This variation defeats that failure mode specifically by two structural choices enforced before any skill is placed: (1) actor-layer assignment, and (2) a required handoff+threshold gate template."*

**C-15 (why-this-position column)** — R2 V-05 had the column but entries were pure labels ("Landscape signals establish what is worth building"). The v3 rubric requires per-actor causal reasoning. V-02 adds "what breaks if moved earlier" to each row. V-03 uses compact notes ("Moved later: design targets an unvalidated problem"). V-04/V-05 use full prose with multi-sentence causal explanations per actor.

**Three hypotheses to resolve in scoring:**

- **R3-H01**: Does C-14 require the word "defeats" or does any explicit contrast ("breaks that pattern by") pass? V-04 uses different phrasing — cross-reference with V-01/V-05 if scores split.
- **R3-H02**: Does C-15 require prose depth or do compact "what breaks if moved" notes suffice? V-03 is the minimal test case.
- **R3-H04**: Did R2 V-05's C-15 fail because of entry depth or absence of "if moved" reasoning? V-01 inherits R2's table with slightly richer entries — if V-01 unexpectedly passes C-15, the gap was shallower than assumed.
he contrast opener is explicit and structurally precise; the actor table includes both "why
  here" and "what breaks if moved" for each actor.

---

## V-01 -- Explicit Contrast Opener (C-14)

**Axis**: C-14 single axis -- the opener becomes an explicit contrast statement naming the
failure mode AND naming the structural choice that defeats it. Actor table is unchanged from
R2 V-05 (one-sentence "Why this position" entries; C-15 at R2 level).
**Hypothesis**: An opener that says "Naive [approach] fails by [specific mode]. This variation
defeats that by [structural choice A] and [structural choice B]" passes C-14 because failure
mode and defeating structural choice are co-located in one sentence, making the contrast
explicit. C-15 fails: table has column but short entries without "what breaks if moved" logic.
**Predicted**: C-01--C-13 PASS, C-14 PASS, C-15 FAIL, C-16 PASS, C-17 PASS -> **130/135, GOLDEN**

---

Naive `program:plan` outputs have a documented failure mode: they produce flat YAML -- skills
sorted by namespace order, gates that say "complete" or "stage done," stages with no arc logic.
The output passes YAML validation but cannot answer: when should this stage advance? Which
artifact unlocks the next stage? Why is this skill in this stage and not the next? The failure
is not syntax -- it is absence of evidence arc.

**This variation defeats that failure mode specifically by enforcing two structural choices
before a single skill is placed**: (1) an actor-layer assignment that maps each namespace to
an arc position (Breadth -> Design -> Depth -> Synthesis), and (2) a unified
handoff+threshold gate template that forces actor-transition language with a quantified
threshold into every gate. Those two choices -- not step-by-step listing -- are what produce
a program with genuine sequencing logic rather than a namespace-sorted file.

---

**Actor assignments** -- each namespace belongs to a primary actor:

| Actor | Namespaces | Arc layer | Why this position |
|-------|-----------|-----------|------------------|
| PM | `scout` | Breadth | Landscape signals establish what is worth building; nothing downstream can start without them |
| Architect/PM | `draft` | Design | Design artifacts anchor what is being validated; cannot exist without scout breadth |
| Team, Researcher | `review`, `prove` | Depth | Validation and investigation require a design to evaluate |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Simulation requires both a spec and a process model |
| Team | `listen` | Synthesis | Post-ship simulation requires depth signals to interpret |
| Anyone | `topic` | Synthesis | Narrative and readiness require all prior signals |

**Evidence arc** -- each layer's output is the input of the next:

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

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis). This mapping determines stage grouping and gate
positions.

**Step 4 -- Write handoff gates using `>=N` syntax.** For each non-echo stage, write the
gate as a handoff condition in this required format:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name the delivering actor and the receiving actor.
- Name specific artifact types: `scout-feasibility`, `draft-spec` -- not "signal" in the abstract.
- The `>=N` threshold is required in every gate where a count is meaningful.
- "Done", "ready", "complete" are not gates -- replace with a specific threshold.

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

## V-02 -- Causal Actor Table (C-15)

**Axis**: C-15 single axis -- the actor table gains per-actor causal rationale combining
"why this position" with "what breaks if moved earlier." Opener is unchanged from R2 V-05
("The competitor you are designing against is unsequenced skill execution").
**Hypothesis**: Per-actor rationale that names what would break if the actor moved earlier
teaches causal arc logic inline and passes C-15 because each entry provides genuine per-actor
reasoning, not just a position label. C-14 fails: opener is the R2 implicit contrast with no
"this variation defeats that by [structural choice]" statement.
**Predicted**: C-01--C-13 PASS, C-14 FAIL, C-15 PASS, C-16 PASS, C-17 PASS -> **130/135, GOLDEN**

---

A program plan is an evidence arc: the team starts broad (breadth signals), narrows to depth
(validation and simulation), then synthesizes into a decision. This arc is not a suggestion --
it is why gates exist. Each gate protects the next stage from starting before it has material
to work with.

**The competitor you are designing against is unsequenced skill execution.**

---

**Actor assignments** -- read the justification column before assigning skills. Each entry
names why this actor is at this arc position and what breaks if moved earlier.

| Actor | Namespaces | Arc layer | Why this position -- and what breaks if moved earlier |
|-------|-----------|-----------|------------------------------------------------------|
| PM | `scout` | Breadth | Must run first: scout signals have no prerequisites, and every downstream layer depends on them. Moved later: design is anchored in the author's assumptions rather than validated landscape signals; review critiques a design targeting the wrong problem; prove investigates a hypothesis without market grounding. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier (before scout): design is unconstrained speculation with no landscape anchor. Moved later (after review): the team is reviewing nothing, then a design appears to confirm what they already concluded. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved before draft: review:design produces critique without an anchor; prove:hypothesis launches an investigation without a defined target. Noise, not signal. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec and a process model. Moved before draft: simulation runs against an undefined system -- outputs cannot be compared against design intent. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback simulation produces anecdotes, not calibrated findings -- the team has no expectation model to compare against. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved before synthesis: narrative has no material; topic:status with no artifacts is a placeholder, not a readiness signal. |

**Evidence arc** -- each layer's output is the input of the next:

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

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** For each non-echo stage, write the
gate in this required format:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name both actors. Name specific artifact types. `>=N` threshold is required.
- "Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Stage names: `discovery`, `design`, `validation`,
`synthesis` -- not `stage1`, not skill names.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what happens if any gate is removed.

---

## V-03 -- C-14 + C-15 Minimal Form

**Axes**: Both C-14 and C-15 added at minimum-sufficient form. Contrast opener names failure
mode and structural choice in one sentence. Justification column adds compact "what breaks if
moved" notes without expanding to full prose.
**Hypothesis**: Minimum implementation of both criteria scores 135, confirming the rubric
rewards structural signal (contrast statement present + causal column entry present) rather
than elaboration depth. If V-03 scores 130 while V-04/V-05 score 135, the failure is entry
depth, not structural presence.
**Predicted**: All 17 PASS -> **135/135, GOLDEN**

---

Naive program plans sort skills by namespace and call that sequencing. Their gates say "ready"
or "complete" -- conditions that cannot be verified. Their stage boundaries reflect file
organization, not workflow logic. **This variation defeats that by two mechanisms: actor-layer
assignment that grounds every stage in a workflow transition, and a required handoff+threshold
gate format that forces artifact naming and role transitions simultaneously.**

---

**Actor assignments** -- assign skills to arc layer using this table. The justification column
names why this actor is at this position and what breaks if moved earlier.

| Actor | Namespaces | Arc layer | Why this position (what breaks if moved earlier) |
|-------|-----------|-----------|--------------------------------------------------|
| PM | `scout` | Breadth | No prerequisites; all downstream work requires landscape context. Moved later: design targets an unvalidated problem. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Moved earlier: design is unconstrained speculation with no landscape anchor. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact to evaluate. Moved earlier: review critiques a void; prove investigates an undefined target. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires both a spec and a process model. Moved before draft: simulation runs against an undefined system. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate. Moved earlier: feedback simulation produces anecdotes, not calibrated findings. |
| Anyone | `topic` | Synthesis | Requires all prior signals. Moved earlier: narrative has no material; readiness signal is empty. |

**Evidence arc** -- each layer produces what the next layer consumes:

1. **Breadth** (scout): Landscape signals. Nothing downstream is productive without them.
2. **Design** (draft): Authored intent anchored in breadth.
3. **Depth** (review, prove, flow, trace): Stress-testing the design.
4. **Synthesis** (listen, topic): Post-signal conclusions.

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
the topic. Identify the decision this investigation must answer.

**Step 2 -- Select skills.** For each actor group, choose only the skills this topic needs.
Select only from the catalog above.

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules: Name both actors. Name specific artifact types. `>=N` threshold required.
"Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Names reflect arc intent (`discovery`, `design`,
`validation`, `synthesis`), not skill names or `stage1`.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages`, and echo.
Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** Write 2-3 sentences: what this plan prioritizes early,
what it defers, and what happens if any gate is removed.

---

## V-04 -- C-14 + C-15 Role-Pedagogy Register

**Axes**: Both C-14 and C-15 using pedagogical framing. The contrast opener teaches the
reader what pattern to break. The actor table justification column is written as causal
prose ("X cannot run before Y because Y produces what X needs") rather than compact notes.
**Hypothesis**: Pedagogical register in both criteria produces stronger C-09 pass rate
because the model is explicitly taught the causal chain rather than reading a reference
table. Tests whether prose depth in C-15 entries affects model arc reasoning quality.
**Predicted**: All 17 PASS -> **135/135, GOLDEN**

---

The pattern this variation is designed to break: a program plan that is secretly a skill list.
A skill list passes every structural check -- it has stages, gates, and an echo -- but its
gates say "complete" instead of naming artifacts, its stages reflect namespace categories
rather than workflow phases, and removing any gate would not change the outcome because no
gate was protecting a real dependency. **This variation breaks that pattern by requiring two
things a skill list cannot satisfy: a causal actor ordering with per-actor justification
explaining what breaks if the actor moves, and a gate format that exposes the handoff --
who delivers what to whom at what threshold.**

---

**Actor arc table** -- before placing any skill, understand why each actor is at this arc
position. The justification column is a causal explanation, not a label.

| Actor | Namespaces | Arc layer | Why this actor cannot run earlier |
|-------|-----------|-----------|-----------------------------------|
| PM | `scout` | Breadth | The PM runs first because scout signals have no prerequisites. Every other actor needs something from scout: the Architect needs landscape context to anchor the design; the Team needs a defined problem to validate against. Without scout, breadth signals are invented by each actor independently, producing inconsistent assumptions downstream. |
| Architect/PM | `draft` | Design | The Architect runs after scout because the draft converts landscape signals into a testable design artifact. Running draft before scout means the design is anchored in the author's intuition, not validated landscape signals. The Team cannot review what does not exist; moving draft after review creates a circular dependency. |
| Team, Researcher | `review`, `prove` | Depth | Review and prove run after draft because they evaluate a specific artifact. Without a draft-spec, review:design produces open-ended critique without an anchor; prove:hypothesis launches an investigation without a target hypothesis anchored in a design decision. Moving them before draft produces noise, not signal. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Flow and trace simulate system behavior and structure. Both require a spec to define what is being simulated. Running flow or trace before draft means simulating an undefined system -- outputs cannot be compared against design intent because no design intent exists. |
| Team | `listen` | Synthesis | Listen simulates post-ship feedback. Without depth signals as a prior baseline, feedback simulation is ungrounded -- the team cannot distinguish expected from unexpected findings because they have no expectation model from validation. |
| Anyone | `topic` | Synthesis | Topic skills aggregate all prior signals into narrative or readiness. Running topic before signals exist means the narrative has no material; topic:status with no artifacts produces a placeholder, not a decision input. |

**Evidence arc** -- each layer produces exactly what the next layer consumes:

1. **Breadth** (scout): Landscape signals that define what is worth building.
2. **Design** (draft): Testable artifacts that define what is being validated.
3. **Depth** (review, prove, flow, trace): Validation signals against the design.
4. **Synthesis** (listen, topic): Conclusions drawn from the full signal set.

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

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis).

**Step 4 -- Write handoff gates using `>=N` syntax.** Required format for every non-echo
gate -- all three elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name both actors. Name specific artifact types (`scout-feasibility`, `draft-spec`).
- The `>=N` threshold is required.
- "Done", "ready", "complete" are not gates.

**Step 5 -- Group into 3-6 named stages.** Stage names communicate arc intent:
`discovery`, `design`, `validation`, `synthesis` -- not `stage1`, not skill names.

**Step 6 -- Add the echo.** Final stage is always `echo` with `skills: []` and `auto: true`.
No other stage may be named `echo`.

**Step 7 -- Produce the YAML.** Valid `program.yaml` with `topic`, `stages` (name, skills,
gate), and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

**Step 8 -- State the arc strategy.** After the YAML, write 2-3 sentences: what this plan
prioritizes early, what it defers, and what happens if any gate is removed.

---

## V-05 -- Full Synthesis Maximum

**Axes**: All 17 criteria given their strongest implementation. C-14 opener is explicit,
structurally precise, and names both the failure mode and the two structural choices that
defeat it in a single sentence. C-15 actor table combines "why here" with "what breaks if
moved" for every actor -- maximum causal reasoning per cell. C-16 gate template is required
with all three elements co-located. C-17 removal clause is in Step 8.
**Hypothesis**: The union of R2 V-05's passing structure (C-01--C-13, C-16, C-17) plus
explicit C-14 contrast statement plus rich C-15 causal table produces 135/135 without
instruction density degradation. If V-05 scores below 135, the failure isolates to one of
the two new criteria -- cross-reference with V-01 and V-02 single-axis results.
**Predicted**: All 17 PASS -> **135/135, GOLDEN**

---

Naive `program:plan` outputs fail in a specific, reproducible way: they produce flat YAML
with abstract gates. Skills are sorted by namespace order. Gates say "complete," "stage done,"
or "artifacts are ready" -- conditions that cannot be verified because they name no artifact.
Stage boundaries reflect namespace categories, not workflow phases. Removing any gate changes
nothing, because no gate was protecting a real dependency.

**This variation defeats that failure mode specifically by two structural choices enforced
before any skill is placed**: (1) an actor-layer assignment table with per-actor causal
justification that names why each actor belongs at their arc position and what breaks if
moved, and (2) a required handoff+threshold gate template that forces three co-located
elements -- actor names, minimum threshold, artifact type -- into every gate. A flat skill
list cannot satisfy either requirement.

---

**Actor assignments** -- read the full justification column before assigning skills. Each
entry explains why this actor is at this arc position AND what breaks if moved earlier.

| Actor | Namespaces | Arc layer | Why this position and what breaks if moved earlier |
|-------|-----------|-----------|-----------------------------------------------------|
| PM | `scout` | Breadth | Must run first: scout signals have no prerequisites, and every downstream layer depends on them. Moved later: design is anchored in the author's assumptions rather than validated landscape signals; review critiques a design targeting the wrong problem; prove investigates a hypothesis without market grounding. Scout gates protect all downstream layers simultaneously. |
| Architect/PM | `draft` | Design | Requires >=1 scout artifact. Design artifacts define the shared target for review, prove, flow, and trace. Moved earlier (before scout): design is unconstrained speculation with no landscape anchor. Moved later (after review): the team reviews a void, then a design appears to confirm conclusions they already reached. Draft gates protect the entire Depth layer from running against an undefined target. |
| Team, Researcher | `review`, `prove` | Depth | Requires a draft artifact. Without a draft-spec, review:design produces open-ended critique without an anchor; prove:hypothesis launches an investigation without a target. Moved before draft: noise, not signal -- critiques and hypotheses are invented rather than derived. Review/prove gates protect synthesis from drawing conclusions from unvalidated designs. |
| Domain Dev, System Dev | `flow`, `trace` | Depth | Requires a spec (what to simulate) and a process model (what to trace). Can run in parallel with review/prove within the Depth layer, but not before draft. Moved before draft: simulation runs against an undefined system -- outputs cannot be compared against design intent because no design intent exists. |
| Team | `listen` | Synthesis | Requires depth signals to calibrate expectations. Moved before depth: feedback simulation produces anecdotes, not calibrated findings -- the team cannot distinguish expected from unexpected findings because they have no expectation model from validation. |
| Anyone | `topic` | Synthesis | Requires all prior signals to be meaningful. Moved before synthesis: narrative has no material; topic:status with no artifacts is a placeholder, not a readiness signal. The topic gate protects the team's decision from being based on an empty or premature signal set. |

**Evidence arc** -- each layer produces exactly what the next layer consumes:

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

**Step 3 -- Map to arc layers.** Assign selected skills to their arc layer
(Breadth -> Design -> Depth -> Synthesis). This mapping determines stage grouping and gate
positions.

**Step 4 -- Write handoff gates using `>=N` syntax.** For each non-echo stage, write the
gate in this required format -- all three elements must appear together:

  `"[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]"`

Examples:
- `"PM hands off to Architect when >=2 scout artifacts including scout-requirements are present"`
- `"Architect hands off to Team when >=1 draft-spec artifact is present"`
- `"Team hands off to Dev when >=2 depth signals (review-design and prove-hypothesis) are present"`

Rules:
- Name the delivering actor and the receiving actor -- both required.
- Name specific artifact types: `scout-feasibility`, `draft-spec` -- not "signal" in the abstract.
- The `>=N` threshold is required in every gate where a count is meaningful.
- "Done", "ready", "complete" are not gates -- replace with threshold and artifact name.

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

| ID | Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | Total | Golden |
|----|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | Explicit contrast opener | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | F | P | P | **130** | YES |
| V-02 | Causal actor table | P | P | P | P | P | P | P | P | P | P | P | P | P | F | **P** | P | P | **130** | YES |
| V-03 | C-14+C-15 minimal | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | P | P | **135** | YES |
| V-04 | C-14+C-15 role-pedagogy | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | P | P | **135** | YES |
| V-05 | Full synthesis maximum | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | P | P | **135** | YES |

Points: Essential 12 pts x 5 = 60 | Recommended 10 pts x 3 = 30 | Aspirational 5 pts x 9 = 45
Max 135 | Golden = all essential pass AND composite >= 108.

---

## R3 Hypotheses to Resolve

**R3-H01: Does C-14 require "this variation defeats that by X" phrasing or does any explicit
contrast statement pass?**
V-01 and V-05 use: "This variation defeats that failure mode specifically by two structural
choices." V-03 uses: "This variation defeats that by two mechanisms." V-04 uses: "This
variation breaks that pattern by requiring two things a skill list cannot satisfy." If C-14
scoring requires the word "defeats" or the phrase "this variation defeats," V-04 is the
riskier form. Cross-reference V-04 vs V-01 if scores differ.

**R3-H02: Does C-15 require prose entries or do compact "what breaks if moved" notes pass?**
V-03 uses compact entries: "Moved later: design targets an unvalidated problem." V-04 uses
full prose paragraphs. V-05 uses multi-sentence cells. If C-15 requires minimum prose depth,
V-03 may fail while V-04 and V-05 pass. If V-03 passes, compact notes are sufficient.

**R3-H03: Does combining C-14 + C-15 degrade any R2 V-05 stable criterion?**
V-03, V-04, V-05 all combine both new criteria. The risk is instruction density: if the
longer actor table or opener crowds out a prior step's clarity, C-09 or C-12 could regress.
If all three score 135, instruction density is not an issue.

**R3-H04: Is the retroactive C-15 fail in R2 V-05 about entry depth or absence of "if moved"
reasoning?**
R2 V-05 had the column but entries were pure descriptions: "Landscape signals establish what
is worth building." V-01 inherits this table unchanged but adds slightly richer entries
("cannot exist without scout breadth"). If V-01 unexpectedly passes C-15, it means the gap
was entry depth, not the absence of "if moved" reasoning -- and V-02 through V-05 were all
overkill for C-15.
