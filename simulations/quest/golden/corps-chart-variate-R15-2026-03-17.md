---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 15
rubric: simulations/quest/rubrics/corps-chart-rubric-v14-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 15)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R15 targets the two new criteria added in v14 of the rubric:

- **C-37 -- ROLE-NAME LOCK block embeds per-name enforcement notes inline at charter fields
  (site 3: Membership and Decides)**:
  R14 V-01 added per-cell notes for sites 2 and 5 adjacent to the role-name enumeration in the
  ROLE-NAME LOCK block (C-36). R14 V-02 had per-role-name enforcement at the charter PRODUCE
  site (C-30) but not embedded in the ROLE-NAME LOCK block itself. C-37 requires the ROLE-NAME
  LOCK block to also embed an inline per-name enforcement note for site 3 (Membership / Decides):
  `[Membership / Decides -- per-name: for each role name in these fields, verify it appears in
  this list before adding the next name -- do not write the full list and verify after]`. The
  anti-drift prohibition must be present in the embedded note alongside the affirmative per-name
  verification action. Placement of the per-name directive only at the downstream charter PRODUCE
  site (satisfying C-30 alone) does not satisfy C-37.

- **C-38 -- HALT header at non-FC BEFORE-PRODUCE sites embeds structural form field contract in
  the HALT line itself**:
  R14 V-02 through V-05 upgraded FC-governed PRODUCE HALT headers to embed schema citations
  (C-35). The same pointer-decoupling failure mode exists for non-FC structural forms: the HALT
  before the ROLE-NAME LOCK block reads "HALT." and the HALT before the Rebuttal reads "HALT."
  -- the form field contract is a subsequent checklist item rather than the gate trigger itself.
  C-38 requires the structural form citation and field enumeration to appear in the HALT line:
  `HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY
  EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.` Recall cannot be bypassed without bypassing
  the HALT. C-35 closes pointer decoupling at FC sites; C-38 closes it at non-FC sites.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | ROLE-NAME LOCK site 3 note -- per-name embedded adjacent to role list (single axis: C-37) | C-37 | R14 V-01 embeds per-cell notes for sites 2 and 5 adjacent to the role-name enumeration. Site 3 (Membership / Decides) has a per-role-name directive at the downstream PRODUCE site but not embedded in the lock block. V-01 adds the per-name note immediately adjacent to the per-cell notes for sites 2 and 5, using the required form with anti-drift prohibition. The ROLE-NAME LOCK block now covers all three high-risk role-consuming sites at declaration time. Built on R14 V-01 base. No FORMAT CONTRACT -- C-35 and C-38 isolated out; V-01 isolates C-37 contribution alone. |
| V-02 | HALT header embeds non-FC structural form field contract (single axis: C-38) | C-38 | R14 V-02 upgraded all FC-governed PRODUCE HALT headers to embed schema citations (C-35). The HALT before the ROLE-NAME LOCK block and the HALT before the Rebuttal still read "HALT." with no form field contract. V-02 upgrades both: the ROLE-NAME LOCK HALT embeds the lock structure summary; the Rebuttal HALT embeds the four-field form contract. The recall action is syntactically part of the gate trigger at all non-FC BEFORE-PRODUCE sites. Built on R14 V-02 base (FORMAT CONTRACT + C-35 + HALT-AND-CONFIRM + per-row vocabulary + per-role-name charter). No C-36 or C-37 per-cell/per-name notes in ROLE-NAME LOCK block -- V-02 isolates C-38. |
| V-03 | ROLE-NAME LOCK site 3 note on STOP/audit base (single axis: C-37) | C-37 | R14 V-03 adds per-cell notes for sites 2 and 5 adjacent to the role list on the STOP/phase-gate-audit base. Site 3 has no embedded note. V-03 adds the per-name note for site 3 adjacent to the per-cell notes in the ROLE-NAME LOCK block, using full procedural form with anti-drift prohibition. Tests whether C-37 is compatible with the phase-gate REGISTER-CONSISTENCY AUDIT architecture: the gate-4 audit checks instruction-site register; the embedded site-3 note provides an earlier enforcement reference. Built on R14 V-03 base. No FORMAT CONTRACT -- C-38 not testable without FC governance of non-FC sites on this base. |
| V-04 | C-37 + C-38 combined on R14 V-04 base | C-37, C-38, all prior through C-36 | R14 V-04 carries C-20 through C-36 (FORMAT CONTRACT + DISQUALIFY-IF + HALT-AND-CONFIRM + C-35 schema citations + C-36 per-cell notes at sites 2 and 5 + C-33/C-34 procedural directives). The ROLE-NAME LOCK block has per-cell notes for sites 2 and 5 but no per-name note for site 3 (C-37 gap). The HALT at Rebuttal and the HALT at ROLE-NAME LOCK embed no form field contracts (C-38 gap). V-04 closes both: adds the per-name site 3 note to the ROLE-NAME LOCK block and upgrades both non-FC HALT headers to embed form field contracts. |
| V-05 | Full integration: C-37 + C-38 on R14 V-05 base -- all 38 criteria | C-37, C-38, all prior | Maximum mechanical stack. R14 V-05 carries C-20 through C-36 inclusive (FORMAT CONTRACT + DISQUALIFY-IF + per-cell DRI/Owner and Key Roles + per-name charter + per-row vocabulary + four-field Rebuttal + activation triad + HALT-AND-CONFIRM at all sites + C-35 schema citations in all FC HALT headers + C-36 per-cell notes for sites 2 and 5 in ROLE-NAME LOCK block + C-33/C-34 sole-instruction-site procedural directives). R15 V-05 adds: C-37 -- per-name enforcement note for site 3 (Membership / Decides) embedded adjacent to the per-cell notes in the ROLE-NAME LOCK block, with anti-drift prohibition; C-38 -- ROLE-NAME LOCK HALT header and Rebuttal HALT header both embed their respective structural form field contracts in the HALT line itself. Targets all 38 criteria. |

