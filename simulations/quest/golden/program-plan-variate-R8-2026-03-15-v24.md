---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 8
rubric: v24
new_criteria: C-26, C-27
---

# program-plan -- R8 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v24 (C-01 through C-27, 27 criteria, golden = all essential PASS
AND composite >= 80).

---

## R7 Retrospective Under v24 Rubric

v24 adds two aspirational criteria beyond v23's 18:

- **C-26** (Layer header cross-layer dependency reference): At least one per-layer arc narration
  header (satisfying C-24) must name an adjacent layer by number or identity within its role
  descriptor. Canonical form: "produces the foundational signals **Layer 2** requires" -- the
  adjacent layer is named by identity in the header itself. A generic role label ("evidence breadth
  phase") passes C-24 but not C-26.

- **C-27** (Terminal layer header states context dependency): The Layer 3 / Synthesis header
  (satisfying C-24) must include a statement of what it requires from prior layers -- not only what
  it produces. "requires the full validated context" qualifies; "produces the synthesis artifact set"
  alone does not. C-26 and C-27 are independent: a header can satisfy C-27 without naming Layer 2
  by number (C-26), and vice versa.

Scoring adjustment: 18 → 20 aspirational criteria, 0.56 → 0.50 pts each. Total aspirational still
= 10 pts.

Re-scoring R7 variations at v24:

| Variation | C-26 | C-27 | asp/20 | composite |
|-----------|------|------|--------|-----------|
| V-01 (C-24 probe; role-labeled headers only) | PASS -- Layer 1 header: "produces the foundational signals **Layer 2** requires" | PASS -- Layer 3 header: "requires the full validated context" | 19/20 (C-25 FAIL -- flowing echo prose) | 99.50 |
| V-02 (C-25 probe; enumerated echo only) | re-run needed -- Layer headers unchanged from R6 V-05 ("**Layer N: Name**") | re-run needed | TBD | TBD |
| V-03 (C-24 + C-25 combined on V-05 base) | PASS -- inherits V-01 Layer 1 header | PASS -- inherits V-01 Layer 3 header | 20/20 | 100.00 |
| V-04 (C-24 + C-25 on V-04 base) | TBD | TBD | TBD | TBD |
| V-05 (golden synthesis) | TBD | TBD | TBD | TBD |

**R7 baseline**: V-03 is the current 100.00 reference. The winning header forms are:
- Layer 1: "**Layer 1 (Breadth) -- dependency origin; produces the foundational signals **Layer 2** requires:**"
- Layer 2: "**Layer 2 (Depth) -- artifact scope and internal handoff contracts:**"
- Layer 3: "**Layer 3 (Synthesis) -- produces the synthesis artifact set; requires the full validated context:**"

**R8 target**: Validate C-26/C-27 robustness across different phrasing registers and structural
axes. Test bidirectional cross-references. Test whether alternative header formulations that
preserve the winning structure can also achieve 100.00. All five variations target 100.00.

---

## Variation Axes

| Axis | Variation | Base | Hypothesis |
|------|-----------|------|------------|
| Phrasing register (formal/specification SHALL/MUST) | V-01 (single) | R7 V-03 | Converts conversational prose to formal constraint language; structural elements (headers, echo enumeration, tables, template) unchanged; C-24/C-26/C-27 headers preserved exactly; tests register neutrality |
| Inertia framing (narrative BAD scenario, C-16 maximized) | V-02 (single) | R7 V-03 | Replaces bad YAML opening with a team-conversation narrative that produces the bad YAML; richer C-16 signal; structural elements unchanged after opening; tests whether elaborate inertia framing disturbs any criterion |
| Layer header enrichment (bidirectional cross-references) | V-03 (single) | R7 V-03 | All three layer headers name adjacent layers; Layer 2 header names both Layer 1 AND Layer 3; Layer 3 header explicitly names Layer 2 as its source; tests whether richer cross-references (beyond C-26 minimum) cause any interference |
| Formal register + lifecycle emphasis (combined) | V-04 | R7 V-03 | Merges V-01 formal language with lifecycle-zone narration per layer; Layer headers use lifecycle terminology + bidirectional references; tests full-coverage formal register with lifecycle depth |
| All R8 axes -- golden synthesis (combined) | V-05 | R7 V-03 | Maximum: narrative BAD scenario (V-02) + bidirectional headers (V-03) + formal gate language (V-01) + deepest lifecycle narration (V-04) + richest tables; all 27 criteria targeted explicitly |

Single-axis: V-01 (register), V-02 (inertia), V-03 (headers). Combined: V-04 (register +
lifecycle), V-05 (all axes).

---

## V-01 -- Formal Specification Register (single-axis: phrasing register)

**Axis**: Phrasing register -- converts R7 V-03 from conversational/imperative prose to formal
specification constraint language (SHALL/MUST/NORMATIVE) throughout. The opening BAD example is
labeled as a non-conformant program instance. Diagnosis uses violation language. Identity uses
"SHALL replace." Layer narration paragraphs use SHALL/MUST framing for dependency constraints.
Echo enumeration uses formal obligation numbering. Gate table columns become "Non-conformant form"
and "Conformant form." The YAML template uses SHALL in gate language annotations.

**Structural elements preserved exactly from R7 V-03**: Same three-layer arc structure. Layer 1
header identical (naming Layer 2 for C-26). Layer 3 header identical (dependency clause for C-27).
Enumerated echo paragraph structure. Same four reference tables (arc, gate BAD/GOOD, skill catalog,
verification). Same YAML template layer dividers and preserve-required comments.

**Hypothesis**: Phrasing register is neutral to all structural criteria. C-24/C-26/C-27 are
determined by header text structure, not by surrounding prose register. C-25 is determined by echo
enumeration form. C-13/C-15 are determined by template skeleton structure. None of these depend on
the prose being conversational vs. formal. Expected: 20/20 aspirational, composite 100.00.

---

### Prompt body

```yaml
# NON-CONFORMANT PROGRAM-BAD-01: This program violates the arc-ordering constraint.

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

PROGRAM-BAD-01 is non-conformant on four counts. (1) `review:design` requires a `draft-spec`
artifact that `draft:spec` has not yet produced -- the constraint is not encoded; both skills are
co-listed in a single stage with no ordering guarantee. (2) `flow:lifecycle` SHALL NOT simulate a
lifecycle for a design that `review:design` has not yet validated; the simulation result propagates
unvalidated design assumptions. (3) `trace:request` SHALL NOT trace a request path through an
unreviewed architecture for the same reason. (4) The gate `"done"` is an execution-state predicate
-- it describes whether the stage has finished running, not whether the required evidence exists.
The next-phase owner has no artifact to check and no threshold to compare against; the gate is
unverifiable.

**`/program:plan` SHALL replace PROGRAM-BAD-01.**

It MUST produce a plan, not an executor. Every skill listed in the plan SHALL remain independently
runnable -- the program MUST NOT execute skills, advance stages, or carry automation authority. The
plan's only normative product is the gate: a declared evidence condition that MUST be met before
the next stage commences. A program with no evidence gates is not a plan; it is a flat skill list
with a naming wrapper.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages SHALL be ordered:**

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals **Layer 2** requires:**

Layer 1 SHALL produce the foundational signal set that every downstream stage requires as a
prerequisite. Scout skills run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`). These MUST produce the feasibility, requirements, market, and competitor
artifacts that Layer 2 depends on before any design skill commences. Layer 1 requires no prior
signals; it is the program entry point. A `draft:spec` written without Layer 1 feasibility and
requirements signals SHALL be treated as speculative -- it encodes the author's beliefs rather than
verified evidence of what should be built. Layer 1's output is Layer 2's required input; the gate
between them makes this dependency verifiable: the next-phase owner MUST be able to confirm that
named scout artifacts are present before any design skill starts.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts:**

