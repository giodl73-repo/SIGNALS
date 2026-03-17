# program-plan — R4 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. All five variations target 140/140 under the v4 rubric.

**R4 diagnostic from v4 scoring of R3 variants:**
- V-01 R3 (125/140): C-15 FAIL (tier headers, no criterion IDs), C-16 FAIL (no `evidence_arc:` field), C-17 FAIL (content constraint only, no interrogative form requirement)
- V-02 R3 (135/140): C-15 PASS, C-17 PASS. **C-16 FAIL** — no `evidence_arc:` YAML field despite strong C-08/C-12 mechanisms
- V-03 R3 (130/140): C-17 PASS. **C-15 FAIL** (tier headers only), **C-16 FAIL** (no `evidence_arc:` field)
- V-04 R3 (135/140): C-15 PASS, C-16 PASS. **C-17 FAIL** — bad example is "What do we need to know?" (non-specific question, not a declarative statement)
- V-05 R3 (n/a): Likely has C-15, C-16; same C-17 problem as V-04 R3

**Path to 140/140** — every R4 variant must add all three:
1. **C-15**: criterion IDs on every checklist item (`- [ ] C-01: YAML valid`, not just tier headers)
2. **C-16**: `evidence_arc:` as explicit required top-level YAML field in output schema
3. **C-17**: bad example in investigative question step must be a **declarative statement** (not a non-specific question), labeled "NOT A QUESTION", "STATEMENT NOT A QUESTION", or equivalent

