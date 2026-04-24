---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 1
rubric: v1
---

# Variations -- program-plan (Round 1)

Five complete prompt body variations for `/program:plan`.
Each is a standalone, runnable skill body -- not a diff.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## V-01 -- Role Sequence axis

**Axis**: Role sequence -- map skills to roles before ordering stages
**Hypothesis**: Framing the plan around *who does what* (PM, Architect, Dev, Lead) before
namespace order produces more coherent phase groupings and prevents treating program-plan
as a topological sort exercise. Role-based grouping surfaces natural handoff gates
(C-04, C-06) because gates become "what the next role needs to start" rather than
"what was done."

---

### Prompt body

You are running `/program:plan` for the topic: **{{topic}}**.

Produce `{{topic}}-program-{{date}}.md` -- a `program.yaml` that stages Signal plugin
skills into phases with gates. This is a plan. It does not run skills; it declares what
evidence must exist before each phase can begin.

**Step 1 -- Map skills to roles**

Signal skills are organized by audience. Before sequencing, identify which roles are
active for this topic and which skills they own:

| Role | Skills |
|------|--------|
| PM | `scout:competitors`, `scout:feasibility`, `scout:naming`, `scout:compliance`, `scout:market`, `scout:stakeholders`, `scout:positioning`, `draft:pitch`, `draft:brainstorm`, `topic:*` |
| Architect | `scout:requirements`, `draft:spec`, `draft:proposal`, `prove:hypothesis`, `prove:analysis`, `prove:synthesize` |
| Domain dev | `flow:lifecycle`, `flow:conversation`, `flow:trigger`, `flow:dataflow`, `flow:integration`, `flow:throttle`, `flow:resilience` |
| System dev | `trace:request`, `trace:state`, `trace:contract`, `trace:component`, `trace:deployment`, `trace:migration`, `trace:permissions` |
| Team | `review:design`, `review:code`, `review:users`, `review:customers`, `listen:feedback`, `listen:support`, `listen:adoption` |
| Lead | `program:plan` (you are here) |

Select only the skills relevant to {{topic}}. Not every topic needs every role active.

**Step 2 -- Group by phase**

Organize the selected skills into 3--6 stages that reflect natural role handoffs:

1. **Discovery** -- PM runs scout skills to establish what is known and what is being built.
2. **Design** -- Architect commits to the approach: spec, proposal, and any open research.
3. **Expert review** -- Team validates the spec before simulation begins.
4. **Simulation** -- Devs run flow and trace skills to stress-test on paper.
5. **Feedback preview** -- Team runs listen skills to simulate post-ship reality.

Merge or skip phases based on {{topic}} scope. Each phase becomes a YAML stage.

**Step 3 -- Write gates**

Each stage (except echo) needs a `gate` field. A gate is a state of evidence, not a
state of execution.

- WRONG: `"all scout skills complete"` -- execution state
- RIGHT: `"scout-feasibility and scout-requirements artifacts present"` -- evidence state
- BETTER: `">=2 scout signals present and no blocking feasibility concerns"` -- quantified

At least one gate must contain a numeric threshold (>=, <=, or an explicit count).

The gate for the last stage before a new role takes over reads like a handoff memo: what
evidence does the next role need before they can start?

**Step 4 -- Add echo**

The final stage is always `echo`. Echo is not a skill stage. It is a reflection moment
that asks what was learned unexpectedly across all prior stages.

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn that we didn't expect?"
```

Echo: no skills, always last, `auto: true` required.

**Output format**

```yaml
# {{topic}}-program-{{date}}.md
# This program is a plan, not an executor. Every skill remains independently runnable.
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:
    - name: <phase-label>        # human-readable, not "scout" or "stage1"
      skills:
        - namespace:skill        # only real Signal skills
      # Gate rationale: what does the next phase owner need to assume is true?
      gate: "<artifact-referencing condition>"
    # ... additional stages ...
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

Write the complete YAML. Include a one-line gate rationale comment above each `gate` field.

---

## V-02 -- Output Format axis

**Axis**: Output format -- annotated YAML skeleton with inline REQUIRED/EXAMPLE/BAD markers
**Hypothesis**: Providing a filled skeleton with `# REQUIRED`, `# EXAMPLE`, and `# BAD` inline
comments produces tighter adherence to C-01 (valid YAML), C-02 (echo contract), and C-04
(evidence-state gates) than prose instructions alone. The model fills in a structure rather
than inventing one, and BAD examples make the failure modes concrete at the point of authoring.

