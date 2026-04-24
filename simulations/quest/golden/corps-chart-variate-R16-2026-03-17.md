---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 16
rubric: simulations/quest/rubrics/corps-chart-rubric-v15-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 16)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R16 targets the two new criteria added in v15 of the rubric:

- **C-39 -- HALT-AND-CONFIRM block carries explicit sole-instruction-site annotation for each
  governed enforcement requirement**:
  C-33 prohibits the checklist-strict/prose-advisory split but places no constraint against a
  subsequent revision introducing advisory language at a new instruction site. C-39 closes the
  future-drift version of the same failure mode. The sole-instruction annotation
  (`[sole instruction site for ...]`) embedded within each HALT block declares it as exclusive
  authority for each governed enforcement requirement. Contamination becomes a detectable
  protocol violation at prompt-structure level rather than a silent drift requiring scored output
  to surface.

- **C-40 -- REGISTER-CONSISTENCY AUDIT block embedded at each phase gate before advancing**:
  C-33 + C-39 achieve register consistency at declaration time but provide no mechanism for
  detecting contamination introduced in section-producing steps between gates. The per-gate
  REGISTER-CONSISTENCY AUDIT requires the model to explicitly confirm register consistency for
  all active governed requirements at each gate boundary, surfacing contamination at the gate
  where it is introduced rather than in later scored output.

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | Sole-instruction-site annotations in HALT blocks (single axis: C-39) | C-39 | R15 V-01 achieves C-33 passively -- no advisory contamination present -- but the HALT blocks carry no architectural declaration of exclusivity. A subsequent revision could add advisory language at a new instruction site without violating any declared constraint. V-01 adds `[sole instruction site for ...]` annotations inside both HALT blocks: the ROLE-NAME LOCK HALT declares itself exclusive authority for the lock-accuracy requirements; the Rebuttal HALT declares itself exclusive authority for the four-field form-order requirement. Built on R15 V-01 base (no FORMAT CONTRACT; HALT-AND-CONFIRM at ROLE-NAME LOCK and Rebuttal; per-row vocabulary; per-cell directives at sites 2+5; per-name note at site 3). C-40 not applied. Isolates C-39 contribution. |
| V-02 | REGISTER-CONSISTENCY AUDIT at all 5 phase gates (single axis: C-40) | C-40 | R15 V-02 has HALT-AND-CONFIRM with C-33 sole-instruction architecture and C-35 schema citations. Contamination introduced in section-producing steps between gates is not caught until scored output. V-02 adds a REGISTER-CONSISTENCY AUDIT block before each of the 5 phase gate markers, requiring explicit confirmation that all active governed requirements used mandatory-register language before the gate fires. Built on R15 V-02 base (FORMAT CONTRACT + DISQUALIFY-IF + C-38 non-FC HALT headers + C-35 schema citations + HALT-AND-CONFIRM + C-33 DRI/Owner consolidation + per-row vocabulary + per-role-name charter). No C-36/C-37 per-cell/per-name notes in ROLE-NAME LOCK block. C-39 not applied. Isolates C-40 contribution. |
| V-03 | Sole-instruction-site annotations in STOP blocks (single axis: C-39, on R15 V-03 base that already satisfies C-40) | C-39, C-40 | R15 V-03 (the source of C-40) has REGISTER-CONSISTENCY AUDIT at all 5 gates but the STOP blocks preceding ROLE-NAME LOCK and Rebuttal carry no sole-instruction-site declarations (C-39 gap). V-03 adds `[sole instruction site for ...]` annotations inside both STOP blocks. Tests C-39 on the STOP/phase-gate-audit architecture: STOP blocks become both gate mechanisms and architectural constraint documents. Built on R15 V-03 base (no FORMAT CONTRACT; STOP/phase-gate-audit; per-cell notes at sites 2+5; per-name note at site 3; REGISTER-CONSISTENCY AUDIT at all 5 gates). |
| V-04 | C-39 + C-40 combined on R15 V-04 base | C-39, C-40, all prior through C-38 | R15 V-04 carries C-20 through C-38. Two gaps remain: (a) HALT blocks carry no sole-instruction-site annotations (C-39 gap); (b) no REGISTER-CONSISTENCY AUDIT at phase gates (C-40 gap). V-04 closes both: embeds sole-instruction-site annotations inside every HALT block for each governed requirement; adds REGISTER-CONSISTENCY AUDIT at all 5 phase gates adapted to the R15 V-04 FORMAT CONTRACT + C-33/C-34 + C-36/C-37/C-38 architecture. |
| V-05 | Full integration: C-39 + C-40 on R15 V-05 base -- all 40 criteria | C-39, C-40, C-01 through C-38 | Maximum mechanical stack. R15 V-05 carries all 38 criteria. The C-33 sole-instruction note for DRI/Owner in STEP 7 is positioned as bracketed prose after the Proceed line -- outside the HALT block. C-39 requires it inside. R16 V-05 moves the DRI/Owner sole-instruction annotation inside the HALT checklist; adds sole-instruction-site annotations to all remaining HALT blocks for each governed requirement; adds REGISTER-CONSISTENCY AUDIT at all 5 phase gates. Targeting all 40 criteria. |

