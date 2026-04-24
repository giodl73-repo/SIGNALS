# program:plan — Round 9 Variates (v9 rubric)

Date: 2026-03-16

## R8 retrospective under v9 rubric

R8 V-03 introduced complete BAD PLAN criterion coverage (all 7 criteria tagged → C-31). R8
V-04 added the production `gate:` correction bridge at all non-echo zones (C-32). R8 V-05
achieved full four-mechanism coexistence at every dep-bearing zone (C-33). The v9 rubric
formalizes these as C-31, C-32, C-33 respectively, raising aspirational count to 26 and total
max to 220 pts. Golden threshold (>= 80) unchanged.

**R9 target**: V-01 through V-03 each isolate one new criterion as single-axis. V-04 combines
C-31 + C-32. V-05 is the golden synthesis: C-31 + C-32 + C-33 + C-29, preserving all R8
mechanisms.

---

## V-01 — Complete BAD-YAML Cross-Criterion Coverage (single-axis: C-31)

**Axis**: BAD PLAN block carries `# WRONG C-XX` tags for all 7 criteria (C-01 through C-07) —
both essential and recommended — making the single block a complete criterion index. Gate
structure remains simple (no three-field); dep reminders at zone-header only (no dual-position).
Correction table covers essential tier only (C-29 absent) to isolate C-31.

**Hypothesis**: A BAD PLAN block that tags all 7 criteria earns C-31 as an isolated criterion,
with C-32 and C-33 absent as controls. Expected delta over a minimal baseline: +1 aspirational
criterion pass (C-31). C-29 deliberately absent confirms independence from the correction-table
coverage axis.

---

### Prompt body

```
`program:plan` — Signal plugin skill.

You sequence Signal skills into a staged program plan for a given topic. Output: `program.yaml`.
A program plan is a plan — not an executor. It describes what evidence to gather and when
conditions are met to advance, not what to run. The final stage is always `echo` (auto: true,
no skills listed).

---

## What a broken plan looks like — complete criterion index

The BAD PLAN below tags every criterion from C-01 through C-07. At least one `# WRONG C-XX`
tag appears for each criterion. Study all seven before filling the template.

```yaml
# BAD PLAN — complete criterion index (C-01 through C-07)

program:
  topic: "{{topic}}"
  stages:
    - name: "scout-phase"                        # WRONG C-06: namespace label — stage names must
                                                 #   describe evidence intent, not namespace
                                                 #   ("Surface signals" ✓ / "scout-phase" ✗)
      skills:
        - scout:feasibility
        - scout:competitors
      gate: "run scout:feasibility"              # WRONG C-04: execution gate — gate must name
                                                 #   an artifact, not describe a skill run
                                                 # WRONG C-07: executor framing — program:plan
                                                 #   is a plan; gates do not issue run commands

    - name: "draft-phase"                        # WRONG C-06: namespace label again
      skills:
        - review:design                          # WRONG C-05: review:design placed before
                                                 #   draft:spec — the reviewed artifact has not
                                                 #   been produced yet in this plan
        - draft:brief                            # WRONG C-03: "draft:brief" is not a Signal
                                                 #   skill — check correction table: skill names
      gate: "draft phase complete"               # WRONG C-07: executor framing — "complete"
                                                 #   is not an artifact existence check

    - name: "validate"
      skills:                                    # WRONG C-01: non-echo stage has empty skills
                                                 #   list — each non-echo stage needs ≥1 skill
      gate: "validated"

# WRONG C-02: no echo final stage — the final stage must always be
#   echo with auto: true and empty skills: []
```

---

## Correction table — look up before filling template

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| skills: (empty, non-echo stage) | skills: [≥1 valid Signal skill] | C-01 |
| (missing echo final stage) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| draft:brief | draft:spec | C-03 |
| draft:outline | draft:proposal | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| prove:analysis | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| gate: "run [skill]" | gate: "[artifact name] present" | C-04 |
| gate: "execute all skills" | gate: "[artifact name(s)] present" | C-04 |
| gate: "phase complete" | gate: "[artifact] present" | C-04 |

---

## YAML template — fill all `""` placeholders; leave echo as-is

