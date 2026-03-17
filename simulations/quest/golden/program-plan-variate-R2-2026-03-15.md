---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 2
rubric: v2
---

# Variations — program-plan (Round 2)

Five complete prompt body variations for `/program:plan`.
Each is a standalone, runnable skill body — not a diff.
Rubric in scope: `program-plan-rubric-v2-2026-03-15.md` (C-01..C-12, 115 pts).

Single-axis variations: V-01 (role sequence), V-02 (output format), V-03 (phrasing register).
Combined variations: V-04 (role sequence + lifecycle emphasis), V-05 (output format + inertia framing).

---

## R1 Retrospective Under v2 Rubric

Three new aspirational criteria (C-10, C-11, C-12) were extracted from R1 excellence signals.
Retroactively scoring the top R1 variations:

| Variation | C-10 contrast | C-11 structural | C-12 dual-anchor | v2 composite |
|-----------|--------------|-----------------|------------------|-------------|
| V-01 (role seq) | FAIL — no contrast pair | FAIL — rules stated, not embedded | PARTIAL — role table + YAML covers C-03/C-04, not C-01/C-02 | ~82 |
| V-02 (annotated) | PARTIAL — inline # BAD/EXAMPLE but not a labeled pair | PASS — echo pre-positioned with # REQUIRED | PARTIAL — skeleton + prose covers C-02/C-04, partial C-01/C-03 | ~87 |
| V-03 (question) | FAIL — no contrast pair | FAIL — rules only | FAIL — single-anchor throughout | ~72 |
| V-04 (bands) | FAIL — no contrast pair | PASS — lifecycle bands enforce namespace order | PARTIAL — band catalog + YAML covers C-03/C-05, not C-01/C-02/C-04 | ~84 |
| V-05 (inertia) | PASS — labeled BAD/GOOD YAML pair | PARTIAL — echo in skeleton but not # REQUIRED annotated | PARTIAL — opening + template + checklist covers C-04/C-07, not all 4 essentials | ~90 |

**R2 target**: every variation achieves all 12 v2 criteria. The three new aspirational criteria
require deliberate placement. V-05 R1 is the strongest baseline; R2 asks whether C-10, C-11,
and C-12 can be made structurally guaranteed rather than incidental across all five axes.

---

## V-01 — Role Sequence axis

**Axis**: Role sequence — map skills to roles before ordering stages
**Hypothesis**: Framing the plan around *who does what* (PM, Architect, Dev, Team) before
namespace order produces handoff gates (C-04, C-06) that naturally reference what the next
role needs to start. The role catalog table functions as anchor-1 for C-03 (valid skills) and
C-04 (evidence framing). The YAML template with inline gate-comment prompts functions as
anchor-2. This dual-anchor structure targets C-12 for all four essential criteria.
C-11 is addressed by pre-positioning echo in the YAML template. C-10 is addressed by a
BAD/GOOD gate table in Step 3.

---

### Prompt body

**`/program:plan` — a plan, not an executor.**

The program stages skills into named phases with evidence gates. It does not run skills.
Every skill listed remains independently runnable without the program. The program exists so
a team can agree on *what evidence must exist* before advancing — not so skills run on their
behalf.

---

You are running `/program:plan` for topic **{{topic}}**.

Produce `{{topic}}-program-{{date}}.md` — a `program.yaml` staging Signal skills into a
gated evidence plan.

**Step 1 — Map skills to roles**

Signal skills are organized by team role. Select only the skills relevant to {{topic}}:

