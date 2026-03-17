Written to `simulations/quest/golden/org-scan-golden-2026-03-16.md`.

**Summary of what's in it:**

- **Frontmatter**: status GOLDEN, score 100, rounds 20, rubric v21
- **Prompt body**: exact R20 V-05 simplified form (QU5 PASS, 2,485 words — 32% reduction from full entry)
- **What made it golden** — 5 patterns:
  1. Three-path verification: preamble manifest + schema-first annotations + PHASE OUTPUTS tokens all independently auditable
  2. PREAMBLE DECLARATION MANIFEST with explicit count (10) + self-referential violation rule naming the criterion number
  3. Three distinct gate token types (PASS / FAIL / TABLE F FAIL STRING), with TABLE F FAIL STRING verbatim-quoted at point of use in checklist
  4. Schema-first reference pattern as a named convention present at every applicable instruction site — re-enumeration violations detectable by annotation absence
  5. Floor-constrained criteria pre-declared in preamble as an auditable token inventory before GROUP A begins
- **Final rubric**: v21 with all 8 bands, new criteria C-70–C-77 called out explicitly
LARATIONS

`(C-73: all structured declarations before GROUP A; declaration count is the self-documenting
manifest — any constraint referenced in GROUP A or GROUP B but absent is a C-73 violation)`

---

#### PREAMBLE DECLARATION MANIFEST

```
PREAMBLE DECLARATION MANIFEST — org-scan
(C-73: self-documenting manifest; any constraint referenced in GROUP A or GROUP B but absent
 from this list is a C-73 violation detectable by count comparison)

Declared in this preamble (10 total):
  Named protocols (2):
    1.  GATE TOKEN PROTOCOL      (C-70: includes TABLE F FAIL STRING as named constant)
    2.  INERTIA PATTERN DICTIONARY
  Schema declarations (8):
    3.  TABLE B — Scan Evidence Table
    4.  TABLE C — Cross-Cutting Concerns
    5.  TABLE D — Team Boundary Candidates
    6.  TABLE E — Headcount Signals
    7.  TABLE F — Transport Manifest (C-67 Analytical Purpose required)
    8.  COVERAGE ATTESTATION     (C-68: Minimum rows: 7 gate-blocking)
    9.  TABLE G — Evidence Gaps and Ambiguities
    10. TABLE H — Org Shape Delta (C-69 BRIDGE RULE)

Floor-constrained criteria (C-71: PHASE OUTPUTS footers carry MET/NOT MET for each):
  TABLE B: floor=5 rows (C-16)
  COVERAGE ATTESTATION: floor=7 rows (C-68)
  Source types scanned: floor=3 (C-02)
  TABLE F: floor=2 rows; Analytical Purpose on all rows (C-67/C-70)
  TABLE H: floor=N rows per pre-production assertion (C-69)
  BRIDGE RULE: YES/NO per TABLE H (C-69)
  C-05: YES/NO (no org chart, no reporting lines)

Any floor criterion absent from GROUP A or GROUP B PHASE OUTPUTS footer is a C-71 violation.
```

---

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan (C-20)
(C-22: gate is postcondition of GROUP A and precondition of GROUP B)
(C-70: TABLE F FAIL STRING is a named constant distinct from generic FAIL TOKEN)

SCAN GATE:
  PASS TOKEN:
    "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN label]"

  FAIL TOKEN (items [1]–[7]):
    "SCAN GATE FAIL — item [N]: [reason]"

  TABLE F FAIL STRING (C-70 — item [8] only):
    "TABLE F Output Consumers: Analytical Purpose row compliance: NOT MET —
     row [N] missing Analytical Purpose annotation (C-67/C-70 violation — gate blocked)"

  Gate-blocking items (all 8 required):
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ file paths in TABLE B (C-09/C-16)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68)
  [ ] TABLE B Inertia Match: all INR-01..INR-06 (C-23)
  [ ] Inertia Match before File Path Evidence (C-25)
  [ ] All TABLE B rows have Anti-Fabrication Note (C-11)
  [ ] No org chart, reporting lines, .craft/roles/ content (C-05)
  [ ] TABLE F Analytical Purpose on all rows in correct form
        (C-67/C-70 — failure: TABLE F FAIL STRING, not generic FAIL TOKEN)
