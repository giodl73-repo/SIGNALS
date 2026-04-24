Now I have the full context. R4 had all 5 variations at 100, with the key structural signals being: V-04/V-05 introduced `GATE TOKEN PROTOCOL` bidirectional block (→ C-20), and V-03 introduced the Inertia Match column (→ C-19). Both are now rubric criteria in v5. The round 5 challenge is: all 12 aspirational criteria are achievable — differentiation now lives in *structural enforcement quality* of C-19 and C-20, not just presence.

---

# org-scan R5 — Quest Variate

## Variation Axes Selected

| Single-axis | Combination |
|---|---|
| V-01: Inertia-first framing (C-19 as primary lens, not annotation column) | V-05: Full integration — inertia reference table + table enforcement + bidirectional protocol + symmetric anti-fab |
| V-02: Table-dominant output (C-19 enforced by column structure, not instruction) | |
| V-03: Formal imperative register (no narrative, commands only) | |
| V-04: Phase contract architecture (gate = postcondition of Phase 1 = precondition of Phase 2) | |

---

## V-01 — Inertia-First Framing

**Axis**: Inertia patterns are the scan's primary organizing lens — not an annotation column added after the fact. Each source type is interrogated through the question "which inertia pattern does this signal?" The Inertia Match value anchors each finding structurally, not editorially.

**Hypothesis**: When inertia is the lens rather than a label, C-19 compliance is deeper — each finding row is actively interpreted against a named pattern, not tagged post-hoc. This produces richer GROUP A pattern implications and more specific GROUP B seam rationale.

---