---

## V-01 -- ROLE-NAME LOCK Site 3 Note Adjacent to Role List (single axis: C-37)

**Axis**: ROLE-NAME LOCK block embeds per-name enforcement note for site 3 (Membership / Decides)
**Hypothesis**: R14 V-01 added per-cell notes for sites 2 (DRI/Owner) and 5 (Key Roles) immediately
adjacent to the role-name enumeration inside the ROLE-NAME LOCK block. Site 3 (Committee Charter
Membership and Decides) had a per-role-name directive at the downstream charter PRODUCE site (satisfying
C-30) but the co-location benefit did not extend to the lock block itself. V-01 adds the per-name note
immediately after the per-cell notes at sites 2 and 5, using the exact required form with anti-drift
prohibition. The ROLE-NAME LOCK block now serves as a co-located per-site instruction document for
all three high-risk role-consuming sites at declaration time. Built on R14 V-01 base (no FORMAT CONTRACT;
HALT-AND-CONFIRM at ROLE-NAME LOCK and Rebuttal sites; per-cell procedural directives at PRODUCE sites;
per-row vocabulary; five-site CHECK enumeration). C-38 not applied -- HALT lines remain "HALT." without
embedded form field contracts. Isolates C-37 contribution.

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

[DRI/Owner -- per-cell: for each cell in the Operating Rhythm Table DRI/Owner column, verify
the value appears in this list before populating the next row -- do not complete the DRI/Owner
column and verify after. A novel role name at any DRI/Owner cell is a violation regardless of
row position.]

[Key Roles -- per-cell: for each cell in the Headcount table Key Roles column, verify each name
appears in this list before populating the next row -- do not complete the Key Roles column and
verify after. A novel role name at any Key Roles cell is a violation regardless of row position.]

[Membership / Decides -- per-name: for each role name in the Committee Charter Membership and
Decides fields, verify it appears in this list before adding the next name -- do not write the
full list and verify after. A novel role name at any position in either field is a violation
regardless of whether earlier names in the same field complied.]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- per-cell directive above applies at every row
  (3) Committee Charter Membership and Decides fields -- per-name directive above applies at every name
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- per-cell directive above applies at every row [MANDATORY FIFTH SITE]

