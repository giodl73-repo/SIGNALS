---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 13
rubric: v13
rubric_date: 2026-03-16
total_pts: 270
golden_threshold: 80
new_criteria: C-41, C-42, C-43
---

# program-plan -- R13 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v13 (C-01 through C-43, 270 pts, golden: all essential pass AND composite >= 80).

**R12-2026-03-16 state under v13 rubric (C-41/C-42/C-43 added):**
- V-01, V-03, V-04: achieve C-01 through C-40, fail C-41/C-42/C-43 → 255/270
- V-02: achieves C-01 through C-40 + C-42 (THREE-FIELD CO-LOCATION RULE) → 260/270
- V-05: achieves C-01 through C-40 + C-41 (header index) + C-42 (SKILLS-FIELD ANNOTATION RULE) + C-43 (strategy: pre-populated) → 270/270

**New rubric scoring delta:**
- 255 → 270 total pts (36 aspirational criteria; +15 from C-41/C-42/C-43 at 5 pts each)
- Golden threshold: unchanged (all essential pass AND composite >= 80)

**R13 design constraint (2026-03-16):** All five variations must satisfy C-41, C-42, and C-43 on
top of the full C-01 through C-40 coverage demonstrated in R12-2026-03-16 variates.

**Canonical C-41 form (BAD PLAN header annotation-type index):**
- Must map at least 3 of 4 annotation types to criterion numbers in the header itself
- PASS: header enumerates `# C-26: gate_fail: field`, `# C-37: name: field`, `# C-39: skills:
  entries`, `# C-38: this header` — all 4 types mapped
- PASS (partial): any 3 of the 4 mapped (e.g., C-26/C-37/C-39 with C-38 omitted or vice versa)
- FAIL: header has affirmative coverage claim (C-38) but no per-criterion annotation-type mapping
- Prerequisite: C-38 (affirmative coverage claim must be present before it can also be indexed)

**Canonical C-42 requirement (named co-location family section):**
- A named section (explicit title) appears BEFORE the BAD PLAN block
- Must present all three field types (gate_fail: / name: / skills:) as a structured family
- Must include a table or enumeration mapping: field type → criterion → annotation tag
- Prose-only paragraph mentioning the three fields does not satisfy (must be scannable table)
- Prerequisites: C-26, C-37, C-39

**Canonical C-43 requirement (strategy: pre-populated in YAML template):**
- YAML template scaffold carries `strategy: "..."` with a non-empty placeholder string
- FAIL: `strategy:` absent from template
- FAIL: `strategy: ""` (empty string)
- FAIL: `# strategy: add here` (comment placeholder only, no string value)
- PASS: `strategy: "why this feature is worth the investment — ..."` (non-empty placeholder)
- Prerequisites: C-07, C-11

**Variation axes for R13:**
- V-01 (single): C-41 Header Index Minimal -- BAD PLAN header becomes criterion-indexed
  artifact directory; 4 annotation types enumerated; C-42 and C-43 present but minimal;
  compact formal register
- V-02 (single): C-42 Named Family Section -- "FIELD CO-LOCATION PRINCIPLE" declared as a
  full 4-column structural document section before BAD PLAN; C-41 and C-43 also present;
  formal/structured register
- V-03 (single): C-43 Scaffold-Enforced Strategy Field -- YAML template strategy: pre-population
  foregrounded with explicit analogy to echo structural enforcement in Step 8; C-41 and C-42
  also present; discovery/analogy register
- V-04 (combined): C-41 + C-42 -- Header index and named section cross-reference each other;
  header says "see CO-LOCATION PRINCIPLE"; section says "header above claims coverage"; C-43
  also present; analytical register
- V-05 (full): Complete Three-Criteria Integration -- all three prominently integrated as a
  unified structural enforcement philosophy (echo/strategy: at plan level; co-location at field
  level); most comprehensive formulation; reference register

---

## V-01 -- C-41 Header Index Minimal Axis

**Axis**: Single-axis variation on C-41. The BAD PLAN header is expanded from an affirmative
coverage claim (C-38) into a criterion-indexed artifact directory: each annotation type present
in the block is enumerated inline in the header, mapping annotation type to criterion number.
The design principle: C-38 tells the model *how many* criteria are indexed; C-41 tells it
*which annotation type* addresses each one, so a model scanning the block knows before it
starts which fields to look for. C-42 (named co-location section) is present but compact.
C-43 (strategy: pre-populated) is present. Register: compact formal, table-first preamble.

