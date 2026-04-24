---
skill: quest-variate
skill_target: program-plan
date: 2026-03-15
round: 18
rubric: v34
aspirational_target: 44/44
new_criteria_candidates: C-52
---

# program-plan -- R18 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-15. Rubric: v34 (C-01 through C-51, 44 aspirational criteria).

**R17 retrospective under v34 rubric:**
- V-01 (tiebreaker carry-forward): C-49 FAIL, C-50 FAIL, C-51 FAIL --> 41/44 (~99.32)
- V-02 (Backward Derivation Walkthrough): C-49 PASS, C-50 FAIL, C-51 FAIL --> 42/44 (~99.55)
- V-03 (Failure Signal Gallery): C-49 FAIL, C-50 PASS, C-51 FAIL --> 42/44 (~99.55)
- V-04 (Derivation Chain Contract): C-49 FAIL, C-50 FAIL, C-51 PASS --> 42/44 (~99.55)
- V-05 (Combined DW + Gallery): C-49 PASS, C-50 PASS, C-51 FAIL --> 43/44 (~99.77)

**R18 design constraint:** All five variations must satisfy C-01 through C-48 simultaneously.
R17 V-05 is the tiebreak leader at 43/44. The remaining gap is C-51 (zone-level derivation
chain contract). R18 ceiling: a variation combining all three (C-49 + C-50 + C-51) = 44/44.

**Variation axes for R18:**
- V-01 (tiebreaker): R17 V-05 carry-forward (C-49 + C-50, 43/44 at v34). Updated checklist
  to reference C-49 and C-50 by their official v34 IDs.
- V-02 (single axis -- C-51 only): DERIVATION CHAIN CONTRACT added to R17 V-01 baseline
  (no DW, no gallery). Zone-granularity pre-catalog handoff table with ARTIFACT 2 resolution.
  Expected: C-49 FAIL, C-50 FAIL, C-51 PASS = 42/44.
- V-03 (single axis -- C-50 + C-51): FAILURE SIGNAL GALLERY + DERIVATION CHAIN CONTRACT;
  no DW procedure. Expected: C-49 FAIL, C-50 PASS, C-51 PASS = 43/44.
- V-04 (single axis -- C-49 + C-51): DERIVATION WALKTHROUGH + DERIVATION CHAIN CONTRACT;
  no gallery. DW and zone contract linked: DW-1 anchors at echo, zone contract governs the
  zone-granularity handoffs that DW traces at stage granularity. Expected: C-49 PASS,
  C-50 FAIL, C-51 PASS = 43/44.
- V-05 (combined -- all three): C-49 + C-50 + C-51 present simultaneously. Three-tier
  derivation architecture declared explicitly: zone contract (zone level) governs DW
  (stage-level backward reasoning procedure), which governs ARTIFACT 2 (stage-level
  transcription matrix). Gallery extended with AP-07 (C-51 violation symptom). Potential
  new criterion: C-52 (three-tier derivation architecture declaration).
  Expected: C-49 PASS, C-50 PASS, C-51 PASS = 44/44 + C-52 candidate.

---

## V-01 -- Tiebreaker: R17 V-05 Carry-Forward (DW + Gallery, C-49 + C-50)

**Axis**: No additional axis. V-01 is the carry-forward of R17 V-05 (Combined Derivation
Walkthrough + Failure Signal Gallery) which achieved 43/44 at v34. Full prompt body with
all elements fully expanded. Register: structured formal third-person.

**Hypothesis**: R17 V-05 is the v34 tiebreaker baseline at 43/44. Reproducing it in full
as R18 V-01 confirms the carry-forward score and provides the reference body from which
single-axis comparisons diverge. Missing: C-51 (zone-level derivation chain contract).
Anticipated score: 43/44 aspirational.

**C-49 form**: DERIVATION WALKTHROUGH (DW-1 through DW-6) positioned after skill catalog,
             before CONSTRUCTION ORDER; DW-6 chain record; ARTIFACT 2 declared to transcribe
             from DW-6; status-quo failure of omitting walkthrough named
**C-50 form**: FAILURE SIGNAL GALLERY (AP-01 through AP-06) positioned after failure taxonomy
             and before RULE COVERAGE TABLE; each row: symptom fingerprint + failure signaled
             + detection question; gallery declared as extending taxonomy to symptom level
**C-51 form**: ABSENT (no zone-level derivation chain contract)

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
that prevents them at the source. Status-quo failure this procedure displaces: proceeding
directly to topic declaration without first establishing what the program must deliver to echo.
Without DW-6's chain record, Consumes/Produces entries in ARTIFACT 2 become authorship
decisions rather than transcription.

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

State the topic name. All artifact names and phase groupings must be coherent with this topic.

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

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

After completing the checklist below, run the FAILURE SIGNAL GALLERY as a final diagnostic
pass: for each AP-01 through AP-06, inspect the completed YAML output and answer the
detection question. Any detection question that answers YES (symptom present) triggers
revision.

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has a non-trivial gate
[ ] C-05: namespace ordering: scout -> draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: coherent stage groupings
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
[ ] C-31: echo causal anchor at two structural levels
[ ] C-32: consumer-pull rule states negation OR equivalence
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule states BOTH negation AND bidirectional equivalence simultaneously
[ ] C-35: ARTIFACT 2 matrix table contains explicit YAML fragment column; sole-source present
[ ] C-36: ARTIFACT 0 echo exception contains "not an arbitrary convention" contrastive clause
[ ] C-37: opening failure taxonomy names F-1 and F-2; counter-move column present; "every
         construction rule is a counter-move against exactly one row" present
[ ] C-38: ARTIFACT 0 consumer-pull rule carries bridge sentence about negation + equivalence
[ ] C-39: RULE COVERAGE TABLE present (7 rows); ALL rules enumerated; completeness assertion
[ ] C-40: ARTIFACT 0 rules carry [counter: F-N] inline annotations; no rule unlabeled
[ ] C-41: failure taxonomy carries independent completeness assertion; RULE COVERAGE TABLE
         carries independent completeness assertion; BOTH present; NEITHER references the other
