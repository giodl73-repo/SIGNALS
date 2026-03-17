---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 3
rubric: trace-skill-rubric-v3-2026-03-15.md
---

# trace-skill -- Variations R3 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

Round 3 target: C-11 and C-12 -- the two new v3 aspirational criteria.

R2 V-04 and V-05 both hit 100 under v3 via heavy architecture (two-stage auditor + relay tables
+ source column). Round 3 explores alternative paths:
- V-01: lifecycle gates (layer coverage gate + source-confirmed field) without a pre-audit stage
- V-02: conversational interrogative register with embedded layer-type questions
- V-03: unified gap-to-resolution ledger (Findings + Amend collapsed into one table)
- V-04: diversity-first auditor (source-layer diversity as auditor success criterion) + token notation
- V-05: named verification checkpoints (Layer Diversity Check, Source-Type Verification) + inertia framing

Single-axis selections: Lifecycle emphasis (V-01), Phrasing register (V-02), Output format (V-03).
Combined selections: Role sequence + concrete tokens (V-04), Lifecycle emphasis + inertia framing (V-05).

---

## V-01 -- Single axis: Lifecycle emphasis (layer-coverage gate + source-confirmed field)

**Axis**: Lifecycle emphasis -- two named verification checkpoints are inserted directly into the
lifecycle without adding a pre-audit stage: (1) a LAYER COVERAGE GATE at the end of Findings that
blocks Amend if fewer than two distinct source types are present, and (2) a Source confirmed field
required in every Amend entry. Both checkpoints are explicit named steps, not emergent from table
structure.

**Hypothesis**: Lifecycle gates directly target C-12 (layer coverage gate blocks single-layer
findings tables from proceeding) and C-11 (source-confirmed field blocks Amend entries that
omit source-type verification). This achieves the same enforcement as R2 V-04/V-05 without
the two-stage architecture or relay notation overhead. Risk: the gate is at the end of Findings,
which means the tracer may have already written a single-layer table and must then backfill --
compared to a pre-audit that surfaces multi-layer gaps before Execute, this is reactive
enforcement. A tracer who finds the gate late may add a superficial finding to pass it.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase 1 -- Setup

Read `{{skill_spec_path}}`. Confirm each input before executing:

- **Topic**: from the test invocation
- **Scope**: what this trace covers; what it explicitly excludes
- **Roles**: full stock list from the spec; any custom roles in `.craft/roles/signal/`
- **Stack**: detected from repo context (package.json / CLAUDE.md / assertion); name the
  detection method
- **Spec version**: from spec frontmatter if present

Any input that cannot be confirmed: label SG-NN and record here. Do not infer silently -- a
silent assumption in Setup becomes an invisible constraint in Execute.

**Phase gate**: Confirm topic, scope, and roles (or label each unconfirmable item SG-NN)
before proceeding.

---

### Phase 2 -- Execute

Carrying forward from Setup: topic `{{topic}}`, scope `{{scope}}`, roles `{{roles}}`.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the skill spec requires must appear. Run each role in sequence. For each role:

