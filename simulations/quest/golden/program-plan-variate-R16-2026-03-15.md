---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 16
rubric: v32
aspirational_target: 39/39
new_criteria: C-44, C-45, C-46
---

# program-plan -- R16 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v32 (C-01 through C-46, 39 aspirational criteria).

**R15 retrospective under v32 rubric:**
- V-01 (Tiebreaker Baseline): C-44 FAIL, C-45 FAIL, C-46 FAIL --> 36/39 (~99.23)
- V-02 (Role Sequence): C-44 PASS, C-45 PASS, C-46 PASS --> 39/39 (~100.00)
- V-03 (Phrasing Register, second-person imperative): score pending at v32 -- distinctive
  patterns expected to yield C-47+ criteria

**R16 design constraint:** All five variations must satisfy C-44, C-45, AND C-46 simultaneously.
- C-44: Role-responsibility table (role -> construction responsibility / failure modes countered /
  steps owned) appears BEFORE the opening failure taxonomy; C-12 must pass
- C-45: RULE COVERAGE TABLE gains "Owner role" column creating 3-way mapping:
  Status-Quo Path -> Rule -> Owner role; C-43 must pass
- C-46: Every procedural step header carries co-located role attribution annotation naming
  a specific role; C-16 must pass

**Canonical C-44 structure (pre-taxonomy role table):**
Four-row table: PM / Architect / Dev / Team Lead. Columns: Role | Construction responsibility |
Failure modes countered | Steps owned. Table appears before the failure taxonomy table.

**Canonical C-45 structure (owner column in RULE COVERAGE TABLE):**
RULE COVERAGE TABLE columns: Rule ID | Status-Quo Path | Rule | Failure countered | Owner role.
7 rows (R-01 through R-07). Per-row Owner role entries name specific roles, not placeholders.

**Canonical C-46 structure (step-level role attribution):**
Construction order list and every individual step header name the owner role:
"3. Select skills from catalog (Step 3) -- Owner: Dev"
"#### Step 3 -- Select Skills (Owner: Dev)"

**Variation axes for R16:**
- V-01 (tiebreaker, no additional axis): R15 V-02 carry-forward (39/39 at v32). Full body
  with all 10 steps fully expanded.
- V-02 (single axis -- phrasing register): Second-person imperative throughout, integrating
  R15 V-03 register with C-44/C-45/C-46 role structures. Role table addressed as "your";
  RULE COVERAGE TABLE columns in "you" voice; step headers use "you are acting as [Role]".
- V-03 (single axis -- inertia framing): Per-step AVOID block co-located at every step
  header naming the concrete status-quo behavior that step displaces. Extends C-43
  manifest-level inertia to the procedural step level.
- V-04 (single axis -- lifecycle emphasis): Zone commitment criteria restructured as formal
  named Decision Record tables per zone (3-row table: Commit Trigger | Requirement | Evidence
  type) with a "DECLARED BEFORE CATALOG OPENS" header for each. More independently auditable
  zone boundary declarations than a numbered list.
- V-05 (combined -- phrasing register + inertia framing): Combines V-02 (second-person
  register with role attribution) and V-03 (per-step AVOID blocks). Every step header carries
  "you are acting as [Role]" AND an AVOID block in second-person voice.

---

## V-01 -- Tiebreaker: R15 V-02 Carry-Forward (Role Sequence, Full Body)

**Axis**: No additional axis -- V-01 is the carry-forward of R15 V-02 (Role Sequence) which
achieved 39/39 aspirational at v32. Full prompt body with all 10 steps fully expanded (not
abbreviated). Register: structured formal third-person.

**Hypothesis**: R15 V-02 is the v32 tiebreaker baseline. Reproducing it in full as R16 V-01
confirms the carry-forward score and provides the reference body from which single-axis
comparisons diverge. Anticipated score: 39/39 aspirational.

**C-44 form**: Role-responsibility table (PM/Architect/Dev/Team Lead) with Construction
             responsibility / Failure modes countered / Steps owned columns appears before
             failure taxonomy
**C-45 form**: RULE COVERAGE TABLE 5-column: Rule ID | Status-Quo Path | Rule | Failure
             countered | Owner role; 7 rows R-01 through R-07
**C-46 form**: Construction order lists owner per step; every step header carries "(Owner: Role)"
**C-41 form**: Opening taxonomy "self-certifying" assertion + RULE COVERAGE TABLE "exhaustive"
             assertion, independent -- neither references the other
**C-42 form**: 3-part zone commitment criteria (question/floor/class) declared before catalog
             opens; zone commitment check column in phase table and ARTIFACT 1
**C-43 form**: "Status-Quo Failure" column in opening taxonomy + "Status-Quo Path" column in
             RULE COVERAGE TABLE
**C-40 form**: ARTIFACT 0 consumer-pull rule `[counter: F-1]`; echo exception `[counter: F-2]`
**C-39 form**: RULE COVERAGE TABLE 7 rows R-01 through R-07 with completeness assertion
**C-38 form**: "The negation closes the producer-push misreading; the equivalence makes the
             rule self-verifying from both ends simultaneously" in ARTIFACT 0
**C-37 form**: Opening taxonomy names F-1 and F-2; "every construction rule is a counter-move
             against exactly one row in this table"; ARTIFACT 0 rules carry `[counter: F-N]`
