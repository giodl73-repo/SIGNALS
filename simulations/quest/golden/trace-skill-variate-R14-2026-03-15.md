---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 14
rubric: trace-skill-rubric-v13-2026-03-15.md
---

# trace-skill -- Variations R14 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

## Entry State

R13 all five variations passed C-42. v13 formalizes two new aspirational criteria from R13
excellence analysis: C-43 and C-44. Aspirational denominator advances from 34 to 36.

**R13 C-42 PASS state and the R14 upgrade axes**:

- **C-43 gap (from V-03 weakness)**: V-01 and V-04 carried an explicit
  `A scorer confirms C-42 compliance by [X] alone without [Y]` heuristic inside the
  conformance-collapse claim. V-03 stated the claim but omitted the self-scoring heuristic.
  C-43 formalizes: the conformance-collapse claim itself must close with a scorer
  confirmation heuristic, making the C-42 mechanism self-scoring (not just present).

- **C-44 gap (from V-02 scope incompleteness)**: V-02's C-28 COUNT GATE scope omitted the
  Template Component Registry's `Required (RequiredVocabulary)` typed column. V-04
  explicitly included it. C-44 formalizes: the COUNT GATE scope list must name
  `Required (RequiredVocabulary)` from the Template Component Registry alongside all
  other typed columns.

**R14 variation axes**:

- **V-01 (single axis: C-43 structural isolation)**: The conformance-collapse claim's scorer
  heuristic is presented as a `**SCORER HEURISTIC (C-43):**` bold-labeled sub-element,
  paralleling the `**Independence Statement**:` pattern from DefectCodeVocab. The label
  makes the heuristic independently locatable by label scan without reading the claim body.

- **V-02 (single axis: C-44 scope format)**: The C-28 COUNT GATE uses a formal ANNOTATION
  SCOPE REGISTRY table with one explicit row per typed column site. The TCR row
  (`Required (RequiredVocabulary)`) appears as row 1. The table makes each annotation site
  independently verifiable without prose parsing.

- **V-03 (single axis: phrasing register / imperative)**: Imperative register throughout.
  The conformance-collapse claim uses commanding form. The COUNT GATE scope uses a numbered
  imperative checklist. C-43 and C-44 requirements stated as hard rules rather than
  structural descriptions.

- **V-04 (combined: V-01 + V-02)**: SCORER HEURISTIC bold label + ANNOTATION SCOPE
  REGISTRY table.

- **V-05 (combined: V-01 + V-02 + V-03 + SCHEMA ROLE)**: Full combination. Pre-trace
  SCHEMA ROLE produces the TCR, canonical template, and type declarations as a named
  structural artifact. All three axes apply inside and after the SCHEMA ROLE.

All five variations have as baseline:
- C-43: conformance-collapse claim closes with `A scorer confirms C-42 compliance by [X]
  alone without [Y]` (all five)
- C-44: COUNT GATE scope explicitly enumerates Template Component Registry's
  `Required (RequiredVocabulary)` using full `ColumnName (TypeName)` notation (all five)
- Full R13 V-05 architecture for C-01 through C-42

---

## V-01 -- Single axis: C-43 heuristic as bold-labeled sub-element (SCORER HEURISTIC label)

**Axis**: C-43 structural isolation -- the conformance-collapse claim's scorer confirmation
heuristic is a `**SCORER HEURISTIC (C-43):**` bold-labeled structural element at the close
of the claim block, paralleling how `**Independence Statement**:` is a named bold label
within the DefectCodeVocab declaration (C-36). The claim body states the collapse mechanism;
the `SCORER HEURISTIC` label isolates the confirmation method as an independently citeable
element.

**Hypothesis**: R13 V-01 embedded the C-43 heuristic as the final sentence of the claim
paragraph, which passes C-43 functionally but requires reading the full claim to locate it.
Isolating the heuristic behind a bold label gives it the same structural standing as the
Independence Statement: a scorer can confirm C-43 compliance by finding the
`**SCORER HEURISTIC (C-43):**` label alone without parsing the claim body. This applies the
same structural isolation discipline that C-36 applies to the Independence Statement at the
level of the conformance-collapse mechanism.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

**REQUIRED COMPONENTS** -- every STRUCTURAL MANDATE block in this prompt must include
both of the following components. A block missing either component is structurally malformed.

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
match `STRUCTURAL MANDATE (C-XX)` header syntax, OR (b) its last line does not carry the
`A scorer confirms C-XX compliance by` closing heuristic. Both components are independently
required.

