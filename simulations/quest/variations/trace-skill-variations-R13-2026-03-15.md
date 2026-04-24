File written. Here's the output inline:

---

## trace-skill -- Variations R13 (2026-03-15)

**Entry state**: R12 V-05 achieves C-01 through C-41 PASS under v11. v12 adds C-42 (denominator 33 → 34). The single gap: R12 V-05's canonical template shows the scorer confirmation line but the **malformedness rule checks only the header syntax** -- the closing heuristic is not declared as a required component in the conformance check. C-40 passes per-block; C-42 requires it to pass **by contract**.

**R13 upgrade**: extend the canonical template declaration to (a) name the closing heuristic as a required component, (b) extend the malformedness rule to both components, (c) add an explicit conformance-collapse claim that template-conformance is one gate for both C-39 and C-40.

**Variation axes**: lifecycle emphasis (V-01), output format/table-driven (V-02), phrasing register/imperative (V-03), combined lifecycle+table (V-04), combined lifecycle+table+role sequence (V-05).

---

## V-01 -- Single axis: Lifecycle emphasis

**Axis**: Canonical template section expanded to a four-part lifecycle: REQUIRED COMPONENTS declaration → canonical form → malformedness rule → conformance-collapse claim. Each part is labeled and minimal.

**Hypothesis**: The scorer's C-42 check path is fully explicit: read REQUIRED COMPONENTS block (Header→C-39, Closing→C-40), read malformedness rule (both components independently required), read conformance-collapse claim (one check satisfies both). No prose-parsing needed. Risk: four labeled sections add 10 lines before Phase Label Schema. Mitigation: each section is under 4 lines.

