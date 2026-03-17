---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 18
rubric: trace-skill-rubric-v17-2026-03-15.md
---

# trace-skill Variations -- Round 18

## Entry State Analysis

R17 V-05 passes C-01 through C-50. R17 introduced and achieved three new excellence patterns as
candidate criteria, now formalized in rubric v17:

- **C-51**: ASR CLOSED ASSERTION terminus declared as `STRUCTURAL MANDATE (C-49+)` -- parallels
  C-26's Coverage Matrix closure terminus discipline. R17 V-01 adds the terminus block but the
  independence statement (TCR component 4) is embedded within the verification sentence rather than
  stated as a structurally separate component. C-51's scorer confirmation path ("locate a
  STRUCTURAL MANDATE block within the ASR section that names C-49 or C-49+") works on R17 V-01
  output, but the block is only partially canonical -- it satisfies C-40 and C-41 in merged form,
  not independently.

- **C-52**: SCORER HEURISTIC steps use `-> confirms C-NN (C-NN)` binding operator. R17 V-02
  introduces the `->` operator but step (b) carries two `-> confirms` operators on two sub-lines
  under a single step heading. The field-split-on-`->` extraction path described in C-52 is
  ambiguous for step (b): a naive field splitter sees three tokens where the rubric contract
  expects each step to produce exactly one confirmation target and one governing criterion.

- **C-53**: Phase Label Schema registered as TCR Component 6 with inline `(C-14)` citation. R17
  V-03/V-05 implement this correctly. No structural gap identified -- R18 V-03 confirms the
  implementation is stable and SCORER HEURISTIC step (d) is coherent.

R18 upgrade axes:

- **V-01 (single: C-51)**: Fully canonical STRUCTURAL MANDATE (C-49+) -- independence statement
  separated from verification instruction as a structurally distinct named element so each of the
  four TCR mandate-template components is individually present and independently readable.

- **V-02 (single: C-52)**: One-step-one-operator discipline -- step (b) split into two numbered
  steps (b) and (c) so every step carries exactly one `-> confirms C-NN (C-NN)` operator, making
  the extraction path unambiguous by field-split-on-`->` without sub-line parsing.

- **V-03 (single: C-53)**: TCR Component 6 confirmation -- PLS at TCR row 6 with `(C-14)` inline
  citation, SCORER HEURISTIC step (d) added with parenthetical `(C-14)` citation (C-52 not
  active), ANTI-PATTERN row updated to name PHASE LABEL SCHEMA omission. Confirms C-53 is
  independently achievable without C-51 or C-52.

- **V-04 (combined: C-51 + C-52)**: Fully canonical ASR terminus mandate + one-step-one-operator
  SCORER HEURISTIC. TCR has 5 components. Hypothesis: the two structural upgrades are
  compositionally independent -- the mandate block isolation and the step isolation solve
  different ambiguity sites without interfering.

- **V-05 (combined: C-51 + C-52 + C-53)**: All three axes. TCR has 6 components. The tightest
  integration -- SCORER HEURISTIC has steps (a)-(e), each carrying one `-> confirms` operator,
  ASR carries a fully canonical closure mandate, PLS is TCR-registered.

All five inherit the full R17 V-05 baseline: DCR, canonical STRUCTURAL MANDATE template, TCR,
Phase Label Schema, Conflict Precedence Rule, Relay Schema, GATHER/BIND/EXECUTE/VERDICT phases,
PRE-READ GATE, C-29 audit, compliance ledger, COUNT GATE, ASR with 6 rows including self-
registration row.

---

## V-01: Single Axis -- C-51 (Fully Canonical STRUCTURAL MANDATE (C-49+))

**Axis**: Lifecycle emphasis
**Hypothesis**: R17 V-01's STRUCTURAL MANDATE (C-49+) block has the independence statement
merged into the verification instruction sentence ("without counting rows or consulting an
external enumeration" appended to the scorer heuristic line). TCR component 4 (INDEPENDENCE
STATEMENT) requires it to be independently stated -- "compliance is verifiable without consulting
other sections." Separating it into a structurally distinct sentence makes the block a full
canonical template instance: all four TCR components present as independent readable elements.
A scorer confirming C-51 by "locating a STRUCTURAL MANDATE block that names C-49+" now also
sees a block that satisfies the canonical template conformance-collapse check without extra
inspection.

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here. This registry is INDEPENDENT of the compliance ledger -- a scorer
> confirms C-36 compliance by verifying this registry appears before the GATHER phase header and
> carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any other section.

| Defect code (DefectCodeVocab) | Meaning |
|-------------------------------|---------|
| OPEN-WORLD-ASSERTION | Coverage Matrix claims inputs not enumerated in the closed world |
| ELISION-MARKER | Artifact body contains ellipsis or placeholder instead of full content |
| EMPTY-CELL | Compliance ledger cell is blank; no PASS / FAIL / N/A sentinel present |
| COUNT-MISMATCH | Annotation site count in COUNT GATE does not match ASR row count |
| UNRESOLVED-INPUT | Bind table contains UNRESOLVED row and trace proceeded past BIND |
| BLOCKED-TRACE | Bind table contains BLOCKED row; trace must halt and emit this defect |
| OPEN-ASR | ASR closure terminus absent or not mandated by a STRUCTURAL MANDATE (C-49+) block |

---

### CANONICAL STRUCTURAL MANDATE TEMPLATE

> CONFORMANCE-COLLAPSE CLAIM: Every STRUCTURAL MANDATE block in this prompt is an instance of the
> Canonical STRUCTURAL MANDATE Template declared here. A scorer confirms global structural
> conformance by verifying the Template Component Registry rows are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) locating the Template Component Registry (C-41);
  (b) verifying ANNOTATION SCOPE REGISTRY appears at TCR row 5 with `(C-47)` notation (C-47), and
      that the row cites `C-47` by name in the row label -- not implied through row-number sequence
      (C-48);
  (c) reading the CONFORMANCE-COLLAPSE CLAIM's stated heuristic (C-43);