**CONFORMANCE-COLLAPSE CLAIM**: Any block conforming to this canonical form satisfies
C-39 (inline criterion citation) and C-40 (scorer confirmation heuristic) by a single
template-conformance check. C-40 compliance is contractually guaranteed by the same
structural mechanism that guarantees C-39 compliance: the Closing component is a required
part of the canonical template, not an optional addition.

**SCORER HEURISTIC (C-43)**: A scorer confirms C-42 compliance by locating this
`**SCORER HEURISTIC (C-43):**` label and reading its stated method alone without
inspecting individual STRUCTURAL MANDATE block bodies. The method: verify this REQUIRED
COMPONENTS declaration names both Header and Closing components -- the presence of both
named components contractually guarantees C-39 and C-40 together.

Additional STRUCTURAL MANDATE blocks are mechanically derivable by substituting the
governing criterion ID, the element description, and the confirmation method into the
canonical form.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. Do not modify phase labels.

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

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                     |
|-------------------------------|---------------------------------------------------------|--------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution          |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column    |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins |

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> `DefectCodeVocab` type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded label structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## GATHER

Enumerate spec inputs first (from `{{skill_spec_path}}`), then invocation inputs (from
`{{invocation}}`).

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

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

**Independence Statement**: Any value outside these vocabularies is a schema error
independently detectable without consulting registry rows.

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

Typed annotation sites -- all columns following `ColumnName (TypeName)` convention,
enumerated by location:

1. Template Component Registry: `Required (RequiredVocabulary)` -- 1 site
2. Bind table: `Status (StatusVocab)` -- 1 site
3. Bind table: `Precedence applied (PrecedenceVocabulary)` -- 1 site
4. Execute Relay: `Role (RequiredVocabulary)` -- 1 site
5. Execute Relay: `Status (StatusVocab)` -- 1 site
6. Defect Classification Registry: `Defect Code (DefectCodeVocab)` -- 1 site
7. Verdict Compliance Ledger: `Defect code (DefectCodeVocab)` -- 1 site

Declared count: 7

IF actual annotation sites == 7 THEN `confirmed`
ELSE `mismatch` -- emit `DEFECT: COUNT-MISMATCH` and record in Defect code column.

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

Declare PASS if C-01 through C-05 all result PASS. Declare FAIL otherwise. State rationale
citing criterion IDs.

---

## V-02 -- Single axis: C-44 scope format (ANNOTATION SCOPE REGISTRY table)

**Axis**: C-44 scope format -- the C-28 COUNT GATE's annotation site scope is declared as
a formal ANNOTATION SCOPE REGISTRY table with one row per typed column site. Row 1 is the
Template Component Registry's `Required (RequiredVocabulary)` column. The table format
gives each site an independently identifiable row with explicit `ColumnName (TypeName)`
notation -- a scorer can verify C-44 by finding the TCR row in the table alone without
parsing a prose scope description.

**Hypothesis**: R13 V-05 described the scope in prose as "across SCHEMA ROLE (Template
Component Registry Required column), BIND..." which mentions the TCR but does not use the
full `ColumnName (TypeName)` typed notation. V-04 was more explicit. A scope registry table
applies the same structural discipline that the Template Component Registry and Defect
Classification Registry apply to their domains: each site is an independently verifiable
row rather than an embedded phrase. C-44 compliance is checkable by finding the TCR row
in the table alone without reading surrounding prose.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

**REQUIRED COMPONENTS** -- every STRUCTURAL MANDATE block in this prompt must include
both of the following components. A block missing either component is structurally malformed.

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
match `STRUCTURAL MANDATE (C-XX)` header syntax, OR (b) its last line does not carry the
`A scorer confirms C-XX compliance by` closing heuristic. Both components are independently
required.

**CONFORMANCE-COLLAPSE CLAIM**: Any block conforming to this canonical form satisfies
C-39 (inline criterion citation) and C-40 (scorer confirmation heuristic) by a single
template-conformance check. C-40 compliance is contractually guaranteed by the same
structural mechanism that guarantees C-39 compliance: the Closing component is a required
part of the canonical template. A scorer confirms C-42 compliance by verifying this
REQUIRED COMPONENTS declaration names both Header and Closing components with their
governing criteria alone without inspecting individual STRUCTURAL MANDATE block bodies.

