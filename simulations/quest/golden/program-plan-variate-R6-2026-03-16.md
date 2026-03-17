---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 6
rubric: v6
aspirational_target: C-22, C-23, C-24
---

# program-plan -- R6 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v6 (C-01 through C-24, 24 criteria, 175 pts max, golden = all essential pass AND composite >= 80).

---

## R5 Retrospective Under v6 Rubric

Three new aspirational criteria (C-22, C-23, C-24) extracted from R5 excellence signals.
Retroactively scoring R5 top variations against v6:

| Variation | C-22 complete recommended annotation | C-23 dual-position zone dependency | C-24 template-field gate contrast | v6 est. |
|-----------|--------------------------------------|-------------------------------------|-----------------------------------|---------|
| V-01 (cross-tier errors) | PASS -- BAD block tags `# WRONG C-05`, `# WRONG C-06`, `# WRONG C-07`; all three in BAD block; correction table absent so only one artifact type | FAIL -- zone headers carry dep notes; no `# requires:` at skill-list placeholder line | FAIL -- contrast in comments only; stripping comments removes it | ~125 |
| V-02 (skill-position deps) | FAIL -- no criterion-tagged error artifacts for C-05/C-06/C-07; zone headers note dependency semantically but no `# WRONG` tags | PARTIAL -- `PREREQUISITE:` at skills for Validation/Simulation; Design zone header has no explicit `# requires:`; Synthesis zone header also absent | FAIL -- no per-zone contrast at all | ~100 |
| V-03 (correction table bridges) | PARTIAL -- correction table has C-06 entries but no C-05 rows and no C-07 row | FAIL -- no skill-position dep reminders | FAIL -- contrast absent | ~120 |
| V-04 (C-19+C-20) | PASS -- BAD block tags all three recommended; all three covered in BAD block | PARTIAL -- `PREREQUISITE:` at skills for Validation/Simulation/Synthesis; Design zone: skills line has `requires: scout signal from Discovery` but zone header says "This zone produces..." not "requires:" | FAIL -- contrast in comments | ~140 |
| V-05 (R5 golden) | PASS -- BAD block tags C-05/C-06/C-07; correction table has C-05/C-06/C-07 rows; all three covered in both artifact types | PARTIAL -- dual-position confirmed for Validation+Simulation; Design header says "This zone produces draft:spec" (not `requires:`) so format asymmetric; Synthesis header says "Goal: confirm..." with no explicit `requires:` | FAIL -- zone-header comments `# FAIL gate:` / `# PASS gate:` are annotations; stripping comments removes contrast | ~155 |

**R5 V-05 scores highest under v6** but C-23 is PARTIAL (Design and Synthesis zones have
asymmetric or absent header-position prerequisite) and C-24 is FAIL across all R5 variations.

**R6 targets:**
- **C-22**: R5 V-05 already passes C-22 via BAD block + correction table. R6 tests whether
  extending coverage to a THIRD artifact type (inline template annotations carrying
  `# (C-06)` / `# (C-05)` / `# (C-07)` references in the scaffold itself) raises compliance
  incrementally beyond dual-artifact coverage.
- **C-23**: Enforce the same `# requires: <artifact> from Zone: <name> (C-05)` format at BOTH
  the zone-header comment AND the `skills:` placeholder line for ALL four dependent zones
  (Design, Validation, Simulation, Synthesis). R5 V-05 was asymmetric on Design and Synthesis.
- **C-24**: Replace comment-based FAIL/PASS gate contrast (`# FAIL gate: "done"`) with actual
  YAML sibling keys (`gate_fail: "done"` / `gate_pass: "scout artifact present"` / `gate: "<fill in>"`)
  that survive comment stripping as visible YAML structure.

---

## Variation Axes

| Axis | Label | What it tests |
|------|-------|---------------|
| Inertia framing | Triple-artifact recommended annotation (C-22) | Does extending recommended-criterion coverage (C-05/C-06/C-07) from two artifact types (BAD block + correction table, R5 V-05) to three (adding inline template annotations) raise compliance further? |
| Lifecycle emphasis | Symmetric dual-position dependency reminders (C-23) | Does enforcing `# requires: <artifact> from Zone: <name> (C-05)` in the same format at BOTH positions for ALL four dependent zones -- closing the Design/Synthesis asymmetry from R5 V-05 -- eliminate the residual dependency violations? |
| Output format | Template-field gate contrast (C-24) | Does converting FAIL/PASS gate contrast from comment annotations to structural YAML sibling keys (`gate_fail:` / `gate_pass:` / `gate:`) -- which survive comment stripping -- improve gate quality by forcing structural engagement with contrast? |
| Inertia framing + Lifecycle emphasis | Full recommended annotation + symmetric dual-position (C-22 + C-23) | Can triple-artifact recommended coverage and symmetric dual-position dependency reminders coexist without crowding the template? |
| Golden synthesis | All three new axes + R5 V-05 foundation (C-22 + C-23 + C-24) | Does stacking triple-artifact recommended annotation, symmetric dual-position deps, and template-field gate contrast on the full R5 V-05 baseline saturate all 24 v6 criteria? |