1. State what the role received (from Setup or the prior role's output)
2. State what the role contributed to the artifact
3. Any required output that cannot be produced: label EG-NN and mark the artifact section
   explicitly

Do not infer silently at any decision point. A silently filled gap is a gap the implementer
will rediscover at runtime.

Carry forward to Findings: artifact at `{{artifact_path}}`, gaps SG-NN and EG-NN recorded above.

---

### Phase 3 -- Findings

Carrying forward: artifact at `{{artifact_path}}`, all gaps from Setup and Execute.

**Source vocabulary** -- required on every finding:

| Label | Meaning | Remediation layer |
|-------|---------|------------------|
| SA | Gap in the spec (spec does not define this input, output, or decision) | Spec revision |
| SG | Gap at setup time (input not available from invocation or repo) | Invocation / documentation change |
| EG | Gap at execute time (required section or role output missing) | Skill implementation change |
| QO | Quality observation (artifact improvable; not a blocking gap) | Advisory |

Produce the findings table. Source column required for every row:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. Each finding must state the action required, not only the observation.

---

**LAYER COVERAGE GATE**

Before proceeding to Amend, verify:

- Count distinct Source types in the findings table.
- If only one Source type appears: identify one finding from an unrepresented layer. Check
  the spec for undefined inputs or handoffs (SA candidates) and the artifact contract for
  missing section definitions (EG candidates). Add the finding before proceeding.
- If two or more distinct Source types appear: proceed.

Record: `[layers covered: {{source_types}}]`

A single-layer findings table means at least one structural failure mode was not inspected.
This gate is not optional.

---

### Phase 4 -- Amend

Carrying forward: highest-priority finding `{{F-NN}}` (Source: `{{source}}`).

Apply the finding. All four fields are required for every amendment or dismissal:

| Field | Value |
|-------|-------|
| Finding | `{{F-NN}}` |
| Source type | SA / SG / EG / QO |
| Change | [section or field changed and what changed; or "dismissed"] |
| Dismissal reason | [if dismissed: why; leave blank if applied] |
| Source confirmed | YES -- fix is at the `{{source}}` layer / NO -- [explain mismatch] |

The Source confirmed field is not decorative. If the fix operates at a different layer than
the source label indicates (e.g., an SA finding patched by changing the artifact instead of
the spec), record `Source confirmed: NO` and explain the mismatch. A mismatch does not
automatically fail the trace but must be declared.

---

### Verdict

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA finding remains unresolved after Amend.
`NEEDS-REDESIGN` if EG findings exceed 3 and cluster on a structural role gap.
`USEFUL` otherwise.

**SA findings**: [count] | **SG findings**: [count] | **EG findings**: [count]
**Layers covered**: [from Layer Coverage Gate]

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Phrasing register (conversational interrogative with embedded layer-type questions)

**Axis**: Phrasing register -- interrogative phase headers throughout, with embedded layer-type
questions at every gap detection point. The prompt asks "what layer does this gap live in?"
rather than requiring a Source column in a table. No structural tables in the prompt instructions
-- only in the outputs the tracer is asked to produce. The conversational register tests whether
question-form prompting drives C-11/C-12 compliance without mechanical table enforcement.

**Hypothesis**: Interrogative prompting activates natural carry-forward (C-09 analogue) and
embedded layer-type questions at discovery points naturalize source attribution (C-10/C-12) and
source-type verification (C-11) as thinking habits rather than table-filling obligations. Risk:
without a hard gate or explicit table column, a tracer under time pressure may provide shallow
layer identification ("probably EG") without the depth needed for C-12 diversity. Findings may
cluster at the most visible layer (EG) unless the Findings section explicitly asks for
multi-layer coverage.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Setup -- what does the spec commit to before we touch the invocation?

Read `{{skill_spec_path}}`. Before running anything, answer:

- What is the topic and test scenario? (from the invocation)
- What is in scope, and what is explicitly out? (invocation + spec)
- Which roles will run? (stock roles in the spec; custom roles in `.craft/roles/signal/`
  if present)
- What does the repo tell us automatically? (stack, contributors, existing artifacts for
  this topic -- name the detection method)

As you answer each question, note any input you cannot confirm. For each unconfirmable item,
ask: is this undefined in the spec, or is it simply not present in the invocation? The first
kind is a spec-level gap (SA-NN). The second kind is a setup-level gap (SG-NN). Label each
one before moving on -- do not silently assume a value and proceed.

---

### Execute -- what does the artifact look like when the skill runs?

Carrying forward from Setup: topic `{{topic}}`, scope confirmed, roles `{{roles}}`.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Run each role in sequence. For each role: what did it receive? what did it add to the artifact?
Write the artifact section and then, where any role encounters a missing input, a spec ambiguity,
or an undefined decision: pause and ask yourself whether this is a spec-level problem (SA), a
setup problem (SG), or an artifact-coverage problem (EG). Label it, mark the artifact section,
and continue.

The artifact must contain every section the skill spec defines. A section you skip without
labeling is a section the implementer will silently miss.

---

### Findings -- what matters and what layer does each problem live in?

Carrying forward from Execute: artifact at `{{artifact_path}}`, gaps labeled above.

Build the findings table. For every row, the Source column answers one question: where did this
problem originate?

| ID | Finding | Source | Severity | What to do |
|----|---------|--------|----------|-----------|

Rules:
- Minimum 2 entries.
- "What to do" must be a concrete action, not a restatement of the problem.
- Before leaving this section, check: do your findings represent at least two different
  source layers? If every row carries the same Source label, you have only inspected one
  dimension of the gap space. Look again at the spec and artifact contract for gaps at a
  layer you haven't surfaced yet -- spec-level gaps (SA) often hide in undefined role handoffs
  or artifact naming decisions, not in the obvious missing sections.

---

### Amend -- what changes, and does the fix land at the right layer?

Carrying forward from Findings: highest-priority finding `{{F-NN}}` (Source: `{{source}}`).

Apply the finding to the artifact. Name the finding, the section changed, and the change.
Then answer: does the fix operate at the same layer as the Source label?

- SA fix: the spec was updated -- not the artifact
- SG fix: the invocation or documentation was updated -- not the artifact
- EG fix: the artifact or role logic was changed

State explicitly: **"This is a `{{source}}` gap. The fix is at [spec / invocation / artifact]
level. Match: YES / NO."**

If you dismiss the finding instead: name it, explain why, and confirm whether the source-type
assignment was correct -- not just whether the finding itself was valid.

---

### Verdict

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

In one sentence: what does this trace tell an implementer they should do next? Reference the
highest-severity finding and its source layer. A trace that produced findings at only one
layer is a weaker signal than one that covered multiple layers -- note the difference in your
verdict reasoning if it applies.

`NEEDS-SPEC-REVISION` if any P1 SA finding is unresolved.
`NEEDS-REDESIGN` if EG findings exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Output format (gap-to-resolution ledger)

**Axis**: Output format -- Findings and Amend are collapsed into a single "gap-to-resolution
ledger" where every row carries the gap from discovery through to resolution and source-type
confirmation. The ledger format makes C-11 structurally mandatory: every row must have a
Source confirmed column entry before the trace is complete. The at-least-2-distinct-source-types
rule is declared in the ledger rules, making C-12 structurally mandatory as well. The four
lifecycle phases (Setup, Execute, Findings/Amend, Verdict) remain present but the third phase
is served by the ledger rather than two separate sections.

**Hypothesis**: A single table with ID / Finding / Source / Severity / Action / Amendment /
Source confirmed is the most compressed structure that can simultaneously enforce C-10 (source
attribution), C-11 (source-type confirmation in Amend), and C-12 (multi-layer coverage) with
zero prose overhead. Every structural requirement is a column that cannot be left blank. Risk:
collapsing Findings + Amend into one table compresses the deliberative space -- tracers may
write shallow findings to keep rows manageable, and the Amend column may receive one-word
entries ("updated") that technically satisfy C-11 without demonstrating real remediation
reasoning. The four-phase lifecycle must remain legible in this format to pass C-01.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase 1 -- Setup

Read `{{skill_spec_path}}`. Confirm before executing:

| Input | Value | Source | Gap? |
|-------|-------|--------|------|
| Topic | | invocation | |
| Scope (in) | | invocation / spec | |
| Scope (out) | | invocation / spec | |
| Roles | | spec stock list | |
| Stack | | auto-detection (state method) | |
| Spec version | | spec frontmatter | |

Mark `Gap? = SG-NN` for any row where the value cannot be determined. Do not infer silently.

**Phase gate**: Every non-gap row populated, or each gap row labeled SG-NN, before proceeding.

---

### Phase 2 -- Execute

Carrying forward from Setup: topic `{{topic}}`, scope `{{scope}}`, roles `{{roles}}`.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the spec defines must appear. Run each role in sequence. Where a role cannot
produce a required output: mark the artifact section EG-NN and continue. Absent sections
are EG-NN, not omissions.

---

### Gap-to-Resolution Ledger

This table replaces both the Findings section and the Amend section. Each row traces one gap
or quality observation from discovery through to resolution and source-type confirmation.

**Source vocabulary**:

| Label | Origin | Remediation |
|-------|--------|-------------|
| SA | Gap in the spec (spec does not define this) | Spec revision required before implementation |
| SG | Gap at setup time (input not available from invocation or repo) | Invocation or documentation change |
| EG | Gap at execute time (required artifact section or role output missing) | Skill implementation or role definition change |
| QO | Quality observation (artifact improvable; not a blocking gap) | Advisory -- no blocking action |

| ID | Finding | Source | Severity | Action | Amendment / Dismissal | Source confirmed |
|----|---------|--------|----------|--------|-----------------------|-----------------|

**Ledger rules**:

1. Minimum 2 rows. All columns required on every row -- no blanks.
2. At least 2 distinct Source types must appear across all rows. If only one type is
   represented after recording all observed gaps, add one finding from an unrepresented
   layer before closing the ledger.
3. "Amendment / Dismissal" answers: what was changed (or why the finding was dismissed)?
   Not "see above." State the specific change.
4. "Source confirmed" answers: does the amendment or dismissal address the layer the Source
   label names? Write YES or NO.
   - SA amendments change the spec, not the artifact.
   - SG amendments change the invocation or documentation, not the artifact.
   - EG amendments change the artifact or role logic.
   - QO amendments improve artifact quality without structural change.
   - If Source confirmed = NO: explain the mismatch on the same row.
5. Two rows with the same Source and the same Action must be merged.
6. SA rows with Severity = P1 and Source confirmed = NO block a `USEFUL` verdict.

---

### Verdict

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA row has Source confirmed = NO or is unresolved.
`NEEDS-REDESIGN` if EG rows exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Layers covered**: [list distinct Source types from ledger]
**SA rows**: [count] | **SG rows**: [count] | **EG rows**: [count] | **QO rows**: [count]

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Role sequence (diversity-first auditor) + concrete token notation

**Axes**:
- Role sequence: a spec-layer auditor runs as Stage 1 before hand-compilation, with source-layer
  diversity as its explicit success criterion -- the audit succeeds only when gaps from at least
  two distinct layers have been identified. This makes C-12 compliance a goal the auditor is
  trying to achieve, not a column it happens to fill.
- Concrete token notation: every phase-to-phase and stage-to-stage carry-forward uses
  `[name: value]` inline notation, freezing extracted values at transition points and making
  every dependency auditable without backtracking.

**Hypothesis**: Making source-layer diversity the auditor's stated success criterion (not just
a table requirement) changes the auditor's behavior: it will look harder for SA-level gaps when
only EG-level gaps are visible, because the criterion is not met until two layers appear. Combined
with token notation for C-09, this variation targets C-08, C-09, C-10, C-11, and C-12 via
three independent structural mechanisms. Risk: the diversity criterion may cause the auditor
to manufacture low-signal SA findings to satisfy the criterion, reducing gap quality in exchange
for layer coverage. Token notation adds length to every transition.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Stage 1 -- Source-Layer Auditor

