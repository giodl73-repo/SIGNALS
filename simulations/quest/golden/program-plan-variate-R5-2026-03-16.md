---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 5
rubric: v5
aspirational_target: C-19, C-20, C-21
---

# program-plan -- R5 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v5 (C-01 through C-21, 21 criteria, 160 pts max, golden = all essential pass AND composite >= 80).

---

## R4 Retrospective Under v5 Rubric

Three new aspirational criteria (C-19, C-20, C-21) were extracted from R4 excellence signals.
Retroactively scoring R4 top variations against v5:

| Variation | C-19 cross-tier error coverage | C-20 per-zone dependency reminder | C-21 scaffold integration | v5 composite |
|-----------|-------------------------------|-----------------------------------|---------------------------|--------------|
| V-01 (criterion-tagged BAD block) | PASS -- BAD block tags `# WRONG C-05` (dependency) and `# WRONG C-06` (stage name) alongside essential tags | FAIL -- Design zone has dep note in header; Validation/Simulation/Synthesis zones have no skill-position reminders | FAIL -- no correction table, so no bridges possible | ~105 |
| V-02 (per-zone gate contrast) | FAIL -- zone headers note dependencies but no error artifacts cover recommended criteria | PARTIAL -- zone headers carry dep notes at zone-open but not at skill-list placeholder line | FAIL -- no correction table | ~90 |
| V-03 (correction table) | PASS -- correction table has 2 C-06 pairs (`name: scout` → `name: discovery`, `name: stage1` → `name: expert-review`) | FAIL -- no dependency constraint reminders at any zone level | PARTIAL -- `# check correction table` present at stage-name and gate fields but absent at skill-list fields | ~110 |
| V-04 (C-16 + C-17 combined) | PASS -- BAD block zone-name annotations carry `# WRONG C-06`; per-zone FAIL examples show namespace-label stage names | PARTIAL -- zone headers embed dep notes (`# review:* requires draft:spec -- this zone MUST precede...`) but not at skill-list placeholder positions | FAIL -- no correction table | ~120 |
| V-05 (R4 golden, all 18 criteria) | PASS -- BAD block tags C-05+C-06; correction table has C-06 pairs | PARTIAL -- zone dep notes present in zone headers across most zones but not uniformly at skill-list placeholder line | PARTIAL -- correction table present + some `# check correction table` at gate/name fields but skill-list fields unbridge | ~145 |

**R4 V-05 scores highest under v5** but has two PARTIAL scores (C-20, C-21) preventing full
golden saturation. V-01 already achieves C-19 PASS via criterion-tagged recommended errors.
V-03 achieves C-19 PASS via C-06 correction table entries.

**R5 target**: C-19 comprehensively covers all three recommended criteria (C-05, C-06, C-07)
across error artifacts. C-20 elevates dependency reminders from zone headers to the exact
skill-list placeholder line. C-21 completes the bidirectional correction-table coupling at
all three field types (skills, gates, stage names).

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Inertia framing | Cross-tier error artifacts | Does expanding error coverage to recommended criteria (C-19) -- showing wrong stage names, out-of-order namespaces, executor framing -- teach the model quality failures in addition to structural failures? |
| Lifecycle emphasis | Skill-position dependency constraint | Does moving dependency reminders from zone headers to the skill-list placeholder line itself (C-20) eliminate dependency violations at source, versus requiring the model to carry a header-level note forward into the skills field? |
| Output format | Scaffold-integrated correction table | Does placing `# check correction table` at every covered field type in the template (C-21) force active table consultation at each decision point, versus a one-time table read followed by template filling? |
| Inertia framing + Lifecycle emphasis | Cross-tier errors + skill-position dependency | Can comprehensive error artifacts (C-19) and inline skill-position prerequisites (C-20) coexist without overcrowding the template's authoring zone? |
| Golden synthesis | All three new criteria on best R4 foundation | Does combining C-19 (comprehensive), C-20 (skill-position), and C-21 (complete bridges) with R4 V-05's arc-spine + deletion-resistance + criterion-tagged BAD block + per-zone contrast + correction table saturate all 21 criteria? |

Single-axis: V-01 (cross-tier error coverage), V-02 (skill-position dependency reminders), V-03 (scaffold-integrated correction table)
Combined: V-04 (cross-tier errors + dependency reminders), V-05 (all three new axes, golden)

---

