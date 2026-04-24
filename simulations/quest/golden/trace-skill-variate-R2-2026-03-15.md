---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 2
rubric: trace-skill-rubric-v2-2026-03-15.md
---

# trace-skill -- Variations R2 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: All earlier rounds (R1-R8) used a Setup/Execute/Findings/Amend phase schema
inherited from earlier trace-* skill conventions. Rubric v2 (this round's rubric) introduces a
new canonical 4-phase schema: **Gather / Bind / Execute / Verdict**. No prior round can satisfy
C-01 or C-06 because they use wrong phase labels. Round 2 is a clean-slate redesign.

**v2 rubric structure**:

Essential (all must pass):
- C-01: Phases present in sequence: Gather, Bind, Execute, Verdict
- C-02: Gather enumerates all inputs by name with source
- C-03: Bind maps every Gather input to a single resolved value
- C-04: Execute produces target skill artifact with correct naming and sections
- C-05: Verdict declares explicit PASS/FAIL with rationale

Recommended:
- C-06: Phases carry exact schema labels (Gather/Bind/Execute/Verdict)
- C-07: Verdict cites criterion IDs, not free-form prose
- C-08: Artifact complete -- no elision markers anywhere

Aspirational:
- C-09: Gather includes Coverage Matrix table with closed-world preamble
- C-10: Execute relays carry (role, signal, binding, status) fields; Verdict reads relay, not reconstructs
- C-11: Gather enumerates spec inputs before invocation inputs
- C-12: Coverage Matrix includes BLOCKED declaration: any Gap=YES halts immediately
- C-13: Execute wraps artifact with delimiter markers ([ARTIFACT BEGINS HERE] / [ARTIFACT ENDS HERE])

**Round 2 variation axes**:

Single-axis:
- V-01: Phrasing register -- formal/imperative, canonical labels locked with compliance-ledger Verdict;
  targets C-01, C-05, C-06, C-07
- V-02: Gather ordering -- spec-first two-tier enumeration before invocation inputs;
  targets C-02, C-11
- V-03: Bind as resolution ledger -- explicit table enforcing one resolved value per input
  with BLOCKED/CONTINUED status vocabulary; targets C-03, C-08

Combined:
- V-04: Coverage Matrix + BLOCKED gate -- closed-world preamble before Gather with halt semantics;
  targets C-09, C-12
- V-05: All aspirationals -- Coverage Matrix, relay carry, spec-first Gather, BLOCKED gate,
  delimiter markers; targets C-09 through C-13 complete

---

## V-01 -- Single axis: Phrasing register (formal/imperative, canonical labels)

**Axis**: Phrasing register -- formal imperative language with canonical phase label enforcement.
The four phase headers are declared as immutable schema names before the trace begins. Any output
that uses a synonym (Setup, Resolve, Run, Summary) instead of the exact canonical label is a
structural violation. The Verdict is formatted as a compliance ledger that cites criterion IDs
directly, not prose description of what passed.

**Hypothesis**: Declaring the phase labels as immutable schema names before the trace begins
makes C-01 and C-06 structural -- a model that uses synonym headers is not producing a valid
trace, which the compliance ledger makes visible at Verdict time. Forcing criterion-ID citation
in the Verdict (C-07) prevents the Verdict from degenerating into a narrative summary that
satisfies C-05 by saying "everything looks fine." Risk: formal label enforcement may produce
rigid phase boundaries that suppress carry-forward reasoning; Bind in particular may become a
mechanical table-fill with no analytic content if the model treats it as a rename of Gather.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema

The four canonical phase labels for this trace are locked. Use them exactly as listed.

| # | Canonical label | Invalid synonyms (do not use) |
|---|----------------|-------------------------------|
| 1 | **Gather** | Setup, Intake, Read, Context, Collect |
| 2 | **Bind** | Resolve, Map, Configure, Init, Prepare |
| 3 | **Execute** | Run, Simulate, Produce, Compile, Perform |
| 4 | **Verdict** | Result, Summary, Assessment, Output, Conclusion |

A section header using a synonym instead of the canonical label is a structural violation.
This constraint is checked at VC-1 in the Verdict compliance ledger.

---

### Gather

Read the skill spec at `{{skill_spec_path}}`. Enumerate every input required to run this skill.
For each input: state its name and its source (spec-defined, invocation-supplied, repo-detected,
or inferred). An input without a confirmed source is a Gap. Label each gap G-NN. Do not proceed
to Bind until every required input is listed -- present or gap.

| Input | Source | Value | Gap? |
|-------|--------|-------|------|
| skill_name | invocation | {{skill_name}} | NO |
| skill_spec_path | invocation | {{skill_spec_path}} | NO |
| topic | invocation-parsed | | |
| invocation | invocation | {{invocation}} | NO |
| [spec-required input N] | spec | | |

Add one row per input the spec declares as required. A spec-required input the invocation does
not supply is Gap=YES -- label it G-NN and carry to Bind.

---

### Bind

Map every input from the Gather table to a single resolved value. Every Gather row must appear
here. An input that cannot be resolved to a single value is UNRESOLVED (carry the G-NN label).
Do not execute with UNRESOLVED inputs without stating why the trace is proceeding and what the
impact is on the artifact. Proceeding past an UNRESOLVED input without explanation is a Bind
violation.

| Input | Gathered value | Resolved value | Status |
|-------|---------------|----------------|--------|
| skill_name | {{skill_name}} | {{skill_name}} | RESOLVED |
| skill_spec_path | {{skill_spec_path}} | {{skill_spec_path}} | RESOLVED |
| topic | [from invocation] | [resolved topic] | RESOLVED / UNRESOLVED (G-NN) |
| [spec-required input N] | | | |

If any row is UNRESOLVED: state whether it blocks Execute or whether Execute can proceed with
a gap marker. Explain the decision.

---

### Execute

Carrying forward: all inputs from Bind, with UNRESOLVED gaps noted.

Produce the hand-compiled artifact as if `/{{skill_name}}` had run on the test invocation.

The artifact:
- Is named `{topic}-{signal}-{date}.md`
- Has every section the skill spec defines as required output
- Has no placeholder values requiring post-production resolution
- Has no elision markers (no "...", "[content here]", "[omitted for brevity]")

Run each stock role the spec defines, in sequence. For each role: state what it receives and
what it contributes to the artifact. Where a role encounters an absent required input (due to
UNRESOLVED gaps from Bind), record Execute Gap EG-NN at the affected artifact section -- do not
silently omit the section.

After producing the artifact, list any EG-NN gaps found.

---

### Verdict

Assess the trace against each rubric criterion. Cite criterion IDs in the table. Do not use
prose summaries in place of criterion-referenced evidence.

| Criterion | PASS / FAIL | Evidence locus |
|-----------|-------------|----------------|
| C-01 | | Phase headers present in document structure |
| C-02 | | Gather table row count vs spec input count |
| C-03 | | Bind table row count vs Gather row count |
| C-04 | | Artifact section count vs spec-required section count |
| C-05 | | This table, Overall result row |
| C-06 | | Phase header labels compared to Phase Label Schema |
| C-07 | | Criterion IDs cited in this table |
| C-08 | | Artifact scanned for elision markers |

**Overall result**: PASS (all C-01 through C-05 are PASS) / FAIL (name failing essential criterion and why)

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Gather ordering (spec-first two-tier enumeration)

**Axis**: Gather ordering -- the Gather phase is structured in two explicit tiers. Tier 1
enumerates every input the skill spec defines, regardless of what the invocation supplies.
Tier 2 maps the invocation onto those spec-defined slots, adding any invocation-only refinements.
The spec anchors the input space; the invocation is a constraint layer applied on top.

**Hypothesis**: When Gather begins from the invocation rather than the spec, the tracer risks
enumerating only what the invocation explicitly mentions and missing spec-required inputs the
invocation leaves implicit. Spec-first enumeration forces the tracer to read the spec before
reading the invocation, surfacing all required inputs including optional ones not present in
this specific test invocation. C-11 (spec inputs before invocation inputs) is satisfied
structurally by the tier separation -- it cannot be violated unless the tracer reverses the
tiers, which the instructions explicitly prohibit. C-02 coverage improves because the spec is
the complete input authority, not the invocation. Risk: the spec may require reading multiple
sections to enumerate all inputs; the tier structure does not help with a poorly organized spec,
only the instruction to read the whole spec before starting Tier 1 does.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Gather

**Before reading the invocation**: Read `{{skill_spec_path}}` completely. Enumerate every input
the spec declares (required and optional) in Tier 1. Only then read the invocation for Tier 2.

#### Gather Tier 1 -- Spec-defined inputs (spec read first, before invocation)

List every input the spec declares. Record: name, required or optional, source type (invoker-
supplied, repo-detected, or spec-defaulted), and the spec-defined default if one exists.

| Input | Required? | Source type | Spec default | Notes |
|-------|-----------|-------------|-------------|-------|
| skill_name | YES | invoker-supplied | none | |
| skill_spec_path | YES | invoker-supplied | none | |
| topic | YES | invoker-supplied | none | |
| [spec-defined input N] | | | | |

Do not consult the invocation for this tier. Record what the spec says, not what the invocation
supplies. Do not skip optional inputs -- an optional input with no default that the invoker does
not supply is still a gap candidate.

#### Gather Tier 2 -- Invocation-supplied values

Now read the test invocation: `{{invocation}}`

Map each invocation token to a Tier 1 slot. Add any invocation-only inputs (topic refinements,
scenario specifics) as additional Tier 2 rows. Flag any Tier 1 Required input that the
invocation does not supply as G-NN.

| Tier 1 input | Invocation value | Present in invocation? |
|--------------|-----------------|----------------------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| [spec-defined input N] | | YES / NO (G-NN) |

**Carry forward**: the merged input set (Tier 1 defaults + Tier 2 invocation values, with G-NN
gaps flagged) to Bind.

---

### Bind

Merge Tier 1 defaults and Tier 2 invocation values. For each input, produce one resolved value.
Conflict rule: when a Tier 1 default and a Tier 2 invocation value differ, the invocation wins
-- state this explicitly. When neither Tier supplies a value, the input is UNRESOLVED (G-NN).

| Input | Resolution source | Resolved value | Status |
|-------|------------------|----------------|--------|
| | Tier 1 default / Tier 2 invocation / Tier 2 wins over Tier 1 | | RESOLVED / UNRESOLVED (G-NN) |

An UNRESOLVED Required input blocks Execute. State whether this trace can proceed and why.

---

### Execute

Carrying forward: resolved inputs from Bind. Produce the hand-compiled artifact:
`{topic}-{signal}-{date}.md`

Run each stock role in spec-defined order. For each role, produce its contribution to the
artifact. Sections the spec requires but that an UNRESOLVED gap prevents are marked EG-NN --
not silently omitted.

The artifact must be complete: every spec-required section present, no elision markers.

---

### Verdict

| Criterion | PASS / FAIL | Evidence |
|-----------|-------------|----------|
| C-01 | | Four phase headers present in sequence |
| C-02 | | Tier 1 input count vs spec input count; source column populated |
| C-03 | | Bind row count vs Gather row count; one value per row |
| C-04 | | Artifact section count vs spec-required sections; naming convention applied |
| C-05 | | This table, Overall result |
| C-11 | | Tier 1 section precedes Tier 2 section in Gather |

**Overall result**: PASS / FAIL
**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Bind as resolution ledger

**Axis**: Bind as resolution ledger -- Bind is an explicit ledger table with one row per Gather
input, enforcing the contract that every gathered input must have exactly one resolved value
before Execute begins. The Status column uses three values only: RESOLVED, UNRESOLVED-CONTINUED
(non-fatal; trace proceeds with gap flagged), UNRESOLVED-BLOCKED (fatal; Execute halts). An
UNRESOLVED-BLOCKED row halts Execute before it starts.

**Hypothesis**: When Bind is described as "map inputs to values" in prose, tracers satisfy it
by re-listing inputs with slightly more context, which does not guarantee one-to-one resolution.
The ledger structure makes C-03 structural: a Bind phase without one row per Gather input fails
on table completeness, not on prose interpretation. The three-value Status vocabulary makes the
blocking decision explicit in Bind rather than implicit in Execute -- the tracer cannot silently
proceed past an unresolvable input and produce a partial artifact that looks complete. Risk: the
BLOCKED/CONTINUED/RESOLVED vocabulary adds terms that may conflict with a Coverage Matrix gap
taxonomy if C-09 is added in a later round; the Bind Status labels must be kept distinct from
any SA/SG/EG/QO taxonomy used in coverage.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Gather

Read `{{skill_spec_path}}` and the test invocation. List every input required to run this skill.
For each input: name it, state its source, and record the raw gathered value (or state why it is
absent).

| Input | Source | Raw value | Present? |
|-------|--------|-----------|----------|
| skill_name | invocation | {{skill_name}} | YES |
| skill_spec_path | invocation | {{skill_spec_path}} | YES |
| topic | invocation-parsed | | YES / NO |
| [spec-required input N] | spec / repo-detected | | YES / NO |

A Present=NO row is a gap candidate. Carry all rows -- including absent ones -- to Bind.

---

### Bind (Resolution Ledger)

Every Gather row gets exactly one Bind row. No row may be omitted. No row may carry two resolved
values. The Status column determines whether Execute can proceed.

**Bind Status vocabulary** (three values, no others permitted):

| Status | Meaning | Effect on Execute |
|--------|---------|-------------------|
| RESOLVED | Input has a single confirmed value | None -- Execute proceeds normally |
| UNRESOLVED-CONTINUED | Input absent; Execute proceeds with gap flagged B-NN | Affected artifact sections marked B-NN |
| UNRESOLVED-BLOCKED | Input absent; Execute cannot produce a valid artifact | Execute halts. State what unblocks this. |

**Resolution Ledger**:

| Input | Resolved value | Confidence | Status | Gap ID |
|-------|---------------|------------|--------|--------|
| skill_name | {{skill_name}} | confirmed | RESOLVED | -- |
| skill_spec_path | {{skill_spec_path}} | confirmed | RESOLVED | -- |
| topic | [parsed from invocation] | confirmed / inferred | RESOLVED / UNRESOLVED-CONTINUED | -- / B-01 |
| [spec-required input N] | | | | |

**Bind Gate**: Before Execute, inspect the ledger.

- Any row with UNRESOLVED-BLOCKED: halt here. Name the blocking input, its gap ID, and what
  invocation change or spec revision would unblock the trace. Do not produce an Execute section.
- No UNRESOLVED-BLOCKED rows: proceed to Execute carrying all B-NN IDs.

---

### Execute

Carrying forward: resolved inputs from Bind Ledger, B-NN gap IDs noted.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Run each stock role in spec-defined order. For each role:
- Name the inputs it receives (by name, referencing Bind Ledger rows)
- State what it contributes to the artifact
- Where a B-NN gap affects a section, mark that section B-NN rather than omitting it

Produce the complete artifact. Every section the spec requires must appear -- with real content
or with an explicit B-NN marker. No section may be elided.

---

### Verdict

| Criterion | PASS / FAIL | Evidence |
|-----------|-------------|----------|
| C-01 | | Phase headers present in sequence |
| C-02 | | Gather table: input names and source column populated |
| C-03 | | Bind ledger row count = Gather row count; one resolved value per row |
| C-04 | | Artifact section count vs spec-required; naming convention applied |
| C-05 | | This table, Overall result |
| C-08 | | Artifact scanned for elision markers; B-NN gap markers are not elision |

**Overall result**: PASS / FAIL
**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined: Coverage Matrix + BLOCKED gate (C-09, C-12)

**Axes**:
- Output format: Coverage Matrix with closed-world preamble declared before Gather begins
- Lifecycle emphasis: BLOCKED gate in Coverage Matrix -- any Required=YES / Gap=YES row halts
  the trace before Gather populates a single row

**Hypothesis**: Without a Coverage Matrix, the v2 trace has no pre-Gather declaration of what
inputs will be checked -- Gather is the first act and its completeness is unknowable until it
finishes. The Coverage Matrix inverts this: the tracer declares the full input space first, then
Gather confirms each entry. C-09 is satisfied by the matrix. C-12 is satisfied by the BLOCKED
declaration, which means a Gap=YES in the Coverage Matrix halts execution before the first
Gather row is populated -- the trace cannot silently become a partial run that looks complete.
This axis combination targets the most common v2 failure mode: a Gather that omits inputs it
cannot resolve, leaving the Execute artifact appearing complete when it is not. Risk: the
BLOCKED gate is conservative and may trigger on optional inputs; the matrix must distinguish
required vs optional to avoid spurious halts.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Coverage Matrix

Declare the complete input space for this trace before Gather runs. This is the closed-world
authority: every input this skill spec requires must appear in this table. Gather confirms each
entry against the invocation and repo context.

**Closed-world preamble**: The Coverage Matrix declares what CAN be gathered for this skill
invocation. An input absent from this matrix that Gather encounters is a Coverage Matrix defect
CMD-NN -- the matrix is incomplete. An input in this matrix that Gather cannot confirm is a gap.
Both directions are structural violations.

| Input | Required? | Expected source | Gap? | Notes |
|-------|-----------|----------------|------|-------|
| skill_name | YES | invocation | NO | |
| skill_spec_path | YES | invocation | NO | |
| topic | YES | invocation-parsed | | |
| date | YES | runtime | NO | |
| stock_roles | YES | spec | | |
| output_sections | YES | spec | | |
| [optional spec input N] | NO | repo-detected | | |

**Coverage Matrix BLOCKED gate**: Before Gather, scan this table.

- If any Required=YES row has Gap=YES: **BLOCKED**. The trace cannot produce a valid artifact
  without the missing required input. Name each blocking input. State what invocation change or
  spec revision would unblock the trace. Do not produce Gather, Bind, Execute, or Verdict
  sections below this point.
- If all Required=YES rows have Gap=NO: proceed to Gather.

---

### Gather

Carrying forward: Coverage Matrix confirmed, no Required=YES/Gap=YES rows.

Enumerate every input from the Coverage Matrix, confirming each with its actual source and value.
If Gather discovers an input not in the Coverage Matrix, add it as a Coverage Matrix defect CMD-NN
and carry it forward -- this is a matrix completeness failure, not a trace failure.

| Input | Source | Value | Confirmed? |
|-------|--------|-------|-----------|
| skill_name | invocation | {{skill_name}} | YES |
| skill_spec_path | invocation | {{skill_spec_path}} | YES |
| topic | invocation-parsed | | YES / NO (G-NN) |
| date | runtime | {{date}} | YES |
| [additional inputs] | | | |

A Confirmed=NO input that was Required=YES in the Coverage Matrix is a contradiction: the
BLOCKED gate should have caught it. Surface as G-NN and state the inconsistency.

---

### Bind

Map every Gather input to a single resolved value. For each G-NN gap: state whether it blocks
Execute or whether Execute proceeds with the gap flagged. For each CMD-NN matrix defect: record
but do not block unless it affects a required input.

| Input | Resolved value | Status |
|-------|---------------|--------|
| | | RESOLVED / UNRESOLVED (G-NN) |

---

### Execute

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Run each stock role in spec-defined order. Every spec-required section must appear -- with
content or with an explicit gap marker. No elision markers.

---

### Verdict

| Criterion | PASS / FAIL | Evidence |
|-----------|-------------|----------|
| C-01 | | Phase headers in sequence |
| C-02 | | Gather confirms each Coverage Matrix entry by name with source |
| C-03 | | Bind row count = Gather row count; one resolved value per row |
| C-04 | | Artifact section count vs spec-required; naming convention applied |
| C-05 | | This table, Overall result |
| C-09 | | Coverage Matrix section present before Gather; closed-world preamble present |
| C-12 | | BLOCKED gate declaration present in Coverage Matrix section |

**Overall result**: PASS / FAIL
**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined: All aspirationals (C-09 through C-13)

**Axes**:
- Coverage Matrix with closed-world preamble and BLOCKED gate (C-09, C-12)
- Gather enumerates spec inputs before invocation inputs in two tiers (C-11)
- Execute relay carry with (role, signal, binding, status) fields; Verdict reads relay table (C-10)
- Artifact wrapped with delimiter markers in Execute (C-13)

**Hypothesis**: Each aspirational criterion targets a different failure mode in the trace:
- C-09/C-12 prevent partial traces from appearing complete by halting before Gather begins
- C-11 prevents invocation-anchored Gather from missing spec-required inputs
- C-10 prevents the Verdict from reconstructing judgment the Execute relay already established --
  the relay table is the evidence and Verdict reads it, not the artifact body
- C-13 makes the artifact unambiguously extractable from the trace output

No single-axis variation satisfies all five aspirationals because they operate at different layers
(pre-Gather, Gather structure, Execute relay format, Verdict sourcing, artifact delimiting). V-05
integrates all five layers in sequence. Risk: the relay carry table adds one row per role to
Execute; skills with many roles produce large relay tables. Mitigation: relay uses a compact
4-column format (role, signal, binding, status) with one row per role only.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Coverage Matrix

Declare the complete input space before Gather runs. This is the closed-world authority.

**Closed-world preamble**: This matrix declares what CAN be gathered for this skill invocation.
Gather confirms each declared input. An input absent from this matrix that Gather encounters is
a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.
Both directions constitute closed-world violations.

| Input | Required? | Expected source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec | |
| output_section_list | YES | spec | |
| [optional input N] | NO | repo-detected / spec-default | |

**BLOCKED gate**: Before Gather, scan this table.

- Any Required=YES row with Gap=YES: **BLOCKED**. Name blocking inputs. State what change
  unblocks this trace. Do not produce any subsequent section.
- All Required=YES rows Gap=NO: proceed to Gather.

---

### Gather

**Spec-first rule (C-11)**: Read `{{skill_spec_path}}` completely before consulting the
invocation. Enumerate spec-defined inputs in Tier 1. Then read the invocation for Tier 2.
The spec defines the input space; the invocation constrains it.

#### Gather Tier 1 -- Spec-defined inputs

| Input | Required? | Source type | Spec default |
|-------|-----------|-------------|-------------|
| skill_name | YES | invoker-supplied | none |
| skill_spec_path | YES | invoker-supplied | none |
| topic | YES | invoker-supplied | none |
| stock_roles | YES | spec-defined | [from spec] |
| output_section_list | YES | spec-defined | [from spec] |
| [optional input N] | NO | repo-detected | [spec default] |

Do not consult the invocation during Tier 1. Record what the spec declares.

#### Gather Tier 2 -- Invocation-supplied values

Read the invocation: `{{invocation}}`

Map invocation tokens to Tier 1 slots. Flag any Required Tier 1 input the invocation does not
supply as G-NN.

| Tier 1 input | Invocation value | Present? |
|--------------|-----------------|----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| stock_roles | -- | NO (spec-defined; not invoker-supplied) |
| output_section_list | -- | NO (spec-defined; not invoker-supplied) |

---

### Bind

Merge Tier 1 and Tier 2. One resolved value per input. Invocation wins over spec default on
conflict.

| Input | Resolution source | Resolved value | Status |
|-------|------------------|----------------|--------|
| skill_name | Tier 2 invocation | {{skill_name}} | RESOLVED |
| skill_spec_path | Tier 2 invocation | {{skill_spec_path}} | RESOLVED |
| topic | Tier 2 invocation | [resolved topic] | RESOLVED / UNRESOLVED (G-NN) |
| stock_roles | Tier 1 spec | [role list] | RESOLVED |
| output_section_list | Tier 1 spec | [section list] | RESOLVED |

Any UNRESOLVED Required input blocks Execute. State decision.

---

### Execute

Carrying forward: resolved inputs from Bind.

**Relay carry (C-10)**: For each stock role, produce one row in the relay table before producing
artifact content. The relay table is the evidence chain; Verdict reads it.

| Role | Signal | Binding (Bind input used) | Status |
|------|--------|--------------------------|--------|
| [Role 1] | [contribution to artifact] | [Bind row name] | COMPLETE / PARTIAL (EG-NN) |
| [Role 2] | | | |

After the relay table, produce the artifact enclosed in delimiter markers:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Every spec-required section, fully populated. No elision markers. No placeholder values.
Every section the spec requires must appear. If an UNRESOLVED Bind gap prevents a section,
mark it EG-NN explicitly -- do not omit it.]

