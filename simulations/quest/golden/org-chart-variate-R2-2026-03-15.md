---
skill: quest-variate
skill_target: org-chart
date: 2026-03-15
round: R2
rubric_version: v2
status: variate
---

# org-chart Variate — Round 2

**Date:** 2026-03-15
**Skill:** org-chart
**Rubric:** v2 (C-01 through C-13; essential C-01–C-05; aspirational now C-09–C-13)
**Round:** R2 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R1 ceiling:** V-05 scored 92 (60 essential + 30 recommended + 2 aspirational = C-13 only).
**R2 target:** Move aspirational from 1/5 to 3/5 (V-04) and 5/5 (V-05).

---

## Round 2 Variation Map

| V | Axis | What Changed vs R1 | Hypothesis |
|---|------|--------------------|------------|
| V-01 | steelman-enforcement | Inertia section requires a labeled "Case for Staying Flat" block with a numbered list of 2+ concrete reasons before any rebuttal may begin | The C-11 steelman failed in R1 not because V-05 lacked the slot, but because the slot had no minimum-bullet-count guard. A required list with a floor of 2 named reasons forces substantive defense rather than a token acknowledgment |
| V-02 | decides-escalates-architecture | Headcount table uses two mandatory columns (Decides / Escalates) instead of a single "Decision Scope" column; generic phrases explicitly disqualified | V-05/R1 used Decides/Escalates column labels in Phase 3 template, but actual runs substituted a single decision-scope description. Making the two-column split a hard architectural requirement with a named-failure rule forces C-12 |
| V-03 | aspirational-section-forcing | Adds two mandatory sections — "Org Evolution Roadmap" and "Anti-Pattern Watch" — with explicit output templates and failure conditions | C-09 and C-10 were never targeted in R1. Making them named deliverables with explicit templates (not suggestions) tests whether section-forcing is sufficient to elicit aspirational content that never appeared in the R1 set |
| V-04 | steelman-enforcement + decides-escalates-architecture + trigger-enforcement | Combines axes from V-01 and V-02, plus a hard requirement for a concrete re-assessment trigger in or adjacent to the VERDICT | Three new aspirational criteria (C-11 + C-12 + C-13) targeted simultaneously in a clean imperative format. Predicted score: 60 + 30 + 6 = 96 |
| V-05 | full-aspirational-contract | All five aspirational criteria (C-09 through C-13) explicitly contracted as named deliverables with per-criterion output templates and failure conditions | Maximum-coverage prompt. If the five-section aspirational contract yields 5/5, total score reaches 100. Falsifiable: if any aspirational section still fails despite explicit template, format-forcing is insufficient and the criteria require semantic depth instructions instead |

---

## V-01 — Steelman Enforcement: Labeled Defense with Minimum Bullet Count

**axis:** steelman-enforcement
**hypothesis:** The C-11 steelman slot existed in V-05/R1 Phase 2 but did not carry a minimum-content rule. A labeled "Case for Staying Flat" block with a floor of two numbered reasons — each required to name a specific working mechanism rather than acknowledge that one exists — will reliably pass C-11. Falsifiable: if two-reason bullets are still generic despite the explicit guard, minimum-count enforcement alone cannot substitute for content depth requirements.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

Check `.craft/roles/` for role files relevant to {topic} or the domain.

Produce a ROLES-LOADED block before writing anything else:

```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
  - [role name] — [one-line description]
  (one entry per role found)
```

If `.craft/roles/` is absent or empty, produce instead:

```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [inferred role name] — [one-line description]
  (list all inferred roles)
```

Do not proceed past this block until it is written.

---

INERTIA ASSESSMENT — THREE PARTS REQUIRED

The inertia assessment has three named parts. Write them in order. Do not begin a part
until the previous part is complete.

**Part 1 — Case for Staying Flat**

List the specific mechanisms that make informal coordination work today.
Each item must name a concrete mechanism, not a generic observation.

```
### Case for Staying Flat

1. [Mechanism — e.g., "single shared Slack channel resolves cross-team
   questions in under four hours without scheduled meetings"]
2. [Mechanism — e.g., "informal tech lead already arbitrates cross-cutting
   decisions; no authority gradient has been needed to date"]
(at minimum two items required; three or more earns stronger inertia coverage)
```

**Part 2 — Rebuttal**

Name the specific failure modes or pressure signals that the flat-team case cannot absorb:

