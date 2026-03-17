# /quest:variate — org-chart Round 8 (v8 rubric)

Five complete variations. Three single-axis, two combined. Targeting the v8 additions: **C-27** (gate-local DO/DO NOT register) and **C-28** (step-embedded default-position instruction).

---

## V-01 — Axis: Step-Embedded Default-Position (C-28)

**Hypothesis**: An explicit `STEP 1a` inside GATE 1 Sub-section 1 — imperative, verbatim, with a prohibition on placement outside that step — ensures the model encounters the default-position directive during GATE 1 execution, not only at authoring time. Modal language is distributed prose throughout; no gate-local DO/DO NOT registers (isolates C-28 from C-27).

---

Generate an org structure for the product or domain provided. Read `.craft/roles/` for role grounding. Output: `org-chart.md` containing ASCII org diagram, headcount by area, committee charters, and operating rhythm table.

**INERTIA FIRST.** The prior is flat. Structure must earn its place. No section of this artifact is produced unless the inertia assessment verdict requires it.

**GATE CHAIN CONTRACT.** Gates execute in strictly ascending order: GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the subsequent gate. Gates must not be invoked out of order.

---

### GATE 0 — Roles + Classification

**Sub-section 0.1: Load Roles**

Read every file in `.craft/roles/`. Under the heading `ROLES-LOADED`, list every role name found.

If `.craft/roles/` is absent or empty, emit:

> `ROLES-NOTE: No .craft/roles/ directory found. Role names inferred from context.`

Every role name used in any subsequent section must appear in the `ROLES-LOADED` list. Introducing a role name after this block is not acceptable.

**Sub-section 0.2: Role-Type Classification**

Immediately after the `ROLES-LOADED` list — with no intervening structural content of any kind — produce the `ROLE-TYPE-CLASSIFICATION` block. Assign every role to exactly one type from the closed set: `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`.

Definitions:
- `DECISION` — holds outcome accountability, budget, or headcount authority
- `EXECUTION` — builds or delivers within defined scope
- `ADVISORY` — provides expertise on request; no unilateral authority
- `GOVERNANCE` — enforces standards, approves exceptions, sets policy

Output order: DECISION roles first, then EXECUTION, then ADVISORY and GOVERNANCE.

```
GATE 0 STATUS: [ ] ROLES-LOADED (or ROLES-NOTE) present
               [ ] Every role has a type assignment
               [ ] No inertia rows, diagram nodes, headcount entries, or rhythm rows appear before this line
               STATUS: PASS / FAIL
```

**GATE 0 PRODUCES:** `typed-role-list` — all role names with type assignments.

---

### GATE 1 — Inertia Assessment

**GATE 1 REQUIRES:** `typed-role-list` from GATE 0.

**Sub-section 1.1: Default-Position Statement**

**STEP 1a.** Write the following statement verbatim as the first content of this sub-section, before any other content in GATE 1:

> `DEFAULT POSITION: The team can operate flat. Structure must earn its place. Every element of formal org proposed in this artifact must demonstrate that flat operation cannot achieve the same outcome.`

This is an executable step instruction, not a scene-setter. Do not paraphrase. Do not place this statement in the artifact preamble, in a header before GATE 1, or in any location outside GATE 1 Sub-section 1.1. Write it here, at this step, before proceeding to Sub-section 1.2.

**STEP 1b.** Proceed to the mechanism table.

**Sub-section 1.2: Mechanism Table**

Produce a mechanism table covering coordination and accountability mechanisms that flat operation would require.

Columns: `Mechanism | Type | Evidence | Flat-Operation Risk`

- Minimum 2 rows required.
- `Type` must be drawn from the closed set: `{COORDINATION, ACCOUNTABILITY, QUALITY-GATE, KNOWLEDGE-TRANSFER, ESCALATION-PATH}`.

Example row (not counted toward minimum):
```
| Quarterly roadmap sync | COORDINATION | 3 teams share schedule dependencies | Without owner, dependencies slip silently |
```

**Sub-section 1.3: FLAT-CASE-PRESSURE Rating**

Rate the structural pressure from the closed set: `{NONE, LOW, MODERATE, HIGH, CRITICAL}`.

Provide exactly one sentence justifying the rating.

**Sub-section 1.4: VERDICT**

State exactly one of: `PROCEED-TO-STRUCTURE` | `STAY-FLAT`

If `STAY-FLAT`:
- Emit ABSENT labels for all downstream sections: `ASCII Diagram — ABSENT`, `Headcount Table — ABSENT`, `Operating Rhythm Table — ABSENT`, `Committee Charters — ABSENT`.
- Simplified or compact versions of any absent section are not acceptable.
- Write: `STOP — ARTIFACT COMPLETE`. No content follows this line.

If `PROCEED-TO-STRUCTURE`: State the concrete re-assessment trigger — a specific headcount threshold, product milestone, or failure mode that would invalidate this verdict.

**CHECKPOINT INERTIA-CHECK:** Confirm that all 4 sub-sections are present and VERDICT is emitted before proceeding to GATE 1 STATUS.

```
GATE 1 STATUS: [ ] All 4 sub-sections present
               [ ] Default-position statement appears as first content of Sub-section 1.1
               [ ] Mechanism table has >= 2 rows with closed-set Types
               [ ] FLAT-CASE-PRESSURE rating from closed set
               [ ] VERDICT emitted
               STATUS: PASS / FAIL
```

**GATE 1 PRODUCES:** `inertia-verdict` (PROCEED-TO-STRUCTURE or STAY-FLAT), `flat-case-pressure-rating`.

Diagram nodes, headcount area rows, rhythm cadence rows, and committee charter fields must not appear before GATE 1 STATUS reads PASS.

---

### GATE 2 — Structure: Diagram + Headcount

**GATE 2 REQUIRES:** `typed-role-list` from GATE 0 + `inertia-verdict` (PROCEED-TO-STRUCTURE) from GATE 1.

**Sub-section 2.1: ASCII Org Diagram**

Produce an ASCII org diagram.

Requirements:
- Minimum 2 hierarchy levels required.
- Committees must appear as distinct nodes, not merged into reporting lines.
- All role names must come from `ROLES-LOADED`; introducing a role name not in that block is not acceptable.
- Node format:

```
+----------------------+
| Role Name            |
| (TYPE)               |
+----------------------+
```

Reporting lines use `|` and `---`.

**Sub-section 2.2: Headcount by Area**

Columns: `Area | HC | Decides | Escalates | Key Roles`

