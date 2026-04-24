---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 9
rubric: simulations/quest/rubrics/corps-chart-rubric-v8-2026-03-17.md
---

# Quest Variate — corps-chart (Round 9)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R9 targets rubric additions in v8 that were absent or incomplete in prior rounds:
- C-23 (FORMAT CONTRACT with per-schema DISQUALIFY-IF annotations — pre-generation disqualification layer)
- C-24 (Four-field form + ROLE-NAME LOCK CHECK + VERIFY activation triad at ROLE UNDER PRESSURE)
- C-25 (DRI/Owner strict mandatory ROLE-LOCK — no softening qualifiers, first-class enforcement site)

R8 V-05 provides the baseline for full-integration (V-05). Single-axis variations build from
narrower R8 baselines to isolate each new mechanism.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | FORMAT CONTRACT DISQUALIFY-IF (single axis) | C-23 | Adding inline DISQUALIFY-IF annotations inside the FORMAT CONTRACT at schema-declaration time fires a pre-generation disqualification signal before any PRODUCE command runs. The FORMAT CONTRACT is in immediate context at every writing moment; placing disqualification conditions there — rather than only at VERIFY blocks — tests whether schema-time signal alone reduces merged-column, denominator-free Quorum, and untyped cat-N failures without requiring any change to the production-step instructions. |
| V-02 | Four-field Rebuttal activation triad (single axis) | C-24 | The C-24 triad requires three co-dependent mechanisms at ROLE UNDER PRESSURE: (a) the four-field form creates the structural anchor, (b) a ROLE-NAME LOCK CHECK embedded as the form's header instruction attaches role-governance to that anchor, (c) a VERIFY block disqualifies future-tense breakdowns. R8 V-05 had all three elements but the CHECK was placed as a separate Rebuttal-level sentence rather than embedded inside the form block header. Testing the embedded-CHECK form variant determines whether co-location of the CHECK with the ROLE UNDER PRESSURE field label is what makes C-24's activation triad structurally complete. |
| V-03 | Strict DRI/Owner ROLE-LOCK enforcement (single axis) | C-25 | Prior rounds produced C-12 partials because the DRI/Owner instruction used hedged language ("where possible", "reference a role from ROLES-LOADED") rather than mandatory enforcement. C-25 requires present-tense mandatory language in the same instruction block as DRI/Owner formatting requirements. Testing this change alone — on a clean R8 V-02-style baseline with ROLE-NAME LOCK present — isolates whether strict mandatory language at DRI/Owner closes the column-level role-coherence gap without the FORMAT CONTRACT or activation triad. |
| V-04 | C-23 DISQUALIFY-IF + C-24 activation triad (combination) | C-23, C-24 | Two-phase disqualification: FORMAT CONTRACT DISQUALIFY-IF fires before generation begins; C-18 VERIFY blocks fire at each PRODUCE command; and the C-24 activation triad (form + embedded CHECK + VERIFY) provides structural role-grounding at ROLE UNDER PRESSURE. Combines these two new mechanisms on an R8 V-04-style baseline (FORMAT CONTRACT + vocabulary-lock/VERIFY pairs already present) to test whether C-23 + C-24 closes the remaining gaps without adding C-25 strict DRI/Owner enforcement. DRI/Owner remains the open variable. |
| V-05 | Full integration: C-23 + C-24 + C-25 on R8 V-05 baseline | C-23, C-24, C-25, all prior | Maximum mechanical stack. R8 V-05 provided FORMAT CONTRACT, ROLE-NAME LOCK with per-section CHECKs, vocabulary-lock/VERIFY co-deployment, 5th phase gate, and four-field Rebuttal form. R9 V-05 adds: (a) DISQUALIFY-IF annotations inside the FORMAT CONTRACT for all three schemas with documented failure modes, (b) the C-24 activation triad with CHECK embedded inside the four-field form block header, (c) strict mandatory DRI/Owner language with explicit ROLE-NAME LOCK reference and no softening qualifiers. Tests whether full constraint density across all 25 criteria produces maximum rubric score or induces section-complexity failures. |

---

## V-01 — FORMAT CONTRACT DISQUALIFY-IF (single axis)

