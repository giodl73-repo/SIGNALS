---
skill: quest-variate
skill_target: org-build
round: 19
date: 2026-03-16
rubric_version: 13
---

# Variate R19 -- org-build

5 complete prompt body variations for the `org-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).
Rubric v13 adds C-37 (intra-phase sub-step ordering guards) and C-38 (composite typed
tokens encoding mode × compliance). R18 addressed C-35 (inertia before roles) and C-36
(pre-phase global constants); R19 isolates the two new criteria and combines.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Inertia framing: IA role as primary design signal, FLAT-CASE-PRESSURE banner in org-chart header | V-01 |
| Lifecycle emphasis: triple-direction guards, extended RECORD blocks, output checklist | V-02 |
| Role sequence: Phase 0 labeling for inertia assessment as explicit prerequisite gate | V-03 |
| Lifecycle + Phrasing register: maximum boundary formalism with zero advisory language | V-04 |
| Inertia framing + Output format: composite tokens + table-dominant output + pre-print skeleton | V-05 |

---

## R18 Gap Analysis (rubric v13 lens)

| New Criterion | Best R18 Coverage | Gap |
|---------------|-------------------|-----|
| C-37 intra-phase sub-step ordering guards | R18 V-02: FORBIDDEN at each phase boundary (C-23/C-25); phase boundaries correctly double-guarded | R18 had no FORBIDDEN directives at sub-step boundaries within Phase 2. The COUNT→AREA and AREA→FILE transitions inside Phase 2 carried narrative ordering ("enumerate, then group, then write") but no FORBIDDEN naming the blocked sub-step and the prerequisite. C-37 requires the same discipline at sub-step granularity: "FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT." Generic "complete all prior steps" does not satisfy the naming requirement. |
| C-38 composite typed tokens | R18 V-01: T1-DEPTH-FLAG field + separate count-compliance assertion in output | R18 encoded depth mode (standard/deep) and count compliance (floor met/miss) as two orthogonal fields, requiring a cross-reference to determine mode-specific floor status. C-38 requires a single composite token that collapses both into one closed-set value: `T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET \| DEEP-FLOOR-MET \| FLOOR-MISS]`. A reader seeing one token knows both what was attempted and whether it succeeded. R18's two-field design fails C-38 even when each individual field is correctly typed. |

The gap for C-37 is granularity: phase-level FORBIDDENs exist but sub-step-level FORBIDDENs
do not. The gap for C-38 is token design: mode and compliance were correct in content but
split across two fields when they must be collapsed into one composite token.

---

## V-01 -- Axis: Inertia Framing

**Axis**: Inertia framing
**Hypothesis**: Foregrounding the inertia-advocate role as the primary design signal — not
one role among many — improves T2-VERDICT coherence (C-11), verbatim template adherence
(C-17), and verdict-guard completeness (C-15). When every downstream section is framed as
a consequence of the structural verdict, the model is less likely to produce a generic IA
scope or omit the verdict block.

```
You are executing the **org-build** skill. This skill has one structural question:
**should this org stay flat?** Everything else — role count, area grouping, anti-pattern
watch, evolution roadmap — is downstream of that verdict. The inertia-advocate role is
not optional and is not a footnote; it is the named structural conscience of the org.

**Produces:**
- `org-chart.md` — opens with a FLAT-CASE-PRESSURE banner, then ASCII hierarchy, headcount
  table (Area / Headcount / Key Roles / Decides / Escalates), operating rhythm, committee
  charters, anti-pattern watch, org evolution roadmap, inertia verdict block
- `.craft/roles/{area}/{role}.md` — typed role files (orientation, lens, expertise, scope,
  collaborates_with) for every enumerated role, including inertia-advocate

---

## GLOBAL CONSTANTS

FORBIDDEN: re-defining or embedding these tables inside any phase instruction. Phase
instructions reference these constants by name only.

### CONST-1 — Verbatim IA Scope Templates (keyed to T2-PRESSURE)

MUST copy the applicable template verbatim into the `scope` field of the inertia-advocate
role file. FORBIDDEN: paraphrase, adaptation, or deviation of any kind.

| T2-PRESSURE | Verbatim Scope Template |
|-------------|-------------------------|
| NONE | Advocate for the current flat structure. No structural triggers are active. Document this baseline assessment for future comparison. Re-evaluate at the next team growth milestone. |
| LOW | Monitor for emerging coordination costs. Low-level structural pressure is present but does not yet warrant intervention. Document the flat-case rationale and schedule a reassessment at the 90-day mark. |
| MODERATE | Present the flat-case trade-offs explicitly at the next Review of Business. Moderate structural pressure is present. Document where coordination costs are accumulating and prepare a threshold analysis for leadership review before any growth-hire cycle begins. |
| HIGH | Formally defend the flat case or yield the argument in writing. High structural pressure requires a decision. If defending: produce a written flat-case brief for leadership sign-off. If yielding: specify the minimum viable structure change — one layer, named owner, scoped mandate — before any new hires join. |
| CRITICAL | Accept that flat operation is no longer defensible. Critical structural pressure requires immediate intervention. Document the accumulated inertia costs, propose a minimum viable hierarchy with named layers and owners, and recommend a transition timeline for executive sponsor review and approval. |

### CONST-2 — Anti-Pattern Category Derivation Table (keyed to T2-VERDICT)

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) | cat-1 (under-structure), cat-4 (span overload) |
| STRUCTURE-WARRANTED | cat-1 (under-structure), cat-4 (span overload) | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) |

---

## PHASE 1 — Structural Verdict

> The inertia verdict governs all downstream choices. FORBIDDEN: beginning Phase 2 before
> the `=== RECORD: PHASE-1 ===` block is emitted.

### Task Steps

**Sub-step 1-A — DETECT**: Read the invocation for a `--depth` flag.
Map: `--depth deep` → `deep`; absent flag → `standard`.
FORBIDDEN: beginning sub-step 1-B before completing sub-step 1-A.

**Sub-step 1-B — SCAN**: Examine the repository or scan results for structural pressure
indicators: span-of-control counts, cross-team dependency frequency, headcount relative
to domain complexity, management-layer count.
FORBIDDEN: beginning sub-step 1-C before completing sub-step 1-B.

**Sub-step 1-C — RATE**: Assign exactly one T2-PRESSURE rating from CONST-1's scale
(NONE / LOW / MODERATE / HIGH / CRITICAL).
Only one rating. Assigning more than one is an error. Assigning none is an error.
FORBIDDEN: beginning sub-step 1-D before completing sub-step 1-C.

**Sub-step 1-D — VERDICT**: Derive T2-VERDICT from T2-PRESSURE.
Rule: NONE or LOW → `CAN-OPERATE-FLAT`; MODERATE through CRITICAL → `STRUCTURE-WARRANTED`.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: beginning Phase 2 before completing sub-step 1-D.

### Constraints

- MUST complete sub-steps in order: 1-A → 1-B → 1-C → 1-D.
- FORBIDDEN: assigning T2-VERDICT before T2-PRESSURE is rated.
- FORBIDDEN: emitting a second verdict alongside the first.

### Gate: Emit RECORD: PHASE-1

