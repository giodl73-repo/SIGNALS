Now I have the full T3 runbook. Generating 5 variations.

---

# /quest:variate — org-chart — Round 3

Skill: `org-chart` — Org structure generation with areas, committees, and operating rhythms.
Baseline: T3 runbook (Engineering-first tier order, 4-sub-section inertia, ASCII diagram, full table suite, phase gates throughout).

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|-----------|
| V-01 | Role sequence (PM-first tier) | Leading with business roles before technical roles surfaces product-outcome alignment earlier; may produce orgs that are easier for exec reviewers to read |
| V-02 | Output format (prose + indented lists) | Replacing tables and ASCII art with structured prose improves copy-paste fidelity into docs/slides; may reduce scannability for engineers |
| V-03 | Lifecycle emphasis (compressed inertia) | Collapsing the 4-sub-section inertia to a single inline verdict saves token budget and time-to-diagram; risk of under-justified structure decisions |
| V-04 | Phrasing register (declarative/descriptive) | Replacing DO/MUST/DO NOT imperatives with descriptive instructions lowers reading friction; may reduce boundary-condition compliance |
| V-05 | Inertia framing (dominant) + Role sequence (PM-first) | Making STAY-FLAT the hard default that requires a named failure to overturn, combined with PM-first loading, produces the most defensible org design |

---

## V-01 — Role Sequence: PM-First Tier Order

**Axis:** Role sequence — PM / Design / Research load first, then Engineering, then Operations.
**Hypothesis:** When org design is being done in a product context, loading business/product roles before technical roles causes the model to frame areas and committees around customer value delivery rather than technical ownership — producing org charts that are easier for exec and PM reviewers to accept.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — PRODUCT-FIRST THREE-TIER CLASSIFICATION SEQUENCE

DO classify roles in this strict three-tier order:
  Tier 1: PM / Design / Research types first.
  Tier 2: Engineering types second.
  Tier 3: Operations and Other types last.
