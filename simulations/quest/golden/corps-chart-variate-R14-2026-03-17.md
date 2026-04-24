---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 14
rubric: simulations/quest/rubrics/corps-chart-rubric-v13-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 14)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R14 targets the two new criteria added in v13 of the rubric:

- **C-35 -- HALT header embeds FORMAT CONTRACT schema recall**:
  R13 V-05 uses `BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (N):\nHALT.` at every
  FC-governed PRODUCE step. The schema citation appears in the BEFORE-PRODUCING label line;
  the HALT line itself reads "HALT." with no schema reference. C-35 requires the schema citation
  to appear in the HALT header line itself -- e.g., "HALT. Re-read FORMAT CONTRACT schema (1) --
  headcount table." -- so the recall action is syntactically part of the gate trigger and cannot
  be bypassed without bypassing the HALT.

- **C-36 -- ROLE-NAME LOCK block embeds per-cell enforcement notes inline at sites 2 and 5**:
  R13 V-05 places `[per-cell directive: verify each cell against this list before populating the
  next row]` notes inside the CHECK SITES enumeration at entries (2) and (5). C-36 requires the
  notes to be adjacent to the role-name enumeration itself (not only in the sites enumeration),
  use full procedural form with temporal constraint and explicit site naming, and follow the exact
  format `[DRI/Owner -- per-cell: for each cell in this column, verify the value appears in this
  list before populating the next row -- do not complete the table and verify after]` and
  `[Key Roles -- per-cell: ...]`. Placement in the sites enumeration alone satisfies the spirit
  but not the letter of C-36's "adjacent to the role-name enumeration" requirement.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | ROLE-NAME LOCK inline notes -- adjacent placement and full procedural form (single axis) | C-36 | R13 V-01 places per-cell directives at PRODUCE-command sites only. The per-cell enforcement procedure for DRI/Owner and Key Roles is separated from the ROLE-NAME LOCK declaration by hundreds of tokens of intervening content. V-01 adds per-cell notes immediately adjacent to the role-name list within the ROLE-NAME LOCK block, using full procedural form with site-specific labeling ("DRI/Owner -- per-cell: for each cell... -- do not complete the table and verify after"). The enforcement procedure travels with the lock declaration. Built on R13 V-01 base (no FORMAT CONTRACT). C-35 not testable without FC -- V-01 isolates C-36 contribution. |
