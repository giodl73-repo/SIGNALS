---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 4
rubric: trace-skill-rubric-v3-2026-03-15.md
---

# trace-skill -- Variations R4 / rubric-v3 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R3 V-05 achieves all C-01 through C-17 PASS under v3 scoring. Round 4 explores
alternative structural approaches that surface potential v4 patterns while maintaining full compliance.

**R3 V-05 residual structural gaps** (present in the execution, not yet formalized as criteria):

- **Relay-to-Bind provenance**: Execute relay "Binding" column cites an input name (e.g., "topic"),
  but not the resolved value that was bound. The relay assertion is not structurally verifiable
  without backtracking to the Bind table. No current criterion requires the relay to carry the
  actual resolved value.
- **Per-row conflict annotation**: C-17 requires the conflict precedence rule to be declared as
  a block. It does not require each Conflict=YES row in the resolution table to record which
  branch of the declared rule resolved it. The rule is traceable at declaration but not at
  individual resolution decisions.
- **Coverage Matrix self-closure assertion**: After the BLOCKED gate passes, Gather begins with
  no explicit acknowledgment that the gate was cleared. The Verdict cites C-12 pass but the
  structural evidence is a conditional branch -- not a named assertion available as a citation target.

**R4 variation axes** (three single-axis, two combined):

Single-axis:
- V-01: Output format -- relay table carries Resolved Value citations alongside input names
- V-02: Phrasing register -- criterion-aligned self-check questions open each phase
- V-03: Lifecycle emphasis -- Bind table gains "Precedence applied" column (per-row C-17 trace)

Combined:
- V-04: Output format + lifecycle emphasis (relay provenance + per-row conflict + CM closure assertion)
- V-05: Full golden -- all R3 V-05 patterns + all three R4 patterns

Single-axis selections: Output format (V-01), Phrasing register (V-02), Lifecycle emphasis (V-03).
Combined selections: Output format + lifecycle emphasis (V-04), All R3 + all R4 (V-05).

---

## V-01 -- Single axis: Output format (Relay-to-Bind provenance via Resolved Value citation)

**Axis**: Output format -- the Execute relay table's Binding column is redefined to carry
`InputName = ResolvedValue` rather than just the input name. A relay row for a role that used
`topic` (resolved to "auth-refresh") writes `topic = "auth-refresh"` in the Binding cell. A role
that used multiple inputs writes each as a semicolon-separated pair. The Resolved Value must
match the Bind table entry verbatim -- the tracer cannot paraphrase or abbreviate it.

**Hypothesis**: Requiring the relay to carry the Resolved Value from Bind rather than just the
input name creates a verifiable chain: Bind row "topic" has Resolved Value "auth-refresh" →
Execute relay row "AuthResolver" has Binding "topic = auth-refresh" → Verdict reads relay row
and can confirm binding matches Bind without backtracking through the artifact body. This is
a stronger form of C-10 (relay carries evidence, Verdict reads relay) because it makes the
relay self-verifying. Currently, a relay row that says "topic" passes C-10 but leaves open
whether the role actually used the bound value or silently used something else. Risk: relay
rows for roles that use many bindings become verbose; the tracer may abbreviate when multiple
inputs are involved, defeating the provenance requirement. Mitigation: require each unique
input used to appear, but permit omitting inputs the role did not actually draw from in
producing its artifact section.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- declared before trace begins)

Phase headers in this document are transcribed from this table only. Do not generate phase
header names from memory or context.

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

---

### Coverage Matrix (closed-world authority -- before Gather)

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each. An input not in this matrix that Gather encounters is a Coverage Matrix
defect CMD-NN.

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |

**Coverage Matrix BLOCKED gate**: Before Gather, scan this table. Any Required=YES row with
Gap=YES: BLOCKED. State which input is missing and what invocation or spec change unblocks it.
Do not produce Gather, Bind, Execute, or Verdict. All Required=YES rows Gap=NO: proceed.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.

#### Gather Tier 1 -- Spec-declared inputs

