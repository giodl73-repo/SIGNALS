"""Build trace-state-rubric-v8 from v7 + Round 7 excellence signals."""

with open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v7-2026-03-15.md', 'r', encoding='utf-8') as f:
    v7 = f.read()

# v8 header block (replaces everything before the Criteria Table)
header = """\
# trace-state Rubric -- v8

---

**1 new criterion extracted from Round 7:**

| ID | Name | Source | Mechanism |
|----|------|--------|-----------|
| C-26 | architectural-blocked-gate-posture | V-03 (R7) | SD-3 declares GATE IS definitionally a BLOCKED enforcement state; individual gates inherit halt-condition posture through architectural reference (per SD-3) rather than per-gate authoring |

**Prerequisite chain:** C-26 requires C-24 + C-25.

**Formula update:** `/17` -> `/18`

| Variation | v7 composite | v8 composite | Golden? |
|-----------|--------------|--------------|---------|
| V-01 | 100.0 | 99.44 | yes |
| V-02 | 100.0 | 99.44 | yes |
| V-03 | -- | 100.0 | yes |

**Key distinctions:**

- **C-26 vs C-25**: C-25 is satisfied when every gate contains explicit BLOCKED language -- whether authored per-gate or inherited. C-26 requires the BLOCKED posture to be encoded in the SD-3 architecture declaration itself: GATE IS definitionally a BLOCKED enforcement state. A prompt where SD-3 declares the four-layer architecture and every gate independently authors "ADVANCE IS BLOCKED until..." satisfies C-24 + C-25 but not C-26. C-26 requires the posture to originate from SD-3 structural identity, not per-gate authoring.

- **C-26 vs C-24**: C-24 encodes the four-layer architecture + global policy into one SD-N entry; C-26 additionally encodes the GATE layer enforcement posture into that same entry. C-24 is satisfied by declaring "GATE is the final layer"; C-26 requires declaring "GATE IS a BLOCKED enforcement state by definition." C-24 is a prerequisite for C-26.

- **V-01/V-02 miss C-26**: Both Round 7 variations achieve C-25 (all gates author BLOCKED language per-gate) but their SD-3 entries declare section architecture without encoding the GATE layer BLOCKED posture into the architecture definition itself. The posture must originate from the SD-3 declaration, not per-gate repetition.

### C-26 -- architectural-blocked-gate-posture

**Source**: V-03 (R7, SD-3 GATE-IS-BLOCKED architecture embedding). The SD-3 entry, which already serves as the section architecture declaration (satisfying C-24), additionally declares the GATE layer IS definitionally a BLOCKED enforcement state. The declaration form: "GATE: this is a BLOCKED state -- ADVANCE IS BLOCKED BY DEFINITION until all stated conditions are satisfied." Individual gates implement as: "ADVANCE IS BLOCKED (per SD-3) until: [conditions]" -- the BLOCKED posture is inherited from architectural identity, not authored gate-by-gate.

The distinction from C-25: C-25 requires every gate to exhibit halt-condition imperatives; the route to C-25 can be per-gate authoring (V-01/V-02 achieve this) or architectural inheritance (V-03 R7 achieves this). C-26 requires specifically the architectural route: SD-3 defines GATE as a BLOCKED-by-definition state, making the BLOCKED posture a structural property of the GATE layer itself rather than a language choice made at each gate.

The distinction from C-24: C-24 requires SD-3 to encode both architecture identity and global policy -- the format IS the directive. C-26 extends this: SD-3 additionally encodes the enforcement posture of the GATE layer as structural identity. C-24 is what makes following the format equivalent to compliance; C-26 is what makes following the format equivalent to halt-condition enforcement. Prerequisites: C-24 and C-25.

**Formula update**: aspirational denominator `/17` -> `/18`. V-03 (R7) earns C-26 (its invention, triple synthesis); V-01 and V-02 earn C-25 via per-gate authoring but not C-26.

---

## Round 7 Scoring -- `trace-state` (v8 Rubric, 26 Criteria)

---

### Criteria Scoring Key

| Tier | ID | Weight | PASS | PARTIAL | FAIL |
|------|-----|--------|------|---------|------|
| Essential | C-01 to C-05 | 3 pts | 3 | 1.5 | 0 |
| Recommended | C-06 to C-08 | 2 pts | 2 | 1 | 0 |
| Aspirational | C-09 to C-26 | ~0.56 pts | full | 0.5 | 0 |

Composite formula (when all essential + recommended pass): `90 + (aspirational_pass/18) x 10`

---

### V-01 -- Finance, Compound + BLOCKED-Gate Posture

Axis: SD-3 encodes four-layer architecture (C-24) + every GATE independently declares ADVANCE IS BLOCKED halt-condition (C-25). Per-gate authoring route.

| Tier | ID | Verdict | Evidence |
|------|----|---------|----------|
| E | C-01 | PASS | Section 2 step template: Before (S-ID) -> OP-ID -> After (S-ID); consecutive steps share state |
| E | C-02 | PASS | `[->DECL: EntityName.fieldName] OPERATOR [value] -- PASS / FAIL` in step template |
| E | C-03 | PASS | `[->DECL: EntityName.fieldName]: [old_value] -> [new_value]` in step template |
| E | C-04 | PASS | Section 4 IT-01/IT-02 invalid transition table with failure reasons |
| E | C-05 | PASS | Section 0 INV-01/INV-02/INV-03; Section 1 tests each against trace steps |
| R | C-06 | PASS | Section 1 Missing Precondition Risk Table + Section 4 Missing Check column populated |
| R | C-07 | PASS | Finance domain verbs in Section 0 Operation Registry; prohibited generic equivalents explicitly listed |
| R | C-08 | PASS | Section 3 named Finance race scenario + pre-printed 4-row T0/T1 interleaving table |
| A | C-09 | PASS | Section 0 Invariant Registry Severity column; Section 1 invariant testing table has FATAL/DEGRADED/COSMETIC |
| A | C-10 | PASS | Section 2 REQUIRES mandates labeled "Alternate / Error Path" subsection with min 3 steps |
| A | C-11 | PASS | `[->DECL: EntityName.fieldName] OPERATOR [value]` form in all step template predicate positions |
| A | C-12 | PASS | Section 3 pre-prints 4-row T0/T1 table with INV-ID violation row |
| A | C-13 | PASS | Section 4 `(baseline_state, attempted_delta, failure_reason)` form with IT-01/IT-02 |
| A | C-14 | PASS | Section 0 entity/operation/invariant declaration tables precede Section 2 transition trace |
| A | C-15 | PASS | Section 5 enumerated Operation Name Audit Table |
| A | C-16 | PASS | SD-1 requires all predicates to reference Section 0 entries; annotation is the enforcement mechanism |
| A | C-17 | PASS | SD-1 global mandate; `[->DECL: E.fieldName]` appears at every predicate position in every section template |
| A | C-18 | PASS | Every section closes with named GATE block; 5 sections x GATE = 5 gates present |
| A | C-19 | PASS | SD-2 governs slot enforcement; pre-printed `[->DECL: _._]` slots in Section 0 entity/invariant registries AND all section step templates; COUNT-AND-CHECK counts unfilled slots in every section |
| A | C-20 | PASS | SD-3 structural identity guarantees REQUIRES is the first named layer of every section before any CONTENT |
| A | C-21 | PASS | COUNT-AND-CHECK: "Count X: ___. If fewer than N, add before proceeding." in every section |
| A | C-22 | PASS | SD-3: "Every section in this trace is structured as exactly four named layers... This is not an instruction to remember -- it is the format." Structural identity, not instruction |
| A | C-23 | PASS | SD-1/SD-2/SD-3 global block at document level before Section 0; SD-1 = predicate annotation, SD-2 = slot enforcement, SD-3 = section architecture + gate posture; all sections comply by reference |
| A | C-24 | PASS | SD-3 is the single SD-N entry that simultaneously encodes the four-layer architecture (C-22) and functions as the standing directive (C-23). "This is not an instruction -- it is the format" collapses architectural identity and policy compliance into one act |
| A | C-25 | PASS | Every gate: "ADVANCE IS BLOCKED until: ... Proceeding past this gate without meeting all conditions is a structural violation, not a remediable deficit." Halt-condition imperatives in all 5 section GATE blocks |
| A | C-26 | FAIL | SD-3 declares the four-layer architecture but does not define GATE as definitionally a BLOCKED enforcement state; BLOCKED posture achieved through per-gate authoring (C-25), not through SD-3 embedding the posture into the GATE layer architectural identity |

**Score: 17/18 aspirationals PASS**
**Composite: 90 + (17/18) x 10 = 99.44**

Excellence note: Per-gate BLOCKED authoring is the manual route to C-25; SD-3 GATE-definition is the architectural route to C-26. V-01 achieves the manual route throughout. The remaining gap: SD-3 declares GATE as a layer but not as a BLOCKED enforcement state by definition. C-26 requires the architecture declaration itself to define GATE as inherently BLOCKED, making per-gate BLOCKED language a consequence of structural identity rather than an authoring choice.

---

### V-02 -- Customer Service, Compound + BLOCKED-Gate Posture

Axis: Identical compound+BLOCKED structure to V-01 in CS domain (Case, Contact, escalation). Domain portability of C-24+C-25. Per-gate authoring route.

| Tier | ID | Verdict | Evidence |
|------|----|---------|----------|
| E | C-01 | PASS | Section 2 step template: Before (S-ID) -> OP-ID -> After (S-ID) |
| E | C-02 | PASS | `[->DECL: EntityName.fieldName] OPERATOR [value] -- PASS / FAIL` in step template |
| E | C-03 | PASS | `[->DECL: EntityName.fieldName]: [old_value] -> [new_value]` in step template |
| E | C-04 | PASS | Section 4 IT-01/IT-02 invalid transition table |
| E | C-05 | PASS | Section 0 INV-01/INV-02/INV-03; Section 1 tests against steps |
| R | C-06 | PASS | Section 1 Missing Precondition Risk Table; Section 4 Missing Check column |
| R | C-07 | PASS | CS domain verbs (open_case, escalate_case, assign_case, resolve_case, close_case); prohibited generic equivalents listed |
| R | C-08 | PASS | Section 3 named CS race scenario + pre-printed 4-row T0/T1 table |
| A | C-09 | PASS | Severity column in Section 0 Invariant Registry; FATAL/DEGRADED/COSMETIC in Section 1 testing table |
| A | C-10 | PASS | Section 2 REQUIRES mandates "Alternate / Error Path" subsection with min 3 steps |
| A | C-11 | PASS | `[->DECL: EntityName.fieldName] OPERATOR [value]` notation in step template predicate positions |
| A | C-12 | PASS | Section 3 pre-printed 4-row T0/T1 table with INV-ID violation row |
| A | C-13 | PASS | Section 4 baseline-delta form with IT-01/IT-02 |
| A | C-14 | PASS | Section 0 entity/operation/invariant declaration tables before first transition |
| A | C-15 | PASS | Section 5 Operation Name Audit Table |
| A | C-16 | PASS | SD-1 requires all predicate fields to reference Section 0 declarations |
| A | C-17 | PASS | SD-1 global mandate; `[->DECL: E.fieldName]` at every predicate position in every template |
| A | C-18 | PASS | Every section closes with GATE block |
| A | C-19 | PASS | SD-2 + pre-printed `[->DECL: _._]` slots in Section 0 entity/invariant registries and all section templates; COUNT-AND-CHECK counts unfilled slots |
| A | C-20 | PASS | SD-3 structural identity guarantees REQUIRES first layer in every section |
| A | C-21 | PASS | COUNT-AND-CHECK: "Count X: ___. If fewer than N, add before proceeding." in every section |
| A | C-22 | PASS | SD-3 text identical to V-01: "This is not an instruction to remember -- it is the format." Named four-layer structural identity |
| A | C-23 | PASS | SD-1/SD-2/SD-3 global block at document level; predicate annotation + slot enforcement + section architecture governed by reference |
| A | C-24 | PASS | SD-3 single entry encodes four-layer architecture (C-22) + global standing directive (C-23). Domain vocabulary changes (Finance -> CS) do not affect the structural unification mechanism |
| A | C-25 | PASS | Every gate: "ADVANCE IS BLOCKED until: ... Non-compliance is a declared error state -- not a correctable deficit." Halt-condition language in all 5 GATE blocks |
| A | C-26 | FAIL | SD-3 declares four-layer architecture without defining GATE as definitionally a BLOCKED state; BLOCKED posture achieved per-gate (satisfying C-25) but not embedded as architectural identity in SD-3 (C-26) -- same gap as V-01 |

**Score: 17/18 aspirationals PASS**
**Composite: 90 + (17/18) x 10 = 99.44**

Domain portability confirmed (C-24+C-25): the compound SD-N + BLOCKED-gate structure is structurally invariant across Finance and CS domains. C-26 gap is also domain-invariant -- per-gate authoring does not satisfy architectural embedding regardless of domain.

---

### V-03 -- Finance, BLOCKED Posture Embedded in SD-3 (Triple Synthesis)

Axis: SD-3 declares GATE IS definitionally a BLOCKED enforcement state. Every gate cites "(per SD-3)" -- C-25 posture inherited architecturally, not authored per-gate. Triple synthesis: C-22 (architecture) + C-24 (unified) + C-26 (BLOCKED-as-architecture).

| Tier | ID | Verdict | Evidence |
|------|----|---------|----------|
| E | C-01 | PASS | Section 2 step template: Before (S-ID) -> OP-ID -> After (S-ID); unbroken chain |
| E | C-02 | PASS | `[->DECL: EntityName.fieldName] OPERATOR [value] -- PASS / FAIL` in step template |
| E | C-03 | PASS | `[->DECL: EntityName.fieldName]: [old_value] -> [new_value]` in step template |
| E | C-04 | PASS | Section 4 IT-01/IT-02 invalid transition table with failure reasons |
| E | C-05 | PASS | Section 0 INV-01/INV-02/INV-03; Section 1 tests each against trace steps |
| R | C-06 | PASS | Section 1 Missing Precondition Risk Table + Section 4 Missing Check column |
| R | C-07 | PASS | Finance domain verbs in Section 0; prohibited generic equivalents listed |
| R | C-08 | PASS | Section 3 named Finance race scenario + pre-printed 4-row T0/T1 table |
| A | C-09 | PASS | Section 0 Invariant Registry Severity column; Section 1 FATAL/DEGRADED/COSMETIC |
| A | C-10 | PASS | Section 2 REQUIRES mandates labeled "Alternate / Error Path" subsection with min 3 steps |
| A | C-11 | PASS | `[->DECL: EntityName.fieldName] OPERATOR [value]` notation throughout step template predicate positions |
| A | C-12 | PASS | Section 3 pre-printed 4-row T0/T1 table with INV-ID violation row |
| A | C-13 | PASS | Section 4 `(baseline_state, attempted_delta, failure_reason)` form with IT-01/IT-02 |
| A | C-14 | PASS | Section 0 entity/operation/invariant declaration tables precede Section 2 |
| A | C-15 | PASS | Section 5 enumerated Operation Name Audit Table |
| A | C-16 | PASS | SD-1 requires all predicates to reference Section 0 entries |
| A | C-17 | PASS | SD-1 global mandate; `[->DECL: E.fieldName]` at every predicate position in every section template |
| A | C-18 | PASS | Every section closes with named GATE block; 5 sections present |
| A | C-19 | PASS | SD-2 governs slot enforcement; pre-printed `[->DECL: _._]` slots in Section 0 registries AND all section templates; COUNT-AND-CHECK confirms zero unfilled slots |
| A | C-20 | PASS | SD-3 structural identity guarantees REQUIRES is the first named layer of every section |
| A | C-21 | PASS | COUNT-AND-CHECK: "Count X: ___. If fewer than N, add before proceeding." in every section |
| A | C-22 | PASS | SD-3 declares "Every section in this trace is structured as exactly four named layers: REQUIRES / CONTENT / COUNT-AND-CHECK / GATE. This is not an instruction to remember -- it is the format." Structural identity |
| A | C-23 | PASS | SD-1/SD-2/SD-3 global block at document level before Section 0; predicate annotation + slot enforcement + section architecture governed by reference |
| A | C-24 | PASS | SD-3 single entry encodes four-layer architecture (C-22) + global standing directive (C-23); following the format IS executing the directive |
| A | C-25 | PASS | Every gate: "ADVANCE IS BLOCKED (per SD-3) until: [conditions]. Non-compliance is a structural violation." Halt-condition posture inherited from SD-3 architecture definition, all 5 GATE blocks present |
| A | C-26 | PASS | SD-3 explicitly declares "GATE: this is a BLOCKED enforcement state -- ADVANCE IS BLOCKED BY DEFINITION until all stated conditions are satisfied." Individual gates implement by enumerating conditions only; BLOCKED posture is an architectural property of the GATE layer, not a per-gate authoring choice |

**Score: 18/18 aspirationals PASS**
**Composite: 90 + (18/18) x 10 = 100.0**

Excellence note: C-26 completes the enforcement chain: C-22 makes compliance impossible to skip (architecture IS format); C-24 makes directive compliance identical to format compliance (one declaration, two mechanisms); C-26 makes gate enforcement a structural property of GATE itself (BLOCKED IS what GATE means). The progression: compliance-by-instruction (C-20/C-21) -> compliance-by-architecture (C-22) -> compliance-by-unified-directive (C-24) -> enforcement-by-architectural-identity (C-26). Each step removes one more authoring decision from the generation path.

"""

