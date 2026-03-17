---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R12
rubric_version: v12
status: variate
---

# org-chart Variate -- Round 12 (Rubric v12)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v12 (C-01 through C-38; C-37/C-38 new from R11 excellence signals)
**Round:** R12 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

## R11 ceiling and R12 target

R11-V-02 achieves full coverage of C-01 through C-36 under the v11 rubric (230 pts).
Under v12, R11-V-02 scores 230/240: all v11 criteria pass, but both new v12 criteria
(C-37 and C-38, 5 pts each) are absent.

**C-37 gap (GATE 1 Inertia Assessment cost-framing enrichments):**
R11-V-02 GATE 1 has four sub-sections with FLAT-CASE-PRESSURE, VERDICT, and a concrete
re-assessment trigger. C-37 requires three additional cost-framing constructs on top of
C-01's minimum: (1) a STRUCTURING-COST FRAME named block before the sub-sections that
enumerates the overhead imposed by formal structure; (2) a NET-COST-COMPARISON block or
table within sub-section 4 that places inertia costs alongside restructuring costs and
yields an explicit net-cost differential; (3) a SUB-SECTION-4-ANCHOR-SEQUENCE in which
sub-section 4 uses an ordered anchor sequence (numbered steps or anchored items) rather
than a narrative paragraph. All three constructs must be present for C-37 to pass.
R11-V-02's sub-section 4 is a narrative VERDICT paragraph -- zero C-37 constructs present.

**C-38 gap (Explicit GATE CHAIN block with named artifact handoffs):**
R11-V-02 has a GATE CHAIN CONTRACT preamble and per-gate "Named artifact handoff"
declarations at each gate boundary. C-38 requires a single dedicated block that
enumerates all four gate transitions and the specific artifact produced/consumed at each.
The distributed per-gate prose satisfies C-25 (per-gate-interface artifact naming) but
not C-38: the artifact handoff inventory is only reconstructable by reading all four gate
sections in sequence. C-38 requires a consolidated block making cross-gate artifact
traceability self-contained and independently verifiable at one structural location.

**R12 target:**
- V-01: control (R11-V-02 baseline; no C-37 or C-38 constructs). 230/240 predicted.
- V-02: single-axis -- NET-COST-COMPARISON table only (partial C-37 probe). 230/240 predicted.
- V-03: single-axis -- STRUCTURING-COST FRAME only (partial C-37 probe). 230/240 predicted.
- V-04: multi-axis -- all three C-37 constructs. C-37 PASS; C-38 absent. 235/240 predicted.
- V-05: maximum integration -- V-04 + ARTIFACT-HANDOFF INVENTORY block. C-37 + C-38. 240/240.

---

## R12 Variation Map

| V    | Axis                                              | C-37 constructs present                                                                    | C-38 | Predicted |
|------|---------------------------------------------------|--------------------------------------------------------------------------------------------|------|-----------|
| V-01 | Phrasing register (formal/imperative; R12 control)| none                                                                                       | no   | 230/240   |
| V-02 | Output format (NET-COST-COMPARISON table added)   | NET-COST-COMPARISON only                                                                   | no   | 230/240   |
| V-03 | Inertia framing (STRUCTURING-COST FRAME added)    | STRUCTURING-COST FRAME only                                                                | no   | 230/240   |
| V-04 | GATE 1 cost-framing depth (all three C-37)        | STRUCTURING-COST FRAME + NET-COST-COMPARISON + SUB-SECTION-4-ANCHOR-SEQUENCE              | no   | 235/240   |
| V-05 | Maximum integration (V-04 + GATE CHAIN block)     | STRUCTURING-COST FRAME + NET-COST-COMPARISON + SUB-SECTION-4-ANCHOR-SEQUENCE              | yes  | 240/240   |

**Single-axis hypothesis:**
- V-01: All 36 v11 criteria inherited; C-37 and C-38 both absent. 230/240 = 95.8%.
  Establishes the R12 control against which V-02 through V-05 are compared.
- V-02: NET-COST-COMPARISON table in sub-section 4 only. C-37 requires all three constructs;
  partial presence is not sufficient per bypass specification. C-37 FAIL predicted.
  Probes whether the most structurally visible enrichment (cost table) registers independently.