**R4 variation axes (single-axis V-01 through V-03, combinations V-04/V-05):**
- V-01: Role sequence — arc assertion FIRST (Step 1, before skill catalog), arc as primary planning contract
- V-02: Output format — arc schema with per-stage `phase:` field that links each stage back to arc phase
- V-03: Phrasing register — V-03 R3 terse extended with all three new criteria
- V-04: V-02 R3 + `evidence_arc:` YAML field (closes V-02 R3's sole C-16 gap)
- V-05: V-04 R3 + C-17 fix (declarative statement bad example) + updated anti-pattern

---

## V-01 — Arc-First Role Sequence

**Axis**: Role sequence — arc assertion precedes skill catalog (Step 1 → arc, Step 2 → catalog,
Step 3 → per-stage questions). The `evidence_arc:` block is the first output committed to paper
before any stage is designed.

**Hypothesis**: In every R3 variant, arc assertion occurs mid-sequence after the skill catalog
(V-04, V-05) or is implied by stage ordering (V-01, V-02, V-03). When arc comes after catalog,
the model is tempted to write stages that reflect skill availability rather than arc phases —
"I have these scout skills, let me make a scout stage" rather than "my breadth phase needs to
answer X, which skills cover that?" Arc-first inverts the dependency: arc phases are committed
before skills are selected, so every stage grouping is justified by an arc phase, not by
namespace clustering. Secondary: moving arc to Step 1 makes C-16 an *entry* requirement, not
a trailing YAML field — a model cannot complete Step 1 without producing the `evidence_arc:` block.

**C-15**: criterion IDs on all checklist items (explicit throughout).
**C-16**: `evidence_arc:` is Step 1 output, appears first in YAML template.
**C-17**: Step 3 bad example is `"Understand the competitive landscape before committing."` —
declarative statement, labeled "STATEMENT, NOT A QUESTION".

**New vs R3 V-04 (base)**:
- Step ordering reversed: arc → catalog → per-stage questions → grouping
- Bad example in Step 3 changed to declarative statement (C-17 closure)
- `evidence_arc:` YAML field moved to first position in template (C-16 emphasized)
- Criterion IDs added to all checklist items (C-15 — V-04 R3 already had this)

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
The `evidence_arc:` is the primary planning contract — every stage exists to answer an arc question.
Every stage carries an investigative question. Every gate is quantified and traceable.
The program is a plan, not an executor.

---

### Step 1 — Assert the evidence arc (write this first)

**Write the `evidence_arc:` block before selecting any skills or designing any stages.**

The arc covers three phases:
- **BREADTH** — What must be known before committing to build? (scout + draft namespace layers)
- **DEPTH** — What must be validated after committing? (review + prove + flow + trace layers)
- **MONITORING** — What must be learned after shipping? (listen + topic layers)

Write the arc as YAML now:

```yaml
evidence_arc:
  breadth: "{specific breadth question for $TOPIC — ends with ?}"
  depth: "{specific depth/validation question for $TOPIC — ends with ?}"
  monitoring: "{specific post-ship learning question for $TOPIC — ends with ?}"
```

Every stage you design must map to exactly one arc phase. A planned stage that doesn't map
to breadth, depth, or monitoring indicates a planning error — remove it or reassign its skills.

---

### Step 2 — Load the skill catalog

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

### Step 3 — Write investigative questions per stage (MANDATORY)

**Before selecting any skills, enumerate each planned stage and its specific investigative question.**

The question must:
- Be answerable by the skills in that stage (not by the whole program)
- Be specific to that stage (not a horizon question applying to all stages)
- Be phrased as a question — ending with `?`

```
# GOOD — stage-specific, interrogative, answerable by that stage's skills:
discovery:  "Do we understand the competitive landscape, technical feasibility, and core
             requirements well enough to commit to building this?"
de-risk:    "Does the proposed design satisfy expert review, and can the primary hypothesis
             be empirically validated before full build begins?"
monitor:    "What are users reporting post-ship, and are adoption signals tracking to prediction?"

# BAD — STATEMENT, NOT A QUESTION (rewrite as interrogative ending with ?):
discovery:  "Understand the competitive landscape before committing."
de-risk:    "Validate the design and prove the hypothesis."
monitor:    "Track user reports and adoption metrics."
```

These become the `intent:` field values in the final YAML.

---

### Step 4 — Group skills into stages

Group into 3–6 stages (not counting echo). Each stage must map to one arc phase from Step 1.

For each stage:
1. `name:` = strategic label encoding purpose: `discovery`, `de-risk`, `validate`, `simulate`,
   `synthesize`, `monitor`. NOT: `scout_stage`, `stage_1`, `layer_3`
2. `intent:` = the investigative question from Step 3 (verbatim, ending with `?`)
3. `skills:` = 2+ skills from the arc-phase-appropriate namespace layer
4. Enforce layer order across stages

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Each gate must:
- Name specific artifact types or signal counts (NOT: `"PM approves"`, `"done"`, `""`)
- Reference only artifacts producible by skills **in the same stage** (no forward references)

---

### Step 6 — Apply enforcement checks

**Step 6a — Gate quantification mandate (C-09 — MANDATORY):**

Every non-echo gate must contain `>=N`.

```
# FAILS C-09 — missing threshold:
gate: "scout-feasibility artifact present"

# PASSES C-09 — quantified:
gate: ">=2 scout signals present (feasibility + requirements), 0 P1 blockers flagged"
```

Threshold patterns: `>=N {namespace} signals`, `>=N artifacts written with 0 P1 open`,
`>=N findings addressed`. Rewrite any gate missing `>=N` before proceeding.

**Step 6b — Traceability audit (C-11 — MANDATORY before writing YAML):**

For every non-echo gate artifact, identify the producing skill in the same stage.

```
Traceability audit:

Stage: discovery
  gate artifact: "scout-feasibility artifact"  -> produced by: scout:feasibility  [OK]
  gate artifact: "scout-requirements artifact" -> produced by: scout:requirements [OK]

Stage: de-risk
  gate artifact: "review-design artifact"      -> produced by: review:design      [OK]
  gate artifact: "prove-synthesize artifact"   -> produced by: prove:synthesize   [OK]

Stage: monitor
  gate artifact: "listen-adoption artifact"    -> produced by: listen:adoption    [OK]
```

If any artifact has no matching skill in the same stage:

```
Stage: design
  gate artifact: "scout-feasibility artifact" -> [NONE — FORWARD REFERENCE]
  ACTION: Move scout:feasibility to an earlier stage, OR rewrite gate to reference
          an artifact producible by a skill already in this stage.
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

The `evidence_arc:` block (from Step 1) appears FIRST — before `stages:`.

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth: "{specific breadth question, ends with ?}"
  depth: "{specific depth/validation question, ends with ?}"
  monitoring: "{specific post-ship learning question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    intent: "{specific investigative question from Step 3, ends with ?}"
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
- [ ] **C-02** Echo stage is last, `auto: true`, has no `skills` or `gate` fields
- [ ] **C-03** Every skill name maps to the 47-skill Signal catalog
- [ ] **C-04** Every non-echo stage has a non-trivial gate condition

**Recommended tier** (all three should pass):
- [ ] **C-05** Stages ordered by namespace layer dependency (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier** (all should pass — enforced by Steps 1, 3, 6a, 6b above):
- [ ] **C-08** Plan reflects the strategic evidence arc (breadth → depth/validation → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Step 6a enforced)
- [ ] **C-10** Every non-echo stage has strategic `name:` encoding purpose, not namespace group
- [ ] **C-11** Traceability audit complete — zero FORWARD REFERENCEs (Step 6b enforced)
- [ ] **C-12** Every non-echo stage has `intent:` as stage-specific investigative question (Step 3)
- [ ] **C-13** Both C-09 (Step 6a) and C-11 (Step 6b) isolated with dedicated enforcement steps and format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ criteria
- [ ] **C-15** Every checklist item above carries an explicit criterion ID (C-01 through C-14)
- [ ] **C-16** `evidence_arc:` block present in output YAML as first-class required field (Step 1 + Step 8 enforced)
- [ ] **C-17** Every `intent:` and `evidence_arc:` value is an interrogative question ending with `?` — no declarative statements (Step 3 enforced)

---

## V-02 — Arc Schema with Phase References (Output Format)

**Axis**: Output format — the arc is a structured YAML schema and each stage carries an explicit
`phase:` field (`breadth | depth | monitoring`) that references back to the arc. The output
becomes self-verifying: arc phases are declared, then every stage cites which phase it satisfies.

**Hypothesis**: V-04 R3 requires `evidence_arc:` but stages have no structural link to arc phases.
A model could write valid arc values that don't match the actual stage sequence, and a reader
must infer phase assignment from namespace layer. Adding a `phase:` field to each stage makes
arc coverage machine-checkable: count stages per phase, verify every phase has at least one
stage, and confirm no stage exists without a phase assignment. This strengthens C-08 and C-16
simultaneously — the arc is both semantically deliberate (C-08) and structurally enforced (C-16).

**C-15**: criterion IDs on all checklist items.
**C-16**: `evidence_arc:` required in Step 2 and in YAML template; `phase:` field ties each
stage back to the arc.
**C-17**: Step 3 bad example is `"Understand the market and confirm technical feasibility."` —
declarative statement, labeled "NOT INTERROGATIVE — rewrite". `intent:` values must end with `?`.

**New vs R3 V-02 (base — 135/140, has C-15 + C-17, lacks C-16)**:
- Step 2 rewritten: `evidence_arc:` block now required output with `?` termination (C-16)
- `phase:` field added to each stage schema, linking stages to arc (strengthens C-08/C-16)
- YAML template updated to show arc block + phase references
- Bad example in Step 3 changed to declarative statement (V-03 R3's C-17 mechanism, reinforcing V-02 R3's `?` requirement)

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
The arc is a required YAML field. Every stage declares its arc phase. Every gate is quantified
and traceable. The program is a plan, not an executor.

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

### Step 2 — Write the evidence arc (required YAML output)

**The `evidence_arc:` block is a required top-level field in the output YAML.**

Write it before planning any stage. Each value is an investigative question for $TOPIC,
ending with `?`. Namespace-to-phase mapping:
- `breadth` → scout + draft (Layers 1–2)
- `depth` → review + prove + flow + trace (Layer 3)
- `monitoring` → listen + topic (Layers 4–5)

```yaml
# Required — write this block before designing any stage:
evidence_arc:
  breadth: "{What must be known about $TOPIC before committing to build? — ends with ?}"
  depth: "{What must be validated and simulated once committed to $TOPIC? — ends with ?}"
  monitoring: "{What must be learned after $TOPIC ships? — ends with ?}"
```

---

### Step 3 — Write investigative questions per stage (MANDATORY)

**Before grouping skills, enumerate each planned stage and its specific question.**

Each question must:
- Be answerable by the skills you will assign to that stage
- Be specific to that stage (not a generic horizon question)
- End with `?`

```
# GOOD — stage-specific, answerable, interrogative:
discovery:  "Is the market real and can we technically deliver within the identified constraints?"
validate:   "Does the design meet expert review standards and can the core hypothesis be proved?"

# BAD — NOT INTERROGATIVE (declarative statement — rewrite as question ending with ?):
discovery:  "Understand the market and confirm technical feasibility."
validate:   "Run expert review and prove the hypothesis."
```

These become the `intent:` field values. Every `intent:` value must end with `?`.

---

### Step 4 — Group skills into stages

Group into 3–6 stages (not counting echo). For each stage:

1. `name:` = strategic label: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`
   NOT: `scout_skills`, `stage_1`, `layer_3`
2. `phase:` = which arc phase this stage satisfies: `breadth` | `depth` | `monitoring`
3. `intent:` = the investigative question from Step 3 (verbatim, ending with `?`)
4. `skills:` = 2+ skills from the phase-appropriate namespace layer
5. Enforce layer order across stages

Arc coverage check: every arc phase (`breadth`, `depth`, `monitoring`) must have at least one
stage assigned. If a phase has no stage, add one or remove the phase from `evidence_arc:`.

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Gate must:
- Name specific artifact types or signal counts (NOT: `"PM approves"`, `"done"`)
- Reference only artifacts producible by skills **in the same stage**

---

### Step 6 — Apply enforcement checks

**Step 6a — Gate quantification mandate (C-09 — MANDATORY):**

Every non-echo gate must contain `>=N`.

```
# FAILS C-09:
gate: "draft-spec written and review-design artifact present"

# PASSES C-09:
gate: ">=1 draft-spec artifact written AND >=1 review-design artifact present, 0 open P1 items"
```

Rewrite any gate missing `>=N` before proceeding.

**Step 6b — Traceability audit (C-11 — MANDATORY before writing YAML):**

Map every gate artifact to a producing skill in the same stage.

```
Traceability audit:

Stage: discovery (phase: breadth)
  "scout-feasibility artifact"  -> scout:feasibility  [OK]
  "scout-market artifact"       -> scout:market        [OK]

Stage: validate (phase: depth)
  "review-design artifact"      -> review:design       [OK]
  "prove-synthesize artifact"   -> prove:synthesize    [OK]

Stage: design [PROBLEM — phase: depth, contains scout skill]:
  "scout-feasibility artifact"  -> [NONE — FORWARD REFERENCE]
  FIX: move scout:feasibility to a breadth-phase stage, or rewrite gate.
```

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
  breadth: "{specific breadth question, ends with ?}"
  depth: "{specific depth/validation question, ends with ?}"
  monitoring: "{specific post-ship question, ends with ?}"
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

**Aspirational tier** (all should pass — enforced by Steps 2, 3, 6a, 6b above):
- [ ] **C-08** Plan reflects strategic evidence arc (breadth → depth → monitoring); `evidence_arc:` and `phase:` fields consistent
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Step 6a enforced)
- [ ] **C-10** Every non-echo stage has strategic `name:` encoding purpose
- [ ] **C-11** Traceability audit complete — zero FORWARD REFERENCEs (Step 6b enforced)
- [ ] **C-12** Every non-echo stage has `intent:` as a stage-specific investigative question (Step 3)
- [ ] **C-13** Both C-09 (Step 6a) and C-11 (Step 6b) isolated with dedicated enforcement steps and format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ criteria
- [ ] **C-15** Every checklist item carries an explicit criterion ID (C-01 through C-14 above)
- [ ] **C-16** `evidence_arc:` block present in output YAML as required top-level field (Step 2 + Step 8)
- [ ] **C-17** All `intent:` and `evidence_arc:` values end with `?` — no declarative statements (Step 3 enforced)

