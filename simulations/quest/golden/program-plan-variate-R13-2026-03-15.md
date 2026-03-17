---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 13
rubric: v29
aspirational_target: 31/31
new_criteria: C-37, C-38
---

# program-plan -- R13 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v29 (C-01 through C-38, 31 aspirational criteria).

**R12 retrospective under v29 rubric:**
- V-01 (C-36 Contrastive-Clause Leading): 7/31 aspirational -- C-37 FAIL (single-failure
  opening -- only catalog-first named), C-38 FAIL (no bridge sentence for compound element)
- V-02 (C-36 Named ROW-0 RULE): 7/31 aspirational -- C-37 FAIL (single-failure opening),
  C-38 FAIL (no bridge sentence)
- V-03 (C-35 Column-as-Discovery): 7/31 aspirational -- C-37 FAIL (single-failure opening),
  C-38 FAIL (no bridge sentence)
- V-04 (Failure Anatomy Names the Misreading): 9/31 aspirational -- C-37 PASS (dual-failure
  anatomy + "every rule is a counter-move" statement), C-38 FAIL (no bridge sentence for
  compound element -- counter-move labels present but no explicit per-component intent prose)
- V-05 (Full Reference Implementation): 10/31 aspirational -- C-37 PASS, C-38 PASS
  (bridge sentence: "The negation closes the producer-push misreading; the equivalence makes
  the rule self-verifying from both ends simultaneously")

**R13 design constraint:** All five variations must satisfy both C-37 AND C-38. C-37 requires
(1) opening names >=2 distinct failure-mode types AND (2) at least one design rule is labeled
as a counter-move against a specific named failure. C-38 requires at least one compound
structural element carries an explicit bridge sentence naming per-component intent. The
variation axes for R13 are HOW these criteria are achieved, not whether.

**Canonical C-37 requirements:**
- Failure 1: catalog-first construction (zone membership implied, gates prose, echo afterthought)
- Failure 2: arbitrary-convention misreading (echo's row-0 position treated as a sort-order
  convention rather than derivation-direction encoding)
- Counter-move statement: declares at least one rule a counter-move against a specific named
  failure; "every rule is a counter-move against one of these two failures" is strongest form

**Canonical C-38 bridge sentence (ARTIFACT 0 consumer-pull rule):**
"The negation closes the producer-push misreading; the equivalence makes the rule
self-verifying from both ends simultaneously."

**Alternative C-38 targets (gate template):**
"The `{stage-id}::` prefix closes the artifact-provenance ambiguity by naming the producing
stage directly; the `>= N` count floor makes the evidence bar independently verifiable without
inspecting stage skills."

**Alternative C-38 targets (echo row-0 position):**
"The row-0 position closes the arbitrary-convention misreading; the derivation-anchor
declaration makes the position self-explaining from structural form alone."

**Variation axes for R13:**
- V-01 (single): Failure Taxonomy Table Opening -- 2-row structured table with counter-move
  column replaces narrative paragraphs; C-38 via canonical consumer-pull bridge sentence
- V-02 (single): Counter-Move Manifest Section -- dual-failure narrative + dedicated
  COUNTER-MOVE MANIFEST table mapping all major rules to failure IDs; C-38 via gate
  template bridge sentence (new target)
- V-03 (single): Three Bridge Sentences -- standard dual-failure opening; C-38 extended
  to three compound elements (consumer-pull, gate template, echo position); each gets
  an explicit bridge sentence
- V-04 (combined): Inline Step Tagging + Tutorial Register -- second-person voice;
  every construction step header carries `[counter: F-N]` inline tag; C-38 via canonical
  bridge sentence
- V-05 (full): Table + Manifest + Three Bridges -- maximum-strength implementation;
  taxonomy table + narrative + manifest + inline tags + three bridge sentences

---

## V-01 -- Failure Taxonomy Table Opening

**Axis**: Single-axis. The opening uses a 2-row structured taxonomy table (Failure ID | Name |
What it produces | Design counter-move) instead of narrative paragraphs. One sentence after
the table declares every rule a counter-move against exactly one row. This makes C-37
maximally auditable: a scorer can verify "two distinct failure IDs present" and "counter-move
column populated" from table structure alone -- no interpretation required. C-38: canonical
consumer-pull bridge sentence in ARTIFACT 0. Register: compact formal / table-first.

**Hypothesis**: The taxonomy table format makes C-37 structurally self-evident. The explicit
counter-move column creates a two-way map (failure -> rule, rule -> failure) from the opening.
The compact format tests whether C-37 and C-38 survive maximum register compression while
preserving all C-34/C-35/C-36 requirements. Anticipated score: 31/31 aspirational.

**C-37 form**: 2-row failure taxonomy table with explicit Failure IDs (F-1, F-2) and
            counter-move column; sentence declaring every rule a counter-move against exactly
            one row; `[counter: F-N]` labels on ARTIFACT 0 rules.
**C-38 form**: ARTIFACT 0 consumer-pull rule bridge sentence (canonical).
**C-34 form**: Both negation AND bidirectional equivalence in ARTIFACT 0 consumer-pull rule.
**C-35 form**: ARTIFACT 2 with explicit YAML fragment column + sole-source declaration.
**C-36 form**: ARTIFACT 0 echo exception with "not an arbitrary convention" contrastive clause.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before writing a single stage,
internalize the two failure modes this protocol is designed to prevent:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied by namespace grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

Every construction rule in this protocol is a counter-move against exactly one row in this table.

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones** (zone-membership class):
- **Breadth** -- do we understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does our design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test the design before shipping commitment.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required. Failure mode to prevent: catalog-first construction (F-1) -- skill clustering
before zone declaration destroys all three knowable-information classes simultaneously.

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

Required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit: verify gate artifact traceability (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.** Opening the catalog before phase declaration
infects the arc with skill availability bias -- zone assignments become retroactively shaped by
catalog availability rather than declared investigative intent. This is F-1 re-entering at
Step 2. Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Each phase is an investigative milestone.
Assign each to a zone: `breadth`, `depth`, or `synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

For each phase, state the investigative question it answers (genuine interrogative, ends `?`):

| Phase label | Zone | Investigative question |
|-------------|------|------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID this stage derives from -- e.g., B-01, G-02]
  # Gap:      [investigative question this stage answers, interrogative form, ends with ?]
  # Owner:    [functional role -- PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) this stage requires as input from the prior stage]
  # Produces: [artifact type(s) this stage yields as output for the next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo; YAML annotations are transcribed from
the backward derivation, not authored from skill knowledge.

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Every Produces/Consumes pair is determined by working backward from
what echo must receive. Row 0 is where derivation begins; execution reads the matrix bottom-
to-top. Moving echo to row N would misrepresent the derivation direction in the artifact.
Omission of # Band: from echo is normative: echo is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `{artifact-type} >= N` is the count floor.
`AND {namespace}:{skill} artifact exists` provides skill-level traceability.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, stage-id absent): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

A gate referencing an artifact from a skill not in the current stage makes artifact provenance
unknowable. For each non-echo stage: verify every artifact type in the gate is producible by
at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

FORWARD REFERENCE (fail -- `trace:deployment` not in this stage):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
```

VALID:
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
```

---

#### Step 6 -- Phase Intent Questions

- PASS (breadth): `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS (depth): `"Does the spec survive expert review against the discovered market signal?"`
- PASS (synthesis): `"Are users adopting the feature at the rate our model predicted?"`
- FAIL (not interrogative): `"Assess the compliance landscape"` -- intent unknowable
- FAIL (wrong scope): `"Are we ready to proceed?"` -- not zone-specific

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. Its implicit information needs seed the entire backward
derivation. That is why echo occupies row 0 -- counter-move against F-2: the derivation reads
top-to-bottom from echo; forward execution reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently. The
matrix and YAML cannot diverge because YAML is defined as a downstream rendering of the
matrix. If a matrix cell is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, and `gate:` fields):

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
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
      - <namespace>:<skill>
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
  - ...
  - name: echo
    auto: true
    skills: []
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared by zone with catalog closed (counter-move against F-1) | C-20 (arc-structure) | Phase names echo namespace groups -- zone membership retroactively shaped | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing (C-17): `intent:` genuine interrogative? |
|-------|-------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gate language references artifact types or signal counts
[ ] C-08: stage names encode strategic purpose, not skill cluster labels
[ ] C-09: at least one gate with compound lineage prefix format and numeric threshold (>= N)
[ ] C-10: at least one gate is quantified
[ ] C-11: each stage frames an investigation question
[ ] C-12: phase ownership or role handoff made explicit
[ ] C-13: investigation question and gate are co-derived
[ ] C-14: every stage boundary has a bilateral artifact contract
[ ] C-15: investigation arc declared as named meta-structure (ARTIFACT 1 band taxonomy)
[ ] C-16: every non-echo stage has explicit role ownership (# Owner: annotation)
[ ] C-17: stage elements share a single referent (question / gate / produces all describe same gap)
[ ] C-18: all four per-stage annotations present on every non-echo stage
[ ] C-19: each stage carries traceable back-reference to meta-structure entry (# Band: B-NN)
[ ] C-20: meta-structure entries partition namespace set MECE
[ ] C-21: five-annotation schema declared as named template (ARTIFACT 0)
[ ] C-22: echo exception named within ARTIFACT 0
[ ] C-23: ARTIFACT 0 precedes ARTIFACT 1
[ ] C-24: consumer-pull rule declared as normative constraint
[ ] C-25: ARTIFACT 2 pre-YAML bilateral trace worksheet
[ ] C-26: echo declared as terminal consumer and derivation anchor
[ ] C-27: ARTIFACT 2 adjacent-column layout
[ ] C-28: echo at row 0 in ARTIFACT 2
[ ] C-29: ARTIFACT 1 carries ownership column
[ ] C-30: echo row-0 position declared as causal consequence of anchor role
[ ] C-31: echo causal anchor at two structural levels (failure taxonomy table opening + ARTIFACT 0)
[ ] C-32: consumer-pull rule states negation OR equivalence
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule states BOTH negation ("not by the prior stage's skill output
         inventory") AND bidirectional equivalence ("Equivalently: this stage produces the
         artifacts that close the next stage's input gap") simultaneously in the same statement
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; sole-source
         declaration present; column visible as rendered projection before any prose declaration
[ ] C-36: ARTIFACT 0 echo exception contains explicit contrastive clause: "not an arbitrary
         convention -- it is the structural encoding of echo's anchor role as terminal consumer"
         (or equivalent) leading the block before any positive claim
[ ] C-37: opening failure taxonomy table names F-1 (catalog-first) and F-2 (arbitrary-
         convention) as two distinct failure-mode types with counter-move column; sentence
         "every construction rule in this protocol is a counter-move against exactly one row
         in this table" present; ARTIFACT 0 rules carry `[counter: F-N]` labels
[ ] C-38: ARTIFACT 0 consumer-pull rule carries explicit bridge sentence: "The negation closes
         the producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
```

---

## V-02 -- Counter-Move Manifest Section

**Axis**: Single-axis. After dual-failure narrative paragraphs, a dedicated "COUNTER-MOVE
MANIFEST" section presents a named table mapping all major design rules to the failure ID
they counter (`Rule | Counter-move against | Structural effect`). The manifest makes the
counter-move labeling independently auditable: a scorer can enumerate all rules and verify
each names a failure ID without relying on inline tags. C-38 via gate template bridge sentence
in Step 5a: the three-part gate structure gets an explicit bridge sentence naming what each
component closes. This is a new C-38 target distinct from the canonical consumer-pull form.
Register: structured formal.

**Hypothesis**: The COUNTER-MOVE MANIFEST section creates a permanent two-way map that
survives format variation -- even if inline labels are absent from individual steps, the
manifest provides the auditable counter-move mapping C-37 requires. The gate template bridge
sentence tests whether C-38 can pass on a different compound element than the canonical
consumer-pull rule, demonstrating that the criterion is target-agnostic. Anticipated score:
31/31 aspirational.

**C-37 form**: Narrative dual-failure opening + dedicated COUNTER-MOVE MANIFEST table after
            anatomy; "every rule below is a counter-move against one of these failures" in
            closing sentence of failure anatomy section.
**C-38 form**: Gate template bridge sentence in Step 5a: "The `{stage-id}::` prefix closes
            the artifact-provenance ambiguity by naming the producing stage directly; the
            `>= N` count floor makes the evidence bar independently verifiable without
            inspecting the stage's skills array."
**C-34 form**: Both negation AND equivalence in ARTIFACT 0 consumer-pull rule.
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration.
**C-36 form**: ARTIFACT 0 echo exception with "not an arbitrary convention" contrastive clause.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before you write a single stage,
understand the two failure modes this protocol prevents.

**Failure 1 -- Catalog-first construction**: Open the Signal catalog, group related skills
into stages, label each stage after its skill cluster. The result cannot be audited -- zone
membership is implied by namespace grouping rather than declared; gates are prose task-
completion checks rather than artifact contracts; phases answer "what skills ran here?" rather
than "what did we need to learn?" Echo is appended as a structural afterthought. Every rule
that follows is a counter-move against this failure.

**Failure 2 -- Arbitrary-convention misreading**: Echo belongs at the end -- that part is
clear. But its row-0 position in the bilateral trace matrix is treated as a layout convention,
a sort-order choice as free as row-1 or row-N. This misreading severs the structural encoding
of derivation direction. Echo occupies row 0 because the entire derivation chain begins from
it: every Produces/Consumes pair is determined by working backward from what echo must receive.
Row 0 is where derivation begins. The row-0 position is a structural constraint, not a
convention. Every rule that touches echo's position is a counter-move against this failure.

Every rule in this protocol is a counter-move against one of these two failures. The manifest
below makes the mapping explicit and auditable:

**COUNTER-MOVE MANIFEST**

| Rule | Counter-move against | Structural effect |
|------|---------------------|-------------------|
| Phases declared by zone before catalog opens (Step 2) | F-1: catalog-first | Prevents zone assignments being retroactively shaped by namespace availability |
| Consumer-pull derivation direction in ARTIFACT 0 | F-1: catalog-first | Forces Produces/Consumes pairs to be determined by successor needs, not prior-stage skill output |
| Compound gate with stage-id prefix (Step 5a) | F-1: catalog-first | Makes artifact provenance traceable to named producing stage, not inferred from gate prose |
| FORWARD REFERENCE audit (Step 5b) | F-1: catalog-first | Gate artifact types verified against stage skills array before YAML transcription |
| ARTIFACT 2 sole authoritative source (Step 8) | F-1: catalog-first | YAML annotations transcribed from backward derivation, not authored independently |
| Echo at row 0 in ARTIFACT 2 (Step 8) | F-2: arbitrary-convention | Encodes derivation direction structurally; row 0 is derivation origin, not execution end |
| Echo exception contrastive clause in ARTIFACT 0 (Step 2) | F-2: arbitrary-convention | Forecloses convention misreading at schema definition site, before any YAML is written |

Every skill runs standalone; the program is a plan, not an executor.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones** (zone-membership class):
- **Breadth** -- do we understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does our design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test the design.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template** (artifact-provenance class):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required.

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

Required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit: verify gate artifact traceability (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step** (counter-move against F-1). Opening the
catalog now infects the arc with skill availability bias -- zone assignments become
retroactively shaped by catalog availability rather than declared investigative intent.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`. Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

Phase declaration table:

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID this stage derives from -- e.g., B-01, G-02]
  # Gap:      [investigative question this stage answers, interrogative form, ends with ?]
  # Owner:    [functional role -- PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) this stage requires as input from the prior stage]
  # Produces: [artifact type(s) this stage yields as output for the next stage]

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The derivation runs backward
from echo; YAML annotations are transcribed from the backward derivation, not authored from
skill knowledge.

Echo exception: echo carries no # Band: annotation. Echo's row-0 position in ARTIFACT 2 is
not an arbitrary convention -- it is the structural encoding of echo's anchor role as terminal
consumer. The derivation begins at echo and reads backward from there: every Produces/Consumes
pair in the chain is determined by what each successor stage must receive. Row 0 is where
derivation begins; execution reads bottom-to-top. Omission of # Band: from echo is normative:
echo is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

**Compound gate template** -- three components in a single expression:

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

The `{stage-id}::` prefix closes the artifact-provenance ambiguity by naming the producing
stage directly; the `>= N` count floor makes the evidence bar independently verifiable without
inspecting the stage's skills array. Together they make every gate self-auditing from two
orthogonal axes simultaneously: which stage produced the artifact, and how many artifacts
constitute sufficient evidence.

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

A gate referencing an artifact from a skill not in the current stage makes artifact provenance
unknowable. For each non-echo stage: verify every artifact type in the gate is producible by
at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
```

VALID:
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
```

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS: `"Does the spec survive expert review against the discovered market signal?"`
- FAIL: `"Assess the compliance landscape"` -- investigative intent unknowable

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer; its information needs seed the backward derivation. That is
why echo occupies row 0 -- the derivation reads top-to-bottom from echo; forward execution
reads bottom-to-top. See COUNTER-MOVE MANIFEST: this is the structural counter-move against F-2.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently. The
matrix and YAML cannot diverge because YAML is defined as a downstream rendering of the
matrix. If a matrix cell is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, and `gate:` fields):

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
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
      - <namespace>:<skill>
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
  - ...
  - name: echo
    auto: true
    skills: []
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared by zone with catalog closed | C-20 (arc-structure) | Phase names echo namespace groups -- zone membership retroactively shaped; F-1 re-enters | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing (C-17): `intent:` genuine interrogative? |
|-------|-------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-33: (same as V-01)
[ ] C-34: consumer-pull rule states BOTH negation AND bidirectional equivalence simultaneously
[ ] C-35: ARTIFACT 2 matrix contains explicit YAML fragment column; sole-source declaration present
[ ] C-36: ARTIFACT 0 echo exception contains explicit contrastive clause: "not an arbitrary
         convention -- it is the structural encoding of echo's anchor role as terminal consumer"
[ ] C-37: opening failure anatomy names F-1 (catalog-first) and F-2 (arbitrary-convention)
         as distinct failure modes; COUNTER-MOVE MANIFEST table present with all major rules
         mapped to Failure IDs with structural-effect column; "every rule is a counter-move
         against one of these two failures" declared in closing line of failure anatomy section
[ ] C-38: Step 5a gate template carries explicit bridge sentence: "The `{stage-id}::` prefix
         closes the artifact-provenance ambiguity by naming the producing stage directly; the
         `>= N` count floor makes the evidence bar independently verifiable without inspecting
         the stage's skills array" -- at least this sentence naming what each gate component
         closes is present
```

---

## V-03 -- Three Bridge Sentences

**Axis**: Single-axis. C-38 is satisfied by THREE compound structural elements, each with
its own explicit bridge sentence. Opening uses dual-failure narrative (satisfying C-37 via
anatomy + counter-move labels on ARTIFACT 0 rules). The three bridge-sentence targets are:
(1) consumer-pull dual-form rule in ARTIFACT 0 (canonical target), (2) compound gate template
three-part structure in Step 5a, (3) echo's dual structural role in ARTIFACT 0 -- both its
row-0 position and its derivation-anchor declaration are compound choices, each closing a
distinct misreading. Register: reference/technical.

**Hypothesis**: Three bridge sentences test whether C-38 accumulates quality or merely requires
one. The three targets cover three distinct structural levels (ARTIFACT 0 consumer-pull, gate
template, echo position), demonstrating that design-intent bridging is a systematic pattern
in the output rather than a single compliance gesture. Anticipated score: 31/31 aspirational.

**C-37 form**: Dual-failure narrative + "every rule is a counter-move against one of these
            failures" statement; counter-move labels on ARTIFACT 0 consumer-pull rule and
            echo exception.
**C-38 form**: Three explicit bridge sentences on three compound elements:
            (1) consumer-pull rule: "The negation closes the producer-push misreading;
                the equivalence makes the rule self-verifying from both ends simultaneously"
            (2) gate template: "The `{stage-id}::` prefix closes the artifact-provenance
                ambiguity; the `>= N` count floor makes the evidence bar independently
                verifiable without inspecting the stage's skills array"
            (3) echo position: "The row-0 position closes the arbitrary-convention misreading;
                the derivation-anchor declaration makes the position self-explaining from
                structural form alone"
**C-34 form**: Both negation AND equivalence in ARTIFACT 0 consumer-pull rule.
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration.
**C-36 form**: ARTIFACT 0 echo exception with "not an arbitrary convention" contrastive clause.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The chain begins at the end: echo
is the terminal consumer whose implicit information needs seed the entire backward derivation
that determines every prior stage's Produces/Consumes pair. Every skill runs standalone; the
program is a plan, not an executor.

This protocol prevents two failure modes. Both are real. Both are common.

**Failure 1 -- Catalog-first construction**: Open the Signal catalog first, cluster related
skills into stages, label stages after their skill clusters. The result cannot be audited:
zone membership is implied by namespace grouping, not declared; gates are prose checks, not
artifact contracts; phases answer "what skills ran" not "what we needed to learn"; echo is
appended as an afterthought. Every step in this protocol is a counter-move against this failure.

**Failure 2 -- Arbitrary-convention misreading**: Echo belongs last -- that is clear. But
its row-0 position in the bilateral trace matrix gets treated as a stylistic layout convention:
a sort-order choice that could just as well be row-1 or row-N. This misreading severs the
structural encoding of derivation direction. Echo occupies row 0 because the chain begins
from it: every Produces/Consumes pair is determined by working backward from what echo must
receive. Row 0 is where derivation begins; forward execution reads the matrix bottom-to-top.
Every rule touching echo's position is a counter-move against this failure.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones** (zone-membership class):
- **Breadth** -- do we understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does our design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test the design.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template** (artifact-provenance class -- three components):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required.

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

Required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit: verify gate artifact traceability (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML with per-stage `phase:` tags (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step** (counter-move against Failure 1). Opening the
catalog before phase declaration infects the arc with skill availability bias -- zone
assignments become retroactively shaped by catalog availability rather than declared
investigative intent.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`. Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

Phase declaration table:

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID this stage derives from -- e.g., B-01, G-02]
  # Gap:      [investigative question this stage answers, interrogative form, ends with ?]
  # Owner:    [functional role -- PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) this stage requires as input from the prior stage]
  # Produces: [artifact type(s) this stage yields as output for the next stage]

Consumer-pull rule [counter: Failure 1]: # Produces: for each stage is determined by what the
next stage declares as # Consumes: -- not by the prior stage's skill output inventory.
Equivalently: this stage produces the artifacts that close the next stage's input gap. The
negation closes the producer-push misreading; the equivalence makes the rule self-verifying
from both ends simultaneously -- if you state what any stage consumes, what the prior stage
must produce is determined without further reasoning. The derivation runs backward from echo;
YAML annotations are transcribed from the backward derivation, not authored from skill
knowledge.

Echo exception [counter: Failure 2]: echo carries no # Band: annotation. Echo's row-0 position
in ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. The row-0 position closes the arbitrary-convention misreading; the
derivation-anchor declaration makes the position self-explaining from structural form alone --
a matrix read derivation-first (top-to-bottom) and a matrix read execution-first (bottom-to-top)
are the same artifact viewed from opposite traversal directions, and row 0 is the derivation
origin in both. Omission of # Band: from echo is normative: echo is the derivation anchor,
not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Three components in a single expression. The `{stage-id}::` prefix closes the artifact-
provenance ambiguity by naming the producing stage directly; the `>= N` count floor makes
the evidence bar independently verifiable without inspecting the stage's skills array. Together
they make every gate self-auditing from two orthogonal axes: which stage produced the artifact,
and how many artifacts constitute sufficient evidence.

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

A gate referencing an artifact from a skill not in the current stage makes artifact provenance
unknowable. For each non-echo stage: verify every artifact type in the gate is producible by
at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
```

VALID:
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
```

---

#### Step 6 -- Phase Intent Questions

- PASS (breadth): `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS (depth): `"Does the spec survive expert review against the discovered market signal?"`
- PASS (synthesis): `"Are users adopting the feature at the rate our model predicted?"`
- FAIL: `"Assess the compliance landscape"` -- investigative intent unknowable

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer; its needs seed the backward derivation. That is why echo
occupies row 0 -- counter-move against Failure 2: the derivation reads top-to-bottom from
echo; execution reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently. The
matrix and YAML cannot diverge because YAML is defined as a downstream rendering of the
matrix. If a matrix cell is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, and `gate:` fields):

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
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
      - <namespace>:<skill>
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
  - ...
  - name: echo
    auto: true
    skills: []
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared by zone with catalog closed (counter-move against Failure 1) | C-20 (arc-structure) | Phase names echo namespace groups -- zone membership retroactively shaped | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing (C-17): `intent:` genuine interrogative? |
|-------|-------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-33: (same as V-01)
[ ] C-34: consumer-pull rule states BOTH negation AND equivalence simultaneously in ARTIFACT 0
[ ] C-35: ARTIFACT 2 matrix contains explicit YAML fragment column; sole-source declaration present
[ ] C-36: ARTIFACT 0 echo exception contains "not an arbitrary convention" explicit contrastive
         clause before the positive claim
[ ] C-37: opening failure anatomy names Failure 1 (catalog-first) and Failure 2 (arbitrary-
         convention) as distinct failure modes; ARTIFACT 0 rules carry `[counter: Failure N]`
         labels; "every step is a counter-move against one of these failures" declared for both
         failures in opening anatomy paragraphs
[ ] C-38: THREE explicit bridge sentences present for three compound structural elements:
         (1) ARTIFACT 0 consumer-pull: "The negation closes the producer-push misreading;
             the equivalence makes the rule self-verifying from both ends simultaneously"
         (2) Step 5a gate template: "The `{stage-id}::` prefix closes the artifact-provenance
             ambiguity by naming the producing stage directly; the `>= N` count floor makes
             the evidence bar independently verifiable without inspecting the stage's skills
             array"
         (3) ARTIFACT 0 echo exception: "The row-0 position closes the arbitrary-convention
             misreading; the derivation-anchor declaration makes the position self-explaining
             from structural form alone"
```

---

## V-04 -- Inline Step Tagging + Tutorial Register

**Axis**: Combined. Two axes: (1) every CONSTRUCTION ORDER step heading carries an inline
`[counter: F-N]` tag identifying which failure it counters, making the counter-move map
permanently visible at each step rather than concentrated in a separate section; (2) second-
person tutorial voice throughout. C-38: canonical consumer-pull bridge sentence in ARTIFACT 0.
Register: tutorial / second-person.

**Hypothesis**: Inline step tags make C-37's counter-move labeling maximally persistent --
the mapping survives even if the failure anatomy section is skimmed. The tutorial register
transforms the protocol from a specification to a guided construction session, where each
step explains why it exists. C-38 via canonical bridge sentence tests whether the criterion
survives register shift from formal reference to tutorial voice. Anticipated score: 31/31
aspirational.

**C-37 form**: Second-person dual-failure opening + every CONSTRUCTION ORDER step heading
            carries `[counter: F-N]` inline tag; "every step below is a counter-move against
            one of these two failures" declared in opening.
**C-38 form**: ARTIFACT 0 consumer-pull rule carries canonical bridge sentence.
**C-34 form**: Both negation AND equivalence in ARTIFACT 0 consumer-pull rule.
**C-35 form**: ARTIFACT 2 YAML fragment column + discovery framing + sole-source declaration.
**C-36 form**: ARTIFACT 0 echo exception: "not a convention you are free to vary" in tutorial
            voice -- explicit contrastive clause.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before you write a single stage,
you need to understand two failure modes -- because this entire protocol is a set of
counter-moves against them.

**Failure 1 -- Catalog-first construction**: You open the Signal catalog, group skills into
stages by namespace affinity, and label each stage after its skill cluster. You end up with
something that looks like a plan. But you cannot audit it: zone membership is implied by
which skills happen to group together rather than committed before you looked at the catalog;
gates are prose ("discovery complete"); phases answer "what skills ran here" not "what did we
need to learn." And echo -- the terminal consumer whose information needs should seed everything
-- gets appended as the last row because it must go somewhere.

**Failure 2 -- Arbitrary-convention misreading**: You know echo belongs at the end. That is
not the problem. The problem is treating echo's row-0 position in the bilateral trace matrix
as a stylistic sort-order convention -- something you could change to row-1 or row-N. This
misreading severs the structural encoding of derivation direction. Echo occupies row 0 because
the chain begins from it: every Produces/Consumes pair is determined by working backward from
what echo must receive. Row 0 is where derivation begins, not where execution ends. Moving
echo to row N would invert the derivation direction in the artifact.

Every step below is a counter-move against one of these two failures. You will see which one
at each step heading. Every skill runs standalone; the program is a plan, not an executor.

To keep your plan auditable at every stage boundary, you will maintain three classes of
knowable information:

| Class | What you must keep knowable | Why it matters |
|-------|----------------------------|----------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before you open the catalog | Without this, zone is inferred from namespace grouping after the fact -- Failure 1 |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Without this, gates are prose checks with no traceable origin |
| **Investigative intent** | What question each phase answers -- not "what skills ran" but "what did we need to learn" | Without this, the plan is a skill roster, not an investigation structure |

**Lifecycle zones -- declare before opening the catalog:**
- **Breadth** -- do you understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does your design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test it.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template -- the expression that keeps artifact provenance knowable:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Three components in a single expression: `{stage-id}` names the producing stage; `>= N`
sets the count floor; `{namespace}:{skill}` traces to the catalog skill.

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

Required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** [counter: F-1] (Step 2)
3. Select skills from catalog [counter: F-1] (Step 3)
4. Assign skills to declared phases [counter: F-1] (Step 4)
5a. Design gates: compound lineage prefix format [counter: F-1] (Step 5a)
5b. FORWARD REFERENCE audit: verify gate artifact traceability [counter: F-1] (Step 5b)
6. Write per-phase intent questions: interrogative form required [counter: F-1] (Step 6)
7. Encode `evidence_arc:` field [counter: F-1] (Step 7)
8. Assemble YAML: echo at row 0 in ARTIFACT 2 [counter: F-2] (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. Everything else -- phase names, gate language, intent questions -- must
cohere with this topic.

---

#### Step 2 -- Declare Arc Phases [counter: F-1]

**Keep the catalog closed.** If you open it now, Failure 1 enters at Step 2: zone assignments
become retroactively shaped by catalog availability rather than declared investigative intent.
That is exactly what you are preventing. Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Ask: what investigative milestones must
the team reach? Assign each to a zone: `breadth`, `depth`, or `synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block` -- these are Failure 1 names

Phase declaration table:

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema** [counter: F-1 and F-2]. This is the
zeroth artifact, before any band taxonomy. It establishes the normative template all
subsequent artifacts instantiate:

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo; YAML annotations are transcribed from
the backward derivation, not authored from skill knowledge.

Echo exception [counter: F-2]: echo carries no # Band: annotation. You may wonder why echo
cannot be placed at row 1 or row N of ARTIFACT 2 -- its position is not a convention you are
free to vary. Echo's row-0 position is not an arbitrary convention; it is the structural
encoding of echo's anchor role: the derivation begins at echo and reads backward from there.
Row 0 is where derivation begins. Moving echo to row N would misrepresent the derivation
direction in the artifact. Omission of # Band: from echo is normative: echo is the derivation
anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition over used namespaces).

---

#### Step 3 -- Select Skills [counter: F-1]

Open the catalog now -- not before. Select skills relevant to the topic. Note the declared
phase each maps to.

---

#### Step 4 -- Assign Skills to Phases [counter: F-1]

Map each skill to its declared phase. If a skill doesn't match any phase, discard it. No new
phases. If you feel the urge to add a phase for an uncovered skill, that is Failure 1
re-entering: the catalog is shaping the arc rather than serving it.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format) [counter: F-1]

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must equal the stage's `name:` field exactly. `>= N` required. `{namespace}:{skill}`
required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (Failure 1 gate -- provenance unknowable): `adequate discovery signals present`
- FAIL (stage unknowable): `>= 3 scout artifacts present`
- FAIL (identity mismatch): `breadth::scout-feasibility >= 2` when `name: discovery`

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE audit [counter: F-1]

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. A gate that references an artifact from a skill not in
the stage is a forward reference -- it makes provenance unknowable. Fix before Step 6.

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
```

VALID:
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
```

