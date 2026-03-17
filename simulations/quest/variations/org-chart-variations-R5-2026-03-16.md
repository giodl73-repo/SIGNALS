Good. I have enough context. Writing the five complete variations now.

---

## org-chart — V-01 through V-05

### Variation axes selected
- **V-01** — Inertia framing (single axis): default-flat as explicit burden-of-proof, ABSENT/STOP termination, two-site constraint
- **V-02** — Output format (single axis): inline example rows in every schema, format-led instruction order
- **V-03** — Role sequence (single axis): GATE 0 = role-type classification before inertia assessment
- **V-04** — Verification checkpoints (single axis): checkbox-format gates + blocking verification loop before every gate emission
- **V-05** — Combined: classification-first + default-flat declaration + two-site constraints + ABSENT/STOP + interleaved rhythm-charter + count verification + checkbox gates

---

## V-01

**Axis:** Inertia framing
**Hypothesis:** Opening with an explicit burden-of-proof declaration — the team can operate flat, structure must justify itself — eliminates the most common failure mode: producing org structure because the skill was invoked, not because structure is warranted.

```
You are executing the /org-chart skill. Generate an org structure for a product or
domain. Read .craft/roles/ first.

THE TEAM CAN OPERATE FLAT. Structure is a cost, not a default. Before proposing any
diagram, headcount table, committee, or operating rhythm, you must establish that
informal coordination mechanisms are insufficient at current scale. This is the burden
of proof. The org chart earns its existence or it does not get produced.

---

## STEP 0: LOAD ROLES

Read all files in .craft/roles/. Extract every role name and any available metadata.

Emit one of:
```
ROLES-LOADED: [role-name-1, role-name-2, ...]
```
or, if the directory is absent or empty:
```
ROLES-NOTE: No .craft/roles/ found. Proceeding with roles declared by user input.
```

CONSTRAINT (enforced at two sites):
SITE 1 — slot order: The ROLES-LOADED or ROLES-NOTE block appears before every other
section.
SITE 2 — conditional rule: If any role name appears in a later section, that role
name must be present in the ROLES-LOADED list. Introducing a role name not declared
here is not acceptable.

---

## STEP 1: INERTIA ASSESSMENT

The Inertia Assessment must appear before any org diagram, headcount table, committee
charter, or operating rhythm table. Four sub-sections are required. Producing any
structural output before this section is complete is not acceptable.

### 1a. Default-Position Statement

Open the Inertia Assessment with this exact statement, verbatim:

  DEFAULT POSITION: The team can operate flat. Formal org structure requires explicit
  justification. The burden of proof is on structure, not on flatness.

Do not paraphrase, abbreviate, or move this statement.

### 1b. Coordination Mechanism Table

Assess informal coordination mechanisms currently available to the team.

Schema:
| Mechanism | Type | Effectiveness (1–5) | Breaks At |
|-----------|------|---------------------|-----------|

Type is a closed set: {SYNC, ASYNC, ESCALATION, GOVERNANCE, SOCIAL}. No other value
is permitted. Include at minimum 2 rows.

### 1c. Flat-Case Pressure Rating

Emit one of:
  FLAT-CASE-PRESSURE: NONE | LOW | MEDIUM | HIGH | CRITICAL

Rating definitions:
- NONE: All mechanisms functional, no breakage signals
- LOW: 1 mechanism showing stress, workarounds exist
- MEDIUM: 2+ mechanisms stressed, coordination tax visible
- HIGH: Regular coordination failures, clear bottlenecks
- CRITICAL: Flat operation causing delivery failures

### 1d. Verdict

Emit:
  VERDICT: OPERATE-FLAT | STRUCTURE-WARRANTED
  Re-assessment trigger: [concrete condition — headcount threshold, product event, or
  incident pattern — that would change this verdict]

---

## FLAT-VERDICT BRANCH

If VERDICT = OPERATE-FLAT:

For each of the following sections — Org Diagram, Role-Type Classification, Headcount
by Area, Operating Rhythm, Committee Charters, Org Evolution Roadmap — emit exactly:

  [SECTION NAME] — ABSENT
  Reason: Flat verdict taken. This section is not produced.
  NOT an acceptable substitute: "simplified hierarchy," "lightweight structure,"
  "interim arrangement," or any compressed-hierarchy alternative.

After the final ABSENT block, emit:

  ARTIFACT END. No content follows this line.

No content of any kind may appear after ARTIFACT END. This is a structural halt,
not a label. Producing content after this line violates the flat-verdict contract.

If VERDICT = STRUCTURE-WARRANTED: proceed to Step 2.

---

## STEP 2: ORG DIAGRAM

Draw an ASCII org chart. Requirements:
- Minimum 2 hierarchy levels
- All role names from ROLES-LOADED block only
- Committees appear as distinct nodes (not embedded in a role box)
- Each role annotated with (domain-type) drawn from Step 3

Format:
  [Domain / Product Name]
  │
  ├── [Area 1]
  │   ├── [Role A] (type)
  │   └── [Role B] (type)
  │
  ├── [Area 2]
  │   └── [Role C] (type)
  │
  └── [Committee: Name]
      ├── [Role A]
      └── [Role C]

CONSTRAINT (enforced at two sites):
SITE 1 — slot order: The org diagram appears after Step 1 (Inertia Assessment) with
STRUCTURE-WARRANTED verdict.
SITE 2 — conditional rule: If you produce an org diagram box, a STRUCTURE-WARRANTED
verdict must appear before it in the artifact. Producing a diagram without a preceding
STRUCTURE-WARRANTED verdict is not acceptable.

---

## STEP 3: ROLE-TYPE CLASSIFICATION

Classify every role from the ROLES-LOADED block.

Closed-set taxonomy: {DECISION, EXECUTION, ADVISORY, GOVERNANCE}

Format:
  ROLE-TYPE-CLASSIFICATION
  | Role       | Type       | Rationale |
  |------------|------------|-----------|
  | [Role A]   | DECISION   | ...       |
  | [Role B]   | EXECUTION  | ...       |

All roles from ROLES-LOADED must appear. Three-tier order: DECISION roles first,
then EXECUTION, then ADVISORY/GOVERNANCE. No role type outside the closed set.

---

## STEP 4: HEADCOUNT BY AREA

| Area     | Headcount | Decides | Escalates | Key Roles                    |
|----------|-----------|---------|-----------|------------------------------|
| [Area 1] | N         | owner   | PM        | [Role A] (decision-type)     |
| Total    | N         | —       | —         | —                            |

Requirements:
- Minimum 2 areas + Total row
- Decides and Escalates are separate columns (do not merge)
- Key Roles annotated with (domain type) from Step 3

---

## STEP 5: OPERATING RHYTHM + COMMITTEE CHARTERS (INTERLEAVED)

Produce rhythm rows and committee charters in pairs. For each governance row:
1. Emit the rhythm table row
2. Immediately emit its committee charter

Do not batch all rhythm rows first and all charters second. This order is required.

Rhythm row schema:
| Cadence  | Name         | Participants | Purpose          | Owner    |
|----------|--------------|--------------|------------------|----------|

Committee charter schema (5 fields required):
  COMMITTEE: [Name]
  Purpose:    [one sentence]
  Membership: [Role A] (type), [Role B] (type)  ← minimum 2 annotated roles
  Quorum:     N of M member roles               ← fraction form required
  Escalates to: [named destination — not "leadership" or "management"]

Operating rhythm requirements:
- Minimum 3 distinct rows: one ROB/regular cadence, one shiproom or gate, one
  governance body
- No merged rows

After all pairs are produced:
  PAIR-COUNT CHECK: [N] pairs produced. Rhythm table has [N] governance rows.
  Match: YES | NO

If NO: identify and produce the missing charter before continuing.

---

## STEP 6: ORG EVOLUTION ROADMAP

| Trigger                     | Current State | Proposed Change | Reversibility |
|-----------------------------|---------------|-----------------|---------------|

Requirements:
- Minimum 2 rows
- Rows from distinct trigger categories — no two rows may both be headcount thresholds
- Valid categories: headcount, product-scope, market-event, incident-pattern,
  capability-gap

---

## OUTPUT

Write the completed artifact to org-chart.md.

All sections must be present, or explicitly ABSENT with reason and the ARTIFACT END
terminator (flat-verdict path only). Partial artifacts are not acceptable.
```

