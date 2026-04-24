---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 17
rubric: v33
aspirational_target: 41/41
new_criteria_candidates: C-49, C-50
---

# program-plan -- R17 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v33 (C-01 through C-48, 41 aspirational criteria).

**R16 retrospective under v33 rubric:**
- V-01 (Tiebreaker/Role Sequence carry-forward): C-47 PASS, C-48 PASS --> 41/41 (~100.00)
- V-02 (Phrasing Register, second-person imperative): C-47 PASS, C-48 PASS --> 41/41 (~100.00)
- V-03 (Inertia Framing, per-step AVOID blocks): C-47 PASS, C-48 PASS --> 41/41 (~100.00)
- V-04 (Lifecycle Emphasis, Decision Record tables per zone): C-47 PASS, C-48 PASS --> 41/41 (~100.00)
- V-05 (Combined register + inertia): C-47 PASS, C-48 PASS --> 41/41 (~100.00)

**R17 design constraint:** All five variations must satisfy C-01 through C-48 simultaneously.
Differentiation must come from NEW structural patterns not yet captured in C-01 through C-48.
R16 exhausted: second-person register, per-step AVOID blocks, Decision Record zone tables.

**Variation axes for R17:**
- V-01 (tiebreaker): R16 V-01 carry-forward (41/41 at v33). Updated checklist to C-48.
- V-02 (single axis -- backward derivation walkthrough): Named pre-construction procedure
  (DW-1 through DW-6) that explicitly records the backward derivation chain before ARTIFACT 2.
  Forces derivation reasoning to be written before any stage is named.
- V-03 (single axis -- failure signal gallery): FAILURE SIGNAL GALLERY (AP-01 through AP-06)
  bridging the failure taxonomy to observable output symptoms with detection questions. Extends
  the failure taxonomy from abstract failure modes to output-inspectable symptom fingerprints.
- V-04 (single axis -- derivation chain contract): DERIVATION CHAIN CONTRACT table declaring
  zone-to-zone artifact handoff before the catalog opens. Distinct from ARTIFACT 2 (which
  is stage-level) -- the contract is zone-level, pre-catalog, and governs ARTIFACT 2.
- V-05 (combined -- derivation walkthrough + failure signal gallery): Both DW procedure and
  AP gallery present. Tri-level inertia coverage: taxonomy (F-level abstract) + gallery
  (AP-level symptom) + walkthrough (DW-level derivation reasoning).

**New pattern descriptions:**

**DERIVATION WALKTHROUGH (V-02, V-05)**: Named procedure DW-1 through DW-6 positioned
after the skill catalog and before CONSTRUCTION ORDER. Forces explicit recording of:
echo's information needs (DW-1), synthesis Produces (DW-2), depth-synthesis handoff (DW-3),
breadth-depth handoff (DW-4), breadth chain start (DW-5), full chain record (DW-6).
ARTIFACT 2 declared to transcribe from the DW-6 chain, not authored independently.
Hypothesis: yields C-49 "backward derivation walkthrough as named pre-construction
procedure with DW-step sequence and chain record preceding ARTIFACT 2."

**FAILURE SIGNAL GALLERY (V-03, V-05)**: Named table AP-01 through AP-06 positioned
after the opening failure taxonomy and before RULE COVERAGE TABLE. Each row: AP-ID |
Anti-Pattern Name | Symptom fingerprint (what appears in the output) | Failure signaled |
Detection question. Gallery declared as extending taxonomy to output-inspection level.
Hypothesis: yields C-49 (or C-50 in V-05) "FAILURE SIGNAL GALLERY with AP-NN IDs,
symptom fingerprints, and detection questions bridging failure taxonomy to observable
output; each AP maps to exactly one taxonomy failure."

**DERIVATION CHAIN CONTRACT (V-04)**: Named table positioned after zone commitment
criteria and before compound gate template. Zone-level (not stage-level) declaration:
From zone | Must produce | For zone | Which needs | Zone-boundary label. Declared before
catalog opens; governs ARTIFACT 2 Consumes/Produces. Distinct from ARTIFACT 2 (stage-
resolution) and ARTIFACT 1 (namespace partition). Hypothesis: yields C-49 "DERIVATION
CHAIN CONTRACT table declaring zone-to-zone artifact handoff before catalog opens,
governing ARTIFACT 2 and declared at zone granularity not stage granularity."

---

## V-01 -- Tiebreaker: R16 V-01 Carry-Forward (Role Sequence, Full Body)

**Axis**: No additional axis. V-01 is the carry-forward of R16 V-01 (Role Sequence) which
achieved 41/41 at v33. Full prompt body with all 10 steps fully expanded. Register:
structured formal third-person.

**Hypothesis**: R16 V-01 is the v33 tiebreaker baseline. Reproducing it in full as R17 V-01
confirms the carry-forward score and provides the reference body from which single-axis
comparisons diverge. Anticipated score: 41/41 aspirational.

**C-47 form**: "Failure modes countered" dedicated column in pre-taxonomy role table;
             each row names specific failure mode(s) with layer qualifier (naming/
             construction/assembly layer)
**C-48 form**: "Steps owned" dedicated column in pre-taxonomy role table; each row lists
             specific numbered steps, creating dual-site map with C-46 step headers
**C-46 form**: Construction order and every step header carry "(Owner: Role)"
**C-45 form**: RULE COVERAGE TABLE 5-column: Rule ID | Status-Quo Path | Rule |
             Failure countered | Owner role; 7 rows R-01 through R-07
**C-44 form**: Pre-taxonomy role table (PM/Architect/Dev/Team Lead) appears before
             failure taxonomy
