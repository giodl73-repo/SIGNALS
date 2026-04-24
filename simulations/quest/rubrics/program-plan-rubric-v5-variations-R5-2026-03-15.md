# program-plan — R5 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. All five variations target 150/150 under the v5 rubric.

**R5 diagnostic from v5 scoring of R4 variants:**
- V-01 R4 (140/150): C-18 FAIL (no per-stage `phase:` field), C-19 FAIL (Step 6a+6b are same gate-behavior ladder; Step 3+C-12 are same question ladder — no cross-ladder consolidation)
- V-02 R4 (145/150): C-18 PASS. **C-19 FAIL** — separate enforcement steps per criterion, no cross-ladder consolidation in one block
- V-03 R4 (145/150): C-19 PASS (Check A: C-16 arc-ladder + C-17 question-ladder). **C-18 FAIL** — no per-stage `phase:` field required

**Path to 150/150** — every R5 variant must add both:
1. **C-18**: Each non-echo stage must carry a `phase:` field (or equivalent) whose value maps to a key in `evidence_arc:`. The prompt must explicitly require this field in the output schema.
2. **C-19**: A single labeled enforcement block must cover criteria from two or more different criterion ladders — with format examples for both. Valid cross-ladder pairs: arc-structure + question-framing; arc-structure + gate-behavior; gate-behavior + question-framing.

**R5 variation axes (single-axis V-01 through V-03, combinations V-04/V-05):**
- V-01: Role sequence — phase membership declared in Step 2 before catalog loaded in Step 3; C-19 via C-18+C-17 (arc+question)
- V-02: Output format — bidirectional compliance table step enforces C-18+C-09 together (arc+gate, new pair)
- V-03: Phrasing register — V-03 R4 terse extended with Rule 5 (`phase:` required) + Check D; C-19 retained via Check A (C-16+C-17)
- V-04: Combination (V-01 phase-first + new C-19 pair) — gate+question cross-enforcement: C-09+C-12 in one block
- V-05: Combination (V-03 terse + new C-19 pair) — traceability+arc cross-enforcement: C-11+C-18 in one block

---

## V-01 — Role Sequence: Phase-Declaration-First

**Axis**: Role sequence — arc phase membership for each planned stage is committed in Step 2,
before the skill catalog is consulted in Step 3.

**Hypothesis**: In R4 V-01 and V-03, stages are designed skill-first: namespace layer determines
stage membership, and arc phase is a post-hoc label. When phase declaration precedes catalog
access, the model cannot assign skills until it has committed each stage's `phase:` value —
every skill choice is downstream of arc intent, not namespace availability. This eliminates
the "scout namespace → make a scout stage" reflex and forces groupings justified by arc phase.

**C-18**: Step 2 requires each planned stage to be named and phase-assigned before catalog access.
The YAML template requires `phase:` on every non-echo stage. Check A verifies both the field
presence and its map to an `evidence_arc:` key.

**C-19**: Check A is a single labeled enforcement block covering two independent criterion
ladders — C-18 (arc-structure: phase back-references arc key) and C-17 (question-framing:
`intent:` must be interrogative, ending with `?`). Bad examples are provided for each:
a stage missing `phase:` (C-18) and a declarative statement in `intent:` (C-17).

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML: `simulations/program/plans/{topic}-program-{date}.md`.
Arc phases are declared before skills are assigned. Every stage carries its arc phase.
Every question ends with `?`. Every gate is quantified and traceable.
The program is a plan, not an executor.

---

### Step 1 — Assert the evidence arc

**Write the `evidence_arc:` block before designing any stage.**

For $TOPIC, write one specific investigative question per phase. Each value must end with `?`:

```yaml
evidence_arc:
  breadth:    "{What must be known about $TOPIC before committing to build? — ends with ?}"
  depth:      "{What must be validated once building $TOPIC begins? — ends with ?}"
  monitoring: "{What must be learned after $TOPIC ships? — ends with ?}"
```

Each question must be specific to $TOPIC — not a generic horizon question applicable to any feature.

---

### Step 2 — Declare stage phases (before selecting skills)

**List each planned stage with its arc-phase assignment. Do not select skills yet.**

```
stage 1: {strategic-name}  →  phase: breadth
stage 2: {strategic-name}  →  phase: breadth
stage 3: {strategic-name}  →  phase: depth
stage 4: {strategic-name}  →  phase: depth
stage 5: {strategic-name}  →  phase: monitoring
```

Rules:
- Phase value must be `breadth`, `depth`, or `monitoring` — a key from `evidence_arc:`
- Every arc phase must have at least one stage assigned
- Breadth stages precede depth stages; depth precedes monitoring
- Plan 3–6 non-echo stages total

---

### Step 3 — Load the skill catalog

The Signal plugin has 47 skills across 9 namespaces. Use only these names.

| Layer | Namespace | Skills |
|-------|-----------|--------|
| 1 — Breadth | `/scout:` | `competitors`, `feasibility`, `naming`, `compliance`, `market`, `stakeholders`, `positioning`, `requirements` |
| 2 — Design | `/draft:` | `spec`, `proposal`, `pitch` |
| 3 — Validation | `/review:` | `design`, `code`, `users`, `customers` |
| 3 — Validation | `/prove:` | `hypothesis`, `websearch`, `analysis`, `intelligence`, `prototype`, `synthesize`, `publish`, `interview` |
| 3 — Simulation | `/flow:` | `lifecycle`, `conversation`, `trigger`, `dataflow`, `integration`, `throttle`, `resilience` |
| 3 — Simulation | `/trace:` | `request`, `state`, `contract`, `component`, `deployment`, `migration`, `permissions` |
| 4 — Monitoring | `/listen:` | `feedback`, `support`, `adoption` |
| 5 — Synthesis | `/topic:` | `new`, `plan`, `report`, `story`, `status`, `echo` |
| Terminal | echo | `auto: true` (no skills, no gate — always final) |

Namespace-to-phase mapping: scout/draft → `breadth`; review/prove/flow/trace → `depth`;
listen/topic → `monitoring`. Layer dependency: scout → draft → review/prove/flow/trace → listen → topic.

---

