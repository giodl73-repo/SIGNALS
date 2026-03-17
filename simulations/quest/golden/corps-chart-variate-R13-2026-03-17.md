---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 13
rubric: simulations/quest/rubrics/corps-chart-rubric-v12-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 13)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R13 targets the two new criteria added in v12 of the rubric:

- **C-33 -- Instruction-site register consistency** (no checklist-strict/prose-advisory split):
  R12 V-04 STEP 7 contains the exact failure pattern: HALT-AND-CONFIRM checklist item 3 reads
  "Confirm DRI / Owner column will be present -- all values from ROLE-NAME LOCK" (strict mandatory)
  while the co-located post-produce instruction reads "Reference a role from ROLES-LOADED in DRI /
  Owner where a role is known" (conditional advisory). The model satisfies the checklist check then
  interprets "where a role is known" as the operative generation instruction; the softening qualifier
  persists in output despite the strict checklist item. C-33 requires: every instruction site that
  references a governed enforcement requirement uses a single unambiguous mandatory-register
  formulation -- no advisory qualifier at any co-located instruction site.

- **C-34 -- Per-granularity enforcement sites use procedural action directives, not emphatic framing**:
  R12 V-01 Key Roles (CHECK SITE 5) uses "treat it as a first-class enforcement site, not an
  optional best-effort column" -- emphatic framing that signals correct priority without specifying
  the mechanical action or temporal constraint. The procedural directive ("for each cell, verify the
  value appears in the ROLE-NAME LOCK list before populating the next row -- do not complete the
  table and verify after") is absent. C-34 requires: per-cell (C-28) and per-row (C-32) enforcement
  sites must specify both the verification action and the temporal sequencing constraint; emphatic
  framing alone is insufficient.

Variation axes: phrasing register (C-34), output format / instruction-site consolidation (C-33),
lifecycle emphasis / phase-gate register audits (C-33 variant), then both new criteria combined on
R12 V-04 base, then full integration on R12 V-05 base.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | Phrasing register -- procedural-action replacement (single axis) | C-34 | R12 V-01 Key Roles uses emphatic framing ("treat it as a first-class enforcement site, not an optional best-effort column") at CHECK SITE 5 -- an importance signal without a mechanical directive. The procedural-action directive ("for each cell in this column, verify the value appears in the ROLE-NAME LOCK list before populating the next row -- do not complete the table and verify after") is absent. V-01 replaces all emphatic framing at per-cell and per-row enforcement sites with explicit procedural directives specifying (a) the verification action and (b) the temporal sequencing constraint. Built on R12 V-01 base (HALT-AND-CONFIRM for ROLE-NAME LOCK and Rebuttal structural forms, four-field Rebuttal, ROLE-NAME LOCK five-site enumeration, per-cell DRI/Owner present, no FORMAT CONTRACT). Key Roles column upgraded from emphatic site designation to procedural per-cell directive matching the DRI/Owner pattern. Mechanism table, trigger table, and Anti-Pattern Watch per-row checks also upgraded to full procedural form (action + temporal constraint). Isolates C-34 contribution: same check sites as R12 V-01, different directive quality at those sites. |
| V-02 | Output format -- instruction-site consolidation (single axis) | C-33 | R12 V-04's C-33 failure is architectural: a HALT-AND-CONFIRM checklist item and a co-located column instruction both reference the same governed requirement but use different registers -- strict in the checklist, advisory in the prose instruction ("where a role is known"). The split exists because the requirement is stated at two instruction sites. V-02 tests an architectural fix: every governed enforcement requirement is stated at exactly ONE instruction site -- the HALT-AND-CONFIRM checklist or the PRODUCE command directive, but not both. Section-level instructions that would duplicate a governed requirement are removed entirely; the HALT-AND-CONFIRM checklist becomes the single operative statement. Where a requirement must appear in a PRODUCE command (for immediate generation reference), the mandatory-register formulation from the checklist is reproduced verbatim -- no alternative phrasing is permitted. Built on R12 V-04 base (HALT-AND-CONFIRM, per-row vocabulary). Advisory "where a role is known" line removed; DRI/Owner PRODUCE command contains only the checklist-identical mandatory formulation. Tests whether single-site instruction eliminates split-register output. |
| V-03 | Lifecycle emphasis -- phase-gate register audits (single axis) | C-33 | V-01 prevents the split-register problem by fixing source language. V-02 prevents it architecturally. V-03 catches it at gate time: each of the four primary phase gates includes a backward-looking REGISTER-CONSISTENCY AUDIT that confirms no advisory qualifier was introduced in the preceding section for any governed enforcement requirement before allowing the next section to begin. The audit enumerates the governed requirements by site and confirms each used mandatory-register language. If a qualifier is found, the gate requires correction before proceeding. Built on R12 V-03 base (STOP variant, per-cell DRI/Owner and Key Roles with per-cell procedural directives, no FORMAT CONTRACT). Phase gates upgraded from labeled dividers to structured REGISTER-CONSISTENCY AUDIT checkpoints. Tests whether retrospective register correction at gate time achieves C-33 compliance comparable to prospective language control. |
| V-04 | C-33 + C-34 combined on R12 V-04 baseline | C-33, C-34, all prior | R12 V-04 achieves C-31 (HALT-AND-CONFIRM at all seven BEFORE-PRODUCE sites) and C-32 (per-row vocabulary enforcement at all three vocabulary-governed tables) but exposes two new failure modes: (a) advisory "where a role is known" at DRI/Owner co-located with strict HALT checklist (C-33 failure) and (b) Key Roles is a designated CHECK site without a per-cell procedural directive -- neither emphatic framing nor procedural directive present at all (C-34 / C-28 gap). V-04 adds both closures on R12 V-04 base: C-33 fix removes the advisory co-located DRI/Owner instruction and ensures all instruction sites for governed requirements use a single mandatory-register formulation; C-34 fix adds per-cell procedural directives (action + temporal constraint) to Key Roles and ensures DRI/Owner per-cell directive uses full procedural form. The combined test determines whether C-33 and C-34 are jointly sufficient to close the two failure modes in combination. |
| V-05 | Full integration: C-33 + C-34 on R12 V-05 baseline | C-33, C-34, all prior | Maximum mechanical stack. R12 V-05 covers C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad), C-25 (strict mandatory DRI/Owner), C-26 (BEFORE-PRODUCE FC back-reference, HALT-AND-CONFIRM), C-27 (Key Roles fifth site), C-28 (per-cell for DRI/Owner and Key Roles), C-29 (BEFORE-PRODUCE for non-FC structural forms, HALT-AND-CONFIRM), C-30 (per-role-name for charter multi-role lists), C-31 (HALT-AND-CONFIRM at all BEFORE-PRODUCE), C-32 (per-row vocabulary in all three vocabulary tables). R13 V-05 adds: C-33 -- audit reveals that R12 V-05 STEP 7 retains the advisory "where a role is known" qualifier co-located with the strict HALT checklist; this is removed and all instruction sites for governed requirements use identical mandatory language; C-34 -- R12 V-05 Key Roles per-cell directive is confirmed to use full procedural form (action + temporal constraint); DRI/Owner per-cell directive likewise confirmed; all per-row vocabulary enforcement confirmed to use procedural form. Together C-33 + C-34 close the two final documented failure modes: register contamination via co-located softeners (C-33) and emphatic-framing evasion at per-granularity sites (C-34). |