| Input Name | Required? | Spec Source Type | Spec Default |
|------------|-----------|-----------------|-------------|
| skill_name | YES | invoker-supplied | (none) |
| skill_spec_path | YES | invoker-supplied | (none) |
| topic | YES | invoker-supplied | (none) |
| date | YES | runtime | today |
| stock_roles | YES | spec-defined | [from spec] |
| output_section_list | YES | spec-defined | [from spec] |

#### Gather Tier 2 -- Invocation-supplied values

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| stock_roles | -- | NO (spec-defined) |
| output_section_list | -- | NO (spec-defined) |

---

## Bind

**Status Enum (declared before resolution table):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; affected sections marked B-NN |
| BLOCKED | Type or format contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both are present and they disagree.
> Exception: invocation value violating the spec's type or format contract → BLOCKED.
> Each row with a conflict cites "invocation override applied" or "spec default retained" in
> Resolved Value.

**Resolution table:**

| Input | Spec Default | Invocation Value | Conflict? | Resolved Value | Status |
|-------|-------------|------------------|-----------|----------------|--------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED |

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum entry. State unblock condition.

---

## Execute

Carrying forward: resolved inputs from Bind.

**Relay table (Resolved Value provenance required)**:

For each stock role, produce one relay row. The Binding column must carry
`InputName = "ResolvedValue"` pairs -- not just input names. List only inputs the role
actually used to produce its artifact section. Multiple inputs: semicolon-separated.

A relay row that names an input without the resolved value fails the provenance requirement.

| Role | Signal | Binding (InputName = "ResolvedValue") | Status |
|------|--------|---------------------------------------|--------|
| [Role 1] | [contribution to artifact] | [e.g., topic = "auth-refresh"; scope_in = "..."] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | | |

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions.
Sections blocked by B-NN gaps are marked B-NN explicitly.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table. Evidence column must name a specific structural element.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Phase headers Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows mapped |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value non-blank |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Filename; sections [list]; relay COMPLETE for all roles |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble |
| C-07 | Verdict cites criterion IDs | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned: [found / not found] |
| C-09 | Coverage Matrix with closed-world preamble | PASS / FAIL | Coverage Matrix block present before Gather; closed-world preamble text present |
| C-10 | Execute relay carries binding evidence; Verdict reads relay | PASS / FAIL | Relay table in Execute: [N] rows; Binding column carries InputName=ResolvedValue pairs; this row reads relay, not artifact |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 section precedes Tier 2; spec consulted before invocation |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present; Gap=YES halts trace before Gather |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema table declared pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict is compliance ledger (ID/Result/Evidence) | PASS / FAIL | This table; columns ID, Criterion, Result, Evidence; Evidence cites structural loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Status Enum definition table above Bind resolution table; RESOLVED/UNRESOLVED/BLOCKED all defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block above Bind row 1; invocation-override rule + BLOCKED exception stated |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Phrasing register (criterion-aligned self-check questions at each phase opening)

**Axis**: Phrasing register -- each phase opens with a set of mandatory self-check questions
the tracer must answer before producing any phase content. The questions are phrased in the
second person imperative and map directly to specific criteria. Answering them is part of the
trace output, not a private mental step. A question answered NO is a compliance signal the
tracer must address before proceeding.

**Hypothesis**: Criterion-aligned questions at phase openings convert compliance checking from
a terminal Verdict activity into a continuous in-phase activity. A tracer who encounters
"Have you read the spec completely before consulting the invocation? [YES/NO]" at the start
of Gather must answer and is unlikely to answer YES falsely if the question is framed as a
concrete behavioral check. This variation tests whether embedded compliance questions are as
effective as structural tables at enforcing criteria -- and whether they surface compliance
failures earlier in the lifecycle. Risk: questions may be answered YES by rote, especially
if the tracer is operating under time pressure. Self-check questions without a structural
enforcement mechanism (like a gate) rely on honest self-assessment. Mitigation: each question
specifies what constitutes a YES answer, making rote YES responses demonstrably wrong if the
check was not actually performed.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- pre-trace preamble)

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

---

## Gather

**Phase-opening self-check** (answer before producing Gather content):

