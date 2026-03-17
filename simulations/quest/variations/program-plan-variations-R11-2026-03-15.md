Now I'll write the R11 variates. The two new criteria to target:

- **C-36**: When BAD PLAN has all 7 criterion tags (C-31 passes), the header must not claim "essential violations only" — label-content accuracy
- **C-37**: Every violating `name:` field in the BAD PLAN must carry `# WRONG C-06` at the `name:` line itself, not displaced to adjacent fields

---

# program:plan — Round 11 Variates (v11 rubric)

Date: 2026-03-16

## R10 retrospective under v11 rubric

R10 introduced compound `gate_fail:` annotation (C-34: criterion tag + `Why:` inline at the field) and dual error-format recommended coverage (C-35: C-31 + C-29 both passing). R10 V-05 achieved golden synthesis with C-34 + C-35 + all R9 mechanisms. The v11 rubric formalizes C-36 (BAD PLAN header label must accurately reflect its criterion coverage scope — not claim "essential only" when the block also carries recommended-tier tags) and C-37 (every violating `name:` field in the BAD PLAN that fails C-06 must carry `# WRONG C-06` co-located at the `name:` field itself, not displaced to an adjacent field or block header). These raise aspirational count to 30 and total max to 240 pts. Golden threshold (>= 80) unchanged.

**R11 target**: V-01 isolates C-36 as single-axis. V-02 isolates C-37 as single-axis. V-03 tests C-37 under a different output format/lifecycle emphasis axis. V-04 combines C-36 + C-37. V-05 is the golden synthesis: C-36 + C-37 + all R10 V-05 mechanisms preserved.

---

## V-01 — Accurate Header Label (single-axis: C-36)

**Axis**: The BAD PLAN block carries all 7 criterion tags (C-31 passes) and its header comment accurately describes full coverage — `# BAD PLAN — complete criterion index (C-01 through C-07)` — not the R10 V-01 label `# BAD PLAN — essential violations (C-01 through C-04)` which falsely restricts claimed scope when C-05/C-06/C-07 tags are present in the body. C-34 preserved (compound `gate_fail:` annotation with `Why:` inline). Correction table essential-tier only (C-29 absent, C-35 absent) to isolate C-36. C-37 incidentally present: `name:` fields carry `# WRONG C-06` at the field, identical to R10 V-01. Phrasing: technical/imperative.

**Hypothesis**: Changing the BAD PLAN header from "essential violations (C-01 through C-04)" to "complete criterion index (C-01 through C-07)" earns C-36 as an isolated criterion. C-35 absent (essential correction table only) confirms C-36 independence from dual error-format coverage. C-34 preserved as baseline. Expected delta over R10 V-01 baseline: +1 aspirational criterion pass (C-36). C-37 incidentally passes due to unchanged `name:` field annotation structure from R10 V-01.

---

### Prompt body

````
`program:plan` — Signal plugin skill.

Stage a Signal investigation for topic: {{topic}}. Output: `program.yaml` — stages with
name, skills, and gate — plus final echo stage. Plan identity: you are sequencing evidence-
gathering, not executing it. A gate checks that artifacts exist, not that skills have run.

---

## Error map — all 7 criteria illustrated

Every criterion from C-01 through C-07 appears with at least one `# WRONG C-XX` tag below.
Study all seven before filling the template.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label (not evidence intent)
      skills:
        - scout:feasibility
        - scout:analysis                         # WRONG C-03: "scout:analysis" not a Signal skill
      gate: "run discovery skills"               # WRONG C-04: execution gate

    - name: "draft-phase"                        # WRONG C-06: namespace label (not evidence intent)
      skills:
        - review:design                          # WRONG C-05: review:design before draft:spec
        - draft:brief                            # WRONG C-03: "draft:brief" not a Signal skill
      gate: "draft phase complete"               # WRONG C-04 / WRONG C-07: executor framing

    - name: "verify"
      skills:                                    # WRONG C-01: empty skills list in non-echo stage
      gate: "verified"

