---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 12
rubric: v12
total_pts: 240
golden_threshold: 220
new_criteria: C-34, C-35, C-36
---

# program-plan -- R12 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v12 (C-01 through C-36, 240 pts, golden >= 220).

**R11 retrospective under v12 rubric:**
- V-01 (Inertia-First Framing): 225/240 -- C-34 FAIL (negation only), C-35 FAIL (no YAML
  fragment column in matrix), C-36 FAIL ("its position encodes its anchor role structurally"
  -- structural language without explicit contrastive negation)
- V-02 (Tutorial Register): 225/240 -- C-34 FAIL (equivalence only), C-35 FAIL, C-36 FAIL
  ("that is why echo is row 0" -- causal connector, no contrastive clause)
- V-03 (Matrix-as-Rendering-Scaffold): 230/240 -- C-34 FAIL (negation only), C-35 PASS
  (YAML fragment column in ARTIFACT 2), C-36 FAIL ("That is why echo is row 0" -- causal
  connector, no contrastive clause)
- V-04 (Inertia-First + Tutorial Combined): 235/240 -- C-34 PASS (both forms), C-35 FAIL
  (sole-source declaration but no YAML fragment column in matrix table), C-36 PASS ("its
  row-0 position is a structural encoding of its anchor role, not an arbitrary convention")
- V-05 (Full Reference Implementation): 235/240 -- C-34 PASS (both forms), C-35 PASS (YAML
  fragment column + sole-source + discovery framing), C-36 FAIL ("its position encodes its
  anchor role structurally" -- "structurally" is implicit, no explicit contrastive negation)

**R12 design constraint:** All five variations must satisfy C-31 through C-36. C-34 (both
negation AND equivalence simultaneously in the same statement) is demonstrated by R11 V-04
and V-05. C-35 (YAML fragment column as structural proof of YAML derivation before any prose
declaration) is demonstrated by R11 V-03 and V-05. C-36 (tier-2 contrastive clause with
explicit "not an arbitrary convention" or equivalent in ARTIFACT 0 echo exception block) is
demonstrated only by R11 V-04. No R11 variant achieves all three simultaneously. R12 target:
every variant scores 240/240 by combining V-04's C-36 language, V-05's C-35 column, and
V-04/V-05's C-34 double form.

**Canonical C-34 language (ARTIFACT 0 consumer-pull rule -- both forms required):**
- Negation: "not by the prior stage's skill output inventory"
- Equivalence: "Equivalently: this stage produces the artifacts that close the next stage's
  input gap"
- Both must appear in the same statement (same paragraph/block)

**Canonical C-35 requirement (ARTIFACT 2 table):**
- Matrix table must include an explicit "YAML fragment" column (or equivalent labeled column)
- YAML must be visibly a rendered column of matrix rows before any declaration states it
- Sole-source declaration also required (C-33 preserved): "ARTIFACT 2 is the sole authoritative
  source; YAML annotations transcribed from matrix, not authored independently"

**Canonical C-36 language (ARTIFACT 0 echo exception -- tier-2 formulation):**
- Must include explicit contrastive negation foreclosing the arbitrary-convention misreading
- Canonical form (V-04): "its row-0 position is a structural encoding of its anchor role,
  not an arbitrary convention"
- Alternative forms: "not an arbitrary convention", "not a convention", "not a stylistic choice"
- Does NOT satisfy: structural language without explicit negation ("encodes its role
  structurally"); causal connectors without contrast ("that is why echo is row 0")

**Variation axes for R12:**
- V-01 (single): C-36 Contrastive-Clause Leading -- negation leads the ARTIFACT 0 echo
  block before any positive claim; compact formal register
- V-02 (single): C-36 Named ROW-0 RULE -- a labeled rule block in ARTIFACT 0 names and
  forecloses the misreading explicitly; formal/structured register
- V-03 (single): C-35 Column-as-Discovery Tutorial -- second-person tutorial voice frames
  YAML column as a discovery moment; C-36 in tutorial "why can't I move echo?" framing
- V-04 (combined): Failure Anatomy Names the Misreading -- opening anatomy explicitly
  catalogues "treating echo's row-0 as an arbitrary convention" as a named failure mode;
  ARTIFACT 0 closes it; inertia-first + tutorial register
- V-05 (full): Full Reference Implementation -- strongest formulation of all three criteria;
  C-34 bridge sentence, C-35 triple evidence, C-36 names and quotes the misreading

---

## V-01 -- C-36 Contrastive-Clause Leading

**Axis**: C-36 Contrastive-Clause Leading -- the echo exception block in ARTIFACT 0 leads
with the explicit negation before stating any positive claim: "Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer." The negative forecloses the competing misreading on first contact;
the positive follows as the correct reading. ARTIFACT 2 carries a YAML fragment column (C-35).
ARTIFACT 0 consumer-pull rule carries both negation and equivalence forms (C-34). Register:
compact formal/reference -- table-first preamble, minimal prose.

**Hypothesis**: Leading with the negation makes C-36 maximally unambiguous -- a reader cannot
mistake structural language for an explicit contrastive clause when the clause opens with
"not an arbitrary convention." The compact register tests whether all three new criteria
survive format compression. Anticipated score: 240/240.

**C-34 form**: Both negation AND bidirectional equivalence simultaneously.
**C-35 form**: YAML fragment column in ARTIFACT 2 + sole-source declaration.
**C-36 form**: Contrastive negation leads the ARTIFACT 0 echo exception block.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the
program is a plan, not an executor. The chain begins at the end: echo is the terminal consumer
whose implicit information needs seed the entire backward derivation that determines every
prior stage's Produces/Consumes pair. That is why echo is row 0 of the bilateral trace matrix
you will build in Step 8.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Arc-structure ladder (C-16 / C-18) |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder (C-09 / C-11) |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder (C-12 / C-17) |

**Lifecycle zones** (zone-membership class): **Breadth** -- problem-space understanding before
committing to direction; scout and draft skills. **Depth** -- adversarial stress-test before
committing to ship; prove, review, flow, trace skills. **Synthesis** -- post-launch signal
monitoring; listen, metrics, goals skills.

**Compound gate template** (artifact-provenance class):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required. Failure mode to prevent: **catalog-first construction** -- skill clustering
before zone declaration destroys all three classes simultaneously.

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
catalog availability rather than declared investigative intent, destroying zone membership as a
declared commitment. This is catalog-first construction re-entering at Step 2.

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

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The chain runs backward from
echo; YAML annotations are transcribed from the backward derivation, not authored from skill
knowledge.

Echo exception: echo carries no # Band: annotation. Echo's row-0 position in ARTIFACT 2 is
not an arbitrary convention -- it is the structural encoding of echo's anchor role as terminal
consumer. Echo's implicit information needs seed the entire backward derivation from which
every prior stage's Produces/Consumes pair is determined. Omission of # Band: from echo is
normative, not an oversight: echo is the derivation anchor, not a band member.
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

**Compound gate template** (named format convention -- artifact-provenance class):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `{artifact-type} >= N` is the count floor.
`AND {namespace}:{skill} artifact exists` provides skill-level traceability.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, no stage-id): `>= 3 scout artifacts present`
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
derivation. That is why echo occupies row 0 -- the derivation reads top-to-bottom from echo;
forward execution reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently. The
matrix and YAML cannot diverge because YAML is defined as a downstream rendering of the
matrix. If a matrix cell is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
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
| Phase boundaries declared by zone in Step 2, catalog closed | C-20 (arc-structure) | Phase names echo namespace groups -- zone membership retroactively shaped | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure Ladder (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior Ladder (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing Ladder (C-17): `intent:` genuine interrogative? |
|-------|---------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
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
[ ] C-20: meta-structure entries partition namespace set without overlap or gap (MECE)
[ ] C-21: five-annotation output schema declared as named stage template (ARTIFACT 0)
[ ] C-22: echo exception declared as normative rule within ARTIFACT 0 schema
[ ] C-23: ARTIFACT 0 schema precedes ARTIFACT 1 meta-structure in plan output
[ ] C-24: consumer-pull derivation direction declared as normative rule
[ ] C-25: pre-YAML ARTIFACT 2 bilateral trace worksheet makes contracts independently verifiable
[ ] C-26: echo declared as terminal consumer and backward-derivation anchor
[ ] C-27: ARTIFACT 2 uses adjacent-column layout (single-row bilateral verification)
[ ] C-28: echo occupies row 0 in ARTIFACT 2, encoding derivation direction structurally
[ ] C-29: ARTIFACT 1 meta-structure table carries ownership column
[ ] C-30: echo row-0 position declared as causal consequence of its anchor role
[ ] C-31: echo causal anchor claim present at two structural levels (opening paragraph + ARTIFACT 0)
[ ] C-32: consumer-pull rule states negation OR equivalence (closes producer-push misreading)
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML annotations transcribed from
         matrix cells, not authored independently
[ ] C-34: consumer-pull rule states BOTH negation ("not by the prior stage's skill output
         inventory") AND bidirectional equivalence ("Equivalently: this stage produces the
         artifacts that close the next stage's input gap") simultaneously in the same statement
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column, making YAML visibly
         a rendered projection of matrix rows before any prose declaration states the relationship
[ ] C-36: ARTIFACT 0 echo exception block contains explicit contrastive clause foreclosing the
         arbitrary-convention misreading: "not an arbitrary convention" or equivalent -- leading
         the block before any positive claim is stated
```

---

## V-02 -- C-36 Named ROW-0 RULE

**Axis**: C-36 Named ROW-0 RULE -- the ARTIFACT 0 echo exception block includes a labeled
"ROW-0 RULE:" subsection that names and forecloses the arbitrary-convention misreading as a
canonical design contract. The named rule makes C-36 impossible to satisfy via implicit
structural language -- the criterion has a labeled home. ARTIFACT 2 carries a YAML fragment
column (C-35). ARTIFACT 0 consumer-pull rule carries both forms (C-34). Register: formal/
structured with named rules and labeled subsections.

**Hypothesis**: Named-rule format makes C-36 structurally explicit and auditable: a labeled
block dedicated to foreclosing the misreading cannot be confused with structural description.
The checklist item has a named location. Anticipated score: 240/240.

**C-34 form**: Both negation AND bidirectional equivalence simultaneously.
**C-35 form**: YAML fragment column in ARTIFACT 2 + sole-source declaration.
**C-36 form**: Named "ROW-0 RULE:" block in ARTIFACT 0 with explicit contrastive negation.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the
program is a plan, not an executor. Echo is the terminal consumer: its implicit information
needs seed the entire backward derivation that determines every prior stage's Produces/Consumes
pair. That is why echo is row 0 of the bilateral trace matrix you will build in Step 8 --
the entire derivation chain reads backward from it.

The failure mode this protocol prevents: **catalog-first construction** -- opening the catalog
first, grouping skills into stages, labeling stages after their skill clusters. The result
cannot be audited: zone membership is implied by namespace grouping; gates are prose checks;
investigative intent is absent. Echo is appended as an afterthought rather than serving as
the derivation anchor from which every prior stage was backward-traced.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder (C-16 / C-18) |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder (C-09 / C-11) |
| **Investigative intent** | What question each phase answers -- declared per-stage | Question-framing ladder (C-12 / C-17) |

**Lifecycle zones** (zone-membership class):
- **Breadth** -- do we understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does our design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test the design before shipping commitment.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template** (artifact-provenance class):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` field exactly. `>= N` and
`{namespace}:{skill}` both required.

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
is complete infects the arc with skill availability bias -- zone assignments become retroactively
shaped by catalog availability rather than declared investigative intent.

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

Echo exception: echo carries no # Band: annotation.

  ROW-0 RULE: Echo's row-0 position in ARTIFACT 2 is not an arbitrary convention -- it is
  a design contract encoding derivation direction. Echo is the terminal consumer; the entire
  derivation chain begins from what echo must receive and works backward. Row 0 is where
  derivation begins, not where execution ends. The misreading that echo could be placed at
  row N by layout convention is what this rule forecloses. Moving echo to row N would
  misrepresent the derivation direction in the artifact. Omission of # Band: from echo is
  normative: echo is the derivation anchor, not a band member.
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

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

VALID:
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
```

FORWARD REFERENCE (fail -- `trace:deployment` not in this stage):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
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

Echo is the terminal consumer; its needs seed the backward derivation. That is why echo
occupies row 0 -- the derivation reads top-to-bottom from echo; execution reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column in ARTIFACT 2 is the authoritative form of the YAML annotation. Copy the YAML
fragment column directly to your stage YAML -- do not author YAML annotations outside this
matrix. The matrix and YAML cannot diverge because YAML is defined as a rendered column of
the matrix. If a cell is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, `gate:` fields):

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
| Phase boundaries declared by zone in Step 2, catalog closed | C-20 | Phase names echo namespace groups -- zone membership retroactively shaped | Phase map locked in Step 2; catalog not opened until Step 3 |
| Each phase has a phase-specific question ending with `?` | C-12 | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment |

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
[ ] C-34: consumer-pull rule states BOTH negation AND equivalence simultaneously
[ ] C-35: ARTIFACT 2 matrix contains explicit YAML fragment column (authoritative form)
[ ] C-36: ARTIFACT 0 echo exception contains named ROW-0 RULE block with explicit contrastive
         negation ("not an arbitrary convention -- it is a design contract encoding derivation
         direction")
```

---

## V-03 -- C-35 Column-as-Discovery (Tutorial Register)

**Axis**: Tutorial Register with Column-as-Discovery -- second-person voice throughout. C-35
is the focal discovery moment at ARTIFACT 2: "When you complete the matrix rows, you'll notice
the YAML fragment column already contains every annotation your YAML needs -- it was there the
moment you filled in the matrix." C-36 in tutorial "why can't I move echo?" voice: "You may
wonder why echo cannot be placed at row N -- its position is not a convention you are free to
vary; it is a structural constraint imposed by derivation direction." C-34 both forms in
ARTIFACT 0.

**Hypothesis**: Tutorial voice transforms C-35 from an obligation into a discovery -- the
reader finds that YAML derivation was already true, not that they must obey a new rule. C-36
as a "why can't I move echo?" question makes the contrastive clause feel naturally motivated
by genuine curiosity rather than arbitrary enforcement. Anticipated score: 240/240.

**C-34 form**: Both negation AND bidirectional equivalence simultaneously.
**C-35 form**: YAML fragment column + discovery narrative ("already contains everything").
**C-36 form**: Tutorial discovery -- "not a convention you are free to vary" in ARTIFACT 0.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before you write a single stage,
you need to understand where the chain begins -- and it begins at the end. Echo, the final
stage, is the terminal consumer: everything the plan produces ultimately flows to echo. Its
implicit information needs determine what the last stage must produce, which determines what
the second-to-last stage must produce, and so on backward to the first breadth stage. That is
why echo is row 0 of the bilateral trace matrix you will build -- the entire derivation reads
backward from it. Every skill runs standalone; the program is a plan, not an executor.

The failure mode to prevent: **catalog-first construction** -- opening the catalog first,
clustering skills into stages, labeling stages after their clusters. You cannot audit the
result. Zone membership is never declared; gates are prose; phases answer "what skills ran"
not "what we needed to learn."

To keep your plan auditable at every stage boundary, you will maintain three classes of
knowable information:

| Class | What you must keep knowable | Criterion ladder |
|-------|----------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before you open the catalog | Arc-structure ladder (C-16 / C-18) |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder (C-09 / C-11) |
| **Investigative intent** | What question each phase answers -- not "what skills ran" but "what did we need to learn" | Question-framing ladder (C-12 / C-17) |

**Lifecycle zones -- commit before opening the catalog:**
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

Three components in a single expression: `{stage-id}` names the producing stage; `>= N` sets
the artifact count floor; `{namespace}:{skill}` traces to the catalog skill.

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

State the topic name. Everything else derives from it.

---

#### Step 2 -- Declare Arc Phases

**Keep the catalog closed.** Here is why: if you open the catalog now and group skills into
stages, your zone assignments will be shaped by which skills happen to exist rather than what
you need to investigate. Zone membership will be implicit in namespace groupings rather than
declared as committed design choices. This is the catalog-first failure entering at Step 2.
Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Ask: what investigative milestones must
the team reach? Assign each phase to a zone: `breadth`, `depth`, or `synthesis`. Zone
assignment is a commitment -- it locks once the catalog opens in Step 3.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`

Phase declaration table:

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema.** This is the zeroth output artifact,
before any band taxonomy. It establishes the normative template that all subsequent artifacts
are instances of:

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The derivation runs backward
from what each stage needs to receive, not forward from what the prior stage happens to
generate.

Echo exception: echo carries no # Band: annotation. You may wonder why echo cannot be placed
at row 1 or row N of ARTIFACT 2 rather than row 0 -- its position is not an arbitrary
convention you are free to vary. Echo occupies row 0 because the derivation direction flows
from it: the chain begins at echo and works backward. Row 0 is where derivation begins.
Moving echo to row N would invert the derivation direction in the artifact, making the matrix
unreadable as a derivation trace. The row-0 position is a structural constraint imposed by
derivation direction, not a stylistic choice. Omission of # Band: from echo is normative:
it is the derivation anchor, not a band member.
```

After ARTIFACT 0, produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition over used namespaces).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must equal the stage's `name:` exactly. `>= N` required. `{namespace}:{skill}`
required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL (no prefix, no threshold): `adequate discovery signals`
- FAIL (threshold only): `>= 3 scout artifacts`
- FAIL (mismatch): `breadth::scout-feasibility >= 2` when `name: discovery`

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE audit

For each non-echo stage: verify that every artifact type in the gate is producible by at least
one skill in that stage's `skills` array. Fix all forward references before proceeding.

---

#### Step 6 -- Phase Intent Questions

Intent questions from Step 2 become `intent:` YAML fields. They must be interrogative:

- PASS: `"Do we understand the compliance landscape well enough to commit to a design?"`
- FAIL: `"Assess the compliance landscape"` -- investigative intent unknowable

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels]
  depth:     [depth-zone phase labels]
  synthesis: [synthesis-zone phase labels]
```

---

#### Step 8 -- Assemble YAML

You begin by asking what echo must receive. Echo is the terminal consumer -- its implicit
information needs are the starting point of the derivation. That is why echo is row 0.

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Fill the matrix backward from echo: what does the last stage need to produce (for echo to
receive)? What does the second-to-last stage produce (for the last stage to consume)?

When your matrix rows are complete, look at the YAML fragment column: you'll notice it already
contains every per-stage annotation your YAML needs. This isn't a coincidence -- the
annotations were determined by the backward derivation, not authored from skill knowledge.
**This column is the authoritative source -- transcribe from it directly, do not author YAML
annotations independently.** ARTIFACT 2 is the sole authoritative source; the YAML is a
downstream rendering of the matrix. The matrix and YAML cannot diverge because YAML is defined
as the rendered form of the YAML fragment column.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer -- derivation anchor) | -- | [what echo receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, and `gate:`):

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
| Phases declared by zone before catalog opens | C-20 | Namespace-grouped phases -- zone membership retroactively shaped | Zone assignments locked in Step 2; catalog closed |
| Each phase has a phase-specific question ending with `?` | C-12 | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` genuine interrogative? |
|-------|---------------------------------------|-------------------------------------|----------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-33: (same as V-01)
[ ] C-34: consumer-pull rule states BOTH negation AND equivalence simultaneously
[ ] C-35: ARTIFACT 2 YAML fragment column present; discovery framing ("you'll notice it already
         contains every per-stage annotation your YAML needs"); sole-source declaration
[ ] C-36: ARTIFACT 0 echo exception contains tutorial discovery framing with explicit contrastive
         clause ("not an arbitrary convention you are free to vary -- a structural constraint
         imposed by derivation direction")
```

---

## V-04 -- Failure Anatomy Names the Arbitrary-Convention Misreading (Combined)

**Axes**: Inertia-First (V-01 R11 axis) + Tutorial Register (V-02 R11 axis) -- the catalog-
first failure anatomy opens the document in tutorial voice. C-36 is integrated into the failure
anatomy itself: "treating echo's row-0 position as an arbitrary stylistic convention" is named
as a distinct failure mode alongside catalog-first construction. ARTIFACT 0 closes it as a
named counter-move with explicit "not an arbitrary convention" language. ARTIFACT 2 carries
YAML fragment column (C-35). ARTIFACT 0 consumer-pull rule carries both forms (C-34).

**Hypothesis**: When "treating echo's row-0 as an arbitrary convention" is named as a failure
mode in the opening anatomy, the ARTIFACT 0 "not an arbitrary convention" clause reads as the
direct counter-move against that named failure -- giving C-36 maximum motivation and making
the contrastive clause structurally load-bearing rather than incidental. Anticipated score:
240/240.

**C-34 form**: Both negation AND bidirectional equivalence simultaneously.
**C-35 form**: YAML fragment column + sole-source declaration.
**C-36 form**: Named failure mode in opening; ARTIFACT 0 closes with explicit contrastive clause.

---

### FULL PROMPT BODY

Before you write a single stage, understand the two failure modes this protocol is designed
to prevent.

**Failure 1 -- Catalog-first construction**: You open the Signal skill catalog, group related
skills into stages, and label each stage after its skill cluster. You cannot audit the result
-- zone membership is implied by namespace grouping rather than declared; gates are prose
task-completion checks rather than artifact contracts; phases answer "what skills ran here?"
rather than "what did we need to learn?" Echo, the terminal consumer whose information needs
should seed the entire backward derivation, gets appended as a structural afterthought.

**Failure 2 -- Arbitrary-convention misreading**: You recognize that echo belongs at the end,
but you treat its row-0 position in the bilateral trace matrix as a stylistic layout convention
-- a sort-order choice that could be row-1 or row-N just as well. This misreading severs the
structural encoding of derivation direction. Echo is at row 0 not by convention but because
the derivation reads from it: every Produces/Consumes pair is determined by working backward
from what echo must receive. Row 0 is where derivation begins.

Every rule in this protocol is a counter-move against one of these two failure modes. Echo's
anchor role -- counter-move against Failure 2 -- is why echo is row 0 of the bilateral trace
matrix you will build in Step 8. Every skill runs standalone; the program is a plan, not an
executor.

To keep your plan auditable at every stage boundary, you will maintain three classes of
knowable information:

| Class | What you must keep knowable | Criterion ladder |
|-------|----------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before you open the catalog | Arc-structure ladder (C-16 / C-18) |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder (C-09 / C-11) |
| **Investigative intent** | What question each phase answers -- not "what skills ran" but "what did we need to learn" | Question-framing ladder (C-12 / C-17) |

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

Three components in a single expression. `{stage-id}` must match the stage's `name:` exactly.
`>= N` and `{namespace}:{skill}` both required.

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

State the topic name. All artifact names and phase groupings must cohere with this topic.

---

#### Step 2 -- Declare Arc Phases

**Keep the catalog closed -- here is why this matters.** If you open the catalog now,
Failure 1 enters at Step 2: phase boundaries will be shaped by which skills happen to exist
rather than what you need to investigate. Zone assignments will be implicit in namespace
groupings rather than declared. Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`. Zone assignment is a commitment -- it locks once the catalog opens in Step 3.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`

Phase declaration table:

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema.** This is the zeroth artifact -- the
schema is the contract; all subsequent artifacts are instances of it:

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-03]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The derivation runs backward
from echo; YAML annotations are transcribed from the backward derivation, not authored from
skill knowledge.

Echo exception: echo carries no # Band: annotation. Counter-move against Failure 2: echo's
row-0 position in ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding
of echo's role as terminal consumer and derivation anchor. The entire Produces/Consumes chain
is determined by working backward from what echo must receive; row 0 is where that derivation
begins. Placing echo at any other row would misrepresent the derivation direction. Omission
of # Band: from echo is normative: echo is the anchor node, not a band member.
```

After ARTIFACT 0, produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must equal the stage's `name:` field. `>= N` required. `{namespace}:{skill}`
required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL (Failure 1 at gate level): `adequate discovery signals`
- FAIL (producing stage unknowable): `>= 3 scout artifacts`
- FAIL (identity unknowable): `breadth::scout-feasibility >= 2` when `name: discovery`

At least one gate must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

A FORWARD REFERENCE cites an artifact from a skill not present in this stage -- Failure 1
re-enters at gate level. For each non-echo stage: verify every artifact type in the gate is
producible by a skill in that stage's `skills` array.

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
- PASS (depth): `"Does the spec survive expert review against the market signal?"`
- PASS (synthesis): `"Are users adopting at the rate our model predicted?"`
- FAIL: `"Assess compliance landscape"` -- investigative intent unknowable

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels]
  depth:     [depth-zone phase labels]
  synthesis: [synthesis-zone phase labels]
```

---

#### Step 8 -- Assemble YAML

You begin where the chain begins: what does echo need to receive? Echo is the terminal consumer;
its information needs are the starting point of the backward derivation. Counter-move against
Failure 2: that is why echo is row 0.

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Fill each row backward from echo. **ARTIFACT 2 is the sole authoritative source for all
per-stage annotations.** The YAML fragment column is the authoritative form of the YAML
annotation -- copy it directly to your stage YAML. Do not author YAML annotations outside this
matrix. The matrix and YAML cannot diverge because YAML is defined as a downstream rendering
of the matrix. If a cell is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer -- derivation anchor) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, `gate:` fields):

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
| Phase boundaries declared by zone in Step 2, catalog closed (counter-move against Failure 1) | C-20 | Phase names echo namespace groups -- Failure 1 re-enters | Phase map locked in Step 2; catalog not opened until Step 3 |
| Each phase has a phase-specific question ending with `?` | C-12 | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure Ladder (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior Ladder (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing Ladder (C-17): `intent:` genuine interrogative? |
|-------|---------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
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
[ ] C-17: stage elements share a single referent
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
[ ] C-31: echo causal anchor at two structural levels (failure anatomy opening + ARTIFACT 0)
[ ] C-32: consumer-pull rule states negation OR equivalence
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule states BOTH negation AND equivalence simultaneously
[ ] C-35: ARTIFACT 2 matrix contains explicit YAML fragment column
[ ] C-36: ARTIFACT 0 echo exception block contains explicit contrastive clause ("not an
         arbitrary convention -- it is the structural encoding of echo's role as terminal
         consumer and derivation anchor" -- counter-move against Failure 2 named in opening)
```

---

## V-05 -- Full Reference Implementation (R12)

**Axes**: All -- Inertia-First + Tutorial + Matrix-as-Rendering-Scaffold + Failure Anatomy
Names the Misreading. Every new criterion receives its strongest possible formulation:
C-34 gets a bridge sentence explicitly explaining why both forms are present; C-35 gets
the YAML fragment column plus discovery framing plus explicit sole-source declaration plus
commentary naming the column as structural proof before any declaration; C-36 gets the
explicit "not an arbitrary convention" phrase plus elaboration naming and quoting the
competing misreading.

**Hypothesis**: Maximum explicitness and redundancy on all three new criteria. C-34: bridge
sentence makes the dual-form intentional, not incidental. C-35: three independent lines of
evidence (column structure, discovery moment, explicit sole-source declaration). C-36: names
and quotes the misreading it forecloses. No criterion depends on inference. Anticipated score:
240/240 with maximum confidence.

**C-34 form**: Both forms with bridge sentence: "The negation closes the producer-push
              misreading; the equivalence makes the rule self-verifying from both ends
              simultaneously."
**C-35 form**: YAML fragment column + discovery framing ("already contains everything") +
              explicit sole-source declaration + commentary naming column as structural proof.
**C-36 form**: Explicit "not an arbitrary convention" + quotes the misreading being foreclosed
              ("the misreading that echo could be placed at row N by convention").

---

### FULL PROMPT BODY

Before you write a single stage, understand what you are preventing. Two failure modes govern
this protocol.

**Failure 1 -- Catalog-first construction**: Open the Signal catalog, cluster related skills
into stages, label each stage after its skill cluster. The result cannot be audited -- zone
membership implied by namespace grouping, not declared; gates are prose; phases answer "what
skills ran" not "what we needed to learn." Echo is appended as an afterthought. Every step in
this protocol is a counter-move against Failure 1.

**Failure 2 -- Arbitrary-convention misreading**: Echo belongs at the end -- that is clear.
But its row-0 position in the bilateral trace matrix is treated as a layout convention, a
sort-order choice that could be row-1 or row-N just as well. This misreading severs the
structural encoding of derivation direction. Echo occupies row 0 because the derivation chain
begins from it: every Produces/Consumes pair is determined by working backward from what echo
must receive. Row 0 is where derivation begins; execution reads the matrix bottom-to-top. The
row-0 position is a structural constraint, not a convention. Counter-move against Failure 2
appears in the opening, in ARTIFACT 0, and structurally in the row-0 position of ARTIFACT 2.

Three classes of information must remain knowable at every stage boundary:

| Class | What you must keep knowable | Criterion ladder |
|-------|----------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before you open the catalog | Arc-structure ladder (C-16 / C-18) |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder (C-09 / C-11) |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder (C-12 / C-17) |

**Lifecycle zones:**
- **Breadth** -- do you understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does your design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test it before you commit to ship.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template** (artifact-provenance class -- single expression):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Three components: `{stage-id}` names the producing stage (must match `name:` exactly);
`>= N` sets the count floor; `{namespace}:{skill}` traces to the catalog skill.

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

State the topic name. All artifact names and phase groupings must cohere with this topic.

---

#### Step 2 -- Declare Arc Phases

**Keep the catalog closed.** If you open it now, Failure 1 enters at Step 2: zone assignments
become retroactively shaped by catalog availability rather than declared investigative intent.
Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`. Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`

Phase declaration table:

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema** (zeroth artifact, before band taxonomy):

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-03]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The negation closes the
producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo.

Echo exception: echo carries no # Band: annotation. Counter-move against Failure 2: echo's
row-0 position in ARTIFACT 2 is not an arbitrary convention -- the misreading that echo could
be placed at row N by convention is the failure mode this position forecloses. Echo occupies
row 0 because the derivation reads from it: every Produces/Consumes pair in the chain is
determined by working backward from what echo must receive. Row 0 is where derivation begins;
the matrix is read derivation-first (top-to-bottom), not execution-first (bottom-to-top). The
row-0 position encodes echo's anchor role structurally. Omission of # Band: from echo is
normative: it is the derivation anchor, not a band member.
```

After ARTIFACT 0, produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition over used namespaces).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must equal the stage's `name:` field. `>= N` required. `{namespace}:{skill}`
required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (Failure 1 at gate): `adequate discovery signals`
- FAIL (producing stage unknowable): `>= 3 scout artifacts`
- FAIL (identity unknowable): `breadth::scout-feasibility >= 2` when `name: discovery`

At least one gate must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

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
- PASS (synthesis): `"Are users adopting at the rate our model predicted?"`
- FAIL: `"Assess compliance landscape"` -- investigative intent unknowable

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

You begin where the chain begins: what does echo need to receive? Counter-move against Failure
2: that is why echo is row 0.

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Fill the matrix backward from echo. When your matrix rows are complete, look at the YAML
fragment column: it already contains every per-stage annotation your YAML needs. This is not
a coincidence -- the annotations were determined by the backward derivation. The YAML fragment
column is the structural proof that YAML is a rendered projection of the matrix, visible before
any declaration states the relationship.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly to your
stage YAML. Do not author YAML annotations outside this matrix. The matrix and YAML cannot
diverge because YAML is defined as the rendered form of the YAML fragment column. If a cell
is incomplete, complete it in ARTIFACT 2 first, then transcribe.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer -- derivation anchor) | -- | [what echo receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

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
    # Band:     <from ARTIFACT 2 YAML fragment column>
    # Gap:      <from ARTIFACT 2 YAML fragment column>
    # Owner:    <from ARTIFACT 2 YAML fragment column>
    # Consumes: <from ARTIFACT 2 YAML fragment column>
    # Produces: <from ARTIFACT 2 YAML fragment column>
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
| Phase boundaries declared by zone in Step 2, catalog closed (counter-move against Failure 1) | C-20 (arc-structure) | Phase names echo namespace groups -- zone membership retroactively shaped; Failure 1 re-enters | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific investigative question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- investigative intent unknowable | Phase-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure Ladder (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior Ladder (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing Ladder (C-17): `intent:` genuine interrogative? |
|-------|---------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
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
[ ] C-31: echo causal anchor at two structural levels (Failure 2 framing in opening + ARTIFACT 0)
[ ] C-32: consumer-pull rule states negation OR equivalence
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule states BOTH negation ("not by the prior stage's skill output
         inventory") AND bidirectional equivalence ("Equivalently: this stage produces the
         artifacts that close the next stage's input gap") simultaneously; bridge sentence
         present: "The negation closes the producer-push misreading; the equivalence makes
         the rule self-verifying from both ends simultaneously."
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; discovery framing
         ("already contains every per-stage annotation your YAML needs"); sole-source
         declaration; column named as structural proof visible before any prose declaration
[ ] C-36: ARTIFACT 0 echo exception block contains explicit contrastive clause naming and
         quoting the misreading it forecloses: "not an arbitrary convention -- the misreading
         that echo could be placed at row N by convention is the failure mode this position
         forecloses"
```