**Hypothesis**: Expanding the BAD PLAN header to enumerate annotation types (C-41) removes the
inferential step where a model must discover that `gate_fail:` is annotated for C-04, `name:` for
C-06, and `skills:` entries for C-03. The header states it directly. Compact register tests whether
all three new criteria survive format compression. Anticipated score: 270/270.

**C-41 form**: Header enumerates all 4 annotation types with criterion numbers inline.
**C-42 form**: 3-column co-location table present before BAD PLAN; brief intro paragraph.
**C-43 form**: `strategy: "..."` non-empty placeholder in YAML template scaffold.

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
infects the arc with skill availability bias.

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
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [dep zones: at zone header]
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [dep zones: at skills: line too]
name: <phase-label>
...
skills:
  - <namespace>:<skill>  # check correction table: skill names
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

#### Step 5b -- FORWARD REFERENCE Audit

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

Echo is the terminal consumer. Its implicit information needs seed the entire backward derivation.
That is why echo occupies row 0 -- the derivation reads top-to-bottom from echo; forward execution
reads bottom-to-top.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** The YAML fragment
column is the authoritative form of the YAML annotation -- copy it directly. YAML annotations are
transcribed from ARTIFACT 2 matrix cells, not authored independently. The matrix and YAML cannot
diverge because YAML is defined as a downstream rendering of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (copy YAML fragment column from ARTIFACT 2, then add fields):

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
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
| Phases declared by zone in Step 2, catalog closed | C-13 | Phase names echo namespace groups | Phase map locked in Step 2; catalog not opened until Step 3 |
| Each phase has a phase-specific question ending with `?` | C-09 | Generic "Are we done?" | Zone-specific question anchored to zone commitment decision |

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
[ ] C-01: YAML valid; program: top-level key; stages: list present
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
[ ] C-25: gate contrast pairs carry Why: explanation at each FAIL example
[ ] C-26: each gate_fail: field carries inline # WRONG C-04 criterion-reference tag
[ ] C-27: all dependency reminders use identical syntactic form across zones and positions
[ ] C-28: production gate: field present as sibling alongside gate_fail:/gate_pass: fields
[ ] C-29: correction table contains wrong-to-correct pairs for C-05, C-06, AND C-07
[ ] C-30: dep reminder AND correction bridge independently coexist at skills: lines
[ ] C-31: BAD PLAN block carries # WRONG C-XX tags for all 7 criteria (C-01 through C-07)
[ ] C-32: production gate: field carries # check correction table: gate values bridge
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed, not authored
[ ] C-34: gate_fail: carries BOTH # WRONG C-04 AND Why: at the field (compound annotation)
[ ] C-35: BAD PLAN (C-31) AND correction table (C-29) both independently cover C-05/C-06/C-07
[ ] C-36: BAD PLAN header does not falsely restrict claimed coverage to essential-only
[ ] C-37: every wrong-format name: in BAD PLAN carries # WRONG C-06 at the name: field itself
[ ] C-38: BAD PLAN header affirmatively claims full-criterion coverage (all 7 / C-01 through C-07)
[ ] C-39: every invalid skills: entry in BAD PLAN carries # WRONG C-03 at the skills-field line
[ ] C-40: C-34 AND C-29 both pass independently
[ ] C-41: BAD PLAN header maps >= 3 of 4 annotation types to criterion numbers
         (C-26: gate_fail: / C-37: name: / C-39: skills: / C-38: header)
[ ] C-42: named section before BAD PLAN declares co-location family as structured table
         mapping all 3 field types (gate_fail: / name: / skills:) to criterion and tag
[ ] C-43: YAML template pre-populates strategy: with non-empty placeholder string
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
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage | C-05 |
| `flow:lifecycle` before any `review:*` stage | `review:*` in prior stage | C-05 |
| `listen:*` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and proceed"` | `strategy:` field framing plan as signal artifact | C-07 |
| `program:` key missing (top-level is `stages:`) | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line -- not at an adjacent field, not in a header comment.