# WRONG C-02: no echo final stage
```

---

## Correction table

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| skills: (empty, non-echo stage) | skills: [≥1 valid Signal skill] | C-01 |
| (missing echo final stage) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| scout:analysis | scout:competitors | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| draft:brief | draft:spec | C-03 |
| prove:analysis | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| gate: "run [skill/stage]" | gate: "[artifact] present" | C-04 |
| gate: "[stage] complete" | gate: "[artifact name] present" | C-04 |

---

## YAML template

Zone 1 (Discovery) has no upstream dependencies — no dep reminders.
Zones 2, 3, 4 are dependency-bearing — each carries all four annotation mechanisms.

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Zone 1: Discovery — no upstream dependencies
    - name: ""                                            # evidence-intent label
      skills:                                             # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run all discovery skills"               # WRONG C-04 — Why: gate names artifact presence, not actions to run
      gate_pass: "feasibility + competitors artifacts present"   # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 2: Shape — depends on Discovery artifacts
    # requires: [Discovery artifact] from Zone: Discovery (C-05)
    - name: ""                                            # evidence-intent label
      # requires: [Discovery artifact] from Zone: Discovery (C-05)
      skills:                                             # requires: [Discovery artifact] from Zone: Discovery (C-05)
                                                          # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                        # WRONG C-07 — Why: completion-state framing names execution, not artifact existence
      gate_pass: "spec artifact present"                  # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 3: Challenge — depends on Shape artifacts
    # requires: [Shape artifact] from Zone: Shape (C-05)
    - name: ""                                            # evidence-intent label
      # requires: [Shape artifact] from Zone: Shape (C-05)
      skills:                                             # requires: [Shape artifact] from Zone: Shape (C-05)
                                                          # check correction table: skill names
        - ""
        - ""
      gate_fail: "review done"                            # WRONG C-07 — Why: "done" names execution state, not an inspectable artifact
      gate_pass: "design review artifact present"         # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 4: Validate — depends on Challenge artifacts
    # requires: [Challenge artifact] from Zone: Challenge (C-05)
    - name: ""                                            # evidence-intent label
      # requires: [Challenge artifact] from Zone: Challenge (C-05)
      skills:                                             # requires: [Challenge artifact] from Zone: Challenge (C-05)
                                                          # check correction table: skill names
        - ""
      gate_fail: "validation complete"                    # WRONG C-04 — Why: phase completion is execution-history, not artifact presence
      gate_pass: "validation artifact present"            # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

At every dependency-bearing zone (Zones 2–4):
- Dep reminder (`# requires: ... from Zone: ... (C-05)`) appears at BOTH the zone-header
  comment AND the `skills:` placeholder line — uniform syntax at both positions
- At the `skills:` line: the dep reminder and the correction-table bridge (`# check correction
  table: skill names`) coexist as independent annotations — neither substitutes for the other
- Fill `gate:` using the correction table; `gate_fail:` and `gate_pass:` are contrast examples
````

---

## V-02 — Stage Name Field-Level Annotation (single-axis: C-37)

**Axis**: Every wrong-format `name:` value in the BAD PLAN that violates C-06 carries `# WRONG C-06` co-located at the `name:` field itself — not displaced to an adjacent `gate:` or `skills:` line. BAD PLAN carries all 7 criteria (C-31 prerequisite for C-37). A prose annotation block above the BAD PLAN explicitly teaches the field-level co-location rule with a displacement anti-pattern. Header accurately labeled (C-36 passes). Correction table covers all 7 criteria including recommended tier (C-29 = C-35 with C-31). C-34 absent (no `Why:` on `gate_fail:`) to isolate C-37 from compound annotation axis. Phrasing: descriptive/intent-forward.

**Hypothesis**: Explicit teaching of field-level co-location discipline — showing both the displacement anti-pattern and the correct co-located pattern before the BAD PLAN — earns C-37. C-34 absent (no `Why:` annotations) confirms independence from compound annotation axis. Expected: C-37 + C-35 + C-36 pass; C-34 fails as intended control.

---

### Prompt body

````
`program:plan` — Signal plugin skill.

You are planning a Signal investigation for topic: {{topic}}. A program plan sequences
evidence-gathering skills into stages with gates. Output: `program.yaml`. The final stage is
always `echo` (auto: true, skills: []). You are a planner — not an executor.

---

## Field-level annotation discipline

Criterion tags belong at the field that contains the violation. For C-06 — `name:` values
that use namespace labels instead of evidence intent — the tag goes at the `name:` line:

```yaml
    # DISPLACEMENT ANTI-PATTERN — tag not at the violating field:
    - name: "scout-phase"
      skills:
        - scout:feasibility
      gate: "run skills"   # WRONG C-06 ← WRONG POSITION: C-06 belongs at name:, not gate:

    # CORRECT CO-LOCATION — tag at the violating field:
    - name: "scout-phase"  # WRONG C-06: namespace label — name the evidence goal
      skills:
        - scout:feasibility
      gate: "run skills"   # WRONG C-04: execution gate
```

---

## Complete error map — all 7 criteria illustrated

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label — name the evidence goal
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "execute scout:feasibility"          # WRONG C-04: execution gate
                                                 # WRONG C-07: executor framing

    - name: "draft-phase"                        # WRONG C-06: namespace label — name the evidence goal
      skills:
        - review:design                          # WRONG C-05: review:design before draft:spec
        - draft:brief                            # WRONG C-03: "draft:brief" not a Signal skill
      gate: "draft phase complete"               # WRONG C-07: executor framing

    - name: "validate"
      skills:                                    # WRONG C-01: empty skills list in non-echo stage
      gate: "validated"

# WRONG C-02: no echo final stage
```

---

## Correction table — all 7 criteria including recommended tier

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| skills: (empty, non-echo stage) | skills: [≥1 valid Signal skill] | C-01 |
| (missing echo final stage) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| draft:brief | draft:spec | C-03 |
| draft:outline | draft:proposal | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| scout:analysis | scout:competitors | C-03 |
| prove:analysis | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| gate: "execute [skill]" | gate: "[artifact] present" | C-04 |
| gate: "run all skills" | gate: "[artifact name(s)] present" | C-04 |
| gate: "phase complete" | gate: "[artifact] present" | C-04 |
| review:design before draft:spec | draft:spec must precede review:design | C-05 |
| flow:lifecycle before draft:spec | draft:spec must precede flow:lifecycle | C-05 |
| name: "scout-phase" | name: "Surface signals" (intent label) | C-06 |
| name: "draft-phase" | name: "Shape the concept" (intent label) | C-06 |
| gate: "execute..." / "run..." | gate: "[artifact] present" — plan identity | C-07 |
| gate: "[stage] complete" / "done" | gate: "[artifact] present" — plan identity | C-07 |

---

## YAML template

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Phase 1: Discovery
    - name: ""                                    # evidence-intent label
      skills:                                     # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run scout skills"               # WRONG C-04 (contrast only)
      gate_pass: "feasibility + competitors artifacts present"  # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 2: Shape
    - name: ""                                    # evidence-intent label
      # requires: [artifact] from Phase 1 (C-05)
      skills:                                     # requires: [artifact] from Phase 1 (C-05)
                                                  # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                # WRONG C-07 (contrast only)
      gate_pass: "spec artifact present"          # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 3: Challenge
    - name: ""                                    # evidence-intent label
      # requires: [artifact] from Phase 2 (C-05)
      skills:                                     # requires: [artifact] from Phase 2 (C-05)
                                                  # check correction table: skill names
        - ""
        - ""
      gate_fail: "review done"                    # WRONG C-07 (contrast only)
      gate_pass: "design review artifact present" # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 4: Validate
    - name: ""                                    # evidence-intent label
      # requires: [artifact] from Phase 3 (C-05)
      skills:                                     # requires: [artifact] from Phase 3 (C-05)
                                                  # check correction table: skill names
        - ""
      gate_fail: "validation complete"            # WRONG C-04 (contrast only)
      gate_pass: "validation artifact present"    # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

Both the BAD PLAN above and the correction table cover all 7 criteria (C-01 through C-07).
Fill `gate:` using the correction table; `gate_fail:` and `gate_pass:` are contrast examples
only. Check dep ordering: skills in Phase 2+ must not precede their artifact prerequisites.
````

---

## V-03 — C-37 under Lifecycle Emphasis Axis (axes: C-37 + output format)

**Axis**: C-37 (field-level C-06 annotation) tested under a lifecycle-emphasis structural format — arc phases as first-class document sections rather than numbered zones in a flat YAML template. Each section header names an arc phase, contains its own skill roster context, and embeds per-section gate contrast inline. This tests whether field-level co-location discipline (C-37) transfers to structurally distinct prompt formats. BAD PLAN is section-prefaced with an annotation discipline note. Header accurately labeled (C-36 passes). C-34 absent (no `Why:` on `gate_fail:`) to isolate C-37 from compound annotation axis. Correction table essential-tier only (C-29 absent, C-35 absent). Phrasing: formal/descriptive.

**Hypothesis**: Field-level C-06 annotation (C-37) is robust across output format variation. A lifecycle-emphasis format where arc phases are structural sections does not impede C-37 — the `name:` field discipline holds regardless of how surrounding structure is organized. C-34 absent confirms isolation from compound annotation. Expected: C-37 + C-36 pass; C-34/C-35 fail as intended controls.

---

### Prompt body

````
`program:plan` — Signal plugin skill.

A program plan sequences Signal evidence-gathering skills into staged phases with artifact
gates. Output: `program.yaml` with five stages: Discovery, Shape, Challenge, Validate, and
the mandatory echo stage. You are a planner — not an executor.

---

## Annotation placement rule

In the BAD PLAN below, every criterion tag (`# WRONG C-XX`) is placed at the field that
carries the violation. For C-06 — stage names that use namespace labels instead of evidence-
intent phrases — the `# WRONG C-06` tag appears at the `name:` field, not at an adjacent
gate or skills field. This field-level co-location makes each violation legible at the
authoring decision point.

