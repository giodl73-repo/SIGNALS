---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R4
rubric_version: v3
status: variate
---

# org-chart Variate -- Round 4

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v3 (C-01--C-05 essential; R-01--R-03 recommended; A-01--A-07 aspirational /7)
**Round:** R4 -- convergence confirmation round

**R3 outcome:** V-05/R3 scored 100/100 under v3. No new excellence patterns emerged.
R4 purpose: confirm dual convergence (two consecutive rounds with no new patterns) through
structurally independent variations. All five variations must attempt 100/100 via different
structural approaches. If any variation surfaces a new excellence pattern, the rubric goes
to v4 and a new variate round follows.

**Known required elements (all R4 variations must carry these):**
- Adversarial burden statement BEFORE any mechanics (A-03)
- Pre-flight contract with CF-NN codes; downstream section headers cite the code(s) satisfied (A-06)
- ANNOTATION-REGISTER with Used-In tracking column (A-07)
- Explicit VERDICT BRANCH with CAN-OPERATE-FLAT investment-note worked example (A-04, R-02)
- Escalates affirmative exclusion clause -- not prohibition-only (A-05, R-03)
- Phase gates at ROLES / INERTIA / STRUCTURE / CHARTERS boundaries (R-01)
- All 5 essential criteria: Inertia 4-sub-sections (C-01), three artifacts (C-02),
  charters 5-fields + N-of-M Quorum (C-03), roles loaded + classified + propagated (C-04),
  annotation consistency (C-05)

---

## Round 4 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | Inertia quantification | Steelman mechanism table gains a fourth column for estimated weekly coordination cost; FLAT-CASE-PRESSURE rating must reference the total cost figure; re-assessment trigger may cite cost threshold | Anchoring the pressure rating in hours-per-week makes the steelman more falsifiable and harder to dismiss. A "Moderate (4)" rating supported by a quantified cost is a stronger inertia case than a qualitative judgment alone. The cost figure also propagates into the re-assessment trigger, making it concrete in units rather than headcount alone |
| V-02 | Prose charter format | Committee charters use labeled prose paragraphs (bold field label + sentence) instead of field:value table rows | Prose format forces the model to integrate the five required fields into coherent reasoning rather than slot values into a template. The N-of-M Quorum fraction is the key C-03 compliance risk: if the fraction disappears in prose context, the table format is structurally necessary |
| V-03 | Self-check phrasing register | DO/DO NOT imperatives replaced by "Confirm before proceeding: ..." interrogative gate questions at each section transition | Question-driven self-check may achieve structural compliance through internal consistency rather than external constraint. Tests whether rubric criteria pass with equal reliability under interrogative framing vs. imperative framing |
| V-04 | Eager-inline annotation register | ANNOTATION-REGISTER updated inline at each role citation site (Key Roles, Membership) rather than forward-declared and reconciled at the end | Eager inline population eliminates the deferred reconciliation step that may produce generic "used in headcount" entries. Tests whether inline updates produce more precise Used-In citations than forward-declaration + reconciliation |
| V-05 | Combined: quantified inertia + eager register | V-01 coordination-cost column + V-04 eager-inline register updates | Both axes are front-loading patterns: the cost metric anchors inertia reasoning at steelman time; the eager register anchors role propagation at citation time. Tests whether the two mechanisms compound |

---

## V-01 -- Quantified Inertia Steelman

**axis:** inertia framing -- coordination cost metric
**hypothesis:** Requiring an estimated weekly coordination cost per mechanism gives the
FLAT-CASE-PRESSURE rating an objective anchor. A rating supported by a cost figure
("approximately 3 hrs/week across 6 people") is harder to dismiss than the same rating
without one. The cost figure also propagates into the VERDICT justification and the
re-assessment trigger, making the trigger concrete in units.
Falsifiable: if cost estimates are too speculative to anchor the rating (e.g., "varies widely"),
quantification adds noise rather than an anchor.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Every structural element you propose must earn its place by naming a specific coordination
failure it prevents. Before loading roles or drawing diagrams, commit to this posture.

---

PRE-FLIGHT CONTRACT

