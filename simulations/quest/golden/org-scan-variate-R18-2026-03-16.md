---
skill: quest-variate
skill_target: org-scan
round: 18
date: 2026-03-16
rubric_version: 18
---

# org-scan Skill Body Prompt Variations V-01 through V-05
## Targeting rubric v18 (C-01 through C-66)
## Round 18 -- 2026-03-16

R17 V-02 produced C-64 (`Output Consumers` block), V-03 produced C-65 (`COVERAGE ATTESTATION`
table), V-04 produced C-66 (`TABLE H -- Org Shape Delta`), V-05 combined all three. All three
are structural invariants for R18 -- every variation must include them alongside the full
C-01 through C-63 stack.

R18 treats these as floor obligations and explores four new axes for C-67+ signals:

- **Axis 1** (V-02): Table-level Output Consumers payload -- each `Output Consumers` entry
  names not only the consuming role but the specific tables it consumes and the analytical
  purpose each table serves in that role's phase. Role-level Output Consumers (C-64) names
  the edge; table-payload Output Consumers enumerates the transport manifest per edge.

- **Axis 2** (V-03): COVERAGE ATTESTATION schema-declared -- elevated from a named output
  produced at SCANNER exit to a first-class entry in SCHEMA DECLARATION with column definitions,
  REQUIRED annotations, and `Minimum rows: 7` (one per source type). Extends C-61's Minimum
  rows protocol to the coverage audit table, making row-floor violations structurally detectable
  without reading the SCANNER phase instructions.

- **Axis 3** (V-04): TABLE H Minimum rows annotation + bridge rule -- TABLE H receives
  `Minimum rows: [N = TABLE E count]` in SCHEMA DECLARATION (every boundary candidate maps
  to at least one org shape dimension), plus a named bridge rule: any TABLE H row where
  Recommended State != Current State must produce a TABLE F gap entry. Closes the loop between
  shape recommendations and tracked gaps at schema level.

- **Combined** (V-05): All three axes active simultaneously. Tests whether table-payload
  consumers, schema-declared attestation, and TABLE H minimum rows with bridge rule interact
  constructively or create structural tension.

All R17 invariants (C-58 through C-63) and all prior-round invariants (C-09 through C-57) are
preserved in all variations. No criterion is weakened or removed.

---

## Variation Axes

| Axis | Used In |
|---|---|
| Baseline R18 -- C-01 through C-66 as invariants, no new axis | V-01 |
| Role sequence -- table-level payload in each Output Consumers entry | V-02 |
| Output format -- COVERAGE ATTESTATION schema-declared with Minimum rows: 7 | V-03 |
| Lifecycle emphasis -- TABLE H Minimum rows + TABLE H / TABLE F bridge rule | V-04 |
| Full combination: table-payload consumers + attestation schema + TABLE H bridge | V-05 |

---

## V-01

**Variation axis**: Baseline R18. C-64, C-65, C-66 incorporated as structural invariants
alongside the full C-01 through C-63 stack. No new axis applied. V-17 V-05 promoted as floor.

**Hypothesis**: V-01 scores 100/100 under rubric v18 (all 58 aspirational criteria firing,
capped at 10). Any variation scoring above V-01 has identified a structural property beyond
C-66. V-01 is the control condition.

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column. Minimum rows
annotations are gate-level obligations -- a table below its floor blocks the corresponding
phase transition.

TABLE A -- Hypothesis Table
Produced by: PREDICTOR before any scan evidence is collected.
Minimum rows: 6 (one row per named pattern I-01 through I-06)

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

TABLE B -- Scan Evidence Table
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 5 (path floor -- EVIDENCE GATE blocks if fewer than 5 rows with File Path
Evidence populated)

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (I-01 through I-07 only -- free text is a schema violation) |
| File Path Evidence | REQUIRED (specific file path -- directory names alone do not satisfy) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match BEFORE File Path Evidence. Inverting the order is a schema
violation. Pattern identification precedes evidence citation as a structural column constraint.

TABLE C -- Headcount Signals
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 2 (at least 2 distinct expertise domains required for range rationale)

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value -- "3-5" not "4") |

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 1 (if none found, write one row: Concern = "none detected", Boundary Note =
"no cross-team dependency evidence in scanned sources", File Path Evidence = "N/A -- absence
recorded explicitly")

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 2

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row by number -- "TABLE B row N" format) |
| Supporting Evidence | REQUIRED |

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 0 (absence is valid -- if TABLE F has 0 rows, write "Gap audit complete --
no evidence gaps identified" rather than leaving the table absent)

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage.
Minimum rows: N (must equal TABLE A count -- execution-time assertion at SYNTHESIZER entry
establishes N before TABLE G production begins)

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row by number) |
| Resolution | REQUIRED (confirmed / refuted / partial / unresolved) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. Named
remediation path for unresolved predictions: add TABLE G row with Resolution = "unresolved"
and Evidence Summary = "no evidence found", then add TABLE F row with Gap =
"[PATTERN-ID] prediction unresolved", Implication = "hypothesis not tested against scan
evidence", Source Types Checked = [source types scanned].

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 1

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row -- "TABLE B row N" format required;
  prose citation without row reference is a schema violation) |

---

GATE TOKEN PROTOCOL

Three gates govern this skill. All three are fully defined here before Phase 1 begins.
No gate uses prose substitution -- only the named tokens below are valid at gate boundaries.

HYPOTHESIS FLOOR GATE (Phase 1 exit):
PASS: Hypothesis floor clear -- [N] patterns predicted, TABLE A has [N] rows, floor met
FAIL: Hypothesis floor not met -- [N] rows in TABLE A, 6 required

EVIDENCE GATE (Phase 2 exit):
PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
PASS: Synthesis complete -- [N] TABLE A rows, [N] TABLE G rows, all predictions resolved
FAIL: Synthesis incomplete -- [N] TABLE A rows, [N] TABLE G rows, [N] predictions unresolved

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from
prediction through verification through synthesis. PREDICTOR applies it in Phase 1 to generate
hypotheses before reading any file -- each TABLE A row must anchor to one dictionary pattern.
SCANNER applies it in Phase 2 to label every TABLE B finding -- the Inertia Match column is
the per-row application of this framework to scan evidence. SYNTHESIZER applies it in Phase 3
to resolve predictions -- every TABLE G resolution cites the dictionary pattern predicted and
the evidence that confirms, refutes, or partially supports it.

Free text in the Inertia Match column is structurally invalid. Only I-01 through I-07 values
are permitted. Unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, and ownership language). PREDICTOR must predict
both registers. SCANNER must check both.

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone" |
| I-02 | Accidental Silos | Multiple directories but no ownership docs; test coverage overlaps across directories; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall without a clear reviewer; incidents involve multiple teams guessing |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain tests; explicit ownership in docs or .roles | "that's the X team's area"; clear escalation path per domain; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer (sdk/, core/, utils/, platform/) distinct from product surfaces; infra layer has own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team separate on-call; product features rarely touch infra |
| I-05 | Federated | Multiple autonomous workspaces with minimal shared root; independent CI per workspace; rare central merge events | "each team ships independently"; incidents scoped to one workspace; "we don't need to coordinate on that" |
| I-06 | Hub-and-Spoke | Central orchestrator directory (nexus/, hub/, core/, router/) with peripherals radiating from it; hub has disproportionate test coverage and documentation depth | "everything routes through the hub"; hub team is bottleneck for peripheral changes; peripheral teams file issues against hub |
| I-07 | Undefined | Fewer than 3 source types readable; evidence insufficient to classify | Cannot assess behavioral signals; pattern classification deferred |

