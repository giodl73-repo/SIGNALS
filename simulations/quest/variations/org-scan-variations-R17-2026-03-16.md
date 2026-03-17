I now have the complete picture: R16 V-05 is the new baseline (C-61 + C-62 + C-63 all present). I'll write R17 with those three as structural invariants and explore three new axes. Let me write the variations.

---

```markdown
---
skill: quest-variate
skill_target: org-scan
round: 17
date: 2026-03-16
rubric_version: 17
---

# org-scan Skill Body Prompt Variations V-01 through V-05
## Targeting rubric v17 (C-01 through C-63)
## Round 17 — 2026-03-16

R16 produced C-61 (`Minimum rows:` annotation in SCHEMA DECLARATION), C-62 (three-phase
symmetric gating: HYPOTHESIS FLOOR GATE + EVIDENCE GATE + SYNTHESIS COMPLETENESS GATE), and
C-63 (`Violated when:` entry in each ROLE SCOPE DECLARATION). All three are structural
invariants for R17: every variation must include them. The R16 V-05 full combination is
promoted to the R17 baseline.

R17 explores three new axes beyond C-63:

- **Axis 1** (V-02): Phrasing register / lifecycle emphasis — `Output Consumers` declaration
  in each ROLE SCOPE DECLARATION, symmetric counterpart to C-59's `Input Dependencies`. Each
  role names which downstream roles consume its outputs and which tables they take. Hypothesis:
  C-59 makes the execution dependency graph derivable from declarations along the incoming edge
  (what I need). `Output Consumers` adds the outgoing edge (who needs me), making the full
  directed dependency graph bidirectional — derivable from role declarations in either direction
  without instruction-text traversal. Candidate for C-64.

- **Axis 2** (V-03): Output format / lifecycle emphasis — Named `COVERAGE ATTESTATION` table
  at SCANNER exit, enumerating all 7 source types with per-type status (scanned / not-found /
  not-applicable). Hypothesis: the EVIDENCE GATE pass token embeds the scanned count (`[N]
  sources scanned`) but not the per-type breakdown. A COVERAGE ATTESTATION table makes the gap
  between scanned and unscanned source types structurally visible as named rows, distinguishing
  "not-found" (attempted, absent) from "not-applicable" (structurally absent in this repo
  type), enabling gap analysis by type rather than gap analysis by count alone. Candidate for
  C-65.

- **Axis 3** (V-04): Output format — `TABLE H -- Org Shape Delta`, a structured table
  extracting the per-dimension delta between CURRENT STATE and RECOMMENDED STATE from the Org
  Shape paragraph. Hypothesis: CURRENT STATE / RECOMMENDED STATE is produced as prose by
  instruction (C-10 requires separation) but not by schema. TABLE H extracts the per-dimension
  comparison into a queryable 4-column table (Dimension | Current State | Recommended State |
  Driving Evidence), making the org shape recommendation structurally auditable at the cell
  level — every recommended state must cite TABLE B evidence, and the gap between current and
  recommended is visible as a named structured dimension. Candidate for C-66.

V-01 is the full baseline (all C-61 + C-62 + C-63 invariants, no new axis). V-02/V-03/V-04
test one new axis each. V-05 combines all three.

---

## Variation Axes

| Axis | Used In |
|---|---|
| Baseline v17 — full C-61/C-62/C-63 invariant stack | V-01 |
| `Output Consumers` in each ROLE SCOPE DECLARATION | V-02 |
| Named `COVERAGE ATTESTATION` table at SCANNER exit | V-03 |
| `TABLE H -- Org Shape Delta` in SYNTHESIZER output | V-04 |
| Full combination (V-02 + V-03 + V-04) | V-05 |

---

## V-01

**Variation axis**: Baseline v17. All three new criteria (C-61, C-62, C-63) are present as
structural invariants alongside the full prior stack (C-01 through C-60). No new axis. This
is the control condition: R16 V-05 fully written out as the R17 floor. V-02 through V-05 are
tested against this ceiling — their value lies in the excellence signals they produce for
potential C-64+ criteria.

**Hypothesis**: V-01 achieves 100/100 under rubric v17 by treating C-61, C-62, C-63 as
structural invariants. Every variation is measured against this baseline to isolate the
contribution of the new axis.

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column.

TABLE A -- Hypothesis Table
Produced by: PREDICTOR before any scan evidence is collected.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Minimum rows: 6 (one row per I-01, I-02, I-03, I-04, I-05, I-06 — one prediction per
dictionary pattern). A TABLE A with fewer than 6 rows is a prediction-coverage gap.

TABLE B -- Scan Evidence Table
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (dictionary value only — I-01 through I-07) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a schema
violation.

Minimum rows: 5 (path floor — each row must cite a distinct File Path Evidence value).
Rows below this floor block evidence gate passage.

TABLE C -- Headcount Signals
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

Minimum rows: 2 (at least 2 distinct expertise domains to support headcount range rationale).

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

Minimum rows: 1 (at least one cross-cutting concern must be identified or explicitly recorded
as absent with source types checked noted in TABLE F).

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row) |
| Supporting Evidence | REQUIRED |

Minimum rows: 2 (at least 2 boundary candidates required for meaningful seam analysis).

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

Minimum rows: none declared (gaps are evidence-dependent; absence of TABLE F rows is valid
if the scan is complete and all predictions are resolved).

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row) |
| Resolution | REQUIRED (yes / no / partial) |
| Predicted by | REQUIRED (PREDICTOR) |
| Evidence rows cited | REQUIRED (TABLE B row references) |
| Resolved by | REQUIRED (SYNTHESIZER) |

Minimum rows: equal to TABLE A row count (enforced by row-count assertion at SYNTHESIZER
entry). Mismatch between TABLE G row count and TABLE A row count is a structurally detectable
omission.

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Remediate: add TABLE F row with Gap set to
"[PATTERN-ID] prediction unresolved", Implication set to "hypothesis not tested against scan
evidence", Source Types Checked set to the source types that were scanned. No prediction may
remain unresolved without a TABLE F gap entry.

Row-count invariant: TABLE G row count must equal TABLE A row count. A row-count mismatch
between TABLE A and TABLE G is a structurally detectable omission — identifiable by table
correspondence alone without prose inspection.

---

GATE TOKEN PROTOCOL

This block defines all named gate tokens before Phase 1 begins. Every gate in this skill must
write exactly one of its defined tokens. No prose substitution.

HYPOTHESIS FLOOR GATE (Phase 1 / Phase 2 boundary):
  PASS: Hypothesis floor clear -- [N] predictions recorded, [N] distinct pattern codes covered
  FAIL: Hypothesis floor not met -- fewer than 3 predictions or fewer than 2 distinct pattern codes

EVIDENCE GATE (Phase 2 / Phase 3 boundary):
  PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
  FAIL: Path floor not met -- scan incomplete

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
  PASS: Synthesis complete -- TABLE G [N] rows = TABLE A [N] rows, all predictions resolved
  FAIL: Synthesis incomplete -- TABLE G [M] rows, TABLE A [N] rows, [N-M] predictions unresolved

One token from each gate's pair must appear at its corresponding boundary. No prose substitution
for any gate.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from prediction
through verification through synthesis, with each named role applying it in its assigned phase:

- PREDICTOR applies it in Phase 1 to generate hypotheses — each TABLE A prediction must anchor
  to a dictionary pattern before any file is read.
- SCANNER applies it in Phase 2 to label every TABLE B finding — the Inertia Match column is
  the per-row application of this framework to scan evidence.
- SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction against labeled TABLE B
  evidence — every TABLE G row must name the pattern predicted, cite the evidence, and state
  the resolution.

The dictionary is not a post-hoc classifier. It is the analytical lens through which each named
role executes its phase of the investigation.

Free text in the Inertia Match column is structurally invalid. Unconstrained values make pattern
comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, incident response patterns).
PREDICTOR must predict both registers. SCANNER must check both.

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone"; onboarding means shadowing the whole codebase |
| I-02 | Accidental Silos | Multiple directories exist but no explicit ownership documentation; test coverage overlaps across directories; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall without a clear reviewer; incidents involve multiple teams guessing; "we should probably document this" is a recurring sentiment |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain test directories; explicit ownership declared in docs or .craft/roles | "that's the X team's area"; clear escalation path per domain; engineers onboard to a single domain first; incidents have a natural first responder; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer (sdk/, core/, utils/, platform/) clearly distinct from product surfaces; infra layer has its own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team has separate on-call rotation; product features rarely touch infra; platform changes require a coordination meeting; "the platform team owns that" |
| I-05 | Federated | Multiple autonomous workspaces, packages, or repos with minimal shared root; independent CI per workspace; rare central merge events | "each team ships independently"; integration is opt-in; shared tooling is a separate small team; incidents are scoped to one workspace; "we don't need to coordinate on that" |
| I-06 | Hub-and-Spoke | Central orchestrator directory (nexus/, hub/, core/, router/) with peripheral plugin or service directories radiating from it; hub has disproportionate test coverage and documentation depth | "everything routes through the hub"; hub team is the bottleneck for peripheral changes; peripheral teams file issues against the hub; "we need the hub team to merge this first"; hub engineers are stretched thin |
| I-07 | Undefined | Fewer than 3 source types were readable; evidence is insufficient to classify | Cannot assess behavioral signals; pattern classification deferred |

---

GROUP A -- PREDICTOR PHASE

Phase 1: Hypothesis Generation (Role: PREDICTOR)

ROLE SCOPE DECLARATION: PREDICTOR
PAF Authority: dictionary application in Phase 1 only — generate hypotheses anchored to
  named patterns; no analytical conclusions from scan evidence permitted in this phase.
Input Dependencies: none — PREDICTOR is the first role; no prior tables required.
Permitted outputs: TABLE A rows only.
Prohibited outputs: file reads / scan evidence / TABLE B / TABLE C / TABLE D / TABLE E /
  TABLE F / TABLE G / any content derived from reading files.
Violated when: any TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G row appears in
  PREDICTOR output; or any cell in TABLE A contains a specific file path or file content quote.
Constraint check: No file has been read since skill invocation. If any file has been read,
  halt and flag a PREDICTOR scope violation before producing TABLE A.
Org chart prohibition: TABLE A must contain no org chart content, no reporting lines, no
  "reports to" statements.

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction (what code-level signals you expect to find or not find) and a behavioral
prediction (what team-language or ownership signals you expect to find in CLAUDE.md prose). Set
Hypothesis Held to your expectation before evidence.

You are the PREDICTOR. Making both predictions forces the inertia dictionary to be falsifiable
at both registers — structural and behavioral. Do not read any files during this phase.

-> Output TABLE A (minimum 6 rows per SCHEMA minimum rows declaration).

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

PREDICTOR PHASE COMPLETION PROOF:
- PAF binding: Inertia Pattern Dictionary applied in Phase 1 prediction only
- Tables produced: TABLE A (matches schema assignment: "Produced by: PREDICTOR")
- Minimum rows satisfied: [N] rows in TABLE A meets minimum of 6
- No file reads occurred during Phase 1

---

PREDICTOR / SCANNER BOUNDARY

This boundary is the postcondition of Phase 1 and the precondition of Phase 2. Both sides
name the same contract. Both must hold.

PREDICTOR exits. Control transfers to HYPOTHESIS FLOOR GATE evaluation. TABLE A must exist.

HYPOTHESIS FLOOR GATE -- evaluate before SCANNER may begin:

Gate checklist:
1. TABLE A is present and non-empty
2. TABLE A contains at least 3 rows (predictions)
3. TABLE A contains at least 2 distinct Pattern IDs (prediction coverage spans multiple patterns)
4. Every Hypothesis Held cell uses: yes / no / partial
5. No file evidence appears in any TABLE A cell

Write exactly one token:
  PASS: Hypothesis floor clear -- [N] predictions recorded, [N] distinct pattern codes covered
  FAIL: Hypothesis floor not met -- fewer than 3 predictions or fewer than 2 distinct pattern codes

FAIL TOKEN halts execution. SCANNER may not begin until PASS token is written.

---

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

ROLE SCOPE DECLARATION: SCANNER
PAF Authority: dictionary application in Phase 2 only — label findings from files actually
  read; no synthesis conclusions or boundary recommendations permitted in this phase.
Input Dependencies: TABLE A (from PREDICTOR) — must be present; hypothesis floor pass token
  — must be present. SCANNER may not begin if either is absent.
Permitted outputs: TABLE B / TABLE C / TABLE D.
Prohibited outputs: TABLE E / TABLE F / TABLE G / synthesis conclusions / team boundary
  recommendations / org shape determinations / headcount estimates.
Violated when: TABLE E, TABLE F, or TABLE G rows appear in SCANNER output; or Finding column
  in TABLE B contains synthesis language ("this means", "therefore", "the org should", "I
  recommend") rather than factual evidence from files read.
Constraint check: Hypothesis floor PASS token is present in output above. If absent, halt.
Org chart prohibition: TABLE B / TABLE C / TABLE D must contain no org chart content.

Entry condition: PREDICTOR COMPLETE present. Hypothesis floor PASS token present. TABLE A
exists.

Anti-fabrication: Report only findings from files actually read. Record absences explicitly.
Do not infer from file names. Cite only paths that exist.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .craft/roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language
-- these are behavioral signal evidence for TABLE B Behavioral Signals and Hypothesis Held.

File path floor (gate precondition): TABLE B must contain at least 5 rows with File Path
Evidence populated with distinct file paths. This requirement blocks gate passage if unmet.

-> Output TABLE B (minimum 5 rows per SCHEMA minimum rows declaration).
-> Output TABLE C (minimum 2 rows per SCHEMA minimum rows declaration).
-> Output TABLE D (minimum 1 row per SCHEMA minimum rows declaration, or TABLE F gap entry
   if no cross-cutting concerns found).

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" before proceeding.

SCANNER PHASE COMPLETION PROOF:
- PAF binding: all Inertia Match cells use dictionary values I-01 through I-07; no free text
- Tables produced: TABLE B, TABLE C, TABLE D (matches schema assignments for SCANNER)
- Anti-fabrication confirmed: all File Path Evidence cells reference files actually read
- Minimum rows satisfied: TABLE B >= 5, TABLE C >= 2

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name
the same contract. Both must hold.

SCANNER exits. GATEKEEPER begins.

ROLE SCOPE DECLARATION: GATEKEEPER
PAF Authority: gate evaluation only — no analytical work, no finding generation, no synthesis.
Input Dependencies: TABLE B + TABLE C + TABLE D (from SCANNER) — all three must be present;
  SCANNER COMPLETE token — must be present.
Permitted outputs: exactly one EVIDENCE GATE token (PASS or FAIL from GATE TOKEN PROTOCOL).
Prohibited outputs: TABLE E / TABLE F / TABLE G / analytical findings / synthesis conclusions /
  any table other than the gate token.
Violated when: any output other than the EVIDENCE GATE token appears in GATEKEEPER output;
  or GATEKEEPER writes a token string not defined in the GATE TOKEN PROTOCOL block.
Constraint check: SCANNER COMPLETE token is present. If absent, halt before evaluating.
Org chart prohibition: gate token contains no org chart content.

Gate checklist — evaluate each item in order; do not skip:
1. At least 3 of 7 source types were scanned
2. TABLE B has at least 5 rows with File Path Evidence populated with distinct paths
3. All Inertia Match cells use I-01 through I-07 (no free text)
4. All Hypothesis Held cells use: yes / no / partial
5. Anti-fabrication confirmed: all FILE PATH cells reference files actually read
6. Hypothesis floor PASS token is present in Phase 1 / Phase 2 boundary output

Write exactly one token from GATE TOKEN PROTOCOL EVIDENCE GATE definition:
  PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
  FAIL: Path floor not met -- scan incomplete

---

GATEKEEPER / SYNTHESIZER BOUNDARY

GATEKEEPER exits. Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

GATEKEEPER PHASE COMPLETION PROOF:
- Gate checklist evaluated in full; no items skipped
- Exactly one token written; no prose substitution
- No prohibited outputs appear in GATEKEEPER section

---

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

ROLE SCOPE DECLARATION: SYNTHESIZER
PAF Authority: dictionary application in Phase 3 only — resolve predictions against labeled
  scan evidence; may draw synthesis conclusions from TABLE B evidence only.
Input Dependencies: TABLE B + TABLE C + TABLE D (from SCANNER) — all three must be present;
  evidence gate PASS token — must be present; TABLE A (from PREDICTOR) — must be present for
  TABLE G row-count assertion.
Permitted outputs: TABLE E / TABLE F / TABLE G / Org Shape paragraph / Headcount Range section.
Prohibited outputs: new scan evidence / raw file content not in TABLE B / TABLE A predictions
  (TABLE A is read-only input) / TABLE B rows (TABLE B is read-only input).
Violated when: any file path appears in SYNTHESIZER output that has no corresponding TABLE B
  row (new path introduced in Phase 3); or TABLE G Evidence Summary contains prose claims not
  traceable to a TABLE B row citation by row number.
Constraint check: Evidence gate PASS token is present. If absent, halt.
Org chart prohibition (stated in preamble; restated here): Raw analysis only. No org chart.
  No reporting lines. No hierarchy diagrams. No "reports to" statements. Producing any org
  chart content is a failure of this skill regardless of how complete the other sections are.

Entry condition: Evidence gate PASS token present.

ROW-COUNT ASSERTION (record before producing TABLE G):
Write: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."
[Replace [N] with the actual row count of TABLE A.]
This assertion is a named output in the execution trace. After producing TABLE G, verify:
TABLE G row count equals [N]. If not equal: add TABLE F gap entries for all unresolved
TABLE A Pattern IDs and write "SYNTHESIZER VERIFICATION: TABLE G row count mismatch --
TABLE A: [N] rows, TABLE G: [M] rows, [N-M] predictions unresolved."

-> Output TABLE E (minimum 2 rows per SCHEMA minimum rows declaration).
-> Output TABLE F.
-> Output TABLE G: for every TABLE A row, resolve both the structural prediction and the
   behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
   Completeness rule applies: every TABLE A Pattern ID must have a TABLE G row.
   Cross-phase attribution required: Predicted by = PREDICTOR; Evidence rows cited = [list
   TABLE B row numbers cited in Evidence Summary]; Resolved by = SYNTHESIZER.
-> Write Org Shape paragraph: name dominant pattern from EVIDENCE GATE PASS TOKEN. Separate
   CURRENT STATE (what the scan found) from RECOMMENDED STATE (what the org shape should be
   given the evidence). Justify from TABLE B structural and behavioral evidence. At least 2
   TABLE B row citations per state.
-> Write Headcount Range: total FTE range aggregated from TABLE C with rationale citing at
   least 2 TABLE C rows.

SYNTHESIS COMPLETENESS GATE -- evaluate after all outputs produced, before SYNTHESIZER COMPLETE:

Gate checklist:
1. TABLE G row count equals the [N] stated in the ROW-COUNT ASSERTION
2. Every TABLE A Pattern ID appears as a TABLE G Pattern ID
3. Every TABLE G Evidence Summary cell cites at least one TABLE B row number
4. No TABLE A prediction is left unresolved without a corresponding TABLE F gap entry
5. Org Shape paragraph contains CURRENT STATE and RECOMMENDED STATE sections
6. Headcount Range cites at least 2 TABLE C rows
7. TABLE E has at least 2 rows (minimum rows per SCHEMA)

Write exactly one token from GATE TOKEN PROTOCOL SYNTHESIS COMPLETENESS GATE definition:
  PASS: Synthesis complete -- TABLE G [N] rows = TABLE A [N] rows, all predictions resolved
  FAIL: Synthesis incomplete -- TABLE G [M] rows, TABLE A [N] rows, [N-M] predictions unresolved

FAIL TOKEN requires: add TABLE F gap entries for every unresolved TABLE A Pattern ID before
halting, then write the FAIL token.

Phase 3 exit: Write "SYNTHESIZER COMPLETE" after the synthesis completeness gate token.

SYNTHESIZER PHASE COMPLETION PROOF:
- PAF binding: all TABLE G resolutions anchor to dictionary pattern; Evidence Summary cites
  TABLE B rows
- Tables produced: TABLE E, TABLE F, TABLE G (matches schema assignments for SYNTHESIZER)
- Row-count assertion honored: TABLE G row count equals TABLE A row count stated in assertion
- Minimum rows satisfied: TABLE E >= 2, TABLE G >= TABLE A row count
- Constraint maintained: no org chart content in any output
- Synthesis completeness gate token written

---

SYNTHESIZER / END BOUNDARY

Skill complete.

---

GROUP D -- OUTPUT SUMMARY

Trace artifact (ground truth): No trace artifact. Use skill description and spec.

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations that made them better.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-02

**Variation axis**: `Output Consumers` declaration in each ROLE SCOPE DECLARATION. All
structure identical to V-01. Single change: each ROLE SCOPE DECLARATION adds an `Output
Consumers` property naming the downstream roles that depend on this role's outputs and which
tables they consume.

**Hypothesis**: C-59 requires a named `Input Dependencies` block in each role scope
declaration — the incoming edge of the dependency graph (what I need). Each role can name
its preconditions from its own scope declaration. But the outgoing edge (who needs me) is
not declared anywhere: to know which downstream role depends on PREDICTOR's TABLE A, a reader
must trace the instruction sequence or read SCANNER and SYNTHESIZER scope declarations.
`Output Consumers` adds the symmetric outgoing declaration — each role names its downstream
consumers and the specific tables they take. Together, `Input Dependencies` (incoming) and
`Output Consumers` (outgoing) make the full directed execution graph bidirectional: derivable
by reading any single role scope declaration and traversing in either direction, without
instruction-text traversal. A broken execution graph (e.g., a role added between SCANNER and
SYNTHESIZER) is structurally detectable because the `Output Consumers` of SCANNER would not
reference the new role, and the new role's `Input Dependencies` would not reference SCANNER.
Not captured by C-59 (incoming edges only). Candidate for C-64.

---

```
[All content identical to V-01 through GROUP A preamble, then:]

