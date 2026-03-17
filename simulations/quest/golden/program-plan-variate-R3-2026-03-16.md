---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 3
rubric: v3
aspirational_target: C-13, C-14, C-15
---

# program-plan -- R3 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v3 (C-01 through C-15, 15 criteria, 130 pts max, golden = all essential pass AND composite >= 80).

---

## R2 Retrospective Under v3 Rubric

Three new aspirational criteria (C-13, C-14, C-15) were extracted from R2 excellence signals.
Retroactively scoring R2 top variations against v3:

| Variation | C-13 arc-spine | C-14 deletion-resist | C-15 plan-level YAML error | v3 composite |
|-----------|---------------|---------------------|---------------------------|--------------|
| V-01 (role seq) | PARTIAL -- arc in stage names but prompt is numbered steps | PARTIAL -- echo # REQUIRED but other slots bare | FAIL -- no plan-level error block | ~88 |
| V-02 (annotated template) | PARTIAL -- arc in template comments, prompt is flat | PASS -- echo annotated with DO NOT ADD/DO NOT MOVE | FAIL -- no plan-level error block | ~93 |
| V-03 (question bank) | PARTIAL -- arc visible in question bank groups, prompt still numbered | PARTIAL -- echo present but no annotations | FAIL -- no plan-level error block | ~88 |
| V-04 (lifecycle bands) | PASS -- bands ARE the prompt structure; stripping prose leaves arc | PASS -- echo # REQUIRED in template | PASS -- # BAD: flat plan block present | ~118 |
| V-05 (inertia + template) | PARTIAL -- arc in layer comments only | PARTIAL -- echo annotated, other slots unannotated | FAIL -- inline # BAD gate comments, no full block | ~95 |

**R2 V-04 retroactively scores highest under v3.** The lifecycle bands were the primary
organizational axis (C-13), echo was annotated (partial C-14), and the `# BAD: flat plan`
block was present (C-15). Gap: C-14 was partial (only echo annotated; gate/name/skills slots
were bare).

**R3 target**: all five variations achieve C-13, C-14, C-15 simultaneously. Three new axes
are isolated in V-01/V-02/V-03 before combining in V-04 and V-05.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Arc-as-spine | Arc zones as first-class section headers (not just YAML comments) | Does making the arc the document's table-of-contents satisfy C-13 without sacrificing other criteria? |
| Full deletion-resistance | Every structural slot carries explicit annotation naming what it is and prohibiting the violation | Does annotating all slots (not just echo) achieve C-14 PASS without bloating the prompt? |
| Plan-level YAML error block | Complete multi-stage wrong-plan YAML as a standalone labeled block | Does a richer bad-plan block (more fields, more failure modes) improve C-15 and help C-12 full pass? |
| Arc-spine + deletion-resistance | Arc as section headers AND all slots annotated | Can C-13 + C-14 coexist without conflicting annotations? |
| Golden synthesis | All three new axes combined plus R2 V-04 band structure | Does the combined approach saturate all 15 criteria? |

Single-axis: V-01 (arc-as-spine), V-02 (full deletion-resistance), V-03 (plan-level YAML error block)
Combined: V-04 (arc-spine + deletion-resistance), V-05 (all three new axes, golden)

---

## V-01 -- Arc-as-Spine (single-axis)

**Axis**: Arc-as-spine -- the evidence arc is the document's primary structural backbone
**Hypothesis**: Using the five arc zones as top-level section headers makes the arc
navigable as structure (C-13). If all prose is stripped and only headers + YAML skeleton
remain, the arc is still visible: Discovery -> Design -> Validation -> Simulation -> Synthesis
-> Echo. Each section header is an arc layer; skill catalogs and gate guidance are nested
inside their zone. The YAML template uses the same arc-zone dividers as first-class comments.
C-14 is expected PARTIAL (echo is annotated but other slots are bare); C-15 is absent
(no plan-level YAML error block).

Expected gains: C-13 PASS (arc is structural backbone). C-14 PARTIAL.
Expected gaps: C-15 FAIL, C-12 PARTIAL (C-01 still single-anchor).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence zones, each gated on what the next zone needs.
No skill runs automatically. Every skill in the plan remains independently runnable.
The value is the gate: a team agreement on what evidence must exist before advancing.

---

You are running `/program:plan` for topic **{{topic}}** with strategy **{{strategy}}**.

Produce `{{topic}}-program-{{date}}.md`. The program is organized into five evidence arc zones.
Select only the zones and skills relevant to {{topic}}. Every zone is optional except echo.
The arc order is fixed: earlier zones produce artifacts that later zones require.

---

## ZONE 1 -- DISCOVERY: Is this worth pursuing?

**Purpose**: Gather external signal before committing design resources. Feasibility,
market, competitors, stakeholders, requirements. PM and Architect own this zone.

**Available skills:**
- `scout:feasibility` -- is it technically and commercially achievable?
- `scout:competitors` -- who else is doing this and how are we differentiated?
- `scout:market` -- what is the market context and opportunity size?
- `scout:stakeholders` -- who has a stake and what do they need?
- `scout:requirements` -- what must the feature do to succeed?
- `scout:positioning` -- how does this fit our narrative?
- `scout:naming` -- what should it be called?
- `scout:compliance` -- are there regulatory constraints?
- `prove:websearch` -- what does the field already know?
- `prove:intelligence` -- competitive intelligence and landscape scan

**Gate guidance**: Zone 1 gate = the evidence that makes zone 2 design safe to start.
Name artifacts. Do not describe what was run.
- PASS: `"scout-feasibility and scout-requirements artifacts present; no blocking concerns identified"`
- PASS: `">=2 scout signals archived; market context and stakeholder needs documented"`
- FAIL: `"discovery done"` -- execution state; names no evidence

