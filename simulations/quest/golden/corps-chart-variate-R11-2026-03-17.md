---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 11
rubric: simulations/quest/rubrics/corps-chart-rubric-v10-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 11)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R11 targets rubric additions in v10 that were absent or incomplete in R10:
- C-29 (BEFORE-PRODUCE back-reference extended to non-FORMAT-CONTRACT structural forms --
  the four-field Rebuttal form (C-14) and the ROLE-NAME LOCK block (C-13) carry the same
  temporal recall gap as FORMAT CONTRACT schemas but C-26 only covers FC-governed PRODUCE
  commands; C-29 extends the temporal bridge to structural forms defined outside the FC)
- C-30 (Per-role-name role-lock CHECK within committee charter Membership and Decides
  multi-role lists -- C-21 section-level CHECKs fire once before the list is written, leaving
  intra-list positions 3+ as ungoverned insertion points; C-30 closes this by requiring
  per-role-name verification before each next name is appended)

R10 V-05 provides the baseline for full-integration (V-05). Single-axis variations build from
narrower R10 baselines to isolate each new mechanism.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | BEFORE-PRODUCE back-reference for non-FORMAT-CONTRACT structural forms (single axis) | C-29 | The four-field Rebuttal form (C-14) is declared at the Rebuttal sub-section instruction; the model produces the Rebuttal 2,000+ tokens after reading that definition. The ROLE-NAME LOCK block (C-13) is declared at the classification step; the model emits it from a ROLES-LOADED list that may have faded from active context. C-26 closes the temporal gap for FORMAT CONTRACT schemas, but both of these structural forms are governed outside the FC and receive no BEFORE-PRODUCE back-reference under C-26. C-29 adds a labeled BEFORE-PRODUCE directive immediately before each: "BEFORE PRODUCING THE ROLE-NAME LOCK: re-read ROLES-LOADED -- enumerate only roles present in that list" and "BEFORE PRODUCING THE REBUTTAL: re-read the four-field form -- ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER -- all four fields in this order." Built on R10 V-02 baseline (ROLE-NAME LOCK with five-site enumeration, four-field Rebuttal, inline CHECKs at all five sites, no FORMAT CONTRACT BEFORE-PRODUCE), isolating C-29 alone. |
| V-02 | Per-role-name role-lock CHECK within charter Membership and Decides (single axis) | C-30 | C-21 requires an inline CHECK before each charter section: "every role name in Membership and Decides must appear in the ROLE-NAME LOCK list." This is a section-level instruction that fires once before the entire Membership list is written. A four-role Membership list ("Engineering Lead, Product Lead, Architect, Program Manager") can introduce a novel name at position 3 while satisfying the section-level CHECK, because the CHECK applies to the section collectively and has faded by position 3. C-30 adds a per-role-name directive embedded in the Membership and Decides field instructions: "for each role name in this field, verify it appears in the ROLE-NAME LOCK list before appending the next name -- do not write the full list and verify after." The per-role-name directive is the intra-field analogue of the per-cell directive (C-28) for DRI/Owner and Key Roles table columns. Built on R10 V-02 baseline (ROLE-NAME LOCK five-site CHECKs, four-field Rebuttal, no per-cell directives), adding only C-30 at charter fields. |
| V-03 | BEFORE-PRODUCE back-reference for non-FORMAT-CONTRACT structural forms (single axis, imperative register) | C-29 | Same mechanism as V-01 but built on R10 V-03 baseline (per-cell role-lock for DRI/Owner and Key Roles, strict mandatory DRI/Owner ROLE-LOCK, no FORMAT CONTRACT, no four-field Rebuttal). Since C-14 is not in the R10 V-03 baseline, C-29 applies only to the ROLE-NAME LOCK structural form in this variation. The BEFORE-PRODUCE directive targets the ROLE-NAME LOCK's emission: "BEFORE EMITTING THE ROLE-NAME LOCK: count the roles in ROLES-LOADED -- the lock must enumerate exactly that count, no more, no fewer." Variation axis is phrasing register: V-01 uses declarative BEFORE-PRODUCING language parallel to C-26; V-03 uses imperative command-register phrasing ("DO NOT emit the ROLE-NAME LOCK until you have counted the ROLES-LOADED entries and confirmed the enumeration is complete") to test whether command-register framing produces higher mechanical compliance than schema-reference framing for structural-form back-references. |
| V-04 | C-29 + C-30 combined on R10 V-04 baseline | C-29, C-30 | R10 V-04 has FORMAT CONTRACT DISQUALIFY-IF, BEFORE-PRODUCE for FC schemas, four-field Rebuttal activation triad, MECHANISM-TYPE VOCABULARY, TRIGGER-TYPE VOCABULARY, CAT-N-CITATION-SCHEMA, and ROLE-NAME LOCK with five-site enumeration. It does not have: (a) BEFORE-PRODUCE for the Rebuttal form or ROLE-NAME LOCK block (C-29 gap), or (b) per-role-name CHECK in charter fields (C-30 gap). This variation adds both mechanisms to the R10 V-04 baseline, testing whether two non-overlapping additions -- temporal gap closure for structural forms (C-29) and intra-field role drift closure for charter multi-role lists (C-30) -- produce compounded coverage gains without introducing prompt-complexity failures. DRI/Owner per-cell directive (C-28) is intentionally absent so the delta from V-04 to V-05 isolates exactly the per-cell mechanism's contribution. |
| V-05 | Full integration: C-29 + C-30 on R10 V-05 baseline | C-29, C-30, all prior | Maximum mechanical stack. R10 V-05 covers C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad), C-25 (strict mandatory DRI/Owner), C-26 (BEFORE-PRODUCE for all FC schemas), C-27 (Key Roles fifth site), C-28 (per-cell for DRI/Owner and Key Roles). R11 V-05 adds: (a) BEFORE-PRODUCING THE ROLE-NAME LOCK directive naming its required content before the lock is emitted; (b) BEFORE PRODUCING THE REBUTTAL directive naming all four fields before the REBUTTAL FORM block is produced; (c) per-role-name CHECK embedded in each charter Membership and Decides field instruction, explicitly stating that each name is verified against the ROLE-NAME LOCK before the next name is appended. Together C-29 and C-30 complete the temporal-gap and granularity-gap enforcement hierarchies: C-29 extends BEFORE-PRODUCE coverage to all governed structural forms regardless of where their contract is declared; C-30 extends per-granularity role-lock enforcement from table row (C-28) to intra-field name (C-30), completing the four-level hierarchy: document declaration (C-13) -> section CHECK (C-21) -> column/field instruction (C-25/C-27) -> row/name per-item verify (C-28/C-30). |

