---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 6
rubric: v22
---

# program-plan -- R6 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v22 (C-01 through C-21, 21 criteria, golden = all essential pass
AND composite >= 80).

---

## R5 Retrospective Under v22 Rubric

v22 adds two aspirational criteria:

- **C-20** (per-layer arc narration): dedicated prose paragraph per arc layer narrating each
  layer's artifact scope and handoff role. Three paragraphs total, each scoped to one named layer.
  A combined summary paragraph does not pass. Requires C-17 PASS.
- **C-21** (echo stage narrated in prose): dedicated paragraph before the template explaining why
  echo carries no skills, what `auto: true` means architecturally, and how echo signals arc
  closure. Independent of C-02. Parenthetical or inline mention does not pass.

Retroactive scoring of R5 variations under v22:

| Variation | C-20 | C-21 | v22 aspirational | v22 score |
|-----------|------|------|-----------------|-----------|
| V-01 (Inertia + C-19) | FAIL -- arc is in table only; no layer narration paragraphs | FAIL -- echo is a table row | 11/14 = 7.81 pts | ~98/100 |
| V-02 (Table-Rich) | FAIL -- no layer narration paragraphs | FAIL -- echo is a table row | 10/14 = 7.10 pts | ~97/100 |
| V-03 (Lifecycle) | **PASS** -- Layer 1/2/3 narration paragraphs each dedicated to one layer (source signal for C-20) | FAIL -- "Echo is automatic and has no skills. It always runs last." is one line; does not address why echo carries no skills, what auto:true means architecturally, or how echo signals arc closure | 12/14 = 8.52 pts | ~99/100 |
| V-04 (C-16+C-17+C-18+C-19) | **PASS** -- three separate paragraphs beginning "Layer 1...", "Layer 2...", "Layer 3...", each covering artifact scope and handoff role | FAIL -- echo appears only in arc table and YAML; no prose paragraph | 12/14 = 8.52 pts | ~99/100 |
| V-05 (Golden) | **PASS** -- same paragraph structure as V-04 | FAIL -- same gap as V-04 | 12/14 = 8.52 pts | ~99/100 |

**R5 C-21 gap**: All five R5 variations miss C-21. Echo treatment across all five is either a
table row, a one-line mention, or YAML placement only. None dedicates a paragraph to echo's
architectural role. The required paragraph must address three elements: (1) why echo carries no
skills, (2) what `auto: true` means architecturally, (3) how echo signals arc closure.

**R5 C-20 status**: V-03, V-04, V-05 already pass C-20. V-01 and V-02 (table-dominant formats)
do not pass because arc is presented in tabular form only.

**R6 target**: The primary gap is C-21. Variations should: (1) probe C-21 in isolation on the
lifecycle base that already passes C-20; (2) test formal register with C-20 + C-21; (3) add C-21
to the contrast-first (C-16) spine; (4) combine all three; (5) golden synthesis.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Echo stage narration | C-21 probe on V-03 lifecycle base | Minimal C-21 fix: does a 3-element echo paragraph pass with no other structural changes? |
| Phrasing register (formal) | Formal register, C-20 + C-21 | Does formal/architectural language produce crisper per-layer and echo paragraphs? C-16 FAIL by design. |
| Inertia framing + C-21 | C-16 spine + C-21 | Echo paragraph after identity conclusion -- does this preserve C-16 (BAD still opens cold)? |
| Combined: C-16 + C-20 + C-21 | Contrast-first + per-layer + echo | All three main new-criteria paths together; arc tables and YAML annotations carried forward. |
| Golden synthesis | All 21 criteria | Full coverage with belt-and-suspenders on every site. |

Single-axis: V-01 (C-21 probe), V-02 (formal register), V-03 (inertia + C-21)
Combined: V-04 (C-16 + C-20 + C-21), V-05 (all 21)

---

## V-01 -- C-21 Echo Paragraph Probe (single-axis: echo stage narration)

