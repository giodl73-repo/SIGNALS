# program-plan — R3 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. All five variations target 125/125 under the v3 rubric.

**R3 diagnostic from v3 scoring of R2 variants:**
- V-01 R2 (122.5): C-13 **partial** (2.5 pts) — Step 5 isolated C-09 with before/after, but C-11
  was only a checklist item, not a dedicated enforcement step. Two separate dedicated steps =
  C-13 full pass (5 pts); one dedicated + one checklist item = C-13 partial (2.5 pts).
- V-04 R2 (117.5): C-11 **fails** (0 pts) — no explicit traceability audit step allows forward
  references under novel topics. C-14 **partial** (2.5 pts) — checklist covered only 3 criteria.

**Path to 125/125** — every R3 variant must include all four mechanisms:
1. Dedicated C-09 enforcement step with `>=N` before/after example
2. Dedicated C-11 traceability audit step with table format + FORWARD REFERENCE flag procedure
3. Per-stage investigative question mandate with before/after (C-12)
4. Cross-tier validation checklist: 4+ criteria, explicit tier labels spanning essential + recommended + aspirational (C-14)

**R3 variation axes (single-axis V-01 through V-03, combinations V-04/V-05):**
- V-01: Lifecycle emphasis — investigative question as a dedicated pre-stage step before skill selection
- V-02: Output format — tier-labeled validation checklist with criterion IDs
- V-03: Phrasing register — terse imperative, all constraints as numbered rules
- V-04: V-01 R3 + V-02 R3 (pre-stage questions + tier-labeled checklist)
- V-05: V-04 R3 + inertia framing (anti-pattern section + all mechanisms)

---

## V-01 — Pre-Stage Question Step (Lifecycle Emphasis)

**Axis**: Lifecycle emphasis — the investigative question for each phase is written as a dedicated
pre-stage step before any skill is selected. Questions become `intent:` values.

