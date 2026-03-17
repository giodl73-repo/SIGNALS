Now I have the full picture. R12-V-05 is the baseline (240/240 under v12). The two v13 gaps are:

- **C-39**: STRUCTURING-COST FRAME must have an *explicit* positional constraint instruction (before mechanism table) — not just be physically positioned there
- **C-40**: GATE CHAIN ARTIFACT-HANDOFF INVENTORY must be *explicitly declared* as a pre-GATE 0 preamble (forward-declaring contract) — not just happen to precede GATE 0

Writing the 5 variations now.

---

# org-chart Variate -- Round 13 (Rubric v13)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v13 (C-01 through C-40; C-39/C-40 new from R12 excellence signals)
**Round:** R13 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

## R12 ceiling and R13 target

R12-V-05 achieves full coverage of C-01 through C-38 under the v12 rubric (240 pts).
Under v13, R12-V-05 scores 240/250: all v12 criteria pass, but both new v13 criteria
(C-39 and C-40, 5 pts each) are absent.

**C-39 gap (STRUCTURING-COST FRAME pre-mechanism table position):**
R12-V-05 GATE 1 has the STRUCTURING-COST FRAME physically placed before Step 1.0 (via
the "[Zone: before Step 1.0]" label and a DO instruction). C-37 is satisfied. C-39
closes the bypass C-37 leaves open: C-37 requires presence and content but not an
explicit positional constraint instruction. A model satisfying C-37 can place the frame
after the mechanism table as a cost-summary. R12-V-05 does not explicitly state *why*
the pre-mechanism position is structurally required, does not name the prohibited form
(post-mechanism placement as cost-summary derived from rows already written), and does
not add a DO NOT guard preventing mechanism rows before the frame is complete.
The "[Zone: before Step 1.0]" label positions the frame before the default-position
statement (Step 1.0) but does not identify the mechanism table (Step 1.1) as the
positional boundary. The causal explanation (interpretive premise vs. derived conclusion)
is absent.

**C-40 gap (GATE CHAIN block pre-GATE 0 preamble position):**
R12-V-05 places the ARTIFACT-HANDOFF INVENTORY within the GATE CHAIN CONTRACT section,
which physically precedes GATE 0. C-38 is satisfied. C-40 closes the bypass C-38 leaves
open: C-38 requires block existence and enumeration completeness but not an explicit
preamble declaration. A model satisfying C-38 can place the consolidated inventory after
GATE 3 as a terminal appendix. R12-V-05 does not explicitly label the block as a
preamble, does not instruct the model to read it before GATE 0 begins, does not name
the prohibited form (post-GATE 3 retrospective record), and does not explain why the
pre-GATE 0 position is structurally required (forward-declaring contract vs. retrospective
record).

---

## R13 Variation Map

| V    | Axis                                                       | C-39 | C-40 | Predicted |
|------|------------------------------------------------------------|------|------|-----------|
| V-01 | Lifecycle emphasis (R13 control; R12-V-05 verbatim)       | no   | no   | 240/250   |
| V-02 | Output format (C-40 preamble-position declaration only)   | no   | yes  | 245/250   |
| V-03 | Inertia framing (C-39 pre-mechanism-table constraint only)| yes  | no   | 245/250   |
| V-04 | Combined (C-39 + C-40 both explicit positional)           | yes  | yes  | 250/250   |
| V-05 | Maximum integration (V-04 + checkpoint position guards)   | yes  | yes  | 250/250   |

**Single-axis hypotheses:**
- V-01: R12-V-05 baseline. C-39 and C-40 both absent. 240/250 = 96%. R13 control.
- V-02: Adds only the C-40 preamble position declaration. Tests whether the forward-
  declaring contract framing and retrospective-record prohibition are sufficient for C-40
  independent of C-39. C-40 PASS predicted; C-39 absent; +5 pts. 245/250.
- V-03: Adds only the C-39 pre-mechanism-table position constraint (DO NOT guard, causal
  explanation, prohibited form named). Tests whether the positional boundary and bypass
  prevention are sufficient for C-39 independent of C-40. C-39 PASS predicted; C-40
  absent; +5 pts. 245/250.
- V-04: Both C-39 and C-40 positional constraints added. C-39 + C-40 PASS predicted.
  First R13 variation targeting full 250/250.
- V-05: V-04 + checkpoint items explicitly verifying positional constraints at
  CHECKPOINT-0 and CHECKPOINT-INERTIA. Hypothesis: checkpoint enforcement of positional
  rules makes the constraint non-bypassable at execution time. 250/250 predicted with
  stronger enforcement guarantee.

---

## V-01 -- Lifecycle Emphasis (R13 Control; R12-V-05 Verbatim)

**Axis:** lifecycle emphasis -- R12-V-05 unchanged; every gate boundary,
sub-section, and checkpoint present as in R12's maximum-integration variation;
no C-39 or C-40 positional constraint additions.
**Hypothesis:** R12-V-05 achieves all C-01 through C-38 (240 pts under v12). Under v13
both new positional criteria are absent. The STRUCTURING-COST FRAME is physically before
the mechanism table but no explicit DO NOT guard or causal explanation for that position
exists. The ARTIFACT-HANDOFF INVENTORY precedes GATE 0 physically but is not declared
as a preamble, does not name the prohibited form, and does not instruct the model to
read it before GATE 0. Composite predicted: 240/250 (96.0%). R13 control point.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Sequence provable from
gate labels. Every gate carries a dedicated verification checkpoint before STATUS.

ARTIFACT-HANDOFF INVENTORY:
  GATE 0 -> GATE 1: typed role list
    Produced by: Step 0.2 ROLE-TYPE-CLASSIFICATION
    Required by: GATE 1 (role names used in mechanism table and inertia reasoning)
  GATE 1 -> GATE 2: inertia verdict + FLAT-CASE-PRESSURE rating
    Produced by: Step 1.4 anchor steps 1 and 3 (FLAT-CASE-PRESSURE + VERDICT)
    Required by: GATE 2 (structural sections only begin if VERDICT = STRUCTURE-WARRANTED)
  GATE 2 -> GATE 3: org diagram with typed nodes
    Produced by: Step 2.1 ASCII Org Diagram + Step 2.2 Headcount by Area
    Required by: GATE 3 Step 3.1 (committee nodes must match diagram; all Escalates
    destinations must name nodes present in the diagram)
  GATE 3 -> STATUS: complete charter set
    Produced by: Step 3.1 interleaved rhythm/charter pairs + CHARTER-FORMAT-AUDIT loop
    Required by: final STATUS (emits only after GATE 3 STATUS PASS; charter set is the
    terminal artifact)

This ARTIFACT-HANDOFF INVENTORY is the authoritative cross-gate traceability reference.
Each gate section also carries a local "Named artifact handoff" line consistent with this
inventory. If any local declaration conflicts with this inventory, this inventory governs.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list (see ARTIFACT-HANDOFF INVENTORY: GATE 0 -> GATE 1)

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block; no structural content between steps. Every role
typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced:
DECISION first, EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed until every role from Step 0.1 is typed.

**CHECKPOINT-0** -- ROLES-LOADED/NOTE present; all roles typed; containment satisfied;
no structural content between 0.1 and 0.2.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 0 -> GATE 1).
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating (see ARTIFACT-HANDOFF INVENTORY: GATE 1 -> GATE 2)

GATE 1 DO/DO NOT:
- DO: Emit STRUCTURING-COST FRAME block before Step 1.0.
- DO: Write default-position statement (Step 1.0) before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Use numbered anchor sequence in Step 1.4 (not a narrative paragraph).
- DO NOT: Write diagram, headcount, rhythm, or charter content before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII diagram nodes, headcount area rows, rhythm cadence rows,
charter fields (Mission, Membership, Quorum, Escalates).

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT** [Zone: before Step 1.0]