---

## V-01 -- Sole-Instruction-Site Annotations in HALT Blocks (single axis: C-39)

**Axis**: HALT blocks embed sole-instruction-site annotations for governed requirements
**Hypothesis**: R15 V-01 passes C-33 passively (no advisory contamination present) but declares
no architectural exclusivity. V-01 adds `[sole instruction site for ...]` inside both HALT blocks.
The ROLE-NAME LOCK HALT declares itself as exclusive authority for the no-novel-role and
lock-count-exactness requirements. The Rebuttal HALT declares itself as exclusive authority for
the four-field form-order requirement. Built on R15 V-01 base: no FORMAT CONTRACT; HALT-AND-CONFIRM
at ROLE-NAME LOCK and Rebuttal; per-cell directives at sites 2 and 5; per-name note at site 3;
per-row vocabulary; five-site CHECK enumeration. C-40 not applied -- no REGISTER-CONSISTENCY AUDIT
blocks at phase gates. Isolates C-39 contribution.

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
  [sole instruction site for lock-enumeration accuracy requirements:
   (a) the lock list must contain exactly the count of roles from ROLES-LOADED -- no more, no fewer;
   (b) every role in the lock list must appear verbatim in ROLES-LOADED;
   (c) no role may be invented here that is absent from ROLES-LOADED.
   No other location in this prompt introduces competing language for requirements (a), (b), or (c).]
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
  [sole instruction site for Rebuttal four-field form-order requirement: the four fields must
   appear in this exact sequence -- ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING
   MECHANISMS FAIL / RE-ASSESSMENT TRIGGER. No other location in this prompt names the Rebuttal
   field sequence. A Rebuttal produced without consulting this HALT block violates the
   sole-instruction-site constraint declared here.]
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
3.  [HALT -- sole-instruction-site annotations for lock-accuracy requirements (a)(b)(c) --
     4-item count-and-match checklist] ROLE-NAME LOCK
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
    [HALT -- sole-instruction-site annotation for Rebuttal four-field form-order --
     4-item field checklist] /
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

## V-02 -- REGISTER-CONSISTENCY AUDIT at All 5 Phase Gates (single axis: C-40)

**Axis**: REGISTER-CONSISTENCY AUDIT block embedded before each phase gate
**Hypothesis**: R15 V-02 has HALT-AND-CONFIRM with C-33 sole-instruction architecture, C-35
schema citations in FC HALT headers, and C-38 non-FC HALT header recall. Contamination
introduced in section-producing steps between gates is not surfaced until scored output. V-02
adds a REGISTER-CONSISTENCY AUDIT block before each of the 5 phase gate markers. Each audit
enumerates the governed requirements active at that gate boundary and requires explicit
confirmation that mandatory-register language was used at every instruction site for those
requirements. Built on R15 V-02 base: FORMAT CONTRACT with DISQUALIFY-IF (C-20, C-23); C-35
schema citations in all FC HALT headers; C-38 non-FC HALT header recall (ROLE-NAME LOCK and
Rebuttal); HALT-AND-CONFIRM at all BEFORE-PRODUCE sites (C-31); per-row vocabulary (C-32);
per-role-name charter at PRODUCE site (C-30); single-site DRI/Owner consolidation (C-33).
No C-36/C-37 per-cell/per-name notes in ROLE-NAME LOCK block. C-39 not applied. Isolates C-40.

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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 1:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] ROLES-LOADED block: used mandatory DO-produce listing language -- no advisory qualifier present.
  [ ] ROLE-TYPE-CLASSIFICATION: used mandatory classification language (every loaded role must appear) -- no hedging.
  [ ] ROLE-NAME LOCK declaration: used mandatory "no role name may appear" exclusion language -- no "where possible" or "try to" qualifier.
  [ ] ROLE-NAME LOCK five-site enumeration: labeled all five sites as "mandatory" -- no advisory softening present.
If any advisory qualifier was introduced at any of the above instruction sites, correct before continuing.
DO NOT emit the phase gate until all four confirmed.

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

VERIFY: A Rebuttal where OBSERVABLE BREAKDOWN begins with "As we scale..." does not satisfy this step.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Rating: `Strong / Moderate / Weak / Negligible / Insufficient`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 2:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] Mechanism-Type VOCABULARY block: used mandatory "No row may use a Type value outside this list" language -- no conditional qualifier.
  [ ] Per-row vocabulary check instruction: used mandatory "verify the Type value appears...before writing the next row" language -- no "where possible" softening.
  [ ] REBUTTAL FORM CHECK [SITE 4]: used mandatory "must name exactly one role from the ROLE-NAME LOCK list" language -- no conditional qualifier.
  [ ] VERDICT FLAT-CASE-PRESSURE rating: drawn from the closed set (Strong / Moderate / Weak / Negligible / Insufficient) -- no open-ended rating introduced.
If any advisory qualifier was introduced at any of the above instruction sites, correct before continuing.
DO NOT emit the phase gate until all four confirmed.

