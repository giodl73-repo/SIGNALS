# program-plan — R2 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. All five variations build on R1 V-03 Layer Walk ceiling (100/110 under v2 rubric).
New axes: Quantified Gate Mandate (V-01), Phase Intent Declaration (V-02), Gate Traceability Audit (V-03),
V-01+V-02 combined (V-04), V-01+V-02+V-03+Arc Assertion combined (V-05).

**R1 diagnostic**: C-09 (quantified gates) failed universally across all R1 variants. That is the primary
target for R2. C-10 (phase-label intent) and C-11 (gate-artifact traceability) are new in the v2 rubric —
V-03 retroactively scores PASS on both, but no R1 prompt explicitly required them. R2 variations make
each requirement explicit so models without R1 layer-walk intuition still pass.

---

## V-01 — Quantified Gate Mandate

**Axis**: Every non-echo gate must include a `>=N` numeric signal-count threshold. No gate passes
without a machine-checkable minimum.

**Hypothesis**: C-09 failed universally in R1 because no prompt told the model to quantify. Models
default to prose conditions ("PM approves", "design reviewed") unless explicitly required to produce
numeric thresholds. A direct mandate — stated as a constraint on gate syntax, not a suggestion —
should produce C-09 PASS in any output that clears the basics. The discriminating signal:
V-01 outputs will have `>=N` in every non-echo gate string; V-02/V-03 outputs will not.

**R2 new element vs R1 V-03 baseline**:
- Step 5b (new): Gate Quantification Mandate — explicit `>=N` syntax requirement per gate,
  with example showing how to translate prose condition into counted threshold.

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
The plan sequences Signal skills into ordered stages, each with a gate condition that must
be satisfied before advancing. The program is a plan, not an executor — gates describe
conditions to verify, not runtime checks to automate.

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

Dependency rule: Layer N skills must not appear in a stage before Layer N-1 artifacts exist.
Scout skills must precede draft skills; draft must precede review and prove; review/prove/flow/trace
must precede listen; listen must precede topic synthesis. The echo stage is always last.

---

### Step 2 — Map the topic to the strategy

Read `$STRATEGY`. Identify which namespaces are relevant for this topic. Not every program
uses all 47 skills. Select the minimal sufficient set that addresses the strategic questions.

Ask: which evidence is mandatory before any team would commit to building this feature?
That determines your early stages. Which evidence validates the decision mid-build?
That determines your middle stages. Which evidence tells you whether shipping worked?
That determines your late stages.

---

### Step 3 — Group skills into stages

Group skills into 3–6 stages (not counting echo). Rules:

1. No single-skill stages — each stage contains 2 or more skills.
2. No single mega-stage — do not collapse all skills into one stage.
3. Each stage is a coherent phase of work: skills within it address the same strategic question.
4. Stage names encode strategic purpose. Use names like "discovery", "de-risk", "design",
   "validate", "simulate", "synthesize", "monitor" — not "scout_skills" or "stage_1".
5. Layer order is enforced: scout-namespace skills precede draft-namespace skills, which
   precede review/prove/flow/trace, which precede listen, which precede topic.

---

### Step 4 — Write gate conditions

Write one gate per non-echo stage. Each gate states the condition that must be true before
the team advances to the next stage.

Gate quality rules:
- Gates must name specific artifact types or signal counts. Examples:
  - "scout-feasibility artifact present and scout-requirements artifact present"
  - "draft-spec written and at least one review-design artifact exists"
  - "3+ prove signals synthesized into prove-synthesize artifact"
- Gates must NOT be abstract prose: "PM approves", "team agrees", "looks good", "done".
- Gates must reference artifacts producible by skills in the same stage (no forward references).

---

### Step 5 — Apply the quantified gate mandate

**THIS STEP IS MANDATORY. Every gate must include a numeric threshold.**

For each non-echo gate you wrote in Step 4, verify or add a `>=N` threshold:

```
# Before (prose-only — FAILS C-09):
gate: "scout-feasibility artifact present and scout-requirements artifact present"

# After (quantified — PASSES C-09):
gate: ">=2 scout signals present (feasibility + requirements artifacts), 0 blockers flagged"
```

Rewrite any gate that lacks a `>=N` count before proceeding.