GROUP A -- PREDICTOR PHASE

Phase 1: Hypothesis Generation (Role: PREDICTOR)

ROLE SCOPE DECLARATION: PREDICTOR
PAF Authority: dictionary application in Phase 1 only — generate hypotheses anchored to
  named patterns; no analytical conclusions from scan evidence permitted in this phase.
Input Dependencies: none — PREDICTOR is the first role; no prior tables required.
Output Consumers: HYPOTHESIS FLOOR GATE (TABLE A — validated for prediction floor before
  SCANNER may begin); SYNTHESIZER (TABLE A — read-only for TABLE G row-count assertion and
  cross-phase attribution; TABLE G row count must match TABLE A row count).
Permitted outputs: TABLE A rows only.
Prohibited outputs: file reads / scan evidence / TABLE B / TABLE C / TABLE D / TABLE E /
  TABLE F / TABLE G / any content derived from reading files.
Violated when: any TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, or TABLE G row appears in
  PREDICTOR output; or any cell in TABLE A contains a specific file path or file content quote.
Constraint check: No file has been read since skill invocation. If any file has been read,
  halt and flag a PREDICTOR scope violation before producing TABLE A.
Org chart prohibition: TABLE A must contain no org chart content, no reporting lines, no
  "reports to" statements.

[Phase 1 instructions and PREDICTOR / SCANNER BOUNDARY identical to V-01, then:]

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