`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name in this diagram must appear in the ROLE-NAME LOCK list.
Verify before placing each node. Draw ASCII hierarchy (minimum two levels). Printable ASCII only.
Committees as distinct labeled nodes.

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 3:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] ASCII diagram CHECK [SITE 1]: used mandatory "must appear in the ROLE-NAME LOCK list" language -- no "where possible" qualifier.
  [ ] Per-node verification instruction: used mandatory "Verify before placing each node" language -- no "try to verify" softening.
If any advisory qualifier was introduced at the diagram CHECK instruction site, correct before continuing.
DO NOT emit the phase gate until both confirmed.

`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 4:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] Schema (1) HALT checklist item 2 (Decides/Escalates): used mandatory DISQUALIFY-IF language -- no conditional qualifier.
  [ ] Schema (1) HALT checklist item 3 (Key Roles): used mandatory "every value must be a role from ROLE-NAME LOCK" language -- no "where possible" softening.
  [ ] Schema (2) HALT checklist item 3 (DRI/Owner): used mandatory "every cell value must be a role from the ROLE-NAME LOCK list" language -- this is the sole instruction site; no competing language at any other site.
  [ ] Schema (3) HALT checklist item 5 (Quorum fraction form): used mandatory "[N] of [M] member roles required" language -- no short-form present.
  [ ] Schema (3) HALT checklist item 6 (DISQUALIFY-IF Quorum): used mandatory DISQUALIFY-IF language -- no advisory qualifier.
  [ ] Charter per-role-name Membership directive: used mandatory "verify the name appears...before appending the next name" language -- no "try to verify" softening.
  [ ] Charter per-role-name Decides directive: same mandatory language -- no advisory qualifier.
If any advisory qualifier was introduced at any of these instruction sites, correct before continuing.
DO NOT emit the phase gate until all seven confirmed.

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
and verify after. An out-of-vocabulary Type or consecutive repeat at any row position is a violation.

VERIFY: Two rows both typed "headcount threshold" do not satisfy this step.

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 5:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] TRIGGER-TYPE VOCABULARY block: used mandatory "No two consecutive rows may share the same Type value" language -- no "try to avoid" qualifier.
  [ ] Per-row vocabulary check instruction: used mandatory "verify the Type value appears...and does not repeat...before writing the next row" language -- no "where possible" softening.
If any advisory qualifier was introduced at either of these instruction sites, correct before continuing.
DO NOT emit the phase gate until both confirmed.

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
For each row: verify the "Why It Applies Here" cell opens with [element name] (cat-N) -- before
writing the next row. Do not complete the table and verify after.

VERIFY: A "Why It Applies Here" cell naming an org element without the `(cat-N)` typed prefix
does not satisfy the citation requirement for that row.

SECTION ORDER -- 11 STEPS, 5 PHASE GATES

1.  UPFRONT FORMAT CONTRACT (DISQUALIFY-IF on schemas 1, 3, 5)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-TYPE-CLASSIFICATION
4.  [HALT. Re-read ROLE-NAME LOCK structure. -- 4-item checklist] ROLE-NAME LOCK (five-site enumeration)
5.  [REGISTER-CONSISTENCY AUDIT: 4-item -- ROLES section] Phase Gate 1
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT. Re-read four-field Rebuttal form. -- 4-item field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY] / VERDICT
7.  [REGISTER-CONSISTENCY AUDIT: 4-item -- INERTIA section] Phase Gate 2
8.  ASCII Org Diagram [CHECK SITE 1]
9.  [REGISTER-CONSISTENCY AUDIT: 2-item -- STRUCTURE section] Phase Gate 3
10. [HALT. Re-read FORMAT CONTRACT schema (1). -- 4-item] Headcount by Area [VERIFY: merged] [CHECK SITE 5]
11. [HALT. Re-read FORMAT CONTRACT schema (2). -- 3-item, sole DRI/Owner site] Operating Rhythm Table
12. [HALT. Re-read FORMAT CONTRACT schema (3). -- 6-item per charter] Committee Charters [CHECK SITE 3] [per-role-name Membership] [per-role-name Decides] [VERIFY: short Quorum]
13. [REGISTER-CONSISTENCY AUDIT: 7-item -- HEADCOUNT/RHYTHM/CHARTERS section] Phase Gate 4
14. [HALT. Re-read FORMAT CONTRACT schema (4). -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
16. [REGISTER-CONSISTENCY AUDIT: 2-item -- ROADMAP section] Phase Gate 5
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5). -- 5-item] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Sole-Instruction-Site Annotations in STOP Blocks (single axis: C-39, on STOP/audit base)

