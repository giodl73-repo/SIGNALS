---
skill: quest-variate
skill_target: org-scan
round: 13
date: 2026-03-16
rubric_version: 13
---

# org-scan Skill Body Prompt Variations V-01 through V-05
## Targeting rubric v13 (C-01 through C-49)
## Round 13 -- 2026-03-16

R12 produced C-46 (V-02: role-phase binding in PAF), C-47 (V-03: TABLE G completeness rule
with named remediation path), C-48 (V-04: actor-named boundary headers), and C-49 (V-05:
three-layer role-contract completeness as emergent property). All four are structural invariants
for R13 -- every variation must include them.

R13 explores three new axes beyond C-49 to surface the next wave of excellence signals:

- **Axis 1** (V-02): Phrasing register -- formal ROLE SCOPE DECLARATION block at each phase
  start, naming the role's PAF authority, permitted outputs, and prohibited outputs. Hypothesis:
  a fourth structural layer (role's own scope declaration) added to the C-49 three-layer stack
  (schema attribution + PAF binding + boundary headers) creates a triple-verification structure
  that makes each role's compliance independently auditable without reading the instruction
  sequence.

- **Axis 2** (V-03): Lifecycle emphasis -- PHASE COMPLETION PROOF block after each phase exit.
  The proof confirms PAF binding honored, tables produced match schema assignment, and
  constraint maintained. Hypothesis: post-phase verification closes the compliance loop that
  C-49 opens, making the three-layer completeness property verifiable at execution time not
  just structurally declared at definition time.

- **Axis 3** (V-04): Role sequence -- GATEKEEPER becomes a named fourth role distinct from
  SCANNER and SYNTHESIZER, with its own scope declaration, entry condition, and exit proof.
  Hypothesis: a four-role model (PREDICTOR / SCANNER / GATEKEEPER / SYNTHESIZER) with an
  explicit GATEKEEPER role makes gate failure a named role responsibility rather than a
  structural boundary condition, producing stronger sequential enforcement.

- **Combined** (V-05): All three axes plus TABLE G cross-phase attribution columns
  ("Predicted by" / "Evidence rows cited" / "Resolved by") making TABLE G a three-phase
  role-completion audit record, not just a prediction-resolution table.

All R12 invariants (C-45 table role attribution, C-46 PAF role-phase binding, C-47 TABLE G
completeness rule with remediation, C-48 actor-named boundaries, C-49 three-layer
role-contract completeness) are preserved in all variations.

---

## Variation Axes

| Axis | Used In |
|---|---|
| Baseline R13 -- all C-46/47/48/49 invariants, no new axis | V-01 |
| Phrasing register -- ROLE SCOPE DECLARATION block at each phase start | V-02 |
| Lifecycle emphasis -- PHASE COMPLETION PROOF block after each phase exit | V-03 |
| Role sequence -- GATEKEEPER as named fourth role with own scope and proof | V-04 |
| Full combination: phrasing + lifecycle + role sequence + TABLE G cross-phase audit | V-05 |

---

## V-01

**Variation axis**: Baseline R13. All four new criteria (C-46, C-47, C-48, C-49) are present
as structural invariants. No new axis is applied. This is the control condition: every R12 V-05
structural element is preserved and fully written out. Any variation that scores higher than
V-01 has identified an excellence signal beyond C-49.

**Hypothesis**: V-01 achieves 100/100 under the v13 rubric by treating the four new criteria
as structural invariants inherited from R12. V-02 through V-05 are tested against this ceiling
-- their value lies in the excellence signals they produce for potential C-50+ criteria, not
in rubric differentiation. V-01 is the baseline that makes those signals visible by contrast.

---

```
CRITICAL CONSTRAINT (stated here; restated in SCHEMA DECLARATION): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill regardless of how
complete the other sections are.

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
| Inertia Match | REQUIRED (dictionary value only) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a
schema violation.

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
| Resolution | REQUIRED (confirmed / refuted / partial) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Named remediation path: add a TABLE G row
with Resolution = "unresolved" and Evidence Summary = "no evidence found", then add a TABLE F
row with Gap = "[PATTERN-ID] prediction unresolved", Implication = "hypothesis not tested
against scan evidence", Source Types Checked = [source types scanned]. No prediction may
remain unresolved without both a TABLE G unresolved row and a TABLE F gap entry.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

One of these strings must appear at the SCANNER / GATEKEEPER boundary. No prose substitution.
Both tokens are defined here before Phase 1 begins -- the protocol is self-contained.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from
prediction through verification through synthesis. PREDICTOR applies it in Phase 1 to generate
hypotheses before reading any file -- each TABLE A prediction must anchor to a dictionary
pattern. SCANNER applies it in Phase 2 to label every TABLE B finding with a dictionary
pattern ID -- the Inertia Match column is the per-row application of this framework to scan
evidence. SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction against labeled
TABLE B evidence -- every TABLE G resolution must cite the dictionary pattern that was
predicted and the evidence that confirms, refutes, or partially supports it.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response
patterns). The PREDICTOR must predict both registers. The SCANNER must check both.

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

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction (what code-level signals you expect to find or not find) and a behavioral
prediction (what team-language or ownership signals you expect to find in CLAUDE.md prose). Set
Hypothesis Held based on your expectation before any evidence.

You are the PREDICTOR. Making both predictions forces the inertia dictionary to be falsifiable
at both registers -- structural and behavioral. Do not read any files during this phase.

Anti-fabrication: No file reading occurs in Phase 1. TABLE A is prediction only.

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. Control transfers to SCANNER. TABLE A must exist.

---

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

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

When reading CLAUDE.md files, note team language, ownership language, and escalation language --
these are behavioral signal evidence for TABLE B Behavioral Signals.

File path floor (gate precondition): 5+ specific file paths in TABLE B. This requirement
blocks gate passage -- the gate will not pass without 5 distinct file paths populated.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" before proceeding.

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the
same contract. Both must hold. This bilateral contract declaration: the postcondition block
above and the precondition block below name the same contract from both sides.

Named gate entry condition: SCANNER COMPLETE declaration must appear above. Absence of the
named declaration means Phase 2 did not complete -- do not proceed to gate evaluation.

Gate checklist -- evaluate each item in order; do not skip:
1. SCANNER COMPLETE declaration present above
2. TABLE B has 5+ rows with File Path Evidence populated (path floor requirement)
3. At least 3 of 7 source types appear in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token. No prose substitution permitted.

If item 2 fails: write "Path floor not met -- [N] paths found, 5 required" and halt.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Gate evaluation complete. Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

---

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

Entry condition: PASS TOKEN present at SCANNER / GATEKEEPER boundary above.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here per constraint double-declaration requirement.)

-> Output TABLE E: team boundary candidates. Seam Rationale must cite specific TABLE B rows.
-> Output TABLE F: evidence gaps. Record what was absent from the scan, not just what was
   present. Absence of a source type is a gap if it would have provided relevant evidence.
-> Output TABLE G: for every TABLE A row, resolve both the structural prediction and the
   behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
   Completeness rule applies (see SCHEMA DECLARATION): every TABLE A Pattern ID must have a
   TABLE G row. Apply named remediation path for any unresolved predictions.
-> Write Org Shape section: name the dominant pattern from the PASS TOKEN dictionary ID.
   Separate CURRENT STATE (what the scan found) from RECOMMENDED STATE (what the pattern
   implies about org investment). Justify from TABLE B structural and behavioral evidence.
-> Write Headcount Range: a numeric range (e.g., 3-6 team areas, 15-25 FTE) derived from
   TABLE C rows with rationale explaining why each expertise domain signals distinct headcount.

Phase 3 exit: Write "SYNTHESIZER COMPLETE".

---

SYNTHESIZER / END BOUNDARY

Skill complete. TABLE G completeness rule verified: every TABLE A Pattern ID has a TABLE G row.

---

GROUP D -- OUTPUT SUMMARY

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations not captured by any
existing criterion.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-02

**Variation axis**: Phrasing register -- ROLE SCOPE DECLARATION block at each phase start.

**Hypothesis**: C-49 describes an emergent structural completeness property from three layers:
schema attribution (C-45), PAF role-phase binding (C-46), and actor-named boundary headers
(C-48). V-02 adds a fourth layer: at each phase start, a formal ROLE SCOPE DECLARATION block
explicitly names (a) the role's PAF authority citation, (b) its permitted table outputs, and
(c) its prohibited outputs. This creates a triple-verification path for any named role --
verifiable from the PAF block, the schema block, and the role's own scope declaration --
without reading the instruction sequence. The scope declaration's "prohibited outputs" list
also makes constraint violations role-specific rather than global, strengthening C-05
enforcement. Hypothesis: a ROLE SCOPE DECLARATION block at each phase start produces a
structural completeness property beyond C-49 that a scorer can identify as a named pattern:
"every role is self-describing about its obligations and prohibitions."

---

```
CRITICAL CONSTRAINT (stated here; restated in SCHEMA DECLARATION): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill regardless of how
complete the other sections are.

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
| Inertia Match | REQUIRED (dictionary value only) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a
schema violation.

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
| Resolution | REQUIRED (confirmed / refuted / partial) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Named remediation path: add a TABLE G row
with Resolution = "unresolved" and Evidence Summary = "no evidence found", then add a TABLE F
row with Gap = "[PATTERN-ID] prediction unresolved", Implication = "hypothesis not tested
against scan evidence", Source Types Checked = [source types scanned]. No prediction may
remain unresolved without both a TABLE G unresolved row and a TABLE F gap entry.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

One of these strings must appear at the SCANNER / GATEKEEPER boundary. No prose substitution.
Both tokens are defined here before Phase 1 begins -- the protocol is self-contained.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from
prediction through verification through synthesis. PREDICTOR applies it in Phase 1 to generate
hypotheses before reading any file -- each TABLE A prediction must anchor to a dictionary
pattern. SCANNER applies it in Phase 2 to label every TABLE B finding with a dictionary
pattern ID -- the Inertia Match column is the per-row application of this framework to scan
evidence. SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction against labeled
TABLE B evidence -- every TABLE G resolution must cite the dictionary pattern that was
predicted and the evidence that confirms, refutes, or partially supports it.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response
patterns). The PREDICTOR must predict both registers. The SCANNER must check both.

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