Layer 2 has internal ordering constraints that MUST be respected. The design sub-stage SHALL run
first and produce the `draft-spec` artifact -- the central document that all subsequent Layer 2
skills require. The validation sub-stage (`review:design`, `review:users`, `prove:prototype`) SHALL
NOT run before the spec exists: `review:design` reviews a specification and without a specification
the review has no object; `prove:prototype` SHALL explore the design described in the spec. The gate
between design and validation MUST state this dependency explicitly, making it verifiable. Flow and
trace skills SHALL run last in Layer 2 because they simulate and trace a validated design --
`flow:lifecycle` simulates a lifecycle defined in a reviewed spec; `trace:contract` traces a
contract that has been reviewed for correctness. Running flow or trace before review SHALL be
considered a dependency-ordering violation; it propagates unvalidated design assumptions into
simulation output. Layer 2 SHALL hand Layer 3 a complete validated context: reviewed design, proved
prototype, simulated flows, and traced paths.

**Layer 3 (Synthesis) -- produces the synthesis artifact set; requires the full validated context:**

Layer 3 SHALL run `listen:*` and `topic:*` last because synthesis skills MUST have the complete
evidence base to produce valid output. `listen:adoption` SHALL synthesize adoption signals across
the validated design context that Layers 1 and 2 produced; running it before validation is a
constraint violation -- the synthesis depends on artifacts that have not yet been produced.
`listen:feedback` SHALL NOT synthesize feedback across signals that have not been gathered.
`topic:story` SHALL construct a coherent narrative from the full evidence arc; running it before all
signals are archived MUST be considered a violation -- the narrative covers a partial evidence set.
`topic:report` SHALL summarize findings across all layers; a report produced before Layer 2 is
complete is non-conformant because it will omit validation findings. Layer 3's gate is the final
evidence checkpoint: all prior signals MUST be archived, all prior artifacts MUST be present, and
there MUST be zero critical blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three normative
obligations:

(1) **Skill-free obligation (NORMATIVE)** -- Echo SHALL carry no skills. By the time echo runs,
all evidence production has ended across Layers 1, 2, and 3 -- there is no evidence remaining to
gather, validate, or synthesize. Adding skills to echo would mean running evidence work in a
terminal stage with no subsequent gate capable of certifying that evidence before the program
closes. The result would be ungated evidence appended after all validation has finished. Echo SHALL
NOT be used as a spillover stage for skills that did not fit earlier layers.

(2) **`auto: true` semantics (NORMATIVE)** -- Echo SHALL NOT wait for human gate inspection.
Echo has no gate condition; when all prior stages have reached their gates, echo MUST close
automatically. The `auto: true` declaration is not a convenience flag -- it is a normative
statement that the program's completion MUST NOT require human gate review at this stage, because
the arc has already closed at Layer 3's evidence gate.

(3) **Arc closure function (NORMATIVE)** -- When echo closes, the program SHALL signal that the
topic's full breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design
validated (Layer 2), synthesis produced (Layer 3). Echo is the program's completion receipt; the
signal archive is coherent and the topic's investigation is formally done.

---

**Evidence arc reference:**

| Layer | Namespaces | Arc role | Produces | Requires | Gate type |
|-------|------------|----------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Dependency origin | Feasibility, requirements, market, competitor signals | (none -- program entry) | Quantified: >= N scout signals |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Echo | -- | All prior gates reached | (none -- auto: true) |

**Gate conformance reference:**

| Violation class | Non-conformant form | Conformant form | Why it violates |
|----------------|---------------------|-----------------|-----------------|
| Execution state | `"Layer 1 complete"` | `"scout-feasibility artifact present"` | Execution state is unverifiable by next-phase owner |
| Empty / vague | `"done"` | `"draft-spec and scout-requirements artifacts present"` | No artifact to check; no threshold to compare |
| Non-quantified | `"some scout signals"` | `">= 2 scout signals present"` | Count threshold is machine-checkable in principle |
| Conformant (best) | -- | `">= 2 scout signals AND draft-spec artifact present"` | Names artifact AND threshold; bilateral verifiability |

