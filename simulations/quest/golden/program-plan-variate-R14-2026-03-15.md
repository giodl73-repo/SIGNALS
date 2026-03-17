---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 14
rubric: v30
aspirational_target: 33/33
new_criteria: C-39, C-40
---

# program-plan -- R14 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v30 (C-01 through C-40, 33 aspirational criteria).

**R13 retrospective under v30 rubric:**
- V-01 (Failure Taxonomy Table Opening): 33/33 aspirational -- C-39 PASS (taxonomy table
  with "every construction rule is a counter-move against exactly one row" = completeness
  assertion; table is the dedicated structure), C-40 PASS (`[counter: F-1]`/`[counter: F-2]`
  inline on both ARTIFACT 0 rules)
- V-02 (Counter-Move Manifest Section): 32/33 -- C-39 PASS (7-row COUNTER-MOVE MANIFEST with
  failure IDs), C-40 FAIL (ARTIFACT 0 rules have no inline `[counter: FN]` -- remote manifest
  satisfies C-39 but inline annotation is required separately for C-40)
- V-03 (Three Bridge Sentences): 32/33 -- C-40 PASS (`[counter: Failure 1]`/`[counter: Failure 2]`
  inline on ARTIFACT 0 rules), C-39 FAIL (narrative "every step is a counter-move" without
  a dedicated table/list enumerating ALL rules individually)
- V-04/V-05: same respective failures as V-02/V-03

**R14 design constraint:** All five variations must satisfy BOTH C-39 AND C-40 simultaneously.
- C-39: a dedicated structure (table, list, or named block) enumerating ALL protocol rules
  (not a sample), each mapped to a named failure ID, with an explicit completeness assertion
  ("this table is exhaustive" or equivalent)
- C-40: EVERY rule in ARTIFACT 0 carries an inline `[counter: F-N]` annotation at its
  definition site -- both consumer-pull rule AND echo exception, exhaustively
- C-39 and C-40 are orthogonal: remote manifest satisfies C-39 but not C-40; inline labels
  satisfy C-40 but not C-39; BOTH structures must co-exist in every variation

**Canonical C-39 rule set (7 rules -- exhaustive):**
- R-01: Phases declared by zone before catalog opens | counter: F-1
- R-02: Consumer-pull derivation direction (ARTIFACT 0) | counter: F-1
- R-03: Compound gate with stage-id lineage prefix (Step 5a) | counter: F-1
- R-04: FORWARD REFERENCE audit (Step 5b) | counter: F-1
- R-05: ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix | counter: F-1
- R-06: Echo at row 0 in ARTIFACT 2 | counter: F-2
- R-07: Echo exception contrastive clause in ARTIFACT 0 | counter: F-2

**Canonical C-40 requirements (ARTIFACT 0 rules, exhaustive):**
- Consumer-pull rule: `[counter: F-1]` inline at definition site
- Echo exception: `[counter: F-2]` inline at definition site
- Both present; neither omitted

**Variation axes for R14:**
- V-01 (single): Output Format -- Dual-Structure Coverage: opening failure taxonomy table
  (2 rows, failure->rule direction) PLUS a 7-row RULE COVERAGE TABLE (rule->failure
  direction); both carry completeness assertions; bidirectional auditing
- V-02 (single): Lifecycle Emphasis -- Zone Commitment Tests: each zone gets 3-condition
  commitment criteria before the catalog opens; C-39 via opening taxonomy table + coverage
  table; zone structure receives significantly expanded treatment
- V-03 (single): Inertia Framing -- Status-Quo Column: coverage table adds "Status-Quo Path"
  column showing what catalog-first construction produces at each decision point; every rule
  is framed as counter to a named inertia behavior
- V-04 (combined): Role Sequence + Output Format: role-responsibility table precedes failure
  taxonomy; C-39 as numbered RULE REGISTRY (named list, not table) with completeness
  assertion; step headers carry role attribution
- V-05 (combined): Phrasing Register + Inertia Framing: second-person imperative throughout;
  each step has explicit AVOID block naming the inertia path; C-39 as COUNTER-MOVE MANIFEST
  (table); C-40 unchanged

---

## V-01 -- Output Format: Dual-Structure Coverage

**Axis**: Single-axis. Two dedicated structures jointly satisfy C-39: (1) the opening 2-row
failure taxonomy table (failure->rule direction, with counter-move column) and (2) a 7-row
RULE COVERAGE TABLE (rule->failure direction, one row per protocol rule). Both tables carry
independent completeness assertions. The bidirectional structure makes C-39 auditable from
either direction without interpretation: enumerate all failures (2 rows) or enumerate all
rules (7 rows) -- both yield the same coverage claim. C-40: both ARTIFACT 0 rules carry
`[counter: F-N]` inline. C-38: canonical consumer-pull bridge sentence.