```yaml
program:
  topic: "{{topic}}"
  stages:

    - name: ""                    # evidence-intent label — what signals are being gathered
      skills:                     # check correction table: skill names
        - ""
        - ""
        - ""
      gate: ""                    # artifact existence check — not a command

    - name: ""                    # evidence-intent label
      # requires: [artifact(s)] from prior stage
      skills:                     # check correction table: skill names
        - ""
        - ""
      gate: ""                    # artifact existence check

    - name: ""                    # evidence-intent label
      # requires: [artifact(s)] from prior stages
      skills:                     # check correction table: skill names
        - ""
        - ""
      gate: ""                    # artifact existence check

    - name: ""                    # evidence-intent label
      # requires: [artifact(s)] from prior stages
      skills:                     # check correction table: skill names
        - ""
      gate: ""                    # artifact existence check

    - name: echo
      auto: true                  # final stage — always echo, no skills listed
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

Rules:
1. Stage names state the evidence goal — not the namespace, not an executor phrase
2. Skills are valid Signal skill calls (check correction table for wrong-to-correct pairs)
3. Gates check artifact existence — never execution state, never phase completion
4. Dependencies flow forward — skills that review, trace, or validate an artifact come after
   the stage that produced it
5. Final stage is always echo (auto: true, skills: [])
```

---

## V-02 — Production Gate Field Correction Bridge (single-axis: C-32)

**Axis**: Three-field gate structure (`gate_fail:` / `gate_pass:` / `gate:`) at every non-echo
zone (C-28 prerequisite), with the production `gate:` sibling carrying an explicit
`# check correction table: gate values` bridge at the field position itself — not only at the
contrast fields. The bridge appears at the production slot so the model encounters the lookup
pointer at the moment it fills the gate. Phrasing register: conversational.

**Hypothesis**: Three-field structure (C-28) combined with a correction bridge at `gate:`
specifically (not at `gate_fail:` or `gate_pass:` only) earns C-32 across all non-echo zones.
C-31 absent (BAD PLAN covers essential tier only). C-33 absent (no dual dep reminders).
Expected: C-32 + C-28 + C-18 pass. C-33 absent as control.

---

### Prompt body

```
You're running `program:plan`. Your job is to turn a Signal investigation into a staged
program plan — stages with names, skills, and gates. The output is `program.yaml`. The last
stage is always echo (auto: true). You're building a plan, not a runner.

---

## Here's a plan that breaks things

```yaml
# BAD PLAN — essential criterion violations

program:
  topic: "{{topic}}"
  stages:
    - name: "discover"
      skills:
        - scout:feasibility
        - scout:analysis              # WRONG C-03: "scout:analysis" is not a Signal skill
      gate: "run discovery skills"    # WRONG C-04: execution gate

    - name: "design"
      skills:
        - draft:spec
        - flow:trace                  # WRONG C-03: "flow:trace" is not a Signal skill
      gate: "design stage done"       # WRONG C-04: execution gate / WRONG C-07: executor framing

    - name: "verify"
      skills:                         # WRONG C-01: empty skills list in non-echo stage
      gate: "verified"

# WRONG C-02: missing echo final stage
```

---

## Correction table

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| gate: "run any skills" | gate: "[artifact] present" | C-04 |
| gate: "stage done" | gate: "[artifact name] present" | C-04 |
| gate: "phase complete" | gate: "[artifact(s)] present" | C-04 |
| scout:analysis | scout:competitors | C-03 |
| flow:trace | flow:lifecycle | C-03 |
| listen:surveys | listen:feedback | C-03 |
| prove:analysis | prove:interview | C-03 |
| draft:brief | draft:spec | C-03 |
| (missing echo) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| skills: (empty, non-echo) | skills: [≥1 Signal skill] | C-01 |

---

## YAML template

At every non-echo zone: `gate_fail:` and `gate_pass:` are contrast examples — do not copy
them into your `gate:` value. `gate:` is the production slot you fill. Use the correction table
to verify your gate value before writing it.

```yaml
program:
  topic: "{{topic}}"
  stages:

    - name: ""                              # evidence-intent stage label
      skills:                              # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run all scout skills"    # contrast only — WRONG: execution gate
      gate_pass: "feasibility + competitors artifacts present"  # contrast only — correct shape
      gate: ""                             # check correction table: gate values

    - name: ""                              # evidence-intent stage label
      # requires: [artifact] from prior stage
      skills:                              # check correction table: skill names
        - ""
        - ""
      gate_fail: "draft phase complete"    # contrast only — WRONG: executor framing
      gate_pass: "spec artifact present"   # contrast only — correct shape
      gate: ""                             # check correction table: gate values

    - name: ""                              # evidence-intent stage label
      # requires: [artifact] from prior stage
      skills:                              # check correction table: skill names
        - ""
        - ""
      gate_fail: "review done"             # contrast only — WRONG: executor framing
      gate_pass: "design review artifact present"  # contrast only — correct shape
      gate: ""                             # check correction table: gate values

    - name: ""                              # evidence-intent stage label
      # requires: [artifact] from prior stage
      skills:                              # check correction table: skill names
        - ""
      gate_fail: "validation complete"     # contrast only — WRONG: executor framing
      gate_pass: "validation artifact(s) present"  # contrast only — correct shape
      gate: ""                             # check correction table: gate values

    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

