---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 3
rubric: trace-skill-rubric-v3-2026-03-15.md
---

# trace-skill -- Variations R3 / rubric-v3 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R2 V-05 achieves all C-01 through C-13 PASS under v2 scoring. Rubric v3 adds
four new aspirational criteria from R2 excellence signals:

- **C-14**: Phase Label Schema table (immutable) declared before any trace content -- makes C-06
  a structural guarantee rather than a convention.
- **C-15**: Verdict is a structured compliance ledger table (ID | Result | Evidence) rather than
  prose citation -- categorically stronger than C-07's criterion-ID-must-appear rule.
- **C-16**: Bind rows carry an explicit three-value Status enum: RESOLVED / UNRESOLVED / BLOCKED.
  Distinct from C-12 (pre-Gather gate); the BLOCKED halt lives in Bind, not before Gather.
- **C-17**: Bind declares an explicit conflict precedence rule: when spec value and invocation
  value disagree, the rule resolves which wins. Distinct from C-03 (which only requires resolution
  happens); C-17 requires the governing rule to be declared explicitly.

**R2 V-05 state against v3** (quick projection):

- C-14: R2 V-01 declares "Phase Label Schema" before trace begins. R2 V-05 inherits V-01's schema
  table. C-14 = PASS (inherited from R2 V-01 design).
- C-15: R2 Verdict is a table with criterion-ID column but no distinct "ID | Result | Evidence"
  compliance-ledger structure. C-15 = PARTIAL (table exists; structure is not compliance-ledger).
- C-16: R2 Bind uses RESOLVED / UNRESOLVED status but not a formally declared three-value enum
  with BLOCKED as a first-class state. C-16 = PARTIAL (two-value implicit; BLOCKED lives in prose
  gate, not in Status column).
- C-17: R2 Bind states conflict rule in V-02 and V-05 ("invocation wins over spec default").
  C-17 = PASS (rule declared, though phrased as inline prose rather than a block declaration).

**R3 variation axes** (targeting C-14, C-15, C-16, C-17 as the four new v3 aspirationals):

Single-axis:
- V-01: Lifecycle emphasis -- Phase Label Schema table as formal immutable preamble (C-14)
- V-02: Output format -- Verdict compliance ledger + Bind three-value Status enum (C-15, C-16)
- V-03: Role sequence -- spec-first Gather + explicit Bind conflict precedence declaration (C-11, C-17)

Combined:
- V-04: Phase Schema + Status Enum + Conflict Precedence (C-14 + C-16 + C-17 -- structural backbone)
- V-05: Full golden -- all C-09 through C-17 (R2 V-05 foundation + all four new v3 criteria)

---

## V-01 -- Single axis: Lifecycle emphasis (Phase Label Schema as immutable preamble)

**Axis**: Lifecycle emphasis -- the trace opens with a "Phase Label Schema" table declared as an
immutable preamble. This is not a header or a section; it is a structural declaration that exists
before the first trace phase begins. Every phase header used in the trace is locked here. Any
output that uses a synonym header is a structural violation that the Verdict can check
mechanically against the schema, not interpretively against the instructions.

**Hypothesis**: A Phase Label Schema declared as an immutable pre-trace preamble makes C-06
structurally guaranteed: the schema is on the page before the model writes a single phase header,
so phase header names are transcribed from the schema rather than generated from context. This
satisfies C-14 (the schema table is the preamble) while strengthening C-06 from a convention to
a constraint. The distinction from R2 V-01 (which names the schema in an introductory prose block)
is that C-14 requires the schema to appear as a table in its own named block before any trace
content. Risk: a model that reads instructions top-to-bottom may produce the schema and then
immediately use a synonym header for the first phase before the schema constraint registers.
Mitigation: the instructions explicitly state "phase headers in this trace are transcribed from
this table -- do not generate them from memory."

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE PRE-TRACE DECLARATION)