**Hypothesis**: Two complementary coverage structures (failure-first and rule-first) make
C-39 a structural invariant. A scorer verifies completeness from either direction without
interpretation: count the failure rows (2) or count the rule rows (7) -- coverage is auditable
from either axis. C-40 remains independent because ARTIFACT 0 inline labels are orthogonal
to the opening tables. Anticipated score: 33/33 aspirational.

**C-39 form**: Opening failure taxonomy table (2 rows) + RULE COVERAGE TABLE (7 rows, R-01
             through R-07); completeness assertion on the rule table: "This table is
             exhaustive: every construction rule in this protocol appears as exactly one row"
**C-40 form**: ARTIFACT 0 consumer-pull rule `[counter: F-1]`; echo exception `[counter: F-2]`;
             both inline at definition site, exhaustive
**C-37 form**: Opening taxonomy table + "every rule is a counter-move against exactly one
             row" + `[counter: F-N]` in ARTIFACT 0
**C-38 form**: Canonical consumer-pull bridge sentence in ARTIFACT 0
**C-34 form**: BOTH negation AND bidirectional equivalence in consumer-pull rule
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-36 form**: "not an arbitrary convention" contrastive clause leading echo exception block

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before writing a single stage,
internalize the two failure modes this protocol is designed to prevent:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied by namespace grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted.

**RULE COVERAGE TABLE**

| Rule ID | Rule | Counter-move against | Structural effect |
|---------|------|---------------------|-------------------|
| R-01 | Phases declared by zone before catalog opens (Step 2) | F-1: catalog-first | Prevents zone assignments retroactively shaped by namespace availability |
| R-02 | Consumer-pull derivation direction in ARTIFACT 0 | F-1: catalog-first | Forces Produces/Consumes pairs determined by successor needs, not prior-stage skill output |
| R-03 | Compound gate with stage-id lineage prefix (Step 5a) | F-1: catalog-first | Makes artifact provenance traceable to named producing stage, not inferred from gate prose |
| R-04 | FORWARD REFERENCE audit (Step 5b) | F-1: catalog-first | Gate artifacts verified against stage skills array; provenance remains knowable |
| R-05 | ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix (Step 8) | F-1: catalog-first | YAML annotations derived from backward derivation, not authored from skill knowledge |
| R-06 | Echo at row 0 in ARTIFACT 2 (Step 8) | F-2: arbitrary-convention | Encodes derivation direction structurally; row 0 is derivation origin, not execution end |
| R-07 | Echo exception contrastive clause in ARTIFACT 0 (Step 2) | F-2: arbitrary-convention | Forecloses convention misreading at schema definition site, before any YAML is written |

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
         artifacts that close the next stage's input gap") simultaneously
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; sole-source
         declaration present; column visible as rendered projection before any prose declaration
[ ] C-36: ARTIFACT 0 echo exception contains explicit contrastive clause: "not an arbitrary
         convention -- it is the structural encoding of echo's anchor role as terminal consumer"
         leading the block before any positive claim
[ ] C-37: opening failure taxonomy table names F-1 and F-2 with counter-move column; "every
         construction rule in this protocol is a counter-move against exactly one row in this
         table" present; ARTIFACT 0 rules carry `[counter: F-N]` labels
[ ] C-38: ARTIFACT 0 consumer-pull rule carries bridge sentence: "The negation closes the
         producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
[ ] C-39: RULE COVERAGE TABLE present (7 rows, R-01 through R-07); ALL protocol rules
         enumerated; each mapped to a failure ID (F-1 or F-2); completeness assertion: "This
         table is exhaustive: every construction rule in this protocol appears as exactly one
         row. No rule is omitted."
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline at definition site;
         ARTIFACT 0 echo exception carries `[counter: F-2]` inline at definition site; both
         present; no ARTIFACT 0 rule unlabeled
