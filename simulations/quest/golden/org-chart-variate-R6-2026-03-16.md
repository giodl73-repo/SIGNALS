---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R6
rubric_version: v6-C24
status: variate
---

# org-chart Variate — Round 6

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v6 (C-01 through C-22; C-21 adds Flat Operating Rhythm table in CAN-OPERATE-FLAT
branch; C-22 adds row cap and governance prohibition on that table)
**Round:** R6 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R5 ceiling under v6:**
V-01/R5 drops to 98.57 under v6 — fails C-21 (flat branch uses prose sync cadence, no table)
and C-22 (no table means no row cap or governance prohibition to apply).
V-02/R5 holds 100.0 under v6 — Flat Operating Rhythm table present (Block B), maximum two rows
stated, governance meeting row explicitly prohibited. It is the confirmed baseline.

**R6 target:** Confirm V-02/R5 as V-01/R6 canonical baseline. Explore the open question from
the rubric header: does V-03/R5's inertia-to-evolution alignment guard close a real gap? If so,
it is a C-23 candidate. Two single-axis variations test: (1) the inertia-to-evolution alignment
guard (does Row 1 of the Evolution Roadmap need to be anchored to the Condition from slot 4?),
and (2) the DRI/Owner column mandate in the Flat Operating Rhythm table (C-21 allows a bare PASS
without DRI population; a mandate closes the roles-propagation gap in the flat branch).

---

## Round 6 Variation Map

| V | Axis | What Changed vs V-02/R5 | Hypothesis |
|---|------|------------------------|------------|
| V-01 | lifecycle-emphasis (V-02/R5 confirmed baseline) | V-02/R5 rewritten under v6 rubric context; C-21/C-22 satisfied by Flat Operating Rhythm table (Block B) with max-two-row constraint and governance prohibition | V-02/R5 holds 100.0 under v6. R6 confirms it as the baseline. Falsifiable: if any of C-09, C-12, C-19, C-20, C-21, or C-22 drop, the baseline is not clean and R6 must isolate the regression. |
| V-02 | lifecycle-emphasis (inertia-to-evolution alignment guard) | V-01/R6 base plus an explicit alignment guard: Evolution Roadmap Row 1 headcount threshold must be at or beyond the Condition from slot 4 — the two commitments cannot diverge | The inertia Condition and Evolution Roadmap Row 1 are currently independent. A model satisfying V-01/R6 can write "Condition: headcount reaches 12" in slot 4 and "Row 1: when headcount reaches 8" in the roadmap without contradiction. The two thresholds describe the same growth event at different scales, and a lower Row 1 threshold would have already passed. The alignment guard closes the divergence by requiring Row 1 to name a threshold at or beyond slot 4's Condition. Candidate for C-23. Falsifiable: if the guard over-constrains Row 1 (produces trivially-derived triggers that merely restate the Condition), the guard adds verbosity without discrimination. |
| V-03 | output format (DRI/Owner column mandatory in Flat Operating Rhythm table) | V-01/R6 base plus an explicit DRI/Owner mandate in Block B: each row must name a role from ROLES-LOADED; blank DRI entries are not permitted | C-21 requires a Flat Operating Rhythm table but treats the DRI/Owner column as "expected but not required for a bare PASS." This leaves role propagation optional in the flat branch. C-10 (role names in two or more sections) tests the STRUCTURE-WARRANTED path; the flat branch has no equivalent enforcement. Mandating the DRI column forces roles from ROLES-LOADED to propagate into the flat output, closing the C-10 gap for flat-verdict outputs. Falsifiable: if the mandate produces phantom roles (model invents roles when ROLES-LOADED is sparse), it introduces inaccuracy. |
| V-04 | lifecycle + output format (alignment guard + DRI mandate) | V-01/R6 with both the inertia-to-evolution alignment guard (V-02 axis) and the DRI/Owner mandate in Block B (V-03 axis) | Direct combination. The axes are orthogonal: the alignment guard operates only in the STRUCTURE-WARRANTED Evolution Roadmap; the DRI mandate operates only in the CAN-OPERATE-FLAT Block B. No interference predicted. If both hold without breaking prior criteria, V-04/R6 is the maximum-coverage R6 candidate and the source for any v7 criteria. Falsifiable: if the alignment guard produces trivial Row 1 triggers AND the DRI mandate produces phantom roles simultaneously, both guards underperform. |
| V-05 | output format (DRI mandate + flat rhythm row floor) | V-01/R6 with DRI/Owner mandate (V-03 axis) plus an explicit minimum row count in the Flat Operating Rhythm table: at least one row and at most two | C-22 states the row cap (maximum two). The floor is unstated. A model can technically satisfy "maximum two rows" with a zero-row table. The minimum closes that gap. The DRI mandate and row floor are co-located in Block B. No alignment guard, isolating the flat-output specification axis from the lifecycle axis. Falsifiable: if specifying minimum AND maximum causes the model to produce exactly two rows even when one is operationally sufficient, the floor adds noise. |

---

## V-01 — Confirmed Champion: V-02/R5 Architecture Under v6 Context