**Axis**: Echo stage narration -- minimal C-21 fix applied to R5 V-03 lifecycle base. The three
layer narration paragraphs (C-20) are carried forward from R5 V-03 unchanged. The single-axis
change is replacing the one-line echo mention with a full paragraph addressing all three required
C-21 elements: why echo carries no skills, what `auto: true` means architecturally, and how echo
signals arc closure. All other V-03 structural choices preserved.
**Hypothesis**: A dedicated echo paragraph placed after the Layer 3 narration and before the arc
reference table is the minimal change required for C-21. C-20 is not affected (layer paragraphs
identical to R5 V-03). C-16 FAIL by design (identity opens the prompt, not BAD-first). Expected:
C-20 PASS (inherited from R5 V-03), C-21 PASS, C-16 FAIL -- 13/14 aspirational = ~99/100.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

Signal programs move through phases. Each phase produces artifacts the next phase requires. The
ordering is not a convention -- it is a dependency graph. A `draft:spec` requires feasibility
signals from Layer 1 before it is design rather than speculation. A `review:design` requires a
spec before it can review anything. A `flow:lifecycle` simulation requires a reviewed design
before its results mean anything. The program's value is not the list of skills; it is the gate
that enforces each handoff.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact lifecycle -- why stages are ordered:**

**Layer 1: Breadth** runs scout skills and early prove skills (`prove:websearch`,
`prove:intelligence`, `prove:hypothesis`). These produce the feasibility, requirements, market,
and competitor signals that Layer 2 needs before it can design anything. A `draft:spec` without
feasibility and requirements signals is speculation, not engineering. Layer 1's signals are
Layer 2's required input; the gate between them makes this dependency checkable by the next
phase owner.

**Layer 2: Depth** has sub-stages ordered by what each sub-stage produces. The design sub-stage
produces the `draft-spec` artifact -- the central document everything downstream depends on. The
validation sub-stage (`review:design`, `review:users`, `prove:prototype`) cannot run before the
spec exists: `review:design` reviews a specification, and without a specification there is nothing
to review. The gate between design and validation states this dependency explicitly: the next
phase owner checks that `draft-spec` is present before any review skill starts. Flow and trace
skills run after review because they simulate and trace a validated design -- tracing a contract
that has not been reviewed for correctness propagates unvalidated assumptions into the simulation.

**Layer 3: Synthesis** runs `listen:*` and `topic:*` last because they synthesize across all
prior signals. `listen:adoption` requires the validated design context that Layer 2 produced.
`topic:story` requires the full evidence arc to tell a coherent narrative. Running synthesis
before validation produces a story built on unvalidated signals.

**Echo** is the final stage of every Signal program. It carries no skills because it serves a
different purpose than any prior stage: it closes the evidence arc rather than contributing to it.
By the time echo runs, all evidence has been gathered (Layer 1), designed and validated
(Layer 2), and synthesized (Layer 3) -- there is nothing left to produce, and adding skills to
echo would mean running evidence work in a terminal stage with no downstream gate capable of
verifying that evidence before the program closes. The `auto: true` declaration means echo does
not wait for a human reviewer to inspect a gate condition and advance the plan -- there is no
gate condition to inspect. Echo closes automatically once all prior stages have reached their
gates. This is its architectural contract: echo is a terminal marker, not a checkpoint. When
echo closes, the program's evidence arc is complete and the topic's signal archive is coherent.

---

**Evidence arc:**

