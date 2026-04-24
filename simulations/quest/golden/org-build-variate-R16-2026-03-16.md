---
skill: quest-variate
skill_target: org-build
round: 16
date: 2026-03-16
rubric_version: 12
---

# Variate R16 -- org-build

5 complete prompt body variations for the `org-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v12 adds C-35 and C-36. R15 best coverage had inertia assessment co-located with role
enumeration and scope templates embedded inline; R16 targets the ordering lock and constant
extraction directly.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence: phase ordering as primary structural constraint (C-35) | V-01 |
| Output format: table-dominant phase instructions, side-by-side constraint columns (C-34, C-36) | V-02 |
| Lifecycle emphasis: maximum gate density, sub-step checkpoints (C-35, C-36) | V-03 |
| Phrasing register: terse imperative, minimum prose (C-29, C-19) | V-04 |
| Combined: inertia-first framing + unified record block as narrative backbone (C-35, C-36, C-26) | V-05 |

---

## R15 Gap Analysis (rubric v12 lens)

| New Criterion | Best R15 Coverage | Gap |
|---------------|-------------------|-----|
| C-35 Inertia assessment phase precedes role enumeration phase | R15 V-05 had ASSESS step before ENUMERATE, but both were inside Phase 2 as sub-steps of a single phase | Co-location in one phase means T2-VERDICT was not a named typed gate output consumed by an Input Contract; the verdict was computed alongside role count, not before it; C-35 requires the verdict to be a gate output of a distinct prior phase with the role-enum phase consuming it via a declared Input Contract |
| C-36 Reusable lookup tables declared as pre-phase global constants | R15 V-05 had scope templates in a "template block" inside Phase 2 instructions; category derivation was inline in Phase 2 constraints | Embedding tables inside phase instructions violates C-36 even if the content is correct; R15 met the content requirements (C-11, C-17, C-18) but the structure requirement -- defined once before Phase 0, referenced by name -- was absent; R16 extracts both tables to a named constants section that precedes all phases |

Both C-35 and C-36 were structurally anticipated in R15. The gap is architectural: R15 had the
right content in the wrong structural positions. R16 relocates the inertia verdict to its own
phase gate and the lookup tables to the pre-phase constants block.

---

## V-01 -- Phase Sequencing: Ordering Lock as Primary Structure (C-35)

**Axis**: Role sequence
**Hypothesis**: Making the inertia-verdict phase a hard gate -- with an explicit SEQUENCE-LOCK
annotation at every boundary and bidirectional FORBIDDENs naming both phases -- prevents the
model from treating the inertia assessment as a formality that runs in parallel with role
enumeration. When the phase names themselves reflect their dependency relationship
(INERTIA-VERDICT before ROLE-ENUM), and when the ROLE-ENUM Input Contract explicitly names
T1-VERDICT as a required typed input, the ordering lock is both structural and semantic.
This is the minimal addition for C-35: one phase split + two record blocks + four FORBIDDENs.

---

You are running `org-build`. Generate a complete org from scan results or a repo.
Produces: (1) `org-chart.md` with ASCII hierarchy, headcount table, and inertia assessment;
(2) `.roles/{area}/{role}.md` for every role.

**Phase sequence**: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: beginning any phase before the preceding phase's record block is emitted.

---

### PRE-PHASE CONSTANTS

These tables are defined once. Phase instructions reference them by name.
FORBIDDEN: embedding these tables inline inside phase instructions.

#### SCOPE-TEMPLATE (keyed to T1-PRESSURE)

| T1-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Attend cross-area syncs. Log coordination events that require non-standard escalation. No active structural-health program ownership required. |
| LOW | Maintain a friction log: date, area-pair, friction-type, resolution-path. MUST escalate to Area Lead when any single friction type recurs three or more times in one sprint. No structural-recommendation authority at this pressure level. |
| MODERATE | Own the flat-org health program. MUST convene a monthly Coordination Review with all Area Leads. Score friction density using the friction-density index. MUST produce a quarterly status report to the Program Lead. Escalate if friction-density score exceeds 0.4. |
| HIGH | Lead a 30-day structural assessment. MUST deliver a written recommendation with friction audit, 18-month headcount projection, cost model, and reversibility rating to the Steering Committee. FORBIDDEN: recommending structural change without evidence package. |
| CRITICAL | Chair the Org Structure Governance Board. MUST convene within 14 days. Own: decision memo, implementation plan, 90-day post-implementation review. FORBIDDEN: any structural change without recorded Steering Committee approval. |

#### CATEGORY-DERIVATION (keyed to T1-VERDICT)

| T1-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (coordination failure), cat-3 (span-of-control inflation) | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) |
| STRUCTURE-WARRANTED | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) | cat-2 (coordination failure), cat-3 (span-of-control inflation) |

---

### PHASE 0 -- INPUT

**Task Steps**

1. Read input: scan results file, repo path, or auto-detect from current directory.
2. Capture depth flag from invocation. If not provided, default to `standard`.
3. Identify primary signal source (scan results or direct repo read).

**Constraints**

- MUST capture T0-DEPTH-FLAG as `standard` or `deep` before emitting record block.
- MUST capture T0-SOURCE as `scan` or `repo` before emitting record block.
- FORBIDDEN: beginning INERTIA-VERDICT before Phase 0 record block is emitted.

```
=== RECORD: PHASE-0 ===
PHASE-ORDERING-GUARD: FORBIDDEN: INERTIA-VERDICT begins before this block is emitted.
T0-DEPTH-FLAG: [standard | deep] = <value>
T0-SOURCE: [scan | repo] = <value>
=== END RECORD: PHASE-0 ===
```

---

### PHASE 1 -- INERTIA-VERDICT

**SEQUENCE-LOCK**: This phase MUST complete and emit its record block before ROLE-ENUM begins.
T1-VERDICT and T1-PRESSURE are the gate outputs that make all downstream choices verdict-coherent.
FORBIDDEN: enumerating any role before this record block is emitted.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T0-SOURCE from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**

1. Scan org signals: team count, coordination surface area, headcount distribution, span of
   existing leads.
2. Rate structural pressure on a five-point scale: NONE, LOW, MODERATE, HIGH, CRITICAL.
   Factors: team count > 8 elevates to MODERATE; unresolved cross-area dependencies elevate
   by one level; existing hierarchy depth > 2 elevates to HIGH.
3. Deliver a single verdict: CAN-OPERATE-FLAT if pressure is NONE/LOW/MODERATE;
   STRUCTURE-WARRANTED if pressure is HIGH/CRITICAL.
   FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict.
   Both is an error. FORBIDDEN: writing neither. Neither is an error.
4. Write the verdict block in org-chart.md:
   ```
   FLAT-CASE-PRESSURE: <T1-PRESSURE>
   VERDICT: <T1-VERDICT>
   Rationale: <one paragraph>
   ```

**Constraints**

- MUST rate T1-PRESSURE from closed set: NONE, LOW, MODERATE, HIGH, CRITICAL.
- MUST assign T1-VERDICT from closed set: CAN-OPERATE-FLAT, STRUCTURE-WARRANTED.
- FORBIDDEN: assigning T1-VERDICT without a T1-PRESSURE rating.
- FORBIDDEN: beginning ROLE-ENUM before this record block is emitted.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ROLE-ENUM begins before this block is emitted.
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] = <value>
=== END RECORD: PHASE-1 ===
```

