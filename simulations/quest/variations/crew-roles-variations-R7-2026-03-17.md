# crew-roles Skill Variations V-01 through V-05

---

## V-01 — Baseline: Explicit Phase Boundaries
**Variation axis**: Lifecycle emphasis — each phase is a numbered, named block with explicit entry condition, work product, and exit gate
**Hypothesis**: Fully named and numbered phases with mandatory named outputs reduce elision; the model cannot skip a structural artifact if the next phase names it as a prerequisite.

---

```
Generate a typed role registry for the domain described in the input.
Roles are written to `.roles/{area}/`, one file per role.
Follow the phases below in order. Do not begin a phase until its predecessor's
exit condition is satisfied.

---

## PHASE 1 — Bucketed Vocabulary Extraction

Read the input. Extract domain vocabulary and assign every term to exactly one
of three Q-domain buckets. Do not produce a flat list.

Output this block verbatim before proceeding:

```
PHASE 1 OUTPUT — BUCKETED VOCABULARY
=====================================
Current-System Terms:
  [term], [term], ...

Migration-Cost Terms:
  [term], [term], ...

User-Habit Terms:
  [term], [term], ...
```

Exit condition: All three buckets are non-empty and every extracted term
appears in exactly one bucket.

---

## PHASE 2 — Inertia Pre-Characterization

Answer the three Q-dimension questions using only terms drawn from the
corresponding Phase 1 bucket.

  Q1 (Current-System): What is the name of the current system?
        Answer must reference a Current-System Term from Phase 1.

  Q2 (Migration-Cost): What are the primary migration costs?
        Answer must reference a Migration-Cost Term from Phase 1.

  Q3 (User-Habit): What user habits are at risk of disruption?
        Answer must reference a User-Habit Term from Phase 1.

After answering, produce the domain-alignment audit table:

```
PHASE 2 AUDIT TABLE
===================
Q-Number | Term Used | Expected Domain     | Match YES/NO
---------|-----------|---------------------|-------------
Q1       | [term]    | Current-System      | YES / NO
Q2       | [term]    | Migration-Cost      | YES / NO
Q3       | [term]    | User-Habit          | YES / NO
```

If any row shows NO:
  1. Replace the non-matching term with a term from the correct bucket.
  2. Restart the audit table from Q1 — do not re-score only the replaced row.
  3. Re-evaluate all three rows as a unit.
  4. Repeat until all three rows show YES.

Exit condition: The completed audit table shows YES in every row after
full-table evaluation. Phase 2 is not complete until this condition holds.

---

## PHASE 3 — Frame Fill

The inertia-advocate `orientation.frame` uses this template:

  "The current approach relies on [Q1 current system]. Adopting this feature
  requires [Q2 migration cost]. Until those costs are justified, the risk
  outweighs the benefit."

Fill both slots from the Phase 2 answers. Produce the following output:

```
PHASE 3 OUTPUT — FRAME FILL
============================
Q1 slot ← Phase 2 Q1: [verbatim Phase 2 Q1 answer]
Q2 slot ← Phase 2 Q2: [verbatim Phase 2 Q2 answer]