[ ] C-42: breadth/depth/synthesis zone commitment criteria (3-part each) declared before
         catalog opens; ARTIFACT 1 includes Zone commitment check column
[ ] C-43: RULE COVERAGE TABLE has Status-Quo Path column; failure taxonomy has Status-Quo
         Failure column; BOTH present
[ ] C-44: role-responsibility table (4 columns) appears before opening failure taxonomy
[ ] C-45: RULE COVERAGE TABLE has Owner role column; three-column manifest
[ ] C-46: every procedural step header carries co-located role attribution annotation
[ ] C-47: role table has dedicated "failure modes countered" column; C-44 PASS
[ ] C-48: role table has dedicated "steps owned" column; dual-site bidirectional ownership
[ ] C-49: FAILURE SIGNAL GALLERY present (AP-01 through AP-06) with symptom fingerprints
         and detection questions; positioned after failure taxonomy and before RULE COVERAGE
         TABLE; each AP maps to exactly one taxonomy failure; C-39 PASS
[ ] C-50: DERIVATION WALKTHROUGH present (DW-1 through DW-6) as named pre-construction
         procedure; DW-6 chain record present; ARTIFACT 2 declared to transcribe from DW-6;
         positioned before CONSTRUCTION ORDER; C-20 PASS and C-21 PASS
[ ] C-51: ABSENT in V-01
```

---

## V-02 -- Single Axis: Zone-Level Derivation Chain Contract (C-51 Only)

**Axis**: Single-axis. DERIVATION CHAIN CONTRACT table added to R17 V-01 baseline (no
DERIVATION WALKTHROUGH, no FAILURE SIGNAL GALLERY). The contract declares zone-to-zone
artifact handoffs at zone granularity before the catalog opens. ARTIFACT 2 is declared
to resolve the contract at stage granularity.

**Hypothesis**: R17 V-04 introduced C-51 but scored 42/44 (lacked C-49 and C-50). V-02
isolates C-51 cleanly against the V-01 baseline to confirm the criterion is stable in
isolation. Expected: C-49 FAIL, C-50 FAIL, C-51 PASS = 42/44.

**C-49 form**: ABSENT
**C-50 form**: ABSENT
**C-51 form**: DERIVATION CHAIN CONTRACT positioned after zone commitment criteria and before
             compound gate template; 5-column zone-granularity table (From zone / Must produce
             / For zone / Which needs / Zone-boundary label); 4 rows (breadth-in,
             breadth-to-depth, depth-to-synthesis, synthesis-to-echo); ARTIFACT 2 declared
             to resolve the contract at stage granularity; contract governs all
             Consumes/Produces entries

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
governs all Consumes/Produces entries in ARTIFACT 2. ARTIFACT 2 resolves this contract at
stage granularity: each stage's Consumes/Produces values must be traceable to the zone-boundary
handoff declared here. Status-quo failure this contract displaces: zone boundaries left as
implicit namespace-grouping transitions with no declared artifact flow across them, making
Consumes/Produces authorship decisions rather than contract obligations.

| From zone | Must produce | For zone | Which needs | Zone-boundary label |
|-----------|-------------|----------|-------------|---------------------|
| (chain origin) | (none -- starts here) | Breadth | initial discovery artifacts: competitor signals, feasibility data, intent baselines | breadth-in |
| Breadth | direction-commitment artifacts: feasibility confirmation + draft spec or proposal | Depth | validated spec baseline for adversarial stress-testing | breadth-to-depth |
| Depth | adversarial-validated artifacts: review records, flow or trace evidence, prove outcomes | Synthesis | confirmed adoption baseline + signal readiness for post-launch monitoring | depth-to-synthesis |
| Synthesis | adoption-signal artifacts: listen evidence + committed metrics + goals artifacts | Echo | live-monitoring confirmation: feature running, signals tracking, metrics committed | synthesis-to-echo |

This contract is written before the catalog opens. ARTIFACT 2 resolves this contract at stage
granularity: each stage's Consumes/Produces entries must satisfy the zone-boundary handoff
declared here. If a zone-boundary artifact type cannot be produced by the selected skills,
revise either the contract or the skill selection before Step 5a.

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.
Gates at zone-final stages must reference artifact types that satisfy the DERIVATION CHAIN
CONTRACT's corresponding zone-boundary "Must produce" row.

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

State the topic name.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect -- counter-move
against F-1). Declare 3--6 phase boundaries from first principles. Assign each to a zone
using the commitment criteria and the DERIVATION CHAIN CONTRACT declared above -- not
namespace grouping.

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
execution reads the matrix bottom-to-top. Moving echo to row N would misrepresent the
derivation direction in the artifact. Omission of # Band: from echo is normative: echo is
the derivation anchor, not a band member.
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
the zone-boundary handoffs declared in the DERIVATION CHAIN CONTRACT. The YAML fragment
column is copied directly; no annotation is authored independently.

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
[ ] C-49: ABSENT in V-02
[ ] C-50: ABSENT in V-02
[ ] C-51: DERIVATION CHAIN CONTRACT present; zone-to-zone handoff declared before catalog
         opens at zone granularity (breadth-in, breadth-to-depth, depth-to-synthesis,
         synthesis-to-echo); minimum 5 columns (From zone / Must produce / For zone /
         Which needs / Zone-boundary label); ARTIFACT 2 declared to resolve the contract
         at stage granularity; contract positioned between zone commitment criteria and
         compound gate template; zone-final stage gates audited against "Must produce"
         entries; C-20 PASS and C-17 PASS
```

---

## V-03 -- Single Axis: Failure Signal Gallery + Derivation Chain Contract (C-50 + C-51)

**Axis**: Single-axis combination of C-50 (gallery) and C-51 (zone contract). Gallery
positioned between failure taxonomy and RULE COVERAGE TABLE. Zone contract positioned
after zone commitment criteria and before compound gate template. No DERIVATION WALKTHROUGH.

**Hypothesis**: V-03 tests whether C-50 and C-51 co-exist structurally -- the gallery
operates at the diagnostic symptom level (output inspection) while the contract operates
at the zone-boundary planning level (pre-catalog interface). The two elements address
different construction phases and should not interfere. Expected: C-49 FAIL, C-50 PASS,
C-51 PASS = 43/44.