without inspecting individual STRUCTURAL MANDATE block bodies.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | Separate sentence stating compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that omits the independence statement, or that merges
> the independence statement into the verification instruction sentence rather than stating it as
> a structurally separate sentence, is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION
> at the mandate site.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section headers
> exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without variation.
> Compliance is verifiable without consulting any other section of the trace.

| Phase | Header label |
|-------|-------------|
| 1 | ## GATHER |
| 2 | ## BIND |
| 3 | ## EXECUTE |
| 4 | ## VERDICT |

---

### CONFLICT PRECEDENCE RULE

> STRUCTURAL MANDATE (C-17): When a value appears in both the skill spec and the test invocation,
> the test invocation wins. When a value appears only in the skill spec, the skill spec value is
> used.
> A scorer confirms C-17 compliance by verifying the Bind table carries a
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill spec.
> Compliance is verifiable from the EXECUTE section alone without consulting earlier phases.

| Field | Required (RequiredVocabulary) |
|-------|-------------------------------|
| Role | YES |
| Signal | YES |
| Binding | YES |
| Status | YES |
| Evidence | YES |

Binding pairs use format: `InputName = "ResolvedValue"`

> ANTI-PATTERN (VIOLATION): A relay block that uses `InputName: ResolvedValue` (colon notation)
> instead of `InputName = "ResolvedValue"` (equals-quote notation) is a binding pair violation and
> emits DEFECT: OPEN-WORLD-ASSERTION at the relay site.

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter markers
> `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted inside the
> artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...` or
> `[continued]` or similar placeholder appears between them. Violation emits DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes `[ARTIFACT BEGINS HERE]`.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

---

## GATHER

Enumerate all inputs. Skill spec inputs first. Test invocation inputs second. Build the Coverage
Matrix with every named input as a row.

| Input name | Source | Value summary |
|------------|--------|---------------|
| (one row per named input from spec and invocation) | | |

> STRUCTURAL MANDATE (C-26): After the Coverage Matrix table, emit the following closure terminus
> exactly as shown.
> A scorer confirms C-26 compliance by locating this exact line after the Coverage Matrix table.
> Compliance is verifiable from the GATHER section alone without consulting BIND or EXECUTE.

**CLOSED WORLD DECLARATION**: The inputs enumerated in the Coverage Matrix above are the complete
and closed set of inputs for this trace. No input referenced in BIND or EXECUTE may appear that
does not have a row in this table.

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name not
> present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input row
will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence Rule.

| Input name | Resolved value | Status | Precedence applied (PrecedenceVocabulary) |
|------------|----------------|--------|-------------------------------------------|
| (one row per Coverage Matrix input) | | RESOLVED / UNRESOLVED / BLOCKED | |

**Status** is a three-value enum: `RESOLVED` | `UNRESOLVED` | `BLOCKED`

> If any row carries status BLOCKED, halt the trace immediately and emit DEFECT: BLOCKED-TRACE.
> Do not proceed to EXECUTE.

---

## EXECUTE

For each role in the skill spec, emit one relay block following the Relay Schema. Then emit the
complete artifact.

Relay block format:

```
Role: <role name>
Signal: <signal this role emits>
Binding: <InputName = "ResolvedValue"> pairs
Status: READY | BLOCKED
Evidence: <one sentence confirming binding is complete>
```

After all relay blocks:

[ARTIFACT BEGINS HERE]

<full artifact content -- no elision markers permitted>

[ARTIFACT ENDS HERE]

---

## VERDICT

**C-29 AUDIT BLOCK**:
1. All Coverage Matrix rows visited in BIND: YES / NO
2. All relay blocks emitted before artifact delimiters: YES / NO
3. Artifact delimiters present and no elision markers inside: YES / NO

> PRE-READ GATE: Before filling the compliance ledger, scan every cell in the table below. If any
> cell is blank (no PASS, no FAIL, no N/A, no -- sentinel), emit DEFECT: EMPTY-CELL at that row
> before continuing. A scorer confirms PRE-READ GATE compliance by verifying no blank cells exist
> in the ledger.

**Compliance ledger**:

| ID | Criterion | Result | Evidence | Defect code (DefectCodeVocab) |
|----|-----------|--------|----------|-------------------------------|
| C-01 | Skill spec input present | PASS / FAIL / N/A | | -- |
| C-02 | Test invocation input present | PASS / FAIL / N/A | | -- |
| C-03 | Coverage Matrix complete | PASS / FAIL / N/A | | -- |
| C-04 | CLOSED WORLD DECLARATION present | PASS / FAIL / N/A | | -- |
| C-05 | CLOSED ASSERTION present | PASS / FAIL / N/A | | -- |
| C-06 | Bind table Status column present | PASS / FAIL / N/A | | -- |
| C-07 | Bind table PrecedenceVocabulary column present | PASS / FAIL / N/A | | -- |
| C-08 | No BLOCKED rows in Bind table | PASS / FAIL / N/A | | -- |
| ... | (continue for all applicable criteria through C-53) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column in
> this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against the
> ASR row count.
> Compliance is verifiable from the COUNT GATE section alone without consulting other tables.

**ANNOTATION SCOPE REGISTRY**:

| Row | Annotation site | Typed column | Required (RequiredVocabulary) |
|-----|-----------------|--------------|-------------------------------|
| 1 | Bind table | Precedence applied (PrecedenceVocabulary) | YES |
| 2 | Relay Schema | Required (RequiredVocabulary) | YES |
| 3 | Defect Classification Registry | Defect code (DefectCodeVocab) | YES |
| 4 | Verdict compliance ledger | Defect code (DefectCodeVocab) | YES |
| 5 | Template Component Registry | Required (RequiredVocabulary) | YES |
| 6 | ANNOTATION SCOPE REGISTRY | Required (RequiredVocabulary) | YES |