ROLE SCOPE DECLARATION: PREDICTOR
Authority: PAF Phase 1 binding -- "PREDICTOR applies it in Phase 1 to generate hypotheses
before reading any file."
Permitted outputs: TABLE A only.
Prohibited outputs: file reads, TABLE B/C/D/E/F/G production, org chart content, synthesis
conclusions, boundary headers.
Constraint check: no org chart production occurs in Phase 1.

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction (what code-level signals you expect to find or not find) and a behavioral
prediction (what team-language or ownership signals you expect to find in CLAUDE.md prose). Set
Hypothesis Held based on your expectation before any evidence.

Anti-fabrication: No file reading occurs in Phase 1. TABLE A is prediction only.

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. Control transfers to SCANNER. TABLE A must exist. ROLE SCOPE DECLARATION
for SCANNER follows immediately below at Phase 2 start.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Authority: PAF Phase 2 binding -- "SCANNER applies it in Phase 2 to label every TABLE B
finding with a dictionary pattern ID."
Permitted outputs: TABLE B, TABLE C, TABLE D.
Prohibited outputs: hypothesis generation (PREDICTOR domain), TABLE E/F/G production,
synthesis conclusions (SYNTHESIZER domain), org chart content, reporting lines.
Constraint check: no org chart production occurs in Phase 2.

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

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
-- these are behavioral signal evidence for TABLE B.