## V-01 -- Cross-Tier Error Coverage (C-19 axis)

**Axis**: Inertia framing -- error artifacts (BAD YAML block and criterion-tagged inline annotations) cover failures from BOTH essential criteria (C-02/C-03/C-04) AND all three recommended criteria (C-05/C-06/C-07).
**Hypothesis**: An error artifact that only shows structural failures (bad YAML, wrong echo, invented skills, execution gates) teaches the model what not to do at the essential tier but leaves recommended failures invisible at authoring time. A BAD PLAN block annotated with `# WRONG C-05` (dependency violation), `# WRONG C-06` (namespace-label stage name), and `# WRONG C-07` (executor framing) makes wrong shapes for quality criteria equally concrete as wrong shapes for structural criteria. C-19 PASS. No skill-position dependency reminders (C-20 FAIL by design); no correction table (C-21 FAIL by design). Base structure is R4 V-01 (criterion-tagged BAD block + lifecycle phases).

Expected gains: C-19 PASS (all recommended criteria represented in at least one error artifact).
Expected gaps: C-20 FAIL (no per-zone skill-position dep reminders), C-21 FAIL (no correction table).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
remain independently runnable. The program does not execute skills, does not advance stages,
and carries no automation authority. Its entire value is the gate: a shared agreement on
what artifacts must exist before handing off to the next phase.

---

You are running `/program:plan` for topic **{{topic}}**.

**The wrong plan -- a complete bad example covering all seven criteria tiers:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- the program reads as an executor, not a plan
  stages:
    - name: scout                  # WRONG C-06: namespace name reused as stage label (not a human-readable phase)
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- invented skill name
        - review:design            # WRONG C-05: review:design placed before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution-state gate -- names no artifact, cannot be verified
    - name: draft                  # WRONG C-06: namespace name again -- "draft" is not a phase label
      skills:
        - draft:spec
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list; skills placed in echo
      auto: true
```

Each `# WRONG C-NN` tag identifies the specific criterion each wrong field violates.
This plan fails all four essential criteria (C-01 through C-04) **and** all three
recommended criteria (C-05 through C-07):

- **C-05** (namespace dependency order): `review:design` appears before `draft:spec`
- **C-06** (descriptive stage names): `scout` and `draft` are namespace names, not phase labels
- **C-07** (plan-not-executor identity): no identity marker anywhere; the plan reads as a task list

---

**The four-phase structure:**

**Phase 1 -- PM: Discovery**
*Goal*: map what we know about the space before designing.
*Gate guidance*: Name the artifacts the Architect needs before drafting. Quantify:
`">= 2 scout signals reviewed; no blocking feasibility concerns"`.
Avoid `"discovery complete"` -- that is an execution state; the Architect cannot verify it.
(Execution-state gates violate C-04.)

**Phase 2 -- Architect + PM: Design**
*Goal*: produce a concrete approach engineering can validate.
*Gate guidance*: What do engineers need before review can begin?
`"draft-spec artifact present; Architect confirmed no blocking feasibility gaps"`.
(`review:*` requires `draft:spec` first -- placing review before draft violates C-05.)
Stage name should be `"design"` or `"proposal"`, not `"draft"` -- C-06 forbids namespace names.

**Phase 3 -- Engineering: Validation**
*Goal*: stress-test the design against real-world signals.
*Gate guidance*: `"review-design and prove-prototype artifacts present; 0 P0 findings open"`.
At least one gate across the plan must include a numeric threshold (C-08).
Stage name should be `"expert-review"` or `"validation"`, not `"review"` -- C-06.

**Phase 4 -- Team: Synthesis**
*Goal*: listen ahead and close the evidence loop.
*Gate guidance*: `"listen-feedback and listen-adoption artifacts present; no critical adoption blockers"`.
Stage name: `"feedback-preview"` or `"synthesis"`, not `"listen"` -- C-06.

**Echo** (auto): always last. `name: echo`, `skills: []`, `auto: true`. The echo contract is C-02.
Echo with any skills violates C-02 -- see the BAD PLAN block above.

