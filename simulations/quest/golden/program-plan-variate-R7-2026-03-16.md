---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 7
rubric: v7
aspirational_target: C-25, C-26, C-27
---

# program-plan -- R7 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v7 (C-01 through C-27, 27 criteria, 190 pts max, golden = all essential pass AND composite >= 80).

---

## R6 Retrospective Under v7 Rubric

Three new aspirational criteria (C-25, C-26, C-27) extracted from R6 excellence signals.
Retroactively scoring R6 top variations against v7:

| Variation | C-25 gate contrast rationale (Why:) | C-26 criterion-tagged structural gates | C-27 uniform dep syntax | v7 est. |
|-----------|--------------------------------------|---------------------------------------|------------------------|---------|
| V-01 (triple-artifact C-22) | FAIL -- per-zone contrast via zone-comment annotations; no Why: rationale | FAIL -- no structural gate fields (C-24 FAIL) | FAIL -- mixed dep phrasings at zone headers | ~130 |
| V-02 (dual-position C-23) | PASS -- `# FAIL gate: "..." Why: ...` / `# PASS gate: "..." Why: ...` at all five non-echo zones | FAIL -- comment-based contrast; no gate_fail: fields to tag (C-24 FAIL) | PASS -- `# requires: <artifact> from Zone: <name> (C-05)` uniformly at both positions | ~145 |
| V-03 (structural gates C-24) | FAIL -- gate_fail:/gate_pass: fields present; no Why: rationale | FAIL -- gate_fail: fields present but no `# WRONG C-04` at field position | FAIL -- zone-header dep reminders only; skills-line absent (C-23 FAIL) | ~140 |
| V-04 (C-22 + C-23) | FAIL -- FAIL/PASS contrast in zone-header comments; no Why: | FAIL -- no structural gate fields | PASS -- uniform `# requires:` format at both positions | ~145 |
| V-05 (C-22 + C-23 + C-24, golden) | FAIL -- gate_fail:/gate_pass: fields present; no Why: | FAIL -- gate_fail: fields lack `# WRONG C-04` at field position | FAIL -- skills-line mixes `# check correction table: skill names; requires:` preamble, breaking uniformity | ~175 |

Diagnosis:
- C-25 (Why: rationale): Only R6 V-02 passed -- comment-based per-zone Why: is the proof of concept;
  structural gate fields (V-03, V-05) never received Why: annotations.
- C-26 (criterion-tagged structural gates): No R6 variation passed -- gate_fail: fields existed in
  V-03/V-05 but lacked `# WRONG C-04` inline at the field; tag was only in the BAD PLAN block.
- C-27 (uniform dep syntax): R6 V-02 and V-04 were close but Synthesis zone used "at least one
  flow/trace or review artifact from prior zones" -- natural-language variation breaks uniformity.
  V-05's skills-line mixed `# check correction table: skill names; requires:` preamble, different
  from the zone-header `# requires:` form.

Single-axis: V-01 (C-25), V-02 (C-26), V-03 (C-27)
Combined: V-04 (C-25 + C-26), V-05 (all three, golden)

---

## V-01 -- Gate Contrast Rationale Annotation (C-25 axis)

**Axis**: Role sequence -- per-zone FAIL and PASS gate examples each carry explicit `Why:` explanations
at the zone header, stating WHY the FAIL form violates C-04 and WHY the PASS form satisfies it.

**Hypothesis**: R6 V-02 earned C-25 via comment-based per-zone Why: rationale. A clean single-axis
test isolates that signal: does adding Why: to per-zone FAIL/PASS examples (without structural gate
fields, without criterion-tagged fields) improve gate correctness independently? The Why: converts
contrast from shape-teaching ("here is wrong; here is right") to principle-teaching ("here is wrong
BECAUSE X; here is right BECAUSE Y"). C-25 PASS (all five non-echo zones carry Why: for both FAIL
and PASS). No structural gate fields (C-24 FAIL by design). No `# WRONG C-04` at gate field positions
(C-26 FAIL by design -- no structural fields to tag). Dependency syntax uses consistent `# requires:`
form (C-23 PASS as side effect of R6 V-02 base), but explicit uniformity enforcement of C-27 not
attempted -- some natural-language variation permitted (C-27 FAIL or PARTIAL).

Expected gains: C-25 PASS (all five non-echo zones carry Why: rationale for both FAIL and PASS).
Expected gaps: C-18 FAIL (no correction table), C-21 FAIL (no table bridges), C-24 FAIL (comment
contrast only), C-26 FAIL (no structural fields), C-27 FAIL (mixed phrasings).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills remain
independently runnable. The plan does not execute skills, does not advance stages, and carries no
automation authority. Its entire value is the gate: a shared agreement on what artifacts must exist
before the next phase begins.

---

You are running `/program:plan` for topic **{{topic}}**.

