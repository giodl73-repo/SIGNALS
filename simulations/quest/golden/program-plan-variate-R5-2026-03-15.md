---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 5
rubric: v21
---

# program-plan -- R5 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v21 (C-01 through C-19, 19 criteria, golden = all essential pass
AND composite >= 80).

---

## R4 Retrospective Under v21 Rubric

v21 adds two aspirational criteria to the v20 set:

- **C-18** (YAML-embedded dependency map): layer divider comments inside the YAML template body
  include inline artifact-flow sub-labels annotating what each layer produces and what the next
  requires. Requires C-14 PASS (layer labels must exist first). Prose narration outside the
  template (C-17) and layer labels alone (C-14) do not pass C-18.
- **C-19** (pre-template reference tables): at least two distinct structured tables appear
  *before* the YAML template body -- one covering the evidence arc (phases, namespaces, arc role)
  and at least one additional table covering gate design or skill catalog. Tables placed after
  the template, or a single combined table, do not pass.

Retroactive scoring of R4 variations under v21:

| Variation | C-18 | C-19 | v21 aspirational | v21 score |
|-----------|------|------|-----------------|-----------|
| V-01 (Contrast-First) | PASS -- Layer 2 has `# review:* requires draft:spec \| flow:*/trace:* require review:*` | FAIL -- gate quality table only (1 table); no arc table; skill catalog is bullet list | 10/12 = 8.33 pts | ~98/100 |
| V-02 (Dependency Narration) | PASS -- Layer 2 has `# draft:* produced here \| review:* requires draft-spec \| flow:*/trace:* require review:*` | FAIL -- BAD/GOOD gate examples are prose bullet pairs, not a table; no arc table | 9/12 = 7.47 pts | ~97/100 |
| V-03 (Compact Table) | FAIL -- Layer 2 template comment is `# ---- Layer 2: Depth ----` with no annotation | PASS -- arc table + gate criteria table + skill catalog table all before template | 9/12 = 7.47 pts | ~97/100 |
| V-04 (C-16+C-17) | PASS -- Layer 2 has `# draft:* produced here \| review:* requires draft-spec \| flow:*/trace:* require review:*` | FAIL -- gate quality table (1 table); skill catalog is bullet list; no arc table | 11/12 = 9.17 pts | ~99/100 |
| V-05 (Golden) | PASS -- Layer 2 has `# draft:spec produced here \| review:* requires it \| flow:*/trace:* require review:*` | FAIL -- gate quality table (1 table); GOOD example YAML is not an arc reference table; skill catalog is bullet list | 11/12 = 9.17 pts | ~99/100 |

**R4 C-19 gap**: Every high-scoring R4 variation misses C-19 by exactly one table. The gate
criteria table is present in all; the arc reference table is absent from all. Adding an arc
reference table (Layer, Namespaces, Arc role, Produces, Gate checkpoint) before the template
makes any of V-01, V-04, V-05 C-19 compliant.

**R4 C-18 gap**: Only V-03 (compact table) misses C-18. Its Layer 2 template divider has the
label (`# ---- Layer 2: Depth ----`) required by C-14 but not the artifact-flow annotation
required by C-18. One additional comment line fixes this.

**R5 target**: (1) add arc reference table before template in contrast-first variants (C-19
fix); (2) test whether table-rich format can satisfy C-19 while also picking up C-18; (3) test
lifecycle framing as a path to C-17 + C-19 + C-18; (4) combine all for golden 100/100.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Inertia framing + C-19 | BAD YAML cold open; arc table added after identity conclusion | Can arc table be inserted after contrast block without breaking C-16 (BAD still opens cold)? |
| Output format: table-rich | 3 pre-template tables; identity opens first (not BAD-first) | Can table-dominant format satisfy C-19 and C-18 while accepting C-16 FAIL? |
| Lifecycle emphasis | Per-phase narration of artifact handoffs + arc/gate tables | Does lifecycle prose produce richer C-17 and naturally support 2 pre-template tables? |
| C-16 + C-17 + C-18 + C-19 combined | Cold BAD open + narration + arc table + annotation | Does adding arc table to R4 V-04 achieve 100/100 under v21? |
| Golden synthesis (all 19) | All -- cold BAD open, narration, 3 tables, all-layer annotation | Does the richest combination achieve 100/100 with belt-and-suspenders coverage? |

