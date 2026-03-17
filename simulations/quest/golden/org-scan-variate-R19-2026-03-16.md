---
skill: quest-variate
skill_target: org-scan
round: 19
date: 2026-03-16
rubric_version: 19
---

# Variate R19 — org-scan

5 complete prompt body variations for the `org-scan` skill, targeting the v19 rubric (C-01
through C-69). All prior invariants through C-66 are treated as structural requirements that
every variation must satisfy. C-67, C-68, and C-69 are the three new criteria this round.

New criteria this round:

- **C-67** — Transport manifest Output Consumers: each Output Consumers entry carries the
  consuming role, the specific tables consumed, AND the analytical purpose each table serves in
  that consuming phase. Form: `[consuming role] — [table(s)] — [analytical purpose in consuming
  phase]`. Extends C-64's Output Consumers block with a per-edge purpose annotation. Any entry
  lacking a purpose annotation is a structurally detectable omission.

- **C-68** — COVERAGE ATTESTATION schema-declared with gate-blocking enforcement: COVERAGE
  ATTESTATION is a first-class SCHEMA DECLARATION entry with full column definitions and a
  `Minimum rows: 7` annotation. Its row floor is enforced as a named gate checklist item (e.g.,
  "COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)"), making attestation
  completeness detectable from SCHEMA DECLARATION alone. SCANNER phase instructions reference
  "source types declared in COVERAGE ATTESTATION schema" rather than restating the enumeration
  inline. Gate-blocking, not soft obligation.

- **C-69** — TABLE H dynamic floor assertion + BRIDGE RULE: before TABLE H is produced the
  SYNTHESIZER records a named assertion line (`Org Shape Dimension count: N — TABLE H must contain
  exactly N rows`). A named `BRIDGE RULE` constraint is declared (e.g., "Every TABLE H row must
  carry at least one `(cite TABLE B row)` annotation in its Driving Evidence cell") enforcing
  evidence linkage as a named structural rule. Any TABLE H row lacking a TABLE B citation is a
  structurally detectable BRIDGE RULE violation.

Variation axes explored this round:

1. **Role sequence** (V-01) — SCANNER and SYNTHESIZER run as the two primary named groups
   (GROUP A / GROUP B) with SCHEMA DECLARATIONS leading; roles within groups run in strict
   sequence. Tests whether table-first schema placement maximises C-61/C-68 detectability.

2. **Output format** (V-02) — Phase footers carry PHASE OUTPUTS blocks declaring exactly what
   was produced; COVERAGE ATTESTATION and TABLE H counts are included in the footer. Tests
   whether footer declarations make C-68 and C-69 counts independently verifiable.

3. **Lifecycle emphasis** (V-03) — Maximum preamble density: all SCHEMA DECLARATIONS, GATE
   TOKEN PROTOCOL, INERTIA PATTERN DICTIONARY, and BRIDGE RULE appear before GROUP A begins.
   Tests whether full preamble concentration improves structural completeness at phase boundaries.

4. **Phrasing register** (V-04) — Imperative/prescriptive register throughout: every instruction
   is a direct command rather than a description. Tests whether imperative phrasing produces more
   reliable gate-blocking enforcement on C-67/C-68/C-69.

5. **Combination** (V-05) — Phase footers (V-02 axis) combined with maximum preamble density
   (V-03 axis). Tests whether preamble + footer together yield the highest structural coverage
   for all three new criteria simultaneously.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence — SCANNER/SYNTHESIZER as named group pair with schema-first placement | V-01 |
| Output format — phase footer PHASE OUTPUTS blocks with count declarations | V-02 |
| Lifecycle emphasis — maximum preamble density (all declarations before GROUP A) | V-03 |
| Phrasing register — imperative/prescriptive throughout | V-04 |
| Combination — phase footer declarations + maximum preamble density | V-05 |

---

## V-01 — Role Sequence: SCANNER / SYNTHESIZER Named Groups with Schema-First Placement

**Axis**: Role sequence
**Hypothesis**: Prior rounds use GATE PHASE / ROLE 1 → SCAN PHASE / ROLE 2 → DELIBERATE PHASE /
ROLE 3 → DRAFT+FINALIZE PHASE / ROLE 4 with varying numbers of roles and phase counts. The
SCANNER / SYNTHESIZER framing (GROUP A / GROUP B) maps the skill directly onto the two named
groups in the rubric's structural group label criterion (C-15), making the group boundary
explicit. Placing all SCHEMA DECLARATIONS at the top — before GROUP A begins — tests whether
the schema-first pattern maximises C-61/C-68 structural detectability, because COVERAGE
ATTESTATION's Minimum rows: 7 and TABLE H's BRIDGE RULE are both readable before any phase
executes. Hypothesis: full C-67/C-68/C-69 coverage plus high prior-criteria coverage.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md, package.json,
design/ directories, namespaces, test coverage areas, SPECS.md files, existing .craft/roles/.
Produce a structured analysis: areas of work, team boundaries, cross-cutting concerns, headcount
signals, and recommended org shape. Output is raw analysis only — not an org chart, not reporting
lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — stated here and again in output format section below)**: This skill
produces RAW ANALYSIS ONLY. No org chart. No reporting lines. No hierarchy diagram. No role
file creation. Violation of this constraint is a critical failure regardless of other scores.

---

### PREAMBLE DECLARATIONS

`(C-20: GATE TOKEN PROTOCOL; C-23: INERTIA PATTERN DICTIONARY; C-61/C-68: SCHEMA DECLARATIONS
with Minimum rows annotations; C-69: BRIDGE RULE; all declared before GROUP A begins)`

---

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan
(C-20: pass and fail tokens defined as named constants before GROUP A begins)
(C-22: gate is postcondition of GROUP A / SCANNER and precondition of GROUP B / SYNTHESIZER)

SCAN GATE:
  PASS TOKEN:  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET/NOT MET], dominant
                pattern:[INR-NN label]"
  FAIL TOKEN:  "SCAN GATE FAIL — [reason: source count below 3 / path floor not met /
                COVERAGE ATTESTATION row count below 7]"

  Postcondition of GROUP A: SCANNER writes one of the above tokens as its final output line.
  Precondition of GROUP B: SYNTHESIZER reads the token. If FAIL TOKEN, halt — output the
    FAIL TOKEN verbatim and stop. If PASS TOKEN, proceed.

  Gate-blocking items (any one unmet causes FAIL TOKEN):
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ specific file paths cited in TABLE B (C-09 / C-16)
  [ ] COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement) (C-68)
```

---

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan
(C-23: enumerated valid values with labels; used as constrained vocabulary in TABLE B
 Inertia Match column; C-25: Inertia Match column positioned before File Path Evidence)

INR-01  Org-by-function     Teams aligned to function (eng, design, QA) regardless of product
INR-02  Org-by-product      Teams aligned to product area or feature surface
INR-03  Org-by-layer        Teams aligned to technical layer (frontend, backend, infra)
INR-04  Org-by-domain       Teams aligned to business domain / bounded context
INR-05  Org-by-geography    Teams aligned to region or timezone
INR-06  Org-by-customer     Teams aligned to customer segment or vertical

Rules:
- Inertia Match column in TABLE B must use only INR-01 through INR-06 labels.
- Free-text in Inertia Match is a structurally detectable violation.
- Column order: Inertia Match (C-25) BEFORE File Path Evidence in TABLE B.
```

---

#### SCHEMA DECLARATIONS

`(C-21: evidence columns declared required; C-61: Minimum rows annotations; C-68: COVERAGE
ATTESTATION is a first-class schema entry with Minimum rows: 7 and gate-blocking enforcement)`

