# program-plan — R8 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v8 (C-01 through C-29, 200 pts, golden >= 160).

R7 golden reference: V-03 (Phase-Boundary Ritual) = 197.5 / 200.
R7 deficit: C-13 partial (2.5 pts) — C-09 gets dedicated format example; C-11 has prose only.
R8 target: 200 / 200 — close C-13 to full by isolating C-11 into its own dedicated step.

Variation axes:
- V-01 (single axis): C-11 isolation — dedicated Gate Traceability Audit step with FORWARD REFERENCE bad/good YAML pair
- V-02 (single axis): Gate lineage prefix format — embed traceability into gate string format, making C-11 violations structurally impossible
- V-03 (single axis): Inertia framing — open with a named status-quo competitor (skill-list-driven programs) and arc-first rebuttal
- V-04 (combined): V-01 + V-02 (C-11 isolation + lineage prefix)
- V-05 (combined): V-01 + V-02 + V-03 (all three axes)

R7 calibration retained: see program-plan-rubric-v8-2026-03-15.md.

---

## V-01 — C-11 Dedicated Traceability Step

**Axis**: C-11 isolation — the Gate Traceability Audit is extracted from Step 5 into its own labeled subsection (Step 5b) with a dedicated bad/good YAML pair showing a FORWARD REFERENCE violation and its fix. C-09 and C-11 enforcement are now two distinct isolated blocks.

**Hypothesis**: V-03 R7's C-13 partial credit was caused by C-11 having enforcement prose ("flag any forward reference and fix it") but no dedicated format example. C-13 requires that both C-09 and C-11 each have a dedicated numbered step or labeled section with a concrete before/after example. Isolating C-11 into Step 5b closes C-13 from 2.5 pts to 5 pts. All other R7 V-03 elements are retained (C-26/C-27/C-28/C-29 pass unchanged). Anticipated score: 200 / 200.

**C-19 pair**: C-20 (arc-structure/construction-protocol) × C-12 (question-framing).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a plan, not an executor. Your job is to produce a program that a team could follow as a sequenced evidence-building arc from discovery through synthesis.

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

Only skills from this catalog may appear in any stage `skills` list. Do not invent, abbreviate, or namespace-expand skill names beyond what is shown.

---

## CONSTRUCTION ORDER

This is the required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases — **the catalog must remain closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: artifact-grounded, at least one quantified (Step 5a)
5b. Gate traceability audit: forward references prohibited (Step 5b)
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
| [name]      | [...?]                 |

The phase map is locked after this step. Subsequent steps select skills and gates to fill it — they do not redesign the arc.

---

#### Step 3 — Select Skills

Now open the catalog. Select skills relevant to the topic, grouped by namespace. Note the phase from Step 2 each skill belongs to.

---

#### Step 4 — Assign Skills to Phases

Map each skill to its Step 2 phase. Do not create new phases. Discard skills with no matching phase.

---

#### Step 5a — Design Gates (Quantification)

Each non-echo phase gate must reference specific artifact types or signal counts. At least one gate must be quantified (`>= N`).

**Gate quantification enforcement** (C-09):
- PASS: `>= 3 scout artifacts present and draft:spec artifact exists`
- FAIL: `team agrees to proceed`
- FAIL: `sufficient evidence gathered`

---

#### Step 5b — Gate Traceability Audit (FORWARD REFERENCE CHECK)

Every artifact named in a gate must be producible by a skill in the same stage. A gate that references an artifact type that no skill in the current stage can produce is a FORWARD REFERENCE — it is a structural error and must be fixed before continuing.

**Traceability enforcement** (C-11):

FORWARD REFERENCE (fail) — gate requires `trace:deployment artifact` but stage contains only `scout:` skills:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the problem space?"
  skills:
    - scout:feasibility
    - scout:market
  gate: ">= 1 trace:deployment artifact present"
```

VALID — gate requires `scout:feasibility artifact` from a stage that contains `scout:feasibility`:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the problem space well enough to commit?"
  skills:
    - scout:feasibility
    - scout:market
  gate: ">= 2 scout-namespace artifacts present and scout:feasibility complete"
```

For each non-echo stage: confirm every gate artifact is producible by at least one skill in that same stage's `skills` array. Flag and fix any forward reference before proceeding to Step 6.

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

Every phase from Step 2 must appear in exactly one arc key.

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
    gate: "<artifact-grounded condition>"
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

**Two-criteria enforcement block: phase declaration before catalog × per-phase investigative questions** (C-19 — crossing arc-structure/construction-protocol and question-framing ladders):

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared in Step 2 before catalog opened in Step 3 | C-20 (arc-structure/construction-protocol) | Phase names derived from catalog scan rather than investigative intent — arc phases reflect skill cluster availability, not learning goals | Phase map complete and locked in Step 2; catalog not consulted until Step 3 begins |
| Every phase carries a phase-specific investigative question ending with `?` | C-12 (question-framing) | Generic question "are we ready to proceed?" applied across all phases — not answerable by running any single phase's skills specifically | Each phase has a distinct question answerable only by running that phase's skills (e.g., "Do we understand the failure modes well enough to spec mitigations?") |