Your job is not to run the skill. Your job is to map the gap space across all source layers
before any phase begins.

Read `{{skill_spec_path}}` and catalog every gap, organized by layer:

**Spec-level gaps (SA)**: inputs the spec does not define, role handoffs that are not specified,
artifact sections with undefined content rules, decision points requiring external knowledge.

**Setup-level gaps (SG)**: inputs the spec defines but that are not derivable from the test
invocation or repo context alone.

**Execute-level gaps (EG)**: artifact section or output requirements that the named roles may
not be able to produce as specified.

**Auditor success criterion**: this audit succeeds when gaps from at least two distinct source
layers have been identified. If all visible gaps appear at a single layer, examine harder:

- If only EG gaps: look at the spec's role handoff definitions and artifact naming contract for
  SA-level gaps.
- If only SA gaps: consider whether the invocation fully specifies all required inputs for SG
  candidates.

Produce the audit record:

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

If 0 gaps found after careful reading: add one P3 QO. A spec with zero auditable gaps has not
been examined rigorously.

**Stage 1 relay to Stage 2**: [SA gaps: `{{sa_list}}`], [SG gaps: `{{sg_list}}`],
[EG gaps: `{{eg_list}}`], [layer diversity: PASS (2+ layers) / FAIL (1 layer)].

