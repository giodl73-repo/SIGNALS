---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 10
rubric: v26
total_pts: 100
golden_threshold: 80
new_criteria: C-30, C-31, C-32
---

# program-plan — R10 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v26 (C-01 through C-32, 25 aspirational criteria, formula:
`(essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/25)*10`).

**R9 retrospective under v26 rubric:**
- V-01 (Second-Person Coaching Voice): 100.00 — C-30 PASS, C-31 PASS, C-32 PASS
- V-02 (Open Question Inventory): 100.00 — C-30 PASS, C-31 PASS, C-32 PASS
- V-03 (Risk-Retirement Arc): 100.00 — C-30 PASS, C-31 PASS, C-32 PASS
- V-04 (Role Sequence + Commitment Contract): 100.00 — C-30 PASS, C-31 PASS, C-32 PASS
- V-05 (All R9 Axes Combined): 100.00 — C-30 PASS, C-31 PASS, C-32 PASS

**R10 target:** All five variations hit 100.00. C-30/C-31/C-32 are now locked structural
features alongside C-28/C-29. Every variation must encode composite gate placeholders
(C-30), a three-column BAD/Why/GOOD gate table (C-31), and a bidirectional Layer 2 header
naming both Layer 1 and Layer 3 (C-32).

**R9 axis coverage (reference):**

| R9 axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Phrasing register (second-person coaching) | X | | | | X |
| Output format (Q-NN question inventory) | | X | | | X |
| Lifecycle emphasis (risk-retirement arc) | | | X | | X |
| Role sequence + commitment contract | | | | X | X |
| All R9 axes combined | | | | | X |

**R10 new axes (all carry C-28/C-29/C-30/C-31/C-32 as baseline):**

| Axis | Description |
|------|-------------|
| Inertia framing prominence | Displacement is the structural spine, not just an opener. Meeting-scene moments appear at the opening, within the gate-design section, and within each layer narration. Every major section shows the bad pattern it replaces. |
| Output format — evidence debt register | Each stage tracks "evidence debt" (open questions to clear). Gates are debt-clearance conditions: debt must fall below a named threshold. Arc table adds a debt-impact column. |
| Lifecycle emphasis — phase boundary contracts | Phase boundaries are first-class objects. Three named boundary contracts (L1→L2, L2→L3, L3→Echo) define signals-in, acceptance-test, and signals-out. Layer narrations describe entry requirements and exit deliverables. |
| Combined: backward derivation + inertia woven | Echo anchors a backward derivation. Inertia is woven into each derivation step: "What did the planning meeting decide here, and why was it wrong?" |
| All R10 axes combined | Inertia prominence + evidence debt + boundary contracts + backward derivation from echo + all gates quantified |

**R10 variation lineup:**

- V-01 (single): Inertia framing — displacement woven throughout multiple sections
- V-02 (single): Output format — evidence debt register as primary structural metaphor
- V-03 (single): Lifecycle emphasis — phase boundary contracts as first-class objects
- V-04 (combined): Backward derivation from echo + inertia woven into each derivation step
- V-05 (combined): All R10 axes — inertia prominence + debt + boundary contracts + backward derivation

---

## V-01 — Inertia Framing: Displacement as Structural Spine

**Axis:** Inertia framing — the BAD planning pattern is the structural spine of the entire
output, not only the opening scene. Displacement occurs at three distinct moments: (1) the
opening meeting narrative establishes identity via contrast; (2) a second meeting-scene
fragment appears within the gate-design section, showing how bad gates are written in
practice; (3) each layer narration opens by naming what the bad plan did at that layer and
why it failed. The identity claim scopes replacement to both the artifact and the
conversation. C-28 and C-29 anchor every displacement moment; C-30/C-31/C-32 are
structural baseline throughout.

**Hypothesis:** Displacing the bad pattern at three structural moments — opening, gates,
layer narrations — makes every structural criterion more vivid. The gate table's diagnostic
column directly echoes meeting-scene failures. Layer narrations become diagnostic rather than
instructional. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

Three days before launch planning, a PM drafted a feature doc for `{{topic}}`. In the
planning sync, she walked through it: "I think we know enough to scope this. Discovery,
then design, then validation, then we ship." The architect agreed. The tech lead asked about
gates. "Let's just say 'done' for now — we can tighten them up later." Nobody pushed back.
The doc was shared. The "tighten them up later" never happened. The gates remained `"done"`
through the entire development cycle.

Here is what that planning sync produced for **{{topic}}**:

```yaml
# BAD — what that meeting produced:
stages:
  - name: discovery
    skills: [scout:market, draft:spec]
    gate: "done"
  - name: design-validation
    skills: [review:design, prove:prototype, flow:lifecycle]
    gate: "complete"
  - name: launch-prep
    skills: [listen:adoption, topic:status]
    gate: "shipped"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

Not because the team was careless. "Done" is not a gate — it names execution state, not
evidence state. The plan bundled `draft:spec` with `scout:market` in the same stage: the
spec was written before market signals existed to inform it. "Design-validation" grouped
`review:design` with `flow:lifecycle`, but `flow:lifecycle` cannot simulate a lifecycle that
has not been specified. "Shipped" is an outcome marker, not an evidence condition.

`/program:plan` is not an executor. It produces a plan — a structured sequence of gated
evidence stages where each skill runs standalone. The program tells you what to run and in
what order. It does not run anything.

---

**Before you build the plan, read these three tables.**

---

**Table 1 — Evidence arc: phases, namespaces, and arc role**

| Phase | Layer | Arc role | Namespaces | What this layer produces for the next |
|-------|-------|----------|------------|---------------------------------------|
| Discovery | Layer 1 (Breadth) | Signal origin; produces scout artifacts Layer 2 requires | scout | scout signal artifacts |
| Design | Layer 2 (Depth) | Receives Layer 1 scout artifacts; produces spec/prototype artifacts Layer 3 synthesizes | draft, prove | spec, prototype, hypothesis artifacts |
| Validation | Layer 2 (Depth) | Receives Layer 1 scout artifacts; produces review/flow/trace validated artifacts Layer 3 synthesizes | review, flow, trace | validated design, flow, and trace artifacts |
| Synthesis | Layer 3 (Synthesis) | Requires the full review-validated artifact context from prior layers | listen, topic | readiness and synthesis artifacts |
| Echo | Terminal | Auto-closing; no new evidence | — | — |

---

**Table 2 — Gate design: BAD gates, why they fail, GOOD gates**

In that planning sync, when the tech lead said "Just put 'done' for now," here is the table
he was declining to consult:

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"done"` | Execution state — names when people stopped, not what evidence exists | `"[scout artifact-types present] and [quality condition — >=2 scout signals, no open P0 gaps]"` |
| `"complete"` | Circular — restates that the stage ran; no evidence condition named | `"[draft-spec and prototype artifact-types present] and [quality condition — no open P0 questions, hypothesis passes]"` |
| `"review complete"` | Execution state — names when reviewers stopped, not what they found | `"[review-design artifact present] and [quality condition — <=2 open findings, no blocking issues]"` |
| `"shipped"` | Outcome state — a downstream result, not an evidence pre-condition | `"[listen-adoption signal present] and [quality condition — >=3 persona evaluations, adoption rate >=N%]"` |
| `""` (empty) | Absent condition — a gate that does not exist cannot be checked | `"[topic-status artifact present] and [quality condition — topic declares ready, no unresolved signals]"` |