**Axis**: STOP blocks embed sole-instruction-site annotations for governed requirements
**Hypothesis**: R15 V-03 has REGISTER-CONSISTENCY AUDIT at all 5 gates (the source of C-40) but
the STOP blocks preceding ROLE-NAME LOCK and Rebuttal carry no sole-instruction-site declarations
(C-39 gap). V-03 adds `[sole instruction site for ...]` annotations inside both STOP blocks.
Tests whether C-39 is compatible with the STOP/phase-gate-audit architecture: the STOP blocks
become both gate mechanisms and sole-instruction-site declaration documents. The phase-gate audits
already require explicit confirmation of register consistency; the C-39 annotation makes the
exclusivity declaration structural at the STOP block itself. Built on R15 V-03 base: no FORMAT
CONTRACT; STOP/phase-gate-audit architecture; per-cell notes at sites 2 and 5; per-name note
at site 3 with anti-drift prohibition; REGISTER-CONSISTENCY AUDIT at all 5 gates.

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
  [sole instruction site for lock-enumeration accuracy requirements:
   (a) the lock list must contain exactly the count of roles from ROLES-LOADED -- no more, no fewer;
   (b) every role in the lock list must appear verbatim in ROLES-LOADED;
   (c) no role may be invented here that is absent from ROLES-LOADED.
   No other location in this prompt introduces competing language for requirements (a), (b), or (c).
   A subsequent revision that adds qualifying language for these requirements at any other location
   violates the sole-instruction-site constraint declared in this STOP block.]
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
  [ ] ROLE-TYPE-CLASSIFICATION: used mandatory classification language -- no advisory qualifier.
  [ ] ROLE-NAME LOCK: used mandatory "no role name may appear" language -- no hedging or "where possible" present.
  [ ] ROLE-NAME LOCK per-cell notes (sites 2 and 5): used mandatory procedural language -- no advisory qualifier.
  [ ] ROLE-NAME LOCK per-name note (site 3): used mandatory procedural language with anti-drift prohibition -- no advisory qualifier.
  [ ] ROLE-NAME LOCK STOP block: sole-instruction-site annotation present for requirements (a), (b), (c) -- no competing instruction added elsewhere.
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
  [sole instruction site for Rebuttal four-field form-order requirement: the four fields must
   appear in this exact sequence -- ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING
   MECHANISMS FAIL / RE-ASSESSMENT TRIGGER. No other location in this prompt names the Rebuttal
   field sequence. A Rebuttal produced without consulting this STOP block violates the
   sole-instruction-site constraint declared here.]
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
  [ ] Rebuttal STOP block: sole-instruction-site annotation present for four-field form-order requirement -- no competing instruction added elsewhere.
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
  [ ] Per-node verification instruction: used mandatory "verify before placing the next node" language -- no advisory softening.
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
  [ ] TRIGGER-TYPE VOCABULARY instruction: used mandatory "No two consecutive rows may share" language -- no "where possible" present.
  [ ] Per-row vocabulary check: used mandatory "verify before writing the next row" language -- no advisory softening.
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
3.  [STOP -- sole-instruction-site annotation for requirements (a)(b)(c) -- 4-item count-record checklist] ROLE-NAME LOCK
    (complete role enumeration +
     [DRI/Owner per-cell note adjacent to list] +
     [Key Roles per-cell note adjacent to list] +
     [Membership/Decides per-name note adjacent to list with anti-drift prohibition] +
     five-site enumeration with per-cell at 2 and 5, per-name at 3)
4.  [REGISTER-CONSISTENCY AUDIT: ROLES section -- 6-item including sole-instruction-site check] Phase Gate 1
5.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row Type verify] / table / [VERIFY] /
    [FLAT-CASE-CLOSED] / How We Coordinate Today /
    [STOP -- sole-instruction-site annotation for Rebuttal four-field form-order -- 4-item field checklist] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY: future-tense] / VERDICT
