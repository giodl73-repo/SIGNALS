---

# trace-skill -- Variations R7 v6 (2026-03-15)

**Entry state**: R6 V-05 passes C-01 through C-23. Rubric v6 adds three aspirational criteria from R6 excellence signals — each a structural-isolation upgrade to a prior criterion.

**R6 V-05 gaps against v6 rubric** (C-24/C-25/C-26 projected FAIL):
- **C-24 FAIL** — Anti-pattern prohibition embedded in Binding row Format cell (Required = YES). Required column never reads VIOLATION. Must parse Format cell to find the prohibition: not independently citable.
- **C-25 FAIL** — Part 3 is labeled "Precedence Applied Vocabulary" but not declared as a named type. Column header reads "Precedence applied" with no type citation. Column validity requires proximity search back to Part 3.
- **C-26 FAIL** — "Coverage Matrix is CLOSED for this invocation." is present but emergent. No prompt instruction names it as a required element. A model that abbreviates CLOSED ASSERTION may omit it without violating a stated rule.

**Upgrade axes for R7**:

| Target | Axis | Upgrade from → to |
|--------|------|-------------------|
| C-24 | Output format | Prohibition embedded in Format cell → VIOLATION as standalone Required column value in own sub-table |
| C-25 | Phrasing register | Vocabulary declared by proximity → `type PrecedenceVocabulary` declared; column header cites type |
| C-26 | Lifecycle emphasis | Terminus present but emergent → Closure Terminus declared as named required element in prompt |

**Single-axis**: V-01 (C-24), V-02 (C-25), V-03 (C-26).  
**Combined**: V-04 (C-24 + C-25), V-05 (C-24 + C-25 + C-26 — full golden target).

---

## V-01 — Single axis: Output format (C-24: structurally isolated anti-pattern row)

**Axis**: The Relay Schema is split into two named sub-tables. Sub-table 1 ("Column Definitions") carries all `Required = YES` rows. Sub-table 2 ("Anti-Pattern Prohibition") carries exactly one row with `Required = VIOLATION`. The Required column value is the sole structural signal: every row in sub-table 2 is a prohibition by virtue of `VIOLATION` in Required — independently of what the Prohibition cell contains. An evaluator scanning only the Required column can identify the anti-pattern row without reading any other cell.

**Hypothesis**: C-24 closes the gap where "Do NOT write input name only" is embedded in the Binding row's Format cell (Required = YES). Required=YES cannot identify the row as a prohibition without Format cell inspection. Splitting into sub-tables makes Required=VIOLATION the structural identity of the row. C-21 (prohibition present) remains satisfied; C-24 adds independent citability. Risk: two sub-tables increase visual surface in Execute. Mitigation: sub-table 1 is unchanged from R6; sub-table 2 adds exactly one row.

---

