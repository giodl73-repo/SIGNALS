# topic-new — Round 9 Variations (v8 rubric)

Five complete, runnable skill body prompts. Each is a standalone prompt body — not a diff against
a prior round. C-26/C-27/C-28 are structurally satisfied in all five; the variation axes determine
*how* each criterion is satisfied, not *whether* it is.

---

## Variation Legend

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Lifecycle emphasis | — | Maximum phase granularity with dual-layer gate architecture; read-before-execute as a required sequencing step at the overview level |
| V-02 | Output format | — | List-based schemas (F-NN:/COV-NN: prefix, not table rows) preserve mechanical coupling while removing table syntax brittleness |
| V-03 | Phrasing register | — | Direct imperative commands ("STOP. Check.") make gate compliance harder to rationalize past than declarative descriptions |
| V-04 | Lifecycle emphasis | Inertia framing | Status-quo consequence woven into every phase makes the cost of skipping visible at each boundary |
| V-05 | Output format | Role sequence + Inertia framing | Engineer-first role sequence, priority-leading signal table, "what this supersedes" framing; tests whether reordering surface form disrupts structural invariants |

---

## V-01 — Lifecycle Emphasis

**Axis**: Single — lifecycle emphasis.
**Hypothesis**: An 8-phase pipeline with maximum per-phase granularity, a three-column PIPELINE OVERVIEW
table as the architectural declaration layer (C-24/C-26), and schema row IDs cited at two independent
gate boundaries (Phase 6 and Phase 7) creates a prompt where every structural criterion is satisfied
before the model writes its first artifact row. Phase 1 fill-in exit gate lists row-count and
column-completeness as two independently checkable items (C-28), ensuring a sparse table cannot pass.

---