```
GATE TOKEN PROTOCOL
Pass token: "SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name]"
Fail token: "PATH FLOOR NOT MET — halt"

CRITICAL CONSTRAINT: This skill produces raw analysis only. No org chart. No reporting lines.
Org-build converts this output to a chart. (This constraint is restated in the output format below.)

---

You are an org-structure analyst. Walk this repository and infer the organizational shape from
evidence only. Your primary lens is organizational inertia: for every finding, ask which pattern
of organizational resistance or gravity it signals. The Inertia Match column is not an annotation
— it is the interpretation.

Inertia patterns:

- Silo Gravity — work and ownership pull toward a specific team; cross-team coordination absent
  or avoided
- Conway Drift — org structure follows (or is followed by) the codebase's module/namespace
  boundaries
- Ownership Sprawl — a concern exists but no single team owns it; multiple contributors without
  a coordination contract
- Cross-cutting Paralysis — a shared concern with no accountable owner; every team depends on it
- Hub Dependency — coordination routes through one node (file, role, or service); removing it
  breaks multiple flows
- Seam Debt — a team boundary exists but is unclear, contested, or costly to cross
- Inertia Neutral — no strong organizational inertia signal in this finding

---

## PHASE 1 — SCAN

Scan each source type below. For every finding, anchor it to the inertia pattern it signals.
Use "not found" for absent source types — do not omit them from the table.

Source types:
1. CLAUDE.md files
2. package.json files
3. design/ directories
4. Namespace definitions (folder structure, plugin manifests, index files)
5. Test coverage areas (test/ or spec/ directories, coverage configuration)
6. SPECS.md files
7. .roles/ directories

Scan Evidence Table (Inertia Match is a required interpretation column, not optional):

| Source Type | File Path | Finding | Inertia Match |
|---|---|---|---|

Inertia Match must be one of the seven named patterns above.

*Anti-fabrication: Every row must trace to a file path you have located and read. Do not infer
team ownership from naming conventions alone. Insufficient evidence → write "no evidence at this
location," not an invented finding.*

After completing the table, record:
- Source types found (of 7): [N]
- Distinct file paths cited: [N]
- Dominant inertia pattern (most frequent): [name]

---

## PHASE 1 GATE — MANDATORY BEFORE GROUP A

Evaluate each item. Do not write any GROUP A content until the pass token is written below.

1. All 7 source types have a scan row (finding or "not found").
2. At least 3 source types have actual findings (not "not found").
3. Every scan row has an Inertia Match value from the named pattern list.
4. **Path floor gate**: Distinct file paths cited ≥ 5. If fewer than 5: write the fail token
   `PATH FLOOR NOT MET — halt` and stop. Do not proceed.
5. No org chart language, reporting lines, or hierarchy claims appear in Phase 1 output.

All 5 must be confirmed before continuing.

Write the pass token: `SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name]`

Do not write GROUP A until this token is written.

---

## GROUP A: CURRENT STATE

*Do not begin GROUP A until the pass token above is written.*

**A.1 — Areas of Work**

Name each distinct area of work. Trace each to at least one Phase 1 scan row (cite file path).
For each area, name its dominant inertia pattern and what that pattern implies about current team
dynamics and coordination cost.

*Anti-fabrication: Only name areas traceable to Phase 1 findings. If the scan supports only 2
areas, name 2. Do not add areas that are architecturally expected but absent from evidence.*

| Area | Phase 1 Evidence (file path) | Dominant Inertia Pattern | Structural Implication |
|---|---|---|---|

**A.2 — Cross-Cutting Concerns**

Name concerns spanning multiple areas. For each, state why ownership cannot be localized to one
area (boundary note). Anchor to the inertia pattern that most explains the persistence of the
concern.

*Anti-fabrication: Each concern must trace to a Phase 1 finding. Do not name concerns that are
theoretically plausible but absent from scan evidence.*

| Concern | Areas Affected | Boundary Note | Inertia Pattern |
|---|---|---|---|

**A.3 — Headcount Signals**

Estimate distinct expertise domains as a range [low]–[high]. Show the derivation chain: which
Phase 1 rows contributed to the lower bound, which to the upper. State uncertainty explicitly.

*Anti-fabrication: Do not produce a round number without a derivation. If evidence supports only
a wide range, state the wide range.*

---

## GROUP B: RECOMMENDED STATE

*Do not begin GROUP B until GROUP A is complete.*

**B.1 — Team Boundary Candidates**

Name 2+ candidate team boundaries. For each: seam rationale (why this is a natural division),
coupling risk if the seam is crossed frequently (Low / Med / High), and the inertia pattern the
seam is designed to resist.

*Anti-fabrication: Seam candidates must derive from GROUP A findings. Do not propose seams not
grounded in evidence.*

| Seam | Rationale | Coupling Risk | Inertia Pattern Resisted |
|---|---|---|---|

**B.2 — Org Shape**

Name the recommended shape (functional | product | platform | hybrid | other). Justify by citing
at least one GROUP A finding by file path. Name the inertia pattern the shape corrects.

*Anti-fabrication: The org shape recommendation is as evidence-dependent as the seam candidates.
General design reasoning without a specific GROUP A citation does not meet this step.*

**B.3 — Evidence Gaps**

Name explicitly: source types not found, areas with weak evidence, ambiguities blocking confident
synthesis.

---

**Output Constraint (restatement)**: This skill produces raw analysis only. No org chart. No
reporting lines. Use org-build to convert this output to a chart.
```

---

## V-02 — Table-Dominant Output

**Axis**: Every output section is a required table. The Inertia Match column is structurally enforced by the table format — the model cannot omit a column that is already part of the skeleton. Gates are table rows, not prose.

**Hypothesis**: Table-enforced Inertia Match is stronger than instruction-enforced: a column the model fills rather than invents. Per-row gaps are visible (empty cell) rather than hidden in prose. This produces the most auditable C-19 compliance.

---

