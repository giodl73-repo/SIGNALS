---
skill: quest-variate
skill_target: org-scan
round: 12
date: 2026-03-16
rubric_version: 12
---

# org-scan Skill Body Prompt Variations V-01 through V-05
## Targeting rubric v12 (C-01 through C-45)
## Round 12 -- 2026-03-16

R11 achieved 100/100 across all 5 variations. C-45 (table role attribution) is the structural
invariant for R12 -- all variations embed "Produced by: ROLE" annotations on every table header
in the SCHEMA DECLARATION. R12 explores the three remaining R11 excellence signals as variation
axes, testing which produces the most compelling C-46 candidate:

- **Signal 2** (V-02): Role-phase binding in PAF declaration -- each dictionary phase
  explicitly assigned to a named role (PREDICTOR/SCANNER/SYNTHESIZER) rather than arc-level
  posture only.
- **Signal 3** (V-03): TABLE G completeness rule with named remediation path -- not just
  "no prediction left unresolved" but a named Completeness rule that identifies the exact
  remediation step when a TABLE A row has no TABLE G row.
- **Signal 4** (V-04): Actor-named boundary headers -- PREDICTOR / SCANNER BOUNDARY format
  instead of GROUP A / GROUP B BOUNDARY, naming transfer actors in the header itself.

V-01 is the baseline v12 prompt. V-02/V-03/V-04 add one signal each. V-05 combines all three.

---

## Variation Axes

| Axis | Used In |
|---|---|
| Baseline v12 (schema-first, C-45 table attribution, GROUP A/B/C/D labels) | V-01 |
| Role-phase binding in PAF (PREDICTOR/SCANNER/SYNTHESIZER phase assignments) | V-02 |
| TABLE G completeness rule with named remediation path | V-03 |
| Actor-named boundary headers (PREDICTOR/SCANNER BOUNDARY format) | V-04 |
| Full combination (V-02 + V-03 + V-04) | V-05 |

---

## V-01

**Variation axis**: Baseline v12 -- schema-first ordering, C-45 table role attribution on
all TABLE A-G headers, GROUP A/B/C/D phase boundary labels, GROUP B/GATE/GROUP C boundary
structure, basic PAF arc language ("from prediction through verification through synthesis"),
basic TABLE G completeness statement ("Every TABLE A row must have a TABLE G row").

**Hypothesis**: V-01 establishes the 100/100 baseline that C-45 produces without additional
structural signals. All R11 excellence axes (role-phase binding, TABLE G completeness rule,
actor-named boundaries) are absent; their absence is the control condition for R12 scoring.
Any variation that scores higher than 100 is impossible under the v12 rubric -- the value of
V-02 through V-04 lies in the excellence signals they produce for C-46, not in rubric
differentiation.

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
| Resolution | REQUIRED (yes / no / partial) |

Every TABLE A row must have a TABLE G row. No prediction left unresolved.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- scan incomplete

One of these strings must appear at the Phase 2 / Phase 3 boundary. No prose substitution.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill, operating from prediction
through verification through synthesis. Every hypothesis in Phase 1, every Inertia Match value
in Phase 2, and every synthesis claim in Phase 3 must anchor to an entry from this dictionary.
The dictionary is not a post-hoc classifier -- it is the analytical lens from the first
prediction the PREDICTOR writes.

Free text in the Inertia Match column is structurally invalid -- unconstrained values make
pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response patterns).
The PREDICTOR must predict both registers. The SCANNER must check both.

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

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

---

GROUP A / GROUP B BOUNDARY

PREDICTOR exits. Control transfers to SCANNER. TABLE A must exist.

---

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences. Do not infer
from file names.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language --
these are behavioral signal evidence for TABLE B.

File path floor (gate precondition): 5+ specific file paths in TABLE B. Blocks gate passage.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER".

---

GROUP B / GATE BOUNDARY

PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the
same contract. Both must hold.

