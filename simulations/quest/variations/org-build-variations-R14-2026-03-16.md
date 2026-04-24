## V-01 — Full Structural Compliance Baseline

**Variation axis**: Lifecycle emphasis — every phase gate explicit, record blocks structurally unified
**Hypothesis**: Maximum structural explicitness at every phase boundary produces the most consistent coverage of all 32 criteria; this is the control prompt against which all other variations are measured.

---

```markdown
You are executing the **org-build** skill. Generate a complete organizational design from
the provided scan results or repository path. Produce two artifacts: `org-chart.md` and
typed `.roles/{area}/{role}.md` files for every role.

## Inputs

- `SOURCE`: scan results file path or repository path (required)
- `DEPTH`: `standard` (default, 20–30 roles) or `deep` (50+ roles)

---

## Phase 1 — Intake and Depth Assessment

### Task Steps

1. Read the source. Identify whether it is scan-results output or a raw repository path.
2. Confirm or assign the depth flag from the `DEPTH` input. If absent, default to `standard`.
3. Record both values in the Phase 1 record block before proceeding.

### Constraints

MUST assign exactly one value from `[standard | deep]` to T1-DEPTH-FLAG.
MUST assign exactly one value from `[scan-results | repo-direct]` to T1-SOURCE.
FORBIDDEN: proceeding to Phase 2 before emitting the Phase 1 record block.

---

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: ___    [standard | deep]
T1-SOURCE:     ___    [scan-results | repo-direct]
===
```

---

## Phase 2 — Role Enumeration

### Input Contract

FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.
MUST read T1-DEPTH-FLAG from the Phase 1 record block before enumerating roles.

### Task Steps

1. Enumerate all roles appropriate to the source. Group each role under a named area.
2. Apply the depth-conditional count floor:
   - T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles across a minimum of 4 areas.
   - T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles across a minimum of 6 areas.
3. MUST include a role with `inertia` or `advocate` in its name (the inertia-advocate role).
4. Produce a flat enumeration list: `area/role-name` for every role.

### Constraints

MUST include the inertia-advocate role. FORBIDDEN: omitting it.
FORBIDDEN: enumerating fewer roles than the T1-DEPTH-FLAG lower bound.
FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

---

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:  ___    [integer ≥ 20]
T2-AREA-COUNT:  ___    [integer ≥ 4]
T2-IA-PRESENT:  ___    [yes | no]
===
```

---

## Phase 3 — Structural Assessment

### Input Contract

FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.
MUST read T2-ROLE-COUNT and T2-AREA-COUNT from the Phase 2 record block.

### Task Steps

1. Evaluate the org structure for structural pressure across five signals:
   - span-of-control breadth, decision velocity, escalation concentration,
     accountability clarity, and cross-area coordination cost.
2. Assign a FLAT-CASE-PRESSURE rating using the closed set below.
3. Issue exactly one verdict — `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
   Only one verdict. Both is an error. Neither is an error.

**FLAT-CASE-PRESSURE rating definitions:**

| Rating | Signal threshold |
|--------|-----------------|
| NONE | No structural friction detected across all five signals |
| LOW | One signal shows friction; others nominal |
| MODERATE | Two signals show friction; no signal is severe |
| HIGH | Three or more signals show friction, or one signal is severe |
| CRITICAL | Multiple severe signals; current structure is blocking execution |

**Verdict derivation:**

| Rating | Verdict |
|--------|---------|
| NONE, LOW | CAN-OPERATE-FLAT |
| MODERATE | CAN-OPERATE-FLAT (if headcount < 40) or STRUCTURE-WARRANTED |
| HIGH, CRITICAL | STRUCTURE-WARRANTED |

### Constraints

MUST assign exactly one FLAT-CASE-PRESSURE rating.
MUST issue exactly one verdict. FORBIDDEN: issuing both. FORBIDDEN: issuing neither.
FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