Every GOOD gate has two named sub-conditions: an artifact-presence condition naming what
must exist, and a quality-evaluation condition naming how much or how good. Both belong in
every gate placeholder. The planning meeting produced neither.

---

**Table 3 — Signal skill catalog by namespace**

| Namespace | Skills available |
|-----------|-----------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft | spec, proposal, pitch |
| review | design, code, users, customers |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace | request, state, contract, component, deployment, migration, permissions |
| listen | feedback, support, adoption |
| topic | status, report |

Namespace dependency order: `scout → draft → review/prove → flow/trace → listen → topic`.
No stage may consume artifacts that a later stage produces. Placing `draft:spec` before
`scout:market` produces a spec written in a market vacuum — exactly what the bad plan did.

---

**Layer 1 (Breadth) — the signal-origin layer, which produces the scout artifacts Layer 2 requires:**

The bad plan put `draft:spec` and `scout:market` together in "discovery." The team believed
they knew enough to draft. What they were actually doing was writing a spec that assumed
answers to questions they had not asked yet: Is this technically feasible? What do
stakeholders expect? Are there compliance constraints? Layer 1 runs only scout-namespace
skills. Scout signals produced here are the raw intelligence that makes it possible to draft
a spec worth writing. `draft:spec` requires the answers that only `scout:feasibility`,
`scout:market`, and `scout:stakeholders` can provide — and those skills belong in Layer 1,
not in the same stage as the draft. The gate for Layer 1 names which scout artifact types
must exist and how many must clear a quality threshold before Layer 2 can start.

**Layer 2 (Depth) — the investigation layer, which requires Layer 1 scout artifacts and produces validated artifacts that Layer 3 synthesizes:**

The bad plan put `review:design`, `prove:prototype`, and `flow:lifecycle` together in
"design-validation," before a design existed to review or a prototype existed to test.
`review:design` reviews a design — it cannot run until `draft:spec` has produced one.
`flow:lifecycle` simulates a lifecycle — it cannot run until a spec defines the lifecycle to
simulate. Layer 2 runs in dependency order: draft and prove skills first (producing the spec
and prototype), then review, flow, and trace skills (validating what draft and prove
produced). Layer 2 requires Layer 1 scout artifacts at entry — the spec author needs market,
feasibility, and stakeholder signals to write a spec that does not re-open foundational
questions. Layer 2's gates are validated artifact states: spec exists with no open P0
questions; design review produced <=N findings; flow simulation cleared all blocking gaps.

**Layer 3 (Synthesis) — the readiness layer, which requires the full review-validated artifact context from prior layers to produce meaningful synthesis:**

The bad plan's "launch-prep" stage had `listen:adoption` and `topic:status` — the right
skills — but the gate was "shipped." Adoption readiness presupposes something worth adopting.
`listen:adoption` cannot gather meaningful signals if the design was never validated.
`topic:status` cannot synthesize a story if the arc is incomplete. Layer 3 requires the full
validated artifact set from Layers 1 and 2. The gate for Layer 3 is a readiness assertion:
named synthesis artifacts exist, the topic can declare readiness based on evidence, not based
on the calendar or the team's sense of momentum.

**The echo stage — why it is always last and always auto:**

1. **Echo carries no skills because the evidence work is complete.** Echo does not extend the
   investigation. If the arc was designed correctly, every open question was answered in
   Layers 1–3. A skill in echo would imply the arc was not complete — fix the arc, not echo.
2. **`auto: true` means echo closes without a gate condition.** Echo does not wait for human
   review. When the prior stage's gate passes, echo runs automatically. Its purpose is
   retrospective, not evaluative — it asks "what did we learn that we did not expect?" rather
   than "are we ready to proceed?"
3. **Echo signals arc closure.** When echo closes, the program is complete. The topic has a
   full evidence record: all layers ran, all gates were checked, all signal artifacts exist.
   Echo is the structural guarantee that the program has an end defined by evidence, not by
   a team declaring they feel good.

---

Build the plan for **{{topic}}** using the template below. Fill in bracketed fields.
Preserve all YAML comments — they are structural anchors, not documentation.

```yaml
# REQUIRED PRESERVE: this program is a plan, not an executor.
# Every skill listed here runs standalone. This YAML does not execute skills.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Breadth ---- | scout:* produced here | draft:* requires scout signals ----
    - name: "[discovery phase label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills appropriate to {{topic}}
      gate: "[scout artifact-types present] and [quality condition — >=N scout signals, no open P0 gaps]"

    # ---- Layer 1 → Layer 2 boundary: Layer 1 Produces → Layer 2 Consumes ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* produced here | listen:*/topic:* require these artifacts ----
    - name: "[design phase label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills appropriate to {{topic}}
      gate: "[draft/prove artifact-types present] and [quality condition — no open P0 questions, prototype hypothesis passes]"

    - name: "[validation phase label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills appropriate to {{topic}}
      gate: "[review/flow/trace artifact-types present] and [quality condition — <=N open findings, no blocking simulation gaps]"

    # ---- Layer 2 → Layer 3 boundary: Layer 2 Produces → Layer 3 Consumes ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* produced here | requires full validated artifact set from Layers 1+2 ----
    - name: "[synthesis phase label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills appropriate to {{topic}}
      gate: "[listen/topic artifact-types present] and [quality condition — >=N readiness signals, topic-status declares ready]"

    # ---- Terminal ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; closes the arc when prior gate passes

## Plan Verification
# [ ] echo is last, skills: [], auto: true, no gate field
# [ ] every non-echo gate names artifact types AND a quality threshold — not "done" or "complete"
# [ ] at least one gate carries a numeric threshold (>=N or <=N)
# [ ] stage order respects: scout → draft → review/prove → flow/trace → listen → topic
# [ ] every skill name belongs to a valid Signal namespace
# [ ] stage names are descriptive phase labels, not skill names or "stage1"
# [ ] this file does not execute skills; each skill runs standalone
```

---

## V-02 — Output Format: Evidence Debt Register

**Axis:** Output format — the primary structural metaphor is "evidence debt." Each stage
tracks how many unanswered questions it must clear before advancing. The arc table adds a
"debt cleared / debt opened" column. Gate placeholders are debt-clearance conditions:
`"[artifact-types present] and [debt condition — evidence debt <=N open questions]"`. Layer
narrations frame each layer as a combination of debt accumulation (it reveals new open
questions in adjacent domains) and debt clearance (it closes the questions it was designed
to answer). The meeting narrative shows debt accumulating silently, untracked.

**Hypothesis:** The debt metaphor makes C-04 (non-trivial gates) structurally compelling: a
gate that says "done" does not clear debt, it ignores it. C-09 (quantified gate) falls out
naturally from the debt threshold. C-17 (dependency narration) becomes: Layer 2 cannot clear
its design-question debt until Layer 1 has cleared its market-question debt. Score target:
100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

