---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 18
rubric: v18
rubric_date: 2026-03-16
total_pts: 325
golden_threshold: 80
new_criteria: C-54
---

# program-plan -- R18 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v18 (C-01 through C-54, 47 aspirational criteria, 325 pts, golden: all essential pass AND composite >= 80).

**R17-2026-03-16 state under v18 rubric (C-54 added):**
- V-01 (SCAN PROTOCOL, 4-column table): C-50 PASS, C-51 FAIL → C-52 not reachable → C-53 not reachable → C-54 not reachable -- ~305/325
- V-02 (BOUNDED BLOCK PROTOCOL first): C-51 PASS, C-50 FAIL → C-52 not reachable → C-53 not reachable → C-54 not reachable -- ~305/325
- V-03 (MANDATE VERIFICATION PROTOCOL): C-50 FAIL, C-51 FAIL → chain unreachable -- ~295/325
- V-04 (ZONE LOCK PROTOCOL): C-50 FAIL, C-51 FAIL → chain unreachable -- ~295/325
- V-05 (BOUNDED BLOCK PROTOCOL first + prescriptive column mandate + 4-column table): C-50 PASS, C-51 PASS, C-52 PASS, C-53 PASS; named exclusions already present in R17 V-05 body → C-54 PASS -- 325/325

**R18 design constraint:** V-01 must maintain C-50. V-02 must maintain C-51. V-03 and V-04 are
new single-axis variants that do not target C-50 or C-51. V-05 must satisfy the full chain
C-50+C-51+C-52+C-53+C-54 simultaneously -- C-54 is only reachable from V-05.

**C-54 canonical form (V-05 only):**
- The C-53 prescriptive mandate enumerates forbidden alternatives by name in the negative
  boundary clause: "Any other format (prose enumeration, indented list, bulleted entries) is
  a protocol violation."
- Naming converts the mandate from one-sided positive ("must be X") into a bounded design
  space ("must be X; these named alternatives are individually disqualified")
- The named exclusion list also functions as a self-review diagnostic checklist

**Variation axes for R18:**
- V-01 (carry-forward: output format): SCAN PROTOCOL with C-41 as 4-column pipe table confirming C-50
- V-02 (carry-forward: role sequence): BOUNDED BLOCK PROTOCOL first confirming C-51
- V-03 (new: inertia framing): INERTIA CONTRAST PROTOCOL -- each construction step names the
  anti-pattern it prevents, with the "catalog-first" failure mode referenced as a named foil at
  every decision point rather than only in the document preamble
- V-04 (new: exclusion-boundary architecture): EXCLUSION-BOUNDARY PROTOCOL -- every major
  requirement leads with enumerated exclusions before stating the positive rule; the C-54
  negative-boundary pattern applied globally as an architectural philosophy
- V-05 (combined: C-50+C-51+C-52+C-53+C-54): BOUNDED BLOCK PROTOCOL first (C-51) + prescriptive
  column mandate with named exclusions (C-52+C-53+C-54) + 4-column pipe table in BAD PLAN
  header (C-50)

---

## V-01 -- Output Format Axis (SCAN PROTOCOL -- 4-Column Table Index)

**Axis**: Single-axis variation on output format. The C-41 annotation-type index in the BAD PLAN
header is a pipe-delimited markdown table with exactly 4 columns: field type, criterion, exact tag
string with full Why: clause, and per-entry C-42 back-reference. Satisfies C-50. SCAN PROTOCOL
naming carried forward from R16/R17 unchanged.

