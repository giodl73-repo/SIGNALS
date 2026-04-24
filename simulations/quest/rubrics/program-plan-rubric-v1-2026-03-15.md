---
skill: quest-rubric
skill_target: program-plan
date: 2026-03-15
version: 1
---

# Rubric — program-plan

Evaluate outputs from the `program-plan` skill, which sequences Signal plugin skills into a
staged evidence-gathering plan (`program.yaml`). The plan is not an executor: its only product
is the gate — a shared definition of what evidence must exist before advancing to the next stage.
Every skill in the plan remains independently runnable. The final stage is always `echo`.

---

## Essential Criteria (all must pass — 60% of score)

### C-01 — Valid YAML Structure
- **Weight**: essential
- **Category**: format
- **Text**: The output is syntactically valid YAML with the required structural skeleton:
  a `program:` top-level key containing `topic` (string), `strategy` (string), and `stages`
  (sequence). Each non-echo stage contains `name` (string), `skills` (sequence), and `gate`
  (string). The echo stage contains `name: echo`, `skills: []`, and `auto: true`. A prose-only
  response or bulleted list is not an acceptable substitute.
- **Pass condition**: Output parses as valid YAML. All three top-level program fields are
  present and non-empty. Every stage includes `name`, `skills`, and either `gate` (non-echo)
  or `auto: true` (echo). Missing required keys or unparseable YAML fails.

### C-02 — Echo Final Stage Contract
- **Weight**: essential
- **Category**: correctness
- **Text**: The last stage is exactly the echo stage: `name: echo`, `skills: []`, `auto: true`.
  Echo appears only once, only last. No skills are listed in the echo stage. The `auto: true`
  field is present. No stage follows echo.
- **Pass condition**: The final element of `stages` is `{name: echo, skills: [], auto: true}`.
  Echo placed anywhere other than last, echo with skills in it, echo missing `auto: true`, or
  echo absent entirely all fail. The echo contract is a hard requirement from plugin design.

### C-03 — Valid Signal Skill Names Only
- **Weight**: essential
- **Category**: correctness
- **Text**: Every entry in every `skills` list is a real, namespace-qualified skill from
  Signal's 9-namespace catalog: `scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`,
  `program`, `topic`. Valid format: `namespace:skill` (e.g., `scout:feasibility`, `flow:lifecycle`,
  `trace:contract`). Invented namespaces, invented skill names within valid namespaces, and
  skills listed without namespace qualification all fail.
- **Pass condition**: Every skill reference resolves to a real Signal skill. A single invented
  name (e.g., `scout:analysis`, `build:deploy`) fails the entire criterion.

### C-04 — Evidence-State Gates (Not Execution State)
- **Weight**: essential
- **Category**: correctness
- **Text**: Every non-echo stage gate expresses evidence state — what artifacts must exist or
  what conditions must be verifiably true — not execution state. Evidence-state gates name
  artifacts by type (`scout-feasibility artifact present`), count signals (`>= 2 scout signals`),
  or describe a checkable condition (`no blocking feasibility concerns identified`).
  Execution-state gates describe what was done: `"done"`, `"complete"`, `"all skills run"`,
  `"proceed"`, `"stage complete"`, `"tasks finished"`. These fail because the next-phase owner
  cannot verify them.
- **Pass condition**: Every non-echo gate contains at least one artifact name, signal count, or
  verifiable evidence condition. A plan where even one gate consists solely of execution-state
  language fails.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-05 — Namespace Dependency Order Respected
- **Weight**: recommended
- **Category**: correctness
- **Text**: Stages follow Signal's namespace dependency order. `scout` skills precede `draft`
  skills; `draft:spec` precedes `review:*`; `review:*` precedes `flow:*` and `trace:*`;
  `listen:*` and `topic:*` appear after simulation stages. The canonical ordering is:
  `scout → draft → review/prove → flow/trace → listen/topic → echo`. A stage with `review:design`
  placed before any `draft:spec` stage violates this order because review requires a spec.
- **Pass condition**: No stage contains skills whose dependencies have not been produced by a
  prior stage. Minor exceptions (e.g., `prove:websearch` in a discovery stage) are acceptable
  where the stage scope makes the ordering intent clear.

### C-06 — Descriptive Stage Names
- **Weight**: recommended
- **Category**: format
- **Text**: Stage names are human-readable phase labels describing team intent — not namespace
  names reused as labels, not generic indices, not skill names. Passing: `discovery`,
  `market-scan`, `design`, `expert-review`, `simulation`, `feedback-preview`. Failing: `scout`,
  `draft`, `stage1`, `step-2`, `flow`.
- **Pass condition**: Every non-echo stage name would communicate phase intent to a stakeholder
  unfamiliar with Signal namespaces. Any stage named identically to a Signal namespace or using
  generic position indices fails.