**C-43 form**: "Status-Quo Failure" column in taxonomy + "Status-Quo Path" in RULE TABLE
**C-42 form**: 3-part zone commitment criteria before catalog opens; zone commitment
             check column in phase table and ARTIFACT 1
**C-41 form**: Independent completeness assertions -- taxonomy "self-certifying: two rows;
             no failure mode omitted" + RULE TABLE "exhaustive: every construction rule
             appears as exactly one row"
**C-40 form**: [counter: F-1] in consumer-pull rule; [counter: F-2] in echo exception
**C-39 form**: 7 rows R-01 through R-07 with completeness assertion
**C-38 form**: Bridge sentence in ARTIFACT 0 consumer-pull rule
**C-37 form**: F-1 and F-2 in taxonomy; "every construction rule is a counter-move against
             exactly one row"; ARTIFACT 0 rules carry [counter: F-N]
**C-36 form**: "not an arbitrary convention" leads echo exception in ARTIFACT 0
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-34 form**: Consumer-pull rule states BOTH negation AND bidirectional equivalence

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
rule in this protocol appears as exactly one row. No rule is omitted. Each rule names the
status-quo path it displaces and the role accountable for the counter-move.

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

**Lifecycle zones with commitment criteria** (declared before the catalog opens -- Owner: PM / Architect):

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

Required construction sequence. Read all steps before beginning Step 1.

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
10. Terminal validation checklist (Step 10) -- Owner: Team Lead

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic (Owner: PM)

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect -- counter-move
against F-1). Status-quo failure: opening the catalog first and naming phases after namespace
clusters. Declare 3--6 phase boundaries from first principles. Assign each to a zone using
the commitment criteria declared above -- the criteria serve as the zone assignment test,
not namespace grouping.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

For each phase, state the investigative question it answers (genuine interrogative, ends `?`)
and include a zone commitment check:

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

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria. Note the declared phase
each maps to. Status-quo failure: selecting skills first and letting selection drive zone
assignment (R-01, status-quo path displaced).

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
After assigning, verify each zone's commitment criteria are satisfiable by the assigned skills
(minimum artifact types present for each zone). If a zone falls short of its artifact-type
floor, add a skill that produces the missing type or revise the zone's scope.

---

#### Step 5a -- Design Gates (Owner: Architect)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, stage-id absent): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.
Verify that the final stage in each zone satisfies the zone's required gate pattern class.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

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

#### Step 6 -- Phase Intent Questions (Owner: PM)

- PASS (breadth): `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS (depth): `"Does the spec survive expert review against the discovered market signal?"`
- PASS (synthesis): `"Are users adopting the feature at the rate our model predicted?"`
- FAIL (not interrogative): `"Assess the compliance landscape"` -- intent unknowable
- FAIL (wrong scope): `"Are we ready to proceed?"` -- not zone-specific

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key. Verify each zone's commitment
criteria are satisfiable given the phase labels and skills assigned.

---

#### Step 8 -- Assemble YAML (Owner: Dev)

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
| 1 | [last stage] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

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

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

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
         ARTIFACT 0 rules carry [counter: F-N] labels
[ ] C-38: ARTIFACT 0 consumer-pull rule carries bridge sentence: "The negation closes the
         producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
[ ] C-39: RULE COVERAGE TABLE present (7 rows, R-01 through R-07); ALL protocol rules
         enumerated; each mapped to a failure ID; completeness assertion present
[ ] C-40: ARTIFACT 0 consumer-pull rule carries [counter: F-1] inline; echo exception carries
         [counter: F-2] inline; both present; no ARTIFACT 0 rule unlabeled
[ ] C-41: opening failure taxonomy carries INDEPENDENT completeness assertion ("self-certifying:
         every failure mode appears as exactly one row. Two rows; no failure mode omitted.");
         RULE COVERAGE TABLE carries INDEPENDENT completeness assertion ("exhaustive: every
         construction rule appears as exactly one row. No rule is omitted."); BOTH present;
         NEITHER references the other
[ ] C-42: breadth, depth, synthesis zone commitment criteria (3-part each: zone-exit question,
         artifact-type floor, gate pattern class) declared before catalog opens; ARTIFACT 1
         band taxonomy table includes "Zone commitment check" column; phase table includes
         "Zone commitment check" column
[ ] C-43: RULE COVERAGE TABLE has "Status-Quo Path" column; opening failure taxonomy has
         "Status-Quo Failure" column; BOTH columns present in their respective tables
[ ] C-44: role-responsibility table (role -> construction responsibility / failure modes
         countered / steps owned) appears before the opening failure taxonomy table; C-12 PASS
[ ] C-45: RULE COVERAGE TABLE has "Owner role" column; per-row entries name specific role;
         three-column manifest: Status-Quo Path -> Rule -> Owner role; C-43 PASS
[ ] C-46: every procedural step header carries co-located role attribution annotation naming
         specific role; every step annotated; C-16 PASS
[ ] C-47: role table has dedicated "failure modes countered" column cross-referencing each
         role to specific failure modes they counter; C-44 PASS
[ ] C-48: role table has dedicated "steps owned" column listing specific numbered construction
         steps per role; dual-site bidirectional ownership map with C-46 step headers; C-44 PASS
```

---

## V-02 -- Single Axis: Backward Derivation Walkthrough