```
You are executing the topic-new skill for the Signal plugin.

Register a new topic, define its investigation strategy, and plan the signals
needed for design commit. You will produce two artifacts:
  1. A row in simulations/TOPICS.md
  2. simulations/{topic}/strategy.md

TOPIC: {topic}
DATE:  {date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PIPELINE OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read this entire table before executing Phase 1. All exit gate conditions
are declared here. Do not begin Phase 1 until you have read every row.

| Phase | Purpose                          | Produces                                    | Exit Gate                                                                     |
|-------|----------------------------------|---------------------------------------------|-------------------------------------------------------------------------------|
| 1     | Enumerate stakeholders and risks | Stakeholder fill-in table (S-01..S-N)       | >= 3 rows filled AND all four columns populated                               |
| 2     | Register topic                   | Row in simulations/TOPICS.md                | topic name, status=active, strategy path all present                          |
| 3     | Write rationale                  | ## Rationale in strategy.md                 | >= 2 sentences; names the specific design decision                            |
| 4     | Define scope                     | ## Scope in strategy.md                     | In-scope boundary stated; >= 1 out-of-scope item listed                       |
| 5     | Artifact naming convention       | ## Artifact Naming Convention               | Pattern stated; >= 1 parameterized example with {topic} substituted           |
| 6     | Pre-write gate                   | Gate checkpoint (no rows written yet)       | F-01 through F-05 and COV-01 through COV-03 all verified before Phase 7      |
| 7     | Signal plan                      | ## Signal Plan table in strategy.md         | F-01–F-05 and COV-01–COV-03 re-verified; all rows complete                   |
| 8     | Commit gate                      | ## Commit Gate in strategy.md               | Gate condition stated explicitly; essential signals named by item name        |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIELD SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every signal row written in Phase 7 must satisfy all rules below.
These rules are enforced at Phase 6 (entry gate to Phase 7) and again at
Phase 7 (exit gate). Both checkpoints cite rules by row ID.

| ID    | Field         | Rule                                                                                     | Immediate Failure                                                        | Downstream Effect                                                                     |
|-------|---------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| F-01  | Namespace     | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic         | Signal row rejected; Phase 6 blocks Phase 7 from starting                | Strategy references non-existent namespace; skill invocations fail at runtime         |
| F-02  | Skill         | Must name an existing skill within the declared namespace                                | Row structurally invalid; no artifact will be produced                   | Plan produces no actionable signal; investigation stalls at that namespace            |
| F-03  | Item Name     | Must follow pattern: {topic}-{signal}-{date}.md, or a parameterized template matching it | Row is uncitable; team cannot locate the artifact by name                | Artifacts accumulate without addressable identifiers; signal tracking collapses       |
| F-04  | Owner Role    | Must reference a specific S-N row from the Phase 1 Stakeholders table                   | Role-stakeholder traceability broken; C-08 cannot be satisfied           | Signal ownership is unverifiable at commit time; responsible party is undefined       |
| F-05  | Priority      | Must be exactly: essential / recommended / optional — no substitutions                   | Strategy unparseable as a commit gate; priority cannot be parsed          | Team commits without a defined stopping condition; evidence coverage is unknown       |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COVERAGE SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The signal plan as a whole must satisfy all coverage rules below.
Enforced at Phase 6 (pre-write gate) and Phase 7 (exit gate). Both cite by row ID.

| ID     | Coverage Rule                          | Threshold                          | Immediate Failure                                               | Downstream Effect                                                              |
|--------|----------------------------------------|------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------|
| COV-01 | At least one signal marked essential   | >= 1 row where priority = essential| No commit gate implied; Phase 6 blocks Phase 7                  | Topic has no stopping condition; investigation is open-ended by default        |
| COV-02 | Signal set spans multiple namespaces   | >= 2 distinct namespace values     | Evidence siloed in one namespace; Phase 6 blocks Phase 7        | Topic strategy reflects one discipline; cross-cutting risks are invisible      |
| COV-03 | Owner roles are differentiated         | >= 2 distinct S-N refs             | Role monoculture; Phase 6 blocks Phase 7                        | All signals owned by one stakeholder type; blind spots by discipline persist   |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — STAKEHOLDER AND RISK ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHO BEARS THE RISK if this topic's strategy is wrong?

Before writing any file, fill in the stakeholder table below using roles
relevant to {topic}. The S-N identifiers from this table are the
authoritative source for Owner Role citations in Phase 7.

| ID   | Stakeholder | If this strategy is wrong, they will... | Risk severity |
|------|-------------|------------------------------------------|---------------|
| S-01 | [fill in]   | [fill in]                                | [fill in]     |
| S-02 | [fill in]   | [fill in]                                | [fill in]     |
| S-03 | [fill in]   | [fill in]                                | [fill in]     |

Add rows as needed. Every owner role in Phase 7 must cite one of these IDs.

Phase 1 Exit Gate — do not advance to Phase 2 until all items are checked:
  [ ] >= 3 rows filled (S-01, S-02, S-03 minimum)
  [ ] All four columns populated in every filled row (ID, Stakeholder, consequence, severity)
  [ ] At least 2 distinct stakeholder types represented

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — TOPICS.md ENTRY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Append a row to simulations/TOPICS.md.

Required columns: Topic | Status | Strategy Path
Values:           {topic} | active | simulations/{topic}/strategy.md

Phase 2 Exit Gate — do not advance to Phase 3 until all items are checked:
  [ ] Row appended to simulations/TOPICS.md
  [ ] topic = {topic}
  [ ] status = active
  [ ] strategy path = simulations/{topic}/strategy.md (exact path, no variation)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — RATIONALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write a ## Rationale section in simulations/{topic}/strategy.md.

The rationale must state:
  1. Why this topic needs investigation (not a description — name the decision it gates)
  2. What the team cannot decide without this topic's signals

Phase 3 Exit Gate — do not advance to Phase 4 until all items are checked:
  [ ] ## Rationale section written to simulations/{topic}/strategy.md
  [ ] >= 2 sentences
  [ ] The specific design decision this topic informs is named explicitly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write a ## Scope section in simulations/{topic}/strategy.md.

State what is in scope and list at least one explicit out-of-scope item.
Out-of-scope items prevent scope creep during signal gathering.

Phase 4 Exit Gate — do not advance to Phase 5 until all items are checked:
  [ ] ## Scope section written
  [ ] In-scope boundary stated in at least one sentence
  [ ] >= 1 out-of-scope item listed explicitly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — ARTIFACT NAMING CONVENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write a ## Artifact Naming Convention section in simulations/{topic}/strategy.md.

Pattern: {topic}-{signal}-{date}.md

Include at least one parameterized example with the actual topic name substituted,
not a placeholder. Example form: {topic}-scout-market-2026-03-14.md

Phase 5 Exit Gate — do not advance to Phase 6 until all items are checked:
  [ ] ## Artifact Naming Convention section written
  [ ] Pattern stated explicitly
  [ ] >= 1 example with {topic} substituted for the actual topic name

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — PRE-WRITE GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase writes no artifact. Verify all schema rules before writing any signal row.

Phase 6 Exit Gate — do not advance to Phase 7 until all items are checked:
  [ ] F-01: All planned namespaces are in the allowed set
  [ ] F-02: All planned skills exist within their declared namespace
  [ ] F-03: All planned item names follow the artifact naming pattern
  [ ] F-04: All planned owner roles reference a specific S-N row from Phase 1
  [ ] F-05: All planned priorities are exactly essential / recommended / optional — no substitutions
  [ ] COV-01: >= 1 signal will be marked essential
  [ ] COV-02: Planned signals span >= 2 distinct namespaces
  [ ] COV-03: Planned owner roles reference >= 2 distinct S-N values

If any item fails, resolve it before writing. Do not write partial rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — SIGNAL PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write a ## Signal Plan section in simulations/{topic}/strategy.md.

Table columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority

  - Stakeholder Ref must cite a specific S-N row from Phase 1 (e.g., S-01)
  - Priority must be exactly: essential / recommended / optional
  - Item Name must follow the artifact naming convention from Phase 5

Phase 7 Exit Gate — do not advance to Phase 8 until all items are checked:
  [ ] ## Signal Plan table written to simulations/{topic}/strategy.md
  [ ] F-01: All namespaces are in the allowed set
  [ ] F-02: All skills exist within their declared namespace
  [ ] F-03: All item names follow the artifact naming convention
  [ ] F-04: All owner roles reference a specific S-N row from Phase 1
  [ ] F-05: All priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 row where priority = essential
  [ ] COV-02: >= 2 distinct namespace values present
  [ ] COV-03: >= 2 distinct S-N values in Stakeholder Ref column

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — COMMIT GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is a dedicated phase separate from signal plan production.

Write a ## Commit Gate section in simulations/{topic}/strategy.md.

State the minimal signal set required before design commit. Name each
essential signal by item name — not by count, not by namespace. The gate
condition must be stated explicitly so a team member can verify it without
re-reading the full signal plan.

Phase 8 Exit Gate — work is complete when all items are checked:
  [ ] ## Commit Gate section written
  [ ] Gate condition stated explicitly (not implied by signal plan row count)
  [ ] Each essential signal named by item name
  [ ] Path context given: simulations/{topic}/{signal-artifact}.md
```

---

## V-02 — Output Format

**Axis**: Single — output format.
**Hypothesis**: List-based schemas with F-NN:/COV-NN: inline prefix notation (rather than table rows)
preserve mechanical coupling between constraint definitions and gate citations (C-23/C-27) without
requiring table syntax. The PIPELINE INDEX uses a numbered-list form instead of a table. C-26 is
satisfied by a prominent "Read this entire index" directive on the list header. C-28 is satisfied by
two separately listed items in the Phase 1 exit gate, unchanged from V-01. C-27 is satisfied by
citing the F-NN/COV-NN IDs at both Phase 6 and Phase 7 boundaries in the same list-item format.

---

