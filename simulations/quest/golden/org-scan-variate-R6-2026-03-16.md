---
skill: quest-variate
topic: org-scan
item: variate-R6
date: 2026-03-16
rubric_version: v6
round: 6
---

# Quest Variate — org-scan Round 6 (rubric v6)

v6 adds C-21 through C-24. All five R5 variations scored 100 on v5. The new criteria are:

- **C-21** Required table column enforcement — REQUIRED declared in output schema; empty cells are structural gaps
- **C-22** Formal phase contract — gate stated as P1 postcondition = P2 precondition (both sides named)
- **C-23** Inertia pattern dictionary — enumerated labels embedded before Phase 1; column is constrained, not free-text
- **C-24** Self-documenting pass token — includes source count, path count, dominant pattern name

All R5 variations already hit C-20 (GATE TOKEN PROTOCOL block) and C-19 (Inertia Match column). The new axes target enforcement posture:
how explicitly are columns declared as REQUIRED, how formally is the phase boundary expressed as a contract, how tightly is the dictionary bound to the column.

**Variation axes selected**:
- V-01: Lifecycle emphasis (single axis)
- V-02: Inertia framing (single axis)
- V-03: Output format / schema-first (single axis)
- V-04: Lifecycle + Inertia (combined)
- V-05: All axes — maximum coverage

---

## V-01: Lifecycle Emphasis

**Axis**: Lifecycle emphasis — GROUP A / GROUP B phase separation is the primary structural mechanism; the gate is expressed as a formal bidirectional phase contract (Phase 1 postcondition = Phase 2 precondition).

**Hypothesis**: When the GROUP A / GROUP B boundary is the dominant structural frame and the gate is expressed as a bidirectional contract rather than a blocking instruction, agents treat premature synthesis as a formal protocol violation — not just an instruction to disregard. This maximizes C-12, C-22 compliance and keeps C-21/C-23/C-24 achievable as supporting mechanisms.

---

# org-scan

Walk the repo and infer the org structure. Output is **raw analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this scan into a full org.

> **OUTPUT CONSTRAINT (preamble)**: This skill produces raw analysis only. No org chart. No reporting lines. No management hierarchy. This constraint is absolute. *Restated in GROUP B output format below.*

---

### GATE TOKEN PROTOCOL

Both tokens are named constants. Defined here before Phase 1 begins.

**PASS TOKEN** — output this format when all gate conditions are satisfied:
```
SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN_LABEL]
```
The token names source count, path count, and dominant inertia pattern — making it self-reporting about the conditions it asserts.

**FAIL TOKEN** — output this exact string when the file path floor is not met:
```
PATH FLOOR NOT MET — halt
```

---

### INERTIA PATTERN REFERENCE

Valid labels for the Inertia Match column. The column accepts only these values. Free text is invalid.

| Label | Meaning |
|---|---|
| SILO | Domain enclosed; team acts independently; few cross-cutting connections |
| FRAGMENT | Domain split across multiple owners; coordination cost elevated |
| OVERLAP | Multiple teams claim or work the same domain |
| INHERIT | Structure inherited from prior state; not aligned to current needs |
| EXPAND | Team boundary growing beyond original scope |
| LOCK | Domain ownership frozen despite scope change |
| CENTRALIZE | Consolidation pressure toward a single owner or team |
| UNKNOWN | Pattern unclear from available evidence |

---

### OUTPUT SCHEMA — Phase 1 Scan Table

The following columns are **REQUIRED**. Empty cells in REQUIRED columns are structural gaps visible in the table — not silently absent from prose.

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| File Path Evidence | REQUIRED |
| Inertia Match | REQUIRED |
| Notes | optional |

*Inertia Match accepts only labels from the INERTIA PATTERN REFERENCE above.*

---

## GROUP A: CURRENT STATE

> **ANTI-FABRICATION**: All areas in this section must be traceable to a cited file path or named source type. Do not name areas without scan evidence.

### Source Coverage

Scan at least 3 of these 7 source types:

1. `CLAUDE.md` files — namespace ownership, design intent, scope signals
2. `package.json` / build manifests — dependency graph, module boundaries
3. `design/` or `specs/` directories — planned areas of work
4. Namespace directories — feature ownership topology
5. Test coverage areas — tested domains, coverage gaps
6. `SPECS.md` files — stated scope and team assumptions
7. `.roles/` — explicit role definitions

**FILE PATH FLOOR (GATE PRECONDITION)**: You must cite a minimum of 5 specific file paths in the File Path Evidence column. This is a gate condition — fewer than 5 paths blocks Phase 2. If fewer than 5 paths are found, output the FAIL TOKEN and stop.

