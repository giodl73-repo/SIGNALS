---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 15
rubric: v31
aspirational_target: 36/36
new_criteria: C-41, C-42, C-43
---

# program-plan -- R15 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v31 (C-01 through C-43, 36 aspirational criteria).

**R14 retrospective under v31 rubric:**
- V-01 (Dual-Structure Coverage): C-41 PASS, C-42 FAIL (no zone commitment criteria
  pre-catalog), C-43 FAIL (no Status-Quo Path or Status-Quo Failure columns) --> 34/36
- V-02 (Zone Commitment Tests): C-41 PASS, C-42 PASS, C-43 FAIL --> 35/36 (~99.72)
- V-03 (Status-Quo Competitor Column): C-41 PASS, C-42 FAIL, C-43 PASS --> 35/36 (~99.72)
- V-04/V-05: split failures, same pattern -- no variation achieves 36/36

**R15 design constraint:** All five variations must satisfy C-41, C-42, AND C-43 simultaneously.
- C-41: BOTH F->R table (failure taxonomy, 2 rows) AND R->F table (rule coverage, 7 rows),
  each with its own INDEPENDENT completeness assertion -- not a joint assertion
- C-42: Per-zone 3-part commitment criteria (zone-exit question, artifact-type floor, required
  gate pattern class) declared BEFORE catalog opens; phase table extended with "Zone commitment
  check" column; ARTIFACT 1 carries same column
- C-43: RULE COVERAGE TABLE has "Status-Quo Path" column naming concrete inertia behavior per
  rule; opening failure taxonomy table has "Status-Quo Failure" column naming concrete inertia
  failure per failure mode

**Canonical C-41 structure (two directions, independent assertions):**
- F->R direction: Opening failure taxonomy table (2 rows: F-1, F-2)
  Independent assertion: "This table is self-certifying: every failure mode this protocol
  counters appears as exactly one row. Two rows; no failure mode omitted."
- R->F direction: RULE COVERAGE TABLE (7 rows: R-01 through R-07)
  Independent assertion: "This table is exhaustive: every construction rule in this protocol
  appears as exactly one row. No rule is omitted."
- The two assertions do not reference each other; each table self-certifies independently

**Canonical C-42 structure (3-part per zone, declared pre-catalog):**
- Breadth: (1) "Have we named the problem space, identified constraints, committed to a
  direction without solution-space knowledge?" (2) floor: competitor/market + feasibility +
  draft artifacts (3) class: compound gate >= 2 on scout or draft artifact
- Depth: (1) "Has the design been tested against failure modes by reviewers who did not
  author the spec?" (2) floor: review + flow/trace + prove artifacts (3) class: compound
  gate >= 2 on review or prove artifact
- Synthesis: (1) "Are post-launch signals tracking against the adoption model we committed
  to before shipping?" (2) floor: listen + metrics/goals artifacts (3) class: compound gate
  with count floor on listen, metrics, or goals artifact
- Phase table in Step 2 and ARTIFACT 1 carry a "Zone commitment check" column

**Canonical C-43 structure (status-quo columns in both tables):**
- Opening failure taxonomy gains "Status-Quo Failure" column:
  F-1: "Open the catalog; group skills by namespace; name stages after clusters; append echo at end"
  F-2: "Place echo at row N because execution ends there; treat row position as formatting"
- RULE COVERAGE TABLE gains "Status-Quo Path" column:
  R-01: "Open the catalog first; group skills; name stages after namespace clusters"
  R-02: "Each stage produces whatever its skills naturally output"
  R-03: "Gate = 'adequate signals present' (prose, no stage ID, no count)"
  R-04: "Gate references the most obvious artifact (may be from a future stage)"
  R-05: "YAML annotations authored from skill knowledge; matrix is a summary"
  R-06: "Echo goes at the end (row N) because execution ends there"
  R-07: "Echo's row position is a formatting choice (row 1 or row N -- both work)"

**Variation axes for R15:**
- V-01 (tiebreaker, no additional axis): Direct merger of R14 V-02 + V-03 -- C-42 zone
  commitment criteria AND C-43 status-quo columns. The minimal combination achieving 36/36.
- V-02 (single axis -- role sequence): Role-responsibility table precedes the opening failure
  taxonomy; step headers carry role attribution; RULE COVERAGE TABLE gains Owner column
- V-03 (single axis -- phrasing register): Second-person imperative throughout; "you are
  planning, not executing" opening identity; all rules addressed as "you must"
- V-04 (single axis -- lifecycle emphasis): Each zone section carries its commitment criteria
  as a structured inline commitment block (zone-exit question + artifact floor + gate class
  as a per-zone table) rather than a flat pre-catalog list
- V-05 (combined -- role sequence + inertia framing): Role attribution on step headers PLUS
  explicit AVOID block per step naming the status-quo behavior each step displaces

---

## V-01 -- Tiebreaker: Zone Commitment + Status-Quo Column (direct merger)

**Axis**: No additional single axis -- V-01 is the minimal tiebreaker variation that merges
R14 V-02 (zone commitment criteria) with R14 V-03 (status-quo competitor column) and extends
the opening failure taxonomy table with a "Status-Quo Failure" column. Both C-42 and C-43
active; C-41 via independent assertions on both tables. Register: structured formal.

**Hypothesis**: The direct merger of V-02 and V-03 is the minimal path to 36/36. C-42 is
satisfied by per-zone 3-part commitment criteria declared before the catalog and the zone
commitment check column in the phase table and ARTIFACT 1. C-43 is satisfied by the
"Status-Quo Path" column in the RULE COVERAGE TABLE and the "Status-Quo Failure" column in
the opening failure taxonomy table. C-41 is satisfied by the two independent completeness
assertions. No additional axis introduced -- this variation proves the combination is
achievable without further structural elaboration. Anticipated score: 36/36 aspirational.