> STRUCTURAL MANDATE (C-49+): The `ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.`
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-51 compliance by locating a STRUCTURAL MANDATE block within the ASR section
> that names C-49 (or C-49+) as the governing criterion without parsing the registry rows.
> Compliance is verifiable from the ASR section alone without consulting the Coverage Matrix or
> compliance ledger.

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-02: Single Axis -- C-52 (One-Step-One-Operator Discipline)

**Axis**: Output format
**Hypothesis**: R17 V-02 uses the `-> confirms C-NN (C-NN)` operator correctly for steps (a) and
(c), but step (b) carries two `-> confirms` operators on two sub-lines under one step letter. A
field-splitter on `->` sees three tokens for step (b) -- one action prefix and two `confirms C-NN
(C-NN)` suffixes -- requiring sub-line parsing to attribute each operator to its criterion. C-52's
machine-readable contract is one binding per split: extractable by `->` field-split alone.
Splitting the two-criterion step into two independent lettered steps (b) and (c) gives each
criterion exactly one step-line, one `->` operator, one confirmation target, and one governing
criterion -- pure field-split extraction with no sub-line disambiguation.

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here. This registry is INDEPENDENT of the compliance ledger -- a scorer
> confirms C-36 compliance by verifying this registry appears before the GATHER phase header and
> carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any other section.

| Defect code (DefectCodeVocab) | Meaning |
|-------------------------------|---------|
| OPEN-WORLD-ASSERTION | Coverage Matrix claims inputs not enumerated in the closed world |
| ELISION-MARKER | Artifact body contains ellipsis or placeholder instead of full content |
| EMPTY-CELL | Compliance ledger cell is blank; no PASS / FAIL / N/A sentinel present |
| COUNT-MISMATCH | Annotation site count in COUNT GATE does not match ASR row count |
| UNRESOLVED-INPUT | Bind table contains UNRESOLVED row and trace proceeded past BIND |
| BLOCKED-TRACE | Bind table contains BLOCKED row; trace must halt and emit this defect |

---

### CANONICAL STRUCTURAL MANDATE TEMPLATE

> CONFORMANCE-COLLAPSE CLAIM: Every STRUCTURAL MANDATE block in this prompt is an instance of the
> Canonical STRUCTURAL MANDATE Template declared here. A scorer confirms global structural
> conformance by verifying the Template Component Registry rows are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
  (c) Verify the TCR row 5 label cites `C-47` by name -- not implied through row-number sequence -> confirms C-48 (C-48)
  (d) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
without inspecting individual STRUCTURAL MANDATE block bodies.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | States that compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that contains only a scope statement without a scorer
> verification instruction, or that omits the independence statement, or that omits the ANNOTATION
> SCOPE REGISTRY row from the TCR, is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at
> the mandate site.

> SCORER HEURISTIC STEP FORMAT: Each step in the SCORER HEURISTIC body follows the pattern:
> `(letter) Action phrase -> confirms C-NN (C-NN)` on a single line. The `->` operator separates
> the confirmation action from the criterion binding. Field-split on `->` yields exactly two tokens:
> [action, `confirms C-NN (C-NN)`]. A step that carries more than one `->` operator, or whose
> `-> confirms` appears on a sub-line rather than the step-letter line, violates the one-step-one-
> operator discipline and is non-conforming.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section headers
> exactly as shown. A scorer confirms C-14 compliance by verifying all four headers appear in order
> without variation.

| Phase | Header label |
|-------|-------------|
| 1 | ## GATHER |
| 2 | ## BIND |
| 3 | ## EXECUTE |
| 4 | ## VERDICT |

---

### CONFLICT PRECEDENCE RULE

> STRUCTURAL MANDATE (C-17): When a value appears in both the skill spec and the test invocation,
> the test invocation wins. When a value appears only in the skill spec, the skill spec value is
> used. A scorer confirms C-17 compliance by verifying the Bind table carries a
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence token.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.

| Field | Required (RequiredVocabulary) |
|-------|-------------------------------|
| Role | YES |
| Signal | YES |
| Binding | YES |
| Status | YES |
| Evidence | YES |

Binding pairs use format: `InputName = "ResolvedValue"`