---

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-PRESSURE: ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
T3-VERDICT:  ___    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
===
```

---

## Phase 4 — Derivation

### Input Contract

FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.
MUST read T3-PRESSURE and T3-VERDICT from the Phase 3 record block before
deriving anti-pattern categories or the IA scope text.

### Task Steps

#### 4A — Anti-Pattern Category Derivation

Derive the applicable anti-pattern categories from T3-VERDICT using the table below.

| T3-VERDICT | Required categories | FORBIDDEN categories |
|------------|--------------------|--------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

**Category definitions:**
- cat-1: Span-of-control excess — too many direct reports per decision node
- cat-2: Cross-area coordination loss — unclear ownership between flat peer areas
- cat-3: Accountability diffusion — responsibilities without named owners
- cat-4: Escalation bottleneck — critical decisions funneling through too few nodes

Populate the Anti-Pattern Watch table (format in Phase 5) using only the required
categories for the T3-VERDICT path.

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.
Every Mitigation cell MUST contain a specific remediation action. FORBIDDEN: format
instructions or column-structure guidance in any Mitigation cell.

#### 4B — IA Scope Template Selection

Select the IA scope text verbatim from the table below using T3-PRESSURE as the key.
FORBIDDEN: paraphrasing, adapting, or composing new text. MUST copy the exact template.

| T3-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | `Monitor org evolution triggers from the Org Evolution Roadmap. No structural intervention warranted. Flag any headcount event that crosses a documented threshold.` |
| LOW | `Track the two lowest-priority items in the Anti-Pattern Watch table. Revisit structural need at the next quarterly review. No intervention required before that checkpoint.` |
| MODERATE | `Own the Anti-Pattern Watch table as a live inertia risk register. Schedule a cross-area retrospective within 60 days. Produce an owner-assigned action list before the retrospective closes.` |
| HIGH | `Convene an org design review within 30 days. Produce a structural change proposal with named decision owners, a 90-day action plan, and a ratification checkpoint at 45 days.` |
| CRITICAL | `Initiate an emergency org redesign. FORBIDDEN: committing to any deliverable that depends on the current structure until a revised charter is ratified by the governing committee.` |

### Constraints

MUST apply the required anti-pattern categories for the T3-VERDICT path.
FORBIDDEN: using categories from the forbidden set for the T3-VERDICT path.
MUST copy the IA scope text verbatim. FORBIDDEN: paraphrasing or adapting the template.
FORBIDDEN: beginning Phase 5 before emitting the Phase 4 record block.

---

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-ANTIPATTERN-CATS: ___    [cat-1,cat-4 | cat-2,cat-3]
T4-IA-SCOPE-KEY:     ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
===
```

---

## Phase 5 — Output Production

### Input Contract

FORBIDDEN: executing Phase 5 before the Phase 4 record block is emitted.
MUST read T3-PRESSURE, T3-VERDICT from Phase 3 and T4-ANTIPATTERN-CATS,
T4-IA-SCOPE-KEY from Phase 4 before generating any output file.

### Task Steps

#### 5A — Generate org-chart.md

Produce `org-chart.md` using the skeleton below. Fill every `{{placeholder}}` with the
value recorded in the named phase gate variable.

```markdown
# Org Chart — {{T1-SOURCE}}

## ASCII Structure Diagram

[Insert ASCII box-and-line hierarchy with minimum 2 org levels]

## Structural Assessment

FLAT-CASE-PRESSURE: {{T3-PRESSURE}}
VERDICT: {{T3-VERDICT}}

Only one verdict. Both is an error. Neither is an error.

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| ...  | ...       | ...       | ...     | ...       |

## Operating Rhythm

| Cadence | Meeting | Owner | Participants | Purpose |
|---------|---------|-------|--------------|---------|
| Weekly  | Shiproom | [owner] | [list] | Unblock active delivery |
| Bi-weekly | ROB | [owner] | [list] | Review commitments vs actuals |
| Quarterly | Governance | [owner] | [list] | Ratify structural decisions |

## Committee Charters

### [Governance Meeting Name]
- **Owner**: [name/role]
- **Quorum**: N of M
- **Frequency**: [cadence]
- **Scope**: [what it decides]
- **Escalates to**: [body or individual]

## Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|-------------|----------|--------------------|-----------||
| [name] | (cat-N) | [element name] (cat-N) — [reason] | [specific remediation action] |

## Org Evolution Roadmap

| Trigger | Category | Threshold | Structural Response |
|---------|----------|-----------|---------------------|
| Headcount crossing 40 | headcount | 40 FTE | Introduce a second reporting layer |
| Decision velocity decline | velocity | >3 decisions per sprint deferred | Establish a decision-rights RACI |
| Delivery failure pattern | delivery | 2 consecutive missed ship gates | Appoint area leads with accountability |

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T3-PRESSURE}}
CAN-OPERATE-FLAT or STRUCTURE-WARRANTED: {{T3-VERDICT}}
```

#### 5B — Generate .roles/{area}/{role}.md files

For every role enumerated in Phase 2, generate a role file at
`.roles/{area}/{role}.md` with exactly these five fields:

```markdown
---
orientation: [engineer | designer | pm | researcher | lead | specialist]
lens: [delivery | quality | user | system | strategy | inertia]
expertise: [one-line statement of primary domain competency]
scope: [one-line statement of operating boundary — for inertia-advocate, copy verbatim from T4-IA-SCOPE-KEY template]
collaborates_with: [comma-separated list of role names]
---
```

For the inertia-advocate role:
- MUST set `lens: inertia`
- MUST copy the scope text verbatim from the T3-PRESSURE-keyed template in Phase 4B.
  FORBIDDEN: paraphrasing or adapting.
- MUST place the file at `.roles/{area}/inertia-advocate.md`

#### 5C — File layout

MUST group role files into area subdirectories under `.roles/`.
MUST create a minimum of 2 area subdirectories.
FORBIDDEN: placing all role files flat with no subdirectory structure.

### Constraints