---

### PHASE 2 -- ROLE-ENUM

**SEQUENCE-LOCK**: This phase begins only after T1-VERDICT is locked in Phase 1 record block.
Role count floor, IA scope template selection, and anti-pattern categories are all
T1-VERDICT-coherent by construction because T1-VERDICT is an Input Contract requirement here.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T1-VERDICT from Phase 1 record block.
- MUST consume T1-PRESSURE from Phase 1 record block.
- FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.
- FORBIDDEN: selecting IA scope template without T1-PRESSURE value.
- FORBIDDEN: deriving anti-pattern categories without T1-VERDICT value.

**Task Steps**

1. Bind role count floor to T0-DEPTH-FLAG:
   T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles.
   T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles.
2. Map roles to area subdirectories. MUST create at least 2 area subdirs under `.roles/`.
3. MUST include an `inertia-advocate` role. Assign its `scope` field using
   SCOPE-TEMPLATE[T1-PRESSURE] verbatim. FORBIDDEN: paraphrasing or adapting the template text.
4. Derive anti-pattern categories from CATEGORY-DERIVATION[T1-VERDICT].
   Use required categories. FORBIDDEN: using FORBIDDEN categories.
5. Enumerate all roles with five required fields: orientation, lens, expertise, scope,
   collaborates_with.

**Constraints**

- MUST bind role count to T0-DEPTH-FLAG per the conditional in Task Step 1.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim to inertia-advocate scope.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories to anti-pattern watch.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-COUNT: [integer >= 20] = <value>
T2-AREA-COUNT: [integer >= 2] = <value>
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T1-PRESSURE from Phase 1 record block.
- MUST consume T1-VERDICT from Phase 1 record block.
- MUST consume T2-ROLE-COUNT, T2-AREA-COUNT, T2-IA-SCOPE-SOURCE, T2-CATEGORY-A,
  T2-CATEGORY-B from Phase 2 record block.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

1. Write `org-chart.md`:
   - ASCII box/line diagram with min 2 org levels.
   - Headcount by area table: Area, Headcount, Key Roles, Decides, Escalates.
   - Level distribution.
   - Inertia assessment block with FLAT-CASE-PRESSURE and VERDICT.
   - Anti-Pattern Watch: 2 rows minimum, each "Why It Applies Here" cell opens with
     `[element name] (cat-N) --` using T2-CATEGORY-A and T2-CATEGORY-B. Mitigation cells
     contain specific remediation actions, not format guidance.
   - Org Evolution Roadmap: 2+ rows, Row 1 is headcount threshold, Row 2 is a different
     trigger category (e.g., coordination load, team formation).
   - Operating Rhythm: table with 3+ rows (ROB, shiproom, governance). Charter per governance
     meeting: name, cadence, chair, attendees, quorum as N of M, purpose, agenda.

2. Write `.roles/{area}/{role}.md` for every enumerated role:
   - All five fields: orientation, lens, expertise, scope, collaborates_with.
   - MUST group roles by area subdirectory.
   - inertia-advocate: scope field MUST be verbatim text from SCOPE-TEMPLATE[T1-PRESSURE].

**Constraints**

- MUST produce org-chart.md with ASCII diagram containing min 2 org levels.
- MUST produce T2-ROLE-COUNT role files.
- MUST include inertia-advocate role file.
- FORBIDDEN: assigning inertia-advocate scope text other than verbatim SCOPE-TEMPLATE[T1-PRESSURE].
- FORBIDDEN: using anti-pattern categories not in CATEGORY-DERIVATION[T1-VERDICT] required set.

---

## V-02 -- Output Format: Table-Dominant Instructions with Side-by-Side Constraint Columns (C-34)

**Axis**: Output format
**Hypothesis**: Presenting phase instructions as structured tables -- task steps as numbered
table rows, constraints split into MUST and FORBIDDEN columns side by side -- makes two things
simultaneously true: (1) every constraint is auditable without reading prose, and (2) the
CATEGORY-DERIVATION table's required/FORBIDDEN side-by-side structure is mirrored throughout
the prompt, making C-34's structural requirement feel native rather than bolted on. The table
format also makes the constants section visually distinct from phase bodies, reinforcing C-36.