Minimum threshold patterns:
- `>=1 {artifact-type} artifact present`
- `>=N {namespace} signals gathered`
- `>=N findings with P1 severity addressed`
- Combine with AND for multi-condition gates: `>=2 scout signals AND draft-spec artifact written`

A plan with even one unquantified non-echo gate fails the quantified gate criterion.

---

### Step 6 — Build the echo stage

The final stage is always echo. It is auto-generated — no skills to run, no gate to pass.

```yaml
- name: echo
  auto: true
```

No additional fields. No skills array. No gate field.

---

### Step 7 — Assemble the program.yaml

Write the final YAML to `simulations/program/plans/{topic}-program-{date}.md`.

Required structure:
```yaml
topic: {topic}
strategy: {one-line strategy summary}
stages:
  - name: {strategic-phase-name}
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} present and {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

Validation checklist before writing:
- [ ] YAML is valid (no unclosed brackets, bad indentation, or unquoted colons in values)
- [ ] Echo stage is last, has `auto: true`, has no `skills` or `gate` fields
- [ ] All skill names are from the 47-skill Signal catalog
- [ ] All non-echo stages have a gate
- [ ] Every gate contains a `>=N` numeric threshold
- [ ] Gate artifacts are producible by skills in the same stage
- [ ] Stages are ordered by namespace layer (scout before draft before review/prove/flow/trace before listen before topic)

---

## V-02 — Phase Intent Declaration

**Axis**: Each non-echo stage must carry an explicit `intent` field stating the strategic question
the phase answers before listing skills.

**Hypothesis**: C-10 requires phase intent legibility. R1 V-03 passed C-10 by using named arc phases
(BREADTH, VALIDATION, SYNTHESIS) — but the names carried the weight. A prompt that requires an
explicit `intent` field makes the strategic purpose visible to a reader regardless of what the
stage is named. The `intent` field also forces the model to reason about *why* a phase exists
before enumerating its skills, which should improve stage coherence (C-06) and arc fidelity (C-08)
as side effects. Discriminating signal: V-02 outputs have `intent:` fields in every non-echo stage;
V-01/V-03 do not.

**R2 new element vs R1 V-03 baseline**:
- Step 3b (new): Intent Declaration — mandatory `intent` field per stage, framed as a strategic
  question the phase must answer.

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
The plan sequences Signal skills into ordered stages, each with an explicit intent declaration
and a gate condition. The program is a plan, not an executor.

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

Layer dependency rule: scout precedes draft; draft precedes review/prove/flow/trace; those precede listen; listen precedes topic. Echo is always last.

---

### Step 2 — Map the topic to the strategy

Read `$STRATEGY`. Identify the minimum sufficient set of skills that address the strategic questions.
For each namespace you plan to use, ask: "What question does running these skills answer?"
Write that question down — it becomes the `intent` for that stage.

The stage lifecycle reads as a sequence of questions:
- Scout: "Should we build this? Is it feasible? Who cares?"
- Draft: "What exactly are we building? Is the design coherent?"
- Review/Prove: "Is the design right? Can we validate our core bets?"
- Flow/Trace: "Does the process work? Does the system work?"
- Listen: "What will customers say? Who adopts? Where does it break down in the field?"
- Topic: "What do all the signals say together? Are we ready?"

Not every program needs all layers. Select layers relevant to the strategy.

---

### Step 3 — Group skills into stages and declare intent

Group skills into 3–6 stages (not counting echo). For each stage, before selecting skills,
write its intent as a strategic question.

**MANDATORY: Every non-echo stage must have an `intent` field.**

The `intent` field must:
- Be phrased as a question the team will answer by running the stage's skills.
- Express strategic purpose, not content description.
- NOT be a paraphrase of the stage name.
- NOT be a skill-cluster description ("runs the scout namespace skills").

```yaml
# Good intent (strategic question):
intent: "Is this technically feasible and does the market exist for it?"

# Bad intent (skill-cluster description — FAILS C-10):
intent: "Runs scout:feasibility and scout:market"