---

## V-02

**Axis:** Output format
**Hypothesis:** Every table schema anchored with a complete worked example row — in exact expected format, not just field labels — eliminates format drift that field-label-only schemas cannot prevent.

```
You are executing the /org-chart skill. Generate an org structure for a product or
domain. Read .craft/roles/ first.

---

## STEP 0: LOAD ROLES

Read all files in .craft/roles/. Extract every role name and available metadata.

Emit:
  ROLES-LOADED: [role-name-1, role-name-2, ...]

If absent or empty:
  ROLES-NOTE: No .craft/roles/ found. Proceeding with roles declared by user input.

All role names used in subsequent sections must appear in this block.

---

## STEP 1: INERTIA ASSESSMENT

Assess whether the team needs formal structure at all. The Inertia Assessment must
appear before any org diagram or structural output.

Required sub-sections:

### 1a. Default-Position Statement

  DEFAULT POSITION: The team can operate flat. Formal org structure requires explicit
  justification. The burden of proof is on structure, not on flatness.

### 1b. Coordination Mechanism Table

Schema with example:
| Mechanism       | Type       | Effectiveness (1–5) | Breaks At                             |
|-----------------|------------|---------------------|---------------------------------------|
| Weekly standup  | SYNC       | 4                   | >8 participants or >3 work-streams    |

Type closed set: {SYNC, ASYNC, ESCALATION, GOVERNANCE, SOCIAL}. Minimum 2 rows.
The example row above anchors the format. Your rows must match this structure exactly.

### 1c. Flat-Case Pressure Rating

  FLAT-CASE-PRESSURE: NONE | LOW | MEDIUM | HIGH | CRITICAL

### 1d. Verdict

  VERDICT: OPERATE-FLAT | STRUCTURE-WARRANTED
  Re-assessment trigger: [concrete condition]

If OPERATE-FLAT: emit ABSENT blocks for all subsequent sections and stop.
If STRUCTURE-WARRANTED: continue.

---

## STEP 2: ROLE-TYPE CLASSIFICATION

Classify every role from ROLES-LOADED. Closed set: {DECISION, EXECUTION, ADVISORY,
GOVERNANCE}.

Schema with example:
  ROLE-TYPE-CLASSIFICATION
  | Role             | Type       | Rationale                                   |
  |------------------|------------|---------------------------------------------|
  | Product Manager  | DECISION   | Sets prioritization direction for the area  |

Your rows must follow this exact format. Three-tier order: DECISION first, then
EXECUTION, then ADVISORY/GOVERNANCE. No role type outside the closed set.

---

## STEP 3: ORG DIAGRAM

ASCII org chart. Minimum 2 hierarchy levels. All roles from ROLES-LOADED. Committees
as distinct nodes. Roles annotated with (type) from Step 2.

Format example:
  Signal Platform
  │
  ├── Evidence Gathering
  │   ├── PM [Product Manager] (DECISION)
  │   └── Lead Architect (DECISION)
  │
  ├── Delivery
  │   └── Engineering Lead (EXECUTION)
  │
  └── [Committee: Architecture Review Board]
      ├── Lead Architect
      └── Engineering Lead

Your diagram must follow this shape. Hierarchy levels and committee nodes are required,
not optional.

---

## STEP 4: HEADCOUNT BY AREA

Schema with example:
| Area               | Headcount | Decides              | Escalates  | Key Roles                          |
|--------------------|-----------|----------------------|------------|------------------------------------|
| Evidence Gathering | 3         | PM, Lead Architect   | Exec Sponsor | PM (DECISION), Lead Arch (DECISION) |
| Total              | 3         | —                    | —          | —                                  |

Requirements:
- Minimum 2 areas + Total row (matching the example structure above)
- Decides and Escalates are separate columns
- Key Roles annotated with (type) drawn from Step 2

---

## STEP 5: OPERATING RHYTHM + COMMITTEE CHARTERS (INTERLEAVED)

Produce each rhythm row immediately followed by its committee charter. Produce in
pairs. Do not batch rows first and charters second.

Rhythm row schema with example:
| Cadence  | Name                       | Participants              | Purpose                      | Owner         |
|----------|----------------------------|---------------------------|------------------------------|---------------|
| Weekly   | Signal Engineering Standup | All ICs + leads            | Unblock, surface dependencies | Eng Lead      |

Committee charter schema with example:
  COMMITTEE: Architecture Review Board
  Purpose:    Approve all cross-area technical decisions before implementation begins.
  Membership: Lead Architect (DECISION), Engineering Lead (EXECUTION), PM (DECISION)
  Quorum:     2 of 3 member roles
  Escalates to: VP Engineering

Your charters must match this structure exactly. All 5 fields required. Quorum in
"N of M member roles" form. Escalates names a real destination (not "leadership").

Operating rhythm requires:
- Minimum 3 distinct rows: one ROB/regular, one shiproom or gate, one governance body
- No merged rows

After all pairs:
  PAIR-COUNT CHECK: [N] pairs produced. Rhythm table has [N] governance rows.
  Match: YES | NO

If NO: produce the missing charter before continuing.

---

## STEP 6: ORG EVOLUTION ROADMAP

Schema with example:
| Trigger                              | Current State        | Proposed Change              | Reversibility |
|--------------------------------------|----------------------|------------------------------|---------------|
| Team grows past 10 engineers         | Flat eng team        | Add sub-lead per area        | High — remove role if team shrinks |

Requirements:
- Minimum 2 rows
- Distinct trigger categories — no two rows may both be headcount thresholds
- Valid categories: headcount, product-scope, market-event, incident-pattern,
  capability-gap

---

## STEP 7: ORG-ELEMENT REGISTER + ANTI-PATTERN WATCH

Categorize every org element introduced:

  ORG-ELEMENT REGISTER
  | Element               | Category | Rationale                         |
  |-----------------------|----------|-----------------------------------|
  | Area: Evidence Gathering | cat-2 | Functional grouping by capability |

Categories: cat-1 (individual role), cat-2 (functional area), cat-3 (committee or
governance body), cat-4 (cross-cutting program or initiative).

Then:
  ANTI-PATTERN WATCH
  | Pattern                    | Risk      | Mitigant                           |
  |----------------------------|-----------|------------------------------------|
  | Committee proliferation (cat-3) | HIGH | Limit to 2 standing committees max |

Each anti-pattern must cite its category in (cat-N) form.

---

## OUTPUT

Write the completed artifact to org-chart.md.

All sections must appear in order. Every table must match its schema and example row.
A table that deviates from the example structure is not acceptable output.
```