### Step 4 — Assign skills and write investigative questions

For each stage from Step 2:

1. `name:` = the strategic label from Step 2. Encodes purpose: `discovery`, `de-risk`, `validate`,
   `simulate`, `synthesize`, `monitor`. NOT: `scout_stage`, `stage_1`, `layer_3`
2. `phase:` = the arc-phase from Step 2 (`breadth` | `depth` | `monitoring`)
3. `intent:` = a stage-specific investigative question answerable by this stage's skills — ends with `?`
4. `skills:` = 2+ skills from the namespace layer that maps to the declared `phase:`
   - `breadth` → scout: or draft: skills
   - `depth` → review:, prove:, flow:, or trace: skills
   - `monitoring` → listen: or topic: skills

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Each gate must:
- Name specific artifact types or signal counts (NOT: `"PM approves"`, `"done"`, `""`)
- Reference only artifacts producible by skills **in the same stage** — no forward references

---

### Step 6a — Gate quantification (C-09 — MANDATORY)

Every non-echo gate must contain `>=N`.

```
# FAILS — missing threshold:
gate: "scout-feasibility artifact present"

# PASSES — quantified:
gate: ">=2 scout signals (feasibility + requirements), 0 P1 blockers flagged"
```

Threshold patterns: `>=N {namespace} signals`, `>=N artifacts with 0 P1 open`.
Rewrite any gate missing `>=N` before proceeding.

### Step 6b — Traceability audit (C-11 — MANDATORY)

For every non-echo gate artifact, identify its producing skill in the same stage:

```
Stage: discovery (phase: breadth)
  "scout-feasibility artifact" → scout:feasibility  [OK]
  "draft-spec artifact"        → draft:spec          [OK]

Stage: validate (phase: depth)
  "review-design artifact"     → review:design       [OK]

Stage: design [PROBLEM — phase: depth, no scout skill]:
  "scout-feasibility artifact" → [NONE — FORWARD REFERENCE]
  FIX: Move scout:feasibility to a breadth-phase stage, OR rewrite gate.
```

Do not proceed to Step 7 until all gate artifacts trace to a skill in the same stage.

---

### Check A — Phase back-reference + Interrogative form (C-18 + C-17)

**Single enforcement block: arc-structure ladder (C-18) + question-framing ladder (C-17).**

For every non-echo stage, verify both:

**C-18 — `phase:` field must be present and map to an `evidence_arc:` key:**

```yaml
# BAD — phase field absent (C-18 violation):
- name: discovery
  intent: "Is the market viable for $TOPIC?"
  skills: [scout:feasibility, scout:market]
  gate: ">=2 scout signals"
  # MISSING: phase: breadth

# GOOD — phase field present, maps to evidence_arc.breadth:
- name: discovery
  phase: breadth
  intent: "Is the market viable for $TOPIC?"
  skills: [scout:feasibility, scout:market]
  gate: ">=2 scout signals"
```

**C-17 — `intent:` must be interrogative, ending with `?`:**

```
# BAD — STATEMENT, NOT A QUESTION (C-17 violation — rewrite as interrogative):
intent: "Understand the competitive landscape and confirm technical feasibility."

# GOOD — interrogative form:
intent: "Do we understand the competitive landscape and technical feasibility well enough to commit?"
```

Both checks required. A stage failing either must be rewritten before Step 7.

---

### Step 7 — Build the echo stage

```yaml
- name: echo
  auto: true
```

No additional fields. No `skills` array. No `gate` field.

---

### Step 8 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth:    "{specific breadth question, ends with ?}"
  depth:      "{specific depth/validation question, ends with ?}"
  monitoring: "{specific post-ship learning question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    phase: breadth|depth|monitoring
    intent: "{specific investigative question, ends with ?}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

---

**Final validation checklist — complete all three tiers before writing.**

**Essential tier** (all four must pass):
- [ ] **C-01** YAML valid — no unclosed brackets, bad indentation, or unquoted colons in values
- [ ] **C-02** Echo stage is last, `auto: true`, no `skills` or `gate` fields
- [ ] **C-03** Every skill name maps to the 47-skill Signal catalog
- [ ] **C-04** Every non-echo stage has a non-trivial gate condition