1. Have I read `{{skill_spec_path}}` completely before consulting `{{invocation}}`?
   [YES -- I read the spec first] / [NO -- I must read the spec before continuing]
2. Does my input enumeration begin with inputs the spec declares, before mapping invocation values?
   [YES -- Tier 1 spec inputs appear before Tier 2 invocation values in my table]
   [NO -- I must restructure so spec inputs precede invocation values]
3. Have I included a Coverage Matrix with a closed-world preamble and explicit BLOCKED gate
   for any Required=YES gap?
   [YES -- Coverage Matrix block present with gate text] / [NO -- I must add it before Gather rows]

If any answer is NO, address it before writing the Gather content below.

---

**Coverage Matrix** (closed-world authority):

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | |
| skill_spec_path | YES | invocation | |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |

**Coverage Matrix BLOCKED gate**: Any Required=YES with Gap=YES: BLOCKED. Do not continue.

---

**Gather Tier 1 -- Spec-declared inputs** (before consulting invocation):

| Input Name | Required? | Spec Source Type | Spec Default |
|------------|-----------|-----------------|-------------|
| skill_name | YES | invoker-supplied | (none) |
| skill_spec_path | YES | invoker-supplied | (none) |
| topic | YES | invoker-supplied | (none) |
| date | YES | runtime | today |
| stock_roles | YES | spec-defined | [from spec] |
| output_section_list | YES | spec-defined | [from spec] |

**Gather Tier 2 -- Invocation-supplied values** (after spec enumeration):

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| stock_roles | -- | NO (spec-defined) |
| output_section_list | -- | NO (spec-defined) |

---

## Bind

**Phase-opening self-check** (answer before producing Bind content):

1. Have I declared a three-value Status Enum (RESOLVED / UNRESOLVED / BLOCKED) as a named
   definition block before the first resolution row?
   [YES -- Status Enum definition table present above resolution table] / [NO -- I must add it]
2. Have I declared a named Conflict Precedence Rule block specifying what happens when spec
   default and invocation value disagree, and what triggers BLOCKED?
   [YES -- Conflict Precedence Rule block present above first row] / [NO -- I must add it]
3. Does every row in my resolution table carry exactly one Resolved Value and a Status from
   the declared enum?
   [YES -- each row: one Resolved Value, one Status from {RESOLVED, UNRESOLVED, BLOCKED}]
   [NO -- I must revise rows with missing or non-enum Status values]

If any answer is NO, address it before writing Bind content.

---

**Status Enum:**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; affected sections marked B-NN |
| BLOCKED | Type or format contract violation | Halt; state unblock condition |

**Conflict Precedence Rule:**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating spec's type or format contract → BLOCKED.

**Resolution table:**

| Input | Spec Default | Invocation Value | Conflict? | Resolved Value | Status |
|-------|-------------|------------------|-----------|----------------|--------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED |

---

## Execute

**Phase-opening self-check**:

1. Have I included a relay table before the artifact, with one row per stock role carrying
   role name, signal contribution, binding, and status?
   [YES -- relay table present before [ARTIFACT BEGINS HERE]] / [NO -- I must add it]
2. Are the artifact delimiters "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" present
   exactly as written?
   [YES -- both strings present] / [NO -- I must add them]
3. Does the artifact contain every section the spec defines, with no elision markers?
   [YES -- every section present; no "..." or "[content here]"] / [NO -- I must complete it]

---

Carrying forward: resolved inputs from Bind.

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution] | [Bind input used] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | | |

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no elision markers]

[ARTIFACT ENDS HERE]

---

## Verdict

**Phase-opening self-check**:

1. Is this Verdict structured as a compliance ledger table with columns ID, Criterion,
   Result, and Evidence?
   [YES -- table present with all four columns] / [NO -- I must restructure as a table]
2. Does the Evidence column name a specific structural element (table header, row count,
   delimiter string, relay row status) -- not free-form prose like "looks correct"?
   [YES -- every Evidence cell names a structural element] / [No -- I must revise vague cells]
3. Do all five essential criteria (C-01 through C-05) have PASS in the Result column?
   [YES -- C-01 through C-05 all PASS] / [NO -- I must identify the failing essential and fix it]

