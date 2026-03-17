---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 19
rubric: v19
rubric_date: 2026-03-16
total_pts: 335
golden_threshold: 80
new_criteria: C-55, C-56
---

# program-plan -- R19 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v19 (C-01 through C-56, 49 aspirational criteria, 335 pts, golden: all essential pass AND composite >= 80).

**R18-2026-03-16 state under v19 rubric (C-55, C-56 added):**
- V-01 (SCAN PROTOCOL, 4-column table): C-50 PASS, C-51 FAIL → C-52 not reachable → C-55/C-56 not reachable -- ~305/335
- V-02 (BOUNDED BLOCK PROTOCOL first): C-51 PASS, C-50 FAIL → C-52 not reachable → C-55/C-56 not reachable -- ~305/335
- V-03 (INERTIA CONTRAST PROTOCOL): C-50 FAIL, C-51 FAIL → chain unreachable -- ~295/335
- V-04 (EXCLUSION-BOUNDARY PROTOCOL): C-50 FAIL, C-51 FAIL → chain unreachable -- ~295/335
- V-05 (BOUNDED BLOCK PROTOCOL first + full chain): C-50 PASS, C-51 PASS, C-52 PASS, C-53 PASS, C-54 PASS, C-55 PASS, C-56 PASS -- 335/335

**R19 design constraint:** V-01 maintains C-50. V-02 maintains C-51. V-03 and V-04 are new single-axis variants exploring universal application of C-55 (active verification) and C-56 (mandate echo) patterns respectively. V-05 must satisfy the full chain C-50+C-51+C-52+C-53+C-54+C-55+C-56 plus a potential C-57 signal: active verification echoed at the application site (dual-site active verification).

**C-55 canonical form (V-05 only):**
- The C-53/C-54 prescriptive mandate section includes an explicit self-review step enumerating forbidden formats as individually checkable NOT items followed by an IS confirmation
- Format: NOT a prose enumeration / NOT an indented list / NOT a bulleted entry set / IS a pipe-delimited table with the four columns

**C-56 canonical form (V-05 only):**
- Component 1 header echoes the C-53 mandate: `# Format: 4-column pipe table as mandated by [PROTOCOL] above`
- Component 1 header echoes the C-54 NOT list: `# (NOT prose enumeration / NOT indented list / NOT bulleted entries)`

**Variation axes for R19:**
- V-01 (carry-forward: output format): SCAN PROTOCOL with C-41 as 4-column pipe table confirming C-50
- V-02 (carry-forward: role sequence): BOUNDED BLOCK PROTOCOL first confirming C-51
- V-03 (new: universal verification axis): UNIVERSAL VERIFICATION PROTOCOL -- C-55 active NOT/IS verification pattern applied at every construction step, not just the Component 1 format mandate
- V-04 (new: mandate echo saturation axis): MANDATE ECHO SATURATION PROTOCOL -- C-56 co-location echo pattern applied to every YAML template field, not just the Component 1 header
- V-05 (combined: C-50+C-51+C-52+C-53+C-54+C-55+C-56 + dual-site active verification): BOUNDED BLOCK PROTOCOL first with full chain AND active verification echoed at both declaration site (C-55) and application site (Component 1 header, extending C-56)

---

## V-01 -- Output Format Axis (SCAN PROTOCOL -- 4-Column Table Index)

**Axis**: Single-axis variation on output format. The C-41 annotation-type index in the BAD PLAN header is a pipe-delimited markdown table with exactly 4 columns: field type, criterion, exact tag string with full Why: clause, and per-entry C-42 back-reference. SCAN PROTOCOL naming carried forward from R16-R18. C-50 confirmed. C-51 not targeted.