---

### Prompt body

You are running `/program:plan` for the topic: **{{topic}}**.

Produce `{{topic}}-program-{{date}}.md` by filling in the template below. Replace all
`<...>` placeholders. Preserve all `# REQUIRED` comments in the output.

```yaml
# Signal program plan
# Topic: {{topic}}
# This program is a plan, not an executor. Skills remain independently runnable.

program:                             # REQUIRED: top-level key must be "program"
  topic: "<topic name>"              # REQUIRED
  strategy: "<one-sentence goal>"    # REQUIRED: what decision does this program inform?

  stages:

    # ---- Stage 1: Discovery ----
    - name: "<phase label>"          # REQUIRED: descriptive label, not "stage1" or "scout"
      skills:                        # REQUIRED: select from Signal catalog
        - scout:<skill>              #   scout options: competitors, feasibility, naming,
        - scout:<skill>              #   compliance, market, stakeholders, positioning, requirements
      gate: "<condition>"            # REQUIRED: names artifact types, NOT execution state
                                     # EXAMPLE: "scout-feasibility and scout-requirements
                                     #           artifacts present; no blocking concerns"
                                     # BAD:     "scout complete" / "all done" / "proceed"

    # ---- Stage 2: Design ----
    - name: "<phase label>"
      skills:
        - draft:<skill>              #   draft options: spec, proposal, pitch, brainstorm
      gate: "<condition>"
                                     # HINT: at least ONE gate in the plan must be quantified
                                     # EXAMPLE: ">=2 scout signals and draft-spec artifact present"
                                     # BAD:     "design done"

    # ---- Stage 3: Validation ----
    - name: "<phase label>"
      skills:
        - review:<skill>             #   review options: design, code, users, customers
      gate: "<condition>"
                                     # DEPENDENCY RULE: review stages must follow a draft stage
                                     # Do NOT place review skills before draft:spec exists

    # ---- Stage 4+: Simulation / Prove / Feedback ----
    # Add stages as needed. Valid namespaces in dependency order:
    #   scout -> draft -> review/prove -> flow/trace -> listen -> topic
    #
    # flow options: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
    # trace options: request, state, contract, component, deployment, migration, permissions
    # prove options: hypothesis, websearch, intelligence, prototype, analysis, interview,
    #                synthesize, publish, topic, program
    # listen options: feedback, support, adoption
    # topic options: new, status, report, plan, story, echo

    # ---- FINAL STAGE: Echo ---- REQUIRED: must be last, exactly as shown ----
    - name: echo                     # REQUIRED: must be "echo" exactly
      skills: []                     # REQUIRED: empty list -- echo runs no skills
      auto: true                     # REQUIRED: must be present and true
      question: "What did we learn that we didn't expect?"
      # DO NOT add skills here. DO NOT move echo before other stages.
```

**Rules before submitting**:
1. Echo must be last. `skills: []`. `auto: true`. All three required.
2. Every non-echo gate must name artifact types or verifiable conditions. "Done" fails.
3. At least one gate must be quantified: `">=N signals"`, `"0 blocking findings"`.
4. All skill references must be real Signal skills: `namespace:skill`. No invented names.
5. Stage names are phase labels, not namespace names. "scout" fails; "discovery" passes.

