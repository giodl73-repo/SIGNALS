## corps-chart Skill Variations — Round 6 (Rubric v5)

---

## V-01 — Axis: Phrasing Register (Formal/Technical Imperative)

**Hypothesis:** Replacing descriptive prose rules with direct `EMIT:` / `PRODUCE:` / `VERIFY:` command syntax reduces ambiguity about what the model must output vs. what it must decide. Every structural requirement becomes an output command rather than a compliance expectation.

---

```markdown
You are generating an org-chart artifact for a product or domain.

INPUT SOURCES:
- Read all role files from `.craft/roles/` (if present). These are your ROLES-LOADED set.
- If `.craft/roles/` is absent or empty, ROLES-LOADED is empty; note this as ROLES-NOTE.
- The topic and domain context is provided by the user or inferred from the directory name.

---

## STEP 1 — ROLE CLASSIFICATION

EMIT a block with this exact header:

```
ROLE-TYPE-CLASSIFICATION
```

For every role in ROLES-LOADED, emit one line:
- `[role name] — (domain type)`
- domain type MUST be exactly one of: (strategic) | (operational) | (advisory) | (governance)
- No role may be omitted. No domain type outside the four-word vocabulary is permitted.

IMMEDIATELY AFTER the classification block, EMIT:

```
ROLE-NAME LOCK
```

List every role from ROLES-LOADED as a numbered enumeration. This list is the complete set of permitted role references for every section that follows. No role name may appear in any downstream section (diagram, tables, charters, inertia sub-sections) unless it appears in this lock list. Roles introduced after this point invalidate the document.

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

---

## STEP 2 — INERTIA ASSESSMENT

PRODUCE an Inertia Assessment with these four sub-sections in strict order:

**Sub-section 2a — Case for Staying Flat**
EMIT a mechanism table with columns: `Mechanism | Type | Why It Works Here`
- Minimum two rows.
- Type values MUST come from this closed vocabulary: span-of-control / direct-comms / shared-context / single-DRI / low-coordination-cost
- Do not introduce Type values outside this vocabulary.

**Sub-section 2b — How We Coordinate Today**
WRITE two to four sentences describing the current coordination pattern using roles from ROLE-NAME LOCK.

**Sub-section 2c — Rebuttal**
PRODUCE this exact four-field form, with each field label on its own line:

```
ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [a current coordination failure — not a growth projection]
WHY EXISTING MECHANISMS FAIL: [why the mechanisms in 2a do not absorb this failure]
RE-ASSESSMENT TRIGGER: [a concrete threshold: specific hire count, named milestone, or structural symptom]
```

VERIFY: `OBSERVABLE BREAKDOWN` must describe a failure that exists now. "As we scale..." is not a valid breakdown. Reject and rewrite if the breakdown is future-tense.

**Sub-section 2d — Verdict**
EMIT the verdict as follows:
- First line: `FLAT-CASE-PRESSURE: [rating] — [justification]`
  - rating MUST be exactly one of: Strong | Moderate | Weak | Negligible | Insufficient
- Second line: declare exactly one of `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
- Third line: `RE-ASSESSMENT TRIGGER: [threshold from 2c]`
  - Threshold must be concrete. "Revisit as the team grows" is not valid.

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

---

## STEP 3 — ASCII ORG DIAGRAM

PRODUCE an ASCII box/tree diagram.
- Minimum two hierarchy levels (e.g., Director-level above Area leads).
- Committees MUST appear as distinct labeled nodes — not embedded inside an area box.
- Every role name appearing in the diagram MUST match a name in ROLE-NAME LOCK exactly.
- Connect nodes with `|`, `├──`, `└──`, or equivalent ASCII connectors. No flat lists of names.

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

---

## STEP 4 — HEADCOUNT TABLE

PRODUCE a table with exactly these five columns: `Area | Headcount | Key Roles | Decides | Escalates`
- Minimum two area rows.
- Final row MUST be `**Total**` with the headcount sum.
- Key Roles cells: each role annotated as `[role name] ([domain type])` using types from ROLE-TYPE-CLASSIFICATION.
- Decides: what this area decides without escalation.
- Escalates: what this area must escalate and to whom.

VERIFY: `Decides` and `Escalates` are separate columns. A merged `Decision Scope` column does not satisfy this step.

## STEP 5 — OPERATING RHYTHM TABLE

PRODUCE a table with columns: `Cadence | Frequency | DRI / Owner | Purpose`
- Minimum three rows.
- Coverage MUST include: (a) a ROB meeting, (b) a shiproom or gate meeting, (c) a governance meeting.
- Do not merge two meetings into one row.
- DRI / Owner values MUST come from ROLE-NAME LOCK.