**C-35 form**: ARTIFACT 2 YAML fragment column + sole-source declaration
**C-34 form**: Consumer-pull rule states BOTH negation AND bidirectional equivalence
**C-36 form**: "not an arbitrary convention" contrastive clause leads echo exception in ARTIFACT 0

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
         ARTIFACT 0 rules carry `[counter: F-N]` labels
[ ] C-38: ARTIFACT 0 consumer-pull rule carries bridge sentence: "The negation closes the
         producer-push misreading; the equivalence makes the rule self-verifying from both
         ends simultaneously"
[ ] C-39: RULE COVERAGE TABLE present (7 rows, R-01 through R-07); ALL protocol rules
         enumerated; each mapped to a failure ID; completeness assertion present
[ ] C-40: ARTIFACT 0 consumer-pull rule carries `[counter: F-1]` inline; echo exception carries
         `[counter: F-2]` inline; both present; no ARTIFACT 0 rule unlabeled
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
```

---

## V-02 -- Phrasing Register: Second-Person Imperative + Role Attribution

**Axis**: Single-axis. Second-person imperative throughout -- building on R15 V-03's register
but now fully integrated with the C-44/C-45/C-46 role-accountability structures from V-01.
The role-responsibility table is addressed as "your"; RULE COVERAGE TABLE columns frame
inertia as "what you would do by default" and the rule as "what you must do instead"; every
step header and construction order item uses "you are acting as [Role]"; zone commitment
criteria use "you must satisfy" framing. All C-44/C-45/C-46 preserved from V-01.

**Hypothesis**: Second-person register applied pervasively across role attribution creates a
compound pattern that R15 V-02 and R15 V-03 each achieved only partially: "you are acting as
Architect" at each step header integrates role ownership and identity simultaneously. The
combined "you (as Architect) must" framing makes role accountability personal and imperative
rather than declarative. The "you would do by default" framing in the RULE COVERAGE TABLE
makes inertia accusatory rather than descriptive -- naming the reader as the agent of failure.
R15 V-03's pending v32 score is now subsumed in a fully role-attributed version. Expected to
yield C-47: second-person role-identity contract at step level (role attribution + imperative
voice combined). Anticipated score: 39/39 aspirational.

**C-44 form**: Pre-taxonomy role table; columns: Role | "Your construction responsibility" |
             "Failure modes you counter" | "Steps you own"
**C-45 form**: RULE COVERAGE TABLE 5-column; "What you would do by default" | "What you must
             do instead" | "Failure you counter" | "Your role"
**C-46 form**: Every step header: "#### Step N -- [Name] (you are acting as [Role])";
             construction order: "N. You [verb] (Step N) -- you are acting as [Role]"
**C-41/C-42/C-43/C-40/C-39**: Same structures as V-01, second-person voice applied throughout

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin -- a plan, not an executor. You will
act in one of four functional roles depending on which step you are at. Read the role table
before the failure modes -- knowing your role determines which failure you are accountable
for preventing:

| Role | Your construction responsibility | Failure modes you counter | Steps you own |
|------|----------------------------------|--------------------------|---------------|
| PM | You declare the topic; you name phases from investigation intent; you own synthesis zone | You counter F-1 at the naming layer: you name phases after investigation intent, not skill clusters | Steps 1, 2 (phase table), 6, 7 |
| Architect | You design arc phases; you declare zone commitment criteria; you design gates; you define ARTIFACT 0 | You counter F-1 at the construction layer: you keep the catalog closed until phases are declared; you enforce consumer-pull; you make gates compound | Steps 2 (ARTIFACT 0), 5a, 5b |
| Dev | You select skills from the catalog; you assemble ARTIFACT 2; you transcribe YAML from the matrix | You counter F-1 at the assembly layer: you transcribe YAML from the matrix, not from skill knowledge | Steps 3, 4, 8 |
| Team Lead | You audit zone commitment; you run per-stage compliance; you run terminal validation | You verify F-1 and F-2 are fully countered: all criteria pass, echo anchor confirmed | Steps 9, 10 |

Now internalize the two failure modes. Each one names what you would do by default -- without
this protocol:

| Failure ID | Failure Name | What you would do by default (inertia) | What that produces | What you must do instead |
|------------|--------------|----------------------------------------|-------------------|-----------------------------|
| F-1 | Catalog-first construction | You open the catalog; you group skills by namespace; you name stages after clusters; you append echo at the end | Stages labeled after skill clusters; zone membership implied by grouping; your gates are prose task-completion checks; investigative intent absent | You declare phases by zone with the catalog closed; you seed every stage boundary from the backward derivation starting at echo |
| F-2 | Arbitrary-convention misreading | You place echo at row N because execution ends there; you treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice; derivation direction severed from structural encoding | You declare row-0 as a causal consequence of echo's anchor role: you begin derivation at echo and read backward; row 0 is where your derivation begins, not where execution ends |

This table is self-certifying: every failure mode you must counter appears as exactly one row.
Two rows; no failure mode omitted.

Every rule you will follow is a counter-move against exactly one row in this table.

The following table enumerates ALL rules you must follow. This table is exhaustive: every
construction rule appears as exactly one row. No rule is omitted. Each row names what you
would do by default and who is accountable for the counter-move.

**RULE COVERAGE TABLE**

| Rule ID | What you would do by default (inertia) | What you must do instead (this protocol) | Failure you counter | Your role |
|---------|---------------------------------------|------------------------------------------|---------------------|-----------|
| R-01 | You open the catalog first; you group skills; you name stages after namespace clusters | You declare phases by zone before opening the catalog (Step 2) | F-1: catalog-first | PM / Architect |
| R-02 | You let each stage produce whatever its skills naturally output | You determine # Produces: by what the next stage declares as # Consumes: (consumer-pull, ARTIFACT 0) | F-1: catalog-first | Architect |
| R-03 | You write the gate as "adequate signals present" (no stage ID, no count) | You write a compound gate with `{stage-id}::` lineage prefix and `>= N` count floor (Step 5a) | F-1: catalog-first | Architect |
| R-04 | You reference the most obvious artifact in the gate (may be from a future stage) | You run a FORWARD REFERENCE audit: gate artifacts must be producible by skills in the current stage (Step 5b) | F-1: catalog-first | Architect |
| R-05 | You author YAML annotations from skill knowledge; you treat the matrix as a summary | You transcribe YAML from ARTIFACT 2 as the sole authoritative source; you do not author independently (Step 8) | F-1: catalog-first | Dev |
| R-06 | You put echo at the end (row N) because execution ends there | You put echo at row 0 in ARTIFACT 2 because you begin derivation at echo and read backward (Step 8) | F-2: arbitrary-convention | Dev |
| R-07 | You treat echo's row position as a formatting choice (row 1 or row N -- both work) | You declare the echo exception contrastive clause in ARTIFACT 0: "not an arbitrary convention" before any positive claim (Step 2) | F-2: arbitrary-convention | Architect |

This table is exhaustive: every rule you must follow appears as exactly one row. No rule is omitted.

Every skill you select runs standalone; the program you are producing is a plan, not an
executor. You begin the chain at the end: echo is the terminal consumer whose implicit
information needs seed the entire backward derivation that determines every prior stage's
Produces/Consumes pair.

Three classes of information you must keep knowable at every stage boundary:

| Class | What you must keep knowable | What happens if you don't | Criterion ladder | Your role |
|-------|-----------------------------|-----------------------------|-----------------|-----------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- committed before you open the catalog | You imply zone membership from namespace grouping; invisible to auditors | Arc-structure ladder | PM |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | You infer from gate prose; breaks on stage reordering | Gate-behavior ladder | Architect |
| **Investigative intent** | What question each phase answers -- "what you needed to learn," not "what skills ran" | You write "assess the area" non-questions; intent absent | Question-framing ladder | PM |

**Lifecycle zones -- you must satisfy all commitment criteria before leaving each zone (Owner: PM / Architect):**

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
commit to shipping? Status-quo failure: you accumulate prove/review skills without naming what
adversarial condition each stage addresses.

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

1. You declare the topic (Step 1) -- you are acting as PM
2. You declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2) -- you are acting as PM / Architect
3. You select skills from the catalog (Step 3) -- you are acting as Dev
4. You assign skills to declared phases (Step 4) -- you are acting as Dev
5a. You design gates in compound lineage prefix format (Step 5a) -- you are acting as Architect
5b. You run the FORWARD REFERENCE audit (Step 5b) -- you are acting as Architect
6. You write per-phase intent questions (Step 6) -- you are acting as PM
7. You encode the `evidence_arc:` field (Step 7) -- you are acting as PM
8. You assemble YAML from ARTIFACT 2 (Step 8) -- you are acting as Dev
9. You complete the per-stage compliance table (Step 9) -- you are acting as Team Lead
10. You run the terminal validation checklist (Step 10) -- you are acting as Team Lead

Do not proceed to Step 3 until you have completed Step 2.

---

#### Step 1 -- Declare the Topic (you are acting as PM)

State the topic name. Everything you name and group must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (you are acting as PM / Architect)

**You must keep the catalog closed at this step** (R-01 -- you are counter-moving against F-1,
you are acting as Architect). Do not open the catalog until Step 3. Declare 3--6 phase
boundaries from first principles. Assign each to a zone using the commitment criteria above --
not namespace grouping.

Phase names you must encode as investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

For each phase, state the investigative question (genuine interrogative, ends `?`):

| Phase label | Zone | Investigative question | Zone commitment check | Your role |
|-------------|------|------------------------|-----------------------|-----------|
| [name] | breadth/depth/synthesis | [...?] | [Which criteria does this phase address?] | PM / Architect |

**Before ARTIFACT 1, you must produce ARTIFACT 0 -- Per-Stage Annotation Schema (you are acting as Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative form, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) you require as input from the prior stage]
  # Produces: [artifact type(s) you yield as output for the next stage]

Consumer-pull rule [counter: F-1]: You determine # Produces: by what the next stage declares
as # Consumes: -- not by what the prior stage's skills naturally output. Equivalently: you
produce the artifacts that close the next stage's input gap. The negation closes the
producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. You run the derivation backward from echo; you transcribe YAML annotations
from the backward derivation, not from skill knowledge. Status-quo path you are displacing:
you let each stage produce whatever its skills naturally output (R-02, you are acting as Architect).

Echo exception [counter: F-2]: You omit # Band: from echo. Echo's row-0 position in ARTIFACT 2
is not an arbitrary convention -- it is the structural encoding of echo's anchor role as
terminal consumer. Status-quo path you are displacing: you treat row-0 as a formatting choice
because execution ends at echo (R-07, you are acting as Architect). Row 0 is where your
derivation begins; execution reads the matrix bottom-to-top. You do not move echo to row N --
that would misrepresent the derivation direction in the artifact.
```