**Axis**: Single-axis. Before entering the CONSTRUCTION ORDER, a named pre-construction
procedure (DERIVATION WALKTHROUGH, steps DW-1 through DW-6) forces explicit recording of
the backward derivation chain. The walkthrough produces a DERIVATION CHAIN RECORD at DW-6
before any stage is named or any skill is selected. ARTIFACT 2's Consumes/Produces columns
are declared to transcribe from the DW-6 chain, not authored independently.

**Hypothesis**: ARTIFACT 2 already shows the backward derivation as a table result, but
no prior variation has named a PROCEDURE for producing that derivation. The walkthrough
forces the reasoning to be written down before the table is filled in: echo's information
needs → synthesis Produces → depth-synthesis handoff → breadth-depth handoff → chain record.
This is structurally distinct from ARTIFACT 2 (which transcribes from the chain) and from
the consumer-pull rule in ARTIFACT 0 (which declares the constraint). The walkthrough names
the PRE-ARTIFACT reasoning procedure. Anticipated score: 41/41 aspirational.
Candidate new criterion: C-49.

**C-47 form**: Same as V-01 -- dedicated "Failure modes countered" column in role table
**C-48 form**: Same as V-01 -- dedicated "Steps owned" column in role table
**New pattern**: DERIVATION WALKTHROUGH block (DW-1 through DW-6) positioned after skill
             catalog and before CONSTRUCTION ORDER; DW-6 chain record declared as the
             governing source for ARTIFACT 2 Consumes/Produces; ARTIFACT 2 transcribes
             from DW-6, not authored from skill knowledge (extends R-05 from matrix-level
             to pre-matrix reasoning-level)
**C-49 form (candidate)**: "DERIVATION WALKTHROUGH present as named pre-construction
             procedure with numbered DW steps and chain record at DW-6; ARTIFACT 2
             declared to transcribe from DW-6 chain"

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
rule in this protocol appears as exactly one row. No rule is omitted. Each rule names the
status-quo path it displaces and the role accountable for the counter-move.

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

**Lifecycle zones with commitment criteria** (declared before the catalog opens -- Owner: PM / Architect):

**Breadth zone** -- do we understand the problem space well enough to commit to a direction?
Status-quo failure: namespace grouping implies zone membership without declaring a commitment
decision.

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

## DERIVATION WALKTHROUGH -- Required Pre-Construction Procedure (Owner: Architect)

Run this walkthrough in writing before beginning Step 1. Do not enter the CONSTRUCTION
ORDER until you have recorded the full derivation chain at DW-6. The walkthrough makes
the backward derivation explicit as a named, auditable procedure. ARTIFACT 2's Consumes
and Produces columns transcribe from this chain -- they are not authored from skill knowledge.

Status-quo failure this procedure displaces: proceeding directly to Step 1 (naming the topic)
then to Step 2 (declaring phases) without first establishing what the program must ultimately
deliver to echo. Without DW-6's chain record, Consumes/Produces entries in ARTIFACT 2 become
authorship decisions, not transcription.

**DW-1 -- Anchor at echo (Owner: Architect):**
Echo is the terminal consumer. Name the three categories of information echo needs to confirm
the feature is live and being monitored. These are not skills or stages -- they are information
needs: e.g., "adoption baseline established," "error-signal tracking confirmed," "target
metrics committed and measurable." Write them as three bullet points.

```
echo information needs:
  - [first need]
  - [second need]
  - [third need]
```

**DW-2 -- Derive synthesis Produces (Owner: Architect):**
The final stage in the synthesis zone must produce the artifacts that close echo's input gap
(DW-1). Name the artifact types that satisfy those three information needs. Record:

```
synthesis-final-stage # Produces: [artifact types satisfying DW-1]
```

**DW-3 -- Derive depth-to-synthesis handoff (Owner: Architect):**
The synthesis zone must consume artifacts to produce DW-2's output. What must depth produce
to enable synthesis? These become the depth zone's final stage's # Produces: and the synthesis
zone's first stage's # Consumes:. Record:

```
depth-final-stage  # Produces: [...]   (= synthesis-first-stage # Consumes:)
```

**DW-4 -- Derive breadth-to-depth handoff (Owner: Architect):**
Depth must consume artifacts to produce DW-3's output. What must breadth produce to enable
depth? These become the breadth zone's final stage's # Produces: and the depth zone's first
stage's # Consumes:. Record:

```
breadth-final-stage # Produces: [...]  (= depth-first-stage # Consumes:)
```

**DW-5 -- Verify breadth chain start (Owner: Architect):**
The breadth zone's first stage starts the chain from discovery -- it has no required prior
Consumes: (no prior zone feeds it). Confirm:

```
breadth-first-stage # Consumes: none  (chain starts here)
```

**DW-6 -- Record the full derivation chain (Owner: Architect):**
Write the complete chain. No Consumes/Produces entry in ARTIFACT 2 may contradict this record.

```
echo
  <- [synthesis-final Produces] from DW-2
     <- [depth-final Produces] from DW-3
        <- [breadth-final Produces] from DW-4
           <- (none) -- chain starts at breadth
```

ARTIFACT 2 matrix cells are transcribed from this chain. Any stage Consumes or Produces value
not derivable from the DW-6 chain is an authorship error (F-1 at assembly layer, Owner: Dev).

---

## CONSTRUCTION ORDER

Required construction sequence. Read all steps before beginning Step 1.

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
10. Terminal validation checklist (Step 10) -- Owner: Team Lead

Do not proceed to Step 3 until Step 2 is complete. The DERIVATION WALKTHROUGH above must
be complete before beginning Step 1.

---