Single-axis: V-01 (C-22), V-02 (C-23), V-03 (C-24)
Combined: V-04 (C-22 + C-23), V-05 (all three, golden)

---

## V-01 -- Triple-Artifact Recommended Annotation (C-22 axis)

**Axis**: Inertia framing -- all three recommended criteria (C-05, C-06, C-07) appear in THREE
artifact types: the BAD PLAN block, the correction table, AND inline template annotations
(zone-level comments in the scaffold itself carry `(WRONG C-06)`, `(C-05)`, `(C-07)` tags).

**Hypothesis**: R5 V-05 achieves C-22 via BAD block + correction table. The inline template
zone comments do NOT carry recommended-criterion references -- they say "NOT 'scout' (C-06)"
at the name placeholder but not at the zone header's framing comment. Spreading recommended
tags to a third artifact type (the scaffold zone comments) creates a third encounter point:
the model sees wrong shapes for recommended criteria in the BAD block, avoidance patterns in
the correction table, and criterion tags at the exact generation position in the template.
C-22 PASS via three artifact types. No dual-position dep reminders (C-23 FAIL by design --
zone headers only); no template-field gate contrast (C-24 FAIL by design). Base: R5 V-01
criterion-tagged BAD block + correction table with full recommended coverage.

Expected gains: C-22 PASS with triple-artifact coverage.
Expected gaps: C-23 FAIL (skills-line `# requires:` absent), C-24 FAIL (comment contrast).

---

### Prompt body

**`/program:plan` is a plan, not an executor.**

It sequences Signal skills into evidence-gated phases, producing `program.yaml`. Skills
remain independently runnable. The plan does not execute skills, does not advance stages,
and carries no automation authority. Its entire value is the gate: a shared agreement on
what artifacts must exist before the next phase begins.

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
| `review:design` before `draft:spec` produced | `draft:spec` in a prior stage; `review:design` after | C-05 |
| `flow:lifecycle` before any `review:*` | `review:*` in a prior stage; `flow:*` after | C-05 |
| `echo` with skills listed | `echo` with `skills: []` only | C-02 |
| `echo` missing `auto: true` | `echo` with `auto: true` | C-02 |
| No plan-identity comment; stages read as task list | Add `# REQUIRED: ...plan, not an executor` at top | C-07 |

---

**The wrong plan -- every failure tagged to its criterion:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment -- stages read as a task list, not a gated plan
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label -- use "discovery"
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: "scout:analysis" does not exist
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

Each `# WRONG C-NN` tag names the criterion. Recommended failures (C-05, C-06, C-07) are
as concrete here as essential failures. Check the correction table for every fix.

---

**The four-phase structure:**

**Phase 1 -- Discovery (PM)**
*Goal*: map the space before designing.
*Gate*: `">= 2 scout signals present; no blocking feasibility concerns"`.
Stage name: `"discovery"` or `"market-scan"` -- NOT `"scout"` (WRONG C-06: namespace label).

**Phase 2 -- Design (Architect + PM)**
*Goal*: produce a concrete approach engineering can validate.
*Gate*: `"draft-spec artifact present; Architect confirmed no blocking gaps"`.
`review:*` requires `draft:spec` first -- placing review here without a prior draft stage
violates C-05. Stage name: `"design"` or `"proposal"` -- NOT `"draft"` (WRONG C-06).

**Phase 3 -- Validation (Engineering)**
*Goal*: stress-test the design.
*Gate*: `"review-design and prove-prototype artifacts present; 0 P0 findings open"`.
Stage name: `"expert-review"` or `"validation"` -- NOT `"review"` (WRONG C-06).

**Phase 4 -- Synthesis (Full team)**
*Goal*: listen ahead and close the evidence loop.
*Gate*: `"listen-feedback and listen-adoption artifacts present; no critical blockers"`.
Stage name: `"synthesis"` or `"feedback-preview"` -- NOT `"listen"` (WRONG C-06).