---

GROUP A -- PREDICTOR PHASE

ROLE SCOPE DECLARATION: PREDICTOR
Input Dependencies:
  - Skill invocation (no prior phase output required)
Output Consumers:
  - SCANNER: reads TABLE A to cross-check each finding against the predicted hypothesis set
Violated when: scan evidence from file reads appears in TABLE A rows; TABLE B, C, D, E, F, G,
  or H production occurs during Phase 1
Authority: PAF Phase 1 binding -- "PREDICTOR applies the dictionary before reading any file"
Permitted outputs: TABLE A only
Prohibited outputs: file reads, TABLE B/C/D/E/F/G/H production, synthesis conclusions, org
  chart content

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction (what code-level signals you expect to find or not find) and a behavioral
prediction (what team-language or ownership signals you expect to find in CLAUDE.md prose). Set
Hypothesis Held based on your expectation before any evidence.

Anti-fabrication: No file reading occurs in Phase 1. TABLE A is prediction only. No Finding
cells may reference any actual file content.

-> Output TABLE A (minimum 6 rows, one per pattern I-01 through I-06).

HYPOTHESIS FLOOR GATE CHECK:
Count TABLE A rows. If fewer than 6: write "Hypothesis floor not met -- [N] rows in TABLE A,
6 required" and halt. If 6+: write "Hypothesis floor clear -- [N] patterns predicted" and
continue.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. TABLE A must exist and must have passed the hypothesis floor gate.
ROLE SCOPE DECLARATION for SCANNER follows at Phase 2 start.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Input Dependencies:
  - PREDICTOR COMPLETE declaration
  - TABLE A (all rows -- findings cross-reference the matching prediction)
Output Consumers:
  - SYNTHESIZER: reads TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Violated when: TABLE E, F, G, or H rows produced before EVIDENCE GATE passage; synthesis
  conclusions drawn during Phase 2; org chart content in any Phase 2 output
Authority: PAF Phase 2 binding -- "SCANNER labels every TABLE B finding with a dictionary
  pattern ID"
Permitted outputs: TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Prohibited outputs: hypothesis generation, TABLE E/F/G/H production, synthesis conclusions,
  org chart content

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE declaration present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences as explicit
findings. Do not infer from file names alone.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language
-- these are behavioral signal evidence for TABLE B Behavioral findings.

File path floor (EVIDENCE GATE precondition): TABLE B must have 5+ rows with File Path
Evidence populated. This blocks gate passage.

-> Output TABLE B (minimum 5 rows with populated File Path Evidence column).
-> Output TABLE C (minimum 2 rows with distinct expertise domains).
-> Output TABLE D (minimum 1 row; absence recorded explicitly per schema rule).
-> Output COVERAGE ATTESTATION (all 7 source types enumerated).

COVERAGE ATTESTATION
Produced at SCANNER phase exit. One row per source type. Status constrained to three values:
- scanned: source type present and read; evidence collected
- not-found: source type applicable to this repo but no evidence found in scan
- not-applicable: source type structurally absent from this repo (e.g., no .roles/
  because org-build has not been run; no design/ because project has no design artifacts)

| Source Type | Status | Notes |
|---|---|---|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [brief note] |
| package.json (root and nested) | [scanned / not-found / not-applicable] | [brief note] |
| design/ or docs/ directories | [scanned / not-found / not-applicable] | [brief note] |
| Namespace directories | [scanned / not-found / not-applicable] | [brief note] |
| Test coverage areas | [scanned / not-found / not-applicable] | [brief note] |
| SPECS.md or specification files | [scanned / not-found / not-applicable] | [brief note] |
| .roles/ or role definitions | [scanned / not-found / not-applicable] | [brief note] |

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" before proceeding.

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name
the same contract -- the bilateral contract declaration makes gate passage verifiable in either
direction.

Named gate entry condition: SCANNER COMPLETE declaration must appear above.

Gate checklist -- evaluate each item in order; do not skip:
1. SCANNER COMPLETE declaration present above
2. TABLE B has 5+ rows with File Path Evidence populated (path floor)
3. At least 3 of 7 source types appear in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token exactly as defined in GATE TOKEN PROTOCOL. No prose substitution.

If item 2 fails: write "Path floor not met -- [N] paths found, 5 required" and halt.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

FAIL TOKEN halts all further execution. PASS TOKEN permits SYNTHESIZER to begin.
ROLE SCOPE DECLARATION for SYNTHESIZER follows at Phase 3 start.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Input Dependencies:
  - PASS TOKEN at SCANNER / GATEKEEPER boundary (execution blocks if FAIL TOKEN present)
  - TABLE A (for TABLE G prediction-resolution matching)
  - TABLE B (for evidence citation in TABLE E, TABLE G, TABLE H)
  - TABLE C (for Headcount Range derivation)
  - TABLE D (for cross-cutting synthesis)
  - COVERAGE ATTESTATION (not-found rows are candidates for TABLE F gap entries)
Output Consumers:
  - org-build: reads TABLE G and TABLE H
Violated when: org chart content appears in any output table; new TABLE B evidence rows
  produced during Phase 3; "reports to" or hierarchy language in any section
Authority: PAF Phase 3 binding -- "SYNTHESIZER resolves TABLE A predictions against labeled
  TABLE B evidence"
Permitted outputs: TABLE E, TABLE F, TABLE G, TABLE H, Org Shape section, Headcount Range
Prohibited outputs: org chart content, hypothesis generation, new scan evidence

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here per critical constraint double-declaration requirement.)

Phase 3: Synthesis

Entry condition: PASS TOKEN present at SCANNER / GATEKEEPER boundary above.

Execution-time assertion (before TABLE G production):
Write: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."
This line makes hypothesis closure verifiable by comparing the asserted count against the
actual TABLE G row count without prose inspection.

