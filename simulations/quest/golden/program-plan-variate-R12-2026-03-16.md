---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 12
rubric: v12
rubric_date: 2026-03-16
total_pts: 255
golden_threshold: 235
new_criteria: C-38, C-39, C-40
---

# program-plan -- R12 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v12 (C-01 through C-40, 255 pts, golden >= 235).

**R12-2026-03-15 retrospective under new v12 rubric (C-38/C-39/C-40 added):**
- All five 2026-03-15 R12 variates achieved 240/240 on the old 240-pt rubric.
- Under the new 255-pt rubric, all five fail C-38, C-39, and C-40:
  - C-38 FAIL: All five use neutral "BAD PLAN" headers without affirmative full-criterion
    coverage claims -- passes C-36 (no false restriction) but no variate makes a positive
    assertion that all 7 criteria are indexed below.
  - C-39 FAIL: No variate annotates `skills:` entries in the BAD PLAN block with
    `# WRONG C-03` at the field line -- C-03 violations are tagged elsewhere (gate or header)
    but the skills-field co-location pattern is absent.
  - C-40 FAIL (or unchecked): C-34 and C-29 were both present in R12-V-04 and R12-V-05 -- the
    first variants to achieve both simultaneously -- but C-40 was not a named criterion in the
    old rubric and was not explicitly targeted. All five new R12 variations must re-confirm both
    C-34 and C-29 pass independently and that their conjunction is named.

**New rubric scoring delta:**
- 240 -> 255 total pts (33 aspirational criteria; +15 from C-38/C-39/C-40 at 5 pts each)
- Golden threshold: 235 (same proportional bar: ~92%)

**R12 design constraint (2026-03-16):** All five variations must satisfy C-38, C-39, and C-40
on top of the full C-01 through C-37 coverage demonstrated in 2026-03-15 R12 variates.

**Canonical C-38 language (BAD PLAN header affirmative full-criterion claim):**
- Must affirmatively name all 7 criteria: "all 7 criteria," "C-01 through C-07," or
  "essential and recommended violations"
- PASS: `# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below`
- PASS: `# BAD PLAN: essential and recommended violations, all field types annotated`
- FAIL (neutral): `# BAD PLAN` alone -- no scope assertion
- FAIL (still neutral): `# BAD PLAN: violations example` -- no criterion count
- C-36 prerequisite (header does not falsely restrict) must also pass

**Canonical C-39 requirement (skills-field C-03 annotation in BAD PLAN):**
- Every `skills:` entry in BAD PLAN block containing an invented/unrecognized skill name
  must carry `# WRONG C-03` inline at that exact skills-field line
- Completing the three-field co-location pattern: C-26 (gate_fail: field), C-37 (name: field),
  C-39 (skills: field)
- PASS: `- make-a-plan  # WRONG C-03: invented skill name, not in Signal catalog`
- FAIL: `- make-a-plan` without annotation, even if C-03 is tagged at gate or name position

**Canonical C-40 requirement (C-34 + C-29 conjunction):**
- C-34 must pass: every `gate_fail:` field carries both `# WRONG C-04` AND `Why:` at field
- C-29 must pass: correction table contains C-05, C-06, and C-07 wrong-to-correct pairs
- Neither substitutes for the other: template-zone teaching (C-34) and lookup-table teaching
  (C-29) address distinct teaching moments (mid-authoring vs pre-authoring)

**Variation axes for R12 (2026-03-16):**
- V-01 (single): C-38 Affirmative-Header Banner -- header leads with a banner-style claim
  naming all 7 criteria by number; compact formal register
- V-02 (single): C-39 Three-Field Co-Location Named Rule -- explicit "THREE-FIELD
  CO-LOCATION RULE" declared as a design principle, BAD PLAN organized by field type;
  formal/structured register
- V-03 (single): C-40 Dual-Teaching-Moment Discovery -- tutorial voice frames C-34 as
  "mid-authoring reference" and C-29 as "pre-authoring checklist," discovery register
- V-04 (combined): C-38 + C-39 Failure-Taxonomy Anatomy -- inertia-first opening names
  silent-header and untethered-skills-tag as gap failure modes; analytical register
- V-05 (full): Complete Three-Criteria Integration -- strongest formulation of C-38, C-39,
  C-40 plus all C-01 through C-37; comprehensive reference register

---

## V-01 -- C-38 Affirmative-Header Banner

**Axis**: Single-axis variation on C-38. The BAD PLAN section opens with a banner-style
header that names all 7 criteria by number as an affirmative positive claim before any YAML
appears. The design principle: a neutral "BAD PLAN" header leaves coverage scope ambiguous --
a model cannot determine from the header alone whether recommended criteria are illustrated.
An affirmative claim primes the model to locate all 7 criterion tags before scanning. C-39
and C-40 are also satisfied (skills-field C-03 tags; C-34 + C-29 both present). Register:
compact formal/reference, table-first preamble, minimal prose.

**Hypothesis**: Leading the BAD PLAN section with an explicit "all 7 criteria (C-01 through
C-07)" claim removes all ambiguity about coverage scope. The claim is verifiable: a model
reading it will look for 7 criterion tags and confirm or disconfirm each. Compact register
tests whether all new criteria survive format compression. Anticipated score: 255/255.

**C-38 form**: Banner header in BAD PLAN section: "all 7 criteria (C-01 through C-07) indexed
below" as the section title.
**C-39 form**: Every invalid skills entry in BAD PLAN carries `# WRONG C-03` inline.
**C-40 form**: C-34 (compound gate_fail: annotation) + C-29 (correction table C-05/C-06/C-07
pairs) both present independently.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the
program is a plan, not an executor. The chain begins at the end: echo is the terminal consumer
whose implicit information needs seed the entire backward derivation that determines every
prior stage's Produces/Consumes pair.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones:** **Breadth** -- problem-space understanding before committing to direction;
scout and draft skills. **Depth** -- adversarial stress-test before shipping commitment; prove,
review, flow, trace skills. **Synthesis** -- post-launch signal monitoring; listen, metrics,
goals skills.

