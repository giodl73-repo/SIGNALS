---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 4
rubric: v4
aspirational_target: C-16, C-17, C-18
---

# program-plan -- R4 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v4 (C-01 through C-18, 18 criteria, 145 pts max, golden = all essential pass AND composite >= 80).

---

## R3 Retrospective Under v4 Rubric

Three new aspirational criteria (C-16, C-17, C-18) were extracted from R3 excellence signals.
Retroactively scoring R3 top variations against v4:

| Variation | C-16 criterion-tagged errors | C-17 per-zone gate contrast | C-18 correction table | v4 composite |
|-----------|------------------------------|-----------------------------|-----------------------|--------------|
| V-01 (arc-as-spine) | FAIL -- no criterion tags on PASS/FAIL examples | PASS -- every zone header carries both FAIL and PASS gate example | FAIL -- no correction table | ~95 |
| V-02 (full deletion-resistance) | FAIL -- no criterion tags | FAIL -- no per-zone contrast | FAIL -- no table | ~90 |
| V-03 (plan-level YAML error block) | PASS -- BAD PLAN block tags each wrong field with `# WRONG C-NN` | FAIL -- one central contrast, no per-zone repetition | PASS -- correction table with 9 pairs covering C-02/C-03/C-04/C-06 | ~108 |
| V-04 (arc-spine + deletion-resistance) | FAIL -- no criterion tags | PASS -- zone headers carry FAIL/PASS per zone | FAIL -- no table | ~118 |
| V-05 (all three axes, golden) | FAIL -- BAD PLAN block has no criterion tags | PARTIAL -- per-zone contrast in some zones but not all | FAIL -- no correction table | ~105 |

**R3 V-04 retroactively scores highest under v4** due to its arc-spine structure (C-13),
full deletion-resistance annotations (C-14), plan-level YAML error block (C-15), and
per-zone gate contrast (C-17). Its gap is C-16 (criterion tags absent) and C-18 (no table).

**R3 V-03 is the second-highest scorer** because it added C-16 (criterion-tagged BAD YAML)
and C-18 (correction table) despite weaker C-13/C-14 coverage. The pattern: each variate
excels on its target axis but leaves two of the three new criteria unsatisfied.

**R4 target**: all five variations achieve at least one new criterion. Three single-axis
variations isolate C-16, C-17, C-18. Two combined variations target pairs and the full set.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Criterion-referenced error tagging | Every error in BAD YAML carries `# WRONG C-NN` tag | Does tagging errors to specific criteria (C-16) improve model understanding of WHY examples fail, without changing the underlying structure? |
| Per-zone gate contrast | Every arc zone header has its own inline FAIL / PASS gate example | Does embedding PASS/FAIL at each authoring decision point (C-17) eliminate the attention gap better than a single central contrast section? |
| Correction table | A structured pre-generation lookup mapping wrong forms to correct forms | Does a reference table (C-18) that the model consults BEFORE generating reduce errors more than illustration-format examples alone? |
| Criterion tags + per-zone contrast | C-16 + C-17 combined | Can dual annotation (tags on errors + per-zone PASS/FAIL) coexist without overcrowding the template? |
| Golden synthesis | C-16 + C-17 + C-18 on best R3 foundation | Does combining all three with R3 V-04's arc-spine, deletion-resistance, and plan-level YAML error block saturate all 18 criteria? |

Single-axis: V-01 (criterion-referenced tagging), V-02 (per-zone gate contrast), V-03 (correction table)
Combined: V-04 (criterion tags + per-zone contrast), V-05 (all three new axes, golden)

---

## V-01 -- Criterion-Referenced Error Tagging (C-16 axis)

