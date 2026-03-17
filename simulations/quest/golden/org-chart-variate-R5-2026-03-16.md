---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R5
rubric_version: v4
status: variate
---

# org-chart Variate -- Round 5

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v4 (C-01--C-05 essential; R-01--R-03 recommended; A-01--A-09 aspirational /9)
**Round:** R5 -- first round against v4 rubric

**R4 outcome:** All 5 R4 variations scored 100/100 against v3. One new excellence pattern found:
V-01's coordination-cost column made FLAT-CASE-PRESSURE an arithmetic conclusion (-> A-08).
V-02's prose charters preserved all 5 required fields in paragraph form (-> A-09).
Rubric advanced to v4; dual convergence not yet confirmed. R5 must attempt 100/100 against v4.

**Known required elements (all R5 variations carry these):**
- Adversarial burden statement BEFORE any mechanics (A-03)
- PRE-FLIGHT CONTRACT with CF-NN codes; section headers cite satisfied codes (A-06)
- ANNOTATION-REGISTER with Used-In tracking column; reconciliation after CHARTERS gate (A-07)
- 4-column mechanism table (adds Estimated Coordination Cost); FLAT-CASE-CLOSED with total cost;
  FLAT-CASE-PRESSURE cites cost figure; re-assessment trigger in cost units (A-08)
- Committee Charters as structured prose paragraphs with bold field labels (A-09)
- VERDICT BRANCH: CAN-OPERATE-FLAT investment-note worked example per mechanism (A-04, R-02)
- Escalates affirmative exclusion clause -- "All matters outside [X] escalate to [named dest.]" (A-05, R-03)
- Phase gates at ROLES / INERTIA / STRUCTURE / CHARTERS boundaries (R-01)
- All 5 essential: Inertia 4-sub-sections (C-01), three structural artifacts (C-02),
  charters 5-fields + N-of-M Quorum (C-03), roles loaded + classified + propagated (C-04),
  annotation consistency (C-05)

---

## Round 5 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | Inertia framing | VERDICT emits a NET-COST-COMPARISON block comparing flat coordination cost against structure overhead; verdict declaration must align with the arithmetic conclusion unless an explicit override applies | The FLAT-CASE-PRESSURE rating and NET-COST-COMPARISON block are complementary signals: pressure captures qualitative concern, cost comparison captures quantitative justification. Requiring them to be explicitly reconciled eliminates verdict decisions that are qualitatively confident but arithmetically unsupported |
| V-02 | Lifecycle emphasis | Org Evolution Roadmap restructured into three named tiers -- Capacity, Process, Strategic -- with Observable Signal and Probability Weight (Low/Medium/High) columns; minimum 5 rows total | Single-dimension threshold triggers underspecify what to watch for. Three-tier categorization with observable signals and probability weights gives teams a structured watch list. Tests whether richer evolution design surfaces a new structural property not captured by A-02's concrete threshold requirement |
| V-03 | Output format | ASCII box-drawing org diagram replaced by an indented Markdown list hierarchy using only dashes and indentation; all structural requirements (2+ levels, committees as distinct named nodes) preserved | C-02 requires an "ASCII org diagram." An indented list IS ASCII. Tests whether C-02 and A-01 are format-agnostic (hierarchy visible, committees distinct) or accidentally tied to box-drawing characters |
| V-04 | A + B combined | NET-COST-COMPARISON block in VERDICT + three-tier evolution roadmap | The cost delta from the steelman feeds into probability weights in the evolution tiers. Tests whether arithmetic verdict precision and tiered evolution richness compound into a more coherent output |
| V-05 | A + B + C combined | Full integration: NET-COST-COMPARISON + three-tier evolution + indented-list org diagram | Maximum structural density. All three R5 axes plus all established patterns from prior rounds in a single coherent prompt |

---

## V-01 -- Net-Cost Verdict Arithmetic

**axis:** inertia framing -- arithmetic verdict via NET-COST-COMPARISON block
**hypothesis:** Requiring an explicit cost comparison in the VERDICT sub-section makes the pressure
rating falsifiable by arithmetic. FLAT-CASE-PRESSURE can assert "Strong (5)" qualitatively, but the
NET-COST-COMPARISON block forces: flat cost, structure overhead estimate, and a net delta. If the
delta says structure costs MORE, a "Strong (5)" pressure rating with STRUCTURE-WARRANTED becomes a
visible contradiction requiring an override justification.
Falsifiable: if cost estimates are too uncertain to produce meaningful deltas, the block adds noise
and prompts hedged values that weaken the verdict rather than sharpen it.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Every structural element you propose must earn its place by naming a specific coordination failure
it prevents. Before loading roles or drawing anything, commit to this posture: the case for
structure must be provable in hours-per-week, not just asserted in words.

---

PRE-FLIGHT CONTRACT

The following contract codes govern this output. Every major section header MUST cite the CF
code(s) it satisfies in the format `(satisfies CF-NN)` or `(satisfies CF-NN, CF-MM)`. A section
header without a citation is incomplete. A CF code with no citing section is a missing section.

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all others third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost column) >= 2 rows + FLAT-CASE-CLOSED separator citing total cost |
| CF-04 | Inertia: How We Coordinate Today -- distinct content from Sub-section 1; named frequency and participants |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating, cost-anchored) + NET-COST-COMPARISON block + verdict declaration + re-assessment trigger in cost units |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes, not embedded in one area |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: prose format; 5 fields; Quorum as N-of-M fraction; Escalates affirmative exclusion clause |
| CF-11 | ORG-ELEMENT REGISTER after CHARTERS gate with all 4 categories populated |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citation in every Why-It-Applies cell |