A role name at any of these five sites not listed above is a violation.
All five sites must be honored. Per-cell directives at sites 2 and 5 and per-name directive
at site 3 are embedded above.
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
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list before populating
the next row -- do not complete the Key Roles column and verify after. Apply this check to every
row individually. A novel role name at any Key Roles cell is a violation regardless of whether
prior rows complied. Key Roles format: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`. Four columns required.
Minimum three rows: one ROB, one shiproom or gate meeting, one governance meeting. No merged rows.

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list before populating the
next row -- do not complete the DRI / Owner column and verify after. Every DRI/Owner cell value
must be a role from ROLE-NAME LOCK. A novel role name at any DRI/Owner cell is a violation
regardless of row position.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table.
Fields per charter: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.

CHECK [SITE 3 -- CHARTER -- per-name directive]:
The per-name directive from the ROLE-NAME LOCK block applies here at every name position.
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list
before adding the next name -- do not write the full list and verify after.
For each role name in the Decides field: apply the same per-name verification before adding the
next name -- do not write the full list and verify after.
A novel role name at any position in Membership or Decides is a violation regardless of whether
earlier names in the same field complied.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: must name a destination.
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
    (complete role enumeration +
     [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] +
     [Membership/Decides per-name note adjacent to list] +
     five-site CHECK enumeration with per-cell at 2 and 5, per-name at 3)
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
9.  Headcount by Area [CHECK SITE 5 -- KEY ROLES -- per-cell: verify before next row, lock-declared directive applies]
10. Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER -- per-cell: verify before next row, lock-declared directive applies]
11. Committee Charters [CHECK SITE 3 -- per-name: verify Membership and Decides before each name, lock-declared directive applies] [VERIFY: short Quorum]
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

## V-02 -- HALT Header Embeds Non-FC Structural Form Field Contract (single axis: C-38)

**Axis**: HALT header embeds structural form field contract at non-FC BEFORE-PRODUCE sites
**Hypothesis**: R14 V-02 upgraded all FC-governed PRODUCE HALT headers to embed schema citations
(C-35): "HALT. Re-read FORMAT CONTRACT schema (N) -- [name]." The HALT before the ROLE-NAME LOCK
block reads "HALT." and the HALT before the Rebuttal reads "HALT." -- both non-FC structural forms
carry the pointer-decoupling failure mode that C-35 closes for FC sites. V-02 upgrades both non-FC
HALT header lines: the ROLE-NAME LOCK HALT embeds a summary of the lock structure; the Rebuttal
HALT embeds the four-field form contract. The recall action is syntactically inseparable from the
gate trigger at all non-FC BEFORE-PRODUCE sites. Built on R14 V-02 base: FORMAT CONTRACT with
DISQUALIFY-IF (C-20, C-23), C-35 schema citations in all FC HALT headers, HALT-AND-CONFIRM at all
BEFORE-PRODUCE sites (C-31), per-row vocabulary (C-32), per-role-name charter at PRODUCE site
(C-30), single-site DRI/Owner consolidation (C-33). No C-36 or C-37 inline notes in ROLE-NAME LOCK
block -- V-02 isolates C-38 contribution.

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
HALT. Re-read ROLE-NAME LOCK structure: complete role enumeration from ROLES-LOADED / no-novel-role constraint / governs five sites (diagram / DRI-Owner / Membership-Decides / Inertia / Key-Roles).
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
HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
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

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  1. Schema (1) columns confirmed: Area | Headcount | Key Roles | Decides | Escalates (five separate columns).
  2. DISQUALIFY-IF confirmed: Decides and Escalates will not be merged into a single column.
  3. Key Roles confirmed: every value must be a role from ROLE-NAME LOCK.
  4. Total row confirmed: will be present.
Proceed only if all four confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy
this step.

CHECK [SITE 5 -- KEY ROLES]: every role name in the Key Roles column must appear in the ROLE-NAME
LOCK list. No new role names may be introduced in this column. Minimum two area rows plus `**Total**`.

STEP 7 -- OPERATING RHYTHM TABLE

HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table.
  1. Schema (2) columns confirmed: Cadence | Frequency | DRI / Owner | Purpose.
  2. Minimum three rows confirmed: ROB, shiproom/gate, governance meeting. No merged rows.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
Proceed only if all three confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[No additional role-lock instruction for DRI/Owner column: the HALT checklist item 3 above is
the sole instruction site for this requirement -- no co-located instruction introduces different
language. Every DRI/Owner value must be a role from ROLE-NAME LOCK, as stated in checklist item 3.]

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter.
  1. Purpose field confirmed: will be present.
  2. Membership field confirmed: will be present with minimum two roles from ROLE-NAME LOCK.
  3. Decides field confirmed: will be present.
  4. Escalates field confirmed: will be present -- must name a destination.
  5. Quorum field confirmed: will be present in fraction form [N] of [M] member roles required.
  6. DISQUALIFY-IF confirmed: Quorum will not omit denominator M.
Proceed only if all six confirmed.

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

HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER.
  1. cat-1 (Areas) confirmed: will be populated with area names and headcounts.
  2. cat-2 (Committees/Cadences) confirmed: will be populated.
  3. cat-3 (Headcount) confirmed: will be populated with the total.
  4. cat-4 (DRI Roles) confirmed: will be populated.
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

HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch.
  1. Anti-Pattern column confirmed: will be present.
  2. Why It Applies Here column confirmed: every cell will open with [element name] (cat-N) --.
  3. Mitigation column confirmed: will be present.
  4. Minimum two rows confirmed.
  5. DISQUALIFY-IF confirmed: no cell will name an org element without the (cat-N) typed prefix.
Proceed only if all five confirmed.

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
4.  [HALT. Re-read ROLE-NAME LOCK structure: complete enumeration / no-novel-role constraint / governs five sites.
     -- 4-item checklist] ROLE-NAME LOCK (complete enumeration + five-site enumeration)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
     -- 4-item field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table. -- 4-item]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5]
11. [HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table. -- 3-item, sole DRI/Owner site]
    Operating Rhythm Table [no co-located advisory prose]
12. [HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter. -- 6-item per charter]
    Committee Charters [CHECK SITE 3] [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER. -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch. -- 5-item] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- ROLE-NAME LOCK Site 3 Note on STOP/Audit Base (single axis: C-37)

**Axis**: ROLE-NAME LOCK block embeds per-name enforcement note for site 3 -- C-37 on STOP/phase-gate-audit base
**Hypothesis**: R14 V-03 added per-cell notes for sites 2 and 5 adjacent to the role-name list on
the STOP/phase-gate-audit base. Site 3 (Membership / Decides) was governed only by a downstream
per-role-name directive at the charter PRODUCE site. V-03 adds the per-name note for site 3
immediately after the per-cell notes for sites 2 and 5 within the ROLE-NAME LOCK block, using
full procedural form with anti-drift prohibition. Tests C-37 on the STOP/audit base: the gate-4
REGISTER-CONSISTENCY AUDIT is extended to check that the Membership and Decides per-name instruction
sites used mandatory-register language consistent with the lock-embedded note. Built on R14 V-03
base. C-38 not applied -- STOP lines remain "STOP." without embedded form field contracts. Isolates C-37.

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

[DRI/Owner -- per-cell: for each cell in the Operating Rhythm Table DRI/Owner column, verify
the value appears in this list before populating the next row -- do not complete the DRI/Owner
column and verify after. A novel role name at any DRI/Owner cell is a violation regardless of
row position.]

[Key Roles -- per-cell: for each cell in the Headcount table Key Roles column, verify each name
appears in this list before populating the next row -- do not complete the Key Roles column and
verify after. A novel role name at any Key Roles cell is a violation regardless of row position.]

[Membership / Decides -- per-name: for each role name in the Committee Charter Membership and
Decides fields, verify it appears in this list before adding the next name -- do not write the
full list and verify after. A novel role name at any position in either field is a violation
regardless of whether earlier names in the same field complied.]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value; per-cell note above applies
  (3) Committee Charter Membership and Decides fields -- every role name; per-name note above applies
  (4) Inertia Assessment sub-sections -- every role name including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]; per-cell note above applies

A role name at any of these sites not listed above is a violation.
```

