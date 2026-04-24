I now have a complete picture of the R15 state-of-art (all 5 variations at 100/100, three new excellence signals crystallized into C-58/C-59/C-60). Writing the R16 variations.

---

```markdown
---
skill: quest-variate
skill_target: org-scan
round: 16
date: 2026-03-16
rubric_version: 16
---

# org-scan Skill Body Prompt Variations V-01 through V-05
## Targeting rubric v16 (C-01 through C-60)
## Round 16 — 2026-03-16

R15 produced C-58 (V-01: execution-time row-count assertion at SYNTHESIZER entry before TABLE G is
produced), C-59 (V-02: named `Input Dependencies` block inside each ROLE SCOPE DECLARATION), and
C-60 (V-03: GATE TOKEN PROTOCOL preamble covers every named gate — both hypothesis floor and
evidence floor). All three are structural invariants for R16: every variation must include them.

R16 explores three new axes beyond C-60 to surface the next wave of excellence signals:

- **Axis 1** (V-02): Output format — per-table minimum row floor declared as a named `Minimum rows:`
  annotation in SCHEMA DECLARATION for every table that has a quantifiable floor. Hypothesis:
  TABLE A's row floor (one row per I-01 through I-06) exists only as an instruction obligation;
  TABLE B's path floor is enforced at the gate; TABLE G's row floor is enforced at SYNTHESIZER
  entry. A `Minimum rows:` annotation in SCHEMA makes all row floor obligations co-located in one
  place, making the SCHEMA a combined type contract and quantitative contract simultaneously.
  Candidate for C-61.

- **Axis 2** (V-03): Lifecycle emphasis — third named gate: SYNTHESIS COMPLETENESS GATE at
  SYNTHESIZER exit. The gate checks the C-58 N=N assertion and produces a third named token.
  All three gates defined in GATE TOKEN PROTOCOL preamble. Hypothesis: C-60 extends gate token
  coverage to all named gates; V-03's hypothesis floor gate created a Phase 1 exit gate symmetric
  to the Phase 2 evidence gate. A Phase 3 synthesis completeness gate would complete the
  three-phase gating structure — each phase exits through a named machine-parseable gate, making
  Phase 3 as structurally auditable as Phase 1 and Phase 2. Candidate for C-61.

- **Axis 3** (V-04): Phrasing register — named `Violated when:` entry in each ROLE SCOPE
  DECLARATION naming the exact structural output signature that constitutes scope violation for
  that role. Distinct from `Prohibited outputs:` (prohibition list) — `Violated when:` names a
  detectable structural condition that, if present in the output, marks a scope breach without
  reading instruction text. Hypothesis: C-56 names PREDICTOR's prohibited outputs as a list.
  A `Violated when:` entry transforms the prohibition list into an auditable violation detector
  per role — scope creep is identifiable by matching output artifacts against named violation
  signatures. Candidate for C-61.

V-01 is the baseline embedding all three new invariants (C-58 + C-59 + C-60). V-02/V-03/V-04
test one new axis each. V-05 combines all three.

---

## Variation Axes

| Axis | Used In |
|---|---|
| Baseline v16 — all C-58/C-59/C-60 invariants, no new axis | V-01 |
| Per-table minimum row floor in SCHEMA DECLARATION | V-02 |
| Synthesis Completeness Gate at SYNTHESIZER exit (third gate) | V-03 |
| `Violated when:` violation signature in each ROLE SCOPE DECLARATION | V-04 |
| Full combination (V-02 + V-03 + V-04) | V-05 |

---

## V-01

**Variation axis**: Baseline v16. All three new criteria (C-58, C-59, C-60) are present as
structural invariants embedded alongside the full invariant stack (C-01 through C-57). No new
axis applied. This is the control condition: every R15 structural element is preserved and
fully written out.

**Hypothesis**: V-01 achieves 100/100 under the v16 rubric by treating C-58, C-59, and C-60
as structural invariants. V-02 through V-05 are tested against this ceiling — their value lies
in the excellence signals they produce for potential C-61+ criteria. V-01 is the baseline that
makes those signals visible by contrast.

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

TABLE C -- Headcount Signals
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Expertise Domain | REQUIRED |
| Signal Evidence | REQUIRED |
| File Path | REQUIRED |
| FTE Range | REQUIRED (range, not point value) |

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2 evidence collection.

| Column | Status |
|---|---|
| Concern | REQUIRED |
| Boundary Note | REQUIRED |
| File Path Evidence | REQUIRED |

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Boundary Candidate | REQUIRED |
| Seam Rationale | REQUIRED (cite TABLE B row) |
| Supporting Evidence | REQUIRED |

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.

| Column | Status |
|---|---|
| Gap | REQUIRED |
| Implication | REQUIRED |
| Source Types Checked | REQUIRED |

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

One token from each gate's pair must appear at the corresponding phase boundary. No prose
substitution for either gate.

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
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain test directories; explicit ownership declared in docs or .roles | "that's the X team's area"; clear escalation path per domain; engineers onboard to a single domain first; incidents have a natural first responder; PRs stay within domain seams |
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

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

PREDICTOR PHASE COMPLETION PROOF:
- PAF binding: Inertia Pattern Dictionary applied in Phase 1 prediction only
- Tables produced: TABLE A (matches schema assignment: "Produced by: PREDICTOR")
- No file reads occurred during Phase 1

---

PREDICTOR / SCANNER BOUNDARY

This boundary is the postcondition of Phase 1 and the precondition of Phase 2. Both sides
name the same contract. Both must hold.

PREDICTOR exits. Control transfers to HYPOTHESIS FLOOR GATE evaluation. TABLE A must exist.

HYPOTHESIS FLOOR GATE — evaluate before SCANNER may begin:

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
7. .roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language
— these are behavioral signal evidence for TABLE B Behavioral Signals and Hypothesis Held.

File path floor (gate precondition): TABLE B must contain at least 5 rows with File Path
Evidence populated with distinct file paths. This requirement blocks gate passage if unmet.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" before proceeding.

SCANNER PHASE COMPLETION PROOF:
- PAF binding: Inertia Pattern Dictionary applied in Phase 2 labeling — all Inertia Match
  cells use dictionary values I-01 through I-07; no free text
- Tables produced: TABLE B, TABLE C, TABLE D (matches schema assignments for SCANNER)
- Anti-fabrication confirmed: all File Path Evidence cells reference files actually read

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
Constraint check: Evidence gate PASS token is present. If absent, halt.
Org chart prohibition (stated in preamble; restated here): Raw analysis only. No org chart.
  No reporting lines. No hierarchy diagrams. No "reports to" statements. Producing any org
  chart content is a failure of this skill regardless of how complete the other sections are.

Entry condition: Evidence gate PASS token present.

ROW-COUNT ASSERTION (record before producing TABLE G):
Write: "TABLE A count: [N] — TABLE G must contain exactly [N] rows."
[Replace [N] with the actual row count of TABLE A.]
This assertion is a named output in the execution trace. After producing TABLE G, verify:
TABLE G row count equals [N]. If not equal: add TABLE F gap entries for all unresolved
TABLE A Pattern IDs and write "SYNTHESIZER VERIFICATION: TABLE G row count mismatch --
TABLE A: [N] rows, TABLE G: [M] rows, [N-M] predictions unresolved."

-> Output TABLE E, TABLE F.
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

Phase 3 exit: Write "SYNTHESIZER COMPLETE" before proceeding.

SYNTHESIZER PHASE COMPLETION PROOF:
- PAF binding: all TABLE G resolutions anchor to dictionary pattern; Evidence Summary cites
  TABLE B rows
- Tables produced: TABLE E, TABLE F, TABLE G (matches schema assignments for SYNTHESIZER)
- Row-count assertion honored: TABLE G row count equals TABLE A row count stated in assertion
- Constraint maintained: no org chart content in any output

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

**Variation axis**: Per-table minimum row floor in SCHEMA DECLARATION. All structure identical
to V-01. Single change: every table in the SCHEMA DECLARATION that has a quantifiable row
floor adds a `Minimum rows:` annotation below the column schema.

**Hypothesis**: TABLE A's row floor (one per I-01 through I-06 = 6 rows minimum) is enforced
only by instruction ("for each pattern I-01 through I-06"). TABLE B's path floor is enforced
at the evidence gate checklist (item 2). TABLE G's row floor is enforced by the C-58 row-count
assertion. All three obligations exist but are distributed: instruction, gate, execution-time
assertion. A `Minimum rows:` annotation in SCHEMA co-locates all row floor obligations in the
type contract, making the SCHEMA DECLARATION a combined type + quantitative contract. A reader
can derive both the column structure and the minimum row count for every table from the SCHEMA
alone. This is not captured by C-55 (schema-level row-count mismatch detectability) or C-58
(execution-time assertion), which are enforcement mechanisms — the new pattern is a declarative
co-location of all floor obligations. Candidate for C-61.

---

```
[All content identical to V-01 through SCHEMA DECLARATION header, then:]

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

