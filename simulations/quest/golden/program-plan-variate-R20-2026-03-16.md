---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 20
rubric: v20
rubric_date: 2026-03-16
total_pts: 350
golden_threshold: 80
new_criteria: C-57, C-58, C-59
---

# program-plan -- R20 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v20 (C-01 through C-59, 52 aspirational criteria, 350 pts, golden: all essential pass AND composite >= 80).

**R19-2026-03-16 state under v20 rubric (C-57, C-58, C-59 added):**
- V-01 (SCAN PROTOCOL, 4-column table): C-50 PASS, C-51 FAIL → C-52 not reachable → C-57/C-58/C-59 not reachable -- ~305/350
- V-02 (BOUNDED BLOCK PROTOCOL first): C-51 PASS, C-50 FAIL → C-52 not reachable → C-57/C-58/C-59 not reachable -- ~305/350
- V-03 (UNIVERSAL VERIFICATION PROTOCOL): C-50 FAIL, C-51 FAIL → chain unreachable -- ~295/350
- V-04 (MANDATE ECHO SATURATION PROTOCOL): C-50 FAIL, C-51 FAIL → chain unreachable -- ~295/350
- V-05 (BOUNDED BLOCK PROTOCOL full chain): C-50/C-51/C-52/C-53/C-54/C-55/C-56 PASS, C-57 PASS (dual-site active verify), C-58 FAIL (not present), C-59 FAIL (not present) -- ~340/350

**R20 design:** V-01 and V-02 carry their single-axis bases forward unchanged. V-03 and V-04 are new single-axis variants built on the V-05 R19 base (50/52), each adding one new criterion. V-05 adds all three new criteria simultaneously.

| Variate | Axis | New criteria targeted | Anticipated aspirational | Anticipated pts | Anticipated composite |
|---------|------|-----------------------|--------------------------|-----------------|----------------------|
| V-01 | Output format (carry-forward) | none | 43/52 | 215 | 305/350 |
| V-02 | Role sequence (carry-forward) | none | 43/52 | 215 | 305/350 |
| V-03 | Lifecycle emphasis: universal per-step verification | C-58 | 51/52 | 255 | 345/350 |
| V-04 | Phrasing register: per-field mandate echo saturation | C-59 | 51/52 | 255 | 345/350 |
| V-05 | Combined: all three new criteria | C-57+C-58+C-59 | 52/52 | 260 | 350/350 |

**Variation axes for R20:**
- V-01 (carry-forward: output format): SCAN PROTOCOL -- C-41 as 4-column pipe table (C-50). C-51 not targeted. C-57/C-58/C-59 not reachable (chain requires C-51).
- V-02 (carry-forward: role sequence): BOUNDED BLOCK PROTOCOL first (C-51). C-50 not targeted. C-57/C-58/C-59 not reachable (chain requires C-50).
- V-03 (new: lifecycle emphasis): COMPLETE VERIFICATION PROTOCOL -- C-55 active NOT/IS verification extended to every construction step (C-58). Built on V-05 R19 base (C-50+C-51+C-52+C-53+C-54+C-55+C-56+C-57 all present). One axis: universal per-step active verification.
- V-04 (new: phrasing register): FIELD SATURATION PROTOCOL -- C-56 mandate-echo-at-application-site extended to every constrained YAML template field (C-59). Built on V-05 R19 base. One axis: template-wide mandate echo saturation.
- V-05 (combined): BOUNDED BLOCK PROTOCOL -- V-05 R19 base + C-58 (universal per-step) + C-59 (template saturation). All three new criteria simultaneously.

---

## V-01 -- Output Format Axis (SCAN PROTOCOL -- 4-Column Table Index)

**Axis**: Single-axis variation on output format. The C-41 annotation-type index in the BAD PLAN header is a pipe-delimited markdown table with exactly 4 columns: field type, criterion, exact tag string with full Why: clause, and per-entry C-42 back-reference. SCAN PROTOCOL naming carried forward from R16-R19. C-50 confirmed. C-51 not targeted.

