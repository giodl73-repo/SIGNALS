# program-plan — R7 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Targeting v7 rubric (2026-03-15) criteria:
- **C-23** — Explicit catalog-access prohibition within the phase-declaration step
- **C-24** — Per-stage compliance table spans all three criterion ladders
- **C-25** — Dedicated labeled CONSTRUCTION ORDER protocol block

R6 ceiling: 170 / 180 (V-01, V-02, V-03; each passes exactly one new criterion).
R7 target: **180 / 180** — all five variants pass all three new criteria simultaneously.

Variation axes explored:
- V-01 (single axis): Construction protocol order — CONSTRUCTION ORDER block first
- V-02 (single axis): Output format — table-centric, ladder-named column headers
- V-03 (single axis): Lifecycle emphasis — phase-boundary ritual, catalog prohibition as arc-integrity protection
- V-04 (combined): V-01 CONSTRUCTION ORDER block + V-02 ladder-named table format
- V-05 (combined): All three axes, terse imperative register

---

## V-01 — Construction Protocol-First

**Axis**: Construction protocol order — the CONSTRUCTION ORDER block serves as a labeled standalone section placed immediately after the catalog, enumerating all construction steps before any step body begins. The reader holds the complete sequence map before entering any single step.

**Hypothesis**: Declaring the full construction sequence upfront as a labeled protocol block (C-25) commits the builder to step ordering before reading any step body, making catalog-prohibition in Step 2 (C-23) structurally reinforced by the protocol summary. The 3-column per-stage compliance table with ladder labels makes C-24 self-documenting.

**C-19 pair**: C-18 (arc-structure ladder) × C-09 (gate-behavior ladder).

**Anticipated score**: 180 / 180

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. The program is a plan, not an executor — every skill can run standalone without the program. Your job is to produce a program that a team could follow as a sequenced evidence-building arc from discovery through synthesis.

---

**Valid Signal Plugin Skill Catalog**

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage's `skills` list. Do not invent, abbreviate, or namespace-expand skill names beyond what is shown.

---

## CONSTRUCTION ORDER

Review the complete construction sequence before beginning Step 1. Follow these steps in order — do not combine, skip, or reorder them.

1. State the topic (Step 1)
2. Declare evidence arc phases — **catalog is off-limits until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5. Design artifact-grounded, quantified gates (Step 5)
6. Write per-phase investigative questions in interrogative form (Step 6)
7. Encode evidence arc in `evidence_arc:` YAML field (Step 7)
8. Assemble `program.yaml` with required schema (Step 8)
9. Run per-stage compliance table across three criterion ladders (Step 9)
10. Run terminal validation checklist (Step 10)

---

#### Step 1 — Topic

State the topic name. All artifact names, phase labels, and gate conditions must be coherent with this topic.

---

#### Step 2 — Declare Evidence Arc Phases

**Do not open the catalog yet. Catalog consultation is forbidden at this step.**

Declare the evidence arc as a sequence of named phase boundaries. Think about what the team needs to learn at each stage of the investigation — not which skills to run.

Name 3–6 phases forming a deliberate evidence-building arc. Phase names must encode strategic purpose, not skill content:
- PASS: `discovery`, `de-risk`, `depth`, `synthesis`, `monitoring`
- FAIL: `scout_phase`, `prove_stage`, `skills_cluster_1`

For each phase, state the investigative question it is designed to answer. Questions must be genuine interrogatives ending with `?`.

| Phase label | Investigative question (must end with `?`) |
|-------------|---------------------------------------------|
| [phase 1]   | [e.g., "Do we understand the problem space well enough to commit?"] |
| [phase 2]   | [...] |
| ...         | ... |

This phase map is the structural skeleton. Subsequent steps fill this skeleton — they do not redesign it.

---

#### Step 3 — Select Skills from Catalog

Now consult the catalog above. Select skills relevant to the topic. Record your selection grouped by namespace. For each skill, note the phase from Step 2 it belongs to.

---

#### Step 4 — Assign Skills to Declared Phases

Map each selected skill to a phase from Step 2. Do not create new phases at this step. If a skill cannot be assigned to any declared phase, discard it or return to Step 2.

---

#### Step 5 — Design Gates

For each non-echo phase, write a gate condition. Requirements:
- Reference specific artifact types or signal counts
- At least one gate must include a numeric threshold (`>= N`)

