---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 20
rubric: v20
rubric_date: 2026-03-16
total_pts: 350
golden_threshold: 80
qu5: true
source_variate: V-05
---

# program-plan -- QU5 Simplified Golden Prompt (V-05 Base)

QU5 simplification of V-05 (BOUNDED BLOCK PROTOCOL, all three new criteria: C-57+C-58+C-59).
Goal: 20-40% word reduction with zero essential criteria lost (C-01 through C-07).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer; all Produces/Consumes derivation runs backward from echo.

---

## BOUNDED BLOCK PROTOCOL

The BAD PLAN block at the end is a bounded teaching unit. Two document-wide disciplines apply: (1) **active verification** -- every step with constraints carries a SELF-VERIFY block; (2) **mandate echo saturation** -- every constrained YAML template field echoes its mandate and NOT list at the field position.

**Component 1 -- Header Index: FORMAT REQUIREMENT**

Component 1 MUST be a 4-column pipe-delimited table. Forbidden formats:
- prose enumeration (entries as running sentences or paragraphs)
- indented list (entries as `# - item:` lines without column alignment)
- bulleted entries (entries as `# * item:` lines without pipe columns)

The four columns are mandatory and must appear in this order:

| Column | Purpose | Criteria satisfied |
|--------|---------|-------------------|
| Column 1: Field type | YAML field carrying the annotation | C-41 |
| Column 2: Criterion | Governing criterion number | C-41 |
| Column 3: Exact tag string | Annotation as it appears at the field; full unabbreviated Why: | C-44 + C-47 |
| Column 4: C-42 back-ref | Per-row reference to this BOUNDED BLOCK PROTOCOL section | C-48 |

**Active verification -- run before completing Component 1 (C-55):**
- NOT a prose enumeration (entries in running sentences)
- NOT an indented list (entries as `# - item:` lines without columns)
- NOT a bulleted entry set (entries as `# * item:` lines without columns)
- IS a pipe-delimited table with the four columns above

The header table MUST affirmatively claim full-criterion coverage of all 7 criteria (C-38).

**Universal active verification (C-58):** The same NOT/IS confirmation pattern applies to every construction step below that declares constraints. Each step's SELF-VERIFY block is mandatory.

**Field saturation mandate (C-59):** Every YAML template field that carries a format constraint echoes its governing mandate and NOT list inline at the field position in the Step 8 schema.

**Component 2 -- Block Body:** Wrong YAML with criterion tags at every violating field line. Tags MUST match Component 1 Column 3 strings exactly.

**Component 3 -- Exit Verification:** Footer confirming all Component 1 annotation types were found present in the block body.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration; the BAD PLAN block below is the bounded instance.
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 table rows.

---

**Lifecycle zones** (assign each phase to one):
- **Breadth** -- problem-space understanding before committing to direction; scout and draft skills.
- **Depth** -- adversarial stress-test before shipping; prove, review, flow, trace skills.
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

---

## CONSTRUCTION ORDER

1. Declare the topic
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3**
3. Select skills from catalog
4. Assign skills to declared phases
5a. Design gates: compound lineage prefix format, at least one quantified
5b. FORWARD REFERENCE audit
6. Write per-phase intent questions: interrogative form required
7. Encode `evidence_arc:` field
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe using the field-saturated schema
9. Per-stage compliance table
10. Terminal checklist

---

#### Step 1 -- Topic

State the topic name.

**SELF-VERIFY before proceeding:**
- NOT: topic left implicit or generic ("feature", "project", "new capability")
- IS: a specific topic name stated

---

#### Step 2 -- Declare Arc Phases

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries from first principles. Assign each to a zone: `breadth`, `depth`, or `synthesis`.