```

---

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan (preamble declaration #2)
(C-23: enumerated valid values; C-25: Inertia Match column before File Path Evidence)

INR-01  Org-by-function     Functional silo alignment (eng, design, QA)
INR-02  Org-by-product      Product area or feature surface alignment
INR-03  Org-by-layer        Technical layer alignment (frontend, backend, infra)
INR-04  Org-by-domain       Business domain / bounded context alignment
INR-05  Org-by-geography    Region or timezone alignment
INR-06  Org-by-customer     Customer segment or vertical alignment
```

---

#### SCHEMA DECLARATIONS

```
SCHEMA DECLARATION: TABLE B — Scan Evidence Table  (preamble declaration #3)
  Columns (all required):
    Area                  (C-01: traceable to scan evidence, not invented)
    Source Type           (C-02: one of 7 types declared in COVERAGE ATTESTATION schema)
    Inertia Match         (C-19/C-25: constrained to INR-01..INR-06; before File Path Evidence)
    File Path Evidence    (C-09/C-16/C-21: specific path)
    Anti-Fabrication Note (C-11: required hedging sentence per row)
  Minimum rows: 5  (C-16: path floor gate-blocking)

SCHEMA DECLARATION: TABLE C — Cross-Cutting Concerns  (preamble declaration #4)
  Columns (all required): Concern Name | Boundary Note | Evidence Path
  Minimum rows: 1

SCHEMA DECLARATION: TABLE D — Team Boundary Candidates  (preamble declaration #5)
  Columns (all required): Boundary Candidate | Seam Rationale | Evidence Citation
  Minimum rows: 1

SCHEMA DECLARATION: TABLE E — Headcount Signals  (preamble declaration #6)
  Columns (all required): Signal Source | Headcount Range | Rationale
  Minimum rows: 1

SCHEMA DECLARATION: TABLE F — Transport Manifest  (preamble declaration #7)
  (C-64/C-67/C-70: per-edge Analytical Purpose required;
   absent purpose = C-67 omission + C-70 gate failure — TABLE F FAIL STRING)
  Columns (all required):
    Producing Role      (this role / group)
    Consuming Role      (downstream consumer)
    Tables Consumed     (specific table names)
    Analytical Purpose  (C-67: what consuming role does; C-70: gate-blocking)
  Minimum rows: 2

SCHEMA DECLARATION: COVERAGE ATTESTATION  (preamble declaration #8)
  (C-65/C-68: first-class schema entry; C-72: source types and status values
   declared here — GROUP A references these, does not restate them)
  Columns (all required): Source Type | Status | Notes
  Source types (7 — declared here; GROUP A references, does not restate):
    1. CLAUDE.md files                    5. test coverage areas
    2. package.json / workspace configs   6. SPECS.md files
    3. design/ directories                7. existing .craft/roles/ files
    4. namespace / module directories
  Status values: scanned / not-found / not-applicable
  Minimum rows: 7  (C-68: gate-blocking)

SCHEMA DECLARATION: TABLE G — Evidence Gaps and Ambiguities  (preamble declaration #9)
  Columns (all required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

SCHEMA DECLARATION: TABLE H — Org Shape Delta  (preamble declaration #10)
  (C-66/C-69: BRIDGE RULE declared here; C-72: dimension list declared here)
  Columns (all required):
    Dimension         (org shape dimension)
    Current State     (C-10: what repo evidence shows today)
    Recommended State (C-10: analysis recommendation)
    Driving Evidence  (C-66/C-69: must contain "(cite TABLE B row)" annotation)
  Org shape dimensions (declared here; GROUP B references, does not restate):
    — Team alignment model
    — Cross-cutting concern ownership
    — Headcount distribution model
    — Boundary definition clarity
  Minimum rows: N  (SYNTHESIZER pre-production assertion before TABLE H)

  BRIDGE RULE (C-69 named constraint — declared here; GROUP B references by name):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any row lacking this citation is a BRIDGE RULE violation."
```

`Preamble complete. 10 declared structures (2 named protocols + 8 schemas).`

---

### GROUP A — SCANNER

**HARD BOUNDARY (C-05 / C-13)**: RAW ANALYSIS ONLY. No org chart, no reporting lines,
no hierarchy, no .craft/roles/ file creation. Applies to GROUP A and GROUP B.

**Anti-fabrication rule (C-11)**: Every TABLE B row requires an Anti-Fabrication Note.
Do not invent file paths, area names, or inertia patterns.