---

## V-01 -- BEFORE-PRODUCE for Non-FORMAT-CONTRACT Structural Forms (single axis)

**Axis**: BEFORE-PRODUCE back-reference directive extended to ROLE-NAME LOCK block and four-field Rebuttal form (C-29)
**Hypothesis**: The temporal gap principle (C-26) applies equally to structural forms defined outside
the FORMAT CONTRACT. The ROLE-NAME LOCK block is produced 500+ tokens after ROLES-LOADED is read;
the Rebuttal form is produced 2,000+ tokens after its four-field template is declared. BEFORE-PRODUCE
directives naming the required fields immediately before each PRODUCE command convert both from
multi-thousand-token recall requirements into per-step active lookups. Built on R10 V-02 baseline
(ROLE-NAME LOCK five-site enumeration, four-field Rebuttal, inline CHECKs at all five sites).

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

BEFORE PRODUCING THE ROLE-NAME LOCK: re-read the ROLES-LOADED block above. Count the roles present.
The ROLE-NAME LOCK must enumerate exactly those roles -- no role absent from ROLES-LOADED, no role invented
here. Confirm the count before emitting the block.

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

BEFORE PRODUCING THE REBUTTAL: re-read the four-field form below -- all four fields must be present
in this order: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL /
RE-ASSESSMENT TRIGGER. Confirm each field label is present before beginning to populate any field.

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
3.  [BEFORE PRODUCING THE ROLE-NAME LOCK: re-read ROLES-LOADED, confirm count] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment:
    mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [BEFORE PRODUCING THE REBUTTAL: re-read four-field form] /
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

## V-02 -- Per-Role-Name Role-Lock CHECK in Charter Fields (single axis)

**Axis**: Per-role-name role-lock CHECK within committee charter Membership and Decides
multi-role lists (C-30)
**Hypothesis**: The section-level CHECK [SITE 3 -- CHARTER] fires once before the Membership
list is written. A charter with four listed members can introduce a novel role name at position 3
while satisfying the CHECK -- because the CHECK applies to the section collectively and has faded
by the time the third name is appended. C-30 adds a per-role-name directive: "for each role name
in Membership and Decides, verify it appears in the ROLE-NAME LOCK list before appending the
next name." This is the intra-field analogue of C-28's per-cell row directive for table columns.
Built on R10 V-02 baseline (ROLE-NAME LOCK five-site CHECKs, four-field Rebuttal).

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
      [per-role-name directive applies: verify each name before appending the next,
       do not write the full list and verify after]
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

ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK list.
Verify each name before drawing it.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes -- not embedded in an area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

