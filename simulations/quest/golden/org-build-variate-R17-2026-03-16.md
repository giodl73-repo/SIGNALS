---
skill: quest-variate
skill_target: org-build
round: 17
date: 2026-03-16
rubric_version: 12
---

# Variate R17 -- org-build

5 complete prompt body variations for the `org-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v12 is unchanged from R16. The universal gap is C-31: `T2-ROLE-COUNT: [integer >= 20]`
and `T2-AREA-COUNT: [integer >= 2]` are range annotations, not closed enumerations. All R16
variations scored 98.9 (25/28) or 99.6 (27/28); R17 targets C-31 exclusively while preserving
all R16 wins.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Count-field encoding: binary compliance tokens (C-31) | V-01 |
| Count-field encoding: depth-outcome class (C-31) | V-02 |
| Count-field encoding: removed from record block; satisfied in Constraints (C-31) | V-03 |
| Combined: binary compliance tokens + terse imperative register (C-31, C-29) | V-04 |
| Full integration: depth-outcome class + complete artifact skeleton (C-31, C-22) | V-05 |

---

## R16 Gap Analysis (rubric v12 lens)

| Criterion | R16 Coverage | Gap |
|-----------|-------------|-----|
| C-31 Record block fields carry inline type annotations as valid-value sets | All variations used `T2-ROLE-COUNT: [integer >= 20]` and `T2-AREA-COUNT: [integer >= 2]`. These are range annotations, not closed enumerations. C-31 requires complete valid-value sets; open-ended range annotations fail. | Integer count fields cannot have finite closed enumerations. R17 eliminates the raw-integer gate variable in favor of typed compliance tokens or depth-outcome classes that carry closed-set valid-value annotations. Three approaches explored: (A) replace with binary compliance tokens [FLOOR-MET | FLOOR-MISS], (B) replace with depth-keyed outcome class [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS], (C) move count compliance out of record block into Constraints pre-emission check. |

R16 V-05 was the high-water mark at 99.6, passing 27/28 aspirational criteria. It passed C-10
(MUST in Constraints for citation format) and C-22 (complete artifact skeleton) which V-01--V-04
did not. R17 builds on V-05's structural wins while fixing C-31.

---

## V-01 -- Count-Field Encoding: Binary Compliance Tokens (C-31)

**Axis**: Count-field encoding
**Hypothesis**: Replacing raw integer gate fields with binary compliance tokens gives Phase 2's
record block two new closed enumerations: `T2-COUNT-COMPLIANCE: [FLOOR-MET | FLOOR-MISS]` and
`T2-AREA-COMPLIANCE: [ADEQUATE | INADEQUATE]`. The depth-flag-conditional count floor (C-27)
moves to Phase 2 Task Steps and Constraints as a verification step whose outcome is recorded as
a compliance token rather than a raw integer. Phase 3 Input Contract consumes
T2-COUNT-COMPLIANCE and carries an explicit FORBIDDEN on proceeding if FLOOR-MISS is recorded.
C-31 passes because all five Phase 2 record fields now carry complete valid-value sets in
bracket notation.

---

You are running `org-build`. Generate a complete org from scan results or a repo.
Produces: (1) `org-chart.md` with ASCII hierarchy, headcount table, and inertia assessment;
(2) `.craft/roles/{area}/{role}.md` for every role.

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
T1-VERDICT and T1-PRESSURE are the gate outputs that make all downstream choices
verdict-coherent. FORBIDDEN: enumerating any role before this record block is emitted.

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
- FORBIDDEN: writing both verdicts. Both is an error.
- FORBIDDEN: writing neither verdict. Neither is an error.
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
- FORBIDDEN: selecting IA scope template without T1-PRESSURE value from Phase 1 record block.
- FORBIDDEN: deriving anti-pattern categories without T1-VERDICT value from Phase 1 record block.

**Task Steps**

1. Bind role count floor to T0-DEPTH-FLAG:
   T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles.
   T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles.
   Verify enumerated count meets floor. Record T2-COUNT-COMPLIANCE as FLOOR-MET if floor is
   met, FLOOR-MISS if below floor.
2. Map roles to area subdirectories. MUST create at least 2 area subdirs under `.craft/roles/`.
   Verify area subdir count >= 2. Record T2-AREA-COMPLIANCE as ADEQUATE if >= 2, INADEQUATE
   if fewer.
3. MUST include an `inertia-advocate` role. Assign its `scope` field using
   SCOPE-TEMPLATE[T1-PRESSURE] verbatim.
   FORBIDDEN: paraphrasing or adapting the template text.
4. Derive anti-pattern categories from CATEGORY-DERIVATION[T1-VERDICT].
   Use required categories. FORBIDDEN: using FORBIDDEN categories.
5. Enumerate all roles with five required fields: orientation, lens, expertise, scope,
   collaborates_with.

**Constraints**

- MUST bind role count floor to T0-DEPTH-FLAG per Task Step 1 conditional.
- MUST record T2-COUNT-COMPLIANCE as FLOOR-MET if count meets floor, FLOOR-MISS otherwise.
- MUST record T2-AREA-COMPLIANCE as ADEQUATE if area subdirs >= 2, INADEQUATE otherwise.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim to inertia-advocate scope.
- MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format in every
  "Why It Applies Here" cell.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories to anti-pattern watch.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-COUNT-COMPLIANCE: [FLOOR-MET | FLOOR-MISS] = <value>
T2-AREA-COMPLIANCE: [ADEQUATE | INADEQUATE] = <value>
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
- MUST consume T2-COUNT-COMPLIANCE from Phase 2 record block.
  FORBIDDEN: proceeding if T2-COUNT-COMPLIANCE is FLOOR-MISS.
- MUST consume T2-AREA-COMPLIANCE from Phase 2 record block.
  FORBIDDEN: proceeding if T2-AREA-COMPLIANCE is INADEQUATE.
- MUST consume T2-IA-SCOPE-SOURCE, T2-CATEGORY-A, T2-CATEGORY-B from Phase 2 record block.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

1. Write `org-chart.md`:
   - ASCII box/line diagram with min 2 org levels.
   - Headcount by area table: Area, Headcount, Key Roles, Decides, Escalates.
   - Level distribution.
   - Inertia assessment block with FLAT-CASE-PRESSURE: <T1-PRESSURE> and VERDICT: <T1-VERDICT>.
   - Anti-Pattern Watch: 2 rows minimum, each "Why It Applies Here" cell opens with
     `[element name] (cat-N) --` using T2-CATEGORY-A and T2-CATEGORY-B. Mitigation cells
     contain specific remediation actions, not format guidance.
   - Org Evolution Roadmap: 2+ rows, Row 1 headcount threshold, Row 2 different trigger category.
   - Operating Rhythm: 3+ rows (ROB, shiproom, governance). Charter per governance meeting:
     name, cadence, chair, attendees, quorum as N of M, purpose, agenda.

2. Write `.craft/roles/{area}/{role}.md` for every enumerated role:
   - All five fields: orientation, lens, expertise, scope, collaborates_with.
   - MUST group roles by area subdirectory.
   - inertia-advocate: scope MUST be verbatim text from SCOPE-TEMPLATE[T1-PRESSURE].

**Constraints**

- MUST produce org-chart.md with ASCII diagram containing min 2 org levels.
- MUST include inertia-advocate role file.
- FORBIDDEN: assigning inertia-advocate scope text other than verbatim SCOPE-TEMPLATE[T1-PRESSURE].
- FORBIDDEN: anti-pattern Mitigation cells containing format guidance instead of remediation actions.
- FORBIDDEN: using anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set.

---

## V-02 -- Count-Field Encoding: Depth-Outcome Class (C-31)

**Axis**: Count-field encoding
**Hypothesis**: A three-way depth-outcome class `T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET |
DEEP-FLOOR-MET | FLOOR-MISS]` is a richer closed enumeration than a binary compliance token.
It encodes both the depth mode that produced the role list and whether the floor was met,
eliminating the need for Phase 3 to re-consult T0-DEPTH-FLAG for count verification. A
companion `T2-AREA-OUTCOME: [COVERAGE-ADEQUATE | COVERAGE-INADEQUATE]` closes the area field.
Both gate variables carry complete valid-value sets in bracket notation -- C-31 passes. This
variation uses the table-dominant format from R16 V-02 to reinforce the side-by-side
constraint structure.

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
| T0-DEPTH-FLAG | Phase 0 record block | MUST bind to role count floor and T2-ROLE-OUTCOME derivation |
| T1-VERDICT | Phase 1 record block | MUST govern category selection per CATEGORY-DERIVATION |
| T1-PRESSURE | Phase 1 record block | MUST govern IA scope selection per SCOPE-TEMPLATE |

FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.

**Task Steps**

| Step | Action | Output |
|------|--------|--------|
| 1 | Bind count floor: T0-DEPTH-FLAG=standard -> 20-30 roles; T0-DEPTH-FLAG=deep -> 50+ roles. Verify floor met. Record T2-ROLE-OUTCOME: STANDARD-FLOOR-MET if standard+floor met; DEEP-FLOOR-MET if deep+floor met; FLOOR-MISS if below floor for either mode. | T2-ROLE-OUTCOME locked |
| 2 | Map roles to area subdirectories (min 2 areas). Record T2-AREA-OUTCOME: COVERAGE-ADEQUATE if >= 2 areas; COVERAGE-INADEQUATE otherwise. | T2-AREA-OUTCOME locked |
| 3 | Assign inertia-advocate scope = SCOPE-TEMPLATE[T1-PRESSURE] verbatim | IA scope assigned |
| 4 | Derive anti-pattern categories = CATEGORY-DERIVATION[T1-VERDICT] required set | Categories locked |
| 5 | Enumerate all role files with 5 fields each | Role list complete |

**Constraints**

| MUST | FORBIDDEN |
|------|-----------|
| MUST bind role count floor to T0-DEPTH-FLAG per Step 1 conditional | FORBIDDEN: recording T2-ROLE-OUTCOME as STANDARD-FLOOR-MET when T0-DEPTH-FLAG is deep |
| MUST assign inertia-advocate scope from SCOPE-TEMPLATE[T1-PRESSURE] verbatim | FORBIDDEN: paraphrasing or adapting SCOPE-TEMPLATE text |
| MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories | FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT] |
| MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format | FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted |

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS] = <value>
T2-AREA-OUTCOME: [COVERAGE-ADEQUATE | COVERAGE-INADEQUATE] = <value>
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
| T0-DEPTH-FLAG | Phase 0 record block | MUST appear in org-chart.md generation metadata |
| T1-PRESSURE | Phase 1 record block | MUST appear in FLAT-CASE-PRESSURE block |
| T1-VERDICT | Phase 1 record block | MUST appear in VERDICT line |
| T2-ROLE-OUTCOME | Phase 2 record block | FORBIDDEN: proceeding if value is FLOOR-MISS |
| T2-AREA-OUTCOME | Phase 2 record block | FORBIDDEN: proceeding if value is COVERAGE-INADEQUATE |
| T2-IA-SCOPE-SOURCE | Phase 2 record block | MUST match T1-PRESSURE |
| T2-CATEGORY-A, T2-CATEGORY-B | Phase 2 record block | MUST appear in Anti-Pattern Watch citations |

FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

| Step | Action | Produces |
|------|--------|----------|
| 1 | Write ASCII org diagram (min 2 levels) | org-chart.md section 1 |
| 2 | Write headcount table: Area, Headcount, Key Roles, Decides, Escalates | org-chart.md section 2 |
| 3 | Write FLAT-CASE-PRESSURE + VERDICT + Rationale using T1-PRESSURE and T1-VERDICT | org-chart.md section 3 |
| 4 | Write Anti-Pattern Watch: 2+ rows, `[element name] (cat-N) --` citations, remediation Mitigations | org-chart.md section 4 |
| 5 | Write Org Evolution Roadmap: row 1 = headcount threshold, row 2 = different trigger type | org-chart.md section 5 |
| 6 | Write Operating Rhythm: 3+ rows; governance charter with quorum as N of M | org-chart.md section 6 |
| 7 | Write role files per area subdir; inertia-advocate scope verbatim from SCOPE-TEMPLATE[T1-PRESSURE] | .craft/roles/ |

**Constraints**

| MUST | FORBIDDEN |
|------|-----------|
| MUST produce ASCII diagram with min 2 org levels | FORBIDDEN: anti-pattern Mitigation cells containing format guidance instead of remediation actions |
| MUST include Decides and Escalates in headcount table | FORBIDDEN: inertia-advocate scope text differing from verbatim SCOPE-TEMPLATE[T1-PRESSURE] |
| MUST include quorum as N of M in governance charter | FORBIDDEN: using anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set |

---

## V-03 -- Count-Field Encoding: Removed from Record Block (C-31)

**Axis**: Count-field encoding
**Hypothesis**: Integer count fields violate C-31 because no finite closed enumeration exists
for them. The clean solution is to remove them from the record block entirely. Count compliance
is verified in Phase 2 Constraints before the record block is emitted -- the record block never
emits them because Phase 3 does not need a count gate variable; it gets the count floor from
T0-DEPTH-FLAG (Phase 0) which is already in its Input Contract. Phase 2's record block retains
three fields (T2-IA-SCOPE-SOURCE, T2-CATEGORY-A, T2-CATEGORY-B), all of which carry closed
enumerations. C-31 passes because every named field in every record block carries a complete
valid-value set. This variation uses the sub-step checkpoint structure from R16 V-03 to make
count verification and area verification independently visible before the record block is
emitted.

---

You are running `org-build`. Generate a complete org from scan results or a repo.
Produces: (1) `org-chart.md` with ASCII hierarchy, headcount table, and inertia assessment;
(2) `.craft/roles/{area}/{role}.md` for every role.

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

**SEQUENCE-LOCK**: FORBIDDEN: enumerating any role before this record block is emitted.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T0-SOURCE from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**

Sub-step SCAN: Scan org signals -- team count, coordination surface, span of leads.
FORBIDDEN: beginning sub-step SCORE before completing SCAN.

Sub-step SCORE: Rate T1-PRESSURE: NONE, LOW, MODERATE, HIGH, or CRITICAL.
Factors: team count > 8 elevates to MODERATE; unresolved cross-area dependencies elevate by
one; existing hierarchy depth > 2 elevates to HIGH.
FORBIDDEN: beginning sub-step VERDICT before completing SCORE.

Sub-step VERDICT: Assign T1-VERDICT from scored pressure.
CAN-OPERATE-FLAT if T1-PRESSURE is NONE, LOW, or MODERATE.
STRUCTURE-WARRANTED if T1-PRESSURE is HIGH or CRITICAL.
FORBIDDEN: writing both verdicts. Both is an error.
FORBIDDEN: writing neither verdict. Neither is an error.

Write verdict block in org-chart.md:
```
FLAT-CASE-PRESSURE: <T1-PRESSURE>
VERDICT: <T1-VERDICT>
Rationale: <one paragraph>
```

**Constraints**

- MUST rate T1-PRESSURE from closed set: NONE, LOW, MODERATE, HIGH, CRITICAL.
- MUST assign T1-VERDICT from closed set: CAN-OPERATE-FLAT, STRUCTURE-WARRANTED.
- FORBIDDEN: assigning T1-VERDICT without a T1-PRESSURE rating.
- FORBIDDEN: writing both verdicts. Both is an error.
- FORBIDDEN: writing neither verdict. Neither is an error.
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

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T1-VERDICT from Phase 1 record block.
- MUST consume T1-PRESSURE from Phase 1 record block.
- FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.
- FORBIDDEN: selecting IA scope template without T1-PRESSURE value from Phase 1 record block.
- FORBIDDEN: deriving anti-pattern categories without T1-VERDICT value from Phase 1 record block.

**Task Steps**

Sub-step COUNT: Bind role count floor to T0-DEPTH-FLAG.
T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles.
T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles.
MUST verify count meets floor before proceeding to sub-step AREA.
FORBIDDEN: proceeding to sub-step AREA if count is below floor.

Sub-step AREA: Map roles to area subdirectories under `.craft/roles/`.
MUST create at least 2 area subdirs.
MUST verify area subdir count >= 2 before proceeding to sub-step IA.
FORBIDDEN: proceeding to sub-step IA if area subdir count is below 2.

Sub-step IA: Assign inertia-advocate scope = SCOPE-TEMPLATE[T1-PRESSURE] verbatim.
FORBIDDEN: paraphrasing or adapting the template text.

Sub-step DERIVE: Derive anti-pattern categories from CATEGORY-DERIVATION[T1-VERDICT].
Use required categories only. FORBIDDEN: using FORBIDDEN categories.

Sub-step ENUMERATE: Write all roles with five fields: orientation, lens, expertise, scope,
collaborates_with.

**Constraints**

- MUST verify role count floor per T0-DEPTH-FLAG before emitting record block.
- MUST verify area subdir count >= 2 before emitting record block.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim to inertia-advocate scope.
- MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format in every
  "Why It Applies Here" cell.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
  MUST verify actual role file count meets floor: T0-DEPTH-FLAG=standard -> 20-30 files;
  T0-DEPTH-FLAG=deep -> 50+ files.
  FORBIDDEN: writing fewer files than the T0-DEPTH-FLAG floor.
- MUST consume T1-PRESSURE from Phase 1 record block.
- MUST consume T1-VERDICT from Phase 1 record block.
- MUST consume T2-IA-SCOPE-SOURCE, T2-CATEGORY-A, T2-CATEGORY-B from Phase 2 record block.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

1. Write `org-chart.md`:
   - ASCII box/line diagram with min 2 org levels.
   - Headcount by area table: Area, Headcount, Key Roles, Decides, Escalates.
   - Level distribution.
   - Inertia assessment block with FLAT-CASE-PRESSURE and VERDICT.
   - Anti-Pattern Watch: 2 rows minimum.
   - Org Evolution Roadmap: 2+ rows, Row 1 headcount threshold, Row 2 different trigger category.
   - Operating Rhythm: 3+ rows (ROB, shiproom, governance). Charter per governance meeting:
     name, cadence, chair, attendees, quorum as N of M, purpose, agenda.

2. Write `.craft/roles/{area}/{role}.md` for every enumerated role:
   - All five fields: orientation, lens, expertise, scope, collaborates_with.
   - MUST group roles by area subdirectory.
   - inertia-advocate: scope MUST be verbatim text from SCOPE-TEMPLATE[T1-PRESSURE].

**Constraints**

- MUST produce org-chart.md with ASCII diagram containing min 2 org levels.
- MUST include inertia-advocate role file.
- FORBIDDEN: assigning inertia-advocate scope text other than verbatim SCOPE-TEMPLATE[T1-PRESSURE].
- FORBIDDEN: anti-pattern Mitigation cells containing format guidance instead of remediation actions.
- FORBIDDEN: using anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set.

---

## V-04 -- Combined: Binary Compliance Tokens + Terse Imperative Register (C-31, C-29)

**Axis**: Count-field encoding + Phrasing register
**Hypothesis**: The compliance-token fix from V-01 achieves C-31. Pairing it with the terse
imperative register from R16 V-04 minimizes prose surface area, maximizing the signal-to-noise
ratio of every MUST and FORBIDDEN. The terse format also makes it easier to audit C-31
compliance: fewer words per field means the annotation is the most prominent element in the
record block. The variation uses zero advisory language; every constraint is MUST or FORBIDDEN
with no preamble.

---

You are running `org-build`. Produce: (1) `org-chart.md` with ASCII hierarchy, headcount
table, and inertia assessment; (2) `.craft/roles/{area}/{role}.md` for every role.

Phase sequence: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: beginning any phase before the preceding phase record block is emitted.

---

### PRE-PHASE CONSTANTS

FORBIDDEN: restating or duplicating these tables inside any phase instruction.

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
| CAN-OPERATE-FLAT | cat-2, cat-3 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

---

### PHASE 0 -- INPUT

**Task Steps**
1. Read input source.
2. Capture T0-DEPTH-FLAG from invocation. Default: `standard`.

**Constraints**
- MUST capture T0-DEPTH-FLAG.
- MUST capture T0-SOURCE.
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
- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T0-SOURCE from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**
1. Scan team count, coordination surface, span of leads.
2. Rate T1-PRESSURE: NONE, LOW, MODERATE, HIGH, CRITICAL.
3. Assign T1-VERDICT: CAN-OPERATE-FLAT (NONE/LOW/MODERATE) or STRUCTURE-WARRANTED (HIGH/CRITICAL).
4. Write FLAT-CASE-PRESSURE block in org-chart.md.

**Constraints**
- MUST rate T1-PRESSURE from: NONE, LOW, MODERATE, HIGH, CRITICAL.
- MUST assign exactly one T1-VERDICT.
- FORBIDDEN: writing both verdicts. Both is an error.
- FORBIDDEN: writing neither verdict. Neither is an error.
- FORBIDDEN: assigning T1-VERDICT without T1-PRESSURE.
- FORBIDDEN: enumerating any role before this record block is emitted.
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
- FORBIDDEN: selecting IA scope without T1-PRESSURE from Phase 1 record block.
- FORBIDDEN: selecting categories without T1-VERDICT from Phase 1 record block.

**Task Steps**
1. Bind count floor to T0-DEPTH-FLAG:
   T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles. Record FLOOR-MET or FLOOR-MISS.
   T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles. Record FLOOR-MET or FLOOR-MISS.
2. Map to area subdirs. MUST create >= 2. Record ADEQUATE or INADEQUATE.
3. Include inertia-advocate. Assign scope = SCOPE-TEMPLATE[T1-PRESSURE] verbatim.
4. Derive categories from CATEGORY-DERIVATION[T1-VERDICT]. Required only.
5. Enumerate all roles. Five fields each.

**Constraints**
- MUST bind count floor to T0-DEPTH-FLAG per Step 1.
- MUST record T2-COUNT-COMPLIANCE: FLOOR-MET if floor met, FLOOR-MISS otherwise.
- MUST record T2-AREA-COMPLIANCE: ADEQUATE if >= 2 areas, INADEQUATE otherwise.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim to inertia-advocate scope.
- MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories only.
- FORBIDDEN: paraphrasing SCOPE-TEMPLATE text.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-COUNT-COMPLIANCE: [FLOOR-MET | FLOOR-MISS] = <value>
T2-AREA-COMPLIANCE: [ADEQUATE | INADEQUATE] = <value>
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
- MUST consume T2-COUNT-COMPLIANCE from Phase 2 record block.
  FORBIDDEN: proceeding if T2-COUNT-COMPLIANCE is FLOOR-MISS.
- MUST consume T2-AREA-COMPLIANCE from Phase 2 record block.
  FORBIDDEN: proceeding if T2-AREA-COMPLIANCE is INADEQUATE.
- MUST consume T2-IA-SCOPE-SOURCE, T2-CATEGORY-A, T2-CATEGORY-B from Phase 2 record block.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**
1. Write `org-chart.md`: ASCII diagram (min 2 levels), headcount table (Area/Headcount/Key
   Roles/Decides/Escalates), level distribution, inertia assessment block, Anti-Pattern Watch
   (2+ rows), Org Evolution Roadmap (2+ rows), Operating Rhythm (3+ rows with governance
   charter including quorum as N of M).
2. Write `.craft/roles/{area}/{role}.md` for every role: five fields, grouped by area subdir.
   inertia-advocate scope = verbatim SCOPE-TEMPLATE[T1-PRESSURE].

**Constraints**
- MUST produce ASCII diagram with min 2 org levels.
- MUST include inertia-advocate role file.
- MUST include Decides and Escalates columns in headcount table.
- MUST include quorum as N of M in governance charter.
- FORBIDDEN: inertia-advocate scope differing from verbatim SCOPE-TEMPLATE[T1-PRESSURE].
- FORBIDDEN: Anti-Pattern Watch Mitigation cells containing format guidance.
- FORBIDDEN: anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set.

---

## V-05 -- Full Integration: Depth-Outcome Class + Complete Artifact Skeleton (C-31, C-22)

**Axis**: Count-field encoding (depth-outcome class) + inertia-first framing + complete artifact skeleton
**Hypothesis**: The depth-outcome class encoding from V-02 fixes C-31 with the richest typed
gate variable: `T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]` captures
both the depth mode and the compliance verdict in a single closed enumeration. Paired with the
inertia-first framing from R16 V-05 and the complete artifact skeleton (which satisfied C-22 in
R16), this variation targets a perfect 28/28 aspirational score. The skeleton extends R16 V-05's
`{{T1-PRESSURE}}` / `{{T1-VERDICT}}` / `{{T2-CATEGORY-A}}` / `{{T2-CATEGORY-B}}` slots to
include `{{T2-ROLE-OUTCOME}}` and `{{T2-AREA-OUTCOME}}` -- all five Phase 2 gate variables now
have corresponding artifact slots, satisfying C-31 and C-22 simultaneously.

---

You are running `org-build`. Before enumerating a single role, answer the central question:
**can this org operate flat?** Everything downstream -- how many roles, what scope the
inertia-advocate carries, which anti-patterns to watch -- is coherent only if the inertia
verdict is locked first.

Produces: (1) `org-chart.md` with ASCII hierarchy, headcount table, and inertia assessment;
(2) `.craft/roles/{area}/{role}.md` for every role.

**Phase sequence**: INPUT -> INERTIA-VERDICT -> ROLE-ENUM -> ARTIFACT-GEN.
FORBIDDEN: beginning any phase before the preceding phase record block is emitted.

---

### PRE-PHASE CONSTANTS

The tools you will need to answer the central question -- defined once, here, before any phase.
FORBIDDEN: embedding these table definitions inside phase instructions.
FORBIDDEN: restating or duplicating any row from these tables inside phase instructions.
Phase instructions reference these tables by name only.

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

### ORG-CHART.MD SKELETON

This is the shape of the primary artifact. Every `{{SLOT}}` corresponds to a named gate
variable from a phase record block. A typed variable declared at a gate with no slot here is
a dangling output. A slot here with no corresponding gate variable is an undeclared dependency.
Both are errors.

```
# Org Chart

