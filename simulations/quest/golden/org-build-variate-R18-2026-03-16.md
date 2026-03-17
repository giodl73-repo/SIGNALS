---
skill: quest-variate
skill_target: org-build
round: 18
date: 2026-03-16
rubric_version: 13
---

# Variate R18 -- org-build

5 complete prompt body variations for the `org-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

Rubric v13 adds C-37 (intra-phase sub-step ordering guards) and C-38 (composite typed tokens
encoding mode x compliance). Denominator: 30.

R17 used rubric v12 (denominator 28). R17 V-02 introduced the depth-outcome class
[STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS] for C-31, which structurally anticipated
C-38. C-37 had no coverage in any R17 variation -- sub-step ordering appeared in Task Steps
prose but carried no FORBIDDEN directives at sub-step boundaries. R18 targets explicit
structural coverage of C-37 and C-38 across all variations.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Lifecycle emphasis: maximal phase-gate machinery, all record blocks explicit | V-01 |
| Role sequence: inertia-first ordering (Phase 1 = inertia, Phase 2 = depth flag) | V-02 |
| Output format: table-driven constraints (constraint rows replace bullet lists) | V-03 |
| Phrasing register: dense machine-readable, MUST:/FORBIDDEN: as syntactic first token | V-04 |
| Combination: inertia as organizing principle + full gate machinery | V-05 |

---

## R17 Gap Analysis (rubric v13 lens)

| New Criterion | Best R17 Coverage | Gap |
|---------------|------------------|-----|
| C-37 intra-phase sub-step ordering guards | All R17 variations: Phase 3 named sub-steps A/B/C in Task Steps prose but no FORBIDDEN directives at sub-step boundaries | C-37 requires FORBIDDEN at each sub-step boundary naming both the blocked sub-step and its prerequisite. Generic prose ordering ("complete A before B") fails -- the guard must use FORBIDDEN: and must name both sides. R17 described ordering without guarding it at sub-step granularity. |
| C-38 composite typed tokens encoding mode x compliance | R17 V-02/V-05 (depth-outcome class): introduced [STANDARD-FLOOR-MET \| DEEP-FLOOR-MET \| FLOOR-MISS] for C-31 compliance | R17 V-02 used T2-ROLE-OUTCOME as the composite token but also retained T1-DEPTH-FLAG as a separate field. C-38 specifically requires that mode x compliance collapse into ONE composite token so a reader sees one value and knows both what was attempted (mode) and whether it succeeded (compliance). Retaining T1-DEPTH-FLAG as a record block field alongside the composite token effectively keeps two orthogonal fields. R18 moves T1-DEPTH-FLAG out of Phase 3 record block -- it appears only in Phase 1 as input; Phase 3 emits only the composite outcome. |

Both C-37 and C-38 were structurally anticipated in R17. The gap for C-37 is enforcement at
sub-step granularity; for C-38 it is eliminating the residual second field (T1-DEPTH-FLAG)
from the record block that consumes the composite token.

---

## V-01 -- Lifecycle Emphasis: maximal phase-gate machinery

**Axis**: Lifecycle emphasis
**Hypothesis**: Maximum explicitness at every phase boundary -- double-guard FORBIDDENs,
record blocks with PHASE-ORDERING-GUARD as first field, sub-step FORBIDDENs within Phase 3,
composite typed token for role outcome -- produces the strongest structural compliance signal
across all 30 criteria.

```
You are running `org-build`. Generate a complete org from scan results or directly from a
repo.

Outputs produced:
  1. org-chart.md -- ASCII hierarchy, headcount table, operating rhythm, committee charters,
     org evolution roadmap, anti-pattern watch, inertia assessment verdict.
  2. .craft/roles/{area}/{role}.md -- one file per role, all five fields present.

Input: provide scan results (from /scout or /trace) OR a repo path for direct generation.
Depth flag: --depth standard (default, 20-30 roles) OR --depth deep (50+ roles).

---

## CONSTANTS

Declared once. FORBIDDEN: redefining or restating inside any phase instruction.
Phases reference these tables by name only.

### VERBATIM-IA-SCOPE-TEMPLATES

Keyed to T2-PRESSURE. FORBIDDEN: paraphrasing, adapting, or summarizing.
The inertia-advocate scope field MUST be copied character-for-character from this table.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE        | "The org is structurally stable at current scale. No structural intervention warranted. Monitor for coordination friction as headcount grows beyond the current floor." |
| LOW         | "Minor flat-structure friction detected. Advocate for lightweight handoff protocols before friction compounds. No structural change required this cycle." |
| MODERATE    | "Moderate flat-structure pressure. Advocate for introducing at least one explicit ownership boundary and a formal escalation path within the current planning cycle." |
| HIGH        | "High structural pressure. Advocate for immediate area decomposition and a formal RACI matrix. Deferral increases compounding coordination cost." |
| CRITICAL    | "Critical structural pressure. The org cannot scale without structural intervention this cycle. Advocate for an architecture review with executive sponsorship within 30 days." |

### ANTI-PATTERN-CATEGORY-DERIVATION

| T2-VERDICT          | REQUIRED Categories | FORBIDDEN Categories |
|---------------------|---------------------|----------------------|
| CAN-OPERATE-FLAT    | cat-2, cat-3        | cat-1, cat-4         |
| STRUCTURE-WARRANTED | cat-1, cat-4        | cat-2, cat-3         |

---

## PHASE 1 -- Depth Classification

### Task Steps

1. Read the --depth flag from input.
2. Bind T1-DEPTH-FLAG to `standard` or `deep`.

### Constraints

- MUST bind T1-DEPTH-FLAG before any other phase executes.
- FORBIDDEN: executing Phase 2 before emitting the Phase 1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
===

---

## PHASE 2 -- Inertia Assessment

### Input Contract

- MUST consume T1-DEPTH-FLAG from PHASE-1 record block before executing.
- FORBIDDEN: executing this phase before PHASE-1 record block is emitted.

### Task Steps

Sub-step A -- EVALUATE: Examine structural inputs (scan results or repo). Rate
FLAT-CASE-PRESSURE on the closed set NONE / LOW / MODERATE / HIGH / CRITICAL.

Sub-step B -- VERDICT: Derive T2-VERDICT from FLAT-CASE-PRESSURE.
  If T2-PRESSURE in {NONE, LOW} --> T2-VERDICT = CAN-OPERATE-FLAT.
  If T2-PRESSURE in {MODERATE, HIGH, CRITICAL} --> T2-VERDICT = STRUCTURE-WARRANTED.

- FORBIDDEN: beginning Sub-step B before completing Sub-step A and recording T2-PRESSURE.
- FORBIDDEN: beginning Phase 3 before completing Sub-step B.

### Constraints

- MUST emit exactly one T2-PRESSURE rating from the closed set.
- MUST emit exactly one T2-VERDICT from the closed set.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict.
  Both is an error.
- FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.
- FORBIDDEN: executing Phase 3 before emitting the Phase 2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT:  [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===

---

## PHASE 3 -- Role Enumeration

### Input Contract

- MUST consume T1-DEPTH-FLAG from PHASE-1 record block.
- MUST consume T2-VERDICT from PHASE-2 record block.
- MUST consume T2-PRESSURE from PHASE-2 record block.
- FORBIDDEN: executing this phase before PHASE-2 record block is emitted.

### Task Steps

Sub-step A -- COUNT: Enumerate all role names to be generated.
  T1-DEPTH-FLAG = standard --> MUST enumerate 20-30 roles.
  T1-DEPTH-FLAG = deep     --> MUST enumerate 50+ roles.

- FORBIDDEN: beginning Sub-step B (AREA grouping) before completing Sub-step A (COUNT
  enumeration). Both the sub-step name and its prerequisite must be named in this guard.

Sub-step B -- AREA: Group enumerated roles into area subdirectories.
  MUST produce a minimum of 2 area subdirectories under .craft/roles/.

- FORBIDDEN: beginning Sub-step C (role file generation) before completing Sub-step B
  (AREA grouping).

Sub-step C -- GENERATE: Write .craft/roles/{area}/{role}.md for every enumerated role.
  Every role file MUST contain all five fields: orientation, lens, expertise, scope,
  collaborates_with.
  The inertia-advocate role MUST be present in one area subdirectory.
  The inertia-advocate scope field MUST be copied verbatim from
  VERBATIM-IA-SCOPE-TEMPLATES keyed to T2-PRESSURE.
  FORBIDDEN: paraphrasing, adapting, or summarizing the verbatim scope template text.

### Constraints

- Anti-pattern categories used in Phase 4 Anti-Pattern Watch MUST match
  ANTI-PATTERN-CATEGORY-DERIVATION for the recorded T2-VERDICT value.
- FORBIDDEN: using categories listed in FORBIDDEN Categories for the recorded T2-VERDICT.
- FORBIDDEN: executing Phase 4 before emitting the Phase 3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-AREA-COUNT:   [integer >= 2]
===

Note on T3-ROLE-OUTCOME: this is a composite token encoding mode x compliance.
  STANDARD-FLOOR-MET = T1-DEPTH-FLAG was standard AND role count is within 20-30.
  DEEP-FLOOR-MET     = T1-DEPTH-FLAG was deep AND role count is 50+.
  FLOOR-MISS         = role count fell below the floor for the operative mode.

---

## PHASE 4 -- org-chart.md Generation

### Input Contract

- MUST consume T2-PRESSURE from PHASE-2 record block.
- MUST consume T2-VERDICT from PHASE-2 record block.
- MUST consume T3-ROLE-OUTCOME from PHASE-3 record block.
- MUST consume T3-AREA-COUNT from PHASE-3 record block.
- FORBIDDEN: executing this phase before PHASE-3 record block is emitted.

### Task Steps

Generate org-chart.md containing the following sections in this order:

1. ASCII Hierarchy Diagram -- box/line diagram with minimum 2 org levels.

2. Headcount by Area Table:
   Columns: Area | Headcount | Key Roles | Decides | Escalates.
   MUST include all five columns. A table without Decides and Escalates columns fails.

3. Operating Rhythm Table -- minimum 3 distinct rows covering:
   ROB, shiproom, and at least one governance meeting (each must be a distinct row type).

4. Committee Charters -- one charter per governance meeting, containing:
   Name | Cadence | Owner | Quorum (as N of M fraction) | Decision Scope.
   MUST include all five fields. Quorum MUST be expressed as N of M fraction.

5. Org Evolution Roadmap -- minimum 2 rows:
   Row 1: headcount threshold trigger.
   Row 2: a DIFFERENT trigger category (skill gap, geographic expansion, regulatory, etc.).
   FORBIDDEN: using headcount threshold for both rows.

6. Anti-Pattern Watch Table -- minimum 2 rows:
   Every "Why It Applies Here" cell MUST open with [element name] (cat-N) -- syntax.
   Every Mitigation cell MUST contain a specific remediation action.
   FORBIDDEN: Mitigation cells that contain format guidance or column-structure instructions
   instead of actions.
   Categories MUST be from the REQUIRED set in ANTI-PATTERN-CATEGORY-DERIVATION for
   T2-VERDICT. FORBIDDEN: using categories from the FORBIDDEN set for T2-VERDICT.

7. Inertia Assessment Block:
   FLAT-CASE-PRESSURE: {T2-PRESSURE value}
   Followed by exactly one verdict line: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
   FORBIDDEN: writing both verdicts. Only one verdict. Both is an error.
   FORBIDDEN: omitting both verdicts. Neither is an error.

### Constraints

- MUST use MUST or FORBIDDEN for every constraint statement throughout this phase.
- FORBIDDEN: advisory language (should, prefer, consider, typically) in any constraint
  context within this phase.
- FORBIDDEN: executing Phase 5 before emitting the Phase 4 record block.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-COMPLETE:  [YES | NO]
T4-RHYTHM-ROWS:     [integer >= 3]
T4-CHARTER-COUNT:   [integer >= 1]
===

---

## PHASE 5 -- Artifact Assembly and Verification

### Input Contract

- MUST consume T3-ROLE-OUTCOME from PHASE-3 record block.
- MUST consume T4-CHART-COMPLETE from PHASE-4 record block.
- FORBIDDEN: executing this phase before PHASE-4 record block is emitted.

### Task Steps

1. Confirm T3-ROLE-OUTCOME != FLOOR-MISS.
   If FLOOR-MISS: FORBIDDEN: proceeding. Report role count shortfall and re-execute Phase 3.
2. Confirm T4-CHART-COMPLETE = YES.
3. Emit final artifact manifest.

### Constraints

- MUST confirm all required outputs are present before declaring completion.
- FORBIDDEN: declaring skill complete if T3-ROLE-OUTCOME = FLOOR-MISS.

---

## OUTPUT SKELETON

```
org-chart.md

  [ASCII-HIERARCHY-DIAGRAM -- min 2 levels]

  | Area              | Headcount | Key Roles | Decides | Escalates |
  |-------------------|-----------|-----------|---------|-----------|
  | {{T3-AREA-1}}     | ...       | ...       | ...     | ...       |

  Operating Rhythm
  | Meeting   | Cadence | Owner | Decides |
  | ROB       | ...     | ...   | ...     |

  Inertia Assessment
  FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
  {{T2-VERDICT}}: [conclusion prose]

.craft/roles/{area}/inertia-advocate.md
  orientation:      ...
  lens:             ...
  expertise:        ...
  scope:            {{VERBATIM-IA-SCOPE-TEMPLATES[T2-PRESSURE]}}
  collaborates_with: ...
```
```

---

## V-02 -- Role Sequence: inertia-first ordering

**Axis**: Role sequence
**Hypothesis**: Locking the structural verdict (T2-VERDICT and T2-PRESSURE) before even
reading the depth flag forces all downstream choices -- role count floor, IA scope selection,
anti-pattern categories -- to be verdict-coherent by construction. When the depth flag is
read after the structural verdict, the count floor binding in Phase 2 consumes T1-VERDICT
as an upstream variable, inverting the dependency arrow and surfacing verdict-first discipline
more naturally. Also exploits C-38 most cleanly: the composite token T3-ROLE-OUTCOME can
name the mode it consumed because the mode was not determined until after the structural
verdict, making the composite semantics fully explicit.

```
You are running `org-build`. Generate a complete org from scan results or a repo path.

Outputs:
  1. org-chart.md  2. .craft/roles/{area}/{role}.md (all five fields, all roles)

Depth: --depth standard (20-30 roles, default) or --depth deep (50+ roles).

---

## CONSTANTS

Declared here. FORBIDDEN: embedding, restating, or duplicating inside any phase.

### VERBATIM-IA-SCOPE-TEMPLATES

Keyed to T1-PRESSURE. Apply character-for-character. FORBIDDEN: paraphrase or adaptation.

| T1-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE        | "The org is structurally stable at current scale. No structural intervention warranted. Monitor for coordination friction as headcount grows beyond the current floor." |
| LOW         | "Minor flat-structure friction detected. Advocate for lightweight handoff protocols before friction compounds. No structural change required this cycle." |
| MODERATE    | "Moderate flat-structure pressure. Advocate for introducing at least one explicit ownership boundary and a formal escalation path within the current planning cycle." |
| HIGH        | "High structural pressure. Advocate for immediate area decomposition and a formal RACI matrix. Deferral increases compounding coordination cost." |
| CRITICAL    | "Critical structural pressure. The org cannot scale without structural intervention this cycle. Advocate for an architecture review with executive sponsorship within 30 days." |

### ANTI-PATTERN-CATEGORY-DERIVATION

| T1-VERDICT          | REQUIRED Categories | FORBIDDEN Categories |
|---------------------|---------------------|----------------------|
| CAN-OPERATE-FLAT    | cat-2, cat-3        | cat-1, cat-4         |
| STRUCTURE-WARRANTED | cat-1, cat-4        | cat-2, cat-3         |

---

## PHASE 1 -- Inertia Assessment

This phase precedes depth-flag reading. The structural verdict is the primary gate.
All downstream phases are verdict-coherent by construction.

### Task Steps

Sub-step A -- EVALUATE: Examine structural inputs. Assign FLAT-CASE-PRESSURE rating.
  Valid values: NONE | LOW | MODERATE | HIGH | CRITICAL.

Sub-step B -- VERDICT: Derive T1-VERDICT from T1-PRESSURE.
  T1-PRESSURE in {NONE, LOW}               --> T1-VERDICT = CAN-OPERATE-FLAT.
  T1-PRESSURE in {MODERATE, HIGH, CRITICAL} --> T1-VERDICT = STRUCTURE-WARRANTED.

- FORBIDDEN: beginning Sub-step B (VERDICT derivation) before completing Sub-step A
  (EVALUATE -- T1-PRESSURE recorded).
- FORBIDDEN: beginning Phase 2 before completing Sub-step B (VERDICT derivation).

### Constraints

- MUST emit exactly one T1-PRESSURE from the closed set.
- MUST emit exactly one T1-VERDICT from the closed set.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict.
  Both is an error.
- FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.
- FORBIDDEN: executing Phase 2 before emitting Phase 1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T1-VERDICT:  [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===

---

## PHASE 2 -- Depth Classification

### Input Contract

- MUST consume T1-VERDICT from PHASE-1 record block before executing.
- MUST consume T1-PRESSURE from PHASE-1 record block before executing.
- FORBIDDEN: executing this phase before PHASE-1 record block is emitted.

### Task Steps

1. Read the --depth flag from input.
2. Bind T2-DEPTH-FLAG to `standard` or `deep`.

### Constraints

- MUST bind T2-DEPTH-FLAG before Phase 3 executes.
- FORBIDDEN: executing Phase 3 before emitting Phase 2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-DEPTH-FLAG: [standard | deep]
===

---

## PHASE 3 -- Role Enumeration

### Input Contract

- MUST consume T1-PRESSURE from PHASE-1 record block.
- MUST consume T1-VERDICT from PHASE-1 record block.
- MUST consume T2-DEPTH-FLAG from PHASE-2 record block.
- FORBIDDEN: executing this phase before PHASE-2 record block is emitted.

### Task Steps

Sub-step A -- COUNT: Enumerate all role names respecting the depth-keyed floor.
  T2-DEPTH-FLAG = standard --> MUST enumerate 20-30 roles.
  T2-DEPTH-FLAG = deep     --> MUST enumerate 50+ roles.

- FORBIDDEN: beginning Sub-step B (AREA grouping) before completing Sub-step A (COUNT --
  full role name list recorded).

Sub-step B -- AREA: Assign each enumerated role to an area subdirectory.
  MUST produce minimum 2 area subdirectories under .craft/roles/.

- FORBIDDEN: beginning Sub-step C (file generation) before completing Sub-step B (AREA --
  area assignments recorded).

Sub-step C -- GENERATE: Write .craft/roles/{area}/{role}.md for each role.
  Every file MUST contain: orientation, lens, expertise, scope, collaborates_with.
  The inertia-advocate role MUST be present.
  The inertia-advocate scope MUST be the verbatim text from VERBATIM-IA-SCOPE-TEMPLATES
  keyed to T1-PRESSURE.
  FORBIDDEN: paraphrasing, adapting, or deviating from the verbatim scope template text.

### Constraints

- Anti-pattern categories for Phase 4 MUST match ANTI-PATTERN-CATEGORY-DERIVATION REQUIRED
  set for T1-VERDICT.
- FORBIDDEN: using categories from ANTI-PATTERN-CATEGORY-DERIVATION FORBIDDEN set for
  T1-VERDICT.
- FORBIDDEN: executing Phase 4 before emitting Phase 3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-AREA-COUNT:   [integer >= 2]
===

Note on T3-ROLE-OUTCOME composite token:
  STANDARD-FLOOR-MET = T2-DEPTH-FLAG was standard AND 20-30 roles enumerated.
  DEEP-FLOOR-MET     = T2-DEPTH-FLAG was deep AND 50+ roles enumerated.
  FLOOR-MISS         = role count fell below floor for the operative mode.

---

## PHASE 4 -- org-chart.md Generation

### Input Contract

- MUST consume T1-PRESSURE from PHASE-1 record block.
- MUST consume T1-VERDICT from PHASE-1 record block.
- MUST consume T3-ROLE-OUTCOME from PHASE-3 record block.
- MUST consume T3-AREA-COUNT from PHASE-3 record block.
- FORBIDDEN: executing this phase before PHASE-3 record block is emitted.

### Task Steps

Generate org-chart.md with these sections in order:

1. ASCII Hierarchy Diagram (min 2 org levels, box/line format).

2. Headcount by Area Table:
   Columns: Area | Headcount | Key Roles | Decides | Escalates.
   MUST include all five columns.

3. Operating Rhythm Table (min 3 distinct rows: ROB + shiproom + governance).

4. Committee Charters (one per governance meeting):
   Fields: Name | Cadence | Owner | Quorum (N of M) | Decision Scope.
   Quorum MUST be expressed as N of M fraction.

5. Org Evolution Roadmap (min 2 rows):
   Row 1: headcount threshold trigger.
   Row 2: a different category trigger.
   FORBIDDEN: two headcount threshold rows.

6. Anti-Pattern Watch (min 2 rows):
   Every "Why It Applies Here" cell MUST open with [element name] (cat-N) -- syntax.
   Every Mitigation cell MUST contain a specific remediation action.
   FORBIDDEN: Mitigation cells containing format guidance instead of actions.
   Categories MUST come from ANTI-PATTERN-CATEGORY-DERIVATION REQUIRED set for T1-VERDICT.
   FORBIDDEN: using categories from FORBIDDEN set for T1-VERDICT.

7. Inertia Assessment Block:
   FLAT-CASE-PRESSURE: {T1-PRESSURE}
   Exactly one verdict: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
   FORBIDDEN: writing both verdicts. Both is an error.
   FORBIDDEN: omitting both verdicts. Neither is an error.

### Constraints

- MUST use MUST or FORBIDDEN for every constraint statement in this phase.
- FORBIDDEN: advisory language in any constraint context.
- FORBIDDEN: executing Phase 5 before emitting Phase 4 record block.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-COMPLETE: [YES | NO]
T4-RHYTHM-ROWS:    [integer >= 3]
T4-CHARTER-COUNT:  [integer >= 1]
===

---

## PHASE 5 -- Verification

### Input Contract

- MUST consume T3-ROLE-OUTCOME from PHASE-3 record block.
- MUST consume T4-CHART-COMPLETE from PHASE-4 record block.
- FORBIDDEN: executing this phase before PHASE-4 record block is emitted.

### Task Steps

1. Confirm T3-ROLE-OUTCOME != FLOOR-MISS.
   FORBIDDEN: proceeding if T3-ROLE-OUTCOME = FLOOR-MISS. Re-execute Phase 3.
2. Confirm T4-CHART-COMPLETE = YES.
3. Emit artifact manifest.

### Constraints

- MUST confirm all outputs before declaring completion.
- FORBIDDEN: declaring complete if T3-ROLE-OUTCOME = FLOOR-MISS.
```

---

## V-03 -- Output Format: table-driven constraints

**Axis**: Output format
**Hypothesis**: Expressing all constraints as table rows (Type | Applies-To | Constraint
columns) rather than bullet lists makes each constraint independently auditable at a glance
and directly satisfies C-30 (structural segmentation) and C-33 (independent auditability of
Input Contract sections) by making the constraint class visually scannable without reading
task prose.

```
You are running `org-build`. Generate a complete org from scan results or a repo.

Outputs:
  1. org-chart.md (hierarchy, headcount, rhythm, charters, roadmap, anti-patterns, verdict)
  2. .craft/roles/{area}/{role}.md (every role, all five fields)

Depth: --depth standard (20-30 roles) | --depth deep (50+ roles). Default: standard.

---

## CONSTANTS

FORBIDDEN: embedding, restating, or duplicating these tables inside any phase.

### VERBATIM-IA-SCOPE-TEMPLATES

| T2-PRESSURE | Verbatim Scope Text (copy character-for-character) |
|-------------|-----------------------------------------------------|
| NONE        | "The org is structurally stable at current scale. No structural intervention warranted. Monitor for coordination friction as headcount grows beyond the current floor." |
| LOW         | "Minor flat-structure friction detected. Advocate for lightweight handoff protocols before friction compounds. No structural change required this cycle." |
| MODERATE    | "Moderate flat-structure pressure. Advocate for introducing at least one explicit ownership boundary and a formal escalation path within the current planning cycle." |
| HIGH        | "High structural pressure. Advocate for immediate area decomposition and a formal RACI matrix. Deferral increases compounding coordination cost." |
| CRITICAL    | "Critical structural pressure. The org cannot scale without structural intervention this cycle. Advocate for an architecture review with executive sponsorship within 30 days." |

### ANTI-PATTERN-CATEGORY-DERIVATION

| T2-VERDICT          | REQUIRED Categories | FORBIDDEN Categories |
|---------------------|---------------------|----------------------|
| CAN-OPERATE-FLAT    | cat-2, cat-3        | cat-1, cat-4         |
| STRUCTURE-WARRANTED | cat-1, cat-4        | cat-2, cat-3         |

---

## PHASE 1 -- Depth Classification

### Task Steps

Read the --depth flag. Bind T1-DEPTH-FLAG.

### Input Contract

(No upstream variables. First phase.)

### Constraints

| Type     | Applies-To     | Constraint |
|----------|----------------|------------|
| MUST     | T1-DEPTH-FLAG  | MUST bind to exactly one value from [standard \| deep] |
| FORBIDDEN | Phase 2 start | FORBIDDEN: Phase 2 begins before Phase 1 record block is emitted |

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
===

---

## PHASE 2 -- Inertia Assessment

### Task Steps

Sub-step A -- EVALUATE: Rate FLAT-CASE-PRESSURE on structural inputs.
Sub-step B -- VERDICT: Derive T2-VERDICT from T2-PRESSURE.
  {NONE, LOW} --> CAN-OPERATE-FLAT. {MODERATE, HIGH, CRITICAL} --> STRUCTURE-WARRANTED.

### Input Contract

| Variable      | Source  | Binding |
|---------------|---------|---------|
| T1-DEPTH-FLAG | PHASE-1 | MUST be present before this phase executes |

### Constraints

| Type     | Applies-To             | Constraint |
|----------|------------------------|------------|
| MUST     | T2-PRESSURE            | MUST emit exactly one value from [NONE \| LOW \| MODERATE \| HIGH \| CRITICAL] |
| MUST     | T2-VERDICT             | MUST emit exactly one value from [CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED] |
| FORBIDDEN | Sub-step B start      | FORBIDDEN: beginning Sub-step B (VERDICT) before completing Sub-step A (EVALUATE -- T2-PRESSURE recorded) |
| FORBIDDEN | Dual verdict          | FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict. Both is an error. |
| FORBIDDEN | Null verdict          | FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error. |
| FORBIDDEN | Phase 3 start         | FORBIDDEN: Phase 3 begins before Phase 2 record block is emitted |

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT:  [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===

---

## PHASE 3 -- Role Enumeration

### Task Steps

Sub-step A -- COUNT: Enumerate all role names.
Sub-step B -- AREA: Group roles into area subdirectories (min 2).
Sub-step C -- GENERATE: Write .craft/roles/{area}/{role}.md for each role.

### Input Contract

| Variable     | Source  | Binding |
|--------------|---------|---------|
| T1-DEPTH-FLAG | PHASE-1 | MUST be present; determines count floor (see Constraints) |
| T2-VERDICT   | PHASE-2 | MUST be present; determines anti-pattern category set |
| T2-PRESSURE  | PHASE-2 | MUST be present; keys IA scope template |

### Constraints

| Type     | Applies-To                   | Constraint |
|----------|------------------------------|------------|
| MUST     | Role count (standard)        | MUST enumerate 20-30 roles when T1-DEPTH-FLAG = standard |
| MUST     | Role count (deep)            | MUST enumerate 50+ roles when T1-DEPTH-FLAG = deep |
| MUST     | Area count                   | MUST produce minimum 2 area subdirectories |
| MUST     | inertia-advocate             | MUST be present in one area subdirectory |
| MUST     | IA scope text                | MUST copy verbatim from VERBATIM-IA-SCOPE-TEMPLATES keyed to T2-PRESSURE |
| MUST     | All role fields              | Every role file MUST contain orientation, lens, expertise, scope, collaborates_with |
| FORBIDDEN | Sub-step B before A         | FORBIDDEN: beginning Sub-step B (AREA) before completing Sub-step A (COUNT -- role name list recorded) |
| FORBIDDEN | Sub-step C before B         | FORBIDDEN: beginning Sub-step C (GENERATE) before completing Sub-step B (AREA -- area assignments recorded) |
| FORBIDDEN | IA scope paraphrase         | FORBIDDEN: paraphrasing, adapting, or summarizing the verbatim scope template |
| FORBIDDEN | Wrong anti-pattern cats     | FORBIDDEN: using categories listed in FORBIDDEN Categories for T2-VERDICT in ANTI-PATTERN-CATEGORY-DERIVATION |
| FORBIDDEN | Phase 4 start               | FORBIDDEN: Phase 4 begins before Phase 3 record block is emitted |

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-AREA-COUNT:   [integer >= 2]
===

T3-ROLE-OUTCOME composite token semantics:
  STANDARD-FLOOR-MET = T1-DEPTH-FLAG was standard AND 20-30 roles enumerated.
  DEEP-FLOOR-MET     = T1-DEPTH-FLAG was deep AND 50+ roles enumerated.
  FLOOR-MISS         = count fell below the floor for the operative mode.

---

## PHASE 4 -- org-chart.md Generation

### Task Steps

Write org-chart.md sections in order:
  1. ASCII Hierarchy Diagram (min 2 levels).
  2. Headcount by Area Table (Area | Headcount | Key Roles | Decides | Escalates).
  3. Operating Rhythm Table (min 3 distinct rows: ROB, shiproom, governance).
  4. Committee Charters (Name | Cadence | Owner | Quorum as N/M | Decision Scope).
  5. Org Evolution Roadmap (min 2 rows, Row 1 headcount trigger, Row 2 different category).
  6. Anti-Pattern Watch (min 2 rows, cat-N typed citations, remediation actions).
  7. Inertia Assessment Block (FLAT-CASE-PRESSURE + single verdict).

### Input Contract

| Variable         | Source  | Binding |
|------------------|---------|---------|
| T2-PRESSURE      | PHASE-2 | MUST be present; used in Inertia Assessment Block |
| T2-VERDICT       | PHASE-2 | MUST be present; governs anti-pattern category set |
| T3-ROLE-OUTCOME  | PHASE-3 | MUST be present before chart generation begins |
| T3-AREA-COUNT    | PHASE-3 | MUST be present; used in area table row count |

### Constraints

| Type     | Applies-To                   | Constraint |
|----------|------------------------------|------------|
| MUST     | Headcount table columns      | MUST include Area, Headcount, Key Roles, Decides, Escalates |
| MUST     | Rhythm rows                  | MUST include minimum 3 distinct rows (ROB + shiproom + governance) |
| MUST     | Charter fields               | MUST include Name, Cadence, Owner, Quorum (N of M), Decision Scope |
| MUST     | Quorum format                | MUST express Quorum as N of M fraction |
| MUST     | Anti-pattern citation        | Every "Why It Applies Here" cell MUST open with [element name] (cat-N) -- syntax |
| MUST     | Mitigation actions           | Every Mitigation cell MUST contain a specific remediation action |
| MUST     | Single inertia verdict       | MUST emit exactly one verdict in the Inertia Assessment Block |
| FORBIDDEN | Missing Decides/Escalates   | FORBIDDEN: headcount table without Decides and Escalates columns |
| FORBIDDEN | Dual roadmap trigger type   | FORBIDDEN: both Org Evolution Roadmap rows using headcount threshold as trigger |
| FORBIDDEN | Mitigation format guidance  | FORBIDDEN: Mitigation cells containing format guidance instead of remediation actions |
| FORBIDDEN | Wrong anti-pattern cats     | FORBIDDEN: anti-pattern categories from the FORBIDDEN set for T2-VERDICT |
| FORBIDDEN | Dual verdict                | FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Both is an error. |
| FORBIDDEN | Null verdict                | FORBIDDEN: omitting both verdicts. Neither is an error. |
| FORBIDDEN | Phase 5 start               | FORBIDDEN: Phase 5 begins before Phase 4 record block is emitted |

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-COMPLETE: [YES | NO]
T4-RHYTHM-ROWS:    [integer >= 3]
T4-CHARTER-COUNT:  [integer >= 1]
===

---

## PHASE 5 -- Verification

### Task Steps

Confirm T3-ROLE-OUTCOME != FLOOR-MISS. Confirm T4-CHART-COMPLETE = YES. Emit manifest.

### Input Contract

| Variable         | Source  | Binding |
|------------------|---------|---------|
| T3-ROLE-OUTCOME  | PHASE-3 | MUST equal STANDARD-FLOOR-MET or DEEP-FLOOR-MET to proceed |
| T4-CHART-COMPLETE | PHASE-4 | MUST equal YES to proceed |

### Constraints

| Type     | Applies-To         | Constraint |
|----------|--------------------|------------|
| MUST     | Role floor check   | MUST confirm T3-ROLE-OUTCOME != FLOOR-MISS before declaring complete |
| MUST     | Chart check        | MUST confirm T4-CHART-COMPLETE = YES before declaring complete |
| FORBIDDEN | Proceed on miss   | FORBIDDEN: declaring complete when T3-ROLE-OUTCOME = FLOOR-MISS. Re-execute Phase 3. |
```

---

## V-04 -- Phrasing Register: dense machine-readable, keyword-first

**Axis**: Phrasing register
**Hypothesis**: Writing every instruction with MUST: or FORBIDDEN: as the syntactic first
token -- even in Task Steps -- reduces the interpretive surface for ambiguity. When the
register keyword precedes the action rather than being embedded in it, a model scanning for
constraint-class content finds it at token position 1 without parsing the sentence. This
hypothesis targets C-29 (all prohibitions as FORBIDDEN:) and C-21 (constraint-completeness
seal) by making every line classifiable from its first token.

```
You are running `org-build`.

MUST generate: (1) org-chart.md (2) .craft/roles/{area}/{role}.md for every role.
MUST accept: scan results from /scout or /trace, OR a repo path for direct generation.
MUST accept: --depth standard (20-30 roles, default) or --depth deep (50+ roles).

---

## CONSTANTS

FORBIDDEN: embedding, restating, or duplicating inside any phase instruction.

### VERBATIM-IA-SCOPE-TEMPLATES

MUST apply verbatim. FORBIDDEN: paraphrase. FORBIDDEN: adaptation. FORBIDDEN: summarization.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE        | "The org is structurally stable at current scale. No structural intervention warranted. Monitor for coordination friction as headcount grows beyond the current floor." |
| LOW         | "Minor flat-structure friction detected. Advocate for lightweight handoff protocols before friction compounds. No structural change required this cycle." |
| MODERATE    | "Moderate flat-structure pressure. Advocate for introducing at least one explicit ownership boundary and a formal escalation path within the current planning cycle." |
| HIGH        | "High structural pressure. Advocate for immediate area decomposition and a formal RACI matrix. Deferral increases compounding coordination cost." |
| CRITICAL    | "Critical structural pressure. The org cannot scale without structural intervention this cycle. Advocate for an architecture review with executive sponsorship within 30 days." |

### ANTI-PATTERN-CATEGORY-DERIVATION

| T2-VERDICT          | REQUIRED Categories | FORBIDDEN Categories |
|---------------------|---------------------|----------------------|
| CAN-OPERATE-FLAT    | cat-2, cat-3        | cat-1, cat-4         |
| STRUCTURE-WARRANTED | cat-1, cat-4        | cat-2, cat-3         |

---

## PHASE 1 -- Depth Classification

### Task Steps

MUST: read --depth flag from input.
MUST: bind T1-DEPTH-FLAG to one value from [standard | deep].

### Constraints

MUST: emit PHASE-1 record block before any other phase.
FORBIDDEN: beginning Phase 2 before emitting PHASE-1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
===

---

## PHASE 2 -- Inertia Assessment

### Input Contract

MUST: consume T1-DEPTH-FLAG from PHASE-1 record block.
FORBIDDEN: executing Phase 2 before PHASE-1 record block is emitted.

### Task Steps

Sub-step A -- EVALUATE:
MUST: examine structural inputs.
MUST: rate FLAT-CASE-PRESSURE from closed set [NONE | LOW | MODERATE | HIGH | CRITICAL].

Sub-step B -- VERDICT:
MUST: derive T2-VERDICT from T2-PRESSURE using rule:
  T2-PRESSURE in {NONE, LOW}               --> MUST: set T2-VERDICT = CAN-OPERATE-FLAT.
  T2-PRESSURE in {MODERATE, HIGH, CRITICAL} --> MUST: set T2-VERDICT = STRUCTURE-WARRANTED.

FORBIDDEN: beginning Sub-step B (VERDICT derivation) before completing Sub-step A
  (EVALUATE -- T2-PRESSURE recorded in working state).

### Constraints

MUST: emit exactly one T2-PRESSURE from closed set.
MUST: emit exactly one T2-VERDICT from closed set.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict.
  Both is an error.
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.
FORBIDDEN: beginning Phase 3 before emitting PHASE-2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT:  [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===

---

## PHASE 3 -- Role Enumeration

### Input Contract

MUST: consume T1-DEPTH-FLAG from PHASE-1 record block.
MUST: consume T2-VERDICT from PHASE-2 record block.
MUST: consume T2-PRESSURE from PHASE-2 record block.
FORBIDDEN: executing Phase 3 before PHASE-2 record block is emitted.

### Task Steps

Sub-step A -- COUNT:
MUST: enumerate all role names.
MUST: count MUST satisfy depth floor:
  T1-DEPTH-FLAG = standard --> MUST enumerate 20-30 roles.
  T1-DEPTH-FLAG = deep     --> MUST enumerate 50+ roles.

FORBIDDEN: beginning Sub-step B (AREA grouping) before completing Sub-step A
  (COUNT -- full role name list recorded in working state).

Sub-step B -- AREA:
MUST: group enumerated roles into area subdirectories.
MUST: produce minimum 2 area subdirectories under .craft/roles/.

FORBIDDEN: beginning Sub-step C (GENERATE) before completing Sub-step B
  (AREA -- area assignments recorded in working state).

Sub-step C -- GENERATE:
MUST: write .craft/roles/{area}/{role}.md for every enumerated role.
MUST: include all five fields in every file: orientation, lens, expertise, scope,
  collaborates_with.
MUST: include inertia-advocate role in one area subdirectory.
MUST: copy inertia-advocate scope verbatim from VERBATIM-IA-SCOPE-TEMPLATES keyed to
  T2-PRESSURE.
FORBIDDEN: paraphrasing, adapting, or deviating from the verbatim scope template text.

### Constraints

MUST: use only REQUIRED categories from ANTI-PATTERN-CATEGORY-DERIVATION for T2-VERDICT.
FORBIDDEN: using categories from FORBIDDEN Categories column for T2-VERDICT.
FORBIDDEN: beginning Phase 4 before emitting PHASE-3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-AREA-COUNT:   [integer >= 2]
===

T3-ROLE-OUTCOME composite token:
  STANDARD-FLOOR-MET = T1-DEPTH-FLAG was standard AND 20-30 roles enumerated.
  DEEP-FLOOR-MET     = T1-DEPTH-FLAG was deep AND 50+ roles enumerated.
  FLOOR-MISS         = count below floor for operative mode.

---

## PHASE 4 -- org-chart.md Generation

### Input Contract

MUST: consume T2-PRESSURE from PHASE-2 record block.
MUST: consume T2-VERDICT from PHASE-2 record block.
MUST: consume T3-ROLE-OUTCOME from PHASE-3 record block.
MUST: consume T3-AREA-COUNT from PHASE-3 record block.
FORBIDDEN: executing Phase 4 before PHASE-3 record block is emitted.

### Task Steps

MUST: write org-chart.md containing all of the following, in this order:

1. ASCII Hierarchy Diagram:
   MUST: include box/line diagram with minimum 2 org levels.

2. Headcount by Area Table:
   MUST: include columns Area, Headcount, Key Roles, Decides, Escalates.
   FORBIDDEN: omitting Decides or Escalates columns.

3. Operating Rhythm Table:
   MUST: include minimum 3 distinct rows (ROB + shiproom + governance).
   FORBIDDEN: using the same row type more than once to satisfy the minimum.

4. Committee Charters:
   MUST: include one charter per governance meeting.
   MUST: include fields Name, Cadence, Owner, Quorum, Decision Scope.
   MUST: express Quorum as N of M fraction.

5. Org Evolution Roadmap:
   MUST: include minimum 2 rows.
   MUST: Row 1 is a headcount threshold trigger.
   MUST: Row 2 is a DIFFERENT category trigger.
   FORBIDDEN: both rows using headcount threshold as trigger.

6. Anti-Pattern Watch:
   MUST: include minimum 2 rows.
   MUST: every "Why It Applies Here" cell opens with [element name] (cat-N) -- syntax.
   MUST: every Mitigation cell contains a specific remediation action.
   FORBIDDEN: Mitigation cells containing format guidance instead of remediation actions.
   MUST: categories come from ANTI-PATTERN-CATEGORY-DERIVATION REQUIRED set for T2-VERDICT.
   FORBIDDEN: using categories from FORBIDDEN set for T2-VERDICT.

7. Inertia Assessment Block:
   MUST: emit FLAT-CASE-PRESSURE: {T2-PRESSURE value}.
   MUST: emit exactly one verdict: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
   FORBIDDEN: writing both verdicts. Both is an error.
   FORBIDDEN: omitting both verdicts. Neither is an error.

### Constraints

MUST: use MUST or FORBIDDEN for every constraint statement in this phase.
FORBIDDEN: advisory language (should, prefer, consider, typically) in any constraint context.
FORBIDDEN: beginning Phase 5 before emitting PHASE-4 record block.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-COMPLETE: [YES | NO]
T4-RHYTHM-ROWS:    [integer >= 3]
T4-CHARTER-COUNT:  [integer >= 1]
===

---

## PHASE 5 -- Verification

### Input Contract

MUST: consume T3-ROLE-OUTCOME from PHASE-3 record block.
MUST: consume T4-CHART-COMPLETE from PHASE-4 record block.
FORBIDDEN: executing Phase 5 before PHASE-4 record block is emitted.

### Task Steps

MUST: confirm T3-ROLE-OUTCOME != FLOOR-MISS.
  FORBIDDEN: proceeding when T3-ROLE-OUTCOME = FLOOR-MISS. Re-execute Phase 3.
MUST: confirm T4-CHART-COMPLETE = YES.
MUST: emit artifact manifest listing all generated files.

### Constraints

MUST: confirm all required outputs before declaring completion.
FORBIDDEN: declaring complete when T3-ROLE-OUTCOME = FLOOR-MISS.
```

---

## V-05 -- Combination: inertia as organizing principle + full gate machinery

**Axis**: Inertia framing + Lifecycle emphasis
**Hypothesis**: Framing inertia-advocate as the PRIMARY output of the skill -- the structural
verdict the org-chart is derived from, rather than a role among roles -- produces stronger
coherence across C-08 (inertia assessment with rated verdict), C-11 (IA scope references
FLAT-CASE-PRESSURE), C-17 (verbatim scope template), and C-35 (inertia phase before role
enumeration). The inertia verdict is declared as a "primary gate" in the preamble; all other
outputs are "verdicted artifacts" that flow from it. Full gate machinery is retained.

```
You are running `org-build`.

Primary gate: the inertia assessment. Every artifact produced by this skill is a
verdicted artifact -- its structure is determined by the T2-VERDICT and T2-PRESSURE
values established in Phase 2 before any role enumeration, chart generation, or
anti-pattern selection occurs.

Outputs:
  1. org-chart.md -- a verdicted org chart: its inertia assessment block, anti-pattern
     categories, and IA scope template are all keyed to T2-VERDICT and T2-PRESSURE.
  2. .craft/roles/{area}/{role}.md -- verdicted role files, including inertia-advocate
     whose scope is copied verbatim from the pressure-keyed template.

Input: scan results or repo path. Depth: --depth standard (20-30) | --depth deep (50+).

---

## CONSTANTS

Declared once. FORBIDDEN: embedding, restating, or duplicating inside any phase.

### VERBATIM-IA-SCOPE-TEMPLATES

These are the only permissible scope values for the inertia-advocate role.
FORBIDDEN: any scope text for inertia-advocate that is not character-for-character from
this table, keyed to the T2-PRESSURE value recorded in the Phase 2 record block.

| T2-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE        | "The org is structurally stable at current scale. No structural intervention warranted. Monitor for coordination friction as headcount grows beyond the current floor." |
| LOW         | "Minor flat-structure friction detected. Advocate for lightweight handoff protocols before friction compounds. No structural change required this cycle." |
| MODERATE    | "Moderate flat-structure pressure. Advocate for introducing at least one explicit ownership boundary and a formal escalation path within the current planning cycle." |
| HIGH        | "High structural pressure. Advocate for immediate area decomposition and a formal RACI matrix. Deferral increases compounding coordination cost." |
| CRITICAL    | "Critical structural pressure. The org cannot scale without structural intervention this cycle. Advocate for an architecture review with executive sponsorship within 30 days." |

### ANTI-PATTERN-CATEGORY-DERIVATION

Category selection is verdict-derived. A flat org (CAN-OPERATE-FLAT) exposes different
structural failure modes than a warranted hierarchy (STRUCTURE-WARRANTED). Categories
independent of the verdict are a scoring error.

| T2-VERDICT          | REQUIRED Categories | FORBIDDEN Categories |
|---------------------|---------------------|----------------------|
| CAN-OPERATE-FLAT    | cat-2, cat-3        | cat-1, cat-4         |
| STRUCTURE-WARRANTED | cat-1, cat-4        | cat-2, cat-3         |

---

## PHASE 1 -- Depth Classification

The depth flag determines the role count floor. It is read before the structural assessment
so that the inertia assessment in Phase 2 operates with full context.

### Task Steps

1. Read --depth flag. Bind T1-DEPTH-FLAG to [standard | deep].

### Constraints

- MUST bind T1-DEPTH-FLAG before Phase 2 executes.
- FORBIDDEN: executing Phase 2 before emitting Phase 1 record block.

=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]
===

---

## PHASE 2 -- Inertia Assessment (PRIMARY GATE)

This is the primary gate. All downstream verdicted artifacts derive from T2-VERDICT
and T2-PRESSURE. The org-chart, role files, anti-pattern categories, and IA scope
template are all locked here before any enumeration begins.

### Input Contract

- MUST consume T1-DEPTH-FLAG from PHASE-1 record block before executing.
- FORBIDDEN: executing Phase 2 before PHASE-1 record block is emitted.

### Task Steps

Sub-step A -- STRUCTURAL SCAN: Examine inputs. Rate FLAT-CASE-PRESSURE.
  Valid values: NONE | LOW | MODERATE | HIGH | CRITICAL.
  This is the inertia-advocate's operating context -- the pressure level the role exists
  to surface and respond to.

Sub-step B -- VERDICT LOCK: Derive T2-VERDICT from T2-PRESSURE.
  T2-PRESSURE in {NONE, LOW}               --> T2-VERDICT = CAN-OPERATE-FLAT.
  T2-PRESSURE in {MODERATE, HIGH, CRITICAL} --> T2-VERDICT = STRUCTURE-WARRANTED.
  This verdict gates all subsequent verdicted artifact generation.

- FORBIDDEN: beginning Sub-step B (VERDICT LOCK) before completing Sub-step A
  (STRUCTURAL SCAN -- T2-PRESSURE recorded).
- FORBIDDEN: beginning Phase 3 before completing Sub-step B (VERDICT LOCK --
  T2-VERDICT recorded).

### Constraints

- MUST emit exactly one T2-PRESSURE rating from the closed set.
- MUST emit exactly one T2-VERDICT from the closed set.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict.
  Both is an error.
- FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Neither is an error.
- FORBIDDEN: executing Phase 3 before emitting Phase 2 record block.

=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT:  [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===

---

## PHASE 3 -- Role Enumeration (VERDICTED)

All choices in this phase are constrained by T2-VERDICT and T2-PRESSURE from the
primary gate. The inertia-advocate role is the first role placed; all other roles are
positioned relative to the structural verdict it embodies.

### Input Contract

- MUST consume T1-DEPTH-FLAG from PHASE-1 record block.
- MUST consume T2-VERDICT from PHASE-2 record block.
- MUST consume T2-PRESSURE from PHASE-2 record block.
- FORBIDDEN: executing Phase 3 before PHASE-2 record block is emitted.

### Task Steps

Sub-step A -- COUNT: Enumerate all role names, anchored to depth floor.
  T1-DEPTH-FLAG = standard --> MUST enumerate 20-30 roles.
  T1-DEPTH-FLAG = deep     --> MUST enumerate 50+ roles.
  The inertia-advocate MUST appear in this enumeration.

- FORBIDDEN: beginning Sub-step B (AREA grouping) before completing Sub-step A
  (COUNT -- full role name list including inertia-advocate recorded).

Sub-step B -- AREA: Group roles into area subdirectories.
  MUST produce minimum 2 area subdirectories under .craft/roles/.
  The inertia-advocate MUST be assigned to an area subdirectory in this sub-step.

- FORBIDDEN: beginning Sub-step C (GENERATE) before completing Sub-step B
  (AREA -- all roles including inertia-advocate assigned to area subdirectories).

Sub-step C -- GENERATE: Write all role files.
  Every .craft/roles/{area}/{role}.md MUST contain:
    orientation, lens, expertise, scope, collaborates_with.
  The inertia-advocate scope MUST be copied verbatim from VERBATIM-IA-SCOPE-TEMPLATES
  keyed to T2-PRESSURE. This is a verdicted artifact: the scope text is determined by
  the primary gate, not composed at write time.
  FORBIDDEN: paraphrasing, adapting, or deviating from the verbatim scope template text.

### Constraints

- Anti-pattern categories for Phase 4 MUST use the REQUIRED set from
  ANTI-PATTERN-CATEGORY-DERIVATION for T2-VERDICT.
- FORBIDDEN: using categories from the FORBIDDEN set for T2-VERDICT.
- FORBIDDEN: executing Phase 4 before emitting Phase 3 record block.

=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]
T3-AREA-COUNT:   [integer >= 2]
===

T3-ROLE-OUTCOME composite token semantics:
  STANDARD-FLOOR-MET = T1-DEPTH-FLAG was standard AND 20-30 roles enumerated.
  DEEP-FLOOR-MET     = T1-DEPTH-FLAG was deep AND 50+ roles enumerated.
  FLOOR-MISS         = count below floor for operative mode. Fail gate.

---

## PHASE 4 -- org-chart.md Generation (VERDICTED)

The org-chart is a verdicted artifact. Its inertia assessment block mirrors T2-VERDICT
and T2-PRESSURE from the primary gate. Anti-pattern categories are verdict-derived.
The chart does not determine the verdict -- it records it.

### Input Contract

- MUST consume T2-PRESSURE from PHASE-2 record block.
- MUST consume T2-VERDICT from PHASE-2 record block.
- MUST consume T3-ROLE-OUTCOME from PHASE-3 record block.
- MUST consume T3-AREA-COUNT from PHASE-3 record block.
- FORBIDDEN: executing Phase 4 before PHASE-3 record block is emitted.

### Task Steps

Generate org-chart.md with these sections in order:

1. ASCII Hierarchy Diagram (min 2 org levels, box/line format).

2. Headcount by Area Table:
   Columns: Area | Headcount | Key Roles | Decides | Escalates.
   MUST include all five columns. FORBIDDEN: table without Decides and Escalates columns.

3. Operating Rhythm Table:
   MUST include minimum 3 distinct rows: ROB, shiproom, and at least one governance
   meeting. Each must be a distinct row type.

4. Committee Charters:
   MUST include one charter per governance meeting.
   Fields: Name | Cadence | Owner | Quorum (N of M fraction) | Decision Scope.
   MUST include all five fields. MUST express Quorum as N of M fraction.

5. Org Evolution Roadmap:
   MUST include minimum 2 rows.
   Row 1: headcount threshold trigger (typed).
   Row 2: a different trigger category (skill gap, geographic expansion, regulatory, etc.).
   FORBIDDEN: both rows using headcount threshold.

6. Anti-Pattern Watch (verdicted):
   MUST include minimum 2 rows.
   Every "Why It Applies Here" cell MUST open with [element name] (cat-N) -- syntax.
   Category set MUST match ANTI-PATTERN-CATEGORY-DERIVATION REQUIRED for T2-VERDICT.
   FORBIDDEN: categories from the FORBIDDEN set for T2-VERDICT.
   Every Mitigation cell MUST contain a specific remediation action.
   FORBIDDEN: Mitigation cells containing format guidance instead of actions.

7. Inertia Assessment Block (verdicted):
   FLAT-CASE-PRESSURE: {T2-PRESSURE}
   Exactly one verdict line: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED (copied from primary
   gate, not re-evaluated).
   FORBIDDEN: writing both verdicts. Both is an error.
   FORBIDDEN: omitting both verdicts. Neither is an error.

### Constraints

- MUST use MUST or FORBIDDEN for every constraint statement in this phase.
- FORBIDDEN: advisory language (should, prefer, consider, typically) in any constraint
  context in this phase.
- FORBIDDEN: executing Phase 5 before emitting Phase 4 record block.

=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-COMPLETE: [YES | NO]
T4-RHYTHM-ROWS:    [integer >= 3]
T4-CHARTER-COUNT:  [integer >= 1]
===

---

## PHASE 5 -- Verification

### Input Contract

- MUST consume T3-ROLE-OUTCOME from PHASE-3 record block.
- MUST consume T4-CHART-COMPLETE from PHASE-4 record block.
- FORBIDDEN: executing Phase 5 before PHASE-4 record block is emitted.

### Task Steps

1. Confirm T3-ROLE-OUTCOME != FLOOR-MISS.
   FORBIDDEN: proceeding when T3-ROLE-OUTCOME = FLOOR-MISS. Report shortfall.
   Re-execute Phase 3 from Sub-step A.
2. Confirm T4-CHART-COMPLETE = YES.
3. Emit artifact manifest: org-chart.md path + all .craft/roles/{area}/{role}.md paths.

### Constraints

- MUST confirm all primary gate and verdicted artifact outputs before declaring complete.
- FORBIDDEN: declaring complete when T3-ROLE-OUTCOME = FLOOR-MISS.

---

## OUTPUT SKELETON

```
org-chart.md

  [ASCII-BOX-DIAGRAM]
      +--[CEO/CTO]--+
      |             |
  [Area-A]      [Area-B]

  | Area       | Headcount | Key Roles | Decides          | Escalates     |
  |------------|-----------|-----------|------------------|---------------|
  | {{AREA-1}} | ...       | ...       | ...              | ...           |

  Operating Rhythm
  | Meeting  | Cadence | Owner | Decides        |
  | ROB      | weekly  | ...   | ...            |
  | Shiproom | weekly  | ...   | ...            |
  | Arch Gov | monthly | ...   | ...            |

  Committee Charter: Arch Gov
  Name: ... | Cadence: ... | Owner: ... | Quorum: N of M | Decision Scope: ...

  Org Evolution Roadmap
  | Trigger Type       | Threshold         | Recommended Action |
  | Headcount          | > 40 ICs          | ...                |
  | Skill gap          | No ML expertise   | ...                |

  Anti-Pattern Watch
  | Anti-Pattern           | Why It Applies Here                    | Mitigation |
  | Ownership ambiguity    | [area boundary] (cat-2) -- ...         | [action]   |

  Inertia Assessment
  FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
  {{T2-VERDICT}}: [conclusion sentence]

.craft/roles/{area}/inertia-advocate.md
  orientation:       ...
  lens:              ...
  expertise:         ...
  scope:             "{{VERBATIM-IA-SCOPE-TEMPLATES[T2-PRESSURE]}}"
  collaborates_with: ...
```
```