**Hypothesis**: R2 V-01 passed C-12 via the three-horizon framing in Step 2 ("mandatory before
building / mid-build / after shipping"), but those questions are arc-level, not stage-level. Under
topics with 4+ stages, the three horizons may not map cleanly to stage boundaries, and a model may
assign the same horizon question to multiple stages without differentiation. R3 V-01 forces the model
to write a *specific* question for each stage before selecting skills — analogous to how Step 5 forces
gate quantification before writing YAML. The pre-stage question step also ensures question specificity:
each question must be answerable by the skills in that stage (not by the program as a whole).

**New vs R2 V-01**:
- Step 2b (new): Per-stage investigative question enumeration with before/after example (C-12 isolation)
- Step 6 (new): Dedicated traceability audit step alongside the existing C-09 step (closes C-13 partial)
- Validation checklist expanded to 9 items across all three tiers with tier labels (C-14 full pass)

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every stage carries an explicit investigative question. Every gate is quantified and artifact-grounded.
The program is a plan, not an executor — gates describe conditions to verify, not runtime automations.

---

### Step 1 — Load the skill catalog

The Signal plugin has 47 skills across 9 namespaces. Use only skills from this catalog.
Invented or misspelled skill names invalidate the plan.

**Namespace layers (dependency order)**:

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

### Step 2 — Map strategy to the evidence arc

Read `$STRATEGY`. Identify which namespace layers are relevant for this topic.

The evidence arc answers three horizon questions:
- **Before building**: Which questions must be answered before any team commits to build?
  (scout + draft namespaces)
- **During building**: Which questions validate the design and behavior once committed?
  (review + prove + flow + trace namespaces)
- **After shipping**: Which questions determine whether shipping worked?
  (listen + topic namespaces)

Not every program needs all namespace layers. Select the minimum sufficient set.

**Step 2b — Write the investigative question for each planned stage (MANDATORY):**

Before selecting any skills, enumerate each stage you plan and write its specific investigative question.

```
# GOOD — stage-specific investigative questions (each answerable by that stage's skills):
discovery:  "Do we understand the competitive landscape, feasibility, and core
             requirements well enough to commit to building this?"
de-risk:    "Does the proposed design hold up under expert review, and can the
             primary hypotheses be validated empirically before full build?"
simulate:   "Do the key user flows, data paths, and edge cases behave correctly
             under realistic conditions?"
monitor:    "What are users experiencing post-ship, and are adoption signals
             tracking to prediction?"

# BAD — horizon-only questions (not stage-specific, apply to whole program):
discovery:  "What do we need to know before building?"
de-risk:    "Is the design good?"
```

Each question must be answerable by the skills you will assign to that stage.
These questions become the `intent:` field values in the final YAML.

---

### Step 3 — Group skills into stages

Group skills into 3–6 stages (not counting echo). Rules:

1. Each stage contains 2+ skills — no single-skill stages.
2. No single mega-stage — skills must be distributed across meaningful phases.
3. `name:` encodes strategic purpose: use `discovery`, `de-risk`, `design`, `validate`,
   `simulate`, `synthesize`, `monitor` — not `scout_stage`, `stage_1`, `layer_3`.
4. `intent:` carries the stage-specific investigative question from Step 2b — verbatim.
5. Layer order: scout before draft before review/prove/flow/trace before listen before topic.

---

### Step 4 — Write gate conditions

Write one gate per non-echo stage. Each gate must:
- Name specific artifact types or signal counts (not abstract prose: "PM approves", "done").
- Reference only artifacts producible by skills **in the same stage** (no forward references).

---

### Step 5 — Apply the quantified gate mandate

**THIS STEP IS MANDATORY. Every non-echo gate must contain a `>=N` numeric threshold.**

```
# Before (prose-only — FAILS C-09):
gate: "scout-feasibility artifact present and scout-requirements artifact present"

# After (quantified — PASSES C-09):
gate: ">=2 scout signals present (feasibility + requirements), 0 P1 blockers flagged"
```

Rewrite any gate that lacks `>=N` before proceeding.

Threshold patterns:
- `>=1 {artifact-type} artifact present`
- `>=N {namespace} signals gathered`
- `>=N findings with P1 severity resolved`
- Combined: `>=2 scout artifacts AND draft-spec written`

A plan with even one unquantified non-echo gate fails the quantified gate criterion.

---

### Step 6 — Apply the traceability audit

**THIS STEP IS MANDATORY before writing the final YAML.**

For every non-echo gate that names an artifact, pair it with the skill in the same stage
that produces it. If no skill in the same stage produces the artifact, it is a forward
reference — fix it before proceeding.

```
Traceability audit:

Stage: discovery
  gate artifact: "scout-feasibility artifact"  -> produced by: scout:feasibility  [OK]
  gate artifact: "scout-requirements artifact" -> produced by: scout:requirements [OK]

Stage: de-risk
  gate artifact: "review-design artifact"      -> produced by: review:design      [OK]
  gate artifact: "prove-synthesize artifact"   -> produced by: prove:synthesize   [OK]

Stage: simulate
  gate artifact: "flow-lifecycle artifact"     -> produced by: flow:lifecycle     [OK]
```

If any gate artifact has no matching skill in the same stage:

```
Stage: design
  gate artifact: "scout-feasibility artifact"  -> produced by: [NONE — FORWARD REFERENCE]
  ACTION: Move scout:feasibility to an earlier stage, OR rewrite the gate to reference
          an artifact producible by a skill in this stage.
```

Do not proceed to Step 7 until every gate artifact traces to a skill in the same stage.

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
stages:
  - name: {strategic-phase-name}
    intent: "{the specific investigative question this phase answers — from Step 2b}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

**Validation checklist — complete all three tiers before writing:**

Essential tier:
- [ ] YAML is valid — no unclosed brackets, bad indentation, or unquoted colons in values
- [ ] Echo stage is the last entry, has `auto: true`, has no `skills` or `gate` fields
- [ ] All skill names are from the 47-skill Signal catalog
- [ ] All non-echo stages have a non-trivial gate

Recommended tier:
- [ ] Stages ordered by namespace layer dependency (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] Each stage groups 2+ related skills — no single-skill stages, no all-in-one mega-stage

Aspirational tier:
- [ ] Every non-echo gate contains a `>=N` numeric threshold (Step 5 enforced)
- [ ] Every non-echo stage has an `intent:` field phrased as a stage-specific investigative question (Step 2b enforced)
- [ ] Every gate artifact traces to a skill in the same stage — traceability audit complete (Step 6 enforced)

---

## V-02 — Tier-Labeled Validation Checklist (Output Format)

**Axis**: Output format — the final validation checklist is organized into three explicitly labeled
tiers (Essential / Recommended / Aspirational) with criterion IDs, making cross-tier coverage
structurally enforced rather than incidental.

**Hypothesis**: R2 V-04 got C-14 partial (2.5 pts) because its checklist had 3 criteria (C-02,
C-05, C-09). The issue was not the content of each checklist item but that the checklist had no
structure forcing cross-tier representation. A tier-labeled checklist makes it architecturally
impossible to produce a single-tier checklist — the tier headers are visible constraints on the
checker, not just on the output. R3 V-02 keeps R2 V-04's `intent:` field mechanism for C-10 and
adds: (a) explicit traceability audit for C-11/C-13, (b) per-stage question framing for C-12,
(c) tier-labeled checklist with criterion IDs for C-14.

**New vs R2 V-04 (base)**:
- Step 2b (new): Per-stage investigative question mandate (C-12)
- Step 5b (new): Dedicated traceability audit alongside existing C-09 step (C-13 full pass)
- Validation checklist reorganized with explicit tier labels and criterion IDs (C-14 full pass)

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every stage declares its strategic intent as an investigative question. Every gate is quantified
and traceable to skills in the same stage. The program is a plan, not an executor.

---

### Step 1 — Load the skill catalog

The Signal plugin has 47 skills across 9 namespaces. Use only skills from this catalog.

**Namespace layers (dependency order)**:

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

### Step 2 — Map strategy to evidence layers

Read `$STRATEGY`. For each namespace layer you plan to use, identify the strategic question
it will answer. The arc reads:
- "Do we know enough to build this?" → scout + draft
- "Is what we're building right?" → review + prove + flow + trace
- "Did shipping work?" → listen + topic

**Step 2b — Write the investigative question per stage (MANDATORY):**
Before grouping skills, enumerate each planned stage and write its specific question.

```
# GOOD — stage-specific (answerable by that stage's skills):
discovery:  "Is the market real, is this technically feasible, and do we have stakeholder alignment?"
validate:   "Does the design meet expert review standards and can the core hypothesis be proved?"

# BAD — not stage-specific (applies to all stages equally):
discovery:  "Are we ready?"
validate:   "Is it good enough?"
```

---

### Step 3 — Group skills into stages with intent declarations

Group into 3–6 stages. For each stage:

**a) Name the stage** with a strategic label:
- Good: `discovery`, `de-risk`, `design`, `validate`, `simulate`, `synthesize`, `monitor`
- Bad: `scout_skills`, `stage_1`, `namespace_layer_3`