**Echo** (auto): always last. `name: echo`, `skills: []`, `auto: true`. The echo contract is C-02.

**Namespace dependency order (C-05):**
```
scout -> draft -> review/prove -> flow/trace -> listen/topic -> echo
```

**Signal skill catalog** (every entry must resolve here -- C-03):

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
# C-07: the comment above marks plan identity; do not remove it or reframe stages as execution steps

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ---- PM Phase: Discovery ----
  # No upstream dependency -- Discovery is the breadth-first anchor (C-05: first layer)
  # Stage name: "discovery" or "market-scan" -- NOT "scout" (WRONG C-06: namespace as stage label)
  # Gate: artifact-referencing, numeric threshold -- NOT "done" / "complete" (WRONG C-04)

    - name: "<discovery-phase-label>"       # e.g. "discovery"; NOT "scout" (WRONG C-06)
      skills:
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate: "<artifacts the Architect needs; numeric threshold: '>= N scout signals present'>"
            # NOT "done" / "complete" (WRONG C-04) -- check correction table

  # ---- Architect+PM Phase: Design ----
  # review:* requires draft:spec -- this zone MUST precede Validation (WRONG C-05 if skipped)
  # Stage name: "design" or "proposal" -- NOT "draft" (WRONG C-06: namespace as stage label)
  # Gate: artifact-referencing -- NOT "spec done" / "complete" (WRONG C-04)

    - name: "<design-phase-label>"          # e.g. "design"; NOT "draft" (WRONG C-06)
      skills:
        - draft:<skill>                     # spec, proposal, or pitch
                                            # review:* cannot appear here; draft:spec must exist first (C-05)
      gate: "<artifact condition; confirm no blocking gaps>"
            # NOT "complete" (WRONG C-04) -- check correction table

  # ---- Engineering Phase: Validation ----
  # review:* requires draft:spec from Design; flow:*/trace:* require review:* (WRONG C-05 if skipped)
  # Stage name: "expert-review" or "validation" -- NOT "review" (WRONG C-06: namespace as stage label)
  # Gate: named artifacts + numeric threshold -- NOT "reviews complete" (WRONG C-04)

    - name: "<validation-phase-label>"      # e.g. "expert-review"; NOT "review" (WRONG C-06)
      skills:
        - review:<skill>                    # design, users, customers, or code
                                            # requires draft:spec from Design (C-05) -- check correction table
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"
            # NOT "reviews complete" (WRONG C-04) -- check correction table

    - name: "<simulation-phase-or-remove>"  # optional; NOT "flow" (WRONG C-06); remove if unneeded
      skills:
        - flow:<skill>                      # requires review:* from Validation (WRONG C-05 if absent)
        - trace:<skill>
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ---- Team Phase: Synthesis ----
  # listen:* requires prior flow/trace or review signal (WRONG C-05 if skipped)
  # Stage name: "synthesis" or "feedback-preview" -- NOT "listen" (WRONG C-06: namespace as stage label)
  # Gate: artifact-referencing -- NOT "synthesis done" (WRONG C-04)

    - name: "<synthesis-phase-label>"       # e.g. "synthesis"; NOT "listen" (WRONG C-06)
      skills:
        - listen:<skill>                    # requires prior flow/trace or review artifact (C-05)
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ---- Final Stage: echo ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages. (WRONG C-02 if violated)

    - name: echo
      skills: []      # REQUIRED: empty -- DO NOT add skills here (WRONG C-02 if violated)
      auto: true      # REQUIRED: must be present and true (WRONG C-02 if missing)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03); check correction table
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04); check correction table
- [ ] Namespace dependency order preserved: scout before draft, draft before review, review before flow/trace (C-05); check correction table
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top (C-07); check correction table
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags on C-05, C-06, AND C-07 alongside essential criteria (C-22 via BAD block)
- [ ] Correction table contains C-05 rows (dependency order) AND C-07 row (plan identity) alongside C-06 rows (C-22 via table)
- [ ] Template zone comments carry `(WRONG C-06)`, `(C-05)`, `(WRONG C-04)` tags at generation positions (C-22 via inline annotations)

---

## V-02 -- Symmetric Dual-Position Zone Dependency Reminders (C-23 axis)

**Axis**: Lifecycle emphasis -- every dependency-bearing zone carries `# requires: <artifact>
from Zone: <name> (C-05)` at BOTH the zone-header comment block AND the `skills:` placeholder
line, in the exact same format at both positions.