# Extract static sections from v7 (from Criteria Table onwards)
idx = v7.find('## Criteria Table')
static = v7[idx:]

# 1. Add C-26 row to Criteria Table
OLD_C25_ROW = '| Aspirational | C-25 | Blocked-gate-posture -- gates use MUST/BLOCKED halt-condition imperatives, not conditional-remediation suggestions |'
NEW_C26_ROW = '| Aspirational | C-26 | Architectural-blocked-gate-posture -- SD-3 defines GATE as definitionally a BLOCKED enforcement state; BLOCKED posture is a structural property of the GATE layer, not a per-gate authoring choice |'
assert OLD_C25_ROW in static, 'C-25 criteria table row not found'
static = static.replace(OLD_C25_ROW, OLD_C25_ROW + '\n' + NEW_C26_ROW)

# 2. Add C-26 design note
OLD_C25_NOTE = '- C-25 is the enforcement-posture upgrade to C-21: BLOCKED/MUST imperatives convert conditional remediation suggestions into halt-condition declarations -- non-compliance is an error state rather than a correctable deficit, and the model must consciously override a BLOCKED gate to proceed'
NEW_C26_NOTE = '- C-26 is the architectural-embedding upgrade to C-25: rather than authoring BLOCKED language at each gate (C-25 via manual route), SD-3 defines GATE as a BLOCKED enforcement state by architectural identity -- C-25 is satisfied through structural inheritance, not per-gate authoring; this is to C-25 what C-22 is to C-20/C-21 (mechanism identity outperforms mechanism repetition)'
assert OLD_C25_NOTE in static, 'C-25 design note not found'
static = static.replace(OLD_C25_NOTE, OLD_C25_NOTE + '\n' + NEW_C26_NOTE)