---

You are running `org-build`. Generate a complete org from scan results or a repo.

**Phase sequence**: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: beginning any phase before the preceding phase record block is emitted.

---

### PRE-PHASE CONSTANTS

All lookup tables used by phase instructions. FORBIDDEN: restating these tables inside any
phase instruction. Reference by table name only.

**SCOPE-TEMPLATE**

| T1-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Attend cross-area syncs. Log coordination events that require non-standard escalation. No active structural-health program ownership required. |
| LOW | Maintain a friction log: date, area-pair, friction-type, resolution-path. MUST escalate to Area Lead when any single friction type recurs three or more times in one sprint. No structural-recommendation authority at this pressure level. |
| MODERATE | Own the flat-org health program. MUST convene a monthly Coordination Review with all Area Leads. Score friction density using the friction-density index. MUST produce a quarterly status report to the Program Lead. Escalate if friction-density score exceeds 0.4. |
| HIGH | Lead a 30-day structural assessment. MUST deliver a written recommendation with friction audit, 18-month headcount projection, cost model, and reversibility rating to the Steering Committee. FORBIDDEN: recommending structural change without evidence package. |
| CRITICAL | Chair the Org Structure Governance Board. MUST convene within 14 days. Own: decision memo, implementation plan, 90-day post-implementation review. FORBIDDEN: any structural change without recorded Steering Committee approval. |

**CATEGORY-DERIVATION**

| T1-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (coordination failure), cat-3 (span-of-control inflation) | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) |
| STRUCTURE-WARRANTED | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) | cat-2 (coordination failure), cat-3 (span-of-control inflation) |

---

### PHASE 0 -- INPUT

**Task Steps**

| Step | Action | Output |
|------|--------|--------|
| 1 | Read input source (scan file or repo path) | T0-SOURCE captured |
| 2 | Read depth flag from invocation; default `standard` if absent | T0-DEPTH-FLAG captured |
| 3 | Confirm input is readable and non-empty | Input validated |

**Constraints**

| MUST | FORBIDDEN |
|------|-----------|
| MUST capture T0-DEPTH-FLAG as `standard` or `deep` | FORBIDDEN: beginning INERTIA-VERDICT before Phase 0 record block is emitted |
| MUST capture T0-SOURCE as `scan` or `repo` | FORBIDDEN: inferring depth flag from input content instead of invocation flag |

```
=== RECORD: PHASE-0 ===
PHASE-ORDERING-GUARD: FORBIDDEN: INERTIA-VERDICT begins before this block is emitted.
T0-DEPTH-FLAG: [standard | deep] = <value>
T0-SOURCE: [scan | repo] = <value>
=== END RECORD: PHASE-0 ===
```

---

### PHASE 1 -- INERTIA-VERDICT

**Input Contract**

| Variable | Source | Constraint |
|----------|--------|------------|
| T0-DEPTH-FLAG | Phase 0 record block | MUST be present and typed |
| T0-SOURCE | Phase 0 record block | MUST be present and typed |

FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**

| Step | Action | Output |
|------|--------|--------|
| 1 | Scan org signals: team count, coordination surface, span of existing leads | Signal set captured |
| 2 | Rate structural pressure: NONE / LOW / MODERATE / HIGH / CRITICAL | T1-PRESSURE draft |
| 3 | Assign single verdict: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED | T1-VERDICT draft |
| 4 | Write FLAT-CASE-PRESSURE block in org-chart.md | Block written |

**Constraints**

