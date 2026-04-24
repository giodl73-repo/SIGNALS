---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 14
rubric: v14
rubric_date: 2026-03-16
total_pts: 285
golden_threshold: 80
new_criteria: C-44, C-45, C-46
---

# program-plan -- R14 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v14 (C-01 through C-46, 285 pts, golden: all essential pass AND composite >= 80).

**R13-2026-03-16 state under v14 rubric (C-44/C-45/C-46 added):**
- V-01, V-02: fail C-44, C-45, C-46 → 255/285
- V-03: passes C-44, fails C-45, C-46 → 260/285
- V-04: fails C-44, passes C-45, fails C-46 → 260/285
- V-05: fails C-44, passes C-45, passes C-46 → 265/285

**New rubric scoring delta:**
- 270 → 285 total pts (39 aspirational criteria; +15 from C-44/C-45/C-46 at 5 pts each)
- Golden threshold: unchanged (all essential pass AND composite >= 80)

**R14 design constraint (2026-03-16):** All five variations must satisfy C-44, C-45, and C-46
on top of the full C-01 through C-43 coverage demonstrated in R13-2026-03-16 variates.

**Canonical C-44 form (exact tag strings in C-41 index entries):**
- Every C-41 index entry must state: field type + criterion number + exact `# WRONG C-XX` string
- PASS: `# C-26: gate_fail: field carries # WRONG C-04`
- PASS: `# C-37: name: field carries # WRONG C-06`
- PASS: `# C-39: skills: entries carry # WRONG C-03`
- FAIL: `# C-26: gate_fail: field` (criterion number present, tag string absent)
- FAIL: `# gate_fail: carries annotation` (no criterion number, no tag string)
- Prerequisite: C-41

**Canonical C-45 form (bidirectional C-41/C-42 cross-reference):**
- C-42 section must include explicit forward reference to the BAD PLAN header below
- C-41 header index must include explicit back-reference to the C-42 section above
- PASS (C-42 direction): `The BAD PLAN header below indexes these three annotation types by criterion`
- PASS (C-41 direction): `# see FIELD CO-LOCATION PRINCIPLE section above`
- FAIL: one direction only -- C-41 references C-42 but C-42 does not reference BAD PLAN header
- FAIL: C-42 references "the block" without naming the header index specifically
- Prerequisites: C-41, C-42

**Canonical C-46 form (BAD PLAN block footer exit verification marker):**
- Must appear at the end of the BAD PLAN YAML block (inside the block)
- Must reference co-location completeness or the C-41 index by name
- PASS: `# Co-location family verified (C-41 index above)`
- PASS: `# Exit verification: all annotation types from C-41 index confirmed present`
- FAIL: `# end of BAD PLAN` (no co-location completeness reference)
- FAIL: closing comment outside the block rather than inside it
- Prerequisite: C-41

**Variation axes for R14:**
- V-01 (single): Phrasing Register -- compact table-first; C-44 as 3-column mini-table in the
  BAD PLAN header; C-45 as single-line cross-refs in each direction; C-46 as one-line footer;
  overall register compressed throughout
- V-02 (single): Structural Foreground -- "bounded teaching unit" framing elevated to opening;
  C-46 introduced alongside C-41 at the first description of the BAD PLAN; C-45 uses
  bounded-unit language; C-44 inline
- V-03 (single): Enumeration Format -- C-42 uses numbered list not table; C-41/C-44 index uses
  matching enumeration form; C-45 references "enumeration above/below"; C-46 references
  "enumeration rules confirmed"
- V-04 (combined): C-44 + C-45 co-designed -- each index entry embeds its own C-45 back-reference
  (`carries # WRONG C-04 -- rule in FIELD CO-LOCATION PRINCIPLE above`); C-46 present; C-42
  section carries per-entry forward pointers to BAD PLAN
- V-05 (full): BLOCK SPECIFICATION PROTOCOL -- C-41/C-44 as "spec header", C-42 as "protocol
  principle section", C-45 as "protocol navigation contract", C-46 as "protocol exit verification";
  all three presented as components of a unified block protocol