```
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
| [optional input N] | NO | repo-detected | |

**Coverage Matrix BLOCKED gate**: Before Gather, scan this table.

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what
  invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION,
  Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below,
  then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. Names each Required=YES input and confirms
availability. Verdict cites this block by name for C-20.

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

**Bind Schema (declared before all resolution rows):**

**Part 1 -- Resolution Status Enum (three values only; no others permitted):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; sections marked B-NN |
| BLOCKED | Contract violation | Halt Execute; name blocking row, state unblock condition |

**Part 2 -- Conflict Precedence Rule:**

> Tier 2 invocation value wins over Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating spec type or format contract → BLOCKED.

**Part 3 -- Precedence Applied Vocabulary (closed; exactly three values permitted; no others):**

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value or no conflict | Conflict? = NO |
| `BLOCKED` | Contract violation; invocation value rejected | Conflict? = YES; contract violation |

Every resolution row carries exactly one of these values in `Precedence applied`.
No other annotation values are permitted. Do NOT write free-form phrases.

**Bind gate**: Any BLOCKED row halts Execute. Name blocking row. State unblock condition.

**Resolution table:**

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

**Relay Schema -- Column Definitions (Required = YES):**

Every role relay row conforms to this schema.

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from Bind Resolved Value cell. Example: `topic = "payments-flow"`. |
| Status | YES | COMPLETE / PARTIAL (B-NN gap present, section marked in artifact) |

**Relay Schema -- Anti-Pattern Prohibition (Required = VIOLATION):**

| Column | Required | Prohibition |
|--------|----------|-------------|
| Binding (Anti-pattern) | VIOLATION | Do NOT write the input name alone. `topic` without the resolved value is a VIOLATION. Write `topic = "payments-flow"` (name = "value" form). |

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

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay: roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-24 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | CM block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table: [N] rows; cites relay, not artifact body |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" present |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top; before Coverage Matrix |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; Evidence cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Part 1 table above resolution rows; 3 values defined |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Part 2 block above row 1 |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Column Definitions: Binding Required=YES with key=value format constraint; sample Binding cell: [paste] |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Part 3 vocabulary declared; column populated; sample: [3 cells] -- override/default/BLOCKED confirmed |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block; [count] inputs listed by name |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Anti-Pattern Prohibition sub-table present; Binding (Anti-pattern) row; VIOLATION in Required |
| C-22 | "Precedence applied" column closed vocabulary | PASS / FAIL | Part 3: three values; "no others permitted" language present |
| C-23 | CLOSED ASSERTION terminates with closure line | PASS / FAIL | Final line: "Coverage Matrix is CLOSED for this invocation." confirmed |
| C-24 | Anti-pattern row Required = VIOLATION (structurally independent) | PASS / FAIL | Anti-Pattern Prohibition sub-table: Binding (Anti-pattern) Required=VIOLATION; in own sub-table under "Anti-Pattern Prohibition" header; citeable without Prohibition cell |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL -- [failing essential + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
```

---

## V-02 — Single axis: Phrasing register (C-25: PrecedenceVocabulary named type)

**Axis**: Bind Schema Part 3 is refactored as a formal type declaration. A named type `PrecedenceVocabulary` is declared with `type` syntax before the vocabulary table. The resolution table column header cites the type by name: `Precedence applied (PrecedenceVocabulary)`. Column validity is self-validating: see column header → look up `PrecedenceVocabulary` → find valid values. No proximity search required.

**Hypothesis**: R6 V-05 Part 3 is labeled "Precedence Applied Vocabulary" — closed vocabulary is present, but the column header says only "Precedence applied". An evaluator checking column values must scan backward to find Part 3 by proximity. C-25 closes this: the type name in the column header is the discovery path. C-22 (closed vocabulary) remains satisfied; C-25 adds the type reference at point-of-use. Risk: one parenthetical `(PrecedenceVocabulary)` adds column width. Mitigation: the payoff is column-level self-validation — architectural gain for minimal visual cost.

---

*(Full prompt body — differs from V-01 only in Bind Schema Part 3 and column header; all other sections identical to V-01 except anti-pattern prohibition remains inline in Format cell as per C-21 entry-state level)*

