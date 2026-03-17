---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 1
rubric: trace-skill-rubric-v1-2026-03-15.md
---

# trace-skill -- Variations R1 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

---

## V-01 -- Single axis: Phrasing register (formal/technical, imperative)

**Axis**: Phrasing register -- formal lifecycle terminology, imperative verbs, explicit label enforcement.

**Hypothesis**: Formal imperative language makes each phase deterministic and labels unambiguous. Risk: over-constrains Execute, suppresses qualitative spec-gap reasoning.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### PHASE 1 -- SETUP

Read the skill spec at `{{skill_spec_path}}`. Record the following before executing any simulation:

- **TOPIC**: Topic parsed from invocation
- **SCOPE**: What is in scope; what is explicitly excluded
- **ROLE-SELECTION**: Stock roles active; any custom roles from `.craft/roles/signal/`
- **STACK-DETECTION**: Method used (package.json / tsconfig / CLAUDE.md assertion); result
- **UNDEFINED-INPUTS**: Any required input that cannot be determined from the spec or repo

Record each undefined input as a Setup Gap (SG-NN). Do not infer silently. A silent inference
in Setup produces an unverifiable Execute trace.

**Phase gate**: Do not begin Phase 2 until TOPIC, SCOPE, and ROLE-SELECTION are confirmed or
each undefined item is explicitly flagged as SG-NN.

---

### PHASE 2 -- EXECUTE

Carrying forward from Phase 1: confirmed TOPIC `{{topic}}`, SCOPE `{{scope}}`, roles
`{{roles}}`. Begin hand-compilation.

**Artifact target**: `{topic}-{signal}-{date}.md`

Run each stock role through their lens in the order the skill spec defines them. For each role:

1. State what the role receives (inputs from Phase 1 or prior role output)
2. State what the role produces (their contribution to the artifact)
3. Flag any decision point where a required input is absent -- record as Execute Gap (EG-NN)

Produce the complete artifact. The artifact structure must match the output format the named
skill would produce: correct section headers, naming convention `{topic}-{signal}-{date}.md`,
and content shape per the skill spec. Sections required by the spec but absent from the
hand-compiled artifact must be flagged EG-NN, not silently omitted.

---

### PHASE 3 -- FINDINGS

Carrying forward from Phase 2: artifact at path `{{artifact_path}}`, gaps SG-NN and EG-NN
recorded above.

Synthesize all gaps, ambiguities, and quality observations into a findings brief. Label each
finding P1, P2, or P3:

- **P1**: Must address before this artifact is useful as a golden baseline
- **P2**: Improves quality; optional for first use
- **P3**: Future enhancement; deferred

Minimum 2 findings required. Each finding must state the required action, not only the
observation. A finding that says "section X is present" without an action direction does not
qualify.

| ID | Finding | Severity | Action |
|----|---------|----------|--------|
| F-01 | | | |

---

### PHASE 4 -- AMEND

Carrying forward from Phase 3: highest-priority finding is `{{F-NN}}`.

Select one finding and apply it to the artifact. Record:

1. **Finding ID**: which finding drove this change
2. **Target**: which field, section, or decision was changed
3. **Change**: before and after (or addition if new content)

If no amendment is warranted, state the reason explicitly and name the finding that was
evaluated and dismissed. "Output accepted as-is" without named reasoning does not pass.

---

### VERDICT

After completing all four phases, deliver:

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Basis**: One sentence per basis. Reference at least one phase finding.

**Findings Register**:

| ID | Finding | Severity |
|----|---------|----------|

**Artifact written to**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Output format (table-anchored with usefulness score)

**Axis**: Output format -- every phase output anchors to a structured table; adds numeric
usefulness score on a 0-100 scale across four dimensions.

**Hypothesis**: Table-anchored output enforces systematic coverage and measurability per phase.
Risk: mechanical table structure produces rigid artifacts that miss qualitative spec gaps
requiring prose reasoning.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

**TRACE SCORECARD** -- fill this in after Phase 3. Do not fill now.