| V-02 | HALT header embeds FORMAT CONTRACT schema citation (single axis) | C-35 | R13 V-02 uses HALT-AND-CONFIRM at all FC-governed BEFORE-PRODUCE sites, but each HALT line reads "HALT." with no schema citation -- the schema reference appears in the BEFORE-PRODUCING label above the HALT line. V-02 merges the label and HALT into a single line: "HALT. Re-read FORMAT CONTRACT schema (N) -- [name]." at every FC-governed PRODUCE step. The schema citation is syntactically part of the HALT instruction; the recall cannot be skipped without bypassing the HALT. Built on R13 V-02 base (FORMAT CONTRACT present, single-site DRI/Owner consolidation, per-row vocabulary, no per-cell C-28). Isolates C-35 contribution. |
| V-03 | ROLE-NAME LOCK inline notes -- compact form on STOP variant base (single axis) | C-36 | R13 V-03 uses STOP variant with phase-gate register audits and no FORMAT CONTRACT. The ROLE-NAME LOCK block has no per-cell notes at sites 2 and 5. V-03 adds inline per-cell notes adjacent to the role-name list within the ROLE-NAME LOCK block using the same full procedural form as V-01. Tests whether C-36 inline notes are compatible with the phase-gate audit architecture: does the declaration-time per-cell note conflict with or complement the gate-time register audit? Built on R13 V-03 base. C-35 not testable without FC -- V-03 isolates C-36 on the STOP/audit base. |
| V-04 | C-35 + C-36 combined on R13 V-04 base | C-35, C-36, all prior through C-34 | R13 V-04 achieves C-33 + C-34 on R12 V-04 base (FORMAT CONTRACT, HALT at all BEFORE-PRODUCE sites, no co-located advisory DRI/Owner prose, full procedural per-cell directives at PRODUCE sites). The HALT headers read "HALT." without schema citation (C-35 gap) and the ROLE-NAME LOCK sites enumeration carries short `[per-cell directive]` notes that are not adjacent to the role-name list and do not use full procedural form (C-36 gap). V-04 closes both: HALT headers embed schema citations at all FC-governed PRODUCE steps; ROLE-NAME LOCK block embeds full per-cell notes adjacent to the role enumeration. Together with R13 V-04's C-33/C-34 stack, tests whether C-35+C-36 can be added without introducing new register splits or emphatic-framing evasion. |
| V-05 | Full integration: C-35 + C-36 on R13 V-05 base | C-35, C-36, all prior | Maximum mechanical stack. R13 V-05 carries C-20 through C-34 inclusive (FORMAT CONTRACT, DISQUALIFY-IF, per-cell DRI/Owner + Key Roles, per-row vocabulary, per-role-name charter, four-field Rebuttal, activation triad, HALT-AND-CONFIRM at all sites, strict DRI/Owner sole-instruction-site consolidation). R14 V-05 adds: C-35 -- HALT headers at all FC-governed PRODUCE steps (schemas 1-5) embed the schema citation in the HALT line itself; C-36 -- ROLE-NAME LOCK block embeds full per-cell enforcement notes immediately after the role-name list for sites 2 and 5, using exact required form ("DRI/Owner -- per-cell: for each cell...verify...before populating the next row -- do not complete the table and verify after"). The combined fix targets dual convergence: all 36 criteria satisfied. |

---

## V-01 -- ROLE-NAME LOCK Adjacent Per-Cell Notes (single axis: C-36)

**Axis**: ROLE-NAME LOCK inline per-cell notes -- adjacent to role-name list, full procedural form
**Hypothesis**: R13 V-01 per-cell directives appear at PRODUCE-command sites (STEP 5 Key Roles,
STEP 6 DRI/Owner), hundreds of tokens from the ROLE-NAME LOCK declaration. The per-cell
enforcement procedure must be recalled from downstream. V-01 adds full per-cell notes immediately
adjacent to the role-name enumeration within the ROLE-NAME LOCK block, converting the declaration
from a name list into a co-located per-site instruction document. Built on R13 V-01 base: HALT for
ROLE-NAME LOCK, HALT for Rebuttal (C-31), four-field Rebuttal (C-14), five-site CHECK enumeration
(C-21, C-27), per-cell DRI/Owner + Key Roles at PRODUCE sites with procedural form (C-28, C-34),
per-row vocabulary with temporal constraints (C-32), no FORMAT CONTRACT. C-35 not achievable
without FC -- isolates C-36 contribution.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:`
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

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- per-cell directive above applies at every row
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- per-cell directive above applies at every row [MANDATORY FIFTH SITE]

A role name at any of these five sites not listed above is a violation.
All five sites must be honored. Per-cell directives at sites 2 and 5 are embedded above.
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
    (complete role enumeration + [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] + five-site CHECK enumeration)
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

## V-02 -- HALT Header Embeds FORMAT CONTRACT Schema Citation (single axis: C-35)

**Axis**: HALT header schema recall -- schema citation moved from BEFORE-PRODUCING label into HALT line
**Hypothesis**: R13 V-02 places "re-read FORMAT CONTRACT schema (N)" in the BEFORE-PRODUCING label
above the HALT line. The HALT line reads "HALT." with no schema reference. A model that processes
the HALT and advances toward the PROCEED-ONLY-IF gate without fully processing each checklist item
loses the recall directive when it appears only as a checklist item or label. V-02 merges the
schema reference into the HALT header itself: "HALT. Re-read FORMAT CONTRACT schema (N) -- [name]."
at every FC-governed PRODUCE step. The schema citation is syntactically inseparable from the gate
trigger -- recall cannot be bypassed without bypassing the HALT. Built on R13 V-02 base: FORMAT
CONTRACT with DISQUALIFY-IF (C-20, C-23), single-site DRI/Owner consolidation (C-33), HALT-AND-CONFIRM
at all BEFORE-PRODUCE sites (C-31), per-row vocabulary checks (C-32), per-role-name charter (C-30).
No per-cell C-28 directives at PRODUCE sites -- C-35 isolated by preserving R13 V-02 mechanical
stack unchanged except HALT header upgrade.

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

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` instead.
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
4.  [HALT -- 4-item checklist] ROLE-NAME LOCK (complete enumeration + five-site enumeration with per-role-name at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist] /
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