**Compound gate template (artifact-provenance class):**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Single expression. `{stage-id}` must match `name:` exactly. `>= N` and `{namespace}:{skill}`
both required. Failure mode to prevent: **catalog-first construction** -- skill clustering
before zone declaration destroys all three knowable classes simultaneously.

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

Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.** Opening the catalog before phase declaration
infects the arc with skill availability bias -- zone assignments become retroactively shaped
by catalog availability rather than declared investigative intent.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`,
`depth`, or `synthesis`. Phase names encode investigative purpose:
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
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The derivation runs backward
from echo; YAML annotations are transcribed from the backward derivation, not authored from
skill knowledge.

Echo exception: echo carries no # Band: annotation. Echo's row-0 position in ARTIFACT 2 is
not an arbitrary convention -- it is the structural encoding of echo's anchor role as terminal
consumer. Echo's implicit information needs seed the entire backward derivation from which
every prior stage's Produces/Consumes pair is determined. Row 0 is where derivation begins,
not where execution ends. Omission of # Band: from echo is normative, not an oversight: echo
is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition over used namespaces).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

For each non-echo zone, use the three-field gate structure to enforce compliance at authoring time:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [dependency-bearing zones only]
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: placeholder too]
name: <phase-label>
...
skills:
  - <namespace>:<skill>  # check correction table: skill names
  # requires: <artifact> from Zone: <prior-zone-name> (C-05)
  # check correction table: skill names
gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Pass/fail reference:
- PASS gate: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, no stage-id): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

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
matrix and YAML cannot diverge because YAML is defined as a downstream rendering of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add `phase:`, `intent:`,
`skills:`, and `gate_fail:`/`gate_pass:`/`gate:` fields):

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>                    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                                # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true
    skills: []  # REQUIRED: empty
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phases declared by zone in Step 2, catalog closed | C-20 | Phase names echo namespace groups -- zone membership retroactively shaped | Phase map locked in Step 2; catalog not opened until Step 3 |
| Each phase has a phase-specific question ending with `?` | C-12 | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` genuine interrogative? |
|-------|---------------------------------------|-------------------------------------|----------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; top-level stages array present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate (artifact-verifiable)
[ ] C-05: namespace ordering respected: scout/draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08: at least one gate with quantified threshold (>= N)
[ ] C-09: stage sequence reflects deliberate evidence arc (breadth -> depth -> synthesis)
[ ] C-10: at least one essential-criterion BAD/GOOD contrast pair present
[ ] C-11: at least one essential requirement enforced structurally (echo pre-positioned)
[ ] C-12: all four essential criteria have >= 2 independent anchors each
[ ] C-13: arc phases are the primary structural division of the prompt
[ ] C-14: echo and structural slots carry deletion-resistance annotations (# REQUIRED)
[ ] C-15: plan-level BAD YAML block present (multi-field, explicitly labeled)
[ ] C-16: at least one error example carries explicit criterion tag (# WRONG C-XX)
[ ] C-17: every arc zone carries inline PASS/FAIL gate example
[ ] C-18: correction table with >= 3 wrong-to-correct pairs present
[ ] C-19: error artifacts cover both essential AND recommended criteria (C-05/C-06/C-07)
[ ] C-20: every dependency-bearing zone carries inline prerequisite statement at skills: line
[ ] C-21: YAML template fields carry # check correction table navigational bridges
[ ] C-22: error artifacts cover ALL THREE recommended criteria (C-05, C-06, C-07)
[ ] C-23: dependency reminders at BOTH zone-header AND skills: placeholder positions
[ ] C-24: gate contrast as actual YAML template fields (gate_fail:/gate_pass:)
[ ] C-25: gate contrast pairs carry Why: explanation at each FAIL and PASS example
[ ] C-26: each gate_fail: field carries inline # WRONG C-04 criterion-reference tag
[ ] C-27: all dependency reminders use identical syntactic form across zones and positions
[ ] C-28: production gate: field present as sibling alongside gate_fail:/gate_pass: fields
[ ] C-29: correction table contains wrong-to-correct pairs for C-05, C-06, AND C-07
[ ] C-30: dep reminder AND correction bridge independently coexist at skills: lines
[ ] C-31: BAD PLAN block carries # WRONG C-XX tags for all 7 criteria (C-01 through C-07)
[ ] C-32: production gate: field carries # check correction table: gate values bridge
[ ] C-33: ARTIFACT 2 is declared as sole authoritative source; YAML transcribed, not authored
[ ] C-34: consumer-pull rule states BOTH negation ("not by the prior stage's skill output
         inventory") AND equivalence ("Equivalently: this stage produces the artifacts that
         close the next stage's input gap") simultaneously in the same statement
[ ] C-35: ARTIFACT 2 matrix contains explicit YAML fragment column (visible before any prose
         declaration states YAML is a rendering of the matrix)
[ ] C-36: ARTIFACT 0 echo exception carries explicit contrastive clause foreclosing the
         arbitrary-convention misreading: "not an arbitrary convention" or equivalent
[ ] C-37: every wrong-format name: value in BAD PLAN block violating C-06 carries
         # WRONG C-06 inline at the name: field itself
[ ] C-38: BAD PLAN header affirmatively claims full-criterion coverage: "all 7 criteria,"
         "C-01 through C-07," or "essential and recommended violations"
[ ] C-39: every skills: entry in BAD PLAN block containing an invented/invalid skill name
         carries # WRONG C-03 inline at the skills-field line itself
[ ] C-40: C-34 and C-29 both pass independently (compound gate_fail: annotation AND
         correction table recommended-tier pairs simultaneously present)
```

---

## CORRECTION TABLE

Consult before authoring any field. Wrong-to-correct pairs for all criteria.

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all tasks finished"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- make-a-plan` | `- program:plan` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_stage` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_block` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` | `draft:spec` in earlier stage, `review:design` in later | C-05 |
| `flow:lifecycle` before `review:design` | `review:design` before `flow:lifecycle` | C-05 |
| `"Execute all skills and proceed"` | plan framed as signal artifact, not executor | C-07 |
| `program:` top-level missing | `program:` as top-level key, `stages:` as list | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
# (essential: C-01 C-02 C-03 C-04 | recommended: C-05 C-06 C-07)

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements          # WRONG C-03: invented skill name, not in Signal catalog
      - make-a-plan                  # WRONG C-03: invented skill name, not in Signal catalog
    gate: "done"                     # WRONG C-04: execution-state, not artifact-verifiable

  - name: review_and_prove           # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: invented skill name, not in Signal catalog
    gate: "complete"                 # WRONG C-04: execution-state, not artifact-verifiable

  - name: echo
    # WRONG C-02: echo missing auto: true; echo has skills listed
    skills:
      - listen:adoption
    # WRONG C-07: plan has no framing as a signal artifact; no purpose or strategy field

# Summary of violations: C-01 (no program: key), C-02 (echo broken),
# C-03 (3 invented skills), C-04 (2 execution gates), C-05 (dep order wrong),
# C-06 (2 namespace-label names), C-07 (no plan identity)
```

---

## V-02 -- C-39 Three-Field Co-Location Named Rule

**Axis**: Single-axis variation on C-39. A "THREE-FIELD CO-LOCATION RULE" is declared as an
explicit design principle adjacent to the BAD PLAN block, naming all three YAML field types
that require inline criterion-tag co-location: `gate_fail:` (C-26), `name:` (C-37), and
`skills:` (C-39). The BAD PLAN section is organized by field type with labeled subsections
so each co-location rule has a named home. C-38 and C-40 also satisfied. Register:
formal/structured with named rules and labeled subsections.

**Hypothesis**: Naming the three-field co-location principle as an explicit rule (rather than
letting each criterion teach it implicitly) makes C-39 feel like the completion of a pattern
rather than an isolated requirement. A model reading the THREE-FIELD CO-LOCATION RULE before
the BAD PLAN block understands why skills: entries need annotation: it is the same reason
gate and name fields need annotation, and the rule names all three simultaneously. Anticipated
score: 255/255.

**C-38 form**: BAD PLAN header: "essential and recommended violations (C-01 through C-07),
three-field co-location complete."
**C-39 form**: THREE-FIELD CO-LOCATION RULE declares the pattern; BAD PLAN skills: entries
annotated at field line.
**C-40 form**: C-34 (compound gate_fail: annotation) + C-29 (correction table C-05/C-06/C-07
pairs) both present.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the
program is a plan, not an executor. Echo is the terminal consumer: its implicit information
needs seed the entire backward derivation that determines every prior stage's Produces/Consumes
pair. That is why echo is row 0 of the bilateral trace matrix you will build in Step 8.

The failure mode this protocol prevents: **catalog-first construction** -- opening the catalog
first, grouping skills into stages, labeling stages after their skill clusters. The result
cannot be audited: zone membership is implied by namespace grouping; gates are prose checks;
investigative intent is absent. Echo is appended as an afterthought rather than serving as
the derivation anchor.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- declared per-stage | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

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

Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed.** Opening the catalog before phase declaration infects the
arc with skill availability bias.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`. Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

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
from echo; YAML annotations are transcribed from the backward derivation, not authored from
skill knowledge.

  ROW-0 RULE: Echo's row-0 position in ARTIFACT 2 is not an arbitrary convention -- it is a
  design contract encoding derivation direction. Echo is the terminal consumer; the entire
  derivation chain begins from what echo must receive and works backward. Row 0 is where
  derivation begins, not where execution ends. Moving echo to any other row would misrepresent
  the derivation direction in the artifact. Omission of # Band: from echo is normative: echo
  is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog now.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone header -- dep zones only]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: placeholder]
skills:
  - <namespace>:<skill>    # check correction table: skill names
gate_fail: "<execution-state>"  # WRONG C-04: Why: not artifact-verifiable, fails evidence-state requirement
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Pass/fail:
- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL: `adequate discovery signals present` (no prefix, no threshold)
- FAIL: `>= 3 scout artifacts` (threshold only, no stage-id)

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE audit

For each non-echo stage: verify gate artifacts are producible by skills in that stage. Fix
all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
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

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo is the terminal consumer; row 0 is where derivation begins. **ARTIFACT 2 is the sole
authoritative source for all per-stage annotations.** The YAML fragment column is the
authoritative form of each annotation. Copy it directly; do not author YAML annotations
outside this matrix. The matrix and YAML cannot diverge because YAML is defined as a rendered
column of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>               # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state>"    # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true
    skills: []  # REQUIRED: empty
```

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to zone? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|------------------------|-------------------------------------|--------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-37: (same as V-01 checklist above)
[ ] C-38: BAD PLAN header affirmatively states "essential and recommended violations
         (C-01 through C-07), three-field co-location complete"
[ ] C-39: every skills: entry in BAD PLAN block with invalid skill name carries
         # WRONG C-03 inline at the skills-field line (THREE-FIELD CO-LOCATION RULE: gate/name/skills)
[ ] C-40: C-34 (compound gate_fail: annotation at every zone) AND C-29 (correction table
         C-05/C-06/C-07 pairs) both independently pass
```

---

## THREE-FIELD CO-LOCATION RULE

Before reading the BAD PLAN block, understand this principle: criterion-reference tags must
appear at the exact field position that violates the criterion -- not at adjacent fields, not
in header comments, not only in the correction table. Three field types carry criterion-testable
values in program.yaml; all three must have their tags co-located at the violating field:

| Field type | Criterion | Tag required at field |
|------------|-----------|----------------------|
| `gate:` / `gate_fail:` values | C-04 (execution-state gate) | `# WRONG C-04` on `gate_fail:` line |
| `name:` values | C-06 (namespace-label, not intent-describing) | `# WRONG C-06` on `name:` line |
| `skills:` entries | C-03 (invented or unrecognized skill name) | `# WRONG C-03` on skills-entry line |

A BAD PLAN block where C-03 violations are tagged at the gate field but not at the skills
line satisfies C-31 (tag exists in the block) but fails C-39 (tag absent at the field itself).
The same logic applies to C-04 (at gate_fail:) and C-06 (at name:). All three must be complete.

---

## CORRECTION TABLE

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all skills executed"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- build-prototype` | `- prove:prototype` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage | C-05 |
| `flow:lifecycle` before any `review:*` stage | `review:*` in prior stage | C-05 |
| `listen:*` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and advance"` | `strategy:` or `purpose:` framing the plan as artifact | C-07 |
| `program:` key missing (top-level is `stages:`) | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## BAD PLAN -- essential and recommended violations (C-01 through C-07), three-field co-location complete

```yaml
# BAD PLAN -- essential and recommended violations (C-01 through C-07),
# three-field co-location complete (gate_fail: / name: / skills: all annotated at field)

stages:                                  # WRONG C-01: missing program: top-level key
  - name: scout_and_draft                # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements              # WRONG C-03: invented skill, not in Signal catalog
      - make-a-plan                      # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "done"                    # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"                         # remove this; use gate_pass form

  - name: prove_and_review               # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed here before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                     # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "complete"                # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"                     # remove this; use gate_pass form

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing paragraph

# THREE-FIELD CO-LOCATION COMPLETE:
# gate_fail: lines carry # WRONG C-04 (C-26 satisfied)
# name: lines carry # WRONG C-06 (C-37 satisfied)
# skills: lines carry # WRONG C-03 (C-39 satisfied)
```

---

## V-03 -- C-40 Dual-Teaching-Moment Discovery (Tutorial Register)

**Axis**: Single-axis variation on C-40. Tutorial second-person voice throughout. C-40 is the
discovery moment: the prompt explicitly frames the correction table as a "pre-authoring
checklist" (consulted before writing any field) and the gate_fail: compound annotation as a
"mid-authoring reference" (encountered during generation). The two teaching moments are named
and distinguished so a model understands they are additive, not alternative. C-38 and C-39
also satisfied. Register: tutorial/discovery second-person.

**Hypothesis**: When C-40's two teaching formats are named by their temporal role (pre-authoring
vs mid-authoring), the conjunction feels motivated by functional difference rather than
redundancy. A model understands that the correction table is what you scan before you write,
and the gate_fail: annotation is what you encounter as you write -- both are necessary because
different errors appear at different times in the authoring process. Anticipated score: 255/255.

**C-38 form**: BAD PLAN header names all 7 criteria with tutorial framing: "all 7 criteria
(C-01 through C-07) -- check your work against each tag below."
**C-39 form**: Skills-field annotations framed as "you'll notice each invalid skill name has
its reason right there at the line."
**C-40 form**: Explicit "DUAL TEACHING MOMENT" subsection names C-34 (mid-authoring) and
C-29 (pre-authoring) as two distinct teaching channels.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. Before you write a single stage,
you need to understand where the chain begins -- and it begins at the end. Echo, the final
stage, is the terminal consumer: everything the plan produces ultimately flows to echo. Its
implicit information needs determine what the last stage must produce, which determines what
the second-to-last stage produces, and so on backward to the first breadth stage. That is
why echo is row 0 of the bilateral trace matrix you will build -- the entire derivation reads
backward from it. Every skill runs standalone; the program is a plan, not an executor.

The failure mode to prevent: **catalog-first construction** -- opening the catalog, clustering
skills into stages, labeling stages after their clusters. You cannot audit the result. Zone
membership is never declared; gates are prose; phases answer "what skills ran" not "what we
needed to learn."

To keep your plan auditable at every stage boundary, you will maintain three classes of
knowable information:

| Class | What you must keep knowable | Criterion ladder |
|-------|----------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before you open the catalog | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- not "what skills ran" but "what did we need to learn" | Question-framing ladder |

**Lifecycle zones -- commit before opening the catalog:**
- **Breadth** -- do you understand the problem space well enough to commit to a direction?
  Scout and draft skills produce breadth artifacts.
- **Depth** -- does your design survive adversarial conditions? Prove, review, flow, and trace
  skills stress-test it.
- **Synthesis** -- are users adopting and signaling as expected? Listen, metrics, and goals
  skills monitor post-launch reality.

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

Three components: `{stage-id}` names the producing stage; `>= N` sets the count floor;
`{namespace}:{skill}` traces to the catalog skill. All three required in a single expression.

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

Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

What is the topic? State it now. Everything that follows derives from this name.

---

#### Step 2 -- Declare Arc Phases

Keep the catalog closed -- here is why this matters for you. If you open the catalog now,
your zone assignments will be shaped by which skills happen to exist rather than what you
need to investigate. Zone membership will be implicit rather than declared. That is
catalog-first construction entering at Step 2. Do not open the catalog until Step 3.

Declare 3--6 phase boundaries from first principles. Ask: what investigative milestones must
the team reach? Assign each to a zone: `breadth`, `depth`, or `synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema.** This is the template all stages must
satisfy:

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
produces the artifacts that close the next stage's input gap. You derive forward from echo's
needs backward; you do not enumerate skills forward and see what they happen to produce.

Echo exception: echo carries no # Band: annotation. You may wonder why echo cannot be placed
at row 1 or row N of ARTIFACT 2 rather than row 0. Its position is not a convention you are
free to vary -- it is a structural constraint imposed by derivation direction. The chain begins
at echo and works backward; row 0 is where the derivation begins. Placing echo elsewhere would
make the matrix unreadable as a derivation trace. Omission of # Band: is normative: echo is
the anchor, not a band member.
```

After ARTIFACT 0, produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog now.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates

For each dependency-bearing zone, the three-field gate structure gives you a mid-authoring
reference at the exact moment you fill the gate field:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone header]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: placeholder]
skills:
  - <namespace>:<skill>    # check correction table: skill names