This table is declared before any trace content. It is not part of any phase. It locks every
phase header used in this document. Phase headers in this trace are **transcribed from this
table** -- do not generate phase header names from memory or context.

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context, Inputs, Read |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare, Init, Load |
| 3 | `## Execute` | Run, Simulate, Produce, Compile, Perform, Generate |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion, Output, Review |

After declaring this schema, run the four-phase trace using the exact headers above.

**Schema enforcement**: In the Verdict compliance table, one row checks C-06 (phase headers
match schema) and one row checks C-14 (this schema table was declared before trace phase 1).
Both checks reference this block by name.

---

## Gather

Read `{{skill_spec_path}}` and `{{invocation}}`. Enumerate every input this skill requires.
For each input: name it, state its source, record the raw value or state why it is absent.

| Input Name | Source | Value / Description | Gap? |
|------------|--------|---------------------|------|
| skill_name | invocation | {{skill_name}} | NO |
| skill_spec_path | invocation | {{skill_spec_path}} | NO |
| topic | invocation-parsed | | |
| date | runtime | {{date}} | NO |
| [spec-required input N] | spec | | |

**Closed-world rule**: Every input the spec declares must appear as a row. Every constraint the
invocation provides must appear as a row. An input absent from this table does not exist for
this trace.

If any Required input has Gap=YES: STOP. State which input is missing, why the trace cannot
proceed, and what invocation or spec change would unblock it.

---

## Bind

Map every Gather input to exactly one resolved value. Every Gather row must appear here.
No row may be omitted. No row may carry two resolved values.

| Input Name | Gathered Value | Resolved Value | Status |
|------------|---------------|----------------|--------|
| skill_name | {{skill_name}} | {{skill_name}} | RESOLVED |
| skill_spec_path | {{skill_spec_path}} | {{skill_spec_path}} | RESOLVED |
| topic | [from invocation] | [resolved] | RESOLVED / UNRESOLVED / BLOCKED |
| date | {{date}} | {{date}} | RESOLVED |
| [spec input N] | | | |

**Status vocabulary** (three values only; no others permitted):
- **RESOLVED** -- single confirmed value from a named source; Execute proceeds normally.
- **UNRESOLVED** -- no confirmed value; trace proceeds with gap flagged B-NN.
- **BLOCKED** -- input conflict or missing required value prevents valid artifact production.

**Bind gate**: If any row is BLOCKED: halt here. Name the blocking row and state what change
would unblock the trace. Do not produce an Execute section.

---

## Execute

Carrying forward: all Bind-resolved values, B-NN gaps noted.

Produce the hand-compiled artifact as if `/{{skill_name}}` had run on the test invocation.
Artifact filename: `{topic}-{signal}-{date}.md`

Run each role the spec defines in spec-defined order. Every spec-required section must appear
in the artifact with real content or an explicit B-NN gap marker. No elision markers.

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions]

[ARTIFACT ENDS HERE]

---

## Verdict

| ID | Criterion (brief) | Result | Evidence |
|----|-------------------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict headers at [locations] |
| C-02 | Gather enumerates inputs by name + source | PASS / FAIL | Gather table: [N] rows, source column populated |
| C-03 | Bind maps every Gather input to one resolved value | PASS / FAIL | Bind table: [N] rows = Gather [N] rows; one Resolved Value per row |
| C-04 | Execute produces artifact with correct naming | PASS / FAIL | Artifact filename, required sections: [list] |
| C-05 | Verdict declares PASS/FAIL with rationale | PASS / FAIL | This table, Overall row |
| C-06 | Exact schema labels used | PASS / FAIL | Phase headers match Phase Label Schema table (Gather/Bind/Execute/Verdict) |
| C-07 | Verdict cites criterion IDs | PASS / FAIL | C-01 through C-NN present in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [result] |
| C-13 | Artifact wrapped in delimiter markers | PASS / FAIL | [ARTIFACT BEGINS HERE] / [ARTIFACT ENDS HERE] present in Execute |
| C-14 | Phase Label Schema table declared before trace | PASS / FAIL | Phase Label Schema block present above Gather; immutable preamble declared |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [name failing essential criterion]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Output format (Verdict compliance ledger + Bind three-value Status enum)

