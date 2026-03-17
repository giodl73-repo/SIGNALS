---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 8
rubric: simulations/quest/rubrics/corps-chart-rubric-v7-2026-03-17.md
---

# Quest Variate — corps-chart (Round 8)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R8 targets rubric additions in v7 that were absent or incomplete in prior rounds:
- C-20 (UPFRONT FORMAT CONTRACT — all five schemas pre-declared before any step)
- C-21 (ROLE-NAME LOCK with inline CHECK reminders at every downstream section that consumes role names, including Inertia Assessment sub-sections)
- C-22 (vocabulary-lock and VERIFY blocks co-deployed as complementary pairs for every governed table)

Additional fix across all variations: domain type vocabulary aligned to C-01's closed set —
(strategic), (operational), (advisory), (governance) — replacing Engineering/PM/Design/Operations/Research/Other
used in prior rounds, which failed C-01 and C-03 silently.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | UPFRONT FORMAT CONTRACT (single axis) | C-20 | Pre-declaring all five table schemas as a named reference block before any step converts column-schema compliance from a recall task (1,500+ tokens of context) into a lookup task (current context) — eliminating merged-column, Quorum-short-form, and cat-N-format errors before any section is written |
| V-02 | ROLE-NAME LOCK with inline CHECK reminders (single axis) | C-21 | Extending the ROLE-NAME LOCK with explicit CHECK annotations at every downstream PRODUCE command — including Inertia Assessment sub-sections and the four-field Rebuttal ROLE UNDER PRESSURE field — converts role coherence from a one-time declaration into an active per-section mechanical check that eliminates the memory-decay failure mode |
| V-03 | Vocabulary-lock + VERIFY co-deployment (single axis) | C-22 | Pairing every vocabulary-lock block with a VERIFY block targeting the complementary right-type-wrong-structure failure mode closes the compliance gap that vocabulary locks alone leave open — locks prevent wrong-type values, VERIFY blocks prevent right-type-but-malformed values, targeting four distinct non-overlapping failure modes |
| V-04 | FORMAT CONTRACT + vocabulary-lock/VERIFY pairs (C-20 + C-22) | C-20, C-22 | Combining the two lookup-conversion mechanisms — schema contract (eliminates column recall errors) and paired vocabulary/VERIFY blocks (eliminates type and format evasions) — without ROLE-NAME LOCK tests whether the two format-enforcement layers already close the highest-frequency essential criteria failures |
| V-05 | Full integration: FORMAT CONTRACT + ROLE-NAME LOCK with inline CHECKs + vocabulary-lock/VERIFY pairs + 5th phase gate + 4-field Rebuttal | C-20 through C-22, C-17, C-14, all prior | Maximum mechanical stack: all five schemas declared upfront, role names checked at every use site including Inertia sub-sections, every governed table covered by both vocabulary lock and VERIFY block, Anti-Pattern Watch structurally non-skippable via 5th gate — tests full constraint density |

---

## V-01 — UPFRONT FORMAT CONTRACT (single axis)

**Axis**: UPFRONT FORMAT CONTRACT pre-declaring all five table schemas before the first phase gate (C-20)
**Hypothesis**: The root cause of merged-column failures (C-03), Quorum short-form failures (C-05), and cat-N-prefix omissions (C-09) is that the model must recall schema details from instructions written 1,500+ tokens earlier. A FORMAT CONTRACT block at the very top of the prompt — before ROLES, before any STEP — places all five schemas in immediate context at every writing moment. Schema compliance becomes a lookup, not a memory exercise. This single mechanism should close multiple essential criteria failures without requiring VERIFY blocks.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING
=======================================================
The following five schemas apply throughout this document.
Reference this block when writing each section. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Required columns: Area | Headcount | Key Roles | Decides | Escalates
    NOTE: "Decision Scope" is NOT a valid column — it merges two required columns into one.
    Key Roles cell format: [role name] ([domain type])
    Required rows: minimum two area rows + one **Total** row with the sum.

(2) OPERATING RHYTHM TABLE
    Required columns: Cadence | Frequency | DRI / Owner | Purpose
    Required rows: minimum three — one ROB, one shiproom or gate meeting, one governance meeting.
    Two meetings must not be merged into one row.