gate_fail: "<execution-state>"  # WRONG C-04: Why: execution-history, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Pass/fail:
- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL: `adequate discovery signals` (no prefix, no threshold)
- FAIL: `>= 3 scout artifacts` (threshold only)

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE audit

For each non-echo stage: verify gate artifacts are producible by skills in that stage.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess compliance"` -- investigative intent unknowable

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

When you complete the matrix rows of ARTIFACT 2, you'll notice the YAML fragment column already
contains every annotation your YAML needs -- it was there the moment you filled in the matrix.
This is not a coincidence: the annotations were determined by the backward derivation, not
authored from skill knowledge. The YAML fragment column IS the annotations; transcribe it
directly.

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

Echo occupies row 0 because that is where the derivation begins. The matrix reads top-to-bottom
from echo's needs; execution runs bottom-to-top from the first breadth stage.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** Copy the YAML
fragment column directly to your YAML -- do not author annotations independently. The matrix
and YAML cannot diverge because YAML is defined as a rendered projection of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>               # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state>"    # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills. DO NOT move echo before other stages.
    auto: true  # REQUIRED
    skills: []  # REQUIRED: empty
```

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to zone? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|------------------------|-------------------------------------|--------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-37: (see V-01 checklist)
[ ] C-38: BAD PLAN header says "all 7 criteria (C-01 through C-07) -- check your work against
         each tag below"
[ ] C-39: skills: entries in BAD PLAN block with invalid names carry # WRONG C-03 at the line
         ("you'll notice each invalid skill name has its reason right there")
[ ] C-40: DUAL TEACHING MOMENT -- C-34 (mid-authoring: gate_fail: compound annotation) AND
         C-29 (pre-authoring: correction table C-05/C-06/C-07 pairs) both independently pass
```