If no PM / Design / Research roles are present, begin with Engineering types.
If neither tier 1 nor tier 2 roles are present, classify all roles in any order.
DO NOT interleave tiers — complete all entries in one tier before writing any entry from the next tier.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] — [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table as `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format.

When all roles are classified, DO emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

DO produce a three-column mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header excluded).
IF count < 2: write the missing row(s) until count reaches 2.
THEN emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present.

Sub-section 2 — How We Coordinate Today

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 — Rebuttal

DO name the coordination failure the flat-team case cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT and Re-assessment Trigger

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
After the pressure line, choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger naming a concrete threshold.
DO NOT write "revisit as the team grows."

When VERDICT is written, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes.
DO use role names from ROLES-LOADED or ROLES-NOTE only.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA — DECIDES / ESCALATES REQUIRED

DO produce a headcount table: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])`.
DO include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

DO produce a cadence table: `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS — FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO annotate each Membership role as `[role name] ([domain type])`, listing at minimum two roles.
DO populate Escalates with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate Quorum as: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it. DO NOT proceed to Org Evolution Roadmap until all four categories are populated:
  `cat-1 (Areas)` — all area names from Headcount table: `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — all names from Rhythm Table and Charters: `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — all DRI roles from the Operating Rhythm Table: `- [DRI role]`

ORG EVOLUTION ROADMAP

DO produce a trigger table: `Trigger | Structural Change | Type`.
DO NOT label it optional. DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category — a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH — TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap: `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with: `[element name] (cat-N) — [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO include at minimum two anti-pattern rows.

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE (PM/Design/Research tier first, then Engineering, then Operations/Other)
2. ROLE-TYPE-CLASSIFICATION
3. PHASE GATE: ROLES COMPLETE
4. Inertia Assessment (four sub-sections with row-count separator after Sub-section 1)
5. PHASE GATE: INERTIA COMPLETE
6. ASCII Org Diagram
7. PHASE GATE: STRUCTURE COMPLETE
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. PHASE GATE: CHARTERS COMPLETE
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap
14. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-02 — Output Format: Prose + Indented Lists

**Axis:** Output format — replace ASCII diagram with indented markdown hierarchy; replace Headcount, Rhythm, Charter, and Anti-Pattern tables with structured prose blocks.
**Hypothesis:** Prose and indented lists survive copy-paste into Google Docs, Notion, and PowerPoint without table formatting artifacts; exec reviewers often prefer narrative structure to dense tables. Risk: harder to scan quickly for gap analysis.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description]`.
DO NOT invent role names unless no roles files are found.
If no files are found, produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

DO classify roles in this strict order: `Engineering` types first, then `Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO assign each role exactly one domain type: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] — [domain type]`.
DO NOT skip this block.
When complete, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org structure.
DO structure it in this order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

DO produce a three-column mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Type column MUST use only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO include at minimum two data rows.
After writing the table, count the data rows and emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator is present.

Sub-section 2 — How We Coordinate Today

DO describe active coordination patterns in prose. Name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 — Rebuttal

In one paragraph, name the coordination failure that flat structure cannot answer. Reference a specific observable.

Sub-section 4 — VERDICT

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [justification]`.
Rating MUST be one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference the pressure rating in the reasoning.
Write a re-assessment trigger naming a concrete threshold.

When VERDICT is written, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

INDENTED ORG HIERARCHY (replaces ASCII diagram)

DO produce an indented markdown list showing the org hierarchy. Use `##`, `###`, and `####` headers or nested bullet points to represent reporting levels. Show at minimum two levels.
DO show committees as separate entries, not embedded inside areas.
DO use role names from ROLES-LOADED or ROLES-NOTE only.

Example format:
```
- CEO / Lead
  - Area: Product
    - PM Lead (PM)
    - Designer (Design)
  - Area: Engineering
    - Eng Lead (Engineering)
  - Committee: Architecture Board
    - Eng Lead (Engineering)
    - PM Lead (PM)
```

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA — PROSE FORMAT

For each area, write a prose paragraph in this format:
**[Area Name]** — [N] headcount. Key roles: [role name] ([domain type]), [role name] ([domain type]). Decides: [decision types owned here]. Escalates: [decision types referred upward, naming the destination].

DO cover at minimum two areas. End with: **Total headcount: [N]**.

OPERATING RHYTHM — PROSE FORMAT

DO describe each standing meeting in this format:
**[Cadence Name]** ([Frequency]) — DRI: [role from ROLES-LOADED]. Purpose: [one sentence]. 

DO include at minimum three cadences: an ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two cadences into one entry.

COMMITTEE CHARTERS — FIVE FIELDS, PROSE FORMAT

For each governance meeting described in the rhythm section, write a charter block:

**[Committee Name]**
- **Purpose:** [one sentence]
- **Membership:** [role name] ([domain type]), [role name] ([domain type]) — list at minimum two roles
- **Decides:** [decision types owned by this committee]
- **Escalates:** [decision types referred upward, naming the destination]
- **Quorum:** [N] of [M] member roles required for binding decisions

DO NOT label any charter optional.
DO NOT write `everything not listed under Decides` in the Escalates field.
DO NOT omit the Quorum field from any charter.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate:
  `cat-1 (Areas)` — each area: `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — each: `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — each DRI role: `- [DRI role]`

ORG EVOLUTION ROADMAP — PROSE FORMAT

For each trigger, write:
**Trigger:** [condition]. **Structural Change:** [what changes]. **Type:** [Headcount Threshold / Workload Signal / Structural Symptom / Milestone Event].

DO include at minimum two entries. Row 1: headcount threshold. Row 2: a different category.

ANTI-PATTERN WATCH — PROSE FORMAT

For each anti-pattern, write:
**[Anti-Pattern Name]** — Why it applies: `[element name] (cat-N) — [one sentence of specific relevance]`. Mitigation: [one sentence].

MUST open each "Why it applies" with the `[element name] (cat-N)` typed citation syntax.
DO include at minimum two anti-patterns.

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. PHASE GATE: ROLES COMPLETE
4. Inertia Assessment
5. PHASE GATE: INERTIA COMPLETE
6. Indented Org Hierarchy
7. PHASE GATE: STRUCTURE COMPLETE
8. Headcount by Area (prose)
9. Operating Rhythm (prose)
10. Committee Charters (prose blocks)
11. PHASE GATE: CHARTERS COMPLETE
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap (prose)
14. Anti-Pattern Watch (prose)

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-03 — Lifecycle Emphasis: Compressed Inertia

**Axis:** Lifecycle emphasis — collapse the 4-sub-section inertia assessment to a single inline FLAT-OR-STRUCTURE verdict (one paragraph + rating + trigger). Remove Sub-section 1 mechanism table, Sub-section 2 inventory, Sub-section 3 rebuttal. All remaining sections unchanged.
**Hypothesis:** Skipping the structured steelman saves ~30% of token budget on setup, produces faster time-to-diagram, and reduces output length for teams who already know they need structure. Risk: org decisions are less defensible in review; the mechanism table is the most frequently cited evidence in org design reviews.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description]`.
DO NOT invent role names unless no roles files are found.
If no files are found, produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

DO classify roles in this strict order: `Engineering` types first, then `Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO assign each role exactly one domain type: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] — [domain type]`.
DO annotate each Key Roles cell in Headcount by Area and each Membership field in Charters as `[role name] ([domain type])`.

When complete, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — INLINE VERDICT (compressed)

DO write a single paragraph (3–5 sentences) addressing:
  (a) The strongest argument for staying flat — name at least one concrete coordination mechanism currently in use.
  (b) The coordination failure that flat structure cannot answer — name a specific observable.

MUST then emit the pressure line immediately after the paragraph:
`FLAT-CASE-PRESSURE: [rating] — [one-sentence justification referencing the mechanism named above and the failure mode named above]`.
Rating MUST be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

MUST then choose exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reference the FLAT-CASE-PRESSURE rating by name in the reasoning sentence.

DO write a re-assessment trigger naming a concrete threshold immediately after the verdict.
DO NOT write "revisit as the team grows."

When VERDICT is written, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes.
DO use role names from ROLES-LOADED or ROLES-NOTE only.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA — DECIDES / ESCALATES REQUIRED

DO produce a headcount table: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])`.
DO include at minimum two area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE

DO produce a cadence table: `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.

COMMITTEE CHARTERS — FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO annotate each Membership role as `[role name] ([domain type])`, at minimum two roles.
DO populate Escalates with a named destination.
DO NOT write `everything not listed under Decides.`
Quorum format: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`

ORG EVOLUTION ROADMAP

DO produce a trigger table: `Trigger | Structural Change | Type`.
DO include at minimum two rows. Row 1: headcount threshold. Row 2: different category.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH — TYPED CITATIONS REQUIRED

DO produce: `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with: `[element name] (cat-N) — [specific relevance]`.
DO include at minimum two anti-pattern rows.

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. PHASE GATE: ROLES COMPLETE
4. Inertia Assessment (inline verdict — one paragraph + FLAT-CASE-PRESSURE line + verdict + trigger)
5. PHASE GATE: INERTIA COMPLETE
6. ASCII Org Diagram
7. PHASE GATE: STRUCTURE COMPLETE
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. PHASE GATE: CHARTERS COMPLETE
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap
14. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-04 — Phrasing Register: Declarative / Descriptive

**Axis:** Phrasing register — replace all DO / MUST / DO NOT imperative constraints with descriptive instructions ("The output includes...", "Each entry shows...", "The section answers..."). Phase gates remain, but use present-tense description rather than command form.
**Hypothesis:** Descriptive register reduces the cognitive load of reading the prompt for non-engineers and produces outputs that read less like a compliance checklist; however, boundary conditions ("DO NOT write X") may be missed more often, particularly the Quorum fraction format and the typed citation syntax.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

Before writing anything else, check `.craft/roles/` for role definition files.

The output begins with a `ROLES-LOADED:` block listing each role found: `- [role name] — [one-line description from role file]`. Role names come from the files — no invented names. If no files are found, the block is labeled `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` and lists reasonable inferred roles for this domain.

Nothing else is written until the ROLES-LOADED or ROLES-NOTE block is complete.

ROLE-LOAD-ORDER

Roles are classified in three tiers, in this order: Engineering types first, Operations types second, then PM / Design / Research / Other types. No interleaving between tiers.

ROLE-TYPE-CLASSIFICATION

Immediately after ROLES-LOADED or ROLES-NOTE, a `ROLE-TYPE-CLASSIFICATION:` block lists each role with its domain type from this set: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`. Every role gets exactly one type. Key Roles cells in the Headcount table and Membership fields in Charters show the annotation `[role name] ([domain type])`.