---

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Phase headers: Gather §[loc], Bind §[loc], Execute §[loc], Verdict §[loc] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows mapped |
| C-03 | Bind maps all inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank; Status from enum |
| C-04 | Artifact with correct naming + sections | PASS / FAIL | Filename; required sections; relay COMPLETE |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This table, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema table |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [result] |
| C-09 | Coverage Matrix with closed-world preamble | PASS / FAIL | Coverage Matrix block in Gather; preamble text "closed-world authority" present |
| C-10 | Relay carries evidence; Verdict reads relay | PASS / FAIL | Relay table rows: [N]; status column populated; this row reads relay status, not artifact body |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 precedes Tier 2; spec-first self-check answer YES |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate text present; gate condition "Required=YES + Gap=YES → BLOCKED" declared |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" present in Execute |
| C-14 | Phase Label Schema table pre-trace | PASS / FAIL | Phase Label Schema block at document top, before Coverage Matrix |
| C-15 | Verdict is compliance ledger | PASS / FAIL | This table: ID, Criterion, Result, Evidence columns; Evidence cites structural elements |
| C-16 | Bind Status Enum declared | PASS / FAIL | Status Enum table above Bind resolution table; all three values declared |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block above first Bind row; invocation-override + exception stated |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL -- [failing essential + evidence]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (Bind "Precedence applied" column for per-row C-17 trace)

**Axis**: Lifecycle emphasis -- the Bind resolution table gains a "Precedence applied" column
with exactly three values: `override` (invocation value overrides spec default, applying the
conflict rule's invocation-wins branch), `default` (spec default applies because no invocation
value was supplied for this input), or `BLOCKED` (the conflict rule's exception branch: the
invocation value violated a type or format contract). This column is populated for every row.
Rows with Conflict=YES must carry `override` or `BLOCKED`. Rows with Conflict=NO carry `default`
when no invocation value was present, or `override` when the invocation value was used even
without conflict.

**Hypothesis**: The conflict precedence rule declared in C-17 governs every row in the resolution
table, but currently only Conflict=YES rows require any visible application of the rule. A
"Precedence applied" column makes the rule traceable at the row level: the Verdict's C-17
evidence row can point to the column ("all Conflict=YES rows carry 'override' or 'BLOCKED'")
rather than just confirming the rule was declared as a block. This strengthens C-17 from
declaration verification to execution verification. Risk: columns with only three values become
mechanical box-checking; tracers may populate the column without reasoning about whether the
rule was correctly applied (e.g., writing `override` for a row that should be `BLOCKED`).
Mitigation: requiring `BLOCKED` for contract violations and requiring those rows to also carry
the Bind gate halt text makes silent BLOCKED-to-override substitutions visible.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- pre-trace preamble)

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

---

### Coverage Matrix (closed-world authority -- before Gather)

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |

**Coverage Matrix BLOCKED gate**: Any Required=YES with Gap=YES: BLOCKED. Do not continue.
All Required=YES rows Gap=NO: proceed to Gather.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.

#### Gather Tier 1 -- Spec-declared inputs

| Input Name | Required? | Spec Source Type | Spec Default |
|------------|-----------|-----------------|-------------|
| skill_name | YES | invoker-supplied | (none) |
| skill_spec_path | YES | invoker-supplied | (none) |
| topic | YES | invoker-supplied | (none) |
| date | YES | runtime | today |
| stock_roles | YES | spec-defined | [from spec] |
| output_section_list | YES | spec-defined | [from spec] |

#### Gather Tier 2 -- Invocation-supplied values

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| stock_roles | -- | NO (spec-defined) |
| output_section_list | -- | NO (spec-defined) |

---

## Bind

**Status Enum (declared before resolution table):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; affected sections B-NN |
| BLOCKED | Contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating spec's type or format contract → BLOCKED.

**Precedence Applied vocabulary** (per-row column -- three values only):

