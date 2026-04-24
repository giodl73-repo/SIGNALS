---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 11
rubric: v27
total_pts: 100
golden_threshold: 80
new_criteria: C-33, C-34
---

# program-plan — R11 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v27 (C-01 through C-34, 27 aspirational criteria, formula:
`(essential_pass/4)*60 + (recommended_pass/3)*30 + (aspirational_pass/27)*10`).

**R10 retrospective under v27 rubric:**
- V-01 (Inertia Framing: Displacement as Structural Spine): 99.26 — C-33 FAIL, C-34 FAIL
- V-02 (Output Format: Evidence Debt Register): 100.00 — C-33 PASS, C-34 PASS
- V-03 through V-05: scored at v26; C-33/C-34 status unknown

**R11 target:** C-33 and C-34 are now mandatory locked features alongside C-28 through
C-32. Every variation must include:
- A tabular skill catalog with a domain-functional third column whose header uses the
  variation's framing vocabulary (C-33)
- At least one pre-printed checklist item phrased in the variation's domain metaphor,
  verifying a structural property (C-34)

**R10 axis coverage (reference):**

| R10 axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Inertia framing prominence | X | | | X | X |
| Output format: evidence debt register | | X | | | X |
| Lifecycle: phase boundary contracts | | | X | | X |
| Backward derivation from echo | | | | X | X |
| All R10 axes combined | | | | | X |

**R11 new axes (all carry C-28 through C-34 as baseline):**

| Axis | Description |
|------|-------------|
| Phrasing register: investigative case file | Plan reads as an investigative brief. Skills gather evidence. Stages are investigative phases. Gates are case-strength conditions. C-33: "Evidence category gathered". C-34: case-file vocabulary in checklist. |
| Output format: confidence calibration register | Primary metaphor is uncertainty reduction. Each stage calibrates confidence in a named dimension. Gates are minimum calibration thresholds. C-33: "Uncertainty dimension addressed". |
| Lifecycle emphasis: readiness ladder | Gate transitions get dominant space. Each gate is a rung-clearance condition. Layer narrations are gate-dominant. C-33: "Readiness dimension cleared". |
| Combined: role sequence + inertia (architectural blueprint) | Skills ordered as construction phases with explicit dependency rationale. Inertia woven at three structural sites. C-33: "Structural dependency cleared". |
| All R11 axes combined: navigation chart | Second-person tone + waypoint-dominant lifecycle + inertia woven throughout + explicit role sequence rationale. C-33: "Navigation waypoint cleared". |

**R11 variation lineup:**

- V-01 (single): Phrasing register — investigative case file as organizing metaphor
- V-02 (single): Output format — confidence calibration register as primary structure
- V-03 (single): Lifecycle emphasis — readiness ladder with gate-dominant space
- V-04 (combined): Role sequence + inertia framing — architectural blueprint
- V-05 (combined): All R11 axes — navigation chart, second-person, inertia woven, waypoints dominant

---

## V-01 — Phrasing Register: Investigative Case File

**Axis:** Phrasing register — the plan reads as an investigative brief. Each skill
gathers a named category of evidence. Stages are investigative phases. Gate conditions
are case-strength conditions specifying what evidence the case file must hold before the
investigation advances. The not-executor identity is expressed as "this case file organizes
evidence collection; it does not conduct the investigation." The skill catalog's third
column names the evidence category each skill gathers, making the catalog a functional
field guide. Layer narrations use investigation vocabulary throughout: "gathering," "case
strength," "open leads," "case close."

**Hypothesis:** The investigative register gives C-34 a natural anchor — the case-file
metaphor makes "organizes collection but does not conduct" immediately vivid. C-33 lands
cleanly: "Evidence category gathered" is domain vocabulary that makes the skill catalog
actionable as a field guide. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

The week before the feature sprint began, a product manager drafted an investigation brief
for `{{topic}}`. At the planning meeting she said: "Three phases — gather context, design
and validate, then prepare for launch." The tech lead asked what evidence the team would
need before advancing from phase one to phase two. The PM said: "The usual stuff. We'll
know it when we have it." Nobody wrote it down. The brief was approved. Six weeks later,
the design review surfaced market signals that contradicted the spec — signals that had
been sitting in unanswered scout questions since week one. The team reworked the spec. The
brief had never specified what evidence the investigation required.

Here is the investigation brief that meeting produced for **{{topic}}**:

```yaml
# BAD — the brief with no case-strength conditions:
stages:
  - name: context-gathering
    skills: [scout:market, draft:spec]
    gate: "done"
  - name: design-and-validate
    skills: [review:design, prove:prototype, flow:lifecycle]
    gate: "complete"
  - name: launch-prep
    skills: [listen:adoption, topic:status]
    gate: "ready"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the brief it produced.

The brief failed at the gate level: "done" is an execution state, not a case-strength
condition. It co-located `draft:spec` with `scout:market` in phase one — the spec was
written while market evidence was still being gathered, meaning the investigation wrote
conclusions before examining evidence. `flow:lifecycle` was grouped with `review:design`
before a spec existed to simulate. "Ready" names how the team felt, not what evidence the
case file holds.

`/program:plan` is not an executor. It produces an investigation plan — a structured brief
with named investigative phases, ordered evidence-gathering operations, and gate conditions
specifying what evidence the case file must hold before advancing. The plan does not
conduct the investigation. Each skill runs standalone. The program is optional scaffolding
for the investigator.

---

**Before you build the investigation plan, read these three tables.**

---

**Table 1 — Evidence arc: investigative phases, layers, arc role, and evidence handoff**

| Phase | Layer | Arc role | Namespaces | Evidence handed to next phase |
|-------|-------|----------|------------|-------------------------------|
| Broad scan | Layer 1 (Breadth) | Case origin — produces scout artifacts Layer 2 requires | scout | market, feasibility, stakeholder, compliance, competitor signal artifacts |
| Deep investigation | Layer 2 (Depth) | Receives Layer 1 scout artifacts; produces validated artifacts Layer 3 synthesizes | draft, prove, review, flow, trace | spec, prototype, design-review, flow-simulation, trace artifacts |
| Case close | Layer 3 (Synthesis) | Requires the full review-validated evidence context from prior phases | listen, topic | adoption-readiness, synthesis, and topic-status artifacts |
| Terminal | Echo | Auto-closing; no new evidence gathering | — | — |

---

**Table 2 — Gate design: BAD case gates, why they fail, GOOD case-strength conditions**

At the planning meeting, nobody answered "what evidence do we need before advancing?" Here
is the table the team was declining to build:

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"done"` | Execution state — names when people stopped, not what evidence the case file holds | `"[scout artifact-types present] and [case-strength condition — >=2 scout signals, no open P0 gaps]"` |
| `"complete"` | Circular — restates that the phase ran; no case evidence condition named | `"[draft-spec and prototype artifact-types present] and [case-strength condition — no open P0 questions, hypothesis passes]"` |
| `"review complete"` | Execution state — names when reviewers finished, not what the case file shows they found | `"[review-design artifact present] and [case-strength condition — <=2 open findings, no blocking issues]"` |
| `"ready"` | Subjective — unverifiable; names team sentiment, not evidence state | `"[listen-adoption signal present] and [case-strength condition — >=3 persona evaluations, adoption rate >=N%]"` |
| `""` (empty) | Absent condition — no case-strength threshold; nothing can be verified | `"[topic-status artifact present] and [case-strength condition — topic declares ready, no unresolved signals]"` |

---

**Table 3 — Signal skill catalog by namespace and evidence category**

| Namespace | Skills | Evidence category gathered |
|-----------|--------|---------------------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | Foundational context evidence (market shape, feasibility envelope, stakeholder positions, compliance constraints) |
| draft | spec, proposal, pitch, brainstorm | Specification and design intent evidence |
| review | design, code, users, customers | Design and implementation quality evidence |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | Assumption validation evidence |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | Behavioral simulation evidence |
| trace | request, state, contract, component, deployment, migration, permissions | Structural contract and boundary evidence |
| listen | feedback, support, adoption | Adoption signal and readiness evidence |
| topic | new, plan, story, status, report, echo | Narrative synthesis and arc-closure evidence |

Namespace investigation order: `scout → draft → review/prove → flow/trace → listen → topic`.
An investigator who opens `draft:spec` while scout-phase evidence is still being gathered
is writing conclusions before examining the case file — exactly what the bad brief did.