The following contract codes govern this output. Every major section header MUST cite
the CF code(s) it satisfies in the format `(satisfies CF-NN)` or `(satisfies CF-NN, CF-MM)`.
A section header without a citation is incomplete. A CF code with no citing section is a
missing section.

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all other types third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost) >= 2 rows + FLAT-CASE-CLOSED separator with total cost figure |
| CF-04 | Inertia: How We Coordinate Today -- distinct content, named frequency and participants |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating, cost-anchored) + declaration + concrete re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: 5 fields; Quorum as N-of-M fraction; Escalates names specific destination |
| CF-11 | ORG-ELEMENT REGISTER with all 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations in every Why-It-Applies cell |

DO NOT begin any section until you have identified which CF code(s) it satisfies.
DO write the citing CF codes in the section header before writing that section's content.

---

ROLES-LOADED (satisfies CF-01)

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description]`.
If no files found, produce `ROLES-NOTE: No .roles/ files found. Using inferred roles:`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, PM / Design / Research / Other
types third. DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

MUST appear immediately after ROLES-LOADED or ROLES-NOTE.
Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.
DO NOT skip any role from the loaded list.

ANNOTATION-REGISTER

Produce immediately after ROLE-TYPE-CLASSIFICATION:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [leave blank -- fill on first downstream cite] |

Fill Used-In when each role first appears in a downstream section (Key Roles or Membership).
After the CHARTERS phase gate, perform ANNOTATION-REGISTER RECONCILIATION:
re-emit the table with all Used-In cells filled.
Flag any role with a blank Used-In as `PROPAGATION-GAP: [role name]`.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

DO write the Inertia Assessment before any org boxes.

Sub-section 1 -- Case for Staying Flat

DO produce a FOUR-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`

Type MUST use only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO include at minimum two data rows.
The Coordination Cost column MUST contain a time estimate per occurrence
(e.g., "2 hrs/week, 5 people" or "30 min/occurrence, 3 people").
DO NOT leave any Coordination Cost cell blank.

After writing the table:
- Count data rows (header excluded). If < 2, add rows until count >= 2.
- Sum the estimated weekly costs across all rows into a TOTAL COORDINATION COST figure.
- Emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {X} hrs/week across {Y} people. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2 and before the total is computed.
DO NOT begin Sub-section 2 before this separator.

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns currently in active use.
Name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

Name the coordination failure the flat-team case and current mechanisms cannot answer.
Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing the
total coordination cost figure from Sub-section 1 and the Sub-section 3 failure mode]`
The rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit the cost figure from the justification sentence.
DO NOT emit the verdict declaration before this line.

After the pressure line, choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  DO produce a coordination investment note for each mechanism in the Sub-section 1 table.
  For each mechanism: name / investment (time, tooling, explicit ownership) / failure signal.
  DO write a re-assessment trigger citing the total cost figure:
    "Revisit when total weekly coordination cost exceeds [X * 1.5] hrs/week
    or when [specific failure signal] occurs more than [N] times in [period]."
  DO NOT proceed to org structure until the investment note is complete.

IF STRUCTURE-WARRANTED:
  DO write a re-assessment trigger naming a concrete threshold.
  The trigger SHOULD cite the total cost figure or a specific headcount / milestone.
  DO NOT write "revisit as the team grows."

DO NOT proceed past VERDICT until pressure line, verdict declaration, branch content,
and re-assessment trigger are all written.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

DO draw an ASCII hierarchy after the inertia phase gate.
DO show at minimum two levels.
DO show committees as distinct labeled nodes -- NOT embedded in one area's subtree.
DO use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

DO produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single Decision Scope column -- Decides and Escalates are SEPARATE REQUIRED columns.
DO annotate each Key Roles entry as `[role name] ([domain type])`. Update ANNOTATION-REGISTER Used-In.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO NOT write "owns the area" or generic ownership phrases.
DO include >= 2 area rows plus a `**Total**` row with sum.

OPERATING RHYTHM TABLE (satisfies CF-09)

DO produce: `Cadence | Frequency | DRI / Owner | Purpose`
DO include >= 3 distinct rows: one ROB, one shiproom or gate meeting, one governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in DRI / Owner where possible.

COMMITTEE CHARTERS (satisfies CF-10)

DO write a charter for EVERY governance meeting in the rhythm table.
DO include all five fields per charter: Purpose, Membership, Decides, Escalates, Quorum.
DO annotate each Membership role as `[role name] ([domain type])` -- >= 2 roles.
  Update ANNOTATION-REGISTER Used-In on first cite.
DO populate Escalates with a named destination.
  The text "everything not listed under Decides" does NOT satisfy CF-10.
  Write: "All matters outside [X listed in Decides] escalate to [named destination]."
DO populate Quorum: `Quorum: [N] of [M] member roles required for binding decisions`
  (N = minimum required; M = total roles in Membership).
  Short form "N roles required" does NOT satisfy CF-10.
DO NOT omit any charter for any rhythm-table governance meeting.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit the ANNOTATION-REGISTER with all Used-In cells populated.
Flag any role with a blank Used-In as `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