---

## V-03 — Terse Imperative + All New Criteria (Phrasing Register)

**Axis**: Phrasing register — V-03 R3's ultra-terse numbered-rules register, extended with:
(a) `evidence_arc:` required YAML field (C-16 via Rule 4 + Check A), (b) criterion IDs on every
checklist item (C-15), (c) the bad example in Check A changed to a declarative statement
with "STATEMENT, NOT A QUESTION" label (C-17 strengthened).

**Hypothesis**: V-03 R3 scores 130/140 (has C-17, lacks C-15 and C-16). The terse register is
the shortest prompt structure and already achieves strong C-13 via labeled Check blocks. Adding
`evidence_arc:` to Rule 4 and the OUTPUT FORMAT template is a single-line insertion. Adding
criterion IDs to the checklist is a cosmetic change. The discriminating signal: V-03 R4 is the
minimum-length prompt to achieve 140/140 — it tests whether all three new criteria can be
satisfied without expanding the prompt's prose footprint.

**C-15**: criterion IDs on every checklist item.
**C-16**: Rule 4 requires `evidence_arc:` with three phase values. Check A verifies it.
OUTPUT FORMAT template shows it.
**C-17**: Check A bad example is `"Understand the market and confirm feasibility."` —
declarative statement, labeled "STATEMENT, NOT A QUESTION — REWRITE".