---

## ZONE 2 -- DESIGN: What exactly are we building?

**Purpose**: Convert discovery signal into a committed design. Spec, proposal, brainstorm.
Architect owns this zone. Requires zone 1 artifacts.

**Available skills:**
- `draft:spec` -- full feature specification
- `draft:proposal` -- approach options and recommendation
- `draft:brainstorm` -- expand the solution space before committing
- `draft:pitch` -- stakeholder narrative
- `prove:hypothesis` -- validate a key design assumption
- `prove:analysis` -- analyze a design tradeoff quantitatively

**Gate guidance**: Zone 2 gate = the evidence that makes zone 3 review safe to start.
A draft:spec artifact must be present -- review cannot proceed without something to review.
- PASS: `"draft-spec artifact present; key design assumptions documented"`
- PASS: `"draft-spec and draft-proposal present; >=1 prove:hypothesis findings reviewed"`
- FAIL: `"design complete"` -- execution state

---

## ZONE 3 -- VALIDATION: Does it hold up under scrutiny?

**Purpose**: Expert and stakeholder review of the design. Find problems before simulation.
Team + Architect own this zone. Requires zone 2 draft:spec.

**Available skills:**
- `review:design` -- expert design review against requirements
- `review:users` -- user-perspective design walkthrough
- `review:customers` -- customer value and willingness-to-pay review
- `prove:interview` -- real user/customer interviews
- `prove:synthesize` -- synthesize multi-source evidence

**Gate guidance**: Zone 3 gate = the evidence that makes zone 4 simulation safe to start.
- PASS: `"review-design artifact present; 0 P0 findings open; draft-spec updated"`
- PASS: `">=2 review artifacts archived; all P0 findings resolved or accepted"`
- FAIL: `"reviewed"` -- execution state

---

## ZONE 4 -- SIMULATION: Does it work on paper?

**Purpose**: Simulate domain behavior and system contracts before implementation.
Dev owns this zone. Requires zone 3 review artifacts.

**Available skills:**
- `flow:lifecycle` -- end-to-end process simulation
- `flow:conversation` -- user-system dialog simulation
- `flow:trigger` -- event trigger and handler simulation
- `flow:dataflow` -- data transformation and routing simulation
- `flow:integration` -- external dependency integration simulation
- `flow:throttle` -- rate limiting and backpressure simulation
- `flow:resilience` -- failure mode and recovery simulation
- `trace:request` -- request-path trace
- `trace:state` -- state machine trace
- `trace:contract` -- API contract trace
- `trace:component` -- component dependency trace
- `trace:deployment` -- deployment sequence trace
- `trace:migration` -- data migration trace
- `trace:permissions` -- permission model trace

**Gate guidance**: Zone 4 gate = the evidence that makes zone 5 feedback safe to start.
- PASS: `">=2 flow simulations archived; trace:contract documented; no P0 simulation gaps"`
- PASS: `"flow:lifecycle and trace:contract artifacts present; all critical paths covered"`
- FAIL: `"simulation complete"` -- execution state

---

## ZONE 5 -- SYNTHESIS: What will the world say?

**Purpose**: Pre-ship feedback modeling and narrative readiness. PM + Team own this zone.
Requires zone 4 simulation artifacts.

**Available skills:**
- `listen:feedback` -- model likely customer feedback after ship
- `listen:support` -- model support load and escalations
- `listen:adoption` -- model adoption curve and blockers
- `topic:status` -- generate current status summary
- `topic:report` -- generate evidence report
- `topic:story` -- generate the feature narrative

**Gate guidance**: Zone 5 gate = the evidence that the program surfaced everything it was
designed to surface. The synthesis zone often does not gate -- or its gate is qualitative.
- PASS: `"listen-feedback and listen-adoption artifacts present; no critical adoption blockers"`
- FAIL: `"listen done"` -- execution state

---

## ECHO -- Reflection (mandatory final stage)

**Purpose**: A listening moment after all zones are complete. Not a zone.
Echo runs no skills. It records what the team learned that it did not expect.

```yaml
- name: echo          # REQUIRED: must be "echo" exactly
  skills: []          # REQUIRED: empty list -- echo runs no skills
  auto: true          # REQUIRED: must be present and true
  question: "What did we learn that we didn't expect?"
```

Echo must be the last stage. `skills: []` and `auto: true` are non-negotiable.

---

**Output format**

Produce valid YAML with top-level key `program`. Include `topic`, `strategy`, `stages`.
Each non-echo stage: `name`, `skills` (list), `gate` (evidence-state string).

```yaml
# {{topic}}-program-{{date}}.md
# This program is a plan, not an executor -- every skill runs standalone
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # --- ZONE 1: DISCOVERY ---
    - name: <discovery-phase-label>
      skills:
        - scout:<skill>       # valid Zone 1 skills listed above
      gate: "<evidence condition naming artifact types or counts>"

    # --- ZONE 2: DESIGN ---
    - name: <design-phase-label>
      skills:
        - draft:<skill>       # valid Zone 2 skills listed above
      gate: "<evidence condition -- draft-spec must be present>"

    # --- ZONE 3: VALIDATION ---
    - name: <validation-phase-label>
      skills:
        - review:<skill>      # valid Zone 3 skills listed above
      gate: "<evidence condition -- artifact presence + finding count>"

    # --- ZONE 4: SIMULATION ---  (add/remove stages within this zone as needed)
    - name: <simulation-phase-label>
      skills:
        - flow:<skill>        # valid Zone 4 skills listed above
        - trace:<skill>
      gate: "<evidence condition -- simulation artifacts + no P0 gaps>"

    # --- ZONE 5: SYNTHESIS ---  (optional)
    - name: <synthesis-phase-label>
      skills:
        - listen:<skill>      # valid Zone 5 skills listed above
      gate: "<evidence condition>"

    # --- ECHO: Reflection -- REQUIRED: must be last ---
    - name: echo
      skills: []              # REQUIRED: empty
      auto: true              # REQUIRED: must be present
      question: "What did we learn that we didn't expect?"
```