**C-49 form**: ABSENT
**C-50 form**: FAILURE SIGNAL GALLERY (AP-01 through AP-07) -- AP-07 added to cover C-51
             violation symptom: "Zone contract absent or post-catalog"
**C-51 form**: DERIVATION CHAIN CONTRACT -- same 5-column zone-granularity table as V-02;
             ARTIFACT 2 declares stage-level resolution

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Four functional roles share
responsibility for a correct program plan. Each role owns specific construction steps and
is accountable for countering specific failure modes:

| Role | Construction responsibility | Failure modes countered | Steps owned |
|------|----------------------------|------------------------|-------------|
| PM | Topic declaration; phase naming from investigation intent; synthesis zone ownership | F-1 at naming layer: phases named after investigation intent, not skill clusters | Steps 1, 2 (phase table), 6, 7 |
| Architect | Arc phase design; zone commitment criteria; zone contract; gate design; ARTIFACT 0 schema | F-1 at construction layer: catalog closed until phases declared; consumer-pull enforced; zone contract governs handoffs; gates compound | Steps 2 (ARTIFACT 0), 5a, 5b |
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
| AP-02 | Prose-only gate | Gate values read as task-completion prose: `adequate signals present`, `work in this stage is complete` -- no `::` separator, no `>= N` count floor | F-1: catalog-first | Does every non-echo gate contain both `::` and `>=`? |
| AP-03 | Forward-reference gate | Gate references an artifact type not producible by any skill listed in that stage's `skills:` array | F-1: catalog-first | For each artifact type in each gate: is there at least one skill in that stage's `skills:` array that produces it? |
| AP-04 | Echo appended without anchor | Echo appears at row N in ARTIFACT 2 without a derivation anchor in ARTIFACT 0; its position described as "where execution ends" | F-2: arbitrary-convention | Is echo at row 0 in ARTIFACT 2? Is the "not an arbitrary convention" clause present in ARTIFACT 0? |
| AP-05 | Producer-push annotation | `# Produces:` derived from skill output inventory; adjacent-stage Produces/Consumes pairs do not match | F-1: catalog-first | For each adjacent stage pair: does stage N's `# Produces:` exactly match stage N+1's `# Consumes:`? |
| AP-06 | Uncommitted zone membership | Zone assignment inferred from namespace grouping after skill selection; ARTIFACT 1 missing Zone commitment check column | F-1: catalog-first | Was the zone commitment criteria section written before Step 3? Does ARTIFACT 1 have a Zone commitment check column? |
| AP-07 | Post-catalog zone contract | Zone-boundary artifact handoffs declared after the skill catalog was opened; no pre-catalog zone-level handoff table; Consumes/Produces entries authored without a zone-contract obligation | F-1: catalog-first | Is the DERIVATION CHAIN CONTRACT present and positioned before the skill catalog? Does ARTIFACT 2 declare stage-level resolution of the zone contract? |

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

**DERIVATION CHAIN CONTRACT** (declared before catalog opens -- Owner: Architect)

Before selecting any skill, declare the zone-to-zone artifact handoff chain. This contract
governs all Consumes/Produces entries in ARTIFACT 2. Status-quo failure this contract
displaces: zone boundaries as implicit namespace-grouping transitions with no declared
artifact flow (AP-07 symptom: no pre-catalog zone-level handoff table present).

| From zone | Must produce | For zone | Which needs | Zone-boundary label |
|-----------|-------------|----------|-------------|---------------------|
| (chain origin) | (none -- starts here) | Breadth | initial discovery artifacts: competitor signals, feasibility data, intent baselines | breadth-in |
| Breadth | direction-commitment artifacts: feasibility confirmation + draft spec or proposal | Depth | validated spec baseline for adversarial stress-testing | breadth-to-depth |
| Depth | adversarial-validated artifacts: review records, flow or trace evidence, prove outcomes | Synthesis | confirmed adoption baseline + signal readiness for post-launch monitoring | depth-to-synthesis |
| Synthesis | adoption-signal artifacts: listen evidence + committed metrics + goals artifacts | Echo | live-monitoring confirmation: feature running, signals tracking, metrics committed | synthesis-to-echo |

ARTIFACT 2 resolves this contract at stage granularity: each stage's Consumes/Produces
entries must satisfy the zone-boundary handoff declared here. AP-07 symptom check: the
contract must be present and written before the catalog opens.

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.
Gates at zone-final stages must reference artifact types satisfying the DERIVATION CHAIN
CONTRACT's "Must produce" row for that zone.

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
GALLERY as a final diagnostic pass (AP-01 through AP-07). Any detection question answering
YES triggers revision.

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed at this step** (R-01, Owner: Architect -- AP-06/AP-07
symptom: zone assigned from namespace grouping; no pre-catalog zone contract). Declare
3--6 phase boundaries using zone commitment criteria and the DERIVATION CHAIN CONTRACT.

Phase names encode investigative purpose (AP-01 symptom check):
- PASS: `discovery`, `stress-test`, `signal-watch`
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which commitment criteria / contract boundary?] | PM / Architect |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema (Owner: Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) from prior stage]
  # Produces: [artifact type(s) for next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. At the zone boundary level, the DERIVATION CHAIN CONTRACT governs which
artifact types cross zone transitions; ARTIFACT 2 resolves the contract at stage granularity.
AP-05 symptom (mismatched Produces/Consumes) signals producer-push annotation error.
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

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo at row 0 -- counter-move against F-2 (AP-04 check). **ARTIFACT 2 is the sole
authoritative source.** Consumes/Produces values must satisfy both the stage-level
consumer-pull constraint (ARTIFACT 0) and the DERIVATION CHAIN CONTRACT zone-boundary
handoffs. AP-05 check: adjacent Produces/Consumes must match exactly.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

After completing the checklist, run the FAILURE SIGNAL GALLERY diagnostic pass (AP-01 through
AP-07). Any YES answer triggers revision.