```
SCHEMA DECLARATION: TABLE B — Scan Evidence Table
  Columns (all required):
    Area                  (C-01: traceable to scan evidence)
    Source Type           (C-02: one of 7 enumerated source types)
    Inertia Match         (C-19/C-25: required; constrained to INR-01..INR-06; BEFORE File Path)
    File Path Evidence    (C-09/C-16/C-21: required; specific path, not generic phrase)
    Anti-Fabrication Note (C-11: required; one sentence of hedging language per row)
  Minimum rows: 5  (C-16: file path floor gate condition — blocks SCAN GATE passage if unmet)

SCHEMA DECLARATION: TABLE C — Cross-Cutting Concerns
  Columns (all required):
    Concern Name    (C-04: named concern)
    Boundary Note   (C-04: which teams share this concern and where it crosses)
    Evidence Path   (C-09: file path supporting this concern's detection)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE D — Team Boundary Candidates
  Columns (all required):
    Boundary Candidate  (C-06: candidate team name)
    Seam Rationale      (C-06: why this is a natural boundary)
    Evidence Citation   (C-09: supporting file path)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE E — Headcount Signals
  Columns (all required):
    Signal Source      (C-03: what evidence supports this signal)
    Headcount Range    (C-03: low-N to high-N, not a point estimate)
    Rationale          (C-03: one sentence supporting the range)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE F — Transport Manifest (Output Consumers)
  (C-64/C-67: per-edge purpose annotation; form: [consuming role] — [table(s)] — [analytical
   purpose in consuming phase]; any entry lacking purpose annotation is a structurally
   detectable omission)
  Columns (all required):
    Producing Role    (this role / group)
    Consuming Role    (downstream role that reads output)
    Tables Consumed   (specific table names, e.g., TABLE B, TABLE H)
    Analytical Purpose (C-67: what the consuming role does with these tables in its phase)
  Minimum rows: 2  (at least SCANNER → SYNTHESIZER and SYNTHESIZER → org-build consumer edges)

SCHEMA DECLARATION: COVERAGE ATTESTATION
  (C-65/C-68: first-class schema entry; C-61/C-68: Minimum rows: 7 is gate-blocking;
   status values constrained to: scanned / not-found / not-applicable;
   SCANNER phase instructions reference "source types declared in COVERAGE ATTESTATION schema"
   — enumeration is not restated inline in SCANNER instructions)
  Columns (all required):
    Source Type   (one of the 7 org-scan source types)
    Status        (constrained: scanned / not-found / not-applicable)
    Notes         (structural reason if not-applicable; evidence gap note if not-found)
  Source types (declared here; SCANNER references this declaration rather than restating):
    1. CLAUDE.md files
    2. package.json / workspace configs
    3. design/ directories
    4. namespace / module directories
    5. test coverage areas
    6. SPECS.md files
    7. existing .craft/roles/ files
  Minimum rows: 7  (C-68: gate-blocking — SCAN GATE fails if COVERAGE ATTESTATION has <7 rows)

SCHEMA DECLARATION: TABLE G — Evidence Gaps and Ambiguities
  Columns (all required):
    Gap / Ambiguity     (C-08: named finding)
    Impact              (C-08: what analysis is limited by this gap)
    Recommended Follow-Up (C-08: one action to resolve)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE H — Org Shape Delta
  (C-66/C-69: four required columns; BRIDGE RULE declared here as named constraint)
  Columns (all required):
    Dimension         (org shape dimension being analysed)
    Current State     (C-10: what the repo evidence shows today)
    Recommended State (C-10: what the analysis recommends)
    Driving Evidence  (C-66/C-69: must contain at least one "(cite TABLE B row)" annotation)
  Minimum rows: N  (set by SYNTHESIZER assertion before TABLE H production — see C-69)

  BRIDGE RULE (C-69 named constraint):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any TABLE H row lacking a TABLE B citation is a BRIDGE RULE
     violation detectable by table correspondence alone."
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan must complete before synthesis begins; C-22: GROUP A
completion is the postcondition that enables GROUP A SCAN GATE PASS TOKEN; C-11: anti-fabrication
language per evidence-dependent section)`

**HARD BOUNDARY (C-05 / C-13)**: This skill produces RAW ANALYSIS ONLY. No org chart, no
reporting lines, no hierarchy, no .craft/roles/ file creation. This constraint applies to every
section in GROUP A and GROUP B.

**Anti-fabrication rule (C-11)**: Each evidence-dependent table row must include an
Anti-Fabrication Note. Valid forms: "No evidence found for this row — placeholder pending scan.",
"Inferred from [path] — verify before org-build.", "Signal detected in [path] — strength: low."

Walk the repo. Scan the source types declared in COVERAGE ATTESTATION schema (see SCHEMA
DECLARATIONS above — enumeration not restated here, per C-68 schema-first reference pattern).
For each source type, record its status in COVERAGE ATTESTATION. Do not invent findings.

#### TABLE B — Scan Evidence Table

`(C-19/C-25: Inertia Match before File Path Evidence; C-21: all columns required; C-09: specific
paths; C-11: Anti-Fabrication Note required per row)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area from scan — C-01: traceable to evidence, not invented] | [source type from COVERAGE ATTESTATION schema] | [INR-01..INR-06] | [specific/path/to/file.ext] | [hedging sentence] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

*Minimum 5 rows required. If fewer than 5 distinct areas are detected, add PLACEHOLDER rows
with Anti-Fabrication Note: "No evidence — placeholder." Path floor gate fails if <5 rows.*

Dominant inertia pattern: [INR-NN label] — [one sentence justifying dominance]

#### TABLE C — Cross-Cutting Concerns

`(C-04: named concern with boundary note; C-09: evidence path)`

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [which teams share this and where it crosses] | [specific/path] |

#### TABLE D — Team Boundary Candidates

`(C-06: seam rationale; C-09: evidence path)`

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [team name — C-06] | [why this is a natural seam] | [specific/path] |

#### TABLE E — Headcount Signals

`(C-03: range with rationale)`

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [evidence — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

`(C-65/C-68: all 7 source types declared in SCHEMA DECLARATION; status constrained to
scanned / not-found / not-applicable; Minimum rows: 7 is gate-blocking)`

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [notes] |
| package.json / workspace configs | [scanned / not-found / not-applicable] | [notes] |
| design/ directories | [scanned / not-found / not-applicable] | [notes] |
| namespace / module directories | [scanned / not-found / not-applicable] | [notes] |
| test coverage areas | [scanned / not-found / not-applicable] | [notes] |
| SPECS.md files | [scanned / not-found / not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned / not-found / not-applicable] | [notes] |

*Row count must equal 7. SCAN GATE fails if row count < 7 (C-68 gate-blocking enforcement).*

#### TABLE G — Evidence Gaps and Ambiguities

`(C-08: named gaps with impact and recommended follow-up)`

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [named gap — C-08] | [what analysis is limited] | [one action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(C-64/C-67: per-edge purpose annotation; form: consuming role — table(s) — analytical purpose)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer uses TABLE B rows as citation targets for TABLE H Driving Evidence cells (BRIDGE RULE); uses TABLE C for cross-cutting concern synthesis; uses TABLE D for boundary recommendation; uses TABLE E for headcount synthesis; uses TABLE G as gaps to acknowledge in org shape recommendation |
| GROUP B / SYNTHESIZER | org-build | TABLE H, TABLE F | org-build uses TABLE H Org Shape Delta to configure the target org structure; TABLE F declares which org-scan outputs org-build reads and for what purpose at each construction phase |

---

**SCAN GATE CHECK** `(C-12/C-16/C-17/C-18/C-22/C-68: gate expressed as GROUP A postcondition
and GROUP B precondition; PASS and FAIL tokens defined in GATE TOKEN PROTOCOL preamble)`

```
SCAN GATE VERIFICATION CHECKLIST
(C-14: numbered items + required confirmation sentence)

[1] Source types scanned: [N] of 7 — must be 3+ to pass (C-02)
[2] File paths in TABLE B: [N] specific paths — must be 5+ to pass (C-09/C-16)
[3] COVERAGE ATTESTATION rows: [N] — must equal exactly 7 (C-68 gate-blocking)
[4] All TABLE B rows have Inertia Match in INR-01..INR-06 range (C-23)
[5] Inertia Match column appears before File Path Evidence in TABLE B (C-25)
[6] All evidence-dependent rows carry Anti-Fabrication Note (C-11)
[7] No org chart, no reporting lines, no .craft/roles/ content (C-05)

If ALL items pass:
  Write: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant pattern:[INR-NN]"

If ANY item fails:
  Write: "SCAN GATE FAIL — [item number]: [reason]"
  STOP. GROUP B / SYNTHESIZER may not begin.
```

*Confirmation sentence (required — C-14): "GROUP A complete. GROUP B / SYNTHESIZER may begin
only if the SCAN GATE PASS TOKEN above is present."*

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: SYNTHESIZER begins only on SCAN GATE PASS TOKEN;
C-10: current state vs recommended state clearly separated in TABLE H; C-07: org shape named
and justified from findings)`

**Precondition check**: Read the final line of GROUP A output. If it is the FAIL TOKEN, halt
immediately — write the FAIL TOKEN verbatim and produce no further output.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: GROUP B produces RAW ANALYSIS ONLY.
No org chart. No reporting lines. No hierarchy. No role files. Org shape analysis is descriptive
— the recommended shape is a named recommendation, not a drawn structure.

#### Org Shape Assessment

`(C-07: org shape named and justified; C-03: headcount referenced from TABLE E)`

Based on the dominant inertia pattern [INR-NN] identified in GROUP A, the org shape this repo
most closely exhibits is: [named shape — e.g., functional silo / product-aligned / domain-driven].

Justification: [one to three sentences citing specific TABLE B rows by Area value and the
dominant INR-NN pattern. Reference TABLE E headcount range.]

#### TABLE H — Org Shape Delta

`(C-66/C-69: BRIDGE RULE applies — every Driving Evidence cell must cite at least one TABLE B
row; C-10: Current State and Recommended State clearly separated as named columns)`

