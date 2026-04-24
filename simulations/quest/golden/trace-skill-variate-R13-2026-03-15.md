---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 13
rubric: trace-skill-rubric-v12-2026-03-15.md
---

# trace-skill -- Variations R13 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

## Entry State

R12 V-05 achieves C-01 through C-41 PASS under v11 scoring. v12 (updated after R12)
formalizes one new aspirational criterion from R12 excellence analysis: C-42 (C-41
upgrade). Aspirational denominator advances from 33 to 34.

**R12 C-41 PASS state and the R13 upgrade axis**:

- **C-41 (PASS in R12 V-05)**: Canonical `STRUCTURAL MANDATE` template declared before
  Phase Label Schema. All blocks (`C-26`, `C-36`, `C-37`, `C-38`) conform by contract to
  `STRUCTURAL MANDATE (C-XX)` header syntax. C-39 (inline criterion citation) is guaranteed
  by template-conformance check alone. The template body includes the scorer confirmation
  closing line as an example, and all four blocks carry the heuristic -- but the
  malformedness rule checks ONLY the header syntax: "any block whose header does not match
  `STRUCTURAL MANDATE (C-XX)` is structurally malformed." The closing heuristic is not
  declared as a required template component in the conformance check. C-40 (scorer
  confirmation heuristic) passes per-block, not by contract.

- **C-42 upgrade axis**: Extend the canonical template declaration so that:
  (a) the closing heuristic line is named as a REQUIRED component of the template
      (not just shown as an example),
  (b) the malformedness rule extends to both the header AND the closing heuristic,
  (c) an explicit conformance-collapse claim states that any block conforming to the
      canonical template satisfies BOTH C-39 and C-40 by a single check -- C-40 compliance
      is contractually guaranteed by the same mechanism that guarantees C-39 compliance.

**R13 variation axes**:

- **V-01 (single axis: lifecycle emphasis)**: Canonical template section expanded with
  an explicit two-component declaration block (Header component → C-39; Closing component
  → C-40), a two-dimensional malformedness rule, and a conformance-collapse claim sentence.
  The template section becomes a four-part lifecycle: component declaration → template form
  → malformedness rule → conformance claim.

- **V-02 (single axis: output format / table-driven)**: Template components expressed as a
  Template Component Registry table (columns: Component | Line position | Governs |
  Required | Malformedness on absence). The table uses `RequiredVocabulary` for the Required
  column, inheriting the same closed-type discipline already applied to the relay schema.

- **V-03 (single axis: phrasing register / imperative)**: The canonical template section
  uses direct imperative language: "This template REQUIRES two components. A block missing
  either is INVALID." Short, no hedge. The C-42 claim is a direct rule, not a structural
  description. The conformance claim is a one-line assertion.

- **V-04 (combined: lifecycle emphasis + table-driven)**: Combines V-01's four-part
  lifecycle with V-02's Template Component Registry table. The registry table anchors the
  component declaration section.

- **V-05 (combined: lifecycle + table + role sequence)**: Adds a pre-trace SCHEMA ROLE
  that declares all canonical templates, registers all typed vocabularies, and produces
  the Phase Label Schema before any trace phase runs. The canonical template declaration
  is part of the SCHEMA ROLE's output, making it a first-class structural artifact rather
  than a prompt comment.

All five variations inherit the full R12 V-05 architecture:
- Phase Label Schema table before trace content (C-14)
- Defect Classification Registry before Phase 1 with DefectCodeVocab CLOSED TYPE (C-30)
- DefectCodeVocab Independence Statement (C-33, C-36)
- DefectCodeVocab extended with DEFECT: COUNT-MISMATCH and DEFECT: EMPTY-CELL (C-37, C-38)
- GATHER: spec inputs first (C-11), Coverage Matrix (C-09), BLOCKED rule (C-12), CLOSED
  ASSERTION with C-26 STRUCTURAL MANDATE with scorer heuristic (C-20, C-23, C-26, C-40)
