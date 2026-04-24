---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 12
rubric: simulations/quest/rubrics/corps-chart-rubric-v11-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 12)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R12 targets rubric additions in v11 that were absent or incomplete in R11:
- C-31 (BEFORE-PRODUCE directives use HALT-AND-CONFIRM imperative register --
  R11 BEFORE-PRODUCE directives (C-26 FORMAT CONTRACT and C-29 non-FC structural forms) use
  advisory register: "re-read and confirm," "confirm each label is ready." Advisory register
  leaves the acknowledgement-without-verification failure mode open: the model reads the
  directive but does not gate generation on per-field confirmation. C-31 upgrades all
  BEFORE-PRODUCE directives to a three-component HALT-AND-CONFIRM gate: `HALT.` as a
  standalone sentence + enumerated per-field checklist requiring item-by-item confirmation +
  `Proceed only if all confirmed.` as an explicit continuation gate.)
- C-32 (Per-row vocabulary-type CHECK within each vocabulary-governed inner table --
  C-19 (MECHANISM-TYPE VOCABULARY), C-16 (TRIGGER-TYPE VOCABULARY), and C-15
  (CAT-N-CITATION-SCHEMA) each declare a closed vocabulary once before their governed table,
  relying on that block-level declaration to constrain all subsequent rows. Same memory-decay
  exposure that C-28 closes for role-consuming columns: an out-of-vocabulary Type value at
  row 3 can slip through while the vocabulary block no longer holds active attention. C-32
  adds per-row verification: for each row, verify the governed field against the vocabulary
  before writing the next row -- do not complete the table and verify after.)

R11 V-05 provides the baseline for full-integration (V-05). Single-axis variations build from
narrower R11 baselines to isolate each new mechanism.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | HALT-AND-CONFIRM register for BEFORE-PRODUCE directives (single axis) | C-31 | R11 V-01 has two BEFORE-PRODUCE directives (ROLE-NAME LOCK structural form, Rebuttal structural form) using advisory language: "re-read ROLES-LOADED block above -- count the roles" and "re-read the four-field form definition -- confirm each label is ready." Advisory directives are read-and-continue: the model acknowledges the instruction but does not gate on explicit per-field confirmation before generating. V-01 upgrades both directives to HALT-AND-CONFIRM: `HALT.` (standalone sentence) + four-item enumerated checklist + "Proceed only if all confirmed." Built on R11 V-01 baseline (C-29 for both structural forms, ROLE-NAME LOCK five-site enumeration, four-field Rebuttal, inline CHECKs at all five sites, no FORMAT CONTRACT, no per-cell directives). Isolates C-31 upgrade to structural-form BEFORE-PRODUCE directives only. |
| V-02 | Per-row vocabulary-type CHECK in vocabulary-governed inner tables (single axis) | C-32 | R11 V-04 has MECHANISM-TYPE VOCABULARY (C-19), TRIGGER-TYPE VOCABULARY (C-16), and CAT-N-CITATION-SCHEMA (C-15) blocks -- each declared once before their table, with VERIFY blocks confirming post-hoc disqualification of wrong-type rows. The vocabulary block is read once before row 1; by row 3, the block no longer holds active attention. VERIFY fires after the table is complete -- a post-hoc disqualification rather than a per-row active check. C-32 adds per-row directives to all three tables: for each row, verify the governed field against the vocabulary before populating the next row. Built on R11 V-04 baseline (FORMAT CONTRACT, C-29, C-30, vocabulary blocks present), adding only C-32 per-row checks. BEFORE-PRODUCE directives intentionally stay advisory (C-31 gap preserved) to isolate V-02 to V-04 delta. |
| V-03 | HALT-AND-CONFIRM with STOP variant and explicit count-record step (single axis) | C-31 | V-01 uses HALT as the interruption word with a permissive gate ("Proceed only if all confirmed"). V-03 tests a stricter variant: STOP as the interruption word (stronger prohibition signal), an explicit count-record step forcing the model to write the count before confirming ("record: [N] roles present"), and a prohibitive gate ("DO NOT proceed until all N items above are confirmed"). Built on R11 V-03 baseline (per-cell role-lock for DRI/Owner and Key Roles, imperative DO NOT register for ROLE-NAME LOCK, no FORMAT CONTRACT, no four-field Rebuttal). R11 V-03 used "DO NOT emit the ROLE-NAME LOCK until you have done the following: 1. Counted... 2. Confirmed... 3. Verified..." -- an imperative prohibitive approach without a structured checklist between the prohibition and the steps. V-03 upgrades to STOP + structured checklist with count-record + prohibitive gate. Tests whether STOP + explicit record + prohibitive gate achieves higher C-12 compliance than HALT + confirm + permissive gate. |
| V-04 | C-31 + C-32 combined on R11 V-04 baseline | C-31, C-32 | R11 V-04 covers FORMAT CONTRACT DISQUALIFY-IF, BEFORE-PRODUCE for FC schemas (advisory), BEFORE-PRODUCE for non-FC structural forms (advisory), MECHANISM-TYPE VOCABULARY, TRIGGER-TYPE VOCABULARY, CAT-N-CITATION-SCHEMA, four-field Rebuttal, C-29, C-30, ROLE-NAME LOCK five-site. Two gaps remain: (a) all seven BEFORE-PRODUCE directives use advisory register (C-31 gap) and (b) three vocabulary-governed inner tables have block-level vocabulary constraints but no per-row enforcement (C-32 gap). V-04 adds both: HALT-AND-CONFIRM upgrades to all seven BEFORE-PRODUCE sites + per-row vocabulary checks to mechanism table, trigger table, and Anti-Pattern Watch. Per-cell DRI/Owner and Key Roles directives (C-28) intentionally absent -- V-04 to V-05 delta isolates per-cell role-lock contribution independently of C-31+C-32. |
| V-05 | Full integration: C-31 + C-32 on R11 V-05 baseline | C-31, C-32, all prior | Maximum mechanical stack. R11 V-05 covers C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad), C-25 (strict mandatory DRI/Owner), C-26 (BEFORE-PRODUCE for all FC schemas, advisory register), C-27 (Key Roles fifth site), C-28 (per-cell for DRI/Owner and Key Roles), C-29 (BEFORE-PRODUCE for non-FC structural forms, advisory register), C-30 (per-role-name for charter multi-role lists). R12 V-05 adds: (a) HALT-AND-CONFIRM upgrade to all seven BEFORE-PRODUCE sites -- ROLE-NAME LOCK structural form, Rebuttal structural form, and five FC schemas -- converting every advisory BEFORE-PRODUCE into HALT + enumerated checklist + Proceed-only-if gate; (b) per-row vocabulary check in each vocabulary-governed inner table (mechanism, trigger, anti-pattern), converting vocabulary enforcement from block-level read-once to row-by-row active verification. C-31 closes the acknowledgement-without-verification failure mode at all BEFORE-PRODUCE sites; C-32 closes the intra-table type-drift failure mode at all vocabulary-governed columns. |

