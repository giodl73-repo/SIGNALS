---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 8
rubric: v8
---

# program-plan -- R8 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v8 (C-01 through C-30, 30 total criteria: 4 essential,
3 recommended, 23 aspirational, golden = all essential pass AND composite >= 80 of 205).

---

## R7 Retrospective Under v8 Rubric

v8 adds three aspirational criteria (C-28, C-29, C-30) derived from R7 excellence signals.
The previous rubric had 20 aspirational criteria (C-08 through C-27). v8 expands to 23.

**New criteria:**

- **C-28** (Structural Gate Target Field Co-Location): The production `gate:` field appears as a
  named sibling YAML key alongside `gate_fail:` / `gate_pass:` at each non-echo zone. C-24
  requires the contrast fields to exist as YAML keys; C-28 requires the production target to
  co-locate as a third sibling key, making the output slot structurally unambiguous.
  R7 source: V-02 and V-03 both used `gate_fail:/gate_pass:/gate:` as actual YAML sibling keys
  at all 5 non-echo zones.

- **C-29** (Correction Table Recommended-Tier Pairs): The correction table (C-18) includes at
  least one wrong-to-correct pair for each of C-05, C-06, and C-07 individually. C-22 requires
  error artifacts to cover all three recommended criteria; C-29 requires the correction table
  specifically to carry that coverage so the pre-generation lookup artifact covers quality
  failures as well as structural ones.
  R7 source: V-02's 13-row correction table included rows for C-05 (dep order), C-06
  (namespace-label-to-intent-label stage name), and C-07 (executor-framing-to-plan-identity).

- **C-30** (Dep-Reminder and Correction-Bridge Independence): At dependency-bearing `skills:`
  lines, a dep constraint reminder (`# requires: <artifact> from Zone: <name> (C-05)`) and a
  correction-table navigational bridge (`# check correction table`) are each present
  independently. C-21 and C-23 are both prerequisites.
  R7 source: V-02's Design zone skills line carried only `# check correction table: skill names`
  with no dep reminder, earning C-20/C-23 PARTIAL; V-03 carried both annotations independently
  at all 4 dep zones, first achieving C-30 PASS.

**Scoring change:** Aspirational 20 → 23 criteria (C-08 through C-30), 100 → 115 pts.
Total max: **205 pts.** Golden threshold (>= 80 composite) unchanged.

**Retroactive scoring of R7 V-05 under v8:**

| Criterion | R7 V-05 status | Reason |
|-----------|---------------|--------|
| C-24 | FAIL | Template had simple `gate:` placeholders, not `gate_fail:`/`gate_pass:` YAML keys |
| C-25 | FAIL | No `Why:` rationale annotations on gate contrast examples |
| C-26 | FAIL | No criterion-tagged structural gate fields (no `gate_fail:` fields to tag) |
| C-27 | FAIL | No dep reminders in template; nothing to apply uniform syntax to |
| C-28 | FAIL | No `gate:` sibling (no gate_fail:/gate_pass: base) |
| C-29 | FAIL | No correction table at all |
| C-30 | FAIL | No dep reminders at skills lines; correction bridges absent |
| C-16 | FAIL | BAD YAML block lacked `# WRONG C-XX` criterion tags |
| C-17 | PARTIAL | Central gate table present but not per-zone inline contrast |
| C-18 | FAIL | No correction table |
| C-20 | FAIL | Dep reminders at zone headers only (not at skills: placeholder lines) |
| C-21 | FAIL | No correction table scaffold bridges |
| C-23 | FAIL | Skills: lines lacked dep reminders (headers had them but not skills lines) |

R7 V-05 estimated score under v8: ~11–13/23 aspirational. Not golden.

**R8 target:** All 23 aspirational pass. V-05 is the synthesis.

---

## Variation Axis Plan

Single-axis (one new criterion cluster per variation):

- **V-01** — C-24/C-25/C-26/C-28 cluster (structural three-field gate zone)
- **V-02** — C-18/C-19/C-21/C-22/C-29 cluster (correction table with recommended-tier pairs)
- **V-03** — C-16/C-17/C-20/C-23/C-27/C-30 cluster (dep reminders + criterion tags)

Combo:

- **V-04** — C-28 + C-29 (three-field gates + full correction table; no C-30)
- **V-05** — Golden synthesis: all 23 criteria, richest form

---

## V-01 -- Structural Three-Field Gate Zone (single-axis: C-24/C-25/C-26/C-28)

**Axis**: Template gate fields as YAML structural keys. Simple `gate:` placeholder replaced with
`gate_fail:` / `gate_pass:` / `gate:` as actual sibling YAML keys at every non-echo zone.
`gate_fail:` carries `# WRONG C-04` criterion tag (C-26). `gate_pass:` carries `# Why:` rationale
(C-25). `gate:` is the production authoring target (C-28). All other elements preserved from R7
V-05 base: same BAD YAML opening, same layer narration, same gate design table, same skill
catalog table, same REQUIRED echo annotations, same Plan Verification table. No correction table;
no dep reminders at skills lines.

**Hypothesis**: The three-field gate structure passes C-24 (structural gate-contrast fields),
C-25 (gate contrast rationale), C-26 (criterion-tagged structural gates), and C-28 (production
gate co-location) as a single self-consistent cluster without disturbing previously passing
criteria. C-17 upgrades to PASS (per-zone contrast now structural). C-12 improves (per-zone gate
structure is a second anchor for C-04). Expected delta: +4 aspirational criteria pass.

---

### Prompt body

