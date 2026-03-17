---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 10
rubric: simulations/quest/rubrics/corps-chart-rubric-v9-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 10)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R10 targets rubric additions in v9 that were absent or incomplete in R9:
- C-26 (PRODUCE-time FORMAT CONTRACT back-reference directive -- the temporal bridge between
  pre-generation DISQUALIFY-IF and post-produce VERIFY)
- C-27 (Headcount table Key Roles column as explicit fifth ROLE-NAME LOCK CHECK site -- closes
  the gap where Key Roles was ungoverned while the other four role-consuming sites had CHECKs)
- C-28 (Per-cell row-by-row role-lock CHECK for DRI/Owner and Key Roles -- converts column-level
  enforcement into row-granularity mechanical verification before the next row is populated)

R9 V-05 provides the baseline for full-integration (V-05). Single-axis variations build from
narrower R9 baselines to isolate each new mechanism.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | BEFORE-PRODUCE back-reference directive (single axis) | C-26 | The FORMAT CONTRACT is read once at document head; by the time each governed PRODUCE command fires, 1,000+ tokens of generation have elapsed and FORMAT CONTRACT schema constraints may have faded from working context. Adding a labeled "BEFORE PRODUCING: re-read FORMAT CONTRACT schema (N)" directive immediately before each PRODUCE command converts schema compliance from a recall requirement into a per-step active reference requirement. The three-point temporal chain becomes: FORMAT CONTRACT DISQUALIFY-IF (pre-generation) -> BEFORE-PRODUCE re-read (production-time) -> post-produce VERIFY (post-generation). This single-axis test adds the bridge mechanism at each governed PRODUCE command on an R9 V-01 baseline (FORMAT CONTRACT with DISQUALIFY-IF, no ROLE-NAME LOCK, no vocab blocks), isolating C-26's contribution alone. |
| V-02 | Key Roles as explicit fifth CHECK site (single axis) | C-27 | C-21 enumerated four mandatory ROLE-NAME LOCK CHECK sites: diagram, DRI/Owner, charter Membership/Decides, Inertia sub-sections. The Key Roles column of the headcount table carries the same role-coherence risk as those four sites -- a novel role name introduced in a Key Roles cell propagates downstream -- but C-21 did not list it, leaving it as an ungoverned insertion point. C-27 closes this by requiring a fifth mandatory site. This variation tests whether explicitly naming Key Roles as the fifth site in the ROLE-NAME LOCK block's site enumeration -- and emitting a dedicated labeled CHECK instruction for it at the headcount table command -- prevents the ungoverned-column failure mode. Built on an R9 V-02 baseline (four-field Rebuttal, ROLE-NAME LOCK with inline CHECKs at four sites), isolating C-27 alone. |
| V-03 | Per-cell row-by-row role-lock CHECK (single axis) | C-28 | R9 V-03 introduced strict mandatory DRI/Owner ROLE-LOCK language ("every DRI/Owner value must appear in the ROLE-NAME LOCK list -- no new role names are introduced in this column"). R9 V-02 had "CHECK: before writing each DRI/Owner cell, verify the role name is in the ROLE-NAME LOCK list." Both are column-level instructions: they apply once at instruction time, then the model populates multiple rows without re-activating the constraint. C-28 targets the memory-decay failure mode within a multi-row table: early rows comply, later rows drift. The fix is a row-granularity directive that explicitly says "for each cell in this column, verify the value against the ROLE-NAME LOCK list before populating the next row -- do not complete the table and verify after." This variation deploys per-cell directives for both DRI/Owner and Key Roles on an R9 V-03 baseline, isolating C-28 alone. |
| V-04 | C-26 BEFORE-PRODUCE + C-27 fifth CHECK site (combination) | C-26, C-27 | Two mechanisms that govern adjacent failure modes in the same production pipeline. C-26 fires at each PRODUCE command to re-anchor the model to the FORMAT CONTRACT schema; C-27 makes Key Roles a named, enumerated CHECK site so it cannot be skipped. Together they cover two distinct gaps: format-evasion recovery (C-26) and role-coherence coverage completeness (C-27). Building on an R9 V-04 baseline (FORMAT CONTRACT DISQUALIFY-IF + four-field Rebuttal + vocab blocks, without strict DRI/Owner) to test whether these two new mechanisms close remaining gaps with DRI/Owner as the open variable. |
| V-05 | Full integration: C-26 + C-27 + C-28 on R9 V-05 baseline | C-26, C-27, C-28, all prior | Maximum mechanical stack. R9 V-05 covered C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad with embedded CHECK at ROLE UNDER PRESSURE), and C-25 (strict mandatory DRI/Owner ROLE-LOCK). R10 V-05 adds: (a) BEFORE-PRODUCE back-reference directives at every FORMAT CONTRACT-governed PRODUCE command, naming the specific schema by number and label; (b) Key Roles listed as the explicit fifth mandatory ROLE-NAME LOCK CHECK site in the ROLE-NAME LOCK block's site enumeration; (c) per-cell row-by-row directive for DRI/Owner AND Key Roles columns, explicitly stating "verify before populating the next row -- do not complete the table and verify after." Tests whether full constraint density across all 28 criteria produces maximum rubric score or induces section-complexity failures. |