DO NOT begin any section until you have identified which CF code(s) it satisfies.
Write the citing CF codes in the section header before writing the section's content.

---

ROLES-LOADED (satisfies CF-01)

DO check `.craft/roles/` before writing anything.
Produce `ROLES-LOADED:` with one entry per role: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred entries.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, PM / Design / Research / Other
types third. DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.
DO NOT skip any role from the loaded list.
Annotate every Key Roles cell in the Headcount table as `[role name] ([domain type])`.
Annotate every Membership field in Committee Charters as `[role name] ([domain type])`.

ANNOTATION-REGISTER

Produce immediately after ROLE-TYPE-CLASSIFICATION:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [leave blank -- fill on first downstream cite] |

Fill Used-In when each role first appears in a downstream section (Key Roles or Membership).
After the CHARTERS phase gate, perform ANNOTATION-REGISTER RECONCILIATION: re-emit the full
table with all Used-In cells populated. Flag any blank Used-In as `PROPAGATION-GAP: [role name]`.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Write the Inertia Assessment before any org boxes.

Sub-section 1 -- Case for Staying Flat

Produce a FOUR-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`

Type MUST use only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Estimated Coordination Cost = person-hours per week consumed by this mechanism across participants
(e.g., "2 hrs/week, 5 people" or "30 min/occurrence x 3 people = ~1.5 hrs/week").
DO NOT leave any Coordination Cost cell blank.
Include at minimum two data rows.

After writing the table:
- Count data rows (header excluded). If count < 2, add rows until count >= 2.
- Sum the Estimated Coordination Cost column into a TOTAL FLAT COST figure: {total_flat_cost}.
- Emit exactly:
  `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {total_flat_cost} hrs/week across {Y} people. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2 and total is computed.

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns currently in active use.
Name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

Name the coordination failure the flat-team case and current mechanisms cannot answer.
Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap. DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

STEP 1: Emit the pressure rating line:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing total flat coordination cost from FLAT-CASE-CLOSED and the Sub-section 3 failure mode]`
Rating MUST be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit the cost figure from the justification. DO NOT emit NET-COST-COMPARISON before this line.

STEP 2: Emit the NET-COST-COMPARISON block immediately after the pressure line:

  NET-COST-COMPARISON:
    Flat coordination cost (from FLAT-CASE-CLOSED): {total_flat_cost} hrs/week
    Estimated structure overhead (standing meetings + coordination layer, first 90 days): {structure_overhead} hrs/week
    Net delta (flat minus overhead): {delta} hrs/week
    Arithmetic conclusion: STRUCTURE-SAVES {delta} hrs/week    [if delta > 0]
                        OR STRUCTURE-COSTS {|delta|} hrs/week MORE    [if delta <= 0]

If Arithmetic conclusion is STRUCTURE-SAVES: STRUCTURE-WARRANTED is arithmetically supported.
If Arithmetic conclusion is STRUCTURE-COSTS MORE: CAN-OPERATE-FLAT is arithmetically supported.

STEP 3: Emit the verdict declaration -- exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference both the FLAT-CASE-PRESSURE rating AND the NET-COST-COMPARISON delta.
If the verdict does not align with the arithmetic conclusion, state the override reason explicitly:
`VERDICT-OVERRIDE: [reason -- e.g., regulatory requirement, executive mandate, immovable deadline]`

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  Produce a coordination investment note for each mechanism in Sub-section 1:
  `[Mechanism Name] -- Investment: [specific action to preserve this mechanism] | Failure Signal: [observable breakdown indicator]`
  Re-assessment trigger: "Revisit when total weekly coordination overhead exceeds [{total_flat_cost} x 1.5] hrs/week
  or when [specific failure signal from investment notes] occurs more than [N] times in [period]."
  DO NOT proceed to org structure sections.

IF STRUCTURE-WARRANTED:
  Re-assessment trigger in cost units: "Reassess org structure if total standing-meeting overhead
  exceeds {total_flat_cost} hrs/week after 90 days, or if the rebuttal failure mode resolves
  without formal structure."
  DO NOT write "revisit as the team grows."

DO NOT proceed past VERDICT without: pressure line, NET-COST-COMPARISON block, verdict declaration,
branch content, and re-assessment trigger all written.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

Draw an ASCII hierarchy after the inertia phase gate.
Show at minimum two levels.
Show committees as distinct labeled nodes -- NOT embedded in one area's subtree.
Use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single Decision Scope column -- Decides and Escalates are SEPARATE REQUIRED columns.
Decides: decision types owned at this area level.
Escalates: decision types referred upward, naming the destination role or forum.
Annotate each Key Roles entry as `[role name] ([domain type])`. Update ANNOTATION-REGISTER Used-In.
Include >= 2 area rows plus a `**Total**` row.
DO NOT write "owns the area" or generic ownership phrases.

OPERATING RHYTHM TABLE (satisfies CF-09)

Produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include >= 3 distinct rows: one ROB, one shiproom or gate meeting, one governance meeting.
DO NOT combine two meetings into one row.
Reference a role from ROLES-LOADED in DRI / Owner where possible.

COMMITTEE CHARTERS -- PROSE FORMAT (satisfies CF-10)

Write a charter for EVERY governance meeting in the rhythm table.
Format: structured prose paragraphs with bold field labels.
Required fields in every charter paragraph:

  **Purpose:** [1-2 sentence committee mission statement]
  **Membership:** [role name (domain type), role name (domain type), ...] -- minimum two roles with domain-type annotations. Update ANNOTATION-REGISTER Used-In on first cite.
  **Decides:** [specific decision types owned by this committee]
  **Escalates:** All matters outside [the Decides scope listed above] escalate to [named destination role or forum].
  **Quorum:** [N] of [M] member roles required for binding decisions.

DO NOT use the short Quorum form ("N roles required"). The full fraction is required.
DO NOT write "everything not listed under Decides" in the Escalates field.
DO NOT omit any charter for any governance meeting in the rhythm table.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit the full ANNOTATION-REGISTER table with all Used-In cells populated from downstream sections.
Flag any role still showing a blank Used-In as: `PROPAGATION-GAP: [role name] -- no downstream cite found.`

ORG-ELEMENT REGISTER (satisfies CF-11)

Produce immediately after ANNOTATION-REGISTER RECONCILIATION:

ORG-ELEMENT REGISTER:
  cat-1 (Areas): `- [area name] -- headcount: [N]`  (one line per area from Headcount table)
  cat-2 (Committees/Cadences): `- [name]`  (one line per committee and cadence from Rhythm Table + Charters)
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`  (one line per DRI role from Rhythm Table)