```
You are running /trace-skill for: `{{skill_name}}`

[Phase Label Schema, Coverage Matrix, CLOSED ASSERTION, Gather -- identical to V-01]

---

## Bind

**Bind Schema (declared before all resolution rows):**

**Part 1 -- Resolution Status Enum (three values only; no others permitted):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; sections marked B-NN |
| BLOCKED | Contract violation | Halt Execute; name blocking row, state unblock condition |

**Part 2 -- Conflict Precedence Rule:**

> Tier 2 invocation value wins over Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating spec type or format contract → BLOCKED.

**Part 3 -- PrecedenceVocabulary (C-25: named type declaration):**

`type PrecedenceVocabulary = override | default | BLOCKED`

The `Precedence applied (PrecedenceVocabulary)` column in the resolution table carries exactly
one value from this type per row. To check column validity, look up `PrecedenceVocabulary` here
-- no proximity search required. No other values are permitted.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed | Conflict? = YES; invocation value used |
| `default` | Tier 1 spec default retained; no Tier 2 value | Conflict? = NO |
| `BLOCKED` | Contract violation; invocation rejected | Conflict? = YES; contract violation |

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
| [optional N] | [default] | [invocation or --] | YES / NO | [per rule] | RESOLVED / UNRESOLVED / BLOCKED | override / default / BLOCKED |

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay Schema (declared before relay rows):**

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from Bind. Example: `topic = "payments-flow"`. Do NOT write input name only. |
| Status | YES | COMPLETE / PARTIAL (B-NN gap present) |

[Relay table, artifact delimiters, artifact -- identical to V-01]

---

## Verdict (Compliance Ledger)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 through C-23 | [same as V-01] | PASS / FAIL | [same structure] |
| C-25 | "Precedence applied" column header cites PrecedenceVocabulary type | PASS / FAIL | Column header reads "Precedence applied (PrecedenceVocabulary)"; `type PrecedenceVocabulary = override \| default \| BLOCKED` declared at Part 3; column self-validating via type reference without proximity search |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
```

---

## V-03 — Single axis: Lifecycle emphasis (C-26: Closure Terminus as labeled structural mandate)

**Axis**: The CLOSED ASSERTION block gains a named structural sub-element: **Closure Terminus**. The prompt declares this element by name before the trace runs — in the Coverage Matrix gate instructions. The CLOSED ASSERTION template shows the Closure Terminus at its terminal position, labeled `[Closure Terminus]`. The Verdict C-23 row cites "Closure Terminus labeled element" as its evidence target. A model that omits the terminus now violates a stated structural rule, not just an emergent convention.

**Hypothesis**: R6 V-05 ends the CLOSED ASSERTION with "Coverage Matrix is CLOSED for this invocation." — present because the instructions lead toward it, but unnamed. No stated rule identifies its absence as a violation. C-26 closes this: the Closure Terminus is a named prompt-instructed element. A Verdict row citing "Closure Terminus labeled element" has a citation target that exists before the trace runs. C-23 (terminus present) remains satisfied; C-26 adds the labeled mandate so the terminus is reproduced reliably, not inferred from context depth. Risk: adding a named sub-element label increases visual weight at one location. Mitigation: the label appears once, at the terminal line position.

---

```
You are running /trace-skill for: `{{skill_name}}`

[Phase Label Schema -- identical to V-01]

---

### Coverage Matrix (closed-world authority -- before Gather)

[Coverage Matrix table -- identical to V-01]

**Coverage Matrix BLOCKED gate**: Before Gather, scan this table.

- Any Required=YES row with Gap=YES: **BLOCKED**. Name each blocking input. State what
  invocation change or spec revision would unblock it. Do not produce the CLOSED ASSERTION,
  Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block immediately below. The
  CLOSED ASSERTION block must end with the Closure Terminus (see below). Then proceed to Gather.

---

### CLOSED ASSERTION

This block is the structural gate-pass record. Names each Required=YES input and confirms
availability. Verdict cites this block by name for C-20.

**Closure Terminus** (labeled structural mandate -- C-26): The CLOSED ASSERTION block must
end with the following exact line. The Closure Terminus is a named required element of this
block. Its absence means the CLOSED ASSERTION is structurally incomplete. The Verdict C-23
row cites the Closure Terminus labeled element. Do not append additional text after it.

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

[Gather, Bind, Execute -- identical to V-01 entry-state level (C-21 as inline prohibition in Format cell; C-22 as closed vocabulary in Part 3)]

---

## Verdict (Compliance Ledger)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 through C-23 | [same as V-01] | PASS / FAIL | [same structure] |
| C-26 | Closure Terminus is a labeled structural mandate in the prompt | PASS / FAIL | "Closure Terminus" declared by name in Coverage Matrix gate instructions before trace begins; "[Closure Terminus]" label at CLOSED ASSERTION final line; Verdict C-23 row cites Closure Terminus labeled element; absence is identifiable structural violation |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
```