**Hypothesis**: A tabular C-41 index promotes each data type to an independently scannable column.
A model returning to the index during block scanning looks up any column directly without re-parsing
prose. C-50 satisfies the format requirement; the SCAN PROTOCOL section (placed after the three-class
table) provides the C-49 named protocol. C-51 not targeted: SCAN PROTOCOL is not document-first.
Anticipated: 305/325 (C-51, C-52, C-53, C-54 not reached -- chain broken at C-51).

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag
string (with full `Why:` in column 3 for gate_fail:) | C-42 back-ref.
**C-47 form**: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` as column 3
value in the gate_fail: table row.
**C-48 form**: Column 4 per row: `SCAN PROTOCOL decl. above`; FIELD CO-LOCATION PRINCIPLE table
has `BAD PLAN entry` column: `Row (1) below`, `Row (2) below`, `Row (3) below`.
**C-49 form**: Section `## SCAN PROTOCOL`; BAD PLAN header label `# SCAN PROTOCOL -- C1: Header
Index`; footer `# SCAN PROTOCOL -- C3: exit verified`.
**C-51**: Not targeted (SCAN PROTOCOL is not document-first).
**C-54**: Not reachable (requires C-53, which requires C-52, which requires C-51 -- not present).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before
declaring arc phases. Result: zone membership is implicit; gates are prose checks; investigative
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
knowledge.

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
[ ] C-09 through C-49: standard aspirational criteria
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: rationale (not Why: ...)
[ ] C-48: per-entry bidirectional navigation: each C-41 entry has own back-ref; C-42 has per-row forward-refs
[ ] C-49: C-41/C-42/C-46 labeled as components of SCAN PROTOCOL named entity
[ ] C-50: C-41 index is a 4-column pipe table -- YES for this variate
[ ] C-51: named protocol section is document-first -- NO for this variate (SCAN PROTOCOL not first)
[ ] C-52: protocol section pre-declares column schema -- NOT REACHABLE (requires C-51)
[ ] C-53: column schema uses prescriptive language -- NOT REACHABLE (requires C-52)
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name -- NOT REACHABLE (requires C-53)
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
C-47, C-48, C-49 carried forward from R17 unchanged. C-51 confirmed.

**Hypothesis**: Positioning the protocol architecture at the document's opening causes every
subsequent section to be read through the protocol frame. The principle-before-instance
architecture (C-51) ensures no section is read before the protocol that governs it. A brief role
context statement before the protocol does not constitute a major section. Anticipated: 305/325
(C-50 not reached -- C-41 index is prose enumeration; C-52, C-53, C-54 not reachable without C-50).

**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before the three-class table, lifecycle
zones, catalog, and construction steps. Only a single opening sentence precedes it.
**C-47 form**: `Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history
check, not artifact-verifiable` with `(rule declared in BOUNDED BLOCK PROTOCOL above)` per entry.
**C-48 form**: Each C-41 entry ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)`;
FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column: `See entry (1/2/3) in BAD PLAN
header below`.
**C-49 form**: `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header:
  `# BOUNDED BLOCK PROTOCOL -- Component 1: Header Entry Index`; footer:
  `# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification (C-46) complete`.
**C-50**: Not targeted (C-41 index is prose enumeration, not 4-column table).
**C-54**: Not reachable (requires C-50 → C-52 → C-53 → C-54 chain; C-50 absent).

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
[ ] C-49: C-41/C-42/C-46 labeled as BOUNDED BLOCK PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate (prose entries)
[ ] C-51: named protocol section is document-first -- YES for this variate
[ ] C-52: protocol section pre-declares column schema -- NOT REACHABLE (requires C-50)
[ ] C-53: column schema uses prescriptive language -- NOT REACHABLE (requires C-52)
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name -- NOT REACHABLE (requires C-53)
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

## V-03 -- Inertia Framing Axis (INERTIA CONTRAST PROTOCOL)

**Axis**: Single-axis variation on inertia framing. Every construction step opens with a named
inertia action -- what a team skipping the program plan and running skills ad-hoc does at this
decision point -- before stating the correct protocol action. The catalog-first failure mode is
referenced at every step as a named anti-pattern foil, not only in the preamble. The inertia
frame appears at the protocol section, at each construction step header, and in the terminal
checklist as a confirmation that each step was taken against its inertia foil.

**Hypothesis**: Single-preamble failure mode framing is read once at document entry and
forgotten by the time the model reaches Step 4 or Step 5. Per-step inertia contrasts fire at
the exact moment each decision is made, making the anti-pattern locally visible at every
authoring choice point. A model that would default to catalog-first behavior encounters the
named inertia action at each step, not just at document entry. Not targeting C-50 or C-51.
Anticipated: 295/325 (C-50 fails -- prose index; C-51 fails -- protocol not document-first;
C-52, C-53, C-54 not reachable).