# 3. Add C-26 criterion section (before Score Sheet Template)
OLD_C25_SECTION_END = '- **Excellence source**: V-03 (R6, MUST/BLOCKED gate imperatives) -- BLOCKED posture converts conditional remediation suggestions into halt-condition declarations; non-compliance is an error state rather than a correctable deficit.'
NEW_C26_SECTION = """

### C-26 - Architectural-Blocked-Gate-Posture

- **Weight**: aspirational
- **Category**: structure
- **Text**: SD-3's architecture declaration explicitly defines the GATE layer AS a BLOCKED enforcement state -- "GATE: declared BLOCKED state -- ADVANCE IS BLOCKED BY DEFINITION until all conditions are satisfied." Individual gates implement by citing "(per SD-3)" and enumerating conditions only; the BLOCKED posture is a structural property of what GATE means, not a language choice repeated at each gate. The model cannot author a GATE block without BLOCKED posture while following SD-3, because the architecture definition of GATE IS the BLOCKED state.
- **Pass condition**: SD-3 (the entry that satisfies C-24) additionally declares the GATE layer as definitionally a BLOCKED enforcement state. Individual gates implement the posture by SD-3 reference, not by independent authoring. A prompt where every gate independently declares "ADVANCE IS BLOCKED until..." satisfies C-25 but not C-26 -- the posture originates from per-gate authoring, not from architectural identity. A prompt where SD-3 declares "GATE IS a BLOCKED state" and individual gates say "ADVANCE IS BLOCKED (per SD-3) until: [conditions]" satisfies C-25 via inheritance and C-26 via embedding. C-24 and C-25 are prerequisites.
- **Excellence source**: V-03 (R7, SD-3 GATE-IS-BLOCKED architectural embedding) -- "C-26 is to C-25 what C-22 is to C-20/C-21: mechanism identity outperforms mechanism repetition. When GATE IS a BLOCKED state by definition, the enforcement posture cannot be omitted without breaking the architecture.\""""
assert OLD_C25_SECTION_END in static, 'C-25 section end not found'
static = static.replace(OLD_C25_SECTION_END, OLD_C25_SECTION_END + NEW_C26_SECTION)