-> Output TABLE E. Every Seam Rationale cell must cite TABLE B by row number ("TABLE B row
   N"). Prose citation without row reference is a schema violation.

-> Output TABLE F. Check COVERAGE ATTESTATION for not-found rows -- each not-found source
   type is a candidate TABLE F entry (Gap = "[source type] not found in scan", Implication =
   "[what evidence this source type would have provided]", Source Types Checked = that type).
   If TABLE F has 0 rows after all checks: write "Gap audit complete -- no evidence gaps
   identified."

-> Output TABLE G. Apply completeness rule and named remediation path for unresolved
   predictions. Evidence Summary must cite TABLE B by row number.

-> Output TABLE H -- Org Shape Delta. Every Driving Evidence cell must cite TABLE B by row
   number. Dimensions must be derived from TABLE B findings, not invented.

-> Write Org Shape section: name the dominant pattern from the PASS TOKEN. Separate CURRENT
   STATE (citable to TABLE B structural and behavioral findings) from RECOMMENDED STATE (what
   the TABLE G resolution outcomes imply about org investment). Do not produce a reporting
   structure or org chart.

-> Write Headcount Range: a numeric range derived from TABLE C rows (e.g., "3-6 team areas,
   15-25 FTE"). Rationale must explain why each TABLE C expertise domain signals distinct
   headcount.

Phase 3 exit: Write "SYNTHESIZER COMPLETE" before proceeding.

---

SYNTHESIS COMPLETENESS GATE (Phase 3 exit)

Gate checklist:
1. SYNTHESIZER COMPLETE declaration present above
2. TABLE G row count = TABLE A row count (per execution-time assertion)
3. Every TABLE A Pattern ID appears in TABLE G Pattern ID column
4. TABLE H has at least 1 row with Driving Evidence citing TABLE B by row number
5. No org chart content in any table or section

Write SYNTHESIS COMPLETENESS GATE PASS or FAIL token. No prose substitution.

---

SYNTHESIZER / END BOUNDARY

Skill complete. Three-phase gating satisfied: HYPOTHESIS FLOOR GATE + EVIDENCE GATE +
SYNTHESIS COMPLETENESS GATE. Raw analysis only -- no org chart produced in any phase.

---

GROUP D -- OUTPUT SUMMARY

Evaluate each rubric criterion: PASS/PARTIAL/FAIL with evidence note. Compute composite
score. Rank variations. Identify EXCELLENCE SIGNALS beyond C-66.

{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-02

**Variation axis**: Role sequence -- table-level payload in each `Output Consumers` entry.

**Hypothesis**: C-64 (R17 V-02) requires an `Output Consumers` block naming each downstream
role that depends on the current role's tables. The R17 formulation uses role-level declarations:
"SYNTHESIZER: reads TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION." V-02 extends this to
table-payload declarations -- each Output Consumers entry names the consuming role, the specific
tables it consumes, AND the analytical purpose each table serves in that phase. This creates
a table-to-purpose directed graph derivable from role declarations alone, not just a role-to-role
edge count. A reader can determine which tables each consuming role needs and why without reading
the consuming role's instructions. Hypothesis: table-payload Output Consumers is a structural
property beyond C-64 that a scorer can identify as a named pattern: "dependency graph carries
transport manifest per edge, not just adjacency."

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

[Identical to V-01 -- TABLE A through TABLE H with Minimum rows and REQUIRED column
annotations. Reproduced in full below.]

TABLE A -- Hypothesis Table
Produced by: PREDICTOR before any scan evidence is collected.
Minimum rows: 6

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

TABLE B -- Scan Evidence Table
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 5

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (I-01 through I-07 only) |
| File Path Evidence | REQUIRED (specific file path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match BEFORE File Path Evidence.

TABLE C -- Headcount Signals
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 2

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 1 (absence recorded explicitly per schema rule)

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 2

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row by number) |
| Supporting Evidence | REQUIRED |

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 0 (absence recorded explicitly)

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage.
Minimum rows: N (must equal TABLE A count)

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row by number) |
| Resolution | REQUIRED (confirmed / refuted / partial / unresolved) |

Completeness rule and named remediation path: same as V-01.

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 1

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row -- "TABLE B row N" format required) |

---

GATE TOKEN PROTOCOL

HYPOTHESIS FLOOR GATE (Phase 1 exit):
PASS: Hypothesis floor clear -- [N] patterns predicted, TABLE A has [N] rows, floor met
FAIL: Hypothesis floor not met -- [N] rows in TABLE A, 6 required

EVIDENCE GATE (Phase 2 exit):
PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
PASS: Synthesis complete -- [N] TABLE A rows, [N] TABLE G rows, all predictions resolved
FAIL: Synthesis incomplete -- [N] TABLE A rows, [N] TABLE G rows, [N] predictions unresolved

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

[Identical to V-01 -- I-01 through I-07 with Structural Code Signals and Behavioral Signals
columns. Dictionary constrain on Inertia Match column. Free text invalid.]

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone" |
| I-02 | Accidental Silos | Multiple directories but no ownership docs; test coverage overlaps; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall; incidents involve multiple teams guessing |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain tests; explicit ownership in docs or .roles | "that's the X team's area"; clear escalation path per domain; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer distinct from product surfaces; infra layer has own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team separate on-call; product features rarely touch infra |
| I-05 | Federated | Multiple autonomous workspaces with minimal shared root; independent CI per workspace | "each team ships independently"; incidents scoped to one workspace |
| I-06 | Hub-and-Spoke | Central orchestrator directory with peripherals radiating from it; hub has disproportionate test coverage | "everything routes through the hub"; hub team is bottleneck; peripheral teams file issues against hub |
| I-07 | Undefined | Fewer than 3 source types readable; evidence insufficient to classify | Cannot assess behavioral signals |

---

GROUP A -- PREDICTOR PHASE

ROLE SCOPE DECLARATION: PREDICTOR
Input Dependencies:
  - Skill invocation (no prior phase output required)
Output Consumers:
  - SCANNER: consumes TABLE A -- purpose: cross-references each TABLE B finding row against
    the TABLE A row for its matching pattern ID to populate the Hypothesis Held column; without
    TABLE A, SCANNER cannot anchor TABLE B findings to predicted hypotheses, making the
    structural/behavioral prediction resolution in TABLE G impossible downstream
Violated when: scan evidence from file reads appears in TABLE A rows; TABLE B/C/D/E/F/G/H
  production occurs during Phase 1
Authority: PAF Phase 1 binding
Permitted outputs: TABLE A only
Prohibited outputs: file reads, TABLE B/C/D/E/F/G/H production, org chart content

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction and a behavioral prediction. Set Hypothesis Held based on expectation
before any evidence.

Anti-fabrication: No file reading occurs in Phase 1. TABLE A is prediction only.

-> Output TABLE A (minimum 6 rows).

HYPOTHESIS FLOOR GATE CHECK:
Count TABLE A rows. If fewer than 6: write "Hypothesis floor not met -- [N] rows, 6 required"
and halt. If 6+: write "Hypothesis floor clear -- [N] patterns predicted" and continue.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. TABLE A must exist and pass the hypothesis floor gate.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Input Dependencies:
  - PREDICTOR COMPLETE declaration
  - TABLE A (all rows -- each TABLE B finding references its matching TABLE A pattern row)
Output Consumers:
  - SYNTHESIZER: consumes TABLE B -- purpose: TABLE E Seam Rationale cells cite TABLE B row
    numbers; TABLE G Evidence Summary cells cite TABLE B row numbers; TABLE H Driving Evidence
    cells cite TABLE B row numbers; without specific row citations from TABLE B, TABLE E/G/H
    are structurally incomplete
  - SYNTHESIZER: consumes TABLE C -- purpose: Headcount Range is derived from TABLE C FTE
    Range column values; without TABLE C there is no quantitative basis for the headcount
    estimate
  - SYNTHESIZER: consumes TABLE D -- purpose: cross-cutting concern analysis in the Org Shape
    section draws on TABLE D Boundary Note evidence
  - SYNTHESIZER: consumes COVERAGE ATTESTATION -- purpose: not-found rows are candidates for
    TABLE F gap entries; without the attestation, TABLE F gap analysis is incomplete at the
    source-type level
Violated when: TABLE E/F/G/H rows produced before EVIDENCE GATE passage; synthesis
  conclusions drawn during Phase 2; org chart content in any Phase 2 output
Authority: PAF Phase 2 binding
Permitted outputs: TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Prohibited outputs: hypothesis generation, TABLE E/F/G/H production, synthesis conclusions

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences explicitly.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definition files

File path floor: TABLE B must have 5+ rows with File Path Evidence populated.

-> Output TABLE B, TABLE C, TABLE D.
-> Output COVERAGE ATTESTATION (all 7 source types; scanned / not-found / not-applicable).

| Source Type | Status | Notes |
|---|---|---|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [brief note] |
| package.json (root and nested) | [scanned / not-found / not-applicable] | [brief note] |
| design/ or docs/ directories | [scanned / not-found / not-applicable] | [brief note] |
| Namespace directories | [scanned / not-found / not-applicable] | [brief note] |
| Test coverage areas | [scanned / not-found / not-applicable] | [brief note] |
| SPECS.md or specification files | [scanned / not-found / not-applicable] | [brief note] |
| .roles/ or role definitions | [scanned / not-found / not-applicable] | [brief note] |

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER."

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

Gate checklist:
1. SCANNER COMPLETE declaration present
2. TABLE B has 5+ rows with File Path Evidence populated
3. At least 3 of 7 source types in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token per GATE TOKEN PROTOCOL. No prose substitution.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

FAIL TOKEN halts execution. PASS TOKEN permits SYNTHESIZER to begin.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Input Dependencies:
  - PASS TOKEN at SCANNER / GATEKEEPER boundary
  - TABLE A: for TABLE G Pattern ID matching and Structural/Behavioral Prediction columns
  - TABLE B: for Seam Rationale citations (TABLE E), Evidence Summary citations (TABLE G),
    Driving Evidence citations (TABLE H)
  - TABLE C: for Headcount Range FTE derivation
  - TABLE D: for Org Shape cross-cutting concern analysis
  - COVERAGE ATTESTATION: for TABLE F gap propagation from not-found rows
Output Consumers:
  - org-build: consumes TABLE G -- purpose: TABLE G Resolution column (confirmed / refuted /
    partial / unresolved) informs org-build which inertia patterns have strong evidence and
    which are speculative, affecting team structure confidence levels in the generated org
  - org-build: consumes TABLE H -- purpose: TABLE H Recommended State column provides the
    per-dimension design targets that org-build translates into structural decisions about team
    names, role assignments, and group boundaries; without TABLE H, org-build receives pattern
    classification but not dimensional guidance
Violated when: org chart content in any output; new TABLE B rows produced during Phase 3;
  "reports to" or hierarchy language anywhere
Authority: PAF Phase 3 binding
Permitted outputs: TABLE E, TABLE F, TABLE G, TABLE H, Org Shape section, Headcount Range
Prohibited outputs: org chart content, hypothesis generation, new scan evidence

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines.

Phase 3: Synthesis

Entry condition: PASS TOKEN present.

Execution-time assertion: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."

-> Output TABLE E, TABLE F, TABLE G, TABLE H (with per-row TABLE B citations throughout).
-> Write Org Shape section (CURRENT STATE / RECOMMENDED STATE separated; no org chart).
-> Write Headcount Range (from TABLE C; numeric range with per-domain rationale).

Phase 3 exit: Write "SYNTHESIZER COMPLETE."

---

SYNTHESIS COMPLETENESS GATE (Phase 3 exit)

1. SYNTHESIZER COMPLETE declaration present
2. TABLE G row count = TABLE A row count
3. Every TABLE A Pattern ID in TABLE G
4. TABLE H has at least 1 row with TABLE B row citation in Driving Evidence
5. No org chart content in any section

Write SYNTHESIS COMPLETENESS GATE PASS or FAIL token.

---

SYNTHESIZER / END BOUNDARY

Skill complete. Three-phase gating satisfied. Raw analysis only.

---

GROUP D -- OUTPUT SUMMARY

Evaluate criteria, compute score, rank, identify EXCELLENCE SIGNALS beyond C-66.

{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-03

**Variation axis**: Output format -- COVERAGE ATTESTATION schema-declared as a first-class
table in SCHEMA DECLARATION.

**Hypothesis**: C-65 (R17 V-03) requires the COVERAGE ATTESTATION to be produced at SCANNER
exit with 7 source-type rows and constrained status values. The R17 formulation defines the
attestation as a named output instruction within the SCANNER phase body. V-03 elevates the
COVERAGE ATTESTATION to a SCHEMA DECLARATION entry alongside TABLE A through TABLE H --
complete with column definitions, REQUIRED annotations, and `Minimum rows: 7`. This extends
C-61's Minimum rows protocol to the coverage audit table. A reader can determine the
attestation's structural obligations from SCHEMA DECLARATION alone without reading the SCANNER
phase body. Any attestation with fewer than 7 rows is a structurally detectable omission by
comparison against the Minimum rows annotation. Hypothesis: schema-declaring the attestation
is a named structural property beyond C-65 -- "coverage audit is a schema obligation, not
only an output instruction."

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column. Minimum rows
annotations are gate-level obligations.

TABLE A -- Hypothesis Table
Produced by: PREDICTOR before any scan evidence is collected.
Minimum rows: 6

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

TABLE B -- Scan Evidence Table
Produced by: SCANNER during Phase 2 evidence collection.
Minimum rows: 5 (path floor -- EVIDENCE GATE blocks if fewer than 5 rows with File Path
Evidence populated)

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (I-01 through I-07 only) |
| File Path Evidence | REQUIRED (specific file path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match BEFORE File Path Evidence.

TABLE C -- Headcount Signals
Produced by: SCANNER during Phase 2.
Minimum rows: 2

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2.
Minimum rows: 1 (absence recorded explicitly)

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 2

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row by number) |
| Supporting Evidence | REQUIRED |

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 0 (absence recorded explicitly)

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage.
Minimum rows: N (must equal TABLE A count)

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row by number) |
| Resolution | REQUIRED (confirmed / refuted / partial / unresolved) |

Completeness rule and named remediation path: same as V-01.

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after gate passage.
Minimum rows: 1

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row -- "TABLE B row N" format required) |