---

#### Step 6 -- Phase Intent Questions [counter: F-1]

Intent questions are interrogative and zone-specific -- they answer "what did we need to learn?"
not "what skills ran?"

- PASS (breadth): `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS (depth): `"Does the spec survive expert review against the discovered market signal?"`
- PASS (synthesis): `"Are users adopting the feature at the rate our model predicted?"`
- FAIL: `"Assess the compliance landscape"` -- investigative intent unknowable; Failure 1 answer

---

#### Step 7 -- Evidence Arc Field [counter: F-1]

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML [counter: F-2]

You begin where the chain begins: what does echo need to receive? That question seeds the
backward derivation. Counter-move against Failure 2: that is why echo is row 0.

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Fill the matrix backward from echo. When your matrix rows are complete, look at the YAML
fragment column: you will notice it already contains every per-stage annotation your YAML
needs. This is not a coincidence -- the annotations were determined by the backward derivation.
**This column is the authoritative source -- transcribe from it directly, do not author YAML
annotations independently.** ARTIFACT 2 is the sole authoritative source; the YAML is a
downstream rendering of the matrix. If a cell is incomplete, complete it in ARTIFACT 2 first.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column, then add `phase:`, `intent:`, `skills:`,
and `gate:`):

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
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
      - <namespace>:<skill>
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
  - ...
  - name: echo
    auto: true
    skills: []
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Failure mode | Compliance |
|------------|-----------|--------------|------------|
| Phases declared by zone before catalog opens [F-1] | C-20 | Namespace-grouped phases -- zone membership retroactively shaped | Zone assignments locked in Step 2; catalog closed |
| Each phase has a phase-specific question ending with `?` [F-1] | C-12 | Generic "Are we done?" | Zone-specific question anchored to zone commitment |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` genuine interrogative? |
|-------|---------------------------------------|-------------------------------------|----------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-33: (same as V-01)
[ ] C-34: consumer-pull rule states BOTH negation AND equivalence simultaneously in ARTIFACT 0
[ ] C-35: ARTIFACT 2 YAML fragment column present; discovery framing ("already contains every
         annotation your YAML needs"); sole-source declaration present
[ ] C-36: ARTIFACT 0 echo exception contains explicit "not an arbitrary convention" contrastive
         clause in tutorial voice ("not a convention you are free to vary -- it is the structural
         encoding of echo's anchor role")
[ ] C-37: second-person opening names F-1 (catalog-first) and F-2 (arbitrary-convention) as
         two distinct failure modes with anatomy paragraphs; every CONSTRUCTION ORDER step
         heading carries `[counter: F-N]` inline tag; "every step below is a counter-move
         against one of these two failures" declared in opening
[ ] C-38: ARTIFACT 0 consumer-pull rule carries explicit bridge sentence: "The negation closes
         the producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
```

---

## V-05 -- Full Reference: Table + Manifest + Three Bridges

**Axes**: Combined (all mechanisms). Failure taxonomy table in opening (V-01 axis) + narrative
failure anatomy (V-04 axis) + dedicated COUNTER-MOVE MANIFEST table (V-02 axis) + inline step
tags on all construction steps (V-04 axis) + three explicit bridge sentences on three distinct
compound structural elements (V-03 axis). Maximum-strength implementation of C-37 and C-38.
Register: comprehensive formal reference.

**Hypothesis**: Maximum-strength implementation tests whether all C-37/C-38 mechanisms
compound their force or merely create redundancy. The three bridge sentences cover three
structural levels (ARTIFACT 0 consumer-pull, gate template, echo position); the three C-37
mechanisms (taxonomy table, manifest, inline tags) provide three independent audit paths for
the counter-move mapping. If any individual mechanism were removed, the criteria would still
pass -- meaning the output's compliance is load-bearing at every site. Anticipated score:
31/31 aspirational with maximum confidence margin.

**C-37 form**: Taxonomy table (opening) + narrative anatomy + COUNTER-MOVE MANIFEST section +
            inline `[counter: F-N]` tags on all construction step headings.
**C-38 form**: Three bridge sentences: (1) consumer-pull canonical, (2) gate template three-
            part structure, (3) echo row-0 + anchor-declaration compound.
**C-34 form**: Both negation AND equivalence in ARTIFACT 0 consumer-pull rule.
**C-35 form**: ARTIFACT 2 YAML fragment column + discovery framing + sole-source declaration.
**C-36 form**: ARTIFACT 0 echo exception: "not an arbitrary convention -- the misreading that
            echo could be placed at row N by convention is the failure mode this position
            forecloses."

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before writing a single stage,
internalize the two failure modes this protocol prevents. The table names them; the paragraphs
show how they occur:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied; gates are prose; echo appended as afterthought | Arc-before-catalog order: phases declared by zone with catalog closed; backward derivation from echo seeds every Produces/Consumes pair |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a sort-order choice, severing derivation direction from structural encoding | Row-0 position declared as causal consequence of echo's anchor role at two structural levels: opening and ARTIFACT 0 |

**Failure 1 -- Catalog-first construction**: Open the Signal catalog, cluster related skills
into stages, label each stage after its skill cluster. The result cannot be audited -- zone
membership is implied by namespace grouping rather than declared; gates are prose task-
completion checks rather than artifact contracts; phases answer "what skills ran here?" rather
than "what did we need to learn?" Echo is appended as a structural afterthought. Every step
in this protocol is a counter-move against Failure 1.

**Failure 2 -- Arbitrary-convention misreading**: Echo belongs at the end -- that is clear.
But its row-0 position in the bilateral trace matrix is treated as a layout convention, a
sort-order choice that could be row-1 or row-N with equal validity. This misreading severs
the structural encoding of derivation direction. Echo occupies row 0 because the entire
derivation chain begins from it: every Produces/Consumes pair is determined by working
backward from what echo must receive. Row 0 is where derivation begins; forward execution
reads the matrix bottom-to-top. Every rule touching echo's position is a counter-move against
Failure 2.

Every construction rule in this protocol is a counter-move against exactly one of these two
failures. The manifest below makes the mapping auditable:

**COUNTER-MOVE MANIFEST**

| Rule | Counter-move against | Structural effect |
|------|---------------------|-------------------|
| Phases declared by zone before catalog opens (Step 2) | F-1: catalog-first | Prevents zone assignments being retroactively shaped by namespace availability |
| Consumer-pull rule in ARTIFACT 0 (Step 2) | F-1: catalog-first | Produces determined by successor needs, not prior-stage skill output |
| Compound gate with stage-id prefix (Step 5a) | F-1: catalog-first | Artifact provenance traceable to named producing stage |
| FORWARD REFERENCE audit (Step 5b) | F-1: catalog-first | Gate artifact types verified against stage skills before transcription |
| ARTIFACT 2 sole authoritative source (Step 8) | F-1: catalog-first | YAML annotations transcribed from backward derivation, not authored independently |
| Echo at row 0 in ARTIFACT 2 (Step 8) | F-2: arbitrary-convention | Derivation direction encoded structurally; row 0 is derivation origin |
| Echo exception contrastive clause in ARTIFACT 0 (Step 2) | F-2: arbitrary-convention | Forecloses convention misreading at schema definition site |

Every skill runs standalone; the program is a plan, not an executor.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones** (zone-membership class):
- **Breadth** -- do we understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does our design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test the design.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template** (artifact-provenance class -- three-component single expression):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required.

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

Required construction sequence. Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** [counter: F-1] (Step 2)
3. Select skills from catalog [counter: F-1] (Step 3)
4. Assign skills to declared phases [counter: F-1] (Step 4)
5a. Design gates: compound lineage prefix format [counter: F-1] (Step 5a)
5b. FORWARD REFERENCE audit: verify gate artifact traceability [counter: F-1] (Step 5b)
6. Write per-phase intent questions: interrogative form required [counter: F-1] (Step 6)
7. Encode `evidence_arc:` field [counter: F-1] (Step 7)
8. Assemble YAML: echo at row 0 in ARTIFACT 2 [counter: F-2] (Step 8)
9. Per-stage compliance table: arc-structure / gate-behavior / question-framing ladders (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases [counter: F-1]

**The catalog must remain closed at this step.** Opening the catalog before phase declaration
infects the arc with skill availability bias -- zone assignments become retroactively shaped by
catalog availability rather than declared investigative intent. This is F-1 re-entering at
Step 2. Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Each phase is an investigative milestone.
Assign each to a zone: `breadth`, `depth`, or `synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

For each phase, state the investigative question it answers (genuine interrogative, ends `?`):

| Phase label | Zone | Investigative question |
|-------------|------|------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID this stage derives from -- e.g., B-01, G-02]
  # Gap:      [investigative question this stage answers, interrogative form, ends with ?]
  # Owner:    [functional role -- PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) this stage requires as input from the prior stage]
  # Produces: [artifact type(s) this stage yields as output for the next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously -- if you state what any stage consumes, what the prior stage must produce is
determined without further reasoning. The derivation runs backward from echo; YAML annotations
are transcribed from the backward derivation, not authored from skill knowledge.

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- the misreading that echo could be placed at row N
by convention is the failure mode this position forecloses. The row-0 position closes the
arbitrary-convention misreading; the derivation-anchor declaration makes the position self-
explaining from structural form alone: the derivation begins at echo and reads backward, every
Produces/Consumes pair determined by what each successor must receive, and row 0 is therefore
where the derivation trace begins -- not where execution ends. Omission of # Band: from echo
is normative: echo is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills [counter: F-1]

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases [counter: F-1]

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format) [counter: F-1]

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Three components in a single expression. The `{stage-id}::` prefix closes the artifact-
provenance ambiguity by naming the producing stage directly; the `>= N` count floor makes the
evidence bar independently verifiable without inspecting the stage's skills array. Together
they make every gate self-auditing from two orthogonal axes: which stage produced the artifact,
and how many artifacts constitute sufficient evidence.