| Role | Valid Signal skills |
|------|---------------------|
| PM | `scout:competitors`, `scout:feasibility`, `scout:naming`, `scout:compliance`, `scout:market`, `scout:stakeholders`, `scout:positioning`, `scout:requirements`, `draft:pitch` |
| Architect | `draft:spec`, `draft:proposal`, `draft:brainstorm`, `prove:hypothesis`, `prove:analysis`, `prove:websearch`, `prove:intelligence`, `prove:synthesize` |
| Domain dev | `flow:lifecycle`, `flow:conversation`, `flow:trigger`, `flow:dataflow`, `flow:integration`, `flow:throttle`, `flow:resilience` |
| System dev | `trace:request`, `trace:state`, `trace:contract`, `trace:component`, `trace:deployment`, `trace:migration`, `trace:permissions` |
| Team | `review:design`, `review:code`, `review:users`, `review:customers`, `prove:prototype`, `prove:interview`, `prove:publish` |
| PM + Team | `listen:feedback`, `listen:support`, `listen:adoption`, `topic:status`, `topic:report`, `topic:story` |

Every skill entry in the plan must come from this table. Invented names (e.g., `scout:analysis`,
`build:deploy`) fail validation.

**Step 2 — Group by phase**

Organize selected skills into 3–6 stages that reflect natural role handoffs. Follow the
namespace dependency chain — a later-layer skill cannot precede the artifacts it depends on:

```
scout → draft → review/prove → flow/trace → listen/topic → echo
```

Dependency rules:
- `review:*` requires a prior stage to have produced `draft:spec`
- `flow:*` and `trace:*` require a prior stage to have produced `review:*` artifacts
- `prove:*` belongs in or before the review/prove layer; never after flow/trace

Stage names must describe team intent, not namespace names:
- PASS: `discovery`, `market-scan`, `design-commit`, `expert-review`, `simulation`, `feedback-preview`
- FAIL: `scout`, `draft`, `stage1`, `step-2`

**Step 3 — Write gates**

Every stage except `echo` needs a `gate` field expressing **evidence state** — what artifacts
must exist or what conditions must be verifiably true before advancing.

| | Gate example | Why |
|--|--------------|-----|
| **BAD** | `"all scout skills complete"` | Execution state. Who checks? What does "complete" require? |
| **GOOD** | `"scout-feasibility and scout-requirements artifacts present; no blocking concerns"` | Names artifacts the next stage owner can verify exist |
| **BETTER** | `">=2 scout signals archived; no blocking feasibility concerns; PM has reviewed"` | Quantified and verifiable without asking if skills ran |

At least one gate across the plan must include a numeric threshold:
`">=2 scout signals"`, `"0 P0 findings open"`, `">=3 review artifacts present"`.

Gate framing tip: a gate at a role boundary reads like a handoff memo —
*"what does the next role's owner need to assume is true before they can start?"*

**Step 4 — Add echo**

The final stage is always `echo`. It is not a skill stage. It is a reflection moment.

```yaml
- name: echo
  skills: []      # required: empty list — echo runs no skills
  auto: true      # required: must be present and true
  question: "What did we learn that we didn't expect?"
```

Echo has no skills. Echo must be last. Do not add any skills to echo.

**Output format**

```yaml
# {{topic}}-program-{{date}}.md
# This program is a plan, not an executor — every skill runs standalone
program:
  topic: "{{topic}}"
  strategy: "{{strategy — what decision does this program inform?}}"
  stages:
    - name: <phase-label>             # descriptive role-intent label, not namespace name
      skills:
        - namespace:skill             # from Step 1 role catalog above — no invented names
      # Gate rationale: what must the next role's owner be able to assume is true?
      gate: "<artifact-referencing condition>"   # name artifacts, NOT "done"/"complete"

    # ... additional stages following scout → draft → review/prove → flow/trace → listen order ...

    - name: echo                      # REQUIRED: must be last
      skills: []                      # REQUIRED: empty — echo runs nothing
      auto: true                      # REQUIRED: must be present
      question: "What did we learn that we didn't expect?"
```

Write the complete YAML. Include a one-sentence gate-rationale comment above each `gate` field.

---

## V-02 — Output Format axis