Single-axis: V-01 (inertia framing + C-19), V-02 (table-rich format), V-03 (lifecycle emphasis)
Combined: V-04 (C-16+C-17+C-18+C-19), V-05 (golden, all 19 criteria)

---

## V-01 -- Inertia Framing + C-19 (single-axis: inertia framing)

**Axis**: Inertia framing with C-19 fix -- BAD YAML opens cold (C-16 PASS), arc reference table
added after the identity conclusion and before the gate criteria table (both tables now present
before the output template, C-19 PASS). Dependency narration deliberately omitted to keep the
axis clean.
**Hypothesis**: An arc reference table inserted after the BAD+diagnosis block does not break
C-16 -- the BAD YAML still opens cold; the table is downstream of the identity conclusion.
Adding only an arc table to R4 V-01's structure is the minimal fix for C-19. C-17 deliberately
omitted. Expected: C-16 PASS, C-18 PASS, C-19 PASS, C-17 FAIL -- 11/12 aspirational = ~99/100.

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
simulates a flow that `review:design` has not yet validated. `trace:request` traces a path
through an unreviewed design. `listen:feedback` synthesizes across signals that have not been
gathered or validated. `"done"` is unverifiable: the next phase owner has no artifact to check,
no threshold to compare against. The team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before advancing.
A plan without meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**Evidence arc -- three-layer structure:**

| Layer | Namespaces | Arc role | Produces | Gate checkpoint |
|-------|------------|----------|----------|-----------------|
| 1: Breadth | scout, prove:websearch/intelligence | Exploration | Scout signals, feasibility/requirements artifacts | >= N scout signals present |
| 2: Depth | draft, review, prove, flow, trace | Design + validation + simulation | Spec, review/prove artifacts, flow/trace artifacts | draft-spec present; 0 P0 findings open |
| 3: Synthesis | listen, topic | Closing | Listen signals, topic artifacts | All prior signals archived |
| (auto) | -- | Echo | -- | (none) |

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes C-04? |
|---|---|---|
| Execution state | `"Layer 1 complete"` | NO -- unverifiable by next phase owner |
| Empty or vague | `"done"` / `""` | NO -- names nothing |
| Artifact-referencing | `"scout-feasibility artifact present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + satisfies C-09 |

At least one non-echo gate must be quantified: `">= N signals"`, `"0 P0 findings open"`, or
equivalent numeric threshold.

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
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
  strategy: "<one-sentence goal>"

  stages:

  # ---- Layer 1: Breadth -- scout the space before designing ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts present; numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design, validate, simulate ----
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

  # ---- Layer 3: Synthesis -- listen ahead, close the evidence loop ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived>"

  # ---- Final Stage: echo -- required, always last ----

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

## V-02 -- Table-Rich Format (single-axis: output format)

**Axis**: Output format -- three pre-template tables (arc, gate criteria, skill catalog) dominate
the instruction section before the output template. Identity opens the prompt (not BAD-first).
Tests whether table-dominant format achieves C-19 PASS and C-18 PASS while accepting C-16 FAIL
as the deliberate single-axis cost.
**Hypothesis**: Three distinct pre-template tables satisfy C-19. C-18 annotation in the template
Layer 2 comment passes independently. C-16 FAIL (identity opens before any BAD example) is the
deliberate cost of the table-first format. C-17 FAIL (no prose dependency narration -- tables
only). Expected: C-19 PASS, C-18 PASS, C-16 FAIL, C-17 FAIL -- 10/12 aspirational = ~98/100.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal plugin skills into a staged program plan with named phases, non-trivial
evidence gates, and a three-layer arc. Skills run independently; the program does not execute
them. Final stage is always `echo` (auto, no skills). The program's only product is the gate.

---

You are running `/program:plan` for topic **{{topic}}**.

**Evidence arc:**

| Layer | Namespaces | Arc role | Produces | Requires |
|-------|------------|----------|----------|----------|
| 1: Breadth | scout, prove:websearch/intelligence | Exploration | Scout signals, feasibility/requirements artifacts | (none) |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* artifacts (Layer 2b) |
| 3: Synthesis | listen, topic | Closing | Listen signals, topic artifacts | All prior layers |
| (auto) | -- | Echo | -- | (none) |

**Gate design principles:**

| Gate property | Requirement | BAD example | GOOD example |
|--------------|-------------|-------------|--------------|
| Evidence state | Names artifact or signal that must *exist*, not what was done | `"layer 1 complete"` | `"scout-feasibility artifact present"` |
| Non-trivial | Not `"done"`, `"complete"`, or empty | `"done"` | `"scout-requirements artifact present"` |
| Quantified (>= 1 gate) | Numeric threshold or count expression | `"some scout signals present"` | `">= 2 scout signals AND draft-spec present"` |

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
  strategy: "<one-sentence goal>"

  stages:

  # ---- Layer 1: Breadth ----

    - name: "<breadth-phase-label>"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<named scout artifacts; numeric threshold>"

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
      gate: "<review/prove artifacts present; 0 P0 findings>"

    - name: "<simulation-or-remove>"          # optional
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis ----

    - name: "<synthesis-phase-label>"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<listen artifacts; all prior signals archived>"

  # ---- Final Stage ----

    - name: echo
      skills: []
      auto: true
```