(3) COMMITTEE CHARTER — one block per governance meeting in the rhythm table
    Purpose:    [text]
    Membership: [role name] ([domain type]), [role name] ([domain type]), ...
                minimum two roles listed
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward — must name a destination, not "everything else"]
    Quorum:     [N] of [M] member roles required for binding decisions
    NOTE: "Quorum: [N roles required]" without the denominator M is NOT valid.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               — [area name] — headcount: [N]        (one entry per area)
    cat-2 (Committees/Cadences) — [name]                              (one entry per committee/cadence)
    cat-3 (Headcount)           — Total headcount: [N]                (one total entry)
    cat-4 (DRI Roles)           — [DRI role]                          (one per DRI in rhythm table)
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Required columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" cell format: [element name] (cat-N) — [one sentence of specific relevance]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 — drawn from the ORG-ELEMENT REGISTER above.
    NOTE: A cell that names an org element without the (cat-N) typed prefix is invalid.

---

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from the closed vocabulary: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Carry this annotation forward: use `[role name] ([domain type])` in Key Roles cells (schema 1) and Charter Membership fields (schema 3).

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO structure it in this exact order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. After writing, count data rows (header excluded). If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator.

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns in active use: channels, cadences, informal roles, artifacts with frequency and participants.
DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case cannot answer. Reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Write a re-assessment trigger naming a concrete threshold. DO NOT write "revisit as the team grows."

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw an ASCII hierarchy with minimum two levels. Committees appear as distinct labeled nodes — not embedded in an area box.
Role names must match ROLES-LOADED or ROLES-NOTE. DO NOT introduce new role names.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce per schema (1) in the FORMAT CONTRACT above. Five-column schema required.
DO NOT merge Decides and Escalates.

OPERATING RHYTHM TABLE

Produce per schema (2) above. Minimum three rows: ROB, shiproom/gate, governance. No merged rows.
Reference a role from ROLES-LOADED in DRI / Owner where possible.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table per schema (3) above.
Escalates must name a destination — not "everything not listed under Decides."
Quorum must use the fraction form — see schema (3).

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce per schema (4) above immediately after the charters gate. All four categories required.
DO NOT proceed to Org Evolution Roadmap until all four are populated.

ORG EVOLUTION ROADMAP

Produce a trigger table: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: a different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH

Produce per schema (5) above. Minimum two rows. Every "Why It Applies Here" cell must use the [element name] (cat-N) — prefix.

SECTION ORDER

1.  UPFRONT FORMAT CONTRACT (present above)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [schema 1]
10. Operating Rhythm Table [schema 2]
11. Committee Charters [schema 3]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER [schema 4]
14. Org Evolution Roadmap
15. Anti-Pattern Watch [schema 5]

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-02 — ROLE-NAME LOCK with Inline CHECK Reminders (single axis)

**Axis**: ROLE-NAME LOCK extended with inline CHECK annotations at every downstream section that consumes role names (C-21)
**Hypothesis**: R7 V-05's ROLE-NAME LOCK emitted the list once but placed brief inline annotations only at the diagram, rhythm table, and charters. C-21 requires CHECKs at Inertia Assessment sub-sections too — specifically at the ROLE UNDER PRESSURE field. Without a CHECK at the Inertia Rebuttal, a model reading the LOCK once and then writing 600+ tokens of Inertia content can drift back to archetypes by the time it reaches the Rebuttal. Placing an explicit CHECK at every use site makes role-coherence an active per-section precondition rather than a one-time declaration.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Annotate Key Roles cells: `[role name] ([domain type])`. Annotate Charter Membership fields the same way.

ROLE-NAME LOCK — REQUIRED IMMEDIATELY AFTER CLASSIFICATION

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock is the authority. Every section that produces role names must verify against it.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO structure it in this exact order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns currently in use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

CHECK: any role name referenced in this sub-section must appear in the ROLE-NAME LOCK list above.
Verify before writing. Name the coordination failure the flat-team case cannot answer.
Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK: every role name placed in this diagram must appear in the ROLE-NAME LOCK list.
Verify each name before drawing it. DO NOT introduce names not in the lock.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes — not embedded in an area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
CHECK: every role name in Key Roles must appear in the ROLE-NAME LOCK list.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles annotated: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`.
CHECK: every role name in DRI / Owner must appear in the ROLE-NAME LOCK list.
Minimum three rows: ROB, shiproom or gate meeting, governance meeting. No merged rows.

COMMITTEE CHARTERS

Write a charter per governance meeting: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
CHECK: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: must name a destination.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`
All four categories required.

ORG EVOLUTION ROADMAP