Gate checklist -- evaluate each item in order; do not skip:
1. At least 3 of 7 source types were scanned
2. TABLE B has at least 5 rows with File Path Evidence populated
3. All Inertia Match cells use I-01 through I-07
4. All Hypothesis Held cells use: yes / no / partial
5. Anti-fabrication confirmed

Write PASS or FAIL token.

---

GATE / GROUP C BOUNDARY

Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

---

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

Entry condition: PASS TOKEN present.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here.)

-> Output TABLE E, TABLE F.
-> Output TABLE G: for every TABLE A row, resolve both the structural prediction and the
   behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
-> Write Org Shape paragraph: dominant pattern from PASS TOKEN. Separate CURRENT STATE from
   RECOMMENDED STATE. Justify from TABLE B structural and behavioral evidence.
-> Write Headcount Range: total FTE range from TABLE C with rationale.

Phase 3 exit: Write "SYNTHESIZER COMPLETE".

---

GROUP C / GROUP D BOUNDARY

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

**Variation axis**: Role-phase binding in PAF declaration. All other structure identical to
V-01. Single change: the PRIMARY ANALYTICAL FRAMEWORK declaration explicitly assigns each
dictionary phase to a named role, making the per-role instruction visible in the PAF block
rather than only inferable from the phase instructions.

**Hypothesis**: C-44 requires the PAF declaration to name all three phases of the arc
("from prediction through verification through synthesis"). V-01 satisfies this. V-02's
stronger form explicitly names which role executes each phase: PREDICTOR in Phase 1,
SCANNER in Phase 2, SYNTHESIZER in Phase 3. This transforms the arc from a posture statement
into a per-role execution contract declared in the PAF block itself -- each role can confirm
its responsibility by reading the PAF declaration rather than cross-referencing phase
instructions. This is not captured by C-44 (which requires arc naming, not per-role binding).
Candidate for C-46.

---

```
[All content identical to V-01 through PRIMARY ANALYTICAL FRAMEWORK section, then:]

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill, operating from prediction
through verification through synthesis. PREDICTOR applies it in Phase 1 to generate hypotheses
before reading any file -- each TABLE A prediction must anchor to a dictionary pattern. SCANNER
applies it in Phase 2 to label every TABLE B finding with a dictionary pattern ID -- the Inertia
Match column is the per-row application of this framework to scan evidence. SYNTHESIZER applies
it in Phase 3 to resolve each TABLE A prediction against labeled TABLE B evidence -- every
TABLE G resolution must cite the dictionary pattern that was predicted and the evidence that
confirms, denies, or partially supports it.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

[Identical pattern table and remaining phases as V-01]
```

---

## V-03

**Variation axis**: TABLE G completeness rule with named remediation path. All other structure
identical to V-01. Single change: TABLE G definition in the SCHEMA DECLARATION adds a named
Completeness rule that states both the coverage requirement (every TABLE A Pattern ID must have
a TABLE G row) and the exact remediation step when a prediction is unresolved.

**Hypothesis**: C-43 requires a dedicated TABLE G "whose sole structural purpose is to close
every prediction from the hypothesis table row-by-row." V-01 satisfies this with "Every TABLE A
row must have a TABLE G row. No prediction left unresolved." V-03's stronger form adds a named
Completeness rule that identifies what to do when compliance fails: add TABLE F row of type
prediction-not-resolved. This makes TABLE G non-compliance and its remediation both
structurally visible from the schema alone -- no instruction reading required. The remediation
path closes the loop between the gap table (TABLE F) and the prediction resolution table
(TABLE G), making them structurally linked in the schema rather than linked only by instruction.
This is not captured by C-43 (which describes the purpose declaration, not the completeness
enforcement mechanism). Candidate for C-46.

---

```
[All content identical to V-01 through TABLE G definition, then:]

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

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Remediate: add TABLE F row with Gap set
to "[PATTERN-ID] prediction unresolved", Implication set to "hypothesis not tested against
scan evidence", Source Types Checked set to the source types that were scanned. No prediction
may remain unresolved without a TABLE F gap entry.

[Identical remaining content as V-01]
```

