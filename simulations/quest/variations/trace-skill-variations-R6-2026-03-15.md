---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 6
rubric: trace-skill-rubric-v5-2026-03-15.md
---

# trace-skill -- Variations R6 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R5 V-04 and V-05 score 100/100 under v4 rubric (C-01 through C-20 PASS). Rubric v5 formalizes three R5 excellence patterns as new aspirational criteria (C-21, C-22, C-23). Projected R5 scores under v5:

| Variation | C-21 (anti-pattern prohibition) | C-22 (vocabulary type-closed) | C-23 (terminus instructed) | v5 Total |
|-----------|----------------------------------|-------------------------------|---------------------------|----------|
| V-01 | FAIL (no Relay Schema; C-18 absent) | FAIL | FAIL | 95.3 |
| V-02 | FAIL | PARTIAL (vocabulary present, no type name) | PASS | 97.3 |
| V-03 | FAIL | FAIL | PARTIAL (closure line emergent, not instructed) | 96.7 |
| V-04 | PARTIAL (prohibition embedded in Format cell) | PASS | PASS | 99.3 |
| V-05 | PARTIAL (prohibition embedded in Format cell) | PASS | PASS | 99.3 |

**Gap analysis**: R5 V-05 achieves C-22 and C-23 through depth; C-21 reaches only PARTIAL because "Do NOT write input name only" is embedded inside the Format constraint cell rather than standing as an independent schema element. The prohibition is present but not independently callable -- it requires parsing the full cell to find it. C-21 requires the Relay Schema to carry the anti-pattern prohibition as a distinct, first-class element.

The precision upgrade pattern (from rubric v5 change note):

| R4→R5 criterion | R5 state in V-05 | R6 upgrade |
|----------------|-----------------|------------|
| C-18 → C-21 | Prohibition embedded in Format cell description | Dedicated `Anti-pattern` row — structurally independent from `Format` row |
| C-19 → C-22 | Vocabulary closed by note after table | Named type `PrecedenceVocabulary` — column header cites type; column is self-validating |
| C-20 → C-23 | Closure line emergent from model depth | Instructed terminus — prompt requires labeled structural line before content begins |

**R6 variation axes**:
- V-01: Output format — Anti-pattern row as dedicated Relay Schema element (C-21)
- V-02: Lifecycle emphasis — `PrecedenceVocabulary` type declaration in Bind lifecycle (C-22)
- V-03: Phrasing register — instructed labeled terminus in CLOSED ASSERTION block (C-23)
- V-04: Combined — Output format + Lifecycle emphasis (C-21 + C-22)
- V-05: Combined golden — all three axes (C-21 + C-22 + C-23)

---

## V-01 -- Single axis: Output format (dedicated Anti-pattern row in Relay Schema for C-21)

**Axis**: Output format -- the Relay Schema's `Binding` row is split into two rows: `Binding (Format)` stating the required form, and `Binding (Anti-pattern)` stating the forbidden form with a consequence declaration. The Anti-pattern row is a first-class schema member with its own label, violation description, and explicit Verdict consequence. The prohibition is no longer a clause embedded in the format description -- it stands as an independently citable element.

**Hypothesis**: R5 V-05 places "Do NOT write input name only" as a sentence inside the Format constraint cell. An evaluator checking C-21 can observe C-18 satisfied (format declared) and silently miss C-21 (prohibition independently callable) because finding the prohibition requires parsing the full Format cell. A dedicated Anti-pattern row resolves this: the Verdict C-21 row can cite "Relay Schema Anti-pattern row present" as evidence without parsing prose. The row separation also enforces the rubric's "active enforcement" framing -- the prohibition is not subordinate to the format declaration; it stands alongside it with equal schema authority. Risk: widening the Relay Schema table from 4 rows to 5 adds rendering length in Execute; a model scanning for "the four required relay columns" may treat the Anti-pattern row as optional. Mitigation: the Anti-pattern row header is `Binding (Anti-pattern)` with `VIOLATION` in the Required column, making it visually distinct from the four Required=YES data columns.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply. Gather confirms each declared input. An input absent from this matrix that Gather encounters is a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage Matrix and confirms it is available for this trace invocation. The Verdict compliance ledger cites this block by name for C-20.