- Minimum 2 areas plus a `Total` row required.
- `Decides` and `Escalates` must be separate columns; merged columns are not acceptable.
- `Key Roles` annotated with `(domain type)`.

Example row (not counted toward minimum):
```
| Platform Engineering | 6 | 2 | 4 | Platform Lead (technical), Reliability Eng (execution) |
```

**CHECKPOINT DIAGRAM-CHECK:** Confirm ASCII diagram has ≥2 hierarchy levels and all role names are drawn from the roles block.

```
GATE 2 STATUS: [ ] ASCII diagram has >= 2 hierarchy levels
               [ ] Committees appear as distinct nodes
               [ ] All role names from ROLES-LOADED block
               [ ] Headcount table has >= 2 areas plus Total row
               [ ] Decides and Escalates are separate columns
               STATUS: PASS / FAIL
```

**GATE 2 PRODUCES:** `org-diagram`, `headcount-table`.

Rhythm rows and committee charters must not appear before GATE 2 STATUS reads PASS.

---

### GATE 3 — Operating Rhythm + Committee Charters

**GATE 3 REQUIRES:** `org-diagram` + `headcount-table` from GATE 2.

**INTERLEAVE REQUIREMENT:** Produce rhythm rows and committee charters in interleaved pairs: rhythm row 1, then its charter; rhythm row 2, then its charter. Batching all rhythm rows before all charters is not acceptable.

**Operating Rhythm Table**

Columns: `Cadence | Name | Owner | Purpose | Attendees | Output`

Minimum 3 rows covering:
- Row 1: ROB (Review of the Business) — weekly or bi-weekly business rhythm
- Row 2: shiproom or gate review
- Row 3: governance or architecture board

Merged rows are not acceptable.

Example row (not counted toward minimum):
```
| Weekly | Eng Shiproom | VP Engineering | Review shipping blockers | Leads, PM | Blockers list |
```

**Committee Charters**

For each committee in the rhythm table, produce a charter with all 5 required fields:
1. `Name`
2. `Mission` — one sentence
3. `Membership` — minimum 2 roles, each annotated with `(TYPE)` from the classification block
4. `Quorum` — expressed as `N of M member roles`
5. `Escalates` — names a specific destination role or governance body

Example charter (not counted toward minimum):
```
Name: Architecture Board
Mission: Approve cross-team technical standards and review design decisions with systemic impact.
Membership: Principal Architect (GOVERNANCE), VP Engineering (DECISION), Staff Engineer (ADVISORY)
Quorum: 2 of 3 member roles
Escalates: CTO
```

**CHECKPOINT PAIR-COUNT-CHECK:** After producing all rhythm-charter pairs, count: pairs produced must equal governance rows in the rhythm table. If the counts do not match, the gate cannot pass.

```
GATE 3 STATUS: [ ] Rhythm table has >= 3 distinct rows
               [ ] Rows cover ROB cadence, shiproom/gate review, governance/architecture board
               [ ] Each committee has a charter with all 5 fields
               [ ] Quorum in "N of M member roles" form
               [ ] Escalates names a specific destination
               [ ] Pair count matches rhythm row count
               STATUS: PASS / FAIL
```

**GATE 3 PRODUCES:** `rhythm-charter-pairs`, `complete-artifact`.

---

### ORG-ELEMENT REGISTER

List all structural elements used, categorized:
- `cat-1`: Reporting relationships
- `cat-2`: Committees and boards
- `cat-3`: Operating rhythms
- `cat-4`: Role-type overlays

Anti-Pattern Watch: Cite each element's category as `(cat-N)`. Flag any element risking a known anti-pattern (committee proliferation, unclear escalation path, span-of-control breach, silent hierarchy).

---

### Org Evolution Roadmap

Columns: `Trigger | Proposed Change | Risk If Ignored`

Minimum 2 rows from distinct trigger categories. No two rows may share the same trigger category (e.g., two headcount thresholds count as one category).

---

`ARTIFACT-END`

---

## V-02 — Axis: Gate-Local DO/DO NOT Registers (C-27)

**Hypothesis**: Placing a structured `DO / DO NOT` register as an explicit section within each gate — listing specific permitted and prohibited operations in parallel columns — makes each gate's compliance contract locally complete. A model executing a gate can verify all constraints without scanning surrounding prose. Default-position declaration is in the artifact preamble only (not step-embedded), isolating C-27 from C-28; this variation earns C-14 via the registers, PARTIAL on C-13, and does not satisfy C-28.

---

Generate an org structure for the product or domain provided. Read `.craft/roles/` for role grounding. Output: `org-chart.md` with ASCII org diagram, headcount by area, committee charters, and operating rhythm table.

**DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.** Structure must earn its place. This artifact produces structural content only if the inertia assessment verdict requires it.

**GATE SEQUENCE:** GATE 0 → GATE 1 → GATE 2 → GATE 3. Each gate's outputs are required inputs for the subsequent gate.

---

### GATE 0 — Roles + Classification

**DO / DO NOT — GATE 0**

| DO | DO NOT |
|----|--------|
| Read every file in `.craft/roles/` | Introduce role names not found in `.craft/roles/` |
| Emit `ROLES-LOADED` with all role names, or `ROLES-NOTE` if absent | Emit inertia rows before GATE 0 STATUS |
| Assign every role a type from `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` | Emit diagram nodes before GATE 0 STATUS |
| Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED with no intervening content | Emit headcount entries before GATE 0 STATUS |
| Output DECISION roles first, then EXECUTION, then ADVISORY/GOVERNANCE | Emit rhythm rows before GATE 0 STATUS |

**Sub-section 0.1: Load Roles**

Emit `ROLES-LOADED:` followed by all role names from `.craft/roles/`. If the directory is absent or empty: `ROLES-NOTE: No .craft/roles/ directory found. Role names inferred from context.`

**Sub-section 0.2: Role-Type Classification**

Immediately after Sub-section 0.1 — no intervening content — produce `ROLE-TYPE-CLASSIFICATION:`. Assign each role to one type from: `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`. Output in three-tier order: DECISION, EXECUTION, ADVISORY/GOVERNANCE.

```
GATE 0 STATUS: PASS when ROLES-LOADED (or ROLES-NOTE) present AND every role has a type assignment.
```

---

### GATE 1 — Inertia Assessment

**GATE 1 REQUIRES:** typed-role-list from GATE 0.

**DO / DO NOT — GATE 1**

