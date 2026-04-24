---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 4
rubric: v20
---

# program-plan -- R4 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v20 (C-01 through C-17, 17 criteria, golden = all essential pass
AND composite >= 80).

---

## R3 Retrospective Under v20 Rubric

v20 adds two aspirational criteria to the v19 set:

- **C-16** (contrast-grounded identity): BAD example opens the output FIRST; diagnosis follows;
  not-executor identity emerges AS THE CONCLUSION of that contrast. Requires C-10 PASS + C-12
  PASS AND a specific structural order. An output that asserts not-executor first and then shows
  a contrast does NOT pass C-16 -- the BAD example must precede and motivate the identity claim.
- **C-17** (explicit dependency narration): at least one prose sentence explicitly names a
  cross-stage artifact dependency -- stating WHAT stage N produces AND WHY stage N+1 requires it.
  Structural ordering (scout before draft) or bullet-rule notation does not pass; the causal link
  must be stated in prose.

Retroactive scoring of R3 variations under v20:

| Variation | C-16 | C-17 | v20 score |
|-----------|------|------|-----------|
| V-01 (Role Sequence) | FAIL -- identity asserted first; no contrast | FAIL -- structural YAML comments only; no prose causal chain | ~94/100 |
| V-02 (Phrasing Register) | FAIL -- identity asserted first; no contrast | FAIL -- question framing does not name artifact causation | ~94/100 |
| V-03 (Inertia Framing) | PASS -- BAD opens cold; diagnosis; "exists to replace this pattern" as conclusion | PASS -- "you cannot review a spec that has not been written; you cannot trace a flow that has not been reviewed" | **~100/100** |
| V-04 (Role+Lifecycle) | FAIL -- "is a plan, not an executor" opens first; BAD/GOOD table appears later | PASS -- "Review skills require the spec from Phase 2. Flow and trace skills require review artifacts." | ~99/100 |
| V-05 (Golden) | FAIL -- "is a plan, not an executor" opens first; BAD YAML shown second | BORDERLINE -- "`review:* requires draft:spec`" is a rule bullet, not a prose causal chain | ~97/100 |

**R3 V-03 retroactively scores ~100/100 under v20.** The contrast-first opening naturally
satisfied C-16; the dependency prose in the diagnosis block satisfied C-17.

**R3 V-04 fails C-16**: identity is asserted in the opening sentence before any contrast.
**R3 V-05 fails C-16**: same structural error -- identity first, BAD second. Also loses ~1 pt
on C-17 if the scorer reads rule bullets as insufficient prose narration.

**R4 target**: fix V-05's C-16 failure (BAD must precede identity, not follow it), add explicit
C-17 dependency narration prose, and test whether the compact table format (V-03) can satisfy
both new criteria when format constraints force prose-avoidance.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Contrast-first structure | BAD YAML opens cold with no preamble; identity emerges as conclusion | C-16: can contrast-first structure alone achieve 99/100 (C-17 deliberately omitted)? |
| Dependency narration emphasis | Explicit prose artifact chain is the primary instructional structure | C-17: does narration-first produce richer dependency prose than rule bullets? |
| Compact table format | All structure in tables; minimal free prose | Can table format satisfy C-16 and C-17? (expected FAIL both -- format axis) |
| C-16 + C-17 combined | Cold BAD open + explicit dependency narration prose | Do the two new criteria reinforce each other when targeted together? |
| All-axes golden | All -- cold BAD open, dependency narration, pre-printed template, full arc | Does fixing R3 V-05's C-16 error achieve 100/100 under v20? |

Single-axis: V-01 (contrast-first), V-02 (dependency narration), V-03 (compact table)
Combined: V-04 (C-16 + C-17), V-05 (golden, all 17 criteria)

---

## V-01 -- Contrast-First Structure (single-axis: C-16)

**Axis**: Contrast-first structure -- BAD YAML opens cold; no preamble, no skill introduction,
no header. Just the bad program. Diagnosis follows. Not-executor identity emerges as the
conclusion of the contrast.
**Hypothesis**: A pure contrast-first opening (BAD before everything else) satisfies C-16 and
carries C-10 and C-12 as byproducts. C-17 is deliberately omitted -- no explicit dependency
narration prose -- to keep the axis clean. Expected: C-16 PASS, C-17 FAIL, ~99/100.

