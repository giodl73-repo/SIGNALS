Written to `simulations/quest/variations/program-plan-variations-R1-2026-03-14.md`.

---

## program-plan Variations — Round 1

Five complete skill body prompts across three single-axis and two combined-axis variations:

| ID | Axis | Hypothesis in brief |
|----|------|---------------------|
| **V-01** | Output format — schema-first | Template up front → structural compliance (C-01, C-02, C-04 format) |
| **V-02** | Phrasing register — conversational/imperative | Step-by-step voice → better stage grouping (C-06) and natural gate prose (C-07) |
| **V-03** | Lifecycle emphasis — phase-first | Name the arc before writing YAML → strategic pacing (C-09) and descriptive names (C-08) |
| **V-04** | Role sequence + quantified gates | "Who acts?" then "what count?" → artifact-specific (C-07) and quantified gates (C-10) |
| **V-05** | Inertia contrast + evidence arc strategy | Design against the naive baseline → non-trivial gates (C-04, C-07) and argued strategy (C-09) |

**Key design decisions:**

- **C-02 (echo contract)** is addressed in all five — each variation names the echo constraint explicitly and differently (rule statement in V-01, step 5 in V-02, arc phase in V-03, actor-phase final entry in V-04, named terminal stage in V-05). The variation tests which framing most reliably triggers correct echo structure.

- **C-07 (gates reference artifacts)** is the hardest recommended — V-01 shows a concrete example gate inline, V-04 names artifact types in the instruction itself, V-05 frames every gate as an "argument" that must name artifacts. The three approaches represent distinct pressure points on the same criterion.

- **V-05's inertia framing** is the most aggressive variation — it names the competitor explicitly ("unsequenced skill execution") and requires the plan to include a post-YAML strategy statement. This tests whether external pressure produces better-argued gates or over-verbose output.
YAML:
1. List each stage name and the gate condition in a summary table.
2. Flag any skills not selected and why they were excluded.
3. Confirm the echo contract is satisfied.

Save to `simulations/program/plans/{topic}-plan-{date}.md`.

---

## V-02 — Conversational/Imperative

**Axis**: Phrasing register (natural step-by-step voice vs formal specification)
**Hypothesis**: A step-by-step imperative register reduces cognitive distance and produces
better stage grouping cohesion (C-06) and more natural, traceable gate prose (C-07).

---

You are building a program plan -- a staged sequence of Signal skills that a team runs in
order to gather evidence for a feature decision. The plan is not an executor; it is a
strategic blueprint.

Here is what to do, in order:

**Step 1 -- Understand the topic.** Ask the user for the topic slug and one sentence
describing what question this feature investigation is trying to answer. Read
`simulations/TOPICS.md` and any existing signal artifacts for that topic.

**Step 2 -- Choose the skills.** From the Signal catalog (scout, draft, review, flow, trace,
prove, listen, metrics, goals, topic namespaces), select the skills relevant to this topic.
Not every skill is needed for every topic -- pick based on what the topic needs to answer.

**Step 3 -- Group into phases.** Organize the chosen skills into 3-6 named stages that
represent coherent phases of work. A good stage does one kind of thing: discovering the
landscape, validating the design, stress-testing the system, proving the hypothesis. Give
each stage a name that communicates its intent (e.g., `discovery`, `design-validation`,
`evidence-gathering`, `synthesis`).

**Step 4 -- Write the gates.** For each stage, write a gate condition: what artifacts or
signals must exist before the team advances to the next stage? Reference specific artifact
types by name. At least one gate should specify a minimum count (e.g., `">=2 scout artifacts
present"`). Empty, vague, or trivial gate strings ("done", "ready") are not acceptable.

**Step 5 -- Add the echo.** The final stage is always `echo` with `skills: []` and
`auto: true`. The echo fires after all human-driven stages complete. It is where the signal
that was not anticipated surfaces.

**Step 6 -- Write the YAML.** Produce `program.yaml` with topic, stages (name, skills, gate),
and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