**Axis**: Inline DISQUALIFY-IF annotations inside the UPFRONT FORMAT CONTRACT at schema-declaration time (C-23)
**Hypothesis**: The root cause of merged-column, denominator-free Quorum, and untyped cat-N failures is that the model cannot recall from 1,500+ tokens away what the exact disqualifying output variants are. Placing DISQUALIFY-IF annotations inside the FORMAT CONTRACT — which is in immediate context at every writing moment — fires a pre-generation signal before the model reaches any PRODUCE command. This single-axis test builds on R8 V-01's FORMAT CONTRACT but adds the DISQUALIFY-IF layer, leaving vocabulary-lock/VERIFY machinery and ROLE-NAME LOCK absent to isolate the C-23 contribution.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING
=======================================================
The following five schemas apply throughout this document.
Reference this block when producing each section. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Required columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles cell format: [role name] ([domain type])
    Required rows: minimum two area rows + one **Total** row with the sum.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") — the five-column schema
                   requires separate Decides and Escalates columns.

(2) OPERATING RHYTHM TABLE
    Required columns: Cadence | Frequency | DRI / Owner | Purpose
    Required rows: minimum three — one ROB, one shiproom or gate meeting, one governance meeting.
    Two meetings must not be merged into one row.

(3) COMMITTEE CHARTER — one block per governance meeting in the rhythm table
    Purpose:    [text]
    Membership: [role name] ([domain type]), [role name] ([domain type]), ... (minimum two roles)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward — must name a destination, not "everything else"]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M
                   (e.g., "3 members required for binding decisions" without "of M member roles") —
                   the fraction form [N] of [M] member roles required is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               — [area name] — headcount: [N]
    cat-2 (Committees/Cadences) — [name]
    cat-3 (Headcount)           — Total headcount: [N]
    cat-4 (DRI Roles)           — [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Required columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" cell format: [element name] (cat-N) — [one sentence of specific relevance]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N) typed
                   citation prefix — every cell must open with [element name] (cat-N) — before
                   the relevance sentence.

---

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
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

Name the coordination failure the flat-team case cannot answer. Reference a specific observable: a blocked
decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the current failure mode.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Write a re-assessment trigger naming a concrete threshold. DO NOT write "revisit as the team grows."

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw an ASCII hierarchy with minimum two levels. Committees appear as distinct labeled nodes — not embedded inside an area box.
Role names must match ROLES-LOADED or ROLES-NOTE. DO NOT introduce new role names.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce per schema (1) in the FORMAT CONTRACT above.
The schema includes a DISQUALIFY-IF annotation — re-read it before producing this table.
Five-column schema required: Area | Headcount | Key Roles | Decides | Escalates.
Minimum two area rows plus `**Total**` row with the sum.

OPERATING RHYTHM TABLE

Produce per schema (2) above. Minimum three rows: ROB, shiproom/gate, governance. No merged rows.
Reference a role from ROLES-LOADED in DRI / Owner where a role is known.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table per schema (3) above.
The schema includes a DISQUALIFY-IF annotation — re-read it before producing each Quorum field.
Escalates must name a destination — not "everything not listed under Decides."

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce per schema (4) above immediately after the charters gate. All four categories required.
DO NOT proceed to Org Evolution Roadmap until all four are populated.

ORG EVOLUTION ROADMAP

Produce a trigger table: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: a different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Produce per schema (5) above. Minimum two rows.
The schema includes a DISQUALIFY-IF annotation — re-read it before producing each "Why It Applies Here" cell.
Every cell must open with: `[element name] (cat-N) — [one sentence]`.

SECTION ORDER

1.  UPFRONT FORMAT CONTRACT (present above)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [schema 1 — re-read DISQUALIFY-IF]
10. Operating Rhythm Table [schema 2]
11. Committee Charters [schema 3 — re-read DISQUALIFY-IF on Quorum]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER [schema 4]
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch [schema 5 — re-read DISQUALIFY-IF]

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-02 — Four-Field Rebuttal Activation Triad (single axis)

**Axis**: C-24 activation triad — four-field form with ROLE-NAME LOCK CHECK embedded as the form block header, co-deployed with VERIFY (C-24)
**Hypothesis**: R8 V-05 placed the CHECK as a sentence before the four-field form block ("CHECK: any role name written in this sub-section must appear in the ROLE-NAME LOCK list"). C-24 requires the CHECK to be embedded immediately before the ROLE UNDER PRESSURE field instruction — inside the form block, not preceding it. The distinction is structural: when the CHECK is inside the form, the model cannot begin filling ROLE UNDER PRESSURE without passing through the CHECK. When the CHECK is outside the form, the model reads the CHECK, writes the form header, and the CHECK context has faded before ROLE UNDER PRESSURE is filled. This variation tests that embedded-CHECK-inside-form distinction on an R8 V-02-style baseline (ROLE-NAME LOCK with per-section CHECKs, no FORMAT CONTRACT), isolating C-24 alone.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Carry annotation forward: `[role name] ([domain type])` in Key Roles cells and Charter Membership fields.

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

DO write before any org boxes. Order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns currently in use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Use this mandatory four-field form. The CHECK is part of the form — do not skip it:

```
REBUTTAL FORM
=============
CHECK: ROLE UNDER PRESSURE must name exactly one role from the ROLE-NAME LOCK list above.
       No new role names may be introduced. Verify the name is in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure — not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold — specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step. The breakdown must describe
a failure that exists now, not a risk that may emerge with growth.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies; restate only if different from what was written there.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK: every role name placed in this diagram must appear in the ROLE-NAME LOCK list. Verify each name before drawing it.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes — not embedded inside an area box.
DO NOT introduce names not in the ROLE-NAME LOCK.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
CHECK: every role name in Key Roles must appear in the ROLE-NAME LOCK list.
DO NOT merge Decides and Escalates into a single column.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles annotated: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`.
DRI / Owner column: every value must appear in the ROLE-NAME LOCK list — no new role names are
introduced in this column.
CHECK: before writing each DRI / Owner cell, verify the role name is in the ROLE-NAME LOCK list.
Minimum three rows: ROB, one shiproom or gate meeting, one governance meeting. No merged rows.

COMMITTEE CHARTERS

Write a charter per governance meeting in the rhythm table: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
CHECK: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list. Verify before writing.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: must name a destination — not "everything not listed under Decides."
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`
All four categories required. No category may be empty.

ORG EVOLUTION ROADMAP

Produce: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: a different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every "Why It Applies Here" cell must open with: `[element name] (cat-N) — [one sentence]`.
cat-N codes must match the ORG-ELEMENT REGISTER (cat-1 through cat-4).

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  ROLE-NAME LOCK (complete permitted-role enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment:
    mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [REBUTTAL FORM with embedded CHECK at ROLE UNDER PRESSURE] / [VERIFY: future-tense fails] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK against ROLE-NAME LOCK]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK Key Roles]
10. Operating Rhythm Table [strict DRI/Owner ROLE-LOCK + CHECK]
11. Committee Charters [CHECK Membership+Decides]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-03 — Strict DRI/Owner ROLE-LOCK Enforcement (single axis)

**Axis**: DRI/Owner column designated as first-class strict role-coherence enforcement site with mandatory language and no softening qualifiers (C-25)
**Hypothesis**: R8 V-02 placed a CHECK at the DRI/Owner column but the instruction read "Reference a role from ROLES-LOADED in DRI / Owner where possible" — hedged language that permits novel role introduction when convenient. C-25 requires present-tense mandatory language ("every DRI/Owner value must appear in the ROLE-NAME LOCK list — no new role names are introduced in this column") in the same instruction block as other DRI/Owner formatting requirements. This variation tests the strict mandatory language change alone on a clean R8 V-02 baseline (ROLE-NAME LOCK with per-section CHECKs), without FORMAT CONTRACT or activation triad, to isolate whether strict DRI/Owner instruction language closes the C-12 partial pattern observed in prior rounds.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Classify in three-tier order: strategic roles first, then operational roles, then advisory and governance roles.
Assign each role exactly one type from: `(strategic) / (operational) / (advisory) / (governance)`.
Format: `- [role name] — [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.

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

DO write before any org boxes. Order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

Produce: `Mechanism Name | Type | Frequency / Participants`.
Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns currently in use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

CHECK: any role name referenced in this sub-section must appear in the ROLE-NAME LOCK list. Verify before writing.
Name the coordination failure the flat-team case cannot answer. Reference a specific observable: blocked
decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the current failure mode.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

CHECK: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify each before drawing.
Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes — not embedded in an area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
CHECK: every role name in Key Roles must appear in the ROLE-NAME LOCK list. Verify before writing.
DO NOT merge Decides and Escalates.
Decides: decision types owned at this level. Escalates: decisions referred upward, naming the destination.
Key Roles: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose` with these requirements applied together:
  - Minimum three rows: one ROB, one shiproom or gate meeting, one governance meeting.
  - DRI / Owner column: every value must appear in the ROLE-NAME LOCK list — no new role names
    are introduced in this column. This column is a first-class role-coherence enforcement site.
    "Where possible" or equivalent hedged language does not apply here. Every DRI/Owner cell must
    name a role from the ROLE-NAME LOCK list or be left blank — it must never introduce a new name.
  - No merged rows.

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
All four categories required. No category may be empty.

ORG EVOLUTION ROADMAP

Produce: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal, structural symptom, or milestone event).
DO NOT use two headcount thresholds.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every "Why It Applies Here" cell must open with: `[element name] (cat-N) — [one sentence]`.
cat-N codes from the ORG-ELEMENT REGISTER (cat-1 through cat-4).

SECTION ORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
3.  ROLE-NAME LOCK (complete permitted-role enumeration)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today /
    Rebuttal [CHECK] / VERDICT)
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram [CHECK against ROLE-NAME LOCK]
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [CHECK Key Roles]
10. Operating Rhythm Table [strict DRI/Owner ROLE-LOCK — mandatory language, no hedging]
11. Committee Charters [CHECK Membership+Decides]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
16. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-04 — C-23 DISQUALIFY-IF + C-24 Activation Triad (combination)

**Axis**: FORMAT CONTRACT with DISQUALIFY-IF annotations (C-23) combined with four-field Rebuttal activation triad — embedded CHECK + form + VERIFY (C-24)
**Hypothesis**: The two mechanisms target adjacent failure points in the generation sequence. DISQUALIFY-IF annotations in the FORMAT CONTRACT fire before any PRODUCE command; the C-24 activation triad fires inside the Inertia Assessment sub-section. Together they create a two-phase safety net: the FORMAT CONTRACT communicates at schema-declaration time what the model must not produce, and the Rebuttal triad enforces role-grounding and observable-breakdown discipline at the point where those failures typically occur. Building on an R8 V-04-style base (FORMAT CONTRACT + vocabulary-lock/VERIFY pairs already present) tests whether adding C-23 and C-24 closes the remaining gaps without C-25. DRI/Owner remains the open variable.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations for schemas with documented failure modes.
Reference this block when producing each section. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope") — five separate columns are required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.

(3) COMMITTEE CHARTER — one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward — must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M (e.g., "3 members required") —
                   the fraction form [N] of [M] member roles required is mandatory.

(4) ORG-ELEMENT REGISTER
    cat-1 (Areas)               — [area name] — headcount: [N]
    cat-2 (Committees/Cadences) — [name]
    cat-3 (Headcount)           — Total headcount: [N]
    cat-4 (DRI Roles)           — [DRI role]
    All four categories required. No category may be empty.

(5) ANTI-PATTERN WATCH
    Columns: Anti-Pattern | Why It Applies Here | Mitigation
    "Why It Applies Here" format: [element name] (cat-N) — [one sentence]
    Valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N)
                   typed citation prefix — every cell must carry the typed prefix.

---

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description]` per role.
If no files are found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` with inferred roles.
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

Before writing the mechanism table, emit:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values:
  Channel           — async or sync communication path
  Informal Role     — person-as-coordinator without formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows.
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

VERIFY: A mechanism row whose Type value is not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If count < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns in active use. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Use this mandatory four-field form. The embedded CHECK is part of the form — do not skip it:

```
REBUTTAL FORM
=============
CHECK: ROLE UNDER PRESSURE must name exactly one role from ROLES-LOADED or ROLES-NOTE.
       No new role names may be introduced here. Verify the role name before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from ROLES-LOADED or ROLES-NOTE]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure — not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold — specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning must reference FLAT-CASE-PRESSURE.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw ASCII hierarchy with minimum two levels. Committees as distinct labeled nodes — not embedded in any area box.
Role names must match ROLES-LOADED or ROLES-NOTE.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce per schema (1) of the FORMAT CONTRACT above.

VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy this step.
Five-column schema required. Re-read the FORMAT CONTRACT DISQUALIFY-IF before producing this table.

Minimum two area rows plus `**Total**`. Key Roles: `[role name] ([domain type])`.

OPERATING RHYTHM TABLE

Produce per schema (2) above. Minimum three rows: ROB, shiproom or gate, governance. No merged rows.
Reference a role from ROLES-LOADED in DRI / Owner where a role is known.

COMMITTEE CHARTERS

Produce per schema (3) above for each governance meeting.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M
does not satisfy this step. Re-read the FORMAT CONTRACT DISQUALIFY-IF before producing each Quorum field.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce per schema (4) above immediately after the charters gate. All four categories required.
DO NOT proceed to Org Evolution Roadmap until all four are populated.

ORG EVOLUTION ROADMAP

Before writing the trigger table, emit:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values:
  headcount threshold — a specific hire count that changes coordination needs
  workload signal     — measurable increase in cross-area dependencies or throughput
  structural symptom  — observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event     — named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce: `Trigger | Structural Change | Type`. Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

When roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`

ANTI-PATTERN WATCH

Before writing the table, emit:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 — Areas           cat-2 — Committees/Cadences
  cat-3 — Headcount       cat-4 — DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) — [one sentence of specific relevance]

A cell naming an org element without the (cat-N) typed prefix does not satisfy this schema.
```

Produce per schema (5) above. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row. Re-read FORMAT CONTRACT DISQUALIFY-IF before
producing this table.

SECTION ORDER — 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF annotations)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [REBUTTAL FORM with embedded CHECK at ROLE UNDER PRESSURE] / [VERIFY: future-tense] / VERDICT
6.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7.  ASCII Org Diagram
8.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9.  Headcount by Area [VERIFY: merged column — re-read DISQUALIFY-IF]
10. Operating Rhythm Table
11. Committee Charters [VERIFY: short Quorum — re-read DISQUALIFY-IF]
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold]
15. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
16. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch [VERIFY: untyped citation — re-read DISQUALIFY-IF]

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-05 — Full Integration: C-23 + C-24 + C-25 on R8 V-05 Baseline