MUST produce `org-chart.md` with an ASCII hierarchy diagram containing min 2 org levels.
MUST include `Decides` and `Escalates` columns in the Headcount by Area table.
MUST include a minimum of 3 rows in the Operating Rhythm table (ROB, shiproom, governance).
MUST include a committee charter for every governance meeting listed in the rhythm table.
Every charter MUST include Quorum expressed as `N of M` fraction.
MUST include 2+ rows in the Org Evolution Roadmap with triggers from different categories.
MUST fill all `{{placeholder}}` slots in the skeleton with values from named gate variables.
FORBIDDEN: leaving any `{{placeholder}}` unfilled.
```

---

## V-02 — Role Sequence: Assessment-Before-Enumeration

**Variation axis**: Role sequence — structural assessment precedes role enumeration
**Hypothesis**: Knowing the verdict before enumerating roles lets the model allocate role slots to pressure areas deliberately; anti-pattern categories and IA placement inform how the org is staffed, not just how it is assessed after the fact.

---

```markdown
You are executing the **org-build** skill. Generate a complete organizational design from
the provided scan results or repository path. Produce two artifacts: `org-chart.md` and
typed `.roles/{area}/{role}.md` files for every role.

## Inputs

- `SOURCE`: scan results file path or repository path (required)
- `DEPTH`: `standard` (default, 20–30 roles) or `deep` (50+ roles)

---

## Phase 1 — Intake and Depth Assessment

### Task Steps

1. Read the source. Determine whether it is scan-results output or a raw repository.
2. Assign the depth flag from the `DEPTH` input. Default to `standard` if absent.

### Constraints

MUST assign exactly one depth flag value.
FORBIDDEN: proceeding to Phase 2 before emitting the Phase 1 record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: ___    [standard | deep]
T1-SOURCE:     ___    [scan-results | repo-direct]
===
```

---

## Phase 2 — Structural Assessment

### Input Contract

FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

### Task Steps

1. From the source, evaluate structural pressure across five signals:
   span-of-control breadth, decision velocity, escalation concentration,
   accountability clarity, cross-area coordination cost.
2. Assign one FLAT-CASE-PRESSURE rating.
3. Issue exactly one verdict. Only one verdict. Both is an error. Neither is an error.

| Rating | Verdict |
|--------|---------|
| NONE, LOW | CAN-OPERATE-FLAT |
| MODERATE | CAN-OPERATE-FLAT (headcount < 40) or STRUCTURE-WARRANTED |
| HIGH, CRITICAL | STRUCTURE-WARRANTED |

4. Derive anti-pattern categories from T2-VERDICT before enumeration begins:
   - CAN-OPERATE-FLAT → required: cat-2, cat-3. FORBIDDEN: cat-1, cat-4.
   - STRUCTURE-WARRANTED → required: cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

5. Select the IA scope template from T2-PRESSURE before role enumeration:

| T2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | `Monitor org evolution triggers from the Org Evolution Roadmap. No structural intervention warranted. Flag any headcount event that crosses a documented threshold.` |
| LOW | `Track the two lowest-priority items in the Anti-Pattern Watch table. Revisit structural need at the next quarterly review. No intervention required before that checkpoint.` |
| MODERATE | `Own the Anti-Pattern Watch table as a live inertia risk register. Schedule a cross-area retrospective within 60 days. Produce an owner-assigned action list before the retrospective closes.` |
| HIGH | `Convene an org design review within 30 days. Produce a structural change proposal with named decision owners, a 90-day action plan, and a ratification checkpoint at 45 days.` |
| CRITICAL | `Initiate an emergency org redesign. FORBIDDEN: committing to any deliverable that depends on the current structure until a revised charter is ratified by the governing committee.` |

### Constraints

MUST issue exactly one FLAT-CASE-PRESSURE rating. FORBIDDEN: issuing none.
MUST issue exactly one verdict. FORBIDDEN: issuing both. FORBIDDEN: issuing neither.
MUST derive anti-pattern categories from T2-VERDICT before Phase 3.
MUST select the IA scope template verbatim from T2-PRESSURE before Phase 3.
FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:         ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT:          ___    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-ANTIPATTERN-CATS: ___    [cat-1,cat-4 | cat-2,cat-3]
T2-IA-SCOPE-KEY:     ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
===
```

---

## Phase 3 — Role Enumeration (verdict-informed)

### Input Contract

FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.
MUST read T2-VERDICT and T2-PRESSURE before assigning roles.

### Task Steps

1. Enumerate roles using T2-VERDICT to weight area staffing:
   - CAN-OPERATE-FLAT → weight coordination and clarity roles (cat-2/cat-3 pressure areas).
   - STRUCTURE-WARRANTED → weight span-control and escalation roles (cat-1/cat-4 pressure areas).
2. Apply the depth-conditional count floor:
   - T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles across min 4 areas.
   - T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles across min 6 areas.
3. MUST include the inertia-advocate role. MUST assign it the scope text from T2-IA-SCOPE-KEY,
   copied verbatim. FORBIDDEN: paraphrasing or adapting the template.

### Constraints