## V-03 -- ROLE-NAME LOCK Adjacent Per-Cell Notes on STOP Variant Base (single axis: C-36)

**Axis**: ROLE-NAME LOCK inline per-cell notes -- C-36 on STOP/phase-gate-audit base without FORMAT CONTRACT
**Hypothesis**: R13 V-03 (phase-gate register audits, STOP variant) has a ROLE-NAME LOCK block
listing roles and five sites but no per-cell notes at sites 2 and 5. The per-cell enforcement
procedure for DRI/Owner and Key Roles is in downstream PRODUCE-command CHECK directives, separated
from the lock by hundreds of tokens of intervening inertia content and org diagram. V-03 adds
per-cell enforcement notes immediately adjacent to the role-name list within the ROLE-NAME LOCK
block, placing the per-cell procedure at declaration time. Tests whether C-36 inline notes are
compatible with the phase-gate REGISTER-CONSISTENCY AUDIT architecture: the audit at gate 4
checks whether DRI/Owner and Key Roles instruction sites used mandatory-register language; the
inline notes at declaration time provide an earlier enforcement reference that the audit can cite.
Built on R13 V-03 base: STOP variant, per-cell per-row directives with procedural form, phase-gate
audits, no FORMAT CONTRACT. C-35 not achievable without FC -- V-03 isolates C-36 on the STOP/audit base.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
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

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value; per-cell note above applies
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
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
  [ ] ROLE-NAME LOCK per-cell notes: used mandatory procedural language at both sites -- no advisory qualifier present.
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
CHECK [SITE 3]: every role in Membership and Decides must appear in the ROLE-NAME LOCK list.
Quorum: `[N] of [M] member roles required`.
VERIFY: "[N] members required" without denominator M does not satisfy this step.

PHASE GATE 4 -- CHARTERS COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] Key Roles per-cell directive: used mandatory "must appear in ROLE-NAME LOCK" language -- no "where possible" present.
  [ ] DRI/Owner per-cell directive: used mandatory "must appear in ROLE-NAME LOCK" language -- no conditional qualifier present.
  [ ] Charter Membership directive: used mandatory "must appear in ROLE-NAME LOCK" language -- no hedging.
  [ ] Quorum directive: used mandatory "[N] of [M] member roles required" language -- no short-form present.
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
before writing the next row -- do not complete the table and verify after.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

PHASE GATE 5 -- ORG-EVOLUTION COMPLETE

REGISTER-CONSISTENCY AUDIT (before proceeding):
STOP. Confirm the following before emitting the phase gate line:
  [ ] TRIGGER-TYPE VOCABULARY instruction: used mandatory "no row may" language -- no "where possible" present.
  [ ] Per-row vocabulary check: used mandatory "verify before writing the next row" language -- no advisory "consider checking" present.
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
    (complete role enumeration + [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] + five-site enumeration)