---

## V-01 -- Procedural-Action Replacement at Per-Cell and Per-Row Sites (single axis)

**Axis**: Phrasing register -- C-34 procedural-action directives replacing emphatic importance framing
**Hypothesis**: R12 V-01 Key Roles (CHECK SITE 5) uses emphatic framing: "treat it as a first-class
enforcement site, not an optional best-effort column." This signals governance priority without
specifying the mechanical check or its timing. The per-cell procedural directive -- "for each cell
in this column, verify the value appears in the ROLE-NAME LOCK list before populating the next row
-- do not complete the table and verify after" -- is absent. V-01 replaces all emphatic framing at
every per-cell and per-row enforcement site with explicit procedural directives specifying the
verification action and the temporal sequencing constraint. All other R12 V-01 mechanisms preserved
unchanged. Built on R12 V-01 base: HALT-AND-CONFIRM for ROLE-NAME LOCK and Rebuttal BEFORE-PRODUCE
structural forms (C-31), four-field Rebuttal (C-14), ROLE-NAME LOCK five-site enumeration (C-21,
C-27), per-cell DRI/Owner with advisory register in R12 upgraded to full procedural here (C-34),
no FORMAT CONTRACT. C-32 per-row vocabulary present with procedural form throughout. No C-28
emphatic replacement needed for DRI/Owner in R12 V-01 (it already had a per-cell directive) --
Key Roles is the primary C-34 target, plus vocabulary table rows receive the temporal constraint.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:`
with inferred roles listed.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

Produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and
governance roles. Assign each role exactly one type: `(strategic) / (operational) / (advisory) /
(governance)`. Format: `- [role name] -- [domain type]`. Every loaded role must appear. No role
absent from ROLES-LOADED may appear. Carry annotation forward: use `[role name] ([domain type])`
in Key Roles cells and Charter Membership fields.

ROLE-NAME LOCK -- REQUIRED IMMEDIATELY AFTER CLASSIFICATION

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
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
  (4) Inertia Assessment sub-sections -- every role name referenced, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

A role name at any of these five sites not listed above is a violation.
Each site carries an inline CHECK directive. All five must be honored.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO NOT draw any org boxes until the Inertia Assessment is complete.
Write all four sub-sections in order.

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
before writing the next row -- do not complete the table and verify after. A Type value outside
{Channel, Informal Role, Recurring Cadence, Shared Artifact} at any row is a violation regardless
of whether prior rows complied.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence,
Shared Artifact} does not satisfy this step.

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
list above. No new role names may be introduced. Verify the name appears in the lock before writing.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates
                               attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN begins with "As we scale..." or "as the team grows..."
does not satisfy this step. The breakdown must describe a failure that exists now.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Rating from: `Strong / Moderate / Weak / Negligible / Insufficient`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK
list. For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node
-- do not complete the diagram and verify after.
Draw ASCII hierarchy with minimum two levels. Use only printable ASCII characters (+, -, |, and text).
Committees as distinct labeled nodes -- not embedded in an area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Minimum two area rows plus `**Total**` row.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list before
populating the next row -- do not complete the Key Roles column and verify after. Apply this check
to every row individually. A novel role name at any Key Roles cell is a violation regardless of
whether prior rows complied. Key Roles format: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`. Four columns required.
Minimum three rows: one ROB, one shiproom or gate meeting, one governance meeting. No merged rows.

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
For each cell in the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list before
populating the next row -- do not complete the DRI / Owner column and verify after. Every DRI/Owner
cell value must be a role from ROLE-NAME LOCK. A novel role name at any DRI/Owner cell is a
violation regardless of row position.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table.
Fields per charter: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME
LOCK list. Verify before writing each name. Membership: minimum two roles annotated
`[role name] ([domain type])`. Escalates: must name a destination.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.
VERIFY: A Quorum written as "[N] members required" without the denominator M does not satisfy
this step. The fraction form [N] of [M] is required.

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- `- [name]`
  `cat-3 (Headcount)` -- `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- `- [DRI role]`
All four categories required. No category may be empty.

ORG EVOLUTION ROADMAP

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

Produce: `Trigger | Structural Change | Type`. Minimum two rows.
Row 1 must be a headcount threshold trigger. Row 2 must use a different Type.

Per-row vocabulary check for trigger table:
For each row in the trigger table: verify the Type value appears in TRIGGER-TYPE VOCABULARY and
does not repeat the preceding row's Type before writing the next row -- do not complete the table
and verify after. An out-of-vocabulary Type or consecutive repeat at any row position is a
violation regardless of whether prior rows complied.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

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

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.

Per-row citation check for Anti-Pattern Watch:
For each row in the Anti-Pattern Watch table: verify the "Why It Applies Here" cell opens with
[element name] (cat-N) -- before writing the next row -- do not complete the table and verify
after. A cell without the typed (cat-N) prefix at any row is a violation regardless of whether
prior rows complied.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  [HALT -- 4-item checklist -- Proceed only if all confirmed] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia:
    [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row -- do not complete and verify after] / table /
    [VERIFY: wrong type] / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist -- Proceed only if all confirmed] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE, four fields in order] /
    [VERIFY: future-tense fails] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify before next node]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK SITE 5 -- KEY ROLES -- per-cell: verify before next row, not after]
10. Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER -- per-cell: verify before next row, not after]
11. Committee Charters [CHECK SITE 3] [VERIFY: short Quorum]
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER (all four categories)
14. [TRIGGER-TYPE VOCAB] +
    [per-row: verify Type before next row -- do not complete and verify after] +
    Org Evolution Roadmap [VERIFY: duplicate threshold type]
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. [CAT-N-CITATION-SCHEMA] +
    [per-row: verify citation before next row -- do not complete and verify after] +
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Instruction-Site Consolidation: Single Mandatory Register per Governed Requirement (single axis)

**Axis**: Output format -- instruction-site consolidation for C-33 register consistency
**Hypothesis**: R12 V-04's C-33 failure is architectural: the DRI/Owner requirement is stated at two
instruction sites with different registers -- strict in the HALT checklist ("all values from
ROLE-NAME LOCK"), advisory in the co-located prose ("where a role is known"). The split exists
because the requirement appears twice. V-02 tests the architectural fix: each governed enforcement
requirement is stated at exactly one instruction site. For BEFORE-PRODUCE directives, the
HALT-AND-CONFIRM checklist is the sole statement of the requirement; the section-level prose
instruction for the same column contains no role-lock language at all (eliminating the co-location
entirely). Where a requirement must appear in a PRODUCE command for generation immediacy, it uses
the checklist formulation verbatim -- no alternative phrasing is permitted at that site. Built on
R12 V-04 base: HALT-AND-CONFIRM at all seven BEFORE-PRODUCE sites (C-31), per-row vocabulary
checks in all three vocabulary tables (C-32), FORMAT CONTRACT with DISQUALIFY-IF (C-20, C-23),
per-role-name charter directive (C-30). The advisory "where a role is known" line removed. DRI/Owner
section prose contains no role-lock instruction -- the HALT checklist is the only instruction site.
Tests whether single-site instruction eliminates split-register output without requiring per-cell
procedural directives (C-28 intentionally absent to isolate C-33 contribution).

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas. Reference this block at each BEFORE PRODUCING directive.
No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") -- five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.
    DRI / Owner: every value must be a role from the ROLE-NAME LOCK list.

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

Read `.craft/roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type: `(strategic) / (operational) / (advisory) / (governance)`.
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