MUST enumerate roles within the depth-conditional count floor.
MUST include inertia-advocate. FORBIDDEN: omitting it.
FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-COUNT: ___    [integer ≥ 20]
T3-AREA-COUNT: ___    [integer ≥ 4]
T3-IA-PRESENT: ___    [yes | no]
===
```

---

## Phase 4 — Output Production

### Input Contract

FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.
MUST read T2-PRESSURE, T2-VERDICT, T2-ANTIPATTERN-CATS, T2-IA-SCOPE-KEY from
Phase 2, and T3-ROLE-COUNT, T3-AREA-COUNT from Phase 3.

### Task Steps

#### 4A — Generate org-chart.md

Produce `org-chart.md` filling every `{{placeholder}}` from named gate variables:

```markdown
# Org Chart — {{T1-SOURCE}}

## ASCII Structure Diagram
[Hierarchy with min 2 org levels]

## Structural Assessment
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
Only one verdict. Both is an error. Neither is an error.

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
...

## Anti-Pattern Watch
| Anti-Pattern | Category | Why It Applies Here | Mitigation |
[Every "Why It Applies Here" opens with `[element name] (cat-N) —`]
[Every Mitigation contains a specific remediation action]

## Org Evolution Roadmap
| Trigger | Category | Threshold | Structural Response |
[Row 1: headcount trigger. Row 2+: different category — velocity or delivery]

## Operating Rhythm
| Cadence | Meeting | Owner | Participants | Purpose |
[Min 3 rows: ROB, shiproom, governance]

## Committee Charters
[Charter per governance meeting, Quorum as N of M]
```

#### 4B — Generate .roles/{area}/{role}.md files

For every role from Phase 3, produce a role file with exactly these five fields:
`orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

For inertia-advocate:
- MUST set `lens: inertia`
- MUST copy scope text verbatim from the T2-IA-SCOPE-KEY template.
  FORBIDDEN: any deviation from the verbatim template text.

MUST group files into area subdirectories. FORBIDDEN: flat layout with no subdirectories.

### Constraints

MUST produce org-chart.md with ASCII hierarchy (min 2 org levels).
MUST include Decides and Escalates columns in Headcount by Area.
MUST include Quorum as N of M in every committee charter.
MUST fill all `{{placeholder}}` slots from named gate variables.
FORBIDDEN: leaving any `{{placeholder}}` unfilled.
```

---

## V-03 — Output Format: Table-Dominant

**Variation axis**: Output format — role files rendered as single-table rows; org-chart.md uses tabular structure throughout
**Hypothesis**: Tabular role representation reduces prose variability in the five-field check and makes field-completeness auditing mechanical; the table header enforces column presence.

---

```markdown
You are executing the **org-build** skill. Generate a complete organizational design.
Output format is table-dominant: role data appears in structured tables, not prose files.

## Inputs

- `SOURCE`: scan results file path or repository path (required)
- `DEPTH`: `standard` (default, 20–30 roles) or `deep` (50+ roles)

---

## Phase 1 — Intake

### Task Steps

1. Identify source type. Assign depth flag.

### Constraints

FORBIDDEN: proceeding to Phase 2 before emitting the Phase 1 record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: ___    [standard | deep]
T1-SOURCE:     ___    [scan-results | repo-direct]
===
```

---

## Phase 2 — Role Enumeration

### Input Contract

FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.
MUST read T1-DEPTH-FLAG to set count floor.

### Task Steps

1. Enumerate roles. Apply depth-conditional count floor:
   - T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles.
   - T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles.
2. MUST include inertia-advocate.
3. For each role, pre-populate: area, role-name, orientation, lens, expertise.
   Leave scope blank — scope is assigned in Phase 4 after structural assessment.

### Constraints

MUST include inertia-advocate. FORBIDDEN: omitting it.
FORBIDDEN: assigning IA scope in this phase. Scope is a Phase 4 output.
FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:  ___    [integer ≥ 20]
T2-AREA-COUNT:  ___    [integer ≥ 4]
T2-IA-PRESENT:  ___    [yes | no]
===
```

---

## Phase 3 — Structural Assessment

### Input Contract

FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.

### Task Steps

1. Assess structural pressure. Assign FLAT-CASE-PRESSURE rating.
2. Issue exactly one verdict. Only one verdict. Both is an error. Neither is an error.
3. Derive anti-pattern categories from verdict:
   - CAN-OPERATE-FLAT → required: cat-2, cat-3. FORBIDDEN: cat-1, cat-4.
   - STRUCTURE-WARRANTED → required: cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

### Constraints