| Layer | Namespaces | Arc role | Produces | Requires |
|-------|------------|----------|----------|----------|
| 1: Breadth | scout, prove (early) | Exploration | Scout signals, feasibility/requirements artifacts | (none) |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (Layer 2b) |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers |
| (auto) | -- | Echo | -- | (none) |

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"all Layer 1 skills run"` | NO -- unverifiable by next phase owner |
| Empty or vague | `"done"` / `""` | NO -- names nothing checkable |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + C-09 |

At least one non-echo gate must be quantified.

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
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<scout artifacts Layer 2 design requires; numeric threshold: '>= N scout signals'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
      gate: "<draft-spec artifact present>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- arc closure, auto:true, no skills; see prose above ----

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

## V-02 -- Formal Register + C-21 (single-axis: phrasing register)

**Axis**: Phrasing register -- formal/architectural language throughout. Same structural coverage
as V-01 (C-20 via three layer paragraphs, C-21 via echo paragraph, C-19 via two tables, C-17 via
explicit dependency sentences) but expressed in specification-register prose ("Layer 1 produces
the following artifact classes:... Layer 1's handoff contract with Layer 2:...") rather than
narrative prose. Identity opens the prompt (C-12 PASS, C-16 FAIL by design -- single-axis cost).
**Hypothesis**: Formal register produces crisper per-layer scoping that is unambiguously
paragraph-per-layer to a scorer -- no ambiguity about whether paragraphs are combined vs.
dedicated. Echo paragraph in formal register ("The echo stage satisfies the following contract:")
is equally unambiguous about its dedicated subject. Expected: C-20 PASS, C-21 PASS, C-16 FAIL
-- 13/14 aspirational = ~99/100.

---

### Prompt body

**`/program:plan` produces a plan, not an executor.**

This skill sequences Signal plugin skills into staged phases with named gates. Each stage declares
which skills to run and what evidence must exist before the next stage begins. Skills remain
independently runnable -- the program carries no automation authority, advances no state, and
enforces no execution order. Its only product is the gate: a shared, evidence-specific condition
encoding what must be true before advancing.

---

You are running `/program:plan` for topic **{{topic}}**.

**Layer 1 (Breadth) -- artifact scope and handoff contract:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Artifact classes produced in Layer 1: feasibility signals, requirements signals, market signals,
competitor signals, compliance signals. Skills that produce these artifacts belong to the `scout`
namespace; early `prove` skills (`prove:websearch`, `prove:intelligence`, `prove:hypothesis`) may
also run here. Layer 1 requires no prior signals -- it is the program entry point. Layer 1's
handoff contract with Layer 2: a `draft:spec` skill may not start until Layer 1 has produced the
feasibility and requirements artifacts that the spec will encode. A spec authored without these
signals encodes assumptions, not evidence.

**Layer 2 (Depth) -- artifact scope and handoff contract:**

Layer 2 produces the design, validation, and simulation artifact set. It has internal dependency
constraints. Sub-stage ordering within Layer 2: (1) design sub-stage -- `draft:spec` or
`draft:proposal` runs first, producing the `draft-spec` artifact; (2) validation sub-stage --
`review:design`, `review:users`, `prove:prototype` run after, each requiring the `draft-spec`
artifact as input (`review:design` reviews a specification; without a specification the review
has no object); (3) simulation sub-stage -- `flow:*` and `trace:*` skills run last, each
requiring review artifacts as precondition (tracing a contract that has not been reviewed for
correctness propagates unvalidated design decisions into simulation output). Layer 2's handoff
contract with Layer 3: synthesis skills may not start until the validated-design context --
reviewed spec, proved prototype, simulated flows -- is present.

**Layer 3 (Synthesis) -- artifact scope and handoff contract:**

Layer 3 produces the synthesis artifact set: adoption signals, feedback signals, topic artifacts
(story, report, status). Skills in this layer (`listen:adoption`, `listen:feedback`,
`topic:story`, `topic:report`) require the complete validated-design context from Layers 1 and 2
as their input. Running `listen:adoption` before validation synthesizes signals that have not
been validated; the synthesis output degrades accordingly. Running `topic:story` before all
signals are archived produces a narrative over a partial evidence set. Layer 3 has no downstream
handoff contract -- it is the final evidence-producing layer. Its gate marks the completion of
the full evidence arc.

**Echo stage -- architectural contract:**

The echo stage satisfies the following contract: it carries no skills, is marked `auto: true`,
and is always the last stage. (1) **No skills** -- echo's function is arc closure, not evidence
production. All evidence was produced across Layers 1-3; adding skills to echo would mean running
evidence work in a terminal stage with no subsequent gate capable of verifying that evidence.
Echo is not a spillover stage for skills that did not fit elsewhere. (2) **`auto: true`** -- echo
does not wait for a human reviewer to inspect a gate and advance. There is no gate condition to
inspect; the arc has already closed. `auto: true` declares that the program's completion is
automatic upon all prior stages reaching their gates. (3) **Arc closure function** -- when echo
closes, the program signals that the topic's full evidence arc is complete: breadth signals
gathered (Layer 1), design validated (Layer 2), synthesis produced (Layer 3). Echo is the receipt
of the completed program.

---

**Evidence arc reference:**

| Layer | Namespaces | Artifact scope | Precondition | Gate checkpoint |
|-------|------------|----------------|--------------|-----------------|
| 1: Breadth | scout, prove (early) | Feasibility, requirements, market, competitor signals | (none) | >= N scout signals present |
| 2a: Design | draft | draft-spec artifact | Layer 1 signals present | draft-spec artifact present |
| 2b: Validation | review, prove | Review/prove artifacts | draft-spec present | 0 P0 findings open |
| 2c: Simulation | flow, trace | Flow/trace artifacts | review:* artifacts present | flow/trace artifacts present |
| 3: Synthesis | listen, topic | Listen/topic artifacts | All prior layers | All prior signals archived |
| (auto) | -- | (none) | All prior gates reached | (none -- auto:true) |

**Gate design reference:**

| Property | Failing example | Passing example | Notes |
|----------|----------------|-----------------|-------|
| Evidence state | `"Layer 1 complete"` | `"scout-feasibility artifact present"` | Name the artifact, not the execution event |
| Non-trivial | `"done"` | `"draft-spec artifact present"` | Must name a checkable artifact or signal |
| Quantified (>= 1 required) | `"several scout signals"` | `">= 2 scout signals AND draft-spec present"` | Numeric threshold is machine-checkable in principle |

**Signal skill catalog:**

| Namespace | Skills |
|-----------|--------|
| scout | feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders |
| draft | spec, proposal, pitch |
| review | design, users, customers, code |
| flow | conversation, dataflow, lifecycle, resilience, throttle, trigger |
| trace | component, contract, deployment, migration, permissions, request, skill, state |
| prove | analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch |
| listen | adoption, feedback, support |
| program | plan |
| topic | echo, new, plan, report, status, story |

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification table verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence evidence goal>"

  stages:

  # ---- Layer 1: Breadth ----

    - name: "<breadth-phase-label>"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<scout artifact classes present; numeric threshold: '>= N signals'>"

  # ---- Layer 2: Depth ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"
      skills:
        - draft:<skill>
      gate: "<draft-spec artifact present>"

    - name: "<validation-phase-label>"
      skills:
        - review:<skill>
        - prove:<skill>
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # remove if flow/trace not needed
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis ----

    - name: "<synthesis-phase-label>"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived>"

  # ---- Final Stage: echo ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

| Property | Pass condition | Check |
|----------|---------------|-------|
| Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after | [ ] |
| Valid skills | All skill names from Signal's 9 namespaces; zero invented names | [ ] |
| Evidence gates | Every non-echo gate names artifact or signal state -- not execution state | [ ] |
| Quantified gate | >= 1 non-echo gate contains numeric threshold | [ ] |
| Descriptive names | Stage names are phase labels, not namespace names, not indices | [ ] |
| Layer comments | Layer 1 / Layer 2 / Layer 3 section comments present in YAML | [ ] |
| REQUIRED comment | `# REQUIRED: preserve this comment` line in YAML output | [ ] |