---

## V-01 -- BEFORE-PRODUCE Back-Reference Directive (single axis)

**Axis**: PRODUCE-time FORMAT CONTRACT back-reference directive at every governed PRODUCE command (C-26)
**Hypothesis**: The FORMAT CONTRACT is read once at document head. By the time each governed PRODUCE
command fires, 1,000+ tokens of generation have elapsed and schema constraints may have faded. Placing
a labeled "BEFORE PRODUCING: re-read FORMAT CONTRACT schema (N)" directive immediately before each
PRODUCE command converts schema compliance from recall into per-step active reference. Three-point
temporal chain: FORMAT CONTRACT DISQUALIFY-IF -> BEFORE-PRODUCE re-read -> post-produce VERIFY.
Built on R9 V-01 baseline (FORMAT CONTRACT with DISQUALIFY-IF, no ROLE-NAME LOCK, no vocab blocks).

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT -- READ BEFORE WRITING ANYTHING
=======================================================
The following five schemas apply throughout this document.
Reference this block at each BEFORE PRODUCING directive. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Required columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles cell format: [role name] ([domain type])
    Required rows: minimum two area rows + one **Total** row with the sum.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") -- the five-column schema
                   requires separate Decides and Escalates columns.

(2) OPERATING RHYTHM TABLE
    Required columns: Cadence | Frequency | DRI / Owner | Purpose
    Required rows: minimum three -- one ROB, one shiproom or gate meeting, one governance meeting.
    Two meetings must not be merged into one row.