| MUST | FORBIDDEN |
|------|-----------|
| MUST rate T1-PRESSURE from: NONE, LOW, MODERATE, HIGH, CRITICAL | FORBIDDEN: assigning two verdicts. Both is an error. |
| MUST assign exactly one T1-VERDICT | FORBIDDEN: assigning no verdict. Neither is an error. |
| MUST assign T1-VERDICT before any role is enumerated | FORBIDDEN: beginning ROLE-ENUM before this record block is emitted |

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ROLE-ENUM begins before this block is emitted.
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] = <value>
=== END RECORD: PHASE-1 ===
```

---

### PHASE 2 -- ROLE-ENUM

**Input Contract**

| Variable | Source | Constraint |
|----------|--------|------------|
| T0-DEPTH-FLAG | Phase 0 record block | MUST bind to role count floor in Task Step 1 |
| T1-VERDICT | Phase 1 record block | MUST govern category selection per CATEGORY-DERIVATION |
| T1-PRESSURE | Phase 1 record block | MUST govern IA scope selection per SCOPE-TEMPLATE |

FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.

**Task Steps**

| Step | Action | Output |
|------|--------|--------|
| 1 | Bind count floor: T0-DEPTH-FLAG=standard -> 20-30 roles; T0-DEPTH-FLAG=deep -> 50+ roles | Count floor locked |
| 2 | Map roles to area subdirectories (min 2 areas) | Area map complete |
| 3 | Assign inertia-advocate scope = SCOPE-TEMPLATE[T1-PRESSURE] verbatim | IA scope assigned |
| 4 | Derive anti-pattern categories = CATEGORY-DERIVATION[T1-VERDICT] required set | Categories locked |
| 5 | Enumerate all role files with 5 fields each | Role list complete |

**Constraints**

| MUST | FORBIDDEN |
|------|-----------|
| MUST bind role count floor to T0-DEPTH-FLAG per Step 1 conditional | FORBIDDEN: deriving categories without T1-VERDICT value |
| MUST assign inertia-advocate scope from SCOPE-TEMPLATE[T1-PRESSURE] verbatim | FORBIDDEN: paraphrasing or adapting SCOPE-TEMPLATE text |
| MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories | FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT] |
| MUST create min 2 area subdirs under .roles/ | FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted |

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-COUNT: [integer >= 20] = <value>
T2-AREA-COUNT: [integer >= 2] = <value>
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**Input Contract**

| Variable | Source | Constraint |
|----------|--------|------------|
| T0-DEPTH-FLAG | Phase 0 record block | MUST govern final role count verification |
| T1-PRESSURE | Phase 1 record block | MUST appear in FLAT-CASE-PRESSURE block |
| T1-VERDICT | Phase 1 record block | MUST appear in VERDICT line |
| T2-ROLE-COUNT | Phase 2 record block | MUST match actual file count written |
| T2-IA-SCOPE-SOURCE | Phase 2 record block | MUST match T1-PRESSURE |
| T2-CATEGORY-A, T2-CATEGORY-B | Phase 2 record block | MUST appear in Anti-Pattern Watch |

FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

| Step | Action | Produces |
|------|--------|----------|
| 1 | Write ASCII org diagram (min 2 levels) | org-chart.md section 1 |
| 2 | Write headcount table: Area, Headcount, Key Roles, Decides, Escalates | org-chart.md section 2 |
| 3 | Write FLAT-CASE-PRESSURE + VERDICT + Rationale using T1-PRESSURE and T1-VERDICT | org-chart.md section 3 |
| 4 | Write Anti-Pattern Watch: 2+ rows, cat-N citations, remediation Mitigations | org-chart.md section 4 |
| 5 | Write Org Evolution Roadmap: row 1 = headcount threshold, row 2 = different trigger type | org-chart.md section 5 |
| 6 | Write Operating Rhythm: 3+ rows; governance charter with quorum as N of M | org-chart.md section 6 |
| 7 | Write T2-ROLE-COUNT role files; inertia-advocate scope = verbatim SCOPE-TEMPLATE[T1-PRESSURE] | .roles/ |

**Constraints**

| MUST | FORBIDDEN |
|------|-----------|
| MUST produce ASCII diagram with min 2 org levels | FORBIDDEN: anti-pattern Mitigation cells containing format guidance instead of remediation actions |
| MUST include Decides and Escalates in headcount table | FORBIDDEN: inertia-advocate scope text differing from verbatim SCOPE-TEMPLATE[T1-PRESSURE] |
| MUST include quorum as N of M in governance charter | FORBIDDEN: using anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set |

---

## V-03 -- Lifecycle Emphasis: Maximum Gate Density with Sub-Step Checkpoints (C-35, C-36)

**Axis**: Lifecycle emphasis
**Hypothesis**: Breaking the inertia assessment into named sub-steps (SCAN, SCORE, VERDICT),
each with its own mini-checkpoint before the full phase record block, forces the model to
externalize its reasoning at each decision point. When T1-PRESSURE is emitted as a
mini-checkpoint before T1-VERDICT is derived, the two values are independently auditable.
This also prevents the model from collapsing the assessment into a single step where verdict
and pressure are assigned simultaneously without visible derivation. Maximum gate density
makes the "inertia assessment phase precedes role enumeration phase" property structurally
enforced at the sub-step level, not just at the phase boundary.

---

You are running `org-build`. Generate a complete org from scan results or a repo.

**Phase sequence**: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: beginning any phase before the preceding phase record block is emitted.

---

### PRE-PHASE CONSTANTS

Defined once. All phase instructions consume by reference.
FORBIDDEN: embedding these tables inside any phase instruction block.

**SCOPE-TEMPLATE** (keyed to T1-PRESSURE)

| T1-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Attend cross-area syncs. Log coordination events that require non-standard escalation. No active structural-health program ownership required. |
| LOW | Maintain a friction log: date, area-pair, friction-type, resolution-path. MUST escalate to Area Lead when any single friction type recurs three or more times in one sprint. No structural-recommendation authority at this pressure level. |
| MODERATE | Own the flat-org health program. MUST convene a monthly Coordination Review with all Area Leads. Score friction density using the friction-density index. MUST produce a quarterly status report to the Program Lead. Escalate if friction-density score exceeds 0.4. |
| HIGH | Lead a 30-day structural assessment. MUST deliver a written recommendation with friction audit, 18-month headcount projection, cost model, and reversibility rating to the Steering Committee. FORBIDDEN: recommending structural change without evidence package. |
| CRITICAL | Chair the Org Structure Governance Board. MUST convene within 14 days. Own: decision memo, implementation plan, 90-day post-implementation review. FORBIDDEN: any structural change without recorded Steering Committee approval. |

**CATEGORY-DERIVATION** (keyed to T1-VERDICT)

| T1-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (coordination failure), cat-3 (span-of-control inflation) | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) |
| STRUCTURE-WARRANTED | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) | cat-2 (coordination failure), cat-3 (span-of-control inflation) |

---

### PHASE 0 -- INPUT

**Task Steps**

1. Read input source. Capture T0-SOURCE.
2. Read depth flag from invocation. Capture T0-DEPTH-FLAG. Default: `standard`.

**Constraints**

- MUST emit T0-DEPTH-FLAG and T0-SOURCE before proceeding.
- FORBIDDEN: beginning INERTIA-VERDICT before Phase 0 record block is emitted.

```
=== RECORD: PHASE-0 ===
PHASE-ORDERING-GUARD: FORBIDDEN: INERTIA-VERDICT begins before this block is emitted.
T0-DEPTH-FLAG: [standard | deep] = <value>
T0-SOURCE: [scan | repo] = <value>
=== END RECORD: PHASE-0 ===
```

---

### PHASE 1 -- INERTIA-VERDICT

**Input Contract**

- MUST have Phase 0 record block emitted.
- MUST consume T0-SOURCE and T0-DEPTH-FLAG from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

This phase has three named sub-steps. MUST emit a sub-step checkpoint after each sub-step
before proceeding to the next.

#### Sub-Step 1-A: SCAN

Enumerate org signals relevant to structural pressure:
- Team count and growth trajectory
- Cross-area dependency density
- Existing hierarchy depth
- Span of current leads

Emit checkpoint:
```
SCAN-CHECKPOINT:
  team-count: <n>
  cross-area-dependencies: [low | medium | high]
  hierarchy-depth: <n>
  lead-span: <n>