Output only the completed YAML. Remove placeholder comments (# REQUIRED, # EXAMPLE, # BAD,
# HINT) before outputting. Keep structural comments (# this program is a plan...).

---

## V-03 -- Phrasing Register axis

**Axis**: Phrasing register -- question-framing turns each stage into an evidence question
**Hypothesis**: Framing each stage as "a question the team is trying to answer" produces
gates that naturally describe evidence state rather than execution state, because every
question has a built-in "how will we know we've answered it?" answer. This addresses
C-04 (evidence-state gates) and C-09 (deliberate evidence arc) by making the structure
feel like an investigation rather than a checklist.

---

### Prompt body

You are running `/program:plan` for topic **{{topic}}**.

A program plan sequences Signal plugin skills into stages. Think of each stage as a
question the team is trying to answer. The gate is your answer to: *"how will we know
we've answered it?"*

**What questions does this topic need to answer?**

Pick the questions that apply to {{topic}} and {{strategy}}. Each question maps to one
or more Signal skills.

**Discovery questions** (scout namespace)
- "Is this technically feasible?" -> `scout:feasibility`
- "Who else is doing this?" -> `scout:competitors`
- "What do stakeholders actually need?" -> `scout:requirements`, `scout:stakeholders`
- "What is the market context?" -> `scout:market`, `scout:positioning`
- "What should we call it?" -> `scout:naming`
- "Are there compliance constraints?" -> `scout:compliance`

**Design questions** (draft namespace)
- "What exactly are we building?" -> `draft:spec`
- "Which approach should we take?" -> `draft:proposal`
- "How do we tell this story?" -> `draft:pitch`
- "What are the ideas we haven't considered?" -> `draft:brainstorm`

**Validation questions** (review namespace)
- "Does the design hold up under expert review?" -> `review:design`
- "Will real users understand it?" -> `review:users`
- "Will customers pay for it?" -> `review:customers`
- "Is the code sound?" -> `review:code`

**Simulation questions** (flow + trace namespaces)
- "Does the business process work end-to-end?" -> `flow:lifecycle`, `flow:conversation`
- "What happens when things go wrong?" -> `flow:resilience`, `flow:throttle`
- "What triggers this feature and what does it produce?" -> `flow:trigger`, `flow:dataflow`
- "What does the system actually do?" -> `trace:request`, `trace:state`, `trace:contract`
- "Will this survive deployment and migration?" -> `trace:deployment`, `trace:migration`
- "Who can do what?" -> `trace:permissions`

**Research questions** (prove namespace)
- "We believe X -- but do we?" -> `prove:hypothesis`, `prove:analysis`, `prove:synthesize`
- "What does the field already know?" -> `prove:websearch`, `prove:intelligence`
- "What do real users say?" -> `prove:interview`

**Feedback questions** (listen namespace)
- "What will customers say after we ship?" -> `listen:feedback`
- "What will support look like?" -> `listen:support`
- "Will people actually adopt it?" -> `listen:adoption`

**Assembling the plan**

1. Select the questions relevant to {{topic}}.
2. Group related questions into 3--6 stages. Each stage is a cluster of questions the
   team works together before hitting a gate.
3. Write a gate for each stage that answers: *"what evidence tells us this question is
   answered?"* Name the artifact types that must exist.
   - "scout-feasibility artifact present and no blocking feasibility concerns" PASS
   - "draft-spec written and no P0 findings from review:design" PASS
   - "stage complete" FAIL -- this tells us nothing about whether the question is answered
4. Make at least one gate quantified: `">=2 scout signals present"` or
   `"draft-spec and >=3 review findings resolved"`.
5. Name each stage after the question cluster it answers: "feasibility", "design-commit",
   "expert-validation", "domain-simulation".
6. Keep questions in order: discovery before design, design before review, review before
   simulation, simulation before feedback.

**The echo**

The last stage is always `echo`. It is not a question. It is a listening moment: after
all questions are answered, you ask *"what did we learn that we didn't expect?"*

```yaml
- name: echo
  skills: []
  auto: true
  question: "What did we learn that we didn't expect?"
```

Echo has no skills. Echo is automatic. Echo is always last.

**Output**

Produce valid YAML. Top-level key: `program`. Include: `topic`, `strategy`, `stages`.
Each stage: `name`, `skills` (list), `gate` (string, evidence state). Echo stage:
`name: echo`, `skills: []`, `auto: true`.

Add a YAML comment above each gate: the question the gate answers.

---

## V-04 -- Combined: Role Sequence + Lifecycle Emphasis

**Axis**: Role sequence x lifecycle emphasis -- four named lifecycle bands with explicit
role-handoff boundaries
**Hypothesis**: Naming the four lifecycle bands (Prove It / Design It / Simulate It /
Listen Ahead) and making role-handoff moments explicit produces both better stage grouping
(C-06) and a more deliberate evidence arc (C-09), because the model reasons about *why*
phases transition rather than just sorting by namespace. Band-boundary gates become
handoff contracts between roles, naturally producing artifact-referencing language (C-04).

---

### Prompt body

You are running `/program:plan` for topic **{{topic}}** with strategy **{{strategy}}**.

A Signal program plan stages the team's evidence-gathering work into phases with explicit
role handoffs. This is a plan, not an executor: the program declares what evidence must
exist before each phase can begin. Every skill remains independently runnable.

**The four lifecycle bands**

Signal's 9 namespaces map onto four lifecycle bands. Build your plan across these bands.

```
Band 1: PROVE IT (PM + Architect)
  Purpose: Is this worth building? Is it feasible?
  Namespaces: scout, draft, prove
  Handoff signal: "we know what we're building and why"

Band 2: DESIGN IT (Architect + Team)
  Purpose: Have we written it down and had it reviewed?
  Namespaces: draft (final), review
  Handoff signal: "spec exists and no blocking review findings remain"

Band 3: SIMULATE IT (Dev)
  Purpose: Does it work on paper before we build it?
  Namespaces: flow, trace
  Handoff signal: "all simulated paths pass; no P0 gaps identified"

Band 4: LISTEN AHEAD (Team + PM)
  Purpose: What will the world say after we ship?
  Namespaces: listen, topic
  Handoff signal: "no critical adoption blockers; topic narrative is complete"
```

**Available skills per band**

Band 1:
- `scout:competitors`, `scout:feasibility`, `scout:naming`, `scout:compliance`,
  `scout:market`, `scout:stakeholders`, `scout:positioning`, `scout:requirements`
- `draft:spec`, `draft:proposal`, `draft:pitch`, `draft:brainstorm`
- `prove:hypothesis`, `prove:websearch`, `prove:intelligence`, `prove:prototype`,
  `prove:analysis`, `prove:interview`, `prove:synthesize`, `prove:publish`

Band 2:
- `draft:spec` (if not finalized in Band 1)
- `review:design`, `review:users`, `review:customers`

Band 3:
- `flow:lifecycle`, `flow:conversation`, `flow:trigger`, `flow:dataflow`,
  `flow:integration`, `flow:throttle`, `flow:resilience`
- `trace:request`, `trace:state`, `trace:contract`, `trace:component`,
  `trace:deployment`, `trace:migration`, `trace:permissions`

Band 4:
- `listen:feedback`, `listen:support`, `listen:adoption`
- `review:code`, `topic:status`, `topic:report`

**Instructions**

1. **Select skills per band** for {{topic}}. Not every topic needs all four bands. A small
   feature might skip Band 3. A research initiative might expand Band 1.

2. **Within each band, create 1--3 stages**. A band with 6 skills might split into
   "market-research" and "feasibility". A band with 2 skills needs one stage.

3. **Write band-boundary gates as handoff memos**: what evidence does the next role's
   first stage require before it can start?
   - "scout-requirements and scout-feasibility artifacts present; Architect ready to draft"
   - "draft-spec reviewed; no P0 findings from review:design or review:users"
   - ">=3 flow simulations pass; trace:request contract documented"
   Make at least one gate quantified.

4. **Stage names reflect band + purpose**:
   - Band 1: "market-research", "feasibility", "hypothesis-investigation"
   - Band 2: "design-commit", "expert-review"
   - Band 3: "domain-simulation", "system-trace"
   - Band 4: "feedback-preview", "adoption-readiness"

**Echo (mandatory final stage)**

After all bands, the program closes with echo. This is not a band. It is a reflection.

```yaml
- name: echo
  skills: []        # no skills -- required empty
  auto: true        # required field
  question: "What did we learn that we didn't expect?"
```

Echo must be last. `skills: []` and `auto: true` are hard requirements.

**Output format**

```yaml
# This program is a plan, not an executor. Skills remain independently runnable.
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:
    # Band 1: Prove It
    - name: <label>
      skills: [...]
      gate: "<handoff condition>"
    # Band 2: Design It
    - name: <label>
      skills: [...]
      gate: "<handoff condition>"
    # Band 3: Simulate It
    - name: <label>
      skills: [...]
      gate: "<handoff condition>"
    # Band 4: Listen Ahead
    - name: <label>
      skills: [...]
      gate: "<handoff condition>"
    # Echo
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

Keep band-separator comments (`# Band N: <name>`) before the first stage of each band.

---

## V-05 -- Combined: Output Format + Inertia Framing

**Axis**: Output format x inertia framing -- contrast ad-hoc run vs gated plan
**Hypothesis**: Showing what the plan looks like *without* gates (the inertia case: all
skills in one stage, execution-state gates) before showing the gated template makes the
model reason about *what the gate buys*, producing more specific artifact-referencing
gates (C-04, C-07) and at least one quantified gate (C-08). The contrast makes the
failure mode concrete at the moment of authoring.

---

### Prompt body

You are running `/program:plan` for topic **{{topic}}**.

**What this skill produces -- and what it avoids**

Without a program plan, teams run Signal skills ad hoc: `scout:feasibility` runs,
then `draft:spec` starts before feasibility is confirmed, then `review:design` happens
before the spec is stable. Skills run. Artifacts accumulate. Nobody knows if the
evidence is good enough to advance.

A program plan imposes gates. A gate is a checkpoint: *"before moving to the next stage,
this evidence must exist."* Gates do not run skills. They name what must be true.
The plan is a contract between phases, not a pipeline executor.

**The inertia pattern** (what you are replacing):

```yaml
# BAD: ad-hoc run -- no gates, no phases, no handoff contract
program:
  topic: "example-topic"
  strategy: "ship the feature"
  stages:
    - name: all-skills
      skills:
        - scout:feasibility
        - draft:spec
        - review:design
        - flow:lifecycle
        - listen:feedback
      gate: "all done"   # <-- meaningless: when is "done" done? who checks?
    - name: echo
      skills: []
      auto: true
```

The above plan will never catch a team advancing to `review:design` before `draft:spec`
is stable. A gate of `"all done"` is inertia captured in YAML.

**The gated plan pattern** (what you are building):

```yaml
# GOOD: gated plan -- phases with artifact-referencing gates
program:
  topic: "example-topic"
  strategy: "validate feasibility before committing to design"
  stages:
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      # Gate: names the artifacts that must exist before design begins
      gate: "scout-feasibility, scout-requirements, and scout-competitors artifacts
             present; no blocking feasibility concerns identified"

    - name: design-commit
      skills:
        - draft:spec
        - draft:proposal
      # Gate: references a specific artifact and a quantified condition
      gate: "draft-spec artifact present; >=2 design options documented in draft:proposal;
             Architect has signed off on approach"

    - name: expert-review
      skills:
        - review:design
        - review:users
      # Gate: quantified -- machine-checkable in principle
      gate: "0 P0 findings open from review:design and review:users;
             all blocking comments resolved in draft-spec"

    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

**Now build the plan for {{topic}}**

Use the template below. Every `<...>` is required.

Valid Signal skill names by namespace:
- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch, brainstorm
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish, topic, program
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

Namespace dependency order: `scout -> draft -> review/prove -> flow/trace -> listen -> topic`
A stage with `review:design` cannot appear before a stage with `draft:spec`.

```yaml
# This program is a plan, not an executor. Skills remain independently runnable.
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"

  stages:

    # Stage 1 -- Discovery / Market / Research
    - name: "<phase-label>"          # descriptive, not "stage1" or "scout"
      skills:
        - <namespace>:<skill>        # select from Signal catalog above
      # Why this gate: what must the NEXT stage owner be able to assume is true?
      gate: "<artifact-condition>"   # name artifacts, NOT "skills complete"

    # Stage 2 -- Design
    - name: "<phase-label>"
      skills:
        - <namespace>:<skill>
      gate: "<artifact-condition>"

    # Stage 3--N -- Validation / Simulation / Prove / Feedback
    # (add or remove stages for {{topic}} scope)

    # FINAL STAGE -- required, must be last, must be exactly as shown
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

**Gate checklist** (verify before submitting):
- [ ] Every non-echo gate names at least one artifact type (`scout-feasibility`, `draft-spec`,
      `review-design findings`)
- [ ] No gate uses execution language: `"done"`, `"complete"`, `"proceed"`, `"all passed"`
- [ ] At least one gate is quantified: `">=2 scout signals"`, `"0 P0 findings open"`
- [ ] Echo is last, has `skills: []`, has `auto: true`
- [ ] No invented skill names -- all from the Signal catalog above

Output the completed YAML only. Do not include the gate checklist in the output.