Before any flat-case argument, enumerate the overhead imposed by formal structure.
This frame establishes the cost denominator: structure must produce net savings
greater than this overhead to be warranted. VERDICT anchor step 3 must cite the
dominant cost category named here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter authoring, role assignment, initial standing-meeting design -- eng-weeks for
     first governance cycle; include time spent by all named roles in setup, not just PM]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries; handoff
     latency introduced for work previously handled informally -- eng-weeks/qtr]
  Governance cadence tax:
    [steady-state recurring meeting load across all governance committees -- eng-hours/qtr
     converted to eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews,
     charter revision, quorum coordination, decision logging]
```

VERDICT (anchor step 3) must declare whether flat coordination cost exceeds or falls
below this governance overhead, naming the dominant cost category.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step. MUST precede the mechanism table. Not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
Two-step separator:
- Count rows. If < 2, produce missing rows first.
- When count >= 2, emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

GUARD: DO NOT emit separator before count >= 2. DO NOT begin Step 1.2 before separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list Step 1.1 mechanism rows.

**Step 1.3 -- Rebuttal**

Name the ONE failure mode flat coordination cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude).

```
UNCOVERED: [decision class or function with no current owner under flat structure]
```

**Step 1.4 -- VERDICT: SUB-SECTION-4-ANCHOR-SEQUENCE**

Complete the following numbered anchor sequence in order. Each step is a labeled output
item. DO NOT collapse into a narrative paragraph. The sequence IS the sub-section.

```
1. FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]
   Evidence: [N] mechanisms at [cost anchor from FLAT-CASE-CLOSED]; dominant flat
   coordination mode: [mechanism type from Step 1.1]

2. NET-COST-COMPARISON:
   | Cost Category                         | Flat Coordination      | Formal Structure        |
   |---------------------------------------|------------------------|-------------------------|
   | Inertia mechanisms (from FLAT-CASE)   | [X eng-weeks/qtr]      | [X eng-weeks/qtr]       |
   | Committee formation + maintenance     | --                     | [Y eng-weeks/qtr]       |
   | Governance cadence tax (from FRAME)   | --                     | [Y eng-weeks/qtr]       |
   | UNCOVERED failure-mode cost           | [Z eng-weeks/qtr]      | [reduced Z eng-weeks]   |
   | Net total                             | [T_flat eng-weeks/qtr] | [T_struct eng-weeks/qtr]|
   Net delta: T_struct - T_flat = [signed value]
   Interpretation: positive = structure costs more; negative = structure produces net savings.

3. VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
   Basis: net delta is [positive/negative]; dominant cost from STRUCTURING-COST FRAME
   is [category]; this [exceeds / is exceeded by] the UNCOVERED failure-mode cost.

4. RE-ASSESSMENT TRIGGER: [concrete measurable threshold; not "revisit as the team grows";
   must be independently verifiable; e.g., "when UNCOVERED failure-mode cost exceeds [N]
   eng-weeks/qtr for two consecutive quarters" or "when headcount in [area] crosses [N]"]
```

Flat-verdict branch -- if VERDICT = CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] STRUCTURING-COST FRAME present before Step 1.0; all three cost categories populated
  (committee formation, role specialization overhead, governance cadence tax)
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set; FLAT-CASE-CLOSED separator emitted
- [ ] Step 1.4 uses numbered anchor sequence 1-4 (not a narrative paragraph)
- [ ] NET-COST-COMPARISON table present at anchor step 2 with signed net delta declared
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED}; cites dominant FRAME cost
- [ ] RE-ASSESSMENT TRIGGER concrete; not growth-narrative
- [ ] No GATE 1 prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 1 -> GATE 2).
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** org diagram with typed nodes (see ARTIFACT-HANDOFF INVENTORY: GATE 2 -> GATE 3)

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row. All Escalates destinations name specific diagram nodes.

**CHECKPOINT DIAGRAM-CHECK** -- diagram levels, role sourcing, committees distinct,
5-column headcount, Decides/Escalates split, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 2 -> GATE 3).
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
  (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** complete charter set (see ARTIFACT-HANDOFF INVENTORY: GATE 3 -> STATUS)

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm rows first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in any charter Membership.
- DO NOT: Write Quorum without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract):
- Appendices of any kind
- Supplementary sections (tables, notes, annexes)
- Editorial commentary after Anti-Pattern Watch table
- Charters not paired with an operating rhythm row
- Any content outside Steps 3.1 through 3.5

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.
For each governance row, immediately produce its charter before the next ORT row.

Charter template:
```
### [Committee Name]
**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2 roles; TYPE from closed set)
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination present in org diagram; no TBD]
```

**Step 3.2 -- Pair-Count Verification**

- Governance rows in ORT: [N]
- Charters produced: [N]
- Must match. If mismatch: identify gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER**

```
ORG-ELEMENT REGISTER
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [committee or cadence name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role name from ORT]
```

All four categories populated before Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

>= 2 rows, distinct trigger categories. Row 1 MUST be headcount threshold.
Row 2 from a different category (workload signal, structural symptom, milestone).

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [structural change] | headcount-threshold |
| [different trigger] | [structural change] | [distinct type] |

**Step 3.5 -- Anti-Pattern Watch**

>= 2 rows. Each entry opens with:
`[element name] (cat-N) -- [one sentence]`
Element names copied exactly from ORG-ELEMENT REGISTER. No cat-N code outside schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter. Each check is per-charter; failure halts the loop:

```
Charter: [Committee Name]
[ ] Quorum: value is in form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority
    of members", "quorum required"), bare number without "member roles" suffix, absent
[ ] Membership: each role carries exactly one `(TYPE)` annotation from
    {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: no annotation; out-of-set value ("OWNER","LEAD","APPROVER"); multiple types
[ ] Role continuity: each Membership role name present in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] not in GATE 0 typed list -- HALT loop at this charter;
    add [X] to GATE 0 ROLES-LOADED; re-emit GATE 0 STATUS;
    restart CHARTER-FORMAT-AUDIT from Charter 1 before continuing