Produce the Phase 1 Scan Table now. All REQUIRED columns must be populated.

---

## PHASE 1 → PHASE 2 GATE

**Phase 1 postcondition** (must hold before Phase 1 terminates):
- At least 3 source types scanned and named
- At least 5 specific file paths present in File Path Evidence
- All Inertia Match cells contain a label from the reference (UNKNOWN is valid; blank is not)
- No org chart or reporting lines appear in GROUP A output

**Phase 2 precondition** (must be confirmed before GROUP B begins):
- At least 3 source types scanned and named
- At least 5 specific file paths present in File Path Evidence
- All Inertia Match cells contain a label from the reference
- No org chart or reporting lines appear in GROUP A output

These two statements name the same contract from both sides. Both must hold.

Verification checklist:
1. Source types: count the named source types in the scan table — is the count ≥ 3?
2. File paths: count distinct paths in File Path Evidence — is the count ≥ 5?
3. Inertia Match: inspect each cell — does each contain a reference label (not blank, not free text)?
4. Constraint: inspect all GROUP A output — does any line contain org chart structure or reporting lines?
5. Confirmation: if all four conditions pass, write the PASS TOKEN from the GATE TOKEN PROTOCOL above.

If any condition fails, output `PATH FLOOR NOT MET — halt` and stop.

---

## GROUP B: RECOMMENDED STATE

> **OUTPUT CONSTRAINT (restatement)**: Raw analysis only. No org chart. No reporting lines. No management hierarchy.

> **ANTI-FABRICATION**: Synthesis draws only from GROUP A findings. This applies equally to seam candidates, headcount estimates, and org shape recommendations — not only to Phase 1 evidence rows.

### Team Boundary Candidates

| Boundary | Seam Rationale | Inertia Patterns Involved | Supporting Paths |
|---|---|---|---|

> **ANTI-FABRICATION**: Each row must cite Supporting Paths from GROUP A.

### Cross-Cutting Concerns

| Concern | Areas Affected | Boundary Note | Inertia Pattern |
|---|---|---|---|

> **ANTI-FABRICATION**: Boundary Note must reference a GROUP A finding.

### Headcount Signals

State headcount as a range (e.g., 4–7). Justify from the count of distinct expertise domains in the GROUP A scan table.

> **ANTI-FABRICATION**: Derive range from GROUP A domain count only.

### Org Shape

Name the shape (functional, product-aligned, platform, feature-team, embedded, or other). Justify from GROUP A findings by citing at least one file path and the dominant inertia pattern.

> **ANTI-FABRICATION**: Shape must be justified by Phase 1 evidence, not convention.

### Evidence Gaps

Name each gap explicitly. State the source type that would resolve it.

### Current State vs Recommended State

**Current State**: What GROUP A reveals about the existing structure.

**Recommended State**: What the analysis suggests the structure should become. Strictly separate from Current State.

---
---

## V-02: Inertia Framing

**Axis**: Inertia framing — the pattern dictionary is the primary analytical lens; every finding anchors to a named inertia pattern before file path citation; pattern distribution drives synthesis; the column order in the scan table reflects this priority.

**Hypothesis**: When inertia patterns are the primary organizing concept — not a secondary annotation column — the agent is forced to categorize each domain finding during Phase 1 rather than after. This surfaces structural pathologies during scanning, makes the dominant pattern visible before seam reasoning begins, and targets C-23 (dictionary constrain) and C-24 (pass token names dominant pattern) as outputs of the scan logic rather than format requirements bolted on after.

---

# org-scan

Walk the repo and infer the org structure. Output is **raw analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this scan into a full org.

> **OUTPUT CONSTRAINT**: Raw analysis only. No org chart. No reporting lines. No management hierarchy. *Restated in Phase 2 output format.*

---

### INERTIA PATTERN DICTIONARY

Defined before Phase 1. The Inertia Match column accepts only labels from this dictionary. Free text is structurally invalid — unconstrained values make pattern comparison across runs unverifiable.

| Label | Meaning |
|---|---|
| SILO | Domain enclosed; team acts independently; few cross-cutting connections |
| FRAGMENT | Domain split across multiple owners; coordination cost elevated |
| OVERLAP | Multiple teams claim or work the same domain |
| INHERIT | Structure inherited from prior state; not aligned to current needs |
| EXPAND | Team boundary growing beyond original scope |
| LOCK | Domain ownership frozen despite scope change |
| CENTRALIZE | Consolidation pressure toward a single owner or team |
| UNKNOWN | Pattern unclear from available evidence |