[Column schema identical to V-01.]

Minimum rows: 2 (at least 2 distinct expertise domains to support headcount range rationale).

TABLE D -- Cross-Cutting Concerns
Produced by: SCANNER during Phase 2 evidence collection.

[Column schema identical to V-01.]

Minimum rows: 1 (at least one cross-cutting concern must be identified or explicitly recorded
as absent with the source types checked).

TABLE E -- Team Boundary Candidates
Produced by: SYNTHESIZER after gate passage.

[Column schema identical to V-01.]

Minimum rows: 2 (at least 2 boundary candidates required for meaningful seam analysis;
single-candidate output is a structural gap).

TABLE F -- Evidence Gaps
Produced by: SYNTHESIZER after gate passage.

[Column schema identical to V-01.]

Minimum rows: none declared (gaps are evidence-dependent; absence of TABLE F rows is valid
if the scan is complete and all predictions are resolved).

TABLE G -- Prediction Resolution
Produced by: SYNTHESIZER after gate passage.

[Column schema identical to V-01 including cross-phase attribution columns.]

Minimum rows: equal to TABLE A row count (enforced by row-count assertion at SYNTHESIZER
entry). Mismatch between TABLE G row count and TABLE A row count is a structurally detectable
omission.

[Completeness rule and row-count invariant identical to V-01.]