---

## V-01 -- HALT-AND-CONFIRM Register for BEFORE-PRODUCE Directives (single axis)

**Axis**: HALT-AND-CONFIRM imperative register upgrade for BEFORE-PRODUCE directives (C-31)
**Hypothesis**: R11 V-01 BEFORE-PRODUCE directives use advisory language -- "re-read ROLES-LOADED
block above -- count the roles" and "re-read the four-field form definition -- confirm each label
is ready before populating any field." Advisory register is read-and-continue: the model
acknowledges, then generates without gating on per-field confirmation. HALT-AND-CONFIRM converts
each BEFORE-PRODUCE from a prose reminder into a structured three-component gate: `HALT.`
(interrupts flow) + enumerated per-field checklist (requires item-by-item confirmation) +
`Proceed only if all confirmed.` (gates continuation on explicit completion). Built on R11 V-01
baseline (C-29 for ROLE-NAME LOCK and Rebuttal structural forms, ROLE-NAME LOCK five-site
enumeration, four-field Rebuttal with embedded CHECK at ROLE UNDER PRESSURE, inline CHECKs
at all five sites, no FORMAT CONTRACT, no per-cell directives).

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Carry annotation forward: use `[role name] ([domain type])` in Key Roles cells and Charter Membership fields.

ROLE-NAME LOCK -- REQUIRED IMMEDIATELY AFTER CLASSIFICATION

BEFORE PRODUCING THE ROLE-NAME LOCK:
HALT.
  1. Count the number of roles in the ROLES-LOADED block.
  2. Confirm the lock enumeration you are about to write contains exactly that count -- no more, no fewer.
  3. Confirm no role in the enumeration is absent from ROLES-LOADED.
  4. Confirm no role name in the enumeration was invented here and not present in ROLES-LOADED.
Proceed only if all four confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every role name placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

A role name at any of these five sites that is not listed above is a violation.
Each site carries an inline CHECK directive. All five must be honored.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write before any org boxes. Order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns currently in use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL:
HALT.
  1. Confirm ROLE UNDER PRESSURE is the first field label in the form.
  2. Confirm OBSERVABLE BREAKDOWN is the second field label.
  3. Confirm WHY EXISTING MECHANISMS FAIL is the third field label.
  4. Confirm RE-ASSESSMENT TRIGGER is the fourth field label.
Proceed only if all four confirmed.

Use this mandatory four-field form. The embedded CHECK is part of the form -- do not skip it:

```
REBUTTAL FORM
=============
CHECK [SITE 4 -- INERTIA]: ROLE UNDER PRESSURE must name exactly one role from the ROLE-NAME LOCK
list above. No new role names may be introduced. Verify the name is in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates
                               attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step. The breakdown must describe
a failure that exists now, not a risk that may emerge with growth.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK list.
Verify each name before drawing it.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes -- not embedded in an area box.
DO NOT introduce names not in the ROLE-NAME LOCK.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column.
This is equivalent to the diagram CHECK and the charter Membership CHECK -- treat it as a
first-class enforcement site, not an optional best-effort column.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`.
CHECK [SITE 2 -- DRI/OWNER]: every value in the DRI / Owner column must appear in the ROLE-NAME LOCK list.
No new role names are introduced in this column. Verify before writing each DRI / Owner value.
Minimum three rows: ROB, one shiproom or gate meeting, one governance meeting. No merged rows.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.
Verify before writing.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: must name a destination -- not "everything not listed under Decides."
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- `- [name]`
  `cat-3 (Headcount)` -- `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- `- [DRI role]`
All four categories required. No category may be empty.

ORG EVOLUTION ROADMAP

Produce: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: a different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every "Why It Applies Here" cell must open with: `[element name] (cat-N) -- [one sentence]`.
cat-N codes must match the ORG-ELEMENT REGISTER (cat-1 through cat-4).

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  [HALT -- 4-item checklist -- Proceed only if all confirmed] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment:
    mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist -- Proceed only if all confirmed] /
    [REBUTTAL FORM: CHECK SITE 4 embedded at ROLE UNDER PRESSURE] /
    [VERIFY: future-tense fails] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK SITE 1]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK SITE 5 -- KEY ROLES]
10. Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER]
11. Committee Charters [CHECK SITE 3]
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Per-Row Vocabulary-Type CHECK in Vocabulary-Governed Inner Tables (single axis)

**Axis**: Per-row vocabulary-type CHECK within mechanism table, trigger table, and Anti-Pattern Watch (C-32)
**Hypothesis**: R11 V-04 declares three vocabulary blocks before their governed tables --
MECHANISM-TYPE VOCABULARY (C-19), TRIGGER-TYPE VOCABULARY (C-16), CAT-N-CITATION-SCHEMA (C-15) --
and pairs each with a VERIFY block that post-hoc disqualifies wrong-type rows. The vocabulary block
is read once before row 1; by row 3, the block no longer holds active attention. The VERIFY fires
after the table is complete -- a disqualification check rather than a per-row active prevention.
C-32 adds per-row directives to all three governed tables: for each row, verify the governed field
against the vocabulary before populating the next row. Built on R11 V-04 baseline (FORMAT CONTRACT,
C-29, C-30, all vocabulary blocks present), adding only C-32 per-row checks. BEFORE-PRODUCE
directives stay advisory (C-31 gap intentionally preserved to isolate V-02 to V-04 delta).

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations for schemas with documented failure modes.
Reference this block at each BEFORE PRODUCING directive. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") -- five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles from ROLE-NAME LOCK)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward -- must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M (e.g., "3 members required") --
                   the fraction form [N] of [M] member roles required is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               -- [area name] -- headcount: [N]
    cat-2 (Committees/Cadences) -- [name]
    cat-3 (Headcount)           -- Total headcount: [N]
    cat-4 (DRI Roles)           -- [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" format: [element name] (cat-N) -- [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N)
                   typed citation prefix -- the typed prefix is mandatory for every cell.

---

STEP 1 -- LOAD ROLES

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No absent role may appear.
Carry annotation to Key Roles (schema 1) and Charter Membership (schema 3).

STEP 3 -- EMIT ROLE-NAME LOCK

BEFORE PRODUCING THE ROLE-NAME LOCK: re-read the ROLES-LOADED block. Confirm that every role you
are about to list in the lock appears in ROLES-LOADED and that no role present in ROLES-LOADED is
omitted from the lock. The lock must be a complete, faithful enumeration of ROLES-LOADED.

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every role name placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive applies: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

All five sites must honor this lock. A role name at any of these sites that is not listed
above is a violation regardless of table position or section order.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until the Inertia Assessment is complete. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values for the mechanism table:
  Channel           -- async or sync communication path
  Informal Role     -- person-as-coordinator without formal title
  Recurring Cadence -- scheduled meeting or review cycle
  Shared Artifact   -- document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.

Per-row vocabulary check for mechanism table:
For each row in the mechanism table: verify the Type value appears in the MECHANISM-TYPE VOCABULARY
before writing the next row. Do not complete the table and verify after -- verify each row's Type
value individually before adding the next row. A Type value outside {Channel, Informal Role,
Recurring Cadence, Shared Artifact} at any row (including row 3 of a four-row table) is a
violation regardless of whether prior rows complied.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL: re-read the four-field form definition -- all four fields must appear
in this order: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL /
RE-ASSESSMENT TRIGGER. Confirm each label is ready before populating any field.

Use this mandatory four-field form. The embedded CHECK is part of the form -- do not skip it:

```
REBUTTAL FORM
=============
CHECK [SITE 4 -- INERTIA]: ROLE UNDER PRESSURE must name exactly one role from the ROLE-NAME LOCK
list above. No new role names may be introduced. Verify the name is in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates
                               attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify before placing.
Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes -- not embedded in any area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (1) -- HEADCOUNT BY AREA -- and confirm that five
separate columns (Area, Headcount, Key Roles, Decides, Escalates) will be used and that the
DISQUALIFY-IF condition (merged Decides/Escalates) will not be met in this output.

Produce per schema (1) of the FORMAT CONTRACT.

VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column.
Minimum two area rows plus `**Total**` row with the sum. Key Roles: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (2) -- OPERATING RHYTHM TABLE -- and confirm that
four columns (Cadence, Frequency, DRI / Owner, Purpose) will be used with minimum three rows and
no merged rows.

Produce per schema (2) above.
CHECK [SITE 2 -- DRI/OWNER]: every DRI / Owner value must appear in the ROLE-NAME LOCK list.
Reference a role from ROLES-LOADED in DRI / Owner where a role is known.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter: re-read FORMAT CONTRACT schema (3) -- COMMITTEE CHARTER -- and confirm
all five fields (Purpose, Membership, Decides, Escalates, Quorum) are present and the DISQUALIFY-IF
condition (Quorum without denominator M) will not be met.

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.

Per-role-name directive for Membership field:
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list before
appending the next name. Do not write the complete Membership list and verify after -- verify each
name before adding the next. A novel role name at any position (including position 3 of a four-role
list) is a violation regardless of whether earlier names complied.

Per-role-name directive for Decides field:
Apply the identical per-role-name directive to Decides: for each role name in this field, verify it
appears in the ROLE-NAME LOCK list before appending the next name.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M
does not satisfy this step. Re-read FORMAT CONTRACT DISQUALIFY-IF. The fraction form [N] of [M] is required.

