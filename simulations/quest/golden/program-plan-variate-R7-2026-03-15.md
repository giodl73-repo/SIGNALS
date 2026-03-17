---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 7
rubric: v23
---

# program-plan -- R7 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v23 (C-01 through C-25, 25 criteria, golden = all essential pass
AND composite >= 80).

---

## R6 Retrospective Under v23 Rubric

v23 adds four aspirational criteria:

- **C-22** (BAD/GOOD gate contrast as reference table): The C-10 gate contrast must be a table
  with BAD and GOOD (or equivalent) as separate column headers. A single "Passes? YES/NO" column
  encoding polarity is borderline; literal "BAD example | GOOD example" columns are unambiguous.
  Requires C-10 PASS.
- **C-23** (Tabular skill catalog): The skill catalog must be a structured table with namespace
  and skills columns. A bullet list does not pass regardless of completeness.
- **C-24** (Layer paragraph headers): Each per-layer arc narration paragraph (C-20) must open
  with a bold/formatted header naming both the layer identity AND its structural arc role (e.g.,
  "**Layer 2 (Depth) -- artifact scope and handoff contract:**"). A header naming only the layer
  without a role descriptor does not pass. Requires C-20 PASS.
- **C-25** (Echo paragraph enumerated): The echo prose paragraph (C-21) must organize its points
  as explicitly numbered sub-items -- minimum three -- covering: skill-free contract rationale,
  `auto: true` semantics, and arc closure function. Flowing prose without enumeration does not
  pass. Requires C-21 PASS.

Retroactive scoring of R6 variations under v23:

| Variation | C-22 | C-23 | C-24 | C-25 | v23 aspirational | v23 composite |
|-----------|------|------|------|------|-----------------|---------------|
| V-01 (C-21 probe) | FAIL -- no contrast (C-10 FAIL) | FAIL -- bullet list | FAIL -- "**Layer N: Name**" no role label | FAIL -- flowing prose | 12/18 | 96.67 |
| V-02 (Formal register) | FAIL -- no contrast (C-10 FAIL) | PASS -- tabular | PASS -- "**Layer N (Name) -- artifact scope...:**" | PASS -- three numbered sub-items | 15/18 | 98.33 |
| V-03 (Contrast-first + C-21) | PASS -- Passes?/YES/NO table (scorer confirmed) | FAIL -- bullet list | FAIL -- "**Layer N: Name**" no role label | FAIL -- flowing prose | 15/18 | 98.33 |
| V-04 (C-16 + C-20 + C-21) | PASS -- Passes?/YES/NO table | PASS -- tabular | FAIL -- "**Layer N: Name**" no role label | FAIL -- flowing prose | 16/18 | ~98.9 |
| V-05 (Golden synthesis) | PASS -- explicit "BAD example \| GOOD example" columns | PASS -- tabular | FAIL -- "**Layer N: Name**" no role label | FAIL -- flowing prose | 16/18 | ~98.9 |

**R6 C-24 gap**: All R6 variations fail C-24. Layer narration openers are consistently
"**Layer N: Name**" (e.g., "**Layer 2: Depth**") -- this identifies the layer by name but states
no arc role. C-24 requires both layer identity AND a role descriptor. Source signal for the
required format: R6 V-02, which passes C-24 with "**Layer 1 (Breadth) -- artifact scope and
handoff contract:**", "**Layer 2 (Depth) -- artifact scope and handoff contract:**", "**Layer 3
(Synthesis) -- artifact scope and handoff contract:**".

**R6 C-25 gap**: V-01/V-03/V-04/V-05 all have flowing prose echo paragraphs. Only R6 V-02 uses
numbered sub-items. Source signal: "(1) **No skills** -- echo's function is arc closure... (2)
**`auto: true`** -- echo does not wait... (3) **Arc closure function** -- when echo closes..."

**R6 C-22 note**: V-03/V-04 use a "Passes? YES/NO" column that the R6 scorer accepted as passing
C-22. R6 V-05 already has explicit "BAD example | GOOD example" column headers, making C-22
unambiguous. For R7 single-axis variations, R6 V-05 is used as the base (inheriting its strong
C-22 and C-23). V-04 base used only for the portability test.

**R7 target**: R6 V-04/V-05 reach 16/18, failing only C-24 and C-25. The primary goal is adding
role-labeled layer headers (C-24) and an enumerated echo paragraph (C-25) to the strongest R6
bases. Source patterns for both criteria are in R6 V-02.