**Recommended tier** (all three should pass):
- [ ] **C-05** Stages in namespace layer order (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier** (all should pass — enforced by steps above):
- [ ] **C-08** Plan reflects strategic evidence arc (breadth → depth → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Step 6a enforced)
- [ ] **C-10** Every non-echo stage has strategic `name:` encoding purpose, not namespace group
- [ ] **C-11** Traceability audit complete — zero FORWARD REFERENCEs (Step 6b enforced)
- [ ] **C-12** Every non-echo stage has `intent:` as stage-specific investigative question (Step 4)
- [ ] **C-13** C-09 (Step 6a) and C-11 (Step 6b) both isolated with dedicated enforcement steps and format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ criteria
- [ ] **C-15** Every checklist item carries an explicit criterion ID (C-01 through C-19)
- [ ] **C-16** `evidence_arc:` block present in output YAML as required top-level field (Step 1 + Step 8)
- [ ] **C-17** All `intent:` and `evidence_arc:` values end with `?` — no declarative statements (Check A enforced)
- [ ] **C-18** Every non-echo stage carries `phase:` field mapping to a key in `evidence_arc:` (Step 2 + Check A enforced)
- [ ] **C-19** Check A enforces C-18 (arc-structure ladder) + C-17 (question-framing ladder) in one block with examples for each

---

## V-02 — Output Format: Bidirectional Compliance Table

**Axis**: Output format — a structured compliance table in Step 6 consolidates arc-phase
back-reference (C-18) and gate quantification (C-09) into a single machine-readable matrix
that must be filled before final YAML is written.

**Hypothesis**: R4 variants enforce C-18 and C-09 in separate blocks (V-02 R4: arc arc arc
separately; V-03 R4: Check B for C-09, Check D for C-18). Combining them in a tabular
enforcement step creates a single surface where both constraints are checked simultaneously —
the model must confirm `phase:` maps to an arc key AND `>=N` is present for each row before
proceeding. The table format makes both constraints visually parallel and equally weighted.

**C-18**: Step 4 requires `phase:` on each stage. Step 6 compliance table has a `phase maps
to arc key?` column — bad/good examples demonstrate the C-18 failure pattern explicitly.

**C-19**: Step 6 is a single labeled enforcement block covering C-18 (arc-structure ladder) +
C-09 (gate-behavior ladder). Format examples for each: a stage missing `phase:` (C-18) and
a gate missing `>=N` (C-09). Different causal chains — arc field vs. gate quantification.

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML: `simulations/program/plans/{topic}-program-{date}.md`.
The arc is a required YAML field. Every stage declares its arc phase. Every gate is quantified
and traceable. The program is a plan, not an executor.

---

### Step 1 — Load the skill catalog

| Layer | Namespace | Skills |
|-------|-----------|--------|
| 1 — Breadth | `/scout:` | `competitors`, `feasibility`, `naming`, `compliance`, `market`, `stakeholders`, `positioning`, `requirements` |
| 2 — Design | `/draft:` | `spec`, `proposal`, `pitch` |
| 3 — Validation | `/review:` | `design`, `code`, `users`, `customers` |
| 3 — Validation | `/prove:` | `hypothesis`, `websearch`, `analysis`, `intelligence`, `prototype`, `synthesize`, `publish`, `interview` |
| 3 — Simulation | `/flow:` | `lifecycle`, `conversation`, `trigger`, `dataflow`, `integration`, `throttle`, `resilience` |
| 3 — Simulation | `/trace:` | `request`, `state`, `contract`, `component`, `deployment`, `migration`, `permissions` |
| 4 — Monitoring | `/listen:` | `feedback`, `support`, `adoption` |
| 5 — Synthesis | `/topic:` | `new`, `plan`, `report`, `story`, `status`, `echo` |
| Terminal | echo | `auto: true` (no skills, no gate — always final) |

Layer dependency: scout → draft → review/prove/flow/trace → listen → topic. Echo always last.

---

### Step 2 — Write the evidence arc (required YAML output)

**The `evidence_arc:` block is a required top-level field in the output YAML.**

Write it before planning any stage. Each value ends with `?`:

```yaml
evidence_arc:
  breadth:    "{What must be known about $TOPIC before committing to build? — ends with ?}"
  depth:      "{What must be validated once building $TOPIC begins? — ends with ?}"
  monitoring: "{What must be learned after $TOPIC ships? — ends with ?}"
```

Phase mapping: scout/draft → `breadth`; review/prove/flow/trace → `depth`; listen/topic → `monitoring`.

---

### Step 3 — Write investigative questions per stage (MANDATORY)

Before grouping skills, enumerate each planned stage and its specific investigative question.
Each question must end with `?`.

```
# GOOD — stage-specific, interrogative:
discovery: "Is the market real and can we technically deliver within the identified constraints?"
validate:  "Does the proposed design pass expert review and can the core hypothesis be proved?"

# BAD — NOT INTERROGATIVE (declarative statement — rewrite as question ending with ?):
discovery: "Understand the market and confirm technical feasibility."
validate:  "Run expert review and prove the hypothesis."
```

These become the `intent:` field values.

---

### Step 4 — Group skills into stages

Group into 3–6 stages (not counting echo). For each stage:

1. `name:` = strategic label: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`.
   NOT: `scout_skills`, `stage_1`, `layer_3`
2. `phase:` = arc phase this stage satisfies: `breadth` | `depth` | `monitoring`
   (must match a key in `evidence_arc:`)
3. `intent:` = the investigative question from Step 3 (verbatim, ending with `?`)
4. `skills:` = 2+ skills from the namespace layer that maps to the declared `phase:`
5. Arc coverage check: every arc phase must have at least one stage assigned

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Gate must:
- Name specific artifact types or signal counts (NOT: `"PM approves"`, `"done"`)
- Reference only artifacts producible by skills **in the same stage**

---

### Step 6 — Compliance table (C-18 + C-09)

**Single enforcement step: arc-phase back-reference (C-18) + gate quantification (C-09).**

Fill this table for every non-echo stage before writing final YAML:

```
| Stage      | phase:      | phase maps to arc key? | gate contains >=N?                      |
|------------|-------------|------------------------|-----------------------------------------|
| discovery  | breadth     | YES (arc.breadth) [OK] | ">=2 scout signals" [OK]               |
| validate   | depth       | YES (arc.depth)   [OK] | "review artifact present" [MISSING >=N] |
| monitor    | MISSING     | NO — VIOLATION C-18    | ">=1 listen signal" [OK]               |
```

**C-18 failure pattern** — stage missing `phase:` field:

```yaml
# BAD — phase field absent (C-18 violation):
- name: validate
  intent: "Does the design pass review?"
  skills: [review:design, prove:hypothesis]
  gate: ">=1 review-design artifact"
  # MISSING: phase: depth

# GOOD — phase declared, maps to evidence_arc.depth:
- name: validate
  phase: depth
  intent: "Does the design pass review?"
  skills: [review:design, prove:hypothesis]
  gate: ">=1 review-design artifact"
```

**C-09 failure pattern** — gate missing `>=N`:

```
# BAD:  gate: "review-design artifact present"
# GOOD: gate: ">=1 review-design artifact present, 0 open P1 items"
```

Both columns must show all-OK before final YAML is written.

---

### Step 7a — Traceability audit (C-11 — MANDATORY)

For every gate artifact, identify the producing skill in the same stage:

```
Stage: discovery (phase: breadth)
  "scout-feasibility artifact" → scout:feasibility  [OK]
  "scout-market artifact"      → scout:market        [OK]

Stage: design [PROBLEM]:
  "scout-feasibility artifact" → [NONE — FORWARD REFERENCE]
  FIX: move scout:feasibility to a breadth-phase stage, OR rewrite gate.
```

### Step 7b — Echo stage

```yaml
- name: echo
  auto: true
```

No additional fields.

---

### Step 8 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth:    "{specific breadth question, ends with ?}"
  depth:      "{specific depth/validation question, ends with ?}"
  monitoring: "{specific post-ship learning question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    phase: breadth|depth|monitoring
    intent: "{specific investigative question, ends with ?}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

---

**Final validation checklist:**

**Essential tier:**
- [ ] **C-01** YAML valid — no unclosed brackets, bad indentation, or unquoted colons
- [ ] **C-02** Echo is last, `auto: true`, no `skills` or `gate` fields
- [ ] **C-03** All skills from the 47-skill Signal catalog
- [ ] **C-04** All non-echo stages have non-trivial gates

**Recommended tier:**
- [ ] **C-05** Stages in namespace layer order (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier:**
- [ ] **C-08** Plan reflects strategic evidence arc (breadth → depth → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Step 6 table enforced)
- [ ] **C-10** Every non-echo stage has strategic `name:` encoding purpose
- [ ] **C-11** All gate artifacts traceable to a skill in same stage (Step 7a enforced)
- [ ] **C-12** Every non-echo stage has `intent:` as stage-specific investigative question (Step 3)
- [ ] **C-13** C-09 (Step 6) and C-11 (Step 7a) both have dedicated labeled enforcement blocks with format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ criteria
- [ ] **C-15** Every checklist item carries an explicit criterion ID
- [ ] **C-16** `evidence_arc:` block present in output YAML (Step 2 + Step 8)
- [ ] **C-17** All `intent:` and `evidence_arc:` values end with `?` — no declarative statements (Step 3 enforced)
- [ ] **C-18** Every non-echo stage carries `phase:` field mapping to `evidence_arc:` key (Step 4 + Step 6 table enforced)
- [ ] **C-19** Step 6 compliance table enforces C-18 (arc-structure ladder) + C-09 (gate-behavior ladder) in one labeled block with examples for each

---

## V-03 — Phrasing Register: Terse + C-18 Extension

**Axis**: Phrasing register — V-03 R4's ultra-terse numbered-rules register, extended with
Rule 5 (per-stage `phase:` field required) and Check D (phase back-reference verification
with bad/good examples). C-19 is retained from V-03 R4 via Check A (C-16 + C-17).

**Hypothesis**: V-03 R4 scores 145/150 (C-19 PASS via Check A, C-18 FAIL). Adding C-18 is
a targeted insertion: Rule 5 adds the `phase:` requirement to the rules block; Check D adds
a dedicated verification step with a bad/good pair. The terse register means these two
additions expand the prompt minimally. This tests whether 150/150 can be achieved at
minimum prompt length without restructuring the existing enforcement architecture.

**C-18**: Rule 5 requires `phase:` on every non-echo stage mapping to an `evidence_arc:` key.
Check D provides a dedicated labeled verification block with bad/good format examples.

**C-19**: Unchanged from V-03 R4 — Check A enforces C-16 (arc-structure ladder: `evidence_arc:`
field presence) + C-17 (question-framing ladder: interrogative form) in one labeled block
with bad examples for each.

---

You are running `/program:plan` for Signal.

**Inputs**: Topic `$TOPIC` — Strategy `$STRATEGY`
**Output**: `simulations/program/plans/{topic}-program-{date}.md` — YAML staged plan. Plan only; not an executor.

---

**CATALOG** — 47 skills, 9 namespaces. Use only these names:

| Layer | Namespace | Skills |
|-------|-----------|--------|
| 1 | `/scout:` | `competitors`, `feasibility`, `naming`, `compliance`, `market`, `stakeholders`, `positioning`, `requirements` |
| 2 | `/draft:` | `spec`, `proposal`, `pitch` |
| 3 | `/review:` | `design`, `code`, `users`, `customers` |
| 3 | `/prove:` | `hypothesis`, `websearch`, `analysis`, `intelligence`, `prototype`, `synthesize`, `publish`, `interview` |
| 3 | `/flow:` | `lifecycle`, `conversation`, `trigger`, `dataflow`, `integration`, `throttle`, `resilience` |
| 3 | `/trace:` | `request`, `state`, `contract`, `component`, `deployment`, `migration`, `permissions` |
| 4 | `/listen:` | `feedback`, `support`, `adoption` |
| 5 | `/topic:` | `new`, `plan`, `report`, `story`, `status`, `echo` |

Layer order is mandatory: scout before draft before review/prove/flow/trace before listen before topic.

---

**RULES** — all apply without exception:

1. **Skill validity**: Every name in `skills:` must appear in CATALOG. No invented names.
2. **Stage count**: 3–6 non-echo stages. No single-skill stages. No mega-stage.
3. **Stage names**: Strategic labels only.
   - PASS: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`
   - FAIL: `scout_skills`, `stage_1`, `layer_3`, `namespace_group`
4. **Arc field required**: Output YAML must include `evidence_arc:` with keys `breadth`, `depth`,
   `monitoring`. Each value ends with `?`.
5. **Phase field required**: Every non-echo stage must declare `phase: breadth|depth|monitoring`.
   The value must match a key in `evidence_arc:`. Every arc phase must have at least one stage.
   - PASS: `phase: breadth` (matches evidence_arc.breadth)
   - FAIL: stage with no `phase:` field
   - FAIL: `phase: build` (not a key in evidence_arc:)
6. **Intent mandate**: Every non-echo stage must have `intent:` as an interrogative question ending with `?`.
   - PASS: `intent: "Is the market real and can we technically deliver?"`
   - FAIL — STATEMENT, NOT A QUESTION: `intent: "Understand the market and confirm feasibility."`
7. **Gate artifacts**: Every non-echo gate names specific artifact types. FAIL: `"PM approves"` / `"done"` / `""`.
8. **Gate quantification — MANDATORY**: Every non-echo gate contains `>=N`.
   - PASS: `gate: ">=2 scout signals (feasibility + requirements), 0 P1 blockers"`
   - FAIL: `gate: "scout-feasibility artifact present"` (threshold missing)
9. **Traceability**: Every gate artifact is producible by a skill in the same stage.
10. **Echo**: Final stage is always `- name: echo` with `auto: true`. No `skills`. No `gate`. No other fields.
11. **Layer order**: Stages observe namespace layer ordering within and across all stages.

---

**PRE-WRITE CHECKS — complete all before assembling YAML:**

**Check A — Arc field + Interrogative questions (C-16 + C-17):**

First, write the `evidence_arc:` block:

```
evidence_arc:
  breadth:    "{question for $TOPIC, ends with ?}"
  depth:      "{question for $TOPIC, ends with ?}"
  monitoring: "{question for $TOPIC, ends with ?}"
```

Then, for each non-echo stage, verify `intent:` is an interrogative question ending with `?`:

```
discovery: "Do we understand market, feasibility, and requirements well enough to commit?" [QUESTION — OK]
validate:  "Understand the design and prove the hypothesis."  [STATEMENT, NOT A QUESTION — REWRITE]
monitor:   "Are adoption signals tracking to prediction?"     [QUESTION — OK]
```

**Check B — Gate quantification (C-09):**

```
">=3 scout signals present"             [QUANTIFIED — OK]
"scout-feasibility artifact present"    [MISSING >=N — REWRITE: ">=1 scout-feasibility artifact present"]
```

**Check C — Gate traceability (C-11):**

```
Stage: discovery
  "scout-feasibility artifact" → scout:feasibility  [OK]
Stage: validate
  "review-design artifact"     → review:design       [OK]

Stage: design [PROBLEM]
  "scout-feasibility artifact" → [NO SCOUT SKILL IN THIS STAGE — FORWARD REFERENCE]
  FIX: move skill or rewrite gate.
```

**Check D — Phase back-reference (C-18):**

For each non-echo stage, verify `phase:` is present and maps to an `evidence_arc:` key:

```yaml
# BAD — phase field absent (C-18 violation):
- name: discovery
  intent: "Is the market viable?"
  skills: [scout:feasibility, scout:market]
  gate: ">=2 scout signals"
  # MISSING: phase: breadth

# GOOD — phase field present, maps to evidence_arc.breadth:
- name: discovery
  phase: breadth
  intent: "Is the market viable?"
  skills: [scout:feasibility, scout:market]
  gate: ">=2 scout signals"
```

Arc coverage: `breadth`, `depth`, and `monitoring` must each have at least one stage with
a matching `phase:` value.

---

**OUTPUT FORMAT:**

```yaml
topic: {topic}
strategy: {one-line summary}
evidence_arc:
  breadth:    "{question, ends with ?}"
  depth:      "{question, ends with ?}"
  monitoring: "{question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    phase: breadth|depth|monitoring
    intent: "{stage-specific interrogative question, ends with ?}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signals/artifacts} AND {condition}"

  - name: echo
    auto: true
```

---

**VALIDATION CHECKLIST:**

Essential tier:
- [ ] **C-01**: YAML valid — no unclosed brackets, bad indentation, or unquoted colons
- [ ] **C-02**: Echo is last, `auto: true`, no `skills` or `gate`
- [ ] **C-03**: All skills from CATALOG
- [ ] **C-04**: All non-echo stages have non-trivial gates

Recommended tier:
- [ ] **C-05**: Stages in namespace layer order
- [ ] **C-06**: Each stage has 2+ skills in a coherent grouping
- [ ] **C-07**: At least half of non-echo gates name specific artifact types

Aspirational tier:
- [ ] **C-08**: Evidence arc present — breadth → depth → monitoring
- [ ] **C-09**: Every non-echo gate has `>=N` threshold (Check B enforced)
- [ ] **C-10**: Every non-echo stage has strategic `name:` encoding purpose
- [ ] **C-11**: Every gate artifact traces to a skill in same stage (Check C enforced)
- [ ] **C-12**: Every non-echo stage has `intent:` as stage-specific interrogative question (Check A + Rule 6)
- [ ] **C-13**: C-09 (Check B) and C-11 (Check C) both have dedicated labeled enforcement blocks with examples
- [ ] **C-14**: This checklist spans Essential, Recommended, Aspirational tiers with 4+ criteria
- [ ] **C-15**: Every checklist item above carries an explicit criterion ID
- [ ] **C-16**: `evidence_arc:` block in output YAML (Rule 4 + Check A + OUTPUT FORMAT enforced)
- [ ] **C-17**: All `intent:` and `evidence_arc:` values are interrogative questions ending with `?` (Check A + Rule 6 enforced)
- [ ] **C-18**: Every non-echo stage carries `phase:` mapping to `evidence_arc:` key (Rule 5 + Check D enforced)
- [ ] **C-19**: Check A enforces C-16 (arc-structure ladder) + C-17 (question-framing ladder) in one block with bad examples for each

---

## V-04 — Combination: Phase-Declaration-First + Gate/Question Cross-Enforcement

**Axes**: Role sequence (V-01 — phase declared before skills) + new C-19 pairing: C-09
(gate-behavior ladder) + C-12 (question-framing ladder) consolidated in one labeled block.

**Hypothesis**: R4 consolidation blocks all used arc-ladder criteria as one member of the
cross-ladder pair (V-03 R4: C-16+C-17; V-02 R4: n/a). C-09+C-12 is an unexplored pairing
where both criteria involve per-stage verification: quantified gates (C-09) and per-stage
investigative questions (C-12). Combining them in one block tests whether two output-content
criteria from different ladders consolidate as naturally as arc+question pairs. Secondary:
phase-first sequencing (V-01 R5) is retained because it eliminates skill-first stage design.

**C-18**: Step 2 declares phase membership before catalog access. YAML template and Step 7
checklist both require `phase:` on every non-echo stage.

**C-19**: Check A is a single labeled enforcement block covering C-09 (gate-behavior ladder:
every gate must contain `>=N`) + C-12 (question-framing ladder: every stage must carry a
stage-specific investigative question). Bad/good format examples for each in one block.

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML: `simulations/program/plans/{topic}-program-{date}.md`.
Arc phases declared before skill assignment. Every stage declares its phase and carries
an investigative question. Every gate is quantified and traceable.
The program is a plan, not an executor.

---

### Step 1 — Assert the evidence arc

**Write the `evidence_arc:` block before designing any stage.**

```yaml
evidence_arc:
  breadth:    "{What must be known about $TOPIC before committing to build? — ends with ?}"
  depth:      "{What must be validated once building $TOPIC begins? — ends with ?}"
  monitoring: "{What must be learned after $TOPIC ships? — ends with ?}"
```

Phase mapping: scout/draft → `breadth`; review/prove/flow/trace → `depth`; listen/topic → `monitoring`.

---

### Step 2 — Declare stage phases (before selecting skills)

**Name each planned stage and assign its arc phase. Do not open the catalog yet.**

```
stage 1: {strategic-name}  →  phase: breadth
stage 2: {strategic-name}  →  phase: breadth
stage 3: {strategic-name}  →  phase: depth
stage 4: {strategic-name}  →  phase: monitoring
```

Rules:
- Phase values: `breadth`, `depth`, or `monitoring` only (keys from `evidence_arc:`)
- Every arc phase must have at least one stage; breadth before depth before monitoring
- Plan 3–6 non-echo stages total

---

### Step 3 — Load the skill catalog

| Layer | Namespace | Skills |
|-------|-----------|--------|
| 1 — Breadth | `/scout:` | `competitors`, `feasibility`, `naming`, `compliance`, `market`, `stakeholders`, `positioning`, `requirements` |
| 2 — Design | `/draft:` | `spec`, `proposal`, `pitch` |
| 3 — Validation | `/review:` | `design`, `code`, `users`, `customers` |
| 3 — Validation | `/prove:` | `hypothesis`, `websearch`, `analysis`, `intelligence`, `prototype`, `synthesize`, `publish`, `interview` |
| 3 — Simulation | `/flow:` | `lifecycle`, `conversation`, `trigger`, `dataflow`, `integration`, `throttle`, `resilience` |
| 3 — Simulation | `/trace:` | `request`, `state`, `contract`, `component`, `deployment`, `migration`, `permissions` |
| 4 — Monitoring | `/listen:` | `feedback`, `support`, `adoption` |
| 5 — Synthesis | `/topic:` | `new`, `plan`, `report`, `story`, `status`, `echo` |
| Terminal | echo | `auto: true` (no skills, no gate — always final) |

Layer dependency: scout → draft → review/prove/flow/trace → listen → topic.

---

### Step 4 — Assign skills to stages

For each stage from Step 2:

1. `name:` = strategic label encoding purpose: `discovery`, `de-risk`, `validate`, `simulate`,
   `synthesize`, `monitor`. NOT: `scout_stage`, `stage_1`, `layer_3`
2. `phase:` = arc-phase from Step 2 (`breadth` | `depth` | `monitoring`)
3. `skills:` = 2+ skills from the namespace layer that maps to the declared `phase:`

`intent:` rules (complete before writing gate conditions):
- Write a stage-specific question answerable by this stage's skills
- Must end with `?` (mandatory)
- BAD — STATEMENT, NOT A QUESTION: `"Understand the competitive landscape and confirm feasibility."`
- GOOD: `"Do we understand the competitive landscape and feasibility well enough to commit?"`

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Gate must:
- Name specific artifact types or signal counts (NOT: `"PM approves"`, `"done"`)
- Reference only artifacts producible by skills **in the same stage**

---

### Check A — Gate quantification + Investigative questions (C-09 + C-12)

**Single enforcement block: gate-behavior ladder (C-09) + question-framing ladder (C-12).**

**C-09 — Every non-echo gate must contain `>=N`:**

```
# BAD — missing threshold (C-09 violation):
gate: "scout-feasibility artifact present"

# GOOD — quantified gate:
gate: ">=2 scout signals (feasibility + requirements), 0 P1 blockers flagged"
```

**C-12 — Every non-echo stage must carry a stage-specific investigative question:**

```yaml
# BAD — intent field absent (C-12 violation):
- name: discovery
  phase: breadth
  skills: [scout:feasibility, scout:market]
  gate: ">=2 scout signals"
  # MISSING: intent: "{stage-specific question?}"

# GOOD — stage-specific question present:
- name: discovery
  phase: breadth
  intent: "Do we understand the competitive landscape and technical constraints well enough to commit to $TOPIC?"
  skills: [scout:feasibility, scout:market]
  gate: ">=2 scout signals"
```

Both checks required. Rewrite any stage or gate failing either before Step 6.

---

### Step 6a — Traceability audit (C-11 — MANDATORY)

For every non-echo gate artifact, identify its producing skill in the same stage:

```
Stage: discovery (phase: breadth)
  "scout-feasibility artifact" → scout:feasibility  [OK]
  "scout-market artifact"      → scout:market        [OK]

Stage: validate (phase: depth)
  "review-design artifact"     → review:design       [OK]
  "prove-hypothesis artifact"  → prove:hypothesis    [OK]

Stage: design [PROBLEM]:
  "scout-feasibility artifact" → [NONE — FORWARD REFERENCE]
  FIX: Move scout:feasibility to a breadth-phase stage, OR rewrite gate.
```

Do not proceed until all artifacts trace.

### Step 6b — Echo stage

```yaml
- name: echo
  auto: true
```

No additional fields.

---

### Step 7 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth:    "{specific breadth question, ends with ?}"
  depth:      "{specific depth/validation question, ends with ?}"
  monitoring: "{specific post-ship learning question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    phase: breadth|depth|monitoring
    intent: "{specific investigative question, ends with ?}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  - name: echo
    auto: true
```

---

**Final validation checklist:**

**Essential tier:**
- [ ] **C-01** YAML valid — no unclosed brackets, bad indentation, or unquoted colons
- [ ] **C-02** Echo is last, `auto: true`, no `skills` or `gate` fields
- [ ] **C-03** Every skill maps to the 47-skill Signal catalog
- [ ] **C-04** Every non-echo stage has a non-trivial gate

**Recommended tier:**
- [ ] **C-05** Stages in namespace layer order (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier:**
- [ ] **C-08** Plan reflects strategic evidence arc (breadth → depth → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Check A enforced)
- [ ] **C-10** Every non-echo stage has strategic `name:` encoding purpose
- [ ] **C-11** All gate artifacts traceable to a skill in same stage (Step 6a enforced)
- [ ] **C-12** Every non-echo stage has `intent:` as stage-specific investigative question (Check A enforced)
- [ ] **C-13** C-09 (Check A) and C-11 (Step 6a) both have dedicated labeled enforcement blocks with format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ criteria
- [ ] **C-15** Every checklist item carries an explicit criterion ID
- [ ] **C-16** `evidence_arc:` block present in output YAML (Step 1 + Step 7)
- [ ] **C-17** All `intent:` and `evidence_arc:` values end with `?` — no declarative statements (Step 4 rule + example enforced)
- [ ] **C-18** Every non-echo stage carries `phase:` mapping to `evidence_arc:` key (Step 2 + Step 7 template enforced)
- [ ] **C-19** Check A enforces C-09 (gate-behavior ladder) + C-12 (question-framing ladder) in one block with examples for each

---

## V-05 — Combination: Terse Register + Traceability/Arc Cross-Enforcement

**Axes**: Phrasing register (V-03 terse rules + Check blocks) + new C-19 pairing: C-11
(gate-behavior ladder) + C-18 (arc-structure ladder) consolidated in one labeled block.

**Hypothesis**: C-11 (gate traceability) and C-18 (arc phase back-reference) are structurally
analogous verification operations — both require auditing each stage's internal consistency:
C-11 asks "does each gate artifact have a producing skill in this stage?", C-18 asks "does
each stage's phase field map back to the arc?". Combining them in one audit block (Check C)
is a natural pairing because the same per-stage inspection satisfies both. This tests whether
a terse register can consolidate a gate-ladder + arc-ladder pair in a single coherent audit
step, and whether that consolidation reads as designed rather than accidental.

**C-18**: Rule 5 requires `phase:` on every non-echo stage. Check C provides a dedicated audit
block with C-18 bad/good format example (stage missing `phase:` field).

**C-19**: Check C is a single labeled enforcement block covering C-11 (gate-behavior ladder:
gate artifact must trace to a producing skill in the same stage) + C-18 (arc-structure ladder:
stage `phase:` must map back to `evidence_arc:` key). Format examples for both in one block.

---

You are running `/program:plan` for Signal.

**Inputs**: Topic `$TOPIC` — Strategy `$STRATEGY`
**Output**: `simulations/program/plans/{topic}-program-{date}.md` — YAML staged plan. Plan only; not an executor.

---

**CATALOG** — 47 skills, 9 namespaces. Use only these names:

| Layer | Namespace | Skills |
|-------|-----------|--------|
| 1 | `/scout:` | `competitors`, `feasibility`, `naming`, `compliance`, `market`, `stakeholders`, `positioning`, `requirements` |
| 2 | `/draft:` | `spec`, `proposal`, `pitch` |
| 3 | `/review:` | `design`, `code`, `users`, `customers` |
| 3 | `/prove:` | `hypothesis`, `websearch`, `analysis`, `intelligence`, `prototype`, `synthesize`, `publish`, `interview` |
| 3 | `/flow:` | `lifecycle`, `conversation`, `trigger`, `dataflow`, `integration`, `throttle`, `resilience` |
| 3 | `/trace:` | `request`, `state`, `contract`, `component`, `deployment`, `migration`, `permissions` |
| 4 | `/listen:` | `feedback`, `support`, `adoption` |
| 5 | `/topic:` | `new`, `plan`, `report`, `story`, `status`, `echo` |

Layer order is mandatory: scout before draft before review/prove/flow/trace before listen before topic.

---

**RULES:**

1. **Skill validity**: Every name in `skills:` must appear in CATALOG. No invented names.
2. **Stage count**: 3–6 non-echo stages. No single-skill stages. No mega-stage.
3. **Stage names**: Strategic labels only.
   - PASS: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`
   - FAIL: `scout_skills`, `stage_1`, `layer_3`
4. **Arc field required**: Output YAML must include `evidence_arc:` with keys `breadth`, `depth`,
   `monitoring`. Each value ends with `?`.
5. **Phase field required**: Every non-echo stage must declare `phase: breadth|depth|monitoring`.
   The value must match a key in `evidence_arc:`. Every arc phase must have at least one stage.
6. **Intent mandate**: Every non-echo stage must have `intent:` as an interrogative question ending with `?`.
   - PASS: `intent: "Is the market real and can we technically deliver?"`
   - FAIL — STATEMENT, NOT A QUESTION: `intent: "Understand the market and confirm feasibility."`
7. **Gate artifacts**: Every non-echo gate names specific artifact types. FAIL: `"PM approves"` / `"done"` / `""`.
8. **Gate quantification — MANDATORY**: Every non-echo gate contains `>=N`.
   - PASS: `gate: ">=2 scout signals (feasibility + requirements), 0 P1 blockers"`
   - FAIL: `gate: "scout-feasibility artifact present"` (threshold missing)
9. **Traceability**: Every gate artifact is producible by a skill in the same stage.
10. **Echo**: Final stage is always `- name: echo` with `auto: true`. No `skills`. No `gate`. No other fields.
11. **Layer order**: Stages observe namespace layer ordering within and across all stages.

---

**PRE-WRITE CHECKS — complete all before assembling YAML:**

**Check A — Arc field + Interrogative questions (C-16 + C-17):**

First, write the `evidence_arc:` block:

```
evidence_arc:
  breadth:    "{question for $TOPIC, ends with ?}"
  depth:      "{question for $TOPIC, ends with ?}"
  monitoring: "{question for $TOPIC, ends with ?}"
```

Then, for each non-echo stage, verify `intent:` is an interrogative question ending with `?`:

```
discovery: "Do we understand market, feasibility, and requirements well enough to commit?" [QUESTION — OK]
validate:  "Understand the design and prove the hypothesis."  [STATEMENT, NOT A QUESTION — REWRITE]
monitor:   "Are adoption signals tracking to prediction?"     [QUESTION — OK]
```

**Check B — Gate quantification (C-09):**

```
">=3 scout signals present"             [QUANTIFIED — OK]
"scout-feasibility artifact present"    [MISSING >=N — REWRITE: ">=1 scout-feasibility artifact present"]
```

**Check C — Gate traceability + Phase back-reference (C-11 + C-18):**

**Single enforcement block: gate-behavior ladder (C-11) + arc-structure ladder (C-18).**

For every non-echo stage, verify both: (a) each gate artifact maps to a producing skill in the
same stage, and (b) the stage's `phase:` field maps to a key in `evidence_arc:`.

```
Stage audit:

Stage: discovery
  phase: breadth         → maps to evidence_arc.breadth [C-18 OK]
  "scout-feasibility"    → scout:feasibility in skills  [C-11 OK]
  "scout-requirements"   → scout:requirements in skills [C-11 OK]

Stage: validate
  phase: depth           → maps to evidence_arc.depth   [C-18 OK]
  "review-design"        → review:design in skills      [C-11 OK]

Stage: design [TWO PROBLEMS]:
  phase: MISSING         → [NO PHASE FIELD — C-18 VIOLATION]
                           FIX: add phase: depth
  "scout-feasibility"    → [NO SCOUT SKILL IN THIS STAGE — C-11 FORWARD REFERENCE]
                           FIX: move skill or rewrite gate
```

**C-11 failure pattern** (gate artifact not producible in this stage):

```yaml
# BAD — forward reference (C-11 violation):
- name: validate
  phase: depth
  skills: [review:design, prove:hypothesis]
  gate: ">=1 scout-feasibility artifact"   # no scout skill in this stage!

# GOOD — gate artifact traceable to same-stage skill:
- name: validate
  phase: depth
  skills: [review:design, prove:hypothesis]
  gate: ">=1 review-design artifact AND >=1 prove-hypothesis artifact"
```

**C-18 failure pattern** (phase field absent or unmapped):

```yaml
# BAD — phase field absent (C-18 violation):
- name: monitor
  intent: "Are adoption signals healthy post-ship?"
  skills: [listen:feedback, listen:adoption]
  gate: ">=2 listen signals"
  # MISSING: phase: monitoring

# GOOD — phase declared, maps to evidence_arc.monitoring:
- name: monitor
  phase: monitoring
  intent: "Are adoption signals healthy post-ship?"
  skills: [listen:feedback, listen:adoption]
  gate: ">=2 listen signals"
```

Both checks in Check C required. A stage failing either must be corrected before final YAML.

---

**OUTPUT FORMAT:**

```yaml
topic: {topic}
strategy: {one-line summary}
evidence_arc:
  breadth:    "{question, ends with ?}"
  depth:      "{question, ends with ?}"
  monitoring: "{question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    phase: breadth|depth|monitoring
    intent: "{stage-specific interrogative question, ends with ?}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signals/artifacts} AND {condition}"

  - name: echo
    auto: true
```

---

**VALIDATION CHECKLIST:**

Essential tier:
- [ ] **C-01**: YAML valid — no unclosed brackets, bad indentation, or unquoted colons
- [ ] **C-02**: Echo is last, `auto: true`, no `skills` or `gate`
- [ ] **C-03**: All skills from CATALOG
- [ ] **C-04**: All non-echo stages have non-trivial gates

Recommended tier:
- [ ] **C-05**: Stages in namespace layer order
- [ ] **C-06**: Each stage has 2+ skills in a coherent grouping
- [ ] **C-07**: At least half of non-echo gates name specific artifact types

Aspirational tier:
- [ ] **C-08**: Evidence arc present — breadth → depth → monitoring
- [ ] **C-09**: Every non-echo gate has `>=N` threshold (Check B enforced)
- [ ] **C-10**: Every non-echo stage has strategic `name:` encoding purpose
- [ ] **C-11**: Every gate artifact traces to a skill in same stage (Check C enforced)
- [ ] **C-12**: Every non-echo stage has `intent:` as stage-specific interrogative question (Check A + Rule 6)
- [ ] **C-13**: C-09 (Check B) and C-11 (Check C) both have dedicated labeled enforcement blocks with examples
- [ ] **C-14**: This checklist spans Essential, Recommended, Aspirational tiers with 4+ criteria
- [ ] **C-15**: Every checklist item above carries an explicit criterion ID
- [ ] **C-16**: `evidence_arc:` block in output YAML (Rule 4 + Check A + OUTPUT FORMAT enforced)
- [ ] **C-17**: All `intent:` and `evidence_arc:` values are interrogative questions ending with `?` (Check A + Rule 6 enforced)
- [ ] **C-18**: Every non-echo stage carries `phase:` mapping to `evidence_arc:` key (Rule 5 + Check C enforced)
- [ ] **C-19**: Check C enforces C-11 (gate-behavior ladder) + C-18 (arc-structure ladder) in one block with examples for each

---

## R5 Predicted Scores (v5 rubric)

| Variant | C-18 mechanism | C-19 pair | Predicted C-18 | Predicted C-19 | Predicted v5 Score |
|---------|---------------|-----------|----------------|----------------|-------------------|
| V-01 — Phase-Declaration-First | Step 2 phase declaration + Check A bad/good | C-18 + C-17 (arc + question) | P | P | 150 / 150 |
| V-02 — Bidirectional Compliance Table | Step 4 phase req + Step 6 table bad/good | C-18 + C-09 (arc + gate) | P | P | 150 / 150 |
| V-03 — Terse + C-18 Extension | Rule 5 phase req + Check D bad/good | C-16 + C-17 (arc + question, retained from R4) | P | P | 150 / 150 |
| V-04 — Phase-First + Gate/Question | Step 2 phase declaration + Step 7 template | C-09 + C-12 (gate + question, new pairing) | P | P | 150 / 150 |
| V-05 — Terse + Traceability/Arc | Rule 5 phase req + Check C bad/good | C-11 + C-18 (gate + arc, new pairing) | P | P | 150 / 150 |

**C-19 pairing inventory across R4 + R5:**
- R4 V-03: C-16 + C-17 (arc + question)
- R5 V-01: C-18 + C-17 (arc + question — uses C-18 instead of C-16)
- R5 V-02: C-18 + C-09 (arc + gate)
- R5 V-03: C-16 + C-17 (arc + question — retained from R4)
- R5 V-04: C-09 + C-12 (gate + question — first use of gate+question pair)
- R5 V-05: C-11 + C-18 (gate + arc — first use of C-11+arc pair)

All six distinct cross-ladder configurations now have at least one golden representative.