# Bad intent (stage name restatement — FAILS C-10):
intent: "Discovery phase"
```

After declaring intent, select skills from the appropriate namespace layer that will produce
evidence to answer the question.

Stage naming rules:
- Use strategic phase names: "discovery", "de-risk", "design", "validate", "simulate",
  "monitor", "synthesize".
- Do not use namespace-cluster labels: "scout_stage", "prove_skills", "layer_3".

---

### Step 4 — Write gate conditions

Write one gate per non-echo stage naming specific artifact types or signal counts. Examples:
- "scout-feasibility artifact present and scout-requirements artifact written"
- "draft-spec artifact written with no P1 open questions"
- "review-design artifact and prove-synthesize artifact present"

Gates must NOT be abstract prose ("PM approves", "done").
Gates must reference artifacts producible by skills in the same stage.

---

### Step 5 — Build the echo stage

The final stage is always echo. It is auto-generated — no skills, no gate.

```yaml
- name: echo
  auto: true
```

---

### Step 6 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
stages:
  - name: {strategic-phase-name}
    intent: "{strategic question this phase answers}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: "{artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

Validation checklist:
- [ ] YAML is valid
- [ ] Echo stage is last, `auto: true`, no `skills` or `gate`
- [ ] All skill names are from the 47-skill Signal catalog
- [ ] All non-echo stages have a non-trivial gate
- [ ] Every non-echo stage has an `intent` field phrased as a strategic question
- [ ] Intent fields express purpose, not content description
- [ ] Gate artifacts are producible by skills in the same stage
- [ ] Stages are ordered by namespace layer dependency

---

## V-03 — Gate Traceability Audit

**Axis**: After drafting gates, perform an explicit traceability audit — for each artifact
named in a gate, identify which skill in the same stage produces it. Flag and fix forward
references before writing the final YAML.

**Hypothesis**: C-11 requires that every gate artifact be producible by a skill in the same stage.
R1 V-03 retroactively passes C-11 (the layer walk naturally avoids forward references), but no
R1 prompt made this requirement explicit. Models under novel topics may construct stages where
a gate names an artifact from a later namespace (e.g., a gate in a draft stage referencing a
review artifact). The traceability audit step — explicitly pairing each gate artifact to a same-stage
skill — eliminates forward references before they reach the output. Discriminating signal:
V-03 outputs show a traceability table or inline annotation for each gate.

**R2 new element vs R1 V-03 baseline**:
- Step 5a (new): Traceability Audit — per-gate table mapping artifact name to producing skill
  in same stage; any unmapped artifact triggers stage redesign.

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every gate in the plan must reference only artifacts producible by skills in the same stage.
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

Layer dependency rule: scout precedes draft; draft precedes review/prove/flow/trace; those precede listen; listen precedes topic. Echo is always last.

---

### Step 2 — Map the topic to the strategy

Read `$STRATEGY`. Select the minimum sufficient set of skills for the topic. Group into
3–6 stages by namespace layer. Name stages with strategic phase labels, not namespace-cluster
labels. ("discovery" not "scout_stage"; "validate" not "review_skills".)

---

### Step 3 — Draft gates

For each non-echo stage, write a gate condition naming specific artifact types the team must
verify before advancing. Example formats:
- `"scout-feasibility artifact present and no P1 blockers"`
- `"draft-spec written and review-design artifact present"`
- `"prove-synthesize artifact with >=3 contributing signals"`

---

### Step 4 — Apply the traceability audit

**THIS STEP IS MANDATORY before writing the final YAML.**

For every non-echo gate that names an artifact, pair it with the skill in the same stage
that produces it. If no skill in the same stage produces the artifact, the gate is a forward
reference — fix it before proceeding.

Format the audit as a table (or inline note per stage):

```
Traceability audit:

Stage: discovery
  gate artifact: "scout-feasibility artifact"  -> produced by: scout:feasibility  [OK]
  gate artifact: "scout-requirements artifact" -> produced by: scout:requirements [OK]

Stage: de-risk
  gate artifact: "prove-synthesize artifact"   -> produced by: prove:synthesize   [OK]
  gate artifact: "review-design artifact"      -> produced by: review:design      [OK]

Stage: monitor
  gate artifact: "listen-feedback artifact"    -> produced by: listen:feedback    [OK]
```

If any gate artifact has no matching skill in the same stage:

```
Stage: design
  gate artifact: "scout-feasibility artifact"  -> produced by: [NONE in this stage — FORWARD REFERENCE]
  ACTION: Move scout:feasibility to an earlier stage, OR rewrite the gate to reference
          an artifact producible by a skill in this stage.