```
### Rebuttal

[The coordination failure — named and specific — that the mechanisms in Part 1
cannot address. Not "the team is growing" but a named observable: e.g.,
"on-call coverage now spans three time zones, and informal arbitration delays
have caused two missed SLA events in the past quarter".]
```

**Part 3 — VERDICT and Re-assessment Trigger**

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences connecting Part 1 vs. Part 2 to this verdict]

Re-assessment trigger: [the concrete headcount threshold, milestone, or
coordination-failure signal that would flip this verdict — required regardless
of which verdict is chosen. Example: "if headcount exceeds 10" or "when
on-call rotation spans more than two distinct service areas".]
```

Do not write an org diagram until the VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT: produce a lightweight coordination model
(ownership map and sync cadence) rather than a formal org chart. Still include
an operating rhythm table and the re-assessment trigger.
If VERDICT is STRUCTURE-WARRANTED: proceed to the org diagram.

---

ASCII ORG DIAGRAM

Draw the hierarchy using role names from ROLES-LOADED or ROLES-NOTE.

Requirements:
- At least two levels
- At least two distinct nodes at the top level or second level
- Committees or boards shown as a separate labeled node — not embedded inside
  a single area's subtree
- Do not produce a flat list of names without hierarchy

---

HEADCOUNT BY AREA

Table with at minimum two areas and individual counts:

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|
| [name] | [N or N–M] | [role names from ROLES-LOADED] | [what this area decides vs. escalates] |
| [name] | [N or N–M] | [role names] | [what this area decides vs. escalates] |
| **Total** | **[N]** | | |

The Decision Scope column must describe specific decision types — not "owns the area."

---

OPERATING RHYTHM TABLE

Three or more distinct entries. Required coverage:
1. ROB or business review
2. Shiproom or equivalent feature-gate meeting
3. One governance meeting (architecture board, steering committee, or equivalent)

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Do not combine two meetings into one row to reach the three-entry minimum.
DRI / Owner should reference a role from ROLES-LOADED where possible.

---

COMMITTEE CHARTERS

For each governance meeting in the rhythm table, write a charter. The charter
section is enforced — it is not optional.

```
### [Committee name]

**Purpose:** [one sentence — what question does this committee answer?]
**Membership:** [roles from ROLES-LOADED — not personal names; at minimum two roles]
**Decides:** [decisions in scope for this committee]
**Escalates:** [decisions this committee refers upward]
```

At minimum two committees must have all four fields populated.

---

SECTION ORDER

Write sections in this exact order:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat → Rebuttal → VERDICT + Re-assessment Trigger)
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm Table
6. Committee Charters

---

FINAL LINE

```
Generated by: /org-chart {topic} — {date}
```

---

## V-02 — Decides/Escalates Architecture: Two-Column Decision Split

**axis:** decides-escalates-architecture
**hypothesis:** V-05/R1 Phase 3 template labeled columns "Decides" and "Escalates" but when run, outputs frequently substituted a single "Decision Scope" description — passing C-08 but failing C-12. Making the two-column split a hard architectural requirement with an explicit failure rule ("'owns X' does not pass either column") will reliably produce the distinct, concrete content that C-12 requires. Falsifiable: if Decides/Escalates entries are still abstract despite two-column enforcement, the problem is at the instruction level, not the structural level.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

Check `.craft/roles/` for role files relevant to {topic} or the domain.

Produce a ROLES-LOADED or ROLES-NOTE block before writing anything else.

ROLES-LOADED (when files found):
```
ROLES-LOADED:
  - [role name] — [one-line description]
  (one entry per role)
```

ROLES-NOTE (when absent):
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [inferred role name] — [purpose in this org]
```

Do not proceed until the block is written.

---

INERTIA ASSESSMENT

Answer the inertia question before drawing any org structure:
Can this team operate without a formal org?

Write a section titled "Inertia Assessment" with:
- Description of current coordination mechanisms (what meetings, channels, informal leads exist today)
- Flat-team viability threshold: the headcount or complexity level at which this type of team's informal coordination breaks down
- VERDICT: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
- Reasoning: one or two sentences connecting the current state and threshold to the verdict
- Re-assessment trigger: the specific condition that would flip this verdict (headcount threshold, coordination-failure signal, or milestone — not a vague "as the team grows")

Do not write an org diagram until the VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT: produce a lightweight coordination model (ownership map, sync cadence) instead of a full org chart.
If VERDICT is STRUCTURE-WARRANTED: proceed to the org diagram.

---

ASCII ORG DIAGRAM

Draw the hierarchy using role names from ROLES-LOADED or ROLES-NOTE.
Minimum: two levels, two distinct nodes at top or second level.
Committees: separate labeled node, not embedded inside one area.

---

HEADCOUNT BY AREA — DECIDES / ESCALATES SPLIT REQUIRED

This table uses five columns. The Decides and Escalates columns are mandatory and
distinct — they are not interchangeable with a single "Decision Scope" description.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N–M] | [roles] | [decision type 1, decision type 2] | [decision type that goes upward] |
| [name] | [N or N–M] | [roles] | [decision type 1, decision type 2] | [decision type that goes upward] |
| **Total** | **[N]** | | | |