FORBIDDEN: beginning Phase 2 before emitting this record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]                            → _______
T2-PRESSURE:   [NONE | LOW | MODERATE | HIGH | CRITICAL]   → _______
T2-VERDICT:    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]    → _______
=== END RECORD: PHASE-1 ===
```

---

## PHASE 2 — Role Enumeration

> The inertia verdict is locked. Role enumeration is now verdict-coherent by construction.
> FORBIDDEN: beginning Phase 3 before the `=== RECORD: PHASE-2 ===` block is emitted.

### Input Contract

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | RECORD: PHASE-1 | MUST use to set count floor per Constraints |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern IA scope template selection from CONST-1 |
| T2-PRESSURE | RECORD: PHASE-1 | MUST be the key for CONST-1 template lookup |

### Task Steps

**Sub-step 2-A — COUNT**: Enumerate all role names in a flat list.
- If T1-DEPTH-FLAG = `standard`: MUST enumerate 20–30 roles.
- If T1-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
- MUST include exactly one role with `inertia` or `advocate` in its name.
FORBIDDEN: beginning sub-step 2-B before completing sub-step 2-A.

**Sub-step 2-B — AREA**: Group the flat list into area subdirectories.
MUST produce a minimum of 2 area subdirs. Assign every role to exactly one area.
FORBIDDEN: beginning sub-step 2-C before completing sub-step 2-B.

**Sub-step 2-C — FILE**: Write each `.craft/roles/{area}/{role}.md` file. Every file MUST
contain exactly these five fields: `orientation`, `lens`, `expertise`, `scope`,
`collaborates_with`. For the inertia-advocate role: `scope` MUST be the verbatim text of
the CONST-1 template keyed to T2-PRESSURE. FORBIDDEN: paraphrasing the template.

### Constraints

- MUST complete sub-steps in order: 2-A → 2-B → 2-C.
- FORBIDDEN: writing role files before area grouping is complete.
- FORBIDDEN: writing the inertia-advocate scope field without first looking up CONST-1.
- FORBIDDEN: omitting any of the five required fields from any role file.
- FORBIDDEN: submitting a role count below the T1-DEPTH-FLAG floor.

### Gate: Emit RECORD: PHASE-2

FORBIDDEN: beginning Phase 3 before emitting this record block.

T3-ROLE-OUTCOME rules:
- T1-DEPTH-FLAG = `standard` AND count 20–30 → `STANDARD-FLOOR-MET`
- T1-DEPTH-FLAG = `deep` AND count 50+ → `DEEP-FLOOR-MET`
- Count below floor for either mode → `FLOOR-MISS`

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]   → _______
=== END RECORD: PHASE-2 ===
```

---

## PHASE 3 — Org-Chart Assembly

> FORBIDDEN: beginning Phase 4 before the `=== RECORD: PHASE-3 ===` block is emitted.

### Input Contract

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | RECORD: PHASE-1 | MUST appear as the FLAT-CASE-PRESSURE banner value |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern anti-pattern category selection via CONST-2 |
| T3-ROLE-OUTCOME | RECORD: PHASE-2 | MUST appear in the org-chart.md header block |

### Task Steps

**Sub-step 3-A — BANNER**: Open `org-chart.md` with a FLAT-CASE-PRESSURE banner:
```
FLAT-CASE-PRESSURE: [T2-PRESSURE value]   VERDICT: [T2-VERDICT value]
ROLE-OUTCOME: [T3-ROLE-OUTCOME value]
```
FORBIDDEN: beginning sub-step 3-B before completing sub-step 3-A.

**Sub-step 3-B — ASCII**: Draw the ASCII box-and-line org hierarchy with minimum 2 levels.
FORBIDDEN: beginning sub-step 3-C before completing sub-step 3-B.

**Sub-step 3-C — TABLE**: Write the headcount-by-area table.
Columns: `Area` | `Headcount` | `Key Roles` | `Decides` | `Escalates`.
FORBIDDEN: beginning sub-step 3-D before completing sub-step 3-C.

**Sub-step 3-D — ANTIPATTERN**: Write the Anti-Pattern Watch table. MUST use CONST-2 to
derive category selections for T2-VERDICT. Every "Why It Applies Here" cell MUST open with
`[element name] (cat-N) —` syntax. Every Mitigation cell MUST contain a specific remediation
action. FORBIDDEN: including any category from the FORBIDDEN column for the current T2-VERDICT.
FORBIDDEN: beginning sub-step 3-E before completing sub-step 3-D.

**Sub-step 3-E — ROADMAP**: Write the Org Evolution Roadmap with 2+ rows. Row 1 MUST be a
headcount threshold trigger. Row 2 MUST use a different trigger category (dependency count,
span overload, communication latency). FORBIDDEN: two headcount rows.
FORBIDDEN: beginning sub-step 3-F before completing sub-step 3-E.

**Sub-step 3-F — INERTIA BLOCK**: Write the inertia assessment block containing:
- `FLAT-CASE-PRESSURE: [exactly one rating from NONE/LOW/MODERATE/HIGH/CRITICAL]`
- Exactly one verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Only one verdict. Both is an error. Neither is an error.
Rating and verdict MUST match the values in RECORD: PHASE-1.

### Constraints

- MUST complete sub-steps in order: 3-A → 3-B → 3-C → 3-D → 3-E → 3-F.
- FORBIDDEN: selecting anti-pattern categories without consulting CONST-2.
- FORBIDDEN: writing the inertia block with values that differ from RECORD: PHASE-1.

### Gate: Emit RECORD: PHASE-3

FORBIDDEN: beginning Phase 4 before emitting this record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T4-CHART-STATUS: [COMPLETE | INCOMPLETE]   → _______
=== END RECORD: PHASE-3 ===
```

---

## PHASE 4 — Operating Rhythm and Committee Charters

### Input Contract

FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T4-CHART-STATUS | RECORD: PHASE-3 | MUST be `COMPLETE` before proceeding; FORBIDDEN if `INCOMPLETE` |

### Task Steps

**Sub-step 4-A — RHYTHM**: Write the operating rhythm table with 3+ distinct rows.
Row 1 MUST be ROB (Review of Business). Row 2 MUST be a shiproom or execution cadence.
Row 3 MUST be a governance meeting.
FORBIDDEN: beginning sub-step 4-B before completing sub-step 4-A.

**Sub-step 4-B — CHARTER**: Write one committee charter per governance meeting row.
Each charter MUST include all 5 fields: Name, Purpose, Cadence, Owner, Quorum.
Quorum MUST be expressed as `N of M` fraction (e.g., "3 of 5").
FORBIDDEN: expressing Quorum as a percentage or plain number.
FORBIDDEN: leaving any governance row in the rhythm table without a corresponding charter.

### Constraints

- MUST complete sub-steps in order: 4-A → 4-B.
- FORBIDDEN: writing charters before the rhythm table is complete.
```

---

## V-02 -- Axis: Lifecycle Emphasis

**Axis**: Lifecycle emphasis
**Hypothesis**: Triple-direction phase guards (outbound FORBIDDEN at gate, inbound FORBIDDEN
at consuming phase, intra-phase sub-step FORBIDDEN between sub-steps) combined with
extended RECORD blocks that carry an ordering anchor as a named structural field reduce
gate-crossing failures at every boundary. When the record block itself is the observable
checkpoint, a model cannot assert completion without emitting the sentinel.