---

### Prompt body

```yaml
# This is what most teams produce when planning a Signal investigation:

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
        - listen:feedback
      gate: "done"
    - name: echo
      skills: []
      auto: true
```

One stage. One gate that means nothing. Skills in the wrong order -- `review:design` requires
a spec that `draft:spec` has not yet produced; `flow:lifecycle` simulates a flow that
`review:design` has not yet validated; `listen:feedback` synthesizes signals that have not been
gathered or validated. `"done"` is unverifiable: the next phase owner has no artifact to check
and no threshold to compare against. The team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the program
does not execute them, advance stages, or carry any automation authority. Its only product is the
gate: a shared, evidence-specific condition that must be true before advancing. A plan without
meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**What you are building**: a staged YAML plan with named phases, ordered skills, and
artifact-referencing gates. One topic. One program. One shared definition of readiness per phase.

**Gate rule -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"all scout complete"` | NO -- names what was done, not what exists |
| Empty or vague | `"done"` / `""` | NO -- unverifiable |
| Artifact-referencing | `"scout-feasibility artifact present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + C-09 |

At least one non-echo gate must be quantified (numeric threshold or count expression).

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
  strategy: "<one-sentence goal>"

  stages:

  # ---- Layer 1: Breadth -- scout the space before designing ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts present; numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design, validate, simulate ----
  # review:* requires draft:spec | flow:*/trace:* require review:* | prove:* before flow/trace

    - name: "<depth-phase-label>"             # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; numeric threshold: '0 P0 findings open'>"

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

## V-02 -- Dependency Narration Emphasis (single-axis: C-17)