- V-03: STRUCTURING-COST FRAME block before sub-section 1 only. Missing NET-COST-COMPARISON
  and SUB-SECTION-4-ANCHOR-SEQUENCE. C-37 FAIL predicted. V-02 vs V-03 comparison isolates
  whether the pre-assessment FRAME or the in-VERDICT table produces the stronger partial signal.
- V-04: All three C-37 constructs present in GATE 1. STRUCTURING-COST FRAME (pre-assessment
  cost inventory), NET-COST-COMPARISON (table with signed net delta in anchor step 2), and
  SUB-SECTION-4-ANCHOR-SEQUENCE (numbered 1-4 replacing narrative paragraph). C-37 PASS
  predicted. Per-gate "Named artifact handoff" prose satisfies C-25 but not C-38. +5 pts.
- V-05: V-04 + dedicated GATE CHAIN ARTIFACT-HANDOFF INVENTORY block at document head
  naming all four transitions with specific artifact names. C-38 PASS predicted. +10 pts
  total over V-01. Full 240/240.

---

## V-01 -- Phrasing Register (Formal/Imperative); R12 Control

**Axis:** phrasing register -- formal DO/DO NOT register throughout; every gate step and
checkpoint uses explicit DO/DO NOT guards; inherits R11-V-02 CHARTER-FORMAT-AUDIT loop
with per-charter role-continuity check (C-35 and C-36 PASS); no C-37 or C-38 constructs.
**Hypothesis:** R11-V-02 baseline achieves C-01 through C-36 (230 pts under v11). Under v12
both new criteria absent. Composite predicted: 230/240 (95.8%). R12 control point.

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
gate labels. Every gate carries a dedicated verification checkpoint before STATUS -- no
gate may emit STATUS without its own checkpoint clearing first.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- the following content types MUST NOT appear within GATE 0
before STATUS is emitted:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block -- no structural content may appear between Step 0.1
and Step 0.2. Every role listed in Step 0.1 MUST be typed from the closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order: DECISION first,
EXECUTION second, ADVISORY/GOVERNANCE third.

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

MUST NOT proceed past this block until every role from Step 0.1 is typed.

**CHECKPOINT-0 (C-29 -- all-gate blocking)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block is present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content appeared between Step 0.1 and Step 0.2
- [ ] No content from the GATE 0 CONTAINMENT CONTRACT appears above this line

All checkboxes MUST be ticked before GATE 0 STATUS can read PASS.

```
GATE 0 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 1. Correct the gap above and re-verify.

**Named artifact handoff:** GATE 1 requires the typed role list produced here.
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as the first executable step (Step 1.0),
  before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use "the team is growing" as a rebuttal without naming the failure mode.
- DO NOT: Use a FLAT-CASE-PRESSURE rating outside the closed set {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows" -- trigger MUST name a concrete condition.

GATE 1 PROHIBITED CONTENT -- MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields (Mission, Membership, Quorum, Escalates)

**Step 1.0 -- Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1.
It MUST precede the mechanism table. It is not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator protocol:
- Step A: Count mechanism rows written above.
- Step B: If count < 2, write missing rows first. Once count >= 2, substitute as N and emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT -- GUARD:** DO NOT EMIT the separator before row count >= 2.
DO NOT begin Step 1.2 until the separator appears in output.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list mechanism rows from Step 1.1.

**Step 1.3 -- Rebuttal**

Name the coordination failure the flat case cannot answer. Reference a specific observable
with a quantifier (count, duration, date, or dollar magnitude).

```
UNCOVERED: [function or decision class with no current owner under flat structure]
```

**Step 1.4 -- VERDICT and Re-assessment Trigger**

Choose exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. Provide one reasoning
sentence. State a concrete re-assessment trigger.

```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH] -- [one sentence: mechanism count + cost anchor]

VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
Reasoning: [one sentence]

