---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 9
rubric: v25
total_pts: 100
golden_threshold: 80
new_criteria: C-28, C-29
---

# program-plan — R9 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v25 (C-01 through C-29, 22 aspirational criteria, formula:
`(essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/22)*10`).

**R8 retrospective under v25 rubric:**
- V-01 (Zone-Anchor Z-NN): 99.09 — C-28 FAIL (raw BAD YAML, no meeting narrative), C-29 FAIL (identity claim artifact-scoped only)
- V-02 (Narrative Inertia Framing): 100.00 — C-28 PASS, C-29 PASS
- V-03 (Formal Constraint Spec): 99.09 — C-28 FAIL, C-29 FAIL
- V-04 (Displacement + Role Sequence): 99.09 — C-28 FAIL, C-29 FAIL
- V-05 (All R8 Axes): 99.09 — C-28 FAIL, C-29 FAIL

**R9 target:** All five variants hit 100.00. C-28/C-29 are now baseline requirements in all
variations. The meeting narrative and process-replacement identity claim are locked structural
features, not optional framing.

**R8 axis coverage (reference):**

| R8 axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Zone-anchor lifecycle (Z-NN) | X | | | | X |
| Handoff-matrix table (adjacent columns) | | X | | | X |
| Formal constraint spec (SHALL/P-NN) | | | X | | X |
| Displacement woven + role sequence (R-NN) | | | | X | X |
| Narrative inertia framing (meeting open) | | X | | | |

**R9 new axes (all carry C-28/C-29 as baseline):**

| Axis | Description |
|------|-------------|
| Phrasing register (second-person coaching) | Entire skill speaks in coaching second-person: "Your team just ran this meeting." Meeting narrative is personal; process-replacement claim is direct advice |
| Output format (open question inventory Q-NN) | Primary navigational structure is a question inventory table. Each stage closes a named open question. Meeting shows questions assumed-closed rather than tracked |
| Lifecycle emphasis (risk-retirement arc R-NN) | Each stage retires a named risk. Gates are risk-retirement conditions. Meeting shows risks not being named or tracked |
| Role sequence + commitment contract | Each stage is a named role's formal commitment. Meeting shows verbal commitments without artifact contracts |
| All R9 axes combined | Coaching voice + question inventory + risk retirement + role ownership + consumer-pull backward derivation |

**R9 variation lineup:**

- V-01 (single): Phrasing register — second-person coaching voice throughout
- V-02 (single): Output format — open question inventory (Q-NN) as primary navigational structure
- V-03 (single): Lifecycle emphasis — risk-retirement arc (each stage retires a named risk)
- V-04 (combined): Role sequence + commitment contract framing
- V-05 (combined): All R9 axes — coaching voice + question inventory + risk retirement + role ownership + consumer-pull

---

## V-01 — Phrasing Register: Second-Person Coaching Voice

**Axis:** Phrasing register — the entire skill body is written in second-person coaching voice.
"Your team just ran this meeting." "Here is what your plan produced." "Your gates need to describe
evidence state, not execution state." The meeting narrative in the opening is personal and immediate
— the reader sees themselves in the bad pattern. The process-replacement identity claim reads as
direct advice. All structural elements (layer narration, YAML template, checklist) stay in coaching
voice.

**Hypothesis:** Second-person coaching register personalizes both C-28 (the meeting becomes the
reader's own meeting, not an abstract cautionary tale) and C-29 (the process-replacement claim
lands as personal advice). All structural criteria proven in R8 carry over. Register variation
is stylistic — all structural criteria remain satisfiable at 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

Your team just wrapped a fifteen-minute planning sync. Your PM opened a doc and said: "Let's put
together a rough plan so we're aligned. Discovery first, then design, then we ship." Your architect
added three stages. For every gate, someone typed "done" or "when we're ready" and moved on.
No one pushed back. The meeting ended. Everyone felt aligned.

Here is what your planning sync produced:

```yaml
# What that meeting produced for {{topic}}:
stages:
  - name: discovery
    skills: [scout, draft]
    gate: "done"
  - name: development
    skills: [trace, flow, review]
    gate: "when we feel good about it"
  - name: launch
    skills: []
    gate: "shipped"
```

`/program:plan` exists to replace this conversation and the plan it produces.

Not because your team was careless — but because "done" is not a gate. It describes execution
state, not evidence state. A gate that says "done" tells you when people stopped working, not
when the evidence needed to advance actually exists. Your discovery stage bundled `draft` with
`scout`, which means you are drafting a spec before your market signals exist to inform it.
Your "launch" stage has no skills and no evidence condition — it is not a stage, it is a wish.

`/program:plan` is not an executor. It produces a plan — a structured sequence of gated evidence
stages you work through, one at a time, each skill running standalone. The program tells you
what to run and in what order. It does not run anything for you.

---

**Before you build your plan, read these three tables.**

---

**Table 1 — Evidence arc: phases, namespaces, arc role**

| Phase | Layer | Arc role | Namespaces | What this layer produces for the next |
|-------|-------|----------|------------|---------------------------------------|
| Discovery | Layer 1 (Breadth) | Establishes the foundational signal set Layer 2 requires | scout | scout signal artifacts |
| Design | Layer 2 (Depth) | Deepens signals into artifacts Layer 3 can validate | draft, prove | spec, prototype, hypothesis artifacts |
| Validation | Layer 2 (Depth) | Closes quality gaps; produces validated artifacts Layer 3 synthesizes | review, flow, trace | validated design and flow artifacts |
| Synthesis | Layer 3 (Synthesis) | Requires the full validated artifact context from prior layers | listen, topic | readiness and synthesis artifacts |
| Echo | Terminal | Auto-closing; requires all prior artifacts to exist | — | — |

---

**Table 2 — Gate design: BAD vs GOOD**

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"done"` | Execution state — when did people stop, not what exists | `"scout-feasibility signal and scout-market signal present"` |
| `"when we feel good"` | Subjective state — unverifiable, undisputable | `"draft-spec artifact present with no open P0 questions"` |
| `"stage complete"` | Circular — restates the fact that the stage ran | `">=2 scout signals present, no blocking feasibility gaps"` |
| `"shipped"` | Outcome state, not evidence state | `"listen-adoption signal present with >=3 persona evaluations"` |
| `""` (empty) | No condition — gate is absent | `"review-design artifact present, <=2 open findings"` |

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

Your namespace dependency order: `scout -> draft -> review/prove -> flow/trace -> listen -> topic`.
Your plan cannot place a stage that consumes artifacts before a stage that produces them.

---

**Layer 1 (Breadth) — your foundation layer, which produces the scout signals Layer 2 requires:**

Your plan's first layer is your breadth investment. Every scout-namespace skill runs here.
Your team does not know what it does not know about `{{topic}}` yet — feasibility, market fit,
compliance constraints, stakeholder expectations. Layer 1 produces the raw intelligence that makes
it possible for your architect to write a spec worth writing. Without Layer 1 artifacts in place,
your draft-namespace skills are guessing into a void. The gate for your Layer 1 stage is the
evidence condition your Layer 2 stages require before they can run — not "done," but a named
artifact type paired with a quality threshold.

**Layer 2 (Depth) — your investigation layer, which requires Layer 1 scout artifacts and produces validated artifacts Layer 3 synthesizes:**

Layer 2 is where your team deepens its knowledge into artifacts with enough fidelity to validate.
Your draft-namespace skills produce the spec and prototype. Your prove-namespace skills test the
spec's assumptions. Your review-namespace skills assess design quality. Your flow- and trace-
namespace skills validate behavior under realistic conditions. Each of these depends on the scout
signals your Layer 1 produced — `review:design` cannot assess a design that does not exist;
`flow:lifecycle` cannot simulate a lifecycle that has not been specified. Layer 2 gates describe
the validated artifact state: the spec exists and has no open P0 questions; the prototype passes
hypothesis testing; the flow simulation has no blocking gaps.

**Layer 3 (Synthesis) — your readiness layer, which requires the full validated artifact context from prior layers to produce meaningful synthesis:**

Layer 3 closes the last gap: whether your team and your users are ready. Your listen-namespace
skills gather feedback, support signal, and adoption readiness. Your topic-namespace skills
synthesize the full artifact set into a story. Layer 3 cannot produce meaningful synthesis if
Layer 2 artifacts are absent or unvalidated — adoption readiness signals presuppose a thing
worth adopting. The gate for your Layer 3 stage is not "launched" — it is the presence of
readiness artifacts that your team can dispute, extend, or act on.

**The echo stage — why it is always last and always auto:**

1. **Echo carries no skills because the investigation is complete.** Echo does not run new
   evidence-gathering work. If your arc was well-designed, every open question was answered in
   Layers 1-3. Echo's job is to surface what you learned, not extend what you investigated.
2. **`auto: true` means echo closes without a gate condition.** Echo does not wait for your
   team to decide it is "done." When the prior stage's gate passes, echo runs automatically.
   It has no human gate because its purpose is retrospective, not evaluative — it asks "what
   did we learn that we didn't expect?" not "are we ready to proceed?"
3. **Echo signals arc closure.** When echo closes, your program is complete. Your topic has
   been investigated, your artifacts exist, and the evidence arc has a terminal point. Echo is
   the structural guarantee that your plan has an end — not "when we feel good," but when the
   arc's evidence conditions have all been satisfied.

---

**Your program.yaml template — fill in all bracketed fields, do not change the structure.**

```yaml
# REQUIRED: preserve this comment — this program is a plan, not an executor.
# Every skill listed here runs standalone. This YAML does not execute skills.
# Treat it as a sequenced evidence plan, not a workflow engine.