Escalates: must name a destination -- not "everything not listed under Decides."

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER -- and confirm that
all four categories (cat-1 through cat-4) will be populated before this step is complete.

Produce per schema (4) of the FORMAT CONTRACT immediately after the charters gate.
All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 -- ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values for the trigger table:
  headcount threshold -- a specific hire count that changes coordination needs
  workload signal     -- measurable increase in cross-area dependencies or throughput
  structural symptom  -- observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     -- named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

Per-row vocabulary check for trigger table:
For each row in the trigger table: verify the Type value appears in the TRIGGER-TYPE VOCABULARY and
does not repeat the preceding row's Type value before writing the next row. Do not complete the
table and verify after -- verify each row individually before adding the next. An out-of-vocabulary
Type or consecutive-row Type repeat at any row position is a violation regardless of whether prior
rows complied.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

STEP 11 -- ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 -- Areas           cat-2 -- Committees/Cadences
  cat-3 -- Headcount       cat-4 -- DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) -- [one sentence of specific relevance]

A cell naming an org element without the (cat-N) typed prefix does not satisfy this schema.
```

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (5) -- ANTI-PATTERN WATCH -- and confirm that every
"Why It Applies Here" cell will open with [element name] (cat-N) -- and that the DISQUALIFY-IF
condition will not be met in this output.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

Per-row citation check for Anti-Pattern Watch:
For each row in the Anti-Pattern Watch table: verify the "Why It Applies Here" cell opens with
[element name] (cat-N) -- before writing the next row. Do not complete the table and verify after --
verify each row's citation prefix individually before adding the next row. A cell without the
(cat-N) typed prefix at any row is a violation regardless of whether prior rows complied.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  [BEFORE PRODUCING THE ROLE-NAME LOCK: re-read ROLES-LOADED] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration + per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [BEFORE PRODUCING THE REBUTTAL: re-read four-field form] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE / four fields in order] /
    [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [BEFORE PRODUCING schema (1)] Headcount by Area
    [VERIFY: merged column] [CHECK SITE 5 -- KEY ROLES]
11. [BEFORE PRODUCING schema (2)] Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER]
12. [BEFORE PRODUCING schema (3) per charter] Committee Charters
    [CHECK SITE 3]
    [per-role-name Membership: verify before each next name]
    [per-role-name Decides: verify before each next name]
    [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [BEFORE PRODUCING schema (4)] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row: verify Type before next row]
    Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [BEFORE PRODUCING schema (5)]
    + [per-row: verify citation prefix before next row]
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- HALT-AND-CONFIRM with STOP Variant and Explicit Count-Record Step (single axis)

**Axis**: HALT-AND-CONFIRM register using STOP as interruption word, explicit count-record step,
and prohibitive gate (C-31, phrasing variant)
**Hypothesis**: V-01 uses HALT as the interruption word with a permissive gate ("Proceed only if
all confirmed"). V-03 tests a stricter phrasing variant: STOP as the interruption word (stronger
prohibition signal), an explicit count-record step that forces the model to write the count
before confirming ("record: [N] roles present"), and a prohibitive gate ("DO NOT proceed until
all items above are confirmed"). Built on R11 V-03 baseline (per-cell role-lock for DRI/Owner
and Key Roles, imperative DO NOT register for ROLE-NAME LOCK, no FORMAT CONTRACT, no four-field
Rebuttal). R11 V-03 used "DO NOT emit the ROLE-NAME LOCK until you have done the following:
1. Counted... 2. Confirmed... 3. Verified..." -- an imperative prohibitive approach without a
structured checklist between the gate and the steps. V-03 adds: STOP as standalone first sentence;
an explicit count-record step that forces an intermediate artifact; a prohibitive gate. Variation
axis: STOP vs HALT, prohibitive vs permissive gate, and explicit count-record vs confirm-count.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.

ROLE-NAME LOCK -- REQUIRED IMMEDIATELY AFTER CLASSIFICATION

STOP.
Before emitting the ROLE-NAME LOCK, complete this checklist item by item:
  1. Count the roles in ROLES-LOADED. Record: [N] roles present.
  2. Confirm the lock enumeration will contain exactly [N] roles -- not one more, not one fewer.
  3. Confirm every role name in the enumeration appears in ROLES-LOADED.
  4. Confirm no role name was introduced after ROLES-LOADED was read.
DO NOT emit the ROLE-NAME LOCK until all four items above are confirmed.

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
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write before any org boxes. Order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns currently in use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

CHECK: any role name referenced in this sub-section must appear in the ROLE-NAME LOCK list. Verify before writing.
Name the coordination failure the flat-team case cannot answer. Reference a specific observable: blocked
decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the current failure mode.
Name at least one specific role from ROLES-LOADED as the coordination failure point.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Write a concrete re-assessment trigger. DO NOT write "revisit as the team grows."

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify each before drawing.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes -- not embedded in an area box.
DO NOT introduce names not in the ROLE-NAME LOCK.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

Key Roles column -- per-cell role-lock directive:
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list.
No new role names may be introduced in this column.
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list
before populating the next row. Do not complete the table and verify after -- verify row by row
as you populate. A novel role name in any Key Roles cell is a violation regardless of table position.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose` with these requirements applied together:
  - Minimum three rows: one ROB, one shiproom or gate meeting, one governance meeting.
  - DRI / Owner column: every value must appear in the ROLE-NAME LOCK list -- no new role names
    are introduced in this column. This column is a first-class role-coherence enforcement site.
    "Where possible" or equivalent hedged language does not apply here. Every DRI/Owner cell must
    name a role from the ROLE-NAME LOCK list or be left blank -- it must never introduce a new name.
  - No merged rows.

