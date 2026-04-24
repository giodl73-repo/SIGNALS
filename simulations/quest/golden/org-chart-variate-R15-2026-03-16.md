---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R15
rubric_version: v3
status: variate
---

# org-chart Variate -- Round 15 (Rubric v3 / Cycle Round 3)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v3 (C-01 through C-17; C-15/C-16/C-17 new from v3)
**Round:** R15 overall / Round 3 of the v3 rubric cycle

**R14 ceiling under v1 rubric:**
V-05/R14 achieves strong coverage of C-01 through C-10. Three gaps remain in all R14
variations not yet addressed:

1. **ABSENT-label gap (C-15):** When VERDICT = CAN-OPERATE-FLAT, structural sections
   (ASCII Org, Headcount, Rhythm, Charters) are silently skipped in all R14 variations.
   No variation explicitly labels them ABSENT or prohibits "simplified"/"compact"
   alternatives. The compressed-hierarchy false-positive path remains open.

2. **Single-anchor bypass gap (C-16):** All R14 variations state critical constraints
   at one enforcement site only. Example: FLAT-CASE-PRESSURE is required to "open the
   VERDICT" (slot-order), but no variation also states "DO NOT write the verdict
   declaration before the FLAT-CASE-PRESSURE line is present." One site allows the
   model to satisfy the letter while violating intent.

3. **Batching gap (C-17):** All R14 variations present the Operating Rhythm table as a
   complete block, then Committee Charters as a complete block. No variation requires
   pair-wise production (rhythm row N -> its charter) or explicitly prohibits batching.
   Drift between rhythm table names and charter content remains possible.

**R15 target:** Close all three v3 gaps. V-01/V-02/V-03 are single-axis; V-04/V-05
are combined.

---

## Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | ABSENT-label SKIP (C-15) | Forcing the CAN-OPERATE-FLAT branch to label each eliminated section ABSENT and prohibiting "simplified" or "compact" alternatives closes the false-positive where a compressed hierarchy masquerades as a flat-verdict artifact |
| V-02 | Two-site constraint enforcement (C-16) | Stating each critical constraint at both a slot-order site ("X must appear before Y") and a conditional-prohibition site ("DO NOT write Y without X above it") eliminates single-anchor bypass for FLAT-CASE-PRESSURE, re-assessment trigger, and Quorum fraction |
| V-03 | Rhythm-charter interleaving (C-17) | Requiring paired production (rhythm row -> its charter before the next row) and explicitly prohibiting all-rows-then-all-charters batching keeps the rhythm-charter coupling tight and detectable |
| V-04 | Two-site + interleaving (C-16 + C-17) | Combining dual-anchor enforcement with interleaved production closes the two structural bypass paths without changing section content or inertia framing |
| V-05 | Full integration: R14-V-05 baseline + C-15 + C-16 + C-17 | Layering ABSENT-labeling, two-site constraints, and interleaved rhythm-charter production onto the proven R14-V-05 foundation (default-position declaration + table schemas + count-and-advance gates) achieves the v3 composite target |

---

## V-01 -- ABSENT-Label SKIP Enforcement

**axis:** conditional-section-elimination
**hypothesis:** When VERDICT = CAN-OPERATE-FLAT, explicitly labeling each structural
section ABSENT and prohibiting "simplified" / "compact" alternatives closes the
false-positive where a compressed hierarchy satisfies C-03 while violating the
flat-verdict branch. The label must name the prohibited alternative by type, not just
say "this section is skipped."

---