Completed frame:
"The current approach relies on [filled Q1 value]. Adopting this feature
requires [filled Q2 value]. Until those costs are justified, the risk
outweighs the benefit."
```

Verification: Confirm Q1 slot is drawn from Q1 answer and Q2 slot is drawn
from Q2 answer. A slot populated from the wrong Q answer is a blocking error.
Do not proceed until slot-source binding is confirmed.

Exit condition: Both slots carry explicit source citations and the binding
check passes.

---

## PHASE 4 — Pre-Write Scope Audit

Before writing any role files, survey the planned role set and assign a scope
value to each planned role.

```
PHASE 4 OUTPUT — PRE-WRITE SCOPE PLAN
=======================================
Planned Role          | Scope
----------------------|---------------
[role name]           | [team / cross-team / org]
[role name]           | [team / cross-team / org]
...
```

Count distinct scope values. If all planned roles share the same scope value,
revise the plan so that at least 2 distinct scope values are present before
any role file is written.

Exit condition: The scope plan contains >= 2 distinct scope values.

---

## PHASE 5 — Role Writing

Write each role file to `.roles/{area}/{role-slug}.md`.
Every role file must contain all five fields:

  - name
  - orientation (frame, verify, simplify)
  - expertise (summary, relevance)
  - collaborates_with
  - scope

Field constraints:
  - `orientation.verify` entries are questions ending with `?`
  - `orientation.simplify` entries are imperatives
  - `expertise.relevance` references at least one term from the Phase 1 vocabulary
  - The inertia-advocate `orientation.frame` is the completed frame string from Phase 3
  - Minimum 3 roles, including the inertia-advocate
  - Roles span at least 3 distinct perspective categories

Inertia-advocate `orientation.frame`:
  Use the completed frame string from Phase 3 output exactly.

Inertia-advocate `orientation.verify` must reference at least 2 of:
  - The current system named in Q1
  - The migration cost named in Q2
  - The user habit named in Q3

---

## PHASE 6 — Verification Gate

All checks below must PASS before delivery. This gate is not optional and
is not satisfied by partial completion. Produce this block in output:

```
VERIFICATION GATE
==================
CHECK 1 — Registry Summary Table
  Role | Orientation Frame (first 8 words) | Scope | Collaborates With
  -----|-----------------------------------|-------|------------------
  [every role listed]

  PASS / FAIL

CHECK 2 — Orphan Reference Check
  For every collaborates_with value: does a file with that name exist
  in the registry? List any missing names.
  PASS / FAIL

CHECK 3 — Scope-Gradient Check
  How many distinct scope values appear? Must be >= 2.
  PASS / FAIL

CHECK 4 — Vocabulary Coverage Check
  For every role: does expertise.relevance reference a Phase 1 vocabulary term?
  List any roles failing this check.
  PASS / FAIL

GATE RESULT: PASS (all four checks pass) / BLOCKED (list failing checks)
```

If BLOCKED: resolve each failing check and re-run the gate before delivering output.
```

---

## V-02 — Inertia-First Role Sequence
**Variation axis**: Role sequence — the inertia-advocate is designed and written before any other role; Phase 2/3 outputs feed directly into the first role written
**Hypothesis**: Designing the inertia-advocate first anchors the current-system framing into the registry before other roles are planned; subsequent roles are positioned relative to a concrete adversarial stance rather than a generic domain.

---

```
Generate a typed role registry for the domain described in the input.
Roles are written to `.roles/{area}/`, one file per role.

The inertia-advocate is written first. All other roles are planned after
the inertia-advocate is complete. This sequence is mandatory.

---

## STEP 1 — Extract Bucketed Vocabulary

Read the input and produce three named Q-domain buckets. Every extracted term
belongs to exactly one bucket.

```
BUCKETED VOCABULARY
====================
Current-System Terms:  [term], [term], ...
Migration-Cost Terms:  [term], [term], ...
User-Habit Terms:      [term], [term], ...
```

All three buckets must be non-empty before proceeding.

---

## STEP 2 — Characterize the Inertia Position

Answer three questions. Each answer must reference a term from the
corresponding bucket.

  Q1 — Current System (draw from Current-System Terms bucket):
       Name the system already in place.

  Q2 — Migration Cost (draw from Migration-Cost Terms bucket):
       Name the primary cost of changing.

  Q3 — User Habit (draw from User-Habit Terms bucket):
       Name the habit that would be disrupted.

After answering, produce the domain-alignment audit table:

```
INERTIA CHARACTERIZATION AUDIT
================================
Q-Number | Term Used | Expected Domain  | Match YES/NO
---------|-----------|------------------|-------------
Q1       | [term]    | Current-System   | YES / NO
Q2       | [term]    | Migration-Cost   | YES / NO
Q3       | [term]    | User-Habit       | YES / NO
```

Any NO row: replace the term with a correct-bucket term, then restart the
table from Q1. Evaluate all three rows as a unit. Repeat until all rows
show YES. Do not close Step 2 with any NO row present.

---

## STEP 3 — Fill the Inertia Frame

Template:
  "The current approach relies on [Q1 current system]. Adopting this feature
  requires [Q2 migration cost]. Until those costs are justified, the risk
  outweighs the benefit."

```
FRAME FILL
===========
Q1 slot ← Step 2 Q1: [verbatim Q1 answer]
Q2 slot ← Step 2 Q2: [verbatim Q2 answer]