**axis:** lifecycle-emphasis (V-02/R5 confirmed baseline)
**hypothesis:** V-02/R5 holds 100.0 under v6. The Flat Operating Rhythm table (Block B) with
max-two-row constraint and governance prohibition satisfies C-21 and C-22. All prior criteria
(C-01 through C-20) are inherited unchanged. This is the first variation to hold 100.0 across
two consecutive rubric versions (v5 and v6). Falsifiable: any aspirational drop vs V-02/R5
reveals an interaction effect not visible in R5's single-axis tests.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT -- STEELMAN FIRST, THEN VERDICT

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact slot order:

**Slot 1 -- Case for Staying Flat**

DO list the specific working mechanisms that make informal coordination viable.
DO include at minimum two numbered reasons.
DO NOT write generic statements like "the team communicates well."
Each reason must name a mechanism (channel, informal lead, decision pattern, cadence).

```
### Case for Staying Flat

1. [Specific mechanism -- e.g., "weekly standup plus a shared backlog resolves
   sprint-level cross-team dependencies without escalation"]
2. [Specific mechanism -- e.g., "a single senior engineer acts as informal
   architecture arbiter, and no cross-cutting decision has been blocked or
   delayed by lack of formal authority"]
(at minimum two; DO NOT proceed until at least two are written)
```

**Slot 2 -- Rebuttal**

DO name the coordination failure the flat-team case cannot answer.
DO NOT write "the team is growing" without specifying the failure mode.
DO reference a specific observable: a blocked decision, a missed SLA, a time-zone gap,
a knowledge silo, a competing roadmap.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Slot 3 -- VERDICT**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting slots 1 and 2 to the verdict.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences -- specific, not generic]
```

**Slot 4 -- Re-assessment Trigger (required for all verdicts)**

DO write the re-assessment trigger immediately after the verdict.
DO decompose the trigger into two separately named sub-fields: Condition and Signal.
DO NOT write a unified "Re-assessment trigger: [condition]" block -- the two sub-fields
are separately required and cannot be merged.
DO NOT write "revisit as the team grows" -- the Condition must name a threshold, milestone,
or observable failure mode. The Signal must name how the Condition will be recognized,
not restate it.

```
Re-assessment trigger:
  Condition: [specific event or threshold -- e.g., "headcount reaches 12"
    or "on-call rotation spans more than two distinct service areas"
    or "a shipped regression is traced to a cross-team coordination gap";
    platitudes like "when the team grows" do not satisfy this field]
  Signal: [observable indicator by which the Condition is recognized --
    e.g., "when the fourth area lead is approved in headcount planning"
    or "when the first cross-team escalation is filed in the on-call queue";
    do not restate the Condition in different words]
```

DO NOT proceed past slot 4 until both Condition and Signal are populated.

---

VERDICT BRANCH -- FOLLOW YOUR VERDICT

**IF VERDICT is CAN-OPERATE-FLAT:**

Sections 3 and 4 (ASCII Org Diagram and Headcount by Area) are ABSENT, not simplified.
A reduced org diagram still fails -- these sections must not exist.

DO produce the following three blocks in order, then stop:

**Block A -- Owner Map:**
```
## Coordination Model

**Owner Map:**
| Area | Informal Lead | Decides Informally |
|------|---------------|--------------------|
| [area] | [role from ROLES-LOADED] | [what this person decides without escalation] |
```

**Block B -- Flat Operating Rhythm:**
```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
| [review or demo] | [e.g., bi-weekly] | [role from ROLES-LOADED] | [review purpose] |
```

Maximum two rows. DO NOT include a governance meeting, architecture board, or steering
committee -- governance requires STRUCTURE-WARRANTED. If governance feels necessary, revisit
whether the verdict should be STRUCTURE-WARRANTED instead.

**Block C -- Re-assessment trigger carry-forward:**
```
**Re-assessment trigger:**
  Condition: [State the Condition from slot 4 here verbatim -- do not paraphrase]
  Signal: [State the Signal from slot 4 here verbatim -- do not paraphrase]
```

DO NOT invent new trigger language. Carry slot 4 values forward verbatim.

Then end with:
```
Generated by: /org-chart {topic} -- {date}
```

**IF VERDICT is STRUCTURE-WARRANTED:**

Continue to all remaining steps in order.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- do not introduce new role names.

---

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns -- Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column -- the Decides and Escalates columns are
separate and both required.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE -- INLINE CHARTERS REQUIRED

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

CHARTER PLACEMENT -- The correct form is: a rhythm row appears, then the charter for that
row appears immediately after it, then the next row appears. Row, then its charter, then the
next row -- this sequence is the required structure. DO NOT write all rhythm rows first and
all charters second. A dedicated COMMITTEE CHARTERS section appearing after the full rhythm
table does not satisfy this requirement.

For each row that designates a committee, board, or governance body:
1. Write the rhythm table row.
2. Immediately write its charter before the next row.
3. Then write the next row.

Charter format:
```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED -- at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward -- name the destination role or forum,
  e.g., "VP of Engineering" or "Executive Steering Committee"]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold: "when headcount reaches N"] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

Requirements:
- At minimum two rows
- Row 1 must name a headcount threshold
- Row 2 must name a workload signal, structural symptom, or milestone event -- NOT a second
  headcount number
- The same trigger dimension restated at a different threshold does not count as distinct
- The structural change column must specify what changes