RE-ASSESSMENT TRIGGER: [concrete measurable threshold -- not "revisit as the team grows"]
```

Flat-verdict branch -- if CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning sentence
- [ ] Re-assessment trigger is concrete (not "revisit as the team grows")
- [ ] No prohibited content from GATE 1 contract appears above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns -- separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (annotated with `(domain type)`), Decides,
Escalates. Minimum two area rows + Total row.

Inline example row (complete, not a label):

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

**CHECKPOINT DIAGRAM-CHECK (C-22 -- blocking)**

Before emitting GATE 2 STATUS, verify:
- [ ] ASCII diagram >= 2 hierarchy levels
- [ ] All role names from ROLES-LOADED; committees as distinct nodes
- [ ] Headcount: 5 columns, Decides/Escalates split, >= 2 area rows + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm rows first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in charter Membership.
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
For each governance cadence row, immediately produce its charter before the next row.

Charter template:
```
### [Committee Name]
**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2 roles; TYPE from closed set)
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination present in org diagram; no TBD]
```

REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles`. Percentage, prose quorum, absent: not acceptable.

**Step 3.2 -- Pair-Count Verification**

- Governance rows in ORT: [N]
- Charters produced: [N]
- MUST match. Correct and recount if mismatch. DO NOT advance until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER** (cat-1 Areas, cat-2 Committees/Cadences,
cat-3 Headcount, cat-4 DRI Roles -- all four populated before Step 3.4)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows; Row 1: headcount threshold;
Row 2: distinct trigger category)

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows; `[element name] (cat-N) -- [one sentence]`)

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter:

```
Charter: [Committee Name]
[ ] Quorum: value is in form `[integer] of [integer] member roles`
    REJECT: fractional ("3/5"), percentage ("60%"), prose ("majority"), bare number, absent
[ ] Membership: each role carries exactly one `(TYPE)` from
    {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: no annotation; out-of-set value ("OWNER","LEAD","APPROVER"); multiple per entry
[ ] Role continuity: each Membership role name present in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] absent -- HALT loop; add [X] to GATE 0 ROLES-LOADED;
    re-emit GATE 0 STATUS; restart CHARTER-FORMAT-AUDIT from Charter 1 before continuing
```

On any REJECT: STOP. Correct. Re-run full audit loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34)**

- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count
- [ ] Each charter: 5 fields (Name/header, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT loop complete: all charters passed Quorum form, Membership TYPE,
  and per-charter role-continuity check
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership role names in GATE 0; absent name
  fails CHECKPOINT-3 with directive to add to GATE 0 and re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 all populated
- [ ] Org Evolution Roadmap: >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch: >= 2 rows, typed element citations from register
- [ ] GATE 3 prohibited-content contract satisfied

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-02 -- Output Format: NET-COST-COMPARISON Table Only (Partial C-37 Probe)

**Axis:** output format -- add a NET-COST-COMPARISON table in sub-section 4 that places
inertia costs (from FLAT-CASE-CLOSED total) alongside structuring costs and yields a signed
net delta. No STRUCTURING-COST FRAME before sub-section 1; sub-section 4 remains a prose
paragraph with the table inserted. All sections outside GATE 1 Step 1.4 unchanged.
**Hypothesis:** C-37 requires all three constructs to be present simultaneously. Adding only
NET-COST-COMPARISON (missing STRUCTURING-COST FRAME and SUB-SECTION-4-ANCHOR-SEQUENCE) does
not satisfy C-37. The variation probes whether partial coverage registers as a scoring signal
or whether C-37 is strictly all-or-nothing. C-37 FAIL predicted; expected: 230/240. The
comparison with V-03 isolates whether the in-VERDICT table or the pre-assessment FRAME
produces the larger partial signal.

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
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after roles block; no structural content between steps. Closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION: [role names]
  EXECUTION: [role names]
  ADVISORY: [role names]
  GOVERNANCE: [role names]
```

GATE 0 CONTAINMENT: no inertia rows, diagram nodes, headcount, rhythm rows, or charter
fields before GATE 0 STATUS.

**CHECKPOINT-0** -- ROLES-LOADED/NOTE present; all roles typed; containment satisfied;
no structural content between 0.1 and 0.2.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires the typed role list produced here.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT: default-position before mechanism rows; 4 sub-sections in sequence;
no diagram, headcount, rhythm, or charter content; FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH};
no "revisit as the team grows."

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [specific mechanism] | [observable evidence] |
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [second mechanism] | [evidence] |

Minimum 2 rows. When count >= 2:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination. DO NOT re-list Step 1.1 rows.

**Step 1.3 -- Rebuttal**

```
UNCOVERED: [function or decision class with no current owner under flat structure]
```

**Step 1.4 -- VERDICT with NET-COST-COMPARISON**

Before the VERDICT declaration, produce the following table:

```
NET-COST-COMPARISON:
| Cost Category                           | Flat Coordination      | Formal Structure        |
|-----------------------------------------|------------------------|-------------------------|
| Coordination mechanism overhead         | [X eng-weeks/qtr]      | [X eng-weeks/qtr]       |
| Committee formation + charter maintenance| --                    | [Y eng-weeks/qtr]       |
| Governance cadence load                 | --                     | [Y eng-weeks/qtr]       |
| UNCOVERED failure-mode cost             | [Z eng-weeks/qtr]      | [reduced Z eng-weeks]   |
| Net total                               | [T_flat]               | [T_struct]              |
Net delta: T_struct - T_flat = [signed value]
Interpretation: positive = structure costs more; negative = structure produces net savings.
VERDICT must follow from the sign of this delta.
```

Then declare:

```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH] -- [one sentence: mechanism count + cost anchor]

VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
Reasoning: [one sentence grounded in the net delta above]

RE-ASSESSMENT TRIGGER: [concrete measurable threshold]
```

Flat-verdict: emit ABSENT labels; STOP.

**CHECKPOINT INERTIA-CHECK** -- 4 sub-sections; NET-COST-COMPARISON table present;
FLAT-CASE-PRESSURE from closed set; VERDICT with reasoning; concrete trigger.

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

**Step 2.1 -- ASCII Org Diagram** (>= 2 levels; committees distinct; roles from ROLES-LOADED)

**Step 2.2 -- Headcount by Area** (5 cols: Area, Headcount, Key Roles `(type)`,
Decides, Escalates; >= 2 area rows + Total)

**CHECKPOINT DIAGRAM-CHECK** -- levels, sourcing, columns, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT: interleave rhythm/charters; pair count; no undeclared roles;
Quorum fraction form; TYPE annotation required. GATE 3 PROHIBITED CONTENT (C-30):
appendices, supplementary sections, post-watch commentary, unpaired charters.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**
>= 3 cadences; each governance row immediately followed by charter; Membership >= 2
roles with `(TYPE)`; Quorum as `N of M member roles`.

**Step 3.2 -- Pair-Count Verification** (match required; correct and recount if mismatch)

**Step 3.3 -- ORG-ELEMENT REGISTER** (cat-1 through cat-4 populated)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows; distinct trigger categories)

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows; typed element citations from register)

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36)**

For each charter, in sequence, before advancing to next:
```
Charter: [Committee Name]
[ ] Quorum: `[integer] of [integer] member roles` (REJECT: fraction, %, prose, absent)
[ ] Membership: each role has `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    (REJECT: missing; out-of-set; multiple per entry)
[ ] Role continuity: each Membership role in GATE 0 typed list
    (REJECT: undeclared -- HALT; add to GATE 0; re-emit GATE 0 STATUS; restart loop)
```

**CHECKPOINT-3** -- ORT >= 3 rows; pair count; 5-field charters; CHARTER-FORMAT-AUDIT all
three checks; ROLE-CONTINUITY aggregate backup; REGISTER cat-1 through cat-4; Roadmap >= 2
distinct trigger rows; Anti-Pattern Watch >= 2 typed rows; no prohibited content.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE.

---

## V-03 -- Inertia Framing: STRUCTURING-COST FRAME Only (Partial C-37 Probe)

**Axis:** inertia framing -- add a labeled STRUCTURING-COST FRAME block before Step 1.0
enumerating the overhead imposed by formal structure as named cost items. Sub-section 4
remains a prose VERDICT paragraph (no NET-COST-COMPARISON table, no anchor sequence).
All sections outside GATE 1 unchanged from V-01.
**Hypothesis:** C-37 requires all three constructs simultaneously. This variation adds only
the STRUCTURING-COST FRAME -- the pre-assessment block that establishes the cost adversary
framing before the flat case is argued. Without NET-COST-COMPARISON and without the SUB-
SECTION-4-ANCHOR-SEQUENCE, C-37 FAIL predicted. The V-02 vs V-03 comparison isolates
whether the in-VERDICT NET-COST-COMPARISON table or the pre-assessment FRAME is the stronger
partial signal. Expected: 230/240.

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
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