```

Do not proceed to Step 5 until every gate artifact traces to a skill in the same stage.

---

### Step 5 — Build the echo stage

```yaml
- name: echo
  auto: true
```

---

### Step 6 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
stages:
  - name: {strategic-phase-name}
    skills:
      - {namespace}:{skill}
    gate: "{artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

Validation checklist:
- [ ] YAML is valid
- [ ] Echo is last, `auto: true`, no `skills` or `gate`
- [ ] All skill names are from the 47-skill Signal catalog
- [ ] All non-echo stages have a non-trivial gate
- [ ] Traceability audit completed — every gate artifact maps to a skill in the same stage
- [ ] Stages are ordered by namespace layer dependency

---

## V-04 — Quantified Gates + Phase Intent (V-01 + V-02 Combined)

**Axis**: Both quantified gate mandate (C-09) and phase intent declaration (C-10) applied
simultaneously. Neither sacrificed for the other.

**Hypothesis**: V-01 cracks C-09 at the cost of no explicit intent framing. V-02 cracks C-10
but adds no numeric thresholds. R1 V-03 Layer Walk earned C-10 through strategic naming alone
(without explicit `intent` fields), then failed C-09. V-04 combines both — mandatory `>=N`
thresholds in every gate AND mandatory `intent` fields in every stage. If both mechanisms work
independently (V-01 PASS C-09, V-02 PASS C-10), V-04 should PASS both, achieving a projected
score of 110/110 assuming C-03, C-05, C-06, C-07, C-08, C-11 also pass. The critical risk:
the prompt becomes long enough that models start omitting fields — V-04 mitigates this with
an explicit validation checklist that lists `intent` and `>=N` as line items.

**R2 new elements vs R1 V-03 baseline**:
- Step 3b: Intent Declaration (from V-02)
- Step 5b: Gate Quantification Mandate (from V-01)
- Both appear in the validation checklist as pass/fail line items.

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every stage declares its strategic intent. Every gate contains a numeric threshold.
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

Layer dependency rule: scout precedes draft; draft precedes review/prove/flow/trace; those precede listen; listen precedes topic. Echo is always last.

---

### Step 2 — Map strategy to evidence layers

Read `$STRATEGY`. Identify the minimum sufficient set of Signal namespaces for this topic.
For each namespace you plan to use, write the strategic question it will answer.
These become the stage `intent` fields.

The evidence arc reads: "Do we know enough to build this?" (scout/draft) →
"Is what we're building right?" (review/prove/flow/trace) →
"Did shipping work?" (listen/topic).

---

### Step 3 — Group into stages with intent declarations

Group skills into 3–6 stages. For each stage:

**a) Name the stage** with a strategic phase label:
- Good: `discovery`, `de-risk`, `design`, `validate`, `simulate`, `synthesize`, `monitor`
- Bad: `scout_skills`, `stage_1`, `layer_3_namespace`

**b) Declare intent — MANDATORY:**
Every non-echo stage must carry an `intent` field. It must be:
- A strategic question: "Is the market real and is this feasible?"
- NOT a skill list: "Runs scout and draft skills"
- NOT a name echo: "Discovery stage"

```yaml
# Good:
intent: "Is the market real, is this technically feasible, and do stakeholders align?"

# Bad (skill description):
intent: "Runs scout:feasibility, scout:market, scout:stakeholders"

# Bad (name restatement):
intent: "Discovery"
```

**c) Select skills** from the layer-appropriate namespace. 2+ skills per stage.

---

### Step 4 — Write and quantify gates

Write one gate per non-echo stage. Gates must:
1. Name specific artifact types (not abstract prose)
2. Reference only artifacts producible by skills in the same stage
3. **Include a `>=N` numeric threshold — MANDATORY**

**Gate quantification rule (C-09): Every non-echo gate must contain at least one `>=N` count.**

```
# Before (no threshold — FAILS C-09):
gate: "scout-feasibility artifact present"