Rules:
- At minimum two area rows with individual counts — no single undifferentiated total only
- Decides column: list decision types owned at this level (e.g., "prioritization within the sprint backlog," "architecture changes below the service boundary")
- Escalates column: list decision types referred upward (e.g., "cross-service contract changes," "headcount additions")
- "Owns the area" does not pass either column — name the decision types explicitly
- A single sentence describing scope does not pass C-12 — Decides and Escalates must be populated as separate columns with distinct, concrete content

---

OPERATING RHYTHM TABLE

Three or more distinct entries. Required coverage:
1. ROB or business review
2. Shiproom or equivalent feature-gate meeting
3. One governance meeting (architecture board, steering committee, or equivalent)

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Do not combine two meetings into one row. DRI / Owner references a role from ROLES-LOADED.

---

COMMITTEE CHARTERS

For each governance meeting in the rhythm table, write a charter. This section
is enforced — do not label it optional.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles, not names — at minimum two roles]
**Decides:** [what is in scope]
**Escalates:** [what this committee refers upward]
```

At minimum two charters with all four fields populated.

---

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (with VERDICT and re-assessment trigger)
3. ASCII Org Diagram
4. Headcount by Area (with Decides / Escalates columns)
5. Operating Rhythm Table
6. Committee Charters

---

FINAL LINE

```
Generated by: /org-chart {topic} — {date}
```

---

## V-03 — Aspirational Section Forcing: Evolution Roadmap + Anti-Pattern Watch

**axis:** aspirational-section-forcing
**hypothesis:** C-09 (org evolution path) and C-10 (anti-patterns flagged) were never targeted in R1. They are not incidental to the core skill — they require distinct, named sections to elicit the concrete growth triggers and specific anti-pattern callouts that the rubric requires. Making "Org Evolution Roadmap" and "Anti-Pattern Watch" mandatory named sections with explicit output templates tests whether section-forcing is the lever, not just aspirational encouragement. Falsifiable: if the sections appear but still score as vague ("the org will evolve"), the problem is that this content requires scenario knowledge the model lacks at prompt time, not a structural issue.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

Check `.craft/roles/` for role files relevant to {topic} or the domain. Produce a ROLES-LOADED or ROLES-NOTE block before writing anything else.

```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

Or if absent:

```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

Do not proceed until this block is written.

---

INERTIA ASSESSMENT

Before writing any org structure, answer: can this team operate without a formal org?

Write a section titled "Inertia Assessment" containing:
- How the team coordinates today (informal mechanisms, existing leads, channels)
- Flat-team viability threshold for this type of team
- VERDICT: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
- Reasoning: specific to this team's size and coordination mode
- Re-assessment trigger: the concrete condition that would flip this verdict

Do not write an org diagram until the VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT: produce a lightweight coordination model and skip to the Operating Rhythm section.
If VERDICT is STRUCTURE-WARRANTED: proceed in order through all sections.

---

ASCII ORG DIAGRAM

Draw the hierarchy using role names from ROLES-LOADED or ROLES-NOTE.
Minimum: two levels, two distinct nodes. Committees as separate labeled nodes.

---

HEADCOUNT BY AREA

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|
| [name] | [N or N–M] | [roles] | [what this area decides vs. escalates] |
| [name] | [N or N–M] | [roles] | [what this area decides vs. escalates] |
| **Total** | **[N]** | | |

Minimum two area rows. Decision Scope must describe specific decision types, not "owns the area."

---

OPERATING RHYTHM TABLE

Three or more distinct entries covering ROB, a shiproom, and a governance meeting.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Do not combine meetings into one row.

---

COMMITTEE CHARTERS

For each governance meeting, write a charter (enforced, not optional):

**[Name]**
Purpose: [one sentence]
Membership: [roles from ROLES-LOADED — not names]
Decides: [in scope] / Escalates: [out of scope]

---

ORG EVOLUTION ROADMAP — REQUIRED

Describe how the proposed structure should change as the team grows. This section
is a mandatory deliverable, not an addendum.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Rationale |
|---------|-------------------|-----------|
| [headcount threshold or workload signal — e.g., "when headcount exceeds 12"] | [what splits, what is added — e.g., "Platform sub-team becomes a separate area with its own lead"] | [why this trigger is the right inflection point] |
| [second trigger] | [structural change] | [rationale] |
```