- BIND: Conflict Precedence Rule (C-17), PrecedenceVocabulary CLOSED TYPE (C-22, C-25),
  StatusVocab CLOSED TYPE (C-16), Independence Statement, RequiredVocabulary (C-27),
  uniform (TypeName) annotations (C-28)
- EXECUTE: delimiter markers (C-13), Relay Schema with Binding pairs (C-18), ANTI-PATTERN
  VIOLATION row (C-21, C-24, C-27)
- VERDICT: PRE-READ GATE with defect emission + C-38 STRUCTURAL MANDATE with scorer
  heuristic (C-35, C-38), C-29 Audit Block at top (C-32), C-28 COUNT GATE as binary
  self-evaluating gate with defect emission + C-37 STRUCTURAL MANDATE with scorer
  heuristic (C-34, C-37), Compliance Ledger with Defect code (DefectCodeVocab) column
  (C-15, C-07, C-31), C-36 STRUCTURAL MANDATE with scorer heuristic

---

## V-01 -- Single axis: C-42 via lifecycle emphasis (two-component declaration + malformedness extension + conformance-collapse claim)

**Axis**: Lifecycle emphasis -- the canonical template section is expanded from a single
conformance statement into a four-part lifecycle: (1) REQUIRED COMPONENTS block declares
the Header component (governs C-39) and Closing component (governs C-40) as named required
parts; (2) CANONICAL FORM block shows the complete template; (3) MALFORMEDNESS RULE extends
to both components; (4) CONFORMANCE-COLLAPSE CLAIM explicitly states that template-
conformance is a single gate for both C-39 and C-40 combined.

**Hypothesis**: R12 V-05's canonical template includes the scorer confirmation line as an
example, but the malformedness check covers only the header syntax. A scorer checking C-42
must confirm that the closing heuristic is declared as a required component -- not just
shown. Adding the REQUIRED COMPONENTS block with two named entries, extending the
malformedness rule to check both components, and adding the conformance-collapse claim
makes C-42 structurally self-evident: a scorer reads the REQUIRED COMPONENTS block,
confirms it names Header (→C-39) and Closing (→C-40), reads the conformance-collapse claim,
and confirms C-42 without inspecting individual blocks. Risk: adding four sections may
increase cognitive weight before the Phase Label Schema. Mitigation: each section is
labeled and short; the combined template section is under 12 lines.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

**REQUIRED COMPONENTS** -- every STRUCTURAL MANDATE block in this prompt must include
both of the following components. A block missing either component is structurally
malformed.

- **Header component** (governs C-39): first line follows `STRUCTURAL MANDATE (C-XX):`
  syntax, naming the governing criterion ID within the block header.
- **Closing component** (governs C-40): last line follows `A scorer confirms C-XX
  compliance by [specific method] alone without [parsing alternative].` syntax,
  embedding the scorer confirmation heuristic within the block body.

**CANONICAL FORM**:

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

**MALFORMEDNESS RULE**: A block is structurally malformed if (a) its first line does not
match `STRUCTURAL MANDATE (C-XX)` header syntax, OR (b) its last line does not include
the `A scorer confirms C-XX compliance by` closing heuristic. Both components are
independently required.

**CONFORMANCE-COLLAPSE CLAIM**: Any block conforming to this canonical form satisfies
C-39 (inline criterion citation) and C-40 (scorer confirmation heuristic) by a single
template-conformance check. C-40 compliance is contractually guaranteed by the same
structural mechanism that guarantees C-39 compliance. A scorer confirms C-42 compliance
by verifying this REQUIRED COMPONENTS declaration names both Header and Closing components
with their governing criteria alone without inspecting individual block bodies.

Additional mandates are mechanically derivable from this template by substituting the
governing criterion ID, the element description, and the confirmation method.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. It is immutable.

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

---

### Defect Classification Registry

Emit before any trace phase runs.

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                            |
|-------------------------------|---------------------------------------------------------|---------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution                 |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column           |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins        |

---

## GATHER

