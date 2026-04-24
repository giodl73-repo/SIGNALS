---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 19
rubric: trace-skill-rubric-v18-2026-03-15.md
---

# trace-skill Variations -- Round 19

## Entry State Analysis

R18 V-05 passes C-01 through C-53. R18 introduced and achieved three new excellence patterns as
candidate criteria, now formalized in rubric v18:

- **C-51**: Fully canonical STRUCTURAL MANDATE (C-49+) block -- independence statement is a
  structurally separate sentence, not merged into the verification instruction. R18 V-01 and
  V-04/V-05 all implement this correctly. No gap.

- **C-52**: One-step-one-operator discipline in SCORER HEURISTIC -- every step uses
  `-> confirms C-NN (C-NN)` on a single line, field-split on `->` yields exactly two tokens.
  R18 V-02/V-04/V-05 implement this by splitting the formerly ambiguous step (b) into two
  independent steps. No gap.

- **C-53**: Phase Label Schema registered as TCR Component 6 with inline `(C-14)` citation. R18
  V-03/V-05 implement this. SCORER HEURISTIC step (e) confirms PLS at TCR row 6. No gap.

R19 upgrade axes (two new criteria from R18 rubric v18):

- **C-54**: SCORER HEURISTIC STEP FORMAT promoted from a note block to a full
  `STRUCTURAL MANDATE (C-52)` block -- all four canonical template components present (label,
  scope, verification instruction, independence statement). The one-step-one-operator discipline
  is governed by the canonical template mechanism so its presence is template-conformance-
  checkable rather than note-location-dependent. TCR gains Component 7 for SCORER HEURISTIC STEP
  FORMAT. SCORER HEURISTIC gains step (f).

- **C-55**: ANTI-PATTERN block declared self-complete with respect to the TCR -- body no longer
  enumerates collapse conditions by naming specific TCR components; instead delegates to
  "any Required=YES TCR row" so coverage is auditable by TCR row count alone without scanning
  the ANTI-PATTERN body for component names.

R19 variation axes:

- **V-01 (single: C-54)**: SCORER HEURISTIC STEP FORMAT as full canonical STRUCTURAL MANDATE
  (C-52). TCR gains row 7. SCORER HEURISTIC gains step (f) `-> confirms C-52 (C-52)`.
  ANTI-PATTERN updated to name Component 7 explicitly (C-55 not active). CONFORMANCE-COLLAPSE
  CLAIM updated to "rows 1-7." ASR count stays 6 (no new typed columns).

- **V-02 (single: C-55 simple delegation)**: ANTI-PATTERN body replaces enumerated component
  names with TCR-count delegation: "any Required=YES TCR row" is the collapse trigger. No
  explicit CLOSED terminus statement. SCORER HEURISTIC STEP FORMAT remains a note (C-54 not
  active).

- **V-03 (single: C-55 with closure terminus)**: Same TCR delegation as V-02 but adds a named
  CLOSED ASSERTION line at the bottom of the ANTI-PATTERN block, parallel to how C-26 adds a
  terminus to the Coverage Matrix and C-51 adds a terminus to the ASR. Hypothesis: the explicit
  closure terminus makes C-55's self-completeness claim structurally mandated rather than
  emergent.

- **V-04 (combined: C-54 + C-55 simple)**: V-01's STRUCTURAL MANDATE (C-52) block + TCR row 7
  + step (f), combined with V-02's delegation-style ANTI-PATTERN. CONFORMANCE-COLLAPSE CLAIM
  "rows 1-7." ANTI-PATTERN body: "any Required=YES TCR row (rows 1-7)." Tightest test of
  compositional independence between the mandate-block upgrade and the ANTI-PATTERN delegation.

- **V-05 (combined: C-54 + C-55 tight)**: V-01's STRUCTURAL MANDATE (C-52) block + TCR row 7
  + step (f), combined with V-03's delegation + explicit closure terminus. The strongest
  integration -- ANTI-PATTERN body delegates AND carries a structural closure terminus, TCR has
  7 rows with all covered, SCORER HEURISTIC has steps (a)-(f) each with one `->` operator.