MUST appear after charters phase gate. Populate all four categories:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP (satisfies CF-12)

Table: `Trigger | Structural Change | Type`
Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH (satisfies CF-13)

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell MUST open with: `[element name] (cat-N) -- [one sentence]`
DO include >= 2 rows.

---

SECTION ORDER:
1. Adversarial burden statement
2. PRE-FLIGHT CONTRACT
3. ROLES-LOADED or ROLES-NOTE (CF-01)
4. ROLE-TYPE-CLASSIFICATION (CF-02)
5. ANNOTATION-REGISTER (initial -- Used-In blank)
6. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7. Inertia: Case for Staying Flat [4-col table + total cost + FLAT-CASE-CLOSED] (CF-03)
8. Inertia: How We Coordinate Today (CF-04)
9. Inertia: Rebuttal (CF-05)
10. Inertia: VERDICT [cost-anchored FLAT-CASE-PRESSURE + branch + trigger] (CF-06)
11. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
12. ASCII Org Diagram (CF-07)
13. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
14. Headcount by Area (CF-08)
15. Operating Rhythm Table (CF-09)
16. Committee Charters (CF-10)
17. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
18. ANNOTATION-REGISTER RECONCILIATION
19. ORG-ELEMENT REGISTER (CF-11)
20. Org Evolution Roadmap (CF-12)
21. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Prose Charter Format

**axis:** output format -- structured prose paragraphs instead of field:value table rows
**hypothesis:** Charter content in prose paragraphs forces the model to integrate the five
required fields into coherent reasoning rather than slot values into a template row.
The key C-03 compliance risk is the N-of-M Quorum fraction: if it disappears in a prose
context, it indicates the table format is structurally necessary to preserve the fraction.
Falsifiable: any charter missing a required field or using short-form Quorum ("N roles required")
fails C-03.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Every structural element must earn its place by naming the specific coordination failure it prevents.
Commit to this posture before loading roles or drawing anything.

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all other types third |
| CF-03 | Inertia: Case for Staying Flat -- mechanism table >= 2 rows + FLAT-CASE-CLOSED separator |
| CF-04 | Inertia: How We Coordinate Today -- distinct content |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating) + declaration + re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: 5 fields in prose; Quorum as N-of-M fraction; Escalates names specific destination with affirmative scope clause |
| CF-11 | ORG-ELEMENT REGISTER with 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

DO check `.roles/` before writing anything.
Produce `ROLES-LOADED:` with one entry per role: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:`.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, remaining types third.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.

ANNOTATION-REGISTER

Produce immediately after classification:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role] | [type] | [to be filled on first downstream cite] |

Fill Used-In when each role first appears downstream. Reconcile after the charters phase gate.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

Produce a three-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants`
Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Include >= 2 data rows. Add rows if < 2.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns with frequency and participants.
DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

Name one specific observable coordination failure.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification]`
Rating: exactly one of `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  Produce a coordination investment note for each Sub-section 1 mechanism:
  name / investment (time, tooling, explicit ownership) / failure signal.
  Write a re-assessment trigger with a concrete threshold. Do not proceed to structure.

IF STRUCTURE-WARRANTED:
  Write a re-assessment trigger with a concrete threshold.
  DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

Draw ASCII hierarchy >= 2 levels. Committees as distinct labeled nodes -- NOT in one area's subtree.
Use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT merge Decides and Escalates.
Annotate Key Roles as `[role name] ([domain type])`. Update ANNOTATION-REGISTER Used-In.
Include >= 2 area rows plus `**Total**` row.