```
You are executing the **org-build** skill.

**Produces:**
- `org-chart.md` — ASCII hierarchy, headcount table (Area / Headcount / Key Roles /
  Decides / Escalates), operating rhythm, committee charters, anti-pattern watch,
  org evolution roadmap, inertia verdict block
- `.craft/roles/{area}/{role}.md` — typed role files for every enumerated role

---

## GLOBAL CONSTANTS

FORBIDDEN: re-defining or embedding these tables inside any phase instruction.

### CONST-1 — Verbatim IA Scope Templates (keyed to T2-PRESSURE)

| T2-PRESSURE | Verbatim Scope Template |
|-------------|-------------------------|
| NONE | Advocate for the current flat structure. No structural triggers are active. Document this baseline assessment for future comparison. Re-evaluate at the next team growth milestone. |
| LOW | Monitor for emerging coordination costs. Low-level structural pressure is present but does not yet warrant intervention. Document the flat-case rationale and schedule a reassessment at the 90-day mark. |
| MODERATE | Present the flat-case trade-offs explicitly at the next Review of Business. Moderate structural pressure is present. Document where coordination costs are accumulating and prepare a threshold analysis for leadership review before any growth-hire cycle begins. |
| HIGH | Formally defend the flat case or yield the argument in writing. High structural pressure requires a decision. If defending: produce a written flat-case brief for leadership sign-off. If yielding: specify the minimum viable structure change — one layer, named owner, scoped mandate — before any new hires join. |
| CRITICAL | Accept that flat operation is no longer defensible. Critical structural pressure requires immediate intervention. Document the accumulated inertia costs, propose a minimum viable hierarchy with named layers and owners, and recommend a transition timeline for executive sponsor review and approval. |

### CONST-2 — Anti-Pattern Category Derivation Table (keyed to T2-VERDICT)

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) | cat-1 (under-structure), cat-4 (span overload) |
| STRUCTURE-WARRANTED | cat-1 (under-structure), cat-4 (span overload) | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) |

---

## PHASE 1 — Inertia Assessment

**Lifecycle anchor**: Phase 1 is the prerequisite gate. Its RECORD block is the entry
condition for all subsequent phases. FORBIDDEN: beginning Phase 2 before
`=== RECORD: PHASE-1 ===` is emitted and complete.

### Task Steps

**Sub-step 1-A — DETECT**: Read the invocation for a `--depth` flag.
Map: `--depth deep` → `deep`; absent flag → `standard`.
FORBIDDEN: beginning sub-step 1-B before completing sub-step 1-A.

**Sub-step 1-B — SCAN**: Examine the repository or scan results for structural pressure
indicators: span-of-control counts, cross-team dependency counts, headcount relative to
domain complexity, existing management-layer count.
FORBIDDEN: beginning sub-step 1-C before completing sub-step 1-B.

**Sub-step 1-C — RATE**: Assign exactly one T2-PRESSURE rating (NONE / LOW / MODERATE /
HIGH / CRITICAL). Only one rating. Assigning more than one is an error. Assigning none is
an error.
FORBIDDEN: beginning sub-step 1-D before completing sub-step 1-C.

**Sub-step 1-D — VERDICT**: Derive T2-VERDICT from T2-PRESSURE.
Rule: NONE or LOW → `CAN-OPERATE-FLAT`; MODERATE through CRITICAL → `STRUCTURE-WARRANTED`.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: beginning the RECORD block before completing sub-step 1-D.

### Constraints

- MUST complete all sub-steps in order: 1-A → 1-B → 1-C → 1-D.
- FORBIDDEN: assigning T2-VERDICT before T2-PRESSURE is rated.
- FORBIDDEN: emitting more than one verdict.
- FORBIDDEN: emitting zero verdicts.

### Gate: RECORD BLOCK — emit before Phase 2 begins

**Outbound**: FORBIDDEN: beginning Phase 2 before this record block is emitted.
**Inbound at Phase 2**: FORBIDDEN: executing Phase 2 before this record block exists.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]                            → _______
T2-PRESSURE:   [NONE | LOW | MODERATE | HIGH | CRITICAL]   → _______
T2-VERDICT:    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]    → _______
=== END RECORD: PHASE-1 ===
```

---

## PHASE 2 — Role Enumeration

**Lifecycle anchor**: Phase 2 uses Phase 1 gate outputs to make all role decisions verdict-
coherent. Its RECORD block gates Phase 3.
FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.
FORBIDDEN: beginning Phase 3 before `=== RECORD: PHASE-2 ===` is emitted and complete.

### Input Contract

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | RECORD: PHASE-1 | MUST bind count floor: standard → 20–30 roles; deep → 50+ roles |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern which CONST-1 template key to look up |
| T2-PRESSURE | RECORD: PHASE-1 | MUST be the key used to retrieve the verbatim IA scope template |

### Task Steps

**Sub-step 2-A — COUNT**: Enumerate all role names in a single flat list.
- T1-DEPTH-FLAG = `standard`: MUST enumerate 20–30 roles.
- T1-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
- MUST include exactly one role with `inertia` or `advocate` in its name.
FORBIDDEN: beginning sub-step 2-B before completing sub-step 2-A.

**Sub-step 2-B — AREA**: Group the flat list from sub-step 2-A into area subdirectories.
MUST produce minimum 2 area subdirs. Every role MUST be assigned to exactly one area.
FORBIDDEN: beginning sub-step 2-C before completing sub-step 2-B.

**Sub-step 2-C — FILE**: Write each `.craft/roles/{area}/{role}.md` file.
Every file MUST contain: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
For the inertia-advocate role: look up CONST-1 keyed to T2-PRESSURE and copy the verbatim
template into `scope`. FORBIDDEN: paraphrasing the CONST-1 template in any form.

### Constraints

- MUST complete sub-steps in order: 2-A → 2-B → 2-C.
- FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT.
- FORBIDDEN: beginning sub-step FILE before completing sub-step AREA.
- FORBIDDEN: writing role files before area assignment is complete.
- FORBIDDEN: submitting a role count below the floor for the operative T1-DEPTH-FLAG.
- FORBIDDEN: omitting any of the five required fields from any role file.

### Gate: RECORD BLOCK — emit before Phase 3 begins

T3-ROLE-OUTCOME composite token:
- T1-DEPTH-FLAG = `standard` AND count 20–30 → `STANDARD-FLOOR-MET`
- T1-DEPTH-FLAG = `deep` AND count 50+ → `DEEP-FLOOR-MET`
- Count below floor → `FLOOR-MISS`

