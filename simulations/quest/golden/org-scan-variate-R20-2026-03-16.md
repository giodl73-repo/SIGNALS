---
skill: quest-variate
skill_target: org-scan
round: 20
date: 2026-03-16
rubric_version: 20
---

# Variate R20 — org-scan

5 complete prompt body variations for the `org-scan` skill, targeting the v20 rubric (C-01
through C-73). All prior invariants through C-69 are treated as structural requirements that
every variation must satisfy. C-70, C-71, C-72, and C-73 are the four new criteria this round.

New criteria this round:

- **C-70** — Transport manifest gate-blocking enforcement: TABLE F Analytical Purpose compliance
  is enforced as a named gate checklist item (e.g., "TABLE F Output Consumers: Analytical Purpose
  annotation present on all rows (C-67/C-70): [MET / NOT MET]"), making transport manifest
  completeness gate-blocking rather than structurally detectable from schema only. Any TABLE F
  entry lacking a purpose annotation produces a named gate failure string rather than requiring
  schema comparison to detect. Extends C-67 from schema detectability to execution-time gate
  enforcement.

- **C-71** — Phase footer compliance status tokens: each PHASE OUTPUTS footer block carries named
  `MET/NOT MET` compliance tokens for every floor-constrained criterion active in that phase
  (e.g., "COVERAGE ATTESTATION rows: [N] (floor=7; status: MET/NOT MET)", "TABLE H rows: [N]
  (assertion: N; match: YES/NO)", "BRIDGE RULE compliance: YES/NO"), creating a second
  independent verification path for gate-adjacent constraints without requiring re-reading gate
  checklist items. Extends C-37's phase footer pattern to carry per-criterion compliance verdicts
  as named status assertions. Any floor-constrained criterion absent from the footer is a
  structurally detectable omission by comparison against the declared floor list.

- **C-72** — Schema-first reference pattern named as convention: procedural phase instructions
  carry explicit schema-first reference annotations in the form "[data type] declared in [SCHEMA
  NAME] (see PREAMBLE SCHEMA DECLARATIONS — [list] not restated here per schema-first reference
  pattern)", making the schema-first reference pattern a named convention that phase instructions
  invoke by name. Extends C-68's schema-first reference requirement to a generalized named
  convention. Any phase instruction that re-enumerates a value set already declared in SCHEMA
  DECLARATION is a structurally detectable violation of the named convention.

- **C-73** — Complete preamble declarative coverage before first group: all structured declarations
  — every schema, GATE TOKEN PROTOCOL, INERTIA PATTERN DICTIONARY, BRIDGE RULE, and any other
  named constraints — are declared in the preamble before any GROUP or phase procedural content
  begins. The count of declared structures (N schemas + named protocols) serves as a
  self-documenting manifest of all structural obligations. Any constraint referenced in a phase
  instruction but absent from the preamble is a structurally detectable omission by comparison
  against the preamble declaration count.

Variation axes explored this round:

1. **Lifecycle emphasis** (V-01) — C-73 complete preamble as self-documenting manifest with
   explicit declaration count. Tests whether a manifest count at the top of the preamble makes
   absent declarations maximally detectable without reading phase bodies.

2. **Output format** (V-02) — C-71 phase footer compliance status tokens: every PHASE OUTPUTS
   block carries named MET/NOT MET tokens for every floor-constrained criterion. Tests whether
   footer status tokens create the strongest independent second verification path for all four
   new criteria simultaneously.

3. **Phrasing register** (V-03) — C-72 schema-first reference pattern named as convention:
   every phase instruction that references a declared schema carries an explicit named-convention
   annotation. Tests whether invoking the convention by name in every reference site eliminates
   re-enumeration and strengthens structural detectability of violations.

4. **Role sequence** (V-04) — C-70 TABLE F gate-blocking enforcement: TABLE F Analytical Purpose
   compliance added as named gate checklist item [8] with a defined named failure string. Tests
   whether gate-blocking on transport manifest completeness is the highest-leverage single-axis
   change in R20.

5. **Combination** (V-05) — C-70 + C-71 + C-72 + C-73 together. Tests whether combining all
   four new criteria in one variation yields the highest structural verifiability score, with
   preamble manifest declaring what will exist, named convention annotations in phase instructions
   referencing preamble declarations, footer compliance tokens confirming what was produced, and
   TABLE F gate-blocking enforcing transport manifest completeness at gate time.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis — C-73 complete preamble with declaration count manifest | V-01 |
| Output format — C-71 phase footer MET/NOT MET compliance status tokens | V-02 |
| Phrasing register — C-72 schema-first reference pattern named as convention throughout | V-03 |
| Role sequence — C-70 TABLE F gate-blocking as named gate checklist item [8] | V-04 |
| Combination — C-70 + C-71 + C-72 + C-73 | V-05 |

---

## V-01 — Lifecycle Emphasis: C-73 Complete Preamble as Self-Documenting Manifest

**Axis**: Lifecycle emphasis
**Hypothesis**: R19's strongest variation (V-05) concentrates declarations in the preamble but
does not publish a declaration count. C-73 requires that the count of declared structures (N
schemas + named protocols) serves as a self-documenting manifest so that any constraint
referenced in a phase instruction but absent from the preamble is structurally detectable by
comparison against the manifest count. Adding a PREAMBLE DECLARATION MANIFEST block at the
top of the preamble with an explicit total count makes structural omissions detectable from
the manifest alone — a scorer can count preamble declarations and compare to the manifest
total without reading phase bodies. Hypothesis: C-73 compliance at its highest verifiability
with no other new criteria targeted, establishing a clean baseline for V-02 through V-05.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md,
package.json, design/ directories, namespaces, test coverage areas, SPECS.md files, existing
.craft/roles/. Produce a structured analysis: areas of work, team boundaries, cross-cutting
concerns, headcount signals, and recommended org shape. Output is raw analysis only — not an
org chart, not reporting lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — stated here and again in GROUP B output format section)**:
This skill produces RAW ANALYSIS ONLY. No org chart. No reporting lines. No hierarchy diagram.
No role file creation. Violation of this constraint is a critical failure regardless of other
scores.

---

### PREAMBLE DECLARATIONS

`(C-73: all structured declarations before GROUP A begins; declaration count below serves as
self-documenting manifest — any constraint referenced in GROUP A or GROUP B but absent from
this preamble is a C-73 violation detectable by comparison against the manifest count)`

---

#### PREAMBLE DECLARATION MANIFEST

```
PREAMBLE DECLARATION MANIFEST — org-scan
(C-73: count of declared structures serves as self-documenting manifest;
 any constraint referenced in GROUP A or GROUP B instructions but absent
 from this manifest is a C-73 violation detectable by count comparison)

Declared in this preamble (10 total):
  Named protocols (2):
    1.  GATE TOKEN PROTOCOL
    2.  INERTIA PATTERN DICTIONARY
  Schema declarations (8):
    3.  TABLE B — Scan Evidence Table
    4.  TABLE C — Cross-Cutting Concerns
    5.  TABLE D — Team Boundary Candidates
    6.  TABLE E — Headcount Signals
    7.  TABLE F — Transport Manifest (Output Consumers)
    8.  COVERAGE ATTESTATION
    9.  TABLE G — Evidence Gaps and Ambiguities
    10. TABLE H — Org Shape Delta (includes BRIDGE RULE)

Total declared structures: 10
Any GROUP A or GROUP B instruction that references a constraint not in this
list is a C-73 violation. Any constraint in this list not declared below is
a C-73 omission detectable from the manifest count alone.
```

---

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan
(C-20: pass and fail tokens defined as named constants before GROUP A begins)
(C-22: gate is postcondition of GROUP A / SCANNER and precondition of GROUP B / SYNTHESIZER)

SCAN GATE:
  PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN label]"
  FAIL TOKEN: "SCAN GATE FAIL — item [N]: [reason: source count / path floor /
               attestation row count below floor]"

  Postcondition of GROUP A: SCANNER writes one of the above tokens as its final output line.
  Precondition of GROUP B: reads token. FAIL TOKEN = halt, write token verbatim, stop.

  Gate-blocking items (any one unmet causes FAIL TOKEN):
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ specific file paths in TABLE B (C-09/C-16)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68 schema minimum rows requirement)
```

---

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan
(C-23: enumerated valid values with labels; C-25: Inertia Match before File Path Evidence)

INR-01  Org-by-function     Teams aligned to function (eng, design, QA)
INR-02  Org-by-product      Teams aligned to product area or feature surface
INR-03  Org-by-layer        Teams aligned to technical layer (frontend, backend, infra)
INR-04  Org-by-domain       Teams aligned to business domain / bounded context
INR-05  Org-by-geography    Teams aligned to region or timezone
INR-06  Org-by-customer     Teams aligned to customer segment or vertical

Rules: Inertia Match column in TABLE B must use only INR-01..INR-06.
Free-text in Inertia Match is a structurally detectable violation.
Column order enforced: Inertia Match (C-25) BEFORE File Path Evidence.
```

---

#### SCHEMA DECLARATIONS

`(C-21: evidence columns declared required; C-61: Minimum rows annotations; C-68: COVERAGE
ATTESTATION first-class schema entry with Minimum rows: 7 gate-blocking; C-69: BRIDGE RULE
in TABLE H schema; C-67: Analytical Purpose in TABLE F schema; C-73: all 8 schemas declared
here — count verifiable from manifest above)`

