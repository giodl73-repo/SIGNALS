---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 17
rubric: v17
rubric_date: 2026-03-16
total_pts: 320
golden_threshold: 80
new_criteria: C-52, C-53
---

# program-plan -- R17 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v17 (C-01 through C-53, 46 aspirational criteria, 320 pts, golden: all essential pass AND composite >= 80).

**R16-2026-03-16 state under v17 rubric (C-52/C-53 added):**
- V-01 (SCAN PROTOCOL, 4-column table): passes C-50 but not C-51 -- C-52 requires both, fails -- 310/320
- V-02 (BOUNDED BLOCK PROTOCOL first): passes C-51 but not C-50 -- C-52 requires both, fails -- 310/320
- V-03 (BLOCK AUDIT PROTOCOL, Zone Decision Tables): fails C-50 and C-51 -- 300/320
- V-04 (ANNOTATION VERIFICATION PROTOCOL, per-step AVOID): fails C-50 and C-51 -- 300/320
- V-05 (BOUNDED BLOCK PROTOCOL first + 4-column table): passes C-50 and C-51; protocol section
  describes columns ("Component 1 is a 4-column table") -- C-52 PASS; but language is descriptive
  not prescriptive -- C-53 FAIL -- 315/320

**R17 design constraint:** V-01 must maintain C-50. V-02 must maintain C-51. V-03 and V-04 are
new single-axis variants that do not target C-50 or C-51. V-05 must satisfy C-50+C-51+C-52+C-53
simultaneously -- C-52 and C-53 are reachable only from V-05.

**C-52 canonical form (V-05 only):**
- Protocol section (first in document per C-51) explicitly names the column schema of the C-41
  index table -- listing all four columns by name and purpose -- before the BAD PLAN block
- Provides dual exposure: column spec in protocol section, instantiated table in BAD PLAN header

**C-53 canonical form (V-05 only):**
- Column schema declaration uses prescriptive/directive language: "Component 1 MUST be a
  4-column table" or "Format requirement for Component 1: 4 columns as listed below"
- Language frames the table format as a protocol requirement, not an observation about current form
- Converts C-50 from observed structural choice into explicitly mandated architectural rule

**Variation axes for R17:**
- V-01 (carry-forward: output format): SCAN PROTOCOL with C-41 as 4-column pipe table confirming C-50
- V-02 (carry-forward: role sequence): BOUNDED BLOCK PROTOCOL first confirming C-51
- V-03 (new: phrasing register): MANDATE VERIFICATION PROTOCOL -- all construction rules expressed
  as SHALL/MUST directives; high-authority mandate register throughout
- V-04 (new: lifecycle emphasis): ZONE LOCK PROTOCOL -- zone commitment locked before catalog;
  per-zone Lock Declaration table at Step 2 makes zone membership a formal artifact
- V-05 (combined: C-50+C-51+C-52+C-53): BOUNDED BLOCK PROTOCOL first (C-51) + prescriptive column
  mandate in protocol section (C-52+C-53) + 4-column pipe table in BAD PLAN header (C-50)

---

## V-01 -- Output Format Axis (SCAN PROTOCOL -- 4-Column Table Index)

**Axis**: Single-axis variation on output format. The C-41 annotation-type index in the BAD PLAN
header is a pipe-delimited markdown table with exactly 4 columns: field type, criterion, exact tag
string with full Why: clause, and per-entry C-42 back-reference. Satisfies C-50. SCAN PROTOCOL
naming carried forward from R15/R16 unchanged.

**Hypothesis**: A tabular C-41 index promotes each data type to an independently scannable column.
A model returning to the index during block scanning looks up any column directly without re-parsing
prose. C-50 satisfies the format requirement; the SCAN PROTOCOL section (placed after the three-class
table) provides the C-49 named protocol. C-51 not targeted: SCAN PROTOCOL is not document-first.
Anticipated: 310/320 (C-51, C-52, C-53 not reached).

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag
string (with full `Why:` in column 3 for gate_fail:) | C-42 back-ref.
**C-47 form**: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` as column 3
value in the gate_fail: table row.
**C-48 form**: Column 4 per row: `SCAN PROTOCOL decl. above`; FIELD CO-LOCATION PRINCIPLE table
has `BAD PLAN entry` column: `Row (1) below`, `Row (2) below`, `Row (3) below`.
**C-49 form**: Section `## SCAN PROTOCOL`; BAD PLAN header label `# SCAN PROTOCOL -- C1: Header
Index`; footer `# SCAN PROTOCOL -- C3: exit verified`.
**C-51**: Not targeted (SCAN PROTOCOL is not document-first).

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

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components:

| Label | Criteria | Content |
|-------|----------|---------|
| **C1 -- Header Index** | C-41, C-44, C-47, C-48, C-50 | 4-column pipe table: field type / criterion / exact tag string with full Why: / C-42 back-ref |
| **C2 -- Block Body** | C-26, C-37, C-39 | Wrong YAML with field-level criterion tags at every violating field line |
| **C3 -- Exit Verification** | C-46 | Footer confirming all C1 annotation types found present in block body |

Navigation contract (C-45 + C-48): This section (SCAN PROTOCOL) is the protocol declaration.
The BAD PLAN C1 header below is the entry index. Each FIELD CO-LOCATION PRINCIPLE table row
carries a per-row forward-reference to its specific C1 table row number. Each C1 table row
carries this section as its back-ref (column 4).

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

Consumer-pull rule [counter: F-1]: # Produces: is set by what the NEXT stage declares as
# Consumes: -- not by the prior stage's skill output inventory. Derivation runs backward from
echo; YAML annotations are transcribed from the backward derivation, not authored from skill
knowledge. The negation closes the producer-push misreading: Produces is NOT authored from the
current stage's skill knowledge.

ROW-0 RULE [counter: F-2]: Echo occupies row 0 of ARTIFACT 2. Row 0 is where derivation begins,
not where execution ends. # Band: omitted from echo is correct.
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
are transcribed from ARTIFACT 2 matrix cells, not authored independently.

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
[ ] C-50: C-41 index is a 4-column pipe table -- YES for this variate
[ ] C-51: named protocol section is document-first -- NO for this variate (SCAN PROTOCOL not first)
[ ] C-52: protocol section pre-declares column schema -- NOT REACHABLE (requires C-51)
[ ] C-53: column schema uses prescriptive language -- NOT REACHABLE (requires C-52)
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
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Row (1) in SCAN PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Row (2) in SCAN PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Row (3) in SCAN PROTOCOL C1 below |

The BAD PLAN C1 header below implements this family as the SCAN PROTOCOL entry index table.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in SCAN PROTOCOL C1 below