```
FORBIDDEN: proceeding to Sub-Step 1-B before SCAN-CHECKPOINT is emitted.

#### Sub-Step 1-B: SCORE

Derive T1-PRESSURE from scan signals:
- Team count > 8: elevate to MODERATE minimum.
- Cross-area dependencies = high: elevate by one level.
- Hierarchy depth > 2: elevate to HIGH minimum.

Emit checkpoint:
```
SCORE-CHECKPOINT:
  T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
  Derivation: <one sentence per elevation factor applied>
```
FORBIDDEN: proceeding to Sub-Step 1-C before SCORE-CHECKPOINT is emitted.

#### Sub-Step 1-C: VERDICT

Assign T1-VERDICT from T1-PRESSURE:
- NONE / LOW / MODERATE -> CAN-OPERATE-FLAT
- HIGH / CRITICAL -> STRUCTURE-WARRANTED

FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED. Only one verdict.
Both is an error.
FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED. Neither is an error.

Write FLAT-CASE-PRESSURE block in org-chart.md.

**Constraints**

- MUST complete all three sub-steps before emitting Phase 1 record block.
- MUST derive T1-VERDICT from T1-PRESSURE per the rule in Sub-Step 1-C.
- FORBIDDEN: beginning ROLE-ENUM before Phase 1 record block is emitted.
- FORBIDDEN: enumerating roles in sub-steps of this phase.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ROLE-ENUM begins before this block is emitted.
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] = <value>
=== END RECORD: PHASE-1 ===
```

---

### PHASE 2 -- ROLE-ENUM

**Input Contract**

- MUST have Phase 1 record block emitted.
- MUST consume T1-VERDICT from Phase 1 record block for category derivation.
- MUST consume T1-PRESSURE from Phase 1 record block for IA scope selection.
- MUST consume T0-DEPTH-FLAG from Phase 0 record block for count floor binding.
- FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.

This phase has four named sub-steps.

#### Sub-Step 2-A: COUNT-FLOOR

Bind role count floor to T0-DEPTH-FLAG:
- T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles.
- T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles.

Emit checkpoint:
```
COUNT-FLOOR-CHECKPOINT:
  T0-DEPTH-FLAG: <value>
  role-count-floor: <value>
  role-count-ceiling: <value or "none for deep">
```

#### Sub-Step 2-B: AREA-MAP

Map roles to area subdirectories. MUST define at least 2 area subdirs.
Emit checkpoint:
```
AREA-MAP-CHECKPOINT:
  areas: [list of area names]
  area-count: <n>
```

#### Sub-Step 2-C: IA-SCOPE-SELECT

Look up SCOPE-TEMPLATE[T1-PRESSURE]. Record the verbatim text that will be assigned to
inertia-advocate scope field.
FORBIDDEN: modifying, paraphrasing, or adapting the template text.

Emit checkpoint:
```
IA-SCOPE-CHECKPOINT:
  T1-PRESSURE: <value>
  scope-text: "<verbatim SCOPE-TEMPLATE text>"
```

#### Sub-Step 2-D: ROLE-LIST

Enumerate all roles with five fields: orientation, lens, expertise, scope, collaborates_with.
Look up CATEGORY-DERIVATION[T1-VERDICT] for required anti-pattern categories.
FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].

**Constraints**

- MUST complete all four sub-steps before emitting Phase 2 record block.
- FORBIDDEN: beginning ARTIFACT-GEN before Phase 2 record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-COUNT: [integer >= 20] = <value>
T2-AREA-COUNT: [integer >= 2] = <value>
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**Input Contract**

- MUST have Phase 2 record block emitted.
- MUST consume all six Phase 2 gate variables.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

1. Write `org-chart.md`:
   - ASCII hierarchy diagram (min 2 org levels).
   - Headcount table: Area, Headcount, Key Roles, Decides, Escalates.
   - FLAT-CASE-PRESSURE and VERDICT block.
   - Anti-Pattern Watch: T2-CATEGORY-A and T2-CATEGORY-B rows; "Why It Applies Here" opens
     with `[element name] (cat-N) --`; Mitigation cell contains remediation action.
   - Org Evolution Roadmap: Row 1 = headcount threshold trigger; Row 2 = different trigger
     category (not headcount).
   - Operating Rhythm: 3+ rows; governance charter rows include quorum as N of M.

2. Write role files: `.roles/{area}/{role}.md`.
   - All five fields present in every file.
   - inertia-advocate scope = verbatim SCOPE-TEMPLATE[T1-PRESSURE].
   - MUST group in area subdirs.

**Constraints**

- MUST verify T2-ROLE-COUNT matches actual file count.
- FORBIDDEN: inertia-advocate scope deviating from verbatim SCOPE-TEMPLATE[T1-PRESSURE].

---

## V-04 -- Phrasing Register: Terse Imperative (C-29, C-19)

**Axis**: Phrasing register
**Hypothesis**: A prompt that uses minimum words with maximum MUST/FORBIDDEN density -- no
explanatory prose, no transitional sentences -- tests whether the rubric criteria can be
satisfied without narrative. When every sentence is either a task step or a constraint, the
structural segmentation requirement (C-30) is naturally satisfied because there is no prose to
blur the boundary. Terse register also makes FORBIDDEN keyword violations visible immediately:
any "do not" or "avoid" in a constraint context stands out against the otherwise purely
MUST/FORBIDDEN register.