All five inherit the full R18 V-05 baseline: DCR (7 rows including OPEN-ASR), canonical
STRUCTURAL MANDATE template with TCR, fully-canonical STRUCTURAL MANDATE (C-49+) with separated
independence statement, Phase Label Schema as TCR Component 6, SCORER HEURISTIC steps (a)-(e)
each carrying one `-> confirms C-NN (C-NN)` operator, PRE-READ GATE, C-29 audit, compliance
ledger, COUNT GATE, ASR 6 rows including self-registration row.

---

## V-01: Single Axis -- C-54 (SCORER HEURISTIC STEP FORMAT as STRUCTURAL MANDATE (C-52))

**Axis**: Lifecycle emphasis -- mandate block structure
**Hypothesis**: R18 V-05 carries SCORER HEURISTIC STEP FORMAT as a `> SCORER HEURISTIC STEP
FORMAT:` note block. A scorer confirming C-52 must locate this note by name-search rather than
by TCR row lookup. Promoting it to a full `STRUCTURAL MANDATE (C-52)` block with all four
canonical template components (label + scope + verification instruction + independence statement)
makes C-52's presence template-conformance-checkable: a scorer confirms C-52 is governed by the
canonical template by locating TCR row 7 with `(C-52)` notation, without scanning the prompt
for a note. TCR gains Component 7. SCORER HEURISTIC gains step (f). ANTI-PATTERN adds Component
7 by name (enumerated style preserved, C-55 not active). CONFORMANCE-COLLAPSE CLAIM updated to
"rows 1-7." ASR count unchanged at 6.

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here.
> A scorer confirms C-36 compliance by verifying this registry appears before the GATHER phase
> header and carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any
> other section.
> Compliance is verifiable from this registry block alone without consulting the compliance ledger
> or any phase section.

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
> conformance by verifying the Template Component Registry rows 1-7 are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
  (c) Verify the TCR row 5 label cites `C-47` by name -- not implied through row-number sequence -> confirms C-48 (C-48)
  (d) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
  (e) Verify PHASE LABEL SCHEMA at TCR row 6 with `(C-14)` notation -> confirms C-14 (C-14)
  (f) Verify SCORER HEURISTIC STEP FORMAT at TCR row 7 with `(C-52)` notation -> confirms C-52 (C-52)
without inspecting individual STRUCTURAL MANDATE block bodies.

> STRUCTURAL MANDATE (C-52): Each step in the SCORER HEURISTIC body follows the pattern
> `(letter) Action phrase -> confirms C-NN (C-NN)` on a single line. Reproduce each step in
> this form exactly.
> A scorer confirms C-52 compliance by verifying each SCORER HEURISTIC step carries exactly one
> `->` operator and that field-split on `->` yields exactly two tokens: [action phrase,
> `confirms C-NN (C-NN)`]. A step carrying more than one `->` operator, or whose `-> confirms`
> clause appears on a sub-line rather than the step-letter line, is non-conforming.
> Compliance is verifiable from the SCORER HEURISTIC section alone without consulting any other
> section of the prompt.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | Separate sentence stating compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |
| 6 (C-14): PHASE LABEL SCHEMA | Immutable 4-phase table declared before GATHER, carrying phase header labels ## GATHER / ## BIND / ## EXECUTE / ## VERDICT | YES |
| 7 (C-52): SCORER HEURISTIC STEP FORMAT | STRUCTURAL MANDATE (C-52) block governing the one-step-one-operator discipline; field-split on `->` yields exactly two tokens per step | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that merges the independence statement into the
> verification instruction sentence, or that omits the ANNOTATION SCOPE REGISTRY row from the
> TCR, or that omits the PHASE LABEL SCHEMA row from the TCR, or that omits the SCORER HEURISTIC
> STEP FORMAT row from the TCR, is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at
> the mandate site.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section
> headers exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without
> variation.
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
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence
> token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or
> invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill
> spec.
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

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter
> markers `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted
> inside the artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...`
> or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes
> `[ARTIFACT BEGINS HERE]`.
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

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name
> not present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input
row will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence
Rule.

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
| ... | (continue for all applicable criteria through C-54) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column
> in this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against
> the ASR row count.
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
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as
> shown.
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