---

## Variation Axes

| Axis | Label | Base | What it tests |
|------|-------|------|---------------|
| Layer header role labels | C-24 probe | R6 V-05 | Does adding "**Layer N (Name) -- role:**" format pass C-24 in isolation? C-25 left unchanged (echo prose). Expected: 17/18. |
| Enumerated echo paragraph | C-25 probe | R6 V-05 | Does replacing flowing echo prose with (1)/(2)/(3) pass C-25 in isolation? C-24 left unchanged (headers without role). Expected: 17/18. |
| C-24 + C-25 combined | Both on V-05 base | R6 V-05 | Do role headers + enumerated echo pass simultaneously? Target: 18/18. |
| C-24 + C-25 portability | Both on V-04 base | R6 V-04 | Same upgrades on R6 V-04 (different prose, Passes?/YES/NO gate table). Tests if C-22 is sensitive to column structure. |
| Golden synthesis | Richest form of all 18 | R6 V-05 | Richest per-layer prose from R6 V-02 merged with V-05 contrast structure; most explicit role headers; richest enumerated echo. Belt-and-suspenders everywhere. |

Single-axis: V-01 (C-24), V-02 (C-25). Combined: V-03 (both on V-05 base), V-04 (both on V-04
base). Golden: V-05 (all 18, richest prose throughout).

---

## V-01 -- Role-Labeled Layer Headers (single-axis: C-24)

**Axis**: Layer paragraph headers -- single-axis addition to R6 V-05. The three layer narration
paragraph openers are upgraded from "**Layer N: Name**" to "**Layer N (Name) -- [role]:**"
format with an explicit arc role descriptor. All other structural choices preserved exactly from
R6 V-05: same opening BAD YAML, same identity conclusion paragraph, same layer narration prose
bodies (only headers changed), same flowing prose echo paragraph, same explicit BAD|GOOD gate
table, same tabular skill catalog, same YAML template, same Plan Verification table.

**Hypothesis**: Adding role descriptors to layer headers passes C-24 without disturbing any
existing pass. C-25 still fails (echo paragraph is unchanged flowing prose). Expected: 17/18
aspirational. Confirms C-24 is independently addressable as a header-only change.

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

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals Layer 2 requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as
precondition. Scout skills run here -- `scout:feasibility`, `scout:requirements`,
`scout:market`, `scout:competitors` -- along with early prove skills (`prove:websearch`,
`prove:intelligence`, `prove:hypothesis`). These produce the feasibility, requirements, market,
and competitor artifacts that Layer 2 depends on before any design skill can start. Layer 1
requires no prior signals; it is the program entry point. A `draft:spec` written without Layer 1
feasibility and requirements signals is speculation -- it encodes what the author believes should
be built rather than what has been verified as needed. Layer 1's output is Layer 2's required
input; the gate between them makes this dependency checkable: the next phase owner can inspect
that named scout artifacts are present before any design skill starts.

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
before review propagates unvalidated design assumptions into simulation output. Layer 2 hands
Layer 3 a complete validated context: reviewed design, proved prototype, simulated flows and
traced paths.

**Layer 3 (Synthesis) -- produces the synthesis artifact set; requires the full validated context:**

Layer 3 runs `listen:*` and `topic:*` last because synthesis skills require the complete evidence
base to produce meaningful output. `listen:adoption` synthesizes adoption signals across the
validated design context that Layers 1 and 2 produced; running it before validation means
synthesizing signals that have not been validated. `listen:feedback` synthesizes feedback across
a signal set that has not yet been gathered. `topic:story` constructs a coherent narrative from
the full evidence arc; running it before all signals are archived produces a narrative over a
partial evidence set. `topic:report` summarizes findings across all layers; a report produced
before Layer 2 is complete will omit validation findings. Layer 3's gate is the final evidence
checkpoint: all prior signals archived, all prior artifacts present, no critical blockers
remaining.

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

## V-02 -- Enumerated Echo Paragraph (single-axis: C-25)

**Axis**: Echo paragraph enumeration -- single-axis addition to R6 V-05. The flowing prose echo
paragraph is replaced with an explicitly numbered (1)/(2)/(3) structure, covering the three
required topics: skill-free contract rationale, `auto: true` semantics, and arc closure function.
All other structural choices preserved exactly from R6 V-05: same opening BAD YAML, same identity
conclusion, same three layer narration paragraphs with "**Layer N: Name**" headers (unchanged --
C-24 deliberately left failing to isolate C-25), same gate table, same skill catalog, same
YAML template, same Plan Verification table.