```
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

**Layer 2 (Depth) -- artifact scope and internal handoff contracts between design, validation, and simulation:**

Layer 2 produces the design, validation, and simulation artifact set. It has internal dependency
constraints. Sub-stage ordering within Layer 2: (1) design sub-stage -- `draft:spec` or
`draft:proposal` runs first, producing the `draft-spec` artifact; (2) validation sub-stage --
`review:design`, `review:users`, `prove:prototype` run after, each requiring the `draft-spec`
artifact as input (`review:design` reviews a specification; without a specification the review
has no object; `prove:prototype` explores the design the spec describes); (3) simulation sub-stage
-- `flow:*` and `trace:*` skills run last, each requiring review artifacts as precondition
(tracing a contract that has not been reviewed for correctness propagates unvalidated design
decisions into simulation output). Layer 2's handoff contract with Layer 3: synthesis skills may
not start until the validated-design context is present.

**Layer 3 (Synthesis) -- arc closure; requires the full validated context from Layers 1 and 2:**

Layer 3 produces the synthesis artifact set: adoption signals, feedback signals, topic artifacts
(story, report, status). Skills in this layer (`listen:adoption`, `listen:feedback`,
`topic:story`, `topic:report`) require the complete validated-design context from Layers 1 and 2
as their input. Running `listen:adoption` before validation synthesizes signals that have not been
validated; the synthesis output degrades accordingly. Running `topic:story` before all signals are
archived produces a narrative over a partial evidence set. Layer 3 has no downstream handoff
contract -- it is the final evidence-producing layer. Its gate marks the completion of the full
evidence arc: all prior signals archived, all prior artifacts present, no critical blockers.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate, or
synthesize. Adding skills to echo means running evidence work in a terminal stage with no
subsequent gate capable of certifying that evidence before the program closes. Echo is not a
spillover stage.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. `auto: true` is not a convenience flag -- it is an
architectural statement that the program's completion requires no human gate inspection here.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2), synthesis produced (Layer 3). Echo is the receipt of the completed program; the signal
archive is coherent and the topic's investigation is done.

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
and the Plan Verification table verbatim. For each zone, fill `gate:` with an artifact-state
condition; `gate_fail:` and `gate_pass:` are teaching examples only -- do not use their values
as your gate.**

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
      gate_fail: "Layer 1 complete"           # WRONG C-04: execution state -- not verifiable
      gate_pass: ">= 2 scout signals AND scout-feasibility artifact present"
                                              # Why: artifact name + count threshold -- inspectable
      gate: "<fill: name scout artifact(s) and numeric threshold>"

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
      gate_fail: "design done"                # WRONG C-04: execution state -- not verifiable
      gate_pass: "draft-spec artifact present"
                                              # Why: artifact reference -- inspectable in signal archive
      gate: "<fill: draft-spec artifact present>"

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate_fail: "validation complete"        # WRONG C-04: execution state -- not verifiable
      gate_pass: "review-design artifact present; 0 P0 findings open"
                                              # Why: artifact name + evidence threshold -- checkable
      gate: "<fill: review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate_fail: "simulation done"            # WRONG C-04: execution state -- not verifiable
      gate_pass: "flow-lifecycle and trace-contract artifacts present"
                                              # Why: artifact references -- inspectable
      gate: "<fill: flow/trace artifacts present>"

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-loop"
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate_fail: "synthesis done"             # WRONG C-04: execution state -- not verifiable
      gate_pass: "listen artifacts present; all prior signals archived; 0 critical blockers open"
                                              # Why: evidence state with quantified threshold -- verifiable
      gate: "<fill: listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

    - name: echo
      skills: []                              # REQUIRED: empty -- DO NOT add skills here
      auto: true                              # REQUIRED: must be present and true
```

## Plan Verification

| Property | Pass condition | Check |
|----------|---------------|-------|
| Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after | [ ] |
| Valid skills | All skill names from Signal's 9 namespaces; zero invented names | [ ] |
| Evidence gates (`gate:`) | Every non-echo `gate:` expresses artifact/evidence state -- not execution state | [ ] |
| Quantified gate | >= 1 non-echo `gate:` has numeric threshold | [ ] |
| Descriptive names | Stage names are phase labels, not namespace names, not indices | [ ] |
| Gate fields filled | All `gate:` fields replaced; `gate_fail:` and `gate_pass:` not used as actual gate | [ ] |
| Layer 1 comment | `# ---- Layer 1: Breadth ----` present in YAML | [ ] |
| Layer 2 comment | `# ---- Layer 2: Depth ----` with dependency annotation present | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved | [ ] |

---

## V-02 -- Correction Table with Full Recommended-Tier Coverage (single-axis: C-18/C-19/C-21/C-22/C-29)

**Axis**: Correction table with complete recommended-tier pairs. A 13-row wrong-to-correct table
covering C-02, C-03, C-04 (essential tier) and C-05, C-06, C-07 (all three recommended criteria)
is added as a dedicated section before the YAML template. Template fields carry navigational
bridges to the table (`# check correction table: skill names`, `# check correction table: stage
names`, `# check correction table: gates`) at every covered authoring position. All other elements
preserved from R7 V-05 base: same BAD YAML opening, same layer narration, same gate design table,
same skill catalog. Simple `gate:` placeholders (no three-field structure -- C-24/C-28 not added).

**Hypothesis**: A correction table with rows for C-05 (dependency-order errors), C-06
(namespace-label stage names), and C-07 (executor framing) passes C-18 (correction table >= 3
pairs), C-19 (cross-tier coverage: essential + recommended), C-22 (all three recommended criteria
in error artifacts), and C-29 (correction table specifically carries recommended-tier pairs).
Template bridges pass C-21 (scaffold integration). Expected delta: +5 aspirational criteria pass.

---

### Prompt body

```
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
simulates a lifecycle for a design that `review:design` has not yet validated. `listen:feedback`
synthesizes signals that have not been gathered or validated. `"done"` is unverifiable. The team
advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before advancing.
A plan without meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals Layer 2 requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Scout skills run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`). These produce the feasibility, requirements, market, and competitor artifacts
that Layer 2 depends on before any design skill can start. Layer 1 requires no prior signals; it
is the program entry point. Layer 1's output is Layer 2's required input; the gate between them
makes this dependency checkable.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts between design, validation, and simulation:**