OPERATING RHYTHM TABLE (satisfies CF-09)

Produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include >= 3 distinct rows: ROB, shiproom/gate, governance.

COMMITTEE CHARTERS -- PROSE FORMAT (satisfies CF-10)

DO write a charter for EVERY governance meeting in the rhythm table.

Each charter MUST be written as structured prose with BOLD FIELD LABELS -- not a table.
Use the following paragraph format for each charter:

**[Committee Name]**

**Purpose:** [One or two sentences describing the committee's decision-making scope and why it exists.]

**Membership:** [A sentence listing each role in the format `[role name] ([domain type])`. List >= 2 roles.
Update ANNOTATION-REGISTER Used-In on first cite for each role.]

**Decides:** [A sentence describing the specific decision types this committee owns outright.]

**Escalates:** [A sentence naming the decision types this committee refers elsewhere AND the named
destination. Write: "All matters outside [X listed in Decides] escalate to [named destination]."
The phrase "everything not listed under Decides" does NOT satisfy CF-10.]

**Quorum:** Quorum: [N] of [M] member roles required for binding decisions.
[N = minimum required; M = total roles in the Membership sentence above.]
The short form "N roles required" does NOT satisfy CF-10. The N-of-M fraction is required.

DO NOT omit any field from any charter.
DO NOT omit a charter for any governance meeting in the rhythm table.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit the ANNOTATION-REGISTER with all Used-In cells filled.
Flag any blank Used-In as `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

cat-1 (Areas): `- [area name] -- headcount: [N]`
cat-2 (Committees/Cadences): `- [name]`
cat-3 (Headcount): `- Total headcount: [N]`
cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP (satisfies CF-12)

Table: `Trigger | Structural Change | Type`
Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone.

ANTI-PATTERN WATCH (satisfies CF-13)

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`
Include >= 2 rows.

---

SECTION ORDER: Adversarial statement / PRE-FLIGHT CONTRACT / ROLES-LOADED / ROLE-TYPE-CLASSIFICATION / ANNOTATION-REGISTER / PHASE GATE (ROLES) / Inertia / PHASE GATE (INERTIA) / ASCII Org / PHASE GATE (STRUCTURE) / Headcount / Rhythm / Charters (prose) / PHASE GATE (CHARTERS) / ANNOTATION-REGISTER RECONCILIATION / ORG-ELEMENT REGISTER / Org Evolution Roadmap / Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Self-Check Phrasing Register

**axis:** phrasing register -- interrogative self-check gates replace DO/DO NOT imperatives
**hypothesis:** Question-driven "Confirm before proceeding: ..." gates maintain structural
compliance through internal consistency rather than external constraint. The model must answer
each gate question affirmatively before writing the next section. If rubric criteria pass with
equal reliability under interrogative framing, the phrasing register is not structurally
load-bearing. Falsifiable: any section that skips its gate question or produces content
that does not satisfy the gate condition fails the test.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Before loading roles or drawing diagrams, ask: "Has this team actually encountered a coordination
failure that informal mechanisms cannot solve?" If the answer is unclear, the flat case wins.
Every structural element must earn its place by naming the specific failure it prevents.

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all other types third |
| CF-03 | Inertia: Case for Staying Flat -- mechanism table >= 2 rows + FLAT-CASE-CLOSED separator |
| CF-04 | Inertia: How We Coordinate Today -- distinct content, named frequency and participants |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating) + declaration + re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: 5 fields; Quorum as N-of-M fraction; Escalates names specific destination |
| CF-11 | ORG-ELEMENT REGISTER with 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

Check `.roles/` before writing anything.
Produce `ROLES-LOADED:`: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:`.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, remaining types third.
Complete each tier before beginning the next.

**Gate before ROLE-TYPE-CLASSIFICATION:**
Confirm: "Have I listed every role from .roles/, or stated that no files were found?"
If not: add missing roles before continuing.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.

**Gate before ANNOTATION-REGISTER:**
Confirm: "Does every role in ROLES-LOADED have exactly one type assigned?"
If not: assign missing types before continuing.

ANNOTATION-REGISTER

Produce immediately after classification:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role] | [type] | [to be filled on first downstream cite] |

**Gate before emitting phase gate:**
Confirm: "Does ANNOTATION-REGISTER have one row per role from ROLE-TYPE-CLASSIFICATION?"
If not: add missing rows.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

Produce a three-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants`
Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Include >= 2 data rows.

