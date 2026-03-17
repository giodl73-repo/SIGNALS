---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 3
rubric: v19
---

# program-plan -- R3 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v19 (C-01 through C-15, 15 criteria, golden = all essential pass AND
composite >= 80).

---

## R2 Retrospective Under v19 Rubric

v19 adds three aspirational criteria to the v18 set: C-13 (template-locked verification),
C-14 (arc structure labeled inside YAML template), C-15 (dual-site not-executor anchoring).

Retroactive scoring of R2 V-04 and V-05 -- the top-scoring R2 variations -- against v19:

| Variation | C-13 | C-14 | C-15 | v19 score |
|-----------|------|------|------|-----------|
| V-04 (Pre-Printed Template) | PASS -- checklist pre-printed as required output section | PASS -- Layer 1/2/3+ labels inside YAML template | PASS -- opening "This skill is a plan, not an executor." + `# REQUIRED: preserve this comment` in YAML | **100/100** |
| V-05 (Golden Synthesis) | PASS -- checklist pre-printed | PASS -- Layer 1/2/3+ labels in YAML template | FAIL -- YAML comment lacks REQUIRED/preserve marker; rubric requires "marked as required or preserve-required" | **98.75/100** |

**R2 V-04 retroactively scores 100/100 on v19.** The three new criteria were structurally
satisfied by the template-skeleton approach V-04 introduced.

**R3 target**: since the R2 V-04 structure achieves 100/100, R3 explores whether different
stylistic approaches also achieve 100/100, and where single-axis variations expose tradeoffs
between expressiveness and criterion coverage.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Role sequence | Phases organized by role handoffs (PM -> Architect -> Engineer -> Team) | Does role-centric labeling preserve namespace dependency while improving readability? |
| Phrasing register | Discovery/invitation questions vs imperative directives | Does question framing produce richer, more evidence-specific gates? |
| Inertia framing | BAD pattern opens the prompt, before skill introduction | Does leading with the anti-pattern establish not-executor identity through negation? |
| Lifecycle emphasis | Extensive per-phase prose + phase-transition criteria | Does more phase-boundary depth push quantified gate production? |
| Output format | Compact inline annotation vs separate instruction blocks | Can all 15 criteria be satisfied in minimal surface area? |

Single-axis: V-01 (role sequence), V-02 (phrasing register), V-03 (inertia framing)
Combined: V-04 (role sequence + lifecycle emphasis), V-05 (all axes, golden)

---

## V-01 -- Role Sequence (single-axis)

**Axis**: Role sequence -- stages organized by role handoffs rather than namespace categories
**Hypothesis**: Framing each arc layer as a role handoff (PM Discovery -> Architect Design ->
Engineering Validation -> Team Synthesis) creates a more accessible plan for cross-functional
readers. Namespace dependency is preserved by the handoff sequence itself -- PM runs scout before
Architect designs; Architect designs before engineers trace. Role labels in the arc template
satisfy C-14 naturally. BAD/GOOD contrast is omitted to keep the axis clean; C-10 is expected
to FAIL in this variation.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into role-owned phases, each gated on evidence the next role needs
before starting their work. No skill runs automatically. Every skill in the plan remains
independently runnable outside the program. The value is the gate: a shared agreement on what
must be true before handing off to the next phase.

---

You are running `/program:plan` for topic **{{topic}}**.

**Role-phase structure**

Signal programs follow a four-role handoff sequence:

| Phase owner | Phase goal | Signal namespaces |
|-------------|-----------|-------------------|
| PM | Discovery -- establish what we know about the space | scout, prove:websearch, prove:intelligence |
| Architect + PM | Design -- commit to a concrete approach | draft:spec, draft:proposal, prove:hypothesis |
| Engineering | Validation -- review, prove, simulate, trace the design | review, prove:prototype, flow, trace |
| Team | Synthesis -- listen ahead, close the evidence loop | listen, topic |
| (auto) | Echo -- what did we learn? | (none) |