**Outbound**: FORBIDDEN: beginning Phase 3 before this record block is emitted.
**Inbound at Phase 3**: FORBIDDEN: executing Phase 3 before this record block exists.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]   → _______
=== END RECORD: PHASE-2 ===
```

---

## PHASE 3 — Org-Chart Assembly

**Lifecycle anchor**: Phase 3 assembles `org-chart.md` using all locked gate outputs.
FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.
FORBIDDEN: beginning Phase 4 before `=== RECORD: PHASE-3 ===` is emitted and complete.

### Input Contract

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | RECORD: PHASE-1 | MUST appear as FLAT-CASE-PRESSURE rated value in inertia block |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern anti-pattern category selection via CONST-2 |
| T3-ROLE-OUTCOME | RECORD: PHASE-2 | MUST appear in the org-chart.md header |

### Task Steps

**Sub-step 3-A — ASCII**: Draw the ASCII box-and-line org hierarchy with minimum 2 levels.
FORBIDDEN: beginning sub-step 3-B before completing sub-step 3-A.

**Sub-step 3-B — TABLE**: Write the headcount-by-area table.
Columns: `Area` | `Headcount` | `Key Roles` | `Decides` | `Escalates`.
A table without Decides/Escalates columns fails.
FORBIDDEN: beginning sub-step 3-C before completing sub-step 3-B.

**Sub-step 3-C — ANTIPATTERN**: Write the Anti-Pattern Watch table using CONST-2 for
T2-VERDICT. Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
Every Mitigation cell MUST contain a remediation action, not format guidance.
FORBIDDEN: including FORBIDDEN-column categories from CONST-2.
FORBIDDEN: beginning sub-step 3-D before completing sub-step 3-C.

**Sub-step 3-D — ROADMAP**: Write the Org Evolution Roadmap with 2+ rows.
Row 1 MUST be a headcount threshold trigger. Row 2 MUST be a different trigger category.
FORBIDDEN: two headcount rows.
FORBIDDEN: beginning sub-step 3-E before completing sub-step 3-D.

**Sub-step 3-E — INERTIA**: Write the inertia assessment block.
MUST contain `FLAT-CASE-PRESSURE: [one rating]` and exactly one verdict.
Only one verdict. Both is an error. Neither is an error.
Symmetric guard: FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: writing neither.
Rating and verdict MUST match RECORD: PHASE-1 values.

### Constraints

- MUST complete sub-steps in order: 3-A → 3-B → 3-C → 3-D → 3-E.
- FORBIDDEN: selecting anti-pattern categories without consulting CONST-2.
- FORBIDDEN: inertia block values that differ from RECORD: PHASE-1.

### Gate: RECORD BLOCK — emit before Phase 4 begins

**Outbound**: FORBIDDEN: beginning Phase 4 before this record block is emitted.
**Inbound at Phase 4**: FORBIDDEN: executing Phase 4 before this record block exists.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T4-CHART-STATUS: [COMPLETE | INCOMPLETE]   → _______
=== END RECORD: PHASE-3 ===
```

---

## PHASE 4 — Operating Rhythm and Committee Charters

**Lifecycle anchor**: Terminal phase. No downstream gate required.
FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

### Input Contract

FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T4-CHART-STATUS | RECORD: PHASE-3 | MUST be `COMPLETE`; FORBIDDEN: proceeding if `INCOMPLETE` |

### Task Steps

**Sub-step 4-A — RHYTHM**: Write the operating rhythm table with 3+ distinct rows.
Row 1 MUST be ROB. Row 2 MUST be shiproom or execution cadence. Row 3 MUST be governance.
FORBIDDEN: beginning sub-step 4-B before completing sub-step 4-A.

**Sub-step 4-B — CHARTER**: Write one committee charter per governance row.
Each charter MUST include all 5 fields: Name, Purpose, Cadence, Owner, Quorum.
Quorum MUST be expressed as `N of M` fraction.
FORBIDDEN: Quorum as percentage or plain number.

### Constraints

- MUST complete sub-steps in order: 4-A → 4-B.
- FORBIDDEN: writing charters before rhythm table is complete.
- FORBIDDEN: leaving any governance row without a charter.

---

## Output Checklist

Before asserting completion, verify:
- [ ] `org-chart.md` exists with ASCII hierarchy (min 2 levels)
- [ ] Headcount table has all 5 columns including Decides/Escalates
- [ ] Anti-pattern watch uses cat-N citations; categories match CONST-2 for T2-VERDICT
- [ ] Inertia assessment block has `FLAT-CASE-PRESSURE:` with exactly one closed-set rating
- [ ] Org evolution roadmap has 2+ rows with mixed trigger types
- [ ] Operating rhythm has 3+ rows; charters complete with Quorum as `N of M`
- [ ] `.craft/roles/` has min 2 area subdirs; all 5 fields present in every role file
- [ ] inertia-advocate role present; scope is verbatim CONST-1 template keyed to T2-PRESSURE
- [ ] T3-ROLE-OUTCOME composite token matches actual count and T1-DEPTH-FLAG
- [ ] All RECORD blocks emitted before downstream phases began
```

---

## V-03 -- Axis: Role Sequence (Phase 0 Labeling)

**Axis**: Role sequence
**Hypothesis**: Numbering the inertia assessment phase as "Phase 0" — rather than Phase 1 —
makes its prerequisite status structurally unambiguous. When the inertia phase is Phase 0
and role enumeration is Phase 1, a model cannot reorder them without renumbering the
sequence entirely. The prerequisite is embedded in the numbering convention, not just in
a FORBIDDEN directive.

```
You are executing the **org-build** skill.

**Produces:**
- `org-chart.md` — ASCII hierarchy, headcount table (Area / Headcount / Key Roles /
  Decides / Escalates), operating rhythm, committee charters, anti-pattern watch,
  org evolution roadmap, inertia verdict block
- `.craft/roles/{area}/{role}.md` — typed role files for every enumerated role

---

## GLOBAL CONSTANTS

FORBIDDEN: re-defining or embedding these tables inside any phase instruction.

### CONST-1 — Verbatim IA Scope Templates (keyed to T2-PRESSURE)

| T2-PRESSURE | Verbatim Scope Template |
|-------------|-------------------------|
| NONE | Advocate for the current flat structure. No structural triggers are active. Document this baseline assessment for future comparison. Re-evaluate at the next team growth milestone. |
| LOW | Monitor for emerging coordination costs. Low-level structural pressure is present but does not yet warrant intervention. Document the flat-case rationale and schedule a reassessment at the 90-day mark. |
| MODERATE | Present the flat-case trade-offs explicitly at the next Review of Business. Moderate structural pressure is present. Document where coordination costs are accumulating and prepare a threshold analysis for leadership review before any growth-hire cycle begins. |
| HIGH | Formally defend the flat case or yield the argument in writing. High structural pressure requires a decision. If defending: produce a written flat-case brief for leadership sign-off. If yielding: specify the minimum viable structure change — one layer, named owner, scoped mandate — before any new hires join. |
| CRITICAL | Accept that flat operation is no longer defensible. Critical structural pressure requires immediate intervention. Document the accumulated inertia costs, propose a minimum viable hierarchy with named layers and owners, and recommend a transition timeline for executive sponsor review and approval. |

### CONST-2 — Anti-Pattern Category Derivation Table (keyed to T2-VERDICT)

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) | cat-1 (under-structure), cat-4 (span overload) |
| STRUCTURE-WARRANTED | cat-1 (under-structure), cat-4 (span overload) | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) |

---

## PHASE 0 — Inertia Assessment (Prerequisite Gate)

> Phase 0 is not a numbered step in a sequence — it is the precondition for the sequence.
> FORBIDDEN: beginning Phase 1 before the `=== RECORD: PHASE-0 ===` block is emitted.
> Phase 0 MUST complete before any Phase 1 labeling begins.

### Task Steps

**Sub-step 0-A — DETECT**: Read the invocation for a `--depth` flag.
Map: `--depth deep` → `deep`; absent flag → `standard`.
FORBIDDEN: beginning sub-step 0-B before completing sub-step 0-A.

**Sub-step 0-B — SCAN**: Examine the repository or scan results for structural pressure
indicators: span-of-control counts, cross-team dependency frequency, management-layer count.
FORBIDDEN: beginning sub-step 0-C before completing sub-step 0-B.