Immediately after ROLE-TYPE-CLASSIFICATION, emit:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive applies: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

All five sites must honor this lock. A role name at any site not listed above is a violation.
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
value individually. A Type value outside the vocabulary at any row is a violation regardless of
whether prior rows complied.

VERIFY: A mechanism row with a Type value outside {Channel, Informal Role, Recurring Cadence,
Shared Artifact} does not satisfy this step.

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

Use this mandatory four-field form:

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

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN begins with "As we scale..." does not satisfy this
step.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Rating: `Strong / Moderate / Weak / Negligible / Insufficient`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list.
Verify before placing each node. Draw ASCII hierarchy (minimum two levels). Printable ASCII only.
Committees as distinct labeled nodes.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

BEFORE PRODUCING:
HALT.
  1. Confirm Area column will be present.
  2. Confirm Headcount column will be present.
  3. Confirm Key Roles column will be present -- every Key Roles value must be a role from ROLE-NAME LOCK.
  4. Confirm Decides column will be present as a standalone column -- not merged.
  5. Confirm Escalates column will be present as a standalone column -- not merged with Decides.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy
this step.

CHECK [SITE 5 -- KEY ROLES]: every role name in the Key Roles column must appear in the ROLE-NAME
LOCK list. No new role names may be introduced in this column. Minimum two area rows plus `**Total**`.

STEP 7 -- OPERATING RHYTHM TABLE

BEFORE PRODUCING:
HALT.
  1. Confirm Cadence column will be present.
  2. Confirm Frequency column will be present.
  3. Confirm DRI / Owner column will be present -- every DRI/Owner value must be a role from ROLE-NAME LOCK.
  4. Confirm Purpose column will be present.
  5. Confirm minimum three rows (ROB, shiproom/gate, governance) with no merged rows.
Proceed only if all five confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[No additional role-lock instruction for DRI/Owner column: the HALT checklist item 3 above is
the sole instruction site for this requirement -- no co-located instruction introduces different
language. Every DRI/Owner value must be a role from ROLE-NAME LOCK, as stated in checklist item 3.]

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

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the
ROLE-NAME LOCK list.

Per-role-name directive for Membership field:
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list
before appending the next name. Do not write the complete list and verify after -- verify each
name before adding the next. A novel role name at any position is a violation regardless of
whether earlier names complied.

Per-role-name directive for Decides field:
For each role name in the Decides field: verify the name appears in the ROLE-NAME LOCK list
before appending the next name. Same per-name rule as Membership.

VERIFY: A Quorum written as "[N] members required" without denominator M does not satisfy this
step. Re-read FORMAT CONTRACT schema (3) DISQUALIFY-IF. Fraction form [N] of [M] is required.

Escalates: must name a destination.

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

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

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold.
Row 2: different Type.

Per-row vocabulary check for trigger table:
For each row in the trigger table: verify the Type value appears in TRIGGER-TYPE VOCABULARY and
does not repeat the preceding row's Type before writing the next row. Do not complete the table
and verify after. An out-of-vocabulary Type or consecutive repeat at any row position is a
violation.

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

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (5) -- ANTI-PATTERN WATCH -- and confirm that
every "Why It Applies Here" cell will open with [element name] (cat-N) -- and that the
DISQUALIFY-IF condition will not be met.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