ORG EVOLUTION ROADMAP (satisfies CF-12)

Produce a trigger table: `Trigger | Structural Change | Type`
Row 1: headcount threshold trigger.
Row 2: a different category -- workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH (satisfies CF-13)

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell MUST open with: `[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT write a cell that names an element without the (cat-N) typed syntax.
Use only cat-N codes that match the ORG-ELEMENT REGISTER category schema.
Include >= 2 anti-pattern rows.

---

SECTION ORDER:
1. ROLES-LOADED or ROLES-NOTE (CF-01)
2. ROLE-TYPE-CLASSIFICATION (CF-02)
3. ANNOTATION-REGISTER (initial -- Used-In blank)
4. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5. Inertia: Case for Staying Flat [4-col table + FLAT-CASE-CLOSED] (CF-03)
6. Inertia: How We Coordinate Today (CF-04)
7. Inertia: Rebuttal (CF-05)
8. Inertia: VERDICT [FLAT-CASE-PRESSURE + NET-COST-COMPARISON + declaration + branch + trigger] (CF-06)
9. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
10. ASCII Org Diagram (CF-07)
11. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
12. Headcount by Area (CF-08)
13. Operating Rhythm Table (CF-09)
14. Committee Charters -- prose format (CF-10)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ANNOTATION-REGISTER RECONCILIATION
17. ORG-ELEMENT REGISTER (CF-11)
18. Org Evolution Roadmap (CF-12)
19. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Three-Tier Evolution Roadmap

**axis:** lifecycle emphasis -- Org Evolution Roadmap restructured as three named tiers
**hypothesis:** The current two-row evolution roadmap captures the minimum required triggers
(headcount + one other). A three-tier structure (Capacity / Process / Strategic) with Observable
Signal and Probability Weight columns gives teams a watch list organized by concern category
and urgency. The tiered format may surface a new structural property: trigger prioritization --
which tier to watch first, and why. This is not captured by A-02 (concrete threshold) or the
current evolution roadmap criteria, which only require trigger diversity.
Falsifiable: if the three-tier structure does not produce materially different observable signals
per tier (all signals look like headcount), the categorization adds overhead without clarity.

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
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all others third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost) >= 2 rows + FLAT-CASE-CLOSED with total cost |
| CF-04 | Inertia: How We Coordinate Today -- distinct content; frequency and participants named |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating, cost-anchored) + verdict declaration + re-assessment trigger in cost units |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: prose format; 5 fields; Quorum as N-of-M fraction; Escalates affirmative exclusion clause |
| CF-11 | ORG-ELEMENT REGISTER after CHARTERS gate with all 4 categories |
| CF-12 | Org Evolution Roadmap: 3 tiers (Capacity / Process / Strategic); >= 5 rows total; Observable Signal and Probability Weight (Low/Medium/High) columns; WATCH-FIRST statement |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citation in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

DO check `.craft/roles/` before writing anything.
Produce `ROLES-LOADED:` with one entry per role: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:`.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, PM / Design / Research / Other third.
DO NOT interleave tiers.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.
Annotate Key Roles in Headcount as `[role name] ([domain type])`.
Annotate Membership in Charters as `[role name] ([domain type])`.

ANNOTATION-REGISTER

Produce immediately after classification:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [leave blank -- fill on first downstream cite] |

Fill Used-In on each role's first appearance downstream. Reconcile after the CHARTERS phase gate.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