| Value | When to use |
|-------|------------|
| `override` | Invocation value was used; spec default overridden by the conflict rule's invocation-wins branch |
| `default` | Spec default was used; no invocation value present for this input |
| `BLOCKED` | Conflict rule's exception: invocation value violates spec's type or format contract |

**Resolution table** -- one row per merged input; every cell required:

| Input | Spec Default | Invocation Value | Conflict? | Resolved Value | Status | Precedence applied |
|-------|-------------|------------------|-----------|----------------|--------|--------------------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED | override |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED | override |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED | override |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED | override |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| [input with conflict] | [spec default] | [invocation value] | YES | [per rule] | RESOLVED / BLOCKED | override / BLOCKED |

**Rule**: "Precedence applied" must be one of the three declared values only. A Conflict=YES
row must carry `override` or `BLOCKED`. A row where Status=BLOCKED must carry `BLOCKED` in
the Precedence applied column.

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED entry. State what
invocation change resolves the contract violation.

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

| Role | Signal | Binding (Bind input used) | Status |
|------|--------|---------------------------|--------|
| [Role 1] | [contribution] | [input name(s)] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | | |

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no elision markers, no omissions]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Evidence column must name a specific structural element.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Phase headers Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows mapped |
| C-03 | Bind maps all inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged count; Resolved Value non-blank; Status from enum |
| C-04 | Artifact with naming + sections | PASS / FAIL | Filename; required sections; relay status all COMPLETE |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [result] |
| C-09 | Coverage Matrix with closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Relay evidence; Verdict reads relay | PASS / FAIL | Relay table in Execute: [N] rows, status populated; this row cites relay status |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate text present; halt condition declared |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID, Criterion, Result, Evidence columns; Evidence cites structural loci |
| C-16 | Bind Status Enum declared | PASS / FAIL | Status Enum table present above resolution table; RESOLVED/UNRESOLVED/BLOCKED defined |
| C-17 | Bind conflict precedence rule declared + per-row applied | PASS / FAIL | Conflict Precedence Rule block present above row 1; "Precedence applied" column present; all Conflict=YES rows carry override or BLOCKED |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL -- [failing essential + evidence]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Output format + lifecycle emphasis (relay provenance + per-row conflict + CM closure assertion)

**Axes**:
- Output format: Execute relay table carries `InputName = "ResolvedValue"` binding citations
  (V-01 axis) -- relay-to-Bind provenance is structurally verifiable.
- Lifecycle emphasis: Bind resolution table carries "Precedence applied" column (V-03 axis) --
  C-17 rule is traceable per row, not just at declaration.
- Lifecycle emphasis (new): after the Coverage Matrix BLOCKED gate passes, an explicit
  "Coverage Matrix: CLOSED" assertion is written as a named structural element before Gather
  begins. This assertion names each Required=YES input confirmed Gap=NO. The Verdict's C-09
  and C-12 evidence rows cite this assertion rather than just pointing at the gate text.

**Hypothesis**: All three patterns target the same structural gap: declarations that exist
("conflict rule declared," "Coverage Matrix BLOCKED gate present," "relay carries binding")
but whose execution cannot be verified without re-reading the content. Per-row conflict
annotation makes C-17 execution traceable. Relay-to-Bind provenance makes C-10 relay reading
traceable. Coverage Matrix closure makes C-09/C-12 gate pass traceable. Combining them creates
a trace where every declared structure has a named execution trace a subsequent reader can
verify without re-running the skill. Risk: the combination adds structural density to Bind and
Execute; a tracer producing a dense trace may fill columns mechanically. Mitigation: the V-05
full golden test will determine whether column density or criterion coverage suffers.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- pre-trace preamble)

Declared before all content. Phase headers transcribed from this table only.

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

---

### Coverage Matrix (closed-world authority -- before Gather)

**Closed-world preamble**: This matrix declares every input this invocation CAN supply. Gather
confirms each. An input absent from this matrix that Gather encounters is a defect CMD-NN.

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |

**Coverage Matrix BLOCKED gate**: Any Required=YES with Gap=YES: BLOCKED. State what
invocation or spec change unblocks it. Do not produce Gather, Bind, Execute, or Verdict.

