---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 5
rubric: trace-skill-rubric-v4-2026-03-15.md
---

# trace-skill -- Variations v4 R5 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: All five R4 variations score 100/100 under rubric v3 (C-01 through C-17).
Rubric v4 formalizes three R4 excellence patterns as new aspirational criteria (C-18, C-19, C-20).

R4 state against v4 rubric (projected):

| Variation | C-18 (relay provenance) | C-19 (per-row conflict) | C-20 (CM CLOSED assertion) | v4 Total |
|-----------|-------------------------|-------------------------|---------------------------|----------|
| V-01 | PASS (relay binding present) | FAIL | FAIL | 98.3 |
| V-02 | FAIL | FAIL | FAIL | 97.5 |
| V-03 | FAIL | PASS (Precedence applied column) | FAIL | 98.3 |
| V-04 | PASS | PASS | PASS | 100 |
| V-05 | PASS | PASS | PASS | 100 |

R4 V-04 and V-05 already pass all 20 criteria. R5 goals:
1. Build single-axis structural paths for C-18, C-19, C-20 individually (V-01, V-02, V-03)
2. Make each new criterion schema-enforced (declared before rows, not emergent from depth)
3. Demonstrate all three combined in two new combined architectures (V-04, V-05)

**R5 variation axes**:

Single-axis:
- V-01: Output format -- Relay Schema declaration before Execute (structural C-18 enforcement)
- V-02: Lifecycle emphasis -- Bind Schema block with Precedence Applied vocabulary (structural C-19)
- V-03: Phrasing register -- formal CLOSED ASSERTION block after Coverage Matrix gate (structural C-20)

Combined:
- V-04: Relay Schema (C-18) + Bind Schema with Precedence (C-19) as "Binding Evidence Architecture"
- V-05: All three new criteria as explicit named structural elements -- full v4 golden

---

## V-01 -- Single axis: Output format (Relay Schema declaration for C-18)

**Axis**: Output format -- a "Relay Schema" block is declared before the first role relay row
is written, exactly as the Phase Label Schema is declared before phases begin. The schema
mandates a `Binding` column with format constraint: `InputName = "ResolvedValue"` -- a verbatim
key=value pair from the Bind resolution table. Relay rows are transcribed from this schema
rather than generated from context. C-18 is satisfied structurally when the schema exists and
relay rows follow its declared format.

**Hypothesis**: In R4, C-18 was present in V-01/V-04/V-05 as an extension of C-10 -- the model
went far enough to include resolved values in relay Binding cells because the instructions pushed
toward depth. Without a schema declaration, C-18 is model-behavior-dependent: a model that
stops at input-name-only binding satisfies C-10 but fails C-18. A pre-declared Relay Schema
converts C-18 from "present when the model is thorough" to "structurally enforced." The schema
also distinguishes C-10's binding requirement (input name sufficient) from C-18's binding
requirement (resolved value required), making the distinction explicit to the tracer. Risk: the
schema declaration adds a pre-relay block; a model may declare the schema and still produce
relay rows with input names only. Mitigation: the schema includes a "Do NOT" prohibition in
the Format constraint cell and a concrete example showing the `InputName = "ResolvedValue"`
form.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input. An input absent from this matrix that Gather encounters is
a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what
  invocation change or spec revision would unblock it. Do not produce Gather, Bind, Execute,
  or Verdict.
- All Required=YES rows Gap=NO: proceed to Gather.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.
The spec defines the input space; the invocation constrains it.

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
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; affected sections marked B-NN |
| BLOCKED | Type / format contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating the spec's type or format contract → BLOCKED.
> Rows with a conflict cite "invocation override applied" or "spec default retained" in
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
| [optional N] | [default] | [invocation or --] | YES / NO | [per conflict rule] | RESOLVED / UNRESOLVED / BLOCKED |

**Bind gate**: Any BLOCKED row halts Execute. Cite the Status Enum BLOCKED entry. State unblock
condition. Do not produce Execute or Verdict.

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay Schema (declared before relay rows -- C-18 structural enforcement):**

This table declares the required columns for every role relay row. Relay rows are transcribed
from this schema -- do not generate columns from context.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | What this role contributes to the artifact (brief phrase) |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind Resolved Value cell. Example: `topic = "payments-flow"`. Do NOT write an input name only. The resolved value must be stated verbatim. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked) |