Produce a FOUR-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`

Type MUST use only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Estimated Coordination Cost = person-hours per week across participants.
DO NOT leave any Coordination Cost cell blank.
Include at minimum two data rows.

After the table, count data rows (N) and sum the cost column ({total_flat_cost}).
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {total_flat_cost} hrs/week across {Y} people. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory coordination patterns with frequency and participants.
DO NOT re-list Sub-section 1 entries.

Sub-section 3 -- Rebuttal

Name one specific observable coordination failure the flat-team case cannot answer.
Reference: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing total coordination cost and the Sub-section 3 failure mode]`
Rating: exactly one of `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit the cost figure. DO NOT emit the verdict declaration before this line.

After the pressure line, emit exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.

VERDICT BRANCH:

IF CAN-OPERATE-FLAT:
  Produce a coordination investment note for each Sub-section 1 mechanism:
  `[Mechanism Name] -- Investment: [specific action] | Failure Signal: [observable breakdown indicator]`
  Re-assessment trigger: "Revisit when weekly coordination overhead exceeds [{total_flat_cost} x 1.5] hrs/week
  or when [failure signal] occurs more than [N] times in [period]."
  DO NOT proceed to org structure.

IF STRUCTURE-WARRANTED:
  Re-assessment trigger in cost units: "Reassess if total structure overhead exceeds {total_flat_cost} hrs/week
  after 90 days, or if the rebuttal failure mode resolves without formal structure."
  DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

Draw an ASCII hierarchy >= 2 levels. Committees as distinct labeled nodes -- NOT in one area's subtree.
Use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
Decides and Escalates are SEPARATE REQUIRED columns -- DO NOT merge.
Annotate Key Roles as `[role name] ([domain type])`. Update ANNOTATION-REGISTER Used-In.
Include >= 2 area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE (satisfies CF-09)

Produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include >= 3 rows: ROB, shiproom or gate, governance.
DO NOT combine meetings. Reference ROLES-LOADED in DRI / Owner.

COMMITTEE CHARTERS -- PROSE FORMAT (satisfies CF-10)

Write a charter for every governance meeting in the rhythm table.
Structured prose paragraphs with bold field labels:

  **Purpose:** [1-2 sentence mission]
  **Membership:** [role name (domain type), role name (domain type)] -- minimum two annotated roles. Update ANNOTATION-REGISTER Used-In.
  **Decides:** [specific decision types]
  **Escalates:** All matters outside [the Decides scope above] escalate to [named destination].
  **Quorum:** [N] of [M] member roles required for binding decisions.

Full N-of-M fraction required. Short form fails CF-10. Affirmative exclusion clause required.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit the ANNOTATION-REGISTER with all Used-In cells populated.
Flag any blank Used-In as: `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

ORG-ELEMENT REGISTER:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP -- THREE-TIER FORMAT (satisfies CF-12)

Produce a trigger table with five columns:
`Tier | Trigger | Observable Signal | Structural Change | Probability`

TIER 1 -- CAPACITY: Triggers driven by team size, headcount, or load limits.
  Include at minimum two rows under Tier 1.
  Observable Signal: a specific metric or observable (e.g., "avg PR review wait > 3 days").
  Probability: Low / Medium / High based on current trajectory.

TIER 2 -- PROCESS: Triggers driven by coordination failure, decision latency, or process breakdown.
  Include at minimum two rows under Tier 2.
  Observable Signal: a specific observable coordination symptom (e.g., "cross-area decisions take > 2 weeks").

TIER 3 -- STRATEGIC: Triggers driven by market, leadership, or milestone events.
  Include at minimum one row under Tier 3.
  Observable Signal: a specific strategic event or milestone (e.g., "Series B closes", "regulatory approval received").

Total rows across all three tiers: >= 5.
DO NOT use two nearly-identical headcount triggers. Tiers must be clearly distinct.
After the table, identify the WATCH-FIRST tier: which tier's triggers are most likely to fire
in the next 6 months based on current context? State the tier name and a one-sentence rationale.

ANTI-PATTERN WATCH (satisfies CF-13)

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`
Each "Why It Applies Here" cell MUST open with: `[element name] (cat-N) -- [one sentence]`
Include >= 2 rows.

---

SECTION ORDER:
1. ROLES-LOADED or ROLES-NOTE (CF-01)
2. ROLE-TYPE-CLASSIFICATION (CF-02)
3. ANNOTATION-REGISTER (initial)
4. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5. Inertia: Case for Staying Flat (CF-03)
6. Inertia: How We Coordinate Today (CF-04)
7. Inertia: Rebuttal (CF-05)
8. Inertia: VERDICT [FLAT-CASE-PRESSURE + declaration + branch + trigger] (CF-06)
9. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
10. ASCII Org Diagram (CF-07)
11. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
12. Headcount by Area (CF-08)
13. Operating Rhythm Table (CF-09)
14. Committee Charters -- prose (CF-10)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ANNOTATION-REGISTER RECONCILIATION
17. ORG-ELEMENT REGISTER (CF-11)
18. Org Evolution Roadmap -- three-tier (CF-12)
19. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Indented-Tree Org Diagram

**axis:** output format -- indented Markdown list hierarchy instead of ASCII box-drawing
**hypothesis:** The rubric C-02 requires an "ASCII org diagram" with >= 2 levels and committees
as distinct labeled nodes. An indented list is technically ASCII (uses only plain ASCII characters).
The question this variation tests: is C-02's intent about structural representation (hierarchy
visible, committees distinct) or about box-drawing character style? If an indented-list diagram
satisfies C-02 and A-01 with equal reliability as a box diagram, the rubric criteria are
format-agnostic. This matters for skill robustness -- box-drawing diagrams are fragile to
token counting and line-wrap issues in many output contexts.
Falsifiable: if reviewers judge the indented-list format as "not an org diagram," C-02 fails,
indicating the rubric criterion must be made explicit about acceptable diagram formats.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Every structural element must earn its place. Before drawing anything, ask: what specific
coordination failure would exist without this element?

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all others third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost) >= 2 rows + FLAT-CASE-CLOSED with total cost |
| CF-04 | Inertia: How We Coordinate Today -- distinct content |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating, cost-anchored) + declaration + re-assessment trigger in cost units |
| CF-07 | Org diagram as indented Markdown list hierarchy >= 2 levels; committees as distinct labeled list items with (Committee) marker; DIAGRAM-FORMAT: INDENTED-LIST declared in section header |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: prose format; 5 fields; Quorum as N-of-M fraction; Escalates affirmative exclusion clause |
| CF-11 | ORG-ELEMENT REGISTER after CHARTERS gate with all 4 categories |
| CF-12 | Org Evolution Roadmap >= 2 rows from different trigger categories |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citation in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

DO check `.craft/roles/` before writing anything.
Produce `ROLES-LOADED:` with one entry per role: `- [role name] -- [one-line description]`.
If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:`.