DRI / Owner column -- per-cell role-lock directive:
For each cell in the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list
before populating the next row. Do not complete the table and verify after -- verify row by row
as you populate. A novel role name in any DRI/Owner cell is a violation regardless of row position.

COMMITTEE CHARTERS

Write a charter per governance meeting: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
CHECK: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list. Verify before writing.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: must name a destination.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- `- [name]`
  `cat-3 (Headcount)` -- `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- `- [DRI role]`
All four categories required. No category may be empty.

ORG EVOLUTION ROADMAP

Produce: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every "Why It Applies Here" cell must open with: `[element name] (cat-N) -- [one sentence]`.
cat-N codes from the ORG-ELEMENT REGISTER (cat-1 through cat-4).

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  [STOP -- 4-item checklist with count-record -- DO NOT emit until all confirmed] ROLE-NAME LOCK
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    Rebuttal [CHECK, role-grounded, current failure] / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK against ROLE-NAME LOCK]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [per-cell KEY ROLES -- verify before each next row]
10. Operating Rhythm Table [strict DRI/Owner ROLE-LOCK + per-cell verify before each next row]
11. Committee Charters [CHECK Membership+Decides]
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- C-31 + C-32 Combined on R11 V-04 Baseline

**Axis**: HALT-AND-CONFIRM register for all BEFORE-PRODUCE directives (C-31) combined with
per-row vocabulary-type CHECK in vocabulary-governed tables (C-32), on R11 V-04 baseline
**Hypothesis**: R11 V-04 covers FORMAT CONTRACT DISQUALIFY-IF, BEFORE-PRODUCE for FC schemas
(advisory register), BEFORE-PRODUCE for non-FC structural forms (advisory register),
MECHANISM-TYPE VOCABULARY, TRIGGER-TYPE VOCABULARY, CAT-N-CITATION-SCHEMA, four-field Rebuttal,
C-29, C-30, ROLE-NAME LOCK five-site. Two gaps remain: (a) all seven BEFORE-PRODUCE directives
use advisory register -- the model acknowledges but does not gate on per-field confirmation
before generating (C-31 gap); (b) three vocabulary-governed inner tables have block-level
vocabulary declarations but no per-row active verification (C-32 gap). V-04 adds both:
HALT-AND-CONFIRM upgrades to all seven BEFORE-PRODUCE sites + per-row vocabulary checks to
mechanism table, trigger table, and Anti-Pattern Watch. Per-cell DRI/Owner and Key Roles
directives (C-28) intentionally absent -- V-04 to V-05 delta isolates the per-cell role-lock
contribution independently of C-31+C-32.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations for schemas with documented failure modes.
Reference this block at each BEFORE PRODUCING directive. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") -- five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles from ROLE-NAME LOCK)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward -- must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M (e.g., "3 members required") --
                   the fraction form [N] of [M] member roles required is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               -- [area name] -- headcount: [N]
    cat-2 (Committees/Cadences) -- [name]
    cat-3 (Headcount)           -- Total headcount: [N]
    cat-4 (DRI Roles)           -- [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" format: [element name] (cat-N) -- [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N)
                   typed citation prefix -- the typed prefix is mandatory for every cell.

---

STEP 1 -- LOAD ROLES

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No absent role may appear.
Carry annotation to Key Roles (schema 1) and Charter Membership (schema 3).

STEP 3 -- EMIT ROLE-NAME LOCK

BEFORE PRODUCING THE ROLE-NAME LOCK:
HALT.
  1. Count the number of roles in the ROLES-LOADED block.
  2. Confirm the lock enumeration you are about to write contains exactly that count -- no more, no fewer.
  3. Confirm every role in the enumeration is present in ROLES-LOADED.
  4. Confirm no role in the enumeration was invented here and not present in ROLES-LOADED.
Proceed only if all four confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every role name placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive applies: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

All five sites must honor this lock. A role name at any of these sites that is not listed
above is a violation regardless of table position or section order.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until the Inertia Assessment is complete. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values for the mechanism table:
  Channel           -- async or sync communication path
  Informal Role     -- person-as-coordinator without formal title
  Recurring Cadence -- scheduled meeting or review cycle
  Shared Artifact   -- document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.

Per-row vocabulary check for mechanism table:
For each row in the mechanism table: verify the Type value appears in the MECHANISM-TYPE VOCABULARY
before writing the next row. Do not complete the table and verify after -- verify each row's Type
value individually before adding the next row. A Type value outside {Channel, Informal Role,
Recurring Cadence, Shared Artifact} at any row is a violation regardless of whether prior rows
complied.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL:
HALT.
  1. Confirm ROLE UNDER PRESSURE is the first field label in the form.
  2. Confirm OBSERVABLE BREAKDOWN is the second field label.
  3. Confirm WHY EXISTING MECHANISMS FAIL is the third field label.
  4. Confirm RE-ASSESSMENT TRIGGER is the fourth field label.
Proceed only if all four confirmed.

Use this mandatory four-field form. The embedded CHECK is part of the form -- do not skip it:

```
REBUTTAL FORM
=============
CHECK [SITE 4 -- INERTIA]: ROLE UNDER PRESSURE must name exactly one role from the ROLE-NAME LOCK
list above. No new role names may be introduced. Verify the name is in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates
                               attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify before placing.
Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes -- not embedded in any area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