Dimension vocabulary (Row 2 must use one of these):
- Workload signal: on-call span, PR review latency, cross-team dependency backlog, SLA miss pattern
- Structural symptom: informal lead shared between two people, shipped regression traced to a
  coordination gap, committee produces no decision output for two consecutive sessions
- Milestone event: first external customer onboards, first product ships with a compliance requirement

DO NOT proceed to Anti-Pattern Watch until both rows are written with distinct trigger dimensions.

---

ANTI-PATTERN WATCH -- REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | [One sentence -- reference a specific element of the org just designed: an area name, committee name, headcount total, or DRI role from the rhythm table] | [Mitigation] |
| [Second anti-pattern] | [Domain-specific rationale referencing a named element from above] | [Mitigation] |

Named anti-patterns to draw from (not limited to):
- Committee capture -- a committee's scope grows until it owns decisions that should be delegated
- Too many dotted lines -- matrix reporting diffuses accountability
- Shiproom without a DRI -- ship/no-ship authority is shared, producing stalls
- Governance theater -- meetings exist but have no decision authority
- Org mirroring Conway's Law without intent -- structure reflects team boundaries, not user needs

Requirements:
- At minimum two named anti-patterns with domain-specific rationale
- The "Why It Applies Here" cell must reference the specific org -- not a generic warning
- Generic rationale such as "this is always a risk" does not pass

---

SECTION ORDER -- DO NOT REORDER

DO write sections in this order:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Slot 1 -> Slot 2 -> Slot 3 -> Slot 4: Condition + Signal)
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (max 2 rows, no governance)
         -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to steps 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (with inline charters)
7. Org Evolution Roadmap
8. Anti-Pattern Watch

DO NOT reorder sections.
DO NOT omit any section applicable to the verdict taken.

---

FINAL LINE

DO end with exactly:

```
Generated by: /org-chart {topic} -- {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-02 -- Inertia-to-Evolution Alignment Guard

**axis:** lifecycle-emphasis (inertia-evolution trigger consistency)
**hypothesis:** The inertia Condition (slot 4) and the Evolution Roadmap Row 1 are currently
independent commitments. V-01/R6 can write "Condition: headcount reaches 12" in slot 4 and
"Row 1: when headcount reaches 8" without structural contradiction -- a lower Row 1 threshold
describes the same growth event but would have already fired before the inertia assessment
gate is reached. An alignment guard requiring Row 1 to name a threshold at or beyond the
Condition closes this divergence. The guard is a structural anchor: Row 1 cannot be an
independently invented threshold that precedes the gate commitment. Candidate for C-23.
Falsifiable: if the guard produces Row 1 triggers that merely restate the Condition (trivially
derived at the same threshold), the guard adds no discriminating value.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT -- STEELMAN FIRST, THEN VERDICT

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact slot order:

**Slot 1 -- Case for Staying Flat**

DO list the specific working mechanisms that make informal coordination viable.
DO include at minimum two numbered reasons.
DO NOT write generic statements like "the team communicates well."
Each reason must name a mechanism (channel, informal lead, decision pattern, cadence).

```
### Case for Staying Flat

1. [Specific mechanism]
2. [Specific mechanism]
(at minimum two; DO NOT proceed until at least two are written)
```

**Slot 2 -- Rebuttal**

DO name the coordination failure the flat-team case cannot answer.
DO NOT write "the team is growing" without specifying the failure mode.
DO reference a specific observable: a blocked decision, a missed SLA, a time-zone gap,
a knowledge silo, a competing roadmap.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Slot 3 -- VERDICT**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting slots 1 and 2 to the verdict.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences -- specific, not generic]
```

**Slot 4 -- Re-assessment Trigger (required for all verdicts)**

DO decompose the trigger into two separately named sub-fields: Condition and Signal.
DO NOT merge into a single "Re-assessment trigger" block.
DO NOT write platitudes -- Condition must name a threshold or observable failure.

```
Re-assessment trigger:
  Condition: [specific event or threshold -- e.g., "headcount reaches 12"
    or "on-call rotation spans more than two distinct service areas";
    platitudes like "when the team grows" do not satisfy this field]
  Signal: [observable indicator by which the Condition is recognized --
    e.g., "when the fourth area lead is approved in headcount planning";
    do not restate the Condition in different words]
```

DO NOT proceed past slot 4 until both Condition and Signal are populated.

---

VERDICT BRANCH -- FOLLOW YOUR VERDICT

**IF VERDICT is CAN-OPERATE-FLAT:**

Sections 3 and 4 (ASCII Org Diagram and Headcount by Area) are ABSENT, not simplified.
A reduced org diagram still fails -- these sections must not exist.

DO produce the following three blocks in order, then stop:

**Block A -- Owner Map:**
```
## Coordination Model

**Owner Map:**
| Area | Informal Lead | Decides Informally |
|------|---------------|--------------------|
| [area] | [role from ROLES-LOADED] | [what this person decides without escalation] |
```

**Block B -- Flat Operating Rhythm:**
```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
| [review or demo] | [e.g., bi-weekly] | [role from ROLES-LOADED] | [review purpose] |
```

Maximum two rows. DO NOT include a governance meeting, architecture board, or steering
committee -- governance requires STRUCTURE-WARRANTED. If governance feels necessary, revisit
whether the verdict should be STRUCTURE-WARRANTED instead.