**Step 0.1 -- Load Roles**

Glob `.craft/roles/`. Produce ROLES-LOADED or ROLES-NOTE.
Every role name in this document must be declared here first.

**Step 0.2 -- Role-Type Classification**

Immediately after roles block. All roles from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Three-tier order: DECISION > EXECUTION > ADVISORY/GOVERNANCE.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION: [role names]
  EXECUTION: [role names]
  ADVISORY: [role names]
  GOVERNANCE: [role names]
```

GATE 0 CONTAINMENT: no inertia rows, diagram, headcount, rhythm, charter content before STATUS.

**CHECKPOINT-0** -- roles block present; all typed; containment satisfied.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires the typed role list produced here.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT** [Zone: before Step 1.0]

Before presenting the flat case, enumerate the overhead imposed by introducing formal
structure. This block establishes the cost denominator: structure must produce net
savings greater than this overhead to be warranted. VERDICT (Step 1.4) must name the
dominant cost category identified here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter authoring, role assignment, initial standing-meeting design -- eng-weeks
     estimated for first governance cycle]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries;
     handoff latency for work previously handled by one person -- eng-weeks/qtr]
  Governance cadence tax:
    [sum of recurring governance meetings at steady state -- eng-hours/qtr converted
     to eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews, charter upkeep]
```

VERDICT must acknowledge whether flat coordination cost exceeds or falls below the
governance overhead enumerated in this FRAME.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
When count >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**Step 1.2 -- How We Coordinate Today**

Inventory coordination. DO NOT re-list Step 1.1 rows.

**Step 1.3 -- Rebuttal**

```
UNCOVERED: [decision class or function with no current owner under flat structure]
```

**Step 1.4 -- VERDICT and Re-assessment Trigger**

```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH] -- [one sentence: mechanism count + cost anchor]

VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
Reasoning: [one sentence; must name dominant cost category from STRUCTURING-COST FRAME]

RE-ASSESSMENT TRIGGER: [concrete measurable threshold]
```

Flat-verdict: emit ABSENT labels; STOP.

**CHECKPOINT INERTIA-CHECK** -- STRUCTURING-COST FRAME present before Step 1.0; 4 sub-sections;
FLAT-CASE-PRESSURE from closed set; VERDICT cites FRAME dominant cost; concrete trigger.

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

**Step 2.1 -- ASCII Org Diagram** (>= 2 levels; committees distinct; roles from ROLES-LOADED)

**Step 2.2 -- Headcount by Area** (5 cols; Decides/Escalates split; >= 2 areas + Total)

**CHECKPOINT DIAGRAM-CHECK** -- verified.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT: interleave; pair count; no undeclared roles; Quorum fraction form;
TYPE annotation. GATE 3 PROHIBITED CONTENT (C-30): appendices, supplementary sections,
post-watch commentary, unpaired charters, content outside Steps 3.1--3.5.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**
>= 3 cadences; each governance row immediately with its charter; Membership >= 2
roles with `(TYPE)`; Quorum as `N of M member roles`.

**Step 3.2 -- Pair-Count Verification**

**Step 3.3 -- ORG-ELEMENT REGISTER** (cat-1 through cat-4)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows; distinct triggers)

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows; typed element citations)

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36)**

Per-charter loop:
```
Charter: [Committee Name]
[ ] Quorum: `[integer] of [integer] member roles` (REJECT: fraction, %, prose, bare, absent)
[ ] Membership: `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE} on each role
    (REJECT: missing; out-of-set; multiple per entry)
[ ] Role continuity: each name in GATE 0 typed list
    (REJECT: undeclared -- HALT; add to GATE 0; re-emit GATE 0 STATUS; restart loop)