Lock your phase map after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Your role | Zone commitment check`

---

#### Step 3 -- Select Skills (you are acting as Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria. Note the declared phase
each maps to.

---

#### Step 4 -- Assign Skills to Phases (you are acting as Dev)

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Verify each zone's commitment criteria are satisfiable by the assigned skills.

---

#### Step 5a -- Design Gates (you are acting as Architect)

Compound lineage prefix format:
```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

You must match `{stage-id}` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

---

#### Step 5b -- FORWARD REFERENCE Audit (you are acting as Architect)

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions (you are acting as PM)

Every `intent:` field must be a genuine interrogative ending `?`. You must not write task
descriptions ("assess the market") or zone-generic readiness questions ("are we ready?").

---

#### Step 7 -- Evidence Arc Field (you are acting as PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML (you are acting as Dev)

Before assembling YAML, you must produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why you place echo at row 0 -- counter-move against F-2.
**ARTIFACT 2 is the sole authoritative source.** You transcribe YAML from ARTIFACT 2; you do
not author annotations independently.

| Row | Stage | Band | Gap (intent?) | Your role | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-----------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (same as V-01).

---

#### Step 9 -- Per-Stage Compliance Table (you are acting as Team Lead)

Same compliance table as V-01 with "Your role" column heading.