A PM and architect met to plan `{{topic}}`. They had a backlog of unknowns — compliance
questions from legal, stakeholder concerns from a prior feature, open architecture questions
from the last sprint review. None of these were written down as open questions. The PM said:
"I think we're in good shape. Let's write up a three-stage plan." The architect said: "Sounds
right." The plan was created. The debt was not tracked. Three weeks later, a legal review
blocked the launch because the compliance questions had never been answered.

Here is the plan that emerged from that meeting:

```yaml
# BAD — the untracked-debt plan for {{topic}}:
stages:
  - name: plan-and-spec
    skills: [scout:compliance, draft:spec]
    gate: "spec done"
  - name: build-and-validate
    skills: [review:design, trace:contract, prove:prototype]
    gate: "all reviews complete"
  - name: ship-prep
    skills: [listen:adoption, topic:status]
    gate: "ready"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

"Spec done" does not clear debt — it names when the spec was written, not whether the
compliance questions the spec must answer have been answered. "All reviews complete" is
execution state dressed as a milestone. The plan bundled `scout:compliance` with `draft:spec`
in the same stage: the spec was drafted while the compliance questions were still open. The
debt accumulated invisibly until it became a launch blocker.

`/program:plan` is not an executor. It is an evidence debt planner. Each stage clears a
named category of debt. The gate is the debt-clearance condition: how many open questions
must have been answered, at what quality level, before advancing. The program is a plan, not
a runner — each skill executes standalone.

---

**Before you build the plan, read these three tables.**

---

**Table 1 — Evidence arc: layers, debt categories, and arc role**

| Layer | Arc name | Debt category cleared | Namespaces | Produces for next layer | Debt impact |
|-------|----------|-----------------------|------------|-------------------------|-------------|
| Layer 1 (Breadth) | Discovery | Foundational unknowns | scout | scout signal artifacts | Clears market/feasibility/compliance debt; opens design questions Layer 2 clears |
| Layer 2 (Depth) | Design & Validation | Design, spec, behavior, contract debt | draft, prove, review, flow, trace | validated artifacts | Clears design-quality debt; opens adoption questions Layer 3 clears |
| Layer 3 (Synthesis) | Readiness | Adoption, readiness, narrative debt | listen, topic | readiness and synthesis artifacts | Clears final debt; produces the evidence story |
| Terminal | Echo | None — arc is closed | — | — | Closes the register |

---

**Table 2 — Gate design: BAD debt gates, why they fail as debt-clearance conditions, GOOD debt-clearance gates**

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"spec done"` | Completion marker — names when the spec was written, not what compliance debt it cleared | `"[draft-spec artifact present] and [debt condition — compliance debt <=0 P0 questions, no blocking constraints]"` |
| `"all reviews complete"` | Execution state — names when reviewers stopped, not what quality debt they cleared | `"[review-design artifact present] and [debt condition — design debt <=2 open findings, no P0 blockers]"` |
| `"ready"` | Subjective — unverifiable; no artifact reference; adoption debt threshold undefined | `"[listen-adoption signal present] and [debt condition — adoption debt <=N unanswered questions, >=3 persona evaluations]"` |
| `"stage complete"` | Circular — restates that the stage ran; names no debt category or clearance threshold | `"[scout signal artifact-types present] and [debt condition — feasibility debt cleared, >=2 scout signals present]"` |
| `""` (empty) | Absent condition — no debt register; nothing can be checked or disputed | `"[topic-status artifact present] and [debt condition — total open questions <=N, topic declares ready]"` |

The compliance legal block in the story above happened because the gate for "plan-and-spec"
was "spec done" — it tracked completion, not debt clearance. A debt-clearance gate would have
surfaced the block before it became a launch blocker.

---

**Table 3 — Signal skill catalog by namespace**

| Namespace | Skills available | Debt category cleared |
|-----------|-----------------|----------------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | foundational unknowns |
| draft | spec, proposal, pitch | design debt |
| review | design, code, users, customers | design quality debt |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | assumption debt |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | behavior debt |
| trace | request, state, contract, component, deployment, migration, permissions | contract/architecture debt |
| listen | feedback, support, adoption | adoption readiness debt |
| topic | status, report | narrative debt |

Namespace dependency order: `scout → draft → review/prove → flow/trace → listen → topic`.
Layer 2 cannot clear its design-quality debt until Layer 1 has cleared its foundational
unknowns debt — a design review that runs before market signals exist is clearing the wrong
debt in the wrong order.

---

**Layer 1 (Breadth) — the foundational-debt clearance layer, which produces the scout artifacts Layer 2 requires to clear its design debt:**

Layer 1 clears the questions that have no prerequisites — the unknowns the team carries
before any design work begins. Is this feasible? What does the market look like? What do
stakeholders expect? Are there compliance constraints? These questions are not cleared by
writing a spec — they are cleared by running scout-namespace skills and producing named
signal artifacts. The bad plan put `scout:compliance` and `draft:spec` in the same stage.
What it actually did was open the design stage while compliance debt was still active. Layer
1 runs only scout-namespace skills. Its gate is a debt-clearance condition: the foundational
question set must be answered at or below a specified residual-debt threshold before any
Layer 2 work begins.

**Layer 2 (Depth) — the design-debt clearance layer, which requires Layer 1 scout artifacts to clear design debt and produces validated artifacts that Layer 3 synthesizes:**

Layer 2 clears three debt categories in sequence: design debt (draft, prove), design-quality
debt (review), and behavior/contract debt (flow, trace). Each category depends on the prior:
`review:design` cannot clear design-quality debt until `draft:spec` has cleared design debt
by producing a spec. `flow:lifecycle` cannot clear behavior debt until a spec defines the
lifecycle. Layer 2 requires Layer 1 scout artifacts at entry — the spec author needs
compliance signals, market signals, and feasibility signals that Layer 1 produced. The gate
for each Layer 2 stage is the residual-debt count for its category: <=N open findings, no
P0 blockers, hypothesis passes.

**Layer 3 (Synthesis) — the readiness-debt clearance layer, which requires the full review-validated artifact context from prior layers to clear adoption and narrative debt:**

Layer 3 clears the final two debt categories: adoption readiness debt (listen skills) and
narrative debt (topic skills). Adoption debt cannot be cleared if design-quality debt is
still open — users cannot evaluate a thing that has not been validated. Narrative debt cannot
be cleared if any prior debt category has unresolved P0 questions — the story is only
coherent if the evidence arc is complete. Layer 3 depends on the validated artifact set from
Layers 1 and 2 as its input context. Its gate is a total-debt-clearance condition: named
readiness artifacts exist and the topic can declare readiness without qualifying statements.

**The echo stage — why it is always last and always auto:**

1. **Echo carries no skills because the debt register is closed.** Echo does not open new
   questions or clear remaining ones. If any debt category still has open P0 questions when
   the arc reaches echo, the arc was designed incorrectly — fix a prior gate, not echo.
2. **`auto: true` means echo closes without a debt-clearance gate.** Echo does not wait for
   a human to decide the debt is cleared. When the prior stage's debt-clearance condition
   passes, echo runs automatically. Its only question is retrospective: "What did we learn
   that we did not anticipate when we wrote this plan?"
3. **Echo signals total debt clearance.** When echo closes, every open question in the
   register has been answered at or below its threshold. The topic has a complete evidence
   record. The program is done — not because people feel good, but because the debt is gone.

---