| DO | DO NOT |
|----|--------|
| Open Sub-section 1.1 with the default-position declaration | Emit diagram nodes before GATE 1 STATUS |
| Produce all 4 sub-sections in order | Emit headcount area rows before GATE 1 STATUS |
| Use only closed-set Types in the mechanism table | Emit rhythm rows before GATE 1 STATUS |
| Choose FLAT-CASE-PRESSURE rating from `{NONE, LOW, MODERATE, HIGH, CRITICAL}` | Emit committee charter fields before GATE 1 STATUS |
| If STAY-FLAT: emit ABSENT labels for all downstream sections, then STOP | Skip any of the 4 sub-sections |
| If PROCEED-TO-STRUCTURE: state a concrete re-assessment trigger | State a vague or hypothetical re-assessment trigger |

**Sub-section 1.1: Default-Position Statement**

Open with:

> `DEFAULT POSITION: The team can operate flat. Structure must earn its place. Every element of formal org proposed below must demonstrate that flat operation cannot achieve the same outcome.`

**Sub-section 1.2: Mechanism Table**

Columns: `Mechanism | Type | Evidence | Flat-Operation Risk`

Minimum 2 rows. `Type` from closed set: `{COORDINATION, ACCOUNTABILITY, QUALITY-GATE, KNOWLEDGE-TRANSFER, ESCALATION-PATH}`.

Example row (not counted):
```
| Release cadence alignment | COORDINATION | 4 teams ship to shared endpoint | Without owner, release conflicts go undetected |
```

**Sub-section 1.3: FLAT-CASE-PRESSURE Rating**

One of: `{NONE, LOW, MODERATE, HIGH, CRITICAL}`. One sentence justification.

**Sub-section 1.4: VERDICT**

`PROCEED-TO-STRUCTURE` or `STAY-FLAT`.

If `STAY-FLAT`: emit ABSENT labels for each downstream section. Simplified or compact alternatives are not acceptable. Write `STOP — ARTIFACT COMPLETE`. No content follows.

If `PROCEED-TO-STRUCTURE`: state the concrete re-assessment trigger.

```
GATE 1 STATUS: PASS when all 4 sub-sections present, VERDICT emitted, and no downstream structural content precedes this line.
```

---

### GATE 2 — Structure: Diagram + Headcount

**GATE 2 REQUIRES:** typed-role-list from GATE 0 + inertia-verdict (PROCEED-TO-STRUCTURE) from GATE 1.

**DO / DO NOT — GATE 2**

| DO | DO NOT |
|----|--------|
| Use only role names from ROLES-LOADED in the diagram | Introduce role names not in ROLES-LOADED |
| Render committees as distinct diagram nodes | Merge committees into reporting lines |
| Produce Decides and Escalates as separate headcount columns | Merge Decides and Escalates into a single column |
| Annotate Key Roles with `(domain type)` | Omit domain-type annotations from Key Roles |
| Include at least 2 hierarchy levels in the diagram | Produce a single-level (flat) diagram |
| Include a Total row in the headcount table | Omit the Total row |
| Emit rhythm rows and charters only after GATE 2 STATUS | Emit rhythm rows or charters before GATE 2 STATUS |

**Sub-section 2.1: ASCII Org Diagram**

Node format:
```
+----------------------+
| Role Name            |
| (TYPE)               |
+----------------------+
```

Minimum 2 hierarchy levels. Committees as distinct nodes. All role names from ROLES-LOADED.

**Sub-section 2.2: Headcount by Area**

Columns: `Area | HC | Decides | Escalates | Key Roles`

Minimum 2 areas plus Total row. Key Roles annotated with `(domain type)`.

Example row (not counted):
```
| Growth | 4 | 1 | 3 | Growth Lead (product), Analyst (data) |
```

```
GATE 2 STATUS: PASS when diagram has >= 2 hierarchy levels and headcount table has >= 2 areas plus Total row.
```

---

### GATE 3 — Operating Rhythm + Committee Charters

**GATE 3 REQUIRES:** org-diagram + headcount-table from GATE 2.

**DO / DO NOT — GATE 3**

| DO | DO NOT |
|----|--------|
| Produce rhythm rows and charters in interleaved pairs (row → charter → row → charter) | Batch all rhythm rows before all charters |
| Include at minimum an ROB row, a shiproom/gate row, and a governance/architecture row | Omit any of the three required row types |
| Include all 5 charter fields for every committee | Omit any charter field |
| Express Quorum as `N of M member roles` | Express Quorum as a percentage or headcount only |
| Name a specific Escalates destination | Use vague Escalates targets ("leadership", "management") |
| Verify pair count equals rhythm row count before emitting GATE 3 STATUS | Skip pair-count verification |
| List minimum 2 annotated roles in each committee's Membership | List fewer than 2 roles in Membership |

**Operating Rhythm Table**

Columns: `Cadence | Name | Owner | Purpose | Attendees | Output`

Minimum 3 distinct rows: ROB cadence + shiproom/gate review + governance/architecture board.

**Committee Charters** (interleaved)

Per committee, all 5 fields: Name, Mission (one sentence), Membership (≥2 annotated roles), Quorum (`N of M member roles`), Escalates (specific destination).

**CHECKPOINT PAIR-COUNT-CHECK:** Pairs produced must equal governance rows in the rhythm table. If counts differ, correct before emitting GATE 3 STATUS.

```
GATE 3 STATUS: PASS when rhythm table has >= 3 rows, all charters have 5 fields, and pair count matches rhythm row count.
```

---

### ORG-ELEMENT REGISTER

Categorize all structural elements used:
- `cat-1`: Reporting relationships
- `cat-2`: Committees and boards
- `cat-3`: Operating rhythms
- `cat-4`: Role-type overlays

Anti-Pattern Watch: Cite `(cat-N)` for each element. Flag committee proliferation, unclear escalation, span-of-control breach, silent hierarchy.

---

### Org Evolution Roadmap

Columns: `Trigger | Proposed Change | Risk If Ignored`

Minimum 2 rows from distinct trigger categories.

---

`ARTIFACT-END`

---

## V-03 — Axis: Named Artifact Handoff at Each Gate Interface (C-25)

**Hypothesis**: Declaring named `INPUT:` and `OUTPUT:` artifacts at every gate boundary — rather than a chain-level dependency assertion — forces per-gate I/O contracts that a model can verify locally. Modal language is distributed prose. No gate-local DO/DO NOT registers. Default position is in preamble only (isolates C-25; does not satisfy C-27 or C-28).

---

Generate an org structure for the product or domain provided. Read `.craft/roles/` for role grounding. Output: `org-chart.md` with ASCII org diagram, headcount by area, committee charters, and operating rhythm table.

**DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.** Formal structure must earn its place. This artifact produces structural content only if the inertia assessment verdict requires it.

**GATE SEQUENCE:** GATE 0 → GATE 1 → GATE 2 → GATE 3. Each gate must not begin until its required inputs are available from the prior gate's named outputs.

---

### GATE 0 — Roles + Classification

**GATE 0 INPUT:** Domain name or context (provided by caller). No prior gate outputs required.

**Sub-section 0.1: Load Roles**

Read all files in `.craft/roles/`. Emit `ROLES-LOADED:` with every role name found.

If `.craft/roles/` is absent or empty: `ROLES-NOTE: No .craft/roles/ directory found. Role names inferred from context.`

Every role name used in subsequent sections must appear in this list. Introducing role names after this block is not acceptable.

**Sub-section 0.2: Role-Type Classification**

Immediately after Sub-section 0.1 — no intervening structural content — produce `ROLE-TYPE-CLASSIFICATION:`. Assign every role to exactly one type from: `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`. Output order: DECISION, then EXECUTION, then ADVISORY and GOVERNANCE.

The following content must not appear before GATE 0 STATUS reads PASS: inertia rows, diagram nodes, headcount entries, rhythm rows, committee charters.

```
GATE 0 STATUS: PASS when ROLES-LOADED (or ROLES-NOTE) present AND every role has a type assignment.
```

**GATE 0 OUTPUT: `typed-role-list`** — all role names with DECISION/EXECUTION/ADVISORY/GOVERNANCE assignments. This artifact is required by GATE 1 before GATE 1 may begin.

---

### GATE 1 — Inertia Assessment

**GATE 1 INPUT: `typed-role-list`** from GATE 0. GATE 1 must not execute until `typed-role-list` is available.

**Sub-section 1.1: Default-Position Statement**

Open with:

> `DEFAULT POSITION: The team can operate flat. Structure must earn its place. Every element of formal org proposed below must demonstrate that flat operation cannot achieve the same outcome.`

**Sub-section 1.2: Mechanism Table**

Columns: `Mechanism | Type | Evidence | Flat-Operation Risk`

Minimum 2 rows required. `Type` must be drawn from: `{COORDINATION, ACCOUNTABILITY, QUALITY-GATE, KNOWLEDGE-TRANSFER, ESCALATION-PATH}`.

Example row (not counted):
```
| Architecture decisions | QUALITY-GATE | 2 squads diverged on data model | Without a gate, divergence goes undetected until integration |
```

**Sub-section 1.3: FLAT-CASE-PRESSURE Rating**

Rate from: `{NONE, LOW, MODERATE, HIGH, CRITICAL}`. One sentence justification.

**Sub-section 1.4: VERDICT**

`PROCEED-TO-STRUCTURE` or `STAY-FLAT`.

If `STAY-FLAT`: emit ABSENT labels for all downstream sections (ASCII Diagram — ABSENT, Headcount Table — ABSENT, Operating Rhythm Table — ABSENT, Committee Charters — ABSENT). Simplified or compact alternatives are not acceptable. Write `STOP — ARTIFACT COMPLETE`. No content follows.

If `PROCEED-TO-STRUCTURE`: state the concrete re-assessment trigger.

Diagram nodes, headcount area rows, rhythm rows, and committee charter fields must not appear before GATE 1 STATUS reads PASS.

```
GATE 1 STATUS: PASS when all 4 sub-sections present, VERDICT emitted, and no downstream structural content precedes this line.
```

**GATE 1 OUTPUT: `inertia-verdict`** — either `PROCEED-TO-STRUCTURE` or `STAY-FLAT`. Also outputs `flat-case-pressure-rating` from the closed set. Both artifacts are required by GATE 2 before GATE 2 may begin.

---

### GATE 2 — Structure: Diagram + Headcount

**GATE 2 INPUT: `typed-role-list`** from GATE 0 AND **`inertia-verdict`** (must be PROCEED-TO-STRUCTURE) from GATE 1. GATE 2 must not execute until both named artifacts are available from their respective gates.

**Sub-section 2.1: ASCII Org Diagram**

Minimum 2 hierarchy levels required. Committees must appear as distinct nodes. All role names must come from `ROLES-LOADED`; using an undeclared role is not acceptable.

Node format:
```
+----------------------+
| Role Name            |
| (TYPE)               |
+----------------------+
```

**Sub-section 2.2: Headcount by Area**

Columns: `Area | HC | Decides | Escalates | Key Roles`

Minimum 2 areas plus Total row. `Decides` and `Escalates` must be separate columns. Key Roles annotated with `(domain type)`.

Example row (not counted):
```
| Infrastructure | 5 | 1 | 4 | Infra Lead (technical), SRE (execution) |
```

Rhythm rows and committee charters must not appear before GATE 2 STATUS reads PASS.

```
GATE 2 STATUS: PASS when diagram has >= 2 hierarchy levels and headcount table has >= 2 areas plus Total row.
```

**GATE 2 OUTPUT: `org-diagram`** — ASCII org diagram with typed nodes. Also outputs **`headcount-table`** — area rows with Decides/Escalates split and annotated Key Roles. Both artifacts are required by GATE 3 before GATE 3 may begin.

---

### GATE 3 — Operating Rhythm + Committee Charters

**GATE 3 INPUT: `org-diagram`** from GATE 2 AND **`headcount-table`** from GATE 2. GATE 3 must not execute until both named artifacts are available.

Produce rhythm rows and committee charters in interleaved pairs. Batching all rhythm rows before all charters is not acceptable.

**Operating Rhythm Table**

Columns: `Cadence | Name | Owner | Purpose | Attendees | Output`

Minimum 3 distinct rows: ROB cadence + shiproom/gate review + governance/architecture board. Merged rows are not acceptable.

**Committee Charters** (interleaved)

Per committee: Name, Mission (one sentence), Membership (≥2 annotated roles with type), Quorum (`N of M member roles`), Escalates (specific destination).

**CHECKPOINT PAIR-COUNT-CHECK:** Count pairs produced and compare to governance rows in the rhythm table. The counts must be equal before GATE 3 STATUS may read PASS.

```
GATE 3 STATUS: PASS when rhythm table has >= 3 rows, all charters have 5 fields, and pair count matches.
```

**GATE 3 OUTPUT: `rhythm-charter-pairs`** — all interleaved rhythm rows and committee charters. Also outputs **`complete-artifact`** — the finished org-chart.md document.

---

### ORG-ELEMENT REGISTER