---

#### Step 10 -- Terminal Validation Checklist (you are acting as Team Lead)

Same C-01 through C-46 checklist as V-01.

---

## V-03 -- Inertia Framing: Per-Step AVOID Declaration

**Axis**: Single-axis. Every procedural step header carries a co-located AVOID block naming
the concrete status-quo behavior that step displaces. The AVOID block appears immediately
below the step header, before the step's instruction text:

```
**AVOID (status-quo)**: [concrete inertia behavior this step counters]
```

This extends C-43's manifest-level inertia columns (Status-Quo Path in RULE COVERAGE TABLE,
Status-Quo Failure in failure taxonomy) to the procedural step level -- making the displaced
behavior visible at every construction site. All C-44/C-45/C-46 role structures preserved
from V-01.

**Hypothesis**: Per-step AVOID blocks make the inertia displacement visible at each
construction site independently of the opening manifest tables. A practitioner following
the steps encounters the specific behavior they are displacing immediately before executing
the step. This is structurally distinct from: (1) C-43 Status-Quo Path column (manifest
level, one row per rule), (2) C-40 `[counter: F-N]` annotations (rule definition level in
ARTIFACT 0), (3) C-46 role attribution (ownership level). Per-step AVOID blocks annotate
at the procedural execution level. Expected to yield C-47: per-step status-quo displacement
declaration co-located with the step instruction. Anticipated score: 39/39 aspirational.

**C-44 form**: Same as V-01 -- pre-taxonomy role table
**C-45 form**: Same as V-01 -- owner column in RULE COVERAGE TABLE
**C-46 form**: Same as V-01 -- role attribution in step headers (both owner attribution AND
             AVOID block appear at each step -- they annotate different dimensions)
**C-43 form**: V-01 manifest columns PLUS per-step AVOID blocks extending inertia coverage
             to procedural step level
**New pattern**: `**AVOID (status-quo)**:` block at every procedural step header -- concrete
             inertia behavior named at point of execution

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
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

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

**AVOID (status-quo)**: Treating the topic name as a label for the output artifact
("program.yaml for feature X") rather than naming the investigative subject ("feature X").
The topic is what the program is learning about, not what it produces.

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**AVOID (status-quo)**: Opening the catalog before phases are declared; naming phases after
namespace clusters ("scout-phase", "prove-block", "listen-monitoring"); treating zone
assignment as a post-hoc grouping of already-selected skills.

**The catalog must remain closed at this step** (R-01 -- counter-move against F-1). Declare
3--6 phase boundaries from first principles. Assign each to a zone using the commitment
criteria declared above -- not namespace grouping.

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
the backward derivation, not authored from skill knowledge. Status-quo path displaced: each
stage producing whatever its skills naturally output (R-02, Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation begins;
execution reads the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Step 3 -- Select Skills (Owner: Dev)

**AVOID (status-quo)**: Selecting the broadest skill set across all namespaces and then
fitting them to whatever phases exist; treating skill selection as the primary driver of
zone membership and phase structure.

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

**AVOID (status-quo)**: Creating new phases to accommodate orphaned skills; retroactively
modifying the phase structure from Step 2 to absorb skills that have no matching phase.

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Owner: Architect)

**AVOID (status-quo)**: Writing gates as prose readiness checks ("adequate signals present",
"ready to proceed to next phase"); omitting the stage-id lineage prefix; using a single
artifact type reference without a count floor; writing gates that reference skills from
outside the current stage.