---

## V-01 -- Phrasing Register Axis (Compact Table-First)

**Axis**: Single-axis variation on phrasing register. All three new criteria (C-44, C-45, C-46)
are present but expressed in the most compressed form: C-44 as a 3-column table embedded in the
BAD PLAN header comment block, C-45 as single-line cross-references in both directions, C-46 as a
one-line footer comment. The overall prompt uses table-first, minimal-prose formatting throughout.

**Hypothesis**: Compressing C-44/C-45/C-46 to minimal form -- table in header, one-line cross-refs,
one-line footer -- reduces visual overhead without sacrificing the teaching value. A 3-column header
table (`field | criterion | tag`) delivers C-44's specification content more densely than prose
enumeration. Register compression tests whether all three new criteria survive format pressure while
maintaining full C-01 through C-43 compliance. Anticipated score: 285/285.

**C-44 form**: `| Field type | Criterion | Tag string |` 3-column table inside BAD PLAN header.
**C-45 form**: `(See FIELD CO-LOCATION PRINCIPLE above)` in header; `(See BAD PLAN header index below)` in C-42 footer.
**C-46 form**: `# Co-location family verified (C-41 index above)` one-line footer inside block.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation that determines every prior stage's Produces/Consumes pair. The chain
begins at echo; YAML is assembled from that anchor forward.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before declaring
arc phases, clustering skills into stages, labeling stages after their namespace groupings. The
result fails C-13 (arc is not the structural spine), C-09 (arc is namespace buckets, not evidence
phases), and C-06 (stage names repeat namespace labels).

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone (breadth / depth / synthesis) each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

**Compound gate format:**

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

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

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
as # Consumes: -- not by the prior stage's skill output inventory. The derivation runs backward
from echo; YAML annotations are transcribed from the backward derivation, not authored from
skill knowledge.

ROW-0 RULE: Echo's row-0 position in ARTIFACT 2 is a design contract encoding derivation
direction. Echo is the terminal consumer; the entire derivation chain begins from what echo
must receive and works backward. Row 0 is where derivation begins, not where execution ends.
Moving echo to any other row misrepresents the derivation direction. Omission of # Band: from
echo is normative: echo is the derivation anchor, not a band member.
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

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at zone header -- dep zones only]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: line -- dep zones only]
skills:                                # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Pass/fail reference:

| Form | Verdict | Reason |
|------|---------|--------|
| `discovery::scout-feasibility >= 3 AND scout:market artifact exists` | PASS | stage-id prefix, threshold, skill ref |
| `adequate discovery signals present` | FAIL C-04 | no prefix, no threshold, not artifact-verifiable |
| `>= 3 scout artifacts present` | FAIL C-04 | threshold only, no stage-id prefix |
| `breadth::scout-feasibility >= 2` when `name: discovery` | FAIL C-04 | stage-id mismatch |

At least one gate across all non-echo stages must include `>= N` in compound template format.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