**Gate before FLAT-CASE-CLOSED separator:**
Confirm: "Do I have at least 2 data rows? Does each Type cell use only the closed vocabulary?"
If not: add rows or correct Type values.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

**Gate before writing:**
Confirm: "Does this sub-section contain content not already present in the Sub-section 1 table?"
If not: write distinct content before proceeding.

Inventory coordination patterns with frequency and participants.

Sub-section 3 -- Rebuttal

**Gate before writing:**
Confirm: "Will the Rebuttal name a specific observable -- blocked decision, missed SLA,
time-zone gap, knowledge silo, or competing roadmap -- not just 'the team is growing'?"
If the answer would be no: identify a specific failure first.

Name one specific observable coordination failure.

Sub-section 4 -- VERDICT

**Gate before writing VERDICT:**
Confirm: "Have I completed all three sub-sections including the FLAT-CASE-CLOSED separator?"
If not: complete the missing sub-sections.

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification]`
Rating: exactly one of `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  Produce a coordination investment note for each Sub-section 1 mechanism:
  name / investment (time, tooling, explicit ownership) / failure signal.
  **Gate:** Confirm: "Does every Sub-section 1 mechanism have a corresponding investment note entry?"
  Write a re-assessment trigger with a concrete threshold.
  Do not proceed to org structure.

IF STRUCTURE-WARRANTED:
  Write a re-assessment trigger with a concrete threshold.
  **Gate:** Confirm: "Is the trigger concrete (a number, a frequency, a named event)?
  If it reads 'revisit as the team grows,' revise it."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

**Gate before drawing:**
Confirm: "Will I draw committees as distinct labeled nodes -- not embedded in one area's subtree?"
Confirm: "Will I use only role names from ROLES-LOADED or ROLES-NOTE -- no invented names?"
If no to either: correct the approach before drawing.

Draw ASCII hierarchy >= 2 levels. Committees as distinct labeled nodes.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

**Gate before writing:**
Confirm: "Does my headcount table have BOTH a Decides column AND a separate Escalates column?"
If not: plan separate columns before writing.

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
Annotate Key Roles as `[role name] ([domain type])`. Update ANNOTATION-REGISTER Used-In.
Include >= 2 area rows plus `**Total**` row.

OPERATING RHYTHM TABLE (satisfies CF-09)

**Gate before writing:**
Confirm: "Do I have at least 3 distinct rows -- one ROB, one shiproom/gate, one governance?"
If not: identify the missing meeting type.

Produce: `Cadence | Frequency | DRI / Owner | Purpose`

COMMITTEE CHARTERS (satisfies CF-10)

**Gate before writing any charter:**
Confirm: "Will every governance meeting in the rhythm table get a charter?"
Confirm: "Will each charter include all 5 fields: Purpose, Membership, Decides, Escalates, Quorum?"
Confirm: "Will Quorum use the N-of-M fraction -- not the short form 'N roles required'?"
Confirm: "Will Escalates name a specific destination with an affirmative scope clause?"
If no to any: plan the charter content before writing.

Write a charter for EVERY governance meeting in the rhythm table.
Membership: >= 2 roles annotated as `[role name] ([domain type])`. Update ANNOTATION-REGISTER.
Escalates: write "All matters outside [X in Decides] escalate to [named destination]."
  "Everything not listed under Decides" does NOT satisfy CF-10.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

**Gate after all charters:**
Confirm: "Does every charter have all 5 fields? Does every Quorum use N-of-M?
Does every Escalates name a specific destination with an affirmative scope clause?"
If not: revise before proceeding.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

**Gate:**
Confirm: "Does every role have a non-blank Used-In entry?"
If not: fill missing entries or flag as PROPAGATION-GAP.