Layer 2 produces the design, validation, and simulation artifact set. Sub-stage ordering: (1)
design sub-stage -- `draft:spec` or `draft:proposal` runs first, producing the `draft-spec`
artifact; (2) validation sub-stage -- `review:design`, `review:users`, `prove:prototype` run
after, each requiring the `draft-spec` artifact as input; (3) simulation sub-stage -- `flow:*`
and `trace:*` skills run last, each requiring review artifacts as precondition. Layer 2's handoff
contract with Layer 3: synthesis skills may not start until the validated-design context is
present.

**Layer 3 (Synthesis) -- arc closure; requires the full validated context from Layers 1 and 2:**

Layer 3 produces the synthesis artifact set. Skills in this layer (`listen:adoption`,
`listen:feedback`, `topic:story`, `topic:report`) require the complete validated-design context
from Layers 1 and 2. Running `listen:adoption` before validation synthesizes signals that have not
been validated. Running `topic:story` before all signals are archived produces a narrative over a
partial evidence set. Layer 3's gate marks the completion of the full evidence arc.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate, or
synthesize. Adding skills to echo means running evidence work with no subsequent gate capable of
certifying that evidence before the program closes. Echo is not a spillover stage.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. `auto: true` is an architectural statement, not a
convenience flag.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete. Echo is the receipt of the completed program; the signal
archive is coherent and the topic's investigation is done.

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

**Correction table -- look up wrong forms before authoring each field:**

| Wrong form | Correct form | Criterion |
|---|---|---|
| `analyze-results` | `prove:analysis` | C-03 |
| `research:competitors` | `scout:competitors` | C-03 |
| `flow:simulate` | `flow:lifecycle` or `flow:dataflow` | C-03 |
| `echo` with `skills: [topic:report]` | `echo` with `skills: []` and `auto: true` | C-02 |
| `gate: "done"` | `gate: "draft-spec artifact present"` | C-04 |
| `gate: "Layer 2 complete"` | `gate: ">= 3 scout signals AND scout-feasibility artifact present"` | C-04 |
| `gate: "proceed to synthesis"` | `gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"` | C-04 |
| `review:design` before `draft:spec` in same stage | `draft:spec` in Layer 2 Design; `review:design` in Layer 2 Validation | C-05 |
| `flow:lifecycle` in same stage as `draft:spec` | `flow:*` in Layer 2 Simulation, after Validation | C-05 |
| `name: "scout"` (namespace as stage name) | `name: "discovery"` or `name: "market-scan"` | C-06 |
| `name: "review"` (namespace as stage name) | `name: "validation"` or `name: "expert-review"` | C-06 |
| `strategy: "run all scout and draft skills then validate"` | `strategy: "does this feature require regulatory approval?"` (evidence question) | C-07 |
| `stages:` described as executed in sequence | `stages:` produce gates only; skills run standalone; program does not execute | C-07 |

---

**Produce the following output -- fill all `<...>` placeholders; check the correction table above
before authoring each skill name, stage name, and gate value; reproduce all REQUIRED comments
and the Plan Verification table verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
                                              # check correction table: stage names
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
                                              # check correction table: skill names
        - scout:<skill>
      gate: "<named scout artifacts present; numeric threshold: '>= N scout signals present'>"
                                              # check correction table: gates

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
                                              # check correction table: stage names
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
                                              # check correction table: skill names
      gate: "<draft-spec artifact present>"   # check correction table: gates

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
                                              # check correction table: stage names
      skills:
        - review:<skill>                      # design, users, customers, or code
                                              # check correction table: skill names
        - prove:<skill>
      gate: "<review/prove artifacts present; 0 P0 findings open>"
                                              # check correction table: gates

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
                                              # check correction table: stage names
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
                                              # check correction table: skill names
        - trace:<skill>
      gate: "<flow/trace artifacts present>"  # check correction table: gates

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-loop"
                                              # check correction table: stage names
      skills:
        - listen:<skill>                      # adoption, feedback, or support
                                              # check correction table: skill names
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"
                                              # check correction table: gates

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

    - name: echo
      skills: []                              # REQUIRED: empty -- DO NOT add skills here
      auto: true                              # REQUIRED: must be present and true
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
| Layer 2 comment | `# ---- Layer 2: Depth ----` with dependency annotation present | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved | [ ] |

---

## V-03 -- Dual-Position Dep Reminders with Independent Correction Bridge (single-axis: C-16/C-20/C-23/C-27/C-30)

**Axis**: Dependency constraint reminders at BOTH zone-header position AND `skills:` placeholder
line in each dependency-bearing zone, using uniform syntax throughout (C-23, C-27). Each `skills:`
line independently carries both the dep reminder (`# requires: <artifact> from Zone: <name>
(C-05)`) and the correction-table bridge (`# check correction table: skill names`) as separate
annotations (C-30). BAD YAML block gains `# WRONG C-XX` criterion tags on each wrong field (C-16).
A minimal correction table is added to enable C-21 (scaffold bridge prerequisite) and C-30.
Gate fields remain simple `gate:` placeholders (no three-field structure).

**Hypothesis**: Dual-position dep reminders in uniform syntax (C-23, C-27), independently present
at skills lines alongside correction bridges (C-30), plus criterion-tagged BAD YAML (C-16), plus
scaffold correction bridges (C-21) pass 5 criteria as a dep-constraint density cluster. The
correction table rows cover essential tier only (no recommended-tier pairs) -- C-29 deliberately
excluded to isolate C-30. Expected delta: +5 aspirational criteria pass. C-29 is left as a gap
to confirm independence from V-02's correction-table axis.

---

### Prompt body

```
# This is what a Signal investigation looks like when planned without an arc:

program:
  topic: "{{topic}}"
  stages:
    - name: "all-work"                    # WRONG C-06: namespace-label, not evidence-phase label
      skills:
        - scout:feasibility
        - draft:spec
        - review:design                   # WRONG C-05: review:design runs before draft:spec has produced the artifact it reviews
        - flow:lifecycle
        - trace:request
        - listen:feedback                 # WRONG C-05: listen runs before any signals have been gathered or validated
        - analyze-results                 # WRONG C-03: invented skill -- not in Signal catalog
      gate: "done"                        # WRONG C-04: execution state -- unverifiable by next phase owner
    - name: echo
      skills:
        - topic:report                    # WRONG C-02: echo must carry no skills
      auto: false                         # WRONG C-02: auto must be true
```