ROLE SCOPE DECLARATION: SCANNER
PAF Authority: dictionary application in Phase 2 only — label findings from files actually
  read; no synthesis conclusions or boundary recommendations permitted in this phase.
Input Dependencies: TABLE A (from PREDICTOR) — must be present; hypothesis floor pass token
  — must be present. SCANNER may not begin if either is absent.
Output Consumers: GATEKEEPER (TABLE B / TABLE C / TABLE D — evaluated for evidence gate
  passage; SCANNER COMPLETE token — required before gate evaluation begins); SYNTHESIZER
  (TABLE B / TABLE C / TABLE D — read-only inputs for all Phase 3 synthesis tables and
  narrative sections; no SYNTHESIZER output may cite paths or findings absent from TABLE B).
Permitted outputs: TABLE B / TABLE C / TABLE D.
Prohibited outputs: TABLE E / TABLE F / TABLE G / synthesis conclusions / team boundary
  recommendations / org shape determinations / headcount estimates.
Violated when: TABLE E, TABLE F, or TABLE G rows appear in SCANNER output; or Finding column
  in TABLE B contains synthesis language ("this means", "therefore", "the org should", "I
  recommend") rather than factual evidence from files read.
Constraint check: Hypothesis floor PASS token is present in output above. If absent, halt.
Org chart prohibition: TABLE B / TABLE C / TABLE D must contain no org chart content.

[SCANNER phase instructions identical to V-01, then:]

ROLE SCOPE DECLARATION: GATEKEEPER
PAF Authority: gate evaluation only — no analytical work, no finding generation, no synthesis.
Input Dependencies: TABLE B + TABLE C + TABLE D (from SCANNER) — all three must be present;
  SCANNER COMPLETE token — must be present.
Output Consumers: SYNTHESIZER (evidence gate PASS token — required as SYNTHESIZER entry
  condition; FAIL token halts the skill and SYNTHESIZER does not execute).
Permitted outputs: exactly one EVIDENCE GATE token (PASS or FAIL from GATE TOKEN PROTOCOL).
Prohibited outputs: TABLE E / TABLE F / TABLE G / analytical findings / synthesis conclusions /
  any table other than the gate token.
Violated when: any output other than the EVIDENCE GATE token appears in GATEKEEPER output;
  or GATEKEEPER writes a token string not defined in the GATE TOKEN PROTOCOL block.
Constraint check: SCANNER COMPLETE token is present. If absent, halt before evaluating.
Org chart prohibition: gate token contains no org chart content.

[Gate checklist, GATEKEEPER / SYNTHESIZER BOUNDARY identical to V-01, then:]

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

ROLE SCOPE DECLARATION: SYNTHESIZER
PAF Authority: dictionary application in Phase 3 only — resolve predictions against labeled
  scan evidence; may draw synthesis conclusions from TABLE B evidence only.
Input Dependencies: TABLE B + TABLE C + TABLE D (from SCANNER) — all three must be present;
  evidence gate PASS token — must be present; TABLE A (from PREDICTOR) — must be present for
  TABLE G row-count assertion.
Output Consumers: none — SYNTHESIZER is the terminal role; all outputs (TABLE E / TABLE F /
  TABLE G / Org Shape paragraph / Headcount Range) are skill artifacts with no downstream
  role dependency.
Permitted outputs: TABLE E / TABLE F / TABLE G / Org Shape paragraph / Headcount Range section.
Prohibited outputs: new scan evidence / raw file content not in TABLE B / TABLE A predictions
  (TABLE A is read-only input) / TABLE B rows (TABLE B is read-only input).
Violated when: any file path appears in SYNTHESIZER output that has no corresponding TABLE B
  row (new path introduced in Phase 3); or TABLE G Evidence Summary contains prose claims not
  traceable to a TABLE B row citation by row number.
Constraint check: Evidence gate PASS token is present. If absent, halt.
Org chart prohibition (stated in preamble; restated here): Raw analysis only. No org chart.
  No reporting lines. No hierarchy diagrams. No "reports to" statements.

[All SYNTHESIZER phase instructions, gates, boundaries, and GROUP D identical to V-01.]
```

---

## V-03

**Variation axis**: Named `COVERAGE ATTESTATION` structured table at SCANNER exit,
enumerating all 7 source types with per-type scan status. All structure identical to V-01.
Two changes: (a) SCANNER phase adds a `COVERAGE ATTESTATION` table production step before
SCANNER COMPLETE, (b) GATEKEEPER gate checklist item 1 references the COVERAGE ATTESTATION
table by name rather than re-evaluating independently.

**Hypothesis**: The EVIDENCE GATE pass token records `[N] sources scanned` as a count, but
not which specific source types were covered. A COVERAGE ATTESTATION table enumerates all 7
source types with per-type status (scanned / not-found / not-applicable), making the gap
between scanned and unscanned source types structurally visible as named rows rather than as
an implied difference between the declared count and 7. Critically, "not-found" (attempted
scan, source type absent in this repo) and "not-applicable" (source type structurally
inapplicable — e.g., no package.json in a pure-bash repo) are distinguishable as named states
rather than collapsed into a single "not scanned" absence. The GATEKEEPER can validate source
coverage by reading the COVERAGE ATTESTATION rather than re-inferring from TABLE B, making
the gate evaluation derive from a declared artifact rather than from an implicit count.
Not captured by C-02 (multi-source requirement) or C-08 (gap flagging) — those require
source coverage and gap identification in output; this requires a structured table declaring
the scan disposition of every source type so coverage is auditable by enumeration.
Candidate for C-65.

---

```
[All content identical to V-01 through SCANNER PHASE instructions, then after TABLE B/C/D
output step:]

COVERAGE ATTESTATION (produce before writing SCANNER COMPLETE):

For each of the 7 source types, record the scan disposition:

| Source Type | Status | Notes |
|---|---|---|
| 1. CLAUDE.md files (all levels) | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 2. package.json (root and nested) | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 3. design/ or docs/ directories | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 4. Namespace directories | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 5. Test coverage areas | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 6. SPECS.md or specification files | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 7. .craft/roles/ or role definition files | [scanned / not-found / not-applicable] | [paths read or reason absent] |

Scanned count: [N of 7 show "scanned"]
Not-found count: [N of 7 show "not-found"]
Not-applicable count: [N of 7 show "not-applicable"]

COVERAGE FLOOR: at least 3 source types must show "scanned" status. If fewer than 3:
halt — do not write SCANNER COMPLETE — write EVIDENCE GATE FAIL token directly.

Status definitions:
- scanned: attempted to read; found file(s); reading produced at least one TABLE B row.
- not-found: attempted to read; no matching files found in the repo.
- not-applicable: structurally absent from this repo type (e.g., no package.json in a
  non-Node repo); not attempted because not plausible.

Anti-fabrication: status must reflect actual file reads. Recording "scanned" for a source
type with no TABLE B row citing a path from that type is a COVERAGE ATTESTATION violation.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" after producing
the COVERAGE ATTESTATION.

[SCANNER PHASE COMPLETION PROOF updated to include:]
- COVERAGE ATTESTATION produced: [N] source types scanned, [N] not-found, [N] not-applicable

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

[Identical to V-01 except GATEKEEPER gate checklist item 1 reads:]

Gate checklist -- evaluate each item in order; do not skip:
1. COVERAGE ATTESTATION shows at least 3 source types with "scanned" status
[Items 2-6 identical to V-01.]

[All remaining content identical to V-01.]
```

---

## V-04

**Variation axis**: `TABLE H -- Org Shape Delta` in SYNTHESIZER output. All structure
identical to V-01. Three changes: (a) SCHEMA DECLARATION adds TABLE H definition with
`Minimum rows: 3`, (b) SYNTHESIZER phase replaces the Org Shape prose paragraph instruction
with a TABLE H production step that includes a prose wrapper, (c) SYNTHESIS COMPLETENESS GATE
checklist adds item 8 checking TABLE H minimum rows.

**Hypothesis**: The SYNTHESIZER currently produces an Org Shape paragraph with prose CURRENT
STATE and RECOMMENDED STATE sections. C-10 requires these sections to be separated, and the
rubric rewards the separation. But the gap between current and recommended is expressed in
prose — the per-dimension delta (what changed, what stayed, what is recommended to change) is
not structured. TABLE H extracts the delta into a 4-column schema (Dimension | Current State |
Recommended State | Driving Evidence), making every recommended-state claim cite a TABLE B row
and making the delta between current and recommended inspectable at the cell level rather than
requiring prose interpretation. The Org Shape paragraph becomes a narrative wrapper that
introduces TABLE H rather than the sole carrier of the structured comparison. This is not
captured by C-10 (which requires CURRENT/RECOMMENDED separation in prose), C-07 (which
requires org shape naming and justification), or C-13 (which restates the CRITICAL CONSTRAINT
in the SYNTHESIZER scope) — TABLE H makes the per-dimension recommendation structurally
queryable, not just narratively present. Candidate for C-66.

---

```
[All content identical to V-01 through SCHEMA DECLARATION, then TABLE G definition is
followed by:]

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after TABLE G.

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED (cite TABLE B row) |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row) |