**Axis**: Criterion-referenced error tagging -- every wrong field in the BAD PLAN block carries an explicit `# WRONG C-NN` tag identifying which criterion it violates.
**Hypothesis**: Tagging each wrong example to its specific criterion (`# WRONG C-04`,
`# WRONG C-03`) lets the model understand WHY the example fails, not just THAT it fails.
The criterion tag creates a direct semantic link from each wrong output shape to the rubric
requirement it violates. C-16 PASS. Per-zone contrast is absent (C-17 FAIL by design);
no correction table (C-18 FAIL by design). Base structure is R3 V-04 (role sequence +
lifecycle emphasis + deletion-resistance), which was the highest R3 scorer.

Expected gains: C-16 PASS.
Expected gaps: C-17 FAIL (no per-zone contrast), C-18 FAIL (no table).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into role-owned phases, each gated on artifacts the next role needs
before starting work. Skills remain independently runnable. The program does not execute skills,
does not advance stages, and carries no automation authority. Its entire value is the gate:
a shared definition of what must be true before handoff.

---

You are running `/program:plan` for topic **{{topic}}**.

**The wrong plan -- understand what you are replacing:**

```yaml
# BAD PLAN: fails all four essential criteria

program:
  topic: "{{topic}}"
  stages:
    - name: scout                  # WRONG C-06: namespace name reused as stage label
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" is an invented skill name
        - draft:spec
        - review:design            # WRONG C-05: review before draft:spec can exist -- dependency violated
      gate: "done"                 # WRONG C-04: execution-state gate -- names no artifact
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

Each `# WRONG C-NN` tag identifies the specific criterion each wrong field violates.
This plan fails all four essential criteria (C-01 through C-04).

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
(`review:*` requires `draft:spec` -- this is C-05 namespace dependency order.)

**Phase 3 -- Engineering: Validation**
*Goal*: stress-test the design against real-world signals.
Review, prove, flow, and trace skills run here. Review skills require the spec from Phase 2.
*Gate guidance*: `"review-design and prove-prototype artifacts present; 0 P0 findings open"`.
At least one gate across the plan must include a numeric threshold (C-08).

**Phase 4 -- Team: Synthesis**
*Goal*: listen ahead and close the evidence loop.
*Gate guidance*: `"listen-feedback and listen-adoption artifacts present; no critical adoption blockers"`.