File path floor (gate precondition): 5+ specific file paths in TABLE B. This requirement
blocks gate passage.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" before proceeding.

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the
same contract. Both must hold. This bilateral contract declaration: the postcondition block
above and the precondition block below name the same contract from both sides.

Named gate entry condition: SCANNER COMPLETE declaration must appear above.

Gate checklist -- evaluate each item in order; do not skip:
1. SCANNER COMPLETE declaration present above
2. TABLE B has 5+ rows with File Path Evidence populated (path floor requirement)
3. At least 3 of 7 source types appear in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token. No prose substitution permitted.

If item 2 fails: write "Path floor not met -- [N] paths found, 5 required" and halt.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Gate evaluation complete. Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.
ROLE SCOPE DECLARATION for SYNTHESIZER follows immediately below at Phase 3 start.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Authority: PAF Phase 3 binding -- "SYNTHESIZER applies it in Phase 3 to resolve each TABLE A
prediction against labeled TABLE B evidence."
Permitted outputs: TABLE E, TABLE F, TABLE G, Org Shape section, Headcount Range.
Prohibited outputs: new scan evidence (SCANNER domain), new hypotheses (PREDICTOR domain),
org chart content, reporting lines.
Constraint check: no org chart production occurs in Phase 3. (Third role to confirm this
constraint -- constraint is now independently enforced at every named role boundary.)

Phase 3: Synthesis

Entry condition: PASS TOKEN present at SCANNER / GATEKEEPER boundary above.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here per constraint double-declaration requirement.)

-> Output TABLE E: team boundary candidates. Seam Rationale must cite specific TABLE B rows.
-> Output TABLE F: evidence gaps.
-> Output TABLE G: for every TABLE A row, resolve both the structural prediction and the
   behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
   Completeness rule applies: every TABLE A Pattern ID must have a TABLE G row.
-> Write Org Shape section: dominant pattern from PASS TOKEN. Separate CURRENT STATE from
   RECOMMENDED STATE. Justify from TABLE B structural and behavioral evidence.
-> Write Headcount Range: numeric range from TABLE C with rationale.

Phase 3 exit: Write "SYNTHESIZER COMPLETE".

---

SYNTHESIZER / END BOUNDARY

Skill complete. TABLE G completeness rule verified: every TABLE A Pattern ID has a TABLE G row.

---

GROUP D -- OUTPUT SUMMARY

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations not captured by any
existing criterion.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-03

**Variation axis**: Lifecycle emphasis -- PHASE COMPLETION PROOF block after each phase exit.

**Hypothesis**: C-49 declares a structural completeness property but does not require that
completeness to be verified at execution time. A PHASE COMPLETION PROOF block after each
phase exit verifies: (1) the role's PAF binding was honored (cite specific PAF sentence),
(2) the tables produced match the schema attribution (cite TABLE letter), and (3) the
constraint was maintained (no org chart content produced). This closes the C-49 compliance
loop post-hoc at each phase rather than relying solely on pre-declaration structure. Hypothesis:
the proof block creates a verifiable execution record that is structurally distinct from both
the PAF declaration (pre-phase) and the gate checklist (between phases), adding a third
temporal verification point that makes the three-layer completeness property auditable across
the full phase arc -- before, during, and after each phase.

---