**Gate quantification format** (dedicated C-09 enforcement):
- PASS: `>= 3 scout-namespace artifacts present and draft:spec artifact exists`
- FAIL: `team is ready to proceed`
- FAIL: `adequate signals gathered`

**Traceability check** (C-11 enforcement):
For every gate artifact named, confirm a skill in the same stage produces that artifact type.
- FORWARD REFERENCE (fail): gate requires `trace:contract artifact` from a stage containing only `scout:` skills
- VALID: gate requires `scout:feasibility artifact` from a stage containing `scout:feasibility`

---

#### Step 6 — Phase Intent Questions

Each non-echo phase must carry the investigative question from Step 2. Questions must:
- Be genuine interrogatives ending with `?`
- Be phase-specific (not applicable to all phases equally)

**Interrogative form enforcement** (C-17):
- PASS: `"Do we have enough validated evidence to commit to building this?"`
- NOT A QUESTION (fail): `"Validate the evidence baseline"`
- NOT A QUESTION (fail): `"Evidence validation completed"`

---

#### Step 7 — Evidence Arc Field

Encode the evidence arc as a required top-level YAML field:

```yaml
evidence_arc:
  breadth:   [phase labels running scout + draft skills]
  depth:     [phase labels running prove + review + flow + trace skills]
  synthesis: [phase labels running listen + metrics + goals skills]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 — Assemble YAML

Required output schema:

```yaml
topic: <topic-name>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    phase: <arc-key>          # must match a key defined in evidence_arc
    intent: "<question ending with ?>"
    skills:
      - <namespace>:<skill>
    gate: "<artifact-grounded condition; at least one quantified with >=N>"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage MUST include a `phase:` field whose value matches one of the arc keys in `evidence_arc:`.

FAIL:
```yaml
- name: de-risk
  skills: [draft:spec]
  gate: ">= 1 draft:spec artifact present"
```
(Missing `phase:` — C-18 violation)

PASS:
```yaml
- name: de-risk
  phase: depth
  intent: "Does our spec hold up under expert scrutiny?"
  skills: [draft:spec]
  gate: ">= 1 draft:spec artifact present"
```

**Two-criteria enforcement block: arc-phase field × gate quantification** (C-19 — crossing arc-structure and gate-behavior ladders):

| Check | Criterion | Fail signal | Pass format |
|-------|-----------|-------------|-------------|
| `phase:` value in `evidence_arc` keys | C-18 (arc-structure) | `phase: stage_two` where `stage_two` ∉ evidence_arc | `phase: depth` where `depth` ∈ evidence_arc |
| Gate has numeric threshold | C-09 (gate-behavior) | `gate: "evidence looks sufficient"` | `gate: ">= 2 scout artifacts present"` |

Both conditions must hold for every non-echo stage.

---

#### Step 9 — Per-Stage Compliance Table

Run this table after YAML assembly. One row per non-echo stage. Three columns, one from each criterion ladder:

| Stage | arc-structure: `phase:` maps to arc key? (C-18) | gate-behavior: gate has `>=N` threshold? (C-09) | question-framing: `intent:` ends with `?` (C-17) |
|-------|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ... | ... | ... | ... |