| Field type | Criterion | Required annotation |
|------------|-----------|---------------------|
| `gate_fail:` value | C-04 (execution-state gate) | `# WRONG C-04: Why: ...` |
| `name:` value | C-06 (namespace-label stage name) | `# WRONG C-06` |
| `skills:` entry | C-03 (invented skill name) | `# WRONG C-03` |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
### Annotation-type index (C-41):
### C-26: gate_fail: field -- inline # WRONG C-04 at structural gate line
### C-37: name: field -- inline # WRONG C-06 at stage-name line
### C-39: skills: entry -- inline # WRONG C-03 at skills-list line
### C-38: this header -- affirmative full-criterion coverage claim

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
# Annotation-type index:
#   C-26: gate_fail: field carries # WRONG C-04 (structural gate zone co-location)
#   C-37: name: field carries # WRONG C-06 (stage-name zone co-location)
#   C-39: skills: entries carry # WRONG C-03 (skills-list zone co-location)
#   C-38: this header -- affirmative full-criterion coverage claim

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements          # WRONG C-03: invented skill name, not in Signal catalog
      - make-a-plan                  # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "done"                # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review           # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "complete"            # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing paragraph
```

---

## V-02 -- C-42 Named Co-Location Family Section Axis

**Axis**: Single-axis variation on C-42. A "FIELD CO-LOCATION PRINCIPLE" section with a full
4-column structured table appears before the BAD PLAN block as a named architectural principle,
presenting all three field-level co-location criteria (C-26/gate_fail:, C-37/name:, C-39/skills:)
as a unified family with: field type, criterion addressed, required annotation tag, and co-location
rule. The section converts three independent criteria into a single generalizable principle with
a named document home. C-41 (header index) and C-43 (strategy: pre-populated) also present.
Register: formal/structured with named principles and tables.

**Hypothesis**: Naming the three-field co-location principle as a dedicated document section
(rather than letting each criterion teach it implicitly) makes the BAD PLAN annotations feel
like instances of a pattern, not three unrelated requirements. A model reading the table before
the BAD PLAN block arrives already primed with the rule: any YAML field carrying a criterion-
testable value gets an inline criterion tag at that field line. When it encounters `gather-
requirements` in the skills list, it applies the pattern immediately. Anticipated score: 270/270.

**C-41 form**: BAD PLAN header enumerates all 4 annotation types; header is minimal (no expanded
commentary beyond the index list).
**C-42 form**: Dedicated "FIELD CO-LOCATION PRINCIPLE" section with 4-column table before BAD PLAN.
**C-43 form**: `strategy: "..."` non-empty placeholder in YAML template scaffold.

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
investigative intent is absent.

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

#### Step 5b -- FORWARD REFERENCE Audit

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
authoritative source for all per-stage annotations.** Copy YAML fragments directly from the
matrix; do not author annotations outside it.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema:

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
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
[ ] C-01 through C-40: same checklist as V-01 above
[ ] C-41: BAD PLAN header maps >= 3 of 4 annotation types to criterion numbers
[ ] C-42: named FIELD CO-LOCATION PRINCIPLE section with 4-column table present before BAD PLAN
[ ] C-43: YAML template strategy: field carries non-empty placeholder string
```

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

## FIELD CO-LOCATION PRINCIPLE

Every YAML field carrying a criterion-testable value requires an inline criterion tag co-located
at that exact field position. Co-location means: the tag appears on the same line as the violating
field value, not at an adjacent gate field, not in a block header comment, and not only in the
correction table. Three field types in program.yaml carry criterion-testable values; all three
have co-location requirements:

| Field type | Criterion addressed | Required annotation tag | Co-location rule |
|------------|---------------------|------------------------|------------------|
| `gate_fail:` value | C-04 (execution-state gate violation) | `# WRONG C-04: Why: <reason>` | At every `gate_fail:` field in template zones AND in BAD PLAN block |
| `name:` value | C-06 (namespace-label, not intent-describing) | `# WRONG C-06` | At every wrong-format `name:` value in BAD PLAN block |
| `skills:` entry | C-03 (invented or unrecognized skill name) | `# WRONG C-03` | At every invalid skills-list entry in BAD PLAN block |

A BAD PLAN block where C-03 violations are tagged at the gate or name field but not at the
skills-list entry satisfies C-31 (tag exists somewhere in the block) but fails C-39 (tag absent
at the exact field). The same logic applies identically to C-04 (at gate_fail:) and C-06 (at
name:). All three field types must be complete.

The principle generalizes: any future field type added to program.yaml that carries a criterion-
testable value follows the same co-location rule by structural analogy.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
# Annotation-type index (C-41): C-26 gate_fail: | C-37 name: | C-39 skills: | C-38 header