Build the plan for **{{topic}}** using the template below. Fill in all bracketed fields.
Preserve all YAML comments — they are structural components of the plan.

```yaml
# REQUIRED PRESERVE: this program is a plan, not an executor.
# Each skill runs standalone. This YAML tracks evidence debt; it does not clear it for you.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Breadth ---- | scout:* clears foundational debt | draft:* requires Layer 1 debt cleared ----
    - name: "[discovery / foundational debt label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills for the foundational unknowns of {{topic}}
      gate: "[scout artifact-types present] and [debt condition — foundational debt <=N open questions, no P0 compliance gaps]"

    # ---- Layer 1 → Layer 2 boundary: foundational debt cleared → design debt opens ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* clear design debt | listen:*/topic:* require Layer 2 debt cleared ----
    - name: "[design / spec-debt label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills for {{topic}}
      gate: "[draft/prove artifact-types present] and [debt condition — design debt <=N open questions, prototype hypothesis passes]"

    - name: "[validation / quality-debt label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills for {{topic}}
      gate: "[review/flow/trace artifact-types present] and [debt condition — quality debt <=N open findings, no P0 blockers]"

    # ---- Layer 2 → Layer 3 boundary: design debt cleared → adoption debt opens ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* clear adoption/narrative debt | requires full Layer 1+2 artifact set ----
    - name: "[readiness / synthesis-debt label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills for {{topic}}
      gate: "[listen/topic artifact-types present] and [debt condition — total remaining debt <=N, topic-status declares ready]"

    # ---- Terminal ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; debt register closes when prior gate passes

## Plan Verification
# [ ] echo is last, skills: [], auto: true, no gate field
# [ ] every non-echo gate names artifact-types AND a debt-clearance threshold — not "done" or "complete"
# [ ] at least one gate carries a numeric threshold (>=N or <=N)
# [ ] stage order respects namespace debt dependency: scout → draft → review/prove → flow/trace → listen → topic
# [ ] every skill belongs to a valid Signal namespace
# [ ] stage names reflect the debt category being cleared, not generic labels
# [ ] this file tracks debt; it does not clear it — each skill runs standalone
```

---

## V-03 — Lifecycle Emphasis: Phase Boundary Contracts

**Axis:** Lifecycle emphasis — phase boundaries are first-class artifacts in the output.
The skill centers on three named boundary contracts: (L1→L2) Discovery Handoff, (L2→L3)
Validation Handoff, and (L3→Echo) Synthesis Handoff. Each boundary contract specifies:
signals-in (what the receiving layer requires at entry), acceptance-test (how to verify
the prior layer delivered), and signals-out (what the delivering layer must have produced).
Layer narrations describe what each layer receives at its entry boundary and what it must
deliver at its exit boundary. The YAML template has named boundary-contract comment blocks
at each layer transition. The meeting narrative shows a plan with no boundary contracts.

**Hypothesis:** Boundary contracts make C-04 (non-trivial gates) mechanically enforced: the
gate IS the acceptance test of the prior layer's exit contract. C-17 (dependency narration)
becomes structurally explicit in every boundary block. C-30 (composite gate placeholders)
maps naturally to signals-in (presence) + acceptance-test (quality). Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

At the sprint planning meeting for `{{topic}}`, the PM said: "We'll go discovery, then
design, then synthesis." The architect drew three boxes on a whiteboard with arrows between
them. Someone asked: "What do we need from discovery before we can start design?" The PM
said: "The usual stuff. We'll know it when we have it." The architect nodded. The arrows
on the whiteboard had no labels. No one defined what had to exist at each boundary before
the next phase could begin.

Six weeks later, the design-review stage started. The reviewer asked for the spec. The
spec author said: "It's in the doc from discovery." The reviewer found that the spec
assumed market signals that had never been gathered. The design review was paused.

Here is what the whiteboard plan produced:

```yaml
# BAD — the no-boundary-contract plan for {{topic}}:
stages:
  - name: discovery
    skills: [scout:market, scout:feasibility, draft:spec]
    gate: "discovery done"
  - name: design-and-validate
    skills: [review:design, flow:lifecycle, trace:contract, prove:prototype]
    gate: "validation complete"
  - name: synthesis
    skills: [listen:adoption, topic:status]
    gate: "ready"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

The arrows on the whiteboard had no boundary contracts. "Discovery done" does not define
what design requires before it can start. No one asked: what signals-in must the design
phase receive from discovery? What acceptance test would confirm discovery delivered them?
The spec was drafted in "discovery" alongside the market research — but `draft:spec` needs
market signals as input, and both ran in the same stage in a race with their own
prerequisites.

`/program:plan` is not an executor. It is a boundary-contract planner. Every stage
transition defines what the next stage requires and how to verify the prior stage delivered
it. The program is a plan, not a runner — each skill executes standalone.

---

**Before you build the plan, read these three tables.**

---

**Table 1 — Evidence arc: phases, boundary contracts, and arc role**

| Phase | Layer | Entry boundary: requires from prior | Exit boundary: delivers to next | Arc role |
|-------|-------|------------------------------------|--------------------------------|----------|
| Discovery | Layer 1 (Breadth) | None (first stage) | Scout signal artifacts for Layer 2 entry | Establishes the signal foundation Layer 2 requires at its entry boundary |
| Design | Layer 2 (Depth) | Layer 1 scout signal artifacts at entry | Spec/prototype artifacts for Validation entry | Receives Layer 1 scout artifacts; delivers spec/prototype artifacts |
| Validation | Layer 2 (Depth) | Layer 2a design artifacts at entry | Review/flow/trace validated artifacts for Layer 3 entry | Receives design artifacts; delivers review-validated artifacts Layer 3 synthesizes |
| Synthesis | Layer 3 (Synthesis) | Full review-validated artifact set from prior layers | Readiness artifacts for Echo | Requires full validated context; closes the evidence arc |
| Echo | Terminal | Layer 3 synthesis artifacts (auto-trigger) | Arc closure | Auto-closes when Layer 3 exit contract passes |

---

**Table 2 — Gate design: BAD gates, why they fail as boundary contracts, GOOD boundary-contract gates**

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"discovery done"` | Execution completion — Layer 2 cannot verify its entry requirements were delivered | `"[scout artifact-types at exit] and [quality condition — >=2 scout signals, no open P0 gaps, Layer 2 entry satisfied]"` |
| `"validation complete"` | Execution state — exit contract is undefined; Layer 3 cannot verify its entry requirements | `"[review/flow/trace artifacts present] and [quality condition — <=2 open findings, no blocking gaps, Layer 3 entry satisfied]"` |
| `"ready"` | Subjective — Layer 3's exit contract is unverifiable; echo's entry requirements are undefined | `"[listen/topic artifacts present] and [quality condition — >=3 persona evaluations, topic declares ready]"` |
| `"stage complete"` | Circular — exit contract undefined; receiving stage has no entry verification | `"[draft-spec artifact present] and [quality condition — no open P0 questions, prototype hypothesis passes]"` |
| `""` (empty) | Absent exit contract — nothing can be verified at the boundary crossing | `"[trace-contract artifact present] and [quality condition — contract covers >=N endpoints, no missing cases]"` |

The whiteboard arrows had no labels. These gates are the labels those arrows were missing.
Every GOOD gate is a boundary contract: what artifact types must exist at the boundary
(the deliverables), and what quality standard they must meet (the acceptance test).