**Coverage Matrix closure assertion** (write this ONLY after the gate confirms all
Required=YES rows are Gap=NO):

> Coverage Matrix: CLOSED. All Required=YES inputs confirmed Gap=NO:
> skill_name (invocation), skill_spec_path (invocation), topic (invocation-parsed),
> date (runtime), stock_roles (spec-defined), output_section_list (spec-defined).
> Trace may proceed to Gather.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.

#### Gather Tier 1 -- Spec-declared inputs

| Input Name | Required? | Spec Source Type | Spec Default |
|------------|-----------|-----------------|-------------|
| skill_name | YES | invoker-supplied | (none) |
| skill_spec_path | YES | invoker-supplied | (none) |
| topic | YES | invoker-supplied | (none) |
| date | YES | runtime | today |
| stock_roles | YES | spec-defined | [from spec] |
| output_section_list | YES | spec-defined | [from spec] |

#### Gather Tier 2 -- Invocation-supplied values

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| stock_roles | -- | NO (spec-defined) |
| output_section_list | -- | NO (spec-defined) |

---

## Bind

**Status Enum (declared before resolution table):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; affected sections B-NN |
| BLOCKED | Contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating spec's type or format contract → BLOCKED.

**Precedence Applied vocabulary:**

| Value | When to use |
|-------|------------|
| `override` | Invocation value applied; spec default overridden |
| `default` | Spec default applied; no invocation value present |
| `BLOCKED` | Invocation value violates type/format contract |

**Resolution table:**

| Input | Spec Default | Invocation Value | Conflict? | Resolved Value | Status | Precedence applied |
|-------|-------------|------------------|-----------|----------------|--------|--------------------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED | override |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED | override |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED | override |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED | override |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED | default |

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED definition.

---

## Execute

Carrying forward: resolved inputs from Bind.

**Relay table (Resolved Value provenance -- required):**

Binding column format: `InputName = "ResolvedValue"` (semicolon-separated for multiple inputs).
Cite only inputs this role actually used to produce its artifact section. The value must match
the Bind Resolved Value cell verbatim.

| Role | Signal | Binding (InputName = "ResolvedValue") | Status |
|------|--------|---------------------------------------|--------|
| [Role 1] | [contribution to artifact] | [e.g., topic = "auth-refresh"; stock_roles = "[list]"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | | |

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions.
Sections blocked by B-NN gaps marked B-NN explicitly.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Evidence column must name a specific structural element.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Phase headers Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows mapped |
| C-03 | Bind maps all inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank; Status from enum |
| C-04 | Artifact with naming + sections | PASS / FAIL | Filename; sections [list]; relay COMPLETE for all roles |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [result] |
| C-09 | Coverage Matrix with closed-world preamble | PASS / FAIL | Coverage Matrix CLOSED assertion present; preamble text present; all Required=YES inputs named |
| C-10 | Relay carries evidence; Verdict reads relay | PASS / FAIL | Relay table: [N] rows; Binding column carries InputName=ResolvedValue pairs; this row cites relay, not artifact body |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate text present; Coverage Matrix CLOSED assertion confirms gate was cleared |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict is compliance ledger | PASS / FAIL | This table; ID, Criterion, Result, Evidence columns; Evidence cites structural loci |
| C-16 | Bind Status Enum declared | PASS / FAIL | Status Enum table above Bind resolution table; all three values defined |
| C-17 | Bind conflict precedence + per-row applied | PASS / FAIL | Conflict Precedence Rule block present; Precedence applied column present; Conflict=YES rows carry override or BLOCKED |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL -- [failing essential + evidence]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined golden: R3 V-05 architecture + all R4 patterns

**Axes** (full integration -- all R3 V-05 patterns + all three R4 patterns):

- Phase Label Schema preamble (C-14): immutable declaration before all content.
- Coverage Matrix + BLOCKED gate (C-09, C-12): closed-world authority before Gather.
- **Coverage Matrix self-closure assertion (R4)**: after gate passes, an explicit CLOSED
  assertion names every Required=YES input confirmed, cited by Verdict for C-09 and C-12.
- Spec-first Gather in two tiers (C-11): spec consulted before invocation.
- Bind Status Enum declared (C-16): RESOLVED/UNRESOLVED/BLOCKED as formal definition.
- Bind Conflict Precedence Rule declared (C-17): named block before resolution rows.
- **Bind Precedence applied column (R4)**: per-row conflict annotation; every row carries
  `override`, `default`, or `BLOCKED` from the declared vocabulary.
- Execute relay table (C-10): (role / signal / binding / status); Verdict reads relay.
- **Relay-to-Bind provenance (R4)**: relay Binding column carries `InputName = "ResolvedValue"`;
  binding is structurally verifiable against Bind table.
- Artifact delimiter markers (C-13): [ARTIFACT BEGINS HERE] / [ARTIFACT ENDS HERE].
- Verdict compliance ledger (C-15): ID | Criterion | Result | Evidence; structural citations.

**Hypothesis**: All three R4 patterns are in the same structural category: they add traceable
execution evidence to declarations that R3 V-05 made but left unverifiable at the row level.
The closure assertion makes the BLOCKED gate exit traceable (not just the gate entry). The
Precedence applied column makes the conflict rule traceable at each resolution decision (not
just at declaration). The relay provenance makes the relay-to-Bind chain traceable at each
binding (not just at role level). These are structural completions of R3 patterns, not
independent innovations. Together they close the gap between "declared" and "demonstrably
applied." Risk: V-05 is the densest variation; Bind resolution table now has 7 columns; Execute
relay has a verbose Binding cell. A tracer with limited attention may satisfy column existence
without column depth. Mitigation: the Verdict compliance ledger has specific evidence requirements
for each new column, making empty or shallow column entries fail C-15 on their own evidence tests.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- pre-trace preamble)