**Namespace dependency order (C-05):**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`.
`prove:*` belongs in or before the review/prove layer, not after flow/trace.
Out-of-order placement violates C-05 -- see the BAD PLAN block above.

**Signal skill catalog** (every skill entry must resolve to a name in this list -- C-03):

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
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ---- PM Phase: Discovery -- what we need to know before designing ----
  # PM owns; gate captures what the Architect needs before drafting
  # Stage name: use "discovery" or "market-scan" -- NOT "scout" (WRONG C-06: namespace as label)

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"; NOT "scout" (WRONG C-06)
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifacts the Architect needs; numeric threshold: '>= N scout signals present'>"
            # NOT "done" / "complete" / "proceed" (WRONG C-04: execution state)

  # ---- Architect+PM Phase: Design -- commit to a concrete approach ----
  # Architect+PM own; gate captures what engineering needs before validation
  # Stage name: use "design" or "proposal" -- NOT "draft" (WRONG C-06: namespace as label)
  # review:* requires draft:spec -- this zone MUST precede the Validation phase (C-05)

    - name: "<design-phase-label>"          # e.g. "design", "proposal"; NOT "draft" (WRONG C-06)
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifacts engineers need; confirm no blocking feasibility gaps>"
            # NOT "spec written" / "complete" (WRONG C-04: execution state)

  # ---- Engineering Phase: Validation -- review, prove, simulate, trace ----
  # Engineering owns; review:* requires draft:spec | flow:*/trace:* require review:*
  # Stage name: use "expert-review" or "validation" -- NOT "review" (WRONG C-06: namespace as label)

    - name: "<expert-review-phase-label>"   # e.g. "expert-review", "validation"; NOT "review" (WRONG C-06)
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"
            # NOT "reviews complete" (WRONG C-04: execution state)

    - name: "<simulation-phase-or-remove>"  # optional; remove if flow/trace not needed; NOT "flow" (WRONG C-06)
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ---- Team Phase: Synthesis -- listen ahead, close the loop ----
  # Full team owns; runs after engineering validation
  # Stage name: use "feedback-preview" or "synthesis" -- NOT "listen" (WRONG C-06: namespace as label)

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"; NOT "listen" (WRONG C-06)
      skills:
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- required, always last, do not move ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here (WRONG C-02 if violated)
      auto: true      # REQUIRED: must be present and true (WRONG C-02 if missing)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03)
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04)
- [ ] Namespace dependency order preserved: scout before draft, draft before review, review before flow/trace (C-05)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (C-06)
- [ ] Plan-identity comment preserved at top of YAML (C-07)
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`) (C-08)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags covering both essential AND recommended criteria (C-19)

---

## V-02 -- Per-Zone Dependency Constraint Reminder at Skill Position (C-20 axis)