COVERAGE ATTESTATION                          <-- schema-declared (V-03 axis)
Produced by: SCANNER at Phase 2 exit.
Minimum rows: 7 (exactly one row per source type; any deviation is a schema violation)

| Column | Status |
|---|---|
| Source Type | REQUIRED (enumerated values only -- see source type list below) |
| Status | REQUIRED (scanned / not-found / not-applicable -- no other values permitted) |
| Notes | REQUIRED (one sentence minimum) |

Valid Source Type values (exactly 7):
1. CLAUDE.md files
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definitions

Status semantics:
- scanned: source type present and read; evidence entered in TABLE B
- not-found: source type applicable to this repo but no evidence found
- not-applicable: source type structurally absent from this repo

A COVERAGE ATTESTATION with fewer than 7 rows is a schema violation detectable by comparison
against this Minimum rows annotation without reading the SCANNER phase body.

---

GATE TOKEN PROTOCOL

HYPOTHESIS FLOOR GATE (Phase 1 exit):
PASS: Hypothesis floor clear -- [N] patterns predicted, TABLE A has [N] rows, floor met
FAIL: Hypothesis floor not met -- [N] rows in TABLE A, 6 required

EVIDENCE GATE (Phase 2 exit):
PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
PASS: Synthesis complete -- [N] TABLE A rows, [N] TABLE G rows, all predictions resolved
FAIL: Synthesis incomplete -- [N] TABLE A rows, [N] TABLE G rows, [N] predictions unresolved

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