**Hypothesis**: A tabular C-41 index promotes each data type to an independently scannable column. A model returning to the index during block scanning looks up any column directly without re-parsing prose. C-50 satisfies the table format requirement; the SCAN PROTOCOL section provides the C-49 named protocol. C-51 not targeted -- SCAN PROTOCOL is not document-first. C-55/C-56 not reachable (require C-54, which requires C-52 requiring C-51).
Anticipated: 43/49 aspirational, 305/335.

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag string (with full `Why:` in column 3 for gate_fail:) | C-42 back-ref.
**C-47 form**: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` as column 3 value in the gate_fail: table row.
**C-48 form**: Column 4 per row: `SCAN PROTOCOL decl. above`; FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column: `Row (1) below`, `Row (2) below`, `Row (3) below`.
**C-49 form**: Section `## SCAN PROTOCOL`; BAD PLAN header label `# SCAN PROTOCOL -- C1: Header Index`; footer `# SCAN PROTOCOL -- C3: exit verified`.
**C-51**: Not targeted (SCAN PROTOCOL is not document-first).
**C-55, C-56**: Not reachable (require C-54 → C-53 → C-52 → C-51 -- chain broken at C-51).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before declaring arc phases. Result: zone membership is implicit; gates are prose checks; investigative intent disappears from the artifact.

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

Navigation contract (C-45 + C-48): This section (SCAN PROTOCOL) is the protocol declaration. The BAD PLAN C1 header below is the entry index. Each FIELD CO-LOCATION PRINCIPLE table row carries a per-row forward-reference to its specific C1 table row number. Each C1 table row carries this section as its back-ref (column 4).

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

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

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

For each non-echo zone, use the three-field gate structure. Dependency zones carry dual-position reminders in uniform syntax:

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

For each non-echo stage: verify every artifact type in the gate is producible by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently.

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
[ ] C-52: NOT REACHABLE (requires C-51)
[ ] C-53: NOT REACHABLE (requires C-52)
[ ] C-54: NOT REACHABLE (requires C-53)
[ ] C-55: NOT REACHABLE (requires C-54)
[ ] C-56: NOT REACHABLE (requires C-54)
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line -- not at an adjacent field, not in a header comment. This is the SCAN PROTOCOL co-location family (see SCAN PROTOCOL section above for the protocol declaration):

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

**Axis**: Single-axis variation on role sequence. The BOUNDED BLOCK PROTOCOL section appears FIRST in the prompt -- before the three-class information table, before lifecycle zones, before the catalog. A model reads the bounded-unit architecture before any construction guidance. C-47, C-48, C-49 carried forward. C-51 confirmed.

**Hypothesis**: Positioning the protocol architecture at the document's opening causes every subsequent section to be read through the protocol frame. The principle-before-instance architecture (C-51) ensures no section is read before the protocol that governs it. Anticipated: 43/49 aspirational, 305/335 (C-50 not reached -- C-41 index is prose enumeration; C-52, C-53, C-54, C-55, C-56 not reachable without C-50).

**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before the three-class table, lifecycle zones, catalog, and construction steps. Only a single opening sentence precedes it.
**C-47 form**: `Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable` with `(rule declared in BOUNDED BLOCK PROTOCOL above)` per entry.
**C-48 form**: Each C-41 entry ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)`; FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column: `See entry (1/2/3) in BAD PLAN header below`.
**C-49 form**: `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL -- Component 1: Header Entry Index`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification (C-46) complete`.
**C-50**: Not targeted (C-41 index is prose enumeration, not 4-column table).
**C-55, C-56**: Not reachable (require C-54 → C-53 → C-52 → C-50; C-50 absent).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit with three components. Understanding the protocol before construction prevents incomplete blocks.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Before reading any field in the block body, the header tells you: which field type carries which annotation, which criterion governs it, what the exact tag string looks like (including the full unabbreviated `Why:` clause where one exists), and where the governing rule is declared. Each entry has the form:

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

The block body contains wrong YAML. Every violating field carries its criterion tag at the exact field line. The FIELD CO-LOCATION PRINCIPLE section (below, after construction steps) declares this family principle.

**Component 3 -- Exit Verification (C-46)**

The block ends with an explicit footer confirming all annotation types from Component 1 were found present in the block body. This closes the bounded scan loop.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration. See the BAD PLAN block for the bounded instance implementing this protocol (Component 1 header below).
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 entry numbers in the BAD PLAN header.