---

## BAD PLAN — complete criterion index (C-01 through C-07)

```yaml
program:
  topic: "{{topic}}"
  stages:
    - name: "scout"                              # WRONG C-06: namespace label, not evidence intent
      skills:
        - scout:feasibility
        - scout:brief                            # WRONG C-03: "scout:brief" not a Signal skill
      gate: "scouting complete"                  # WRONG C-04: execution-state gate
                                                 # WRONG C-07: executor framing

    - name: "draft"                              # WRONG C-06: namespace label, not evidence intent
      skills:
        - flow:lifecycle                         # WRONG C-05: flow before any draft artifact exists
        - draft:outline                          # WRONG C-03: "draft:outline" not a Signal skill
      gate: "drafts done"                        # WRONG C-07: executor framing

    - name: "review"
      skills:                                    # WRONG C-01: non-echo stage with empty skills list
      gate: "reviewed"

# WRONG C-02: echo stage absent — final stage must be name: echo, auto: true, skills: []
```

---

## Correction table

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| skills: (empty, non-echo stage) | skills: [≥1 valid Signal skill] | C-01 |
| (missing echo final stage) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| scout:brief | scout:stakeholders | C-03 |
| draft:outline | draft:proposal | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| prove:analysis | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| gate: "scouting complete" | gate: "[artifact name] present" | C-04 |
| gate: "drafts done" | gate: "[artifact] present" | C-04 |
| gate: "[stage] complete" | gate: "[artifact name] present" | C-04 |

---

## Stage template by arc phase

### Discovery — surface what exists

```yaml
    - name: ""                                            # evidence-intent label
      skills:                                             # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "ran discovery skills"                   # WRONG C-04 (contrast only)
      gate_pass: "discovery artifacts (feasibility, competitors) present"  # correct shape
      gate: ""                                            # check correction table: gate values
```

### Shape — articulate the concept
*(requires Discovery artifacts — C-05)*

```yaml
    - name: ""                                            # evidence-intent label
      # requires: [Discovery artifact] from Discovery (C-05)
      skills:                                             # requires: [Discovery artifact] from Discovery (C-05)
                                                          # check correction table: skill names
        - ""
        - ""
      gate_fail: "shaping complete"                       # WRONG C-07 (contrast only)
      gate_pass: "spec artifact present"                  # correct shape
      gate: ""                                            # check correction table: gate values
```

### Challenge — stress-test the concept
*(requires Shape artifacts — C-05)*

```yaml
    - name: ""                                            # evidence-intent label
      # requires: [Shape artifact] from Shape (C-05)
      skills:                                             # requires: [Shape artifact] from Shape (C-05)
                                                          # check correction table: skill names
        - ""
        - ""
      gate_fail: "challenge done"                         # WRONG C-07 (contrast only)
      gate_pass: "design review artifact present"         # correct shape
      gate: ""                                            # check correction table: gate values
```