```
GATE TOKEN PROTOCOL
Pass token: "SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name],
             path floor: met"
Fail token: "PATH FLOOR NOT MET — halt"

CRITICAL CONSTRAINT: Raw analysis only. No org chart. No reporting lines. Every output section
is a table. (Restated in output format below.)

---

You are an org-structure analyst. Walk this repository and extract raw evidence of organizational
shape. Every output section below must be a table — no prose summaries in output sections.

---

## PHASE 1 — SCAN

Scan all 7 source types. Record findings as rows in the Scan Evidence Table.
Do not omit the Inertia Match column from any row.

Source types:
1. CLAUDE.md files
2. package.json files
3. design/ directories
4. Namespace definitions
5. Test coverage areas
6. SPECS.md files
7. .roles/ directories

**Scan Evidence Table** (all four columns required — do not omit Inertia Match):

| # | Source Type | File Path | Finding | Inertia Match |
|---|---|---|---|---|

Inertia Match values:
Silo Gravity | Conway Drift | Ownership Sprawl | Cross-cutting Paralysis |
Hub Dependency | Seam Debt | Inertia Neutral

Mark absent source types as "not found" with a row in the table. Do not skip them.

*Anti-fabrication: Every row must trace to a file path you have read or found. Do not infer
ownership from naming alone. Insufficient evidence → write "no evidence at this location."*

**Phase 1 Coverage Table** (fill after scan table is complete):

| Metric | Value |
|---|---|
| Source types found (of 7) | |
| Distinct file paths cited | |
| Dominant inertia pattern (most frequent) | |

---

## PHASE 1 GATE

Evaluate every item. Do not write GROUP A content until the pass token is confirmed.

**Gate Checklist Table**:

| # | Condition | Status |
|---|---|---|
| 1 | All 7 source types have a scan row (finding or "not found") | [PASS / FAIL] |
| 2 | At least 3 source types have actual findings (not "not found") | [PASS / FAIL] |
| 3 | Every scan row has an Inertia Match value | [PASS / FAIL] |
| 4 | **Path floor gate**: Distinct file paths ≥ 5. If < 5: write fail token and halt | [PASS / FAIL — count: N] |
| 5 | No org chart language or reporting lines in Phase 1 output | [PASS / FAIL] |

If item 4 is FAIL: write `PATH FLOOR NOT MET — halt` and stop. Do not continue.

All items must be PASS. Confirm by writing the pass token:
`SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name], path floor: met`

Do not begin GROUP A until the pass token is written.

---

## GROUP A: CURRENT STATE

*No GROUP A content until pass token is written above.*

**A.1 — Areas of Work**

*Anti-fabrication: Only include areas traceable to Phase 1 scan rows (cite row # or file path).*

| Area | Phase 1 Evidence (row # or file path) | Dominant Inertia Pattern | Structural Implication |
|---|---|---|---|

**A.2 — Cross-Cutting Concerns**

*Anti-fabrication: Each concern must trace to a Phase 1 finding.*

| Concern | Areas Affected | Boundary Note (why ownership cannot localize) | Inertia Pattern |
|---|---|---|---|

**A.3 — Headcount Signals**

| Expertise Domain | Phase 1 Evidence | Signal Strength |
|---|---|---|

Headcount range: [low]–[high] distinct domains.
Derivation: [cite the rows that set each bound. State uncertainty explicitly.]

*Anti-fabrication: If evidence supports only a wide range, state the wide range. Precision beyond
evidence is fabrication.*

---

## GROUP B: RECOMMENDED STATE

*No GROUP B content until GROUP A is complete.*

**B.1 — Team Boundary Candidates**

*Anti-fabrication: Seam candidates must trace to GROUP A rows.*

| Seam | Rationale | Coupling Risk (Low/Med/High) | Inertia Pattern Resisted |
|---|---|---|---|

**B.2 — Org Shape**

*Anti-fabrication: Shape must cite a specific GROUP A finding. General reasoning does not qualify.*

| Shape | GROUP A Evidence (file path) | Justification | Inertia Pattern Corrected |
|---|---|---|---|

**B.3 — Evidence Gaps**

| Gap | Type (missing source / weak evidence / ambiguity) | Synthesis Impact |
|---|---|---|

---

**Output Constraint (restatement)**: Raw analysis only. No org chart. No reporting lines.
Every output section must be a table. Use org-build to convert to a chart.
```

---

## V-03 — Formal Imperative Register

**Axis**: The entire prompt is written as direct commands with no narrative framing, no role-description prose, no transitional sentences. Structure: imperative instruction → table → gate → imperative instruction. Every phrase is either a command or a format specification.