**Pre-production assertion (C-69):**
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE (restated at production point, C-69): Every TABLE H row must carry at least one
`(cite TABLE B row)` annotation in its Driving Evidence cell. BRIDGE RULE violation = any row
with no TABLE B citation.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [what the scan found — C-10 current] | [C-10 recommended] | (cite TABLE B row: [Area value]) — [one sentence] |
| Cross-cutting concern handling | [current — C-04] | [recommended] | (cite TABLE B row: [Area value]) — [one sentence] |
| Headcount distribution | [current range from TABLE E] | [recommended range] | (cite TABLE B row: [Area value]) — [one sentence] |
| Boundary clarity | [current state of team boundary signals] | [recommended boundary structure] | (cite TABLE B row: [Area value]) — [one sentence] |

*Actual TABLE H row count: [N]. Matches pre-production assertion: [YES / NO — BRIDGE RULE
compliance: YES / NO — any row without TABLE B citation is a BRIDGE RULE violation].*

#### Current State vs Recommended State Summary

`(C-10: clearly separated; C-07: org shape named)`

**Current state**: [two to four sentences describing what the scan found — org shape as
inferred from evidence. No invention. Cite dominant INR-NN pattern and TABLE B rows.]

**Recommended state**: [two to four sentences describing the recommended org shape adjustment.
Named shape type. Reference TABLE H dimensions. No org chart produced here — raw analysis only.]

#### Evidence Gaps Acknowledged

`(C-08: gaps flagged; references TABLE G)`

[One sentence per TABLE G row acknowledging the gap and its impact on the recommended state.
Gaps do not invalidate the analysis — they bound its confidence.]

---

> "org-scan complete (R19 V-01 — Role Sequence: SCANNER/SYNTHESIZER named groups with
> schema-first placement). SCHEMA DECLARATIONS declared before GROUP A: TABLE B, TABLE C,
> TABLE D, TABLE E, TABLE F (transport manifest with per-edge purpose — C-67), COVERAGE
> ATTESTATION with Minimum rows: 7 (C-68 gate-blocking), TABLE H with BRIDGE RULE (C-69).
> GATE TOKEN PROTOCOL preamble covers SCAN GATE pass and fail tokens (C-20/C-22). INERTIA
> PATTERN DICTIONARY INR-01..INR-06 constrained TABLE B Inertia Match column (C-23/C-25).
> TABLE H pre-production assertion: Org Shape Dimension count: N (C-69). Raw analysis only —
> no org chart, no reporting lines (C-05 stated twice: preamble + GROUP B output constraint)."

---

## V-02 — Output Format: Phase Footer PHASE OUTPUTS Blocks with Count Declarations

**Axis**: Output format
**Hypothesis**: V-01 places all schema declarations in the preamble and runs a gate at GROUP A
exit. V-02 adds explicit PHASE OUTPUTS footer blocks at the end of GROUP A and GROUP B,
declaring the produced artifact names, row counts, and gate token written. Footer declarations
make C-68 (COVERAGE ATTESTATION row count) and C-69 (TABLE H row count assertion) independently
verifiable without re-reading the phase body: the footer names the deliverables precisely with
counts. Combined with the SCAN GATE CLEAR token, this gives scorers two independent verification
paths for row count compliance. Hypothesis: full C-67/C-68/C-69 coverage with highest
verifiability per criterion.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md, package.json,
design/ directories, namespaces, test coverage areas, SPECS.md files, existing .craft/roles/.
Produce a structured analysis: areas of work, team boundaries, cross-cutting concerns, headcount
signals, and recommended org shape. Output is raw analysis only — not an org chart, not reporting
lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — first statement)**: RAW ANALYSIS ONLY. No org chart. No reporting
lines. No .craft/roles/ creation. No hierarchy. Violation is a critical failure.

---

### PREAMBLE

`(C-20: GATE TOKEN PROTOCOL; C-23: INERTIA PATTERN DICTIONARY; C-61/C-68: SCHEMA DECLARATIONS)`

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan (C-20)
(C-22: gate is postcondition of GROUP A and precondition of GROUP B)

SCAN GATE:
  PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"
  FAIL TOKEN: "SCAN GATE FAIL — [reason: source count / path floor / attestation row count]"

  Gate-blocking conditions — any one unmet causes FAIL TOKEN:
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ file paths in TABLE B (C-09/C-16)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68 — schema minimum rows requirement)
```

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan (C-23)
(Inertia Match column constrained to these labels; C-25: positioned before File Path Evidence)

INR-01  Org-by-function     Functional silo alignment (eng, design, QA)
INR-02  Org-by-product      Product area or feature surface alignment
INR-03  Org-by-layer        Technical layer alignment (frontend, backend, infra)
INR-04  Org-by-domain       Business domain / bounded context alignment
INR-05  Org-by-geography    Region or timezone alignment
INR-06  Org-by-customer     Customer segment or vertical alignment
```

#### SCHEMA DECLARATIONS

```
TABLE B — Scan Evidence Table
  Columns (required): Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note
  Minimum rows: 5  (path floor gate — C-16/C-61)
  Inertia Match: constrained to INR-01..INR-06 (C-23); positioned before File Path Evidence (C-25)

TABLE C — Cross-Cutting Concerns
  Columns (required): Concern Name | Boundary Note | Evidence Path
  Minimum rows: 1

TABLE D — Team Boundary Candidates
  Columns (required): Boundary Candidate | Seam Rationale | Evidence Citation
  Minimum rows: 1

TABLE E — Headcount Signals
  Columns (required): Signal Source | Headcount Range | Rationale
  Minimum rows: 1

TABLE F — Transport Manifest (Output Consumers)
  (C-64/C-67: per-edge purpose annotation required; form: consuming role — table(s) — purpose)
  Columns (required): Producing Role | Consuming Role | Tables Consumed | Analytical Purpose
  Minimum rows: 2

COVERAGE ATTESTATION
  (C-65/C-68: first-class schema entry; Minimum rows: 7 — gate-blocking; status constrained:
   scanned / not-found / not-applicable; SCANNER references "source types declared in COVERAGE
   ATTESTATION schema" rather than restating the list inline)
  Columns (required): Source Type | Status | Notes
  Source types declared (7 total):
    1. CLAUDE.md files
    2. package.json / workspace configs
    3. design/ directories
    4. namespace / module directories
    5. test coverage areas
    6. SPECS.md files
    7. existing .craft/roles/ files
  Minimum rows: 7  (C-68: gate-blocking)

TABLE G — Evidence Gaps and Ambiguities
  Columns (required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

TABLE H — Org Shape Delta
  (C-66/C-69: BRIDGE RULE applies; Minimum rows: N per pre-production assertion)
  Columns (required): Dimension | Current State | Recommended State | Driving Evidence
  BRIDGE RULE (C-69 named constraint):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any row lacking this citation is a BRIDGE RULE violation."
  Minimum rows: N  (declared by SYNTHESIZER pre-production assertion — see GROUP B)
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before GROUP B; C-11: anti-fabrication per
evidence-dependent section; C-13: C-05 stated in preamble and in GROUP B output constraint)`

**HARD BOUNDARY (C-05)**: RAW ANALYSIS ONLY throughout this response. No org chart, no
reporting lines, no role files.

**Anti-fabrication rule (C-11)**: Every TABLE B row requires an Anti-Fabrication Note.
Do not invent file paths, area names, or inertia patterns. Only report what the scan finds.

Walk: scan the source types declared in COVERAGE ATTESTATION schema (see SCHEMA DECLARATIONS).

#### TABLE B — Scan Evidence Table

`(C-19: Inertia Match column; C-25: Inertia Match before File Path Evidence; C-21: all columns
required; C-09: specific paths; C-11: Anti-Fabrication Note per row)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

Dominant pattern: [INR-NN] — [one sentence justification]

#### TABLE C — Cross-Cutting Concerns

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [boundary description] | [specific/path] |

#### TABLE D — Team Boundary Candidates

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [seam rationale] | [specific/path] |

#### TABLE E — Headcount Signals

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [N to N] | [one sentence] |

#### COVERAGE ATTESTATION

`(C-65/C-68: 7 rows required; status constrained to scanned/not-found/not-applicable;
 source types referenced from COVERAGE ATTESTATION schema declaration above, not restated)`

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned/not-found/not-applicable] | [notes] |
| package.json / workspace configs | [scanned/not-found/not-applicable] | [notes] |
| design/ directories | [scanned/not-found/not-applicable] | [notes] |
| namespace / module directories | [scanned/not-found/not-applicable] | [notes] |
| test coverage areas | [scanned/not-found/not-applicable] | [notes] |
| SPECS.md files | [scanned/not-found/not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned/not-found/not-applicable] | [notes] |

#### TABLE G — Evidence Gaps and Ambiguities

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(C-64/C-67: each entry: consuming role — table(s) — analytical purpose in consuming phase)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE; uses TABLE C cross-cutting concerns for synthesis recommendations; uses TABLE D boundary candidates for recommended state; uses TABLE E headcount range for dimension analysis; uses TABLE G to bound recommendation confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build uses TABLE H Org Shape Delta rows to configure the target org structure at each dimension; the Current State column establishes the baseline org-build departs from; Recommended State drives the target configuration |

---

**SCAN GATE**

```
SCAN GATE VERIFICATION CHECKLIST (C-14: numbered items + confirmation sentence)