[I-01 through I-07 -- identical to V-01]

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone" |
| I-02 | Accidental Silos | Multiple directories but no ownership docs; test coverage overlaps; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall; incidents involve multiple teams guessing |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain tests; explicit ownership in docs or .roles | "that's the X team's area"; clear escalation path per domain; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer distinct from product surfaces; infra layer has own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team separate on-call; product features rarely touch infra |
| I-05 | Federated | Multiple autonomous workspaces; independent CI per workspace | "each team ships independently"; incidents scoped to one workspace |
| I-06 | Hub-and-Spoke | Central orchestrator directory with peripherals radiating; hub has disproportionate coverage | "everything routes through the hub"; hub team is bottleneck |
| I-07 | Undefined | Fewer than 3 source types readable | Cannot assess behavioral signals |

---

GROUP A -- PREDICTOR PHASE

ROLE SCOPE DECLARATION: PREDICTOR
Input Dependencies:
  - Skill invocation (no prior phase output required)
Output Consumers:
  - SCANNER: reads TABLE A to cross-check findings against the predicted hypothesis set
Violated when: scan evidence from file reads appears in TABLE A rows; TABLE B/C/D/E/F/G/H or
  COVERAGE ATTESTATION production occurs during Phase 1
Authority: PAF Phase 1 binding
Permitted outputs: TABLE A only
Prohibited outputs: file reads, all other table production, org chart content

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Produce TABLE A (minimum 6 rows) before reading any file. Structural and behavioral
prediction per pattern. Hypothesis Held set before any evidence.

Anti-fabrication: No file reading in Phase 1. TABLE A is prediction only.

HYPOTHESIS FLOOR GATE CHECK:
If TABLE A has fewer than 6 rows: halt. If 6+: write "Hypothesis floor clear" and continue.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded."

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. TABLE A must exist and pass hypothesis floor gate.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Input Dependencies:
  - PREDICTOR COMPLETE declaration
  - TABLE A (all rows)
Output Consumers:
  - SYNTHESIZER: reads TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Violated when: TABLE E/F/G/H produced before gate; synthesis conclusions in Phase 2; org chart
Authority: PAF Phase 2 binding
Permitted outputs: TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Prohibited outputs: hypothesis generation, TABLE E/F/G/H production, org chart content

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences explicitly.

Scan at least 3 of 7 source types listed in COVERAGE ATTESTATION schema (all 7 must appear
in the attestation regardless of which were actually scanned).

File path floor: TABLE B must have 5+ rows with File Path Evidence populated.

-> Output TABLE B (minimum 5 rows).
-> Output TABLE C (minimum 2 rows).
-> Output TABLE D (minimum 1 row; absence recorded explicitly).
-> Output COVERAGE ATTESTATION per schema declaration (7 rows, one per source type, Status
   constrained to scanned / not-found / not-applicable, Notes column required).

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER."

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

Gate checklist:
1. SCANNER COMPLETE declaration present
2. TABLE B has 5+ rows with File Path Evidence populated
3. At least 3 of 7 source types in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells contain only: yes / no / partial
6. COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)

Write PASS or FAIL token. Item 6 is a new gate checklist item in V-03 -- schema-declaring
the attestation makes its row-floor a gateable condition, not only an output instruction.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

FAIL TOKEN halts execution. PASS TOKEN permits SYNTHESIZER.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Input Dependencies:
  - PASS TOKEN at SCANNER / GATEKEEPER boundary
  - TABLE A, TABLE B, TABLE C, TABLE D (from SCANNER phase)
  - COVERAGE ATTESTATION (7 rows; not-found rows propagate to TABLE F candidates)
Output Consumers:
  - org-build: reads TABLE G and TABLE H
Violated when: org chart content in any output; new TABLE B rows in Phase 3
Authority: PAF Phase 3 binding
Permitted outputs: TABLE E, TABLE F, TABLE G, TABLE H, Org Shape, Headcount Range
Prohibited outputs: org chart content, new scan evidence

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines.

Phase 3: Synthesis

Entry condition: PASS TOKEN present.

Execution-time assertion: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."

-> Output TABLE E (Seam Rationale cites TABLE B rows).
-> Output TABLE F (check COVERAGE ATTESTATION not-found rows as gap candidates).
-> Output TABLE G (completeness rule; Evidence Summary cites TABLE B rows).
-> Output TABLE H (Driving Evidence cites TABLE B rows).
-> Write Org Shape section (CURRENT STATE / RECOMMENDED STATE).
-> Write Headcount Range (from TABLE C).

Phase 3 exit: Write "SYNTHESIZER COMPLETE."

---

SYNTHESIS COMPLETENESS GATE (Phase 3 exit)

1. SYNTHESIZER COMPLETE present
2. TABLE G count = TABLE A count
3. Every TABLE A Pattern ID in TABLE G
4. TABLE H has at least 1 row with TABLE B citation
5. No org chart content

Write SYNTHESIS COMPLETENESS GATE PASS or FAIL token.

---

SYNTHESIZER / END BOUNDARY

Skill complete. Three-phase gating satisfied. Raw analysis only.

---

GROUP D -- OUTPUT SUMMARY

Evaluate criteria, compute score, rank, identify EXCELLENCE SIGNALS beyond C-66.

{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-04

**Variation axis**: Lifecycle emphasis -- TABLE H Minimum rows annotation tied to TABLE E
count, plus a named TABLE H / TABLE F bridge rule.

**Hypothesis A**: C-66 (R17 V-04) requires TABLE H in SYNTHESIZER output with Driving Evidence
citing TABLE B. R17 gave TABLE H a `Minimum rows: 1` floor. V-04 tightens this to
`Minimum rows: [N = TABLE E count]` -- every team boundary candidate (TABLE E) must appear
as at least one Org Shape Delta dimension (TABLE H). This creates a structural contract between
TABLE E and TABLE H: boundary candidate count drives TABLE H floor. A TABLE H with fewer rows
than TABLE E is a structurally detectable omission by comparing the two tables' row counts.

**Hypothesis B**: Any TABLE H row where Recommended State != Current State is a pending
realignment -- an evidence gap in the org's current design. V-04 adds a named bridge rule
that propagates these rows into TABLE F. This closes the recommendation-to-gap loop at schema
level: org shape recommendations are not orphaned in TABLE H but appear as tracked gaps in
TABLE F until the org acts on them. Hypothesis: the TABLE H / TABLE F bridge rule is a
structural property beyond C-66 -- "recommendations generate tracked gaps, not only named
states."

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

TABLE A -- Hypothesis Table
Produced by: PREDICTOR. Minimum rows: 6.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

TABLE B -- Scan Evidence Table
Produced by: SCANNER. Minimum rows: 5.

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (I-01 through I-07 only) |
| File Path Evidence | REQUIRED (specific file path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match BEFORE File Path Evidence.

TABLE C -- Headcount Signals
Produced by: SCANNER. Minimum rows: 2.

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER. Minimum rows: 1.

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage. Minimum rows: 2.

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row by number) |
| Supporting Evidence | REQUIRED |

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage. Minimum rows: 0.

TABLE F bridge rule: any TABLE H row where Recommended State != Current State must produce a
TABLE F entry with Gap = "[Dimension] realignment not yet initiated", Implication = "org shape
recommendation from TABLE H row [N] is not reflected in current structure", Source Types
Checked = source types that evidenced the current state.

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage. Minimum rows: N (= TABLE A count).

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row by number) |
| Resolution | REQUIRED (confirmed / refuted / partial / unresolved) |