Any NO requires revision before Step 10.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: stages array present; YAML parses without error
[ ] C-02: last stage is echo with auto: true; no skills field; no gate field
[ ] C-03: all skills in catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace layers ordered: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: stages are coherent phases, not one-skill-per-stage or all-in-one
[ ] C-07: gates reference specific artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate has a numeric threshold (>= N)
[ ] C-10: every non-echo stage has a phase name encoding strategic purpose
[ ] C-11: every gate artifact traceable to a skill in the same stage
[ ] C-12: every phase carries a distinct investigative question
[ ] C-13: gate quantification (Step 5) and gate traceability (Step 5) each have dedicated format examples
[ ] C-14: this checklist spans essential + recommended + aspirational tiers
[ ] C-15: each checklist item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level YAML field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-18 (arc-structure) x C-09 (gate-behavior)
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 table columns span arc-structure (C-18) + gate-behavior (C-09) + question-framing (C-17)
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section before Step 1
```

---

## V-02 — Three-Ladder Table Focus

**Axis**: Output format — the per-stage compliance table is the structural center of the prompt. Column headers name the criterion ladders in full (Arc-Structure Ladder / Gate-Behavior Ladder / Question-Framing Ladder) so 3-ladder coverage is self-documenting. The CONSTRUCTION ORDER block and catalog prohibition are present but briefer.

**Hypothesis**: Labeling table columns by ladder name rather than criterion ID (V-01) makes the 3-ladder requirement legible without cross-referencing the rubric (C-24). The C-19 pair shifts to C-16 × C-17 (arc schema × interrogative form) to cover a different ladder combination.

**C-19 pair**: C-16 (arc-structure ladder) × C-17 (question-framing ladder).

**Anticipated score**: 180 / 180

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a sequencing plan, not an executor.

---

**Valid Signal Plugin Skill Catalog**

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage `skills` list.

---

## CONSTRUCTION ORDER

Complete each step in sequence. Do not skip, reorder, or combine steps.

1. Topic declaration (Step 1)
2. Arc phase declaration — **catalog closed until Step 3** (Step 2)
3. Skill selection from catalog (Step 3)
4. Skill-to-phase assignment (Step 4)
5. Gate design: artifact-grounded, quantified (Step 5)
6. Per-phase investigative questions: interrogative form required (Step 6)
7. `evidence_arc:` YAML field encoding (Step 7)
8. YAML assembly with `phase:` tags (Step 8)
9. Per-stage compliance table — three ladders (Step 9)
10. Terminal validation checklist (Step 10)

---

#### Step 1 — Topic

State the topic name.

---

#### Step 2 — Declare Arc Phases

**Catalog is off-limits at this step. Do not consult the skill list until Step 3.**

Name 3–6 phases that form a coherent evidence-building arc. Phase names encode strategic purpose:
- PASS: `discovery`, `validation`, `depth-simulation`, `synthesis`
- FAIL: `prove_skills`, `scout_and_draft`, `stage_2`

For each phase, write the investigative question it is designed to answer (genuine interrogative, ends with `?`):

| Phase | Investigative question |
|-------|------------------------|
| [name] | [...?] |

---

#### Step 3 — Select Skills

Consult the catalog. Select skills for the topic, grouped by namespace. Note the assigned phase for each.

---

#### Step 4 — Assign Skills to Phases

Map each selected skill to its declared phase from Step 2. Do not introduce new phases.

---

#### Step 5 — Design Gates

Each non-echo phase gate must:
- Name specific artifact types or signal counts
- At least one gate: include a numeric threshold (`>= N`)

Gate format enforcement (C-09):
- PASS: `>= 2 scout-namespace artifacts present`
- FAIL: `team ready`

Traceability check (C-11): every gate artifact must be producible by a skill in the same stage.

---

#### Step 6 — Phase Intent Questions

Assign investigative questions to phases. Each question must end with `?`. A statement is not a question:
- PASS: `"Do we understand the failure modes well enough to spec mitigations?"`
- NOT A QUESTION (fail): `"Understand the failure modes"`

---

#### Step 7 — Evidence Arc Field

Required top-level YAML field:

```yaml
evidence_arc:
  breadth:   [phases running scout + draft skills]
  depth:     [phases running prove + review + flow + trace skills]
  synthesis: [phases running listen + metrics + goals skills]
```

---

#### Step 8 — Assemble YAML

Schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    phase: <arc-key>
    intent: "<question?>"
    skills:
      - <namespace>:<skill>
    gate: "<artifact-grounded condition>"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage must include `phase:` whose value is a key defined in `evidence_arc:`.

FAIL:
```yaml
- name: synthesis
  skills: [listen:feedback]
  gate: ">= 1 listen:feedback artifact"
```

PASS:
```yaml
- name: synthesis
  phase: synthesis
  intent: "Are users adopting the feature as designed?"
  skills: [listen:feedback]
  gate: ">= 1 listen:feedback artifact"