**Echo** (auto): always last. `name: echo`, `skills: []`, `auto: true`. The echo contract is C-02.

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`.
`prove:*` belongs in or before the review/prove layer, not after flow/trace.

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

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal>"

  stages:

  # ---- PM Phase: Discovery -- what we need to know before designing ----
  # PM owns; gate captures what the Architect needs before drafting

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifacts the Architect needs; numeric threshold: '>= N scout signals present'>"

  # ---- Architect+PM Phase: Design -- commit to a concrete approach ----
  # Architect+PM own; gate captures what engineering needs before validation

    - name: "<design-phase-label>"          # e.g. "design", "proposal"
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifacts engineers need; Architect confirmed no blocking feasibility gaps>"

  # ---- Engineering Phase: Validation -- review, prove, simulate, trace ----
  # Engineering owns; review:* requires draft:spec | prove:* here | flow:*/trace:* last in layer

    - name: "<expert-review-phase-label>"   # e.g. "expert-review", "validation"
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

    - name: "<simulation-phase-or-remove>"  # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ---- Team Phase: Synthesis -- listen ahead, close the loop ----
  # Full team owns; runs after engineering validation

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"
      skills:
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo -- required, always last, do not move ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here
      auto: true      # REQUIRED: must be present and true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state -- not execution state
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels (not namespace names, not generic indices)
- [ ] Four role-phase comments (PM / Architect+PM / Engineering / Team) preserved in YAML

---

## V-02 -- Per-Zone Gate Contrast (C-17 axis)

**Axis**: Per-zone gate contrast -- every arc zone header carries its own inline FAIL / PASS
gate example, not just a central contrast section.
**Hypothesis**: Embedding a PASS/FAIL gate example at every arc zone removes the attention
gap between the central contrast section and the gate field being authored. When a model
reaches zone N's gate field, it has already seen zone N's own PASS/FAIL example -- it does
not need to remember a lesson from a section three pages back. C-17 PASS. No criterion tags
on the examples (C-16 FAIL by design); no correction table (C-18 FAIL by design). Base
structure is R3 V-01 (arc-as-spine with zone headers), which earned C-13/C-17 naturally.

Expected gains: C-17 PASS (all non-echo zones carry FAIL + PASS examples).
Expected gaps: C-16 FAIL (no criterion tags), C-18 FAIL (no table).

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
  #
  # FAIL gate: "research done"
  #   Why: execution state -- names what was done, not what must exist
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
  #   Why: artifact names + numeric threshold -- verifiable by the Architect before drafting

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"; NOT "scout"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # NOTE: review:* requires draft:spec -- design zone must precede all validation zones
  #
  # FAIL gate: "spec written"
  #   Why: past-tense action, not an evidence state -- cannot be verified without asking the author
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
  #   Why: artifact name present -- engineering can check the archive before starting review

    - name: "<design-phase-label>"          # e.g. "design", "proposal"; NOT "draft"
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact-referencing condition; confirm Architect reviewed for blocking gaps>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design; requires draft:spec from Zone: Design
  #
  # FAIL gate: "reviews complete"
  #   Why: execution state -- "complete" is not checkable by the next phase owner
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"
  #   Why: named artifacts + quantified threshold -- synthesis team can verify before starting

    - name: "<validation-phase-label>"      # e.g. "expert-review", "validation"; NOT "review"
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove this zone if flow/trace signals are not needed for {{topic}}
  # Requires review:* artifacts from Zone: Validation
  #
  # FAIL gate: "simulation done"
  #   Why: execution state -- names what was run, not what exists
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
  #   Why: artifact names present -- checkable before synthesis begins

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # Runs after all validation zones are gated
  #
  # FAIL gate: "synthesis done"
  #   Why: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
  #   Why: artifact names + checkable condition

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"; NOT "listen"
      skills:
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
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state -- not execution state
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels (not namespace names, not generic indices)
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example

---

## V-03 -- Correction Table (C-18 axis)

**Axis**: Correction table -- a structured pre-generation lookup mapping wrong forms to
correct forms, placed before the skill introduction.
**Hypothesis**: A correction table is consulted before generating rather than encountered
during error-checking. It enables active avoidance: the model checks the table before
filling each gate, skill, and name field, rather than pattern-matching from scattered inline
examples. C-18 PASS. No criterion tags on errors (C-16 FAIL by design); no per-zone contrast
(C-17 FAIL by design). Base structure is R3 V-03 (inertia-framing opening), which is a
natural fit for table-first presentation.

Expected gains: C-18 PASS (correction table with >= 3 pairs covering C-02/C-03/C-04/C-06).
Expected gaps: C-16 FAIL (no criterion tags), C-17 FAIL (no per-zone contrast).

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
| `- scout:analysis` (invented) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `name: scout` (namespace as label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: stage1` | `name: expert-review` or `name: validation` | C-06 |
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

Problems: dependency order violated (`review:*` before `draft:spec`); gate names no evidence;
no arc structure -- one stage does everything.

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

    - name: "<breadth-phase-label>"         # check correction table -- NOT "scout"
      skills:
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N signals present'>"
                                            # check correction table -- NOT "done" / "complete"

  # ---- Layer 2: Depth (draft / review / prove / flow / trace) ----
  # review:* requires draft:spec | flow:*/trace:* require review:* | prove:* before flow/trace

    - name: "<depth-phase-label>"           # check correction table -- NOT "draft" / "stage1"
      skills:
        - draft:<skill>
        - review:<skill>
        - prove:<skill>
      gate: "<artifact-referencing condition; at least one numeric threshold across the plan>"
                                            # check correction table -- NOT "proceed" / "complete"

    - name: "<simulation-phase-or-remove>"  # optional; remove if flow/trace not needed
      skills:
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present>"

  # ---- Layer 3: Synthesis (listen / topic) ----

    - name: "<synthesis-phase-label>"       # check correction table -- NOT "listen" / "topic"
      skills:
        - listen:<skill>
        - topic:<skill>
      gate: "<all prior signals archived; listen signal present>"

  # ---- Final Stage: echo ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- see correction table (C-02)
      auto: true      # REQUIRED: must be present and true -- see correction table (C-02)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names -- check correction table)