6.  [REGISTER-CONSISTENCY AUDIT: INERTIA section -- 4-item including sole-instruction-site check] Phase Gate 2
7.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify]
8.  [REGISTER-CONSISTENCY AUDIT: STRUCTURE section -- 2-item] Phase Gate 3
9.  Headcount [CHECK SITE 5 -- per-cell; lock-declared directive applies]
10. Operating Rhythm [CHECK SITE 2 -- per-cell; lock-declared directive applies]
11. Committee Charters [CHECK SITE 3 -- per-name; lock-declared directive applies] [VERIFY: short Quorum]
12. [REGISTER-CONSISTENCY AUDIT: HEADCOUNT/RHYTHM/CHARTERS section -- 5-item] Phase Gate 4
13. ORG-ELEMENT REGISTER (all four categories)
14. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
15. [REGISTER-CONSISTENCY AUDIT: ROADMAP section -- 2-item] Phase Gate 5
16. [CAT-N-CITATION-SCHEMA] + [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- C-39 + C-40 Combined on R15 V-04 Base

**Axis**: Sole-instruction-site annotations + REGISTER-CONSISTENCY AUDIT on R15 V-04 base
**Hypothesis**: R15 V-04 carries C-20 through C-38: FORMAT CONTRACT + DISQUALIFY-IF + HALT-AND-CONFIRM
+ C-35 schema citations + C-36 per-cell notes at sites 2+5 + C-37 per-name note at site 3 +
C-38 non-FC HALT header recall + C-33/C-34 procedural directives. Two gaps remain: (a) HALT blocks
carry no sole-instruction-site annotations (C-39 gap); (b) no REGISTER-CONSISTENCY AUDIT at phase
gates (C-40 gap). V-04 closes both. Each HALT block receives `[sole instruction site for ...]`
annotations for its governed requirements; REGISTER-CONSISTENCY AUDIT blocks are added at all
5 phase gates. The audit items are adapted to the R15 V-04 FORMAT CONTRACT + C-33/C-34 + C-36/C-37
architecture, checking requirements at the gate where they become applicable.

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
HALT. Re-read ROLE-NAME LOCK structure: complete role enumeration from ROLES-LOADED / per-cell enforcement notes at sites 2 and 5 / per-name enforcement note at site 3 / no-novel-role constraint at all five sites.
  [sole instruction site for lock-enumeration accuracy requirements:
   (a) lock list must contain exactly the count from ROLES-LOADED -- no more, no fewer;
   (b) every role must appear verbatim in ROLES-LOADED;
   (c) no invented role absent from ROLES-LOADED.
   No other location in this prompt introduces competing language for requirements (a), (b), (c).]
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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 1:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] ROLES-LOADED block: mandatory DO-produce listing language -- no advisory qualifier.
  [ ] ROLE-TYPE-CLASSIFICATION: mandatory "every loaded role must appear" language -- no hedging.
  [ ] ROLE-NAME LOCK declaration: mandatory "no role name may appear" language -- no "where possible".
  [ ] ROLE-NAME LOCK per-cell notes (sites 2 and 5): mandatory per-cell procedural language -- no advisory qualifier.
  [ ] ROLE-NAME LOCK per-name note (site 3): mandatory per-name procedural language with anti-drift prohibition -- no advisory qualifier.
  [ ] ROLE-NAME LOCK HALT block: sole-instruction-site annotation present for requirements (a)(b)(c).
If any advisory qualifier was introduced at any of the above sites, correct before continuing.
DO NOT emit the phase gate until all six confirmed.

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
  [sole instruction site for Rebuttal four-field form-order requirement: the four fields must
   appear in this exact sequence. No other location in this prompt names the field sequence.
   A Rebuttal produced without consulting this HALT block violates the sole-instruction-site
   constraint declared here.]
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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 2:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] Mechanism-Type VOCABULARY: mandatory "No row may use a Type value outside this list" -- no conditional.
  [ ] Per-row vocabulary check: mandatory "verify...before writing the next row" -- no softening.
  [ ] Rebuttal HALT block: sole-instruction-site annotation present for four-field form-order requirement.
  [ ] REBUTTAL FORM CHECK [SITE 4]: mandatory "must name exactly one role" -- no conditional qualifier.
  [ ] VERDICT FLAT-CASE-PRESSURE: drawn from closed set -- no open-ended rating introduced.
If any advisory qualifier was introduced at any governed instruction site, correct before continuing.
DO NOT emit the phase gate until all five confirmed.

`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK
list. For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node
-- do not complete the diagram and verify after. Draw ASCII hierarchy (minimum two levels). Printable
ASCII only. Committees as distinct labeled nodes.

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 3:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] ASCII diagram CHECK [SITE 1]: mandatory "must appear in the ROLE-NAME LOCK list" -- no "where possible".
  [ ] Per-node verification: mandatory "verify...before placing the next node" -- no advisory softening.
If any advisory qualifier was introduced at the diagram CHECK instruction site, correct before continuing.
DO NOT emit the phase gate until both confirmed.

`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  [sole instruction site for Headcount table column-structure and DISQUALIFY-IF requirements:
   five separate columns required; Decides and Escalates must not be merged; Key Roles must use
   roles from ROLE-NAME LOCK. No other location in this prompt introduces competing language
   for these schema (1) requirements.]
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
     [sole instruction site for DRI/Owner role-lock requirement -- no other instruction site in
      this prompt introduces competing language for DRI/Owner role membership]
Proceed only if all three confirmed.

Produce per schema (2) of the FORMAT CONTRACT.
[The HALT checklist item 3 above is the sole instruction site for the DRI/Owner role-lock
requirement, as declared in the annotation on that item. No co-located instruction uses
different language.]

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list before populating the
next row -- do not complete the column and verify after. A novel role name at any DRI/Owner cell
is a violation regardless of row position.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter.
  [sole instruction site for Charter schema requirements: Membership minimum-two-roles,
   Escalates-must-name-destination, Quorum fraction form [N] of [M], and DISQUALIFY-IF for
   Quorum. No other location in this prompt introduces competing language for these requirements.]
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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 4:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] Schema (1) HALT: sole-instruction-site annotation present for column-structure and DISQUALIFY-IF requirements.
  [ ] Schema (1) HALT item 2: mandatory DISQUALIFY-IF language for Decides/Escalates merge -- no conditional.
  [ ] Schema (1) HALT item 3: mandatory "every value must be a role from ROLE-NAME LOCK" for Key Roles -- no softening.
  [ ] Schema (2) HALT item 3: mandatory "every cell value must be a role from the ROLE-NAME LOCK list" -- sole instruction site annotation present.
  [ ] Schema (3) HALT: sole-instruction-site annotation present for Charter schema requirements.
  [ ] Schema (3) HALT item 5: mandatory "[N] of [M] member roles required" language -- no short-form.
  [ ] Schema (3) HALT item 6: mandatory DISQUALIFY-IF language -- no advisory qualifier.
  [ ] Charter per-name Membership directive: mandatory "verify...before adding the next name" -- no advisory softening.
  [ ] Charter per-name Decides directive: same mandatory language -- no advisory softening.