**Sub-step 0-C — RATE**: Assign exactly one T2-PRESSURE rating (NONE / LOW / MODERATE /
HIGH / CRITICAL). Only one rating. More than one is an error. None is an error.
FORBIDDEN: beginning sub-step 0-D before completing sub-step 0-C.

**Sub-step 0-D — VERDICT**: Derive T2-VERDICT from T2-PRESSURE.
Rule: NONE or LOW → `CAN-OPERATE-FLAT`; MODERATE through CRITICAL → `STRUCTURE-WARRANTED`.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: beginning the RECORD: PHASE-0 block before completing sub-step 0-D.

### Constraints

- MUST complete sub-steps in order: 0-A → 0-B → 0-C → 0-D.
- FORBIDDEN: assigning T2-VERDICT before T2-PRESSURE is rated.
- FORBIDDEN: emitting more than one verdict.
- FORBIDDEN: emitting zero verdicts.

### Gate: Emit RECORD: PHASE-0

FORBIDDEN: beginning Phase 1 before this record block is emitted. This gate is not
optional. FORBIDDEN: treating Phase 0 as skippable when a `--depth` flag is present.

```
=== RECORD: PHASE-0 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 1 begins before this block is emitted.
T0-DEPTH-FLAG: [standard | deep]                            → _______
T0-PRESSURE:   [NONE | LOW | MODERATE | HIGH | CRITICAL]   → _______
T0-VERDICT:    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]    → _______
=== END RECORD: PHASE-0 ===
```

---

## PHASE 1 — Role Enumeration

### Input Contract

FORBIDDEN: executing Phase 1 before Phase 0 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T0-DEPTH-FLAG | RECORD: PHASE-0 | MUST bind count floor: standard → 20–30 roles; deep → 50+ roles |
| T0-VERDICT | RECORD: PHASE-0 | MUST govern which CONST-1 template key to look up |
| T0-PRESSURE | RECORD: PHASE-0 | MUST be the key for CONST-1 template lookup |

### Task Steps

**Sub-step 1-A — COUNT**: Enumerate all role names in a flat list.
- T0-DEPTH-FLAG = `standard`: MUST enumerate 20–30 roles.
- T0-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
- MUST include exactly one role with `inertia` or `advocate` in its name.
FORBIDDEN: beginning sub-step 1-B (AREA) before completing sub-step 1-A (COUNT).

**Sub-step 1-B — AREA**: Group roles from sub-step 1-A into area subdirectories.
MUST produce minimum 2 area subdirs. Every role MUST be assigned to exactly one area.
FORBIDDEN: beginning sub-step 1-C (FILE) before completing sub-step 1-B (AREA).

**Sub-step 1-C — FILE**: Write each `.craft/roles/{area}/{role}.md` file.
Every file MUST contain: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
For the inertia-advocate role: copy the verbatim CONST-1 template keyed to T0-PRESSURE
into `scope`. FORBIDDEN: paraphrasing the template.

### Constraints

- MUST complete sub-steps in order: 1-A (COUNT) → 1-B (AREA) → 1-C (FILE).
- FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT.
- FORBIDDEN: beginning sub-step FILE before completing sub-step AREA.
- FORBIDDEN: submitting below the T0-DEPTH-FLAG count floor.
- FORBIDDEN: omitting any of the five required role file fields.

### Gate: Emit RECORD: PHASE-1

T1-ROLE-OUTCOME composite token:
- T0-DEPTH-FLAG = `standard` AND count 20–30 → `STANDARD-FLOOR-MET`
- T0-DEPTH-FLAG = `deep` AND count 50+ → `DEEP-FLOOR-MET`
- Count below floor → `FLOOR-MISS`

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]   → _______
=== END RECORD: PHASE-1 ===
```

---

## PHASE 2 — Org-Chart Assembly

### Input Contract

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T0-PRESSURE | RECORD: PHASE-0 | MUST appear as FLAT-CASE-PRESSURE value in inertia block |
| T0-VERDICT | RECORD: PHASE-0 | MUST govern anti-pattern category selection via CONST-2 |
| T1-ROLE-OUTCOME | RECORD: PHASE-1 | MUST appear in org-chart.md header |

### Task Steps

**Sub-step 2-A — ASCII**: Draw the ASCII box-and-line org hierarchy with minimum 2 levels.
FORBIDDEN: beginning sub-step 2-B before completing sub-step 2-A.

**Sub-step 2-B — TABLE**: Write the headcount-by-area table with columns:
`Area` | `Headcount` | `Key Roles` | `Decides` | `Escalates`.
FORBIDDEN: beginning sub-step 2-C before completing sub-step 2-B.

**Sub-step 2-C — ANTIPATTERN**: Write the Anti-Pattern Watch table. Use CONST-2 for
T0-VERDICT. Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
Every Mitigation cell MUST contain a remediation action.
FORBIDDEN: categories from the FORBIDDEN column for current T0-VERDICT.
FORBIDDEN: beginning sub-step 2-D before completing sub-step 2-C.

**Sub-step 2-D — ROADMAP**: Write the Org Evolution Roadmap with 2+ rows.
Row 1 MUST be a headcount threshold trigger. Row 2 MUST be a different trigger category.
FORBIDDEN: beginning sub-step 2-E before completing sub-step 2-D.

**Sub-step 2-E — INERTIA**: Write the inertia assessment block.
MUST contain `FLAT-CASE-PRESSURE: [one rating]` and exactly one verdict.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: writing neither.

### Constraints

- MUST complete sub-steps in order: 2-A → 2-B → 2-C → 2-D → 2-E.
- FORBIDDEN: anti-pattern categories without consulting CONST-2.

### Gate: Emit RECORD: PHASE-2

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-CHART-STATUS: [COMPLETE | INCOMPLETE]   → _______
=== END RECORD: PHASE-2 ===
```

---

## PHASE 3 — Operating Rhythm and Committee Charters

### Input Contract

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T2-CHART-STATUS | RECORD: PHASE-2 | MUST be `COMPLETE`; FORBIDDEN: proceeding if `INCOMPLETE` |

### Task Steps

**Sub-step 3-A — RHYTHM**: Write the operating rhythm table with 3+ distinct rows.
Row 1 MUST be ROB. Row 2 MUST be shiproom or execution cadence. Row 3 MUST be governance.
FORBIDDEN: beginning sub-step 3-B before completing sub-step 3-A.

**Sub-step 3-B — CHARTER**: Write one charter per governance row. Each charter MUST include
all 5 fields: Name, Purpose, Cadence, Owner, Quorum. Quorum MUST be `N of M` fraction.

### Constraints

- MUST complete sub-steps in order: 3-A → 3-B.
- FORBIDDEN: charters before rhythm table is complete.
- FORBIDDEN: any governance row without a charter.
```

---

## V-04 -- Axis: Lifecycle Emphasis + Phrasing Register

**Axis**: Lifecycle emphasis + Phrasing register
**Hypothesis**: Combining maximum phase-boundary formalism with a strict MUST/FORBIDDEN-only
register — eliminating all advisory language throughout — closes C-19 and C-29 failures
simultaneously. When every instruction in every phase is either MUST [action] or
FORBIDDEN: [action], advisory drift ("should", "prefer", "consider") cannot appear in any
constraint context. The register is structurally enforced by construction.

```
You are executing the **org-build** skill.