**Axis**: Output format — annotated YAML skeleton with `# REQUIRED` / `# BAD` / `# GOOD` markers
**Hypothesis**: A pre-filled skeleton with structural annotations is the strongest C-11 mechanism:
the model fills in `<...>` placeholders within a correct-by-construction scaffold. C-02 (echo
contract) is structurally enforced by pre-positioning echo at the end of the skeleton with
`# REQUIRED: DO NOT REMOVE`. C-04 (evidence-state gates) is pre-anchored by inline `# BAD` and
`# GOOD` comments at every gate slot — the failure mode is visible at authoring time. C-03 (valid
skills) is doubly anchored by a namespace catalog before the template and by `# valid namespaces:`
inline comments at each skill slot. C-12 is addressed because every essential requirement appears
in both the pre-template rules section AND the skeleton inline comments.

---

### Prompt body

You are running `/program:plan` for topic: **{{topic}}**.

Produce `{{topic}}-program-{{date}}.md` by filling in the template below.
Replace all `<...>` placeholders. The program is a plan, not an executor — every skill in the
plan remains independently runnable without it.

**Signal skill catalog** (valid skills only — any invented name fails):

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

**Template** — fill in all `<...>`; keep all `# REQUIRED` lines in your output:

```yaml
# {{topic}}-program-{{date}}.md
# REQUIRED: preserve — this program is a plan, not an executor; skills run standalone

program:                                # REQUIRED: top-level key must be "program"
  topic: "<topic name>"                 # REQUIRED
  strategy: "<one-sentence goal>"       # REQUIRED: what decision does this plan inform?

  stages:

    # ---- Stage 1 ----
    - name: "<phase-label>"             # REQUIRED: descriptive intent label, not "stage1" or "scout"
      skills:                           # REQUIRED: select from Signal catalog above
        - scout:<skill>                 #   valid scout options listed in catalog table above
      gate: "<condition>"               # REQUIRED: names artifact types or signal counts
                                        # BAD:  "scout complete" / "done" / "all run" / "proceed"
                                        # GOOD: "scout-feasibility and scout-requirements artifacts present"
                                        # BEST: ">=2 scout signals archived; no blocking concerns"

    # ---- Stage 2 ----
    - name: "<phase-label>"
      skills:
        - draft:<skill>                 #   valid draft options: spec, proposal, pitch, brainstorm
      gate: "<condition>"
                                        # HINT: at least ONE gate across the plan must be quantified
                                        # e.g., "draft-spec present; >=2 scout signals reviewed"
                                        # DEPENDENCY: draft stages must follow scout stages

    # ---- Stage 3 ----
    - name: "<phase-label>"
      skills:
        - review:<skill>                #   valid review options: design, code, users, customers
      gate: "<condition>"
                                        # DEPENDENCY: review stages require draft:spec in a prior stage
                                        # BAD:  "review done"
                                        # GOOD: "review-design artifact present; 0 P0 findings open"

    # ---- Stage 4+ (add/remove stages as needed) ----
    # Namespace dependency order: scout → draft → review/prove → flow/trace → listen → topic
    #
    # flow options: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
    # trace options: request, state, contract, component, deployment, migration, permissions
    # prove options: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
    # listen options: feedback, support, adoption
    #
    # flow:* / trace:* require review:* artifacts from a prior stage
    # listen:* / topic:* come after simulation stages

    # ---- FINAL STAGE ---- REQUIRED: must be last, exactly as shown ----
    - name: echo                        # REQUIRED: must be "echo" exactly
      skills: []                        # REQUIRED: empty list — echo runs no skills
      auto: true                        # REQUIRED: must be present and true
      question: "What did we learn that we didn't expect?"
      # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
```

**Rules checklist before submitting**:
1. Echo must be last. `skills: []`. `auto: true`. All three required — no exceptions.
2. Every non-echo gate names artifact types or verifiable conditions. "Done" fails.
3. At least one gate is quantified: `">=N signals"`, `"0 P0 findings"`.
4. All skill references are from the Signal catalog above. No invented names.
5. Stage names are phase-intent labels, not namespace names and not `stage1`/`step-N`.