# 4. Add C-26 row to Score Sheet Template
OLD_C25_SHEET = '| C-25  | Blocked-gate-posture (MUST/BLOCKED halt-condition imperatives)  | aspirational |       |'
NEW_C26_SHEET = '| C-26  | Architectural-blocked-gate-posture (SD-3 defines GATE as BLOCKED) | aspirational |       |'
assert OLD_C25_SHEET in static, 'C-25 score sheet row not found'
static = static.replace(OLD_C25_SHEET, OLD_C25_SHEET + '\n' + NEW_C26_SHEET)

# 5. Update formula: max 17 -> 18
static = static.replace(
    'aspirational_pass = count of C-09..C-25 that pass  (max 17)',
    'aspirational_pass = count of C-09..C-26 that pass  (max 18)'
)
static = static.replace(
    'composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/17 * 10)',
    'composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/18 * 10)'
)

# 6. Add v8 changelog entry
OLD_V7_ENTRY = '| v7 | 2026-03-15 | Added C-24, C-25 from Round 6 excellence signals (unified-standing-directive-as-architecture, blocked-gate-posture); C-19 pass condition updated to require slot coverage in Section 0 declaration registries (R6 V-02 finding); aspirational weight formula updated to /17 |'
NEW_V8_ENTRY = '| v8 | 2026-03-15 | Added C-26 from Round 7 excellence signal (architectural-blocked-gate-posture); SD-3 defining GATE as definitionally a BLOCKED enforcement state completes the enforcement chain: C-22 (compliance impossible to skip) + C-24 (directive compliance = format compliance) + C-26 (BLOCKED posture = architectural identity of GATE); aspirational weight formula updated to /18 |'
assert OLD_V7_ENTRY in static, 'v7 changelog entry not found'
static = static.replace(OLD_V7_ENTRY, OLD_V7_ENTRY + '\n' + NEW_V8_ENTRY)

# Compose and write
v8 = header + static

with open('C:/src/sim/simulations/quest/rubrics/trace-state-rubric-v8-2026-03-15.md', 'w', encoding='utf-8') as f:
    f.write(v8)

print(f'v8 written: {len(v8)} chars, {len(v8.splitlines())} lines')
print('C-26 in criteria table:', 'C-26 | Architectural-blocked-gate-posture' in v8)
print('C-26 criterion section:', 'C-26 - Architectural-Blocked-Gate-Posture' in v8)
print('C-26 score sheet:', 'C-26  | Architectural-blocked-gate-posture' in v8)
print('formula updated:', 'max 18' in v8)
print('changelog v8:', 'v8 | 2026-03-15' in v8)