**C-47 form**: Full Why: in C-41 prose entries with INERTIA CONTRAST PROTOCOL naming.
**C-48 form**: Per-entry back-refs ending with `(rule declared in INERTIA CONTRAST PROTOCOL above)`.
**C-49 form**: `## INERTIA CONTRAST PROTOCOL`; BAD PLAN header:
  `# INERTIA CONTRAST PROTOCOL -- Component 1: Header Entry Index`; footer:
  `# INERTIA CONTRAST PROTOCOL -- Component 3: Exit Verification complete`.
**C-50, C-51**: Not targeted.
**C-54**: Not reachable.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**The inertia path:** A team without a program plan opens the skill catalog, picks skills that
seem relevant, groups them loosely by namespace, and calls the grouping a plan. Gates become
task-completion checks. Investigative intent disappears. The artifact documents what was run,
not what was learned. Every step below is a direct counter-move against a specific inertia
action.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Inertia failure when absent |
|-------|--------------------------|----------------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to | Namespace buckets replace zones; skills cluster by catalog proximity, not investigation logic |
| **Artifact provenance** | Which stage produced each gated artifact, at what count | Gates become prose: "review complete" rather than `review-design >= 2 artifacts present` |
| **Investigative intent** | What question each phase answers | Phases have no question; the plan is a skill execution sequence, not an investigation |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## INERTIA CONTRAST PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.
The BAD PLAN is the inertia path instantiated: it shows exactly what the catalog-first failure
mode produces as a concrete artifact. Read the protocol architecture before construction.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Each entry names: field type, criterion, exact tag
string with full unabbreviated `Why:` where applicable, and a back-reference to this section.
The header affirmatively covers all 7 criteria (C-38).

Entry form:
```
# C-XX: <field type> carries <exact tag string with full Why: if applicable>
#       (rule declared in INERTIA CONTRAST PROTOCOL above)
```

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line. Each tagged field is a named
inertia artifact: what the catalog-first path produces at that slot.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types found present in the block body.

**Navigation contract (C-45 + C-48)**: This section (INERTIA CONTRAST PROTOCOL) is the
governing declaration. The FIELD CO-LOCATION PRINCIPLE section below carries per-row
forward-refs to specific Component 1 entry numbers in the BAD PLAN header.

---

**Compound gate format:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

**Inertia gate:** `"done"` or `"complete"` -- these are execution-history checks, not
artifact-verifiable states. The inertia path produces these because it does not track artifact
counts; it tracks task completion.

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

Read all steps before beginning Step 1. Each step header names the inertia action it prevents.

1. Declare the topic (Step 1) -- inertia: skip, topic is implicit
2. Declare arc phases before catalog -- **catalog closed until Step 3** (Step 2) -- inertia: open catalog first, derive phases from skill clusters
3. Select skills from catalog (Step 3) -- inertia: already done at Step 1, catalog-first
4. Assign skills to declared phases (Step 4) -- inertia: phases are skill containers, not investigation frames
5a. Design gates: compound lineage prefix format (Step 5a) -- inertia: gate = "done"
5b. FORWARD REFERENCE audit (Step 5b) -- inertia: skip, gates are not artifact-traceable anyway
6. Write per-phase intent questions: interrogative form required (Step 6) -- inertia: omit, there is no question
7. Encode `evidence_arc:` field (Step 7) -- inertia: omit, no arc declared
8. Assemble YAML: produce ARTIFACT 2 first (Step 8) -- inertia: assemble YAML directly from skill list
9. Per-stage compliance table (Step 9) -- inertia: skip, no compliance frame
10. Terminal checklist (Step 10) -- inertia: skip, done when YAML is written

Do not proceed to Step 3 until Step 2 is complete. Opening the catalog before Step 2 is the
single inertia action that produces every downstream failure.

---

#### Step 1 -- Topic

**Inertia action prevented:** skipping topic declaration and treating the plan as generic.

State the topic name. All artifact names, phase groupings, and gate artifact types must be
coherent with this specific topic. A generic plan with no topic anchor is the inertia output.

---

#### Step 2 -- Declare Arc Phases

**Inertia action prevented:** opening the catalog and deriving phases from skill namespace clusters.

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first
principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`. Phase names must
describe investigation intent, not namespace labels.

| Phase label | Zone | Investigative question (ends with ?) | Inertia equivalent (FAIL) |
|-------------|------|--------------------------------------|---------------------------|
| [name] | breadth/depth/synthesis | [...?] | `scout_and_draft_stage` (namespace bucket) |

- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage` -- names namespaces, not investigation; `listen_phase` -- namespace label

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
Inertia failure: # Produces: authored from current stage skill knowledge (producer-push misreading).
Derivation runs backward from echo; annotations are transcribed, not invented.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Inertia failure: echo placed last as execution
terminus. Row 0 is derivation anchor, not execution position.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