**Hypothesis**: R5 V-05 had asymmetric coverage: Validation and Simulation were dual-position,
but Design's header said "This zone produces draft:spec" (output framing, not input framing)
and Synthesis's header had no `# requires:` at all. A prompt that enforces the same
`# requires: <artifact> from Zone: <name> (C-05)` format at the zone header AND at the
`skills:` line for all four dependent zones closes the asymmetry. The header fires when
the model enters the zone; the skills-line reminder fires at the exact skill-selection moment.
C-23 PASS (all four dependent zones, both positions, same format). No correction table
(C-18/C-21 FAIL by design); no template-field gate contrast (C-24 FAIL by design). BAD block
covers all three recommended criteria so C-22 passes as a side effect.

Expected gains: C-23 PASS (all four dependent zones, dual-position, consistent format).
Expected gaps: C-18 FAIL (no correction table), C-21 FAIL (no table bridges), C-24 FAIL.

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
`listen:*` requires at least one prior flow, trace, or review signal.
At least one non-echo gate must contain a numeric threshold.

**The wrong plan -- every failure tagged:**

```yaml
# BAD PLAN: fails all four essential criteria AND all three recommended criteria

program:
  topic: "{{topic}}"
  # WRONG C-07: no plan-identity comment
  stages:
    - name: scout                  # WRONG C-06: namespace name as stage label
      skills:
        - scout:feasibility
        - scout:analysis           # WRONG C-03: invented skill name
        - review:design            # WRONG C-05: review before draft:spec exists
      gate: "done"                 # WRONG C-04: execution state
    - name: draft                  # WRONG C-06: namespace name
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
  #   Why: execution state -- names what was done, not what must exist
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
  #   Why: artifact names + numeric threshold -- verifiable before committing to design

    - name: "<discovery-phase-label>"       # e.g. "discovery", "market-scan"; NOT "scout" (C-06)
      # requires: (none) -- Discovery is the upstream anchor (C-05)
      skills:                               # requires: (none -- first layer)
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # requires: scout signals from Zone: Discovery (C-05)
  #
  # FAIL gate: "spec done"
  #   Why: execution state -- unnamed artifact, cannot be verified
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
  #   Why: artifact name present -- engineering can check before starting review

    - name: "<design-phase-label>"          # e.g. "design", "proposal"; NOT "draft" (C-06)
      # requires: scout signals from Zone: Discovery (C-05)
      skills:                               # requires: scout signals from Zone: Discovery (C-05)
        - draft:<skill>                     # spec, proposal, or pitch
      gate: "<artifact condition; confirm Architect reviewed for blocking gaps>"

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design
  # requires: draft:spec artifact from Zone: Design (C-05)
  #
  # FAIL gate: "reviews complete"
  #   Why: execution state -- "complete" is not checkable by the synthesis team
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"
  #   Why: named artifacts + quantified threshold

    - name: "<validation-phase-label>"      # e.g. "expert-review", "validation"; NOT "review" (C-06)
      # requires: draft:spec artifact from Zone: Design (C-05)
      skills:                               # requires: draft:spec artifact from Zone: Design (C-05)
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate: "<review/prove artifacts present; 0 P0 findings open>"

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove this zone if flow/trace signals are not needed for {{topic}}
  # requires: review:* artifact from Zone: Validation (C-05)
  #
  # FAIL gate: "simulation done"
  #   Why: execution state -- names what was run, not what exists
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
  #   Why: artifact names present -- checkable before synthesis begins

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed; NOT "flow" (C-06)
      # requires: review:* artifact from Zone: Validation (C-05)
      skills:                               # requires: review:* artifact from Zone: Validation (C-05)
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # requires: at least one flow/trace or review artifact from prior zones (C-05)
  #
  # FAIL gate: "synthesis done"
  #   Why: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
  #   Why: artifact names + checkable condition

    - name: "<synthesis-phase-label>"       # e.g. "synthesis", "feedback-preview"; NOT "listen" (C-06)
      # requires: at least one flow/trace or review artifact from prior zones (C-05)
      skills:                               # requires: flow/trace or review artifact from prior zones (C-05)
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"

  # ==== Final Stage: echo ====
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty
      auto: true      # REQUIRED: must be present and true
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03)
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04)
- [ ] Namespace dependency order preserved (C-05)
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06)
- [ ] Plan-identity REQUIRED comment preserved at top (C-07)
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example (C-17)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries `# requires: <artifact> from Zone: <name> (C-05)` at BOTH the zone-header comment AND the `skills:` line, in the same format (C-23)