**New vs R3 V-03 (base — 130/140, has C-17)**:
- Rule 4 (new): `evidence_arc:` required in output YAML (C-16)
- Check A: expanded to cover arc field + bad example changed to statement (C-16 + C-17 explicit)
- Validation checklist: criterion IDs added to every item (C-15)

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
4. **Arc field required**: Output YAML must include `evidence_arc:` with three phase keys:
   `breadth`, `depth`, `monitoring`. Each value must end with `?`.
5. **Intent mandate**: Every non-echo stage must have `intent:` as an interrogative question ending with `?`.
   - PASS: `intent: "Is the market real and can we technically deliver?"`
   - FAIL — STATEMENT, NOT A QUESTION: `intent: "Understand the market and confirm feasibility."`
   - FAIL — MISSING `?`: `intent: "Is the market real"`
6. **Gate artifacts**: Every non-echo gate names specific artifact types.
   - PASS: `gate: "scout-feasibility artifact present"`
   - FAIL: `gate: "PM approves"` / `gate: "done"` / `gate: ""`
7. **Gate quantification — MANDATORY**: Every non-echo gate contains `>=N`.
   - PASS: `gate: ">=2 scout signals (feasibility + requirements), 0 P1 blockers"`
   - FAIL: `gate: "scout-feasibility artifact present"` (threshold missing)
8. **Traceability**: Every gate artifact is producible by a skill in the same stage.
9. **Echo**: Final stage is always `- name: echo` with `auto: true`. No `skills`. No `gate`. No other fields.
10. **Layer order**: Stages observe namespace layer ordering within and across all stages.