FORWARD REFERENCE (fail):
```yaml
- name: discovery
  skills: [scout:feasibility, scout:requirements]
  gate: "discovery::trace-deployment >= 1 AND trace:deployment artifact confirmed"
  # trace:deployment not in this stage -- forward reference
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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** Copy the YAML
fragment column directly. YAML annotations are transcribed from ARTIFACT 2 matrix cells, not
authored independently. The matrix and YAML cannot diverge because YAML is defined as a downstream
rendering of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...`<br>`# Produces: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (transcribe YAML fragment column from ARTIFACT 2, then add fields):

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
    skills:                                # requires: <artifact> from Zone: <name> (C-05)  [dep zones]
                                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true
    skills: []  # REQUIRED: empty
```

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
[ ] C-42: named section before BAD PLAN declares co-location family as structured table/enumeration
[ ] C-43: YAML template strategy: field carries non-empty placeholder string
[ ] C-44: C-41 index entries name exact annotation tag strings (# WRONG C-XX) per entry
[ ] C-45: C-41 header index and C-42 section bidirectionally cross-reference each other
[ ] C-46: BAD PLAN block footer carries exit verification marker confirming co-location completeness
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

*(See BAD PLAN header index below for block-level instances of each annotation type.)*

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
#
# Annotation-type index (C-41 + C-44 -- exact tag strings per entry):
# | Field type       | Criterion | Exact tag string              |
# |------------------|-----------|-------------------------------|
# | gate_fail: field | C-26/C-04 | # WRONG C-04: Why: ...        |
# | name: field      | C-37/C-06 | # WRONG C-06                  |
# | skills: entry    | C-39/C-03 | # WRONG C-03                  |
# | this header      | C-38      | (affirmative coverage claim)  |
#
# (See FIELD CO-LOCATION PRINCIPLE section above for the family principle.)

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
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing element

# Co-location family verified (C-41 index above)
```

---

## V-02 -- Structural Foreground Axis (BAD PLAN as Bounded Teaching Unit)

**Axis**: Single-axis variation on structural foreground. The BAD PLAN block is introduced from
the opening as a "bounded teaching unit" -- a closed scan loop with an entry-point index (C-41)
and an exit-point verification marker (C-46) that bracket the block's body. C-46 is elevated to
the same structural status as C-41 rather than treated as an afterthought. C-45 bidirectional
links use "bounded unit" language. C-44 is expressed as inline header annotations.

**Hypothesis**: Naming the bounded structure explicitly at the conceptual level -- "this block has
an entry index and an exit marker that together bracket the co-location scan" -- makes C-46 feel
architecturally necessary rather than optional. A model reading the framing before encountering
the block knows it must produce both a header index and a footer marker. C-45 becomes the
connection between the principle section (C-42) and the bounded unit's entry index (C-41). C-44
flows naturally when the entry index is described as a "pre-scan specification." Anticipated
score: 285/285.

**C-44 form**: Inline header annotations: `# C-26: gate_fail: field carries # WRONG C-04`.
**C-45 form**: C-42 section references `the bounded BAD PLAN unit below and its header index`; C-41 header references `principle declaration in FIELD CO-LOCATION PRINCIPLE above`.
**C-46 form**: `# Exit marker (C-46): all annotation types from header index confirmed present in block above.`

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation that determines every prior stage's Produces/Consumes pair.

**The failure mode this protocol prevents:** catalog-first construction -- opening the catalog
before declaring arc phases, grouping skills into stages, labeling stages after their namespace
groupings. A catalog-first plan cannot be audited: zone membership is implied by namespace
grouping; gates are prose checks; investigative intent is absent.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- declared before the catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

**BAD PLAN as bounded teaching unit:** The BAD PLAN block at the end of this prompt is a closed
scan loop. It has two structural brackets:
- **Entry-point index (header)**: enumerates which annotation type appears at which field, naming
  the exact criterion and exact tag string for each. A model reads this before scanning the block
  and knows in advance what to look for (C-41 + C-44).
- **Exit-point marker (footer)**: confirms that all annotation types listed in the header were
  found present in the block body. The scan is closed when the footer is reached (C-46).

The FIELD CO-LOCATION PRINCIPLE section declares the family principle underlying the header index.
The BAD PLAN header implements that principle as a bounded entry specification.

**Compound gate format:**

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
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed.** Phase declaration must precede catalog access.

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

Phase names encode investigative purpose:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: is determined by what the next stage declares as # Consumes:
The derivation runs backward from echo; YAML annotations are transcribed from the backward
derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This is a design contract encoding derivation
direction. Row 0 is where derivation begins, not where execution ends. Omission of # Band: from
echo is normative: echo is the derivation anchor, not a band member.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**:
`Band ID | Namespaces | Zone | Gap class | Owner role` (MECE partition).

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure. Dep zones carry dual-position
reminders in uniform syntax:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at zone header -- dep zones]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: line -- dep zones]
skills:                                # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