**Inertia action prevented:** selecting all skills from all namespaces indiscriminately.

Open the catalog now. Select only skills relevant to the topic and the declared phases. For
each skill, confirm it maps to a declared phase -- not that it seems useful in general.

---

#### Step 4 -- Assign Skills to Phases

**Inertia action prevented:** creating new phases to accommodate skills that have no declared home.

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.
Inertia output: every skill finds a phase because phases are created on demand to hold them.

---

#### Step 5a -- Design Gates

**Inertia action prevented:** writing `gate: "done"` as the execution-state completion check.

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

| Form | Verdict | Inertia diagnosis |
|------|---------|-------------------|
| `discovery::scout-feasibility >= 3 AND scout:market artifact exists` | PASS | artifact-verifiable, stage-prefixed, quantified |
| `"done"` | FAIL C-04 | inertia gate: execution-history check; no artifact named |
| `"all tasks complete"` | FAIL C-04 | inertia gate: task-completion language; not verifiable by inspection |
| `>= 3 scout artifacts` | FAIL C-04 | threshold without stage-id prefix; provenance lost |

At least one gate across all non-echo stages must include `>= N`. A plan with zero quantified
thresholds has reverted to inertia gate logic even if the gate language avoids "done."

---

#### Step 5b -- FORWARD REFERENCE Audit

**Inertia action prevented:** leaving gate artifact types that no skill in the stage produces.

For each non-echo stage: verify every artifact type in the gate is producible by at least one
skill in that stage's `skills` array. Fix all forward references before Step 6. The inertia
path skips this because its gates do not reference artifacts at all.

---

#### Step 6 -- Phase Intent Questions

**Inertia action prevented:** omitting intent questions entirely or using imperative task descriptions.

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL -- inertia: `"Assess the compliance landscape"` -- task description, not investigation question
- FAIL -- inertia: `"Are we ready to proceed?"` -- scope-generic; not tied to this phase's investigation

---

#### Step 7 -- Evidence Arc Field

**Inertia action prevented:** omitting the arc declaration; leaving zone membership implicit in stage order.

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML

**Inertia action prevented:** assembling YAML directly from the skill list without a trace matrix.

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

**Inertia action prevented:** skipping post-assembly verification; delivering an unchecked plan.

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` genuine interrogative? | Inertia flag |
|-------|---------------------------------------|-------------------------------------|----------------------------------|--------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | [name inertia if NO] |

Any NO triggers revision. Name the specific inertia action that produced the NO.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; program: top-level key; stages: list present
[ ] C-02: echo is last; auto: true; skills: []; no gate field
[ ] C-03: all skills from catalog; no invented names (inertia: invented names look plausible)
[ ] C-04: every non-echo gate is artifact-verifiable (inertia: "done", "complete", "all tasks finished")
[ ] C-05: namespace ordering respected (inertia: skills placed by namespace proximity, not dependency)
[ ] C-06: stage names describe investigative purpose (inertia: namespace labels used as stage names)
[ ] C-07: plan framed as signal-gathering artifact (inertia: plan written as executor script)
[ ] C-08: at least one quantified gate threshold (inertia: zero thresholds, all prose gates)
[ ] C-09 through C-49: all aspirational criteria
[ ] C-47: gate_fail: C-41 entry includes full unabbreviated Why: (not Why: ...)
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as INERTIA CONTRAST PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate
[ ] C-51: named protocol section is document-first -- NO for this variate
[ ] C-52: NOT REACHABLE (requires C-50 and C-51)
[ ] C-53: NOT REACHABLE (requires C-52)
[ ] C-54: NOT REACHABLE (requires C-53)
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
exact field line. This is the INERTIA CONTRAST PROTOCOL co-location family (see INERTIA
CONTRAST PROTOCOL section above for the full protocol declaration). Tagged wrong fields are
inertia artifacts -- what the catalog-first path produces at each slot:

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in INERTIA CONTRAST PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in INERTIA CONTRAST PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in INERTIA CONTRAST PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07): the inertia path instantiated

```yaml
# INERTIA CONTRAST PROTOCOL -- Component 1: Header Entry Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
# This block is the catalog-first failure mode as a concrete artifact.
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in INERTIA CONTRAST PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in INERTIA CONTRAST PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in INERTIA CONTRAST PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in INERTIA CONTRAST PROTOCOL above)