---

## V-02 -- Full Deletion-Resistance (single-axis)

**Axis**: Full deletion-resistance -- every structural slot in the YAML template carries
explicit inline annotations naming what it is and prohibiting the specific violation
**Hypothesis**: R2 V-04 earned C-11 PASS and partial C-14 by annotating echo's slots.
Full C-14 requires annotating ALL structural slots -- not just echo -- with `# REQUIRED`
markers that name the prohibited action at the point of authoring. This makes every
required field a labeled constraint, not a convention. A model filling the template
encounters deletion friction at every field, not just at echo. C-13 is expected PARTIAL
(arc is visible in template zone comments but the prompt document itself is structured
as numbered steps). C-15 is absent.

Expected gains: C-14 PASS (all slots annotated). C-11 full PASS.
Expected gaps: C-13 PARTIAL, C-15 FAIL, C-12 PARTIAL (C-01 still single-anchor).

---

### Prompt body

You are running `/program:plan` for topic: **{{topic}}**.

Produce `{{topic}}-program-{{date}}.md` by completing the template below.
Replace all `<...>` placeholders. The program is a plan, not an executor -- every skill
in the plan remains independently runnable without it. The program exists to declare what
evidence must exist before each phase can begin.

**Signal skill catalog** (any name not in this table is invalid -- invented names fail):

| Namespace | Skills |
|-----------|--------|
| `scout` | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| `draft` | spec, proposal, pitch, brainstorm |
| `review` | design, code, users, customers |
| `flow` | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| `trace` | request, state, contract, component, deployment, migration, permissions |
| `prove` | hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish |
| `listen` | feedback, support, adoption |
| `topic` | new, status, report, plan, story, echo |

**Namespace dependency order** (stages must follow this sequence):
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
A stage with `review:design` before any `draft:spec` stage violates this order.
`flow:*` and `trace:*` require a prior `review:*` stage.

**Template** -- fill in all `<...>`; every `# REQUIRED` annotation must appear in output:

```yaml
# {{topic}}-program-{{date}}.md
# REQUIRED: preserve this comment -- program is a plan, not an executor; skills run standalone

program:               # REQUIRED: top-level key must be "program" -- DO NOT RENAME
  topic: "<topic>"     # REQUIRED: string -- the feature being planned
  strategy: "<goal>"   # REQUIRED: one sentence -- what decision does this evidence inform?
                       # REQUIRED: DO NOT omit strategy; a plan without a stated goal is not a plan

  stages:              # REQUIRED: list of stage objects -- DO NOT replace with prose

    # --- Layer 1: Breadth (scout / prove:websearch / prove:intelligence) ---
    - name: "<phase-label>"         # REQUIRED: phase-intent label -- DO NOT use namespace name ("scout")
                                    # REQUIRED: DO NOT use generic index ("stage1", "step-1")
      skills:                       # REQUIRED: list from catalog above -- DO NOT invent names
        - scout:<skill>             # valid: feasibility, competitors, market, stakeholders, requirements,
                                    #        positioning, naming, compliance
      gate: "<condition>"           # REQUIRED: names artifact types or signal counts
                                    # REQUIRED: DO NOT write "done", "complete", "all skills run"
                                    # EXAMPLE: "scout-feasibility artifact present; no blocking concerns"
                                    # BETTER:  ">=2 scout signals archived; no blocking concerns identified"

    # --- Layer 2: Focus (draft / prove) ---
    - name: "<phase-label>"         # REQUIRED: phase-intent label, not "draft"
      skills:
        - draft:<skill>             # valid: spec, proposal, pitch, brainstorm
      gate: "<condition>"           # REQUIRED: evidence state
                                    # DEPENDENCY: draft-spec must appear in or before this stage
                                    #             before any review:* stage can follow

    # --- Layer 3: Validation (review / prove) ---
    - name: "<phase-label>"         # REQUIRED: phase-intent label, not "review"
      skills:
        - review:<skill>            # valid: design, code, users, customers
      gate: "<condition>"           # REQUIRED: evidence state
                                    # EXAMPLE: "review-design artifact present; 0 P0 findings open"
                                    # HINT: include a count: ">=2 review artifacts; 0 P0 open"

    # --- Layer 4: Simulation (flow / trace) ---  add/remove stages as needed
    - name: "<phase-label>"         # REQUIRED: phase-intent label, not "flow" or "trace"
      skills:
        - flow:<skill>              # valid: lifecycle, conversation, trigger, dataflow,
                                    #        integration, throttle, resilience
        - trace:<skill>             # valid: request, state, contract, component,
                                    #        deployment, migration, permissions
      gate: "<condition>"           # REQUIRED: evidence state

    # --- Layer 5: Synthesis (listen / topic) ---  optional
    - name: "<phase-label>"         # REQUIRED: phase-intent label, not "listen" or "topic"
      skills:
        - listen:<skill>            # valid: feedback, support, adoption
      gate: "<condition>"           # REQUIRED: evidence state

    # ===========================================================================
    # ECHO -- REQUIRED: must be the LAST stage. DO NOT ADD stages after this.
    # ===========================================================================
    - name: echo                    # REQUIRED: must be "echo" exactly -- DO NOT RENAME
      skills: []                    # REQUIRED: empty list -- DO NOT ADD any skills here
      auto: true                    # REQUIRED: must be present and true -- DO NOT SET to false
      question: "What did we learn that we didn't expect?"
      # REQUIRED: DO NOT move echo before other stages
      # REQUIRED: DO NOT add a gate field to echo
```