```

---

## V-02 -- Lifecycle Emphasis: Zone Commitment Tests

**Axis**: Single-axis. Each lifecycle zone receives explicit 3-condition commitment criteria:
(a) the zone-exit question that must be answered, (b) the minimum artifact types that must
exist as evidence, (c) the gate-pattern class the final stage in the zone must satisfy. These
criteria are declared before the catalog opens and anchor zone-level auditing. C-39 via opening
failure taxonomy table + 7-row RULE COVERAGE TABLE. C-40 via ARTIFACT 0 inline labels. The
zone commitment section is new material that does not appear in V-01. Register: structured formal.

**Hypothesis**: Zone commitment tests make the lifecycle boundaries independently verifiable
at two granularities: per-stage compound gates AND zone-level commitment criteria. This should
not interfere with C-39/C-40 because those criteria attach to the opening framing and ARTIFACT 0
respectively. The expanded zone treatment may improve C-20 pass rates by making zone membership
criteria explicit. Anticipated score: 33/33 aspirational.

**C-39 form**: Same as V-01 -- opening taxonomy table + RULE COVERAGE TABLE (7 rows) +
             completeness assertion
**C-40 form**: ARTIFACT 0 `[counter: F-1]` on consumer-pull; `[counter: F-2]` on echo
             exception; both inline, exhaustive
**C-37 form**: Standard -- taxonomy table + "every rule is a counter-move against exactly
             one row" + `[counter: F-N]` in ARTIFACT 0
**C-38 form**: Canonical consumer-pull bridge sentence
**C-34 form**: BOTH negation AND bidirectional equivalence
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-36 form**: "not an arbitrary convention" contrastive clause

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before writing a single stage,
internalize the two failure modes this protocol is designed to prevent:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied by namespace grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted.

**RULE COVERAGE TABLE**

| Rule ID | Rule | Counter-move against | Structural effect |
|---------|------|---------------------|-------------------|
| R-01 | Phases declared by zone before catalog opens (Step 2) | F-1: catalog-first | Prevents zone assignments retroactively shaped by namespace availability |
| R-02 | Consumer-pull derivation direction in ARTIFACT 0 | F-1: catalog-first | Forces Produces/Consumes pairs determined by successor needs, not prior-stage skill output |
| R-03 | Compound gate with stage-id lineage prefix (Step 5a) | F-1: catalog-first | Makes artifact provenance traceable to named producing stage, not inferred from gate prose |
| R-04 | FORWARD REFERENCE audit (Step 5b) | F-1: catalog-first | Gate artifacts verified against stage skills array; provenance remains knowable |
| R-05 | ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix (Step 8) | F-1: catalog-first | YAML annotations derived from backward derivation, not authored from skill knowledge |
| R-06 | Echo at row 0 in ARTIFACT 2 (Step 8) | F-2: arbitrary-convention | Encodes derivation direction structurally; row 0 is derivation origin, not execution end |
| R-07 | Echo exception contrastive clause in ARTIFACT 0 (Step 2) | F-2: arbitrary-convention | Forecloses convention misreading at schema definition site, before any YAML is written |

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones with commitment criteria** (zone-membership class):

**Breadth zone** -- do we understand the problem space well enough to commit to a direction?
Scout and draft skills produce breadth artifacts.

Breadth zone commitment criteria (all three must be satisfied before advancing to depth):
1. Zone-exit question answered: "Have we named the problem space, identified key constraints,
   and committed to a direction without relying on solution-space knowledge?"
2. Minimum artifact types present: at least one competitor or market signal artifact, at least
   one feasibility artifact, at least one draft artifact (spec or proposal)
3. Gate pattern required: at least one compound gate with `>= 2` count floor on a scout or
   draft skill artifact from this stage

**Depth zone** -- does our design survive adversarial conditions before shipping commitment?
Prove, review, flow, and trace skills stress-test the design.

Depth zone commitment criteria (all three must be satisfied before advancing to synthesis):
1. Zone-exit question answered: "Has the design been tested against failure modes, edge cases,
   and adversarial conditions by reviewers who did not author the spec?"
2. Minimum artifact types present: at least one review artifact, at least one flow or trace
   artifact, at least one prove artifact
3. Gate pattern required: at least one compound gate referencing a review or prove skill
   with `>= 2` count floor

**Synthesis zone** -- are users adopting and signaling as expected post-launch?
Listen, metrics, and goals skills monitor post-launch reality.

Synthesis zone commitment criteria (all three must be satisfied before echo advances):
1. Zone-exit question answered: "Are post-launch signals tracking against the adoption model
   the team committed to before shipping?"
2. Minimum artifact types present: at least one listen artifact, at least one metrics or
   goals artifact
3. Gate pattern required: compound gate with count floor on a listen, metrics, or goals skill

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

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

**The catalog must remain closed at this step.** Opening the catalog before phase declaration
infects the arc with skill availability bias -- zone assignments become retroactively shaped by
catalog availability rather than declared investigative intent. This is F-1 re-entering at
Step 2. Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Assign each to a zone using the
commitment criteria defined above -- the criteria serve as the zone assignment test, not
namespace grouping.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

For each phase, state the investigative question it answers (genuine interrogative, ends `?`).
Include a zone commitment check:

| Phase label | Zone | Investigative question | Zone commitment check |
|-------------|------|------------------------|-----------------------|
| [name] | breadth/depth/synthesis | [...?] | [Which commitment criteria does this phase address?] |

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

Open the catalog. Select skills relevant to the topic. Verify each selected skill satisfies
the minimum artifact type requirements for its zone's commitment criteria -- not just namespace
grouping. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
After assigning, verify the zone's commitment criteria are satisfiable by the assigned skills
(minimum artifact types present for each zone).

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors should be calibrated to zone commitment
criteria: breadth and depth stages require `>= 2` for commitment-bearing artifacts; synthesis
stages require `>= 1`.

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

Every phase from Step 2 must appear in exactly one arc key. Verify each zone's commitment
criteria are satisfiable given the phase labels and skills assigned.

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
[ ] C-01 through C-38: (same as V-01)
[ ] C-39: RULE COVERAGE TABLE present (7 rows, R-01 through R-07); ALL protocol rules
         enumerated; each mapped to a failure ID; completeness assertion: "This table is
         exhaustive: every construction rule in this protocol appears as exactly one row.
         No rule is omitted."
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline at definition site;
         ARTIFACT 0 echo exception carries `[counter: F-2]` inline at definition site;
         both present; no ARTIFACT 0 rule unlabeled
```