Output only the completed YAML. Remove `# BAD` / `# GOOD` / `# HINT` / `# DEPENDENCY`
placeholder comments. Keep `# REQUIRED` comments and the plan-not-executor header comment.

---

## V-03 — Phrasing Register axis

**Axis**: Phrasing register — question-framing turns each stage into an investigation question
**Hypothesis**: When stages are framed as questions ("Is this feasible?", "What are we building?"),
the gate answer naturally takes the form "what evidence proves we answered it?" — producing
artifact-referencing language for C-04 without requiring the model to remember the rule. C-11
is addressed by framing echo as "the moment after all questions have been answered — a listening
moment, not a question," structurally distinguishing it from skill stages. C-12 is addressed by
the question-bank catalog (anchor-1 for C-03 and C-04) and YAML `# Question:` comment above each
gate (anchor-2). C-10 is addressed by a "question answered vs. question run" BAD/GOOD contrast.

---

### Prompt body

You are running `/program:plan` for topic **{{topic}}**.

A program plan is a plan, not an executor. It does not run skills. It sequences investigation
questions into phases with evidence gates — checkpoints that answer: *"how do we know this
question has been answered?"*

Think of each stage as a question the team is trying to answer. The gate is your response to:
*"what evidence tells us we've answered it?"* The distinction matters:

| | |
|--|--|
| **Not answered** | "We ran `scout:feasibility`" — execution state; tells us the skill ran, not what was found |
| **Answered** | "scout-feasibility artifact present; no blocking feasibility concerns identified" — evidence state; names what must be true |

**Question bank — select questions relevant to {{topic}}:**

*Discovery questions* (scout namespace):
- "Is this technically and commercially feasible?" → `scout:feasibility`
- "Who else is doing this, and how are we different?" → `scout:competitors`
- "What do stakeholders actually need?" → `scout:stakeholders`, `scout:requirements`
- "What is the market context?" → `scout:market`, `scout:positioning`
- "What should we call it?" → `scout:naming`
- "Are there compliance constraints?" → `scout:compliance`

*Design questions* (draft namespace):
- "What exactly are we building?" → `draft:spec`
- "Which approach should we commit to?" → `draft:proposal`
- "What options haven't we considered?" → `draft:brainstorm`
- "How do we tell this story?" → `draft:pitch`

*Validation questions* (review + prove namespace):
- "Does the design hold up under expert scrutiny?" → `review:design`
- "Will real users understand and trust it?" → `review:users`
- "Will customers pay for it?" → `review:customers`
- "We believe X — but do we?" → `prove:hypothesis`, `prove:analysis`, `prove:synthesize`
- "What does the field already know?" → `prove:websearch`, `prove:intelligence`
- "What do real users say in their own words?" → `prove:interview`

*Simulation questions* (flow + trace namespace):
- "Does the business process work end-to-end?" → `flow:lifecycle`, `flow:conversation`
- "What happens when things go wrong?" → `flow:resilience`, `flow:throttle`
- "What triggers this feature and what does it produce?" → `flow:trigger`, `flow:dataflow`
- "What does the system actually do?" → `trace:request`, `trace:state`, `trace:contract`
- "Will this survive deployment and migration?" → `trace:deployment`, `trace:migration`
- "Who can do what, and under what conditions?" → `trace:permissions`, `trace:component`

*Feedback questions* (listen namespace):
- "What will customers say after we ship?" → `listen:feedback`
- "What will support look like?" → `listen:support`
- "Will people actually adopt it?" → `listen:adoption`

**Assembling the plan**

1. **Select questions** that apply to {{topic}} and {{strategy}}.
2. **Group related questions** into 3–6 stages. Each stage is a cluster of questions the team
   works through before hitting a gate.
3. **Keep questions in order**: discovery before design, design before validation, validation
   before simulation, simulation before feedback. This is the namespace dependency order:
   `scout → draft → review/prove → flow/trace → listen → topic`.