(3) COMMITTEE CHARTER -- one block per governance meeting in the rhythm table
    Purpose:    [text]
    Membership: [role name] ([domain type]), [role name] ([domain type]), ... (minimum two roles)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward -- must name a destination, not "everything else"]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M
                   (e.g., "3 members required for binding decisions" without "of M member roles") --
                   the fraction form [N] of [M] member roles required is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               -- [area name] -- headcount: [N]
    cat-2 (Committees/Cadences) -- [name]
    cat-3 (Headcount)           -- Total headcount: [N]
    cat-4 (DRI Roles)           -- [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Required columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" cell format: [element name] (cat-N) -- [one sentence of specific relevance]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N) typed
                   citation prefix -- every cell must open with [element name] (cat-N) -- before
                   the relevance sentence.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from the closed vocabulary: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Carry this annotation forward: use `[role name] ([domain type])` in Key Roles cells (schema 1) and Charter Membership fields (schema 3).

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO structure it in this exact order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. After writing, count data rows (header excluded). If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator.

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns in active use: channels, cadences, informal roles, artifacts with frequency and participants.
DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

Name the coordination failure the flat-team case cannot answer. Reference a specific observable: a blocked
decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the current failure mode.
Name at least one specific role as the coordination failure point.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Write a re-assessment trigger naming a concrete threshold. DO NOT write "revisit as the team grows."

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw an ASCII hierarchy with minimum two levels. Committees appear as distinct labeled nodes -- not embedded inside an area box.
Role names must match ROLES-LOADED or ROLES-NOTE. DO NOT introduce new role names.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (1) -- HEADCOUNT BY AREA -- and confirm that the
output will use five separate columns (Area, Headcount, Key Roles, Decides, Escalates) and that
the DISQUALIFY-IF condition (merged Decides/Escalates) will not be met in this output.

Produce per schema (1) in the FORMAT CONTRACT above.
Five-column schema required: Area | Headcount | Key Roles | Decides | Escalates.
Key Roles cells annotated: `[role name] ([domain type])`.
Minimum two area rows plus `**Total**` row with the sum.

OPERATING RHYTHM TABLE

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (2) -- OPERATING RHYTHM TABLE -- and confirm
that the output will use four columns (Cadence, Frequency, DRI / Owner, Purpose) and that the
minimum three rows (ROB, shiproom/gate, governance) will be present with no merged rows.

Produce per schema (2) above.
Reference a role from ROLES-LOADED in DRI / Owner where a role is known.

COMMITTEE CHARTERS

For every governance meeting in the rhythm table, write a charter.

BEFORE PRODUCING each charter: re-read FORMAT CONTRACT schema (3) -- COMMITTEE CHARTER -- and
confirm that all five fields are present (Purpose, Membership, Decides, Escalates, Quorum) and
that the DISQUALIFY-IF condition (Quorum without denominator M) will not be met in this output.

Produce per schema (3) above.
Escalates must name a destination -- not "everything not listed under Decides."

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER -- and confirm that
all four categories (cat-1 through cat-4) will be populated in this output before proceeding.

Produce per schema (4) above immediately after the charters gate. All four categories required.
DO NOT proceed to Org Evolution Roadmap until all four categories are populated.

ORG EVOLUTION ROADMAP

Produce a trigger table: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: a different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (5) -- ANTI-PATTERN WATCH -- and confirm that
every "Why It Applies Here" cell will open with the [element name] (cat-N) -- typed citation prefix
and that the DISQUALIFY-IF condition (cell without cat-N prefix) will not be met in this output.

Produce per schema (5) above. Minimum two rows.
The schema includes a DISQUALIFY-IF annotation -- re-read it before producing each "Why It Applies Here" cell.
Every cell must open with: `[element name] (cat-N) -- [one sentence]`.

SECTION ORDER

1.  UPFRONT FORMAT CONTRACT (present above, with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  [BEFORE PRODUCING schema (1)] Headcount by Area
10. [BEFORE PRODUCING schema (2)] Operating Rhythm Table
11. [BEFORE PRODUCING schema (3) per charter] Committee Charters
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. [BEFORE PRODUCING schema (4)] ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. [BEFORE PRODUCING schema (5)] Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Key Roles as Explicit Fifth CHECK Site (single axis)

**Axis**: Headcount table Key Roles column designated as mandatory fifth ROLE-NAME LOCK CHECK site,
with explicit site enumeration in the ROLE-NAME LOCK block (C-27)
**Hypothesis**: C-21 required inline CHECKs at four sites: diagram, DRI/Owner, charter
Membership/Decides, Inertia sub-sections. The Key Roles column carries identical role-coherence risk
but was not enumerated as a mandatory site -- leaving it as an ungoverned insertion point. C-27 fixes
this by making Key Roles the fifth required site, explicitly listed in the ROLE-NAME LOCK block's
site enumeration and carrying its own dedicated labeled CHECK at the headcount table instruction.
Built on R9 V-02 baseline (four-field Rebuttal, ROLE-NAME LOCK with inline CHECKs at four sites).

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Carry annotation forward: `[role name] ([domain type])` in Key Roles cells and Charter Membership fields.

ROLE-NAME LOCK -- REQUIRED IMMEDIATELY AFTER CLASSIFICATION

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

A role name that appears at any of these five sites but is not listed above is a violation.
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
                               or structural symptom such as two or more missed ship dates]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step. The breakdown must describe
a failure that exists now, not a risk that may emerge with growth.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different from what was written there.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK list.
Verify each name before drawing it.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes -- not embedded inside an area box.
DO NOT introduce names not in the ROLE-NAME LOCK.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles annotated: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column.
This is equivalent to the diagram CHECK and the charter Membership CHECK -- treat it as a first-class
enforcement site, not an optional best-effort column.

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
3.  ROLE-NAME LOCK (complete permitted-role enumeration + five-site CHECK enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment:
    mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [REBUTTAL FORM: CHECK SITE 4 embedded at ROLE UNDER PRESSURE] / [VERIFY: future-tense fails] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK SITE 1]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK SITE 5 -- KEY ROLES, explicit fifth mandatory site]
10. Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER]
11. Committee Charters [CHECK SITE 3]
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Per-Cell Row-by-Row Role-Lock CHECK (single axis)

**Axis**: Per-cell role-lock CHECK directive at role-consuming columns, converting column-level
enforcement to row-granularity mechanical verification before the next row is populated (C-28)
**Hypothesis**: Column-level CHECK instructions ("every DRI/Owner value must appear in the
ROLE-NAME LOCK list") apply once at instruction time; the model then populates multiple rows
across potentially hundreds of tokens without re-activating the constraint. Memory-decay within
a table produces the compliance-drift pattern: early rows comply, later rows introduce novel names
because the column-level instruction has faded. C-28 adds a structural directive that makes
row-level verification the mechanic: "for each cell in this column, verify the value appears in
the ROLE-NAME LOCK list before populating the next row -- do not complete the table and verify after."
Built on R9 V-03 baseline (strict mandatory DRI/Owner ROLE-LOCK), adding per-cell directives for
DRI/Owner and Key Roles, isolating C-28 alone.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.

ROLE-NAME LOCK -- REQUIRED IMMEDIATELY AFTER CLASSIFICATION

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

Produce: `Mechanism Name | Type | Frequency / Participants`.
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

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify each before drawing.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes -- not embedded in an area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

Key Roles column -- per-cell role-lock directive:
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list.
No new role names may be introduced in this column.
For each cell in the Key Roles column: verify the role name appears in the ROLE-NAME LOCK list
before populating the next row. Do not complete the table and verify after -- verify row by row
as you populate. A novel role name entered in any Key Roles cell, regardless of table position,
is a violation even if all prior cells complied.

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
as you populate. A novel role name entered in any DRI/Owner cell, regardless of row position,
is a violation even if all prior rows complied.

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
3.  ROLE-NAME LOCK (complete permitted-role enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    Rebuttal [CHECK] / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK against ROLE-NAME LOCK]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [per-cell KEY ROLES -- verify before each next row]
10. Operating Rhythm Table [strict DRI/Owner -- mandatory + per-cell verify before each next row]
11. Committee Charters [CHECK Membership+Decides]
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- C-26 BEFORE-PRODUCE + C-27 Fifth CHECK Site (combination)

**Axis**: PRODUCE-time FORMAT CONTRACT back-reference directive (C-26) combined with Key Roles
as explicit fifth ROLE-NAME LOCK CHECK site (C-27)
**Hypothesis**: C-26 and C-27 govern adjacent failure modes in the same pipeline: C-26 ensures the
FORMAT CONTRACT schema is re-read immediately before each governed PRODUCE command (preventing
format-evasion through context decay); C-27 ensures the Key Roles column is treated as a
first-class role-coherence site (preventing ungoverned role introduction in the one headcount
column not covered by C-21's original four-site enumeration). Together they extend coverage
in two orthogonal dimensions: temporal (C-26 fires at every PRODUCE moment) and spatial
(C-27 adds a governed column that was previously unguarded). Built on an R9 V-04 baseline
(FORMAT CONTRACT DISQUALIFY-IF + four-field Rebuttal activation triad + vocabulary blocks),
with DRI/Owner as the open variable (no per-cell directive yet).

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
                   (e.g., "Decision Scope") -- five separate columns are required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.

(3) COMMITTEE CHARTER -- one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles)
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
                   typed citation prefix -- every cell must carry the typed prefix.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational, then advisory and governance.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear.
Carry annotation to Key Roles and Charter Membership per schemas (1) and (3) above.

ROLE-NAME LOCK -- REQUIRED IMMEDIATELY AFTER CLASSIFICATION

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

All five sites must honor this lock. A role name at any of these sites that is not listed
above is a violation regardless of table position or section order.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write before any org boxes. Order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

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

Produce: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows.
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

VERIFY: A mechanism row whose Type value is not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns in active use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

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
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning must reference FLAT-CASE-PRESSURE.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK list.
Verify each before drawing.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes -- not embedded in any area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (1) -- HEADCOUNT BY AREA -- and confirm that five
separate columns (Area, Headcount, Key Roles, Decides, Escalates) will be used and that the DISQUALIFY-IF
condition (merged Decides/Escalates) will not be met in this output.

Produce per schema (1) above.
CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column. Treat it as a first-class enforcement site.
Minimum two area rows plus `**Total**`. Key Roles: `[role name] ([domain type])`.

VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy this step.

OPERATING RHYTHM TABLE

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (2) -- OPERATING RHYTHM TABLE -- and confirm
that four columns (Cadence, Frequency, DRI / Owner, Purpose) will be used with minimum three rows
(ROB, shiproom/gate, governance) and no merged rows.

Produce per schema (2) above.
CHECK [SITE 2 -- DRI/OWNER]: every DRI / Owner value must appear in the ROLE-NAME LOCK list.
Minimum three rows: ROB, shiproom or gate, governance. No merged rows.
Reference a role from ROLES-LOADED in DRI / Owner where a role is known.

COMMITTEE CHARTERS

For every governance meeting in the rhythm table, write a charter.

BEFORE PRODUCING each charter: re-read FORMAT CONTRACT schema (3) -- COMMITTEE CHARTER -- and confirm
all five fields (Purpose, Membership, Decides, Escalates, Quorum) are present and the DISQUALIFY-IF
condition (Quorum without denominator M) will not be met in this output.

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: must name a destination.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M
does not satisfy this step.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER -- and confirm that
all four categories (cat-1 through cat-4) will be populated before proceeding.

Produce per schema (4) above immediately after the charters gate. All four categories required.
DO NOT proceed to Org Evolution Roadmap until all four categories are populated.

ORG EVOLUTION ROADMAP

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

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

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

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (5) -- ANTI-PATTERN WATCH -- and confirm that every
"Why It Applies Here" cell will carry the [element name] (cat-N) -- typed prefix and that the DISQUALIFY-IF
condition will not be met in this output.

Produce per schema (5) above. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 17 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  ROLE-NAME LOCK (complete permitted-role enumeration + five-site CHECK enumeration)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [BEFORE PRODUCING schema (1)] Headcount by Area [CHECK SITE 5 -- KEY ROLES] [VERIFY: merged column]
11. [BEFORE PRODUCING schema (2)] Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER]
12. [BEFORE PRODUCING schema (3) per charter] Committee Charters [CHECK SITE 3] [VERIFY: short Quorum]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [BEFORE PRODUCING schema (4)] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [BEFORE PRODUCING schema (5)] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-26 + C-27 + C-28 on R9 V-05 Baseline