---

## V-03 -- Inertia Framing: Status-Quo Competitor Column

**Axis**: Single-axis. The status-quo path (catalog-first, convention-following construction)
is named as a competitor at every structural decision point. The RULE COVERAGE TABLE gains a
"Status-Quo Path" column showing what a naive construction produces at each decision. Every
rule is framed as a deliberate choice against a named inertia behavior, not just against an
abstract failure mode ID. C-39 via opening failure taxonomy table + 3-column RULE COVERAGE
TABLE with completeness assertion. C-40 via ARTIFACT 0 inline labels (ARTIFACT 0 echo
exception adds an anti-inertia sentence alongside the `[counter: F-2]` label). Register:
technical-persuasive.

**Hypothesis**: The status-quo column makes the design rationale visible at the point of each
rule, answering "why not just do the obvious thing?" inline without requiring a separate
explanation section. C-39 is strengthened because the completeness assertion covers three
columns; C-40 is unchanged. The ARTIFACT 0 anti-inertia framing may improve C-31 and C-36
scores by making the counter-convention logic more explicit. Anticipated score: 33/33
aspirational.

**C-39 form**: 3-column RULE COVERAGE TABLE (Status-Quo Path | Rule | Failure countered);
             7 rows (R-01 through R-07); completeness assertion: "This table is exhaustive:
             every construction rule in this protocol appears as exactly one row"
**C-40 form**: ARTIFACT 0 consumer-pull `[counter: F-1]`; echo exception `[counter: F-2]`;
             both inline at definition site, exhaustive
**C-37 form**: Opening failure taxonomy table + "every rule is a counter-move against exactly
             one row" + `[counter: F-N]` in ARTIFACT 0
**C-38 form**: Canonical consumer-pull bridge sentence
**C-34 form**: BOTH negation AND equivalence in consumer-pull rule
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-36 form**: Echo exception with "not an arbitrary convention" contrastive clause

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The status quo for program planning
is catalog-first construction: open the Signal skill catalog, group related namespaces into
stages, append echo at the end. Every rule in this protocol exists because the status quo
produces plans that cannot be audited. Before writing a single stage, internalize the two
failure modes that catalog-first construction produces:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied by namespace grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. Each rule shows what the status-quo path
produces and which failure it counters.

**RULE COVERAGE TABLE**

| Rule ID | Status-Quo Path (inertia) | Rule (this protocol) | Failure countered |
|---------|--------------------------|---------------------|-------------------|
| R-01 | Open the catalog first; group skills; name stages after namespace clusters | Declare phases by zone before opening the catalog (Step 2) | F-1: catalog-first |
| R-02 | Each stage produces whatever its skills naturally output | # Produces: determined by what the next stage needs as # Consumes: (consumer-pull, ARTIFACT 0) | F-1: catalog-first |
| R-03 | Gate = "adequate signals present" (prose, no stage ID, no count) | Compound gate with `{stage-id}::` lineage prefix and `>= N` count floor (Step 5a) | F-1: catalog-first |
| R-04 | Gate references the most obvious artifact (may be from a future stage) | FORWARD REFERENCE audit: gate artifacts must be producible by skills in the current stage (Step 5b) | F-1: catalog-first |
| R-05 | YAML annotations authored from skill knowledge; matrix is a summary | ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix, not authored independently (Step 8) | F-1: catalog-first |
| R-06 | Echo goes at the end (row N) because execution ends there | Echo at row 0 in ARTIFACT 2 because derivation begins at echo and reads backward (Step 8) | F-2: arbitrary-convention |
| R-07 | Echo's row position is a formatting choice (row 1 or row N -- both work) | Echo exception contrastive clause in ARTIFACT 0: "not an arbitrary convention" declared before any positive claim (Step 2) | F-2: arbitrary-convention |

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Status-Quo Failure | Criterion ladder |
|-------|--------------------------|-------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Zone membership implied by namespace grouping; invisible to auditors | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Inferred from gate prose; breaks on stage reordering | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | "Assess the area" non-questions; intent absent | Question-framing ladder |