If any advisory qualifier was introduced at any of these instruction sites, correct before continuing.
DO NOT emit the phase gate until all nine confirmed.

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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 5:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] TRIGGER-TYPE VOCABULARY: mandatory "No two consecutive rows may share" -- no "try to avoid".
  [ ] Per-row vocabulary check: mandatory "verify...before writing the next row" -- no softening.
If any advisory qualifier was introduced at either instruction site, correct before continuing.
DO NOT emit the phase gate until both confirmed.

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
  [sole instruction site for Anti-Pattern Watch citation-prefix requirement: every "Why It
   Applies Here" cell must open with [element name] (cat-N) -- and no other instruction site
   in this prompt introduces competing language for this requirement.]
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
4.  [HALT. Re-read ROLE-NAME LOCK structure. sole-instruction-site annotation for (a)(b)(c). -- 4-item checklist]
    ROLE-NAME LOCK (complete enumeration + [DRI/Owner per-cell] + [Key Roles per-cell] + [Membership/Decides per-name] + five-site CHECK)
5.  [REGISTER-CONSISTENCY AUDIT: 6-item -- ROLES section] Phase Gate 1
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT. Re-read four-field Rebuttal form. sole-instruction-site annotation for form-order. -- 4-item] /
    [REBUTTAL FORM: CHECK SITE 4] / [VERIFY] / VERDICT
7.  [REGISTER-CONSISTENCY AUDIT: 5-item -- INERTIA section] Phase Gate 2
8.  ASCII Org Diagram [CHECK SITE 1 -- per-node]
9.  [REGISTER-CONSISTENCY AUDIT: 2-item -- STRUCTURE section] Phase Gate 3
10. [HALT. Re-read FORMAT CONTRACT schema (1). sole-instruction-site annotation. -- 4-item]
    Headcount [VERIFY: merged] [CHECK SITE 5 -- per-cell]
11. [HALT. Re-read FORMAT CONTRACT schema (2). sole-instruction-site annotation on item 3. -- 3-item]
    Operating Rhythm Table [CHECK SITE 2 -- per-cell; no co-located advisory prose]
12. [HALT. Re-read FORMAT CONTRACT schema (3). sole-instruction-site annotation. -- 6-item per charter]
    Committee Charters [CHECK SITE 3 -- per-name] [VERIFY: short Quorum]
13. [REGISTER-CONSISTENCY AUDIT: 9-item -- HEADCOUNT/RHYTHM/CHARTERS section] Phase Gate 4
14. [HALT. Re-read FORMAT CONTRACT schema (4). -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
16. [REGISTER-CONSISTENCY AUDIT: 2-item -- ROADMAP section] Phase Gate 5
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5). sole-instruction-site annotation. -- 5-item] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: C-39 + C-40 on R15 V-05 Base (all 40 criteria)

**Axis**: Maximum mechanical stack -- C-39 + C-40 added to R15 V-05 base targeting all 40 criteria
**Hypothesis**: R15 V-05 carries all 38 criteria. One C-39 gap remains: the C-33 sole-instruction
note for DRI/Owner in STEP 7 is bracketed prose positioned after the Proceed line -- outside the
HALT block. C-39 requires the annotation inside the HALT block at the specific checklist item.
V-05 moves the DRI/Owner sole-instruction annotation inside HALT checklist item 3; adds
sole-instruction-site annotations to all other HALT blocks for each of their governed requirements;
adds REGISTER-CONSISTENCY AUDIT at all 5 phase gates with audit items adapted to the full C-01
through C-38 mechanical stack. Targeting all 40 criteria.

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
HALT. Re-read ROLE-NAME LOCK structure: complete role enumeration from ROLES-LOADED / per-cell enforcement notes at DRI/Owner (site 2) and Key Roles (site 5) / per-name enforcement note at Membership/Decides (site 3) / no-novel-role constraint at all five sites.
  [sole instruction site for lock-enumeration accuracy requirements:
   (a) lock list must contain exactly the count from ROLES-LOADED -- no more, no fewer;
   (b) every role must appear verbatim in ROLES-LOADED;
   (c) no invented role absent from ROLES-LOADED.
   No other location in this prompt introduces competing language for requirements (a), (b), (c).
   These requirements travel with this HALT block as the exclusive instruction authority.]
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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 1:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] ROLES-LOADED block: mandatory DO-produce listing language -- no advisory qualifier.
  [ ] ROLE-TYPE-CLASSIFICATION: mandatory "every loaded role must appear" classification language -- no hedging.
  [ ] ROLE-NAME LOCK declaration: mandatory "no role name may appear" exclusion language -- no "where possible".
  [ ] ROLE-NAME LOCK per-cell notes (sites 2 and 5): mandatory per-cell procedural language -- no advisory qualifier.
  [ ] ROLE-NAME LOCK per-name note (site 3): mandatory per-name procedural language with anti-drift prohibition -- no advisory qualifier.
  [ ] ROLE-NAME LOCK HALT block: sole-instruction-site annotation present for requirements (a)(b)(c) -- no competing language at any other site.