Walk the repo. Scan the 7 source types [declared in COVERAGE ATTESTATION schema — decl. #8;
not restated here per schema-first reference pattern]. For each, record status using constrained
values [declared in COVERAGE ATTESTATION schema — decl. #8].

#### TABLE B — Scan Evidence Table

`(TABLE B schema — decl. #3; Inertia Match values per INERTIA PATTERN DICTIONARY — decl. #2;
column order: Inertia Match before File Path Evidence per C-25; all columns required per C-21)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01: from scan evidence] | [source type] | [INR-NN per INERTIA PATTERN DICTIONARY] | [specific/path/file.ext] | [hedging sentence — C-11] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

Dominant inertia pattern: [INR-NN per INERTIA PATTERN DICTIONARY — decl. #2] —
[one sentence justifying dominance]

#### TABLE C — Cross-Cutting Concerns

`(TABLE C schema — decl. #4)`

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [boundary description] | [specific/path] |

#### TABLE D — Team Boundary Candidates

`(TABLE D schema — decl. #5)`

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [seam rationale] | [specific/path] |

#### TABLE E — Headcount Signals

`(TABLE E schema — decl. #6)`

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

`(COVERAGE ATTESTATION schema — decl. #8; source types and status values per decl. #8 —
not restated here per schema-first reference pattern; C-68: Minimum rows: 7 gate-blocking)`

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [notes] |
| package.json / workspace configs | [scanned / not-found / not-applicable] | [notes] |
| design/ directories | [scanned / not-found / not-applicable] | [notes] |
| namespace / module directories | [scanned / not-found / not-applicable] | [notes] |
| test coverage areas | [scanned / not-found / not-applicable] | [notes] |
| SPECS.md files | [scanned / not-found / not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned / not-found / not-applicable] | [notes] |

#### TABLE G — Evidence Gaps and Ambiguities

`(TABLE G schema — decl. #9)`

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(TABLE F schema — decl. #7; C-67/C-70: Analytical Purpose required on every row;
missing purpose = TABLE F FAIL STRING at gate)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67/C-70) |
|----------------|----------------|-----------------|--------------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence per BRIDGE RULE [decl. #10 — not restated per schema-first reference pattern]; uses TABLE C for cross-cutting synthesis; TABLE D for boundary candidates; TABLE E headcount for dimension analysis; TABLE G to bound confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H rows for target org structure; Current State establishes baseline; Recommended State drives configuration at each dimension |

---

**SCAN GATE CHECK**

```
SCAN GATE VERIFICATION CHECKLIST (C-14: numbered items + confirmation sentence)

[1] Source types scanned: [N] of 7 — 3+ required (C-02; decl. #8) .... [MET/NOT MET]
[2] File paths in TABLE B: [N] — 5+ required (C-09/C-16; decl. #3) ... [MET/NOT MET]
[3] COVERAGE ATTESTATION rows: [N] — exactly 7 (C-68; decl. #8) ...... [MET/NOT MET]
[4] TABLE B Inertia Match: all INR-01..INR-06 (C-23; decl. #2) ........ [MET/NOT MET]
[5] Inertia Match before File Path Evidence (C-25; decl. #2) .......... [MET/NOT MET]
[6] All TABLE B rows have Anti-Fabrication Note (C-11; decl. #3) ...... [MET/NOT MET]
[7] No org chart, reporting lines, .craft/roles/ content (C-05) ....... [MET/NOT MET]
[8] TABLE F Analytical Purpose on all rows (C-67/C-70; decl. #7) ..... [MET/NOT MET]
      On NOT MET: write TABLE F FAIL STRING — not generic FAIL TOKEN

If ALL 8 [MET]: write PASS TOKEN (GATE TOKEN PROTOCOL — decl. #1)
If [1]–[7] fail: write FAIL TOKEN (GATE TOKEN PROTOCOL — decl. #1)
If [8] fails: write TABLE F FAIL STRING (GATE TOKEN PROTOCOL — decl. #1)
Any failure: STOP. GROUP B / SYNTHESIZER may not begin.
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may begin only if
the SCAN GATE PASS TOKEN above is present as the final line of GROUP A output."*

```
GROUP A PHASE OUTPUTS
(C-37/C-71: MET/NOT MET tokens for all floor-constrained criteria in PREAMBLE DECLARATION MANIFEST)

  Source types scanned:          [N] of 7  (floor=3; C-02:                    MET / NOT MET)
  TABLE B rows:                  [N]       (floor=5; C-16 path floor:          MET / NOT MET)
  COVERAGE ATTESTATION rows:     [N]       (floor=7; C-68 gate-blocking:       MET / NOT MET)
  TABLE F rows:                  [N]       (floor=2:                           MET / NOT MET)
  TABLE F Analytical Purpose:              (C-67/C-70:                         MET / NOT MET)
  Inertia Match column-order:              (C-25:                              MET / NOT MET)
  Anti-Fabrication Notes:                  (C-11:                              MET / NOT MET)
  C-05 constraint:                         (no org chart / reporting lines:    MET / NOT MET)
  Gate token written:            [PASS TOKEN / FAIL TOKEN / TABLE F FAIL STRING — verbatim]
  Dominant inertia pattern:      [INR-NN]
  Schema-first reference (C-72): MET / NOT MET
```

---

### GROUP B — SYNTHESIZER

**Precondition (C-22)**: Read GROUP A final output line. If FAIL TOKEN or TABLE F FAIL STRING,
write verbatim and halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy diagram. Named recommendations only — no drawn structure.

#### Org Shape Assessment

`(C-07: named from findings; headcount from TABLE E — decl. #6)`

Dominant pattern from GROUP A: [INR-NN — named shape].

Org shape inferred: [named type]. Justification: [two to three sentences citing TABLE B rows
by Area, INR-NN pattern [per INERTIA PATTERN DICTIONARY — decl. #2], TABLE E headcount.]

#### TABLE H — Org Shape Delta

`(TABLE H schema — decl. #10; BRIDGE RULE and dimensions per decl. #10 —
not restated here per schema-first reference pattern; C-10: Current / Recommended separated)`

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE [decl. #10]: every Driving Evidence cell must contain `(cite TABLE B row)` annotation.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Headcount distribution model | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |

#### Current State vs Recommended State Summary

**Current state (C-10)**: [Three to five sentences. Grounded in TABLE B dominant INR-NN
pattern, TABLE C cross-cutting concerns, TABLE D boundaries. No invention.]

**Recommended state (C-10)**: [Three to five sentences. Named shape type. Reference TABLE H
dimensions [per TABLE H schema — decl. #10]. Raw analysis only — no org chart.]

#### Evidence Gaps Acknowledged

`(C-08: TABLE G — decl. #9)`

[One sentence per TABLE G row: acknowledge gap, state impact on recommendation confidence.]

```
GROUP B PHASE OUTPUTS
(C-37/C-71: MET/NOT MET tokens for floor-constrained criteria active in GROUP B)

  TABLE H rows produced:             [N]  (pre-production assertion: [N]; match: YES / NO)
  BRIDGE RULE compliance:                  (all Driving Evidence cells cite TABLE B: YES / NO)
  Org shape named and justified:           (C-07:                              MET / NOT MET)
  Current vs Recommended separated:        (C-10:                              MET / NOT MET)
  Evidence gaps acknowledged:        [N] from TABLE G (decl. #9)
  C-05 constraint:                         (raw analysis only:                 MET / NOT MET)
  Schema-first reference (C-72):           (GROUP B convention annotations:    MET / NOT MET)
```

---

## What Made It Golden

### 1. Three-path verification for every obligation

V-05 is the only variation where every criterion is independently verifiable from three
locations simultaneously: the PREAMBLE DECLARATION MANIFEST (what must exist), the
schema-first reference annotation at each instruction site (violation detectable by annotation
absence), and the PHASE OUTPUTS footer MET/NOT MET token (output-time audit). No prior
variation covered all three paths at once — V-01 had the manifest, V-02 had the footer
tokens, V-03 had the named convention. V-05 combined them.

### 2. PREAMBLE DECLARATION MANIFEST as a self-enforcing audit contract

The manifest publishes an explicit count (10 total: 2 named protocols + 8 schemas) and
embeds the violation rule: "any constraint referenced in GROUP A or GROUP B but absent from
this list is a C-73 violation detectable by count comparison." The count alone makes absent
declarations detectable without reading any phase body. The violation rule names the criterion
number, making the manifest a self-contained enforcement contract requiring no external rubric
knowledge to audit.

### 3. GATE TOKEN PROTOCOL with three distinct token types

Rather than a single FAIL TOKEN with a reason field, the gate defines three distinct named
constants: PASS TOKEN, FAIL TOKEN (items [1]–[7]), and TABLE F FAIL STRING (item [8] only).
The gate checklist quotes the TABLE F FAIL STRING behavior verbatim at the point of use:
"On NOT MET: write TABLE F FAIL STRING — not generic FAIL TOKEN." TABLE F non-compliance is
independently identifiable without parsing any reason field.

### 4. Schema-first reference pattern as a named, annotated convention

The phrase "not restated here per schema-first reference pattern" appears at every applicable
instruction site (source types, status values, Inertia Match values, BRIDGE RULE, TABLE H
dimensions). Any instruction that re-enumerates a declared value set is a structurally
detectable violation: the convention annotation should be present but is not. The pattern name
makes re-enumeration violations auditable by text search rather than by content inspection.

### 5. Floor-constrained criteria pre-declared as an auditable token inventory

The PREAMBLE DECLARATION MANIFEST explicitly lists every floor-constrained criterion that
will appear as a MET/NOT MET token in PHASE OUTPUTS footers, before GROUP A begins.
The expected footer token set is auditable from preamble-read time — missing tokens are
detectable by comparing the preamble inventory against actual footer content, without
inspecting all phase footers.

---

## Final Rubric — org-scan v21

**Scoring model**: Essential 60 pts + Recommended 30 pts + Aspirational capped at 10 pts = 100 max.

### Essential (12 pts each x 5 = 60 pts)

| ID | Criterion |
|----|-----------|
| C-01 | Areas named and traceable to scan evidence, not invented |
| C-02 | Multi-source scan — 3+ of 7 source types cited |
| C-03 | Headcount estimated as a range with supporting rationale |
| C-04 | Cross-cutting concerns named with boundary note |
| C-05 | Raw analysis only — no org chart, no reporting lines |

### Recommended (10 pts each x 3 = 30 pts)

| ID | Criterion |
|----|-----------|
| C-06 | Team boundary candidates with seam rationale |
| C-07 | Org shape named and justified from findings |
| C-08 | Evidence gaps and ambiguities flagged explicitly |

### Aspirational (2 pts each, capped at 10 pts; 69 criteria total)

**Evidence quality**
C-09 5+ specific file paths cited as auditable evidence
C-10 Current state vs recommended state clearly separated
C-11 Anti-fabrication language embedded per evidence-dependent section
C-12 Hard sequencing gate: scan must complete before synthesis begins
C-13 Critical constraint (C-05) stated twice — preamble + output format

**Gate mechanics**
C-14 Verification checklist at gate — numbered items + required confirmation sentence
C-15 Structural group labels for phase separation (GROUP A / GROUP B)
C-16 File path floor enforced as a gate condition (5-path precondition)
C-17 Gate confirmation token — named-token format, machine-parseable
C-18 Gate failure output — named failure-state string when condition unmet
C-19 Inertia Match column — per-row anchor to organizational inertia pattern
C-20 Bidirectional gate token protocol block — PASS and FAIL tokens defined before Phase 1
C-21 Required table column enforcement — omissions structurally visible as empty cells
C-22 Formal phase contract — gate is postcondition of GROUP A AND precondition of GROUP B

**Inertia patterns**
C-23 Inertia pattern dictionary — constrained enumerated values, embedded before Phase 1
C-24 Self-documenting pass token — key conditions verified embedded in token text
C-25 Inertia Match column before File Path Evidence (column-order constraint)

**Schema architecture (selected)**
C-61 TABLE H schema declared in preamble before GROUP B
C-64 TABLE F (transport manifest) declared in preamble
C-65 COVERAGE ATTESTATION declared as first-class schema, not inline prose
C-66 TABLE H Driving Evidence column requires TABLE B citation annotation
C-67 TABLE F Analytical Purpose — required column on every edge row
C-68 COVERAGE ATTESTATION minimum rows gate-blocking (7 rows)
C-69 BRIDGE RULE — named constraint; pre-production assertion before TABLE H

**New criteria added R20**
C-70 TABLE F gate-blocking — named TABLE F FAIL STRING distinct from FAIL TOKEN; 8-item gate
C-71 Phase footer compliance tokens — every PHASE OUTPUTS block carries MET/NOT MET for all floor criteria
C-72 Schema-first reference pattern named as convention — annotation at every applicable instruction site
C-73 Preamble declaration count manifest — explicit count makes absent declarations detectable by comparison
C-74 Pre-declared C-71 token floor list — complete floor-constrained criteria enumerated in preamble; footer token set auditable at preamble-read time
C-75 Preamble manifest self-referential violation type — manifest embeds criterion number in violation-detection statement; self-contained enforcement contract
C-76 Secondary gate obligation distinct failure string — each gate obligation type gets its own named failure string; GATE TOKEN PROTOCOL token count equals distinct obligation types
C-77 Gate checklist verbatim failure string quotation — each gate checklist item quotes its failure string verbatim at point of use; self-contained for agent execution