Completed frame:
"The current approach relies on [Q1 value]. Adopting this feature requires
[Q2 value]. Until those costs are justified, the risk outweighs the benefit."

Slot-source binding check:
  Q1 slot drawn from Q1 answer? YES / NO
  Q2 slot drawn from Q2 answer? YES / NO
```

Both binding checks must show YES. A mismatch is a blocking error.

---

## STEP 4 — Write the Inertia-Advocate Role

Write `.roles/{area}/inertia-advocate.md` now, before planning any
other role.

Required fields:
  - name: "Inertia Advocate"
  - orientation:
      frame: [completed frame string from Step 3 — verbatim]
      verify:
        - [question referencing Q1 current system or Q2 migration cost] ?
        - [question referencing Q3 user habit] ?
        - [question referencing at least one more Q1/Q2/Q3 dimension] ?
      simplify:
        - [imperative reducing scope to core migration concern]
        - [imperative surfacing the habit disruption risk]
  - expertise:
      summary: [domain-grounded summary]
      relevance: [references at least one Phase 1 vocabulary term]
  - collaborates_with: [at least one other role — resolve after other roles
                        are written; mark as PENDING for now]
  - scope: [team / cross-team / org]

`orientation.verify` entries end with `?`.
`orientation.simplify` entries are imperatives.
At least 2 of the 3 verify questions reference Q1, Q2, or Q3 answers.

---

## STEP 5 — Plan Remaining Roles with Scope Audit

Now that the inertia-advocate exists, plan the remaining roles.

```
REMAINING ROLE PLAN
====================
Role Name             | Perspective Category | Planned Scope
----------------------|----------------------|---------------
[role]                | [product/technical/domain/etc.] | [scope]
[role]                | ...                  | ...
```

Requirements:
  - At least 2 more roles beyond the inertia-advocate (minimum total: 3)
  - At least 3 distinct perspective categories across all roles
  - At least 2 distinct scope values across all roles (including inertia-advocate)

If distinct scope values < 2: revise the plan before writing. This is a
structural gate, not a soft instruction.

---

## STEP 6 — Write Remaining Roles

Write each planned role to `.roles/{area}/{role-slug}.md`.

Every file must contain all five fields:
  - name
  - orientation (frame, verify, simplify)
  - expertise (summary, relevance)
  - collaborates_with
  - scope

  `orientation.verify` entries are questions ending with `?`.
  `orientation.simplify` entries are imperatives.
  `expertise.relevance` references at least one Phase 1 vocabulary term.

After all files are written, resolve any PENDING `collaborates_with` values in
the inertia-advocate file.

---

## STEP 7 — Verification Gate

```
VERIFICATION GATE
==================
CHECK 1 — Registry Summary Table
  Role | Orientation Frame (first 8 words) | Scope | Collaborates With
  -----|-----------------------------------|-------|------------------
  [all roles]

  Inertia-advocate written first? YES / NO
  PASS / FAIL

CHECK 2 — Orphan Reference Check
  For every collaborates_with value: file exists in registry?
  Missing: [list any]
  PASS / FAIL

CHECK 3 — Scope Gradient Check
  Distinct scope values: [list]   Count: [n]   >= 2? YES / NO
  PASS / FAIL

CHECK 4 — Vocabulary Coverage Check
  Every expertise.relevance references a Phase 1 term?
  Missing: [list any roles failing]
  PASS / FAIL

GATE RESULT: PASS / BLOCKED — [list failing checks]
```

Resolve all BLOCKED items before delivering output.
```

---

## V-03 — Table-Heavy Output Format
**Variation axis**: Output format — every phase produces a structured table as its primary artifact; prose instructions are minimal; the model commits to structured values before writing prose
**Hypothesis**: Forcing table output at every phase produces verifiable commitments that cannot be elided; a table with a blank cell is visible, where an omitted prose sentence is not.