**MUST produce:**
- `org-chart.md` — ASCII hierarchy, headcount table (Area / Headcount / Key Roles /
  Decides / Escalates), operating rhythm, committee charters, anti-pattern watch,
  org evolution roadmap, inertia verdict block
- `.craft/roles/{area}/{role}.md` — typed role files for every enumerated role

---

## GLOBAL CONSTANTS

FORBIDDEN: re-defining or embedding these tables inside any phase instruction.
FORBIDDEN: referencing any lookup table other than CONST-1 or CONST-2 for verdict-keyed
selections.

### CONST-1 — Verbatim IA Scope Templates (keyed to T2-PRESSURE)

| T2-PRESSURE | Verbatim Scope Template |
|-------------|-------------------------|
| NONE | Advocate for the current flat structure. No structural triggers are active. Document this baseline assessment for future comparison. Re-evaluate at the next team growth milestone. |
| LOW | Monitor for emerging coordination costs. Low-level structural pressure is present but does not yet warrant intervention. Document the flat-case rationale and schedule a reassessment at the 90-day mark. |
| MODERATE | Present the flat-case trade-offs explicitly at the next Review of Business. Moderate structural pressure is present. Document where coordination costs are accumulating and prepare a threshold analysis for leadership review before any growth-hire cycle begins. |
| HIGH | Formally defend the flat case or yield the argument in writing. High structural pressure requires a decision. If defending: produce a written flat-case brief for leadership sign-off. If yielding: specify the minimum viable structure change — one layer, named owner, scoped mandate — before any new hires join. |
| CRITICAL | Accept that flat operation is no longer defensible. Critical structural pressure requires immediate intervention. Document the accumulated inertia costs, propose a minimum viable hierarchy with named layers and owners, and recommend a transition timeline for executive sponsor review and approval. |

### CONST-2 — Anti-Pattern Category Derivation Table (keyed to T2-VERDICT)

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) | cat-1 (under-structure), cat-4 (span overload) |
| STRUCTURE-WARRANTED | cat-1 (under-structure), cat-4 (span overload) | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) |

---

## PHASE 1 — Inertia Assessment

FORBIDDEN: beginning Phase 2 before `=== RECORD: PHASE-1 ===` is emitted.

### Task Steps

1. **DETECT** — Read the `--depth` flag. MUST map `--depth deep` to `deep`; MUST map absent
   flag to `standard`.
2. **SCAN** — MUST examine span-of-control counts, dependency frequency, headcount, and
   management-layer depth from the repository or scan results.
3. **RATE** — MUST assign exactly one T2-PRESSURE rating from: NONE / LOW / MODERATE /
   HIGH / CRITICAL.
4. **VERDICT** — MUST derive T2-VERDICT: NONE or LOW → `CAN-OPERATE-FLAT`; MODERATE
   through CRITICAL → `STRUCTURE-WARRANTED`.

### Constraints

- MUST execute task steps in order: DETECT → SCAN → RATE → VERDICT.
- FORBIDDEN: beginning sub-step SCAN before completing sub-step DETECT.
- FORBIDDEN: beginning sub-step RATE before completing sub-step SCAN.
- FORBIDDEN: beginning sub-step VERDICT before completing sub-step RATE.
- FORBIDDEN: assigning T2-VERDICT before T2-PRESSURE is rated.
- FORBIDDEN: emitting more than one T2-VERDICT value.
- FORBIDDEN: emitting zero T2-VERDICT values.
- FORBIDDEN: beginning Phase 2 before all DETECT → VERDICT sub-steps are complete.

### Gate: RECORD: PHASE-1

FORBIDDEN: beginning Phase 2 before this block is emitted.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]                            → _______
T2-PRESSURE:   [NONE | LOW | MODERATE | HIGH | CRITICAL]   → _______
T2-VERDICT:    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]    → _______
=== END RECORD: PHASE-1 ===
```

---

## PHASE 2 — Role Enumeration

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.
FORBIDDEN: beginning Phase 3 before `=== RECORD: PHASE-2 ===` is emitted.

### Input Contract

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | RECORD: PHASE-1 | MUST bind count floor |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern CONST-1 template key |
| T2-PRESSURE | RECORD: PHASE-1 | MUST be the CONST-1 lookup key |

### Task Steps

1. **COUNT** — MUST enumerate all role names in a flat list.
   - T1-DEPTH-FLAG = `standard`: MUST enumerate 20–30 roles.
   - T1-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
   - MUST include exactly one role with `inertia` or `advocate` in its name.
2. **AREA** — MUST group roles from COUNT into area subdirectories.
   MUST produce minimum 2 area subdirs. MUST assign every role to exactly one area.
3. **FILE** — MUST write each `.craft/roles/{area}/{role}.md` file.
   MUST include all five fields: `orientation`, `lens`, `expertise`, `scope`,
   `collaborates_with`.
   MUST copy the CONST-1 template keyed to T2-PRESSURE verbatim into `scope` for the
   inertia-advocate role.

### Constraints

- MUST execute task steps in order: COUNT → AREA → FILE.
- FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT.
- FORBIDDEN: beginning sub-step FILE before completing sub-step AREA.
- FORBIDDEN: writing role files before area assignment is finalized.
- FORBIDDEN: submitting below the T1-DEPTH-FLAG count floor.
- FORBIDDEN: omitting any required role file field.
- FORBIDDEN: paraphrasing the CONST-1 template in the inertia-advocate scope field.
- FORBIDDEN: looking up any scope template key other than T2-PRESSURE.

### Gate: RECORD: PHASE-2

FORBIDDEN: beginning Phase 3 before this block is emitted.

T3-ROLE-OUTCOME composite token derivation:
- T1-DEPTH-FLAG = `standard` AND count 20–30 → MUST assign `STANDARD-FLOOR-MET`
- T1-DEPTH-FLAG = `deep` AND count 50+ → MUST assign `DEEP-FLOOR-MET`
- Count below floor for either mode → MUST assign `FLOOR-MISS`

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]   → _______
=== END RECORD: PHASE-2 ===
```

---

## PHASE 3 — Org-Chart Assembly

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.
FORBIDDEN: beginning Phase 4 before `=== RECORD: PHASE-3 ===` is emitted.

### Input Contract

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | RECORD: PHASE-1 | MUST be the FLAT-CASE-PRESSURE value in the inertia block |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern anti-pattern categories via CONST-2 |
| T3-ROLE-OUTCOME | RECORD: PHASE-2 | MUST appear in org-chart.md header |

### Task Steps

1. **ASCII** — MUST draw the ASCII box-and-line org hierarchy with minimum 2 levels.
2. **TABLE** — MUST write the headcount-by-area table.
   MUST include columns: `Area` | `Headcount` | `Key Roles` | `Decides` | `Escalates`.
3. **ANTIPATTERN** — MUST write the Anti-Pattern Watch table using CONST-2 for T2-VERDICT.
   MUST open every "Why It Applies Here" cell with `[element name] (cat-N) —` syntax.
   MUST include a remediation action in every Mitigation cell.
4. **ROADMAP** — MUST write the Org Evolution Roadmap with 2+ rows.
   MUST make Row 1 a headcount threshold trigger.
   MUST make Row 2 a different trigger category.
5. **INERTIA** — MUST write the inertia assessment block with `FLAT-CASE-PRESSURE: [rating]`
   and exactly one verdict. FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither.
   MUST match values to RECORD: PHASE-1.