program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # ---- Layer 1: Breadth — produces the foundational scout signals Layer 2 requires ----
    - name: [gap-derived label — not "stage1", not a skill name]
      # Gap: "We don't yet know [the specific question this stage answers about {{topic}}]"
      # Owner: PM
      # Consumes: []
      # Produces: [scout signal artifact types — name them specifically]
      skills: [scout:feasibility, scout:market]   # replace with applicable scout skills
      gate: "[produces artifact-types present] and [quality condition — numeric threshold: >=N]"

    # ---- Layer 1 -> Layer 2 boundary ----
    # Layer 1 final Produces: [artifact types]
    # Layer 2 first Consumes: [same artifact types — bilateral contract]

    # ---- Layer 2: Depth — requires Layer 1 scout artifacts; produces validated artifacts Layer 3 synthesizes ----
    - name: [gap-derived label]
      # Gap: "We don't yet know [the specific design/spec question this stage answers]"
      # Owner: Architect
      # Consumes: [Layer 1 scout signal types]
      # Produces: [spec/prototype/review artifact types]
      skills: [draft:spec, prove:prototype]   # replace with applicable skills
      gate: "[produces artifact-types present] [+ quality condition]"

    - name: [gap-derived label]
      # Gap: "We don't yet know [the specific validation question this stage answers]"
      # Owner: Architect + Dev
      # Consumes: [Layer 2 design artifact types from stage above]
      # Produces: [validated flow/trace artifact types]
      skills: [review:design, flow:lifecycle, trace:contract]   # replace with applicable skills
      gate: "[produces artifact-types present, <=N open findings]"

    # ---- Layer 2 -> Layer 3 boundary ----
    # Layer 2 final Produces: [artifact types]
    # Layer 3 first Consumes: [same artifact types — bilateral contract]

    # ---- Layer 3: Synthesis — requires the full validated artifact context from prior layers ----
    - name: [gap-derived label]
      # Gap: "We don't yet know [the readiness/adoption question this stage answers]"
      # Owner: PM + Team
      # Consumes: [Layer 2 validated artifact types]
      # Produces: [readiness and synthesis artifact types]
      skills: [listen:adoption, topic:status]   # replace with applicable skills
      gate: "[produces artifact-types present] [+ readiness condition]"

    # ---- Terminal stage — do not modify ----
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"

    ## Plan Verification
    # [ ] Echo is last, has skills: [], auto: true, no gate field
    # [ ] Every non-echo stage has a gap, owner, consumes, produces, AND a non-trivial gate
    # [ ] Every gate describes evidence state (artifact present / quality condition) — not execution state
    # [ ] At least one gate carries a numeric threshold (>=N or <=N)
    # [ ] Stage order respects namespace dependency: scout -> draft -> review/prove -> flow/trace -> listen -> topic
    # [ ] Every skill name belongs to a valid Signal namespace
    # [ ] This file is a plan — it does not execute skills; each skill runs standalone
```

---

## V-02 — Output Format: Open Question Inventory (Q-NN)

**Axis:** Output format — the primary navigational structure is an open question inventory table
(Q-NN IDs). Every stage exists to close a named open question about `{{topic}}`. The Q-NN table
is the pre-YAML derivation artifact: stages are organized by the open questions they close, and
gates are the evidence conditions that confirm the question has been answered. The meeting narrative
shows questions being assumed-closed rather than tracked.

**Hypothesis:** R8 used zone-exit criteria (V-01), Produces/Consumes matrix rows (V-02), and
constraint satisfaction records (V-03) as pre-YAML derivation artifacts. A question inventory is
a distinct format: the open question IS the gap-language object that drives both the stage name
(what is the question?) and the gate design (what evidence would answer it?). This makes C-04
(non-trivial gates) nearly automatic and C-17 (dependency narration) maps naturally to question
dependency chains. Anticipated score: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

A product manager, an architect, and two developers were in a planning sync. The PM had written
a one-pager about `{{topic}}` the day before. In the meeting, the architect said: "I think we have
a pretty good handle on the design." The PM said: "Agreed." Nobody wrote down what they did not
know. The doc had no open questions section. The meeting ended in twelve minutes. The plan that
emerged looked like this:

```yaml
# What that meeting produced for {{topic}}:
stages:
  - name: planning
    skills: [scout:market, draft:spec]
    gate: "spec drafted"
  - name: build-and-validate
    skills: [review:design, flow:lifecycle, trace:contract, prove:prototype]
    gate: "review complete"
  - name: launch-readiness
    skills: [listen:adoption, topic:status]
    gate: "ready"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

Nobody in that meeting named an open question. "Spec drafted" does not tell you what the spec
needs to answer before the team can advance. "Review complete" does not tell you what the review
must find (or not find) before validation is done. "Ready" is not a gate — it is an adjective.
The team bundled `scout:market` with `draft:spec` in the same stage: the spec was written
before market signals existed to inform it.

`/program:plan` is not a workflow executor. It is a question-closure plan. Each stage is an
evidence-gathering campaign aimed at a named open question. The gate is the evidence condition
that proves the question has been answered. The plan does not run skills — you run them, one at
a time, when their stage is active.

---

**Before you build your plan, read these three tables.**

---

**Table 1 — Evidence arc: open question layers, namespaces, arc role**

| Q-layer | Arc name | What layer closes | Namespaces | Question type |
|---------|----------|-------------------|------------|---------------|
| Layer 1 (Breadth) | Discovery | Foundational questions Layer 2 builds on | scout | Feasibility, market, stakeholder, compliance questions |
| Layer 2 (Depth) | Design + Validation | Design questions Layer 3 synthesizes; requires Layer 1 answers | draft, prove, review, flow, trace | Design quality, correctness, behavior, risk questions |
| Layer 3 (Synthesis) | Readiness | Readiness questions; requires the full validated artifact context from prior layers | listen, topic | Adoption, feedback, readiness questions |
| Terminal | Echo | Retrospective question; auto-closed | — | Retrospective |

---

**Table 2 — Gate design: BAD vs GOOD (question-answer framing)**