```
SCHEMA DECLARATION: TABLE B — Scan Evidence Table
  Columns (all required):
    Area                  (C-01: traceable to scan evidence, not invented)
    Source Type           (C-02: one of 7 enumerated source types)
    Inertia Match         (C-19/C-25: constrained to INR-01..INR-06; BEFORE File Path Evidence)
    File Path Evidence    (C-09/C-16/C-21: specific path, not generic phrase)
    Anti-Fabrication Note (C-11: required hedging sentence per row)
  Minimum rows: 5  (C-16: path floor gate condition)

SCHEMA DECLARATION: TABLE C — Cross-Cutting Concerns
  Columns (all required):
    Concern Name    (C-04: named concern)
    Boundary Note   (C-04: which teams share and where it crosses)
    Evidence Path   (C-09: supporting file path)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE D — Team Boundary Candidates
  Columns (all required):
    Boundary Candidate  (C-06: candidate team name)
    Seam Rationale      (C-06: why this is a natural boundary)
    Evidence Citation   (C-09: supporting file path)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE E — Headcount Signals
  Columns (all required):
    Signal Source      (C-03: evidence source)
    Headcount Range    (C-03: low-N to high-N, not a point estimate)
    Rationale          (C-03: one sentence supporting the range)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE F — Transport Manifest (Output Consumers)
  (C-64/C-67: per-edge purpose annotation required;
   form: [consuming role] — [table(s)] — [analytical purpose in consuming phase];
   any entry lacking Analytical Purpose is a structurally detectable C-67 omission)
  Columns (all required):
    Producing Role      (this role / group)
    Consuming Role      (downstream role that reads output)
    Tables Consumed     (specific table names)
    Analytical Purpose  (C-67: what the consuming role does with these tables in its phase)
  Minimum rows: 2

SCHEMA DECLARATION: COVERAGE ATTESTATION
  (C-65/C-68: first-class schema entry; Minimum rows: 7 is gate-blocking;
   status values constrained to: scanned / not-found / not-applicable;
   source types declared here — GROUP A instructions reference this declaration,
   not restate the enumeration inline)
  Columns (all required):
    Source Type   (one of the 7 org-scan source types declared below)
    Status        (constrained: scanned / not-found / not-applicable)
    Notes         (structural reason if not-applicable; evidence gap note if not-found)
  Source types (declared once here; referenced by GROUP A, not restated):
    1. CLAUDE.md files
    2. package.json / workspace configs
    3. design/ directories
    4. namespace / module directories
    5. test coverage areas
    6. SPECS.md files
    7. existing .craft/roles/ files
  Minimum rows: 7  (C-68: gate-blocking — SCAN GATE fails if COVERAGE ATTESTATION < 7 rows)

SCHEMA DECLARATION: TABLE G — Evidence Gaps and Ambiguities
  Columns (all required):
    Gap / Ambiguity       (C-08: named finding)
    Impact                (C-08: what analysis is limited)
    Recommended Follow-Up (C-08: one action to resolve)
  Minimum rows: 1

SCHEMA DECLARATION: TABLE H — Org Shape Delta
  (C-66/C-69: four required columns; BRIDGE RULE is a named constraint declared here)
  Columns (all required):
    Dimension         (org shape dimension being analysed)
    Current State     (C-10: what repo evidence shows today)
    Recommended State (C-10: what the analysis recommends)
    Driving Evidence  (C-66/C-69: must contain at least one "(cite TABLE B row)" annotation)
  Minimum rows: N  (set by SYNTHESIZER pre-production assertion before TABLE H — see GROUP B)

  BRIDGE RULE (C-69 named constraint — declared here in preamble, active in GROUP B):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any TABLE H row lacking a TABLE B citation is a BRIDGE RULE
     violation detectable by table correspondence alone."
```

`Preamble complete. 10 declared structures above (2 named protocols + 8 schemas). GROUP A
and GROUP B reference these declarations; they do not re-declare them inline.`

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before synthesis; C-22: GROUP A completion
is postcondition enabling SCAN GATE token; C-11: anti-fabrication per evidence-dependent section;
C-73: all constraints used below are declared in preamble — no inline re-declaration)`

**HARD BOUNDARY (C-05 / C-13)**: This skill produces RAW ANALYSIS ONLY. No org chart, no
reporting lines, no hierarchy, no .craft/roles/ file creation. Applies to every section in
GROUP A and GROUP B.

**Anti-fabrication rule (C-11)**: Each TABLE B row requires an Anti-Fabrication Note. Do not
invent file paths, area names, or inertia patterns. Only report what the scan finds.

Walk the repo. Scan the source types declared in COVERAGE ATTESTATION schema (see PREAMBLE
SCHEMA DECLARATIONS — source type list not restated here; enumeration is declaration #8 in
PREAMBLE DECLARATION MANIFEST).

#### TABLE B — Scan Evidence Table

`(schemas declared in preamble — declaration #3; column order: Inertia Match before File Path
Evidence per C-25; all columns required per C-21)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01: from scan evidence] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence — C-11] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