## STEP 6 — COMMITTEE CHARTERS

For every governance meeting in the rhythm table, PRODUCE a charter block with exactly these five fields:
- `Purpose:` — one sentence
- `Membership:` — list minimum two roles, each annotated `[role name] ([domain type])`
- `Decides:` — specific decisions this committee owns
- `Escalates:` — specific destinations for decisions outside scope (not "everything not listed under Decides")
- `Quorum:` — written as `[N] of [M] member roles required for binding decisions`

VERIFY: Every governance meeting in the rhythm table has a charter. Every charter has all five fields. Escalates names a destination.

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

## STEP 7 — ORG-ELEMENT REGISTER

EMIT a block with this exact header:

```
ORG-ELEMENT REGISTER
```

Populate all four categories:
- `cat-1 (Areas)` — list each area with headcount: `[area name]: [N] headcount`
- `cat-2 (Committees/Cadences)` — list each meeting/committee by name
- `cat-3 (Headcount)` — emit: `Total headcount: [N]`
- `cat-4 (DRI Roles)` — list each role that appears as DRI/Owner in the rhythm table

No category may be empty or missing.

## STEP 8 — ORG EVOLUTION ROADMAP

EMIT a block with this exact header immediately before the trigger table:

```
TRIGGER-TYPE VOCABULARY
Permitted Type values: headcount threshold | workload signal | structural symptom | milestone event
Constraint: no two consecutive rows may share the same Type value.
```

PRODUCE a trigger table with columns: `Trigger | Structural Change | Type`
- Minimum two rows.
- Row 1: a headcount threshold trigger. Type = `headcount threshold`.
- Row 2: a trigger from a DIFFERENT category. Valid alternatives: `workload signal` | `structural symptom` | `milestone event`.
- VERIFY: Two headcount threshold rows do not satisfy this step.

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

---

## STEP 9 — ANTI-PATTERN WATCH

EMIT a block with this exact header immediately before the Anti-Pattern Watch table:

```
CAT-N-CITATION-SCHEMA
Valid cat-N codes (drawn from ORG-ELEMENT REGISTER above):
  cat-1 = Areas
  cat-2 = Committees/Cadences
  cat-3 = Headcount
  cat-4 = DRI Roles
Mandatory prefix for every "Why It Applies Here" cell:
  [element name] (cat-N) — [explanation]
No cell may name an org element without this typed prefix.
```

PRODUCE an Anti-Pattern Watch table with columns: `Anti-Pattern | Why It Applies Here | Mitigation`
- Minimum two rows.
- Every `Why It Applies Here` cell MUST open with `[element name] (cat-N) —` using a valid cat-N code from the schema block.
- VERIFY: No cell names an area, committee, role, or headcount figure without the typed citation prefix.

---

OUTPUT FILE: Write the complete artifact to `org-chart.md` in the topic's simulation directory.
```

---

## V-02 — Axis: Lifecycle Emphasis (Phase Gate Explicitness)

**Hypothesis:** Treating each phase gate as a mandatory output token — with `EMIT THIS EXACT LINE:` syntax and a pre-gate checklist — prevents the silent omission that caused C-09, C-15, and C-17 to fail in V-01. Gates become checkpoints the model must satisfy before proceeding, not just organizational labels.

---

```markdown
You are generating an org-chart artifact for a product or domain.

Read all files in `.craft/roles/`. These become ROLES-LOADED. If absent, note ROLES-NOTE and continue.

---

## PHASE 1 — ROLE CLASSIFICATION AND LOCK

Write a `ROLE-TYPE-CLASSIFICATION` block. For each role in ROLES-LOADED assign exactly one domain type from this closed set: (strategic) | (operational) | (advisory) | (governance). List every role. Introduce no types outside this set.

Immediately after, write a `ROLE-NAME LOCK` block that enumerates every role as a numbered list. This enumeration governs the entire document: no role name may appear in any section below unless it is on this list.

**PRE-GATE CHECK — answer each before emitting the gate line:**
- [ ] Every role in ROLES-LOADED has exactly one domain type from the closed vocabulary
- [ ] ROLE-NAME LOCK lists all roles as a numbered enumeration
- [ ] No role in the lock list has a domain type not in the closed set

**EMIT THIS EXACT LINE:**
```
=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===
```

---

## PHASE 2 — INERTIA ASSESSMENT

The Inertia Assessment has four sub-sections.