---

**PRE-WRITE CHECKS — complete all three before assembling YAML:**

**Check A — Arc field + Investigative questions (C-16 + C-17):**

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
Stage: validate
  "review-design artifact"     -> review:design       [OK]

Stage: design [PROBLEM]
  "scout-feasibility artifact" -> [NO SCOUT SKILL IN THIS STAGE — FORWARD REFERENCE]
  FIX: move skill or rewrite gate.
```

---

**OUTPUT FORMAT:**

```yaml
topic: {topic}
strategy: {one-line summary}
evidence_arc:
  breadth: "{question, ends with ?}"
  depth: "{question, ends with ?}"
  monitoring: "{question, ends with ?}"
stages:
  - name: {strategic-phase-name}
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
- [ ] **C-12**: Every non-echo stage has `intent:` as stage-specific interrogative question (Check A)
- [ ] **C-13**: C-09 (Check B) and C-11 (Check C) both have dedicated labeled enforcement blocks with examples
- [ ] **C-14**: This checklist spans Essential, Recommended, Aspirational tiers with 4+ criteria
- [ ] **C-15**: Every checklist item above carries an explicit criterion ID
- [ ] **C-16**: `evidence_arc:` block in output YAML (Rule 4 + Check A + OUTPUT FORMAT enforced)
- [ ] **C-17**: All `intent:` and `evidence_arc:` values are interrogative questions ending with `?` (Check A + Rule 5 enforced)

---

## V-04 — V-02 R3 + Arc Field (Closes V-02 R3's C-16 Gap)

**Axis**: Combination — V-02 R3 (135/140: C-15 PASS, C-17 PASS, C-16 FAIL) with one targeted
addition: a required `evidence_arc:` YAML field in Step 2.

**Hypothesis**: V-02 R3 is 5 pts from 140/140. The sole gap is C-16: it requires `intent:`
fields ending with `?` (C-17 PASS) and has a criterion-ID checklist (C-15 PASS) but never
asks for an arc block in the YAML. Adding Step 2 arc assertion — with the same `?` termination
requirement already applied to `intent:` fields — closes C-16 without disrupting any other
mechanism. The `?` requirement applied to both `intent:` and `evidence_arc:` values makes
C-16 and C-17 mutually reinforcing: the model sees the interrogative form constraint twice
in the same prompt, applied to two different YAML fields.

**C-15**: retained from V-02 R3 (criterion-ID checklist).
**C-16**: new Step 2 requires `evidence_arc:` block in output YAML.
**C-17**: retained from V-02 R3 (`intent:` must end with `?`; bad example is `"Runs scout:feasibility"`
— a skill description, not a question). Additionally strengthened: `evidence_arc:` values also
require `?` termination, making interrogative form apply to both arc and stage levels.

**New vs R3 V-02 (base)**:
- Step 2 (new): evidence arc assertion — `evidence_arc:` required YAML field with `?` termination
- YAML template (Step 6, was Step 5): `evidence_arc:` block added before `stages:`
- C-16 added to checklist; C-17 note updated to cover both `intent:` and `evidence_arc:` values

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every stage declares its strategic intent as an investigative question. The evidence arc is a
required YAML field. Every gate is quantified and traceable. The program is a plan, not an executor.

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

### Step 2 — Write the evidence arc (required YAML field)

**The `evidence_arc:` block is a required top-level field in the output YAML.**

Write it now, before grouping any skills. Each value is an investigative question for $TOPIC
and must end with `?`.

```yaml
evidence_arc:
  breadth: "{What must be known about $TOPIC before committing to build? — ends with ?}"
  depth: "{What must be validated and simulated once committed to $TOPIC? — ends with ?}"
  monitoring: "{What must be learned after $TOPIC ships? — ends with ?}"
```

Arc-to-namespace mapping:
- `breadth` → scout + draft (Layers 1–2)
- `depth` → review + prove + flow + trace (Layer 3)
- `monitoring` → listen + topic (Layers 4–5)

---

### Step 3 — Write the investigative question per stage (MANDATORY)

**Before grouping any skills, enumerate each planned stage and its specific question.**

Each question must:
- Be answerable by the skills in that stage (not by the whole program)
- Be specific to that stage — not the same horizon question applied everywhere
- End with `?`

```yaml
# Good:
intent: "Is the market real and can we technically deliver within the identified constraints?"

# Bad (does not end with ?) — NOT A QUESTION:
intent: "Runs scout:feasibility, scout:market, scout:requirements"
intent: "Discovery"
intent: "Understand the competitive landscape and confirm feasibility constraints."
```

These become the `intent:` field values in the final YAML.

---

### Step 4 — Group skills into stages with intent declarations