---

## V-03 -- Contrast-First + C-21 (single-axis: inertia framing)

**Axis**: Inertia framing -- BAD YAML opens cold (C-16), identity conclusion follows diagnosis,
then layer narration paragraphs (C-20) and echo paragraph (C-21) appear after the identity
conclusion. Tests whether C-21 placement after the identity block breaks C-16 (it should not --
BAD YAML still opens cold; echo paragraph is downstream of the contrast). Two pre-template tables
(C-19), YAML dependency annotations (C-18), arc layer labels (C-14) all carried forward from
R5 V-04.
**Hypothesis**: Echo paragraph placed after the contrast identity block does not disturb C-16
(BAD precedes diagnosis precedes identity). C-20 passes from the three layer narration paragraphs.
C-21 passes from the dedicated echo paragraph. C-16 + C-20 + C-21 all pass simultaneously.
Expected: C-16 PASS, C-20 PASS, C-21 PASS, C-19 PASS -- 14/14 aspirational = 100/100.

---

### Prompt body

```yaml
# This is how most Signal investigations get planned:

program:
  topic: "{{topic}}"
  stages:
    - name: "investigation"
      skills:
        - scout:feasibility
        - scout:requirements
        - draft:spec
        - review:design
        - trace:contract
        - listen:adoption
      gate: "done"
    - name: echo
      skills: []
      auto: true
```