Fill `gate:` at every non-echo stage. The `gate_fail:` and `gate_pass:` lines are teaching
examples — leave them as written, do not copy them as your gate value. Use the correction
table's gate values column to verify your gate string before writing it.
```

---

## V-03 — Maximal Zone Teaching Density (single-axis: C-33)

**Axis**: Every dependency-bearing non-echo zone simultaneously carries all four annotation
mechanisms: (a) three-field gate structure with criterion-tagged `gate_fail:` (C-28 + C-26);
(b) production `gate:` with correction bridge (C-32); (c) dual-position dep reminder in
uniform syntax at zone-header AND `skills:` line (C-27); (d) independent dep reminder +
correction bridge coexisting at `skills:` line (C-30). BAD PLAN covers essential tier only
(C-31 absent to isolate the zone-density axis). Phrasing: imperative/directive.

**Hypothesis**: Full four-mechanism coexistence at every dep-bearing zone earns C-33 plus all
five prerequisites (C-26, C-27, C-28, C-30, C-32) in a single variation. C-31 absent confirms
independence from the BAD PLAN criterion-coverage axis. Expected: +6 aspirational criteria
pass (C-26, C-27, C-28, C-30, C-32, C-33) over a minimal baseline.

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
# BAD PLAN — essential violations only

program:
  topic: "{{topic}}"
  stages:
    - name: "gather"
      skills:
        - scout:feasibility
        - scout:brief                  # WRONG C-03: "scout:brief" not a Signal skill
      gate: "run gather stage"         # WRONG C-04: execution gate

    - name: "build"
      skills:
        - draft:concept                # WRONG C-03: "draft:concept" not a Signal skill
      gate: "build stage complete"     # WRONG C-04: execution gate / WRONG C-07: executor framing

    - name: "check"
      skills:                          # WRONG C-01: empty skills list — non-echo stage needs ≥1 skill
      gate: "checked"

# WRONG C-02: no echo stage — final stage must be echo (auto: true)
```

---

## Correction table

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| gate: "run [stage]" | gate: "[artifact] present" | C-04 |
| gate: "[stage] complete" | gate: "[artifact name] present" | C-04 |
| scout:brief | scout:stakeholders | C-03 |
| draft:concept | draft:spec | C-03 |
| flow:process | flow:lifecycle | C-03 |
| prove:validation | prove:interview | C-03 |
| listen:surveys | listen:feedback | C-03 |
| (no echo) | - name: echo\n  auto: true\n  skills: [] | C-02 |
| skills: (empty, non-echo) | skills: [≥1 valid skill] | C-01 |

---

## YAML template

Zone 1 (Discovery) has no upstream dependencies — no dep reminders.
Zones 2, 3, 4 are dependency-bearing — each carries all four annotation mechanisms.

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Zone 1: Discovery — no upstream dependencies
    - name: ""                                    # evidence-intent label
      skills:                                     # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run all scout skills"           # WRONG C-04: execution gate (contrast only)
      gate_pass: "feasibility + competitors artifacts present"  # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Zone 2: Shape — depends on Discovery artifacts
    # requires: [Discovery artifact] from Zone: Discovery (C-05)
    - name: ""                                    # evidence-intent label
      # requires: [Discovery artifact] from Zone: Discovery (C-05)
      skills:                                     # requires: [Discovery artifact] from Zone: Discovery (C-05)
                                                  # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                # WRONG C-07: executor framing (contrast only)
      gate_pass: "spec artifact present"          # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Zone 3: Challenge — depends on Shape artifacts
    # requires: [Shape artifact] from Zone: Shape (C-05)
    - name: ""                                    # evidence-intent label
      # requires: [Shape artifact] from Zone: Shape (C-05)
      skills:                                     # requires: [Shape artifact] from Zone: Shape (C-05)
                                                  # check correction table: skill names
        - ""
        - ""
      gate_fail: "challenge phase done"           # WRONG C-07: executor framing (contrast only)
      gate_pass: "design review artifact present" # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Zone 4: Validate — depends on Challenge artifacts
    # requires: [Challenge artifact] from Zone: Challenge (C-05)
    - name: ""                                    # evidence-intent label
      # requires: [Challenge artifact] from Zone: Challenge (C-05)
      skills:                                     # requires: [Challenge artifact] from Zone: Challenge (C-05)
                                                  # check correction table: skill names
        - ""
      gate_fail: "validation done"                # WRONG C-07: executor framing (contrast only)
      gate_pass: "validation artifact present"    # correct shape (contrast only)
      gate: ""                                    # check correction table: gate values

    # Zone 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