## Plan Verification

| Check | Pass condition |
|-------|----------------|
| [ ] Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after |
| [ ] Valid skills | All skill names from Signal's 9 namespaces; no invented names |
| [ ] Evidence gates | Every non-echo gate names artifact or signal state -- not execution state |
| [ ] Quantified gate | >= 1 non-echo gate has numeric threshold |
| [ ] Descriptive names | Stage names are phase labels, not namespace names, not indices |
| [ ] Layer comments | Layer 1 / Layer 2 / Layer 3 section comments preserved in YAML |
| [ ] REQUIRED comment | `# REQUIRED: preserve this comment` line preserved in output |

---

## V-03 -- Lifecycle Emphasis (single-axis: lifecycle emphasis)

**Axis**: Lifecycle emphasis -- per-phase prose narrates what each phase produces and what the
next requires. This is the primary instructional structure; tables support it but do not replace
the prose chain. Identity opens the prompt (C-12 PASS, C-16 FAIL by design -- single-axis).
**Hypothesis**: Lifecycle-narrated prose produces richer C-17 (explicit artifact dependency
chain stated in prose) than rule-bullet format. Two pre-template tables (arc + gate criteria)
satisfy C-19. C-18 annotation in template satisfies C-18. C-16 FAIL (identity-first, not
BAD-first) is the deliberate single-axis cost. Expected: C-17 PASS, C-18 PASS, C-19 PASS,
C-16 FAIL -- 11/12 aspirational = ~99/100.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

Signal programs move through phases. Each phase produces artifacts the next phase requires.
The ordering is not a convention -- it is a dependency graph. A `draft:spec` requires feasibility
signals from Layer 1 before it is design rather than speculation. A `review:design` requires a
spec before it can review anything. A `flow:lifecycle` simulation requires a reviewed design
before its results mean anything. The program's value is not the list of skills; it is the gate
that enforces each handoff.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact lifecycle -- why stages are ordered:**

**Layer 1: Breadth** runs scout skills and early prove skills (websearch, intelligence,
hypothesis). These produce the feasibility, requirements, market, and competitor signals that
Layer 2 needs before it can design anything. A `draft:spec` without feasibility and requirements
signals is speculation, not engineering. Layer 1's signals are Layer 2's required input; the gate
between them makes this dependency explicit and checkable.