The Inertia Match column is a **REQUIRED column**. Empty cells in REQUIRED columns are structural gaps — not silently absent from prose.

---

### GATE TOKEN PROTOCOL

**PASS TOKEN**:
```
SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [LABEL]
```
Include the actual source count, path count, and the most frequent Inertia Match label from the scan table — making the token self-documenting about what it asserts.

**FAIL TOKEN**:
```
PATH FLOOR NOT MET — halt
```

---

## PHASE 1: PATTERN DETECTION SCAN

> **ANTI-FABRICATION**: Every area named must be traceable to a cited file path or named source type. Do not name areas without evidence.

For each domain area found, identify the Inertia Match pattern first, then cite evidence. Pattern identification drives the scan — look for signals of each pattern type in the source files.

### Source Coverage

Scan at least 3 of these 7:

1. `CLAUDE.md` files — namespace ownership, design intent, scope
2. `package.json` / build manifests — module boundaries, dependencies
3. `design/` or `specs/` directories — planned domains
4. Namespace directories — feature ownership topology
5. Test coverage areas — tested domains and gaps
6. `SPECS.md` files — stated scope and team assumptions
7. `.roles/` — explicit role definitions

**FILE PATH FLOOR**: You must cite at least 5 specific file paths before proceeding to Phase 2. If fewer than 5 paths are found, output the FAIL TOKEN and stop.

### Phase 1 Output: Pattern-Evidence Table

Required columns (empty cells in required columns are visible structural gaps):

| Area | Inertia Match | Source Type | File Path Evidence | Notes |
|---|---|---|---|---|

*Column order places Inertia Match before evidence — pattern identification precedes citation.*
*Inertia Match accepts only labels from the INERTIA PATTERN DICTIONARY above.*

---

### GATE

**Phase 1 postcondition / Phase 2 precondition**: scan table complete with 5+ paths, all Inertia Match values from the dictionary, no constraint violations. Both sides of this contract must hold.

Before Phase 2:
1. Source types cited: count ≥ 3?
2. File paths in File Path Evidence: count ≥ 5?
3. Inertia Match cells: all contain a dictionary label (not free text, not blank)?
4. No org chart or reporting lines in Phase 1 output?

If all pass — write the PASS TOKEN (include actual source count, actual path count, dominant pattern label):
`SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [LABEL]`

If file path floor not met — write the FAIL TOKEN:
`PATH FLOOR NOT MET — halt`

---

## PHASE 2: PATTERN-DRIVEN SYNTHESIS

> **OUTPUT CONSTRAINT (restatement)**: Raw analysis only. No org chart. No reporting lines.

> **ANTI-FABRICATION**: All synthesis draws from Phase 1 findings only. Seam candidates, headcount, and org shape must be grounded in Phase 1 evidence — not pattern familiarity or prior codebase knowledge.

### Pattern Distribution

| Pattern | Count | Interpretation |
|---|---|---|

Summarize the Inertia Match distribution from Phase 1. Which pattern(s) dominate? What does the distribution signal about org health?

### Current State

What Phase 1 reveals about the existing structure. Keep separate from Recommended State.

### Team Boundary Candidates

| Boundary | Seam Rationale | Dominant Inertia Pattern | Supporting Paths |
|---|---|---|---|

> **ANTI-FABRICATION**: Each row must cite Supporting Paths from Phase 1.

### Cross-Cutting Concerns

| Concern | Areas Affected | Boundary Note | Driving Pattern |
|---|---|---|---|

### Headcount Signals

Range (e.g., 4–7) with rationale from the count of distinct expertise domains in the Phase 1 table.

### Org Shape

Named shape justified from Phase 1 findings including the dominant inertia pattern. Do not name a shape unsupported by the scan.

### Evidence Gaps

What was not findable. Source type that would resolve each gap.

### Recommended State

What the analysis suggests the structure should become. Separated from Current State above.

---
---

## V-03: Output Format (Schema-First)

**Axis**: Output format — the skill declares a complete output schema with REQUIRED column tags before Phase 1 begins; all output fills that schema; empty REQUIRED cells are structurally visible gaps, not absent prose.

**Hypothesis**: Declaring the full schema first — with REQUIRED explicitly tagged — makes the agent treat the schema as a contract to fill rather than a structure to imitate. Empty cells in REQUIRED columns become structural failures visible in the output table without requiring prose inspection. This maximizes C-21 compliance while keeping C-19 (Inertia Match column) constrained by the Inertia Pattern Dictionary embedded in the schema declaration.

---

# org-scan

Walk the repo and infer the org structure. Output is **raw analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this scan into a full org.