At every dependency-bearing zone (Zones 2–4):
- The dep reminder (`# requires: ... from Zone: ... (C-05)`) appears at BOTH the zone-header
  comment AND the `skills:` placeholder line — same syntax at both positions
- At the `skills:` line: the dep reminder and the correction-table bridge (`# check correction
  table: skill names`) coexist as independent annotations — neither substitutes for the other
- Fill `gate:` using the correction table; `gate_fail:` and `gate_pass:` are contrast examples
```

---

## V-04 — Combination: C-31 + C-32

**Axis**: BAD PLAN block carries `# WRONG C-XX` tags for all 7 criteria (C-31), AND production
`gate:` field carries correction bridge at every non-echo zone (C-32). Three-field structure
present as C-32 prerequisite (C-28). Dep reminders at zone-header only (C-27 absent; C-33
absent to test additivity). Lifecycle emphasis: explicit zone-level phase boundary markers.

**Hypothesis**: C-31 and C-32 are additive and jointly achievable. The complete BAD PLAN
criterion index (C-31) operates on the BAD PLAN section; the production gate: bridge (C-32)
operates on the YAML template zones — two non-overlapping sections. C-33 absent confirms that
the pair does not require full zone-density to coexist. Expected: C-31 + C-32 both pass, C-33
fails as intended control.

---

### Prompt body

```
`program:plan` — Signal plugin skill.

Stage a Signal investigation for topic: {{topic}}. Output: `program.yaml` — stages with name,
skills, gate — plus final echo. Plan identity: you are planning evidence-gathering, not
executing it. A gate checks that artifacts exist, not that skills have run.

---

## The complete failure catalog — all 7 criteria tagged

Every criterion from C-01 through C-07 appears at least once below. This block is the
complete criterion index for program:plan.

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
                                                   #   has not been produced at this point
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

## Correction table

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
| gate: "stage done" | gate: "[artifact] present" | C-04 |

---

## YAML template

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Phase 1: Discovery
    - name: ""                               # evidence-intent label
      skills:                               # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run scout skills"         # contrast only — WRONG: execution gate
      gate_pass: "feasibility + competitors artifacts present"  # contrast only — correct shape
      gate: ""                              # check correction table: gate values

    # Phase 2: Shape
    - name: ""                               # evidence-intent label
      # requires: [artifact] from Phase 1
      skills:                               # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"          # contrast only — WRONG: executor framing
      gate_pass: "spec artifact present"    # contrast only — correct shape
      gate: ""                              # check correction table: gate values

    # Phase 3: Challenge
    - name: ""                               # evidence-intent label
      # requires: [artifact] from Phase 2
      skills:                               # check correction table: skill names
        - ""
        - ""
      gate_fail: "review done"              # contrast only — WRONG: executor framing
      gate_pass: "design review artifact present"  # contrast only — correct shape
      gate: ""                              # check correction table: gate values

    # Phase 4: Validate
    - name: ""                               # evidence-intent label
      # requires: [artifact] from Phase 3
      skills:                               # check correction table: skill names
        - ""
      gate_fail: "validation complete"      # contrast only — WRONG: executor framing
      gate_pass: "validation artifact present"  # contrast only — correct shape
      gate: ""                              # check correction table: gate values

    # Phase 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

At every non-echo phase: fill `gate:` using the correction table's gate values column. The
`gate_fail:` and `gate_pass:` lines are contrast examples — do not copy them into `gate:`.
```

---

## V-05 — Golden synthesis: C-31 + C-32 + C-33