**Rules checklist before submitting:**
1. Echo is last. `skills: []`. `auto: true`. All three fields present -- no exceptions.
2. Every non-echo gate names artifact types or signal counts. "Done" / "complete" / "proceed" fail.
3. At least one gate is quantified: `">=N signals"`, `"0 P0 findings"`, `">=3 artifacts"`.
4. All skills come from the catalog above. No invented names.
5. Stage names are phase-intent labels, not namespace names and not `stage1`/`step-N`.
6. Namespace dependency order respected: scout before draft, draft before review, review before flow/trace.

---

## V-03 -- Plan-Level YAML Error Block (single-axis)

**Axis**: Plan-level YAML error block -- a complete, multi-stage wrong-plan YAML labeled
as a bad plan (not just inline # BAD gate comments)
**Hypothesis**: C-15 requires a standalone full YAML block showing plan-level failure.
Inline `# BAD: "done"` comments target gate correctness (C-04) but do not provide a second
anchor for structural correctness (C-01). A complete BAD YAML plan block with multiple
wrong fields across multiple stages serves as the second anchor for C-01, enabling C-12
full PASS. This variation uses a richer bad-plan block than R2 V-04 (which had only one
stage in the bad block) -- the R3 version shows all four essential failure modes as a
complete parseable-but-wrong plan. C-13 is expected PARTIAL (arc visible in YAML template
dividers but prompt organized as rules + template). C-14 is PARTIAL (echo annotated only).

Expected gains: C-15 PASS, C-12 PASS (all four essential criteria dual-anchored via
bad-plan block + template). C-10 PASS.
Expected gaps: C-13 PARTIAL, C-14 PARTIAL.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

Every skill in the program remains independently runnable outside of it. The program exists
to declare what evidence must exist before each phase can begin -- not to run skills for you.

---

You are running `/program:plan` for topic **{{topic}}**.

Produce `{{topic}}-program-{{date}}.md` -- a `program.yaml` staging Signal skills into
a gated evidence plan.

**Signal skill catalog** (every skill reference must resolve to a name in this table):

| Namespace | Skills |
|-----------|--------|
| `scout` | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| `draft` | spec, proposal, pitch, brainstorm |
| `review` | design, code, users, customers |
| `flow` | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| `trace` | request, state, contract, component, deployment, migration, permissions |
| `prove` | hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish |
| `listen` | feedback, support, adoption |
| `topic` | new, status, report, plan, story, echo |

Any name not in this table is invalid. A single invented name (e.g., `scout:analysis`,
`build:deploy`) fails the entire plan.

---

**Study this wrong plan before authoring**

The following YAML plan is semantically invalid. It demonstrates all four essential
failure modes. Study each failure annotation. Do not reproduce any of these patterns.

```yaml
# ======================================================
# BAD PLAN -- fails C-01, C-02, C-03, C-04 simultaneously
# This is a complete wrong-plan example, not just bad gates.
# ======================================================
program:
  topic: "payment-api"
  # FAILURE: no strategy field -- the plan has no stated decision to inform

  stages:
    # FAILURE C-06 + C-04: namespace name as stage label + execution-state gate
    - name: scout                   # WRONG: "scout" is a namespace, not a phase intent
      skills:
        - scout:feasibility
        - scout:analysis            # WRONG C-03: invented skill -- "scout:analysis" does not exist
      gate: "done"                  # WRONG C-04: execution-state -- who can verify "done"?

    # FAILURE C-06 + C-04: generic index + execution-state gate
    - name: stage2                  # WRONG: generic index communicates nothing
      skills:
        - draft:spec
        - draft:outline             # WRONG C-03: invented skill -- "draft:outline" does not exist
      gate: "complete"              # WRONG C-04: "complete" names no evidence

    # FAILURE C-05: flow stage before any review stage
    - name: build-simulation        # Ordering violation: review not yet present
      skills:
        - flow:lifecycle
        - flow:trigger
      gate: "all tasks finished"    # WRONG C-04: execution-state gate

    # FAILURE C-02: echo with skills and wrong auto value
    - name: echo
      skills:
        - listen:feedback           # WRONG C-02: echo must have empty skills list
        - listen:support            # WRONG C-02: echo runs no skills
      auto: false                   # WRONG C-02: auto must be true
      # WRONG: no question field
# END OF BAD PLAN
```

**Every failure in the bad plan has a correct form:**

| Wrong | Correct |
|-------|---------|
| `name: scout` (namespace name) | `name: market-research` (phase intent) |
| `scout:analysis` (invented) | `scout:feasibility` or `scout:requirements` (from catalog) |
| `gate: "done"` (execution state) | `gate: "scout-feasibility artifact present; no blocking concerns"` |
| `gate: "complete"` (execution state) | `gate: "draft-spec present; >=2 scout signals reviewed"` |
| `flow:lifecycle` before any `review:*` | `flow:lifecycle` only after `review:design` stage exists |
| `echo` with skills listed | `echo` with `skills: []` |
| `auto: false` on echo | `auto: true` on echo |

---

**Instructions**

1. **Select skills** from the catalog above that apply to {{topic}} and {{strategy}}.

2. **Group into 3-6 stages**. Follow namespace dependency order:
   `scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo`
   - `review:*` requires a prior stage with `draft:spec`
   - `flow:*` and `trace:*` require a prior stage with `review:*` artifacts

3. **Name stages by phase intent** -- what the team is trying to learn or decide in
   this stage. `discovery`, `design-commit`, `expert-review`, `domain-simulation` are
   better than `scout`, `draft`, `stage1`.

4. **Write evidence-state gates** -- what artifacts must exist or what conditions must be
   verifiably true before the next stage can begin:
   - Name artifact types: `"scout-feasibility artifact present"`
   - Count signals: `">=2 scout signals archived; no blocking concerns"`
   - Name finding states: `"0 P0 findings open from review:design"`
   - At least one gate must include a numeric threshold (>=N, 0 open, count)

5. **Close with echo** -- the final stage, always, with empty skills and `auto: true`.

---

**Output template**

```yaml
# {{topic}}-program-{{date}}.md
# This program is a plan, not an executor -- every skill runs standalone
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # Layer 1: Breadth
    - name: <phase-label>
      skills:
        - namespace:skill         # from Signal catalog above -- no invented names
      gate: "<artifact-referencing condition>"

    # Layer 2: Focus  (add stages as needed)
    - name: <phase-label>
      skills:
        - namespace:skill
      gate: "<artifact-referencing condition>"

    # Layer 3: Validation
    - name: <phase-label>
      skills:
        - namespace:skill
      gate: "<artifact-referencing condition -- include >=N count>"

    # Layer 4: Simulation  (add/remove stages)
    - name: <phase-label>
      skills:
        - namespace:skill
      gate: "<artifact-referencing condition>"

    # Layer 5: Synthesis  (optional)
    - name: <phase-label>
      skills:
        - namespace:skill
      gate: "<artifact-referencing condition>"

    # REQUIRED: echo must be last
    - name: echo
      skills: []              # REQUIRED: empty
      auto: true              # REQUIRED: must be present and true
      question: "What did we learn that we didn't expect?"
      # REQUIRED: DO NOT add skills here. DO NOT move echo.
```

---

## V-04 -- Arc-as-Spine + Full Deletion-Resistance (combined)

**Axis**: Arc-as-spine x full deletion-resistance -- arc zones are top-level section headers
AND every structural slot carries deletion-resistance annotations
**Hypothesis**: C-13 requires the arc to be navigable as structure (not just described); C-14
requires every structural slot to be annotated. These are complementary -- if the arc IS the
section structure, arc-zone headers are also structural constraints, and deletion-resistance
annotations reinforce those headers. V-04 tests whether the two axes coexist without conflict.
C-15 is absent (no plan-level YAML error block) -- expected to give C-12 PARTIAL for C-01.
Both C-13 and C-14 expected to PASS independently.

Expected gains: C-13 PASS, C-14 PASS, C-11 full PASS.
Expected gaps: C-15 FAIL, C-12 PARTIAL.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It stages Signal skills into evidence zones, each gated on what the next zone needs to start.
Skills do not run automatically. Every skill in the plan remains independently runnable.
The program is a team alignment artifact -- a shared contract on what evidence must exist
before work can advance to the next zone.

---

You are running `/program:plan` for topic **{{topic}}** with strategy **{{strategy}}**.

Produce `{{topic}}-program-{{date}}.md`. The plan is organized into five evidence arc zones
in fixed sequence. Choose the zones and skills relevant to {{topic}}. Echo is mandatory.

---

# ZONE 1: DISCOVERY -- Is this worth pursuing?

**Arc position**: Breadth-first. Gathers external signal before committing design resources.
**Who owns it**: PM + Architect
**Namespace(s)**: `scout`, `prove:websearch`, `prove:intelligence`

**Available skills for Zone 1:**
- `scout:feasibility` -- technical and commercial viability
- `scout:competitors` -- competitive landscape and differentiation
- `scout:market` -- market context and size
- `scout:stakeholders` -- who has a stake and what they need
- `scout:requirements` -- what the feature must do
- `scout:positioning` -- narrative fit
- `scout:naming` -- naming options
- `scout:compliance` -- regulatory constraints
- `prove:websearch` -- prior art and field knowledge
- `prove:intelligence` -- competitive intelligence

**Gate requirement for Zone 1:**
```
# REQUIRED: gate must name artifact types or count signals -- DO NOT write "done" or "complete"
# REQUIRED: at least one gate across the entire plan must include a numeric threshold
# EXAMPLE:  "scout-feasibility and scout-requirements artifacts present; no blocking concerns"
# EXAMPLE:  ">=2 scout signals archived; market context documented"
```

---

# ZONE 2: DESIGN -- What exactly are we building?

**Arc position**: Focus. Converts discovery signal into committed design artifacts.
**Who owns it**: Architect
**Namespace(s)**: `draft`, `prove:hypothesis`, `prove:analysis`
**Dependency**: Requires Zone 1 artifacts before starting.

**Available skills for Zone 2:**
- `draft:spec` -- full feature specification (required for Zone 3 to follow)
- `draft:proposal` -- approach options and recommendation
- `draft:brainstorm` -- option expansion before commit
- `draft:pitch` -- stakeholder narrative
- `prove:hypothesis` -- validate a key design assumption
- `prove:analysis` -- quantitative design tradeoff analysis

**Gate requirement for Zone 2:**
```
# REQUIRED: draft-spec must appear in or before this zone's final stage
# REQUIRED: gate must confirm draft-spec artifact exists before Zone 3 can start
# EXAMPLE:  "draft-spec present; key design assumptions documented"
```

---

# ZONE 3: VALIDATION -- Does it hold up?

**Arc position**: Focused validation. Expert and stakeholder review of the design.
**Who owns it**: Team + Architect
**Namespace(s)**: `review`, `prove:interview`, `prove:synthesize`, `prove:prototype`
**Dependency**: Requires `draft:spec` artifact from Zone 2.

**Available skills for Zone 3:**
- `review:design` -- expert design review
- `review:users` -- user-perspective walkthrough
- `review:customers` -- customer value review
- `prove:interview` -- user/customer interviews
- `prove:synthesize` -- multi-source evidence synthesis
- `prove:prototype` -- prototype-based validation
- `prove:publish` -- publish findings

**Gate requirement for Zone 3:**
```
# REQUIRED: gate must reference review artifact presence and finding count
# REQUIRED: P0 findings must be resolved before Zone 4 can start
# EXAMPLE:  "review-design artifact present; 0 P0 findings open"
# EXAMPLE:  ">=2 review artifacts archived; all P0 findings resolved or accepted"
```

---

# ZONE 4: SIMULATION -- Does it work on paper?

**Arc position**: Depth. Domain behavior and system contract simulation.
**Who owns it**: Dev (Domain + System)
**Namespace(s)**: `flow`, `trace`
**Dependency**: Requires Zone 3 review artifacts.

**Available skills for Zone 4:**
- `flow:lifecycle`, `flow:conversation`, `flow:trigger`, `flow:dataflow`
- `flow:integration`, `flow:throttle`, `flow:resilience`
- `trace:request`, `trace:state`, `trace:contract`, `trace:component`
- `trace:deployment`, `trace:migration`, `trace:permissions`

**Gate requirement for Zone 4:**
```
# REQUIRED: gate must reference simulation artifact types and coverage
# EXAMPLE:  ">=2 flow simulations archived; trace:contract documented; no P0 simulation gaps"
# EXAMPLE:  "flow:lifecycle and trace:contract artifacts present; all critical paths covered"
```

---

# ZONE 5: SYNTHESIS -- What will the world say?

**Arc position**: Synthesis. Pre-ship feedback modeling and narrative readiness.
**Who owns it**: PM + Team
**Namespace(s)**: `listen`, `topic`
**Dependency**: Requires Zone 4 simulation artifacts. This zone is optional.

**Available skills for Zone 5:**
- `listen:feedback` -- model likely customer feedback after ship
- `listen:support` -- model support load and escalation patterns
- `listen:adoption` -- model adoption curve and blockers
- `topic:status` -- current status signal
- `topic:report` -- evidence report
- `topic:story` -- feature narrative

**Gate requirement for Zone 5:**
```
# REQUIRED if present: gate must reference feedback/adoption artifact presence
# EXAMPLE:  "listen-feedback artifact present; no critical adoption blockers identified"
```

---

# ECHO -- Reflection (mandatory final zone)

**Arc position**: Terminus. The program closes here. Echo is not a zone -- it is a
reflection moment after all zones complete. Echo runs no skills. It is always last.

```yaml
# REQUIRED: echo must be the final stage -- DO NOT ADD stages after this block
- name: echo                # REQUIRED: must be "echo" exactly -- DO NOT RENAME
  skills: []                # REQUIRED: empty list -- DO NOT ADD skills here
  auto: true                # REQUIRED: must be present and true -- DO NOT SET to false
  question: "What did we learn that we didn't expect?"
  # REQUIRED: DO NOT add a gate field to echo
```

---

**Output template**

Produce valid YAML with top-level key `program`. Keep all zone-separator comments.

```yaml
# {{topic}}-program-{{date}}.md
# REQUIRED: preserve -- this program is a plan, not an executor; skills run standalone
program:
  topic: "{{topic}}"         # REQUIRED: feature name -- DO NOT OMIT
  strategy: "{{strategy}}"   # REQUIRED: what decision does this plan inform -- DO NOT OMIT
  stages:

    # === ZONE 1: DISCOVERY ===
    - name: <discovery-phase-label>         # REQUIRED: phase intent, not "scout"
      skills:                               # REQUIRED: from Zone 1 catalog above
        - scout:<skill>
      gate: "<evidence condition>"          # REQUIRED: artifact types or counts, not "done"

    # === ZONE 2: DESIGN ===
    - name: <design-phase-label>            # REQUIRED: phase intent, not "draft"
      skills:                               # REQUIRED: from Zone 2 catalog above
        - draft:<skill>
      gate: "<evidence condition>"          # REQUIRED: draft-spec must be confirmed present

    # === ZONE 3: VALIDATION ===
    - name: <validation-phase-label>        # REQUIRED: phase intent, not "review"
      skills:                               # REQUIRED: from Zone 3 catalog above
        - review:<skill>
      gate: "<evidence condition>"          # REQUIRED: include finding count (0 P0 open)

    # === ZONE 4: SIMULATION ===  (add/remove stages within this zone)
    - name: <simulation-phase-label>        # REQUIRED: phase intent, not "flow" or "trace"
      skills:                               # REQUIRED: from Zone 4 catalog above
        - flow:<skill>
        - trace:<skill>
      gate: "<evidence condition>"          # REQUIRED: simulation artifact types + coverage

    # === ZONE 5: SYNTHESIS ===  (optional zone -- omit if not applicable)
    - name: <synthesis-phase-label>         # REQUIRED if present: phase intent, not "listen"
      skills:                               # REQUIRED: from Zone 5 catalog above
        - listen:<skill>
      gate: "<evidence condition>"          # REQUIRED: feedback/adoption artifact presence

    # === ECHO ===  REQUIRED: must be last -- DO NOT ADD stages after this
    - name: echo                            # REQUIRED: "echo" exactly -- DO NOT RENAME
      skills: []                            # REQUIRED: empty -- DO NOT ADD skills
      auto: true                            # REQUIRED: present and true -- DO NOT REMOVE
      question: "What did we learn that we didn't expect?"
```

---

## V-05 -- Golden Synthesis (all three new axes combined)

**Axis**: Arc-as-spine x full deletion-resistance x plan-level YAML error block
**Hypothesis**: All three new criteria can coexist in a single prompt. The arc-as-spine
organizes the document; per-zone deletion-resistance annotations reinforce each arc slot;
the plan-level YAML error block anchors C-01/C-04 at the wrong-plan level; and the YAML
template anchors C-01/C-02/C-03/C-04 at the correct-plan level. C-12 full PASS is possible
because all four essential criteria are dual-anchored (error block + template for C-01,
arc-zone echo slot + template annotations for C-02, zone catalogs + template comments for
C-03, zone gate guidance + error block gates for C-04). C-15 PASS because the wrong-plan
YAML block is complete with multiple stages and multiple failure modes.

Expected: C-13 PASS, C-14 PASS, C-15 PASS, C-12 full PASS. All 15 criteria targeted.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence zones, each gated on what the next zone needs.
No skill runs automatically. Every skill listed remains independently runnable.
The program is a decision-support artifact -- it tells the team what evidence must exist
before they can move forward, not what work to execute.

---

You are running `/program:plan` for topic **{{topic}}** with strategy **{{strategy}}**.

Produce `{{topic}}-program-{{date}}.md`.

**Before reading the instructions, study this wrong plan to understand what not to produce.**

---

# WRONG PLAN -- read before authoring

The following YAML plan is structurally and semantically invalid. It demonstrates all four
essential failure modes. Study each annotated failure. Every pattern here must be avoided.

```yaml
# =====================================================
# WRONG PLAN -- C-01 through C-04 all fail here
# Do not produce a plan that looks like this.
# =====================================================
program:
  topic: "notification-service"
  # FAIL: no strategy field -- the plan names no decision to inform

  stages:

    # FAIL C-06 + C-04: namespace label + execution-state gate
    - name: scout                     # WRONG: "scout" is a namespace, not a phase intent
      skills:
        - scout:feasibility
        - scout:competitive-review    # WRONG C-03: invented skill name
      gate: "done"                    # WRONG C-04: execution-state gate

    # FAIL C-04: execution-state gate
    - name: design
      skills:
        - draft:spec
        - draft:outline               # WRONG C-03: invented skill name
      gate: "complete"                # WRONG C-04: "complete" names no evidence

    # FAIL C-05: simulation before any review
    - name: simulate                  # C-05 violation: flow before review:*
      skills:
        - flow:lifecycle
        - trace:contract
      gate: "all tasks finished"      # WRONG C-04: execution-state gate

    # FAIL C-02: echo with skills and auto: false
    - name: echo
      skills:
        - listen:feedback             # WRONG C-02: echo must have empty skills
      auto: false                     # WRONG C-02: must be auto: true
# FAIL: no quantified gate anywhere in the plan
```

**Pattern map -- wrong to correct:**

| Failure | Wrong | Correct |
|---------|-------|---------|
| Stage naming | `name: scout` | `name: market-research` |
| Invented skill | `scout:competitive-review` | `scout:competitors` |
| Invented skill | `draft:outline` | `draft:spec` or `draft:brainstorm` |
| Execution gate | `gate: "done"` | `gate: "scout-feasibility artifact present"` |
| Execution gate | `gate: "complete"` | `gate: "draft-spec present; >=2 scout signals reviewed"` |
| Ordering | `flow:lifecycle` before review | `flow:lifecycle` only after `review:*` stage exists |
| Echo skills | `skills: [listen:feedback]` | `skills: []` |
| Echo auto | `auto: false` | `auto: true` |

---

# ZONE 1: DISCOVERY -- Is this worth pursuing?

**Arc position**: Breadth-first. Gathers external signal before committing design resources.
**Namespaces**: `scout`, `prove:websearch`, `prove:intelligence`

Available skills:
- `scout:feasibility`, `scout:competitors`, `scout:market`, `scout:stakeholders`
- `scout:requirements`, `scout:positioning`, `scout:naming`, `scout:compliance`
- `prove:websearch`, `prove:intelligence`

```
# REQUIRED: Zone 1 gate must name artifact types or count signals
# REQUIRED: DO NOT write "done", "complete", "finished", "all run"
# EXAMPLE:  "scout-feasibility artifact present; no blocking concerns identified"
# QUANTIFIED: ">=2 scout signals archived; market context documented"
```

---

# ZONE 2: DESIGN -- What are we building?

**Arc position**: Focus. Converts discovery into committed design artifacts.
**Namespaces**: `draft`, `prove:hypothesis`, `prove:analysis`
**Dependency**: Zone 1 artifacts must exist before this zone starts.

Available skills:
- `draft:spec` (required before Zone 3 can follow), `draft:proposal`, `draft:brainstorm`, `draft:pitch`
- `prove:hypothesis`, `prove:analysis`

```
# REQUIRED: Zone 2 gate must confirm draft-spec artifact is present
# REQUIRED: DO NOT start a review:* stage until draft-spec exists
# EXAMPLE:  "draft-spec present; key design assumptions documented"
```

---

# ZONE 3: VALIDATION -- Does it hold up?

**Arc position**: Focused validation. Expert and stakeholder review.
**Namespaces**: `review`, `prove:interview`, `prove:synthesize`, `prove:prototype`
**Dependency**: `draft:spec` from Zone 2 must be present.

Available skills:
- `review:design`, `review:users`, `review:customers`
- `prove:interview`, `prove:synthesize`, `prove:prototype`, `prove:publish`

```
# REQUIRED: Zone 3 gate must reference review artifact presence and finding count
# REQUIRED: 0 P0 findings must be the gate condition before Zone 4 can start
# EXAMPLE:  "review-design artifact present; 0 P0 findings open"
# QUANTIFIED: ">=2 review artifacts; all P0 findings resolved"
```

---

# ZONE 4: SIMULATION -- Does it work on paper?

**Arc position**: Depth. Domain behavior and system contract simulation.
**Namespaces**: `flow`, `trace`
**Dependency**: Zone 3 review artifacts must be present.

Available skills:
- `flow:lifecycle`, `flow:conversation`, `flow:trigger`, `flow:dataflow`
- `flow:integration`, `flow:throttle`, `flow:resilience`
- `trace:request`, `trace:state`, `trace:contract`, `trace:component`
- `trace:deployment`, `trace:migration`, `trace:permissions`

```
# REQUIRED: Zone 4 gate must reference simulation artifact types and coverage
# EXAMPLE:  ">=2 flow simulations archived; trace:contract documented; no P0 gaps"
```

---

# ZONE 5: SYNTHESIS -- What will the world say?

**Arc position**: Synthesis. Pre-ship feedback modeling and narrative readiness.
**Namespaces**: `listen`, `topic`
**Dependency**: Zone 4 artifacts. This zone is optional.

Available skills:
- `listen:feedback`, `listen:support`, `listen:adoption`
- `topic:status`, `topic:report`, `topic:story`

```
# REQUIRED if zone present: gate must name feedback/adoption artifacts
# EXAMPLE:  "listen-feedback artifact present; no critical adoption blockers"
```

---

# ECHO -- Reflection (mandatory final stage)

**Arc position**: Terminus. Always last. Not a zone. Echo runs no skills.

```yaml
# REQUIRED: echo must be the LAST stage
# REQUIRED: DO NOT add any stages after echo
# REQUIRED: DO NOT add skills to echo
# REQUIRED: auto: true must be present
- name: echo                # REQUIRED: "echo" exactly -- DO NOT RENAME
  skills: []                # REQUIRED: empty list -- DO NOT ADD anything here
  auto: true                # REQUIRED: present and true -- DO NOT REMOVE or set false
  question: "What did we learn that we didn't expect?"
```

---

# OUTPUT TEMPLATE

Produce valid YAML. Keep all zone-separator comments in your output.
Every `# REQUIRED` annotation must appear in the completed YAML.

```yaml
# {{topic}}-program-{{date}}.md
# REQUIRED: preserve -- this program is a plan, not an executor; skills run standalone
program:
  topic: "{{topic}}"          # REQUIRED: feature name
  strategy: "{{strategy}}"    # REQUIRED: one sentence -- what decision does this plan inform?
                               # REQUIRED: DO NOT omit strategy

  stages:

    # ===== ZONE 1: DISCOVERY =====
    - name: <discovery-phase-label>           # REQUIRED: phase intent -- DO NOT use "scout"
      skills:                                 # REQUIRED: from Zone 1 catalog above
        - scout:<skill>                       # valid: feasibility, competitors, market, etc.
      gate: "<evidence condition>"            # REQUIRED: artifact names or counts, not "done"
                                              # REQUIRED: at least ONE gate in plan must be quantified
                                              # EXAMPLE: ">=2 scout signals; no blocking concerns"

    # ===== ZONE 2: DESIGN =====
    - name: <design-phase-label>              # REQUIRED: phase intent -- DO NOT use "draft"
      skills:                                 # REQUIRED: from Zone 2 catalog above
        - draft:<skill>
      gate: "<evidence condition>"            # REQUIRED: must confirm draft-spec present

    # ===== ZONE 3: VALIDATION =====
    - name: <validation-phase-label>          # REQUIRED: phase intent -- DO NOT use "review"
      skills:                                 # REQUIRED: from Zone 3 catalog above
        - review:<skill>
      gate: "<evidence condition>"            # REQUIRED: include P0 finding count

    # ===== ZONE 4: SIMULATION =====  (add/remove stages within this zone as needed)
    - name: <simulation-phase-label>          # REQUIRED: phase intent -- DO NOT use "flow"/"trace"
      skills:                                 # REQUIRED: from Zone 4 catalog above
        - flow:<skill>
        - trace:<skill>
      gate: "<evidence condition>"            # REQUIRED: simulation artifact coverage

    # ===== ZONE 5: SYNTHESIS =====  (optional -- omit if not applicable to {{topic}})
    - name: <synthesis-phase-label>           # REQUIRED if present: phase intent, not "listen"
      skills:                                 # REQUIRED: from Zone 5 catalog above
        - listen:<skill>
      gate: "<evidence condition>"

    # ===== ECHO =====  REQUIRED: must be LAST -- DO NOT ADD stages after this
    - name: echo                              # REQUIRED: "echo" exactly -- DO NOT RENAME
      skills: []                              # REQUIRED: empty -- DO NOT ADD any skills
      auto: true                              # REQUIRED: present and true -- DO NOT REMOVE
      question: "What did we learn that we didn't expect?"
      # REQUIRED: DO NOT add a gate field to echo
      # REQUIRED: DO NOT move echo before other stages
```

---

## Summary

| Variation | Axis | C-13 | C-14 | C-15 | Expected composite |
|-----------|------|------|------|------|--------------------|
| V-01 | Arc-as-spine | PASS | PARTIAL | FAIL | ~103 |
| V-02 | Full deletion-resistance | PARTIAL | PASS | FAIL | ~103 |
| V-03 | Plan-level YAML error block | PARTIAL | PARTIAL | PASS | ~108 |
| V-04 | Arc-spine + deletion-resist | PASS | PASS | FAIL | ~113 |
| V-05 | Golden synthesis (all three) | PASS | PASS | PASS | ~125 |