ROLE-LOAD-ORDER: Engineering types first, Operations types second, PM / Design / Research / Other third.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] -- [domain type]`.
Annotate Key Roles as `[role name] ([domain type])`.
Annotate Charter Membership as `[role name] ([domain type])`.

ANNOTATION-REGISTER

Produce immediately after classification:

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [leave blank -- fill on first downstream cite] |

Fill Used-In on first downstream cite. Reconcile after the CHARTERS phase gate.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

Produce a FOUR-column mechanism evidence table:
`Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`
Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact` only.
Estimated Coordination Cost = person-hours per week. No blank cells.
Include >= 2 data rows.

After the table, count rows (N) and sum cost ({total_flat_cost}).
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {total_flat_cost} hrs/week across {Y} people. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Inventory active coordination patterns. DO NOT re-list Sub-section 1.

Sub-section 3 -- Rebuttal

Name one specific observable coordination failure.

Sub-section 4 -- VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing total cost and failure mode]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

Emit CAN-OPERATE-FLAT or STRUCTURE-WARRANTED with reasoning citing FLAT-CASE-PRESSURE rating.

IF CAN-OPERATE-FLAT:
  Per-mechanism investment note: `[Mechanism] -- Investment: [action] | Failure Signal: [observable]`
  Re-assessment trigger: "Revisit when overhead exceeds [{total_flat_cost} x 1.5] hrs/week or when [signal] > [N] times in [period]."

IF STRUCTURE-WARRANTED:
  Re-assessment trigger in cost units. DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ORG DIAGRAM -- INDENTED-LIST FORMAT (satisfies CF-07)

DIAGRAM-FORMAT: INDENTED-LIST

Produce the org hierarchy as an indented Markdown list. Use only dashes (`-`) and indentation.
DO NOT use ASCII box-drawing characters (no `+`, `|`, `--`, `[  ]`).

Format rules:
- Level 0 (root): the domain or product name
- Level 1: reporting areas (indented 2 spaces under root)
- Level 2+: sub-areas and committees (indented 2 spaces per level)
- Committees: labeled with `(Committee)` marker to distinguish from org areas

Example:
  - [Domain Name]
    - [Area A]
      - [Sub-team or role cluster]
    - [Area B]
    - [Governance Layer]
      - [Committee X] (Committee)
      - [Committee Y] (Committee)

Show at minimum two hierarchy levels.
Committees must be distinct labeled items -- NOT merged into an area's description.
Use only role/area names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

Produce: `Area | Headcount | Key Roles | Decides | Escalates`
Decides and Escalates: SEPARATE REQUIRED columns.
Annotate Key Roles as `[role name] ([domain type])`. Update ANNOTATION-REGISTER Used-In.
Include >= 2 area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE (satisfies CF-09)

Produce: `Cadence | Frequency | DRI / Owner | Purpose`
Include >= 3 rows: ROB, shiproom/gate, governance. DO NOT combine meetings.

COMMITTEE CHARTERS -- PROSE FORMAT (satisfies CF-10)

Write a charter for every governance meeting in the rhythm table.
Structured prose with bold field labels:

  **Purpose:** [1-2 sentence mission]
  **Membership:** [role name (domain type), ...] -- minimum two annotated roles. Update ANNOTATION-REGISTER.
  **Decides:** [specific decision types]
  **Escalates:** All matters outside [the Decides scope above] escalate to [named destination].
  **Quorum:** [N] of [M] member roles required for binding decisions.

Full N-of-M required. Affirmative exclusion clause required.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit ANNOTATION-REGISTER with all Used-In populated.
Flag blanks as: `PROPAGATION-GAP: [role name]`.

ORG-ELEMENT REGISTER (satisfies CF-11)

ORG-ELEMENT REGISTER:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP (satisfies CF-12)

`Trigger | Structural Change | Type`
Row 1: headcount threshold. Row 2: workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH (satisfies CF-13)

`Anti-Pattern | Why It Applies Here | Mitigation`
Each cell: `[element name] (cat-N) -- [one sentence]`. >= 2 rows.

---

SECTION ORDER:
1. ROLES-LOADED or ROLES-NOTE (CF-01)
2. ROLE-TYPE-CLASSIFICATION (CF-02)
3. ANNOTATION-REGISTER (initial)
4. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5-8. Inertia Assessment (CF-03--CF-06)
9. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
10. Org Diagram -- indented-list format (CF-07)
11. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
12. Headcount by Area (CF-08)
13. Operating Rhythm Table (CF-09)
14. Committee Charters -- prose (CF-10)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ANNOTATION-REGISTER RECONCILIATION
17. ORG-ELEMENT REGISTER (CF-11)
18. Org Evolution Roadmap (CF-12)
19. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Net-Cost Verdict + Three-Tier Evolution (Axes A + B)