### Validate — ground-truth against reality
*(requires Challenge artifacts — C-05)*

```yaml
    - name: ""                                            # evidence-intent label
      # requires: [Challenge artifact] from Challenge (C-05)
      skills:                                             # requires: [Challenge artifact] from Challenge (C-05)
                                                          # check correction table: skill names
        - ""
      gate_fail: "validation done"                        # WRONG C-04 (contrast only)
      gate_pass: "validation artifact present"            # correct shape
      gate: ""                                            # check correction table: gate values
```

### Echo — always last

```yaml
    - name: echo
      auto: true
      skills: []
```

---

Write a `program.yaml` for topic: {{topic}} by assembling the five arc phases above.
Fill `gate:` using the correction table. At dep-bearing phases (Shape, Challenge, Validate):
dep reminder (`# requires: ... from ... (C-05)`) appears at BOTH the phase comment AND the
`skills:` line — same syntax at both positions; correction-table bridge is independent.
````

---

## V-04 — Combination: C-36 + C-37

**Axis**: Accurate BAD PLAN header label (C-36) AND every violating `name:` field carries `# WRONG C-06` co-located at the field (C-37). BAD PLAN carries all 7 criteria tags (C-31 prerequisite for both). Header claims full coverage to satisfy C-36. Compound `gate_fail:` annotation with `Why:` inline at every non-echo zone (C-34). Correction table covers all 7 criteria including recommended tier (C-29 → C-35 with C-31). Full four-mechanism zone density (C-26+C-27+C-30+C-32 = C-33). Phrasing: formal/technical. Lifecycle emphasis: named zone sequence with explicit boundary markers.

**Hypothesis**: C-36 and C-37 are orthogonal — C-36 governs the header string, C-37 governs annotation co-location at `name:` fields. Both are achievable simultaneously without displacing C-34 (compound `gate_fail:`) or C-35 (dual error-format recommended coverage). C-34 operates on `gate_fail:` fields in the YAML template; C-36 and C-37 operate on the BAD PLAN block — three non-overlapping sections. Expected: C-36 + C-37 + C-34 + C-35 all pass.

---

### Prompt body

````
`program:plan` — Signal plugin skill.

Stage a Signal investigation for topic: {{topic}}. Output: `program.yaml` — stages with
name, skills, and gate — plus final echo stage. Plan identity: a gate checks that artifacts
exist, not that skills have run. You sequence evidence-gathering; you do not execute it.

---

## Complete failure catalog — all 7 criteria

Every criterion from C-01 through C-07 appears at least once. Criterion tags are placed at
the field that carries the violation — C-06 tags appear at `name:` fields where namespace
labels occur.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                          # WRONG C-06: namespace label — "scout-phase"
                                                   #   names the namespace, not the evidence goal
                                                   #   CORRECT: "Surface competitive signals"
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "execute scout:feasibility"            # WRONG C-04: execution gate — gate must name
                                                   #   an artifact, not a skill invocation
                                                   # WRONG C-07: executor framing — "execute"
                                                   #   makes this a runner, not a plan

    - name: "draft-phase"                          # WRONG C-06: namespace label — name the
                                                   #   evidence goal, not the namespace
                                                   #   CORRECT: "Shape the concept"
      skills:
        - review:design                            # WRONG C-05: review:design before draft:spec —
                                                   #   the artifact under review does not exist yet
        - draft:brief                              # WRONG C-03: "draft:brief" not a Signal skill
                                                   #   CORRECT: draft:spec, draft:proposal
      gate: "drafts done"                          # WRONG C-07: executor framing — "done" is
                                                   #   not an artifact existence check

    - name: "validate"
      skills:                                      # WRONG C-01: non-echo stage has empty skills
                                                   #   list — each non-echo stage needs ≥1 skill
      gate: "validated"