Additional STRUCTURAL MANDATE blocks are mechanically derivable by substituting the
governing criterion ID, the element description, and the confirmation method into the
canonical form.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. Do not modify phase labels.

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

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                     |
|-------------------------------|---------------------------------------------------------|--------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution          |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column    |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins |

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> `DefectCodeVocab` type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded label structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## GATHER

Enumerate spec inputs first (from `{{skill_spec_path}}`), then invocation inputs (from
`{{invocation}}`).

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

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

**Independence Statement**: Any value outside these vocabularies is a schema error
independently detectable without consulting registry rows.

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

#### Annotation Scope Registry

All typed columns following `ColumnName (TypeName)` convention, enumerated by site:

| Site | Location                      | Typed Column                          | Count |
|------|-------------------------------|---------------------------------------|-------|
| 1    | Template Component Registry   | `Required (RequiredVocabulary)`       | 1     |
| 2    | Bind table                    | `Status (StatusVocab)`                | 1     |
| 3    | Bind table                    | `Precedence applied (PrecedenceVocabulary)` | 1 |
| 4    | Execute Relay schema          | `Role (RequiredVocabulary)`           | 1     |
| 5    | Execute Relay schema          | `Status (StatusVocab)`                | 1     |
| 6    | Defect Classification Registry| `Defect Code (DefectCodeVocab)`       | 1     |
| 7    | Verdict Compliance Ledger     | `Defect code (DefectCodeVocab)`       | 1     |

Declared count: 7

IF actual annotation sites == 7 THEN `confirmed`
ELSE `mismatch` -- emit `DEFECT: COUNT-MISMATCH` and record in Defect code column.

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

Declare PASS if C-01 through C-05 all result PASS. Declare FAIL otherwise. State rationale
citing criterion IDs.

---

## V-03 -- Single axis: phrasing register (imperative) with C-43 and C-44 as hard rules

**Axis**: Phrasing register -- all structural requirements stated as imperative commands.
The conformance-collapse claim uses commanding voice: the scorer confirmation heuristic is
a declared rule, not a structural description. The COUNT GATE scope is a numbered checklist
with each item as a mandatory verification step. C-43 and C-44 are present at full strength
in imperative form.

**Hypothesis**: R13 V-03 used imperative register but omitted C-43's scorer heuristic.
R14 V-03 carries both C-43 and C-44 in imperative form to test whether commanding language
produces different structural reliability from the declarative register used by V-01 and
V-02. Imperative register may make the C-43 requirement feel more binding ("you MUST
state") than declarative ("the claim closes with"). Risk: the implied prohibition structure
("do NOT omit") may be harder to audit than a labeled element. Mitigation: the C-43
imperative rule is named as a RULE block, making it independently citable.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template

Every STRUCTURAL MANDATE block in this trace MUST include TWO components. A block missing
either component is INVALID.

**Component 1 -- Header** (governs C-39): The first line MUST follow `STRUCTURAL MANDATE (C-XX):` syntax. The criterion ID goes inside the parentheses.

**Component 2 -- Scorer heuristic** (governs C-40): The last line MUST follow
`A scorer confirms C-XX compliance by [specific method] alone without [parsing alternative].`
Any block missing this closing line is INVALID.

**Required canonical form**:

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

**CONFORMANCE-COLLAPSE RULE (C-42)**: When a block conforms to the canonical form above,
it satisfies BOTH C-39 AND C-40 automatically. You MUST NOT check C-39 and C-40
separately for conforming blocks -- one conformance check covers both. C-40 is guaranteed
by Component 2 being required. C-39 is guaranteed by Component 1 being required.
**You MUST close this rule with the following scorer confirmation line**: A scorer confirms
C-42 compliance by verifying both Component 1 and Component 2 are declared as required
above alone without inspecting individual STRUCTURAL MANDATE block bodies.

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. Do not modify phase labels.

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

---

### Defect Classification Registry

ALWAYS emit this registry before any trace phase begins. You MUST NOT skip it.

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH, DEFECT: EMPTY-CELL}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                     |
|-------------------------------|---------------------------------------------------------|--------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution          |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column    |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins |

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> `DefectCodeVocab` type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded label structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## GATHER

ALWAYS enumerate spec inputs first, then invocation inputs. NEVER reverse this order.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

You MUST treat the following inputs as the complete and exhaustive set. No inputs exist
outside this list. Additions are PROHIBITED.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, you MUST write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and STOP. Do NOT proceed to BIND.