```
CRITICAL CONSTRAINT (stated here; restated in SCHEMA DECLARATION): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill regardless of how
complete the other sections are.

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
| Inertia Match | REQUIRED (dictionary value only) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a
schema violation.

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
| Resolution | REQUIRED (confirmed / refuted / partial) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Named remediation path: add a TABLE G row
with Resolution = "unresolved" and Evidence Summary = "no evidence found", then add a TABLE F
row with Gap = "[PATTERN-ID] prediction unresolved", Implication = "hypothesis not tested
against scan evidence", Source Types Checked = [source types scanned]. No prediction may
remain unresolved without both a TABLE G unresolved row and a TABLE F gap entry.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

One of these strings must appear at the SCANNER / GATEKEEPER boundary. No prose substitution.
Both tokens are defined here before Phase 1 begins -- the protocol is self-contained.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from
prediction through verification through synthesis. PREDICTOR applies it in Phase 1 to generate
hypotheses before reading any file -- each TABLE A prediction must anchor to a dictionary
pattern. SCANNER applies it in Phase 2 to label every TABLE B finding with a dictionary
pattern ID -- the Inertia Match column is the per-row application of this framework to scan
evidence. SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction against labeled
TABLE B evidence -- every TABLE G resolution must cite the dictionary pattern that was
predicted and the evidence that confirms, refutes, or partially supports it.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response
patterns). The PREDICTOR must predict both registers. The SCANNER must check both.

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

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction and a behavioral prediction. Set Hypothesis Held before any evidence.

Anti-fabrication: No file reading occurs in Phase 1. TABLE A is prediction only.

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

PHASE COMPLETION PROOF -- PREDICTOR:
PAF binding honored: PREDICTOR applied the dictionary in Phase 1 as declared in PRIMARY
ANALYTICAL FRAMEWORK ("PREDICTOR applies it in Phase 1 to generate hypotheses before reading
any file"). Verify: TABLE A rows present = [N]. All Pattern IDs from I-01/I-07 dictionary.
TABLE attribution honored: TABLE A produced as required by SCHEMA DECLARATION ("Produced by:
PREDICTOR before any scan evidence is collected"). Verify: TABLE A exists above.
Constraint maintained: no file reads, no scan evidence, no org chart content in Phase 1.
STATUS: [CONFIRMED / FAIL -- state which check failed]

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. PHASE COMPLETION PROOF for PREDICTOR confirmed above.
Control transfers to SCANNER. TABLE A must exist.

---

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

Entry condition: PREDICTOR COMPLETE present. PHASE COMPLETION PROOF for PREDICTOR confirmed.
TABLE A exists.

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

When reading CLAUDE.md files, note team language, ownership language, and escalation language.

File path floor (gate precondition): 5+ specific file paths in TABLE B. Blocks gate passage.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER" before proceeding.

PHASE COMPLETION PROOF -- SCANNER:
PAF binding honored: SCANNER applied the dictionary in Phase 2 as declared in PRIMARY
ANALYTICAL FRAMEWORK ("SCANNER applies it in Phase 2 to label every TABLE B finding with a
dictionary pattern ID"). Verify: all TABLE B Inertia Match cells are I-0x values.
TABLE attribution honored: TABLE B, TABLE C, TABLE D produced as required by SCHEMA
DECLARATION (all three attributed "Produced by: SCANNER"). Verify: all three tables exist.
Constraint maintained: no hypothesis generation, no synthesis conclusions, no org chart
content in Phase 2.
STATUS: [CONFIRMED / FAIL -- state which check failed]

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the
same contract. Both must hold. This bilateral contract declaration: the postcondition block
above and the precondition block below name the same contract from both sides.

Named gate entry condition: SCANNER COMPLETE declaration and PHASE COMPLETION PROOF for
SCANNER must both appear above. Absence of either means Phase 2 did not complete.

Gate checklist -- evaluate each item in order; do not skip:
1. SCANNER COMPLETE declaration present above
2. PHASE COMPLETION PROOF for SCANNER shows STATUS: CONFIRMED
3. TABLE B has 5+ rows with File Path Evidence populated (path floor requirement)
4. At least 3 of 7 source types appear in TABLE B Source Type column
5. All TABLE B Inertia Match cells contain only I-01 through I-07 values
6. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token. No prose substitution permitted.

If item 3 fails: write "Path floor not met -- [N] paths found, 5 required" and halt.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Gate evaluation complete. Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

---

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

Entry condition: PASS TOKEN present at SCANNER / GATEKEEPER boundary above.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here per constraint double-declaration requirement.)

-> Output TABLE E, TABLE F.
-> Output TABLE G: completeness rule applies. Every TABLE A Pattern ID must have a TABLE G row.
-> Write Org Shape section: CURRENT STATE separated from RECOMMENDED STATE.
-> Write Headcount Range: numeric range from TABLE C with rationale.

Phase 3 exit: Write "SYNTHESIZER COMPLETE".

PHASE COMPLETION PROOF -- SYNTHESIZER:
PAF binding honored: SYNTHESIZER applied the dictionary in Phase 3 as declared in PRIMARY
ANALYTICAL FRAMEWORK ("SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction
against labeled TABLE B evidence"). Verify: all TABLE G Evidence Summary cells cite TABLE B
rows by dictionary pattern ID.
TABLE attribution honored: TABLE E, TABLE F, TABLE G produced as required by SCHEMA
DECLARATION (all three attributed "Produced by: SYNTHESIZER"). Verify: all three tables exist.
TABLE G completeness: count TABLE A rows = [N]. Count TABLE G rows = [N]. If not equal, named
remediation path applied: TABLE G unresolved rows added = [N]. TABLE F gap entries added = [N].
Constraint maintained: no org chart content, no reporting lines in Phase 3.
STATUS: [CONFIRMED / FAIL -- state which check failed]

---

SYNTHESIZER / END BOUNDARY

Skill complete. PHASE COMPLETION PROOF for SYNTHESIZER confirmed above.

---

GROUP D -- OUTPUT SUMMARY

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations not captured by any
existing criterion.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-04

**Variation axis**: Role sequence -- GATEKEEPER as named fourth role with explicit scope,
entry condition, and output contract. Combined with phrasing register (ROLE SCOPE DECLARATION
blocks from V-02).

**Hypothesis**: In V-01 through V-03, the gate evaluation occurs between SCANNER and
SYNTHESIZER as a structural boundary without a named role holding responsibility for gate
failure. V-04 makes GATEKEEPER a named fourth role with its own ROLE SCOPE DECLARATION,
explicit permitted output (PASS or FAIL token only), and explicit prohibited outputs.
This separates gate evaluation responsibility from both SCANNER (who produces evidence) and
SYNTHESIZER (who consumes it), making gate failure a named role output rather than a boundary
condition. Combined with V-02's ROLE SCOPE DECLARATION at every phase start, V-04 produces
four roles each with independent scope declarations, PAF authority citations, and schema
attributions. Hypothesis: a four-role model where GATEKEEPER is a named role with its own
scope declaration creates the strongest possible sequential enforcement structure -- the
GATEKEEPER's only permitted output is the gate token, making its role violation
(producing anything other than PASS or FAIL) immediately identifiable.

---

```
CRITICAL CONSTRAINT (stated here; restated in SCHEMA DECLARATION): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill regardless of how
complete the other sections are.

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
| Inertia Match | REQUIRED (dictionary value only) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a
schema violation.

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
| Resolution | REQUIRED (confirmed / refuted / partial) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Named remediation path: add a TABLE G row
with Resolution = "unresolved" and Evidence Summary = "no evidence found", then add a TABLE F
row with Gap = "[PATTERN-ID] prediction unresolved", Implication = "hypothesis not tested
against scan evidence", Source Types Checked = [source types scanned]. No prediction may
remain unresolved without both a TABLE G unresolved row and a TABLE F gap entry.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