stages:                              # WRONG C-01: inertia output -- missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: inertia stage name -- namespace label, not investigation intent
    skills:
      - gather-requirements          # WRONG C-03: inertia skill name -- invented, not in Signal catalog
      - make-a-plan                  # WRONG C-03: inertia skill name -- invented, not in Signal catalog
    gate_fail: "done"                # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review           # WRONG C-06: inertia stage name -- namespace cluster label
    # WRONG C-05: inertia dependency violation -- review:design before any draft:spec stage
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: inertia skill name -- invented, not in Signal catalog
    gate_fail: "complete"            # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: inertia echo violation -- missing auto: true; skills list is non-empty
    skills:
      - listen:adoption
    # WRONG C-07: inertia framing violation -- no strategy:, purpose:, or plan-identity element

# INERTIA CONTRAST PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header entry index confirmed present in block above.
# Every tagged field above is the inertia path instantiated at that slot.
```

---

## V-04 -- Exclusion-Boundary Architecture Axis (EXCLUSION-BOUNDARY PROTOCOL)

**Axis**: Single-axis variation on exclusion-boundary architecture. The C-54 negative boundary
pattern -- enumerating forbidden alternatives by name before stating the positive rule -- is
applied globally as a design philosophy across all major requirements. Every requirement with
a well-defined exclusion set opens with "NOT: [X, Y, Z]" before "IS: [A]." This applies to
stage names, gate forms, skill names, echo structure, and plan framing -- not only to the
Component 1 table format. The architecture makes the design space bounded and directly
checkable at every field.

**Hypothesis**: The C-54 negative boundary pattern derives its teaching power from making each
forbidden category individually disqualified and checkable. Applied globally, it converts every
requirement from a one-sided positive rule ("must be X") into a bounded design statement
("must be X; these named alternatives are violations"). A model self-reviewing against named
exclusions can confirm no violation category applies rather than only confirming the positive
form is present. Not targeting C-50 or C-51.
Anticipated: 295/325 (C-50 fails -- prose index; C-51 fails -- protocol not document-first;
C-52, C-53, C-54 not reachable through chain).

**Exclusion-boundary form per requirement type:**
- Stage names: NOT [namespace labels, generic numbers, task descriptions] / IS [investigation-intent labels]
- Gate values: NOT [done, complete, execution phrases] / IS [artifact-state conditions with stage-id prefix]
- Skill names: NOT [invented names, namespace-only entries, plain English] / IS [catalog-qualified names]
- Echo structure: NOT [skills listed, auto missing, non-terminal position] / IS [empty skills, auto:true, terminal]
- Plan framing: NOT [executor script, task list, run-order] / IS [signal-gathering artifact with strategy]

**C-47, C-48, C-49 form**: standard protocol entries with EXCLUSION-BOUNDARY PROTOCOL naming.
**C-50, C-51**: Not targeted.
**C-54**: Not reachable through rubric chain (requires C-53 which requires C-52 which requires C-51).
Note: the exclusion-boundary architecture as a global design philosophy IS the spirit of C-54
applied outside the protocol scope; C-54 specifically measures the protocol section's column mandate.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Design philosophy -- exclusion boundary:** Every requirement below states what is forbidden
before stating what is required. Named exclusions make the design space bounded: each forbidden
category is individually checkable. Self-review: confirm your output matches none of the named
forbidden forms, then confirm it satisfies the positive requirement.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Forbidden absence forms |
|-------|--------------------------|------------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to | Stage names as namespace labels; phases derived from catalog proximity |
| **Artifact provenance** | Which stage produced each gated artifact, at what count | Gates as execution checks: "done", "complete", "all tasks finished" |
| **Investigative intent** | What question each phase answers, interrogative | Imperative task descriptions; scope-generic readiness checks |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## EXCLUSION-BOUNDARY PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Each entry names: field type, criterion, exact tag
string with full unabbreviated `Why:` where applicable, and a back-reference to this section.
The header affirmatively covers all 7 criteria (C-38).

Entry form:
```
# C-XX: <field type> carries <exact tag string with full Why: if applicable>
#       (rule declared in EXCLUSION-BOUNDARY PROTOCOL above)
```

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types found present in block body.

**Navigation contract (C-45 + C-48)**: This section (EXCLUSION-BOUNDARY PROTOCOL) is the
governing declaration. The FIELD CO-LOCATION PRINCIPLE section below carries per-row
forward-refs to specific Component 1 entry numbers in the BAD PLAN header.

---

**Gate value exclusion boundary:**

Gate is NOT: `"done"`, `"complete"`, `"all tasks finished"`, `"skills executed"`, `"proceed"`,
or any execution-state phrase. These are forbidden gate forms.

Gate IS: `{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists`
- `{stage-id}` must match `name:` exactly
- `>= N` quantified threshold required
- `{namespace}:{skill}` artifact reference required

---

**Stage name exclusion boundary:**

Stage name is NOT: a namespace label (`scout`, `draft`, `review`), a namespace cluster
(`scout_and_draft`, `prove_and_review`), a generic phase label (`stage-1`, `phase-A`), or
a task description (`gather-data`, `run-reviews`). These are forbidden stage name forms.

Stage name IS: an investigation-intent label describing what question the phase answers
(`discovery`, `stress-test`, `signal-watch`).

---

**Skill name exclusion boundary:**

Skill entry is NOT: an invented name (`gather-requirements`, `make-a-plan`, `run-analysis`),
a namespace-only entry (`scout:`, `review:`), or a plain English description. These are
forbidden skill name forms.

Skill entry IS: a namespace-qualified name from the Signal plugin catalog.

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

---

**Echo exclusion boundary:**

Echo is NOT: a stage with skills listed, a stage missing `auto: true`, a stage in non-terminal
position, or a stage named anything other than `echo`. These are forbidden echo forms.

Echo IS:
```yaml
- name: echo
  auto: true
  skills: []
```
placed as the final stage in `stages:`.

---

**Plan framing exclusion boundary:**

The plan is NOT: an executor script, a task checklist, a run-order sequence, or a list of
skills to execute in order. These are forbidden framing forms.

The plan IS: a signal-gathering artifact for a human decision-maker, framed with a `strategy:`
field explaining why the feature is worth the investment.

---

## CONSTRUCTION ORDER

Read all steps before beginning Step 1.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: use gate IS form above, not gate NOT forms (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe (Step 8)
9. Per-stage compliance table with exclusion-boundary self-check (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.**

Declare 3--6 phase boundaries from first principles. Apply stage name exclusion boundary:
names are NOT namespace labels; names ARE investigation-intent labels.

| Phase label | Zone | Investigative question (ends with ?) | Excluded form |
|-------------|------|--------------------------------------|---------------|
| [name] | breadth/depth/synthesis | [...?] | [namespace cluster this is NOT] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: is NOT authored from current stage's skill knowledge.
# Produces: IS set by what the NEXT stage declares as # Consumes:
Derivation runs backward from echo.

ROW-0 RULE: Echo is NOT execution terminus. Echo IS derivation anchor at row 0 of ARTIFACT 2.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Apply skill name exclusion boundary: select only catalog-qualified names.
Do NOT invent names. Do NOT use namespace-only entries.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. Do NOT create new phases. Skills with no matching phase
are discarded.

---

#### Step 5a -- Design Gates

Apply gate value exclusion boundary at every non-echo stage. Use the three-field gate structure:

```
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [dep zones only, zone header]
name: <phase-label>                    # NOT: namespace label, namespace cluster, generic label
...
# requires: <artifact> from Zone: <prior-zone-name> (C-05)   [dep zones only, skills line]
skills:                                # check correction table: skill names
  - <namespace>:<skill>                # NOT: invented name / NOT: namespace-only
gate_fail: "<forbidden gate form>"     # WRONG C-04: Why: execution-history check, not artifact-verifiable
gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
```

Gate NOT forms: `"done"`, `"complete"`, `"all tasks finished"` -- each individually forbidden.
Gate IS form: `{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists`.

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify gate artifact types are producible by skills in that stage. Fix before Step 6.

---

#### Step 6 -- Phase Intent Questions

Intent question is NOT: an imperative task description, a scope-generic readiness check.
Intent question IS: an interrogative sentence ending with `?` tied to this phase's investigation.

- NOT: `"Assess the compliance landscape"` (imperative, not interrogative)
- NOT: `"Are we ready to proceed?"` (scope-generic, not phase-specific)
- IS: `"Do we understand the compliance landscape well enough to commit to a direction?"`

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
  - name: <phase-label>                    # NOT: namespace label -- IS: investigation intent; check correction table
    phase: <arc-key>
    intent: "<question ending with ?>"     # NOT: imperative -- IS: interrogative, phase-specific
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:                                # requires: <artifact> from Zone: <name> (C-05)  [dep zones]
                                           # NOT: invented names -- IS: catalog-qualified; check correction table
      - <namespace>:<skill>
    gate_fail: "<forbidden gate form>"     # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate:      "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"  # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true
    skills: []  # REQUIRED: empty
```

---

#### Step 9 -- Per-Stage Compliance Table (Exclusion-Boundary Self-Check)

For each stage, apply both the exclusion boundary (confirm NOT forms absent) and the positive
requirement (confirm IS form present):

| Stage | Gate NOT form absent? | Gate IS form present? | Stage name NOT forbidden? | Stage name IS intent label? |
|-------|----------------------|-----------------------|--------------------------|----------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO | YES / NO |

Any NO triggers revision. Name the specific forbidden form found.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01: YAML valid; program: top-level key; stages: list present
[ ] C-02: echo IS last, auto: true, skills: []; echo NOT: skills listed, auto missing, non-terminal
[ ] C-03: all skills IS catalog-qualified; NOT: invented names, namespace-only entries
[ ] C-04: all gates IS artifact-state; NOT: "done", "complete", "all tasks finished", execution phrases
[ ] C-05: namespace ordering IS respected; NOT: dependency-violating placement
[ ] C-06: stage names IS investigation-intent labels; NOT: namespace labels, namespace clusters, generic labels
[ ] C-07: plan IS signal-gathering artifact with strategy:; NOT: executor script, task checklist
[ ] C-08: at least one quantified gate threshold (>= N) present
[ ] C-09 through C-49: all aspirational criteria
[ ] C-47: gate_fail: C-41 entry includes full unabbreviated Why: (not Why: ...)
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as EXCLUSION-BOUNDARY PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate (prose entries)
[ ] C-51: named protocol section is document-first -- NO for this variate
[ ] C-52: NOT REACHABLE (requires C-50 and C-51)
[ ] C-53: NOT REACHABLE (requires C-52)
[ ] C-54: NOT REACHABLE through rubric chain (requires C-53); exclusion-boundary architecture
          IS the C-54 design philosophy applied globally -- C-54 rubric criterion specifically
          measures the protocol section column mandate, not global application
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
exact field line. This is the EXCLUSION-BOUNDARY PROTOCOL co-location family (see
EXCLUSION-BOUNDARY PROTOCOL section above for the full protocol declaration):

| Field type | Criterion | Forbidden forms (NOT) | Required tag (IS) | Co-location rule | BAD PLAN entry |
|------------|-----------|----------------------|-------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | execution-state strings | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in EXCLUSION-BOUNDARY PROTOCOL C1 below |
| `name:` | C-06 (C-37) | namespace labels, clusters | `# WRONG C-06` | At name: line | Entry (2) in EXCLUSION-BOUNDARY PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | invented names, ns-only | `# WRONG C-03` | At skills-list entry line | Entry (3) in EXCLUSION-BOUNDARY PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# EXCLUSION-BOUNDARY PROTOCOL -- Component 1: Header Entry Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in EXCLUSION-BOUNDARY PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in EXCLUSION-BOUNDARY PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in EXCLUSION-BOUNDARY PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in EXCLUSION-BOUNDARY PROTOCOL above)

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: forbidden form -- namespace cluster label
    skills:
      - gather-requirements          # WRONG C-03: forbidden form -- invented name, not in catalog
      - make-a-plan                  # WRONG C-03: forbidden form -- invented name, not in catalog
    gate_fail: "done"                # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"

  - name: prove_and_review           # WRONG C-06: forbidden form -- namespace cluster label
    # WRONG C-05: forbidden dependency -- review:design before any draft:spec stage has run
    skills:
      - review:design
      - run-analysis                 # WRONG C-03: forbidden form -- invented name, not in catalog
    gate_fail: "complete"            # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"
    gate: "complete"

  - name: echo
    # WRONG C-02: forbidden echo form -- missing auto: true; skills: list non-empty
    skills:
      - listen:adoption
    # WRONG C-07: forbidden framing -- no strategy:, purpose:, or plan-identity element

# EXCLUSION-BOUNDARY PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header entry index confirmed present in block above.
```

---

## V-05 -- Combined Axis (C-50 + C-51 + C-52 + C-53 + C-54: Full Chain)

**Axis**: Combined variation targeting all five criteria in the C-50-through-C-54 chain
simultaneously. The BOUNDED BLOCK PROTOCOL section appears FIRST (C-51). The protocol section
uses prescriptive MUST/SHALL directive language to mandate that Component 1 is a 4-column
pipe-delimited table, naming all four columns by purpose (C-52 + C-53). The mandate explicitly
enumerates forbidden alternative formats by name: "prose enumeration, indented list, bulleted
entries" (C-54). The BAD PLAN header implements the mandated table format (C-50).

**Hypothesis**: C-54 requires the C-53 prescriptive mandate to close in the negative direction
by naming forbidden alternatives individually, converting the mandate from one-sided positive
("must be X") into a bounded design space ("must be X; these named alternatives are violations").
R17 V-05 already contained the necessary text ("Any other format (prose enumeration, indented
list, bulleted entries) is a protocol violation"). R18 V-05 confirms this and strengthens the
negative boundary by: (a) presenting each forbidden form as a separately named item in an
inline list rather than a parenthetical, and (b) adding a self-review diagnostic step after
the column mandate that explicitly invokes the exclusion list.
Anticipated: 325/325 (all five chain criteria pass).

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag
string with full Why: | C-42 back-ref per row.
**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before three-class table, lifecycle zones,
catalog, and construction steps. Only a single opening sentence precedes it.
**C-52 form**: Protocol section explicitly names all four column purposes before the BAD PLAN
block: "Column 1: field type; Column 2: criterion; Column 3: exact tag string including full
Why: where applicable; Column 4: per-row C-42 back-reference."
**C-53 form**: Protocol section uses MUST directive language for the column mandate: "Component 1
MUST be a 4-column pipe-delimited table." Prescriptive, not descriptive.
**C-54 form**: Prescriptive mandate names forbidden alternatives individually: "Forbidden formats
for Component 1: prose enumeration, indented list, bulleted entries. Each of these formats is
individually disqualified." Self-review step: "Before proceeding, confirm your Component 1 is
NOT a prose enumeration, NOT an indented list, and NOT a bulleted entry set."

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

Component 1 MUST be a 4-column pipe-delimited table. Forbidden formats for Component 1:
prose enumeration, indented list, bulleted entries. Each of these formats is individually
disqualified -- they do not satisfy the structured column requirement regardless of content
completeness. The four columns are mandatory:

| Column | Purpose | Criteria satisfied |
|--------|---------|-------------------|
| Column 1: Field type | Which YAML field carries the annotation -- gate_fail:, name:, skills: entry, or this header | C-41 |
| Column 2: Criterion | Criterion number governing that field -- C-04 (C-26), C-06 (C-37), C-03 (C-39), C-38 | C-41 |
| Column 3: Exact tag string | The annotation string as it appears at the field, including full unabbreviated Why: clause where applicable | C-44 + C-47 |
| Column 4: C-42 back-ref | Per-row reference to this protocol section by name | C-48 |

Self-review step for Component 1: Before completing the BAD PLAN block header, confirm:
- Your Component 1 is NOT a prose enumeration (entries in running sentences)
- Your Component 1 is NOT an indented list (entries as `# - item:` lines without columns)
- Your Component 1 is NOT a bulleted entry set (entries as `# * item:` lines without columns)
- Your Component 1 IS a pipe-delimited table with the four columns above

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
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name
          (prose enumeration, indented list, bulleted entries) -- YES
          Self-review step present in protocol section -- YES
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
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                         | C-42 back-ref                      |
# |---------------|---------------|-------------------------------------------------------------------------------|------------------------------------|
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