[All remaining content — GATE TOKEN PROTOCOL, PRIMARY ANALYTICAL FRAMEWORK, all GROUP
sections, phases, role scope declarations, boundaries, OUTPUT SUMMARY — identical to V-01.]
```

---

## V-03

**Variation axis**: Third named gate — SYNTHESIS COMPLETENESS GATE at SYNTHESIZER exit. All
structure identical to V-01. Two changes: (a) GATE TOKEN PROTOCOL preamble adds a third gate
definition (synthesis completeness), (b) SYNTHESIZER phase adds a SYNTHESIS COMPLETENESS GATE
evaluation block after all tables are produced, before writing SYNTHESIZER COMPLETE.

**Hypothesis**: C-60 extends gate token coverage to all named gates. V-01's baseline has two
named gates: hypothesis floor (Phase 1 exit) and evidence floor (Phase 2 exit). Phase 3 has no
named exit gate — "SYNTHESIZER COMPLETE" is an informal declaration. A SYNTHESIS COMPLETENESS
GATE with named pass/fail tokens defined in the GATE TOKEN PROTOCOL preamble would complete the
three-phase gating architecture: every phase exits through a machine-parseable named gate token,
not just informal "X COMPLETE" prose. The synthesis completeness gate verifies the C-58 N=N
assertion is satisfied before the skill terminates, making TABLE G completeness as structurally
enforced at exit as evidence completeness is enforced at Phase 2 exit. Not captured by C-58
(which records the assertion) or C-60 (which covers current named gates) — C-60 would need to
be extended to cover all three gates, or C-61 would cover the three-gate completion pattern.
Candidate for C-61.

---

```
[All content identical to V-01 through GATE TOKEN PROTOCOL block, then:]

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