---

## V-03 -- Template-Field Gate Contrast (C-24 axis)

**Axis**: Output format -- per-zone FAIL/PASS gate contrast appears as actual YAML sibling
keys (`gate_fail:` / `gate_pass:` / `gate:`) in each non-echo zone, not as comment
annotations. Stripping comments leaves the contrast visible as YAML structure.

**Hypothesis**: Comment-based FAIL/PASS contrast (C-17) can be scanned past when the model
writes the `gate:` field. Converting contrast to sibling YAML keys makes engagement
structural: to produce the output, the model must either resolve or remove `gate_fail:` and
`gate_pass:`, forcing contact with the contrast at each zone. The `gate_fail:` field shows
the wrong shape; `gate_pass:` provides the model to follow; `gate:` is the placeholder to
fill. The final output should collapse the triple to a single `gate:` scalar -- but the
generation moment encounters all three as YAML structure. C-24 PASS. No dual-position
dep reminders (C-23 FAIL by design); C-22 satisfied via BAD block + correction table.

Expected gains: C-24 PASS (all five non-echo zones have YAML-key contrast).
Expected gaps: C-23 FAIL (zone headers only, no skills-line `# requires:`).

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

**The wrong plan (inertia pattern):**

```yaml
# WRONG: flat plan, dependency order violated, execution-state gates
program:
  topic: "{{topic}}"
  stages:
    - name: "all-work"
      skills:
        - scout:feasibility
        - review:design       # WRONG C-05: review before draft:spec
        - flow:lifecycle      # WRONG C-05: flow before review
        - listen:feedback
      gate: "done"            # WRONG C-04: execution state
    - name: echo
      skills: []
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

**Produce the following output. The `gate_fail:` and `gate_pass:` fields in each stage show a
wrong and a right gate example. Write your `gate:` value using `gate_pass:` as the model.
In your final output, each stage should contain only `gate:` (delete `gate_fail:` and
`gate_pass:` lines). Reproduce the REQUIRED comment and Plan Verification section verbatim.**

```yaml
# REQUIRED: preserve this comment -- this program is a plan, not an executor; skills run standalone

program:
  topic: "<topic-name>"
  strategy: "<one-sentence goal: what decision does this program inform?>"

  stages:

  # ---- Layer 1: Breadth (scout / prove:websearch / prove:intelligence) ----

    - name: "<breadth-phase-label>"         # check correction table: stage names -- NOT "scout"
      skills:                               # check correction table: skill names
        - scout:<skill>
        - scout:<skill>
      gate_fail: "research done"            # WRONG C-04: execution state -- do not copy
      gate_pass: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
      gate: "<fill in: use gate_pass as model; include numeric threshold; delete gate_fail/gate_pass>"

  # ---- Layer 2: Depth (draft / review / prove / flow / trace) ----
  # review:* requires draft:spec | flow:*/trace:* require review:* | dependency order: C-05

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft"
      skills:                               # check correction table: skill names
        - draft:<skill>
      gate_fail: "spec done"               # WRONG C-04: execution state
      gate_pass: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review"
      skills:                               # check correction table: skill names; requires draft:spec (C-05)
        - review:<skill>
        - prove:<skill>
      gate_fail: "reviews complete"         # WRONG C-04: execution state
      gate_pass: "review-design and prove-prototype artifacts present; 0 P0 findings open"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed; check correction table
      skills:                               # check correction table: skill names; requires review:* (C-05)
        - flow:<skill>
        - trace:<skill>
      gate_fail: "simulation done"          # WRONG C-04: execution state
      gate_pass: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"

  # ---- Layer 3: Synthesis (listen / topic) ----

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen"
      skills:                               # check correction table: skill names
        - listen:<skill>
        - topic:<skill>
      gate_fail: "synthesis done"           # WRONG C-04: execution state
      gate_pass: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"

  # ---- Final Stage: echo ----
  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.

    - name: echo
      skills: []      # REQUIRED: empty -- check correction table (C-02)
      auto: true      # REQUIRED: must be present and true -- check correction table (C-02)