**Axis**: Output format -- two structural changes to phase-internal format. (1) Bind uses an
explicitly declared three-value Status enum (RESOLVED / UNRESOLVED / BLOCKED) with a formal
enum definition block before the resolution table. (2) Verdict is formatted as a compliance
ledger -- a structured table with columns ID | Criterion | Result | Evidence -- where the
Evidence column names a specific structural element in this document (table name, section
header, row count, or delimiter location), not free-form prose.

**Hypothesis**: Declaring the Bind Status enum before the resolution table (C-16) makes BLOCKED
a first-class state, not a prose gate note appended after the table. A model that reads the
enum declaration before writing rows will write three-value status; a model that reads only
prose gate instructions may still write two-value status. The compliance ledger Verdict (C-15)
is categorically stronger than C-07: C-07 is satisfied if criterion IDs appear anywhere in the
Verdict text; C-15 requires a table where Evidence is a structural reference. A model filling
the Evidence column must name something in the document -- it cannot satisfy C-15 with "looks
correct." Risk: the Evidence column requirement is strict; a model that cannot identify a
structural evidence locus may write "N/A" or a vague reference. Mitigation: the ledger
instructions name explicit evidence types for each criterion row.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Gather

Read `{{skill_spec_path}}` and `{{invocation}}`. Enumerate every input the skill needs.
For each: name it, state its source, record the available value.

| Input Name | Source | Value | Present? |
|------------|--------|-------|----------|
| skill_name | invocation | {{skill_name}} | YES |
| skill_spec_path | invocation | {{skill_spec_path}} | YES |
| topic | invocation-parsed | | YES / NO |
| date | runtime | {{date}} | YES |
| [spec-required input N] | spec / invocation | | YES / NO |

Carry all rows -- present or absent -- to Bind. A Present=NO required input is a gap candidate.

---

### Bind

**Status Enum (three values -- declare before resolution table):**

| Status | Meaning | Effect on Execute |
|--------|---------|-------------------|
| RESOLVED | Single confirmed value from a named source | Execute proceeds for this input |
| UNRESOLVED | No confirmed value; trace proceeds with gap B-NN | Affected artifact sections marked B-NN |
| BLOCKED | Input conflict or type violation; valid artifact production impossible | Execute halts; state blocking input and unblock condition |

**Conflict Precedence Rule** (declare before resolution rows):
> When a spec-declared default and an invocation-supplied value occupy the same input slot,
> the invocation wins (runtime override). Exception: if the invocation value violates the
> spec's declared type or format contract, status is BLOCKED -- invocation cannot override
> a contract violation.

**Resolution table** -- one row per Gather input, no omissions:

| Input Name | Spec Default | Invocation Value | Resolved Value | Status |
|------------|-------------|------------------|----------------|--------|
| skill_name | (none) | {{skill_name}} | {{skill_name}} | RESOLVED |
| skill_spec_path | (none) | {{skill_spec_path}} | {{skill_spec_path}} | RESOLVED |
| topic | (none) | [from invocation] | [resolved] | RESOLVED |
| date | runtime | {{date}} | {{date}} | RESOLVED |
| [spec input N] | [spec default] | [invocation or --] | [per conflict rule] | RESOLVED / UNRESOLVED / BLOCKED |

**Bind gate**: Any BLOCKED row: halt. Name the blocking input, cite the Status Enum entry, and
state what invocation or spec change would change its status to RESOLVED. Do not produce Execute.

---

### Execute

Carrying forward: resolved values from Bind. B-NN gaps noted.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every spec-required section must appear -- with content or with an explicit B-NN marker. No
elision markers anywhere.

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact]

[ARTIFACT ENDS HERE]

---

### Verdict (Compliance Ledger)