**CLOSED ASSERTION block** -- you MUST reproduce this block verbatim:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec ALWAYS
anchors. Record `override`. When invocation supplies a value absent from spec, record
`default`. For BLOCKED inputs, record `BLOCKED`. You MUST NOT use any other values.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

**Independence Statement**: Any value outside these vocabularies is a schema error
independently detectable without consulting registry rows.

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

Produce the COMPLETE artifact. You MUST NOT use elision markers. You MUST NOT write
placeholder sections. Every section required by the skill spec MUST appear in full.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay. You MUST include every required field.

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | NEVER write input name only -- ALWAYS write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell MUST carry an explicit `` `InputName = "ResolvedValue"` `` pair.
NEVER write just the input name. NEVER omit the resolved value.

---

## VERDICT

### PRE-READ GATE

You MUST run phases (a), (b), (c) BEFORE reading any compliance ledger row.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) FAILS: HALT. You MUST emit `DEFECT: EMPTY-CELL`. Record it in the Defect code
column. Do NOT proceed until gate clears.

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

You MUST verify all typed annotation sites before reading the Compliance Ledger. Typed
columns follow `ColumnName (TypeName)` convention. Check each site below:

1. Template Component Registry -- `Required (RequiredVocabulary)`: PRESENT / ABSENT
2. Bind table -- `Status (StatusVocab)`: PRESENT / ABSENT
3. Bind table -- `Precedence applied (PrecedenceVocabulary)`: PRESENT / ABSENT
4. Execute Relay -- `Role (RequiredVocabulary)`: PRESENT / ABSENT
5. Execute Relay -- `Status (StatusVocab)`: PRESENT / ABSENT
6. Defect Classification Registry -- `Defect Code (DefectCodeVocab)`: PRESENT / ABSENT
7. Verdict Compliance Ledger -- `Defect code (DefectCodeVocab)`: PRESENT / ABSENT

Declared count: 7. Count present sites. IF count == 7 THEN `confirmed`
ELSE you MUST emit `DEFECT: COUNT-MISMATCH` and record in Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code MUST be `--`. FAIL rows: Defect code MUST be a value from
DefectCodeVocab. NEVER leave any cell empty.

Declare PASS if C-01 through C-05 all result PASS. Declare FAIL otherwise. State rationale
citing criterion IDs.

---

## V-04 -- Combined: V-01 + V-02 (SCORER HEURISTIC bold label + ANNOTATION SCOPE REGISTRY table)

**Axes**: C-43 structural isolation (V-01 axis) + C-44 scope format (V-02 axis). The
conformance-collapse claim carries a `**SCORER HEURISTIC (C-43):**` labeled sub-element.
The COUNT GATE scope is a formal ANNOTATION SCOPE REGISTRY table with TCR as row 1.

**Hypothesis**: V-01 demonstrated that structural isolation of C-43 is possible via bold
label. V-02 demonstrated that tabular scope declaration makes C-44 independently verifiable.
V-04 tests whether both structural isolation mechanisms work additively: the scorer can
confirm C-43 by label scan AND confirm C-44 by table row lookup, without either check
requiring inference or prose parsing. Combined, these two mechanisms represent the highest
structural isolation available to the new criteria without the overhead of the SCHEMA ROLE.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

**REQUIRED COMPONENTS** -- every STRUCTURAL MANDATE block in this prompt must include
both of the following components. A block missing either component is structurally malformed.

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
match `STRUCTURAL MANDATE (C-XX)` header syntax, OR (b) its last line does not carry the
`A scorer confirms C-XX compliance by` closing heuristic. Both components are independently
required.

**CONFORMANCE-COLLAPSE CLAIM**: Any block conforming to this canonical form satisfies
C-39 (inline criterion citation) and C-40 (scorer confirmation heuristic) by a single
template-conformance check. C-40 compliance is contractually guaranteed by the same
structural mechanism that guarantees C-39 compliance: the Closing component is a required
part of the canonical template, not an optional addition.

**SCORER HEURISTIC (C-43)**: A scorer confirms C-42 compliance by locating this
`**SCORER HEURISTIC (C-43):**` label and reading its stated method alone without
inspecting individual STRUCTURAL MANDATE block bodies. The method: verify this REQUIRED
COMPONENTS declaration names both Header and Closing components -- the presence of both
named components contractually guarantees C-39 and C-40 together.

