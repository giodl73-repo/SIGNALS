---
skill: quest-variate
skill_target: program-plan
date: 2026-03-16
round: 16
rubric: v16
rubric_date: 2026-03-16
total_pts: 310
golden_threshold: 80
new_criteria: C-50, C-51
---

# program-plan -- R16 Variate Prompt Bodies (V-01 through V-05)

Generated 2026-03-16. Rubric: v16 (C-01 through C-51, 44 aspirational criteria, 310 pts, golden: all essential pass AND composite >= 80).

**R15-2026-03-16 state under v16 rubric (C-50/C-51 added):**
- V-01 (SCAN PROTOCOL, compact table): passes C-50 (C-41 index is 4-column pipe table) -- 310/310
- V-02 (BOUNDED BLOCK PROTOCOL first): passes C-51 (protocol section is first major section) -- 310/310
- V-03 (BLOCK SCAN PROTOCOL, numbered list): C-41 index is numbered list, not table -- fails C-50; protocol not first -- fails C-51 -- 300/310
- V-04 (BLOCK SPECIFICATION PROTOCOL, fused Why/nav): C-41 index is prose list -- fails C-50; protocol not first -- fails C-51 -- 300/310
- V-05 (extended protocol, formal sub-spec): C-41 index is prose list -- fails C-50; protocol not first -- fails C-51 -- 300/310

**R16 design constraint:** V-01 must satisfy C-50 (4-column table for C-41 index). V-02 must
satisfy C-51 (named protocol section is the FIRST major structural section). V-05 must satisfy
BOTH C-50 and C-51 simultaneously. All five variations must maintain C-47, C-48, and C-49 plus
full C-01 through C-46 coverage.

**C-50 canonical form (V-01 and V-05):**
- C-41 index in BAD PLAN header is a pipe-delimited markdown table
- Column 1: field type (gate_fail:, name:, skills:, this header)
- Column 2: criterion number (C-26, C-37, C-39, C-38)
- Column 3: exact tag string including full Why: clause (C-44 + C-47 data)
- Column 4: C-42 back-ref (C-48 data)
- All four columns present per row; Why: merged into column 3 or as column 5

**C-51 canonical form (V-02 and V-05):**
- Named protocol section (C-42/C-49 declaration) appears before every implementation section
- Specifically: before the three-class information table, before lifecycle zones, before catalog
- A brief opening sentence or role context does not count as a major section

**Variation axes for R16:**
- V-01 (single: output format): SCAN PROTOCOL carry-forward; C-41 index as 4-column markdown
  table confirming C-50; same structural arrangement as R15 V-01
- V-02 (single: role sequence): BOUNDED BLOCK PROTOCOL carry-forward first; same structural
  arrangement as R15 V-02 confirming C-51
- V-03 (single: lifecycle emphasis): Zone Decision Tables for each lifecycle zone declared before
  catalog opens; each zone has a formal 3-row table (Commit Trigger / Artifact Floor / Gate
  Pattern Class) making zone commitment independently auditable; BLOCK AUDIT PROTOCOL naming
- V-04 (single: inertia framing): Per-step AVOID blocks at every construction step header
  naming the concrete F-1 behavior displaced; status-quo competitor foregrounded at every
  decision point; ANNOTATION VERIFICATION PROTOCOL naming
- V-05 (combined: C-50 + C-51): BOUNDED BLOCK PROTOCOL first (C-51) AND BAD PLAN header uses
  4-column pipe table (C-50); maximum two-criterion convergence

---

## V-01 -- Output Format Axis (SCAN PROTOCOL -- 4-Column Table Index)

**Axis**: Single-axis variation on output format. The C-41 annotation-type index in the BAD PLAN
header is implemented as a pipe-delimited markdown table with exactly 4 columns: field type,
criterion, exact tag string with full Why: clause, and per-entry C-42 back-reference. This
directly satisfies C-50. SCAN PROTOCOL naming carried forward from R15 V-01 unchanged.