| BAD gate | Why it fails as a question closure | GOOD gate (question-answer form) |
|----------|-----------------------------------|----------------------------------|
| `"spec drafted"` | Does not state what the spec must answer; a blank spec is "drafted" | `"draft-spec artifact present; Q-02 (design question) answered; no open P0 gaps"` |
| `"review complete"` | States execution, not finding state; a rubber-stamp review is "complete" | `"review-design artifact present; <=2 open findings; no P0 severity"` |
| `"ready"` | Adjective, not evidence condition | `"listen-adoption signal present; >=3 persona evaluations recorded"` |
| `"done"` | Execution state — when did people stop, not what exists | `"scout-feasibility and scout-market signals present; Q-01 answered"` |
| `""` (empty) | No condition — the question is never closed | `">=2 scout signals present with Q-01 explicitly resolved"` |

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

Namespace dependency order: `scout -> draft -> review/prove -> flow/trace -> listen -> topic`.
A stage cannot use skills from a namespace whose artifacts no earlier stage has produced.

---

**Before writing stage YAML, produce the open question inventory.**

For each open question about `{{topic}}`, assign a Q-NN ID, name the question precisely, identify
which namespace closes it, and write the gate condition that proves the question is answered.

```
Q-NN Open Question Inventory for {{topic}}

| Q-ID | Open question | Layer | Namespace(s) | Gate condition (proves question answered) |
|------|--------------|-------|--------------|-------------------------------------------|
| Q-01 | [What do we not know about feasibility/market for {{topic}}?] | Layer 1 | scout | [>=N scout signals present, Q-01 resolved] |
| Q-02 | [What do we not know about the design of {{topic}}?] | Layer 2 | draft, prove | [draft-spec present, Q-02 answered, no P0 gaps] |
| Q-03 | [What do we not know about quality/correctness of {{topic}}?] | Layer 2 | review, flow, trace | [review + flow + trace artifacts present, <=N findings] |
| Q-04 | [What do we not know about readiness for {{topic}}?] | Layer 3 | listen, topic | [listen-adoption signal present, >=N evaluations] |
```

Rules:
- Question language: "We don't yet know [X]" — not task language ("implement X")
- Gate condition is the evidence that closes Q-NN — not execution state
- Dependency: Q-02 cannot be answered before Q-01 artifacts exist; Q-03 before Q-02; Q-04 before Q-03
- Stage names are derived from the question, not from namespace or task descriptions

---

**Layer 1 (Breadth) — closes your foundational open questions, producing the scout signal artifacts that Layer 2's design questions require:**

Your first layer is entirely about naming what you do not know and producing the signals that
answer those questions. Every Q-NN question assigned to Layer 1 is a scout-namespace question:
feasibility, market position, stakeholder expectations, compliance constraints. Layer 1 does not
produce a spec — it produces the signal set that makes it possible to write a spec worth writing.
The gate for each Layer 1 stage is the evidence condition that proves Q-NN has been answered, not
that a task was completed. A numeric threshold (">=2 scout signals") makes the gate machine-checkable
and removes the subjectivity that makes "done" useless.

**Layer 2 (Depth) — requires Layer 1 scout signals; closes design and validation questions to produce validated artifacts Layer 3 can synthesize:**

Layer 2 has two sub-arcs. The first closes design questions (draft- and prove-namespace): the
spec answers Q-01's gaps, the prototype tests design assumptions, the hypothesis investigation
validates the core claim. The second closes validation questions (review-, flow-, trace-namespace):
the design is reviewed for quality; the lifecycle is simulated; the contract is traced. These are
ordered — you cannot review a spec that does not exist, and you cannot trace a contract that has
not been defined. Layer 2 gate conditions state what artifact types must be present AND what quality
conditions they satisfy (finding counts, severity thresholds). The question drives the gate: the
gate proves Q-02 or Q-03 has been answered.

**Layer 3 (Synthesis) — closes your readiness questions, but requires the full validated artifact context from prior layers to give those questions meaning:**

Layer 3 closes the question of readiness. Your listen-namespace skills gather feedback and adoption
signals. Your topic-namespace skills synthesize the entire artifact set. Neither is meaningful
without Layers 1 and 2 complete: adoption readiness presupposes a designed, validated thing.
Layer 3 gates describe the readiness evidence state — not "launched," but specific artifact presence
and evaluation counts. The synthesis artifact is the answer to the question your program was built
to investigate.

**The echo stage — why it is the answer to a question no prior stage can close:**

1. **Echo's question is retrospective, not investigative.** Every Q-NN question was about
   `{{topic}}` — what the team needed to know. Echo's question — "What did we learn that we
   didn't expect?" — is about the investigation itself. No amount of evidence-gathering can
   pre-answer it. It requires the complete arc to have run.
2. **`auto: true` means echo closes its question automatically.** Echo does not wait for a gate
   condition. When the final Layer 3 gate passes, echo's question becomes answerable and the
   program closes. The auto flag encodes this: retrospection is triggered by completion.
3. **Echo is structurally outside the Q-NN inventory.** It is not an investigation question —
   it is a learning question. Its presence in every program signals that investigation and learning
   are distinct activities, and your plan supports both.

---

**Your program.yaml template — fill in Q-NN IDs from your open question inventory.**

```yaml
# REQUIRED: preserve this comment — this program is a plan, not an executor.
# Skills run standalone. This YAML sequences them; it does not execute them.

program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # ---- Layer 1: Breadth — closes foundational open questions; produces scout signals Layer 2 requires ----
    - name: [Q-01 question-derived label]
      # Q-ref: Q-01 — "[open question text from inventory]"
      # Owner: PM
      # Consumes: []
      # Produces: [scout signal artifact types that answer Q-01]
      skills: [scout:feasibility, scout:market]   # replace with Q-01 applicable skills
      gate: "[Q-01 artifact-types present] [+ >=N threshold]"

    # ---- Layer 1 -> Layer 2 boundary: Q-01 answered; Q-02 can now be pursued ----

    # ---- Layer 2: Depth — requires Layer 1 scout signals; closes design and validation questions ----
    - name: [Q-02 question-derived label]
      # Q-ref: Q-02 — "[open question text from inventory]"
      # Owner: Architect
      # Consumes: [Layer 1 scout signal types]
      # Produces: [spec and prototype artifact types that answer Q-02]
      skills: [draft:spec, prove:prototype]   # replace with Q-02 applicable skills
      gate: "[Q-02 artifact-types present, no P0 open gaps]"

    - name: [Q-03 question-derived label]
      # Q-ref: Q-03 — "[open question text from inventory]"
      # Owner: Architect + Dev
      # Consumes: [Layer 2 design artifact types from stage above]
      # Produces: [validated review/flow/trace artifact types that answer Q-03]
      skills: [review:design, flow:lifecycle, trace:contract]   # replace with Q-03 applicable skills
      gate: "[Q-03 artifact-types present, <=N open findings]"

    # ---- Layer 2 -> Layer 3 boundary: Q-02 and Q-03 answered; Q-04 can now be pursued ----

    # ---- Layer 3: Synthesis — requires the full validated artifact context from prior layers ----
    - name: [Q-04 question-derived label]
      # Q-ref: Q-04 — "[open question text from inventory]"
      # Owner: PM + Team
      # Consumes: [Layer 2 validated artifact types]
      # Produces: [readiness and synthesis artifact types that answer Q-04]
      skills: [listen:adoption, topic:status]   # replace with Q-04 applicable skills
      gate: "[Q-04 artifact-types present] [+ >=N evaluation count]"

    # ---- Terminal stage — do not modify ----
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"

    ## Plan Verification
    # [ ] Echo is last, skills: [], auto: true, no gate
    # [ ] Every non-echo stage has a Q-ref, owner, consumes, produces, and a non-trivial gate
    # [ ] Every gate describes evidence state that proves Q-NN answered — not execution state
    # [ ] At least one gate carries a numeric threshold (>=N or <=N)
    # [ ] Stage order matches Q-NN dependency chain: Q-01 before Q-02 before Q-03 before Q-04
    # [ ] Every skill name belongs to a valid Signal namespace
    # [ ] This plan does not execute skills — each skill runs standalone
```