**Axis**: Lifecycle emphasis -- dependency constraint reminders are placed at the skill-list placeholder line itself, not just at the zone header comment.
**Hypothesis**: A dependency note in a zone header fires when the model enters the zone but is separated from the decision it constrains (which skills to pick). A reminder placed directly before or at the `skills:` placeholder fires at the exact authoring moment -- when the model is choosing which skills to list for that zone. Moving the reminder from header to skill-list position makes a dependency violation feel wrong locally, without needing to carry the zone-header rule across multiple template fields. C-20 PASS. No recommended-criterion error artifacts (C-19 FAIL by design; zone headers don't constitute error artifacts); no correction table bridges (C-21 FAIL by design). Base structure is R4 V-02 (arc-zone structure with per-zone FAIL/PASS gate examples).

Expected gains: C-20 PASS (all dependency-bearing zones carry an explicit prerequisite statement at the skill-list placeholder position).
Expected gaps: C-19 FAIL (zone headers note dependencies but no error artifact covers recommended criteria), C-21 FAIL (no correction table).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence zones, each gated on what the next zone needs.
Skills remain independently runnable. The plan does not execute skills and carries no
automation authority. Its product is the gate: a shared agreement on what artifacts must
exist before advancing.

---

You are running `/program:plan` for topic **{{topic}}**.

**Namespace dependency order** (stages must respect this sequence):
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`.
`listen:*` requires at least one prior flow, trace, or review signal to synthesize.
At least one non-echo gate must contain a numeric threshold: `">= 2 scout signals present"`
or `"0 P0 findings open"`.

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

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ==== Zone: Discovery (scout / prove:websearch / prove:intelligence) ====
  # Goal: establish what we know about the space before designing
  # No upstream artifact dependency -- discovery is the breadth-first anchor
  #
  # FAIL gate: "research done"
  #   Why: execution state -- names what was done, not what must exist
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
  #   Why: artifact names + numeric threshold -- verifiable by the Architect before drafting

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"; NOT "scout"
      # No upstream dependency for this zone -- scout is the first layer
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  #
  # FAIL gate: "spec written"
  #   Why: past-tense action, not an evidence state -- cannot be verified without asking the author
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
  #   Why: artifact name present -- engineering can check the archive before starting review

    - name: "<design-phase-label>"          # e.g. "design", "proposal"; NOT "draft"
      # NOTE: review:* requires draft:spec -- this zone must produce draft:spec before Validation begins
      skills:                               # requires: scout signals from Discovery zone to exist
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact-referencing condition; confirm Architect reviewed for blocking gaps>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design; review:* requires draft:spec from Zone: Design
  #
  # FAIL gate: "reviews complete"
  #   Why: execution state -- "complete" is not checkable by the next phase owner
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"
  #   Why: named artifacts + quantified threshold -- synthesis team can verify before starting

    - name: "<validation-phase-label>"      # e.g. "expert-review", "validation"; NOT "review"
      # PREREQUISITE: review:* requires draft:spec artifact from Zone: Design
      # Do not place review:* skills here unless draft:spec was produced in a prior stage
      skills:                               # requires: draft:spec artifact from Design zone
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove this zone if flow/trace signals are not needed for {{topic}}
  # flow:* and trace:* require review:* artifacts from Zone: Validation
  #
  # FAIL gate: "simulation done"
  #   Why: execution state -- names what was run, not what exists
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
  #   Why: artifact names present -- checkable before synthesis begins

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed
      # PREREQUISITE: flow:* and trace:* require review:design (or equivalent) from Zone: Validation
      # Do not include flow:* or trace:* unless the Validation zone ran review:* first
      skills:                               # requires: review:* artifact from Validation zone
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # listen:* and topic:* synthesize prior signals -- requires at least one flow/trace or review signal
  #
  # FAIL gate: "synthesis done"
  #   Why: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
  #   Why: artifact names + checkable condition

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"; NOT "listen"
      # PREREQUISITE: listen:* requires at least one prior flow, trace, review, or prove signal
      # Do not place listen:* or topic:* before all simulation/validation zones are gated
      skills:                               # requires: at least one flow/trace or review artifact from prior zones
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen/topic artifacts present; no critical blockers>"

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty
      auto: true      # REQUIRED: must be present and true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names
- [ ] Every non-echo gate expresses evidence state -- not execution state
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries a `PREREQUISITE:` comment at the `skills:` line

---

## V-03 -- Correction Table Scaffold Integration (C-21 axis)

**Axis**: Output format -- bidirectional coupling: the correction table exists (C-18), and the YAML template carries `# check correction table` at every field type the table covers (skill lists, gates, and stage names).
**Hypothesis**: A correction table consulted once before generation can be forgotten by the time the model fills field 12 of the template. Inline navigational bridges at each covered field type convert the table from a one-time read into an active reference loop: the table pulls the model in at document level, the template pushes the model back to the table at each decision point. C-21 PASS. No recommended-criterion error artifacts (C-19: the correction table has C-06 entries, so C-19 passes incidentally -- this is expected given C-06 entries were present in R4 V-03's table). No skill-position dependency reminders beyond what bridges provide (C-20 FAIL by design). Base structure is R4 V-03 (correction table with inertia-framing opening).

Expected gains: C-21 PASS (bridges at all three field types: skills, gates, stage names).
Expected gaps: C-20 FAIL (no inline skill-position dependency reminders), but C-19 expected PASS incidentally via C-06 correction table entries.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases. Skills remain independently runnable.
The plan does not execute skills and carries no automation authority. Its entire value is
the gate: a shared agreement on what artifacts must exist before the next phase begins.

---

You are running `/program:plan` for topic **{{topic}}**.

**Before you generate -- consult this correction table:**

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "scout-feasibility artifact present; >= 2 signals reviewed"` | C-04 |
| `gate: "all skills complete"` | `gate: "review-design and prove-prototype artifacts present"` | C-04 |
| `gate: "phase complete"` | `gate: "draft-spec artifact present; 0 blocking feasibility concerns"` | C-04 |
| `gate: "proceed"` | `gate: "flow-lifecycle and trace-contract artifacts present; no P0 gaps"` | C-04 |
| `gate: "synthesis done"` | `gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"` | C-04 |
| `- scout:analysis` (invented name) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `- plan:create` (invented) | `- program:plan` | C-03 |
| `name: scout` (namespace as label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: draft` (namespace as label) | `name: design` or `name: proposal` | C-06 |
| `name: review` (namespace as label) | `name: expert-review` or `name: validation` | C-06 |
| `name: stage1` or `name: step-2` | `name: expert-review` or `name: simulation` | C-06 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |

Consult this table before filling each `gate:`, `name:`, and `skills:` field.

---

**The inertia pattern -- what most teams produce today:**

```yaml
# WRONG: everything in one stage, flat gate, dependency order violated
program:
  topic: "{{topic}}"
  stages:
    - name: "all-work"
      skills:
        - scout:feasibility
        - review:design       # cannot review a spec that does not exist yet
        - flow:lifecycle      # cannot simulate before review
        - listen:feedback
      gate: "done"
    - name: echo
      skills: []
      auto: true
```

Problems: dependency order violated (`review:*` before `draft:spec`); gate is execution state;
no arc structure -- one stage does everything. Check the correction table for each wrong field.

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc, artifact-referencing gates, dependency order preserved
program:
  topic: "{{topic}}"
  stages:

  # Layer 1: Breadth -- establish what we know
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      gate: "scout-feasibility, scout-requirements, and scout-competitors artifacts present;
             >= 2 scout signals reviewed; no blocking feasibility concerns"

  # Layer 2: Depth -- design, validate, simulate
    - name: design
      skills:
        - draft:spec
        - draft:proposal
      gate: "draft-spec artifact present; Architect confirmed no blocking gaps"

    - name: expert-review
      skills:
        - review:design
        - review:users
        - prove:prototype
      gate: "review-design, review-users, prove-prototype artifacts present; 0 P0 findings open"

  # Layer 3: Synthesis -- listen ahead, close the loop
    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: echo
      skills: []
      auto: true
```

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
At least one gate must be quantified: `">= 2 scout signals"` or `"0 P0 findings open"`.

**Signal skill catalog** (consult correction table above before picking any skill name):

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

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal>"

  stages:

  # ---- Layer 1: Breadth (scout / prove:websearch / prove:intelligence) ----

    - name: "<breadth-phase-label>"         # check correction table: stage names -- NOT "scout"
      skills:                               # check correction table: skill names
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N signals present'>"
                                            # check correction table: gates -- NOT "done" / "complete"

  # ---- Layer 2: Depth (draft / review / prove / flow / trace) ----
  # review:* requires draft:spec | flow:*/trace:* require review:* | prove:* before flow/trace

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" / "stage1"
      skills:                               # check correction table: skill names
        - draft:<skill>
      gate: "<artifact-referencing condition>"
                                            # check correction table: gates -- NOT "proceed" / "complete"

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review"
      skills:                               # check correction table: skill names
        - review:<skill>
        - prove:<skill>
      gate: "<review/prove artifacts present; at least one numeric threshold across the plan>"
                                            # check correction table: gates

    - name: "<simulation-phase-or-remove>"  # check correction table: stage names; optional -- remove if flow/trace not needed
      skills:                               # check correction table: skill names
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"
                                            # check correction table: gates

  # ---- Layer 3: Synthesis (listen / topic) ----

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" / "topic"
      skills:                               # check correction table: skill names
        - listen:<skill>
        - topic:<skill>
      gate: "<all prior signals archived; listen signal present>"
                                            # check correction table: gates

  # ---- Final Stage: echo ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- check correction table (C-02)
      auto: true      # REQUIRED: must be present and true -- check correction table (C-02)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (check correction table)
- [ ] Every non-echo gate expresses evidence state -- not execution state (check correction table)
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (check correction table)
- [ ] Three arc-layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved
- [ ] Every `name:`, `skills:`, and `gate:` field in the template carried a `# check correction table` annotation

---

## V-04 -- Cross-Tier Errors + Skill-Position Dependency Reminders (C-19 + C-20)

**Axes**: Inertia framing (C-19 cross-tier error coverage) + Lifecycle emphasis (C-20 skill-position dependency reminders) combined.
**Hypothesis**: Comprehensive error coverage (recommended criteria visible in BAD YAML) and skill-position dependency reminders attack two independent failure modes simultaneously: (1) the model generates wrong stage names or out-of-order namespaces because it never saw a concrete example of those failures; (2) the model places `review:*` before `draft:spec` because the dependency constraint was in the zone header, not at the skills field. Combining both should raise C-05 compliance (fewer dependency violations) and produce richer stage names and plan identity. C-19 PASS, C-20 PASS. No correction table bridges (C-21 FAIL by design). Base structure is R4 V-04 (criterion-tagged BAD block + per-zone FAIL/PASS gate contrast).

Expected gains: C-19 PASS, C-20 PASS.
Expected gaps: C-21 FAIL (no correction table scaffold bridges).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
listed here still run standalone -- the plan does not execute them, does not advance stages,
and carries no automation authority. This identity is the plan's value: it tells you what
evidence must exist before handing off, not what to run. A plan without gates is a list.
A plan that frames stages as execution steps (C-07) has lost the distinction.

---

You are running `/program:plan` for topic **{{topic}}**.

**The wrong plan -- covering all seven criteria (essential + recommended):**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity marker -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery" or "market-scan"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- use scout:requirements
        - review:design            # WRONG C-05: review:design before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution-state gate -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:spec
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

Each `# WRONG C-NN` tag names the criterion. Recommended-criterion failures (C-05, C-06, C-07)
are as concrete here as essential-criterion failures (C-02, C-03, C-04).

**The gated plan -- what to build:**

```yaml
# GOOD: three-layer evidence arc, criterion-compliant, dependency order preserved
program:
  topic: "{{topic}}"
  stages:
  # Layer 1: Breadth
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
      gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
  # Layer 2: Depth
    - name: design
      skills:
        - draft:spec
      gate: "draft-spec artifact present; no blocking feasibility gaps"
    - name: expert-review
      skills:
        - review:design
        - prove:prototype
      gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"
  # Layer 3: Synthesis
    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"
    - name: echo
      skills: []
      auto: true
```

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

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ==== Zone: Discovery (scout / prove:websearch / prove:intelligence) ====
  # Goal: establish what we know about the space before designing
  # No upstream artifact dependency -- Discovery is the breadth-first anchor zone
  #
  # FAIL gate: "research done"              <-- WRONG C-04: execution state, names no artifact
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"

    - name: "<discovery-phase-label>"       # NOT "scout" -- WRONG C-06: namespace as stage label
      # No upstream dependency for this zone -- scout:* is the first layer
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # This zone produces draft:spec, which review:* and flow:*/trace:* require in later zones
  #
  # FAIL gate: "spec done"                  <-- WRONG C-04: execution state
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"

    - name: "<design-phase-label>"          # NOT "draft" -- WRONG C-06: namespace as stage label
      # PREREQUISITE: scout signals from Discovery zone should exist before committing to a design
      skills:                               # requires: sufficient scout signal from Discovery zone
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact condition; at least ONE gate across the full plan must be quantified>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design; review:* requires draft:spec from Zone: Design
  #
  # FAIL gate: "reviews complete"           <-- WRONG C-04: execution state
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"

    - name: "<validation-phase-label>"      # NOT "review" -- WRONG C-06: namespace as stage label
      # PREREQUISITE: review:* requires draft:spec artifact from Zone: Design
      # Do NOT list review:* skills here unless draft:spec was produced in a prior stage (WRONG C-05 if violated)
      skills:                               # requires: draft:spec artifact from Design zone
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed; requires review:* from Zone: Validation
  #
  # FAIL gate: "simulation done"            <-- WRONG C-04: execution state
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed; NOT "flow" -- WRONG C-06
      # PREREQUISITE: flow:* and trace:* require review:design (or equivalent) from Zone: Validation
      # Do NOT list flow:* or trace:* without a prior review:* zone (WRONG C-05 if violated)
      skills:                               # requires: review:* artifact from Validation zone
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  #
  # FAIL gate: "synthesis done"             <-- WRONG C-04: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: "<synthesis-phase-label>"       # NOT "listen" -- WRONG C-06: namespace as stage label
      # PREREQUISITE: listen:* requires at least one prior flow, trace, review, or prove signal
      # Do NOT place listen:* or topic:* before all validation/simulation zones are gated (WRONG C-05 if violated)
      skills:                               # requires: at least one flow/trace or review artifact from prior zones
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)

    - name: echo
      skills: []      # REQUIRED: empty -- adding skills violates C-02
      auto: true      # REQUIRED: must be present and true -- missing violates C-02
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03)
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04)
- [ ] Namespace dependency order preserved: scout before draft, draft before review, review before flow/trace (C-05)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (C-06)
- [ ] Plan-identity REQUIRED comment preserved at top of YAML (C-07)
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example (C-17)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags covering both essential AND recommended criteria (C-19)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries a `PREREQUISITE:` comment at the `skills:` line (C-20)

