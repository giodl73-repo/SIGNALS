---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 12
rubric: trace-skill-rubric-v11-2026-03-15.md
---

# trace-skill -- Variations R12 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

## Entry State

R11 V-01 achieves C-01 through C-36 PASS under v10 scoring (99.33 composite). v11
(updated after R11) formalizes three new aspirational criteria from R11 excellence
signals: C-39 (C-36 upgrade), C-40 (C-39 upgrade), C-41 (C-36 parallel-by-contract).
Aspirational denominator advances from 30 to 33.

**R11 failure analysis (C-37, C-38)** determines the R12 mechanical fixes:

- **C-37 FAIL in R11**: COUNT GATE emits `mismatch` on count discrepancy but carries no
  `DefectCodeVocab`-coded defect citation. `DEFECT: COUNT-MISMATCH` is absent from both
  the gate block and the DefectCodeVocab registry. Gate outcome is not ledger-traceable
  by defect code -- it is a prose verdict requiring scorer interpretation.

- **C-38 FAIL in R11**: PRE-READ GATE says "HALT and report violation in the ledger"
  but emits no DefectCodeVocab-coded defect. `DEFECT: EMPTY-CELL` is absent from both
  the gate block and the registry. The gate is ordering-only, not defect-emitting.

**R11 excellence patterns (C-39, C-40, C-41 source)**:

- **Pattern 1 (C-39 source)**: V-01 C-36 block labels itself `STRUCTURAL MANDATE (C-36)`
  with criterion ID embedded -- scorer traces mandate to criterion bidirectionally without
  table lookup. C-26 and C-36 already follow identical syntax. C-39 formalizes this as a
  general property: every STRUCTURAL MANDATE block carries inline criterion ID.

- **Pattern 2 (C-40 source)**: V-01 C-36 block closes with "A scorer confirms C-33
  compliance by label presence alone without parsing surrounding definition bullets."
  C-40 formalizes this as a required element of every STRUCTURAL MANDATE block.

- **Pattern 3 (C-41 source)**: C-26 and C-36 happen to follow identical syntax -- the
  parallelism is emergent. C-41 upgrades from parallel-in-practice to parallel-by-contract
  by declaring the canonical template explicitly so all blocks conform to a single declared
  form; additional mandates are mechanically derivable.

**R12 variation axes**:

- **V-01 (single axis: C-41)**: Canonical STRUCTURAL MANDATE template declared before
  Phase Label Schema. All existing blocks (C-26, C-36) verified to conform. C-39 passes
  by contract; C-40 absent; C-37/C-38 still FAIL.

- **V-02 (single axis: C-40)**: Scorer confirmation heuristic added to every STRUCTURAL
  MANDATE block. C-39 passes by inheritance (blocks already carry inline IDs from R11).
  C-41 absent; C-37/C-38 still FAIL.

- **V-03 (single axis: C-37 + C-38)**: DefectCodeVocab extended with DEFECT:
  COUNT-MISMATCH and DEFECT: EMPTY-CELL. COUNT GATE and PRE-READ GATE upgraded to
  defect-emitting. Both carry STRUCTURAL MANDATE (C-37) / STRUCTURAL MANDATE (C-38)
  blocks. C-40 absent; C-41 absent.

- **V-04 (combined: C-37 + C-38 + C-41)**: Gate defect emission + canonical template.
  C-39 confirmed by contract; C-40 absent.

- **V-05 (combined: C-37 + C-38 + C-39 + C-40 + C-41)**: Complete R12 ceiling. Canonical
  template + scorer heuristics + defect-emitting gates. All five new targets integrated.

All five variations inherit the full R11 V-01 architecture:
- Phase Label Schema table before trace content (C-14)
- Defect Classification Registry before Phase 1 (C-29, C-30)
- DefectCodeVocab CLOSED TYPE with Independence Statement (C-33, C-36)
- GATHER: spec inputs first (C-11), Coverage Matrix (C-09), BLOCKED rule (C-12), CLOSED
  ASSERTION with closure terminus (C-20, C-23, C-26)