## V-02: Single Axis -- C-55 (ANTI-PATTERN TCR Delegation, No Closure Statement)

**Axis**: Output format -- ANTI-PATTERN coverage claim
**Hypothesis**: R18 V-05's ANTI-PATTERN enumerates three specific component names:
"independence statement," "ANNOTATION SCOPE REGISTRY row," and "PHASE LABEL SCHEMA row." A
scorer verifying ANTI-PATTERN completeness must scan the body for these names and compare them
against all 6 TCR Required=YES rows -- a body-scan-dependent check. Replacing the enumerated
names with a TCR-count delegation ("any Required=YES TCR row") removes the body dependency:
coverage is auditable by counting TCR Required=YES rows (currently 6) and checking the ANTI-
PATTERN delegates to ALL of them, without reading the ANTI-PATTERN body for component names.
Hypothesis: this single body change achieves C-55 without any other structural modification. The
SCORER HEURISTIC STEP FORMAT remains a note block (C-54 not active in this variation).

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here.
> A scorer confirms C-36 compliance by verifying this registry appears before the GATHER phase
> header and carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any
> other section.
> Compliance is verifiable from this registry block alone without consulting the compliance ledger
> or any phase section.

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

> ANTI-PATTERN: A STRUCTURAL MANDATE block that omits any required component (any TCR row where
> Required=YES) is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate
> site. ANTI-PATTERN coverage is CLOSED: auditable by TCR Required=YES row count (6 rows) alone
> without scanning this block for component names.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section
> headers exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without
> variation.
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
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence
> token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or
> invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill
> spec.
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

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter
> markers `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted
> inside the artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...`
> or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes
> `[ARTIFACT BEGINS HERE]`.
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

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name
> not present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input
row will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence
Rule.

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
| ... | (continue for all applicable criteria through C-55) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column
> in this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against
> the ASR row count.
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
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as
> shown.
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

## V-03: Single Axis -- C-55 with Explicit Closure Terminus