**2a — Case for Staying Flat**
Write a mechanism table with columns `Mechanism | Type | Why It Works Here`. Minimum two rows. Type values only from: span-of-control | direct-comms | shared-context | single-DRI | low-coordination-cost.

**2b — How We Coordinate Today**
Two to four sentences. Reference at least one role from ROLE-NAME LOCK.

**2c — Rebuttal**
Write a four-field form with these exact labels in this exact order:
```
ROLE UNDER PRESSURE: [one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [a present-tense coordination failure, not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [why 2a mechanisms don't absorb this failure]
RE-ASSESSMENT TRIGGER: [specific hire count, named milestone, or observable structural symptom]
```

**2d — Verdict**
First line: `FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [justification]`
Second line: declare `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` (exactly one, no other text on this line).
Third line: repeat the RE-ASSESSMENT TRIGGER from 2c verbatim.

**PRE-GATE CHECK:**
- [ ] 2a mechanism table has >= 2 rows with Type values only from the closed vocabulary
- [ ] 2c has all four field labels present and populated
- [ ] 2c OBSERVABLE BREAKDOWN is present-tense, not "as we scale..."
- [ ] 2d FLAT-CASE-PRESSURE rating is from the closed set
- [ ] 2d declares exactly one verdict keyword

**EMIT THIS EXACT LINE:**
```
=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===
```

---

## PHASE 3 — ORG STRUCTURE DIAGRAM

Produce an ASCII org diagram showing at minimum two hierarchy levels. Committees appear as distinct labeled nodes — not embedded inside area boxes. Use `|`, `├──`, `└──` or equivalent connectors. No flat name lists.

Every role name in the diagram must match a name from ROLE-NAME LOCK exactly. Introduce no new role names.

**PRE-GATE CHECK:**
- [ ] Diagram shows >= 2 hierarchy levels
- [ ] At least one committee appears as a distinct labeled node (not embedded in an area box)
- [ ] All role names in diagram are in ROLE-NAME LOCK

**EMIT THIS EXACT LINE:**
```
=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===
```

---

## PHASE 4 — HEADCOUNT, RHYTHM, AND CHARTERS

**4a — Headcount Table**
Five columns exactly: `Area | Headcount | Key Roles | Decides | Escalates`
Minimum two area rows. Final row: `**Total**` with sum. Key Roles cells: `[role name] ([domain type])`. Decides and Escalates are separate columns — no merged `Decision Scope`.

**4b — Operating Rhythm Table**
Columns: `Cadence | Frequency | DRI / Owner | Purpose`
Minimum three rows. Must cover: (a) ROB, (b) shiproom or gate meeting, (c) governance meeting. No two meetings merged into one row. DRI/Owner values from ROLE-NAME LOCK only.

**4c — Committee Charters**
For every governance meeting in 4b, write a charter with exactly these five labeled fields:
- `Purpose:` one sentence
- `Membership:` >= 2 roles, each as `[role name] ([domain type])`
- `Decides:` specific owned decisions
- `Escalates:` named escalation destination (not "everything not listed under Decides")
- `Quorum:` `[N] of [M] member roles required for binding decisions`

**PRE-GATE CHECK:**
- [ ] Headcount table has exactly 5 columns including separate Decides and Escalates
- [ ] Rhythm table has >= 3 rows covering ROB, shiproom/gate, governance
- [ ] Every governance meeting in rhythm table has a charter
- [ ] Every charter has all five labeled fields
- [ ] Escalates in each charter names a destination

**EMIT THIS EXACT LINE:**
```
=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===
```

---

## PHASE 5 — ORG-ELEMENT REGISTER AND EVOLUTION

**5a — ORG-ELEMENT REGISTER**
Emit a block labeled `ORG-ELEMENT REGISTER` with all four categories:
- `cat-1 (Areas)` — each area with headcount: `[name]: [N] headcount`
- `cat-2 (Committees/Cadences)` — each meeting/committee by name
- `cat-3 (Headcount)` — `Total headcount: [N]`
- `cat-4 (DRI Roles)` — each role appearing as DRI/Owner in 4b

No category may be empty.

**5b — Org Evolution Roadmap**
Before the trigger table, emit this exact block:
```
TRIGGER-TYPE VOCABULARY
Permitted Type values: headcount threshold | workload signal | structural symptom | milestone event
Rule: no two consecutive rows may share the same Type value.
```

Then write a trigger table with columns `Trigger | Structural Change | Type`. Minimum two rows. Row 1 must be Type `headcount threshold`. Row 2 must be a different Type. Two headcount threshold rows fail this section.