**Gate rule**: Each gate names the artifacts the NEXT role needs before they can begin -- not
what the current phase did. A gate saying `"discovery complete"` tells the Architect nothing.
A gate saying `"scout-feasibility and scout-requirements artifacts present; PM has reviewed for
blocking concerns"` tells the Architect exactly what must be true before they draft a spec.

At least one gate must include a numeric threshold: `">= 2 scout signals present"` or
`"0 P0 findings open"`.

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`. `prove:*` belongs
in or before the review/prove layer, not after flow/trace.

**Signal skill catalog** (valid names only):

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming,
  stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize,
  websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal for this program>"

  stages:

  # ---- PM Phase: Discovery -- scout the space, establish what we know ----
  # PM runs these; gate captures what the Architect needs before designing

    - name: "<discovery-phase-label>"       # descriptive, e.g. "discovery" or "market-scan"
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>                     # add/remove as topic warrants
      gate: "<what the Architect needs before drafting -- name specific artifacts;
             numeric threshold: '>= 2 scout signals present'>"

  # ---- Architect+PM Phase: Design -- commit to a concrete approach ----
  # Architect+PM run these; gate captures what engineers need before validation

    - name: "<design-phase-label>"          # e.g. "design" or "proposal"
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<what engineers need before they can review or trace -- name draft artifacts>"

  # ---- Engineering Phase: Validation -- review, prove, simulate, trace ----
  # Engineering runs these; requires design artifacts from above
  # review:* requires draft:spec | prove:* belongs here | flow:*/trace:* last in this layer

    - name: "<validation-phase-label>"      # e.g. "expert-review" or "validation"
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-label>"      # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ---- Team Phase: Synthesis -- listen ahead, close the loop ----
  # Full team; runs after engineering validation

    - name: "<synthesis-phase-label>"       # e.g. "synthesis" or "feedback-preview"
      skills:
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<all key signals archived; listen signal present>"

  # ---- Final Stage: echo -- always last, do not move ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state (artifact exists, signal present) -- not execution state
- [ ] At least one gate contains a numeric threshold (e.g., `>= 2 scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels (not namespace names, not generic indices)
- [ ] Four role-phase comments (PM / Architect+PM / Engineering / Team) preserved in YAML

---

## V-02 -- Phrasing Register (single-axis)