**b) Declare intent — MANDATORY:**
Every non-echo stage must carry an `intent:` field. It must be:
- The stage-specific investigative question from Step 2b (ends with "?")
- NOT a skill-list description: `"Runs scout:feasibility and scout:market"`
- NOT a stage name restatement: `"Discovery phase"`

```yaml
# Good:
intent: "Is the market real and can we technically deliver within the identified constraints?"

# Bad:
intent: "Runs scout:feasibility, scout:market, scout:requirements"
intent: "Discovery"
```

**c) Select skills** from the layer-appropriate namespace. 2+ per stage. Enforce layer order.

**d) Write the gate** with a `>=N` threshold — MANDATORY:

```
# Fails (no threshold):
gate: "scout-feasibility artifact present"

# Passes:
gate: ">=3 scout signals present (feasibility + market + requirements), 0 P1 blockers"
```

---

### Step 4 — Run pre-write enforcement checks

**Step 4a — Gate quantification (C-09 mandate):**

Every non-echo gate must contain `>=N`.

```
# FAILS C-09:
gate: "draft-spec written and review-design artifact present"

# PASSES C-09:
gate: ">=1 draft-spec artifact written AND >=1 review-design artifact present, 0 open P1 items"
```

Rewrite any gate missing `>=N` before proceeding.

**Step 4b — Traceability audit (C-11 mandate — MANDATORY before writing YAML):**

For every artifact named in a non-echo gate, identify the skill in the same stage that produces it.

```
Traceability audit:

Stage: discovery
  "scout-feasibility artifact"  -> scout:feasibility  [OK]
  "scout-market artifact"       -> scout:market        [OK]

Stage: validate
  "review-design artifact"      -> review:design       [OK]
  "prove-synthesize artifact"   -> prove:synthesize    [OK]

Stage: monitor
  "listen-feedback artifact"    -> listen:feedback     [OK]
```

Flag and fix any FORWARD REFERENCE before proceeding:

```
Stage: design
  "scout-feasibility artifact"  -> [NONE in this stage — FORWARD REFERENCE]
  FIX: move scout:feasibility to an earlier stage, or rewrite gate to reference
       an artifact producible by a skill already in this stage.
```

---

### Step 5 — Build the echo stage

```yaml
- name: echo
  auto: true
```

No additional fields.

---

### Step 6 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
stages:
  - name: {strategic-phase-name}
    intent: "{specific investigative question this phase answers}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

---

**Final validation checklist — every item must pass before writing.**

