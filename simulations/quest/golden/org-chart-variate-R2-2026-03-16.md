---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R2
rubric_version: v2
status: variate
---

# org-chart Variate -- Round 2

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v2 (C-01 through C-13; essential C-01--C-05; aspirational adds C-11/C-12/C-13)
**Round:** R2 -- single-axis (V-01/V-02/V-03) targeting new v2 criteria + combined (V-04/V-05)

---

## Round 2 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | rhythm-charter coupling | Each governance rhythm row is written as a row+charter pair -- the charter slot opens inline as the row is created, before the next row is permitted | Writing the charter immediately after the row it belongs to eliminates the C-11 failure mode (rhythm row present, charter absent) because the model cannot advance to the next row without completing the charter for the current one |
| V-02 | re-assessment trigger placement | The re-assessment trigger is a required slot placed BEFORE the VERDICT field in the inertia template, making it a precondition rather than a footnote | Placing the trigger before VERDICT forces the model to commit to a specific flip condition before choosing a verdict -- making C-12 (universal trigger regardless of verdict) a structural precondition rather than an afterthought |
| V-03 | verdict branching / hard section gating | CAN-OPERATE-FLAT verdict issues explicit SKIP directives that name Steps 3 and 4 as structurally absent, not reduced | Naming which sections are absent (rather than simplified) closes C-13 -- a "simplified hierarchy" passes C-07 but fails C-13; the SKIP directive removes the section entirely |
| V-04 | rhythm-charter coupling + re-assessment trigger placement | Combines V-01 row+charter pairing with V-02 pre-verdict trigger slot | C-11 and C-12 address independent structural gaps (rhythm completeness vs. trigger universality); combining them in one prompt imposes both constraints without conflict |
| V-05 | hard section gating + universal trigger + imperative register | Combines V-03 hard skip with V-02 trigger placement and the DO/DO NOT imperative register from R1-V-04 | Targeting all three new v2 criteria (C-11/C-12/C-13) simultaneously through prohibitions rather than instructions -- the model cannot orphan a rhythm row, cannot omit the trigger, and cannot produce org boxes under a flat verdict |

---

## V-01 -- Rhythm-Charter Coupling: Row-Plus-Charter Pairs

**axis:** rhythm-charter coupling
**hypothesis:** Making the charter the immediate continuation of its rhythm row -- write the row, then write the charter before moving to the next row -- eliminates the orphaned-rhythm-row failure (C-11). If the template treats each governance entry as a two-part unit (row + charter), the model cannot write a governance meeting row and defer or forget its charter. Falsifiable: if governance rows still appear without charters despite the paired format, the coupling constraint is being ignored rather than enforced structurally.

---

You are running `/org-chart {topic}`.

---

ROLES INPUT

Check `.roles/` for role files relevant to {topic} or the domain.

If roles exist, write before any other section:
```
ROLES-LOADED: [role-1], [role-2], ...
```

If no roles exist, write:
```
ROLES-NOTE: No .roles/ files found -- using inferred roles: [list]
```

---

INERTIA GATE

Before drawing any org box, answer the inertia question: can this team operate without
formal structure?

Write an `## Inertia Assessment` section containing:

- **Current coordination mode:** How does the team coordinate today? Name specific
  mechanisms -- which channels, standups, or informal leads exist right now.
- **Status-quo defense:** Argue the case for doing nothing. What is working? What
  is the switching cost of formalizing (reporting overhead, title weight, decision latency)?
- **Flat-team threshold:** The headcount or complexity level at which informal
  coordination fails for this team type. State whether the team is above or below
  that threshold today.
- **Re-assessment trigger:** The specific condition (headcount number, milestone event,
  or named failure mode) that would flip or revisit this verdict. "When the team grows"
  does not satisfy this field.
- **VERDICT:** `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` -- as a discrete labeled field.
- **Reasoning:** One or two sentences naming the specific failure mode or threshold
  condition that determined the verdict.