**C-41 form**: Opening taxonomy table (F->R, "self-certifying: every failure mode...exactly
             one row. Two rows; no failure mode omitted.") + RULE COVERAGE TABLE (R->F,
             "exhaustive: every construction rule...exactly one row. No rule is omitted.");
             assertions are independent -- each table self-certifies without reference to other
**C-42 form**: Breadth/Depth/Synthesis zone commitment criteria (3-part each: zone-exit
             question, artifact-type floor, gate pattern class) declared before catalog opens;
             phase table has "Zone commitment check" column; ARTIFACT 1 has same column
**C-43 form**: Opening failure taxonomy gains "Status-Quo Failure" column; RULE COVERAGE
             TABLE gains "Status-Quo Path" column; both columns present, both tables updated
**C-40 form**: ARTIFACT 0 consumer-pull rule `[counter: F-1]`; echo exception `[counter: F-2]`;
             both inline at definition site, exhaustive
**C-39 form**: RULE COVERAGE TABLE (7 rows, R-01 through R-07) with independent completeness
             assertion (same table also satisfies C-41 R->F direction)
**C-37 form**: Opening taxonomy table names F-1 and F-2; "every construction rule is a
             counter-move against exactly one row in this table" + `[counter: F-N]` in ARTIFACT 0
**C-38 form**: Canonical consumer-pull bridge sentence in ARTIFACT 0
**C-34 form**: BOTH negation AND bidirectional equivalence in consumer-pull rule
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-36 form**: "not an arbitrary convention" contrastive clause leading echo exception block

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before writing a single stage,
internalize the two failure modes this protocol is designed to prevent. Each failure has a
concrete status-quo behavior that produces it:

| Failure ID | Failure Name | Status-Quo Failure (inertia) | What it produces | Design counter-move |
|------------|--------------|------------------------------|------------------|---------------------|
| F-1 | Catalog-first construction | Open the catalog; group skills by namespace; name stages after clusters; append echo at end | Stages labeled after skill clusters; zone membership implied by grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted. Each rule names the
status-quo path it displaces.

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

This table is exhaustive: every construction rule in this protocol appears as exactly one row.
No rule is omitted.

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Status-Quo Failure | Criterion ladder |
|-------|--------------------------|-------------------|-----------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before the catalog opens | Zone membership implied by namespace grouping; invisible to auditors | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Inferred from gate prose; breaks on stage reordering | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | "Assess the area" non-questions; intent absent | Question-framing ladder |

**Lifecycle zones with commitment criteria** (declared before the catalog opens):

**Breadth zone** -- do we understand the problem space well enough to commit to a direction?
Scout and draft skills produce breadth artifacts. Status-quo failure: namespace grouping
implies zone membership without declaring a commitment decision.

Breadth zone commitment criteria (all three must be satisfied before advancing to depth):
1. Zone-exit question: "Have we named the problem space, identified key constraints, and
   committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor: at least one competitor or market signal artifact, at least one
   feasibility artifact, at least one draft artifact (spec or proposal)
3. Required gate pattern class: at least one compound gate with `>= 2` count floor on a
   scout or draft skill artifact from a stage in this zone

**Depth zone** -- does our design survive adversarial conditions before shipping commitment?
Prove, review, flow, and trace skills stress-test the design. Status-quo failure: depth
stages accumulate prove/review skills without naming what adversarial condition each addresses.

Depth zone commitment criteria (all three must be satisfied before advancing to synthesis):
1. Zone-exit question: "Has the design been tested against failure modes and adversarial
   conditions by reviewers who did not author the spec?"
2. Artifact-type floor: at least one review artifact, at least one flow or trace artifact,
   at least one prove artifact
3. Required gate pattern class: at least one compound gate referencing a review or prove
   skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** -- are users adopting and signaling as expected post-launch?
Listen, metrics, and goals skills monitor post-launch reality. Status-quo failure:
listen/metrics appended at the end without a declared adoption model to monitor against.

Synthesis zone commitment criteria (all three must be satisfied before echo advances):
1. Zone-exit question: "Are post-launch signals tracking against the adoption model the
   team committed to before shipping?"
2. Artifact-type floor: at least one listen artifact, at least one metrics or goals artifact
3. Required gate pattern class: compound gate with count floor on a listen, metrics, or
   goals skill artifact from a stage in this zone

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required. Count floors calibrated to zone commitment criteria: breadth and depth stages
require `>= 2` for commitment-bearing artifacts; synthesis stages require `>= 1`.

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
5a. Design gates: compound lineage prefix format, calibrated to zone commitment criteria (Step 5a)
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
phase boundaries from first principles. Assign each to a zone using the commitment criteria
declared above -- the criteria serve as the zone assignment test, not namespace grouping.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

For each phase, state the investigative question it answers (genuine interrogative, ends `?`).
Include a zone commitment check referencing the criteria declared above:

| Phase label | Zone | Investigative question | Zone commitment check |
|-------------|------|------------------------|-----------------------|
| [name] | breadth/depth/synthesis | [...?] | [Which commitment criteria does this phase address? E.g., "satisfies Breadth criterion 2: contributes competitor artifact"] |

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
the backward derivation, not authored from skill knowledge. Status-quo path displaced: each
stage producing whatever its skills naturally output (R-02).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07). Row 0 is where derivation begins; execution reads
the matrix bottom-to-top. Moving echo to row N would misrepresent the derivation direction
in the artifact. Omission of # Band: from echo is normative: echo is the derivation anchor,
not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table** with columns:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).
The "Zone commitment check" column identifies which zone commitment criteria each band's
skills address.

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria. Note the declared phase
each maps to. Status-quo failure: selecting skills first and letting selection drive zone
assignment (R-01, status-quo path displaced).

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
After assigning, verify each zone's commitment criteria are satisfiable by the assigned skills
(minimum artifact types present for each zone). If a zone falls short of its artifact-type
floor, add a skill that produces the missing type or revise the zone's scope.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors calibrated to zone commitment criteria:
breadth and depth stages require `>= 2` for commitment-bearing artifacts; synthesis `>= 1`.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, stage-id absent): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.
Verify that the final stage in each zone satisfies the zone's required gate pattern class.

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