**Hypothesis**: Replacing prose echo with numbered sub-items passes C-25 in isolation without
disturbing any existing pass. C-24 still fails (layer headers remain "**Layer N: Name**" with no
role label). Expected: 17/18 aspirational. Confirms C-25 is independently addressable as an
echo-paragraph-only change.

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

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate,
or synthesize. Adding skills to echo would mean running evidence work in a terminal stage with
no subsequent gate capable of certifying that evidence before the program closes; the result
would be ungated evidence appended after all validation has finished. Echo is not a spillover
stage for skills that did not fit earlier layers.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. The `auto: true` declaration is not a convenience flag
-- it is an architectural statement that the program's completion requires no human gate
inspection at this stage, because the arc has already closed at Layer 3's gate.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2), synthesis produced (Layer 3). Echo is the receipt of the completed program; the
signal archive is coherent and the topic's investigation is done.

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

## V-03 -- C-24 + C-25 Combined on V-05 Base (primary target: 18/18)

**Axes**: Both C-24 and C-25 applied simultaneously to R6 V-05. Layer narration paragraph
headers upgraded to "**Layer N (Name) -- [role descriptor]:**" (from V-01). Echo paragraph
replaced with (1)/(2)/(3) enumerated structure (from V-02). All other structural choices
preserved from R6 V-05: same opening BAD YAML, same identity conclusion, same layer narration
prose bodies, same explicit BAD|GOOD gate table, same tabular skill catalog, same YAML template,
same Plan Verification table.

**Hypothesis**: Role-labeled headers (C-24) and enumerated echo (C-25) pass simultaneously
without tension. Neither change disturbs existing passing criteria: C-16 (contrast still opens
cold), C-20 (three dedicated layer paragraphs still present), C-21 (echo still a dedicated
paragraph, now also enumerated), C-22 (explicit BAD|GOOD gate table preserved). Expected: 18/18
aspirational = 100/100 composite.

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

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals Layer 2 requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as
precondition. Scout skills run here -- `scout:feasibility`, `scout:requirements`,
`scout:market`, `scout:competitors` -- along with early prove skills (`prove:websearch`,
`prove:intelligence`, `prove:hypothesis`). These produce the feasibility, requirements, market,
and competitor artifacts that Layer 2 depends on before any design skill can start. Layer 1
requires no prior signals; it is the program entry point. A `draft:spec` written without Layer 1
feasibility and requirements signals is speculation -- it encodes what the author believes should
be built rather than what has been verified as needed. Layer 1's output is Layer 2's required
input; the gate between them makes this dependency checkable: the next phase owner can inspect
that named scout artifacts are present before any design skill starts.

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
before review propagates unvalidated design assumptions into simulation output. Layer 2 hands
Layer 3 a complete validated context: reviewed design, proved prototype, simulated flows and
traced paths.

**Layer 3 (Synthesis) -- produces the synthesis artifact set; requires the full validated context:**

Layer 3 runs `listen:*` and `topic:*` last because synthesis skills require the complete evidence
base to produce meaningful output. `listen:adoption` synthesizes adoption signals across the
validated design context that Layers 1 and 2 produced; running it before validation means
synthesizing signals that have not been validated. `listen:feedback` synthesizes feedback across
a signal set that has not yet been gathered. `topic:story` constructs a coherent narrative from
the full evidence arc; running it before all signals are archived produces a narrative over a
partial evidence set. `topic:report` summarizes findings across all layers; a report produced
before Layer 2 is complete will omit validation findings. Layer 3's gate is the final evidence
checkpoint: all prior signals archived, all prior artifacts present, no critical blockers
remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate,
or synthesize. Adding skills to echo would mean running evidence work in a terminal stage with
no subsequent gate capable of certifying that evidence before the program closes; the result
would be ungated evidence appended after all validation has finished. Echo is not a spillover
stage for skills that did not fit earlier layers.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. The `auto: true` declaration is not a convenience flag
-- it is an architectural statement that the program's completion requires no human gate
inspection at this stage, because the arc has already closed at Layer 3's gate.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2), synthesis produced (Layer 3). Echo is the receipt of the completed program; the
signal archive is coherent and the topic's investigation is done.

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

## V-04 -- C-24 + C-25 on Alternate Base (portability: R6 V-04)