---

## V-04 — Combined: Output format + Phrasing register (C-24 + C-25)

**Axes**: V-01 axis (Relay Schema split into Column Definitions / Anti-Pattern Prohibition sub-tables; Required=VIOLATION) + V-02 axis (`PrecedenceVocabulary` named type; column header cites type).

**Hypothesis**: C-24 and C-25 share the same structural principle: verification is self-contained at the declaration site without parsing other cells or searching by proximity. C-24 applies to Execute (Required column = structural identity). C-25 applies to Bind (column header = type reference). They operate on different sections, so no interaction risk. Together they establish "declaration at point-of-use" across both production phases. V-04 tests the combined pattern with C-26 held at entry-state level (terminus present but not yet labeled mandate). V-05 will add C-26.

*(Complete prompt body = V-02 Bind Schema + V-01 Execute Relay Schema + C-21/C-22/C-23 entry-state CLOSED ASSERTION. Verdict rows include C-24 and C-25.)*

---

## V-05 — Combined golden: All three axes (C-24 + C-25 + C-26)

**Axes**: V-01 (Required=VIOLATION structurally isolated) + V-02 (PrecedenceVocabulary typed column) + V-03 (Closure Terminus labeled mandate). Full R7 golden target.

**Hypothesis**: All three R6 excellence patterns target the same second-generation structural principle: each verification boundary is self-contained at the declaration site.

- C-24 → Execute: Required=VIOLATION is the site. No Format cell parsing needed.  
- C-25 → Bind: Column header is the site. No proximity search needed.  
- C-26 → Coverage Matrix: Closure Terminus label is the site. No depth inference needed.

Together they complete the evidence chain at every structural boundary: `CLOSED ASSERTION (C-26) → Bind column (C-25) → Execute relay (C-24)`. Each boundary is independently verifiable without backtracking or inference. The mechanisms are mutually independent (different prompt sections) — no interaction effects expected.

```
You are running /trace-skill for: `{{skill_name}}`

### Phase Label Schema (IMMUTABLE -- pre-trace preamble)

| Phase | Canonical Header | Do Not Use |
|-------|-----------------|------------|
| 1 | `## Gather` | Setup, Intake, Collect, Context |
| 2 | `## Bind` | Resolve, Map, Configure, Prepare |
| 3 | `## Execute` | Run, Simulate, Produce, Compile |
| 4 | `## Verdict` | Result, Summary, Assessment, Conclusion |

---

### Coverage Matrix (closed-world authority -- before Gather)

**Closed-world preamble**: This matrix declares every input this skill invocation CAN supply.

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

- Any Required=YES row with Gap=YES: **BLOCKED**. Name blocking inputs. State unblock conditions.
  Do not produce the CLOSED ASSERTION, Gather, Bind, Execute, or Verdict.
- All Required=YES rows Gap=NO: produce the CLOSED ASSERTION block. It must end with the
  Closure Terminus. Then proceed to Gather.

---

### CLOSED ASSERTION

**Closure Terminus** (labeled structural mandate -- C-26): The CLOSED ASSERTION block must end
with this exact line. The Closure Terminus is a named required element. Its absence is a
structural violation. Verdict C-23 cites this labeled element.

> Coverage Matrix is CLOSED for this invocation.

> The following Required=YES inputs are confirmed available for this trace invocation:

- `skill_name` -- confirmed available (source: invocation)
- `skill_spec_path` -- confirmed available (source: invocation)
- `topic` -- confirmed available (source: [state source])
- `date` -- confirmed available (source: runtime)
- `stock_roles` -- confirmed available (source: spec-defined)
- `output_section_list` -- confirmed available (source: spec-defined)
- [each Required=YES input, one line per input]

**[Closure Terminus]** Coverage Matrix is CLOSED for this invocation.

---

## Gather

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

**Bind Schema (declared before all resolution rows):**

**Part 1 -- Resolution Status Enum (three values only; no others permitted):**