Every phase from Step 2 must appear in exactly one arc key. Verify each zone's commitment
criteria are satisfiable given the phase labels and skills assigned.

---

#### Step 8 -- Assemble YAML

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. Its implicit information needs seed the entire backward
derivation. That is why echo occupies row 0 -- counter-move against F-2 (status-quo path
displaced: echo at row N because execution ends there). The derivation reads top-to-bottom
from echo; forward execution reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is the authoritative form of the YAML annotation -- copy it directly. YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema:

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

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO | YES / NO |

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
[ ] C-31: echo causal anchor at two structural levels (failure taxonomy table + ARTIFACT 0)
[ ] C-32: consumer-pull rule states negation OR equivalence
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule states BOTH negation AND bidirectional equivalence simultaneously
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; sole-source present
[ ] C-36: ARTIFACT 0 echo exception contains "not an arbitrary convention" contrastive clause
         leading the block before any positive claim
[ ] C-37: opening failure taxonomy table names F-1 and F-2 with counter-move column; "every
         construction rule in this protocol is a counter-move against exactly one row" present;
         ARTIFACT 0 rules carry `[counter: F-N]` labels
[ ] C-38: ARTIFACT 0 consumer-pull rule carries bridge sentence: "The negation closes the
         producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
[ ] C-39: RULE COVERAGE TABLE present (7 rows, R-01 through R-07); ALL protocol rules
         enumerated; each mapped to a failure ID; completeness assertion present
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline; echo exception carries
         `[counter: F-2]` inline; both present; no ARTIFACT 0 rule unlabeled