**Block C -- Re-assessment trigger carry-forward:**
```
**Re-assessment trigger:**
  Condition: [State the Condition from slot 4 here verbatim -- do not paraphrase]
  Signal: [State the Signal from slot 4 here verbatim -- do not paraphrase]
```

DO NOT invent new trigger language. Carry slot 4 values forward verbatim.

Then end with:
```
Generated by: /org-chart {topic} -- {date}
```

**IF VERDICT is STRUCTURE-WARRANTED:**

Continue to all remaining steps in order.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- do not introduce new role names.

---

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns -- Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column -- the Decides and Escalates columns are
separate and both required.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE -- INLINE CHARTERS REQUIRED

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

CHARTER PLACEMENT -- The correct form is: a rhythm row appears, then the charter for that
row appears immediately after it, then the next row appears. Row, then its charter, then the
next row -- this sequence is the required structure. DO NOT write all rhythm rows first and
all charters second. A dedicated COMMITTEE CHARTERS section appearing after the full rhythm
table does not satisfy this requirement.

For each row that designates a committee, board, or governance body:
1. Write the rhythm table row.
2. Immediately write its charter before the next row.
3. Then write the next row.

Charter format:
```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED -- at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward -- name the destination role or forum]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG EVOLUTION ROADMAP -- REQUIRED (ALIGNMENT GUARD ACTIVE)

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold at or beyond the Condition from slot 4] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

ALIGNMENT GUARD -- Row 1 must name a headcount threshold that is at or beyond the Condition
committed to in slot 4 of the Inertia Assessment. If slot 4 Condition names "headcount reaches
12," Row 1 must use a headcount threshold of 12 or higher -- a lower threshold would describe
growth that has already passed or will pass before the re-assessment gate fires. The inertia
Condition and the Evolution Roadmap Row 1 describe the same growth trajectory; they cannot
diverge to unrelated scales.

DO NOT write a Row 1 threshold below the Condition stated in slot 4.
DO NOT invent an independent Row 1 trigger that ignores the slot 4 commitment.
Row 1 must be the same growth event, extended -- not a separately authored trigger.

Requirements:
- At minimum two rows
- Row 1: headcount threshold at or beyond slot 4 Condition
- Row 2: workload signal, structural symptom, or milestone -- NOT a second headcount number
- The same trigger dimension restated at a different threshold does not count as distinct
- Dimension vocabulary: on-call span, PR latency, dependency backlog, SLA miss, informal lead
  shared between two people, shipped regression, no-decision committee session, first external
  customer, first compliance requirement

DO NOT proceed to Anti-Pattern Watch until both rows are written with distinct trigger dimensions
and Row 1 has been checked against the slot 4 Condition.

---

ANTI-PATTERN WATCH -- REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | [One sentence -- reference a specific element: area name, committee name, headcount total, or DRI role] | [Mitigation] |
| [Second anti-pattern] | [Domain-specific rationale referencing a named element from above] | [Mitigation] |

Named anti-patterns to draw from (not limited to):
- Committee capture -- a committee's scope grows until it owns decisions that should be delegated
- Too many dotted lines -- matrix reporting diffuses accountability
- Shiproom without a DRI -- ship/no-ship authority is shared, producing stalls
- Governance theater -- meetings exist but have no decision authority
- Org mirroring Conway's Law without intent -- structure reflects team boundaries, not user needs

Requirements:
- At minimum two named anti-patterns with domain-specific rationale
- The "Why It Applies Here" cell must reference the specific org -- not a generic warning
- Generic rationale such as "this is always a risk" does not pass

---

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Slot 1 -> Slot 2 -> Slot 3 -> Slot 4: Condition + Signal)
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (max 2 rows, no governance)
         -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
8. Anti-Pattern Watch

---

FINAL LINE

```
Generated by: /org-chart {topic} -- {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-03 -- Mandatory DRI/Owner Column in Flat Operating Rhythm Table

**axis:** output format (DRI/Owner column mandate in CAN-OPERATE-FLAT Block B)
**hypothesis:** C-21 requires a Flat Operating Rhythm table but states the DRI/Owner column
is "expected but not required for a bare PASS." C-10 (role names in two or more sections)
tests STRUCTURE-WARRANTED outputs; no criterion explicitly tests role propagation in the flat
branch. V-01/R6 Block B includes DRI/Owner as a template column but does not mandate it. A
model can produce a table with blank DRI entries and still satisfy C-21. Mandating the DRI
column forces roles from ROLES-LOADED to propagate into the flat output, closing the C-10
gap for flat-verdict outputs. Single-axis addition to V-01/R6: only Block B changes. All other
sections identical to V-01/R6. Falsifiable: if ROLES-LOADED is sparse and the mandate causes
the model to invent roles, the mandate introduces inaccuracy.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT -- STEELMAN FIRST, THEN VERDICT

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact slot order:

**Slot 1 -- Case for Staying Flat**

DO list the specific working mechanisms that make informal coordination viable.
DO include at minimum two numbered reasons.
DO NOT write generic statements like "the team communicates well."
Each reason must name a mechanism (channel, informal lead, decision pattern, cadence).

```
### Case for Staying Flat

1. [Specific mechanism]
2. [Specific mechanism]
(at minimum two; DO NOT proceed until at least two are written)
```

**Slot 2 -- Rebuttal**

DO name the coordination failure the flat-team case cannot answer.
DO NOT write "the team is growing" without specifying the failure mode.
DO reference a specific observable: a blocked decision, a missed SLA, a time-zone gap,
a knowledge silo, a competing roadmap.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Slot 3 -- VERDICT**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting slots 1 and 2 to the verdict.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences -- specific, not generic]
```

**Slot 4 -- Re-assessment Trigger (required for all verdicts)**

DO decompose the trigger into two separately named sub-fields: Condition and Signal.
DO NOT merge into a single "Re-assessment trigger" block.
DO NOT write platitudes -- Condition must name a threshold or observable failure.

```
Re-assessment trigger:
  Condition: [specific event or threshold; platitudes do not satisfy this field]
  Signal: [observable indicator -- not a restatement of the Condition]