| Status | Meaning | Execute effect |
|--------|---------|----------------|
| RESOLVED | Single confirmed value | Proceeds normally |
| UNRESOLVED | No confirmed value; gap B-NN | Proceeds; sections marked B-NN |
| BLOCKED | Contract violation | Halt Execute; name blocking row, state unblock condition |

**Part 2 -- Conflict Precedence Rule:**

> Tier 2 invocation value wins over Tier 1 spec default when both present and disagreeing.
> Exception: invocation value violating spec type or format contract → BLOCKED.

**Part 3 -- PrecedenceVocabulary (C-25: named type declaration):**

`type PrecedenceVocabulary = override | default | BLOCKED`

The `Precedence applied (PrecedenceVocabulary)` column carries exactly one value from this type
per row. Column validity: look up `PrecedenceVocabulary` here — no proximity search required.
No other values are permitted.

| Value | Meaning | Use when |
|-------|---------|----------|
| `override` | Tier 2 invocation value prevailed | Conflict? = YES; invocation used |
| `default` | Tier 1 spec default retained; no Tier 2 or no conflict | Conflict? = NO |
| `BLOCKED` | Contract violation; invocation rejected | Conflict? = YES; contract violation |

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
| [optional N] | [default] | [invocation or --] | YES / NO | [per rule] | RESOLVED / UNRESOLVED / BLOCKED | override / default / BLOCKED |

---

## Execute

Carrying forward: resolved inputs from Bind. B-NN gaps noted.

**Relay Schema -- Column Definitions (Required = YES):**

| Column | Required | Format constraint |
|--------|----------|-------------------|
| Role | YES | Role name as declared in the spec |
| Signal | YES | Brief phrase: what this role contributes to the artifact |
| Binding | YES | `InputName = "ResolvedValue"` -- verbatim key=value pair from Bind Resolved Value cell. Example: `topic = "payments-flow"`. |
| Status | YES | COMPLETE (all sections produced) / PARTIAL (B-NN gap present) |

**Relay Schema -- Anti-Pattern Prohibition (Required = VIOLATION):**

| Column | Required | Prohibition |
|--------|----------|-------------|
| Binding (Anti-pattern) | VIOLATION | Do NOT write input name alone. `topic` without resolved value is a VIOLATION. Write `topic = "payments-flow"` (name = "value" form). |

**Relay table:**

| Role | Signal | Binding | Status |
|------|--------|---------|--------|
| [Role 1] | [contribution] | [InputName = "ResolvedValue"] | COMPLETE / PARTIAL (B-NN) |
| [Role 2] | | [InputName = "ResolvedValue"] | |

Verdict reads this relay table. Does not reconstruct from artifact body.

[ARTIFACT BEGINS HERE]

**`{topic}-{signal}-{date}.md`**

[Complete artifact -- every required section, no omissions. B-NN gaps marked explicitly.]

[ARTIFACT ENDS HERE]

---