# WRONG C-02: no echo final stage — the final stage must be:
#   - name: echo
#   - auto: true
#   - skills: []
```

---

## Correction table — all 7 criteria including recommended tier

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| skills: (empty, non-echo stage) | skills: [≥1 valid Signal skill] | C-01 |
| (missing echo final stage) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| draft:brief | draft:spec | C-03 |
| draft:outline | draft:proposal | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| scout:analysis | scout:competitors | C-03 |
| prove:analysis | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| gate: "execute [skill]" | gate: "[artifact] present" | C-04 |
| gate: "run all skills" | gate: "[artifact name(s)] present" | C-04 |
| gate: "phase complete" / "done" | gate: "[artifact] present" | C-04 |
| review:design before draft:spec | draft:spec must precede review:design | C-05 |
| flow:lifecycle before draft:spec | draft:spec must precede flow:lifecycle | C-05 |
| name: "scout-phase" | name: "Surface signals" (intent label) | C-06 |
| name: "draft-phase" | name: "Shape the concept" (intent label) | C-06 |
| gate: "execute..." / "run..." | gate: "[artifact] present" — plan identity | C-07 |
| gate: "[stage] complete" / "done" | gate: "[artifact] present" — plan identity | C-07 |

---

## YAML template

Zone 1 (Discovery) has no upstream dependencies — no dep reminders.
Zones 2, 3, 4 are dependency-bearing — each carries all four annotation mechanisms.

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Zone 1: Discovery — no upstream dependencies
    - name: ""                                            # evidence-intent label
      skills:                                             # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run all discovery skills"               # WRONG C-04 — Why: gate tests artifact presence, not execution history
      gate_pass: "feasibility + competitors artifacts present"   # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 2: Shape — depends on Discovery artifacts
    # requires: [Discovery artifact] from Zone: Discovery (C-05)
    - name: ""                                            # evidence-intent label
      # requires: [Discovery artifact] from Zone: Discovery (C-05)
      skills:                                             # requires: [Discovery artifact] from Zone: Discovery (C-05)
                                                          # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                        # WRONG C-07 — Why: plan identity disallows completion-state gates; name the artifact
      gate_pass: "spec artifact present"                  # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 3: Challenge — depends on Shape artifacts
    # requires: [Shape artifact] from Zone: Shape (C-05)
    - name: ""                                            # evidence-intent label
      # requires: [Shape artifact] from Zone: Shape (C-05)
      skills:                                             # requires: [Shape artifact] from Zone: Shape (C-05)
                                                          # check correction table: skill names
        - ""
        - ""
      gate_fail: "challenge phase done"                   # WRONG C-07 — Why: "done" is execution state; a gate inspects artifact existence
      gate_pass: "design review artifact present"         # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 4: Validate — depends on Challenge artifacts
    # requires: [Challenge artifact] from Zone: Challenge (C-05)
    - name: ""                                            # evidence-intent label
      # requires: [Challenge artifact] from Zone: Challenge (C-05)
      skills:                                             # requires: [Challenge artifact] from Zone: Challenge (C-05)
                                                          # check correction table: skill names
        - ""
      gate_fail: "validation complete"                    # WRONG C-04 — Why: phase completion is not artifact presence; gate must name an artifact
      gate_pass: "validation artifact present"            # correct shape (contrast only)
      gate: ""                                            # check correction table: gate values

    # Zone 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

At every dependency-bearing zone (Zones 2–4):
- Dep reminder (`# requires: ... from Zone: ... (C-05)`) appears at BOTH the zone-header
  comment AND the `skills:` placeholder line — uniform syntax at both positions
- At the `skills:` line: the dep reminder and the correction-table bridge (`# check correction
  table: skill names`) coexist as independent annotations — neither substitutes for the other
- Fill `gate:` using the correction table; `gate_fail:` and `gate_pass:` are contrast examples
- Both the BAD PLAN and the correction table cover all 7 criteria — consult both before
  authoring any field
````

---

## V-05 — Golden synthesis: C-36 + C-37 + all R10 mechanisms

**Axis**: All R10 V-05 mechanisms (C-34+C-35+C-31+C-29+C-32+C-33) plus both new R11 criteria. BAD PLAN carries all 7 criterion tags (C-31, prerequisite for C-35 and C-37). Header accurately claims full criterion coverage (C-36). Every violating `name:` field carries `# WRONG C-06` at the field (C-37). Every non-echo zone's `gate_fail:` carries both criterion tag AND `Why:` inline (C-34). Correction table covers all 7 criteria including recommended tier (C-29, prerequisite for C-35). C-35 = PASS (C-31 + C-29 both present). Full four-mechanism zone density at all dep-bearing zones (C-26+C-27+C-30+C-32 coexisting = C-33). Phrasing: descriptive/intent-forward.