---

## DUAL TEACHING MOMENT

Two separate teaching formats address recommended-tier errors at two separate moments in your
authoring process. Both are necessary; neither substitutes for the other.

**Pre-authoring (C-29 -- correction table):** Before you write any field, scan the correction
table below. It maps wrong forms to correct forms for all criteria including C-05 (dependency
order), C-06 (stage names), and C-07 (plan identity). You consult this before writing because
at authoring time you have not yet encountered the gate_fail: annotation -- you need the lookup
reference available before you start.

**Mid-authoring (C-34 -- compound gate_fail: annotation):** When you reach each gate field in
the template, you encounter the gate_fail: field with its criterion tag and Why: explanation
right there at the field. This is your mid-authoring reference -- it fires at the exact moment
you are filling the gate slot, not before and not after.

These two channels address different error windows. A correction table without compound
gate_fail: annotations leaves mid-authoring gate decisions without a local reference. Compound
gate_fail: annotations without a correction table leave pre-authoring recommended-tier
decisions without a lookup reference. Both formats must be present for full coverage.

---

## CORRECTION TABLE (Pre-Authoring Reference)

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "proceed to next phase"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- implement-feature` | `- prove:prototype` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` in prior stage | place `draft:spec` earlier | C-05 |
| `flow:lifecycle` with no prior `review:*` stage | place `review:design` in prior stage | C-05 |
| `listen:*` with no prior `flow:*` or `trace:*` | place `flow:*` or `trace:*` earlier | C-05 |
| `"Run all skills and proceed"` | plan with `strategy:` or framing paragraph | C-07 |
| `program:` key absent | `program:` as top-level, `stages:` nested inside | C-01 |
| `echo` missing `auto: true` | add `auto: true` | C-02 |
| `echo` with non-empty `skills:` | set `skills: []` | C-02 |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) -- check your work against each tag below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) -- check your work against each tag below