PASS gate: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL gate: `"done"` -- Why: execution-history check, not verifiable by artifact inspection

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by skills in that
stage. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
FAIL: `"Assess compliance"` -- not interrogative, not zone-specific

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

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** Copy YAML fragment
column directly. YAML annotations are transcribed from ARTIFACT 2, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
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
  - name: <phase-label>                    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                                # requires: <artifact> from Zone: <name> (C-05)  [dep zones]
                                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
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
[ ] C-01 through C-43: same checklist items as V-01 above
[ ] C-44: C-41 index entries name exact annotation tag strings (# WRONG C-XX) per entry
[ ] C-45: C-41 header index and C-42 section bidirectionally cross-reference each other
[ ] C-46: BAD PLAN block footer carries exit verification marker confirming co-location completeness
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
| `"Execute all skills and advance"` | `strategy:` framing plan as signal-gathering artifact | C-07 |
| `program:` key missing | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. This principle governs three field types, presented here as a named family:

| Field type | Criterion | Required annotation | Co-location rule |
|------------|-----------|---------------------|------------------|
| `gate_fail:` value | C-04 | `# WRONG C-04: Why: ...` | At gate_fail: field line |
| `name:` value | C-06 | `# WRONG C-06` | At name: field line |
| `skills:` entry | C-03 | `# WRONG C-03` | At skills-list entry line |

The BAD PLAN block below is the bounded teaching unit implementing this principle. Its header
enumerates these annotation types as a pre-scan specification (C-41 + C-44); its footer confirms
all types were found present (C-46). See the BAD PLAN header index below for the full instance map.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07)
#
# BOUNDED TEACHING UNIT -- entry-point index below; exit-point marker at footer.
# Principle declaration: see FIELD CO-LOCATION PRINCIPLE section above.
#
# Annotation-type index (C-41 + C-44 -- exact tag strings):
#   C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#   C-37: name: field carries # WRONG C-06
#   C-39: skills: entries carry # WRONG C-03
#   C-38: this header -- affirmative full-criterion coverage claim (all 7 / C-01 through C-07)

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
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing element

# Exit marker (C-46): all annotation types from header index confirmed present in block above.
```

---

## V-03 -- Enumeration Format Axis (Numbered-List C-42 and C-41)

**Axis**: Single-axis variation on output format. The FIELD CO-LOCATION PRINCIPLE section (C-42)
uses a numbered list rather than a table to present the three field-type rules. The BAD PLAN
annotation-type index (C-41) uses matching enumeration form to parallel the principle section.
C-44 is expressed via enumeration entries that include the exact tag string. C-45 cross-references
use "enumeration above/below" language. C-46 references the enumeration rules.

**Hypothesis**: Numbered-list format for C-42 produces a more action-oriented, rule-checklist feel
compared to table format. A model reading a numbered list naturally treats each entry as a
checklist item to verify during generation. The C-41 index's matching enumeration form reinforces
the parallel between the principle section and its block-level implementation. C-44's tag-string
inclusion is natural in an enumeration: "(3) skills: entry → criterion C-03 → tag: # WRONG C-03".
Anticipated score: 285/285.

**C-44 form**: Enumeration entries: `(1) gate_fail: → C-04 (C-26) → tag at field: # WRONG C-04: Why: ...`.
**C-45 form**: C-42 enumeration footer: `Instance: the BAD PLAN header below enumerates these rules by annotation type`; C-41 header: `Principle: see FIELD CO-LOCATION PRINCIPLE enumeration above`.
**C-46 form**: `# All three co-location annotations from the enumeration above confirmed present in this block.`

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer whose implicit information needs seed
the entire backward derivation determining every prior stage's Produces/Consumes pair.

The failure mode this protocol prevents is **catalog-first construction**: opening the skill
catalog before declaring arc phases. When skills are grouped first, zone membership becomes
implicit, gates become prose checks, and investigative intent disappears from the artifact.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- declared before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

**Compound gate format:**

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
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed.** Declare 3--6 phase boundaries from first principles.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

Phase name examples:
- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: is set by what the next stage needs as # Consumes:, not by
skill output inventory. Derivation runs backward from echo.