```
You are executing the topic-new skill for the Signal plugin.

Register a new topic, define its investigation strategy, and plan the signals
needed for design commit.

TOPIC: {topic}
DATE:  {date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PIPELINE INDEX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read this entire index before executing Step 1. All exit conditions are
declared here. Do not begin Step 1 until you have read every item.

1. STAKEHOLDERS — fill in risk table → exit: >= 3 rows filled; all four columns populated
2. REGISTER — append TOPICS.md row → exit: topic, status=active, path all present
3. RATIONALE — write ## Rationale → exit: >= 2 sentences; design decision named
4. SCOPE — write ## Scope → exit: boundary stated; >= 1 out-of-scope item
5. NAMING — write ## Artifact Naming Convention → exit: pattern + parameterized example
6. GATE-CHECK — verify all field and coverage rules → exit: F-01–F-05 and COV-01–COV-03 all pass
7. SIGNAL PLAN — write ## Signal Plan table → exit: F-01–F-05 and COV-01–COV-03 re-verified
8. COMMIT GATE — write ## Commit Gate → exit: explicit gate condition; essentials named by item name

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIELD RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every signal row in the Step 7 plan must satisfy the rules below.
These rules are cited by ID at Step 6 (entry gate) and Step 7 (exit gate).

F-01: Namespace
  Rule: Must be one of — scout, draft, review, flow, trace, prove, listen, program, topic
  If wrong immediately: Signal row rejected; Step 6 blocks Step 7 from starting
  Downstream: Strategy references non-existent namespace; skill invocations fail at runtime

F-02: Skill
  Rule: Must name an existing skill within the declared namespace
  If wrong immediately: Row invalid; no artifact will be produced
  Downstream: Investigation stalls at that namespace; plan produces no actionable signal

F-03: Item Name
  Rule: Must follow pattern {topic}-{signal}-{date}.md or a parameterized template
  If wrong immediately: Row uncitable; team cannot locate artifact by name
  Downstream: Artifacts accumulate without addressable IDs; signal tracking collapses

F-04: Owner Role
  Rule: Must reference a specific S-N row from the Step 1 stakeholders table
  If wrong immediately: Role-stakeholder traceability broken
  Downstream: Signal ownership is unverifiable at commit time

F-05: Priority
  Rule: Must be exactly — essential / recommended / optional. No substitutions.
         Not "high/medium/low". Not "required/nice-to-have". No other values.
  If wrong immediately: Strategy unparseable as a commit gate
  Downstream: Team commits without a defined stopping condition; coverage is unknown

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COVERAGE RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The plan as a whole must satisfy the rules below.
Cited by ID at Step 6 (gate-check) and Step 7 (exit gate).

COV-01: Essential signal present
  Threshold: >= 1 row where priority = essential
  If wrong immediately: No commit gate implied; Step 6 blocks Step 7
  Downstream: Topic has no stopping condition; investigation is open-ended

COV-02: Multi-namespace coverage
  Threshold: >= 2 distinct namespace values
  If wrong immediately: Evidence siloed in one discipline; Step 6 blocks Step 7
  Downstream: Cross-cutting risks are invisible to the strategy

COV-03: Role differentiation
  Threshold: >= 2 distinct S-N references in Owner Role column
  If wrong immediately: Role monoculture; Step 6 blocks Step 7
  Downstream: All signals owned by one stakeholder type; blind spots persist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — STAKEHOLDERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHO BEARS THE RISK if this topic's strategy is wrong?

Fill in this table before writing any file. Use roles relevant to {topic}.

| ID   | Stakeholder | If strategy is wrong, they will... | Risk severity |
|------|-------------|-------------------------------------|---------------|
| S-01 | [fill]      | [fill]                              | [fill]        |
| S-02 | [fill]      | [fill]                              | [fill]        |
| S-03 | [fill]      | [fill]                              | [fill]        |

The S-N IDs are the authoritative source for F-04 Owner Role values in Step 7.

Step 1 exit — before moving to Step 2, check:
  [ ] >= 3 rows filled
  [ ] All four columns populated in every filled row
  [ ] >= 2 distinct stakeholder types

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — REGISTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Append to simulations/TOPICS.md:

  | {topic} | active | simulations/{topic}/strategy.md |

Step 2 exit — before moving to Step 3, check:
  [ ] Row appended to simulations/TOPICS.md
  [ ] topic = {topic}; status = active; path = simulations/{topic}/strategy.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3 — RATIONALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Rationale in simulations/{topic}/strategy.md.

Explain why this topic needs investigation and what design decision it gates.

Step 3 exit — before moving to Step 4, check:
  [ ] ## Rationale section written
  [ ] >= 2 sentences
  [ ] Design decision named explicitly (not just topic description)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4 — SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Scope in simulations/{topic}/strategy.md.
Include at least one explicit out-of-scope item.

Step 4 exit — before moving to Step 5, check:
  [ ] ## Scope section written
  [ ] In-scope boundary stated
  [ ] >= 1 out-of-scope item listed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5 — NAMING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Artifact Naming Convention in simulations/{topic}/strategy.md.
Pattern: {topic}-{signal}-{date}.md
Include >= 1 parameterized example with the actual topic name.

Step 5 exit — before moving to Step 6, check:
  [ ] ## Artifact Naming Convention written
  [ ] Pattern stated
  [ ] >= 1 example with actual topic substituted

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6 — GATE-CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

No artifact is written in this step. Verify all field and coverage rules.

Step 6 exit — before moving to Step 7, check:
  [ ] F-01: All planned namespaces are in the allowed set
  [ ] F-02: All planned skills exist within their declared namespace
  [ ] F-03: All planned item names follow the naming convention
  [ ] F-04: All planned owner roles reference a specific S-N row from Step 1
  [ ] F-05: All planned priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 signal will be marked essential
  [ ] COV-02: Planned signals span >= 2 distinct namespaces
  [ ] COV-03: Planned owner roles reference >= 2 distinct S-N values

If any item fails, resolve before proceeding. Do not write partial rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 7 — SIGNAL PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Signal Plan in simulations/{topic}/strategy.md.

Table columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority

Step 7 exit — before moving to Step 8, check:
  [ ] ## Signal Plan table written
  [ ] F-01: All namespaces in allowed set
  [ ] F-02: All skills exist in their namespace
  [ ] F-03: All item names follow naming convention
  [ ] F-04: All owner roles reference a specific S-N row from Step 1
  [ ] F-05: All priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 row where priority = essential
  [ ] COV-02: >= 2 distinct namespace values
  [ ] COV-03: >= 2 distinct S-N values in Stakeholder Ref

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 8 — COMMIT GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is a dedicated step separate from signal plan production.

Write ## Commit Gate in simulations/{topic}/strategy.md.

Name every essential signal by item name. State the condition explicitly.

Step 8 done when:
  [ ] ## Commit Gate written
  [ ] Gate condition stated explicitly
  [ ] Each essential signal named by item name
  [ ] Path context: simulations/{topic}/{signal-artifact}.md
```