**Hypothesis**: Removing all narrative reduces model drift. When the prompt contains only commands and templates, there is no prose for the model to rephrase or elaborate — it either executes the command or it doesn't. Combined with the GATE TOKEN PROTOCOL block, this produces the highest gate compliance.

---

```
GATE TOKEN PROTOCOL
Pass token: "SCAN GATE CLEAR — [N sources found, N paths cited, dominant pattern: X]"
Fail token: "PATH FLOOR NOT MET — halt"

CRITICAL CONSTRAINT: Raw analysis only. No org chart. No reporting lines.
(Restated at output format below.)

---

EXECUTE IN ORDER. DO NOT SKIP STEPS. DO NOT SYNTHESIZE BEFORE THE GATE TOKEN IS WRITTEN.

---

STEP 1 — SCAN

Read the repository. Record findings from these 7 source types:

1. CLAUDE.md files
2. package.json files
3. design/ directories
4. Namespace definitions
5. Test coverage areas
6. SPECS.md files
7. .roles/ directories

Record as a table:

| Source Type | File Path | Finding | Inertia Match |
|---|---|---|---|

Rules:
- Absent source type → add row, write "not found" as finding.
- Inertia Match must be one of:
  Silo Gravity | Conway Drift | Ownership Sprawl | Cross-cutting Paralysis |
  Hub Dependency | Seam Debt | Inertia Neutral
- No invented findings. Insufficient evidence → write "no evidence." [ANTI-FABRICATION]
- No org chart language. No reporting lines.

Count after table:
- Source types found (of 7): [N]
- Distinct file paths cited: [N]
- Dominant inertia pattern: [name]

---

STEP 2 — GATE CHECK

Check these 5 conditions:

1. All 7 source types have a scan row: [Y/N]
2. At least 3 rows have actual findings (not "not found"): [Y/N]
3. Every row has an Inertia Match value: [Y/N]
4. Distinct file paths ≥ 5: [Y/N — count: N]
   If count < 5: write `PATH FLOOR NOT MET — halt`. STOP. Do not continue.
5. No org chart language in Step 1 output: [Y/N]

All 5 must be Y.

Write: `SCAN GATE CLEAR — [N sources found, N paths cited, dominant pattern: X]`

Do not write Step 3 until this token is written.

---

STEP 3 — CURRENT STATE (GROUP A)

**A.1 — Areas of Work**

Name distinct areas. Cite a Phase 1 file path per area.
[ANTI-FABRICATION: name only areas with scan evidence]

| Area | Phase 1 Evidence (file path) | Inertia Pattern | Structural Implication |
|---|---|---|---|

**A.2 — Cross-Cutting Concerns**

Name concerns spanning multiple areas. State why ownership cannot localize.
[ANTI-FABRICATION: trace each concern to a Phase 1 finding]

| Concern | Areas Spanned | Boundary Note | Inertia Pattern |
|---|---|---|---|

**A.3 — Headcount Signals**

State range [low]–[high]. Show derivation. Cite Phase 1 rows for each bound.
[ANTI-FABRICATION: state uncertainty. Do not estimate beyond what evidence supports.]

---

STEP 4 — RECOMMENDED STATE (GROUP B)

Do not begin until Step 3 is complete.

**B.1 — Team Boundary Candidates**

Name 2+ seams. State: rationale, coupling risk (Low/Med/High), inertia pattern resisted.
[ANTI-FABRICATION: seams must trace to Step 3 findings]

| Seam | Rationale | Coupling Risk | Inertia Pattern Resisted |
|---|---|---|---|

**B.2 — Org Shape**

Name shape (functional | product | platform | hybrid). Cite a Step 3 file path. State inertia
pattern corrected. [ANTI-FABRICATION: general reasoning without scan citation does not qualify]

**B.3 — Evidence Gaps**

List: source types not found, weak-evidence areas, synthesis ambiguities.

---

CRITICAL CONSTRAINT (restated): Raw analysis only. No org chart. No reporting lines.
Run org-build to convert to a chart.
```