**Axis**: All three new R9 criteria combined. BAD PLAN block carries all 7 criterion tags (C-31).
Every dep-bearing zone carries full four-mechanism density: criterion-tagged `gate_fail:` (C-26),
three-field structure (C-28), production `gate:` correction bridge (C-32), dual dep reminders at
zone-header AND `skills:` line (C-27), and independent dep reminder + correction bridge at
`skills:` line (C-30) — all coexisting (C-33). Correction table covers all 7 criteria including
recommended tier (C-29). Incorporates all R8 V-05 mechanisms as foundation. Phrasing:
descriptive/intent-forward.

**Hypothesis**: C-31, C-32, and C-33 are mutually compatible and jointly achievable. The R8
V-05 four-mechanism zone structure absorbs C-31 (BAD PLAN upgrade) and the full C-32 bridge
at `gate:` without structural collision. C-29 (recommended-tier correction table coverage) is
a natural add given the full correction table. Expected near-maximum composite with all R8
achieved criteria preserved.

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
| name: "scout-phase" | name: "Surface signals" (intent label) | C-06 |
| name: "draft-phase" | name: "Shape the concept" (intent label) | C-06 |
| gate: "execute..." / "complete" | gate: "[artifact] present" — plan identity | C-07 |

---

## YAML template

Zone 1 (Discovery) has no upstream dependencies — no dep reminders.
Zones 2, 3, 4 are dependency-bearing — each carries full four-mechanism density.

```yaml
program:
  topic: "{{topic}}"
  stages:

    # Zone 1: Discovery — no upstream dependencies
    - name: ""                                     # evidence-intent label
      skills:                                      # check correction table: skill names
        - ""
        - ""
        - ""
      gate_fail: "run all discovery skills"        # WRONG C-04: execution gate (contrast only)
      gate_pass: "feasibility + competitors artifacts present"  # correct shape (contrast only)
      gate: ""                                     # check correction table: gate values

    # Zone 2: Shape — depends on Discovery artifacts
    # requires: [Discovery artifact] from Zone: Discovery (C-05)
    - name: ""                                     # evidence-intent label
      # requires: [Discovery artifact] from Zone: Discovery (C-05)
      skills:                                      # requires: [Discovery artifact] from Zone: Discovery (C-05)
                                                   # check correction table: skill names
        - ""
        - ""
      gate_fail: "drafts complete"                 # WRONG C-07: executor framing (contrast only)
      gate_pass: "spec artifact present"           # correct shape (contrast only)
      gate: ""                                     # check correction table: gate values

    # Zone 3: Challenge — depends on Shape artifacts
    # requires: [Shape artifact] from Zone: Shape (C-05)
    - name: ""                                     # evidence-intent label
      # requires: [Shape artifact] from Zone: Shape (C-05)
      skills:                                      # requires: [Shape artifact] from Zone: Shape (C-05)
                                                   # check correction table: skill names
        - ""
        - ""
      gate_fail: "challenge phase done"            # WRONG C-07: executor framing (contrast only)
      gate_pass: "design review artifact present"  # correct shape (contrast only)
      gate: ""                                     # check correction table: gate values

    # Zone 4: Validate — depends on Challenge artifacts
    # requires: [Challenge artifact] from Zone: Challenge (C-05)
    - name: ""                                     # evidence-intent label
      # requires: [Challenge artifact] from Zone: Challenge (C-05)
      skills:                                      # requires: [Challenge artifact] from Zone: Challenge (C-05)
                                                   # check correction table: skill names
        - ""
      gate_fail: "validation done"                 # WRONG C-07: executor framing (contrast only)
      gate_pass: "validation artifact present"     # correct shape (contrast only)
      gate: ""                                     # check correction table: gate values

    # Zone 5: Echo — always last
    - name: echo
      auto: true
      skills: []
```

Write a `program.yaml` for topic: {{topic}}

At every dependency-bearing zone (Zones 2–4):
- Dep reminder (`# requires: ... from Zone: ... (C-05)`) appears at BOTH the zone-header
  comment line AND the `skills:` placeholder line — uniform syntax at both positions
- At the `skills:` line: the dep reminder and the correction-table bridge
  (`# check correction table: skill names`) coexist independently — each serves a distinct
  purpose; neither substitutes for the other
- Fill `gate:` using the correction table; `gate_fail:` and `gate_pass:` are contrast
  examples only — do not copy them into `gate:`
```