---

You are running `org-build`. Input: scan results or repo path.
Output: `org-chart.md` + `.roles/{area}/{role}.md`.
Phase sequence: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: any phase beginning before the preceding phase record block is emitted.

---

### PRE-PHASE CONSTANTS

FORBIDDEN: embedding these tables inside phase instructions.

**SCOPE-TEMPLATE**

| T1-PRESSURE | Verbatim Scope |
|-------------|----------------|
| NONE | Attend cross-area syncs. Log coordination events that require non-standard escalation. No active structural-health program ownership required. |
| LOW | Maintain a friction log: date, area-pair, friction-type, resolution-path. MUST escalate to Area Lead when any single friction type recurs three or more times in one sprint. No structural-recommendation authority at this pressure level. |
| MODERATE | Own the flat-org health program. MUST convene a monthly Coordination Review with all Area Leads. Score friction density using the friction-density index. MUST produce a quarterly status report to the Program Lead. Escalate if friction-density score exceeds 0.4. |
| HIGH | Lead a 30-day structural assessment. MUST deliver a written recommendation with friction audit, 18-month headcount projection, cost model, and reversibility rating to the Steering Committee. FORBIDDEN: recommending structural change without evidence package. |
| CRITICAL | Chair the Org Structure Governance Board. MUST convene within 14 days. Own: decision memo, implementation plan, 90-day post-implementation review. FORBIDDEN: any structural change without recorded Steering Committee approval. |

**CATEGORY-DERIVATION**

| T1-VERDICT | Required | FORBIDDEN |
|------------|----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

### PHASE 0 -- INPUT

**Task Steps**
1. Read input. Capture T0-SOURCE.
2. Read depth flag. Capture T0-DEPTH-FLAG. Default: `standard`.

**Constraints**
- MUST capture T0-DEPTH-FLAG as `standard` or `deep`.
- MUST capture T0-SOURCE as `scan` or `repo`.
- FORBIDDEN: beginning INERTIA-VERDICT before this record block is emitted.

```
=== RECORD: PHASE-0 ===
PHASE-ORDERING-GUARD: FORBIDDEN: INERTIA-VERDICT begins before this block is emitted.
T0-DEPTH-FLAG: [standard | deep] = <value>
T0-SOURCE: [scan | repo] = <value>
=== END RECORD: PHASE-0 ===
```

---

### PHASE 1 -- INERTIA-VERDICT

**Input Contract**
- MUST consume T0-DEPTH-FLAG and T0-SOURCE from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**
1. Score structural pressure from org signals.
2. Assign T1-PRESSURE: NONE / LOW / MODERATE / HIGH / CRITICAL.
3. Assign T1-VERDICT: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
4. Write FLAT-CASE-PRESSURE block.