[1] TABLE B rows: [N] — gate requires 5+ (path floor: [MET/NOT MET])
[2] Source types scanned: [N] of 7 — gate requires 3+ (C-02: [MET/NOT MET])
[3] COVERAGE ATTESTATION rows: [N] — gate requires exactly 7 (C-68: [MET/NOT MET])
[4] TABLE B Inertia Match values: all INR-01..INR-06 (C-23: [MET/NOT MET])
[5] Inertia Match column before File Path Evidence in TABLE B (C-25: [MET/NOT MET])
[6] All TABLE B rows have Anti-Fabrication Note (C-11: [MET/NOT MET])
[7] No org chart, reporting lines, or .craft/roles/ content (C-05: [MET/NOT MET])

Write PASS TOKEN if all 7 items [MET]:
  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"

Write FAIL TOKEN if any item [NOT MET]:
  "SCAN GATE FAIL — item [N]: [reason]"
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may proceed only if
SCAN GATE PASS TOKEN is present as the final line above."*

```
GROUP A PHASE OUTPUTS (C-37 pattern — footer declaration)
  TABLE B rows produced: [N]
  TABLE C rows produced: [N]
  TABLE D rows produced: [N]
  TABLE E rows produced: [N]
  COVERAGE ATTESTATION rows: [N]  (C-68: gate-blocking floor = 7; status: [MET/NOT MET])
  TABLE G rows produced: [N]
  TABLE F rows produced: [N]
  Gate token written: [PASS TOKEN / FAIL TOKEN — verbatim]
  Dominant inertia pattern: [INR-NN]
  File paths cited: [N] (gate floor = 5; status: [MET/NOT MET])
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: begins on SCAN GATE PASS TOKEN only; C-10: current vs
recommended state clearly separated; C-07: org shape named and justified)`

**Precondition**: Verify GROUP A final line is SCAN GATE PASS TOKEN. If FAIL TOKEN, write it
verbatim and halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy diagram. Named recommendations only — no drawn structure.

#### Org Shape Assessment

`(C-07: org shape named from findings; C-03: headcount from TABLE E)`

Dominant pattern from GROUP A: [INR-NN — named shape].

Org shape inferred: [named shape type]. Justification: [two to three sentences citing specific
TABLE B rows by Area value and explaining the inertia pattern dominance. Reference TABLE E
headcount range to size the analysis.]

#### TABLE H — Org Shape Delta

`(C-66/C-69: BRIDGE RULE; C-10: Current State / Recommended State separated as columns)`

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE enforcement (C-69): every Driving Evidence cell must contain at least one
`(cite TABLE B row)` annotation. No exceptions.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended — C-10] | (cite TABLE B row: [Area]) — [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Headcount distribution model | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |

*Post-production check: TABLE H rows = [N]. Matches assertion: [YES/NO].
BRIDGE RULE compliance: all rows have TABLE B citation: [YES/NO].*

#### Current State vs Recommended State Summary

**Current state (C-10)**: [Three to five sentences synthesising what the scan evidence shows
about the current org structure — grounded in TABLE B dominant pattern, TABLE C cross-cutting
concerns, TABLE D boundaries. No invention.]

**Recommended state (C-10)**: [Three to five sentences describing the recommended org shape
adjustment. Named shape. Reference TABLE H dimensions. This is raw analysis — no org chart.]

#### Evidence Gaps Acknowledged

`(C-08: references TABLE G)`

[One sentence per TABLE G row: acknowledge the gap, state its impact on recommendation
confidence.]

```
GROUP B PHASE OUTPUTS (footer declaration)
  TABLE H rows produced: [N]  (assertion declared: "Dimension count: [N]"; match: [YES/NO])
  BRIDGE RULE compliance: all TABLE H Driving Evidence cells cite TABLE B: [YES/NO]
  Org shape named: [INR-NN / named shape type]
  Current vs Recommended clearly separated: YES (C-10)
  Evidence gaps acknowledged: [N] from TABLE G
  Raw analysis only — no org chart, no reporting lines: CONFIRMED (C-05)
```

---

> "org-scan complete (R19 V-02 — Output Format: Phase Footer PHASE OUTPUTS blocks).
> GROUP A PHASE OUTPUTS footer declares: TABLE B [N] rows, COVERAGE ATTESTATION [N]=7 rows
> (C-68 gate-blocking confirmed), gate token: [PASS/FAIL]. GROUP B PHASE OUTPUTS footer
> declares: TABLE H [N] rows matching pre-production assertion [N] (C-69), BRIDGE RULE
> compliance [YES/NO], org shape named [INR-NN]. TABLE F transport manifest carries per-edge
> purpose annotation on all 2 edges (C-67). C-05 stated twice: preamble constraint + GROUP B
> output constraint. Raw analysis only."

---

## V-03 — Lifecycle Emphasis: Maximum Preamble Density

**Axis**: Lifecycle emphasis
**Hypothesis**: V-01 and V-02 place key declarations in the preamble but still leave some
structural elements at their point of use (e.g., BRIDGE RULE restated before TABLE H,
COVERAGE ATTESTATION source-type list only in schema). V-03 concentrates ALL structural
declarations — SCHEMA DECLARATIONS, GATE TOKEN PROTOCOL, INERTIA PATTERN DICTIONARY, BRIDGE
RULE, TABLE F transport manifest template, and the complete source-type enumeration for
COVERAGE ATTESTATION — in the preamble before GROUP A begins. GROUP A and GROUP B body
instructions then reference preamble declarations rather than re-declaring inline. Tests
whether maximum preamble concentration yields the highest structural completeness score for
C-67/C-68/C-69 because a scorer can verify all three criteria from the preamble alone.
Hypothesis: full C-67/C-68/C-69 coverage plus possible lift on structural-detectability scoring.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md, package.json,
design/ directories, namespaces, test coverage areas, SPECS.md files, existing .craft/roles/.
Produce a structured analysis: areas of work, team boundaries, cross-cutting concerns, headcount
signals, and recommended org shape.

**OUTPUT CONSTRAINT (C-05 — first statement)**: This skill produces RAW ANALYSIS ONLY.
No org chart. No reporting lines. No .craft/roles/ files. No hierarchy. Any violation is a
critical failure regardless of all other scores.

---

### PREAMBLE — ALL STRUCTURAL DECLARATIONS

`(C-20: GATE TOKEN PROTOCOL; C-23: INERTIA PATTERN DICTIONARY; C-61/C-68: SCHEMA DECLARATIONS
with Minimum rows; C-69: BRIDGE RULE; C-64/C-67: TABLE F template; all declared here — GROUP A
and GROUP B reference these declarations rather than re-declaring inline)`

---

#### GATE TOKEN PROTOCOL (C-20)

```
GATE TOKEN PROTOCOL — org-scan
(C-22: gate is simultaneously the postcondition of GROUP A and the precondition of GROUP B)

SCAN GATE:
  PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN label]"
  FAIL TOKEN: "SCAN GATE FAIL — [condition that failed: source count / path floor / attestation]"

  Gate-blocking conditions — ALL must be MET for PASS TOKEN:
  [ ] C-02: 3 or more source types scanned
  [ ] C-09/C-16: 5 or more specific file paths in TABLE B
  [ ] C-68: COVERAGE ATTESTATION has exactly 7 rows (schema minimum rows requirement)

  If any condition is NOT MET: write FAIL TOKEN and halt. GROUP B may not begin.
  If ALL conditions are MET: write PASS TOKEN. GROUP B may begin.
```

---

#### INERTIA PATTERN DICTIONARY (C-23)

```
INERTIA PATTERN DICTIONARY
Valid values for TABLE B Inertia Match column (C-25: positioned before File Path Evidence):

INR-01  Org-by-function     Functional silo — eng / design / QA / ops separated regardless of product
INR-02  Org-by-product      Product or feature surface alignment
INR-03  Org-by-layer        Technical layer — frontend / backend / infra / data
INR-04  Org-by-domain       Business domain or bounded context alignment
INR-05  Org-by-geography    Region or timezone-driven team boundaries
INR-06  Org-by-customer     Customer segment or vertical-driven boundaries

Constraint: TABLE B Inertia Match cells must contain only these labels. Free-text is a
structurally detectable violation by comparison against this dictionary.
```

---

#### SCHEMA DECLARATIONS (C-21/C-61/C-68)

```
TABLE B — Scan Evidence Table
  Purpose: primary scan output; cited by TABLE H Driving Evidence cells (BRIDGE RULE)
  Columns (all required — C-21):
    Area                   traceable to scan evidence; not invented (C-01)
    Source Type            one of the 7 source types from COVERAGE ATTESTATION schema
    Inertia Match          constrained to INR-01..INR-06; positioned before File Path (C-25)
    File Path Evidence     specific repo path; not a generic phrase (C-09/C-21)
    Anti-Fabrication Note  hedging sentence per row (C-11)
  Minimum rows: 5          path floor gate — C-16/C-61; gate-blocking

TABLE C — Cross-Cutting Concerns
  Columns (all required): Concern Name | Boundary Note | Evidence Path
  Minimum rows: 1

TABLE D — Team Boundary Candidates
  Columns (all required): Boundary Candidate | Seam Rationale | Evidence Citation
  Minimum rows: 1

TABLE E — Headcount Signals
  Columns (all required): Signal Source | Headcount Range | Rationale
  Minimum rows: 1

TABLE F — Transport Manifest (Output Consumers)
  Purpose: per-edge dependency declaration with purpose annotation (C-64/C-67)
  Columns (all required):
    Producing Role         the group/role that produces the output
    Consuming Role         the downstream group/role that reads the output
    Tables Consumed        specific table names
    Analytical Purpose     C-67: what the consuming role does with these tables;
                           form: [consuming role] — [table(s)] — [analytical purpose];
                           any entry lacking Analytical Purpose is a C-67 violation
  Minimum rows: 2

COVERAGE ATTESTATION
  Purpose: per-source-type audit trail; distinguishes structural vs evidential absence (C-65)
  Status vocabulary: scanned / not-found / not-applicable  (constrained — C-65)
    scanned:         source type applicable and evidence found
    not-found:       source type applicable but no evidence detected
    not-applicable:  source type structurally absent from this repo type
  Columns (all required): Source Type | Status | Notes
  Source types declared (GROUP A references this list — not restated inline — C-68):
    1.  CLAUDE.md files
    2.  package.json / workspace configs
    3.  design/ directories
    4.  namespace / module directories
    5.  test coverage areas
    6.  SPECS.md files
    7.  existing .craft/roles/ files
  Minimum rows: 7            C-68 gate-blocking — SCAN GATE fails if row count < 7

TABLE G — Evidence Gaps and Ambiguities
  Columns (all required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

TABLE H — Org Shape Delta
  Purpose: per-dimension current-vs-recommended comparison with scan evidence linkage (C-66/C-69)
  Columns (all required):
    Dimension         named org shape dimension
    Current State     what scan evidence shows today (C-10)
    Recommended State what analysis recommends (C-10)
    Driving Evidence  must contain at least one "(cite TABLE B row)" annotation (C-66/C-69)
  Minimum rows: N    declared by SYNTHESIZER pre-production assertion (C-69)

  BRIDGE RULE (C-69 — named structural constraint, declared here):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any TABLE H row lacking a TABLE B citation is a BRIDGE RULE
     violation detectable by table correspondence alone without prose inspection."
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before GROUP B begins; C-11: anti-fabrication
per evidence-dependent section; C-13: C-05 stated in preamble and again in GROUP B)`

**Anti-fabrication rule**: Every TABLE B, TABLE C, TABLE D, TABLE E row must contain
evidence-grounded content. Do not invent file paths, area names, or patterns. If a source type
yields no evidence, record `not-found` in COVERAGE ATTESTATION. Do not fabricate rows.

**Scan instruction**: Walk the repo scanning the source types declared in the COVERAGE ATTESTATION
schema (see PREAMBLE SCHEMA DECLARATIONS — source type list not restated here per C-68
schema-first reference pattern).

#### TABLE B

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01: from scan] | [source type from COVERAGE ATTESTATION schema] | [INR-NN] | [specific/path] | [hedging sentence — C-11] |
| [area 2] | [source type] | [INR-NN] | [specific/path] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path] | [hedging sentence] |