---

## V-03 — Phrasing Register

**Axis**: Single — phrasing register (direct imperative command voice).
**Hypothesis**: Replacing declarative descriptions ("Phase 1 produces X") with direct commands
("Write this table now. Do not advance until you check these items.") makes gate compliance harder
to rationalize past. C-26 is satisfied by a mandatory-tone read directive: "STOP. Read every row
below before you write anything." C-27 is satisfied because the Phase 6 and Phase 7 gate items use
the same F-NN/COV-NN IDs with "CHECK:" prefix — imperative, not descriptive. C-28 is satisfied by
"STOP. Check: (1) >= 3 rows filled. (2) All four columns in each row are filled." as two separate
enumerated items.

---

```
You are executing the topic-new skill. Your job is to register a new topic
and produce an investigation strategy with a planned signal set.

TOPIC: {topic}
DATE:  {date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STOP. READ THIS PIPELINE BEFORE YOU START.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read every row below before executing Phase 1. Every exit condition for
every phase is declared in this table. Do not start Phase 1 until you
have read all eight rows.

| Phase | What you will do                  | What you will produce                       | What you must check before advancing                                          |
|-------|-----------------------------------|---------------------------------------------|-------------------------------------------------------------------------------|
| 1     | Fill in the stakeholder table     | S-01..S-N rows, four columns each           | >= 3 rows filled AND all four columns populated in each row                   |
| 2     | Add TOPICS.md row                 | New row in simulations/TOPICS.md            | topic, status=active, strategy path all written exactly                       |
| 3     | Write the rationale               | ## Rationale section                        | >= 2 sentences; design decision named explicitly                              |
| 4     | Define the scope                  | ## Scope section                            | In-scope boundary written; >= 1 out-of-scope item present                     |
| 5     | Write the naming convention       | ## Artifact Naming Convention               | Pattern stated; >= 1 parameterized example present                            |
| 6     | Run the pre-write check           | Nothing — check only, write nothing         | F-01 through F-05 AND COV-01 through COV-03 all verified                     |
| 7     | Write the signal plan             | ## Signal Plan table                        | F-01–F-05 AND COV-01–COV-03 checked again; every row complete                |
| 8     | Write the commit gate             | ## Commit Gate section                      | Gate condition explicit; essentials named by item name                        |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIELD RULES — memorize these IDs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every signal row you write in Phase 7 must satisfy these five rules.
You will check each one by ID at Phase 6 and again at Phase 7.

| ID    | Field         | Rule                                                                                     | If you get it wrong immediately                                          | What that causes downstream                                                           |
|-------|---------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| F-01  | Namespace     | Use only: scout, draft, review, flow, trace, prove, listen, program, topic               | The row is rejected; you cannot start Phase 7                            | The strategy references namespaces that don't exist; runtime invocations fail         |
| F-02  | Skill         | Name a real skill that exists inside the namespace you chose                             | The row produces nothing; the plan is broken before you start            | That signal is never gathered; the investigation stalls at that point                 |
| F-03  | Item Name     | Write it as {topic}-{signal}-{date}.md or a template in that form                       | No one can find the artifact; it has no canonical address                | Signals pile up without IDs; tracking collapses                                       |
| F-04  | Owner Role    | Copy an S-N identifier from the Phase 1 table — do not invent a role                    | Traceability is broken; you cannot satisfy role differentiation          | At commit time no one can verify who owns the signal                                  |
| F-05  | Priority      | Write exactly: essential OR recommended OR optional — nothing else                       | The strategy cannot be parsed as a commit gate                           | The team commits without knowing which signals must exist first                       |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COVERAGE RULES — memorize these IDs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your signal plan as a whole must satisfy these three rules.
You will check each one by ID at Phase 6 and again at Phase 7.

| ID     | What you must ensure                           | Minimum required                   | If you miss it immediately                                      | What that causes downstream                                              |
|--------|------------------------------------------------|------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------|
| COV-01 | At least one signal is marked essential        | >= 1 row with priority = essential | No commit gate exists; Phase 6 blocks you from writing Phase 7  | The investigation has no stopping condition                              |
| COV-02 | Your signals span more than one namespace      | >= 2 distinct namespaces           | Evidence is siloed; Phase 6 blocks Phase 7                      | Cross-cutting risks are invisible; one discipline's view dominates       |
| COV-03 | Your owner roles come from multiple rows       | >= 2 distinct S-N refs             | Role monoculture; Phase 6 blocks Phase 7                        | All investigation owned by one stakeholder type; blind spots accumulate  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — FILL IN THE STAKEHOLDER TABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ask yourself: WHO GETS HURT if this topic's strategy is wrong?

Fill in this table now. Use real roles for {topic}. These IDs will be
the source of truth for every Owner Role you write in Phase 7.

| ID   | Stakeholder | What happens to them if strategy is wrong | How bad |
|------|-------------|-------------------------------------------|---------|
| S-01 | [write it]  | [write it]                                | [write] |
| S-02 | [write it]  | [write it]                                | [write] |
| S-03 | [write it]  | [write it]                                | [write] |

Add rows until you have covered all meaningful stakeholder types.

STOP. Check these two items independently before Phase 2:
  [ ] (1) >= 3 rows filled
  [ ] (2) All four columns filled in every row you wrote

Do not advance until both items are checked separately.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — ADD THE TOPICS.md ROW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Append this row to simulations/TOPICS.md:

  | {topic} | active | simulations/{topic}/strategy.md |

CHECK before Phase 3:
  [ ] Row written to simulations/TOPICS.md
  [ ] topic = {topic}; status = active; path exact

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — WRITE THE RATIONALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Rationale in simulations/{topic}/strategy.md.
Tell the reader why this topic matters and which specific design decision
cannot be made without these signals.

CHECK before Phase 4:
  [ ] ## Rationale written
  [ ] >= 2 sentences
  [ ] The specific design decision is named — not just "this topic is about X"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — DEFINE THE SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Scope in simulations/{topic}/strategy.md.
Draw the boundary. List at least one thing this topic explicitly does not cover.

CHECK before Phase 5:
  [ ] ## Scope written
  [ ] In-scope boundary stated
  [ ] >= 1 out-of-scope item listed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — WRITE THE NAMING CONVENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Artifact Naming Convention in simulations/{topic}/strategy.md.
Pattern: {topic}-{signal}-{date}.md
Write at least one real example using the actual topic name.

CHECK before Phase 6:
  [ ] ## Artifact Naming Convention written
  [ ] Pattern stated
  [ ] >= 1 example with real topic name (not placeholder)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — RUN THE PRE-WRITE CHECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STOP. Write nothing. Verify every rule before you write a single row.

CHECK before Phase 7:
  [ ] F-01: Every namespace I planned is in the allowed list
  [ ] F-02: Every skill I planned exists inside its namespace
  [ ] F-03: Every item name follows the pattern from Phase 5
  [ ] F-04: Every owner role I planned maps to an S-N row from Phase 1
  [ ] F-05: Every priority I planned is exactly essential / recommended / optional
  [ ] COV-01: At least one signal will be marked essential
  [ ] COV-02: My signals span at least 2 different namespaces
  [ ] COV-03: My owner roles map to at least 2 different S-N values

If anything fails, fix it now. Do not write partial rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — WRITE THE SIGNAL PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Signal Plan in simulations/{topic}/strategy.md.

Columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority

STOP when done. Check everything again before Phase 8:
  [ ] ## Signal Plan table written
  [ ] F-01: Every namespace in allowed list
  [ ] F-02: Every skill exists in its namespace
  [ ] F-03: Every item name follows naming convention
  [ ] F-04: Every owner role maps to an S-N row from Phase 1
  [ ] F-05: Every priority is exactly essential / recommended / optional
  [ ] COV-01: >= 1 row with priority = essential
  [ ] COV-02: >= 2 distinct namespaces
  [ ] COV-03: >= 2 distinct S-N values in Stakeholder Ref

Do not write Phase 8 until every item above is checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — WRITE THE COMMIT GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase is separate from signal production. Do not mix signal rows
and commit gate text in the same section.

Write ## Commit Gate in simulations/{topic}/strategy.md.

Name every essential signal by its item name. Write the condition so
a team member can check it without re-reading the signal plan.

DONE when:
  [ ] ## Commit Gate written as its own section
  [ ] Gate condition stated explicitly — not implied
  [ ] Each essential signal named by item name
  [ ] Path context present: simulations/{topic}/{signal-artifact}.md
```