**Layer 2: Depth** has sub-stages ordered by what each sub-stage produces. The design sub-stage
produces the `draft-spec` artifact -- the central document everything downstream depends on. The
validation sub-stage (`review:design`, `review:users`, `prove:prototype`) cannot run before the
spec exists: you cannot review a spec that has not been written. The gate between design and
validation states this dependency explicitly: the next phase owner checks that `draft-spec` is
present before any review skill starts. Flow and trace skills run after review because they
simulate and trace a design that has been validated -- tracing a contract that has not been
reviewed for design correctness propagates unvalidated assumptions forward.

**Layer 3: Synthesis** runs `listen:*` and `topic:*` last because they synthesize across all
prior signals. `listen:adoption` requires the validated design context that Layer 2 produced.
`topic:story` requires the full evidence arc to tell a coherent narrative. Running synthesis
before validation produces a story built on unvalidated signals.

**Echo** is automatic and has no skills. It always runs last.

**Evidence arc:**

| Layer | Namespaces | Arc role | Produces | Requires |
|-------|------------|----------|----------|----------|
| 1: Breadth | scout, prove (early) | Exploration | Scout signals | (none) |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* (Layer 2b) |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers |
| (auto) | -- | Echo | -- | (none) |

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"all Layer 1 skills run"` | NO -- unverifiable |
| Empty or vague | `"done"` / `""` | NO -- names nothing |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals; draft-spec artifact present"` | YES + C-09 |

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
        - scout:<skill>
        - scout:<skill>
      gate: "<scout artifacts Layer 2 design requires; numeric threshold: '>= N scout signals'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>
      gate: "<draft-spec artifact present; validation requires this before reviewing>"

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

  # ---- Final Stage: echo -- required, always last ----

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
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output

---

## V-04 -- Combined: C-16 + C-17 + C-18 + C-19 (minimal C-19 fix on golden path)

**Axes**: Contrast-first structure (C-16) + explicit dependency narration (C-17) + C-18 YAML
annotation (already in R4 V-04) + arc reference table before template (C-19 fix).
**Hypothesis**: Adding one arc reference table to R4 V-04's structure -- which already achieves
C-16, C-17, C-18 PASS -- fixes the only R4 C-19 failure with minimal structural change. The
arc table and gate criteria table are placed after the identity conclusion, before the template.
C-16 is unaffected (BAD still opens cold; tables are downstream of the contrast). Expected: all
12 aspirational PASS -- 100/100.

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

Signal programs are layered by what each stage produces and what the next stage requires.
Layer 1 (Breadth) produces scout signals -- feasibility, requirements, market, competitor
artifacts. Layer 2 cannot design before Layer 1 has produced these signals: a `draft:spec`
without feasibility or requirements signals is speculation, not design. Layer 1's output is
Layer 2's required input; the gate between them makes this dependency checkable.

Layer 2 has sub-stages ordered by what each produces. The design sub-stage produces the
`draft-spec` artifact; the validation sub-stage (`review:design`, `prove:prototype`) requires
this artifact before any review skill can run -- `review:design` reviews a spec, and without
a spec there is nothing to review. The gate between design and validation states this dependency
explicitly: the next phase owner checks that `draft-spec` exists before starting any review.
Flow and trace skills require review artifacts before running -- tracing a contract that has not
been reviewed for correctness builds simulation on an unvalidated foundation; these run last
in Layer 2.

Layer 3 (Synthesis) runs `listen:*` and `topic:*` last because they synthesize across all prior
signals. `listen:adoption` requires the validated context Layer 2 produced; `topic:story` requires
the full evidence arc to tell a coherent narrative. Running synthesis before validation produces
a story built on unvalidated signals.

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
      gate: "<named scout artifacts Layer 2 design requires;
             numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # draft:spec, draft:proposal
      gate: "<draft-spec artifact present; Layer 2 validation requires it before reviewing>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present; review artifacts confirmed before this stage>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
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
- [ ] Three arc-layer comments (Layer 1 / Layer 2 / Layer 3) preserved in YAML
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output