**PRE-GATE CHECK:**
- [ ] ORG-ELEMENT REGISTER has all four categories populated
- [ ] TRIGGER-TYPE VOCABULARY block appears before the trigger table
- [ ] Trigger table has >= 2 rows
- [ ] Row 1 and Row 2 have different Type values

**EMIT THIS EXACT LINE:**
```
=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===
```

---

## PHASE 6 — ANTI-PATTERN WATCH

Before the Anti-Pattern Watch table, emit this exact block:
```
CAT-N-CITATION-SCHEMA
Valid cat-N codes from this document's ORG-ELEMENT REGISTER:
  cat-1 = Areas
  cat-2 = Committees/Cadences
  cat-3 = Headcount
  cat-4 = DRI Roles
Required prefix for every "Why It Applies Here" cell:
  [element name] (cat-N) — [explanation]
Cells that name an org element without this prefix fail the schema.
```

Write an Anti-Pattern Watch table with columns `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows. Every `Why It Applies Here` cell must open with `[element name] (cat-N) —` using a valid cat-N code.

**PRE-GATE CHECK:**
- [ ] CAT-N-CITATION-SCHEMA block appears before the table
- [ ] >= 2 rows
- [ ] Every "Why It Applies Here" cell opens with `[element name] (cat-N) —`
- [ ] No cat-N code is used that does not appear in the ORG-ELEMENT REGISTER

---

Save completed artifact to `org-chart.md`.
```

---

## V-03 — Axis: Inertia Framing (Front-Loaded, Conditional Structure)

**Hypothesis:** Framing all structural output as conditional on the inertia verdict — "you earn the right to draw the org chart by passing the flat-case test" — prevents premature structure generation and produces a more argued, evidence-linked Inertia Assessment. The rebuttal form should carry higher stakes when structure is optional rather than assumed.

---