Skills in the wrong order. A gate that verifies nothing. `review:design` cannot review a spec
that `draft:spec` has not yet produced -- these skills share a dependency but the plan treats
them as unordered peers. `trace:contract` runs before `review:design` has confirmed the contract
design is sound -- tracing an unreviewed contract propagates design errors into simulation.
`listen:adoption` synthesizes signals that have not been gathered or validated; there is nothing
coherent to synthesize. `"done"` tells no one when it is safe to advance; the team advances on
shared optimism, not shared evidence.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Skills remain independently runnable -- the program does not
execute them, advance stages, or carry any automation authority. Its value is the gate and the
arc: a shared, evidence-specific condition per phase, structured in the order that reflects how
artifacts depend on each other.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1: Breadth** produces the foundational signal set that Layer 2 requires before it can
design anything. Scout skills run here: `scout:feasibility`, `scout:requirements`,
`scout:market`, `scout:competitors`. A `draft:spec` written without feasibility and requirements
signals is speculation, not engineering. Layer 1's output is Layer 2's required input; the gate
between them makes this dependency checkable by the next phase owner before any design skill
starts.

**Layer 2: Depth** has sub-stages ordered by what each produces. The design sub-stage produces
the `draft-spec` artifact; the validation sub-stage (`review:design`, `prove:prototype`) requires
this artifact before any review skill can run -- `review:design` reviews a specification, and
without a specification there is nothing to review. The gate between design and validation states
this dependency explicitly: the next phase owner checks that `draft-spec` is present before
starting any review. Flow and trace skills require review artifacts before running -- tracing a
contract that has not been reviewed for correctness builds simulation on an unvalidated
foundation; these run last in Layer 2. Layer 2 hands Layer 3 a complete validated context.

**Layer 3: Synthesis** runs `listen:*` and `topic:*` last because they synthesize across all
prior signals. `listen:adoption` requires the validated context Layer 2 produced; `topic:story`
requires the full evidence arc to tell a coherent narrative. Running synthesis before validation
produces a story built on unvalidated signals. Layer 3's gate is the final evidence checkpoint
before the arc closes: all prior signals must be archived and no critical blockers must remain.

**Echo -- terminal arc closure:**

Echo carries no skills and runs automatically. Its role is different from every prior stage: it
does not produce evidence, it closes the evidence arc. By the time echo runs, all evidence has
been gathered (Layer 1), validated (Layer 2), and synthesized (Layer 3) -- there is nothing left
to produce, and adding skills to echo would mean running evidence work in a terminal stage with
no subsequent gate capable of verifying that evidence before the program closes. The `auto: true`
flag declares that echo does not require a human reviewer to inspect a gate and advance; there is
no gate condition for echo to satisfy. It closes automatically once all prior stages have reached
their gates. When echo closes, the signal archive is complete: the topic's full
breadth-depth-synthesis arc has been executed and all artifacts are present.

---

**Evidence arc:**

| Layer | Namespaces | Arc role | Produces | Requires |
|-------|------------|----------|----------|----------|
| 1: Breadth | scout, prove (early) | Exploration | Scout signals, feasibility/requirements artifacts | (none) |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (Layer 2b) |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers |
| (auto) | -- | Echo | -- | (none) |

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"Layer 1 complete"` | NO -- unverifiable by next phase owner |
| Empty or vague | `"done"` / `""` | NO -- names nothing |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + C-09 |

At least one non-echo gate must be quantified: `">= N"`, `"0 P0 findings open"`, or equivalent.

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

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<named scout artifacts; numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>
      gate: "<draft-spec artifact present>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>
        - prove:<skill>
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

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
- [ ] Both `# REQUIRED: preserve this comment` lines preserved in YAML output

---

## V-04 -- Combined: C-16 + C-20 + C-21 (axes: inertia framing + per-layer narration + echo)

**Axes**: Contrast-first structure (C-16) + three per-layer narration paragraphs (C-20) + full
echo paragraph (C-21) + three pre-template tables (arc, gate, skill catalog) for strong C-19 +
YAML dependency annotations (C-18). This is R5 V-04 with the C-21 echo paragraph added and the
skill catalog upgraded to a table (making three distinct pre-template tables). R5 V-04 already
achieved C-16, C-17, C-18, C-19, and all other 12 v21 criteria; the only addition is a dedicated
echo paragraph placed between the Layer 3 narration and the first reference table.
**Hypothesis**: Echo paragraph inserted after the Layer 3 narration and before the reference
tables satisfies C-21 without disturbing any prior passing criterion. C-16 unaffected (BAD still
opens cold; echo paragraph is well downstream of the contrast block). Expected: all 14 aspirational
PASS -- 100/100.