Six problems in one plan. `review:design` requires a `draft-spec` artifact that `draft:spec` has
not yet produced -- they share a flat stage with no ordering enforced. `listen:feedback` synthesizes
signals that have not been gathered or validated. `analyze-results` does not exist in Signal's
skill catalog. `"done"` is unverifiable: the next phase owner has no artifact to check. Echo
carries skills and `auto: false` -- both wrong. `"all-work"` groups skills by execution, not by
evidence phase.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before advancing.
A plan without meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals Layer 2 requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Scout skills run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`). These produce the feasibility, requirements, market, and competitor artifacts
that Layer 2 depends on before any design skill can start. Layer 1 requires no prior signals; it
is the program entry point. Layer 1's output is Layer 2's required input; the gate between them
makes this dependency checkable.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts between design, validation, and simulation:**

Layer 2 produces the design, validation, and simulation artifact set. Sub-stage ordering: (1)
design sub-stage -- `draft:spec` or `draft:proposal` runs first, producing the `draft-spec`
artifact; (2) validation sub-stage -- `review:design`, `review:users`, `prove:prototype` run
after, each requiring the `draft-spec` artifact as input; (3) simulation sub-stage -- `flow:*`
and `trace:*` skills run last, each requiring review artifacts as precondition. Layer 2's handoff
contract with Layer 3: synthesis skills may not start until the validated-design context is
present.

**Layer 3 (Synthesis) -- arc closure; requires the full validated context from Layers 1 and 2:**

Layer 3 produces the synthesis artifact set: adoption signals, feedback signals, topic artifacts
(story, report, status). Skills in this layer require the complete validated-design context from
Layers 1 and 2. Running synthesis skills before validation produces output over unvalidated
signals. Layer 3's gate marks the completion of the full evidence arc.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3. Adding skills to echo means running evidence work
with no subsequent gate capable of certifying that evidence before the program closes.

(2) **`auto: true` semantics** -- Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. `auto: true` is an architectural statement, not a
convenience flag.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete. Echo is the receipt of the completed program.

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

**Correction table -- look up wrong forms before authoring each field:**

| Wrong form | Correct form | Criterion |
|---|---|---|
| `analyze-results` | `prove:analysis` | C-03 |
| `research:competitors` | `scout:competitors` | C-03 |
| `flow:simulate` | `flow:lifecycle` or `flow:dataflow` | C-03 |
| `echo` with skills listed | `echo` with `skills: []` and `auto: true` | C-02 |
| `gate: "done"` | `gate: "draft-spec artifact present"` | C-04 |
| `gate: "Layer 2 complete"` | `gate: ">= 3 scout signals AND scout-feasibility artifact present"` | C-04 |
| `gate: "proceed to synthesis"` | `gate: "review-design artifact present; 0 P0 findings open"` | C-04 |

---

**Produce the following output -- fill all `<...>` placeholders; note dep reminders at each zone
header and skills line; reproduce all REQUIRED comments and the Plan Verification table verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----
  # (entry point -- Layer 1 has no upstream artifact dependency)

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
      skills:   # (no upstream dep for Layer 1 -- this is the program entry point)
                # check correction table: skill names
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<named scout artifacts present; numeric threshold: '>= N scout signals present'>"
                                              # check correction table: gates

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # requires: scout-feasibility artifact from Zone: Layer 1 Breadth (C-05)

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
      skills:   # requires: scout-feasibility artifact from Zone: Layer 1 Breadth (C-05)
                # check correction table: skill names
        - draft:<skill>                       # spec, proposal, or pitch
      gate: "<draft-spec artifact present>"   # check correction table: gates

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
      skills:   # requires: draft-spec artifact from Zone: Layer 2 Design (C-05)
                # check correction table: skill names
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"
                                              # check correction table: gates

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
      skills:   # requires: review-design artifact from Zone: Layer 2 Validation (C-05)
                # check correction table: skill names
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate: "<flow/trace artifacts present>"  # check correction table: gates

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----
  # requires: all Layer 2 artifacts from Zones: Layer 2 Validation, Layer 2 Simulation (C-05)

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-loop"
      skills:   # requires: all Layer 2 artifacts from Zones: Layer 2 (C-05)
                # check correction table: skill names
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"
                                              # check correction table: gates

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

    - name: echo
      skills: []                              # REQUIRED: empty -- DO NOT add skills here
      auto: true                              # REQUIRED: must be present and true
```

## Plan Verification

| Property | Pass condition | Check |
|----------|---------------|-------|
| Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after | [ ] |
| Valid skills | All skill names from Signal's 9 namespaces; zero invented names | [ ] |
| Evidence gates | Every non-echo gate names artifact or signal state -- not execution state | [ ] |
| Quantified gate | >= 1 non-echo gate has numeric threshold | [ ] |
| Descriptive names | Stage names are phase labels, not namespace names, not indices | [ ] |
| Dep reminders | Zone headers AND skills: lines carry dep reminders at all dep-bearing zones | [ ] |
| Layer 1 comment | `# ---- Layer 1: Breadth ----` present in YAML | [ ] |
| Layer 2 comment | `# ---- Layer 2: Depth ----` with dependency annotation present | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved | [ ] |

---

## V-04 -- Three-Field Gates + Full Correction Table (combo: C-28 + C-29)

**Axes**: V-01's three-field gate structure (C-24/C-25/C-26/C-28) combined with V-02's full
correction table covering recommended-tier pairs (C-18/C-19/C-22/C-29). Dep reminders at zone
headers only (not at skills: lines) -- C-23/C-30 deliberately excluded to test C-28 + C-29 in
isolation. Template carries correction bridges at gate fields only (not at skill-list positions) --
C-21 partially satisfied but not C-30.