**Lifecycle zones** (zone-membership class):
- **Breadth** -- do we understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts. Status-quo failure: namespace grouping
  implies zone membership without declaring a commitment decision.
- **Depth** -- does our design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test the design before shipping commitment. Status-quo failure: depth stages
  accumulate prove/review skills without naming what adversarial condition each addresses.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality. Status-quo failure: listen/metrics appended at the end
  without a declared adoption model to monitor against.

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

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

**The catalog must remain closed at this step** (R-01 -- counter-move against F-1). Status-quo
failure: opening the catalog first and naming phases after namespace clusters. Declare 3--6
phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or
`synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

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
the backward derivation, not authored from skill knowledge. Status-quo failure to prevent:
each stage producing whatever its skills "naturally" output (R-02, counter: F-1).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo failure to prevent: treating row-0 as a formatting
choice because "execution ends at echo" (R-07, counter: F-2). Row 0 is where derivation
begins; execution reads the matrix bottom-to-top. Moving echo to row N would misrepresent
the derivation direction in the artifact. Omission of # Band: from echo is normative: echo
is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic. Note the declared phase each maps to.
Status-quo failure: selecting skills first and letting selection drive zone assignment (R-01).

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Status-quo failure: inventing a new phase to accommodate an unmatched skill (this is F-1
re-entering through skill assignment).

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Status-quo failure: writing gates as prose ("adequate
signals present") -- this is the F-1 pattern that R-03 counters.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (status-quo form): `adequate discovery signals present`
- FAIL (partial status-quo): `>= 3 scout artifacts present` (no stage-id prefix)
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

Status-quo failure: referencing "the most obvious artifact" without verifying it is producible
by this stage's skills (R-04). For each non-echo stage: verify every artifact type in the gate
is producible by at least one skill in that stage's `skills` array. Fix all forward references
before Step 6.

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
- FAIL (status-quo form): `"Assess the compliance landscape"` -- intent unknowable
- FAIL (status-quo form): `"Are we ready to proceed?"` -- not zone-specific

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

Echo occupies row 0 (R-06 -- counter-move against F-2). Status-quo failure: placing echo at
row N because "execution ends there" -- this is the arbitrary-convention misreading.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations** (R-05). The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. Status-
quo failure: authoring YAML annotations from skill knowledge independently of the matrix.

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

| Constraint | Criterion | Status-Quo Violation | Compliance |
|------------|-----------|---------------------|------------|
| Phase boundaries declared by zone with catalog closed (R-01, counter F-1) | C-20 (arc-structure) | Phase names echo namespace groups | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | "Assess the area" task-description statements | Zone-specific question anchored to zone commitment decision |

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
[ ] C-01 through C-38: (same as V-01)
[ ] C-39: 3-column RULE COVERAGE TABLE present (Status-Quo Path | Rule | Failure countered);
         7 rows (R-01 through R-07); ALL protocol rules enumerated; completeness assertion:
         "This table is exhaustive: every construction rule in this protocol appears as
         exactly one row. No rule is omitted."
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline at definition site;
         ARTIFACT 0 echo exception carries `[counter: F-2]` inline at definition site;
         both present; no ARTIFACT 0 rule unlabeled
```

---

## V-04 -- Combined: Role Sequence + Output Format (Role-First + Rule Registry)

**Axis**: Combined. Role Sequence axis: a ROLE-RESPONSIBILITY TABLE is the first structural
element after the initial framing, preceding the failure taxonomy. This makes ownership visible
before any rule is declared. Output Format axis: C-39 is satisfied by a numbered RULE REGISTRY
(a named numbered list, not a table); each entry carries `[counter: F-N]` inline. The
completeness assertion follows: "This registry is exhaustive." C-40: ARTIFACT 0 inline labels
(independent of registry format). C-38: gate template bridge sentence (alternative target,
different from V-01). Register: structured formal.

**Hypothesis**: Role-first opening makes the plan's ownership model legible before any rule
is processed. The RULE REGISTRY as a numbered list tests whether C-39 tolerates format
variation (list vs table) as long as the dedicated structure, exhaustive enumeration, and
completeness assertion co-exist. C-40 is format-agnostic -- ARTIFACT 0 inline labels survive
regardless of registry format. C-38 via gate template bridge sentence demonstrates that the
criterion is target-agnostic (consumer-pull AND gate template are both valid C-38 targets).
Anticipated score: 33/33 aspirational.

**C-39 form**: Numbered RULE REGISTRY (dedicated named list, not table); 7 entries (R-01
             through R-07); each entry mapped to failure ID inline `[counter: FN]`;
             completeness assertion: "This registry is exhaustive: every construction rule
             in this protocol appears here. No rule is omitted."
**C-40 form**: ARTIFACT 0 consumer-pull `[counter: F-1]`; echo exception `[counter: F-2]`;
             both inline at definition site, exhaustive