---

## V-03 — Lifecycle Emphasis: Risk-Retirement Arc

**Axis:** Lifecycle emphasis — the arc is organized as a sequence of risk-retirement events.
Each stage retires one or more named risks about `{{topic}}`. The gate is the risk-retirement
condition: the evidence state that proves the named risk is retired. The meeting narrative shows
risks existing but never being named — the team "felt aligned" while carrying unretired risks
into the next phase.

**Hypothesis:** Risk-retirement framing gives C-04 (non-trivial gates) a natural semantic anchor
— gates are risk-retirement conditions, not execution conditions. C-08 (deliberate arc) maps to
a risk severity gradient: Layer 1 retires existential risks, Layer 2 retires design risks, Layer 3
retires launch risks. C-17 narration states causal dependency: design risks cannot be retired while
existential risks are open — a design built on unretired feasibility risk is contingent. Anticipated
score: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

A team was three weeks into designing `{{topic}}` when the PM asked the engineering lead: "Are we
still confident in the market case?" The engineering lead paused. "I assumed the PM had validated
that in the first week." The PM said: "I thought we were past that." Nobody had run
`scout:feasibility`. The risk had been open since day one. The plan that started them down this
path looked like this:

```yaml
# What that plan looked like:
stages:
  - name: design-and-spec
    skills: [draft:spec, review:design]
    gate: "spec approved"
  - name: implementation-validation
    skills: [flow:lifecycle, trace:contract, prove:prototype]
    gate: "validation done"
  - name: readiness
    skills: [listen:adoption, topic:status]
    gate: "ready to ship"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

The plan had no risk register. No stage was assigned to retire the feasibility risk. "Spec
approved" is not a risk-retirement condition — it is a social condition. "Validation done"
does not name which risks were retired by validation. "Ready to ship" is an assertion, not
a risk condition. The team built an entire design on unretired existential risk.

`/program:plan` is not a workflow engine. It is a risk-retirement plan. Each stage is an
evidence-gathering campaign that retires one or more named risks before the team advances.
The gate is the evidence condition that proves the risk is retired. Skills run standalone —
the plan sequences what to run and when, but does not execute anything.

---

**Before you build your plan, read these three tables.**

---

**Table 1 — Evidence arc: risk layers, namespaces, arc role**

| Risk layer | Arc name | Risks retired | Namespaces | What retiring these risks enables |
|-----------|----------|--------------|------------|----------------------------------|
| Layer 1 (Breadth) | Discovery | Existential risks: feasibility, market, stakeholders, compliance — foundational; Layer 2 risks cannot be retired while Layer 1 risks are open | scout | Enables Layer 2: design built on validated foundation |
| Layer 2 (Depth) | Design + Validation | Design risks: spec, prototype, implementation correctness — structural; Layer 3 synthesis is hollow if Layer 2 risks are open | draft, prove, review, flow, trace | Enables Layer 3: readiness assessed against a validated thing |
| Layer 3 (Synthesis) | Readiness | Launch risks: adoption, user readiness, team alignment — requires the full validated artifact context from prior layers | listen, topic | Enables echo: retrospective on complete investigation |
| Terminal | Echo | None retired — retrospective only | — | Closes the program |

---

**Table 2 — Gate design: BAD vs GOOD (risk-retirement framing)**

| BAD gate | Why it fails as a risk-retirement condition | GOOD gate (risk-retirement form) |
|----------|---------------------------------------------|----------------------------------|
| `"spec approved"` | Social condition — does not name which risks the spec retires | `"draft-spec present; feasibility risk R-01 retired (scout signal confirms)"` |
| `"validation done"` | Execution state — does not name which design risks were retired | `"review-design + flow-lifecycle artifacts present; design risk R-02 retired; <=2 P1 findings"` |
| `"ready to ship"` | Assertion — launch risks may still be open | `"listen-adoption signal present; launch risk R-03 retired; >=3 persona evaluations"` |
| `"done"` | Not a risk condition | `">=2 scout signals present; R-01 (feasibility) explicitly retired"` |
| `""` (empty) | No risk retirement condition stated | `"scout-feasibility signal present; R-01 status: RETIRED"` |

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

Namespace dependency order: `scout -> draft -> review/prove -> flow/trace -> listen -> topic`.
Existential risks (Layer 1) must be retired before design risks (Layer 2) can be addressed.

---

**Before writing stage YAML, produce the risk register.**

For each named risk about `{{topic}}`, assign an R-NN ID, name the risk precisely, identify
which layer retires it, and write the retirement condition that proves it closed.

```
Risk Register for {{topic}}

| R-ID | Risk name | Layer | Namespace(s) | Retirement condition (evidence that closes this risk) |
|------|-----------|-------|--------------|------------------------------------------------------|
| R-01 | [Existential risk — e.g., "We don't know if {{topic}} is technically feasible"] | Layer 1 | scout | [scout-feasibility signal present, gap rate <=N%] |
| R-02 | [Design risk — e.g., "We don't know if our spec will hold under real constraints"] | Layer 2 | draft, prove | [draft-spec present, hypothesis tested, no P0 gaps] |
| R-03 | [Validation risk — e.g., "We don't know if the implementation is correct"] | Layer 2 | review, flow, trace | [review + flow artifacts present, <=N findings] |
| R-04 | [Launch risk — e.g., "We don't know if users are ready to adopt {{topic}}"] | Layer 3 | listen | [listen-adoption signal, >=N persona evaluations] |
```

Rules:
- Risk language: "We don't know if [X]" or "We don't yet know [X]"
- A risk without a retirement condition is not a risk — it is anxiety
- Stages correspond to R-NN IDs; stage names are derived from the risk being retired

---

**Layer 1 (Breadth) — retires your existential risks, producing the scout signal artifacts that Layer 2 design risks cannot be addressed without:**

Layer 1 is your existential-risk retirement campaign. Before your team designs anything, it must
know whether `{{topic}}` is worth designing. Feasibility, market fit, compliance exposure, and
stakeholder alignment are all existential risks — if any one of them is open when you start
drafting a spec, your spec is a bet. Scout-namespace skills produce the signals that retire these
risks. The Layer 1 gate condition is the risk-retirement evidence: not "research done," but named
artifact types present with a risk explicitly retired.

**Layer 2 (Depth) — requires Layer 1 existential risks to be retired; addresses design and validation risks to produce validated artifacts Layer 3 can assess for readiness:**

Layer 2 has two risk families. Design risks (draft-, prove-namespace): the spec may be under-
specified, the prototype may reveal false assumptions, the hypothesis may not hold. Validation risks
(review-, flow-, trace-namespace): the design may have quality gaps, the flow may have unhandled
edge cases, the contract may have behavioral mismatches. These cannot be addressed while Layer 1
risks are open — a design built on unretired feasibility risk is contingent. The Layer 2 gate
condition is the validated artifact state with a named risk-retirement record: specific artifacts
present, quality threshold satisfied, risk status updated.

**Layer 3 (Synthesis) — requires the full validated artifact context from prior layers to give launch-risk retirement its meaning:**

Layer 3 retires launch risks: adoption readiness, user preparedness, and team alignment. These
cannot be meaningfully assessed without Layers 1 and 2 complete. An adoption readiness signal is
hollow if the thing being adopted has unretired design risks. A topic synthesis is misleading if
the underlying artifacts are unvalidated. Layer 3 retirement conditions reference both the new
listen- and topic-namespace artifacts AND the prior layers' retirement status — the gate confirms
that evidence was gathered against a validated foundation, not merely that evidence was gathered.

**The echo stage — the one event that retires no risk:**

1. **Echo carries no skills because all risks have been retired.** Every R-NN risk in your
   register was retired in Layers 1-3. Echo's job is retrospective, not risk-oriented — it asks
   what you learned unexpectedly, not whether risks are still open.
2. **`auto: true` means echo triggers automatically on final risk retirement.** When the last
   Layer 3 gate condition is satisfied, echo's turn arrives without a human gate. The retrospective
   is a natural consequence of completion, not a gateable deliverable.
3. **Echo closes the program by closing the investigation.** Its presence guarantees that every
   program has a defined terminal state — a point at which the risk register is exhausted and the
   team turns from investigation to reflection.

---

**Your program.yaml template — fill in R-NN IDs from your risk register.**

```yaml
# REQUIRED: preserve this comment — this program is a plan, not an executor.
# Skills run standalone. This plan sequences risk-retirement campaigns; it does not run them.