| Dimension | Score (0-25) | Basis |
|-----------|-------------|-------|
| Implementability (spec complete?) | | |
| Artifact fidelity (matches skill output format?) | | |
| Role coverage (all roles ran?) | | |
| Findability (spec gaps surfaced?) | | |
| **TOTAL** | **/100** | |

---

### Phase 1 -- Setup

Read `{{skill_spec_path}}`. Populate this table before proceeding:

| Input | Value | Source | Gap? |
|-------|-------|--------|------|
| Topic | | invocation | |
| Scope | | invocation | |
| Roles | | spec stock roles / .craft/roles | |
| Stack | | package.json / CLAUDE.md / fallback | |
| Spec version | | spec frontmatter | |

Mark `Gap? = YES` for any row where the value cannot be determined. A Gap?=YES row in Setup
is a spec defect, not an assumption -- label it SG-NN and carry it forward.

---

### Phase 2 -- Execute

Inputs confirmed in Phase 1 (see table above). Produce the hand-compiled artifact.

**Artifact**: `{topic}-{signal}-{date}.md`

Run each stock role. For each role, produce one table row:

| Role | Input received | Output produced | Gap found? |
|------|---------------|----------------|-----------|
| | | | |

Then produce the complete artifact body beneath the role table. The artifact must match the
output format from the skill description: every required section present, naming convention
applied, no placeholder values. Record any missing required section as EG-NN.

---

### Phase 3 -- Findings

From Phase 2 outputs. Minimum 2 rows. Each row must carry an action item.

| ID | Observation | Severity | Action |
|----|------------|----------|--------|
| F-01 | | P1/P2/P3 | |

Now return to the TRACE SCORECARD above and fill it in. Score each dimension independently.

---

### Phase 4 -- Amend

Pick the highest-severity finding from Phase 3. Apply it to the artifact.

| Field | Before | After | Finding |
|-------|--------|-------|---------|
| | | | |

If no change is made, populate the table with a single row: `Finding dismissed | [F-NN] | [reason]`.

---

### Verdict

**Score**: [total from TRACE SCORECARD] / 100
**Result**: `USEFUL` (score >= 70) | `NEEDS-REDESIGN` (score < 50) | `NEEDS-SPEC-REVISION` (gap-driven)
**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (Setup as hard gate, front-loaded findings skeleton)

**Axis**: Lifecycle emphasis -- Setup is a blocking confirmation gate; findings skeleton is
declared before Phase 2 begins (same pattern as trace-deployment golden).

**Hypothesis**: Front-loading the findings skeleton and requiring Setup confirmation before
execution begins improves C-03 and C-04 compliance. Risk: structural overhead before Execute
may reduce depth of hand-compiled artifact.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

**FINDINGS** -- do not fill this now. Return here after Phase 2.

| ID | Finding | Phase found | Severity | Action required |
|----|---------|------------|----------|----------------|

Return to this table after completing Phase 2. Add one row per spec gap or artifact defect.
Before assigning severity, compare each finding against the others -- rank by impact on
implementability, not by order of discovery.

---

### Phase 1 -- Setup (confirmation gate)

Read `{{skill_spec_path}}` and the test invocation. Confirm and record:

**what is in scope?**

Name the topic, the test scenario, and the boundary (what this trace covers and what it
explicitly excludes). If the invocation is ambiguous, surface the ambiguity here -- do not
pick an interpretation silently.

**which roles will run?**

List the stock roles the skill spec defines. If custom roles exist in `.craft/roles/signal/`,
name them. Record the role selection as: stock roles only / stock + custom / custom only.

**what context was auto-detected?**

Show what was detected from the repo (stack, contributor count, existing artifacts for this
topic) and how it was detected. Detection by inference must be labeled as such.

**GATE**: Confirm all three above before proceeding to Phase 2. If any item cannot be
confirmed, record it as SG-NN in the FINDINGS table and explain why execution cannot proceed
until it is resolved.

---

### Phase 2 -- Execute

Carrying forward from Setup: topic `{{topic}}`, scope confirmed, roles `{{roles}}`.