---

**Layer 1 (Breadth) — Case origin: gathers the foundational evidence that Layer 2's investigation requires:**

Layer 1 runs the broad-scan phase — open-field evidence gathering that precedes any
hypothesis-specific work. Scout-namespace skills produce the raw signals: market shape,
technical feasibility, stakeholder positions, competitive context, compliance constraints.
These are not produced by any prior phase; they are the entry conditions that make Layer
2's targeted investigation possible. The bad brief placed `draft:spec` inside this phase —
the case file writer was generating conclusions (the spec) while the field investigators
(scout skills) were still gathering the evidence those conclusions would depend on. Layer
1 produces scout signal artifacts and nothing else. Its gate is a case-strength condition:
named scout artifact types must be present and the evidence quality must clear a numeric
threshold before the investigation advances to deep examination.

**Layer 2 (Depth) — Deep investigation: receives Layer 1 scout artifacts; produces the validated evidence set that Layer 3 synthesis requires:**

Layer 2 conducts the targeted investigation that Layer 1's broad scan made possible.
Draft-namespace skills produce the spec and prototype — the working hypotheses of the
investigation. Review-namespace skills test those hypotheses against quality criteria.
Flow- and trace-namespace skills simulate behavioral and structural evidence, testing
whether the spec's claims hold under realistic runtime paths. Each skill in Layer 2 depends
on evidence that a prior Layer 2 skill or Layer 1 produced: `review:design` cannot evaluate
a design `draft:spec` has not produced; `flow:lifecycle` cannot simulate a lifecycle the
spec has not defined. Layer 2 requires Layer 1 scout evidence at entry — the spec author
needs market signals, feasibility bounds, and stakeholder positions that only Layer 1 can
supply. Layer 2's gates are case-strength conditions on the validated artifact set: spec
present with no open P0 questions; design review found <=N issues; flow simulation has no
blocking gaps.

**Layer 3 (Synthesis) — Case close: requires the full review-validated evidence context from prior phases to produce a defensible readiness finding:**

Layer 3 closes the investigation. Listen-namespace skills gather adoption signals and
support patterns — but only meaningful ones if the design has been validated. A case that
tries to assess adoption readiness before design review is closed is gathering witness
testimony before the forensic evidence is in. Topic-namespace skills synthesize the full
evidence record into a narrative and a readiness declaration. `topic:status` cannot produce
a defensible readiness finding if any prior phase produced unresolved P0 signals — the
case is not ready to close if material questions remain open. Layer 3 requires the complete
validated evidence set from Layers 1 and 2. Its gate is a final case-strength condition:
named synthesis artifacts present, topic can declare readiness, no unresolved signals
remain in the evidence record.

**The echo stage — why it is always last and always auto:**

1. **Echo carries no investigation skills because the case is closed.** Echo does not
   gather new evidence or re-open questions. If the investigation arc was designed
   correctly, every open lead was followed and closed in Layers 1–3. Adding skills to echo
   means the investigation was not complete — fix a prior gate's case-strength condition,
   not echo.
2. **`auto: true` means echo closes without a case-strength gate.** Echo does not wait for
   an investigator to review the findings and declare the case closed. When the prior
   stage's gate passes, echo closes automatically. Its function is retrospective: what did
   the investigation reveal that the original brief did not anticipate?
3. **Echo signals case closure.** When echo closes, the case file is sealed. Every
   evidence category was gathered, every gate was cleared, every open lead was resolved at
   or below its threshold. The topic has a complete investigation record. The case is
   closed — not because the team felt ready, but because the evidence arc is complete.

---

Build the investigation plan for **{{topic}}** using the template below. Fill in all
bracketed fields. Preserve all YAML comments — they are structural anchors in the brief.

```yaml
# REQUIRED PRESERVE: this program is an investigation plan, not an investigator.
# It organizes evidence collection; it does not conduct it. Each skill runs standalone.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Breadth ---- | scout:* gathers foundational evidence | draft:* requires Layer 1 case file populated ----
    - name: "[broad-scan phase label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills appropriate to the investigation of {{topic}}
      gate: "[scout artifact-types present] and [case-strength condition — >=N scout signals, no open P0 gaps]"

    # ---- Layer 1 → Layer 2 boundary: scout evidence gathered → deep investigation opens ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* produced here | requires Layer 1 evidence | produces validated set Layer 3 requires ----
    - name: "[design/hypothesis phase label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills appropriate to {{topic}}
      gate: "[draft/prove artifact-types present] and [case-strength condition — no open P0 questions, <=N open findings]"

    - name: "[validation phase label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills appropriate to {{topic}}
      gate: "[review/flow/trace artifact-types present] and [case-strength condition — <=N open findings, no blocking simulation gaps]"

    # ---- Layer 2 → Layer 3 boundary: validated evidence gathered → case-close phase opens ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* close the case | requires full validated evidence from Layers 1+2 ----
    - name: "[case-close phase label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills appropriate to {{topic}}
      gate: "[listen/topic artifact-types present] and [case-strength condition — >=N readiness signals, topic declares ready, no unresolved leads]"

    # ---- Terminal ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; case file seals when prior gate passes

## Investigation Plan Verification
# [ ] YAML parses; every stage has name, skills, and gate fields
# [ ] Last stage is echo with skills: [] and auto: true; no stages follow it
# [ ] Every skill belongs to Signal's 9 namespaces; no invented skill names
# [ ] Every non-echo gate names an artifact type and a case-strength condition — not "done", "complete", or empty
# [ ] Scout skills appear before draft; draft before review/prove; review/prove before listen/topic
# [ ] Stage names are descriptive investigative phase labels, not "stage1" or skill name repeats
# [ ] At least one gate carries a numeric threshold (>=N or <=N)
# [ ] This case file organizes evidence collection; it does not conduct the investigation — each skill runs standalone
```

---

## V-02 — Output Format: Confidence Calibration Register

**Axis:** Output format — the primary structural metaphor is confidence calibration. Each
stage reduces uncertainty in a named dimension. The evidence arc table adds a "calibration
target" column. Gate placeholders are calibration thresholds: `"[artifact-types present]
and [calibration condition — uncertainty in [dimension] <=N open questions]"`. Layer
narrations describe what uncertainty each layer addresses and what calibration it enables
in the next. The meeting narrative shows a plan that declared confidence without
calibrating it. The skill catalog's third column names the uncertainty dimension each skill
addresses, making the catalog a calibration map. The checklist item: "This plan calibrates
confidence; it does not achieve it."

**Hypothesis:** The calibration register makes C-09 (quantified gate) structurally
inevitable — a confidence threshold is inherently numeric. C-04 (non-trivial gates)
becomes: "done" does not calibrate any uncertainty dimension; it declares confidence
without evidence. C-17 (dependency narration) becomes: Layer 2 cannot calibrate design
uncertainty until Layer 1 has calibrated foundational uncertainty. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

The day the feature brief was circulated for `{{topic}}`, the VP of Product said: "I think
we're confident enough to proceed." When the principal engineer asked what uncertainty the
team had actually addressed before that claim, the PM said: "The usual stuff — we've been
thinking about this for a while." Nobody named an uncertainty dimension. Nobody set a
confidence threshold. The brief was approved. Two sprints later, a stakeholder review
revealed that the team had built a spec against a market assumption that had never been
validated. The confidence claim had been asserted, not calibrated.

Here is the plan that emerged from that session for **{{topic}}**:

