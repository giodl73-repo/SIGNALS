# program:plan — Round 10 Variates (v10 rubric)

Date: 2026-03-16

## R9 retrospective under v10 rubric

R9 V-01 introduced complete BAD-PLAN criterion coverage (all 7 criteria tagged → C-31). R9
V-02 added the production `gate:` correction bridge at all non-echo zones (C-32). R9 V-05
achieved golden synthesis with C-31+C-32+C-33+C-29 all coexisting. The v10 rubric formalizes
C-34 (compound `gate_fail:` annotation: both criterion tag AND `Why:` at the field line, not
split between field-inline and header positions) and C-35 (dual error-format recommended
coverage: C-29 AND C-31 both passing simultaneously), raising aspirational count to 28 and
total max to 230 pts. Golden threshold (>= 80) unchanged.

**R10 target**: V-01 isolates C-34 as single-axis. V-02 isolates C-35 as single-axis. V-03
tests C-34 under a different structural axis (inertia framing). V-04 combines C-34 + C-35.
V-05 is the golden synthesis: C-34 + C-35 + all R9 V-05 mechanisms preserved.

---

## V-01 — Compound gate_fail: Annotation (single-axis: C-34)

**Axis**: Every non-echo zone's `gate_fail:` field carries both an inline criterion tag
(`# WRONG C-XX`) AND an inline `Why:` explanation at the same field line — not split between
the field value and a surrounding header comment. BAD PLAN covers essential tier only (C-31
absent, to isolate). Correction table covers essential tier only (C-29 absent, to isolate).
Full four-mechanism zone density preserved from R9 (C-33 prerequisite chain intact). Phrasing:
technical/imperative.

**Hypothesis**: Compound annotation (`# WRONG C-XX — Why: [principle]`) at every `gate_fail:`
field earns C-34 as an isolated criterion. C-35 absent (BAD PLAN essential-tier only,
correction table essential-tier only) confirms C-34 independence from dual error-format
recommended coverage. Expected delta: +1 aspirational criterion pass (C-34) over R9 V-05
baseline, C-35 fails as intended control.

---

### Prompt body

```
`program:plan` — Signal plugin skill.

Output: `program.yaml`. Stages: name (evidence intent), skills (Signal skill calls), gate
(artifact existence check). Final stage: echo (auto: true, skills: []). You are a planner —
not an executor.

---

## Do not do this

```yaml
# BAD PLAN — essential violations (C-01 through C-04)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label (not evidence intent)
      skills:
        - scout:feasibility
        - scout:analysis                         # WRONG C-03: "scout:analysis" not a Signal skill
      gate: "run discovery skills"               # WRONG C-04: execution gate

    - name: "draft-phase"                        # WRONG C-06: namespace label
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
```

---

## V-02 — Dual Error-Format Recommended Coverage (single-axis: C-35)

**Axis**: BAD PLAN block carries `# WRONG C-XX` tags for all 7 criteria including C-05, C-06,
C-07 (satisfying C-31), AND correction table has recommended-tier rows for all three
recommended criteria (satisfying C-29). C-31 + C-29 = C-35. The `gate_fail:` fields carry
criterion tags but NO inline `Why:` explanation (C-34 absent, to isolate). Three-field
structure and production gate bridge present (C-24, C-28, C-32). Dep reminders at both
positions (C-27, C-30). Phrasing: descriptive/intent-forward.

**Hypothesis**: C-31 and C-29 are jointly achievable in a single prompt, satisfying C-35's
dual-format requirement. C-34 absent (no `Why:` at `gate_fail:`) confirms independence from
compound annotation axis. Expected: C-31 + C-29 + C-35 all pass; C-34 fails as intended
control.

---

### Prompt body