Re-emit the ANNOTATION-REGISTER with all Used-In cells filled.
Flag any blank Used-In as `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

**Gate:** Confirm all four categories are populated before proceeding.
cat-1 (Areas): `- [area name] -- headcount: [N]`
cat-2 (Committees/Cadences): `- [name]`
cat-3 (Headcount): `- Total headcount: [N]`
cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP (satisfies CF-12)

Table: `Trigger | Structural Change | Type`
Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone.
**Gate:** Confirm Row 1 and Row 2 come from different trigger categories.

ANTI-PATTERN WATCH (satisfies CF-13)

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`
Include >= 2 rows.
**Gate:** Confirm every "Why It Applies Here" cell uses the `(cat-N)` typed citation syntax.

---

SECTION ORDER: Adversarial statement / PRE-FLIGHT CONTRACT / ROLES-LOADED / ROLE-TYPE-CLASSIFICATION / ANNOTATION-REGISTER / PHASE GATE (ROLES) / Inertia / PHASE GATE (INERTIA) / ASCII Org / PHASE GATE (STRUCTURE) / Headcount / Rhythm / Charters / PHASE GATE (CHARTERS) / ANNOTATION-REGISTER RECONCILIATION / ORG-ELEMENT REGISTER / Org Evolution Roadmap / Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Eager-Inline Annotation Register

**axis:** role sequence -- annotation register updated eagerly at each use site
**hypothesis:** Forward-declaring the ANNOTATION-REGISTER and reconciling at the end creates
a two-pass process where the reconciliation step may produce generic "used in headcount" entries
rather than precise section citations. An eager-inline approach -- where the model emits a
register update immediately when it writes each role citation -- eliminates the deferred
reconciliation and creates a running register that reflects the actual propagation path.
Falsifiable: if roles appear in downstream sections without corresponding inline register updates,
eager inline cannot be enforced through prompt design alone.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Every structural element must earn its place by naming the specific coordination failure it prevents.
Commit to this posture before loading roles or drawing anything.

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all other types third |
| CF-03 | Inertia: Case for Staying Flat -- mechanism table >= 2 rows + FLAT-CASE-CLOSED separator |
| CF-04 | Inertia: How We Coordinate Today -- distinct content |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating) + declaration + re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: 5 fields; Quorum as N-of-M fraction; Escalates names specific destination |
| CF-11 | ORG-ELEMENT REGISTER with 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

Check `.roles/` before writing anything.
Produce `ROLES-LOADED:`: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:`.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, remaining types third.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.

ANNOTATION-REGISTER -- LIVE TABLE

Produce immediately after classification:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | (pending) |

**EAGER UPDATE RULE:**
Every time you write a role citation in a downstream section (Key Roles in headcount,
or Membership in a charter), you MUST immediately emit an inline register update in
this exact format -- on its own line, BEFORE the next sentence:

`>>> REGISTER UPDATE: [role name] -- Used In: [section name / area or committee] <<<`

DO NOT batch updates at the end.
DO NOT defer to a reconciliation step.
Emit the update at the exact point of first citation.

After all sections are written, emit a REGISTER CLOSURE block:
Re-emit the ANNOTATION-REGISTER table with Used-In cells populated from the inline update
entries. The cells must match the inline updates exactly.
Flag any role still showing "(pending)" as `PROPAGATION-GAP: [role name]`.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

Produce a three-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants`
Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Include >= 2 data rows. Add rows if < 2.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns with frequency and participants. Do not duplicate Sub-section 1.

Sub-section 3 -- Rebuttal

Name one specific observable coordination failure. Do not write "the team is growing" without
specifying the failure mode.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification]`
Rating: exactly one of `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  Produce coordination investment note for each Sub-section 1 mechanism:
  name / investment (time, tooling, explicit ownership) / failure signal.
  Write re-assessment trigger with concrete threshold. Do not proceed to structure.

IF STRUCTURE-WARRANTED:
  Write re-assessment trigger with concrete threshold. DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

Draw ASCII hierarchy >= 2 levels. Committees as distinct labeled nodes.
Use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT merge Decides and Escalates.
Annotate Key Roles as `[role name] ([domain type])`.
For EACH role cited in Key Roles, emit an inline register update IMMEDIATELY:
  `>>> REGISTER UPDATE: [role name] -- Used In: Headcount / [Area Name] <<<`
Include >= 2 area rows plus `**Total**` row.
Decides: decision types owned at this level.
Escalates: decision types referred upward, naming destination. DO NOT write "owns the area."