```

DO NOT proceed past slot 4 until both Condition and Signal are populated.

---

VERDICT BRANCH -- FOLLOW YOUR VERDICT

**IF VERDICT is CAN-OPERATE-FLAT:**

Sections 3 and 4 (ASCII Org Diagram and Headcount by Area) are ABSENT, not simplified.
A reduced org diagram still fails -- these sections must not exist.

DO produce the following three blocks in order, then stop:

**Block A -- Owner Map:**
```
## Coordination Model

**Owner Map:**
| Area | Informal Lead | Decides Informally |
|------|---------------|--------------------|
| [area] | [role from ROLES-LOADED] | [what this person decides without escalation] |
```

**Block B -- Flat Operating Rhythm:**
```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
| [review or demo] | [e.g., bi-weekly] | [role from ROLES-LOADED] | [review purpose] |
```

Maximum two rows. DO NOT include a governance meeting, architecture board, or steering
committee -- governance requires STRUCTURE-WARRANTED. If governance feels necessary, revisit
whether the verdict should be STRUCTURE-WARRANTED instead.

DRI MANDATE -- The DRI / Owner column is required. DO NOT leave any DRI / Owner cell blank.
Each row must name a role drawn from the ROLES-LOADED or ROLES-NOTE block. If ROLES-LOADED
has only one role, that role may appear in both rows. DO NOT invent a role name not present
in the roles block.

**Block C -- Re-assessment trigger carry-forward:**
```
**Re-assessment trigger:**
  Condition: [State the Condition from slot 4 here verbatim -- do not paraphrase]
  Signal: [State the Signal from slot 4 here verbatim -- do not paraphrase]
```

DO NOT invent new trigger language. Carry slot 4 values forward verbatim.

Then end with:
```
Generated by: /org-chart {topic} -- {date}
```

**IF VERDICT is STRUCTURE-WARRANTED:**

Continue to all remaining steps in order.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- do not introduce new role names.

---

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns -- Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column -- the Decides and Escalates columns are
separate and both required.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE -- INLINE CHARTERS REQUIRED

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

CHARTER PLACEMENT -- The correct form is: a rhythm row appears, then the charter for that
row appears immediately after it, then the next row appears. Row, then its charter, then the
next row -- this sequence is the required structure. DO NOT write all rhythm rows first and
all charters second. A dedicated COMMITTEE CHARTERS section appearing after the full rhythm
table does not satisfy this requirement.

For each row that designates a committee, board, or governance body:
1. Write the rhythm table row.
2. Immediately write its charter before the next row.
3. Then write the next row.

Charter format:
```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED -- at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward -- name the destination role or forum]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold: "when headcount reaches N"] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

Requirements:
- At minimum two rows
- Row 1: headcount threshold
- Row 2: workload signal, structural symptom, or milestone -- NOT a second headcount number
- The same trigger dimension restated at a different threshold does not count as distinct
- Dimension vocabulary: on-call span, PR latency, dependency backlog, SLA miss, informal lead
  shared between two people, shipped regression, no-decision committee session, first external
  customer, first compliance requirement

DO NOT proceed to Anti-Pattern Watch until both rows are written with distinct trigger dimensions.

---

ANTI-PATTERN WATCH -- REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | [One sentence -- reference a specific element: area name, committee name, headcount total, DRI role] | [Mitigation] |
| [Second anti-pattern] | [Domain-specific rationale referencing a named element from above] | [Mitigation] |

Named anti-patterns to draw from (not limited to):
- Committee capture -- a committee's scope grows until it owns decisions that should be delegated
- Too many dotted lines -- matrix reporting diffuses accountability
- Shiproom without a DRI -- ship/no-ship authority is shared, producing stalls
- Governance theater -- meetings exist but have no decision authority
- Org mirroring Conway's Law without intent -- structure reflects team boundaries, not user needs

Requirements:
- At minimum two named anti-patterns with domain-specific rationale
- The "Why It Applies Here" cell must reference the specific org -- not a generic warning
- Generic rationale such as "this is always a risk" does not pass