- BIND: Conflict Precedence Rule (C-17), typed columns with (TypeName) annotations (C-28),
  Status (StatusVocab) (C-16), Precedence applied (PrecedenceVocabulary) (C-19, C-22, C-25)
- EXECUTE: delimiter markers (C-13), Relay Schema with Binding pairs (C-18), anti-pattern
  prohibition row with VIOLATION (C-21, C-24), RequiredVocabulary (C-27)
- VERDICT: PRE-READ GATE structurally ordered (C-35), C-29 Audit Block at top (C-32),
  C-28 COUNT GATE as binary self-evaluating gate (C-34), Compliance Ledger as structured
  table with ID | Result | Evidence | Defect code columns (C-15, C-07, C-31)

---

## V-01 -- Single axis: C-41 (canonical STRUCTURAL MANDATE template declared)

**Axis**: Lifecycle emphasis -- the canonical `STRUCTURAL MANDATE` template is declared
as the first named element of the prompt, before the Phase Label Schema and before any
trace content. All existing STRUCTURAL MANDATE blocks (C-26, C-36) are verified to
conform to the declared form. Any block whose header does not match
`STRUCTURAL MANDATE (C-XX)` syntax is structurally malformed by the declared template.

**Hypothesis**: R11 V-01 has two STRUCTURAL MANDATE blocks (C-26 and C-36) that happen
to use identical `STRUCTURAL MANDATE (C-XX)` syntax -- the parallelism is emergent from
individual block design. C-41 requires the canonical form to be declared explicitly so
conformance is checkable against a single structural template rather than by comparing
each block to C-36's block. Declaring the template first also makes C-39 pass by
contract: a scorer confirming C-39 reads the canonical template, then verifies each
block's header matches the `STRUCTURAL MANDATE (C-XX)` pattern -- the ID match is the
gate, not a check requiring block-by-block comparison. C-40 is not targeted: no scorer
confirmation heuristic is added to block bodies. C-37 and C-38 are not fixed: COUNT GATE
and PRE-READ GATE remain prose-only with no defect emission.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template