```
[ ] C-01 through C-48: same as V-01
[ ] C-49: ABSENT in V-03
[ ] C-50: FAILURE SIGNAL GALLERY present (AP-01 through AP-07); positioned after failure
         taxonomy and before RULE COVERAGE TABLE; AP-07 covers zone-contract absence;
         each AP maps to exactly one taxonomy failure; C-39 PASS
[ ] C-51: DERIVATION CHAIN CONTRACT present; zone-to-zone handoff declared before catalog
         opens at zone granularity; 5 columns; 4 rows; ARTIFACT 2 declares stage-level
         resolution; AP-07 symptom references contract absence; C-20 PASS and C-17 PASS
```

---

## V-04 -- Single Axis: Derivation Walkthrough + Derivation Chain Contract (C-49 + C-51)

**Axis**: Single-axis combination of C-49 (DW) and C-51 (zone contract). The DERIVATION
CHAIN CONTRACT declares zone-granularity handoffs before the catalog opens. The DERIVATION
WALKTHROUGH traces the stage-level chain backward from echo -- governed by the contract at
the zone level. The two elements form a two-tier derivation hierarchy: contract (zone level)
governs walkthrough (stage-level backward reasoning). No FAILURE SIGNAL GALLERY.

**Hypothesis**: C-49 and C-51 are both backward-derivation structures at different
granularities. V-04 tests whether their co-presence is structurally coherent -- the zone
contract sets boundary conditions that DW must satisfy at stage resolution. Expected:
C-49 PASS, C-50 FAIL, C-51 PASS = 43/44. Candidate new signal: explicit two-tier derivation
hierarchy declaration (DW governed by zone contract).

**C-49 form**: DERIVATION WALKTHROUGH (DW-1 through DW-6); ARTIFACT 2 transcribes from
             DW-6; DW explicitly operates within the boundaries set by the zone contract
             (DW-3 = breadth-to-depth boundary; DW-4 = depth-to-synthesis boundary)
**C-50 form**: ABSENT
**C-51 form**: DERIVATION CHAIN CONTRACT; positioned after zone commitment criteria before
             compound gate template; ARTIFACT 2 declares stage-level resolution; DW
             walkthrough declared to trace within the zone contract's boundaries

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Four functional roles share
responsibility for a correct program plan. Each role owns specific construction steps and
is accountable for countering specific failure modes:

| Role | Construction responsibility | Failure modes countered | Steps owned |
|------|----------------------------|------------------------|-------------|
| PM | Topic declaration; phase naming from investigation intent; synthesis zone ownership | F-1 at naming layer: phases named after investigation intent, not skill clusters | Steps 1, 2 (phase table), 6, 7 |
| Architect | Arc phase design; zone commitment criteria; zone contract; derivation walkthrough; gate design; ARTIFACT 0 schema | F-1 at construction and reasoning layers: catalog closed; zone contract governs handoffs; DW traces them backward at stage granularity | Steps 2 (ARTIFACT 0), DW-1 through DW-6, 5a, 5b |
| Dev | Skill catalog selection; ARTIFACT 2 assembly; YAML transcription from matrix | F-1 at assembly layer: YAML transcribed from DW-6 chain via ARTIFACT 2 | Steps 3, 4, 8 |
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
| R-05 | YAML annotations authored from skill knowledge; matrix is a summary | ARTIFACT 2 as sole authoritative source; YAML transcribed from DW-6 chain via matrix (Step 8) | F-1: catalog-first | Dev |
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

Before running the DERIVATION WALKTHROUGH, declare the zone-to-zone artifact handoff chain.
This contract sets the boundary conditions the walkthrough must satisfy: DW-3 (depth-to-
synthesis handoff) must satisfy the `depth-to-synthesis` row; DW-4 (breadth-to-depth handoff)
must satisfy the `breadth-to-depth` row. Status-quo failure: zone boundaries left as implicit
transitions with no declared artifact flow, making DW chain values authorship decisions.

| From zone | Must produce | For zone | Which needs | Zone-boundary label |
|-----------|-------------|----------|-------------|---------------------|
| (chain origin) | (none -- starts here) | Breadth | initial discovery artifacts: competitor signals, feasibility data, intent baselines | breadth-in |
| Breadth | direction-commitment artifacts: feasibility confirmation + draft spec or proposal | Depth | validated spec baseline for adversarial stress-testing | breadth-to-depth |
| Depth | adversarial-validated artifacts: review records, flow or trace evidence, prove outcomes | Synthesis | confirmed adoption baseline + signal readiness for post-launch monitoring | depth-to-synthesis |
| Synthesis | adoption-signal artifacts: listen evidence + committed metrics + goals artifacts | Echo | live-monitoring confirmation: feature running, signals tracking, metrics committed | synthesis-to-echo |

The DERIVATION WALKTHROUGH below traces this contract at stage granularity. DW-3 must
produce values that satisfy the `depth-to-synthesis` row's "Must produce" declaration.
DW-4 must produce values that satisfy the `breadth-to-depth` row's "Must produce" declaration.
ARTIFACT 2 resolves the contract at the individual stage level.

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

Run this walkthrough in writing before beginning Step 1. The walkthrough traces the
DERIVATION CHAIN CONTRACT at stage granularity -- it does not author new handoff values,
it resolves the zone contract to specific stage Produces/Consumes entries. Status-quo failure
this procedure displaces: proceeding to topic declaration without establishing what the
program must deliver to echo, leaving ARTIFACT 2 Consumes/Produces as authorship decisions.

**DW-1 -- Anchor at echo (Owner: Architect):**
Echo is the terminal consumer. Name the information needs echo requires (satisfying the
`synthesis-to-echo` row in the zone contract). These are information needs, not skills:

```
echo information needs (satisfying zone contract synthesis-to-echo):
  - [first need]
  - [second need]
  - [third need]
```

**DW-2 -- Derive synthesis Produces (Owner: Architect):**
The final synthesis-zone stage must produce artifacts satisfying DW-1 (= zone contract
`synthesis-to-echo` Must produce). Record:

```
synthesis-final-stage # Produces: [artifact types satisfying DW-1 / zone contract synthesis-to-echo]
```

**DW-3 -- Derive depth-to-synthesis handoff (Owner: Architect):**
What must depth produce to enable synthesis to produce DW-2's output? This value must
satisfy the zone contract `depth-to-synthesis` Must produce row. Record:

```
depth-final-stage  # Produces: [...]   (= synthesis-first-stage # Consumes:)
[verify: satisfies zone contract depth-to-synthesis "Must produce"]
```

**DW-4 -- Derive breadth-to-depth handoff (Owner: Architect):**
What must breadth produce to enable depth to produce DW-3's output? This value must satisfy
the zone contract `breadth-to-depth` Must produce row. Record:

```
breadth-final-stage # Produces: [...]  (= depth-first-stage # Consumes:)
[verify: satisfies zone contract breadth-to-depth "Must produce"]
```

**DW-5 -- Verify breadth chain start (Owner: Architect):**
Breadth starts the chain -- no prior zone feeds it (= zone contract `breadth-in` row).

```
breadth-first-stage # Consumes: none  (chain starts here -- satisfies zone contract breadth-in)
```

**DW-6 -- Record the full derivation chain (Owner: Architect):**

```
echo
  <- [synthesis-final Produces] from DW-2  [contract: synthesis-to-echo]
     <- [depth-final Produces] from DW-3   [contract: depth-to-synthesis]
        <- [breadth-final Produces] from DW-4  [contract: breadth-to-depth]
           <- (none)  [contract: breadth-in]
```

No Consumes/Produces entry in ARTIFACT 2 may contradict the DW-6 chain. If DW-3 or DW-4
values do not satisfy the zone contract "Must produce" rows, revise before proceeding.

---

## CONSTRUCTION ORDER

Required construction sequence. The DERIVATION WALKTHROUGH above must be complete before
beginning Step 1.

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

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed** (R-01, Owner: Architect). Declare 3--6 phase boundaries
using zone commitment criteria and the DERIVATION CHAIN CONTRACT.

Phase names encode investigative purpose:
- PASS: `discovery`, `stress-test`, `signal-watch`
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which criteria / contract boundary?] | PM / Architect |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema (Owner: Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) from prior stage]
  # Produces: [artifact type(s) for next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. At the zone boundary level, the DERIVATION CHAIN CONTRACT governs which