**Axis**: Dependency narration emphasis -- explicit prose narration of why stages are ordered is
the primary instructional structure, not a side note or rule bullet.
**Hypothesis**: Framing the dependency chain as narrated causal prose ("Layer 1 produces X;
Layer 2 requires X before it can run -- here is why") produces dependency statements that
unambiguously satisfy C-17. No BAD/GOOD contrast (C-10, C-16 expected FAIL) to keep the axis
clean. Not-executor asserted at opening (C-12 PASS). Expected: C-17 PASS, C-16 FAIL, ~98/100.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Every skill
in the plan remains independently runnable -- the program does not execute them, does not advance
stages, and carries no automation authority. What makes the program useful is not the list of
skills; it is the gates. Gates are the plan's only product. A plan without meaningful gates
is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**Why stages are ordered the way they are -- the artifact dependency chain:**

Signal programs are layered by what each layer produces and what the next layer requires.
The ordering is not a convention; it is a dependency graph.

**Layer 1: Breadth** runs scout skills and early prove skills (websearch, intelligence,
hypothesis). These produce feasibility signals, requirements signals, and market signals. Layer 2
cannot draft a spec before Layer 1 has produced these signals -- a `draft:spec` without a
feasibility signal is speculation, not design. A `draft:proposal` without `scout:requirements`
is missing its brief. Layer 1's output is Layer 2's required input.

**Layer 2: Depth** has two sub-stages. The design sub-stage consumes Layer 1's scout signals
and produces the `draft-spec` artifact. The validation sub-stage runs `review:*` and `prove:*`
skills; these require the `draft-spec` artifact before they can run -- `review:design` reviews
a spec, and there is no review without a spec to review. The gate between design and validation
makes this dependency checkable: the next phase owner verifies that `draft-spec` exists before
any review skill starts. Flow and trace skills run last in Layer 2 because they require review
artifacts -- tracing a contract that has not been reviewed for design correctness builds
simulation on an unvalidated foundation.

**Layer 3: Synthesis** runs `listen:*` and `topic:*` skills last because they synthesize across
all prior signals. `listen:adoption` requires the validated design context that Layer 2 produced;
`topic:story` requires the full evidence arc to tell a coherent narrative. Running synthesis
before validation produces a story built on unvalidated signals.

**Echo** runs last, always. It is automatic and has no skills.

---

**Gate design -- evidence state, not execution state:**

- BAD: `"Layer 1 complete"` -- execution state; the next phase owner cannot verify it
- BAD: `"done"` -- names nothing; team advances on shared optimism
- GOOD: `"scout-feasibility and scout-requirements artifacts present; >= 2 scout signals reviewed"`
  -- artifact state; verifiable by anyone
- GOOD: `"draft-spec artifact present; no blocking feasibility gaps from Layer 1"` -- artifact
  state plus handoff condition

At least one gate must be quantified: `">= N signals"`, `"0 P0 findings open"`, or equivalent
numeric threshold.

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

  # ---- Layer 1: Breadth -- produces scout signals that Layer 2 design requires ----

    - name: "<breadth-phase-label>"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<named scout artifacts present; Layer 2 design skills require these before drafting;
             numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace require review ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"
      skills:
        - draft:<skill>
      gate: "<draft-spec artifact present; Layer 2 validation requires this before reviewing>"

    - name: "<validation-phase-label>"
      skills:
        - review:<skill>
        - prove:<skill>
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present; review artifacts required before this stage>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived>"

  # ---- Final Stage: echo -- required, always last ----

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
- [ ] Three arc-layer comments (Layer 1 / Layer 2 / Layer 3) preserved in YAML
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output

---

## V-03 -- Compact Table Format (single-axis: output format)

**Axis**: Output format -- all structural information (arc layers, dependency rules, gate
criteria, skill catalog) presented in tables; minimal free prose.
**Hypothesis**: A table-dominant format can satisfy all essential and recommended criteria and
most aspirational criteria. C-16 and C-17 are expected to FAIL -- contrast-grounded identity
requires a contrast-first prose structure, and explicit dependency narration requires causal
prose sentences that tables cannot substitute. These failures isolate whether the format axis
specifically blocks the two new v20 criteria. Expected: C-16 FAIL, C-17 FAIL, ~97/100.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

Produces `program.yaml`: staged skill sequence with named phases, non-trivial gates, and a
three-layer arc. Skills run standalone; the program does not execute them. Final stage is always
`echo` (auto, no skills).

---

You are running `/program:plan` for topic **{{topic}}**.

**Evidence arc:**

| Layer | Phase role | Namespaces | Produces | Requires |
|-------|------------|------------|----------|----------|
| 1: Breadth | Exploration | scout, prove:websearch/intelligence | Scout signals | (none) |
| 2a: Design | Architecture | draft | draft-spec artifact | Layer 1 scout signals |
| 2b: Validation | Review + prove | review, prove | Review/prove artifacts | draft-spec (Layer 2a) |
| 2c: Simulation | Simulation (optional) | flow, trace | Flow/trace artifacts | review:* (Layer 2b) |
| 3: Synthesis | Closing | listen, topic | Listen signals, topic artifacts | All prior layers |
| (auto) | Echo | -- | -- | (none) |

**Gate criteria:**

| Gate property | Requirement | Example |
|--------------|-------------|---------|
| Evidence state | Names artifact or signal that must *exist* | `"scout-feasibility artifact present"` |
| Non-trivial | Not `"done"`, `"complete"`, empty | -- |
| Quantified (>= 1 gate) | Numeric threshold or count | `">= 2 scout signals"` / `"0 P0 findings"` |

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
      gate: "<named artifacts; numeric threshold>"

  # ---- Layer 2: Depth ----

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
| [ ] Layer comments | Three layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved |
| [ ] REQUIRED comment | `# REQUIRED: preserve this comment` line preserved in output |

---

## V-04 -- Combined: Contrast-First + Dependency Narration (C-16 + C-17)

**Axes**: Contrast-first structure (C-16) + explicit dependency narration (C-17).
**Hypothesis**: Targeting both new v20 criteria together achieves 100/100 under v20. The
contrast-first opening (BAD opens cold, identity-via-contrast conclusion) satisfies C-16 while
the explicit dependency narration prose satisfies C-17. The two axes reinforce each other
naturally: the diagnosis block that follows the BAD YAML is the natural home for dependency
narration -- explaining WHY the bad pattern fails IS explaining what the correct dependency order
requires. Pre-printed template carries C-13, C-14, C-15.

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
them as peers in an unordered flat list. `trace:contract` runs before `review:design` has
confirmed the contract design is sound -- tracing an unreviewed contract propagates design errors
into the simulation. `listen:adoption` synthesizes nothing if there are no prior validated
signals to synthesize across. `"done"` tells no one when it is safe to advance; the team acts
on shared optimism, not shared evidence.

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
without a feasibility signal is speculation, not design. Layer 1's output is Layer 2's required
input; the gate between them makes this dependency checkable.

Layer 2 has two sub-stages. The design sub-stage produces the `draft-spec` artifact. The
validation sub-stage (`review:design`, `review:users`, `prove:prototype`) requires this artifact
-- `review:design` reviews a spec, and without a spec there is nothing to review. The gate
between design and validation states this dependency explicitly: the next phase owner checks that
`draft-spec` exists before starting any review. Flow and trace skills require review artifacts
before running -- tracing a contract that has not been reviewed for correctness builds simulation
on an unvalidated foundation; these run last in Layer 2.

Layer 3 (Synthesis) runs `listen:*` and `topic:*` last because they synthesize across all prior
signals. `listen:adoption` requires the validated context that Layer 2 produced; `topic:story`
requires the full evidence arc to tell a coherent narrative. Running synthesis before validation
produces a story built on unvalidated signals.

---

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
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- produces scout signals Layer 2 design requires before drafting ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts Layer 2 design requires;
             numeric threshold: '>= N scout signals present'>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace require review ----
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

## V-05 -- Golden Synthesis (all 17 criteria)

**Axes**: All -- cold BAD open, explicit dependency narration, pre-printed arc-labeled template
with REQUIRED preserve comment and pre-printed checklist, GOOD example contrast, quantified
gate requirement, descriptive stage names.
**Hypothesis**: Fixing R3 V-05's C-16 failure (BAD YAML now precedes identity claim rather than
following it) and adding an explicit C-17 dependency narration prose block achieves 100/100 under
v20. All other machinery is inherited from R3 V-05, which scored 100/100 on v19 when its C-16
error was not yet a criterion.