Produce: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every "Why It Applies Here" cell must open with: `[element name] (cat-N) — [one sentence]`.
cat-N codes must match the ORG-ELEMENT REGISTER.

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  ROLE-NAME LOCK (complete permitted-role list)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal [CHECK] / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK Key Roles]
10. Operating Rhythm Table [CHECK DRI/Owner]
11. Committee Charters [CHECK Membership+Decides]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-03 — Vocabulary-Lock + VERIFY Co-Deployment (single axis)

**Axis**: Every vocabulary-lock block paired with a VERIFY block targeting the complementary right-type-wrong-structure failure mode (C-22)
**Hypothesis**: Vocabulary locks prevent wrong-type values (e.g., a Type value outside the closed set). But a model can comply with the type constraint while still producing a wrong-structure value — e.g., using a valid Type in two consecutive rows (satisfies the vocabulary lock, fails C-10), or writing a valid Quorum count without the denominator (satisfies "use a number", fails C-05). VERIFY blocks target the complementary failure mode that vocabulary locks cannot close. The four required pairings — mechanism type, trigger type, cat-N citation, and Quorum — each address a distinct non-overlapping failure mode. Testing this alone determines whether co-deployment is sufficient without the FORMAT CONTRACT.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear.
Annotate Key Roles cells: `[role name] ([domain type])`. Annotate Charter Membership the same way.

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO structure in this order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

Before writing the mechanism table, emit this vocabulary block:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values for the mechanism table:
  Channel           — async or sync communication path (Slack, email, standup)
  Informal Role     — person-as-coordinator without a formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state that coordinates work

No row in the mechanism table may use a Type value outside this list.
```

Produce: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows.
Every Type cell must contain exactly one value from the MECHANISM-TYPE VOCABULARY above.

VERIFY: A mechanism table row whose Type cell contains a value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact} does not satisfy this step. Check every Type cell against the vocabulary before proceeding.

Count data rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns currently in use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case cannot answer. Reference a specific observable.
DO NOT write "the team is growing" without specifying the failure mode.

VERIFY: A Rebuttal that opens with "As we scale..." or "as the team grows..." without naming a current observable failure does not satisfy this step.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes.
Role names must match ROLES-LOADED or ROLES-NOTE.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns.
DO NOT merge Decides and Escalates into a "Decision Scope" column.

VERIFY: A table that merges Decides and Escalates into a single "Decision Scope" column does not satisfy this step. The five-column schema is required: Area, Headcount, Key Roles, Decides, Escalates.

Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles annotated: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows: ROB, shiproom or gate, governance. No merged rows.

COMMITTEE CHARTERS

Write a charter per governance meeting: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: names a destination.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

VERIFY: A Quorum field written as "Quorum: [N roles required for binding decisions]" without the denominator M does not satisfy this step. The fraction form [N] of [M] is required.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`
All four categories required.

ORG EVOLUTION ROADMAP

Before writing the trigger table, emit:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values for the trigger table:
  headcount threshold — a specific hire count that changes coordination needs
  workload signal     — a measurable increase in cross-area dependencies or throughput
  structural symptom  — an observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     — a named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows.
Row 1: headcount threshold type. Row 2: a different Type from the vocabulary above.

VERIFY: Two rows that both use "headcount threshold" as their Type value do not satisfy this step. Row 2 must use a different Type from the vocabulary above.

ANTI-PATTERN WATCH

Before writing the anti-pattern table, emit:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 — Areas
  cat-2 — Committees/Cadences
  cat-3 — Headcount
  cat-4 — DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) — [one sentence of specific relevance]