### C-07 — Plan-Not-Executor Identity Present
- **Weight**: recommended
- **Category**: behavior
- **Text**: The output makes clear the program is a plan, not an executor. This may appear as
  a YAML comment (`# this program is a plan, not an executor; skills run standalone`), in the
  `strategy` field framing the program as a decision-support artifact, or in a verification note
  accompanying the YAML. The plan does not describe stages as automatically running skills or
  present the program as a pipeline executor.
- **Pass condition**: At least one place in the output explicitly marks the program as a plan
  and not an automation layer, or the strategy field describes what decision the evidence
  informs. Plans that frame stages as execution steps or imply skills run automatically fail.

---

## Aspirational Criteria (raise the bar — 10% of score)

### C-08 — At Least One Quantified Gate
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one non-echo gate contains a numeric threshold that makes it
  machine-checkable in principle: `">= 2 scout signals present"`, `"0 P0 findings open"`,
  `">= 3 review artifacts"`, `"draft-spec and >= 1 feasibility signal archived"`. Quantified
  gates transform qualitative evidence conditions into verifiable pass/fail checks and signal
  the program was designed to be evaluated, not just read.
- **Pass condition**: At least one gate uses `>=`, `<=`, `=`, or an explicit count
  (`"0 blocking findings"`, `"at least 2 signals"`). Plans where all gates are qualitative
  only fail.

### C-09 — Deliberate Evidence Arc
- **Weight**: aspirational
- **Category**: depth
- **Text**: The stage sequence forms a coherent investigation arc — broad exploration first
  (scout, draft), focused validation and depth next (review, prove, flow, trace), synthesis
  last (listen, topic) — rather than a flat skill accumulation or purely topological sort.
  The arc may be made visible via YAML layer-divider comments, stage name groupings that
  reflect the arc (e.g., `discovery` → `design` → `simulation` → `feedback-preview`), or a
  `strategy` field describing the investigation trajectory. The structure shows the plan was
  shaped by a deliberate evidence strategy, not just namespace defaults.
- **Pass condition**: The plan has at least 3 substantive stages (plus echo) organized so that
  earlier stages build the foundation later stages require. The progression from breadth to
  depth to synthesis is visible in stage sequencing and stage naming. Plans that pack all skills
  into one stage or randomize namespace ordering fail.

---

## Scoring Formula

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04 |
| Recommended | 30% | C-05, C-06, C-07 |
| Aspirational | 10% | C-08, C-09 |

```
composite = (essential_pass/4 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/2 * 10)
```

**Golden threshold**: all 4 essential criteria pass **and** composite >= 80.

---

## Scoring Worksheet

```
Essential:    C-01 [ ]  C-02 [ ]  C-03 [ ]  C-04 [ ]
              Pass count: ___ / 4  ->  ___ / 4 * 60 = ___ pts  (of 60)

Recommended:  C-05 [ ]  C-06 [ ]  C-07 [ ]
              Pass count: ___ / 3  ->  ___ / 3 * 30 = ___ pts  (of 30)

Aspirational: C-08 [ ]  C-09 [ ]
              Pass count: ___ / 2  ->  ___ / 2 * 10 = ___ pts  (of 10)

Composite score: ___ / 100
Golden: all essential pass AND composite >= 80  ->  [ ] YES  [ ] NO
```

---

## Failure Fast-Paths

The following conditions fail scoring regardless of composite score:

- Output contains no YAML at all (prose plan or bulleted list only)
- Echo stage is absent, not last, or has any skills listed in it
- Any stage contains an invented Signal skill name not in the 9-namespace catalog
- Every non-echo gate uses execution-state language only (`"done"`, `"complete"`, `"proceed"`)

---

## Scorer Notes

- **C-01**: Check YAML validity first. If unparseable, C-01 fails. Score remaining criteria
  as best-effort but note the failure.
- **C-02**: Echo is a hard contract. Missing `auto: true`, placing echo mid-plan, or listing
  any skills in echo are all hard fails regardless of otherwise valid structure.
- **C-03**: Authority for valid skill names is the plugin-plan.md catalog (9 namespaces, ~47
  skills). Skills listed without namespace prefix fail unless the plan establishes unambiguous
  context — prefer `namespace:skill` form.
- **C-04**: The key test: can the next-phase owner verify the gate is satisfied by looking at
  artifacts, not by asking "did we run the skills?" Gates that describe running fail; gates
  that describe what must exist pass.
- **C-05**: Dependency ordering is assessed by namespace layer (`scout → draft → review/prove
  → topic`), not alphabetically. A plan with `review:design` before any `draft:spec` fails
  C-05 because design review requires a spec artifact to review.
- **C-07**: The "plan not executor" signal can be subtle (a comment, a strategy field framing)
  — it does not require an explicit disclaimer paragraph.
