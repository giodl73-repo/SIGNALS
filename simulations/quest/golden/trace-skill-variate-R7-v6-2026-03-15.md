---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 7
rubric: trace-skill-rubric-v6-2026-03-15.md
---

# trace-skill -- Variations R7 v6 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: Best R6 variation achieves C-01 through C-23 PASS under rubric v6. Rubric v6
adds three aspirational criteria from R6 excellence signals: C-24 (C-21 upgrade -- anti-pattern
row structurally independent with `VIOLATION` in Required column, not embedded in Format cell),
C-25 (C-22 upgrade -- vocabulary given named type `PrecedenceVocabulary`; column header cites type
by name; column is self-validating via type reference), C-26 (C-23 upgrade -- closure terminus is
a labeled structural mandate in the prompt, not emergent from model depth; line appears as an
instructed named element).

**R6 V-05 state against v6** (C-24/C-25/C-26 projected):

- C-24: FAIL. R6 V-05 Relay Schema has anti-pattern prohibition embedded in the Binding row's Format
  constraint cell ("Do NOT write input name only"). The Required column for the Binding row reads
  YES, not VIOLATION. An evaluator must parse the Format cell to find the prohibition. C-24 requires
  VIOLATION as a standalone Required column value on a structurally isolated row -- independently
  citable without Format cell inspection.

- C-25: FAIL. R6 V-05 Bind Schema Part 3 is labelled "Precedence Applied Vocabulary" and declares
  three values (override/default/BLOCKED), but does not declare a named type. The resolution table
  column header reads "Precedence applied" without citing a type. C-25 requires the type name
  (`PrecedenceVocabulary` or equivalent) to appear both in the type declaration and in the column
  header -- making the column self-validating by type reference, not by proximity to the declaration.

- C-26: FAIL. R6 V-05 CLOSED ASSERTION ends with "Coverage Matrix is CLOSED for this invocation.
  Proceed to Gather." -- the terminus line is present but emerges from prompt depth, not from a
  labeled structural mandate. A model that abbreviates the CLOSED ASSERTION block may omit it
  without violating any stated structural rule. C-26 requires the terminus line to be named as a
  structural element in the prompt, so that its absence is identifiable as a violation.

**R7 variation axes**:

- **Output format (C-24)**: Relay Schema restructured into two sub-tables -- (1) Required Columns
  (all Required = YES) and (2) Anti-Pattern Prohibition (Required = VIOLATION). The VIOLATION value
  in the Required column is the sole structural signal identifying the prohibition row; the row is
  independently citable without inspecting the Format/Prohibition cell (V-01).

- **Phrasing register (C-25)**: Bind Schema Part 3 refactored as a named type declaration
  `PrecedenceVocabulary`. The type declaration uses `type PrecedenceVocabulary = override | default
  | BLOCKED` syntax before the vocabulary table. The resolution table column header cites the type:
  `Precedence applied (PrecedenceVocabulary)`. Column is self-validating: header -> type -> valid
  values, without proximity search (V-02).

- **Lifecycle emphasis (C-26)**: CLOSED ASSERTION block gains a named structural sub-element:
  `Closure Terminus`. The prompt declares this element by name, specifies its exact content, and
  states that its absence is a structural violation. Verdict C-23 row cites `Closure Terminus`
  labeled element specifically -- the citation target exists before the trace runs (V-03).

**Combined variations**:
- V-04: C-24 + C-25 (Output format + Phrasing register)
- V-05: C-24 + C-25 + C-26 (all three new criteria -- full R7 golden target)

All five inherit the full R6 V-05 architecture (C-01 through C-23 PASS). What varies per V-0N:
only the C-24/C-25/C-26 structural mechanisms.

---

## V-01 -- Single axis: Output format (C-24: anti-pattern row structural isolation)

**Axis**: Output format -- the Relay Schema is split into two named sub-tables. Sub-table 1
("Column Definitions") carries all Required = YES rows. Sub-table 2 ("Anti-Pattern Prohibition")
carries exactly one row with Required = VIOLATION. The split makes the Required column value the
sole structural signal for row classification: every row in sub-table 2 is a prohibition by virtue
of its Required = VIOLATION value, independently of Format or Prohibition cell content. An
evaluator scanning only the Required column can identify the anti-pattern row without reading any
other cell.