4. **Write each gate** as: *"what evidence tells us this cluster of questions has been answered?"*
   Name the artifact types that must exist.
   - "scout-feasibility artifact present; no blocking concerns" → PASS
   - "stage complete" → FAIL: names no evidence
5. **Make at least one gate quantified**: `">=2 scout signals present"` or
   `"draft-spec present and >=3 review findings resolved"`.
6. **Name each stage** after the question cluster: `feasibility`, `design-commit`,
   `expert-validation`, `domain-simulation`, `feedback-preview`.

**The echo**

After all questions are answered, the program closes with `echo`. Echo is not a question — it
is a listening moment. You are asking: *"what did we learn that we didn't expect, across all
the questions we just answered?"*

```yaml
- name: echo
  skills: []      # echo asks no new questions — it reflects on what was learned
  auto: true
  question: "What did we learn that we didn't expect?"
```

Echo has no skills. Echo is always last. `auto: true` is required.

**Output**

Produce valid YAML with top-level key `program`. Include: `topic`, `strategy`, `stages`.
Each non-echo stage: `name`, `skills` (list), `gate` (evidence-state string).
Echo stage: `name: echo`, `skills: []`, `auto: true`, `question`.

Above each gate, include a comment: `# Question: <the question this stage answers>`.

```yaml
# {{topic}}-program-{{date}}.md
# This program is a plan, not an executor — every skill runs standalone
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:
    # Question: <question this stage answers>
    - name: <stage-name>
      skills:
        - namespace:skill       # from question bank above — no invented names
      gate: "<evidence condition — what artifacts prove the question is answered?>"
    # ...
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis

**Axis**: Role sequence × lifecycle emphasis — four named lifecycle bands with explicit
role-handoff boundaries
**Hypothesis**: Naming four lifecycle bands (Prove It / Design It / Simulate It / Listen Ahead)
with explicit role assignments produces both better stage grouping (C-06, C-09) and structural
enforcement of namespace dependency order (C-11 for C-05). Band-boundary gates become handoff
contracts between roles, naturally producing artifact-referencing language (C-04). C-12 is
addressed by per-band skill catalogs (anchor-1 for C-03) and YAML band-divider comments with
inline skill options (anchor-2). C-10 is addressed by a BAD/GOOD contrast between a flat plan
and a banded plan. C-11 for C-02 is addressed by echo pre-positioned with `# REQUIRED` after
the final band.

---

### Prompt body

You are running `/program:plan` for topic **{{topic}}** with strategy **{{strategy}}**.

A Signal program plan stages evidence-gathering work into phases with role-handoff gates.
This is a plan, not an executor: the program declares what evidence must exist before each
phase can begin. Every skill remains independently runnable.

**The cost of no bands** — what teams get without a program plan:

```yaml
# BAD: flat plan — all skills in one stage, execution-state gate
program:
  topic: "example"
  stages:
    - name: everything
      skills:
        - scout:feasibility
        - draft:spec
        - review:design
        - flow:lifecycle
        - listen:feedback
      gate: "all done"    # meaningless: "done" by what measure? who checks?
    - name: echo
      skills: []
      auto: true
```

Skills run out of dependency order. Nobody knows when it is safe to advance because `"all done"`
names no evidence.

**The four lifecycle bands**

Signal's namespaces map onto four lifecycle bands. Build your plan across these bands.

```
Band 1 — PROVE IT (PM + Architect)
  Purpose: Is this worth building? Is it feasible?
  Namespaces: scout, draft, prove
  Handoff signal: "we know what we are building and why"

Band 2 — DESIGN IT (Architect + Team)
  Purpose: Have we written it down and had it reviewed?
  Namespaces: draft (finalization), review
  Handoff signal: "spec exists and no blocking review findings remain"

Band 3 — SIMULATE IT (Dev)
  Purpose: Does it work on paper before we build it?
  Namespaces: flow, trace
  Handoff signal: "all critical paths simulated; no P0 simulation gaps"

Band 4 — LISTEN AHEAD (Team + PM)
  Purpose: What will the world say after we ship?
  Namespaces: listen, topic
  Handoff signal: "no critical adoption blockers; narrative is coherent"
```