**Essential tier** (structure and correctness — all four must pass):
- [ ] **C-01** YAML valid — no unclosed brackets, bad indentation, or unquoted colons in values
- [ ] **C-02** Echo stage is the last entry, has `auto: true`, has no `skills` or `gate` fields
- [ ] **C-03** All skill names map to the 47-skill Signal catalog
- [ ] **C-04** Every non-echo stage has a non-trivial gate (not "done", "proceed", or a stage name echo)

**Recommended tier** (depth and ordering — all three should pass):
- [ ] **C-05** Stages ordered by namespace layer dependency (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier** (arc and enforcement — all should pass):
- [ ] **C-08** Plan reflects a strategic evidence arc (breadth → depth/validation → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` numeric threshold (Step 4a enforced)
- [ ] **C-10/C-12** Every non-echo stage has `intent:` phrased as a stage-specific investigative question (Step 2b enforced)
- [ ] **C-11** Traceability audit complete — every gate artifact maps to a producing skill in the same stage (Step 4b enforced)

---

## V-03 — Terse Imperative Register (Phrasing Register)

**Axis**: Phrasing register — all instructions are expressed as numbered imperatives and rule lists,
with no narrative prose. Same four mechanisms as V-04/V-05 R2 but written at maximum constraint
density.

**Hypothesis**: R2 variants used 600–800 words of narrative instruction per step. In a narrative
register, constraint-critical requirements can be buried in surrounding prose — a model skimming
the "Assemble" step may miss the gate quantification rule from an earlier step. In a terse
imperative register, every line is a constraint: there is no surrounding text to absorb attention.
The discriminating signal: V-03 outputs are structurally identical to V-01 R3 outputs (all four
mechanisms active) but produced from instructions half the length.

**New vs R2 V-05 (base)**:
- All narrative steps replaced with numbered rule lists
- Pre-write checks A (C-12), B (C-09), C (C-11) are labeled check blocks with inline before/after
- Validation checklist retains tier labels from V-02 R3

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

1. **Skill validity**: Every name in `skills:` must appear in CATALOG above. No invented names.
2. **Stage count**: 3–6 non-echo stages. No single-skill stages. No mega-stage.
3. **Stage names**: Strategic labels only.
   - PASS: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`
   - FAIL: `scout_skills`, `stage_1`, `layer_3`, `namespace_group`
4. **Intent mandate**: Every non-echo stage must have `intent:` phrased as a stage-specific question.
   - PASS: `intent: "Is the market real and can we technically deliver within constraints?"`
   - FAIL: `intent: "Runs scout skills"` / `intent: "Discovery"` / (field absent)
5. **Gate artifacts**: Every non-echo gate names specific artifact types from the same stage.
   - PASS: `gate: "scout-feasibility artifact present"`
   - FAIL: `gate: "PM approves"` / `gate: "done"` / `gate: ""`
6. **Gate quantification — MANDATORY**: Every non-echo gate contains `>=N`.
   - PASS: `gate: ">=2 scout signals (feasibility + requirements), 0 P1 blockers"`
   - FAIL: `gate: "scout-feasibility artifact present"` (threshold missing)
7. **Traceability**: Every gate artifact is producible by a skill in the same stage.
8. **Echo**: Final stage is always `- name: echo` with `auto: true`. No `skills`. No `gate`. No other fields.
9. **Layer order**: Stages observe namespace layer ordering within and across all stages.

---

**PRE-WRITE CHECKS — complete all three before assembling YAML:**

**Check A — Investigative questions (C-12):**
For each non-echo stage, verify `intent:` is a specific question answerable by that stage's skills:
```
discovery: "Do we understand market, feasibility, and requirements well enough to commit?" [SPECIFIC QUESTION — OK]
validate:  "Validate the design."     [NOT A QUESTION — REWRITE AS: "Does the design...?"]
monitor:   "Are we ready?"            [NOT STAGE-SPECIFIC — REWRITE: "What do post-ship users report...?"]
```

**Check B — Gate quantification (C-09):**
For each non-echo gate, verify `>=N` is present:
```
">=3 scout signals present"             [QUANTIFIED — OK]
"scout-feasibility artifact present"    [MISSING >=N — ADD: ">=1 scout-feasibility artifact present"]
```

**Check C — Gate traceability (C-11):**
For each gate artifact, map to its producing skill in the same stage:
```
Stage: discovery
  "scout-feasibility artifact" -> scout:feasibility  [OK]
  "scout-market artifact"      -> scout:market        [OK]
Stage: validate
  "review-design artifact"     -> review:design       [OK]

Stage: design [PROBLEM EXAMPLE]
  "scout-feasibility artifact" -> [NO SCOUT SKILL IN THIS STAGE — FORWARD REFERENCE]
  FIX: move skill or rewrite gate.
```

---

**OUTPUT FORMAT:**

```yaml
topic: {topic}
strategy: {one-line summary}
stages:
  - name: {strategic-phase-name}
    intent: "{stage-specific investigative question}"
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
- [ ] C-01: YAML valid
- [ ] C-02: Echo is last, `auto: true`, no `skills` or `gate`
- [ ] C-03: All skills from CATALOG
- [ ] C-04: All non-echo stages have non-trivial gates

Recommended tier:
- [ ] C-05: Stages in namespace layer order
- [ ] C-06: Each stage has 2+ skills in a coherent grouping

Aspirational tier:
- [ ] C-09: Every non-echo gate has `>=N` threshold (Check B)
- [ ] C-12: Every non-echo stage has `intent:` as a stage-specific investigative question (Check A)
- [ ] C-11: Every gate artifact traces to a skill in the same stage (Check C)

---

## V-04 — Pre-Stage Questions + Tier-Labeled Checklist (V-01 R3 + V-02 R3)

**Axis**: Combination — the dedicated pre-stage question writing step from V-01 R3 and the
tier-labeled criterion-ID checklist from V-02 R3, layered on the R2 V-05 arc assertion base.

**Hypothesis**: V-01 R3 isolates C-12 enforcement (questions before skills). V-02 R3 isolates
C-14 enforcement (tier-labeled checklist). Neither single axis alone fully addresses all four
gaps — V-01 has the stronger C-12 mechanism (dedicated step) but V-02 has the stronger C-14
mechanism (explicit tier structure). Combined, they close both gaps simultaneously while
preserving the arc assertion (C-08), quantified gate mandate (C-09), and traceability audit
(C-11) from R2 V-05. Projected score: 125/125.

**New vs R2 V-05 (base)**:
- Step 3 (new): Dedicated pre-stage investigative question step with before/after (V-01 R3 mechanism)
- Step 6: Traceability audit retains R2 V-05 structure but adds FORWARD REFERENCE flag procedure
- Final checklist: tier-labeled with criterion IDs (V-02 R3 mechanism)

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every stage asks an explicit investigative question. Every gate is quantified and traceable.
The program is a plan, not an executor.

---

### Step 1 — Load the skill catalog

The Signal plugin has 47 skills across 9 namespaces. Use only skills from this catalog.

**Namespace layers (dependency order)**:

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

### Step 2 — Assert the evidence arc

Before drafting stages, write the program's evidence arc. The arc covers three phases:

1. **BREADTH** — What must be known before committing to build? (scout + draft)
2. **DEPTH** — What must be validated and simulated after committing? (review + prove + flow + trace)
3. **MONITORING** — What must be learned after shipping? (listen + topic)

```
Evidence arc for {topic}:
- BREADTH:     Is the market real? Is the architecture feasible? Do stakeholders align?
- DEPTH:       Does the design hold under expert review? Can core hypotheses be proved?
               Do the key flows and traces behave correctly?
- MONITORING:  What do early users report? Where does support friction appear?
               What does the full signal picture say?
```

Every stage maps to exactly one arc phase. Stages that don't fit indicate a planning error.

---

### Step 3 — Write investigative questions per stage (MANDATORY)

**Before selecting any skills, enumerate each planned stage and its specific investigative question.**

The question must be:
- Answerable by the skills in that stage (not by the whole program)
- Specific to that stage (not a generic horizon question)
- Phrased as a question (ends with "?")

```
# GOOD — stage-specific investigative questions:
- discovery:  "Do we understand the competitive landscape, technical feasibility, and core
               requirements well enough to commit to building this feature?"
- de-risk:    "Does the proposed design satisfy expert review, and can the primary value
               hypothesis be empirically validated before full build begins?"
- simulate:   "Do the primary user flows, data paths, and failure modes behave correctly
               under realistic conditions?"
- monitor:    "What are users experiencing post-ship, and are adoption signals tracking
               to prediction?"

# BAD — horizon-only (not stage-specific):
- discovery:  "What do we need to know before building?"
- de-risk:    "Is the design good?"
- simulate:   "Does it work?"
- monitor:    "Are we learning?"
```

These questions become the `intent:` field values in the YAML.

---

### Step 4 — Group skills into stages

Group into 3–6 stages aligned to arc phases. For each stage:

1. `intent:` = the investigative question from Step 3 (verbatim).
2. `name:` = strategic label: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`.
   Not: `scout_stage`, `stage_1`, `namespace_layer_3`.
3. Skills = 2+ from the arc-phase-appropriate namespace layer.
4. Enforce layer order within and across all stages.

---

### Step 5 — Write gate conditions

Write one gate per non-echo stage naming specific artifact types.
Gates must reference only artifacts producible by skills **in the same stage**.

---

### Step 6 — Apply enforcement checks

**Step 6a — Gate quantification mandate (C-09 — MANDATORY):**

Every non-echo gate must contain `>=N`.

```
# FAILS C-09 (no threshold):
gate: "scout-feasibility artifact present"

# PASSES C-09:
gate: ">=2 scout signals present (feasibility + requirements), 0 P1 blockers flagged"
```

Threshold patterns: `>=N {namespace} signals present`, `>=N artifacts written with 0 P1 open questions`,
`>=N findings addressed`. Rewrite any gate missing `>=N` before proceeding.

**Step 6b — Traceability audit (C-11 mandate — MANDATORY before writing YAML):**

For every non-echo gate artifact, identify the producing skill in the same stage.

```
Traceability audit:

Stage: discovery
  gate artifact: "scout-feasibility artifact"  -> produced by: scout:feasibility  [OK]
  gate artifact: "scout-market artifact"        -> produced by: scout:market        [OK]

Stage: de-risk
  gate artifact: "review-design artifact"       -> produced by: review:design      [OK]
  gate artifact: "prove-synthesize artifact"    -> produced by: prove:synthesize   [OK]

Stage: monitor
  gate artifact: "listen-adoption artifact"     -> produced by: listen:adoption    [OK]
```

If any gate artifact has no matching skill in the same stage:

```
Stage: design
  gate artifact: "scout-feasibility artifact"  -> produced by: [NONE — FORWARD REFERENCE]
  ACTION: Move scout:feasibility to an earlier stage, OR rewrite the gate to reference
          an artifact producible by a skill already in this stage.
```

Do not proceed to Step 7 until every gate artifact traces to a skill in the same stage.

---

### Step 7 — Build the echo stage

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
  breadth: "{question}"
  depth: "{question}"
  monitoring: "{question}"
stages:
  - name: {strategic-phase-name}
    intent: "{specific investigative question this phase answers}"
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

**Essential tier** (all four must pass — YAML is invalid if any fail):
- [ ] **C-01** YAML valid — no unclosed brackets, bad indentation, or unquoted colons in values
- [ ] **C-02** Echo stage is last, has `auto: true`, has no `skills` or `gate` fields
- [ ] **C-03** Every skill name maps to the 47-skill Signal catalog
- [ ] **C-04** Every non-echo stage has a non-trivial gate condition

**Recommended tier** (all three should pass):
- [ ] **C-05** Stages ordered by namespace layer dependency (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier** (all should pass — enforced by Steps 2, 3, 6a, 6b above):
- [ ] **C-08** Plan reflects a strategic evidence arc matching the `evidence_arc:` block
- [ ] **C-09** Every non-echo gate contains `>=N` numeric threshold (Step 6a)
- [ ] **C-10/C-12** Every non-echo stage has `intent:` as a specific investigative question, not a skill description or name echo (Step 3)
- [ ] **C-11** Traceability audit complete — every gate artifact maps to a producing skill in the same stage, no FORWARD REFERENCEs (Step 6b)

---

## V-05 — Inertia Framing + Full Synthesis (Inertia Framing Axis)

**Axis**: Inertia framing — opens with a concrete anti-pattern section showing what a bad program
plan looks like before instructing the model to produce a good one. All mechanisms from V-04 R3
are preserved.

**Hypothesis**: V-01 through V-04 focus on the positive-case constraints: what a plan *must* have.
The inertia framing adds the negative case: what a plan that wasn't written with Signal looks like.
Teams shipping without a program plan produce: mixed-layer stage groupings, abstract prose gates
("PM approves"), no arc, and echo stages with gates. Showing the model this anti-pattern before
writing makes the failure modes salient and reduces the chance of "PM approves"-style gates or
echo-with-gate errors even in novel topics. Secondary benefit: the anti-pattern explicitly violates
C-02 (echo with gate), C-04 (abstract gates), C-05 (mixed layers), and C-09 (no thresholds) —
priming C-02 compliance even though R2 V-01 already passes C-02 robustly.

**New vs V-04 R3 (base)**:
- Anti-pattern section before Step 1 with annotated bad YAML showing 6 failure modes
- `evidence_arc:` block retained from R2 V-05
- All V-04 R3 mechanisms: pre-stage question step, arc assertion, traceability audit, C-09 mandate, tier-labeled checklist

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
The plan reflects a deliberate evidence arc. Every stage asks an explicit investigative question.
Every gate is quantified and traceable. The program is a plan, not an executor.

---

### What a bad program plan looks like

Recognize these failure modes before writing — do not produce any of them:

```yaml
# FAILURE PATTERN — every line below violates at least one criterion:
stages:
  - name: stage_1                          # FAIL: namespace-cluster label, not strategic
    skills:
      - scout:feasibility
      - review:design                      # FAIL: mixed layers (Layer 1 + Layer 3 together)
      - listen:feedback                    # FAIL: mixed layers (Layer 4 in a Layer 1 stage)
    gate: "team approves"                  # FAIL: abstract prose, no artifact, no >=N threshold
                                           # intent: field absent — FAIL: no investigative question

  - name: stage_2
    skills:
      - draft:spec                         # FAIL: single-skill stage
    gate: "spec looks good"                # FAIL: no artifact type, no >=N

  - name: echo
    auto: true
    gate: "done"                           # FAIL: echo stage cannot have a gate field
```

What is missing: evidence arc, per-stage investigative questions, `>=N` gate thresholds,
artifact-grounded gate conditions, layer ordering, and a correctly formed echo stage.

---

### Step 1 — Load the skill catalog

The Signal plugin has 47 skills across 9 namespaces. Use only skills from this catalog.

**Namespace layers (dependency order)**:

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

### Step 2 — Assert the evidence arc

Write the program's evidence arc before drafting any stage:

1. **BREADTH** — What must be known before committing to build? (scout + draft)
2. **DEPTH** — What must be validated after committing? (review + prove + flow + trace)
3. **MONITORING** — What must be learned after shipping? (listen + topic)

```
Evidence arc for {topic}:
- BREADTH:     {specific questions this topic needs to answer before committing}
- DEPTH:       {specific validation and simulation questions for this topic}
- MONITORING:  {specific post-ship learning questions for this topic}
```

Every stage maps to exactly one arc phase. Stages that don't fit indicate a planning error.

---

### Step 3 — Write investigative questions per stage (MANDATORY)

**Before selecting any skills, enumerate each planned stage and its specific question.**

```
# GOOD — each question is answerable by skills assigned to that stage:
discovery:  "Do we understand the competitive landscape, technical feasibility, and
             core requirements well enough to commit?"
de-risk:    "Does the proposed design satisfy expert review, and can the primary
             hypothesis be empirically validated before full build?"
monitor:    "What are post-ship users reporting, and are adoption signals tracking
             to prediction?"

# BAD — generic, not answerable by a specific stage's skills:
discovery:  "What do we need to know?"
de-risk:    "Is it good?"
```

These become the `intent:` field values.

---

### Step 4 — Group skills into stages

Group into 3–6 stages aligned to arc phases:
1. `intent:` = stage-specific investigative question from Step 3.
2. `name:` = `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`. Not `scout_skills`, `stage_1`.
3. 2+ skills per stage from the arc-phase-appropriate namespace layer.
4. Enforce layer order within and across stages.

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Gates name specific artifact types producible by skills in the same stage.
Reference the anti-pattern above: "team approves" and "looks good" are not gates.

---

### Step 6 — Apply enforcement checks

**Step 6a — Gate quantification (C-09 — MANDATORY for every non-echo gate):**

```
# FAILS (no threshold — see anti-pattern):
gate: "scout-feasibility artifact present"

# PASSES:
gate: ">=2 scout signals present (feasibility + requirements), 0 P1 blockers flagged"
```

Rewrite every gate missing `>=N` before proceeding.

**Step 6b — Traceability audit (C-11 — MANDATORY before writing YAML):**

Map every gate artifact to a producing skill in the same stage:

```
Traceability audit:

Stage: discovery
  "scout-feasibility artifact"  -> scout:feasibility  [OK]
  "scout-requirements artifact" -> scout:requirements [OK]

Stage: de-risk
  "review-design artifact"      -> review:design      [OK]
  "prove-synthesize artifact"   -> prove:synthesize   [OK]

Stage: monitor
  "listen-feedback artifact"    -> listen:feedback    [OK]
```

Fix any FORWARD REFERENCE before proceeding:

```
Stage: design
  "scout-feasibility artifact"  -> [NONE — FORWARD REFERENCE]
  FIX: move skill to earlier stage or rewrite gate.
```

---

### Step 7 — Build the echo stage

```yaml
- name: echo
  auto: true
```

No additional fields — contrast with the anti-pattern's invalid `gate: "done"`.

---

### Step 8 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth: "{question}"
  depth: "{question}"
  monitoring: "{question}"
stages:
  - name: {strategic-phase-name}
    intent: "{specific investigative question}"
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
- [ ] **C-01** YAML valid — no unclosed brackets, bad indentation, or unquoted colons
- [ ] **C-02** Echo stage is last, `auto: true`, no `skills` or `gate` fields (contrast anti-pattern)
- [ ] **C-03** All skill names from the 47-skill Signal catalog
- [ ] **C-04** Every non-echo stage has a non-trivial gate

**Recommended tier** (all three should pass):
- [ ] **C-05** Stages ordered by namespace layer dependency — no mixed-layer stages (contrast anti-pattern)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages
- [ ] **C-07** At least half of non-echo gates name specific artifact types

**Aspirational tier** (all should pass — enforced by Steps 2, 3, 6a, 6b):
- [ ] **C-08** Plan reflects the asserted `evidence_arc:` (breadth → depth → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Step 6a enforced)
- [ ] **C-10/C-12** Every non-echo stage has `intent:` as a stage-specific investigative question (Step 3 enforced)
- [ ] **C-11** Traceability audit complete — zero FORWARD REFERENCEs (Step 6b enforced)

---

## Variation Summary

| Variant | Primary Axis | New vs R2 V-01 baseline | C-12 mechanism | C-13 mechanism | C-14 mechanism | Projected v3 |
|---------|-------------|------------------------|----------------|----------------|----------------|--------------|
| V-01 | Lifecycle emphasis | Pre-stage question step (2b) + C-11 audit (6) | Dedicated pre-stage step with before/after | C-09: Step 5 with `>=N` example; C-11: Step 6 with table+flag | 9 items, 3 tiers | 125/125 |
| V-02 | Output format | Pre-stage question mandate (2b) + audit (4b) + tier-labeled checklist | Step 2b mandate + `intent:` before/after | C-09: Step 4a; C-11: Step 4b with table+flag | Tier-labeled, criterion IDs, 11 items | 125/125 |
| V-03 | Phrasing register | Rules list + Check A/B/C blocks + tier checklist | Check A with before/after inline | Check B for C-09; Check C for C-11 with table+flag | 9 items, 3 tiers, terse labels | 125/125 |
| V-04 | V-01 R3 + V-02 R3 | Pre-stage questions (3) + arc (2) + audit (6a/6b) + tier checklist | Dedicated Step 3 with before/after | C-09: Step 6a; C-11: Step 6b with table+flag | Tier-labeled, criterion IDs, 11 items | 125/125 |
| V-05 | V-04 R3 + inertia framing | Anti-pattern section + all V-04 mechanisms | Dedicated Step 3 with before/after | C-09: Step 6a; C-11: Step 6b with table+flag | Tier-labeled, 11 items, anti-pattern anchors | 125/125 |

**Key discriminators for scoring:**
- V-01 PASS: pre-stage question step in output reasoning; C-11 audit table present; no arc assertion block
- V-02 PASS: tier-labeled checklist with C-0N labels; `intent:` fields before skills in each stage; no arc assertion block
- V-03 PASS: ultra-terse format — all rules numbered; Check A/B/C labeled blocks in output; no `evidence_arc:` YAML key
- V-04 PASS: both pre-stage question step AND tier-labeled checklist; `evidence_arc:` block in YAML
- V-05 PASS: failure-mode anti-pattern section referenced in checklist; `evidence_arc:` block; all other V-04 discriminators

**Why R3 closes the R2 gaps:**
- C-13 partial (V-01 R2): closed by adding dedicated C-11 audit step — now both C-09 and C-11 have
  dedicated enforcement steps with format examples. C-13 = full 5 pts across all R3 variants.
- C-14 partial (V-04 R2): closed by tier-labeled checklist with 9+ items spanning all three tiers.
  C-14 = full 5 pts in V-02/V-04/V-05; V-01/V-03 achieve it via 9-item 3-tier checklists.
- C-11 fail (V-04 R2): closed by mandatory traceability audit step in every R3 variant.
- C-12 mechanism strengthened: pre-stage question writing step forces stage-specific questions
  before skill selection, replacing reliance on horizon-level framing.