4.  [REGISTER-CONSISTENCY AUDIT: ROLES section + per-cell note register check] Phase Gate 1
5.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [STOP -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense] / VERDICT
6.  [REGISTER-CONSISTENCY AUDIT: INERTIA section] Phase Gate 2
7.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify]
8.  [REGISTER-CONSISTENCY AUDIT: STRUCTURE section] Phase Gate 3
9.  Headcount [CHECK SITE 5 -- per-cell; lock-declared directive applies]
10. Operating Rhythm [CHECK SITE 2 -- per-cell; lock-declared directive applies]
11. Committee Charters [CHECK SITE 3] [VERIFY: short Quorum]
12. [REGISTER-CONSISTENCY AUDIT: HEADCOUNT/RHYTHM/CHARTERS section] Phase Gate 4
13. ORG-ELEMENT REGISTER (all four categories)
14. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
15. [REGISTER-CONSISTENCY AUDIT: ROADMAP section] Phase Gate 5
16. [CAT-N-CITATION-SCHEMA] + [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- C-35 + C-36 Combined on R13 V-04 Base

**Axis**: C-35 HALT header schema recall + C-36 ROLE-NAME LOCK adjacent per-cell notes, combined on R13 V-04
**Hypothesis**: R13 V-04 achieves C-33 (no co-located advisory DRI/Owner prose) and C-34 (procedural
per-cell directives at PRODUCE sites for DRI/Owner and Key Roles) on R12 V-04 base. Two gaps remain:
(a) HALT headers at FC-governed PRODUCE commands read "HALT." without schema citation (C-35 gap);
(b) ROLE-NAME LOCK sites enumeration carries `[per-cell directive: verify each cell against this list
before populating the next row]` but these are short form, not the full procedural form, and they
are in the sites list rather than adjacent to the role-name enumeration (C-36 gap). V-04 closes both:
HALT headers embed schema citations ("HALT. Re-read FORMAT CONTRACT schema (N) -- [name]."); ROLE-NAME
LOCK embeds full per-cell notes immediately after the role-name list for sites 2 and 5 with complete
procedural form and temporal constraint. Built on R13 V-04 base (FORMAT CONTRACT, C-33 sole-instruction-
site consolidation, C-34 procedural per-cell directives). Tests whether C-35 + C-36 stack cleanly
on C-33 + C-34 without register contamination.

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
    "Why It Applies Here": [element name] (cat-N) -- [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: "Why It Applies Here" cell names an org element without (cat-N) prefix.

---

STEP 1 -- LOAD ROLES

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
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

[DRI/Owner -- per-cell: for each cell in the Operating Rhythm Table DRI/Owner column, verify the
value appears in this list before populating the next row -- do not complete the DRI/Owner column
and verify after. A novel role name at any DRI/Owner cell is a violation regardless of row position.]

[Key Roles -- per-cell: for each cell in the Headcount table Key Roles column, verify each name
appears in this list before populating the next row -- do not complete the Key Roles column and
verify after. A novel role name at any Key Roles cell is a violation regardless of row position.]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- per-cell directive above governs every row
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive applies: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- per-cell directive above governs every row [MANDATORY FIFTH SITE]

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

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  1. Schema (1) columns confirmed: Area | Headcount | Key Roles | Decides | Escalates (five separate columns).
  2. DISQUALIFY-IF confirmed: Decides and Escalates will not be merged into a single column.
  3. Key Roles confirmed: every value must be a role from ROLE-NAME LOCK.
  4. Total row confirmed: will be present.
  5. Each area from the input will have its own row.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table merging Decides and Escalates into a single column does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list before populating
the next row -- do not complete the Key Roles column and verify after. A novel role name at any
Key Roles cell is a violation regardless of whether prior rows complied.
Key Roles format: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table.
  1. Schema (2) columns confirmed: Cadence | Frequency | DRI / Owner | Purpose.
  2. Minimum three rows confirmed: ROB, shiproom/gate, governance meeting. No merged rows.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
  4. No merged rows confirmed.
Proceed only if all four confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The DRI/Owner role-lock requirement is stated in HALT checklist item 3 above and in the ROLE-NAME
LOCK per-cell note. No alternative or supplementary DRI/Owner role-lock instruction appears at
this location. No conditional qualifier such as "where a role is known" is present at any
instruction site for this requirement.]

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here. For each cell in the DRI / Owner
column: verify the value appears in the ROLE-NAME LOCK list before populating the next row -- do
not complete the DRI / Owner column and verify after. A novel role name at any DRI/Owner cell is
a violation regardless of row position.

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

CHECK [SITE 3 -- CHARTER]: every role in Membership and Decides must appear in ROLE-NAME LOCK.

Per-role-name directive for Membership:
For each role name in Membership: verify it appears in ROLE-NAME LOCK before appending the next
name -- do not write the full list and verify after. A novel role name at any position is a violation.

Per-role-name directive for Decides:
For each role name in Decides: verify it appears in ROLE-NAME LOCK before appending the next name.

VERIFY: A Quorum written as "[N] members required" without denominator M does not satisfy this
step. FORMAT CONTRACT schema (3) DISQUALIFY-IF applies. Fraction form [N] of [M] required.

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

Produce per schema (4) immediately after the charters gate. All four categories required.

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
the next row -- do not complete the table and verify after.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5; schema 2 states DRI/Owner req)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION
4.  [HALT -- 4-item checklist] ROLE-NAME LOCK
    (role enumeration + [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] + five-site enumeration with per-role-name at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia:
    [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table. -- 5-item]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5 -- per-cell; lock-declared directive applies]