```

## Plan Verification

- [ ] Last stage is `echo` with `skills: []` and `auto: true`; no stage after echo (C-02)
- [ ] All skill names belong to Signal's 9 namespaces -- no invented names (C-03); check correction table
- [ ] Every non-echo gate expresses evidence state -- not execution state (C-04); check correction table
- [ ] Namespace dependency order preserved (C-05); check correction table
- [ ] Stage names are descriptive phase labels -- not namespace names (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top (C-07); check correction table
- [ ] At least one gate contains a numeric threshold (C-08)
- [ ] Three arc-layer comments (Layer 1: Breadth / Layer 2: Depth / Layer 3: Synthesis) preserved (C-13)
- [ ] Every `name:`, `skills:`, and `gate:` field carries a `# check correction table` annotation (C-21)
- [ ] Every non-echo zone had `gate_fail:` / `gate_pass:` / `gate:` as sibling YAML fields; final output collapses to `gate:` scalar (C-24)

---

## V-04 -- Complete Recommended Annotation + Symmetric Dual-Position (C-22 + C-23)

**Axes**: Inertia framing (C-22) + Lifecycle emphasis (C-23) combined.

**Hypothesis**: Comprehensive recommended-criterion error coverage in both artifact types
ensures the model encounters wrong shapes for C-05/C-06/C-07 in the BAD block AND avoidance
patterns in the correction table. Symmetric dual-position dependency reminders close the
Design/Synthesis asymmetry from R5 V-05 by enforcing `# requires: <artifact> from Zone: <name>
(C-05)` at both the zone-header AND the skills-line for all four dependent zones. Together they
attack two independent failure modes: (1) model generates namespace-label stage names or
executor-framed plans because recommended failures were underrepresented; (2) model places
`review:*` before `draft:spec` because only one structural position reminded it of the
constraint. C-22 PASS, C-23 PASS. No template-field gate contrast (C-24 FAIL by design).

Expected gains: C-22 PASS (all three recommended in both BAD block and correction table),
C-23 PASS (all four dependent zones, both positions, same format).
Expected gaps: C-24 FAIL (comment-based contrast only).

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

Each `# WRONG C-NN` tag names the criterion. Check the correction table for every fix.

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
  # requires: (none) -- Discovery is the upstream anchor (C-05)
  #
  # FAIL gate: "research done"     <-- WRONG C-04: execution state, names no artifact
  # PASS gate: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"

    - name: "<discovery-phase-label>"       # check correction table: stage names -- NOT "scout" (WRONG C-06)
      # requires: (none) -- Discovery is the first layer (C-05)
      skills:                               # check correction table: skill names; no prerequisite for Discovery
        - scout:<skill>
        - scout:<skill>
      gate: "<artifact-referencing condition; numeric threshold: '>= N scout signals present'>"
                                            # check correction table: gates -- NOT "done" (WRONG C-04)

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # requires: scout signals from Zone: Discovery (C-05)
  #
  # FAIL gate: "spec done"         <-- WRONG C-04: execution state
  # PASS gate: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" (WRONG C-06)
      # requires: scout signals from Zone: Discovery (C-05)
      skills:                               # check correction table: skill names; requires: scout signals from Zone: Discovery (C-05)
        - draft:<skill>
      gate: "<artifact condition; at least ONE gate across the full plan must be quantified>"
                                            # check correction table: gates -- NOT "proceed" (WRONG C-04)

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design
  # requires: draft:spec artifact from Zone: Design (C-05)
  #
  # FAIL gate: "reviews complete"  <-- WRONG C-04: execution state
  # PASS gate: "review-design and prove-prototype artifacts present; 0 P0 findings open"

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review" (WRONG C-06)
      # requires: draft:spec artifact from Zone: Design (C-05)
      # Do NOT list review:* skills unless draft:spec was produced in a prior stage (WRONG C-05)
      skills:                               # check correction table: skill names; requires: draft:spec from Zone: Design (C-05)
        - review:<skill>
        - prove:<skill>
      gate: "<review/prove artifacts present; 0 P0 findings open>"
                                            # check correction table: gates -- NOT "complete" (WRONG C-04)

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed; requires: review:* artifact from Zone: Validation (C-05)
  #
  # FAIL gate: "simulation done"   <-- WRONG C-04: execution state
  # PASS gate: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed; NOT "flow" (WRONG C-06)
      # requires: review:* artifact from Zone: Validation (C-05)
      # Do NOT list flow:*/trace:* without a prior review:* zone (WRONG C-05)
      skills:                               # check correction table: skill names; requires: review:* from Zone: Validation (C-05)
        - flow:<skill>
        - trace:<skill>
      gate: "<flow/trace artifacts present; no P0 simulation gaps>"
                                            # check correction table: gates

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # requires: at least one flow/trace or review artifact from prior zones (C-05)
  #
  # FAIL gate: "synthesis done"    <-- WRONG C-04: execution state
  # PASS gate: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" (WRONG C-06)
      # requires: at least one flow/trace or review artifact from prior zones (C-05)
      # Do NOT place listen:*/topic:* before all validation zones are gated (WRONG C-05)
      skills:                               # check correction table: skill names; requires: flow/trace or review artifact from prior zones (C-05)
        - listen:<skill>
        - topic:<skill>
      gate: "<listen artifacts present; all prior signals archived; no critical blockers>"
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
- [ ] Each arc zone comment includes both a FAIL and a PASS gate example (C-17)
- [ ] Correction table present with C-02/C-03/C-04/C-05/C-06/C-07 rows (C-18)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags covering C-05, C-06, AND C-07 alongside essential criteria (C-22 via BAD block)
- [ ] Correction table contains C-05 rows AND C-07 row alongside C-06 rows (C-22 via table)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries `# requires: <artifact> from Zone: <name> (C-05)` at BOTH the zone-header comment AND the `skills:` line (C-23)