**Available skills per band**

Band 1 — Prove It:
- `scout:competitors`, `scout:feasibility`, `scout:naming`, `scout:compliance`,
  `scout:market`, `scout:stakeholders`, `scout:positioning`, `scout:requirements`
- `draft:spec`, `draft:proposal`, `draft:pitch`, `draft:brainstorm`
- `prove:hypothesis`, `prove:websearch`, `prove:intelligence`, `prove:prototype`,
  `prove:analysis`, `prove:interview`, `prove:synthesize`, `prove:publish`

Band 2 — Design It:
- `draft:spec` (if not finalized in Band 1)
- `review:design`, `review:users`, `review:customers`

Band 3 — Simulate It:
- `flow:lifecycle`, `flow:conversation`, `flow:trigger`, `flow:dataflow`,
  `flow:integration`, `flow:throttle`, `flow:resilience`
- `trace:request`, `trace:state`, `trace:contract`, `trace:component`,
  `trace:deployment`, `trace:migration`, `trace:permissions`

Band 4 — Listen Ahead:
- `listen:feedback`, `listen:support`, `listen:adoption`
- `review:code`, `topic:status`, `topic:report`, `topic:story`

Any skill name not in a band above is invalid. Do not invent skill names.

**Instructions**

1. **Select skills per band** for {{topic}}. Not every topic needs all four bands. Skip
   a band only if none of its questions apply to {{topic}}.

2. **Within each band, create 1–3 stages**. A band with 6 skills might split into
   `market-research` and `feasibility`. A band with 2 skills needs one stage.

3. **Write band-boundary gates as handoff memos**:
   *"What evidence does the next role's first stage require before they can start?"*
   - "scout-requirements and scout-feasibility artifacts present; Architect ready to draft" → PASS
   - "draft-spec reviewed; 0 P0 findings from review:design or review:users" → PASS
   - ">=3 flow simulations complete; trace:contract documented" → PASS (quantified)
   - "Band 1 done" → FAIL — execution state; names no evidence
   Make at least one gate quantified.

4. **Stage names reflect band + purpose**:
   - Band 1: `market-research`, `feasibility`, `hypothesis-investigation`
   - Band 2: `design-commit`, `expert-review`
   - Band 3: `domain-simulation`, `system-trace`
   - Band 4: `feedback-preview`, `adoption-readiness`

**Echo (mandatory final stage)**

After all bands, the program closes with echo. This is not a band stage. It is a reflection.

```yaml
- name: echo
  skills: []        # REQUIRED: no skills — echo reflects across all prior stages
  auto: true        # REQUIRED: must be present and true
  question: "What did we learn that we didn't expect?"
```

Echo must be last. `skills: []` and `auto: true` are hard requirements.

**Output format**

```yaml
# {{topic}}-program-{{date}}.md
# This program is a plan, not an executor — every skill runs standalone
program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # Band 1: Prove It
    - name: <discovery-label>
      skills:
        - scout:<skill>           # valid Band 1 skills listed above
      gate: "<handoff condition — what must be true before design begins?>"

    # Band 2: Design It
    - name: <design-label>
      skills:
        - draft:<skill>           # valid Band 2 skills listed above
        - review:<skill>
      gate: "<handoff condition — what must be true before simulation begins?>"

    # Band 3: Simulate It (add/remove as needed)
    - name: <simulation-label>
      skills:
        - flow:<skill>            # valid Band 3 skills listed above
        - trace:<skill>
      gate: "<handoff condition — what must be true before feedback begins?>"

    # Band 4: Listen Ahead (add/remove as needed)
    - name: <feedback-label>
      skills:
        - listen:<skill>          # valid Band 4 skills listed above
      gate: "<handoff condition>"

    # Echo — REQUIRED: must be last, no stage after this
    - name: echo
      skills: []                  # REQUIRED: empty
      auto: true                  # REQUIRED
      question: "What did we learn that we didn't expect?"
```