**Compliance Ledger** -- this is a structured table, not a prose summary. The Evidence column
must name a specific structural element in this document (table header, row count, delimiter
string, or section header). Entries such as "looks correct" or "seems complete" are structural
failures of C-15.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Section headers at: Gather §[location], Bind §[location], Execute §[location], Verdict §[location] |
| C-02 | Gather inputs enumerated by name + source | PASS / FAIL | Gather table: [N] rows; Source column populated for all [N] rows |
| C-03 | Bind maps every Gather input to one resolved value | PASS / FAIL | Bind resolution table: [N] rows = Gather [N] rows; Resolved Value column non-blank for all |
| C-04 | Execute produces artifact with correct naming + sections | PASS / FAIL | Artifact filename: {topic}-{signal}-{date}.md; required sections: [list from spec] |
| C-05 | Verdict declares PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row below |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Gather / Bind / Execute / Verdict |
| C-07 | Verdict cites criterion IDs | PASS / FAIL | C-01 through C-NN present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned for "...", "[omitted]", "[content here]": [found / not found] |
| C-13 | Artifact delimiter markers present | PASS / FAIL | Strings "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute at [line or section] |
| C-15 | Verdict is compliance ledger with Evidence column | PASS / FAIL | This table contains ID, Criterion, Result, Evidence columns; Evidence column cites structural loci |
| C-16 | Bind Status Enum declared (RESOLVED/UNRESOLVED/BLOCKED) | PASS / FAIL | Status Enum definition table present above Bind resolution table; three-value enum declared |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block present before Bind resolution table; invocation-override rule named |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [name failing essential criterion and evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Role sequence (spec-first Gather + Bind conflict precedence declaration)

**Axis**: Role sequence and Bind declaration order. Gather is structured in two explicit tiers:
Tier 1 enumerates every input the spec declares (required and optional) before the invocation
is consulted; Tier 2 maps invocation tokens onto Tier 1 slots. The spec anchors the input
space; the invocation is a constraint layer applied on top. In Bind, a conflict precedence rule
is declared as a named block before any resolution row is written -- the rule is visible when
each row is resolved, not inferred from surrounding context.

**Hypothesis**: When Gather begins from the invocation rather than the spec, the tracer risks
enumerating only what the invocation explicitly mentions and missing spec-required inputs the
invocation leaves implicit (C-11). Spec-first enumeration forces a full spec read before the
invocation is consulted. C-11 is satisfied structurally: Tier 1 always precedes Tier 2, and
Tier 1 is forbidden from consulting the invocation. C-17 is satisfied by declaring the conflict
precedence rule as a named block before any Bind row -- a model that sees the rule before
resolving row 1 applies it consistently; a model that sees it after the table may apply it
inconsistently. Risk: the spec may be large or poorly organized; the tier separation helps only
if the instruction "read the spec completely before starting Tier 1" is followed. Risk mitigation
for C-17: "named block" means a visually distinct declaration (heading + rule text), not inline
prose buried in the Bind table instructions.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.
The spec defines the complete input space. The invocation constrains it. Do not consult the
invocation during Tier 1.

#### Gather Tier 1 -- Spec-defined inputs (spec read before invocation)

List every input the spec declares. For each: record Required/Optional, the source type the
spec names, and the spec default if one exists.

| Input Name | Required? | Spec Source Type | Spec Default | Notes |
|------------|-----------|-----------------|-------------|-------|
| skill_name | YES | invoker-supplied | (none) | |
| skill_spec_path | YES | invoker-supplied | (none) | |
| topic | YES | invoker-supplied | (none) | |
| date | YES | runtime | today's date | |
| [spec-required input N] | YES / NO | | | |
| [spec-optional input N] | NO | | | |

Do not skip optional inputs. An optional input with no default that the invoker does not supply
is a gap candidate even though it is not required.

#### Gather Tier 2 -- Invocation-supplied values (read invocation after spec enumeration)

Now read the test invocation: `{{invocation}}`

Map each invocation token to a Tier 1 slot. Flag any Required Tier 1 input the invocation does
not supply as G-NN.

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| [spec input N] | | YES / NO (G-NN) |

**Carry forward**: the merged input set (Tier 1 spec declarations + Tier 2 invocation values,
with G-NN gaps flagged) to Bind.

---

### Bind

**Conflict Precedence Rule** (declared before any resolution row):

> When a Tier 1 spec default and a Tier 2 invocation-supplied value occupy the same input slot
> and disagree, the invocation wins (runtime override). Rationale: the invocation is the
> caller's specific request; the spec default is a fallback for absent values, not a constraint
> that blocks a valid invocation.
>
> Exception: if the invocation value violates the spec's declared type or format contract
> (e.g., wrong data type, invalid enum member, missing required subfield), status is BLOCKED.
> An invocation cannot override a type or format contract violation -- the caller must supply
> a conforming value.

Apply this rule to every row. Cite "invocation override" or "spec default retained" explicitly
in the Resolved Value cell for any row where spec and invocation differ.

**Resolution table** -- one row per merged Tier 1 + Tier 2 input:

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status |
|-------|--------------------|-----------------------|-----------|----------------|--------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED / UNRESOLVED (G-NN) |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED |
| [spec input N] | [default] | [invocation or --] | YES / NO | [per conflict rule] | RESOLVED / UNRESOLVED / BLOCKED |

**Bind gate**: Any BLOCKED row halts Execute. Name the blocking row, cite the conflict rule
exception that applies, and state what invocation change would change status to RESOLVED.

---

### Execute

Carrying forward: resolved inputs from Bind. G-NN unresolved gaps noted.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every spec-required section must appear -- with content or with an explicit G-NN marker. No
elision markers.

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact]