```

On any REJECT at any charter: STOP. Correct. Re-run full audit loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count produced
- [ ] Each charter: 5 fields (Name/header, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT loop complete: all charters passed Quorum form, Membership TYPE,
  and per-charter role-continuity check against GATE 0 typed list
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership role names present in GATE 0;
  absent name fails CHECKPOINT-3; remediation: add to GATE 0, re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 all populated
- [ ] Roadmap >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 rows, typed element citations from register
- [ ] GATE 3 prohibited-content contract satisfied (C-30)

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-02 -- Output Format: C-40 Preamble-Position Declaration Only

**Axis:** output format -- adds explicit forward-declaring contract framing to the
GATE CHAIN ARTIFACT-HANDOFF INVENTORY: the block is labeled as a pre-GATE 0 preamble,
the prompt states that a model reading this prompt encounters all four gate transitions
before any gate executes, and the prohibited form (post-GATE 3 retrospective record) is
named. No C-39 changes: STRUCTURING-COST FRAME position constraint unchanged from V-01
baseline.
**Hypothesis:** C-40 requires the prompt to explicitly declare the pre-GATE 0 preamble
role and name the prohibited form. V-02 adds these declarations. C-40 PASS predicted
(+5 pts). C-39 absent: no DO NOT guard for pre-mechanism-table position, no causal
explanation for that constraint. C-38 satisfied (block exists); C-37 satisfied (frame
present). Composite: 245/250.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN PREAMBLE (pre-GATE 0) -- READ BEFORE EXECUTING ANY GATE

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS.

POSITION CONTRACT: This block appears as a preamble before GATE 0 so that a model
reading this prompt encounters the full artifact dependency graph before any gate
executes. It is a forward-declaring contract. A model operating under this prompt
reads all four gate transitions before GATE 0 begins. The prohibited form is placing
this inventory after GATE 3, where it becomes a retrospective record consulted after
the gates it is meant to govern -- a model processing the prompt gate-by-gate under
the post-GATE 3 form never consults the artifact inventory before the gate that
requires it.

ARTIFACT-HANDOFF INVENTORY:
  GATE 0 -> GATE 1: typed role list
    Produced by: Step 0.2 ROLE-TYPE-CLASSIFICATION
    Required by: GATE 1 (role names used in mechanism table and inertia reasoning)
  GATE 1 -> GATE 2: inertia verdict + FLAT-CASE-PRESSURE rating
    Produced by: Step 1.4 anchor steps 1 and 3 (FLAT-CASE-PRESSURE + VERDICT)
    Required by: GATE 2 (structural sections only begin if VERDICT = STRUCTURE-WARRANTED)
  GATE 2 -> GATE 3: org diagram with typed nodes
    Produced by: Step 2.1 ASCII Org Diagram + Step 2.2 Headcount by Area
    Required by: GATE 3 Step 3.1 (committee nodes must match diagram; all Escalates
    destinations must name nodes present in the diagram)
  GATE 3 -> STATUS: complete charter set
    Produced by: Step 3.1 interleaved rhythm/charter pairs + CHARTER-FORMAT-AUDIT loop
    Required by: final STATUS (emits only after GATE 3 STATUS PASS; charter set is the
    terminal artifact)

This ARTIFACT-HANDOFF INVENTORY is the authoritative cross-gate traceability reference.
Each gate section also carries a local "Named artifact handoff" line consistent with this
inventory. If any local declaration conflicts with this inventory, this inventory governs.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list (see ARTIFACT-HANDOFF INVENTORY: GATE 0 -> GATE 1)

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block; no structural content between steps. Every role
typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced:
DECISION first, EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed until every role from Step 0.1 is typed.

**CHECKPOINT-0** -- ROLES-LOADED/NOTE present; all roles typed; containment satisfied;
no structural content between 0.1 and 0.2.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 0 -> GATE 1).
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating (see ARTIFACT-HANDOFF INVENTORY: GATE 1 -> GATE 2)

GATE 1 DO/DO NOT:
- DO: Emit STRUCTURING-COST FRAME block before Step 1.0.
- DO: Write default-position statement (Step 1.0) before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Use numbered anchor sequence in Step 1.4 (not a narrative paragraph).
- DO NOT: Write diagram, headcount, rhythm, or charter content before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII diagram nodes, headcount area rows, rhythm cadence rows,
charter fields (Mission, Membership, Quorum, Escalates).

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT** [Zone: before Step 1.0]

Before any flat-case argument, enumerate the overhead imposed by formal structure.
This frame establishes the cost denominator: structure must produce net savings
greater than this overhead to be warranted. VERDICT anchor step 3 must cite the
dominant cost category named here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter authoring, role assignment, initial standing-meeting design -- eng-weeks for
     first governance cycle; include time spent by all named roles in setup, not just PM]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries; handoff
     latency introduced for work previously handled informally -- eng-weeks/qtr]
  Governance cadence tax:
    [steady-state recurring meeting load across all governance committees -- eng-hours/qtr
     converted to eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews,
     charter revision, quorum coordination, decision logging]
```

VERDICT (anchor step 3) must declare whether flat coordination cost exceeds or falls
below this governance overhead, naming the dominant cost category.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step. MUST precede the mechanism table. Not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
Two-step separator:
- Count rows. If < 2, produce missing rows first.
- When count >= 2, emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

GUARD: DO NOT emit separator before count >= 2. DO NOT begin Step 1.2 before separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list Step 1.1 mechanism rows.

**Step 1.3 -- Rebuttal**

Name the ONE failure mode flat coordination cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude).

```
UNCOVERED: [decision class or function with no current owner under flat structure]
```

**Step 1.4 -- VERDICT: SUB-SECTION-4-ANCHOR-SEQUENCE**

Complete the following numbered anchor sequence in order. Each step is a labeled output
item. DO NOT collapse into a narrative paragraph. The sequence IS the sub-section.

```
1. FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]
   Evidence: [N] mechanisms at [cost anchor from FLAT-CASE-CLOSED]; dominant flat
   coordination mode: [mechanism type from Step 1.1]

2. NET-COST-COMPARISON:
   | Cost Category                         | Flat Coordination      | Formal Structure        |
   |---------------------------------------|------------------------|-------------------------|
   | Inertia mechanisms (from FLAT-CASE)   | [X eng-weeks/qtr]      | [X eng-weeks/qtr]       |
   | Committee formation + maintenance     | --                     | [Y eng-weeks/qtr]       |
   | Governance cadence tax (from FRAME)   | --                     | [Y eng-weeks/qtr]       |
   | UNCOVERED failure-mode cost           | [Z eng-weeks/qtr]      | [reduced Z eng-weeks]   |
   | Net total                             | [T_flat eng-weeks/qtr] | [T_struct eng-weeks/qtr]|
   Net delta: T_struct - T_flat = [signed value]
   Interpretation: positive = structure costs more; negative = structure produces net savings.

3. VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
   Basis: net delta is [positive/negative]; dominant cost from STRUCTURING-COST FRAME
   is [category]; this [exceeds / is exceeded by] the UNCOVERED failure-mode cost.

4. RE-ASSESSMENT TRIGGER: [concrete measurable threshold; not "revisit as the team grows";
   must be independently verifiable; e.g., "when UNCOVERED failure-mode cost exceeds [N]
   eng-weeks/qtr for two consecutive quarters" or "when headcount in [area] crosses [N]"]
```

Flat-verdict branch -- if VERDICT = CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] STRUCTURING-COST FRAME present before Step 1.0; all three cost categories populated
  (committee formation, role specialization overhead, governance cadence tax)
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set; FLAT-CASE-CLOSED separator emitted
- [ ] Step 1.4 uses numbered anchor sequence 1-4 (not a narrative paragraph)
- [ ] NET-COST-COMPARISON table present at anchor step 2 with signed net delta declared
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED}; cites dominant FRAME cost
- [ ] RE-ASSESSMENT TRIGGER concrete; not growth-narrative
- [ ] No GATE 1 prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 1 -> GATE 2).
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** org diagram with typed nodes (see ARTIFACT-HANDOFF INVENTORY: GATE 2 -> GATE 3)

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row. All Escalates destinations name specific diagram nodes.

**CHECKPOINT DIAGRAM-CHECK** -- diagram levels, role sourcing, committees distinct,
5-column headcount, Decides/Escalates split, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 2 -> GATE 3).
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
  (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** complete charter set (see ARTIFACT-HANDOFF INVENTORY: GATE 3 -> STATUS)

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm rows first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in any charter Membership.
- DO NOT: Write Quorum without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract):
- Appendices of any kind
- Supplementary sections (tables, notes, annexes)
- Editorial commentary after Anti-Pattern Watch table
- Charters not paired with an operating rhythm row
- Any content outside Steps 3.1 through 3.5

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.
For each governance row, immediately produce its charter before the next ORT row.

Charter template:
```
### [Committee Name]
**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2 roles; TYPE from closed set)
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination present in org diagram; no TBD]
```

**Step 3.2 -- Pair-Count Verification**

- Governance rows in ORT: [N]
- Charters produced: [N]
- Must match. If mismatch: identify gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER**