## Hierarchy

[ASCII box/line diagram]
{{ORG-DIAGRAM}}

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{HEADCOUNT-TABLE-ROWS}}

## Level Distribution

{{LEVEL-DISTRIBUTION}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}
Rationale: {{INERTIA-RATIONALE}}

## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|-------------|---------------------|------------|
| [element name] ({{T2-CATEGORY-A}}) | {{T2-CATEGORY-A-WHY}} | {{T2-CATEGORY-A-MITIGATION}} |
| [element name] ({{T2-CATEGORY-B}}) | {{T2-CATEGORY-B-WHY}} | {{T2-CATEGORY-B-MITIGATION}} |

## Org Evolution Roadmap

| Trigger | Threshold | Recommended Action |
|---------|-----------|--------------------|
| Headcount | {{HEADCOUNT-TRIGGER}} | {{HEADCOUNT-ACTION}} |
| {{ALT-TRIGGER-TYPE}} | {{ALT-TRIGGER-THRESHOLD}} | {{ALT-TRIGGER-ACTION}} |

## Operating Rhythm

| Meeting | Cadence | Chair | Purpose |
|---------|---------|-------|---------|
| ROB | {{ROB-CADENCE}} | {{ROB-CHAIR}} | {{ROB-PURPOSE}} |
| Shiproom | {{SHIPROOM-CADENCE}} | {{SHIPROOM-CHAIR}} | {{SHIPROOM-PURPOSE}} |
| {{GOVERNANCE-NAME}} | {{GOVERNANCE-CADENCE}} | {{GOVERNANCE-CHAIR}} | {{GOVERNANCE-PURPOSE}} |