Skill dependency order is enforced: scout before draft, draft before review/prove, review/prove
before listen and metrics. Violating this order means required artifacts do not exist when
later skills need them.

---

## V-03 — Phase-First

**Axis**: Lifecycle emphasis (evidence arc phases named and justified before YAML)
**Hypothesis**: Asking the model to reason about the evidence arc (breadth → depth →
synthesis) before writing YAML produces strategic pacing (C-09) and more descriptive stage
names (C-08). The plan reads like strategy, not a sorted skill list.

---

A program plan sequences Signal skills into an evidence arc: the team starts broad, narrows
to depth, then synthesizes into a decision. Every plan follows this arc. Name the arc phases
for this topic before writing any YAML.

**Phase 1 -- Breadth signals** (scout namespace): The team learns the landscape. What is
feasible, what exists, who cares, what the market looks like. No commitments yet.

**Phase 2 -- Design and draft** (draft namespace): The team authors what they plan to build,
anchored in the breadth signals. Gate: key scout artifacts must exist.

**Phase 3 -- Depth signals** (review, prove, flow, trace namespaces): The team stress-tests
the design and the system. Expert reviewers critique the spec. Hypothesis experiments run.
Process simulations walk the user journey. Gate: draft artifact must exist.

**Phase 4 -- Synthesis and measurement** (listen, metrics, goals, topic namespaces): The
team looks at the full signal set and draws conclusions. What does the evidence say? What
will customers say when it ships? Gate: at least one depth signal from Phase 3.

**Phase 5 -- Echo** (auto, no skills): The unexpected finding -- what the signals revealed
that was not in the original plan. Always present, always last.

Instructions:
1. For this topic, decide which Signal namespaces and skills are relevant (not all are
   required for every topic). Valid namespaces: scout, draft, review, flow, trace, prove,
   listen, metrics, goals, topic. No invented skill names.
2. Map selected skills to the arc phases above.
3. For phases with 0 selected skills, either remove that phase or explain the gap.
4. Write the gate for each phase -- reference the artifact types produced by the prior phase
   by name (e.g., `"scout-feasibility and scout-requirements artifacts present"`).
5. Produce `program.yaml` with the arc phases as stages plus echo as the final stage.
6. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

Dependency rule: skills can only be in a later phase than the artifacts they consume. A
review skill that reads a draft-spec cannot appear before the draft stage.

---

## V-04 — Role-Aware + Quantified Gates

**Axes**: Role sequence (who acts per stage) + quantified gates (signal count thresholds)
**Hypothesis**: Prompting "who acts here?" before "what must exist to proceed?" grounds the
planner in concrete workflow transitions and produces gates that are both artifact-specific
(C-07) and quantified with thresholds (C-10).

---

Signal assigns each namespace to a primary actor:
- `scout`: PM proves the idea
- `draft`: Architect/PM authors the design
- `review`, `prove`: Team validates, researchers investigate
- `flow`, `trace`: Domain dev and system dev simulate
- `listen`, `metrics`, `goals`: Team measures pre-ship
- `topic`: Anyone manages the narrative

A program plan sequences these actors in the order that makes evidence-building sense. You
do not schedule a review before there is something to review. You do not measure before there
is a design.

To build the plan:

1. **Read context.** Read `simulations/TOPICS.md` and any existing signal artifacts for the
   topic. Note what has already been produced -- do not re-plan completed stages.

2. **Assign actor order.** For this topic, list the actors in the sequence they should
   engage: PM first (scout), then Architect/PM (draft), then Team (review/prove), then
   Dev (flow/trace), then Team again (listen/metrics).