stages:                                  # WRONG C-01: missing program: top-level key
  - name: scout_and_draft                # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements              # WRONG C-03: invented skill, not in Signal catalog
      - make-a-plan                      # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "done"                    # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review               # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                     # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "complete"                # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- no strategy: field or framing element
```

---

## V-03 -- C-43 Scaffold-Enforced Strategy Field Axis

**Axis**: Single-axis variation on C-43. Step 8 foregrounds the `strategy:` pre-population
with an explicit structural enforcement note that analogizes it to echo pre-positioning:
just as echo is placed at the template end to enforce C-02 structurally, `strategy:` is
placed at the template top to enforce C-07 structurally. A model filling the template cannot
omit plan identity without actively deleting the pre-populated field. C-41 (header index) and
C-42 (named co-location section) also present. Register: discovery/analogy, foregrounding
the structural enforcement reasoning.

**Hypothesis**: Naming the `strategy:` pre-population as an analogy to echo structural
enforcement makes C-43 feel like the logical completion of a pattern the model already
understands (C-11/C-02). A model that grasps "echo is pre-positioned to enforce its contract
structurally" immediately understands why `strategy:` is pre-populated for the same reason.
The analogy converts C-43 from an isolated requirement into a named principle with a precedent.
Anticipated score: 270/270.

**C-41 form**: BAD PLAN header enumerates all 4 annotation types with criterion numbers.
**C-42 form**: 3-column FIELD CO-LOCATION PRINCIPLE table before BAD PLAN.
**C-43 form**: `strategy: "..."` in template with STRUCTURAL ENFORCEMENT NOTE in Step 8.

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
skills into stages, labeling stages after their clusters. Zone membership is never declared;
gates become prose; phases answer "what skills ran" not "what did we need to learn."

Three classes of information must remain knowable at every stage boundary:

| Class | What you must keep knowable | Criterion ladder |
|-------|----------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- committed before you open the catalog | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- not "what skills ran" but "what did we need to learn" | Question-framing ladder |

**Lifecycle zones:**
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
`{namespace}:{skill}` traces to the catalog skill. All three required.

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

What is the topic? State it now.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed.** Opening the catalog before phase declaration infects the
arc with skill availability bias.

Declare 3--6 phase boundaries from first principles. Assign each to a zone. Phase names encode
investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
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
design contract encoding derivation direction. Row 0 is where derivation begins, not where
execution ends. Omission of # Band: from echo is normative: echo is the derivation anchor,
not a band member.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

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
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:{skill} artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:{skill} artifact exists"  # check correction table: gate values
```

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

Verify each stage's gate references only artifacts producible by skills in that stage. Fix all
forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess the compliance landscape"` -- not interrogative, intent unknowable

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

Echo is the terminal consumer. Row 0 is where derivation begins. **ARTIFACT 2 is the sole
authoritative source for all per-stage annotations.** Copy YAML fragments directly from the
matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

**STRUCTURAL ENFORCEMENT NOTE (C-43 / C-07):**
The YAML template pre-populates `strategy:` with a non-empty placeholder string. This is the
same structural enforcement pattern used for echo: echo is pre-positioned at the template end
to make C-02 compliance the path of least resistance (a model filling the template encounters
the correctly-formed echo slot and must actively deviate to break it). `strategy:` is pre-
populated for exactly the same reason applied to C-07: a model filling the template encounters
the plan-identity field and must actively delete it to omit plan framing. Structural enforcement
converts both requirements from prose-attention-dependent to scaffold-default.

Required YAML schema:

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
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
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
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
[ ] C-01 through C-40: full checklist (same as V-01)
[ ] C-41: BAD PLAN header maps >= 3 of 4 annotation types to criterion numbers
[ ] C-42: named co-location section with structured table present before BAD PLAN
[ ] C-43: YAML template strategy: pre-populated with non-empty placeholder string (STRUCTURAL
         ENFORCEMENT NOTE in Step 8 names the echo analogy)
```

---

## CORRECTION TABLE

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all tasks finished"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- make-a-plan` | `- program:plan` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage | C-05 |
| `flow:lifecycle` before any `review:*` stage | `review:*` in prior stage | C-05 |
| `listen:*` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and proceed"` | `strategy:` field framing plan as signal artifact | C-07 |
| `program:` key missing | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE

| Field type | Criterion | Required annotation |
|------------|-----------|---------------------|
| `gate_fail:` value | C-04 (execution-state gate) | `# WRONG C-04: Why: ...` at field line |
| `name:` value | C-06 (namespace-label stage name) | `# WRONG C-06` at field line |
| `skills:` entry | C-03 (invented skill name) | `# WRONG C-03` at entry line |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
# Annotation-type index (C-41):
#   C-26: gate_fail: field carries # WRONG C-04 (structural gate zone co-location)
#   C-37: name: field carries # WRONG C-06 (stage-name zone co-location)
#   C-39: skills: entries carry # WRONG C-03 (skills-list zone co-location)
#   C-38: this header -- affirmative full-criterion coverage claim

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements          # WRONG C-03: invented skill name, not in Signal catalog
      - make-a-plan                  # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "done"                # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review           # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: invented skill name, not in Signal catalog
    gate_fail: "complete"            # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- strategy: absent; plan not framed as signal artifact
```

---

## V-04 -- C-41 + C-42 Combined Header-Section Cross-Reference Axis

**Axis**: Combined variation on C-41 + C-42. The BAD PLAN header index (C-41) and the named
co-location family section (C-42) are explicitly cross-referenced: the header says "see FIELD
CO-LOCATION PRINCIPLE section for family rationale"; the section says "the header above claims
complete coverage of these three annotation types." The design intent: each mechanism validates
the other, so a model reading either encounters a pointer to the other. A model reading the
header first is directed to the section for depth; a model reading the section first is
reminded that the header claims completeness of the family. C-43 (strategy: pre-populated)
also present. Register: analytical/reference, tight coupling emphasized.

**Hypothesis**: Cross-referencing C-41 (header) and C-42 (named section) creates bidirectional
coupling that prevents either from being read in isolation. A model encountering the header
knows there is a named principle section that elaborates the family; a model encountering the
section knows the header claims coverage of all three field types. The coupling makes both
mechanisms mutually reinforcing rather than independently optional. Anticipated score: 270/270.

**C-41 form**: BAD PLAN header includes 4 annotation-type mappings + "see FIELD CO-LOCATION
PRINCIPLE section."
**C-42 form**: "FIELD CO-LOCATION PRINCIPLE" section with 4-column table includes "the header
above claims full coverage of these types."
**C-43 form**: `strategy: "..."` non-empty placeholder in YAML template.

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

**Lifecycle zones:** **Breadth** -- scout and draft skills. **Depth** -- prove, review, flow,
trace skills. **Synthesis** -- listen, metrics, goals skills.

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. Failure mode to prevent:
**catalog-first construction**.

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
6. Write per-phase intent questions: interrogative form (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed.** Declare 3--6 phase boundaries from first principles.

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: for each stage is determined by what the next stage declares
as # Consumes: -- not by the prior stage's skill output inventory. Equivalently: this stage
produces the artifacts that close the next stage's input gap. The derivation runs backward
from echo; annotations are transcribed from the backward derivation, not authored from skill
knowledge.

ROW-0 RULE: Echo's row-0 position in ARTIFACT 2 is not an arbitrary convention -- it is a
design contract encoding derivation direction. Row 0 is where derivation begins, not where
execution ends. Omission of # Band: from echo is normative: echo is the derivation anchor.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard unmatched skills.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure to enforce compliance at authoring time:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone header -- dep zones only]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: placeholder]
skills:
  - <namespace>:<skill>    # check correction table: skill names
gate_fail: "<execution-state>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

Verify each stage's gate references artifacts producible by its own skills. Fix all forward
references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess compliance landscape"` -- intent unknowable

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

Produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column** before writing YAML.

Echo row-0: derivation anchor. **ARTIFACT 2 is the sole authoritative source** for per-stage
annotations. Copy YAML fragments directly from the matrix; do not author annotations outside it.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema:

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
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
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
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
[ ] C-01 through C-40: full checklist (same as V-01)
[ ] C-41: BAD PLAN header maps >= 3 of 4 annotation types + cross-reference to named section
[ ] C-42: FIELD CO-LOCATION PRINCIPLE section with 4-column table + cross-reference to header
[ ] C-43: YAML template strategy: carries non-empty placeholder string
```

---

## CORRECTION TABLE

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all tasks finished"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- make-a-plan` | `- program:plan` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage | C-05 |
| `flow:lifecycle` before any `review:*` stage | `review:*` in prior stage | C-05 |
| `listen:*` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and advance"` | `strategy:` framing plan as signal artifact | C-07 |
| `program:` key missing | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE
### The header in the BAD PLAN section below claims full coverage of these three annotation types.