### {{GOVERNANCE-NAME}} Charter
- Attendees: {{GOVERNANCE-ATTENDEES}}
- Quorum: {{GOVERNANCE-QUORUM-N}} of {{GOVERNANCE-QUORUM-M}}
- Agenda: {{GOVERNANCE-AGENDA}}

## Generation Metadata

Depth mode: {{T0-DEPTH-FLAG}}
Role count outcome: {{T2-ROLE-OUTCOME}}
Area coverage: {{T2-AREA-OUTCOME}}
IA scope source: {{T2-IA-SCOPE-SOURCE}}
```

---

### PHASE 0 -- INPUT

**Task Steps**

1. Read input: scan results file, repo path, or auto-detect from current directory.
2. Capture T0-DEPTH-FLAG from invocation. Default `standard` if absent.
3. Identify primary signal source.

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

**SEQUENCE-LOCK**: The structural verdict is the gate that makes all downstream choices
coherent. T1-VERDICT and T1-PRESSURE MUST be locked here before ROLE-ENUM begins. Any choice
made about role count, IA scope, or anti-pattern categories before T1-VERDICT is recorded is
verdict-incoherent by construction.
FORBIDDEN: enumerating any role before this record block is emitted.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T0-SOURCE from Phase 0 record block.
- FORBIDDEN: executing INERTIA-VERDICT before Phase 0 record block is emitted.

**Task Steps**

1. Scan org signals: team count, coordination surface area, headcount distribution, span of
   existing leads.
2. Rate structural pressure: NONE, LOW, MODERATE, HIGH, or CRITICAL.
   Factors: team count > 8 elevates to MODERATE; unresolved cross-area dependencies elevate by
   one level; existing hierarchy depth > 2 elevates to HIGH.
3. Assign a single verdict from the rated pressure:
   CAN-OPERATE-FLAT if T1-PRESSURE is NONE, LOW, or MODERATE.
   STRUCTURE-WARRANTED if T1-PRESSURE is HIGH or CRITICAL.
   FORBIDDEN: writing both verdicts. Both is an error.
   FORBIDDEN: writing neither verdict. Neither is an error.
4. Write the verdict block in org-chart.md (slot `{{T1-PRESSURE}}` and `{{T1-VERDICT}}`).

**Constraints**

- MUST rate T1-PRESSURE from closed set: NONE, LOW, MODERATE, HIGH, CRITICAL.
- MUST assign T1-VERDICT from closed set: CAN-OPERATE-FLAT, STRUCTURE-WARRANTED.
- FORBIDDEN: writing both verdicts. Both is an error.
- FORBIDDEN: writing neither verdict. Neither is an error.
- FORBIDDEN: assigning T1-VERDICT without T1-PRESSURE.
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

**SEQUENCE-LOCK**: T1-VERDICT is now locked. Every choice in this phase is verdict-coherent
by construction because T1-VERDICT is a required Input Contract variable.

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
- MUST consume T1-VERDICT from Phase 1 record block.
- MUST consume T1-PRESSURE from Phase 1 record block.
- FORBIDDEN: executing ROLE-ENUM before Phase 1 record block is emitted.
- FORBIDDEN: selecting IA scope template without T1-PRESSURE value from Phase 1 record block.
- FORBIDDEN: deriving anti-pattern categories without T1-VERDICT value from Phase 1 record block.

**Task Steps**

1. Bind role count floor to T0-DEPTH-FLAG and verify:
   T0-DEPTH-FLAG = standard -> MUST enumerate 20-30 roles.
   T0-DEPTH-FLAG = deep -> MUST enumerate 50+ roles.
   Record T2-ROLE-OUTCOME:
   - STANDARD-FLOOR-MET if T0-DEPTH-FLAG=standard and count is 20-30.
   - DEEP-FLOOR-MET if T0-DEPTH-FLAG=deep and count is 50+.
   - FLOOR-MISS if count is below floor for either mode.
2. Map roles to area subdirectories. MUST create at least 2 area subdirs under `.craft/roles/`.
   Record T2-AREA-OUTCOME: COVERAGE-ADEQUATE if >= 2 area subdirs; COVERAGE-INADEQUATE if fewer.
3. MUST include an `inertia-advocate` role. Assign its `scope` field using
   SCOPE-TEMPLATE[T1-PRESSURE] verbatim.
   FORBIDDEN: paraphrasing or adapting the template text.
4. Derive anti-pattern categories from CATEGORY-DERIVATION[T1-VERDICT].
   MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format in every
   "Why It Applies Here" cell.
   FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
5. Enumerate all roles with five required fields: orientation, lens, expertise, scope,
   collaborates_with.

**Constraints**

- MUST bind role count floor to T0-DEPTH-FLAG per Task Step 1 conditional.
- MUST record T2-ROLE-OUTCOME: STANDARD-FLOOR-MET, DEEP-FLOOR-MET, or FLOOR-MISS.
  FORBIDDEN: recording STANDARD-FLOOR-MET when T0-DEPTH-FLAG is deep.
  FORBIDDEN: recording DEEP-FLOOR-MET when T0-DEPTH-FLAG is standard.
- MUST record T2-AREA-OUTCOME: COVERAGE-ADEQUATE or COVERAGE-INADEQUATE.
- MUST apply SCOPE-TEMPLATE[T1-PRESSURE] verbatim to inertia-advocate scope.
- MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format.
- MUST apply CATEGORY-DERIVATION[T1-VERDICT] required categories.
- FORBIDDEN: using FORBIDDEN categories per CATEGORY-DERIVATION[T1-VERDICT].
- FORBIDDEN: beginning ARTIFACT-GEN before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: ARTIFACT-GEN begins before this block is emitted.
T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS] = <value>
T2-AREA-OUTCOME: [COVERAGE-ADEQUATE | COVERAGE-INADEQUATE] = <value>
T2-IA-SCOPE-SOURCE: [NONE | LOW | MODERATE | HIGH | CRITICAL] = <value>
T2-CATEGORY-A: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
T2-CATEGORY-B: [cat-1 | cat-2 | cat-3 | cat-4] = <value>
=== END RECORD: PHASE-2 ===
```