---

## V-03

**Axis:** Role sequence
**Hypothesis:** Placing role-type classification as GATE 0 — before any inertia assessment or structural decision — prevents the feedback-loop bypass where inertia-assessment assumptions contaminate the role taxonomy. Role types become inputs to structural decisions, not byproducts of them.

```
You are executing the /org-chart skill. Generate an org structure for a product or
domain. Execute the gates below in strict sequence. No gate may reference information
not established by a prior gate.

---

## GATE 0: ROLE INVENTORY + TYPE CLASSIFICATION

Execute this gate before any structural assessment. Role types established here are
inputs to all subsequent gates. No structural decision may reference a role type not
established in this gate.

### 0a. Load Roles

Read all files in .craft/roles/. Extract every role name.

Emit:
  ROLES-LOADED: [role-name-1, role-name-2, ...]

If absent or empty:
  ROLES-NOTE: No .craft/roles/ found. Proceeding with roles declared by user input.

### 0b. Classify Every Role

Classify each role from ROLES-LOADED into the closed-set taxonomy:
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}

  ROLE-TYPE-CLASSIFICATION
  | Role       | Type       | Rationale |
  |------------|------------|-----------|

Produce this table in three-tier order: DECISION roles first, then EXECUTION, then
ADVISORY/GOVERNANCE. All roles from ROLES-LOADED must appear. No role type outside
the closed set is permitted.

GATE 0 STATUS: PASS when all roles classified into closed-set types.
              FAIL when any role is unclassified or typed outside the closed set.
Do not proceed to GATE 1 until GATE 0 STATUS = PASS.

---

## GATE 1: INERTIA ASSESSMENT

Uses role types from GATE 0. No new role types may be introduced here.

Four sub-sections required.

### 1a. Default-Position Statement

  DEFAULT POSITION: The team can operate flat. Formal org structure requires explicit
  justification. The burden of proof is on structure, not on flatness.

### 1b. Coordination Mechanism Table

| Mechanism | Type | Effectiveness (1–5) | Breaks At |
|-----------|------|---------------------|-----------|

Type closed set: {SYNC, ASYNC, ESCALATION, GOVERNANCE, SOCIAL}. Minimum 2 rows.

### 1c. Flat-Case Pressure Rating

  FLAT-CASE-PRESSURE: NONE | LOW | MEDIUM | HIGH | CRITICAL

### 1d. Verdict

  VERDICT: OPERATE-FLAT | STRUCTURE-WARRANTED
  Re-assessment trigger: [concrete condition]

GATE 1 STATUS: PASS when all 4 sub-sections complete and verdict emitted.
              FAIL when any sub-section is absent or verdict is missing.
Do not proceed until GATE 1 STATUS = PASS.

If VERDICT = OPERATE-FLAT: emit ABSENT block for all gates 2–5 and stop.

---

## GATE 2: STRUCTURAL DIAGRAM

Requires GATE 0 role types and GATE 1 STRUCTURE-WARRANTED verdict.

Draw an ASCII org chart:
- Minimum 2 hierarchy levels
- All roles from ROLES-LOADED (GATE 0) only
- Role types drawn from GATE 0 classification — no new type assignments
- Committees as distinct nodes

  [Domain]
  │
  ├── [Area 1]
  │   ├── [Role A] (type from GATE 0)
  │   └── [Role B] (type from GATE 0)
  │
  └── [Committee: Name]
      └── [Role A]

GATE 2 STATUS: PASS when diagram has >= 2 hierarchy levels, all roles sourced from
GATE 0, all types sourced from GATE 0.
FAIL when any role or type not established in GATE 0 appears.

---

## GATE 3: HEADCOUNT BY AREA

| Area     | Headcount | Decides | Escalates | Key Roles             |
|----------|-----------|---------|-----------|------------------------|
| [Area 1] | N         | ...     | ...       | [Role] (type-from-G0) |
| Total    | N         | —       | —         | —                      |

Requirements:
- Minimum 2 areas + Total row
- Decides and Escalates separate columns
- Key Roles annotated with types from GATE 0 only
- No type appearing here may differ from GATE 0 classification

GATE 3 STATUS: PASS when >= 2 areas, Total row present, types match GATE 0.

---

## GATE 4: OPERATING RHYTHM + COMMITTEE CHARTERS (INTERLEAVED)

Produce rhythm rows and committee charters in pairs. Rhythm row 1 → its charter.
Rhythm row 2 → its charter. Do not batch rows first and charters second.

Rhythm row schema:
| Cadence | Name | Participants | Purpose | Owner |
|---------|------|--------------|---------|-------|

Committee charter (5 fields required):
  COMMITTEE: [Name]
  Purpose:    [one sentence]
  Membership: [Role] (type-from-GATE-0), [Role] (type-from-GATE-0) — min 2 annotated
  Quorum:     N of M member roles
  Escalates to: [named destination]

Membership role types must match GATE 0. Role types not in GATE 0 are not acceptable.

Operating rhythm: minimum 3 distinct rows (one ROB/regular, one shiproom or gate,
one governance body). No merged rows.

After all pairs:
  PAIR-COUNT CHECK: [N] pairs produced. Rhythm table has [N] governance rows.
  Match: YES | NO

If NO: produce the missing charter before GATE 4 can close.

GATE 4 STATUS: PASS when pair count matches governance row count and all 5 charter
fields present for every committee.

---

## GATE 5: ORG EVOLUTION ROADMAP

| Trigger | Current State | Proposed Change | Reversibility |
|---------|---------------|-----------------|---------------|

Requirements:
- Minimum 2 rows
- Distinct trigger categories — no two headcount thresholds
- Valid categories: headcount, product-scope, market-event, incident-pattern,
  capability-gap

GATE 5 STATUS: PASS when >= 2 rows from distinct trigger categories.

---

## OUTPUT

Write the completed artifact to org-chart.md.

All gates must reach PASS status before the artifact is written. An artifact written
while any gate is in FAIL status is not acceptable output.
```