artifact types cross zone transitions; the DERIVATION WALKTHROUGH (DW-6) resolves those
boundaries to stage-specific values; ARTIFACT 2 transcribes from DW-6. Status-quo path
displaced: each stage producing whatever its skills naturally output (R-02, Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. Status-quo path displaced: treating row-0 as a formatting choice
because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation begins;
execution reads the matrix bottom-to-top. DW-1 is where the walkthrough anchors -- echo's
information needs are the walkthrough's starting point, not its ending point.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

---

#### Step 8 -- Assemble YAML (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo at row 0 -- counter-move against F-2. **ARTIFACT 2 is the sole authoritative source.**
All Consumes/Produces values transcribed from DW-6 chain. Zone-boundary rows in ARTIFACT 2
must satisfy the DERIVATION CHAIN CONTRACT. ARTIFACT 2 simultaneously resolves the zone
contract (zone level) and transcribes the DW-6 chain (stage level).

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [from DW-6] | [from DW-6] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [from DW-6] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

```
[ ] C-01 through C-48: same as V-01
[ ] C-49: DERIVATION WALKTHROUGH present (DW-1 through DW-6); backward from echo; DW-3 and
         DW-4 verified against zone contract "Must produce" rows; DW-6 chain record present;
         ARTIFACT 2 transcribes from DW-6; C-20 PASS and C-21 PASS
[ ] C-50: ABSENT in V-04
[ ] C-51: DERIVATION CHAIN CONTRACT present; zone-granularity table (5 columns, 4 rows);
         pre-catalog; DW walkthrough declared to trace within zone contract boundaries;
         ARTIFACT 2 resolves contract at stage granularity; C-20 PASS and C-17 PASS
```

---

## V-05 -- Combined: All Three (C-49 + C-50 + C-51) with Three-Tier Derivation Architecture

**Axis**: Combined. DERIVATION CHAIN CONTRACT (C-51), DERIVATION WALKTHROUGH (C-49), and
FAILURE SIGNAL GALLERY (C-50) all present simultaneously. The three elements form an
explicit THREE-TIER DERIVATION ARCHITECTURE:

- **Tier 1 (Zone level)**: DERIVATION CHAIN CONTRACT declares artifact handoffs at zone
  granularity before the catalog opens. Sets the interface obligations for each zone boundary.
- **Tier 2 (Stage-level reasoning)**: DERIVATION WALKTHROUGH (DW-1 through DW-6) traces
  the backward chain from echo at stage granularity, operating within the zone contract's
  boundary conditions.
- **Tier 3 (Artifact transcription)**: ARTIFACT 2 bilateral trace matrix transcribes from
  the DW-6 chain, resolving Tier 1 contracts through Tier 2 reasoning to produce per-stage
  YAML annotations.

**Hypothesis**: V-01 achieves 43/44 (C-49 + C-50). V-02/V-03/V-04 introduce C-51 in
isolation or in pairs. V-05 combines all three and explicitly names the three-tier architecture
they form together. Anticipated score: C-49 PASS + C-50 PASS + C-51 PASS = 44/44.
Candidate new criterion: C-52 (three-tier derivation architecture -- explicit declaration
that zone contract governs walkthrough procedure, which governs ARTIFACT 2 transcription,
creating a named three-tier hierarchy with the tier-governance relationship declared).

**C-49 form**: DERIVATION WALKTHROUGH (DW-1 through DW-6); Tier 2 in named architecture;
             DW-3/DW-4 declared to operate within zone contract boundary conditions
**C-50 form**: FAILURE SIGNAL GALLERY (AP-01 through AP-07); AP-07 covers zone-contract
             absence; gallery also references the three-tier architecture (AP-07 symptom
             is detectable at Tier 1; AP-05 symptom detectable at Tier 2/Tier 3)
**C-51 form**: DERIVATION CHAIN CONTRACT; Tier 1 in named architecture; ARTIFACT 2 declared
             to resolve the contract (via DW-6 as the intermediate); five columns, four rows
**C-52 form (candidate)**: "THREE-TIER DERIVATION ARCHITECTURE declared explicitly, naming
             zone contract as Tier 1, walkthrough as Tier 2, ARTIFACT 2 as Tier 3; tier-
             governance relationships declared: Tier 1 governs Tier 2, Tier 2 governs Tier 3;
             no stage annotation can contradict DW-6, no DW value can contradict the zone
             contract; each tier's authority declared before the construction order begins"

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Four functional roles share
responsibility for a correct program plan. Each role owns specific construction steps and
is accountable for countering specific failure modes:

| Role | Construction responsibility | Failure modes countered | Steps owned |
|------|----------------------------|------------------------|-------------|
| PM | Topic declaration; phase naming from investigation intent; synthesis zone ownership | F-1 at naming layer: phases named after investigation intent, not skill clusters | Steps 1, 2 (phase table), 6, 7 |
| Architect | Arc phase design; zone commitment criteria; zone contract (Tier 1); derivation walkthrough (Tier 2); gate design; ARTIFACT 0 schema | F-1 at construction, zone-contract, and reasoning layers: catalog closed; zone contract governs handoffs; DW traces them at stage granularity | Steps 2 (ARTIFACT 0), contract, DW-1 through DW-6, 5a, 5b |
| Dev | Skill catalog selection; ARTIFACT 2 assembly (Tier 3); YAML transcription from matrix | F-1 at assembly layer: YAML transcribed from DW-6 chain via ARTIFACT 2 | Steps 3, 4, 8 |
| Team Lead | Zone commitment audit; per-stage compliance; terminal validation | F-1 and F-2 completeness: all criteria verified, echo anchor confirmed, three-tier chain audited | Steps 9, 10 |

Before writing a single stage, internalize the two failure modes this protocol is designed
to prevent. Each failure has a concrete status-quo behavior that produces it:

| Failure ID | Failure Name | Status-Quo Failure (inertia) | What it produces | Design counter-move |
|------------|--------------|------------------------------|------------------|---------------------|
| F-1 | Catalog-first construction | Open the catalog; group skills by namespace; name stages after clusters; append echo at end | Stages labeled after skill clusters; zone membership implied by grouping, not declared; gates are prose task-completion checks; investigative intent absent; echo appended as afterthought | Arc-before-catalog construction order: phases declared by zone with catalog closed; zone contract declares inter-zone handoffs; backward walkthrough derives stage chains; ARTIFACT 2 transcribes from chain |
| F-2 | Arbitrary-convention misreading | Place echo at row N because execution ends there; treat row position as a formatting choice | Echo's row-0 position treated as a stylistic sort-order choice that could be row-1 or row-N with equal validity; derivation direction severed from structural encoding | Row-0 position declared as causal consequence of echo's anchor role: the derivation begins at echo and reads backward; row 0 is where derivation begins, not where execution ends |

This table is self-certifying: every failure mode this protocol counters appears as exactly
one row. Two rows; no failure mode omitted.

Every construction rule in this protocol is a counter-move against exactly one row in this table.

**FAILURE SIGNAL GALLERY**

The taxonomy above names failure modes at the abstract level. This gallery names their
observable symptoms -- what you see in a produced output when the failure has occurred.
Symptoms are organized by derivation tier: Tier 1 (zone contract), Tier 2 (walkthrough),
Tier 3 (ARTIFACT 2 / YAML). Use as a diagnostic checklist before auditing the final YAML.

| AP-ID | Anti-Pattern Name | Symptom fingerprint (what you see in the output) | Failure signaled | Detection question |
|-------|-------------------|--------------------------------------------------|------------------|--------------------|
| AP-01 | Namespace-named stages | Stage `name:` values contain namespace tokens: `scout_phase`, `prove_block`, `listen_monitoring` | F-1: catalog-first | Does any `name:` field contain a namespace identifier or skill cluster label? |
| AP-02 | Prose-only gate | Gate values read as task-completion prose with no `::` separator, no `>= N` count floor | F-1: catalog-first | Does every non-echo gate contain both `::` and `>=`? |
| AP-03 | Forward-reference gate | Gate references an artifact type not producible by any skill in that stage's `skills:` array | F-1: catalog-first | For each gate artifact type: is it producible by at least one skill in that stage? |
| AP-04 | Echo appended without anchor | Echo at row N in ARTIFACT 2; no "not an arbitrary convention" clause in ARTIFACT 0 | F-2: arbitrary-convention | Is echo at row 0 in ARTIFACT 2? Is the contrastive clause present in ARTIFACT 0? |
| AP-05 | Producer-push annotation | Adjacent-stage Produces/Consumes pairs do not match; `# Produces:` derived from skill inventory, not DW-6 chain (Tier 2 violation) | F-1: catalog-first | For each adjacent stage pair: does stage N's `# Produces:` exactly match stage N+1's `# Consumes:`? |
| AP-06 | Uncommitted zone membership | Zone assignment inferred from namespace grouping; ARTIFACT 1 missing Zone commitment check column | F-1: catalog-first | Was zone commitment criteria written before Step 3? Does ARTIFACT 1 have a Zone commitment check column? |
| AP-07 | Post-catalog zone contract | No pre-catalog zone-level handoff table (Tier 1 absent); Consumes/Produces entries authored without a zone-contract obligation; DW-3/DW-4 values cannot be verified against a zone boundary | F-1: catalog-first | Is the DERIVATION CHAIN CONTRACT present before the skill catalog? Does ARTIFACT 2 declare stage-level resolution of the zone contract? |

This gallery extends the failure taxonomy to the symptom level, organized by derivation tier.
Each anti-pattern maps to exactly one failure in the taxonomy above. The gallery does not
introduce new failure modes; it makes them detectable from output inspection alone.

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
| R-05 | YAML annotations authored from skill knowledge; matrix is a summary | ARTIFACT 2 as sole authoritative source; YAML transcribed from DW-6 chain via matrix (Step 8) | F-1: catalog-first | Dev |
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

**THREE-TIER DERIVATION ARCHITECTURE** (declared before catalog opens -- Owner: Architect)

The derivation chain from echo to breadth is established through three governed tiers.
Each tier's authority is declared before any construction step begins:

- **Tier 1 -- DERIVATION CHAIN CONTRACT (zone granularity)**: Declares artifact handoffs
  at zone boundaries. Authority: no DW value (Tier 2) may contradict a zone contract row.
- **Tier 2 -- DERIVATION WALKTHROUGH (stage granularity)**: Traces the backward chain from
  echo to breadth at stage resolution, governed by Tier 1 boundary conditions. Authority:
  no ARTIFACT 2 Consumes/Produces entry (Tier 3) may contradict the DW-6 chain record.
- **Tier 3 -- ARTIFACT 2 (transcription)**: Bilateral trace matrix transcribing Tier 2
  chain values into per-stage annotations. Authority: the YAML fragment column is copied
  directly; no annotation is authored from skill knowledge or tier-independent reasoning.

Status-quo failure the three-tier architecture displaces: ARTIFACT 2 Consumes/Produces
values authored as construction decisions (F-1 at assembly layer) rather than derived
through a governed two-step chain that resolves zone obligations to stage-specific artifacts.

**DERIVATION CHAIN CONTRACT -- Tier 1** (Owner: Architect)

| From zone | Must produce | For zone | Which needs | Zone-boundary label |
|-----------|-------------|----------|-------------|---------------------|
| (chain origin) | (none -- starts here) | Breadth | initial discovery artifacts: competitor signals, feasibility data, intent baselines | breadth-in |
| Breadth | direction-commitment artifacts: feasibility confirmation + draft spec or proposal | Depth | validated spec baseline for adversarial stress-testing | breadth-to-depth |
| Depth | adversarial-validated artifacts: review records, flow or trace evidence, prove outcomes | Synthesis | confirmed adoption baseline + signal readiness for post-launch monitoring | depth-to-synthesis |
| Synthesis | adoption-signal artifacts: listen evidence + committed metrics + goals artifacts | Echo | live-monitoring confirmation: feature running, signals tracking, metrics committed | synthesis-to-echo |

ARTIFACT 2 resolves this Tier 1 contract at stage granularity through the Tier 2 walkthrough.
No stage annotation may be traceable only to Tier 3 authorship; every Consumes/Produces value
must be derivable from DW-6 (Tier 2), which must be verifiable against this contract (Tier 1).

**Compound gate template** (artifact-provenance class -- counter-move against F-1):

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. Count floors: breadth and depth `>= 2`; synthesis `>= 1`.
Gates at zone-final stages must reference artifact types satisfying the zone contract "Must
produce" row for that boundary.

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

## DERIVATION WALKTHROUGH -- Tier 2: Required Pre-Construction Procedure (Owner: Architect)

Run this walkthrough in writing before beginning Step 1. This is Tier 2 of the three-tier
derivation architecture: it resolves Tier 1 zone-boundary contracts to stage-specific
Consumes/Produces values. ARTIFACT 2 (Tier 3) transcribes from the DW-6 chain. Status-quo
failure this procedure displaces: proceeding to construction without recording the backward
derivation in writing, leaving ARTIFACT 2 entries as Tier 3 authorship decisions rather than
Tier 2 transcription of a Tier 1-governed chain.

**DW-1 -- Anchor at echo (Owner: Architect):**
Echo is the terminal consumer. Name the information needs echo requires (satisfies zone
contract `synthesis-to-echo` "Which needs" column):

```
echo information needs [zone contract: synthesis-to-echo]:
  - [first need]
  - [second need]
  - [third need]
```

**DW-2 -- Derive synthesis Produces (Owner: Architect):**
Name artifact types satisfying DW-1. These satisfy zone contract `synthesis-to-echo`
"Must produce" row. Record:

```
synthesis-final-stage # Produces: [artifact types satisfying DW-1]
[zone contract row satisfied: synthesis-to-echo]
```

**DW-3 -- Derive depth-to-synthesis handoff (Owner: Architect):**
What must depth produce to enable synthesis to produce DW-2's output? This must satisfy
zone contract `depth-to-synthesis` "Must produce" row. Record:

```
depth-final-stage  # Produces: [...]   (= synthesis-first-stage # Consumes:)
[zone contract row satisfied: depth-to-synthesis]
```

**DW-4 -- Derive breadth-to-depth handoff (Owner: Architect):**
What must breadth produce to enable depth to produce DW-3's output? This must satisfy
zone contract `breadth-to-depth` "Must produce" row. Record:

```
breadth-final-stage # Produces: [...]  (= depth-first-stage # Consumes:)
[zone contract row satisfied: breadth-to-depth]
```

**DW-5 -- Verify breadth chain start (Owner: Architect):**
Breadth starts the chain -- satisfies zone contract `breadth-in` row.

```
breadth-first-stage # Consumes: none  (chain starts here)
[zone contract row satisfied: breadth-in]
```

**DW-6 -- Record the full derivation chain (Owner: Architect):**

```
echo
  <- [synthesis-final Produces] from DW-2  [Tier 1: synthesis-to-echo satisfied]
     <- [depth-final Produces] from DW-3   [Tier 1: depth-to-synthesis satisfied]
        <- [breadth-final Produces] from DW-4  [Tier 1: breadth-to-depth satisfied]
           <- (none)  [Tier 1: breadth-in satisfied]
```

ARTIFACT 2 (Tier 3) transcribes Consumes/Produces values from this chain. AP-05 symptom
(mismatched adjacent Produces/Consumes) is a Tier 3 transcription error against the DW-6
chain. AP-07 symptom (no zone contract) is a Tier 1 absence that makes DW-3/DW-4 values
unverifiable. All three tiers must be consistent: Tier 3 from Tier 2, Tier 2 from Tier 1.

---

## CONSTRUCTION ORDER

Required construction sequence. The THREE-TIER DERIVATION ARCHITECTURE above (Tier 1 zone
contract + Tier 2 walkthrough) must be complete before beginning Step 1.

1. Declare the topic (Step 1) -- Owner: PM
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2) -- Owner: PM / Architect
3. Select skills from catalog (Step 3) -- Owner: Dev
4. Assign skills to declared phases (Step 4) -- Owner: Dev
5a. Design gates in compound lineage prefix format (Step 5a) -- Owner: Architect
5b. FORWARD REFERENCE audit (Step 5b) -- Owner: Architect
6. Write per-phase intent questions (Step 6) -- Owner: PM
7. Encode `evidence_arc:` field (Step 7) -- Owner: PM
8. Assemble YAML from ARTIFACT 2 -- Tier 3 (Step 8) -- Owner: Dev
9. Per-stage compliance table (Step 9) -- Owner: Team Lead
10. Terminal validation checklist (Step 10) -- Owner: Team Lead