PHASE GATE 1 -- ROLES COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] ROLES-LOADED block: used mandatory listing language -- no advisory qualifier present.
  [ ] ROLE-TYPE-CLASSIFICATION: used mandatory classification language -- no advisory qualifier present.
  [ ] ROLE-NAME LOCK: used mandatory "no role name may appear" language -- no hedging or "where possible" present.
  [ ] ROLE-NAME LOCK per-cell notes: used mandatory procedural language at sites 2 and 5 -- no advisory qualifier present.
  [ ] ROLE-NAME LOCK per-name note: used mandatory procedural language at site 3 with anti-drift prohibition -- no advisory qualifier present.
If any advisory qualifier was introduced at any of the above sites, correct it now before continuing.
DO NOT emit the phase gate until all confirmed.

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
  [ ] Mechanism table Type column: used mandatory vocabulary language -- no advisory qualifier.
  [ ] Rebuttal ROLE UNDER PRESSURE: used mandatory "one role from ROLE-NAME LOCK" language -- no conditional qualifier.
  [ ] VERDICT FLAT-CASE-PRESSURE: used rating from closed set -- no open-ended rating introduced.
If any advisory qualifier was introduced at any governed instruction site, correct before continuing.
DO NOT emit the phase gate until all confirmed.

`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK [SITE 1]: every role name in this diagram must appear in the ROLE-NAME LOCK list.
For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node --
do not complete the diagram and verify after.
Draw ASCII hierarchy (minimum two levels). Printable ASCII only. Committees as distinct nodes.

PHASE GATE 3 -- STRUCTURE COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] ASCII diagram CHECK instruction: used mandatory "must appear in ROLE-NAME LOCK" language -- no "where possible" present.
  [ ] Every node label used in the diagram matches the mandatory per-node directive -- no advisory exception applied.
If any advisory qualifier was introduced at the diagram CHECK instruction site, correct before continuing.
DO NOT emit the phase gate until confirmed.

`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates.
Minimum two area rows plus `**Total**`.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here. For each cell in the Key Roles
column: verify the role name appears in the ROLE-NAME LOCK list before populating the next row --
do not complete the column and verify after. Every Key Roles cell value must be a role from
ROLE-NAME LOCK. Key Roles format: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows. No merged rows.

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here. For each cell in the DRI / Owner
column: verify the value appears in the ROLE-NAME LOCK list before populating the next row -- do
not complete the column and verify after. Every DRI/Owner value must be a role from ROLE-NAME LOCK.

COMMITTEE CHARTERS

Write a charter per governance meeting.
Fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.

CHECK [SITE 3 -- CHARTER -- per-name directive]:
The per-name directive from the ROLE-NAME LOCK block applies here at every name position.
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list
before adding the next name -- do not write the full list and verify after.
For each role name in the Decides field: apply the same per-name verification before adding the
next name -- do not write the full list and verify after.
A novel role name at any position in Membership or Decides is a violation regardless of whether
earlier names in the same field complied.
Quorum: `[N] of [M] member roles required`.
VERIFY: "[N] members required" without denominator M does not satisfy this step.

PHASE GATE 4 -- CHARTERS COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] Key Roles per-cell directive: used mandatory "must appear in ROLE-NAME LOCK" language -- no "where possible" present.
  [ ] DRI/Owner per-cell directive: used mandatory "must appear in ROLE-NAME LOCK" language -- no conditional qualifier present.
  [ ] Charter Membership per-name directive: used mandatory "must appear in ROLE-NAME LOCK" language with anti-drift prohibition -- no hedging.
  [ ] Charter Decides per-name directive: same -- mandatory language with anti-drift prohibition.
  [ ] Quorum directive: used mandatory "[N] of [M] member roles required" language -- no short-form present.
If any advisory qualifier was introduced at any of these five instruction sites, correct before continuing.
DO NOT emit the phase gate until all five confirmed.

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
before writing the next row -- do not complete the table and verify after.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

PHASE GATE 5 -- ORG-EVOLUTION COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] TRIGGER-TYPE VOCABULARY instruction: used mandatory "no row may" language -- no "where possible" present.
  [ ] Per-row vocabulary check: used mandatory "verify before writing the next row" language.
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
the next row -- do not complete the table and verify after.