All STRUCTURAL MANDATE blocks in this prompt conform to this template. Any block whose
header does not match `STRUCTURAL MANDATE (C-XX)` syntax is structurally malformed.

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
```

Additional mandates are mechanically derivable from this template by substituting the
governing criterion ID and the element description.

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

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab)  | Mandate violated                                  | Structural consequence                           |
|--------------------------------|---------------------------------------------------|--------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION   | Coverage Matrix closure -- Required=YES input absent | Trace halts; no partial execution                |

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
|-------|------------|-----------------|---------------|---------------------|------------------------------------------|

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
|---------------------------|--------|----------------------------------------|---------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

Each Binding cell carries an explicit `` `InputName = "ResolvedValue"` `` pair. The
resolved value is stated in the relay itself so Verdict can verify without re-reading BIND.

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order is
mandated: no ledger row may be read until all three checks clear.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Report violation. Do not proceed until gate clears.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed: [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across BIND and
EXECUTE relay schema and the Defect Classification Registry and the Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE `mismatch`

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|---------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-33 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-02 -- Single axis: C-40 (scorer confirmation heuristic in every STRUCTURAL MANDATE block)

**Axis**: Phrasing register -- every STRUCTURAL MANDATE block closes with an explicit
scorer confirmation heuristic of the form "A scorer confirms [Criterion] compliance by
[specific method] alone without [parsing alternative]." The block is self-scoring: the
prompt documents how compliance is confirmed, eliminating scorer judgment about what
constitutes evidence.

**Hypothesis**: R11 V-01 embeds a scorer heuristic in the C-36 block but not in the C-26
block. C-40 requires the heuristic in EVERY block. Extending the heuristic to C-26 is
straightforward: "A scorer confirms C-26 compliance by closure terminus line presence
alone without parsing the CLOSED ASSERTION block content." Adding heuristics to the gate
blocks (C-37, C-38) would require those blocks to exist -- but this variation does NOT fix
C-37/C-38, so no gate heuristics appear. C-41 is not targeted: no canonical template is
declared. C-40 is satisfied for all existing blocks (C-26, C-36). Risk: the heuristic for
C-26 must describe a specific observable indicator ("closure terminus line presence") not
a paraphrase of the criterion text -- if the heuristic is too general it satisfies C-40
in form but not in specificity.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

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

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab)  | Mandate violated                                  | Structural consequence                           |
|--------------------------------|---------------------------------------------------|--------------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION   | Coverage Matrix closure -- Required=YES input absent | Trace halts; no partial execution                |

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
and stop.

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
Record `override`. When the invocation supplies a value absent from the spec, record
`default`. When input is BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|---------------|---------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|----------------------------------------|---------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Report violation. Do not proceed.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed: [YES / NO]

### C-28 COUNT GATE

Typed annotation sites: all columns of the form `ColumnName (TypeName)` across BIND,
EXECUTE relay schema, Defect Classification Registry, and Compliance Ledger.

Expected: [N]
Actual: [N]

IF actual == expected THEN `confirmed` ELSE `mismatch`

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|---------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by STRUCTURAL MANDATE (C-36) block-header presence
> alone without parsing the mandate body content.

---

## V-03 -- Single axis: C-37 + C-38 (defect-emitting gates)

**Axis**: Lifecycle emphasis -- the COUNT GATE and PRE-READ GATE are upgraded from
ordering-only gates to defect-emitting gates. DefectCodeVocab is extended with
`DEFECT: COUNT-MISMATCH` and `DEFECT: EMPTY-CELL`. Each gate carries a
STRUCTURAL MANDATE block that names the emitted defect code. Gate violations become
ledger-traceable by defect code without re-reading the gate block.

**Hypothesis**: R11 V-01 COUNT GATE resolves to `confirmed` or `mismatch` -- the
`mismatch` branch is a prose outcome with no DefectCodeVocab citation. Similarly, the
PRE-READ GATE says "HALT and report violation" but does not emit a named defect code.
The fix is additive: extend DefectCodeVocab with two new codes, update each gate's ELSE
branch to name the emitted code, add STRUCTURAL MANDATE (C-37) / STRUCTURAL MANDATE (C-38)
blocks following the C-26/C-36 pattern. C-37 requires the gate block to emit a
DefectCodeVocab-coded defect when it fires; C-38 requires the same for the PRE-READ GATE.
C-40 is not targeted: blocks carry no scorer confirmation heuristic. C-41 is not targeted:
no canonical template is declared.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

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

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH,
DEFECT: EMPTY-CELL}`

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

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override`. When the invocation supplies a value absent from the spec, record
`default`. When input is BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|---------------|---------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|----------------------------------------|---------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. Structural order mandated:
no ledger row may be read until all three checks clear.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column of the
Compliance Ledger. Do not read ledger until gate clears.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.

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

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|---------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-33 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-04 -- Combined: C-37 + C-38 + C-41 (defect-emitting gates + canonical template)

**Axis**: Lifecycle emphasis -- combines V-01's canonical template declaration with V-03's
defect-emitting gate upgrades. All existing and new STRUCTURAL MANDATE blocks conform to
the canonical template by contract. C-39 passes mechanically: a scorer verifying C-39
reads the canonical template, then confirms each block header matches `STRUCTURAL MANDATE
(C-XX)` -- the pattern is the gate, not block-by-block comparison. C-40 is not targeted:
no scorer confirmation heuristic added to block bodies.

**Hypothesis**: V-04 integrates two independent axes that do not interact structurally --
the canonical template (C-41) does not change gate behavior, and the gate defect emission
(C-37, C-38) does not change the template. Combining them in V-04 tests whether the two
axes compose cleanly: the new STRUCTURAL MANDATE (C-37) and STRUCTURAL MANDATE (C-38)
blocks must conform to the canonical template, which they do by construction (they follow
the same `> STRUCTURAL MANDATE (C-XX): [element]... Reproduce it exactly as shown.` form).
C-40 is the remaining gap: blocks close with defect emission but not with a scorer
heuristic. Risk: the canonical template section may add cognitive weight before the Phase
Label Schema; the tracer must register the template before seeing any content. Mitigation:
the canonical template section is short (4 lines) and is structurally distinct from trace
instructions.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template

All STRUCTURAL MANDATE blocks in this prompt conform to this template. Any block whose
header does not match `STRUCTURAL MANDATE (C-XX)` syntax is structurally malformed.

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
```