---

### Prompt body

```yaml
# This is how most Signal investigations get planned:

program:
  topic: "{{topic}}"
  stages:
    - name: "investigation"
      skills:
        - scout:feasibility
        - scout:requirements
        - draft:spec
        - review:design
        - trace:contract
        - listen:adoption
      gate: "done"
    - name: echo
      skills: []
      auto: true
```

Skills in the wrong order. A gate that verifies nothing. `review:design` cannot review a spec
that `draft:spec` has not yet produced -- these skills depend on each other but the plan treats
them as unordered peers. `trace:contract` runs before `review:design` has confirmed the contract
design is sound -- tracing an unreviewed contract propagates design errors into the simulation.
`listen:adoption` synthesizes signals that have not been gathered or validated; there is nothing
meaningful to synthesize. `"done"` tells no one when it is safe to advance; the team advances on
shared optimism, not shared evidence.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Skills remain independently runnable -- the program does not
execute them, advance stages, or carry any automation authority. Its value is the gate and the
arc: a shared, evidence-specific condition per phase, structured in the order that reflects how
artifacts depend on each other.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1: Breadth** produces the foundational signal set that Layer 2 requires before it can
design anything. Scout skills run here: `scout:feasibility`, `scout:requirements`,
`scout:market`, `scout:competitors`. A `draft:spec` written without feasibility and requirements
signals is speculation, not engineering. Layer 1's output is Layer 2's required input; the gate
between them makes this dependency checkable by the next phase owner before any design skill
starts.

**Layer 2: Depth** has sub-stages ordered by what each produces. The design sub-stage produces
the `draft-spec` artifact; the validation sub-stage (`review:design`, `prove:prototype`) requires
this artifact before any review skill can run -- `review:design` reviews a specification, and
without a specification there is nothing to review. The gate between design and validation states
this dependency explicitly: the next phase owner checks that `draft-spec` is present before
starting any review. Flow and trace skills require review artifacts before running -- tracing a
contract that has not been reviewed for correctness builds simulation on an unvalidated foundation;
these run last in Layer 2. Layer 2 hands Layer 3 a complete validated context.

**Layer 3: Synthesis** runs `listen:*` and `topic:*` last because they synthesize across all
prior signals. `listen:adoption` requires the validated context Layer 2 produced; `topic:story`
requires the full evidence arc to tell a coherent narrative. Running synthesis before validation
produces a story built on unvalidated signals. Layer 3's gate is the final evidence checkpoint:
all prior signals archived, no critical blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program, and its contract is architecturally distinct
from all prior stages. Echo carries no skills for one reason: all evidence production ends at
Layer 3. Echo's function is not to gather or validate evidence -- it is to mark that the
evidence arc has been completed. Adding skills to echo would mean running evidence work in a
terminal stage with no subsequent gate capable of certifying that evidence before the program's
close; the result would be ungated evidence appended after all validation has finished. The
`auto: true` declaration means echo does not require a human reviewer to inspect a gate condition
and advance the plan -- echo has no gate condition. When all prior stages have reached their
gates, echo closes automatically. This automatic closure is the program's completion signal: the
topic's full breadth-depth-synthesis arc is done, all artifacts are present, and the signal
archive is coherent.

---

**Evidence arc:**

| Layer | Namespaces | Arc role | Produces | Requires |
|-------|------------|----------|----------|----------|
| 1: Breadth | scout, prove (early) | Exploration | Scout signals, feasibility/requirements artifacts | (none) |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (Layer 2b) |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers |
| (auto) | -- | Echo | -- | (none) |

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"Layer 1 complete"` | NO -- unverifiable by next phase owner |
| Empty or vague | `"done"` / `""` | NO -- names nothing |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + C-09 |

At least one non-echo gate must be quantified: `">= N"`, `"0 P0 findings open"`, or equivalent.

**Signal skill catalog:**

| Namespace | Skills |
|-----------|--------|
| scout | feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders |
| draft | spec, proposal, pitch |
| review | design, users, customers, code |
| flow | conversation, dataflow, lifecycle, resilience, throttle, trigger |
| trace | component, contract, deployment, migration, permissions, request, skill, state |
| prove | analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch |
| listen | adoption, feedback, support |
| program | plan |
| topic | echo, new, plan, report, status, story |

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<named scout artifacts present; numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>
      gate: "<draft-spec artifact present>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>
        - prove:<skill>
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

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
- [ ] Three arc-layer comments (Layer 1 / Layer 2 / Layer 3) preserved in YAML
- [ ] Both `# REQUIRED: preserve this comment` lines preserved in YAML output