Produce the hand-compiled artifact as if the skill had run. The artifact:

- Is named `{topic}-{signal}-{date}.md`
- Has every section the skill spec requires
- Has no placeholder values that require post-production resolution

Run each role in sequence. Where a role encounters a missing input, a circular dependency, or
a spec ambiguity: do not infer. Record it as EG-NN, write the artifact section with the gap
explicitly marked, and continue.

After Phase 2 is complete, return to the FINDINGS table above and fill it in.

---

### Phase 3 -- Findings

Carrying forward from Phase 2: artifact at `{{artifact_path}}`, FINDINGS table populated.

Confirm each finding carries:
- A P1 / P2 / P3 label
- An action direction (not just an observation)

If the FINDINGS table has fewer than 2 entries, add at least one P3 observation that an
implementer could act on. A trace with zero findings is suspicious -- it means either the
skill spec is perfect (rare) or the trace was not rigorous enough.

---

### Phase 4 -- Amend

Carrying forward from Phase 3: highest-priority finding is `{{F-NN}}`.

Apply one finding to the artifact. Name the finding, the section changed, and the nature of
the change (addition / correction / removal). If the finding is dismissed, name it and
explain why it does not warrant a change to this artifact.

---

### Verdict

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Reasoning**: Reference the highest-severity finding. State whether the skill can be
implemented from the spec as written or whether a spec revision is required first.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Role sequence (spec-auditor first) + inertia framing

**Axes**:
- Role sequence: spec-auditor runs as Stage 1 before hand-compilation proper (Stage 2)
- Inertia framing: frames the exercise around what a developer would have to do manually
  without this skill -- sharpens Verdict into a build-vs-defer decision

**Hypothesis**: Staging a spec-auditor pass before hand-compilation surfaces implementability
gaps (C-04) before Execute begins, making the trace structurally prevent silent gap papering.
Inertia framing makes the Verdict actionable (build now vs defer vs redesign) rather than
binary (useful / not). Combined risk: two-stage overhead may produce verbose Setup at the
cost of Execute depth.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Without this skill**, a developer wanting to validate `{{skill_name}}` before implementing
it would need to: read the spec manually, mentally simulate each lifecycle phase, guess at
role outputs, and discover implementability gaps only after writing code. This trace replaces
that. The hand-compiled artifact is what the developer gets instead.

---

### STAGE 1 -- SPEC AUDIT (Spec Auditor)

You are a spec auditor. Your job is not to run the skill -- it is to determine whether the
skill can be run. Read `{{skill_spec_path}}` and answer:

**are the inputs fully defined?**

List every input the skill requires. For each input, state whether it is fully defined in the
spec or whether it requires inference, assumption, or external knowledge. An input that
requires inference is a spec gap -- label it SA-NN.

**is the role sequence unambiguous?**

Name each stock role. State the order they run in and what they receive from the prior role.
If the order is not specified, flag it SA-NN. If a role's input is the output of a prior
role but the handoff is not defined, flag it SA-NN.

**does the output format match the skill's artifact contract?**

The artifact naming convention is `{topic}-{signal}-{date}.md`. Does the spec define what
`{signal}` should be for this skill? Does the spec define every required section of the
artifact? Flag any undefined element SA-NN.

**STAGE 1 SUMMARY**: List all SA-NN gaps. If 0 gaps: proceed to Stage 2. If >= 1 P1 gap:
flag the skill as NEEDS-SPEC-REVISION and proceed to Stage 2 with caveats noted.

---

### STAGE 2 -- HAND-COMPILATION

Carrying forward from Stage 1: spec audit complete, gaps SA-NN recorded.

Now trace the full 4-phase lifecycle as if the skill had run.

#### Phase 1 -- Setup

Using the test invocation `{{invocation}}` and repo context, confirm:

- Topic: `{{topic}}`
- Scope: what is in, what is out
- Roles: stock list from spec; custom roles from `.craft/roles/signal/` if present