```

**CHECKPOINT-3** -- ORT >= 3 rows; pair count; 5-field charters; all audit checks; aggregate
ROLE-CONTINUITY backup; REGISTER cat-1 through cat-4; Roadmap >= 2; Watch >= 2; no C-30 violation.

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE.

---

## V-04 -- GATE 1 Cost-Framing Depth: All Three C-37 Constructs (Multi-Axis, C-37 Target)

**Axis:** GATE 1 cost-framing depth -- adds all three C-37 constructs to GATE 1 on the
V-01 baseline: (1) STRUCTURING-COST FRAME named block before Step 1.0; (2) NET-COST-
COMPARISON table within anchor step 2 of the numbered sub-section 4 sequence; (3) SUB-
SECTION-4-ANCHOR-SEQUENCE replacing the narrative VERDICT paragraph with a numbered 1-4
anchor sequence (FLAT-CASE-PRESSURE -> NET-COST-COMPARISON -> VERDICT -> RE-ASSESSMENT
TRIGGER). GATE CHAIN CONTRACT and all other sections unchanged from V-01 baseline:
per-gate "Named artifact handoff" prose satisfies C-25 but no consolidated GATE CHAIN
ARTIFACT-HANDOFF INVENTORY block.
**Hypothesis:** All three C-37 constructs present; C-37 PASS predicted (+5 pts over V-01).
C-38 absent: artifact handoffs distributed across four gate sections satisfy C-25 but the
inventory is not independently verifiable at one structural location. Composite: 235/240.

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
gate labels. Every gate carries a dedicated verification checkpoint before STATUS -- no
gate may emit STATUS without its own checkpoint clearing first.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

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
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after roles block; no structural content between steps. Closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order enforced.

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

MUST NOT proceed until every role typed.

**CHECKPOINT-0** -- ROLES-LOADED/NOTE present; all typed; containment satisfied;
no structural content between 0.1 and 0.2.

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires the typed role list produced here.
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Emit STRUCTURING-COST FRAME block before Step 1.0.
- DO: Write default-position statement (Step 1.0) before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Use numbered anchor sequence in Step 1.4 (not a narrative paragraph).
- DO NOT: Write diagram, headcount, rhythm rows, or charter fields before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII diagram nodes, headcount rows, rhythm cadence rows,
charter fields (Mission, Membership, Quorum, Escalates).

**STRUCTURING-COST FRAME -- PRE-ASSESSMENT** [Zone: before Step 1.0]

Before any flat-case argument, enumerate the overhead imposed by formal structure.
This frame establishes the cost denominator. VERDICT anchor step 3 must cite the
dominant cost category identified here.

```
STRUCTURING-COST FRAME:
  Committee formation cost:
    [charter creation, role assignment, onboarding to standing meetings -- eng-weeks for
     first governance cycle]
  Role specialization overhead:
    [coordination increase as generalist scope narrows to formal role boundaries;
     handoff latency introduced -- eng-weeks/qtr or days/decision]
  Governance cadence tax:
    [recurring governance meetings at steady state -- eng-hours/qtr converted to
     eng-weeks/qtr; covers ROB prep, shiproom cycles, board reviews, charter maintenance]