stages:                               # WRONG C-01: missing program: top-level key
  - name: scout_and_draft             # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements           # WRONG C-03: invented skill, not in Signal catalog
      - make-a-plan                   # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "done"                 # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review            # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design appears here before any draft:spec stage has produced a spec
    skills:
      - review:design
      - run-analysis                  # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "complete"             # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: plan contains no strategy:, purpose:, or plan-identity framing
```

---

## V-04 -- C-38 + C-39 Failure-Taxonomy Anatomy (Inertia-First + Analytical)

**Axes**: Combined C-38 + C-39. Opens with an inertia-first anatomy that names two gap failure
modes beyond catalog-first construction: (a) **Silent-header gap** -- BAD PLAN blocks with
neutral headers that leave coverage scope ambiguous; (b) **Untethered-skills-tag gap** -- BAD
PLAN blocks that tag C-03 violations at adjacent gate or name fields but not at the skills
entry itself. These two gaps are named as failure modes in the opening anatomy; the protocol
provides counter-moves against each. Register: inertia-first + analytical.

**Hypothesis**: When "silent header" and "untethered skills tag" are named as failure modes
alongside catalog-first construction, C-38 and C-39 become structurally load-bearing -- each
criterion is a named counter-move against a named failure, not an isolated requirement.
Anticipated score: 255/255.

**C-38 form**: Named "SILENT-HEADER COUNTER-MOVE" in the BAD PLAN section; header affirmatively
names all 7 criteria.
**C-39 form**: Named "UNTETHERED-SKILLS-TAG COUNTER-MOVE" in the BAD PLAN section; skills
entries annotated at field line.
**C-40 form**: C-34 + C-29 both present; "DUAL-COVERAGE REQUIREMENT" named in Step 10.

---

### FULL PROMPT BODY

Before writing a single stage, understand the failure modes this protocol is designed to prevent.

**Failure 1 -- Catalog-first construction**: Open the catalog, group skills into stages, label
stages after their clusters. Cannot audit: zone membership implied by namespace grouping;
gates are prose task-checks; phases answer "what skills ran" not "what we needed to learn."
Echo appended as afterthought, not used as the derivation anchor.

**Failure 2 -- Silent-header gap**: Write a BAD PLAN block covering all 7 criteria but label
it with a neutral header ("BAD PLAN," "violations example"). A model reading the header cannot
determine how many criteria to scan for. Recommended-tier tags (C-05, C-06, C-07) may exist
in the block but be skipped because the header did not prime the model to look for them.

**Failure 3 -- Untethered-skills-tag gap**: Tag C-03 violations somewhere in the BAD PLAN
block (at the gate or name field) but not at the `skills:` entry itself. A model filling a
skills slot in the template encounters the wrong shape (an invented skill name) without a
criterion tag at that exact position identifying why it is wrong. The tag exists in the
block but is spatially disconnected from the field it should annotate.

Every rule in this protocol is a counter-move against one or more of these failure modes.
Echo's anchor role is the counter-move against Failure 1. The affirmative BAD PLAN header
is the counter-move against Failure 2. The skills-field criterion-tag co-location rule is
the counter-move against Failure 3.

**Echo as derivation anchor**: Every Produces/Consumes pair is determined by working backward
from what echo must receive. That is why echo is row 0 of the bilateral trace matrix you will
build in Step 8. Every skill runs standalone; the program is a plan, not an executor.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding; scout and draft skills.
- **Depth** -- adversarial stress-test; prove, review, flow, trace skills.
- **Synthesis** -- post-launch monitoring; listen, metrics, goals skills.

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

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

Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**Counter-move against Failure 1: keep the catalog closed.** If you open the catalog here,
zone assignments will be shaped by skill availability rather than declared investigative intent.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
`synthesis`.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

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
produces the artifacts that close the next stage's input gap. Counter-move against Failure 1
at annotation level: derivation runs backward from echo, not forward from skill catalogs.

Echo exception: echo carries no # Band: annotation. Counter-move against Failure 1's echo-
as-afterthought variant: echo's row-0 position in ARTIFACT 2 is not an arbitrary convention
-- it is the structural encoding of echo's anchor role as terminal consumer. The derivation
chain begins from what echo must receive; row 0 is where derivation begins. Omission of
# Band: from echo is normative: it is the anchor node, not a band member.
```