```yaml
# BAD — the asserted-confidence plan:
stages:
  - name: research
    skills: [scout:market, scout:stakeholders, draft:spec]
    gate: "confident enough"
  - name: design-and-test
    skills: [review:design, prove:prototype, trace:state]
    gate: "validated"
  - name: readiness
    skills: [listen:adoption, topic:status]
    gate: "ready to launch"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

"Confident enough" names a feeling, not a calibrated state. It co-located `draft:spec`
with `scout:market` — the spec was drafted while market uncertainty was still uncalibrated,
producing a design built on unexamined assumptions. "Validated" is execution state: it
names when reviewers stopped, not which uncertainty dimensions their review addressed.
"Ready to launch" is an outcome assertion, not a pre-condition. No uncertainty dimension
was named; no confidence threshold was defined.

`/program:plan` is not an executor. It produces a calibration plan — a structured program
that reduces uncertainty in named dimensions through an ordered sequence of evidence-
gathering operations, with gates specifying what confidence level must be achieved in each
dimension before advancing. The plan does not achieve confidence. Each skill runs
standalone. The program is optional scaffolding.

---

**Before you build the calibration plan, read these three tables.**

---

**Table 1 — Evidence arc: calibration layers, uncertainty addressed, and confidence handoff**

| Layer | Arc name | Uncertainty dimension addressed | Namespaces | Confidence handed to next layer |
|-------|----------|---------------------------------|------------|---------------------------------|
| Layer 1 (Breadth) | Foundational calibration | Foundational uncertainty (market, feasibility, stakeholders, compliance) | scout | Calibrated foundational context that Layer 2 requires to reduce design uncertainty |
| Layer 2 (Depth) | Design calibration — receives Layer 1 calibrated context; reduces design uncertainty Layer 3 requires | Design, behavior, contract uncertainty | draft, prove, review, flow, trace | Validated design artifacts with bounded uncertainty that Layer 3 uses to calibrate readiness |
| Layer 3 (Synthesis) | Readiness calibration — requires the full calibrated artifact context from prior layers | Adoption, readiness, narrative uncertainty | listen, topic | Readiness declaration with explicit confidence level |
| Terminal | Echo | None — calibration complete | — | — |

---

**Table 2 — Gate design: BAD asserted-confidence gates, why they fail, GOOD calibration gates**

When the VP said "confident enough," here is the table the team was declining to produce:

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"confident enough"` | Asserted — names team sentiment; no uncertainty dimension or threshold named | `"[scout artifact-types present] and [calibration condition — market uncertainty <=N open questions, feasibility calibrated at >=80%]"` |
| `"validated"` | Execution state — names when validation ran, not what uncertainty it reduced | `"[draft-spec and prototype artifact-types present] and [calibration condition — design uncertainty <=N open questions, prototype hypothesis passes]"` |
| `"ready to launch"` | Outcome assertion — names a downstream result, not an upstream evidence condition | `"[listen-adoption signal present] and [calibration condition — adoption uncertainty <=N open questions, >=3 persona confidence signals]"` |
| `"all done"` | Circular — no dimension or threshold; restates that stages ran | `"[review-design artifact present] and [calibration condition — design-quality uncertainty <=2 open findings, no blocking issues]"` |
| `""` (empty) | Absent — no calibration condition to check | `"[topic-status artifact present] and [calibration condition — total remaining uncertainty <=N, topic declares confidence reached]"` |

---

**Table 3 — Signal skill catalog by namespace and uncertainty dimension**

| Namespace | Skills | Uncertainty dimension addressed |
|-----------|--------|----------------------------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | Foundational uncertainty (market viability, technical limits, stakeholder alignment, constraints) |
| draft | spec, proposal, pitch, brainstorm | Specification uncertainty (what the feature should be and how it should work) |
| review | design, code, users, customers | Design-quality uncertainty (whether the design is sound and implementable) |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | Assumption uncertainty (whether key claims are empirically supportable) |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | Behavioral uncertainty (how the feature behaves under realistic conditions) |
| trace | request, state, contract, component, deployment, migration, permissions | Structural uncertainty (whether contracts, state machines, and boundaries are sound) |
| listen | feedback, support, adoption | Adoption uncertainty (whether users will adopt and support can handle load) |
| topic | new, plan, story, status, report, echo | Narrative uncertainty (whether the story is coherent and readiness is defensible) |

Calibration order: `scout → draft → review/prove → flow/trace → listen → topic`. Layer 2
cannot calibrate design uncertainty until Layer 1 has calibrated foundational uncertainty.
A spec drafted while market uncertainty is unaddressed is calibrating in the wrong order —
the VP's "confident enough" was built on exactly that misordering.

---

**Layer 1 (Breadth) — Foundational calibration: reduces the uncertainty that Layer 2 requires to be addressed before design work begins:**

Layer 1 calibrates the pre-conditions of design: is this technically feasible? What does
the market require? What do stakeholders expect? Are there compliance constraints that
bound the design space? These uncertainty dimensions are not reducible by design or
validation work — they require direct evidence gathering via scout-namespace skills. Layer
1 runs only scout-namespace skills. Its gate is a calibration threshold: named scout
artifacts must be present and the residual uncertainty in each foundational dimension must
fall at or below a named level before Layer 2 begins design work. A design that proceeds
before foundational calibration is complete inherits the full uncertainty it was supposed
to reduce — which is precisely what produced the market-assumption failure in the meeting
scenario above.

**Layer 2 (Depth) — Design calibration: receives Layer 1 calibrated context; reduces design, behavior, and contract uncertainty that Layer 3 requires to calibrate readiness:**

Layer 2 calibrates three uncertainty families in dependency order. Design uncertainty is
addressed first (draft, prove): `draft:spec` produces the specification that makes design-
quality calibration possible; `prove:prototype` reduces assumption uncertainty by building
and testing the working model. Design-quality uncertainty is addressed next (review):
`review:design` cannot calibrate design quality until `draft:spec` has produced a design
to evaluate. Behavioral and structural uncertainty are addressed last (flow, trace): these
skills cannot run meaningfully until a spec and validated design exist to simulate and
trace. Layer 2 requires Layer 1's calibrated foundational context at entry — designing
without it is drafting into an unaddressed uncertainty space. Layer 2 gates name the
residual uncertainty ceiling for each family: <=N open findings, no P0 uncertainty
blockers, prototype hypothesis confirmed.

**Layer 3 (Synthesis) — Readiness calibration: requires the full calibrated artifact context from prior layers to produce a defensible confidence claim:**

Layer 3 calibrates the final uncertainty families: adoption (listen skills) and narrative
(topic skills). Adoption uncertainty cannot be meaningfully addressed if design-quality
uncertainty from Layer 2 is still open — calibrating adoption against an unvalidated
design produces a false confidence signal. Narrative uncertainty cannot be resolved if any
prior dimension has residual P0 uncertainty — a story built on unaddressed foundational
gaps is not defensible. Layer 3 requires the complete calibrated artifact set from Layers
1 and 2. Its gate is a confidence declaration: readiness artifacts exist, named uncertainty
dimensions are below threshold, and the topic can make a confidence claim without
qualification.

**The echo stage — why it is always last and always auto:**

1. **Echo carries no calibration skills because all uncertainty dimensions have been
   addressed.** Echo does not run evidence-gathering operations. If any dimension has
   residual P0 uncertainty when echo is reached, the arc was designed incorrectly — fix a
   prior gate's calibration threshold, not echo.
2. **`auto: true` means echo closes without a confidence gate.** Echo does not wait for a
   reviewer to declare the confidence level sufficient. When the prior stage's calibration
   gate passes, echo fires automatically. Its question is retrospective: what uncertainty
   emerged during calibration that the original plan did not anticipate?
3. **Echo signals total calibration.** When echo closes, every named uncertainty dimension
   has been addressed at or below its threshold. The topic has a complete calibration
   record. The program is done — not because someone asserted confidence, but because
   every dimension has been measured and bounded.

---

Build the calibration plan for **{{topic}}** using the template below. Fill in all
bracketed fields. Preserve all YAML comments.