**Key structural change from R3 V-05**: R3 V-05 opened "**`/program:plan` is a plan, not an
executor.**" before showing the BAD YAML -- C-16 FAIL. R4 V-05 opens cold with BAD YAML first,
diagnosis second (including explicit dependency narration for C-17), identity-via-contrast as
the conclusion. The not-executor identity now emerges FROM the contrast rather than preceding it.

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

One stage. Seven skills. No dependency order -- `review:design` requires a spec that `draft:spec`
has not yet produced; `flow:lifecycle` simulates a flow that `review:design` has not yet
validated; `trace:request` traces a path through an unreviewed design; `listen:feedback`
synthesizes signals that have not been gathered or validated. `"done"` means nothing: the next
phase owner has no artifact to check, no signal to verify, no threshold to compare against.
The team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed here still runs standalone -- the program
does not execute them, advance stages, or carry any automation authority. Its value is the gate
and the arc: a shared definition of what evidence must exist before each handoff, structured in
the order that reflects how artifacts depend on each other.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

Signal programs are layered by what each stage produces and what the next stage requires.
Layer 1 (Breadth) produces scout signals -- feasibility, requirements, market, competitor
artifacts. Layer 2's design skills require these signals before they can produce a meaningful
spec: a `draft:spec` without feasibility or requirements signals is speculation, not design.
Layer 2's design sub-stage then produces the `draft-spec` artifact; the validation sub-stage
(`review:design`, `review:users`, `prove:prototype`) requires this artifact before any review
skill can run -- `review:design` reviews a spec, and without a spec there is nothing to review.
Layer 2's flow and trace skills require review artifacts before running -- tracing a request
path that has not been reviewed for design correctness propagates unvalidated assumptions into
the simulation. Layer 3 (`listen:*`, `topic:*`) synthesizes across all prior signals and runs
last because it has the most to synthesize; `topic:story` requires the full evidence arc to
tell a coherent narrative.