**Axes**: Same C-24 and C-25 upgrades as V-03, applied to R6 V-04's structural base instead of
R6 V-05. R6 V-04 differs from R6 V-05 in: (a) different BAD YAML opening (flat "investigation"
stage vs. "all-work"), (b) slightly different Layer 2 and Layer 3 prose, (c) gate table uses
"Passes? YES/NO" column rather than explicit "BAD example | GOOD example" columns. Tests whether
the C-24/C-25 upgrades produce the same 18/18 result on a slightly different base, and whether
C-22 is sensitive to the column structure difference.

**Hypothesis**: C-24/C-25 upgrades port cleanly. C-22 still passes (R6 scorer confirmed V-04's
"Passes? YES/NO" column satisfies C-22). Expected: 18/18. If C-22 proves sensitive to column
structure, this variation exposes it: V-04 gets 17/18 while V-03 gets 18/18.

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

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals Layer 2 requires:**

Layer 1 produces the foundational signal set that Layer 2 requires before it can design
anything. Scout skills run here: `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors`. A `draft:spec` written without feasibility and requirements signals is
speculation, not engineering. Layer 1's output is Layer 2's required input; the gate between them
makes this dependency checkable by the next phase owner before any design skill starts.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts:**

Layer 2 has sub-stages ordered by what each produces. The design sub-stage produces the
`draft-spec` artifact; the validation sub-stage (`review:design`, `prove:prototype`) requires
this artifact before any review skill can run -- `review:design` reviews a specification, and
without a specification there is nothing to review. The gate between design and validation states
this dependency explicitly: the next phase owner checks that `draft-spec` is present before
starting any review. Flow and trace skills require review artifacts before running -- tracing a
contract that has not been reviewed for correctness builds simulation on an unvalidated foundation;
these run last in Layer 2. Layer 2 hands Layer 3 a complete validated context.

**Layer 3 (Synthesis) -- produces the synthesis artifact set; runs after all prior validation:**

Layer 3 runs `listen:*` and `topic:*` last because they synthesize across all prior signals.
`listen:adoption` requires the validated context Layer 2 produced; `topic:story` requires the
full evidence arc to tell a coherent narrative. Running synthesis before validation produces a
story built on unvalidated signals. Layer 3's gate is the final evidence checkpoint: all prior
signals archived, no critical blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. All evidence production ends at Layer 3;
echo's function is arc closure, not evidence gathering. Adding skills to echo would mean running
evidence work in a terminal stage with no subsequent gate capable of verifying that evidence
before the program closes. Echo is not a spillover stage for skills that did not fit elsewhere.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. There is no gate condition for echo to satisfy. When all prior
stages have reached their gates, echo closes automatically. `auto: true` declares that the
program's completion is automatic upon all prior stages reaching their gates.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
evidence arc is complete: breadth signals gathered (Layer 1), design validated (Layer 2),
synthesis produced (Layer 3). Echo is the receipt of the completed program.

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

## V-05 -- Golden Synthesis (all 18 criteria; richest prose)