```yaml
# REQUIRED PRESERVE: this program is a calibration plan, not a calibrator.
# It sequences uncertainty reduction; it does not achieve confidence. Each skill runs standalone.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Breadth ---- | scout:* calibrates foundational uncertainty | draft:* requires Layer 1 calibration complete ----
    - name: "[foundational calibration phase label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills that address foundational uncertainty for {{topic}}
      gate: "[scout artifact-types present] and [calibration condition — foundational uncertainty <=N open questions, no P0 market or feasibility gaps]"

    # ---- Layer 1 → Layer 2 boundary: foundational uncertainty calibrated → design calibration opens ----

    # ---- Layer 2: Depth ---- | draft:*/prove:*/review:*/flow:*/trace:* calibrate design uncertainty | requires Layer 1 | produces calibrated set Layer 3 requires ----
    - name: "[design calibration phase label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills for {{topic}}
      gate: "[draft/prove artifact-types present] and [calibration condition — specification uncertainty <=N open questions, prototype hypothesis passes]"

    - name: "[validation calibration phase label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills for {{topic}}
      gate: "[review/flow/trace artifact-types present] and [calibration condition — design-quality uncertainty <=N open findings, no P0 behavioral gaps]"

    # ---- Layer 2 → Layer 3 boundary: design uncertainty calibrated → readiness calibration opens ----

    # ---- Layer 3: Synthesis ---- | listen:*/topic:* calibrate readiness | requires full calibrated artifact context from Layers 1+2 ----
    - name: "[readiness calibration phase label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills for {{topic}}
      gate: "[listen/topic artifact-types present] and [calibration condition — adoption uncertainty <=N open questions, topic confidence declared, no unresolved dimensions]"

    # ---- Terminal ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; calibration arc closes when prior gate passes

## Calibration Plan Verification
# [ ] YAML parses; every stage has name, skills, and gate fields
# [ ] Last stage is echo with skills: [] and auto: true; no stages follow it
# [ ] Every skill belongs to Signal's 9 namespaces; no invented skill names
# [ ] Every non-echo gate names an artifact type and a calibration threshold — not "confident enough" or "validated"
# [ ] Scout skills appear before draft; draft before review/prove; review/prove before listen/topic
# [ ] Stage names reflect the uncertainty dimension being calibrated, not generic labels
# [ ] At least one gate carries a numeric threshold (>=N or <=N)
# [ ] This plan calibrates confidence; it does not achieve it — each skill runs standalone
```

---

## V-03 — Lifecycle Emphasis: Readiness Ladder

**Axis:** Lifecycle emphasis — gate transitions get dominant space. Each gate is a
"readiness rung" on an evidence ladder. Layer narrations are organized around what each
rung requires to be cleared and what clearing it unlocks. The arc table includes a "rung-
clearance requirement" column. The YAML template labels boundary transitions as rung
transitions. The not-executor identity: "this plan defines the rungs; it does not climb
them." The skill catalog's third column names the readiness dimension each skill
contributes to, making the catalog a rung-clearance map. Layer narrations are gate-
dominant: each paragraph centers on what must be true to step from this rung to the next.

**Hypothesis:** The readiness ladder makes C-04 structurally prominent — each gate is
literally a rung description, and "done" is not a rung. C-21/C-25 (echo narration) maps
naturally: echo is the top of the ladder — you are not still climbing. C-30 (composite
gate) is the rung's two-part structure: presence of artifacts (step onto the rung) and
quality threshold (clear the rung). Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

At the kickoff meeting for `{{topic}}`, the engineering manager shared a four-stage plan.
When the QA lead asked what the team needed to clear each stage transition, the manager
said: "Each stage is done when the team feels like the work is done. We move on when
we're ready." The PM added: "We'll know when to move." Nobody defined what "ready" meant
at any stage boundary. The plan was shared. Three stages completed. The synthesis stage
ran before the design review had produced findings. The team had stepped to the next rung
before the prior rung had been cleared.

Here is the plan that kickoff produced for **{{topic}}**:

```yaml
# BAD — no rungs, just feelings:
stages:
  - name: discovery
    skills: [scout:market, scout:feasibility, draft:spec]
    gate: "done when team is ready"
  - name: design
    skills: [review:design, prove:prototype]
    gate: "done"
  - name: validation
    skills: [flow:lifecycle, trace:state, listen:adoption]
    gate: "complete"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the plan it produces.

"Done when team is ready" is not a rung — it is a declaration that no rung exists. The
plan placed `draft:spec` on the same rung as `scout:market`: the team stepped from
discovery to design before market evidence existed to inform the spec. `listen:adoption`
was placed in the validation rung alongside `flow:lifecycle` and `trace:state` — but
adoption readiness cannot be assessed before a validated design exists. No rung had a
clearance condition. The team climbed without a ladder.

`/program:plan` is not an executor. It builds a readiness ladder — a structured sequence
of rungs, each with a clearance condition specifying what evidence must exist before the
investigation steps to the next level. The plan defines the rungs; it does not climb them.
Each skill runs standalone. The program is optional scaffolding.

---

**Before you build the readiness ladder, read these three tables.**

---

**Table 1 — Evidence arc: ladder levels, rung-clearance requirements, and handoff**

| Level | Layer | Rung-clearance requirement | Namespaces | Clears for next level |
|-------|-------|---------------------------|------------|-----------------------|
| Rung 1: Ground level | Layer 1 (Breadth) | Scout artifacts present; foundational unknowns answered to threshold | scout | Enables Layer 2 to begin design on a cleared foundation |
| Rung 2: Design level | Layer 2 (Depth) — clears Rung 2 using Layer 1 foundation; produces validated artifacts Rung 3 requires | Spec + prototype artifacts present; design-quality threshold cleared | draft, prove, review, flow, trace | Enables Layer 3 synthesis on a validated artifact base |
| Rung 3: Synthesis level | Layer 3 (Synthesis) — requires full validated artifact set from prior rungs to clear readiness threshold | Readiness artifacts present; full arc complete at threshold | listen, topic | Clears the arc; echo can close |
| Top of ladder | Echo | No rung to clear — the ladder is climbed | — | — |

---

**Table 2 — Gate design: BAD un-runged gates, why they fail, GOOD rung-clearance conditions**

The kickoff manager said "we'll know when to move." Here is the rung-clearance table the
team was declining to build:

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"done when team is ready"` | Sentiment — names when the team decides to move, not what the rung requires to be cleared | `"[scout artifact-types present] and [rung-clearance condition — >=2 scout signals present, no open P0 foundational questions]"` |
| `"done"` | Execution state — the rung was not cleared; it was abandoned | `"[draft-spec and prototype artifact-types present] and [rung-clearance condition — no open P0 spec questions, prototype hypothesis passes]"` |
| `"complete"` | Circular — restates that the stage ran; the rung has no clearance condition | `"[review/flow/trace artifact-types present] and [rung-clearance condition — <=2 open findings, no blocking simulation gaps]"` |
| `"good enough"` | Subjective — no rung definition, no clearance threshold | `"[listen-adoption signal present] and [rung-clearance condition — >=3 persona evaluations, adoption rate >=N%]"` |
| `""` (empty) | Absent — the rung does not exist; climbing it cannot be verified | `"[topic-status artifact present] and [rung-clearance condition — topic declares ready, no unresolved signals remain]"` |

---

**Table 3 — Signal skill catalog by namespace and readiness dimension**

| Namespace | Skills | Readiness dimension cleared |
|-----------|--------|------------------------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | Foundational readiness (is the design space defined? are constraints known?) |
| draft | spec, proposal, pitch, brainstorm | Specification readiness (does a design artifact exist?) |
| review | design, code, users, customers | Design-quality readiness (has the design been evaluated and found sound?) |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | Assumption readiness (are key claims validated by evidence?) |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | Behavioral readiness (does the design behave correctly under realistic conditions?) |
| trace | request, state, contract, component, deployment, migration, permissions | Structural readiness (are contracts, state machines, and boundaries sound?) |
| listen | feedback, support, adoption | Adoption readiness (are users and support prepared?) |
| topic | new, plan, story, status, report, echo | Arc readiness (is the full evidence story coherent and defensible?) |

Rung-clearance order: `scout → draft → review/prove → flow/trace → listen → topic`.
Rung 1 must be cleared before Rung 2 can be attempted. A team that runs `draft:spec`
before `scout:market` has not cleared Rung 1 — they have stepped onto Rung 2 while Rung
1 is still beneath them, uncleared.

---

**Layer 1 (Breadth) — Ground level: clears the foundational readiness rung that Layer 2 requires before stepping onto the design level:**

Rung 1 asks: is the investigation ready to design? That question has a specific clearance
condition — foundational signals must exist and meet a numeric threshold. Scout-namespace
skills produce those signals: market shape, feasibility bounds, stakeholder positions,
compliance constraints, competitive context. None of these are produced by design work;
they are pre-conditions for it. The bad plan placed `draft:spec` on this rung — the team
attempted to step to the design level before the foundational rung was cleared, producing
a spec written in an evidence vacuum. Layer 1 clears only the foundational readiness
dimension. Its gate is the rung-clearance condition: named scout artifact types present
and the residual open-question count below the stated threshold. When Rung 1 is cleared,
Layer 2 can step onto the design level.

**Layer 2 (Depth) — Design level: requires Layer 1 foundational rung cleared; clears the design readiness rung that Layer 3 requires before stepping onto the synthesis level:**