---

## V-04 — Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis (compact phases with maximum gate density) + Inertia framing
(status-quo consequence woven into every phase as a "without this step" consequence statement).
**Hypothesis**: Making the cost of skipping each phase visible at the phase header — not just in
the schema — makes the pipeline feel operationally consequential throughout, not only at the gates.
C-26 is satisfied by "Read the full overview before starting — the cost of skipping a phase is
visible at every row." C-27 is satisfied by citing F-NN/COV-NN at Phase 6 and Phase 7. C-28 is
satisfied by two separately enumerated Phase 1 exit items. The inertia framing tests whether the
"without this step" pattern at each phase header degrades structural gate compliance.

---

```
You are executing the topic-new skill for the Signal plugin.

Register a new topic, define its investigation strategy, and plan the signals
needed for design commit. Two artifacts must exist at completion:
  - simulations/TOPICS.md — new row for {topic}
  - simulations/{topic}/strategy.md — complete strategy

TOPIC: {topic}
DATE:  {date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PIPELINE OVERVIEW — read before executing Phase 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the full overview before starting — the cost of skipping a phase is
visible at every row. Do not begin Phase 1 until you have read every entry.

| Phase | Purpose                   | If skipped                                                         | Exit Gate                                                       |
|-------|---------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------|
| 1     | Identify who bears risk   | Owner roles in Phase 7 have no source of truth; C-08 unverifiable | >= 3 rows filled; all four columns populated                    |
| 2     | Register in TOPICS.md     | Topic is undiscoverable; strategy file has no registry entry       | topic, status=active, path all present                          |
| 3     | Write rationale           | Team cannot identify which decision this topic gates               | >= 2 sentences; design decision named                           |
| 4     | Define scope              | Signal gathering expands without bound; investigation never closes | In-scope stated; >= 1 out-of-scope item                         |
| 5     | Artifact naming           | Artifacts produced have no canonical address; tracking collapses   | Pattern stated; >= 1 parameterized example                      |
| 6     | Pre-write gate            | Invalid rows enter the signal plan undetected                      | F-01–F-05 and COV-01–COV-03 all verified                        |
| 7     | Signal plan               | No evidence plan exists; design commit is a guess                  | F-01–F-05 and COV-01–COV-03 re-verified; all rows complete      |
| 8     | Commit gate               | Team has no defined stopping condition; investigation is open-ended| Gate explicit; essentials named by item name                    |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIELD SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Each row defines a field rule enforced at Phase 6 (entry gate) and Phase 7 (exit gate).
Without these rules, the signal plan defaults to whatever the model assumes is reasonable —
which may not match what the plugin can execute.

| ID    | Field         | Rule                                                                                     | Immediate Failure                                              | Downstream Effect                                                                 |
|-------|---------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------------|
| F-01  | Namespace     | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic         | Row rejected; Phase 6 blocks Phase 7                           | Strategy references namespaces that don't exist; runtime invocations fail         |
| F-02  | Skill         | Must name an existing skill within the declared namespace                                | Row invalid; no artifact produced                              | Signal never gathered; investigation stalls at that namespace                     |
| F-03  | Item Name     | Must match pattern {topic}-{signal}-{date}.md or equivalent template                    | Artifact has no canonical address; uncitable                   | Signals accumulate without identifiers; tracking collapses at audit time          |
| F-04  | Owner Role    | Must reference a specific S-N row from Phase 1                                          | Traceability from signal to stakeholder broken                 | No verifiable owner at commit time; accountability disappears                     |
| F-05  | Priority      | Must be exactly: essential / recommended / optional — no other vocabulary                | Strategy unparseable as commit gate                            | Team commits without knowing which signals must exist; evidence coverage unknown  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COVERAGE SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without these rules, a syntactically valid signal plan could still default to a single namespace
and a single owner — which is worse than no strategy at all, because it projects false confidence.

| ID     | Coverage Rule                        | Threshold                          | Immediate Failure                                          | Downstream Effect                                                          |
|--------|--------------------------------------|------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------|
| COV-01 | At least one essential signal        | >= 1 row where priority = essential| No commit gate implied; Phase 6 blocks Phase 7             | Investigation has no stopping condition; runs until budget or patience runs out |
| COV-02 | Multi-namespace coverage             | >= 2 distinct namespaces           | Siloed evidence; Phase 6 blocks Phase 7                    | Strategy reflects one discipline's view; cross-cutting risks go undetected |
| COV-03 | Differentiated owner roles           | >= 2 distinct S-N refs             | Role monoculture; Phase 6 blocks Phase 7                   | Investigation bottlenecks on one stakeholder type; others' risks unaddressed |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — STAKEHOLDER AND RISK ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: Owner roles in Phase 7 have no source of truth, making
role differentiation a checklist assertion rather than a derived property.

WHO BEARS THE RISK if this topic's strategy is wrong? Fill in the table below.
Every S-N identifier produced here is the authoritative source for F-04 citations in Phase 7.

| ID   | Stakeholder | If strategy is wrong, they will...    | Risk severity |
|------|-------------|---------------------------------------|---------------|
| S-01 | [fill]      | [fill]                                | [fill]        |
| S-02 | [fill]      | [fill]                                | [fill]        |
| S-03 | [fill]      | [fill]                                | [fill]        |

Add rows until all meaningful stakeholder types are represented.

Phase 1 Exit Gate:
  [ ] >= 3 rows filled (row-count condition)
  [ ] All four columns populated in every filled row (column-completeness condition)
  [ ] >= 2 distinct stakeholder types

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — REGISTER IN TOPICS.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: The topic is undiscoverable by the topic namespace;
strategy file exists with no registry entry pointing to it.

Append to simulations/TOPICS.md:
  | {topic} | active | simulations/{topic}/strategy.md |

Phase 2 Exit Gate:
  [ ] Row appended; topic = {topic}; status = active; path = simulations/{topic}/strategy.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — RATIONALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: The strategy document describes the topic but names no
decision, making it impossible to evaluate when enough signals exist.

Write ## Rationale in simulations/{topic}/strategy.md.
State why this topic needs investigation and name the specific design decision it gates.

Phase 3 Exit Gate:
  [ ] ## Rationale written; >= 2 sentences; design decision named explicitly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: Signal gathering expands to fill available time;
the investigation has no defined boundary and never reaches commit gate.

Write ## Scope in simulations/{topic}/strategy.md.
State what is in scope. List at least one explicit out-of-scope item.

Phase 4 Exit Gate:
  [ ] ## Scope written; in-scope stated; >= 1 out-of-scope item present

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — ARTIFACT NAMING CONVENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: Signal artifacts use ad-hoc names; item names in Phase 7
cannot be verified against a declared pattern; F-03 has no reference point.

Write ## Artifact Naming Convention in simulations/{topic}/strategy.md.
Pattern: {topic}-{signal}-{date}.md
Include >= 1 parameterized example with the actual topic name substituted.

Phase 5 Exit Gate:
  [ ] ## Artifact Naming Convention written; pattern stated; >= 1 real example present

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — PRE-WRITE GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: Invalid namespace values, wrong priority vocabulary, and
missing owner-role citations enter the signal plan silently and are discovered
(if ever) at commit time rather than at design time.

Write nothing in this phase. Verify all rules before writing any signal row.

Phase 6 Exit Gate:
  [ ] F-01: All planned namespaces are in the allowed set
  [ ] F-02: All planned skills exist within their declared namespace
  [ ] F-03: All planned item names match the Phase 5 naming convention
  [ ] F-04: All planned owner roles reference a specific S-N row from Phase 1
  [ ] F-05: All planned priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 signal will be marked essential
  [ ] COV-02: Planned signals span >= 2 distinct namespaces
  [ ] COV-03: Planned owner roles reference >= 2 distinct S-N values

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — SIGNAL PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: No evidence plan exists. Design commit is made on
assumption rather than gathered signals; the team defaults to the last
decision or the loudest opinion.

Write ## Signal Plan in simulations/{topic}/strategy.md.
Columns: Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority

Phase 7 Exit Gate:
  [ ] ## Signal Plan table written to simulations/{topic}/strategy.md
  [ ] F-01: All namespaces in allowed set
  [ ] F-02: All skills exist in their namespace
  [ ] F-03: All item names follow naming convention
  [ ] F-04: All owner roles reference a specific S-N row from Phase 1
  [ ] F-05: All priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 row where priority = essential
  [ ] COV-02: >= 2 distinct namespace values
  [ ] COV-03: >= 2 distinct S-N values in Stakeholder Ref

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — COMMIT GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Without this step: The team has no defined stopping condition. Investigation
runs until exhaustion rather than until the gate is satisfied. This is the
default outcome when no strategy is written — and it is the outcome this
entire pipeline exists to prevent.

This is a dedicated phase separate from signal plan production.

Write ## Commit Gate in simulations/{topic}/strategy.md.
State the minimal set of signals required before design commit.
Name each essential signal by item name, not by count.

Phase 8 Exit Gate:
  [ ] ## Commit Gate written as a dedicated section
  [ ] Gate condition stated explicitly — not implied by row count
  [ ] Each essential signal named by item name
  [ ] Path: simulations/{topic}/{signal-artifact}.md
```