---

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before declaring arc phases. Zone membership becomes implicit; gates become prose checks; investigative intent disappears from the artifact.

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

Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

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
[ ] C-52: NOT REACHABLE (requires C-50)
[ ] C-53: NOT REACHABLE (requires C-52)
[ ] C-54: NOT REACHABLE (requires C-53)
[ ] C-55: NOT REACHABLE (requires C-54)
[ ] C-56: NOT REACHABLE (requires C-54)
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. Three field types form the co-location family (BOUNDED BLOCK PROTOCOL Component 2 body rules; see BOUNDED BLOCK PROTOCOL section above for the full protocol):

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

## V-03 -- Universal Verification Axis (UNIVERSAL VERIFICATION PROTOCOL)

**Axis**: Single-axis variation on verification depth. The C-55 active NOT/IS verification pattern is applied universally -- every major authoring decision in the construction order ends with an explicit self-verify block that enumerates forbidden forms (NOT) and the required form (IS) for that step. Not just the Component 1 format mandate but arc phase naming, skill selection, gate design, echo structure, and intent questions each have a localized NOT/IS checklist that fires at the moment of authoring.

**Hypothesis**: C-55 derives its teaching power from converting static exclusions into per-item confirmation actions that fire AT generation time. Applied universally, every authoring step is bounded by an active checklist at the point of decision rather than at pre-generation reading. A model that self-checks after Step 2 catches wrong stage names before choosing skills; a model that self-checks after Step 5a catches bad gate forms before writing the YAML schema. Per-step verification prevents error propagation across steps. Not targeting C-50 or C-51 -- protocol section not document-first, C-41 index is prose.
Anticipated: 42/49 aspirational, 300/335 (C-50 FAIL, C-51 FAIL; chain C-52 through C-56 not reachable).

**C-49 form**: `## UNIVERSAL VERIFICATION PROTOCOL`; BAD PLAN header: `# UNIVERSAL VERIFICATION PROTOCOL -- Component 1: Header Entry Index`; footer: `# UNIVERSAL VERIFICATION PROTOCOL -- Component 3: Exit Verification complete`.
**C-47, C-48 form**: Standard prose entries with UNIVERSAL VERIFICATION PROTOCOL naming and per-entry back-refs.
**C-50**: Not targeted (prose index).
**C-51**: Not targeted (protocol section appears after opening framing, not document-first).
**C-55, C-56**: Not reachable through rubric chain (require C-54).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

**Design principle -- universal verification:** Every construction step in this protocol ends with a SELF-VERIFY block. Each block lists the forbidden output forms (NOT items) and the required output form (IS item) for that specific step. Run the NOT/IS checklist before proceeding to the next step. Catching violations step-by-step prevents error propagation.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Forbidden absence |
|-------|--------------------------|-------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to | Stage names derived from namespace clusters rather than investigation intent |
| **Artifact provenance** | Which stage produced each gated artifact, at what count | Gates as execution checks: "done", "complete", "all tasks finished" |
| **Investigative intent** | What question each phase answers, interrogative | Imperative task descriptions; scope-generic readiness checks |

**Lifecycle zones:**
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping commitment; prove, review, flow, trace skills.
- **Synthesis** -- post-launch signal monitoring; listen, metrics, goals skills.

---

## UNIVERSAL VERIFICATION PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Each entry names: field type, criterion, exact tag string with full unabbreviated `Why:` where applicable, and a back-reference to this section.

Entry form:
```
# C-XX: <field type> carries <exact tag string with full Why: if applicable>
#       (rule declared in UNIVERSAL VERIFICATION PROTOCOL above)
```

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types found present in the block body.

**Navigation contract (C-45 + C-48)**: This section (UNIVERSAL VERIFICATION PROTOCOL) is the governing declaration. The FIELD CO-LOCATION PRINCIPLE section below carries per-row forward-refs to specific Component 1 entry numbers in the BAD PLAN header.

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

Read all steps before beginning Step 1. Each step ends with a SELF-VERIFY block.

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete and the Step 2 SELF-VERIFY passes.

---

#### Step 1 -- Topic

State the topic name. All artifact names, phase groupings, and gate artifact types must be coherent with this specific topic.