A cell that names an org element without the (cat-N) prefix does not satisfy this schema.
```

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed citation prefix does not satisfy the citation requirement for that row.

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
4.  Inertia Assessment:
    [MECHANISM-TYPE VOCABULARY] / mechanism table / [VERIFY: wrong-vocabulary Type fails] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal [VERIFY: future-tense fails] / VERDICT
5.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
6.  ASCII Org Diagram
7.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
8.  Headcount by Area [VERIFY: merged column fails]
9.  Operating Rhythm Table
10. Committee Charters [VERIFY: short Quorum fails]
11. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
12. ORG-ELEMENT REGISTER
13. [TRIGGER-TYPE VOCABULARY] + Org Evolution Roadmap [VERIFY: duplicate threshold Type fails]
14. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch [VERIFY: untyped citation fails]

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-04 — FORMAT CONTRACT + Vocabulary-Lock/VERIFY Pairs (C-20 + C-22)

**Axis**: UPFRONT FORMAT CONTRACT combined with co-deployed vocabulary-lock/VERIFY pairs for all governed tables (C-20 + C-22)
**Hypothesis**: The FORMAT CONTRACT eliminates schema recall errors before any section is written. Vocabulary-lock/VERIFY pairs close the right-type-wrong-structure failure modes that remain after the contract is in place. Together they target distinct, complementary failure modes: the contract handles column structure and field-level format, the vocabulary/VERIFY pairs handle Type-value selection and format-constraint evasion. Testing these two without ROLE-NAME LOCK determines whether the format-enforcement layer already closes the highest-frequency failures before role-coherence mechanisms are added.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas are declared here. Reference this block when producing each section.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    INVALID: "Decision Scope" merges two required columns — use separate Decides and Escalates.
    Key Roles format: [role name] ([domain type])
    Total row required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting.

(3) COMMITTEE CHARTER — one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ...  (minimum two roles)
    Decides:    [decision types owned here]
    Escalates:  [decision types referred upward — name the destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    INVALID Quorum: omitting denominator M — the fraction [N] of [M] is required.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               — [area name] — headcount: [N]
    cat-2 (Committees/Cadences) — [name]
    cat-3 (Headcount)           — Total headcount: [N]
    cat-4 (DRI Roles)           — [DRI role]

(5) ANTI-PATTERN WATCH
    Columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" format: [element name] (cat-N) — [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)

---

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear.
Carry annotation to Key Roles and Charter Membership per schemas (1) and (3) above.

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write before any org boxes. Order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

```
MECHANISM-TYPE VOCABULARY
=========================
  Channel           — async or sync communication path
  Informal Role     — person-as-coordinator without formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows.
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

VERIFY: A mechanism row whose Type is not in {Channel, Informal Role, Recurring Cadence, Shared Artifact} does not satisfy this step.

Count rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns in active use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case cannot answer. Reference a specific observable.
DO NOT write "the team is growing" without specifying the failure mode.

VERIFY: A Rebuttal opening with "As we scale..." or "as the team grows..." without naming a current failure does not satisfy this step.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes.
Role names from ROLES-LOADED only.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce per schema (1) above.

VERIFY: A table with a "Decision Scope" column that merges Decides and Escalates does not satisfy this step. The five-column schema is required.

Minimum two area rows plus `**Total**`. Key Roles: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE

Produce per schema (2) above. Minimum three rows. No merged rows.

COMMITTEE CHARTERS

Produce per schema (3) above for each governance meeting.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M does not satisfy this step.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce per schema (4) above immediately after the charters gate. All four categories required.

ORG EVOLUTION ROADMAP

```
TRIGGER-TYPE VOCABULARY
=======================
  headcount threshold — a specific hire count
  workload signal     — measurable increase in cross-area dependencies or throughput
  structural symptom  — observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     — named program event (GA, launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

VERIFY: Two rows both using "headcount threshold" as Type do not satisfy this step.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes (from ORG-ELEMENT REGISTER):
  cat-1 — Areas       cat-2 — Committees/Cadences
  cat-3 — Headcount   cat-4 — DRI Roles

Required "Why It Applies Here" format:
  [element name] (cat-N) — [one sentence of specific relevance]
```

Produce per schema (5) above. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the (cat-N) typed prefix does not satisfy the citation requirement for that row.

SECTION ORDER — 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (present above)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal [VERIFY: future-tense] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [VERIFY: merged column]
10. Operating Rhythm Table
11. Committee Charters [VERIFY: short Quorum]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold]
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
16. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-05 — Full Integration

**Axis**: FORMAT CONTRACT (C-20) + ROLE-NAME LOCK with inline CHECKs at every use site (C-21) + vocabulary-lock/VERIFY co-deployed pairs (C-22) + 5th phase gate (C-17) + 4-field Rebuttal form (C-14)
**Hypothesis**: Maximum mechanical enforcement across all C-17 through C-22 aspirational criteria. The FORMAT CONTRACT eliminates recall-based schema errors. The ROLE-NAME LOCK with per-section CHECKs — including a CHECK embedded inside the Inertia Rebuttal sub-section — eliminates role drift at every use site. Co-deployed vocabulary/VERIFY pairs close right-type-wrong-structure evasions at four distinct locations. The 5th phase gate makes Anti-Pattern Watch structurally non-skippable. The 4-field Rebuttal form forces sequential role-grounding before the breakdown prose. Tests whether full constraint density produces the highest rubric score or induces section-skip failures.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas. Reference this block at each section. No output produced before reading.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    INVALID: "Decision Scope" — separate Decides and Escalates columns are required.
    Key Roles: [role name] ([domain type]) — Total row required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum 3 rows: ROB, shiproom/gate, governance meeting. No merged rows.