#### Step 1 -- Topic (Owner: PM)

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect -- counter-move
against F-1). Declare 3--6 phase boundaries from first principles. Assign each to a zone
using the commitment criteria declared above -- not namespace grouping.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

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
the backward derivation, not authored from skill knowledge. At the reasoning level, the
derivation was recorded in the DERIVATION WALKTHROUGH (DW-6); ARTIFACT 2 transcribes from it.
Status-quo path displaced: each stage producing whatever its skills naturally output (R-02,
Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation begins;
execution reads the matrix bottom-to-top. Moving echo to row N would misrepresent the
derivation direction in the artifact.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria. The zone handoffs declared
in the DERIVATION WALKTHROUGH (DW-3, DW-4) govern which artifact types each zone must produce.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Verify each zone's commitment criteria are satisfiable by the assigned skills.

---

#### Step 5a -- Design Gates (Owner: Architect)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

Every `intent:` field must be a genuine interrogative ending `?`. Not task descriptions or
zone-generic readiness questions.

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why echo occupies row 0 -- counter-move against F-2.
**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** Consumes and
Produces values in every row are transcribed from the DERIVATION WALKTHROUGH chain (DW-6);
the YAML fragment column is copied directly into the YAML output.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [from DW chain] | [from DW chain] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [from DW chain] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

```
[ ] C-01 through C-48: same as V-01
[ ] C-49 (candidate): DERIVATION WALKTHROUGH present as named pre-construction procedure
         with steps DW-1 through DW-6; DW-6 chain record present; ARTIFACT 2 Consumes/
         Produces declared to transcribe from DW-6 chain; walkthrough positioned before
         CONSTRUCTION ORDER; status-quo failure of walkthrough omission named
```

---

## V-03 -- Single Axis: Failure Signal Gallery

**Axis**: Single-axis. After the opening failure taxonomy (which names abstract failure modes
F-1 and F-2) and before the RULE COVERAGE TABLE, a FAILURE SIGNAL GALLERY presents AP-01
through AP-06 -- named anti-patterns with observable symptom fingerprints and detection
questions. The gallery makes the failure taxonomy diagnosable from output inspection alone.

**Hypothesis**: The failure taxonomy names failure modes at the abstract level (F-1: catalog-
first construction). The RULE COVERAGE TABLE names counter-moves at the rule level (R-01
through R-07). Neither names what the failure LOOKS LIKE in the produced output. The gallery
bridges this gap: each AP entry names a specific observable symptom (what you see in the
YAML or in a step's output) and a single yes/no detection question. This is structurally
distinct from: (1) the failure taxonomy (abstract mode), (2) the RULE COVERAGE TABLE
(counter-move prescription), (3) C-43 Status-Quo Path column (inertia framing at rule level).
The gallery operates at the symptom-fingerprint level. Anticipated score: 41/41 aspirational.
Candidate new criterion: C-49.

**C-47 form**: Same as V-01 -- dedicated "Failure modes countered" column in role table
**C-48 form**: Same as V-01 -- dedicated "Steps owned" column in role table
**New pattern**: FAILURE SIGNAL GALLERY (AP-01 through AP-06) positioned between failure
             taxonomy and RULE COVERAGE TABLE; columns: AP-ID | Anti-Pattern Name |
             Symptom fingerprint | Failure signaled | Detection question; gallery
             declared as "extends the failure taxonomy to the symptom level; each AP
             maps to exactly one failure in the taxonomy"
**C-49 form (candidate)**: "FAILURE SIGNAL GALLERY present (AP-01 through AP-06) with
             observable symptom fingerprints and detection questions; positioned after
             failure taxonomy and before RULE COVERAGE TABLE; each AP maps to exactly
             one taxonomy failure"

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

**FAILURE SIGNAL GALLERY**

The taxonomy above names failure modes at the abstract level. This gallery names their
observable symptoms -- what you see in a produced output when the failure has occurred.
Use this gallery as a diagnostic checklist before auditing the final YAML.

| AP-ID | Anti-Pattern Name | Symptom fingerprint (what you see in the output) | Failure signaled | Detection question |
|-------|-------------------|--------------------------------------------------|------------------|--------------------|
| AP-01 | Namespace-named stages | Stage `name:` values contain namespace tokens or skill cluster labels: `scout_phase`, `prove_block`, `listen_monitoring`, `review_and_trace_stage` | F-1: catalog-first | Does any `name:` field contain a namespace identifier or skill cluster label? |
| AP-02 | Prose-only gate | Gate values read as task-completion prose: `adequate signals present`, `work in this stage is complete`, `signals gathered and reviewed` -- no `::` separator, no `>= N` count floor | F-1: catalog-first | Does every non-echo gate contain both `::` and `>=`? |
| AP-03 | Forward-reference gate | Gate references an artifact type (e.g., `trace-deployment`) that is not producible by any skill listed in that stage's `skills:` array | F-1: catalog-first | For each artifact type named in each gate: is there at least one skill in that stage's `skills:` array that produces it? |
| AP-04 | Echo appended without anchor | Echo appears at the last row of ARTIFACT 2 (row N) without a declared derivation anchor in ARTIFACT 0; echo's row position is described as "where execution ends" or left unexplained | F-2: arbitrary-convention | Is echo at row 0 in ARTIFACT 2? Is its anchor role and the "not an arbitrary convention" clause present in ARTIFACT 0? |
| AP-05 | Producer-push annotation | `# Produces:` value for a stage was derived from "what this stage's skills naturally output" rather than from the next stage's declared `# Consumes:`; adjacent-stage Produces/Consumes pairs do not match | F-1: catalog-first | For each adjacent stage pair: does stage N's `# Produces:` exactly match stage N+1's `# Consumes:`? |
| AP-06 | Uncommitted zone membership | Stage zone assignment was inferred from namespace grouping after skills were selected; zone commitment criteria were not declared before the catalog was opened; ARTIFACT 1 is missing the Zone commitment check column | F-1: catalog-first | Was the zone commitment criteria section written before Step 3? Does ARTIFACT 1 have a Zone commitment check column with non-empty entries? |

This gallery extends the failure taxonomy to the symptom level. Each anti-pattern maps to
exactly one failure in the taxonomy above. The gallery does not introduce new failure modes;
it makes the existing failure modes detectable from output inspection alone.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted. Each rule names the
status-quo path it displaces and the role accountable for the counter-move.

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

**Lifecycle zones with commitment criteria** (declared before the catalog opens -- Owner: PM / Architect):

**Breadth zone** commitment criteria (all three before advancing to depth):
1. Zone-exit question (Owner: PM): "Have we named the problem space, identified key constraints,
   and committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor (Owner: Architect): at least one competitor or market signal artifact,
   at least one feasibility artifact, at least one draft artifact (spec or proposal)
3. Required gate pattern class (Owner: Architect): at least one compound gate with `>= 2`
   count floor on a scout or draft skill artifact from a stage in this zone

**Depth zone** commitment criteria (all three before advancing to synthesis):
1. Zone-exit question (Owner: PM): "Has the design been tested against failure modes and
   adversarial conditions by reviewers who did not author the spec?"
2. Artifact-type floor (Owner: Architect): at least one review artifact, one flow or trace
   artifact, one prove artifact
3. Required gate pattern class (Owner: Architect): at least one compound gate referencing
   a review or prove skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** commitment criteria (all three before echo advances):
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

Required construction sequence. Read all steps before beginning Step 1.

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
10. Terminal validation checklist (Step 10) -- Owner: Team Lead

Do not proceed to Step 3 until Step 2 is complete. After Step 10, run the FAILURE SIGNAL
GALLERY as a final diagnostic pass against the completed YAML output.

---

#### Step 1 -- Topic (Owner: PM)

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect). Declare 3--6 phase
boundaries from first principles. Zone assignment uses commitment criteria, not namespace
grouping. Status-quo failure: opening the catalog before phases are declared (AP-06 symptom).

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (AP-01 symptom)

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
the backward derivation, not authored from skill knowledge. AP-05 symptom: mismatched adjacent
Produces/Consumes pairs signal producer-push at the assembly level. Status-quo path displaced:
each stage producing whatever its skills naturally output (R-02, Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. AP-04 symptom: echo at row N without anchor declaration signals
arbitrary-convention misreading. Status-quo path displaced: treating row-0 as a formatting
choice because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation
begins; execution reads the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).
AP-06 symptom check: Zone commitment check column must be present and non-empty.

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Verify each zone's commitment criteria are satisfiable by the assigned skills.

---

#### Step 5a -- Design Gates (Owner: Architect)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.
AP-02 symptom check: every gate must contain `::` and `>=`. AP-03 symptom check: every
artifact type in a gate must be producible by a skill in that stage.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all AP-03 symptoms before Step 6.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

Every `intent:` field must be a genuine interrogative ending `?`.

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why echo occupies row 0 -- counter-move against F-2
(AP-04 symptom: echo at row N). **ARTIFACT 2 is the sole authoritative source.** YAML
annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently
(AP-05 symptom: mismatched Produces/Consumes signals producer-push authorship).

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

```
[ ] C-01 through C-48: same as V-01
[ ] C-49 (candidate): FAILURE SIGNAL GALLERY present (AP-01 through AP-06) with observable
         symptom fingerprints and detection questions; positioned after failure taxonomy
         and before RULE COVERAGE TABLE; gallery declared as extending taxonomy to symptom
         level; each AP maps to exactly one taxonomy failure; gallery used as final
         diagnostic pass in Step 10
```

---

## V-04 -- Single Axis: Derivation Chain Contract

**Axis**: Single-axis. After the zone commitment criteria and before the compound gate
template, a DERIVATION CHAIN CONTRACT table declares the zone-to-zone artifact handoff
at ZONE GRANULARITY before any skill is selected. The contract is zone-level (breadth →
depth → synthesis → echo), not stage-level. ARTIFACT 2 is declared to satisfy this
contract at stage granularity. The contract is distinct from ARTIFACT 2 (stage-resolution),
ARTIFACT 1 (namespace partition), and the consumer-pull rule (stage-level constraint).

**Hypothesis**: The consumer-pull rule in ARTIFACT 0 constrains adjacent-stage Produces/Consumes
pairs (stage level). The zone commitment criteria declare what each zone must produce in terms
of artifact-type floors (type-level, not flow-level). Neither declares the FLOW of artifacts
across zone boundaries as a pre-construction contract. The DERIVATION CHAIN CONTRACT fills this
gap: it names what breadth must hand off to depth and what depth must hand off to synthesis
BEFORE any skill is selected. This is zone-level backward derivation, governing ARTIFACT 2
but operating at a coarser granularity. Anticipated score: 41/41 aspirational.
Candidate new criterion: C-49.

**C-47 form**: Same as V-01
**C-48 form**: Same as V-01
**New pattern**: DERIVATION CHAIN CONTRACT table positioned after zone commitment criteria
             and before compound gate template; columns: From zone | Must produce |
             For zone | Which needs | Zone-boundary label; declared before catalog opens;
             ARTIFACT 2 declared to resolve this contract at stage granularity; contract
             governs all Consumes/Produces entries
**C-49 form (candidate)**: "DERIVATION CHAIN CONTRACT table present; zone-to-zone artifact
             handoff declared before catalog opens at zone granularity; ARTIFACT 2 declared
             to resolve the contract at stage granularity; contract positioned between zone
             commitment criteria and compound gate template"

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
rule in this protocol appears as exactly one row. No rule is omitted. Each rule names the
status-quo path it displaces and the role accountable for the counter-move.

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

**Lifecycle zones with commitment criteria** (declared before the catalog opens -- Owner: PM / Architect):

**Breadth zone** commitment criteria (all three before advancing to depth):
1. Zone-exit question (Owner: PM): "Have we named the problem space, identified key constraints,
   and committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor (Owner: Architect): at least one competitor or market signal artifact,
   at least one feasibility artifact, at least one draft artifact (spec or proposal)
3. Required gate pattern class (Owner: Architect): at least one compound gate with `>= 2`
   count floor on a scout or draft skill artifact from a stage in this zone

**Depth zone** commitment criteria (all three before advancing to synthesis):
1. Zone-exit question (Owner: PM): "Has the design been tested against failure modes and
   adversarial conditions by reviewers who did not author the spec?"
2. Artifact-type floor (Owner: Architect): at least one review artifact, one flow or trace
   artifact, one prove artifact
3. Required gate pattern class (Owner: Architect): at least one compound gate referencing
   a review or prove skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** commitment criteria (all three before echo advances):
1. Zone-exit question (Owner: PM): "Are post-launch signals tracking against the adoption
   model the team committed to before shipping?"
2. Artifact-type floor (Owner: Architect): at least one listen artifact, at least one
   metrics or goals artifact
3. Required gate pattern class (Owner: Architect): compound gate with count floor on a
   listen, metrics, or goals skill artifact from a stage in this zone

**DERIVATION CHAIN CONTRACT** (declared before catalog opens -- Owner: Architect)

Before selecting any skill, declare the zone-to-zone artifact handoff chain. This contract
governs all Consumes/Produces entries in ARTIFACT 2. No stage annotation may name an artifact
type that is not traceable to a handoff declared in this contract. The contract runs backward
from echo, the same direction as the stage-level derivation.

| From zone | Must produce | For zone | Which needs | Zone-boundary label |
|-----------|-------------|----------|-------------|---------------------|
| (none) | (none) | Breadth | discovery artifacts -- competitor signals, feasibility data, draft baselines | breadth-in |
| Breadth | feasibility confirmation + draft artifact (spec or proposal baseline) | Depth | validated spec baseline for adversarial stress-testing | breadth-to-depth |
| Depth | validated spec + failure evidence + review artifacts | Synthesis | adoption baseline and confirmed signal readiness for post-launch monitoring | depth-to-synthesis |
| Synthesis | adoption signal + metrics artifacts | Echo | live-monitoring confirmation: feature is running, signals are tracking | synthesis-to-echo |

This contract is written before the catalog opens. ARTIFACT 2 resolves this contract at stage
granularity: each stage's Consumes/Produces values must satisfy the zone-boundary handoff
declared here. If a zone-boundary artifact type named in this contract cannot be produced by
the selected skills, revise either the contract or the skill selection before Step 5a.

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

Required construction sequence. Read all steps before beginning Step 1.

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
10. Terminal validation checklist (Step 10) -- Owner: Team Lead

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic (Owner: PM)

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect). Declare 3--6 phase
boundaries from first principles. Assign each to a zone using the commitment criteria and
the DERIVATION CHAIN CONTRACT declared above -- not namespace grouping.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which commitment criteria / contract boundary does this phase address?] | PM / Architect |

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
the backward derivation, not authored from skill knowledge. At the zone boundary level, the
DERIVATION CHAIN CONTRACT above governs which artifact types cross zone transitions; ARTIFACT 2
resolves the contract at stage granularity. Status-quo path displaced: each stage producing
whatever its skills naturally output (R-02, Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation begins;
execution reads the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

Every namespace in the plan's skill set must appear in exactly one band row (MECE partition).

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria AND by the DERIVATION CHAIN
CONTRACT's zone-boundary handoffs. Skills that cannot contribute to a declared zone-boundary
handoff artifact type should be reconsidered.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Verify each zone's commitment criteria are satisfiable and that the DERIVATION CHAIN CONTRACT
zone-boundary artifact types are producible by the assigned skills.

---

#### Step 5a -- Design Gates (Owner: Architect)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.
Gates at zone-final stages must reference artifact types that satisfy the DERIVATION CHAIN
CONTRACT's corresponding zone-boundary "Must produce" row.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

Every `intent:` field must be a genuine interrogative ending `?`.

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why echo occupies row 0 -- counter-move against F-2.
**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** Consumes and
Produces values must satisfy both the stage-level consumer-pull constraint (ARTIFACT 0) and
the zone-boundary handoffs declared in the DERIVATION CHAIN CONTRACT. The YAML fragment column
is copied directly; no annotation is authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10. Also verify: does each zone-final stage's gate
artifact type satisfy the DERIVATION CHAIN CONTRACT's corresponding "Must produce" entry?

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

```
[ ] C-01 through C-48: same as V-01
[ ] C-49 (candidate): DERIVATION CHAIN CONTRACT table present; zone-to-zone artifact
         handoff declared before catalog opens at zone granularity (breadth-in,
         breadth-to-depth, depth-to-synthesis, synthesis-to-echo); ARTIFACT 2 declared
         to resolve the contract at stage granularity; contract positioned between zone
         commitment criteria and compound gate template; zone-final stage gates audited
         against contract "Must produce" entries
```

---

## V-05 -- Combined: Derivation Walkthrough + Failure Signal Gallery

**Axis**: Combined. Both the DERIVATION WALKTHROUGH (V-02) and the FAILURE SIGNAL GALLERY
(V-03) are present simultaneously. The walkthrough runs before CONSTRUCTION ORDER; the gallery
appears between the failure taxonomy and the RULE COVERAGE TABLE. The two elements create a
three-level inertia coverage stack: (1) failure taxonomy names abstract failure modes (F-level);
(2) gallery names observable output symptoms (AP-level); (3) walkthrough names the pre-
construction derivation reasoning procedure (DW-level).

**Hypothesis**: V-02 and V-03 each introduce one new structural element. Combining them tests
whether the two elements co-exist without structural interference and whether they together
yield two candidate new criteria rather than one. The tri-level stack (F → AP → DW) covers
inertia at the abstract, diagnostic, and procedural levels simultaneously -- no prior variation
has coverage at all three levels. Anticipated score: 41/41 aspirational. Candidate new
criteria: C-49 (gallery) and C-50 (walkthrough).

**C-47 form**: Same as V-01
**C-48 form**: Same as V-01
**New pattern 1 (C-49 candidate)**: FAILURE SIGNAL GALLERY (AP-01 through AP-06) -- same
             as V-03; positioned after failure taxonomy, before RULE COVERAGE TABLE
**New pattern 2 (C-50 candidate)**: DERIVATION WALKTHROUGH (DW-1 through DW-6) -- same
             as V-02; positioned after skill catalog, before CONSTRUCTION ORDER
**Combined pattern**: Both present simultaneously; terminal checklist references both;
             Step 8 ARTIFACT 2 declared to transcribe from DW-6 chain; AP gallery used
             as final diagnostic pass after Step 10

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

**FAILURE SIGNAL GALLERY**

The taxonomy above names failure modes at the abstract level. This gallery names their
observable symptoms -- what you see in a produced output when the failure has occurred.
Use this gallery as a diagnostic checklist before auditing the final YAML.

| AP-ID | Anti-Pattern Name | Symptom fingerprint (what you see in the output) | Failure signaled | Detection question |
|-------|-------------------|--------------------------------------------------|------------------|--------------------|
| AP-01 | Namespace-named stages | Stage `name:` values contain namespace tokens or skill cluster labels: `scout_phase`, `prove_block`, `listen_monitoring`, `review_and_trace_stage` | F-1: catalog-first | Does any `name:` field contain a namespace identifier or skill cluster label? |
| AP-02 | Prose-only gate | Gate values read as task-completion prose: `adequate signals present`, `work in this stage is complete`, `signals gathered and reviewed` -- no `::` separator, no `>= N` count floor | F-1: catalog-first | Does every non-echo gate contain both `::` and `>=`? |
| AP-03 | Forward-reference gate | Gate references an artifact type not producible by any skill listed in that stage's `skills:` array | F-1: catalog-first | For each artifact type named in each gate: is there at least one skill in that stage's `skills:` array that produces it? |
| AP-04 | Echo appended without anchor | Echo appears at the last row of ARTIFACT 2 (row N) without a declared derivation anchor in ARTIFACT 0; echo's row position described as "where execution ends" | F-2: arbitrary-convention | Is echo at row 0 in ARTIFACT 2? Is the "not an arbitrary convention" clause present in ARTIFACT 0? |
| AP-05 | Producer-push annotation | `# Produces:` value derived from "what this stage's skills naturally output"; adjacent-stage Produces/Consumes pairs do not match | F-1: catalog-first | For each adjacent stage pair: does stage N's `# Produces:` exactly match stage N+1's `# Consumes:`? |
| AP-06 | Uncommitted zone membership | Zone assignment inferred from namespace grouping after skills were selected; ARTIFACT 1 missing Zone commitment check column | F-1: catalog-first | Was the zone commitment criteria section written before Step 3? Does ARTIFACT 1 have a Zone commitment check column? |

This gallery extends the failure taxonomy to the symptom level. Each anti-pattern maps to
exactly one failure in the taxonomy above. The gallery does not introduce new failure modes;
it makes the existing failure modes detectable from output inspection alone.

The following table enumerates ALL protocol rules. This table is exhaustive: every construction
rule in this protocol appears as exactly one row. No rule is omitted. Each rule names the
status-quo path it displaces and the role accountable for the counter-move.

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

**Lifecycle zones with commitment criteria** (declared before the catalog opens -- Owner: PM / Architect):

**Breadth zone** commitment criteria (all three before advancing to depth):
1. Zone-exit question (Owner: PM): "Have we named the problem space, identified key constraints,
   and committed to a direction without relying on solution-space knowledge?"
2. Artifact-type floor (Owner: Architect): at least one competitor or market signal artifact,
   at least one feasibility artifact, at least one draft artifact (spec or proposal)
3. Required gate pattern class (Owner: Architect): at least one compound gate with `>= 2`
   count floor on a scout or draft skill artifact from a stage in this zone

**Depth zone** commitment criteria (all three before advancing to synthesis):
1. Zone-exit question (Owner: PM): "Has the design been tested against failure modes and
   adversarial conditions by reviewers who did not author the spec?"
2. Artifact-type floor (Owner: Architect): at least one review artifact, one flow or trace
   artifact, one prove artifact
3. Required gate pattern class (Owner: Architect): at least one compound gate referencing
   a review or prove skill with `>= 2` count floor from a stage in this zone

**Synthesis zone** commitment criteria (all three before echo advances):
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

## DERIVATION WALKTHROUGH -- Required Pre-Construction Procedure (Owner: Architect)

Run this walkthrough in writing before beginning Step 1. Do not enter the CONSTRUCTION ORDER
until you have recorded the full derivation chain at DW-6. The FAILURE SIGNAL GALLERY above
names what failures look like in the output; this walkthrough names the reasoning procedure
that prevents them at the source.

**DW-1 -- Anchor at echo (Owner: Architect):**
Echo is the terminal consumer. Name the three categories of information echo needs to confirm
the feature is live and being monitored. These are information needs, not skills:

```
echo information needs:
  - [first need]
  - [second need]
  - [third need]
```

**DW-2 -- Derive synthesis Produces (Owner: Architect):**
The final synthesis-zone stage must produce artifacts satisfying DW-1. Record:

```
synthesis-final-stage # Produces: [artifact types satisfying DW-1]
```

**DW-3 -- Derive depth-to-synthesis handoff (Owner: Architect):**
What must depth produce to enable synthesis to produce DW-2's output? Record:

```
depth-final-stage  # Produces: [...]   (= synthesis-first-stage # Consumes:)
```

**DW-4 -- Derive breadth-to-depth handoff (Owner: Architect):**
What must breadth produce to enable depth to produce DW-3's output? Record:

```
breadth-final-stage # Produces: [...]  (= depth-first-stage # Consumes:)
```

**DW-5 -- Verify breadth chain start (Owner: Architect):**
Breadth starts the chain from discovery -- no prior zone feeds it. Confirm:

```
breadth-first-stage # Consumes: none  (chain starts here)
```

**DW-6 -- Record the full derivation chain (Owner: Architect):**

```
echo
  <- [synthesis-final Produces] from DW-2
     <- [depth-final Produces] from DW-3
        <- [breadth-final Produces] from DW-4
           <- (none) -- chain starts at breadth
```

No Consumes/Produces entry in ARTIFACT 2 may contradict the DW-6 chain. ARTIFACT 2 matrix
cells transcribe from this chain. AP-05 symptom (mismatched adjacent Produces/Consumes) is
a transcription error against DW-6, not an authorship decision.

---

## CONSTRUCTION ORDER

Required construction sequence. Read all steps before beginning Step 1. The DERIVATION
WALKTHROUGH above must be complete before beginning Step 1.

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
10. Terminal validation checklist (Step 10) -- Owner: Team Lead

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic (Owner: PM)

State the topic name.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect -- AP-06 symptom:
zone assigned from namespace grouping). Declare 3--6 phase boundaries from first principles.