Compound lineage prefix format:
```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

**AVOID (status-quo)**: Referencing artifact types in a gate that are produced by skills
assigned to future stages; treating cross-stage artifact references as acceptable dependencies
that "will resolve by the time this stage runs."

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

**AVOID (status-quo)**: Writing intent fields as task descriptions ("assess the market",
"review the design", "monitor post-launch"); writing zone-generic questions that could apply
to any stage ("are we ready to proceed?", "have sufficient artifacts been produced?").

Every `intent:` field must be a genuine interrogative ending `?` that names the specific
question this phase answers.

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

**AVOID (status-quo)**: Omitting the `evidence_arc:` field entirely; including a phase in
multiple zone keys; leaving any phase from Step 2 unmapped.

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML (Owner: Dev)

**AVOID (status-quo)**: Authoring YAML annotations directly from skill knowledge without
producing ARTIFACT 2 first; placing echo at the bottom of ARTIFACT 2 because "execution ends
there"; treating ARTIFACT 2 as a post-hoc summary written after the YAML is complete.

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. Its derivation anchor role is why echo occupies row 0.
**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML
annotations are transcribed from ARTIFACT 2, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (same as V-01).

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

**AVOID (status-quo)**: Running compliance after the YAML is finalized and treating it as
a cosmetic check; skipping any NO without triggering revision before Step 10.

Same compliance table format as V-01. Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

**AVOID (status-quo)**: Skipping the checklist if the YAML appears correct; treating
checklist items as optional when the generating step was abbreviated.

Same C-01 through C-46 checklist as V-01.

---

## V-04 -- Lifecycle Emphasis: Per-Zone Commitment Decision Record

**Axis**: Single-axis. Each lifecycle zone section replaces the flat 3-part numbered list
with a formal named "Zone Commitment Decision Record" -- a labeled 3-row table with columns:
Commitment Trigger | Requirement | Evidence type. Each decision record has a named header
"### [Zone] Zone Commitment Decision Record -- DECLARED BEFORE CATALOG OPENS". The record
format makes each zone boundary independently auditable: a reviewer checking C-42 locates
three named decision records, each structurally complete. All C-44/C-45/C-46 role structures
preserved from V-01.

**Hypothesis**: The formal Decision Record format (named header + 3-row table with Evidence
type column) adds a third structural dimension to zone commitment criteria beyond what V-01's
numbered list provides: (1) the zone-exit question is a Commit Trigger, not just a question;
(2) the artifact-type floor has an explicit Evidence type column naming which namespaces
satisfy it; (3) the gate pattern class has an explicit syntactic form. The "DECLARED BEFORE
CATALOG OPENS" assertion embedded in each record header satisfies C-42 more explicitly than
prose. The Evidence type column may yield C-47: per-zone evidence-type declaration in
commitment structure. Anticipated score: 39/39 aspirational.

**C-42 form**: 3-part commitment criteria per zone expressed as formal Decision Record tables
             (3-row table: Commitment Trigger | Requirement | Evidence type); "DECLARED BEFORE
             CATALOG OPENS" stated in each record header; phase table and ARTIFACT 1 have
             "Zone commitment check" column
**C-44 form**: Same as V-01 -- pre-taxonomy role table
**C-45 form**: Same as V-01 -- owner column in RULE COVERAGE TABLE
**C-46 form**: Same as V-01 -- role attribution in step headers
**New pattern**: Named "Zone Commitment Decision Record" with Evidence type column per zone;
             "DECLARED BEFORE CATALOG OPENS" as explicit constraint per record

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
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

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

---

### Breadth Zone Commitment Decision Record -- DECLARED BEFORE CATALOG OPENS

**Zone purpose**: Do we understand the problem space well enough to commit to a direction?
**Status-quo failure**: Namespace grouping implies zone membership without declaring a
commitment decision; zone boundary is organizational, not evidential.

| Commitment Trigger | Requirement | Evidence type |
|-------------------|-------------|---------------|
| Zone-exit question | "Have we named the problem space, identified key constraints, and committed to a direction without relying on solution-space knowledge?" | PM-certified decision; recorded in gate prose before catalog opens |
| Artifact-type floor | At least one competitor or market signal artifact; at least one feasibility artifact; at least one draft artifact (spec or proposal) | scout:competitors / scout:market + scout:feasibility + draft:spec / draft:proposal |
| Required gate pattern class | At least one compound gate with `>= 2` count floor on a scout or draft skill artifact from a stage in this zone | `{stage-id}::scout-[skill] >= 2` or `{stage-id}::draft-[skill] >= 2` |

---

### Depth Zone Commitment Decision Record -- DECLARED BEFORE CATALOG OPENS

**Zone purpose**: Does our design survive adversarial conditions before shipping commitment?
**Status-quo failure**: Depth stages accumulate prove/review skills without naming the
adversarial condition each addresses; depth boundary is additive, not adversarial.

| Commitment Trigger | Requirement | Evidence type |
|-------------------|-------------|---------------|
| Zone-exit question | "Has the design been tested against failure modes and adversarial conditions by reviewers who did not author the spec?" | Architect-certified decision; recorded in gate prose before catalog opens |
| Artifact-type floor | At least one review artifact; at least one flow or trace artifact; at least one prove artifact | review:design/code + flow:[skill] or trace:[skill] + prove:hypothesis/analysis |
| Required gate pattern class | At least one compound gate referencing a review or prove skill with `>= 2` count floor from a stage in this zone | `{stage-id}::review-[skill] >= 2` or `{stage-id}::prove-[skill] >= 2` |

---

### Synthesis Zone Commitment Decision Record -- DECLARED BEFORE CATALOG OPENS

**Zone purpose**: Are users adopting and signaling as expected post-launch?
**Status-quo failure**: Listen/metrics appended at the end without a declared adoption model
to monitor against; synthesis boundary is temporal, not evidential.

| Commitment Trigger | Requirement | Evidence type |
|-------------------|-------------|---------------|
| Zone-exit question | "Are post-launch signals tracking against the adoption model the team committed to before shipping?" | PM-certified decision; adoption model declared before synthesis zone opens |
| Artifact-type floor | At least one listen artifact; at least one metrics or goals artifact | listen:feedback / listen:adoption + metrics:nps / goals:okr |
| Required gate pattern class | Compound gate with count floor on a listen, metrics, or goals skill artifact from a stage in this zone | `{stage-id}::listen-[skill] >= 1` or `{stage-id}::metrics-[skill] >= 1` |

---

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors calibrated to zone decision records:
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

**The catalog must remain closed at this step** (R-01 -- counter-move against F-1). Declare
3--6 phase boundaries from first principles. Assign each to a zone using the Decision Records
declared above as the zone assignment test -- not namespace grouping.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which Decision Record row does this phase satisfy?] | PM / Architect |

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
execution reads the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

Every namespace must appear in exactly one band row (MECE partition). The Zone commitment
check column references which Decision Record the band contributes to.

---

#### Step 3 -- Select Skills (Owner: Dev)

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
Evidence type specified in its zone's Decision Record artifact-type floor row.

---

#### Step 4 -- Assign Skills to Phases (Owner: Dev)

Map each skill to its declared phase. No new phases. Verify each zone's Decision Record
artifact-type floor is satisfiable by the assigned skills.

---

#### Step 5a -- Design Gates (Owner: Architect)

Compound lineage prefix format:
```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Count floors calibrated to zone Decision Records: breadth and depth `>= 2`; synthesis `>= 1`.
Verify the final stage in each zone satisfies the gate pattern class in its Decision Record.