```
ORG-ELEMENT REGISTER
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [committee or cadence name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role name from ORT]
```

All four categories populated before Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

>= 2 rows, distinct trigger categories. Row 1 MUST be headcount threshold.
Row 2 from a different category (workload signal, structural symptom, milestone).

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [structural change] | headcount-threshold |
| [different trigger] | [structural change] | [distinct type] |

**Step 3.5 -- Anti-Pattern Watch**

>= 2 rows. Each entry opens with:
`[element name] (cat-N) -- [one sentence]`
Element names copied exactly from ORG-ELEMENT REGISTER. No cat-N code outside schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter. Each check is per-charter; failure halts the loop:

```
Charter: [Committee Name]
[ ] Quorum: value is in form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority
    of members", "quorum required"), bare number without "member roles" suffix, absent
[ ] Membership: each role carries exactly one `(TYPE)` annotation from
    {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: no annotation; out-of-set value ("OWNER","LEAD","APPROVER"); multiple types
[ ] Role continuity: each Membership role name present in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] not in GATE 0 typed list -- HALT loop at this charter;
    add [X] to GATE 0 ROLES-LOADED; re-emit GATE 0 STATUS;
    restart CHARTER-FORMAT-AUDIT from Charter 1 before continuing
```

On any REJECT at any charter: STOP. Correct. Re-run full audit loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count produced
- [ ] Each charter: 5 fields (Name/header, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT loop complete: all charters passed Quorum form, Membership TYPE,
  and per-charter role-continuity check against GATE 0 typed list
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership role names present in GATE 0;
  absent name fails CHECKPOINT-3; remediation: add to GATE 0, re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 all populated
- [ ] Roadmap >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 rows, typed element citations from register
- [ ] GATE 3 prohibited-content contract satisfied (C-30)

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-03 -- Inertia Framing: C-39 Pre-Mechanism-Table Position Constraint Only

**Axis:** inertia framing -- adds explicit pre-mechanism-table position constraint
to STRUCTURING-COST FRAME: a POSITION CONTRACT label names the mechanism table (Step 1.1)
as the positional boundary, explains the causal logic (interpretive premise vs. derived
conclusion), names the prohibited form (post-mechanism placement as cost-summary), and
adds a DO NOT guard in GATE 1. GATE CHAIN CONTRACT section unchanged from V-01: no
preamble declaration, no forward-declaring contract language, no prohibited-form naming
for the inventory block.
**Hypothesis:** C-39 requires an explicit positional constraint instruction that names
the mechanism table as the boundary, explains why pre-table position is required, and
names the prohibited form. V-03 adds all three. C-39 PASS predicted (+5 pts). C-40
absent: ARTIFACT-HANDOFF INVENTORY physically precedes GATE 0 but has no preamble
declaration or forward-declaring contract framing. Composite: 245/250.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Sequence provable from
gate labels. Every gate carries a dedicated verification checkpoint before STATUS.

ARTIFACT-HANDOFF INVENTORY:
  GATE 0 -> GATE 1: typed role list
    Produced by: Step 0.2 ROLE-TYPE-CLASSIFICATION
    Required by: GATE 1 (role names used in mechanism table and inertia reasoning)
  GATE 1 -> GATE 2: inertia verdict + FLAT-CASE-PRESSURE rating
    Produced by: Step 1.4 anchor steps 1 and 3 (FLAT-CASE-PRESSURE + VERDICT)
    Required by: GATE 2 (structural sections only begin if VERDICT = STRUCTURE-WARRANTED)
  GATE 2 -> GATE 3: org diagram with typed nodes
    Produced by: Step 2.1 ASCII Org Diagram + Step 2.2 Headcount by Area
    Required by: GATE 3 Step 3.1 (committee nodes must match diagram; all Escalates
    destinations must name nodes present in the diagram)
  GATE 3 -> STATUS: complete charter set
    Produced by: Step 3.1 interleaved rhythm/charter pairs + CHARTER-FORMAT-AUDIT loop
    Required by: final STATUS (emits only after GATE 3 STATUS PASS; charter set is the
    terminal artifact)

This ARTIFACT-HANDOFF INVENTORY is the authoritative cross-gate traceability reference.
Each gate section also carries a local "Named artifact handoff" line consistent with this
inventory. If any local declaration conflicts with this inventory, this inventory governs.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list (see ARTIFACT-HANDOFF INVENTORY: GATE 0 -> GATE 1)

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block; no structural content between steps. Every role
typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced:
DECISION first, EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed until every role from Step 0.1 is typed.

**CHECKPOINT-0** -- ROLES-LOADED/NOTE present; all roles typed; containment satisfied;
no structural content between 0.1 and 0.2.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 0 -> GATE 1).
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating (see ARTIFACT-HANDOFF INVENTORY: GATE 1 -> GATE 2)

GATE 1 DO/DO NOT:
- DO: Emit STRUCTURING-COST FRAME before the mechanism table (Step 1.1). The frame is
  the first element of GATE 1 content; it establishes overhead categories as the
  interpretive lens through which each mechanism row is read.
- DO: Write default-position statement (Step 1.0) before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Use numbered anchor sequence in Step 1.4 (not a narrative paragraph).
- DO NOT: Write any mechanism table row before STRUCTURING-COST FRAME is complete.
  Emitting the frame after the mechanism table produces overhead as a conclusion derived
  from rows already written -- this reverses the causal structure and is the prohibited form.
- DO NOT: Write diagram, headcount, rhythm, or charter content before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII diagram nodes, headcount area rows, rhythm cadence rows,
charter fields (Mission, Membership, Quorum, Escalates).

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT**
[POSITION CONTRACT: before mechanism table (Step 1.1) -- this block is the interpretive
premise through which each mechanism row is read; it MUST appear before the first row of
the Step 1.1 table; the prohibited form is STRUCTURING-COST FRAME positioned after
Step 1.1, where it functions as a cost-summary derived from rows already written rather
than as the evaluative lens applied to each row as it is produced]

Before any flat-case argument, enumerate the overhead imposed by formal structure.
This frame establishes the cost denominator: structure must produce net savings
greater than this overhead to be warranted. VERDICT anchor step 3 must cite the
dominant cost category named here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter authoring, role assignment, initial standing-meeting design -- eng-weeks for
     first governance cycle; include time spent by all named roles in setup, not just PM]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries; handoff
     latency introduced for work previously handled informally -- eng-weeks/qtr]
  Governance cadence tax:
    [steady-state recurring meeting load across all governance committees -- eng-hours/qtr
     converted to eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews,
     charter revision, quorum coordination, decision logging]
```

VERDICT (anchor step 3) must declare whether flat coordination cost exceeds or falls
below this governance overhead, naming the dominant cost category.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step. MUST precede the mechanism table. Not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
Two-step separator:
- Count rows. If < 2, produce missing rows first.
- When count >= 2, emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

GUARD: DO NOT emit separator before count >= 2. DO NOT begin Step 1.2 before separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list Step 1.1 mechanism rows.

**Step 1.3 -- Rebuttal**

Name the ONE failure mode flat coordination cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude).

```
UNCOVERED: [decision class or function with no current owner under flat structure]
```

**Step 1.4 -- VERDICT: SUB-SECTION-4-ANCHOR-SEQUENCE**

Complete the following numbered anchor sequence in order. Each step is a labeled output
item. DO NOT collapse into a narrative paragraph. The sequence IS the sub-section.

```
1. FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]
   Evidence: [N] mechanisms at [cost anchor from FLAT-CASE-CLOSED]; dominant flat
   coordination mode: [mechanism type from Step 1.1]