> ANTI-PATTERN (VIOLATION): A relay block that uses `InputName: ResolvedValue` (colon notation)
> instead of `InputName = "ResolvedValue"` (equals-quote notation) is a binding pair violation and
> emits DEFECT: OPEN-WORLD-ASSERTION at the relay site.

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter markers
> `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted inside the
> artifact body. A scorer confirms C-24 compliance by verifying both delimiter markers are present
> and no `...` or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.

---

## GATHER

Enumerate all inputs. Skill spec inputs first. Test invocation inputs second. Build the Coverage
Matrix with every named input as a row.

| Input name | Source | Value summary |
|------------|--------|---------------|
| (one row per named input from spec and invocation) | | |

> STRUCTURAL MANDATE (C-26): After the Coverage Matrix table, emit the following closure terminus
> exactly as shown. A scorer confirms C-26 compliance by locating this exact line after the Coverage
> Matrix table.

**CLOSED WORLD DECLARATION**: The inputs enumerated in the Coverage Matrix above are the complete
and closed set of inputs for this trace. No input referenced in BIND or EXECUTE may appear that
does not have a row in this table.

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name not
> present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input row
will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence Rule.

| Input name | Resolved value | Status | Precedence applied (PrecedenceVocabulary) |
|------------|----------------|--------|-------------------------------------------|
| (one row per Coverage Matrix input) | | RESOLVED / UNRESOLVED / BLOCKED | |

**Status** is a three-value enum: `RESOLVED` | `UNRESOLVED` | `BLOCKED`

> If any row carries status BLOCKED, halt the trace immediately and emit DEFECT: BLOCKED-TRACE.
> Do not proceed to EXECUTE.

---

## EXECUTE

For each role in the skill spec, emit one relay block following the Relay Schema. Then emit the
complete artifact.

Relay block format:

```
Role: <role name>
Signal: <signal this role emits>
Binding: <InputName = "ResolvedValue"> pairs
Status: READY | BLOCKED
Evidence: <one sentence confirming binding is complete>
```

After all relay blocks:

[ARTIFACT BEGINS HERE]

<full artifact content -- no elision markers permitted>

[ARTIFACT ENDS HERE]

---

## VERDICT

**C-29 AUDIT BLOCK**:
1. All Coverage Matrix rows visited in BIND: YES / NO
2. All relay blocks emitted before artifact delimiters: YES / NO
3. Artifact delimiters present and no elision markers inside: YES / NO

> PRE-READ GATE: Before filling the compliance ledger, scan every cell in the table below. If any
> cell is blank (no PASS, no FAIL, no N/A, no -- sentinel), emit DEFECT: EMPTY-CELL at that row
> before continuing. A scorer confirms PRE-READ GATE compliance by verifying no blank cells exist
> in the ledger.

**Compliance ledger**:

| ID | Criterion | Result | Evidence | Defect code (DefectCodeVocab) |
|----|-----------|--------|----------|-------------------------------|
| C-01 | Skill spec input present | PASS / FAIL / N/A | | -- |
| C-02 | Test invocation input present | PASS / FAIL / N/A | | -- |
| C-03 | Coverage Matrix complete | PASS / FAIL / N/A | | -- |
| C-04 | CLOSED WORLD DECLARATION present | PASS / FAIL / N/A | | -- |
| C-05 | CLOSED ASSERTION present | PASS / FAIL / N/A | | -- |
| C-06 | Bind table Status column present | PASS / FAIL / N/A | | -- |
| C-07 | Bind table PrecedenceVocabulary column present | PASS / FAIL / N/A | | -- |
| C-08 | No BLOCKED rows in Bind table | PASS / FAIL / N/A | | -- |
| ... | (continue for all applicable criteria through C-52) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column in
> this trace. A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly
> against the ASR row count.

**ANNOTATION SCOPE REGISTRY**:

| Row | Annotation site | Typed column | Required (RequiredVocabulary) |
|-----|-----------------|--------------|-------------------------------|
| 1 | Bind table | Precedence applied (PrecedenceVocabulary) | YES |
| 2 | Relay Schema | Required (RequiredVocabulary) | YES |
| 3 | Defect Classification Registry | Defect code (DefectCodeVocab) | YES |
| 4 | Verdict compliance ledger | Defect code (DefectCodeVocab) | YES |
| 5 | Template Component Registry | Required (RequiredVocabulary) | YES |
| 6 | ANNOTATION SCOPE REGISTRY | Required (RequiredVocabulary) | YES |

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-03: Single Axis -- C-53 (Phase Label Schema as TCR Component 6 with (C-14) Citation)

**Axis**: Role sequence / TCR extension
**Hypothesis**: R17 V-03 added PLS as TCR Component 6 with `(C-14)` notation and added SCORER
HEURISTIC step (d) to confirm it. R18 confirms this implementation satisfies C-53 as a
standalone criterion (without C-51 or C-52 active). The ANTI-PATTERN row in the canonical
template block is updated to name PHASE LABEL SCHEMA omission as a collapse condition, making
PLS omission from TCR independently citable without reading all 6 TCR rows. Step (d) uses
parenthetical `(C-14)` citation (not `->` operator -- C-52 not active in this variation).

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here. This registry is INDEPENDENT of the compliance ledger -- a scorer
> confirms C-36 compliance by verifying this registry appears before the GATHER phase header and
> carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any other section.

| Defect code (DefectCodeVocab) | Meaning |
|-------------------------------|---------|
| OPEN-WORLD-ASSERTION | Coverage Matrix claims inputs not enumerated in the closed world |
| ELISION-MARKER | Artifact body contains ellipsis or placeholder instead of full content |
| EMPTY-CELL | Compliance ledger cell is blank; no PASS / FAIL / N/A sentinel present |
| COUNT-MISMATCH | Annotation site count in COUNT GATE does not match ASR row count |
| UNRESOLVED-INPUT | Bind table contains UNRESOLVED row and trace proceeded past BIND |
| BLOCKED-TRACE | Bind table contains BLOCKED row; trace must halt and emit this defect |

---

### CANONICAL STRUCTURAL MANDATE TEMPLATE

> CONFORMANCE-COLLAPSE CLAIM: Every STRUCTURAL MANDATE block in this prompt is an instance of the
> Canonical STRUCTURAL MANDATE Template declared here. A scorer confirms global structural
> conformance by verifying the Template Component Registry rows 1-6 are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) locating the Template Component Registry (C-41);
  (b) verifying ANNOTATION SCOPE REGISTRY appears at TCR row 5 with `(C-47)` notation (C-47), and
      that the row cites `C-47` by name in the row label -- not implied through row-number sequence
      (C-48);
  (c) reading the CONFORMANCE-COLLAPSE CLAIM's stated heuristic (C-43);
  (d) verifying the PHASE LABEL SCHEMA appears as TCR row 6 with `(C-14)` notation (C-14) by TCR
      row lookup alone without parsing prompt structure;
without inspecting individual STRUCTURAL MANDATE block bodies.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | States that compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |
| 6 (C-14): PHASE LABEL SCHEMA | Immutable 4-phase table declared before GATHER, carrying phase header labels ## GATHER / ## BIND / ## EXECUTE / ## VERDICT | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that omits the independence statement, or that omits
> the ANNOTATION SCOPE REGISTRY row from the TCR, or that omits the PHASE LABEL SCHEMA row from
> the TCR, is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate site.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section headers
> exactly as shown. A scorer confirms C-14 compliance by verifying all four headers appear in order
> without variation.

| Phase | Header label |
|-------|-------------|
| 1 | ## GATHER |
| 2 | ## BIND |
| 3 | ## EXECUTE |
| 4 | ## VERDICT |

---

### CONFLICT PRECEDENCE RULE

> STRUCTURAL MANDATE (C-17): When a value appears in both the skill spec and the test invocation,
> the test invocation wins. When a value appears only in the skill spec, the skill spec value is
> used. A scorer confirms C-17 compliance by verifying the Bind table carries a
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence token.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.

| Field | Required (RequiredVocabulary) |
|-------|-------------------------------|
| Role | YES |
| Signal | YES |
| Binding | YES |
| Status | YES |
| Evidence | YES |

Binding pairs use format: `InputName = "ResolvedValue"`

> ANTI-PATTERN (VIOLATION): A relay block that uses `InputName: ResolvedValue` (colon notation)
> instead of `InputName = "ResolvedValue"` (equals-quote notation) is a binding pair violation and
> emits DEFECT: OPEN-WORLD-ASSERTION at the relay site.

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter markers
> `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted inside the
> artifact body. A scorer confirms C-24 compliance by verifying both delimiter markers are present
> and no `...` or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.