One of these strings must appear as the sole output of the GATEKEEPER role. No prose
substitution. Both tokens are defined here before Phase 1 begins -- the protocol is
self-contained. The GATEKEEPER role produces this token and nothing else.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from
prediction through verification through synthesis. PREDICTOR applies it in Phase 1 to generate
hypotheses before reading any file -- each TABLE A prediction must anchor to a dictionary
pattern. SCANNER applies it in Phase 2 to label every TABLE B finding with a dictionary
pattern ID -- the Inertia Match column is the per-row application of this framework to scan
evidence. SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction against labeled
TABLE B evidence -- every TABLE G resolution must cite the dictionary pattern that was
predicted and the evidence that confirms, refutes, or partially supports it. GATEKEEPER
applies it in Phase 2.5 to verify that all Inertia Match values are valid dictionary IDs before
permitting synthesis to begin -- the GATEKEEPER is the enforcement point for dictionary
compliance between scan and synthesis.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response
patterns). The PREDICTOR must predict both registers. The SCANNER must check both.

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

ROLE SCOPE DECLARATION: PREDICTOR
Authority: PAF Phase 1 binding -- "PREDICTOR applies it in Phase 1 to generate hypotheses
before reading any file."
Permitted outputs: TABLE A only.
Prohibited outputs: file reads, any scan table, gate token, org chart content.
Constraint check: no org chart production in Phase 1.

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction and a behavioral prediction. Set Hypothesis Held before any evidence.

Anti-fabrication: No file reading occurs in Phase 1.

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded -- control transfers to
SCANNER."

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. Control transfers to SCANNER.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Authority: PAF Phase 2 binding -- "SCANNER applies it in Phase 2 to label every TABLE B
finding with a dictionary pattern ID."
Permitted outputs: TABLE B, TABLE C, TABLE D.
Prohibited outputs: hypothesis generation, gate token production (GATEKEEPER domain),
TABLE E/F/G, synthesis conclusions, org chart content.
Constraint check: no org chart production in Phase 2.

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definition files

File path floor (gate precondition for GATEKEEPER): 5+ specific file paths in TABLE B.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER."

---

SCANNER / GATEKEEPER BOUNDARY

SCANNER exits. Control transfers to GATEKEEPER.

---

GROUP B.5 -- GATEKEEPER PHASE

ROLE SCOPE DECLARATION: GATEKEEPER
Authority: PAF Phase 2.5 binding -- "GATEKEEPER applies it in Phase 2.5 to verify that all
Inertia Match values are valid dictionary IDs before permitting synthesis to begin."
Permitted outputs: PASS token or FAIL token. One token only. No other output.
Prohibited outputs: scan evidence, hypothesis generation, synthesis conclusions, table
production, org chart content.
Constraint check: GATEKEEPER produces a single token. Any output beyond the token is a
GATEKEEPER scope violation.