OPERATING RHYTHM TABLE (satisfies CF-09)

Produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include >= 3 distinct rows: ROB, shiproom/gate, governance.

COMMITTEE CHARTERS (satisfies CF-10)

Write a charter for EVERY governance meeting in the rhythm table.
Include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
Membership: annotate each role as `[role name] ([domain type])`, >= 2 roles.
  For EACH role cited in Membership, emit an inline register update IMMEDIATELY:
  `>>> REGISTER UPDATE: [role name] -- Used In: [Committee Name] / Membership <<<`
Escalates: name a specific destination.
  Write: "All matters outside [X in Decides] escalate to [named destination]."
  "Everything not listed under Decides" does NOT satisfy CF-10.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.
  Short form "N roles required" does NOT satisfy CF-10.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

REGISTER CLOSURE

Re-emit the ANNOTATION-REGISTER with Used-In cells from inline update entries.
Cells must match inline updates exactly.
Flag any "(pending)" entry as `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

cat-1 (Areas): `- [area name] -- headcount: [N]`
cat-2 (Committees/Cadences): `- [name]`
cat-3 (Headcount): `- Total headcount: [N]`
cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP (satisfies CF-12)

Table: `Trigger | Structural Change | Type`
Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone event.

ANTI-PATTERN WATCH (satisfies CF-13)

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`
Include >= 2 rows.

---

SECTION ORDER: Adversarial statement / PRE-FLIGHT CONTRACT / ROLES-LOADED / ROLE-TYPE-CLASSIFICATION / ANNOTATION-REGISTER (live, pending) / PHASE GATE (ROLES) / Inertia / PHASE GATE (INERTIA) / ASCII Org / PHASE GATE (STRUCTURE) / Headcount [inline updates] / Rhythm / Charters [inline updates] / PHASE GATE (CHARTERS) / REGISTER CLOSURE / ORG-ELEMENT REGISTER / Org Evolution Roadmap / Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Combined: Quantified Inertia + Eager-Inline Register

**axis:** combination -- V-01 coordination-cost metric + V-04 eager-inline annotation register
**hypothesis:** Both axes are front-loading patterns: the cost metric forces precision in the
inertia steelman at the time of production; the eager register forces role propagation accuracy
at the time of each citation. Combining them tests whether the two mechanisms compound.
If V-05 surfaces a pattern not present in V-01 or V-04 individually, the combination creates
a new excellence signal. Falsifiable: if V-05 scores identically to V-01 or V-04 on all criteria,
combination adds no marginal value.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Every structural element must earn its place by naming the specific coordination failure it prevents.
Before loading roles or drawing diagrams, commit to this posture. The question is not
"how should we organize?" but "does the coordination cost of staying flat exceed the
coordination cost of the proposed structure?"

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all other types third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost) >= 2 rows + FLAT-CASE-CLOSED separator with total cost |
| CF-04 | Inertia: How We Coordinate Today -- distinct content |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (cost-anchored rating) + declaration + cost-grounded re-assessment trigger |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: 5 fields; Quorum as N-of-M fraction; Escalates names specific destination with affirmative scope clause |
| CF-11 | ORG-ELEMENT REGISTER with 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

Check `.roles/` before writing anything.
Produce `ROLES-LOADED:`: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .roles/ files found. Using inferred roles:`.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, remaining types third.
Complete each tier before starting the next.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.
Every role from ROLES-LOADED must appear.

ANNOTATION-REGISTER -- LIVE TABLE (eager update mode)

Produce immediately after classification:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | (pending) |

**EAGER UPDATE RULE:** Every time you cite a role in a downstream section (Key Roles or Membership),
emit an inline register update immediately -- on its own line, before the next sentence:
`>>> REGISTER UPDATE: [role name] -- Used In: [section / area or committee name] <<<`
Do not batch updates. Do not defer to end. Emit at first cite per section.

After Anti-Pattern Watch, emit REGISTER CLOSURE: re-emit the table with Used-In cells
populated from inline updates. Flag any "(pending)" entry as `PROPAGATION-GAP: [role name]`.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

Produce a FOUR-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`

Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Include >= 2 data rows.
Coordination Cost: a time estimate per occurrence (e.g., "2 hrs/week, 5 people").
DO NOT leave any Coordination Cost cell blank.

