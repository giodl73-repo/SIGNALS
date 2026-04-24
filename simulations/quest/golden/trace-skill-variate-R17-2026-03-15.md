---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 17
rubric: trace-skill-rubric-v16-2026-03-15.md
---

# trace-skill Variations -- Round 17

## Entry State Analysis

R16 V-05 passes C-01 through C-50. R16 introduced and achieved three new criteria:

- **C-48**: SCORER HEURISTIC (C-43) decomposes each step with explicit per-step criterion citation --
  step (b) cites `C-47` by name (not implied through row-number sequence). Upgrades C-45 from
  scorer-heuristic-label-self-citing to scorer-heuristic-steps-criterion-cited.

- **C-49**: ANNOTATION SCOPE REGISTRY self-registers as a named row -- ASR includes itself (row 6 in
  the G/B/E/V architecture) carrying its own typed column `Required (RequiredVocabulary)`. Upgrades
  C-46 from independently-row-verifiable-registry to self-complete-registry.

- **C-50**: TCR row 5 carries inline `(C-47)` criterion citation -- TCR row for ASR follows
  `Component 5 (C-47): ANNOTATION SCOPE REGISTRY` notation. Upgrades C-47 from
  scope-registry-TCR-registered to scope-registry-TCR-row-self-citing.

R16 V-05 is the baseline: all three criteria active together. R17 builds on this baseline and
explores structural tightening without relaxing any prior criteria.

## Variation Axes for R17

- **V-01 (single: Lifecycle emphasis)**: ASR CLOSED ASSERTION terminus -- a formal closure line
  "ANNOTATION SCOPE REGISTRY is CLOSED for this invocation." added as STRUCTURAL MANDATE (C-49+),
  paralleling the Coverage Matrix closure terminus (C-23).

- **V-02 (single: Output format)**: SCORER HEURISTIC steps use explicit `-> confirms (C-NN)` binding
  operator instead of inline parentheticals. Each step ends with `-> confirms C-NN (C-NN)` as a
  structural field.

- **V-03 (single: Role sequence / TCR extension)**: Phase Label Schema registered in TCR as
  Component 6 with `(C-14)` criterion citation; SCORER HEURISTIC gains step (d) confirming Component
  6; Anti-pattern row updates to include PHASE LABEL SCHEMA omission.

- **V-04 (combined: V-01 + V-02)**: ASR CLOSED ASSERTION terminus + step-explicit `-> confirms`
  format. TCR has 5 components.

- **V-05 (combined: V-01 + V-02 + V-03)**: All three axes -- the tightest integration. TCR has 6
  components.

---

## V-01: Single Axis -- Lifecycle Emphasis (ASR CLOSED ASSERTION Terminus)

**Axis**: Lifecycle emphasis
**Hypothesis**: ASR row 6 self-registers (C-49) but lacks a formal closure terminus analogous to
the Coverage Matrix closure terminus (C-23). Adding "ANNOTATION SCOPE REGISTRY is CLOSED" makes ASR
completeness self-evidencing by terminus-line presence rather than row-count inference.

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
| 4 (C-41): INDEPENDENCE STATEMENT | States that compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that contains only a scope statement without a scorer
> verification instruction, or that omits the independence statement, or that omits the ANNOTATION
> SCOPE REGISTRY row from the TCR, is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at
> the mandate site.

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

> STRUCTURAL MANDATE (C-25): PrecedenceVocabulary is a closed type. Only these tokens are permitted:

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
| ... | (continue for all applicable criteria through C-50) | | | |

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

> STRUCTURAL MANDATE (C-49+): The `ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.`
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-49 compliance by locating this exact line after the ANNOTATION SCOPE REGISTRY
> table alone without counting rows or consulting an external enumeration.

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-02: Single Axis -- Output Format (Step-Explicit `-> confirms` Binding Operator)

**Axis**: Output format
**Hypothesis**: C-48 requires per-step criterion citations. Making the step-criterion binding
structurally explicit (operator `-> confirms`) rather than a parenthetical `(C-NN)` makes each
step's criterion coverage independently parseable by field-scan without reading the step's
narrative.

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
      and verify the row cites `C-47` by name in the row label -- not implied through row-number
      sequence -> confirms C-48 (C-48)
  (c) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
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

> STRUCTURAL MANDATE (C-25): PrecedenceVocabulary is a closed type. Only these tokens are permitted:

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
| ... | (continue for all applicable criteria through C-50) | | | |

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

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-03: Single Axis -- Role Sequence / TCR Extension (Phase Label Schema as TCR Component 6)