---

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc, dependency order preserved, artifact-referencing gates
program:
  topic: "{{topic}}"
  stages:

  # Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      gate: "scout-feasibility, scout-requirements, scout-competitors artifacts present;
             >= 2 scout signals reviewed; no blocking feasibility concerns"

  # Layer 2: Depth -- draft-spec produced; review/prove require it; flow/trace require review
    - name: design
      skills:
        - draft:spec
        - draft:proposal
      gate: "draft-spec artifact present; Architect confirmed no blocking gaps from discovery"

    - name: expert-review
      skills:
        - review:design
        - review:users
        - prove:prototype
      gate: "review-design, review-users, prove-prototype artifacts present; 0 P0 findings open"

  # Layer 3: Synthesis -- synthesizes across all prior signals
    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: echo
      skills: []
      auto: true
```

Key distinctions: dependency order preserved; each gate names artifacts the next phase owner
needs; one gate is quantified (`>= 2 scout signals`); three arc layer comments make the
investigation strategy structurally visible.

---

**Gate design -- evidence state, not execution state:**

| Gate quality | Example | Passes? |
|---|---|---|
| Execution state | `"all reviews done"` | NO -- names what was done, not what exists |
| Empty or vague | `"done"` / `""` | NO -- unverifiable |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals AND draft-spec artifact present"` | YES + C-09 |

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
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----
  # Goal: establish what we know before committing to a design

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate: "<named scout artifacts; Layer 2 design requires these before drafting;
             numeric threshold: '>= N scout signals present'>"

    # Optional second breadth stage -- remove if not needed
    - name: "<breadth-phase-2-or-remove>"
      skills:
        - draft:<skill>                       # early structural artifact: pitch or hypothesis
      gate: "<artifact condition>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # Goal: commit to an approach and validate it against evidence
  # draft:spec produced here | review:* requires it | flow:*/trace:* require review:*

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

    # Optional simulation stage -- add if flow/trace signals needed; remove otherwise
    - name: "<simulation-or-remove>"
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present; review artifacts confirmed before this stage>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs last ----
  # Goal: confirm what users and adopters signal; narrative close

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
- [ ] Three arc-layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved in YAML
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output

---

## Predicted v20 Scores

| Variation | C-10 | C-12 | C-16 | C-17 | Predicted score |
|-----------|------|------|------|------|-----------------|
| V-01 Contrast-First | PASS | PASS (via contrast conclusion) | PASS | FAIL (omitted -- single-axis) | ~99/100 |
| V-02 Dependency Narration | FAIL (no contrast) | PASS | FAIL (C-10 fails) | PASS | ~98/100 |
| V-03 Compact Table | FAIL (no contrast) | PASS | FAIL (C-10 fails) | FAIL (tables not prose) | ~97/100 |
| V-04 C-16+C-17 Combined | PASS | PASS (via contrast) | PASS | PASS | **~100/100** |
| V-05 Golden | PASS | PASS (via contrast) | PASS | PASS | **~100/100** |

**V-01**: Loses C-17 (1.0 pt) by design -- single-axis; contrast-first kept clean from
dependency narration. Aspirational: 9/10 = 9.0 pts. Total: 60 + 30 + 9 = 99/100.

**V-02**: Loses C-10 and C-16 (2.0 pts) by design -- no contrast shown. Aspirational: 8/10 =
8.0 pts. Total: 60 + 30 + 8 = 98/100.

**V-03**: Loses C-10, C-16, C-17 (3.0 pts) by format -- table format cannot satisfy
contrast-first opening (C-16) or prose causal narration (C-17). Aspirational: 7/10 = 7.0 pts.
Total: 60 + 30 + 7 = 97/100.

**V-04 and V-05 predicted 100/100 under v20.** V-04 achieves this by combining the two new
targeted axes; V-04 is the minimal-surface-area path to 100/100 under v20 (no GOOD example
shown, leaner prose overall). V-05 achieves 100/100 with the additional GOOD example (making
C-10 doubly satisfied via labeled BAD/GOOD pair) and optional second breadth stage scaffold.

**V-01 is the minimal path to C-16**: demonstrates that a pure contrast-first opening achieves
C-16 with only the single deliberate C-17 miss -- 99/100, one criterion short of golden.