**Hypothesis**: A tabular C-41 index promotes each data type (field type, criterion, tag string,
back-ref) to an independently scannable column. A model returning to the index during block
scanning can look up any column directly without re-reading the full entry prose. C-47 full Why:
text in the tag-string column is as complete as in a prose entry, and C-48 per-entry back-ref
occupies a dedicated column rather than being appended as a phrase. Table format is the
minimum-overhead form that satisfies C-44, C-47, and C-48 simultaneously as column values.
Anticipated: 310/310.

**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag
string (with full `Why:` in the tag column for gate_fail:) | C-42 back-ref.
**C-47 form**: `# WRONG C-04: Why: execution-history check, not artifact-verifiable` as cell
value in column 3 of the table row for gate_fail:.
**C-48 form**: Column 4 per row: `SCAN PROTOCOL decl. above`; FIELD CO-LOCATION PRINCIPLE table
has `BAD PLAN entry` column: `Entry (1) below`, `Entry (2) below`, `Entry (3) below`.
**C-49 form**: Section `## SCAN PROTOCOL`; BAD PLAN header table label `# SCAN PROTOCOL -- C1:
Header Index`; footer `# SCAN PROTOCOL -- C3: exit verified`.
**C-51**: Not required for V-01.

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
| **C1 -- Header Index** | C-41, C-44, C-47, C-48 | 4-column table: field type / criterion / exact tag string with full Why: / C-42 back-ref |
| **C2 -- Block Body** | C-26, C-37, C-39 | Wrong YAML with field-level criterion tags at every violating field line |
| **C3 -- Exit Verification** | C-46 | Footer confirming all C1 annotation types found present in block body |

Navigation contract (C-45 + C-48): this section (SCAN PROTOCOL) is the protocol declaration.
The BAD PLAN header below is C1. Each FIELD CO-LOCATION PRINCIPLE table row carries a per-row
forward-reference to its specific C1 entry number. Each C1 table row carries this section as
its back-ref.

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
current stage's skill knowledge. The equivalence makes the rule self-verifying from both ends:
Produces(stage N) == Consumes(stage N+1).

ROW-0 RULE [counter: F-2]: Echo occupies row 0 of ARTIFACT 2. This is not an arbitrary
convention -- it encodes derivation direction. Row 0 is where derivation begins, not where
execution ends. # Band: omitted from echo is correct.
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
[ ] C-50: C-41 index is a pipe-delimited markdown table with >= 4 columns (field type / criterion / tag string / C-42 back-ref)
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
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in SCAN PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in SCAN PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in SCAN PROTOCOL C1 below |

The BAD PLAN C1 header below implements this family as the SCAN PROTOCOL entry index table.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in SCAN PROTOCOL C1 below

```yaml
# SCAN PROTOCOL -- C1: Header Index (C-41 + C-44 + C-47 + C-48 + C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# | Field type    | Criterion     | Exact tag string (full Why: merged here per C-47)                             | C-42 back-ref (C-48)     |
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
the catalog. A model reads the bounded-unit architecture before any construction guidance and
therefore approaches the BAD PLAN block as a known protocol rather than an appended illustration.
C-47, C-48, and C-49 carried forward from R15 V-02 unchanged. C-51 is now the primary target.

**Hypothesis**: Positioning the protocol architecture at the document's opening causes every
subsequent section to be read through the protocol frame. When the BAD PLAN block is encountered,
the model has prior context for why it has three components and what each must contain. The
principle-before-instance architecture (C-51) ensures no section in the document is read before
the protocol that governs it. A brief role context statement before the protocol does not
constitute a major section and does not violate C-51 placement. Anticipated: 310/310.

**C-51 form**: BOUNDED BLOCK PROTOCOL section appears before the three-class table, before
lifecycle zones, before the catalog, and before any construction steps. Only a single-sentence
role context precedes it.
**C-47 form**: `# C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check,
not artifact-verifiable` with `(rule declared in BOUNDED BLOCK PROTOCOL above)` on the next line.
**C-48 form**: Each C-41 entry ends with `(rule declared in BOUNDED BLOCK PROTOCOL above)`;
FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column: `See entry (1/2/3) in BAD PLAN
header below`.
**C-49 form**: Section `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL
-- Component 1: Header Entry Index`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3: Exit
Verification (C-46) complete`.
**C-50**: Not required for V-02.

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
[ ] C-01 through C-49: all criteria
[ ] C-47: C-41 index gate_fail: entry includes full unabbreviated Why: rationale (not Why: ...)
[ ] C-48: per-entry bidirectional navigation (each C-41 entry has own back-ref; C-42 has per-row forward-refs)
[ ] C-49: C-41/C-42/C-46 labeled as components of BOUNDED BLOCK PROTOCOL named entity
[ ] C-51: BOUNDED BLOCK PROTOCOL section is the FIRST major structural section in the document
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