---

## V-05 -- Golden Synthesis (all 19 criteria)

**Axes**: All -- cold BAD open (C-16), explicit dependency narration (C-17), arc reference table
+ gate criteria table + skill catalog table before template (C-19, belt-and-suspenders), C-18
annotation on all three layer dividers (richer than V-04's Layer 2-only annotation), pre-printed
8-item checklist including C-18 preservation check.
**Hypothesis**: Fixes R4 V-05's C-19 gap by adding arc reference table (now 2+ tables before
template). Extends C-18 to all three layer dividers. Adds skill catalog table (3rd pre-template
table, C-19 belt-and-suspenders). 8-item checklist protects C-18 annotation from accidental
omission. Expected: all 12 aspirational PASS -- 100/100.

**Key change from R4 V-05**: R4 V-05 had the gate quality table (1 table) and skill catalog
as bullet list -- C-19 FAIL. R5 V-05 adds an arc reference table (2 distinct tables on distinct
concerns) and converts the skill catalog to a table (3 tables total, fully satisfying C-19).
C-18 is also extended: Layer 1 and Layer 3 dividers now include artifact-flow annotations
alongside Layer 2.

---

### Prompt body

```yaml
# This is what a plan without an arc looks like:

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

One stage. Seven skills. No dependency order. `review:design` requires a spec that `draft:spec`
has not yet produced -- they are in the same flat list, ordered by nothing. `flow:lifecycle`
simulates a flow that `review:design` has not yet validated -- the simulation runs on an
unreviewed design and propagates design errors forward. `trace:request` traces a request path
through a design that has not been confirmed sound. `listen:feedback` synthesizes across signals
that have not been gathered or validated -- there is nothing yet to synthesize. `"done"` means
nothing: no artifact to check, no threshold to compare, no shared definition of readiness. The
team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed here still runs standalone -- the program does
not execute them, advance stages, or carry any automation authority. Its value is the gate and
the arc: a shared definition of what evidence must exist before each handoff, structured in the
order that reflects how artifacts depend on each other.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

Signal programs are layered by what each stage produces and what the next stage requires.
Layer 1 (Breadth) produces scout signals -- feasibility, requirements, market, competitor
artifacts. Layer 2's design skills require these signals before they can produce a meaningful
spec: a `draft:spec` without feasibility or requirements signals is speculation, not design.
Layer 1's output is Layer 2's required input; the gate between them makes this dependency
explicit and checkable.

Layer 2's design sub-stage produces the `draft-spec` artifact. The validation sub-stage
(`review:design`, `review:users`, `prove:prototype`) requires this artifact -- `review:design`
reviews a spec, and without a spec there is nothing to review. The gate between design and
validation states this dependency explicitly: the next phase owner checks that `draft-spec`
exists before any review skill starts. Flow and trace skills require review artifacts before
running -- tracing a request path that has not been reviewed for design correctness builds
simulation on an unvalidated foundation; these run last in Layer 2.

Layer 3 (`listen:*`, `topic:*`) synthesizes across all prior signals and runs last because
it has the most to synthesize. `topic:story` requires the full evidence arc to tell a coherent
narrative. Running synthesis before validation produces a story built on unvalidated signals.

**Evidence arc:**

| Layer | Namespaces | Arc role | Produces | Requires |
|-------|------------|----------|----------|----------|
| 1: Breadth | scout, prove:websearch/intelligence | Exploration | Scout signals, feasibility/requirements artifacts | (none) |
| 2a: Design | draft | Architecture | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | review, prove | Review + prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | flow, trace | Simulation (optional) | Flow/trace artifacts | review:* artifacts (Layer 2b) |
| 3: Synthesis | listen, topic | Closing | Listen/topic artifacts | All prior layers |
| (auto) | -- | Echo | -- | (none) |

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"all reviews done"` | NO -- names what was done, not what exists |
| Empty or vague | `"done"` / `""` | NO -- unverifiable |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + C-09 |