program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # ---- Layer 1: Breadth — retires existential risks; produces scout signals that Layer 2 risk retirement requires ----
    - name: [risk-derived label — e.g., "feasibility-risk-retirement"]
      # Risk: R-01 — "[risk name from register]"
      # Owner: PM
      # Consumes: []
      # Produces: [scout signal artifact types that retire R-01]
      skills: [scout:feasibility, scout:market]   # replace with R-01 applicable skills
      gate: "[produces artifact-types present]; R-01 status: RETIRED [+ >=N threshold]"

    # ---- Layer 1 -> Layer 2: R-01 retired; Layer 2 risk retirement can proceed ----

    # ---- Layer 2: Depth — requires Layer 1 retirement; retires design and validation risks ----
    - name: [risk-derived label — e.g., "design-risk-retirement"]
      # Risk: R-02 — "[risk name from register]"
      # Owner: Architect
      # Consumes: [Layer 1 scout signal types]
      # Produces: [spec/prototype artifact types that retire R-02]
      skills: [draft:spec, prove:prototype]   # replace with R-02 applicable skills
      gate: "[produces artifact-types present]; R-02 status: RETIRED"

    - name: [risk-derived label — e.g., "validation-risk-retirement"]
      # Risk: R-03 — "[risk name from register]"
      # Owner: Architect + Dev
      # Consumes: [Layer 2 design artifact types]
      # Produces: [review/flow/trace artifact types that retire R-03]
      skills: [review:design, flow:lifecycle, trace:contract]   # replace with R-03 applicable skills
      gate: "[produces artifact-types present]; R-03 status: RETIRED; <=N open findings"

    # ---- Layer 2 -> Layer 3: R-02 and R-03 retired; Layer 3 risk retirement can proceed ----

    # ---- Layer 3: Synthesis — requires the full validated artifact context from prior layers ----
    - name: [risk-derived label — e.g., "launch-risk-retirement"]
      # Risk: R-04 — "[risk name from register]"
      # Owner: PM + Team
      # Consumes: [Layer 2 validated artifact types]
      # Produces: [listen/topic artifact types that retire R-04]
      skills: [listen:adoption, topic:status]   # replace with R-04 applicable skills
      gate: "[produces artifact-types present]; R-04 status: RETIRED [+ >=N evaluation count]"

    # ---- Terminal stage — do not modify ----
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"

    ## Plan Verification
    # [ ] Echo is last, skills: [], auto: true, no gate
    # [ ] Every non-echo stage has a risk reference, owner, consumes, produces, and risk-retirement gate
    # [ ] Every gate names a risk ID and retirement condition — not an execution state
    # [ ] At least one gate carries a numeric threshold (>=N or <=N)
    # [ ] Stage order retires Layer 1 risks before Layer 2, Layer 2 before Layer 3
    # [ ] Every skill name belongs to a valid Signal namespace
    # [ ] This plan does not execute skills — each skill runs standalone
```

---

## V-04 — Combined: Role Sequence + Commitment Contract

**Axes:** Role sequence + commitment contract framing. Each stage is a named role's formal
commitment to the team: they commit to producing specific evidence artifacts before the team can
advance. The meeting narrative shows roles making verbal agreements without artifact commitments.
Gates are contract clauses — the specific conditions the committing role must satisfy.

**Hypothesis:** Role sequence provides organizational anchoring (who owns what, in what order),
and commitment contract framing transforms the gate from an evidence condition into a named
commitment. This strengthens C-16/C-29 (meeting shows verbal commitments replacing contracts)
and C-04 (gates as contract clauses are semantically non-trivial by definition). C-28/C-29 are
structurally integrated: the meeting shows the PM, architect, and dev each saying "I've got it"
without naming the artifacts they commit to produce. Anticipated score: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

At the end of the planning sync, the PM said: "So we're all aligned?" The architect nodded: "Yep,
I'll start on the design." The lead developer said: "Once the design is ready I'll do the technical
work." The PM said: "I'll handle the readiness side." Everyone agreed. The plan produced from this
exchange looked like this:

```yaml
# What those verbal commitments produced for {{topic}}:
stages:
  - name: pm-discovery
    skills: [scout:market, scout:feasibility]
    gate: "PM signs off"
  - name: architect-design
    skills: [draft:spec, review:design, prove:prototype]
    gate: "Design approved"
  - name: dev-implementation
    skills: [flow:lifecycle, trace:contract, trace:state]
    gate: "Dev done"
  - name: pm-launch
    skills: [listen:adoption, topic:status]
    gate: "Shipped"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

"PM signs off" is not a commitment condition — it is a social ritual. "Design approved" does
not name what the architect committed to produce; it names what happens when they stop. "Dev done"
names when the developer stopped working, not what they committed to deliver. No role in that
meeting named an artifact. Each person said "I've got it" without stating what "it" produces.
When commitments are verbal and artifact-free, there is no contract to inspect when the gate arrives.

`/program:plan` is not a workflow engine. It is a commitment architecture. Each stage is a named
role's contract: a commitment to produce specific evidence artifacts before the team advances.
Gates are contract clauses — they state the artifact and quality conditions that fulfill the
commitment, not the role's subjective sense of completion.

---

**Before you build your plan, read these three tables.**

---

**Table 1 — Evidence arc: commitment layers, role ownership, arc role**

| Layer | Arc name | Role owner | What they commit to producing | Layer dependency |
|-------|----------|------------|-------------------------------|-----------------|
| Layer 1 (Breadth) | Discovery | PM | Scout signal artifacts — the foundational intelligence Layer 2 commitments depend on | None; first layer |
| Layer 2a (Depth-Design) | Design | Architect | Spec, prototype, and hypothesis artifacts — requires Layer 1 PM commitments delivered | Requires Layer 1 scout artifacts |
| Layer 2b (Depth-Validation) | Validation | Architect + Dev | Validated review/flow/trace artifacts — requires Layer 2a design artifacts | Requires Layer 2a spec artifacts |
| Layer 3 (Synthesis) | Readiness | PM + Team | Readiness and synthesis artifacts — requires the full validated artifact context from prior layers | Requires Layer 2b validated artifacts |
| Terminal | Echo | Auto | Retrospective close — no new commitment | All prior commitments fulfilled |

---

**Table 2 — Gate design: BAD vs GOOD (commitment contract framing)**

| BAD gate (verbal commitment) | Why it fails as a contract clause | GOOD gate (commitment contract form) |
|------------------------------|-----------------------------------|--------------------------------------|
| `"PM signs off"` | Social act, not artifact condition | `"scout-feasibility and scout-market artifacts present; PM commitment C-01 fulfilled"` |
| `"Design approved"` | Approval is social; no committed deliverable named | `"draft-spec artifact present, no open P0 gaps; architect commitment C-02 fulfilled"` |
| `"Dev done"` | Execution state, no committed artifact | `"flow-lifecycle and trace-contract artifacts present; C-03 fulfilled; <=2 findings"` |
| `"Shipped"` | Outcome state, not commitment fulfillment | `"listen-adoption signal present, >=3 persona evaluations; PM commitment C-04 fulfilled"` |
| `"Stage complete"` | Execution state — no committed artifact named | `"[named artifact types] present [+ quality condition]"` |

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