- [ ] Every non-echo gate expresses evidence state -- not execution state (check correction table)
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (check correction table)
- [ ] Three arc-layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved

---

## V-04 -- Criterion Tags + Per-Zone Contrast (C-16 + C-17 combined)

**Axes**: Criterion-referenced error tagging (C-16) + per-zone gate contrast (C-17) combined.
**Hypothesis**: Combining criterion tags on all errors with per-zone PASS/FAIL examples
creates a dual-reinforcement mechanism: the criterion tag at each error tells the model
WHICH requirement is violated; the per-zone PASS/FAIL at each zone tells the model WHAT
correct output looks like at the exact authoring moment. A model that ignores the central
BAD/GOOD section still encounters per-zone feedback; a model that skips the zone examples
still sees criterion-tagged inline errors. C-16 and C-17 should both PASS. No correction
table (C-18 FAIL by design). Base structure is R3 V-05 (golden, all 15 criteria), which
provides the strongest foundation.

Expected gains: C-16 PASS, C-17 PASS.
Expected gaps: C-18 FAIL (no table).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
remain independently runnable. The program does not execute skills, does not advance stages,
and carries no automation authority. Its entire value is the gate: a shared agreement on
what artifacts must exist before the next phase owner begins work.

---

You are running `/program:plan` for topic **{{topic}}**.

**The wrong plan -- a complete bad example:**

```yaml
# BAD PLAN: fails all four essential criteria

program:
  topic: "{{topic}}"
  stages:
    - name: scout                  # WRONG C-06: namespace name reused as stage label
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" is an invented skill name
        - draft:spec
        - review:design            # WRONG C-05: review before draft:spec can exist -- dependency violated
      gate: "done"                 # WRONG C-04: execution-state gate -- names no artifact
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

Each `# WRONG C-NN` tag identifies which criterion the wrong field violates.

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
  #
  # FAIL gate: "research done"              <-- WRONG C-04: execution state, names no artifact
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"

    - name: "<discovery-phase-label>"       # NOT "scout" -- WRONG C-06: namespace as stage label
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # review:* requires draft:spec -- this zone MUST precede all validation zones (C-05)
  #
  # FAIL gate: "spec done"                  <-- WRONG C-04: execution state
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"

    - name: "<design-phase-label>"          # NOT "draft" -- WRONG C-06: namespace as stage label
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact condition; at least ONE gate across the full plan must be quantified>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design; requires draft:spec from Zone: Design
  #
  # FAIL gate: "reviews complete"           <-- WRONG C-04: execution state
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"

    - name: "<validation-phase-label>"      # NOT "review" -- WRONG C-06: namespace as stage label
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed; requires review:* from Zone: Validation
  #
  # FAIL gate: "simulation done"            <-- WRONG C-04: execution state
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  #
  # FAIL gate: "synthesis done"             <-- WRONG C-04: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: "<synthesis-phase-label>"       # NOT "listen" -- WRONG C-06: namespace as stage label
      skills:
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

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names)
- [ ] Every non-echo gate expresses evidence state -- not execution state
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels (not namespace names, not generic indices)
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example
- [ ] BAD PLAN block carries `# WRONG C-NN` tags on each wrong field

---

## V-05 -- Golden Synthesis (all 18 criteria)