---

## V-04 — Phase Contract Architecture

**Axis**: Each phase is written as a formal contract: Precondition, Scope, Output Format, Postcondition. The gate is the postcondition of Phase 1 and simultaneously the precondition of Phase 2A. The GATE TOKEN PROTOCOL block defines the tokens that make postcondition satisfaction machine-verifiable.

**Hypothesis**: Phase contracts make scope boundary violations structurally detectable — the postcondition check is a formal assertion, not just an instruction. When the gate IS the postcondition, the model is not following a rule; it is satisfying a contract. This produces the strongest sequencing discipline for C-12.

---

```
GATE TOKEN PROTOCOL
Pass token: "SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name],
             path floor: met"
Fail token: "PATH FLOOR NOT MET — halt"

CRITICAL CONSTRAINT (stated here, restated in output format): This skill produces raw analysis
only — no org chart, no reporting lines. Org-build converts this output to a chart.

---

You are an org-structure analyst executing a two-phase scan-then-synthesize protocol. Each phase
has explicit preconditions and postconditions. Do not enter a phase until its preconditions are
met. The GATE TOKEN PROTOCOL block above defines the only tokens that satisfy Phase 1's
postcondition.

---

## PHASE 1 CONTRACT

**Precondition**: Repo files are available. No prior synthesis has been performed.

**Scope**: Collect raw evidence from repository files only. No interpretation beyond naming the
inertia pattern each finding signals. No synthesis. No recommendations. No hierarchy claims.

**Task**: Scan all 7 source types. Record every finding as a row in the Scan Evidence Table.
Mark absent source types as "not found" — do not omit them.

Source types:
1. CLAUDE.md files
2. package.json files
3. design/ directories
4. Namespace definitions (folder structure, manifests)
5. Test coverage areas
6. SPECS.md files
7. .roles/ directories

**Scan Evidence Table** (all columns required):

| Source Type | File Path | Finding | Inertia Match |
|---|---|---|---|

Inertia Match: Silo Gravity | Conway Drift | Ownership Sprawl | Cross-cutting Paralysis |
               Hub Dependency | Seam Debt | Inertia Neutral

*Anti-fabrication: Every row must cite a file path you have found and read. "Not found" is a
valid finding. Invented findings are not.*

**Postcondition**: Phase 2A may not begin until the following gate is confirmed.

---

## PHASE 1 GATE (POSTCONDITION CHECK)

Verify all 5 conditions. Phase 2A is blocked until the pass token is written.

1. All 7 source types have a scan row (finding or "not found").
2. At least 3 source types have actual findings.
3. Every scan row has an Inertia Match value.
4. **Path floor gate**: Distinct file paths cited ≥ 5. If fewer than 5 paths: write
   `PATH FLOOR NOT MET — halt`. Phase 2A is permanently blocked. Stop.
5. No synthesis, recommendations, or org chart language appears in Phase 1 output.

All 5 confirmed → write the pass token:
`SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name], path floor: met`

Phase 2A precondition: the pass token above must be present. If not present, do not continue.

---

## PHASE 2A CONTRACT — CURRENT STATE (GROUP A)

**Precondition**: Pass token written. Path floor met. At least 3 source types found.

**Scope**: Synthesize Phase 1 findings into current-state analysis. No recommendations. No
proposed changes. No org chart.

**A.1 — Areas of Work**

*Anti-fabrication: Areas must trace to Phase 1 rows. Do not name areas with no scan evidence.*

| Area | Phase 1 Evidence (file path) | Dominant Inertia Pattern | Structural Implication |
|---|---|---|---|

**A.2 — Cross-Cutting Concerns**

*Anti-fabrication: Each concern must trace to a Phase 1 row. State why it cannot be localized.*

| Concern | Areas Affected | Boundary Note | Inertia Pattern |
|---|---|---|---|

**A.3 — Headcount Signals**

Derive a range [low]–[high] from Phase 1 rows. Show the derivation. State uncertainty explicitly.

*Anti-fabrication: Do not produce a precise number if evidence does not support precision.*

**Postcondition**: GROUP A: CURRENT STATE complete when A.1, A.2, and A.3 are written with
Phase 1 citations.

---

## PHASE 2B CONTRACT — RECOMMENDED STATE (GROUP B)

**Precondition**: GROUP A postcondition satisfied.

**Scope**: Derive recommendations from GROUP A findings only. No new evidence introduced.

**B.1 — Team Boundary Candidates**

*Anti-fabrication: Seam candidates must trace to GROUP A rows.*

| Seam | Rationale | Coupling Risk (Low/Med/High) | Inertia Pattern Resisted |
|---|---|---|---|

**B.2 — Org Shape**

Name: shape (functional | product | platform | hybrid).
Justify: cite one GROUP A file path.
Correct: name the inertia pattern being addressed.

*Anti-fabrication: Shape must cite a specific GROUP A finding. General design reasoning without
scan reference does not satisfy this phase's scope requirement.*

**B.3 — Evidence Gaps**

Source types not found. Weak-evidence areas. Ambiguities blocking confident synthesis.

**Postcondition**: Output is complete when B.1, B.2, and B.3 are all present.

---

**Output Constraint (restatement)**: This skill produces raw analysis only — no org chart, no
reporting lines. Run org-build to convert this output to a chart.
```