> **OUTPUT CONSTRAINT**: Raw analysis only. No org chart. No reporting lines. No management hierarchy. *Restated in Output Schema below.*

---

### OUTPUT SCHEMA

Declared before Phase 1. Columns marked **[REQUIRED]** must be populated. Empty cells in REQUIRED columns are **structural gaps visible in the table** — they are not hidden in prose.

#### Schema A — Phase 1 Scan Table

| Column | Status | Constraint |
|---|---|---|
| Area | REQUIRED | Traceable to a cited file path |
| Source Type | REQUIRED | One of the 7 named source types |
| File Path Evidence | REQUIRED | Specific path(s) from the repo |
| Inertia Match | REQUIRED | Label from Inertia Pattern Dictionary only (see below) |
| Notes | optional | Supplemental context |

*Valid Inertia Match values*: SILO, FRAGMENT, OVERLAP, INHERIT, EXPAND, LOCK, CENTRALIZE, UNKNOWN. Free text is not a valid Inertia Match entry.

#### Schema B — Team Boundary Candidates

| Column | Status |
|---|---|
| Boundary | REQUIRED |
| Seam Rationale | REQUIRED |
| Inertia Patterns Involved | REQUIRED |
| Supporting Paths (from Schema A) | REQUIRED |

#### Schema C — Cross-Cutting Concerns

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Areas Affected | REQUIRED |
| Boundary Note | REQUIRED |
| Inertia Pattern | REQUIRED |

> **OUTPUT CONSTRAINT (restatement)**: Schema B and Schema C produce raw analysis. No reporting lines. No org chart.

---

### GATE TOKEN PROTOCOL

**PASS TOKEN**:
```
SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [LABEL]
```
Include actual source count, actual path count, and the most frequent Inertia Match label from Schema A — making the token self-documenting about what it asserts.

**FAIL TOKEN**:
```
PATH FLOOR NOT MET — halt
```

---

### INERTIA PATTERN DICTIONARY

Embedded before Phase 1. Constrains the Inertia Match column in Schema A.

| Label | Meaning |
|---|---|
| SILO | Domain enclosed; team acts independently; few cross-cutting connections |
| FRAGMENT | Domain split across multiple owners; coordination cost elevated |
| OVERLAP | Multiple teams claim or work the same domain |
| INHERIT | Structure inherited from prior state; not aligned to current needs |
| EXPAND | Team boundary growing beyond original scope |
| LOCK | Domain ownership frozen despite scope change |
| CENTRALIZE | Consolidation pressure toward a single owner or team |
| UNKNOWN | Pattern unclear from available evidence |

---

### CURRENT STATE vs RECOMMENDED STATE

Phase 2 output must maintain strict separation. These are distinct labeled sections. Do not blend them.

---

## PHASE 1: SCAN

> **ANTI-FABRICATION**: Every row in Schema A must be traceable to a cited file path. Do not populate Area without File Path Evidence.

#### Source Types

Scan at least 3 of these 7:

1. `CLAUDE.md` files
2. `package.json` / build manifests
3. `design/` or `specs/` directories
4. Namespace directories
5. Test coverage areas
6. `SPECS.md` files
7. `.roles/`

**FILE PATH FLOOR (GATE CONDITION)**: At least 5 specific file paths must appear in Schema A before Phase 2 proceeds. This is a gate condition — not an output expectation. If fewer than 5 paths are found, output the FAIL TOKEN and stop.

Produce Schema A now. All REQUIRED columns must be populated per the Output Schema declaration above.

---

### GATE CHECK

**Phase 1 postcondition / Phase 2 precondition**: Schema A is complete with all REQUIRED columns populated, 5+ paths present, all Inertia Match values from the dictionary, no constraint violations. Both sides name the same conditions.

Verify before proceeding:

1. Schema A REQUIRED columns: are all populated in every row?
2. Source types: count distinct named source types — is the count ≥ 3?
3. File paths: count distinct paths in File Path Evidence — is the count ≥ 5?
4. Inertia Match: does each cell contain a dictionary label (not blank, not free text)?
5. Constraint: does any line contain org chart structure or reporting lines?

If all pass, write the PASS TOKEN:
`SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [LABEL]`

If path floor not met:
`PATH FLOOR NOT MET — halt`

---

## PHASE 2: SYNTHESIS

> **ANTI-FABRICATION**: Synthesis draws only from Schema A. Schema B seam rationale must cite Supporting Paths. Schema C boundary notes must reference Schema A findings. Headcount must derive from Schema A domain count. Org shape must be justified by Schema A evidence.