**C-37 form**: Failure taxonomy table (after role table) + "every rule is a counter-move
             against exactly one row" + `[counter: F-N]` in ARTIFACT 0
**C-38 form**: Gate template bridge sentence in Step 5a: "The `{stage-id}::` prefix closes
             the artifact-provenance ambiguity by naming the producing stage directly; the
             `>= N` count floor makes the evidence bar independently verifiable without
             inspecting the stage's skills array"
**C-34 form**: BOTH negation AND bidirectional equivalence in consumer-pull rule
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-36 form**: "not an arbitrary convention" contrastive clause leading echo exception block

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Three functional roles share
responsibility for a program plan. Each role owns a distinct artifact class:

| Role | Artifact responsibility | Owns which steps |
|------|------------------------|-----------------|
| PM | Topic declaration; arc phase boundaries by lifecycle zone; investigative questions | Steps 1, 2, 6 |
| Architect | Band taxonomy (ARTIFACT 1); bilateral trace matrix (ARTIFACT 2); skill-to-phase assignment | Steps 3, 4, 7, 8 |
| Dev/Team Lead | Gate design; FORWARD REFERENCE audit; per-stage compliance verification | Steps 5a, 5b, 9 |

Every skill runs standalone; the program is a plan, not an executor. Role ownership is
declared before any skill is named -- the plan's accountability structure cannot be derived
from the catalog.

Before writing a single stage, internalize the two failure modes this protocol prevents:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied by namespace grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

Every construction rule in this protocol is a counter-move against exactly one row in this table.

**RULE REGISTRY** -- This registry is exhaustive: every construction rule in this protocol
appears here. No rule is omitted.

1. [R-01] Phases declared by zone before catalog opens (Step 2) [counter: F-1] -- prevents
   zone assignments retroactively shaped by namespace availability
2. [R-02] Consumer-pull derivation direction in ARTIFACT 0 [counter: F-1] -- forces
   Produces/Consumes pairs determined by successor needs, not prior-stage skill output
3. [R-03] Compound gate with stage-id lineage prefix (Step 5a) [counter: F-1] -- makes
   artifact provenance traceable to named producing stage, not inferred from gate prose
4. [R-04] FORWARD REFERENCE audit (Step 5b) [counter: F-1] -- gate artifacts verified
   against stage skills array; provenance remains knowable
5. [R-05] ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix (Step 8)
   [counter: F-1] -- YAML annotations derived from backward derivation, not authored
   independently from skill knowledge
6. [R-06] Echo at row 0 in ARTIFACT 2 (Step 8) [counter: F-2] -- encodes derivation
   direction structurally; row 0 is derivation origin, not execution end
7. [R-07] Echo exception contrastive clause in ARTIFACT 0 (Step 2) [counter: F-2] --
   forecloses convention misreading at schema definition site, before any YAML is written

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

Required construction sequence. Step owner noted. Read all steps before beginning Step 1.

1. PM: Declare the topic (Step 1)
2. PM: Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Architect: Select skills from catalog (Step 3)
4. Architect: Assign skills to declared phases (Step 4)
5a. Dev/Team Lead: Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. Dev/Team Lead: FORWARD REFERENCE audit: verify gate artifact traceability (Step 5b)
6. PM: Write per-phase intent questions: interrogative form required (Step 6)
7. Architect: Encode `evidence_arc:` field (Step 7)
8. Architect: Assemble YAML with per-stage `phase:` tags (Step 8)
9. Dev/Team Lead: Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic (PM)

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (PM)

**The catalog must remain closed at this step** (R-01 -- counter-move against F-1). Opening
the catalog before phase declaration infects the arc with skill availability bias. Do not
open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`,
`depth`, or `synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

For each phase, state the investigative question it answers (genuine interrogative, ends `?`):

| Phase label | Zone | Investigative question | PM owner |
|-------------|------|------------------------|----------|
| [name] | breadth/depth/synthesis | [...?] | [PM role/name] |

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

#### Step 3 -- Select Skills (Architect)

Open the catalog. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases (Architect)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Dev/Team Lead -- Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Three components in a single expression. The `{stage-id}::` prefix closes the artifact-
provenance ambiguity by naming the producing stage directly; the `>= N` count floor makes
the evidence bar independently verifiable without inspecting the stage's skills array.
Together they make every gate self-auditing from two orthogonal axes simultaneously: which
stage produced the artifact, and how many artifacts constitute sufficient evidence.

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit (Dev/Team Lead)

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

#### Step 6 -- Phase Intent Questions (PM)