---

### PHASE 3 -- ARTIFACT-GEN

**Input Contract**

- MUST consume T0-DEPTH-FLAG from Phase 0 record block.
  MUST use T0-DEPTH-FLAG to populate `{{T0-DEPTH-FLAG}}` slot in Generation Metadata.
- MUST consume T1-PRESSURE from Phase 1 record block.
  MUST populate `{{T1-PRESSURE}}` slot in org-chart.md skeleton.
- MUST consume T1-VERDICT from Phase 1 record block.
  MUST populate `{{T1-VERDICT}}` slot in org-chart.md skeleton.
- MUST consume T2-ROLE-OUTCOME from Phase 2 record block.
  FORBIDDEN: proceeding if T2-ROLE-OUTCOME is FLOOR-MISS.
  MUST populate `{{T2-ROLE-OUTCOME}}` slot in Generation Metadata.
- MUST consume T2-AREA-OUTCOME from Phase 2 record block.
  FORBIDDEN: proceeding if T2-AREA-OUTCOME is COVERAGE-INADEQUATE.
  MUST populate `{{T2-AREA-OUTCOME}}` slot in Generation Metadata.
- MUST consume T2-IA-SCOPE-SOURCE from Phase 2 record block.
  MUST populate `{{T2-IA-SCOPE-SOURCE}}` slot in Generation Metadata.