Categorize all structural elements:
- `cat-1`: Reporting relationships — `(cat-1)`
- `cat-2`: Committees and boards — `(cat-2)`
- `cat-3`: Operating rhythms — `(cat-3)`
- `cat-4`: Role-type overlays — `(cat-4)`

Anti-Pattern Watch: For each element, cite `(cat-N)` and flag known anti-patterns.

---

### Org Evolution Roadmap

Columns: `Trigger | Proposed Change | Risk If Ignored`

Minimum 2 rows from distinct trigger categories.

---

`ARTIFACT-END`

---

## V-04 — Combined Axis: Gate-Local DO/DO NOT + Step-Embedded Default (C-27 + C-28)

**Hypothesis**: Gate-local DO/DO NOT registers and step-embedded default-position create mutually reinforcing enforcement. The DO section for GATE 1 Sub-section 1 lists "Write default-position statement" as an explicit required operation, and an executable STEP 1a confirms it. A model sees the directive twice in the same gate scope: once in the register, once as a step instruction. Neither can be bypassed by the other's absence.

---

Generate an org structure for the product or domain provided. Read `.craft/roles/` for role grounding. Output: `org-chart.md` with ASCII org diagram, headcount by area, committee charters, and operating rhythm table.

**INERTIA FIRST.** The prior is flat. Structure must earn its place. No structural section is produced unless the inertia verdict requires it.

**GATE SEQUENCE:** GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the subsequent gate. Gates must execute in strictly ascending numeric order.

---

### GATE 0 — Roles + Classification

**DO / DO NOT — GATE 0**

| DO | DO NOT |
|----|--------|
| Emit `ROLES-LOADED` with all role names from `.craft/roles/` | Introduce role names not found in `.craft/roles/` |
| Emit `ROLES-NOTE` if `.craft/roles/` is absent | Skip `ROLES-NOTE` when directory is missing |
| Classify every role into exactly one type from `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` | Leave any role unclassified |
| Output ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED with no intervening content | Place any inertia rows, diagram nodes, headcount entries, or rhythm rows before GATE 0 STATUS |
| Output roles in three-tier order: DECISION, EXECUTION, ADVISORY/GOVERNANCE | Use an undeclared role name in any later section |

**Sub-section 0.1: Load Roles**

Read all files in `.craft/roles/`. Emit `ROLES-LOADED:` with every role name found. If absent or empty: `ROLES-NOTE: No .craft/roles/ directory found. Role names inferred from context.`

**Sub-section 0.2: Role-Type Classification**

Immediately after Sub-section 0.1 — no intervening structural content — produce `ROLE-TYPE-CLASSIFICATION:`. Classify every role from: `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`. Three-tier output order: DECISION, EXECUTION, ADVISORY/GOVERNANCE.

```
GATE 0 STATUS: [ ] ROLES-LOADED (or ROLES-NOTE) present
               [ ] Every role classified
               [ ] No downstream structural content precedes this line
               STATUS: PASS / FAIL
```

**GATE 0 PRODUCES:** `typed-role-list`.

---

### GATE 1 — Inertia Assessment

**GATE 1 REQUIRES:** `typed-role-list` from GATE 0.

**DO / DO NOT — GATE 1**

| DO | DO NOT |
|----|--------|
| **Write the default-position statement as the first content of Sub-section 1.1** | Place the default-position statement before GATE 1, in a preamble, or in any location outside Sub-section 1.1 |
| Produce all 4 sub-sections in order | Skip or merge any sub-section |
| Use closed-set Types in the mechanism table | Use Type values outside the closed set |
| Rate FLAT-CASE-PRESSURE from `{NONE, LOW, MODERATE, HIGH, CRITICAL}` | Use a rating outside the closed set |
| If STAY-FLAT: emit ABSENT labels for every downstream section, then STOP | Produce simplified or compact versions of absent sections |
| If PROCEED-TO-STRUCTURE: state a concrete re-assessment trigger | State a vague trigger |
| Emit diagram nodes, headcount rows, or rhythm rows only after GATE 1 STATUS | Emit any diagram, headcount, or rhythm content before GATE 1 STATUS |

**Sub-section 1.1: Default-Position Statement**

**STEP 1a.** Write the following statement verbatim as the first content of this sub-section:

> `DEFAULT POSITION: The team can operate flat. Structure must earn its place. Every element of formal org proposed in this artifact must demonstrate that flat operation cannot achieve the same outcome.`

This is an executable step instruction. Write this statement at this step. Do not paraphrase. Do not relocate to a preamble, a header, or any position outside GATE 1 Sub-section 1.1. The DO register above lists this as a required operation. This step is where it executes.

**STEP 1b.** Proceed to Sub-section 1.2.

**Sub-section 1.2: Mechanism Table**

Columns: `Mechanism | Type | Evidence | Flat-Operation Risk`

Minimum 2 rows. `Type` from: `{COORDINATION, ACCOUNTABILITY, QUALITY-GATE, KNOWLEDGE-TRANSFER, ESCALATION-PATH}`.

Example row (not counted):
```
| Incident ownership | ACCOUNTABILITY | 3 services share on-call | Without owner assignment, incidents fall through |
```

**Sub-section 1.3: FLAT-CASE-PRESSURE Rating**

From: `{NONE, LOW, MODERATE, HIGH, CRITICAL}`. One sentence justification.

**Sub-section 1.4: VERDICT**

`PROCEED-TO-STRUCTURE` or `STAY-FLAT`.

If `STAY-FLAT`: emit ABSENT labels for ASCII Diagram, Headcount Table, Operating Rhythm Table, Committee Charters. Simplified or compact alternatives are not acceptable. Write `STOP — ARTIFACT COMPLETE`.

If `PROCEED-TO-STRUCTURE`: state the concrete re-assessment trigger.

```
GATE 1 STATUS: [ ] Default-position statement is first content of Sub-section 1.1
               [ ] All 4 sub-sections present
               [ ] Mechanism table has >= 2 rows with closed-set Types
               [ ] FLAT-CASE-PRESSURE from closed set
               [ ] VERDICT emitted
               [ ] No diagram/headcount/rhythm content precedes this line
               STATUS: PASS / FAIL
```

**GATE 1 PRODUCES:** `inertia-verdict`, `flat-case-pressure-rating`.

---

### GATE 2 — Structure: Diagram + Headcount

**GATE 2 REQUIRES:** `typed-role-list` from GATE 0 + `inertia-verdict` (PROCEED-TO-STRUCTURE) from GATE 1.

**DO / DO NOT — GATE 2**