Additional STRUCTURAL MANDATE blocks are mechanically derivable by substituting the
governing criterion ID, the element description, and the confirmation method into the
canonical form.

---

### Phase Label Schema (Immutable)

Emit this schema BEFORE any trace content begins. Do not modify phase labels.

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

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                     |
|-------------------------------|---------------------------------------------------------|--------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution          |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column    |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins |

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> `DefectCodeVocab` type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded label structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## GATHER

Enumerate spec inputs first (from `{{skill_spec_path}}`), then invocation inputs (from
`{{invocation}}`).

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

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

**Independence Statement**: Any value outside these vocabularies is a schema error
independently detectable without consulting registry rows.

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

#### Annotation Scope Registry

All typed columns following `ColumnName (TypeName)` convention, enumerated by site:

| Site | Location                      | Typed Column                                | Count |
|------|-------------------------------|---------------------------------------------|-------|
| 1    | Template Component Registry   | `Required (RequiredVocabulary)`             | 1     |
| 2    | Bind table                    | `Status (StatusVocab)`                      | 1     |
| 3    | Bind table                    | `Precedence applied (PrecedenceVocabulary)` | 1     |
| 4    | Execute Relay schema          | `Role (RequiredVocabulary)`                 | 1     |
| 5    | Execute Relay schema          | `Status (StatusVocab)`                      | 1     |
| 6    | Defect Classification Registry| `Defect Code (DefectCodeVocab)`             | 1     |
| 7    | Verdict Compliance Ledger     | `Defect code (DefectCodeVocab)`             | 1     |

Declared count: 7

IF actual annotation sites == 7 THEN `confirmed`
ELSE `mismatch` -- emit `DEFECT: COUNT-MISMATCH` and record in Defect code column.

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

Declare PASS if C-01 through C-05 all result PASS. Declare FAIL otherwise. State rationale
citing criterion IDs.

---

## V-05 -- Combined: V-01 + V-02 + V-03 + SCHEMA ROLE (maximum structural isolation)

**Axes**: C-43 SCORER HEURISTIC label (V-01) + C-44 ANNOTATION SCOPE REGISTRY table (V-02)
+ imperative register (V-03) + SCHEMA ROLE pre-trace structure (R13 V-05 architecture).
The SCHEMA ROLE produces the Template Component Registry as a named trace artifact before
any phase runs, giving the TCR (and its `Required (RequiredVocabulary)` column that C-44
targets) a structural identity as a role output rather than a prompt annotation.

**Hypothesis**: V-04 achieves C-43 and C-44 with maximum structural isolation within the
existing prompt structure. V-05 adds the SCHEMA ROLE, which elevates the TCR from a prompt
structural element to a trace-produced artifact -- meaning a scorer checking C-44 finds the
TCR's typed column in the SCHEMA ROLE output section, which is structurally separated from
the COUNT GATE. The TCR column's presence is verifiable independently before the gate runs.
Combined with imperative register and the V-01/V-02 isolation mechanisms, V-05 represents
the most defensively complete implementation. Risk: SCHEMA ROLE adds structural overhead.
Mitigation: the SCHEMA ROLE is bounded, labeled, and produces exactly four outputs (TCR,
canonical template, Phase Label Schema, type declarations). Once the SCHEMA ROLE ends,
trace phases proceed as in V-04.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

## SCHEMA ROLE (Pre-Trace)

The SCHEMA ROLE runs before any trace phase. It MUST produce all four outputs below.
No trace content is produced during the SCHEMA ROLE. All subsequent trace phases MUST
inherit these declarations.