MUST assign exactly one rating. MUST issue exactly one verdict.
FORBIDDEN: issuing both verdicts. FORBIDDEN: issuing neither.
FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-PRESSURE:         ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
T3-VERDICT:          ___    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-ANTIPATTERN-CATS: ___    [cat-1,cat-4 | cat-2,cat-3]
===
```

---

## Phase 4 — Scope Assignment and Output Production

### Input Contract

FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.
MUST read T3-PRESSURE, T3-VERDICT, T3-ANTIPATTERN-CATS from Phase 3.
MUST read T2-ROLE-COUNT, T2-AREA-COUNT from Phase 2.

### Task Steps

#### 4A — Assign IA scope (verbatim from T3-PRESSURE)

| T3-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | `Monitor org evolution triggers from the Org Evolution Roadmap. No structural intervention warranted. Flag any headcount event that crosses a documented threshold.` |
| LOW | `Track the two lowest-priority items in the Anti-Pattern Watch table. Revisit structural need at the next quarterly review. No intervention required before that checkpoint.` |
| MODERATE | `Own the Anti-Pattern Watch table as a live inertia risk register. Schedule a cross-area retrospective within 60 days. Produce an owner-assigned action list before the retrospective closes.` |
| HIGH | `Convene an org design review within 30 days. Produce a structural change proposal with named decision owners, a 90-day action plan, and a ratification checkpoint at 45 days.` |
| CRITICAL | `Initiate an emergency org redesign. FORBIDDEN: committing to any deliverable that depends on the current structure until a revised charter is ratified by the governing committee.` |

MUST copy scope text verbatim. FORBIDDEN: paraphrasing.

#### 4B — Generate org-chart.md (table-dominant format)

```markdown
# Org Chart — {{T1-SOURCE}}

## ASCII Structure Diagram
[Min 2 org levels]

## Structural Assessment
| Field | Value |
|-------|-------|
| FLAT-CASE-PRESSURE | {{T3-PRESSURE}} |
| VERDICT | {{T3-VERDICT}} |
| Guard | Only one verdict. Both is an error. Neither is an error. |

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |

## Role Registry (all roles, table format)
| Area | Role | Orientation | Lens | Expertise | Scope | Collaborates With |

## Anti-Pattern Watch
| Anti-Pattern | Category | Why It Applies Here | Mitigation |
[Opens with `[element name] (cat-N) —`. Mitigation = specific action.]

## Org Evolution Roadmap
| Trigger | Category | Threshold | Structural Response |
[Row 1: headcount. Row 2+: different category.]

## Operating Rhythm
| Cadence | Meeting | Owner | Participants | Purpose |
[3+ rows: ROB, shiproom, governance]

## Committee Charters (table format)
| Meeting | Owner | Quorum | Frequency | Scope | Escalates To |
[Quorum as N of M]
```

#### 4C — Generate .roles/{area}/{role}.md files

For every role in the Role Registry table, write a role file at
`.roles/{area}/{role}.md`. Use this table-format template:

```markdown
| Field | Value |
|-------|-------|
| orientation | [value] |
| lens | [value] |
| expertise | [value] |
| scope | [value — for inertia-advocate: verbatim from T3-PRESSURE template] |
| collaborates_with | [value] |
```

MUST produce one file per role. MUST group files into area subdirectories.
FORBIDDEN: flat file layout.

### Constraints

MUST assign IA scope verbatim from T3-PRESSURE template. FORBIDDEN: any deviation.
MUST include all five role fields in every role file. FORBIDDEN: omitting any field.
MUST fill all `{{placeholder}}` slots in org-chart.md from named gate variables.
MUST include Decides and Escalates in the Headcount by Area table.
MUST include Quorum as N of M in the committee charters table.
```

---

## V-04 — Lifecycle Emphasis: Expanded Phase Boundaries

**Variation axis**: Lifecycle emphasis — each phase boundary carries expanded transition commentary; double-guard stated twice per boundary in separate structural forms
**Hypothesis**: Verbose boundary guards reduce phase-skipping; restating the guard as both a record-block field and a consuming-phase preamble creates two independent catch points.

---

```markdown
You are executing the **org-build** skill. This prompt is phase-gated. Each phase
produces a named record block. FORBIDDEN: executing any phase before the prior
phase's record block is emitted and verified. This rule applies at every boundary.

## Inputs

- `SOURCE`: scan results file path or repository path (required)
- `DEPTH`: `standard` (20–30 roles) or `deep` (50+ roles)

---

## PHASE 1 — Intake and Depth Flag Assignment

### Task Steps

1. Identify source type from the `SOURCE` input.
2. Determine depth flag from `DEPTH`. Default to `standard` if absent.
3. Emit the Phase 1 record block. FORBIDDEN: continuing until it is emitted.

### Constraints

MUST emit the Phase 1 record block before any Phase 2 work begins.
FORBIDDEN: beginning Phase 2 before this record block appears in output.

### Phase 1 → Phase 2 Gate

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: ___    [standard | deep]
T1-SOURCE:     ___    [scan-results | repo-direct]
===
```

**Boundary check before Phase 2:** Confirm both T1 fields are filled. If either is blank,
FORBIDDEN: advancing. Resolve the missing field before crossing the gate.

---

## PHASE 2 — Role Enumeration

**Phase 2 Entry Guard** (inbound — mirrors the outbound guard above):
FORBIDDEN: executing Phase 2 content before the Phase 1 record block above is emitted.

### Input Contract

- T1-DEPTH-FLAG (from Phase 1 record block)    [standard | deep]
- T1-SOURCE (from Phase 1 record block)        [scan-results | repo-direct]

### Task Steps

1. Read T1-DEPTH-FLAG. Apply count floor:
   - T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles across min 4 areas.
   - T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles across min 6 areas.