[ARTIFACT ENDS HERE]

---

### Verdict

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS / FAIL | Four phase headers present in sequence |
| C-02 | PASS / FAIL | Gather Tier 1 + Tier 2 tables populated with name + source for all inputs |
| C-03 | PASS / FAIL | Bind table row count = Gather merged input count; one Resolved Value per row |
| C-04 | PASS / FAIL | Artifact filename + required sections vs spec |
| C-05 | PASS / FAIL | This verdict table, Overall result |
| C-11 | PASS / FAIL | Tier 1 section present before Tier 2 section in Gather; spec consulted before invocation |
| C-17 | PASS / FAIL | Conflict Precedence Rule block present before Bind resolution row 1; invocation-override and exception declared |

**Overall**: PASS / FAIL

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Phase Schema + Bind Status Enum + Conflict Precedence (C-14, C-16, C-17)

**Axes**:
- Lifecycle emphasis: Phase Label Schema table as immutable pre-trace preamble (C-14); phase
  headers transcribed from schema, not generated.
- Output format: Bind three-value Status Enum declared as a formal definition block before the
  resolution table (C-16); BLOCKED is a first-class column value, not a prose gate.
- Role sequence / Bind declaration: explicit conflict precedence rule declared as a named block
  before any resolution row (C-17); conflict resolution is cited per row, not inferred.

**Hypothesis**: C-14, C-16, and C-17 all operate at the structural-declaration layer -- they
require something to be explicitly declared before content is produced, rather than discovered
after the fact. Combining all three in one variation tests whether pre-declaration patterns are
compositional: a prompt that opens with a Phase Label Schema, then opens Bind with a Status Enum
definition, then opens Bind's resolution table with a Conflict Precedence Rule establishes a
consistent "declare before you use" rhythm. Each subsequent phase knows the schema; each Bind
row knows the Status vocabulary and conflict rule before it is written. Risk: three pre-content
declarations add length before trace content begins; a model that skims instructions may see
the declarations as boilerplate and proceed without internalizing them. Mitigation: each
declaration names the specific criterion it satisfies, making the structural purpose legible.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- declared before trace begins)

This block exists before any phase. Phase headers in this document are transcribed from this
table -- do not generate them from memory or context.

| Phase | Canonical Header | Prohibited Synonyms |
|-------|-----------------|---------------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context, Inputs |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare, Init |
| 3 | `## Execute` | Run, Simulate, Produce, Compile, Perform |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion, Output |