Minimum rows: 3 (at least 3 dimensions required: structural shape, team boundaries, and
headcount signal. A TABLE H with fewer than 3 rows is an org shape analysis gap).

Org chart prohibition: TABLE H must contain no org chart content, no reporting lines, no
"reports to" statements. TABLE H is a delta analysis of current vs recommended org shape —
not an org chart.

[All content identical to V-01 through SYNTHESIZER phase, then the Org Shape paragraph
instruction is replaced with:]

-> Write TABLE H: produce at least 3 rows covering structural shape, team boundaries, and
   headcount signal as distinct dimensions. Every Current State cell must cite a TABLE B row.
   Every Driving Evidence cell must cite a TABLE B row. Recommended State may be prose but
   must not introduce org chart content.
-> Write Org Shape narrative: a paragraph introducing TABLE H and naming the dominant pattern
   from the EVIDENCE GATE PASS TOKEN. The narrative references TABLE H rows by dimension name
   (e.g., "On the structural shape dimension [see TABLE H row 1]..."). This narrative is the
   wrapper; TABLE H is the primary structured output.

[SYNTHESIS COMPLETENESS GATE checklist updated to add:]
8. TABLE H has at least 3 rows with all Current State and Driving Evidence cells citing
   TABLE B row numbers

[All other content identical to V-01.]
```

---

## V-05

**Variation axis**: Full combination of V-02 + V-03 + V-04. All three new axes active
simultaneously: (a) `Output Consumers` in each ROLE SCOPE DECLARATION, (b) `COVERAGE
ATTESTATION` table at SCANNER exit, (c) `TABLE H -- Org Shape Delta` in SYNTHESIZER.

**Hypothesis**: The three axes operate at different layers of the skill. `Output Consumers`
(V-02) makes the execution dependency graph bidirectional at the declaration layer. `COVERAGE
ATTESTATION` (V-03) makes source type coverage auditable by enumeration at the SCANNER exit
boundary. `TABLE H` (V-04) makes the org shape recommendation structurally queryable at the
output layer. Together they close three remaining structural gaps: who depends on whom
(bidirectional declaration), what was attempted and what was absent (per-type coverage table),
and what is being recommended per dimension (structured delta table). Whether this combination
produces a new multi-signal synthesis criterion or surfaces interactions is an empirical
question this combination tests.

---

```
CRITICAL CONSTRAINT (stated here; restated in SYNTHESIZER scope declaration): This skill
produces raw analysis only. No org chart. No reporting lines. No hierarchy diagrams. No
"reports to" statements. Producing any org chart content is a failure of this skill regardless
of how complete the other sections are.