2. Include the inertia-advocate role. MUST set `lens: inertia` for this role.
3. Produce a role list as `area/role-name` pairs.

### Constraints

MUST enumerate roles within the depth-conditional bounds.
MUST include inertia-advocate. FORBIDDEN: omitting it.
FORBIDDEN: beginning Phase 3 before this record block is emitted.

### Phase 2 → Phase 3 Gate

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-ROLE-COUNT:  ___    [integer ≥ 20]
T2-AREA-COUNT:  ___    [integer ≥ 4]
T2-IA-PRESENT:  ___    [yes | no]
===
```

**Boundary check before Phase 3:** Confirm T2-ROLE-COUNT is within the T1-DEPTH-FLAG
floor. Confirm T2-IA-PRESENT = yes. If either check fails, FORBIDDEN: advancing.

---

## PHASE 3 — Structural Assessment

**Phase 3 Entry Guard** (inbound):
FORBIDDEN: executing Phase 3 content before the Phase 2 record block above is emitted.

### Input Contract

- T2-ROLE-COUNT (from Phase 2 record block)    [integer ≥ 20]
- T2-AREA-COUNT (from Phase 2 record block)    [integer ≥ 4]

### Task Steps

1. Evaluate five structural pressure signals:
   - span-of-control breadth
   - decision velocity
   - escalation concentration
   - accountability clarity
   - cross-area coordination cost
2. Assign a FLAT-CASE-PRESSURE rating from the closed set.
3. Issue exactly one verdict. Only one verdict. Both is an error. Neither is an error.
4. Derive anti-pattern categories:
   - CAN-OPERATE-FLAT → required: cat-2, cat-3. FORBIDDEN: cat-1, cat-4.
   - STRUCTURE-WARRANTED → required: cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

**Category definitions:**
- cat-1: Span-of-control excess
- cat-2: Cross-area coordination loss
- cat-3: Accountability diffusion
- cat-4: Escalation bottleneck

### Constraints

MUST assign exactly one FLAT-CASE-PRESSURE rating.
MUST issue exactly one verdict. FORBIDDEN: issuing both. FORBIDDEN: issuing neither.
MUST include cat-N derivation. FORBIDDEN: using forbidden category set for the verdict path.
FORBIDDEN: beginning Phase 4 before this record block is emitted.

### Phase 3 → Phase 4 Gate

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-PRESSURE:         ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
T3-VERDICT:          ___    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T3-ANTIPATTERN-CATS: ___    [cat-1,cat-4 | cat-2,cat-3]
===
```

**Boundary check before Phase 4:** Confirm the T3-ANTIPATTERN-CATS value is consistent
with the T3-VERDICT path. Inconsistency is a constraint violation — FORBIDDEN: advancing.

---

## PHASE 4 — IA Scope and Anti-Pattern Derivation

**Phase 4 Entry Guard** (inbound):
FORBIDDEN: executing Phase 4 content before the Phase 3 record block above is emitted.

### Input Contract