Declared before all content. Phase headers in this document are transcribed from this table
only. Do not generate phase header names from memory or context.

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

The Verdict compliance ledger checks C-14 (this schema present before phase 1) and C-06
(all phase headers match this schema) as distinct row entries.

---

### Coverage Matrix (closed-world authority -- before Gather)

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input. An input absent from this matrix that Gather encounters
is a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |

**Coverage Matrix BLOCKED gate**: Before Gather, scan this table.

- Any Required=YES row with Gap=YES: **BLOCKED**. The trace cannot produce a valid artifact
  without this input. Name each blocking input. State what invocation change or spec revision
  unblocks it. Do not produce Gather, Bind, Execute, or Verdict below this point.
- All Required=YES rows Gap=NO: write the Coverage Matrix closure assertion and proceed.

**Coverage Matrix closure assertion** (written ONLY after gate confirms all Required=YES
rows are Gap=NO -- this assertion is a named structural element the Verdict cites):

> Coverage Matrix: CLOSED. All Required=YES inputs confirmed Gap=NO:
> [list each Required=YES input with its confirmed source].
> Gather may proceed.

---

## Gather

**Spec-first rule (C-11)**: Read `{{skill_spec_path}}` completely before consulting the
invocation. The spec defines the input space; the invocation constrains it.

#### Gather Tier 1 -- Spec-declared inputs (before invocation)

| Input Name | Required? | Spec Source Type | Spec Default |
|------------|-----------|-----------------|-------------|
| skill_name | YES | invoker-supplied | (none) |
| skill_spec_path | YES | invoker-supplied | (none) |
| topic | YES | invoker-supplied | (none) |
| date | YES | runtime | today |
| stock_roles | YES | spec-defined | [from spec] |
| output_section_list | YES | spec-defined | [from spec] |
| [optional input N] | NO | repo-detected | [spec default] |

#### Gather Tier 2 -- Invocation-supplied values (after spec enumeration)

Read `{{invocation}}`. Map to Tier 1 slots. Flag absent Required inputs G-NN.

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| stock_roles | -- | NO (spec-defined) |
| output_section_list | -- | NO (spec-defined) |

---

## Bind