---

```
Generate a typed role registry for the domain described in the input.
Output path: `.roles/{area}/`

Produce the tables below in sequence. Each table is a phase exit artifact.
Do not begin the next table until the current table's gate row shows PASS.

---

### TABLE 1 — Bucketed Vocabulary

| Bucket               | Terms Extracted                          |
|----------------------|------------------------------------------|
| Current-System       | [term], [term], ...                      |
| Migration-Cost       | [term], [term], ...                      |
| User-Habit           | [term], [term], ...                      |
| Gate: all non-empty  | PASS / BLOCKED                           |

---

### TABLE 2 — Inertia Q&A

| Q    | Question                         | Answer (verbatim)       | Source Bucket    |
|------|----------------------------------|-------------------------|------------------|
| Q1   | Current system name?             | [answer]                | Current-System   |
| Q2   | Primary migration cost?          | [answer]                | Migration-Cost   |
| Q3   | User habit at risk?              | [answer]                | User-Habit       |

---

### TABLE 3 — Domain-Alignment Audit

| Q-Number | Term Used | Expected Domain  | Match YES/NO |
|----------|-----------|------------------|--------------|
| Q1       | [term]    | Current-System   | YES / NO     |
| Q2       | [term]    | Migration-Cost   | YES / NO     |
| Q3       | [term]    | User-Habit       | YES / NO     |
| Gate: all YES, full-table re-eval after any replacement | PASS / BLOCKED |

Rule: if any row shows NO, replace the non-matching term with a term from
the correct bucket and reprint Table 3 from row Q1. Evaluate all three rows
as a unit. Repeat until Gate shows PASS.

---

### TABLE 4 — Frame Fill

| Slot | Source Q | Verbatim Phase 2 Answer          | Filled Value (for frame) |
|------|----------|----------------------------------|--------------------------|
| Q1   | Q1       | [verbatim]                       | [value placed in frame]  |
| Q2   | Q2       | [verbatim]                       | [value placed in frame]  |

Completed frame string:
> "The current approach relies on [Q1 value]. Adopting this feature requires
> [Q2 value]. Until those costs are justified, the risk outweighs the benefit."

| Binding check             | Result   |
|---------------------------|----------|
| Q1 slot ← Q1 answer       | YES / NO |
| Q2 slot ← Q2 answer       | YES / NO |
| Gate: both YES            | PASS / BLOCKED |

---

### TABLE 5 — Pre-Write Scope Plan

| Planned Role Name        | Perspective Category              | Planned Scope       |
|--------------------------|-----------------------------------|---------------------|
| Inertia Advocate         | inertia                           | [scope]             |
| [role]                   | [product / technical / domain /…] | [scope]             |
| [role]                   | ...                               | [scope]             |

| Scope gate                                      | Result          |
|-------------------------------------------------|-----------------|
| Distinct scope values                           | [list values]   |
| Count >= 2?                                     | YES / NO        |
| Distinct perspective categories (need >= 3)     | [list]          |
| Count >= 3?                                     | YES / NO        |
| Gate: scope >= 2 AND categories >= 3            | PASS / BLOCKED  |

If BLOCKED: revise the plan before writing any file.

---

### ROLE FILES

Write `.roles/{area}/{role-slug}.md` for each row in Table 5.

Each file:

```yaml
name: [role name]
orientation:
  frame: [one declarative sentence — completed frame for inertia-advocate]
  verify:
    - [question] ?
    - [question] ?
  simplify:
    - [imperative]
    - [imperative]
expertise:
  summary: [1-2 sentences]
  relevance: "[references at least one Table 1 vocabulary term]"
collaborates_with:
  - [name matching another role file]