---

**Table 3 — Signal skill catalog by namespace**

| Namespace | Skills available |
|-----------|-----------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft | spec, proposal, pitch |
| review | design, code, users, customers |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace | request, state, contract, component, deployment, migration, permissions |
| listen | feedback, support, adoption |
| topic | status, report |

Namespace dependency order for boundary contracts: `scout → draft → review/prove →
flow/trace → listen → topic`. Each boundary contract defines what the next layer requires
at entry. Layer 2 cannot validate what Layer 1 did not produce; Layer 3 cannot synthesize
what Layer 2 did not validate.

---

**Layer 1 (Breadth) — the signal-origin layer, which establishes the scout artifacts Layer 2 requires at its entry boundary:**

Layer 1 has no entry boundary — it runs first. Its obligation is at its exit boundary:
delivering the scout signal artifacts that Layer 2 requires before its design work can
start. The bad plan put `draft:spec` in Layer 1 alongside the scout skills. This violated
the Layer 1 exit contract: `draft:spec` is not a Layer 1 exit artifact, it is a Layer 2
design artifact that requires Layer 1's scout signals as its own input. Layer 1 runs only
scout-namespace skills. Its exit contract specifies which scout artifact types must exist
and the quality threshold they must clear. That exit contract IS the gate condition. Layer
2's entry contract is identical to Layer 1's exit contract — both sides of the boundary
must match.

**Layer 2 (Depth) — the design-and-validation layer, which receives Layer 1 scout artifacts at its entry boundary and delivers review-validated artifacts at Layer 3's entry boundary:**