When classification is complete, the output includes: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT

The inertia assessment runs before any org diagram is drawn. It covers four sub-sections in order.

Sub-section 1 — Case for Staying Flat

A three-column mechanism evidence table shows the existing coordination that makes formal structure unnecessary: `Mechanism Name | Type | Frequency / Participants`. The Type column uses only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`. At least two data rows appear. After the table, the count of data rows is stated, and the sub-section closes with: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

A prose or list inventory of active coordination patterns — channels, cadences, informal roles, and artifacts — shows how the team currently manages dependencies. Entries already in the Sub-section 1 table are not repeated here.

Sub-section 3 — Rebuttal

A short paragraph names the specific coordination failure that the flat-team case cannot handle: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap. The failure is named concretely, not described generically.

Sub-section 4 — VERDICT

The verdict opens with the pressure line: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing the mechanism count from Sub-section 1 and the failure mode from Sub-section 3]`. The rating is exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

The verdict declaration follows: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`, with a reasoning sentence that references the FLAT-CASE-PRESSURE rating by name.

A re-assessment trigger names a concrete threshold — not "revisit as the team grows."

When the verdict is written, the output includes: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

After the inertia phase gate, an ASCII hierarchy shows the org structure with at least two levels. Committees appear as distinct labeled nodes rather than embedded in area boxes. Role names come from ROLES-LOADED or ROLES-NOTE.

When the diagram is complete: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

A headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates` covers each org area. The Decides column shows decision types owned at this level. The Escalates column shows decision types referred upward, naming the destination role or forum. Key Roles entries follow the `[role name] ([domain type])` annotation from ROLE-TYPE-CLASSIFICATION. At least two area rows appear, plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

A cadence table with columns `Cadence | Frequency | DRI / Owner | Purpose` covers the standing meeting structure. At least three distinct cadences appear: an ROB, a shiproom or gate review, and a governance meeting. No two meetings are combined into one row. DRI / Owner entries reference roles from ROLES-LOADED where possible.

COMMITTEE CHARTERS

Each governance meeting listed in the rhythm table has a charter with all five fields:
- **Purpose** — what the committee exists to decide
- **Membership** — at least two roles listed as `[role name] ([domain type])`
- **Decides** — decision types owned by this committee
- **Escalates** — decision types referred upward, named destination
- **Quorum** — written as `Quorum: [N] of [M] member roles required for binding decisions`

The Escalates field names a specific destination — not "everything not listed under Decides." The Quorum field appears in every charter without exception.

When all charters are written: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

An `ORG-ELEMENT REGISTER` block immediately follows the charters phase gate with four categories:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`

ORG EVOLUTION ROADMAP

A trigger table with columns `Trigger | Structural Change | Type` shows the conditions under which this org design changes. At least two rows appear: the first is a headcount threshold trigger; the second comes from a different category (workload signal, structural symptom, or milestone event). Two headcount thresholds as the only rows is not sufficient.

ANTI-PATTERN WATCH

An anti-pattern table with columns `Anti-Pattern | Why It Applies Here | Mitigation` closes the analysis. Each `Why It Applies Here` cell opens with the typed citation format: `[element name] (cat-N) — [one sentence of specific relevance]`. The cat-N code matches the ORG-ELEMENT REGISTER category schema. At least two anti-patterns appear.

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. PHASE GATE: ROLES COMPLETE
4. Inertia Assessment (four sub-sections)
5. PHASE GATE: INERTIA COMPLETE
6. ASCII Org Diagram
7. PHASE GATE: STRUCTURE COMPLETE
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. PHASE GATE: CHARTERS COMPLETE
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap
14. Anti-Pattern Watch

No section begins before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-05 — Inertia Framing (Dominant) + Role Sequence (PM-First) [Combination]

**Axes:** Inertia framing (dominant — FLAT is the default; STRUCTURE requires a named failure to unlock) + Role sequence (PM / Design / Research first).
**Hypothesis:** Treating STAY-FLAT as the hard default and requiring a named failure mode to unlock the org diagram — combined with PM-first role loading — produces the most defensible org designs. Teams using this variation will draw fewer unnecessary structures and will have explicit written evidence for every design decision. The cost is extra friction: org diagrams are blocked until the inertia gate passes, and the gate requires more than a generic growth argument.

```
You are running `/org-chart {topic}`.