---

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Slot 1 -> Slot 2 -> Slot 3 -> Slot 4: Condition + Signal)
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (max 2 rows, DRI required,
         no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (inline charters)
7. Org Evolution Roadmap
8. Anti-Pattern Watch

---

FINAL LINE

```
Generated by: /org-chart {topic} -- {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-04 -- Combined: Alignment Guard + Mandatory DRI

**axis:** lifecycle + output format (inertia-to-evolution alignment guard AND DRI/Owner mandate)
**hypothesis:** V-02/R6 (alignment guard) and V-03/R6 (DRI mandate) are orthogonal: the
alignment guard operates only in the STRUCTURE-WARRANTED Evolution Roadmap; the DRI mandate
operates only in the CAN-OPERATE-FLAT Block B. No interference predicted. If both hold without
breaking prior criteria, V-04/R6 is the maximum-coverage R6 candidate and the source for any
v7 criteria. Falsifiable: if the alignment guard produces trivial Row 1 triggers AND the DRI
mandate produces phantom roles simultaneously, both guards underperform and neither C-23 nor
the DRI criterion is viable.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT -- STEELMAN FIRST, THEN VERDICT

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact slot order:

**Slot 1 -- Case for Staying Flat**

DO list the specific working mechanisms that make informal coordination viable.
DO include at minimum two numbered reasons.
DO NOT write generic statements like "the team communicates well."
Each reason must name a mechanism (channel, informal lead, decision pattern, cadence).

```
### Case for Staying Flat

1. [Specific mechanism]
2. [Specific mechanism]
(at minimum two; DO NOT proceed until at least two are written)
```

**Slot 2 -- Rebuttal**

DO name the coordination failure the flat-team case cannot answer.
DO reference a specific observable: a blocked decision, a missed SLA, a time-zone gap,
a knowledge silo, a competing roadmap.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Slot 3 -- VERDICT**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting slots 1 and 2 to the verdict.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences -- specific, not generic]
```

**Slot 4 -- Re-assessment Trigger (required for all verdicts)**

DO decompose the trigger into two separately named sub-fields: Condition and Signal.
DO NOT merge into a single "Re-assessment trigger" block.
DO NOT write platitudes -- Condition must name a threshold or observable failure.

```
Re-assessment trigger:
  Condition: [specific event or threshold; platitudes do not satisfy this field]
  Signal: [observable indicator -- not a restatement of the Condition]
```

DO NOT proceed past slot 4 until both Condition and Signal are populated.

---

VERDICT BRANCH -- FOLLOW YOUR VERDICT

**IF VERDICT is CAN-OPERATE-FLAT:**

Sections 3 and 4 (ASCII Org Diagram and Headcount by Area) are ABSENT, not simplified.
A reduced org diagram still fails -- these sections must not exist.

DO produce the following three blocks in order, then stop:

**Block A -- Owner Map:**
```
## Coordination Model

**Owner Map:**
| Area | Informal Lead | Decides Informally |
|------|---------------|--------------------|
| [area] | [role from ROLES-LOADED] | [what this person decides without escalation] |
```

**Block B -- Flat Operating Rhythm:**
```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
| [review or demo] | [e.g., bi-weekly] | [role from ROLES-LOADED] | [review purpose] |
```

Maximum two rows. DO NOT include a governance meeting, architecture board, or steering
committee -- governance requires STRUCTURE-WARRANTED. If governance feels necessary, revisit
whether the verdict should be STRUCTURE-WARRANTED instead.

DRI MANDATE -- The DRI / Owner column is required. DO NOT leave any DRI / Owner cell blank.
Each row must name a role drawn from the ROLES-LOADED or ROLES-NOTE block. If ROLES-LOADED
has only one role, that role may appear in both rows. DO NOT invent a role name not present
in the roles block.

**Block C -- Re-assessment trigger carry-forward:**
```
**Re-assessment trigger:**
  Condition: [State the Condition from slot 4 here verbatim -- do not paraphrase]
  Signal: [State the Signal from slot 4 here verbatim -- do not paraphrase]
```

DO NOT invent new trigger language. Carry slot 4 values forward verbatim.

Then end with:
```
Generated by: /org-chart {topic} -- {date}
```

**IF VERDICT is STRUCTURE-WARRANTED:**

Continue to all remaining steps in order.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- do not introduce new role names.

---

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns -- Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column -- the Decides and Escalates columns are
separate and both required.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE -- INLINE CHARTERS REQUIRED

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

CHARTER PLACEMENT -- The correct form is: a rhythm row appears, then the charter for that
row appears immediately after it, then the next row appears. Row, then its charter, then the
next row -- this sequence is the required structure. DO NOT write all rhythm rows first and
all charters second. A dedicated COMMITTEE CHARTERS section appearing after the full rhythm
table does not satisfy this requirement.

For each row that designates a committee, board, or governance body:
1. Write the rhythm table row.
2. Immediately write its charter before the next row.
3. Then write the next row.

Charter format:
```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED -- at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward -- name the destination role or forum]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG EVOLUTION ROADMAP -- REQUIRED (ALIGNMENT GUARD ACTIVE)

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold at or beyond the Condition from slot 4] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

ALIGNMENT GUARD -- Row 1 must name a headcount threshold that is at or beyond the Condition
committed to in slot 4. If slot 4 Condition names "headcount reaches 12," Row 1 must use a
headcount threshold of 12 or higher. A lower Row 1 threshold describes growth that precedes
the re-assessment gate and cannot be a forward structural trigger.

DO NOT write a Row 1 threshold below the Condition stated in slot 4.
Row 1 must be the same growth event, extended -- not an independently authored trigger.

Requirements:
- At minimum two rows
- Row 1: headcount threshold at or beyond slot 4 Condition
- Row 2: workload signal, structural symptom, or milestone -- NOT a second headcount number
- Same trigger dimension at different threshold does not count as distinct
- Dimension vocabulary: on-call span, PR latency, dependency backlog, SLA miss, informal lead
  shared between two people, shipped regression, no-decision committee session, first external
  customer, first compliance requirement

DO NOT proceed to Anti-Pattern Watch until both rows are written with distinct trigger dimensions
and Row 1 has been checked against the slot 4 Condition.

---

ANTI-PATTERN WATCH -- REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | [One sentence -- reference a specific element: area name, committee name, headcount total, DRI role] | [Mitigation] |
| [Second anti-pattern] | [Domain-specific rationale referencing a named element from above] | [Mitigation] |

Named anti-patterns to draw from (not limited to):
- Committee capture -- a committee's scope grows until it owns decisions that should be delegated
- Too many dotted lines -- matrix reporting diffuses accountability
- Shiproom without a DRI -- ship/no-ship authority is shared, producing stalls
- Governance theater -- meetings exist but have no decision authority
- Org mirroring Conway's Law without intent -- structure reflects team boundaries, not user needs

Requirements:
- At minimum two named anti-patterns with domain-specific rationale
- The "Why It Applies Here" cell must reference the specific org -- not a generic warning
- Generic rationale such as "this is always a risk" does not pass

---

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Slot 1 -> Slot 2 -> Slot 3 -> Slot 4: Condition + Signal)
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (max 2 rows, DRI required,
         no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
8. Anti-Pattern Watch

---

FINAL LINE

```
Generated by: /org-chart {topic} -- {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-05 -- Combined: Mandatory DRI + Flat Rhythm Row Floor

**axis:** output format (DRI/Owner mandate AND explicit minimum row count in Flat Operating Rhythm)
**hypothesis:** V-03/R6 mandates the DRI/Owner column in Block B but does not constrain the
minimum row count. C-22 states a maximum of two rows; the floor is unstated. A table with zero
rows technically satisfies "maximum two rows." The minimum constraint (at least one row) forces
the flat output to provide positive operational content, not a structural shell. The DRI mandate
and the row floor are co-located in Block B -- both are structural constraints on the same table.
No alignment guard, isolating the flat-output specification axis from the lifecycle axis. If
V-05/R6 matches V-04/R6, the alignment guard is not load-bearing for v7 criteria; if V-05/R6
matches V-03/R6, the row floor adds nothing beyond the DRI mandate. Falsifiable: if specifying
a minimum causes the model to produce exactly two rows even when one is operationally sufficient,
the floor adds noise.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT -- STEELMAN FIRST, THEN VERDICT

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact slot order:

**Slot 1 -- Case for Staying Flat**

DO list the specific working mechanisms that make informal coordination viable.
DO include at minimum two numbered reasons.
DO NOT write generic statements like "the team communicates well."
Each reason must name a mechanism (channel, informal lead, decision pattern, cadence).

```
### Case for Staying Flat

1. [Specific mechanism]
2. [Specific mechanism]
(at minimum two; DO NOT proceed until at least two are written)
```

**Slot 2 -- Rebuttal**

DO name the coordination failure the flat-team case cannot answer.
DO reference a specific observable: a blocked decision, a missed SLA, a time-zone gap,
a knowledge silo, a competing roadmap.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Slot 3 -- VERDICT**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting slots 1 and 2 to the verdict.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences -- specific, not generic]
```

**Slot 4 -- Re-assessment Trigger (required for all verdicts)**

DO decompose the trigger into two separately named sub-fields: Condition and Signal.
DO NOT merge into a single "Re-assessment trigger" block.
DO NOT write platitudes -- Condition must name a threshold or observable failure.

```
Re-assessment trigger:
  Condition: [specific event or threshold; platitudes do not satisfy this field]
  Signal: [observable indicator -- not a restatement of the Condition]
```

DO NOT proceed past slot 4 until both Condition and Signal are populated.

---

VERDICT BRANCH -- FOLLOW YOUR VERDICT

**IF VERDICT is CAN-OPERATE-FLAT:**

Sections 3 and 4 (ASCII Org Diagram and Headcount by Area) are ABSENT, not simplified.
A reduced org diagram still fails -- these sections must not exist.

DO produce the following three blocks in order, then stop:

**Block A -- Owner Map:**
```
## Coordination Model

**Owner Map:**
| Area | Informal Lead | Decides Informally |
|------|---------------|--------------------|
| [area] | [role from ROLES-LOADED] | [what this person decides without escalation] |
```

**Block B -- Flat Operating Rhythm:**
```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
```

At least one row, at most two rows. DO NOT produce an empty table.
DO NOT include a governance meeting, architecture board, or steering committee --
governance requires STRUCTURE-WARRANTED. If governance feels necessary, revisit
whether the verdict should be STRUCTURE-WARRANTED instead.

DRI MANDATE -- The DRI / Owner column is required. DO NOT leave any DRI / Owner cell blank.
Each row must name a role drawn from the ROLES-LOADED or ROLES-NOTE block. If ROLES-LOADED
has only one role, that role may appear in both rows. DO NOT invent a role name not present
in the roles block.

**Block C -- Re-assessment trigger carry-forward:**
```
**Re-assessment trigger:**
  Condition: [State the Condition from slot 4 here verbatim -- do not paraphrase]
  Signal: [State the Signal from slot 4 here verbatim -- do not paraphrase]
```

DO NOT invent new trigger language. Carry slot 4 values forward verbatim.

Then end with:
```
Generated by: /org-chart {topic} -- {date}
```

**IF VERDICT is STRUCTURE-WARRANTED:**

Continue to all remaining steps in order.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- do not introduce new role names.

---

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns -- Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column -- the Decides and Escalates columns are
separate and both required.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated -- name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE -- INLINE CHARTERS REQUIRED

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

CHARTER PLACEMENT -- The correct form is: a rhythm row appears, then the charter for that
row appears immediately after it, then the next row appears. Row, then its charter, then the
next row -- this sequence is the required structure. DO NOT write all rhythm rows first and
all charters second. A dedicated COMMITTEE CHARTERS section appearing after the full rhythm
table does not satisfy this requirement.

For each row that designates a committee, board, or governance body:
1. Write the rhythm table row.
2. Immediately write its charter before the next row.
3. Then write the next row.

Charter format:
```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED -- at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward -- name the destination role or forum]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold: "when headcount reaches N"] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