```
`program:plan` — Signal plugin skill.

You are planning a Signal investigation for topic: {{topic}}. A program plan sequences
evidence-gathering skills into stages with gates. Output: `program.yaml`. The final stage is
always `echo` (auto: true, skills: []). You are a planner — not an executor.

---

## Complete error map — all 7 criteria illustrated

Every criterion from C-01 through C-07 appears with at least one `# WRONG C-XX` tag below.
Study all seven before filling the template.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label — stage names must
                                                 #   state evidence intent, not namespace
                                                 #   CORRECT shape: "Surface signals"
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "execute scout:feasibility"          # WRONG C-04: execution gate — gates name
                                                 #   artifact presence, not skill invocations
                                                 # WRONG C-07: executor framing — plan identity
                                                 #   disallows run/execute language

    - name: "draft-phase"                        # WRONG C-06: namespace label
      skills:
        - review:design                          # WRONG C-05: review:design before draft:spec —
                                                 #   reviewed artifact has not been produced yet
        - draft:brief                            # WRONG C-03: "draft:brief" not a Signal skill
                                                 #   CORRECT: draft:spec, draft:proposal
      gate: "draft phase complete"               # WRONG C-07: executor framing

    - name: "validate"
      skills:                                    # WRONG C-01: empty skills list in non-echo stage —
                                                 #   each non-echo stage must list ≥1 skill
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
      gate_fail: "run scout skills"               # WRONG C-04: execution gate (contrast only)
      gate_pass: "feasibility + competitors artifacts present"  # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 2: Shape
    - name: ""                                    # evidence-intent label
      # requires: [artifact] from Phase 1 (C-05)
      skills:                                     # requires: [artifact] from Phase 1 (C-05)
                                                  # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                # WRONG C-07: executor framing (contrast only)
      gate_pass: "spec artifact present"          # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 3: Challenge
    - name: ""                                    # evidence-intent label
      # requires: [artifact] from Phase 2 (C-05)
      skills:                                     # requires: [artifact] from Phase 2 (C-05)
                                                  # check correction table: skill names
        - ""
        - ""
      gate_fail: "review done"                    # WRONG C-07: executor framing (contrast only)
      gate_pass: "design review artifact present" # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Phase 4: Validate
    - name: ""                                    # evidence-intent label
      # requires: [artifact] from Phase 3 (C-05)
      skills:                                     # requires: [artifact] from Phase 3 (C-05)
                                                  # check correction table: skill names
        - ""
      gate_fail: "validation complete"            # WRONG C-04: execution gate (contrast only)
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
```

---

## V-03 — C-34 with Inertia Framing (axes: C-34 + inertia framing)

**Axis**: C-34 compound `gate_fail:` annotation (criterion tag + `Why:` inline) combined with
prominent inertia framing — the status-quo alternative ("ad hoc skill runs with no sequence or
gates") is explicitly named in the opening to motivate the plan's artifact-gate structure. BAD
PLAN essential tier only (C-31 absent). Correction table essential tier only (C-29 absent).
Dep reminders at both zone-header and `skills:` line (C-27, C-30). Phrasing: conversational.

**Hypothesis**: Inertia framing does not impede C-34 acquisition — compound annotation is
robust across phrasing registers. The inertia frame may improve plan-identity understanding
(C-07) as a side effect by making the executor/planner distinction concrete. C-35 absent
(essential correction table only) confirms isolation from dual-format coverage axis. Expected:
C-34 passes; C-31/C-29/C-35 absent as intended controls.

---

### Prompt body

```
You're running `program:plan`. Without a plan, you'd just run Signal skills ad hoc — no
sequence, no gates, no way to know when evidence is sufficient to advance. A program plan
fixes that: staged evidence-gathering with artifact gates that say when you're ready to move.

Output: `program.yaml`. Final stage: always echo (auto: true, skills: []). You are a planner
— not a runner.

---

## What goes wrong without discipline