| Phase label | Zone | Investigative question (ends with ?) |
|-------------|------|--------------------------------------|
| [name] | breadth/depth/synthesis | [...?] |

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: set by next stage's # Consumes: (backward derivation from echo)
ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2.
```

**SELF-VERIFY before proceeding:**
- NOT: any phase name that is a namespace label, cluster, or generic identifier (`scout`, `scout_and_draft`, `stage-1`)
- IS: every phase name describes investigation intent (`discovery`, `stress-test`, `signal-watch`)

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic and the declared phases.

**SELF-VERIFY before proceeding:**
- NOT: any invented skill name not in the catalog (`gather-requirements`, `make-a-plan`, `run-analysis`)
- NOT: any namespace-only entry (`scout:`, `review:`, `flow:`)
- IS: every selected skill is namespace-qualified from the catalog above

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases. Discard unmatched skills.

**SELF-VERIFY before proceeding:**
- NOT: new phases created to accommodate unmatched skills
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

**SELF-VERIFY before proceeding:**
- NOT: any gate using execution-state language (`"done"`, `"complete"`, `"all tasks finished"`)
- NOT: any gate without a stage-id prefix matching `name:` exactly
- NOT: any gate with zero quantified thresholds (`>= N` absent from all gates)
- IS: every non-echo gate is artifact-state, stage-id prefixed, with at least one `>= N` threshold

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every gate artifact type is producible by a skill in that stage's `skills` array. Fix before Step 6.

**SELF-VERIFY before proceeding:**
- NOT: any gate referencing an artifact type that no skill in that stage produces
- IS: every gate artifact type is traceable to a skill in the same stage

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL (imperative): `"Assess the compliance landscape"`
- FAIL (generic): `"Are we ready to proceed?"`

**SELF-VERIFY before proceeding:**
- NOT: any intent value that is an imperative task description (`"Assess X"`, `"Gather Y"`)
- NOT: any intent value that is scope-generic (`"Are we ready?"`, `"Is this done?"`)
- IS: every intent value is a genuine interrogative ending with `?` tied to that specific phase

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

**SELF-VERIFY before proceeding:**
- NOT: any phase label in `evidence_arc` not declared in Step 2
- NOT: a zone key absent from `evidence_arc` that has at least one assigned phase
- IS: every zone key maps exactly to its declared phases from Step 2

---

#### Step 8 -- Assemble YAML

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema -- field saturation: every constrained field echoes its mandate and NOT list (C-59):

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
  # Mandate (C-07): IS plan-identity framing / NOT: executor script / NOT: task list / NOT: empty
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    # Mandate (C-06): IS investigation-intent / NOT: namespace label (scout) / NOT: cluster (scout_and_draft) / NOT: generic (stage-1)
    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Mandate: IS interrogative ending with ? for this phase / NOT: imperative ("Assess X") / NOT: generic / NOT: missing ?
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
    # Mandate (C-03): IS namespace-qualified catalog names / NOT: invented (gather-requirements) / NOT: namespace-only (scout:)
    # requires: <artifact> from Zone: <name> (C-05)  [dep zones only]
    # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"
    # Mandate (C-04): IS artifact-state with stage-id:: prefix and >= N
    # NOT: "done" / NOT: "complete" / NOT: "all tasks finished" / NOT: any execution-history phrase
    # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    # Mandate (C-04): IS {stage-id}::{artifact-type} >= N / NOT: execution-state / NOT: missing stage-id:: / NOT: missing >= N
    # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true / NOT: false / NOT: absent
    skills: []  # REQUIRED: empty list / NOT: any skill entries
```

**SELF-VERIFY before proceeding:**
- NOT: echo has any skills listed
- NOT: echo is missing `auto: true`
- NOT: echo appears in any non-terminal position
- IS: echo is the final stage, has `skills: []`, has `auto: true`

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` genuine interrogative? |
|-------|---------------------------------------|-------------------------------------|----------------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

**SELF-VERIFY before proceeding:**
- NOT: any row with a NO that has not triggered revision
- IS: all rows show YES before advancing to Step 10

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
[ ] C-50: C-41 index is a 4-column pipe table -- YES
[ ] C-51: named protocol section is document-first -- YES
[ ] C-52: protocol section pre-declares column schema -- YES
[ ] C-53: column schema declaration uses prescriptive MUST language -- YES
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name -- YES
[ ] C-55: active NOT/IS verification checklist at declaration site -- YES
[ ] C-56: mandate echo with NOT list at Component 1 header -- YES
[ ] C-57: active NOT/IS checklist also echoed at Component 1 header (dual-site) -- YES
[ ] C-58: active NOT/IS verification at every constraint-bearing construction step -- YES
[ ] C-59: per-field mandate echo at every constrained YAML template field -- YES
```

---

## CORRECTION TABLE

| Wrong | Correct | Criterion |
|-------|---------|-----------|
| `gate: "done"` | `gate: "discovery::scout-feasibility >= 2 AND scout:market artifact exists"` | C-04 |
| `gate: "complete"` | `gate: "stress-test::review-design >= 2 AND trace:contract artifact confirmed"` | C-04 |
| `- gather-requirements` | `- scout:requirements` | C-03 |
| `- make-a-plan` | `- program:plan` | C-03 |
| `- scout:` (namespace only) | `- scout:feasibility` (qualified skill) | C-03 |
| `name: scout_and_draft` | `name: discovery` | C-06 |
| `name: prove_and_review` | `name: stress-test` | C-06 |
| `review:design` before `draft:spec` exists | `draft:spec` in earlier stage | C-05 |
| `listen:*` before any `flow:*` or `trace:*` | `flow:*` or `trace:*` in prior stage | C-05 |
| `"Execute all skills and proceed"` | `strategy:` field framing plan as signal artifact | C-07 |
| `program:` key missing | `program:` as top-level, `stages:` nested | C-01 |
| `echo` missing `auto: true` | `auto: true` on echo stage | C-02 |

---

## FIELD CO-LOCATION PRINCIPLE

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line (BOUNDED BLOCK PROTOCOL co-location family -- see above):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Row (1) in BOUNDED BLOCK PROTOCOL C1 table below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Row (2) in BOUNDED BLOCK PROTOCOL C1 table below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Row (3) in BOUNDED BLOCK PROTOCOL C1 table below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in BOUNDED BLOCK PROTOCOL C1 below

```yaml
# BOUNDED BLOCK PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
# Format: 4-column pipe table as mandated by BOUNDED BLOCK PROTOCOL above
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)
# Verify before finalizing this Component 1: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                                 | C-42 back-ref                      |
# |---------------|---------------|---------------------------------------------------------------------------------------|------------------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable                   | BOUNDED BLOCK PROTOCOL decl. above |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                          | BOUNDED BLOCK PROTOCOL decl. above |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                          | BOUNDED BLOCK PROTOCOL decl. above |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                           | BOUNDED BLOCK PROTOCOL decl. above |

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

# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header index confirmed present in block above.
```