DESIGN PHILOSOPHY: FLAT IS THE DEFAULT

This skill treats staying flat as the correct answer until a specific coordination failure is named. Org structure is a tax on communication. The default verdict is CAN-OPERATE-FLAT. STRUCTURE-WARRANTED requires naming the failure mode explicitly. If the failure cannot be named, the org diagram section is replaced with a FLAT-RECOMMENDED notice.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — PRODUCT-FIRST THREE-TIER CLASSIFICATION SEQUENCE

DO classify roles in this strict order:
  Tier 1: PM / Design / Research types.
  Tier 2: Engineering types.
  Tier 3: Operations and Other types.
DO NOT interleave tiers. Complete each tier fully before starting the next.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO assign each role exactly one type: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`.
DO NOT skip this block. DO NOT proceed until every role is classified.
DO annotate Key Roles cells in Headcount by Area as `[role name] ([domain type])`.
DO annotate Membership fields in Charters in the same format.

When complete, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FLAT IS DEFAULT, FAILURE MODE REQUIRED TO UNLOCK STRUCTURE

The inertia assessment is the primary output of this skill when the org is small. Four sub-sections run in strict order.

Sub-section 1 — Case for Staying Flat (STEELMAN — write this as if you are advocating for it)

DO write the strongest possible case for not adding structure. Identify the concrete mechanisms that make informal coordination work today.
DO produce the three-column mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
The Type column MUST use only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO include at minimum two data rows.

After the table: count data rows.
IF count < 2: write the missing row(s).
THEN emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator.

Sub-section 2 — How We Coordinate Today

Inventory active coordination patterns — channels, cadences, informal roles, artifacts — with frequency and participants. DO NOT re-list the Sub-section 1 table entries.

Sub-section 3 — Rebuttal (STRUCTURE UNLOCK CONDITION)

MUST name one specific, observable coordination failure. The failure must be concrete:
  - A blocked decision: naming the decision and who was blocked
  - A missed SLA: naming the SLA and the miss
  - A time-zone gap: naming the teams and the coverage hole
  - A knowledge silo: naming the knowledge and who holds it exclusively
  - A competing roadmap: naming the roadmap conflict and which teams

DO NOT write "the team is growing" as the failure mode without naming the specific thing that broke.
DO NOT write "the team needs more structure" — this is not an observable failure.

IF the failure cannot be named with this specificity: DO NOT emit the STRUCTURE-WARRANTED verdict. The verdict MUST be CAN-OPERATE-FLAT.

Sub-section 4 — VERDICT and Re-assessment Trigger

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and the failure mode from Sub-section 3, or noting that no specific failure was identified]`.
Rating MUST be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

DO choose exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
  - If pressure is Strong (5) or Moderate (4) AND no specific failure was named: verdict MUST be `CAN-OPERATE-FLAT`.
  - If a specific failure was named AND pressure is Weak (3) or lower: verdict MUST be `STRUCTURE-WARRANTED`.
  - If pressure is Strong (5) or Moderate (4) AND a specific failure was named: judgment call, explain the tension.

The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger naming a concrete, measurable threshold. DO NOT write "revisit as the team grows."

CONDITIONAL GATE — FLAT VS STRUCTURE PATH

IF verdict is `CAN-OPERATE-FLAT`:
  DO emit: `=== [PHASE GATE: FLAT RECOMMENDED — ORG DIAGRAM SKIPPED] ===`
  DO write a FLAT-RECOMMENDED notice with three items:
    1. The coordination mechanisms to preserve (from Sub-section 1 table)
    2. The signals to watch that would change this verdict (name 2–3 concrete observables)
    3. The recommended re-assessment date or threshold
  DO skip the ASCII Org Diagram, Headcount by Area, Operating Rhythm, and Committee Charters sections.
  DO skip to the ORG-ELEMENT REGISTER (flat variant — see below).
  DO produce the Org Evolution Roadmap and Anti-Pattern Watch sections.