Every YAML field carrying a criterion-testable value requires an inline criterion tag co-located
at that exact field position. The three field types below form a structural family: the same
principle applies to each, and any future field type in program.yaml that carries a criterion-
testable value joins the family by analogy.

| Field type | Criterion addressed | Required annotation tag | Co-location rule |
|------------|---------------------|------------------------|------------------|
| `gate_fail:` value | C-04 (execution-state gate violation) | `# WRONG C-04: Why: <reason>` | At every `gate_fail:` field in template zones AND BAD PLAN block |
| `name:` value | C-06 (namespace-label, not intent-describing) | `# WRONG C-06` | At every wrong-format `name:` in BAD PLAN block |
| `skills:` entry | C-03 (invented or unrecognized skill name) | `# WRONG C-03` | At every invalid skills-list entry in BAD PLAN block |

Satisfying C-31 (tag somewhere in the block) is not sufficient: each criterion tag must appear
at the violating field's own line. A BAD PLAN with C-03 tagged at the gate field but not at
the skills entry satisfies C-31 but fails C-39. See the BAD PLAN header below -- it claims
full coverage of all three field types listed here.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
# Annotation-type index (C-41) -- see FIELD CO-LOCATION PRINCIPLE section above:
#   C-26: gate_fail: field carries # WRONG C-04 (structural gate zone co-location)
#   C-37: name: field carries # WRONG C-06 (stage-name zone co-location)
#   C-39: skills: entries carry # WRONG C-03 (skills-list zone co-location)
#   C-38: this header -- affirmative full-criterion coverage claim

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements          # WRONG C-03: invented skill, not in Signal catalog
      - make-a-plan                  # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "done"                # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review           # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "complete"            # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- strategy: absent