VERIFY: A cell naming an org element without the `(cat-N)` typed prefix does not satisfy this step.

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION
3.  [STOP -- 4-item count-record checklist] ROLE-NAME LOCK
    (complete role enumeration +
     [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] +
     [Membership/Decides per-name note adjacent to list with anti-drift prohibition] +
     five-site enumeration with per-cell at 2 and 5, per-name at 3)
4.  [REGISTER-CONSISTENCY AUDIT: ROLES section -- 5-item including per-name note register check] Phase Gate 1
5.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [STOP -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense] / VERDICT
6.  [REGISTER-CONSISTENCY AUDIT: INERTIA section] Phase Gate 2
7.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify]
8.  [REGISTER-CONSISTENCY AUDIT: STRUCTURE section] Phase Gate 3
9.  Headcount [CHECK SITE 5 -- per-cell; lock-declared directive applies]
10. Operating Rhythm [CHECK SITE 2 -- per-cell; lock-declared directive applies]
11. Committee Charters [CHECK SITE 3 -- per-name; lock-declared directive applies] [VERIFY: short Quorum]
12. [REGISTER-CONSISTENCY AUDIT: HEADCOUNT/RHYTHM/CHARTERS section -- 5-item including per-name register check] Phase Gate 4
13. ORG-ELEMENT REGISTER (all four categories)
14. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
15. [REGISTER-CONSISTENCY AUDIT: ROADMAP section] Phase Gate 5
16. [CAT-N-CITATION-SCHEMA] + [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- C-37 + C-38 Combined on R14 V-04 Base

**Axis**: C-37 ROLE-NAME LOCK site 3 per-name note + C-38 non-FC HALT header form recall, combined on R14 V-04 base
**Hypothesis**: R14 V-04 carries C-20 through C-36. Two gaps remain for rubric v14:
(a) ROLE-NAME LOCK block has per-cell notes for sites 2 and 5 (C-36) but no per-name note for
site 3 -- the co-location benefit does not extend to charter fields without explicit embedding (C-37 gap);
(b) HALT at ROLE-NAME LOCK reads "HALT." and HALT at Rebuttal reads "HALT." -- the form field
contract is a subsequent checklist item rather than embedded in the gate trigger (C-38 gap).
V-04 closes both: adds the per-name note for site 3 with anti-drift prohibition adjacent to the
per-cell notes inside the ROLE-NAME LOCK block; upgrades the ROLE-NAME LOCK HALT header to embed
the lock structure summary and upgrades the Rebuttal HALT header to embed the four-field form
contract. Tests whether C-37 + C-38 stack cleanly on R14 V-04's C-33/C-34 architecture.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations. Reference by schema number at each
BEFORE PRODUCING directive. No output is produced before reading this block.

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
    "Why It Applies Here" format: [element name] (cat-N) -- [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without (cat-N) prefix.

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
HALT. Re-read ROLE-NAME LOCK structure: complete role enumeration from ROLES-LOADED / per-cell enforcement notes at sites 2 and 5 / per-name enforcement note at site 3 / no-novel-role constraint at all five sites.
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

[DRI/Owner -- per-cell: for each cell in the Operating Rhythm Table DRI/Owner column, verify
the value appears in this list before populating the next row -- do not complete the DRI/Owner
column and verify after. A novel role name at any DRI/Owner cell is a violation regardless of
row position.]

[Key Roles -- per-cell: for each cell in the Headcount table Key Roles column, verify each name
appears in this list before populating the next row -- do not complete the Key Roles column and
verify after. A novel role name at any Key Roles cell is a violation regardless of row position.]

[Membership / Decides -- per-name: for each role name in the Committee Charter Membership and
Decides fields, verify it appears in this list before adding the next name -- do not write the
full list and verify after. A novel role name at any position in either field is a violation
regardless of whether earlier names in the same field complied.]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- per-cell directive above applies at every row
  (3) Committee Charter Membership and Decides fields -- per-name directive above applies at every name
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- per-cell directive above applies at every row [MANDATORY FIFTH SITE]

A role name at any of these five sites not listed above is a violation.
All five sites must be honored. Per-cell directives at sites 2 and 5 and per-name directive at
site 3 are embedded above.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until complete. Four sub-sections in order.

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
before writing the next row. Do not complete the table and verify after. A Type value outside the
vocabulary at any row is a violation regardless of whether prior rows complied.

VERIFY: A mechanism row with a Type value outside {Channel, Informal Role, Recurring Cadence,
Shared Artifact} does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL:
HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
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
                               or structural symptom such as two or more missed ship dates]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN begins with "As we scale..." does not satisfy this step.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Rating: `Strong / Moderate / Weak / Negligible / Insufficient`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list.
For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node --
do not complete the diagram and verify after. Draw ASCII hierarchy (minimum two levels). Printable
ASCII only. Committees as distinct labeled nodes.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  1. Schema (1) columns confirmed: Area | Headcount | Key Roles | Decides | Escalates (five separate columns).
  2. DISQUALIFY-IF confirmed: Decides and Escalates will not be merged into a single column.
  3. Key Roles confirmed: every value must be a role from ROLE-NAME LOCK, annotated [role name] ([domain type]).
  4. Total row confirmed: will be present.
Proceed only if all four confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy
this step.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list before populating
the next row -- do not complete the Key Roles column and verify after. A novel role name at any
Key Roles cell is a violation regardless of whether prior rows complied.

STEP 7 -- OPERATING RHYTHM TABLE

HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table.
  1. Schema (2) columns confirmed: Cadence | Frequency | DRI / Owner | Purpose.
  2. Minimum three rows confirmed: ROB, shiproom/gate, governance meeting. No merged rows.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
Proceed only if all three confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The HALT checklist item 3 above is the sole instruction site for the DRI/Owner role-lock
requirement. No co-located instruction uses different language. Every DRI/Owner value must be
a role from ROLE-NAME LOCK, exactly as stated in checklist item 3.]

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list before populating the
next row -- do not complete the column and verify after. A novel role name at any DRI/Owner cell
is a violation regardless of row position.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter.
  1. Purpose field confirmed: will be present.
  2. Membership field confirmed: will be present with minimum two roles from ROLE-NAME LOCK.
  3. Decides field confirmed: will be present.
  4. Escalates field confirmed: will be present -- must name a destination.
  5. Quorum field confirmed: will be present in fraction form [N] of [M] member roles required.
  6. DISQUALIFY-IF confirmed: Quorum will not omit denominator M.