## V-03 -- Lifecycle Emphasis Axis (Zone Decision Tables)

**Axis**: Single-axis variation on lifecycle emphasis. Each lifecycle zone has a formal
Zone Decision Table declared before the catalog opens. Each table has three rows:
Commit Trigger / Artifact Floor / Gate Pattern Class. The tables make zone commitment
independently auditable: a reviewer can verify any stage's zone advancement criteria from
the table without reading construction prose. Protocol: BLOCK AUDIT PROTOCOL.

**Hypothesis**: Making zone commitment criteria tabular and per-zone forces the model to
treat zone advancement as three independently verifiable conditions per zone rather than a
narrative paragraph. A model building gates will check its output against the Zone Decision
Table rows, not against general prose guidance. Each zone's Commit Trigger column names the
concrete decision (not just "breadth zone completed") making zone membership falsifiable.
Anticipated: 300/310 (C-50 and C-51 not targeted in this axis).

**C-47 form**: Full Why: in C-41 index prose entries: `Entry (1) C-26: gate_fail: carries
# WRONG C-04: Why: execution-history check, not artifact-verifiable (rule declared in BLOCK
AUDIT PROTOCOL above)`.
**C-48 form**: Each C-41 entry ends with `(rule declared in BLOCK AUDIT PROTOCOL above)`;
FIELD CO-LOCATION PRINCIPLE table has `BAD PLAN entry` column per row.
**C-49 form**: `## BLOCK AUDIT PROTOCOL`; BAD PLAN header: `# BLOCK AUDIT PROTOCOL --
Component 1: Header Index`; footer: `# BLOCK AUDIT PROTOCOL -- Component 3: Exit Verified`.
**Zone emphasis form**: Before catalog, each zone has its own Zone Decision Table with
Commit Trigger / Artifact Floor / Gate Pattern Class rows.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent:** catalog-first construction -- opening the skill catalog before
declaring arc phases. Zone membership becomes implicit; gates collapse to prose task-completion
checks; investigative intent disappears from the artifact.

Three classes of information must remain knowable at every stage boundary:

| Class | What must remain knowable | Criterion ladder |
|-------|--------------------------|------------------|
| **Zone membership** | Which lifecycle zone each stage belongs to -- declared before catalog opens | Arc-structure ladder |
| **Artifact provenance** | Which stage produced each gated artifact, at what count, from which catalog skill | Gate-behavior ladder |
| **Investigative intent** | What question each phase answers -- interrogative, zone-specific | Question-framing ladder |

---

## BLOCK AUDIT PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.

**Component 1 -- Header Index (C-41 + C-44 + C-47 + C-48)**: Pre-scan annotation-type index.
Each entry names: field type, criterion, exact tag string with full Why: where applicable, and
a back-reference to this section. Covers all 7 criteria affirmatively.

**Component 2 -- Block Body (C-26, C-37, C-39)**: Wrong YAML with field-level criterion tags
at every violating field line.

**Component 3 -- Exit Verification (C-46)**: Footer confirming all Component 1 annotation types
found present in block body.

Navigation contract (C-45 + C-48): This section (BLOCK AUDIT PROTOCOL) is the governing
declaration. The FIELD CO-LOCATION PRINCIPLE section below carries per-row forward-refs to
specific Component 1 entry numbers. Each Component 1 entry back-references this section.
See the BAD PLAN block below for the bounded instance implementing this protocol.

---

**Lifecycle zones and Zone Decision Tables** (catalog closed until Step 3):