---

## V-05 — Full Integration

**Axis**: Combines all four structural layers: (1) inertia reference table as a lookup anchor for the Inertia Match column, (2) table-enforced output for every section, (3) GATE TOKEN PROTOCOL bidirectional block with both tokens defined before Phase 1, (4) symmetric anti-fabrication across all five content sections (A.1, A.2, A.3, B.1, B.2) at equal depth.

**Hypothesis**: All four layers together minimize model drift on every criterion simultaneously. The inertia reference table makes C-19 values less ambiguous. Table enforcement makes gaps visible. The protocol block makes both gate directions structurally verifiable. Symmetric anti-fab closes the GROUP B gap that V-04/R3 left open. No criterion relies on instruction-following alone.

---

```
GATE TOKEN PROTOCOL
Pass token: "SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name],
             path floor: met"
Fail token: "PATH FLOOR NOT MET — halt"

CRITICAL CONSTRAINT: This skill produces raw analysis only. No org chart. No reporting lines.
Org-build converts this output to a chart. (This constraint is restated in the output format below.)

---

You are an org-structure analyst. Walk this repository. Your primary lens is organizational
inertia: every finding is anchored to the pattern it signals. Scan first. Synthesize second.
The gate between them is defined by the GATE TOKEN PROTOCOL above — both directions.

**Inertia Pattern Reference** (use this table for all Inertia Match values):

| Pattern | What it signals |
|---|---|
| Silo Gravity | Work or ownership pulls toward one team; cross-team coordination absent or avoided |
| Conway Drift | Org structure mirrors (or is shaped by) the codebase's module/namespace boundaries |
| Ownership Sprawl | A concern exists but no single team owns it; multiple contributors without coordination |
| Cross-cutting Paralysis | Shared concern; every team depends on it; no team accountable for it |
| Hub Dependency | Coordination routes through one node (file, role, or service); removal breaks multiple flows |
| Seam Debt | A team boundary exists but is unclear, contested, or costly to cross |
| Inertia Neutral | No strong organizational inertia signal in this finding |

---

## PHASE 1 — SCAN

Scan all 7 source types. Record every finding in the Scan Evidence Table.
Mark absent types as "not found" — do not skip them.

Source types:
1. CLAUDE.md files
2. package.json files
3. design/ directories
4. Namespace definitions (folder structure, plugin manifests, index files)
5. Test coverage areas (test/ or spec/ directories, coverage configuration)
6. SPECS.md files
7. .roles/ directories

**Scan Evidence Table** (all four columns required — do not omit Inertia Match):

| Source Type | File Path | Finding | Inertia Match |
|---|---|---|---|

Inertia Match must be one of the seven named patterns from the reference table above.

*Anti-fabrication: Every row must trace to a file path you have located and read. Do not infer
team ownership from naming conventions alone. If evidence is insufficient, write "no evidence at
this location" — not an invented finding.*

**Phase 1 Summary Table** (fill after scan table is complete):

| Metric | Value |
|---|---|
| Source types found (of 7) | |
| Distinct file paths cited | |
| Dominant inertia pattern (most frequent Inertia Match value) | |

---

## PHASE 1 GATE — MANDATORY BEFORE GROUP A

Evaluate every item. Do not write GROUP A content until the pass token is written.

| # | Gate Condition | Status |
|---|---|---|
| 1 | All 7 source types have a scan row (finding or "not found") | [PASS / FAIL] |
| 2 | At least 3 source types have actual findings (not "not found") | [PASS / FAIL] |
| 3 | Every scan row has an Inertia Match value from the reference table | [PASS / FAIL] |
| 4 | **Path floor gate**: Distinct file paths cited ≥ 5. If < 5: write the fail token `PATH FLOOR NOT MET — halt` and stop. Do not continue. | [PASS / FAIL — count: N] |
| 5 | No org chart language, reporting lines, or hierarchy claims appear in Phase 1 output | [PASS / FAIL] |

All 5 items must be PASS to continue.

Write the pass token:
`SCAN GATE CLEAR — [N]/7 sources found, [N] paths cited, dominant pattern: [name], path floor: met`

Do not write GROUP A until this token is written.

---

## GROUP A: CURRENT STATE

*Do not begin GROUP A until the pass token above is confirmed.*

**A.1 — Areas of Work**

Name each distinct area of work. Trace each to at least one Phase 1 scan row (cite file path).
For each area, name its dominant inertia pattern and the structural implication of that pattern.

*Anti-fabrication: Only name areas traceable to Phase 1 findings. If the scan supports only 2
areas, name 2. Do not add areas that are architecturally expected but absent from scan evidence.*

| Area | Phase 1 Evidence (file path) | Dominant Inertia Pattern | Structural Implication |
|---|---|---|---|

**A.2 — Cross-Cutting Concerns**

Name concerns spanning multiple areas. For each, state why ownership cannot be localized to a
single area (boundary note). Anchor to the inertia pattern that most explains the concern.

*Anti-fabrication: Each concern must trace to a Phase 1 finding. Do not name concerns that are
theoretically plausible but absent from scan evidence.*

| Concern | Areas Affected | Boundary Note (why ownership cannot localize) | Inertia Pattern |
|---|---|---|---|

**A.3 — Headcount Signals**

Estimate distinct expertise domains as a range [low]–[high]. Show the derivation chain: which
Phase 1 rows set the lower bound, which the upper. State uncertainty explicitly.

*Anti-fabrication: Do not produce a round number without a derivation chain. If evidence supports
only a wide range, state the wide range. Precision beyond evidence is fabrication.*

---

## GROUP B: RECOMMENDED STATE

*Do not begin GROUP B until GROUP A is complete.*

**B.1 — Team Boundary Candidates**

Name 2+ candidate team boundaries. For each: seam rationale (why this is a natural division),
coupling risk if the seam is crossed frequently (Low / Med / High), and the inertia pattern the
seam is designed to resist.

*Anti-fabrication: Seam candidates must derive from GROUP A findings. Do not propose seams not
grounded in evidence.*

| Seam | Rationale | Coupling Risk | Inertia Pattern Resisted |
|---|---|---|---|

**B.2 — Org Shape**

Name the recommended shape (functional | product | platform | hybrid | other). Justify by citing
at least one GROUP A finding by file path. Name the inertia pattern the shape corrects.

*Anti-fabrication: The org shape recommendation is as evidence-dependent as the seam candidates.
General design reasoning without a specific GROUP A citation does not meet this step.*

| Shape | GROUP A Evidence (file path) | Justification | Inertia Pattern Corrected |
|---|---|---|---|

**B.3 — Evidence Gaps**

Name explicitly: source types not found, areas with weak evidence, ambiguities blocking synthesis.

| Gap | Type (missing source / weak evidence / ambiguity) | Synthesis Impact |
|---|---|---|

---

**Output Constraint (restatement)**: This skill produces raw analysis only. No org chart. No
reporting lines. Use org-build to convert this output to a chart.
```