---

#### Step 2 -- Declare Arc Phases (Owner: PM / Architect)

**The catalog must remain closed** (R-01 -- AP-06 symptom: zone from namespace grouping;
AP-07 symptom: no pre-catalog zone contract). Declare 3--6 phases using commitment criteria
and Tier 1 zone contract.

Phase names encode investigative purpose (AP-01 check):
- PASS: `discovery`, `stress-test`, `signal-watch`
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question | Zone commitment check | Owner |
|-------------|------|------------------------|-----------------------|-------|
| [name] | breadth/depth/synthesis | [...?] | [Which criteria / Tier 1 boundary?] | PM / Architect |

**Before ARTIFACT 1, produce ARTIFACT 0 -- Per-Stage Annotation Schema (Owner: Architect):**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) from prior stage]
  # Produces: [artifact type(s) for next stage]

Consumer-pull rule [counter: F-1]: # Produces: for each stage is determined by what the next
stage declares as # Consumes: -- not by the prior stage's skill output inventory. Equivalently:
this stage produces the artifacts that close the next stage's input gap. The negation closes
the producer-push misreading; the equivalence makes the rule self-verifying from both ends
simultaneously. In the three-tier architecture: Consumes/Produces values are not authored
(Tier 3 independent reasoning) -- they are transcribed from DW-6 (Tier 2), which was governed
by the zone contract (Tier 1). AP-05 symptom (mismatched pairs) is a Tier 3 transcription
error that breaks the three-tier chain. Status-quo path displaced: each stage producing
whatever its skills naturally output (R-02, Owner: Architect).