BEFORE PRODUCING:
HALT.
  1. Confirm Area column will be present.
  2. Confirm Headcount column will be present.
  3. Confirm Key Roles column will be present.
  4. Confirm Decides column will be present as a standalone column -- not merged.
  5. Confirm Escalates column will be present as a standalone column -- not merged with Decides.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.

VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column.
Minimum two area rows plus `**Total**` row with the sum. Key Roles: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

BEFORE PRODUCING:
HALT.
  1. Confirm Cadence column will be present.
  2. Confirm Frequency column will be present.
  3. Confirm DRI / Owner column will be present -- all values from ROLE-NAME LOCK.
  4. Confirm Purpose column will be present.
  5. Confirm minimum three rows (ROB, shiproom/gate, governance) with no merged rows.
Proceed only if all five confirmed.

Produce per schema (2) above.
CHECK [SITE 2 -- DRI/OWNER]: every DRI / Owner value must appear in the ROLE-NAME LOCK list.
Reference a role from ROLES-LOADED in DRI / Owner where a role is known.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT.
  1. Confirm Purpose field will be present.
  2. Confirm Membership field will be present with minimum two roles from ROLE-NAME LOCK.
  3. Confirm Decides field will be present.
  4. Confirm Escalates field will be present -- must name a destination.
  5. Confirm Quorum field will be present in fraction form [N] of [M] member roles required.
Proceed only if all five confirmed.

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.

Per-role-name directive for Membership field:
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list before
appending the next name. Do not write the complete Membership list and verify after -- verify each
name before adding the next. A novel role name at any position (including position 3 of a four-role
list) is a violation regardless of whether earlier names complied.

Per-role-name directive for Decides field:
Apply the identical per-role-name directive to Decides: for each role name in this field, verify it
appears in the ROLE-NAME LOCK list before appending the next name.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M
does not satisfy this step. Re-read FORMAT CONTRACT DISQUALIFY-IF. The fraction form [N] of [M] is required.

Escalates: must name a destination -- not "everything not listed under Decides."

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

BEFORE PRODUCING:
HALT.
  1. Confirm cat-1 (Areas) will be populated with area names and headcounts.
  2. Confirm cat-2 (Committees/Cadences) will be populated.
  3. Confirm cat-3 (Headcount) will be populated with the total.
  4. Confirm cat-4 (DRI Roles) will be populated.
Proceed only if all four confirmed.

Produce per schema (4) of the FORMAT CONTRACT immediately after the charters gate.
All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 -- ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values for the trigger table:
  headcount threshold -- a specific hire count that changes coordination needs
  workload signal     -- measurable increase in cross-area dependencies or throughput
  structural symptom  -- observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     -- named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

Per-row vocabulary check for trigger table:
For each row in the trigger table: verify the Type value appears in the TRIGGER-TYPE VOCABULARY and
does not repeat the preceding row's Type value before writing the next row. Do not complete the
table and verify after -- verify each row individually. An out-of-vocabulary Type or consecutive-row
Type repeat at any row position is a violation regardless of whether prior rows complied.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

STEP 11 -- ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 -- Areas           cat-2 -- Committees/Cadences
  cat-3 -- Headcount       cat-4 -- DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) -- [one sentence of specific relevance]