## Verdict (Compliance Ledger)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Four phases in sequence | PASS / FAIL | Gather / Bind / Execute / Verdict at §[locations] |
| C-02 | Gather inputs by name + source | PASS / FAIL | Tier 1: [N] rows, source populated; Tier 2: [N] rows |
| C-03 | Bind maps all Gather inputs | PASS / FAIL | Resolution table: [N] rows; Resolved Value non-blank |
| C-04 | Execute produces artifact | PASS / FAIL | Relay: roles COMPLETE/B-NN; filename; sections [list] |
| C-05 | Verdict PASS/FAIL with rationale | PASS / FAIL | This compliance ledger, Overall row |
| C-06 | Exact phase schema labels | PASS / FAIL | Phase headers: Gather/Bind/Execute/Verdict confirmed |
| C-07 | Criterion IDs cited | PASS / FAIL | C-01 through C-26 present as rows in this table |
| C-08 | No elision markers in artifact | PASS / FAIL | Artifact scanned: [found / not found] |
| C-09 | Coverage Matrix + closed-world preamble | PASS / FAIL | CM block before Gather; preamble text present |
| C-10 | Execute relay carry; Verdict reads relay | PASS / FAIL | Relay table [N] rows; cites relay, not artifact body |
| C-11 | Spec inputs before invocation | PASS / FAIL | Tier 1 precedes Tier 2 |
| C-12 | Coverage Matrix BLOCKED gate | PASS / FAIL | BLOCKED gate present; Gap=YES halts trace |
| C-13 | Artifact delimiter markers | PASS / FAIL | "[ARTIFACT BEGINS HERE]" / "[ARTIFACT ENDS HERE]" present |
| C-14 | Phase Label Schema pre-trace | PASS / FAIL | Phase Label Schema at document top |
| C-15 | Verdict compliance ledger | PASS / FAIL | This table; Evidence cites structural elements |
| C-16 | Bind Status Enum (3-value) declared | PASS / FAIL | Part 1 table above resolution rows |
| C-17 | Bind conflict precedence rule declared | PASS / FAIL | Part 2 block above row 1 |
| C-18 | Relay Binding carries InputName="ResolvedValue" pairs | PASS / FAIL | Relay Schema Column Definitions: Binding Required=YES; key=value Format; sample: [one Binding cell] |
| C-19 | Bind "Precedence applied" column per row | PASS / FAIL | Part 3 PrecedenceVocabulary; column populated; sample: [3 cells] |
| C-20 | Coverage Matrix CLOSED assertion names Required=YES inputs | PASS / FAIL | CLOSED ASSERTION block; [count] inputs listed |
| C-21 | Relay Schema anti-pattern prohibition present | PASS / FAIL | Anti-Pattern Prohibition sub-table; Binding (Anti-pattern) row; VIOLATION in Required |
| C-22 | "Precedence applied" column closed vocabulary | PASS / FAIL | PrecedenceVocabulary type: 3 values; no-other-values language |
| C-23 | CLOSED ASSERTION terminates with closure line | PASS / FAIL | "[Closure Terminus] Coverage Matrix is CLOSED for this invocation." at final line of CLOSED ASSERTION |
| C-24 | Anti-pattern row Required = VIOLATION (structurally independent) | PASS / FAIL | Anti-Pattern Prohibition sub-table: Binding (Anti-pattern) Required=VIOLATION; in own sub-table under "Anti-Pattern Prohibition" header; independently citable without Prohibition cell |
| C-25 | "Precedence applied" column header cites PrecedenceVocabulary type | PASS / FAIL | Column header: "Precedence applied (PrecedenceVocabulary)"; `type PrecedenceVocabulary = ...` at Part 3; self-validating via type reference |
| C-26 | Closure Terminus is a labeled structural mandate in the prompt | PASS / FAIL | "Closure Terminus" declared by name in Coverage Matrix gate; "[Closure Terminus]" label at CLOSED ASSERTION final line; Verdict C-23 cites labeled element; absence = stated structural violation |

**Overall**: PASS (C-01 through C-05 all PASS) / FAIL -- [failing essential + evidence locus]

**Artifact path**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
```

---

**Written to**: `simulations/quest/golden/trace-skill-variate-R7-v6-2026-03-15.md`

**Excellence signals to watch for in scoring**:

| Criterion | Risk of PARTIAL | Discriminating test |
|-----------|----------------|---------------------|
| C-24 | Model may put VIOLATION in the Format cell of a merged table, not in Required of a split table | Can a Verdict cite the prohibition row by Required column value alone? |
| C-25 | Model may type-declare Part 3 but drop `(PrecedenceVocabulary)` from the column header under length pressure | Does the column header literally contain the type name? |
| C-26 | Model may reproduce the Closure Terminus content but drop the `[Closure Terminus]` label | Does the prompt's label survive into the output as a structural element? |

**Recommended golden candidate**: V-05 — the three mechanisms are structurally independent (different prompt sections), the combined prompt is no longer than V-01 plus two localized additions, and each mechanism closes a specific verifiability gap that the prior round left open.