> The following Required=YES inputs are confirmed available for this trace invocation (Coverage Matrix: CLOSED):

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

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation. The spec defines the input space; the invocation constrains it.

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

**Bind Schema (declared before all resolution rows)**:

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only; no others permitted)**:

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule**:

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree, the invocation wins (runtime override). Exception: if the invocation value violates the spec's declared type or format contract, status is BLOCKED. An invocation cannot override a contract violation.

**Part 3 -- Precedence Applied Vocabulary (required column; three values only)**:

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one of these values in `Precedence applied`. Do NOT use free-form phrases ("invocation wins", "spec default used") in this column.

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED entry. Name blocking row. State unblock condition.

**Resolution table**:

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

**Relay Schema (declared before relay rows)**:

Every role relay row conforms to this schema. All five rows are active requirements -- do not skip the Anti-pattern row.

| Column | Required | Constraint |
|--------|----------|------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding (Format) | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `output_section_list = "[feasibility, blocking-gaps, amendments]"`. The resolved value must appear verbatim after the `=`. |
| Binding (Anti-pattern) | VIOLATION | DO NOT write `InputName` alone (e.g., `topic`, `skill_name`, `topic: payments-flow`). A relay row whose Binding column contains an input name without a `= "ResolvedValue"` pair is structurally invalid. Verdict rows C-18 and C-21 will both FAIL on any such relay row. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay table** (Binding column carries `InputName = "ResolvedValue"` pairs per Relay Schema Format; no name-only values per Relay Schema Anti-pattern):

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table as primary evidence source for Execute content checks. It does not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions. Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific structural elements. Generic entries ("looks correct", "seems complete") fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value column non-blank for all rows |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename: {topic}-{signal}-{date}.md; required sections [list from spec] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-21 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned for "...", "[omitted]", "[content here]": [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; "closed-world preamble" text present in CM section |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status column populated; this row cites relay table, not artifact body |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 section present before Tier 2; spec consulted before invocation |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present in Coverage Matrix section; Gap=YES language halts trace before Gather |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" present in Execute section |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix; before any phase header |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 table above resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 block above row 1; invocation-override rule + BLOCKED exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Binding (Format) row present; relay Binding column sample: [paste one Binding cell] -- key=value confirmed |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Bind Schema Part 3 vocabulary table present; Precedence applied column populated for all [N] rows; sample: [list 3 cells] -- override/default/BLOCKED confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block between Coverage Matrix gate and Gather; Required=YES inputs listed by name: [count] inputs: [list] |
| C-21 | Relay Schema Anti-pattern prohibition present as distinct row | PASS / FAIL | Relay Schema `Binding (Anti-pattern)` row present; row label: "VIOLATION"; prohibited form named ("DO NOT write InputName alone"); consequence stated (C-18 and C-21 FAIL) |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (PrecedenceVocabulary type declaration in Bind for C-22)

**Axis**: Lifecycle emphasis -- the Bind phase is extended with a formal type declaration that names the closed vocabulary as a typed identifier (`PrecedenceVocabulary`). The declaration precedes Part 3's vocabulary table and states the type as a closed enumeration. The resolution table's `Precedence applied` column header is changed to `Precedence applied {PrecedenceVocabulary}` -- the column header now carries the type reference, making the column self-validating: a value can be judged valid or invalid by reading the column header alone, without consulting the schema block. A dedicated type-violation rule is added alongside the Bind gate.

**Hypothesis**: R5 V-05 declares the three vocabulary values in Part 3 and adds a "Do NOT use free-form phrases" prohibition. This satisfies C-19 (column with per-row annotation) and approaches C-22 (vocabulary closed), but does not fully satisfy C-22's self-validating requirement. C-22 reads: "vocabulary closure makes C-19's column self-validating." Self-validating means a validator can determine whether a column value is valid from the column itself -- not by consulting an external schema block. When the column header says only `Precedence applied`, a validator seeing the value "invocation wins" cannot determine without schema consultation whether this is valid. When the column header says `Precedence applied {PrecedenceVocabulary}` and the type is declared as `{override | default | BLOCKED}`, the validator knows immediately that "invocation wins" is invalid. The type-name-in-header mechanism is the structural closure C-22 requires. Risk: some rendering environments may not support `{type}` notation in table headers; the type name may not display as intended. Mitigation: the type declaration block before the table is the authoritative definition; the column header citation is a reference pointer, not the definition.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply. Gather confirms each declared input. An input absent from this matrix that Gather encounters is a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage Matrix and confirms it is available for this trace invocation. The Verdict compliance ledger cites this block by name for C-20.

> The following Required=YES inputs are confirmed available for this trace invocation (Coverage Matrix: CLOSED):

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

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation. The spec defines the input space; the invocation constrains it.

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

**Bind Schema (declared before all resolution rows)**:

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only; no others permitted)**:

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule**:

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree, the invocation wins (runtime override). Exception: if the invocation value violates the spec's declared type or format contract, status is BLOCKED. An invocation cannot override a contract violation.