**Namespace dependency order** (stages must respect this sequence):
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`.
`listen:*` requires at least one prior flow, trace, or review signal.
At least one non-echo gate must contain a numeric threshold.

**The wrong plan -- every failure tagged:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- use scout:requirements
        - review:design            # WRONG C-05: review:design before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution state -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:spec
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

**Signal skill catalog:**

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch
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
  # requires: (none) -- Discovery is the upstream anchor; no prior artifact needed (C-05)
  #
  # FAIL gate: "research done"
  #   Why: execution state -- names what was done, not what artifact must exist;
  #        a gate-checker verifying readiness cannot inspect "research done" against any file (C-04)
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
  #   Why: names specific artifacts + numeric threshold -- verifiable by checking artifact list
  #        before advancing, without consulting execution history (C-04)

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"; NOT "scout" (WRONG C-06)
      # requires: (none) -- Discovery is the first layer (C-05)
      skills:                               # no prerequisite artifact for Discovery zone
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # requires: scout signals from Zone: Discovery (C-05)
  #
  # FAIL gate: "spec done"
  #   Why: execution state -- "done" is a process record, not an artifact name;
  #        the Validation team cannot verify "spec done" against any inspectable file (C-04)
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
  #   Why: names the artifact + a team-checkable condition; engineering can confirm draft-spec
  #        file exists and feasibility is clear before starting review (C-04)

    - name: "<design-phase-label>"          # e.g. "design", "proposal"; NOT "draft" (WRONG C-06)
      # requires: scout signals from Zone: Discovery (C-05)
      skills:                               # requires: scout signals from Zone: Discovery (C-05)
        - draft:<skill>                     # spec, proposal, or pitch
                                            # review:* cannot appear here; draft:spec must exist first (C-05)
      gate: "<artifact condition; confirm Architect reviewed for blocking gaps>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design
  # requires: draft:spec artifact from Zone: Design (C-05)
  #
  # FAIL gate: "reviews complete"
  #   Why: execution state -- "complete" records that review ran, not what artifacts exist;
  #        "reviews complete" may refer to Jira ticket state, not an inspectable file (C-04)
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"
  #   Why: names two specific artifacts + quantified threshold -- the Synthesis team can verify
  #        both by artifact inspection before advancing (C-04)

    - name: "<validation-phase-label>"      # e.g. "expert-review", "validation"; NOT "review" (WRONG C-06)
      # requires: draft:spec artifact from Zone: Design (C-05)
      skills:                               # requires: draft:spec artifact from Zone: Design (C-05)
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove this zone if flow/trace signals are not needed for {{topic}}
  # requires: review:design artifact from Zone: Validation (C-05)
  #
  # FAIL gate: "simulation done"
  #   Why: execution state -- names a run event, not a file; a post-simulation checker cannot
  #        verify "simulation done" without knowing which artifact files were produced (C-04)
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
  #   Why: names specific artifacts + condition -- Synthesis can list files before advancing (C-04)

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed; NOT "flow" (WRONG C-06)
      # requires: review:design artifact from Zone: Validation (C-05)
      skills:                               # requires: review:design artifact from Zone: Validation (C-05)
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # requires: at least one flow/trace or review artifact from prior zones (C-05)
  #
  # FAIL gate: "synthesis done"
  #   Why: execution state -- "done" records a step completion; echo cannot verify "synthesis done"
  #        as a file or evidence state -- there is no artifact named "synthesis done" (C-04)
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
  #   Why: names two listen artifacts + adoption condition -- verifiable by artifact inspection
  #        before closing the evidence loop (C-04)

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"; NOT "listen" (WRONG C-06)
      # requires: at least one flow/trace or review artifact from prior zones (C-05)
      skills:                               # requires: flow/trace or review artifact from prior zones (C-05)
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here (WRONG C-02 if violated)
      auto: true      # REQUIRED: must be present and true (WRONG C-02 if missing)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03)
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04)
- [ ] Namespace dependency order preserved: scout before draft, draft before review, review before flow/trace (C-05)
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06)
- [ ] Plan-identity REQUIRED comment preserved at top (C-07)
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags on C-05, C-06, AND C-07 alongside essential criteria (C-22 via BAD block)
- [ ] Every non-echo zone comment includes FAIL gate, PASS gate, AND `Why:` rationale for both FAIL and PASS (C-25)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries `# requires:` at BOTH zone-header comment AND skills-line (C-23)

---

## V-02 -- Criterion-Tagged Structural Gate Values (C-26 axis)

**Axis**: Output format -- structural gate-contrast fields (`gate_fail:` / `gate_pass:` / `gate:` as
actual YAML keys in each non-echo zone) where each `gate_fail:` field carries an inline `# WRONG C-04`
criterion-reference tag at the field position itself -- not only in the BAD PLAN block.

**Hypothesis**: R6 V-03 used `gate_fail:` structural fields (C-24 PASS) but the `# WRONG C-04` tag
appeared only in the BAD PLAN block, not at the `gate_fail:` field. A model resolving the structural
`gate_fail:` field encounters the wrong shape structurally but must look elsewhere for the criterion
mapping. Placing `# WRONG C-04` inline at the `gate_fail:` field makes the criterion tag and the
wrong shape coincide at one atomic location -- no cross-document lookup required. C-26 PASS. No Why:
rationale (C-25 FAIL by design -- single axis on C-26). No dual-position dep reminders beyond zone
headers (C-23 PARTIAL -- as in R6 V-03 base). C-27 absent (dep syntax not uniformized). Correction
table present (C-18, C-21 via `# check correction table` bridges). Full recommended BAD block
coverage (C-22).

