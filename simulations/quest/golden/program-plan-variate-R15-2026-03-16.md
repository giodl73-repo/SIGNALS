---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 15
rubric: v15
rubric_date: 2026-03-16
total_pts: 300
golden_threshold: 80
new_criteria: C-47, C-48, C-49
---

# program-plan -- R15 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v15 (C-01 through C-49, 300 pts, golden: all essential pass AND composite >= 80).

**R14-2026-03-16 state under v15 rubric (C-47/C-48/C-49 added):**
- V-01, V-03: fail C-47 (Why: abbreviated), fail C-48, fail C-49 → 255/300
- V-02: passes C-47, fails C-48, fails C-49 → 260/300
- V-04: passes C-47, passes C-48, fails C-49 → 265/300
- V-05: passes C-47, fails C-48 (section-level only, not per-entry), passes C-49 → 265/300

**R15 design constraint:** All five variations must satisfy C-47, C-48, and C-49 on top of
the full C-01 through C-46 coverage demonstrated in R14-2026-03-16 variates.

**Canonical C-47 form (full unabbreviated Why: in C-41 index gate_fail: entry):**
- PASS: `# C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable`
- FAIL: `# C-26: gate_fail: field carries # WRONG C-04: Why: ...` (abbreviated placeholder)
- Prerequisite: C-44

**Canonical C-48 form (per-entry bidirectional C-41/C-42 navigation):**
- C-41 direction: each individual entry ends with its own back-ref e.g.
  `(rule declared in FIELD CO-LOCATION PRINCIPLE above)` or equivalent
- C-42 direction: each table row or list item carries a per-row forward-ref to the
  specific numbered entry in the BAD PLAN header e.g. `See entry (1) in BAD PLAN header below`
- FAIL: a single shared header-level pointer serving all C-41 entries (satisfies C-45 but not C-48)
- Prerequisite: C-45

**Canonical C-49 form (named multi-component block specification protocol):**
- C-42 named section IS the protocol declaration (title uses the protocol name)
- C-41 BAD PLAN header carries the protocol name as component label:
  e.g. `# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Entry Specification`
- C-46 footer carries the protocol name as component label:
  e.g. `# BLOCK SPECIFICATION PROTOCOL -- Component 3: Exit Verification (C-46)`
- All three components share the same protocol name
- Prerequisites: C-41, C-42, C-46

**Variation axes for R15:**
- V-01 (single): Phrasing Register -- compact table-first throughout; SCAN PROTOCOL as
  a compact two-row component table; C-41 index as 4-column table row entries (criterion |
  field | exact tag+full Why: | back-ref); C-48 fourth column per entry; C-49 "SCAN PROTOCOL"
- V-02 (single): Role Sequence -- BOUNDED BLOCK PROTOCOL section appears FIRST in the prompt,
  before the 3-class table and lifecycle zones; protocol framing establishes the BAD PLAN
  architecture before construction begins; normal prose register throughout
- V-03 (single): Enumeration Format -- BLOCK SCAN PROTOCOL section uses numbered list for
  components; C-42 uses numbered list not table; C-41 index uses matching numbered entries;
  C-48 uses "(rule #N above)" / "instance #N in header below" notation; C-49 labeling via
  enumeration-parallel "(P1)/(P2)/(P3)" component markers
- V-04 (combined): C-47 + C-48 co-designed -- full Why: text is embedded inside each per-entry
  back-reference phrase, fusing both criteria into a single annotation unit per entry; C-42 table
  has forward-ref column; BLOCK SPECIFICATION PROTOCOL; C-49 present
- V-05 (full): Extended Protocol -- BLOCK SPECIFICATION PROTOCOL formally specifies C-47 and C-48
  as sub-requirements within Component 1's definition; C-46 footer explicitly verifies both
  co-location completeness AND C-47 full Why: presence; highest-density formulation

---

## V-01 -- Phrasing Register Axis (Compact Protocol)