Rung 2 asks: is the investigation ready to synthesize? To clear this rung, three readiness
dimensions must be addressed. Specification readiness first: `draft:spec` and
`prove:prototype` produce the working design and its tested model. Design-quality readiness
next: `review:design` cannot evaluate a design that does not yet exist; it requires
`draft:spec` to have stepped onto the rung before review can contribute to clearing it.
Behavioral and structural readiness last: `flow:lifecycle` cannot simulate a lifecycle the
spec has not defined; `trace:state` cannot trace state transitions the spec has not
specified. Each sub-dimension of Rung 2 requires the prior sub-dimension to be in progress
or cleared. Rung 2 also requires Rung 1 to be cleared at entry — the spec author needs
the market signals, feasibility bounds, and compliance constraints that Layer 1 produced.
When Rung 2 is cleared, Layer 3 can step onto the synthesis level.

**Layer 3 (Synthesis) — Synthesis level: requires the full validated artifact set from prior rungs to clear the readiness rung that opens the top of the ladder:**

Rung 3 asks: is the investigation ready to close? This rung cannot be attempted until
Rungs 1 and 2 are both fully cleared. Listen-namespace skills assess adoption readiness
against the validated design — but that validation must exist from Rung 2. Topic-namespace
skills produce the readiness declaration and narrative synthesis — but they require the
full evidence arc from all prior rungs to produce a defensible synthesis. A synthesis
attempted on partial evidence is not Rung 3 — it is a premature exit from the ladder. The
gate for Rung 3 is the total-arc clearance condition: named synthesis artifacts present
and the topic can declare readiness without qualification based on the evidence the prior
rungs produced.

**The echo stage — why it is always at the top of the ladder and always auto:**

1. **Echo carries no skills because the ladder is fully climbed.** Every rung has a
   clearance condition; echo is not a rung. It is the landing at the top. Adding skills to
   echo means a rung was missing from the plan — not that echo should carry the remaining
   work. Fix the ladder, not the landing.
2. **`auto: true` means echo closes without a rung-clearance gate.** Echo does not wait
   for a human to declare the ladder climbed. When the prior stage's rung-clearance
   condition passes, echo fires automatically. Its question is retrospective: what did the
   investigation teach us about the rungs we designed?
3. **Echo signals arc completion.** When echo closes, every rung was cleared, every
   readiness dimension addressed. The program is complete — not because the team felt
   ready, but because every rung was climbed.

---

Build the readiness ladder for **{{topic}}** using the template below. Fill in all
bracketed fields. Preserve all YAML comments — they are the rung markers.

```yaml
# REQUIRED PRESERVE: this program is a readiness ladder, not a climber.
# It defines the rungs and clearance conditions; it does not climb them. Each skill runs standalone.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Ground Level ---- | scout:* clears Rung 1 foundational readiness | draft:* requires Rung 1 cleared ----
    - name: "[foundational rung label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills that address foundational readiness for {{topic}}
      gate: "[scout artifact-types present] and [rung-clearance condition — >=N scout signals, foundational questions answered, no P0 gaps]"

    # ---- Rung 1 → Rung 2 transition: foundational readiness cleared → design rung unlocked ----

    # ---- Layer 2: Design Level ---- | draft:*/prove:*/review:*/flow:*/trace:* clear Rung 2 | requires Rung 1 | clears design readiness Rung 3 requires ----
    - name: "[specification rung label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills for {{topic}}
      gate: "[draft/prove artifact-types present] and [rung-clearance condition — specification readiness cleared, <=N open questions, prototype passes]"

    - name: "[validation rung label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills for {{topic}}
      gate: "[review/flow/trace artifact-types present] and [rung-clearance condition — design-quality readiness cleared, <=N open findings, no P0 blockers]"

    # ---- Rung 2 → Rung 3 transition: design readiness cleared → synthesis rung unlocked ----

    # ---- Layer 3: Synthesis Level ---- | listen:*/topic:* clear Rung 3 | requires full Rung 1+2 cleared ----
    - name: "[synthesis rung label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills for {{topic}}
      gate: "[listen/topic artifact-types present] and [rung-clearance condition — adoption readiness cleared, >=N signals, topic declares ready]"

    # ---- Top of Ladder ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; top of ladder reached when prior rung clears

## Readiness Ladder Verification
# [ ] YAML parses; every stage has name, skills, and gate fields
# [ ] Last stage is echo with skills: [] and auto: true; no stages follow it
# [ ] Every skill belongs to Signal's 9 namespaces; no invented skill names
# [ ] Every non-echo gate names an artifact type and a rung-clearance condition — not "done", "ready", or empty
# [ ] Scout skills appear before draft; draft before review/prove; review/prove before listen/topic
# [ ] Stage names describe the readiness rung being cleared, not generic labels
# [ ] At least one gate carries a numeric threshold (>=N or <=N)
# [ ] This plan defines the rungs; it does not climb them — each skill runs standalone
```

---

## V-04 — Combined: Role Sequence + Inertia Framing (Architectural Blueprint)

**Axes:** Role sequence — skills are ordered as construction phases with explicit
dependency rationale; each phase states what structural artifact it requires from the
prior phase before work can begin. Inertia framing — the bad pattern is a meeting where
an architect sketched phases without defining structural acceptance criteria; inertia
framing appears at the opening (meeting narrative), within the gate table (the acceptance
criteria the architect declined to define), and within Layer 2 narration (the structural
dependency the bad plan violated). Domain metaphor: architectural blueprint. Skills produce
load-bearing artifacts. Gates are structural acceptance criteria. C-33: "Structural
dependency cleared." C-34: "This blueprint specifies the construction sequence; it does
not build it."

**Hypothesis:** The blueprint metaphor gives C-05 (dependency ordering) a vivid anchor:
construction phases have structural dependencies that are ethically non-negotiable. C-10
(inertia contrast) gains three distinct displacement moments. C-33 naturally yields
"Structural dependency cleared" as the skill catalog column. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

In the architecture review for `{{topic}}`, the principal architect drew four boxes on a
whiteboard: Foundation, Structure, Inspection, Handoff. "Standard construction phases,"
she said. "Each phase builds on the prior." The tech lead asked what structural artifacts
each phase needed to produce before the next could begin. The architect said: "The usual
acceptance criteria — we'll define them as we go." The product manager said: "Let's just
say 'acceptance complete' for each gate. We can tighten them up in sprint one." Nobody
pushed back. The phases were written up. Twelve weeks later, the structural review found
that the validation phase had run before the specification was finalized — the team had
built a structure on an unfinished foundation.

Here is the blueprint that architecture review produced for **{{topic}}**:

```yaml
# BAD — the blueprint with no structural acceptance criteria:
stages:
  - name: foundation
    skills: [scout:feasibility, scout:requirements, draft:spec]
    gate: "foundation complete"
  - name: structure
    skills: [review:design, prove:prototype, flow:lifecycle]
    gate: "structure complete"
  - name: inspection
    skills: [trace:contract, trace:state, listen:adoption]
    gate: "inspection complete"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the blueprint it produced.

"Foundation complete" is not a structural acceptance criterion — it names execution state,
not what load-bearing artifacts the phase produced. The blueprint placed `draft:spec` in
the foundation phase alongside `scout:feasibility` and `scout:requirements`: the spec was
written while requirements gathering was still in progress, producing a specification with
an unfinished requirements foundation beneath it. `flow:lifecycle` was placed in the
structure phase before a finalized spec existed for the lifecycle to simulate. "Structure
complete" names when builders stopped; it does not specify whether the structure is sound.
`listen:adoption` was placed in the inspection phase before behavioral validation existed
to support an adoption assessment.

`/program:plan` is not an executor. It produces an architectural blueprint — a structured
construction plan with named phases, dependency-ordered skills, and structural acceptance
criteria specifying what load-bearing artifacts must exist before the next phase can begin.
The blueprint specifies the construction sequence; it does not build it. Each skill runs
standalone. The program is optional scaffolding.

---

**Before you build the blueprint, read these three tables.**

---

**Table 1 — Evidence arc: construction phases, structural layers, and artifact handoff**

| Phase | Layer | Structural role | Namespaces | Load-bearing artifacts produced for next phase |
|-------|-------|-----------------|------------|------------------------------------------------|
| Foundation | Layer 1 (Breadth) | Structural origin — lays the scout foundation Layer 2 builds upon | scout | Scout signal artifacts: feasibility bounds, market constraints, requirements, compliance shape |
| Structure | Layer 2 (Depth) | Receives Layer 1 foundation artifacts; produces the structural frame Layer 3 inspects | draft, prove, review, flow, trace | spec, prototype, design-review, simulation, and trace artifacts |
| Inspection + Handoff | Layer 3 (Synthesis) | Requires the full structurally-validated artifact set from prior phases | listen, topic | adoption-readiness, synthesis, and handoff artifacts |
| Terminal | Echo | Post-construction retrospective — no new building | — | — |

---

**Table 2 — Gate design: BAD construction gates, why they fail as acceptance criteria, GOOD structural acceptance criteria**

When the tech lead asked about acceptance criteria and the architect said "we'll define
them as we go," here is the table that "as we go" was deferring:

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"foundation complete"` | Completion state — names when builders stopped, not whether the foundation is load-bearing | `"[scout artifact-types present] and [acceptance condition — >=2 scout signals, requirements coverage complete, no P0 feasibility gaps]"` |
| `"structure complete"` | Execution state — names when construction ran, not whether the structure is sound | `"[draft-spec and prototype artifact-types present] and [acceptance condition — no open P0 spec questions, prototype passes structural test]"` |
| `"inspection complete"` | Execution state — names when inspectors stopped, not what structural findings they produced | `"[review/flow/trace artifact-types present] and [acceptance condition — <=2 structural findings, no load-bearing issues, simulation gaps <=N]"` |
| `"acceptance complete"` | Circular — restates that acceptance ran; names no structural criterion | `"[listen-adoption signal present] and [acceptance condition — >=3 adoption evaluations, handoff readiness criteria met]"` |
| `""` (empty) | Absent — no structural acceptance criterion; the blueprint has no gates | `"[topic-status artifact present] and [acceptance condition — topic declares structural readiness, no unresolved findings]"` |

---

**Table 3 — Signal skill catalog by namespace and structural dependency**

| Namespace | Skills | Structural dependency cleared |
|-----------|--------|-------------------------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | Foundation dependency (market viability, feasibility bounds, requirements shape, compliance constraints) |
| draft | spec, proposal, pitch, brainstorm | Specification dependency (the working design document all later phases build on) |
| review | design, code, users, customers | Design-soundness dependency (structural review of the load-bearing design artifacts) |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | Assumption dependency (empirical validation of the structural claims the spec makes) |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | Behavioral dependency (the runtime structural model of the designed system) |
| trace | request, state, contract, component, deployment, migration, permissions | Contract dependency (the boundary and state structural contracts the system must honor) |
| listen | feedback, support, adoption | Handoff dependency (adoption readiness and support structure for post-construction) |
| topic | new, plan, story, status, report, echo | Arc dependency (the construction story and structural readiness declaration) |

Construction order: `scout → draft → review/prove → flow/trace → listen → topic`. No
construction phase may begin before the structural dependencies of the prior phase are
met. Placing `draft:spec` in the foundation phase before `scout:requirements` completes
is building a frame on an unfinished foundation — exactly the error the architecture
review normalized by deferring acceptance criteria.

---

**Layer 1 (Breadth) — Foundation phase: lays the structural origin that Layer 2's design and validation phases build upon:**

The foundation phase establishes the invariants all subsequent construction depends on:
what is technically feasible, what requirements must be satisfied, what the market demands,
what compliance constraints bound the design space. Scout-namespace skills produce these
structural inputs. None of them are produced by design or review work — they are pre-
conditions that make the structure phase possible. The bad blueprint placed `draft:spec`
in this phase alongside `scout:feasibility` and `scout:requirements` — the team laid the
structural frame before the foundation was poured. A spec written before requirements
gathering is complete inherits the open requirement questions as unresolved structural
gaps. Layer 1 runs only scout-namespace skills. Its gate is a structural acceptance
criterion: named scout artifact types present and the foundational uncertainty below a
specified threshold. When the foundation phase clears its acceptance criterion, the
structure phase can begin on a solid base.

**Layer 2 (Depth) — Structure phase: receives Layer 1 foundation artifacts; produces the structural frame that Layer 3 inspection and handoff requires:**

The structure phase builds on the foundation. Draft-namespace skills produce the working
design: `draft:spec` draws the structural plan; `prove:prototype` builds and tests the
working model. Review-namespace skills inspect the structure: `review:design` cannot
evaluate a design that `draft:spec` has not produced. Flow- and trace-namespace skills
validate behavioral and contract structure: `flow:lifecycle` cannot simulate a lifecycle
the spec has not specified; `trace:contract` cannot verify contracts the spec has not
defined. The bad blueprint grouped `review:design`, `prove:prototype`, and `flow:lifecycle`
in the same "structure" phase — the inspector ran alongside the builder, reviewing plans
that were still being drawn. Layer 2 requires Layer 1 foundation artifacts at entry — the
spec author needs feasibility bounds, requirements constraints, and market signals to
produce a structurally grounded design. Layer 2 gates are per-phase structural acceptance
criteria: spec present with no P0 questions; design review passed with <=N findings;
simulation cleared all blocking structural gaps.

**Layer 3 (Synthesis) — Inspection and handoff phase: requires the full structurally-validated artifact set from prior phases before certifying construction is complete:**

The inspection and handoff phase cannot certify what it has not inspected. Listen-namespace
skills assess adoption readiness — but only against a validated structural frame. If
`review:design` produced unresolved P0 findings, the structure is not ready for adoption
assessment. Topic-namespace skills produce the construction completion declaration and
handoff narrative — but only if the full arc is structurally sound. The bad blueprint
placed `listen:adoption` in the inspection phase alongside `trace:contract` and
`trace:state` — the adoption assessment ran before behavioral validation (flow) was
complete. Layer 3 requires the complete structurally-validated artifact set from Layers 1
and 2. Its gate is the final structural acceptance criterion: named handoff artifacts
present and the topic can declare structural readiness without qualification.

**The echo stage — why it is always the last phase and always auto:**

1. **Echo carries no construction skills because the structure is complete.** Echo is the
   post-construction retrospective, not a construction phase. If a structural gap remains
   when the arc reaches echo, the blueprint was missing a phase — add the missing
   acceptance criterion to a prior gate, not to echo. Echo does not fix incomplete
   construction; it reflects on complete construction.
2. **`auto: true` means echo closes without a structural acceptance gate.** Echo does not
   wait for a final inspector to sign off on the construction. When the prior phase's gate
   passes, echo fires automatically. Its question is retrospective: what did we learn about
   the construction that the original blueprint did not anticipate?
3. **Echo signals construction completion.** When echo closes, every phase has cleared its
   structural acceptance criterion. The construction is done — not because the team felt
   it was done, but because every load-bearing artifact exists and every structural
   criterion was met.

---

Build the blueprint for **{{topic}}** using the template below. Fill in all bracketed
fields. Preserve all YAML comments — they are structural load-bearing annotations.

```yaml
# REQUIRED PRESERVE: this program is an architectural blueprint, not a builder.
# It specifies the construction sequence; it does not build it. Each skill runs standalone.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Foundation ---- | scout:* lays structural foundation | draft:* requires Layer 1 foundation cleared ----
    - name: "[foundation phase label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* skills that address structural foundation dependencies for {{topic}}
      gate: "[scout artifact-types present] and [acceptance condition — >=N scout signals, requirements coverage complete, no P0 feasibility gaps]"

    # ---- Foundation → Structure transition: foundation acceptance criteria met → structure phase begins ----

    # ---- Layer 2: Structure ---- | draft:*/prove:*/review:*/flow:*/trace:* build structural frame | requires Layer 1 foundation | produces validated frame Layer 3 requires ----
    - name: "[specification/design phase label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* skills for {{topic}}
      gate: "[draft/prove artifact-types present] and [acceptance condition — no P0 spec questions, structural prototype passes, <=N open findings]"

    - name: "[structural validation phase label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* skills for {{topic}}
      gate: "[review/flow/trace artifact-types present] and [acceptance condition — <=N structural findings, no load-bearing gaps, simulation complete]"

    # ---- Structure → Inspection transition: structural acceptance criteria met → inspection phase begins ----

    # ---- Layer 3: Inspection + Handoff ---- | listen:*/topic:* complete construction | requires full structural artifact set from Layers 1+2 ----
    - name: "[inspection and handoff phase label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* skills for {{topic}}
      gate: "[listen/topic artifact-types present] and [acceptance condition — adoption criteria met, >=N evaluations, topic declares structural readiness]"

    # ---- Post-Construction ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; construction complete when prior acceptance criterion passes

## Blueprint Verification
# [ ] YAML parses; every stage has name, skills, and gate fields
# [ ] Last stage is echo with skills: [] and auto: true; no stages follow it
# [ ] Every skill belongs to Signal's 9 namespaces; no invented skill names
# [ ] Every non-echo gate names an artifact type and a structural acceptance condition — not "complete" or "done"
# [ ] Scout skills appear before draft; draft before review/prove; review/prove before listen/topic
# [ ] Stage names describe the construction phase, not generic labels
# [ ] At least one gate carries a numeric threshold (>=N or <=N)
# [ ] This blueprint specifies the construction sequence; it does not build it — each skill runs standalone
```