---

## V-05 -- Golden Synthesis (all 21 criteria)

**Axes**: All three new criteria (C-19 + C-20 + C-21) combined with the best R4 foundation
(arc-as-spine from R3 V-01, deletion-resistance from R3 V-02, plan-level criterion-tagged BAD
YAML block from R4 V-01, per-zone FAIL/PASS gate contrast from R4 V-02, correction table from
R4 V-03, full lifecycle phase emphasis from R4 V-01, plan-identity framing from throughout).
**Hypothesis**: A prompt that (1) opens with a comprehensive correction table covering essential
AND recommended criteria (C-18 + C-19), (2) follows with a criterion-tagged BAD PLAN block
covering C-02/C-03/C-04/C-05/C-06/C-07 (C-16 + C-19), (3) provides a GOOD plan example, (4)
embeds the arc as structural section headers each carrying per-zone FAIL/PASS gate examples
(C-13 + C-17) AND per-zone PREREQUISITE reminders at skill-list positions (C-20), (5) pre-
positions the output template with REQUIRED annotations on all structural slots (C-11 + C-14),
plan-identity comment (C-07 + C-12), and `# check correction table` bridges at all three field
types (C-21), and (6) closes with the Plan Verification checklist, saturates all 21 v5 criteria.

Expected gains: C-19 PASS (comprehensive cross-tier coverage), C-20 PASS (skill-position dep
reminders at all dependency-bearing zones), C-21 PASS (correction table bridges at all three
field types: skills, gates, stage names).
Expected overall: all 21 criteria pass. Golden candidate.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
listed here still run standalone -- the plan does not execute them, does not advance stages,
and carries no automation authority. This identity is the plan's value: it tells you what
evidence must exist before handing off to the next phase, not what to run. A plan without
gates is a list. A plan that frames stages as execution steps is an executor (C-07). The
gate is everything.