**Hypothesis**: The three-field gate structure and the full correction table are additive without
structural tension. Both pass simultaneously. C-30 still fails because dep reminders are not at
skills: lines independently alongside correction bridges. C-27 fails (no skills-line reminders to
apply uniform syntax to). Expected: prior criteria + C-17/C-24/C-25/C-26/C-28 + C-18/C-19/C-22/
C-29 pass; C-20/C-21/C-23/C-27/C-30 still require V-05 treatment.

---

### Prompt body

```
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
has not yet produced. `flow:lifecycle` simulates a lifecycle for an unreviewed design.
`listen:feedback` synthesizes signals that have not been gathered or validated. `"done"` is
unverifiable. The team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before advancing.
A plan without meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1 (Breadth) -- dependency origin; produces the foundational signals Layer 2 requires:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Scout skills run here -- `scout:feasibility`, `scout:requirements`, `scout:market`,
`scout:competitors` -- along with early prove skills (`prove:websearch`, `prove:intelligence`,
`prove:hypothesis`). These produce the feasibility, requirements, market, and competitor artifacts
that Layer 2 depends on before any design skill can start. Layer 1 requires no prior signals; it
is the program entry point. Layer 1's output is Layer 2's required input.

**Layer 2 (Depth) -- artifact scope and internal handoff contracts between design, validation, and simulation:**

Layer 2 produces the design, validation, and simulation artifact set. Sub-stage ordering: (1)
design sub-stage -- `draft:spec` or `draft:proposal` runs first, producing the `draft-spec`
artifact; (2) validation sub-stage -- `review:design`, `review:users`, `prove:prototype` run
after, each requiring the `draft-spec` artifact as input; (3) simulation sub-stage -- `flow:*`
and `trace:*` skills run last, each requiring review artifacts as precondition. Layer 2's
handoff contract with Layer 3: synthesis skills may not start until the validated-design context
is present.

**Layer 3 (Synthesis) -- arc closure; requires the full validated context from Layers 1 and 2:**

Layer 3 produces the synthesis artifact set. Skills in this layer require the complete
validated-design context from Layers 1 and 2. Running synthesis before validation produces output
over unvalidated signals. Layer 3's gate marks the completion of the full evidence arc.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3. Adding skills to echo means running evidence work
with no subsequent gate capable of certifying that evidence before the program closes.

(2) **`auto: true` semantics** -- Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. `auto: true` is an architectural statement, not a
convenience flag.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete. Echo is the receipt of the completed program.

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

**Correction table -- consult before authoring skill names, stage names, and gate values:**

| Wrong form | Correct form | Criterion |
|---|---|---|
| `analyze-results` | `prove:analysis` | C-03 |
| `research:competitors` | `scout:competitors` | C-03 |
| `flow:simulate` | `flow:lifecycle` or `flow:dataflow` | C-03 |
| `echo` with skills listed | `echo` with `skills: []` and `auto: true` | C-02 |
| `gate: "done"` | `gate: "draft-spec artifact present"` | C-04 |
| `gate: "Layer 2 complete"` | `gate: ">= 3 scout signals AND scout-feasibility artifact present"` | C-04 |
| `gate: "proceed to synthesis"` | `gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"` | C-04 |
| `review:design` before `draft:spec` in same stage | `draft:spec` in Layer 2 Design; `review:design` in Layer 2 Validation | C-05 |
| `flow:lifecycle` in same stage as `draft:spec` | `flow:*` in Layer 2 Simulation, after Validation | C-05 |
| `name: "scout"` (namespace as stage name) | `name: "discovery"` or `name: "market-scan"` | C-06 |
| `name: "review"` (namespace as stage name) | `name: "validation"` or `name: "expert-review"` | C-06 |
| `strategy: "run all scout and draft skills then validate"` | `strategy: "does this feature require regulatory approval?"` (evidence question) | C-07 |
| `stages:` described as executed in sequence | `stages:` produce gates only; skills run standalone | C-07 |

---

**Produce the following output -- fill all `<...>` placeholders; for each zone, fill the `gate:`
field with an artifact-state condition (the `gate_fail:` and `gate_pass:` fields are teaching
examples only -- do not use their values as your gate); consult the correction table before
authoring each skill name, stage name, and gate value; reproduce all REQUIRED comments and the
Plan Verification table verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what evidence question does this program answer?>"

  stages:

  # ---- Layer 1: Breadth -- scout signals produced here; Layer 2 design requires them ----
  # draft:* may not start until Layer 1 scout signals are present

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
                                              # check correction table: stage names
      skills:
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # check correction table: skill names
      gate_fail: "Layer 1 complete"           # WRONG C-04: execution state -- unverifiable
      gate_pass: ">= 2 scout signals AND scout-feasibility artifact present"
                                              # Why: artifact name + count threshold -- inspectable
      gate: "<fill: name scout artifact(s) and numeric threshold>"
                                              # check correction table: gates

  # ---- Layer 2: Depth -- design produces draft-spec; validation requires it; flow/trace last ----
  # requires: scout-feasibility artifact from Zone: Layer 1 Breadth (C-05)
  # draft:* produced here | review:* requires draft-spec | flow:*/trace:* require review:*

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
                                              # check correction table: stage names
      skills:
        - draft:<skill>                       # spec, proposal, or pitch
                                              # check correction table: skill names
      gate_fail: "design done"                # WRONG C-04: execution state -- unverifiable
      gate_pass: "draft-spec artifact present"
                                              # Why: artifact reference -- inspectable
      gate: "<fill: draft-spec artifact present>"
                                              # check correction table: gates

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
                                              # check correction table: stage names
      skills:
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
                                              # check correction table: skill names
      gate_fail: "validation complete"        # WRONG C-04: execution state -- unverifiable
      gate_pass: "review-design artifact present; 0 P0 findings open"
                                              # Why: artifact name + evidence threshold -- checkable
      gate: "<fill: review/prove artifacts present; 0 P0 findings open>"
                                              # check correction table: gates

    - name: "<simulation-phase-or-remove>"    # optional; remove if flow/trace not needed
                                              # check correction table: stage names
      skills:
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
                                              # check correction table: skill names
      gate_fail: "simulation done"            # WRONG C-04: execution state -- unverifiable
      gate_pass: "flow-lifecycle and trace-contract artifacts present"
                                              # Why: artifact references -- inspectable
      gate: "<fill: flow/trace artifacts present>"
                                              # check correction table: gates

  # ---- Layer 3: Synthesis -- synthesizes across all prior signals; runs after all validation ----
  # requires: all Layer 2 artifacts from Zones: Layer 2 Validation, Layer 2 Simulation (C-05)

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-loop"
                                              # check correction table: stage names
      skills:
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
                                              # check correction table: skill names
      gate_fail: "synthesis done"             # WRONG C-04: execution state -- unverifiable
      gate_pass: "listen artifacts present; all prior signals archived; 0 critical blockers open"
                                              # Why: evidence state with quantified threshold
      gate: "<fill: listen artifacts present; all prior signals archived; no critical blockers>"
                                              # check correction table: gates

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills

    - name: echo
      skills: []                              # REQUIRED: empty -- DO NOT add skills here
      auto: true                              # REQUIRED: must be present and true