**Constraints**
- MUST assign T1-PRESSURE from closed set.
- MUST assign exactly one T1-VERDICT. Both is an error. Neither is an error.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
- FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED.
- FORBIDDEN: enumerating any role in this phase.
- FORBIDDEN: beginning ROLE-ENUM before this record block is emitted.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ROLE-ENUM begins before this block is emitted.
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] = <value>
=== END RECORD: PHASE-1 ===
```

---

### PHASE 2 -- ROLE-ENUM

**Input Contract**
- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T1-VERDICT from Phase 1 record block.
- MUST consume T1-PRESSURE from Phase 1 record block.
- FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.
- FORBIDDEN: selecting anti-pattern categories without T1-VERDICT value.
- FORBIDDEN: selecting IA scope template without T1-PRESSURE value.

**Task Steps**
1. Bind count: T0-DEPTH-FLAG=standard -> 20-30 roles; T0-DEPTH-FLAG=deep -> 50+ roles.
2. Map areas. Min 2 area subdirs.
3. Assign inertia-advocate scope = SCOPE-TEMPLATE[T1-PRESSURE] verbatim.
4. Derive categories = CATEGORY-DERIVATION[T1-VERDICT] required set.
5. Enumerate all roles. Five fields each.

**Constraints**
- MUST bind role count to T0-DEPTH-FLAG per Step 1.
- MUST include inertia-advocate role.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim to inertia-advocate scope.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories.
- FORBIDDEN: paraphrasing SCOPE-TEMPLATE text.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-COUNT: [integer >= 20] = <value>
T2-AREA-COUNT: [integer >= 2] = <value>
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**Input Contract**
- MUST consume T1-PRESSURE, T1-VERDICT from Phase 1 record block.
- MUST consume T2-ROLE-COUNT, T2-AREA-COUNT, T2-IA-SCOPE-SOURCE, T2-CATEGORY-A,
  T2-CATEGORY-B from Phase 2 record block.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**
1. Write org-chart.md: ASCII diagram (min 2 levels); headcount table (Area, Headcount, Key
   Roles, Decides, Escalates); FLAT-CASE-PRESSURE + VERDICT; Anti-Pattern Watch (T2-CATEGORY-A
   and T2-CATEGORY-B, `[element] (cat-N) --` citations, remediation Mitigations); Org
   Evolution Roadmap (row 1 = headcount threshold, row 2 = different trigger type); Operating
   Rhythm (3+ rows, governance charter with quorum as N of M).
2. Write role files: `.roles/{area}/{role}.md`. Five fields each. inertia-advocate
   scope = verbatim SCOPE-TEMPLATE[T1-PRESSURE].

**Constraints**
- MUST write T2-ROLE-COUNT role files.
- MUST verify ASCII diagram has min 2 org levels.
- FORBIDDEN: inertia-advocate scope deviating from SCOPE-TEMPLATE[T1-PRESSURE] verbatim text.
- FORBIDDEN: anti-pattern Mitigation cells containing format guidance instead of actions.
- FORBIDDEN: anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set.

---

## V-05 -- Combined: Inertia-First Framing + Unified Record Block as Narrative Backbone (C-35, C-36, C-26)

**Axis**: Inertia framing + record block integration
**Hypothesis**: When the entire prompt is framed around the inertia verdict as the primary
question ("before enumerating any role, answer: can this org operate flat?"), the phase
ordering constraint (C-35) becomes a natural consequence of the framing rather than a
structural rule the model must remember. The record block serves as the narrative backbone:
each phase's record block is the answer to a question the prompt explicitly posed. The
constants section is introduced as "the tools you will need to answer that question" -- making
C-36's referential structure feel purposeful. Combined axis tests whether narrative coherence
and structural compliance reinforce each other.

---

You are running `org-build`.

Before enumerating a single role, answer the central question: **can this org operate flat?**
That verdict -- locked as a named gate output -- makes every downstream choice verdict-coherent
by construction: role count floor, inertia-advocate scope, anti-pattern categories, and
evolution triggers all follow from the verdict, not from arbitrary defaults.

**Phase sequence**: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: beginning ROLE-ENUM before the INERTIA-VERDICT record block is emitted.

---

### PRE-PHASE CONSTANTS

The tools you will need to answer the central question and act on the verdict.
These tables are defined once. Phase instructions reference them by name.
FORBIDDEN: embedding these definitions inside any phase instruction.

**SCOPE-TEMPLATE** -- The inertia-advocate's scope is determined by structural pressure.
Look up by T1-PRESSURE. Apply verbatim.

| T1-PRESSURE | Verbatim Scope Text |
|-------------|---------------------|
| NONE | Attend cross-area syncs. Log coordination events that require non-standard escalation. No active structural-health program ownership required. |
| LOW | Maintain a friction log: date, area-pair, friction-type, resolution-path. MUST escalate to Area Lead when any single friction type recurs three or more times in one sprint. No structural-recommendation authority at this pressure level. |
| MODERATE | Own the flat-org health program. MUST convene a monthly Coordination Review with all Area Leads. Score friction density using the friction-density index. MUST produce a quarterly status report to the Program Lead. Escalate if friction-density score exceeds 0.4. |
| HIGH | Lead a 30-day structural assessment. MUST deliver a written recommendation with friction audit, 18-month headcount projection, cost model, and reversibility rating to the Steering Committee. FORBIDDEN: recommending structural change without evidence package. |
| CRITICAL | Chair the Org Structure Governance Board. MUST convene within 14 days. Own: decision memo, implementation plan, 90-day post-implementation review. FORBIDDEN: any structural change without recorded Steering Committee approval. |

**CATEGORY-DERIVATION** -- Anti-pattern categories follow the verdict.
A flat org is at risk from flat-org failures. A structured org is at risk from hierarchy failures.

| T1-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (coordination failure), cat-3 (span-of-control inflation) | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) |
| STRUCTURE-WARRANTED | cat-1 (over-hierarchy), cat-4 (reporting-line ambiguity) | cat-2 (coordination failure), cat-3 (span-of-control inflation) |

---

### PHASE 0 -- INPUT

Read the inputs that frame the central question: what org are we building and at what depth?

**Task Steps**

1. Read input source (scan results or repo). Capture T0-SOURCE.
2. Capture depth flag from invocation. Default: `standard`. Capture T0-DEPTH-FLAG.

**Constraints**

- MUST capture T0-DEPTH-FLAG as `standard` or `deep` before proceeding.
- MUST capture T0-SOURCE as `scan` or `repo` before proceeding.
- FORBIDDEN: beginning INERTIA-VERDICT before this record block is emitted.

```
=== RECORD: PHASE-0 ===
PHASE-ORDERING-GUARD: FORBIDDEN: INERTIA-VERDICT begins before this block is emitted.
T0-DEPTH-FLAG: [standard | deep] = <value>
T0-SOURCE: [scan | repo] = <value>
=== END RECORD: PHASE-0 ===
```

---

### PHASE 1 -- INERTIA-VERDICT

**This phase answers the central question.**

Answer it before touching roles. The verdict locks two typed outputs -- T1-PRESSURE and
T1-VERDICT -- that every subsequent choice in this session is downstream of.

**Input Contract**

- MUST consume T0-DEPTH-FLAG and T0-SOURCE from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**

1. Scan org signals: team count, coordination surface area, span of existing leads, hierarchy
   depth. High team count (>8), high dependency density, or existing hierarchy elevate pressure.
2. Assign T1-PRESSURE: NONE, LOW, MODERATE, HIGH, or CRITICAL.
3. Derive T1-VERDICT from T1-PRESSURE:
   - NONE / LOW / MODERATE -> CAN-OPERATE-FLAT.
   - HIGH / CRITICAL -> STRUCTURE-WARRANTED.
   The verdict is singular. Write one. FORBIDDEN: writing both. Both is an error.
   FORBIDDEN: writing neither. Neither is an error.
4. Write the FLAT-CASE-PRESSURE block in org-chart.md:
   ```
   FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
   VERDICT: {{T1-VERDICT}}
   Rationale: <one paragraph>
   ```

**Constraints**

- MUST assign T1-PRESSURE from closed set before deriving T1-VERDICT.
- MUST assign exactly one T1-VERDICT.
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
- FORBIDDEN: writing neither CAN-OPERATE-FLAT nor STRUCTURE-WARRANTED.
- FORBIDDEN: enumerating any role before this record block is emitted.
- FORBIDDEN: beginning ROLE-ENUM before this record block is emitted.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ROLE-ENUM begins before this block is emitted.
T1-PRESSURE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T1-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED] = <value>
=== END RECORD: PHASE-1 ===
```