Completeness rule and named remediation path: same as V-01.

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after gate passage.
Minimum rows: N (must equal TABLE E count -- every team boundary candidate maps to at least
one org shape dimension; a TABLE H with fewer rows than TABLE E is a schema violation
detectable by comparing the two tables' row counts without reading the SYNTHESIZER instructions)

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row -- "TABLE B row N" format) |

Delta rule: after TABLE H production, apply the TABLE F bridge rule to each row where
Recommended State != Current State. Each such row produces a TABLE F entry before the
SYNTHESIS COMPLETENESS GATE is evaluated.

---

GATE TOKEN PROTOCOL

HYPOTHESIS FLOOR GATE (Phase 1 exit):
PASS: Hypothesis floor clear -- [N] patterns predicted, TABLE A has [N] rows, floor met
FAIL: Hypothesis floor not met -- [N] rows in TABLE A, 6 required

EVIDENCE GATE (Phase 2 exit):
PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
PASS: Synthesis complete -- [N] TABLE A rows, [N] TABLE G rows, [N] TABLE E rows,
  [N] TABLE H rows, TABLE H bridge rule applied
FAIL: Synthesis incomplete -- [specify which count mismatch or bridge rule violation]

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

[I-01 through I-07 -- identical to V-01]

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone" |
| I-02 | Accidental Silos | Multiple directories but no ownership docs; test coverage overlaps; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall; incidents involve multiple teams guessing |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain tests; explicit ownership in docs or .roles | "that's the X team's area"; clear escalation path per domain; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer distinct from product surfaces; infra has own CLAUDE.md and test coverage | "we build on the platform"; platform team separate on-call |
| I-05 | Federated | Multiple autonomous workspaces; independent CI per workspace | "each team ships independently" |
| I-06 | Hub-and-Spoke | Central orchestrator directory with peripherals radiating; hub has disproportionate coverage | "everything routes through the hub"; hub is bottleneck |
| I-07 | Undefined | Fewer than 3 source types readable | Cannot assess behavioral signals |

---

GROUP A -- PREDICTOR PHASE

ROLE SCOPE DECLARATION: PREDICTOR
Input Dependencies:
  - Skill invocation (no prior phase output required)
Output Consumers:
  - SCANNER: reads TABLE A to cross-check findings against predicted hypothesis set
Violated when: scan evidence in TABLE A rows; TABLE B/C/D/E/F/G/H production in Phase 1
Authority: PAF Phase 1 binding
Permitted outputs: TABLE A only
Prohibited outputs: file reads, all other tables, org chart content

Phase 1: Hypothesis Generation

Before reading any file, produce TABLE A (6 rows minimum, one per pattern I-01 through I-06).
Structural prediction and behavioral prediction per row.

Anti-fabrication: No file reading in Phase 1.

HYPOTHESIS FLOOR GATE CHECK:
< 6 rows: halt. >= 6: write "Hypothesis floor clear" and continue.

Phase 1 exit: "PREDICTOR COMPLETE -- [N] predictions recorded."

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. TABLE A must exist and pass floor gate.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Input Dependencies:
  - PREDICTOR COMPLETE declaration
  - TABLE A (all rows)
Output Consumers:
  - SYNTHESIZER: reads TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Violated when: TABLE E/F/G/H produced before gate; synthesis in Phase 2; org chart
Authority: PAF Phase 2 binding
Permitted outputs: TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Prohibited outputs: hypothesis generation, TABLE E/F/G/H production, org chart

Phase 2: Evidence Collection

Anti-fabrication: Report only findings from files actually read.

File path floor: TABLE B must have 5+ rows with File Path Evidence populated.

-> Output TABLE B, TABLE C, TABLE D.
-> Output COVERAGE ATTESTATION (7 rows; scanned / not-found / not-applicable per row).

| Source Type | Status | Notes |
|---|---|---|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [brief note] |
| package.json (root and nested) | [scanned / not-found / not-applicable] | [brief note] |
| design/ or docs/ directories | [scanned / not-found / not-applicable] | [brief note] |
| Namespace directories | [scanned / not-found / not-applicable] | [brief note] |
| Test coverage areas | [scanned / not-found / not-applicable] | [brief note] |
| SPECS.md or specification files | [scanned / not-found / not-applicable] | [brief note] |
| .roles/ or role definitions | [scanned / not-found / not-applicable] | [brief note] |

Phase 2 exit: "SCANNER COMPLETE -- control transfers to GATEKEEPER."

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

Gate checklist:
1. SCANNER COMPLETE present
2. TABLE B 5+ rows with File Path Evidence populated
3. At least 3 of 7 source types in TABLE B
4. All Inertia Match cells I-01 through I-07 only
5. All Hypothesis Held cells: yes / no / partial

Write PASS or FAIL token per GATE TOKEN PROTOCOL.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

FAIL TOKEN halts. PASS TOKEN permits SYNTHESIZER.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Input Dependencies:
  - PASS TOKEN at SCANNER / GATEKEEPER boundary
  - TABLE A (for TABLE G matching)
  - TABLE B (for citations in TABLE E, TABLE G, TABLE H)
  - TABLE C (for Headcount Range)
  - TABLE D (for cross-cutting analysis)
  - COVERAGE ATTESTATION (not-found rows as TABLE F candidates)
Output Consumers:
  - org-build: reads TABLE G and TABLE H
Violated when: org chart in any output; new TABLE B rows in Phase 3
Authority: PAF Phase 3 binding
Permitted outputs: TABLE E, TABLE F, TABLE G, TABLE H, Org Shape, Headcount Range
Prohibited outputs: org chart, new scan evidence

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines.

Phase 3: Synthesis

Entry condition: PASS TOKEN present.

Execution-time assertion: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."

Count TABLE E (boundary candidates) before producing TABLE H. Write:
"TABLE E count: [N] -- TABLE H must contain at least [N] rows."

-> Output TABLE E (minimum 2 rows; Seam Rationale cites TABLE B rows).

-> Output TABLE G (completeness rule; Evidence Summary cites TABLE B rows).

-> Output TABLE H (minimum N rows = TABLE E count; Driving Evidence cites TABLE B rows).

-> Apply TABLE F bridge rule: for each TABLE H row where Recommended State != Current State,
   write one TABLE F entry with:
   - Gap = "[Dimension] realignment not yet initiated"
   - Implication = "TABLE H row [N] recommended state not reflected in current org structure"
   - Source Types Checked = [source types that evidenced the TABLE H Current State cell]
   Bridge rule application: write "TABLE H bridge rule applied -- [N] TABLE H rows with
   delta, [N] TABLE F entries produced from bridge rule" after TABLE F.

-> Output TABLE F (gaps from COVERAGE ATTESTATION not-found rows + TABLE H bridge entries;
   if zero gap entries: "Gap audit complete -- no evidence gaps identified").