**Part 3 -- PrecedenceVocabulary (closed type declaration)**:

```
PrecedenceVocabulary := { override | default | BLOCKED }
```

This is the closed type for the `Precedence applied` column. Exactly three members; no others are valid. A resolution row carrying any value outside this set is a Bind type violation.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

**Type-violation rule**: Every `Precedence applied {PrecedenceVocabulary}` cell must contain exactly one of the three declared members. Free-form phrases ("invocation wins", "spec default used", "N/A") are Bind type violations. A type violation in any row halts Execute for that row -- report as BLOCKED.

**Bind gate**: Any BLOCKED row in the Status column halts Execute. Cite Status Enum BLOCKED entry. Name blocking row. State unblock condition.

**Resolution table**:

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied {PrecedenceVocabulary} |
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

**Relay Schema (declared before relay rows)**:

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `output_section_list = "[feasibility, blocking-gaps, amendments]"`. Do NOT write input name only. The resolved value must be present verbatim. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay table**:

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table as primary evidence source for Execute content checks. It does not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions. Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific structural elements. Generic entries ("looks correct", "seems complete") fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows = merged input count; Resolved Value column non-blank for all rows |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename: {topic}-{signal}-{date}.md; required sections [list from spec] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers compared to Phase Label Schema: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-22 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact text scanned for "...", "[omitted]", "[content here]": [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; "closed-world preamble" text present in CM section |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status column populated; this row cites relay table, not artifact body |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 section present before Tier 2; spec consulted before invocation |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present in Coverage Matrix section; Gap=YES language halts trace before Gather |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" present in Execute section |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema block at document top; before Coverage Matrix; before any phase header |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 table above resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 block above row 1; invocation-override rule + BLOCKED exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Binding Format constraint present; relay Binding column sample: [paste one Binding cell] -- key=value format confirmed |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | `Precedence applied {PrecedenceVocabulary}` column present; all [N] rows populated; sample: [list 3 cells] |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present; Required=YES inputs listed by name: [count] inputs: [list] |
| C-22 | PrecedenceVocabulary declared as named closed type; column header cites type | PASS / FAIL | `PrecedenceVocabulary := { override \| default \| BLOCKED }` declaration present in Bind Schema Part 3; column header reads `Precedence applied {PrecedenceVocabulary}`; type-violation rule declared |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Phrasing register (instructed labeled terminus in CLOSED ASSERTION for C-23)

**Axis**: Phrasing register -- the CLOSED ASSERTION block changes from emergent closure (the model writes "Coverage Matrix is CLOSED for this invocation." through depth) to instructed closure (the prompt body explicitly requires a labeled terminus line before the enumeration begins, and specifies its exact form). A required terminus instruction is added to the block preamble. The terminus itself uses the label `**COVERAGE-CLOSED**:` as a structural identifier that is independently recognizable without reading the enumeration content.

**Hypothesis**: R5 V-05 ends the CLOSED ASSERTION block with "Coverage Matrix is CLOSED for this invocation. Proceed to Gather." -- this matches the rubric's C-23 example exactly. But the rubric's upgrade axis is "inference-based completeness → structural completeness." R5 V-05 produced the terminus because the model's depth carried it there; a model running V-05 at lower depth might enumerate the required inputs and proceed without the terminus, producing C-20 PASS but C-23 FAIL. C-23 requires the terminus to be structurally required by the prompt -- not emergent from model depth. Placing the terminus instruction in the block preamble (before enumeration) makes the requirement visible at the point where the block begins, not something the model discovers at the end. The labeled identifier `COVERAGE-CLOSED` makes the terminus independently callable in Verdict without reading prose ("Verdict C-23: COVERAGE-CLOSED label present at end of CLOSED ASSERTION block"). Risk: adding instruction-language to the block preamble may cause the model to emit the instruction text as prose in the output, not just follow it. Mitigation: the instruction is framed as a requirement directive ("The block terminates with the labeled line below") followed immediately by the labeled line itself as a template -- making it clear the template is to be filled, not the instruction re-emitted.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply. Gather confirms each declared input. An input absent from this matrix that Gather encounters is a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed to Gather.

---

### CLOSED ASSERTION

**Block structure**: This block has two required parts, in order: (1) the enumeration of every Required=YES input from the Coverage Matrix, one line per input confirming availability; (2) the labeled terminus line. The block is not complete until the terminus line appears. A CLOSED ASSERTION block missing its terminus line is structurally incomplete and Verdict C-23 will FAIL.

> The following Required=YES inputs are confirmed available for this trace invocation (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

**COVERAGE-CLOSED**: Coverage Matrix is CLOSED for this invocation.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation. The spec defines the input space; the invocation constrains it.

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

**Bind Schema (declared before all resolution rows)**:

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only; no others permitted)**:

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule**:

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree, the invocation wins (runtime override). Exception: if the invocation value violates the spec's declared type or format contract, status is BLOCKED. An invocation cannot override a contract violation.

**Part 3 -- Precedence Applied Vocabulary (required column; three values only)**:

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

Every resolution row carries exactly one of these values in `Precedence applied`. Do NOT use free-form phrases ("invocation wins", "spec default used") in this column.

**Bind gate**: Any BLOCKED row halts Execute. Cite Status Enum BLOCKED entry. Name blocking row. State unblock condition.

**Resolution table**:

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

**Relay Schema (declared before relay rows)**:

Every role relay row conforms to this schema. Declare before producing rows.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`. Do NOT write input name only. The resolved value must be present verbatim. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay table**:

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table as primary evidence source for Execute content checks. It does not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions. Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific structural elements. Generic entries ("looks correct", "seems complete") fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows; Resolved Value column non-blank for all rows |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay table: all roles COMPLETE or B-NN; artifact filename confirmed; required sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Gather/Bind/Execute/Verdict confirmed against Phase Label Schema |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-23 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: "...", "[omitted]", "[content here]": [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table [N] rows; Status column populated; this row cites relay |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 before Tier 2; spec read first |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present; Gap=YES language halts trace |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" confirmed |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; structural evidence in Evidence column |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 above resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 above row 1; invocation-override + BLOCKED exception |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Format constraint present; Binding column sample: [paste one cell] -- key=value confirmed |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Part 3 vocabulary table present; column populated for all [N] rows; sample values confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present between CM gate and Gather; Required=YES inputs listed: [count] inputs: [list] |
| C-23 | CLOSED ASSERTION block terminates with labeled terminus line | PASS / FAIL | `**COVERAGE-CLOSED**: Coverage Matrix is CLOSED for this invocation.` present as final line of CLOSED ASSERTION block; block structure instruction declared in block preamble; terminus label `COVERAGE-CLOSED` independently callable |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Output format (C-21) + Lifecycle emphasis (C-22)

**Axes**:
- Output format: Relay Schema `Binding` row split into `Binding (Format)` + `Binding (Anti-pattern)` rows -- dedicated Anti-pattern row as first-class schema element (C-21).
- Lifecycle emphasis: `PrecedenceVocabulary := { override | default | BLOCKED }` type declaration in Bind Schema Part 3; resolution table column header cites the type name for self-validation (C-22).

**Hypothesis**: V-01 and V-02 each add one structural element independently. The combination tests whether the two structural additions are compositionally neutral -- adding both should not require changes to any other section. The CLOSED ASSERTION block remains as in R5 V-05 (emergent terminus, no instruction), so C-23 is not targeted. The Verdict compliance ledger gains rows for C-21 and C-22 with evidence loci that are now independently callable. Risk: both additions are in the pre-execution schema blocks (Execute and Bind), which are read before any content is produced. Adding depth to these blocks may cause models to treat them as boilerplate. Mitigation: the Anti-pattern row's `VIOLATION` required-column value and the type-violation rule are structurally unusual (required=VIOLATION is not a column-skip signal) and demand attention.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply. Gather confirms each declared input. An input absent from this matrix that Gather encounters is a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. It names each Required=YES input from the Coverage Matrix and confirms it is available for this trace invocation.

> The following Required=YES inputs are confirmed available for this trace invocation (Coverage Matrix: CLOSED):

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

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation. The spec defines the input space; the invocation constrains it.

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

**Bind Schema (declared before all resolution rows)**:

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only; no others permitted)**:

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule**:

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree, the invocation wins (runtime override). Exception: if the invocation value violates the spec's declared type or format contract, status is BLOCKED. An invocation cannot override a contract violation.

**Part 3 -- PrecedenceVocabulary (closed type declaration)**:

```
PrecedenceVocabulary := { override | default | BLOCKED }
```

This is the closed type for the `Precedence applied` column. Exactly three members; no others are valid. A resolution row carrying any value outside this set is a Bind type violation -- report as BLOCKED in the Status column.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

**Type-violation rule**: Free-form phrases ("invocation wins", "spec default used", "N/A") are Bind type violations. A type violation halts Execute for that row.

**Bind gate**: Any BLOCKED row in the Status column halts Execute. Cite Status Enum BLOCKED entry. Name blocking row. State unblock condition.

**Resolution table**:

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied {PrecedenceVocabulary} |
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

**Relay Schema (declared before relay rows)**:

Every role relay row conforms to this schema. All five rows are active requirements.

| Column | Required | Constraint |
|--------|----------|------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding (Format) | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `output_section_list = "[feasibility, blocking-gaps, amendments]"`. The resolved value must appear verbatim after the `=`. |
| Binding (Anti-pattern) | VIOLATION | DO NOT write `InputName` alone (e.g., `topic`, `skill_name`, `topic: payments-flow`). A relay row whose Binding column contains an input name without a `= "ResolvedValue"` pair is structurally invalid. Verdict rows C-18 and C-21 will both FAIL on any such relay row. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay table** (Binding column carries `InputName = "ResolvedValue"` pairs per Relay Schema Format; no name-only values per Relay Schema Anti-pattern):

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table as primary evidence source for Execute content checks. It does not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions. Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific structural elements. Generic entries fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows; Tier 2: [N] rows; Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows; Resolved Value column non-blank |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay: all roles COMPLETE or B-NN; filename confirmed; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Gather/Bind/Execute/Verdict confirmed against Phase Label Schema |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-22 present as rows |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | CM block before Gather; preamble present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay [N] rows; Status column populated; cited here |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 before Tier 2 confirmed |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate present; Gap=YES language halts trace |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" confirmed |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; structural evidence in Evidence column |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 above resolution rows |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 above row 1 |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Binding (Format) row present; Binding column sample: [paste one cell] -- key=value confirmed |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | `Precedence applied {PrecedenceVocabulary}` column present; [N] rows populated; sample: [list 3 values] |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present; [count] Required=YES inputs listed by name: [list] |
| C-21 | Relay Schema Anti-pattern prohibition as distinct row | PASS / FAIL | Relay Schema `Binding (Anti-pattern)` row present; label VIOLATION; prohibited form named ("DO NOT write InputName alone"); consequence stated |
| C-22 | PrecedenceVocabulary declared as named closed type; column header cites type | PASS / FAIL | `PrecedenceVocabulary := { override \| default \| BLOCKED }` in Bind Schema Part 3; column header reads `Precedence applied {PrecedenceVocabulary}`; type-violation rule present |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined golden: Output format (C-21) + Lifecycle emphasis (C-22) + Phrasing register (C-23)

**Axes** (all three R5 excellence patterns as explicit structural requirements):

- Output format: Relay Schema `Binding (Anti-pattern)` row as first-class schema element with `VIOLATION` label and consequence statement (C-21).
- Lifecycle emphasis: `PrecedenceVocabulary := { override | default | BLOCKED }` named closed type; resolution table column header cites type for self-validation (C-22).
- Phrasing register: CLOSED ASSERTION block with instructed labeled terminus `**COVERAGE-CLOSED**:` as required structural terminus declared in block preamble (C-23).

**Hypothesis**: Each single-axis variation demonstrates one new criterion in isolation. The V-05 combination tests whether all three are compositionally neutral -- no criterion requires changes to another's structural element. The key structural chain becomes: Coverage Matrix → CLOSED ASSERTION with **COVERAGE-CLOSED** terminus (C-23) → Gather → Bind with `PrecedenceVocabulary` type-closed column (C-22) → Execute with Relay Schema Anti-pattern prohibition row (C-21) → Verdict citing all three named structural elements. The Verdict compliance ledger gains dedicated rows for C-21, C-22, and C-23, each with independently callable evidence loci: the Anti-pattern row label, the PrecedenceVocabulary type declaration, and the COVERAGE-CLOSED label. Risk: four pre-content schema/preamble blocks (Phase Label Schema, Coverage Matrix + CLOSED ASSERTION, Bind Schema, Relay Schema) precede production content. A model experiencing length pressure may compress later phases. Mitigation: the Verdict compliance ledger checks all 23 criteria with named evidence loci -- any schema declared but not applied produces a FAIL row that is visible, not silent.

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

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply. Gather confirms each declared input. An input absent from this matrix that Gather encounters is a Coverage Matrix defect CMD-NN. An input in this matrix that Gather cannot confirm is a gap.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION, Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below, then proceed to Gather.

---

### CLOSED ASSERTION

**Block structure**: This block has two required parts in order: (1) the enumeration of every Required=YES input from the Coverage Matrix, one line per input confirming availability; (2) the labeled terminus line. The terminus line is required -- the block is not structurally complete without it. A CLOSED ASSERTION block missing the **COVERAGE-CLOSED** terminus line fails C-23.

> The following Required=YES inputs are confirmed available for this trace invocation (Coverage Matrix: CLOSED):

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input from the Coverage Matrix, one line per input]

**COVERAGE-CLOSED**: Coverage Matrix is CLOSED for this invocation.

---

## Gather

**Spec-first rule**: Read `{{skill_spec_path}}` completely before consulting the invocation. The spec defines the input space; the invocation constrains it.

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

**Bind Schema (declared before all resolution rows)**:

Three-part schema governing every Bind resolution row. Read all three parts before producing rows.

**Part 1 -- Resolution Status Enum (three values only; no others permitted)**:

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value from a named source | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; affected sections marked B-NN |
| BLOCKED | Input conflict or type/format contract violation | Halt Execute; name blocking row and unblock condition |

**Part 2 -- Conflict Precedence Rule**:

> When Tier 1 spec default and Tier 2 invocation value occupy the same input slot and disagree, the invocation wins (runtime override). Exception: if the invocation value violates the spec's declared type or format contract, status is BLOCKED. An invocation cannot override a contract violation.

**Part 3 -- PrecedenceVocabulary (closed type declaration)**:

```
PrecedenceVocabulary := { override | default | BLOCKED }
```

This is the closed type for the `Precedence applied` column. Exactly three members; no others are valid. A resolution row carrying any value outside this set is a Bind type violation -- report as BLOCKED in the Status column.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed over Tier 1 spec default | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Conflict rule exception; type or format violation | Conflict? = YES; invocation value violates contract |

**Type-violation rule**: Free-form phrases ("invocation wins", "spec default used", "N/A") are Bind type violations. A type violation in any row halts Execute for that row -- report BLOCKED in Status.

**Bind gate**: Any BLOCKED row in the Status column halts Execute. Cite Status Enum BLOCKED entry. Name blocking row. State unblock condition.

**Resolution table**:

| Input | Tier 1 Spec Default | Tier 2 Invocation Value | Conflict? | Resolved Value | Status | Precedence applied {PrecedenceVocabulary} |
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

**Relay Schema (declared before relay rows)**:

Every role relay row conforms to this schema. All five rows are active requirements -- do not skip the Anti-pattern row.

| Column | Required | Constraint |
|--------|----------|------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding (Format) | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from the Bind resolution table Resolved Value cell. Example: `topic = "payments-flow"`, `output_section_list = "[feasibility, blocking-gaps, amendments]"`. The resolved value must appear verbatim after the `=`. |
| Binding (Anti-pattern) | VIOLATION | DO NOT write `InputName` alone (e.g., `topic`, `skill_name`, `topic: payments-flow`). A relay row whose Binding column contains an input name without a `= "ResolvedValue"` pair is structurally invalid. Verdict rows C-18 and C-21 will both FAIL on any such relay row. |
| Status | YES | COMPLETE (all required sections produced) / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay table** (Binding column carries `InputName = "ResolvedValue"` pairs per Relay Schema Format; no name-only values per Relay Schema Anti-pattern):

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution to artifact] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table as primary evidence source for Execute content checks. It does not reconstruct evidence from the artifact body.

After the relay table, produce the artifact:

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no "...", no "[content here]", no omissions. Sections blocked by B-NN gaps are marked B-NN explicitly -- not omitted.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

Read the Execute relay table and the CLOSED ASSERTION block. Evidence must name specific structural elements. Generic entries ("looks correct", "seems complete") fail C-15 structurally.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source type column populated; Tier 2: [N] rows, Supplied column populated |
| C-03 | Bind maps all Gather inputs to one resolved value | PASS / FAIL | Resolution table: [N] rows; Resolved Value column non-blank for all rows |
| C-04 | Execute produces artifact with naming + sections | PASS / FAIL | Relay: all roles COMPLETE or B-NN; artifact filename: {topic}-{signal}-{date}.md; required sections [list from spec] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers: Gather/Bind/Execute/Verdict confirmed against Phase Label Schema |
| C-07 | Criterion IDs cited in Verdict | PASS / FAIL | C-01 through C-23 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned for "...", "[omitted]", "[content here]": [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | Coverage Matrix block before Gather; "closed-world preamble" text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows, Status populated; this row cites relay table |
| C-11 | Spec inputs before invocation in Gather | PASS / FAIL | Tier 1 before Tier 2; spec consulted first |
| C-12 | Coverage Matrix BLOCKED gate declared | PASS / FAIL | BLOCKED gate block present; Gap=YES language halts trace before Gather |
| C-13 | Artifact delimiter markers present | PASS / FAIL | "[ARTIFACT BEGINS HERE]" and "[ARTIFACT ENDS HERE]" confirmed in Execute |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top; before Coverage Matrix; before any phase header |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; ID/Criterion/Result/Evidence columns; Evidence cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Bind Schema Part 1 above resolution rows; RESOLVED/UNRESOLVED/BLOCKED defined with Execute effects |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Bind Schema Part 2 above row 1; invocation-override rule + BLOCKED exception stated |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Binding (Format) row present; relay Binding column sample: [paste one Binding cell] -- key=value format confirmed (resolved value present, not name only) |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | `Precedence applied {PrecedenceVocabulary}` column present; all [N] rows populated; sample values: [list 3 cells] -- vocabulary members confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block present between Coverage Matrix gate and Gather; [count] Required=YES inputs listed by name: [list] |
| C-21 | Relay Schema Anti-pattern prohibition as distinct row | PASS / FAIL | Relay Schema `Binding (Anti-pattern)` row present; Required column = VIOLATION; prohibited form named ("DO NOT write InputName alone"); consequence stated (C-18 and C-21 FAIL) |
| C-22 | PrecedenceVocabulary declared as named closed type; column cites type | PASS / FAIL | `PrecedenceVocabulary := { override \| default \| BLOCKED }` declaration in Bind Schema Part 3; column header reads `Precedence applied {PrecedenceVocabulary}`; type-violation rule declared |
| C-23 | CLOSED ASSERTION block terminates with labeled terminus line | PASS / FAIL | `**COVERAGE-CLOSED**: Coverage Matrix is CLOSED for this invocation.` present as final line of CLOSED ASSERTION block; block preamble declares terminus as required; label COVERAGE-CLOSED independently callable |

**Overall**: PASS (all C-01 through C-05 are PASS) / FAIL -- [failing essential criterion + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