# After (quantified — PASSES C-09):
gate: ">=2 scout signals present (feasibility + market), 0 P1 blockers"
```

Quantification patterns:
- `>=N {namespace} signals present`
- `>=N artifacts written with 0 P1 open questions`
- `>=N {namespace} findings synthesized`
- Combined: `>=2 scout artifacts AND draft-spec written`

Rewrite any gate lacking `>=N` before proceeding.

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
    intent: "{strategic question this phase answers}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

**Validation checklist — every item must pass before writing:**
- [ ] YAML is valid
- [ ] Echo stage is last, `auto: true`, no `skills` or `gate`
- [ ] All skill names from the 47-skill Signal catalog
- [ ] Every non-echo stage has a non-trivial gate
- [ ] **Every non-echo stage has an `intent` field (strategic question, not skill description)**
- [ ] **Every non-echo gate contains a `>=N` numeric threshold**
- [ ] Gate artifacts are producible by skills in the same stage (no forward references)
- [ ] Stages ordered by namespace layer dependency (scout → draft → review/prove/flow/trace → listen → topic)

---

## V-05 — Full Synthesis (V-01 + V-02 + V-03 + Arc Assertion)

**Axis**: All three single-axis mechanisms (quantified gates, phase intent, traceability audit)
combined with an explicit program-level evidence arc assertion that the model must write before
drafting stages.

**Hypothesis**: V-04 stacks V-01 and V-02. V-05 adds V-03 (traceability audit) and a program-level
arc assertion — a pre-stage step requiring the model to articulate the full arc ("breadth → depth →
validation → monitoring") before enumerating any skills. The arc assertion serves two purposes:
(1) it anchors C-08 explicitly rather than relying on the model to discover the arc through layer
ordering, and (2) it forces the model to plan the whole program before any stage is written, reducing
the chance of incoherent mid-program pivots. With all four mechanisms active, the projected score
is 110/110 — the first R2 variant theoretically capable of a perfect run. The risk is prompt
length: at ~800 words of instructions, some models may truncate or simplify. The validation
checklist is positioned at the end as a hard gate on output completeness.

**R2 new elements vs R1 V-03 baseline**:
- Step 2b: Evidence Arc Assertion (new) — model writes the arc before drafting stages
- Step 3b: Intent Declaration (from V-02)
- Step 5a: Traceability Audit (from V-03)
- Step 5b: Gate Quantification Mandate (from V-01)

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
The plan reflects a deliberate evidence arc. Every stage declares its strategic intent.
Every gate is quantified and traceable to skills in the same stage.
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

Layer dependency rule: scout precedes draft; draft precedes review/prove/flow/trace; those precede listen; listen precedes topic. Echo is always last.

---

### Step 2 — Assert the evidence arc

**Before drafting any stage, write the program's evidence arc narrative.**

The arc must cover three phases:

1. **BREADTH** — What questions must be answered before committing to build?
   (scout + draft namespaces answer these)

2. **DEPTH** — What must be validated and simulated once the design is committed?
   (review + prove + flow + trace namespaces answer these)

3. **MONITORING** — What must be learned after shipping?
   (listen + topic namespaces answer these)

Write the arc as three bullet points naming the specific questions this topic needs to answer
in each phase. Example:

```
Evidence arc for {topic}:
- BREADTH: Is the market real? Is the architecture feasible? Do we have stakeholder alignment?
- DEPTH: Does the design hold up to expert review? Can the core hypothesis be proved?
         Does the system behave correctly under the key flows and traces?
- MONITORING: What do early adopters report? Where does support friction appear?
              What does the full signal picture say — are we learning what we expected?
```

This arc drives stage grouping. Every stage must fit one of these three phases.
Stages that don't map to a phase of the arc indicate a planning error — remove or regroup.

---

### Step 3 — Group into stages with intent declarations

Group skills into 3–6 stages aligned to the arc phases. For each stage:

**a) Name the stage** with a strategic phase label:
- Good: `discovery`, `de-risk`, `design`, `validate`, `simulate`, `synthesize`, `monitor`
- Bad: `scout_skills`, `stage_1`, `namespace_layer_3`

**b) Declare intent — MANDATORY:**
Every non-echo stage must carry an `intent` field phrased as a strategic question.

```yaml
intent: "Is the market real and is this technically feasible?"  # GOOD
intent: "Runs scout skills"                                      # BAD — describes, not asks
```

**c) Select skills** from the arc-phase-appropriate namespace layer. 2+ skills per stage.
Skills must follow namespace layer order within and across stages.

---

### Step 4 — Write gate conditions

Write one gate per non-echo stage naming specific artifact types. Reference only artifacts
producible by skills in the same stage (no forward references to later namespace work).

---

### Step 5 — Run pre-write checks

**5a — Traceability audit (C-11 check):**
For every non-echo gate that names an artifact, verify a skill in the same stage produces it.

```
Stage: discovery
  gate artifact: "scout-feasibility artifact"  -> scout:feasibility  [OK]
  gate artifact: "scout-market artifact"        -> scout:market       [OK]