[ARTIFACT ENDS HERE]

---

### Verdict

Read the Execute relay table. Do not reconstruct evidence from the artifact body. The relay
table is the evidence source for all criterion checks.

| Criterion | PASS / FAIL | Evidence (relay row or Coverage Matrix entry) |
|-----------|-------------|----------------------------------------------|
| C-01 | | Phase headers: Gather, Bind, Execute, Verdict present in document |
| C-02 | | Tier 1 + Tier 2 row count matches spec input count; source column populated |
| C-03 | | Bind ledger row count = Gather row count; one resolved value per row |
| C-04 | | Relay table: all roles COMPLETE or EG-NN flagged; delimiter markers present |
| C-05 | | This table, Overall result row |
| C-09 | | Coverage Matrix section with closed-world preamble present before Gather |
| C-10 | | Relay table present in Execute; Verdict reads relay row status, not artifact |
| C-11 | | Tier 1 precedes Tier 2 in Gather section |
| C-12 | | BLOCKED gate declared in Coverage Matrix; Gap=YES would halt before Gather |
| C-13 | | [ARTIFACT BEGINS HERE] / [ARTIFACT ENDS HERE] delimiters present in Execute |

**Overall result**: PASS (all C-01 through C-05 PASS) / FAIL (name failing essential criterion)
**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