**Hypothesis**: C-36 and C-37 are fully compatible with all R10 mechanisms. C-36 operates on the BAD PLAN header string. C-37 operates on the `name:` field annotations within the BAD PLAN body. C-34 operates on `gate_fail:` fields in the YAML template. All three modify distinct structural positions without displacement. C-35 (C-31+C-29) was already latent in R10 V-05 and is now explicit. Expected: near-maximum composite with all prior criteria preserved and C-36+C-37 added.

---

### Prompt body

````
`program:plan` — Signal plugin skill.

You are planning a Signal investigation for topic: {{topic}}. A program plan sequences
evidence-gathering skills into stages with gates. Output: `program.yaml`. The final stage is
always `echo` (auto: true, skills: []). You are a planner — not an executor.

---

## The complete error map — all 7 criteria illustrated

The BAD PLAN below is a criterion index. Every criterion from C-01 through C-07 appears with
at least one `# WRONG C-XX` tag. Criterion tags are co-located with the violating field: C-06
tags appear at `name:` fields where namespace labels occur, not at adjacent lines. Study all
seven tags before filling the template.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label — stage names
                                                 #   must state evidence intent, not namespace
                                                 #   CORRECT shape: "Surface competitive signals"
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "execute scout:feasibility"          # WRONG C-04: execution gate — gates name
                                                 #   artifact presence, not skill calls
                                                 # WRONG C-07: executor framing — plan identity
                                                 #   disallows run/execute language in gates

    - name: "draft-phase"                        # WRONG C-06: namespace label — name the
                                                 #   evidence goal, not the namespace
                                                 #   CORRECT shape: "Shape the concept"
      skills:
        - review:design                          # WRONG C-05: review:design before draft:spec —
                                                 #   the reviewed artifact has not been produced yet
        - draft:brief                            # WRONG C-03: "draft:brief" not a Signal skill
                                                 #   CORRECT: draft:spec, draft:proposal
      gate: "draft phase complete"               # WRONG C-07: executor framing

    - name: "validate"
      skills:                                    # WRONG C-01: empty skills list in non-echo stage —
                                                 #   each non-echo stage must list ≥1 skill
      gate: "validated"