The Verdict compliance ledger checks C-14 (this schema table present before phase 1) and C-06
(all phase headers match this schema) as distinct row entries.

---

## Gather

Read `{{skill_spec_path}}` completely, then read `{{invocation}}`. Enumerate every input.

**Spec-first rule**: enumerate spec-declared inputs in Tier 1 before consulting the invocation.

#### Gather Tier 1 -- Spec-declared inputs

| Input Name | Required? | Spec Source Type | Spec Default |
|------------|-----------|-----------------|-------------|
| skill_name | YES | invoker-supplied | (none) |
| skill_spec_path | YES | invoker-supplied | (none) |
| topic | YES | invoker-supplied | (none) |
| date | YES | runtime | today |
| [spec input N] | | | |

#### Gather Tier 2 -- Invocation-supplied values

| Tier 1 Input | Invocation Value | Supplied? |
|--------------|-----------------|-----------|
| skill_name | {{skill_name}} | YES |
| skill_spec_path | {{skill_spec_path}} | YES |
| topic | [from invocation] | YES / NO (G-NN) |
| date | {{date}} | YES |
| [spec input N] | | YES / NO (G-NN) |

Any Required Tier 1 input missing from Tier 2 is G-NN. Carry all rows to Bind.

---

## Bind

**Status Enum (declared before resolution table -- three values only):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value; source named | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Affected artifact sections marked B-NN; trace continues |
| BLOCKED | Conflict or type violation; artifact production impossible | Halt. State blocking input and unblock condition. |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides spec default when both are present and they disagree.
> Exception: if the invocation value violates the spec's type or format contract, status
> is BLOCKED. An invocation cannot override a contract violation.

**Resolution table -- one row per merged input, Status from declared enum only:**

| Input | Spec Default | Invocation Value | Conflict? | Resolved Value | Status |
|-------|-------------|------------------|-----------|----------------|--------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED |
| [spec input N] | [default] | [invocation or --] | YES / NO | [per conflict rule] | RESOLVED / UNRESOLVED / BLOCKED |

**Bind gate**: Any BLOCKED row halts Execute. Name the input, cite the Status Enum BLOCKED row,
and state what invocation change unblocks it.

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Run each spec-defined role in sequence. Every spec-required section must appear -- with content
or explicit B-NN marker. No elision markers.

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Evidence column must name a specific structural element in this document. Generic "looks correct"
entries are structural failures of C-15 independently of C-05.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1 + Tier 2 tables; [N] total inputs; source type column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = Tier 1 count; Resolved Value non-blank; Status column values from enum only |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Filename; sections [list]; delimiters present |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema table above |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned; result: [found / not found] |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 present; precedes Tier 2; spec consulted first |
| C-13 | Artifact delimiter markers present | PASS / FAIL | [ARTIFACT BEGINS HERE] / [ARTIFACT ENDS HERE] in Execute |
| C-14 | Phase Label Schema table declared pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Gather |
| C-15 | Verdict is compliance ledger (ID/Result/Evidence) | PASS / FAIL | This table; ID, Criterion, Result, Evidence columns present; Evidence column cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Status Enum definition table above Bind resolution table; RESOLVED/UNRESOLVED/BLOCKED declared |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block above Bind row 1; invocation-override rule + exception stated |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined golden: all aspirationals C-09 through C-17

**Axes** (all aspirationals, full integration):

- Coverage Matrix + BLOCKED gate (C-09, C-12): closed-world authority declared before Gather;
  any Required=YES / Gap=YES row halts trace before Gather begins.
- Spec-first Gather in two tiers (C-11): Tier 1 reads spec before invocation.
- Relay carry in Execute (C-10): per-role relay table (role / signal / binding / status) before
  artifact content; Verdict reads relay table, not artifact body.