11. [HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table. -- 4-item; sole DRI/Owner site]
    Operating Rhythm Table [no co-located advisory prose]
    [CHECK SITE 2 -- per-cell DRI/Owner; lock-declared directive applies]
12. [HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter. -- 6-item per charter]
    Committee Charters [CHECK SITE 3] [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER. -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row Type verify] + Roadmap [VERIFY: duplicate type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch. -- 5-item] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-35 + C-36 on R13 V-05 Base

**Axis**: All axes combined -- maximum mechanical stack with C-35 HALT header schema recall and
C-36 ROLE-NAME LOCK adjacent per-cell notes added to R13 V-05 base
**Hypothesis**: R13 V-05 achieves C-20 through C-34 inclusive. Two gaps remain before dual
convergence: (a) C-35: HALT headers at FC-governed PRODUCE commands read "HALT." prefixed by
"BEFORE PRODUCING -- re-read FORMAT CONTRACT schema (N):" on a separate line; the schema citation
is not in the HALT line itself; (b) C-36: ROLE-NAME LOCK block carries per-cell notes at sites 2
and 5 within the CHECK SITES enumeration using a shortened form ("verify each cell against this
list before populating the next row") but not adjacent to the role-name list, and without the full
procedural form specifying "for each cell in this column" and "do not complete the table and verify
after." V-05 closes both: HALT headers embed schema citations in the gate-trigger line at all five
FC-governed PRODUCE steps; ROLE-NAME LOCK block embeds full per-cell notes immediately after the
role-name enumeration using exact required form for both DRI/Owner (site 2) and Key Roles (site 5).
Together with the full R13 V-05 mechanical stack (C-20 through C-34), V-05 targets all 36 criteria.

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

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
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

[DRI/Owner -- per-cell: for each cell in the Operating Rhythm Table DRI/Owner column, verify the
value appears in this list before populating the next row -- do not complete the DRI/Owner column
and verify after. A novel role name at any DRI/Owner cell is a violation regardless of row position.]

[Key Roles -- per-cell: for each cell in the Headcount table Key Roles column, verify each name
appears in this list before populating the next row -- do not complete the Key Roles column and
verify after. A novel role name at any Key Roles cell is a violation regardless of row position.]

This lock governs five mandatory CHECK sites:
  (1) ASCII diagram -- every node label placed in the diagram
  (2) Operating Rhythm Table DRI/Owner column -- every DRI/Owner cell value;
      per-cell directive above governs site 2 from declaration time forward
  (3) Committee Charter Membership and Decides fields -- every role name in both fields
      [per-role-name directive: verify each name before appending the next]
  (4) Inertia Assessment sub-sections -- every role name including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE];
      per-cell directive above governs site 5 from declaration time forward

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

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  1. Schema (1) column headers confirmed: Area | Headcount | Key Roles | Decides | Escalates.
  2. DISQUALIFY-IF confirmed: Decides and Escalates will not be merged into a single column.
  3. Key Roles confirmed: every value in this column must be a role from the ROLE-NAME LOCK list.
  4. Total row confirmed: will be present.
  5. Each area from the input will have its own row.