```
You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Canonical Structural Mandate Template (C-41, C-42)

**REQUIRED COMPONENTS** -- every STRUCTURAL MANDATE block must include both. A block
missing either is structurally malformed.

- **Header component** (governs C-39): first line `STRUCTURAL MANDATE (C-XX):` syntax.
- **Closing component** (governs C-40): last line `A scorer confirms C-XX compliance by
  [specific method] alone without [parsing alternative].` syntax.

**CANONICAL FORM**:

> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt.
> Reproduce it exactly as shown.
> A scorer confirms C-XX compliance by [specific observable indicator] alone without
> [parsing alternative].

**MALFORMEDNESS RULE**: A block is malformed if (a) header does not match
`STRUCTURAL MANDATE (C-XX)` syntax, OR (b) closing line `A scorer confirms C-XX
compliance by` is absent. Both components are independently required.

**CONFORMANCE-COLLAPSE CLAIM**: Any conforming block satisfies C-39 and C-40 by a
single template-conformance check. C-40 is contractually guaranteed by the same
structural mechanism that guarantees C-39. A scorer confirms C-42 compliance by
verifying this REQUIRED COMPONENTS declaration names both Header and Closing with their
governing criteria alone without inspecting individual block bodies.

---

### Phase Label Schema (Immutable)

| Phase | Label   | Function                                  |
|-------|---------|-------------------------------------------|
| 1     | Gather  | Enumerate all inputs with source          |
| 2     | Bind    | Resolve every input to a single value     |
| 3     | Execute | Produce the target artifact               |
| 4     | Verdict | Declare PASS/FAIL with criterion evidence |

---

### Defect Classification Registry

`DefectCodeVocab` (CLOSED TYPE): `{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: COUNT-MISMATCH,
DEFECT: EMPTY-CELL}`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

| Defect Code (DefectCodeVocab) | Mandate violated                                        | Structural consequence                     |
|-------------------------------|---------------------------------------------------------|--------------------------------------------|
| DEFECT: OPEN-WORLD-ASSERTION  | Coverage Matrix closure -- Required=YES input absent    | Trace halts; no partial execution          |
| DEFECT: COUNT-MISMATCH        | C-28 COUNT GATE -- annotation site count does not match | Ledger-traceable via Defect code column    |
| DEFECT: EMPTY-CELL            | PRE-READ GATE -- empty cell in Defect code column       | Trace halts before ledger traversal begins |

---

## GATHER

### Section 1: Spec Inputs

| Input | Value | Source |
|-------|-------|--------|

### Section 2: Invocation Inputs

| Input | Value | Source |
|-------|-------|--------|

### Coverage Matrix

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

`PrecedenceVocabulary` (CLOSED TYPE): `override` | `default` | `BLOCKED`

`StatusVocab` (CLOSED TYPE): `RESOLVED` | `UNRESOLVED` | `BLOCKED`

**Independence Statement**: Any value outside this vocabulary is a schema error
independently detectable without consulting registry rows.

`RequiredVocabulary` (CLOSED TYPE): `YES` | `VIOLATION`

| Input | Spec Value | Invocation Value | Resolved Value | Status (StatusVocab) | Precedence applied (PrecedenceVocabulary) |
|-------|------------|-----------------|----------------|----------------------|------------------------------------------|

---

## EXECUTE

```
[ARTIFACT BEGINS HERE]
{artifact content}
[ARTIFACT ENDS HERE]
```

| Role (RequiredVocabulary) | Signal | Binding (`InputName = "ResolvedValue"`) | Status (StatusVocab) |
|---------------------------|--------|-----------------------------------------|----------------------|
| ANTI-PATTERN              | Do NOT write input name only -- always write `InputName = "ResolvedValue"` | VIOLATION |
| [role 1]                  | [signal] | `[InputName] = "[ResolvedValue]"` | RESOLVED |

---

## VERDICT

### PRE-READ GATE

(a) Defect Classification Registry present before Phase 1: YES / NO
(b) All FAIL citations drawn from DefectCodeVocab: YES / NO
(c) No empty cells in Defect code column: YES / NO

If (c) fails: HALT. Emit `DEFECT: EMPTY-CELL`. Record in Defect code column.

> STRUCTURAL MANDATE (C-38): When the PRE-READ GATE fires on an empty Defect code cell,
> emit `DEFECT: EMPTY-CELL` -- a DefectCodeVocab-coded defect independently citable in
> the Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-38 compliance by `DEFECT: EMPTY-CELL` emission presence (or explicit
> "no empty cells" clearance) before the compliance ledger alone without reading ledger rows.

### C-29 Audit Block

(a) Registry present before Stage 1: [YES / NO]
(b) All FAIL Defect code values drawn from DefectCodeVocab: [YES / NO]
(c) No empty cells confirmed: [YES / NO]

### C-28 COUNT GATE

Expected: [N]  Actual: [N]

IF actual == expected THEN `confirmed` ELSE emit `DEFECT: COUNT-MISMATCH` and record.

> STRUCTURAL MANDATE (C-37): When the C-28 COUNT GATE resolves to count mismatch, emit
> `DEFECT: COUNT-MISMATCH` -- a DefectCodeVocab-coded defect independently citable in the
> Verdict compliance ledger by defect code without re-reading the gate block.
> A scorer confirms C-37 compliance by `DEFECT: COUNT-MISMATCH` emission presence (or
> `confirmed` gate-pass) before the compliance ledger alone without re-counting columns.

### Compliance Ledger

| ID   | Result | Evidence | Defect code (DefectCodeVocab) |
|------|--------|----------|-------------------------------|

PASS rows: Defect code = `--`   FAIL rows: Defect code from DefectCodeVocab

> STRUCTURAL MANDATE (C-36): The label `**Independence Statement**:` within the
> DefectCodeVocab type declaration is a named structural mandate of this prompt. Reproduce
> it exactly as a bolded labeled element structurally isolated from the definition body.
> A scorer confirms C-36 compliance by `**Independence Statement**:` label presence alone
> without parsing surrounding definition bullets.
```

---

## V-02 -- Single axis: Output format / Template Component Registry table

**Axis**: The template's required components are expressed as a table (Component | Line position | Governs | Required | Malformedness on absence). The `Required` column uses `RequiredVocabulary` (CLOSED TYPE) already declared in BIND — no new type registration needed here. A conformance-collapse claim sentence follows the table.