After declaring this schema, produce the relay table. One row per spec-defined role.

**Relay table:**

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table. It does not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions.
Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table. Evidence column must name a specific structural element
(table header, row count, delimiter string, relay row Binding cell value, section heading).
Generic entries ("looks correct", "seems complete") fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers match Phase Label Schema preamble |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-NN present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; this row cites relay, not artifact body |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present in Coverage Matrix; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites structural loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Status Enum definition table above Bind resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block above Bind row 1; invocation-override + exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema block present above relay table; relay Binding column sample: [paste one Binding cell] -- key=value format confirmed (resolved value present, not input name only) |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (Bind Schema with Precedence Applied vocabulary for C-19)

**Axis**: Lifecycle emphasis -- the Bind section opens with a unified "Bind Schema" block that
declares all three resolution-governing sub-schemas before any resolution row is written. Part 1
is the Status Enum (C-16). Part 2 is the Conflict Precedence Rule (C-17). Part 3 is the
Precedence Applied Vocabulary -- three values (`override` / `default` / `BLOCKED`) declared as
a required column in the resolution table. The resolution table gains a `Precedence applied`
column whose values are transcribed from the Part 3 vocabulary. Per-row conflict traceability
is structural, not instructional.

**Hypothesis**: C-17 requires the conflict rule be declared once; C-19 requires each row show
which rule applied. In R4, V-03/V-04/V-05 had a "Precedence applied" column but it emerged
from an extension of the Conflict Precedence Rule prose -- it was not a declared required column
in a named schema. Without a schema declaration for this column, a model may produce it in rows
where a conflict is visible and omit it in rows with `Conflict? = NO`. A unified Bind Schema
block that declares "Precedence applied" as a required column -- before any row is written --
makes per-row annotation structural. Risk: three-part schema block lengthens Bind preamble;
a model that skims may declare Part 3 and fill the column inconsistently. Mitigation: Part 3
includes a "do not use free-form annotation" prohibition alongside the three-value vocabulary
declaration.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what
  change would unblock it. Do not produce Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: proceed to Gather.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.

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

**Bind Schema (declared before all resolution rows -- structural enforcement for C-16, C-17, C-19):**

Three-part schema governing every Bind resolution row. Produce rows only after reading all
three parts completely.

**Part 1 -- Resolution Status Enum (three values only; no others permitted):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule (governing rule for Conflict? = YES rows):**

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree,
> the invocation wins (runtime override). Exception: if the invocation value violates the spec's
> declared type or format contract, status is BLOCKED. An invocation cannot override a contract
> violation.

**Part 3 -- Precedence Applied Vocabulary (required column; three values only):**

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value, or only one source present | Conflict? = NO |
| `BLOCKED` | Conflict rule exception applied; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one of these values in `Precedence applied`. Do NOT use
free-form annotation ("invocation wins", "spec default used", "n/a") in this column.

**Bind gate**: Any BLOCKED row halts Execute. Cite the Status Enum BLOCKED entry. Name the
blocking row. State unblock condition.

**Resolution table (one row per merged Tier 1 + Tier 2 input):**

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied |
|-------|--------------------|-----------------------|-----------|----------------|--------|--------------------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED | default |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED | default |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED | default |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED | default |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| [optional N] | [default] | [invocation or --] | YES / NO | [per rule] | RESOLVED / UNRESOLVED / BLOCKED | override / default / BLOCKED |

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay carry (C-10)**: For each stock role, produce one relay row before artifact content.
Verdict reads relay row status.

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

Read the Execute relay table. Evidence must name specific structural elements.
Generic entries fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows = merged count; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers match Phase Label Schema preamble |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; this row cites relay |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate block present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 table above resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 block above row 1; invocation-override + exception stated |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 vocabulary table present; resolution table Precedence applied column: [N] rows populated; sample values: [list 3 cells] -- vocabulary terms (override/default/BLOCKED) confirmed |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Phrasing register (formal CLOSED ASSERTION block for C-20)