Role sequence order: PM (Layer 1) -> Architect (Layer 2a) -> Architect+Dev (Layer 2b) -> PM+Team (Layer 3).
Maps to namespace dependency: scout -> draft/prove -> review/flow/trace -> listen/topic.

---

**Before writing stage YAML, produce the commitment register.**

For each stage, name the committing role, the commitment they are making, and the contract clause
that proves the commitment fulfilled.

```
Commitment Register for {{topic}}

| C-ID | Role | Commitment statement | Artifacts committed | Contract clause (gate) |
|------|------|---------------------|---------------------|------------------------|
| C-01 | PM | "I commit to producing foundational signal artifacts before design begins" | [scout signal artifact types] | [artifact-types present + >=N threshold] |
| C-02 | Architect | "I commit to producing design artifacts before validation begins" | [spec, prototype artifact types] | [artifact-types present, no P0 gaps] |
| C-03 | Architect + Dev | "I commit to producing validated artifacts before readiness assessment begins" | [review, flow, trace artifact types] | [artifact-types present, <=N findings] |
| C-04 | PM + Team | "I commit to producing readiness artifacts before the program closes" | [listen, topic artifact types] | [artifact-types present + >=N evaluations] |
```

---

**Layer 1 (Breadth) — the PM's commitment layer, which produces the foundational scout signal artifacts that Layer 2 architect commitments depend on:**

The PM owns Layer 1. Their commitment is to produce the scout signal artifact set that gives the
architect something concrete to design against. Feasibility signals, market signals, stakeholder
alignment artifacts, compliance research — these are the PM's committed deliverables. Until these
artifacts exist and satisfy the Layer 1 contract clause, the architect's commitment cannot begin:
a spec written without feasibility and market signals is a design without a foundation. The PM's
gate condition is the evidence state that fulfills their commitment — not their subjective sense
of "done," but named artifact types present with a quality threshold.

**Layer 2 (Depth) — the architect's and dev's commitment layer, which requires the PM's Layer 1 commitments fulfilled and produces validated artifacts the PM's Layer 3 commitment depends on:**

Layer 2 has two sequential commitments. First, the architect commits to producing design artifacts
(spec, prototype, hypothesis) — but cannot fulfill this commitment without the PM's Layer 1 scout
signals. Second, the architect and dev together commit to producing validated artifacts (review,
flow, trace) — but cannot fulfill this without the architect's Layer 2a design artifacts. Each
commitment depends on the previous one, and each contract clause names the artifacts that fulfill
it. The validation commitment's clause includes a quality threshold — "reviewed with <=N findings"
is a committed deliverable; "reviewed" alone is not.

**Layer 3 (Synthesis) — the PM and team's final commitment layer, which requires the full validated artifact context from prior layers to fulfill the readiness commitment:**

Layer 3 is the PM's second commitment, shared with the team. Their commitment is to produce
readiness artifacts — listen signals, adoption evaluations, topic synthesis — confirming the
feature is ready for the next milestone. This commitment is meaningful only if Layers 1 and 2
commitments are fulfilled: adoption readiness evaluated against an unvalidated design is a
commitment to the wrong thing. The Layer 3 contract clause references the readiness artifacts AND
the evaluation count — because a readiness commitment without a minimum number of evaluations is
a commitment without sufficient evidence.

**The echo stage — the commitment the plan makes to learning:**

1. **Echo carries no role commitment because it is the plan's commitment to the team.** The plan
   itself commits to closing with a retrospective. No individual role owns echo — it belongs to
   the program. Its skill-free design encodes this: there is no deliverable to produce, only a
   question to answer.
2. **`auto: true` is the plan's fulfillment of its own commitment.** When all role commitments
   C-01 through C-04 are fulfilled, echo triggers automatically. The plan committed to a
   retrospective and delivers it without requiring another human gate.
3. **Echo's question is the program's final artifact.** "What did we learn that we didn't expect?"
   is the commitment the program makes to institutional learning — that no investigation ends
   without surfacing its own surprises.

---

**Your program.yaml template — fill in commitment register C-IDs.**

```yaml
# REQUIRED: preserve this comment — this program is a plan, not an executor.
# Each commitment is fulfilled by running skills standalone, not by this YAML.

program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # ---- Layer 1: Breadth — PM commitment layer; produces foundational scout signals Layer 2 depends on ----
    - name: [commitment-derived label — e.g., "market-and-feasibility-commitment"]
      # Commitment: C-01 — PM: "[commitment statement from register]"
      # Owner: PM
      # Consumes: []
      # Produces: [scout artifact types committed in C-01]
      skills: [scout:feasibility, scout:market]   # replace with C-01 applicable skills
      gate: "[C-01 artifact-types present]; commitment C-01 fulfilled [+ >=N threshold]"

    # ---- Layer 1 -> Layer 2: C-01 fulfilled; architect commitment can begin ----

    # ---- Layer 2: Depth — architect + dev commitment layer; requires C-01 fulfilled ----
    - name: [commitment-derived label — e.g., "design-commitment"]
      # Commitment: C-02 — Architect: "[commitment statement from register]"
      # Owner: Architect
      # Consumes: [Layer 1 scout artifact types from C-01]
      # Produces: [spec/prototype artifact types committed in C-02]
      skills: [draft:spec, prove:prototype]   # replace with C-02 applicable skills
      gate: "[C-02 artifact-types present]; commitment C-02 fulfilled; no P0 gaps"

    - name: [commitment-derived label — e.g., "validation-commitment"]
      # Commitment: C-03 — Architect + Dev: "[commitment statement from register]"
      # Owner: Architect + Dev
      # Consumes: [Layer 2a design artifact types from C-02]
      # Produces: [review/flow/trace artifact types committed in C-03]
      skills: [review:design, flow:lifecycle, trace:contract]   # replace with C-03 applicable skills
      gate: "[C-03 artifact-types present]; commitment C-03 fulfilled; <=N open findings"

    # ---- Layer 2 -> Layer 3: C-02 and C-03 fulfilled; PM+team commitment can begin ----

    # ---- Layer 3: Synthesis — requires the full validated artifact context from prior layers ----
    - name: [commitment-derived label — e.g., "readiness-commitment"]
      # Commitment: C-04 — PM + Team: "[commitment statement from register]"
      # Owner: PM + Team
      # Consumes: [Layer 2 validated artifact types from C-03]
      # Produces: [listen/topic artifact types committed in C-04]
      skills: [listen:adoption, topic:status]   # replace with C-04 applicable skills
      gate: "[C-04 artifact-types present]; commitment C-04 fulfilled [+ >=N evaluation count]"

    # ---- Terminal stage — do not modify ----
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"

    ## Plan Verification
    # [ ] Echo is last, skills: [], auto: true, no gate
    # [ ] Every non-echo stage has a commitment ID, owner, consumes, produces, and contract clause gate
    # [ ] Every gate names a commitment and artifact condition — not a social or execution state
    # [ ] At least one gate carries a numeric threshold (>=N or <=N)
    # [ ] Commitment order: PM (L1) -> Architect (L2a) -> Architect+Dev (L2b) -> PM+Team (L3)
    # [ ] Every skill name belongs to a valid Signal namespace
    # [ ] This plan does not execute skills — each skill runs standalone
```

---

## V-05 — Combined: All R9 Axes

**Axes:** Coaching voice + open question inventory (Q-NN) + risk-retirement (R-NN) + role
commitment (C-NN) + consumer-pull backward derivation (handoff matrix). All R9 axes in a single
variation with maximum structural density. The meeting narrative is the richest of any R9
variation: it names roles, shows unregistered risks, questions assumed-closed, and verbal
commitments replacing artifact contracts. The not-executor identity emerges from a four-point
failure diagnosis.