After ARTIFACT 0, produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog now.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

For each non-echo zone:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone header -- dep zones only]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: placeholder]
skills:
  - <namespace>:<skill>    # check correction table: skill names
gate_fail: "<execution-state>"  # WRONG C-04: Why: execution-history, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE audit

Verify gate artifacts are producible by skills in each stage.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess compliance"` -- intent unknowable

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
```

---

#### Step 8 -- Assemble YAML

Counter-move against Failure 1's echo-as-afterthought: begin where the chain begins. What
does echo need to receive? Fill ARTIFACT 2 backward from that.

Before writing YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML
fragment column is authoritative -- transcribe directly. The matrix and YAML cannot diverge
because YAML is defined as a rendered column of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema:

```yaml
topic: <topic>
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>               # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state>"    # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills. DO NOT move echo before other stages.
    auto: true  # REQUIRED
    skills: []  # REQUIRED: empty
```

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to zone? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|------------------------|-------------------------------------|--------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-37: (see V-01 checklist)
[ ] C-38: SILENT-HEADER COUNTER-MOVE -- BAD PLAN header affirmatively names all 7 criteria
         (counter-move against Failure 2)
[ ] C-39: UNTETHERED-SKILLS-TAG COUNTER-MOVE -- every invalid skills: entry in BAD PLAN carries
         # WRONG C-03 at the field line itself (counter-move against Failure 3)
[ ] C-40: DUAL-COVERAGE REQUIREMENT -- C-34 (mid-authoring: gate_fail: compound annotation)
         AND C-29 (pre-authoring: correction table C-05/C-06/C-07 pairs) both independently pass
```

---

## CORRECTION TABLE

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all tasks finished"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:feedback artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- implement-prototype` | `- prove:prototype` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` with no prior `draft:spec` stage | `draft:spec` in earlier stage first | C-05 |
| `flow:lifecycle` before `review:design` | `review:design` in prior stage | C-05 |
| `listen:feedback` before any `flow:*` stage | `flow:*` in prior stage | C-05 |
| `"Execute skills and proceed"` | plan with `strategy:` or purpose framing | C-07 |
| `stages:` as top-level key | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | add `auto: true` | C-02 |
| `echo` with `skills: [listen:adoption]` | `skills: []` | C-02 |

---

## BAD PLAN -- SILENT-HEADER COUNTER-MOVE: all 7 criteria (C-01 through C-07) affirmatively indexed

```yaml
# BAD PLAN -- SILENT-HEADER COUNTER-MOVE: all 7 criteria (C-01 through C-07) affirmatively indexed
# (Failure 2 prevention: header names scope explicitly so no criterion tag is skipped on scan)
# UNTETHERED-SKILLS-TAG COUNTER-MOVE: skills: entries annotated at field line (Failure 3 prevention)

stages:                                # WRONG C-01: missing program: top-level key (Failure 1)
  - name: scout_and_draft              # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements            # WRONG C-03: invented skill, not in Signal catalog (Failure 3 counter-move: tag at field)
      - make-a-plan                    # WRONG C-03: invented skill, not in Signal catalog (Failure 3 counter-move: tag at field)
    gate_fail: "done"                  # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review             # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage
    skills:
      - review:design
      - run-analysis                   # WRONG C-03: invented skill, not in Signal catalog (Failure 3 counter-move: tag at field)
    gate_fail: "complete"              # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills non-empty
    skills: [listen:adoption]
    # WRONG C-07: no plan identity, no strategy:, no purpose framing
```

---

## V-05 -- Complete Three-Criteria Integration (Full Reference)