Produce the following sections, using required schemas where applicable:

**Current State** — prose narrative of what Schema A reveals about existing structure.

**Schema B** — Team Boundary Candidates table. Each row must cite Supporting Paths from Schema A.

**Schema C** — Cross-Cutting Concerns table. Boundary Note must reference a Schema A finding.

**Headcount Signals** — range with rationale from distinct expertise domain count in Schema A.

**Org Shape** — named shape (functional, product-aligned, platform, feature-team, embedded, or other) justified from Schema A findings including dominant Inertia Match pattern.

**Evidence Gaps** — what was not findable; source type that would resolve each gap.

**Recommended State** — what the analysis suggests the structure should become. Clearly separated from Current State above.

---
---

## V-04: Lifecycle + Inertia Combined

**Axis**: Combined — GROUP A / GROUP B lifecycle machinery (V-01) + inertia pattern dictionary as primary analytical lens (V-02).

**Hypothesis**: Combining explicit GROUP labels with inertia-pattern-first scanning produces the strongest structural integrity: the GROUP boundary enforces scan-before-synthesis while the pattern dictionary makes every finding double-constrained — it must anchor to a dictionary label AND cite a file path. The two mechanisms are orthogonal and mutually reinforcing, and together they produce the densest coverage of C-19 through C-24 without any mechanism depending on another for its effect.

---

# org-scan

Walk the repo and infer the org structure. Output is **raw analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this scan into a full org.

> **OUTPUT CONSTRAINT (preamble)**: Raw analysis only. No org chart. No reporting lines. No management hierarchy. *Restated in GROUP B output format below.*

---

### GATE TOKEN PROTOCOL

Both tokens are named constants. Defined before Phase 1 begins.

**PASS TOKEN**:
```
SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN_LABEL]
```
The token is self-documenting: it names source count, path count (asserting path floor status), and dominant pattern name — making it self-reporting about the three key conditions it verifies.

**FAIL TOKEN**:
```
PATH FLOOR NOT MET — halt
```

---

### INERTIA PATTERN DICTIONARY

Defined before Phase 1. The Inertia Match column accepts only labels from this dictionary. Free text is invalid.

| Label | Meaning |
|---|---|
| SILO | Domain enclosed; team acts independently; few cross-cutting connections |
| FRAGMENT | Domain split across multiple owners; coordination cost elevated |
| OVERLAP | Multiple teams claim or work the same domain |
| INHERIT | Structure inherited from prior state; not aligned to current needs |
| EXPAND | Team boundary growing beyond original scope |
| LOCK | Domain ownership frozen despite scope change |
| CENTRALIZE | Consolidation pressure toward a single owner or team |
| UNKNOWN | Pattern unclear from available evidence |

---

### OUTPUT SCHEMA — Phase 1 Scan Table

Required columns — empty cells in REQUIRED columns are visible structural gaps:

| Column | Status | Constraint |
|---|---|---|
| Area | REQUIRED | Traceable to a cited file path |
| Inertia Match | REQUIRED | Label from INERTIA PATTERN DICTIONARY only |
| Source Type | REQUIRED | One of the 7 named source types |
| File Path Evidence | REQUIRED | Specific path(s) from the repo |
| Notes | optional | Supplemental context |

*Column order places Inertia Match before evidence — pattern identification precedes citation.*

---

## GROUP A: CURRENT STATE

> **ANTI-FABRICATION**: All areas in GROUP A must be traceable to a cited file path or named source type. Do not name areas without evidence.

### Source Coverage

Scan at least 3 of these 7:

1. `CLAUDE.md` files — namespace ownership, design intent, scope signals
2. `package.json` / build manifests — dependency graph, module boundaries
3. `design/` or `specs/` directories — planned areas of work
4. Namespace directories — feature ownership topology
5. Test coverage areas — tested domains, coverage gaps
6. `SPECS.md` files — stated scope and team assumptions
7. `.roles/` — explicit role definitions

**FILE PATH FLOOR (GATE PRECONDITION)**: Minimum 5 specific file paths in File Path Evidence is a precondition for Phase 2. If fewer than 5 paths are found, output the FAIL TOKEN and stop. Do not proceed.

Produce the Phase 1 Scan Table now. All REQUIRED columns must be populated.

---

### GATE CHECK — Phase 1 Postcondition / Phase 2 Precondition

**Phase 1 postcondition** (must hold before Phase 1 terminates):
- Schema REQUIRED columns: all populated in every row
- Source types: 3+ distinct types cited
- File paths: 5+ specific paths in File Path Evidence
- Inertia Match: all cells contain a dictionary label (not blank, not free text)
- No org chart or reporting lines in GROUP A output