**Hypothesis**: A tabular C-41 index promotes each data type to an independently scannable column. A model returning to the index during block scanning looks up any column directly without re-parsing prose. C-50 satisfies the table format requirement; the SCAN PROTOCOL section provides the C-49 named protocol. C-51 not targeted -- SCAN PROTOCOL is not document-first. C-57/C-58/C-59 not reachable (require full chain through C-51).
Anticipated: 43/52 aspirational, 305/350.

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag string (with full `Why:` in column 3 for gate_fail:) | C-42 back-ref.
**C-47 form**: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` as column 3 value in the gate_fail: table row.
**C-48 form**: Column 4 per row: `SCAN PROTOCOL decl. above`; FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column: `Row (1) below`, `Row (2) below`, `Row (3) below`.
**C-49 form**: Section `## SCAN PROTOCOL`; BAD PLAN header label `# SCAN PROTOCOL -- C1: Header Index`; footer `# SCAN PROTOCOL -- C3: exit verified`.
**C-51**: Not targeted.
**C-57, C-58, C-59**: Not reachable (require C-54 → C-53 → C-52 → C-51 -- chain broken at C-51).

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

The BAD PLAN block at the end of this prompt is a bounded teaching unit. The annotation-type index in Component 1 is a 4-column pipe-delimited table. Read this protocol section before construction.

**Component 1 -- Header Index (C-41 + C-44 + C-47 + C-48 + C-50)**

Component 1 is a 4-column pipe-delimited table with columns: field type | criterion | exact tag string (full Why: per C-47) | C-42 back-reference. Each row maps one annotation type to its field, criterion, tag, and declaration source.

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types confirmed present in block body.

**Navigation contract (C-45 + C-48):**
- This section (SCAN PROTOCOL) is the governing declaration. See the BAD PLAN block for the bounded instance.
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 row numbers.

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

---

#### Step 3 -- Select Skills

Open the catalog now. Select skills relevant to the topic and the declared phases.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. No new phases may be created. Discard skills with no matching phase.

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

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess the compliance landscape"` -- imperative, not interrogative
- FAIL: `"Are we ready to proceed?"` -- scope-generic, not phase-specific

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
[ ] C-50: C-41 index is a 4-column pipe table -- YES for this variate
[ ] C-51: named protocol section is document-first -- NO for this variate (SCAN PROTOCOL appears after intro)
[ ] C-52 through C-59: NOT REACHABLE (require C-51)
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

**Hypothesis**: Positioning the protocol architecture at the document's opening causes every subsequent section to be read through the protocol frame. Principle-before-instance architecture (C-51) ensures no section is read before the protocol that governs it. C-50 not targeted -- C-41 index is prose enumeration. C-57/C-58/C-59 not reachable (chain requires C-50 for C-52).
Anticipated: 43/52 aspirational, 305/350.

**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before the three-class table, lifecycle zones, catalog, and construction steps. Only a single opening sentence precedes it.
**C-47 form**: Full unabbreviated Why: in index entries.
**C-48 form**: Each C-41 entry ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)`.
**C-49 form**: `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL -- Component 1: Header Entry Index`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification complete`.
**C-50**: Not targeted (C-41 index is prose enumeration).
**C-57, C-58, C-59**: Not reachable (require C-52 → C-50, which is absent).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit with three components. Understanding the protocol before construction prevents incomplete blocks.

**Component 1 -- Header Entry Index (C-41 + C-44 + C-47 + C-48)**

The BAD PLAN header is a pre-scan index. Each entry names: field type, criterion, exact tag string with full unabbreviated `Why:` where applicable, and a back-reference to this section.

Entry form:
```
# C-XX: <field type> carries <exact tag string with full Why: if applicable>
#       (rule declared in BOUNDED BLOCK PROTOCOL above)
```

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all Component 1 annotation types found present in block body.