2. NET-COST-COMPARISON:
   | Cost Category                         | Flat Coordination      | Formal Structure        |
   |---------------------------------------|------------------------|-------------------------|
   | Inertia mechanisms (from FLAT-CASE)   | [X eng-weeks/qtr]      | [X eng-weeks/qtr]       |
   | Committee formation + maintenance     | --                     | [Y eng-weeks/qtr]       |
   | Governance cadence tax (from FRAME)   | --                     | [Y eng-weeks/qtr]       |
   | UNCOVERED failure-mode cost           | [Z eng-weeks/qtr]      | [reduced Z eng-weeks]   |
   | Net total                             | [T_flat eng-weeks/qtr] | [T_struct eng-weeks/qtr]|
   Net delta: T_struct - T_flat = [signed value]
   Interpretation: positive = structure costs more; negative = structure produces net savings.

3. VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
   Basis: net delta is [positive/negative]; dominant cost from STRUCTURING-COST FRAME
   is [category]; this [exceeds / is exceeded by] the UNCOVERED failure-mode cost.

4. RE-ASSESSMENT TRIGGER: [concrete measurable threshold; not "revisit as the team grows";
   must be independently verifiable; e.g., "when UNCOVERED failure-mode cost exceeds [N]
   eng-weeks/qtr for two consecutive quarters" or "when headcount in [area] crosses [N]"]
```

Flat-verdict branch -- if VERDICT = CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] STRUCTURING-COST FRAME appears before Step 1.1 mechanism table (not after, not as
  cost-summary appendix to sub-section 4)
- [ ] STRUCTURING-COST FRAME: all three cost categories populated
  (committee formation, role specialization overhead, governance cadence tax)
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set; FLAT-CASE-CLOSED separator emitted
- [ ] Step 1.4 uses numbered anchor sequence 1-4 (not a narrative paragraph)
- [ ] NET-COST-COMPARISON table present at anchor step 2 with signed net delta declared
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED}; cites dominant FRAME cost
- [ ] RE-ASSESSMENT TRIGGER concrete; not growth-narrative
- [ ] No GATE 1 prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 1 -> GATE 2).
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** org diagram with typed nodes (see ARTIFACT-HANDOFF INVENTORY: GATE 2 -> GATE 3)

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row. All Escalates destinations name specific diagram nodes.

**CHECKPOINT DIAGRAM-CHECK** -- diagram levels, role sourcing, committees distinct,
5-column headcount, Decides/Escalates split, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 2 -> GATE 3).
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
  (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** complete charter set (see ARTIFACT-HANDOFF INVENTORY: GATE 3 -> STATUS)

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm rows first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in any charter Membership.
- DO NOT: Write Quorum without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract):
- Appendices of any kind
- Supplementary sections (tables, notes, annexes)
- Editorial commentary after Anti-Pattern Watch table
- Charters not paired with an operating rhythm row
- Any content outside Steps 3.1 through 3.5

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.
For each governance row, immediately produce its charter before the next ORT row.

Charter template:
```
### [Committee Name]
**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2 roles; TYPE from closed set)
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination present in org diagram; no TBD]
```

**Step 3.2 -- Pair-Count Verification**

- Governance rows in ORT: [N]
- Charters produced: [N]
- Must match. If mismatch: identify gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER**

```
ORG-ELEMENT REGISTER
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [committee or cadence name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role name from ORT]
```

All four categories populated before Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

>= 2 rows, distinct trigger categories. Row 1 MUST be headcount threshold.
Row 2 from a different category (workload signal, structural symptom, milestone).

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [structural change] | headcount-threshold |
| [different trigger] | [structural change] | [distinct type] |

**Step 3.5 -- Anti-Pattern Watch**

>= 2 rows. Each entry opens with:
`[element name] (cat-N) -- [one sentence]`
Element names copied exactly from ORG-ELEMENT REGISTER. No cat-N code outside schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter. Each check is per-charter; failure halts the loop:

```
Charter: [Committee Name]
[ ] Quorum: value is in form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority
    of members", "quorum required"), bare number without "member roles" suffix, absent
[ ] Membership: each role carries exactly one `(TYPE)` annotation from
    {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: no annotation; out-of-set value ("OWNER","LEAD","APPROVER"); multiple types
[ ] Role continuity: each Membership role name present in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] not in GATE 0 typed list -- HALT loop at this charter;
    add [X] to GATE 0 ROLES-LOADED; re-emit GATE 0 STATUS;
    restart CHARTER-FORMAT-AUDIT from Charter 1 before continuing
```

On any REJECT at any charter: STOP. Correct. Re-run full audit loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count produced
- [ ] Each charter: 5 fields (Name/header, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT loop complete: all charters passed Quorum form, Membership TYPE,
  and per-charter role-continuity check against GATE 0 typed list
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership role names present in GATE 0;
  absent name fails CHECKPOINT-3; remediation: add to GATE 0, re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 all populated
- [ ] Roadmap >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 rows, typed element citations from register
- [ ] GATE 3 prohibited-content contract satisfied (C-30)

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-04 -- Combined: C-39 + C-40 Both Explicit Positional Constraints

**Axis:** combined -- integrates both the C-40 preamble-position declaration (from V-02)
and the C-39 pre-mechanism-table position constraint (from V-03) into a single variation.
V-02 and V-03 are independent additions; neither constrains the other; the combination
is additive without structural conflict.
**Hypothesis:** C-39 PASS (STRUCTURING-COST FRAME POSITION CONTRACT with causal
explanation and prohibited form) + C-40 PASS (GATE CHAIN PREAMBLE forward-declaring
contract with retrospective-record prohibition). First R13 variation predicted to achieve
full coverage of all 40 v13 criteria. Composite: 250/250 (100%).

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN PREAMBLE (pre-GATE 0) -- READ BEFORE EXECUTING ANY GATE

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS.

POSITION CONTRACT: This block appears as a preamble before GATE 0 so that a model
reading this prompt encounters the full artifact dependency graph before any gate
executes. It is a forward-declaring contract. A model operating under this prompt
reads all four gate transitions before GATE 0 begins. The prohibited form is placing
this inventory after GATE 3, where it becomes a retrospective record consulted after
the gates it is meant to govern -- a model processing the prompt gate-by-gate under
the post-GATE 3 form never consults the artifact inventory before the gate that
requires it.

ARTIFACT-HANDOFF INVENTORY:
  GATE 0 -> GATE 1: typed role list
    Produced by: Step 0.2 ROLE-TYPE-CLASSIFICATION
    Required by: GATE 1 (role names used in mechanism table and inertia reasoning)
  GATE 1 -> GATE 2: inertia verdict + FLAT-CASE-PRESSURE rating
    Produced by: Step 1.4 anchor steps 1 and 3 (FLAT-CASE-PRESSURE + VERDICT)
    Required by: GATE 2 (structural sections only begin if VERDICT = STRUCTURE-WARRANTED)
  GATE 2 -> GATE 3: org diagram with typed nodes
    Produced by: Step 2.1 ASCII Org Diagram + Step 2.2 Headcount by Area
    Required by: GATE 3 Step 3.1 (committee nodes must match diagram; all Escalates
    destinations must name nodes present in the diagram)
  GATE 3 -> STATUS: complete charter set
    Produced by: Step 3.1 interleaved rhythm/charter pairs + CHARTER-FORMAT-AUDIT loop
    Required by: final STATUS (emits only after GATE 3 STATUS PASS; charter set is the
    terminal artifact)

This ARTIFACT-HANDOFF INVENTORY is the authoritative cross-gate traceability reference.
Each gate section also carries a local "Named artifact handoff" line consistent with this
inventory. If any local declaration conflicts with this inventory, this inventory governs.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list (see ARTIFACT-HANDOFF INVENTORY: GATE 0 -> GATE 1)

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block; no structural content between steps. Every role
typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced:
DECISION first, EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed until every role from Step 0.1 is typed.

**CHECKPOINT-0** -- ROLES-LOADED/NOTE present; all roles typed; containment satisfied;
no structural content between 0.1 and 0.2.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 0 -> GATE 1).
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating (see ARTIFACT-HANDOFF INVENTORY: GATE 1 -> GATE 2)

GATE 1 DO/DO NOT:
- DO: Emit STRUCTURING-COST FRAME before the mechanism table (Step 1.1). The frame is
  the first element of GATE 1 content; it establishes overhead categories as the
  interpretive lens through which each mechanism row is read.
- DO: Write default-position statement (Step 1.0) before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Use numbered anchor sequence in Step 1.4 (not a narrative paragraph).
- DO NOT: Write any mechanism table row before STRUCTURING-COST FRAME is complete.
  Emitting the frame after the mechanism table produces overhead as a conclusion derived
  from rows already written -- this reverses the causal structure and is the prohibited form.
- DO NOT: Write diagram, headcount, rhythm, or charter content before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII diagram nodes, headcount area rows, rhythm cadence rows,
charter fields (Mission, Membership, Quorum, Escalates).

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT**
[POSITION CONTRACT: before mechanism table (Step 1.1) -- this block is the interpretive
premise through which each mechanism row is read; it MUST appear before the first row of
the Step 1.1 table; the prohibited form is STRUCTURING-COST FRAME positioned after
Step 1.1, where it functions as a cost-summary derived from rows already written rather
than as the evaluative lens applied to each row as it is produced]

Before any flat-case argument, enumerate the overhead imposed by formal structure.
This frame establishes the cost denominator: structure must produce net savings
greater than this overhead to be warranted. VERDICT anchor step 3 must cite the
dominant cost category named here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter authoring, role assignment, initial standing-meeting design -- eng-weeks for
     first governance cycle; include time spent by all named roles in setup, not just PM]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries; handoff
     latency introduced for work previously handled informally -- eng-weeks/qtr]
  Governance cadence tax:
    [steady-state recurring meeting load across all governance committees -- eng-hours/qtr
     converted to eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews,
     charter revision, quorum coordination, decision logging]
```