**Axis**: Phrasing register -- formal and declarative throughout. The key addition: after the
Coverage Matrix BLOCKED gate passes, a named "CLOSED ASSERTION" block is required before Gather
begins. The block declares each Required=YES input from the Coverage Matrix by name, confirms
Gap=NO for each, and closes with the statement "Coverage Matrix is CLOSED for this invocation."
The Verdict cites the CLOSED ASSERTION block by name for C-20 -- converting gate-pass from an
absence-of-BLOCKED inference into a positive structural citation target.

**Hypothesis**: C-20 requires the Coverage Matrix carry a CLOSED assertion naming each
Required=YES input explicitly. In R4, V-04/V-05 had this pattern as an extension of C-12 --
the CLOSED assertion appeared as a note appended to the gate block. Without a standalone named
block, a Verdict row for C-20 must cite the gate block generally ("BLOCKED gate present; no
BLOCKED found") rather than a named assertion specifically ("CLOSED ASSERTION block at §X names
skill_name, skill_spec_path, topic, ..."). The formal phrasing register makes the CLOSED
ASSERTION visually distinct and independently citable. Risk: a model may merge the CLOSED
ASSERTION text into the gate block rather than producing it as a separate named block. Mitigation:
the instructions explicitly label the block "CLOSED ASSERTION" as a separate heading-level
element and instruct the model to produce it after the gate passes, not within it.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input. An input absent from this matrix that Gather encounters is
a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what
  invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION,
  Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below.

---

### CLOSED ASSERTION

This block is the formal gate-pass record and is produced only when the BLOCKED gate passes.
It names each Required=YES input from the Coverage Matrix and confirms availability. The Verdict
compliance ledger cites this block by name for C-20. A Verdict row for C-20 that cites only the
Coverage Matrix gate text (not this named block) does not satisfy C-20.

> The following Required=YES inputs are confirmed available for this trace invocation
> (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one per line]

Coverage Matrix is CLOSED for this invocation. Proceed to Gather.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.

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
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; sections marked B-NN |
| BLOCKED | Type / format contract violation | Halt; state unblock condition |

**Conflict Precedence Rule (declared before resolution rows):**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating the spec's type or format contract → BLOCKED.
> Rows with a conflict cite "invocation override applied" or "spec default retained" in
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
| [optional N] | [default] | [invocation or --] | YES / NO | [per conflict rule] | RESOLVED / UNRESOLVED / BLOCKED |

**Bind gate**: Any BLOCKED row halts Execute. Cite the Status Enum BLOCKED entry. State unblock
condition.

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay carry (C-10)**: For each stock role, produce one relay row before artifact content.
Verdict reads relay row status.

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

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific
structural elements. Generic entries fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers match Phase Label Schema preamble |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; this row cites relay |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate block present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Status Enum table above Bind resolution rows |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Conflict Precedence Rule block above Bind row 1 |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present between Coverage Matrix gate and Gather; Required=YES inputs enumerated by name: [count] inputs listed (skill_name, skill_spec_path, topic, date, stock_roles, output_section_list, ...) |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Output format (Relay Schema / C-18) + Lifecycle emphasis (Bind Schema / C-19)

**Axes**:
- Output format: Relay Schema declaration before Execute relay rows (C-18). Relay Binding
  column carries `InputName = "ResolvedValue"` verbatim pairs declared as required format.
- Lifecycle emphasis: Bind Schema block (Status Enum / Conflict Precedence Rule / Precedence
  Applied vocabulary) declared before resolution rows (C-19). "Precedence applied" column is
  schema-declared required.

**Hypothesis**: These two axes share a structural pattern: declaring a row schema before
producing rows converts format compliance from model-behavior-dependent to structural. The Bind
Schema declares three sub-schemas (status vocabulary, conflict rule, precedence vocabulary) as
a unified block; the Relay Schema declares relay row columns. Together they establish a
"declare-before-rows" rhythm across both production phases. C-18 and C-19 become schema-
transcription behaviors rather than optional depth signals. Risk: two schema declaration blocks
(Bind Schema + Relay Schema) increase prompt length before production content begins. A model
that skims declarations may declare both schemas and produce non-conforming rows. Mitigation:
each schema includes a prohibited-form statement -- Bind Schema Part 3 prohibits free-form
annotation; Relay Schema prohibits input-name-only Binding cells.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input.

| Input | Required? | Expected Source | Gap? |
|-------|-----------|----------------|------|
| skill_name | YES | invocation | NO |
| skill_spec_path | YES | invocation | NO |
| topic | YES | invocation-parsed | |
| date | YES | runtime | NO |
| stock_roles | YES | spec-defined | |
| output_section_list | YES | spec-defined | |
| [optional input N] | NO | repo-detected | |

**Coverage Matrix BLOCKED gate**:

- Any Required=YES row with Gap=YES: **BLOCKED**. Name blocking inputs. State unblock
  condition. Do not produce Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: proceed to Gather.

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
| [optional input N] | NO | repo-detected | [spec default] |

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

**Bind Schema (declared before all resolution rows -- C-16, C-17, C-19 structural enforcement):**

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; B-NN gap | Proceeds; sections marked B-NN |
| BLOCKED | Type / format contract violation | Halt; state unblock condition |

**Part 2 -- Conflict Precedence Rule:**

> Invocation value overrides Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating the spec's type or format contract → BLOCKED.

**Part 3 -- Precedence Applied Vocabulary (required column; three values only):**

| Value | Meaning |
|-------|---------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default; conflict present |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict |
| `BLOCKED` | Conflict rule exception; type or format violation; row status = BLOCKED |

Every resolution row carries exactly one of these values in `Precedence applied`.
Do NOT use free-form annotation in this column.

**Bind gate**: Any BLOCKED row halts Execute. Name the blocking row. State unblock condition.

**Resolution table:**

| Input | Tier 1 Default | Tier 2 Invocation | Conflict? | Resolved Value | Status | Precedence applied |
|-------|---------------|------------------|-----------|----------------|--------|--------------------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED | default |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED | default |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED | default |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED | default |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| [optional N] | [default] | [invocation or --] | YES / NO | [per rule] | RESOLVED / UNRESOLVED / BLOCKED | override / default / BLOCKED |

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay Schema (declared before relay rows -- C-18 structural enforcement):**

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in spec |
| Signal | YES | What this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` verbatim pair from Bind Resolved Value cell. Example: `topic = "payments-flow"`. Do NOT write input name only. |
| Status | YES | COMPLETE / PARTIAL (B-NN) |

**Relay table:**

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table. Does not reconstruct evidence from artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions.
Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table. Evidence must name specific structural elements.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers match Phase Label Schema preamble |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-NN as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; this row cites relay |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate block present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 table above resolution rows; 3-value enum defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 block above row 1; invocation-override + exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" | PASS / FAIL | Relay Schema block present above relay table; Binding column sample: [paste one cell] -- key=value format confirmed |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 vocabulary present; resolution table Precedence applied column: [N] rows, sample values: [list 3] -- vocabulary terms confirmed |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined golden: Relay Schema (C-18) + Bind Schema (C-19) + CLOSED ASSERTION (C-20)

**Axes** (all three R4 excellence patterns as explicit structural requirements):

- Output format: Relay Schema declaration before Execute relay rows (C-18). Relay Binding
  column carries `InputName = "ResolvedValue"` verbatim pairs declared as required format.
- Lifecycle emphasis: Bind Schema block (Status Enum / Conflict Precedence Rule / Precedence
  Applied vocabulary) declared before resolution rows (C-19). "Precedence applied" column
  is schema-declared required with a three-value vocabulary (override/default/BLOCKED).
- Phrasing register: formal CLOSED ASSERTION block after Coverage Matrix gate passes (C-20).
  Block names each Required=YES input by name. Verdict cites CLOSED ASSERTION explicitly.

**Hypothesis**: All three R4 excellence patterns target the same underlying failure mode --
structural presence without structural enforcement. C-18 emerges in relay rows only when the
model goes far enough; C-18 is structural when a Relay Schema requires it. C-19 emerges in the
Bind table only when per-row annotation is natural; C-19 is structural when a Bind Schema
declares it required. C-20 exists as an implicit gate-pass that cannot be positively cited;
C-20 is structural when a named CLOSED ASSERTION block is produced. The three axes together
complete the binding evidence chain: Coverage Matrix → CLOSED ASSERTION (C-20) → Gather →
Bind with per-row precedence (C-19) → Relay with verbatim binding pairs (C-18) → Verdict
citing all three named blocks. Risk: four pre-content schema/preamble blocks (Phase Label
Schema, Coverage Matrix + CLOSED ASSERTION, Bind Schema, Relay Schema) precede production
content. Length pressure may cause model to skip later schemas. Mitigation: the Verdict
compliance ledger checks all 20 criteria with named structural evidence loci; any schema
declared but not applied produces a FAIL in its Verdict row -- failure is visible, not silent.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase Label Schema (IMMUTABLE -- pre-trace preamble)

Declared before all content. Phase headers in this document are transcribed from this table only.

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

---

### Coverage Matrix (closed-world authority -- before Gather)

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.
Gather confirms each declared input. An input absent from this matrix that Gather encounters is
a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what
  invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION,
  Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then
  proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the
Coverage Matrix and confirms it is available for this trace invocation. The Verdict compliance
ledger cites this block by name for C-20. A Verdict row for C-20 that cites only the Coverage
Matrix gate text (not this named block) does not satisfy C-20 -- C-20 requires the closed-world
enumeration to be a named positive structural element, not inferred from the absence of a
BLOCKED branch.

> The following Required=YES inputs are confirmed available for this trace invocation
> (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

Coverage Matrix is CLOSED for this invocation. Proceed to Gather.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation.
The spec defines the input space; the invocation constrains it.

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

**Bind Schema (declared before all resolution rows):**

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only; no others permitted):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule:**

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree,
> the invocation wins (runtime override). Exception: if the invocation value violates the spec's
> declared type or format contract, status is BLOCKED. An invocation cannot override a contract
> violation.

**Part 3 -- Precedence Applied Vocabulary (required column; three values only):**

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one of these values in `Precedence applied`.
Do NOT use free-form phrases ("invocation wins", "spec default used") in this column.

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED entry. Name blocking row.
State unblock condition.

**Resolution table:**

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied |
|-------|--------------------|-----------------------|-----------|----------------|--------|--------------------|
| skill_name | (none) | {{skill_name}} | NO | {{skill_name}} | RESOLVED | default |
| skill_spec_path | (none) | {{skill_spec_path}} | NO | {{skill_spec_path}} | RESOLVED | default |
| topic | (none) | [from invocation] | NO | [resolved] | RESOLVED | default |
| date | runtime | {{date}} | NO | {{date}} | RESOLVED | default |
| stock_roles | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| output_section_list | [spec list] | -- | NO | [spec list] | RESOLVED | default |
| [optional N] | [default] | [invocation or --] | YES / NO | [per conflict rule] | RESOLVED / UNRESOLVED / BLOCKED | override / default / BLOCKED |

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay Schema (declared before relay rows -- C-18 structural enforcement):**

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `output_section_list = "[feasibility, blocking-gaps, amendments]"`. Do NOT write input name only. The resolved value must be present verbatim. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay table:**

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table as primary evidence source for Execute content checks. It does
not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions.
Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific
structural elements. Generic entries ("looks correct", "seems complete") fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value column non-blank for all rows |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename: {topic}-{signal}-{date}.md; required sections [list from spec] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble: Gather/Bind/Execute/Verdict |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-20 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned for "...", "[omitted]", "[content here]": [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; "closed-world preamble" text present in CM section |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status column populated; this row cites relay status, not artifact body |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 section present before Tier 2; spec consulted before invocation |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present in Coverage Matrix; Gap=YES halts trace before Gather |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" in Execute section |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix; before any phase header |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites structural elements (not prose) |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 table above resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined with Execute effects |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 block above row 1; invocation-override rule + BLOCKED exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema block present above relay table; relay Binding column sample: [paste one Binding cell] -- key=value format confirmed (resolved value present, not input name only) |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 vocabulary table present above resolution rows; Precedence applied column populated for all [N] rows; sample values: [list 3 cells] -- vocabulary terms (override/default/BLOCKED) confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present between Coverage Matrix gate and Gather; Required=YES inputs enumerated by name: [count] inputs listed (skill_name, skill_spec_path, topic, date, stock_roles, output_section_list, ...) |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