Dominant pattern: [INR-NN] — [one sentence justification citing area distribution]

#### TABLE C

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [boundary — C-04] | [specific/path] |

#### TABLE D

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [rationale] | [specific/path] |

#### TABLE E

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [N to N] | [sentence] |

#### COVERAGE ATTESTATION

`(C-65/C-68: 7 rows; status from constrained vocabulary; source types from PREAMBLE schema)`

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned/not-found/not-applicable] | [notes] |
| package.json / workspace configs | [scanned/not-found/not-applicable] | [notes] |
| design/ directories | [scanned/not-found/not-applicable] | [notes] |
| namespace / module directories | [scanned/not-found/not-applicable] | [notes] |
| test coverage areas | [scanned/not-found/not-applicable] | [notes] |
| SPECS.md files | [scanned/not-found/not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned/not-found/not-applicable] | [notes] |

#### TABLE G

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest

`(C-64/C-67: form from PREAMBLE schema: producing role — consuming role — tables — purpose)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence per BRIDGE RULE declared in PREAMBLE; synthesizes TABLE C into cross-cutting concern recommendations; uses TABLE D boundary candidates as Recommended State inputs; uses TABLE E headcount range in Headcount Distribution dimension; uses TABLE G to bound recommendation confidence statements |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H row by row — Dimension drives what aspect of org to configure; Current State drives the baseline; Recommended State drives the target; Driving Evidence TABLE B citations provide the scan provenance org-build presents to reviewers |

---

**SCAN GATE**

```
SCAN GATE VERIFICATION CHECKLIST (C-14: numbered items; C-17: named-token confirmation)

[1] TABLE B rows: [N] — requires 5+ (C-16): [MET / NOT MET]
[2] Source types: [N] of 7 scanned — requires 3+ (C-02): [MET / NOT MET]
[3] COVERAGE ATTESTATION rows: [N] — requires exactly 7 (C-68): [MET / NOT MET]
[4] TABLE B Inertia Match values in INR-01..INR-06 (C-23): [MET / NOT MET]
[5] Inertia Match before File Path Evidence in TABLE B schema (C-25): [MET / NOT MET]
[6] All TABLE B rows have Anti-Fabrication Note (C-11): [MET / NOT MET]
[7] No org chart, no reporting lines, no .craft/roles/ content (C-05): [MET / NOT MET]

Write PASS TOKEN if [1]–[7] all MET:
  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"

Write FAIL TOKEN if any NOT MET (C-18: named failure-state string):
  "SCAN GATE FAIL — item [N]: [specific reason]"

GROUP A is the postcondition of the SCAN GATE. GROUP B is the precondition.
GROUP B may not begin until the PASS TOKEN above is written. (C-22 bidirectional contract)
```

*Required confirmation sentence (C-14/C-17): "GROUP A complete. GROUP B / SYNTHESIZER may
begin only if SCAN GATE PASS TOKEN is the final output line of GROUP A."*

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: begins only on PASS TOKEN; C-10: current vs recommended
clearly separated; C-07: org shape named; C-69: pre-production assertion before TABLE H)`

**Precondition**: Final GROUP A output line must be PASS TOKEN. If FAIL TOKEN, write it
verbatim and stop.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No role files. No hierarchy. These constraints apply to every section below.

**BRIDGE RULE reminder** (declared in PREAMBLE — see SCHEMA DECLARATIONS for TABLE H):
Every TABLE H Driving Evidence cell must contain at least one `(cite TABLE B row)` annotation.

#### Org Shape Assessment (C-07/C-03)

Dominant pattern: [INR-NN]. Org shape inferred: [named type].
Justification: [two to three sentences citing specific TABLE B rows by Area value].
Headcount signal: TABLE E range [N to N] — [one sentence sizing context].

#### TABLE H — Org Shape Delta

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended — C-10] | (cite TABLE B row: [Area]) [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) [sentence] |
| Headcount distribution | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) [sentence] |
| Boundary definition approach | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) [sentence] |

*Row count: [N]. Assertion match: [YES/NO]. BRIDGE RULE compliance: [YES/NO].*

#### Current State vs Recommended State Summary (C-10)

**Current state**: [synthesised from TABLE B dominant pattern, TABLE C, TABLE D. No invention.]

**Recommended state**: [named shape adjustment, referencing TABLE H dimensions. Raw analysis.
No org chart produced here.]

#### Evidence Gaps (C-08 — references TABLE G)

[One sentence per TABLE G row acknowledging gap and impact on recommendation confidence.]

---

> "org-scan complete (R19 V-03 — Lifecycle Emphasis: Maximum Preamble Density). All structural
> declarations in PREAMBLE before GROUP A: GATE TOKEN PROTOCOL (C-20/C-22), INERTIA PATTERN
> DICTIONARY INR-01..INR-06 (C-23/C-25), SCHEMA DECLARATIONS for all 8 tables including TABLE F
> transport manifest with C-67 per-edge purpose form and COVERAGE ATTESTATION with Minimum rows:
> 7 gate-blocking (C-68) and BRIDGE RULE for TABLE H (C-69). GROUP A references preamble
> declarations — source-type list not restated inline (C-68 schema-first pattern). TABLE H
> pre-production assertion: Org Shape Dimension count: N (C-69). C-05 stated twice: preamble
> constraint + GROUP B output constraint. Raw analysis only."