`{stage-id}` must match `name:` exactly. `{artifact-type} >= N` is the count floor.
`AND {namespace}:{skill} artifact exists` provides skill-level traceability.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (F-1 gate -- provenance unknowable): `adequate discovery signals present`
- FAIL (stage unknowable): `>= 3 scout artifacts present`
- FAIL (identity mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit [counter: F-1]

A gate referencing an artifact from a skill not in the current stage makes artifact provenance
unknowable. For each non-echo stage: verify every artifact type in the gate is producible by
at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
```

VALID:
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
```

---

#### Step 6 -- Phase Intent Questions [counter: F-1]

- PASS (breadth): `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS (depth): `"Does the spec survive expert review against the discovered market signal?"`
- PASS (synthesis): `"Are users adopting the feature at the rate our model predicted?"`
- FAIL: `"Assess the compliance landscape"` -- investigative intent unknowable

---

#### Step 7 -- Evidence Arc Field [counter: F-1]

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML [counter: F-2]

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. Its implicit information needs seed the entire backward
derivation. That is why echo occupies row 0 -- the derivation reads top-to-bottom from echo;
forward execution reads bottom-to-top. See COUNTER-MOVE MANIFEST: this is the structural
counter-move against F-2.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently. The
matrix and YAML cannot diverge because YAML is defined as a downstream rendering of the
matrix. When your matrix rows are complete, look at the YAML fragment column: it already
contains every per-stage annotation your YAML needs -- the annotations were determined by the
backward derivation. If a matrix cell is incomplete, complete it in ARTIFACT 2 first.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, and `gate:` fields):

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
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
      - <namespace>:<skill>
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
  - ...
  - name: echo
    auto: true
    skills: []
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared by zone with catalog closed (counter-move against F-1) | C-20 (arc-structure) | Phase names echo namespace groups -- zone membership retroactively shaped; F-1 re-enters | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- investigative intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing (C-17): `intent:` genuine interrogative? |
|-------|-------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings, not one-skill-per-stage
[ ] C-07: gate language references artifact types or signal counts
[ ] C-08: stage names encode strategic purpose, not skill cluster labels
[ ] C-09: at least one gate with compound lineage prefix format and numeric threshold (>= N)
[ ] C-10: at least one gate is quantified
[ ] C-11: each stage frames an investigation question
[ ] C-12: phase ownership or role handoff made explicit
[ ] C-13: investigation question and gate are co-derived
[ ] C-14: every stage boundary has a bilateral artifact contract
[ ] C-15: investigation arc declared as named meta-structure (ARTIFACT 1 band taxonomy)
[ ] C-16: every non-echo stage has explicit role ownership (# Owner: annotation)
[ ] C-17: stage elements share a single referent (question / gate / produces all describe same gap)
[ ] C-18: all four per-stage annotations present on every non-echo stage
[ ] C-19: each stage carries traceable back-reference to meta-structure entry (# Band: B-NN)
[ ] C-20: meta-structure entries partition namespace set MECE
[ ] C-21: five-annotation schema declared as named template (ARTIFACT 0)
[ ] C-22: echo exception named within ARTIFACT 0
[ ] C-23: ARTIFACT 0 precedes ARTIFACT 1
[ ] C-24: consumer-pull rule declared as normative constraint
[ ] C-25: ARTIFACT 2 pre-YAML bilateral trace worksheet
[ ] C-26: echo declared as terminal consumer and derivation anchor
[ ] C-27: ARTIFACT 2 adjacent-column layout
[ ] C-28: echo at row 0 in ARTIFACT 2
[ ] C-29: ARTIFACT 1 carries ownership column
[ ] C-30: echo row-0 position declared as causal consequence of anchor role
[ ] C-31: echo causal anchor at two structural levels (failure taxonomy table opening + ARTIFACT 0)
[ ] C-32: consumer-pull rule states negation OR equivalence
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule states BOTH negation ("not by the prior stage's skill output
         inventory") AND bidirectional equivalence ("Equivalently: this stage produces the
         artifacts that close the next stage's input gap") simultaneously in same statement
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; discovery framing
         ("already contains every per-stage annotation your YAML needs"); sole-source
         declaration; column named as structural proof visible before any prose declaration
[ ] C-36: ARTIFACT 0 echo exception contains explicit contrastive clause naming and quoting
         the misreading it forecloses: "not an arbitrary convention -- the misreading that
         echo could be placed at row N by convention is the failure mode this position
         forecloses"
[ ] C-37: failure taxonomy table in opening names F-1 (catalog-first) and F-2 (arbitrary-
         convention) as two distinct failure IDs with counter-move column; narrative anatomy
         paragraphs follow; COUNTER-MOVE MANIFEST table maps all major rules to failure IDs;
         every CONSTRUCTION ORDER step heading carries `[counter: F-N]` inline tag; "every
         construction rule is a counter-move against exactly one of these two failures" declared
[ ] C-38: THREE explicit bridge sentences present for three compound structural elements:
         (1) ARTIFACT 0 consumer-pull: "The negation closes the producer-push misreading;
             the equivalence makes the rule self-verifying from both ends simultaneously"
         (2) Step 5a gate template: "The `{stage-id}::` prefix closes the artifact-provenance
             ambiguity by naming the producing stage directly; the `>= N` count floor makes
             the evidence bar independently verifiable without inspecting the stage's skills
             array"
         (3) ARTIFACT 0 echo exception: "The row-0 position closes the arbitrary-convention
             misreading; the derivation-anchor declaration makes the position self-explaining
             from structural form alone"
```