**Hypothesis**: A table row is independently citable ("Template Component Registry row: Scorer heuristic, Required=YES, Governs=C-40"). A scorer checking C-42 reads the table, finds both rows Required=YES, reads the claim, and confirms without prose-parsing. The table format also creates a new typed annotation site (`Required (RequiredVocabulary)`) that the C-28 COUNT GATE must count, adding one annotation site to the expected tally.

*(Full prompt body: identical to V-01 except the Canonical Structural Mandate Template section is replaced with the Template Component Registry table version shown in the written file.)*

---

## V-03 -- Single axis: Phrasing register / Imperative

**Axis**: The canonical template section uses direct imperative language: "MUST include two components — a block missing either is INVALID." Short, no hedge. The conformance-collapse claim is a one-line assertion: "Any conforming block satisfies C-39 and C-40 by one check. C-40 is contractually required — not optional, not inferred."

**Hypothesis**: Imperative phrasing with no structural overhead minimizes model interpretation. A model reading "MUST include both components" has a clear obligation rule. Risk: without a component registry table, a scorer must infer from prose that the closing heuristic is a named required component. Mitigation: both components are labeled inline ("Component 1: criterion-ID header... Required by C-39" / "Component 2: scorer confirmation closing line... Required by C-40").

---

## V-04 -- Combined: Lifecycle emphasis + Table-driven

**Axis**: Four-part lifecycle (V-01) with the component declaration step anchored by the Template Component Registry table (V-02). The malformedness rule references the registry by row: "a block is malformed if missing any Required=YES row." The conformance-collapse claim cites the registry rows by name: "Scorer heuristic row (Required=YES) guarantees C-40 by the same mechanism the Criterion header row guarantees C-39."

**C-28 note**: The Template Component Registry's `Required (RequiredVocabulary)` column adds one annotation site. The COUNT GATE scope expands to include "Template Component Registry."

---

## V-05 -- Combined: Lifecycle + Table + Role sequence (SCHEMA ROLE)

**Axis**: A pre-trace **SCHEMA ROLE** produces three outputs before any trace phase: (1) Canonical Structural Mandate Template + Template Component Registry table, (2) Phase Label Schema, (3) Type Vocabulary Declarations. The SCHEMA ROLE output is a first-class trace artifact — not a prompt annotation. All STRUCTURAL MANDATE blocks in subsequent phases must conform to the canonical form declared by the SCHEMA ROLE.

**Hypothesis**: Making the canonical template declaration a SCHEMA ROLE output rather than a prompt header strengthens the contractual guarantee: the template is an artifact in the record, not a comment that could be forgotten. A scorer checking C-42 finds the Template Component Registry as SCHEMA ROLE Output 1, verifies both Required=YES rows, and confirms the conformance-collapse claim — all before any trace content. The SCHEMA ROLE also consolidates all type vocabulary declarations in one place, reducing scatter. **C-28 scope note**: the Template Component Registry's `Required (RequiredVocabulary)` column is now explicitly in scope for the COUNT GATE; the expected count tally must include this annotation site.

---

**Full file written to**: `simulations/quest/golden/trace-skill-variate-R13-2026-03-15.md`

**C-42 upgrade summary across variations**:

| V | Axis | C-42 mechanism |
|---|------|----------------|
| V-01 | Lifecycle | REQUIRED COMPONENTS block + two-dimensional malformedness rule + conformance-collapse claim |
| V-02 | Table format | Template Component Registry table (Required=YES rows for Header and Closing) + claim sentence |
| V-03 | Imperative register | Direct "MUST include both components — INVALID if missing" + one-line claim |
| V-04 | Lifecycle + Table | Registry table anchors component declaration; malformedness rule cites rows by name |
| V-05 | Lifecycle + Table + Role sequence | SCHEMA ROLE elevates template declaration to a first-class trace artifact |

**Primary risk across all variations**: the C-28 COUNT GATE expected tally changes in V-02/V-04/V-05 because the Template Component Registry introduces a new `Required (RequiredVocabulary)` typed annotation column. Scorers must recount annotation sites when evaluating these variations; the gate's expected value must include this new site.