**SELF-VERIFY after Step 1:**
- NOT: topic left implicit or generic ("feature", "project", "new capability")
- IS: a specific topic name stated that will anchor all subsequent artifact naming

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

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

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:
ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Derivation begins at row 0.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

**SELF-VERIFY after Step 2:**
- NOT: any phase name that is a namespace label (`scout`, `draft`, `review`, `flow`, `trace`)
- NOT: any phase name that is a namespace cluster (`scout_and_draft`, `prove_and_review`)
- NOT: any phase name that is a generic label (`stage-1`, `phase-A`, `step-one`)
- IS: every phase name describes investigation intent (`discovery`, `stress-test`, `signal-watch`)

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic and the declared phases.

**SELF-VERIFY after Step 3:**
- NOT: any invented skill name not in the catalog (`gather-requirements`, `make-a-plan`, `run-analysis`)
- NOT: any namespace-only entry (`scout:`, `review:`, `flow:`)
- IS: every selected skill is namespace-qualified from the catalog above

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases may be created. Discard skills with no matching phase.

**SELF-VERIFY after Step 4:**
- NOT: new phases created to accommodate unmatched skills
- NOT: skills placed in phases solely by namespace proximity rather than investigation match
- IS: every skill maps to a declared phase from Step 2; unmatched skills are discarded

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure. Dependency zones carry dual-position reminders in uniform syntax:

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

At least one gate across all non-echo stages must include `>= N`.

**SELF-VERIFY after Step 5a:**
- NOT: any gate using execution-state language (`"done"`, `"complete"`, `"all tasks finished"`, `"proceed"`)
- NOT: any gate without a stage-id prefix matching `name:` exactly
- NOT: any gate with zero quantified thresholds (`>= N` absent from all gates)
- IS: every non-echo gate is an artifact-state condition, stage-id prefixed, with at least one `>= N` threshold

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

**SELF-VERIFY after Step 5b:**
- NOT: any gate referencing an artifact type that no skill in that stage produces
- IS: every gate artifact type is traceable to a skill in the same stage

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess the compliance landscape"` -- imperative, not interrogative
- FAIL: `"Are we ready to proceed?"` -- scope-generic, not phase-specific

**SELF-VERIFY after Step 6:**
- NOT: any intent value that is an imperative task description (`"Assess X"`, `"Gather Y"`)
- NOT: any intent value that is scope-generic (`"Are we ready?"`, `"Is this done?"`)
- IS: every intent value is a genuine interrogative ending with `?` tied to that specific phase's investigation

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

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