Expected gains: C-26 PASS (every `gate_fail:` field carries `# WRONG C-04` at field position).
Expected gaps: C-23 PARTIAL (zone-header dep reminders; skills-line placement incomplete), C-25 FAIL
(no Why: rationale), C-27 FAIL (dep syntax not uniformized).

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
| `gate: "synthesis done"` | `gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"` | C-04 |
| `- scout:analysis` (invented) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `name: scout` (namespace label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: draft` (namespace label) | `name: design` or `name: proposal` | C-06 |
| `name: review` (namespace label) | `name: expert-review` or `name: validation` | C-06 |
| `name: stage1` (generic index) | `name: expert-review` or `name: simulation` | C-06 |
| `review:design` before `draft:spec` | `draft:spec` in a prior stage; `review:design` after | C-05 |
| `flow:lifecycle` before any `review:*` | `review:*` in a prior stage; `flow:*` after | C-05 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |
| No plan-identity comment at top | Add `# REQUIRED: ...plan, not an executor` | C-07 |

Consult this table before filling each `gate:`, `name:`, and `skills:` field.

---

**The wrong plan -- all seven criteria tagged:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: invented skill name -- use scout:requirements
        - review:design            # WRONG C-05: review:design before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution state -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:spec
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog** (consult correction table before picking any skill name):

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output. Each non-echo zone contains `gate_fail:` / `gate_pass:` / `gate:`
as YAML sibling keys. Each `gate_fail:` carries `# WRONG C-04` inline at the field. Write your
`gate:` value using `gate_pass:` as the model. In your final output, collapse each triple to a
single `gate:` scalar (delete `gate_fail:` and `gate_pass:` lines). Reproduce the REQUIRED comment
and Plan Verification section verbatim.**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"                     # check correction table
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ---- Layer 1: Breadth (scout / prove:websearch / prove:intelligence) ----
  # review:*/flow:*/trace:*/listen:* must appear in LATER zones -- C-05

    - name: "<breadth-phase-label>"         # check correction table: stage names -- NOT "scout" (WRONG C-06)
      # No upstream dependency -- Discovery is the first zone (C-05)
      skills:                               # check correction table: skill names
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate_fail: "research done"            # WRONG C-04: execution state -- do not copy
      gate_pass: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
      gate: "<fill in: use gate_pass as model; include numeric threshold; delete gate_fail/gate_pass>"
                                            # check correction table: gates

  # ---- Layer 2: Design (draft) ----
  # review:* requires draft:spec | dependency order: C-05

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" (WRONG C-06)
      # review:* cannot appear here -- draft:spec does not exist yet (C-05)
      skills:                               # check correction table: skill names
        - draft:<skill>                     # spec, proposal, or pitch
      gate_fail: "spec done"               # WRONG C-04: execution state -- do not copy
      gate_pass: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
                                            # check correction table: gates

  # ---- Layer 2: Validation (review / prove) ----
  # requires draft:spec from Design | flow:*/trace:* must appear AFTER this zone (C-05)

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review" (WRONG C-06)
      # review:* requires draft:spec from Design; do not place review:* before Design zone (C-05)
      skills:                               # check correction table: skill names; requires draft:spec (C-05)
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate_fail: "reviews complete"         # WRONG C-04: execution state -- do not copy
      gate_pass: "review-design and prove-prototype artifacts present; 0 P0 findings open"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
                                            # check correction table: gates

  # ---- Layer 2: Simulation (flow / trace) -- OPTIONAL ----
  # requires review:* from Validation | remove if not needed (C-05)

    - name: "<simulation-phase-or-remove>"  # optional; NOT "flow" (WRONG C-06); check correction table
      # flow:*/trace:* require review:* from Validation; do not place before Validation zone (C-05)
      skills:                               # check correction table: skill names; requires review:* (C-05)
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate_fail: "simulation done"          # WRONG C-04: execution state -- do not copy
      gate_pass: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
                                            # check correction table: gates

  # ---- Layer 3: Synthesis (listen / topic) ----

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" (WRONG C-06)
      # listen:*/topic:* require at least one prior flow/trace or review signal (C-05)
      skills:                               # check correction table: skill names; requires prior signals (C-05)
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate_fail: "synthesis done"           # WRONG C-04: execution state -- do not copy
      gate_pass: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
                                            # check correction table: gates

  # ---- Final Stage: echo ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here; check correction table (C-02)
      auto: true      # REQUIRED: must be present and true; check correction table (C-02)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03); check correction table
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04); check correction table
- [ ] Namespace dependency order preserved (C-05); check correction table
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top (C-07); check correction table
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Three arc-layer section comments (Layer 1: Breadth / Layer 2: Design+Validation+Simulation / Layer 3: Synthesis) preserved (C-13)
- [ ] Every `name:`, `skills:`, and `gate:` field carries a `# check correction table` annotation (C-21)
- [ ] BAD PLAN block covers C-05, C-06, AND C-07 alongside essential criteria (C-22)
- [ ] Every `gate_fail:` field carries `# WRONG C-04` inline at the field position (C-26)