**Hypothesis:** R8 V-05 (all axes) scored 99.09 because C-28/C-29 were not yet in the rubric.
Here, the R8 V-05 structure (zone-anchor + handoff-matrix + constraint language) is replaced by
a richer combined structure that adds meeting narrative, Q-NN question inventory, R-NN risk
register, and C-NN commitment register as a unified pre-derivation index, then uses the
consumer-pull handoff matrix (proven 100% in R8 V-02) as the backward-derivation artifact.
Anticipated score: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

Here is a planning meeting your team probably recognizes. Your PM opens a doc and says: "Let's put
together a quick plan." Your architect looks at the PM's one-pager and says: "I think the design
is pretty clear from what you've written — I can start on the spec." Your developer says: "Just
let me know when the spec is ready." Your PM says: "I'll handle the go-to-market stuff at the
end." The meeting ends in ten minutes. Your plan looks like this:

```yaml
# What that meeting produced for {{topic}}:
stages:
  - name: research
    skills: [scout:market, scout:feasibility, draft:spec]
    gate: "research done, spec drafted"
  - name: build
    skills: [flow:lifecycle, trace:contract, prove:prototype, review:design]
    gate: "build complete"
  - name: launch
    skills: [listen:adoption, topic:status]
    gate: "shipped"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

Here is what is wrong with that conversation and the plan it produced:

1. **Your team named no open questions.** "The design is pretty clear" is an assumption, not a
   question closure. If nobody names the open questions, nobody knows which stages answer them.
2. **Your team registered no risks.** Your architect started the spec before `scout:feasibility`
   ran. The spec is contingent on an unretired existential risk. If feasibility fails, the spec
   is waste.
3. **Your team made verbal commitments without artifact contracts.** "I'll handle the go-to-market
   stuff" is a direction, not a commitment. Nobody named what the PM would produce or when it
   would be considered fulfilled.
4. **Your stages collapsed the arc.** `draft:spec` in the same stage as `scout:market` means the
   spec is drafted in parallel with the signal that should inform it. `review:design` in the same
   stage as `prove:prototype` means the design is reviewed before the prototype has challenged
   its assumptions.

`/program:plan` is not a workflow executor. It names your open questions, retires your risks in
the right order, anchors each stage to a role commitment, and sequences everything backward from
echo so that every Produces/Consumes boundary is a bilateral contract — not a verbal agreement.

---

**Before you build your plan, read these four tables.**

---

**Table 1 — Evidence arc: layers, roles, arc role, and what each layer produces for the next**

| Layer | Arc name | Role owner | Q-NN type closed | R-NN type retired | Produces for next layer | Dependency |
|-------|----------|------------|-----------------|-------------------|------------------------|------------|
| Layer 1 (Breadth) | Discovery | PM | Foundational questions (feasibility, market) | Existential risks | Scout signal artifacts | None — first layer |
| Layer 2a (Depth-Design) | Design | Architect | Design questions (spec, prototype) | Design risks | Spec and prototype artifacts | Requires Layer 1 artifacts |
| Layer 2b (Depth-Validation) | Validation | Architect + Dev | Validation questions (quality, correctness) | Validation risks | Validated artifacts | Requires Layer 2a artifacts |
| Layer 3 (Synthesis) | Readiness | PM + Team | Readiness questions (adoption, alignment) | Launch risks | Synthesis artifacts for echo | Requires full validated context from prior layers |
| Terminal | Echo | Auto | Retrospective question | None retired | — | All prior layers complete |

---

**Table 2 — Gate design: BAD vs GOOD**

| BAD gate | Failure mode | GOOD gate |
|----------|--------------|-----------|
| `"research done, spec drafted"` | Bundles Layer 1 and 2; spec drafted before signals exist | `"scout-feasibility and scout-market artifacts present; >=2 signals; Q-01 answered"` |
| `"build complete"` | Execution state, no artifact condition named | `"draft-spec present, no P0 gaps (R-02 retired); review-design + flow artifacts present, <=3 findings"` |
| `"shipped"` | Outcome state, not evidence state | `"listen-adoption signal present, >=3 persona evaluations (R-04 retired)"` |
| `"done"` | Not a condition | `"[named artifact-types] present [quality condition, numeric threshold]"` |

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

---

**Table 4 — Pre-derivation index: your Q-NN open questions, R-NN risks, C-NN commitments**

Before writing stage YAML, fill in all three indexes. Each stage in YAML corresponds to a row here.

```
Unified Pre-Derivation Index for {{topic}}

| Stage | Layer | Q-NN: Open question | R-NN: Risk retired | C-NN: Role commitment | Artifact produced | Gate clause |
|-------|-------|--------------------|--------------------|----------------------|-------------------|-------------|
| discovery | Layer 1 | Q-01: [feasibility/market question] | R-01: [existential risk] | C-01: PM commits to scout signals | [scout artifact types] | [artifact present + >=N threshold] |
| design | Layer 2a | Q-02: [design/spec question] | R-02: [design risk] | C-02: Architect commits to spec/prototype | [spec, prototype types] | [artifact present, no P0 gaps] |
| validation | Layer 2b | Q-03: [validation question] | R-03: [validation risk] | C-03: Architect+Dev commit to validated artifacts | [review, flow, trace types] | [artifact present, <=N findings] |
| readiness | Layer 3 | Q-04: [readiness question] | R-04: [launch risk] | C-04: PM+Team commit to readiness artifacts | [listen, topic types] | [artifact present + >=N evaluations] |
```

---

**Before writing stage YAML, complete the handoff matrix.**

Fill backward from echo (row 0). Each row's Produces is derived from the Consumes of the row above
(consumer-pull rule). Verify Produces(row N) = Consumes(row N-1) at every adjacent pair before
writing YAML.

```
Handoff Matrix for {{topic}} (fill backward from row 0)

Consumer-pull rule: Produces(row N) = Consumes(row N-1 above).

| Row | Stage | Layer | Produces | Consumes (row above) | Gate clause | Owner |
|-----|-------|-------|----------|----------------------|-------------|-------|
| 0 | echo | Terminal | — | [What must exist for echo to have retrospective content?] | auto: true | Auto |
| 4 | readiness | Layer 3 | [= row 0 Consumes] | [What Layer 3 needs from Layer 2b] | [readiness + >=N count] | PM+Team |
| 3 | validation | Layer 2b | [= row 4 Consumes] | [What Layer 2b needs from Layer 2a] | [validated + <=N findings] | Arch+Dev |
| 2 | design | Layer 2a | [= row 3 Consumes] | [What Layer 2a needs from Layer 1] | [spec/prototype condition] | Architect |
| 1 | discovery | Layer 1 | [= row 2 Consumes] | [] (first stage) | [scout + >=N threshold] | PM |
```

---

**Layer 1 (Breadth) — your PM's commitment layer, which closes your foundational open questions, retires existential risks, and produces the scout signal artifacts Layer 2 requires:**

Your PM's Layer 1 commitment answers the questions your team does not yet know it is asking.
Feasibility: is `{{topic}}` buildable given your constraints? Market: is there demand? Stakeholders:
who has veto power? Compliance: what are the non-negotiable constraints? These are your Q-01
questions and your R-01 existential risks — if left open, each becomes an assumption that Layer 2
builds on top of. The scout-namespace skills produce the signals that close Q-01 and retire R-01.
Your PM's gate condition is the artifact evidence that proves the commitment fulfilled: named
artifact types, with a numeric threshold.

**Layer 2 (Depth) — your architect's and dev's commitment layer, which requires your PM's Layer 1 artifacts and produces validated artifacts your PM's Layer 3 commitment depends on:**

Layer 2 is a two-phase commitment your architect and dev share. First, your architect closes the
design questions (Q-02) and retires the design risks (R-02) by producing a spec and prototype —
but cannot start until your PM's Layer 1 artifacts exist. A spec written before `scout:feasibility`
has run is a document built on unretired risk. Second, your architect and dev together close the
validation questions (Q-03) and retire the validation risks (R-03) — but cannot start until the
spec from Layer 2a exists. The handoff matrix makes the bilateral contract at every boundary
auditable: Layer 2a Produces = Layer 2b Consumes, by column scan.

**Layer 3 (Synthesis) — your PM and team's final commitment layer, which requires the full validated artifact context from prior layers to give your readiness questions their meaning:**

Layer 3 is where your team commits to answering the readiness question (Q-04) and retiring the
launch risks (R-04). But "ready" is not in the gate vocabulary — the gate names artifact types
and evaluation counts. Your listen-namespace skills gather adoption readiness signals. Your topic-
namespace skills synthesize the full artifact set. Neither is meaningful without Layers 1 and 2
complete: you cannot assess adoption readiness for a feature with unretired design risks. The
handoff matrix confirms Layer 3 Produces = what echo implicitly Consumes.

**The echo stage — why it closes all four indexes simultaneously:**

1. **Echo carries no Q-NN, R-NN, or C-NN entries because the investigation is complete.** Every
   question in your Q-NN inventory was answered. Every risk in your R-NN register was retired.
   Every commitment in your C-NN register was fulfilled. Echo's only job is retrospective: to ask
   what you learned that you did not expect. It cannot close an open question or retire a risk —
   those are all gone. Echo is what remains when the arc is exhausted.
2. **`auto: true` encodes that retrospection is a consequence of completion, not a gate condition.**
   There is no "retrospection gate." When the final Layer 3 gate passes, echo runs. Your job at
   that point is not to decide whether to run it — it is to answer its question.
3. **Echo's architectural role is to guarantee your program has a defined terminal state.** Without
   echo, a program could be abandoned at any stage and claim informal completion. With echo, the
   program has a structural close — all indexes exhausted, all contracts fulfilled, reflection
   remaining.

---

**Your program.yaml template — fill all indexes from the pre-derivation table and handoff matrix.**

```yaml
# REQUIRED: preserve this comment — this program is a plan, not an executor.
# Skills run standalone. This YAML sequences evidence-gathering; it does not execute it.
# All Q-NN, R-NN, C-NN indexes and the handoff matrix must be completed before this YAML is filled.