**Axis**: Phrasing register -- invitation and discovery questions throughout, replacing imperatives
**Hypothesis**: Framing every structural instruction as a question the plan must answer ("What
must be true before the next phase is worth starting?") induces richer gate construction. The
model answers the question with evidence conditions rather than transcribing a rule about evidence
state. C-04 and C-09 are expected to benefit. BAD/GOOD contrast is omitted (C-10 FAIL expected)
to keep the register axis clean.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It asks one question for every phase: *what must be true before the next phase is worth starting?*
Every skill in the plan remains independently runnable. The program is optional scaffolding for
teams that want shared gate criteria -- a contract, not an automation layer. Gates are its only
product. A plan without gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The three planning questions:**

**Question 1 -- What does the team need to explore before designing?**

What do you need to understand about {{topic}} before committing to an approach?
These are the breadth signals: feasibility, market shape, requirements, competing approaches,
compliance constraints. Scout-namespace and early prove skills (websearch, intelligence,
hypothesis) answer this question.

What does a complete answer look like before you move on? That is your gate for this phase.
Numeric thresholds make it machine-checkable: `">= 2 scout signals present; PM has reviewed"`.

**Question 2 -- What needs to be designed, validated, or proven?**

After exploring, what is unproven? What assumptions need to be stress-tested before the team
ships? Draft, review, prove, flow, and trace skills answer this question. They require artifacts
from Question 1 -- you cannot review a spec that does not exist yet.

What does validation complete look like? That is your gate. At least one gate across the plan
should be quantified: `"0 P0 findings open"` or `">= 2 review signals present"`.

**Question 3 -- What does readiness sound like from the outside?**

Before the team commits, what do users, customers, and adopters need to have signaled? Listen
and topic skills answer this question. They close the evidence loop.

What does readiness sound like? That is your final non-echo gate.

**Namespace dependency** (which questions must be answered in sequence):
```
scout/prove:websearch -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`. `prove:*` belongs
in or before the review/prove layer.

**Signal skill catalog:**

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming,
  stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize,
  websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<what question does this program ultimately answer?>"

  stages:

  # ---- Layer 1: Exploration -- what do we need to know before designing? ----

    - name: "<what is this exploration phase called?>"
      skills:
        # What skills answer the breadth questions for {{topic}}?
        - scout:<skill>
        - scout:<skill>
      gate: "<what does a complete answer to the exploration question look like?
             What must exist before design can begin?
             Numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Validation -- what needs to be proven or reviewed? ----
  # (review:* requires draft from Layer 1; flow:*/trace:* require review:*)

    - name: "<what is this validation phase called?>"
      skills:
        # What skills validate or prove the approach for {{topic}}?
        - draft:<skill>
        - review:<skill>
        - prove:<skill>
      gate: "<what does validation complete look like?
             What must exist before synthesis can begin?
             Quantified: '0 P0 findings open' or '>= N signals present'>"

  # ---- Layer 3: Synthesis -- what does readiness sound like from the outside? ----

    - name: "<what is this synthesis phase called?>"
      skills:
        # What skills close the evidence loop for {{topic}}?
        - listen:<skill>
        - topic:<skill>
      gate: "<what does the team need to have heard before committing?
             What listen/topic artifacts must be present?>"

  # ---- Final Stage: echo -- always last ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

Answer each question about the plan you produced:

- [ ] Is the last stage `echo` with `skills: []` and `auto: true`?
- [ ] Do all skill names come from Signal's 9 namespaces?
- [ ] Does every non-echo gate describe what must *exist* -- not what was *done*?
- [ ] Does at least one gate name a number?
- [ ] Do stage names answer "what phase is this?" rather than labeling the namespace?
- [ ] Are the three layer comments (Exploration / Validation / Synthesis) preserved?

---

## V-03 -- Inertia Framing (single-axis)

**Axis**: Inertia framing -- the BAD anti-pattern opens the entire prompt, before the skill
is introduced
**Hypothesis**: Placing the anti-pattern before the skill description establishes not-executor
identity through negation (C-12 via contrast). The opening bad example is what most teams do
today; the skill exists because that pattern fails. Leading with failure makes the purpose of
each element -- phases, gates, arc structure -- concrete rather than abstract. The contrast-first
opening also maximizes labeled juxtaposition for C-10. Role framing is minimal to keep the
inertia axis clean.

---

### Prompt body

```yaml
# This is how most feature work gets planned today:

program:
  topic: "{{topic}}"
  stages:
    - name: "do the research"
      skills:
        - scout:feasibility
        - scout:requirements
        - draft:spec
        - review:design
        - flow:lifecycle
        - trace:request
        - listen:feedback
      gate: "done"
    - name: echo
      skills: []
      auto: true
```

One stage. Skills in the wrong order. A gate that names nothing. The team has no shared
definition of what "done" means, and nobody knows when it's safe to advance -- because the gate
names no evidence. Skills run out of dependency order: you cannot review a spec that has not
been written; you cannot trace a flow that has not been reviewed.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Skills listed here still run standalone. The plan's only product
is the gate: a shared agreement on what evidence must exist before advancing. No gate, no plan.

---

You are running `/program:plan` for topic **{{topic}}**.

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc with artifact-referencing gates

program:
  topic: "{{topic}}"
  stages:

  # Layer 1: Breadth -- establish what we know
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      gate: "scout-feasibility, scout-requirements, and scout-competitors artifacts present;
             >= 2 scout signals reviewed by PM; no blocking feasibility concerns"

  # Layer 2: Depth -- design and validate
    - name: design
      skills:
        - draft:spec
        - draft:proposal
      gate: "draft-spec artifact present; Architect has confirmed no blocking feasibility gaps"

    - name: expert-review
      skills:
        - review:design
        - review:users
        - prove:prototype
      gate: "review-design, review-users, prove-prototype artifacts present; 0 P0 findings open"

  # Layer 3: Synthesis -- listen ahead, close the loop
    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: echo
      skills: []
      auto: true
```

Phases. Evidence gates. Dependency order preserved. This is what you're building for {{topic}}.

**Rules:**

1. **Gates name evidence state, not execution state.** `"done"`, `"complete"`, `"proceed"` fail.
   `"scout-feasibility artifact present"` passes. Quantified is better:
   `">= 2 scout signals present and draft-spec artifact exists"`.

2. **Namespace dependency order:**
   ```
   scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
   ```
   `review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`.
   `prove:*` belongs in or before the review/prove layer.

3. **Descriptive stage names.** `discovery`, `design`, `expert-review`, `simulation`,
   `synthesis`. Not `stage1`, not namespace names reused as labels.

4. **Echo is last.** `name: echo`, `skills: []`, `auto: true`. No stage after echo.

---

**Signal skill catalog:**

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming,
  stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize,
  websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal>"

  stages:

  # ---- Layer 1: Breadth (scout / draft / prove:websearch) ----

    - name: "<breadth-phase-label>"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth (draft / review / prove / flow / trace) ----
  # review:* requires draft:spec | flow:*/trace:* require review:* | prove:* before flow/trace

    - name: "<depth-phase-label>"
      skills:
        - draft:<skill>
        - review:<skill>
        - prove:<skill>
      gate: "<artifact-referencing condition; at least one numeric threshold across the plan>"

    - name: "<simulation-phase-or-remove>"  # optional; add if flow/trace needed
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis (listen / topic) ----

    - name: "<synthesis-phase-label>"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<all prior signals archived; listen signal present>"

  # ---- Final Stage: echo ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state -- not execution state
- [ ] At least one gate contains a numeric threshold
- [ ] Stage names are descriptive phase labels (not namespace names, not generic indices)
- [ ] Three arc-layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved

---

## V-04 -- Combined: Role Sequence + Lifecycle Emphasis

**Axes**: Role sequence + lifecycle emphasis -- role-owned phases with extensive per-phase prose
describing phase goal, role owner, and gate rationale
**Hypothesis**: Combining role handoff framing with deep lifecycle prose (each phase gets its
own goal statement, role owner, and gate rationale) produces plans where gates are contextually
motivated rather than structurally required. The role-owner prose creates natural quantification
pressure: `">= 2 scout signals; PM has reviewed"` emerges from context, not from a rule.
Arc layers labeled by role in the YAML template satisfy C-14 while making the plan readable
by non-technical stakeholders.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It produces `program.yaml` -- a staged evidence-gathering plan where each phase is owned by
a role and gated on the artifacts the next role needs before starting their work. Skills remain
independently runnable. The program is optional sequencing scaffolding: it does not execute
skills, does not advance stages, and carries no automation authority. Its entire value is the
gate: a shared definition of what must be true before handoff.

---

You are running `/program:plan` for topic **{{topic}}**.

**The evidence arc -- four phases, four owners:**

**Phase 1 -- PM: Discovery**
*Goal*: establish what we know about the space before the Architect begins designing.
The PM runs scout and early prove skills to map the landscape: feasibility, market shape,
competitor approaches, requirements, compliance constraints.

*Gate guidance*: What does the Architect need to have in front of them before drafting the spec?
Name the artifacts. Quantify: `">= 2 scout signals reviewed; no blocking feasibility concerns"`.
Avoid: `"discovery complete"` -- the Architect cannot verify that.

**Phase 2 -- Architect + PM: Design**
*Goal*: produce a concrete approach the engineering team can validate.
The Architect drafts the spec and proposal; PM may contribute pitch or hypothesis framing.

*Gate guidance*: What do engineers need before expert review can begin?
`"draft-spec artifact present; Architect has confirmed no blocking feasibility gaps from discovery"`.

**Phase 3 -- Engineering: Validation**
*Goal*: stress-test the design against real-world signals.
Engineers run review, prove, flow, and trace skills. Review skills require the spec from Phase 2.
Flow and trace skills require review artifacts. Prove skills (prototype, interview, analysis)
belong here alongside review -- not after flow and trace.

*Gate guidance*: What does the team need before synthesis?
`"review-design and prove-prototype artifacts present; 0 P0 findings open; all blocking spec
comments resolved"`.

**Phase 4 -- Team: Synthesis**
*Goal*: listen ahead and close the evidence loop.
Listen and topic skills run last (before echo) because they synthesize across all prior signals.

*Gate guidance*: `"listen-feedback and listen-adoption artifacts present; no critical adoption blockers"`.

**Echo** (auto): always last. `name: echo`, `skills: []`, `auto: true`.

**BAD gate vs GOOD gate:**

| | Example | Why |
|--|---------|-----|
| BAD | `"Phase 3 complete"` | Names no artifact; "complete" is unverifiable |
| BAD | `"all reviews done"` | Execution state; next phase owner cannot check it |
| GOOD | `"review-design and prove-prototype present; 0 P0 findings open"` | Names artifacts; Architect can verify |

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog:**

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming,
  stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize,
  websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal>"

  stages:

  # ---- PM Phase: Discovery -- what we need to know before designing ----
  # PM owns; gate captures what the Architect needs before drafting

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifacts the Architect needs; numeric threshold: '>= N scout signals present'>"

  # ---- Architect+PM Phase: Design -- commit to a concrete approach ----
  # Architect+PM own; gate captures what engineering needs before validation

    - name: "<design-phase-label>"          # e.g. "design", "proposal"
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifacts engineers need; confirm Architect reviewed for blocking feasibility gaps>"

  # ---- Engineering Phase: Validation -- review, prove, simulate, trace ----
  # Engineering owns; review:* requires draft:spec | prove:* here | flow:*/trace:* last in layer

    - name: "<expert-review-phase-label>"   # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"  # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ---- Team Phase: Synthesis -- listen ahead, close the loop ----
  # Full team owns; runs after engineering validation

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- always last, do not move ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state -- not execution state
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels (not namespace names, not generic indices)
- [ ] Four role-phase comments (PM / Architect+PM / Engineering / Team) preserved in YAML

---

## V-05 -- Golden Synthesis (all 15 criteria)

**Axes**: All -- inertia contrast, role sequence for arc labels, discovery register for gate
guidance, pre-printed arc-labeled template with REQUIRED preserve comment and pre-printed
checklist, not-executor as opening identity, quantified gate requirement
**Hypothesis**: A prompt that (1) opens with not-executor identity (C-12, C-15 site 1),
(2) shows a labeled BAD/GOOD YAML contrast (C-10), (3) uses invitation register for gate
guidance (C-04, C-09 depth), (4) pre-prints the output template with REQUIRED preserve comment
(C-15 site 2), three arc layer dividers (C-14), and verification checklist (C-13), achieves
all 15 v19 criteria in a single cohesive body. This is the R3 golden candidate.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills listed
here still run standalone -- the plan does not execute them, does not advance stages, and carries
no automation authority. This identity is the plan's value: it tells you what evidence must exist
before handing off to the next phase, not what to run. A plan without gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The inertia pattern -- what you're replacing:**

```yaml
# BAD: flat list, one meaningless gate
program:
  topic: "{{topic}}"
  stages:
    - name: "all-work"
      skills:
        - scout:feasibility
        - scout:requirements
        - draft:spec
        - review:design
        - flow:lifecycle
        - trace:request
        - listen:feedback
      gate: "done"        # execution state: when is "done" done?
    - name: echo
      skills: []
      auto: true
```

Problems: skills run out of dependency order (you cannot review a spec that does not exist);
one gate covers everything but names no evidence; `"done"` is unverifiable. Nobody knows when
it's safe to advance.

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc, artifact-referencing gates, dependency order preserved
program:
  topic: "{{topic}}"
  stages:

  # Layer 1: Breadth -- establish what we know before designing
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      gate: "scout-feasibility, scout-requirements, and scout-competitors artifacts present;
             >= 2 scout signals reviewed by PM; no blocking feasibility concerns"

  # Layer 2: Depth -- design, validate, simulate
    - name: design
      skills:
        - draft:spec
        - draft:proposal
      gate: "draft-spec artifact present; Architect has confirmed no blocking gaps"

    - name: expert-review
      skills:
        - review:design
        - review:users
        - prove:prototype
      gate: "review-design, review-users, prove-prototype artifacts present; 0 P0 findings open"

  # Layer 3: Synthesis -- listen ahead, close the loop
    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: echo
      skills: []
      auto: true
```

Key distinctions from the bad pattern: skills ordered by dependency; each gate names artifacts
the next phase owner needs; one gate is quantified (`>= 2 scout signals`); three arc layers
make the investigation strategy visible.

---

**Gate design -- what does readiness look like for each phase?**

For each stage, ask: *what must exist before the next phase owner can begin their work?*

| Gate quality | Example | Passes? |
|-------------|---------|---------|
| Execution state | `"all scout complete"` | NO -- names what was done, not what exists |
| Empty or vague | `"done"` / `""` | NO -- unverifiable by next phase owner |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals present AND draft-spec artifact exists"` | YES + C-09 |

Require at least one quantified gate. Numeric thresholds make gates machine-checkable in
principle and signal deliberate evidence design.

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`. `prove:*` belongs
in or before the review/prove layer, not after flow/trace.

**Signal skill catalog:**

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming,
  stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize,
  websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output exactly -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim with each box checked:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ---- Layer 1: Breadth -- scout the space, draft the artifact ----
  # Goal: establish what we know before committing to a design

    - name: "<breadth-phase-label>"         # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>                     # add/remove as topic warrants
      gate: "<what the design phase needs; numeric threshold: '>= N scout signals present'>"

    # Optional second breadth stage -- remove if not needed
    - name: "<breadth-phase-2-or-remove>"
      skills:
        - draft:<skill>                     # early structural artifact: pitch or hypothesis
      gate: "<artifact condition>"

  # ---- Layer 2: Depth -- design, review, prove, simulate ----
  # Goal: commit to an approach and validate it against evidence
  # review:* requires draft:spec from Layer 1 | prove:* belongs here | flow:*/trace:* last

    - name: "<depth-phase-label>"           # e.g. "design", "proposal"
      skills:
        - draft:<skill>                     # draft:spec, draft:proposal
      gate: "<artifact condition; at least ONE gate across the plan must be quantified>"

    - name: "<depth-phase-2-label>"         # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                    # review:design, review:users, review:customers...
        - prove:<skill>                     # prove:prototype, prove:analysis, prove:interview...
      gate: "<review/prove artifacts present; P0 threshold: '0 P0 findings open'>"

    # Optional simulation stage -- add if flow/trace signals needed; remove otherwise
    - name: "<simulation-or-remove>"
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ---- Layer 3: Synthesis -- listen ahead, close the evidence loop ----
  # Goal: confirm what users and adopters signal; narrative close

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                    # listen:adoption, listen:feedback, listen:support
        - topic:<skill>                     # topic:plan, topic:report, topic:story...
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- required, always last, do not move ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state (artifact exists, signal present) -- not execution state
- [ ] At least one non-echo gate contains a numeric threshold (e.g., `>= 2 scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels (not namespace names, not `stage1`, not generic indices)
- [ ] Three arc-layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved in YAML
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output

---

## Predicted v19 Scores

| Variation | C-10 | C-12 | C-13 | C-14 | C-15 | Predicted score |
|-----------|------|------|------|------|------|-----------------|
| V-01 Role Sequence | FAIL (no contrast) | PASS | PASS | PASS (role labels) | PASS | ~96/100 |
| V-02 Phrasing Register | FAIL (no contrast) | PASS | PASS | PASS | PASS | ~96/100 |
| V-03 Inertia Framing | PASS | PASS | PASS | PASS | PASS | ~100/100 |
| V-04 Role+Lifecycle | PASS | PASS | PASS | PASS | PASS | ~100/100 |
| V-05 Golden | PASS | PASS | PASS | PASS | PASS | ~100/100 |

**V-01 and V-02 expected to fail C-10 by design** -- single-axis; contrast deliberately omitted
to isolate role sequence and phrasing register axes respectively.

**V-03, V-04, V-05 predicted golden** under v19.