---

## GATHER

Enumerate all inputs. Skill spec inputs first. Test invocation inputs second. Build the Coverage
Matrix with every named input as a row.

| Input name | Source | Value summary |
|------------|--------|---------------|
| (one row per named input from spec and invocation) | | |

> STRUCTURAL MANDATE (C-26): After the Coverage Matrix table, emit the following closure terminus
> exactly as shown. A scorer confirms C-26 compliance by locating this exact line after the Coverage
> Matrix table.

**CLOSED WORLD DECLARATION**: The inputs enumerated in the Coverage Matrix above are the complete
and closed set of inputs for this trace. No input referenced in BIND or EXECUTE may appear that
does not have a row in this table.

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name not
> present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input row
will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence Rule.

| Input name | Resolved value | Status | Precedence applied (PrecedenceVocabulary) |
|------------|----------------|--------|-------------------------------------------|
| (one row per Coverage Matrix input) | | RESOLVED / UNRESOLVED / BLOCKED | |

**Status** is a three-value enum: `RESOLVED` | `UNRESOLVED` | `BLOCKED`

> If any row carries status BLOCKED, halt the trace immediately and emit DEFECT: BLOCKED-TRACE.
> Do not proceed to EXECUTE.

---

## EXECUTE

For each role in the skill spec, emit one relay block following the Relay Schema. Then emit the
complete artifact.

Relay block format:

```
Role: <role name>
Signal: <signal this role emits>
Binding: <InputName = "ResolvedValue"> pairs
Status: READY | BLOCKED
Evidence: <one sentence confirming binding is complete>
```

After all relay blocks:

[ARTIFACT BEGINS HERE]

<full artifact content -- no elision markers permitted>

[ARTIFACT ENDS HERE]

---

## VERDICT

**C-29 AUDIT BLOCK**:
1. All Coverage Matrix rows visited in BIND: YES / NO
2. All relay blocks emitted before artifact delimiters: YES / NO
3. Artifact delimiters present and no elision markers inside: YES / NO

> PRE-READ GATE: Before filling the compliance ledger, scan every cell in the table below. If any
> cell is blank (no PASS, no FAIL, no N/A, no -- sentinel), emit DEFECT: EMPTY-CELL at that row
> before continuing. A scorer confirms PRE-READ GATE compliance by verifying no blank cells exist
> in the ledger.

**Compliance ledger**:

| ID | Criterion | Result | Evidence | Defect code (DefectCodeVocab) |
|----|-----------|--------|----------|-------------------------------|
| C-01 | Skill spec input present | PASS / FAIL / N/A | | -- |
| C-02 | Test invocation input present | PASS / FAIL / N/A | | -- |
| C-03 | Coverage Matrix complete | PASS / FAIL / N/A | | -- |
| C-04 | CLOSED WORLD DECLARATION present | PASS / FAIL / N/A | | -- |
| C-05 | CLOSED ASSERTION present | PASS / FAIL / N/A | | -- |
| C-06 | Bind table Status column present | PASS / FAIL / N/A | | -- |
| C-07 | Bind table PrecedenceVocabulary column present | PASS / FAIL / N/A | | -- |
| C-08 | No BLOCKED rows in Bind table | PASS / FAIL / N/A | | -- |
| ... | (continue for all applicable criteria through C-53) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column in
> this trace. A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly
> against the ASR row count.

**ANNOTATION SCOPE REGISTRY**:

| Row | Annotation site | Typed column | Required (RequiredVocabulary) |
|-----|-----------------|--------------|-------------------------------|
| 1 | Bind table | Precedence applied (PrecedenceVocabulary) | YES |
| 2 | Relay Schema | Required (RequiredVocabulary) | YES |
| 3 | Defect Classification Registry | Defect code (DefectCodeVocab) | YES |
| 4 | Verdict compliance ledger | Defect code (DefectCodeVocab) | YES |
| 5 | Template Component Registry | Required (RequiredVocabulary) | YES |
| 6 | ANNOTATION SCOPE REGISTRY | Required (RequiredVocabulary) | YES |

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-04: Combined -- V-01 + V-02 (C-51 + C-52)

**Axis**: Combined V-01 + V-02
**Hypothesis**: The two upgrades are compositionally independent. V-01's upgrade targets the
STRUCTURAL MANDATE (C-49+) block internal structure (separation of independence statement from
verification instruction). V-02's upgrade targets the SCORER HEURISTIC step format (one-line
one-operator discipline). Neither change affects the other's structural site: the mandate block
sits in the ASR section; the step format sits in the canonical template preamble. Together they
eliminate two distinct ambiguity sites -- the partially-merged mandate block and the multi-
operator step (b) -- without creating new dependencies. TCR has 5 components. SCORER HEURISTIC
has steps (a)-(d) (step (b) and (c) from the original R17 step (b) split).

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here. This registry is INDEPENDENT of the compliance ledger -- a scorer
> confirms C-36 compliance by verifying this registry appears before the GATHER phase header and
> carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any other section.