Requirements:
- At minimum two rows, each with a concrete headcount threshold or named workload signal
- The structural change column must name what changes (new area, committee goes standing, etc.)
- "The org will evolve" is not a valid entry — name the trigger and the change

---

ANTI-PATTERN WATCH — REQUIRED

Identify org anti-patterns that are specifically risky given the proposed structure.
This section is a mandatory deliverable, not a generic risk note.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern — e.g., "shiproom without a DRI"] | [One sentence on why this pattern is a risk for this specific org design — not a generic warning] | [One sentence on how the proposed structure avoids or monitors for it] |
| [Second named anti-pattern] | [Why it applies here] | [Mitigation] |
```

Requirements:
- At minimum one named anti-pattern with a one-sentence domain-specific rationale
- Named anti-patterns include (but are not limited to): "committee capture," "too many dotted lines," "shiproom without a DRI," "org mirroring Conway's Law without intent," "governance theater"
- Generic warnings like "watch for communication breakdowns" do not pass

---

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (with VERDICT and re-assessment trigger)
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm Table
6. Committee Charters
7. Org Evolution Roadmap
8. Anti-Pattern Watch

---

FINAL LINE

```
Generated by: /org-chart {topic} — {date}
```

---

## V-04 — Steelman + Decides/Escalates + Re-assessment Trigger: Three Aspirational Criteria Combined

**axis:** steelman-enforcement + decides-escalates-architecture + trigger-enforcement
**hypothesis:** The three new v2 aspirational criteria (C-11: steelman, C-12: D/E split, C-13: re-assessment trigger) target three distinct output locations (inertia section, headcount table, VERDICT field). A prompt that enforces all three in an imperative DO/DO NOT register — while preserving the V-04/R1 essential coverage — should produce a reliable 3/5 aspirational score. Predicted composite: 60 + 30 + 6 = 96. Falsifiable: if all three enforcement points are present but scoring still misses any one criterion, the failure is in output quality rather than structural presence.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT — STEELMAN FIRST, THEN VERDICT

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact sub-section order:

**Sub-section 1 — Case for Staying Flat**

DO list the specific working mechanisms that make informal coordination viable.
DO include at minimum two numbered reasons.
DO NOT write generic statements like "the team communicates well."
Each reason must name a mechanism (channel, informal lead, decision pattern, cadence).

```
### Case for Staying Flat