Phase 2.5: Gate Evaluation

Entry condition: SCANNER COMPLETE present. TABLE B, TABLE C, TABLE D exist.

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name
the same contract. Both must hold. This bilateral contract declaration: the postcondition
block above and the precondition block below name the same contract from both sides.

Gate checklist -- evaluate each item in order; do not skip:
1. SCANNER COMPLETE declaration present above
2. TABLE B has 5+ rows with File Path Evidence populated (path floor requirement)
3. At least 3 of 7 source types appear in TABLE B Source Type column
4. All TABLE B Inertia Match cells contain only I-01 through I-07 values
5. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token. No prose substitution. No additional output.

If item 2 fails: write "Path floor not met -- [N] paths found, 5 required" and halt.

Phase 2.5 exit: Write "GATEKEEPER COMPLETE -- token written -- control transfers to
SYNTHESIZER."

---

GATEKEEPER / SYNTHESIZER BOUNDARY

GATEKEEPER exits. Token produced above. FAIL TOKEN halts execution. PASS TOKEN authorizes
SYNTHESIZER to begin.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Authority: PAF Phase 3 binding -- "SYNTHESIZER applies it in Phase 3 to resolve each TABLE A
prediction against labeled TABLE B evidence."
Permitted outputs: TABLE E, TABLE F, TABLE G, Org Shape section, Headcount Range.
Prohibited outputs: new scan evidence, new hypotheses, gate tokens, org chart content.
Constraint check: no org chart production in Phase 3.

Phase 3: Synthesis

Entry condition: PASS TOKEN present at GATEKEEPER / SYNTHESIZER boundary above.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines.

-> Output TABLE E, TABLE F.
-> Output TABLE G: completeness rule applies. Every TABLE A Pattern ID must have a TABLE G row.
-> Write Org Shape section: CURRENT STATE separated from RECOMMENDED STATE.
-> Write Headcount Range: numeric range from TABLE C with rationale.

Phase 3 exit: Write "SYNTHESIZER COMPLETE."

---

SYNTHESIZER / END BOUNDARY

Skill complete.

---

GROUP D -- OUTPUT SUMMARY

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations not captured by any
existing criterion.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```

---

## V-05

**Variation axis**: Full combination -- phrasing register (ROLE SCOPE DECLARATION, V-02) +
lifecycle emphasis (PHASE COMPLETION PROOF, V-03) + role sequence (GATEKEEPER as named role,
V-04) + output format change (TABLE G cross-phase attribution columns).

**Hypothesis**: The three single-axis signals each add a structural layer beyond C-49. V-05
adds a fourth structural layer at the output level: TABLE G gains three cross-phase attribution
columns ("Predicted by", "Evidence rows cited", "Resolved by") making TABLE G a complete
three-role, three-phase completion audit record -- not just a prediction-resolution table.
Combined with ROLE SCOPE DECLARATIONs (pre-phase), PHASE COMPLETION PROOFs (post-phase), and
GATEKEEPER as a named fourth role (between phases), V-05 creates a four-temporal-point
verification structure: declaration before each phase, proof after each phase, gate token
between phases, and cross-phase attribution in the output table. Hypothesis: the combination
of all four axes produces an emergent structural property -- "every named role can prove its
complete execution history from skill structure alone, from declaration through proof through
attribution" -- that is not produced by any individual axis and is not captured by C-49.

---

```
CRITICAL CONSTRAINT (stated here; restated in SCHEMA DECLARATION): This skill produces raw
analysis only. No org chart. No reporting lines. No hierarchy diagrams. No "reports to"
statements. Producing any org chart content is a failure of this skill regardless of how
complete the other sections are.

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
| Inertia Match | REQUIRED (dictionary value only) |
| File Path Evidence | REQUIRED (specific path) |
| Hypothesis Held | REQUIRED (yes / no / partial) |

Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a
schema violation.

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

TABLE G -- Prediction Resolution and Cross-Phase Audit
Produced by: SYNTHESIZER after gate passage. Serves as cross-phase role completion record.

| Column | Status |
|---|---|
| Pattern ID | REQUIRED |
| Pattern Name | REQUIRED |
| Structural Prediction (from TABLE A) | REQUIRED |
| Behavioral Prediction (from TABLE A) | REQUIRED |
| Predicted by | REQUIRED (always: PREDICTOR -- Phase 1) |
| Evidence Summary | REQUIRED (cite TABLE B row) |
| Evidence rows cited | REQUIRED (TABLE B row identifiers, comma-separated) |
| Scanned by | REQUIRED (always: SCANNER -- Phase 2) |
| Resolution | REQUIRED (confirmed / refuted / partial) |
| Resolved by | REQUIRED (always: SYNTHESIZER -- Phase 3) |