**Axis**: Role sequence / TCR extension
**Hypothesis**: TCR has 5 components covering the canonical template mechanism. The Phase Label
Schema (C-14) is declared before trace content but not TCR-registered. Adding it as
`Component 6 (C-14): PHASE LABEL SCHEMA` makes every declared pre-trace structural element
TCR-verifiable by row lookup, closing the loop between C-14's declaration requirement and the
canonical template verification path.

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
  (d) verifying the PHASE LABEL SCHEMA appears as TCR row 6 with `(C-14)` notation -- confirms C-14
      (C-14) by TCR row lookup alone without parsing prompt structure;
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

> ANTI-PATTERN: A STRUCTURAL MANDATE block that contains only a scope statement without a scorer
> verification instruction, or that omits the independence statement, or that omits the ANNOTATION
> SCOPE REGISTRY row from the TCR, or that omits the PHASE LABEL SCHEMA from the TCR, is a
> collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate site.

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

> STRUCTURAL MANDATE (C-25): PrecedenceVocabulary is a closed type. Only these tokens are permitted:

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
| ... | (continue for all applicable criteria through C-50) | | | |

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

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-04: Combined -- V-01 + V-02 (ASR Closure Terminus + Step-Explicit `-> confirms` Format)

**Axis**: Combined V-01 + V-02
**Hypothesis**: The ASR CLOSED ASSERTION terminus (V-01) makes ASR completeness self-evidencing by
line presence. The step-explicit `-> confirms` binding operator (V-02) makes per-step criterion
coverage field-scannable. Together they provide two independent structural confirmation paths --
one for ASR completeness (C-49+), one for criterion coverage per step (C-48) -- without requiring
narrative parsing in either case. TCR has 5 components (Phase Label Schema not added here).

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
      and verify the row cites `C-47` by name in the row label -- not implied through row-number
      sequence -> confirms C-48 (C-48)
  (c) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
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

> STRUCTURAL MANDATE (C-25): PrecedenceVocabulary is a closed type. Only these tokens are permitted:

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
| ... | (continue for all applicable criteria through C-50) | | | |

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

> STRUCTURAL MANDATE (C-49+): The `ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.`
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-49 compliance by locating this exact line after the ANNOTATION SCOPE REGISTRY
> table alone without counting rows or consulting an external enumeration.

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.

---

## V-05: Combined -- V-01 + V-02 + V-03 (All Three Axes -- Tightest Integration)

**Axis**: Combined V-01 + V-02 + V-03
**Hypothesis**: The three axes address independent structural gaps: ASR lacks a closure terminus
(V-01), SCORER HEURISTIC steps lack a field-scannable criterion binding operator (V-02), and the
Phase Label Schema lacks TCR registration (V-03). All three can be active simultaneously without
logical conflict. Together they produce a prompt where: ASR completeness is self-evidencing by
terminus-line presence; per-step criterion coverage is field-parseable by operator scan; and every
declared pre-trace structural element is TCR-verifiable by row lookup. TCR has 6 components.

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
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
      and verify the row cites `C-47` by name in the row label -- not implied through row-number
      sequence -> confirms C-48 (C-48)
  (c) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
  (d) Verify the PHASE LABEL SCHEMA appears as TCR row 6 with `(C-14)` notation
      -> confirms C-14 (C-14) by TCR row lookup alone without parsing prompt structure
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

> ANTI-PATTERN: A STRUCTURAL MANDATE block that contains only a scope statement without a scorer
> verification instruction, or that omits the independence statement, or that omits the ANNOTATION
> SCOPE REGISTRY row from the TCR, or that omits the PHASE LABEL SCHEMA from the TCR, is a
> collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate site.

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

> STRUCTURAL MANDATE (C-25): PrecedenceVocabulary is a closed type. Only these tokens are permitted:

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
| ... | (continue for all applicable criteria through C-50) | | | |

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

> STRUCTURAL MANDATE (C-49+): The `ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.`
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-49 compliance by locating this exact line after the ANNOTATION SCOPE REGISTRY
> table alone without counting rows or consulting an external enumeration.

**ANNOTATION SCOPE REGISTRY is CLOSED for this invocation.** Every typed column in this trace,
including this registry's own `Required (RequiredVocabulary)` column, is enumerated above. No
annotation site exists that is not represented by a row in this table.

**COUNT GATE**: ASR row count = 6.

IF the number of typed-column annotation sites present in this trace != 6,
THEN emit DEFECT: COUNT-MISMATCH and mark C-28 as FAIL in the compliance ledger.