If any advisory qualifier was introduced at any of the above sites, correct before continuing.
DO NOT emit the phase gate until all six confirmed.

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
  [sole instruction site for Rebuttal four-field form-order requirement: the four fields must
   appear in this exact sequence. No other location in this prompt names the Rebuttal field
   sequence. This HALT block is the exclusive instruction authority for field order. A Rebuttal
   produced without consulting this block violates the sole-instruction-site constraint.]
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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 2:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] Mechanism-Type VOCABULARY block: mandatory "No row may use a Type value outside this list" -- no conditional qualifier.
  [ ] Per-row mechanism vocabulary check: mandatory "verify the Type value appears...before writing the next row" -- no "where possible" softening.
  [ ] Rebuttal HALT block: sole-instruction-site annotation present for four-field form-order requirement -- no competing instruction at any other site.
  [ ] REBUTTAL FORM CHECK [SITE 4]: mandatory "must name exactly one role from the ROLE-NAME LOCK list" -- no conditional qualifier.
  [ ] VERDICT FLAT-CASE-PRESSURE rating: drawn from the closed set (Strong / Moderate / Weak / Negligible / Insufficient) -- no open-ended rating introduced.
If any advisory qualifier was introduced at any governed instruction site, correct before continuing.
DO NOT emit the phase gate until all five confirmed.

`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

CHECK [SITE 1 -- DIAGRAM]: every role name placed in this diagram must appear in the ROLE-NAME LOCK
list. For each node label: verify the label appears in ROLE-NAME LOCK before placing the next node
-- do not complete the diagram and verify after. A label absent from ROLE-NAME LOCK is a violation
regardless of position.
Draw ASCII hierarchy with minimum two levels. Use only printable ASCII characters (+, -, |, and text).
Committees as distinct labeled nodes -- not embedded in an area box.

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 3:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] ASCII diagram CHECK [SITE 1]: mandatory "must appear in the ROLE-NAME LOCK list" language -- no "where possible" qualifier.
  [ ] Per-node verification instruction: mandatory "verify the label appears in ROLE-NAME LOCK before placing the next node" -- no advisory softening.
If any advisory qualifier was introduced at the diagram CHECK instruction site, correct before continuing.
DO NOT emit the phase gate until both confirmed.

`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

HALT. Re-read FORMAT CONTRACT schema (1) -- headcount table.
  [sole instruction site for Headcount table schema (1) requirements: five-column structure,
   Decides/Escalates non-merge constraint, Key Roles role-membership constraint, Total-row
   requirement. No other location in this prompt introduces competing language for these
   schema (1) requirements.]
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
  2. Minimum three rows confirmed: ROB, shiproom/gate, governance meeting. No merged rows.
  3. DRI / Owner confirmed: every cell value must be a role from the ROLE-NAME LOCK list.
     [sole instruction site for DRI/Owner role-lock requirement -- this checklist item 3 is the
      exclusive authority for the DRI/Owner role membership constraint; no other instruction site
      in this prompt introduces competing language for this requirement]
Proceed only if all three confirmed.

Produce per schema (2) of the FORMAT CONTRACT.

CHECK [SITE 2 -- DRI/OWNER -- per-cell directive]:
The per-cell directive from the ROLE-NAME LOCK block applies here at every row. For each cell in
the DRI / Owner column: verify the value appears in the ROLE-NAME LOCK list before populating the
next row -- do not complete the column and verify after. A novel role name at any DRI/Owner cell
is a violation regardless of row position.

STEP 8 -- COMMITTEE CHARTERS

Write a charter per governance rhythm row per schema (3) of the FORMAT CONTRACT.

BEFORE PRODUCING each charter:
HALT. Re-read FORMAT CONTRACT schema (3) -- committee charter.
  [sole instruction site for Charter schema (3) requirements: Membership minimum-two-roles from
   ROLE-NAME LOCK, Escalates-must-name-destination, Quorum fraction form [N] of [M] member roles
   required, DISQUALIFY-IF for Quorum omitting denominator M. No other location in this prompt
   introduces competing language for these charter requirements.]
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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 4:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] Schema (1) HALT: sole-instruction-site annotation present for schema (1) requirements.
  [ ] Schema (1) HALT item 2: mandatory DISQUALIFY-IF language for Decides/Escalates merge -- no conditional qualifier.
  [ ] Schema (1) HALT item 3: mandatory "every value must be a role from ROLE-NAME LOCK" for Key Roles -- no "where possible" softening.
  [ ] Schema (2) HALT item 3: mandatory "every cell value must be a role from the ROLE-NAME LOCK list" -- sole-instruction-site annotation present on this item; no competing language at any other site.
  [ ] Schema (3) HALT: sole-instruction-site annotation present for schema (3) charter requirements.
  [ ] Schema (3) HALT item 5: mandatory "[N] of [M] member roles required" fraction form -- no short-form.
  [ ] Schema (3) HALT item 6: mandatory DISQUALIFY-IF language for Quorum denominator -- no advisory qualifier.
  [ ] Charter CHECK [SITE 3] per-name Membership directive: mandatory "verify...before adding the next name" with anti-drift prohibition -- no advisory softening.
  [ ] Charter CHECK [SITE 3] per-name Decides directive: same mandatory language and anti-drift prohibition.
