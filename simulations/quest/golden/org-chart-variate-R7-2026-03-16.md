---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R7
rubric_version: v7
status: variate
---

# org-chart Variate -- Round 7

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v7 (C-01 through C-25; C-23 adds Evolution Roadmap alignment guard; C-24 promotes
DRI/Owner mandate to hard requirement; C-25 adds explicit row floor for Flat Operating Rhythm)
**Round:** R7 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R6 ceiling under v7:**
V-04/R6 scores 99.41 under v7 -- passes C-23 (alignment guard) and C-24 (DRI mandate),
fails C-25 (no row floor; "maximum two rows" without a floor leaves zero-row shell open).
V-05/R6 scores 99.41 under v7 -- passes C-24 (DRI mandate) and C-25 (row floor),
fails C-23 (no alignment guard; Evolution Roadmap Row 1 independently authored).
No R6 variation scores 100.0 under v7.

**R7 target:** Combine V-04/R6 (C-23 + C-24) with V-05/R6 (C-25). The three axes are
orthogonal: C-23 operates in the STRUCTURE-WARRANTED Evolution Roadmap section; C-24 and
C-25 operate in the CAN-OPERATE-FLAT Block B. A single variation carrying all three
achieves 17/17 aspirational and 100.0 under v7. V-01/R7 is that combination. R7 then
explores four additional axes for expressing the three new criteria, testing whether
phrasing register, output format, or lifecycle emphasis changes model compliance.

---

## Round 7 Variation Map

| V | Axis | What Changed vs V-04/R6 | Hypothesis |
|---|------|------------------------|------------|
| V-01 | output format (row floor added to V-04/R6) | V-04/R6 base + V-05/R6 row floor: "At least one row, at most two rows. DO NOT produce an empty table." replaces "Maximum two rows." in Block B | Combining V-04/R6 (C-23+C-24) with V-05/R6 (C-25) produces the first 17/17 aspirational candidate. C-23/C-24/C-25 are orthogonal sections; no interference predicted. Falsifiable: if any of the three new criteria fail on a scored run, one combination has an unexpected interaction. |
| V-02 | phrasing register (formal/structural prose for C-23) | V-01/R7 base with the Evolution Roadmap alignment guard rewritten in structural-prose style -- explanatory sentences naming the relationship between slot 4 and Row 1 -- rather than DO/DO NOT imperatives | DO/DO NOT imperatives work for structural gates. For a cross-section alignment constraint, formal prose may convey the dependency more precisely: "Row 1 inherits its threshold from slot 4's Condition" names the logical dependency, not just the rule. Falsifiable: if models comply better with DO/DO NOT than formal prose, imperative style is load-bearing for C-23. |
| V-03 | output format (CONSTRAINTS block extracted before templates) | V-01/R7 base with Block B and Evolution Roadmap each prefaced by an explicit CONSTRAINTS checklist that extracts C-24/C-25 and C-23 requirements from the embedded template text into a pre-block rules section | Embedding constraints inside the template requires parsing them mid-generation. An extracted CONSTRAINTS block states all requirements before the template, allowing confirmation before rows are written. Falsifiable: if the external CONSTRAINTS block causes the model to treat the template as optional, format compliance regresses. |
| V-04 | lifecycle + output format (V-02 prose for C-23 + V-03 CONSTRAINTS block for C-24/C-25) | V-01/R7 base with formal prose alignment guard (V-02 axis) AND extracted CONSTRAINTS block for Block B (V-03 axis) | Orthogonal combination: C-23 change is in Evolution Roadmap; C-24/C-25 change is in Block B. If both hold at 17/17 aspirational, phrasing register and pre-block format are independently viable. Falsifiable: if formal prose for C-23 and CONSTRAINTS block for C-24/C-25 together reduce compliance on one of the three criteria, the combination has an unexpected interaction. |
| V-05 | lifecycle emphasis (expanded WHY rationale for C-23, C-24, C-25) | V-01/R7 base with each of the three new constraint points prefaced by a brief rationale explaining why the constraint exists and what failure mode it closes | Constraints without rationale rely on the model inferring the enforcement goal. Adding WHY language names the failure mode explicitly. Explicit failure-mode naming may reduce technically-correct-but-non-compliant outputs. Falsifiable: if rationale expansion produces verbose outputs that obscure the structural requirements, compliance on C-23/C-24/C-25 regresses. |