---

SCHEMA DECLARATION

This schema governs every table in this skill. Status applies to every column.

TABLE A -- Hypothesis Table
Produced by: PREDICTOR before any scan evidence is collected.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction | REQUIRED |
| Behavioral Prediction | REQUIRED |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Minimum rows: 6 (one row per I-01, I-02, I-03, I-04, I-05, I-06 — one prediction per
dictionary pattern). A TABLE A with fewer than 6 rows is a prediction-coverage gap.

TABLE B -- Scan Evidence Table
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Area | REQUIRED |
| Source Type | REQUIRED |
| Finding | REQUIRED |
| Inertia Match | REQUIRED (dictionary value only — I-01 through I-07) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a schema
violation.

Minimum rows: 5 (path floor — each row must cite a distinct File Path Evidence value).
Rows below this floor block evidence gate passage.

TABLE C -- Headcount Signals
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

Minimum rows: 2 (at least 2 distinct expertise domains to support headcount range rationale).

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

Minimum rows: 1 (at least one cross-cutting concern must be identified or explicitly recorded
as absent with source types checked noted in TABLE F).

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row) |
| Supporting Evidence | REQUIRED |

Minimum rows: 2 (at least 2 boundary candidates required for meaningful seam analysis).

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

Minimum rows: none declared (gaps are evidence-dependent; absence of TABLE F rows is valid
if the scan is complete and all predictions are resolved).

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Evidence Summary | REQUIRED (cite TABLE B row) |
| Resolution | REQUIRED (yes / no / partial) |
| Predicted by | REQUIRED (PREDICTOR) |
| Evidence rows cited | REQUIRED (TABLE B row references) |
| Resolved by | REQUIRED (SYNTHESIZER) |