**Axes**: Full reference implementation with maximal formulation of C-38, C-39, and C-40
simultaneously. C-38: header format is "BAD PLAN -- essential and recommended violations
(C-01 through C-07), all field types annotated (gate_fail:/name:/skills:)" -- names both the
criterion set and the three-field co-location pattern. C-39: explicit "SKILLS-FIELD ANNOTATION
RULE" named block adjacent to BAD PLAN explains why skills entries need tags. C-40: explicit
"DUAL TEACHING CHANNELS" subsection in the correction table section names C-34 as template-zone
and C-29 as lookup-zone with their respective teaching moments. All C-01 through C-37
mechanisms preserved from strongest R12-2026-03-15 formulations.

**Hypothesis**: Naming all three new criteria as explicit design rules in dedicated subsections
makes C-38, C-39, C-40 structurally impossible to miss. A model reading the prompt encounters
a SKILLS-FIELD ANNOTATION RULE before the BAD PLAN, an affirmative header IN the BAD PLAN,
and a DUAL TEACHING CHANNELS explanation BEFORE the correction table. Each new criterion has
a labeled home at the point it matters most. Anticipated score: 255/255.

**C-38 form**: BAD PLAN header names both criterion set and field coverage:
"essential and recommended violations (C-01 through C-07), all field types annotated."
**C-39 form**: SKILLS-FIELD ANNOTATION RULE declared as named subsection before BAD PLAN.
**C-40 form**: DUAL TEACHING CHANNELS subsection names C-34 (template zone) and C-29 (lookup
zone) as independently required formats with distinct teaching-moment roles.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the
program is a plan, not an executor. The chain begins at the end: echo is the terminal consumer
whose implicit information needs seed the entire backward derivation that determines every
prior stage's Produces/Consumes pair. That is why echo is row 0 of the bilateral trace matrix
you will build in Step 8 -- the entire derivation chain reads backward from it.

The failure mode this protocol prevents: **catalog-first construction** -- opening the catalog
first, grouping skills into stages, labeling stages after their skill clusters. The result
cannot be audited: zone membership is implied by namespace grouping; gates are prose checks;
investigative intent is absent. Echo is appended as an afterthought rather than serving as
the derivation anchor from which every prior stage was backward-traced.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- declared per-stage | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

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

Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.** Opening the catalog before phase declaration
infects the arc with skill availability bias -- zone assignments become retroactively shaped
by catalog availability rather than declared investigative intent.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`. Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

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
produces the artifacts that close the next stage's input gap. The chain runs backward from
echo; YAML annotations are transcribed from the backward derivation, not authored from skill
knowledge.

Echo exception: echo carries no # Band: annotation. Echo's row-0 position in ARTIFACT 2 is
not an arbitrary convention -- it is the structural encoding of echo's anchor role as terminal
consumer and derivation origin. The entire Produces/Consumes chain is determined by working
backward from what echo must receive; row 0 is where that derivation begins. Placing echo at
any other row would misrepresent the derivation direction in the artifact. Omission of # Band:
from echo is normative, not an oversight: echo is the derivation anchor, not a band member.
```

Phase map locked after ARTIFACT 0 and the phase table are complete.

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition over used namespaces).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates (Compound Lineage Prefix Format)

For each non-echo zone, use the full four-mechanism zone structure:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone-header dep reminder]
name: <phase-label>                  # check correction table: stage names
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [skills-line dep reminder]
skills:                              # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state>"       # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Pass/fail reference:
- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- PASS: `stress-test::review-design >= 2 AND trace:contract artifact confirmed`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, no stage-id): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N`.

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

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add remaining fields):

```yaml
topic: <topic>
strategy: >
  Signal-gathering roadmap for <topic>. Each stage gate is artifact-verifiable;
  the plan does not execute skills, it sequences evidence collection.
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>                    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                                # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true
    skills: []  # REQUIRED: empty