**Phase 2 precondition** (must be confirmed before GROUP B begins):
- Schema REQUIRED columns: all populated in every row
- Source types: 3+ distinct types cited
- File paths: 5+ specific paths in File Path Evidence
- Inertia Match: all cells contain a dictionary label
- No org chart or reporting lines in GROUP A output

These two statements name the same contract from both sides. Both must hold.

Verification checklist:
1. REQUIRED columns: are all populated in every row?
2. Source types: count distinct named source types — is the count ≥ 3?
3. File paths: count distinct paths in File Path Evidence — is the count ≥ 5?
4. Inertia Match: inspect each cell — does each contain a dictionary label?
5. Constraint: inspect all GROUP A output — does any line contain org chart or reporting lines?

If all five conditions pass, write the PASS TOKEN:
`SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN_LABEL]`

If path floor not met, write: `PATH FLOOR NOT MET — halt`

---

## GROUP B: RECOMMENDED STATE

> **OUTPUT CONSTRAINT (restatement)**: Raw analysis only. No org chart. No reporting lines. No management hierarchy.

> **ANTI-FABRICATION**: All GROUP B synthesis draws from GROUP A findings. Seam candidates must cite Supporting Paths. Headcount must derive from GROUP A domain count. Org shape must be justified by Phase 1 evidence — not convention, pattern familiarity, or assumption.

### Pattern Distribution

| Pattern | Count | Signal |
|---|---|---|

Summarize the Inertia Match distribution from GROUP A. Which pattern dominates?

### Current State

What GROUP A reveals about the existing structure. Keep separate from Recommended State.

### Team Boundary Candidates

| Boundary | Seam Rationale | Dominant Inertia Pattern | Supporting Paths |
|---|---|---|---|

> **ANTI-FABRICATION**: Each row must cite Supporting Paths from GROUP A.

### Cross-Cutting Concerns

| Concern | Areas Affected | Boundary Note | Driving Pattern |
|---|---|---|---|

> **ANTI-FABRICATION**: Boundary Note must reference a GROUP A finding.

### Headcount Signals

Range (e.g., 4–7) with rationale from the count of distinct expertise domains in GROUP A.

### Org Shape

Named shape (functional, product-aligned, platform, feature-team, embedded, or other) justified from GROUP A findings including the dominant inertia pattern.

### Evidence Gaps

What was not findable. Source type that would resolve each gap.

### Recommended State

What the analysis suggests the structure should become. Clearly separated from Current State above.

---
---

## V-05: All Axes — Maximum Coverage

**Axis**: Combined — lifecycle GROUP machinery (V-01) + inertia dictionary as primary lens (V-02) + schema-first output declaration (V-03) + symmetric anti-fabrication in both GROUP A and GROUP B + formal bidirectional phase contract + self-documenting pass token with all three conditions named.

**Hypothesis**: Full combination of lifecycle GROUP labels, schema-first output declaration with REQUIRED column tags, inertia pattern dictionary as constrained vocabulary, formal bidirectional phase contracts, self-documenting pass token, and symmetric anti-fabrication in both phases produces the highest composite score by making each of the 24 criteria structurally enforced rather than present only in prose — and by ensuring that all four v6-new criteria (C-21 through C-24) are addressed by dedicated, named mechanisms rather than implied by neighboring structure.

---

# org-scan

Walk the repo and infer the org structure. Output is **raw analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this scan into a full org.

> **OUTPUT CONSTRAINT (preamble)**: Raw analysis only. No org chart. No reporting lines. No management hierarchy. *Restated in GROUP B output schema below.*

---

### GATE TOKEN PROTOCOL

Both tokens are named constants. Defined before Phase 1 begins.

**PASS TOKEN** — write this format when all gate conditions are satisfied:
```
SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN_LABEL]
```
The token is self-documenting: it asserts source count, path floor status (via path count), and dominant inertia pattern name — naming the three key conditions it verifies.

**FAIL TOKEN** — write this exact string when the file path floor is not met:
```
PATH FLOOR NOT MET — halt
```

---

### INERTIA PATTERN DICTIONARY

Defined before Phase 1. The Inertia Match column in Schema A accepts only these labels. Free text is structurally invalid — unconstrained values make the column unverifiable and cross-run pattern comparison impossible.