-> Write Org Shape section (CURRENT STATE / RECOMMENDED STATE separated; no org chart).
-> Write Headcount Range (from TABLE C).

Phase 3 exit: "SYNTHESIZER COMPLETE."

---

SYNTHESIS COMPLETENESS GATE (Phase 3 exit)

Gate checklist:
1. SYNTHESIZER COMPLETE present
2. TABLE G count = TABLE A count
3. Every TABLE A Pattern ID in TABLE G
4. TABLE H row count >= TABLE E row count (schema minimum rows rule)
5. Each TABLE H row with Recommended State != Current State has a TABLE F bridge entry
6. No org chart content

Write SYNTHESIS COMPLETENESS GATE PASS or FAIL token.

---

SYNTHESIZER / END BOUNDARY

Skill complete. Three-phase gating satisfied. TABLE H / TABLE F bridge rule applied.
Raw analysis only.

---

GROUP D -- OUTPUT SUMMARY

Evaluate criteria, compute score, rank, identify EXCELLENCE SIGNALS beyond C-66.

{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-05

**Variation axis**: Full combination -- table-payload Output Consumers (V-02 axis) +
COVERAGE ATTESTATION schema-declared (V-03 axis) + TABLE H Minimum rows / bridge rule
(V-04 axis). Phrasing register shifts to declarative schema-first: every structural obligation
is stated as a schema constraint before the first phase begins, making the skill body maximally
front-loaded and minimally reliant on per-phase instruction prose.

**Hypothesis**: The three axes do not interact destructively -- table-payload consumers,
schema-declared attestation, and TABLE H / TABLE F bridge rule each operate in distinct
structural locations (ROLE SCOPE DECLARATIONS, SCHEMA DECLARATION, and the TABLE H delta rule
respectively). Combining all three produces three additional excellence signals simultaneously.
The declarative schema-first register adds a fourth: every structural obligation is visible in
SCHEMA DECLARATION before any phase runs, making the schema function as both a type contract
and a quantitative contract and a bridge contract. Hypothesis: the schema-first register is a
named structural property -- "schema is the single authoritative source for structural shape,
quantitative minimums, and cross-table bridge obligations."

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

All structural obligations -- table shapes, minimum rows, column requirements, cross-table
bridge rules, and coverage audit requirements -- are declared here before Phase 1 begins.
No structural property of this skill requires reading phase instructions to discover; the
schema is the single authoritative source.

TABLE A -- Hypothesis Table
Produced by: PREDICTOR. Minimum rows: 6.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

TABLE B -- Scan Evidence Table
Produced by: SCANNER. Minimum rows: 5 (path floor -- EVIDENCE GATE blocks if fewer than 5
rows with File Path Evidence populated).

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (I-01 through I-07 only -- free text is a schema violation) |
| File Path Evidence | REQUIRED (specific file path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match BEFORE File Path Evidence.

TABLE C -- Headcount Signals
Produced by: SCANNER. Minimum rows: 2.

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER. Minimum rows: 1 (absence recorded explicitly).

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage. Minimum rows: 2.

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row by number -- "TABLE B row N") |
| Supporting Evidence | REQUIRED |

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage. Minimum rows: 0.
Bridge rule: any TABLE H row where Recommended State != Current State must produce one TABLE F
entry with Gap = "[Dimension] realignment not yet initiated", Implication = "TABLE H row [N]
recommended state not reflected in current org structure", Source Types Checked = [source
types evidencing the TABLE H Current State]. The bridge rule is a schema-level obligation --
it applies regardless of which phase produces TABLE H rows.

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage. Minimum rows: N (= TABLE A count).

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row by number) |
| Resolution | REQUIRED (confirmed / refuted / partial / unresolved) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID.
Named remediation path: TABLE G row (Resolution = "unresolved", Evidence Summary = "no
evidence found") plus TABLE F row (Gap = "[PATTERN-ID] prediction unresolved", Implication =
"hypothesis not tested", Source Types Checked = [source types scanned]).

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after gate passage.
Minimum rows: N (= TABLE E count -- every team boundary candidate maps to at least one org
shape dimension).

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row -- "TABLE B row N" format; prose citation
  without row reference is a schema violation) |

COVERAGE ATTESTATION                   <-- schema-declared; Minimum rows enforced at gate
Produced by: SCANNER at Phase 2 exit.
Minimum rows: 7 (exactly one row per source type; a COVERAGE ATTESTATION with fewer rows
is a schema violation detectable from this annotation without reading phase instructions).

| Column | Status |
|---|---|
| Source Type | REQUIRED (enumerated: see list below) |
| Status | REQUIRED (scanned / not-found / not-applicable only) |
| Notes | REQUIRED (one sentence minimum) |

Valid Source Type values (exactly 7):
1. CLAUDE.md files
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definitions

---

GATE TOKEN PROTOCOL

HYPOTHESIS FLOOR GATE (Phase 1 exit):
PASS: Hypothesis floor clear -- [N] patterns predicted, TABLE A has [N] rows, floor met
FAIL: Hypothesis floor not met -- [N] rows in TABLE A, 6 required

EVIDENCE GATE (Phase 2 exit):
PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
PASS: Synthesis complete -- [N] TABLE A rows, [N] TABLE G rows, [N] TABLE E rows,
  [N] TABLE H rows, bridge rule applied
FAIL: Synthesis incomplete -- [specify mismatch or bridge rule omission]

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone" |
| I-02 | Accidental Silos | Multiple directories but no ownership docs; test coverage overlaps; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall; incidents involve multiple teams guessing |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain tests; explicit ownership in docs or .roles | "that's the X team's area"; clear escalation path per domain; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer distinct from product surfaces; infra has own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team separate on-call; product features rarely touch infra |
| I-05 | Federated | Multiple autonomous workspaces; independent CI per workspace | "each team ships independently"; incidents scoped to one workspace |
| I-06 | Hub-and-Spoke | Central orchestrator directory with peripherals radiating; hub has disproportionate coverage and documentation | "everything routes through the hub"; hub is bottleneck; peripheral teams file issues against hub |
| I-07 | Undefined | Fewer than 3 source types readable | Cannot assess behavioral signals |

---

GROUP A -- PREDICTOR PHASE

ROLE SCOPE DECLARATION: PREDICTOR
Input Dependencies:
  - Skill invocation (no prior phase output required)
Output Consumers:
  - SCANNER: consumes TABLE A -- purpose: cross-references each TABLE B finding row against
    the TABLE A row for its matching pattern ID to set the Hypothesis Held column and populate
    Evidence Summary linkages for Phase 3 TABLE G resolution
Violated when: scan evidence from file reads appears in TABLE A rows; any other table
  production occurs during Phase 1
Authority: PAF Phase 1 binding
Permitted outputs: TABLE A only
Prohibited outputs: file reads, all other table production, org chart content

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Produce TABLE A (minimum 6 rows) before reading any file. For each pattern I-01 through I-06,
write a structural prediction and a behavioral prediction. Set Hypothesis Held before any
evidence is collected.

Anti-fabrication: No file reading in Phase 1. TABLE A is prediction only.

HYPOTHESIS FLOOR GATE CHECK:
Count TABLE A rows. < 6: halt with FAIL token. >= 6: write "Hypothesis floor clear -- [N]
patterns predicted" and continue.