scope: [team / cross-team / org]
```

`orientation.verify` entries end with `?`.
`orientation.simplify` entries are imperatives.
Inertia-advocate `orientation.frame` is the completed frame string from Table 4 verbatim.
Inertia-advocate `orientation.verify` references at least 2 of Q1/Q2/Q3 answers.

---

### TABLE 6 — Verification Gate

| Check | Description                                                      | Result       |
|-------|------------------------------------------------------------------|--------------|
| C1    | Registry summary (Role / Frame snippet / Scope / Collab)         |              |
|       | [one row per role, inline]                                       |              |
| C2    | Orphan references — any collaborates_with name missing a file?   | PASS / FAIL  |
|       | Missing: [list or NONE]                                          |              |
| C3    | Scope gradient — distinct scope values >= 2                      | PASS / FAIL  |
|       | Values present: [list]                                           |              |
| C4    | Vocabulary coverage — every expertise.relevance has a Table 1 term | PASS / FAIL |
|       | Roles missing term: [list or NONE]                               |              |
| GATE  | All checks PASS?                                                 | PASS / BLOCKED |

If BLOCKED: resolve flagged items, reprint failing rows with corrections,
re-run gate until PASS.
```

---

## V-04 — Imperative Register
**Variation axis**: Phrasing register — short imperative sentences throughout; no explanatory prose; each instruction is a direct command; phase names are action verbs, not phase nouns
**Hypothesis**: Removing explanatory prose eliminates hedge language that allows a model to interpret compliance loosely; direct commands with named outputs leave no interpretive gap.

---

```
Build a typed role registry for this domain. Write files to `.roles/{area}/`.

---

**EXTRACT VOCABULARY.**

Read the input. Pull domain terms. Sort every term into one of three buckets:

  CURRENT-SYSTEM TERMS — things already in place
  MIGRATION-COST TERMS — costs of changing
  USER-HABIT TERMS     — behaviors users would need to change

Print all three buckets. Stop if any bucket is empty — add terms before continuing.

---

**ANSWER THREE QUESTIONS.**

Q1 — Name the current system. Use a Current-System term.
Q2 — Name the migration cost. Use a Migration-Cost term.
Q3 — Name the at-risk user habit. Use a User-Habit term.

Print each Q and its answer.

---

**AUDIT THE ANSWERS.**

Print this table:

  Q-Number | Term Used | Expected Bucket  | Match YES/NO
  Q1       | ...       | Current-System   | ...
  Q2       | ...       | Migration-Cost   | ...
  Q3       | ...       | User-Habit       | ...

Any NO: swap the term for a correct-bucket term. Reprint the table from Q1.
Score all three rows together. Keep reprinting until every row shows YES.
Do not move forward with any NO in the table.

---

**FILL THE FRAME.**

Use this template:

  "The current approach relies on [Q1]. Adopting this feature requires [Q2].
  Until those costs are justified, the risk outweighs the benefit."

Print:

  Q1 slot ← Q1 answer: [verbatim]
  Q2 slot ← Q2 answer: [verbatim]
  Completed frame: "[filled sentence]"
  Q1 binding: YES / NO
  Q2 binding: YES / NO

Both bindings must show YES. Fix any mismatch before continuing.

---

**PLAN THE ROLES.**

List every role you will write. Add a scope for each.

  Role Name | Perspective Category | Scope (team / cross-team / org)

Count distinct scope values. Need >= 2. Need >= 3 distinct perspective categories.
Fix the list if either count is too low. Do not write any file until the list passes.

---

**WRITE THE FILES.**

Write `.roles/{area}/{slug}.md` for each role.

Every file needs these five fields:

  name
  orientation:
    frame    — declarative sentence
    verify   — questions (each ends with ?)
    simplify — imperatives
  expertise:
    summary   — 1-2 sentences
    relevance — must name a vocabulary term from the extraction step
  collaborates_with — names of other files in this registry
  scope

Inertia-advocate rules:
  frame     — paste the completed frame string from the Fill step, verbatim
  verify    — at least 2 questions reference Q1, Q2, or Q3 answers
  relevance — name a vocabulary term

Write the inertia-advocate first.

---

**RUN THE GATE.**

Print:

  REGISTRY SUMMARY TABLE
  Role | Frame (8 words) | Scope | Collaborates With
  [one row per role]

  ORPHAN CHECK
  Every collaborates_with value — file exists in registry?
  Missing: [list or NONE]
  Result: PASS / FAIL

  SCOPE GRADIENT CHECK
  Distinct scope values: [list]   Count >= 2: YES / NO
  Result: PASS / FAIL

  VOCABULARY COVERAGE CHECK
  Every expertise.relevance names a vocabulary term?
  Failing roles: [list or NONE]
  Result: PASS / FAIL

  GATE: PASS / BLOCKED

Fix every FAIL. Reprint the gate. Deliver output only after GATE shows PASS.
```