**axes:** inertia framing (A) + lifecycle emphasis (B)
**hypothesis:** The cost delta from NET-COST-COMPARISON feeds naturally into the Probability
Weight column in the three-tier evolution roadmap. If structure overhead already approaches flat
cost (small positive delta), Capacity tier triggers should be rated High probability -- the org
is already near the breakeven point and any headcount or load increase pushes coordination cost
past the delta threshold. Testing whether arithmetic verdict precision and tiered evolution
richness compound into a more internally consistent output.
Falsifiable: if the NET-COST-COMPARISON delta does not propagate into evolution tier probability
weights (the two sections remain independent), the combination produces no compounding benefit.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Make the case with arithmetic. Design evolution triggers you can actually observe and measure.

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all others third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost) >= 2 rows + FLAT-CASE-CLOSED with total cost |
| CF-04 | Inertia: How We Coordinate Today -- distinct content |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating, cost-anchored) + NET-COST-COMPARISON block + declaration + re-assessment trigger in cost units |
| CF-07 | ASCII org diagram >= 2 hierarchy levels; committees as distinct labeled nodes |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: prose format; 5 fields; Quorum N-of-M; Escalates affirmative clause |
| CF-11 | ORG-ELEMENT REGISTER after CHARTERS gate |
| CF-12 | Org Evolution Roadmap: 3 tiers (Capacity / Process / Strategic); >= 5 rows; Observable Signal + Probability columns; COST-DELTA ANNOTATION on Capacity tier; WATCH-FIRST statement |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citations |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

Check `.craft/roles/`. Produce `ROLES-LOADED:` or `ROLES-NOTE:`.
ROLE-LOAD-ORDER: Engineering -> Operations -> PM/Design/Research/Other. No tier interleaving.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

`- [role name] -- [domain type]` for each role.
One type from: `Engineering / PM / Design / Operations / Research / Other`.
Annotate Key Roles and Charter Membership as `[role name] ([domain type])`.

ANNOTATION-REGISTER

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [pending] |

Fill Used-In on first downstream cite. Reconcile after CHARTERS gate.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

FOUR-column table: `Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`
Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`. No blank cost cells.
>= 2 data rows. Count rows (N) and sum cost ({total_flat_cost}).
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {total_flat_cost} hrs/week across {Y} people. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Active coordination inventory. DO NOT re-list Sub-section 1.

Sub-section 3 -- Rebuttal

One specific observable coordination failure.

Sub-section 4 -- VERDICT

STEP 1: `FLAT-CASE-PRESSURE: [rating] -- [justification citing {total_flat_cost} and failure mode]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

STEP 2: NET-COST-COMPARISON block:

  NET-COST-COMPARISON:
    Flat coordination cost: {total_flat_cost} hrs/week
    Structure overhead (meetings + coordination layer): {structure_overhead} hrs/week
    Net delta: {delta} hrs/week
    Arithmetic conclusion: STRUCTURE-SAVES {delta}   OR   STRUCTURE-COSTS {|delta|} MORE

Save {net_delta} for use in the three-tier evolution roadmap COST-DELTA ANNOTATION.

STEP 3: Verdict declaration (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) citing FLAT-CASE-PRESSURE
rating and NET-COST-COMPARISON delta.
VERDICT-OVERRIDE: [reason] if verdict contradicts arithmetic conclusion.

IF CAN-OPERATE-FLAT:
  Per-mechanism investment note: `[Mechanism] -- Investment: [action] | Failure Signal: [observable]`
  Re-assessment at [{total_flat_cost} x 1.5] hrs/week. DO NOT proceed to structure.

IF STRUCTURE-WARRANTED:
  Re-assessment trigger in cost units. DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ASCII ORG DIAGRAM (satisfies CF-07)

Draw ASCII hierarchy >= 2 levels. Committees as distinct labeled nodes.
Use only role names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

`Area | Headcount | Key Roles | Decides | Escalates`
Decides and Escalates SEPARATE. Annotate Key Roles. >= 2 area rows + Total.

OPERATING RHYTHM TABLE (satisfies CF-09)

`Cadence | Frequency | DRI / Owner | Purpose`
>= 3 rows: ROB, shiproom/gate, governance.

COMMITTEE CHARTERS -- PROSE FORMAT (satisfies CF-10)

Charter for every governance meeting. Bold field labels:

  **Purpose:** [mission]
  **Membership:** [role name (type), ...] -- >= 2 annotated roles. Update ANNOTATION-REGISTER.
  **Decides:** [decision types]
  **Escalates:** All matters outside [Decides scope] escalate to [named destination].
  **Quorum:** [N] of [M] member roles required for binding decisions.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit with all Used-In populated. Flag blanks as PROPAGATION-GAP.