Proceed only if all six confirmed.

CHECK [SITE 3 -- CHARTER -- per-name directive]:
The per-name directive from the ROLE-NAME LOCK block applies here at every name position.
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list
before adding the next name -- do not write the full list and verify after.
For each role name in the Decides field: apply the same per-name verification before adding the
next name -- do not write the full list and verify after.
A novel role name at any position in Membership or Decides is a violation regardless of whether
earlier names in the same field complied.
Escalates: must name a destination.

VERIFY: A Quorum written as "[N] members required" without denominator M does not satisfy this
step. Re-read FORMAT CONTRACT schema (3) DISQUALIFY-IF. Fraction form [N] of [M] is required.

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER.
  1. cat-1 (Areas) confirmed: will be populated with area names and headcounts.
  2. cat-2 (Committees/Cadences) confirmed: will be populated.
  3. cat-3 (Headcount) confirmed: will be populated with the total.
  4. cat-4 (DRI Roles) confirmed: will be populated.
Proceed only if all four confirmed.

Produce per schema (4). All four categories required. DO NOT proceed until all four are populated.

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
For each row: verify Type appears in TRIGGER-TYPE VOCABULARY and does not repeat the preceding
row's Type before writing the next row. Do not complete the table and verify after.

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

HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch.
  1. Anti-Pattern column confirmed: will be present.
  2. Why It Applies Here column confirmed: every cell will open with [element name] (cat-N) --.
  3. Mitigation column confirmed: will be present.
  4. Minimum two rows confirmed.
  5. DISQUALIFY-IF confirmed: no cell will name an org element without the (cat-N) typed prefix.
Proceed only if all five confirmed.

Produce per schema (5). Minimum two rows.

Per-row citation check:
For each row: verify "Why It Applies Here" opens with [element name] (cat-N) -- before writing
the next row. Do not complete the table and verify after.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION
4.  [HALT. Re-read ROLE-NAME LOCK structure: complete enumeration / per-cell at sites 2+5 / per-name at site 3 / no-novel-role constraint.
     -- 4-item checklist] ROLE-NAME LOCK
    (complete role enumeration +
     [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] +
     [Membership/Decides per-name note adjacent to list with anti-drift prohibition] +
     five-site CHECK enumeration with per-cell at 2 and 5, per-name at 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
     -- 4-item field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table. -- 4-item]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5 -- per-cell; lock-declared directive applies]
11. [HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table. -- 3-item, sole DRI/Owner site]
    Operating Rhythm Table [CHECK SITE 2 -- per-cell; no co-located advisory prose]
12. [HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter. -- 6-item per charter]
    Committee Charters [CHECK SITE 3 -- per-name; lock-declared directive applies] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER. -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch. -- 5-item] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-37 + C-38 on R14 V-05 Base (all 38 criteria)