program:
  topic: "{{topic}}"
  strategy: "{{strategy}}"
  stages:

    # ---- Layer 1: Breadth — closes Q-01, retires R-01, fulfills C-01; produces scout signals Layer 2 requires ----
    - name: [Q-01 gap-derived label]
      # Q-ref: Q-01 — "[open question from index]"
      # Risk: R-01 — "[risk from index]"; retirement condition: [gate clause]
      # Commitment: C-01 — PM: "[commitment from index]"
      # Owner: PM
      # Consumes: []
      # Produces: [scout artifact types from handoff matrix row 1]
      skills: [scout:feasibility, scout:market]   # replace with Q-01/R-01 applicable skills
      gate: "[produces artifact-types present]; Q-01 answered; R-01 RETIRED [+ >=N threshold]"

    # ---- Layer 1 -> Layer 2 boundary: Q-01 answered, R-01 retired, C-01 fulfilled ----
    # Layer 1 Produces: [artifact types] — Layer 2 Consumes: [same]

    # ---- Layer 2: Depth — closes Q-02/Q-03, retires R-02/R-03, fulfills C-02/C-03 ----
    - name: [Q-02 gap-derived label]
      # Q-ref: Q-02 — "[open question from index]"
      # Risk: R-02 — "[risk from index]"
      # Commitment: C-02 — Architect: "[commitment from index]"
      # Owner: Architect
      # Consumes: [Layer 1 scout artifact types from matrix row 1 Produces]
      # Produces: [spec/prototype types from matrix row 2 — = row 3 Consumes]
      skills: [draft:spec, prove:prototype]   # replace with Q-02/R-02 applicable skills
      gate: "[produces artifact-types present]; Q-02 answered; R-02 RETIRED; no P0 gaps"

    - name: [Q-03 gap-derived label]
      # Q-ref: Q-03 — "[open question from index]"
      # Risk: R-03 — "[risk from index]"
      # Commitment: C-03 — Architect + Dev: "[commitment from index]"
      # Owner: Architect + Dev
      # Consumes: [Layer 2a artifact types from matrix row 2 Produces]
      # Produces: [review/flow/trace types from matrix row 3 — = row 4 Consumes]
      skills: [review:design, flow:lifecycle, trace:contract]   # replace with Q-03/R-03 skills
      gate: "[produces artifact-types present]; Q-03 answered; R-03 RETIRED; <=N open findings"

    # ---- Layer 2 -> Layer 3 boundary: Q-02/Q-03 answered, R-02/R-03 retired, C-02/C-03 fulfilled ----
    # Layer 2 Produces: [artifact types] — Layer 3 Consumes: [same]

    # ---- Layer 3: Synthesis — requires the full validated artifact context from prior layers ----
    - name: [Q-04 gap-derived label]
      # Q-ref: Q-04 — "[open question from index]"
      # Risk: R-04 — "[risk from index]"
      # Commitment: C-04 — PM + Team: "[commitment from index]"
      # Owner: PM + Team
      # Consumes: [Layer 2 validated artifact types from matrix row 3 Produces]
      # Produces: [listen/topic artifact types from matrix row 4 — = row 0 Consumes]
      skills: [listen:adoption, topic:status]   # replace with Q-04/R-04 applicable skills
      gate: "[produces artifact-types present]; Q-04 answered; R-04 RETIRED [+ >=N evaluation count]"

    # ---- Terminal stage — do not modify ----
    - name: echo
      skills: []
      auto: true
      question: "What did we learn that we didn't expect?"

    ## Plan Verification
    # [ ] Echo is last, skills: [], auto: true, no gate field
    # [ ] Every non-echo stage has Q-ref, Risk, Commitment, Owner, Consumes, Produces, and gate
    # [ ] Every gate names artifact types + quality condition — no execution or social state
    # [ ] At least one gate has a numeric threshold (>=N or <=N)
    # [ ] Handoff matrix verified: Produces(row N) = Consumes(row N-1) at all boundaries
    # [ ] Stage order: Layer 1 -> Layer 2a -> Layer 2b -> Layer 3 -> echo
    # [ ] Every skill name belongs to a valid Signal namespace
    # [ ] This plan does not execute skills — each skill runs standalone
```

---

## R9 Axis Coverage Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| **BASELINE: C-28 meeting narrative** | X | X | X | X | X |
| **BASELINE: C-29 process-replacement identity** | X | X | X | X | X |
| Phrasing register (second-person coaching) | X | | | | X |
| Output format (open question inventory Q-NN) | | X | | | X |
| Lifecycle emphasis (risk-retirement arc R-NN) | | | X | | X |
| Role sequence + commitment contract (C-NN) | | | | X | X |
| Consumer-pull backward derivation (handoff matrix) | | | | | X |

## Anticipated Scores (v25 rubric)

| Variation | C-28 | C-29 | Aspirational | Composite |
|-----------|------|------|-------------|-----------|
| V-01 (Coaching voice) | PASS — "Your team just wrapped a fifteen-minute planning sync"; PM types "done" | PASS — "exists to replace this conversation and the plan it produces" | 22/22 | 100.00 |
| V-02 (Question inventory) | PASS — 12-minute sync, 4-person team, nobody writes open questions | PASS — "exists to replace this conversation and the plan it produces" | 22/22 | 100.00 |
| V-03 (Risk retirement) | PASS — 3-week downstream failure traced to unretired feasibility risk; plan shown | PASS — "exists to replace this conversation and the plan it produces" | 22/22 | 100.00 |
| V-04 (Commitment contract) | PASS — 4-role meeting, "I'll handle that" verbal commitments without artifact naming | PASS — "exists to replace this conversation and the plan it produces" | 22/22 | 100.00 |
| V-05 (All axes) | PASS — richest narrative: PM says "pretty clear from what you've written"; 4-point failure diagnosis | PASS — "exists to replace this conversation and the plan it produces" | 22/22 | 100.00 |