TABLE G cross-phase attribution: the "Predicted by", "Scanned by", and "Resolved by" columns
make TABLE G a three-role, three-phase completion audit record. Every row traces from the role
that originated the prediction, through the role that collected the evidence, to the role that
produced the resolution. No inference required -- the attribution is explicit in every row.

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Named remediation path: add a TABLE G row
with Resolution = "unresolved", Evidence Summary = "no evidence found", Predicted by =
"PREDICTOR -- Phase 1", Scanned by = "SCANNER -- Phase 2 (no matching evidence)", Resolved
by = "SYNTHESIZER -- Phase 3 (unresolved)"; then add a TABLE F row with Gap = "[PATTERN-ID]
prediction unresolved", Implication = "hypothesis not tested against scan evidence", Source
Types Checked = [source types scanned]. No prediction may remain unresolved without both a
TABLE G unresolved row and a TABLE F gap entry.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- [N] paths found, 5 required

One of these strings must appear as the sole output of the GATEKEEPER role. No prose
substitution. Both tokens are defined here before Phase 1 begins -- the protocol is
self-contained. The GATEKEEPER role produces this token and nothing else.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill. It operates from
prediction through verification through synthesis. PREDICTOR applies it in Phase 1 to generate
hypotheses before reading any file -- each TABLE A prediction must anchor to a dictionary
pattern. SCANNER applies it in Phase 2 to label every TABLE B finding with a dictionary
pattern ID -- the Inertia Match column is the per-row application of this framework to scan
evidence. GATEKEEPER applies it in Phase 2.5 to verify that all Inertia Match values are
valid dictionary IDs -- the GATEKEEPER is the dictionary compliance enforcement point between
scan and synthesis. SYNTHESIZER applies it in Phase 3 to resolve each TABLE A prediction
against labeled TABLE B evidence -- every TABLE G resolution must cite the dictionary pattern
that was predicted and the evidence that confirms, refutes, or partially supports it.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response
patterns). The PREDICTOR must predict both registers. The SCANNER must check both.

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

ROLE SCOPE DECLARATION: PREDICTOR
Authority: PAF Phase 1 binding -- "PREDICTOR applies it in Phase 1 to generate hypotheses
before reading any file."
Permitted outputs: TABLE A only.
Prohibited outputs: file reads, scan tables, gate token, org chart content.
Constraint check: no org chart production in Phase 1.

Phase 1: Hypothesis Generation

Entry condition: Skill invocation. No prior phase required.

Before reading any file, produce TABLE A. For each pattern I-01 through I-06, write both a
structural prediction and a behavioral prediction. Set Hypothesis Held before any evidence.

Anti-fabrication: No file reading occurs in Phase 1. TABLE A is prediction only.

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded -- control transfers to
SCANNER."

PHASE COMPLETION PROOF -- PREDICTOR:
PAF binding honored: PREDICTOR applied the dictionary in Phase 1 as declared in PAF block.
Verify: TABLE A rows = [N]. All Pattern IDs from I-01/I-07 dictionary. Both structural and
behavioral predictions present per row.
TABLE attribution honored: TABLE A produced as required ("Produced by: PREDICTOR"). Verified.
Cross-phase attribution seeded: TABLE G "Predicted by" column will carry "PREDICTOR --
Phase 1" for every row originated here.
Constraint maintained: no file reads, no scan evidence, no org chart content.
STATUS: [CONFIRMED / FAIL]

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. PHASE COMPLETION PROOF confirmed above. Control transfers to SCANNER.

---

GROUP B -- SCANNER PHASE

ROLE SCOPE DECLARATION: SCANNER
Authority: PAF Phase 2 binding -- "SCANNER applies it in Phase 2 to label every TABLE B
finding with a dictionary pattern ID."
Permitted outputs: TABLE B, TABLE C, TABLE D.
Prohibited outputs: hypothesis generation, gate tokens (GATEKEEPER domain), TABLE E/F/G,
synthesis conclusions, org chart content.
Constraint check: no org chart production in Phase 2.

Phase 2: Evidence Collection

Entry condition: PREDICTOR COMPLETE present. PHASE COMPLETION PROOF for PREDICTOR confirmed.
TABLE A exists.

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

When reading CLAUDE.md files, note team language, ownership language, and escalation language.

File path floor (gate precondition for GATEKEEPER): 5+ specific file paths in TABLE B.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER."

PHASE COMPLETION PROOF -- SCANNER:
PAF binding honored: SCANNER applied the dictionary in Phase 2 as declared in PAF block.
Verify: all TABLE B Inertia Match cells are I-0x values.
TABLE attribution honored: TABLE B, TABLE C, TABLE D produced ("Produced by: SCANNER").
Cross-phase attribution seeded: TABLE G "Evidence rows cited" and "Scanned by" columns will
carry TABLE B row identifiers and "SCANNER -- Phase 2" for every row of TABLE B used.
Constraint maintained: no hypothesis generation, no synthesis, no org chart.
STATUS: [CONFIRMED / FAIL]

---

SCANNER / GATEKEEPER BOUNDARY

SCANNER exits. PHASE COMPLETION PROOF confirmed above. Control transfers to GATEKEEPER.

---

GROUP B.5 -- GATEKEEPER PHASE