```yaml
# SCAN PROTOCOL -- C1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                         | C-42 back-ref            |
# |---------------|---------------|-------------------------------------------------------------------------------|--------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable           | SCAN PROTOCOL decl. above |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                  | SCAN PROTOCOL decl. above |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                  | SCAN PROTOCOL decl. above |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                   | SCAN PROTOCOL decl. above |

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

## V-02 -- Role Sequence Axis (BOUNDED BLOCK PROTOCOL -- First Section)

**Axis**: Single-axis variation on role sequence. The BOUNDED BLOCK PROTOCOL section appears
FIRST in the prompt -- before the three-class information table, before lifecycle zones, before
the catalog. A model reads the bounded-unit architecture before any construction guidance.
C-47, C-48, C-49 carried forward from R15/R16 unchanged. C-51 confirmed.

**Hypothesis**: Positioning the protocol architecture at the document's opening causes every
subsequent section to be read through the protocol frame. The principle-before-instance
architecture (C-51) ensures no section is read before the protocol that governs it. A brief role
context statement before the protocol does not constitute a major section. Anticipated: 310/320
(C-50 not reached -- C-41 index is prose enumeration; C-52 and C-53 not reachable without C-50).

**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before the three-class table, lifecycle
zones, catalog, and construction steps. Only a single opening sentence precedes it.
**C-47 form**: `Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history
check, not artifact-verifiable` with `(rule declared in BOUNDED BLOCK PROTOCOL above)` per entry.
**C-48 form**: Each C-41 entry ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)`;
FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column: `See entry (1/2/3) in BAD PLAN
header below`.
**C-49 form**: `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL --
Component 1: Header Entry Index`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3: Exit
Verification (C-46) complete`.
**C-50**: Not targeted (C-41 index is prose enumeration, not 4-column table).

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
field line. The FIELD CO-LOCATION PRINCIPLE section (below, after construction steps) declares
this family principle.

**Component 3 -- Exit Verification (C-46)**

The block ends with an explicit footer confirming all annotation types from Component 1 were
found present in the block body. This closes the bounded scan loop.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration. See the BAD PLAN block
  for the bounded instance implementing this protocol (Component 1 header below).
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1
  entry numbers in the BAD PLAN header.

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

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction.
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
[ ] C-01 through C-49: all criteria
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: rationale (not Why: ...)
[ ] C-48: per-entry bidirectional navigation (each C-41 entry has own back-ref; C-42 has per-row forward-refs)
[ ] C-49: C-41/C-42/C-46 labeled as components of BOUNDED BLOCK PROTOCOL named entity
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate (prose entries)
[ ] C-51: named protocol section is document-first -- YES for this variate
[ ] C-52: protocol section pre-declares column schema -- NOT REACHABLE (requires C-50)
[ ] C-53: column schema uses prescriptive language -- NOT REACHABLE (requires C-52)
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

## V-03 -- Phrasing Register Axis (MANDATE VERIFICATION PROTOCOL)

**Axis**: Single-axis variation on phrasing register. All construction step rules, co-location
family declarations, and gate requirements are expressed using prescriptive SHALL/MUST/WILL
mandate language throughout the prompt. The construction order is a series of mandatory
obligations, not instructions. This register distinguishes this variation from both V-01
(output format) and V-02 (role sequence).

**Hypothesis**: Mandate language elevates every construction rule from a suggestion to an
explicit requirement. A model reading "You SHALL NOT open the catalog before declaring phases"
treats the constraint as a hard rule, not a guideline. Mandate register applied uniformly
creates a consistent compliance-framing throughout the document. The protocol section
(MANDATE VERIFICATION PROTOCOL) uses the same register internally -- "Component 1 MUST contain
a pre-scan annotation index." This makes the bounded block architecture feel like a hard
specification, not a recommendation. Not targeting C-50 or C-51.
Anticipated: 300/320 (C-50 fails -- prose index; C-51 fails -- protocol not first).

**C-47 form**: Full Why: in C-41 prose entries with mandate register:
  `Entry (1) C-26: gate_fail: MUST carry # WRONG C-04: Why: execution-history check, not artifact-verifiable`
**C-48 form**: Each C-41 entry ends with `(rule declared in MANDATE VERIFICATION PROTOCOL above)`;
  FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column per row.
**C-49 form**: `## MANDATE VERIFICATION PROTOCOL`; BAD PLAN header:
  `# MANDATE VERIFICATION PROTOCOL -- Component 1: Header Index`; footer:
  `# MANDATE VERIFICATION PROTOCOL -- Component 3: Exit Verified`.
**C-50, C-51**: Not targeted.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program SHALL sequence plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs MUST seed
the entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before
declaring arc phases. You MUST NOT open the catalog before completing Step 2. Violation causes
implicit zone membership, prose gates, and absent investigative intent.

Three classes of information SHALL remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- MUST be declared before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill -- MUST be traceable | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- MUST be interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## MANDATE VERIFICATION PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit. The following
component obligations MUST be satisfied:

**Component 1 -- Header Index (C-41 + C-44 + C-47 + C-48): REQUIRED**

The BAD PLAN header MUST contain a pre-scan annotation-type index. Each entry SHALL name:
field type, criterion, exact tag string with full unabbreviated Why: where applicable, and a
per-entry back-reference to this section. The header MUST affirmatively claim full-criterion
coverage of all 7 criteria (C-38).

Required index entry form:
```
# C-XX: <field type> MUST carry <exact tag string with full Why: if applicable>
#       (rule declared in MANDATE VERIFICATION PROTOCOL above)
```

**Component 2 -- Block Body (C-26, C-37, C-39): REQUIRED**

The block body MUST contain wrong YAML. Every violating field SHALL carry its criterion tag at
the exact field line -- not adjacent, not in a header comment.

**Component 3 -- Exit Verification (C-46): REQUIRED**

The block MUST end with a footer confirming all Component 1 annotation types were found present
in the block body. Omitting this component is a protocol violation.