- Artifact delimiter markers (C-13): [ARTIFACT BEGINS HERE] / [ARTIFACT ENDS HERE].
- Phase Label Schema table preamble (C-14): immutable pre-trace declaration before Coverage Matrix.
- Verdict compliance ledger (C-15): ID | Criterion | Result | Evidence; structural evidence loci.
- Bind three-value Status Enum (C-16): RESOLVED / UNRESOLVED / BLOCKED declared before rows.
- Bind conflict precedence rule (C-17): named block before resolution rows; invocation-override.

**Hypothesis**: Each criterion targets an independent failure mode at a different structural
layer: C-14 (pre-trace header commitment) → C-09/C-12 (pre-Gather input completeness gate) →
C-11 (spec-first Gather ordering) → C-16/C-17 (Bind resolution unambiguity) → C-10 (Execute
relay evidence chain) → C-13 (artifact boundary) → C-15 (Verdict structural evidence). These
layers do not overlap: satisfying C-14 does not satisfy C-16, and satisfying C-09 does not
satisfy C-11. A prompt that addresses all eight simultaneously must do so in structural sequence,
not by phrasing alone. Risk: V-05 is the longest variation; each layer adds length. A model with
limited context attention may satisfy early layers (C-14, C-09) and skip later ones (C-16, C-17).
Mitigation: the compliance ledger Verdict is the last phase and checks all criteria explicitly;
the model must produce evidence for each row or leave it blank, which is itself a fail signal.

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

### Coverage Matrix (closed-world authority -- declared before Gather runs)

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input. An input absent from this matrix that Gather encounters is
Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |
| [optional input N] | NO | repo-detected | |

**Coverage Matrix BLOCKED gate**: Before Gather, scan this table.

- Any Required=YES row with Gap=YES: **BLOCKED**. The trace cannot produce a valid artifact
  without this input. Name each blocking input. State what invocation change or spec revision
  would unblock it. Do not produce Gather, Bind, Execute, or Verdict below this point.
- All Required=YES rows Gap=NO: proceed to Gather.

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
| BLOCKED | Type / format contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating the spec's type or format contract → BLOCKED.
> Each row with a conflict cites "invocation override applied" or "spec default retained" in
> Resolved Value cell.

**Resolution table:**

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status |
|-------|--------------------|-----------------------|-----------|----------------|--------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED |
| [optional N] | [default] | [invocation or --] | YES / NO | [per rule] | RESOLVED / UNRESOLVED / BLOCKED |

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED entry. State unblock condition.

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay carry (C-10)**: For each stock role, produce one relay row before artifact content.
The relay table is the evidence chain. The Verdict reads relay row status -- it does not
reconstruct evidence from the artifact body.

| Role | Signal | Binding (Bind row used) | Status |
|------|--------|------------------------|--------|
| [Role 1] | [contribution to artifact] | [Bind input name] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | | |

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions.
Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table. Do not reconstruct evidence from the artifact body. The relay
table is the primary evidence source for all criterion checks involving Execute content.

Evidence column must name a specific structural element (table header, row count, delimiter
string, relay row status, section heading). Generic entries fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value column non-blank |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble |
| C-07 | Verdict cites criterion IDs | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned: [result] |
| C-09 | Coverage Matrix with closed-world preamble | PASS / FAIL | Coverage Matrix block present before Gather; closed-world preamble text present |
| C-10 | Execute relay carry; Verdict reads relay, not artifact | PASS / FAIL | Relay table in Execute: [N] rows, COMPLETE/PARTIAL status; this Verdict row cites relay status, not artifact body |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 section precedes Tier 2 section in Gather |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present in Coverage Matrix; Gap=YES halts trace before Gather |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute section |
| C-14 | Phase Label Schema table declared pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict is compliance ledger (ID/Result/Evidence) | PASS / FAIL | This table; ID, Criterion, Result, Evidence columns; Evidence column cites structural loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Status Enum definition table above Bind resolution table; RESOLVED/UNRESOLVED/BLOCKED all defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block above Bind row 1; invocation-override rule + BLOCKED exception stated |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