Stage: validate
  gate artifact: "review-design artifact"       -> review:design      [OK]
  gate artifact: "prove-synthesize artifact"    -> prove:synthesize   [OK]
```

If any gate artifact has no matching skill in the same stage: fix the gate or move the skill
before proceeding.

**5b — Gate quantification (C-09 check):**
Every non-echo gate must contain a `>=N` numeric threshold.

```
# FAILS (no threshold):
gate: "scout-feasibility artifact present"

# PASSES:
gate: ">=2 scout artifacts present (feasibility + market) with 0 P1 blockers"
```

Add thresholds to any gate that lacks `>=N` before proceeding.

---

### Step 6 — Build the echo stage

```yaml
- name: echo
  auto: true
```

---

### Step 7 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth: "{question}"
  depth: "{question}"
  monitoring: "{question}"
stages:
  - name: {strategic-phase-name}
    intent: "{strategic question this phase answers}"
    skills:
      - {namespace}:{skill}
      - {namespace}:{skill}
    gate: ">=N {signal type} AND {artifact condition}"

  # ... additional stages ...

  - name: echo
    auto: true
```

**Final validation checklist — every item must pass before writing:**
- [ ] YAML is valid
- [ ] `evidence_arc` block present with breadth/depth/monitoring questions
- [ ] Echo stage is last, `auto: true`, no `skills` or `gate`
- [ ] All skill names from the 47-skill Signal catalog
- [ ] Every non-echo stage has a non-trivial gate
- [ ] **Every non-echo stage has an `intent` field (strategic question)**
- [ ] **Every non-echo gate contains `>=N` numeric threshold**
- [ ] **Traceability audit complete — no gate artifact is a forward reference**
- [ ] Stages ordered by namespace layer (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] All stages map to one of the three arc phases (breadth / depth / monitoring)

---

## Variation Summary

| Variant | Primary Axis | New vs R1 V-03 | C-09 target | C-10 target | C-11 target | Projected score |
|---------|-------------|----------------|-------------|-------------|-------------|-----------------|
| V-01 | Quantified Gate Mandate | `>=N` syntax per gate | Direct mandate | Inherited from V-03 naming | Inherited from V-03 layer walk | 105/110 |
| V-02 | Phase Intent Declaration | `intent:` field per stage | Unconstrained | Direct mandate | Inherited | 105/110 |
| V-03 | Gate Traceability Audit | Pre-write audit table | Unconstrained | Inherited from naming | Direct mandate | 105/110 |
| V-04 | V-01 + V-02 | `>=N` gates + `intent:` fields | Direct mandate | Direct mandate | Inherited | 110/110 |
| V-05 | Full synthesis | arc assertion + `intent:` + audit + `>=N` | Direct mandate | Direct mandate | Direct mandate | 110/110 |

**Key discriminators for scoring:**
- V-01 PASS: every gate has `>=N` count; no `intent:` fields
- V-02 PASS: every stage has `intent:` question field; no `>=N` in gates
- V-03 PASS: traceability audit table present in output; no `>=N`, no `intent:`
- V-04 PASS: both `>=N` gates and `intent:` fields; no audit table
- V-05 PASS: `evidence_arc:` block + `intent:` fields + traceability audit + `>=N` gates

**Universal floor maintained from R1 V-03**: all variants inherit the layer-walk structure
(C-05 PASS), strategic phase naming (C-10 base), artifact-grounded gates (C-07 PASS → C-11 base),
and arc sequencing (C-08 PASS). R2 axes layer explicit mechanisms on top of this floor,
trading the risk of over-instruction for the reward of cracking the C-09 ceiling.
