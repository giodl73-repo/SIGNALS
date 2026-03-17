out = "C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v2-2026-03-16.md"
text = """\
---
skill: quest-rubric
skill_target: org-chart
date: 2026-03-16
version: 2
---

# Scoring Rubric -- org-chart

**Skill:** `/org-chart {topic}`
**Purpose:** Score whether an org-chart output is structurally sound and operationally useful.
**Composite formula:** `(essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)`
**Golden threshold:** All essential criteria pass AND composite >= 80.

---

## Essential Criteria (must all pass)

### C-01 -- Inertia assessment gate
**Category:** behavior
**Weight:** essential

The output must contain a labeled inertia assessment section that explicitly answers
whether the team can operate without formal structure -- before any org diagram is drawn.

**Pass condition:** A named section (e.g. "Inertia Assessment") is present and appears
before the ASCII org diagram. The section must include an explicit verdict field with one
of two values: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. Generic introductory paragraphs
that mention "org structure is important" do not satisfy this criterion -- the verdict must
be a discrete, named field.

---

### C-02 -- ASCII org diagram with hierarchy
**Category:** format
**Weight:** essential

The output must include an ASCII org diagram showing at least two levels of hierarchy
and at least two distinct nodes (a single person listed without hierarchy is not an org).

**Pass condition:** ASCII art or indented tree is present. At minimum one top-level node
and one second-level node are visible. A flat list of names without structural hierarchy
does not pass. Committees or boards, if present, are shown as distinct labeled nodes
rather than embedded inline in a single area's subtree.

---

### C-03 -- Roles input acknowledged
**Category:** behavior
**Weight:** essential

The output must acknowledge whether `.craft/roles/` contains role definitions for the
domain. Silence about roles is not acceptable.

**Pass condition:** One of two conditions is met:
(a) A ROLES-LOADED line or block lists role names sourced from `.craft/roles/`, or
(b) An explicit ROLES-NOTE states that no `.craft/roles/` files were found and that
    inferred roles are being used.
The acknowledgment must appear before or within the org diagram section.

---

### C-04 -- Headcount table with area breakdown
**Category:** correctness
**Weight:** essential

The output must include a headcount table that breaks down team size by area.
A single aggregate total without area breakdown does not satisfy this criterion.

**Pass condition:** A markdown table is present with at minimum two distinct area rows,
each carrying a numeric headcount (exact or range). A totals row must be present.
The Key Roles or equivalent column must be populated (not blank).

---

### C-05 -- Operating rhythm table covers three meeting types
**Category:** coverage
**Weight:** essential

The output must include a structured operating rhythm table with at minimum three
distinct entries representing: (1) a business review (ROB or equivalent), (2) a
shiproom or feature-gate meeting, and (3) a governance meeting (architecture board,
steering committee, or equivalent).

**Pass condition:** Three or more rows are present. At least one row maps to each of
the three meeting types above. Two meetings merged into one row to reach the minimum
does not pass. Each row must have at minimum: cadence name, frequency, and purpose.

---

## Recommended Criteria (output is better with these)

### C-06 -- Committee charters include all three elements
**Category:** depth
**Weight:** recommended

For each governance or shiproom meeting listed in the rhythm table, the output should
provide a mini-charter with: (a) a purpose statement, (b) membership by role (not by
personal name), and (c) an explicit authority scope (what this committee decides vs.
what it escalates).

**Pass condition:** At least one committee charter is present that contains all three
elements: purpose (one sentence), membership (two or more roles listed), and
decides/escalates split (at least one item on each side). Generic statements such as
"this committee makes decisions" without specifying scope do not satisfy the authority
element.

---

### C-07 -- Verdict drives output shape
**Category:** behavior
**Weight:** recommended

The inertia verdict (C-01) should determine what the output contains. A CAN-OPERATE-FLAT
verdict should produce a lightweight coordination model, not a full hierarchical org chart.
A STRUCTURE-WARRANTED verdict should produce the full output.

**Pass condition:** If VERDICT is CAN-OPERATE-FLAT, the output omits or explicitly
defers the formal ASCII hierarchy and instead provides an informal coordination model
(ownership map, sync cadence) plus a re-assessment trigger. If VERDICT is
STRUCTURE-WARRANTED, all remaining sections (diagram, headcount, rhythm) are present.
An output that states CAN-OPERATE-FLAT and then proceeds to draw a full org chart
does not pass.

---

### C-08 -- Decision scope column in headcount table
**Category:** depth
**Weight:** recommended

The headcount table should include a column that specifies what each area owns
versus escalates -- not just who sits in the area.

**Pass condition:** The headcount table contains a "Decision Scope," "Decides," or
equivalent column with non-trivial content for each area row. Entries like "owns the
area" or "responsible for outcomes" do not pass. Entries must name a decision class
(e.g., "ship/no-ship for in-sprint changes," "cross-area API contracts") or an explicit
escalation path.

---

## Aspirational Criteria (raise the bar once essential/recommended are stable)

### C-09 -- Concrete re-assessment trigger
**Category:** depth
**Weight:** aspirational

Regardless of which verdict was chosen, the output should state a specific condition
that would flip or revisit the verdict -- not a platitude like "when the team grows."

**Pass condition:** A re-assessment trigger is stated somewhere in the inertia section
or operating rhythm. The trigger must be specific: a headcount number, a milestone
event, a workload signal, a geographic distribution threshold, or a named failure mode
that has materialized. Statements like "revisit when the team scales" or "as the org
matures" do not pass.

---

### C-10 -- Role names appear in two or more sections
**Category:** correctness
**Weight:** aspirational

Role names sourced from `.craft/roles/` (or from the inferred roles list when no role
files exist) should propagate into at least two output sections, not just be listed once
at the top.

**Pass condition:** Role names established in the roles-input acknowledgment (C-03)
appear in at least two of the following: the ASCII org diagram, the headcount table's
Key Roles column, a committee membership list, or the rhythm table's DRI/Owner column.
An output that lists roles at the top and then uses generic titles ("Team Lead," "Engineer")
everywhere else does not pass.

---

### C-11 -- Rhythm-charter linkage (no orphaned rhythm rows)
**Category:** depth
**Weight:** aspirational

*New in v2. Source: V-04 "DO NOT write a rhythm row and omit its charter."*

Every governance meeting row in the operating rhythm table should have a corresponding
charter entry. A rhythm table that lists a steering committee or architecture board but
provides no charter is incomplete -- the meeting exists without authority definition.

**Pass condition:** For every row in the rhythm table that designates a committee,
board, or governance body (as opposed to a team standup or feature review), a
corresponding charter entry exists covering purpose, membership, and authority scope.
Rhythm rows for a meeting that has no charter do not pass. If no governance meetings
are listed (edge case: flat team), this criterion is vacuously satisfied.

---

### C-12 -- Universal re-assessment trigger field
**Category:** depth
**Weight:** aspirational

*New in v2. Source: V-02 explicit "Re-assessment trigger" slot required regardless of verdict.*

The inertia section should contain a named "Re-assessment trigger" field for all
verdicts -- not only when the verdict is CAN-OPERATE-FLAT. STRUCTURE-WARRANTED outputs
also need a trigger that would prompt revisiting the decision to add structure.

**Pass condition:** A labeled "Re-assessment trigger" (or equivalent named field) is
present in the inertia section and is non-empty for whichever verdict was chosen.
A trigger buried in prose or mentioned only in the CAN-OPERATE-FLAT branch does not
pass. The field must be present regardless of verdict.

---

### C-13 -- Hard section skip for flat verdict
**Category:** behavior
**Weight:** aspirational

*New in v2. Source: V-03 "Proceed directly to Step 5 -- Steps 3-4 structurally absent" for flat verdict.*

When VERDICT is CAN-OPERATE-FLAT, the org diagram and headcount table sections should be
structurally absent -- not present in a lighter form. Producing a "simplified hierarchy"
or a "compact headcount table" for a flat team dilutes the verdict's meaning.

**Pass condition:** When VERDICT is CAN-OPERATE-FLAT, no ASCII org diagram and no
headcount table appear in the output. The output jumps directly to the coordination
model and operating rhythm. A reduced or annotated org diagram ("shown for reference
only") does not satisfy this criterion. This criterion applies only when the verdict
is CAN-OPERATE-FLAT; it is vacuously satisfied for STRUCTURE-WARRANTED outputs.

---

## Scoring Reference

| Tier | Criteria IDs | Count | Weight | Max points |
|------|-------------|-------|--------|-----------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60% | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30% | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13 | 5 | 10% | 10 |

**Composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)**

**Golden:** All 5 essential pass AND composite >= 80.

---

## v2 Change Log

| Added | Source |
|-------|--------|
| C-11 Rhythm-charter linkage | V-04: "DO NOT write a rhythm row and omit its charter" |
| C-12 Universal re-assessment trigger field | V-02: explicit slot required for all verdicts, not only CAN-OPERATE-FLAT |
| C-13 Hard section skip for flat verdict | V-03: Steps 3-4 structurally absent when VERDICT is CAN-OPERATE-FLAT |

**Aspirational denominator updated:** 2 -> 5. All existing scores remain comparable --
C-09 and C-10 weights are now diluted by the larger denominator, reflecting that the
aspirational tier has grown richer.

---

*Generated by: /quest:rubric org-chart -- 2026-03-16 v2*
"""
with open(out, "w", encoding="utf-8") as f:
    f.write(text)
print("written", len(text), "bytes to", out)