ROLE SCOPE DECLARATION: GATEKEEPER
Authority: PAF Phase 2.5 binding -- "GATEKEEPER applies it in Phase 2.5 to verify that all
Inertia Match values are valid dictionary IDs before permitting synthesis to begin."
Permitted outputs: PASS token or FAIL token. One token only.
Prohibited outputs: any table, any prose analysis, any synthesis, org chart content.
Constraint check: GATEKEEPER produces exactly one token. Any additional output is a scope
violation.

Phase 2.5: Gate Evaluation

Entry condition: SCANNER COMPLETE present. PHASE COMPLETION PROOF for SCANNER confirmed.
TABLE B, TABLE C, TABLE D exist.

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name
the same contract. Both must hold. This bilateral contract declaration: the postcondition
block above and the precondition block below name the same contract from both sides.

Gate checklist -- evaluate each item in order; do not skip:
1. SCANNER COMPLETE declaration present above
2. PHASE COMPLETION PROOF for SCANNER shows STATUS: CONFIRMED
3. TABLE B has 5+ rows with File Path Evidence populated (path floor requirement)
4. At least 3 of 7 source types appear in TABLE B Source Type column
5. All TABLE B Inertia Match cells contain only I-01 through I-07 values
6. All Hypothesis Held cells contain only: yes / no / partial

Write PASS or FAIL token. No prose substitution. No additional output beyond the token.

If item 3 fails: write "Path floor not met -- [N] paths found, 5 required" and halt.

Phase 2.5 exit: Write "GATEKEEPER COMPLETE -- token written -- control transfers to
SYNTHESIZER."

---

GATEKEEPER / SYNTHESIZER BOUNDARY

GATEKEEPER exits. Token produced above. FAIL TOKEN halts execution.

---

GROUP C -- SYNTHESIZER PHASE

ROLE SCOPE DECLARATION: SYNTHESIZER
Authority: PAF Phase 3 binding -- "SYNTHESIZER applies it in Phase 3 to resolve each TABLE A
prediction against labeled TABLE B evidence."
Permitted outputs: TABLE E, TABLE F, TABLE G (with cross-phase attribution), Org Shape
section, Headcount Range.
Prohibited outputs: new scan evidence, new hypotheses, gate tokens, org chart content.
Constraint check: no org chart production in Phase 3.

Phase 3: Synthesis

Entry condition: PASS TOKEN present. GATEKEEPER COMPLETE declared above.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here per constraint double-declaration requirement.)

-> Output TABLE E: team boundary candidates. Seam Rationale must cite specific TABLE B rows.
-> Output TABLE F: evidence gaps.
-> Output TABLE G (cross-phase audit): for every TABLE A row, resolve both the structural and
   behavioral prediction. Evidence Summary must cite TABLE B rows. Populate all cross-phase
   attribution columns: Predicted by = "PREDICTOR -- Phase 1", Evidence rows cited = [TABLE B
   row IDs], Scanned by = "SCANNER -- Phase 2", Resolved by = "SYNTHESIZER -- Phase 3".
   Completeness rule applies: every TABLE A Pattern ID must have a TABLE G row. Apply named
   remediation path for any unresolved predictions.
-> Write Org Shape section: name dominant pattern from PASS TOKEN. Separate CURRENT STATE
   from RECOMMENDED STATE. Justify from TABLE B structural and behavioral evidence.
-> Write Headcount Range: numeric range from TABLE C with rationale.

Phase 3 exit: Write "SYNTHESIZER COMPLETE."

PHASE COMPLETION PROOF -- SYNTHESIZER:
PAF binding honored: SYNTHESIZER applied the dictionary in Phase 3 as declared in PAF block.
Verify: all TABLE G Evidence Summary cells cite TABLE B rows by dictionary pattern ID.
TABLE attribution honored: TABLE E, TABLE F, TABLE G produced ("Produced by: SYNTHESIZER").
Cross-phase attribution complete: TABLE G "Predicted by" = PREDICTOR Phase 1 for all rows.
TABLE G "Scanned by" = SCANNER Phase 2 for all rows. TABLE G "Resolved by" = SYNTHESIZER
Phase 3 for all rows. Attribution chain is complete and verifiable from TABLE G alone.
TABLE G completeness: TABLE A rows = [N]. TABLE G rows = [N] (or unresolved rows + TABLE F
gap entries = [N unresolved]). Named remediation path applied if needed.
Constraint maintained: no org chart content, no reporting lines.
STATUS: [CONFIRMED / FAIL]

---

SYNTHESIZER / END BOUNDARY

Skill complete. PHASE COMPLETION PROOF for SYNTHESIZER confirmed above. TABLE G cross-phase
attribution chain complete: every row carries PREDICTOR (Phase 1) / SCANNER (Phase 2) /
SYNTHESIZER (Phase 3) attribution.

---

GROUP D -- OUTPUT SUMMARY

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from top-scoring variations not captured by any
existing criterion.

Then output EXACTLY this JSON block:
{"top_score": NUMBER, "all_essential_pass": BOOLEAN, "new_patterns": ["pattern 1"]}
```