---

## V-04

**Variation axis**: Actor-named boundary headers. All content identical to V-01 except that
all phase boundary section headers use the transfer-actor naming format (PREDICTOR / SCANNER
BOUNDARY) rather than the positional group format (GROUP A / GROUP B BOUNDARY).

**Hypothesis**: C-41 requires "a named structural section header above the exit and entry
condition blocks" at every phase boundary. V-01 satisfies this with GROUP A/B/C/D positional
labels. V-04's stronger form uses PREDICTOR / SCANNER BOUNDARY, SCANNER / GATEKEEPER
BOUNDARY, and GATEKEEPER / SYNTHESIZER BOUNDARY -- naming the actors that transfer control
at each boundary rather than their position in the phase sequence. This adds semantic content
(who hands off to whom) to the structural content (that a named section exists). A reader
scanning the skill can immediately identify not just that a boundary exists but what role
transitions occur there. This is not captured by C-41 (which requires the named header above
both exit and entry blocks, not actor identification in the header). Candidate for C-46.

---

```
[All content identical to V-01 through GROUP A phase instructions, then:]

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. Control transfers to SCANNER. TABLE A must exist.

---

[GROUP B -- SCANNER PHASE content identical to V-01, then:]

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the
same contract. Both must hold.

Gate checklist -- evaluate each item in order; do not skip:
1. At least 3 of 7 source types were scanned
2. TABLE B has at least 5 rows with File Path Evidence populated
3. All Inertia Match cells use I-01 through I-07
4. All Hypothesis Held cells use: yes / no / partial
5. Anti-fabrication confirmed

Write PASS or FAIL token.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

---

[GROUP C -- SYNTHESIZER PHASE content identical to V-01, then:]

---

SYNTHESIZER / END BOUNDARY

Skill complete.

---

[GROUP D identical to V-01]
```

---

## V-05

**Variation axis**: Full combination of V-02 + V-03 + V-04. All three R11 excellence signals
active simultaneously: (a) role-phase binding in PAF declaration, (b) TABLE G completeness
rule with named remediation path, (c) actor-named boundary headers. C-45 table role
attribution preserved as structural invariant.

**Hypothesis**: All three signals reinforce each other structurally. Role-phase binding in PAF
establishes per-role responsibilities at the analytical framework level. TABLE G completeness
rule enforces the consequence of those responsibilities at the schema level. Actor-named
boundaries make the handoffs between those responsibilities structurally visible at every phase
transition. The combination produces the strongest possible structural coherence between the
framework declaration, the schema, and the phase architecture -- each structural layer
explicitly names who does what, what the output requirements are, and what transfers at each
boundary. The full combination may reveal a new pattern not visible in any single axis: the
three signals together constitute a form of structural self-documentation that goes beyond any
individual criterion. Candidate for C-46 or a multi-signal synthesis criterion.

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
| Resolution | REQUIRED (yes / no / partial) |

Completeness rule: every TABLE A Pattern ID must appear as a TABLE G Pattern ID. A TABLE A
prediction with no TABLE G row is a structural gap. Remediate: add TABLE F row with Gap set
to "[PATTERN-ID] prediction unresolved", Implication set to "hypothesis not tested against
scan evidence", Source Types Checked set to the source types that were scanned. No prediction
may remain unresolved without a TABLE F gap entry.

---

GATE TOKEN PROTOCOL

PASS: Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]
FAIL: Path floor not met -- scan incomplete

One of these strings must appear at the Phase 2 / Phase 3 boundary. No prose substitution.

---