Group into 3–6 stages. For each stage:

**a) Name the stage** with a strategic label:
- Good: `discovery`, `de-risk`, `design`, `validate`, `simulate`, `synthesize`, `monitor`
- Bad: `scout_skills`, `stage_1`, `namespace_layer_3`

**b) Declare intent — MANDATORY:**
Every non-echo stage must carry an `intent:` field. It must:
- Be the stage-specific investigative question from Step 3 (ends with `?`)
- NOT be a skill-list description: `"Runs scout:feasibility and scout:market"`
- NOT be a stage name restatement: `"Discovery phase"`

**c) Select skills** from the layer-appropriate namespace. 2+ per stage. Enforce layer order.

**d) Write the gate** with a `>=N` threshold — MANDATORY.

---

### Step 5 — Run pre-write enforcement checks

**Step 5a — Gate quantification (C-09 mandate):**

Every non-echo gate must contain `>=N`.

```
# FAILS C-09:
gate: "draft-spec written and review-design artifact present"

# PASSES C-09:
gate: ">=1 draft-spec artifact written AND >=1 review-design artifact present, 0 open P1 items"
```

Rewrite any gate missing `>=N` before proceeding.

**Step 5b — Traceability audit (C-11 mandate — MANDATORY before writing YAML):**

For every artifact named in a non-echo gate, identify the skill in the same stage that produces it.

```
Traceability audit:

Stage: discovery
  "scout-feasibility artifact"  -> scout:feasibility  [OK]
  "scout-market artifact"       -> scout:market        [OK]

Stage: validate
  "review-design artifact"      -> review:design       [OK]
  "prove-synthesize artifact"   -> prove:synthesize    [OK]
```

Flag and fix any FORWARD REFERENCE before proceeding:

```
Stage: design
  "scout-feasibility artifact"  -> [NONE in this stage — FORWARD REFERENCE]
  FIX: move scout:feasibility to an earlier stage, or rewrite gate to reference
       an artifact producible by a skill already in this stage.
```

---

### Step 6 — Assemble the program.yaml

```yaml
topic: {topic}
strategy: {one-line strategy summary}
evidence_arc:
  breadth: "{specific breadth question, ends with ?}"
  depth: "{specific depth/validation question, ends with ?}"
  monitoring: "{specific post-ship question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    intent: "{specific investigative question this phase answers, ends with ?}"
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
- [ ] **C-04** Every non-echo stage has a non-trivial gate (not "done", "proceed", or stage name restatement)

**Recommended tier** (depth and ordering — all three should pass):
- [ ] **C-05** Stages ordered by namespace layer dependency (scout → draft → review/prove/flow/trace → listen → topic)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages, no mega-stage
- [ ] **C-07** At least half of non-echo gates name specific artifact types or signal counts

**Aspirational tier** (arc and enforcement — all should pass):
- [ ] **C-08** Plan reflects a strategic evidence arc (breadth → depth/validation → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` numeric threshold (Step 5a enforced)
- [ ] **C-10/C-12** Every non-echo stage has `intent:` phrased as a stage-specific investigative question ending with `?` (Step 3 enforced)
- [ ] **C-11** Traceability audit complete — every gate artifact maps to a producing skill in the same stage (Step 5b enforced)
- [ ] **C-13** Both C-09 (Step 5a) and C-11 (Step 5b) have dedicated enforcement steps with format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ distinct criteria
- [ ] **C-15** Every checklist item carries an explicit criterion ID (C-01 through C-14 above)
- [ ] **C-16** `evidence_arc:` block present in output YAML as required top-level field (Step 2 enforced)
- [ ] **C-17** All `intent:` and `evidence_arc:` values end with `?` — no declarative statements (Steps 2 + 3 enforced)

---

## V-05 — V-04 R3 + C-17 Fix + Updated Anti-Pattern (Combination + Inertia Framing)

**Axis**: Combination — V-04 R3 (135/140: C-15 PASS, C-16 PASS, C-17 FAIL) with one targeted
change: the bad example in Step 3 is replaced with a declarative statement, and the anti-pattern
section (from V-05 R3) is extended with a C-17 failure example.

**Hypothesis**: V-04 R3 fails C-17 because its bad example is "What do we need to know before
building?" — a non-specific question, not a declarative statement. C-17 requires the bad example
to be a statement rather than a question (or to use a "NOT A QUESTION" label). The minimal fix:
change `"What do we need to know?"` to `"Understand the competitive landscape before committing."`,
label it "STATEMENT, NOT A QUESTION", and add a matching failure to the anti-pattern's `intent:`
field. All other V-04 R3 mechanisms — `evidence_arc:` YAML field, criterion-ID checklist,
pre-stage question step, traceability audit, gate quantification — remain identical.