---

## V-04 — Phrasing Register: Imperative / Prescriptive Throughout

**Axis**: Phrasing register
**Hypothesis**: V-01 through V-03 use a declarative/descriptive register for most instructions
("Each row must include...", "The table carries..."). V-04 switches to a fully imperative
register throughout: every instruction is a direct command ("Include an Anti-Fabrication Note
in every TABLE B row.", "Declare BRIDGE RULE before TABLE H.", "Write PASS TOKEN only if all
gate-blocking conditions are met."). The hypothesis is that imperative phrasing produces more
reliable gate-blocking enforcement — particularly for C-67 (each Output Consumers entry MUST
carry a purpose annotation), C-68 (COVERAGE ATTESTATION row floor MUST be gate-blocking),
and C-69 (SYNTHESIZER MUST record the pre-production assertion before producing TABLE H).
Hypothesis: imperative register elevates structural compliance on the three new criteria.

---

You are running `org-scan`. Walk the repo. Infer the org structure. Produce a structured
analysis: areas of work, team boundaries, cross-cutting concerns, headcount signals, and
recommended org shape.

**STOP. READ THIS BEFORE PRODUCING ANY OUTPUT (C-05 — first statement)**:
Produce RAW ANALYSIS ONLY. Do not produce an org chart. Do not produce reporting lines.
Do not produce a hierarchy diagram. Do not create or reference .craft/roles/ files.
Violating this constraint fails the skill regardless of all other criteria.

---

### PREAMBLE

`(Declare all protocols and schemas here. Do not restate them inline in GROUP A or GROUP B.)`

#### GATE TOKEN PROTOCOL — Declare Now (C-20)

```
GATE TOKEN PROTOCOL
Define these constants. Use them verbatim at the SCAN GATE.

PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"
FAIL TOKEN: "SCAN GATE FAIL — [failed condition: source count / path floor / attestation rows]"

Gate-blocking conditions. Write FAIL TOKEN if ANY are not met:
  CONDITION 1: TABLE B contains 5 or more rows with specific file paths (C-02/C-09/C-16)
  CONDITION 2: 3 or more distinct source types are represented in TABLE B (C-02)
  CONDITION 3: COVERAGE ATTESTATION contains exactly 7 rows (C-68 — gate-blocking requirement)

Write PASS TOKEN only when ALL THREE conditions are confirmed.
The PASS TOKEN is simultaneously the postcondition of GROUP A and the precondition of GROUP B.
Do not begin GROUP B unless the PASS TOKEN is present. (C-22)
```

#### INERTIA PATTERN DICTIONARY — Declare Now (C-23)

```
INERTIA PATTERN DICTIONARY
Constrain every TABLE B Inertia Match cell to one of these labels. Write no other values.
Position Inertia Match BEFORE File Path Evidence in TABLE B. (C-25)

INR-01  Org-by-function     Functional silo (eng / design / QA / ops separate from product)
INR-02  Org-by-product      Product or feature surface boundaries
INR-03  Org-by-layer        Technical layer (frontend / backend / infra / data)
INR-04  Org-by-domain       Business domain or bounded context
INR-05  Org-by-geography    Regional or timezone-driven
INR-06  Org-by-customer     Customer segment or vertical
```

#### SCHEMA DECLARATIONS — Declare Now (C-21/C-61/C-68)

```
Declare all table schemas here. Reference these declarations in GROUP A and GROUP B.
Do not restate column definitions or source-type lists inline.

TABLE B — Scan Evidence Table
  REQUIRED COLUMNS: Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note
  MINIMUM ROWS: 5  (C-16/C-61 — gate-blocking: fail CONDITION 1 if not met)
  RULES:
    - Area: traceable to scan evidence; do not invent (C-01/C-11)
    - Source Type: use only source types from COVERAGE ATTESTATION schema (reference below)
    - Inertia Match: use only INR-01..INR-06 from INERTIA PATTERN DICTIONARY (C-23)
    - Inertia Match column: position BEFORE File Path Evidence column (C-25)
    - File Path Evidence: write a specific repo path; do not write generic phrases (C-09/C-21)
    - Anti-Fabrication Note: write one hedging sentence; do not omit (C-11)

TABLE C — Cross-Cutting Concerns
  REQUIRED COLUMNS: Concern Name | Boundary Note | Evidence Path
  MINIMUM ROWS: 1  (C-04)

TABLE D — Team Boundary Candidates
  REQUIRED COLUMNS: Boundary Candidate | Seam Rationale | Evidence Citation
  MINIMUM ROWS: 1  (C-06)

TABLE E — Headcount Signals
  REQUIRED COLUMNS: Signal Source | Headcount Range | Rationale
  MINIMUM ROWS: 1  (C-03; write a range, not a point estimate)

TABLE F — Transport Manifest
  REQUIRED COLUMNS: Producing Role | Consuming Role | Tables Consumed | Analytical Purpose
  MINIMUM ROWS: 2
  RULE (C-67): Write Analytical Purpose for every row. Use this form exactly:
    "[consuming role] — [table(s)] — [analytical purpose in consuming phase]"
    Omitting Analytical Purpose from any row is a C-67 violation.

COVERAGE ATTESTATION
  REQUIRED COLUMNS: Source Type | Status | Notes
  MINIMUM ROWS: 7  (C-68 — gate-blocking: fail CONDITION 3 if row count != 7)
  STATUS VALUES: scanned | not-found | not-applicable  (write only these three values)
  SOURCE TYPES (declared here; GROUP A references this list — do not restate it inline):
    1. CLAUDE.md files
    2. package.json / workspace configs
    3. design/ directories
    4. namespace / module directories
    5. test coverage areas
    6. SPECS.md files
    7. existing .craft/roles/ files

TABLE G — Evidence Gaps and Ambiguities
  REQUIRED COLUMNS: Gap / Ambiguity | Impact | Recommended Follow-Up
  MINIMUM ROWS: 1  (C-08)

TABLE H — Org Shape Delta
  REQUIRED COLUMNS: Dimension | Current State | Recommended State | Driving Evidence
  MINIMUM ROWS: N  (declared by SYNTHESIZER pre-production assertion — see C-69 below)
  BRIDGE RULE (C-69 — named structural constraint):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Write no TABLE H row without a TABLE B citation.
     Any row lacking a TABLE B citation is a BRIDGE RULE violation."
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: complete all tables before GROUP B; C-11: anti-fabrication
enforced per row; C-13: C-05 stated in preamble and again in GROUP B precondition)`

Scan source types declared in COVERAGE ATTESTATION schema. Do not restate the list here.
Record findings in the tables declared in SCHEMA DECLARATIONS. Do not invent rows.
If a source type yields no evidence, record `not-found` in COVERAGE ATTESTATION.

#### TABLE B

`(Follow TABLE B schema from SCHEMA DECLARATIONS; Inertia Match before File Path Evidence)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area] | [source type] | [INR-NN] | [specific/path/file] | [hedging sentence] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file] | [hedging sentence] |

Dominant pattern: [INR-NN] — [one sentence justification]

#### TABLE C

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern] | [boundary description] | [specific/path] |

#### TABLE D

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate] | [seam rationale] | [specific/path] |

#### TABLE E

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source] | [N to N] | [sentence] |

#### COVERAGE ATTESTATION

Produce exactly 7 rows. Use status values from SCHEMA DECLARATIONS only.
Source types from SCHEMA DECLARATIONS — not restated here (C-68 schema-first pattern).

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned/not-found/not-applicable] | [notes] |
| package.json / workspace configs | [scanned/not-found/not-applicable] | [notes] |
| design/ directories | [scanned/not-found/not-applicable] | [notes] |
| namespace / module directories | [scanned/not-found/not-applicable] | [notes] |
| test coverage areas | [scanned/not-found/not-applicable] | [notes] |
| SPECS.md files | [scanned/not-found/not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned/not-found/not-applicable] | [notes] |

#### TABLE G

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap] | [impact] | [action] |

#### TABLE F — Transport Manifest

Write Analytical Purpose for EVERY row. Omitting it is a C-67 violation.
Use the form: [consuming role] — [table(s)] — [analytical purpose in consuming phase].

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | GROUP B / SYNTHESIZER — TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION — SYNTHESIZER cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE; derives cross-cutting recommendations from TABLE C; generates boundary Recommended State from TABLE D; sets headcount dimension from TABLE E; acknowledges gaps from TABLE G; bounds confidence using COVERAGE ATTESTATION status values |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build — TABLE H — org-build reads each TABLE H row in sequence: Dimension names the org construct to configure; Current State provides the baseline the org is departing from; Recommended State drives the target configuration; Driving Evidence TABLE B citations provide scan provenance org-build surfaces during construction review |

---

**SCAN GATE**

```
SCAN GATE VERIFICATION CHECKLIST
Number each item. Write the gate token defined in GATE TOKEN PROTOCOL. (C-14/C-17/C-18)

[1] Count TABLE B rows: [N] — CONDITION 1 requires 5+ — result: [MET / NOT MET]
[2] Count distinct source types in TABLE B: [N] — CONDITION 2 requires 3+ — result: [MET / NOT MET]
[3] Count COVERAGE ATTESTATION rows: [N] — CONDITION 3 requires exactly 7 — result: [MET / NOT MET]
[4] Verify TABLE B Inertia Match values are in INR-01..INR-06: [MET / NOT MET]
[5] Verify Inertia Match column appears before File Path Evidence in TABLE B: [MET / NOT MET]
[6] Verify every TABLE B row has an Anti-Fabrication Note: [MET / NOT MET]
[7] Verify TABLE F has Analytical Purpose on every row: [MET / NOT MET]
[8] Verify no org chart, reporting lines, or .craft/roles/ content anywhere above: [MET / NOT MET]

Write the PASS TOKEN if items [1]–[8] all read MET:
  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"

Write the FAIL TOKEN if any item reads NOT MET (C-18 named failure-state string):
  "SCAN GATE FAIL — item [N]: [reason from GATE TOKEN PROTOCOL]"
```

*Required confirmation sentence (C-14/C-17): "GROUP A complete. GROUP B / SYNTHESIZER
must not begin unless the SCAN GATE PASS TOKEN appears as the final line above."*

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: PASS TOKEN required; C-10: separated columns in TABLE H;
C-07: named org shape; C-69: pre-production assertion before TABLE H)`

**Precondition check**: Read the final output line of GROUP A. If it is the FAIL TOKEN, write
it verbatim. Stop. Produce no further output.

**READ THIS BEFORE PRODUCING ANY OUTPUT (C-05 — second statement)**:
Produce RAW ANALYSIS ONLY. Do not produce an org chart. Do not produce reporting lines.
Do not produce a hierarchy. Do not create role files. This applies to every line below.

#### Org Shape Assessment

`(C-07: named and justified from findings; C-03: headcount range from TABLE E)`

Dominant pattern: [INR-NN]. Named org shape: [shape type].
Justification: [two to three sentences. Cite TABLE B rows by Area. Reference TABLE E range.]

#### TABLE H — Org Shape Delta

**Pre-production assertion (C-69 — write this line before the table)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

**Apply BRIDGE RULE** (from SCHEMA DECLARATIONS PREAMBLE): write at least one
`(cite TABLE B row)` annotation in every Driving Evidence cell.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended — C-10] | (cite TABLE B row: [Area]) [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) [sentence] |
| Headcount distribution | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) [sentence] |
| Boundary definition approach | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) [sentence] |