---

## V-04

**Axis:** Verification checkpoints
**Hypothesis:** Checkbox-format gates — where each pass condition is a discrete `[ ]` item that must be individually ticked before the STATUS line reads PASS — combined with a mandatory blocking verification loop placed before gate-status emission, prevent the silent-advance bypass where a model asserts "conditions met" without enumerating them.

```
You are executing the /org-chart skill. Generate an org structure for a product or
domain. Read .craft/roles/ first.

At every gate below, you must:
1. Complete all production steps for that gate
2. Run the blocking ANNOTATION-CHECK loop (scan all items; no advancing on assumption)
3. Tick each [ ] checkbox
4. Emit the gate STATUS line — PASS only when all boxes are checked

A gate whose STATUS line reads PASS without all checkboxes ticked is not acceptable.

---

## STEP 0: LOAD ROLES

Read all files in .craft/roles/. Extract every role name.

Emit:
  ROLES-LOADED: [role-name-1, role-name-2, ...]
or:
  ROLES-NOTE: No .craft/roles/ found. Proceeding with roles declared by user input.

ANNOTATION-CHECK: Verify the following before emitting gate status.
  [ ] ROLES-LOADED or ROLES-NOTE is present
  [ ] Every role name to be used later appears in this block
  [ ] No role is listed more than once

GATE 0 STATUS: PASS — proceed | FAIL — correct before continuing

---

## STEP 1: ROLE-TYPE CLASSIFICATION

Classify every role from ROLES-LOADED into {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.

  ROLE-TYPE-CLASSIFICATION
  | Role       | Type       | Rationale |
  |------------|------------|-----------|

Three-tier order: DECISION first, then EXECUTION, then ADVISORY/GOVERNANCE.

ANNOTATION-CHECK: Before emitting gate status, scan the classification table.
  [ ] Every role from ROLES-LOADED appears in the table
  [ ] Every type value is from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
  [ ] No role appears in more than one row
  [ ] Three-tier order respected

GATE 1 STATUS: PASS — proceed | FAIL — correct before continuing

---

## STEP 2: INERTIA ASSESSMENT

Four sub-sections required. Produces the VERDICT that determines whether structural
sections are generated. Must appear before any org diagram or structural output.

### 2a. Default-Position Statement (verbatim)

  DEFAULT POSITION: The team can operate flat. Formal org structure requires explicit
  justification. The burden of proof is on structure, not on flatness.

### 2b. Coordination Mechanism Table

| Mechanism | Type | Effectiveness (1–5) | Breaks At |
|-----------|------|---------------------|-----------|

Type closed set: {SYNC, ASYNC, ESCALATION, GOVERNANCE, SOCIAL}. Minimum 2 rows.

### 2c. Flat-Case Pressure Rating

  FLAT-CASE-PRESSURE: NONE | LOW | MEDIUM | HIGH | CRITICAL

### 2d. Verdict

  VERDICT: OPERATE-FLAT | STRUCTURE-WARRANTED
  Re-assessment trigger: [concrete condition]

ANNOTATION-CHECK: Before emitting gate status, verify each item.
  [ ] Default-position statement present verbatim before mechanism table
  [ ] Mechanism table has >= 2 rows
  [ ] All Type values in mechanism table from closed set
  [ ] FLAT-CASE-PRESSURE emitted with value from closed set
  [ ] VERDICT emitted as OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger states a concrete condition

GATE 2 STATUS: PASS — proceed | FAIL — correct before continuing

If VERDICT = OPERATE-FLAT: for each structural section (Org Diagram, Headcount,
Operating Rhythm, Committee Charters, Org Evolution Roadmap), emit:

  [SECTION NAME] — ABSENT
  Reason: Flat verdict taken. Not produced.
  NOT an acceptable substitute: "simplified hierarchy," "lightweight structure,"
  or any compressed-hierarchy alternative.

Then emit:
  ARTIFACT END. No content follows this line.

No content may appear after ARTIFACT END. This is a structural halt.

If VERDICT = STRUCTURE-WARRANTED: proceed to Step 3.

---

## STEP 3: ORG DIAGRAM

Draw ASCII org chart. Minimum 2 hierarchy levels. All roles from ROLES-LOADED.
Committees as distinct nodes. Roles annotated with type from Step 1.

ANNOTATION-CHECK: Before emitting gate status, scan the diagram.
  [ ] Diagram has >= 2 hierarchy levels
  [ ] Every role in the diagram appears in ROLES-LOADED
  [ ] Every role type annotation matches Step 1 classification
  [ ] At least one committee appears as a distinct node
  [ ] Diagram follows after Step 2 with STRUCTURE-WARRANTED verdict

GATE 3 STATUS: PASS — proceed | FAIL — correct before continuing

---

## STEP 4: HEADCOUNT BY AREA

| Area     | Headcount | Decides | Escalates | Key Roles          |
|----------|-----------|---------|-----------|--------------------|
| [Area 1] | N         | ...     | ...       | [Role] (type)      |
| Total    | N         | —       | —         | —                  |

ANNOTATION-CHECK: Before emitting gate status.
  [ ] >= 2 area rows present (excluding Total)
  [ ] Total row present
  [ ] Decides and Escalates are separate columns (not merged)
  [ ] Every Key Role annotated with (type) from Step 1
  [ ] No role appears in Key Roles that was not in ROLES-LOADED

GATE 4 STATUS: PASS — proceed | FAIL — correct before continuing

---

## STEP 5: OPERATING RHYTHM + COMMITTEE CHARTERS (INTERLEAVED)

Produce rhythm row 1 → its charter. Rhythm row 2 → its charter. And so on.
Do not batch all rows first and all charters second.

Rhythm row schema:
| Cadence | Name | Participants | Purpose | Owner |

Charter schema (5 fields required):
  COMMITTEE: [Name]
  Purpose:    [one sentence]
  Membership: [Role] (type), [Role] (type) — minimum 2 annotated roles
  Quorum:     N of M member roles
  Escalates to: [named destination]

After all pairs:
  PAIR-COUNT CHECK: [N] pairs produced. Rhythm table has [N] governance rows.
  Match: YES | NO

If NO: produce missing charter before proceeding.

ANNOTATION-CHECK: Before emitting gate status.
  [ ] >= 3 distinct rhythm rows (ROB/regular, shiproom/gate, governance)
  [ ] No merged rows in rhythm table
  [ ] Every charter has all 5 fields
  [ ] Quorum is in "N of M member roles" fraction form for every charter
  [ ] Escalates names a concrete destination in every charter
  [ ] Every Membership role appears in ROLES-LOADED
  [ ] Pair count matches governance row count (PAIR-COUNT CHECK = YES)
  [ ] Rhythm rows and charters are interleaved, not batched

GATE 5 STATUS: PASS — proceed | FAIL — correct before continuing

---

## STEP 6: ORG EVOLUTION ROADMAP

| Trigger | Current State | Proposed Change | Reversibility |

ANNOTATION-CHECK: Before emitting gate status.
  [ ] >= 2 rows present
  [ ] No two rows use headcount as their trigger category
  [ ] All trigger categories from: {headcount, product-scope, market-event,
      incident-pattern, capability-gap}

GATE 6 STATUS: PASS — proceed | FAIL — correct before continuing

---

## OUTPUT

Write the completed artifact to org-chart.md only after all gates reach PASS status.
An artifact written while any gate is FAIL is not acceptable output.
```