CHECK [SITE 5 -- KEY ROLES]: This column is the fifth mandatory ROLE-NAME LOCK CHECK site.
Every role name in the Key Roles column must appear in the ROLE-NAME LOCK list above.
No new role names may be introduced in this column. This is a first-class enforcement site.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`.
CHECK [SITE 2 -- DRI/OWNER]: every value in the DRI / Owner column must appear in the ROLE-NAME LOCK list.
No new role names are introduced in this column. Verify before writing each DRI / Owner value.
Minimum three rows: ROB, one shiproom or gate meeting, one governance meeting. No merged rows.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.

CHECK [SITE 3 -- CHARTER]: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list.

Per-role-name directive for Membership and Decides fields:
For each role name in the Membership field: verify the name appears in the ROLE-NAME LOCK list before
appending the next name. Do not write the full Membership list and verify after -- verify each role name
individually before adding the next. A novel role name at any position in the list (including position 3
of a four-role list) is a violation regardless of whether prior names complied.

Apply the identical per-role-name directive to the Decides field: for each role name listed in Decides,
verify it appears in the ROLE-NAME LOCK list before appending the next name.

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
3.  ROLE-NAME LOCK (complete permitted-role enumeration + five-site CHECK enumeration
    + per-role-name note at site 3)
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment:
    mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [REBUTTAL FORM: CHECK SITE 4 embedded at ROLE UNDER PRESSURE] /
    [VERIFY: future-tense fails] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK SITE 1]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK SITE 5 -- KEY ROLES]
10. Operating Rhythm Table [CHECK SITE 2 -- DRI/OWNER]
11. Committee Charters [CHECK SITE 3] [per-role-name: verify each name before appending next]
12. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- BEFORE-PRODUCE for ROLE-NAME LOCK in Imperative Register (single axis)

**Axis**: BEFORE-PRODUCE back-reference for non-FORMAT-CONTRACT structural forms (C-29),
imperative command-register phrasing variant
**Hypothesis**: V-01 uses declarative BEFORE-PRODUCING language parallel to C-26 schema
back-references ("BEFORE PRODUCING THE ROLE-NAME LOCK: re-read ROLES-LOADED"). V-03 tests whether
imperative/prohibitive framing ("DO NOT emit the ROLE-NAME LOCK until you have counted the
ROLES-LOADED entries and confirmed the enumeration is complete") produces higher compliance for
the structural-form temporal gap than schema-reference framing. Built on R10 V-03 baseline (per-cell
role-lock for DRI/Owner and Key Roles, strict mandatory DRI/Owner ROLE-LOCK, no FORMAT CONTRACT,
no four-field Rebuttal). C-29 is applied only to the ROLE-NAME LOCK structural form here, since
C-14 (four-field Rebuttal) is not in the R10 V-03 baseline. Variation axis: phrasing register.

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

DO NOT emit the ROLE-NAME LOCK until you have done the following:
  1. Counted the roles in ROLES-LOADED (or ROLES-NOTE).
  2. Confirmed that the lock enumeration you are about to write contains exactly that count.
  3. Verified that no role in the enumeration is absent from ROLES-LOADED.
Emitting the ROLE-NAME LOCK before completing steps 1-3 is not permitted.

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
as you populate. A novel role name entered in any Key Roles cell is a violation regardless of table position.

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
as you populate. A novel role name entered in any DRI/Owner cell is a violation regardless of row position.

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
3.  [DO NOT emit ROLE-NAME LOCK until ROLES-LOADED count verified] ROLE-NAME LOCK
4.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    Rebuttal [CHECK, role-grounded] / VERDICT)
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

## V-04 -- C-29 + C-30 Combined on R10 V-04 Baseline

**Axis**: BEFORE-PRODUCE for non-FORMAT-CONTRACT structural forms (C-29) combined with per-role-name
CHECK in charter Membership and Decides (C-30), on R10 V-04 baseline
**Hypothesis**: R10 V-04 covers FORMAT CONTRACT DISQUALIFY-IF, BEFORE-PRODUCE for FC schemas,
four-field Rebuttal activation triad, MECHANISM-TYPE VOCABULARY, TRIGGER-TYPE VOCABULARY,
CAT-N-CITATION-SCHEMA, and ROLE-NAME LOCK with five-site enumeration. Two gaps remain: (a) the
Rebuttal form and ROLE-NAME LOCK block have no BEFORE-PRODUCE directive (C-29); (b) charter
Membership and Decides multi-role lists have a section-level CHECK but no per-role-name enforcement
(C-30). Adding both: C-29 closes the temporal gap for structural forms defined outside the FC;
C-30 closes the intra-field compliance-drift gap in charter multi-role lists. DRI/Owner per-cell
directive (C-28) intentionally absent -- V-04 to V-05 delta isolates C-28's contribution.

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
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

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
separate columns (Area, Headcount, Key Roles, Decides, Escalates) will be used and that the DISQUALIFY-IF
condition (merged Decides/Escalates) will not be met in this output.

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
appending the next name. Do not write the complete Membership list and verify after -- verify each name
before adding the next. A novel role name at any position (including position 3 of a four-role list)
is a violation regardless of whether earlier names complied.

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

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  [BEFORE PRODUCING THE ROLE-NAME LOCK: re-read ROLES-LOADED] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration + per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
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
15. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [BEFORE PRODUCING schema (5)]
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-29 + C-30 on R10 V-05 Baseline

**Axis**: BEFORE-PRODUCE for non-FORMAT-CONTRACT structural forms (C-29) + per-role-name CHECK
in charter Membership and Decides (C-30), layered on R10 V-05 full-integration baseline
**Hypothesis**: R10 V-05 covers C-23 (FORMAT CONTRACT DISQUALIFY-IF), C-24 (activation triad
with embedded CHECK at ROLE UNDER PRESSURE), C-25 (strict mandatory DRI/Owner ROLE-LOCK),
C-26 (BEFORE-PRODUCE for all FC schemas), C-27 (Key Roles fifth site), C-28 (per-cell for
DRI/Owner and Key Roles). R11 V-05 adds: (a) BEFORE-PRODUCING THE ROLE-NAME LOCK directive
naming ROLES-LOADED as the authority before the lock is emitted (C-29 applied to C-13 structural
form); (b) BEFORE PRODUCING THE REBUTTAL directive naming all four fields before the REBUTTAL FORM
block is produced (C-29 applied to C-14 structural form); (c) per-role-name CHECK in Membership
and Decides field instructions, verifying each name against the ROLE-NAME LOCK before appending
the next (C-30). Together C-29 and C-30 complete the two remaining enforcement gaps: C-29 extends
BEFORE-PRODUCE coverage from FORMAT CONTRACT schemas to all governed structural forms; C-30
extends per-granularity role-lock from table row (C-28) to intra-field name, completing the
four-level hierarchy: document declaration (C-13) -> section CHECK (C-21) -> column/field
instruction (C-25/C-27) -> row/name per-item verify (C-28/C-30).

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

BEFORE PRODUCING THE ROLE-NAME LOCK: re-read the ROLES-LOADED block. Count the roles present.
Confirm that the lock enumeration you are about to write contains exactly those roles -- no role
absent from ROLES-LOADED, no role invented here that was not in ROLES-LOADED. The lock must be
a complete, faithful enumeration of the roles in ROLES-LOADED, neither adding nor omitting any.

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
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 -- Rebuttal

BEFORE PRODUCING THE REBUTTAL: re-read the four-field form definition below. All four field labels
must appear in this order: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL /
RE-ASSESSMENT TRIGGER. Confirm each label is present in the template before populating any field.
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
4.  [BEFORE PRODUCING THE ROLE-NAME LOCK: re-read ROLES-LOADED, confirm count] ROLE-NAME LOCK
    (complete permitted-role enumeration + five-site CHECK enumeration
    + per-cell notes at sites 2 and 5 + per-role-name note at site 3)
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [BEFORE PRODUCING THE REBUTTAL: re-read four-field form, confirm all four labels] /
    [REBUTTAL FORM: CHECK SITE 4 at ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN /
    WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER] /
    [VERIFY: future-tense fails] / VERDICT
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
    [per-role-name Membership: verify each name before appending next]
    [per-role-name Decides: verify each name before appending next]
    [VERIFY: short Quorum -- fraction form required]
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. [BEFORE PRODUCING schema (4)] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE -- ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + [BEFORE PRODUCING schema (5)]
    Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`