ROW-0 RULE: Echo occupies row 0. This is a derivation-direction contract, not an arbitrary
convention. Row 0 = derivation start. # Band: omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

Use the three-field gate structure with dual-position dep reminders in uniform syntax:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at zone header]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: line]
skills:                                # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL: `"done"` -- execution-history check, not artifact-verifiable (Why: violates C-04)

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify gate artifacts are producible by skills in that stage.

---

#### Step 6 -- Phase Intent Questions

PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
FAIL: `"Assess compliance landscape"` -- not interrogative

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01` |

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
    skills:                                # requires: <artifact> from Zone: <name> (C-05)
                                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
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
[ ] C-01 through C-43: all criteria as listed in V-01 above
[ ] C-44: C-41 index entries name exact annotation tag strings per entry
[ ] C-45: C-41 header index and C-42 section bidirectionally cross-reference each other
[ ] C-46: BAD PLAN block footer carries exit verification marker confirming co-location completeness
```

---

## CORRECTION TABLE

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `gate: "all tasks finished"` | `gate: "signal-watch::listen-adoption >= 1 AND listen:support artifact present"` | C-04 |
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
| `"Execute all skills and advance"` | `strategy:` framing plan as signal-gathering artifact | C-07 |
| `program:` key missing | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. Three co-location rules, by field type:

1. `gate_fail:` field -- criterion C-04 (C-26) -- tag at field line: `# WRONG C-04: Why: <reason>`
2. `name:` field -- criterion C-06 (C-37) -- tag at field line: `# WRONG C-06`
3. `skills:` entry -- criterion C-03 (C-39) -- tag at entry line: `# WRONG C-03`

Rule: if the field value is wrong, the criterion tag (and for gates, a Why: explanation) must
appear at the field line itself. Tags in adjacent fields or header comments do not satisfy
co-location.

> Instance: the BAD PLAN header index below enumerates these three rules by annotation type,
> naming the exact criterion and tag string for each. (See BAD PLAN header below.)

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) covered in this block
#
# Annotation-type index by enumeration (C-41 + C-44 -- exact tag strings per entry):
#   (1) gate_fail: field → criterion C-04 (C-26) → tag at field: # WRONG C-04: Why: ...
#   (2) name: field → criterion C-06 (C-37) → tag at field: # WRONG C-06
#   (3) skills: entry → criterion C-03 (C-39) → tag at entry: # WRONG C-03
#   (4) this header → criterion C-38 → affirmative full-coverage claim
#
# Principle: see FIELD CO-LOCATION PRINCIPLE enumeration above (C-45).

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
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing element

# All three co-location annotations from the enumeration above confirmed present in this block.
```

---

## V-04 -- C-44 + C-45 Combined Axis (Per-Entry Cross-References)

**Axis**: Combined variation on C-44 and C-45. Each C-41 index entry embeds its own C-45
back-reference to the FIELD CO-LOCATION PRINCIPLE section (`rule declared in FIELD CO-LOCATION
PRINCIPLE above`), making every entry self-contained with: criterion number, exact tag string,
and a pointer to the rule that governs it. The C-42 section carries a per-row forward reference
to the BAD PLAN header. C-46 exit marker is present but minimal.

**Hypothesis**: Embedding the C-45 back-reference inside each C-41/C-44 index entry converts the
header from a standalone index into a series of navigational units -- each entry tells the model
what to look for (C-44) and where the governing rule lives (C-45 direction). This allows a model
that reads only the header, without scanning back to the C-42 section, to still be directed toward
the principle. The C-42 section's per-row forward references close the other direction: a model
reading the principle table is directed toward the BAD PLAN header for each specific entry.
Anticipated score: 285/285.

**C-44 form**: Each entry: `# C-26: gate_fail: carries # WRONG C-04: Why: ... (rule in FIELD CO-LOCATION PRINCIPLE above)`.
**C-45 form**: Each C-41 entry ends with `(rule in FIELD CO-LOCATION PRINCIPLE above)`; C-42 table has a "BAD PLAN header entry" column pointing forward.
**C-46 form**: `# Co-location family verified (C-41 index above)`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its information needs seed the backward
derivation that determines every prior stage's Produces/Consumes pair.