```markdown
You are generating an org-chart artifact. Before drawing any structure, you must first determine whether structure is warranted. This document has a hard gate: the org diagram, headcount table, rhythm table, and charters are only written after the Inertia Assessment declares STRUCTURE-WARRANTED. If the verdict is CAN-OPERATE-FLAT, the document ends at the inertia phase.

Read all files in `.craft/roles/`. These are ROLES-LOADED. If absent, note ROLES-NOTE.

---

## STEP 1 — ROLE CLASSIFICATION

Write a `ROLE-TYPE-CLASSIFICATION` block. Assign every role in ROLES-LOADED exactly one domain type:
- (strategic) — sets direction and owns outcomes across areas
- (operational) — executes and delivers within a bounded scope
- (advisory) — provides input without decision authority
- (governance) — approves, controls, or creates accountability

No role is omitted. No type outside this four-word set is introduced.

Immediately after the classification block, write a `ROLE-NAME LOCK`:
> This is the complete enumeration of roles permitted in this document. Every role reference in every section below — diagram, tables, charters, inertia sub-sections — must match a name on this list exactly. Adding a new role name after this point is a document error.

List every role as a numbered enumeration.

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

---

## STEP 2 — INERTIA ASSESSMENT

**The inertia assessment is the primary question of this document.** Assume the status quo is correct until the rebuttal proves otherwise. Write each sub-section in order.

### 2a — Case for Staying Flat

Build the strongest possible case for not adding structure. Write a mechanism table:

| Mechanism | Type | Why It Works Here |
|-----------|------|-------------------|
| ... | ... | ... |

Type must be exactly one of: `span-of-control` | `direct-comms` | `shared-context` | `single-DRI` | `low-coordination-cost`. Minimum two rows. Do not introduce Type values outside this set.

Write one paragraph after the table explaining how these mechanisms combine to absorb today's coordination load.

### 2b — How We Coordinate Today

Describe the current coordination pattern in two to four sentences using specific roles from ROLE-NAME LOCK. Name the dominant mechanism (e.g., "The [role] serves as the single coordination point for...").

### 2c — Rebuttal

The rebuttal must break the case for staying flat using a specific role failure — not a growth projection. Write the rebuttal as a four-field form:

```
ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [a current, observable coordination failure — "as we scale" and "when we grow" are not valid; the failure must exist now]
WHY EXISTING MECHANISMS FAIL: [specifically which mechanism(s) from 2a do not absorb this failure, and why]
RE-ASSESSMENT TRIGGER: [a concrete measurable threshold: a specific hire count, a named milestone, or a structural symptom such as "two or more missed ship dates attributable to cross-area misalignment"]
```

The rebuttal earns structure. If the observable breakdown is hypothetical or future-tense, the rebuttal fails and the verdict must be CAN-OPERATE-FLAT regardless of team size.

### 2d — Verdict

```
FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [one-sentence justification]
```

Then declare exactly one of:
- `CAN-OPERATE-FLAT` — if the flat case mechanisms fully absorb the observable failures; stop here, do not write structure sections.
- `STRUCTURE-WARRANTED` — if the rebuttal identified an observable, un-absorbed failure in the roles from ROLE-NAME LOCK; continue to Step 3.

```
RE-ASSESSMENT TRIGGER: [verbatim from 2c]
```

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

*(If verdict is CAN-OPERATE-FLAT, the document ends here.)*

---

## STEP 3 — ORG STRUCTURE DIAGRAM

Draw an ASCII box/tree diagram. Minimum two hierarchy levels. Committees are distinct labeled nodes — not embedded in area boxes. Use `|`, `├──`, `└──` connectors. All role names must match ROLE-NAME LOCK exactly. Introduce no new names.

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

---

## STEP 4 — HEADCOUNT TABLE

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

Minimum two area rows. Final row `**Total**` with sum. Key Roles: `[role name] ([domain type])`. Decides and Escalates are separate columns.

## STEP 5 — OPERATING RHYTHM TABLE

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Minimum three rows covering: (a) ROB, (b) shiproom or gate meeting, (c) governance meeting. DRI/Owner from ROLE-NAME LOCK only. Do not merge two meetings into one row.

## STEP 6 — COMMITTEE CHARTERS

For every governance meeting in the rhythm table:

**[Committee Name]**
- Purpose: [one sentence]
- Membership: [>= 2 roles as `[role name] ([domain type])`]
- Decides: [specific owned decisions]
- Escalates: [named destination — not "everything not listed under Decides"]
- Quorum: [N] of [M] member roles required for binding decisions

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

## STEP 7 — ORG-ELEMENT REGISTER

```
ORG-ELEMENT REGISTER
cat-1 (Areas): [each area with headcount]
cat-2 (Committees/Cadences): [each meeting by name]
cat-3 (Headcount): Total headcount: [N]
cat-4 (DRI Roles): [each DRI/Owner role from rhythm table]
```

All four categories required. None may be empty.

## STEP 8 — ORG EVOLUTION ROADMAP

Before the trigger table, emit:
```
TRIGGER-TYPE VOCABULARY
Permitted Type values: headcount threshold | workload signal | structural symptom | milestone event
Constraint: no two consecutive rows may share the same Type value.
```

| Trigger | Structural Change | Type |
|---------|------------------|------|

Minimum two rows. Row 1: `headcount threshold`. Row 2: different Type. Two headcount threshold rows fail this section.

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

---

## STEP 9 — ANTI-PATTERN WATCH

Before the table, emit:
```
CAT-N-CITATION-SCHEMA
cat-1 = Areas | cat-2 = Committees/Cadences | cat-3 = Headcount | cat-4 = DRI Roles
Mandatory prefix: [element name] (cat-N) — [explanation]
```

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|

Minimum two rows. Every `Why It Applies Here` cell opens with `[element name] (cat-N) —`.

---

Save artifact to `org-chart.md`.
```

---

## V-04 — Axis: Output Format (Schema-First / Fill-in-Template)

**Hypothesis:** Providing literal blank-row table templates before instructing the model to fill them eliminates the column-divergence failure mode (e.g., merged `Decision Scope` column). When the template exists before the instruction, the model fills rather than invents format.

---

```markdown
You are generating an org-chart artifact for a product or domain.

Read `.craft/roles/` and collect all role files as ROLES-LOADED. If absent, note ROLES-NOTE.

Each section below provides a template. Your task is to populate the template — do not alter column names, block headers, or field labels.

---

## STEP 1 — ROLE CLASSIFICATION

Populate this template. Add one row per role in ROLES-LOADED.

```
ROLE-TYPE-CLASSIFICATION
| Role Name | Domain Type |
|-----------|-------------|
| [role]    | [type]      |

Domain type vocabulary (use exactly one per row):
  (strategic) | (operational) | (advisory) | (governance)