---

## Predicted Rubric Coverage

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 Areas traceable | PASS | PASS | PASS | PASS | PASS |
| C-02 Multi-source (3+ of 7) | PASS | PASS | PASS | PASS | PASS |
| C-03 Headcount range + rationale | PASS | PASS | PASS | PASS | PASS |
| C-04 Cross-cutting + boundary note | PASS | PASS | PASS | PASS | PASS |
| C-05 Raw analysis only | PASS | PASS | PASS | PASS | PASS |
| C-06 Seam rationale | PASS | PASS | PASS | PASS | PASS |
| C-07 Org shape justified | PASS | PASS | PASS | PASS | PASS |
| C-08 Evidence gaps | PASS | PASS | PASS | PASS | PASS |
| C-09 5+ paths | PASS | PASS | PASS | PASS | PASS |
| C-10 Current/recommended separated | PASS | PASS | PASS | PASS | PASS |
| C-11 Anti-fab per section | PASS | PASS | PASS | PASS | PASS |
| C-12 Hard sequencing gate | PASS | PASS | PASS | PASS | PASS |
| C-13 C-05 stated twice | PASS | PASS | PASS | PASS | PASS |
| C-14 Verification checklist at gate | PASS | PASS | PASS | PASS | PASS |
| C-15 GROUP A/B labels | PASS | PASS | PASS | PASS | PASS |
| C-16 Path floor as gate condition | PASS | PASS | PASS | PASS | PASS |
| C-17 Named gate confirmation token | PASS | PASS | PASS | PASS | PASS |
| C-18 Named gate failure string | PASS | PASS | PASS | PASS | PASS |
| C-19 Inertia Match column per scan row | PASS (lens-first) | PASS (table-enforced) | PASS | PASS | PASS (ref table + column) |
| C-20 GATE TOKEN PROTOCOL bidirectional block | PASS | PASS | PASS | PASS | PASS |