**Axes**: All three new criteria (C-16 + C-17 + C-18) combined with the best R3 foundation
(arc-as-spine from R3 V-01, deletion-resistance from R3 V-02, plan-level YAML error block
from R3 V-03, lifecycle emphasis from R3 V-04).
**Hypothesis**: A prompt that (1) opens with a correction table (C-18) consulted before
generation, (2) follows with a criterion-tagged BAD PLAN block (C-15 + C-16), (3) provides
a GOOD plan example, (4) pre-positions the output template with arc-zone section headers each
carrying FAIL/PASS gate examples (C-13 + C-17), REQUIRED annotations on all structural slots
(C-11 + C-14), and a `# REQUIRED: preserve` comment (C-07 + C-12), and (5) closes with the
pre-printed Plan Verification checklist (C-13), saturates all 18 v4 criteria in one body.

Expected gains: C-16 PASS, C-17 PASS, C-18 PASS.
Expected overall: all 18 criteria pass. Golden candidate.

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
listed here still run standalone -- the plan does not execute them, does not advance stages,
and carries no automation authority. This identity is the plan's value: it tells you what
evidence must exist before handing off to the next phase, not what to run. A plan without
gates is a list.

---

You are running `/program:plan` for topic **{{topic}}**.

**Before you generate -- consult this correction table:**

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "scout-feasibility artifact present; >= 2 signals reviewed"` | C-04 |
| `gate: "all skills complete"` | `gate: "review-design and prove-prototype artifacts present"` | C-04 |
| `gate: "phase complete"` | `gate: "draft-spec artifact present; 0 blocking feasibility concerns"` | C-04 |
| `gate: "proceed"` | `gate: "flow-lifecycle and trace-contract artifacts present; no P0 gaps"` | C-04 |
| `- scout:analysis` (invented name) | `- scout:feasibility` or `- scout:requirements` | C-03 |
| `- build:deploy` (invented namespace) | `- trace:deployment` | C-03 |
| `- review:architecture` (invented) | `- review:design` | C-03 |
| `name: scout` (namespace as label) | `name: discovery` or `name: market-scan` | C-06 |
| `name: stage1` | `name: expert-review` or `name: validation` | C-06 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |

---

**The wrong plan -- a complete bad example:**

```yaml
# BAD PLAN: fails all four essential criteria

program:
  topic: "{{topic}}"
  stages:
    - name: scout                  # WRONG C-06: namespace name reused as stage label
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist -- invented skill
        - draft:spec
        - review:design            # WRONG C-05: review:design requires draft:spec to exist first
      gate: "done"                 # WRONG C-04: execution-state gate -- names no artifact
    - name: echo
      skills:
        - listen:feedback          # WRONG C-02: echo must have empty skills list
      auto: true
```

Each `# WRONG C-NN` tag identifies the specific criterion each field violates. This plan
fails all four essentials. Check the correction table above for each wrong field's fix.

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc, criterion-compliant, dependency order preserved
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

Key distinctions from the bad pattern: skills ordered by dependency; each gate names
artifacts; one gate is quantified (`>= 2 scout signals`); three arc layers visible.

---

**Gate design rule**: For each stage, ask: *what must exist before the next phase owner
can begin their work?* The answer is your gate.

| Gate quality | Example | Passes? |
|-------------|---------|---------|
| Execution state | `"all scout complete"` | NO -- WRONG C-04 |
| Empty / vague | `"done"` | NO -- WRONG C-04 |
| Artifact-referencing | `"scout-feasibility and scout-requirements artifacts present"` | YES |
| Quantified (best) | `">= 2 scout signals present AND draft-spec artifact exists"` | YES + C-08 |

At least one gate must be quantified. Numeric thresholds make gates machine-checkable.