**Axis**: Maximum mechanical stack -- C-37 + C-38 added to R14 V-05 base targeting all 38 criteria
**Hypothesis**: R14 V-05 carries C-20 through C-36. Two remaining gaps:
(a) ROLE-NAME LOCK block has per-cell notes at sites 2 and 5 (C-36) but no per-name note at site
3. The R14 V-01 C-30 PARTIAL demonstrated this: per-name verification intent at charter fields
without the anti-drift prohibition and without co-location in the lock block does not satisfy C-37.
(b) HALT at ROLE-NAME LOCK and HALT at Rebuttal both read "HALT." -- recall is a checklist item
after the gate rather than embedded in the gate trigger (C-38 gap).
V-05 closes both: adds per-name note for site 3 with anti-drift prohibition adjacent to per-cell
notes in ROLE-NAME LOCK block; upgrades ROLE-NAME LOCK HALT and Rebuttal HALT to embed their
respective structural form field contracts in the HALT line itself. Targeting all 38 criteria.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations. Reference by schema number at each
BEFORE PRODUCING directive. No output is produced before reading this block.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]) from ROLE-TYPE-CLASSIFICATION. Total row required.
    DISQUALIFY-IF: Decides and Escalates merged into a single column (e.g., "Decision Scope") --
                   five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate meeting, one governance meeting. No merged rows.
    DRI / Owner: every cell value must be a role from the ROLE-NAME LOCK list.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles from ROLE-NAME LOCK)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward -- must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum omits denominator M (e.g., "3 members required") --
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
HALT. Re-read ROLE-NAME LOCK structure: complete role enumeration from ROLES-LOADED / per-cell enforcement notes at DRI/Owner (site 2) and Key Roles (site 5) / per-name enforcement note at Membership/Decides (site 3) / no-novel-role constraint at all five sites.
  1. Count the number of roles in the ROLES-LOADED block.
  2. Confirm the lock enumeration you are about to write contains exactly that count -- no more, no fewer.
  3. Confirm every role in the enumeration is present in ROLES-LOADED.
  4. Confirm no role in the enumeration was invented here and not present in ROLES-LOADED.
Proceed only if all four confirmed.

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block exactly:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

[DRI/Owner -- per-cell: for each cell in the Operating Rhythm Table DRI/Owner column, verify
the value appears in this list before populating the next row -- do not complete the DRI/Owner
column and verify after. A novel role name at any DRI/Owner cell is a violation regardless of
row position.]

[Key Roles -- per-cell: for each cell in the Headcount table Key Roles column, verify each name
appears in this list before populating the next row -- do not complete the Key Roles column and
verify after. A novel role name at any Key Roles cell is a violation regardless of row position.]

[Membership / Decides -- per-name: for each role name in the Committee Charter Membership and
Decides fields, verify it appears in this list before adding the next name -- do not write the
full list and verify after. A novel role name at any position in either field is a violation
regardless of whether earlier names in the same field complied.]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- per-cell directive above applies at every row
  (3) Committee Charter Membership and Decides fields -- per-name directive above applies at every name
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- per-cell directive above applies at every row [MANDATORY FIFTH SITE]

A role name at any of these five sites not listed above is a violation.
All five sites must be honored. Per-cell directives at sites 2 and 5 and per-name directive at
site 3 are embedded above. These directives travel with the lock and govern those sites from
declaration time.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

DO NOT draw any org boxes until the Inertia Assessment is complete. Write all four sub-sections in order.

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
HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
  1. Confirm ROLE UNDER PRESSURE is the first field label in the form.
  2. Confirm OBSERVABLE BREAKDOWN is the second field label.
  3. Confirm WHY EXISTING MECHANISMS FAIL is the third field label.
  4. Confirm RE-ASSESSMENT TRIGGER is the fourth field label.
Proceed only if all four confirmed.

Use this mandatory four-field form. The embedded CHECK and VERIFY are part of the form -- do not skip either:

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

VERIFY [REBUTTAL]: A Rebuttal where OBSERVABLE BREAKDOWN begins with "As we scale..." or
"as the team grows..." does not satisfy this step. The breakdown must describe a failure that
exists now. A ROLE UNDER PRESSURE value absent from the ROLE-NAME LOCK list does not satisfy
this step.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from closed set: `Strong / Moderate / Weak / Negligible / Insufficient`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning must reference
the FLAT-CASE-PRESSURE rating by name.
RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different context required.
DO NOT proceed past VERDICT until pressure line, declaration, and re-assessment trigger are all present.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK
list. For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node
-- do not complete the diagram and verify after. A label absent from ROLE-NAME LOCK is a violation
regardless of position.
Draw ASCII hierarchy with minimum two levels. Use only printable ASCII characters (+, -, |, and text).
Committees as distinct labeled nodes -- not embedded in an area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  1. Schema (1) columns confirmed: Area | Headcount | Key Roles | Decides | Escalates (five separate columns).
  2. DISQUALIFY-IF confirmed: Decides and Escalates will not be merged into a single column.
  3. Key Roles confirmed: every value must be a role from ROLE-NAME LOCK, annotated [role name] ([domain type]).
  4. Total row confirmed: will be present.
Proceed only if all four confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy
schema (1) of the FORMAT CONTRACT. The five-column structure is required.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list before populating
the next row -- do not complete the Key Roles column and verify after. Apply this check to every
row individually. A novel role name at any Key Roles cell is a violation regardless of whether
prior rows complied. Key Roles format: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table.
  1. Schema (2) columns confirmed: Cadence | Frequency | DRI / Owner | Purpose.
  2. Minimum three rows confirmed: ROB, one shiproom or gate meeting, one governance meeting. No merged rows.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list -- no new role names introduced.
Proceed only if all three confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The HALT checklist item 3 above is the sole instruction site for the DRI/Owner role-lock
requirement. No co-located instruction at this step uses different language. Every DRI/Owner
value must be a role from ROLE-NAME LOCK, exactly as stated in checklist item 3.]

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list before populating the
next row -- do not complete the DRI / Owner column and verify after. A novel role name at any
DRI/Owner cell is a violation regardless of row position.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter.
  1. Purpose field confirmed: will be present.
  2. Membership field confirmed: will be present with minimum two roles from ROLE-NAME LOCK.
  3. Decides field confirmed: will be present.
  4. Escalates field confirmed: will be present -- must name a destination.
  5. Quorum field confirmed: will be present in fraction form [N] of [M] member roles required for binding decisions.
  6. DISQUALIFY-IF confirmed: Quorum will not omit denominator M.