**Hypothesis**: R6 V-05 embeds "Do NOT write input name only" inside the Format constraint cell of
the Binding row (Required = YES). An evaluator must parse the Format cell to locate the prohibition.
C-24 closes this gap: the prohibition row is structurally isolated in its own sub-table, and
VIOLATION in the Required column is the structural identity signal. The C-21 criterion (prohibition
present) remains satisfied; C-24 adds independent citability. Risk: two sub-tables increase visual
surface area in the Execute section. Mitigation: sub-table 1 is unchanged from R6; sub-table 2
adds exactly one row; the split is labeled so a reader knows the partition is intentional.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation
  change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind,
  Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed
  to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage
Matrix and confirms it is available for this trace invocation. The Verdict compliance ledger cites
this block by name for C-20. A Verdict row for C-20 that cites only the Coverage Matrix gate text
(not this named block) does not satisfy C-20 -- C-20 requires the closed-world enumeration to be
a named positive structural element, not inferred from the absence of a BLOCKED branch.

> The following Required=YES inputs are confirmed available for this trace invocation
> (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

Coverage Matrix is CLOSED for this invocation.

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

**Bind Schema (declared before all resolution rows -- C-16, C-17, C-19 structural enforcement):**

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

**Part 3 -- Precedence Applied Vocabulary (closed; exactly three values permitted; no others):**

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one of these values in `Precedence applied`.
No other annotation values are permitted in this column. Do NOT write free-form phrases.

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

**Relay Schema -- Column Definitions (C-18, C-24: Required = YES rows):**

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `date = "2026-03-15"`. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay Schema -- Anti-Pattern Prohibition (Required = VIOLATION):**

| Column | Required | Prohibition |
|--------|----------|-------------|
| Binding (Anti-pattern) | VIOLATION | Do NOT write the input name alone. `topic` without the resolved value is a VIOLATION of the Binding Required format. The resolved value must be present verbatim: write `topic = "payments-flow"` not `topic`. |

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
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-24 present as rows in this table |
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
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Column Definitions table present; Binding column Required=YES; Format constraint cites key=value form with example; relay Binding column sample: [paste one cell] |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 vocabulary table present; resolution table Precedence applied column populated for all [N] rows; sample values: [list 3] -- override/default/BLOCKED confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present between Coverage Matrix gate and Gather; Required=YES inputs enumerated: [count] inputs listed by name |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Relay Schema Anti-Pattern Prohibition sub-table present; Binding (Anti-pattern) row present; prohibition text in Prohibition cell |
| C-22 | "Precedence applied" column closed vocabulary declared | PASS / FAIL | Bind Schema Part 3 vocabulary table: three values (override/default/BLOCKED); "no others permitted" language present |
| C-23 | CLOSED ASSERTION terminates with closure declaration line | PASS / FAIL | CLOSED ASSERTION block final line: "Coverage Matrix is CLOSED for this invocation." confirmed present |
| C-24 | Relay Schema anti-pattern row Required = VIOLATION (structurally independent) | PASS / FAIL | Relay Schema Anti-Pattern Prohibition sub-table: Binding (Anti-pattern) row Required column value = VIOLATION; row is in own sub-table, citable without parsing Prohibition cell; sub-table header "Anti-Pattern Prohibition" present |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Phrasing register (C-25: PrecedenceVocabulary named type)

**Axis**: Phrasing register -- Bind Schema Part 3 is refactored as a formal type declaration.
The vocabulary is given a named type `PrecedenceVocabulary` using `type` declaration syntax before
the vocabulary table. The resolution table column header cites the type by name: `Precedence applied
(PrecedenceVocabulary)`. The Verdict C-22 row cites the type name. A reader seeing the column header
can look up `PrecedenceVocabulary` to find valid values without searching by proximity. C-22
(closed vocabulary declared) remains satisfied; C-25 adds type reference in the column header so
the column is self-validating.

**Hypothesis**: R6 V-05 declares three values in a Part 3 block labeled "Precedence Applied
Vocabulary" -- the vocabulary is closed, but the column header reads only "Precedence applied".
An evaluator checking column validity must scan backward from the column to find Part 3 by
proximity (it is the block declared just before the table). C-25 closes this gap: the type name
appears IN the column header, so the column is self-validating by type reference at the column
header site, without backward search. Risk: adding `(PrecedenceVocabulary)` to the column header
increases column width. Mitigation: one parenthetical annotation is visually minimal and the
payoff (zero-proximity validation) is architectural.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation
  change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind,
  Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed
  to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage
Matrix and confirms it is available for this trace invocation. The Verdict compliance ledger cites
this block by name for C-20.

> The following Required=YES inputs are confirmed available for this trace invocation
> (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

Coverage Matrix is CLOSED for this invocation.

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

**Bind Schema (declared before all resolution rows -- C-16, C-17, C-19, C-25 structural enforcement):**

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

**Part 3 -- PrecedenceVocabulary (C-25: named type declaration):**

`type PrecedenceVocabulary = override | default | BLOCKED`

The `Precedence applied (PrecedenceVocabulary)` column in the resolution table below carries
exactly one value from this type per row. No other values are permitted. Column validity is
verified by this type declaration, not by proximity search.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one PrecedenceVocabulary value in the typed column.
Do NOT use free-form annotation in this column.

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED entry. Name blocking row.
State unblock condition.

**Resolution table:**

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied (PrecedenceVocabulary) |
|-------|--------------------|-----------------------|-----------|----------------|--------|------------------------------------------|
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
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `date = "2026-03-15"`. Do NOT write input name only. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Anti-pattern prohibition (C-21)**: The Binding column must carry the resolved value. Writing
`topic` without `= "payments-flow"` is a violation of the Binding Required format constraint.

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
structural elements. Generic entries fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows, Supplied populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value non-blank |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay: all roles COMPLETE or B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers: Gather/Bind/Execute/Verdict confirmed against Phase Label Schema |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-25 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; this row cites relay |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 precedes Tier 2 in Gather |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 table above resolution rows; 3 values defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 block above row 1; invocation-override + exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Required=YES Binding row; Format constraint cites key=value form; Binding column sample: [paste one cell] |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 PrecedenceVocabulary declaration; column populated for all [N] rows; sample values: [list 3] |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block between CM gate and Gather; [count] inputs listed by name |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Anti-pattern prohibition note present in Execute; Binding violation described |
| C-22 | "Precedence applied" column closed vocabulary declared | PASS / FAIL | PrecedenceVocabulary type declaration in Part 3; three values enumerated; "no other values" language present |
| C-23 | CLOSED ASSERTION terminates with closure declaration line | PASS / FAIL | CLOSED ASSERTION block final line: "Coverage Matrix is CLOSED for this invocation." confirmed |
| C-25 | "Precedence applied" column header cites PrecedenceVocabulary type | PASS / FAIL | Column header reads "Precedence applied (PrecedenceVocabulary)"; type declaration at Part 3 declares `type PrecedenceVocabulary = override \| default \| BLOCKED`; column is self-validating via type reference without proximity search |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (C-26: Closure Terminus as labeled structural mandate)

**Axis**: Lifecycle emphasis -- the CLOSED ASSERTION block gains a named structural sub-element:
`Closure Terminus`. The prompt declares this element by name before the trace runs. The CLOSED
ASSERTION instructions explicitly state: produce the Closure Terminus as the final line; its
absence is a structural violation; the Verdict C-23 row cites `Closure Terminus` by name. C-23
(terminus line present) remains satisfied; C-26 adds the mandate that the terminus is a named
prompt-instructed element, not an emergent closing statement.

**Hypothesis**: R6 V-05 CLOSED ASSERTION ends with "Coverage Matrix is CLOSED for this invocation."
-- the line is present because the instructions lead toward it, not because the prompt explicitly
names it as a required element. A model abbreviating the CLOSED ASSERTION might omit this line
without violating any stated rule. C-26 closes this gap: the Closure Terminus is a named required
element in the prompt, so its absence is identifiable as a specific structural violation. The
Verdict C-23 row cites the Closure Terminus labeled element -- providing a named citation target
that exists before the trace runs. Risk: adding a named sub-element label increases visual weight
in the CLOSED ASSERTION section. Mitigation: the label ("Closure Terminus") appears once, at the
final line position; it does not restructure the block, only names its terminal element.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation
  change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind,
  Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below. The CLOSED
  ASSERTION block must end with the Closure Terminus (see below). Then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage
Matrix and confirms it is available for this trace invocation. The Verdict compliance ledger cites
this block by name for C-20.

**Closure Terminus** (labeled structural mandate -- C-26): The CLOSED ASSERTION block must end
with the following exact line. The Closure Terminus is a named required element of this block.
Its absence means the CLOSED ASSERTION is structurally incomplete. The Verdict C-23 row cites
the Closure Terminus labeled element:

> Coverage Matrix is CLOSED for this invocation.

Produce the CLOSED ASSERTION block now:

> The following Required=YES inputs are confirmed available for this trace invocation:

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

**[Closure Terminus]** Coverage Matrix is CLOSED for this invocation.

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

**Bind Schema (declared before all resolution rows -- C-16, C-17, C-19 structural enforcement):**

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

**Part 3 -- Precedence Applied Vocabulary (closed; exactly three values permitted; no others):**

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one of these values in `Precedence applied`.
No other annotation values are permitted. Do NOT write free-form phrases.

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
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table. Example: `topic = "payments-flow"`. Do NOT write input name only. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked) |
| Binding (Anti-pattern) | VIOLATION | Do NOT write `InputName` alone. `topic` without the resolved value is a VIOLATION. Write `topic = "payments-flow"`. |

**Relay table:**

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
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

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific
structural elements. Generic entries fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay: roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-26 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; cites relay |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" present |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence; Evidence cites loci |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Part 1 table above resolution rows |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Part 2 block above row 1 |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Binding Required=YES; Format key=value; sample: [one Binding cell] |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Part 3 vocabulary; column populated; sample values: [3 cells] |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block; [count] inputs listed |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Relay Schema: Binding (Anti-pattern) row present; VIOLATION in Required column |
| C-22 | "Precedence applied" column closed vocabulary declared | PASS / FAIL | Part 3: three values declared; no-other-values language present |
| C-23 | CLOSED ASSERTION terminates with closure declaration line | PASS / FAIL | CLOSED ASSERTION final line: "[Closure Terminus] Coverage Matrix is CLOSED for this invocation." confirmed |
| C-26 | Closure Terminus is a labeled structural mandate in the prompt | PASS / FAIL | "Closure Terminus" named element declared before trace in Coverage Matrix gate instructions; "[Closure Terminus]" label present at final line of CLOSED ASSERTION; Verdict C-23 row cites Closure Terminus labeled element; absence identifiable as structural violation |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined: Output format + Phrasing register (C-24 + C-25)

**Axes**:
- Output format: Relay Schema split into two sub-tables -- Column Definitions (Required = YES) and
  Anti-Pattern Prohibition (Required = VIOLATION). VIOLATION in Required column is the structural
  isolation signal (C-24).
- Phrasing register: Bind Schema Part 3 declares named type `PrecedenceVocabulary`. Resolution
  table column header cites the type: `Precedence applied (PrecedenceVocabulary)`. Column is
  self-validating via type reference (C-25).

**Hypothesis**: C-24 and C-25 share the same structural principle: make validation self-contained
at the declaration site rather than requiring proximity search or Format cell parsing. C-24 does
this for the Relay Schema (Required=VIOLATION is the declaration site; no Format parsing needed).
C-25 does this for the Bind column (type name in column header is the declaration site; no proximity
search needed). Together they establish a "declaration at point-of-use" pattern across both Bind
and Execute. C-26 (Closure Terminus) remains at entry-state level (present, not yet a labeled
mandate) so V-04 can isolate the two-axis pattern. Risk: combining two axis changes tests whether
the mechanisms interact negatively. They don't share structural elements (Relay Schema vs Bind
column header), so independence is expected. Combined V-05 will add C-26.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation
  change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind,
  Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed
  to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input and confirms