**SELF-VERIFY after Step 8:**
- NOT: echo has any skills listed
- NOT: echo is missing `auto: true`
- NOT: echo appears in any non-terminal position
- IS: echo is the final stage, has `skills: []`, has `auto: true`

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
[ ] C-02: echo is last; auto: true; skills: []
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate
[ ] C-05: namespace ordering respected
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08: at least one quantified gate threshold (>= N)
[ ] C-09 through C-49: all aspirational criteria
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why:
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as UNIVERSAL VERIFICATION PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate (prose entries)
[ ] C-51: named protocol section is document-first -- NO for this variate
[ ] C-52 through C-56: NOT REACHABLE (require C-51 and C-50)
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. This is the UNIVERSAL VERIFICATION PROTOCOL co-location family (see UNIVERSAL VERIFICATION PROTOCOL section above for the full protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in UNIVERSAL VERIFICATION PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in UNIVERSAL VERIFICATION PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in UNIVERSAL VERIFICATION PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# UNIVERSAL VERIFICATION PROTOCOL -- Component 1: Header Entry Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in UNIVERSAL VERIFICATION PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in UNIVERSAL VERIFICATION PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in UNIVERSAL VERIFICATION PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in UNIVERSAL VERIFICATION PROTOCOL above)

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

# UNIVERSAL VERIFICATION PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header entry index confirmed present in block above.
```

---

## V-04 -- Mandate Echo Saturation Axis (MANDATE ECHO SATURATION PROTOCOL)

**Axis**: Single-axis variation on lifecycle emphasis. The C-56 mandate-echo-at-application-site pattern is applied to every YAML template field, not just the Component 1 header. Every template field that carries a criterion-testable value echoes its governing mandate inline at that field position: the `name:` placeholder echoes the stage name rule; the `skills:` placeholder echoes the catalog constraint; the `gate:` placeholder echoes the gate format rule; the `intent:` placeholder echoes the interrogative requirement. Every authoring decision is locally self-contained -- no cross-document recall required.

**Hypothesis**: C-56 applies co-location to the format mandate (one rule echoed at one application site). If every template field echoes its governing rule at its application position, the entire YAML template becomes a dense local rule set where each field simultaneously shows the placeholder and its constraint. A model filling any field encounters the mandate immediately, without referencing any rule section. This maximizes per-field compliance by saturating every application site with its governing rule. Not targeting C-50 or C-51.
Anticipated: 42/49 aspirational, 300/335 (C-50 FAIL, C-51 FAIL; chain C-52 through C-56 not reachable).

**C-49 form**: `## MANDATE ECHO SATURATION PROTOCOL`; BAD PLAN header: `# MANDATE ECHO SATURATION PROTOCOL -- Component 1: Header Entry Index`; footer: `# MANDATE ECHO SATURATION PROTOCOL -- Component 3: Exit Verification complete`.
**C-47, C-48 form**: Standard prose entries with MANDATE ECHO SATURATION PROTOCOL naming.
**C-50**: Not targeted (prose index).
**C-51**: Not targeted (protocol section appears mid-document, not first).
**C-55, C-56**: Not reachable through rubric chain.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

**Design principle -- mandate echo saturation:** Every YAML template field in this prompt carries an inline echo of its governing rule at the field position itself. No field requires cross-document lookup to know what is required. The governing rule is present where you fill the field.

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

## MANDATE ECHO SATURATION PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Each entry names: field type, criterion, exact tag string with full unabbreviated `Why:` where applicable, and a back-reference to this section.

Entry form:
```
# C-XX: <field type> carries <exact tag string with full Why: if applicable>
#       (rule declared in MANDATE ECHO SATURATION PROTOCOL above)
```

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types found present in the block body.

**Navigation contract (C-45 + C-48)**: This section (MANDATE ECHO SATURATION PROTOCOL) is the governing declaration. The FIELD CO-LOCATION PRINCIPLE section below carries per-row forward-refs to specific Component 1 entry numbers in the BAD PLAN header.

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
5a. Design gates (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML using the mandate-echo-saturated schema below (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 is complete.

---

#### Step 1 -- Topic

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage`, `prove_and_review_block`, `listen_phase`

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band, # Gap, # Owner, # Consumes, # Produces

Consumer-pull rule: # Produces: set by next stage's # Consumes: (backward derivation from echo)
ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Derivation begins at row 0.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic and declared phases.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard skills with no matching phase.

---

#### Step 5a -- Design Gates

For each non-echo zone, use the three-field gate structure with uniform dual-position dep reminders. At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify gate artifact types are producible by skills in that stage. Fix before Step 6.

---

#### Step 6 -- Phase Intent Questions

Intent must be interrogative and phase-specific:
- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess the compliance landscape"` (imperative) / `"Are we ready to proceed?"` (generic)

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML (Mandate-Echo-Saturated Schema)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema -- every field echoes its governing mandate at the field position (mandate echo saturation):

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
  # Mandate (C-07): IS a signal-gathering artifact framing statement -- NOT an executor script or task list
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    # Mandate (C-06): IS investigation-intent label -- NOT namespace label / NOT namespace cluster / NOT generic label
    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Mandate: IS genuine interrogative ending with ? tied to this phase -- NOT imperative / NOT scope-generic
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
    # Mandate (C-03): IS namespace-qualified catalog names -- NOT invented names / NOT namespace-only entries
    # requires: <artifact> from Zone: <name> (C-05)  [dep zones]
    # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"  # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    # Mandate (C-04): IS artifact-state with stage-id prefix and >= N -- NOT "done" / NOT "complete" / NOT execution phrases
    # check correction table: gate values
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
[ ] C-02: echo is last; auto: true; skills: []
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate
[ ] C-05: namespace ordering respected
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08: at least one quantified gate threshold (>= N)
[ ] C-09 through C-49: all aspirational criteria
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why:
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as MANDATE ECHO SATURATION PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate (prose entries)
[ ] C-51: named protocol section is document-first -- NO for this variate
[ ] C-52 through C-56: NOT REACHABLE (require C-51 and C-50)
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. This is the MANDATE ECHO SATURATION PROTOCOL co-location family (see MANDATE ECHO SATURATION PROTOCOL section above for the full protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in MANDATE ECHO SATURATION PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in MANDATE ECHO SATURATION PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in MANDATE ECHO SATURATION PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# MANDATE ECHO SATURATION PROTOCOL -- Component 1: Header Entry Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in MANDATE ECHO SATURATION PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in MANDATE ECHO SATURATION PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in MANDATE ECHO SATURATION PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in MANDATE ECHO SATURATION PROTOCOL above)

stages:                              # WRONG C-01: missing top-level program: key
  - name: scout_and_draft            # WRONG C-06: namespace-label, not investigative purpose
    # Mandate (C-06): IS investigation-intent -- NOT: namespace label (violated above)
    skills:
      - gather-requirements          # WRONG C-03: invented skill name, not in Signal catalog
      - make-a-plan                  # WRONG C-03: invented skill name, not in Signal catalog
    # Mandate (C-03): IS catalog-qualified -- NOT: invented names (violated above)
    gate_fail: "done"                # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "discovery::scout-feasibility >= 2 AND scout:requirements artifact present"
    gate: "done"
    # Mandate (C-04): IS artifact-state -- NOT: execution phrases (violated above)

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

# MANDATE ECHO SATURATION PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header entry index confirmed present in block above.
```

---

## V-05 -- Combined Axis (C-50+C-51+C-52+C-53+C-54+C-55+C-56 + Dual-Site Active Verification)

**Axis**: Combined variation targeting the full C-50-through-C-56 chain simultaneously, plus a potential C-57 signal: dual-site active verification. The BOUNDED BLOCK PROTOCOL section appears FIRST (C-51). The protocol section mandates that Component 1 MUST be a 4-column pipe-delimited table, names all four columns (C-52), uses MUST/SHALL directive language (C-53), enumerates forbidden alternative formats by name (C-54), and includes an explicit NOT/IS self-review checklist at the declaration site (C-55). The Component 1 header echoes the C-53 mandate and C-54 NOT list at the application site (C-56). The potential C-57 extension: the active NOT/IS verification checklist is ALSO echoed at the application site (Component 1 header) -- not just the static mandate and NOT list, but the full active per-item confirmation protocol.

**Hypothesis**: C-55 places the active verification step at the declaration site; C-56 echoes the mandate at the application site. The dual-site active verification extension echoes the active verification step itself at the application site, closing the loop: the model encounters the active NOT/IS checklist at BOTH the moment it reads the protocol (declaration site, C-55) AND the moment it fills Component 1 (application site, new). A model that skips the protocol section encounters the active checklist at the application site; a model that reads the protocol encounters it there first. Dual-site coverage eliminates the attention gap.
Anticipated: 49/49 aspirational, 335/335.

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag string (full Why: per C-47) | C-42 back-ref per row.
**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before three-class table, lifecycle zones, catalog, and construction steps.
**C-52 form**: Protocol section names all four columns: "Column 1: field type; Column 2: criterion; Column 3: exact tag string including full Why: where applicable; Column 4: per-row C-42 back-reference."
**C-53 form**: Protocol section uses MUST/SHALL directive language: "Component 1 MUST be a 4-column pipe-delimited table."
**C-54 form**: Prescriptive mandate names forbidden alternatives: "Forbidden formats: prose enumeration, indented list, bulleted entries. Each is individually disqualified."
**C-55 form**: Active NOT/IS verification checklist at declaration site: "Before completing Component 1: NOT a prose enumeration / NOT an indented list / NOT a bulleted entry set / IS a pipe-delimited table with the four columns."
**C-56 form**: Component 1 header echoes mandate and NOT list: `# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above` / `# (NOT prose enumeration / NOT indented list / NOT bulleted entries)`.
**Potential C-57 form**: Component 1 header ALSO echoes the active NOT/IS verification checklist: `# Verify before finalizing: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit. The protocol architecture below MUST be understood before any construction step begins. This section is the governing declaration for the block's structure, format, and verification requirements.

**Component 1 -- Header Index: FORMAT REQUIREMENT**

Component 1 MUST be a 4-column pipe-delimited table. Forbidden formats for Component 1:
- prose enumeration (entries written as running sentences or paragraphs)
- indented list (entries as `# - item:` or `#   item:` lines without column alignment)
- bulleted entries (entries as `# * item:` or `# - item:` lines without pipe columns)

Each of these formats is individually disqualified -- content completeness does not compensate for format non-compliance. The four columns are mandatory and must appear in this order:

| Column | Purpose | Criteria satisfied |
|--------|---------|-------------------|
| Column 1: Field type | Which YAML field carries the annotation -- `gate_fail:`, `name:`, `skills:` entry, or this header | C-41 |
| Column 2: Criterion | Criterion number governing that field -- C-04 (C-26), C-06 (C-37), C-03 (C-39), C-38 | C-41 |
| Column 3: Exact tag string | The annotation string as it appears at the field, including full unabbreviated Why: clause where applicable | C-44 + C-47 |
| Column 4: C-42 back-ref | Per-row reference to this BOUNDED BLOCK PROTOCOL section by name | C-48 |

**Active verification -- run before completing Component 1:**
- NOT a prose enumeration (entries in running sentences)
- NOT an indented list (entries as `# - item:` lines without columns)
- NOT a bulleted entry set (entries as `# * item:` lines without columns)
- IS a pipe-delimited table with the four columns above

The header table MUST affirmatively claim full-criterion coverage of all 7 criteria (C-38).

**Component 2 -- Block Body: FIELD CO-LOCATION REQUIREMENT**

The block body MUST contain wrong YAML. Every violating field SHALL carry its criterion tag at the exact field line -- not adjacent, not in a header comment. Field-level tags MUST match the tag strings specified in Component 1 Column 3.

**Component 3 -- Exit Verification: COMPLETION REQUIREMENT**

The block MUST end with an explicit footer confirming all annotation types from Component 1 were found present in the block body. This closes the bounded scan loop.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration. The BAD PLAN block below is the bounded instance.
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 table rows. Each Component 1 table row carries "BOUNDED BLOCK PROTOCOL decl. above" in column 4.

---

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before declaring arc phases. Zone membership becomes implicit; gates become prose checks; investigative intent disappears from the artifact.

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

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

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

For each non-echo zone, use the three-field gate structure. Dependency zones carry dual-position reminders in uniform syntax:

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

For each non-echo stage: verify every artifact type in the gate is producible by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently.

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
[ ] C-08: at least one gate with quantified threshold (>= N)
[ ] C-09 through C-49: all aspirational criteria
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: (not Why: ...)
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as BOUNDED BLOCK PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe table -- YES for this variate
[ ] C-51: named protocol section is document-first -- YES for this variate
[ ] C-52: protocol section pre-declares column schema using all four column names -- YES
[ ] C-53: column schema declaration uses prescriptive MUST/SHALL language -- YES
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name
          (prose enumeration, indented list, bulleted entries) -- YES
[ ] C-55: active NOT/IS verification checklist present at declaration site -- YES
          (NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table)
[ ] C-56: mandate echo with NOT list present at Component 1 header -- YES
          (# Format: 4-column pipe table as mandated... / # NOT list echoed)
[ ] Potential C-57: active NOT/IS checklist also echoed at Component 1 header (dual-site) -- YES
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. This is the BOUNDED BLOCK PROTOCOL co-location family (see BOUNDED BLOCK PROTOCOL section above for the full protocol declaration). The BAD PLAN C1 table below implements this family per the Component 1 format requirement stated in the protocol section:

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
# Verify before finalizing this Component 1: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns
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