**Axis**: FORMAT CONTRACT with DISQUALIFY-IF (C-23) + four-field Rebuttal activation triad with embedded CHECK (C-24) + strict mandatory DRI/Owner ROLE-LOCK with no softening qualifiers (C-25), layered on the R8 V-05 full-integration baseline
**Hypothesis**: R8 V-05 covered C-17 through C-22 but lacked C-23, C-24, C-25. Adding all three: (a) DISQUALIFY-IF annotations inside the FORMAT CONTRACT pre-declare what constitutes a failing output for three schemas before any section is produced; (b) the C-24 activation triad places the ROLE-NAME LOCK CHECK inside the REBUTTAL FORM block header — co-located with the ROLE UNDER PRESSURE field label — so the model cannot fill that field without passing through the governance constraint; (c) the DRI/Owner column carries mandatory present-tense enforcement language in the same instruction block as its formatting requirements, treating it as a first-class role-coherence site equivalent to Charter Membership and Decides. The three mechanisms close three distinct, non-overlapping failure modes: format-evasion (C-23), Rebuttal role-grounding and observable-breakdown compliance (C-24), and DRI/Owner role drift (C-25). Testing full constraint density across all 25 criteria.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING
=======================================================
All five output schemas with DISQUALIFY-IF annotations for schemas with documented failure modes.
Reference this block at each section. No output is produced before reading it.