Minimum rows: equal to TABLE A row count (enforced by row-count assertion at SYNTHESIZER
entry). Mismatch between TABLE G row count and TABLE A row count is a structurally detectable
omission.

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Remediate: add TABLE F row with Gap set to
"[PATTERN-ID] prediction unresolved", Implication set to "hypothesis not tested against scan
evidence", Source Types Checked set to the source types that were scanned. No prediction may
remain unresolved without a TABLE F gap entry.

Row-count invariant: TABLE G row count must equal TABLE A row count. A row-count mismatch
is a structurally detectable omission — identifiable by table correspondence alone.

TABLE H -- Org Shape Delta
Produced by: SYNTHESIZER after TABLE G.

| Column | Status |
|---|---|
| Dimension | REQUIRED |
| Current State | REQUIRED (cite TABLE B row) |
| Recommended State | REQUIRED |
| Driving Evidence | REQUIRED (cite TABLE B row) |

Minimum rows: 3 (dimensions required: structural shape, team boundaries, headcount signal).

Org chart prohibition: TABLE H must contain no org chart content, no reporting lines, no
"reports to" statements. TABLE H captures the delta between current and recommended org shape
— not the org shape itself.

---

GATE TOKEN PROTOCOL

This block defines all named gate tokens before Phase 1 begins. Every gate in this skill must
write exactly one of its defined tokens. No prose substitution.

HYPOTHESIS FLOOR GATE (Phase 1 / Phase 2 boundary):
  PASS: Hypothesis floor clear -- [N] predictions recorded, [N] distinct pattern codes covered
  FAIL: Hypothesis floor not met -- fewer than 3 predictions or fewer than 2 distinct pattern codes

EVIDENCE GATE (Phase 2 / Phase 3 boundary):
  PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
  FAIL: Path floor not met -- scan incomplete

SYNTHESIS COMPLETENESS GATE (Phase 3 exit):
  PASS: Synthesis complete -- TABLE G [N] rows = TABLE A [N] rows, all predictions resolved
  FAIL: Synthesis incomplete -- TABLE G [M] rows, TABLE A [N] rows, [N-M] predictions unresolved

One token from each gate's pair must appear at its corresponding boundary. No prose substitution
for any gate.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from prediction
through verification through synthesis, with each named role applying it in its assigned phase:

- PREDICTOR applies it in Phase 1 to generate hypotheses — each TABLE A prediction must anchor
  to a dictionary pattern before any file is read.
- SCANNER applies it in Phase 2 to label every TABLE B finding — the Inertia Match column is
  the per-row application of this framework to scan evidence.
- SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction against labeled TABLE B
  evidence — every TABLE G row must name the pattern predicted, cite the evidence, and state
  the resolution.

The dictionary is not a post-hoc classifier. It is the analytical lens through which each named
role executes its phase of the investigation.

Free text in the Inertia Match column is structurally invalid. Unconstrained values make pattern
comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, incident response patterns).
PREDICTOR must predict both registers. SCANNER must check both.

| Pattern ID | Pattern Name | Structural Code Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith | Single root package.json; flat directory structure; no namespace separation; all tests in one directory; no per-area CLAUDE.md | "we all work on the same thing"; any engineer opens any file; bugs have no natural owner; on-call is "everyone"; onboarding means shadowing the whole codebase |
| I-02 | Accidental Silos | Multiple directories exist but no explicit ownership documentation; test coverage overlaps across directories; no seam-respecting PR convention | "not sure who owns that"; cross-area PRs stall without a clear reviewer; incidents involve multiple teams guessing; "we should probably document this" is a recurring sentiment |
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain test directories; explicit ownership declared in docs or .craft/roles | "that's the X team's area"; clear escalation path per domain; engineers onboard to a single domain first; incidents have a natural first responder; PRs stay within domain seams |
| I-04 | Platform + Product | Shared infra layer (sdk/, core/, utils/, platform/) clearly distinct from product surfaces; infra layer has its own CLAUDE.md and dedicated test coverage | "we build on the platform"; platform team has separate on-call rotation; product features rarely touch infra; platform changes require a coordination meeting; "the platform team owns that" |
| I-05 | Federated | Multiple autonomous workspaces, packages, or repos with minimal shared root; independent CI per workspace; rare central merge events | "each team ships independently"; integration is opt-in; shared tooling is a separate small team; incidents are scoped to one workspace; "we don't need to coordinate on that" |
| I-06 | Hub-and-Spoke | Central orchestrator directory (nexus/, hub/, core/, router/) with peripheral plugin or service directories radiating from it; hub has disproportionate test coverage and documentation depth | "everything routes through the hub"; hub team is the bottleneck for peripheral changes; peripheral teams file issues against the hub; "we need the hub team to merge this first"; hub engineers are stretched thin |
| I-07 | Undefined | Fewer than 3 source types were readable; evidence is insufficient to classify | Cannot assess behavioral signals; pattern classification deferred |

---

GROUP A -- PREDICTOR PHASE

Phase 1: Hypothesis Generation (Role: PREDICTOR)

ROLE SCOPE DECLARATION: PREDICTOR
PAF Authority: dictionary application in Phase 1 only — generate hypotheses anchored to
  named patterns; no analytical conclusions from scan evidence permitted in this phase.
Input Dependencies: none — PREDICTOR is the first role; no prior tables required.
Output Consumers: HYPOTHESIS FLOOR GATE (TABLE A — validated for prediction floor before
  SCANNER may begin); SYNTHESIZER (TABLE A — read-only for TABLE G row-count assertion and
  cross-phase attribution; TABLE G row count must match TABLE A row count).
Permitted outputs: TABLE A rows only.
Prohibited outputs: file reads / scan evidence / TABLE B / TABLE C / TABLE D / TABLE E /
  TABLE F / TABLE G / TABLE H / any content derived from reading files.
Violated when: any TABLE B, TABLE C, TABLE D, TABLE E, TABLE F, TABLE G, or TABLE H row
  appears in PREDICTOR output; or any cell in TABLE A contains a specific file path or file
  content quote.
Constraint check: No file has been read since skill invocation. If any file has been read,
  halt and flag a PREDICTOR scope violation before producing TABLE A.
Org chart prohibition: TABLE A must contain no org chart content, no reporting lines, no
  "reports to" statements.

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction (what code-level signals you expect to find or not find) and a behavioral
prediction (what team-language or ownership signals you expect to find in CLAUDE.md prose). Set
Hypothesis Held to your expectation before evidence.

You are the PREDICTOR. Making both predictions forces the inertia dictionary to be falsifiable
at both registers — structural and behavioral. Do not read any files during this phase.

-> Output TABLE A (minimum 6 rows per SCHEMA minimum rows declaration).

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