Phase names encode investigative purpose (AP-01 symptom check: no namespace tokens in names):
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
  # Consumes: [artifact type(s) required as input from the prior stage]
  # Produces: [artifact type(s) yielded as output for the next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. The derivation runs backward from echo; YAML annotations are transcribed from
the backward derivation, not authored from skill knowledge. At the reasoning level, the
derivation was recorded in the DERIVATION WALKTHROUGH (DW-6); ARTIFACT 2 transcribes from it.
AP-05 symptom (mismatched Produces/Consumes) signals producer-push authorship against DW-6.
Status-quo path displaced: each stage producing whatever its skills naturally output (R-02,
Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. AP-04 symptom: echo at row N without anchor declaration. Status-quo
path displaced: treating row-0 as a formatting choice because "execution ends at echo" (R-07,
Owner: Architect). Row 0 is where derivation begins; execution reads the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

AP-06 symptom check: Zone commitment check column must be present and non-empty.

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria. The zone handoffs in DW-3
and DW-4 govern which artifact types each zone must produce.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Verify each zone's commitment criteria are satisfiable.

---

#### Step 5a -- Design Gates (Owner: Architect)

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.
AP-02 symptom check: every gate must contain `::` and `>=`.
AP-03 symptom check: every gate artifact type must be producible by a skill in that stage.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fixes all AP-03 symptoms.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

Every `intent:` field must be a genuine interrogative ending `?`.

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why echo occupies row 0 -- counter-move against F-2
(AP-04 symptom check: echo at row 0, anchor declared in ARTIFACT 0).
**ARTIFACT 2 is the sole authoritative source.** All Consumes/Produces values transcribed
from DW-6 chain (AP-05 symptom check: adjacent pairs must match exactly). YAML fragment
column is copied directly.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [from DW-6] | [from DW-6] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [from DW-6] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

After completing the checklist below, run the FAILURE SIGNAL GALLERY as a final diagnostic
pass: for each AP-01 through AP-06, inspect the completed YAML output and answer the
detection question. Any detection question that answers YES (symptom present) triggers
revision.

```
[ ] C-01 through C-48: same as V-01
[ ] C-49 (candidate): FAILURE SIGNAL GALLERY present (AP-01 through AP-06) with observable
         symptom fingerprints and detection questions; positioned after failure taxonomy
         and before RULE COVERAGE TABLE; each AP maps to exactly one taxonomy failure;
         gallery used as final diagnostic pass after terminal validation checklist
[ ] C-50 (candidate): DERIVATION WALKTHROUGH present (DW-1 through DW-6) as named pre-
         construction procedure; DW-6 chain record present; ARTIFACT 2 Consumes/Produces
         declared to transcribe from DW-6 chain; walkthrough positioned before CONSTRUCTION
         ORDER; AP-05 symptom declared to signal transcription error against DW-6 chain
```