A cell naming an org element without the (cat-N) typed prefix does not satisfy this schema.
```

BEFORE PRODUCING:
HALT.
  1. Confirm Anti-Pattern column will be present.
  2. Confirm Why It Applies Here column will be present -- every cell opens with [element name] (cat-N) --.
  3. Confirm Mitigation column will be present.
  4. Confirm minimum two rows.
Proceed only if all four confirmed.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

Per-row citation check for Anti-Pattern Watch:
For each row in the Anti-Pattern Watch table: verify the "Why It Applies Here" cell opens with
[element name] (cat-N) -- before writing the next row. Do not complete the table and verify after --
verify each row's citation prefix individually before adding the next. A cell without the (cat-N)
typed prefix at any row is a violation regardless of whether prior rows complied.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  [HALT -- 4-item checklist -- Proceed only if all confirmed] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration + per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist -- Proceed only if all confirmed] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE / four fields in order] /
    [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT -- 5-item column checklist] Headcount by Area
    [VERIFY: merged column] [CHECK SITE 5 -- KEY ROLES]
11. [HALT -- 5-item column checklist] Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER]
12. [HALT per charter -- 5-item field checklist] Committee Charters
    [CHECK SITE 3]
    [per-role-name Membership: verify before each next name]
    [per-role-name Decides: verify before each next name]
    [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT -- 4-item category checklist] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row: verify Type before next row]
    Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [HALT -- 4-item column checklist] +
    [per-row: verify citation prefix before next row]
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-31 + C-32 on R11 V-05 Baseline

**Axis**: HALT-AND-CONFIRM register for all BEFORE-PRODUCE directives (C-31) + per-row
vocabulary-type CHECK in vocabulary-governed tables (C-32), layered on R11 V-05 full-integration
baseline
**Hypothesis**: R11 V-05 covers C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad with
embedded CHECK at ROLE UNDER PRESSURE), C-25 (strict mandatory DRI/Owner ROLE-LOCK), C-26
(BEFORE-PRODUCE for all FC schemas, advisory register), C-27 (Key Roles fifth site), C-28 (per-cell
for DRI/Owner and Key Roles), C-29 (BEFORE-PRODUCE for non-FC structural forms, advisory register),
C-30 (per-role-name for charter multi-role lists). Two enforcement gaps remain: (a) all seven
BEFORE-PRODUCE directives use advisory register -- acknowledged without per-field confirmation gate
(C-31 gap); (b) three vocabulary-governed inner tables have block-level vocabulary declarations
but no per-row active verification (C-32 gap). R12 V-05 adds: (a) HALT-AND-CONFIRM upgrade to
all seven BEFORE-PRODUCE sites -- ROLE-NAME LOCK structural form (C-29), Rebuttal structural
form (C-29), and five FC schemas (C-26) -- converting every advisory BEFORE-PRODUCE into HALT +
enumerated checklist + Proceed-only-if gate; (b) per-row vocabulary check in each vocabulary-
governed inner table (mechanism, trigger, anti-pattern), converting enforcement from block-level
read-once to row-by-row active verification. C-31 closes the acknowledgement-without-verification
failure mode at all BEFORE-PRODUCE sites; C-32 closes the intra-table type-drift failure mode
at all vocabulary-governed columns. Together they complete two parallel enforcement hierarchies
introduced across rounds R9-R12.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations for schemas with documented failure modes.
Reference this block at each BEFORE PRODUCING directive. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") -- five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    DRI / Owner: every value must appear in the ROLE-NAME LOCK list -- no new role names introduced.
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles from ROLE-NAME LOCK)
    Decides:    [decision types or role names from ROLE-NAME LOCK]
    Escalates:  [decision types referred upward -- must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M (e.g., "3 members required") --
                   the fraction form [N] of [M] member roles required is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               -- [area name] -- headcount: [N]
    cat-2 (Committees/Cadences) -- [name]
    cat-3 (Headcount)           -- Total headcount: [N]
    cat-4 (DRI Roles)           -- [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here": [element name] (cat-N) -- [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N)
                   typed citation prefix -- the typed prefix is mandatory for every cell.

---

STEP 1 -- LOAD ROLES

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No absent role may appear.
Carry annotation to Key Roles (schema 1) and Charter Membership (schema 3).

STEP 3 -- EMIT ROLE-NAME LOCK

BEFORE PRODUCING THE ROLE-NAME LOCK:
HALT.
  1. Count the number of roles in the ROLES-LOADED block.
  2. Confirm the lock enumeration you are about to write contains exactly that count -- no more, no fewer.
  3. Confirm every role name in the enumeration appears in ROLES-LOADED.
  4. Confirm no role name in the enumeration was invented here and not present in ROLES-LOADED.
Proceed only if all four confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every role name placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
      [per-cell directive applies: verify before each next row, not after table is complete]
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive applies: verify each name before appending the next,
       do not write the full list and verify after]
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]
      [per-cell directive applies: verify before each next row, not after table is complete]

Sites 2 and 5 carry per-cell row-by-row directives in their section instructions.
Site 3 carries per-role-name directives in the Membership and Decides field instructions.
These are the activation layer for this lock at those sites.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until the Inertia Assessment is complete. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values for the mechanism table:
  Channel           -- async or sync communication path
  Informal Role     -- person-as-coordinator without formal title
  Recurring Cadence -- scheduled meeting or review cycle
  Shared Artifact   -- document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.

Per-row vocabulary check for mechanism table:
For each row in the mechanism table: verify the Type value appears in the MECHANISM-TYPE VOCABULARY
before writing the next row. Do not complete the table and verify after -- verify each row's Type
value individually before adding the next row. A Type value outside {Channel, Informal Role,
Recurring Cadence, Shared Artifact} at any row is a violation regardless of whether prior rows
complied. The vocabulary check fires per-row, not after the table is complete.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL:
HALT.
  1. Confirm ROLE UNDER PRESSURE is the first field label in the form.
  2. Confirm OBSERVABLE BREAKDOWN is the second field label.
  3. Confirm WHY EXISTING MECHANISMS FAIL is the third field label.
  4. Confirm RE-ASSESSMENT TRIGGER is the fourth field label.
Proceed only if all four confirmed.
The embedded CHECK at ROLE UNDER PRESSURE fires before the first field is written -- do not skip it.

Use this mandatory four-field form. The embedded CHECK is part of the form -- do not skip it:

```
REBUTTAL FORM
=============
CHECK [SITE 4 -- INERTIA]: ROLE UNDER PRESSURE must name exactly one role from the ROLE-NAME LOCK
list above. No new role names may be introduced. Verify the name is in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates
                               attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step. The breakdown must describe
a failure that exists now.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies -- restate only if different.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify before placing.
Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes -- not embedded in any area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

BEFORE PRODUCING:
HALT.
  1. Confirm Area column will be present.
  2. Confirm Headcount column will be present.
  3. Confirm Key Roles column will be present.
  4. Confirm Decides column will be present as a standalone column -- not merged.
  5. Confirm Escalates column will be present as a standalone column -- not merged with Decides.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.

VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column.

Key Roles column -- per-cell role-lock directive:
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list
before populating the next row. Do not complete the table and verify after -- verify row by row
as you populate. A novel role name in any Key Roles cell is a violation regardless of table position.

Minimum two area rows plus `**Total**` row with the sum. Key Roles: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

BEFORE PRODUCING:
HALT.
  1. Confirm Cadence column will be present.
  2. Confirm Frequency column will be present.
  3. Confirm DRI / Owner column will be present -- all values from ROLE-NAME LOCK, no new names.
  4. Confirm Purpose column will be present.
  5. Confirm minimum three rows (ROB, shiproom/gate, governance) with no merged rows.
Proceed only if all five confirmed.