---

## V-05 — All R11 Axes Combined: Navigation Chart

**Axes:** Phrasing register (second-person coaching — "you are charting a course"); output
format (waypoint-dominant — each gate is a waypoint fix with bearing and landmark
references); lifecycle emphasis (transitions between waypoints get dominant space); inertia
framing (bad plan = sailing without landmarks, woven at opening, within gate table, and
within Layer 2 narration); role sequence (skills explained as navigation legs with explicit
bearing rationale). Domain metaphor: navigation chart. Skills are navigation instruments.
Stages are voyage legs. Gates are waypoint fixes. C-33: "Navigation waypoint cleared."
C-34: "This chart plots the course; it does not sail it."

**Hypothesis:** The navigation metaphor gives every structural criterion a vivid anchor.
A waypoint fix has a natural two-part structure (landmark present + bearing confirmed) that
maps to C-30 (artifact presence + quality condition). "Sailing without landmarks" is the
inertia pattern. The second-person register makes C-12 (not-executor as opening identity)
immediately personal. Score target: 100.00.

---

### Prompt body

You are running `/program:plan` for **{{topic}}**.

---

Before the feature sprint started, a product manager charted the course for `{{topic}}`.
In the navigation briefing she said: "We'll sail in three legs — exploration, design, and
synthesis. When each leg feels complete, we move on." The navigator asked what landmarks
the crew would use to fix their position before advancing to the next leg. The PM said:
"We'll know when we've arrived. We've sailed similar routes before." Nobody named a
landmark. Nobody defined what a confirmed waypoint would look like. The chart was approved.
Two legs in, the crew discovered they had sailed past the design-validation waypoint
without fixing their position — the prototype had been built against a spec that had not
cleared its departure fix. The crew was at sea without a confirmed bearing.

Here is the chart that briefing produced for **{{topic}}**:

```yaml
# BAD — the chart with no waypoint fixes:
stages:
  - name: exploration
    skills: [scout:market, scout:feasibility, draft:spec]
    gate: "exploration complete"
  - name: design-and-build
    skills: [review:design, prove:prototype, flow:lifecycle, trace:state]
    gate: "design complete"
  - name: synthesis
    skills: [listen:adoption, topic:status]
    gate: "ready to ship"
  - name: echo
    skills: []
    auto: true
```

`/program:plan` exists to replace this conversation and the chart it produced.

"Exploration complete" is not a waypoint fix — it names when the crew stopped sailing, not
what landmark they confirmed their position against. The chart co-located `draft:spec` with
`scout:market` on the same exploration leg: the spec was written before market signals
existed to set the bearing. `flow:lifecycle` and `trace:state` were placed alongside
`review:design` and `prove:prototype` — the crew was simulating a lifecycle before the
spec had established the route to simulate. "Ready to ship" is a destination, not a
waypoint fix — it names the port they hoped to reach, not the confirmed bearing that
validates they are on course.

You are charting a course, not sailing it. `/program:plan` produces a navigation chart —
a structured plan with named voyage legs, dependency-ordered instruments, and waypoint
fixes specifying what landmarks must be confirmed before the crew can advance to the next
leg. The chart does not sail. Each skill runs standalone. The program is optional
scaffolding that organizes the voyage but does not crew it.

---

**Before you chart the course, read these three tables.**

---

**Table 1 — Evidence arc: voyage legs, navigation role, and bearing handoff**

| Leg | Layer | Navigation role | Namespaces | Bearing handed to next leg |
|-----|-------|-----------------|------------|---------------------------|
| Departure leg | Layer 1 (Breadth) | Course origin — fixes departure bearing that Layer 2 navigates from | scout | Scout signal artifacts: market bearing, feasibility heading, stakeholder landmarks, compliance constraints |
| Passage leg | Layer 2 (Depth) | Receives Layer 1 departure bearing; fixes passage waypoints that Layer 3 navigates from | draft, prove, review, flow, trace | spec, prototype, design-review, simulation, and trace artifacts |
| Arrival leg | Layer 3 (Synthesis) | Requires the full validated bearing context from prior legs to fix the arrival waypoint | listen, topic | adoption-readiness, synthesis, and arrival-fix artifacts |
| Harbor | Echo | Auto-closing; anchor is set; voyage is complete | — | — |

---

**Table 2 — Gate design: BAD unanchored gates, why they fail as waypoint fixes, GOOD confirmed waypoints**

When the navigator asked "what landmarks will we fix our position against?" and the PM
said "we'll know when we've arrived," here is the chart the crew was declining to draw:

| BAD gate | Why it fails | GOOD gate |
|----------|--------------|-----------|
| `"exploration complete"` | Momentum marker — names when the crew stopped, not what landmark they confirmed | `"[scout artifact-types present] and [waypoint condition — >=2 scout signals confirm bearing, no P0 course hazards]"` |
| `"design complete"` | Execution state — names when designers stopped, not whether the waypoint fix is confirmed | `"[draft-spec and prototype artifact-types present] and [waypoint condition — bearing confirmed at >=N%, no P0 course deviations]"` |
| `"ready to ship"` | Destination assertion — names the port they hope to reach, not the bearing confirming they are on course | `"[listen-adoption signal present] and [waypoint condition — >=3 crew confidence readings, arrival heading confirmed]"` |
| `"all good"` | Subjective — no landmark; no bearing threshold | `"[review/flow/trace artifact-types present] and [waypoint condition — <=N open course corrections, no blocking passage gaps]"` |
| `""` (empty) | Absent — no waypoint; position cannot be confirmed | `"[topic-status artifact present] and [waypoint condition — topic fixes arrival position, no unresolved bearings]"` |

---

**Table 3 — Signal skill catalog by namespace and navigation waypoint**

| Namespace | Skills | Navigation waypoint cleared |
|-----------|--------|------------------------------|
| scout | competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements | Departure fix (is the course viable? are the hazards charted? is the heading cleared?) |
| draft | spec, proposal, pitch, brainstorm | Specification fix (is the route documented and the destination defined?) |
| review | design, code, users, customers | Design-soundness fix (is the documented route safe and navigable?) |
| prove | hypothesis, websearch, analysis, intelligence, prototype, synthesize, publish, interview | Assumption fix (have the key route assumptions been confirmed by evidence?) |
| flow | lifecycle, conversation, trigger, dataflow, integration, throttle, resilience | Passage fix (does the route hold under realistic voyage conditions?) |
| trace | request, state, contract, component, deployment, migration, permissions | Contract fix (are the channel boundaries and state transitions correctly charted?) |
| listen | feedback, support, adoption | Arrival fix (are crew and harbor ready to receive the vessel?) |
| topic | new, plan, story, status, report, echo | Voyage fix (is the full voyage story coherent and the arrival defensible?) |

Navigation order: `scout → draft → review/prove → flow/trace → listen → topic`. You
cannot fix a passage waypoint without first confirming the departure bearing. Sailing the
passage leg before the departure leg is cleared is sailing into uncharted waters — which
is what the exploration-phase spec was doing when `draft:spec` shared a leg with
`scout:market`.

---

**Layer 1 (Breadth) — Departure leg: fixes the departure bearing that Layer 2's passage leg navigates from:**