With T1-VERDICT locked, proceed to role enumeration. All choices from here are
verdict-coherent because T1-VERDICT is a required Input Contract item for ROLE-ENUM.

---

### PHASE 2 -- ROLE-ENUM

**This phase builds verdict-coherently.**

T1-VERDICT governs what anti-pattern categories are valid. T1-PRESSURE governs the
inertia-advocate's scope. T0-DEPTH-FLAG governs how many roles to enumerate. All three
are consumed from prior record blocks via this phase's Input Contract.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block -- governs count floor in Task Step 1.
- MUST consume T1-VERDICT from Phase 1 record block -- governs CATEGORY-DERIVATION lookup.
- MUST consume T1-PRESSURE from Phase 1 record block -- governs SCOPE-TEMPLATE lookup.
- FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.
- FORBIDDEN: selecting IA scope template without consuming T1-PRESSURE.
- FORBIDDEN: deriving anti-pattern categories without consuming T1-VERDICT.

**Task Steps**

1. Bind count floor to T0-DEPTH-FLAG:
   T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles.
   T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles.
2. Map roles to area subdirectories. MUST create min 2 area subdirs under `.roles/`.
3. MUST include inertia-advocate role. Assign scope = SCOPE-TEMPLATE[T1-PRESSURE] verbatim.
   This role is the structural memory of the verdict.
   FORBIDDEN: paraphrasing or adapting SCOPE-TEMPLATE text.
4. Look up CATEGORY-DERIVATION[T1-VERDICT]. Assign T2-CATEGORY-A and T2-CATEGORY-B from
   the required set. FORBIDDEN: using FORBIDDEN categories.
5. Enumerate all roles. Every role file: orientation, lens, expertise, scope, collaborates_with.

**Constraints**

- MUST bind count floor to T0-DEPTH-FLAG value inside this phase's Task Step 1.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim. Paraphrase fails.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-COUNT: [integer >= 20] = <value>
T2-AREA-COUNT: [integer >= 2] = <value>
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**This phase materializes the verdict-coherent org.**

All gate outputs from prior record blocks are consumed here. The artifacts reflect the
inertia verdict throughout: the FLAT-CASE-PRESSURE block, the anti-pattern categories,
the inertia-advocate role, and the evolution roadmap triggers all trace to T1-VERDICT.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T1-PRESSURE and T1-VERDICT from Phase 1 record block.
- MUST consume T2-ROLE-COUNT, T2-AREA-COUNT, T2-IA-SCOPE-SOURCE, T2-CATEGORY-A,
  T2-CATEGORY-B from Phase 2 record block.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

1. Write `org-chart.md` using the following skeleton with slots keyed to gate variables:

```markdown
# Org Chart: {{ORG-NAME}}

## ASCII Structure

{{ASCII-DIAGRAM-MIN-2-LEVELS}}

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{HEADCOUNT-TABLE-ROWS}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}
Rationale: {{RATIONALE}}

## Anti-Pattern Watch

| Pattern | Category | Why It Applies Here | Mitigation |
|---------|----------|---------------------|------------|
| {{PATTERN-NAME}} | {{T2-CATEGORY-A}} | [{{ELEMENT-NAME}}] ({{T2-CATEGORY-A}}) -- {{WHY}} | {{REMEDIATION-ACTION}} |
| {{PATTERN-NAME}} | {{T2-CATEGORY-B}} | [{{ELEMENT-NAME}}] ({{T2-CATEGORY-B}}) -- {{WHY}} | {{REMEDIATION-ACTION}} |

## Org Evolution Roadmap

| Trigger | Type | Threshold | Action |
|---------|------|-----------|--------|
| {{TRIGGER-1}} | headcount | {{HEADCOUNT-THRESHOLD}} | {{ACTION}} |
| {{TRIGGER-2}} | {{DIFFERENT-TYPE}} | {{THRESHOLD}} | {{ACTION}} |

## Operating Rhythm

| Meeting | Cadence | Chair | Attendees | Purpose |
|---------|---------|-------|-----------|---------|
| ROB | {{CADENCE}} | {{CHAIR}} | {{ATTENDEES}} | {{PURPOSE}} |
| Shiproom | {{CADENCE}} | {{CHAIR}} | {{ATTENDEES}} | {{PURPOSE}} |
| {{GOVERNANCE-MEETING}} | {{CADENCE}} | {{CHAIR}} | {{ATTENDEES}} | {{PURPOSE}} |

### Charter: {{GOVERNANCE-MEETING}}
- Name: {{NAME}}
- Cadence: {{CADENCE}}
- Chair: {{CHAIR}}
- Attendees: {{ATTENDEES}}
- Quorum: {{N}} of {{M}}
- Purpose: {{PURPOSE}}
- Agenda: {{AGENDA}}
```

2. Write `.roles/{area}/{role}.md` for all T2-ROLE-COUNT roles.
   Each file: orientation, lens, expertise, scope, collaborates_with.
   inertia-advocate scope field: verbatim text from SCOPE-TEMPLATE[T1-PRESSURE].
   MUST group files under area subdirectories (T2-AREA-COUNT areas).

**Constraints**

- MUST produce ASCII diagram with min 2 org levels.
- MUST include Decides and Escalates columns in headcount table.
- MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format.
- MUST write Mitigation cells as specific remediation actions -- FORBIDDEN: format guidance.
- MUST write Org Evolution Roadmap row 1 as headcount threshold; row 2 as different trigger type.
- MUST write governance charter with quorum as N of M fraction.
- MUST write T2-ROLE-COUNT role files grouped in T2-AREA-COUNT area subdirs.
- FORBIDDEN: inertia-advocate scope deviating from SCOPE-TEMPLATE[T1-PRESSURE] verbatim text.
- FORBIDDEN: anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set.