---

## V-05 -- Golden Synthesis (all 21 criteria)

**Axes**: All -- contrast-first (C-16), per-layer narration (C-20), echo paragraph (C-21), three
distinct pre-template tables (C-19), YAML-embedded dependency annotations (C-18), arc layer
labels in template (C-14), template-locked verification table (C-13), dual-site not-executor
anchoring with echo site as third reinforcement (C-15), quantified gate (C-09), deliberate
evidence arc (C-08), all essential and recommended criteria. Richest layer narration paragraphs,
most explicit echo paragraph, three-table pre-template reference section.
**Hypothesis**: All 21 criteria pass simultaneously. Layering the richer echo paragraph from
V-04 onto the belt-and-suspenders template structure from R5 V-05 achieves 100/100 under v22
with no weaknesses in any criterion. Expected: 14/14 aspirational -- 100/100.

---

### Prompt body

```yaml
# This is what a Signal investigation looks like when planned without an arc:

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
      gate: "done"
    - name: echo
      skills: []
      auto: true
```

One stage. One gate that verifies nothing. `review:design` requires a spec that `draft:spec`
has not yet produced -- they are in the same flat list with no ordering enforced. `flow:lifecycle`
simulates a lifecycle for a design that `review:design` has not yet validated -- simulation
results are built on an unreviewed design. `trace:request` traces a request path through an
unreviewed, unvalidated architecture. `listen:feedback` synthesizes feedback across signals that
have not been gathered or validated; there is nothing coherent to synthesize. `"done"` is
unverifiable: the next phase owner has no artifact to check, no threshold to compare against.
The team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before advancing.
A plan without meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1: Breadth** produces the foundational signal set that every downstream stage requires
as precondition. Scout skills run here -- `scout:feasibility`, `scout:requirements`,
`scout:market`, `scout:competitors` -- along with early prove skills (`prove:websearch`,
`prove:intelligence`, `prove:hypothesis`). These produce the feasibility, requirements, market,
and competitor artifacts that Layer 2 depends on before any design skill can start. Layer 1
requires no prior signals; it is the program entry point. A `draft:spec` written without Layer 1
feasibility and requirements signals is speculation -- it encodes what the author believes should
be built rather than what has been verified as needed. Layer 1's output is Layer 2's required
input; the gate between them makes this dependency checkable: the next phase owner can inspect
that named scout artifacts are present before any design skill starts.

**Layer 2: Depth** has internal ordering constraints arising from artifact dependencies within
the layer. The design sub-stage runs first and produces the `draft-spec` artifact -- the central
document that all subsequent Layer 2 skills require. The validation sub-stage (`review:design`,
`review:users`, `prove:prototype`) cannot run before the spec exists: `review:design` reviews a
specification, and without a specification the review has no object; `prove:prototype` explores
the design described in the spec. The gate between design and validation states this dependency
explicitly, making it checkable. Flow and trace skills run last in Layer 2 because they simulate
and trace a validated design -- `flow:lifecycle` simulates a lifecycle defined in a reviewed spec;
`trace:contract` traces a contract that has been reviewed for correctness. Running flow or trace
before review propagates unvalidated design assumptions into simulation output. Layer 2 hands
Layer 3 a complete validated context: reviewed design, proved prototype, simulated flows and
traced paths.