You begin by establishing where you are and what heading you are sailing on. Scout-
namespace skills are your instruments for the departure fix: they measure the market
bearing (is there demand?), the feasibility heading (is the route technically viable?),
the stakeholder landmarks (who is watching from shore?), the compliance hazards (what
channels are restricted?). None of these readings are produced by design or validation
instruments — they are pre-conditions for knowing what you are about to build. The bad
chart placed `draft:spec` on the departure leg alongside `scout:market` — the crew was
charting the passage route before the departure bearing was confirmed. A spec written
without a confirmed departure bearing is a map drawn from an unknown position. Layer 1
runs only scout-namespace instruments. Its gate is a waypoint fix: named scout artifact
types present and the departure bearing confirmed to a named confidence level before you
sail the passage leg.

**Layer 2 (Depth) — Passage leg: receives Layer 1 departure bearing; fixes the passage waypoints that Layer 3's arrival leg navigates from:**

You sail the passage leg with your departure bearing confirmed. Draft-namespace instruments
chart the route: `draft:spec` draws the detailed navigation plan; `prove:prototype` sails
a test run and confirms the model holds. Review-namespace instruments inspect the chart:
`review:design` cannot inspect a chart that `draft:spec` has not drawn. Flow- and trace-
namespace instruments simulate the passage and chart the channel contracts: `flow:lifecycle`
cannot simulate a voyage leg the spec has not defined; `trace:state` cannot chart state
transitions the spec has not specified. The bad chart placed `flow:lifecycle` alongside
`review:design` and `prove:prototype` — the passage simulation ran before the route was
designed. Layer 2 requires the Layer 1 departure bearing at entry: the spec author needs
market readings, feasibility headings, and compliance hazard charts that Layer 1 produced.
Layer 2 fixes three passage waypoints in sequence: specification fix, design-soundness fix,
and passage-simulation fix. Each fix requires the prior to be confirmed.

**Layer 3 (Synthesis) — Arrival leg: requires the full passage-confirmed bearing context from prior legs to fix the arrival waypoint:**

You fix the arrival waypoint only after the departure and passage bearings are both
confirmed. Listen-namespace instruments take arrival readings: crew readiness, harbor
capacity, adoption confidence. But if the passage was not confirmed — if `review:design`
found blocking structural issues, or `flow:lifecycle` found unreachable lifecycle states —
the arrival readings will be taken against an unconfirmed bearing, and the arrival fix will
be false. Topic-namespace instruments synthesize the full voyage into a readiness
declaration and narrative. `topic:status` cannot declare arrival if the passage waypoints
are not confirmed. Layer 3 requires the complete passage-confirmed artifact set from Layers
1 and 2. Its gate is the arrival waypoint fix: named arrival artifacts present and the
topic can declare a confirmed position without qualification.

**The echo stage — why it is always the harbor and always auto:**

1. **Echo carries no navigation instruments because the voyage is complete.** Echo is the
   harbor — the vessel has arrived, the anchor is set, the sails are furled. Adding skills
   to echo means a passage waypoint was missing from the chart. Fix the chart: add the
   missing waypoint fix to a prior gate and re-sail the leg. Echo does not extend the
   voyage; it marks its end.
2. **`auto: true` means echo anchors without a final waypoint fix.** Echo does not wait
   for a harbor master to confirm arrival. When the prior stage's gate passes, echo fires
   automatically. Its question is retrospective: what did the voyage teach us that the
   original chart did not show?
3. **Echo signals voyage completion.** When echo closes, every waypoint was fixed, every
   leg was cleared, every bearing was confirmed. The voyage is complete — not because the
   crew felt they had arrived, but because every waypoint fix was confirmed against the
   chart.

---

Chart the course for **{{topic}}** using the template below. Fill in all bracketed fields.
Preserve all YAML comments — they are the chart's waypoint markers.

```yaml
# REQUIRED PRESERVE: this program is a navigation chart, not a crew.
# It plots the course; it does not sail it. Each skill runs standalone.

program:
  topic: "{{topic}}"
  stages:

    # ---- Layer 1: Departure Leg ---- | scout:* fixes departure bearing | draft:* requires Layer 1 departure bearing confirmed ----
    - name: "[departure leg label]"
      skills:
        - "[scout namespace skill]"
        - "[scout namespace skill]"
        # add scout:* instruments for fixing the departure bearing of {{topic}}
      gate: "[scout artifact-types present] and [waypoint condition — >=N scout signals confirm bearing, no P0 course hazards]"

    # ---- Departure → Passage transition: departure bearing confirmed → passage leg begins ----

    # ---- Layer 2: Passage Leg ---- | draft:*/prove:*/review:*/flow:*/trace:* fix passage waypoints | requires Layer 1 bearing | produces confirmed route Layer 3 requires ----
    - name: "[specification/routing leg label]"
      skills:
        - "[draft namespace skill]"
        - "[prove namespace skill]"
        # add draft:* and prove:* instruments for {{topic}}
      gate: "[draft/prove artifact-types present] and [waypoint condition — specification fix confirmed, <=N open course questions, prototype run passes]"

    - name: "[passage validation leg label]"
      skills:
        - "[review namespace skill]"
        - "[flow namespace skill]"
        - "[trace namespace skill]"
        # add review:*/flow:*/trace:* instruments for {{topic}}
      gate: "[review/flow/trace artifact-types present] and [waypoint condition — passage fix confirmed, <=N course corrections, no blocking channel gaps]"

    # ---- Passage → Arrival transition: passage waypoints confirmed → arrival leg begins ----

    # ---- Layer 3: Arrival Leg ---- | listen:*/topic:* fix arrival waypoint | requires full confirmed bearing from Layers 1+2 ----
    - name: "[arrival/synthesis leg label]"
      skills:
        - "[listen namespace skill]"
        - "[topic namespace skill]"
        # add listen:* and topic:* instruments for {{topic}}
      gate: "[listen/topic artifact-types present] and [waypoint condition — arrival fix confirmed, >=N crew confidence signals, topic declares position]"

    # ---- Harbor ----
    - name: echo
      skills: []
      auto: true
      # REQUIRED PRESERVE: echo is always last, always auto; harbor reached when arrival waypoint fix passes

## Navigation Chart Verification
# [ ] YAML parses; every stage has name, skills, and gate fields
# [ ] Last stage is echo with skills: [] and auto: true; no stages follow it
# [ ] Every skill belongs to Signal's 9 namespaces; no invented skill names
# [ ] Every non-echo gate names an artifact type and a waypoint condition — not "complete" or "ready to ship"
# [ ] Scout skills appear before draft; draft before review/prove; review/prove before listen/topic
# [ ] Stage names describe the voyage leg, not generic labels
# [ ] At least one gate carries a numeric threshold (>=N or <=N)
# [ ] This chart plots the course; it does not sail it — each skill runs standalone
```

---

## Criterion Coverage Summary

All five variations target 27/27 aspirational criteria. C-33 and C-34 coverage:

| Variation | Axis | C-33 Third Column Header | C-34 Domain-Metaphor Checklist Item |
|-----------|------|--------------------------|--------------------------------------|
| V-01 (Case File) | Phrasing register | "Evidence category gathered" | "This case file organizes evidence collection; it does not conduct the investigation" |
| V-02 (Calibration) | Output format | "Uncertainty dimension addressed" | "This plan calibrates confidence; it does not achieve it" |
| V-03 (Readiness Ladder) | Lifecycle emphasis | "Readiness dimension cleared" | "This plan defines the rungs; it does not climb them" |
| V-04 (Blueprint) | Role sequence + inertia | "Structural dependency cleared" | "This blueprint specifies the construction sequence; it does not build it" |
| V-05 (Navigation) | All R11 axes | "Navigation waypoint cleared" | "This chart plots the course; it does not sail it" |

**Locked structural features inherited from R10 (C-28 through C-32):**
- BAD example as causal meeting narrative (C-28) — distinct meeting scene per variation
- Identity claim scopes replacement to conversation + plan (C-29) — all five use "replace this conversation and the [plan] it produced"
- Composite gate placeholder: artifact-presence + quality condition (C-30) — all gates use `"[X artifact-types present] and [Y condition — ...]"` notation
- Three-column BAD/Why it fails/GOOD gate table (C-31) — all variations
- Layer 2 header bidirectional: names Layer 1 upstream AND Layer 3 downstream (C-32) — all variations