**Failure mode:** catalog-first construction -- skill clustering before zone declaration. Prevents
zone membership, artifact provenance, and investigative intent from being independently auditable.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding; scout and draft skills.
- **Depth** -- adversarial stress-test; prove, review, flow, trace skills.
- **Synthesis** -- post-launch monitoring; listen, metrics, goals skills.

**Compound gate format:**

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
5a. Design gates: compound lineage prefix, at least one quantified (Step 5a)
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

**Catalog must remain closed.** Declare 3--6 phases from first principles.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

PASS: `discovery`, `stress-test`, `signal-watch`
FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

  # Band:     [entry ID]
  # Gap:      [question, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s)]
  # Produces: [artifact type(s)]

Consumer-pull rule: # Produces: is set by what the NEXT stage needs.
Derivation runs backward from echo; YAML transcribed from backward derivation.

ROW-0 RULE: Echo is row 0. Derivation starts at row 0. # Band: omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

Three-field gate structure with uniform dual-position dep reminders:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone header]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [skills: line]
skills:                                # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

Verify gate artifacts are producible by stage skills. Fix before Step 6.

---

#### Step 6 -- Phase Intent Questions

PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
FAIL: `"Assess compliance"` -- not interrogative, not zone-specific

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01` |

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
    skills:                                # requires: <artifact> from Zone: <name> (C-05)
                                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
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
[ ] C-01 through C-43: as listed in V-01 above
[ ] C-44: C-41 index entries name exact annotation tag strings per entry
[ ] C-45: C-41 header index and C-42 section bidirectionally cross-reference each other
[ ] C-46: BAD PLAN block footer carries exit verification marker confirming co-location completeness
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. Three field types form the co-location family:

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN header entry |
|------------|-----------|-------------------------|------------------|----------------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: ...` | At gate_fail: line | See entry (1) in BAD PLAN header below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | See entry (2) in BAD PLAN header below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry | See entry (3) in BAD PLAN header below |

Each row above has a corresponding entry in the BAD PLAN header index (see below) that names the
exact tag string. The BAD PLAN header back-references this section for the governing rule.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below
#
# Annotation-type index (C-41 + C-44 -- field type, criterion, exact tag, rule reference):
#   C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#         (rule declared in FIELD CO-LOCATION PRINCIPLE above)
#   C-37: name: field carries # WRONG C-06
#         (rule declared in FIELD CO-LOCATION PRINCIPLE above)
#   C-39: skills: entries carry # WRONG C-03
#         (rule declared in FIELD CO-LOCATION PRINCIPLE above)
#   C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)

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
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing element

# Co-location family verified (C-41 index above)
```

---

## V-05 -- Full Integration Axis (BLOCK SPECIFICATION PROTOCOL)

**Axis**: Full three-criteria integration. C-41/C-44/C-45/C-46 are presented as components of a
named "BLOCK SPECIFICATION PROTOCOL" that replaces the standalone FIELD CO-LOCATION PRINCIPLE +
BAD PLAN header structure with an explicitly named three-component architecture: (1) the header
entry index as a "pre-scan specification" (C-41 + C-44), (2) the principle section as the
"governing declaration" (C-42 + C-45 direction 1), (3) the footer as the "exit verification"
(C-46 + C-45 direction 2 via protocol reference). The protocol is introduced before the
CONSTRUCTION ORDER, making it a first-class design element of the prompt rather than a structural
add-on after the steps.

**Hypothesis**: Naming the three-component structure as a unified protocol before any construction
steps causes a model to treat the BAD PLAN block as a bounded artifact to be constructed according
to the protocol, not as an appended illustration. A model that understands the protocol before it
sees the steps will, when it reaches the BAD PLAN block, expect a header specification (C-41/C-44),
a bounded body, and a footer verification (C-46). The C-45 bidirectional links become the
"protocol navigation contract" -- a model sees them as required structural connections between the
principle declaration and the header specification. This is the most comprehensive formulation,
maximizing teaching density at the cost of greatest prompt length. Anticipated score: 285/285.

**C-44 form**: `# C-26 → gate_fail: ← tag: # WRONG C-04: Why: ...` per entry in header specification.
**C-45 form**: Protocol section says `Component 1 (header) below; Component 2 (body); Component 3 (footer)`; C-41 header says `Component 1 of BLOCK SPECIFICATION PROTOCOL above`.
**C-46 form**: `# BLOCK SPECIFICATION PROTOCOL -- Component 3: exit verification complete. All annotation types from Component 1 confirmed present. (see BLOCK SPECIFICATION PROTOCOL above)`

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction. Opening the catalog before declaring arc
phases destroys zone membership, artifact provenance, and investigative intent simultaneously.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- declared before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## BLOCK SPECIFICATION PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.
Understanding the protocol before construction prevents incomplete BAD PLAN blocks.