**Layer 3: Synthesis** runs `listen:*` and `topic:*` last because synthesis skills require the
complete evidence base to produce meaningful output. `listen:adoption` synthesizes adoption
signals across the validated design context that Layers 1 and 2 produced; running it before
validation means synthesizing signals that have not been validated. `listen:feedback` synthesizes
feedback across a signal set that has not yet been gathered. `topic:story` constructs a coherent
narrative from the full evidence arc; running it before all signals are archived produces a
narrative over a partial evidence set. `topic:report` summarizes findings across all layers; a
report produced before Layer 2 is complete will omit validation findings. Layer 3's gate is the
final evidence checkpoint: all prior signals archived, all prior artifacts present, no critical
blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program, and its contract is architecturally distinct
from all prior stages. Echo carries no skills for one reason: by the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate, or
synthesize. Adding skills to echo would mean running evidence work in a terminal stage with no
subsequent gate capable of certifying that evidence before the program closes; the work would be
ungated. Echo is not a spillover stage for skills that did not fit earlier layers. `auto: true`
declares that echo does not wait for a human reviewer to inspect a gate condition and advance the
plan -- echo has no gate condition. When all prior stages have reached their gates, echo closes
automatically. This automatic closure is the program's completion receipt: the full
breadth-depth-synthesis arc has been executed, all artifacts are present, all signals are
archived, and the topic's investigation is complete.

---

**Evidence arc reference:**

| Layer | Namespaces | Arc role | Produces | Requires | Gate type |
|-------|------------|----------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Exploration | Feasibility, requirements, market, competitor signals | (none) | Quantified: >= N scout signals |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Echo | -- | All prior gates reached | (none -- auto:true) |

**Gate design reference:**

| Gate quality | BAD example | GOOD example | Why it matters |
|---|---|---|---|
| Execution state | `"Layer 1 complete"` | `"scout-feasibility artifact present"` | Execution state is unverifiable by next phase owner |
| Empty or vague | `"done"` | `"draft-spec and scout-requirements artifacts present"` | Vague gate gives no artifact to check |
| Non-quantified | `"some scout signals"` | `">= 2 scout signals present"` | Count threshold is machine-checkable in principle |
| Quantified (best) | -- | `">= 2 scout signals AND draft-spec artifact present"` | Names artifact AND threshold |

At least one non-echo gate must be quantified: `">= N"`, `"0 P0 findings open"`, or equivalent.

**Signal skill catalog:**

| Namespace | Skills |
|-----------|--------|
| scout | feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders |
| draft | spec, proposal, pitch |
| review | design, users, customers, code |
| flow | conversation, dataflow, lifecycle, resilience, throttle, trigger |
| trace | component, contract, deployment, migration, permissions, request, skill, state |
| prove | analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch |
| listen | adoption, feedback, support |
| program | plan |
| topic | echo, new, plan, report, status, story |

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED comments
and the Plan Verification table verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts present; numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
      gate: "<draft-spec artifact present>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

| Property | Pass condition | Check |
|----------|---------------|-------|
| Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after | [ ] |
| Valid skills | All skill names from Signal's 9 namespaces; zero invented names | [ ] |
| Evidence gates | Every non-echo gate names artifact or signal state -- not execution state | [ ] |
| Quantified gate | >= 1 non-echo gate has numeric threshold | [ ] |
| Descriptive names | Stage names are phase labels, not namespace names, not indices | [ ] |
| Layer 1 comment | `# ---- Layer 1: Breadth ----` present in YAML | [ ] |
| Layer 2 comment | `# ---- Layer 2: Depth ----` with dependency annotation present in YAML | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present in YAML | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved in YAML | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved in YAML | [ ] |

---

## Predicted Scores Under v22

| Variation | Axis | C-16 | C-20 | C-21 | Other gaps | Aspirational | Score |
|-----------|------|------|------|------|------------|-------------|-------|
| V-01 | C-21 probe (lifecycle base) | FAIL | PASS | PASS | none | 13/14 = 9.24 pts | ~99/100 |
| V-02 | Formal register | FAIL | PASS | PASS | none | 13/14 = 9.24 pts | ~99/100 |
| V-03 | Inertia + C-21 | PASS | PASS | PASS | none | 14/14 = 9.94 pts | ~100/100 |
| V-04 | C-16 + C-20 + C-21 combined | PASS | PASS | PASS | none | 14/14 = 9.94 pts | ~100/100 |
| V-05 | Golden synthesis | PASS | PASS | PASS | none | 14/14 = 9.94 pts | ~100/100 |