```
You are running `/org-chart {topic}`.

STARTING ASSUMPTION: THE TEAM CAN OPERATE FLAT.

Formal structure must be justified. Do not draw an org until you have argued the case
for staying flat and found a specific failure mode it cannot answer.

---

STEP 1 -- LOAD AND CLASSIFY ROLES

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE instead:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name used later must be declared here first.

Immediately after, produce ROLE-TYPE-CLASSIFICATION in three-tier order:
  Tier 1 (Engineering) -- complete before writing Tier 2
  Tier 2 (Operations)  -- complete before writing Tier 3
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

STEP 2 -- INERTIA ASSESSMENT (four sub-sections, strict order)

Sub-section 1 -- Case for Staying Flat

Produce a mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |

Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

Minimum two data rows. After writing the table, count data rows (header excluded).
If count < 2, add missing rows until count >= 2. Then emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Inventory coordination patterns not already in the Sub-section 1 table.

Sub-section 3 -- Rebuttal
Name the specific failure mode the Sub-section 1 mechanisms cannot answer.
Observable: blocked decision, missed SLA, time-zone gap, knowledge silo, competing
roadmap. Do not write "the team is growing" alone.

Sub-section 4 -- VERDICT

Open with (required before any other sentence in this sub-section):
  FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + named failure mode]
Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then choose exactly one:
  CAN-OPERATE-FLAT
  STRUCTURE-WARRANTED

Then write a re-assessment trigger with a concrete, measurable threshold.

---

FLAT-VERDICT BRANCH -- ABSENT LABELING REQUIRED

IF VERDICT = CAN-OPERATE-FLAT:

  DO NOT silently skip the structural sections.
  DO NOT produce a "simplified hierarchy" or "compact org" as an alternative.
  DO NOT write a flat list of names and call it an org diagram.
  A simplified hierarchy IS NOT an acceptable substitute for ABSENT sections.

  Instead, label each structural section in this exact format:

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy is not warranted.
    PROHIBITED ALTERNATIVE: Do not substitute a "simplified hierarchy" or
    "compact org chart" -- both are structural proposals and require STRUCTURE-WARRANTED.
    ABSENT sections: Headcount by Area, Operating Rhythm, Committee Charters,
    ORG-ELEMENT REGISTER, Org Evolution Roadmap, Anti-Pattern Watch.

  After labeling the first ABSENT section, do not produce any structural content.
  End the artifact with:
    Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: continue with Step 3.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

STEP 3 -- ASCII ORG DIAGRAM (STRUCTURE-WARRANTED only)

Draw after the phase gate. Minimum two hierarchy levels. Committees as distinct nodes.
All role names from ROLES-LOADED or ROLES-NOTE only.

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

STEP 4 -- HEADCOUNT BY AREA

Columns: Area | Headcount | Key Roles | Decides | Escalates
Decides and Escalates are separate columns -- do NOT merge into "Decision Scope."
Annotate Key Roles as [role name] ([domain type]).
Minimum two area rows plus **Total** row.

---

STEP 5 -- OPERATING RHYTHM TABLE

Columns: Cadence | Frequency | DRI / Owner | Purpose
Minimum three distinct rows: ROB + shiproom or gate + governance meeting.
Do not combine two meetings into one row.

---

STEP 6 -- COMMITTEE CHARTERS

Write one charter per governance meeting in the rhythm table. Five fields required:

  Purpose:
  Membership:   [role name] ([domain type]) -- >= 2 roles
  Decides:
  Escalates:    [named destination -- not "everything not in Decides"]
  Quorum:       [N] of [M] member roles required for binding decisions

Quorum fraction format required. Short form "N roles required" is not acceptable.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

STEP 7 -- ORG-ELEMENT REGISTER + ROADMAP + WATCH

ORG-ELEMENT REGISTER (all four categories):
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

Org Evolution Roadmap (two rows, distinct trigger categories):
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone event

Anti-Pattern Watch (>= 2 rows):
  | Anti-Pattern | Why It Applies Here | Mitigation |
  Each "Why It Applies Here" opens with: [element name] (cat-N) -- [one sentence]
  Only use cat codes from the ORG-ELEMENT REGISTER.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02 -- Two-Site Constraint Enforcement

**axis:** dual-anchor constraint placement
**hypothesis:** Stating each critical constraint at two independent enforcement sites --
once as a slot-order rule (X must appear before Y) and once as a conditional prohibition
(DO NOT write Y without X above it) -- eliminates single-anchor bypass. A model can
satisfy slot order while placing the required element in the wrong position; the
conditional prohibition closes that path. Three constraints are anchored at two sites:
FLAT-CASE-PRESSURE, re-assessment trigger, and Quorum fraction form.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description]

If no files found:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name used later must be declared here first.

Immediately after, produce ROLE-TYPE-CLASSIFICATION in three-tier order:
  Tier 1 (Engineering) first, then Tier 2 (Operations), then Tier 3 (PM/Design/Research/Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Write before any org diagram. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count after writing. If count < 2, add rows. Emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Inventory active coordination patterns not already in the Sub-section 1 table.

Sub-section 3 -- Rebuttal
Name the specific failure mode the mechanisms cannot answer. Observable required.

Sub-section 4 -- VERDICT

FLAT-CASE-PRESSURE CONSTRAINT -- TWO ENFORCEMENT SITES:

  SITE 1 (slot order): The VERDICT sub-section MUST open with the FLAT-CASE-PRESSURE
  line. It is the first and only sentence before the verdict declaration.

  SITE 2 (conditional prohibition): DO NOT write "CAN-OPERATE-FLAT" or
  "STRUCTURE-WARRANTED" before the following line is present in the output:
    FLAT-CASE-PRESSURE: [rating] -- [sentence]
  If you have written a verdict declaration and the FLAT-CASE-PRESSURE line does not
  appear above it, delete the declaration and write the pressure line first.

Required format:
  FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

RE-ASSESSMENT TRIGGER CONSTRAINT -- TWO ENFORCEMENT SITES:

  SITE 1 (slot order): The re-assessment trigger MUST appear immediately after the
  verdict declaration, before any other text in the VERDICT sub-section.

  SITE 2 (conditional prohibition): DO NOT emit the INERTIA COMPLETE phase gate before
  a re-assessment trigger with a concrete, measurable threshold is present in the output.
  "Revisit as the team grows" is not a concrete threshold.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

ASCII ORG DIAGRAM

Draw after the gate. Minimum two levels. Committees as distinct labeled nodes.
All role names from ROLES-LOADED or ROLES-NOTE only.

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

HEADCOUNT BY AREA

Columns: Area | Headcount | Key Roles | Decides | Escalates
Decides and Escalates are separate. Do NOT use "Decision Scope."
Annotate Key Roles as [role name] ([domain type]).
Minimum two area rows plus **Total** row.

---

OPERATING RHYTHM TABLE

Columns: Cadence | Frequency | DRI / Owner | Purpose
Minimum three distinct rows: ROB + shiproom or gate + governance meeting.
Do not combine two meetings into one row.

---

COMMITTEE CHARTERS

Write one charter per governance meeting in the rhythm table.

QUORUM FRACTION CONSTRAINT -- TWO ENFORCEMENT SITES:

  SITE 1 (field definition): The Quorum field in every charter MUST use the format:
    Quorum: [N] of [M] member roles required for binding decisions

  SITE 2 (conditional prohibition): DO NOT emit the CHARTERS COMPLETE phase gate before
  every charter in the output contains a Quorum field in the full fraction format.
  If any charter contains "Quorum: [N] roles required" (short form), rewrite that
  charter's Quorum field before proceeding. Short form is not acceptable at any point.

Five required fields per charter:
  Purpose:
  Membership:   [role name] ([domain type]) -- >= 2 roles
  Decides:
  Escalates:    [named destination -- not "everything not in Decides"]
  Quorum:       [N] of [M] member roles required for binding decisions

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

All four categories required:
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

---

ORG EVOLUTION ROADMAP

Two rows, distinct trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone event (not another headcount)

---

ANTI-PATTERN WATCH

>= 2 rows:
  | Anti-Pattern | Why It Applies Here | Mitigation |
Each "Why It Applies Here" opens with: [element name] (cat-N) -- [one sentence]
Only use cat codes from the ORG-ELEMENT REGISTER.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-03 -- Rhythm-Charter Interleaving

**axis:** production-order coupling
**hypothesis:** Requiring pair-wise production (rhythm row N -> its charter before row
N+1) and explicitly prohibiting the batching pattern ("DO NOT write all rhythm rows
first and all charters second") keeps each charter immediately verifiable against its
rhythm entry. Batching separates cadence from governance, allowing drift between what
the rhythm table names and what the charter specifies. Interleaving makes that drift
detectable at the point of production.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE instead with inferred roles.
Every role name used later must be declared here first.

Immediately after, produce ROLE-TYPE-CLASSIFICATION in three-tier order:
  Engineering types first, then Operations, then PM / Design / Research / Other.

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Write before any org diagram.

Sub-section 1 -- Case for Staying Flat
Mechanism table: Mechanism Name | Type | Frequency / Participants
Type closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two rows. Count. Emit separator when count >= 2:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Active coordination patterns not already in the Sub-section 1 table.

Sub-section 3 -- Rebuttal
Specific observable failure the mechanisms cannot answer.

Sub-section 4 -- VERDICT
Open with:
  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)
Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
Then: re-assessment trigger with concrete, measurable threshold.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

ASCII ORG DIAGRAM

Draw after the gate. Minimum two levels. Committees as distinct nodes.
Role names from ROLES-LOADED or ROLES-NOTE only.

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

HEADCOUNT BY AREA

Columns: Area | Headcount | Key Roles | Decides | Escalates
Decides and Escalates are separate. Key Roles annotated as [role name] ([domain type]).
Minimum two area rows plus **Total** row.

---

OPERATING RHYTHM AND COMMITTEE CHARTERS -- INTERLEAVED

INTERLEAVING RULE: Produce each rhythm row immediately followed by its committee
charter before writing the next rhythm row.

DO NOT write all rhythm rows first and all committee charters second.
DO NOT batch the Operating Rhythm table as a complete block before writing any charter.
A batched rhythm table followed by a batched charter block violates this rule even if
both contain the correct content.

The correct production order is:

  [RHYTHM ROW 1: ROB entry]
    Cadence | Frequency | DRI / Owner | Purpose
    ROB     | ...       | [role]      | ...

  [No charter for ROB -- ROB is not a governance committee; continue to next row]

  [RHYTHM ROW 2: shiproom or gate entry]
    [row content]

  [No charter for shiproom -- shiproom is not a governance committee; continue]

  [RHYTHM ROW 3+: governance committee entry]
    [row content]

  [CHARTER FOR ROW 3: immediately after its rhythm row]
    ### [Committee Name]
    Purpose:
    Membership:   [role name] ([domain type]) -- >= 2 roles
    Decides:
    Escalates:    [named destination]
    Quorum:       [N] of [M] member roles required for binding decisions

  [RHYTHM ROW 4+: next governance committee, if any]
    [row content]

  [CHARTER FOR ROW 4: immediately after its rhythm row]
    [charter content]

AFTER INTERLEAVING IS COMPLETE:

Verify: every governance meeting in the rhythm entries has a charter immediately
following it. If any governance row has no charter below it, write the missing charter
before continuing.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

All four categories required:
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

---

ORG EVOLUTION ROADMAP

Two rows from distinct trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone (not another headcount)

---

ANTI-PATTERN WATCH

>= 2 rows:
  | Anti-Pattern | Why It Applies Here | Mitigation |
Each "Why It Applies Here" opens with: [element name] (cat-N) -- [one sentence]
Only use cat codes defined in the ORG-ELEMENT REGISTER.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04 -- Two-Site + Interleaving Combined

**axis:** C-16 + C-17 structural constraint architecture
**hypothesis:** Two-site enforcement for the three critical constraints (FLAT-CASE-PRESSURE,
re-assessment trigger, Quorum fraction) combined with interleaved rhythm-charter production
closes both the single-anchor bypass and the batching gap without changing inertia framing
or table schemas. These are structural constraints on constraint placement, not content
constraints, so they compose cleanly.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description]

If no files found, produce ROLES-NOTE with inferred roles.
Every role used later must be declared here.

Immediately after, produce ROLE-TYPE-CLASSIFICATION, three-tier order:
  Engineering first, then Operations, then PM / Design / Research / Other.

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Sub-section 1 -- Case for Staying Flat
Table: Mechanism Name | Type | Frequency / Participants
Type: Channel / Informal Role / Recurring Cadence / Shared Artifact
Two rows minimum. Count. Emit separator when count >= 2:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not in Sub-section 1.

Sub-section 3 -- Rebuttal
Specific observable failure mode.

Sub-section 4 -- VERDICT

FLAT-CASE-PRESSURE -- TWO ENFORCEMENT SITES:
  SITE 1 (slot): VERDICT sub-section opens with the FLAT-CASE-PRESSURE line.
  SITE 2 (conditional): DO NOT write CAN-OPERATE-FLAT or STRUCTURE-WARRANTED before
  the FLAT-CASE-PRESSURE line is present above it in the output.

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

RE-ASSESSMENT TRIGGER -- TWO ENFORCEMENT SITES:
  SITE 1 (slot): Trigger appears immediately after the verdict declaration.
  SITE 2 (conditional): DO NOT emit the INERTIA COMPLETE phase gate before a concrete
  re-assessment trigger is present. "Revisit as the team grows" is not concrete.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

ASCII ORG DIAGRAM

Draw after the gate. Two levels minimum. Committees as distinct nodes.
Role names from ROLES-LOADED or ROLES-NOTE only.

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

HEADCOUNT BY AREA

Columns: Area | Headcount | Key Roles | Decides | Escalates
Separate Decides and Escalates columns required. Key Roles annotated [role] ([type]).
Two area rows minimum plus **Total** row.

---

OPERATING RHYTHM AND COMMITTEE CHARTERS -- INTERLEAVED PRODUCTION

INTERLEAVING RULE: Write each rhythm row, then its charter (if it is a governance
committee), before writing the next rhythm row.

DO NOT write all rhythm rows first and all committee charters second.
DO NOT produce the Operating Rhythm as a complete standalone table block.

Production sequence:
  1. Write rhythm row for ROB (no charter required -- ROB is not a governance committee)
  2. Write rhythm row for shiproom / gate (no charter required)
  3. Write rhythm row for governance committee 1 -> then write its charter immediately
  4. Write rhythm row for governance committee 2 (if any) -> then write its charter
  Continue until all rhythm rows and their charters are written.

Charter schema (five fields required):
  ### [Committee Name]
  Purpose:
  Membership:   [role name] ([domain type]) -- >= 2 roles with annotation
  Decides:
  Escalates:    [named destination -- not "everything not in Decides"]
  Quorum:       [N] of [M] member roles required for binding decisions

QUORUM FRACTION -- TWO ENFORCEMENT SITES:
  SITE 1 (field): Quorum field uses the full fraction format shown above.
  SITE 2 (conditional): DO NOT emit the CHARTERS COMPLETE phase gate if any charter
  in the output uses the short form "Quorum: [N] roles required." Rewrite first.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

All four categories:
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

---

ORG EVOLUTION ROADMAP

Two rows from distinct trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone

---

ANTI-PATTERN WATCH

>= 2 rows:
  | Anti-Pattern | Why It Applies Here | Mitigation |
Each "Why It Applies Here": [element name] (cat-N) -- [one sentence]
Only cat codes from the ORG-ELEMENT REGISTER.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-05 -- Full Integration: R14-V05 Baseline + C-15 + C-16 + C-17

**axis:** combined -- default-position (V-01/R14) + table schemas (V-02/R14) + count-and-advance
(V-04/R14) + ABSENT-label SKIP (C-15) + two-site constraint enforcement (C-16) + rhythm-charter
interleaving (C-17)
**hypothesis:** Layering the three v3 new criteria onto the R14 V-05 foundation achieves the
v3 composite target. The R14 V-05 baseline already handles C-01 through C-10 via default-position
declaration, inline table schemas, and count-and-advance gates. Adding ABSENT labeling, dual-anchor
constraints, and interleaved production closes C-15/C-16/C-17 without disrupting the proven
essentials.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

PHASE 1: LOAD AND CLASSIFY ROLES

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found:
  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this document must be declared here.

Immediately produce ROLE-TYPE-CLASSIFICATION in three-tier order:
  Tier 1 (Engineering) -- complete before writing Tier 2
  Tier 2 (Operations)  -- complete before writing Tier 3
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

PHASE 2: INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Write before any org diagram. You are the advocate for staying flat.

Sub-section 1 -- Case for Staying Flat

Fill this table schema with the team's actual coordination mechanisms:

  | Mechanism Name                    | Type               | Frequency / Participants      |
  |-----------------------------------|--------------------|-------------------------------|
  | (e.g., #signal-eng Slack channel) | Channel            | (e.g., Continuous, 14 people) |
  | (e.g., Monday standup)            | Recurring Cadence  | (e.g., Weekly, 8 leads)       |

Type must be one of: Channel / Informal Role / Recurring Cadence / Shared Artifact

COUNT CHECKPOINT:
  MECHANISM-ROW-COUNT: [N] rows.
  If N < 2: add missing rows until N >= 2. Re-emit count.
When count >= 2, emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Describe coordination patterns in practice. Do not repeat Sub-section 1 table entries.

Sub-section 3 -- Rebuttal
Name the ONE failure mode the Sub-section 1 mechanisms cannot resolve.
Must name an observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap. "The team is growing" alone is not acceptable.

Sub-section 4 -- VERDICT

FLAT-CASE-PRESSURE -- TWO ENFORCEMENT SITES:
  SITE 1 (slot): The first and only sentence in this sub-section before the verdict
  declaration is the FLAT-CASE-PRESSURE line.
  SITE 2 (conditional): DO NOT write "CAN-OPERATE-FLAT" or "STRUCTURE-WARRANTED"
  before the FLAT-CASE-PRESSURE line is present above it in the output.

  FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + named failure mode]
  Rating closed set: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then declare: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

RE-ASSESSMENT TRIGGER -- TWO ENFORCEMENT SITES:
  SITE 1 (slot): The trigger appears immediately after the verdict declaration, before
  any other text in the VERDICT sub-section.
  SITE 2 (conditional): DO NOT emit the INERTIA COMPLETE phase gate before a concrete,
  measurable re-assessment trigger is present. "Revisit as the team grows" is not a
  concrete threshold and does not satisfy this requirement.

---

FLAT-VERDICT BRANCH -- ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:

  DO NOT silently skip structural sections.
  DO NOT produce a "simplified hierarchy" or "compact org" as an alternative.
  A simplified hierarchy IS NOT a valid substitute for an ABSENT section.

  Label each structural section explicitly:

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy is not warranted.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org chart" are both
    structural proposals -- they require STRUCTURE-WARRANTED, not CAN-OPERATE-FLAT.
    Remaining sections also ABSENT: Headcount by Area, Operating Rhythm, Committee
    Charters, ORG-ELEMENT REGISTER, Org Evolution Roadmap, Anti-Pattern Watch.

  End the artifact immediately after the ABSENT block with:
    Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit the phase gate and continue.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

PHASE 3: ASCII ORG DIAGRAM

Draw after the gate. Schema:

  [Top-Level Lead]
        |
  ------+--------+---------
  |              |         |
  [Area A]   [Area B]   [Committee X]
  Lead         Lead

Rules:
  - Minimum two hierarchy levels
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

PHASE 4: HEADCOUNT BY AREA

Fill this schema (Decides and Escalates are ALWAYS separate columns):

  | Area     | Headcount | Key Roles                    | Decides               | Escalates              |
  |----------|-----------|------------------------------|-----------------------|------------------------|
  | (area 1) | N         | [role name] (Engineering)    | (decision types)      | (types) -> [dest.]     |
  | (area 2) | N         | [role name] (PM)             | (decision types)      | (types) -> [dest.]     |
  | **Total**| N         |                              |                       |                        |

DO NOT use a "Decision Scope" column.
Annotate Key Roles as [role name] ([domain type]).
Two area rows minimum plus Total row.

COUNT CHECKPOINT: HEADCOUNT-SUM: [area sums] = Total.

---

PHASE 5: OPERATING RHYTHM AND COMMITTEE CHARTERS -- INTERLEAVED

INTERLEAVING RULE: Write each rhythm row, then its committee charter (if governance),
before writing the next rhythm row.

DO NOT write all rhythm rows first and all committee charters second.
DO NOT batch the Operating Rhythm table as a complete standalone block.

Schema for rhythm rows:
  | Cadence         | Frequency | DRI / Owner | Purpose |

Schema for committee charters (immediately follows its rhythm row):
  ### [Committee Name]
  Purpose:     [what it governs]
  Membership:
    - [role name] ([domain type])
    - [role name] ([domain type])
    (minimum two roles with domain annotation)
  Decides:     [decision types owned here]
  Escalates:   [named destination role or forum]
  Quorum:      [N] of [M] member roles required for binding decisions

QUORUM FRACTION -- TWO ENFORCEMENT SITES:
  SITE 1 (field): The Quorum field uses the full fraction format above.
  SITE 2 (conditional): DO NOT emit the CHARTERS COMPLETE phase gate if any charter
  in the output uses the short form "Quorum: [N] roles required." Rewrite first.
  Example of required form: "Quorum: 3 of 5 member roles required for binding decisions."

Production sequence:
  1. Rhythm row: ROB (weekly leadership review) -- no charter (ROB is not a committee)
  2. Rhythm row: shiproom / gate -- no charter (shiproom is not a governance committee)
  3. Rhythm row: governance committee 1 -- write its charter immediately after this row
  4. Rhythm row: governance committee 2 (if any) -- write its charter immediately
  Continue until all rows and charters are written.

COUNT CHECKPOINT: CADENCE-ROW-COUNT: [N] rows. >= 3 required (ROB + gate + >= 1 committee).

Verify interleaving: every governance row has a charter immediately below it before
the next row begins. If not, write the missing charter before continuing.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

PHASE 6: REGISTER

Populate all four categories before the roadmap:

  ORG-ELEMENT REGISTER:
  cat-1 (Areas):
    - [area name] -- headcount: [N]
  cat-2 (Committees/Cadences):
    - [name]
  cat-3 (Headcount):
    - Total headcount: [N]
  cat-4 (DRI Roles):
    - [DRI role from Operating Rhythm]

---

PHASE 6 (continued): ORG EVOLUTION ROADMAP

  | Trigger                      | Structural Change | Type                        |
  |------------------------------|-------------------|-----------------------------|
  | Row 1: headcount threshold   | ...               | Headcount                   |
  | Row 2: different-category    | ...               | Workload / Symptom /        |
  |        trigger               |                   | Milestone                   |

Two rows from DISTINCT trigger categories. Two headcount rows do not qualify.

---

PHASE 6 (continued): ANTI-PATTERN WATCH

  | Anti-Pattern | Why It Applies Here                                           | Mitigation |
  |--------------|---------------------------------------------------------------|------------|
  | (name)       | [element name] (cat-N) -- [one sentence of specific relevance]| ...        |
  | (name)       | [element name] (cat-N) -- [one sentence of specific relevance]| ...        |

Each "Why It Applies Here" opens with typed citation: [element name] (cat-N).
Only use cat codes defined in the ORG-ELEMENT REGISTER (cat-1 through cat-4).
Two rows minimum.

---

SECTION ORDER (enforced by phase gates):
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION (three-tier order)
3. === PHASE GATE: ROLES COMPLETE ===
4. Inertia Assessment:
   - Sub-section 1 (mechanism table + MECHANISM-ROW-COUNT + FLAT-CASE-CLOSED separator)
   - Sub-section 2 (How We Coordinate Today)
   - Sub-section 3 (Rebuttal)
   - Sub-section 4 (FLAT-CASE-PRESSURE [two sites] + verdict + re-assessment trigger [two sites])
5. === PHASE GATE: INERTIA COMPLETE ===
   [IF CAN-OPERATE-FLAT: emit ABSENT labels for all structural sections, then end]
6. ASCII Org Diagram
7. === PHASE GATE: STRUCTURE COMPLETE ===
8. Headcount by Area (HEADCOUNT-SUM checkpoint)
9. Operating Rhythm + Committee Charters (INTERLEAVED; CADENCE-ROW-COUNT checkpoint;
   Quorum fraction [two sites])
10. === PHASE GATE: CHARTERS COMPLETE ===
11. ORG-ELEMENT REGISTER
12. Org Evolution Roadmap
13. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```