[PRIMARY ANALYTICAL FRAMEWORK and all GROUP A, GROUP B sections identical to V-01, then
GROUP C -- SYNTHESIZER PHASE with the following addition after the Headcount Range step:]

After producing all outputs (TABLE E, TABLE F, TABLE G, Org Shape paragraph, Headcount Range):

SYNTHESIS COMPLETENESS GATE — evaluate before writing SYNTHESIZER COMPLETE:

Gate checklist:
1. TABLE G row count equals the [N] stated in the ROW-COUNT ASSERTION
2. Every TABLE A Pattern ID appears as a TABLE G Pattern ID
3. Every TABLE G Evidence Summary cell cites at least one TABLE B row number
4. No TABLE A prediction is left unresolved without a corresponding TABLE F gap entry
5. Org Shape paragraph contains CURRENT STATE and RECOMMENDED STATE sections
6. Headcount Range cites at least 2 TABLE C rows

Write exactly one token from GATE TOKEN PROTOCOL SYNTHESIS COMPLETENESS GATE definition:
  PASS: Synthesis complete -- TABLE G [N] rows = TABLE A [N] rows, all predictions resolved
  FAIL: Synthesis incomplete -- TABLE G [M] rows, TABLE A [N] rows, [N-M] predictions unresolved

FAIL TOKEN requires: add TABLE F gap entries for every unresolved TABLE A Pattern ID before
halting, then write the FAIL token.

Phase 3 exit: Write "SYNTHESIZER COMPLETE" after the synthesis completeness gate token.

[SYNTHESIZER / END BOUNDARY and GROUP D identical to V-01.]
```

---

## V-04

**Variation axis**: Named `Violated when:` entry in each ROLE SCOPE DECLARATION. All structure
identical to V-01. Single change: each ROLE SCOPE DECLARATION adds a `Violated when:` property
naming the exact structural output signature that constitutes scope violation for that role.

**Hypothesis**: C-56 requires the PREDICTOR blacklist to name "file reads / scan evidence" as
prohibited outputs. C-57 cascades the primary constraint (no org chart) to all role scope
declarations. Both are prohibition statements: they list what must not appear. A `Violated
when:` entry transforms the prohibition into a detectable violation condition: the exact output
pattern that, if seen in the execution trace, marks a confirmed scope breach without needing to
re-read the instruction text. E.g., for SCANNER: "Violated when: TABLE E, TABLE F, or TABLE G
rows appear in SCANNER output." A reader can audit scope compliance by checking whether any
named violation signature is present in role outputs, without inspecting whether instructions
were followed. This extends C-56's blacklist pattern from PREDICTOR to all four roles, making
scope-violation detection uniformly structural across the full role architecture. Not captured
by C-56 (single role) or C-57 (primary constraint only). Candidate for C-61.

---

```
[All content identical to V-01 through GROUP A preamble, then:]

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

[Phase 1 instructions and PREDICTOR / SCANNER BOUNDARY identical to V-01, then:]

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

[SCANNER phase instructions and SCANNER / GATEKEEPER BOUNDARY identical to V-01, then:]

ROLE SCOPE DECLARATION: GATEKEEPER
PAF Authority: gate evaluation only — no analytical work, no finding generation, no synthesis.
Input Dependencies: TABLE B + TABLE C + TABLE D (from SCANNER) — all three must be present;
  SCANNER COMPLETE token — must be present.
Permitted outputs: exactly one EVIDENCE GATE token (PASS or FAIL from GATE TOKEN PROTOCOL).
Prohibited outputs: TABLE E / TABLE F / TABLE G / analytical findings / synthesis conclusions.
Violated when: any output other than the EVIDENCE GATE token appears in GATEKEEPER output;
  or GATEKEEPER writes a token not defined in the GATE TOKEN PROTOCOL block.
Constraint check: SCANNER COMPLETE token is present. If absent, halt before evaluating.
Org chart prohibition: gate token contains no org chart content.