**Component 1 -- Header Entry Specification (C-41 + C-44)**

The BAD PLAN header is a pre-scan specification: before a model reads a single field in the
block body, it knows from the header what annotation type to expect at each field type, what
criterion governs it, and what exact tag string to look for. Each header entry has the form:

```
# C-XX: <field type> carries <exact tag string>
```

Example complete header entries:
- `# C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable`
- `# C-37: name: field carries # WRONG C-06`
- `# C-39: skills: entries carry # WRONG C-03`
- `# C-38: this header -- affirmative coverage claim (all 7 criteria / C-01 through C-07)`

**Component 2 -- Block Body with Field-Level Annotations (C-26, C-37, C-39)**

The block body contains wrong YAML with criterion tags at each violating field line. Three
co-location rules:

| Field type | Criterion | Required annotation tag |
|------------|-----------|-------------------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: ...` |
| `name:` | C-06 (C-37) | `# WRONG C-06` |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` |

**Component 3 -- Footer Exit Verification (C-46)**

The BAD PLAN block ends with an explicit footer confirming that all annotation types from
Component 1 (the header specification) were found present in the block body. This closes the
bounded scan loop.

**Protocol Navigation Contract (C-45):**

- This section (BLOCK SPECIFICATION PROTOCOL) is the principle declaration: see BAD PLAN block
  below for the bounded instance implementing this protocol.
- The BAD PLAN header below is Component 1 of this protocol: see BLOCK SPECIFICATION PROTOCOL
  above for the full protocol definition.

---

**Compound gate format:**

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
5a. Design gates: compound lineage prefix, at least one quantified (Step 5a)
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

**The catalog must remain closed.** Declare 3--6 phase boundaries from first principles.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [entry ID]
  # Gap:      [question, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s)]
  # Produces: [artifact type(s)]

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:
Derivation runs backward from echo. YAML transcribed from backward derivation, not authored
from skill knowledge.

ROW-0 RULE: Echo is row 0. This is derivation-direction encoding, not convention. # Band:
omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

Three-field gate structure with uniform dual-position dep reminders:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [zone header]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [skills: line]
skills:                                # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

PASS gate: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL gate: `"done"` -- Why: execution-history check, not artifact-verifiable (C-04 violation)

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify gate artifacts producible by stage skills. Fix before Step 6.

---

#### Step 6 -- Phase Intent Questions

PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
FAIL: `"Assess the compliance landscape"` -- not interrogative

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** Transcribe YAML
from ARTIFACT 2; do not author annotations outside it.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
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
  - name: <phase-label>                    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                                # requires: <artifact> from Zone: <name> (C-05)
                                           # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
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
[ ] C-01: YAML valid; program: top-level; stages: list present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has evidence-state gate (artifact-verifiable)
[ ] C-05: namespace ordering respected
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08: at least one gate with quantified threshold (>= N)
[ ] C-09: deliberate evidence arc (breadth -> depth -> synthesis)
[ ] C-10: at least one essential-criterion BAD/GOOD contrast pair
[ ] C-11: at least one essential requirement enforced structurally
[ ] C-12: all four essential criteria have >= 2 independent anchors
[ ] C-13: arc phases are the primary structural division
[ ] C-14: echo and structural slots carry deletion-resistance annotations
[ ] C-15: plan-level BAD YAML block present
[ ] C-16: at least one error example carries criterion tag
[ ] C-17: every arc zone carries inline PASS/FAIL gate example
[ ] C-18: correction table with >= 3 wrong-to-correct pairs
[ ] C-19: error artifacts cover both essential AND recommended criteria
[ ] C-20: every dep-bearing zone has inline prerequisite at skills: line
[ ] C-21: YAML template fields carry # check correction table bridges
[ ] C-22: error artifacts cover ALL THREE recommended criteria
[ ] C-23: dep reminders at BOTH zone-header AND skills: positions
[ ] C-24: gate contrast as actual YAML fields (gate_fail:/gate_pass:)
[ ] C-25: gate contrast pairs carry Why: at each FAIL example
[ ] C-26: each gate_fail: carries inline # WRONG C-04
[ ] C-27: dep reminders use identical syntactic form across zones
[ ] C-28: production gate: field present alongside contrast fields
[ ] C-29: correction table has C-05, C-06, C-07 pairs
[ ] C-30: dep reminder AND correction bridge coexist at skills: lines
[ ] C-31: BAD PLAN carries # WRONG C-XX for all 7 criteria
[ ] C-32: production gate: field carries # check correction table bridge
[ ] C-33: ARTIFACT 2 declared sole authoritative source
[ ] C-34: gate_fail: carries BOTH # WRONG C-04 AND Why: at field
[ ] C-35: BAD PLAN (C-31) AND correction table (C-29) independently cover C-05/C-06/C-07
[ ] C-36: BAD PLAN header not falsely restricted to essential-only
[ ] C-37: wrong name: in BAD PLAN carries # WRONG C-06 at name: field
[ ] C-38: BAD PLAN header affirmatively claims full-criterion coverage
[ ] C-39: invalid skills: entries in BAD PLAN carry # WRONG C-03 at entry line
[ ] C-40: C-34 AND C-29 both pass independently
[ ] C-41: BAD PLAN header maps >= 3 of 4 annotation types to criterion numbers
[ ] C-42: named section before BAD PLAN declares co-location family as structured table
[ ] C-43: YAML template strategy: carries non-empty placeholder string
[ ] C-44: C-41 index entries name exact annotation tag strings (# WRONG C-XX) per entry
[ ] C-45: C-41 header index and C-42 section bidirectionally cross-reference each other
[ ] C-46: BAD PLAN block footer carries exit verification marker confirming co-location completeness
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

## BLOCK SPECIFICATION PROTOCOL -- Component 2 Declaration

*(This section is the governing declaration for Component 2 of the BAD PLAN block below.)*

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. Three field types form the co-location family:

| Field type | Criterion | Required annotation tag | Co-location rule |
|------------|-----------|-------------------------|------------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: ...` | At gate_fail: field line |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: field line |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line |

The BAD PLAN header below implements this family as Component 1 of the BLOCK SPECIFICATION
PROTOCOL (see BLOCK SPECIFICATION PROTOCOL section above for the full three-component definition).

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BAD PLAN -- all 7 criteria (C-01 through C-07)
#
# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Entry Specification (C-41 + C-44)
# See BLOCK SPECIFICATION PROTOCOL section above for full protocol definition. (C-45)
#
# Annotation-type index with exact tag strings:
#   C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#   C-37: name: field carries # WRONG C-06
#   C-39: skills: entries carry # WRONG C-03
#   C-38: this header -- affirmative full-criterion coverage claim (all 7 / C-01 through C-07)

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
    # WRONG C-07: no plan identity -- no strategy:, purpose:, or framing element

# BLOCK SPECIFICATION PROTOCOL -- Component 3: Exit Verification (C-46)
# All annotation types from Component 1 (header index above) confirmed present in block body.
# (see BLOCK SPECIFICATION PROTOCOL section above for protocol definition)
```