**Axes**: All 18 aspirational criteria simultaneously. Base: R6 V-05 (contrast-first, explicit
BAD|GOOD gate table, tabular skill catalog). Upgrades: (1) role-labeled layer headers in richest
form -- each header names layer number, parenthetical name, and a distinct role phrase capturing
that layer's specific arc function; (2) enumerated echo -- richest three sub-items, each with a
named bold tag and a full explanatory sentence; (3) layer narration prose upgraded with the most
explicit per-layer artifact scope language (formal "handoff contract" language from R6 V-02
merged with V-05's fuller examples). Belt-and-suspenders on every criterion site.

**Hypothesis**: All 18 aspirational criteria pass. Richest prose choices maximize confidence on
borderline criteria (C-22 unambiguous via explicit columns; C-24 role labels unambiguous via
distinct role phrase per layer; C-25 three individually citable sub-items). Expected: 18/18
aspirational = 100/100 composite.

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

**Layer 1 (Breadth) -- dependency origin; all downstream stages require its signals as precondition:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Artifact classes produced in Layer 1: feasibility signals, requirements signals, market signals,
competitor signals, compliance signals. Skills that produce these artifacts belong to the `scout`
namespace; early `prove` skills (`prove:websearch`, `prove:intelligence`, `prove:hypothesis`)
may also run here. Layer 1 requires no prior signals -- it is the program entry point. Layer 1's
handoff contract with Layer 2: a `draft:spec` skill may not start until Layer 1 has produced the
feasibility and requirements artifacts that the spec will encode. A spec authored without these
signals encodes assumptions, not evidence.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts between design, validation, and simulation:**

Layer 2 produces the design, validation, and simulation artifact set. It has internal dependency
constraints. Sub-stage ordering within Layer 2: (1) design sub-stage -- `draft:spec` or
`draft:proposal` runs first, producing the `draft-spec` artifact; (2) validation sub-stage --
`review:design`, `review:users`, `prove:prototype` run after, each requiring the `draft-spec`
artifact as input (`review:design` reviews a specification; without a specification the review
has no object; `prove:prototype` explores the design the spec describes); (3) simulation
sub-stage -- `flow:*` and `trace:*` skills run last, each requiring review artifacts as
precondition (tracing a contract that has not been reviewed for correctness propagates unvalidated
design decisions into simulation output). Layer 2's handoff contract with Layer 3: synthesis
skills may not start until the validated-design context -- reviewed spec, proved prototype,
simulated flows and traced paths -- is present.

**Layer 3 (Synthesis) -- arc closure; requires the full validated context from Layers 1 and 2:**

Layer 3 produces the synthesis artifact set: adoption signals, feedback signals, topic artifacts
(story, report, status). Skills in this layer (`listen:adoption`, `listen:feedback`,
`topic:story`, `topic:report`) require the complete validated-design context from Layers 1 and 2
as their input. Running `listen:adoption` before validation synthesizes signals that have not
been validated; the synthesis output degrades accordingly. Running `topic:story` before all
signals are archived produces a narrative over a partial evidence set. Layer 3 has no downstream
handoff contract -- it is the final evidence-producing layer. Its gate marks the completion of
the full evidence arc: all prior signals archived, all prior artifacts present, no critical
blockers remaining.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements, each independently verifiable:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate,
or synthesize. Adding skills to echo would mean running evidence work in a terminal stage with
no subsequent gate capable of certifying that evidence before the program closes; the result
would be ungated evidence appended after all validation has finished. Echo is not a spillover
stage for skills that did not fit earlier layers. Its emptiness is intentional and
architecturally required.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. The `auto: true` declaration is not a convenience flag
-- it is an architectural statement that the program's completion requires no human gate
inspection at this stage. The arc closed at Layer 3's gate; echo merely records that closure.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2), synthesis produced (Layer 3). Echo is the receipt of the completed program; the
signal archive is coherent, all artifacts are present, and the topic's investigation is done.
The program has no further work to do.

---

**Evidence arc reference:**

| Layer | Namespaces | Arc role | Produces | Requires | Gate type |
|-------|------------|----------|----------|----------|-----------|
| 1: Breadth | scout, prove (early) | Dependency origin | Feasibility, requirements, market, competitor signals | (none) | Quantified: >= N scout signals |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 signals | Artifact-ref: draft-spec present |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (2a) | Evidence: 0 P0 findings open |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (2b) | Artifact-ref: flow/trace artifacts present |
| 3: Synthesis | listen, topic | Arc closure | Listen/topic artifacts | All prior layers | Evidence: all prior signals archived |
| (auto) | -- | Receipt | -- | All prior gates reached | (none -- auto:true) |

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

## Predicted Scores Under v23

| Variation | Axis | C-22 | C-23 | C-24 | C-25 | Other gaps | Aspirational | Score |
|-----------|------|------|------|------|------|------------|-------------|-------|
| V-01 | C-24 probe on V-05 base | PASS (inherited) | PASS (inherited) | PASS (role headers added) | FAIL (echo prose unchanged) | none | 17/18 | ~99.7/100 |
| V-02 | C-25 probe on V-05 base | PASS (inherited) | PASS (inherited) | FAIL (headers unchanged) | PASS (echo enumerated) | none | 17/18 | ~99.7/100 |
| V-03 | C-24+C-25 on V-05 base | PASS (inherited) | PASS (inherited) | PASS | PASS | none | 18/18 | 100/100 |
| V-04 | C-24+C-25 on V-04 base | PASS (YES/NO -- borderline) | PASS (inherited) | PASS | PASS | none | 17-18/18 | ~99.7-100/100 |
| V-05 | Golden synthesis | PASS (explicit BAD\|GOOD) | PASS (inherited) | PASS (richest headers) | PASS (richest echo) | none | 18/18 | 100/100 |