These three tables define zone advancement criteria. A stage belongs to a zone only if its
name was committed to that zone before the catalog opened (Step 2). Advancement to the next
zone requires all three rows to be satisfied.

**Breadth Zone Decision Table:**

| Dimension | Requirement | Verification method |
|-----------|-------------|---------------------|
| Commit trigger | Named the problem space and key constraints from first principles -- no catalog consulted | Phase label is investigative, not namespace-cluster |
| Artifact floor | >= 1 scout artifact AND >= 1 draft artifact from stages in this zone | gate_pass field references both types |
| Gate pattern class | Compound gate: `{stage-id}::` with `>= 2` count floor on a scout or draft artifact | Verifiable by inspection of gate: field |

*Breadth skills: scout and draft namespaces.*

**Depth Zone Decision Table:**

| Dimension | Requirement | Verification method |
|-----------|-------------|---------------------|
| Commit trigger | Confirmed spec exists (draft:spec artifact produced in breadth) before any review or prove stage | Stage sequence: draft:spec precedes review:*, prove:* |
| Artifact floor | >= 1 review artifact AND >= 1 flow-or-trace artifact AND >= 1 prove artifact from stages in this zone | gate_pass fields cover all three types |
| Gate pattern class | Compound gate: `{stage-id}::` with `>= 2` count floor on a review or prove artifact | Verifiable by inspection of gate: field |

*Depth skills: review, flow, trace, prove namespaces.*

**Synthesis Zone Decision Table:**

| Dimension | Requirement | Verification method |
|-----------|-------------|---------------------|
| Commit trigger | Confirmed flow/trace artifacts from depth exist before any listen or metrics stage | Stage sequence: flow:* or trace:* precedes listen:* |
| Artifact floor | >= 1 listen artifact AND >= 1 metrics-or-goals artifact from stages in this zone | gate_pass fields reference both types |
| Gate pattern class | Compound gate: `{stage-id}::` with `>= 1` count floor on a listen, metrics, or goals artifact | Verifiable by inspection of gate: field |

*Synthesis skills: listen, metrics, goals namespaces.*

---

**Compound gate format:**

```
{stage-id}::{artifact-type} >= N AND {namespace}:{skill} artifact exists
```

`{stage-id}` must match `name:` exactly. `>= N` required. `{namespace}:{skill}` required.

Gate form PASS: `discovery::scout-feasibility >= 2 AND scout:market artifact exists`
Gate form FAIL: `"done"` -- Why: execution-history check, not verifiable by artifact inspection

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
2. Declare arc phases per Zone Decision Tables -- **catalog closed until Step 3** (Step 2)
3. Select skills from catalog (Step 3)
4. Assign skills to declared phases (Step 4)
5a. Design gates aligned to Zone Decision Table gate pattern class (Step 5a)
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
principles. Assign each to a zone per the Zone Decision Tables above.

| Phase label | Zone | Commit trigger satisfied? | Investigative question (ends with ?) |
|-------------|------|--------------------------|--------------------------------------|
| [name] | breadth/depth/synthesis | YES/NO | [...?] |

- PASS: `discovery` (breadth), `stress-test` (depth), `signal-watch` (synthesis)
- FAIL: `scout_and_draft_stage` (namespace-cluster label), `listen_phase` (namespace repetition)

**Produce ARTIFACT 0 -- Per-Stage Annotation Schema:**