*Minimum 5 rows (path floor gate — declaration #3 in manifest). Fewer than 5 triggers FAIL
TOKEN at SCAN GATE. Placeholder rows permitted with Anti-Fabrication Note: "No evidence."*

Dominant inertia pattern: [INR-NN label] — [one sentence justifying dominance]

#### TABLE C — Cross-Cutting Concerns

`(schema declared in preamble — declaration #4)`

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [which teams share; where it crosses] | [specific/path] |

#### TABLE D — Team Boundary Candidates

`(schema declared in preamble — declaration #5)`

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [why natural seam] | [specific/path] |

#### TABLE E — Headcount Signals

`(schema declared in preamble — declaration #6)`

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

`(schema declared in preamble — declaration #8; Minimum rows: 7 gate-blocking per C-68;
status values constrained per schema declaration; source types referenced from preamble,
not restated here)`

| Source Type | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md files | [scanned / not-found / not-applicable] | [notes] |
| package.json / workspace configs | [scanned / not-found / not-applicable] | [notes] |
| design/ directories | [scanned / not-found / not-applicable] | [notes] |
| namespace / module directories | [scanned / not-found / not-applicable] | [notes] |
| test coverage areas | [scanned / not-found / not-applicable] | [notes] |
| SPECS.md files | [scanned / not-found / not-applicable] | [notes] |
| existing .craft/roles/ files | [scanned / not-found / not-applicable] | [notes] |

*Row count must equal 7. SCAN GATE fails if row count < 7 (C-68 gate-blocking per declaration #8).*

#### TABLE G — Evidence Gaps and Ambiguities

`(schema declared in preamble — declaration #9)`

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [what analysis is limited] | [one action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(schema declared in preamble — declaration #7; C-64/C-67: per-edge purpose annotation
required; form: consuming role — table(s) — analytical purpose in consuming phase)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE (declaration #10); uses TABLE C for cross-cutting synthesis; uses TABLE D boundary candidates for recommended state; uses TABLE E headcount range for dimension analysis; uses TABLE G to bound recommendation confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H Org Shape Delta rows to configure target org structure; Current State column establishes the baseline org-build departs from; Recommended State drives target configuration at each dimension |

---

**SCAN GATE CHECK**

`(C-12/C-16/C-17/C-18/C-22/C-68: gate is GROUP A postcondition / GROUP B precondition;
PASS and FAIL tokens defined in GATE TOKEN PROTOCOL — declaration #1 in manifest;
C-73: all gate-blocking conditions traceable to preamble declarations)`

```
SCAN GATE VERIFICATION CHECKLIST
(C-14: numbered items + required confirmation sentence)

[1] Source types scanned: [N] of 7 — must be 3+ to pass (C-02; COVERAGE ATTESTATION: decl. #8)
[2] File paths in TABLE B: [N] — must be 5+ to pass (C-09/C-16; TABLE B schema: decl. #3)
[3] COVERAGE ATTESTATION rows: [N] — must equal exactly 7 (C-68; decl. #8: Minimum rows: 7)
[4] TABLE B Inertia Match values: all INR-01..INR-06 (C-23; INERTIA PATTERN DICTIONARY: decl. #2)
[5] Inertia Match column before File Path Evidence in TABLE B (C-25; decl. #2 column-order rule)
[6] All TABLE B rows have Anti-Fabrication Note (C-11; decl. #3 required column)
[7] No org chart, reporting lines, or .craft/roles/ content (C-05; OUTPUT CONSTRAINT above)

Write PASS TOKEN if all 7 items pass (tokens from GATE TOKEN PROTOCOL — decl. #1):
  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN label]"

Write FAIL TOKEN if any item fails (tokens from GATE TOKEN PROTOCOL — decl. #1):
  "SCAN GATE FAIL — item [N]: [reason]"
  STOP. GROUP B / SYNTHESIZER may not begin.
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may begin only if the
SCAN GATE PASS TOKEN above is present as the final output line of GROUP A."*

```
GROUP A PHASE OUTPUTS (C-37: footer declaration)
  TABLE B rows produced:          [N]
  TABLE C rows produced:          [N]
  TABLE D rows produced:          [N]
  TABLE E rows produced:          [N]
  COVERAGE ATTESTATION rows:      [N]  (schema decl. #8; Minimum rows: 7; status: [MET/NOT MET])
  TABLE G rows produced:          [N]
  TABLE F rows produced:          [N]
  Gate token written:             [SCAN GATE CLEAR / SCAN GATE FAIL — verbatim]
  Dominant inertia pattern:       [INR-NN]
  File paths cited in TABLE B:    [N]  (gate floor = 5; status: [MET/NOT MET])
  Preamble declarations verified: 10 (manifest count matches declared structures: YES/NO)
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: begins only on SCAN GATE PASS TOKEN; C-10: current vs
recommended clearly separated; C-07: org shape named and justified; C-73: all constraints
used below declared in preamble — no inline re-declaration)`

**Precondition (C-22)**: Read GROUP A final output line. If FAIL TOKEN, write it verbatim and halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy diagram. Named recommendations only — no drawn structure.

#### Org Shape Assessment

`(C-07: named from findings; C-03: headcount from TABLE E)`

Dominant pattern from GROUP A: [INR-NN — named shape].

Org shape inferred: [named shape type]. Justification: [two to three sentences citing specific
TABLE B rows by Area value and the dominant INR-NN pattern. Reference TABLE E headcount range.]

#### TABLE H — Org Shape Delta

`(schema declared in preamble — declaration #10; C-66/C-69: BRIDGE RULE active;
C-10: Current State / Recommended State separated as named columns)`

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE active (C-69; declared in preamble declaration #10): every Driving Evidence cell
must contain at least one `(cite TABLE B row)` annotation. No exceptions.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended — C-10] | (cite TABLE B row: [Area]) — [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Headcount distribution model | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |

*Post-production check: TABLE H rows = [N]. Matches assertion: [YES/NO].
BRIDGE RULE compliance — all rows have TABLE B citation: [YES/NO].*

#### Current State vs Recommended State Summary

**Current state (C-10)**: [Three to five sentences synthesising what the scan evidence shows.
Grounded in TABLE B dominant INR-NN pattern, TABLE C cross-cutting concerns, TABLE D boundaries.
No invention.]

**Recommended state (C-10)**: [Three to five sentences describing the recommended org shape
adjustment. Named shape type. Reference TABLE H dimensions. Raw analysis only — no org chart.]

#### Evidence Gaps Acknowledged

`(C-08: references TABLE G — gaps declared in preamble declaration #9)`

[One sentence per TABLE G row: acknowledge gap, state impact on recommendation confidence.]

```
GROUP B PHASE OUTPUTS (C-37: footer declaration)
  TABLE H rows produced:             [N]  (assertion: [N]; match: [YES/NO])
  BRIDGE RULE compliance:            [YES/NO]  (any row without TABLE B citation: NO)
  Org shape named:                   [INR-NN / named shape type]
  Current vs Recommended separated:  YES (C-10; TABLE H columns per decl. #10)
  Evidence gaps acknowledged:        [N] from TABLE G (decl. #9)
  Raw analysis only — no org chart:  CONFIRMED (C-05 — stated twice)
  Preamble declaration count used:   10 (all 10 preamble declarations referenced in this output)
```

---

> "org-scan complete (R20 V-01 — Lifecycle Emphasis: C-73 complete preamble as self-documenting
> manifest). PREAMBLE DECLARATION MANIFEST published at preamble top: 10 declared structures
> (2 named protocols + 8 schemas). Any constraint referenced in GROUP A or GROUP B but absent
> from manifest count is a C-73 violation detectable by comparison. All schema and protocol
> declarations precede GROUP A. GROUP A and GROUP B reference declarations by number — no
> inline re-declaration. C-05 stated twice. BRIDGE RULE in TABLE H preamble declaration #10.
> COVERAGE ATTESTATION Minimum rows: 7 gate-blocking (declaration #8). TABLE F per-edge
> Analytical Purpose (C-67, declaration #7). Raw analysis only."

---

## V-02 — Output Format: C-71 Phase Footer Compliance Status Tokens

**Axis**: Output format
**Hypothesis**: R19 V-02 and V-05 introduced PHASE OUTPUTS footer blocks that declare row
counts and a MET/NOT MET status for C-68 (attestation floor) and a YES/NO for C-69 (TABLE H
match). C-71 formalises this pattern: every PHASE OUTPUTS block must carry named `MET/NOT MET`
compliance tokens for *every* floor-constrained criterion active in that phase — not just
C-68 and C-69, but also C-02 (source floor), C-16 (path floor), C-67/C-70 (TABLE F Analytical
Purpose), and BRIDGE RULE. This creates a second independent verification path for all
floor-constrained criteria simultaneously, and makes any floor-constrained criterion absent
from the footer a structurally detectable omission by comparison against the declared floor
list. Hypothesis: C-71 compliance at its highest structural verifiability as the single
new-criteria axis, with partial C-70 coverage via footer (but TABLE F not yet gate-blocking).

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md,
package.json, design/ directories, namespaces, test coverage areas, SPECS.md files, existing
.craft/roles/. Produce a structured analysis: areas of work, team boundaries, cross-cutting
concerns, headcount signals, and recommended org shape. Output is raw analysis only — not an
org chart, not reporting lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — first statement)**: RAW ANALYSIS ONLY. No org chart. No reporting
lines. No .craft/roles/ creation. No hierarchy. Violation is a critical failure.

---

### PREAMBLE

`(C-20: GATE TOKEN PROTOCOL; C-23: INERTIA PATTERN DICTIONARY; SCHEMA DECLARATIONS with C-68
Minimum rows annotations; C-69 BRIDGE RULE; all declared before GROUP A)`

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan (C-20)
(C-22: gate is postcondition of GROUP A and precondition of GROUP B)

SCAN GATE:
  PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"
  FAIL TOKEN: "SCAN GATE FAIL — item [N]: [reason: source count / path floor / attestation
               row count below floor]"

  Gate-blocking conditions (any one unmet causes FAIL TOKEN):
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ file paths in TABLE B (C-09/C-16)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68)
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

Free-text in Inertia Match is a structurally detectable violation.
```

#### SCHEMA DECLARATIONS

```
TABLE B — Scan Evidence Table
  Columns (required): Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note
  Minimum rows: 5  (C-16/C-61; path floor gate condition)
  Inertia Match: constrained to INR-01..INR-06 (C-23); before File Path Evidence (C-25)

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
  (C-64/C-67: per-edge purpose annotation required;
   form: [consuming role] — [table(s)] — [analytical purpose in consuming phase];
   any entry lacking Analytical Purpose is a structurally detectable C-67 omission)
  Columns (required): Producing Role | Consuming Role | Tables Consumed | Analytical Purpose
  Minimum rows: 2

COVERAGE ATTESTATION
  (C-65/C-68: first-class schema entry; Minimum rows: 7 gate-blocking;
   status constrained: scanned / not-found / not-applicable;
   GROUP A instructions reference "source types declared in COVERAGE ATTESTATION schema"
   — enumeration not restated inline)
  Columns (required): Source Type | Status | Notes
  Source types declared (7 total):
    1. CLAUDE.md files          4. namespace / module directories
    2. package.json / workspace configs   5. test coverage areas
    3. design/ directories      6. SPECS.md files
    7. existing .craft/roles/ files
  Minimum rows: 7  (C-68: gate-blocking)

TABLE G — Evidence Gaps and Ambiguities
  Columns (required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

TABLE H — Org Shape Delta
  (C-66/C-69: BRIDGE RULE; four required columns)
  Columns (required): Dimension | Current State | Recommended State | Driving Evidence
  BRIDGE RULE (C-69 named constraint):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in
     Driving Evidence. Any row lacking this citation is a BRIDGE RULE violation."
  Minimum rows: N  (SYNTHESIZER pre-production assertion — see GROUP B)
```

`(C-71: floor-constrained criteria declared above with their floor values; GROUP A and GROUP B
PHASE OUTPUTS footers will carry MET/NOT MET tokens for each floor-constrained criterion listed
here: TABLE B floor=5; COVERAGE ATTESTATION floor=7; source types floor=3; TABLE F floor=2;
TABLE H floor=N-assertion; BRIDGE RULE YES/NO)`

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before synthesis; C-11: anti-fabrication
per evidence-dependent section; C-13: C-05 stated in preamble and in GROUP B)`

**HARD BOUNDARY (C-05)**: RAW ANALYSIS ONLY. No org chart, no reporting lines, no role files.

**Anti-fabrication rule (C-11)**: Every TABLE B row requires an Anti-Fabrication Note.
Do not invent file paths, area names, or inertia patterns.

Walk the repo. Scan the source types declared in COVERAGE ATTESTATION schema (see SCHEMA
DECLARATIONS — source type list not restated here per C-68 schema-first reference pattern).

#### TABLE B — Scan Evidence Table

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
| [source — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

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

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE; uses TABLE C for cross-cutting synthesis; uses TABLE D boundary candidates for recommended state; uses TABLE E headcount range for dimension analysis; uses TABLE G to bound recommendation confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H Org Shape Delta rows to configure target org structure; Current State establishes baseline; Recommended State drives target configuration at each dimension |

---

**SCAN GATE**

```
SCAN GATE VERIFICATION CHECKLIST (C-14)

[1] Source types scanned: [N] of 7 — 3+ required (C-02)
[2] File paths in TABLE B: [N] — 5+ required (C-09/C-16)
[3] COVERAGE ATTESTATION rows: [N] — exactly 7 required (C-68)
[4] TABLE B Inertia Match: all INR-01..INR-06 (C-23)
[5] Inertia Match before File Path Evidence (C-25)
[6] All TABLE B rows have Anti-Fabrication Note (C-11)
[7] No org chart, reporting lines, .craft/roles/ content (C-05)

PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"
FAIL TOKEN: "SCAN GATE FAIL — item [N]: [reason]"
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may proceed only if
SCAN GATE PASS TOKEN is present as the final line of the SCAN GATE section above."*

```
GROUP A PHASE OUTPUTS
(C-71: named MET/NOT MET compliance tokens for every floor-constrained criterion active
 in GROUP A; any criterion below absent from this footer is a C-71 violation)

  Source types scanned:          [N] of 7  (floor=3; C-02 status:              MET / NOT MET)
  TABLE B rows:                  [N]       (floor=5; C-16 path floor:          MET / NOT MET)
  COVERAGE ATTESTATION rows:     [N]       (floor=7; C-68 gate-blocking:       MET / NOT MET)
  TABLE F rows:                  [N]       (floor=2; TABLE F minimum:          MET / NOT MET)
  TABLE F Analytical Purpose:              (C-67: all rows have purpose:        YES / NO)
  Inertia Match column-order:              (C-25: Inertia Match before path:    MET / NOT MET)
  Anti-Fabrication Notes:                  (C-11: all TABLE B rows covered:     MET / NOT MET)
  C-05 constraint (no chart):              (no org chart / reporting lines:     MET / NOT MET)

  Gate token written: [SCAN GATE CLEAR / SCAN GATE FAIL — verbatim]
  Dominant inertia pattern: [INR-NN]
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: begins only on SCAN GATE PASS TOKEN; C-10: current vs
recommended clearly separated; C-07: org shape named and justified)`

**Precondition (C-22)**: Read GROUP A final SCAN GATE token. If FAIL TOKEN, write verbatim, halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy. Named recommendations only.

#### Org Shape Assessment

Dominant pattern: [INR-NN — named shape]. Org shape inferred: [named type]. Justification:
[two to three sentences citing TABLE B rows by Area value and dominant INR-NN. Reference
TABLE E headcount range.]

#### TABLE H — Org Shape Delta

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE (C-69): every Driving Evidence cell must contain at least one `(cite TABLE B row)`
annotation. No exceptions.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Headcount distribution model | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |

#### Current State vs Recommended State Summary

**Current state (C-10)**: [Three to five sentences. Grounded in TABLE B, TABLE C, TABLE D.
No invention.]

**Recommended state (C-10)**: [Three to five sentences. Named shape. Reference TABLE H
dimensions. Raw analysis only — no org chart.]

#### Evidence Gaps Acknowledged

[One sentence per TABLE G row: acknowledge gap, state impact on recommendation confidence.]

```
GROUP B PHASE OUTPUTS
(C-71: named MET/NOT MET compliance tokens for every floor-constrained criterion active
 in GROUP B; any criterion below absent from this footer is a C-71 violation)

  TABLE H rows produced:             [N]  (pre-production assertion: [N]; match: YES / NO)
  BRIDGE RULE compliance:                  (all Driving Evidence cells cite TABLE B: YES / NO)
  Org shape named and justified:           (C-07: named shape type present:    MET / NOT MET)
  Current vs Recommended separated:        (C-10: distinct columns in TABLE H: MET / NOT MET)
  Evidence gaps acknowledged:        [N] from TABLE G
  C-05 constraint (raw analysis):          (no org chart produced:             MET / NOT MET)
```

---

> "org-scan complete (R20 V-02 — Output Format: C-71 phase footer compliance status tokens).
> GROUP A PHASE OUTPUTS footer carries MET/NOT MET compliance tokens for 8 floor-constrained
> criteria: source floor (C-02), path floor (C-16), attestation floor (C-68), TABLE F floor
> (minimum rows), TABLE F Analytical Purpose (C-67), column-order (C-25), anti-fabrication
> (C-11), C-05 constraint. GROUP B PHASE OUTPUTS footer carries MET/NOT MET for TABLE H
> assertion match (C-69), BRIDGE RULE compliance, org shape named (C-07), current/recommended
> separation (C-10), C-05. Any floor-constrained criterion absent from either footer is a
> C-71 violation detectable by comparison against declared floor list. C-05 stated twice.
> Raw analysis only."

---

## V-03 — Phrasing Register: C-72 Schema-First Reference Pattern Named as Convention

**Axis**: Phrasing register
**Hypothesis**: C-68's schema-first reference requirement establishes that SCANNER instructions
reference COVERAGE ATTESTATION schema rather than restating the source-type enumeration inline.
C-72 generalises this to a named convention: every phase instruction that references a schema
must carry an explicit annotation invoking the convention by name —
"[data type] declared in [SCHEMA NAME] (see PREAMBLE SCHEMA DECLARATIONS — [list] not restated
here per schema-first reference pattern)". The difference from prior rounds is the annotation
names the convention ("per schema-first reference pattern") rather than just following it
structurally. This makes violations detectable by presence/absence of the convention name in
phase instructions: any instruction that re-enumerates a schema-declared value set is a named
violation of the convention. Hypothesis: C-72 coverage at highest verifiability as single axis,
with named-convention annotations appearing in every applicable phase instruction site.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md,
package.json, design/ directories, namespaces, test coverage areas, SPECS.md files, existing
.craft/roles/. Produce a structured analysis: areas of work, team boundaries, cross-cutting
concerns, headcount signals, and recommended org shape. Output is raw analysis only — not an
org chart, not reporting lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — first statement)**: RAW ANALYSIS ONLY. No org chart. No reporting
lines. No .craft/roles/ creation. No hierarchy. Violation is a critical failure.

---

### PREAMBLE DECLARATIONS

`(C-20: GATE TOKEN PROTOCOL; C-23: INERTIA PATTERN DICTIONARY; SCHEMA DECLARATIONS including
C-68 COVERAGE ATTESTATION and C-69 BRIDGE RULE; C-72: all value sets declared here so that
GROUP A and GROUP B instructions invoke the schema-first reference pattern by name rather than
restating enumerated values inline)`

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan (C-20)
(C-22: gate is postcondition of GROUP A and precondition of GROUP B)

SCAN GATE:
  PASS TOKEN: "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"
  FAIL TOKEN: "SCAN GATE FAIL — item [N]: [reason]"

  Gate-blocking conditions:
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ file paths in TABLE B (C-09/C-16)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68)
```

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan (C-23)
(C-72: valid Inertia Match values declared here; GROUP A TABLE B instructions reference
 "constrained values declared in INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA DECLARATIONS
 — INR-01..INR-06 not restated here per schema-first reference pattern)")

INR-01  Org-by-function     Functional silo alignment (eng, design, QA)
INR-02  Org-by-product      Product area or feature surface alignment
INR-03  Org-by-layer        Technical layer alignment (frontend, backend, infra)
INR-04  Org-by-domain       Business domain / bounded context alignment
INR-05  Org-by-geography    Region or timezone alignment
INR-06  Org-by-customer     Customer segment or vertical alignment
```

#### SCHEMA DECLARATIONS

`(C-72: schema-first reference convention — all value sets, column definitions, and floor
constraints are declared here once; any phase instruction that re-enumerates a value set
already declared in this section is a structurally detectable violation of the schema-first
reference pattern)`

```
TABLE B — Scan Evidence Table
  Columns (required): Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note
  Minimum rows: 5  (C-16/C-61)
  Inertia Match: constrained values declared in INERTIA PATTERN DICTIONARY (C-23); before
    File Path Evidence (C-25) — any GROUP A instruction restating INR-01..INR-06 inline is
    a C-72 violation of the schema-first reference pattern

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
  (C-65/C-68: first-class schema entry; Minimum rows: 7 gate-blocking;
   status values: scanned / not-found / not-applicable — constrained here;
   C-72: source type enumeration declared below; GROUP A instructions reference
   "source types declared in COVERAGE ATTESTATION schema (see PREAMBLE SCHEMA DECLARATIONS
   — source type list not restated here per schema-first reference pattern)")
  Columns (required): Source Type | Status | Notes
  Source types declared here (7 total — not restated elsewhere per C-72):
    1. CLAUDE.md files          5. test coverage areas
    2. package.json / workspace configs   6. SPECS.md files
    3. design/ directories      7. existing .craft/roles/ files
    4. namespace / module directories
  Minimum rows: 7  (C-68: gate-blocking)
  Status constrained values: scanned / not-found / not-applicable
    — any GROUP A instruction restating these three status values inline is a C-72 violation

TABLE G — Evidence Gaps and Ambiguities
  Columns (required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

TABLE H — Org Shape Delta
  (C-66/C-69: BRIDGE RULE declared here; four required columns)
  Columns (required): Dimension | Current State | Recommended State | Driving Evidence
  BRIDGE RULE (C-69 named constraint — declared here; GROUP B references by name):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any row lacking this citation is a BRIDGE RULE violation."
  Org shape dimensions (declared here for C-72; GROUP B instructions reference
    "dimensions declared in TABLE H schema (see PREAMBLE SCHEMA DECLARATIONS — dimension
     list not restated here per schema-first reference pattern)"):
    — Team alignment model
    — Cross-cutting concern ownership
    — Headcount distribution model
    — Boundary definition clarity
  Minimum rows: N  (SYNTHESIZER pre-production assertion — see GROUP B)
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before synthesis; C-11: anti-fabrication
per evidence-dependent section; C-72: every instruction below that references a schema-declared
value set invokes the schema-first reference pattern by name rather than restating values inline)`

**HARD BOUNDARY (C-05 / C-13)**: RAW ANALYSIS ONLY. No org chart, no reporting lines,
no hierarchy, no .craft/roles/ file creation. Applies to GROUP A and GROUP B.

**Anti-fabrication rule (C-11)**: Every TABLE B row requires an Anti-Fabrication Note.
Do not invent file paths, area names, or patterns.

Walk the repo. Scan the 7 source types [source types declared in COVERAGE ATTESTATION schema
(see PREAMBLE SCHEMA DECLARATIONS — source type list not restated here per schema-first
reference pattern)]. For each source type, record its status in COVERAGE ATTESTATION using
the constrained status values [status values declared in COVERAGE ATTESTATION schema
(see PREAMBLE SCHEMA DECLARATIONS — scanned/not-found/not-applicable not restated here per
schema-first reference pattern)].

#### TABLE B — Scan Evidence Table

`(column definitions declared in TABLE B schema — see PREAMBLE SCHEMA DECLARATIONS; Inertia
Match constrained values [declared in INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA
DECLARATIONS — INR-01..INR-06 not restated here per schema-first reference pattern)];
column order: Inertia Match before File Path Evidence per C-25)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01] | [source type] | [INR-NN from INERTIA PATTERN DICTIONARY] | [specific/path/file.ext] | [hedging sentence] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

Dominant inertia pattern: [INR-NN from INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA
DECLARATIONS — pattern labels not restated here per schema-first reference pattern)] —
[one sentence justifying dominance]

#### TABLE C — Cross-Cutting Concerns

`(column definitions declared in TABLE C schema — see PREAMBLE SCHEMA DECLARATIONS)`

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [boundary description] | [specific/path] |

#### TABLE D — Team Boundary Candidates

`(column definitions declared in TABLE D schema — see PREAMBLE SCHEMA DECLARATIONS)`

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [seam rationale] | [specific/path] |

#### TABLE E — Headcount Signals

`(column definitions declared in TABLE E schema — see PREAMBLE SCHEMA DECLARATIONS)`

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

`(schema declared in PREAMBLE SCHEMA DECLARATIONS; source types [declared in COVERAGE
ATTESTATION schema (see PREAMBLE SCHEMA DECLARATIONS — 7-item source type list not restated
here per schema-first reference pattern)]; status values [declared in COVERAGE ATTESTATION
schema (see PREAMBLE SCHEMA DECLARATIONS — scanned/not-found/not-applicable not restated
here per schema-first reference pattern)]; Minimum rows: 7 gate-blocking per C-68)`

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

`(column definitions declared in TABLE G schema — see PREAMBLE SCHEMA DECLARATIONS)`

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(schema declared in PREAMBLE SCHEMA DECLARATIONS; C-67: Analytical Purpose required per-edge;
form: consuming role — table(s) — analytical purpose in consuming phase)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67) |
|----------------|----------------|-----------------|---------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE [declared in TABLE H schema (see PREAMBLE SCHEMA DECLARATIONS — BRIDGE RULE not restated here per schema-first reference pattern)]; uses TABLE C for cross-cutting synthesis; uses TABLE D for boundary recommendations; uses TABLE E headcount for dimension analysis; uses TABLE G to bound confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H Org Shape Delta rows to configure target org structure; Current State establishes baseline; Recommended State drives target configuration per dimension |