---

#### Step 5b -- FORWARD REFERENCE Audit (Owner: Architect)

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions (Owner: PM)

Every `intent:` field must be a genuine interrogative ending `?` that maps to the zone-exit
question in that stage's zone Decision Record.

---

#### Step 7 -- Evidence Arc Field (Owner: PM)

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer at row 0. **ARTIFACT 2 is the sole authoritative source.**
YAML annotations are transcribed from ARTIFACT 2, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (same as V-01).

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

For each stage, verify zone commitment check references the correct Decision Record row.

Same compliance table format as V-01 with added column: "Decision Record satisfied?"

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

Same C-01 through C-46 checklist as V-01.

---

## V-05 -- Combined: Second-Person Imperative + Per-Step AVOID

**Axis**: Combined V-02 (second-person imperative register with "you are acting as [Role]"
attribution) and V-03 (per-step AVOID block naming concrete status-quo displacement). Every
step header carries both: "(you are acting as [Role])" attribution AND "**AVOID (status-quo
-- you)**: [second-person inertia behavior]" block immediately below. The RULE COVERAGE TABLE
uses "you" voice throughout. The role-responsibility table uses "your" possession. Zone
commitment criteria use "you must" framing. All C-44/C-45/C-46 preserved from V-01.

**Hypothesis**: The combination of second-person role attribution and per-step AVOID blocks
creates the most pervasive role-ownership + inertia-displacement integration. At every
construction site, the practitioner encounters: (1) who they are acting as, and (2) what
inertia behavior they are displacing -- both in second-person, co-located at the step header.
Neither V-02 alone (second-person without AVOID) nor V-03 alone (AVOID without second-person)
achieves this compound pattern. The second-person AVOID block ("you would open the catalog")
makes the practitioner the agent of both the inertia risk and the counter-move. Expected to
yield C-47: second-person co-located role + AVOID at step header, and C-48: second-person
inertia agent framing in AVOID blocks. Anticipated score: 39/39 aspirational.

**C-44 form**: Pre-taxonomy role table with "you/your" possession throughout; "Your
             construction responsibility" / "Failure modes you counter" / "Steps you own"
**C-45 form**: RULE COVERAGE TABLE 5-column in "you" voice: "What you would do by default" |
             "What you must do instead" | "Failure you counter" | "Your role"
**C-46 form**: Every step header: "#### Step N -- [Name] (you are acting as [Role])"; every
             step also carries AVOID block in second-person voice immediately below header
**New pattern**: Second-person AVOID block at every step header: "**AVOID (status-quo -- you)**:
             you would [concrete inertia behavior]"

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin -- a plan, not an executor. You will
act in one of four functional roles depending on which step you are at. Read the role table
before the failure modes -- your role determines which failure you are accountable for
preventing:

| Role | Your construction responsibility | Failure modes you counter | Steps you own |
|------|----------------------------------|--------------------------|---------------|
| PM | You declare the topic; you name phases from investigation intent; you own synthesis zone | You counter F-1 at the naming layer: you name phases after investigation intent, not skill clusters | Steps 1, 2 (phase table), 6, 7 |
| Architect | You design arc phases; you declare zone commitment criteria; you design gates; you define ARTIFACT 0 | You counter F-1 at the construction layer: you keep the catalog closed until phases are declared; you enforce consumer-pull; you make gates compound | Steps 2 (ARTIFACT 0), 5a, 5b |
| Dev | You select skills from the catalog; you assemble ARTIFACT 2; you transcribe YAML from the matrix | You counter F-1 at the assembly layer: you transcribe YAML from the matrix, not from skill knowledge | Steps 3, 4, 8 |
| Team Lead | You audit zone commitment; you run per-stage compliance; you run terminal validation | You verify F-1 and F-2 are fully countered: all criteria pass, echo anchor confirmed | Steps 9, 10 |