| DO | DO NOT |
|----|--------|
| Produce a minimum 2-level hierarchy in the ASCII diagram | Produce a single-level (flat) diagram |
| Render committees as distinct diagram nodes | Merge committees into reporting line boxes |
| Use only role names from ROLES-LOADED | Introduce undeclared role names |
| Provide Decides and Escalates as separate headcount columns | Merge Decides and Escalates into one column |
| Annotate Key Roles with `(domain type)` | Omit domain-type annotations |
| Include a Total row in the headcount table | Omit the Total row |
| Emit rhythm rows and charters only after GATE 2 STATUS | Emit rhythm or charter content before GATE 2 STATUS |

**Sub-section 2.1: ASCII Org Diagram**

Minimum 2 hierarchy levels. Committees as distinct nodes. All roles from ROLES-LOADED.

Node format:
```
+----------------------+
| Role Name            |
| (TYPE)               |
+----------------------+
```

**Sub-section 2.2: Headcount by Area**

Columns: `Area | HC | Decides | Escalates | Key Roles`

Minimum 2 areas plus Total row. Key Roles annotated with `(domain type)`.

Example row (not counted):
```
| Mobile | 8 | 2 | 6 | Mobile Lead (product), iOS Eng (execution), Android Eng (execution) |
```

```
GATE 2 STATUS: [ ] ASCII diagram has >= 2 hierarchy levels
               [ ] Committees as distinct nodes
               [ ] All role names from ROLES-LOADED
               [ ] Headcount table has >= 2 areas plus Total row
               [ ] Decides and Escalates are separate columns
               STATUS: PASS / FAIL
```

**GATE 2 PRODUCES:** `org-diagram`, `headcount-table`.

---

### GATE 3 — Operating Rhythm + Committee Charters

**GATE 3 REQUIRES:** `org-diagram` + `headcount-table` from GATE 2.

**DO / DO NOT — GATE 3**

| DO | DO NOT |
|----|--------|
| Interleave rhythm rows and charters: row 1 → charter 1 → row 2 → charter 2 | Batch all rhythm rows before all charters |
| Include at minimum an ROB row, a shiproom/gate row, a governance/architecture row | Omit any of the three required row types |
| Provide all 5 charter fields per committee | Omit any charter field |
| Express Quorum as `N of M member roles` | Express Quorum as a percentage or bare number |
| Name a specific Escalates destination | Use a vague Escalates target |
| Verify pair count before emitting GATE 3 STATUS | Skip pair-count verification |

**Operating Rhythm Table**

Columns: `Cadence | Name | Owner | Purpose | Attendees | Output`

Minimum 3 distinct rows: ROB cadence + shiproom/gate review + governance/architecture board.

**Committee Charters** (interleaved with rhythm rows)

Per committee: Name, Mission (one sentence), Membership (≥2 annotated roles), Quorum (`N of M member roles`), Escalates (specific destination).

**CHECKPOINT PAIR-COUNT-CHECK:** Pairs produced must equal governance rows in the rhythm table.

```
GATE 3 STATUS: [ ] Rhythm table has >= 3 distinct rows
               [ ] Rhythm-charter pairs are interleaved
               [ ] All charters have 5 fields
               [ ] Quorum in "N of M member roles" form
               [ ] Escalates names specific destination
               [ ] Pair count matches rhythm row count
               STATUS: PASS / FAIL
```

**GATE 3 PRODUCES:** `rhythm-charter-pairs`, `complete-artifact`.

---

### ORG-ELEMENT REGISTER

Categorize all structural elements:
- `cat-1`: Reporting relationships
- `cat-2`: Committees and boards
- `cat-3`: Operating rhythms
- `cat-4`: Role-type overlays

Anti-Pattern Watch: Cite `(cat-N)` for each element. Flag committee proliferation, unclear escalation, span-of-control breach, silent hierarchy.

---

### Org Evolution Roadmap

Columns: `Trigger | Proposed Change | Risk If Ignored`

Minimum 2 rows from distinct trigger categories.

---

`ARTIFACT-END`

---

## V-05 — Combined Axis: Full v8 Integration (C-25 + C-26 + C-27 + C-28)

**Hypothesis**: Combining named artifact handoffs at every gate boundary (C-25), prohibited-content contracts at GATE 1/2/3 mirroring the C-24 pattern (C-26), gate-local DO/DO NOT registers (C-27), and step-embedded default-position (C-28) closes all four bypass paths identified across v7–v8 analysis simultaneously. The design is maximally self-contained: each gate is independently verifiable without reference to surrounding prose.

---

Generate an org structure for the product or domain provided. Read `.craft/roles/` for role grounding. Output: `org-chart.md` with ASCII org diagram, headcount by area, committee charters, and operating rhythm table.

**INERTIA FIRST. THE DEFAULT POSITION IS FLAT.** Formal structure must earn its place. Every section of this artifact is conditional on the inertia assessment verdict.

**GATE SEQUENCE:** GATE 0, GATE 1, GATE 2, GATE 3. Strictly ascending execution order. Each gate's named output artifacts are required inputs for the subsequent gate. A gate must not execute until its named inputs are present.

---

### GATE 0 — Roles + Classification

**GATE 0 INPUT:** Domain name or context (provided by caller). No prior gate outputs required.

**DO / DO NOT — GATE 0**

| DO | DO NOT |
|----|--------|
| Read all files in `.craft/roles/`; emit `ROLES-LOADED:` | Introduce any role name not found in `.craft/roles/` |
| Emit `ROLES-NOTE` when `.craft/roles/` is absent | Omit `ROLES-NOTE` when the directory is missing |
| Classify every role to exactly one type from `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}` | Leave any role unclassified |
| Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED with zero intervening content | Place inertia rows, diagram nodes, headcount entries, or rhythm rows before GATE 0 STATUS |
| Use undeclared role names in any subsequent section | Output roles in three-tier order: DECISION, EXECUTION, ADVISORY/GOVERNANCE |

**GATE 0 CONTAINMENT CONTRACT:** The following content must not appear before GATE 0 STATUS reads PASS: inertia assessment rows, ASCII diagram nodes, headcount entries, operating rhythm rows, committee charter fields.

**Sub-section 0.1: Load Roles**

Read every file in `.craft/roles/`. Emit `ROLES-LOADED:` with all role names. If absent or empty: `ROLES-NOTE: No .craft/roles/ directory found. Role names inferred from context.`

**Sub-section 0.2: Role-Type Classification**

Immediately after Sub-section 0.1 — no intervening content of any kind — produce `ROLE-TYPE-CLASSIFICATION:`. Assign every role to exactly one type from: `{DECISION, EXECUTION, ADVISORY, GOVERNANCE}`.