Keep band-separator comments (`# Band N: <name>`) before each band's first stage.

---

## V-05 — Combined: Output Format + Inertia Framing

**Axis**: Output format × inertia framing — BAD/GOOD YAML pair + pre-annotated template + checklist
**Hypothesis**: Showing a labeled BAD plan (inertia: all skills in one stage, execution-state gate)
before the GOOD template makes the failure mode concrete before instructions begin (C-10). The
pre-annotated YAML template enforces C-02 (echo pre-placed with `# REQUIRED: DO NOT REMOVE`) and
C-04 (gate slots annotated with inline `# BAD: / # GOOD:` markers), satisfying C-11 for two
essential criteria. C-12 is satisfied by anchoring each of C-01–C-04 in both the opening contrast
and the template inline comments. The pre-printed checklist as a required output section locks
C-11 verification. C-09 is addressed by layer comments in the template skeleton. C-08 is
modeled in the GOOD example. This is the R2 golden-synthesis candidate.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

Every skill in the program remains independently runnable outside of it. The program exists so
a team can agree on when it is safe to advance — not to run skills automatically. This identity
separates a program plan from a task list: a task list tells you what to do; a program plan
tells you what evidence must exist before you move forward.

---

You are running `/program:plan` for topic **{{topic}}**.

**The inertia pattern — what you are replacing:**

```yaml
# BAD: ad hoc run — no phases, one meaningless gate
program:
  topic: "example-topic"
  strategy: "ship it"
  stages:
    - name: everything
      skills:
        - scout:feasibility
        - scout:requirements
        - draft:spec
        - review:design
        - flow:lifecycle
        - trace:contract
        - listen:feedback
      gate: "all done"    # execution state: when is "done" done? who checks?
    - name: echo
      skills: []
      auto: true
```

No phases. Skills run out of dependency order. `review:design` runs before `draft:spec` is
stable. `flow:lifecycle` runs before the design is reviewed. The gate `"all done"` names no
evidence — no one can tell when it is safe to advance.

**The gated plan — what you are building:**

```yaml
# GOOD: three-layer evidence arc with artifact-referencing gates
program:
  topic: "example-topic"
  strategy: "validate feasibility and design before committing to simulation"
  stages:

    # Layer 1: Breadth — establish what we know and what we're building
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      # Gate names the artifacts the design stage owner needs before they can start
      gate: "scout-feasibility, scout-requirements, and scout-competitors artifacts present;
             no blocking feasibility concerns identified; PM has reviewed findings"

    # Layer 2: Depth — commit to an approach, validate it
    - name: design-commit
      skills:
        - draft:spec
        - draft:proposal
      gate: "draft-spec artifact present; draft-proposal options documented;
             Architect has signed off on approach"

    - name: expert-review
      skills:
        - review:design
        - review:users
      # Quantified gate — machine-checkable in principle
      gate: "review-design and review-users artifacts present; >=0 P0 findings open;
             all blocking comments resolved in draft-spec"

    # Layer 3: Synthesis — stress-test, simulate, and listen ahead
    - name: simulation
      skills:
        - flow:lifecycle
        - flow:resilience
        - trace:contract
      gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps identified"

    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"
```

Evidence arc: **breadth** (scout/draft — establish scope) → **depth** (review/prove —
validate the approach) → **synthesis** (flow/trace/listen — stress-test and look ahead) →
**echo** (reflect on what was unexpected).

---

**Build the plan for {{topic}}**

Adapt the example above. Fill in the template below. All `<...>` are required.