---

## V-05 -- Golden Synthesis (all 24 criteria)

**Axes**: All three new criteria (C-22 + C-23 + C-24) combined with the full R5 V-05 foundation.

**Hypothesis**: A prompt that (1) places all three recommended criteria (C-05, C-06, C-07) in
both the BAD PLAN block and the correction table (C-22), (2) enforces `# requires: <artifact>
from Zone: <name> (C-05)` at BOTH the zone-header comment AND the `skills:` line for all four
dependent zones in the same format (C-23), and (3) uses `gate_fail:` / `gate_pass:` / `gate:`
as actual YAML sibling keys in all five non-echo zones so gate contrast survives comment
stripping (C-24), stacked on the complete R5 V-05 baseline (C-01 through C-21 addressed),
saturates all 24 v6 criteria.

C-22 PASS: all three recommended covered in both artifact types.
C-23 PASS: all four dependent zones dual-position, consistent `# requires:` format.
C-24 PASS: all five non-echo zones have YAML-key gate contrast.
Expected overall: all 24 criteria pass. Golden candidate.

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

**The gated plan -- what you're building:**

```yaml
# GOOD: three-layer evidence arc, all criteria satisfied, dependency order preserved
program:
  topic: "{{topic}}"
  stages:

  # Layer 1: Breadth
    - name: discovery
      skills:
        - scout:feasibility
        - scout:requirements
        - scout:competitors
      gate: "scout-feasibility, scout-requirements, scout-competitors artifacts present;
             >= 2 scout signals reviewed; no blocking feasibility concerns"

  # Layer 2: Depth
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

  # Layer 3: Synthesis
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

**Produce the following output. The `gate_fail:` and `gate_pass:` fields show a wrong and a
right gate example for each zone. Write your `gate:` value using `gate_pass:` as the model.
In your final output, collapse each triple to a single `gate:` scalar (delete `gate_fail:`
and `gate_pass:` lines). Reproduce the REQUIRED comment and Plan Verification verbatim.**

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

    - name: "<discovery-phase-label>"       # check correction table: stage names -- NOT "scout" (WRONG C-06)
      # requires: (none) -- Discovery is the first layer (C-05)
      skills:                               # check correction table: skill names; no prerequisite for Discovery
        - scout:<skill>                     # feasibility, market, requirements, competitors...
        - scout:<skill>
      gate_fail: "research done"            # WRONG C-04: execution state -- do not use
      gate_pass: "scout-feasibility and scout-requirements artifacts present; >= 2 signals reviewed"
      gate: "<fill in: use gate_pass as model; include numeric threshold; delete gate_fail/gate_pass>"
                                            # check correction table: gates -- NOT "done" (WRONG C-04)

  # ==== Zone: Design (draft) ====
  # Goal: produce a concrete approach engineering can validate
  # requires: scout signals from Zone: Discovery (C-05)

    - name: "<design-phase-label>"          # check correction table: stage names -- NOT "draft" (WRONG C-06)
      # requires: scout signals from Zone: Discovery (C-05)
      skills:                               # check correction table: skill names; requires: scout signals from Zone: Discovery (C-05)
        - draft:<skill>                     # spec, proposal, or pitch
      gate_fail: "spec done"               # WRONG C-04: execution state
      gate_pass: "draft-spec artifact present; Architect confirmed no blocking feasibility gaps"
      gate: "<fill in: use gate_pass as model; at least ONE gate across the full plan must be quantified>"
                                            # check correction table: gates -- NOT "proceed" (WRONG C-04)

  # ==== Zone: Validation (review / prove) ====
  # Goal: stress-test the design
  # requires: draft:spec artifact from Zone: Design (C-05)

    - name: "<validation-phase-label>"      # check correction table: stage names -- NOT "review" (WRONG C-06)
      # requires: draft:spec artifact from Zone: Design (C-05)
      # Do NOT list review:* skills unless draft:spec was produced in a prior stage (WRONG C-05)
      skills:                               # check correction table: skill names; requires: draft:spec from Zone: Design (C-05)
        - review:<skill>                    # design, users, customers, or code
        - prove:<skill>                     # prototype, analysis, interview...
      gate_fail: "reviews complete"         # WRONG C-04: execution state
      gate_pass: "review-design and prove-prototype artifacts present; 0 P0 findings open"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
                                            # check correction table: gates -- NOT "complete" (WRONG C-04)

  # ==== Zone: Simulation (flow / trace) -- OPTIONAL ====
  # Remove if flow/trace signals not needed for {{topic}}
  # requires: review:* artifact from Zone: Validation (C-05)

    - name: "<simulation-phase-or-remove>"  # optional; remove if not needed; NOT "flow" (WRONG C-06)
      # requires: review:* artifact from Zone: Validation (C-05)
      # Do NOT include flow:*/trace:* without a prior review:* zone (WRONG C-05)
      skills:                               # check correction table: skill names; requires: review:* from Zone: Validation (C-05)
        - flow:<skill>                      # lifecycle, resilience, trigger...
        - trace:<skill>                     # component, contract, request...
      gate_fail: "simulation done"          # WRONG C-04: execution state
      gate_pass: "flow-lifecycle and trace-contract artifacts present; no P0 simulation gaps"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
                                            # check correction table: gates

  # ==== Zone: Synthesis (listen / topic) ====
  # Goal: confirm what users and adopters signal; close the evidence loop
  # requires: at least one flow/trace or review artifact from prior zones (C-05)

    - name: "<synthesis-phase-label>"       # check correction table: stage names -- NOT "listen" (WRONG C-06)
      # requires: at least one flow/trace or review artifact from prior zones (C-05)
      # Do NOT place listen:*/topic:* before all validation zones are gated (WRONG C-05)
      skills:                               # check correction table: skill names; requires: flow/trace or review artifact from prior zones (C-05)
        - listen:<skill>                    # adoption, feedback, or support
        - topic:<skill>                     # plan, report, status, or story
      gate_fail: "synthesis done"           # WRONG C-04: execution state
      gate_pass: "listen-feedback and listen-adoption artifacts present; no critical adoption blockers"
      gate: "<fill in: use gate_pass as model; delete gate_fail/gate_pass>"
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
- [ ] Namespace dependency order preserved: scout before draft, draft before review, review before flow/trace (C-05); check correction table
- [ ] Stage names are descriptive phase labels -- not namespace names, not generic indices (C-06); check correction table
- [ ] Plan-identity REQUIRED comment preserved at top of YAML (C-07); check correction table
- [ ] At least one gate contains a numeric threshold (e.g., `>= N scout signals`, `0 P0 findings`) (C-08)
- [ ] Evidence arc visible in stage sequencing: breadth (Discovery) -> depth (Design/Validation/Simulation) -> synthesis (Synthesis) (C-09)
- [ ] BAD PLAN block carries `# WRONG C-NN` tags on each wrong field (C-16)
- [ ] Each arc zone had both a FAIL and a PASS example -- delivered via `gate_fail:`/`gate_pass:` fields (C-17 + C-24)
- [ ] Correction table present with >= 3 pairs covering C-02/C-03/C-04/C-05/C-06/C-07 (C-18)
- [ ] Every `name:`, `skills:`, and `gate:` field carries a `# check correction table` annotation (C-21)
- [ ] All three recommended criteria (C-05, C-06, C-07) covered in both BAD PLAN block AND correction table (C-22)
- [ ] Every dependency-bearing zone (Design, Validation, Simulation, Synthesis) carries `# requires: <artifact> from Zone: <name> (C-05)` at BOTH the zone-header comment AND the `skills:` line (C-23)
- [ ] Every non-echo zone had `gate_fail:` / `gate_pass:` / `gate:` as sibling YAML fields; final output collapses to single `gate:` scalar (C-24)