| Defect code (DefectCodeVocab) | Meaning |
|-------------------------------|---------|
| OPEN-WORLD-ASSERTION | Coverage Matrix claims inputs not enumerated in the closed world |
| ELISION-MARKER | Artifact body contains ellipsis or placeholder instead of full content |
| EMPTY-CELL | Compliance ledger cell is blank; no PASS / FAIL / N/A sentinel present |
| COUNT-MISMATCH | Annotation site count in COUNT GATE does not match ASR row count |
| UNRESOLVED-INPUT | Bind table contains UNRESOLVED row and trace proceeded past BIND |
| BLOCKED-TRACE | Bind table contains BLOCKED row; trace must halt and emit this defect |
| OPEN-ASR | ASR closure terminus absent or not mandated by a STRUCTURAL MANDATE (C-49+) block |

---

### CANONICAL STRUCTURAL MANDATE TEMPLATE

> CONFORMANCE-COLLAPSE CLAIM: Every STRUCTURAL MANDATE block in this prompt is an instance of the
> Canonical STRUCTURAL MANDATE Template declared here. A scorer confirms global structural
> conformance by verifying the Template Component Registry rows are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
  (c) Verify the TCR row 5 label cites `C-47` by name -- not implied through row-number sequence -> confirms C-48 (C-48)
  (d) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
without inspecting individual STRUCTURAL MANDATE block bodies.

> SCORER HEURISTIC STEP FORMAT: Each step follows the pattern: `(letter) Action phrase ->
> confirms C-NN (C-NN)` on a single line. Field-split on `->` yields exactly two tokens per step.
> A step carrying more than one `->` operator is non-conforming.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | Separate sentence stating compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that merges the independence statement into the
> verification instruction sentence rather than stating it as a structurally separate sentence,
> or that omits the independence statement entirely, or that omits the ANNOTATION SCOPE REGISTRY
> row from the TCR, is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate
> site.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section headers
> exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without variation.
> Compliance is verifiable without consulting any other section of the trace.

| Phase | Header label |
|-------|-------------|
| 1 | ## GATHER |
| 2 | ## BIND |
| 3 | ## EXECUTE |
| 4 | ## VERDICT |

---

### CONFLICT PRECEDENCE RULE

> STRUCTURAL MANDATE (C-17): When a value appears in both the skill spec and the test invocation,
> the test invocation wins. When a value appears only in the skill spec, the skill spec value is
> used.
> A scorer confirms C-17 compliance by verifying the Bind table carries a
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill spec.
> Compliance is verifiable from the EXECUTE section alone without consulting earlier phases.

| Field | Required (RequiredVocabulary) |
|-------|-------------------------------|
| Role | YES |
| Signal | YES |
| Binding | YES |
| Status | YES |
| Evidence | YES |

Binding pairs use format: `InputName = "ResolvedValue"`

> ANTI-PATTERN (VIOLATION): A relay block that uses `InputName: ResolvedValue` (colon notation)
> instead of `InputName = "ResolvedValue"` (equals-quote notation) is a binding pair violation and
> emits DEFECT: OPEN-WORLD-ASSERTION at the relay site.

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter markers
> `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted inside the
> artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...` or
> `[continued]` or similar placeholder appears between them. Violation emits DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes `[ARTIFACT BEGINS HERE]`.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

---

## GATHER

Enumerate all inputs. Skill spec inputs first. Test invocation inputs second. Build the Coverage
Matrix with every named input as a row.

| Input name | Source | Value summary |
|------------|--------|---------------|
| (one row per named input from spec and invocation) | | |

> STRUCTURAL MANDATE (C-26): After the Coverage Matrix table, emit the following closure terminus
> exactly as shown.
> A scorer confirms C-26 compliance by locating this exact line after the Coverage Matrix table.
> Compliance is verifiable from the GATHER section alone without consulting BIND or EXECUTE.

**CLOSED WORLD DECLARATION**: The inputs enumerated in the Coverage Matrix above are the complete
and closed set of inputs for this trace. No input referenced in BIND or EXECUTE may appear that
does not have a row in this table.

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name not
> present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input row
will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence Rule.

| Input name | Resolved value | Status | Precedence applied (PrecedenceVocabulary) |
|------------|----------------|--------|-------------------------------------------|
| (one row per Coverage Matrix input) | | RESOLVED / UNRESOLVED / BLOCKED | |

**Status** is a three-value enum: `RESOLVED` | `UNRESOLVED` | `BLOCKED`

> If any row carries status BLOCKED, halt the trace immediately and emit DEFECT: BLOCKED-TRACE.
> Do not proceed to EXECUTE.

---

## EXECUTE

For each role in the skill spec, emit one relay block following the Relay Schema. Then emit the
complete artifact.

Relay block format:

```
Role: <role name>
Signal: <signal this role emits>
Binding: <InputName = "ResolvedValue"> pairs
Status: READY | BLOCKED
Evidence: <one sentence confirming binding is complete>
```

After all relay blocks:

[ARTIFACT BEGINS HERE]

<full artifact content -- no elision markers permitted>

[ARTIFACT ENDS HERE]

---

## VERDICT

**C-29 AUDIT BLOCK**:
1. All Coverage Matrix rows visited in BIND: YES / NO
2. All relay blocks emitted before artifact delimiters: YES / NO
3. Artifact delimiters present and no elision markers inside: YES / NO

> PRE-READ GATE: Before filling the compliance ledger, scan every cell in the table below. If any
> cell is blank (no PASS, no FAIL, no N/A, no -- sentinel), emit DEFECT: EMPTY-CELL at that row
> before continuing. A scorer confirms PRE-READ GATE compliance by verifying no blank cells exist
> in the ledger.