**C-15**: retained from V-04 R3 (criterion-ID checklist).
**C-16**: retained from V-04 R3 (`evidence_arc:` YAML field).
**C-17**: bad example changed from non-specific question to declarative statement + "STATEMENT,
NOT A QUESTION" label. Anti-pattern shows `intent: "Understand the market."` as a C-17 failure.

**New vs R3 V-04 (base)**:
- Anti-pattern section (new, from V-05 R3): includes `intent: "Understand the market."` as C-17 failure
- Step 3 bad examples changed: `"What do we need to know?"` → `"Understand the competitive landscape."` with "STATEMENT, NOT A QUESTION" label

---

You are running `/program:plan` for Signal — the AI-first feature decision plugin.

**Inputs**
- Topic: `$TOPIC`
- Strategy: `$STRATEGY`

**What you are producing**
A staged program plan in YAML form: `simulations/program/plans/{topic}-program-{date}.md`.
Every stage asks an explicit investigative question. The evidence arc is a required YAML field.
Every gate is quantified and traceable. The program is a plan, not an executor.

---

### What a bad program plan looks like

Recognize these failure modes before writing — do not produce any of them:

```yaml
# FAILURE PATTERN — every line below violates at least one criterion:
stages:
  - name: stage_1                          # FAIL C-10: namespace-cluster label, not strategic
    intent: "Understand the market."       # FAIL C-17: declarative statement, NOT A QUESTION
    skills:
      - scout:feasibility
      - review:design                      # FAIL C-05: mixed layers (Layer 1 + Layer 3)
      - listen:feedback                    # FAIL C-05: mixed layers (Layer 4 in Layer 1 stage)
    gate: "team approves"                  # FAIL C-04/C-07/C-09: abstract prose, no artifact, no >=N

  - name: stage_2
    skills:
      - draft:spec                         # FAIL C-06: single-skill stage
    gate: "spec looks good"                # FAIL C-09: no >=N threshold

  - name: echo
    auto: true
    gate: "done"                           # FAIL C-02: echo cannot have a gate field
```

What is missing: `evidence_arc:` block, interrogative `intent:` fields (questions, not statements),
`>=N` gate thresholds, artifact-grounded gate conditions, layer ordering, clean echo stage.

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

### Step 2 — Assert the evidence arc (required YAML field)

Write the program's evidence arc before drafting any stage.
**The `evidence_arc:` block is required in the output YAML.**

```yaml
evidence_arc:
  breadth: "{What must be known before committing to build $TOPIC?}"
  depth: "{What must be validated and simulated once committed?}"
  monitoring: "{What must be learned after $TOPIC ships?}"
```

Arc-to-namespace mapping:
- BREADTH → scout + draft (Layers 1–2)
- DEPTH → review + prove + flow + trace (Layer 3)
- MONITORING → listen + topic (Layers 4–5)

Every stage maps to exactly one arc phase. Stages that don't map indicate a planning error.

---

### Step 3 — Write investigative questions per stage (MANDATORY)

**Before selecting any skills, enumerate each planned stage and its specific investigative question.**

The question must:
- Be answerable by the skills in that stage (not by the whole program)
- Be specific to that stage — not a generic question applying everywhere
- Be phrased as a question, NOT a statement

```
# GOOD — stage-specific, answerable, interrogative (must end with ?):
discovery:  "Do we understand the competitive landscape, technical feasibility, and
             core requirements well enough to commit to building this feature?"
de-risk:    "Does the proposed design satisfy expert review, and can the primary
             value hypothesis be empirically validated before full build begins?"
monitor:    "What are users experiencing post-ship, and are adoption signals tracking
             to prediction?"

# BAD — STATEMENT, NOT A QUESTION (rewrite as interrogative ending with ?):
discovery:  "Understand the competitive landscape before committing."
de-risk:    "Validate the design and confirm the hypothesis."
monitor:    "Track adoption metrics and user reports."
```

These become the `intent:` field values. See anti-pattern for what `intent: "Understand..."` looks like.

---

### Step 4 — Group skills into stages

Group into 3–6 stages aligned to arc phases:
1. `intent:` = the stage-specific investigative question from Step 3 (verbatim).
2. `name:` = strategic label: `discovery`, `de-risk`, `validate`, `simulate`, `synthesize`, `monitor`.
   Not: `scout_stage`, `stage_1`, `namespace_layer_3`.
3. 2+ skills per stage from the arc-phase-appropriate namespace layer.
4. Enforce layer order within and across stages.

---

### Step 5 — Write gate conditions

One gate per non-echo stage. Gates name specific artifact types producible by skills in the same stage.
Reference the anti-pattern: `"team approves"` and `"looks good"` are not gates.

---

### Step 6 — Apply enforcement checks

**Step 6a — Gate quantification mandate (C-09 — MANDATORY for every non-echo gate):**