Requirements:
- At minimum two rows
- Row 1: headcount threshold
- Row 2: workload signal, structural symptom, or milestone -- NOT a second headcount number
- The same trigger dimension restated at a different threshold does not count as distinct
- Dimension vocabulary: on-call span, PR latency, dependency backlog, SLA miss, informal lead
  shared between two people, shipped regression, no-decision committee session, first external
  customer, first compliance requirement

DO NOT proceed to Anti-Pattern Watch until both rows are written with distinct trigger dimensions.

---

ANTI-PATTERN WATCH -- REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | [One sentence -- reference a specific element: area name, committee name, headcount total, DRI role] | [Mitigation] |
| [Second anti-pattern] | [Domain-specific rationale referencing a named element from above] | [Mitigation] |

Named anti-patterns to draw from (not limited to):
- Committee capture -- a committee's scope grows until it owns decisions that should be delegated
- Too many dotted lines -- matrix reporting diffuses accountability
- Shiproom without a DRI -- ship/no-ship authority is shared, producing stalls
- Governance theater -- meetings exist but have no decision authority
- Org mirroring Conway's Law without intent -- structure reflects team boundaries, not user needs

Requirements:
- At minimum two named anti-patterns with domain-specific rationale
- The "Why It Applies Here" cell must reference the specific org -- not a generic warning
- Generic rationale such as "this is always a risk" does not pass