PREDICTOR PHASE COMPLETION PROOF:
- PAF binding: Inertia Pattern Dictionary applied in Phase 1 prediction only
- Tables produced: TABLE A (matches schema assignment: "Produced by: PREDICTOR")
- Minimum rows satisfied: [N] rows in TABLE A meets minimum of 6
- No file reads occurred during Phase 1

---

PREDICTOR / SCANNER BOUNDARY

This boundary is the postcondition of Phase 1 and the precondition of Phase 2. Both sides
name the same contract. Both must hold.

PREDICTOR exits. Control transfers to HYPOTHESIS FLOOR GATE evaluation. TABLE A must exist.

HYPOTHESIS FLOOR GATE -- evaluate before SCANNER may begin:

Gate checklist:
1. TABLE A is present and non-empty
2. TABLE A contains at least 3 rows (predictions)
3. TABLE A contains at least 2 distinct Pattern IDs (prediction coverage spans multiple patterns)
4. Every Hypothesis Held cell uses: yes / no / partial
5. No file evidence appears in any TABLE A cell

Write exactly one token:
  PASS: Hypothesis floor clear -- [N] predictions recorded, [N] distinct pattern codes covered
  FAIL: Hypothesis floor not met -- fewer than 3 predictions or fewer than 2 distinct pattern codes

FAIL TOKEN halts execution. SCANNER may not begin until PASS token is written.

---

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

ROLE SCOPE DECLARATION: SCANNER
PAF Authority: dictionary application in Phase 2 only — label findings from files actually
  read; no synthesis conclusions or boundary recommendations permitted in this phase.
Input Dependencies: TABLE A (from PREDICTOR) — must be present; hypothesis floor pass token
  — must be present. SCANNER may not begin if either is absent.
Output Consumers: GATEKEEPER (TABLE B / TABLE C / TABLE D / COVERAGE ATTESTATION — evaluated
  for evidence gate passage; SCANNER COMPLETE token — required before gate evaluation begins);
  SYNTHESIZER (TABLE B / TABLE C / TABLE D — read-only inputs for all Phase 3 synthesis tables
  and narrative sections; no SYNTHESIZER output may cite paths absent from TABLE B).
Permitted outputs: TABLE B / TABLE C / TABLE D / COVERAGE ATTESTATION.
Prohibited outputs: TABLE E / TABLE F / TABLE G / TABLE H / synthesis conclusions / team
  boundary recommendations / org shape determinations / headcount estimates.