**Axis**: BEFORE-PRODUCE back-reference (C-26) + Key Roles fifth CHECK site (C-27) + per-cell
row-by-row role-lock for DRI/Owner and Key Roles (C-28), layered on R9 V-05 full-integration baseline
**Hypothesis**: R9 V-05 covered C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad with
embedded CHECK at ROLE UNDER PRESSURE), and C-25 (strict mandatory DRI/Owner ROLE-LOCK). These three
new mechanisms close three remaining failure modes. C-26 closes the temporal gap: FORMAT CONTRACT
constraints are re-read at every PRODUCE command, not just at document head (prevents memory-decay
across 1,000+ tokens between schema declaration and production). C-27 closes the spatial gap: Key
Roles is enumerated as the fifth mandatory CHECK site in the ROLE-NAME LOCK block, making it
structurally parallel to the diagram and charter enforcement sites (prevents ungoverned insertion
into the one role-consuming column that was previously unlisted). C-28 closes the within-table
row-drift gap: per-cell directives fire before each row is populated rather than applying once
at column-instruction time (prevents late-row non-compliance after early rows establish
a compliant pattern). All three mechanisms are non-overlapping: C-26 governs table format
evasion, C-27 governs role-site coverage, C-28 governs row-granularity role drift.

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
    "Why It Applies Here": [element name] (cat-N) -- [one sentence]
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
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] -- [domain type]`. Every loaded role must appear. No absent role may appear.
Carry annotation to Key Roles (schema 1) and Charter Membership (schema 3).

STEP 3 -- EMIT ROLE-NAME LOCK

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
  (4) Inertia Assessment sub-sections -- every role name, including ROLE UNDER PRESSURE
  (5) Headcount table Key Roles column -- every Key Roles cell value [MANDATORY FIFTH SITE]
      [per-cell directive applies: verify before each next row, not after table is complete]

All five sites must honor this lock. Sites 2 and 5 carry per-cell row-by-row directives in
their respective section instructions -- these are the activation layer for this lock at
those sites.
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
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

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

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (1) -- HEADCOUNT BY AREA -- and confirm that five
separate columns (Area, Headcount, Key Roles, Decides, Escalates) will be used and that the DISQUALIFY-IF
condition (merged Decides/Escalates column) will not be met in this output.

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

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (2) -- OPERATING RHYTHM TABLE -- and confirm that
four columns (Cadence, Frequency, DRI / Owner, Purpose) will be used, the DRI/Owner column will carry
only ROLE-NAME LOCK values, and minimum three rows (ROB, shiproom/gate, governance) will be present
with no merged rows.

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

BEFORE PRODUCING each charter: re-read FORMAT CONTRACT schema (3) -- COMMITTEE CHARTER -- and confirm
all five fields (Purpose, Membership, Decides, Escalates, Quorum) are present and the DISQUALIFY-IF
condition (Quorum without denominator M) will not be met.

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.
Verify before writing.

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

BEFORE PRODUCING: re-read FORMAT CONTRACT schema (5) -- ANTI-PATTERN WATCH -- and confirm that every
"Why It Applies Here" cell will open with [element name] (cat-N) -- and that the DISQUALIFY-IF
condition (cell without typed prefix) will not be met in this output.

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row. Re-read FORMAT CONTRACT DISQUALIFY-IF
and the CAT-N-CITATION-SCHEMA before producing each cell.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5; DRI/Owner per-cell note in schema 2)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  ROLE-NAME LOCK (complete permitted-role enumeration + five-site CHECK enumeration
    + per-cell note at sites 2 and 5)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [REBUTTAL FORM: CHECK SITE 4 embedded at ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN /
    WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK SITE 1]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. [BEFORE PRODUCING schema (1)] Headcount by Area
    [VERIFY: merged column]
    [CHECK SITE 5 -- KEY ROLES, explicit fifth mandatory site]
    [per-cell: verify before each next row, not after table is complete]
11. [BEFORE PRODUCING schema (2)] Operating Rhythm Table
    [strict mandatory DRI/Owner ROLE-LOCK -- no hedging, first-class site]
    [CHECK SITE 2]
    [per-cell: verify before each next row, not after table is complete]
12. [BEFORE PRODUCING schema (3) per charter] Committee Charters
    [CHECK SITE 3]
    [VERIFY: short Quorum -- fraction form required]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [BEFORE PRODUCING schema (4)] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [BEFORE PRODUCING schema (5)]
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`