VERDICT (anchor step 3) must declare whether flat coordination cost exceeds or falls
below this governance overhead, naming the dominant cost category.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step. MUST precede the mechanism table. Not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
Two-step separator:
- Count rows. If < 2, produce missing rows first.
- When count >= 2, emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

GUARD: DO NOT emit separator before count >= 2. DO NOT begin Step 1.2 before separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list Step 1.1 mechanism rows.

**Step 1.3 -- Rebuttal**

Name the ONE failure mode flat coordination cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude).

```
UNCOVERED: [decision class or function with no current owner under flat structure]
```

**Step 1.4 -- VERDICT: SUB-SECTION-4-ANCHOR-SEQUENCE**

Complete the following numbered anchor sequence in order. Each step is a labeled output
item. DO NOT collapse into a narrative paragraph. The sequence IS the sub-section.

```
1. FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]
   Evidence: [N] mechanisms at [cost anchor from FLAT-CASE-CLOSED]; dominant flat
   coordination mode: [mechanism type from Step 1.1]

2. NET-COST-COMPARISON:
   | Cost Category                         | Flat Coordination      | Formal Structure        |
   |---------------------------------------|------------------------|-------------------------|
   | Inertia mechanisms (from FLAT-CASE)   | [X eng-weeks/qtr]      | [X eng-weeks/qtr]       |
   | Committee formation + maintenance     | --                     | [Y eng-weeks/qtr]       |
   | Governance cadence tax (from FRAME)   | --                     | [Y eng-weeks/qtr]       |
   | UNCOVERED failure-mode cost           | [Z eng-weeks/qtr]      | [reduced Z eng-weeks]   |
   | Net total                             | [T_flat eng-weeks/qtr] | [T_struct eng-weeks/qtr]|
   Net delta: T_struct - T_flat = [signed value]
   Interpretation: positive = structure costs more; negative = structure produces net savings.

3. VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
   Basis: net delta is [positive/negative]; dominant cost from STRUCTURING-COST FRAME
   is [category]; this [exceeds / is exceeded by] the UNCOVERED failure-mode cost.

4. RE-ASSESSMENT TRIGGER: [concrete measurable threshold; not "revisit as the team grows";
   must be independently verifiable; e.g., "when UNCOVERED failure-mode cost exceeds [N]
   eng-weeks/qtr for two consecutive quarters" or "when headcount in [area] crosses [N]"]
```

Flat-verdict branch -- if VERDICT = CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] STRUCTURING-COST FRAME appears before Step 1.1 mechanism table (not after, not as
  cost-summary appendix to sub-section 4)
- [ ] STRUCTURING-COST FRAME: all three cost categories populated
  (committee formation, role specialization overhead, governance cadence tax)
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set; FLAT-CASE-CLOSED separator emitted
- [ ] Step 1.4 uses numbered anchor sequence 1-4 (not a narrative paragraph)
- [ ] NET-COST-COMPARISON table present at anchor step 2 with signed net delta declared
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED}; cites dominant FRAME cost
- [ ] RE-ASSESSMENT TRIGGER concrete; not growth-narrative
- [ ] No GATE 1 prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 1 -> GATE 2).
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** org diagram with typed nodes (see ARTIFACT-HANDOFF INVENTORY: GATE 2 -> GATE 3)

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row. All Escalates destinations name specific diagram nodes.

**CHECKPOINT DIAGRAM-CHECK** -- diagram levels, role sourcing, committees distinct,
5-column headcount, Decides/Escalates split, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 2 -> GATE 3).
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
  (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** complete charter set (see ARTIFACT-HANDOFF INVENTORY: GATE 3 -> STATUS)

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm rows first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in any charter Membership.
- DO NOT: Write Quorum without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract):
- Appendices of any kind
- Supplementary sections (tables, notes, annexes)
- Editorial commentary after Anti-Pattern Watch table
- Charters not paired with an operating rhythm row
- Any content outside Steps 3.1 through 3.5

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.
For each governance row, immediately produce its charter before the next ORT row.

Charter template:
```
### [Committee Name]
**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2 roles; TYPE from closed set)
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination present in org diagram; no TBD]
```

**Step 3.2 -- Pair-Count Verification**

- Governance rows in ORT: [N]
- Charters produced: [N]
- Must match. If mismatch: identify gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER**

```
ORG-ELEMENT REGISTER
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [committee or cadence name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role name from ORT]
```

All four categories populated before Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

>= 2 rows, distinct trigger categories. Row 1 MUST be headcount threshold.
Row 2 from a different category (workload signal, structural symptom, milestone).

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [structural change] | headcount-threshold |
| [different trigger] | [structural change] | [distinct type] |

**Step 3.5 -- Anti-Pattern Watch**

>= 2 rows. Each entry opens with:
`[element name] (cat-N) -- [one sentence]`
Element names copied exactly from ORG-ELEMENT REGISTER. No cat-N code outside schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter. Each check is per-charter; failure halts the loop:

```
Charter: [Committee Name]
[ ] Quorum: value is in form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority
    of members", "quorum required"), bare number without "member roles" suffix, absent
[ ] Membership: each role carries exactly one `(TYPE)` annotation from
    {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: no annotation; out-of-set value ("OWNER","LEAD","APPROVER"); multiple types
[ ] Role continuity: each Membership role name present in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] not in GATE 0 typed list -- HALT loop at this charter;
    add [X] to GATE 0 ROLES-LOADED; re-emit GATE 0 STATUS;
    restart CHARTER-FORMAT-AUDIT from Charter 1 before continuing
```