Per-row citation check:
For each row: verify the "Why It Applies Here" cell opens with [element name] (cat-N) -- before
writing the next row. Do not complete the table and verify after.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION
4.  [HALT -- 4-item checklist] ROLE-NAME LOCK (five-site enumeration, per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT -- 5-item schema (1) checklist] Headcount by Area [VERIFY: merged] [CHECK SITE 5]
11. [HALT -- 5-item schema (2) checklist, item 3: ROLE-NAME LOCK -- sole instruction site]
    Operating Rhythm Table [no co-located DRI/Owner prose instruction]
12. [HALT -- 5-item schema (3) checklist per charter] Committee Charters [CHECK SITE 3]
    [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT -- 4-item schema (4) checklist] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row Type verify] + Roadmap [VERIFY: duplicate type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [BEFORE PRODUCING schema (5)] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Phase-Gate Register-Consistency Audits (single axis)

**Axis**: Lifecycle emphasis -- backward-looking REGISTER-CONSISTENCY AUDIT at each phase gate
**Hypothesis**: V-01 prevents C-33 violations by fixing source language before generation. V-02
prevents them architecturally by eliminating co-located instruction sites. V-03 tests a third
mechanism: each phase gate includes a backward-looking REGISTER-CONSISTENCY AUDIT that confirms
no advisory qualifier was introduced for any governed enforcement requirement in the preceding
section before allowing the next section to begin. The audit enumerates each governed requirement
by site name and asks for explicit confirmation that mandatory-register language was used. If an
advisory qualifier is found, the gate requires correction before the next section begins. Built on
R12 V-03 base (STOP variant, per-cell per-row directives using DO NOT imperative register for
ROLE-NAME LOCK, per-cell role-lock for DRI/Owner and Key Roles already present). Phase gates
upgraded from labeled dividers to REGISTER-CONSISTENCY AUDIT + labeled transition. No FORMAT
CONTRACT (R12 V-03 base preserved). Tests whether retrospective catch at gate time achieves C-33
compliance as effectively as prospective prevention at source.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

Read `.craft/roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION

Produce immediately after ROLES-LOADED or ROLES-NOTE.
Three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No absent role may appear.

ROLE-NAME LOCK

STOP.
DO NOT emit the ROLE-NAME LOCK until the following are confirmed:
  1. Record: [N] roles found in ROLES-LOADED.
  2. Confirm: the lock list you are about to write contains exactly [N] entries.
  3. Confirm: every entry in the lock list appears verbatim in ROLES-LOADED.
  4. Confirm: no entry in the lock list was invented here and is absent from ROLES-LOADED.
DO NOT proceed until all four items above are confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
  (4) Inertia Assessment sub-sections -- every role name including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

A role name at any of these sites not listed above is a violation.
```

PHASE GATE 1 -- ROLES COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] ROLES-LOADED block: used mandatory listing language -- no advisory qualifier present.
  [ ] ROLE-TYPE-CLASSIFICATION: used mandatory classification language -- no advisory qualifier present.
  [ ] ROLE-NAME LOCK: used mandatory "no role name may appear" language -- no hedging or "where possible" present.
If any advisory qualifier was introduced at any of the above sites, correct it now before continuing.
DO NOT emit the phase gate until all three confirmed.

`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

DO NOT draw any org boxes until complete. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values: Channel / Informal Role / Recurring Cadence / Shared Artifact
No row may use a Type value outside this list.
```

Produce mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.

Per-row vocabulary check for mechanism table:
For each row: verify the Type value appears in MECHANISM-TYPE VOCABULARY before writing the next
row -- do not complete the table and verify after.

VERIFY: A Type value outside the vocabulary does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL:
STOP.
DO NOT begin writing any Rebuttal field until the following are confirmed:
  1. Confirm ROLE UNDER PRESSURE will be the first field label.
  2. Confirm OBSERVABLE BREAKDOWN will be the second field label.
  3. Confirm WHY EXISTING MECHANISMS FAIL will be the third field label.
  4. Confirm RE-ASSESSMENT TRIGGER will be the fourth field label.
DO NOT proceed until all four confirmed.

```
REBUTTAL FORM
=============
CHECK [SITE 4]: ROLE UNDER PRESSURE must name exactly one role from ROLE-NAME LOCK.
Verify the name appears in the lock before writing it.

ROLE UNDER PRESSURE:          [one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN:         [current failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [why Sub-section 1 mechanisms do not resolve this]
RE-ASSESSMENT TRIGGER:        [specific measurable threshold]
```

VERIFY: OBSERVABLE BREAKDOWN beginning with "As we scale..." does not satisfy this step.

Sub-section 4 -- VERDICT

`FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] -- [justification]`
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.

PHASE GATE 2 -- INERTIA COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] Mechanism table Type column: used mandatory vocabulary language -- no advisory qualifier
      such as "where available" or "if applicable" introduced at Type instruction site.
  [ ] Rebuttal ROLE UNDER PRESSURE: used mandatory "one role from ROLE-NAME LOCK" language --
      no "if applicable" or "where a role is known" present at the CHECK instruction site.
  [ ] VERDICT FLAT-CASE-PRESSURE: used rating from closed set -- no open-ended rating introduced.
If any advisory qualifier was introduced at any governed instruction site, correct it before continuing.
DO NOT emit the phase gate until all three confirmed.