- MUST consume T2-CATEGORY-A, T2-CATEGORY-B from Phase 2 record block.
  MUST populate `{{T2-CATEGORY-A}}` and `{{T2-CATEGORY-B}}` slots in Anti-Pattern Watch.
- FORBIDDEN: executing ARTIFACT-GEN before Phase 2 record block is emitted.

**Task Steps**

1. Fill `org-chart.md` by populating every `{{SLOT}}` in the ORG-CHART.MD SKELETON:
   - ASCII box/line diagram (min 2 org levels) -> `{{ORG-DIAGRAM}}`
   - Headcount table rows (Area, Headcount, Key Roles, Decides, Escalates) -> `{{HEADCOUNT-TABLE-ROWS}}`
   - Level distribution -> `{{LEVEL-DISTRIBUTION}}`
   - Inertia assessment block -> `{{T1-PRESSURE}}` and `{{T1-VERDICT}}` from Phase 1 record
   - Anti-Pattern Watch rows: `[element name] (cat-N) --` citations using T2-CATEGORY-A and
     T2-CATEGORY-B. Mitigation cells contain specific remediation actions.
   - Org Evolution Roadmap: Row 1 headcount threshold, Row 2 different trigger category type.
   - Operating Rhythm: 3+ rows. Governance charter with quorum as N of M.
   - Generation Metadata section populated with all remaining gate variable slots.