---

## V-03 -- Uniform Dependency Reminder Syntax (C-27 axis)

**Axis**: Phrasing register -- all dependency constraint reminders, at every position (zone-header
and skills-line) for every dependency-bearing zone, use exactly `# requires: <artifact> from Zone:
<name> (C-05)`. The form is machine-recognizable as a structured signal; no zone uses a different
phrasing. Zones share only the artifact name and zone name as substitution variables.

**Hypothesis**: R6 V-02 and V-04 used `# requires:` at many positions but Synthesis zone used "at
least one flow/trace or review artifact from prior zones" -- natural-language variation breaks
uniformity. R6 V-05's skills-line mixed `# check correction table: skill names; requires: ...`
prefix preamble, making it structurally different from the zone-header form. True C-27 compliance
means EVERY dep reminder at EVERY position is `# requires: <artifact> from Zone: <name> (C-05)`,
with correction table reference as a separate comment if needed. C-27 PASS (all four dep-bearing
zones, both positions, same form). C-23 PASS as prerequisite. No structural gate fields (C-24 FAIL
-- single axis). No Why: rationale (C-25 FAIL). No criterion-tagged fields (C-26 FAIL). Correction
table present (C-18 PASS). Full recommended BAD block coverage (C-22 PASS).

Expected gains: C-27 PASS (uniform `# requires: <artifact> from Zone: <name> (C-05)` at all
positions across all four dependent zones).
Expected gaps: C-24 FAIL (comment-based contrast), C-25 FAIL (no Why:), C-26 FAIL.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
listed here still run standalone -- the plan does not execute them, does not advance stages,
and carries no automation authority. This identity is the plan's value: it tells you what
evidence must exist before handing off, not what to run. A plan that frames stages as
execution steps (C-07) has lost the distinction.

---

You are running `/program:plan` for topic **{{topic}}**.

**Before you generate -- consult this correction table (all seven criteria):**

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "scout-feasibility artifact present; >= 2 signals reviewed"` | C-04 |
| `gate: "all skills complete"` | `gate: "review-design and prove-prototype artifacts present"` | C-04 |
| `gate: "phase complete"` | `gate: "draft-spec artifact present; 0 blocking feasibility concerns"` | C-04 |
| `gate: "synthesis done"` | `gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"` | C-04 |
| `- scout:analysis` (invented) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `name: scout` (namespace label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: draft` (namespace label) | `name: design` or `name: proposal` | C-06 |
| `name: review` (namespace label) | `name: expert-review` or `name: validation` | C-06 |
| `name: stage1` (generic index) | `name: expert-review` or `name: simulation` | C-06 |
| `review:design` before `draft:spec` | `draft:spec` in a prior stage; `review:design` after | C-05 |
| `flow:lifecycle` before any `review:*` | `review:*` in a prior stage; `flow:*` after | C-05 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |
| No plan-identity comment; stages read as task list | Add `# REQUIRED: ...plan, not an executor` at top | C-07 |

---

**The wrong plan -- all seven criteria tagged:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- use scout:requirements
        - review:design            # WRONG C-05: review:design before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution state -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:spec
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog:**

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output -- fill all `<...>` placeholders; reproduce all REQUIRED
comments and the Plan Verification section verbatim. Every `# requires:` annotation uses
exactly the form `# requires: <artifact> from Zone: <name> (C-05)` at both the zone-header
comment and the `skills:` line -- do not rephrase or combine with other annotation prefixes.**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ==== Zone: Discovery (scout / prove:websearch / prove:intelligence) ====
  # Goal: establish what we know about the space before designing
  # requires: (none) -- Discovery is the upstream anchor (C-05)
  #
  # FAIL gate: "research done"  -- WRONG C-04: execution state
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"

    - name: "<discovery-phase-label>"       # e.g. "discovery"; NOT "scout" (WRONG C-06)
      # requires: (none) -- Discovery is the upstream anchor (C-05)
      skills:  # requires: (none) -- Discovery is the upstream anchor (C-05)
               # check correction table: skill names
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"
                                            # check correction table: gates

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # requires: scout-feasibility artifact from Zone: Discovery (C-05)
  #
  # FAIL gate: "spec done"  -- WRONG C-04: execution state
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"

    - name: "<design-phase-label>"          # e.g. "design"; NOT "draft" (WRONG C-06)
      # requires: scout-feasibility artifact from Zone: Discovery (C-05)
      skills:  # requires: scout-feasibility artifact from Zone: Discovery (C-05)
               # check correction table: skill names
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact condition; confirm Architect reviewed for blocking gaps>"
                                            # check correction table: gates

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design
  # requires: draft-spec artifact from Zone: Design (C-05)
  #
  # FAIL gate: "reviews complete"  -- WRONG C-04: execution state
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"

    - name: "<validation-phase-label>"      # e.g. "expert-review"; NOT "review" (WRONG C-06)
      # requires: draft-spec artifact from Zone: Design (C-05)
      skills:  # requires: draft-spec artifact from Zone: Design (C-05)
               # check correction table: skill names
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"
                                            # check correction table: gates

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove this zone if flow/trace signals are not needed for {{topic}}
  # requires: review-design artifact from Zone: Validation (C-05)
  #
  # FAIL gate: "simulation done"  -- WRONG C-04: execution state
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"

    - name: "<simulation-phase-or-remove>"  # optional; NOT "flow" (WRONG C-06)
      # requires: review-design artifact from Zone: Validation (C-05)
      skills:  # requires: review-design artifact from Zone: Validation (C-05)
               # check correction table: skill names
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"
                                            # check correction table: gates

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # requires: flow-lifecycle artifact from Zone: Simulation (C-05)
  #
  # FAIL gate: "synthesis done"  -- WRONG C-04: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: "<synthesis-phase-label>"       # e.g. "synthesis"; NOT "listen" (WRONG C-06)
      # requires: flow-lifecycle artifact from Zone: Simulation (C-05)
      skills:  # requires: flow-lifecycle artifact from Zone: Simulation (C-05)
               # check correction table: skill names
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"
                                            # check correction table: gates

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here (WRONG C-02 if violated)
      auto: true      # REQUIRED: must be present and true (WRONG C-02 if missing)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03)
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04)
- [ ] Namespace dependency order preserved (C-05)
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06)
- [ ] Plan-identity REQUIRED comment preserved at top (C-07)
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Correction table present with C-02/C-03/C-04/C-05/C-06/C-07 rows (C-18)
- [ ] BAD PLAN block covers C-05, C-06, AND C-07 alongside essential criteria (C-22)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries `# requires: <artifact> from Zone: <name> (C-05)` at BOTH the zone-header comment AND the `skills:` line, in exactly that syntactic form and no other (C-27 satisfying C-23)