| Label | Meaning |
|---|---|
| SILO | Domain enclosed; team acts independently; few cross-cutting connections |
| FRAGMENT | Domain split across multiple owners; coordination cost elevated |
| OVERLAP | Multiple teams claim or work the same domain |
| INHERIT | Structure inherited from prior state; not aligned to current needs |
| EXPAND | Team boundary growing beyond original scope |
| LOCK | Domain ownership frozen despite scope change |
| CENTRALIZE | Consolidation pressure toward a single owner or team |
| UNKNOWN | Pattern unclear from available evidence |

---

### OUTPUT SCHEMA

Declared before Phase 1. Columns marked **[REQUIRED]** must be populated. Empty cells in REQUIRED columns are **structural gaps visible in the table** — not silently absent from prose.

#### Schema A — Phase 1 Scan Table

| Column | Status | Constraint |
|---|---|---|
| Area | REQUIRED | Traceable to a cited file path |
| Inertia Match | REQUIRED | Label from INERTIA PATTERN DICTIONARY only |
| Source Type | REQUIRED | One of the 7 named source types |
| File Path Evidence | REQUIRED | Specific path(s) from the repo |
| Notes | optional | Supplemental context |

#### Schema B — Team Boundary Candidates

| Column | Status |
|---|---|
| Boundary | REQUIRED |
| Seam Rationale | REQUIRED |
| Inertia Patterns Involved | REQUIRED |
| Supporting Paths (from Schema A) | REQUIRED |

#### Schema C — Cross-Cutting Concerns

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Areas Affected | REQUIRED |
| Boundary Note | REQUIRED |
| Inertia Pattern | REQUIRED |

---

### CURRENT STATE vs RECOMMENDED STATE

Phase 2 output must maintain strict separation. Do not blend them. They must appear as distinct labeled sections.

---

## GROUP A: CURRENT STATE

> **ANTI-FABRICATION**: All areas in Schema A must be traceable to a cited file path or named source type. Do not populate Area without File Path Evidence.

### Source Coverage

Scan at least 3 of these 7:

1. `CLAUDE.md` files — namespace ownership, design intent, scope signals
2. `package.json` / build manifests — dependency graph, module boundaries
3. `design/` or `specs/` directories — planned areas of work
4. Namespace directories — feature ownership topology
5. Test coverage areas — tested domains, coverage gaps
6. `SPECS.md` files — stated scope and team assumptions
7. `.roles/` — explicit role definitions

**FILE PATH FLOOR (GATE CONDITION)**: A minimum of 5 specific file paths in File Path Evidence is a precondition for Phase 2. This is a gate condition — not merely an output expectation. If fewer than 5 paths are found, output the FAIL TOKEN and stop.

Produce Schema A now. All REQUIRED columns must be populated per the Output Schema declaration above.

---

### GATE CHECK — Phase 1 Postcondition / Phase 2 Precondition

**Phase 1 postcondition** (must hold before Phase 1 terminates):
- Schema A REQUIRED columns: all populated in every row
- Source types: 3+ distinct types cited and named
- File paths: 5+ specific paths in File Path Evidence
- Inertia Match: all cells contain a label from the Inertia Pattern Dictionary
- No org chart or reporting lines present in GROUP A output

**Phase 2 precondition** (must be confirmed before GROUP B begins):
- Schema A REQUIRED columns: all populated in every row
- Source types: 3+ distinct types cited and named
- File paths: 5+ specific paths in File Path Evidence
- Inertia Match: all cells contain a label from the Inertia Pattern Dictionary
- No org chart or reporting lines present in GROUP A output

These two statements name the same contract from both sides. Both must hold.

Verification checklist:
1. REQUIRED columns: are all populated in every row of Schema A?
2. Source types: count distinct named source types — is the count ≥ 3?
3. File paths: count distinct paths in File Path Evidence — is the count ≥ 5?
4. Inertia Match: inspect each cell — does each contain a dictionary label (not blank, not free text)?
5. Constraint: inspect all GROUP A output — does any line contain org chart structure or reporting lines?

If all five conditions pass, write the PASS TOKEN:
`SCAN GATE CLEAR — [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN_LABEL]`

If path floor not met, write: `PATH FLOOR NOT MET — halt`

---

## GROUP B: RECOMMENDED STATE

> **OUTPUT CONSTRAINT (restatement)**: Raw analysis only. No org chart. No reporting lines. No management hierarchy.

> **ANTI-FABRICATION**: All GROUP B synthesis draws from Schema A. Seam candidates must cite Supporting Paths. Cross-cutting boundary notes must reference Schema A findings. Headcount must derive from Schema A domain count. Org shape must be justified by Phase 1 evidence — not convention, pattern familiarity, or inference beyond what the scan supports.

### Pattern Distribution

| Pattern | Count | Signal |
|---|---|---|