Now internalize the two failure modes. Each one names what you would do by default -- without
this protocol:

| Failure ID | Failure Name | What you would do by default (inertia) | What that produces | What you must do instead |
|------------|--------------|----------------------------------------|-------------------|-----------------------------|
| F-1 | Catalog-first construction | You open the catalog; you group skills by namespace; you name stages after clusters; you append echo at the end | Stages labeled after skill clusters; zone membership implied by grouping; your gates are prose task-completion checks; investigative intent absent | You declare phases by zone with the catalog closed; you seed every stage boundary from the backward derivation starting at echo |
| F-2 | Arbitrary-convention misreading | You place echo at row N because execution ends there; you treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice; derivation direction severed from structural encoding | You declare row-0 as a causal consequence of echo's anchor role: you begin derivation at echo and read backward; row 0 is where your derivation begins, not where execution ends |

This table is self-certifying: every failure mode you must counter appears as exactly one row.
Two rows; no failure mode omitted.

Every rule you will follow is a counter-move against exactly one row in this table.

The following table enumerates ALL rules you must follow. This table is exhaustive: every
construction rule appears as exactly one row. No rule is omitted.

**RULE COVERAGE TABLE**

| Rule ID | What you would do by default (inertia) | What you must do instead (this protocol) | Failure you counter | Your role |
|---------|---------------------------------------|------------------------------------------|---------------------|-----------|
| R-01 | You open the catalog first; you group skills; you name stages after namespace clusters | You declare phases by zone before opening the catalog (Step 2) | F-1: catalog-first | PM / Architect |
| R-02 | You let each stage produce whatever its skills naturally output | You determine # Produces: by what the next stage declares as # Consumes: (consumer-pull, ARTIFACT 0) | F-1: catalog-first | Architect |
| R-03 | You write the gate as "adequate signals present" (no stage ID, no count) | You write a compound gate with `{stage-id}::` lineage prefix and `>= N` count floor (Step 5a) | F-1: catalog-first | Architect |
| R-04 | You reference the most obvious artifact in the gate (may be from a future stage) | You run a FORWARD REFERENCE audit: gate artifacts must be producible by skills in the current stage (Step 5b) | F-1: catalog-first | Architect |
| R-05 | You author YAML annotations from skill knowledge; you treat the matrix as a summary | You transcribe YAML from ARTIFACT 2 as the sole authoritative source; you do not author independently (Step 8) | F-1: catalog-first | Dev |
| R-06 | You put echo at the end (row N) because execution ends there | You put echo at row 0 in ARTIFACT 2 because you begin derivation at echo and read backward (Step 8) | F-2: arbitrary-convention | Dev |
| R-07 | You treat echo's row position as a formatting choice (row 1 or row N -- both work) | You declare the echo exception contrastive clause in ARTIFACT 0: "not an arbitrary convention" before any positive claim (Step 2) | F-2: arbitrary-convention | Architect |

This table is exhaustive: every rule you must follow appears as exactly one row. No rule is omitted.

Every skill you select runs standalone; the program you are producing is a plan, not an
executor. You begin the chain at the end: echo is the terminal consumer whose implicit
information needs seed the entire backward derivation that determines every prior stage's
Produces/Consumes pair.

Three classes of information you must keep knowable at every stage boundary:

| Class | What you must keep knowable | What happens if you don't | Criterion ladder | Your role |
|-------|-----------------------------|-----------------------------|-----------------|-----------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- committed before you open the catalog | You imply zone membership from namespace grouping; invisible to auditors | Arc-structure ladder | PM |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | You infer from gate prose; breaks on stage reordering | Gate-behavior ladder | Architect |
| **Investigative intent** | What question each phase answers -- "what you needed to learn," not "what skills ran" | You write "assess the area" non-questions; intent absent | Question-framing ladder | PM |

**Lifecycle zones -- you must satisfy all commitment criteria before leaving each zone (Owner: PM / Architect):**

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
commit to shipping? Status-quo failure: you accumulate prove/review skills without naming what
adversarial condition each stage addresses.

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

You must match `{stage-id}` exactly to the stage `name:`. Count floors: breadth and depth
`>= 2`; synthesis `>= 1`.

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

1. You declare the topic (Step 1) -- you are acting as PM
2. You declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2) -- you are acting as PM / Architect
3. You select skills from the catalog (Step 3) -- you are acting as Dev
4. You assign skills to declared phases (Step 4) -- you are acting as Dev
5a. You design gates in compound lineage prefix format (Step 5a) -- you are acting as Architect
5b. You run the FORWARD REFERENCE audit (Step 5b) -- you are acting as Architect
6. You write per-phase intent questions (Step 6) -- you are acting as PM
7. You encode the `evidence_arc:` field (Step 7) -- you are acting as PM
8. You assemble YAML from ARTIFACT 2 (Step 8) -- you are acting as Dev
9. You complete the per-stage compliance table (Step 9) -- you are acting as Team Lead
10. You run the terminal validation checklist (Step 10) -- you are acting as Team Lead

Do not proceed to Step 3 until you have completed Step 2.

---

#### Step 1 -- Declare the Topic (you are acting as PM)