```

**Two-criteria enforcement block:**

| Constraint | Criterion | Violation | Compliance |
|------------|-----------|-----------|------------|
| Phase boundaries declared by zone in Step 2, catalog closed | C-20 | Phase names echo namespace groups -- zone membership retroactively shaped | Phase map locked in Step 2; catalog not opened until Step 3 |
| Each phase has a phase-specific question ending with `?` | C-12 | Generic "Are we done?" -- intent unknowable | Zone-specific question anchored to zone commitment decision |

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` genuine interrogative? |
|-------|---------------------------------------|-------------------------------------|----------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |
| [stage 2] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; program: top-level key present; stages: as list
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names; no namespace-only entries
[ ] C-04: every non-echo stage has an artifact-verifiable gate (not execution-state)
[ ] C-05: namespace ordering respected: scout/draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact (strategy: field present)
[ ] C-08: at least one gate with quantified threshold (>= N)
[ ] C-09: stage sequence reflects deliberate evidence arc (breadth -> depth -> synthesis)
[ ] C-10: at least one essential-criterion BAD/GOOD contrast pair present
[ ] C-11: echo pre-positioned with # REQUIRED annotations (structural enforcement)
[ ] C-12: all four essential criteria have >= 2 independent anchors
[ ] C-13: arc phases are the primary structural division of the prompt
[ ] C-14: echo and structural slots carry # REQUIRED: DO NOT ... annotations
[ ] C-15: plan-level BAD YAML block present (multi-field, multi-stage, explicitly labeled)
[ ] C-16: at least one error example carries explicit criterion tag (# WRONG C-XX)
[ ] C-17: every arc zone carries inline PASS/FAIL gate example
[ ] C-18: correction table with >= 3 wrong-to-correct pairs
[ ] C-19: error artifacts cover both essential AND recommended criteria
[ ] C-20: dependency-bearing zones carry inline prerequisite statement at skills: line
[ ] C-21: YAML template fields carry # check correction table navigational bridges
[ ] C-22: error artifacts cover ALL THREE recommended criteria (C-05, C-06, C-07)
[ ] C-23: dep reminders at BOTH zone-header AND skills: placeholder positions
[ ] C-24: gate contrast as YAML template fields (gate_fail:/gate_pass:)
[ ] C-25: gate contrast pairs carry Why: at each FAIL and PASS example
[ ] C-26: each gate_fail: field carries inline # WRONG C-04
[ ] C-27: all dep reminders use identical syntax: # requires: <artifact> from Zone: <name> (C-05)
[ ] C-28: production gate: field present as YAML sibling alongside gate_fail:/gate_pass:
[ ] C-29: correction table contains C-05, C-06, AND C-07 wrong-to-correct pairs
[ ] C-30: dep reminder AND correction bridge independently coexist at every dep-bearing skills: line
[ ] C-31: BAD PLAN block carries # WRONG C-XX for all 7 criteria (C-01 through C-07)
[ ] C-32: production gate: field carries # check correction table: gate values bridge
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed from matrix
[ ] C-34: consumer-pull rule in ARTIFACT 0 states BOTH:
         (negation) "not by the prior stage's skill output inventory"
         (equivalence) "Equivalently: this stage produces the artifacts that close the next
         stage's input gap" -- simultaneously in the same statement
[ ] C-35: ARTIFACT 2 matrix contains explicit YAML fragment column (visibly a rendered
         projection of matrix rows before any prose declaration)
[ ] C-36: ARTIFACT 0 echo exception carries explicit contrastive clause: "not an arbitrary
         convention" or "not a convention you are free to vary" -- forecloses misreading
[ ] C-37: every wrong-format name: value in BAD PLAN block violating C-06 carries
         # WRONG C-06 inline at the name: field itself
[ ] C-38: BAD PLAN header affirmatively names all 7 criteria: "essential and recommended
         violations (C-01 through C-07), all field types annotated (gate_fail:/name:/skills:)"
[ ] C-39: SKILLS-FIELD ANNOTATION RULE satisfied -- every invalid skills: entry in BAD PLAN
         carries # WRONG C-03 inline at the skills-field line itself
[ ] C-40: DUAL TEACHING CHANNELS both pass:
         - C-34 (template-zone channel): compound gate_fail: annotation at every zone
         - C-29 (lookup-zone channel): correction table C-05/C-06/C-07 pairs present
```

---

## SKILLS-FIELD ANNOTATION RULE

Criterion-reference tags must appear at the exact field position that violates the criterion.
Three YAML field types carry criterion-testable values; all three must carry tags at the
violating field line:

| Field type | Criterion violation | Tag location |
|------------|--------------------|-|
| `gate_fail:` values | C-04 execution-state gate | `# WRONG C-04` inline on gate_fail: line (C-26) |
| `name:` values | C-06 namespace-label, not intent | `# WRONG C-06` inline on name: line (C-37) |
| `skills:` entries | C-03 invented/unrecognized skill | `# WRONG C-03` inline on skills-entry line (C-39) |

A BAD PLAN block where C-03 violations appear only in the header or at adjacent gate fields
satisfies C-31 (tag present in block) but fails C-39 (tag absent at the skills-field line
itself). All three field types must have co-located tags at their violating lines.

---

## DUAL TEACHING CHANNELS

Two teaching formats address recommended-tier errors at two distinct teaching moments.
Both are required (C-40); neither substitutes for the other.

**Template-zone channel (C-34) -- mid-authoring reference**: When you fill each gate field
in the YAML template, the gate_fail: field presents its compound annotation right there:
criterion tag + Why: explanation at the field position. This fires during generation, at the
exact moment you resolve the gate slot. The correction table is not visible at this moment;
the compound annotation is the only lookup available at field-fill time.

**Lookup-zone channel (C-29) -- pre-authoring reference**: Before you write any field, scan
the correction table. It covers all criteria including C-05 (dependency order), C-06 (stage
names), C-07 (plan identity). You consult this before writing because at authoring time you
have not yet encountered the gate_fail: annotation for any specific zone -- you need the
pre-flight reference for both structural and quality errors before any field is resolved.

C-40 requires both channels to independently function. C-34 alone leaves pre-authoring
recommended-tier errors uncovered. C-29 alone leaves mid-authoring gate decisions without
a local criterion reference. Together they close both teaching-moment windows.

---

## CORRECTION TABLE (Lookup-Zone Channel -- pre-authoring)

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all skills executed"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `gate: "proceed to next phase"` | `gate: "synthesis::listen-feedback >= 2 AND listen:adoption artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- implement-prototype` | `- prove:prototype` | C-03 |
| `- build-feature` | `- flow:lifecycle` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage first | C-05 |
| `flow:lifecycle` with no prior `review:*` | `review:design` in prior stage | C-05 |
| `listen:feedback` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and proceed to next stage"` | `strategy:` framing the plan as artifact | C-07 |
| `stages:` as top-level key | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with `skills: [listen:adoption]` | `skills: []` on echo stage | C-02 |

---

## BAD PLAN -- essential and recommended violations (C-01 through C-07), all field types annotated (gate_fail:/name:/skills:)

```yaml
# BAD PLAN -- essential and recommended violations (C-01 through C-07),
# all field types annotated (gate_fail: / name: / skills:)
# C-38: affirmative header names full criterion set and field coverage
# C-39: skills: entries annotated at field line (SKILLS-FIELD ANNOTATION RULE complete)
# C-37: name: entries annotated at field line (same rule applied)
# C-26: gate_fail: entries annotated at field line (same rule applied)

stages:                                  # WRONG C-01: missing program: top-level key
  - name: scout_and_draft                # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements              # WRONG C-03: invented skill name, not in Signal catalog
      - make-a-plan                      # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "done"                    # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review               # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has produced a spec
    skills:
      - review:design
      - run-analysis                     # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "complete"                # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills list non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- no strategy: field, no framing paragraph
```