```yaml
# BAD PLAN — essential violations (C-01 through C-04)

program:
  topic: "{{topic}}"
  stages:
    - name: "information-gathering"
      skills:
        - scout:feasibility
        - scout:brief                            # WRONG C-03: "scout:brief" not a Signal skill
      gate: "gather enough info"                 # WRONG C-04: execution gate — what artifact proves this?

    - name: "spec-writing"
      skills:
        - draft:outline                          # WRONG C-03: "draft:outline" not a Signal skill
        - review:design                          # WRONG C-05: review:design before any draft exists
      gate: "spec done"                          # WRONG C-04 / WRONG C-07: executor framing

    - name: "check"
      skills:                                    # WRONG C-01: empty skills list
      gate: "checked"

# WRONG C-02: no echo — the plan never closes without an echo stage
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
| gate: "gather enough info" | gate: "[artifact name] present" | C-04 |
| gate: "spec done" | gate: "[artifact] present" | C-04 |
| gate: "[stage] complete" | gate: "[artifact name] present" | C-04 |

---

## Template — with gate contrast at every zone

The difference between a plan and ad hoc runs lives in the gates. `gate_fail:` shows the
ad hoc pattern; `gate_pass:` shows the plan pattern; `gate:` is what you fill.

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Zone 1: Signal — surface what's out there (no prior artifacts yet)
    - name: ""                                             # what evidence are you gathering here?
      skills:                                              # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run signal gathering skills"             # WRONG C-04 — Why: a plan gates on artifact existence, not on having run skills
      gate_pass: "signal artifacts (feasibility, competitors) present"  # correct shape (contrast only)
      gate: ""                                             # check correction table: gate values

    # Zone 2: Shape — draft the concept (needs Zone 1 artifacts)
    # requires: [Zone 1 artifact] from Zone: Signal (C-05)
    - name: ""                                             # what evidence are you gathering here?
      # requires: [Zone 1 artifact] from Zone: Signal (C-05)
      skills:                                              # requires: [Zone 1 artifact] from Zone: Signal (C-05)
                                                           # check correction table: skill names
        - ""
        - ""
      gate_fail: "shaping phase complete"                  # WRONG C-07 — Why: plan identity requires artifact presence, not phase completion state
      gate_pass: "spec artifact present"                   # correct shape (contrast only)
      gate: ""                                             # check correction table: gate values

    # Zone 3: Challenge — stress-test the concept (needs Zone 2 artifacts)
    # requires: [Zone 2 artifact] from Zone: Shape (C-05)
    - name: ""                                             # what evidence are you gathering here?
      # requires: [Zone 2 artifact] from Zone: Shape (C-05)
      skills:                                              # requires: [Zone 2 artifact] from Zone: Shape (C-05)
                                                           # check correction table: skill names
        - ""
        - ""
      gate_fail: "challenge done"                          # WRONG C-07 — Why: "done" names execution state, not an inspectable artifact
      gate_pass: "challenge review artifact present"       # correct shape (contrast only)
      gate: ""                                             # check correction table: gate values

    # Zone 4: Prove — validate against reality (needs Zone 3 artifacts)
    # requires: [Zone 3 artifact] from Zone: Challenge (C-05)
    - name: ""                                             # what evidence are you gathering here?
      # requires: [Zone 3 artifact] from Zone: Challenge (C-05)
      skills:                                              # requires: [Zone 3 artifact] from Zone: Challenge (C-05)
                                                           # check correction table: skill names
        - ""
      gate_fail: "validation complete"                     # WRONG C-04 — Why: phase completion is not artifact presence; what artifact proves readiness?
      gate_pass: "validation artifacts present"            # correct shape (contrast only)
      gate: ""                                             # check correction table: gate values

    # Zone 5: Echo — always last, always auto
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

Fill `gate:` using the correction table — the ad hoc pattern is in `gate_fail:`, the correct
pattern is in `gate_pass:`. At dep-bearing zones (2–4): the dep reminder appears both at the
zone-header comment and at the `skills:` line — same syntax at both positions; the correction
bridge at `skills:` is independent (don't collapse the two).
```

---

## V-04 — Combination: C-34 + C-35