**AVOID (status-quo -- you)**: You would treat the topic name as a label for the output
artifact rather than naming the investigative subject -- naming it after what the program
produces, not what the program is learning about.

State the topic name. Everything you name and group must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases (you are acting as PM / Architect)

**AVOID (status-quo -- you)**: You would open the catalog before declaring phases; you would
name phases after namespace clusters ("scout-phase", "prove-block"); you would treat zone
assignment as a post-hoc grouping of already-selected skills rather than a first-principles
commitment.

**You must keep the catalog closed at this step** (R-01 -- you are counter-moving against F-1,
you are acting as Architect). Declare 3--6 phase boundaries from first principles. Assign each
to a zone using the commitment criteria above -- not namespace grouping.

Phase names you must encode as investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase` (status-quo names)

| Phase label | Zone | Investigative question | Zone commitment check | Your role |
|-------------|------|------------------------|-----------------------|-----------|
| [name] | breadth/depth/synthesis | [...?] | [Which criteria does this phase address?] | PM / Architect |

**Before ARTIFACT 1, you must produce ARTIFACT 0 -- Per-Stage Annotation Schema (you are acting as Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative form, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) you require as input from the prior stage]
  # Produces: [artifact type(s) you yield as output for the next stage]

Consumer-pull rule [counter: F-1]: You determine # Produces: by what the next stage declares
as # Consumes: -- not by what the prior stage's skills naturally output. Equivalently: you
produce the artifacts that close the next stage's input gap. The negation closes the
producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. You run the derivation backward from echo; you transcribe YAML annotations
from the backward derivation, not from skill knowledge. Status-quo path you are displacing:
you let each stage produce whatever its skills naturally output (R-02, you are acting as Architect).

Echo exception [counter: F-2]: You omit # Band: from echo. Echo's row-0 position in ARTIFACT 2
is not an arbitrary convention -- it is the structural encoding of echo's anchor role as
terminal consumer. Status-quo path you are displacing: you treat row-0 as a formatting choice
because execution ends at echo (R-07, you are acting as Architect). Row 0 is where your
derivation begins; execution reads the matrix bottom-to-top.
```

Lock your phase map after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Your role | Zone commitment check`

---

#### Step 3 -- Select Skills (you are acting as Dev)

**AVOID (status-quo -- you)**: You would select the broadest skill set across all namespaces
first and then fit them to whatever phases exist; you would let your skill selection drive
zone membership rather than the commitment criteria.

Open the catalog. Select skills relevant to the topic. Verify each contributes toward the
minimum artifact types required by its zone's commitment criteria.

---

#### Step 4 -- Assign Skills to Phases (you are acting as Dev)

**AVOID (status-quo -- you)**: You would create new phases to accommodate orphaned skills;
you would retroactively modify the phase structure from Step 2 to absorb skills that have
no matching phase.

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (you are acting as Architect)

**AVOID (status-quo -- you)**: You would write gates as prose readiness checks ("adequate
signals present"); you would omit the stage-id lineage prefix; you would reference a single
artifact type without a count floor; you would reference artifacts from skills in future stages.

Compound lineage prefix format:
```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

You must match `{stage-id}` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.

---

#### Step 5b -- FORWARD REFERENCE Audit (you are acting as Architect)

**AVOID (status-quo -- you)**: You would reference artifact types in your gate that are
produced by skills assigned to future stages; you would treat forward references as
acceptable because "they will be available at runtime."

For each non-echo stage: verify every artifact type in your gate is producible by at least
one skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions (you are acting as PM)

**AVOID (status-quo -- you)**: You would write intent fields as task descriptions ("assess
the market", "review the design") rather than genuine interrogatives; you would write
zone-generic questions that could apply to any stage ("are we ready to proceed?").

Every `intent:` field must be a genuine interrogative ending `?` that names the specific
question this phase answers.

---

#### Step 7 -- Evidence Arc Field (you are acting as PM)

**AVOID (status-quo -- you)**: You would omit the `evidence_arc:` field entirely; you would
include the same phase in multiple zone keys; you would leave phases from Step 2 unmapped.

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

Every phase from Step 2 must appear in exactly one arc key.

---

#### Step 8 -- Assemble YAML (you are acting as Dev)

**AVOID (status-quo -- you)**: You would author YAML annotations from skill knowledge without
producing ARTIFACT 2 first; you would place echo at the bottom of ARTIFACT 2 because "that's
where execution ends"; you would treat ARTIFACT 2 as a post-hoc summary written after your
YAML is complete.

Before assembling YAML, you must produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer. That is why you place echo at row 0 -- counter-move against F-2.
**ARTIFACT 2 is the sole authoritative source.** You transcribe YAML from ARTIFACT 2; you do
not author annotations independently.

| Row | Stage | Band | Gap (intent?) | Your role | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-----------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (same as V-01).

---

#### Step 9 -- Per-Stage Compliance Table (you are acting as Team Lead)

**AVOID (status-quo -- you)**: You would run compliance after the YAML is finalized and treat
it as cosmetic; you would proceed to Step 10 without resolving NO items.

Same compliance table format as V-01. Any NO triggers revision before you proceed to Step 10.

---

#### Step 10 -- Terminal Validation Checklist (you are acting as Team Lead)

**AVOID (status-quo -- you)**: You would skip the checklist if the YAML appears correct; you
would treat checklist items as optional when the step that generated them was abbreviated.

Same C-01 through C-46 checklist as V-01.