`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK [SITE 1]: every role name in this diagram must appear in the ROLE-NAME LOCK list.
For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node --
do not complete the diagram and verify after.
Draw ASCII hierarchy (minimum two levels). Printable ASCII only. Committees as distinct nodes.

PHASE GATE 3 -- STRUCTURE COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] ASCII diagram CHECK instruction: used mandatory "must appear in ROLE-NAME LOCK" language --
      no "where possible" or "where a role is known" qualifier present at the CHECK instruction site.
  [ ] Every node label used in the diagram matches the mandatory per-node directive -- no advisory
      exception was applied to any node.
If any advisory qualifier was introduced at the diagram CHECK instruction site, correct it before continuing.
DO NOT emit the phase gate until confirmed.

`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates.
Minimum two area rows plus `**Total**`.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list
before populating the next row -- do not complete the column and verify after. Every Key Roles
cell value must be a role from ROLE-NAME LOCK. Key Roles format: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows. No merged rows.

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
For each cell in the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list
before populating the next row -- do not complete the column and verify after. Every DRI/Owner
value must be a role from ROLE-NAME LOCK.

COMMITTEE CHARTERS

Write a charter per governance meeting.
Fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
CHECK [SITE 3]: every role in Membership and Decides must appear in the ROLE-NAME LOCK list.
Quorum: `[N] of [M] member roles required`.
VERIFY: "[N] members required" without denominator M does not satisfy this step.

PHASE GATE 4 -- CHARTERS COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] Key Roles per-cell directive: used mandatory "must appear in ROLE-NAME LOCK" language --
      no "where possible" or "where a role is known" present at the Key Roles instruction site.
  [ ] DRI/Owner per-cell directive: used mandatory "must appear in ROLE-NAME LOCK" language --
      no "where a role is known" or conditional qualifier present at the DRI/Owner instruction site.
  [ ] Charter Membership directive: used mandatory "must appear in ROLE-NAME LOCK" language --
      no hedging at the Membership instruction site.
  [ ] Quorum directive: used mandatory "[N] of [M] member roles required" language -- no
      short-form instruction present at the Quorum instruction site.
If any advisory qualifier was introduced at any of these four instruction sites, correct before continuing.
DO NOT emit the phase gate until all four confirmed.

`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` / `cat-2 (Committees/Cadences)` / `cat-3 (Headcount)` / `cat-4 (DRI Roles)`
All four categories required. No category may be empty.

ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values:
  headcount threshold / workload signal / structural symptom / milestone event
No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold.
Row 2: different Type.

Per-row vocabulary check:
For each row: verify Type appears in TRIGGER-TYPE VOCABULARY and differs from the preceding row
before writing the next row.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

PHASE GATE 5 -- ORG-EVOLUTION COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] TRIGGER-TYPE VOCABULARY instruction: used mandatory "no row may" language -- no "where
      possible" or "try to use" qualifier present at the Type instruction site.
  [ ] Per-row vocabulary check: used mandatory "verify before writing the next row" language --
      no advisory "consider checking" or "aim to verify" at the per-row instruction site.
If any advisory qualifier was found, correct before continuing.
DO NOT emit the phase gate until confirmed.

`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes: cat-1 (Areas) / cat-2 (Committees/Cadences) / cat-3 (Headcount) / cat-4 (DRI Roles)
Required format: [element name] (cat-N) -- [one sentence]
A cell without (cat-N) prefix does not satisfy this schema.
```

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.

Per-row citation check:
For each row: verify "Why It Applies Here" opens with [element name] (cat-N) -- before writing
the next row.

VERIFY: A cell naming an org element without the `(cat-N)` typed prefix does not satisfy this step.

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION
3.  [STOP -- 4-item checklist with count-record -- DO NOT proceed until confirmed] ROLE-NAME LOCK
4.  [REGISTER-CONSISTENCY AUDIT: ROLES section] Phase Gate 1
5.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [STOP -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense] / VERDICT
6.  [REGISTER-CONSISTENCY AUDIT: INERTIA section] Phase Gate 2
7.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify]
8.  [REGISTER-CONSISTENCY AUDIT: STRUCTURE section] Phase Gate 3
9.  Headcount [CHECK SITE 5 -- per-cell verify before next row]
10. Operating Rhythm [CHECK SITE 2 -- per-cell verify before next row]
11. Committee Charters [CHECK SITE 3] [VERIFY: short Quorum]
12. [REGISTER-CONSISTENCY AUDIT: HEADCOUNT/RHYTHM/CHARTERS section] Phase Gate 4
13. ORG-ELEMENT REGISTER (all four categories)
14. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
15. [REGISTER-CONSISTENCY AUDIT: ROADMAP section] Phase Gate 5
16. [CAT-N-CITATION-SCHEMA] + [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- C-33 + C-34 Combined on R12 V-04 Baseline

**Axis**: Phrasing register + output format -- C-33 register consistency + C-34 procedural-action
directives, combined on R12 V-04 base
**Hypothesis**: R12 V-04 exposes two failure modes: (a) C-33: advisory "where a role is known"
co-located with strict HALT checklist item for DRI/Owner -- the checklist says "all values from
ROLE-NAME LOCK" (mandatory) while the PRODUCE-command prose says "where a role is known"
(conditional); (b) C-34/C-28: Key Roles is listed as a CHECK site but receives no per-cell
procedural directive -- neither per-cell action nor temporal constraint is specified. V-04
closes both on R12 V-04 base: C-33 fix removes the advisory co-located DRI/Owner instruction
entirely; the HALT checklist item becomes the sole instruction site for that requirement.
C-34 fix adds a full procedural per-cell directive to Key Roles column (action: "verify the value
appears in the ROLE-NAME LOCK list"; temporal: "before populating the next row -- do not complete
the table and verify after"), and confirms DRI/Owner per-cell directive already uses full procedural
form in the HALT checklist. FORMAT CONTRACT, per-row vocabulary enforcement (C-32), HALT-AND-CONFIRM
at all seven BEFORE-PRODUCE sites (C-31), and per-role-name charter directive (C-30) all preserved
from R12 V-04. C-28 added for Key Roles. Tests whether C-33 + C-34 together close the two observed
R12 V-04 failure modes without further changes.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas. Reference this block at each BEFORE PRODUCING directive.
No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates merged into a single column -- five columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.
    DRI / Owner: every cell value must be a role from the ROLE-NAME LOCK list.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles from ROLE-NAME LOCK)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward -- must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum omits denominator M (e.g., "3 members required") -- fraction form required.

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
    DISQUALIFY-IF: "Why It Applies Here" cell names an org element without (cat-N) prefix.

---

STEP 1 -- LOAD ROLES

Read `.craft/roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE:` instead. DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Produce `ROLE-TYPE-CLASSIFICATION:` immediately after ROLES-LOADED or ROLES-NOTE.
Three-tier order: strategic / operational / advisory+governance.
Type: `(strategic) / (operational) / (advisory) / (governance)`. Format: `- [role name] -- [domain type]`.
Every loaded role appears. No absent role appears.

STEP 3 -- EMIT ROLE-NAME LOCK

BEFORE PRODUCING THE ROLE-NAME LOCK:
HALT.
  1. Count the number of roles in ROLES-LOADED.
  2. Confirm the lock enumeration contains exactly that count -- no more, no fewer.
  3. Confirm every role in the enumeration is present in ROLES-LOADED.
  4. Confirm no role in the enumeration was invented here and is absent from ROLES-LOADED.
Proceed only if all four confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive applies: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]