**Axis**: Single-axis variation on phrasing register. All three new criteria (C-47, C-48, C-49)
present in maximum-compressed form. The protocol section (C-49) is a 4-row component table rather
than prose. The C-41 annotation-type index uses a 4-column table: `criterion | field type | exact
tag string with full Why: | back-ref`. C-47 full Why: text appears as a table cell value (not
truncated). C-48 per-entry back-refs appear as the 4th column of each index row. C-49 protocol
named "SCAN PROTOCOL" with short component labels "C1" and "C3".

**Hypothesis**: Compressing C-47/C-48/C-49 to tabular forms reduces visual overhead without
sacrificing teaching content. A 4-column table for the C-41 index delivers criterion + field type
+ full tag string + per-entry back-ref simultaneously in a scannable format. C-47's full Why: text
is as present in a table cell as in a prose line. Register compression tests whether all three new
criteria survive format pressure while maintaining semantic completeness. Anticipated: 300/300.

**C-47 form**: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` as cell in
4-column index table -- full text, no abbreviation.
**C-48 form**: 4th column in C-41 table: `SCAN PROTOCOL decl. above`; C-42 table has `BAD PLAN
entry` column: `Entry (1) below`, `Entry (2) below`, `Entry (3) below`.
**C-49 form**: Section `## SCAN PROTOCOL`; BAD PLAN header: `# SCAN PROTOCOL -- C1: Header Index`;
footer: `# SCAN PROTOCOL -- C3: exit verified`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before
declaring arc phases. Result: zone membership is implicit; gates are prose checks; investigative
intent is absent from the artifact.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- declared before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## SCAN PROTOCOL

The BAD PLAN block is a bounded teaching unit with three components:

| Label | Criteria | Content |
|-------|----------|---------|
| **C1 -- Header Index** | C-41, C-44, C-47, C-48 | 4-column table: criterion / field type / exact tag+full Why: / back-ref to this section |
| **C2 -- Block Body** | C-26, C-37, C-39 | Wrong YAML with field-level criterion tags at every violating field line |
| **C3 -- Exit Verification** | C-46 | Footer confirming all C1 annotation types found present in block body |

Navigation contract (C-45 + C-48): this section (SCAN PROTOCOL) is the protocol declaration.
The BAD PLAN header below is C1. Each FIELD CO-LOCATION PRINCIPLE table row forward-references
its specific C1 entry number. Each C1 entry back-references this section.

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

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first
principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

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

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes: -- not
by the prior stage's skill output inventory. Derivation runs backward from echo; YAML annotations
are transcribed from the backward derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction. Row 0 is where
derivation begins, not where execution ends. # Band: omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure. Dependency zones carry dual-position
reminders in uniform syntax:

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

| Form | Verdict | Reason |
|------|---------|--------|
| `discovery::scout-feasibility >= 3 AND scout:market artifact exists` | PASS | stage-id prefix, threshold, skill ref |
| `adequate discovery signals present` | FAIL C-04 | no prefix, no threshold, not artifact-verifiable |
| `>= 3 scout artifacts present` | FAIL C-04 | threshold only, no stage-id prefix |
| `breadth::scout-feasibility >= 2` when `name: discovery` | FAIL C-04 | stage-id mismatch |