(1) HEADCOUNT BY AREA
    Columns: Area | Headcount | Key Roles | Decides | Escalates
    Key Roles: [role name] ([domain type]). Total row required.
    DISQUALIFY-IF: Decides and Escalates are merged into a single column
                   (e.g., "Decision Scope" or "Decision Authority") — five separate columns required.

(2) OPERATING RHYTHM TABLE
    Columns: Cadence | Frequency | DRI / Owner | Purpose
    DRI / Owner: every value must appear in the ROLE-NAME LOCK list — no new role names introduced.
    Minimum three rows: ROB, one shiproom or gate, one governance meeting. No merged rows.

(3) COMMITTEE CHARTER — one block per governance meeting
    Purpose:    [text]
    Membership: [role name] ([domain type]), ... (minimum two roles from ROLE-NAME LOCK)
    Decides:    [decision types owned at this level]
    Escalates:  [decision types referred upward — must name a destination]
    Quorum:     [N] of [M] member roles required for binding decisions
    DISQUALIFY-IF: Quorum field omits the denominator M (e.g., "3 members required") —
                   the fraction form [N] of [M] member roles required is mandatory.

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
    DISQUALIFY-IF: a "Why It Applies Here" cell names an org element without the (cat-N)
                   typed citation prefix — the typed prefix is mandatory for every cell.