---

**SCAN GATE CHECK**

```
SCAN GATE VERIFICATION CHECKLIST (C-14)

[1] Source types scanned: [N] of 7 — 3+ required (C-02)
[2] FILE paths in TABLE B: [N] — 5+ required (C-09/C-16)
[3] COVERAGE ATTESTATION rows: [N] — exactly 7 required (C-68)
[4] TABLE B Inertia Match: constrained values from INERTIA PATTERN DICTIONARY only (C-23)
[5] Inertia Match before File Path Evidence (C-25)
[6] All TABLE B rows have Anti-Fabrication Note (C-11)
[7] No org chart, reporting lines, .craft/roles/ content (C-05)

PASS TOKEN (from GATE TOKEN PROTOCOL):
  "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN]"

FAIL TOKEN (from GATE TOKEN PROTOCOL):
  "SCAN GATE FAIL — item [N]: [reason]"
  STOP.
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may begin only if
SCAN GATE PASS TOKEN is present as the final line of GROUP A output."*

```
GROUP A PHASE OUTPUTS (C-37: footer)
  TABLE B rows: [N]    TABLE C rows: [N]    TABLE D rows: [N]    TABLE E rows: [N]
  COVERAGE ATTESTATION rows: [N] (floor=7; C-68: MET/NOT MET)
  TABLE G rows: [N]    TABLE F rows: [N]    File paths cited: [N] (floor=5: MET/NOT MET)
  Schema-first reference pattern invoked: YES (all phase instructions cite schema; no
    inline re-enumeration of declared value sets)
  Gate token written: [PASS TOKEN / FAIL TOKEN — verbatim]
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: SCAN GATE PASS TOKEN required; C-10: current vs
recommended clearly separated; C-07: org shape named; C-72: all references to declared
schema value sets invoke schema-first reference pattern by name)`

**Precondition (C-22)**: Read GROUP A final line. If FAIL TOKEN, write verbatim, halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy. No role files.

#### Org Shape Assessment

`(C-07: named from findings; C-03: headcount from TABLE E)`

Dominant pattern from GROUP A: [INR-NN — named shape].

Org shape inferred: [named shape type]. Justification: [two to three sentences citing TABLE B
rows by Area value, dominant INR-NN pattern, TABLE E headcount range.]

#### TABLE H — Org Shape Delta

`(column definitions declared in TABLE H schema — see PREAMBLE SCHEMA DECLARATIONS; BRIDGE
RULE [declared in TABLE H schema (see PREAMBLE SCHEMA DECLARATIONS — BRIDGE RULE constraint
not restated here per schema-first reference pattern)]; org shape dimensions [declared in
TABLE H schema (see PREAMBLE SCHEMA DECLARATIONS — dimension list not restated here per
schema-first reference pattern)])`

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE active (declared in TABLE H schema per schema-first reference pattern; not
restated here): every Driving Evidence cell must contain `(cite TABLE B row)` annotation.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Headcount distribution model | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |

*Post-production check: TABLE H rows = [N]. Matches assertion: [YES/NO].
BRIDGE RULE compliance: [YES/NO].*

#### Current State vs Recommended State Summary

**Current state (C-10)**: [Three to five sentences. Grounded in scan evidence. No invention.]

**Recommended state (C-10)**: [Three to five sentences. Named shape. Reference TABLE H
dimensions. Raw analysis only — no org chart.]

#### Evidence Gaps Acknowledged

[One sentence per TABLE G row. Acknowledge gap, state impact on confidence.]

```
GROUP B PHASE OUTPUTS (C-37: footer)
  TABLE H rows: [N] (assertion: [N]; match: YES/NO)
  BRIDGE RULE compliance: YES/NO
  Schema-first reference pattern invoked: YES (TABLE H dimensions from schema; BRIDGE RULE
    from schema; org shape dimensions not restated inline — all reference preamble)
  Org shape named: [INR-NN / shape type]
  Current vs Recommended separated: YES (C-10)
  Evidence gaps acknowledged: [N] from TABLE G
  Raw analysis only: CONFIRMED (C-05 stated twice)