```

**Two-criteria enforcement block: arc schema field × interrogative form** (C-19 — crossing arc-structure and question-framing ladders):

| Check | Criterion | Fail signal | Pass format |
|-------|-----------|-------------|-------------|
| `evidence_arc:` required at top level | C-16 (arc-structure) | field absent or optional | `evidence_arc:` present with breadth/depth/synthesis keys |
| `intent:` ends with `?` | C-17 (question-framing) | `intent: "Build the spec"` | `intent: "Does the spec capture all constraints?"` |

---

#### Step 9 — Per-Stage Compliance Table

One row per non-echo stage. Column headers name each criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to arc key? (C-18) | Gate-Behavior Ladder: gate has `>=N` threshold? (C-09) | Question-Framing Ladder: `intent:` ends with `?` (C-17) |
|-------|--------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ... | ... | ... | ... |

Three ladders represented. Any NO is a revision trigger.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: valid YAML, stages array present
[ ] C-02: echo stage last; auto: true; no skills; no gate
[ ] C-03: all skills from catalog; no hallucinated names
[ ] C-04: every non-echo stage gate is non-trivial
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gates name specific artifact types or signal counts
[ ] C-08: arc structure: breadth -> depth -> synthesis
[ ] C-09: at least one gate quantified with >= N threshold
[ ] C-10: stage names encode strategic purpose, not skill clusters
[ ] C-11: every gate artifact traceable to a skill in the same stage
[ ] C-12: every phase carries a phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification (Step 5) and traceability (Step 5)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID
[ ] C-16: evidence_arc: present as required top-level field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-16 (arc-structure) x C-17 (question-framing)
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition
[ ] C-24: Step 9 table columns span Arc-Structure + Gate-Behavior + Question-Framing ladders
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section
```

---

## V-03 — Phase-Boundary Ritual

**Axis**: Lifecycle emphasis — the phase-declaration step receives maximum structural weight. Catalog access is framed as a contamination risk to phase purity. The phase-boundary moment is treated as an architectural commitment, not a planning convenience.

**Hypothesis**: Framing catalog consultation as a contamination threat (not just a sequence constraint) amplifies the C-23 prohibition effect. Combining this with a CONSTRUCTION ORDER block (C-25) and 3-ladder table (C-24) produces the strongest arc-integrity variant. The C-19 pair shifts to C-20 × C-12 to test arc-structure × question-framing coverage at a different criterion pair.

**C-19 pair**: C-20 (arc-structure ladder) × C-12 (question-framing ladder).

**Anticipated score**: 180 / 180

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a plan.

The arc — not the skill list — is the load-bearing structure of this program. Phase boundaries must be declared from first principles before the catalog is consulted. Consulting the catalog before phase declaration contaminates the arc with skill availability bias: you stop asking "what does the team need to learn?" and start asking "what skills are available?" These are different questions with different answers. The phase-declaration step is the architectural commitment that makes everything else coherent.

---

**Valid Signal Plugin Skill Catalog**

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage `skills` list.

---

## CONSTRUCTION ORDER