Valid Signal skills by namespace:
- `scout`: competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
- `draft`: spec, proposal, pitch, brainstorm
- `review`: design, code, users, customers
- `flow`: lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
- `trace`: request, state, contract, component, deployment, migration, permissions
- `prove`: hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
- `listen`: feedback, support, adoption
- `topic`: new, status, report, plan, story, echo

Namespace dependency order: `scout → draft → review/prove → flow/trace → listen → topic`
A stage with `review:*` cannot precede a stage with `draft:spec`.
A stage with `flow:*` or `trace:*` cannot precede a stage with `review:*`.

```yaml
# {{topic}}-program-{{date}}.md
# REQUIRED: this program is a plan, not an executor — every skill runs standalone

program:
  topic: "{{topic}}"
  strategy: "<one-sentence goal>"

  stages:

    # --- Layer 1: Breadth (scout / draft / prove) ---
    # Goal: establish what we know and what we're building
    - name: "<discovery-phase>"         # descriptive label, not "stage1" or "scout"
      skills:
        # pick from: scout:competitors, scout:feasibility, scout:naming, scout:compliance,
        #            scout:market, scout:stakeholders, scout:positioning, scout:requirements,
        #            draft:pitch, prove:hypothesis, prove:websearch, prove:intelligence
        - scout:<skill>
      # Why this gate: what must the design-phase owner know before they can start?
      gate: "<artifact-condition>"      # name artifacts; NOT "done" / "complete" / "proceed"
                                        # BAD:  "scout complete"
                                        # GOOD: "scout-feasibility and scout-requirements artifacts present"

    # --- Layer 2: Depth (draft / review / prove) ---
    # Goal: commit to an approach and validate it
    # DEPENDENCY: review:* requires draft:spec to have been produced in Layer 1 or this stage
    # DEPENDENCY: prove:* belongs here — not after flow/trace
    - name: "<design-or-review-phase>"
      skills:
        # pick from: draft:spec, draft:proposal, draft:brainstorm, review:design, review:users,
        #            review:customers, prove:prototype, prove:analysis, prove:interview,
        #            prove:synthesize
        - draft:<skill>
      gate: "<artifact-condition>"
                                        # REQUIRED: at least ONE gate in the plan must be quantified
                                        # e.g., ">=2 scout signals reviewed; 0 P0 findings open"

    # --- Layer 3+: Synthesis (flow / trace / listen / topic) ---
    # DEPENDENCY: flow:*/trace:* require review:* from Layer 2
    # DEPENDENCY: listen:*/topic:* come after simulation stages
    # (add or remove Layer 3 stages based on {{topic}} scope)

    # --- Final Stage: REQUIRED, must be last ---
    - name: echo                        # REQUIRED: must be "echo" exactly
      skills: []                        # REQUIRED: empty list — echo runs no skills
      auto: true                        # REQUIRED: must be present and true
      question: "What did we learn that we didn't expect?"
      # REQUIRED: DO NOT add skills here. DO NOT move this stage before any other stage.
```

After the YAML block, produce this verification section with each box honestly checked:

```markdown
## Plan Verification

- [ ] Every non-echo gate names at least one artifact type (e.g., `scout-feasibility`, `draft-spec`)
- [ ] No gate uses execution language: "done" / "complete" / "proceed" / "all passed"
- [ ] At least one gate includes a numeric threshold (e.g., `>=2 scout signals`, `0 P0 findings`)
- [ ] Echo is last, has `skills: []`, has `auto: true`; no skills added; no stage follows echo
- [ ] Every skill name is from the Signal catalog (9 namespaces); no invented names
- [ ] Stage names are descriptive phase labels; not namespace names; not `stage1` / `step-N`
```

Output: the completed YAML plus the Plan Verification section with boxes checked.
Do not include the `# BAD:` / `# GOOD:` / `# DEPENDENCY:` placeholder comments in the output.
Keep `# REQUIRED:` comments and the plan-not-executor header comment.