```

## Plan Verification

| Property | Pass condition | Check |
|----------|---------------|-------|
| Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after | [ ] |
| Valid skills | All skill names from Signal's 9 namespaces; zero invented names | [ ] |
| Evidence gates (`gate:`) | Every non-echo `gate:` expresses artifact/evidence state -- not execution state | [ ] |
| Quantified gate | >= 1 non-echo `gate:` has numeric threshold | [ ] |
| Descriptive names | Stage names are phase labels, not namespace names, not indices | [ ] |
| Gate fields filled | All `gate:` fields replaced; `gate_fail:` / `gate_pass:` not used as actual gate | [ ] |
| Layer 1 comment | `# ---- Layer 1: Breadth ----` present in YAML | [ ] |
| Layer 2 comment | `# ---- Layer 2: Depth ----` with dependency annotation present | [ ] |
| Layer 3 comment | `# ---- Layer 3: Synthesis ----` present in YAML | [ ] |
| Echo comment | `# ---- Final Stage: echo ----` with REQUIRED line present | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved | [ ] |
| REQUIRED (echo) | Echo `# REQUIRED: preserve this comment` line preserved | [ ] |

---

## V-05 -- Golden Synthesis (all 23 aspirational criteria)

**Axes**: All five new criteria (C-26/C-27/C-28/C-29/C-30) applied simultaneously on the richest
base. Three-field gate structure at every non-echo zone with `# WRONG C-04` criterion tag on
`gate_fail:` (C-24/C-26/C-28) and `# Why:` rationale on both `gate_fail:` and `gate_pass:`
(C-25). Full 13-row correction table covering C-02/C-03/C-04 (essential) and C-05/C-06/C-07
(all three recommended) (C-18/C-19/C-22/C-29). Uniform dep reminder syntax at BOTH zone-header
position AND `skills:` placeholder line across all dep-bearing zones (C-23/C-27). Each dep-bearing
`skills:` line carries dep reminder AND correction bridge independently (C-30). BAD YAML block
carries `# WRONG C-XX` criterion tags on each wrong field (C-16). Echo section enumerated with
named bold items (C-25 carried from earlier rounds). Richest layer narration with role-labeled
headers.

**Hypothesis**: All five new criteria pass simultaneously without structural tension. Each cluster
is additive: the three-field gate structure does not interfere with dep reminders; the correction
table does not interfere with gate contrast. The dual annotation at skills lines (dep reminder +
bridge) satisfies C-30 independently -- neither substitutes for the other. Expected: 23/23
aspirational = 115/115 pts, composite 205/205.

---

### Prompt body

```
# This is what a Signal investigation looks like when planned without an arc:

program:
  topic: "{{topic}}"
  stages:
    - name: "all-work"                    # WRONG C-06: namespace-label stage name, not evidence-phase label
      skills:
        - scout:feasibility
        - draft:spec
        - review:design                   # WRONG C-05: review:design requires draft-spec artifact -- must follow draft stage
        - flow:lifecycle
        - trace:request
        - listen:feedback                 # WRONG C-05: listen requires validated signals -- must follow review stage
        - analyze-results                 # WRONG C-03: invented skill -- not in Signal catalog
      gate: "done"                        # WRONG C-04: execution state -- next phase owner cannot verify
    - name: echo
      skills:
        - topic:report                    # WRONG C-02: echo must carry no skills
      auto: false                         # WRONG C-02: auto must be true
```

Seven problems in one plan. `review:design` requires a `draft-spec` artifact that `draft:spec`
has not yet produced -- they share a flat stage with no ordering enforced. `flow:lifecycle`
simulates a lifecycle for a design that `review:design` has not yet validated -- simulation
results are built on an unreviewed design. `listen:feedback` synthesizes signals that have not
been gathered or validated. `analyze-results` does not exist in Signal's skill catalog. `"done"`
is unverifiable: the next phase owner has no artifact to check, no threshold to compare against.
Echo carries skills and `auto: false` -- both wrong. The team advances on faith.

**`/program:plan` exists to replace this pattern.**

It is a plan, not an executor. Every skill listed in the plan still runs standalone -- the
program does not execute them, advance stages, or carry any automation authority. Its only
product is the gate: a shared, evidence-specific condition that must be true before the next phase
owner can advance the investigation. A plan without meaningful gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**The artifact dependency chain -- why stages are ordered:**

**Layer 1 (Breadth) -- dependency origin; all downstream stages require its signals as precondition:**