```

---

> "org-scan complete (R20 V-03 — Phrasing Register: C-72 schema-first reference pattern named
> as convention). Every phase instruction that references a schema-declared value set carries
> an explicit C-72 annotation: '[data type] declared in [SCHEMA NAME] (see PREAMBLE SCHEMA
> DECLARATIONS — [list] not restated here per schema-first reference pattern)'. Named convention
> invoked at 6 instruction sites: source types (COVERAGE ATTESTATION schema), status values
> (COVERAGE ATTESTATION schema), Inertia Match values (INERTIA PATTERN DICTIONARY), pattern
> labels (INERTIA PATTERN DICTIONARY), BRIDGE RULE (TABLE H schema), org shape dimensions
> (TABLE H schema). Any phase instruction restating a schema-declared value set inline is a
> structurally detectable C-72 violation by comparison against annotation presence. C-05 stated
> twice. Raw analysis only."

---

## V-04 — Role Sequence: C-70 TABLE F Gate-Blocking Enforcement

**Axis**: Role sequence
**Hypothesis**: R19's V-04 (imperative register) made TABLE F Analytical Purpose compliance a
gate checklist item, but C-70 formalises the requirement more precisely: the gate checklist
item must produce a *named gate failure string* when unmet — distinct from the generic SCAN
GATE FAIL token — making TABLE F compliance failures verifiable without prose inspection. The
key advance is that the gate failure string for TABLE F non-compliance is a separate named
string (e.g., "TABLE F Output Consumers: Analytical Purpose row compliance: NOT MET — row [N]
missing Analytical Purpose annotation (C-67/C-70 violation)") so it is independently
identifiable in the gate output without parsing the FAIL TOKEN reason field. The gate checklist
grows to 8 items. Hypothesis: C-70 coverage at strongest enforceability with a single-axis
change, matching or exceeding V-04's gate-blocking on TABLE F from R19 while making the failure
string more structurally precise.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md,
package.json, design/ directories, namespaces, test coverage areas, SPECS.md files, existing
.craft/roles/. Produce a structured analysis: areas of work, team boundaries, cross-cutting
concerns, headcount signals, and recommended org shape. Output is raw analysis only — not an
org chart, not reporting lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — stated here and again in GROUP B output format section)**:
RAW ANALYSIS ONLY. No org chart. No reporting lines. No hierarchy. No .craft/roles/ creation.
Violation is a critical failure.

---

### PREAMBLE DECLARATIONS

`(C-20: GATE TOKEN PROTOCOL with C-70 TABLE F failure string; C-23: INERTIA PATTERN DICTIONARY;
SCHEMA DECLARATIONS with C-68 COVERAGE ATTESTATION and C-69 BRIDGE RULE; all before GROUP A)`

#### GATE TOKEN PROTOCOL

```
GATE TOKEN PROTOCOL — org-scan (C-20)
(C-22: gate is postcondition of GROUP A and precondition of GROUP B)
(C-70: TABLE F failure string is a named constant distinct from the generic FAIL TOKEN)

SCAN GATE:
  PASS TOKEN:
    "SCAN GATE CLEAR — sources:[N] scanned, path floor:[MET], dominant:[INR-NN label]"

  FAIL TOKEN (generic — for items [1]–[7]):
    "SCAN GATE FAIL — item [N]: [reason: source count / path floor / attestation row count
     / Inertia Match violation / column order / anti-fabrication / C-05 violation]"

  TABLE F FAIL STRING (C-70: named string distinct from generic FAIL TOKEN):
    "TABLE F Output Consumers: Analytical Purpose row compliance: NOT MET —
     row [N] missing Analytical Purpose annotation (C-67/C-70 violation — gate blocked)"

  Usage:
    - If items [1]–[7] all pass but item [8] fails: write the TABLE F FAIL STRING.
    - If items [1]–[7] fail: write the generic FAIL TOKEN for the failing item.
    - If all 8 items pass: write the PASS TOKEN.
    - On any FAIL output: STOP. GROUP B / SYNTHESIZER may not begin.

  Gate-blocking conditions (all 8 required):
  [ ] 3+ source types scanned (C-02)
  [ ] 5+ file paths in TABLE B (C-09/C-16)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68)
  [ ] TABLE B Inertia Match: all INR-01..INR-06 (C-23)
  [ ] Inertia Match before File Path Evidence (C-25)
  [ ] All TABLE B rows have Anti-Fabrication Note (C-11)
  [ ] No org chart, reporting lines, .craft/roles/ content (C-05)
  [ ] TABLE F Analytical Purpose present on every row in correct form (C-67/C-70)
        Failure string: "TABLE F Output Consumers: Analytical Purpose row compliance:
        NOT MET — row [N] missing Analytical Purpose annotation (C-67/C-70 violation)"
```

---

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan (C-23)
(C-25: Inertia Match before File Path Evidence in TABLE B)

INR-01  Org-by-function     Functional silo alignment (eng, design, QA)
INR-02  Org-by-product      Product area or feature surface alignment
INR-03  Org-by-layer        Technical layer alignment (frontend, backend, infra)
INR-04  Org-by-domain       Business domain / bounded context alignment
INR-05  Org-by-geography    Region or timezone alignment
INR-06  Org-by-customer     Customer segment or vertical alignment

Free-text Inertia Match = structurally detectable violation.
```

---

#### SCHEMA DECLARATIONS