All five sites must honor this lock. A role name at any site not listed above is a violation.
```

When emitted, emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until complete. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values:
  Channel / Informal Role / Recurring Cadence / Shared Artifact
No row may use a Type value outside this list.
```

Produce: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.

Per-row vocabulary check for mechanism table:
For each row: verify the Type value appears in MECHANISM-TYPE VOCABULARY before writing the next
row -- do not complete the table and verify after. A Type value outside the vocabulary at any row
position is a violation.

VERIFY: A row with Type outside {Channel, Informal Role, Recurring Cadence, Shared Artifact} does
not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL:
HALT.
  1. Confirm ROLE UNDER PRESSURE is the first field label.
  2. Confirm OBSERVABLE BREAKDOWN is the second field label.
  3. Confirm WHY EXISTING MECHANISMS FAIL is the third field label.
  4. Confirm RE-ASSESSMENT TRIGGER is the fourth field label.
Proceed only if all four confirmed.

```
REBUTTAL FORM
=============
CHECK [SITE 4 -- INERTIA]: ROLE UNDER PRESSURE must name exactly one role from ROLE-NAME LOCK.
Verify the name appears in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN:         [current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- hire count, named milestone,
                               or structural symptom]
```

VERIFY: OBSERVABLE BREAKDOWN beginning with "As we scale..." does not satisfy this step.

Sub-section 4 -- VERDICT

`FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] -- [justification]`
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.

When complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list.
Verify before placing each node. Draw ASCII hierarchy (minimum two levels). Printable ASCII only.
Committees as distinct labeled nodes.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

BEFORE PRODUCING:
HALT.
  1. Confirm Area column will be present.
  2. Confirm Headcount column will be present.
  3. Confirm Key Roles column will be present -- every Key Roles value must be a role from ROLE-NAME LOCK.
  4. Confirm Decides column will be present as a standalone column -- not merged.
  5. Confirm Escalates column will be present as a standalone column -- not merged with Decides.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table merging Decides and Escalates into a "Decision Scope" column does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list
before populating the next row -- do not complete the Key Roles column and verify after. A novel
role name at any Key Roles cell is a violation regardless of whether prior rows complied.

STEP 7 -- OPERATING RHYTHM TABLE

BEFORE PRODUCING:
HALT.
  1. Confirm Cadence column will be present.
  2. Confirm Frequency column will be present.
  3. Confirm DRI / Owner column will be present -- every DRI/Owner value must be a role from ROLE-NAME LOCK.
  4. Confirm Purpose column will be present.
  5. Confirm minimum three rows (ROB, shiproom/gate, governance) with no merged rows.
Proceed only if all five confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The DRI/Owner requirement is stated in checklist item 3 above. No additional DRI/Owner
role-lock instruction appears at this site -- checklist item 3 is the single instruction site
for this requirement. No advisory qualifier is present at any co-located instruction site.]

Per-cell directive for DRI/Owner column:
For each cell in the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list
before populating the next row -- do not complete the DRI / Owner column and verify after. A novel
role name at any DRI/Owner cell is a violation regardless of row position.

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

CHECK [SITE 3 -- CHARTER]: every role in Membership and Decides must appear in ROLE-NAME LOCK.

Per-role-name directive for Membership:
For each role name in Membership: verify it appears in ROLE-NAME LOCK before appending the next
name -- do not write the full list and verify after.

Per-role-name directive for Decides:
For each role name in Decides: verify it appears in ROLE-NAME LOCK before appending the next name.

VERIFY: A Quorum written as "[N] members required" without denominator M does not satisfy this
step. FORMAT CONTRACT schema (3) DISQUALIFY-IF applies. Fraction form [N] of [M] required.

Escalates: must name a destination.

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

BEFORE PRODUCING:
HALT.
  1. Confirm cat-1 (Areas) will be populated with area names and headcounts.
  2. Confirm cat-2 (Committees/Cadences) will be populated.
  3. Confirm cat-3 (Headcount) will be populated with the total.
  4. Confirm cat-4 (DRI Roles) will be populated.
Proceed only if all four confirmed.

Produce per schema (4) immediately after the charters gate. All four categories required.

STEP 10 -- ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values:
  headcount threshold / workload signal / structural symptom / milestone event
No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold.
Row 2: different Type.

Per-row vocabulary check for trigger table:
For each row: verify the Type value appears in TRIGGER-TYPE VOCABULARY and does not repeat the
preceding row's Type before writing the next row -- do not complete the table and verify after.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