- PASS (breadth): `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS (depth): `"Does the spec survive expert review against the discovered market signal?"`
- PASS (synthesis): `"Are users adopting the feature at the rate our model predicted?"`
- FAIL: `"Assess the compliance landscape"` -- not interrogative; intent unknowable

---

#### Step 7 -- Evidence Arc Field (Architect)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML (Architect)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. Its implicit information needs seed the entire backward
derivation. That is why echo occupies row 0 (R-06 -- counter-move against F-2): the derivation
reads top-to-bottom from echo; forward execution reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations** (R-05). The YAML
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
| Phase boundaries declared by zone with catalog closed (R-01, counter F-1) | C-20 (arc-structure) | Phase names echo namespace groups | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table (Dev/Team Lead)

| Stage | Arc-Structure (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing (C-17): `intent:` genuine interrogative? |
|-------|-------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-37: (same as V-01)
[ ] C-38: Step 5a gate template carries explicit bridge sentence: "The `{stage-id}::` prefix
         closes the artifact-provenance ambiguity by naming the producing stage directly; the
         `>= N` count floor makes the evidence bar independently verifiable without inspecting
         the stage's skills array"
[ ] C-39: RULE REGISTRY present (numbered list, 7 entries, R-01 through R-07); ALL protocol
         rules enumerated; each entry includes failure ID inline `[counter: FN]`;
         completeness assertion: "This registry is exhaustive: every construction rule in
         this protocol appears here. No rule is omitted."
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline at definition site;
         ARTIFACT 0 echo exception carries `[counter: F-2]` inline at definition site;
         both present; no ARTIFACT 0 rule unlabeled
```

---

## V-05 -- Combined: Phrasing Register + Inertia Framing (Imperative + AVOID Blocks)