At least one non-echo gate MUST be quantified: `">= N"`, `"0 P0 findings open"`, or equivalent.

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

    - name: "<breadth-phase-label>"           # SHALL be a phase label (e.g. "discovery"); not a namespace name
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

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; full validated context required ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; 0 critical blockers>"

  # ---- Final Stage: echo -- arc closure; auto: true; no skills ----
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

## V-02 -- Narrative Inertia Framing (single-axis: inertia framing)

**Axis**: Inertia framing -- the BAD example is expanded from a bare YAML block to a realistic
team-conversation narrative that PRODUCES the bad YAML. The narrative opens the prompt body,
establishes what planning-without-Signal looks like in practice, and then shows the YAML that
emerges from that conversation. The identity conclusion ("/program:plan exists to replace this
pattern") applies to both the conversation and the plan it produces. This maximizes C-16
(contrast-grounded identity): the BAD narrative IS the opening identity mechanism, and the
identity claim is the conclusion drawn from observing the narrative.

**Structural elements preserved exactly from R7 V-03**: Same three-layer arc structure with same
Layer 1 header (naming Layer 2 for C-26) and same Layer 3 header (dependency clause for C-27).
Same enumerated echo paragraph (C-25 PASS). Same three pre-template reference tables (arc, gate,
skill catalog). Same YAML template with layer dividers and preserve-required comments. Same Plan
Verification table.

**Hypothesis**: Elaborating the inertia framing enriches C-10 (contrast) and C-16 (contrast-as-
identity-foundation) without disturbing any other criterion. The narrative is the opening, so C-12
(not-executor as opening identity) remains satisfied because the identity claim concludes the
narrative opening block. Expected: 20/20 aspirational, composite 100.00.

---

### Prompt body

A product manager opens a planning sync. The team has agreed to build a new API capability for
{{topic}}. She opens a new YAML file. Someone calls out the skills the team will need to run.
She lists them: scout, spec, review, flow, trace, listen. The next question: what order? The
team talks for a moment. "Doesn't matter much -- we'll do them roughly in this order." She types
a single stage. Someone asks about the gate. "Let's put 'done' for now and update it later." The
meeting ends. The team has a plan.

This plan is PROGRAM-BAD-01:

```yaml
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

`review:design` requires a spec that `draft:spec` has not yet produced -- they are in the same
flat list with no ordering enforced. `flow:lifecycle` simulates a lifecycle for a design that
`review:design` has not yet validated -- simulation results are built on an unreviewed design.
`trace:request` traces a request path through an unreviewed, unvalidated architecture.
`listen:feedback` synthesizes feedback across signals that have not been gathered or validated;
there is nothing coherent to synthesize. `"done"` is unverifiable: the next phase owner has no
artifact to check, no threshold to compare against. The team advances on faith.

What you just read is every ad-hoc plan: a sync that produces a flat list and a gate that
describes completion without specifying evidence.

**`/program:plan` exists to replace this conversation and the plan it produces.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before advancing.
A plan without meaningful gates is a list. A list is what PROGRAM-BAD-01 is.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals **Layer 2** requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Scout skills run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`). These produce the feasibility, requirements, market, and competitor artifacts
that Layer 2 depends on before any design skill can start. Layer 1 requires no prior signals; it
is the program entry point. A `draft:spec` written without Layer 1 feasibility and requirements
signals is speculation -- it encodes what the author believes should be built rather than what has
been verified as needed. This is how PROGRAM-BAD-01 fails: both `scout:requirements` and
`draft:spec` are in the same flat stage; the spec can run before any requirements signal exists.
Layer 1's gate is what PROGRAM-BAD-01's meeting should have produced: a named, checkable condition
that lets the next-phase owner verify that required artifacts exist before design begins.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts:**

Layer 2 has internal ordering constraints arising from artifact dependencies within the layer.
The design sub-stage runs first and produces the `draft-spec` artifact -- the central document
that all subsequent Layer 2 skills require. The validation sub-stage (`review:design`,
`review:users`, `prove:prototype`) cannot run before the spec exists: `review:design` reviews a
specification, and without a specification the review has no object; `prove:prototype` explores
the design described in the spec. The gate between design and validation states this dependency
explicitly, making it checkable. Flow and trace skills run last in Layer 2 because they simulate
and trace a validated design -- `flow:lifecycle` simulates a lifecycle defined in a reviewed spec;
`trace:contract` traces a contract that has been reviewed for correctness. Running flow or trace
before review propagates unvalidated design assumptions into simulation output -- exactly what
PROGRAM-BAD-01 does by placing `flow:lifecycle` and `review:design` in the same flat stage.
Layer 2 hands Layer 3 a complete validated context: reviewed design, proved prototype, simulated
flows and traced paths.

**Layer 3 (Synthesis) -- produces the synthesis artifact set; requires the full validated context:**

Layer 3 runs `listen:*` and `topic:*` last because synthesis skills require the complete evidence
base to produce meaningful output. `listen:adoption` synthesizes adoption signals across the
validated design context that Layers 1 and 2 produced; running it before validation means
synthesizing signals that have not been validated. `listen:feedback` synthesizes feedback across
a signal set that has not yet been gathered. `topic:story` constructs a coherent narrative from
the full evidence arc; running it before all signals are archived produces a narrative over a
partial evidence set. `topic:report` summarizes findings across all layers; a report produced
before Layer 2 is complete will omit validation findings. Layer 3's gate is what
PROGRAM-BAD-01's planning sync skipped entirely: an evidence checkpoint that makes the final
synthesis verifiable -- all prior signals archived, all prior artifacts present, no critical
blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program, and its contract is architecturally distinct
from all prior stages:

(1) **No skills** -- echo's function is arc closure, not evidence production. By the time echo
runs, all evidence production has ended across Layers 1, 2, and 3. Adding skills to echo would
place evidence work in a terminal stage with no subsequent gate to certify it; the result would
be ungated evidence appended after all validation has finished. Echo is not a spillover stage for
skills that did not fit earlier layers.