```
TABLE B — Scan Evidence Table
  Columns (required): Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note
  Minimum rows: 5  (C-16/C-61)

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
  (C-64/C-67/C-70: per-edge Analytical Purpose required; form: consuming role — table(s) —
   analytical purpose in consuming phase; any row lacking Analytical Purpose is both a C-67
   structurally detectable omission AND a C-70 gate-blocking failure — the TABLE F FAIL STRING
   is defined in GATE TOKEN PROTOCOL above)
  Columns (required): Producing Role | Consuming Role | Tables Consumed | Analytical Purpose
  Minimum rows: 2

COVERAGE ATTESTATION
  (C-65/C-68: first-class schema entry; Minimum rows: 7 gate-blocking;
   status constrained: scanned / not-found / not-applicable;
   GROUP A references "source types declared in COVERAGE ATTESTATION schema" — not restated inline)
  Columns (required): Source Type | Status | Notes
  Source types (7): CLAUDE.md files | package.json / workspace configs | design/ directories |
    namespace / module directories | test coverage areas | SPECS.md files |
    existing .craft/roles/ files
  Minimum rows: 7  (C-68: gate-blocking)

TABLE G — Evidence Gaps and Ambiguities
  Columns (required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

TABLE H — Org Shape Delta
  (C-66/C-69: BRIDGE RULE; four required columns)
  Columns (required): Dimension | Current State | Recommended State | Driving Evidence
  BRIDGE RULE (C-69): "Every TABLE H row must carry at least one (cite TABLE B row) annotation
    in its Driving Evidence cell. Any row lacking this is a BRIDGE RULE violation."
  Minimum rows: N  (SYNTHESIZER pre-production assertion)
```

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before synthesis; C-11: anti-fabrication
per evidence-dependent section; C-70: TABLE F must be complete before SCAN GATE check — any
missing Analytical Purpose produces TABLE F FAIL STRING, not generic FAIL TOKEN)`

**HARD BOUNDARY (C-05 / C-13)**: RAW ANALYSIS ONLY. No org chart, no reporting lines,
no hierarchy, no .craft/roles/ file creation. Applies throughout.

**Anti-fabrication rule (C-11)**: Every TABLE B row requires an Anti-Fabrication Note.

Walk the repo. Scan the source types declared in COVERAGE ATTESTATION schema (see SCHEMA
DECLARATIONS — enumeration not restated here per C-68 schema-first reference pattern).

#### TABLE B — Scan Evidence Table

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
| [source — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

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

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(C-67/C-70: Analytical Purpose required on every row in form: consuming role — table(s) —
analytical purpose; any missing Analytical Purpose is a C-70 gate failure — TABLE F FAIL
STRING will be written at SCAN GATE CHECK below)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67/C-70) |
|----------------|----------------|-----------------|--------------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE; uses TABLE C for cross-cutting synthesis; uses TABLE D for boundary recommendations; uses TABLE E headcount range for dimension analysis; uses TABLE G to bound confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H Org Shape Delta rows to configure target org structure; Current State establishes baseline org-build departs from; Recommended State drives target configuration per dimension |

---

**SCAN GATE CHECK** `(C-14/C-70: 8-item checklist; item [8] produces TABLE F FAIL STRING,
not generic FAIL TOKEN, if unmet — two distinct failure string types in GATE TOKEN PROTOCOL)`

```
SCAN GATE VERIFICATION CHECKLIST
(C-14: numbered items + confirmation sentence; C-70: item [8] uses named TABLE F FAIL STRING)

[1] Source types scanned: [N] of 7 — 3+ required (C-02) ............. [MET / NOT MET]
[2] File paths in TABLE B: [N] — 5+ required (C-09/C-16) ............. [MET / NOT MET]
[3] COVERAGE ATTESTATION rows: [N] — exactly 7 (C-68) ............... [MET / NOT MET]
[4] TABLE B Inertia Match: all INR-01..INR-06 (C-23) ................. [MET / NOT MET]
[5] Inertia Match before File Path Evidence (C-25) .................... [MET / NOT MET]
[6] All TABLE B rows have Anti-Fabrication Note (C-11) ................ [MET / NOT MET]
[7] No org chart, reporting lines, .craft/roles/ content (C-05) ....... [MET / NOT MET]
[8] TABLE F Analytical Purpose present on every row in correct form
    (C-67/C-70 — gate-blocking; failure uses named TABLE F FAIL STRING) [MET / NOT MET]

If ALL 8 items [MET]: write PASS TOKEN (from GATE TOKEN PROTOCOL)
If items [1]–[7] fail: write FAIL TOKEN (from GATE TOKEN PROTOCOL) — stop
If item [8] fails: write TABLE F FAIL STRING (from GATE TOKEN PROTOCOL) — stop

  TABLE F FAIL STRING format:
  "TABLE F Output Consumers: Analytical Purpose row compliance: NOT MET —
   row [N] missing Analytical Purpose annotation (C-67/C-70 violation — gate blocked)"
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may begin only if
the SCAN GATE PASS TOKEN above is present as the final line of GROUP A output."*

```
GROUP A PHASE OUTPUTS (C-37: footer)
  TABLE B rows: [N]  TABLE C rows: [N]  TABLE D rows: [N]  TABLE E rows: [N]
  COVERAGE ATTESTATION rows: [N] (floor=7; C-68: MET/NOT MET)
  TABLE G rows: [N]  TABLE F rows: [N]  File paths cited: [N] (floor=5: MET/NOT MET)
  TABLE F Analytical Purpose (C-70 gate item): all rows present in correct form: [YES/NO]
  Gate token written: [PASS TOKEN / FAIL TOKEN / TABLE F FAIL STRING — verbatim]
  Dominant inertia pattern: [INR-NN]
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: begins only on PASS TOKEN from GATE TOKEN PROTOCOL;
C-10: current vs recommended clearly separated; C-07: org shape named and justified)`

**Precondition (C-22)**: Read GROUP A final output line. If FAIL TOKEN or TABLE F FAIL STRING,
write it verbatim and halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy. Named recommendations only.

#### Org Shape Assessment

Dominant pattern from GROUP A: [INR-NN — named shape]. Org shape inferred: [named type].
Justification: [two to three sentences citing TABLE B rows by Area, INR-NN, TABLE E headcount.]

#### TABLE H — Org Shape Delta

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE (C-69): every Driving Evidence cell must cite at least one `(cite TABLE B row)`.

| Dimension | Current State | Recommended State | Driving Evidence |
|-----------|---------------|-------------------|-----------------|
| Team alignment model | [current — C-10] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Cross-cutting concern ownership | [current] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Headcount distribution model | [current from TABLE E] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |
| Boundary definition clarity | [current from TABLE D] | [recommended] | (cite TABLE B row: [Area]) — [sentence] |

*Post-production: TABLE H rows = [N]. Assertion match: [YES/NO]. BRIDGE RULE: [YES/NO].*

#### Current State vs Recommended State Summary

**Current state (C-10)**: [Three to five sentences. Evidence-grounded. No invention.]
**Recommended state (C-10)**: [Three to five sentences. Named shape. TABLE H reference. No chart.]

#### Evidence Gaps Acknowledged

[One sentence per TABLE G row: gap, impact on confidence.]

```
GROUP B PHASE OUTPUTS (C-37: footer)
  TABLE H rows: [N] (assertion: [N]; match: YES/NO)
  BRIDGE RULE compliance: YES/NO
  Org shape named: [INR-NN / shape type]
  Current vs Recommended separated: YES (C-10)
  Evidence gaps acknowledged: [N]
  Raw analysis only: CONFIRMED (C-05 stated twice)
```

---

> "org-scan complete (R20 V-04 — Role Sequence: C-70 TABLE F gate-blocking enforcement).
> GATE TOKEN PROTOCOL defines three distinct token types: PASS TOKEN, generic FAIL TOKEN
> (items [1]–[7]), and named TABLE F FAIL STRING (item [8] — C-70). Gate checklist grows
> to 8 items. TABLE F Analytical Purpose compliance is gate-blocking: any row lacking
> purpose annotation produces the TABLE F FAIL STRING rather than the generic FAIL TOKEN,
> making TABLE F non-compliance independently identifiable without parsing the FAIL TOKEN
> reason field. C-67 structural detectability (schema) + C-70 gate enforcement (named failure
> string) both active. C-05 stated twice. Raw analysis only."

---

## V-05 — Combination: C-70 + C-71 + C-72 + C-73

**Axis**: Combination — all four new criteria
**Hypothesis**: V-01 through V-04 each test one new criterion in isolation. V-05 combines all
four: C-73 preamble manifest declares what will exist (count verifiable); C-72 named convention
annotations in phase instructions reference preamble declarations by name (re-enumeration
violations detectable); C-71 footer compliance status tokens confirm what was produced (second
independent verification path); C-70 TABLE F gate-blocking with named failure string enforces
transport manifest completeness at execution time. Together, every criterion introduced in R19
(C-67/C-68/C-69) and every criterion introduced in R20 (C-70/C-71/C-72/C-73) is verifiable
from three independent locations: preamble declaration (what is required), phase instruction
convention annotation (how it is applied), and phase footer compliance token (whether it was
met). No criterion requires prose body inspection. Hypothesis: highest structural verifiability
across all 73 criteria with zero required prose inspection paths.

---

You are running `org-scan`. Walk a repo and infer the org structure. Scan: CLAUDE.md,
package.json, design/ directories, namespaces, test coverage areas, SPECS.md files, existing
.craft/roles/. Produce a structured analysis: areas of work, team boundaries, cross-cutting
concerns, headcount signals, and recommended org shape. Output is raw analysis only — not an
org chart, not reporting lines. Use org-build to turn the scan into a full org.

**OUTPUT CONSTRAINT (C-05 — stated here and again in GROUP B output format section)**:
This skill produces RAW ANALYSIS ONLY. No org chart. No reporting lines. No hierarchy diagram.
No role file creation. Violation is a critical failure regardless of other scores.

---

### PREAMBLE DECLARATIONS

`(C-73: all structured declarations before GROUP A; declaration count below is the
self-documenting manifest — any constraint referenced in GROUP A or GROUP B but absent is
a C-73 violation; C-72: all value sets declared here so phase instructions invoke
schema-first reference pattern by name; C-70: TABLE F FAIL STRING defined in GATE TOKEN
PROTOCOL; C-71: floor-constrained criteria declared here so GROUP A/B PHASE OUTPUTS footers
carry MET/NOT MET tokens for each)`

---

#### PREAMBLE DECLARATION MANIFEST