```

---

## V-05 -- Complete Three-Criteria Integration

**Axis**: Full integration of C-41 + C-42 + C-43. All three new criteria prominently integrated
as a unified structural enforcement philosophy operating at two levels: plan level (echo and
strategy: are both structurally pre-positioned, enforcing C-02 and C-07 by scaffold default)
and field level (gate_fail:, name:, and skills: entries each carry co-located criterion tags,
enforcing the family principle). The named section, the YAML template, and the BAD PLAN header
all reference each other as parts of a coherent structural design, not independent requirements.
Register: comprehensive reference, cross-referencing all levels.

**Hypothesis**: Framing all three new criteria as instances of a single "structural enforcement
principle at two levels" makes each feel motivated by the same architecture: the plan-level
mechanism (pre-positioned fields) and the field-level mechanism (co-located tags) are the
same idea applied at different granularities. A model that understands the general principle
can predict what compliance looks like without memorizing each criterion individually. Deepest
integration; anticipated score: 270/270.

**C-41 form**: BAD PLAN header enumerates all 4 annotation types; says "co-location family
complete -- see FIELD CO-LOCATION PRINCIPLE and STRUCTURAL ENFORCEMENT sections."
**C-42 form**: "FIELD CO-LOCATION PRINCIPLE" with full 4-column table, explicit criterion-number
columns, cross-references to template (C-43) and header (C-41).
**C-43 form**: `strategy:` pre-populated in template; STRUCTURAL ENFORCEMENT PRINCIPLE sidebar
in Step 8 names both echo and strategy: as scaffold-enforced, references C-42 family.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the
program is a plan, not an executor. The chain begins at the end: echo is the terminal consumer
whose implicit information needs seed the entire backward derivation that determines every
prior stage's Produces/Consumes pair. That is why echo is row 0 of the bilateral trace matrix.

**Structural enforcement principle (two levels):**

The prompt enforces correctness at two granularities simultaneously:

| Level | Mechanism | Criterion(s) enforced |
|-------|-----------|----------------------|
| Plan level | Pre-positioned scaffold fields: `echo` at template end, `strategy:` at template top | C-02 (echo contract), C-07 (plan identity) |
| Field level | Co-located criterion tags at violating field lines in BAD PLAN | C-04 at `gate_fail:`, C-06 at `name:`, C-03 at `skills:` entries |

Both levels operate by making the correct form the scaffold default. Deletion requires active
deviation; compliance is the path of least resistance.

The failure mode to prevent: **catalog-first construction** -- opening the catalog, clustering
skills into stages, labeling stages after their clusters. Zone membership is never declared;
gates become prose; phases answer "what skills ran" not "what did we need to learn."

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- "what we needed to learn," not "what skills ran" | Question-framing ladder |

**Lifecycle zones:** **Breadth** -- scout and draft skills, problem-space commitment decision.
**Depth** -- prove, review, flow, trace skills, adversarial stress-test before shipping.
**Synthesis** -- listen, metrics, goals skills, post-launch signal monitoring.

**Compound gate template:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. All three components required.

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
6. Write per-phase intent questions: interrogative form (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed.** Declare 3--6 phase boundaries from first principles.

Phase names encode investigative purpose:
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
design contract encoding derivation direction. Row 0 is where derivation begins, not where
execution ends. Moving echo to any other row would misrepresent the derivation direction.
Omission of # Band: from echo is normative: echo is the derivation anchor, not a band member.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

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
gate_fail: "<execution-state>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Pass/fail reference:
- PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
- FAIL (no prefix, no threshold): `adequate discovery signals present`
- FAIL (threshold only, no stage-id): `>= 3 scout artifacts present`
- FAIL (stage-id mismatch): `breadth::scout-feasibility >= 2` when stage `name: discovery`

At least one gate across all non-echo stages must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS: `"Does the spec survive expert review against the discovered market signal?"`
- PASS: `"Are users adopting the feature at the rate our model predicted?"`
- FAIL: `"Assess the compliance landscape"` -- not interrogative, intent unknowable
- FAIL: `"Are we ready to proceed?"` -- not zone-specific

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

Echo is the terminal consumer; row 0 is where derivation begins. **ARTIFACT 2 is the sole
authoritative source for all per-stage annotations.** The YAML fragment column is the
authoritative form of the YAML annotation -- copy it directly. YAML annotations are transcribed
from ARTIFACT 2 matrix cells, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|---------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

**STRUCTURAL ENFORCEMENT PRINCIPLE -- Plan Level (C-43 / C-07 / C-02 / C-11):**
Two fields are structurally pre-populated in the YAML template:
- `echo` at the template END -- enforces C-02 (echo contract) by scaffold default. A model
  filling the template encounters the correctly-formed echo slot and must actively deviate to
  break it. This is C-11 structural enforcement for C-02.
- `strategy:` at the template TOP -- enforces C-07 (plan identity) by the same mechanism. A
  model filling the template encounters the plan-identity field and must actively delete it to
  omit framing. This is C-43 structural enforcement for C-07.
Both follow the same principle: pre-populate the required element so compliance is default,
not model-attention-dependent. See FIELD CO-LOCATION PRINCIPLE section for the field-level
equivalent of this structural enforcement philosophy.

Required YAML schema:

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
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
| Phases declared by zone in Step 2, catalog closed | C-13 | Phase names echo namespace groups | Phase map locked in Step 2; catalog not opened until Step 3 |
| Each phase has a phase-specific question ending with `?` | C-09 | Generic "Are we done?" | Zone-specific question anchored to zone commitment decision |

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
[ ] C-01: YAML valid; program: top-level key; stages: list present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate (artifact-verifiable)
[ ] C-05: namespace ordering respected: scout/draft -> review/prove -> flow/trace -> listen -> metrics/goals
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact (strategy: field present by default)
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
[ ] C-25: gate contrast pairs carry Why: explanation at each FAIL example
[ ] C-26: each gate_fail: field carries inline # WRONG C-04 criterion-reference tag
[ ] C-27: all dependency reminders use identical syntactic form across zones and positions
[ ] C-28: production gate: field present as sibling alongside gate_fail:/gate_pass: fields
[ ] C-29: correction table contains wrong-to-correct pairs for C-05, C-06, AND C-07
[ ] C-30: dep reminder AND correction bridge independently coexist at skills: lines
[ ] C-31: BAD PLAN block carries # WRONG C-XX tags for all 7 criteria (C-01 through C-07)
[ ] C-32: production gate: field carries # check correction table: gate values bridge
[ ] C-33: ARTIFACT 2 declared as sole authoritative source; YAML transcribed, not authored
[ ] C-34: gate_fail: carries BOTH # WRONG C-04 AND Why: at the field (compound annotation)
[ ] C-35: BAD PLAN (C-31) AND correction table (C-29) both independently cover C-05/C-06/C-07
[ ] C-36: BAD PLAN header does not falsely restrict claimed coverage to essential-only
[ ] C-37: every wrong-format name: in BAD PLAN carries # WRONG C-06 at the name: field itself
[ ] C-38: BAD PLAN header affirmatively claims full-criterion coverage (all 7 / C-01 through C-07)
[ ] C-39: every invalid skills: entry in BAD PLAN carries # WRONG C-03 at the skills-field line
[ ] C-40: C-34 AND C-29 both pass independently
[ ] C-41: BAD PLAN header maps >= 3 of 4 annotation types to criterion numbers; cross-references
         FIELD CO-LOCATION PRINCIPLE section
[ ] C-42: FIELD CO-LOCATION PRINCIPLE section with 4-column table (field / criterion / tag /
         rule) presents all 3 co-location criteria as named family before BAD PLAN block;
         cross-references both template (strategy:/echo) and BAD PLAN header
[ ] C-43: YAML template strategy: carries non-empty placeholder string; STRUCTURAL ENFORCEMENT
         PRINCIPLE names the echo analogy (C-02 :: strategy: maps to C-07)
```