At least one gate across all non-echo stages must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS: `"Does the spec survive expert review against the discovered market signal?"`
- FAIL (not interrogative): `"Assess the compliance landscape"`
- FAIL (wrong scope): `"Are we ready to proceed?"`

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML annotations
are transcribed from ARTIFACT 2 matrix cells, not authored independently. The matrix and YAML
cannot diverge because YAML is a downstream rendering of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
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

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; program: top-level key; stages: list present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate (artifact-verifiable)
[ ] C-05: namespace ordering respected: scout/draft -> review/prove -> flow/trace -> listen
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
[ ] C-19: error artifacts cover both essential AND recommended criteria
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
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: rationale (not Why: ...)
[ ] C-48: per-entry bidirectional navigation: each C-41 entry has own back-ref to C-42; C-42 has per-row forward-ref to specific C-41 entry number
[ ] C-49: C-41/C-42/C-46 all labeled as components of SCAN PROTOCOL named entity
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
exact field line -- not at an adjacent field, not in a header comment. This is the SCAN PROTOCOL
co-location family (see SCAN PROTOCOL section above for the protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in BAD PLAN header below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in BAD PLAN header below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in BAD PLAN header below |

The BAD PLAN C1 header below implements this family as the SCAN PROTOCOL entry index.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in SCAN PROTOCOL C1 below

```yaml
# SCAN PROTOCOL -- C1: Header Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# | Criterion | Field type      | Exact tag string (full Why: per C-47)                                        | Back-ref (C-48)         |
# |-----------|-----------------|------------------------------------------------------------------------------|-------------------------|
# | C-26      | gate_fail:      | # WRONG C-04: Why: execution-history check, not artifact-verifiable          | SCAN PROTOCOL decl. above |
# | C-37      | name:           | # WRONG C-06                                                                 | SCAN PROTOCOL decl. above |
# | C-39      | skills: entry   | # WRONG C-03                                                                 | SCAN PROTOCOL decl. above |
# | C-38      | this header     | affirmative full-coverage claim (all 7 / C-01 through C-07)                 | SCAN PROTOCOL decl. above |

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

# SCAN PROTOCOL -- C3: exit verified. All C1 annotation types confirmed present in block above.
```

---

## V-02 -- Role Sequence Axis (Protocol First)

**Axis**: Single-axis variation on role sequence. The BOUNDED BLOCK PROTOCOL section appears
FIRST in the prompt -- before the three-class information table, before lifecycle zones, before
the catalog -- making the BAD PLAN block architecture the conceptual anchor from the opening.
A model reads the bounded-unit architecture before any construction guidance, and therefore
approaches the BAD PLAN block as a known protocol rather than an appended illustration. C-47
full Why: text in C-41 entries, C-48 per-entry navigation, and C-49 protocol naming are all
implemented in normal prose register throughout.

**Hypothesis**: Placing the protocol architecture at the front of the document causes a model
to frame all subsequent construction steps as leading toward a bounded artifact whose structure
is already specified. When the BAD PLAN block is encountered, the model has prior context for
why it has three components and what each must contain. C-47 and C-48 feel like mandatory
protocol sub-requirements rather than optional enrichments. Anticipated: 300/300.

**C-47 form**: `# C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check,
not artifact-verifiable` -- full text in prose-indented annotation index entries.
**C-48 form**: Each C-41 entry ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)`;
C-42 table has `BAD PLAN entry` column with `See entry (1/2/3) in BAD PLAN header below`.
**C-49 form**: Section `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL
-- Component 1: Header Entry Index`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3:
Exit Verification (C-46) complete`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit
with three components. Understanding the protocol before construction prevents incomplete blocks.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Before reading any field in the block body, the header
tells you: which field type carries which annotation, which criterion governs it, what the exact
tag string looks like (including the full unabbreviated `Why:` clause where one exists), and
where the governing rule is declared. Each entry has the form:

```
# C-XX: <field type> carries <exact tag string with full Why: if applicable>
#       (rule declared in BOUNDED BLOCK PROTOCOL above)
```

Example entries satisfying C-47 (full Why:) and C-48 (per-entry back-ref):
- `# C-26: gate_fail: carries # WRONG C-04: Why: execution-history check, not artifact-verifiable`
  `#       (rule declared in BOUNDED BLOCK PROTOCOL above)`
- `# C-37: name: carries # WRONG C-06`
  `#       (rule declared in BOUNDED BLOCK PROTOCOL above)`
- `# C-39: skills: entries carry # WRONG C-03`
  `#       (rule declared in BOUNDED BLOCK PROTOCOL above)`

**Component 2 -- Block Body with Field-Level Annotations (C-26, C-37, C-39)**

The block body contains wrong YAML. Every violating field carries its criterion tag at the exact
field line -- not at an adjacent field, not in a header comment. The FIELD CO-LOCATION PRINCIPLE
section (below, before the BAD PLAN block) declares this family principle.

**Component 3 -- Exit Verification (C-46)**

The block ends with an explicit footer confirming all annotation types from Component 1 were
found present. This closes the bounded scan loop.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration. See the BAD PLAN block
  below for the bounded instance implementing this protocol (Component 1 header below).
- The FIELD CO-LOCATION PRINCIPLE section below is the family principle declaration; its table
  carries per-row forward-refs to specific Component 1 entry numbers in the BAD PLAN header.