Do not write an org diagram until VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT:
  Produce a lightweight coordination model (ownership map, sync cadence) instead of
  a formal org chart. State the re-assessment trigger prominently. Skip the ASCII
  hierarchy and headcount table entirely.

If VERDICT is STRUCTURE-WARRANTED:
  Proceed to all sections below.

---

ASCII ORG DIAGRAM

Draw an ASCII hierarchy showing at minimum two levels and two distinct nodes.
Label committees or boards as separate nodes, not embedded in a single area's subtree.

---

HEADCOUNT BY AREA

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|

At minimum two area rows with distinct counts and a total row.
Decision Scope: name a specific decision class, not "owns the area."

---

OPERATING RHYTHM (ROW + CHARTER PAIRS)

Write the rhythm table one entry at a time. For every entry that names a committee,
board, or governance body: write the table row, then write the charter immediately
below it before writing the next table row.

**Table header:**

| Cadence | Frequency | DRI / Owner | Purpose | Type |
|---------|-----------|-------------|---------|------|

**Required entries (minimum three, each as a separate row):**

1. ROB or business review -- type: business-review
   (Write row only -- no charter required for operational meetings)

2. Shiproom or feature-gate meeting -- type: shiproom
   After writing this row, write its charter:
   ```
   **[Shiproom name] Charter**
   Purpose: [one sentence]
   Membership: [roles from ROLES-LOADED -- not personal names; minimum two roles]
   Decides: [what gate criteria are in scope]
   Escalates: [what goes to a higher body]
   ```

3. Governance meeting (architecture board, steering committee, or equivalent) -- type: governance
   After writing this row, write its charter:
   ```
   **[Governance body name] Charter**
   Purpose: [one sentence]
   Membership: [roles from ROLES-LOADED -- minimum two roles]
   Decides: [what decisions are in this body's authority]
   Escalates: [what this body sends to a higher body or individual]
   ```

For any additional governance or shiproom rows: write the row, then its charter, before
adding the next row. Do not write all rows first and charters second.

---

SECTION ORDER

1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment (with VERDICT)
3. ASCII Org Diagram (if STRUCTURE-WARRANTED)
4. Headcount by Area (if STRUCTURE-WARRANTED)
5. Operating Rhythm with inline charters

---

End with:
```
Generated by: /org-chart {topic} -- {date}
```

---

## V-02 -- Re-assessment Trigger Placement: Trigger Before VERDICT

**axis:** re-assessment trigger placement
**hypothesis:** Placing the re-assessment trigger as a required slot immediately BEFORE the VERDICT field makes it a precondition rather than an afterthought. C-12 requires the trigger regardless of which verdict is chosen -- but when the trigger appears after the verdict, the model tends to skip it if the verdict is already written. Reversing the order forces commitment to a specific flip condition before the verdict can be selected. Falsifiable: if C-12 still fails (trigger absent or platitude-level) despite the pre-verdict placement, the ordering has no protective effect and the issue is elsewhere.

---

You are running `/org-chart {topic}`.

---

ROLES INPUT

Check `.roles/` for role files relevant to {topic} or the domain.

Produce immediately:
```
ROLES-LOADED: [role names from .roles/]
```

If absent:
```
ROLES-NOTE: No .roles/ files found -- using inferred roles: [list]
```

---

INERTIA GATE

Write `## Inertia Assessment` as the first output section. Fill in every slot below.
Do not omit any slot and do not reorder the slots.

```
## Inertia Assessment

**Current coordination mode:**
[How does the team coordinate today? Name the specific mechanisms -- channels,
recurring meetings, informal leads -- that exist before any formal structure.]

**Status-quo defense:**
[Argue the case for doing nothing. What is the team doing instead of formalizing,
and is that actually insufficient? Name the switching cost.]

**Flat-team threshold:**
[The headcount or complexity level at which informal coordination fails for this
type of team. Is the team currently above or below that level?]

**Re-assessment trigger:**
[REQUIRED regardless of verdict. The specific condition that would flip or revisit
the verdict: a headcount number, a milestone event, a workload signal, or a named
failure mode. "When the team grows" does not satisfy this field.]

**VERDICT:** [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

**Reasoning:**
[One or two sentences. Must name the specific failure mode or threshold condition
that determined the verdict -- not a generic statement.]
```