```

VERDICT (anchor step 3) must name the dominant cost category and declare whether flat
coordination cost exceeds or falls below this governance overhead.

**Step 1.0 -- Default-Position Statement**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step. MUST precede the mechanism table. Not a preamble.

**Step 1.1 -- Case for Staying Flat**

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

Type closed set: {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}. Minimum 2 rows.
Two-step separator:
- Count rows. If < 2, write missing rows first.
- When count >= 2, emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

GUARD: DO NOT emit separator before count >= 2. DO NOT begin Step 1.2 before separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination channels, cadences, informal roles, artifacts.
DO NOT re-list Step 1.1 rows.

**Step 1.3 -- Rebuttal**

Name the ONE failure mode flat coordination cannot resolve. Specific observable with
a quantifier (count, duration, date, or dollar magnitude).

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
   must be independently verifiable without team-size narrative]
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
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set; FLAT-CASE-CLOSED separator emitted
- [ ] Step 1.4 uses numbered anchor sequence 1-4 (not a narrative paragraph)
- [ ] NET-COST-COMPARISON table present at anchor step 2 with signed net delta declared
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED}; cites dominant FRAME cost
- [ ] RE-ASSESSMENT TRIGGER concrete; not growth narrative
- [ ] No prohibited content from GATE 1 contract above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns.
- DO NOT: Introduce undeclared role names.
- DO NOT: Merge Decides and Escalates into one column.

GATE 2 PROHIBITED CONTENT: operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED. Use box-drawing characters (+, -, |).

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles `(domain type)`, Decides, Escalates.
Minimum two area rows + Total row.

**CHECKPOINT DIAGRAM-CHECK** -- levels, role sourcing, committees distinct, 5-column
headcount, Decides/Escalates split, no prohibited content.

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave each governance rhythm row immediately with its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Undeclared roles in Membership; Quorum without fraction form; TYPE missing.

GATE 3 PROHIBITED CONTENT (C-30): appendices, supplementary sections, post-watch
commentary, unpaired charters, content outside Steps 3.1--3.5.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.
Each governance row immediately followed by its charter.

```
### [Committee Name]
**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]  (>= 2; TYPE from {DECISION, EXECUTION, ADVISORY, GOVERNANCE})
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination in org diagram; no TBD]
```

**Step 3.2 -- Pair-Count Verification**

Governance rows in ORT: [N]. Charters produced: [N]. Must match.
Correct and recount if mismatch. DO NOT advance until verified.

**Step 3.3 -- ORG-ELEMENT REGISTER**

cat-1 Areas, cat-2 Committees/Cadences, cat-3 Headcount, cat-4 DRI Roles.
All four categories populated before Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

>= 2 rows, distinct trigger categories. Row 1 headcount threshold; Row 2 different.

**Step 3.5 -- Anti-Pattern Watch**

>= 2 rows. `[element name] (cat-N) -- [one sentence]`. Element names from REGISTER exactly.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36)**

Per-charter loop before CHECKPOINT-3:
```
Charter: [Committee Name]
[ ] Quorum: `[integer] of [integer] member roles`
    REJECT: fraction, %, prose quorum, bare number, absent
[ ] Membership: each role has exactly one `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: missing; out-of-set value; multiple per entry
[ ] Role continuity: each Membership role name in GATE 0 ROLES-LOADED/ROLES-NOTE
    REJECT: name [X] absent -- HALT; add to GATE 0; re-emit GATE 0 STATUS; restart loop
```

On any REJECT: STOP. Correct. Re-run full loop from first charter.

**CHECKPOINT-3 (C-29/C-33/C-34)**

- [ ] ORT >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count: ORT governance rows == charter count
- [ ] Each charter: 5 fields (Name, Mission, Membership, Quorum, Escalates)
- [ ] CHARTER-FORMAT-AUDIT: all charters passed all three checks
- [ ] ROLE-CONTINUITY (aggregate backup): all Membership names in GATE 0; absent fails
  CHECKPOINT-3; remediation: add to GATE 0, re-emit GATE 0 STATUS
- [ ] ORG-ELEMENT REGISTER: cat-1 through cat-4 populated
- [ ] Roadmap >= 2 rows, distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 typed rows
- [ ] GATE 3 prohibited-content contract satisfied

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-05 -- Maximum Integration: V-04 + Explicit GATE CHAIN Block (C-37 + C-38)

**Axis:** maximum integration -- V-04 baseline (all three C-37 constructs in GATE 1) plus
a dedicated GATE CHAIN ARTIFACT-HANDOFF INVENTORY block at document head that enumerates
all four gate transitions with specific artifact names in one structural location, making
cross-gate artifact traceability independently verifiable without reading four gate sections.
**Hypothesis:** C-37 PASS from V-04 constructs (+5 pts). C-38 PASS from dedicated ARTIFACT-
HANDOFF INVENTORY block (+5 pts). The block consolidates what V-01 through V-04 leave as
distributed per-gate prose: GATE 0 -> GATE 1 (typed role list), GATE 1 -> GATE 2 (inertia
verdict + FLAT-CASE-PRESSURE rating), GATE 2 -> GATE 3 (org diagram with typed nodes),
GATE 3 -> STATUS (complete charter set). Per-gate "Named artifact handoff" declarations
remain and are consistent with the inventory; the inventory governs if any conflict.
Composite: 240/240 (100%). First full-coverage R12 variation.

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
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [specific mechanism] | [observable evidence with quantifier] |
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [second mechanism] | [evidence with quantifier] |

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

>= 2 rows. Each "Why It Applies Here" opens with:
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