Echo exception [counter: F-2]: echo carries no # Band: annotation. Echo's row-0 position in
ARTIFACT 2 is not an arbitrary convention -- it is the structural encoding of echo's anchor
role as terminal consumer. In the Tier 2 walkthrough, DW-1 anchors at echo's information
needs: echo is both the Tier 1 zone-contract terminal node (synthesis-to-echo) and the
Tier 2 walkthrough starting point. Status-quo path displaced: treating row-0 as a formatting
choice because "execution ends at echo" (R-07, Owner: Architect). Row 0 is where derivation
begins; execution reads the matrix bottom-to-top.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role | Zone commitment check`

AP-06 symptom check: Zone commitment check column must be present and non-empty.

---

#### Step 8 -- Assemble YAML -- Tier 3 (Owner: Dev)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

ARTIFACT 2 is Tier 3 of the three-tier derivation architecture. Echo at row 0 -- counter-move
against F-2 (AP-04 check). **ARTIFACT 2 is the sole authoritative source.** All Consumes/
Produces values transcribed from DW-6 chain (Tier 2). Zone-boundary stage entries must
satisfy the zone contract Tier 1 "Must produce" rows. AP-05 check: adjacent pairs must
match. AP-07 check: zone contract present and pre-catalog.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives per zone contract: synthesis-to-echo] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last stage] | [B-NN] | [question?] | [role] | [from DW-6 Tier 2] | [from DW-6 Tier 2] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first stage] | [B-01] | [question?] | [role] | -- | [from DW-6 Tier 2] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema: same as V-01.

---

#### Step 9 -- Per-Stage Compliance Table (Owner: Team Lead)

| Stage | Arc-Structure: `phase:` maps to zone? | Gate-Behavior: compound `{stage-id}::` with `>=N`? | Question-Framing: `intent:` genuine interrogative? | Zone commitment satisfied? |
|-------|--------------------------------------|---------------------------------------------------|---------------------------------------------------|-----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10. Also verify: do zone-final stage gates reference
artifact types satisfying the zone contract "Must produce" rows?

---

#### Step 10 -- Terminal Validation Checklist (Owner: Team Lead)

After completing the checklist, run the FAILURE SIGNAL GALLERY diagnostic pass (AP-01 through
AP-07). Any YES answer triggers revision. AP-07 specifically checks Tier 1 (zone contract
pre-catalog presence and ARTIFACT 2 resolution declaration).

```
[ ] C-01 through C-48: same as V-01
[ ] C-49: DERIVATION WALKTHROUGH present (DW-1 through DW-6) as Tier 2; backward from echo;
         DW-3/DW-4 verified against Tier 1 zone contract "Must produce" rows; DW-6 chain
         record with Tier 1 satisfaction annotations; ARTIFACT 2 transcribes from DW-6;
         C-20 PASS and C-21 PASS
[ ] C-50: FAILURE SIGNAL GALLERY present (AP-01 through AP-07); positioned after failure
         taxonomy and before RULE COVERAGE TABLE; AP-07 covers Tier 1 absence; each AP
         maps to exactly one taxonomy failure; organized by derivation tier; C-39 PASS
[ ] C-51: DERIVATION CHAIN CONTRACT present as Tier 1; zone-granularity table (5 columns,
         4 rows: breadth-in, breadth-to-depth, depth-to-synthesis, synthesis-to-echo);
         pre-catalog; ARTIFACT 2 declared to resolve the contract via DW-6; C-20 PASS
         and C-17 PASS
[ ] C-52 (candidate): THREE-TIER DERIVATION ARCHITECTURE declared explicitly before
         CONSTRUCTION ORDER; three tiers named (zone contract / walkthrough / ARTIFACT 2);
         tier-governance relationships declared (Tier 1 governs Tier 2; Tier 2 governs
         Tier 3); no stage annotation traceable only to Tier 3 independent authorship;
         echo is declared as both Tier 1 terminal node (synthesis-to-echo) and Tier 2
         walkthrough anchor (DW-1); AP-07 in gallery references Tier 1 absence
```