The re-assessment trigger must appear in the inertia section even when VERDICT is
STRUCTURE-WARRANTED -- it names the condition that would prompt revisiting the
decision to add more structure, or to dissolve it.

Do not proceed to any downstream section until all six slots above are filled.

If VERDICT is CAN-OPERATE-FLAT:
  Produce a lightweight coordination model (ownership map + sync cadence) instead
  of a formal org chart. The re-assessment trigger you wrote above is the central
  output of the flat-team branch.

If VERDICT is STRUCTURE-WARRANTED:
  Proceed to all sections below.

---

ASCII ORG DIAGRAM

After the Inertia Assessment, draw an ASCII hierarchy showing at minimum two levels
and two distinct nodes. Committees or boards appear as separate labeled nodes.

---

HEADCOUNT BY AREA

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|
| [name] | [N or N-M] | [roles] | [decision class] |
| **Total** | **[N]** | | |

At minimum two area rows. Decision Scope column: name a decision class, not "owns the area."

---

OPERATING RHYTHM TABLE

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Required rows (distinct, not merged): ROB or business review, shiproom or feature-gate,
one governance meeting.

---

COMMITTEE CHARTERS

For each governance or shiproom meeting in the rhythm table, write:

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [roles from ROLES-LOADED -- minimum two]
Decides: [what is in scope]
Escalates: [what goes to a higher body]
```

---

SECTION ORDER

1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment (six slots, trigger before VERDICT)
3. ASCII Org Diagram (if STRUCTURE-WARRANTED)
4. Headcount by Area (if STRUCTURE-WARRANTED)
5. Operating Rhythm Table
6. Committee Charters

---

End with:
```
Generated by: /org-chart {topic} -- {date}
```

---

## V-03 -- Verdict Branching: Hard Section Skip for Flat Verdict

**axis:** lifecycle emphasis / verdict branching
**hypothesis:** Declaring Steps 3 and 4 (org diagram and headcount table) as structurally absent -- not simplified -- when VERDICT is CAN-OPERATE-FLAT closes the C-13 failure mode. C-07 (recommended) is satisfied by a "simplified hierarchy"; C-13 (aspirational) is satisfied only when those sections are entirely absent. The SKIP directive must name the sections by step number so the model cannot substitute a reduced version. Falsifiable: if a simplified org diagram still appears under CAN-OPERATE-FLAT despite the SKIP directive, explicit step-level gating is insufficient and the flat-verdict branch needs a stronger structural break.

---

You are running `/org-chart {topic}`.

---

STEP 1 -- READ ROLES

Check `.roles/` for role files relevant to {topic}.

```
ROLES-LOADED: [roles from .roles/]
```

or if absent:

```
ROLES-NOTE: No .roles/ files found -- using inferred roles: [list]
```

Do not proceed to Step 2 until this block is written.

---

STEP 2 -- INERTIA ASSESSMENT

Write `## Inertia Assessment` containing:
- Current coordination mode (name the specific mechanisms)
- Status-quo defense (what is working today; what would be lost by formalizing)
- Flat-team threshold (a number or named condition)
- Re-assessment trigger (a specific number, milestone, or failure mode)
- `VERDICT: CAN-OPERATE-FLAT` or `VERDICT: STRUCTURE-WARRANTED` as a labeled field
- Reasoning (specific failure mode or threshold, not generic)

Do not write any org box until VERDICT is written.

---

VERDICT BRANCH -- READ BEFORE CONTINUING

```
IF VERDICT IS CAN-OPERATE-FLAT:
  SKIP Step 3.  <-- org diagram section is absent, not simplified
  SKIP Step 4.  <-- headcount table is absent, not simplified
  Proceed directly to Step 5.
  The output for a flat team is a coordination model only:
    - Ownership map (who owns which area or workstream -- no hierarchy boxes)
    - Sync cadence (meeting frequency, not a formal rhythm table)
    - The re-assessment trigger from Step 2 stated prominently
  Do not draw ASCII boxes. Do not produce a headcount table.
  A "simplified hierarchy" or "compact headcount" still fails -- these sections
  must be absent.

IF VERDICT IS STRUCTURE-WARRANTED:
  Continue to Step 3.
```