**Compliance ledger**:

| ID | Criterion | Result | Evidence | Defect code (DefectCodeVocab) |
|----|-----------|--------|----------|-------------------------------|
| C-01 | Skill spec input present | PASS / FAIL / N/A | | -- |
| C-02 | Test invocation input present | PASS / FAIL / N/A | | -- |
| C-03 | Coverage Matrix complete | PASS / FAIL / N/A | | -- |
| C-04 | CLOSED WORLD DECLARATION present | PASS / FAIL / N/A | | -- |
| C-05 | CLOSED ASSERTION present | PASS / FAIL / N/A | | -- |
| C-06 | Bind table Status column present | PASS / FAIL / N/A | | -- |
| C-07 | Bind table PrecedenceVocabulary column present | PASS / FAIL / N/A | | -- |
| C-08 | No BLOCKED rows in Bind table | PASS / FAIL / N/A | | -- |
| ... | (continue for all applicable criteria through C-52) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column in
> this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against the
> ASR row count.
> Compliance is verifiable from the COUNT GATE section alone without consulting other tables.

**ANNOTATION SCOPE REGISTRY**:

| Row | Annotation site | Typed column | Required (RequiredVocabulary) |
|-----|-----------------|--------------|-------------------------------|
| 1 | Bind table | Precedence applied (PrecedenceVocabulary) | YES |
| 2 | Relay Schema | Required (RequiredVocabulary) | YES |
| 3 | Defect Classification Registry | Defect code (DefectCodeVocab) | YES |
| 4 | Verdict compliance ledger | Defect code (DefectCodeVocab) | YES |
| 5 | Template Component Registry | Required (RequiredVocabulary) | YES |
| 6 | ANNOTATION SCOPE REGISTRY | Required (RequiredVocabulary) | YES |

> STRUCTURAL MANDATE (C-49+): The `ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.`
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-51 compliance by locating a STRUCTURAL MANDATE block within the ASR section
> that names C-49 (or C-49+) as the governing criterion without parsing the registry rows.
> Compliance is verifiable from the ASR section alone without consulting the Coverage Matrix or
> compliance ledger.

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-05: Combined -- V-01 + V-02 + V-03 (All Three Axes -- Tightest Integration)

**Axis**: Combined V-01 + V-02 + V-03
**Hypothesis**: All three axes are active simultaneously. The ASR carries a fully canonical
STRUCTURAL MANDATE (C-49+) with separated independence statement (C-51). Every SCORER HEURISTIC
step is a single-line one-operator field (C-52). PLS is TCR Component 6 with `(C-14)` citation
(C-53). SCORER HEURISTIC has steps (a)-(e): (a) TCR, (b) ASR in TCR at row 5 (C-47), (c) TCR
row 5 self-citing label (C-48), (d) CONFORMANCE-COLLAPSE CLAIM heuristic (C-43), (e) PLS in TCR
at row 6 (C-14). Each step carries exactly one `-> confirms C-NN (C-NN)` operator. TCR has 6
components. ANTI-PATTERN row covers both ASR omission and PLS omission. DCR carries OPEN-ASR.

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here. This registry is INDEPENDENT of the compliance ledger -- a scorer
> confirms C-36 compliance by verifying this registry appears before the GATHER phase header and
> carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any other section.

| Defect code (DefectCodeVocab) | Meaning |
|-------------------------------|---------|
| OPEN-WORLD-ASSERTION | Coverage Matrix claims inputs not enumerated in the closed world |
| ELISION-MARKER | Artifact body contains ellipsis or placeholder instead of full content |
| EMPTY-CELL | Compliance ledger cell is blank; no PASS / FAIL / N/A sentinel present |
| COUNT-MISMATCH | Annotation site count in COUNT GATE does not match ASR row count |
| UNRESOLVED-INPUT | Bind table contains UNRESOLVED row and trace proceeded past BIND |
| BLOCKED-TRACE | Bind table contains BLOCKED row; trace must halt and emit this defect |
| OPEN-ASR | ASR closure terminus absent or not mandated by a STRUCTURAL MANDATE (C-49+) block |

---

### CANONICAL STRUCTURAL MANDATE TEMPLATE

> CONFORMANCE-COLLAPSE CLAIM: Every STRUCTURAL MANDATE block in this prompt is an instance of the
> Canonical STRUCTURAL MANDATE Template declared here. A scorer confirms global structural
> conformance by verifying the Template Component Registry rows 1-6 are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
  (c) Verify the TCR row 5 label cites `C-47` by name -- not implied through row-number sequence -> confirms C-48 (C-48)
  (d) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
  (e) Verify PHASE LABEL SCHEMA at TCR row 6 with `(C-14)` notation -> confirms C-14 (C-14)
without inspecting individual STRUCTURAL MANDATE block bodies.

> SCORER HEURISTIC STEP FORMAT: Each step follows the pattern: `(letter) Action phrase ->
> confirms C-NN (C-NN)` on a single line. Field-split on `->` yields exactly two tokens per step:
> [action phrase, `confirms C-NN (C-NN)`]. A step carrying more than one `->` operator, or whose
> `-> confirms` clause appears on a continuation line rather than the step-letter line, is
> non-conforming and is not machine-readable by field-split-on-`->` alone.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | Separate sentence stating compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |
| 6 (C-14): PHASE LABEL SCHEMA | Immutable 4-phase table declared before GATHER, carrying phase header labels ## GATHER / ## BIND / ## EXECUTE / ## VERDICT | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that merges the independence statement into the
> verification instruction sentence, or that omits the ANNOTATION SCOPE REGISTRY row from the
> TCR, or that omits the PHASE LABEL SCHEMA row from the TCR, is a collapsed mandate and emits
> DEFECT: OPEN-WORLD-ASSERTION at the mandate site.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section headers
> exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without variation.
> Compliance is verifiable without consulting any other section of the trace.