IF verdict is `STRUCTURE-WARRANTED`:
  DO emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
  DO proceed to ASCII Org Diagram and all subsequent sections.

ASCII ORG DIAGRAM (STRUCTURE-WARRANTED path only)

DO draw an ASCII hierarchy after the inertia phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes.
DO use role names from ROLES-LOADED or ROLES-NOTE only.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA (STRUCTURE-WARRANTED path only)

DO produce: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single Decision Scope column.
DO annotate Key Roles as `[role name] ([domain type])`.
DO include at minimum two area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE (STRUCTURE-WARRANTED path only)

DO produce: `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.

COMMITTEE CHARTERS (STRUCTURE-WARRANTED path only)

For each governance meeting in the rhythm table, write a charter with all five fields:
`Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
Membership lists at minimum two roles annotated as `[role name] ([domain type])`.
Escalates names a specific destination.
Quorum format: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

STRUCTURE-WARRANTED path:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`

CAN-OPERATE-FLAT path (flat variant):
  `cat-1 (Coordination Mechanisms)` — list each mechanism from Sub-section 1 table: `- [mechanism name] ([type])`
  `cat-2 (Informal Roles)` — list any informal roles identified: `- [role name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (Watch Signals)` — list the 2–3 re-assessment signals from the FLAT-RECOMMENDED notice: `- [signal]`

ORG EVOLUTION ROADMAP

DO produce: `Trigger | Structural Change | Type`.
DO include at minimum two rows. Row 1: headcount threshold. Row 2: a different category.
On the FLAT path, "Structural Change" describes what form the structure would take when triggered (e.g., "Add an Engineering Lead with dedicated area").

ANTI-PATTERN WATCH — TYPED CITATIONS REQUIRED

DO produce: `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with: `[element name] (cat-N) — [specific relevance]`.
The cat-N code MUST match the ORG-ELEMENT REGISTER category used in this run (flat variant or structured variant).
DO include at minimum two anti-patterns.

SECTION ORDER (STRUCTURE-WARRANTED path)

1. ROLES-LOADED or ROLES-NOTE (PM/Design/Research tier first)
2. ROLE-TYPE-CLASSIFICATION
3. PHASE GATE: ROLES COMPLETE
4. Inertia Assessment (four sub-sections with row-count separator)
5. PHASE GATE: INERTIA COMPLETE
6. ASCII Org Diagram
7. PHASE GATE: STRUCTURE COMPLETE
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. PHASE GATE: CHARTERS COMPLETE
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap
14. Anti-Pattern Watch

SECTION ORDER (CAN-OPERATE-FLAT path)

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. PHASE GATE: ROLES COMPLETE
4. Inertia Assessment (four sub-sections)
5. PHASE GATE: FLAT RECOMMENDED — ORG DIAGRAM SKIPPED
6. FLAT-RECOMMENDED notice (preserve / watch / threshold)
7. ORG-ELEMENT REGISTER (flat variant)
8. Org Evolution Roadmap
9. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## Round 3 Variation Index

| ID | Primary Axis | Secondary Axis | Key Structural Change | Expected Strength | Expected Risk |
|----|-------------|----------------|----------------------|-------------------|---------------|
| V-01 | Role sequence (PM-first) | — | Tier order: PM/Design/Research → Engineering → Operations | Exec-readable org framing | May underweight technical ownership areas |
| V-02 | Output format (prose + indent) | — | No tables; no ASCII art; all prose blocks | Clean copy-paste; doc-friendly | Harder to diff/scan; charter compliance harder to verify |
| V-03 | Lifecycle emphasis (compressed inertia) | — | Inertia = 1 paragraph + 1 pressure line; no mechanism table | Faster time-to-diagram; less token cost | Weaker justification; inertia gate may pass trivially |
| V-04 | Phrasing register (declarative) | — | All DO/MUST/DO NOT → descriptive present-tense | Lower reading friction | Boundary conditions (Quorum format, typed citations) may degrade |
| V-05 | Inertia framing (dominant) | Role sequence (PM-first) | FLAT is hard default; failure mode required to unlock diagram; two output paths | Most defensible design; eliminates unnecessary structure | Higher refusal rate for diagram generation; requires richer input |