STEP 11 -- ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes: cat-1 (Areas) / cat-2 (Committees/Cadences) / cat-3 (Headcount) / cat-4 (DRI Roles)
Required format for every "Why It Applies Here" cell: [element name] (cat-N) -- [one sentence]
A cell naming an org element without the (cat-N) prefix does not satisfy this schema.
```

BEFORE PRODUCING:
HALT.
  1. Confirm Anti-Pattern column will be present.
  2. Confirm Why It Applies Here column will be present -- every cell opens with [element name] (cat-N) --.
  3. Confirm Mitigation column will be present.
  4. Confirm minimum two rows.
Proceed only if all four confirmed.

Re-read FORMAT CONTRACT schema (5) DISQUALIFY-IF before producing.

Produce per schema (5). Minimum two rows.

Per-row citation check:
For each row: verify "Why It Applies Here" opens with [element name] (cat-N) -- before writing
the next row -- do not complete the table and verify after.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5; schema (2) states DRI/Owner requirement)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION
4.  [HALT -- 4-item checklist] ROLE-NAME LOCK
    (complete enumeration + five-site enumeration, per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia:
    [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row -- temporal constraint] / table / [VERIFY: wrong type] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT -- 5-item schema (1) checklist, item 3: ROLE-NAME LOCK]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5 -- per-cell: verify before next row]
11. [HALT -- 5-item schema (2) checklist, item 3: sole DRI/Owner instruction site]
    Operating Rhythm Table [per-cell DRI/Owner: verify before next row -- no advisory co-location]
12. [HALT -- 5-item schema (3) checklist per charter] Committee Charters [CHECK SITE 3]
    [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT -- 4-item schema (4) checklist] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row: verify before next row] + Roadmap [VERIFY: duplicate type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [HALT -- 4-item schema (5) checklist] +
    [per-row: citation verify before next row] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-33 + C-34 on R12 V-05 Baseline

**Axis**: All axes combined -- maximum mechanical stack with C-33 register consistency and C-34
procedural-action directives added to R12 V-05 base
**Hypothesis**: R12 V-05 achieves C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad),
C-25 (strict mandatory DRI/Owner), C-26 (HALT-AND-CONFIRM BEFORE-PRODUCE for all FC schemas),
C-27 (Key Roles fifth site), C-28 (per-cell DRI/Owner and Key Roles), C-29 (HALT-AND-CONFIRM
BEFORE-PRODUCE for non-FC structural forms), C-30 (per-role-name charter multi-role lists),
C-31 (HALT-AND-CONFIRM at all seven BEFORE-PRODUCE sites), C-32 (per-row vocabulary in all
three vocabulary tables). R13 V-05 adds C-33 and C-34: C-33 audit of R12 V-05 reveals that the
STEP 7 PRODUCE command retains a post-produce prose instruction for DRI/Owner that uses different
language from the HALT checklist item (the R12 V-04 failure pattern may propagate into V-05 if
not explicitly corrected); C-33 fix ensures the HALT checklist item is the sole instruction site
for the DRI/Owner role-lock requirement -- no co-located prose at the PRODUCE command introduces
different language. C-34 audit confirms Key Roles per-cell directive uses the full procedural form
("for each cell...verify...before populating the next row -- do not complete the table and verify
after") and DRI/Owner per-cell directive uses the same form; C-34 further confirms per-row
vocabulary directives at all three vocabulary tables specify the verification action and temporal
constraint. Together C-33 and C-34 close the two final documented failure modes: register
contamination via co-located softeners and emphatic-framing evasion at per-granularity sites.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations. Reference by schema number at each
BEFORE PRODUCING directive. No output is produced before reading this block.

(1) HEADCOUNT BY AREA
    Columns (exact order): Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates merged into one column -- five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns (exact order): Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate meeting, one governance meeting. No merged rows.
    DRI / Owner: every cell value must be a role from the ROLE-NAME LOCK list.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles; each from ROLE-NAME LOCK)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward -- must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum omits denominator M -- fraction form [N] of [M] is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               -- [area name] -- headcount: [N]
    cat-2 (Committees/Cadences) -- [name]
    cat-3 (Headcount)           -- Total headcount: [N]
    cat-4 (DRI Roles)           -- [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Columns (exact order): Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here": [element name] (cat-N) -- [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: "Why It Applies Here" cell names an org element without (cat-N) typed prefix.

---

STEP 1 -- LOAD ROLES

Read `.craft/roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE:` instead. DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Produce `ROLE-TYPE-CLASSIFICATION:` immediately after ROLES-LOADED or ROLES-NOTE.
Three-tier order: strategic / operational / advisory+governance.
Type: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role appears. No absent role appears.
Carry annotation to Key Roles (schema 1) and Charter Membership (schema 3).

STEP 3 -- EMIT ROLE-NAME LOCK

BEFORE PRODUCING THE ROLE-NAME LOCK:
HALT.
  1. Count the roles in ROLES-LOADED: record the count as [N].
  2. Confirm the lock enumeration contains exactly [N] entries -- no more, no fewer.
  3. Confirm every entry in the enumeration appears verbatim in ROLES-LOADED.
  4. Confirm no entry was invented here and is absent from ROLES-LOADED.
Proceed only if all four confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value
      [per-cell directive: verify each cell against this list before populating the next row]
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]
      [per-cell directive: verify each cell against this list before populating the next row]

All five sites honor this lock. A role name at any site not listed above is a violation.
```

When emitted, emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until complete. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values:
  Channel           -- async or sync communication path
  Informal Role     -- person-as-coordinator without formal title
  Recurring Cadence -- scheduled meeting or review cycle
  Shared Artifact   -- document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.

Per-row vocabulary check for mechanism table:
For each row: verify the Type value appears in MECHANISM-TYPE VOCABULARY before writing the next
row -- do not complete the table and verify after. A Type value outside the vocabulary at any
row position is a violation regardless of whether prior rows complied.