Layer 1 produces the foundational signal set that every downstream stage requires as precondition.
Artifact classes produced in Layer 1: feasibility signals, requirements signals, market signals,
competitor signals, compliance signals. Skills that produce these artifacts belong to the `scout`
namespace; early `prove` skills (`prove:websearch`, `prove:intelligence`, `prove:hypothesis`) may
also run here. Layer 1 requires no prior signals -- it is the program entry point. Layer 1's
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
as their input. Running `listen:adoption` before validation synthesizes signals that have not been
validated; the synthesis output degrades accordingly. Running `topic:story` before all signals are
archived produces a narrative over a partial evidence set. Layer 3 has no downstream handoff
contract -- it is the final evidence-producing layer. Its gate marks the completion of the full
evidence arc: all prior signals archived, all prior artifacts present, no critical blockers.

**Echo -- terminal arc closure:**

Echo is the final stage of every Signal program. Its architectural contract has three distinct
elements, each independently verifiable:

(1) **Skill-free contract** -- Echo carries no skills. By the time echo runs, all evidence
production has ended across Layers 1, 2, and 3 -- there is nothing left to gather, validate, or
synthesize. Adding skills to echo means running evidence work in a terminal stage with no
subsequent gate capable of certifying that evidence before the program closes; the result is
ungated evidence appended after all validation has finished. Echo is not a spillover stage for
skills that did not fit earlier layers. Its emptiness is intentional and architecturally required.

(2) **`auto: true` semantics** -- Echo does not wait for a human reviewer to inspect a gate
condition and advance the plan. Echo has no gate condition. When all prior stages have reached
their gates, echo closes automatically. The `auto: true` declaration is not a convenience flag --
it is an architectural statement that the program's completion requires no human gate inspection
at this stage. The arc closed at Layer 3's gate; echo merely records that closure.

(3) **Arc closure function** -- When echo closes, the program signals that the topic's full
breadth-depth-synthesis arc is complete: breadth signals gathered (Layer 1), design validated
(Layer 2), synthesis produced (Layer 3). Echo is the receipt of the completed program; the signal
archive is coherent, all artifacts are present, and the topic's investigation is done. The program
has no further work to do.

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

**Correction table -- consult before authoring each skill name, stage name, and gate value:**

| Wrong form | Correct form | Criterion |
|---|---|---|
| `analyze-results` | `prove:analysis` | C-03 |
| `research:competitors` | `scout:competitors` | C-03 |
| `flow:simulate` | `flow:lifecycle` or `flow:dataflow` | C-03 |
| `echo` with skills listed | `echo` with `skills: []` and `auto: true` | C-02 |
| `gate: "done"` | `gate: "draft-spec artifact present"` | C-04 |
| `gate: "Layer 2 complete"` | `gate: ">= 3 scout signals AND scout-feasibility artifact present"` | C-04 |
| `gate: "proceed to synthesis"` | `gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"` | C-04 |
| `review:design` before `draft:spec` in same stage | `draft:spec` in Layer 2 Design; `review:design` in Layer 2 Validation | C-05 |
| `flow:lifecycle` in same stage as `draft:spec` | `flow:*` in Layer 2 Simulation, after Validation | C-05 |
| `name: "scout"` (namespace as stage name) | `name: "discovery"` or `name: "market-scan"` | C-06 |
| `name: "review"` (namespace as stage name) | `name: "validation"` or `name: "expert-review"` | C-06 |
| `strategy: "run all scout and draft skills in sequence"` | `strategy: "does this feature require regulatory approval?"` (evidence question, not execution plan) | C-07 |
| `stages:` described as "executed in order" or "orchestrated" | `stages:` produce gates only; every skill runs standalone; program carries no automation authority | C-07 |

---