Post-production BRIDGE RULE check: Every Driving Evidence cell has a TABLE B citation: [YES/NO].
TABLE H row count: [N]. Matches pre-production assertion: [YES/NO].

#### Current State vs Recommended State Summary (C-10)

**Current state**: [synthesised from TABLE B, TABLE C, TABLE D. Cite evidence. Do not invent.]

**Recommended state**: [named shape adjustment. Reference TABLE H. No org chart. Raw analysis.]

#### Evidence Gaps (C-08 — TABLE G)

[One sentence per TABLE G row: name the gap, state its impact on recommendation confidence.]

---

> "org-scan complete (R19 V-04 — Phrasing Register: Imperative/Prescriptive). Imperative
> register applied throughout: GATE TOKEN PROTOCOL uses 'Write PASS TOKEN only when...',
> SCHEMA DECLARATIONS use 'REQUIRED COLUMNS:', 'MINIMUM ROWS:', 'Write Analytical Purpose
> for every row. Omitting it is a C-67 violation.' (C-67 gate-blocking imperative), TABLE F
> form enforced via 'Use this form exactly:' (C-67), COVERAGE ATTESTATION source-type list in
> PREAMBLE SCHEMA not restated inline (C-68 schema-first), TABLE H pre-production assertion
> written as 'Write this line before the table' (C-69), BRIDGE RULE as 'Write no TABLE H row
> without a TABLE B citation' (C-69). C-05 stated twice: preamble 'STOP. READ THIS.' +
> GROUP B 'READ THIS BEFORE PRODUCING ANY OUTPUT.' Raw analysis only."

---

## V-05 — Combination: Phase Footer PHASE OUTPUTS Blocks + Maximum Preamble Density

**Axis**: Combination (V-02 phase footers + V-03 maximum preamble density)
**Hypothesis**: V-02 produces verifiability via footer declarations (scorers can check row
counts from footers alone). V-03 produces verifiability via preamble concentration (scorers can
check all three new criteria from the preamble alone). Combined, these two axes create dual
verification paths for C-67/C-68/C-69: the preamble declares what will be produced (including
TABLE F purpose form, COVERAGE ATTESTATION 7-row floor, BRIDGE RULE), and the phase footers
confirm what was produced (COVERAGE ATTESTATION actual rows, TABLE H actual rows vs assertion,
TABLE F purpose annotation completeness). No criterion in the new three requires prose reading
when both preamble and footer are present. Hypothesis: highest combined verifiability score
for C-67/C-68/C-69 of any variation in this round.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md, package.json,
design/ directories, namespaces, test coverage areas, SPECS.md files, existing .craft/roles/.
Produce a structured analysis: areas of work, team boundaries, cross-cutting concerns, headcount
signals, and recommended org shape. Output is raw analysis only — not an org chart, not reporting
lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — first statement)**: RAW ANALYSIS ONLY. No org chart. No reporting
lines. No .craft/roles/ files. No hierarchy. This constraint applies to every section.
Violation is a critical failure.

---

### PREAMBLE — ALL DECLARATIONS BEFORE GROUP A

`(C-20: GATE TOKEN PROTOCOL; C-23: INERTIA PATTERN DICTIONARY; C-21/C-61/C-68: SCHEMA
DECLARATIONS; C-69: BRIDGE RULE; C-67: TABLE F form; all declared before GROUP A begins)`

---

#### GATE TOKEN PROTOCOL (C-20/C-22)

```
GATE TOKEN PROTOCOL — org-scan
(C-22: SCAN GATE is the postcondition of GROUP A and the precondition of GROUP B)

SCAN GATE:
  PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"
  FAIL TOKEN: "SCAN GATE FAIL — [condition: source count / path floor / attestation row count]"

  Gate-blocking conditions (ALL must be confirmed for PASS TOKEN):
  [ ] CONDITION 1 (C-02/C-09/C-16): TABLE B has 5+ rows with specific file paths
  [ ] CONDITION 2 (C-02): 3+ distinct source types in TABLE B
  [ ] CONDITION 3 (C-68): COVERAGE ATTESTATION has exactly 7 rows (schema minimum requirement)

  On any unmet condition: write FAIL TOKEN; GROUP B halts immediately.
  On all conditions met: write PASS TOKEN; GROUP B may begin.
```

---

#### INERTIA PATTERN DICTIONARY (C-23/C-25)

```
INERTIA PATTERN DICTIONARY — org-scan
(C-25: Inertia Match column positioned before File Path Evidence in TABLE B schema)

INR-01  Org-by-function     Functional silos separate from product (eng, design, QA, ops)
INR-02  Org-by-product      Product area or feature surface alignment
INR-03  Org-by-layer        Technical layer alignment (frontend / backend / infra / data)
INR-04  Org-by-domain       Business domain or bounded context alignment
INR-05  Org-by-geography    Region or timezone-driven team structure
INR-06  Org-by-customer     Customer segment or vertical alignment

Constraint: TABLE B Inertia Match cells accept only INR-01..INR-06.
```

---

#### SCHEMA DECLARATIONS (C-21/C-61/C-68/C-69)

```
TABLE B — Scan Evidence Table
  Required columns: Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note
  Minimum rows: 5  (C-16/C-61 — gate-blocking via CONDITION 1)
  Column order: Inertia Match before File Path Evidence (C-25)

TABLE C — Cross-Cutting Concerns
  Required columns: Concern Name | Boundary Note | Evidence Path
  Minimum rows: 1

TABLE D — Team Boundary Candidates
  Required columns: Boundary Candidate | Seam Rationale | Evidence Citation
  Minimum rows: 1

TABLE E — Headcount Signals
  Required columns: Signal Source | Headcount Range | Rationale
  Minimum rows: 1  (C-03: range required, not point estimate)

TABLE F — Transport Manifest (Output Consumers)
  Required columns: Producing Role | Consuming Role | Tables Consumed | Analytical Purpose
  Minimum rows: 2
  C-64/C-67 FORM REQUIREMENT:
    Analytical Purpose cell must follow this form exactly:
    "[consuming role] — [table(s)] — [analytical purpose in consuming phase]"
    Any Analytical Purpose cell not following this form is a C-67 violation.

COVERAGE ATTESTATION
  Required columns: Source Type | Status | Notes
  Minimum rows: 7  (C-68 — gate-blocking via CONDITION 3; violation = FAIL TOKEN)
  Status vocabulary (constrained): scanned | not-found | not-applicable
  Source types declared here (GROUP A references this declaration — C-68 schema-first):
    1. CLAUDE.md files
    2. package.json / workspace configs
    3. design/ directories
    4. namespace / module directories
    5. test coverage areas
    6. SPECS.md files
    7. existing .craft/roles/ files

TABLE G — Evidence Gaps and Ambiguities
  Required columns: Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

TABLE H — Org Shape Delta
  Required columns: Dimension | Current State | Recommended State | Driving Evidence
  Minimum rows: N  (set by SYNTHESIZER pre-production assertion — C-69)
  BRIDGE RULE (C-69 — named structural constraint declared here):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any TABLE H row without a TABLE B citation is a BRIDGE RULE
     violation, detectable by table correspondence alone."
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: complete before GROUP B; C-11: anti-fabrication per
evidence-dependent row; C-13: C-05 stated in preamble and again in GROUP B)`