**Navigation contract (C-45 + C-48):**
- This section (BOUNDED BLOCK PROTOCOL) is the governing declaration. See the BAD PLAN block for the bounded instance (Component 1 header below).
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 entry numbers.

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

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

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
[ ] C-02: echo is last; auto: true; skills: []
[ ] C-03: all skills from catalog; no invented names
[ ] C-04: every non-echo stage has an evidence-state gate
[ ] C-05: namespace ordering respected
[ ] C-06: stage names describe investigative purpose, not namespace labels
[ ] C-07: plan framed as signal-gathering artifact, not executor script
[ ] C-08: at least one quantified gate threshold (>= N)
[ ] C-09 through C-49: all aspirational criteria
[ ] C-50: C-41 index is a 4-column pipe table -- NO for this variate (prose entries)
[ ] C-51: named protocol section is document-first -- YES for this variate
[ ] C-52 through C-59: NOT REACHABLE (require C-50)
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. This is the BOUNDED BLOCK PROTOCOL co-location family (see BOUNDED BLOCK PROTOCOL section above for the full protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in BOUNDED BLOCK PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in BOUNDED BLOCK PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in BOUNDED BLOCK PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BOUNDED BLOCK PROTOCOL -- Component 1: Header Entry Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index (exact tag strings; full Why: per C-47; per-entry back-refs per C-48):
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

# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header entry index confirmed present in block above.
```

---

## V-03 -- Lifecycle Emphasis Axis (COMPLETE VERIFICATION PROTOCOL -- Universal Per-Step Active Verification)

**Axis**: Single-axis variation on lifecycle emphasis. The C-55 active NOT/IS verification pattern is extended from Component 1's format mandate to EVERY construction step in the protocol (C-58). Every named step that declares constraints carries its own explicit SELF-VERIFY block with individually checkable NOT/IS items. Built on the V-05 R19 base (C-50+C-51+C-52+C-53+C-54+C-55+C-56+C-57 all present). One new criterion: C-58.

**Hypothesis**: C-55 converts the format exclusion list from static rules into a per-item confirmation step at the declaration site. If the same per-item NOT/IS confirmation pattern applies to every construction step -- not just the format mandate -- then every constraint in the protocol becomes an active audit step rather than background knowledge read once and forgotten. A model executing any step must explicitly confirm each NOT condition before proceeding, making constraint violations structurally visible at each step boundary.
Anticipated: 51/52 aspirational (V-05 R19 base 50/52 + C-58), 345/350.

**C-58 form**: Every construction step (Step 1 through Step 10) that declares constraints carries a dedicated SELF-VERIFY block: `**SELF-VERIFY before proceeding: confirm:** NOT [wrong form 1] / NOT [wrong form 2] / IS [correct form]`.
**C-55 form**: Active NOT/IS checklist at the Component 1 format mandate declaration site (carried from V-05 R19).
**C-56 form**: Mandate echo (static) at Component 1 header (carried from V-05 R19).
**C-57 form**: Active verification checklist also echoed at Component 1 header (carried from V-05 R19).
**C-59**: Not targeted (template-field saturation is V-04's single axis).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## COMPLETE VERIFICATION PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit. This protocol section is the governing declaration. **Active verification is a document-wide discipline in this prompt -- every construction step that declares constraints carries a SELF-VERIFY block, not only the Component 1 format mandate.**

**Component 1 -- Header Index: FORMAT REQUIREMENT**

Component 1 MUST be a 4-column pipe-delimited table. Forbidden formats for Component 1:
- prose enumeration (entries written as running sentences or paragraphs)
- indented list (entries as `# - item:` or `#   item:` lines without column alignment)
- bulleted entries (entries as `# * item:` or `# - item:` lines without pipe columns)

Each of these formats is individually disqualified -- content completeness does not compensate for format non-compliance. The four columns are mandatory and must appear in this order:

| Column | Purpose | Criteria satisfied |
|--------|---------|-------------------|
| Column 1: Field type | Which YAML field carries the annotation | C-41 |
| Column 2: Criterion | Criterion number governing that field | C-41 |
| Column 3: Exact tag string | The annotation as it appears at the field, including full unabbreviated Why: | C-44 + C-47 |
| Column 4: C-42 back-ref | Per-row reference to this COMPLETE VERIFICATION PROTOCOL section | C-48 |

**Active verification -- run before completing Component 1 (C-55):**
- NOT a prose enumeration (entries in running sentences)
- NOT an indented list (entries as `# - item:` lines without columns)
- NOT a bulleted entry set (entries as `# * item:` lines without columns)
- IS a pipe-delimited table with the four columns above

The header table MUST affirmatively claim full-criterion coverage of all 7 criteria (C-38).

**Universal active verification (C-58):** This same NOT/IS confirmation pattern applies to every construction step below that declares constraints. Each SELF-VERIFY block is mandatory -- do not skip.

**Component 2 -- Block Body: FIELD CO-LOCATION REQUIREMENT**

The block body MUST contain wrong YAML. Every violating field SHALL carry its criterion tag at the exact field line.

**Component 3 -- Exit Verification: COMPLETION REQUIREMENT**

The block MUST end with an explicit footer confirming all annotation types from Component 1 were found present.

**Navigation contract (C-45 + C-48):**
- This section (COMPLETE VERIFICATION PROTOCOL) is the governing declaration.
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 table rows. Each Component 1 table row carries "COMPLETE VERIFICATION PROTOCOL decl. above" in column 4.

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

Do not proceed to Step 3 until Step 2 SELF-VERIFY passes.

---

#### Step 1 -- Topic

State the topic name. All artifact names, phase groupings, and gate artifact types must be coherent with this specific topic.

**SELF-VERIFY before proceeding:**
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
ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. Derivation begins at row 0, not where execution ends.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

**SELF-VERIFY before proceeding:**
- NOT: any phase name that is a namespace label (`scout`, `draft`, `review`, `flow`, `trace`)
- NOT: any phase name that is a namespace cluster (`scout_and_draft`, `prove_and_review`)
- NOT: any phase name that is a generic label (`stage-1`, `phase-A`, `step-one`)
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

Map each skill to its declared phase. No new phases may be created. Discard skills with no matching phase.

**SELF-VERIFY before proceeding:**
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

At least one gate must include `>= N`.

**SELF-VERIFY before proceeding:**
- NOT: any gate using execution-state language (`"done"`, `"complete"`, `"all tasks finished"`, `"proceed"`)
- NOT: any gate without a stage-id prefix matching `name:` exactly
- NOT: any gate with zero quantified thresholds (`>= N` absent from all gates)
- IS: every non-echo gate is an artifact-state condition, stage-id prefixed, with at least one `>= N` threshold

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

**SELF-VERIFY before proceeding:**
- NOT: any gate referencing an artifact type that no skill in that stage produces
- IS: every gate artifact type is traceable to a skill in the same stage

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess the compliance landscape"` -- imperative, not interrogative
- FAIL: `"Are we ready to proceed?"` -- scope-generic, not phase-specific

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
- NOT: any phase label in `evidence_arc` that was not declared in Step 2
- NOT: any zone key absent from `evidence_arc` that has at least one phase assigned to it
- IS: every zone key maps to its declared phases from Step 2 exactly

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

Any NO triggers revision before Step 10.

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
[ ] C-50: C-41 index is a 4-column pipe table -- YES for this variate
[ ] C-51: named protocol section is document-first -- YES for this variate
[ ] C-52: protocol section pre-declares column schema -- YES
[ ] C-53: column schema declaration uses prescriptive MUST language -- YES
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name -- YES
[ ] C-55: active NOT/IS verification checklist at declaration site -- YES
[ ] C-56: mandate echo with NOT list at Component 1 header -- YES
[ ] C-57: active NOT/IS checklist also echoed at Component 1 header (dual-site) -- YES
[ ] C-58: active NOT/IS verification at EVERY constraint-bearing construction step -- YES
[ ] C-59: per-field mandate echo at every constrained YAML template field -- NO for this variate
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. This is the COMPLETE VERIFICATION PROTOCOL co-location family (see COMPLETE VERIFICATION PROTOCOL section above). The BAD PLAN C1 table below implements this family per the Component 1 format requirement:

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Row (1) in COMPLETE VERIFICATION PROTOCOL C1 table below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Row (2) in COMPLETE VERIFICATION PROTOCOL C1 table below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Row (3) in COMPLETE VERIFICATION PROTOCOL C1 table below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in COMPLETE VERIFICATION PROTOCOL C1 below

```yaml
# COMPLETE VERIFICATION PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
# Format: 4-column pipe table as mandated by COMPLETE VERIFICATION PROTOCOL above
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)
# Verify before finalizing: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                                    | C-42 back-ref                               |
# |---------------|---------------|------------------------------------------------------------------------------------------|---------------------------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable                      | COMPLETE VERIFICATION PROTOCOL decl. above  |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                             | COMPLETE VERIFICATION PROTOCOL decl. above  |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                             | COMPLETE VERIFICATION PROTOCOL decl. above  |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                              | COMPLETE VERIFICATION PROTOCOL decl. above  |

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

# COMPLETE VERIFICATION PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

## V-04 -- Phrasing Register Axis (FIELD SATURATION PROTOCOL -- Per-Field Mandate Echo)

**Axis**: Single-axis variation on phrasing register. The C-56 mandate-echo-at-application-site pattern is extended from the Component 1 header to every constrained YAML template field (C-59). Every field in the template scaffold that carries a format constraint echoes its own governing mandate and NOT list inline at the field position itself. Built on the V-05 R19 base (C-50+C-51+C-52+C-53+C-54+C-55+C-56+C-57 all present). One new criterion: C-59.

**Hypothesis**: C-56 echoes the format mandate at one application site (Component 1 header). If every constrained YAML template field echoes its own mandate and NOT list, the entire YAML scaffold becomes locally self-documenting -- every authoring decision encounters its constraint at the point of decision, without any cross-document recall. The co-location discipline is saturated across the entire template surface rather than applied at one exceptional site.
Anticipated: 51/52 aspirational (V-05 R19 base 50/52 + C-59), 345/350.

**C-59 form**: Every constrained YAML template field carries an inline echo of its positive mandate and NOT list: `name:` echoes the stage-name rule, `intent:` echoes the interrogative requirement, `skills:` echoes the catalog constraint, `gate_fail:` echoes the evidence-state rule, `gate:` echoes the gate format, `strategy:` echoes the plan-identity rule.
**C-55, C-56, C-57 forms**: Carried from V-05 R19 (present and unchanged).
**C-58**: Not targeted (universal per-step SELF-VERIFY is V-03's single axis).

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## FIELD SATURATION PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit. This protocol section is the governing declaration. **Mandate echo saturation is a template-wide discipline in this prompt -- every constrained YAML template field echoes its governing rule at the field position itself, not only the Component 1 header.**

**Component 1 -- Header Index: FORMAT REQUIREMENT**

Component 1 MUST be a 4-column pipe-delimited table. Forbidden formats for Component 1:
- prose enumeration (entries written as running sentences or paragraphs)
- indented list (entries as `# - item:` or `#   item:` lines without column alignment)
- bulleted entries (entries as `# * item:` or `# - item:` lines without pipe columns)

Each of these formats is individually disqualified. The four columns are mandatory and must appear in this order:

| Column | Purpose | Criteria satisfied |
|--------|---------|-------------------|
| Column 1: Field type | Which YAML field carries the annotation | C-41 |
| Column 2: Criterion | Criterion number governing that field | C-41 |
| Column 3: Exact tag string | The annotation as it appears at the field, including full unabbreviated Why: | C-44 + C-47 |
| Column 4: C-42 back-ref | Per-row reference to this FIELD SATURATION PROTOCOL section | C-48 |

**Active verification -- run before completing Component 1 (C-55):**
- NOT a prose enumeration
- NOT an indented list
- NOT a bulleted entry set
- IS a pipe-delimited table with the four columns above

The header table MUST affirmatively claim full-criterion coverage of all 7 criteria (C-38).

**Field saturation mandate (C-59):** Every YAML template field that carries a format constraint includes an inline echo of both the positive mandate and the NOT list for that field's constraint, at the field position. No constrained field is left without its governing rule co-located at the authoring point.

**Component 2 -- Block Body: FIELD CO-LOCATION REQUIREMENT**

The block body MUST contain wrong YAML. Every violating field SHALL carry its criterion tag at the exact field line.

**Component 3 -- Exit Verification: COMPLETION REQUIREMENT**

The block MUST end with an explicit footer confirming all annotation types from Component 1 were found present.

**Navigation contract (C-45 + C-48):**
- This section (FIELD SATURATION PROTOCOL) is the governing declaration.
- The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to specific Component 1 table rows. Each Component 1 table row carries "FIELD SATURATION PROTOCOL decl. above" in column 4.

---

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before declaring arc phases.

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

1. Declare the topic (Step 1)
2. Declare arc phases by lifecycle zone -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates: compound lineage prefix format, at least one quantified (Step 5a)
5b. FORWARD REFERENCE audit (Step 5b)
6. Write per-phase intent questions: interrogative form required (Step 6)
7. Encode `evidence_arc:` field (Step 7)
8. Assemble YAML using the field-saturated schema below (Step 8)
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

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL (imperative): `"Assess the compliance landscape"`
- FAIL (generic): `"Are we ready to proceed?"`

---

#### Step 7 -- Evidence Arc Field

```yaml
evidence_arc:
  breadth:   [breadth-zone phase labels from Step 2]
  depth:     [depth-zone phase labels from Step 2]
  synthesis: [synthesis-zone phase labels from Step 2]
```

---

#### Step 8 -- Assemble YAML (Field-Saturated Schema)

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.**

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema -- every constrained field echoes its mandate and NOT list inline (C-59 field saturation):

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
  # Mandate (C-07): IS a plan-identity framing element
  # NOT: executor script ("Execute all skills and proceed") / NOT: task list / NOT: empty
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    # Mandate (C-06): IS investigation-intent label describing what this phase answers
    # NOT: namespace label (scout, draft, review) / NOT: namespace cluster (scout_and_draft) / NOT: generic (stage-1)
    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Mandate: IS genuine interrogative ending with ? tied to this specific phase
    # NOT: imperative ("Assess X") / NOT: scope-generic ("Are we ready?") / NOT: missing ?
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
    # Mandate (C-03): IS namespace-qualified catalog names only
    # NOT: invented names (gather-requirements, make-a-plan) / NOT: namespace-only (scout:)
    # requires: <artifact> from Zone: <name> (C-05)  [dep zones only]
    # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"
    # Mandate (C-04): gate MUST be artifact-state condition with stage-id prefix and >= N
    # NOT: "done" / NOT: "complete" / NOT: "all tasks finished" / NOT: execution-history phrases
    # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    # Mandate (C-04): IS artifact-state with stage-id:: prefix and >= N threshold
    # NOT: execution-state / NOT: missing stage-id prefix / NOT: missing >= N
    # check correction table: gate values
  - ...
  - name: echo  # REQUIRED: DO NOT add skills here. DO NOT move echo before other stages.
    auto: true  # REQUIRED: must be true
    skills: []  # REQUIRED: empty / NOT: any skill entries
```

---

#### Step 9 -- Per-Stage Compliance Table

| Stage | `phase:` maps to `evidence_arc` zone? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|---------------------------------------|-------------------------------------|--------------------------|
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
[ ] C-50: C-41 index is a 4-column pipe table -- YES
[ ] C-51: named protocol section is document-first -- YES
[ ] C-52: protocol section pre-declares column schema -- YES
[ ] C-53: column schema declaration uses prescriptive MUST language -- YES
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name -- YES
[ ] C-55: active NOT/IS verification checklist at declaration site -- YES
[ ] C-56: mandate echo with NOT list at Component 1 header -- YES
[ ] C-57: active NOT/IS checklist also echoed at Component 1 header (dual-site) -- YES
[ ] C-58: active NOT/IS verification at every constraint-bearing construction step -- NO for this variate
[ ] C-59: per-field mandate echo at every constrained YAML template field -- YES
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

Every YAML field carrying a criterion-testable value requires an inline criterion tag at that exact field line. This is the FIELD SATURATION PROTOCOL co-location family (see FIELD SATURATION PROTOCOL above). The BAD PLAN C1 table below implements this family per the Component 1 format requirement:

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Row (1) in FIELD SATURATION PROTOCOL C1 table below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Row (2) in FIELD SATURATION PROTOCOL C1 table below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Row (3) in FIELD SATURATION PROTOCOL C1 table below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in FIELD SATURATION PROTOCOL C1 below

```yaml
# FIELD SATURATION PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
# Format: 4-column pipe table as mandated by FIELD SATURATION PROTOCOL above
# (NOT prose enumeration / NOT indented list / NOT bulleted entries)
# Verify before finalizing: NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table with 4 columns
#
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                                | C-42 back-ref                              |
# |---------------|---------------|--------------------------------------------------------------------------------------|--------------------------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable                  | FIELD SATURATION PROTOCOL decl. above      |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                         | FIELD SATURATION PROTOCOL decl. above      |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                         | FIELD SATURATION PROTOCOL decl. above      |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                          | FIELD SATURATION PROTOCOL decl. above      |

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

# FIELD SATURATION PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

## V-05 -- Combined Axis (BOUNDED BLOCK PROTOCOL -- C-57+C-58+C-59 All Three New Criteria)

**Axis**: Combined variation targeting all three new R20 criteria simultaneously. The BOUNDED BLOCK PROTOCOL section appears FIRST (C-51). The protocol section mandates Component 1 as a 4-column table (C-50+C-52+C-53+C-54+C-55+C-56). C-57 (active verify echoed at Component 1 header) is carried from R19 V-05. C-58 (universal per-step active verification) is added: every construction step with constraints gets a SELF-VERIFY block. C-59 (per-field mandate echo saturation) is added: every constrained YAML template field echoes its mandate and NOT list.

**Hypothesis**: C-58 saturates the active verification pattern across every construction step, making constraint auditing a continuous discipline rather than a one-step check. C-59 saturates the mandate echo pattern across every YAML template field, making every authoring decision locally self-documenting. Together with C-57's application-site active verification, all three mechanisms close the attention gap at every level: construction step, template field, and block header simultaneously.
Anticipated: 52/52 aspirational (V-05 R19 base 50/52 + C-58 + C-59), 350/350.

**C-57 form**: Component 1 header echoes both the static mandate (C-56) AND the active NOT/IS verification checklist (C-57).
**C-58 form**: Every construction step (Steps 1-10) with constraints carries a SELF-VERIFY block with NOT/IS items.
**C-59 form**: Every constrained YAML template field in Step 8 echoes its mandate (positive) and NOT list inline.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit. This protocol section is the governing declaration. This prompt applies two document-wide disciplines simultaneously: (1) **active verification at every construction step** -- every step with constraints carries a SELF-VERIFY block; (2) **mandate echo saturation** -- every constrained YAML template field echoes its mandate and NOT list at the field position.

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

**Active verification -- run before completing Component 1 (C-55):**
- NOT a prose enumeration (entries in running sentences)
- NOT an indented list (entries as `# - item:` lines without columns)
- NOT a bulleted entry set (entries as `# * item:` lines without columns)
- IS a pipe-delimited table with the four columns above

The header table MUST affirmatively claim full-criterion coverage of all 7 criteria (C-38).

**Universal active verification (C-58):** The same NOT/IS confirmation pattern applies to every construction step below that declares constraints. Each step's SELF-VERIFY block is mandatory.

**Field saturation mandate (C-59):** Every YAML template field that carries a format constraint echoes its governing mandate and NOT list inline at the field position in the Step 8 schema.

**Component 2 -- Block Body: FIELD CO-LOCATION REQUIREMENT**

The block body MUST contain wrong YAML. Every violating field SHALL carry its criterion tag at the exact field line. Field-level tags MUST match the tag strings specified in Component 1 Column 3.

**Component 3 -- Exit Verification: COMPLETION REQUIREMENT**

The block MUST end with an explicit footer confirming all annotation types from Component 1 were found present in the block body.

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
8. Assemble YAML: produce ARTIFACT 2 first, then transcribe using the field-saturated schema (Step 8)
9. Per-stage compliance table (Step 9)
10. Terminal checklist (Step 10)

Do not proceed to Step 3 until Step 2 SELF-VERIFY passes.

---

#### Step 1 -- Topic

State the topic name. All artifact names, phase groupings, and gate artifact types must be coherent with this specific topic.

**SELF-VERIFY before proceeding:**
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

**SELF-VERIFY before proceeding:**
- NOT: any phase name that is a namespace label (`scout`, `draft`, `review`, `flow`, `trace`)
- NOT: any phase name that is a namespace cluster (`scout_and_draft`, `prove_and_review`)
- NOT: any phase name that is a generic label (`stage-1`, `phase-A`, `step-one`)
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

Map each skill to its declared phase. No new phases may be created. Discard skills with no matching phase.

**SELF-VERIFY before proceeding:**
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

**SELF-VERIFY before proceeding:**
- NOT: any gate using execution-state language (`"done"`, `"complete"`, `"all tasks finished"`, `"proceed"`)
- NOT: any gate without a stage-id prefix matching `name:` exactly
- NOT: any gate with zero quantified thresholds (`>= N` absent from all gates)
- IS: every non-echo gate is an artifact-state condition, stage-id prefixed, with at least one `>= N` threshold

---

#### Step 5b -- FORWARD REFERENCE Audit

For each non-echo stage: verify every artifact type in the gate is producible by at least one skill in that stage's `skills` array. Fix all forward references before Step 6.

**SELF-VERIFY before proceeding:**
- NOT: any gate referencing an artifact type that no skill in that stage produces
- IS: every gate artifact type is traceable to a skill in the same stage

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL (not interrogative): `"Assess the compliance landscape"`
- FAIL (wrong scope): `"Are we ready to proceed?"`

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
- NOT: any phase label in `evidence_arc` that was not declared in Step 2
- NOT: a zone key absent from `evidence_arc` that has at least one assigned phase
- IS: every zone key maps exactly to its declared phases from Step 2

---

#### Step 8 -- Assemble YAML

Before assembling YAML, produce **ARTIFACT 2 -- Bilateral Trace Matrix with YAML Fragment Column**.

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML annotations are transcribed from ARTIFACT 2 matrix cells, not authored independently.

| Row | Stage | Band | Gap (intent?) | Owner | Consumes | Produces | YAML fragment |
|-----|-------|------|---------------|-------|----------|----------|---------------|
| 0 | echo | -- | (terminal consumer) | -- | [receives] | -- | `name: echo`<br>`auto: true`<br>`skills: []` |
| 1 | [last] | [B-NN] | [question?] | [role] | [artifacts] | [artifacts] | `# Band: B-NN`<br>`# Consumes: ...` |
| N | [first] | [B-01] | [question?] | [role] | -- | [artifacts] | `# Band: B-01`<br>`# Produces: ...` |

Required YAML schema -- field saturation: every constrained field echoes its mandate and NOT list (C-59):

```yaml
topic: <topic>
strategy: "why this feature is worth the investment and what signal-gathering decision this plan resolves"
  # Mandate (C-07): IS a plan-identity framing element
  # NOT: executor script / NOT: task list / NOT: empty string / NOT: absent field
evidence_arc:
  breadth:   [...]
  depth:     [...]
  synthesis: [...]
stages:
  - name: <phase-label>
    # Mandate (C-06): IS investigation-intent label describing what this phase answers
    # NOT: namespace label (scout, draft, review, flow, trace)
    # NOT: namespace cluster (scout_and_draft, prove_and_review)
    # NOT: generic label (stage-1, phase-A, step-one)
    # check correction table: stage names
    phase: <arc-key>
    intent: "<question ending with ?>"
    # Mandate: IS genuine interrogative ending with ? tied to this specific phase
    # NOT: imperative ("Assess X", "Gather Y") / NOT: scope-generic ("Are we ready?")
    # NOT: missing question mark
    # Band:     <from ARTIFACT 2>
    # Gap:      <from ARTIFACT 2>
    # Owner:    <from ARTIFACT 2>
    # Consumes: <from ARTIFACT 2>
    # Produces: <from ARTIFACT 2>
    skills:
    # Mandate (C-03): IS namespace-qualified catalog names only
    # NOT: invented names (gather-requirements, make-a-plan, run-analysis)
    # NOT: namespace-only entries (scout:, review:, flow:)
    # requires: <artifact> from Zone: <name> (C-05)  [dep zones only]
    # check correction table: skill names
      - <namespace>:<skill>
    gate_fail: "<execution-state string>"
    # Mandate (C-04): gate MUST be artifact-state with stage-id prefix and >= N
    # NOT: "done" / NOT: "complete" / NOT: "all tasks finished" / NOT: any execution-history phrase
    # WRONG C-04: Why: execution-history check, not artifact-verifiable
    gate_pass: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    gate: "<stage-id>::<artifact-type> >= N AND <namespace>:<skill> artifact exists"
    # Mandate (C-04): IS {stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
    # NOT: execution-state string / NOT: missing stage-id:: prefix / NOT: missing >= N
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

Any NO triggers revision before Step 10.

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
[ ] C-52: protocol section pre-declares column schema using all four column names -- YES
[ ] C-53: column schema declaration uses prescriptive MUST/SHALL language -- YES
[ ] C-54: prescriptive mandate enumerates forbidden alternatives by name
          (prose enumeration, indented list, bulleted entries) -- YES
[ ] C-55: active NOT/IS verification checklist present at declaration site -- YES
          (NOT prose enumeration / NOT indented list / NOT bulleted entries / IS pipe table)
[ ] C-56: mandate echo with NOT list present at Component 1 header -- YES
          (# Format: 4-column pipe table as mandated... / # NOT list echoed)
[ ] C-57: active NOT/IS checklist also echoed at Component 1 header (dual-site) -- YES
          (# Verify before finalizing: NOT.../IS... present at Component 1 header)
[ ] C-58: active NOT/IS verification at every constraint-bearing construction step -- YES
          (SELF-VERIFY blocks present at Steps 1, 2, 3, 4, 5a, 5b, 6, 7, 8, 9)
[ ] C-59: per-field mandate echo at every constrained YAML template field -- YES
          (strategy:, name:, intent:, skills:, gate_fail:, gate: all carry inline mandate+NOT)
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
# | Field type    | Criterion     | Exact tag string (full Why: per C-47)                                                 | C-42 back-ref                      |
# |---------------|---------------|---------------------------------------------------------------------------------------|------------------------------------|
# | gate_fail:    | C-04 (C-26)   | # WRONG C-04: Why: execution-history check, not artifact-verifiable                   | BOUNDED BLOCK PROTOCOL decl. above |
# | name:         | C-06 (C-37)   | # WRONG C-06                                                                          | BOUNDED BLOCK PROTOCOL decl. above |
# | skills: entry | C-03 (C-39)   | # WRONG C-03                                                                          | BOUNDED BLOCK PROTOCOL decl. above |
# | this header   | C-38          | affirmative full-coverage claim (all 7 / C-01 through C-07)                           | BOUNDED BLOCK PROTOCOL decl. above |

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

# BOUNDED BLOCK PROTOCOL -- Component 3: Exit Verification complete.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

```json
{"round": 20, "rubric": "v20", "total_pts": 350, "new_criteria": ["C-57", "C-58", "C-59"], "anticipated_scores": {"V-01": {"aspirational": "43/52", "composite": "305/350", "new_criteria_achieved": []}, "V-02": {"aspirational": "43/52", "composite": "305/350", "new_criteria_achieved": []}, "V-03": {"aspirational": "51/52", "composite": "345/350", "new_criteria_achieved": ["C-58"]}, "V-04": {"aspirational": "51/52", "composite": "345/350", "new_criteria_achieved": ["C-59"]}, "V-05": {"aspirational": "52/52", "composite": "350/350", "new_criteria_achieved": ["C-57", "C-58", "C-59"]}}}
```