## V-01 -- Confirmed R7 Champion: V-04/R6 + Row Floor

**axis:** output format (add row floor to V-04/R6 baseline)
**hypothesis:** V-04/R6 is the highest-scoring R6 variation under v7 (99.41), failing only
C-25. V-05/R6 contributes exactly C-25: "At least one row, at most two rows. DO NOT produce
an empty table." Combining the two produces 17/17 aspirational. The three new criteria are
in distinct sections -- alignment guard in Evolution Roadmap, DRI mandate and row floor in
Block B -- no interaction predicted. This is the R7 target variation. Falsifiable: if adding
the row floor causes Block B to be oversized (model produces exactly two rows regardless of
operational need), the floor adds noise.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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
**Escalates:** [decision types referred upward -- name the destination role or forum,
  e.g., "VP of Engineering" or "Executive Steering Committee"]
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
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (min 1 / max 2 rows,
         DRI required from roles block, no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to steps 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (with inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
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

## V-02 -- Phrasing Register: Formal Prose for C-23 Alignment Guard

**axis:** phrasing register (structural-prose rewrite of the Evolution Roadmap alignment guard)
**hypothesis:** V-01/R7 expresses the C-23 alignment guard with DO/DO NOT imperatives: "DO NOT
write a Row 1 threshold below the Condition stated in slot 4." This is structurally correct
but does not explain the logical dependency -- why a lower Row 1 threshold is structurally
incoherent. Formal prose names the dependency explicitly: "Row 1 inherits its threshold from
the Condition in slot 4; they describe the same growth event." If formal prose improves C-23
compliance by making the failure mode visible, phrasing register is load-bearing for
cross-section alignment constraints. Falsifiable: if DO/DO NOT outperforms formal prose,
concise imperatives suppress workarounds better than explanatory language. Single-axis change:
only the Evolution Roadmap alignment guard text changes. Block B (C-24, C-25) identical to
V-01/R7.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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
**Escalates:** [decision types referred upward -- name the destination role or forum,
  e.g., "VP of Engineering" or "Executive Steering Committee"]
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

ALIGNMENT GUARD -- The Row 1 threshold is structurally bound to the Condition committed to
in slot 4. The inertia gate and the first structural trigger in the Evolution Roadmap are two
facets of the same growth event: slot 4 names the Condition at which re-assessment is warranted;
Row 1 names the growth threshold at which structural change follows from that re-assessment.
These two values describe the same growth trajectory and must be consistent. A Row 1 threshold
that falls below the slot 4 Condition describes growth that precedes the gate -- it cannot be
a forward structural trigger. A Row 1 threshold authored independently of slot 4 introduces two
competing figures for the same growth event, which is structurally incoherent.

The rule: Row 1's headcount threshold is at or beyond the slot 4 Condition. If the Condition
is "headcount reaches 12," Row 1 names 12 or higher. Row 1 extends the growth trajectory
established at the gate; it does not restart or contradict it.

Requirements:
- At minimum two rows
- Row 1: headcount threshold at or beyond slot 4 Condition -- same growth event, not a new one
- Row 2: workload signal, structural symptom, or milestone -- NOT a second headcount number
- The same trigger dimension restated at a different threshold does not count as distinct
- Dimension vocabulary: on-call span, PR latency, dependency backlog, SLA miss, informal lead
  shared between two people, shipped regression, no-decision committee session, first external
  customer, first compliance requirement

Confirm Row 1 is consistent with slot 4 before proceeding to Anti-Pattern Watch.

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
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (min 1 / max 2 rows,
         DRI required from roles block, no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to steps 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (with inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
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

## V-03 -- Output Format: CONSTRAINTS Block Before Templates

**axis:** output format (pre-block CONSTRAINTS checklists for Block B and Evolution Roadmap)
**hypothesis:** In V-01/R7, C-24/C-25 constraints are embedded inside the Block B section
text and C-23 is embedded in the Evolution Roadmap section text. A model generating the table
row by row must parse the constraint mid-generation. An extracted CONSTRAINTS block placed
before the template allows the model to confirm all requirements before writing any rows.
This is a structural pre-commitment pattern: requirements stated before the template are
checked before generation begins rather than during. Single-axis: only the placement of
C-23/C-24/C-25 constraints changes. The constraint text itself is identical to V-01/R7.
Falsifiable: if the CONSTRAINTS block causes the model to treat the following template as
optional (having already "satisfied" the checklist), format compliance regresses.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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

BLOCK B CONSTRAINTS -- confirm all before writing any rows:
  1. Row floor: at least one row. DO NOT produce an empty table.
  2. Row ceiling: at most two rows. DO NOT exceed two rows.
  3. DRI/Owner required: DO NOT leave any DRI / Owner cell blank.
  4. DRI/Owner source: each value must name a role from ROLES-LOADED or ROLES-NOTE only.
     DO NOT invent a role name not present in the roles block.
  5. Governance prohibition: DO NOT include a governance meeting, architecture board, or
     steering committee -- governance requires STRUCTURE-WARRANTED.

```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
| [review or demo] | [e.g., bi-weekly] | [role from ROLES-LOADED] | [review purpose] |
```

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

ORG EVOLUTION ROADMAP -- REQUIRED (ALIGNMENT GUARD ACTIVE)

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

EVOLUTION ROADMAP CONSTRAINTS -- confirm all before writing any rows:
  1. Alignment guard: Row 1 threshold must be at or beyond the Condition from slot 4.
     A lower Row 1 threshold precedes the gate and cannot be a forward structural trigger.
  2. Row 1 dimension: headcount threshold only -- no workload signals in Row 1.
  3. Row 2 dimension: workload signal, structural symptom, or milestone -- NOT headcount.
  4. Minimum: at least two rows with distinct trigger dimensions.
  5. Consistency check: confirm Row 1 >= slot 4 Condition before proceeding.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold at or beyond the Condition from slot 4] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

Dimension vocabulary (Row 2 must use one of these):
- Workload signal: on-call span, PR review latency, cross-team dependency backlog, SLA miss
- Structural symptom: informal lead shared between two people, shipped regression traced to
  a coordination gap, committee produces no decision output for two consecutive sessions
- Milestone event: first external customer onboards, first product ships with a compliance
  requirement

DO NOT proceed to Anti-Pattern Watch until the consistency check passes.

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
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (min 1 / max 2 rows,
         DRI required from roles block, no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to steps 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (with inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
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

## V-04 -- Combined: Formal Prose for C-23 + CONSTRAINTS Block for C-24/C-25

**axis:** lifecycle + output format (V-02 phrasing register for C-23 AND V-03 CONSTRAINTS
block for C-24/C-25)
**hypothesis:** V-02 and V-03 are orthogonal: V-02 changes only the Evolution Roadmap
alignment guard text; V-03 changes only the Block B constraints placement. No interference
predicted -- C-23 is in STRUCTURE-WARRANTED path, C-24/C-25 are in CAN-OPERATE-FLAT path.
If both pass at 17/17 aspirational, formal prose is a viable register for C-23 and pre-block
CONSTRAINTS are a viable format for C-24/C-25 independently. Falsifiable: if formal prose
in Evolution Roadmap and CONSTRAINTS block in Block B together produce a regression on one
of the three criteria, a cross-section interaction exists despite the path separation.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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

BLOCK B CONSTRAINTS -- confirm all before writing any rows:
  1. Row floor: at least one row. DO NOT produce an empty table.
  2. Row ceiling: at most two rows. DO NOT exceed two rows.
  3. DRI/Owner required: DO NOT leave any DRI / Owner cell blank.
  4. DRI/Owner source: each value must name a role from ROLES-LOADED or ROLES-NOTE only.
     DO NOT invent a role name not present in the roles block.
  5. Governance prohibition: DO NOT include a governance meeting, architecture board, or
     steering committee -- governance requires STRUCTURE-WARRANTED.

```
## Flat Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| [standup or sync] | [e.g., weekly] | [role from ROLES-LOADED] | [coordination purpose] |
| [review or demo] | [e.g., bi-weekly] | [role from ROLES-LOADED] | [review purpose] |
```

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

ORG EVOLUTION ROADMAP -- REQUIRED (ALIGNMENT GUARD ACTIVE)

DO produce this section after the Operating Rhythm section.
DO NOT label it optional.
DO NOT omit it.

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 -- headcount threshold at or beyond the Condition from slot 4] | [Named structural change] | [split / add-area / standing-committee / add-layer] |
| [Row 2 -- workload signal or structural symptom -- NOT a headcount number] | [Named structural change] | [type] |

ALIGNMENT GUARD -- The Row 1 threshold is structurally bound to the Condition committed to
in slot 4. The inertia gate and the first structural trigger in the Evolution Roadmap are two
facets of the same growth event: slot 4 names the Condition at which re-assessment is warranted;
Row 1 names the growth threshold at which structural change follows from that re-assessment.
These two values describe the same growth trajectory and must be consistent. A Row 1 threshold
that falls below the slot 4 Condition describes growth that precedes the gate -- it cannot be
a forward structural trigger. A Row 1 threshold authored independently of slot 4 introduces two
competing figures for the same growth event, which is structurally incoherent.

The rule: Row 1's headcount threshold is at or beyond the slot 4 Condition. If the Condition
is "headcount reaches 12," Row 1 names 12 or higher. Row 1 extends the growth trajectory
established at the gate; it does not restart or contradict it.

Requirements:
- At minimum two rows
- Row 1: headcount threshold at or beyond slot 4 Condition -- same growth event, not a new one
- Row 2: workload signal, structural symptom, or milestone -- NOT a second headcount number
- The same trigger dimension restated at a different threshold does not count as distinct
- Dimension vocabulary: on-call span, PR latency, dependency backlog, SLA miss, informal lead
  shared between two people, shipped regression, no-decision committee session, first external
  customer, first compliance requirement

Confirm Row 1 is consistent with slot 4 before proceeding to Anti-Pattern Watch.

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
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (min 1 / max 2 rows,
         DRI required from roles block, no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to steps 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (with inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
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

## V-05 -- Lifecycle Emphasis: Expanded WHY Rationale for C-23, C-24, C-25

**axis:** lifecycle emphasis (inline rationale explaining why each new constraint exists)
**hypothesis:** V-01/R7 states all three new constraints but does not explain the failure mode
each closes. A model that sees "at least one row" without context may treat it as style
guidance. A model that sees "at least one row -- without a floor, a zero-row table satisfies
the maximum constraint" understands the workaround being closed. Explicit failure-mode naming
may reduce technically-correct-but-non-compliant outputs. Single-axis: only WHY language is
added. All constraint text from V-01/R7 is preserved verbatim. Falsifiable: if expanded
rationale increases output length without improving compliance, lifecycle emphasis adds
verbosity without benefit.

---

You are running `/org-chart {topic}`.

---

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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

At least one row, at most two rows. DO NOT produce an empty table.
[WHY: "at most two rows" without a floor is satisfied by a zero-row shell -- the table header
exists but contains no operational content. The floor closes this workaround: the table must
provide at least one cadence a team can execute.]

DO NOT include a governance meeting, architecture board, or steering committee --
governance requires STRUCTURE-WARRANTED. If governance feels necessary, revisit
whether the verdict should be STRUCTURE-WARRANTED instead.

DRI MANDATE -- The DRI / Owner column is required. DO NOT leave any DRI / Owner cell blank.
Each row must name a role drawn from the ROLES-LOADED or ROLES-NOTE block. If ROLES-LOADED
has only one role, that role may appear in both rows. DO NOT invent a role name not present
in the roles block.
[WHY: blank DRI cells defeat the column's purpose -- the flat output has no authority map
if ownership is unnamed. Invented roles introduce inaccuracy: the ROLES-LOADED block is the
authoritative source for both flat and structured outputs. A role not present in the roles
block has no grounding in the team being described.]

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
[WHY: without this guard, two independently authored thresholds can describe incompatible
scales of the same growth event. A Condition of "headcount reaches 12" and a Row 1 of
"when headcount reaches 8" do not contradict each other structurally -- but the lower Row 1
threshold has already fired before the inertia gate triggers. The alignment guard makes Row 1
an extension of the gate commitment, not a separate figure that predates it.]

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
3. Branch: CAN-OPERATE-FLAT -> Owner Map -> Flat Operating Rhythm (min 1 / max 2 rows,
         DRI required from roles block, no governance) -> trigger carry-forward -> STOP
         STRUCTURE-WARRANTED -> continue to steps 4-8
4. ASCII Org Diagram
5. Headcount by Area (Decides / Escalates columns)
6. Operating Rhythm Table (with inline charters)
7. Org Evolution Roadmap (alignment guard: Row 1 >= slot 4 Condition)
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

## Predicted Scores Under v7

All five R7 variations carry C-23, C-24, and C-25. Discrimination under v7 requires scored
model outputs -- the open question is whether expression style affects compliance rate.

| V | C-23 | C-24 | C-25 | Predicted asp pass | Predicted composite | Notes |
|---|------|------|------|--------------------|---------------------|-------|
| V-01/R7 | PASS | PASS | PASS | 17/17 | 100.0 | Confirmed target: V-04/R6 + row floor |
| V-02/R7 | PASS | PASS | PASS | 17/17 | 100.0 | Formal prose for C-23; DO/DO NOT for C-24/C-25 |
| V-03/R7 | PASS | PASS | PASS | 17/17 | 100.0 | CONSTRAINTS block for C-24/C-25; DO/DO NOT for C-23 |
| V-04/R7 | PASS | PASS | PASS | 17/17 | 100.0 | Formal prose for C-23 + CONSTRAINTS block for C-24/C-25 |
| V-05/R7 | PASS | PASS | PASS | 17/17 | 100.0 | WHY rationale added to all three; no structural change |

All five are predicted to score 100.0 under v7. The R7 open question: which expression style
produces the highest compliance rate on real runs? If V-01/R7 (DO/DO NOT throughout) matches
V-03/R7 (pre-block CONSTRAINTS), format placement is not load-bearing. If V-02/R7 (formal
prose for C-23) outperforms V-01/R7, phrasing register for cross-section alignment guards
deserves promotion to a rubric-level concern.

**v8 candidate criteria from R7:**

R7 does not introduce new criteria -- all three new criteria (C-23, C-24, C-25) were
introduced in v7. R7 tests whether they can be reliably elicited under multiple expression
styles. If scored outputs show that one style consistently fails on C-23/C-24/C-25 while
others pass, the failing style is not a viable canonical form and the rubric should note the
constraint on expression. If all five hold at 100.0 on scored runs, the criteria are
expression-style-independent and the canonical form can be chosen on clarity grounds alone.

*Generated by: /quest:variate org-chart R7 -- 2026-03-16*