Both conditions must hold for every non-echo stage before YAML output is produced.

---

#### Step 9 — Per-Stage Compliance Table

Run after YAML assembly. One row per non-echo stage. Three columns, one per criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to `evidence_arc` key? (C-18) | Gate-Behavior Ladder: gate contains numeric threshold? (C-09) | Question-Framing Ladder: `intent:` is a genuine interrogative ending with `?` (C-17) |
|-------|-------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ...       | ...      | ...      | ...      |

Any NO triggers revision before proceeding to Step 10.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; no skills field; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering respected: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gate language references artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate with numeric threshold (>= N)
[ ] C-10: stage names encode strategic purpose, not skill clusters
[ ] C-11: every gate artifact traceable to a skill in the same stage (Step 5b audit complete)
[ ] C-12: every phase has a phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification (Step 5a) AND gate traceability (Step 5b, FORWARD REFERENCE pair)
[ ] C-14: this checklist spans essential + recommended + aspirational tiers
[ ] C-15: each checklist item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level YAML field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-20 (arc-structure) x C-12 (question-framing), four-column decomposition
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 table spans Arc-Structure Ladder (C-18) + Gate-Behavior Ladder (C-09) + Question-Framing Ladder (C-17)
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section before Step 1
[ ] C-26: Step 2 catalog prohibition names failure mechanism (skill availability bias contaminates arc)
[ ] C-27: Step 9 column headers name ladder family with criterion ID (e.g., "Arc-Structure Ladder (C-18)")
[ ] C-28: Step 8 C-19 block uses four-column decomposition (Constraint/Criterion/Violation/Compliance)
[ ] C-29: CONSTRUCTION ORDER block contains meta-execution directive ("Read all steps before beginning Step 1")
```

---

## V-02 — Gate Lineage Prefix Format

**Axis**: Output format — gate strings must include a lineage prefix that names the producing skill and stage before the threshold condition. Format: `[<namespace>:<skill> in <stage-name> produces <artifact-type>] >= N <artifact-type> present`. This embeds C-11 traceability into the gate format itself, making forward references structurally impossible to write without noticing them.

**Hypothesis**: V-03 R7's C-11 was prose-only ("flag any forward reference and fix it") with no format example. V-02 converts C-11 traceability from a post-hoc audit into a gate-format requirement. A builder writing `[trace:deployment in discovery produces deployment-manifest]` when the discovery stage contains only `scout:` skills will immediately see the contradiction. This gives C-11 a dedicated format example embedded in the gate design step, closing C-13 to full.

**C-19 pair**: C-18 (arc-structure/construction-protocol) × C-09 (gate-behavior).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a plan, not an executor. Your job is to produce a program that a team could follow as a sequenced evidence-building arc.

The arc — not the skill list — is the load-bearing structure of this program. Phase boundaries must be declared from first principles before the catalog is consulted. Consulting the catalog before phase declaration contaminates the arc with skill availability bias: you stop asking "what does the team need to learn?" and start asking "what skills are available?" These are different questions with different answers.

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
5. Design gates: artifact-grounded with lineage prefix format (Step 5)
6. Write per-phase questions: interrogative form mandatory (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 — Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 — Declare Arc Phases

**The catalog must remain closed at this step. Opening the catalog before phase declaration is complete contaminates the arc with skill availability bias. Do not do it.**

Declare 3–6 phase boundaries from first principles — investigative milestones, not skill containers.

Phase names encode investigative purpose, not skill content:
- PASS: `discovery`, `de-risk`, `depth-simulation`, `signal-watch`
- FAIL: `scout_stage`, `prove_and_review_block`, `skills_cluster_1`

For each phase, the investigative question it answers (genuine interrogative, ends with `?`):

| Phase label | Investigative question |
|-------------|------------------------|
| [name]      | [...?]                 |

The phase map is locked after this step.

---

#### Step 3 — Select Skills

Now open the catalog. Select skills relevant to the topic, grouped by namespace. Note the phase from Step 2 each skill belongs to.

---

#### Step 4 — Assign Skills to Phases

Map each skill to its Step 2 phase. Do not create new phases. Discard skills with no matching phase.

---

#### Step 5 — Design Gates

Each non-echo phase gate must include a **lineage prefix** that names the producing skill and stage, followed by a numeric threshold and artifact condition.

**Gate lineage prefix format** (C-09 + C-11 combined enforcement):

```
[<namespace>:<skill> in <stage-name> produces <artifact-type>] >= N <artifact-type> present
```

- PASS:
  ```
  [scout:feasibility in discovery produces feasibility-signal] >= 3 scout-namespace artifacts present and draft:spec artifact exists
  ```
- FAIL (no lineage prefix, no threshold):
  ```
  adequate scout evidence gathered
  ```
- FAIL (forward reference — producing skill not in the named stage):
  ```
  [trace:deployment in discovery produces deployment-manifest] >= 1 deployment-manifest present
  ```
  (Invalid: `trace:deployment` is not assigned to `discovery`; this is a forward reference.)

Every lineage prefix must name a skill that appears in that stage's `skills` array. A prefix naming a skill from a different stage is a structural error — fix the gate or move the skill.

At least one gate across all non-echo stages must include a numeric threshold (`>= N`).

---

#### Step 6 — Phase Intent Questions

Questions from Step 2 become `intent:` fields. Each must:
- End with `?`
- Be phase-specific (not applicable across all phases equally)

**Interrogative form requirement** (C-17):
- PASS: `"Do we understand the operational failure modes well enough to spec mitigations?"`
- NOT A QUESTION (fail): `"Understand the operational failure modes"`

---

#### Step 7 — Evidence Arc Field

Encode the arc as a required top-level field:

```yaml
evidence_arc:
  breadth:   [scout + draft phase labels]
  depth:     [prove + review + flow + trace phase labels]
  synthesis: [listen + metrics + goals phase labels]