```
ARTIFACT 0 -- Per-Stage Annotation Schema

Five required annotations per non-echo stage:
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:.
Derivation runs backward from echo; YAML annotations are transcribed from the backward
derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction. Row 0 is
where derivation begins, not where execution ends. # Band: omitted from echo is correct.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

Open the catalog now. Verify each selected skill maps to a declared zone per the Zone Decision
Tables. Skills with no matching zone are discarded.

---

#### Step 4 -- Assign Skills to Phases

Map each skill to its declared phase. Verify the assignment satisfies the Zone Decision Table
artifact floor for that zone.

---

#### Step 5a -- Design Gates

For each non-echo stage, use the compound gate format. Verify gate pattern class matches the
Zone Decision Table row for that zone. Dependency zones carry dual-position reminders:

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

Zone Decision Table gate pattern class column specifies the required count floor per zone:
breadth and depth `>= 2`; synthesis `>= 1`. At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each stage: verify gate artifact type is producible by a skill in that stage's `skills` list.

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

**ARTIFACT 2 is the sole authoritative source for all per-stage annotations.** YAML is
transcribed from ARTIFACT 2, not authored independently.

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

| Stage | Zone Decision Table satisfied? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|-------------------------------|-------------------------------------|--------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

Any NO triggers revision.

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-49: all criteria
[ ] C-47: gate_fail: C-41 entry has full unabbreviated Why:
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as BLOCK AUDIT PROTOCOL components
[ ] Zone Decision Tables: breadth, depth, synthesis each have 3-row commit criteria table
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
exact field line. This is the BLOCK AUDIT PROTOCOL co-location family (see BLOCK AUDIT PROTOCOL
section above for the protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in BLOCK AUDIT PROTOCOL C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in BLOCK AUDIT PROTOCOL C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in BLOCK AUDIT PROTOCOL C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# BLOCK AUDIT PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index:
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in BLOCK AUDIT PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in BLOCK AUDIT PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in BLOCK AUDIT PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in BLOCK AUDIT PROTOCOL above)

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

# BLOCK AUDIT PROTOCOL -- Component 3: Exit Verified.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

## V-04 -- Inertia Framing Axis (Per-Step AVOID Blocks)

**Axis**: Single-axis variation on inertia framing. Every construction step header carries an
explicit AVOID block naming the concrete F-1 behavior that step displaces. The status-quo
competitor is foregrounded at each decision point rather than only at the opening taxonomy.
A model reading Step 2 sees the inertia behavior it must avoid before any other instruction.
Protocol: ANNOTATION VERIFICATION PROTOCOL.

**Hypothesis**: Concentrating inertia framing at the step header level -- not just at the
opening failure taxonomy -- makes the status-quo path visible at the exact moment a model
would otherwise default to it. Step 2 AVOID block names catalog-opening. Step 3 AVOID block
names skill-first phase assignment. Step 5a AVOID block names prose gate construction.
Each AVOID block is short (1-2 sentences) and names the inertia behavior specifically.
Anticipated: 300/310 (C-50 and C-51 not targeted in this axis).

**C-47 form**: Full Why: in C-41 prose entries as per ANNOTATION VERIFICATION PROTOCOL.
**C-48 form**: Each C-41 entry back-refs protocol section; C-42 table has per-row forward-refs.
**C-49 form**: `## ANNOTATION VERIFICATION PROTOCOL`; BAD PLAN header: `# ANNOTATION
VERIFICATION PROTOCOL -- Component 1: Header Index`; footer: `# ANNOTATION VERIFICATION
PROTOCOL -- Component 3: Exit Verified`.
**Inertia framing form**: Every numbered step header (`#### Step N -- Name`) is followed by
an `**AVOID (F-1):**` block naming the concrete status-quo behavior displaced.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

**Failure mode to prevent (F-1):** catalog-first construction -- opening the skill catalog
before declaring arc phases. Zone membership becomes implicit; gates collapse to prose checks;
investigative intent disappears from the artifact.

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

## ANNOTATION VERIFICATION PROTOCOL

The BAD PLAN block at the end of this prompt is a bounded teaching unit with three components.

**Component 1 -- Header Index (C-41 + C-44 + C-47 + C-48)**: Pre-scan annotation-type index.
Each entry names: field type, criterion, exact tag string with full Why: where applicable, and
a per-entry back-reference to this section. Affirmatively covers all 7 criteria.

**Component 2 -- Block Body (C-26, C-37, C-39)**: Wrong YAML with criterion tags at every
violating field line.

**Component 3 -- Exit Verification (C-46)**: Footer confirming all Component 1 annotation
types present in block body.

Navigation contract (C-45 + C-48): This section (ANNOTATION VERIFICATION PROTOCOL) is the
protocol declaration. The FIELD CO-LOCATION PRINCIPLE section carries per-row forward-refs to
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