**Axis**: Coverage declaration -- ANTI-PATTERN structural closure
**Hypothesis**: V-02 achieves C-55 by replacing enumerated names with TCR delegation ("any
Required=YES TCR row"). However the self-completeness claim is emergent -- a reader has to infer
that the delegation covers ALL TCR rows from the "any" quantifier alone. Adding an explicit
CLOSED ASSERTION line at the bottom of the ANTI-PATTERN block ("ANTI-PATTERN CLOSED ASSERTION:
Coverage is closed for this prompt version...") makes the self-completeness claim structurally
mandated, parallel to how C-26 mandates a CLOSED WORLD DECLARATION at the bottom of the Coverage
Matrix and C-51 mandates a closure terminus at the bottom of the ASR. Hypothesis: the closure
terminus makes C-55 compliance auditable by locating the CLOSED ASSERTION line alone, without
reading the ANTI-PATTERN body to verify the delegation quantifier. SCORER HEURISTIC STEP FORMAT
remains a note block (C-54 not active).

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here.
> A scorer confirms C-36 compliance by verifying this registry appears before the GATHER phase
> header and carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any
> other section.
> Compliance is verifiable from this registry block alone without consulting the compliance ledger
> or any phase section.

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

> ANTI-PATTERN: A STRUCTURAL MANDATE block that omits any required component (any TCR row where
> Required=YES) is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate
> site.
>
> **ANTI-PATTERN CLOSED ASSERTION**: Coverage is closed for this prompt version. Every Required=YES
> TCR row (rows 1-6) is a named collapse condition. A scorer confirms C-55 compliance by locating
> this CLOSED ASSERTION line without scanning the ANTI-PATTERN body for individual component names.
> Auditable by TCR Required=YES row count (6 rows) alone.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section
> headers exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without
> variation.
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
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence
> token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or
> invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill
> spec.
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

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter
> markers `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted
> inside the artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...`
> or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes
> `[ARTIFACT BEGINS HERE]`.
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

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name
> not present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input
row will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence
Rule.

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
| ... | (continue for all applicable criteria through C-55) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column
> in this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against
> the ASR row count.
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
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as
> shown.
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

## V-04: Combined -- C-54 + C-55 Simple (V-01 + V-02 Approaches)

**Axis**: Combined V-01 + V-02
**Hypothesis**: The two upgrades are compositionally independent. V-01's upgrade promotes SCORER
HEURISTIC STEP FORMAT from a note to a STRUCTURAL MANDATE (C-52) block and extends TCR to 7
rows. V-02's upgrade replaces ANTI-PATTERN's enumerated body with TCR delegation ("any
Required=YES TCR row"). These changes do not interfere: the mandate-block upgrade affects the
preamble structure; the ANTI-PATTERN delegation affects only the coverage claim. Together: TCR
has 7 rows, CONFORMANCE-COLLAPSE CLAIM says "rows 1-7," ANTI-PATTERN delegates to "any
Required=YES TCR row (rows 1-7)," SCORER HEURISTIC has steps (a)-(f) with one `->` operator
each. The ANTI-PATTERN delegation automatically covers the new Component 7 without a body update
-- this is the primary composability proof for C-54 + C-55.

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here.
> A scorer confirms C-36 compliance by verifying this registry appears before the GATHER phase
> header and carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any
> other section.
> Compliance is verifiable from this registry block alone without consulting the compliance ledger
> or any phase section.

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
> conformance by verifying the Template Component Registry rows 1-7 are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
  (c) Verify the TCR row 5 label cites `C-47` by name -- not implied through row-number sequence -> confirms C-48 (C-48)
  (d) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
  (e) Verify PHASE LABEL SCHEMA at TCR row 6 with `(C-14)` notation -> confirms C-14 (C-14)
  (f) Verify SCORER HEURISTIC STEP FORMAT at TCR row 7 with `(C-52)` notation -> confirms C-52 (C-52)
without inspecting individual STRUCTURAL MANDATE block bodies.

> STRUCTURAL MANDATE (C-52): Each step in the SCORER HEURISTIC body follows the pattern
> `(letter) Action phrase -> confirms C-NN (C-NN)` on a single line. Reproduce each step in
> this form exactly.
> A scorer confirms C-52 compliance by verifying each SCORER HEURISTIC step carries exactly one
> `->` operator and that field-split on `->` yields exactly two tokens: [action phrase,
> `confirms C-NN (C-NN)`]. A step carrying more than one `->` operator, or whose `-> confirms`
> clause appears on a sub-line rather than the step-letter line, is non-conforming.
> Compliance is verifiable from the SCORER HEURISTIC section alone without consulting any other
> section of the prompt.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | Separate sentence stating compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |
| 6 (C-14): PHASE LABEL SCHEMA | Immutable 4-phase table declared before GATHER, carrying phase header labels ## GATHER / ## BIND / ## EXECUTE / ## VERDICT | YES |
| 7 (C-52): SCORER HEURISTIC STEP FORMAT | STRUCTURAL MANDATE (C-52) block governing the one-step-one-operator discipline; field-split on `->` yields exactly two tokens per step | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that omits any required component (any TCR row where
> Required=YES) is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate
> site. ANTI-PATTERN coverage is CLOSED: auditable by TCR Required=YES row count (7 rows) alone
> without scanning this block for component names.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section
> headers exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without
> variation.
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
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence
> token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or
> invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill
> spec.
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

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter
> markers `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted
> inside the artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...`
> or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes
> `[ARTIFACT BEGINS HERE]`.
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

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name
> not present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input
row will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence
Rule.

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
| ... | (continue for all applicable criteria through C-55) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column
> in this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against
> the ASR row count.
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
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as
> shown.
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

## V-05: Combined -- C-54 + C-55 Tight (V-01 + V-03 Approaches -- Tightest Integration)

**Axis**: Combined V-01 + V-03
**Hypothesis**: All four R19 upgrade elements are active simultaneously: STRUCTURAL MANDATE
(C-52) block with full canonical form (C-54), TCR Component 7 for SCORER HEURISTIC STEP FORMAT
(C-54), SCORER HEURISTIC step (f) with `-> confirms C-52 (C-52)` (C-54), and ANTI-PATTERN body
uses TCR delegation with an explicit CLOSED ASSERTION terminus (C-55). The explicit closure
terminus makes C-55's self-completeness not only true but structurally mandated. The combination
proves: (1) adding TCR row 7 does not break ANTI-PATTERN self-completeness -- the delegation
automatically covers the new row, and (2) the explicit CLOSED ASSERTION terminus explicitly names
the new row count (7), closing the loop between the two upgrades. CONFORMANCE-COLLAPSE CLAIM
"rows 1-7." ANTI-PATTERN CLOSED ASSERTION names "rows 1-7." SCORER HEURISTIC steps (a)-(f)
each carry exactly one `->` operator.

---

You are running /trace-skill for: {{skill_name}}

Inputs:
- Skill spec: {{skill_spec}}
- Test invocation: {{test_invocation}}

---

### DEFECT CLASSIFICATION REGISTRY

> STRUCTURAL MANDATE (C-36): This registry is declared before any trace content. It is the closed
> authority for all defect codes emitted in this trace. No defect code may appear in this trace
> that is not listed here.
> A scorer confirms C-36 compliance by verifying this registry appears before the GATHER phase
> header and carries a closed-type column `Defect code (DefectCodeVocab)`, without consulting any
> other section.
> Compliance is verifiable from this registry block alone without consulting the compliance ledger
> or any phase section.

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
> conformance by verifying the Template Component Registry rows 1-7 are present without inspecting
> individual STRUCTURAL MANDATE block bodies. A STRUCTURAL MANDATE block that omits any TCR
> component collapses to a non-conforming instance and the trace is defective at that site.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by:
  (a) Locate the Template Component Registry -> confirms C-41 (C-41)
  (b) Verify ANNOTATION SCOPE REGISTRY at TCR row 5 with `(C-47)` notation -> confirms C-47 (C-47)
  (c) Verify the TCR row 5 label cites `C-47` by name -- not implied through row-number sequence -> confirms C-48 (C-48)
  (d) Read the CONFORMANCE-COLLAPSE CLAIM's stated heuristic -> confirms C-43 (C-43)
  (e) Verify PHASE LABEL SCHEMA at TCR row 6 with `(C-14)` notation -> confirms C-14 (C-14)
  (f) Verify SCORER HEURISTIC STEP FORMAT at TCR row 7 with `(C-52)` notation -> confirms C-52 (C-52)
without inspecting individual STRUCTURAL MANDATE block bodies.

> STRUCTURAL MANDATE (C-52): Each step in the SCORER HEURISTIC body follows the pattern
> `(letter) Action phrase -> confirms C-NN (C-NN)` on a single line. Reproduce each step in
> this form exactly.
> A scorer confirms C-52 compliance by verifying each SCORER HEURISTIC step carries exactly one
> `->` operator and that field-split on `->` yields exactly two tokens: [action phrase,
> `confirms C-NN (C-NN)`]. A step carrying more than one `->` operator, or whose `-> confirms`
> clause appears on a sub-line rather than the step-letter line, is non-conforming.
> Compliance is verifiable from the SCORER HEURISTIC section alone without consulting any other
> section of the prompt.

**Template Component Registry (TCR)**:

| Component | Description | Required |
|-----------|-------------|----------|
| 1 (C-38): MANDATE LABEL | Named label in format STRUCTURAL MANDATE (C-NN) identifying the criterion being mandated | YES |
| 2 (C-39): SCOPE STATEMENT | One sentence declaring what structural element is mandated | YES |
| 3 (C-40): VERIFICATION INSTRUCTION | Explicit instruction to scorer on how to confirm compliance | YES |
| 4 (C-41): INDEPENDENCE STATEMENT | Separate sentence stating compliance is verifiable without consulting other sections | YES |
| 5 (C-47): ANNOTATION SCOPE REGISTRY | Named row in ASR table; self-registers with typed column Required (RequiredVocabulary) | YES |
| 6 (C-14): PHASE LABEL SCHEMA | Immutable 4-phase table declared before GATHER, carrying phase header labels ## GATHER / ## BIND / ## EXECUTE / ## VERDICT | YES |
| 7 (C-52): SCORER HEURISTIC STEP FORMAT | STRUCTURAL MANDATE (C-52) block governing the one-step-one-operator discipline; field-split on `->` yields exactly two tokens per step | YES |

> ANTI-PATTERN: A STRUCTURAL MANDATE block that omits any required component (any TCR row where
> Required=YES) is a collapsed mandate and emits DEFECT: OPEN-WORLD-ASSERTION at the mandate
> site.
>
> **ANTI-PATTERN CLOSED ASSERTION**: Coverage is closed for this prompt version. Every Required=YES
> TCR row (rows 1-7) is a named collapse condition. A scorer confirms C-55 compliance by locating
> this CLOSED ASSERTION line without scanning the ANTI-PATTERN body for individual component names.
> Auditable by TCR Required=YES row count (7 rows) alone.

**RequiredVocabulary**: `YES` | `NO` (closed type; no other values permitted)

---

### PHASE LABEL SCHEMA

> STRUCTURAL MANDATE (C-14): The four phase labels below are immutable. Use them as section
> headers exactly as shown.
> A scorer confirms C-14 compliance by verifying all four headers appear in order without
> variation.
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
> `Precedence applied (PrecedenceVocabulary)` column and every RESOLVED row names a precedence
> token.
> Compliance is verifiable from the Bind table alone without consulting the skill spec or
> invocation.

**PrecedenceVocabulary**: `INVOCATION-WINS` | `SPEC-DEFAULT` | `INVOCATION-ONLY` | `SPEC-ONLY`

---

### RELAY SCHEMA

> STRUCTURAL MANDATE (C-21): Every role in the skill spec produces exactly one relay block in the
> EXECUTE phase. A relay block that omits any required field is defective.
> A scorer confirms C-21 compliance by counting relay blocks against the role list in the skill
> spec.
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

> STRUCTURAL MANDATE (C-24): The EXECUTE phase emits the complete artifact between delimiter
> markers `[ARTIFACT BEGINS HERE]` and `[ARTIFACT ENDS HERE]`. No elision markers are permitted
> inside the artifact body.
> A scorer confirms C-24 compliance by verifying both delimiter markers are present and no `...`
> or `[continued]` or similar placeholder appears between them. Violation emits
> DEFECT: ELISION-MARKER.
> Compliance is verifiable from the EXECUTE section alone without consulting other phases.

> STRUCTURAL MANDATE (C-27): Relay blocks appear before the artifact delimiters, not after.
> A scorer confirms C-27 compliance by verifying the last relay block precedes
> `[ARTIFACT BEGINS HERE]`.
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

> DEFECT: OPEN-WORLD-ASSERTION -- emitted if any BIND or EXECUTE step references an input name
> not present as a row in the Coverage Matrix.

**CLOSED ASSERTION**: Every input row in the Coverage Matrix will be visited in BIND. No input
row will be skipped. Coverage Matrix is CLOSED for this invocation.

---

## BIND

Resolve each input from the Coverage Matrix. One row per input. Apply the Conflict Precedence
Rule.

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
| ... | (continue for all applicable criteria through C-55) | | | |

> PASS rows carry `--` in the Defect code column as a sentinel. FAIL rows carry the applicable
> defect code from DefectCodeVocab. N/A rows carry `--`.

**Overall verdict**: PASS (all criteria PASS or N/A) / FAIL (one or more criteria FAIL)

---

**C-28 COUNT GATE**

> STRUCTURAL MANDATE (C-28): The ANNOTATION SCOPE REGISTRY below enumerates every typed column
> in this trace.
> A scorer confirms C-28 compliance by verifying the COUNT GATE IF/THEN fires correctly against
> the ASR row count.
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
> closure terminus line is a named structural mandate of this prompt. Reproduce it exactly as
> shown.
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