Enumerate spec inputs first, then invocation inputs.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop. Do not proceed to BIND.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override` in the Precedence applied column. When the invocation supplies a value
absent from the spec, record `default`. When input is BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections. Every section
required by the skill spec must appear in full.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell carries an explicit `` `InputName = "ResolvedValue"` `` pair. The
resolved value is stated in the relay itself so Verdict can verify without re-reading BIND.

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order is
mandated: (a), (b), (c) complete before any ledger row is read.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column of the
Compliance Ledger. Do not proceed until gate clears.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-38 compliance by `DEFECT: EMPTY-CELL` emission presence (or explicit
> "no empty cells" clearance) before the compliance ledger alone without reading ledger rows.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed (PRE-READ GATE cleared): [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across BIND,
EXECUTE relay schema, Defect Classification Registry, and Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE emit `DEFECT: COUNT-MISMATCH` and record in
Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-02 -- Single axis: C-42 via output format (Template Component Registry table)

**Axis**: Output format / table-driven -- the canonical template section introduces a
Template Component Registry table with columns: Component | Line position | Governs |
Required (RequiredVocabulary) | Malformedness on absence. The table inherits the same
`RequiredVocabulary` (CLOSED TYPE) already declared in BIND, making the Required column
self-validating without additional type registration. The template form and a conformance-
collapse claim follow the table.

**Hypothesis**: Expressing required template components as a table rows makes each
component independently citable by row (as "Template Component Registry row: Closing
heuristic") without prose interpretation. A scorer confirming C-42 reads the Registry
table, locates the Closing heuristic row, confirms Required = YES, and confirms Governs =
C-40 -- the table is the gate. The conformance-collapse claim then states that this table
is the single check for both C-39 and C-40. Risk: the Template Component Registry
introduces a new table before the Phase Label Schema; a model may omit the Registry at
run time. Mitigation: the Registry appears directly under the canonical template section
header with an emit instruction, parallel to the Defect Classification Registry.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

Emit this Template Component Registry BEFORE any trace content begins.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION` -- inherited from BIND schema;
applies to this registry's Required column.

| Component | Line position | Governs | Required (RequiredVocabulary) | Malformedness on absence |
|-----------|---------------|---------|-------------------------------|--------------------------|
| Criterion header | First line | C-39 (inline criterion citation) | YES | Block header does not cite criterion ID in `STRUCTURAL MANDATE (C-XX):` format |
| Body mandate | Middle line(s) | C-41 (element named + reproduce instruction) | YES | Block body missing "named structural mandate" phrase or "Reproduce it exactly" instruction |
| Scorer heuristic | Last line | C-40 (scorer confirmation heuristic) | YES | Block lacks `A scorer confirms C-XX compliance by [method] alone without [alternative].` closing line |

**CANONICAL FORM** -- all STRUCTURAL MANDATE blocks in this prompt conform to this form:

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

**CONFORMANCE-COLLAPSE CLAIM**: A block conforming to this canonical form satisfies C-39
and C-40 by a single Template Component Registry conformance check. C-40 compliance is
contractually guaranteed by the Closing heuristic row (Required = YES) in the same
registry that guarantees C-39 compliance via the Criterion header row.

Additional mandates are mechanically derivable from this template by substituting the
governing criterion ID, the element description, and the confirmation method.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. It is immutable.

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

---

### Defect Classification Registry

Emit before any trace phase runs.

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                            |
|-------------------------------|---------------------------------------------------------|---------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution                 |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column           |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins        |

---

## GATHER