- T3-PRESSURE (from Phase 3 record block)          [NONE | LOW | MODERATE | HIGH | CRITICAL]
- T3-VERDICT (from Phase 3 record block)           [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
- T3-ANTIPATTERN-CATS (from Phase 3 record block)  [cat-1,cat-4 | cat-2,cat-3]

### Task Steps

1. Select IA scope text verbatim from the T3-PRESSURE key:

| T3-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | `Monitor org evolution triggers from the Org Evolution Roadmap. No structural intervention warranted. Flag any headcount event that crosses a documented threshold.` |
| LOW | `Track the two lowest-priority items in the Anti-Pattern Watch table. Revisit structural need at the next quarterly review. No intervention required before that checkpoint.` |
| MODERATE | `Own the Anti-Pattern Watch table as a live inertia risk register. Schedule a cross-area retrospective within 60 days. Produce an owner-assigned action list before the retrospective closes.` |
| HIGH | `Convene an org design review within 30 days. Produce a structural change proposal with named decision owners, a 90-day action plan, and a ratification checkpoint at 45 days.` |
| CRITICAL | `Initiate an emergency org redesign. FORBIDDEN: committing to any deliverable that depends on the current structure until a revised charter is ratified by the governing committee.` |

2. Construct the Anti-Pattern Watch table using only the required categories.
   Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
   Every Mitigation cell MUST contain a specific remediation action.
   FORBIDDEN: format guidance in Mitigation cells.

### Constraints

MUST copy IA scope verbatim. FORBIDDEN: paraphrasing or composing.
MUST use only the required anti-pattern categories for the T3-VERDICT path.
FORBIDDEN: using anti-pattern categories from the forbidden set.
FORBIDDEN: beginning Phase 5 before this record block is emitted.

### Phase 4 → Phase 5 Gate

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-IA-SCOPE-KEY:     ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
T4-ANTIPATTERN-CATS: ___    [cat-1,cat-4 | cat-2,cat-3]
===
```

**Boundary check before Phase 5:** Confirm T4-IA-SCOPE-KEY = T3-PRESSURE.
Confirm T4-ANTIPATTERN-CATS = T3-ANTIPATTERN-CATS. Any mismatch is a constraint
violation — FORBIDDEN: advancing.

---

## PHASE 5 — Output Production

**Phase 5 Entry Guard** (inbound):
FORBIDDEN: executing Phase 5 content before the Phase 4 record block above is emitted.

### Input Contract

- T1-SOURCE (Phase 1)       [scan-results | repo-direct]
- T1-DEPTH-FLAG (Phase 1)   [standard | deep]
- T3-PRESSURE (Phase 3)     [NONE | LOW | MODERATE | HIGH | CRITICAL]
- T3-VERDICT (Phase 3)      [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
- T4-IA-SCOPE-KEY (Phase 4) [NONE | LOW | MODERATE | HIGH | CRITICAL]
- T4-ANTIPATTERN-CATS (Phase 4) [cat-1,cat-4 | cat-2,cat-3]

### Task Steps

1. Generate `org-chart.md` filling all `{{placeholder}}` slots:

```markdown
# Org Chart — {{T1-SOURCE}}
## ASCII Diagram [min 2 org levels]
## Structural Assessment
FLAT-CASE-PRESSURE: {{T3-PRESSURE}}
VERDICT: {{T3-VERDICT}}
Only one verdict. Both is an error. Neither is an error.
## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
## Anti-Pattern Watch [from Phase 4]
## Org Evolution Roadmap
| Trigger | Category | Threshold | Structural Response |
[Row 1: headcount. Row 2+: different category.]
## Operating Rhythm [3+ rows: ROB, shiproom, governance]
## Committee Charters [quorum as N of M per charter]
```

2. Generate `.roles/{area}/{role}.md` for every enumerated role.
   Every file MUST contain: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.
   For inertia-advocate: scope MUST be the verbatim T4-IA-SCOPE-KEY template text.

3. MUST group role files into area subdirectories (min 2).

### Constraints

MUST produce org-chart.md with ASCII hierarchy (min 2 org levels).
MUST include Decides and Escalates in the Headcount by Area table.
MUST include Quorum as N of M in every committee charter.
MUST fill all `{{placeholder}}` slots. FORBIDDEN: leaving any unfilled.
FORBIDDEN: flat role file layout with no area subdirectories.
```

---

## V-05 — Inertia-First Framing + Direct Register

**Variation axis**: Combination — inertia-advocate as organizing lens throughout; more direct phrasing register (shorter sentences, tighter imperatives), same MUST/FORBIDDEN discipline
**Hypothesis**: Opening with the inertia question and keeping it visible through every phase produces a structurally grounded IA scope and cleaner anti-pattern derivation; the directness reduces hedging tokens that dilute constraint strength.

---

```markdown
You are executing **org-build**. The central question of this skill is:
**Does this org need more structure, or can it operate flat?**
Every phase builds toward answering that question. The inertia-advocate role
captures the answer and carries it into every future org decision.

## Inputs

- `SOURCE`: scan results or repository path (required)
- `DEPTH`: `standard` (20–30 roles) or `deep` (50+ roles)

---

## Phase 1 — Source and Depth

### Task Steps

1. Read the source. Determine its type.
2. Assign the depth flag. Default: `standard`.

### Constraints

FORBIDDEN: proceeding to Phase 2 before emitting this record block.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG: ___    [standard | deep]
T1-SOURCE:     ___    [scan-results | repo-direct]
===
```

---

## Phase 2 — The Inertia Question: Structural Assessment

### Input Contract

FORBIDDEN: executing Phase 2 before the Phase 1 record block is emitted.

### Task Steps

The inertia question has three parts. Answer each one in sequence.

**Part A — FLAT-CASE-PRESSURE rating.**
Evaluate these five signals. Rate the pressure:
- span-of-control breadth
- decision velocity
- escalation concentration
- accountability clarity
- cross-area coordination cost

Rating scale: NONE → LOW → MODERATE → HIGH → CRITICAL.
Assign exactly one.

**Part B — Verdict.**
Issue exactly one verdict.
Only one verdict. Both is an error. Neither is an error.

| Pressure | Verdict |
|----------|---------|
| NONE, LOW | CAN-OPERATE-FLAT |
| MODERATE | CAN-OPERATE-FLAT or STRUCTURE-WARRANTED (headcount dependent) |
| HIGH, CRITICAL | STRUCTURE-WARRANTED |

**Part C — Anti-pattern categories from the verdict.**
The verdict determines which anti-patterns are structurally possible.

| Verdict | Required categories | FORBIDDEN categories |
|---------|--------------------|--------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

Categories:
- cat-1: Span-of-control excess
- cat-2: Cross-area coordination loss
- cat-3: Accountability diffusion
- cat-4: Escalation bottleneck

**Part D — IA scope template (selected from pressure).**
The inertia-advocate's scope is determined by the pressure rating, not composed.
Select the verbatim text from the table below. Copy it. Do not write new text.

| T2-PRESSURE | Verbatim scope |
|-------------|----------------|
| NONE | `Monitor org evolution triggers from the Org Evolution Roadmap. No structural intervention warranted. Flag any headcount event that crosses a documented threshold.` |
| LOW | `Track the two lowest-priority items in the Anti-Pattern Watch table. Revisit structural need at the next quarterly review. No intervention required before that checkpoint.` |
| MODERATE | `Own the Anti-Pattern Watch table as a live inertia risk register. Schedule a cross-area retrospective within 60 days. Produce an owner-assigned action list before the retrospective closes.` |
| HIGH | `Convene an org design review within 30 days. Produce a structural change proposal with named decision owners, a 90-day action plan, and a ratification checkpoint at 45 days.` |
| CRITICAL | `Initiate an emergency org redesign. FORBIDDEN: committing to any deliverable that depends on the current structure until a revised charter is ratified by the governing committee.` |

### Constraints

MUST assign exactly one pressure rating.
MUST issue exactly one verdict. FORBIDDEN: issuing both. FORBIDDEN: issuing neither.
MUST derive anti-pattern categories from the verdict. FORBIDDEN: using the wrong category set.
MUST record the IA scope key before Phase 3.
FORBIDDEN: beginning Phase 3 before this record block is emitted.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:         ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
T2-VERDICT:          ___    [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-ANTIPATTERN-CATS: ___    [cat-1,cat-4 | cat-2,cat-3]
T2-IA-SCOPE-KEY:     ___    [NONE | LOW | MODERATE | HIGH | CRITICAL]
===
```

---

## Phase 3 — Role Enumeration

### Input Contract

FORBIDDEN: executing Phase 3 before the Phase 2 record block is emitted.
MUST read T1-DEPTH-FLAG from Phase 1 and T2-VERDICT from Phase 2.

### Task Steps

1. Enumerate roles. The verdict from Phase 2 guides staffing emphasis.
   CAN-OPERATE-FLAT → weight coordination, clarity, cross-area liaison roles.
   STRUCTURE-WARRANTED → weight span-control, escalation path, decision-rights roles.

2. Apply depth-conditional count floor:
   - T1-DEPTH-FLAG = `standard` → MUST enumerate 20–30 roles across min 4 areas.
   - T1-DEPTH-FLAG = `deep` → MUST enumerate 50+ roles across min 6 areas.

3. MUST include the inertia-advocate.
   - `lens`: inertia
   - `scope`: copy verbatim from T2-IA-SCOPE-KEY template. FORBIDDEN: paraphrasing.
   - Place at `.roles/{primary-area}/inertia-advocate.md`

### Constraints

MUST include inertia-advocate with verbatim scope. FORBIDDEN: omitting it.
MUST stay within depth-conditional count bounds.
FORBIDDEN: beginning Phase 4 before this record block is emitted.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-ROLE-COUNT: ___    [integer ≥ 20]
T3-AREA-COUNT: ___    [integer ≥ 4]
T3-IA-PRESENT: ___    [yes | no]
===
```

---

## Phase 4 — Output Production

### Input Contract

FORBIDDEN: executing Phase 4 before the Phase 3 record block is emitted.
MUST read: T1-SOURCE (P1), T2-PRESSURE (P2), T2-VERDICT (P2),
T2-ANTIPATTERN-CATS (P2), T2-IA-SCOPE-KEY (P2), T3-ROLE-COUNT (P3).

### Task Steps

#### 4A — org-chart.md

The org-chart answers the inertia question at a glance. Structure it accordingly.

```markdown
# Org Chart — {{T1-SOURCE}}

## The Inertia Question
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
Only one verdict. Both is an error. Neither is an error.

## ASCII Structure Diagram
[Min 2 org levels — layout reflects the verdict]

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |

## Anti-Pattern Watch
| Anti-Pattern | Category | Why It Applies Here | Mitigation |
[Every Why cell: `[element name] (cat-N) —`. Every Mitigation: specific action.]
[Use only T2-ANTIPATTERN-CATS categories. FORBIDDEN: categories from forbidden set.]

## Org Evolution Roadmap
| Trigger | Category | Threshold | Structural Response |
[Row 1: headcount. Row 2: velocity or delivery (different category).]

## Operating Rhythm
| Cadence | Meeting | Owner | Participants | Purpose |
[Min 3 rows: ROB, shiproom, quarterly governance]

## Committee Charters
[One charter per governance meeting. Quorum as N of M.]
```

#### 4B — Role files

Generate `.roles/{area}/{role}.md` for every enumerated role.

Every file: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`.

For inertia-advocate:
- `lens: inertia`
- `scope`: verbatim from T2-IA-SCOPE-KEY. This is not a summary. It is a copy.
  FORBIDDEN: any rewriting, shortening, or adaptation.

Group files into area subdirectories. FORBIDDEN: flat file layout.

### Constraints

MUST produce org-chart.md with ASCII hierarchy (min 2 org levels).
MUST include Decides and Escalates in Headcount by Area.
MUST include Quorum as N of M per committee charter.
MUST fill all `{{placeholder}}` slots from named gate variables.
FORBIDDEN: any placeholder left unfilled.
MUST copy inertia-advocate scope verbatim. FORBIDDEN: deviation.
```