**Produce the following output -- fill all `<...>` placeholders; for each zone, fill `gate:` with
an artifact-state condition (`gate_fail:` and `gate_pass:` are teaching examples only); at each
`skills:` line, the dep reminder names the prerequisite and the correction bridge routes to the
lookup table -- both serve different purposes; reproduce all REQUIRED comments and the Plan
Verification table verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence evidence question this program answers -- not an execution plan>"

  stages:

  # ---- Zone 1: Layer 1 Breadth -- dependency origin; no prior artifact deps; produces scout signals ----
  # (entry point -- Layer 1 has no upstream artifact dependency)

    - name: "<breadth-phase-label>"           # e.g. "discovery", "market-scan"
                                              # check correction table: stage names
      skills:   # (no upstream dep for Layer 1 -- this is the program entry point)
                # check correction table: skill names
        - scout:<skill>                       # feasibility, market, requirements, competitors...
        - scout:<skill>                       # add/remove as topic warrants
      gate_fail: "Layer 1 complete"           # WRONG C-04: Why: execution state -- next phase owner cannot verify without asking who ran what
      gate_pass: ">= 2 scout signals AND scout-feasibility artifact present"
                                              # Why: artifact name + count threshold -- verifiable by inspecting signal archive
      gate: "<fill: name scout artifact(s) and numeric threshold; see gate_pass for correct form>"
                                              # check correction table: gates

  # ---- Zone 2: Layer 2 Design -- requires Zone 1 scout signals; produces draft-spec ----
  # requires: scout-feasibility artifact from Zone: Layer 1 Breadth (C-05)

    - name: "<design-phase-label>"            # e.g. "design", "proposal"
                                              # check correction table: stage names
      skills:   # requires: scout-feasibility artifact from Zone: Layer 1 Breadth (C-05)
                # check correction table: skill names
        - draft:<skill>                       # spec, proposal, or pitch
      gate_fail: "design done"                # WRONG C-04: Why: execution state -- cannot be verified by artifact inspection
      gate_pass: "draft-spec artifact present"
                                              # Why: artifact reference -- inspectable in signal archive
      gate: "<fill: draft-spec artifact present>"
                                              # check correction table: gates

  # ---- Zone 3: Layer 2 Validation -- requires Zone 2 draft-spec; produces review/prove artifacts ----
  # requires: draft-spec artifact from Zone: Layer 2 Design (C-05)

    - name: "<validation-phase-label>"        # e.g. "expert-review", "validation"
                                              # check correction table: stage names
      skills:   # requires: draft-spec artifact from Zone: Layer 2 Design (C-05)
                # check correction table: skill names
        - review:<skill>                      # design, users, customers, or code
        - prove:<skill>                       # prototype, analysis, interview...
      gate_fail: "validation complete"        # WRONG C-04: Why: execution state -- no artifact to inspect
      gate_pass: "review-design artifact present; 0 P0 findings open"
                                              # Why: artifact name + evidence threshold -- checkable without running skills
      gate: "<fill: review/prove artifacts present; 0 P0 findings open>"
                                              # check correction table: gates

  # ---- Zone 4: Layer 2 Simulation -- optional; requires Zone 3 review artifacts; flow/trace here ----
  # requires: review-design artifact from Zone: Layer 2 Validation (C-05)

    - name: "<simulation-phase-or-remove>"    # optional; remove entire zone if flow/trace not needed
                                              # check correction table: stage names
      skills:   # requires: review-design artifact from Zone: Layer 2 Validation (C-05)
                # check correction table: skill names
        - flow:<skill>                        # lifecycle, resilience, trigger...
        - trace:<skill>                       # component, contract, request...
      gate_fail: "simulation done"            # WRONG C-04: Why: execution state -- cannot be verified by artifact inspection
      gate_pass: "flow-lifecycle and trace-contract artifacts present"
                                              # Why: artifact references -- each present in signal archive
      gate: "<fill: flow/trace artifacts present>"
                                              # check correction table: gates

  # ---- Zone 5: Layer 3 Synthesis -- requires ALL prior zones; produces listen/topic artifacts ----
  # requires: all Layer 2 artifacts from Zones: Layer 2 Validation, Layer 2 Simulation (C-05)

    - name: "<synthesis-phase-label>"         # e.g. "synthesis", "feedback-loop"
                                              # check correction table: stage names
      skills:   # requires: all Layer 2 artifacts from Zones: Layer 2 Validation, Layer 2 Simulation (C-05)
                # check correction table: skill names
        - listen:<skill>                      # adoption, feedback, or support
        - topic:<skill>                       # plan, report, status, or story
      gate_fail: "synthesis done"             # WRONG C-04: Why: execution state -- no artifact to inspect
      gate_pass: "listen artifacts present; all prior signals archived; 0 critical blockers open"
                                              # Why: evidence state with quantified threshold -- verifiable in signal archive
      gate: "<fill: listen artifacts present; all prior signals archived; no critical blockers>"
                                              # check correction table: gates

  # ---- Final Stage: echo -- arc closure; auto:true; no skills ----
  # REQUIRED: preserve this comment -- echo closes the arc automatically; it carries no skills
  # REQUIRED: DO NOT add skills to echo. DO NOT move echo before other stages.

    - name: echo                              # REQUIRED: preserve this name
      skills: []                              # REQUIRED: empty -- all evidence production ends at Layer 3
      auto: true                              # REQUIRED: must be present and true -- echo closes automatically
```

## Plan Verification

| Property | Pass condition | Check |
|----------|---------------|-------|
| Echo final | Last stage: `name: echo`, `skills: []`, `auto: true`; nothing after | [ ] |
| Valid skills | All skill names from Signal's 9 namespaces; zero invented names | [ ] |
| Evidence gates (`gate:`) | Every non-echo `gate:` expresses artifact/evidence state -- not execution state | [ ] |
| Quantified gate | >= 1 non-echo `gate:` has numeric threshold | [ ] |
| Descriptive names | Stage names are phase labels, not namespace names, not indices | [ ] |
| Gate fields filled | All `gate:` fields replaced; `gate_fail:` / `gate_pass:` are teaching examples, not output | [ ] |
| Dep reminders | Zone headers AND skills: lines carry `# requires: <artifact> from Zone: <name> (C-05)` at all dep-bearing zones | [ ] |
| Correction bridges | skills: lines carry `# check correction table: skill names` independently of dep reminders | [ ] |
| Layer 1 comment | `# ---- Zone 1: Layer 1 Breadth ----` (or equivalent) present | [ ] |
| Layer 2 comment | `# ---- Zone 2: Layer 2 Design ----` with dep annotation present | [ ] |
| Layer 3 comment | `# ---- Zone 5: Layer 3 Synthesis ----` with dep annotation present | [ ] |
| Echo REQUIRED comments | All three `# REQUIRED:` lines at echo preserved | [ ] |
| REQUIRED (top) | Top `# REQUIRED: preserve this comment` line preserved | [ ] |

---

## Predicted Scores Under v8

| Variation | Axis | C-16 | C-17 | C-20/C-23 | C-24/C-26/C-28 | C-25 | C-18/C-29 | C-21/C-30 | C-27 | Aspirational | Score |
|-----------|------|------|------|-----------|----------------|------|-----------|-----------|------|-------------|-------|
| V-01 | Three-field gate structure | FAIL (no tags) | PASS (per-zone structural) | FAIL (no skills-line reminders) | PASS/PASS/PASS | PASS (Why: present) | FAIL (no table) | FAIL | FAIL | ~15-16/23 | ~140-150 |
| V-02 | Correction table + bridges | FAIL (no tags) | PARTIAL (central table) | FAIL (no skills-line reminders) | FAIL (no gate_fail keys) | FAIL | PASS/PASS | PARTIAL/FAIL | FAIL | ~15-16/23 | ~140-150 |
| V-03 | Dual dep reminders + tags | PASS (WRONG tags) | PARTIAL | PASS/PASS | FAIL | FAIL | PARTIAL (7 rows, essential only) | PARTIAL/FAIL | PASS | ~16-17/23 | ~150-160 |
| V-04 | C-28 + C-29 combo | FAIL | PASS | FAIL | PASS/PASS/PASS | PASS | PASS/PASS | PARTIAL | FAIL | ~18-19/23 | ~165-175 |
| V-05 | Golden synthesis | PASS | PASS | PASS/PASS | PASS/PASS/PASS | PASS | PASS/PASS | PASS/PASS | PASS | 23/23 | 205/205 |
```