1. [Specific mechanism — e.g., "weekly standup plus a shared backlog resolves
   sprint-level cross-team dependencies without escalation"]
2. [Specific mechanism — e.g., "a single senior engineer acts as informal
   architecture arbiter, and no cross-cutting decision has been blocked or
   delayed by lack of formal authority"]
(at minimum two; DO NOT proceed until at least two are written)
```

**Sub-section 2 — Rebuttal**

DO name the coordination failure the flat-team case cannot answer.
DO NOT write "the team is growing" without specifying the failure mode.
DO reference a specific observable: a blocked decision, a missed SLA, a time-zone gap,
a knowledge silo, a competing roadmap.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Sub-section 3 — VERDICT and Re-assessment Trigger**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting sub-sections 1 and 2 to the verdict.
DO write a re-assessment trigger immediately after the verdict.
DO NOT write "revisit as the team grows" — the trigger must name a threshold.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences — specific, not generic]

Re-assessment trigger: [concrete condition — e.g., "when headcount exceeds 12"
or "when on-call rotation spans more than two distinct service areas" or
"when the first cross-team dependency causes a shipped regression"]
```

DO NOT proceed past this sub-section until VERDICT and re-assessment trigger are both written.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE — do not introduce new role names.

---

HEADCOUNT BY AREA — DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns — Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column — the Decides and Escalates columns are separate and both required.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N–M] | [roles] | [decision types owned here] | [decision types escalated] |
| [name] | [N or N–M] | [roles] | [decision types owned here] | [decision types escalated] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

---

COMMITTEE CHARTERS

DO write a charter for each governance meeting in the rhythm table.
DO include all four fields: Purpose, Membership, Decides, Escalates.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED — at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward]
```

---

SECTION ORDER — DO NOT REORDER

DO write sections in this order:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat → Rebuttal → VERDICT + Re-assessment Trigger)
3. ASCII Org Diagram
4. Headcount by Area (Decides / Escalates columns)
5. Operating Rhythm Table
6. Committee Charters

DO NOT reorder sections.
DO NOT omit any of the six sections.

---

FINAL LINE

DO end with exactly:

```
Generated by: /org-chart {topic} — {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-05 — Full Aspirational Contract: All Five Criteria Explicitly Templated

**axis:** lifecycle-emphasis + output-format + full-aspirational-contract
**hypothesis:** V-05/R1 earned 1/5 aspirational because C-11 and C-12 templates existed but were not reliably followed in output, and C-09/C-10 were never targeted. A prompt that gives every aspirational criterion its own named phase with an explicit output contract and a stated failure condition will produce the first 5/5 aspirational run (10 pts), bringing the theoretical maximum to 100. Falsifiable: if the five-section aspirational contract still fails any criterion, the failure is semantic depth (the model lacks domain knowledge at run time), not structural — and the conclusion is that aspirational criteria require dynamic context, not static contract enforcement.

---

You are running `/org-chart {topic}`.

Complete the following six phases in order. Do not begin a phase until the previous
phase deliverable is written.

---

PHASE 1 — READ ROLES

**Deliverable:** ROLES-LOADED or ROLES-NOTE table

Read `.craft/roles/` for role files relevant to {topic} or the domain.

If files are found:
```
## Roles Input

Source: .craft/roles/{domain}/

| Role | Archetype | Orientation (one line) |
|------|-----------|------------------------|
| [name] | [product/technical/challenger/etc.] | [from role file] |
```

If absent:
```
## Roles Input

Source: inferred (no .craft/roles/ files found for this domain)

| Role | Archetype | Orientation (one line) |
|------|-----------|------------------------|
| [inferred name] | [archetype] | [purpose in this org] |
```

Phase 1 complete when: table is written with at least one row.

---

PHASE 2 — INERTIA ASSESSMENT

**Deliverable:** Inertia Assessment section with VERDICT and re-assessment trigger

The assessment has five mandatory sub-sections:

```
## Inertia Assessment

### Case for Staying Flat

List the specific working mechanisms that make informal coordination viable today.
Present the strongest case for NOT formalizing structure.

1. [Specific mechanism — name it concretely, not generically]
2. [Second specific mechanism]
(at minimum two items; each must name a real coordination pattern, not acknowledge
that coordination exists)

### Switching Cost

What does formalizing cost? Be specific:
[reporting overhead, slower decision paths, political weight of titles,
coordination tax of scheduled meetings over ad-hoc resolution]

### Flat-Team Viability Threshold

[The headcount or complexity level at which informal coordination fails for
this type of team. State whether the team is currently below, at, or above
this threshold.]

### Rebuttal

[The named coordination failure or growth pressure that the Case for Staying Flat
cannot answer. Must be a specific observable — not "the team is growing."]

### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences connecting the Case vs. Rebuttal to this verdict]

Re-assessment trigger: [concrete condition that would flip this verdict — headcount
threshold, coordination-failure event, or named milestone. Example: "when headcount
exceeds 10" or "when the on-call rotation first spans more than two service areas"
or "when cross-team dependency failures reach two per sprint." Vague language such
as "revisit as the team grows" does not satisfy this requirement.]
```

Phase 2 complete when: all five sub-sections are written, VERDICT and re-assessment
trigger are both present.

If VERDICT is CAN-OPERATE-FLAT: produce a lightweight coordination model (ownership
map, sync cadence) and proceed directly to Phase 4. Skip Phase 3.
If VERDICT is STRUCTURE-WARRANTED: proceed to Phase 3.

---

PHASE 3 — DESIGN STRUCTURE

**Deliverable:** ASCII Org Diagram + Headcount by Area (with Decides / Escalates split)

Draw the org hierarchy using role names from Phase 1:

```
## Org Structure

[ASCII diagram — at minimum two levels, at minimum two distinct top-level or
second-level nodes, committees shown as separate labeled nodes]
```

Immediately after the diagram, produce the headcount table with a five-column format.
The Decides and Escalates columns are separate, mandatory, and distinct:

```
## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N–M] | [roles from Phase 1] | [decision types owned at this level] | [decision types referred upward] |
| [name] | [N or N–M] | [roles from Phase 1] | [decision types owned at this level] | [decision types referred upward] |
| **Total** | **[N]** | | | |
```

Decides / Escalates rules:
- Each column must list named decision types — not "owns X" or generic scope descriptions
- At minimum two area rows with individual counts
- A single "Decision Scope" column does not satisfy this requirement even if it contains decision language

Phase 3 complete when: diagram and headcount table with Decides/Escalates are written.

---

PHASE 4 — DOCUMENT RHYTHMS AND CHARTER COMMITTEES

**Deliverable:** Operating Rhythm Table + Committee Charters

```
## Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose | Type |
|---------|-----------|-------------|---------|------|
| ROB | [freq] | [role] | Review business health, surface escalations | business-review |
| [Shiproom] | [freq] | [role] | Gate for ship/no-ship decisions | shiproom |
| [Architecture Board] | [freq] | [role] | Technical governance, cross-cutting standards | governance |
| [additional rows as needed] | | | | |
```

For every governance-type row, write a charter immediately after the table:

```
### [Committee name]

**Purpose:** [one sentence — what question does this committee answer?]

**Membership:**
  - [role from Phase 1] — [why this role attends]
  - [role] — [reason]
  (all standing members by role, not by name)

**Decides:**
  - [specific decision type 1]
  - [specific decision type 2]

**Escalates:**
  - [specific decision type referred to a higher body or individual]
```

Charter requirements:
- All four fields (Purpose, Membership, Decides, Escalates) must be present per committee
- Membership: at minimum two roles listed
- This section is enforced — not optional

Phase 4 complete when: three or more distinct rhythm rows and at least two charters
with all four fields are written.

---

PHASE 5 — ORG EVOLUTION ROADMAP

**Deliverable:** Concrete growth trigger table

This phase is mandatory. It is not an addendum.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Concrete headcount threshold or workload signal — e.g., "when headcount reaches 15"] | [Named structural change — e.g., "Platform sub-team splits into its own area with a dedicated lead"] | [split / add-area / standing-committee / add-layer] |
| [Second trigger] | [Named change] | [type] |
```

Requirements:
- At minimum two rows, each with a concrete trigger and a named structural change
- "The org will evolve" or "revisit as needed" does not pass — the trigger must name a threshold or signal
- The structural change column must specify what changes (a team splits, a committee becomes standing, a layer is added)

Phase 5 complete when: two or more rows with concrete triggers and named structural changes are written.

---

PHASE 6 — ANTI-PATTERN WATCH

**Deliverable:** Named anti-pattern table with domain-specific rationale

This phase is mandatory. It is not a generic risk section.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | [One sentence on why this pattern is a risk for this specific org design — not a generic warning] | [How the proposed structure avoids or monitors for it] |
```

Named anti-patterns to draw from (not limited to):
- Committee capture — a committee's scope grows until it owns decisions that should be delegated
- Too many dotted lines — matrix reporting diffuses accountability
- Shiproom without a DRI — ship/no-ship authority is shared, producing stalls
- Governance theater — meetings exist but have no decision authority
- Org mirroring Conway's Law without intent — structure reflects team boundaries, not user needs

Requirements:
- At minimum one named anti-pattern with a one-sentence domain-specific rationale
- The "Why It Applies Here" column must reference the specific org design — not a generic statement
- Two or more anti-patterns with domain-specific rationale earns full C-10 credit

Phase 6 complete when: at minimum one named anti-pattern with domain-specific rationale and mitigation is written.

---

ARTIFACT OUTPUT

Collect all phase deliverables into `org-chart.md` in this section order:
1. Roles Input (Phase 1)
2. Inertia Assessment (Phase 2)
3. Org Structure + Headcount by Area (Phase 3)
4. Operating Rhythm + Committee Charters (Phase 4)
5. Org Evolution Roadmap (Phase 5)
6. Anti-Pattern Watch (Phase 6)

---

FINAL LINE

```
Generated by: /org-chart {topic} — {date}
```