- `DECISION`: outcome accountability, budget, or headcount authority
- `EXECUTION`: builds or delivers within defined scope
- `ADVISORY`: expertise on request; no unilateral authority
- `GOVERNANCE`: enforces standards, approves exceptions

Output in three-tier order: DECISION, EXECUTION, ADVISORY/GOVERNANCE.

```
GATE 0 STATUS: [ ] ROLES-LOADED (or ROLES-NOTE) present
               [ ] Every role has a type assignment
               [ ] GATE 0 CONTAINMENT CONTRACT satisfied (no downstream content precedes this line)
               STATUS: PASS / FAIL
```

**GATE 0 OUTPUT: `typed-role-list`** — all role names with type assignments. This artifact is the required input for GATE 1. GATE 1 must not execute until `typed-role-list` is available from GATE 0.

---

### GATE 1 — Inertia Assessment

**GATE 1 INPUT: `typed-role-list`** from GATE 0. Must be present before GATE 1 begins.

**DO / DO NOT — GATE 1**

| DO | DO NOT |
|----|--------|
| **Execute STEP 1a: write the default-position statement verbatim as the first content of Sub-section 1.1** | Place the default-position statement in a preamble, artifact header, or any location outside Sub-section 1.1 |
| Produce all 4 sub-sections in sequence | Skip or merge any sub-section |
| Use only closed-set Types in the mechanism table | Use Type values outside `{COORDINATION, ACCOUNTABILITY, QUALITY-GATE, KNOWLEDGE-TRANSFER, ESCALATION-PATH}` |
| Rate FLAT-CASE-PRESSURE from `{NONE, LOW, MODERATE, HIGH, CRITICAL}` | Rate FLAT-CASE-PRESSURE with a value outside the closed set |
| If STAY-FLAT: emit ABSENT labels for all downstream sections, then STOP | Produce simplified or compact versions of absent sections |
| If PROCEED-TO-STRUCTURE: state a specific, concrete re-assessment trigger | State a vague or hypothetical re-assessment trigger |

**GATE 1 CONTAINMENT CONTRACT:** The following content must not appear before GATE 1 STATUS reads PASS: ASCII diagram nodes, headcount area rows, operating rhythm cadence rows, committee charter fields.

**Sub-section 1.1: Default-Position Statement**

**STEP 1a.** Write the following statement verbatim as the first content of this sub-section, before anything else in GATE 1:

> `DEFAULT POSITION: The team can operate flat. Structure must earn its place. Every element of formal org proposed in this artifact must demonstrate that flat operation cannot achieve the same outcome.`

This is an executable step instruction embedded within GATE 1's execution sequence. Write this statement at this step. Do not paraphrase. Do not move this statement to any location outside GATE 1 Sub-section 1.1. The DO register above identifies this as a required operation; this step is where it executes.

**STEP 1b.** Proceed to Sub-section 1.2.

**Sub-section 1.2: Mechanism Table**

Columns: `Mechanism | Type | Evidence | Flat-Operation Risk`

Minimum 2 rows. `Type` from: `{COORDINATION, ACCOUNTABILITY, QUALITY-GATE, KNOWLEDGE-TRANSFER, ESCALATION-PATH}`.

Example row (not counted):
```
| Cross-team dependency tracking | COORDINATION | 4 squads share a data pipeline | Without owner, untracked dependencies cause silent breakage |
```

**Sub-section 1.3: FLAT-CASE-PRESSURE Rating**

One of: `{NONE, LOW, MODERATE, HIGH, CRITICAL}`. One sentence justification.

**Sub-section 1.4: VERDICT**

`PROCEED-TO-STRUCTURE` or `STAY-FLAT`.

If `STAY-FLAT`:
- Emit: `ASCII Diagram — ABSENT`, `Headcount Table — ABSENT`, `Operating Rhythm Table — ABSENT`, `Committee Charters — ABSENT`.
- Simplified or compact alternatives are not acceptable.
- Write: `STOP — ARTIFACT COMPLETE`. No content follows this line.

If `PROCEED-TO-STRUCTURE`: State the concrete re-assessment trigger — a specific headcount number, product milestone, or failure mode.

**CHECKPOINT INERTIA-CHECK:** Confirm all 4 sub-sections present, default-position statement is first content of Sub-section 1.1, and VERDICT is emitted. Confirm GATE 1 CONTAINMENT CONTRACT satisfied.

```
GATE 1 STATUS: [ ] Default-position statement is first content of Sub-section 1.1 (STEP 1a executed)
               [ ] All 4 sub-sections present
               [ ] Mechanism table has >= 2 rows with closed-set Types
               [ ] FLAT-CASE-PRESSURE rating from closed set with one-sentence justification
               [ ] VERDICT emitted with concrete re-assessment trigger (if PROCEED)
               [ ] GATE 1 CONTAINMENT CONTRACT satisfied
               STATUS: PASS / FAIL
```

**GATE 1 OUTPUT: `inertia-verdict`** — `PROCEED-TO-STRUCTURE` or `STAY-FLAT`. Also **`flat-case-pressure-rating`** from the closed set. Both artifacts are required inputs for GATE 2. GATE 2 must not execute until both are present from GATE 1.

---

### GATE 2 — Structure: Diagram + Headcount

**GATE 2 INPUT: `typed-role-list`** from GATE 0 AND **`inertia-verdict`** (must be PROCEED-TO-STRUCTURE) from GATE 1. Both must be present before GATE 2 begins.

**DO / DO NOT — GATE 2**

| DO | DO NOT |
|----|--------|
| Produce a minimum 2-level hierarchy in the ASCII diagram | Produce a single-level (flat) diagram |
| Render committees as distinct diagram nodes | Merge committees into reporting line boxes |
| Use only role names from `ROLES-LOADED` | Introduce undeclared role names in the diagram |
| Provide Decides and Escalates as separate headcount columns | Merge Decides and Escalates into a single column |
| Annotate Key Roles with `(domain type)` | Omit domain-type annotations from Key Roles |
| Include a Total row in the headcount table | Omit the Total row |

**GATE 2 CONTAINMENT CONTRACT:** The following content must not appear before GATE 2 STATUS reads PASS: operating rhythm cadence rows, committee charter fields.

**Sub-section 2.1: ASCII Org Diagram**

Minimum 2 hierarchy levels. Committees as distinct nodes. All role names from ROLES-LOADED.

Node format:
```
+----------------------+
| Role Name            |
| (TYPE)               |
+----------------------+
```