[Gate checklist and GATEKEEPER / SYNTHESIZER BOUNDARY identical to V-01, then:]

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
Violated when: any TABLE B FILE PATH EVIDENCE cell is cited in SYNTHESIZER output that was
  not produced by SCANNER (i.e., a new path introduced in Phase 3 that has no TABLE B row);
  or TABLE G Evidence Summary contains prose claims not traceable to a TABLE B row citation.
Constraint check: Evidence gate PASS token is present. If absent, halt.
Org chart prohibition (stated in preamble; restated here): Raw analysis only. No org chart.
  No reporting lines. No hierarchy diagrams. No "reports to" statements.

[All SYNTHESIZER phase instructions, SYNTHESIZER / END BOUNDARY, and GROUP D identical to V-01.]
```

---

## V-05

**Variation axis**: Full combination of V-02 + V-03 + V-04. All three new axes active
simultaneously: (a) per-table minimum row floor in SCHEMA DECLARATION, (b) synthesis
completeness gate at SYNTHESIZER exit as third named gate with preamble definition, (c)
`Violated when:` violation signature in each ROLE SCOPE DECLARATION.

**Hypothesis**: All three signals reinforce each other at different layers of the skill
architecture. Per-table row floors (V-02) make the SCHEMA a declarative quantity contract,
establishing floor obligations before any phase begins. The synthesis completeness gate (V-03)
enforces those floor obligations at Phase 3 exit via a named machine-parseable token, creating
a three-gate closure architecture across all phases. The `Violated when:` signatures (V-04)
make scope violations detectable by output inspection at each role boundary, making each
role's compliance both declared (scope declaration) and auditable (violation signature). The
three signals together form a layered verification stack: quantity declared (schema floors) →
scope enforced (violation signatures) → completeness verified (three-gate tokens). Whether this
stack produces a new multi-signal synthesis criterion (stronger than any of the three in
isolation) or surfaces a structural redundancy is an empirical question this combination tests.

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

Minimum rows: none declared (gaps are evidence-dependent).

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
evidence", Source Types Checked set to the source types that were scanned.

Row-count invariant: TABLE G row count must equal TABLE A row count. A row-count mismatch is
a structurally detectable omission — identifiable by table correspondence alone.

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
| I-03 | Domain Teams | Named namespace directories; per-namespace CLAUDE.md or README; per-domain test directories; explicit ownership declared in docs or .roles | "that's the X team's area"; clear escalation path per domain; engineers onboard to a single domain first; incidents have a natural first responder; PRs stay within domain seams |
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

HYPOTHESIS FLOOR GATE — evaluate before SCANNER may begin:

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
7. .roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language
— these are behavioral signal evidence for TABLE B Behavioral Signals and Hypothesis Held.

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
Violated when: any TABLE B FILE PATH EVIDENCE path appears in SYNTHESIZER output that has no
  corresponding TABLE B row (new path introduced in Phase 3); or TABLE G Evidence Summary
  contains prose claims not traceable to a TABLE B row citation by row number.
Constraint check: Evidence gate PASS token is present. If absent, halt.
Org chart prohibition (stated in preamble; restated here): Raw analysis only. No org chart.
  No reporting lines. No hierarchy diagrams. No "reports to" statements. Producing any org
  chart content is a failure of this skill regardless of how complete the other sections are.

Entry condition: Evidence gate PASS token present.

ROW-COUNT ASSERTION (record before producing TABLE G):
Write: "TABLE A count: [N] — TABLE G must contain exactly [N] rows."
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

SYNTHESIS COMPLETENESS GATE — evaluate after all outputs produced, before SYNTHESIZER COMPLETE:

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

## Axis Summary

| Variation | C-58 | C-59 | C-60 | Per-table row floors (V-02) | Synthesis Completeness Gate (V-03) | Violated when (V-04) |
|---|---|---|---|---|---|---|
| V-01 | YES | YES | YES | NO | NO | NO |
| V-02 | YES | YES | YES | YES | NO | NO |
| V-03 | YES | YES | YES | NO | YES | NO |
| V-04 | YES | YES | YES | NO | NO | YES |
| V-05 | YES | YES | YES | YES | YES | YES |
```