availability. Verdict cites this block by name for C-20.

> The following Required=YES inputs are confirmed available (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

Coverage Matrix is CLOSED for this invocation.

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

**Bind Schema (declared before all resolution rows -- C-16, C-17, C-19, C-25):**

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule:**

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree,
> the invocation wins (runtime override). Exception: if the invocation value violates the spec's
> declared type or format contract, status is BLOCKED.

**Part 3 -- PrecedenceVocabulary (C-25: named type declaration):**

`type PrecedenceVocabulary = override | default | BLOCKED`

The `Precedence applied (PrecedenceVocabulary)` column in the resolution table carries exactly one
value from this type per row. To check column validity, look up PrecedenceVocabulary here -- no
proximity search required. No other values are permitted.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation wins |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Contract violation; invocation value rejected | Conflict? = YES; contract violation |

**Bind gate**: Any BLOCKED row halts Execute. Name blocking row. State unblock condition.

**Resolution table:**

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied (PrecedenceVocabulary) |
|-------|--------------------|-----------------------|-----------|----------------|--------|------------------------------------------|
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

**Relay Schema -- Column Definitions (C-18, C-24: Required = YES rows):**

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from Bind Resolved Value cell. Example: `topic = "payments-flow"`. |
| Status | YES | COMPLETE (all sections produced) / PARTIAL (B-NN gap present) |

**Relay Schema -- Anti-Pattern Prohibition (C-24: Required = VIOLATION):**

| Column | Required | Prohibition |
|--------|----------|-------------|
| Binding (Anti-pattern) | VIOLATION | Do NOT write input name alone. `topic` without the resolved value is a VIOLATION. Write `topic = "payments-flow"` (name = "value" form required). |

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

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific
structural elements.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay: roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-25 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows; this row cites relay |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" present |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; Evidence cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Part 1 table above resolution rows |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Part 2 block above row 1 |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Column Definitions; Binding Required=YES; sample: [one Binding cell] |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Part 3 PrecedenceVocabulary declaration; column populated; sample: [3 cells] |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block; [count] inputs listed |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Relay Schema Anti-Pattern Prohibition sub-table; Binding (Anti-pattern) row present |
| C-22 | "Precedence applied" column closed vocabulary declared | PASS / FAIL | PrecedenceVocabulary: three values; no-other-values language; type declaration present |
| C-23 | CLOSED ASSERTION terminates with closure declaration line | PASS / FAIL | CLOSED ASSERTION final line: "Coverage Matrix is CLOSED for this invocation." confirmed |
| C-24 | Anti-pattern row Required = VIOLATION (structurally independent) | PASS / FAIL | Relay Schema Anti-Pattern Prohibition sub-table: Required=VIOLATION for Binding (Anti-pattern); own sub-table under "Anti-Pattern Prohibition" header; independently citable without Prohibition cell |
| C-25 | "Precedence applied" column header cites PrecedenceVocabulary type | PASS / FAIL | Column header: "Precedence applied (PrecedenceVocabulary)"; `type PrecedenceVocabulary = override \| default \| BLOCKED` at Part 3; column self-validating via type reference |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined golden: Output format + Phrasing register + Lifecycle emphasis (C-24 + C-25 + C-26)

**Axes** (all three R6 excellence patterns as explicit structural requirements):

- Output format: Relay Schema split into Column Definitions (Required = YES) and Anti-Pattern
  Prohibition (Required = VIOLATION) sub-tables. VIOLATION in Required column is the structural
  isolation signal. Independently citable without Prohibition cell inspection (C-24).
- Phrasing register: Bind Schema Part 3 declares named type `PrecedenceVocabulary`. Column header
  cites type: `Precedence applied (PrecedenceVocabulary)`. Column self-validating via type reference,
  not proximity (C-25).
- Lifecycle emphasis: CLOSED ASSERTION block gains named sub-element `Closure Terminus`. Prompt
  declares it as a required element before the trace runs. Verdict C-23 cites labeled element (C-26).

**Hypothesis**: All three R6 excellence patterns target the same second-generation structural
principle: make verification self-contained at the declaration site. C-24: Required=VIOLATION is
the site (no Format parsing). C-25: column header is the site (no proximity search). C-26: Closure
Terminus label is the site (no emergent-depth inference). Together they complete the binding
evidence chain at every structural boundary: CLOSED ASSERTION (C-26) -> Bind column (C-25) ->
Execute relay (C-24). Each boundary is independently verifiable without backtracking or inference.
Risk: three structural additions are mutually independent (different sections of the prompt) so
interaction effects are minimal. The Verdict compliance ledger checks all 26 criteria; any labeled
element declared but absent produces a FAIL at a named citation target -- failure is visible and
specific.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation
  change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind,
  Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below. The CLOSED
  ASSERTION block must end with the Closure Terminus. Then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage
Matrix and confirms it is available for this trace invocation. The Verdict compliance ledger cites
this block by name for C-20.

**Closure Terminus** (labeled structural mandate -- C-26): The CLOSED ASSERTION block must end
with the following exact line. The Closure Terminus is a named required element of this block.
Its absence means the CLOSED ASSERTION is structurally incomplete. The Verdict C-23 row cites
the Closure Terminus labeled element. Do not append additional text after the Closure Terminus.

> Coverage Matrix is CLOSED for this invocation.

Produce the CLOSED ASSERTION block now:

> The following Required=YES inputs are confirmed available for this trace invocation:

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

**[Closure Terminus]** Coverage Matrix is CLOSED for this invocation.

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

**Bind Schema (declared before all resolution rows -- C-16, C-17, C-19, C-25):**

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

**Part 3 -- PrecedenceVocabulary (C-25: named type declaration):**

`type PrecedenceVocabulary = override | default | BLOCKED`

The `Precedence applied (PrecedenceVocabulary)` column in the resolution table carries exactly one
value from this type per row. Column validity is verified by this type declaration -- no proximity
search required. No other values are permitted in this column.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; contract violation |

Every resolution row carries exactly one PrecedenceVocabulary value. Do NOT use free-form annotation.

**Bind gate**: Any BLOCKED row halts Execute. Name blocking row. State unblock condition.

**Resolution table:**

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied (PrecedenceVocabulary) |
|-------|--------------------|-----------------------|-----------|----------------|--------|------------------------------------------|
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

**Relay Schema -- Column Definitions (C-18, C-24: Required = YES rows):**

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `date = "2026-03-15"`. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay Schema -- Anti-Pattern Prohibition (C-24: Required = VIOLATION):**

| Column | Required | Prohibition |
|--------|----------|-------------|
| Binding (Anti-pattern) | VIOLATION | Do NOT write the input name alone. `topic` without the resolved value is a VIOLATION of the Binding Required format. Write `topic = "payments-flow"` (name = "value" form). |

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
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema preamble: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-26 present as rows in this table |
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
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Column Definitions table present; Binding Required=YES; Format constraint cites key=value form with example; relay Binding column sample: [paste one cell] -- key=value confirmed |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 PrecedenceVocabulary declaration present; Precedence applied (PrecedenceVocabulary) column populated for all [N] rows; sample values: [list 3] -- override/default/BLOCKED confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present between Coverage Matrix gate and Gather; [count] Required=YES inputs listed by name |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Relay Schema Anti-Pattern Prohibition sub-table present; Binding (Anti-pattern) row; VIOLATION in Required column |
| C-22 | "Precedence applied" column closed vocabulary declared | PASS / FAIL | PrecedenceVocabulary type declaration at Part 3; three values enumerated; type syntax `type PrecedenceVocabulary = ...` present |
| C-23 | CLOSED ASSERTION terminates with closure declaration line | PASS / FAIL | CLOSED ASSERTION block final element: "[Closure Terminus] Coverage Matrix is CLOSED for this invocation." confirmed |
| C-24 | Anti-pattern row Required = VIOLATION (structurally independent) | PASS / FAIL | Relay Schema Anti-Pattern Prohibition sub-table: Binding (Anti-pattern) Required=VIOLATION in dedicated sub-table; independently citable; sub-table header "Anti-Pattern Prohibition" present |
| C-25 | "Precedence applied" column header cites PrecedenceVocabulary type | PASS / FAIL | Column header: "Precedence applied (PrecedenceVocabulary)"; `type PrecedenceVocabulary = override \| default \| BLOCKED` at Part 3; self-validating via type reference |
| C-26 | Closure Terminus is a labeled structural mandate in the prompt | PASS / FAIL | "Closure Terminus" declared by name before trace begins in Coverage Matrix gate; "[Closure Terminus]" label at CLOSED ASSERTION final line; Verdict C-23 cites Closure Terminus labeled element; absence is identifiable structural violation |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