### SCHEMA ROLE Output 1: Canonical Structural Mandate Template

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`
This type governs the Required column of the Template Component Registry below AND the
Role column of the Execute Relay schema.

Every STRUCTURAL MANDATE block in this trace MUST include BOTH of the following components.
A block missing either component is INVALID.

#### Template Component Registry

| Component         | Line position  | Governs                          | Required (RequiredVocabulary) | Malformedness on absence                                                          |
|-------------------|----------------|----------------------------------|-------------------------------|-----------------------------------------------------------------------------------|
| Criterion header  | First line     | C-39 (inline criterion citation) | YES                           | Block header missing `STRUCTURAL MANDATE (C-XX):` format                         |
| Body mandate      | Middle line(s) | C-41 (element + reproduce inst.) | YES                           | Body missing "named structural mandate" phrase or "Reproduce it exactly"          |
| Scorer heuristic  | Last line      | C-40 (self-scoring heuristic)    | YES                           | Closing line absent: `A scorer confirms C-XX compliance by [method] alone without [alt].` |
| Absent component  | --             | --                               | VIOLATION                     | --                                                                                |

**Canonical form** -- every STRUCTURAL MANDATE block in this trace MUST conform:

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

**MALFORMEDNESS RULE**: A block is INVALID if it is missing any component marked
Required=YES in the Template Component Registry above.

**CONFORMANCE-COLLAPSE CLAIM (C-42)**: Any block conforming to this canonical form
AUTOMATICALLY satisfies BOTH C-39 AND C-40 by a single Template Component Registry
conformance check. You MUST NOT check C-39 and C-40 separately for conforming blocks.
C-40 is contractually guaranteed by the Scorer heuristic row (Required=YES). C-39 is
contractually guaranteed by the Criterion header row (Required=YES).

**SCORER HEURISTIC (C-43)**: A scorer confirms C-42 compliance by locating this
`**SCORER HEURISTIC (C-43):**` label and reading its stated method alone without
inspecting individual STRUCTURAL MANDATE block bodies. The method: verify the Template
Component Registry above declares both Criterion header and Scorer heuristic rows with
Required=YES -- their presence contractually guarantees C-39 and C-40 together.

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

### SCHEMA ROLE Output 4: Defect Classification Registry

You MUST emit this registry before any trace phase begins.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                     |
|-------------------------------|---------------------------------------------------------|--------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution          |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column    |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell found in Defect code column | Trace halts before ledger traversal begins |

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> type vocabulary declarations is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded label structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## GATHER

ALWAYS enumerate spec inputs first, then invocation inputs. NEVER reverse this order.

### Section 1: Spec Inputs

Read `{{skill_spec_path}}` and list every input the skill declares.

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

From `{{invocation}}`, list every value supplied at call time.

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

You MUST treat the following inputs as the complete and exhaustive set. No inputs exist
outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, you MUST write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and STOP. Do NOT proceed to BIND.

**CLOSED ASSERTION block** -- reproduce verbatim:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-26 compliance by closure terminus line presence alone without
> parsing the CLOSED ASSERTION block content.

---

## BIND

**Conflict Precedence Rule**: Spec ALWAYS anchors. When Spec and Invocation disagree,
record `override`. When invocation supplies a value absent from spec, record `default`.
For BLOCKED inputs, record `BLOCKED`. You MUST NOT use any other values.

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

You MUST produce the COMPLETE artifact. NEVER use elision markers. NEVER write placeholder
sections.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay. NEVER write just the input name -- ALWAYS use
`` `InputName = "ResolvedValue"` `` format in the Binding column.

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | NEVER write input name only -- ALWAYS write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

---

## VERDICT

### PRE-READ GATE

You MUST run phases (a), (b), (c) BEFORE reading any compliance ledger row.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) FAILS: HALT. You MUST emit `DEFECT: EMPTY-CELL`. Record it in the Defect code
column. Do NOT proceed until gate clears.

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

You MUST verify all typed annotation sites before reading the Compliance Ledger. Every
site below MUST be PRESENT. Typed columns follow `ColumnName (TypeName)` convention.

#### Annotation Scope Registry

| Site | Location                      | Typed Column                                | Count |
|------|-------------------------------|---------------------------------------------|-------|
| 1    | Template Component Registry   | `Required (RequiredVocabulary)`             | 1     |
| 2    | Bind table                    | `Status (StatusVocab)`                      | 1     |
| 3    | Bind table                    | `Precedence applied (PrecedenceVocabulary)` | 1     |
| 4    | Execute Relay schema          | `Role (RequiredVocabulary)`                 | 1     |
| 5    | Execute Relay schema          | `Status (StatusVocab)`                      | 1     |
| 6    | Defect Classification Registry| `Defect Code (DefectCodeVocab)`             | 1     |
| 7    | Verdict Compliance Ledger     | `Defect code (DefectCodeVocab)`             | 1     |

Declared count: 7. Count present sites.
IF count == 7 THEN `confirmed`
ELSE you MUST emit `DEFECT: COUNT-MISMATCH` and record in Defect code column.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code MUST be `--`. FAIL rows: Defect code MUST be a value from
DefectCodeVocab. You MUST NOT leave any cell empty.

Declare PASS if C-01 through C-05 all result PASS. Declare FAIL otherwise. State rationale
citing criterion IDs.