**Namespace dependency order:**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```
`review:*` requires `draft:spec`. `flow:*` and `trace:*` require `review:*`.

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

**Produce the following output exactly -- fill all `<...>` placeholders; reproduce all
REQUIRED comments and the Plan Verification section verbatim with each box checked:**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ==== Zone: Discovery (scout / prove:websearch / prove:intelligence) ====
  # Goal: establish what we know about the space before designing
  #
  # FAIL gate: "research done"              <-- WRONG C-04: execution state, names no artifact
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"
                                            # NOT "scout" -- see correction table (C-06)
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>                     # add/remove as topic warrants
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"
                                            # NOT "done" / "complete" -- see correction table (C-04)

    # Optional second discovery stage -- remove if not needed
    - name: "<discovery-2-or-remove>"
      skills:
        - prove:<skill>                     # websearch, intelligence, hypothesis
      gate: "<artifact condition>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # review:* requires draft:spec -- this zone MUST precede all validation zones (C-05)
  #
  # FAIL gate: "spec written"               <-- WRONG C-04: past-tense action, not evidence state
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"

    - name: "<design-phase-label>"          # e.g. "design", "proposal"
                                            # NOT "draft" -- see correction table (C-06)
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact condition; at least ONE gate across the full plan must be quantified (C-08)>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design; requires draft:spec from Zone: Design
  #
  # FAIL gate: "reviews complete"           <-- WRONG C-04: execution state
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"

    - name: "<validation-phase-label>"      # e.g. "expert-review", "validation"
                                            # NOT "review" -- see correction table (C-06)
      skills:
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed for {{topic}}; requires review:* from Zone: Validation
  #
  # FAIL gate: "simulation done"            <-- WRONG C-04: execution state
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed
      skills:
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # Runs after all validation zones are gated
  #
  # FAIL gate: "synthesis done"             <-- WRONG C-04: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"
                                            # NOT "listen" -- see correction table (C-06)
      skills:
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
  #           Violation is WRONG C-02 -- see correction table.

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here (WRONG C-02 if violated)
      auto: true      # REQUIRED: must be present and true (WRONG C-02 if missing)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo
- [ ] All skill names belong to Signal's 9 namespaces (no invented names -- check correction table)
- [ ] Every non-echo gate expresses evidence state -- not execution state (check correction table + zone FAIL examples)
- [ ] At least one non-echo gate contains a numeric threshold (e.g., `>= 2 scout signals`, `0 P0 findings`)
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (check correction table)
- [ ] Each zone comment includes both a FAIL and a PASS gate example
- [ ] BAD PLAN block carries `# WRONG C-NN` tags on each wrong field
- [ ] `# REQUIRED: preserve this comment` line preserved in YAML output

---

## Predicted v4 Scores

| Variation | C-16 criterion tags | C-17 per-zone contrast | C-18 correction table | Predicted v4 composite |
|-----------|---------------------|------------------------|----------------------|------------------------|
| V-01 (criterion tags) | PASS | FAIL | FAIL | ~120/145 |
| V-02 (per-zone contrast) | FAIL | PASS | FAIL | ~120/145 |
| V-03 (correction table) | FAIL | FAIL | PASS | ~120/145 |
| V-04 (tags + per-zone) | PASS | PASS | FAIL | ~130/145 |
| V-05 (golden, all 18) | PASS | PASS | PASS | ~145/145 |

**V-01, V-02, V-03 expected to FAIL two of the three new criteria by design** -- single-axis
variations isolate each new criterion to test it independently.

**V-04 expected to miss only C-18** -- the combination of criterion tags + per-zone contrast
should achieve all other criteria from R3 V-04's foundation; correction table deliberately
omitted to keep the combination clean.

**V-05 predicted golden under v4** -- all three new criteria combined with arc-as-spine
(C-13), full deletion-resistance (C-14), plan-level YAML error block (C-15), and the pre-printed
verification checklist. If V-05 achieves all essentials and composite >= 80, it satisfies
the golden threshold and is the R4 golden candidate.