---

## V-05 — Combined: Inertia-First + Gate-Pattern Phases
**Variation axes (combined)**: Inertia framing (inertia-advocate designed before other roles are considered) + Lifecycle emphasis (each phase is expressed as a CHECK/GATE block; no prose between phases)
**Hypothesis**: Pairing inertia-first sequencing with gate-only phase transitions eliminates two gap classes simultaneously — generic role language (closed by inertia-first) and phase elision (closed by gates that name the prior phase output as their input).

---

```
You are building a typed role registry.
Output path: `.roles/{area}/`

Each block below is a GATE. Produce its named output. Confirm its exit
condition before the next GATE opens. A GATE that produces no named output
is incomplete.

---

GATE 1 — VOCABULARY EXTRACTION
  Input: the domain description in the user message.
  Work: extract terms; assign each to exactly one bucket.

  OUTPUT:
    CURRENT-SYSTEM TERMS: [comma-separated]
    MIGRATION-COST TERMS: [comma-separated]
    USER-HABIT TERMS:     [comma-separated]

  EXIT: all three buckets non-empty.
  If any bucket is empty: extract more terms before exit.

---

GATE 2 — INERTIA CHARACTERIZATION
  Input: Gate 1 buckets.
  Work: answer Q1/Q2/Q3; draw each answer's key term from its bucket.

  OUTPUT:
    Q1 (Current-System bucket): [full answer — key term underlined or marked]
    Q2 (Migration-Cost bucket): [full answer — key term marked]
    Q3 (User-Habit bucket):     [full answer — key term marked]

    AUDIT TABLE:
    Q-Number | Term Used | Expected Bucket  | Match YES/NO
    Q1       | [term]    | Current-System   | [YES/NO]
    Q2       | [term]    | Migration-Cost   | [YES/NO]
    Q3       | [term]    | User-Habit       | [YES/NO]

  EXIT RULE: all three rows YES after full-table evaluation.
  If any row is NO: replace the term, reprint the full audit table from Q1,
  re-evaluate all rows as a unit. Do not exit until all rows are YES.

---

GATE 3 — FRAME FILL
  Input: Gate 2 Q1 answer (verbatim), Gate 2 Q2 answer (verbatim).
  Work: fill template; bind each slot to its source; verify binding.

  Template:
    "The current approach relies on [Q1 current system]. Adopting this
    feature requires [Q2 migration cost]. Until those costs are justified,
    the risk outweighs the benefit."

  OUTPUT:
    Q1 slot ← Gate 2 Q1: [verbatim Gate 2 Q1 answer]
    Q2 slot ← Gate 2 Q2: [verbatim Gate 2 Q2 answer]

    Completed frame:
    "[Q1 value filled]. [Q2 value filled]. Until those costs are justified,
    the risk outweighs the benefit."

    Binding check — Q1 slot drawn from Q1 answer: YES / NO
    Binding check — Q2 slot drawn from Q2 answer: YES / NO

  EXIT: both binding checks YES.
  If NO: correct the slot, recheck binding before exit.

---

GATE 4 — WRITE INERTIA-ADVOCATE
  Input: Gate 3 completed frame; Gate 1 vocabulary; Gate 2 Q1/Q2/Q3 answers.
  Work: write `.roles/{area}/inertia-advocate.md` before planning
  any other role.

  File must contain:
    name: Inertia Advocate
    orientation:
      frame: [Gate 3 completed frame — verbatim, unchanged]
      verify:
        - [references Q1 or Q2 answer] ?
        - [references Q3 answer] ?
        - [references any remaining Q-dimension] ?
      simplify:
        - [imperative targeting migration cost]
        - [imperative targeting habit disruption]
    expertise:
      summary: [domain-grounded, 1-2 sentences]
      relevance: "[names at least one Gate 1 vocabulary term]"
    collaborates_with: PENDING
    scope: [team / cross-team / org — assign now]

  EXIT: file written; orientation.frame matches Gate 3 output verbatim;
  at least 2 verify questions reference Gate 2 Q answers; expertise.relevance
  names a vocabulary term.

---

GATE 5 — ROLE PLAN WITH SCOPE AUDIT
  Input: Gate 4 inertia-advocate scope value.
  Work: plan remaining roles; audit scope and perspective diversity.

  OUTPUT:
    ROLE PLAN:
    Role Name           | Perspective Category            | Planned Scope
    --------------------|----------------------------------|---------------
    Inertia Advocate    | inertia (already written)       | [from Gate 4]
    [new role]          | [product/technical/domain/etc.] | [scope]
    [new role]          | ...                             | ...

    SCOPE AUDIT:
      Distinct scope values in plan: [list]
      Count >= 2? YES / NO

    PERSPECTIVE AUDIT:
      Distinct categories in plan: [list]
      Count >= 3? YES / NO

  EXIT: scope count >= 2 AND perspective count >= 3.
  If either fails: revise the plan before exit. Do not write any additional
  file until both conditions hold.

---

GATE 6 — WRITE REMAINING ROLES
  Input: Gate 5 role plan.
  Work: write each planned role file (excluding inertia-advocate, already written).

  Each `.roles/{area}/{slug}.md` must contain all five fields:
    name, orientation (frame/verify/simplify), expertise (summary/relevance),
    collaborates_with, scope.

  Field rules:
    orientation.verify   — questions ending with ?
    orientation.simplify — imperatives
    expertise.relevance  — names at least one Gate 1 vocabulary term
    collaborates_with    — names of files that exist or will exist in registry

  After all files are written: resolve the PENDING collaborates_with in the
  inertia-advocate file by filling in at least one role name from this registry.

  EXIT: all role files written; inertia-advocate PENDING resolved.

---

GATE 7 — VERIFICATION GATE
  Input: all role files in `.roles/{area}/`.
  Work: run all four checks; report results in a single block; do not deliver
  output until GATE RESULT shows PASS.

  OUTPUT:

    CHECK 1 — REGISTRY SUMMARY TABLE
    Role | Orientation Frame (first 8 words) | Scope | Collaborates With
    [one row per role]
    Result: PASS / FAIL

    CHECK 2 — ORPHAN REFERENCE CHECK
    Roles with unresolved collaborates_with values:
      [list or NONE]
    Result: PASS / FAIL

    CHECK 3 — SCOPE GRADIENT CHECK
    Distinct scope values: [list]
    Count >= 2: YES / NO
    Result: PASS / FAIL

    CHECK 4 — VOCABULARY COVERAGE CHECK
    Roles missing a Gate 1 term in expertise.relevance:
      [list or NONE]
    Result: PASS / FAIL

    GATE RESULT: PASS / BLOCKED

  If BLOCKED: resolve each failing check; reprint the full gate block;
  repeat until GATE RESULT shows PASS.
  Deliver output only after GATE RESULT shows PASS.
```

---

## Variation Summary

| Variation | Axis | Single/Combined | Key Structural Bet |
|-----------|------|-----------------|--------------------|
| V-01 | Lifecycle emphasis | Single | Named phases with explicit exit conditions prevent elision of structural artifacts |
| V-02 | Role sequence (inertia-first) | Single | Inertia-advocate written first anchors vocabulary into concrete adversarial framing before generic roles are planned |
| V-03 | Output format (table-heavy) | Single | Tables with blank cells are visible failures; prose omissions are not |
| V-04 | Phrasing register (imperative) | Single | Direct commands without explanatory prose remove hedging surface where compliance is argued rather than demonstrated |
| V-05 | Inertia-first + gate-pattern | Combined | Pairing inertia-first with mandatory gate blocks closes generic-role risk and phase-elision risk simultaneously |