```
PREAMBLE DECLARATION MANIFEST — org-scan
(C-73: self-documenting manifest; total count is the structural completeness contract;
 any constraint referenced in GROUP A or GROUP B but absent from this list is a C-73
 violation detectable by comparison against this count)

Declared in this preamble (10 total):
  Named protocols (2):
    1.  GATE TOKEN PROTOCOL      (includes C-70 TABLE F FAIL STRING as named constant)
    2.  INERTIA PATTERN DICTIONARY   (constrained values for TABLE B Inertia Match)
  Schema declarations (8):
    3.  TABLE B — Scan Evidence Table
    4.  TABLE C — Cross-Cutting Concerns
    5.  TABLE D — Team Boundary Candidates
    6.  TABLE E — Headcount Signals
    7.  TABLE F — Transport Manifest (includes C-67 Analytical Purpose requirement)
    8.  COVERAGE ATTESTATION     (C-68: Minimum rows: 7 gate-blocking; source types declared)
    9.  TABLE G — Evidence Gaps and Ambiguities
    10. TABLE H — Org Shape Delta (includes C-69 BRIDGE RULE as named constraint)

Total: 10 declared structures (2 named protocols + 8 schemas)

Floor-constrained criteria (declared for C-71 footer compliance tokens):
  TABLE B: floor=5 rows (C-16)
  COVERAGE ATTESTATION: floor=7 rows (C-68)
  Source types scanned: floor=3 (C-02)
  TABLE F: floor=2 rows; Analytical Purpose on all rows (C-67/C-70)
  TABLE H: floor=N rows per pre-production assertion (C-69)
  BRIDGE RULE: YES/NO per TABLE H (C-69)
  C-05: YES/NO (no org chart, no reporting lines)

Any floor-constrained criterion above absent from GROUP A or GROUP B PHASE OUTPUTS
footer is a C-71 violation detectable by comparison against this declared floor list.
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

  FAIL TOKEN (for items [1]–[7]):
    "SCAN GATE FAIL — item [N]: [reason]"

  TABLE F FAIL STRING (C-70: named constant — used only for item [8]):
    "TABLE F Output Consumers: Analytical Purpose row compliance: NOT MET —
     row [N] missing Analytical Purpose annotation (C-67/C-70 violation — gate blocked)"

  Usage: PASS TOKEN if all 8 items pass. TABLE F FAIL STRING if item [8] fails.
    Generic FAIL TOKEN if items [1]–[7] fail. Any failure: STOP, GROUP B may not begin.

  Gate-blocking items (all 8 required — C-70 extends gate to 8 items):
  [ ] 3+ source types scanned (C-02; floor declared in PREAMBLE DECLARATION MANIFEST)
  [ ] 5+ file paths in TABLE B (C-09/C-16; floor declared in manifest)
  [ ] COVERAGE ATTESTATION exactly 7 rows (C-68; floor declared in manifest)
  [ ] TABLE B Inertia Match: all INR-01..INR-06 (C-23; values in INERTIA PATTERN DICTIONARY)
  [ ] Inertia Match before File Path Evidence (C-25)
  [ ] All TABLE B rows have Anti-Fabrication Note (C-11)
  [ ] No org chart, reporting lines, .craft/roles/ content (C-05)
  [ ] TABLE F Analytical Purpose present on all rows in correct form (C-67/C-70; uses
        TABLE F FAIL STRING on failure, not generic FAIL TOKEN)
```

---

#### INERTIA PATTERN DICTIONARY

```
INERTIA PATTERN DICTIONARY — org-scan (C-23; preamble declaration #2)
(C-72: valid Inertia Match values declared here once; GROUP A TABLE B instructions annotate:
 "constrained values declared in INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA DECLARATIONS
 — INR-01..INR-06 not restated here per schema-first reference pattern)";
C-25: column-order rule — Inertia Match before File Path Evidence)

INR-01  Org-by-function     Functional silo alignment (eng, design, QA)
INR-02  Org-by-product      Product area or feature surface alignment
INR-03  Org-by-layer        Technical layer alignment (frontend, backend, infra)
INR-04  Org-by-domain       Business domain / bounded context alignment
INR-05  Org-by-geography    Region or timezone alignment
INR-06  Org-by-customer     Customer segment or vertical alignment
```

---

#### SCHEMA DECLARATIONS

`(C-72: all value sets, column definitions, floor values, and named constraints declared here;
phase instructions invoke schema-first reference pattern by name — no inline re-enumeration;
C-73: 8 schemas below + 2 protocols above = 10 total per PREAMBLE DECLARATION MANIFEST)`

```
SCHEMA DECLARATION: TABLE B — Scan Evidence Table  (preamble declaration #3)
  Columns (all required):
    Area                  (C-01: traceable to scan evidence, not invented)
    Source Type           (C-02: one of 7 types declared in COVERAGE ATTESTATION schema)
    Inertia Match         (C-19/C-25: constrained to INR-01..INR-06 per INERTIA PATTERN
                           DICTIONARY; positioned before File Path Evidence)
    File Path Evidence    (C-09/C-16/C-21: specific path)
    Anti-Fabrication Note (C-11: required hedging sentence per row)
  Minimum rows: 5  (C-16/C-61: path floor gate-blocking)
  C-72 convention: GROUP A TABLE B instructions cite "column definitions declared in TABLE B
    schema (see PREAMBLE SCHEMA DECLARATIONS — columns not restated inline per schema-first
    reference pattern)"

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
  (C-64/C-67/C-70: per-edge Analytical Purpose required; any missing purpose is a C-67
   structurally detectable omission AND a C-70 gate failure — TABLE F FAIL STRING fires)
  Columns (all required):
    Producing Role      (this role / group)
    Consuming Role      (downstream consumer)
    Tables Consumed     (specific table names)
    Analytical Purpose  (C-67: what consuming role does with tables in consuming phase;
                         C-70: gate-blocking — absence produces named TABLE F FAIL STRING)
  Minimum rows: 2

SCHEMA DECLARATION: COVERAGE ATTESTATION  (preamble declaration #8)
  (C-65/C-68: first-class schema entry with floor annotation; C-72: source types and status
   values declared here — GROUP A instructions annotate "declared in COVERAGE ATTESTATION
   schema (see PREAMBLE SCHEMA DECLARATIONS — enumeration not restated here per schema-first
   reference pattern)")
  Columns (all required): Source Type | Status | Notes
  Source types (7 — declared here per C-72; GROUP A references, does not restate):
    1. CLAUDE.md files          5. test coverage areas
    2. package.json / workspace configs   6. SPECS.md files
    3. design/ directories      7. existing .craft/roles/ files
    4. namespace / module directories
  Status values (declared here per C-72; not restated in GROUP A instructions):
    scanned / not-found / not-applicable
  Minimum rows: 7  (C-68: gate-blocking — SCAN GATE fails if < 7 rows)

SCHEMA DECLARATION: TABLE G — Evidence Gaps and Ambiguities  (preamble declaration #9)
  Columns (all required): Gap / Ambiguity | Impact | Recommended Follow-Up
  Minimum rows: 1

SCHEMA DECLARATION: TABLE H — Org Shape Delta  (preamble declaration #10)
  (C-66/C-69: BRIDGE RULE is a named constraint declared here; C-72: dimension list declared
   here — GROUP B references, does not restate)
  Columns (all required):
    Dimension         (org shape dimension)
    Current State     (C-10: what repo evidence shows today)
    Recommended State (C-10: analysis recommendation)
    Driving Evidence  (C-66/C-69: must contain "(cite TABLE B row)" annotation)
  Org shape dimensions (C-72: declared here; GROUP B annotates "dimensions declared in TABLE H
    schema (see PREAMBLE SCHEMA DECLARATIONS — list not restated here per schema-first
    reference pattern)"):
    — Team alignment model
    — Cross-cutting concern ownership
    — Headcount distribution model
    — Boundary definition clarity
  Minimum rows: N  (SYNTHESIZER pre-production assertion before TABLE H)

  BRIDGE RULE (C-69 named constraint — declared here in preamble, active in GROUP B;
    GROUP B references by name, does not restate per C-72):
    "Every TABLE H row must carry at least one (cite TABLE B row) annotation in its
     Driving Evidence cell. Any row lacking this citation is a BRIDGE RULE violation
     detectable by table correspondence alone."
```

`Preamble complete. 10 declared structures (2 named protocols + 8 schemas) matching
PREAMBLE DECLARATION MANIFEST count. C-71 floor list confirmed. All GROUP A and GROUP B
instructions below reference preamble declarations — no inline re-declaration.`

---

### GROUP A — SCANNER

`(C-15: structural group label; C-12: scan completes before synthesis; C-11: anti-fabrication
per evidence-dependent section; C-72: every instruction referencing a schema-declared value
set carries named-convention annotation; C-73: all constraints used here are in preamble)`

**HARD BOUNDARY (C-05 / C-13)**: RAW ANALYSIS ONLY. No org chart, no reporting lines,
no hierarchy, no .craft/roles/ file creation. Applies to GROUP A and GROUP B.

**Anti-fabrication rule (C-11)**: Every TABLE B row requires an Anti-Fabrication Note.

Walk the repo. Scan the 7 source types [source types declared in COVERAGE ATTESTATION schema
(see PREAMBLE SCHEMA DECLARATIONS — source type list not restated here per schema-first
reference pattern; preamble declaration #8)]. For each, record status using the constrained
values [status values declared in COVERAGE ATTESTATION schema (see PREAMBLE SCHEMA
DECLARATIONS — scanned/not-found/not-applicable not restated here per schema-first reference
pattern)].

#### TABLE B — Scan Evidence Table

`(column definitions declared in TABLE B schema — preamble declaration #3; Inertia Match
constrained values [declared in INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA DECLARATIONS
— INR-01..INR-06 not restated here per schema-first reference pattern; preamble declaration #2)];
column order: Inertia Match before File Path Evidence per C-25; all columns required per C-21)`

| Area | Source Type | Inertia Match | File Path Evidence | Anti-Fabrication Note |
|------|-------------|---------------|--------------------|-----------------------|
| [area — C-01: from scan evidence] | [source type] | [INR-NN per INERTIA PATTERN DICTIONARY] | [specific/path/file.ext] | [hedging sentence — C-11] |
| [area 2] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 3] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 4] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |
| [area 5] | [source type] | [INR-NN] | [specific/path/file.ext] | [hedging sentence] |

Dominant inertia pattern: [INR-NN from INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA
DECLARATIONS — pattern labels not restated here per schema-first reference pattern)] —
[one sentence justifying dominance]

#### TABLE C — Cross-Cutting Concerns

`(column definitions declared in TABLE C schema — preamble declaration #4)`

| Concern Name | Boundary Note | Evidence Path |
|--------------|---------------|---------------|
| [concern — C-04] | [boundary description] | [specific/path] |

#### TABLE D — Team Boundary Candidates

`(column definitions declared in TABLE D schema — preamble declaration #5)`

| Boundary Candidate | Seam Rationale | Evidence Citation |
|--------------------|----------------|-------------------|
| [candidate — C-06] | [seam rationale] | [specific/path] |

#### TABLE E — Headcount Signals

`(column definitions declared in TABLE E schema — preamble declaration #6)`

| Signal Source | Headcount Range | Rationale |
|---------------|-----------------|-----------|
| [source — C-03] | [low-N to high-N] | [one sentence] |

#### COVERAGE ATTESTATION