2. Write `.craft/roles/{area}/{role}.md` for every enumerated role:
   - All five fields: orientation, lens, expertise, scope, collaborates_with.
   - MUST group roles by area subdirectory.
   - inertia-advocate: scope MUST be verbatim text from SCOPE-TEMPLATE[T1-PRESSURE].

**Constraints**

- MUST produce org-chart.md with ASCII diagram containing min 2 org levels.
- MUST include inertia-advocate role file.
- MUST include Decides and Escalates in headcount table.
- MUST include quorum as N of M in governance charter.
- MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format.
- MUST populate all `{{SLOT}}` entries in ORG-CHART.MD SKELETON before artifact is complete.
- FORBIDDEN: assigning inertia-advocate scope text other than verbatim SCOPE-TEMPLATE[T1-PRESSURE].
- FORBIDDEN: anti-pattern Mitigation cells containing format guidance instead of remediation actions.
- FORBIDDEN: using anti-pattern categories outside CATEGORY-DERIVATION[T1-VERDICT] required set.
- FORBIDDEN: any `{{SLOT}}` remaining unfilled in the final org-chart.md artifact.

---

```json
{"top_score_predicted": 100.0, "c31_fix": "closed-enum compliance tokens / depth-outcome class", "new_patterns": ["depth-outcome class encodes mode + compliance in single token", "generation metadata section as home for count/area gate variable slots in artifact skeleton"]}
```