Enumerate spec inputs first, then invocation inputs.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop. Do not proceed to BIND.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override` in the Precedence applied column. When the invocation supplies a value
absent from the spec, record `default`. When input is BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections. Every section
required by the skill spec must appear in full.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell carries an explicit `` `InputName = "ResolvedValue"` `` pair. The
resolved value is stated in the relay itself so Verdict can verify without re-reading BIND.

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order is
mandated: (a), (b), (c) complete before any ledger row is read.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column of the
Compliance Ledger. Do not proceed until gate clears.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-38 compliance by `DEFECT: EMPTY-CELL` emission presence (or explicit
> "no empty cells" clearance) before the compliance ledger alone without reading ledger rows.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed (PRE-READ GATE cleared): [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across BIND,
EXECUTE relay schema, Defect Classification Registry, and Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE emit `DEFECT: COUNT-MISMATCH` and record in
Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-03 -- Single axis: C-42 via phrasing register (imperative two-component requirement)

**Axis**: Phrasing register / imperative -- the canonical template section uses direct
imperative language. The two-component requirement is stated as a hard rule ("MUST"),
not as a description. The canonical form is shown once. The C-42 claim is a one-line
assertion, not a structural description. No table. No multi-section lifecycle.

**Hypothesis**: Imperative phrasing minimizes model interpretation overhead. A model
reading "you MUST include both components -- a block missing either is INVALID" has a
clear compliance rule without parsing a registry table or a four-part lifecycle. The
scorer confirmation heuristic requirement is stated as a direct obligation: "every block
MUST close with `A scorer confirms C-XX compliance by [method] alone without
[alternative]`." The conformance-collapse claim is a one-line assertion. Risk: without
a registry table or component labels, a scorer checking C-42 must infer from the imperative
statement that the closing heuristic is a named required component. Mitigation: the
imperative statement names both components ("criterion-ID header" and "scorer confirmation
closing line") explicitly, so the identification does not require parsing surrounding prose.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

Every STRUCTURAL MANDATE block in this prompt MUST include two components. A block missing
either component is INVALID.

- **Component 1**: criterion-ID header -- `> STRUCTURAL MANDATE (C-XX):` syntax, naming
  the governing criterion by ID. Required by C-39.
- **Component 2**: scorer confirmation closing line -- `> A scorer confirms C-XX compliance
  by [specific method] alone without [parsing alternative].` as the last line of the block.
  Required by C-40.

Canonical form -- every block MUST conform to this:

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

Any block conforming to this form satisfies C-39 and C-40 by one check. C-40 is
contractually required -- not optional, not inferred.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. It is immutable.

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

---

### Defect Classification Registry

Emit before any trace phase runs.

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                            |
|-------------------------------|---------------------------------------------------------|---------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution                 |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column           |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins        |

---

## GATHER

Enumerate spec inputs first, then invocation inputs.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop. Do not proceed to BIND.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override` in the Precedence applied column. When the invocation supplies a value
absent from the spec, record `default`. When input is BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections. Every section
required by the skill spec must appear in full.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell carries an explicit `` `InputName = "ResolvedValue"` `` pair. The
resolved value is stated in the relay itself so Verdict can verify without re-reading BIND.

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order is
mandated: (a), (b), (c) complete before any ledger row is read.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column of the
Compliance Ledger. Do not proceed until gate clears.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-38 compliance by `DEFECT: EMPTY-CELL` emission presence (or explicit
> "no empty cells" clearance) before the compliance ledger alone without reading ledger rows.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed (PRE-READ GATE cleared): [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across BIND,
EXECUTE relay schema, Defect Classification Registry, and Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE emit `DEFECT: COUNT-MISMATCH` and record in
Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-04 -- Combined: C-42 via lifecycle emphasis + table-driven (Template Component Registry + four-part lifecycle)

**Axis**: Lifecycle emphasis + output format -- combines V-01's four-part lifecycle
(component declaration → canonical form → malformedness rule → conformance-collapse claim)
with V-02's Template Component Registry table. The registry table IS the component
declaration section; the four-part lifecycle organizes the overall section. The registry
uses `RequiredVocabulary` (CLOSED TYPE) inherited from BIND, making the Required column
self-validating. The malformedness rule references the registry by row, not by prose
description. The conformance-collapse claim follows the malformedness rule.

**Hypothesis**: V-04 composes V-01 and V-02 cleanly: the table anchors the component
declaration, and the lifecycle structure organizes the reader's traversal. A scorer
checking C-42 reads: (1) the registry table -- Closing heuristic row is Required=YES
governed by C-40; (2) the malformedness rule -- "a block is malformed if it is missing
any Required=YES row from the Template Component Registry"; (3) the conformance-collapse
claim -- "conformance to this template satisfies C-39 and C-40 by the single registry
check." The C-42 check path is fully explicit without any prose-parsing. No axis degrades
prior passing criteria: the registry table uses RequiredVocabulary already declared in
BIND, so no new type registration is required at this location.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

**Step 1 -- TEMPLATE COMPONENT REGISTRY**: Emit before any trace content begins.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION` -- inherited from BIND schema.

| Component | Line position | Governs | Required (RequiredVocabulary) | Malformedness on absence |
|-----------|---------------|---------|-------------------------------|--------------------------|
| Criterion header | First line | C-39 (inline criterion citation) | YES | Header does not cite criterion ID in `STRUCTURAL MANDATE (C-XX):` format |
| Body mandate | Middle line(s) | C-41 (element named + reproduce instruction) | YES | Body missing "named structural mandate" phrase or "Reproduce it exactly" instruction |
| Scorer heuristic | Last line | C-40 (scorer confirmation heuristic) | YES | Closing line absent: `A scorer confirms C-XX compliance by [method] alone without [alternative].` |

**Step 2 -- CANONICAL FORM**: All STRUCTURAL MANDATE blocks conform to this form.

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

**Step 3 -- MALFORMEDNESS RULE**: A block is structurally malformed if it is missing any
component marked Required=YES in the Template Component Registry. Absence of the Criterion
header row component OR absence of the Scorer heuristic row component independently
constitutes malformedness.

**Step 4 -- CONFORMANCE-COLLAPSE CLAIM**: A block conforming to this canonical form
satisfies C-39 (Criterion header row, Required=YES) and C-40 (Scorer heuristic row,
Required=YES) by a single Template Component Registry conformance check. C-40 compliance
is contractually guaranteed by the registry's Scorer heuristic row using the same
mechanism that guarantees C-39 compliance via the Criterion header row. A scorer confirms
C-42 compliance by verifying the Template Component Registry declares both rows with
Required=YES alone without inspecting individual block bodies.

Additional mandates are mechanically derivable from this template by substituting the
governing criterion ID, the element description, and the confirmation method.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. It is immutable.

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

---

### Defect Classification Registry

Emit before any trace phase runs.

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                            |
|-------------------------------|---------------------------------------------------------|---------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution                 |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column           |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins        |

---

## GATHER

Enumerate spec inputs first, then invocation inputs.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop. Do not proceed to BIND.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override` in the Precedence applied column. When the invocation supplies a value
absent from the spec, record `default`. When input is BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections. Every section
required by the skill spec must appear in full.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell carries an explicit `` `InputName = "ResolvedValue"` `` pair. The
resolved value is stated in the relay itself so Verdict can verify without re-reading BIND.

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order is
mandated: (a), (b), (c) complete before any ledger row is read.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column of the
Compliance Ledger. Do not proceed until gate clears.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-38 compliance by `DEFECT: EMPTY-CELL` emission presence (or explicit
> "no empty cells" clearance) before the compliance ledger alone without reading ledger rows.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed (PRE-READ GATE cleared): [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across BIND,
EXECUTE relay schema, Defect Classification Registry, Template Component Registry, and
Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE emit `DEFECT: COUNT-MISMATCH` and record in
Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-05 -- Combined: C-42 via lifecycle emphasis + table-driven + role sequence (SCHEMA ROLE pre-trace declaration)

**Axis**: Lifecycle emphasis + output format + role sequence -- a pre-trace SCHEMA ROLE
declares all canonical templates, registers all typed vocabularies, and produces the Phase
Label Schema before any trace phase runs. The canonical template declaration and its
Template Component Registry are part of the SCHEMA ROLE's output, making them first-class
structural artifacts rather than prompt comments. The trace phases (GATHER, BIND, EXECUTE,
VERDICT) execute as subsequent roles after the SCHEMA ROLE completes. All STRUCTURAL
MANDATE blocks in the trace phases must conform to the canonical form declared by the
SCHEMA ROLE.

**Hypothesis**: V-05 integrates three axes. The SCHEMA ROLE separation gives the canonical
template declaration a structural identity distinct from trace instructions: it is an
artifact produced by a named role, not a prompt annotation. This makes the Template
Component Registry a trace output (verifiable in the record) rather than a prompt element
(which could be forgotten). A scorer checking C-42 reads the SCHEMA ROLE output section,
finds the Template Component Registry table, confirms both Required=YES rows (Criterion
header and Scorer heuristic), and confirms the conformance-collapse claim -- all before
any trace content exists. Risk: the SCHEMA ROLE adds structural overhead before GATHER.
Mitigation: the SCHEMA ROLE is bounded, labeled, and produces exactly three outputs
(canonical template registry, Phase Label Schema, type vocabulary declarations). Once the
SCHEMA ROLE section ends, the trace proceeds exactly as in V-04.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

## SCHEMA ROLE (Pre-Trace)

The SCHEMA ROLE runs before any trace phase. It declares all structural schemas that
govern the trace. No trace content is produced during the SCHEMA ROLE. All subsequent
trace phases inherit these declarations.

### SCHEMA ROLE Output 1: Canonical Structural Mandate Template (C-41, C-42)

The following Template Component Registry declares all required components of every
STRUCTURAL MANDATE block in this trace. Emit this registry as part of SCHEMA ROLE output
before the Phase Label Schema.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION` -- governs the Required column
of the Template Component Registry and the Role column of the Execute Relay Schema.

| Component | Line position | Governs | Required (RequiredVocabulary) | Malformedness on absence |
|-----------|---------------|---------|-------------------------------|--------------------------|
| Criterion header | First line | C-39 (inline criterion citation) | YES | Header does not cite criterion ID in `STRUCTURAL MANDATE (C-XX):` format |
| Body mandate | Middle line(s) | C-41 (element named + reproduce instruction) | YES | Body missing "named structural mandate" phrase or "Reproduce it exactly" instruction |
| Scorer heuristic | Last line | C-40 (scorer confirmation heuristic) | YES | Closing line absent: `A scorer confirms C-XX compliance by [method] alone without [alternative].` |

Canonical form -- every STRUCTURAL MANDATE block in this trace MUST conform:

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

Malformedness rule: A block is structurally malformed if it is missing any component
marked Required=YES in the Template Component Registry above.

Conformance-collapse claim: A block conforming to this canonical form satisfies C-39
and C-40 by a single Template Component Registry conformance check. C-40 compliance is
contractually guaranteed by the Scorer heuristic row (Required=YES) in the same registry
that guarantees C-39 compliance via the Criterion header row. A scorer confirms C-42
compliance by verifying the Template Component Registry declares both rows with
Required=YES alone without inspecting individual block bodies.

### SCHEMA ROLE Output 2: Phase Label Schema (Immutable)

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

### SCHEMA ROLE Output 3: Type Vocabulary Declarations

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside these vocabularies is a schema error
independently detectable without consulting registry rows.

---

### Defect Classification Registry

Emit after SCHEMA ROLE, before trace phases run.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                            |
|-------------------------------|---------------------------------------------------------|---------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution                 |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column           |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins        |

---

## GATHER

Enumerate spec inputs first, then invocation inputs.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop. Do not proceed to BIND.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override` in the Precedence applied column. When the invocation supplies a value
absent from the spec, record `default`. When input is BLOCKED, record `BLOCKED`.

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections. Every section
required by the skill spec must appear in full.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell carries an explicit `` `InputName = "ResolvedValue"` `` pair. The
resolved value is stated in the relay itself so Verdict can verify without re-reading BIND.

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order is
mandated: (a), (b), (c) complete before any ledger row is read.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column of the
Compliance Ledger. Do not proceed until gate clears.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-38 compliance by `DEFECT: EMPTY-CELL` emission presence (or explicit
> "no empty cells" clearance) before the compliance ledger alone without reading ledger rows.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed (PRE-READ GATE cleared): [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across SCHEMA
ROLE (Template Component Registry Required column), BIND, EXECUTE relay schema, Defect
Classification Registry, and Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE emit `DEFECT: COUNT-MISMATCH` and record in
Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.