**Status Enum (declared before resolution table):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; affected artifact sections marked B-NN |
| BLOCKED | Type or format contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both are present and they disagree.
> Exception: if the invocation value violates the spec's declared type or format contract
> (wrong type, invalid enum member, missing required subfield), status is BLOCKED.
> Each row with a conflict cites "invocation override applied" or "spec default retained"
> in the Resolved Value cell.

**Precedence Applied vocabulary** (per-row column -- three values only):

| Value | When to use |
|-------|------------|
| `override` | Invocation value was used; spec default overridden by the conflict rule's invocation-wins branch |
| `default` | Spec default applies; no invocation value present for this input |
| `BLOCKED` | Conflict rule exception triggered: invocation value violates type/format contract |

**Resolution table** -- one row per merged input; all seven cells required:

| Input | Spec Default | Invocation Value | Conflict? | Resolved Value | Status | Precedence applied |
|-------|-------------|------------------|-----------|----------------|--------|--------------------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED | override |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED | override |
| topic | (none) | [from invocation] | NO | [resolved value] | RESOLVED | override |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED | override |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| [optional N] | [default] | [invocation or --] | YES / NO | [per rule] | RESOLVED / UNRESOLVED / BLOCKED | override / default / BLOCKED |

**Rules for Precedence applied column**:
- Conflict=YES rows must carry `override` or `BLOCKED`.
- Status=BLOCKED rows must carry `BLOCKED`.
- Status=UNRESOLVED rows where input is absent carry `default`.
- No other values permitted.

**Bind gate**: Any BLOCKED row halts Execute. Name the blocking row, cite the Status Enum BLOCKED
entry, and state what invocation change resolves the violation.

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay table (Resolved Value provenance required)**:

For each stock role, one relay row. The Binding column must carry `InputName = "ResolvedValue"`
pairs (semicolon-separated for multiple inputs). List only inputs the role actually used to
produce its artifact section. The Resolved Value must match the Bind table entry verbatim --
do not paraphrase or abbreviate. The Verdict reads this relay table; it does not reconstruct
evidence from the artifact body.

| Role | Signal | Binding (InputName = "ResolvedValue") | Status |
|------|--------|---------------------------------------|--------|
| [Role 1] | [contribution to artifact] | [e.g., topic = "auth-refresh"; scope_in = "token lifecycle"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | | |

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every section the spec defines must appear with real content or an
explicit B-NN marker. No "...", no "[content here]", no "[see above]", no omitted sections.
Sections blocked by B-NN gaps are marked B-NN explicitly and the trace continues.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table. Do not reconstruct evidence from the artifact body. The relay
table is the primary evidence source for all criteria involving Execute content.

Evidence column must name a specific structural element (table header, row count, delimiter
string, relay row status, section heading, assertion text). Generic entries like "looks
correct" or "seems complete" are structural failures of C-15 independently of C-05.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations]; sequence verified |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value non-blank; Status from enum |
| C-04 | Artifact with naming + sections | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename {topic}-{signal}-{date}.md; required sections: [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble; all four match |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-NN present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned for "...", "[omitted]", "[content here]": [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix CLOSED assertion present; preamble text "closed-world authority" present; [N] Required=YES inputs named in assertion |
| C-10 | Relay carries evidence; Verdict reads relay | PASS / FAIL | Relay table: [N] rows; Binding column carries InputName=ResolvedValue pairs; this row reads relay status directly: [list role statuses] |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 section precedes Tier 2 section; spec read before invocation |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate text present; Coverage Matrix CLOSED assertion confirms gate was cleared before Gather |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" at §[location]; "[ARTIFACT ENDS HERE]" at §[location] in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix; before any phase content |
| C-15 | Verdict is compliance ledger | PASS / FAIL | This table; ID, Criterion, Result, Evidence columns present; Evidence column cites structural loci for all rows |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Status Enum definition table above Bind resolution table; RESOLVED/UNRESOLVED/BLOCKED all defined with Execute effects |
| C-17 | Bind conflict precedence + per-row applied | PASS / FAIL | Conflict Precedence Rule block above first resolution row; Precedence applied column present; [N] Conflict=YES rows carry override or BLOCKED |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