---

### Stage 2 -- Hand-Compilation

**Stage 2 relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

SA and SG gaps from Stage 1 are inputs to every phase -- carry them forward at each transition.
Do not re-derive them and do not silently resolve them.

---

#### Phase 1 -- Setup

Using the test invocation and repo context. Write confirmed values using `[name: value]`
notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ]
- [detection_method: ]

SA gaps from Stage 1 affecting Setup: carry forward as SG-NN. New gaps discovered here: add SG-NN.

Carry forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_list}}`], [SG: `{{sg_list}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

For each role, open a role relay before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Phase 1]
- Received values: [name: value, name: value, ...]
- SA/SG gaps affecting this role: [list or "none"]
- Produced: [artifact content added]
- EG gaps found: [EG-NN list or "none"]

Carry forward: [artifact: `{{artifact_path}}`], [SA: `{{sa_list}}`],
[SG: `{{sg_list}}`], [EG: `{{eg_list}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], [all gaps: `{{gap_list}}`].

Merge all gaps from Stage 1 and Stage 2 into the unified findings table. Source column required.
Entries with the same Source type must carry distinct action directions. If Stage 1 layer
diversity was PASS, the two-layer requirement is already met -- verify the merged table reflects it.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|
| | | SA / SG / EG / QO | P1/P2/P3 | |

Minimum 2 entries with at least 2 distinct Source types.

Carry forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

---

#### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [source type confirmed: YES (source label was correct) / NO (source label needs revision)]

---

### Verdict

**Stage 1 layer diversity**: PASS / FAIL -- [note]
**SA gaps**: [count] -- spec revision required before implementation
**SG gaps**: [count] -- invocation or documentation update
**EG gaps**: [count] -- skill implementation change

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap is unresolved.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined axes: Lifecycle emphasis (named verification checkpoints) + inertia framing

**Axes**:
- Lifecycle emphasis: two verification checkpoints are inserted as named, visually distinct
  steps in the lifecycle -- LAYER DIVERSITY CHECK between Findings and Amend, and SOURCE-TYPE
  VERIFICATION at the end of Amend. Unlike V-01's gate (which blocks if the criterion is not
  met), these checkpoints name the criterion, explain why it exists, and require a declared
  result. The "named step" design makes C-11 and C-12 visible requirements a tracer must
  acknowledge by name, not structural constraints they may not see.
- Inertia framing: the prompt opens with a "without this skill" statement and each checkpoint
  is followed by a one-sentence cost statement explaining what failure at that checkpoint would
  mean for a developer without the trace. Inertia framing converts abstract rubric criteria
  into developer decisions.

**Hypothesis**: Making C-11 and C-12 visible as named lifecycle steps converts them from
scoring criteria into operational requirements the tracer knows they must satisfy. Combined
with inertia framing that explains the cost of failure at each checkpoint, this variation tests
whether motivation is as effective as mechanical enforcement for producing compliant behavior.
Risk: named steps without hard gates can be nominally satisfied -- a tracer may write
"Layer Diversity Check: 2 EG and 1 SA found, PASS" without substantive multi-layer coverage.
The conversational cost framing may not override time-pressure shortcuts.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Without `/{{skill_name}}`**: A developer validating this skill would read the spec manually,
mentally simulate role behavior, and discover implementability gaps only after writing code.
Each gap found in this trace is a failure they would have paid for later. The source layer a
gap lives in (spec / setup / execute) determines who pays and when -- a spec-layer gap caught
here saves implementation work; the same gap missed here surfaces as a runtime defect.

---

### Phase 1 -- Setup

Read `{{skill_spec_path}}`. Confirm each input from the test invocation and repo context:

- **Topic**: named from the invocation
- **Scope**: what is in; what is out
- **Roles**: stock list from spec; custom roles in `.craft/roles/signal/` if present
- **Stack**: auto-detected from repo (name method and result)

Undefined inputs: label SG-NN. Do not infer silently. Each SG-NN is a gap the developer would
have guessed past -- note it so the trace surfaces the cost.

---

### Phase 2 -- Execute

Carrying forward from Setup: topic `{{topic}}`, scope `{{scope}}`, roles `{{roles}}`.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the spec defines must appear. Run each role in sequence. Where a role encounters
a missing input, undefined spec decision, or circular dependency: label EG-NN and mark the
artifact section explicitly. Do not infer -- a filled-in gap is a gap the implementer cannot see.

---

### Phase 3 -- Findings

Carrying forward from Execute: artifact at `{{artifact_path}}`, all gaps recorded.

Source vocabulary:

| Label | Origin | Remediation |
|-------|--------|-------------|
| SA | Spec does not define this | Spec must be revised before implementation |
| SG | Input not available at invocation time | Invocation or documentation change |
| EG | Required artifact section or role output absent | Skill logic or role definition change |
| QO | Quality observation; artifact improvable | Advisory -- no blocking action |

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries with concrete action directions.

---

**LAYER DIVERSITY CHECK**

*Without this check, a trace that surfaces only execute-level gaps gives an implementer a
misleading sense of completeness. Spec-layer and setup-layer gaps have different owners --
missing them means the fix request goes to the wrong person.*

Count distinct Source types in the findings table above.

- **1 distinct type**: the trace has only inspected one structural dimension. Examine the spec
  for undefined inputs or role handoffs (SA candidates) and the invocation for setup-level
  ambiguities (SG candidates). Add at least one finding from a different layer before proceeding.
- **2+ distinct types**: proceed.

Record: `[layers covered: {{source_types}}]`

---

### Phase 4 -- Amend

Carrying forward from Findings: highest-priority finding `{{F-NN}}` (Source: `{{source}}`).

Apply the finding. State the finding ID, source type, section changed, and the change.

---

**SOURCE-TYPE VERIFICATION**

*Without this step, a developer could apply an EG-style artifact patch to what is actually a
spec-layer gap. The patch appears to work at first; the gap resurfaces at the next invocation
because the spec was never updated.*

Answer: does the fix operate at the layer the Source label names?

- SA fix: the spec was updated (not the artifact)
- SG fix: the invocation or documentation was updated (not the artifact)
- EG fix: the artifact or role logic was changed
- QO fix: artifact quality was improved without structural change

Write: **`Source type: {{source}}. Fix applied at: [spec / invocation / artifact / quality]. Match: YES / NO.`**

If Match = NO: explain the mismatch and revise the fix to target the correct layer, or state
explicitly why cross-layer remediation is justified in this case.

If dismissed: state the finding ID, the dismissal reason, and confirm: was the source-type
assignment correct?

---

### Verdict

**Without this skill**: [one sentence -- what the developer would have done manually]
**With this skill**: [one sentence -- what the developer now has instead]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA finding is unresolved.
`NEEDS-REDESIGN` if EG gaps exceed 3 and cluster on a structural role gap.
`USEFUL` otherwise.

**Layers covered**: [from Layer Diversity Check]
**SA findings**: [count] | **SG findings**: [count] | **EG findings**: [count]

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