ORG-ELEMENT REGISTER (satisfies CF-11)

  cat-1 (Areas): `- [area] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP -- THREE-TIER WITH COST-DELTA ANNOTATION (satisfies CF-12)

Produce: `Tier | Trigger | Observable Signal | Structural Change | Probability`

TIER 1 -- CAPACITY (>= 2 rows):
  Triggers driven by team size or load limits.
  COST-DELTA ANNOTATION: if {net_delta} < 2 hrs/week (structure barely saves vs. flat), mark all
  Capacity tier Probability cells as High -- the team is already near cost breakeven and any
  headcount or load increase pushes coordination cost past the delta threshold.
  If {net_delta} >= 5 hrs/week, mark Capacity tier base Probability as Medium.
  Observable Signal: a specific capacity metric (e.g., "PR review queue > 4 days avg wait").

TIER 2 -- PROCESS (>= 2 rows):
  Triggers driven by coordination failure or decision latency.
  Observable Signal: specific coordination symptom (e.g., "cross-area decision takes > 2 weeks").
  Probability calibrated to how frequently the Sub-section 3 rebuttal failure mode currently occurs.

TIER 3 -- STRATEGIC (>= 1 row):
  Triggers driven by market, product, or organizational milestone.
  Observable Signal: a named event or threshold (e.g., "headcount doubles", "second product launched").

Total rows: >= 5 across all tiers.
WATCH-FIRST: After the table, name the tier most likely to fire in the next 6 months.
Cite the {net_delta} figure as part of the rationale: "At {net_delta} hrs/week net savings,
Tier [X] is [most / second most] likely because ..."

ANTI-PATTERN WATCH (satisfies CF-13)

`Anti-Pattern | Why It Applies Here | Mitigation`
Each cell: `[element name] (cat-N) -- [one sentence]`. >= 2 rows.

---

SECTION ORDER:
1. ROLES-LOADED / ROLES-NOTE (CF-01)
2. ROLE-TYPE-CLASSIFICATION (CF-02)
3. ANNOTATION-REGISTER
4. Phase gate: ROLES COMPLETE
5. Inertia: Case for Staying Flat (CF-03)
6. Inertia: How We Coordinate Today (CF-04)
7. Inertia: Rebuttal (CF-05)
8. Inertia: VERDICT [FLAT-CASE-PRESSURE + NET-COST-COMPARISON + declaration + branch + trigger] (CF-06)
9. Phase gate: INERTIA COMPLETE
10. ASCII Org Diagram (CF-07)
11. Phase gate: STRUCTURE COMPLETE
12. Headcount by Area (CF-08)
13. Operating Rhythm Table (CF-09)
14. Committee Charters -- prose (CF-10)
15. Phase gate: CHARTERS COMPLETE
16. ANNOTATION-REGISTER RECONCILIATION
17. ORG-ELEMENT REGISTER (CF-11)
18. Org Evolution Roadmap -- three-tier with cost-delta annotation (CF-12)
19. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration (Axes A + B + C)

**axes:** net-cost verdict (A) + three-tier evolution (B) + indented-list diagram (C)
**hypothesis:** All three R5 axes combined with all established excellence patterns from
prior rounds. The indented-list diagram test (C) is independent of the arithmetic and evolution
improvements (A, B) -- they can be combined without interference. The combination tests whether
maximum structural density produces a coherent, highest-scoring output or whether the three axes
produce conflicting instructions that create compliance gaps.
Falsifiable: if the combination produces a C-02 failure (indented-list diagram deemed non-compliant)
or any other structural gap, the full-integration prompt requires mitigation to coordinate the axes.

---

You are running `/org-chart {topic}`.

**The burden of proof is on structure, not on flatness. Flatness has inertia advantage.**
Make the case with arithmetic. Design evolution triggers by tier. Represent hierarchy clearly --
box-drawing is not required when indented structure communicates the same information.

---

PRE-FLIGHT CONTRACT

| Code | Requirement |
|------|-------------|
| CF-01 | ROLES-LOADED or ROLES-NOTE block before any other section |
| CF-02 | ROLE-TYPE-CLASSIFICATION in three-tier order: Engineering first, Operations second, all others third |
| CF-03 | Inertia: Case for Staying Flat -- 4-column mechanism table (with Coordination Cost) >= 2 rows + FLAT-CASE-CLOSED with total cost |
| CF-04 | Inertia: How We Coordinate Today -- distinct content |
| CF-05 | Inertia: Rebuttal -- one specific observable coordination failure |
| CF-06 | Inertia: VERDICT -- FLAT-CASE-PRESSURE (closed-set rating, cost-anchored) + NET-COST-COMPARISON block + declaration + re-assessment trigger in cost units |
| CF-07 | Org hierarchy as indented Markdown list >= 2 levels; committees as distinct labeled list items with (Committee) marker; DIAGRAM-FORMAT: INDENTED-LIST declared in section header |
| CF-08 | Headcount: Decides and Escalates as separate columns; >= 2 area rows + Total |
| CF-09 | Operating rhythm >= 3 distinct rows: ROB, shiproom/gate, governance |
| CF-10 | Committee Charters: prose format; 5 fields; Quorum N-of-M fraction; Escalates affirmative exclusion clause |
| CF-11 | ORG-ELEMENT REGISTER after CHARTERS gate with all 4 categories |
| CF-12 | Org Evolution Roadmap: 3 tiers (Capacity / Process / Strategic); >= 5 rows; Observable Signal + Probability; COST-DELTA ANNOTATION on Capacity tier; WATCH-FIRST statement |
| CF-13 | Anti-Pattern Watch with typed (cat-N) citation in every Why-It-Applies cell |

Each section header cites `(satisfies CF-NN)`. A CF code with no citing section is a missing section.

---

ROLES-LOADED (satisfies CF-01)

Check `.craft/roles/`. Produce `ROLES-LOADED:` or `ROLES-NOTE:`.
ROLE-LOAD-ORDER: Engineering -> Operations -> PM/Design/Research/Other. No interleaving.

ROLE-TYPE-CLASSIFICATION (satisfies CF-02)

`- [role name] -- [domain type]` for each role.
One type from: `Engineering / PM / Design / Operations / Research / Other`.
Annotate Key Roles and Charter Membership as `[role name] ([domain type])`.

ANNOTATION-REGISTER

| Role Name | Domain Type | Used In |
|-----------|-------------|---------|
| [role]    | [type]      | [pending] |

Fill Used-In on first downstream cite. Reconcile after CHARTERS gate.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

---

INERTIA ASSESSMENT (satisfies CF-03, CF-04, CF-05, CF-06)

Sub-section 1 -- Case for Staying Flat

FOUR-column table: `Mechanism Name | Type | Frequency / Participants | Estimated Coordination Cost`
Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`. No blank cost cells.
>= 2 data rows. Count (N) and sum ({total_flat_cost}).
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows. Total estimated coordination cost: {total_flat_cost} hrs/week across {Y} people. How We Coordinate Today begins.] ---`

Sub-section 2 -- How We Coordinate Today

Active coordination inventory. DO NOT re-list Sub-section 1.

Sub-section 3 -- Rebuttal

One specific observable coordination failure.

Sub-section 4 -- VERDICT

STEP 1: `FLAT-CASE-PRESSURE: [rating] -- [justification citing {total_flat_cost} and failure mode]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