After the table:
- Count data rows. Add rows if < 2.
- Sum the weekly costs into a TOTAL COORDINATION COST figure.
- Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {X} hrs/week across {Y} people. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns with frequency and participants.
DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

Name one specific observable coordination failure the flat case cannot answer.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing the total
coordination cost figure from Sub-section 1 and the Sub-section 3 failure mode]`
Rating: exactly one of `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit the cost figure from the justification.

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  Produce coordination investment note for each Sub-section 1 mechanism:
  name / investment (time, tooling, explicit ownership) / failure signal.
  Write re-assessment trigger citing the total cost figure:
    "Revisit when total weekly coordination cost exceeds [X * 1.5] hrs/week
    or when [specific failure signal] occurs more than [N] times in [period]."
  Do not proceed to structure until investment note is complete.

IF STRUCTURE-WARRANTED:
  Write re-assessment trigger citing the cost figure or naming a concrete threshold.
  DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

Draw ASCII hierarchy >= 2 levels. Committees as distinct labeled nodes -- NOT in one area's subtree.
Use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT merge Decides and Escalates.
Annotate Key Roles as `[role name] ([domain type])`.
For EACH role cited in Key Roles, emit inline immediately:
  `>>> REGISTER UPDATE: [role name] -- Used In: Headcount / [Area Name] <<<`
Include >= 2 area rows plus `**Total**` row.
Decides: decision types owned at this level.
Escalates: decision types referred upward, naming destination role or forum.
DO NOT write "owns the area."

OPERATING RHYTHM TABLE (satisfies CF-09)

Produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include >= 3 distinct rows: ROB, shiproom/gate, governance.
Reference a role from ROLES-LOADED in DRI / Owner where possible.

COMMITTEE CHARTERS (satisfies CF-10)

Write a charter for EVERY governance meeting in the rhythm table.
Include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
Membership: annotate each role as `[role name] ([domain type])`, >= 2 roles.
  For EACH role cited in Membership, emit inline immediately:
  `>>> REGISTER UPDATE: [role name] -- Used In: [Committee Name] / Membership <<<`
Escalates: name a specific destination.
  Write: "All matters outside [X in Decides] escalate to [named destination]."
  "Everything not listed under Decides" does NOT satisfy CF-10.
Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.
  Short form "N roles required" does NOT satisfy CF-10.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

REGISTER CLOSURE

Re-emit the ANNOTATION-REGISTER with Used-In cells from inline update entries.
Cells must match inline updates exactly.
Flag any "(pending)" entry as `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

cat-1 (Areas): `- [area name] -- headcount: [N]`
cat-2 (Committees/Cadences): `- [name]`
cat-3 (Headcount): `- Total headcount: [N]`
cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP (satisfies CF-12)

Table: `Trigger | Structural Change | Type`
Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH (satisfies CF-13)

Table: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`
Include >= 2 rows.

---

SECTION ORDER:
1. Adversarial burden statement (before PRE-FLIGHT CONTRACT and all mechanics)
2. PRE-FLIGHT CONTRACT (CF-01 through CF-13)
3. ROLES-LOADED or ROLES-NOTE (CF-01)
4. ROLE-TYPE-CLASSIFICATION (CF-02)
5. ANNOTATION-REGISTER live table -- all Used-In cells "(pending)"
6. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7. Inertia: Case for Staying Flat [4-col + total cost + FLAT-CASE-CLOSED] (CF-03)
8. Inertia: How We Coordinate Today (CF-04)
9. Inertia: Rebuttal (CF-05)
10. Inertia: VERDICT [cost-anchored FLAT-CASE-PRESSURE + branch + trigger] (CF-06)
11. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
12. ASCII Org Diagram (CF-07)
13. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
14. Headcount by Area [inline REGISTER UPDATE per role] (CF-08)
15. Operating Rhythm Table (CF-09)
16. Committee Charters [inline REGISTER UPDATE per role] (CF-10)
17. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
18. REGISTER CLOSURE
19. ORG-ELEMENT REGISTER (CF-11)
20. Org Evolution Roadmap (CF-12)
21. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