**Axis**: Combined. Phrasing Register axis: second-person imperative throughout ("You must
produce ARTIFACT 0 before opening the catalog"; "Do not author YAML annotations
independently"). Inertia Framing axis: each structural step has an explicit one-line AVOID
block naming the specific inertia behavior to avoid at that step. C-39 via a dedicated
COUNTER-MOVE MANIFEST section (named, 7-row table, rule->failure direction) with completeness
assertion. C-40 via ARTIFACT 0 inline labels (same as V-01 canonical form -- imperative
register does not change ARTIFACT 0 structure). C-38 via canonical consumer-pull bridge
sentence. Register: direct imperative.

**Hypothesis**: Second-person imperative register eliminates explanatory prose and replaces
it with directives. AVOID blocks deliver inertia framing at point-of-use (one per step)
rather than in a front-loaded framing section. C-39 and C-40 survive register compression
because both are structural requirements that can be stated in imperative form. The AVOID
blocks distribute the inertia-framing function across all steps without concentrating it in
the opening. Anticipated score: 33/33 aspirational.

**C-39 form**: COUNTER-MOVE MANIFEST (named section, 7-row table, Rule | Failure countered
             | What it prevents); completeness assertion: "This manifest is exhaustive:
             every construction rule in this protocol appears as exactly one row"
**C-40 form**: ARTIFACT 0 consumer-pull `[counter: F-1]`; echo exception `[counter: F-2]`;
             both inline at definition site, exhaustive
**C-37 form**: Opening failure taxonomy table + "every rule is a counter-move against
             exactly one row" + `[counter: F-N]` in ARTIFACT 0
**C-38 form**: Canonical consumer-pull bridge sentence in ARTIFACT 0
**C-34 form**: BOTH negation AND equivalence in consumer-pull rule
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-36 form**: "not an arbitrary convention" contrastive clause in echo exception block

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Every skill runs standalone; the
program is a plan, not an executor. Read this entire protocol before beginning Step 1.

You must internalize these two failure modes before writing a single stage:

| Failure ID | Failure Name | What it produces | Design counter-move |
|------------|--------------|------------------|---------------------|
| F-1 | Catalog-first construction | Stages labeled after skill clusters; zone membership implied by namespace grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

Every construction rule in this protocol is a counter-move against exactly one row in this table.

**COUNTER-MOVE MANIFEST** -- This manifest is exhaustive: every construction rule in this
protocol appears as exactly one row. No rule is omitted.

| Rule ID | Rule | Failure countered | What it prevents |
|---------|------|-------------------|-----------------|
| R-01 | Phases declared by zone before catalog opens (Step 2) | F-1: catalog-first | Zone assignments retroactively shaped by namespace availability |
| R-02 | Consumer-pull derivation direction in ARTIFACT 0 | F-1: catalog-first | Produces/Consumes authored from skill knowledge instead of successor needs |
| R-03 | Compound gate with stage-id lineage prefix (Step 5a) | F-1: catalog-first | Artifact provenance inferred from gate prose rather than named producing stage |
| R-04 | FORWARD REFERENCE audit (Step 5b) | F-1: catalog-first | Gate artifacts not producible by current stage skills; provenance unknowable |
| R-05 | ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix (Step 8) | F-1: catalog-first | YAML annotations authored independently; matrix and YAML diverge |
| R-06 | Echo at row 0 in ARTIFACT 2 (Step 8) | F-2: arbitrary-convention | Derivation direction misrepresented; row N treats execution end as derivation origin |
| R-07 | Echo exception contrastive clause in ARTIFACT 0 (Step 2) | F-2: arbitrary-convention | Convention misreading enters ARTIFACT 0 before any YAML is written |

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

You must follow this sequence. Read all steps before beginning Step 1.

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

You must not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. Every phase label, artifact name, and skill selection must cohere with
this topic.

AVOID: A generic topic name that does not constrain phase label choices.

---

#### Step 2 -- Declare Arc Phases

**Do not open the catalog at this step** (R-01). You must declare 3--6 phase boundaries from
first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

AVOID: Naming phases after skill namespaces (`scout_stage`, `prove_block`) -- this is
catalog-first construction entering through phase naming.

Phase names must encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

For each phase, state the investigative question it answers (genuine interrogative, ends `?`):

| Phase label | Zone | Investigative question |
|-------------|------|------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**You must produce ARTIFACT 0 before ARTIFACT 1:**

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

AVOID: Omitting # Owner: from any non-echo stage; omitting # Band: from any non-echo stage.

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

AVOID: Letting namespace rows overlap; leaving any namespace without a band assignment.

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic. Note the declared phase each maps to.

AVOID: Selecting skills that have no corresponding declared phase; creating implied phases
by selecting skills from an undeclared zone.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

AVOID: Inventing a new phase to fit an unmatched skill -- return to Step 2 and revise the
arc instead.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

You must use this format. `{stage-id}` must match `name:` exactly. `>= N` required.
`{namespace}:{skill}` required. At least one gate must include `>= N`.

AVOID: Prose gates ("adequate signals present") -- this is the F-1 failure pattern that severs
artifact provenance from the gate.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL (inertia form): `adequate discovery signals present`
- FAIL (inertia form): `>= 3 scout artifacts present` (no stage-id prefix)

---

#### Step 5b -- FORWARD REFERENCE audit

You must verify: for each non-echo stage, every artifact type in the gate is producible by at
least one skill in that stage's `skills` array. Fix all forward references before Step 6.

AVOID: Referencing artifacts from skills not in the current stage's skills array -- provenance
becomes unknowable even with the correct compound gate format.

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

Every `intent:` field must be a genuine interrogative ending with `?`.

AVOID: Non-interrogative intent statements ("Assess the compliance landscape") -- these make
investigative intent unknowable.

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL (inertia form): `"Assess the compliance landscape"`

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

AVOID: Omitting a phase from the evidence_arc; placing a phase in the wrong zone key.

---

#### Step 8 -- Assemble YAML

You must produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column** before
writing any YAML.

AVOID: Authoring YAML annotations independently from skill knowledge (R-05 -- this is the
F-1 failure at the transcription step). All annotations must be transcribed from ARTIFACT 2.

You must place echo at row 0 (R-06).

AVOID: Placing echo at row N because "execution ends there" -- this is the F-2 arbitrary-
convention misreading.

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

| Constraint | Criterion | AVOID | Comply |
|------------|-----------|-------|--------|
| Phase boundaries declared by zone with catalog closed (R-01, counter F-1) | C-20 (arc-structure) | Phase names that echo namespace groups | Phase map locked in Step 2; catalog not opened until Step 3 |
| Every phase carries a phase-specific question ending with `?` | C-12 (question-framing) | Non-interrogative task descriptions | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure (C-18): `phase:` maps to `evidence_arc` zone? | Gate-Behavior (C-09): compound `{stage-id}::` with `>=N`? | Question-Framing (C-17): `intent:` genuine interrogative? |
|-------|-------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO requires revision. Do not proceed to Step 10 with any NO.

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
         artifacts that close the next stage's input gap") simultaneously
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; sole-source
         declaration present; column visible as rendered projection before any prose declaration
[ ] C-36: ARTIFACT 0 echo exception contains explicit contrastive clause: "not an arbitrary
         convention -- it is the structural encoding of echo's anchor role as terminal consumer"
         leading the block before any positive claim
[ ] C-37: opening failure taxonomy table names F-1 and F-2 with counter-move column; "every
         construction rule in this protocol is a counter-move against exactly one row in this
         table" present; ARTIFACT 0 rules carry `[counter: F-N]` labels
[ ] C-38: ARTIFACT 0 consumer-pull rule carries bridge sentence: "The negation closes the
         producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
[ ] C-39: COUNTER-MOVE MANIFEST present (named section, 7-row table, R-01 through R-07);
         ALL protocol rules enumerated; each mapped to a failure ID; completeness assertion:
         "This manifest is exhaustive: every construction rule in this protocol appears as
         exactly one row. No rule is omitted."
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline at definition site;
         ARTIFACT 0 echo exception carries `[counter: F-2]` inline at definition site;
         both present; no ARTIFACT 0 rule unlabeled
```