---

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Slot 1 -> Slot 2 -> Slot 3 -> Slot 4: Condition + Signal)
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (min 1 / max 2 rows,
         DRI required, no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (inline charters)
7. Org Evolution Roadmap
8. Anti-Pattern Watch

---

FINAL LINE

```
Generated by: /org-chart {topic} -- {date}
```

DO NOT emit literal placeholder text in the final line.

---

## Predicted Scores Under v6

| V | C-21 | C-22 | Alignment guard | Asp pass | Composite | Notes |
|---|------|------|-----------------|----------|-----------|-------|
| V-01/R6 | PASS | PASS | absent | 14/14 | 100.0 | Confirmed carry-forward of V-02/R5 |
| V-02/R6 | PASS | PASS | PASS (C-23 candidate) | 14/14 | 100.0 | If guard becomes C-23, retroactive credit |
| V-03/R6 | PASS | PASS | absent | 14/14 | 100.0 | DRI mandate not yet a v6 criterion; no v6 delta |
| V-04/R6 | PASS | PASS | PASS | 14/14 | 100.0 | Max-coverage combination; source for v7 |
| V-05/R6 | PASS | PASS | absent | 14/14 | 100.0 | Row floor not a v6 criterion; no v6 delta |

All five variations are predicted to score 100.0 under v6. The discrimination moves to v7.
The R6 open question -- does V-02/R6's alignment guard produce a real gap observable in scored
outputs, and if so, does it survive as C-23? -- can only be resolved by running the variations
against actual model outputs and checking whether inertia Condition and Evolution Row 1 diverge
in practice.

**v7 candidate criteria from R6:**

| ID | Criterion | Source |
|----|-----------|--------|
| C-23 | Evolution Roadmap Row 1 anchored to Inertia slot 4 Condition (threshold at or beyond) | V-02/R6: alignment guard closes independent-commitment divergence |
| C-24 | Flat Operating Rhythm DRI/Owner column mandatory (role from ROLES-LOADED, no blanks) | V-03/R6 + V-04/R6: closes C-10 role-propagation gap in flat branch |
| C-25 | Flat Operating Rhythm row floor: at least one row required (empty table does not satisfy max-two) | V-05/R6: "maximum two" without a floor allows structural shell with no content |

*Generated by: /quest:variate org-chart R6 -- 2026-03-16*