[ ] C-41: opening failure taxonomy table carries INDEPENDENT completeness assertion ("This
         table is self-certifying: every failure mode appears as exactly one row. Two rows;
         no failure mode omitted."); RULE COVERAGE TABLE carries INDEPENDENT completeness
         assertion ("This table is exhaustive: every construction rule appears as exactly one
         row. No rule is omitted."); BOTH assertions present; NEITHER references the other
[ ] C-42: breadth, depth, and synthesis zone commitment criteria (3-part each: zone-exit
         question, artifact-type floor, gate pattern class) declared before the skill catalog
         opens; ARTIFACT 1 band taxonomy table includes "Zone commitment check" column; phase
         table in Step 2 includes "Zone commitment check" column
[ ] C-43: RULE COVERAGE TABLE has "Status-Quo Path" column (7 rows of concrete inertia
         behaviors); opening failure taxonomy table has "Status-Quo Failure" column (2 rows
         of concrete inertia failures); BOTH columns present in their respective tables
```

---

## V-02 -- Role Sequence: Role-Responsibility Table First

**Axis**: Single-axis. A role-responsibility table (PM / Architect / Dev / Team Lead) appears
before the opening failure taxonomy, mapping each role to the construction steps they own and
the failure mode they are responsible for countering. The RULE COVERAGE TABLE gains an "Owner
role" column. Step headers in the construction order carry explicit role attribution.
Zone commitment + status-quo columns preserved from V-01 baseline.

**Hypothesis**: Front-loading the role map establishes ownership before failure-mode framing
begins. Seeing "Architect owns gate pattern class selection" before "F-1 = catalog-first" makes
each role's counter-move responsibility traceable from the opening structure. The role column
in the RULE COVERAGE TABLE creates a three-way mapping: status-quo path -> rule -> owner.
C-41/C-42/C-43 preserved from V-01. Anticipated score: 36/36 aspirational.

**C-41 form**: Same as V-01 -- both tables with independent completeness assertions
**C-42 form**: Same as V-01 -- 3-part zone commitment criteria pre-catalog; zone commitment
             check column in phase table and ARTIFACT 1
**C-43 form**: Same as V-01 -- "Status-Quo Failure" column in taxonomy; "Status-Quo Path"
             column in RULE COVERAGE TABLE
**Additional axis**: Role-responsibility table before failure taxonomy; RULE COVERAGE TABLE
             has "Owner role" column; each construction step header names the owner role

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Four functional roles share
responsibility for a correct program plan. Each role owns specific construction steps and
is accountable for countering specific failure modes:

| Role | Construction responsibility | Failure modes countered | Steps owned |
|------|----------------------------|------------------------|-------------|
| PM | Topic declaration; phase naming from investigation intent; synthesis zone ownership | F-1 at naming layer: phases named after investigation intent, not skill clusters | Steps 1, 2 (phase table), 6, 7 |
| Architect | Arc phase design; zone commitment criteria; gate design; ARTIFACT 0 schema | F-1 at construction layer: catalog closed until phases declared; consumer-pull enforced; gates compound | Steps 2 (ARTIFACT 0), 5a, 5b |
| Dev | Skill catalog selection; ARTIFACT 2 assembly; YAML transcription from matrix | F-1 at assembly layer: YAML transcribed from matrix, not authored from skill knowledge | Steps 3, 4, 8 |
| Team Lead | Zone commitment audit; per-stage compliance; terminal validation | F-1 and F-2 completeness: all criteria verified, echo anchor confirmed | Steps 9, 10 |

Before writing a single stage, internalize the two failure modes this protocol is designed
to prevent. Each failure has a concrete status-quo behavior that produces it:

| Failure ID | Failure Name | Status-Quo Failure (inertia) | What it produces | Design counter-move |
|------------|--------------|------------------------------|------------------|---------------------|
| F-1 | Catalog-first construction | Open the catalog; group skills by namespace; name stages after clusters; append echo at end | Stages labeled after skill clusters; zone membership implied by grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted.

**RULE COVERAGE TABLE**

| Rule ID | Status-Quo Path (inertia) | Rule (this protocol) | Failure countered | Owner role |
|---------|--------------------------|---------------------|-------------------|------------|
| R-01 | Open the catalog first; group skills; name stages after namespace clusters | Declare phases by zone before opening the catalog (Step 2) | F-1: catalog-first | PM / Architect |
| R-02 | Each stage produces whatever its skills naturally output | # Produces: determined by what the next stage needs as # Consumes: (consumer-pull, ARTIFACT 0) | F-1: catalog-first | Architect |
| R-03 | Gate = "adequate signals present" (prose, no stage ID, no count) | Compound gate with `{stage-id}::` lineage prefix and `>= N` count floor (Step 5a) | F-1: catalog-first | Architect |
| R-04 | Gate references the most obvious artifact (may be from a future stage) | FORWARD REFERENCE audit: gate artifacts must be producible by skills in the current stage (Step 5b) | F-1: catalog-first | Architect |
| R-05 | YAML annotations authored from skill knowledge; matrix is a summary | ARTIFACT 2 as sole authoritative source; YAML transcribed from matrix, not authored independently (Step 8) | F-1: catalog-first | Dev |
| R-06 | Echo goes at the end (row N) because execution ends there | Echo at row 0 in ARTIFACT 2 because derivation begins at echo and reads backward (Step 8) | F-2: arbitrary-convention | Dev |
| R-07 | Echo's row position is a formatting choice (row 1 or row N -- both work) | Echo exception contrastive clause in ARTIFACT 0: "not an arbitrary convention" declared before any positive claim (Step 2) | F-2: arbitrary-convention | Architect |

This table is exhaustive: every construction rule in this protocol appears as exactly one row.
No rule is omitted.

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Status-Quo Failure | Criterion ladder | Owner |
|-------|--------------------------|-------------------|-----------------|-------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- committed before catalog opens | Zone membership implied by namespace grouping; invisible to auditors | Arc-structure ladder | PM |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | Inferred from gate prose; breaks on stage reordering | Gate-behavior ladder | Architect |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | "Assess the area" non-questions; intent absent | Question-framing ladder | PM |

**Lifecycle zones with commitment criteria** (declared before catalog opens -- Owner: PM / Architect):

**Breadth zone** -- do we understand the problem space well enough to commit to a direction?
Scout and draft skills produce breadth artifacts. Status-quo failure: namespace grouping
implies zone membership without declaring a commitment decision.

Breadth zone commitment criteria (all three must be satisfied before advancing to depth):
1. Zone-exit question (Owner: PM): "Have we named the problem space, identified key constraints,
   and committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor (Owner: Architect): at least one competitor or market signal artifact,
   at least one feasibility artifact, at least one draft artifact (spec or proposal)
3. Required gate pattern class (Owner: Architect): at least one compound gate with `>= 2`
   count floor on a scout or draft skill artifact from a stage in this zone

**Depth zone** -- does our design survive adversarial conditions before shipping commitment?
Status-quo failure: depth stages accumulate prove/review skills without naming what adversarial
condition each addresses.

Depth zone commitment criteria (all three must be satisfied before advancing to synthesis):
1. Zone-exit question (Owner: PM): "Has the design been tested against failure modes and
   adversarial conditions by reviewers who did not author the spec?"
2. Artifact-type floor (Owner: Architect): at least one review artifact, at least one flow
   or trace artifact, at least one prove artifact
3. Required gate pattern class (Owner: Architect): at least one compound gate referencing
   a review or prove skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** -- are users adopting and signaling as expected post-launch?
Status-quo failure: listen/metrics appended at the end without a declared adoption model.

Synthesis zone commitment criteria (all three must be satisfied before echo advances):
1. Zone-exit question (Owner: PM): "Are post-launch signals tracking against the adoption
   model the team committed to before shipping?"
2. Artifact-type floor (Owner: Architect): at least one listen artifact, at least one
   metrics or goals artifact
3. Required gate pattern class (Owner: Architect): compound gate with count floor on a
   listen, metrics, or goals skill artifact from a stage in this zone

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

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

1. Declare the topic (Step 1) -- Owner: PM
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2) -- Owner: PM / Architect
3. Select skills from catalog (Step 3) -- Owner: Dev
4. Assign skills to declared phases (Step 4) -- Owner: Dev
5a. Design gates in compound lineage prefix format (Step 5a) -- Owner: Architect
5b. FORWARD REFERENCE audit (Step 5b) -- Owner: Architect
6. Write per-phase intent questions (Step 6) -- Owner: PM
7. Encode `evidence_arc:` field (Step 7) -- Owner: PM
8. Assemble YAML from ARTIFACT 2 (Step 8) -- Owner: Dev
9. Per-stage compliance table (Step 9) -- Owner: Team Lead
10. Terminal checklist (Step 10) -- Owner: Team Lead

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic (Owner: PM)

State the topic name.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect). Declare 3--6 phase
boundaries from first principles using the commitment criteria above as zone assignment tests.

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which commitment criteria does this phase address?] | PM / Architect |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema (Owner: Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative form, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input from the prior stage]
  # Produces: [artifact type(s) yielded as output for the next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo; YAML annotations are transcribed from
the backward derivation, not authored from skill knowledge. Status-quo path displaced: each
stage producing whatever its skills naturally output (R-02, Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation begins;
execution reads the matrix bottom-to-top. Moving echo to row N would misrepresent the
derivation direction in the artifact. Omission of # Band: from echo is normative: echo is
the derivation anchor, not a band member.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Steps 3-10 (Owner attribution per step header above)

Steps 3-10 follow the same pattern as V-01 with owner attribution. Terminal checklist includes
all C-01 through C-43 items (same as V-01 checklist).

---

## V-03 -- Phrasing Register: Second-Person Imperative

**Axis**: Single-axis. Opening identity and all construction steps are addressed in
second-person imperative throughout. "You are planning a route, not driving it." Every
step header uses imperative voice. The failure taxonomy addresses the reader directly:
"you open the catalog" as the status-quo failure behavior. Zone commitment + status-quo
columns preserved from V-01 baseline.

**Hypothesis**: Second-person register makes the not-executor identity claim a direct address
rather than an object-level description of the skill, improving C-35. The "you" subject in
the status-quo failure column intensifies the inertia framing (C-43) by naming the reader as
the agent of the status-quo failure. C-41/C-42/C-43 structures preserved. Anticipated score:
36/36 aspirational.

**C-41 form**: Same as V-01 -- both tables with independent completeness assertions
**C-42 form**: Same as V-01 -- 3-part zone commitment criteria pre-catalog; zone commitment
             check column in phase table
**C-43 form**: Same as V-01 -- status-quo columns in both tables; "you open the catalog"
             phrasing in Status-Quo Failure cells makes the inertia behavior second-person
**C-35 form**: Opening identity block uses second-person direct address: "You are planning
             a route, not driving it." Subject of the identity claim is "you"

---

### FULL PROMPT BODY

You are planning a route, not driving it. You are producing a `program.yaml` for the Signal
plugin -- a plan that sequences skills into stages. You will not execute those skills; you will
sequence them. Before you write a single stage, you must internalize the two failure modes
that catalog-first construction produces -- because every rule you will follow is your
deliberate counter-move against one of these failures:

| Failure ID | Failure Name | Status-Quo Failure (what you would do by default) | What it produces | Design counter-move |
|------------|--------------|---------------------------------------------------|------------------|---------------------|
| F-1 | Catalog-first construction | You open the catalog; you group skills by namespace; you name stages after clusters; you append echo at the end | Stages labeled after skill clusters; zone membership implied by grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog: you declare phases by zone with the catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | You place echo at row N because execution ends there; you treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: you begin derivation at echo and read backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode you must counter appears as exactly one row.
Two rows; no failure mode omitted.

Every rule you will follow is a counter-move against exactly one row in this table.

The following table enumerates ALL rules you must follow. This table is exhaustive: every
construction rule appears as exactly one row. No rule is omitted. Each rule names the
status-quo path you are displacing.

**RULE COVERAGE TABLE**

| Rule ID | Status-Quo Path (what you would do by default) | Rule (what you must do instead) | Failure countered |
|---------|------------------------------------------------|--------------------------------|-------------------|
| R-01 | You open the catalog first; you group skills; you name stages after namespace clusters | You declare phases by zone before opening the catalog (Step 2) | F-1: catalog-first |
| R-02 | You let each stage produce whatever its skills naturally output | You determine # Produces: by what the next stage declares as # Consumes: (consumer-pull, ARTIFACT 0) | F-1: catalog-first |
| R-03 | You write the gate as "adequate signals present" (no stage ID, no count) | You write a compound gate with `{stage-id}::` lineage prefix and `>= N` count floor (Step 5a) | F-1: catalog-first |
| R-04 | You reference the most obvious artifact in the gate (may be from a future stage) | You run a FORWARD REFERENCE audit: gate artifacts must be producible by skills in the current stage (Step 5b) | F-1: catalog-first |
| R-05 | You author YAML annotations from skill knowledge; you treat the matrix as a summary | You transcribe YAML from ARTIFACT 2 as the sole authoritative source; you do not author independently (Step 8) | F-1: catalog-first |
| R-06 | You put echo at the end (row N) because execution ends there | You put echo at row 0 in ARTIFACT 2 because you begin derivation at echo and read backward (Step 8) | F-2: arbitrary-convention |
| R-07 | You treat echo's row position as a formatting choice (row 1 or row N -- both work) | You declare the echo exception contrastive clause in ARTIFACT 0: "not an arbitrary convention" before any positive claim (Step 2) | F-2: arbitrary-convention |

This table is exhaustive: every rule you must follow appears as exactly one row. No rule is omitted.

Every skill you select runs standalone; the program you produce is a plan, not an executor.
You begin the chain at the end: echo is the terminal consumer whose implicit information needs
seed the entire backward derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information you must keep knowable at every stage boundary:

| Class | What you must keep knowable | Status-Quo Failure (if you don't) | Criterion ladder |
|-------|-----------------------------|------------------------------------|-----------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- committed before you open the catalog | You imply zone membership from namespace grouping; invisible to auditors | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | You infer from gate prose; breaks on stage reordering | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what you needed to learn," not "what skills ran" | You write "assess the area" non-questions; intent absent | Question-framing ladder |

**Lifecycle zones -- you must satisfy the commitment criteria before leaving each zone:**

**Breadth zone** -- you must answer: do you understand the problem space well enough to commit
to a direction? Status-quo failure: you imply zone membership from namespace grouping without
declaring a commitment decision.

Breadth zone commitment criteria (all three must be satisfied before you advance to depth):
1. Zone-exit question you must answer: "Have you named the problem space, identified key
   constraints, and committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor you must reach: at least one competitor or market signal artifact,
   at least one feasibility artifact, at least one draft artifact (spec or proposal)
3. Gate pattern class you must use: at least one compound gate with `>= 2` count floor on
   a scout or draft skill artifact from a stage in this zone

**Depth zone** -- you must answer: does your design survive adversarial conditions before you
commit to shipping? Status-quo failure: you accumulate prove/review skills without naming
what adversarial condition each stage addresses.

Depth zone commitment criteria (all three must be satisfied before you advance to synthesis):
1. Zone-exit question you must answer: "Has the design been tested against failure modes and
   adversarial conditions by reviewers who did not author the spec?"
2. Artifact-type floor you must reach: at least one review artifact, at least one flow or
   trace artifact, at least one prove artifact
3. Gate pattern class you must use: at least one compound gate referencing a review or prove
   skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** -- you must answer: are users adopting and signaling as expected?
Status-quo failure: you append listen/metrics at the end without a declared adoption model.

Synthesis zone commitment criteria (all three must be satisfied before echo advances):
1. Zone-exit question you must answer: "Are post-launch signals tracking against the adoption
   model you committed to before shipping?"
2. Artifact-type floor you must reach: at least one listen artifact, at least one metrics
   or goals artifact
3. Gate pattern class you must use: a compound gate with count floor on a listen, metrics,
   or goals skill artifact from a stage in this zone

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

You must match `{stage-id}` exactly to the stage `name:`. You must include `>= N` and
`{namespace}:{skill}`. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

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

Required construction sequence you must follow. Read all steps before beginning Step 1.

1. You declare the topic (Step 1)
2. You declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. You select skills from the catalog (Step 3)
4. You assign skills to declared phases (Step 4)
5a. You design gates in compound lineage prefix format (Step 5a)
5b. You run the FORWARD REFERENCE audit (Step 5b)
6. You write per-phase intent questions (Step 6)
7. You encode the `evidence_arc:` field (Step 7)
8. You assemble YAML from ARTIFACT 2 (Step 8)
9. You complete the per-stage compliance table (Step 9)
10. You run the terminal validation checklist (Step 10)

Do not proceed to Step 3 until you have completed Step 2.

---

#### Step 1 -- Declare the Topic

State the topic name. Everything you name and group must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**You must keep the catalog closed at this step** (R-01 -- you are counter-moving against F-1).
Do not open the catalog until Step 3. Declare 3--6 phase boundaries from first principles.
Assign each to a zone using the commitment criteria above -- not namespace grouping.

Phase names you must encode as investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

For each phase, state the investigative question (genuine interrogative, ends `?`) and the
zone commitment check:

| Phase label | Zone | Investigative question | Zone commitment check |
|-------------|------|------------------------|-----------------------|
| [name] | breadth/depth/synthesis | [...?] | [Which zone commitment criteria does this phase satisfy?] |

**Before ARTIFACT 1, you must produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative form, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input from the prior stage]
  # Produces: [artifact type(s) yielded as output for the next stage]

Consumer-pull rule [counter: F-1]: You determine # Produces: by what the next stage declares
as # Consumes: -- not by what the prior stage's skills naturally output. Equivalently: you
produce the artifacts that close the next stage's input gap. The negation closes the
producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. You run the derivation backward from echo; you transcribe YAML annotations
from the backward derivation, not from skill knowledge. Status-quo path you are displacing:
you let each stage produce whatever its skills naturally output (R-02).

Echo exception [counter: F-2]: You omit # Band: from echo. Echo's row-0 position in ARTIFACT 2
is not an arbitrary convention -- it is the structural encoding of echo's anchor role as
terminal consumer. Status-quo path you are displacing: you treat row-0 as a formatting choice
because execution ends at echo (R-07). Row 0 is where your derivation begins; execution reads
the matrix bottom-to-top. You do not move echo to row N -- that would misrepresent the
derivation direction in the artifact.
```

Lock your phase map after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Steps 3-10

Steps 3-10 follow the same pattern as V-01 with second-person imperative register throughout.
Terminal checklist includes all C-01 through C-43 items (same as V-01 checklist).

---

## V-04 -- Lifecycle Emphasis: Per-Zone Commitment Block Structure

**Axis**: Single-axis. Each zone section carries its 3-part commitment criteria as a
structured inline commitment block -- a labeled two-column table embedded within the zone
description (commitment component | requirement). The zone-exit question, artifact-type floor,
and gate pattern class appear as table rows, not a numbered list. The commitment block is
tightly coupled to the zone's purpose statement and appears immediately after the status-quo
failure sentence. Status-quo + C-41 preserved from V-01 baseline.

**Hypothesis**: The per-zone commitment table structure (versus a flat numbered list)
makes the 3-part structure visually distinct and independently auditable per zone. A
scorer verifying C-42 can locate the commitment block for each zone by scanning for the
two-column table format within each zone section. The commitment block format also creates
a richer zone section that may improve C-20 pass rates. Anticipated score: 36/36 aspirational.

**C-41 form**: Same as V-01 -- both tables with independent completeness assertions
**C-42 form**: Per-zone commitment criteria as inline two-column table within each zone
             section (commitment component | requirement); declared before catalog opens;
             phase table and ARTIFACT 1 have "Zone commitment check" column
**C-43 form**: Same as V-01 -- status-quo columns in both tables

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before writing a single stage,
internalize the two failure modes this protocol is designed to prevent. Each failure has a
concrete status-quo behavior that produces it:

| Failure ID | Failure Name | Status-Quo Failure (inertia) | What it produces | Design counter-move |
|------------|--------------|------------------------------|------------------|---------------------|
| F-1 | Catalog-first construction | Open the catalog; group skills by namespace; name stages after clusters; append echo at end | Stages labeled after skill clusters; zone membership implied by grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted.

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

This table is exhaustive: every construction rule in this protocol appears as exactly one row.
No rule is omitted.

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Status-Quo Failure | Criterion ladder |
|-------|--------------------------|-------------------|-----------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- committed before catalog opens | Zone membership implied by namespace grouping; invisible to auditors | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | Inferred from gate prose; breaks on stage reordering | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | "Assess the area" non-questions; intent absent | Question-framing ladder |

**Lifecycle zones with commitment blocks** (declared before the catalog opens):

---

**BREADTH ZONE** -- Do we understand the problem space well enough to commit to a direction?
Scout and draft skills produce breadth artifacts. *Status-quo failure*: namespace grouping
implies zone membership without declaring a commitment decision.

| Commitment component | Requirement |
|---------------------|-------------|
| **Zone-exit question** | "Have we named the problem space, identified key constraints, and committed to a direction without relying on solution-space knowledge?" |
| **Artifact-type floor** | At least one competitor or market signal artifact; at least one feasibility artifact; at least one draft artifact (spec or proposal) |
| **Required gate pattern class** | At least one compound gate with `>= 2` count floor on a scout or draft skill artifact from a stage in this zone |

---

**DEPTH ZONE** -- Does our design survive adversarial conditions before shipping commitment?
Prove, review, flow, and trace skills stress-test the design. *Status-quo failure*: depth
stages accumulate prove/review skills without naming what adversarial condition each addresses.

| Commitment component | Requirement |
|---------------------|-------------|
| **Zone-exit question** | "Has the design been tested against failure modes and adversarial conditions by reviewers who did not author the spec?" |
| **Artifact-type floor** | At least one review artifact; at least one flow or trace artifact; at least one prove artifact |
| **Required gate pattern class** | At least one compound gate referencing a review or prove skill with `>= 2` count floor from a stage in this zone |

---

**SYNTHESIS ZONE** -- Are users adopting and signaling as expected post-launch?
Listen, metrics, and goals skills monitor post-launch reality. *Status-quo failure*:
listen/metrics appended at the end without a declared adoption model to monitor against.

| Commitment component | Requirement |
|---------------------|-------------|
| **Zone-exit question** | "Are post-launch signals tracking against the adoption model the team committed to before shipping?" |
| **Artifact-type floor** | At least one listen artifact; at least one metrics or goals artifact |
| **Required gate pattern class** | Compound gate with count floor on a listen, metrics, or goals skill artifact from a stage in this zone |

---

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors calibrated to commitment blocks:
breadth and depth `>= 2`; synthesis `>= 1`.

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

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates in compound lineage prefix format (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML from ARTIFACT 2 (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step** (R-01). Status-quo failure: opening the
catalog first. Declare 3--6 phase boundaries. Assign each to a zone using the commitment
block for that zone as the assignment test.

| Phase label | Zone | Investigative question | Zone commitment check |
|-------------|------|------------------------|-----------------------|
| [name] | breadth/depth/synthesis | [...?] | [Which row from the zone's commitment block does this phase address?] |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative form, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo; YAML annotations are transcribed from
the backward derivation, not authored from skill knowledge. Status-quo path displaced: each
stage producing whatever its skills naturally output (R-02).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07). Row 0 is where derivation begins; execution reads
the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Steps 3-10

Steps 3-10 follow the same pattern as V-01. Terminal checklist includes all C-01 through C-43
items (same as V-01 checklist).

---

## V-05 -- Combined: Role Sequence + Inertia Framing with AVOID Blocks

**Axis**: Combined. Role-responsibility table precedes the opening failure taxonomy (role
sequence axis) AND each construction step carries an explicit AVOID block naming the
status-quo behavior it replaces (inertia framing axis). Zone commitment + status-quo
columns preserved from V-01.

**Hypothesis**: AVOID blocks per step make the status-quo framing pervasive at every
procedural decision point, extending C-43's manifest-level status-quo naming into the
procedural body of the protocol. Combined with role attribution, each step now carries:
who owns it AND what inertia behavior to avoid. C-41/C-42/C-43 preserved from V-01.
Anticipated score: 36/36 aspirational.

**C-41 form**: Same as V-01 -- both tables with independent completeness assertions
**C-42 form**: Same as V-01 -- 3-part zone commitment criteria pre-catalog; zone commitment
             check column in phase table and ARTIFACT 1
**C-43 form**: Same as V-01 -- status-quo columns in both tables
**Additional axes**: Role table before failure taxonomy; each step has AVOID block per R-NN

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Four roles share construction
responsibility. Each role counters a specific class of failure:

| Role | Construction responsibility | Failure class countered |
|------|----------------------------|------------------------|
| PM | Topic and phase naming from investigation intent | F-1 at naming layer |
| Architect | Arc design; zone commitment; gate design; ARTIFACT 0 | F-1 at construction layer; F-2 at convention layer |
| Dev | Skill selection; ARTIFACT 2 assembly; YAML transcription | F-1 at assembly layer |
| Team Lead | Zone commitment audit; compliance; terminal validation | F-1 and F-2 completeness |

Before writing a single stage, internalize the two failure modes this protocol counters:

| Failure ID | Failure Name | Status-Quo Failure (inertia) | What it produces | Design counter-move |
|------------|--------------|------------------------------|------------------|---------------------|
| F-1 | Catalog-first construction | Open the catalog; group skills by namespace; name stages after clusters; append echo at end | Stages labeled after skill clusters; zone membership implied by grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; backward derivation from echo seeds every stage boundary |
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted.

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

This table is exhaustive: every construction rule in this protocol appears as exactly one row.
No rule is omitted.

Every skill runs standalone; the program is a plan, not an executor. The chain begins at the
end: echo is the terminal consumer whose implicit information needs seed the entire backward
derivation that determines every prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Status-Quo Failure | Criterion ladder |
|-------|--------------------------|-------------------|-----------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- committed before catalog opens | Zone membership implied by namespace grouping; invisible to auditors | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | Inferred from gate prose; breaks on stage reordering | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | "Assess the area" non-questions; intent absent | Question-framing ladder |

**Lifecycle zones with commitment criteria** (declared before the catalog opens):

**Breadth zone** -- do we understand the problem space well enough to commit to a direction?
Scout and draft skills produce breadth artifacts. Status-quo failure: namespace grouping
implies zone membership without declaring a commitment decision.

Breadth zone commitment criteria (all three must be satisfied before advancing to depth):
1. Zone-exit question: "Have we named the problem space, identified key constraints, and
   committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor: at least one competitor or market signal artifact, at least one
   feasibility artifact, at least one draft artifact (spec or proposal)
3. Required gate pattern class: at least one compound gate with `>= 2` count floor on a
   scout or draft skill artifact from a stage in this zone

**Depth zone** -- does our design survive adversarial conditions before shipping commitment?
Status-quo failure: depth stages accumulate prove/review skills without naming what
adversarial condition each addresses.

Depth zone commitment criteria (all three must be satisfied before advancing to synthesis):
1. Zone-exit question: "Has the design been tested against failure modes and adversarial
   conditions by reviewers who did not author the spec?"
2. Artifact-type floor: at least one review artifact, at least one flow or trace artifact,
   at least one prove artifact
3. Required gate pattern class: at least one compound gate referencing a review or prove
   skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** -- are users adopting and signaling as expected post-launch?
Status-quo failure: listen/metrics appended at the end without a declared adoption model.

Synthesis zone commitment criteria (all three must be satisfied before echo advances):
1. Zone-exit question: "Are post-launch signals tracking against the adoption model the
   team committed to before shipping?"
2. Artifact-type floor: at least one listen artifact, at least one metrics or goals artifact
3. Required gate pattern class: compound gate with count floor on a listen, metrics, or
   goals skill artifact from a stage in this zone

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

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

1. Declare the topic (Step 1) -- Owner: PM
2. Declare arc phases -- **catalog closed until Step 3** (Step 2) -- Owner: PM / Architect
3. Select skills (Step 3) -- Owner: Dev
4. Assign skills to phases (Step 4) -- Owner: Dev
5a. Design gates (Step 5a) -- Owner: Architect
5b. FORWARD REFERENCE audit (Step 5b) -- Owner: Architect
6. Write per-phase intent questions (Step 6) -- Owner: PM
7. Encode `evidence_arc:` field (Step 7) -- Owner: PM
8. Assemble YAML (Step 8) -- Owner: Dev
9. Per-stage compliance table (Step 9) -- Owner: Team Lead
10. Terminal checklist (Step 10) -- Owner: Team Lead

---

#### Step 1 -- Topic (Owner: PM)

State the topic name.

> **AVOID** (R-01, status-quo): Selecting a topic name that maps directly to a namespace
> cluster. Topic names must be coherent with the investigative problem, not with skill
> availability.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01 -- counter-move against F-1).

> **AVOID** (R-01, status-quo): Opening the catalog first, grouping skills by namespace,
> then naming phases after the groups you see. This is F-1 entering at Step 2.

Declare 3--6 phase boundaries from first principles. Assign each to a zone using the
commitment criteria declared above as the assignment test.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which commitment criteria does this phase address?] | PM / Architect |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema (Owner: Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative form, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo; YAML annotations are transcribed from
the backward derivation, not authored from skill knowledge. Status-quo path displaced: each
stage producing whatever its skills naturally output (R-02).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07). Row 0 is where derivation begins; execution reads
the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward its
zone's artifact-type floor.

> **AVOID** (R-01, status-quo): Selecting all skills in a namespace cluster and letting
> the selection drive zone assignment. Status-quo path: selection precedes zone assignment.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. Verify zone commitment artifact floors are satisfiable.

> **AVOID** (R-01, status-quo): Creating new phases at assignment time to accommodate skills
> that don't fit the declared arc. Discard skills without a matching phase; do not create phases.

---

#### Step 5a -- Design Gates (Owner: Architect)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Count floors: breadth and depth `>= 2`; synthesis `>= 1`. Verify the final stage in each
zone satisfies its required gate pattern class.

> **AVOID** (R-03, status-quo): Writing gates as prose task-completion checks ("adequate
> signals present", "discovery complete"). These are the status-quo path R-03 displaces.

---

#### Step 5b -- FORWARD REFERENCE audit (Owner: Architect)

For each non-echo stage: verify every artifact type in the gate is producible by a skill in
that stage's `skills` array. Fix all forward references before Step 6.

> **AVOID** (R-04, status-quo): Referencing the most obvious artifact without verifying
> the current stage's skills can produce it. This is the status-quo path R-04 displaces.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

Write a genuine interrogative ending with `?` for each phase. Zone-specific questions only.

> **AVOID** (status-quo): Non-interrogative intent statements ("assess the market landscape")
> or task-completion pseudo-questions ("are we done with discovery?").

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels]
  depth:     [depth-zone phase labels]
  synthesis: [synthesis-zone phase labels]
```

Verify each zone's commitment criteria are satisfiable given the labels and skills assigned.

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why echo occupies row 0 -- counter-move against F-2.

> **AVOID** (R-06, status-quo): Placing echo at row N because "execution ends there." This
> is the status-quo path R-06 displaces. Row 0 is where derivation begins.

> **AVOID** (R-05, status-quo): Authoring YAML annotations from skill knowledge rather than
> transcribing from ARTIFACT 2. The matrix is the sole authoritative source.

**ARTIFACT 2 is the sole authoritative source.** Transcribe YAML from the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

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

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

```
[ ] C-01 through C-40: (same as V-01)
[ ] C-41: opening failure taxonomy table carries INDEPENDENT completeness assertion ("This
         table is self-certifying: every failure mode appears as exactly one row. Two rows;
         no failure mode omitted."); RULE COVERAGE TABLE carries INDEPENDENT completeness
         assertion ("This table is exhaustive: every construction rule appears as exactly one
         row. No rule is omitted."); BOTH assertions present; NEITHER references the other
[ ] C-42: breadth, depth, and synthesis zone commitment criteria (3-part each) declared before
         catalog opens; ARTIFACT 1 and phase table both include "Zone commitment check" column
[ ] C-43: RULE COVERAGE TABLE has "Status-Quo Path" column (7 rows); opening failure taxonomy
         has "Status-Quo Failure" column (2 rows); BOTH columns present in their tables
```