**AVOID (F-1):** Writing a topic name that is already a skill cluster (e.g., "scout and draft
phase"). The topic is the feature or capability being investigated -- not the method for
investigating it.

State the topic name.

---

#### Step 2 -- Declare Arc Phases

**AVOID (F-1):** Opening the catalog and grouping skills into phases. The catalog must stay
closed. Declare phases from first principles: what questions must be answered, in what order,
to commit to shipping this feature? Name phases after investigation goals, not namespace clusters.

**The catalog must remain closed at this step.** Declare 3--6 phase boundaries. Assign each
to a zone: `breadth`, `depth`, or `synthesis`.

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
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:.
Derivation runs backward from echo; annotations transcribed from backward derivation, not
authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction. Row 0 is
where derivation begins, not where execution ends.
```

Produce **ARTIFACT 1 -- Band Taxonomy Table**: `Band ID | Namespaces | Zone | Gap class | Owner role`.

---

#### Step 3 -- Select Skills

**AVOID (F-1):** Selecting all skills in a namespace because the phase exists. Select skills
that produce artifacts directly answering the phase's investigative question.

Open the catalog now. Select skills relevant to the topic. Note the declared phase each maps to.

---

#### Step 4 -- Assign Skills to Phases

**AVOID (F-1):** Creating new phases to accommodate skills with no matching phase. Discard
skills that don't map to a declared phase -- do not create phases around the skill catalog.

Map each skill to its declared phase. No new phases.

---

#### Step 5a -- Design Gates

**AVOID (F-1):** Writing a gate like `"done"` or `"all tasks complete"`. This is an
execution-history check -- verifiable only by asking "did we do this?" not by inspecting
artifacts. Gates must be artifact-verifiable: checking whether an artifact exists and meets
a count threshold, independent of execution history.

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

| Form | Verdict | Reason |
|------|---------|--------|
| `discovery::scout-feasibility >= 3 AND scout:market artifact exists` | PASS | stage-id prefix, threshold, skill ref |
| `adequate discovery signals present` | FAIL C-04 | no prefix, no threshold, not artifact-verifiable |

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

**AVOID (F-1):** Referencing an artifact type in a gate that no skill in the current stage
can produce. Forward references make gates unverifiable at the stage where they appear.

For each stage: verify gate artifact type is producible by a skill in that stage's `skills` list.

---

#### Step 6 -- Phase Intent Questions

**AVOID (F-1):** Writing a non-interrogative intent like "Assess the market" or "Validate the
spec." Intent questions must end with `?` and be specific to the zone decision.

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess compliance"` -- not interrogative

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

**AVOID (F-1):** Authoring YAML annotations from skill knowledge rather than transcribing from
ARTIFACT 2. Annotations authored independently can diverge from the matrix; transcription cannot.

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

**AVOID (F-1):** Skipping this step or treating it as optional. Any NO in the table below
requires revision before Step 10.

| Stage | `phase:` maps to zone? | Compound `{stage-id}::` with `>=N`? | `intent:` interrogative? |
|-------|------------------------|-------------------------------------|--------------------------|
| [stage 1] | YES / NO | YES / NO | YES / NO |

---

#### Step 10 -- Terminal Validation Checklist

```
[ ] C-01 through C-49: all criteria
[ ] C-47: gate_fail: C-41 entry has full unabbreviated Why:
[ ] C-48: per-entry bidirectional navigation in C-41 and C-42
[ ] C-49: C-41/C-42/C-46 labeled as ANNOTATION VERIFICATION PROTOCOL components
[ ] Per-step AVOID blocks present at every Step N header
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
exact field line. This is the ANNOTATION VERIFICATION PROTOCOL co-location family (see
ANNOTATION VERIFICATION PROTOCOL section above for the protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Entry (1) in C1 below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Entry (2) in C1 below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Entry (3) in C1 below |

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below

```yaml
# ANNOTATION VERIFICATION PROTOCOL -- Component 1: Header Index (C-41 + C-44 + C-47 + C-48)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# Annotation-type index:
#   Entry (1) C-26: gate_fail: field carries # WRONG C-04: Why: execution-history check, not artifact-verifiable
#             (rule declared in ANNOTATION VERIFICATION PROTOCOL above)
#   Entry (2) C-37: name: field carries # WRONG C-06
#             (rule declared in ANNOTATION VERIFICATION PROTOCOL above)
#   Entry (3) C-39: skills: entries carry # WRONG C-03
#             (rule declared in ANNOTATION VERIFICATION PROTOCOL above)
#   Entry (4) C-38: this header -- affirmative full-criterion coverage (all 7 / C-01 through C-07)
#             (rule declared in ANNOTATION VERIFICATION PROTOCOL above)

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

# ANNOTATION VERIFICATION PROTOCOL -- Component 3: Exit Verified.
# All annotation types from Component 1 header index confirmed present in block above.
```

---

## V-05 -- Combined Axis (C-50 + C-51: Table Index + Protocol First)

**Axis**: Combined variation. The BOUNDED BLOCK PROTOCOL section appears FIRST in the prompt
(satisfying C-51), AND the BAD PLAN header index is a 4-column pipe-delimited markdown table
(satisfying C-50). This is the only variate that targets both new v16 criteria simultaneously.
Protocol name: BOUNDED BLOCK PROTOCOL (same as V-02 to test whether C-50 and C-51 coexist
under the same protocol name with different structural choices).

**Hypothesis**: Combining protocol-first placement (C-51) with a tabular C-41 index (C-50)
tests whether the two criteria reinforce or conflict. Principle-before-instance architecture
(protocol first) declares the table structure before a model encounters the BAD PLAN header,
giving prior context for both the protocol name AND the tabular format expected in Component 1.
A model reading the BOUNDED BLOCK PROTOCOL component spec encounters: "Component 1 is a
4-column table with columns field type / criterion / tag string / back-ref" before reaching
the BAD PLAN header. Anticipated: 310/310.

**C-51 form**: BOUNDED BLOCK PROTOCOL appears before three-class table, lifecycle zones,
catalog, and construction steps. Only a single opening sentence precedes it.
**C-50 form**: BAD PLAN C1 header is a 4-column pipe table: field type | criterion | exact tag
string with full Why: | C-42 back-ref. Same table format as V-01, embedded in V-02's protocol.
**C-47 form**: Full Why: text in column 3 of the table: `# WRONG C-04: Why: execution-history
check, not artifact-verifiable`.
**C-48 form**: Column 4 per row: `BOUNDED BLOCK PROTOCOL decl. above`; FIELD CO-LOCATION
PRINCIPLE table has `BAD PLAN entry` column per row.
**C-49 form**: `## BOUNDED BLOCK PROTOCOL`; BAD PLAN header: `# BOUNDED BLOCK PROTOCOL --
Component 1: Header Index (4-column table)`; footer: `# BOUNDED BLOCK PROTOCOL -- Component 3:
Exit Verification (C-46) complete`.

---

### FULL PROMPT BODY

You are producing a `program.yaml` for the Signal plugin. The program sequences plugin skills
into staged phases with handoff gates and topic tracking. Every skill runs standalone; the program
is a plan, not an executor. Echo is the terminal consumer: its implicit information needs seed the
entire backward derivation determining every prior stage's Produces/Consumes pair.

---

## BOUNDED BLOCK PROTOCOL

Before construction: the BAD PLAN block at the end of this prompt is a bounded teaching unit.
Understanding the protocol before construction prevents incomplete or malformed blocks.

**Component 1 -- Header Index (C-41 + C-44 + C-47 + C-48 + C-50)**

The BAD PLAN header is a 4-column pipe-delimited table. Columns:

| Column | Content | Criteria satisfied |
|--------|---------|-------------------|
| Field type | Which YAML field carries the annotation (gate_fail:, name:, skills: entry, this header) | C-41 |
| Criterion | Criterion number governing that field (C-26, C-37, C-39, C-38) | C-41 |
| Exact tag string | The annotation string as it appears at the field, including full Why: clause where applicable | C-44 + C-47 |
| C-42 back-ref | Per-row reference to this section (BOUNDED BLOCK PROTOCOL above) | C-48 |

All 7 criteria must be covered in the header table (C-38 affirmative coverage).

**Component 2 -- Block Body (C-26, C-37, C-39)**

Wrong YAML with criterion tags at every violating field line. Field-level tags match the tag
strings specified in Component 1 column 3.

**Component 3 -- Exit Verification (C-46)**

Footer confirming all annotation types from Component 1 table were found present in the block body.

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
  # Band:     [meta-structure entry ID]
  # Gap:      [investigative question, interrogative, ends with ?]
  # Owner:    [PM / Architect / Dev / Team Lead]
  # Consumes: [artifact type(s) required as input]
  # Produces: [artifact type(s) yielded as output]

Consumer-pull rule: # Produces: is set by what the NEXT stage declares as # Consumes:.
Derivation runs backward from echo; YAML annotations are transcribed from the backward
derivation, not authored from skill knowledge.

ROW-0 RULE: Echo occupies row 0 of ARTIFACT 2. This encodes derivation direction. Row 0 is
where derivation begins, not where execution ends.
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

PASS: `discovery::scout-feasibility >= 3 AND scout:market artifact exists`
FAIL: `"done"` -- Why: execution-history check, not artifact-verifiable

At least one gate must include `>= N`.

---

#### Step 5b -- FORWARD REFERENCE Audit

For each stage: verify gate artifact type is producible by a skill in that stage.

---

#### Step 6 -- Phase Intent Questions

- PASS: `"Do we understand the compliance landscape well enough to commit to a direction?"`
- FAIL: `"Assess compliance"` -- not interrogative

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
[ ] C-47: gate_fail: C-41 entry includes full unabbreviated Why:
[ ] C-48: per-entry bidirectional navigation (each C-41 entry has own back-ref; C-42 per-row forward-refs)
[ ] C-49: C-41/C-42/C-46 labeled as BOUNDED BLOCK PROTOCOL components
[ ] C-50: C-41 index is a 4-column pipe-delimited table (field type / criterion / tag string / C-42 back-ref)
[ ] C-51: BOUNDED BLOCK PROTOCOL section is the FIRST major structural section in the document
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
PROTOCOL section above for the protocol declaration):

| Field type | Criterion | Required annotation tag | Co-location rule | BAD PLAN entry |
|------------|-----------|-------------------------|------------------|----------------|
| `gate_fail:` | C-04 (C-26) | `# WRONG C-04: Why: execution-history check, not artifact-verifiable` | At gate_fail: line | Row (1) in BOUNDED BLOCK PROTOCOL C1 table below |
| `name:` | C-06 (C-37) | `# WRONG C-06` | At name: line | Row (2) in BOUNDED BLOCK PROTOCOL C1 table below |
| `skills:` entry | C-03 (C-39) | `# WRONG C-03` | At skills-list entry line | Row (3) in BOUNDED BLOCK PROTOCOL C1 table below |

Each row above maps to a specific row in the Component 1 table in the BAD PLAN header below.

---

## BAD PLAN -- all 7 criteria (C-01 through C-07) indexed in BOUNDED BLOCK PROTOCOL C1 below

```yaml
# BOUNDED BLOCK PROTOCOL -- Component 1: Header Index (4-column table) (C-41+C-44+C-47+C-48+C-50)
# All 7 criteria covered (C-01 through C-07) -- essential and recommended violations
#
# | Field type    | Criterion   | Exact tag string (full Why: per C-47)                                | C-42 back-ref (C-48)              |
# |---------------|-------------|----------------------------------------------------------------------|-----------------------------------|
# | gate_fail:    | C-04 (C-26) | # WRONG C-04: Why: execution-history check, not artifact-verifiable  | BOUNDED BLOCK PROTOCOL decl. above |
# | name:         | C-06 (C-37) | # WRONG C-06                                                         | BOUNDED BLOCK PROTOCOL decl. above |
# | skills: entry | C-03 (C-39) | # WRONG C-03                                                         | BOUNDED BLOCK PROTOCOL decl. above |
# | this header   | C-38        | affirmative full-coverage claim (all 7 / C-01 through C-07)          | BOUNDED BLOCK PROTOCOL decl. above |

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
# All annotation types from Component 1 header table confirmed present in block above.
```