---

## V-04 -- Gate Rationale + Criterion-Tagged Structural Fields (C-25 + C-26)

**Axes**: Lifecycle emphasis (C-25 Why: rationale) + Output format (C-26 criterion-tagged structural
gate fields). Structural gate fields (C-24) are the prerequisite for C-26.

**Hypothesis**: C-25 and C-26 are gate-teaching complements -- C-25 explains WHY a gate form is
wrong (principle-teaching via rationale), C-26 names WHICH criterion it violates (criterion-reference
co-located with the wrong shape in the YAML skeleton). R6 V-02 achieved C-25 via comment-based Why:
but had no structural fields (C-26 impossible). R6 V-03 had structural gate fields (C-24 PASS) but
no Why: or `# WRONG C-04`. Combining both creates maximum gate-teaching density at the structural
field position: wrong shape (`gate_fail:`) + which criterion (`# WRONG C-04`) + Why: this is wrong
(rationale comment) + correct shape (`gate_pass:`) + Why: this is right -- all co-located in the
YAML skeleton. C-24 PASS, C-25 PASS, C-26 PASS. C-27 not attempted (dep syntax allowed to vary --
single combined axis on gate quality). Correction table present (C-18, C-21). Full recommended BAD
block coverage (C-22).

Expected gains: C-24 PASS, C-25 PASS (Why: at every gate_fail:/gate_pass: pair across all zones),
C-26 PASS (`# WRONG C-04` at every gate_fail: field position).
Expected gaps: C-23 PARTIAL (zone-header dep reminders; skills-line inconsistent), C-27 FAIL (dep
syntax not uniformized by design).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
remain independently runnable. The plan does not execute skills and carries no automation
authority. Its entire value is the gate: a shared agreement on what artifacts must exist
before the next phase begins.

---

You are running `/program:plan` for topic **{{topic}}**.