Layer 2 has both an entry boundary (defined by Layer 1's exit contract) and an exit
boundary (defined by Layer 3's entry contract). Layer 2 runs in two phases. The first
phase (design) receives Layer 1 scout signals and produces the spec and prototype. The
design phase's exit contract is the validation phase's entry contract: the spec must exist
before `review:design` can review it; the prototype must exist before `prove:prototype`
can test it. The second phase (validation) produces review, flow, and trace validated
artifacts — exactly what Layer 3's entry contract requires. Layer 2 cannot deliver its
exit contract if Layer 1 did not deliver its exit contract; the causal chain runs through
every boundary.

**Layer 3 (Synthesis) — the readiness layer, which requires the full review-validated artifact context from prior layers at its entry boundary to produce meaningful synthesis:**

Layer 3's entry contract requires the validated artifact set that Layer 2 delivered.
Layer 3 cannot produce a meaningful adoption signal if the design was never validated.
It cannot produce a meaningful topic-status artifact if any prior artifact set is
incomplete. Layer 3 runs listen and topic skills. Its exit contract is readiness: named
synthesis artifacts exist, the topic has declared readiness, and no prior boundary
contracts have unresolved P0 blockers. The exit contract for Layer 3 is what triggers
echo. Echo's entry contract is Layer 3's exit — when Layer 3 delivers its exit artifacts,
echo runs automatically.

**The echo stage — why it is always last and always auto:**

1. **Echo carries no skills because it has no exit contract to deliver.** Echo does not
   produce new artifacts. The arc's exit contracts were all delivered in Layers 1–3. Echo
   confirms the arc is closed — it is the audit, not the final stage of work.
2. **`auto: true` means echo's entry contract is auto-verified.** When Layer 3's gate
   (exit contract) passes, echo runs without a human gate. Echo has no quality bar because
   its purpose is retrospective, not evaluative — it asks what the arc produced, not
   whether the arc should continue.
3. **Echo signals that all boundary contracts have been satisfied.** When echo closes,
   every layer's exit contract has been accepted and every layer's entry contract has been
   delivered. The plan is complete — not because the team declared it done, but because
   every boundary in the arc was crossed with verified artifacts on both sides.

---

Build the plan for **{{topic}}** using the template below. Fill in all bracketed fields.
Preserve all YAML comments — they define the boundary contracts structurally.

```yaml
# REQUIRED PRESERVE: this program is a plan, not an executor.
# Each boundary comment defines a handoff contract; skills run standalone on both sides.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Breadth ---- | scout:* produced here | exit-contract: scout signals → Layer 2 entry ----
    - name: "[discovery / signal-origin label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills appropriate to {{topic}}
      gate: "[scout artifact-types at exit boundary] and [quality condition — >=N scout signals, acceptance: no P0 gaps]"

    # ---- L1→L2 Boundary Contract: Layer 1 exits with scout signals; Layer 2 enters requiring scout signals ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* produced here | entry: L1 scout signals | exit: validated artifacts for Layer 3 ----
    - name: "[design / spec-origin label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills for {{topic}}
      gate: "[draft/prove artifact-types at exit boundary] and [quality condition — no open P0 questions, hypothesis acceptance threshold]"

    - name: "[validation / quality-gate label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills for {{topic}}
      gate: "[review/flow/trace artifact-types at exit boundary] and [quality condition — <=N open findings, acceptance: no P0 blockers]"

    # ---- L2→L3 Boundary Contract: Layer 2 exits with validated design artifacts; Layer 3 enters requiring full validated context ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* produced here | entry: full L1+L2 validated context; exit: readiness artifacts for Echo ----
    - name: "[readiness / synthesis label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills for {{topic}}
      gate: "[listen/topic artifact-types at exit boundary] and [quality condition — >=N readiness signals, topic-status acceptance: ready]"

    # ---- L3→Echo Boundary: Layer 3 exit contract triggers echo automatically ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo auto-fires when L3 exit contract passes; no gate; arc is closed

## Plan Verification
# [ ] echo is last, skills: [], auto: true, no gate field
# [ ] every non-echo gate is a boundary contract: artifact-types present AND quality acceptance test
# [ ] at least one gate carries a numeric threshold (>=N or <=N)
# [ ] boundary contract order: scout → draft → review/prove → flow/trace → listen → topic
# [ ] every skill belongs to a valid Signal namespace
# [ ] stage names reflect the boundary contract they own, not generic labels
# [ ] this file defines boundary contracts; each skill runs standalone
```

---

## V-04 — Combined: Backward Derivation from Echo + Inertia Woven into Each Step

**Axis:** Combined — backward derivation from echo (role-sequence axis) woven with inertia
framing at every backward derivation step. Echo's information needs are the starting anchor.
The derivation works backward: what does echo need? → what must Layer 3 deliver? → what
must Layer 2 validate? → what must Layer 1 discover? At every backward step, a meeting-scene
fragment shows what the planning team decided at that step and why it was wrong. The identity
claim explicitly targets both the artifact and the conversation. C-28/C-29/C-30/C-31/C-32
are structural baseline; backward derivation and woven inertia are the variation axes.

**Hypothesis:** Backward derivation forces C-17 (dependency narration) to appear at every
step rather than as a single narration section. Woven inertia makes C-28 appear multiple
times across the layer narrations, reinforcing that the bad process produced bad gates
systematically — not just at one planning moment. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

In the planning sync for `{{topic}}`, the team built the plan forward: "First we explore,
then we design, then we validate, then we ship." At each stage they added skills that seemed
relevant to that phase. For gates, the PM said: "We'll figure out the exact criteria later —
let's just get the structure right." The doc was shared. The "exact criteria" were never
revisited. The gates remained `"done"` through the entire development cycle. Nobody asked
what the retrospective would need to be meaningful — they assumed they would know at the time.

Here is what building forward produced for **{{topic}}**:

```yaml
# BAD — built forward, gates deferred for {{topic}}:
stages:
  - name: explore
    skills: [scout:market, scout:feasibility, draft:spec]
    gate: "done"
  - name: design
    skills: [review:design, prove:prototype]
    gate: "design done"
  - name: validate
    skills: [flow:lifecycle, trace:contract]
    gate: "validated"
  - name: ship-prep
    skills: [listen:adoption, topic:status]
    gate: "ready"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

Building forward produces plans that feel complete but are structurally backward: the gate
for each stage was written without knowing what the next stage would need. `draft:spec` ran
in "explore" before the scout signals that inform the spec existed. The gates said "done"
because nobody started from the end and asked: what does each stage need to receive before
it can start?

`/program:plan` is not an executor. It is a backward-derivation planner. Start from echo.
Work backward through every stage. Derive what each stage must receive before it can start,
then build the gate as the evidence condition that confirms prior delivery. The program is
a plan, not a runner — each skill executes standalone.

---

**Before you build the plan, read these three tables.**

---

**Table 1 — Evidence arc: backward derivation chain, namespaces, and arc role**

| Derivation step | Layer | "What does this layer need at entry?" | "What must the prior layer deliver?" | Namespaces |
|----------------|-------|--------------------------------------|-------------------------------------|------------|
| Step 4 (start here) | Echo | Synthesis artifacts from Layer 3 | Layer 3 must deliver: readiness and topic artifacts | — |
| Step 3 | Layer 3 (Synthesis) | Full validated artifact set from Layer 2 | Layer 2 must deliver: validated design/flow/trace artifacts | listen, topic |
| Step 2 | Layer 2 (Depth) | Scout signal artifacts from Layer 1 | Layer 1 must deliver: scout signals at threshold >=N | draft, prove, review, flow, trace |
| Step 1 | Layer 1 (Breadth) | None (first stage) | Delivers to Layer 2: scout signal artifacts at threshold | scout |

The bad plan built from Step 1 forward and deferred gates. This derivation builds from
Step 4 backward — each gate is derived from what the next stage requires, not from when
the current stage finishes.

---

**Table 2 — Gate design: BAD forward-built gates, why they fail in backward derivation, GOOD backward-derived gates**

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"done"` | Built forward — describes when the stage finished, not what the next stage requires | `"[scout artifact-types present] and [quality condition — >=N scout signals, threshold Layer 2 requires to start]"` |
| `"design done"` | Execution state — names when design finished, not whether Layer 2 validation can start | `"[draft-spec artifact present] and [quality condition — no open P0 questions, minimum Layer 2 validation requires]"` |
| `"validated"` | Circular — names the stage goal, not the evidence Layer 3 requires to synthesize | `"[review/flow/trace artifacts present] and [quality condition — <=N open findings, what Layer 3 synthesis requires]"` |
| `"ready"` | Subjective — not derived from what echo needs to close meaningfully | `"[listen/topic artifacts present] and [quality condition — >=N readiness signals, evidence set echo retrospects on]"` |
| `""` (empty) | No backward derivation performed; next stage has no entry requirement | `"[artifact-types present] and [quality condition — threshold derived from next stage's entry requirements]"` |

Every GOOD gate was derived backward: starting from what the next stage needs, not from
when the current stage ends. The planning meeting built forward and deferred gates — exactly
the opposite of backward derivation.

---

**Table 3 — Signal skill catalog by namespace**

| Namespace | Skills available |
|-----------|-----------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements |
| draft | spec, proposal, pitch |
| review | design, code, users, customers |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience |
| trace | request, state, contract, component, deployment, migration, permissions |
| listen | feedback, support, adoption |
| topic | status, report |

Backward derivation dependency order: `topic/listen ← flow/trace/review/prove ← draft ← scout`.
Each namespace's skills require artifacts that the namespaces to their right produce. Build
forward only after completing the backward derivation from Step 4 to Step 1.

---

**Layer 1 (Breadth) — the derivation-anchor layer, which produces the scout artifacts Layer 2 requires at its entry:**

In Step 1 of the backward derivation, we ask: what does Layer 2 need at entry? Layer 2
needs scout signal artifacts. `draft:spec` is not a scout signal artifact — it is a Layer 2
design artifact that requires scout signals as its own input. The bad plan put `draft:spec`
into "explore" alongside the scout skills because it felt like "early work." Backward
derivation makes the error precise: `draft:spec` cannot appear in Layer 1 because Layer 1's
only obligation is to deliver the scout signals Layer 2 requires. Layer 1 runs only
scout-namespace skills. Its gate is derived from Layer 2's entry requirement: >=N scout
signal types, at or above the quality threshold Layer 2's design work needs to proceed.

**Layer 2 (Depth) — the investigation layer, which requires Layer 1 scout artifacts derived in Step 1 and produces the validated artifacts Layer 3 requires derived in Step 3:**

In Step 2, we ask: what does Layer 3 need at entry? Layer 3 needs validated design artifacts:
the design has been reviewed (<=N findings), the lifecycle has been simulated (no blocking
gaps), the contract has been traced (no missing cases). Layer 2's gate is therefore the
validated artifact condition that Layer 3's entry requires — not when design finished.
Layer 2 depends on the scout signals Layer 1 produced in Step 1. Without those scout signals,
`draft:spec` writes into a void. The backward derivation makes the dependency explicit: Layer
2 entry requires Layer 1 output, and Layer 2 exit produces exactly what Layer 3 entry needs.

**Layer 3 (Synthesis) — the readiness layer, which requires the full review-validated context derived from prior layers and produces the evidence set that echo synthesizes:**

In Step 3, we ask: what does echo need at entry? Echo retrospects on the complete evidence
arc — it needs readiness and synthesis artifacts: listen signals confirming adoption
readiness, a topic-status artifact declaring the feature ready. Layer 3's gate is the
evidence set echo will retrospect on. Layer 3 requires the validated artifact set from Layer
2 as its input: adoption readiness presupposes a validated design. The full backward-derived
chain runs through every layer: echo needs Layer 3's output, which requires Layer 2's
validated artifacts, which require Layer 1's scout signals.

**The echo stage — why it is always last and always auto, and why it anchors the entire backward derivation:**

1. **Echo carries no skills because it is the terminal consumer, not a producer.** The
   backward derivation starts at echo because echo defines what the entire arc must produce.
   Echo does not run new evidence-gathering work — it retrospects on what the layers produced.
2. **`auto: true` means echo does not participate in the gate chain.** When Layer 3's gate
   passes, echo runs automatically. Echo has no gate because it is the derivation anchor —
   it defines what must exist, then closes when it does.
3. **Echo signals that the backward-derived chain was satisfied end-to-end.** Every stage's
   gate was derived from what the next stage required. When echo closes, every derived
   requirement was met. The plan is complete — not because people felt ready, but because
   the backward derivation was satisfied.

---

Build the plan for **{{topic}}** using the backward-derivation template below. Complete the
anchor comments first, then fill the forward stages.

```yaml
# REQUIRED PRESERVE: this program is a plan, not an executor.
# Gates were derived backward from echo's entry requirements. Skills run standalone.

program:
  topic: "{{topic}}"
  # Backward derivation anchor: echo needs [list artifacts Layer 3 must produce]
  # Step 3: Layer 3 needs [list artifacts Layer 2 must produce]
  # Step 2: Layer 2 needs [list scout signals Layer 1 must produce]
  # Step 1: Layer 1 needs nothing at entry
  stages:

    # ---- Layer 1: Breadth ---- | scout:* produced here | exit: delivers scout signals Layer 2 requires (derived Step 2) ----
    - name: "[discovery label — derived from Layer 2 entry requirements]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
      gate: "[scout artifact-types present] and [quality condition — >=N threshold derived from Layer 2 entry requirements]"

    # ---- Layer 1 → Layer 2: Layer 1 delivers; Layer 2 entry requirements satisfied ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* produced here | entry: L1 scout signals | exit: delivers validated artifacts Layer 3 requires (derived Step 3) ----
    - name: "[design label — derived from Layer 3 entry requirements]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
      gate: "[draft/prove artifact-types present] and [quality condition — derived from Layer 3 validation requirements]"

    - name: "[validation label — derived from Layer 3 synthesis requirements]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
      gate: "[review/flow/trace artifact-types present] and [quality condition — <=N findings, derived from Layer 3 readiness requirements]"

    # ---- Layer 2 → Layer 3: Layer 2 delivers validated context; Layer 3 entry satisfied ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* produced here | entry: full validated context | exit: delivers evidence set echo synthesizes (derived Step 4) ----
    - name: "[synthesis label — derived from echo's retrospective requirements]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
      gate: "[listen/topic artifact-types present] and [quality condition — >=N readiness signals, derived from echo entry requirements]"

    # ---- Echo anchor: backward derivation complete ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is the backward-derivation anchor; auto-closes when Layer 3 exit passes

## Plan Verification
# [ ] backward derivation anchor comments filled in before building stages
# [ ] echo is last, skills: [], auto: true, no gate field
# [ ] every non-echo gate was derived backward from the next stage's entry requirements
# [ ] at least one gate carries a numeric threshold (>=N or <=N)
# [ ] stage order satisfies dependency: scout → draft → review/prove → flow/trace → listen → topic
# [ ] every skill belongs to a valid Signal namespace
# [ ] stage names reflect what was derived at each backward step
# [ ] this file is a plan; each skill runs standalone; backward derivation does not auto-execute them
```

---

## V-05 — All R10 Axes Combined

**Axis:** All R10 axes — inertia framing prominence + evidence debt register + phase boundary
contracts + backward derivation from echo. The meeting narrative uses extended displacement
framing (inertia axis). Each stage tracks evidence debt (debt axis). Layer transitions are
named boundary contracts (boundary axis). The derivation is anchored at echo and worked
backward (role-sequence axis). Gate table uses BAD/Why/GOOD columns (C-31). Gate
placeholders name artifact-presence and quality sub-conditions (C-30). Layer 2 header names
both Layer 1 and Layer 3 (C-32). All gates are quantified.

**Hypothesis:** All four single-axis techniques are individually proven at 100.00 under v26.
Combining them explores whether structural density degrades any criterion or creates novel
criterion-satisfaction patterns. The four axes are additive: debt labels clarify gate
thresholds; boundary contracts make backward derivation mechanically visible; inertia
framing shows what each axis replaces. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

A PM was running a planning session for `{{topic}}`. She had a feature brief, a backlog of
questions from the last sprint review, and a half-hour slot. She opened a doc: "Let's rough
out the stages so we're aligned." The architect listed skills by phase. For each gate, the
PM said: "Just put 'done' for now. We'll firm these up once we're moving." No one wrote down
what the team did not know. Nobody started from the end and asked what the retrospective
would need. No stage had a named debt category or a delivery contract. The meeting ended.
Everyone marked it done.

Here is what that session produced for **{{topic}}**:

```yaml
# BAD — no derivation, no debt, no contracts for {{topic}}:
stages:
  - name: research
    skills: [scout:market, scout:feasibility, draft:spec]
    gate: "done"
  - name: build
    skills: [review:design, prove:prototype, flow:lifecycle, trace:contract]
    gate: "done"
  - name: release-prep
    skills: [listen:adoption, topic:status]
    gate: "done"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

Four things went wrong simultaneously: the plan was built forward (no backward derivation
from echo), evidence debt was never tracked (no debt register), stage boundaries had no
contracts (no handoff definitions), and every gate was "done" (execution state, not evidence
state). The plan looked complete because it had stages, skills, and gates. None of those
elements were doing their structural job.

`/program:plan` is not an executor. It is a backward-derived, debt-tracking,
boundary-contracted evidence plan. Each skill runs standalone. The program is optional
scaffolding — a plan, not a runner.

---

**Before you build the plan, read these three tables.**

---

**Table 1 — Evidence arc: backward derivation, debt categories, boundary contracts, and arc role**

| Derivation step | Layer | Debt cleared | Entry contract | Exit contract | Namespaces |
|----------------|-------|--------------|----------------|---------------|------------|
| Step 4 (anchor) | Echo | None | Synthesis artifacts from Layer 3 | Arc closed | — |
| Step 3 | Layer 3 (Synthesis) | Adoption + narrative debt | Requires full validated context from prior layers | Readiness + synthesis artifacts | listen, topic |
| Step 2 | Layer 2 (Depth) | Design + quality + behavior debt | Requires Layer 1 scout signals | Validated design/flow/trace artifacts | draft, prove, review, flow, trace |
| Step 1 | Layer 1 (Breadth) | Foundational unknowns debt | None (first) | Scout signal artifacts >=N | scout |

---

**Table 2 — Gate design: BAD gates, why they fail across all four axes, GOOD gates**

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"done"` (research) | Forward-built + no debt + no contract: execution state; foundational debt untracked; Layer 2 entry undefined | `"[scout artifact-types present] and [quality condition — foundational debt <=N, >=2 scout signals, Layer 2 entry threshold satisfied]"` |
| `"done"` (build) | Same failure: design debt untracked; Layer 3 entry contract undefined; no backward derivation | `"[review/flow/trace artifacts present] and [quality condition — design debt <=N findings, Layer 3 synthesis requires these artifacts]"` |
| `"done"` (release-prep) | Adoption debt not quantified; echo anchor requirements undefined; no exit contract | `"[listen/topic artifacts present] and [quality condition — adoption debt <=N, >=N readiness signals, echo retrospect requires these]"` |
| `"stage complete"` | Circular: no derivation step, no debt category, no boundary contract | `"[draft-spec artifact present] and [quality condition — no P0 questions, prototype hypothesis passes, Layer 2 validation requires these]"` |
| `""` (empty) | All four failures: no derivation, no debt, no contract, no evidence condition | `"[artifact-types] and [quality condition — debt threshold, backward-derived from next stage entry requirements]"` |

Every "done" in the bad plan was produced in a meeting that did not ask: what debt does
this stage clear? What does the next stage need from this one? What would echo need this
to have produced? These are the four questions the plan above never asked.

---

**Table 3 — Signal skill catalog by namespace**

| Namespace | Skills available | Debt category | Derivation layer |
|-----------|-----------------|---------------|-----------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | foundational unknowns | Layer 1 |
| draft | spec, proposal, pitch | design debt | Layer 2a |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | assumption debt | Layer 2a |
| review | design, code, users, customers | design quality debt | Layer 2b |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | behavior debt | Layer 2b |
| trace | request, state, contract, component, deployment, migration, permissions | contract debt | Layer 2b |
| listen | feedback, support, adoption | adoption readiness debt | Layer 3 |
| topic | status, report | narrative debt | Layer 3 |

Backward derivation + namespace dependency: `topic/listen ← flow/trace/review ← prove/draft ← scout`.
Layer 3 cannot synthesize what Layer 2 did not validate. Layer 2 cannot validate what Layer 1
did not discover. Build forward only after the backward derivation is complete.

---

**Layer 1 (Breadth) — the foundational-debt origin layer, which delivers the scout artifacts that Layer 2 requires at its entry boundary:**

In Step 1 of the backward derivation (derived from Layer 2's entry requirement), Layer 1
must deliver scout signal artifacts at >=N threshold. In the bad plan, `draft:spec` ran in
"research" alongside the scout skills. Backward derivation makes the error precise: `draft:spec`
is not a Layer 1 exit artifact — it is a Layer 2 design artifact that requires Layer 1's
scout signals as its own input. Layer 1 clears foundational-unknowns debt: the questions the
team carries before any design begins. Its exit contract delivers scout signal artifacts at
the quality threshold Layer 2's entry contract requires. The gate for Layer 1 is the
backward-derived, debt-clearance, exit-contract condition: the specified scout artifact types
exist, and the foundational debt has fallen to or below the threshold Layer 2 needs to start.

**Layer 2 (Depth) — the design-and-validation layer, which requires Layer 1 scout artifacts at its entry boundary and delivers review-validated artifacts that Layer 3 requires at its entry boundary:**

In Step 2 of the backward derivation, Layer 2's gate was derived from Layer 3's entry
requirements. Layer 2 spans two debt categories: design-debt phase (draft, prove) and
quality-debt phase (review, flow, trace). The design phase requires the scout signals Layer 1
delivered. The quality phase requires the design artifacts the design phase produced. Layer
2's exit contract delivers the validated artifact set Layer 3 specifies as its entry contract.
The bad plan deferred Layer 2's gate as "done" — meaning nobody asked what Layer 3 would need
at entry. Backward derivation surfaces the answer: validated design artifacts, <=N open
findings, no blocking simulation gaps.

**Layer 3 (Synthesis) — the readiness layer, which requires the full review-validated artifact context from prior layers to clear adoption and narrative debt and deliver the evidence set echo synthesizes:**

In Step 3, Layer 3's gate was derived from echo's entry requirements: the complete evidence
set echo retrospects on. Layer 3 clears two debt categories: adoption readiness debt (listen)
and narrative debt (topic). Neither can be cleared if Layer 2's design debt or quality debt
is still open. Layer 3's entry contract is the full validated context that Layers 1 and 2
produced. Its exit contract is the evidence set that satisfies echo's anchor requirements
— identified at Step 4 before any forward planning began. The bad plan's "done" gate for
"release-prep" tracked completion, not debt clearance, and never defined what echo would need.

**The echo stage — why it is always last and always auto, and why all four axes anchor at echo:**

1. **Echo carries no skills because all four axes terminate at echo.** Echo is the
   backward-derivation anchor (all gates were derived from echo's requirements), the
   debt-register terminus (all debt categories are cleared before echo), the final boundary
   consumer (all exit contracts are delivered before echo triggers), and the inertia contrast
   target (the bad plan's "done" gates would have produced a meaningless echo). Echo closes
   all four axes simultaneously.
2. **`auto: true` means echo's entry requirements are auto-verified.** When Layer 3's gate —
   derived backward from echo's requirements, structured as a debt-clearance condition, and
   expressed as a boundary exit contract — passes, echo runs automatically. Echo has no gate
   because it is the derivation anchor, not a step within the chain.
3. **Echo signals that all four axes were satisfied end-to-end.** The backward derivation
   was followed; all debt was cleared at threshold; all boundary contracts were delivered;
   all gates described evidence state, not execution state. When echo closes, the plan did
   its job — all four things the bad planning meeting failed to do.

---

Build the plan for **{{topic}}** using the full combined template below. Complete the backward
derivation anchor comments first, then fill the forward stages.

```yaml
# REQUIRED PRESERVE: this program is a plan, not an executor.
# Built backward from echo. Gates are debt-clearance boundary-exit contracts. Skills run standalone.

program:
  topic: "{{topic}}"
  # === BACKWARD DERIVATION (complete before filling stages) ===
  # Echo requires: [name the synthesis artifacts Layer 3 must deliver]
  # Layer 3 requires: [name the validated artifacts Layer 2 must deliver]
  # Layer 2 requires: [name the scout signals Layer 1 must deliver]
  # Layer 1 requires: nothing at entry
  stages:

    # ---- Layer 1: Breadth ---- | scout:* clears foundational debt | exit contract → Layer 2 entry ----
    - name: "[discovery label — derived from Layer 2 entry + Layer 1 debt category]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
      gate: "[scout artifact-types present] and [quality condition — foundational debt <=N, >=N scout signals, Layer 2 entry threshold]"

    # ---- L1→L2 Boundary: Layer 1 exit contract satisfied → Layer 2 entry contract opens ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* clear design + quality debt | entry: L1 scout | exit: delivers to Layer 3 ----
    - name: "[design label — derived from Layer 3 entry + design debt category]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
      gate: "[draft/prove artifact-types present] and [quality condition — design debt <=N, no P0 questions, Layer 3 validation threshold]"

    - name: "[validation label — derived from Layer 3 synthesis + quality debt category]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
      gate: "[review/flow/trace artifact-types present] and [quality condition — quality debt <=N findings, Layer 3 readiness threshold]"

    # ---- L2→L3 Boundary: Layer 2 exit contract satisfied → Layer 3 entry contract opens ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* clear adoption + narrative debt | entry: full validated context | exit: satisfies echo anchor ----
    - name: "[synthesis label — derived from echo anchor + adoption/narrative debt category]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
      gate: "[listen/topic artifact-types present] and [quality condition — total remaining debt <=N, >=N readiness signals, echo anchor requirements satisfied]"

    # ---- L3→Echo Boundary: all four axes terminate here ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo auto-closes when L3 exit contract passes; all derivation, debt, and boundary axes close here

## Plan Verification
# [ ] backward derivation anchor comments filled in before building stages
# [ ] echo is last, skills: [], auto: true, no gate field
# [ ] every non-echo gate is a debt-clearance condition AND a boundary exit contract
# [ ] every non-echo gate names artifact-types (presence) AND a quality threshold (debt condition)
# [ ] at least one gate carries a numeric threshold (>=N or <=N)
# [ ] stage order satisfies backward-derived dependency: scout → draft → review/prove → flow/trace → listen → topic
# [ ] every skill belongs to a valid Signal namespace
# [ ] stage names reflect the backward-derived debt category they clear
# [ ] this file is a plan; skills run standalone; backward derivation does not auto-execute them
```