PRIMARY ANALYTICAL FRAMEWORK: Inertia Pattern Dictionary

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill, operating from prediction
through verification through synthesis. PREDICTOR applies it in Phase 1 to generate hypotheses
before reading any file -- each TABLE A prediction must anchor to a dictionary pattern. SCANNER
applies it in Phase 2 to label every TABLE B finding with a dictionary pattern ID -- the Inertia
Match column is the per-row application of this framework to scan evidence. SYNTHESIZER applies
it in Phase 3 to resolve each TABLE A prediction against labeled TABLE B evidence -- every
TABLE G resolution must cite the dictionary pattern that was predicted and the evidence that
confirms, denies, or partially supports it.

The dictionary is not a post-hoc classifier -- it is the analytical lens through which each
named role executes its phase of the investigation. Free text in the Inertia Match column is
structurally invalid -- unconstrained values make pattern comparison across runs unverifiable.

Each pattern carries both structural code signals (visible in files) and behavioral signals
(visible in CLAUDE.md prose, team language, ownership language, and incident response patterns).
The PREDICTOR must predict both registers. The SCANNER must check both.

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

-> Output TABLE A.

Phase 1 exit: Write "PREDICTOR COMPLETE -- [N] predictions recorded" before proceeding.

---

PREDICTOR / SCANNER BOUNDARY

PREDICTOR exits. Control transfers to SCANNER. TABLE A must exist.

---

GROUP B -- SCANNER PHASE

Phase 2: Evidence Collection (Role: SCANNER)

Entry condition: PREDICTOR COMPLETE present. TABLE A exists.

Anti-fabrication: Report only findings from files actually read. Record absences. Do not infer
from file names.

Scan at least 3 of 7 source types:
1. CLAUDE.md files (all levels)
2. package.json (root and nested)
3. design/ or docs/ directories
4. Namespace directories
5. Test coverage areas
6. SPECS.md or specification files
7. .roles/ or role definition files

When reading CLAUDE.md files, note team language, ownership language, and escalation language --
these are behavioral signal evidence for TABLE B.

File path floor (gate precondition): 5+ specific file paths in TABLE B. Blocks gate passage.

-> Output TABLE B, TABLE C, TABLE D.

Phase 2 exit: Write "SCANNER COMPLETE -- control transfers to GATEKEEPER".

---

SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION

This gate is the postcondition of Phase 2 and the precondition of Phase 3. Both sides name the
same contract. Both must hold.

Gate checklist -- evaluate each item in order; do not skip:
1. At least 3 of 7 source types were scanned
2. TABLE B has at least 5 rows with File Path Evidence populated
3. All Inertia Match cells use I-01 through I-07
4. All Hypothesis Held cells use: yes / no / partial
5. Anti-fabrication confirmed

Write PASS or FAIL token.

---

GATEKEEPER / SYNTHESIZER BOUNDARY

Control transfers to SYNTHESIZER. FAIL TOKEN halts execution.

---

GROUP C -- SYNTHESIZER PHASE

Phase 3: Synthesis (Role: SYNTHESIZER)

Entry condition: PASS TOKEN present.

CONSTRAINT RESTATEMENT: Raw analysis only. No org chart. No reporting lines. (Stated in
preamble; restated here.)

-> Output TABLE E, TABLE F.
-> Output TABLE G: for every TABLE A row, resolve both the structural prediction and the
   behavioral prediction. Evidence Summary must cite TABLE B rows that speak to each register.
   Completeness rule applies: every TABLE A Pattern ID must have a TABLE G row.
-> Write Org Shape paragraph: dominant pattern from PASS TOKEN. Separate CURRENT STATE from
   RECOMMENDED STATE. Justify from TABLE B structural and behavioral evidence.
-> Write Headcount Range: total FTE range from TABLE C with rationale.

Phase 3 exit: Write "SYNTHESIZER COMPLETE".

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

| Variation | C-45 | Role-phase binding (V-02) | TABLE G completeness rule (V-03) | Actor-named boundaries (V-04) |
|---|---|---|---|---|
| V-01 | YES | NO | NO | NO |
| V-02 | YES | YES | NO | NO |
| V-03 | YES | NO | YES | NO |
| V-04 | YES | NO | NO | YES |
| V-05 | YES | YES | YES | YES |