**Before you generate -- consult this correction table (all seven criteria):**

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "scout-feasibility artifact present; >= 2 signals reviewed"` | C-04 |
| `gate: "all skills complete"` | `gate: "review-design and prove-prototype artifacts present"` | C-04 |
| `gate: "phase complete"` | `gate: "draft-spec artifact present; 0 blocking feasibility concerns"` | C-04 |
| `gate: "synthesis done"` | `gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"` | C-04 |
| `- scout:analysis` (invented) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `name: scout` (namespace label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: draft` (namespace label) | `name: design` or `name: proposal` | C-06 |
| `name: review` (namespace label) | `name: expert-review` or `name: validation` | C-06 |
| `name: stage1` (generic index) | `name: expert-review` or `name: simulation` | C-06 |
| `review:design` before `draft:spec` | `draft:spec` in a prior stage; `review:design` after | C-05 |
| `flow:lifecycle` before any `review:*` | `review:*` in a prior stage; `flow:*` after | C-05 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |
| No plan-identity comment; stages read as task list | Add `# REQUIRED: ...plan, not an executor` at top | C-07 |

Consult this table before filling each `gate:`, `name:`, and `skills:` field.

---

**The wrong plan -- all seven criteria tagged:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- use scout:requirements
        - review:design            # WRONG C-05: review:design before draft:spec -- dependency violated
      gate: "done"                 # WRONG C-04: execution state -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:spec
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog** (consult correction table before picking any skill name):

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output. Each non-echo zone has `gate_fail:` / `gate_pass:` / `gate:` as
YAML sibling keys. Each `gate_fail:` carries `# WRONG C-04` and is followed by a `# Why FAIL:`
comment. Each `gate_pass:` is followed by a `# Why PASS:` comment. Write your `gate:` value using
`gate_pass:` as the model. In your final output, collapse each triple to a single `gate:` scalar
(delete `gate_fail:`, `gate_pass:`, and their Why: lines). Reproduce the REQUIRED comment and Plan
Verification section verbatim.**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"                     # check correction table
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ---- Zone: Discovery ----
  # No upstream dependency -- first evidence layer (C-05)

    - name: "<discovery-phase-label>"       # check correction table: stage names -- NOT "scout" (WRONG C-06)
      # No upstream dependency required -- Discovery is the first zone (C-05)
      skills:                               # check correction table: skill names
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate_fail: "research done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "research done" names a past action, not an artifact; a gate-checker verifying
      #           readiness cannot inspect "research done" against any file or evidence state (C-04)
      gate_pass: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
      # Why PASS: names specific artifacts + numeric threshold -- verifiable by inspecting artifact
      #           list before advancing, without consulting execution history (C-04)
      gate: "<fill in: use gate_pass as model; include numeric threshold; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates

  # ---- Zone: Design ----
  # draft:spec must be produced here before review:* can run (C-05)

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" (WRONG C-06)
      # review:* cannot appear here -- draft:spec does not exist yet (C-05)
      skills:                               # check correction table: skill names
        - draft:<skill>                     # spec, proposal, or pitch
      gate_fail: "spec done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "spec done" is a process record; the Validation team cannot verify "spec done"
      #           by inspecting a file -- only "draft-spec artifact present" is checkable (C-04)
      gate_pass: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
      # Why PASS: names the artifact + a team-checkable condition; Validation can confirm both
      #           before starting review:design (C-04)
      gate: "<fill in: use gate_pass as model; at least ONE gate across the full plan must be quantified>"
                                            # check correction table: gates

  # ---- Zone: Validation ----
  # requires draft:spec from Design zone (C-05)

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review" (WRONG C-06)
      # review:* requires draft:spec -- do NOT place review:* before Design zone (C-05)
      skills:                               # check correction table: skill names; requires draft:spec (C-05)
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate_fail: "reviews complete"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "reviews complete" records execution, not artifact existence; "complete" may refer
      #           to ticket state -- the Synthesis team cannot check it against actual files (C-04)
      gate_pass: "review-design and prove-prototype artifacts present; 0 P0 findings open"
      # Why PASS: names two specific artifacts + quantified threshold (0 P0 findings); both are
      #           verifiable by artifact inspection before advancing (C-04)
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates

  # ---- Zone: Simulation -- OPTIONAL ----
  # Remove if flow/trace signals not needed; requires review:* from Validation (C-05)

    - name: "<simulation-phase-or-remove>"  # optional; NOT "flow" (WRONG C-06); check correction table
      # flow:*/trace:* require review:* -- do NOT place before Validation zone (C-05)
      skills:                               # check correction table: skill names; requires review:* (C-05)
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate_fail: "simulation done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "simulation done" names a run event; the Synthesis team cannot verify it without
      #           knowing which artifact files were produced by the simulation run (C-04)
      gate_pass: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
      # Why PASS: names specific artifacts + condition; Synthesis can list generated files before
      #           advancing (C-04)
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates

  # ---- Zone: Synthesis ----
  # requires at least one flow/trace or review signal from prior zones (C-05)

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" (WRONG C-06)
      # listen:*/topic:* require prior flow/trace or review signal -- do NOT place before Validation (C-05)
      skills:                               # check correction table: skill names; requires prior signals (C-05)
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate_fail: "synthesis done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "synthesis done" records a step completion; echo cannot verify it as a file
      #           or evidence state -- there is no artifact named "synthesis done" (C-04)
      gate_pass: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
      # Why PASS: names two listen artifacts + adoption condition; verifiable by artifact inspection
      #           before closing the evidence loop (C-04)
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates

  # ---- Final Stage: echo ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here; check correction table (C-02)
      auto: true      # REQUIRED: must be present and true; check correction table (C-02)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03); check correction table
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04); check correction table
- [ ] Namespace dependency order preserved (C-05); check correction table
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top (C-07); check correction table
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Correction table present with C-02/C-03/C-04/C-05/C-06/C-07 rows (C-18); all field types bridged (C-21)
- [ ] BAD PLAN block covers C-05, C-06, AND C-07 alongside essential criteria (C-22)
- [ ] Every non-echo zone had `gate_fail:` / `gate_pass:` / `gate:` as YAML sibling fields (C-24)
- [ ] Every `gate_fail:` and `gate_pass:` field carries a `# Why FAIL:` / `# Why PASS:` explanation (C-25)
- [ ] Every `gate_fail:` field carries `# WRONG C-04` inline at the field position (C-26)

---

## V-05 -- Golden Synthesis (all 27 criteria)

**Axes**: All three new criteria (C-25 + C-26 + C-27) combined with the full R6 V-05 foundation
(C-01 through C-24).