# WRONG C-02: no echo final stage — the final stage must always be:
#   - name: echo
#   - auto: true
#   - skills: []
```

---

## Correction table — consult before authoring any field

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| skills: (empty, non-echo stage) | skills: [≥1 valid Signal skill] | C-01 |
| (missing echo final stage) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| draft:brief | draft:spec | C-03 |
| draft:outline | draft:proposal | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| scout:analysis | scout:competitors | C-03 |
| prove:analysis | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| gate: "execute [skill]" | gate: "[artifact] present" | C-04 |
| gate: "run all skills" | gate: "[artifact name(s)] present" | C-04 |
| gate: "phase complete" | gate: "[artifact] present" | C-04 |
| review:design before draft:spec | draft:spec must precede review:design | C-05 |
| flow:lifecycle before draft:spec | draft:spec must precede flow:lifecycle | C-05 |
| name: "scout-phase" | name: "Surface signals" (intent label) | C-06 |
| name: "draft-phase" | name: "Shape the concept" (intent label) | C-06 |
| gate: "execute..." / "run..." | gate: "[artifact] present" — plan identity | C-07 |
| gate: "[stage] complete" / "done" | gate: "[artifact] present" — plan identity | C-07 |

---

## YAML template

Zone 1 (Discovery) has no upstream dependencies — no dep reminders.
Zones 2, 3, 4 are dependency-bearing — each carries full four-mechanism density.

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Zone 1: Discovery — no upstream dependencies
    - name: ""                                          # evidence-intent label
      skills:                                           # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run all discovery skills"             # WRONG C-04 — Why: gate checks artifact presence, not execution history
      gate_pass: "feasibility + competitors artifacts present"   # correct shape (contrast only)
      gate: ""                                          # check correction table: gate values

    # Zone 2: Shape — depends on Discovery artifacts
    # requires: [Discovery artifact] from Zone: Discovery (C-05)
    - name: ""                                          # evidence-intent label
      # requires: [Discovery artifact] from Zone: Discovery (C-05)
      skills:                                           # requires: [Discovery artifact] from Zone: Discovery (C-05)
                                                        # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                      # WRONG C-07 — Why: plan identity disallows completion-state gates; name the artifact instead
      gate_pass: "spec artifact present"                # correct shape (contrast only)
      gate: ""                                          # check correction table: gate values

    # Zone 3: Challenge — depends on Shape artifacts
    # requires: [Shape artifact] from Zone: Shape (C-05)
    - name: ""                                          # evidence-intent label
      # requires: [Shape artifact] from Zone: Shape (C-05)
      skills:                                           # requires: [Shape artifact] from Zone: Shape (C-05)
                                                        # check correction table: skill names
        - ""
        - ""
      gate_fail: "challenge phase done"                 # WRONG C-07 — Why: "done" is execution state; a gate inspects artifact existence
      gate_pass: "design review artifact present"       # correct shape (contrast only)
      gate: ""                                          # check correction table: gate values

    # Zone 4: Validate — depends on Challenge artifacts
    # requires: [Challenge artifact] from Zone: Challenge (C-05)
    - name: ""                                          # evidence-intent label
      # requires: [Challenge artifact] from Zone: Challenge (C-05)
      skills:                                           # requires: [Challenge artifact] from Zone: Challenge (C-05)
                                                        # check correction table: skill names
        - ""
      gate_fail: "validation done"                      # WRONG C-04 — Why: phase completion is not artifact presence; gate must name an artifact
      gate_pass: "validation artifact present"          # correct shape (contrast only)
      gate: ""                                          # check correction table: gate values

    # Zone 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

At every dependency-bearing zone (Zones 2–4):
- Dep reminder (`# requires: ... from Zone: ... (C-05)`) appears at BOTH the zone-header
  comment AND the `skills:` placeholder line — uniform syntax at both positions
- At the `skills:` line: the dep reminder and the correction-table bridge
  (`# check correction table: skill names`) coexist independently — each serves a distinct
  purpose; neither substitutes for the other
- Fill `gate:` using the correction table; `gate_fail:` and `gate_pass:` are contrast
  examples only — do not copy them into `gate:`
- Both the BAD PLAN and the correction table cover all 7 criteria — consult both before
  authoring any field
````

---

## Summary table

| Variate | Primary axis | C-34 | C-35 | C-36 | C-37 | Correction table tier |
|---------|-------------|------|------|------|------|-----------------------|
| V-01 | C-36 header label accuracy | PASS | FAIL | **PASS** | incidental | essential only |
| V-02 | C-37 field-level C-06 annotation | FAIL | PASS | PASS | **PASS** | all 7 |
| V-03 | C-37 under lifecycle format axis | FAIL | FAIL | PASS | **PASS** | essential only |
| V-04 | C-36 + C-37 combined | PASS | PASS | **PASS** | **PASS** | all 7 |
| V-05 | Golden synthesis (all R10 + C-36 + C-37) | PASS | PASS | **PASS** | **PASS** | all 7 |

**Design decisions**:

- V-01 keeps correction table essential-only to isolate C-36 from C-35 (dual error-format coverage). C-37 passes incidentally because the `name:` field annotation structure is unchanged from R10 V-01.
- V-02 introduces the displacement anti-pattern teaching block — the only variate that explicitly demonstrates WHERE the C-06 tag must not go before showing where it must. C-34 absent to confirm C-37 independence.
- V-03 tests C-37 robustness across a structurally different format (arc phases as document sections rather than numbered zones), verifying that field-level co-location discipline is format-invariant.
- V-04 confirms C-36 and C-37 are orthogonal — C-36 targets the BAD PLAN header string, C-37 targets annotation position within the BAD PLAN body, C-34 targets `gate_fail:` fields in the YAML template; three non-overlapping sections.
- V-05 is the intended golden synthesis. C-36 and C-37 add to a fully-loaded R10 V-05 baseline without displacing any existing mechanism.