---

STEP 3 -- ASCII ORG DIAGRAM (STRUCTURE-WARRANTED only)

[Reached only when VERDICT is STRUCTURE-WARRANTED.]

Draw an ASCII hierarchy showing at minimum two levels and two distinct nodes.
Every named node uses a role name from Step 1. Committees shown as separate labeled nodes.

---

STEP 4 -- HEADCOUNT BY AREA (STRUCTURE-WARRANTED only)

[Reached only when VERDICT is STRUCTURE-WARRANTED.]

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|

At minimum two area rows with distinct counts. Total row required.
Decision Scope: name a specific decision class per row.

---

STEP 5 -- OPERATING RHYTHM TABLE

Write a cadence table. Required rows (distinct, not merged):
1. ROB or business review
2. Shiproom or feature-gate meeting
3. Governance meeting (architecture board, steering committee, or equivalent)

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

For a flat team (CAN-OPERATE-FLAT), this section contains only the sync cadence
and ownership map described in the VERDICT BRANCH above -- not a formal rhythm table.

---

STEP 6 -- COMMITTEE CHARTERS (STRUCTURE-WARRANTED only)

For each governance or shiproom meeting in the rhythm table:

```
**[Name] Charter**
Purpose: [one sentence]
Membership: [roles -- minimum two, not personal names]
Decides: [scope]
Escalates: [what goes up]
```

---

ARTIFACT OUTPUT

Section order for `org-chart.md`:
- CAN-OPERATE-FLAT verdict: Steps 1, 2, 5 (coordination model)
- STRUCTURE-WARRANTED verdict: Steps 1, 2, 3, 4, 5, 6

End with:
```
Generated by: /org-chart {topic} -- {date}
```

---

## V-04 -- Rhythm-Charter Coupling + Universal Trigger (Combined)

**axis:** rhythm-charter coupling + re-assessment trigger placement
**hypothesis:** Combining the row+charter pairing (V-01) with the pre-verdict trigger slot (V-02) closes both C-11 and C-12 simultaneously. C-11 (orphaned rhythm rows) and C-12 (universal trigger) address independent structural gaps that do not conflict -- a prompt can require inline charters while also requiring the trigger before the verdict. Falsifiable: if either C-11 or C-12 still fails despite the combination, one of the two mechanisms is being overridden by the other or by unrelated factors.

---

You are running `/org-chart {topic}`.

---

STEP 1 -- READ ROLES

Check `.roles/` for role files relevant to {topic}.

Produce a ROLES-LOADED block:
```
ROLES-LOADED: [role names]
```

or if absent:
```
ROLES-NOTE: No .roles/ files found -- using inferred roles: [list]
```

Do not proceed until this block is written.

---

STEP 2 -- INERTIA ASSESSMENT

Write `## Inertia Assessment`. Fill in all slots in this order (do not reorder):

```
## Inertia Assessment

**Current coordination mode:**
[Specific mechanisms -- channels, standups, informal leads -- that exist today]

**Status-quo defense:**
[The case for doing nothing: what is working, what the switching cost is]

**Flat-team threshold:**
[Headcount or complexity level at which informal coordination fails -- a number
or named condition; is the team above or below it today?]

**Re-assessment trigger:**
[A specific headcount, milestone, or named failure mode that would flip or
revisit this verdict. Required regardless of which verdict you choose.
"When the team grows" does not satisfy this field.]

**VERDICT:** [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

**Reasoning:**
[One or two sentences naming the specific condition that determined the verdict]
```

The re-assessment trigger is required for both verdicts -- for CAN-OPERATE-FLAT it
names the condition to revisit; for STRUCTURE-WARRANTED it names when to consider
simplifying.