---

STEP 1 — LOAD ROLES

Read `.roles/`. Produce `ROLES-LOADED:` block: `- [role name] — [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:` instead.
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
Permitted Type values for the mechanism table:
  Channel           — async or sync communication path
  Informal Role     — person-as-coordinator without formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.
Every Type cell: one value from MECHANISM-TYPE VOCABULARY only.

VERIFY: A mechanism row with a Type value not in {Channel, Informal Role, Recurring Cadence, Shared Artifact}
does not satisfy this step.

Count rows. If < 2, add rows.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 — Rebuttal

Use this mandatory four-field form. The embedded CHECK is part of the form — do not skip it:

```
REBUTTAL FORM
=============
CHECK: ROLE UNDER PRESSURE must name exactly one role from the ROLE-NAME LOCK list above.
       No new role names may be introduced. Verify the name is in the lock before writing it.

ROLE UNDER PRESSURE:          [name exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN:         [describe a current coordination failure — not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER:        [concrete measurable threshold — specific hire count, named milestone,
                               or structural symptom such as two or more missed ship dates
                               attributable to cross-area misalignment]
```

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN is filled with "As we scale..." or "as the team grows..."
without naming a current observable failure does not satisfy this step. The breakdown must describe
a failure that exists now.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The RE-ASSESSMENT TRIGGER from the four-field form applies — restate only if different.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 5 — ASCII ORG DIAGRAM