---

## V-05 — Output Format + Role Sequence + Inertia Framing

**Axes**: Three-axis combination.
- Output format: Priority column leads the signal table (rightmost becomes leftmost);
  schema tables have a "Status-Quo Default" column replacing Downstream Effect name.
- Role sequence: Phase 1 opens with technical-risk-owner perspective first, then PM, then users.
  The fill-in table header prompts for "Technical owner / PM / User-facing role" in that order.
- Inertia framing: A "What this topic supersedes" field in Phase 3 names the implicit assumption
  this topic is challenging, making the rationale harder to write generically.

**Hypothesis**: Reordering Priority to the first column makes C-04/C-05 violations visually
prominent (the most important field appears first). Engineering-first role sequence tests whether
C-08/C-19 (role differentiation from Phase 1 as source of truth) is robust to a non-PM-first
framing. The "status-quo default" column label tests whether consequence framing (C-14/C-20) is
preserved when the Downstream Effect is relabeled but still structurally present. C-26/C-27/C-28
are carried forward unchanged from V-01 to test stability across three simultaneous axes.

---

```
You are executing the topic-new skill for the Signal plugin.

Register {topic} as a new investigation topic, define its strategy, and plan
the signals needed for design commit.

TOPIC: {topic}
DATE:  {date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PIPELINE OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read this entire table before executing Phase 1. All exit gate conditions
are declared here. Do not begin Phase 1 until you have read every row.

| Phase | Produces                                    | Exit Gate                                                                         |
|-------|---------------------------------------------|-----------------------------------------------------------------------------------|
| 1     | Stakeholder fill-in table (S-01..S-N)       | >= 3 rows filled; all four columns populated                                      |
| 2     | Row in simulations/TOPICS.md                | topic, status=active, strategy path all present                                   |
| 3     | ## Rationale + ## What This Supersedes      | Rationale >= 2 sentences; superseded assumption named                             |
| 4     | ## Scope                                    | In-scope boundary stated; >= 1 out-of-scope item                                  |
| 5     | ## Artifact Naming Convention               | Pattern stated; >= 1 parameterized example                                        |
| 6     | Gate checkpoint (nothing written)           | F-01–F-05 and COV-01–COV-03 verified before Phase 7                              |
| 7     | ## Signal Plan table                        | F-01–F-05 and COV-01–COV-03 re-verified; all rows complete                        |
| 8     | ## Commit Gate                              | Gate explicit; essentials named by item name; dedicated section                   |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FIELD SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rules enforced at Phase 6 (entry gate) and Phase 7 (exit gate). Both cite by row ID.

| ID    | Field         | Rule                                                                                     | Immediate Failure                                            | Status-Quo Default (if uncorrected)                                                 |
|-------|---------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------|
| F-01  | Namespace     | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic         | Row rejected; Phase 6 blocks Phase 7                         | Team uses ad-hoc namespace names; plugin cannot resolve them at invocation time      |
| F-02  | Skill         | Must name an existing skill within the declared namespace                                | Row invalid; no artifact produced                            | Investigation plan references skills that don't execute; gaps go unnoticed           |
| F-03  | Item Name     | Must follow pattern {topic}-{signal}-{date}.md or equivalent template                   | Artifact has no canonical address                            | Teams default to free-form filenames; signals cannot be audited or cited             |
| F-04  | Owner Role    | Must reference a specific S-N row from the Phase 1 stakeholders table                   | Role traceability broken                                     | Ownership defaults to "team" or "PM"; accountability is undefined at commit time     |
| F-05  | Priority      | Must be exactly: essential / recommended / optional — no substitutions                   | Plan unparseable as commit gate                              | Teams default to "high/medium/low"; commit gate cannot be evaluated mechanically     |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COVERAGE SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Plan-level rules enforced at Phase 6 (entry gate) and Phase 7 (exit gate). Both cite by row ID.

| ID     | Coverage Rule                        | Threshold                           | Immediate Failure                                    | Status-Quo Default (if uncorrected)                                           |
|--------|--------------------------------------|-------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------|
| COV-01 | At least one essential signal        | >= 1 row with priority = essential  | No commit gate; Phase 6 blocks Phase 7               | Investigation runs until exhaustion; stopping condition is implicit or absent  |
| COV-02 | Multi-namespace coverage             | >= 2 distinct namespace values      | Evidence siloed; Phase 6 blocks Phase 7              | One namespace (usually scout) covers everything; technical and user signals absent |
| COV-03 | Role differentiation                 | >= 2 distinct S-N refs              | Role monoculture; Phase 6 blocks Phase 7             | All signals owned by PM or tech lead; other stakeholder views never surface    |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — STAKEHOLDER AND RISK ENUMERATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHO BEARS THE RISK if this topic's strategy is wrong?

Start from the technical owner — who implements the system affected by this
topic's decision? Then add the PM who gates commit. Then add the user-facing
role who lives with the outcome. Extend as needed for {topic}.

The S-N identifiers from this table are the authoritative source for F-04
Owner Role citations in Phase 7. No role may be cited that is not present here.

| ID   | Stakeholder (technical first) | If strategy is wrong, they will...    | Risk severity |
|------|-------------------------------|---------------------------------------|---------------|
| S-01 | [technical owner — fill]      | [fill]                                | [fill]        |
| S-02 | [PM / decision owner — fill]  | [fill]                                | [fill]        |
| S-03 | [user-facing role — fill]     | [fill]                                | [fill]        |

Phase 1 Exit Gate:
  [ ] >= 3 rows filled
  [ ] All four columns populated in every filled row
  [ ] Technical, decision, and user-facing perspectives each represented by at least one row

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — REGISTER IN TOPICS.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Append to simulations/TOPICS.md:
  | {topic} | active | simulations/{topic}/strategy.md |

Phase 2 Exit Gate:
  [ ] Row appended; topic = {topic}; status = active; path = simulations/{topic}/strategy.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — RATIONALE AND WHAT THIS SUPERSEDES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write two sections in simulations/{topic}/strategy.md:

## Rationale
Why this topic needs investigation. Name the specific design decision this topic gates.
The team currently cannot make this decision without the signals planned in Phase 7.

## What This Supersedes
Name the implicit assumption or prior decision this topic is challenging.
What does the team currently believe (or default to) if no investigation is done?
This section makes the inertia explicit — without a named status-quo assumption,
the investigation has no defined contrast point.

Phase 3 Exit Gate:
  [ ] ## Rationale written; >= 2 sentences; design decision named
  [ ] ## What This Supersedes written; current assumption or default named explicitly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — SCOPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Scope in simulations/{topic}/strategy.md.
State the in-scope boundary. List at least one explicit out-of-scope item.

Phase 4 Exit Gate:
  [ ] ## Scope written; in-scope boundary stated; >= 1 out-of-scope item listed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5 — ARTIFACT NAMING CONVENTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Artifact Naming Convention in simulations/{topic}/strategy.md.
Pattern: {topic}-{signal}-{date}.md
Include >= 1 parameterized example with the actual topic name substituted.

Phase 5 Exit Gate:
  [ ] ## Artifact Naming Convention written; pattern stated; >= 1 real example present

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6 — PRE-WRITE GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write nothing. Verify all field and coverage rules before writing any signal row.

Phase 6 Exit Gate:
  [ ] F-01: All planned namespaces are in the allowed set
  [ ] F-02: All planned skills exist within their declared namespace
  [ ] F-03: All planned item names follow the Phase 5 naming convention
  [ ] F-04: All planned owner roles reference a specific S-N row from Phase 1
  [ ] F-05: All planned priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 signal will be marked essential
  [ ] COV-02: Planned signals span >= 2 distinct namespaces
  [ ] COV-03: Planned owner roles reference >= 2 distinct S-N values

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 7 — SIGNAL PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write ## Signal Plan in simulations/{topic}/strategy.md.

Priority leads the table to make essential/recommended/optional decisions visible first.

Columns: Priority | Namespace | Skill | Item Name | Stakeholder Ref | Owner Role

  - Priority must be exactly: essential / recommended / optional
  - Stakeholder Ref must cite a specific S-N row from Phase 1
  - Item Name must follow the artifact naming convention from Phase 5

Phase 7 Exit Gate:
  [ ] ## Signal Plan table written to simulations/{topic}/strategy.md
  [ ] F-01: All namespaces in allowed set
  [ ] F-02: All skills exist in their namespace
  [ ] F-03: All item names follow naming convention
  [ ] F-04: All owner roles reference a specific S-N row from Phase 1
  [ ] F-05: All priorities are exactly essential / recommended / optional
  [ ] COV-01: >= 1 row where priority = essential
  [ ] COV-02: >= 2 distinct namespace values
  [ ] COV-03: >= 2 distinct S-N values in Stakeholder Ref

Do not advance to Phase 8 until all items above are checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 8 — COMMIT GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is a dedicated phase separate from signal plan production.

Write ## Commit Gate in simulations/{topic}/strategy.md.

State the minimal signal set required before design commit — as a contrast to
the status-quo default named in Phase 3 ("What This Supersedes"). Name each
essential signal by item name.

Phase 8 Exit Gate:
  [ ] ## Commit Gate written as a dedicated section (not appended to Signal Plan)
  [ ] Gate condition stated explicitly
  [ ] Each essential signal named by item name
  [ ] Path context: simulations/{topic}/{signal-artifact}.md
```