```

Every phase from Step 2 must appear in exactly one arc key.

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
    gate: "[<namespace>:<skill> in <stage-name> produces <artifact-type>] >= N <artifact-type> present"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage MUST include a `phase:` field whose value matches a key in `evidence_arc:`.

FAIL (phase: missing):
```yaml
- name: de-risk
  intent: "Does our design withstand expert review?"
  skills: [review:design, draft:spec]
  gate: "[draft:spec in de-risk produces spec-artifact] >= 1 spec-artifact present"
```

PASS:
```yaml
- name: de-risk
  phase: depth
  intent: "Does our design withstand expert review?"
  skills: [review:design, draft:spec]
  gate: "[draft:spec in de-risk produces spec-artifact] >= 1 spec-artifact present"
```

**Two-criteria enforcement block: arc phase field × gate quantification** (C-19 — crossing arc-structure/construction-protocol and gate-behavior ladders):

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Every non-echo stage must declare `phase:` with a value matching an `evidence_arc:` key | C-18 (Arc-Structure Ladder) | `phase: stage_two` where `stage_two` is not defined in `evidence_arc:` | `phase: depth` where `depth` is a defined arc key |
| At least one gate must include a numeric threshold in the lineage prefix format | C-09 (Gate-Behavior Ladder) | `gate: "adequate scout coverage"` — no threshold, no lineage prefix | `gate: "[scout:feasibility in discovery produces feasibility-signal] >= 3 scout artifacts present"` |

Both conditions must hold across the full stages array.

---

#### Step 9 — Per-Stage Compliance Table

One row per non-echo stage. Column headers name each criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to arc key? (C-18) | Gate-Behavior Ladder: gate has lineage prefix with `>=N` threshold? (C-09) | Question-Framing Ladder: `intent:` ends with `?` (C-17) |
|-------|--------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ...       | ...      | ...      | ...      |

Any NO requires revision before Step 10.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; no skills field; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gates reference specific artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate with numeric threshold (>= N) in lineage prefix format
[ ] C-10: stage names encode strategic purpose
[ ] C-11: every gate lineage prefix names a skill present in the same stage (no forward references)
[ ] C-12: every phase has a phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification (Step 5) AND gate traceability (Step 5, FORWARD REFERENCE fail example)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level YAML field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-18 (Arc-Structure Ladder) x C-09 (Gate-Behavior Ladder), four-column decomposition
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 table spans Arc-Structure Ladder (C-18) + Gate-Behavior Ladder (C-09) + Question-Framing Ladder (C-17)
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section before Step 1
[ ] C-26: Step 2 catalog prohibition names failure mechanism (skill availability bias contaminates arc)
[ ] C-27: Step 9 column headers name ladder family with criterion ID
[ ] C-28: Step 8 C-19 block uses four-column decomposition (Constraint/Criterion/Violation/Compliance)
[ ] C-29: CONSTRUCTION ORDER block contains meta-execution directive ("Read all steps before beginning Step 1")
```

---

## V-03 — Inertia Framing

**Axis**: Inertia framing — the prompt opens with an explicit named description of the status-quo competitor (skill-list-driven program building, where you scan the catalog first and assemble stages around available skills). The arc-first approach is positioned as the antidote, not merely the default. The framing is placed before the catalog to make the structural inversion visible before any construction begins.

**Hypothesis**: The status-quo competitor for program planning is "catalog-first program building" — scanning skills, grouping related ones into stages, then labeling the stages. This produces programs where the arc is retroactively inferred from skill clusters rather than declared as investigative intent. Naming this failure mode before Step 1 (not just inside Step 2) shifts the reader's attention to the underlying architectural question — what does this team need to learn? — before any catalog is opened. This reinforces C-26 (failure mechanism named in prohibition) and C-23 (catalog prohibition explicit in phase-declaration step) by priming the reader on WHY the constraint matters.

**C-19 pair**: C-20 (arc-structure/construction-protocol) × C-12 (question-framing).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a plan, not an executor.

---

**What this prompt is NOT doing (and why it matters)**