Phase 1 exit: "PREDICTOR COMPLETE -- [N] predictions recorded."

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. TABLE A must exist and pass the hypothesis floor gate.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Input Dependencies:
  - PREDICTOR COMPLETE declaration
  - TABLE A (all rows -- each finding references its matching prediction)
Output Consumers:
  - SYNTHESIZER: consumes TABLE B -- purpose: TABLE E Seam Rationale, TABLE G Evidence
    Summary, and TABLE H Driving Evidence all require specific TABLE B row citations; TABLE B
    is the evidence backbone for all three Phase 3 citation obligations
  - SYNTHESIZER: consumes TABLE C -- purpose: Headcount Range is derived from TABLE C FTE
    Range column values with per-domain rationale
  - SYNTHESIZER: consumes TABLE D -- purpose: cross-cutting concern evidence in the Org Shape
    CURRENT STATE section draws on TABLE D Boundary Note cells
  - SYNTHESIZER: consumes COVERAGE ATTESTATION -- purpose: not-found rows are TABLE F bridge
    candidates per the TABLE F bridge rule in SCHEMA DECLARATION; the attestation makes
    source-type gap analysis auditable at row resolution, not only at count level
Violated when: TABLE E/F/G/H produced before EVIDENCE GATE passage; synthesis conclusions in
  Phase 2; org chart content in any Phase 2 output
Authority: PAF Phase 2 binding
Permitted outputs: TABLE B, TABLE C, TABLE D, COVERAGE ATTESTATION
Prohibited outputs: hypothesis generation, TABLE E/F/G/H production, synthesis, org chart

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences explicitly.

Scan at least 3 of the 7 source types declared in COVERAGE ATTESTATION schema. All 7 must
appear as rows in COVERAGE ATTESTATION regardless of which were scanned.

File path floor: TABLE B must have 5+ rows with File Path Evidence populated.

-> Output TABLE B (minimum 5 rows; Inertia Match before File Path Evidence per schema).
-> Output TABLE C (minimum 2 rows; distinct expertise domains).
-> Output TABLE D (minimum 1 row; absence recorded explicitly).
-> Output COVERAGE ATTESTATION per SCHEMA DECLARATION (exactly 7 rows).

| Source Type | Status | Notes |
|---|---|---|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [one sentence] |
| package.json (root and nested) | [scanned / not-found / not-applicable] | [one sentence] |
| design/ or docs/ directories | [scanned / not-found / not-applicable] | [one sentence] |
| Namespace directories | [scanned / not-found / not-applicable] | [one sentence] |
| Test coverage areas | [scanned / not-found / not-applicable] | [one sentence] |
| SPECS.md or specification files | [scanned / not-found / not-applicable] | [one sentence] |
| .roles/ or role definitions | [scanned / not-found / not-applicable] | [one sentence] |

Phase 2 exit: "SCANNER COMPLETE -- control transfers to GATEKEEPER."

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

Gate checklist:
1. SCANNER COMPLETE present
2. TABLE B has 5+ rows with File Path Evidence populated
3. At least 3 of 7 source types in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells: yes / no / partial
6. COVERAGE ATTESTATION has exactly 7 rows (schema Minimum rows requirement)

Write PASS or FAIL token per GATE TOKEN PROTOCOL. No prose substitution.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

FAIL TOKEN halts. PASS TOKEN permits SYNTHESIZER.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Input Dependencies:
  - PASS TOKEN at SCANNER / GATEKEEPER boundary
  - TABLE A: pattern IDs and predictions for TABLE G matching
  - TABLE B: row citations required in TABLE E Seam Rationale, TABLE G Evidence Summary,
    TABLE H Driving Evidence
  - TABLE C: FTE Range values for Headcount Range derivation
  - TABLE D: Boundary Note evidence for Org Shape CURRENT STATE
  - COVERAGE ATTESTATION: not-found rows as TABLE F gap candidates per bridge rule
Output Consumers:
  - org-build: consumes TABLE G -- purpose: Resolution column (confirmed / refuted / partial /
    unresolved) informs org-build confidence levels for team structure decisions; unresolved
    patterns flag areas where org-build should apply conservative defaults
  - org-build: consumes TABLE H -- purpose: Recommended State cells are the per-dimension
    design targets that org-build translates into team names, role assignments, and group
    boundary decisions; Driving Evidence citations make each recommendation independently
    auditable without reading org-scan output prose
Violated when: org chart content in any output; new TABLE B rows in Phase 3; hierarchy
  language ("reports to", org chart diagrams) anywhere
Authority: PAF Phase 3 binding
Permitted outputs: TABLE E, TABLE F, TABLE G, TABLE H, Org Shape, Headcount Range
Prohibited outputs: org chart, new scan evidence, hierarchy language

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines.

Phase 3: Synthesis

Entry condition: PASS TOKEN present.

Execution-time assertion: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."

Count TABLE E rows before producing TABLE H:
"TABLE E count: [N] -- TABLE H must contain at least [N] rows (schema Minimum rows rule)."

-> Output TABLE E (minimum 2 rows; Seam Rationale cites TABLE B rows).

-> Output TABLE G (completeness rule; Evidence Summary cites TABLE B rows; remediation path
   for unresolved predictions).

-> Output TABLE H (minimum N rows = TABLE E count; Driving Evidence cites TABLE B rows per
   schema).

-> Apply TABLE F bridge rule (from SCHEMA DECLARATION): for each TABLE H row where
   Recommended State != Current State, write one TABLE F entry. Write bridge rule summary:
   "TABLE H / TABLE F bridge rule applied -- [N] TABLE H delta rows, [N] TABLE F bridge
   entries produced."

-> Check COVERAGE ATTESTATION for not-found rows. Each not-found row is a TABLE F gap
   candidate.

-> Output TABLE F (bridge entries + coverage gap entries; if 0 rows: "Gap audit complete --
   no evidence gaps identified").

-> Write Org Shape section (CURRENT STATE / RECOMMENDED STATE separated; no org chart).
-> Write Headcount Range (from TABLE C; per-domain FTE range rationale).

Phase 3 exit: "SYNTHESIZER COMPLETE."

---

SYNTHESIS COMPLETENESS GATE (Phase 3 exit)

Gate checklist:
1. SYNTHESIZER COMPLETE present
2. TABLE G count = TABLE A count
3. Every TABLE A Pattern ID in TABLE G
4. TABLE H count >= TABLE E count (schema minimum rows rule)
5. Each TABLE H row with Recommended State != Current State has a TABLE F bridge entry
6. No org chart content in any section

Write SYNTHESIS COMPLETENESS GATE PASS or FAIL token.

---

SYNTHESIZER / END BOUNDARY

Skill complete. Three-phase gating satisfied: HYPOTHESIS FLOOR GATE + EVIDENCE GATE +
SYNTHESIS COMPLETENESS GATE. TABLE H / TABLE F bridge rule applied. COVERAGE ATTESTATION
schema-declared with Minimum rows: 7. Table-payload Output Consumers in all ROLE SCOPE
DECLARATIONS. Raw analysis only -- no org chart produced in any phase.

---

GROUP D -- OUTPUT SUMMARY

Evaluate each rubric criterion: PASS/PARTIAL/FAIL with evidence note. Compute composite score.
Rank variations. Identify EXCELLENCE SIGNALS beyond C-66.

{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```