Record each confirmed input explicitly. Any input flagged SA-NN in Stage 1 is carried forward
here as SG-NN (Setup Gap) -- do not resolve it by assumption.

#### Phase 2 -- Execute

Carrying forward confirmed inputs. Run each role in the order Stage 1 established.
Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Where Stage 1 found a spec gap (SA-NN / SG-NN), show the gap in the artifact section it
affects. The artifact must be producible from the inputs alone. Sections that require
knowledge outside the skill's scope are Execute Gaps (EG-NN).

#### Phase 3 -- Findings

Carry forward: artifact from Phase 2, all gaps (SA-NN, SG-NN, EG-NN). Merge into a unified
findings brief.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|
| | | SA / SG / EG | P1/P2/P3 | |

Minimum 2 entries. Each must carry an action direction.

#### Phase 4 -- Amend

Apply the highest P1 finding to the artifact. If no P1 exists, apply the highest P2. State:
finding ID, section changed, change made. If dismissed, state why.

---

### Verdict

**Without this skill**: [one sentence -- what the developer had to do manually]
**With this skill**: [one sentence -- what the developer gets instead]
**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Spec revision required before implementation?**: YES / NO -- [reason]

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined axes: Phrasing register (conversational/interrogative) + lifecycle compression

**Axes**:
- Phrasing register: conversational interrogative headers ("what did Setup detect?",
  "what does the artifact look like?") -- same register as trace-deployment golden
- Lifecycle compression: Execute and Findings are structurally integrated (findings surface
  inline during Execute, then are consolidated); Amend is lean

**Hypothesis**: Colloquial interrogative phase headers activate natural carry-forward between
phases (C-05), and inline Findings during Execute surface spec gaps at the moment they are
found (C-04) rather than deferred to a separate section. Risk: integrated Execute+Findings
may blur the boundary that C-01 requires -- the phase must still be labeled and non-empty.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Setup -- what does the repo tell us before we run anything?

Read `{{skill_spec_path}}`. Before touching the test invocation, record what you can confirm
from the spec and repo context:

- what is the topic and test scenario? (from the invocation)
- what is in scope and what is out? (from the invocation + spec)
- which roles will run? (stock roles from the spec; any custom roles in `.craft/roles/signal/`)
- what did auto-detection find? (stack, contributors, existing topic artifacts)

If anything cannot be confirmed, say so here. Don't infer silently -- an unconfirmed input
in Setup becomes an unverifiable step in Execute.

---

### Execute -- what does the artifact look like when the skill runs?

Carrying forward from Setup: topic confirmed, scope set, roles ready.

Produce the hand-compiled artifact as if `/{{skill_name}}` had just run on the test invocation.
Name it `{topic}-{signal}-{date}.md`.

Run each role in sequence. For each role: what did they receive? what did they add to the
artifact? As you work through each role, call out any step where:

- a required input is not in scope or not defined in the spec
- a decision depends on information the skill cannot have at runtime
- the output format the spec describes doesn't match what naturally emerges

These are inline findings -- label them IF-NN as they appear. Keep the artifact body intact;
put inline findings as margin notes after the relevant section.

---

### Findings -- what did we learn that matters?

Carrying forward from Execute: artifact complete, inline findings IF-NN recorded.

Consolidate the inline findings into a brief. For each finding, decide: is this P1 (blocks
useful baseline), P2 (improves quality), or P3 (future)?

| ID | Finding | Severity | What to do |
|----|---------|----------|-----------|

Minimum 2 entries. "What to do" must be a concrete action, not a restatement of the problem.

---

### Amend -- what changes based on what we found?

Carrying forward from Findings: priority finding is `{{F-NN}}`.

Pick one finding and show what it changes in the artifact. Name the finding, the section, and
the change (a sentence or a diff is both fine). If nothing changes, name the finding you
considered and explain why you're leaving the artifact as-is.

---

### Verdict

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Why**: One or two sentences. Ground it in a specific finding or in the absence of any
findings. A trace that produces zero findings is evidence of insufficient rigor, not a
perfect spec.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