STEP 2: NET-COST-COMPARISON block:

  NET-COST-COMPARISON:
    Flat coordination cost: {total_flat_cost} hrs/week
    Structure overhead: {structure_overhead} hrs/week
    Net delta: {delta} hrs/week
    Arithmetic conclusion: STRUCTURE-SAVES {delta}   OR   STRUCTURE-COSTS {|delta|} MORE

Save {net_delta} for COST-DELTA ANNOTATION in the three-tier evolution roadmap.

STEP 3: Verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) citing FLAT-CASE-PRESSURE rating and delta.
VERDICT-OVERRIDE: [reason] if verdict contradicts arithmetic conclusion.

IF CAN-OPERATE-FLAT:
  Per-mechanism investment note: `[Mechanism] -- Investment: [action] | Failure Signal: [observable]`
  Re-assessment at [{total_flat_cost} x 1.5] hrs/week. DO NOT proceed to structure.

IF STRUCTURE-WARRANTED:
  Re-assessment trigger in cost units. DO NOT write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

---

ORG DIAGRAM -- INDENTED-LIST FORMAT (satisfies CF-07)

DIAGRAM-FORMAT: INDENTED-LIST

Produce the org hierarchy as an indented Markdown list using only dashes and indentation.
DO NOT use ASCII box-drawing characters (+, |, --, [  ]).

Structure:
- Level 0 (root): domain or product name
- Level 1: reporting areas (2-space indent)
- Level 2+: sub-areas and committees (2-space per additional level)
- Committees: labeled with `(Committee)` marker to distinguish from org areas

Example:
  - [Domain]
    - [Area A]
      - [Sub-team]
    - [Governance Layer]
      - [Committee X] (Committee)

>= 2 hierarchy levels. Committees as distinct labeled list items.
Use only role/area names from ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

---

HEADCOUNT BY AREA (satisfies CF-08)

`Area | Headcount | Key Roles | Decides | Escalates`
Decides and Escalates SEPARATE. Annotate Key Roles. >= 2 area rows + **Total**.

OPERATING RHYTHM TABLE (satisfies CF-09)

`Cadence | Frequency | DRI / Owner | Purpose`
>= 3 rows: ROB, shiproom/gate, governance. No merged meetings.

COMMITTEE CHARTERS -- PROSE FORMAT (satisfies CF-10)

Charter for every governance meeting. Bold field labels:

  **Purpose:** [1-2 sentence mission]
  **Membership:** [role name (domain type), ...] -- >= 2 annotated roles. Update ANNOTATION-REGISTER.
  **Decides:** [decision types]
  **Escalates:** All matters outside [the Decides scope above] escalate to [named destination].
  **Quorum:** [N] of [M] member roles required for binding decisions.

Full N-of-M required. Affirmative exclusion clause required.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

---

ANNOTATION-REGISTER RECONCILIATION

Re-emit with all Used-In populated. Flag blanks as PROPAGATION-GAP.

ORG-ELEMENT REGISTER (satisfies CF-11)

  cat-1 (Areas): `- [area] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP -- THREE-TIER WITH COST-DELTA ANNOTATION (satisfies CF-12)

`Tier | Trigger | Observable Signal | Structural Change | Probability`

TIER 1 -- CAPACITY (>= 2 rows):
  COST-DELTA ANNOTATION: if {net_delta} < 2 hrs/week -> all Capacity triggers: High.
  If {net_delta} >= 5 hrs/week -> Capacity base Probability: Medium.
  Observable Signal: specific capacity metric (e.g., "PR review queue > 4 days avg wait").

TIER 2 -- PROCESS (>= 2 rows):
  Triggers from coordination failure or decision latency.
  Observable Signal: specific coordination symptom.
  Probability calibrated to Sub-section 3 failure mode frequency.

TIER 3 -- STRATEGIC (>= 1 row):
  Triggers from market or organizational milestone.
  Observable Signal: named event.

Total: >= 5 rows.
WATCH-FIRST: Name the tier most likely to fire in 6 months; cite {net_delta} in rationale.

ANTI-PATTERN WATCH (satisfies CF-13)

`Anti-Pattern | Why It Applies Here | Mitigation`
Each cell: `[element name] (cat-N) -- [one sentence]`. >= 2 rows.

---

SECTION ORDER:
1. ROLES-LOADED / ROLES-NOTE (CF-01)
2. ROLE-TYPE-CLASSIFICATION (CF-02)
3. ANNOTATION-REGISTER
4. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
5. Inertia: Case for Staying Flat (CF-03)
6. Inertia: How We Coordinate Today (CF-04)
7. Inertia: Rebuttal (CF-05)
8. Inertia: VERDICT [FLAT-CASE-PRESSURE + NET-COST-COMPARISON + declaration + branch + trigger] (CF-06)
9. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
10. Org Diagram -- indented-list format (CF-07)
11. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
12. Headcount by Area (CF-08)
13. Operating Rhythm Table (CF-09)
14. Committee Charters -- prose (CF-10)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ANNOTATION-REGISTER RECONCILIATION
17. ORG-ELEMENT REGISTER (CF-11)
18. Org Evolution Roadmap -- three-tier + cost-delta annotation (CF-12)
19. Anti-Pattern Watch (CF-13)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