Produce: `Cadence | Frequency | DRI / Owner | Purpose` with all requirements applied together:
  - DRI / Owner column: every value must appear in the ROLE-NAME LOCK list -- no new role names
    are introduced in this column. This column is a first-class role-coherence enforcement site
    equivalent to charter Membership and Decides. "Where possible" or equivalent hedged language
    does not apply here. Every DRI/Owner cell must name a role from the ROLE-NAME LOCK list or
    be left blank -- it must never introduce a new name.
  - Minimum three rows: one ROB, one shiproom or gate meeting, one governance meeting.
  - No merged rows.

CHECK [SITE 2 -- DRI/OWNER]: every DRI / Owner value must appear in the ROLE-NAME LOCK list.

DRI / Owner column -- per-cell role-lock directive:
For each cell in the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list
before populating the next row. Do not complete the table and verify after -- verify row by row
as you populate. A novel role name in any DRI/Owner cell is a violation regardless of row position.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT.
  1. Confirm Purpose field will be present.
  2. Confirm Membership field will be present with minimum two roles from ROLE-NAME LOCK.
  3. Confirm Decides field will be present.
  4. Confirm Escalates field will be present -- must name a destination.
  5. Confirm Quorum field will be present in fraction form [N] of [M] member roles required.
Proceed only if all five confirmed.

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.
Verify before writing.

Per-role-name directive for Membership field:
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list before
appending the next name. Do not write the full Membership list and verify after -- verify each role
name individually before adding the next. A novel role name at any position in the list (including
position 3 of a four-role list, or position N of any multi-role list) is a violation regardless of
whether all prior names complied.

Per-role-name directive for Decides field:
Apply the identical per-role-name directive to the Decides field: for each role name listed in
Decides, verify it appears in the ROLE-NAME LOCK list before appending the next name. This applies
to all role references in Decides, not just names in isolation (e.g., "Engineering Lead (operational)"
-- verify "Engineering Lead" against the lock before appending the next role name in the field).

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M
does not satisfy this step. Re-read FORMAT CONTRACT DISQUALIFY-IF. The fraction form [N] of [M] is required.

Escalates: must name a destination -- not "everything not listed under Decides."

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

BEFORE PRODUCING:
HALT.
  1. Confirm cat-1 (Areas) will be populated with area names and headcounts.
  2. Confirm cat-2 (Committees/Cadences) will be populated.
  3. Confirm cat-3 (Headcount) will be populated with the total.
  4. Confirm cat-4 (DRI Roles) will be populated.
Proceed only if all four confirmed.

Produce per schema (4) of the FORMAT CONTRACT immediately after the charters gate.
All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 -- ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values for the trigger table:
  headcount threshold -- a specific hire count that changes coordination needs
  workload signal     -- measurable increase in cross-area dependencies or throughput
  structural symptom  -- observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     -- named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

Per-row vocabulary check for trigger table:
For each row in the trigger table: verify the Type value appears in the TRIGGER-TYPE VOCABULARY and
does not repeat the preceding row's Type value before writing the next row. Do not complete the
table and verify after -- verify each row individually. An out-of-vocabulary Type or consecutive-row
Type repeat is a violation regardless of row position.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step. Row 2 must use a different Type.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
DO NOT begin Anti-Pattern Watch until this gate line is present.

STEP 11 -- ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 -- Areas           cat-2 -- Committees/Cadences
  cat-3 -- Headcount       cat-4 -- DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) -- [one sentence of specific relevance]

A cell naming an org element without the (cat-N) typed prefix does not satisfy this schema.
```

BEFORE PRODUCING:
HALT.
  1. Confirm Anti-Pattern column will be present.
  2. Confirm Why It Applies Here column will be present -- every cell opens with [element name] (cat-N) --.
  3. Confirm Mitigation column will be present.
  4. Confirm minimum two rows.
Proceed only if all four confirmed.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

Per-row citation check for Anti-Pattern Watch:
For each row in the Anti-Pattern Watch table: verify the "Why It Applies Here" cell opens with
[element name] (cat-N) -- before writing the next row. Do not complete the table and verify after --
verify each row's citation prefix individually before adding the next. A cell without the (cat-N)
typed prefix at any row is a violation regardless of whether prior rows complied. Re-read the
CAT-N-CITATION-SCHEMA before verifying each row's prefix.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row. Re-read FORMAT CONTRACT DISQUALIFY-IF
and the CAT-N-CITATION-SCHEMA before producing each cell.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5; DRI/Owner per-cell note in schema 2)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  [HALT -- 4-item checklist -- Proceed only if all confirmed] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration
    + per-cell notes at sites 2 and 5 + per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row, not after table] /
    table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist -- Proceed only if all confirmed] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN /
    WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER] /
    [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT -- 5-item column checklist] Headcount by Area
    [VERIFY: merged column]
    [CHECK SITE 5 -- KEY ROLES, explicit fifth mandatory site]
    [per-cell: verify before each next row, not after table is complete]
11. [HALT -- 5-item column checklist] Operating Rhythm Table
    [strict mandatory DRI/Owner ROLE-LOCK -- no hedging, first-class site]
    [CHECK SITE 2]
    [per-cell: verify before each next row, not after table is complete]
12. [HALT per charter -- 5-item field checklist] Committee Charters
    [CHECK SITE 3]
    [per-role-name Membership: verify each name before appending next]
    [per-role-name Decides: verify each name before appending next]
    [VERIFY: short Quorum -- fraction form required]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT -- 4-item category checklist] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row: verify Type before next row]
    Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [HALT -- 4-item column checklist] +
    [per-row: verify citation prefix before next row]
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`