### Constraints

- MUST execute task steps in order: ASCII → TABLE → ANTIPATTERN → ROADMAP → INERTIA.
- FORBIDDEN: beginning TABLE before completing ASCII.
- FORBIDDEN: beginning ANTIPATTERN before completing TABLE.
- FORBIDDEN: beginning ROADMAP before completing ANTIPATTERN.
- FORBIDDEN: beginning INERTIA before completing ROADMAP.
- FORBIDDEN: selecting anti-pattern categories without consulting CONST-2.
- FORBIDDEN: including categories from the FORBIDDEN column in CONST-2.
- FORBIDDEN: inertia block values that differ from RECORD: PHASE-1 values.

### Gate: RECORD: PHASE-3

FORBIDDEN: beginning Phase 4 before this block is emitted.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T4-CHART-STATUS: [COMPLETE | INCOMPLETE]   → _______
=== END RECORD: PHASE-3 ===
```

---

## PHASE 4 — Operating Rhythm and Committee Charters

FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

### Input Contract

FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T4-CHART-STATUS | RECORD: PHASE-3 | MUST be `COMPLETE`; FORBIDDEN: proceeding if `INCOMPLETE` |

### Task Steps

1. **RHYTHM** — MUST write the operating rhythm table with 3+ distinct rows.
   MUST include ROB as Row 1. MUST include shiproom or execution cadence as Row 2.
   MUST include a governance meeting as Row 3.
2. **CHARTER** — MUST write one committee charter per governance row.
   MUST include all 5 fields: Name, Purpose, Cadence, Owner, Quorum.
   MUST express Quorum as `N of M` fraction.

### Constraints

- MUST execute task steps in order: RHYTHM → CHARTER.
- FORBIDDEN: beginning CHARTER before completing RHYTHM.
- FORBIDDEN: expressing Quorum as a percentage or plain number.
- FORBIDDEN: leaving any governance row without a corresponding charter.
```

---

## V-05 -- Axis: Inertia Framing + Output Format

**Axis**: Inertia framing + Output format
**Hypothesis**: Combining a table-dominant output format with composite typed tokens and a
pre-print skeleton keyed to gate variables satisfies C-22 (skeleton with named slots),
C-38 (composite tokens), and C-34 (side-by-side required/FORBIDDEN columns) while keeping
inertia framing as a structural presence in every table. When the org-chart.md skeleton
explicitly names `{{T2-VERDICT}}` and `{{T3-ROLE-OUTCOME}}` as slot tokens, a reader can
derive the gate schema from the template alone.

```
You are executing the **org-build** skill.

**Produces:**
- `org-chart.md` — structured via the pre-print skeleton below; all `{{SLOT}}` tokens
  replaced with values from RECORD blocks before writing
- `.craft/roles/{area}/{role}.md` — typed role files for every enumerated role

---

## GLOBAL CONSTANTS

FORBIDDEN: re-defining or embedding these tables inside any phase instruction.

### CONST-1 — Verbatim IA Scope Templates (keyed to T2-PRESSURE)

| T2-PRESSURE | Verbatim Scope Template |
|-------------|-------------------------|
| NONE | Advocate for the current flat structure. No structural triggers are active. Document this baseline assessment for future comparison. Re-evaluate at the next team growth milestone. |
| LOW | Monitor for emerging coordination costs. Low-level structural pressure is present but does not yet warrant intervention. Document the flat-case rationale and schedule a reassessment at the 90-day mark. |
| MODERATE | Present the flat-case trade-offs explicitly at the next Review of Business. Moderate structural pressure is present. Document where coordination costs are accumulating and prepare a threshold analysis for leadership review before any growth-hire cycle begins. |
| HIGH | Formally defend the flat case or yield the argument in writing. High structural pressure requires a decision. If defending: produce a written flat-case brief for leadership sign-off. If yielding: specify the minimum viable structure change — one layer, named owner, scoped mandate — before any new hires join. |
| CRITICAL | Accept that flat operation is no longer defensible. Critical structural pressure requires immediate intervention. Document the accumulated inertia costs, propose a minimum viable hierarchy with named layers and owners, and recommend a transition timeline for executive sponsor review and approval. |

### CONST-2 — Anti-Pattern Category Derivation Table (keyed to T2-VERDICT)

| T2-VERDICT | Required Categories | FORBIDDEN Categories |
|------------|---------------------|----------------------|
| CAN-OPERATE-FLAT | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) | cat-1 (under-structure), cat-4 (span overload) |
| STRUCTURE-WARRANTED | cat-1 (under-structure), cat-4 (span overload) | cat-2 (premature hierarchy), cat-3 (invisible coordination tax) |

### CONST-3 — Pre-Print Skeleton for org-chart.md

All `{{SLOT}}` tokens are named gate variables. MUST replace each slot verbatim with the
value emitted in the corresponding RECORD block. A slot left as `{{SLOT}}` fails.

```
# Org Chart — {{ORG-NAME}}
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}   VERDICT: {{T2-VERDICT}}   ROLE-OUTCOME: {{T3-ROLE-OUTCOME}}

## Hierarchy
[ASCII diagram]

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{HEADCOUNT-ROWS}}

## Anti-Pattern Watch
| Pattern | Why It Applies Here | Mitigation |
|---------|---------------------|------------|
{{ANTIPATTERN-ROWS}}

## Org Evolution Roadmap
| Trigger | Category | Threshold | Recommended Action |
|---------|----------|-----------|-------------------|
{{ROADMAP-ROWS}}

## Operating Rhythm
| Meeting | Cadence | Owner | Purpose |
|---------|---------|-------|---------|
{{RHYTHM-ROWS}}

## Committee Charters
{{CHARTER-BLOCKS}}

## Inertia Assessment
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```

---

## PHASE 1 — Inertia Assessment

FORBIDDEN: beginning Phase 2 before `=== RECORD: PHASE-1 ===` is emitted.

### Task Steps

**Sub-step 1-A — DETECT**: Read the `--depth` flag.
Map: `--depth deep` → `deep`; absent → `standard`.
FORBIDDEN: beginning sub-step 1-B before completing sub-step 1-A.

**Sub-step 1-B — SCAN**: Examine structural pressure indicators from the repository or scan.
FORBIDDEN: beginning sub-step 1-C before completing sub-step 1-B.

**Sub-step 1-C — RATE**: Assign exactly one T2-PRESSURE rating (NONE / LOW / MODERATE /
HIGH / CRITICAL). Only one. More than one is an error. None is an error.
FORBIDDEN: beginning sub-step 1-D before completing sub-step 1-C.

**Sub-step 1-D — VERDICT**: Derive T2-VERDICT.
Rule: NONE or LOW → `CAN-OPERATE-FLAT`; MODERATE through CRITICAL → `STRUCTURE-WARRANTED`.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither.

### Constraints

- MUST complete sub-steps in order: 1-A → 1-B → 1-C → 1-D.
- FORBIDDEN: beginning sub-step 1-B before completing sub-step 1-A.
- FORBIDDEN: beginning sub-step 1-C before completing sub-step 1-B.
- FORBIDDEN: beginning sub-step 1-D before completing sub-step 1-C.
- FORBIDDEN: deriving T2-VERDICT without first completing T2-PRESSURE rating.

### Gate: Emit RECORD: PHASE-1

FORBIDDEN: beginning Phase 2 before this block is emitted.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: [standard | deep]                            → _______
T2-PRESSURE:   [NONE | LOW | MODERATE | HIGH | CRITICAL]   → _______
T2-VERDICT:    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]    → _______
=== END RECORD: PHASE-1 ===
```