**Hypothesis**: A prompt that stacks:
(1) All three recommended criteria in both the BAD PLAN block and correction table (C-22)
(2) Dual-position dependency reminders at BOTH zone-header AND skills-line in uniform form (C-23)
(3) Structural YAML gate-contrast fields -- `gate_fail:` / `gate_pass:` / `gate:` (C-24)
(4) `# Why FAIL:` / `# Why PASS:` rationale at every gate_fail:/gate_pass: pair (C-25)
(5) `# WRONG C-04` inline at every `gate_fail:` field position (C-26)
(6) `# requires: <artifact> from Zone: <name> (C-05)` uniformly at zone-header AND skills-line
    for all four dependency-bearing zones, with no variation in form (C-27)
-- on the complete R6 V-05 baseline (C-01 through C-21 addressed) --
saturates all 27 v7 criteria.

C-25 PASS: `# Why FAIL:` / `# Why PASS:` rationale at all five non-echo zones.
C-26 PASS: `# WRONG C-04` inline at every `gate_fail:` field position across all five zones.
C-27 PASS: `# requires: <artifact> from Zone: <name> (C-05)` uniformly at zone-header AND
  skills-line for all four dependent zones -- Design, Validation, Simulation, Synthesis.
Expected overall: all 27 criteria pass. Golden candidate.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
listed here still run standalone -- the plan does not execute them, does not advance stages,
and carries no automation authority. This identity is the plan's value: it tells you what
evidence must exist before handing off, not what to run. A plan without gates is a list.
A plan that frames stages as execution steps is an executor (C-07). The gate is everything.

---

You are running `/program:plan` for topic **{{topic}}**.

**Before you generate -- consult this correction table (all seven criteria):**

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "scout-feasibility artifact present; >= 2 signals reviewed"` | C-04 |
| `gate: "all skills complete"` | `gate: "review-design and prove-prototype artifacts present"` | C-04 |
| `gate: "phase complete"` | `gate: "draft-spec artifact present; 0 blocking feasibility concerns"` | C-04 |
| `gate: "proceed"` | `gate: "flow-lifecycle and trace-contract artifacts present; no P0 gaps"` | C-04 |
| `gate: "synthesis done"` | `gate: "listen-feedback and listen-adoption artifacts present; no critical blockers"` | C-04 |
| `- scout:analysis` (invented) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `- plan:create` (invented) | `- program:plan` | C-03 |
| `name: scout` (namespace label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: draft` (namespace label) | `name: design` or `name: proposal` | C-06 |
| `name: review` (namespace label) | `name: expert-review` or `name: validation` | C-06 |
| `name: stage1` or `name: step-2` | `name: expert-review` or `name: simulation` | C-06 |
| `review:design` before `draft:spec` | `draft:spec` in a prior stage; `review:design` after | C-05 |
| `flow:lifecycle` before any `review:*` | `review:*` in a prior stage; `flow:*` after | C-05 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |
| No plan-identity comment; stages read as task list | Add `# REQUIRED: ...plan, not an executor` at top | C-07 |

Consult this table before filling each `gate:`, `name:`, and `skills:` field.

---

**The wrong plan -- all seven criteria tagged (essential + recommended):**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- reads as an executor; add REQUIRED comment at top
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- use scout:requirements
        - draft:spec
        - review:design            # WRONG C-05: review:design in same stage as draft:spec -- must follow in a later stage
      gate: "done"                 # WRONG C-04: execution state -- names no artifact
    - name: draft                  # WRONG C-06: namespace name -- use "design" or "proposal"
      skills:
        - draft:proposal
      gate: "complete"             # WRONG C-04: execution state
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

Each `# WRONG C-NN` tag names the criterion violated. Recommended-criterion failures (C-05,
C-06, C-07) are as concrete here as essential failures. Check the correction table for each fix.

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog** (consult correction table before picking any skill name):

- **scout**: feasibility, market, competitors, requirements, compliance, positioning, naming, stakeholders
- **draft**: spec, proposal, pitch
- **review**: design, users, customers, code
- **flow**: conversation, dataflow, lifecycle, resilience, throttle, trigger
- **trace**: component, contract, deployment, migration, permissions, request, skill, state
- **prove**: analysis, hypothesis, intelligence, interview, prototype, publish, synthesize, websearch
- **listen**: adoption, feedback, support
- **program**: plan
- **topic**: echo, new, plan, report, status, story

---