---

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before
declaring arc phases. Zone membership becomes implicit; gates become prose checks; investigative
intent disappears from the artifact.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- declared before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

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

**The catalog must remain closed at this step.**

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`,
or `synthesis`.

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

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:
Derivation runs backward from echo; YAML annotations are transcribed from the backward
derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction. Row 0 is
where derivation begins, not where execution ends. # Band: omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure with uniform dual-position dep reminders:

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

PASS gate: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL gate: `"done"` -- Why: execution-history check, not verifiable by artifact inspection

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify gate artifacts are producible by skills in that stage. Fix before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess compliance"` -- not interrogative, not zone-specific

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML annotations
are transcribed from ARTIFACT 2 matrix cells, not authored independently.

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
[ ] C-01 through C-46: all criteria as specified in V-01 above
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: rationale (not Why: ...)
[ ] C-48: per-entry bidirectional navigation (each C-41 entry has own back-ref; C-42 has per-row forward-refs)
[ ] C-49: C-41/C-42/C-46 labeled as components of BOUNDED BLOCK PROTOCOL named entity
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. Three field types form the co-location family (BOUNDED BLOCK PROTOCOL
Component 2 body rules; see BOUNDED BLOCK PROTOCOL section above for the full protocol):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | See entry (1) in BAD PLAN header below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | See entry (2) in BAD PLAN header below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry | See entry (3) in BAD PLAN header below |

Each row above maps to a specific Component 1 header entry below (see "BAD PLAN entry" column).

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BOUNDED BLOCK PROTOCOL -- Component 1: Header Entry Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered -- essential (C-01 through C-04) and recommended (C-05 through C-07)
#
# Annotation-type index (exact tag strings per entry; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in BOUNDED BLOCK PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in BOUNDED BLOCK PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in BOUNDED BLOCK PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in BOUNDED BLOCK PROTOCOL above)

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

# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification (C-46) complete.
# All annotation types from Component 1 header entry index confirmed present in block above.
```

---

## V-03 -- Enumeration Format Axis (Numbered-List Protocol)

**Axis**: Single-axis variation on output format. The BLOCK SCAN PROTOCOL section uses a
numbered list for its component specifications rather than a component table. The FIELD
CO-LOCATION PRINCIPLE section uses a numbered list (not a table) to present the three field
rules. The C-41 annotation-type index in the BAD PLAN header uses matching numbered-list entries.
C-48 per-entry back-refs use `(rule #N above)` notation referencing the numbered list. C-49
component labels use `(P1)`, `(P2)`, `(P3)` markers matching the numbered format. C-47 full
Why: text present in numbered list entry for the gate_fail: rule.

**Hypothesis**: Numbered-list format produces a stronger checklist orientation than tables. A
model reading numbered entries treats each as a verifiable item. C-41 entries numbered `(1)`,
`(2)`, `(3)` match the FIELD CO-LOCATION PRINCIPLE numbered items `(1)`, `(2)`, `(3)` exactly,
making the C-48 per-entry navigation explicit: each entry in the C-41 index corresponds to the
same-numbered item in the FIELD CO-LOCATION enumeration above. Anticipated: 300/300.

**C-47 form**: `(1) gate_fail: → C-04 (C-26) → tag: # WRONG C-04: Why: execution-history
check, not artifact-verifiable` -- full Why: text in the numbered entry.
**C-48 form**: Each C-41 entry ends with `(rule #N in BLOCK SCAN PROTOCOL above)`; C-42
enumeration items carry `instance #N in BAD PLAN header below`.
**C-49 form**: `## BLOCK SCAN PROTOCOL` with numbered components `(P1)`, `(P2)`, `(P3)`;
BAD PLAN header: `# BLOCK SCAN PROTOCOL (P1)`; footer: `# BLOCK SCAN PROTOCOL (P3): exit OK`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the catalog before declaring
arc phases. When skills are grouped first, zone membership becomes implicit, gates become prose
checks, and investigative intent disappears from the artifact.

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

---

## BLOCK SCAN PROTOCOL

The BAD PLAN block is a bounded teaching unit. Three components:

1. **(P1) Header Entry Index** (C-41 + C-44 + C-47 + C-48): Numbered annotation-type entries
   each stating field type, criterion, exact tag string with full `Why:` clause, and a back-ref
   to this protocol section. Covers all 7 criteria affirmatively.
2. **(P2) Block Body** (C-26, C-37, C-39): Wrong YAML with criterion tags at every violating
   field line -- gate_fail: for C-04, name: for C-06, skills: entries for C-03.
3. **(P3) Exit Verification** (C-46): Footer confirming all (P1) annotation types present.

Navigation contract (C-45 + C-48): this section (BLOCK SCAN PROTOCOL) is the protocol declaration.
The BAD PLAN block below is the bounded instance. The FIELD CO-LOCATION PRINCIPLE enumeration
below carries per-item instance references to the BAD PLAN header's (P1) entry numbers.
Each (P1) entry back-references this section as `(rule #N in BLOCK SCAN PROTOCOL above)`.

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

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:
Derivation runs backward from echo. # Band: omitted from echo is correct.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Row 0 = derivation start, not execution end.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

Three-field gate structure with uniform dual-position dep reminders:

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

PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL: `"done"` -- Why: execution-history check, not verifiable by artifact inspection

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

Verify gate artifacts are producible by skills in that stage. Fix before Step 6.

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
[ ] C-01 through C-46: all criteria as specified in V-01 above
[ ] C-47: C-41 index gate_fail: entry (1) includes full unabbreviated Why: rationale
[ ] C-48: each C-41 entry ends with (rule #N in BLOCK SCAN PROTOCOL above); C-42 items carry instance #N in BAD PLAN header below
[ ] C-49: C-41/C-42/C-46 labeled as (P1)/(P2)/(P3) components of BLOCK SCAN PROTOCOL
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. Three co-location rules (BLOCK SCAN PROTOCOL body rules; see BLOCK SCAN
PROTOCOL above for the protocol declaration):

1. `gate_fail:` field -- criterion C-04 (C-26) -- tag: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` -- at gate_fail: line
   *(instance #1 in BAD PLAN header below)*
2. `name:` field -- criterion C-06 (C-37) -- tag: `# WRONG C-06` -- at name: line
   *(instance #2 in BAD PLAN header below)*
3. `skills:` entry -- criterion C-03 (C-39) -- tag: `# WRONG C-03` -- at skills-list entry line
   *(instance #3 in BAD PLAN header below)*

Each item above corresponds to a numbered entry in the BAD PLAN (P1) header below.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BLOCK SCAN PROTOCOL (P1) -- Header Entry Index
# All 7 criteria: essential (C-01 through C-04) and recommended (C-05 through C-07)
#
# Numbered annotation-type index (exact tag strings per entry; full Why: per C-47; per-entry back-refs per C-48):
#   (1) gate_fail: → C-04 (C-26) → tag: # WRONG C-04: Why: execution-history check, not artifact-verifiable
#       (rule #1 in BLOCK SCAN PROTOCOL above)
#   (2) name: → C-06 (C-37) → tag: # WRONG C-06
#       (rule #2 in BLOCK SCAN PROTOCOL above)
#   (3) skills: entry → C-03 (C-39) → tag: # WRONG C-03
#       (rule #3 in BLOCK SCAN PROTOCOL above)
#   (4) this header → C-38 → affirmative full-criterion coverage (all 7 / C-01 through C-07)
#       (rule #4 in BLOCK SCAN PROTOCOL above)

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

# BLOCK SCAN PROTOCOL (P3): exit OK. All (P1) annotation types confirmed present in block above.
```

---

## V-04 -- C-47 + C-48 Co-Designed Axis (Fused Why/Navigation)

**Axis**: Combined variation on C-47 and C-48. The full Why: text (C-47) is embedded inside each
per-entry back-reference phrase (C-48), fusing both criteria into a single continuous annotation
unit per C-41 entry. Entry form: criterion + field type + exact tag string + full Why: clause +
`(this Why: text is the rationale declared in FIELD CO-LOCATION PRINCIPLE above -- see that
section for the co-location rule governing this field type)`. The C-42 table carries a per-row
forward-reference column pointing to specific entry numbers in the BAD PLAN header. C-49 is
satisfied via the BLOCK SPECIFICATION PROTOCOL naming convention.

**Hypothesis**: Fusing C-47 (full Why: content) into the C-48 per-entry back-reference phrase
creates a single annotation that simultaneously names the field type, exact tag string, the reason
the annotation is required (Why:), and where the rule governing it lives. A model reading any
single entry in the C-41 header encounters the full annotation specification and the principle
reference in one uninterrupted read, without needing to navigate to the C-42 section for the
rationale or to the C-44 spec for the tag form. Anticipated: 300/300.

**C-47 form**: Full Why: text embedded in the back-reference sentence -- `(this Why: clause --
execution-history check, not artifact-verifiable -- is the rationale declared in FIELD CO-LOCATION
PRINCIPLE above)`.
**C-48 form**: Each C-41 entry ends with the fused Why:/back-ref phrase; C-42 table has `BAD
PLAN header entry` column: `Entry (1)/(2)/(3) in BAD PLAN header below`.
**C-49 form**: `## BLOCK SPECIFICATION PROTOCOL`; BAD PLAN header: `# BLOCK SPECIFICATION
PROTOCOL -- Component 1: Header Entry Specification`; footer: `# BLOCK SPECIFICATION PROTOCOL
-- Component 3: Exit Verification (C-46)`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode:** catalog-first construction -- skill clustering before zone declaration. Destroys
zone membership, artifact provenance, and investigative intent simultaneously.

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

**Component 1 -- Header Entry Specification (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan specification: each entry names the field type, criterion,
exact tag string (including full Why: clause where applicable), and a back-reference to this
section that fuses the rationale with the navigation pointer. The fused form ensures a model
reading any header entry encounters the complete annotation specification and principle reference
without cross-document lookup.

**Component 2 -- Block Body with Field-Level Annotations (C-26, C-37, C-39)**

Wrong YAML with criterion tags at each violating field line.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types found present in block body.

**Navigation contract (C-45 + C-48):** this section (BLOCK SPECIFICATION PROTOCOL) is the
protocol declaration. See BAD PLAN block below for the bounded instance (Component 1 header
below). The FIELD CO-LOCATION PRINCIPLE table carries per-row forward-refs to specific
Component 1 entry numbers. Each Component 1 entry back-references this section.

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

**Catalog must remain closed.** Declare 3--6 phases from first principles.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

PASS: `discovery`, `stress-test`, `signal-watch`
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

Consumer-pull rule: # Produces: is set by what the NEXT stage needs.
Derivation runs backward from echo; YAML transcribed from backward derivation.

ROW-0 RULE: Echo is row 0. Derivation starts at row 0. # Band: omitted from echo is correct.
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

Three-field gate structure with uniform dual-position dep reminders:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at zone header -- dep zones only]
name: <phase-label>
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [at skills: line -- dep zones only]
skills:                                # check correction table: skill names
  - <namespace>:<skill>
gate_fail: "<execution-state>"         # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL: `"done"` -- Why: execution-history check, not artifact-verifiable

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

Verify gate artifacts are producible by stage skills. Fix before Step 6.

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
    skills:                                # requires: <artifact> from Zone: <name> (C-05)  [dep zones]
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
[ ] C-01 through C-46: all criteria as specified in V-01 above
[ ] C-47: full Why: text fused into per-entry back-ref phrase in C-41 header entries
[ ] C-48: each C-41 entry ends with fused Why:/back-ref phrase; C-42 table has per-row entry-number forward-refs
[ ] C-49: C-41/C-42/C-46 labeled as components of BLOCK SPECIFICATION PROTOCOL
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
exact field line. Three field types form the co-location family (BLOCK SPECIFICATION PROTOCOL
Component 2 body rules; see BLOCK SPECIFICATION PROTOCOL above):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN header entry |
|------------|-----------|-------------------------|------------------|----------------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | See entry (1) in BAD PLAN header below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | See entry (2) in BAD PLAN header below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry | See entry (3) in BAD PLAN header below |

Each row maps to a specific Component 1 entry in the BAD PLAN header below.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Entry Specification (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered -- essential (C-01 through C-04) and recommended (C-05 through C-07)
#
# Annotation-type entries (field type, criterion, exact tag+full Why:, fused back-ref per C-47+C-48):
#
#   Entry (1) C-26: gate_fail: carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (this Why: clause -- execution-history check, not artifact-verifiable -- is the rationale
#              declared in BLOCK SPECIFICATION PROTOCOL above for the gate_fail: co-location rule)
#
#   Entry (2) C-37: name: carries # WRONG C-06
#             (rule: namespace-label names violate C-06 -- declared in BLOCK SPECIFICATION PROTOCOL above)
#
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule: invented skill names violate C-03 -- declared in BLOCK SPECIFICATION PROTOCOL above)
#
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (coverage contract declared in BLOCK SPECIFICATION PROTOCOL above)

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

# BLOCK SPECIFICATION PROTOCOL -- Component 3: Exit Verification (C-46).
# All annotation types from Component 1 header entry specification confirmed present in block above.
```

---

## V-05 -- Extended Protocol Axis (Formal Sub-Specification)

**Axis**: Full integration. The BLOCK SPECIFICATION PROTOCOL section explicitly specifies C-47
and C-48 as numbered sub-requirements within Component 1's definition, making them first-class
protocol obligations rather than implicit enrichments of C-44. The C-46 exit footer explicitly
verifies both co-location completeness AND C-47 full Why: presence in Component 1. The protocol
is the most formal specification -- any model reading the protocol before the BAD PLAN block
encounters C-47 and C-48 as stated requirements, not discoverable patterns.

**Hypothesis**: Formally specifying C-47 and C-48 as sub-requirements of Component 1 causes a
model to treat the absence of full Why: text or per-entry back-refs as a protocol violation --
not just a quality gap. The C-46 footer's explicit C-47 verification raises the standard:
the exit marker confirms not just that co-location annotations exist but that the Why: rationale
in the header entry is unabbreviated. This is the maximum-density formulation, highest teaching
specificity. Anticipated: 300/300.

**C-47 form**: Protocol Component 1 spec sub-requirement: `(b) For entries referencing a Why:
annotation: include the full unabbreviated Why: text (C-47). Not Why: ... -- the complete clause.`
C-41 entries carry full Why: text per this sub-requirement.
**C-48 form**: Protocol Component 1 spec sub-requirement: `(c) Per-entry back-reference to this
section (C-48).` Each C-41 entry ends with `(rule declared in BLOCK SPECIFICATION PROTOCOL above)`.
C-42 table carries `BAD PLAN entry` column per-row.
**C-49 form**: `## BLOCK SPECIFICATION PROTOCOL`; BAD PLAN header: `# BLOCK SPECIFICATION
PROTOCOL -- Component 1: Header Entry Specification`; footer: `# BLOCK SPECIFICATION PROTOCOL
-- Component 3: Exit Verification (C-46) -- co-location complete; full Why: present in entry (1)`.

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
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## BLOCK SPECIFICATION PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit. Understanding this
protocol before construction ensures all three components are produced correctly.

**Component 1 -- Header Entry Specification (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan specification. Each entry must satisfy three sub-requirements:

- **(a) Name the exact tag string (C-44):** The entry states the exact annotation string used at
  that field type in the block body -- not just the field type and criterion number.
- **(b) Include the full unabbreviated Why: text where applicable (C-47):** For entries referencing
  an annotation that carries a Why: clause (specifically the gate_fail: / C-26 entry), the entry
  must include the complete Why: text verbatim: `Why: execution-history check, not artifact-
  verifiable`. The abbreviated form `Why: ...` fails this sub-requirement.
- **(c) Include a per-entry back-reference to this section (C-48):** Each individual entry ends
  with its own pointer to this section: `(rule declared in BLOCK SPECIFICATION PROTOCOL above)`.
  A single shared section-level pointer for all entries does not satisfy this sub-requirement.

**Component 2 -- Block Body with Field-Level Annotations (C-26, C-37, C-39)**

The block body contains wrong YAML. Every violating field carries its criterion tag at the exact
field line. The FIELD CO-LOCATION PRINCIPLE section (below) declares the three co-location rules
as the family principle. Component 2 is the instantiation of those rules in the BAD PLAN block.

**Component 3 -- Exit Verification (C-46)**

The block ends with an explicit footer confirming:
- (a) All annotation types from Component 1 are confirmed present in the block body.
- (b) The full Why: text (C-47) was present in the Component 1 gate_fail: entry -- not truncated.

This closes the bounded scan loop and provides a self-check: if the footer's (b) verification is
false, the Component 1 header entry (1) is incomplete and must be corrected.

**Protocol Navigation Contract (C-45 + C-48):**

- This section (BLOCK SPECIFICATION PROTOCOL) is the governing declaration. The BAD PLAN block
  below is the bounded instance: see the BAD PLAN header below for Component 1 (entry specification).
- The FIELD CO-LOCATION PRINCIPLE table below (C-42) carries a per-row forward reference to the
  specific Component 1 entry that implements each row's rule; each Component 1 entry carries its
  own per-entry back-reference to this section.

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

**The catalog must remain closed at this step.**

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

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:
Derivation runs backward from echo; YAML annotations are transcribed from the backward
derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction. Row 0 is
where derivation begins, not where execution ends. # Band: omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure. Dependency zones carry uniform
dual-position reminders:

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

| Form | Verdict | Reason |
|------|---------|--------|
| `discovery::scout-feasibility >= 3 AND scout:market artifact exists` | PASS | stage-id prefix, threshold, skill ref |
| `adequate discovery signals present` | FAIL C-04 | no prefix, no threshold, not artifact-verifiable |
| `>= 3 scout artifacts present` | FAIL C-04 | threshold only, no stage-id prefix |

At least one gate across all non-echo stages must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- PASS: `"Does the spec survive expert review against the discovered market signal?"`
- FAIL (not interrogative): `"Assess the compliance landscape"`
- FAIL (wrong scope): `"Are we ready to proceed?"`

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML annotations
are transcribed from ARTIFACT 2 matrix cells, not authored independently. The matrix and YAML
cannot diverge because YAML is a downstream rendering of the matrix.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
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

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; program: top-level key; stages: list present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate (artifact-verifiable)
[ ] C-05: namespace ordering respected: scout/draft -> review/prove -> flow/trace -> listen
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
[ ] C-19: error artifacts cover both essential AND recommended criteria
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
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: rationale (sub-req b of Component 1)
[ ] C-48: each C-41 entry has own per-entry back-ref (sub-req c); C-42 table has per-row forward-refs
[ ] C-49: C-41/C-42/C-46 labeled as components of BLOCK SPECIFICATION PROTOCOL
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
| `program:` key missing (top-level is `stages:`) | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |
| `echo` with skills listed | `skills: []` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that
exact field line. Three field types form the co-location family. This section is the BLOCK
SPECIFICATION PROTOCOL family declaration; the BAD PLAN Component 1 header below implements it
as an entry specification (see BLOCK SPECIFICATION PROTOCOL above for the full protocol):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | See entry (1) in BAD PLAN header below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | See entry (2) in BAD PLAN header below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry | See entry (3) in BAD PLAN header below |

Each row above maps to a specific numbered entry in the Component 1 header below.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BLOCK SPECIFICATION PROTOCOL -- Component 1: Header Entry Specification (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered -- essential (C-01 through C-04) AND recommended (C-05 through C-07)
#
# Annotation-type entry specification (sub-reqs: (a) exact tag, (b) full Why: where applicable, (c) per-entry back-ref):
#
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in BLOCK SPECIFICATION PROTOCOL above)
#
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in BLOCK SPECIFICATION PROTOCOL above)
#
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in BLOCK SPECIFICATION PROTOCOL above)
#
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in BLOCK SPECIFICATION PROTOCOL above)

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
# (a) Co-location complete: all annotation types from Component 1 entry specification confirmed present.
# (b) C-47 verified: full Why: text present in entry (1) -- "execution-history check, not artifact-verifiable"
#     (not truncated; sub-requirement (b) of Component 1 satisfied).
# (see BLOCK SPECIFICATION PROTOCOL above for protocol definition)
```