Additional mandates are mechanically derivable from this template by substituting the
governing criterion ID and the element description.

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

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH,
DEFECT: EMPTY-CELL}`

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

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

The following inputs are the complete and exhaustive set for this invocation. No inputs
exist outside this list.

| Input | Required | Gap |
|-------|----------|-----|

**BLOCKED rule**: If any Required=YES input has Gap=YES, write
`BLOCKED: [InputName] is required and absent. Trace halts. DEFECT: OPEN-WORLD-ASSERTION`
and stop.

**CLOSED ASSERTION block**:

Required inputs covered: [name each Required=YES input explicitly]

Coverage Matrix is CLOSED for this invocation.

> STRUCTURAL MANDATE (C-26): `Coverage Matrix is CLOSED for this invocation.` is a named
> structural mandate of this prompt. Reproduce it exactly as shown.

---

## BIND

**Conflict Precedence Rule**: When Spec Value and Invocation Value disagree, spec anchors.
Record `override`. When the invocation supplies absent values, record `default`. When
BLOCKED, record `BLOCKED`.

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|---------------|---------------------|------------------------------------------|

---

## EXECUTE

Produce the complete artifact. No elision. No placeholder sections.

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

After the artifact, produce the Relay:

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|----------------------------------------|---------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

---

## VERDICT

### PRE-READ GATE

Run phases (a), (b), (c) BEFORE reading the compliance ledger. No ledger row may be read
until all three checks clear.

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column. Do not
proceed.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.

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

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|---------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-33 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.

---

## V-05 -- Combined: C-37 + C-38 + C-39 + C-40 + C-41 (complete R12 ceiling)

**Axis**: Lifecycle emphasis + phrasing register -- canonical STRUCTURAL MANDATE template
declared; all blocks carry inline criterion IDs (C-39 by contract); all blocks close with
scorer confirmation heuristic (C-40); COUNT GATE and PRE-READ GATE emit DefectCodeVocab-
coded defects (C-37, C-38). Full R12 integration.

**Hypothesis**: V-05 integrates all five R12 targets in a single prompt body. The canonical
template (C-41) is declared first: all subsequent STRUCTURAL MANDATE blocks are derivable
from it by mechanical substitution, making C-39 a structural property rather than an
emergent pattern. The scorer confirmation heuristic (C-40) in every block self-documents
the confirmation method, closing the evaluation loop at each mandate site. Gate defect
emission (C-37, C-38) makes both gate violations ledger-traceable by code. The five axes
compose without conflict: the canonical template adds four lines before the Phase Label
Schema; the scorer heuristics add one closing line per block; the gate defect codes add
one emission statement per gate. No axis degrades prior passing criteria. The only
structural risk is annotation site count: adding STRUCTURAL MANDATE (C-37) and STRUCTURAL
MANDATE (C-38) blocks may not add new typed columns (they use prose, not tables), so the
C-28 COUNT GATE expected count stays the same as R11 V-01. The scorer confirms this by
re-counting typed columns in BIND, EXECUTE, Registry, and Ledger -- the gate blocks
themselves do not introduce new (TypeName)-annotated columns.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template

All STRUCTURAL MANDATE blocks in this prompt conform to this template. Any block whose
header does not match `STRUCTURAL MANDATE (C-XX)` syntax is structurally malformed. A
scorer confirms any block's well-formedness by checking its header against this template
without reading neighboring blocks.

```
> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].
```

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

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH,
DEFECT: EMPTY-CELL}`

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
|-------|------------|-----------------|---------------|---------------------|------------------------------------------|

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
|---------------------------|--------|----------------------------------------|---------------------|
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
|------|--------|---------|-------------------------------|

PASS rows: Defect code = `--`
FAIL rows: Defect code = value from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by STRUCTURAL MANDATE (C-36) block-header presence
> alone without parsing the mandate body.