Proceed only if all six confirmed.

CHECK [SITE 3 -- CHARTER -- per-name directive]:
The per-name directive from the ROLE-NAME LOCK block applies here at every name position.
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list
before adding the next name -- do not write the full list and verify after. A novel role name at
any position in Membership is a violation regardless of whether earlier names complied.
For each role name in the Decides field: apply the same per-name verification before adding the
next name -- do not write the full list and verify after. A novel role name at any position in
Decides is a violation regardless of whether earlier names in the same field complied.
Escalates: must name a destination. Membership minimum: two roles annotated `[role name] ([domain type])`.

VERIFY [QUORUM]: A Quorum written as "[N] members required" without the denominator M does not
satisfy FORMAT CONTRACT schema (3) DISQUALIFY-IF. The fraction form [N] of [M] member roles
required for binding decisions is mandatory. A charter that omits the Quorum field entirely does
not satisfy this step.

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER.
  1. cat-1 (Areas) confirmed: will be populated with all area names and headcounts from the Headcount table.
  2. cat-2 (Committees/Cadences) confirmed: will be populated with all committee and cadence names.
  3. cat-3 (Headcount) confirmed: will be populated with total headcount.
  4. cat-4 (DRI Roles) confirmed: will be populated with all DRI role names from the Rhythm Table.
Proceed only if all four confirmed.

Produce per schema (4) immediately after the charters gate.
All four categories required. No category may be empty.
DO NOT proceed to Org Evolution Roadmap until all four categories are populated.

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

Produce: `Trigger | Structural Change | Type`. Minimum two rows.
Row 1: a headcount threshold trigger. Row 2: must use a different Type value than Row 1.

Per-row vocabulary check for trigger table:
For each row in the trigger table: verify the Type value appears in TRIGGER-TYPE VOCABULARY and
does not repeat the preceding row's Type before writing the next row -- do not complete the table
and verify after. An out-of-vocabulary Type or consecutive repeat at any row position is a
violation regardless of whether prior rows complied.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step. A trigger table with
fewer than two rows does not satisfy this step.

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

HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch.
  1. Anti-Pattern column confirmed: will be present.
  2. Why It Applies Here column confirmed: every cell will open with [element name] (cat-N) -- followed by one sentence.
  3. Mitigation column confirmed: will be present.
  4. Minimum two rows confirmed.
  5. DISQUALIFY-IF confirmed: no cell will name an org element without the (cat-N) typed prefix.
Proceed only if all five confirmed.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

Per-row citation check for Anti-Pattern Watch:
For each row in the Anti-Pattern Watch table: verify the "Why It Applies Here" cell opens with
[element name] (cat-N) -- before writing the next row -- do not complete the table and verify
after. A cell without the typed (cat-N) prefix at any row is a violation regardless of whether
prior rows complied.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy FORMAT CONTRACT schema (5) citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (schemas 1-5 with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  [HALT. Re-read ROLE-NAME LOCK structure: complete enumeration / per-cell at DRI/Owner (site 2) + Key Roles (site 5) / per-name at Membership/Decides (site 3) / no-novel-role constraint at all five sites.
     -- 4-item checklist -- Proceed only if all confirmed]
    ROLE-NAME LOCK (complete role enumeration +
     [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] +
     [Membership/Decides per-name note adjacent to list with anti-drift prohibition] +
     five-site CHECK enumeration with per-cell at 2 and 5, per-name at 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia:
    [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row -- do not complete and verify after] / table /
    [VERIFY: wrong type fails] / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
     -- 4-item field checklist -- Proceed only if all confirmed] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE] /
    [VERIFY: future-tense fails; absent-from-lock fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify before next node]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table. -- 4-item]
    Headcount by Area [VERIFY: merged Decides/Escalates fails schema (1)] [CHECK SITE 5 -- per-cell; lock-declared directive applies]
11. [HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table. -- 3-item; sole DRI/Owner instruction site]
    Operating Rhythm Table [CHECK SITE 2 -- per-cell; lock-declared directive applies; no co-located advisory prose]
12. [HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter. -- 6-item per charter]
    Committee Charters [CHECK SITE 3 -- per-name for Membership and Decides; lock-declared directive applies]
    [VERIFY: short Quorum fails schema (3) DISQUALIFY-IF]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER. -- 4-item] ORG-ELEMENT REGISTER (all four categories)
15. [TRIGGER-TYPE VOCAB] + [per-row: verify Type before next row] + Org Evolution Roadmap
    [VERIFY: duplicate threshold type fails]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch. -- 5-item] +
    [per-row: verify citation before next row] + Anti-Pattern Watch
    [VERIFY: untyped citation fails schema (5) DISQUALIFY-IF]

End with: `Generated by: /org-chart {topic} -- {date}`