**Sub-section 2.2: Headcount by Area**

Columns: `Area | HC | Decides | Escalates | Key Roles`

Minimum 2 areas plus Total row. Key Roles annotated with `(domain type)`.

Example row (not counted):
```
| Developer Experience | 5 | 1 | 4 | DevEx Lead (product), Tooling Eng (execution) |
```

**CHECKPOINT DIAGRAM-CHECK:** Confirm diagram has ≥2 hierarchy levels, all role names are from the roles block, and headcount table has ≥2 areas plus Total row before proceeding.

```
GATE 2 STATUS: [ ] ASCII diagram has >= 2 hierarchy levels
               [ ] Committees appear as distinct nodes
               [ ] All role names from ROLES-LOADED
               [ ] Headcount table has >= 2 areas plus Total row
               [ ] Decides and Escalates are separate columns
               [ ] Key Roles annotated with (domain type)
               [ ] GATE 2 CONTAINMENT CONTRACT satisfied
               STATUS: PASS / FAIL
```

**GATE 2 OUTPUT: `org-diagram`** — ASCII diagram with typed nodes. Also **`headcount-table`** — area rows with Decides/Escalates split and annotated Key Roles. Both artifacts are required inputs for GATE 3. GATE 3 must not execute until both are present from GATE 2.

---

### GATE 3 — Operating Rhythm + Committee Charters

**GATE 3 INPUT: `org-diagram`** from GATE 2 AND **`headcount-table`** from GATE 2. Both must be present before GATE 3 begins.

**DO / DO NOT — GATE 3**

| DO | DO NOT |
|----|--------|
| Produce rhythm rows and charters in interleaved pairs: row 1 → charter 1 → row 2 → charter 2 | Batch all rhythm rows before all charters |
| Include at minimum an ROB row, a shiproom/gate row, and a governance/architecture row | Omit any of the three required row types |
| Include all 5 charter fields per committee | Omit any charter field |
| Express Quorum as `N of M member roles` | Express Quorum as a percentage or bare headcount |
| Name a specific destination in the Escalates field | Use a vague Escalates target such as "leadership" or "management" |
| Verify pair count before emitting GATE 3 STATUS | Skip pair-count verification |
| Annotate at least 2 roles in each Membership list with `(TYPE)` | List only one role in any Membership |

**GATE 3 CONTAINMENT CONTRACT:** No additional structural sections may appear after GATE 3 STATUS reads PASS except the ORG-ELEMENT REGISTER and Org Evolution Roadmap.

**Operating Rhythm Table**

Columns: `Cadence | Name | Owner | Purpose | Attendees | Output`

Minimum 3 distinct rows: ROB cadence + shiproom/gate review + governance/architecture board.

Example row (not counted):
```
| Bi-weekly | Program Shiproom | VP Engineering | Surface cross-team blockers and shipping risks | Tech leads, PM, TPM | Risk log, go/no-go decision |
```

**Committee Charters** (interleaved with rhythm rows)

Per committee, all 5 required fields:
1. `Name`
2. `Mission` — one sentence
3. `Membership` — minimum 2 roles, each annotated with `(TYPE)`
4. `Quorum` — `N of M member roles`
5. `Escalates` — specific destination role or governance body

Example charter (not counted):
```
Name: Technical Architecture Board
Mission: Review and ratify technical standards with cross-team impact.
Membership: Principal Architect (GOVERNANCE), VP Engineering (DECISION), Staff Engineers x2 (ADVISORY)
Quorum: 3 of 4 member roles
Escalates: CTO
```

**CHECKPOINT PAIR-COUNT-CHECK:** After producing all rhythm-charter pairs, count pairs produced and compare to governance rows in the rhythm table. Counts must be equal before GATE 3 STATUS may read PASS. If counts differ, identify the missing charter and produce it before proceeding.

```
GATE 3 STATUS: [ ] Rhythm table has >= 3 distinct rows
               [ ] Rows cover ROB, shiproom/gate, governance/architecture
               [ ] Rhythm-charter pairs are interleaved (not batched)
               [ ] All charters have all 5 fields
               [ ] Quorum in "N of M member roles" form
               [ ] Escalates names a specific destination
               [ ] Pair count matches rhythm row count (CHECKPOINT PAIR-COUNT-CHECK complete)
               [ ] GATE 3 CONTAINMENT CONTRACT satisfied
               STATUS: PASS / FAIL
```

**GATE 3 OUTPUT: `rhythm-charter-pairs`** — all interleaved rhythm rows and committee charters. Also **`complete-artifact`** — the finished org-chart.md document.

---

### ORG-ELEMENT REGISTER

List all structural elements used in this artifact, categorized:
- `cat-1`: Reporting relationships — `(cat-1)`
- `cat-2`: Committees and boards — `(cat-2)`
- `cat-3`: Operating rhythms — `(cat-3)`
- `cat-4`: Role-type overlays — `(cat-4)`

Anti-Pattern Watch: For each element, cite `(cat-N)` and note if the element risks a known anti-pattern: committee proliferation, unclear escalation path, span-of-control breach, silent hierarchy.

---

### Org Evolution Roadmap

Columns: `Trigger | Proposed Change | Risk If Ignored`

Minimum 2 rows from distinct trigger categories. Valid categories: headcount threshold, technology adoption, market expansion, product milestone, failure mode. No two rows may share the same trigger category.

---

`ARTIFACT-END`

---

## Summary Table

| Variation | Single/Combined | Primary Axis | C-27 | C-28 | C-25 | C-26 | Expected delta |
|-----------|----------------|--------------|------|------|------|------|----------------|
| V-01 | Single | Step-embedded default (C-28) | FAIL (prose modal only) | PASS | PARTIAL (chain-level) | PARTIAL (GATE 1+2 only) | C-28 PASS, C-13 PASS |
| V-02 | Single | Gate-local DO/DO NOT (C-27) | PASS | FAIL (preamble only) | FAIL (no per-gate I/O) | PARTIAL (GATE 0 only) | C-27 PASS, C-13 PARTIAL |
| V-03 | Single | Named artifact handoffs (C-25) | FAIL (prose modal only) | FAIL (preamble only) | PASS | PARTIAL (GATE 0+1+2) | C-25 PASS |
| V-04 | Combined | C-27 + C-28 | PASS | PASS | PARTIAL (chain-level) | PARTIAL (GATE 1+2) | C-27 PASS + C-28 PASS |
| V-05 | Combined | C-25 + C-26 + C-27 + C-28 | PASS | PASS | PASS | PASS | Full v8 closure |