VERIFY: A row with Type outside {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

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
list above. No new role names may be introduced. Verify the name appears in the lock before writing.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [current coordination failure -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold -- specific hire count, named
                               milestone, or structural symptom such as two or more missed ship
                               dates attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN begins with "As we scale..." or "As the team grows..."
does not satisfy this step.

Sub-section 4 -- VERDICT

`FLAT-CASE-PRESSURE: [Strong / Moderate / Weak / Negligible / Insufficient] -- [justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different.

When complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

HALT.
  1. Confirm all node labels will be drawn from the ROLE-NAME LOCK list.
  2. Confirm printable ASCII characters only will be used.
  3. Confirm minimum two levels below the root.
  4. Confirm committees will appear as distinct labeled nodes, not embedded in area boxes.
Proceed only if all four confirmed.

CHECK [SITE 1 -- DIAGRAM]: every node label must appear in ROLE-NAME LOCK. For each node label:
verify it appears in ROLE-NAME LOCK before placing the next node.
Draw ASCII hierarchy. Printable ASCII only (+, -, |, text).

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (1):
HALT.
  1. Schema (1) column headers confirmed: Area | Headcount | Key Roles | Decides | Escalates.
  2. DISQUALIFY-IF confirmed: Decides and Escalates will not be merged into a single column.
  3. Key Roles confirmed: every value in this column must be a role from the ROLE-NAME LOCK list.
  4. Total row confirmed: will be present.
  5. Each area from the input will have its own row.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table merging Decides and Escalates into "Decision Scope" does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list
before populating the next row -- do not complete the Key Roles column and verify after. A novel
role name at any Key Roles cell is a violation regardless of whether prior rows complied.
Key Roles format: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (2):
HALT.
  1. Schema (2) column headers confirmed: Cadence | Frequency | DRI / Owner | Purpose.
  2. Minimum three rows confirmed: ROB, shiproom or gate, governance meeting.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
  4. No merged rows confirmed.
Proceed only if all four confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The DRI/Owner role-lock requirement is stated once in HALT checklist item 3 above. No
alternative or supplementary DRI/Owner role-lock instruction appears at this location.
No conditional qualifier such as "where a role is known" is present at any instruction site
for this requirement.]

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
For each cell in the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list
before populating the next row -- do not complete the DRI / Owner column and verify after. A
novel role name at any DRI/Owner cell is a violation regardless of row position.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter -- re-read FORMAT CONTRACT schema (3):
HALT.
  1. Purpose field confirmed: will be present.
  2. Membership field confirmed: will be present with minimum two roles from ROLE-NAME LOCK.
  3. Decides field confirmed: will be present.
  4. Escalates field confirmed: will be present -- must name a destination.
  5. Quorum field confirmed: will be present in fraction form [N] of [M] member roles required.
  6. DISQUALIFY-IF confirmed: Quorum will not omit denominator M.
Proceed only if all six confirmed.

CHECK [SITE 3 -- CHARTER]: every role in Membership and Decides must appear in ROLE-NAME LOCK.

Per-role-name directive for Membership field:
For each role name in Membership: verify it appears in ROLE-NAME LOCK before appending the next
name -- do not write the complete Membership list and verify after. A novel role name at any
position is a violation regardless of whether earlier names complied.

Per-role-name directive for Decides field:
For each role name in Decides: verify it appears in ROLE-NAME LOCK before appending the next name.
Same per-name rule as Membership.

VERIFY: A Quorum written as "[N] members required" without denominator M does not satisfy this
step. FORMAT CONTRACT schema (3) DISQUALIFY-IF confirms. Fraction form [N] of [M] required.

Escalates: must name a destination -- not "everything not listed under Decides."

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (4):
HALT.
  1. cat-1 (Areas) confirmed: will list area names with headcounts.
  2. cat-2 (Committees/Cadences) confirmed: will list each committee and cadence.
  3. cat-3 (Headcount) confirmed: will state total headcount.
  4. cat-4 (DRI Roles) confirmed: will list roles classified as strategic/DRI.
Proceed only if all four confirmed.

Produce per schema (4) immediately after the charters gate. All four categories required.
DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 -- ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values:
  headcount threshold -- a specific hire count that changes coordination needs
  workload signal     -- measurable increase in cross-area dependencies or throughput
  structural symptom  -- observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     -- named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold.
Row 2: different Type.

Per-row vocabulary check for trigger table:
For each row: verify the Type value appears in TRIGGER-TYPE VOCABULARY and does not repeat the
preceding row's Type before writing the next row -- do not complete the table and verify after.
An out-of-vocabulary Type or consecutive repeat at any row position is a violation regardless of
whether prior rows complied.

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

BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (5):
HALT.
  1. Anti-Pattern column confirmed: will be present.
  2. Why It Applies Here column confirmed: every cell will open with [element name] (cat-N) --.
  3. Mitigation column confirmed: will be present.
  4. Minimum two rows confirmed.
  5. DISQUALIFY-IF confirmed: no cell will name an org element without the (cat-N) typed prefix.
Proceed only if all five confirmed.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

Per-row citation check:
For each row: verify the "Why It Applies Here" cell opens with [element name] (cat-N) -- before
writing the next row -- do not complete the table and verify after. A cell without the typed
(cat-N) prefix at any row is a violation regardless of whether prior rows complied.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5; DRI/Owner req in schema 2)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier)
4.  [HALT -- 4-item checklist with count-record] ROLE-NAME LOCK
    (complete enumeration + five-site enumeration with per-cell notes at sites 2 and 5)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia:
    [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row -- temporal constraint, not after] /
    table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE] /
    [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  [HALT -- 4-item diagram checklist] ASCII Org Diagram [per-node verify before next node]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT -- re-read FC schema (1) -- 5-item checklist]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5 -- per-cell: verify before next row]
11. [HALT -- re-read FC schema (2) -- 4-item checklist, item 3: sole DRI/Owner instruction]
    Operating Rhythm Table [no co-located DRI/Owner advisory prose]
    [CHECK SITE 2 -- per-cell DRI/Owner: verify before next row]
12. [HALT -- re-read FC schema (3) -- 6-item checklist per charter] Committee Charters
    [CHECK SITE 3] [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT -- re-read FC schema (4) -- 4-item checklist] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] +
    [per-row: verify Type and non-repeat before next row -- temporal constraint] +
    Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] +
    [HALT -- re-read FC schema (5) -- 5-item checklist] +
    [per-row: citation verify before next row -- temporal constraint] +
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`