If any advisory qualifier was introduced at any of these instruction sites, correct before continuing.
DO NOT emit the phase gate until all nine confirmed.

STEP 9 -- ORG-ELEMENT REGISTER

HALT. Re-read FORMAT CONTRACT schema (4) -- ORG-ELEMENT REGISTER.
  1. cat-1 (Areas) confirmed: will be populated with area names and headcounts.
  2. cat-2 (Committees/Cadences) confirmed: will be populated.
  3. cat-3 (Headcount) confirmed: will be populated with the total.
  4. cat-4 (DRI Roles) confirmed: will be populated.
Proceed only if all four confirmed.

Produce per schema (4). All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

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

REGISTER-CONSISTENCY AUDIT -- before emitting PHASE GATE 5:
HALT. Confirm all active governed requirements used mandatory-register language before advancing:
  [ ] TRIGGER-TYPE VOCABULARY block: mandatory "No two consecutive rows may share the same Type value" -- no "try to avoid" or "where possible" qualifier.
  [ ] Per-row trigger vocabulary check: mandatory "verify the Type appears...and does not repeat...before writing the next row" -- no advisory softening.
If any advisory qualifier was introduced at either instruction site, correct before continuing.
DO NOT emit the phase gate until both confirmed.

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
  [sole instruction site for Anti-Pattern Watch citation-prefix requirement: every "Why It
   Applies Here" cell must open with [element name] (cat-N) -- and the DISQUALIFY-IF applies
   to every cell. No other location in this prompt introduces competing language for this
   requirement.]
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
     sole-instruction-site annotation for (a)(b)(c). -- 4-item checklist]
    ROLE-NAME LOCK (complete enumeration + [DRI/Owner per-cell] + [Key Roles per-cell] + [Membership/Decides per-name with anti-drift] + five-site CHECK with per-cell at 2+5, per-name at 3)
5.  [REGISTER-CONSISTENCY AUDIT: 6-item -- ROLES section] Phase Gate 1
6.  Inertia: [MECHANISM-TYPE VOCAB] / [per-row verify] / table / [VERIFY] / [FLAT-CASE-CLOSED] /
    How We Coordinate Today /
    [HALT. Re-read four-field Rebuttal form: ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER.
     sole-instruction-site annotation for form-order. -- 4-item field checklist] /
    [REBUTTAL FORM: CHECK SITE 4 + VERIFY] / VERDICT
7.  [REGISTER-CONSISTENCY AUDIT: 5-item -- INERTIA section] Phase Gate 2
8.  ASCII Org Diagram [CHECK SITE 1 -- per-node verify]
9.  [REGISTER-CONSISTENCY AUDIT: 2-item -- STRUCTURE section] Phase Gate 3
10. [HALT. Re-read FORMAT CONTRACT schema (1). sole-instruction-site annotation for schema (1) requirements. -- 4-item]
    Headcount by Area [VERIFY: merged] [CHECK SITE 5 -- per-cell; lock-declared directive applies]
11. [HALT. Re-read FORMAT CONTRACT schema (2). sole-instruction-site annotation on item 3 for DRI/Owner. -- 3-item]
    Operating Rhythm Table [CHECK SITE 2 -- per-cell; no co-located advisory prose]
12. [HALT. Re-read FORMAT CONTRACT schema (3). sole-instruction-site annotation for schema (3) requirements. -- 6-item per charter]
    Committee Charters [CHECK SITE 3 -- per-name] [VERIFY: short Quorum]
13. [REGISTER-CONSISTENCY AUDIT: 9-item -- HEADCOUNT/RHYTHM/CHARTERS section] Phase Gate 4
14. [HALT. Re-read FORMAT CONTRACT schema (4). -- 4-item] ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCAB] + [per-row verify] + Roadmap [VERIFY: duplicate type]
16. [REGISTER-CONSISTENCY AUDIT: 2-item -- ROADMAP section] Phase Gate 5
17. [CAT-N-CITATION-SCHEMA] +
    [HALT. Re-read FORMAT CONTRACT schema (5). sole-instruction-site annotation for citation-prefix requirement. -- 5-item] +
    [per-row citation verify] + Anti-Pattern Watch [VERIFY: untyped citation]

End with: `Generated by: /org-chart {topic} -- {date}`