`(schema preamble declaration #8; source types [declared in COVERAGE ATTESTATION schema
(see PREAMBLE SCHEMA DECLARATIONS — 7-item list not restated here per schema-first reference
pattern)]; status values [declared in COVERAGE ATTESTATION schema (see PREAMBLE SCHEMA
DECLARATIONS — scanned/not-found/not-applicable not restated here per schema-first reference
pattern)]; C-68: Minimum rows: 7 gate-blocking; C-71: row count appears in footer with status)`

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

`(column definitions declared in TABLE G schema — preamble declaration #9)`

| Gap / Ambiguity | Impact | Recommended Follow-Up |
|-----------------|--------|----------------------|
| [gap — C-08] | [impact] | [action] |

#### TABLE F — Transport Manifest (GROUP A Output Consumers)

`(schema preamble declaration #7; C-67/C-70: Analytical Purpose required on every row in
form: consuming role — table(s) — analytical purpose in consuming phase; missing Analytical
Purpose = TABLE F FAIL STRING at gate check; C-71: footer will carry TABLE F Analytical
Purpose compliance token)`

| Producing Role | Consuming Role | Tables Consumed | Analytical Purpose (C-67/C-70) |
|----------------|----------------|-----------------|--------------------------------|
| GROUP A / SCANNER | GROUP B / SYNTHESIZER | TABLE B, TABLE C, TABLE D, TABLE E, TABLE G, COVERAGE ATTESTATION | Synthesizer cites TABLE B rows in TABLE H Driving Evidence cells per BRIDGE RULE [declared in TABLE H schema (see PREAMBLE SCHEMA DECLARATIONS — BRIDGE RULE not restated here per schema-first reference pattern)]; uses TABLE C for cross-cutting synthesis; uses TABLE D boundary candidates for recommended state; uses TABLE E headcount for dimension analysis; uses TABLE G to bound confidence |
| GROUP B / SYNTHESIZER | org-build | TABLE H | org-build reads TABLE H Org Shape Delta rows to configure target org structure; Current State column establishes baseline; Recommended State drives target configuration at each dimension |

---

**SCAN GATE CHECK**

`(C-14/C-70: 8-item checklist; item [8] uses TABLE F FAIL STRING from GATE TOKEN PROTOCOL;
C-22: postcondition of GROUP A / precondition of GROUP B; C-73: all items traceable to
preamble declarations by number)`

```
SCAN GATE VERIFICATION CHECKLIST
(C-14: numbered items + confirmation sentence; C-70: item [8] produces TABLE F FAIL STRING)

[1] Source types scanned: [N] of 7 — 3+ required (C-02; manifest floor list) [MET/NOT MET]
[2] File paths in TABLE B: [N] — 5+ required (C-09/C-16; decl. #3 floor) .. [MET/NOT MET]
[3] COVERAGE ATTESTATION rows: [N] — exactly 7 (C-68; decl. #8 floor) ..... [MET/NOT MET]
[4] TABLE B Inertia Match: all INR-01..INR-06 (C-23; decl. #2) ............. [MET/NOT MET]
[5] Inertia Match before File Path Evidence (C-25; decl. #2) ............... [MET/NOT MET]
[6] All TABLE B rows have Anti-Fabrication Note (C-11; decl. #3) ........... [MET/NOT MET]
[7] No org chart, reporting lines, .craft/roles/ content (C-05) ............ [MET/NOT MET]
[8] TABLE F Analytical Purpose on all rows in correct form (C-67/C-70; decl. #7) [MET/NOT MET]
      On NOT MET: write TABLE F FAIL STRING — not generic FAIL TOKEN

If ALL 8 [MET]: write PASS TOKEN (from GATE TOKEN PROTOCOL — decl. #1)
If [1]–[7] fail: write FAIL TOKEN (from GATE TOKEN PROTOCOL — decl. #1)
If [8] fails: write TABLE F FAIL STRING (from GATE TOKEN PROTOCOL — decl. #1)
Any failure: STOP. GROUP B / SYNTHESIZER may not begin.
```

*Confirmation sentence (C-14): "GROUP A complete. GROUP B / SYNTHESIZER may begin only if
the SCAN GATE PASS TOKEN above is present as the final line of GROUP A output."*

```
GROUP A PHASE OUTPUTS
(C-37/C-71: footer carries named MET/NOT MET compliance tokens for every floor-constrained
 criterion declared in PREAMBLE DECLARATION MANIFEST floor list; any criterion absent from
 this footer is a C-71 violation detectable by comparison against the manifest floor list)

  Source types scanned:          [N] of 7  (floor=3; C-02:                    MET / NOT MET)
  TABLE B rows:                  [N]       (floor=5; C-16 path floor:          MET / NOT MET)
  COVERAGE ATTESTATION rows:     [N]       (floor=7; C-68 gate-blocking:       MET / NOT MET)
  TABLE F rows:                  [N]       (floor=2; TABLE F minimum:          MET / NOT MET)
  TABLE F Analytical Purpose:              (C-67/C-70: all rows correct form:  MET / NOT MET)
  Inertia Match column-order:              (C-25: before File Path Evidence:   MET / NOT MET)
  Anti-Fabrication Notes:                  (C-11: all TABLE B rows covered:    MET / NOT MET)
  C-05 constraint:                         (no org chart / reporting lines:    MET / NOT MET)
  Gate token written:            [PASS TOKEN / FAIL TOKEN / TABLE F FAIL STRING — verbatim]
  Dominant inertia pattern:      [INR-NN]
  Preamble declarations used:    10 (manifest count verified: YES/NO)
  Schema-first reference convention invoked: YES (C-72 annotations present at all
    applicable instruction sites; no inline re-enumeration of declared value sets)
```

---

### GROUP B — SYNTHESIZER

`(C-15: structural group label; C-22: begins only on SCAN GATE PASS TOKEN; C-10: current vs
recommended clearly separated; C-07: org shape named and justified; C-72: all references
to schema-declared value sets carry named-convention annotations; C-73: all constraints
traceable to preamble declarations; C-71: footer carries MET/NOT MET for all GROUP B floors)`

**Precondition (C-22)**: Read GROUP A final output line. If FAIL TOKEN or TABLE F FAIL STRING,
write verbatim and halt.

**OUTPUT FORMAT CONSTRAINT (C-05 — second statement)**: RAW ANALYSIS ONLY. No org chart.
No reporting lines. No hierarchy diagram. Named recommendations only — no drawn structure.

#### Org Shape Assessment

`(C-07: named from findings; C-03: headcount from TABLE E; preamble declaration #6)`

Dominant pattern from GROUP A: [INR-NN — named shape].

Org shape inferred: [named type]. Justification: [two to three sentences citing TABLE B rows
by Area, INR-NN pattern [from INERTIA PATTERN DICTIONARY (see PREAMBLE SCHEMA DECLARATIONS
— pattern labels not restated here per schema-first reference pattern)], TABLE E headcount.]

#### TABLE H — Org Shape Delta

`(schema preamble declaration #10; BRIDGE RULE [declared in TABLE H schema (see PREAMBLE
SCHEMA DECLARATIONS — BRIDGE RULE constraint not restated here per schema-first reference
pattern)]; dimensions [declared in TABLE H schema (see PREAMBLE SCHEMA DECLARATIONS —
dimension list not restated here per schema-first reference pattern)];
C-10: Current State / Recommended State separated as named columns; C-71: footer will carry
TABLE H assertion match and BRIDGE RULE compliance tokens)`

**Pre-production assertion (C-69)**:
`Org Shape Dimension count: [N] — TABLE H must contain exactly [N] rows.`

BRIDGE RULE active [declared in TABLE H schema — preamble declaration #10; not restated here
per schema-first reference pattern]: every Driving Evidence cell must contain
`(cite TABLE B row)` annotation.

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
dimensions [declared in TABLE H schema per schema-first reference pattern]. Raw analysis only
— no org chart.]

#### Evidence Gaps Acknowledged

`(C-08: references TABLE G — preamble declaration #9)`

[One sentence per TABLE G row: acknowledge gap, state impact on recommendation confidence.]

```
GROUP B PHASE OUTPUTS
(C-37/C-71: footer carries named MET/NOT MET compliance tokens for every floor-constrained
 criterion declared in PREAMBLE DECLARATION MANIFEST floor list that is active in GROUP B;
 any criterion absent is a C-71 violation detectable by comparison against manifest floor list)

  TABLE H rows produced:             [N]  (pre-production assertion: [N]; match: YES / NO)
  BRIDGE RULE compliance:                  (all Driving Evidence cells cite TABLE B: YES / NO)
  Org shape named and justified:           (C-07: named shape present:         MET / NOT MET)
  Current vs Recommended separated:        (C-10: distinct named columns:      MET / NOT MET)
  Evidence gaps acknowledged:        [N] from TABLE G (decl. #9)
  C-05 constraint:                         (raw analysis only, no org chart:   MET / NOT MET)
  Schema-first reference convention:       (C-72: all GROUP B instructions
                                            carry named-convention annotations: MET / NOT MET)
  Preamble declarations used in GROUP B:   10 (all 10 referenced: YES/NO)
```

---

> "org-scan complete (R20 V-05 — Combination: C-70 + C-71 + C-72 + C-73). PREAMBLE
> DECLARATION MANIFEST: 10 declared structures (2 named protocols + 8 schemas) with explicit
> count — any absent declaration is a C-73 violation by count comparison. Floor list in
> manifest drives C-71 footer compliance tokens in both GROUP A and GROUP B PHASE OUTPUTS —
> 8 MET/NOT MET tokens in GROUP A footer, 6 in GROUP B footer; any floor criterion absent
> from a footer is a C-71 violation. C-72 schema-first reference convention invoked by name
> at 8 instruction sites across GROUP A and GROUP B — no inline re-enumeration of any
> schema-declared value set. C-70: TABLE F FAIL STRING is a named constant in GATE TOKEN
> PROTOCOL distinct from generic FAIL TOKEN; gate checklist item [8] is TABLE F Analytical
> Purpose compliance; failure produces TABLE F FAIL STRING independently identifiable without
> parsing FAIL TOKEN reason field. Every criterion C-67 through C-73 is verifiable from three
> independent locations: preamble declaration (requirement), instruction annotation (application),
> footer compliance token (confirmation). C-05 stated twice. Raw analysis only."