**Navigation obligations (C-45 + C-48):**
- This section (MANDATE VERIFICATION PROTOCOL) SHALL be the governing declaration.
- The FIELD CO-LOCATION PRINCIPLE section MUST carry per-row forward-refs to specific Component 1
  entry numbers. Each Component 1 entry SHALL carry this section as its back-ref.

---

**Compound gate format -- MANDATORY:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

You SHALL use this exact format. `{stage-id}` MUST match `name:` exactly. `>= N` is required.
`{namespace}:{skill}` is required. A gate MUST NOT use execution-state language.

---

**Valid Signal Plugin Skill Catalog -- MANDATORY REFERENCE**

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

Every `skills:` entry MUST be a namespace-qualified name from this catalog. Invented names are
a hard fail (C-03).

---

## CONSTRUCTION ORDER -- MANDATORY SEQUENCE

You SHALL follow these steps in order. You MUST NOT proceed to Step 3 before completing Step 2.

1. Declare the topic (Step 1)
2. Declare arc phases -- catalog MUST remain closed (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit -- MUST complete before Step 6 (Step 5b)
6. Write per-phase intent questions: MUST be interrogative (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: MUST produce ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings MUST be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases

**The catalog MUST remain closed at this step.** You SHALL declare 3--6 phase boundaries from
first principles. Each phase MUST be assigned to a zone: `breadth`, `depth`, or `synthesis`.

| Phase label | Zone | Investigative question (MUST end with ?) |
|-------------|------|------------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage` (namespace-cluster label), `listen_phase` (namespace repetition)

**You MUST produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage (MANDATORY):
  # Band:     [meta-structure entry ID -- e.g., B-01, G-02]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule [MANDATORY]: # Produces: MUST be set by what the NEXT stage declares as
# Consumes: -- NOT by the prior stage's skill output inventory. Derivation MUST run backward
from echo; YAML annotations SHALL be transcribed from the backward derivation, not authored
from skill knowledge.

ROW-0 RULE [MANDATORY]: Echo MUST occupy row 0 of ARTIFACT 2. Row 0 is where derivation
begins, not where execution ends. # Band: omitted from echo is correct.
```

You MUST produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. You SHALL select only skills relevant to the topic. For each skill, note
the declared phase it maps to.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. You MUST NOT create new phases to accommodate skills.
Skills with no matching phase SHALL be discarded.

---

#### Step 5a -- Design Gates

For each non-echo zone, you SHALL use the three-field gate structure. Dependency zones MUST
carry dual-position reminders in uniform syntax:

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
| `"done"` | FAIL C-04 | execution-history check -- MUST NOT be used |
| `>= 3 scout artifacts present` | FAIL C-04 | threshold only, no stage-id prefix |

At least one gate across all non-echo stages MUST include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: you MUST verify every artifact type in the gate is producible by at
least one skill in that stage's `skills` array. All forward references MUST be fixed before Step 6.

---

#### Step 6 -- Phase Intent Questions

Intent questions MUST be interrogative (end with `?`) and MUST be zone-specific.

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL (not interrogative): `"Assess the compliance landscape"` -- MUST be rejected
- FAIL (wrong scope): `"Are we ready to proceed?"` -- MUST be rejected as non-zone-specific

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

You MUST produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column** before
assembling YAML.

**ARTIFACT 2 SHALL be the sole authoritative source for all per-stage annotations.** YAML
annotations MUST be transcribed from ARTIFACT 2 matrix cells. They SHALL NOT be authored
independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (MANDATORY -- transcribe from ARTIFACT 2, then add fields):

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

Any NO MUST trigger revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; program: top-level key; stages: list present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate (artifact-verifiable)
[ ] C-05: namespace ordering respected
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08 through C-49: all aspirational criteria
[ ] C-47: gate_fail: C-41 entry includes full unabbreviated Why: (not Why: ...)
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as MANDATE VERIFICATION PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate
[ ] C-51: named protocol section is document-first -- NO for this variate
[ ] C-52, C-53: not reachable (require C-50 and C-51)
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

Every YAML field carrying a criterion-testable value MUST carry an inline criterion tag at that
exact field line. This is the MANDATE VERIFICATION PROTOCOL co-location family (see MANDATE
VERIFICATION PROTOCOL section above for the full protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | MUST be at gate_fail: line | Entry (1) in MANDATE VERIFICATION PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | MUST be at name: line | Entry (2) in MANDATE VERIFICATION PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | MUST be at skills-list entry line | Entry (3) in MANDATE VERIFICATION PROTOCOL C1 below |

The BAD PLAN C1 header below SHALL implement this family as the entry index.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# MANDATE VERIFICATION PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: MUST carry # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in MANDATE VERIFICATION PROTOCOL above)
#   Entry (2) C-37: name: MUST carry # WRONG C-06
#             (rule declared in MANDATE VERIFICATION PROTOCOL above)
#   Entry (3) C-39: skills: entries MUST carry # WRONG C-03
#             (rule declared in MANDATE VERIFICATION PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in MANDATE VERIFICATION PROTOCOL above)

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

# MANDATE VERIFICATION PROTOCOL -- Component 3: Exit Verified.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

## V-04 -- Lifecycle Emphasis Axis (ZONE LOCK PROTOCOL)

**Axis**: Single-axis variation on lifecycle emphasis. Step 2 produces a formal Zone Lock
Declaration for each phase -- a per-phase table with columns Zone | Lock Condition | Artifact
Floor | Owner -- making zone membership a formal artifact that must be produced before the
catalog opens. "Zone locking" frames the pre-catalog commitment as a gate that the plan itself
must pass before construction proceeds. A model that opens the catalog before producing Zone
Lock Declarations has violated the lock condition. Distinct from R16 V-03 (Zone Decision Tables
are reference tables per zone; Zone Lock Declarations are per-phase commitment artifacts
produced BY the model during Step 2).

**Hypothesis**: Making zone membership a produced artifact (Zone Lock Declaration) rather than a
classification step creates stronger phase boundary enforcement. A model filling in a Zone Lock
Declaration for each phase must commit to a zone, a lock condition, an artifact floor, and an
owner -- four independently checkable facts per phase. This forecloses "zone drift" where phase
membership is nominal but gate design contradicts it. Not targeting C-50 or C-51.
Anticipated: 300/320 (C-50 fails -- prose index; C-51 fails -- protocol not first).

**C-47 form**: Full Why: in C-41 prose entries with ZONE LOCK PROTOCOL naming.
**C-48 form**: Per-entry back-refs and per-row forward-refs per protocol standard.
**C-49 form**: `## ZONE LOCK PROTOCOL`; BAD PLAN header:
  `# ZONE LOCK PROTOCOL -- Component 1: Header Index`; footer:
  `# ZONE LOCK PROTOCOL -- Component 3: Exit Verified`.
**Zone lock form**: Step 2 requires production of Zone Lock Declaration table
  (Phase | Zone | Lock Condition | Artifact Floor | Owner) before catalog access.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before
declaring and locking arc phases. Zone lock declarations must exist before any catalog access.
A plan with implicit zone membership has no lock condition -- phase boundaries drift as skills
are added, gates become prose checks, investigative intent disappears.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- locked before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## ZONE LOCK PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components:

**Component 1 -- Header Index (C-41 + C-44 + C-47 + C-48)**: Pre-scan annotation-type index.
Each entry names: field type, criterion, exact tag string with full Why: where applicable, and
a back-reference to this section. Affirmatively covers all 7 criteria (C-38).

**Component 2 -- Block Body (C-26, C-37, C-39)**: Wrong YAML with criterion tags at every
violating field line.

**Component 3 -- Exit Verification (C-46)**: Footer confirming all Component 1 annotation types
found present in block body.

Navigation contract (C-45 + C-48): This section (ZONE LOCK PROTOCOL) is the governing
declaration. The FIELD CO-LOCATION PRINCIPLE section below carries per-row forward-refs to
specific Component 1 entry numbers. Each Component 1 entry back-references this section.

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
2. Declare arc phases and produce Zone Lock Declarations -- catalog closed (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates aligned to Zone Lock artifact floors (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table with zone lock verification (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Zone Lock Declarations are complete.

---

#### Step 1 -- Topic

State the topic name. All artifact names and phase groupings must be coherent with this topic.

---

#### Step 2 -- Declare Arc Phases and Produce Zone Lock Declarations

**The catalog must remain closed at this step.**

Declare 3--6 phase boundaries from first principles. For each phase, produce a Zone Lock
Declaration -- a formal commitment that locks the phase to a zone before any catalog access.

**Step 2a -- Phase Declaration Table:**

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

- PASS phase labels: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL phase labels: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

**Step 2b -- Zone Lock Declaration Table (one row per phase):**

| Phase | Zone | Lock Condition (what must exist before this phase unlocks) | Artifact Floor (minimum artifacts required) | Owner |
|-------|------|------------------------------------------------------------|---------------------------------------------|-------|
| [name] | breadth/depth/synthesis | [prior artifact or "none" for first phase] | >= N artifacts of type [X] | PM/Architect/Dev/Team Lead |

The Lock Condition column is the predecessor artifact gate: a phase cannot begin until the
prior zone has produced what this zone's Lock Condition names. This is the same principle as
gate design (Step 5a) applied at zone entry rather than stage exit.

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
Derivation runs backward from echo; YAML annotations are transcribed from backward derivation,
not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Derivation begins at row 0.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. For each selected skill, verify it maps to a phase declared in the Zone
Lock Declaration Table. Skills with no matching phase are discarded -- do not create new phases.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. Verify the Zone Lock Declaration's artifact floor will be
satisfied by the skills assigned to each phase.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure. Gate values must reference the
artifact floor specified in the Zone Lock Declaration Table for that phase. Dependency zones
carry dual-position reminders in uniform syntax:

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
| `discovery::scout-feasibility >= 3 AND scout:market artifact exists` | PASS | matches Zone Lock Declaration artifact floor |
| `"done"` | FAIL C-04 | execution-history check, not verifiable by artifact inspection |
| `adequate signals present` | FAIL C-04 | no stage-id prefix, no threshold, not artifact-verifiable |

At least one gate across all non-echo stages must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix before Step 6.

---

#### Step 6 -- Phase Intent Questions

Intent questions must be interrogative (end with `?`) and zone-specific.

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

| Stage | Zone Lock Declaration satisfied? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|----------------------------------|-------------------------------------|--------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision before Step 10.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-49: all criteria
[ ] C-47: gate_fail: C-41 entry has full unabbreviated Why: (not Why: ...)
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as ZONE LOCK PROTOCOL components
[ ] Zone Lock Declarations produced in Step 2b for all phases
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate
[ ] C-51: named protocol section is document-first -- NO for this variate
[ ] C-52, C-53: not reachable (require C-50 and C-51)
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
exact field line. This is the ZONE LOCK PROTOCOL co-location family (see ZONE LOCK PROTOCOL
section above for the protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in ZONE LOCK PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in ZONE LOCK PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in ZONE LOCK PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# ZONE LOCK PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in ZONE LOCK PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in ZONE LOCK PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in ZONE LOCK PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in ZONE LOCK PROTOCOL above)

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

# ZONE LOCK PROTOCOL -- Component 3: Exit Verified.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

## V-05 -- Combined Axis (C-50 + C-51 + C-52 + C-53: Table Index + Protocol First + Prescriptive Column Mandate)

**Axis**: Combined variation targeting all four new criteria simultaneously. The BOUNDED BLOCK
PROTOCOL section appears FIRST (C-51). The protocol section uses prescriptive language to
MANDATE that Component 1 is a 4-column table, naming all four columns by purpose before the
BAD PLAN block (C-52 + C-53). The BAD PLAN header implements the mandated table format (C-50).

**Hypothesis**: The C-52/C-53 chain requires both C-50 and C-51 to be present simultaneously,
then requires the protocol section (first in document) to pre-specify the Component 1 table
format. C-52 is satisfied when the protocol section names the column schema. C-53 is satisfied
when that naming uses prescriptive/directive language -- "Component 1 MUST be a 4-column table"
rather than "Component 1 is a 4-column table." The upgrade from descriptive (R16 V-05) to
prescriptive (R17 V-05) converts the column schema from an observed fact about the document
into an architecturally mandated format requirement: a model deviating from the declared column
schema produces a protocol violation, not merely an unexpected structural choice.
Anticipated: 320/320 (all four new criteria pass).

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag
string with full Why: | C-42 back-ref per row.
**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before three-class table, lifecycle zones,
catalog, and construction steps. Only a single opening sentence precedes it.
**C-52 form**: Protocol section explicitly names all four column purposes before the BAD PLAN
block: "Column 1: field type; Column 2: criterion; Column 3: exact tag string including full
Why: where applicable; Column 4: per-row C-42 back-reference."
**C-53 form**: Protocol section uses MUST/SHALL directive language for the column mandate:
"Component 1 MUST be a 4-column pipe-delimited table. Format requirement: columns as specified
below." The word "must" converts C-50 from structural observation into protocol requirement.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit.
The protocol architecture below MUST be understood before any construction step begins.

**Component 1 -- Header Index: FORMAT REQUIREMENT**

Component 1 MUST be a 4-column pipe-delimited table. Any other format (prose enumeration,
indented list, bulleted entries) is a protocol violation. The four columns are mandatory:

| Column | Purpose | Criteria satisfied |
|--------|---------|-------------------|
| Column 1: Field type | Which YAML field carries the annotation -- gate_fail:, name:, skills: entry, or this header | C-41 |
| Column 2: Criterion | Criterion number governing that field -- C-04 (C-26), C-06 (C-37), C-03 (C-39), C-38 | C-41 |
| Column 3: Exact tag string | The annotation string as it appears at the field, including full unabbreviated Why: clause where applicable | C-44 + C-47 |
| Column 4: C-42 back-ref | Per-row reference to this protocol section by name | C-48 |

The header table MUST affirmatively claim full-criterion coverage of all 7 criteria (C-38).

**Component 2 -- Block Body: FIELD CO-LOCATION REQUIREMENT**

The block body MUST contain wrong YAML. Every violating field SHALL carry its criterion tag at
the exact field line -- not adjacent, not in a header comment. Field-level tags MUST match the
tag strings specified in Component 1 Column 3.

**Component 3 -- Exit Verification: COMPLETION REQUIREMENT**

The block MUST end with an explicit footer confirming all annotation types from Component 1 were
found present in the block body. This closes the bounded scan loop.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration. The BAD PLAN block below
  is the bounded instance.
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1
  table rows. Each Component 1 table row carries "BOUNDED BLOCK PROTOCOL decl. above" in column 4.

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

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:
Derivation runs backward from echo; YAML annotations are transcribed from the backward
derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Derivation begins at row 0, not where
execution ends.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic.

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
| `"done"` | FAIL C-04 | execution-history check, not artifact-verifiable |
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
are transcribed from ARTIFACT 2 matrix cells, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema (transcribe from ARTIFACT 2, then add fields):

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
[ ] C-05: namespace ordering respected
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08 through C-49: all aspirational criteria
[ ] C-47: gate_fail: C-41 entry has full unabbreviated Why:
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as BOUNDED BLOCK PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- YES for this variate
[ ] C-51: named protocol section is document-first -- YES for this variate
[ ] C-52: protocol section pre-declares column schema using all four column names -- YES
[ ] C-53: column schema declaration uses prescriptive MUST/SHALL language -- YES
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
exact field line. This is the BOUNDED BLOCK PROTOCOL co-location family (see BOUNDED BLOCK
PROTOCOL section above for the full protocol declaration). The BAD PLAN C1 table below
implements this family per the Component 1 format requirement stated in the protocol section:

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Row (1) in BOUNDED BLOCK PROTOCOL C1 table below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Row (2) in BOUNDED BLOCK PROTOCOL C1 table below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Row (3) in BOUNDED BLOCK PROTOCOL C1 table below |

Each row maps to a specific C1 table row below (see "BAD PLAN entry" column).

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in BOUNDED BLOCK PROTOCOL C1 below

```yaml
# BOUNDED BLOCK PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                         | C-42 back-ref                    |
# |---------------|---------------|-------------------------------------------------------------------------------|----------------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable           | BOUNDED BLOCK PROTOCOL decl. above |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                  | BOUNDED BLOCK PROTOCOL decl. above |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                  | BOUNDED BLOCK PROTOCOL decl. above |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                   | BOUNDED BLOCK PROTOCOL decl. above |

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
# All annotation types from Component 1 table confirmed present in block above.
```