3. **Select skills per actor.** For each actor, choose the Signal skills relevant to this
   topic. Use only real skills from the catalog: scout (competitors, feasibility, naming,
   compliance, market, stakeholders, positioning, requirements), draft (spec, proposal, pitch),
   review (design, code, users, customers), flow (lifecycle, conversation, trigger, dataflow,
   integration, throttle, resilience), trace (request, state, contract, component, deployment,
   migration, permissions), prove (hypothesis, websearch, intelligence, prototype, analysis,
   interview, synthesize, publish), listen (feedback, support, adoption), metrics (nps, nsat,
   adoption, sla, dashboard), goals (okr, sla, commit, pr, msr, xr), topic (new, status,
   report, plan, story, echo).

4. **Write quantified gates.** For each non-echo stage, write a gate that:
   - Names the specific artifact types that must exist (e.g., `"scout-feasibility artifact"`).
   - Where possible, specifies a minimum count: `">=2 scout artifacts present"` or
     `"scout-spec artifact and draft-spec artifact both present"`.
   - Never uses vague terms: "done", "ready", "complete" are not valid gates.

5. **Produce the YAML.** Group actor-phases into 3-6 stages. The final stage is `echo` with
   `skills: []` and `auto: true`. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

6. **Summarize.** Show actor-to-stage mapping and flag any actor group that has no skills
   selected for this topic.

---

## V-05 — Inertia Contrast + Evidence Arc Strategy

**Axes**: Inertia framing (contrast against naive baseline) + evidence arc strategy
**Hypothesis**: Framing the plan against the naive baseline ("run all skills with no gates")
forces the model to justify every gate as a deliberate checkpoint, producing non-trivial gates
(C-04, C-07), strategic stage ordering (C-09), and a plan that reads as argued strategy.

---

The naive program plan is: run all skills at once, no gates, no order. That plan has a known
failure mode -- teams run later-stage skills (review, trace, prove) before earlier-stage
artifacts exist, so the review has nothing to evaluate, the trace has no spec to follow, and
the evidence gathering produces noise instead of signal.

Your job is to build the plan that defeats the naive approach. Every gate you write is an
argument for why the next stage cannot safely start until this signal exists.

**The competitor you are designing against is unsequenced skill execution.** Name this
explicitly in the plan header.

Instructions:

1. **Understand the topic.** Read `simulations/TOPICS.md` and existing signal artifacts.
   Identify what question this feature investigation must answer before the team can commit.

2. **Select relevant skills.** From the Signal catalog (scout, draft, review, flow, trace,
   prove, listen, metrics, goals, topic namespaces), select only the skills this topic
   needs. Not every skill applies to every topic. Do not invent skills not in the catalog.

3. **Build the evidence arc.** Lay out the causal chain: what signals must exist before the
   next type of work is productive? Start with breadth signals (scout), move to design
   (draft), then depth validation (review, prove, flow, trace), then synthesis and measurement
   (listen, metrics, goals, topic). Each transition in this arc is a gate.

4. **Write gates as arguments.** Each gate must state what signal or artifact must exist and
   why the next stage cannot start without it. Reference artifact types by name. At least one
   gate must specify a quantified threshold (e.g., `">=3 scout signals present and
   draft-spec artifact produced"`). A gate that says "done" or "ready" is not an argument --
   it is a placeholder; replace it.

5. **Group into named stages.** 3-6 stages, each with a name that communicates the arc phase
   intent (e.g., `landscape`, `architecture`, `validation`, `evidence`, `synthesis`). Not
   generic names (`stage1`, `phase2`). Not skill names reused as stage names.

6. **Add the echo.** The final stage is always `echo` with `skills: []` and `auto: true`.
   The echo is where the unexpected signals surface after all deliberate stages complete.

7. **Produce the YAML.** Write valid `program.yaml` with topic, stages (name, skills, gate),
   and the echo final stage. Save to `simulations/program/plans/{topic}-plan-{date}.md`.

8. **State the strategy.** Below the YAML, write 2-3 sentences explaining the evidence arc
   strategy: what the plan prioritizes early, what it defers, and what the gates are
   protecting against.

Dependency enforcement: scout before draft, draft before review/prove, review/prove before
listen and metrics. This is not optional -- it is what makes the gates meaningful.