---

## V-05

**Axis:** Combined
**Hypothesis:** Combining classification-first gate ordering (V-03), explicit default-flat declaration with ABSENT/STOP termination (V-01), two-site constraint enforcement for both diagram placement and role-name scope (V-01), interleaved rhythm-charter pairs with post-production count verification (V-03), and checkbox-format gates with blocking annotation checks (V-04) closes all known bypass paths simultaneously without any single axis dominating.

```
You are executing the /org-chart skill. Generate an org structure for a product or
domain. Execute the gates below in strict sequence. Each gate has a mandatory
ANNOTATION-CHECK that must complete before the gate STATUS line can read PASS.

THE TEAM CAN OPERATE FLAT. Structure is a cost, not a default. The burden of proof
is on org structure, not on flatness. Every gate below enforces this default.

---

## GATE 0: ROLE INVENTORY + TYPE CLASSIFICATION

This gate executes before any inertia assessment, structural decision, or diagram.
Role types established here are the only role types permitted in all subsequent gates.
No structural gate may reference a role type not established in this gate.

### 0a. Load Roles

Read all files in .craft/roles/. Extract every role name.

CONSTRAINT (two sites):
SITE 1 — slot order: ROLES-LOADED or ROLES-NOTE is the first block in the artifact.
SITE 2 — conditional rule: If any role name appears in any subsequent section, that
role name must be present in the ROLES-LOADED list declared here. A role name not
declared here is not acceptable in any later section.

Emit:
  ROLES-LOADED: [role-name-1, role-name-2, ...]
or:
  ROLES-NOTE: No .craft/roles/ found. Proceeding with roles declared by user input.

### 0b. Classify Every Role

Classify every role from ROLES-LOADED into the closed-set taxonomy:
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}

  ROLE-TYPE-CLASSIFICATION
  | Role       | Type       | Rationale |
  |------------|------------|-----------|

Three-tier order: DECISION roles first, then EXECUTION, then ADVISORY/GOVERNANCE.
No role type outside the closed set is permitted.

ANNOTATION-CHECK (blocking — gate is held open until this loop closes):
  [ ] ROLES-LOADED or ROLES-NOTE present as first block
  [ ] Every role that will appear in any later section is listed in ROLES-LOADED
  [ ] Every role from ROLES-LOADED appears in the classification table
  [ ] Every type value is from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
  [ ] Three-tier order respected (DECISION → EXECUTION → ADVISORY/GOVERNANCE)
  [ ] No role appears in more than one row

GATE 0 STATUS: PASS — proceed | FAIL — correct before continuing

---

## GATE 1: INERTIA ASSESSMENT

Uses role types from GATE 0 only. No new role types may be introduced here.
Must appear before any org diagram, headcount table, committee charter, or rhythm row.

CONSTRAINT (two sites):
SITE 1 — slot order: Inertia Assessment appears immediately after GATE 0.
SITE 2 — conditional rule: If any org diagram box or committee charter appears in
the artifact, a STRUCTURE-WARRANTED verdict must precede it. Producing structural
output without a preceding STRUCTURE-WARRANTED verdict is not acceptable.

### 1a. Default-Position Statement

Open with this statement verbatim:

  DEFAULT POSITION: The team can operate flat. Formal org structure requires explicit
  justification. The burden of proof is on structure, not on flatness.

Do not paraphrase, abbreviate, reorder, or move this statement. It must open the
Inertia Assessment before the mechanism table.

### 1b. Coordination Mechanism Table

Schema:
| Mechanism | Type | Effectiveness (1–5) | Breaks At |
|-----------|------|---------------------|-----------|

Type closed set: {SYNC, ASYNC, ESCALATION, GOVERNANCE, SOCIAL}. Minimum 2 rows.

### 1c. Flat-Case Pressure Rating

  FLAT-CASE-PRESSURE: NONE | LOW | MEDIUM | HIGH | CRITICAL

### 1d. Verdict

  VERDICT: OPERATE-FLAT | STRUCTURE-WARRANTED
  Re-assessment trigger: [concrete condition — headcount threshold, product event,
  or incident pattern — that would change this verdict]

ANNOTATION-CHECK (blocking — gate is held open until this loop closes):
  [ ] Default-position statement present verbatim before mechanism table
  [ ] Mechanism table has >= 2 rows
  [ ] All Type values in mechanism table from closed set
  [ ] No role type appears here that was not established in GATE 0
  [ ] FLAT-CASE-PRESSURE emitted with value from closed set
  [ ] VERDICT emitted as OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger states a concrete condition (not generic)

GATE 1 STATUS: PASS — proceed | FAIL — correct before continuing

---

## FLAT-VERDICT BRANCH

If VERDICT = OPERATE-FLAT:

For each of the following sections, emit the exact block below:

  GATE 2 (Org Diagram) — ABSENT
  Reason: Flat verdict taken in GATE 1. This section is not produced.
  NOT an acceptable substitute: "simplified hierarchy," "lightweight structure,"
  "interim arrangement," or any compressed-hierarchy alternative.

  GATE 3 (Headcount by Area) — ABSENT
  Reason: Flat verdict taken in GATE 1. This section is not produced.
  NOT an acceptable substitute: any reduced or summary headcount table.

  GATE 4 (Operating Rhythm + Charters) — ABSENT
  Reason: Flat verdict taken in GATE 1. This section is not produced.
  NOT an acceptable substitute: informal schedule, suggested meetings, or cadence
  outline.

  GATE 5 (Org Evolution Roadmap) — ABSENT
  Reason: Flat verdict taken in GATE 1. This section is not produced.
  NOT an acceptable substitute: future-state notes or contingency plans.

After the final ABSENT block, emit:

  ARTIFACT END. No content follows this line.

This is a structural halt. No content of any kind — not notes, not caveats, not
observations — may appear after ARTIFACT END. Producing content after this line is
not acceptable, even if that content is labeled as optional or supplementary.

If VERDICT = STRUCTURE-WARRANTED: proceed to GATE 2.

---

## GATE 2: ORG DIAGRAM

Requires GATE 0 types and GATE 1 STRUCTURE-WARRANTED verdict.

ASCII org chart requirements:
- Minimum 2 hierarchy levels
- All roles from ROLES-LOADED (GATE 0) only
- Role types drawn from GATE 0 — no new type assignments
- Committees as distinct nodes (not embedded in a role box)
- Roles annotated with (type) from GATE 0

Format:
  [Domain]
  │
  ├── [Area 1]
  │   ├── [Role A] (type-from-GATE-0)
  │   └── [Role B] (type-from-GATE-0)
  │
  └── [Committee: Name]
      └── [Role A]

ANNOTATION-CHECK (blocking):
  [ ] STRUCTURE-WARRANTED verdict is present before this diagram
  [ ] Diagram has >= 2 hierarchy levels
  [ ] Every role in the diagram appears in ROLES-LOADED
  [ ] Every role type annotation matches GATE 0 classification exactly
  [ ] At least one committee node is present
  [ ] No role or type introduced here that was not in GATE 0

GATE 2 STATUS: PASS — proceed | FAIL — correct before continuing

---

## GATE 3: HEADCOUNT BY AREA

Schema:
| Area     | Headcount | Decides | Escalates | Key Roles          |
|----------|-----------|---------|-----------|--------------------|
| [Area 1] | N         | ...     | ...       | [Role] (type)      |
| Total    | N         | —       | —         | —                  |

Decides and Escalates are required as separate columns. Do not merge them.
Key Roles annotated with (type) from GATE 0 only. No type from outside GATE 0.

ANNOTATION-CHECK (blocking):
  [ ] >= 2 area rows present (excluding Total row)
  [ ] Total row present
  [ ] Decides and Escalates are separate columns (not merged into one)
  [ ] Every Key Role annotated with (type) matching GATE 0
  [ ] No role in Key Roles that was not in ROLES-LOADED

GATE 3 STATUS: PASS — proceed | FAIL — correct before continuing

---

## GATE 4: OPERATING RHYTHM + COMMITTEE CHARTERS (INTERLEAVED)

Produce rhythm rows and committee charters in pairs:
- Rhythm row 1 → its charter immediately
- Rhythm row 2 → its charter immediately
- Continue until all governance rows are paired

Do not batch all rhythm rows first and all charters second. Each rhythm row must be
immediately followed by its charter before the next rhythm row is produced.

Rhythm row schema:
| Cadence | Name | Participants | Purpose | Owner |

Charter schema (all 5 fields required for every committee):
  COMMITTEE: [Name]
  Purpose:    [one sentence]
  Membership: [Role] (type-from-GATE-0), [Role] (type-from-GATE-0)
              — minimum 2 roles, each annotated with type from GATE 0
  Quorum:     N of M member roles
  Escalates to: [named destination — not "leadership," "management," or
                 "the team"; must name a real role or body]

Operating rhythm requirements:
- Minimum 3 distinct rows: one ROB or regular cadence, one shiproom or gate, one
  governance body
- No merged rows permitted
- Row types must be distinct (not three variants of the same cadence)

After all pairs are produced, emit this count verification:
  PAIR-COUNT CHECK: [N] pairs produced. Operating rhythm table has [N] governance
  rows. Match: YES | NO

If Match = NO: identify the missing charter by name and produce it before this gate
can close.

ANNOTATION-CHECK (blocking — gate is held open until this loop closes):
  [ ] >= 3 distinct rhythm rows present
  [ ] No merged rows in rhythm table
  [ ] Rhythm row types are distinct (ROB/regular, shiproom/gate, governance — one each)
  [ ] Every charter has all 5 required fields (COMMITTEE, Purpose, Membership, Quorum,
      Escalates to)
  [ ] Quorum is in "N of M member roles" fraction form for every charter
  [ ] Escalates names a concrete destination (not "leadership" or "management")
  [ ] Every Membership role appears in ROLES-LOADED
  [ ] Every Membership role type matches GATE 0 classification
  [ ] Rhythm rows and charters are interleaved (not batched)
  [ ] PAIR-COUNT CHECK emitted and Match = YES

GATE 4 STATUS: PASS — proceed | FAIL — correct before continuing

---

## GATE 5: ORG EVOLUTION ROADMAP

Schema:
| Trigger | Current State | Proposed Change | Reversibility |
|---------|---------------|-----------------|---------------|

Requirements:
- Minimum 2 rows
- Rows from distinct trigger categories — no two rows may both be headcount thresholds
- Valid trigger categories: headcount, product-scope, market-event, incident-pattern,
  capability-gap

ANNOTATION-CHECK (blocking):
  [ ] >= 2 rows present
  [ ] No two rows share the same trigger category
  [ ] All trigger categories from the valid set above

GATE 5 STATUS: PASS — proceed | FAIL — correct before continuing

---

## OUTPUT

Write the completed artifact to org-chart.md after all gates reach PASS status.

CONSTRAINT (two sites):
SITE 1 — slot order: The artifact is written only after GATE 5 STATUS = PASS.
SITE 2 — conditional rule: If org-chart.md is written with any gate in FAIL status,
that is not acceptable output. Correct the failing gate and re-emit.

An artifact that contains content after ARTIFACT END (flat-verdict path) is not
acceptable. An artifact missing any ABSENT block (flat-verdict path) is not
acceptable. An artifact written while any gate is in FAIL status is not acceptable.
```

---

### Variation summary

| Variation | Axis | Key structural signal | Primary criteria targeted |
|-----------|------|-----------------------|---------------------------|
| V-01 | Inertia framing | DEFAULT POSITION verbatim + ABSENT/STOP + two-site constraints | C-01, C-13, C-15, C-16, C-18 |
| V-02 | Output format | Inline example rows in every schema | C-11, C-04, C-05, C-06, C-09 |
| V-03 | Role sequence | GATE 0 = classification before any structural gate | C-20, C-08, C-03, C-04, C-05 |
| V-04 | Verification checkpoints | `[ ]` checkbox format + blocking ANNOTATION-CHECK at every gate | C-21, C-22, C-12, C-19 |
| V-05 | Combined | All axes: classification-first + default-flat + two-site + ABSENT/STOP + interleaved + count check + checkbox gates | C-01–C-22 (full coverage) |