Violated when: TABLE E, TABLE F, TABLE G, or TABLE H rows appear in SCANNER output; or
  Finding column in TABLE B contains synthesis language ("this means", "therefore", "the org
  should", "I recommend") rather than factual evidence from files read.
Constraint check: Hypothesis floor PASS token is present in output above. If absent, halt.
Org chart prohibition: TABLE B / TABLE C / TABLE D must contain no org chart content.

Entry condition: PREDICTOR COMPLETE present. Hypothesis floor PASS token present. TABLE A
exists.

Anti-fabrication: Report only findings from files actually read. Record absences explicitly.
Do not infer from file names. Cite only paths that exist.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .craft/roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language
-- these are behavioral signal evidence for TABLE B Behavioral Signals and Hypothesis Held.

File path floor (gate precondition): TABLE B must contain at least 5 rows with File Path
Evidence populated with distinct file paths. This requirement blocks gate passage if unmet.

-> Output TABLE B (minimum 5 rows per SCHEMA minimum rows declaration).
-> Output TABLE C (minimum 2 rows per SCHEMA minimum rows declaration).
-> Output TABLE D (minimum 1 row per SCHEMA minimum rows declaration, or TABLE F gap entry
   if no cross-cutting concerns found).

COVERAGE ATTESTATION (produce before writing SCANNER COMPLETE):

For each of the 7 source types, record the scan disposition:

| Source Type | Status | Notes |
|---|---|---|
| 1. CLAUDE.md files (all levels) | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 2. package.json (root and nested) | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 3. design/ or docs/ directories | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 4. Namespace directories | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 5. Test coverage areas | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 6. SPECS.md or specification files | [scanned / not-found / not-applicable] | [paths read or reason absent] |
| 7. .craft/roles/ or role definition files | [scanned / not-found / not-applicable] | [paths read or reason absent] |

Scanned count: [N of 7 show "scanned"]
Not-found count: [N of 7 show "not-found"]
Not-applicable count: [N of 7 show "not-applicable"]

COVERAGE FLOOR: at least 3 source types must show "scanned" status. If fewer than 3:
halt — do not write SCANNER COMPLETE — write EVIDENCE GATE FAIL token directly.

Status definitions:
- scanned: attempted to read; found file(s); reading produced at least one TABLE B row.
- not-found: attempted to read; no matching files found in the repo.
- not-applicable: structurally absent from this repo type (e.g., no package.json in a
  non-Node repo); not attempted because not plausible.

Anti-fabrication: status must reflect actual file reads. Recording "scanned" for a source
type with no TABLE B row citing a path from that type is a COVERAGE ATTESTATION violation.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" after the
COVERAGE ATTESTATION.

SCANNER PHASE COMPLETION PROOF:
- PAF binding: all Inertia Match cells use dictionary values I-01 through I-07; no free text
- Tables produced: TABLE B, TABLE C, TABLE D (matches schema assignments for SCANNER)
- Anti-fabrication confirmed: all File Path Evidence cells reference files actually read
- Minimum rows satisfied: TABLE B >= 5, TABLE C >= 2
- COVERAGE ATTESTATION produced: [N] source types scanned, [N] not-found, [N] not-applicable

---

SCANNER / GATEKEEPER BOUNDARY: EVIDENCE GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name
the same contract. Both must hold.

SCANNER exits. GATEKEEPER begins.

ROLE SCOPE DECLARATION: GATEKEEPER
PAF Authority: gate evaluation only — no analytical work, no finding generation, no synthesis.
Input Dependencies: TABLE B + TABLE C + TABLE D + COVERAGE ATTESTATION (from SCANNER) — all
  must be present; SCANNER COMPLETE token — must be present.
Output Consumers: SYNTHESIZER (evidence gate PASS token — required as SYNTHESIZER entry
  condition; FAIL token halts the skill and SYNTHESIZER does not execute).
Permitted outputs: exactly one EVIDENCE GATE token (PASS or FAIL from GATE TOKEN PROTOCOL).
Prohibited outputs: TABLE E / TABLE F / TABLE G / TABLE H / analytical findings / synthesis
  conclusions / any table other than the gate token.
Violated when: any output other than the EVIDENCE GATE token appears in GATEKEEPER output;
  or GATEKEEPER writes a token string not defined in the GATE TOKEN PROTOCOL block.
Constraint check: SCANNER COMPLETE token is present. If absent, halt before evaluating.
Org chart prohibition: gate token contains no org chart content.

Gate checklist -- evaluate each item in order; do not skip:
1. COVERAGE ATTESTATION shows at least 3 source types with "scanned" status
2. TABLE B has at least 5 rows with File Path Evidence populated with distinct paths
3. All Inertia Match cells use I-01 through I-07 (no free text)
4. All Hypothesis Held cells use: yes / no / partial
5. Anti-fabrication confirmed: all FILE PATH cells reference files actually read
6. Hypothesis floor PASS token is present in Phase 1 / Phase 2 boundary output

Write exactly one token from GATE TOKEN PROTOCOL EVIDENCE GATE definition:
  PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
  FAIL: Path floor not met -- scan incomplete

---

GATEKEEPER / SYNTHESIZER BOUNDARY

GATEKEEPER exits. Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

GATEKEEPER PHASE COMPLETION PROOF:
- Gate checklist evaluated in full; no items skipped
- Exactly one token written; no prose substitution
- No prohibited outputs appear in GATEKEEPER section

---

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

ROLE SCOPE DECLARATION: SYNTHESIZER
PAF Authority: dictionary application in Phase 3 only — resolve predictions against labeled
  scan evidence; may draw synthesis conclusions from TABLE B evidence only.
Input Dependencies: TABLE B + TABLE C + TABLE D (from SCANNER) — all three must be present;
  evidence gate PASS token — must be present; TABLE A (from PREDICTOR) — must be present for
  TABLE G row-count assertion.
Output Consumers: none — SYNTHESIZER is the terminal role; all outputs (TABLE E / TABLE F /
  TABLE G / TABLE H / Org Shape narrative / Headcount Range) are skill artifacts with no
  downstream role dependency.
Permitted outputs: TABLE E / TABLE F / TABLE G / TABLE H / Org Shape narrative / Headcount
  Range section.
Prohibited outputs: new scan evidence / raw file content not in TABLE B / TABLE A predictions
  (TABLE A is read-only input) / TABLE B rows (TABLE B is read-only input).
Violated when: any file path appears in SYNTHESIZER output that has no corresponding TABLE B
  row (new path introduced in Phase 3); or TABLE G Evidence Summary contains prose claims not
  traceable to a TABLE B row citation by row number.
Constraint check: Evidence gate PASS token is present. If absent, halt.
Org chart prohibition (stated in preamble; restated here): Raw analysis only. No org chart.
  No reporting lines. No hierarchy diagrams. No "reports to" statements. Producing any org
  chart content is a failure of this skill regardless of how complete the other sections are.

Entry condition: Evidence gate PASS token present.

ROW-COUNT ASSERTION (record before producing TABLE G):
Write: "TABLE A count: [N] -- TABLE G must contain exactly [N] rows."
[Replace [N] with the actual row count of TABLE A.]
This assertion is a named output in the execution trace. After producing TABLE G, verify:
TABLE G row count equals [N]. If not equal: add TABLE F gap entries for all unresolved
TABLE A Pattern IDs and write "SYNTHESIZER VERIFICATION: TABLE G row count mismatch --
TABLE A: [N] rows, TABLE G: [M] rows, [N-M] predictions unresolved."

-> Output TABLE E (minimum 2 rows per SCHEMA minimum rows declaration).
-> Output TABLE F.
-> Output TABLE G: for every TABLE A row, resolve both the structural prediction and the
   behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
   Completeness rule applies: every TABLE A Pattern ID must have a TABLE G row.
   Cross-phase attribution required: Predicted by = PREDICTOR; Evidence rows cited = [list
   TABLE B row numbers cited in Evidence Summary]; Resolved by = SYNTHESIZER.
-> Output TABLE H: produce at least 3 rows covering structural shape, team boundaries, and
   headcount signal as named dimensions. Every Current State cell must cite a TABLE B row.
   Every Driving Evidence cell must cite a TABLE B row. Recommended State may be prose but
   must not introduce org chart content.
-> Write Org Shape narrative: a paragraph introducing TABLE H, naming the dominant pattern
   from the EVIDENCE GATE PASS TOKEN, and referencing TABLE H rows by dimension name. The
   narrative is the wrapper; TABLE H is the primary structured delta artifact.
-> Write Headcount Range: total FTE range aggregated from TABLE C with rationale citing at
   least 2 TABLE C rows.

SYNTHESIS COMPLETENESS GATE -- evaluate after all outputs produced, before SYNTHESIZER COMPLETE:

Gate checklist:
1. TABLE G row count equals the [N] stated in the ROW-COUNT ASSERTION
2. Every TABLE A Pattern ID appears as a TABLE G Pattern ID
3. Every TABLE G Evidence Summary cell cites at least one TABLE B row number
4. No TABLE A prediction is left unresolved without a corresponding TABLE F gap entry
5. Org Shape narrative references TABLE H by dimension name
6. Headcount Range cites at least 2 TABLE C rows
7. TABLE E has at least 2 rows (minimum rows per SCHEMA)
8. TABLE H has at least 3 rows with all Current State and Driving Evidence cells citing
   TABLE B row numbers

Write exactly one token from GATE TOKEN PROTOCOL SYNTHESIS COMPLETENESS GATE definition:
  PASS: Synthesis complete -- TABLE G [N] rows = TABLE A [N] rows, all predictions resolved
  FAIL: Synthesis incomplete -- TABLE G [M] rows, TABLE A [N] rows, [N-M] predictions unresolved

FAIL TOKEN requires: add TABLE F gap entries for every unresolved TABLE A Pattern ID before
halting, then write the FAIL token.

Phase 3 exit: Write "SYNTHESIZER COMPLETE" after the synthesis completeness gate token.

SYNTHESIZER PHASE COMPLETION PROOF:
- PAF binding: all TABLE G resolutions anchor to dictionary pattern; Evidence Summary cites
  TABLE B rows
- Tables produced: TABLE E, TABLE F, TABLE G, TABLE H (matches schema assignments)
- Row-count assertion honored: TABLE G row count equals TABLE A row count stated in assertion
- Minimum rows satisfied: TABLE E >= 2, TABLE G >= TABLE A row count, TABLE H >= 3
- Constraint maintained: no org chart content in any output
- Synthesis completeness gate token written

---

SYNTHESIZER / END BOUNDARY

Skill complete.

---

GROUP D -- OUTPUT SUMMARY

Trace artifact (ground truth): No trace artifact. Use skill description and spec.

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations that made them better.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## Axis Summary

| Variation | C-61 | C-62 | C-63 | Output Consumers (V-02) | Coverage Attestation (V-03) | TABLE H Delta (V-04) |
|---|---|---|---|---|---|---|
| V-01 | YES | YES | YES | NO | NO | NO |
| V-02 | YES | YES | YES | YES | NO | NO |
| V-03 | YES | YES | YES | NO | YES | NO |
| V-04 | YES | YES | YES | NO | NO | YES |
| V-05 | YES | YES | YES | YES | YES | YES |
```

---

**What's new in R17 vs R16:**

| Axis | Signal | Candidate |
|---|---|---|
| V-02 | `Output Consumers` in ROLE SCOPE DECLARATION — symmetric outgoing counterpart to C-59's `Input Dependencies`, making the execution dependency graph fully bidirectional from any single role declaration | C-64 |
| V-03 | Named `COVERAGE ATTESTATION` table enumerating all 7 source types with per-type status (scanned / not-found / not-applicable) — makes source gap visible by type, not just by count | C-65 |
| V-04 | `TABLE H -- Org Shape Delta` — structured 4-column table extracting the per-dimension gap between CURRENT STATE and RECOMMENDED STATE, with every recommended-state claim citing TABLE B evidence | C-66 |

V-05 is the richest variation. The three axes close gaps at three distinct layers: **declaration** (bidirectional dependency graph), **boundary** (per-type source attestation), and **output** (structured recommendation delta).