On any REJECT at any charter: STOP. Correct. Re-run full audit loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count produced
- [ ] Each charter: 5 fields (Name/header, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT loop complete: all charters passed Quorum form, Membership TYPE,
  and per-charter role-continuity check against GATE 0 typed list
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership role names present in GATE 0;
  absent name fails CHECKPOINT-3; remediation: add to GATE 0, re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 all populated
- [ ] Roadmap >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 rows, typed element citations from register
- [ ] GATE 3 prohibited-content contract satisfied (C-30)

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-05 -- Maximum Integration: V-04 + Checkpoint Position Guards

**Axis:** maximum integration -- V-04 baseline (both C-39 and C-40 positional constraints)
plus explicit checkpoint verification of both positional properties at execution time:
CHECKPOINT-0 gains a step verifying the GATE CHAIN PREAMBLE was encountered as a
pre-GATE 0 block (not a post-GATE 3 appendix); CHECKPOINT-INERTIA-CHECK gains a step
verifying the STRUCTURING-COST FRAME position relative to the mechanism table (not just
presence). The hypothesis is that co-locating the positional constraint verification
with the checkpoint that enforces gate completion makes the constraint non-bypassable:
a model that correctly emits GATE 0 STATUS PASS must have verified the preamble position,
and a model that correctly emits GATE 1 STATUS PASS must have verified the frame position.
**Hypothesis:** C-39 and C-40 both PASS from V-04 constructs. Checkpoint enforcement
adds execution-time verification of positional rules at the site where gate authorization
is issued, consistent with the C-29 all-gate-blocking pattern applied to positional
constraints. 250/250 predicted. Eliminates the bypass where a model inherits the correct
structure from training prior but does not explicitly reason about the position at gate
verification time.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN PREAMBLE (pre-GATE 0) -- READ BEFORE EXECUTING ANY GATE

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS.

POSITION CONTRACT: This block appears as a preamble before GATE 0 so that a model
reading this prompt encounters the full artifact dependency graph before any gate
executes. It is a forward-declaring contract. A model operating under this prompt
reads all four gate transitions before GATE 0 begins. The prohibited form is placing
this inventory after GATE 3, where it becomes a retrospective record consulted after
the gates it is meant to govern -- a model processing the prompt gate-by-gate under
the post-GATE 3 form never consults the artifact inventory before the gate that
requires it. CHECKPOINT-0 verifies this block was encountered as a preamble before
GATE 0 execution.

ARTIFACT-HANDOFF INVENTORY:
  GATE 0 -> GATE 1: typed role list
    Produced by: Step 0.2 ROLE-TYPE-CLASSIFICATION
    Required by: GATE 1 (role names used in mechanism table and inertia reasoning)
  GATE 1 -> GATE 2: inertia verdict + FLAT-CASE-PRESSURE rating
    Produced by: Step 1.4 anchor steps 1 and 3 (FLAT-CASE-PRESSURE + VERDICT)
    Required by: GATE 2 (structural sections only begin if VERDICT = STRUCTURE-WARRANTED)
  GATE 2 -> GATE 3: org diagram with typed nodes
    Produced by: Step 2.1 ASCII Org Diagram + Step 2.2 Headcount by Area
    Required by: GATE 3 Step 3.1 (committee nodes must match diagram; all Escalates
    destinations must name nodes present in the diagram)
  GATE 3 -> STATUS: complete charter set
    Produced by: Step 3.1 interleaved rhythm/charter pairs + CHARTER-FORMAT-AUDIT loop
    Required by: final STATUS (emits only after GATE 3 STATUS PASS; charter set is the
    terminal artifact)

This ARTIFACT-HANDOFF INVENTORY is the authoritative cross-gate traceability reference.
Each gate section also carries a local "Named artifact handoff" line consistent with this
inventory. If any local declaration conflicts with this inventory, this inventory governs.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list (see ARTIFACT-HANDOFF INVENTORY: GATE 0 -> GATE 1)

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block; no structural content between steps. Every role
typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced:
DECISION first, EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed until every role from Step 0.1 is typed.

**CHECKPOINT-0** -- Before emitting GATE 0 STATUS, verify all items:
- [ ] GATE CHAIN PREAMBLE (pre-GATE 0) was the first structural block read before this
  gate; it was not deferred to a post-GATE 3 appendix position (verify: the preamble
  text and ARTIFACT-HANDOFF INVENTORY appear above GATE 0 in document order)
- [ ] ROLES-LOADED/NOTE present; all roles typed; three-tier order respected
- [ ] ROLE-TYPE-CLASSIFICATION containment satisfied; no structural content between
  Step 0.1 and Step 0.2
- [ ] No containment-contract violations above this line

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 0 -> GATE 1).
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating (see ARTIFACT-HANDOFF INVENTORY: GATE 1 -> GATE 2)

GATE 1 DO/DO NOT:
- DO: Emit STRUCTURING-COST FRAME before the mechanism table (Step 1.1). The frame is
  the first element of GATE 1 content; it establishes overhead categories as the
  interpretive lens through which each mechanism row is read.
- DO: Write default-position statement (Step 1.0) before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Use numbered anchor sequence in Step 1.4 (not a narrative paragraph).
- DO NOT: Write any mechanism table row before STRUCTURING-COST FRAME is complete.
  Emitting the frame after the mechanism table produces overhead as a conclusion derived
  from rows already written -- this reverses the causal structure and is the prohibited form.
- DO NOT: Write diagram, headcount, rhythm, or charter content before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII diagram nodes, headcount area rows, rhythm cadence rows,
charter fields (Mission, Membership, Quorum, Escalates).

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT**
[POSITION CONTRACT: before mechanism table (Step 1.1) -- this block is the interpretive
premise through which each mechanism row is read; it MUST appear before the first row of
the Step 1.1 table; the prohibited form is STRUCTURING-COST FRAME positioned after
Step 1.1, where it functions as a cost-summary derived from rows already written rather
than as the evaluative lens applied to each row as it is produced; CHECKPOINT-INERTIA
verifies this position before GATE 1 STATUS can PASS]

Before any flat-case argument, enumerate the overhead imposed by formal structure.
This frame establishes the cost denominator: structure must produce net savings
greater than this overhead to be warranted. VERDICT anchor step 3 must cite the
dominant cost category named here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter authoring, role assignment, initial standing-meeting design -- eng-weeks for
     first governance cycle; include time spent by all named roles in setup, not just PM]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries; handoff
     latency introduced for work previously handled informally -- eng-weeks/qtr]
  Governance cadence tax:
    [steady-state recurring meeting load across all governance committees -- eng-hours/qtr
     converted to eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews,
     charter revision, quorum coordination, decision logging]
```

VERDICT (anchor step 3) must declare whether flat coordination cost exceeds or falls
below this governance overhead, naming the dominant cost category.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step. MUST precede the mechanism table. Not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE\|CHANNEL\|INFORMAL-LEAD\|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
Two-step separator:
- Count rows. If < 2, produce missing rows first.
- When count >= 2, emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

GUARD: DO NOT emit separator before count >= 2. DO NOT begin Step 1.2 before separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list Step 1.1 mechanism rows.

**Step 1.3 -- Rebuttal**

Name the ONE failure mode flat coordination cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude).

```
UNCOVERED: [decision class or function with no current owner under flat structure]
```

**Step 1.4 -- VERDICT: SUB-SECTION-4-ANCHOR-SEQUENCE**

Complete the following numbered anchor sequence in order. Each step is a labeled output
item. DO NOT collapse into a narrative paragraph. The sequence IS the sub-section.

```
1. FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH]
   Evidence: [N] mechanisms at [cost anchor from FLAT-CASE-CLOSED]; dominant flat
   coordination mode: [mechanism type from Step 1.1]