```
# FAILS (no threshold — see anti-pattern stage_2):
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
  breadth: "{question, ends with ?}"
  depth: "{question, ends with ?}"
  monitoring: "{question, ends with ?}"
stages:
  - name: {strategic-phase-name}
    intent: "{specific investigative question — ends with ?, NOT a statement}"
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
- [ ] **C-05** Stages in namespace layer order — no mixed-layer stages (contrast anti-pattern)
- [ ] **C-06** Each stage groups 2+ related skills — no single-skill stages
- [ ] **C-07** At least half of non-echo gates name specific artifact types

**Aspirational tier** (all should pass — enforced by Steps 2, 3, 6a, 6b):
- [ ] **C-08** Plan reflects strategic `evidence_arc:` (breadth → depth → monitoring)
- [ ] **C-09** Every non-echo gate contains `>=N` threshold (Step 6a enforced)
- [ ] **C-10** Every non-echo stage has strategic `name:` encoding purpose (contrast anti-pattern)
- [ ] **C-11** Traceability audit complete — zero FORWARD REFERENCEs (Step 6b enforced)
- [ ] **C-12** Every non-echo stage has `intent:` as stage-specific investigative question (Step 3)
- [ ] **C-13** Both C-09 (Step 6a) and C-11 (Step 6b) isolated with dedicated enforcement steps and format examples
- [ ] **C-14** This checklist spans Essential, Recommended, and Aspirational tiers with 4+ criteria
- [ ] **C-15** Every checklist item carries an explicit criterion ID (C-01 through C-14 above)
- [ ] **C-16** `evidence_arc:` block present in output YAML as required field (Step 2 enforced)
- [ ] **C-17** All `intent:` and `evidence_arc:` values are interrogative questions ending with `?` — no declarative statements (Step 3 enforced; contrast anti-pattern `intent: "Understand the market."`)

---

## Variation Summary

| Variant | Primary Axis | C-15 mechanism | C-16 mechanism | C-17 mechanism | Base | Projected v4 |
|---------|-------------|----------------|----------------|----------------|------|--------------|
| V-01 | Role sequence (arc first) | Criterion IDs on all 16 checklist items | Step 1 arc block = first output; YAML template places `evidence_arc:` before `stages:` | Bad examples are declarative statements labeled "STATEMENT, NOT A QUESTION" | V-04 R3 reordered | 140/140 |
| V-02 | Output format (phase references) | Criterion IDs on all 16 checklist items | Step 2 required arc block + `phase:` field on each stage links stages to arc | Bad example `"Understand the market..."` labeled "NOT INTERROGATIVE"; `intent:` must end with `?` | V-02 R3 extended | 140/140 |
| V-03 | Phrasing register (terse) | Criterion IDs on all 17 checklist items (terse format) | Rule 4 mandates `evidence_arc:`; Check A verifies it; OUTPUT FORMAT shows it | Check A bad example is declarative statement labeled "STATEMENT, NOT A QUESTION" | V-03 R3 extended | 140/140 |
| V-04 | V-02 R3 + C-16 | Retained from V-02 R3 | New Step 2 adds `evidence_arc:` required YAML block with `?` termination | Retained from V-02 R3 (`intent:` ends with `?`; bad example includes declarative statement) | V-02 R3 | 140/140 |
| V-05 | V-04 R3 + C-17 + anti-pattern | Retained from V-04 R3 | Retained from V-04 R3 (`evidence_arc:` YAML field) | Bad example changed to declarative statement + "STATEMENT, NOT A QUESTION" label; anti-pattern shows `intent: "Understand..."` | V-04 R3 | 140/140 |

**Key discriminators for scoring:**
- V-01 PASS: arc block appears in output reasoning BEFORE skill catalog; `evidence_arc:` is Step 1 output, not late-stage
- V-02 PASS: each stage carries `phase: breadth|depth|monitoring` field linking it to arc; arc coverage check in Step 4
- V-03 PASS: shortest prompt; Check A covers both arc field and interrogative form in one labeled block; all items terse
- V-04 PASS: `evidence_arc:` required in Step 2 output; `intent:` and arc values both end with `?` — same constraint applied twice
- V-05 PASS: anti-pattern explicitly shows `intent: "Understand the market."` as C-17 failure before any instruction is given

**Why R4 closes the R3 gaps:**
- C-15 (V-01 R3, V-03 R3 fail): all R4 variants add explicit criterion IDs to every checklist item.
- C-16 (V-01, V-02, V-03 R3 fail): all R4 variants require `evidence_arc:` as a top-level YAML field
  in the output schema, not merely implied by stage ordering.
- C-17 (V-01, V-04 R3 fail): all R4 variants provide a bad example that is a declarative statement
  (not a non-specific question), making the interrogative form constraint unambiguous.