```

Then populate this template immediately after:

```
ROLE-NAME LOCK
This is the complete set of role names permitted in this document.
1. [role name]
2. [role name]
...
No role reference in any section below may introduce a name not on this list.
```

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

---

## STEP 2 — INERTIA ASSESSMENT

Populate each sub-section template in order.

**2a — Case for Staying Flat**

```
| Mechanism | Type | Why It Works Here |
|-----------|------|-------------------|
| [mech]    | [type from: span-of-control / direct-comms / shared-context / single-DRI / low-coordination-cost] | [why] |
| [mech]    | [type]              | [why] |
```

(Add rows as needed. Minimum two. No Type value outside the vocabulary.)

**2b — How We Coordinate Today**

[2-4 sentences describing current coordination using roles from ROLE-NAME LOCK]

**2c — Rebuttal**

Populate this exact form:

```
ROLE UNDER PRESSURE: [role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [present-tense coordination failure — not "as we scale"]
WHY EXISTING MECHANISMS FAIL: [which mechanism(s) from 2a fail and why]
RE-ASSESSMENT TRIGGER: [specific hire count, named milestone, or structural symptom]
```

**2d — Verdict**

```
FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [justification]
[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
RE-ASSESSMENT TRIGGER: [verbatim from 2c]
```

(Choose exactly one keyword. No additional text on the verdict line.)

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

---

## STEP 3 — ASCII DIAGRAM

Draw an org diagram using this layout convention:
```
[Level 1 Role / Area]
├── [Level 2 Role / Area]
│   └── [Level 3 if needed]
└── [Committee Node — committees are NEVER embedded in area boxes]
    └── [Committee member or cadence]
```

Rules:
- All role names must match ROLE-NAME LOCK exactly
- Committees appear as distinct labeled nodes at whatever level fits the structure
- Minimum two hierarchy levels

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

---

## STEP 4 — HEADCOUNT TABLE

Populate this template exactly. Do not rename columns.

```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [area name] | [N] | [role] ([domain type]), [role] ([domain type]) | [what area decides] | [what area escalates and to whom] |
| [area name] | [N] | ... | ... | ... |
| **Total** | [sum] | | | |
```

(Add rows for each area. Minimum two area rows before Total.)

## STEP 5 — OPERATING RHYTHM TABLE

Populate this template. Minimum three rows. Do not merge meetings.

```
| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| ROB | [freq] | [role from ROLE-NAME LOCK] | [purpose] |
| [Shiproom or Gate Meeting] | [freq] | [role] | [purpose] |
| [Governance Meeting] | [freq] | [role] | [purpose] |
```

(Add rows as needed. DRI / Owner values from ROLE-NAME LOCK only.)

## STEP 6 — COMMITTEE CHARTERS

For each governance meeting row in Step 5, populate one charter. Do not alter field labels.

```
**[Committee Name]**
Purpose: [one sentence]
Membership: [role name] ([domain type]), [role name] ([domain type]) [add roles as needed, minimum two]
Decides: [specific decisions owned by this committee]
Escalates: [named destination for out-of-scope decisions — not "everything not listed under Decides"]
Quorum: [N] of [M] member roles required for binding decisions
```

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

## STEP 7 — ORG-ELEMENT REGISTER

Populate this register. Every category must be filled.

```
ORG-ELEMENT REGISTER
cat-1 (Areas):
  [area name]: [N] headcount
  [area name]: [N] headcount
  ...
cat-2 (Committees/Cadences):
  [committee or cadence name]
  [committee or cadence name]
  ...
cat-3 (Headcount):
  Total headcount: [N]
cat-4 (DRI Roles):
  [role name]
  [role name]
  ...
```

## STEP 8 — ORG EVOLUTION ROADMAP

First, emit the vocabulary block exactly as shown. Then fill the table.

```
TRIGGER-TYPE VOCABULARY
Permitted Type values: headcount threshold | workload signal | structural symptom | milestone event
Constraint: no two consecutive rows may share the same Type value.
```

```
| Trigger | Structural Change | Type |
|---------|------------------|------|
| [headcount threshold trigger] | [structural change] | headcount threshold |
| [different-category trigger] | [structural change] | [workload signal | structural symptom | milestone event] |
```

(Minimum two rows. Row 1 Type must be `headcount threshold`. Row 2 Type must differ.)

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

---

## STEP 9 — ANTI-PATTERN WATCH

First, emit the schema block exactly as shown. Then fill the table.

```
CAT-N-CITATION-SCHEMA
Valid cat-N codes (from ORG-ELEMENT REGISTER above):
  cat-1 = Areas
  cat-2 = Committees/Cadences
  cat-3 = Headcount
  cat-4 = DRI Roles
Required prefix for "Why It Applies Here" cells:
  [element name] (cat-N) — [explanation]
```

```
| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [anti-pattern name] | [element name] (cat-N) — [why it applies] | [mitigation] |
| [anti-pattern name] | [element name] (cat-N) — [why it applies] | [mitigation] |
```

(Minimum two rows. Every "Why It Applies Here" cell must use the `[element name] (cat-N) —` prefix.)

---

Save to `org-chart.md`.
```

---

## V-05 — Axis: Combined (Phase Gate Explicitness + Schema-First Templates)

**Hypothesis:** V-02's pre-gate checklists prevent silent section omission; V-04's fill-in templates prevent format deviation. Combined, they close the largest gap class: structural omissions that manifest as missing sections AND format failures that manifest as wrong columns. The combination should produce the highest C-08, C-17 compliance (gate presence) and C-03, C-09, C-15, C-16 compliance (format fidelity) simultaneously.

---

```markdown
You are generating an org-chart artifact for a product or domain.

Read `.craft/roles/` to collect ROLES-LOADED. If absent, note ROLES-NOTE and continue.

This document has nine phases. Each phase ends with a pre-gate checklist you must satisfy before emitting the gate line. Emit every gate line verbatim. Do not skip a phase.

---

## PHASE 1 — ROLE CLASSIFICATION AND LOCK

Populate these two templates in order.

**Template 1: ROLE-TYPE-CLASSIFICATION**
```
ROLE-TYPE-CLASSIFICATION
| Role Name | Domain Type |
|-----------|-------------|
| [role]    | [type]      |
```
Domain type vocabulary (closed): `(strategic)` | `(operational)` | `(advisory)` | `(governance)`
Every role in ROLES-LOADED gets exactly one. No unlisted types.

**Template 2: ROLE-NAME LOCK**
```
ROLE-NAME LOCK
Complete enumeration of roles permitted in this document:
1. [role name]
2. [role name]
...
Every section below checks against this list. No new role names after this point.
```

**PRE-GATE CHECK — satisfy all before emitting gate:**
- [ ] All ROLES-LOADED appear in classification table with a type from the closed vocabulary
- [ ] ROLE-NAME LOCK contains exactly the same roles as the classification table
- [ ] No domain type outside the four-word set appears in the classification

**EMIT:**
```
=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===
```

---

## PHASE 2 — INERTIA ASSESSMENT

Four sub-sections. Populate each template.

**2a — Case for Staying Flat**
```
| Mechanism | Type | Why It Works Here |
|-----------|------|-------------------|
| [mech 1]  | [type from closed set] | [why] |
| [mech 2]  | [type from closed set] | [why] |
```
Type vocabulary (closed): `span-of-control` | `direct-comms` | `shared-context` | `single-DRI` | `low-coordination-cost`

**2b — How We Coordinate Today**
[2–4 sentences. Name at least one role from ROLE-NAME LOCK and identify the dominant coordination mechanism.]

**2c — Rebuttal**
```
ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [present-tense failure — not "as we scale" or future projection]
WHY EXISTING MECHANISMS FAIL: [which 2a mechanism(s) fail and the specific reason]
RE-ASSESSMENT TRIGGER: [specific hire count, named milestone, or structural symptom — not "revisit as the team grows"]
```

**2d — Verdict**
```
FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [justification]
[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
RE-ASSESSMENT TRIGGER: [verbatim from 2c RE-ASSESSMENT TRIGGER field]
```

**PRE-GATE CHECK:**
- [ ] 2a has >= 2 rows; all Type values from closed vocabulary
- [ ] 2c: all four field labels present; ROLE UNDER PRESSURE names a role from ROLE-NAME LOCK
- [ ] 2c: OBSERVABLE BREAKDOWN is present-tense, not future-conditional
- [ ] 2c: RE-ASSESSMENT TRIGGER is concrete (hire count, milestone, or symptom)
- [ ] 2d: FLAT-CASE-PRESSURE rating is from the closed set
- [ ] 2d: exactly one verdict keyword declared

**EMIT:**
```
=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===
```

---

## PHASE 3 — ASCII ORG DIAGRAM

Draw the org diagram:
```
[Top-level role or area]
├── [Area or role]
│   └── [Sub-role if applicable]
└── [Committee — as a distinct labeled node, never embedded in an area box]
    └── [Key committee participant role]
```

All role names must appear in ROLE-NAME LOCK exactly. Minimum two hierarchy levels.

**PRE-GATE CHECK:**
- [ ] >= 2 hierarchy levels visible in diagram
- [ ] >= 1 committee appears as a distinct labeled node
- [ ] All named roles in diagram are in ROLE-NAME LOCK
- [ ] No committee name is embedded inside an area box

**EMIT:**
```
=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===
```

---

## PHASE 4 — HEADCOUNT, RHYTHM, CHARTERS

**4a — Headcount Table** (populate, do not rename columns)
```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [area] | [N] | [role] ([type]), [role] ([type]) | [owned decisions] | [escalations + destination] |
| [area] | [N] | ... | ... | ... |
| **Total** | [sum] | | | |
```

**4b — Operating Rhythm Table** (minimum three rows, do not merge)
```
| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| ROB | [freq] | [role from ROLE-NAME LOCK] | [purpose] |
| [Shiproom or Gate] | [freq] | [role] | [purpose] |
| [Governance Meeting] | [freq] | [role] | [purpose] |
```

**4c — Committee Charters** (one charter per governance row in 4b)
```
**[Committee Name]**
Purpose: [one sentence]
Membership: [role] ([domain type]), [role] ([domain type]) [minimum two]
Decides: [specific owned decisions]
Escalates: [named destination — not "everything not listed under Decides"]
Quorum: [N] of [M] member roles required for binding decisions
```

**PRE-GATE CHECK:**
- [ ] Headcount table has exactly 5 columns: Area, Headcount, Key Roles, Decides, Escalates
- [ ] No merged `Decision Scope` column
- [ ] **Total** row present with sum
- [ ] Rhythm table has >= 3 rows; ROB, shiproom/gate, and governance covered
- [ ] All DRI/Owner values in rhythm table are in ROLE-NAME LOCK
- [ ] Every governance cadence row has a matching charter
- [ ] Every charter has: Purpose, Membership, Decides, Escalates, Quorum (all five)
- [ ] Escalates in each charter names a destination
- [ ] Quorum uses fraction format `[N] of [M] member roles`

**EMIT:**
```
=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===
```

---

## PHASE 5 — ORG-ELEMENT REGISTER AND EVOLUTION ROADMAP

**5a — ORG-ELEMENT REGISTER** (all four categories required)
```
ORG-ELEMENT REGISTER
cat-1 (Areas):
  [area name]: [N] headcount
  ...
cat-2 (Committees/Cadences):
  [committee/cadence name]
  ...
cat-3 (Headcount):
  Total headcount: [N]
cat-4 (DRI Roles):
  [role name]
  ...
```

**5b — Org Evolution Roadmap**
Emit this exact vocabulary block first:
```
TRIGGER-TYPE VOCABULARY
Permitted Type values: headcount threshold | workload signal | structural symptom | milestone event
Constraint: no two consecutive rows may share the same Type value.
```

Then populate the trigger table:
```
| Trigger | Structural Change | Type |
|---------|------------------|------|
| [headcount trigger description] | [structural change] | headcount threshold |
| [different-category trigger] | [structural change] | [workload signal | structural symptom | milestone event] |
```

**PRE-GATE CHECK:**
- [ ] ORG-ELEMENT REGISTER has all four cat-N categories populated
- [ ] No category is empty
- [ ] TRIGGER-TYPE VOCABULARY block appears before trigger table
- [ ] Trigger table has >= 2 rows
- [ ] Row 1 Type = `headcount threshold`; Row 2 Type differs from Row 1

**EMIT:**
```
=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===
```

---

## PHASE 6 — ANTI-PATTERN WATCH

Emit this exact schema block first:
```
CAT-N-CITATION-SCHEMA
Valid cat-N codes (from this document's ORG-ELEMENT REGISTER):
  cat-1 = Areas
  cat-2 = Committees/Cadences
  cat-3 = Headcount
  cat-4 = DRI Roles
Required prefix for every "Why It Applies Here" cell:
  [element name] (cat-N) — [explanation]
Any cell that names an org element without this prefix fails the schema.
```

Then populate the table:
```
| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [anti-pattern] | [element name] (cat-N) — [why it applies] | [mitigation] |
| [anti-pattern] | [element name] (cat-N) — [why it applies] | [mitigation] |
```

**FINAL CHECK:**
- [ ] CAT-N-CITATION-SCHEMA block appears before the table
- [ ] >= 2 rows
- [ ] Every "Why It Applies Here" cell opens with `[element name] (cat-N) —`
- [ ] All cat-N codes used appear in the ORG-ELEMENT REGISTER

---

Save to `org-chart.md`.
```

---

## Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register — formal/technical imperative | `EMIT:` / `VERIFY:` command syntax eliminates compliance ambiguity |
| V-02 | Lifecycle emphasis — phase gate explicitness | Pre-gate checklists prevent silent section omission |
| V-03 | Inertia framing — front-loaded, conditional | Conditional structure framing produces higher-quality argued rebuttal |
| V-04 | Output format — schema-first fill-in templates | Blank templates before instructions prevent column divergence |
| V-05 | Combined — V-02 gates + V-04 templates | Gate checklists + fill-in templates close both omission and format failure simultaneously |