Proceed only if all five confirmed.

Produce per schema (1) of the FORMAT CONTRACT.
VERIFY: A table merging Decides and Escalates into "Decision Scope" does not satisfy this step.

CHECK [SITE 5 -- KEY ROLES -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here. For each cell in the Key Roles
column: verify the role name appears in the ROLE-NAME LOCK list before populating the next row --
do not complete the Key Roles column and verify after. A novel role name at any Key Roles cell is
a violation regardless of whether prior rows complied.
Key Roles format: `[role name] ([domain type])`.

STEP 7 -- OPERATING RHYTHM TABLE

HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table.
  1. Schema (2) column headers confirmed: Cadence | Frequency | DRI / Owner | Purpose.
  2. Minimum three rows confirmed: ROB, shiproom or gate, governance meeting.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
  4. No merged rows confirmed.
Proceed only if all four confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The DRI/Owner role-lock requirement is stated once in HALT checklist item 3 above and in the
ROLE-NAME LOCK per-cell note declared at STEP 3. No alternative or supplementary DRI/Owner
role-lock instruction appears at this location. No conditional qualifier such as "where a role
is known" is present at any instruction site for this requirement.]

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here. For each cell in the DRI / Owner
column: verify the value appears in the ROLE-NAME LOCK list before populating the next row -- do
not complete the DRI / Owner column and verify after. A novel role name at any DRI/Owner cell is
a violation regardless of row position.

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

HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER.
  1. cat-1 (Areas) confirmed: will list area names with headcounts.
  2. cat-2 (Committees/Cadences) confirmed: will list each committee and cadence.
  3. cat-3 (Headcount) confirmed: will state total headcount.
  4. cat-4 (DRI Roles) confirmed: will list DRI roles from the Operating Rhythm Table.
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
writing the next row -- do not complete the table and verify after. A cell without the typed
(cat-N) prefix at any row is a violation regardless of whether prior rows complied.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5; DRI/Owner req in schema 2)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier)
4.  [HALT -- 4-item checklist with count-record] ROLE-NAME LOCK
    (role enumeration +
     [DRI/Owner -- per-cell: for each cell...verify...before next row -- do not complete and verify after] +
     [Key Roles -- per-cell: for each cell...verify...before next row -- do not complete and verify after] +
     five-site enumeration with per-cell references at sites 2 and 5 and per-role-name at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia:
    [MECHANISM-TYPE VOCAB] /
    [per-row: verify Type before next row -- do not complete and verify after] /
    table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT -- 4-item Rebuttal field checklist] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE] /
    [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  [HALT -- 4-item diagram checklist] ASCII Org Diagram [per-node verify before next node]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table. -- 5-item]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5 -- per-cell; lock-declared directive applies]
11. [HALT. Re-read FORMAT CONTRACT schema (2) -- operating rhythm table. -- 4-item; sole DRI/Owner site]
    Operating Rhythm Table [no co-located advisory prose]
    [CHECK SITE 2 -- per-cell DRI/Owner; lock-declared directive applies]
12. [HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter. -- 6-item per charter]
    Committee Charters [CHECK SITE 3] [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER. -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] +
    [per-row: verify Type and non-repeat before next row -- do not complete and verify after] +
    Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5) -- Anti-Pattern Watch. -- 5-item] +
    [per-row: citation verify before next row -- do not complete and verify after] +
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`