The default failure mode for program planning is **catalog-first construction**: open the skill catalog, identify relevant skills, group related ones into stages, then name the stages after the skill clusters. This produces programs that answer "what can we run?" rather than "what do we need to learn?" The resulting stages are named `scout_and_draft_phase` and `prove_and_review_block` — labels that describe skill content, not investigative intent. Gates become summaries ("all probe skills complete") rather than artifact conditions (">=3 scout artifacts and draft:spec present"). The program is a skill inventory with sequencing, not an evidence arc.

This prompt builds programs that answer "what does the team need to learn, and in what order?" — then fills those investigative phases with skills. Phase declarations happen before the catalog is consulted. Skills are assigned to declared phases, not the other way around.

The structural discipline is simple: arc first, skills second.

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
5a. Design gates: artifact-grounded, at least one quantified (Step 5a)
5b. Gate traceability audit: forward references prohibited (Step 5b)
6. Write per-phase questions: interrogative form mandatory (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 — Topic

State the topic name.

---

#### Step 2 — Declare Arc Phases

**The catalog must remain closed at this step. Opening the catalog before phase declaration is complete contaminates the arc with skill availability bias. Do not do it.**

Declare 3–6 phase boundaries as investigative milestones — not skill containers, not stage labels, not catalog clusters. Ask: what does the team need to believe, confirm, or rule out before advancing to the next phase?

Phase names encode investigative purpose:
- PASS: `discovery`, `stress-test`, `de-risk`, `adoption-watch`
- FAIL: `scout_stage`, `prove_skills_block`, `trace_and_flow_phase`

For each phase, state the investigative question it is designed to answer (genuine interrogative, ends with `?`):

| Phase label | Investigative question |
|-------------|------------------------|
| [name]      | [...?]                 |

The phase map is locked after this step. Steps 3–8 fill this skeleton — they do not redesign it.

---

#### Step 3 — Select Skills

Now open the catalog. Select skills relevant to the topic, grouped by namespace. Note the phase from Step 2 each skill belongs to.

---

#### Step 4 — Assign Skills to Phases

Map each skill to its Step 2 phase. Do not create new phases. Discard skills with no matching phase.

---

#### Step 5a — Design Gates (Quantification)

Each non-echo phase gate must reference specific artifact types or signal counts. At least one gate must include a numeric threshold (`>= N`).

**Gate quantification enforcement** (C-09):
- PASS: `>= 3 scout artifacts present and draft:spec artifact exists`
- FAIL: `team ready to advance`
- FAIL: `adequate discovery signals present`

---

#### Step 5b — Gate Traceability Audit

Every artifact named in a gate must be producible by a skill in the same stage. A gate that references an artifact type from a skill not in the current stage is a FORWARD REFERENCE.

**Traceability enforcement** (C-11):

FORWARD REFERENCE (fail) — gate requires `trace:deployment artifact` but stage contains only `scout:` skills:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the platform constraints?"
  skills:
    - scout:feasibility
    - scout:compliance
  gate: ">= 1 trace:deployment artifact confirming platform topology"
```

VALID — gate requires artifacts producible by skills in the same stage:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the platform constraints well enough to commit to a design direction?"
  skills:
    - scout:feasibility
    - scout:compliance
  gate: ">= 2 scout-namespace artifacts present and scout:compliance signal confirmed"
```

For each non-echo stage: verify every gate artifact type can be produced by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 — Phase Intent Questions

Questions from Step 2 become `intent:` YAML fields. Each must end with `?` and be specific to that phase.

**Interrogative form requirement** (C-17):
- PASS: `"Does this design survive adversarial failure conditions?"`
- NOT A QUESTION (fail): `"Validate the design under failure conditions"`

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
    gate: "<artifact-grounded condition>"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage MUST include `phase:` mapping to an `evidence_arc:` key.

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

**Two-criteria enforcement block: phase declaration before catalog × per-phase investigative questions** (C-19 — crossing arc-structure/construction-protocol and question-framing ladders):

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared in Step 2 before catalog opened in Step 3 | C-20 (arc-structure/construction-protocol) | Phase names match catalog namespace clusters (scout_and_draft, prove_block) — phases declared by scanning catalog, not by investigative intent | Phase map complete and locked before Step 3 begins; no phase name echoes a namespace |
| Every phase carries a phase-specific investigative question ending with `?` | C-12 (question-framing) | Generic question "are we ready to proceed?" applicable to all phases equally | Phase-specific question answerable only by running that phase's skills (e.g., "Have we stress-tested the design against adversarial failure conditions?") |

---

#### Step 9 — Per-Stage Compliance Table

One row per non-echo stage. Column headers name each criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to `evidence_arc` key? (C-18) | Gate-Behavior Ladder: gate contains `>=N` threshold? (C-09) | Question-Framing Ladder: `intent:` ends with `?` (C-17) |
|-------|-------------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ...       | ...      | ...      | ...      |

Any NO triggers revision.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: YAML valid; stages array present
[ ] C-02: echo is last; auto: true; no skills; no gate
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gates reference specific artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate with numeric threshold (>= N)
[ ] C-10: stage names encode strategic purpose
[ ] C-11: every gate artifact traceable to same-stage skill (Step 5b audit complete)
[ ] C-12: every phase has a distinct phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification (Step 5a) AND gate traceability (Step 5b, FORWARD REFERENCE pair)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level YAML field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-20 (arc-structure) x C-12 (question-framing), four-column decomposition
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 table spans Arc-Structure Ladder (C-18) + Gate-Behavior Ladder (C-09) + Question-Framing Ladder (C-17)
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section
[ ] C-26: Step 2 catalog prohibition names failure mechanism (skill availability bias contaminates arc)
[ ] C-27: Step 9 column headers name ladder family with criterion ID
[ ] C-28: Step 8 C-19 block uses four-column decomposition (Constraint/Criterion/Violation/Compliance)
[ ] C-29: CONSTRUCTION ORDER block contains meta-execution directive ("Read all steps before beginning Step 1")
```

---

## V-04 — C-11 Isolation + Gate Lineage Prefix (V-01 + V-02 Combined)

**Axis**: Combines V-01 (dedicated C-11 traceability step with FORWARD REFERENCE bad/good pair) and V-02 (gate lineage prefix format that embeds producer identity in gate strings). C-09 enforcement comes from the lineage prefix format requirement; C-11 enforcement comes from both the embedded prefix check AND the dedicated Step 5b traceability audit. Two independent mechanisms enforce the same constraint from different angles.

**Hypothesis**: V-01's dedicated C-11 step closes C-13 by isolation. V-02's lineage prefix format makes forward references visually immediate during gate authoring. Combined, C-11 traceability is enforced both structurally (format prevents it) and procedurally (audit catches residual errors). C-13 passes with full credit (both C-09 and C-11 have dedicated format examples). Anticipated score: 200 / 200.

**C-19 pair**: C-20 (arc-structure/construction-protocol) × C-12 (question-framing).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a plan, not an executor.

The arc — not the skill list — is the load-bearing structure. Phase boundaries must be declared from first principles before the catalog is consulted. Consulting the catalog before phase declaration contaminates the arc with skill availability bias.

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
5a. Design gates: lineage prefix format, at least one quantified (Step 5a)
5b. Gate traceability audit: forward references prohibited (Step 5b)
6. Write per-phase questions: interrogative form mandatory (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 — Topic

State the topic name.

---

#### Step 2 — Declare Arc Phases

**The catalog must remain closed at this step. Opening the catalog before phase declaration is complete contaminates the arc with skill availability bias. Do not do it.**

Declare 3–6 phase boundaries as investigative milestones, not skill containers.

Phase names encode investigative purpose:
- PASS: `discovery`, `de-risk`, `depth`, `signal-watch`
- FAIL: `scout_stage`, `prove_block`, `flow_and_trace`

For each phase, state the investigative question it answers (genuine interrogative, ends with `?`):

| Phase label | Investigative question |
|-------------|------------------------|
| [name]      | [...?]                 |

Phase map is locked after this step.

---

#### Step 3 — Select Skills

Now open the catalog. Select skills grouped by namespace. Note the phase each belongs to.

---

#### Step 4 — Assign Skills to Phases

Map each skill to its declared phase. Do not introduce new phases.

---

#### Step 5a — Design Gates (Lineage Prefix Format)

Each gate must use the lineage prefix format to make producer identity explicit:

```
[<namespace>:<skill> in <stage-name> produces <artifact-type>] >= N <artifact-type> present
```

**Gate format enforcement** (C-09):
- PASS:
  ```
  [scout:feasibility in discovery produces feasibility-signal] >= 3 scout artifacts present and draft:spec artifact exists
  ```
- FAIL (no prefix, no threshold):
  ```
  team ready to advance
  ```

At least one gate across all non-echo stages must include `>= N`.

---

#### Step 5b — Gate Traceability Audit (FORWARD REFERENCE CHECK)

After writing all gates, verify: every skill named in a lineage prefix exists in that stage's `skills` array.

**Traceability enforcement** (C-11):

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the technical constraints?"
  skills:
    - scout:feasibility
  gate: "[trace:deployment in discovery produces deployment-map] >= 1 deployment-map present"
```
(`trace:deployment` is not in `discovery`'s `skills` — forward reference.)

VALID:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the technical constraints well enough to commit to a design direction?"
  skills:
    - scout:feasibility
    - scout:compliance
  gate: "[scout:feasibility in discovery produces feasibility-signal] >= 2 scout artifacts present"
```

Fix all forward references before Step 6.

---

#### Step 6 — Phase Intent Questions

Questions from Step 2 become `intent:` YAML fields. Each must end with `?` and be phase-specific.

**Interrogative form requirement** (C-17):
- PASS: `"Do we have enough validated evidence to commit to this design?"`
- NOT A QUESTION (fail): `"Validate the evidence baseline"`

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
    intent: "<question ending with ?>"
    skills:
      - <namespace>:<skill>
    gate: "[<skill> in <stage> produces <artifact>] >= N <artifact> present"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage MUST include `phase:` mapping to an `evidence_arc:` key.

FAIL:
```yaml
- name: de-risk
  intent: "Does our spec hold up?"
  skills: [draft:spec, review:design]
  gate: "[draft:spec in de-risk produces spec-artifact] >= 1 spec-artifact present"
```

PASS:
```yaml
- name: de-risk
  phase: depth
  intent: "Does our spec hold up under expert review?"
  skills: [draft:spec, review:design]
  gate: "[draft:spec in de-risk produces spec-artifact] >= 1 spec-artifact present"
```

**Two-criteria enforcement block: phase declaration before catalog × per-phase questions** (C-19 — crossing arc-structure/construction-protocol and question-framing ladders):

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared in Step 2 before catalog opened in Step 3 | C-20 (arc-structure/construction-protocol) | Phase names match catalog namespace groups — phases assembled by scanning catalog, not by investigative intent | Phase map locked in Step 2 before catalog is consulted in Step 3 |
| Every phase carries a phase-specific investigative question ending with `?` | C-12 (question-framing) | Generic question applicable to all phases ("are we ready to advance?") rather than a question answerable only by this phase's skills | Each phase has a distinct, phase-specific question (e.g., "Have we validated the design against the market signal?") |

---

#### Step 9 — Per-Stage Compliance Table

One row per non-echo stage. Column headers name each criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to arc key? (C-18) | Gate-Behavior Ladder: gate has lineage prefix with `>=N`? (C-09) | Question-Framing Ladder: `intent:` ends with `?` (C-17) |
|-------|--------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ...       | ...      | ...      | ...      |

Any NO requires revision.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: YAML valid; stages array present
[ ] C-02: echo is last; auto: true; no skills; no gate
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings
[ ] C-07: gates reference specific artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis
[ ] C-09: at least one gate with lineage prefix and numeric threshold (>= N)
[ ] C-10: stage names encode strategic purpose
[ ] C-11: every gate lineage prefix names a skill in the same stage (Step 5b audit complete)
[ ] C-12: every phase has a phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification (Step 5a, lineage prefix PASS/FAIL) AND gate traceability (Step 5b, FORWARD REFERENCE pair)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level YAML field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-20 (arc-structure) x C-12 (question-framing), four-column decomposition
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone, fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 table spans Arc-Structure Ladder (C-18) + Gate-Behavior Ladder (C-09) + Question-Framing Ladder (C-17)
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section
[ ] C-26: Step 2 catalog prohibition names failure mechanism (skill availability bias)
[ ] C-27: Step 9 column headers name ladder family with criterion ID
[ ] C-28: Step 8 C-19 block uses four-column decomposition (Constraint/Criterion/Violation/Compliance)
[ ] C-29: CONSTRUCTION ORDER block contains meta-execution directive ("Read all steps before beginning Step 1")
```

---

## V-05 — All Three Axes Combined (C-11 Isolation + Lineage Prefix + Inertia Framing)

**Axis**: Combines all three R8 axes — dedicated C-11 step (V-01), gate lineage prefix format (V-02), and inertia framing with named status-quo competitor (V-03). The inertia framing primes the reader before the catalog is shown. The lineage prefix makes forward references visible during gate authoring. The dedicated C-11 audit step catches residual errors. Three independent mechanisms across two constraint dimensions (format + process).

**Hypothesis**: The three axes are orthogonal: inertia framing operates at the motivation layer (why arc-first?), lineage prefix operates at the format layer (what do gate strings look like?), and dedicated C-11 step operates at the process layer (how are errors audited?). They reinforce different failure modes without duplicating each other. Combined, they should produce the highest-reliability variant: readers unlikely to miss C-23/C-26 (motivated by inertia framing), C-11 (blocked by lineage prefix + audit), and C-13 (isolated by dedicated step). Anticipated score: 200 / 200.

**C-19 pair**: C-20 (arc-structure/construction-protocol) × C-12 (question-framing).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with explicit handoff gates and topic tracking. Every skill runs standalone — the program is a plan, not an executor.

---

**The status-quo competitor: catalog-first program building**

The default failure mode for program planning is scanning the skill catalog, grouping related skills into stages, and labeling each group after its namespace cluster: `scout_and_draft_phase`, `prove_and_review_block`, `listen_and_metrics_stage`. This produces plans that answer "what skills can we run?" rather than "what do we need to learn?" The arc is retroactively inferred from skill clusters — not declared from investigative intent. Gates become completion summaries ("all scout skills done") rather than artifact conditions (">=3 scout signals present and draft:spec artifact exists"). The program is a skill inventory with sequencing labels, not a strategic evidence arc.

This prompt builds programs that ask "what does the team need to learn, and in what order?" — then fills those investigative phases with skills. Arc first. Skills second. This is not a stylistic preference; it is a structural discipline. A catalog-first program cannot distinguish between a phase that asks "Do we know enough to build this?" and one that asks "Did building it work?" An arc-first program makes that distinction load-bearing.

The construction protocol enforces this order explicitly.

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

Only skills from this catalog may appear in any stage `skills` list. Do not invent, abbreviate, or namespace-expand skill names beyond what is shown.

---

## CONSTRUCTION ORDER

This is the required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases — **the catalog must remain closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: lineage prefix format, at least one quantified (Step 5a)
5b. Gate traceability audit: forward references prohibited (Step 5b)
6. Write per-phase questions: interrogative form mandatory (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 — Topic

State the topic name.

---

#### Step 2 — Declare Arc Phases

**The catalog must remain closed at this step. Opening the catalog before phase declaration is complete contaminates the arc with skill availability bias. Do not do it.**

The arc-first discipline means declaring investigative milestones before knowing which skills will fill them. A phase named "discovery" asks "do we understand the problem space well enough to commit?" regardless of which scout skills happen to be available. A phase named "scout_skills" is a catalog label, not an investigative commitment.

Declare 3–6 phases as investigative milestones. Phase names encode what the team is trying to learn, not which catalog entries they will run.

- PASS: `discovery`, `stress-test`, `de-risk`, `adoption-watch`, `evidence-synthesis`
- FAIL: `scout_and_draft`, `prove_block`, `flow_trace_simulation`, `all_validation_skills`

For each phase, the investigative question it is designed to answer (genuine interrogative, ends with `?`):

| Phase label | Investigative question |
|-------------|------------------------|
| [name]      | [...?]                 |

Phase map is locked after this step. Do not revise it when consulting the catalog in Step 3.

---

#### Step 3 — Select Skills

Now open the catalog. Select skills relevant to the topic, grouped by namespace. Note the phase from Step 2 each skill belongs to.

---

#### Step 4 — Assign Skills to Phases

Map each selected skill to its Step 2 phase. Do not create new phases. If a skill cannot be assigned to any declared phase, discard it or revisit Step 2.

---

#### Step 5a — Design Gates (Lineage Prefix Format)

Each gate must use the lineage prefix format to make the producing skill and artifact type explicit before the threshold condition:

```
[<namespace>:<skill> in <stage-name> produces <artifact-type>] >= N <artifact-type> condition
```

**Gate format enforcement** (C-09):
- PASS:
  ```
  [scout:feasibility in discovery produces feasibility-signal] >= 3 scout-namespace artifacts present and draft:spec artifact exists
  ```
- FAIL (no prefix, no threshold):
  ```
  team has sufficient discovery signal
  ```
- FAIL (threshold missing):
  ```
  [scout:feasibility in discovery produces feasibility-signal] discovery complete
  ```

At least one gate must include `>= N`.

---

#### Step 5b — Gate Traceability Audit

After writing all gates, verify: every skill named in a lineage prefix exists in that same stage's `skills` array. A prefix that names a skill not assigned to the current stage is a FORWARD REFERENCE — a structural error.

**Traceability enforcement** (C-11):

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the deployment topology?"
  skills:
    - scout:feasibility
    - scout:compliance
  gate: "[trace:deployment in discovery produces deployment-map] >= 1 deployment-map present"
```
(`trace:deployment` not in `discovery`'s skills — forward reference. Fix by moving `trace:deployment` to the appropriate depth-phase stage or rewriting the gate.)

VALID:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the platform constraints well enough to commit to a design direction?"
  skills:
    - scout:feasibility
    - scout:compliance
  gate: "[scout:feasibility in discovery produces feasibility-signal] >= 2 scout-namespace artifacts present"
```

Check every non-echo stage. Fix all forward references before Step 6.

---

#### Step 6 — Phase Intent Questions

Questions from Step 2 become `intent:` YAML fields. Each must end with `?` and be phase-specific.

**Interrogative form requirement** (C-17):
- PASS: `"Does our design survive adversarial failure conditions?"`
- NOT A QUESTION (fail): `"Validate the design against failure conditions"`
- NOT A QUESTION (fail): `"Design validation complete"`

---

#### Step 7 — Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [scout + draft phase labels]
  depth:     [prove + review + flow + trace phase labels]
  synthesis: [listen + metrics + goals phase labels]
```

Every phase from Step 2 must appear in exactly one arc key.

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
    gate: "[<skill> in <stage> produces <artifact>] >= N <artifact> condition"
  - ...
  - name: echo
    auto: true
```

**Dedicated C-18 enforcement — per-stage `phase:` field** (standalone block):

Every non-echo stage MUST include `phase:` mapping to an `evidence_arc:` key. A stage without `phase:` is structurally incomplete.

FAIL:
```yaml
- name: discovery
  intent: "Do we understand the problem?"
  skills: [scout:feasibility]
  gate: "[scout:feasibility in discovery produces feasibility-signal] >= 2 scout artifacts"
```

PASS:
```yaml
- name: discovery
  phase: breadth
  intent: "Do we understand the problem well enough to commit?"
  skills: [scout:feasibility]
  gate: "[scout:feasibility in discovery produces feasibility-signal] >= 2 scout artifacts"
```

**Two-criteria enforcement block: phase declaration before catalog × per-phase investigative questions** (C-19 — crossing arc-structure/construction-protocol and question-framing ladders):

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared in Step 2 before catalog opened in Step 3 | C-20 (arc-structure/construction-protocol) | Phase names match catalog namespace clusters — arc assembled by scanning catalog, not by investigative intent; catalog-first construction produces skill inventories, not evidence arcs | Phase map locked in Step 2; catalog not consulted until Step 3; phase names encode investigative milestones, not skill groups |
| Every phase carries a phase-specific investigative question ending with `?` | C-12 (question-framing) | Generic question applicable to all phases equally ("are we ready to advance?"); or a statement masquerading as a question ("Validate the design baseline") | Each phase carries a distinct question answerable only by running that phase's specific skills (e.g., "Have we stress-tested the design against adversarial failure conditions?") |

---

#### Step 9 — Per-Stage Compliance Table

One row per non-echo stage. Column headers name each criterion ladder:

| Stage | Arc-Structure Ladder: `phase:` maps to `evidence_arc` key? (C-18) | Gate-Behavior Ladder: gate has lineage prefix with `>=N`? (C-09) | Question-Framing Ladder: `intent:` ends with `?` (C-17) |
|-------|-------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |
| ...       | ...      | ...      | ...      |

Any NO requires revision before Step 10.

---

#### Step 10 — Terminal Validation Checklist

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; no skills; no gate
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gates reference specific artifact types or signal counts
[ ] C-08: arc reads breadth -> depth -> synthesis (catalog-first programs fail this: they read skill-cluster-1 -> skill-cluster-2)
[ ] C-09: at least one gate with lineage prefix and numeric threshold (>= N)
[ ] C-10: stage names encode strategic purpose, not catalog namespace groups
[ ] C-11: every gate lineage prefix names a skill present in the same stage (Step 5b audit complete; no forward references)
[ ] C-12: every phase has a distinct phase-specific investigative question
[ ] C-13: dedicated format examples for gate quantification (Step 5a: PASS/FAIL lineage prefix examples) AND gate traceability (Step 5b: FORWARD REFERENCE fail + VALID pass YAML pair)
[ ] C-14: checklist spans essential + recommended + aspirational tiers
[ ] C-15: each item tagged with criterion ID (C-XX)
[ ] C-16: evidence_arc: present as required top-level YAML field
[ ] C-17: all intent: values end with ?
[ ] C-18: all non-echo stages have phase: field mapping to evidence_arc key
[ ] C-19: Step 8 two-criteria block covers C-20 (arc-structure) x C-12 (question-framing), four-column Constraint/Criterion/Violation/Compliance decomposition
[ ] C-20: phase declaration (Step 2) precedes catalog consultation (Step 3)
[ ] C-21: per-stage compliance table in Step 9 with criterion-mapped columns
[ ] C-22: dedicated C-18 enforcement block in Step 8 (standalone fail/pass YAML pair)
[ ] C-23: Step 2 contains explicit catalog prohibition language
[ ] C-24: Step 9 table spans Arc-Structure Ladder (C-18) + Gate-Behavior Ladder (C-09) + Question-Framing Ladder (C-17)
[ ] C-25: CONSTRUCTION ORDER block present as labeled standalone section before Step 1
[ ] C-26: Step 2 catalog prohibition names failure mechanism (skill availability bias contaminates arc)
[ ] C-27: Step 9 column headers name ladder family with criterion ID (e.g., "Arc-Structure Ladder (C-18)")
[ ] C-28: Step 8 C-19 block uses four-column decomposition (Constraint/Criterion/Violation/Compliance)
[ ] C-29: CONSTRUCTION ORDER block contains meta-execution directive ("Read all steps before beginning Step 1")
```

---

## Anticipated R8 Scores (v8 rubric)

| Variant | R7 Deficit Fixed? | C-26 | C-27 | C-28 | C-29 | v8 Anticipated |
|---------|------------------|------|------|------|------|----------------|
| V-01 — C-11 Isolation | YES (C-13 full, not partial) | P | P | P | P | 200 / 200 |
| V-02 — Gate Lineage Prefix | YES (C-13 full via format + fail example) | P | P | P | P | 200 / 200 |
| V-03 — Inertia Framing | YES (C-13 full via Step 5b) | P | P | P | P | 200 / 200 |
| V-04 — V-01 + V-02 | YES (dual mechanism) | P | P | P | P | 200 / 200 |
| V-05 — All Three Axes | YES (triple mechanism) | P | P | P | P | 200 / 200 |

P = anticipated pass (5 pts).

**R8 differential signal**: All variants target 200/200. Differentiation will emerge if any variant:
- Fails C-13 full (e.g., format example not specific enough to count as "dedicated isolation")
- Fails C-28 (four-column decomposition missing or merging Violation/Compliance)
- Fails C-27 partial vs full (column headers say "arc-structure" vs "Arc-Structure Ladder")
- Introduces new partial-credit exposure in C-21 (table coverage) or C-14 (checklist tier span)

The C-13 fix is the primary R8 hypothesis. If V-01 scores 200/200 and V-02/V-03 score 197.5, the delta isolates whether dedicated-step isolation (V-01) or format-based enforcement (V-02/V-03) satisfies C-13's "dedicated numbered step or labeled section with concrete example" requirement.