---

You are running `/program:plan` for topic **{{topic}}**.

**Before you generate -- consult this correction table:**

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "scout-feasibility artifact present; >= 2 signals reviewed"` | C-04 |
| `gate: "all skills complete"` | `gate: "review-design and prove-prototype artifacts present"` | C-04 |
| `gate: "phase complete"` | `gate: "draft-spec artifact present; 0 blocking feasibility concerns"` | C-04 |
| `gate: "proceed"` | `gate: "flow-lifecycle and trace-contract artifacts present; no P0 gaps"` | C-04 |
| `gate: "synthesis done"` | `gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"` | C-04 |
| `- scout:analysis` (invented name) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `name: scout` (namespace as label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: draft` (namespace as label) | `name: design` or `name: proposal` | C-06 |
| `name: review` (namespace as label) | `name: expert-review` or `name: validation` | C-06 |
| `name: stage1` | `name: expert-review` or `name: simulation` | C-06 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |
| `review:design` before `draft:spec` exists | `draft:spec` in a prior stage; `review:design` after | C-05 |
| `flow:lifecycle` before any `review:*` | `review:*` in a prior stage; `flow:*` after | C-05 |
| No plan-identity comment; stages read as task list | Add `# REQUIRED: ... plan, not an executor` at top | C-07 |

Consult this table before filling each `gate:`, `name:`, and `skills:` field.

---

**The wrong plan -- a complete bad example covering all seven criteria (essential + recommended):**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity marker -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- use scout:requirements
        - draft:spec
        - review:design            # WRONG C-05: review:design before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution-state gate -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:proposal
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

Each `# WRONG C-NN` tag names the criterion violated. Check the correction table above for
the fix. Recommended-criterion failures (C-05, C-06, C-07) are equally concrete here.

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc, all 21 criteria satisfied
program:
  topic: "{{topic}}"
  stages:

  # Layer 1: Breadth -- establish what we know before designing
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      gate: "scout-feasibility, scout-requirements, and scout-competitors artifacts present;
             >= 2 scout signals reviewed by PM; no blocking feasibility concerns"

  # Layer 2: Depth -- design, validate, simulate
    - name: design
      skills:
        - draft:spec
        - draft:proposal
      gate: "draft-spec artifact present; Architect confirmed no blocking gaps"

    - name: expert-review
      skills:
        - review:design
        - review:users
        - prove:prototype
      gate: "review-design, review-users, prove-prototype artifacts present; 0 P0 findings open"

  # Layer 3: Synthesis -- listen ahead, close the loop
    - name: feedback-preview
      skills:
        - listen:feedback
        - listen:adoption
      gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: echo
      skills: []
      auto: true
```

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog** (consult correction table before picking any skill name):

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

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ==== Zone: Discovery (scout / prove:websearch / prove:intelligence) ====
  # Goal: establish what we know about the space before designing
  # No upstream artifact dependency -- Discovery is the first breadth layer
  #
  # FAIL gate: "research done"              <-- WRONG C-04: execution state, names no artifact
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"

    - name: "<discovery-phase-label>"       # check correction table: stage names -- NOT "scout" (WRONG C-06)
      # No upstream dependency for this zone -- scout:* is the first layer
      skills:                               # check correction table: skill names
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"
                                            # check correction table: gates -- NOT "done" / "complete" (WRONG C-04)

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # This zone produces draft:spec -- required artifact for all review:* and flow:*/trace:* zones
  #
  # FAIL gate: "spec done"                  <-- WRONG C-04: execution state
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" (WRONG C-06)
      # PREREQUISITE: scout signals from Discovery zone should exist before committing to a design
      skills:                               # check correction table: skill names; requires: scout signal from Discovery
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact condition; at least ONE gate across the full plan must be quantified>"
                                            # check correction table: gates -- NOT "proceed" (WRONG C-04)

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design; requires draft:spec from Zone: Design
  #
  # FAIL gate: "reviews complete"           <-- WRONG C-04: execution state
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review" (WRONG C-06)
      # PREREQUISITE: review:* requires draft:spec artifact from Zone: Design
      # Do NOT list review:* skills unless draft:spec was produced in a prior stage (WRONG C-05 if violated)
      skills:                               # check correction table: skill names; requires: draft:spec from Design zone
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"
                                            # check correction table: gates -- NOT "complete" (WRONG C-04)

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed for {{topic}}; requires review:* from Zone: Validation
  #
  # FAIL gate: "simulation done"            <-- WRONG C-04: execution state
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"

    - name: "<simulation-phase-or-remove>"  # check correction table: stage names; optional -- remove if not needed; NOT "flow" (WRONG C-06)
      # PREREQUISITE: flow:* and trace:* require review:design (or equivalent) from Zone: Validation
      # Do NOT include flow:*/trace:* without a prior review:* zone (WRONG C-05 if violated)
      skills:                               # check correction table: skill names; requires: review:* artifact from Validation zone
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"
                                            # check correction table: gates

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  #
  # FAIL gate: "synthesis done"             <-- WRONG C-04: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" (WRONG C-06)
      # PREREQUISITE: listen:* requires at least one prior flow, trace, review, or prove signal to synthesize
      # Do NOT place listen:*/topic:* before all validation zones are gated (WRONG C-05 if violated)
      skills:                               # check correction table: skill names; requires: flow/trace or review artifact from prior zones
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen/topic artifacts present; all prior signals archived; no critical blockers>"
                                            # check correction table: gates

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here; check correction table (C-02)
      auto: true      # REQUIRED: must be present and true; check correction table (C-02)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03); check correction table
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04); check correction table
- [ ] Namespace dependency order preserved: scout before draft, draft before review, review before flow/trace (C-05)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top of YAML (C-07)
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`) (C-08)
- [ ] Evidence arc visible in stage sequencing: breadth (Discovery) → depth (Design/Validation/Simulation) → synthesis (Synthesis) (C-09)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags on each wrong field (C-16)
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example (C-17)
- [ ] Correction table present with >= 3 pairs covering C-02/C-03/C-04/C-05/C-06/C-07 (C-18)
- [ ] Error artifacts (BAD PLAN block + correction table) cover recommended criteria C-05, C-06, C-07 alongside essential criteria (C-19)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries a `PREREQUISITE:` comment at the `skills:` line (C-20)
- [ ] Every `name:`, `skills:`, and `gate:` field in the template carries a `# check correction table` annotation (C-21)