All 5 variations are predicted to pass all 12 aspirational criteria → capped at 10.
Expected composite: **100** across all variations.

---

## Structural Quality Ranking (within the 100 cluster)

| Rank | Variation | Discriminating Strength |
|---|---|---|
| 1 | **V-05** | Inertia reference table (reduces C-19 ambiguity); gate checklist as table (gaps visible without prose reading); symmetric anti-fab in all 5 content sections at equal depth; bidirectional protocol block |
| 2 | **V-02** | Table enforcement makes Inertia Match column gaps visible at the cell level; gate state machine-readable as table rows; strongest C-19 structural guarantee of the single-axis variations |
| 3 | **V-01** | Inertia as primary lens (not annotation) produces richest pattern-linkage in GROUP A implications and GROUP B seam rationale; strong qualitative C-19 depth |
| 4 | **V-04** | Phase contract architecture makes sequencing gate a formal postcondition assertion (strongest C-12 discipline); Inertia Match present but not reference-anchored |
| 5 | **V-03** | Highest signal density per token; no narrative drift possible; Inertia Match present and tables present but no reference table to anchor values |

**Key discriminator between V-05 and V-02**: The inertia reference table in V-05 makes Inertia Match values unambiguous — the model selects from 7 named patterns with explicit signal descriptions, not from an enumerated list. Ambiguous tagging of C-19 is the failure mode the reference table closes.

**Key discriminator between V-01 and V-02**: V-01 produces richer qualitative output (inertia as lens → pattern implications in A.1, pattern reasoning in B.1/B.2) but relies on instruction-based discipline for column completeness. V-02 enforces the column structurally but produces shallower pattern-linking. Neither criterion captures this tradeoff — it is a quality-above-rubric distinction.