Do not write an org diagram until VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT:
  Produce a lightweight coordination model (ownership map, sync cadence) instead of
  a formal org chart. Skip the org diagram and headcount table.

If VERDICT is STRUCTURE-WARRANTED:
  Proceed to Step 3.

---

STEP 3 -- ASCII ORG DIAGRAM (STRUCTURE-WARRANTED only)

Draw an ASCII hierarchy showing at minimum two levels and two distinct nodes.
Every node label uses a role name from Step 1. Committees appear as separate labeled nodes.

---

STEP 4 -- HEADCOUNT BY AREA (STRUCTURE-WARRANTED only)

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|
| [name] | [N or N-M] | [roles from Step 1] | [decision class] |
| **Total** | **[N]** | | |

At minimum two area rows. Decision Scope must name a specific decision class per row.

---

STEP 5 -- OPERATING RHYTHM WITH INLINE CHARTERS

Write the rhythm table and charters as paired units. For every governance or shiproom
row: write the row, then write its charter immediately below before adding the next row.

**Table header:**

| Cadence | Frequency | DRI / Owner | Purpose | Type |
|---------|-----------|-------------|---------|------|

**Required entries (each a separate row + charter where applicable):**

**Entry 1 -- Business review (type: business-review)**
Write the row. No charter required for operational reviews.

**Entry 2 -- Shiproom or feature-gate (type: shiproom)**
Write the row.
Then immediately write its charter:
```
**[Shiproom name] Charter**
Purpose: [one sentence]
Membership: [roles from Step 1 -- minimum two]
Decides: [gate criteria in scope]
Escalates: [what goes to a higher body]
```

**Entry 3 -- Governance meeting (type: governance)**
Write the row.
Then immediately write its charter:
```
**[Governance body name] Charter**
Purpose: [one sentence]
Membership: [roles from Step 1 -- minimum two]
Decides: [decisions in this body's authority]
Escalates: [decisions sent to a higher body]
```

For any additional governance or shiproom entries: row then charter before the next entry.
Do not batch all rows first and all charters second.

---

SECTION ORDER

1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment (trigger before VERDICT)
3. ASCII Org Diagram (STRUCTURE-WARRANTED only)
4. Headcount by Area (STRUCTURE-WARRANTED only)
5. Operating Rhythm with inline charters

---

End with:
```
Generated by: /org-chart {topic} -- {date}
```

---

## V-05 -- Hard Skip + Universal Trigger + Imperative Register (Combined)

**axis:** verdict branching + re-assessment trigger placement + phrasing register
**hypothesis:** Combining hard SKIP directives (V-03), pre-verdict trigger placement (V-02), and DO/DO NOT imperative phrasing (from R1-V-04) closes all three new v2 criteria in one prompt. C-11 is addressed by prohibiting rhythm rows without charters; C-12 is addressed by requiring the trigger before VERDICT; C-13 is addressed by hard SKIP directives on Steps 3-4 under CAN-OPERATE-FLAT. The imperative register prevents the model from treating any of these as advisory. Falsifiable: if all three new criteria still fail despite the combined approach, the constraints are being structurally ignored and a different mechanism (e.g., output validation schema) is needed.

---

You are running `/org-chart {topic}`.

---

ROLES -- DO THIS FIRST

DO check `.roles/` before writing anything.
DO write a ROLES-LOADED block listing every role found.
DO NOT invent role names that contradict roles already defined.
If no roles exist: DO write `ROLES-NOTE: No .roles/ files found -- using inferred roles: [list]`
DO reference loaded role names in the org diagram, headcount table, and rhythm table.

---

INERTIA GATE -- COMPLETE ALL SLOTS BEFORE CONTINUING

DO write `## Inertia Assessment` as the first output section.
DO NOT write an org diagram as the first section.
DO NOT skip the inertia assessment.

The Inertia Assessment MUST include ALL of these slots in this order:

1. **Current coordination mode** -- name specific mechanisms, not "the team coordinates informally"
2. **Status-quo defense** -- argue for doing nothing; name the switching cost
3. **Flat-team threshold** -- a headcount number or named condition; state current position
4. **Re-assessment trigger** -- a specific number, milestone, or failure mode
   DO NOT write "when the team grows"
   DO fill this in regardless of which verdict you are going to choose
   DO fill this in BEFORE writing the VERDICT line
5. **VERDICT: CAN-OPERATE-FLAT** or **VERDICT: STRUCTURE-WARRANTED** -- discrete labeled field
6. **Reasoning** -- one or two sentences naming the specific condition

DO NOT write a VERDICT without a reasoning field.
DO NOT write a reasoning field without a re-assessment trigger above it.
DO NOT proceed past the Inertia Assessment until all six slots are filled.

---

VERDICT BRANCH -- READ AND FOLLOW EXACTLY

```
IF VERDICT IS CAN-OPERATE-FLAT:

  DO SKIP Step 3 (org diagram). The org diagram section is ABSENT.
  DO SKIP Step 4 (headcount table). The headcount table is ABSENT.
  DO NOT draw any ASCII hierarchy.
  DO NOT produce a "simplified" or "compact" org chart.
  DO NOT produce a headcount table in any form.
  A reduced org diagram still fails -- these sections must not exist.

  DO proceed directly to Step 5.
  DO produce a coordination model containing:
    - Ownership map (who owns which area or workstream, in prose or a flat list)
    - Sync cadence (when the team meets and why)
  DO state the re-assessment trigger from the Inertia Assessment prominently.

IF VERDICT IS STRUCTURE-WARRANTED:

  DO proceed to Step 3.
  DO complete all remaining steps.
```

---

STEP 3 -- ASCII ORG DIAGRAM (STRUCTURE-WARRANTED only)

DO draw an ASCII hierarchy after the Inertia Assessment.
DO show at minimum two levels.
DO label committees or boards as distinct nodes -- not embedded in one area's subtree.
DO NOT produce a flat list of names without hierarchy.
DO use role names from ROLES-LOADED for node labels.

---

STEP 4 -- HEADCOUNT BY AREA (STRUCTURE-WARRANTED only)

DO produce a headcount table immediately after the org diagram.
DO include at minimum two distinct area rows with individual counts.
DO NOT produce only a single aggregate total.
DO fill in Decision Scope for every area row.
DO NOT write "owns the area" -- name a specific decision class.

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|

DO include a totals row.

---

STEP 5 -- OPERATING RHYTHM WITH CHARTERS

DO produce a cadence table.
DO include at minimum three distinct rows: ROB, shiproom, and governance -- one each.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.

| Cadence | Frequency | DRI / Owner | Purpose | Type |
|---------|-----------|-------------|---------|------|

DO reference a role from ROLES-LOADED in DRI / Owner where possible.

For every governance or shiproom row:
DO write the charter immediately after the row before adding the next row.
DO NOT write a rhythm row for a committee and then omit its charter.
DO NOT batch all rhythm rows first and all charters second.

Charter format (required per governance / shiproom row):
```
**[Name] Charter**
Purpose: [one sentence -- what question does this body answer?]
Membership: [roles from ROLES-LOADED -- minimum two, not personal names]
Decides: [at minimum one specific decision type]
Escalates: [at minimum one item sent to a higher body]
```

DO NOT write "makes decisions" without naming the scope.

---

SECTION ORDER -- DO NOT REORDER, DO NOT OMIT

For STRUCTURE-WARRANTED:
1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment (trigger before VERDICT)
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm with inline charters

For CAN-OPERATE-FLAT:
1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment (trigger before VERDICT)
3. [SKIP -- absent]
4. [SKIP -- absent]
5. Coordination model (ownership map + sync cadence)

DO NOT reorder sections.
DO NOT emit "[SKIP]" labels in the final artifact -- just omit those sections entirely.

---

DO end with exactly:
```
Generated by: /org-chart {topic} -- {date}
```
DO NOT emit placeholder text in the final line.

---

*Generated by: /quest:variate org-chart R2 -- 2026-03-16*