Summarize the Inertia Match distribution from Schema A. Which pattern(s) dominate? What does the distribution signal?

### Current State

What Schema A reveals about the existing structure. Keep separate from Recommended State.

### Team Boundary Candidates

Produce Schema B. Each row must cite Supporting Paths from Schema A.

> **ANTI-FABRICATION**: Seam Rationale and Inertia Patterns Involved must be grounded in Schema A rows.

### Cross-Cutting Concerns

Produce Schema C. Boundary Note must reference a Schema A finding.

> **ANTI-FABRICATION**: Concern, Areas Affected, and Inertia Pattern must be traceable to Schema A evidence.

### Headcount Signals

Range (e.g., 4–7) with rationale from the count of distinct expertise domains in Schema A.

> **ANTI-FABRICATION**: Derive from Schema A domain count only. Do not extrapolate.

### Org Shape

Named shape (functional, product-aligned, platform, feature-team, embedded, or other) justified from Schema A findings, including the dominant inertia pattern.

> **ANTI-FABRICATION**: Must be justified by Phase 1 evidence, not convention or assumption.

### Evidence Gaps

What was not findable. Source type that would resolve each gap.

### Recommended State

What the analysis suggests the structure should become. Clearly separated from Current State above.

---

## Criteria Coverage by Variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-01** Areas traceable | PASS | PASS | PASS | PASS | PASS |
| **C-02** 3+/7 source types | PASS | PASS | PASS | PASS | PASS |
| **C-03** Headcount range | PASS | PASS | PASS | PASS | PASS |
| **C-04** Cross-cutting + boundary | PASS | PASS | PASS | PASS | PASS |
| **C-05** Raw analysis only | PASS | PASS | PASS | PASS | PASS |
| **C-06** Boundary candidates + seam | PASS | PASS | PASS | PASS | PASS |
| **C-07** Org shape named | PASS | PASS | PASS | PASS | PASS |
| **C-08** Evidence gaps | PASS | PASS | PASS | PASS | PASS |
| **C-09** 5+ file paths | PASS | PASS | PASS | PASS | PASS |
| **C-10** Current vs recommended separated | PASS | PASS | PASS | PASS | PASS |
| **C-11** Anti-fabrication per section | PASS | PASS | PASS | PASS | PASS |
| **C-12** Hard sequencing gate | PASS | PASS | PASS | PASS | PASS |
| **C-13** C-05 stated twice | PASS | PASS | PASS | PASS | PASS |
| **C-14** Verification checklist + confirmation | PASS | PASS | PASS | PASS | PASS |
| **C-15** GROUP A / GROUP B labels | PASS | — | — | PASS | PASS |
| **C-16** Path floor as gate condition | PASS | PASS | PASS | PASS | PASS |
| **C-17** Named-token confirmation | PASS | PASS | PASS | PASS | PASS |
| **C-18** Named failure string | PASS | PASS | PASS | PASS | PASS |
| **C-19** Inertia Match column | PASS | PASS+ | PASS | PASS+ | PASS+ |
| **C-20** GATE TOKEN PROTOCOL block | PASS | PASS | PASS | PASS | PASS |
| **C-21** Required table column enforcement | PASS | PASS | PASS+ | PASS+ | PASS+ |
| **C-22** Formal phase contract (bidirectional) | PASS+ | PASS | PASS | PASS+ | PASS+ |
| **C-23** Inertia pattern dictionary | PASS | PASS+ | PASS | PASS+ | PASS+ |
| **C-24** Self-documenting pass token | PASS | PASS+ | PASS+ | PASS+ | PASS+ |

**Notes**:
- V-01 C-15: explicit GROUP A / GROUP B headers throughout; C-22 PASS+ because phase contract is the lead mechanism
- V-02 C-15: Phase 1 / Phase 2 labels used, not GROUP labels — C-15 risk
- V-03 C-15: Phase 1 / Phase 2 labels — C-15 risk; C-21 PASS+ because schema declaration is the lead mechanism
- V-04: strongest combined coverage; GROUP labels + dictionary both get full treatment
- V-05: all mechanisms at full strength; symmetric anti-fabrication in both phases; four v6-new criteria explicitly addressed

**Excellence differentiators for scoring**:
- V-02/V-04/V-05: pattern dictionary drives column order (Inertia Match before File Path Evidence) — C-23 strongest
- V-03/V-04/V-05: REQUIRED column tag in schema declaration — C-21 strongest
- V-01/V-04/V-05: GROUP labels + explicit P1 postcondition / P2 precondition — C-22 strongest
- V-02/V-03/V-04/V-05: pass token includes dominant pattern label explicitly — C-24