**Axis**: Compound `gate_fail:` annotation (C-34: criterion tag + `Why:` inline) AND dual
error-format recommended coverage (C-35: BAD PLAN all 7 criteria + correction table
recommended-tier rows). Three-field structure (C-24, C-28), production bridge at `gate:`
(C-32), dep reminders at both positions (C-27, C-30, C-33). Lifecycle emphasis: explicit
zone-level phase boundary markers with named zone sequence. Phrasing: formal/technical.

**Hypothesis**: C-34 and C-35 are additive and jointly achievable. C-34 operates on the YAML
template `gate_fail:` fields; C-35 operates on the BAD PLAN block and correction table — two
non-overlapping sections. Neither displaces the other. C-33 (R9 baseline) preserved as
foundation. Expected: C-34 + C-35 both pass along with all C-33 prerequisites.

---

### Prompt body

```
`program:plan` — Signal plugin skill.

Stage a Signal investigation for topic: {{topic}}. Output: `program.yaml` — stages with
name, skills, and gate — plus final echo stage. Plan identity: you are sequencing evidence-
gathering, not executing it. A gate checks that artifacts exist, not that skills have run.

---

## Complete failure catalog — all 7 criteria

Every criterion from C-01 through C-07 appears at least once in this block.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                          # WRONG C-06: namespace label — "scout-phase"
                                                   #   names the namespace, not the evidence goal
                                                   #   CORRECT: "Surface signals"
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "execute scout:feasibility"            # WRONG C-04: execution gate — gate must name
                                                   #   an artifact that can be inspected, not a
                                                   #   skill invocation to be run
                                                   # WRONG C-07: executor framing — "execute"
                                                   #   identifies the plan as a runner, not a plan

    - name: "draft-phase"                          # WRONG C-06: namespace label again
      skills:
        - review:design                            # WRONG C-05: review:design placed before
                                                   #   draft:spec — the artifact under review
                                                   #   has not been produced at this stage
        - draft:brief                              # WRONG C-03: "draft:brief" is not a Signal
                                                   #   skill — valid: draft:spec, draft:proposal
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
```

---

## V-05 — Golden synthesis: C-34 + C-35 + all R9 mechanisms

**Axis**: All R9 V-05 mechanisms (C-31+C-32+C-33+C-29) plus both new R10 criteria. BAD PLAN
carries all 7 criterion tags (C-31, also C-35 prerequisite). Correction table covers all 7
criteria including recommended tier (C-29, also C-35 prerequisite). C-35 = PASS (both
confirmations hold). Every non-echo zone: `gate_fail:` carries both criterion tag AND `Why:`
inline (C-34). Full four-mechanism density at all dep-bearing zones (C-26+C-27+C-30+C-32
coexisting = C-33). Phrasing: descriptive/intent-forward.

**Hypothesis**: C-34, C-35, and all R9 mechanisms are mutually compatible. C-34 adds `Why:`
to an existing criterion-tagged `gate_fail:` field without displacing C-26 (criterion tag),
C-28 (three-field structure), C-32 (production gate bridge), or C-33 (four-mechanism zone
density). C-35 is already latent in R9 V-05 (C-31 + C-29 both present) and is now explicit.
Expected near-maximum composite with all prior criteria preserved.

---

### Prompt body

```
`program:plan` — Signal plugin skill.

You are planning a Signal investigation for topic: {{topic}}. A program plan sequences
evidence-gathering skills into stages with gates. Output: `program.yaml`. The final stage is
always `echo` (auto: true, skills: []). You are a planner — not an executor.

---

## The complete error map — all 7 criteria illustrated

The BAD PLAN below is a criterion index. Every criterion from C-01 through C-07 appears with
at least one `# WRONG C-XX` tag. Study all seven tags before filling the template.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label — stage names
                                                 #   must state evidence intent, not namespace
                                                 #   CORRECT shape: "Surface signals"
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "execute scout:feasibility"          # WRONG C-04: execution gate — gates name
                                                 #   artifact presence, not skill calls
                                                 # WRONG C-07: executor framing — plan identity
                                                 #   disallows run/execute language in gates

    - name: "draft-phase"                        # WRONG C-06: namespace label
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
```