**Produce the following output. Each non-echo zone contains `gate_fail:` / `gate_pass:` / `gate:`
as YAML sibling keys. Each `gate_fail:` carries `# WRONG C-04` and is followed by a `# Why FAIL:`
comment. Each `gate_pass:` is followed by a `# Why PASS:` comment. Every `# requires:` annotation
uses exactly `# requires: <artifact> from Zone: <name> (C-05)` at both the zone-header comment and
the `skills:` line -- do not rephrase or prefix with other text. Write your `gate:` value using
`gate_pass:` as the model. In your final output, collapse each triple to a single `gate:` scalar
(delete `gate_fail:`, `gate_pass:`, and their Why: lines). Reproduce the REQUIRED comment and Plan
Verification section verbatim.**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"                     # check correction table
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ==== Zone: Discovery (scout / prove:websearch / prove:intelligence) ====
  # Goal: establish what we know about the space before designing
  # requires: (none) -- Discovery is the upstream anchor (C-05)

    - name: "<discovery-phase-label>"       # check correction table: stage names -- NOT "scout" (WRONG C-06)
      # requires: (none) -- Discovery is the upstream anchor (C-05)
      skills:  # requires: (none) -- Discovery is the upstream anchor (C-05)
               # check correction table: skill names
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate_fail: "research done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "research done" names a past action, not an artifact; a gate-checker cannot
      #           inspect "research done" against any file or evidence state (C-04)
      gate_pass: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
      # Why PASS: names specific artifacts + numeric threshold -- verifiable by artifact inspection
      #           before committing to design, without consulting execution history (C-04)
      gate: "<fill in: use gate_pass as model; include numeric threshold; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates -- NOT "done" (WRONG C-04)

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # requires: scout-feasibility artifact from Zone: Discovery (C-05)

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" (WRONG C-06)
      # requires: scout-feasibility artifact from Zone: Discovery (C-05)
      skills:  # requires: scout-feasibility artifact from Zone: Discovery (C-05)
               # check correction table: skill names
        - draft:<skill>                     # spec, proposal, or pitch
      gate_fail: "spec done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "spec done" is a process record; the Validation team cannot verify "spec done"
      #           by inspecting a file -- only "draft-spec artifact present" is checkable (C-04)
      gate_pass: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
      # Why PASS: names the artifact + a team-checkable condition; Validation can confirm both
      #           before starting review:design (C-04)
      gate: "<fill in: use gate_pass as model; at least ONE gate across the full plan must be quantified>"
                                            # check correction table: gates -- NOT "proceed" (WRONG C-04)

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design
  # requires: draft-spec artifact from Zone: Design (C-05)

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review" (WRONG C-06)
      # requires: draft-spec artifact from Zone: Design (C-05)
      # Do NOT list review:* skills unless draft:spec was produced in a prior stage (WRONG C-05)
      skills:  # requires: draft-spec artifact from Zone: Design (C-05)
               # check correction table: skill names
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate_fail: "reviews complete"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "reviews complete" records execution, not artifact existence; "complete" may refer
      #           to ticket state -- Synthesis cannot check it against actual files (C-04)
      gate_pass: "review-design and prove-prototype artifacts present; 0 P0 findings open"
      # Why PASS: names two specific artifacts + quantified threshold (0 P0); both verifiable by
      #           artifact inspection before advancing to listen:* skills (C-04)
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates -- NOT "complete" (WRONG C-04)

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed for {{topic}}
  # requires: review-design artifact from Zone: Validation (C-05)

    - name: "<simulation-phase-or-remove>"  # optional; NOT "flow" (WRONG C-06); check correction table
      # requires: review-design artifact from Zone: Validation (C-05)
      # Do NOT include flow:*/trace:* without a prior review:* zone (WRONG C-05)
      skills:  # requires: review-design artifact from Zone: Validation (C-05)
               # check correction table: skill names
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate_fail: "simulation done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "simulation done" names a run event; Synthesis cannot verify it without knowing
      #           which artifact files the simulation produced (C-04)
      gate_pass: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
      # Why PASS: names specific artifacts + condition -- Synthesis can list generated files
      #           before advancing (C-04)
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass and Why lines>"
                                            # check correction table: gates

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # requires: flow-lifecycle artifact from Zone: Simulation (C-05)

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" (WRONG C-06)
      # requires: flow-lifecycle artifact from Zone: Simulation (C-05)
      # Do NOT place listen:*/topic:* before all validation zones are gated (WRONG C-05)
      skills:  # requires: flow-lifecycle artifact from Zone: Simulation (C-05)
               # check correction table: skill names
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate_fail: "synthesis done"  # WRONG C-04: execution state -- check correction table
      # Why FAIL: "synthesis done" records a step completion; echo cannot verify it as a file
      #           or evidence state -- no artifact is named "synthesis done" (C-04)
      gate_pass: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
      # Why PASS: names two listen artifacts + adoption condition -- verifiable by artifact
      #           inspection before closing the evidence loop (C-04)
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass and Why lines>"
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
- [ ] Namespace dependency order preserved (C-05); check correction table
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top (C-07); check correction table
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Correction table present with C-02/C-03/C-04/C-05/C-06/C-07 rows (C-18); all field types bridged (C-21)
- [ ] BAD PLAN block covers C-05, C-06, AND C-07 alongside essential criteria (C-22 via BAD block)
- [ ] Correction table contains C-05 rows AND C-07 row alongside C-06 rows (C-22 via table)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries `# requires: <artifact> from Zone: <name> (C-05)` at BOTH the zone-header comment AND the `skills:` line, in exactly that syntactic form (C-23 + C-27)
- [ ] Every non-echo zone had `gate_fail:` / `gate_pass:` / `gate:` as YAML sibling fields (C-24)
- [ ] Every `gate_fail:` and `gate_pass:` field carries a `# Why FAIL:` / `# Why PASS:` explanation (C-25)
- [ ] Every `gate_fail:` field carries `# WRONG C-04` inline at the field position (C-26)