2. NET-COST-COMPARISON:
   | Cost Category                         | Flat Coordination      | Formal Structure        |
   |---------------------------------------|------------------------|-------------------------|
   | Inertia mechanisms (from FLAT-CASE)   | [X eng-weeks/qtr]      | [X eng-weeks/qtr]       |
   | Committee formation + maintenance     | --                     | [Y eng-weeks/qtr]       |
   | Governance cadence tax (from FRAME)   | --                     | [Y eng-weeks/qtr]       |
   | UNCOVERED failure-mode cost           | [Z eng-weeks/qtr]      | [reduced Z eng-weeks]   |
   | Net total                             | [T_flat eng-weeks/qtr] | [T_struct eng-weeks/qtr]|
   Net delta: T_struct - T_flat = [signed value]
   Interpretation: positive = structure costs more; negative = structure produces net savings.

3. VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
   Basis: net delta is [positive/negative]; dominant cost from STRUCTURING-COST FRAME
   is [category]; this [exceeds / is exceeded by] the UNCOVERED failure-mode cost.

4. RE-ASSESSMENT TRIGGER: [concrete measurable threshold; not "revisit as the team grows";
   must be independently verifiable; e.g., "when UNCOVERED failure-mode cost exceeds [N]
   eng-weeks/qtr for two consecutive quarters" or "when headcount in [area] crosses [N]"]
```

Flat-verdict branch -- if VERDICT = CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] STRUCTURING-COST FRAME position verified: the FRAME block appears before the
  Step 1.1 mechanism table in document order (verify: FRAME text is above the
  first `| Type |` table row; the prohibited form -- FRAME after Step 1.1 -- is absent)
- [ ] STRUCTURING-COST FRAME: all three cost categories populated
  (committee formation, role specialization overhead, governance cadence tax)
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set; FLAT-CASE-CLOSED separator emitted
- [ ] Step 1.4 uses numbered anchor sequence 1-4 (not a narrative paragraph)
- [ ] NET-COST-COMPARISON table present at anchor step 2 with signed net delta declared
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED}; cites dominant FRAME cost
- [ ] RE-ASSESSMENT TRIGGER concrete; not growth-narrative
- [ ] No GATE 1 prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 1 -> GATE 2).
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1 (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** org diagram with typed nodes (see ARTIFACT-HANDOFF INVENTORY: GATE 2 -> GATE 3)

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row. All Escalates destinations name specific diagram nodes.

**CHECKPOINT DIAGRAM-CHECK** -- diagram levels, role sourcing, committees distinct,
5-column headcount, Decides/Escalates split, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** see ARTIFACT-HANDOFF INVENTORY (GATE 2 -> GATE 3).
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
  (see ARTIFACT-HANDOFF INVENTORY)
**Produces:** complete charter set (see ARTIFACT-HANDOFF INVENTORY: GATE 3 -> STATUS)

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm rows first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in any charter Membership.
- DO NOT: Write Quorum without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract):
- Appendices of any kind
- Supplementary sections (tables, notes, annexes)
- Editorial commentary after Anti-Pattern Watch table
- Charters not paired with an operating rhythm row
- Any content outside Steps 3.1 through 3.5

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.
For each governance row, immediately produce its charter before the next ORT row.

Charter template:
```
### [Committee Name]
**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2 roles; TYPE from closed set)
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination present in org diagram; no TBD]
```

**Step 3.2 -- Pair-Count Verification**

- Governance rows in ORT: [N]
- Charters produced: [N]
- Must match. If mismatch: identify gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER**

```
ORG-ELEMENT REGISTER
  cat-1 (Areas): [area name] -- headcount: [N]
  cat-2 (Committees/Cadences): [committee or cadence name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role name from ORT]
```

All four categories populated before Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

>= 2 rows, distinct trigger categories. Row 1 MUST be headcount threshold.
Row 2 from a different category (workload signal, structural symptom, milestone).

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [structural change] | headcount-threshold |
| [different trigger] | [structural change] | [distinct type] |

**Step 3.5 -- Anti-Pattern Watch**

>= 2 rows. Each entry opens with:
`[element name] (cat-N) -- [one sentence]`
Element names copied exactly from ORG-ELEMENT REGISTER. No cat-N code outside schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter. Each check is per-charter; failure halts the loop:

```
Charter: [Committee Name]
[ ] Quorum: value is in form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority
    of members", "quorum required"), bare number without "member roles" suffix, absent
[ ] Membership: each role carries exactly one `(TYPE)` annotation from
    {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: no annotation; out-of-set value ("OWNER","LEAD","APPROVER"); multiple types
[ ] Role continuity: each Membership role name present in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] not in GATE 0 typed list -- HALT loop at this charter;
    add [X] to GATE 0 ROLES-LOADED; re-emit GATE 0 STATUS;
    restart CHARTER-FORMAT-AUDIT from Charter 1 before continuing
```

On any REJECT at any charter: STOP. Correct. Re-run full audit loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count produced
- [ ] Each charter: 5 fields (Name/header, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT loop complete: all charters passed Quorum form, Membership TYPE,
  and per-charter role-continuity check against GATE 0 typed list
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership role names present in GATE 0;
  absent name fails CHECKPOINT-3; remediation: add to GATE 0, re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 all populated
- [ ] Roadmap >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 rows, typed element citations from register
- [ ] GATE 3 prohibited-content contract satisfied (C-30)

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## Variation Delta Summary

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| GATE CHAIN section header | `GATE CHAIN CONTRACT` | `GATE CHAIN PREAMBLE (pre-GATE 0)` | `GATE CHAIN CONTRACT` | `GATE CHAIN PREAMBLE (pre-GATE 0)` | `GATE CHAIN PREAMBLE (pre-GATE 0)` |
| POSITION CONTRACT in preamble | absent | present (forward-declaring + retrospective-record prohibition) | absent | present | present (+ CHECKPOINT-0 verification pointer) |
| STRUCTURING-COST FRAME label | `[Zone: before Step 1.0]` | `[Zone: before Step 1.0]` | `[POSITION CONTRACT: before mechanism table]` | `[POSITION CONTRACT: before mechanism table]` | `[POSITION CONTRACT: before mechanism table + CHECKPOINT-INERTIA pointer]` |
| DO NOT guard (pre-table) | absent | absent | present | present | present |
| Causal explanation in label | absent | absent | present (premise vs. conclusion) | present | present |
| Prohibited form named | absent | absent | present (post-Step 1.1 cost-summary) | present | present |
| CHECKPOINT-0 preamble position item | absent | absent | absent | absent | present |
| CHECKPOINT-INERTIA frame position item | generic "before Step 1.0" | generic "before Step 1.0" | explicit "before Step 1.1 table; prohibited form absent" | explicit | explicit (document-order verification instruction) |
| C-39 predicted | FAIL | FAIL | PASS | PASS | PASS |
| C-40 predicted | FAIL | PASS | FAIL | PASS | PASS |
| Composite predicted | 240/250 | 245/250 | 245/250 | 250/250 | 250/250 |

**Distinguishing V-04 from V-05:** V-04 adds the constraints as DO/DO NOT guards and
labeled position contracts. V-05 additionally closes the loop at checkpoint execution
time: CHECKPOINT-0 explicitly verifies the preamble position via document-order scan,
and CHECKPOINT-INERTIA explicitly verifies the frame position via document-order scan
against the mechanism table boundary. V-04 constraints are detectable by rubric review;
V-05 constraints are also self-enforcing at checkpoint execution time.