| Phase | Header label |
|-------|-------------|
| 1 | ## GATHER |
| 2 | ## BIND |
| 3 | ## EXECUTE |
| 4 | ## VERDICT |

---

### CONFLICT PRECEDENCE RULE

> STRUCTURAL MANDATE (C-17): When a value appears in both the skill spec and the test invocation,
> the test invocation wins. When a value appears only in the skill spec, the skill spec value is
> used.
> A scorer confirms C-17 compliance by verifying the Bind table carries a
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill spec.
> Compliance is verifiable from the EXECUTE section alone without consulting earlier phases.

| Field | Required (RequiredVocabulary) |
|-------|-------------------------------|
| Role | YES |
| Signal | YES |
| Binding | YES |
| Status | YES |
| Evidence | YES |

Binding pairs use format: `InputName = "ResolvedValue"`

> ANTI-PATTERN (VIOLATION): A relay block that uses `InputName: ResolvedValue` (colon notation)
> instead of `InputName = "ResolvedValue"` (equals-quote notation) is a binding pair violation and
> emits DEFECT: OPEN-WORLD-ASSERTION at the relay site.

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter markers
> `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted inside the
> artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...` or
> `[continued]` or similar placeholder appears between them. Violation emits DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes `[ARTIFACT BEGINS HERE]`.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

---

## GATHER

Enumerate all inputs. Skill spec inputs first. Test invocation inputs second. Build the Coverage
Matrix with every named input as a row.

| Input name | Source | Value summary |
|------------|--------|---------------|
| (one row per named input from spec and invocation) | | |

> STRUCTURAL MANDATE (C-26): After the Coverage Matrix table, emit the following closure terminus
> exactly as shown.
> A scorer confirms C-26 compliance by locating this exact line after the Coverage Matrix table.
> Compliance is verifiable from the GATHER section alone without consulting BIND or EXECUTE.

**CLOSED WORLD DECLARATION**: The inputs enumerated in the Coverage Matrix above are the complete
and closed set of inputs for this trace. No input referenced in BIND or EXECUTE may appear that
does not have a row in this table.

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name not
> present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input row
will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence Rule.

| Input name | Resolved value | Status | Precedence applied (PrecedenceVocabulary) |
|------------|----------------|--------|-------------------------------------------|
| (one row per Coverage Matrix input) | | RESOLVED / UNRESOLVED / BLOCKED | |

**Status** is a three-value enum: `RESOLVED` | `UNRESOLVED` | `BLOCKED`

> If any row carries status BLOCKED, halt the trace immediately and emit DEFECT: BLOCKED-TRACE.
> Do not proceed to EXECUTE.

---

## EXECUTE

For each role in the skill spec, emit one relay block following the Relay Schema. Then emit the
complete artifact.

Relay block format:

```
Role: <role name>
Signal: <signal this role emits>
Binding: <InputName = "ResolvedValue"> pairs
Status: READY | BLOCKED
Evidence: <one sentence confirming binding is complete>
```

After all relay blocks:

[ARTIFACT BEGINS HERE]

<full artifact content -- no elision markers permitted>

[ARTIFACT ENDS HERE]

---

## VERDICT

**C-29 AUDIT BLOCK**:
1. All Coverage Matrix rows visited in BIND: YES / NO
2. All relay blocks emitted before artifact delimiters: YES / NO
3. Artifact delimiters present and no elision markers inside: YES / NO

> PRE-READ GATE: Before filling the compliance ledger, scan every cell in the table below. If any
> cell is blank (no PASS, no FAIL, no N/A, no -- sentinel), emit DEFECT: EMPTY-CELL at that row
> before continuing. A scorer confirms PRE-READ GATE compliance by verifying no blank cells exist
> in the ledger.

**Compliance ledger**:

| ID | Criterion | Result | Evidence | Defect code (DefectCodeVocab) |
|----|-----------|--------|----------|-------------------------------|
| C-01 | Skill spec input present | PASS / FAIL / N/A | | -- |
| C-02 | Test invocation input present | PASS / FAIL / N/A | | -- |
| C-03 | Coverage Matrix complete | PASS / FAIL / N/A | | -- |
| C-04 | CLOSED WORLD DECLARATION present | PASS / FAIL / N/A | | -- |
| C-05 | CLOSED ASSERTION present | PASS / FAIL / N/A | | -- |
| C-06 | Bind table Status column present | PASS / FAIL / N/A | | -- |
| C-07 | Bind table PrecedenceVocabulary column present | PASS / FAIL / N/A | | -- |
| C-08 | No BLOCKED rows in Bind table | PASS / FAIL / N/A | | -- |
| ... | (continue for all applicable criteria through C-53) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column in
> this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against the
> ASR row count.
> Compliance is verifiable from the COUNT GATE section alone without consulting other tables.

**ANNOTATION SCOPE REGISTRY**:

| Row | Annotation site | Typed column | Required (RequiredVocabulary) |
|-----|-----------------|--------------|-------------------------------|
| 1 | Bind table | Precedence applied (PrecedenceVocabulary) | YES |
| 2 | Relay Schema | Required (RequiredVocabulary) | YES |
| 3 | Defect Classification Registry | Defect code (DefectCodeVocab) | YES |
| 4 | Verdict compliance ledger | Defect code (DefectCodeVocab) | YES |
| 5 | Template Component Registry | Required (RequiredVocabulary) | YES |
| 6 | ANNOTATION SCOPE REGISTRY | Required (RequiredVocabulary) | YES |

> STRUCTURAL MANDATE (C-49+): The `ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.`
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-51 compliance by locating a STRUCTURAL MANDATE block within the ASR section
> that names C-49 (or C-49+) as the governing criterion without parsing the registry rows.
> Compliance is verifiable from the ASR section alone without consulting the Coverage Matrix or
> compliance ledger.

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.