Require at least one quantified gate. Numeric thresholds make gates machine-checkable in
principle and signal deliberate evidence design.

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

**Produce the following output exactly -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim with each box checked:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----
  # scout:* produced here | Layer 2 draft:* requires these signals before drafting

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts; Layer 2 design requires these before drafting;
             numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # draft:spec, draft:proposal
      gate: "<draft-spec artifact present; Layer 2 validation requires it before reviewing;
             at least ONE gate across the plan must be quantified>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # review:design, review:users, review:customers...
        - prove:<skill>                       # prove:prototype, prove:analysis, prove:interview...
      gate: "<review/prove artifacts present; P0 threshold: '0 P0 findings open'>"

    - name: "<simulation-or-remove>"          # optional; add if flow/trace signals needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present; review artifacts confirmed before this stage>"

  # ---- Layer 3: Synthesis -- synthesizes all prior signals; runs after all validation ----
  # listen:*/topic:* require all Layer 2 artifacts; echo follows automatically

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                      # listen:adoption, listen:feedback, listen:support
        - topic:<skill>                       # topic:plan, topic:report, topic:story...
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
- [ ] Three arc-layer comments (Layer 1 / Layer 2 / Layer 3) preserved in YAML output
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output
- [ ] Layer 2 divider comment includes artifact-flow annotation (`draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*`) preserved in YAML output

---

## Predicted v21 Scores

| Variation | C-16 | C-17 | C-18 | C-19 | Aspirational passes | Predicted score |
|-----------|------|------|------|------|---------------------|-----------------|
| V-01 Inertia+C-19 | PASS | FAIL (omitted) | PASS | PASS | 11/12 = 9.17 pts | ~99/100 |
| V-02 Table-Rich | FAIL (identity-first) | FAIL (tables not prose) | PASS | PASS | 10/12 = 8.33 pts | ~98/100 |
| V-03 Lifecycle | FAIL (identity-first) | PASS | PASS | PASS | 11/12 = 9.17 pts | ~99/100 |
| V-04 C-16+C-17+C-18+C-19 | PASS | PASS | PASS | PASS | 12/12 = 10 pts | **100/100** |
| V-05 Golden | PASS | PASS | PASS | PASS | 12/12 = 10 pts | **100/100** |

**V-01**: Loses C-17 by design (single-axis). 11/12 aspirational. Total: 60 + 30 + 9.17 = 99.17.
Golden = YES.

**V-02**: Loses C-16 (identity opens before BAD, single-axis format) and C-17 (tables not prose).
10/12 aspirational. Total: 60 + 30 + 8.33 = 98.33. Golden = YES.

**V-03**: Loses C-16 (identity opens before BAD, single-axis lifecycle). 11/12 aspirational.
Total: 60 + 30 + 9.17 = 99.17. Golden = YES.

**V-04 and V-05 predicted 100/100 under v21.** V-04 is the minimal-surface path: one arc table
added to R4 V-04's structure, nothing else changed. V-05 achieves 100/100 with richer C-18
(three-layer annotation vs Layer 2-only), three pre-template tables (belt-and-suspenders for
C-19), and an 8-item checklist explicitly protecting the C-18 annotation from omission.

**V-01 is the minimal path to C-16 + C-19**: demonstrates that an arc reference table added
after the BAD+diagnosis block does not break C-16. The BAD example still opens cold; the table
is downstream of the identity conclusion. 99/100, one criterion short of golden (C-17 FAIL).

**V-03 vs V-01**: Both predict 99/100 (11/12 aspirational). V-01 achieves 99 via inertia
framing (C-16 PASS, C-17 FAIL). V-03 achieves 99 via lifecycle framing (C-16 FAIL, C-17 PASS).
Together they test whether C-16 and C-17 can be independently satisfied by their respective
structural approaches -- useful if a future rubric version makes one of them worth more.