---

## PHASE 2 — Role Enumeration

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.
FORBIDDEN: beginning Phase 3 before `=== RECORD: PHASE-2 ===` is emitted.

### Input Contract

FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T1-DEPTH-FLAG | RECORD: PHASE-1 | MUST bind count floor: standard → 20–30; deep → 50+ |
| T2-VERDICT | RECORD: PHASE-1 | MUST govern CONST-1 template selection |
| T2-PRESSURE | RECORD: PHASE-1 | MUST be the CONST-1 lookup key for IA scope |

### Task Steps

**Sub-step 2-A — COUNT**: Enumerate all role names in a flat list.
- T1-DEPTH-FLAG = `standard`: MUST enumerate 20–30 roles.
- T1-DEPTH-FLAG = `deep`: MUST enumerate 50+ roles.
- MUST include exactly one role with `inertia` or `advocate` in its name.
FORBIDDEN: beginning sub-step 2-B (AREA) before completing sub-step 2-A (COUNT).

**Sub-step 2-B — AREA**: Group roles into area subdirectories.
MUST produce minimum 2 area subdirs. MUST assign every role to exactly one area.
FORBIDDEN: beginning sub-step 2-C (FILE) before completing sub-step 2-B (AREA).

**Sub-step 2-C — FILE**: Write each `.craft/roles/{area}/{role}.md` file.
MUST include all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
For inertia-advocate: MUST copy the CONST-1 template keyed to T2-PRESSURE verbatim into
`scope`. FORBIDDEN: paraphrasing.

### Constraints

- MUST complete sub-steps in order: COUNT → AREA → FILE.
- FORBIDDEN: beginning sub-step AREA before completing sub-step COUNT.
- FORBIDDEN: beginning sub-step FILE before completing sub-step AREA.
- FORBIDDEN: submitting below the T1-DEPTH-FLAG count floor.
- FORBIDDEN: omitting any of the five required role file fields.
- FORBIDDEN: paraphrasing the CONST-1 template.

### Gate: Emit RECORD: PHASE-2

T3-ROLE-OUTCOME composite token (encodes mode × compliance in a single value):

| T1-DEPTH-FLAG | Count Result | T3-ROLE-OUTCOME |
|---------------|-------------|-----------------|
| standard | 20–30 (floor met) | STANDARD-FLOOR-MET |
| deep | 50+ (floor met) | DEEP-FLOOR-MET |
| standard or deep | Below floor | FLOOR-MISS |

FORBIDDEN: beginning Phase 3 before this block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET | DEEP-FLOOR-MET | FLOOR-MISS]   → _______
=== END RECORD: PHASE-2 ===
```

---

## PHASE 3 — Org-Chart Assembly

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.
FORBIDDEN: beginning Phase 4 before `=== RECORD: PHASE-3 ===` is emitted.

### Input Contract

FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T2-PRESSURE | RECORD: PHASE-1 | MUST fill `{{T2-PRESSURE}}` slots in CONST-3 skeleton |
| T2-VERDICT | RECORD: PHASE-1 | MUST fill `{{T2-VERDICT}}` slots; MUST govern CONST-2 selection |
| T3-ROLE-OUTCOME | RECORD: PHASE-2 | MUST fill `{{T3-ROLE-OUTCOME}}` slot in CONST-3 skeleton |

### Task Steps

**Sub-step 3-A — FILL-HEADER**: Replace the CONST-3 skeleton header slots:
`{{T2-PRESSURE}}`, `{{T2-VERDICT}}`, `{{T3-ROLE-OUTCOME}}` with RECORD block values.
FORBIDDEN: beginning sub-step 3-B before completing sub-step 3-A.

**Sub-step 3-B — ASCII**: Draw the ASCII hierarchy and insert into the skeleton Hierarchy
section. MUST include minimum 2 levels.
FORBIDDEN: beginning sub-step 3-C before completing sub-step 3-B.

**Sub-step 3-C — TABLE**: Fill the `{{HEADCOUNT-ROWS}}` slot with one row per area.
Columns: Area / Headcount / Key Roles / Decides / Escalates.
FORBIDDEN: beginning sub-step 3-D before completing sub-step 3-C.

**Sub-step 3-D — ANTIPATTERN**: Fill `{{ANTIPATTERN-ROWS}}` using CONST-2 for T2-VERDICT.
Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
Every Mitigation cell MUST contain a remediation action.
FORBIDDEN: categories from CONST-2's FORBIDDEN column for current T2-VERDICT.
FORBIDDEN: beginning sub-step 3-E before completing sub-step 3-D.

**Sub-step 3-E — ROADMAP**: Fill `{{ROADMAP-ROWS}}` with 2+ rows.
Row 1 MUST be a headcount threshold trigger. Row 2 MUST use a different trigger category.
FORBIDDEN: beginning sub-step 3-F before completing sub-step 3-E.

**Sub-step 3-F — INERTIA**: Fill the Inertia Assessment section of the skeleton.
MUST include `FLAT-CASE-PRESSURE: {{T2-PRESSURE}}` (filled) and exactly one verdict.
FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither.

### Constraints

- MUST complete sub-steps in order: FILL-HEADER → ASCII → TABLE → ANTIPATTERN → ROADMAP → INERTIA.
- FORBIDDEN: beginning any sub-step before the preceding sub-step is complete.
- FORBIDDEN: leaving any `{{SLOT}}` token unfilled in the final org-chart.md.
- FORBIDDEN: selecting anti-pattern categories without consulting CONST-2.
- FORBIDDEN: inertia values that differ from RECORD: PHASE-1.

### Gate: Emit RECORD: PHASE-3

FORBIDDEN: beginning Phase 4 before this block is emitted.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T4-CHART-STATUS: [COMPLETE | INCOMPLETE]   → _______
=== END RECORD: PHASE-3 ===
```

---

## PHASE 4 — Operating Rhythm and Committee Charters

FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

### Input Contract

FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.

| Variable | Source | Binding |
|----------|--------|---------|
| T4-CHART-STATUS | RECORD: PHASE-3 | MUST be `COMPLETE`; FORBIDDEN: proceeding if `INCOMPLETE` |

### Task Steps

**Sub-step 4-A — RHYTHM**: Fill `{{RHYTHM-ROWS}}` with 3+ distinct rows.
Row 1 MUST be ROB. Row 2 MUST be shiproom or execution cadence. Row 3 MUST be governance.
FORBIDDEN: beginning sub-step 4-B before completing sub-step 4-A.

**Sub-step 4-B — CHARTER**: Fill `{{CHARTER-BLOCKS}}` with one charter per governance row.
Each charter MUST include all 5 fields: Name, Purpose, Cadence, Owner, Quorum.
Quorum MUST be `N of M` fraction.

### Constraints

- MUST complete sub-steps in order: RHYTHM → CHARTER.
- FORBIDDEN: beginning sub-step CHARTER before completing sub-step RHYTHM.
- FORBIDDEN: Quorum expressed as percentage or plain number.
- FORBIDDEN: any governance row without a charter.
```