(3) COMMITTEE CHARTER — per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), [role name] ([domain type]) ... (min 2 roles)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward — must name destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    INVALID Quorum: "Quorum: [N roles required]" — omitting M is not valid.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               — [area name] — headcount: [N]
    cat-2 (Committees/Cadences) — [name]
    cat-3 (Headcount)           — Total headcount: [N]
    cat-4 (DRI Roles)           — [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here": [element name] (cat-N) — [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)

---

STEP 1 — LOAD ROLES

Read `.craft/roles/`. Produce `ROLES-LOADED:` block: `- [role name] — [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear. No absent role may appear.

STEP 3 — EMIT ROLE-NAME LOCK

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

CHECK: before writing any role name in the Diagram, Headcount Key Roles, Rhythm Table
DRI/Owner, Charter Membership/Decides, or Inertia sub-sections — verify it is in this list.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 4 — INERTIA ASSESSMENT

DO NOT draw any org boxes until the Inertia Assessment is complete. Four sub-sections in order.

Sub-section 1 — Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
  Channel           — async or sync communication path
  Informal Role     — person-as-coordinator without formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table per schema above. Minimum two rows. Every Type cell: vocabulary value only.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact} does not satisfy this step.

Count rows. If < 2, add rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

Sub-section 2 — How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 — Rebuttal

CHECK: any role name written in this sub-section must appear in the ROLE-NAME LOCK list above. Verify before writing.

Use this mandatory four-field form with these exact labels in this order:

```
ROLE UNDER PRESSURE:       [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:      [describe a current coordination failure — not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:     [concrete measurable threshold — hire count, milestone, or structural symptom]
```

VERIFY: A Rebuttal that fills OBSERVABLE BREAKDOWN with "As we scale..." or "as the team grows..." does not satisfy this step. The breakdown must describe a current failure.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning must reference FLAT-CASE-PRESSURE.
Re-assessment trigger from the four-field form applies here — do not repeat unless it differs.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 5 — ASCII ORG DIAGRAM

CHECK: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify before placing.
Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes — not embedded in any area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 — HEADCOUNT BY AREA

Produce per schema (1) of the FORMAT CONTRACT.

VERIFY: A table with a "Decision Scope" column merging Decides and Escalates does not satisfy this step. Five-column schema required.

CHECK: every role name in Key Roles must appear in the ROLE-NAME LOCK list.
Minimum two area rows plus `**Total**`. Key Roles: `[role name] ([domain type])`.

STEP 7 — OPERATING RHYTHM TABLE

Produce per schema (2) of the FORMAT CONTRACT. Minimum three rows: ROB, shiproom/gate, governance.

CHECK: every role name in DRI / Owner must appear in the ROLE-NAME LOCK list.
No merged rows.

STEP 8 — COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

CHECK: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M does not satisfy this step. The fraction form [N] of [M] is required.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 — ORG-ELEMENT REGISTER

Produce per schema (4) of the FORMAT CONTRACT immediately after the charters gate.
All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 — ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
  headcount threshold — a specific hire count that changes coordination needs
  workload signal     — measurable increase in cross-area dependencies or throughput
  structural symptom  — observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     — named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step. Row 2 must use a different Type.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
DO NOT begin Anti-Pattern Watch until this gate line is present.

STEP 11 — ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 — Areas           cat-2 — Committees/Cadences
  cat-3 — Headcount       cat-4 — DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) — [one sentence of specific relevance]

A cell naming an org element without the (cat-N) prefix does not satisfy this schema.
```

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix does not satisfy the citation requirement for that row.

SECTION ORDER — 17 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (present above)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  ROLE-NAME LOCK (complete permitted-role enumeration with CHECK reminder)
5.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today / [CHECK + 4-field Rebuttal] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK against ROLE-NAME LOCK]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area [VERIFY: merged column] [CHECK Key Roles]
11. Operating Rhythm Table [CHECK DRI/Owner]
12. Committee Charters [CHECK Membership+Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
14. ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} — {date}`