---

## CORRECTION TABLE

Consult before authoring any field.

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all tasks finished"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- make-a-plan` | `- program:plan` | C-03 |
| `- run-design-review` | `- review:design` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `name: listen_phase` | `name: signal-watch` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage | C-05 |
| `flow:lifecycle` before any `review:*` stage | `review:*` in prior stage | C-05 |
| `listen:*` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and advance"` | `strategy:` field framing plan as signal artifact | C-07 |
| `program:` key missing (top-level is `stages:`) | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE
### All three co-location criteria (C-26 / C-37 / C-39) form a named structural family.
### See also: STRUCTURAL ENFORCEMENT PRINCIPLE in Step 8 (plan-level analogue).
### The BAD PLAN header below claims full coverage of all three field types listed here.

Every YAML field carrying a criterion-testable value requires an inline criterion tag co-located
at that exact field position. The three field types below form a structural family: any future
field type added to program.yaml that carries a criterion-testable value joins this family by
structural analogy. Co-location means the tag appears on the same line as the violating field
value -- not at an adjacent gate, not in a block header, not only in the correction table.

| Field type | Criterion | Required annotation | Co-location rule |
|------------|-----------|---------------------|-----------------|
| `gate_fail:` value | C-04 / C-26 (execution-state gate) | `# WRONG C-04: Why: <reason>` | At every `gate_fail:` field in template zones AND in BAD PLAN block |
| `name:` value | C-06 / C-37 (namespace-label stage name) | `# WRONG C-06` | At every wrong-format `name:` value in BAD PLAN block |
| `skills:` entry | C-03 / C-39 (invented or invalid skill name) | `# WRONG C-03` | At every invalid skills-list entry in BAD PLAN block |

The plan-level analogue to this field-level family is the STRUCTURAL ENFORCEMENT PRINCIPLE
in Step 8: `echo` (C-02) and `strategy:` (C-07) are pre-positioned scaffold fields enforcing
plan-level requirements. Both levels implement the same principle: make correct form the
scaffold default; require active deviation to produce a violation.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
# Annotation-type index (C-41) -- co-location family complete (see FIELD CO-LOCATION PRINCIPLE):
#   C-26 / gate_fail: field carries # WRONG C-04 (structural gate zone co-location)
#   C-37 / name:      field carries # WRONG C-06 (stage-name zone co-location)
#   C-39 / skills:    entries carry # WRONG C-03 (skills-list zone co-location)
#   C-38 / this header -- affirmative full-criterion coverage claim

stages:                                  # WRONG C-01: missing top-level program: key
  - name: scout_and_draft                # WRONG C-06: namespace-label, not investigative purpose
    skills:
      - gather-requirements              # WRONG C-03: invented skill, not in Signal catalog
      - make-a-plan                      # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "done"                    # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review               # WRONG C-06: namespace-label, not investigative purpose
    # WRONG C-05: review:design placed before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                     # WRONG C-03: invented skill, not in Signal catalog
    gate_fail: "complete"                # WRONG C-04: Why: execution-history, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: echo missing auto: true; skills: list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: no plan identity -- strategy: absent; plan framed as executor, not signal artifact

# Co-location family verified (C-41 index above):
# gate_fail: lines carry # WRONG C-04 at field (C-26)
# name: lines carry # WRONG C-06 at field (C-37)
# skills: lines carry # WRONG C-03 at entry (C-39)
```