**HARD BOUNDARY (C-05)**: RAW ANALYSIS ONLY. No org chart. No .craft/roles/ files.

**Anti-fabrication (C-11)**: Do not invent file paths, area names, or inertia patterns.
If a source type yields no evidence, record `not-found` in COVERAGE ATTESTATION. Do not
add TABLE B rows for areas where no evidence exists.

Scan source types declared in COVERAGE ATTESTATION schema in PREAMBLE (not restated here
per C-68 schema-first reference pattern).

#### TABLE B

`(Inertia Match before File Path Evidence per SCHEMA DECLARATIONS; C-25; all columns required)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01] | [source type from PREAMBLE] | [INR-NN] | [specific/path/file.ext] | [hedging sentence — C-11] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

Dominant inertia pattern: [INR-NN] — [one sentence justification]

#### TABLE C

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [boundary note] | [specific/path] |

#### TABLE D

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [seam rationale] | [specific/path] |

#### TABLE E

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [N to N] | [one sentence] |

#### COVERAGE ATTESTATION

`(C-65/C-68: 7 rows; status from PREAMBLE schema; source types from PREAMBLE — not restated)`

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned/not-found/not-applicable] | [notes] |
| package.json / workspace configs | [scanned/not-found/not-applicable] | [notes] |
| design/ directories | [scanned/not-found/not-applicable] | [notes] |
| namespace / module directories | [scanned/not-found/not-applicable] | [notes] |
| test coverage areas | [scanned/not-found/not-applicable] | [notes] |
| SPECS.md files | [scanned/not-found/not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned/not-found/not-applicable] | [notes] |

#### TABLE G

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(C-64/C-67: Analytical Purpose form declared in PREAMBLE schema; apply it here)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | GROUP B / SYNTHESIZER — TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION — SYNTHESIZER uses TABLE B as the citation pool for TABLE H Driving Evidence cells (BRIDGE RULE declared in PREAMBLE); derives cross-cutting concern dimension recommendations from TABLE C; derives boundary Recommended State from TABLE D; sets Headcount Distribution dimension from TABLE E headcount range; acknowledges TABLE G gaps in evidence section; uses COVERAGE ATTESTATION status values to bound recommendation confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build — TABLE H — org-build reads TABLE H row by row at construction time: Dimension drives which org aspect to configure; Current State establishes the departure baseline; Recommended State specifies the target; Driving Evidence TABLE B citations provide scan provenance that org-build surfaces in construction review before committing any structural change |

---

**SCAN GATE**

```
SCAN GATE VERIFICATION CHECKLIST (C-14: numbered items + confirmation sentence; C-17: named token;
C-18: named fail string; C-22: postcondition of GROUP A; precondition of GROUP B)

[1] TABLE B rows: [N] — CONDITION 1 requires 5+:  [MET / NOT MET]
[2] Distinct source types in TABLE B: [N] — CONDITION 2 requires 3+: [MET / NOT MET]
[3] COVERAGE ATTESTATION rows: [N] — CONDITION 3 requires exactly 7: [MET / NOT MET]
[4] TABLE B Inertia Match values all in INR-01..INR-06 (C-23): [MET / NOT MET]
[5] Inertia Match column before File Path Evidence (C-25): [MET / NOT MET]
[6] All TABLE B rows have Anti-Fabrication Note (C-11): [MET / NOT MET]
[7] TABLE F Analytical Purpose present on all rows with correct form (C-67): [MET / NOT MET]
[8] No org chart, reporting lines, role files anywhere in GROUP A (C-05): [MET / NOT MET]

All [MET] — write PASS TOKEN from GATE TOKEN PROTOCOL:
  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"

Any [NOT MET] — write FAIL TOKEN from GATE TOKEN PROTOCOL (C-18):
  "SCAN GATE FAIL — condition [N]: [specific reason]"
```

*Required confirmation sentence (C-14/C-17): "GROUP A complete. GROUP B / SYNTHESIZER
may begin only if the SCAN GATE PASS TOKEN is the final output line of GROUP A."*

```
GROUP A PHASE OUTPUTS
  TABLE B rows produced: [N]  (CONDITION 1 floor = 5; status: [MET/NOT MET])
  Distinct source types in TABLE B: [N]  (CONDITION 2 floor = 3; status: [MET/NOT MET])
  COVERAGE ATTESTATION rows: [N]  (C-68 floor = 7; status: [MET/NOT MET])
  TABLE G rows: [N]
  TABLE F rows: [N]; Analytical Purpose form (C-67) on all rows: [YES/NO]
  Dominant inertia pattern: [INR-NN]
  Gate token written: [PASS TOKEN verbatim / FAIL TOKEN verbatim]
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: PASS TOKEN required before starting; C-10: current vs
recommended clearly separated; C-07: named org shape; C-69: pre-production assertion)`

**Precondition**: Final GROUP A output line must be PASS TOKEN. If FAIL TOKEN: write it
verbatim and stop. Produce no further output.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy. No role files. Named recommendations are acceptable;
drawn structure is not.

**BRIDGE RULE** (from PREAMBLE SCHEMA DECLARATIONS — TABLE H): Every TABLE H Driving Evidence
cell must contain at least one `(cite TABLE B row)` annotation.

#### Org Shape Assessment (C-07/C-03)

Dominant pattern identified in GROUP A: [INR-NN]. Named org shape: [shape type].
Justification: [two to three sentences citing TABLE B rows by Area. Reference TABLE E range.]

#### TABLE H — Org Shape Delta

**Pre-production assertion (C-69 — write before the table)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE check point (C-69): every Driving Evidence cell below must cite at least one
TABLE B row by Area value. No exceptions.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended — C-10] | (cite TABLE B row: [Area]) [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) [sentence] |
| Headcount distribution | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) [sentence] |

#### Current State vs Recommended State Summary (C-10)

**Current state**: [synthesised from TABLE B dominant pattern, TABLE C, TABLE D. No invention.
Cite evidence.]

**Recommended state**: [named shape adjustment referencing TABLE H dimensions. Raw analysis
only. No org chart.]

#### Evidence Gaps (C-08 — TABLE G)

[One sentence per TABLE G row: gap name, impact on recommendation confidence.]

```
GROUP B PHASE OUTPUTS
  TABLE H rows produced: [N]  (pre-production assertion: "Dimension count: [N]"; match: [YES/NO])
  BRIDGE RULE compliance (all Driving Evidence cells cite TABLE B): [YES/NO]
  Org shape named: [INR-NN / named type]
  Current vs Recommended clearly separated as named columns: YES (C-10)
  Evidence gaps acknowledged: [N] rows from TABLE G
  Raw analysis only — no org chart, no reporting lines: CONFIRMED (C-05 second statement)
```

---

> "org-scan complete (R19 V-05 — Combination: Phase Footer PHASE OUTPUTS + Maximum Preamble
> Density). PREAMBLE declares: GATE TOKEN PROTOCOL (C-20/C-22), INERTIA PATTERN DICTIONARY
> INR-01..INR-06 (C-23/C-25), SCHEMA DECLARATIONS for all 8 tables including TABLE F with
> C-67 Analytical Purpose form requirement ('any cell not following this form is a C-67
> violation'), COVERAGE ATTESTATION with Minimum rows: 7 gate-blocking (C-68), BRIDGE RULE for
> TABLE H (C-69). GROUP A PHASE OUTPUTS footer confirms: TABLE B [N] rows, COVERAGE
> ATTESTATION [N]=7 rows, TABLE F purpose form on all rows [YES/NO]. GROUP B PHASE OUTPUTS
> footer confirms: TABLE H [N] rows vs assertion [N] (C-69 match), BRIDGE RULE compliance
> [YES/NO]. Dual verification paths: preamble declares + footer confirms for all three new
> criteria. C-05 stated twice: preamble OUTPUT CONSTRAINT + GROUP B OUTPUT FORMAT CONSTRAINT.
> Raw analysis only."