This is the required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases — **the catalog must remain closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5. Design gates: artifact-grounded, at least one quantified (Step 5)
6. Write per-phase questions: interrogative form mandatory (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 — Topic

State the topic name. All subsequent work is constrained to this topic.

---

#### Step 2 — Declare Arc Phases

**The catalog must remain closed at this step. Opening the catalog before phase declaration is complete contaminates the arc with skill availability bias. Do not do it.**

Declare 3–6 phase boundaries from first principles. These are not skill containers — they are investigative milestones. Ask: what does the team need to believe, confirm, or rule out before advancing?

Phase names encode investigative purpose, not skill content:
- PASS: `discovery` (are we solving the right problem?), `stress-test` (does our design survive adversarial conditions?), `signal-watch` (are users adopting as expected?)
- FAIL: `scout_block`, `flow_and_trace_stage`, `all_prove_skills`

For each phase, the investigative question it answers (genuine interrogative, ends with `?`):

| Phase label | Investigative question |
|-------------|------------------------|
| [name] | [...?] |

The phase map is locked after this step. Subsequent steps select skills and gates to fill it — they do not redesign the arc.

---

#### Step 3 — Select Skills

Now open the catalog. Select skills relevant to the topic, grouped by namespace. Note the phase from Step 2 each skill belongs to.

---

#### Step 4 — Assign Skills to Phases

Map each skill to its Step 2 phase. Do not create new phases. Discard skills with no matching phase.

---

#### Step 5 — Design Gates

Each non-echo phase gate must reference specific artifact types or signal counts. At least one gate must be quantified (`>= N`).

**Gate quantification enforcement** (C-09):
- PASS: `>= 3 scout artifacts present and draft:spec artifact exists`
- FAIL: `team agrees to proceed`
- FAIL: `sufficient evidence`

**Traceability enforcement** (C-11): every artifact named in a gate must be producible by a skill in the same stage. Flag any forward reference and fix it.

---

#### Step 6 — Phase Intent Questions

Questions from Step 2 become `intent:` fields in YAML. Each must:
- End with `?`
- Be phase-specific (not applicable across all phases)

**Interrogative form requirement** (C-17):
- PASS: `"Does this design hold up when we stress-test its failure modes?"`
- NOT A QUESTION (fail): `"Stress-test the design"`

---

#### Step 7 — Evidence Arc Field

Encode the arc as a required top-level field:

```yaml
evidence_arc:
  breadth:   [scout + draft phase labels]
  depth:     [prove + review + flow + trace phase labels]
  synthesis: [listen + metrics + goals phase labels]
```

---

#### Step 8 — Assemble YAML

Required schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    phase: <arc-key>
    intent: "<question ending with ?>"
    skills:
      - <namespace>:<skill>
    gate: "<condition with artifact reference>"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

The `phase:` field is mandatory in every non-echo stage. Its value must match a key defined in `evidence_arc:`. A stage without `phase:` is structurally incomplete regardless of its gate or skill content.

FAIL (phase: missing):
```yaml
- name: discovery
  intent: "Do we understand the problem?"
  skills: [scout:feasibility]
  gate: ">= 2 scout artifacts"
```

PASS:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the problem well enough to commit?"
  skills: [scout:feasibility]
  gate: ">= 2 scout artifacts"
```

**Two-criteria enforcement block: phase declaration before catalog × per-phase questions** (C-19 — crossing arc-structure and question-framing ladders):

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared in Step 2 before catalog opened in Step 3 | C-20 (arc-structure) | Phase names derived from catalog scan rather than investigative intent | Phase map complete and locked before Step 3 begins |
| Every phase carries a phase-specific investigative question | C-12 (question-framing) | Generic question "are we ready?" applied to all phases | Each phase has a distinct question answerable only by running that phase's skills |

---

#### Step 9 — Per-Stage Compliance Table

Run after YAML assembly. One row per non-echo stage. Three columns, one per criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to `evidence_arc` key? (C-18) | Gate-Behavior Ladder: gate contains numeric threshold? (C-09) | Question-Framing Ladder: `intent:` is a genuine interrogative ending with `?` (C-17) |
|-------|-------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ... | ... | ... | ... |

Any NO triggers revision.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: YAML valid; stages array present
[ ] C-02: echo is last; auto: true; no skills; no gate
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage gate is non-trivial
[ ] C-05: namespace ordering respected across stages
[ ] C-06: coherent stage groupings
[ ] C-07: gate language references artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate with numeric threshold
[ ] C-10: stage names encode strategic purpose
[ ] C-11: every gate artifact traceable to same-stage skill
[ ] C-12: every phase has a phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification and gate traceability (Step 5)
[ ] C-14: checklist covers criteria from essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-20 (arc-structure) x C-12 (question-framing)
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language ("catalog must remain closed")
[ ] C-24: Step 9 table spans Arc-Structure + Gate-Behavior + Question-Framing ladders
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section
```

---

## V-04 — CONSTRUCTION ORDER Block + Ladder-Named Table (V-01 + V-02 Combined)

**Axis**: Combines V-01 (CONSTRUCTION ORDER protocol-first with enumerated steps) and V-02 (table columns labeled by ladder name in title case). The CONSTRUCTION ORDER block matches V-01 in structure; the per-stage compliance table uses V-02's ladder-name column headers. This tests whether combining the two strongest single-axis variants produces ceiling performance.

**Hypothesis**: V-01's CONSTRUCTION ORDER block makes the prohibition structural; V-02's ladder-named columns make 3-ladder coverage self-auditing. Their combination eliminates the risk that either feature fails by isolation — both reinforce the same evidence-first discipline from different angles.

**C-19 pair**: C-18 (arc-structure ladder) × C-17 (question-framing ladder).

**Anticipated score**: 180 / 180

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a sequencing plan, not an executor.

---

**Valid Signal Plugin Skill Catalog**

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Only skills from this catalog may appear in any stage `skills` list.

---

## CONSTRUCTION ORDER

Read the full construction sequence before beginning Step 1. Execute in order — do not skip, combine, or reorder steps.

1. State the topic (Step 1)
2. Declare arc phases — **catalog is off-limits until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5. Design artifact-grounded, quantified gates (Step 5)
6. Write per-phase investigative questions in interrogative form (Step 6)
7. Encode `evidence_arc:` YAML field (Step 7)
8. Assemble `program.yaml` with `phase:` field per stage (Step 8)
9. Run per-stage compliance table: Arc-Structure / Gate-Behavior / Question-Framing (Step 9)
10. Run terminal validation checklist (Step 10)

---

#### Step 1 — Topic

State the topic name.

---

#### Step 2 — Declare Arc Phases

**Do not open the catalog yet. Catalog consultation is forbidden at this step.**

Declare 3–6 phases as investigative milestones. Phase names encode strategic purpose, not skill content:
- PASS: `discovery`, `de-risk`, `depth`, `synthesis`
- FAIL: `scout_stage`, `prove_block`

For each phase, write the investigative question it is designed to answer (genuine interrogative, ends with `?`):

| Phase | Investigative question (ends with `?`) |
|-------|----------------------------------------|
| [name] | [question?] |

Phase map locks after this step.

---

#### Step 3 — Select Skills

Consult the catalog. Select relevant skills grouped by namespace. Note each skill's phase from Step 2.

---

#### Step 4 — Assign Skills

Map each selected skill to its declared phase. Do not introduce new phases.

---

#### Step 5 — Design Gates

Each non-echo gate must:
- Name artifact types or signal counts
- At least one gate: numeric threshold (`>= N`)

**Gate quantification format** (C-09):
- PASS: `>= 3 scout artifacts present`
- FAIL: `seems complete`

**Traceability check** (C-11): every gate artifact must be producible by a skill in the same stage.

---

#### Step 6 — Phase Intent Questions

Questions from Step 2 become `intent:` values. Each must end with `?` and be phase-specific.

**Interrogative form** (C-17):
- PASS: `"Do we have enough signal to commit to this design?"`
- NOT A QUESTION (fail): `"Evaluate the design signal"`

---

#### Step 7 — Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [scout + draft phase labels]
  depth:     [prove + review + flow + trace phase labels]
  synthesis: [listen + metrics + goals phase labels]
```

---

#### Step 8 — Assemble YAML

Required schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    phase: <arc-key>
    intent: "<question?>"
    skills:
      - <namespace>:<skill>
    gate: "<artifact-grounded condition>"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage must include `phase:` mapping to an `evidence_arc:` key.

FAIL (missing phase field):
```yaml
- name: validation
  skills: [review:design]
  gate: ">= 1 review:design artifact"
```

PASS:
```yaml
- name: validation
  phase: depth
  intent: "Does the design withstand expert review?"
  skills: [review:design]
  gate: ">= 1 review:design artifact"
```

**Two-criteria enforcement block: arc phase field × interrogative form** (C-19 — crossing arc-structure and question-framing ladders):

| Check | Criterion | Fail signal | Pass format |
|-------|-----------|-------------|-------------|
| `phase:` matches `evidence_arc` key | C-18 (Arc-Structure Ladder) | phase value not in arc keys | `phase: depth` where `depth` ∈ evidence_arc |
| `intent:` is an interrogative | C-17 (Question-Framing Ladder) | `intent: "Design validation"` | `intent: "Does the design hold up?"` |

---

#### Step 9 — Per-Stage Compliance Table

One row per non-echo stage. Column headers name the criterion ladders:

| Stage | Arc-Structure Ladder: `phase:` maps to arc key? (C-18) | Gate-Behavior Ladder: gate has `>=N` threshold? (C-09) | Question-Framing Ladder: `intent:` ends with `?` (C-17) |
|-------|--------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ... | ... | ... | ... |

All columns named by ladder. Any NO requires revision.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: valid YAML; stages array present
[ ] C-02: echo last; auto: true; no skills; no gate
[ ] C-03: all skills from catalog
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings
[ ] C-07: gates reference artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate with numeric threshold
[ ] C-10: stage names encode strategic purpose
[ ] C-11: every gate artifact traceable to same-stage skill
[ ] C-12: every phase has a distinct investigative question
[ ] C-13: dedicated examples for gate quantification and gate traceability (Step 5)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID
[ ] C-16: evidence_arc: present as required top-level field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-18 (arc-structure) x C-17 (question-framing)
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 columns span Arc-Structure + Gate-Behavior + Question-Framing ladders
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section
```

---

## V-05 — All Three Axes, Terse Imperative Register

**Axis**: Terse imperative register — all three new criteria are present (C-23, C-24, C-25) but every instruction is stated in the minimum words needed. Short sentences. Bullets over prose. Format examples remain but descriptive framing is cut. This tests whether criterion coverage degrades under information-density pressure.

**Hypothesis**: A terse prompt with all three new criteria retains the same ceiling score as the verbose variants (V-01–V-04). If it degrades, the degradation localizes to criteria that require contextual framing — a signal for which criteria depend on verbal scaffolding vs. structural placement.

**C-19 pair**: C-20 (arc-structure ladder) × C-09 (gate-behavior ladder).

**Anticipated score**: 180 / 180

---

### FULL PROMPT BODY

Produce a `program.yaml` for the Signal plugin. Sequences skills into staged phases with gates. Plan only — not an executor.

---

**Signal Plugin Skill Catalog**

```
scout:    competitors, feasibility, naming, compliance, market, stakeholders, positioning, requirements
draft:    spec, proposal, pitch
review:   design, code, users, customers
flow:     lifecycle, conversation, trigger, dataflow, integration, throttle, resilience
trace:    request, state, contract, component, deployment, migration, permissions
prove:    hypothesis, websearch, intelligence, prototype, analysis, interview, synthesize, publish
listen:   feedback, support, adoption
program:  plan
metrics:  nps, nsat, adoption, sla, dashboard
goals:    okr, sla, commit, pr, msr, xr
```

Catalog skills only. No invented names.

---

## CONSTRUCTION ORDER

All steps in sequence. No skips. No reordering.

1. Topic (Step 1)
2. Arc phases — **catalog off-limits until Step 3** (Step 2)
3. Skill selection (Step 3)
4. Skill assignment to phases (Step 4)
5. Gates: artifact-grounded, quantified (Step 5)
6. Per-phase questions: interrogative form (Step 6)
7. `evidence_arc:` field (Step 7)
8. YAML assembly with `phase:` per stage (Step 8)
9. Compliance table: 3 ladders (Step 9)
10. Checklist (Step 10)

---

#### Step 1 — Topic

State the topic name.

---

#### Step 2 — Arc Phases

**Catalog is forbidden at this step. Do not open it.**

Name 3–6 phases. Names encode purpose, not skills.
- PASS: `discovery`, `de-risk`, `depth`, `synthesis`
- FAIL: `scout_phase`, `prove_stage`

Each phase: one investigative question ending with `?`.

| Phase | Question (must end `?`) |
|-------|--------------------------|
| [name] | [question?] |

Phase map locked after this step.

---

#### Step 3 — Skills

Consult catalog. Select relevant skills. Note phase assignment for each.

---

#### Step 4 — Assignment

Map skills to phases from Step 2. No new phases.

---

#### Step 5 — Gates

Each non-echo gate:
- Name specific artifact types or signal counts
- At least one gate: `>= N` threshold

**Gate quantification** (C-09):
- PASS: `>= 2 scout artifacts present`
- FAIL: `complete enough`

**Traceability** (C-11): gate artifact must be producible by same-stage skill. Flag forward references.

---

#### Step 6 — Questions

Each phase: `intent:` ends with `?`. Phase-specific only.

**Form** (C-17):
- PASS: `"Do we have the signal needed to commit?"`
- FAIL: `"Evaluate the signal"`

---

#### Step 7 — Arc Field

```yaml
evidence_arc:
  breadth:   [scout + draft phases]
  depth:     [prove + review + flow + trace phases]
  synthesis: [listen + metrics + goals phases]
```

---

#### Step 8 — YAML

Schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase>
    phase: <arc-key>
    intent: "<question?>"
    skills:
      - <ns>:<skill>
    gate: "<condition>"
  - ...
  - name: echo
    auto: true
```

**C-18 enforcement — `phase:` field** (standalone block):

Every non-echo stage: `phase:` required. Value must be a key in `evidence_arc:`.

FAIL:
```yaml
- name: depth
  skills: [prove:prototype]
  gate: ">= 1 prototype"
```

PASS:
```yaml
- name: depth
  phase: depth
  intent: "Does the prototype validate our architecture?"
  skills: [prove:prototype]
  gate: ">= 1 prototype artifact"
```

**Two-criteria block: phase-first order × gate quantification** (C-19 — arc-structure × gate-behavior ladders):

| Check | Criterion | Fail | Pass |
|-------|-----------|------|------|
| Phase declaration (Step 2) before catalog (Step 3) | C-20 (arc-structure) | phases named by scanning catalog | phases named from investigative intent before catalog opens |
| Gate has `>= N` threshold | C-09 (gate-behavior) | `gate: "looks good"` | `gate: ">= 2 artifacts"` |

---

#### Step 9 — Compliance Table

One row per non-echo stage. Three columns, one per ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to arc key? (C-18) | Gate-Behavior Ladder: gate has `>=N`? (C-09) | Question-Framing Ladder: `intent:` ends `?`? (C-17) |
|-------|--------------------------------------------------------|----------------------------------------------|------------------------------------------------------|
| [s1] | Y/N | Y/N | Y/N |
| [s2] | Y/N | Y/N | Y/N |
| ... | ... | ... | ... |

Any N: revise before Step 10.

---

#### Step 10 — Checklist

```
[ ] C-01: valid YAML; stages array present
[ ] C-02: echo last; auto: true; no skills; no gate
[ ] C-03: catalog skills only
[ ] C-04: every non-echo gate is non-trivial
[ ] C-05: namespace order: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings
[ ] C-07: gates name artifact types or signal counts
[ ] C-08: arc: breadth -> depth -> synthesis
[ ] C-09: >= 1 gate has numeric threshold
[ ] C-10: stage names encode strategic purpose
[ ] C-11: gate artifacts traceable to same-stage skills
[ ] C-12: every phase has a distinct interrogative question
[ ] C-13: dedicated examples for gate quantification and traceability (Step 5)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID
[ ] C-16: evidence_arc: required top-level field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field in evidence_arc keys
[ ] C-19: Step 8 block covers C-20 (arc-structure) x C-09 (gate-behavior)
[ ] C-20: Step 2 (phase declaration) before Step 3 (catalog)
[ ] C-21: per-stage compliance table with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement in Step 8 (standalone, fail/pass pair)
[ ] C-23: Step 2 contains catalog prohibition ("catalog is forbidden")
[ ] C-24: Step 9 columns span Arc-Structure + Gate-Behavior + Question-Framing ladders
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section
```

---

## R7 Anticipated Calibration (v7 rubric, 2026-03-15)

| Variant | C-23 | C-24 | C-25 | v7 Composite | v7 Golden |
|---------|------|------|------|--------------|-----------|
| V-01 — Construction Protocol-First | P | P | P | 180 / 180 | YES |
| V-02 — Three-Ladder Table Focus | P | P | P | 180 / 180 | YES |
| V-03 — Phase-Boundary Ritual | P | P | P | 180 / 180 | YES |
| V-04 — V-01 + V-02 Combined | P | P | P | 180 / 180 | YES |
| V-05 — All Three Axes, Terse Register | P | P | P | 180 / 180 | YES |

P = pass (5 pts). All five variants target 180 / 180 — the first round achieving a three-way simultaneous pass of the new criteria.

**C-23 notes** (R7 confirmation):
- V-01: "Catalog consultation is forbidden at this step" in Step 2 body — PASS
- V-02: "Catalog is off-limits at this step. Do not consult the skill list until Step 3" — PASS
- V-03: "The catalog must remain closed at this step" with contamination framing — PASS
- V-04: "Catalog consultation is forbidden at this step" — PASS
- V-05: "Catalog is forbidden at this step. Do not open it." — PASS

**C-24 notes** (R7 confirmation):
- V-01: Step 9 columns mapped to C-18 (arc-structure), C-09 (gate-behavior), C-17 (question-framing) — three ladders — PASS
- V-02: Step 9 columns labeled "Arc-Structure Ladder (C-18) / Gate-Behavior Ladder (C-09) / Question-Framing Ladder (C-17)" — three ladders — PASS
- V-03: Step 9 columns labeled by full ladder names — three ladders — PASS
- V-04: Step 9 columns labeled "Arc-Structure Ladder (C-18) / Gate-Behavior Ladder (C-09) / Question-Framing Ladder (C-17)" — three ladders — PASS
- V-05: Step 9 columns labeled "Arc-Structure Ladder (C-18) / Gate-Behavior Ladder (C-09) / Question-Framing Ladder (C-17)" — three ladders — PASS

**C-25 notes** (R7 confirmation):
- V-01: "## CONSTRUCTION ORDER" labeled section enumerates all 10 steps before Step 1 body — PASS
- V-02: "## CONSTRUCTION ORDER" block present as labeled section — PASS
- V-03: "## CONSTRUCTION ORDER" block with preamble "Read all steps before beginning Step 1" — PASS
- V-04: "## CONSTRUCTION ORDER" block with "Execute in order" — PASS
- V-05: "## CONSTRUCTION ORDER" block (terse) enumerating all 10 steps — PASS

**R7 spread**: V-01 = V-02 = V-03 = V-04 = V-05 = 180 / 180.
First round achieving full ceiling on all criteria. All five variants golden.
New golden references: all five (180 / 180 unanimous).