CHECK: every role name in this diagram must appear in the ROLE-NAME LOCK list. Verify before placing.
Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes — not embedded in any area box.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 — HEADCOUNT BY AREA

Produce per schema (1) of the FORMAT CONTRACT.

VERIFY: A table that merges Decides and Escalates into a "Decision Scope" column does not satisfy this step.
Re-read the FORMAT CONTRACT DISQUALIFY-IF before producing this table. Five-column schema required.

CHECK: every role name in Key Roles must appear in the ROLE-NAME LOCK list.
Minimum two area rows plus `**Total**`. Key Roles: `[role name] ([domain type])`.

STEP 7 — OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose` with all requirements applied together:
  - DRI / Owner column: every value must appear in the ROLE-NAME LOCK list — no new role names
    are introduced in this column. This column is a first-class role-coherence enforcement site.
    "Where possible" or equivalent hedged language does not apply. Every DRI/Owner cell must name
    a role from the ROLE-NAME LOCK list or be left blank — it must never introduce a new name.
  - Minimum three rows: one ROB, one shiproom or gate meeting, one governance meeting.
  - No merged rows.

STEP 8 — COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

CHECK: every role name in Membership and Decides must appear in the ROLE-NAME LOCK list. Verify before writing.

VERIFY: A Quorum written as "Quorum: [N roles required for binding decisions]" without denominator M
does not satisfy this step. Re-read FORMAT CONTRACT DISQUALIFY-IF. The fraction form [N] of [M] is required.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 — ORG-ELEMENT REGISTER

Produce per schema (4) of the FORMAT CONTRACT immediately after the charters gate.
All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 — ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values for the trigger table:
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

A cell naming an org element without the (cat-N) typed prefix does not satisfy this schema.
```

Produce per schema (5) of the FORMAT CONTRACT. Minimum two rows.

VERIFY: A "Why It Applies Here" cell that names an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row. Re-read FORMAT CONTRACT DISQUALIFY-IF
and the CAT-N-CITATION-SCHEMA before producing each cell.

SECTION ORDER — 17 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (with DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION (three-tier: strategic / operational / advisory+governance)
4.  ROLE-NAME LOCK (complete permitted-role enumeration + CHECK reminder)
5.  `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia: [MECHANISM-TYPE VOCAB] / table / [VERIFY: wrong type] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [REBUTTAL FORM: embedded CHECK at ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN /
    WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER] / [VERIFY: future-tense fails] / VERDICT
7.  `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram [CHECK against ROLE-NAME LOCK]
9.  `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area [VERIFY: merged column — re-read DISQUALIFY-IF] [CHECK Key Roles]
11. Operating Rhythm Table [strict mandatory DRI/Owner ROLE-LOCK — no hedging, first-class site]
12. Committee Charters [CHECK Membership+Decides] [VERIFY: short Quorum — re-read DISQUALIFY-IF]
13. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
14. ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + Org Evolution Roadmap [VERIFY: duplicate threshold type]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch [VERIFY: untyped citation — re-read DISQUALIFY-IF]

End with: `Generated by: /org-chart {topic} — {date}`