(2) **`auto: true`** -- echo does not wait for a human reviewer to inspect a gate condition and
advance the plan. Echo has no gate condition. When all prior stages have reached their gates,
echo closes automatically. This is the structural counterpart to PROGRAM-BAD-01's `"done"` gate:
instead of a fictitious completion predicate, echo's auto-closure is architecturally earned --
the arc has already closed at Layer 3's evidence gate before echo runs.

(3) **Arc closure function** -- when echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2), synthesis produced (Layer 3). Echo is the program's completion receipt; the signal
archive is coherent and the topic's investigation is done. This is what the planning meeting that
produced PROGRAM-BAD-01 was trying to achieve -- and the arc is the mechanism that actually
delivers it.

---

**Evidence arc reference:**

| Layer | Namespaces | Arc role | Produces | Requires | Gate type |
|-------|------------|----------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Dependency origin | Feasibility, requirements, market, competitor signals | (none -- program entry) | Quantified: >= N scout signals |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Echo | -- | All prior gates reached | (none -- auto: true) |

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

  # ---- Final Stage: echo -- arc closure; auto: true; no skills ----
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

## V-03 -- Bidirectional Layer Headers (single-axis: layer header cross-references)

**Axis**: Layer header cross-references -- all three layer narration headers name adjacent layers
by number, creating bidirectional dependency pointers. V-03 tests whether richer cross-references
(beyond C-26's minimum of one) cause any criterion interference and whether an alternative
formulation of the Layer 3 header (naming Layer 2 explicitly by number rather than using "full
validated context") passes C-27 more strongly than R7 V-03.

Header changes from R7 V-03:
- Layer 1 (unchanged): "**Layer 1 (Breadth) -- dependency origin; produces the foundational signals **Layer 2** requires:**" -- names Layer 2 (C-26 PASS)
- Layer 2 (NEW): "**Layer 2 (Depth) -- receives **Layer 1** scout artifacts; produces validated context **Layer 3** requires:**" -- names both Layer 1 AND Layer 3
- Layer 3 (NEW): "**Layer 3 (Synthesis) -- requires validated artifacts from **Layer 2**; produces the final synthesis artifact set:**" -- names Layer 2 (C-27: explicit dependency statement naming the source by number)

All other structural elements preserved exactly from R7 V-03.

**Hypothesis**: Bidirectional cross-references satisfy C-26 and C-27 more explicitly than R7 V-03.
C-27 is satisfied by Layer 3's "requires validated artifacts from **Layer 2**" -- naming the source
layer by number is a stronger form of the dependency statement than "requires the full validated
context." No criterion should conflict with richer cross-references. Expected: 20/20 aspirational,
composite 100.00.

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

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals **Layer 2** requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Scout skills run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`). These produce the feasibility, requirements, market, and competitor artifacts
that Layer 2 depends on before any design skill can start. Layer 1 requires no prior signals; it
is the program entry point. A `draft:spec` written without Layer 1 feasibility and requirements
signals is speculation -- it encodes what the author believes should be built rather than what has
been verified as needed. Layer 1's output is Layer 2's required input; the gate between them makes
this dependency checkable: the next phase owner can inspect that named scout artifacts are present
before any design skill starts.

**Layer 2 (Depth) -- receives **Layer 1** scout artifacts; produces validated context **Layer 3** requires:**

Layer 2 has internal ordering constraints arising from artifact dependencies within the layer.
It opens by consuming Layer 1's scout artifacts -- without them, the design sub-stage is
speculative -- and it closes by producing a complete validated context that Layer 3 requires before
any synthesis skill can run. The design sub-stage runs first and produces the `draft-spec` artifact
-- the central document that all subsequent Layer 2 skills require. The validation sub-stage
(`review:design`, `review:users`, `prove:prototype`) cannot run before the spec exists:
`review:design` reviews a specification, and without a specification the review has no object;
`prove:prototype` explores the design described in the spec. The gate between design and validation
states this dependency explicitly, making it checkable. Flow and trace skills run last in Layer 2
because they simulate and trace a validated design -- `flow:lifecycle` simulates a lifecycle
defined in a reviewed spec; `trace:contract` traces a contract that has been reviewed for
correctness. Running flow or trace before review propagates unvalidated design assumptions into
simulation output. Layer 2 hands Layer 3 a complete validated context: reviewed design, proved
prototype, simulated flows and traced paths.

**Layer 3 (Synthesis) -- requires validated artifacts from **Layer 2**; produces the final synthesis artifact set:**

Layer 3 runs `listen:*` and `topic:*` last because synthesis skills require the complete evidence
base that Layer 2 produced -- validated design, proved prototype, simulated flows and traced paths.
`listen:adoption` synthesizes adoption signals across that validated context; running it before
Layer 2 is complete means synthesizing signals that have not been validated. `listen:feedback`
synthesizes feedback across a signal set that has not yet been gathered. `topic:story` constructs
a coherent narrative from the full evidence arc; running it before all signals are archived
produces a narrative over a partial evidence set. `topic:report` summarizes findings across all
layers; a report produced before Layer 2 is complete will omit validation findings. Layer 3's
gate is the final evidence checkpoint: all prior signals archived, all prior artifacts present, no
critical blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program, and its contract is architecturally distinct
from all prior stages:

(1) **No skills** -- Echo carries no skills. By the time echo runs, all evidence production has
ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate, or synthesize.
Adding skills to echo would mean running evidence work in a terminal stage with no subsequent gate
capable of certifying that evidence before the program closes; the work would be ungated. Echo is
not a spillover stage for skills that did not fit earlier layers.

(2) **`auto: true`** -- Echo does not wait for a human reviewer to inspect a gate condition and
advance the plan. Echo has no gate condition. When all prior stages have reached their gates, echo
closes automatically. The `auto: true` declaration is not a convenience flag -- it is an
architectural statement that the program's completion requires no human gate inspection at this
stage, because the arc has already closed at Layer 3's gate.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2, drawing on Layer 1's artifacts), synthesis produced (Layer 3, drawing on Layer 2's
validated context). Echo is the receipt of the completed program; the signal archive is coherent
and the topic's investigation is done.

---

**Evidence arc reference:**

| Layer | Namespaces | Arc role | Produces | Requires | Gate type |
|-------|------------|----------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Dependency origin | Feasibility, requirements, market, competitor signals | (none -- program entry) | Quantified: >= N scout signals |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Echo | -- | All prior gates reached | (none -- auto: true) |

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

  # ---- Layer 2: Depth -- receives Layer 1 artifacts; produces validated context for Layer 3 ----
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

  # ---- Layer 3: Synthesis -- requires validated artifacts from Layer 2; produces synthesis set ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- arc closure; auto: true; no skills ----
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

## V-04 -- Formal Register + Lifecycle Emphasis (combined: phrasing register + lifecycle)

**Axes**: Phrasing register (formal SHALL/MUST from V-01) combined with lifecycle emphasis --
each layer narration paragraph foregrounds the lifecycle zone the layer covers, not just the
artifact dependencies. Layer narrations describe what phase of the feature's existence is
advancing, what lifecycle question is being answered, and what lifecycle-state transitions the
gate enables. Bidirectional cross-references (from V-03) are also included. Gate descriptions
reference lifecycle readiness conditions.

**Header forms (combining V-01 formality + V-03 bidirectionality)**:
- Layer 1: "**Layer 1 (Breadth) -- lifecycle entry gate; produces the foundational signals **Layer 2** requires before design commences:**"
- Layer 2: "**Layer 2 (Depth) -- consumes **Layer 1** signals; produces the validated lifecycle model **Layer 3** requires:**"
- Layer 3: "**Layer 3 (Synthesis) -- requires the full lifecycle-validated context from **Layer 2**; produces the readiness artifact set:**"

**Hypothesis**: Formal register + lifecycle emphasis + bidirectional references all target the
same structural criteria as V-01/V-03 individually. The lifecycle zone framing adds richness
to C-08 (deliberate arc) and C-17 (dependency narration) without disturbing any criterion.
Expected: 20/20 aspirational, composite 100.00.

---

### Prompt body

```yaml
# NON-CONFORMANT: this program places skills that require artifact preconditions in the same stage
# as the skills that produce those artifacts. No lifecycle ordering is enforced.

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

This program is non-conformant. The feature it plans for `{{topic}}` SHALL pass through four
lifecycle zones before it is ready to ship: an unknown zone (feasibility and requirements unknown),
a design zone (design and spec produced), a validation zone (design reviewed and proved), and a
synthesis zone (adoption and readiness assessed). Each zone entry requires artifacts that the
prior zone produced. A flat single-stage plan with a `"done"` gate enforces none of this
progression. `review:design` requires a spec that `draft:spec` has not yet produced. `flow:lifecycle`
simulates a lifecycle that `review:design` has not yet validated. `listen:feedback` synthesizes
signals that have not yet been gathered. `"done"` is an execution state -- it SHALL NOT serve as
a gate because it describes whether the stage has finished running, not whether lifecycle
progression criteria have been met.

**`/program:plan` SHALL replace this pattern.**

It MUST produce a plan, not an executor. Every skill listed in the plan SHALL remain independently
runnable. The program MUST NOT execute skills, advance stages, or carry automation authority. Its
normative product is the gate: a declared lifecycle-readiness condition that MUST be satisfied
before the feature advances to the next zone. A program with vague or execution-state gates is a
flat list with incorrect lifecycle framing.

---

You are running `/program:plan` for topic **{{topic}}**.

**The lifecycle dependency chain -- why stages are ordered:**

**Layer 1 (Breadth) -- lifecycle entry gate; produces the foundational signals **Layer 2** requires before design commences:**

Layer 1 advances the feature from the unknown zone into the design zone. The feature enters Layer 1
in a state of unknown: feasibility is unassessed, requirements are undefined, market context is
absent. Scout skills SHALL run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`) that test early hypotheses before design begins. These MUST produce the
feasibility, requirements, market, and competitor artifacts that constitute the design zone's entry
criteria. Layer 1 requires no prior signals; it is the program's lifecycle entry gate. The gate
between Layer 1 and Layer 2 is the lifecycle threshold between "unknown" and "ready to design":
the next-phase owner MUST be able to confirm that named scout artifacts are present, that a
feasibility signal exists, and that requirements are defined, before any design skill commences.
A `draft:spec` written without Layer 1's artifacts is lifecycle speculation -- it encodes the
author's beliefs rather than verified lifecycle evidence.

**Layer 2 (Depth) -- consumes **Layer 1** signals; produces the validated lifecycle model **Layer 3** requires:**

Layer 2 advances the feature from the design zone through validation and into simulation. It
MUST consume Layer 1's scout artifacts as entry criteria -- the design zone cannot be entered
without them. The design sub-stage SHALL run first: `draft:spec` produces the specification that
defines the feature's design intent and constitutes the artifact that all subsequent Layer 2 skills
MUST reference. The validation sub-stage (`review:design`, `review:users`, `prove:prototype`) SHALL
NOT commence before the spec exists -- `review:design` validates a specification's design decisions,
and without a specification there is nothing to validate; `prove:prototype` explores the user
experience described in the spec. The gate between design and validation enforces the zone entry
condition for validation: `draft-spec` MUST be present. Flow and trace skills SHALL run last in
Layer 2 because they simulate and trace a validated lifecycle model -- `flow:lifecycle` simulates
the feature's end-to-end lifecycle as defined in a reviewed spec; `trace:contract` traces the API
contract after it has been reviewed for correctness. Running flow or trace before review is a
lifecycle-ordering violation: it produces a simulation of an unvalidated model. Layer 2 MUST hand
Layer 3 a complete validated lifecycle model: reviewed design, proved prototype, simulated lifecycle
flows, traced paths.

**Layer 3 (Synthesis) -- requires the full lifecycle-validated context from **Layer 2**; produces the readiness artifact set:**

Layer 3 advances the feature from the validated design zone into the synthesis and readiness zone.
It MUST consume Layer 2's complete validated lifecycle model as entry criteria -- synthesis MUST
NOT commence before validation is complete. `listen:adoption` SHALL synthesize adoption signals
across the validated lifecycle model that Layer 2 produced; running it before Layer 2 is complete
violates the lifecycle entry constraint for synthesis -- the synthesis depends on validated
artifacts that have not yet been produced. `listen:feedback` SHALL synthesize feedback across a
signal set that Layer 1 and Layer 2 produced; running it before those signals exist means
synthesizing an empty set. `topic:story` SHALL construct a coherent narrative from the full
lifecycle evidence arc -- running it before all signals are archived produces a narrative with
lifecycle gaps. `topic:report` SHALL summarize findings across all layers; a report produced before
Layer 2 is complete MUST be considered incomplete because it omits validation findings. Layer 3's
gate is the final lifecycle-readiness checkpoint: all prior signals MUST be archived, all prior
artifacts MUST be present, and there MUST be zero critical blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program and its contract is normatively distinct from all
prior stages:

(1) **Skill-free obligation (NORMATIVE)** -- Echo SHALL carry no skills. By the time echo runs,
the feature's full lifecycle has been advanced: unknown zone completed (Layer 1), design validated
(Layer 2), readiness assessed (Layer 3). There is no lifecycle evidence remaining to produce.
Adding skills to echo would place lifecycle work in a terminal stage with no subsequent gate to
certify it before the program closes. Echo SHALL NOT serve as a spillover stage for skills that
did not fit earlier lifecycle zones.

(2) **`auto: true` semantics (NORMATIVE)** -- Echo SHALL NOT require human gate inspection. Echo
has no gate condition because the lifecycle has already been certified at Layer 3's readiness gate.
When all prior stages have met their evidence conditions, echo MUST close automatically. The
`auto: true` declaration is the normative statement that the program lifecycle is complete.

(3) **Arc closure function (NORMATIVE)** -- When echo closes, the program SHALL signal that the
full lifecycle arc is complete: unknown zone resolved (Layer 1), design validated (Layer 2),
readiness established (Layer 3). The signal archive is coherent, the lifecycle evidence is complete,
and the feature's investigation is done. Echo is the program's lifecycle completion receipt.

---

**Evidence arc reference:**

| Layer | Namespaces | Lifecycle zone | Produces | Requires | Gate type |
|-------|------------|----------------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Unknown -> design entry | Feasibility, requirements, market, competitor signals | (none -- lifecycle entry) | Quantified: >= N scout signals |
| 2a: Design | draft | Design zone | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Validation zone | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation zone (optional) | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Readiness zone | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Lifecycle close | -- | All prior gates reached | (none -- auto: true) |

**Gate conformance reference:**

| Violation class | Non-conformant form | Conformant form | Why it violates |
|----------------|---------------------|-----------------|-----------------|
| Execution state | `"Layer 1 complete"` | `"scout-feasibility artifact present"` | Execution state describes running, not lifecycle readiness |
| Empty / vague | `"done"` | `"draft-spec and scout-requirements present"` | No artifact to check; no lifecycle threshold |
| Non-quantified | `"some scout signals"` | `">= 2 scout signals present"` | Count threshold is machine-checkable in principle |
| Conformant (best) | -- | `">= 2 scout signals AND draft-spec artifact present"` | Names artifact AND threshold; bilateral lifecycle verification |

At least one non-echo gate MUST contain a numeric threshold: `">= N"`, `"0 P0 findings open"`, or
equivalent.

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
  strategy: "<one-sentence lifecycle goal: what zone does this program advance the feature through?>"

  stages:

  # ---- Layer 1: Breadth -- lifecycle entry; scout signals produced here; Layer 2 requires them ----

    - name: "<breadth-phase-label>"           # lifecycle zone label (e.g. "discovery")
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts present; lifecycle entry threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- consumes Layer 1 artifacts; produces validated lifecycle model for Layer 3 ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
      gate: "<draft-spec artifact present; design zone entered>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open; validation zone complete>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- requires validated lifecycle model from Layer 2; produces readiness set ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "readiness"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; 0 critical blockers; readiness zone complete>"

  # ---- Final Stage: echo -- lifecycle arc closure; auto: true; no skills ----
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
| Layer 1 comment | `# ---- Layer 1: Breadth ----` with lifecycle annotation present in YAML | [ ] |
| Layer 2 comment | `# ---- Layer 2: Depth ----` with dependency annotation present in YAML | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` with Layer 2 reference present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present in YAML | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved in YAML | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved in YAML | [ ] |

---

## V-05 -- All R8 Axes: Golden Synthesis (combined)

**Axes**: Narrative inertia framing (V-02) + bidirectional layer headers (V-03) + formal gate
language (V-01) + lifecycle zone emphasis (V-04) + richest tables (all three tables maximally
populated). V-05 tests whether all R8 axes can coexist without criterion interference and whether
the combination produces the most robustly-scored variation in this round.

**Header forms** (combining all axes):
- Layer 1: "**Layer 1 (Breadth) -- lifecycle entry; dependency origin; produces the foundational signals **Layer 2** requires before design commences:**"
- Layer 2: "**Layer 2 (Depth) -- consumes **Layer 1** artifacts; produces the validated lifecycle context **Layer 3** requires:**"
- Layer 3: "**Layer 3 (Synthesis) -- requires the full validated context from **Layer 2**; produces the readiness artifact set:**"

C-26: Layer 1 names Layer 2; Layer 2 names both Layer 1 AND Layer 3; Layer 3 names Layer 2.
Multiple cross-references; minimum requirement satisfied by Layer 1 alone.
C-27: Layer 3 states "requires the full validated context from **Layer 2**" -- both a dependency
statement (C-27) and a named-layer reference (additional C-26 coverage).

**Hypothesis**: Maximum axis combination. Narrative BAD scenario enriches C-16 without disturbing
any structural criterion. Bidirectional headers satisfy C-26/C-27 in the strongest possible form.
Formal language is register-neutral. Lifecycle framing enriches C-08/C-17. All tables richest
form. Expected: 20/20 aspirational, composite 100.00. The strongest possible prompt body under
v24.

---

### Prompt body

The team has just kicked off planning for `{{topic}}`. The PM opens a YAML file. "What skills do
we need?" The team calls them out, one by one. She types them. "What order?" A beat. "Roughly this
order is fine, we'll figure it out." "And the gate?" Silence. "Put 'done' for now." The file is
saved. The team has a program plan.

Here is the plan they just produced:

```yaml
# What every ad-hoc planning sync produces:

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

This plan is non-conformant on four counts. (1) `review:design` requires a `draft-spec` artifact
that `draft:spec` has not yet produced -- they are co-listed in a flat stage with no ordering
constraint enforced. (2) `flow:lifecycle` SHALL NOT simulate a lifecycle for a design that
`review:design` has not yet validated -- the simulation propagates unvalidated design assumptions
into lifecycle output. (3) `trace:request` SHALL NOT trace a request path through an unreviewed
architecture for the same reason. (4) `"done"` is an execution-state predicate -- it describes
whether the stage finished running, not whether the required evidence exists. The next-phase owner
has no artifact to check, no lifecycle threshold to compare against, and no way to know whether the
investigation was actually complete when the gate was called. The team has a list, not a plan.

**`/program:plan` SHALL replace both the meeting and the plan it produces.**

It MUST produce a plan, not an executor. Every skill listed in the plan SHALL remain independently
runnable -- the program MUST NOT execute skills, advance stages, or carry automation authority. Its
normative product is the gate: a declared, evidence-specific, lifecycle-checkable condition that
MUST be satisfied before the next stage commences. A program without evidence gates is not a plan.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact and lifecycle dependency chain -- why stages SHALL be ordered:**

**Layer 1 (Breadth) -- lifecycle entry; dependency origin; produces the foundational signals **Layer 2** requires before design commences:**

Layer 1 advances the feature from the unknown zone into the design zone. It SHALL produce the
foundational signal set that every downstream stage requires as a lifecycle prerequisite -- the
artifacts that constitute the design zone's entry criteria. Scout skills SHALL run here:
`scout:feasibility`, `scout:requirements`, `scout:market`, `scout:competitors`, along with early
prove skills (`prove:websearch`, `prove:intelligence`, `prove:hypothesis`) that test early
hypotheses before any design work commences. These MUST produce the feasibility, requirements,
market, and competitor artifacts that Layer 2 depends on. Layer 1 requires no prior signals; it
is the program's lifecycle entry gate. A `draft:spec` written without Layer 1's feasibility and
requirements signals is lifecycle speculation -- it encodes the author's beliefs rather than
verified evidence of what should be built. Layer 1's gate is the lifecycle threshold between
"unknown" and "ready to design": the next-phase owner MUST be able to confirm that named scout
artifacts are present before any Layer 2 design skill commences.

**Layer 2 (Depth) -- consumes **Layer 1** artifacts; produces the validated lifecycle context **Layer 3** requires:**

Layer 2 advances the feature through the design, validation, and simulation zones. It MUST consume
Layer 1's scout artifacts as zone-entry criteria -- the design zone SHALL NOT be entered without
them. The design sub-stage SHALL run first: `draft:spec` produces the specification that defines
the feature's design intent and constitutes the entry artifact for every subsequent Layer 2 skill.
The validation sub-stage (`review:design`, `review:users`, `prove:prototype`) SHALL NOT commence
before the spec exists -- `review:design` validates a specification and without a specification the
review has no object; `prove:prototype` SHALL explore the design described in the spec. The gate
between design and validation enforces the validation zone entry condition: `draft-spec` MUST be
present, and the gate MUST state this condition explicitly. Flow and trace skills SHALL run last
in Layer 2: `flow:lifecycle` simulates the feature's lifecycle as defined in a reviewed spec;
`trace:contract` traces the API contract after it has been reviewed for correctness. Running flow
or trace before review is a lifecycle-ordering violation that propagates unvalidated design
assumptions. Layer 2 MUST hand Layer 3 a complete validated lifecycle context: reviewed design,
proved prototype, simulated flows, and traced paths -- the artifact set that Layer 3 requires as
its zone-entry criteria.

**Layer 3 (Synthesis) -- requires the full validated context from **Layer 2**; produces the readiness artifact set:**

Layer 3 advances the feature from the validated design zone into the synthesis and readiness zone.
It MUST consume Layer 2's complete validated lifecycle context as zone-entry criteria -- synthesis
SHALL NOT commence before Layer 2's validation is complete. `listen:adoption` SHALL synthesize
adoption signals across the validated context that Layer 2 produced; running it before Layer 2 is
complete violates the synthesis zone's entry constraint. `listen:feedback` SHALL NOT synthesize
feedback across signals that Layer 1 and Layer 2 have not yet produced. `topic:story` SHALL
construct a coherent narrative from the full lifecycle evidence arc; running it before all signals
are archived produces a narrative over a lifecycle gap. `topic:report` SHALL summarize findings
across all layers; a report produced before Layer 2 is complete MUST be considered non-conformant
because it omits validation findings. Layer 3's gate is the final lifecycle-readiness checkpoint:
all prior signals MUST be archived, all prior artifacts MUST be present, and there MUST be zero
critical blockers remaining before the feature can be considered investigation-complete.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three normative
obligations, each of which follows from the lifecycle arc that precedes it:

(1) **Skill-free obligation (NORMATIVE)** -- Echo SHALL carry no skills. By the time echo runs,
the feature's full lifecycle investigation has been completed: unknown zone resolved (Layer 1),
design validated (Layer 2), readiness established (Layer 3). There is no lifecycle evidence
remaining to produce. Adding skills to echo would place lifecycle work in a terminal stage with
no subsequent gate capable of certifying that evidence before the program closes -- exactly the
structural failure that PROGRAM-BAD-01 commits with its flat single stage. Echo SHALL NOT serve
as a spillover stage for skills that did not fit earlier lifecycle zones.

(2) **`auto: true` semantics (NORMATIVE)** -- Echo SHALL NOT require human gate inspection. Echo
has no gate condition because the lifecycle has already been certified at Layer 3's readiness gate.
When all prior stages have met their declared evidence conditions, echo MUST close automatically.
The `auto: true` declaration is the normative statement that the program lifecycle is complete;
it is not a convenience flag. This is the structural answer to `"done"`: instead of an
unverifiable execution predicate, the arc's completion is earned by Layer 3's evidence gate and
confirmed by echo's automatic closure.

(3) **Arc closure function (NORMATIVE)** -- When echo closes, the program SHALL signal that the
topic's full lifecycle investigation is complete: unknown zone resolved (Layer 1), design
validated (Layer 2), readiness established (Layer 3). The signal archive is coherent, the
lifecycle evidence is complete, and the feature investigation is formally done. Echo is the
program's lifecycle completion receipt -- the structural outcome that the planning sync that
produced PROGRAM-BAD-01 was trying to achieve.

---

**Evidence arc reference:**

| Layer | Namespaces | Lifecycle zone | Arc role | Produces | Requires | Gate type |
|-------|------------|----------------|----------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Unknown -> design entry | Dependency origin | Feasibility, requirements, market, competitor signals | (none -- lifecycle entry) | Quantified: >= N scout signals |
| 2a: Design | draft | Design zone | Architecture | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Validation zone | Review + prove | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation zone (optional) | Simulation | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Readiness zone | Closing | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Lifecycle close | Echo | -- | All prior gates reached | (none -- auto: true) |

**Gate conformance reference:**

| Violation class | Non-conformant form | Conformant form | Why it violates |
|----------------|---------------------|-----------------|-----------------|
| Execution state | `"Layer 1 complete"` | `"scout-feasibility artifact present"` | Execution state describes running state, not lifecycle readiness |
| Empty / vague | `"done"` | `"draft-spec and scout-requirements artifacts present"` | No artifact to check; no lifecycle threshold to compare against |
| Non-quantified | `"some scout signals"` | `">= 2 scout signals present"` | Count threshold is machine-checkable; "some" is not |
| Conformant (best) | -- | `">= 2 scout signals AND draft-spec artifact present"` | Names artifact AND numeric threshold; bilaterally verifiable |

At least one non-echo gate MUST contain a numeric threshold: `">= N"`, `"0 P0 findings open"`, or
equivalent.

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
  strategy: "<one-sentence lifecycle goal: what lifecycle question does this program answer for {{topic}}?>"

  stages:

  # ---- Layer 1: Breadth -- lifecycle entry; scout signals produced here; Layer 2 requires them ----

    - name: "<breadth-phase-label>"           # lifecycle zone label (e.g. "discovery", "unknown-resolution")
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic and lifecycle gap warrant
      gate: "<named scout artifacts present; lifecycle entry threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- consumes Layer 1 artifacts; produces validated lifecycle context for Layer 3 ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
      gate: "<draft-spec artifact present; design zone entered>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open; validation zone complete>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- requires validated context from Layer 2; produces readiness artifact set ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "readiness"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; 0 critical blockers; readiness complete>"

  # ---- Final Stage: echo -- lifecycle arc closure; auto: true; no skills ----
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
| Layer 1 comment | `# ---- Layer 1: Breadth ----` with lifecycle annotation present in YAML | [ ] |
| Layer 2 comment | `# ---- Layer 2: Depth ----` with Layer 1/Layer 3 dependency annotation present in YAML | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` with Layer 2 reference annotation present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present in YAML | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved in YAML | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved in YAML | [ ] |

---

## Predicted Scores at v24

| Variation | C-24 | C-25 | C-26 | C-27 | Predicted asp/20 | Predicted composite |
|-----------|------|------|------|------|-----------------|---------------------|
| V-01 (formal register) | PASS -- same headers as R7 V-03 V-01 | PASS -- formal numbered obligations (1)/(2)/(3) | PASS -- Layer 1 header names Layer 2 | PASS -- Layer 3 header: "requires the full validated context" | 20/20 | 100.00 |
| V-02 (narrative inertia) | PASS -- same headers as R7 V-03 | PASS -- same (1)/(2)/(3) echo enumeration | PASS -- same Layer 1 header | PASS -- same Layer 3 header | 20/20 | 100.00 |
| V-03 (bidirectional headers) | PASS -- all three headers have role descriptors | PASS -- same (1)/(2)/(3) echo enumeration | PASS -- Layer 1 names Layer 2; Layer 2 names Layer 1 AND Layer 3; Layer 3 names Layer 2 | PASS -- Layer 3: "requires validated artifacts from **Layer 2**" | 20/20 | 100.00 |
| V-04 (formal + lifecycle) | PASS -- lifecycle-zone headers with role descriptors | PASS -- formal numbered obligations (1)/(2)/(3) | PASS -- Layer 1 names Layer 2; Layer 2 names Layer 1 AND Layer 3 | PASS -- Layer 3: "requires the full validated lifecycle context from **Layer 2**" | 20/20 | 100.00 |
| V-05 (golden synthesis) | PASS -- all three headers with role descriptors + lifecycle labels | PASS -- formal numbered obligations with lifecycle arc closure context | PASS -- multiple cross-references in all three headers | PASS -- Layer 3: "requires the full validated context from **Layer 2**" | 20/20 | 100.00 |

**Key C-26/C-27 risks to verify at scoring time**:
- V-01: C-26 depends on Layer 1 header preserving "**Layer 2**" verbatim -- formal register must not paraphrase the layer reference away
- V-03/V-04/V-05: Layer 2 header names adjacent layers -- scorer should confirm these also pass C-26 (though Layer 1 alone is sufficient)
- V-04/V-05: lifecycle-zone framing in Layer 3 header -- "full validated lifecycle context from **Layer 2**" should satisfy C-27 (dependency statement present + Layer 2 named by identity)