---

## Structural Invariants Across All Five Variations

Every variation satisfies C-26, C-27, and C-28 through a distinct surface form.
The table below maps each new criterion to its carrier in each variation.

| Criterion | V-01 carrier | V-02 carrier | V-03 carrier | V-04 carrier | V-05 carrier |
|-----------|-------------|-------------|-------------|-------------|-------------|
| C-26 (read-before-execute directive) | "Read this entire table before executing Phase 1..." on the PIPELINE OVERVIEW table | "Read this entire index before executing Step 1..." on the numbered PIPELINE INDEX | "STOP. READ THIS PIPELINE BEFORE YOU START... Read every row before executing Phase 1" bold header | "Read the full overview before starting — the cost of skipping a phase is visible at every row" on PIPELINE OVERVIEW | "Read this entire table before executing Phase 1..." on PIPELINE OVERVIEW |
| C-27 (schema IDs at 2 independent boundaries) | F-01–F-05 and COV-01–COV-03 cited at Phase 6 exit gate AND Phase 7 exit gate | F-01–F-05 and COV-01–COV-03 cited at Step 6 exit AND Step 7 exit | F-01–F-05 and COV-01–COV-03 cited at Phase 6 ("CHECK:") AND Phase 7 ("STOP. Check again:") | F-01–F-05 and COV-01–COV-03 cited at Phase 6 exit AND Phase 7 exit | F-01–F-05 and COV-01–COV-03 cited at Phase 6 exit AND Phase 7 exit |
| C-28 (column completeness separate from row count) | Phase 1 exit: "[ ] >= 3 rows filled" AND "[ ] All four columns populated in every filled row" as two distinct checkbox items | Step 1 exit: "[ ] >= 3 rows filled" AND "[ ] All four columns populated in every filled row" as two distinct items | Phase 1: "STOP. Check these two items independently" with "(1) >= 3 rows filled" and "(2) All four columns filled in every row" explicitly enumerated | Phase 1 exit: "[ ] >= 3 rows filled (row-count condition)" AND "[ ] All four columns populated in every filled row (column-completeness condition)" as two labeled separate items | Phase 1 exit: "[ ] >= 3 rows filled" AND "[ ] All four columns populated in every filled row" as two distinct items |
