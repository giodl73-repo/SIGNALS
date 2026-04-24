# corps-chart Skill — V-01 through V-05 (Rubric v5)

---

## V-01 — Single Axis: Lifecycle Emphasis
**Hypothesis:** Maximally explicit per-phase scaffolding with inline examples at every step reduces ambiguity and produces the most complete structural output. Every section gets its own instruction block; no step relies on model inference.

---

```
You are generating a corps org chart for the product or domain described below.

## INPUT

ROLES-LOADED:
{{roles}}

DOMAIN:
{{domain}}

TOPIC:
{{topic}}

---

## STEP 1 — ROLE CLASSIFICATION

Read every role in ROLES-LOADED. Emit the block below exactly as formatted.
Use only the four domain types shown — no others.

ROLE-TYPE-CLASSIFICATION
------------------------
[role name] — (strategic | operational | advisory | governance)
[role name] — (strategic | operational | advisory | governance)
...one line per role, every role from ROLES-LOADED included, no role omitted

Domain type definitions:
- strategic: sets direction, owns long-horizon decisions
- operational: executes day-to-day, owns delivery
- advisory: provides input, no binding authority
- governance: approves, audits, or enforces policy

Immediately after the classification block, emit:

ROLE-NAME LOCK
--------------
Permitted role references for the remainder of this document:
[List every role name from ROLES-LOADED, one per line]

This list is the complete permitted set. No role name may appear
in any downstream section — diagram, tables, charters, or prose —
unless it is on this list. Invented role names are prohibited.

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

## STEP 2 — INERTIA ASSESSMENT

Before designing any structure, make the strongest possible case for
staying flat. A weak flat-case produces a low-pressure VERDICT.

### 2a. Case for Staying Flat

Write one paragraph arguing why the current arrangement is defensible.
Then emit a mechanism table (minimum 2 rows):

| Type | Mechanism | Why It Suffices Today |
|------|-----------|----------------------|

Type values (closed vocabulary): coordination / decision / communication / governance
Every row must use one of those four types. No invented types.

### 2b. How We Coordinate Today

Write one paragraph naming the actual artifacts, meetings, DRIs, and
channels the team currently uses. Be concrete: name the specific meeting
or channel, not "we have standups."

### 2c. Rebuttal

Complete the four-field form below. Every field label must appear
exactly as printed. Do not reorder the fields.

ROLE UNDER PRESSURE: [exactly one role from the ROLE-NAME LOCK list]
OBSERVABLE BREAKDOWN: [a current, observable coordination failure —
    not a projection like "as we scale this will break"]
WHY EXISTING MECHANISMS FAIL: [name a specific mechanism from Step 2a
    and explain the precise way it fails for the role above]
RE-ASSESSMENT TRIGGER: [one of: (a) a specific hire count threshold,
    (b) a named milestone event, or (c) a structural symptom such as
    "two or more missed ship dates attributable to cross-area dependency
    disputes" — generic signals like "revisit as the team grows" are
    not acceptable]

### 2d. VERDICT

Open the verdict with this exact prefix format:
FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [one sentence]

Ratings:
- Strong: flat case has no rebuttal; structure adds overhead without benefit
- Moderate: flat case holds today but has a clear expiry condition
- Weak: flat case rests on mechanisms that are already straining
- Negligible: flat case is formally arguable but structurally implausible
- Insufficient: insufficient information to rate; state what is missing

Then declare exactly one conclusion:
- CAN-OPERATE-FLAT: [the condition under which flat remains viable]
  OR
- STRUCTURE-WARRANTED: [the specific coordination problem structure resolves]

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

## STEP 3 — ORG STRUCTURE DIAGRAM

Draw the ASCII org chart. Requirements:
- Minimum two levels of hierarchy (e.g., division → area or area → sub-team)
- Committees must appear as distinct labeled nodes separate from area boxes
  (do not embed committee names inside an area box)
- Every role name that appears in the diagram must be in the ROLE-NAME LOCK list
- Use box-and-line characters: +, -, |, or bracket notation

Acceptable form example:
+---------------------+
|   DIVISION NAME     |
+--------+------------+
         |
   +-----+------+        +---------------------------+
   |  AREA A    |        |  GOVERNANCE COMMITTEE     |
   +------------+        +---------------------------+

Label each node with its area or committee name. If a role is shown
as a node rather than an area, it must appear in ROLE-NAME LOCK.

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

## STEP 4 — HEADCOUNT TABLE

Emit a five-column table with exactly these column headers:

| Area | Headcount | Key Roles | Decides | Escalates |

Rules:
- Key Roles: annotate every role as `[role name] ([domain type])` using
  the domain type from ROLE-TYPE-CLASSIFICATION
- Decides: what this area resolves without escalation — be specific
- Escalates: name the destination (e.g., "Steering Committee") —
  do not write "everything not listed under Decides"
- Minimum two area rows
- Final row must be: `**Total**` | [sum of headcounts] | — | — | —

## STEP 5 — OPERATING RHYTHM TABLE

Emit a four-column table with exactly these headers:

| Cadence | Frequency | DRI / Owner | Purpose |

Requirements:
- Minimum three rows
- The three rows must cover three distinct meeting types:
  (a) ROB: review of business metrics or program health
  (b) Shiproom or gate meeting: active go/no-go or release decision
  (c) Governance meeting: policy review or direction-setting
- Types (a), (b), and (c) must appear as separate rows — they may not
  be merged
- DRI / Owner values must come from ROLE-NAME LOCK

## STEP 6 — COMMITTEE CHARTERS

For every row in the rhythm table that is a governance meeting,
write a charter using exactly this five-field format:

**[Committee Name]**
Purpose: [one sentence]
Membership: [role name] ([domain type]), [role name] ([domain type])
  (minimum two roles; domain types from ROLE-TYPE-CLASSIFICATION)
Decides: [what this committee resolves — be specific]
Escalates: [named destination — not "everything not listed under Decides"]
Quorum: [N] of [M] member roles required for binding decisions

All five fields must be present. A charter missing any field fails C-05.

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

## STEP 7 — ORG-ELEMENT REGISTER

Emit the register block exactly as formatted:

ORG-ELEMENT REGISTER
--------------------
cat-1 (Areas): [area name — N headcount], [area name — N headcount], ...
cat-2 (Committees/Cadences): [committee or cadence name], [name], ...
cat-3 (Headcount): Total = [N]
cat-4 (DRI Roles): [role names that own at least one rhythm row], ...

No category may be empty or absent. This register is the canonical
source for cat-N citations used in the Anti-Pattern Watch section below.

## STEP 8 — ORG EVOLUTION ROADMAP

Before the trigger table, emit this vocabulary block:

TRIGGER-TYPE VOCABULARY
-----------------------
Permitted Type values:
  headcount threshold | workload signal | structural symptom | milestone event
Constraint: no two consecutive rows may share the same Type value.

Then emit the roadmap table:

| Trigger | Structural Change | Type |
|---------|-------------------|------|

Requirements:
- Minimum two rows
- Row 1: must be a headcount threshold (Type = headcount threshold)
- Row 2: must use a different Type from the vocabulary above —
  two headcount thresholds do not satisfy this criterion
- Every Type value in the table must appear in the vocabulary block above

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

## STEP 9 — ANTI-PATTERN WATCH

Before the table, emit this schema block:

CAT-N-CITATION-SCHEMA
---------------------
Valid cat-N codes drawn from the ORG-ELEMENT REGISTER:
  cat-1 (Areas) | cat-2 (Committees/Cadences) | cat-3 (Headcount) | cat-4 (DRI Roles)
Mandatory prefix format for "Why It Applies Here" cells:
  [element name] (cat-N) — [explanation]
Every cell in "Why It Applies Here" must open with this prefix.
Naming an org element without the typed citation syntax is not permitted.

Then emit the table:

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|

Requirements:
- Minimum two rows
- Every "Why It Applies Here" cell must open with `[element name] (cat-N) —`
  using a valid cat-N code from the schema block above
- "Why It Applies Here" cells that name an org element without (cat-N) fail C-09
```

---

## V-02 — Single Axis: Phrasing Register (Conversational Imperative)
**Hypothesis:** Short, direct commands without explanatory scaffolding produce cleaner output by eliminating prose noise around the structural requirements. The model needs the contract, not the rationale for the contract.

---

```
Build an org chart for the domain below. Work through 9 steps in order.
Do not skip steps. Do not merge steps.

ROLES-LOADED: {{roles}}
DOMAIN: {{domain}}
TOPIC: {{topic}}

---

STEP 1 — CLASSIFY ROLES

Write a ROLE-TYPE-CLASSIFICATION block. One line per role.
Tag each role with exactly one type: (strategic), (operational), (advisory), (governance).
Use those four types only.

Then write a ROLE-NAME LOCK block listing every role from ROLES-LOADED.
This is the only set of role names allowed in everything that follows.

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

STEP 2 — ARGUE FOR STAYING FLAT

Write the inertia assessment in four parts:

Part A — Case for Staying Flat
One paragraph, then a mechanism table (2+ rows):
| Type | Mechanism | Why It Suffices Today |
Types allowed: coordination / decision / communication / governance

Part B — How We Coordinate Today
One paragraph. Name specific meetings, DRIs, channels. No generalities.

Part C — Rebuttal
Four fields, this order, these labels:
ROLE UNDER PRESSURE: [one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [something breaking now, not a future risk]
WHY EXISTING MECHANISMS FAIL: [name one mechanism from Part A, explain failure]
RE-ASSESSMENT TRIGGER: [specific hire count, named milestone, or structural symptom]

Part D — VERDICT
Start with: FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [one sentence]
End with exactly one of:
  CAN-OPERATE-FLAT: [condition]
  STRUCTURE-WARRANTED: [what it resolves]

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

STEP 3 — DRAW THE ORG CHART

ASCII box diagram. Two-level hierarchy minimum.
Committees are separate nodes — not inside area boxes.
All role names in the diagram must be in ROLE-NAME LOCK.

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

STEP 4 — HEADCOUNT TABLE

Five columns, no exceptions:
| Area | Headcount | Key Roles | Decides | Escalates |

Key Roles: write each as `[role name] ([domain type])`.
Decides: what this area resolves without going up.
Escalates: name the destination — not "everything else."
Last row: `**Total**` with headcount sum.
Minimum two area rows.

STEP 5 — OPERATING RHYTHM TABLE

| Cadence | Frequency | DRI / Owner | Purpose |

Three rows minimum. Each must be a different type:
(a) ROB, (b) shiproom or gate, (c) governance. One row per type.
DRI / Owner values must be from ROLE-NAME LOCK.

STEP 6 — COMMITTEE CHARTERS

One charter per governance row in the rhythm table. Five fields each:
Purpose / Membership / Decides / Escalates / Quorum

Membership: 2+ roles as `[name] ([domain type])`.
Escalates: name a destination.
Quorum: [N] of [M] member roles required for binding decisions.

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

STEP 7 — ORG-ELEMENT REGISTER

ORG-ELEMENT REGISTER
--------------------
cat-1 (Areas): [area — N headcount], ...
cat-2 (Committees/Cadences): [names]
cat-3 (Headcount): Total = [N]
cat-4 (DRI Roles): [role names]

All four categories required. No empty categories.

STEP 8 — ORG EVOLUTION ROADMAP

First, emit:
TRIGGER-TYPE VOCABULARY
-----------------------
headcount threshold | workload signal | structural symptom | milestone event
No two consecutive rows may share the same Type.

Then:
| Trigger | Structural Change | Type |

Two rows minimum. Row 1: headcount threshold. Row 2: different type.

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

STEP 9 — ANTI-PATTERN WATCH

First, emit:
CAT-N-CITATION-SCHEMA
---------------------
cat-1 (Areas) | cat-2 (Committees/Cadences) | cat-3 (Headcount) | cat-4 (DRI Roles)
Required prefix in "Why It Applies Here": [element name] (cat-N) — [explanation]

Then:
| Anti-Pattern | Why It Applies Here | Mitigation |

Two rows minimum.
Every "Why It Applies Here" cell must start with [element name] (cat-N) —.
```

---

## V-03 — Single Axis: Inertia Framing (Inertia as Primary Antagonist)
**Hypothesis:** Foregrounding inertia as a serious competitor — by extending its instruction block and framing structure as a claim that must overcome strong resistance — produces a more honest VERDICT and a better-calibrated Rebuttal field.

---

```
You are generating a corps org chart. Before you draw a single box,
you must determine whether structure is actually warranted. Most teams
that request an org chart do not need one yet. Your first job is to
make the strongest possible case against structure. Only if that case
fails does the chart follow.

## INPUT

ROLES-LOADED: {{roles}}
DOMAIN: {{domain}}
TOPIC: {{topic}}

---

## STEP 1 — CLASSIFY ROLES

Emit ROLE-TYPE-CLASSIFICATION. One line per role from ROLES-LOADED.
Each role tagged with exactly one type: (strategic) / (operational) /
(advisory) / (governance). No invented types.

Then emit ROLE-NAME LOCK:
This is the complete permitted set of role references. Every downstream
section — diagram, tables, charters, prose — is bound to this list.

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

## STEP 2 — INERTIA ASSESSMENT

This is the most important section of the document. A team that adds
structure it does not need pays an ongoing coordination tax: slower
decisions, more meetings, more handoffs, more process drag. The cost
is real and permanent. Argue against structure thoroughly.

### The Case for Staying Flat

Write the strongest possible defense of the current flat arrangement.
Address two angles:
1. What coordination problems does flat solve cheaply that structure
   would make expensive?
2. What would be lost if a layer were added now?

Then emit the mechanism table. Minimum 2 rows. Type values are closed:
coordination / decision / communication / governance

| Type | Mechanism | Why It Suffices Today |
|------|-----------|----------------------|

A weak mechanism table (e.g., "we have Slack") produces a low-pressure
VERDICT. Make each mechanism count.

### How We Coordinate Today

Name the actual operating system: the specific recurring meetings,
the DRIs by name, the escalation path, the communication channels.
Do not use generic descriptions. If you do not know the details, say so.

### Where the Flat Case Breaks Down

Every flat case eventually breaks. Find the fracture point now.
Complete the four-field form below. Field order is fixed.

ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK —
    the role whose coordination load is the leading failure indicator]
OBSERVABLE BREAKDOWN: [something that is failing or straining right now,
    observable today — not "as we scale this will become a problem";
    if you cannot name a current breakdown, the flat case may be stronger
    than you think]
WHY EXISTING MECHANISMS FAIL: [take one mechanism from the table above;
    explain the specific way it fails under the load of the role above;
    name the mechanism by its Type and row description]
RE-ASSESSMENT TRIGGER: [the tripwire that would make flat definitively
    untenable — a specific hire count like "12 engineers", a named
    milestone like "Series B close", or a structural symptom like
    "three or more cross-area dependency disputes in a single sprint";
    "when we grow" is not a trigger]

### VERDICT

The verdict is a cost-benefit call. If the flat case is strong and
the breakdown is speculative, rate it Strong. If structure would resolve
a real observable coordination failure, rate it accordingly.

FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [one sentence]

Ratings:
- Strong: flat case holds; structure adds overhead without matching benefit
- Moderate: flat case holds today; has a clear, named expiry condition
- Weak: flat case is arguable but the breakdown is real and present
- Negligible: flat case is formally arguable but structurally implausible
- Insufficient: state what information is missing before this can be rated

Conclude with exactly one of:
  CAN-OPERATE-FLAT: [condition under which this holds — name it precisely]
  STRUCTURE-WARRANTED: [what specific coordination problem structure resolves]

If STRUCTURE-WARRANTED, the rest of this document follows.
If CAN-OPERATE-FLAT, note the re-assessment trigger and stop.

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

## STEP 3 — ORG STRUCTURE DIAGRAM

Structure is now warranted. Draw the ASCII chart.

Requirements:
- Minimum two levels of hierarchy
- Committees appear as distinct labeled nodes, not embedded in area boxes
- All role names in the diagram come from ROLE-NAME LOCK only
- Box-and-line characters required (+, -, |) or bracket notation

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

## STEP 4 — HEADCOUNT TABLE

| Area | Headcount | Key Roles | Decides | Escalates |

Key Roles: `[role name] ([domain type])`. Decides and Escalates are
separate columns. Escalates names a destination. Last row is **Total**.
Minimum two area rows.

## STEP 5 — OPERATING RHYTHM

| Cadence | Frequency | DRI / Owner | Purpose |

Three rows minimum covering: (a) ROB, (b) shiproom or gate, (c) governance.
Each must be a separate row. DRI / Owner values from ROLE-NAME LOCK.

## STEP 6 — COMMITTEE CHARTERS

Per governance meeting in the rhythm table:

**[Committee Name]**
Purpose:
Membership: [role] ([domain type]), [role] ([domain type]) — 2+ roles
Decides:
Escalates: [named destination]
Quorum: [N] of [M] member roles required for binding decisions

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

## STEP 7 — ORG-ELEMENT REGISTER

ORG-ELEMENT REGISTER
--------------------
cat-1 (Areas): [area name — N headcount], ...
cat-2 (Committees/Cadences): [names]
cat-3 (Headcount): Total = [N]
cat-4 (DRI Roles): [names of DRI / Owner roles]

## STEP 8 — ORG EVOLUTION ROADMAP

TRIGGER-TYPE VOCABULARY
-----------------------
headcount threshold | workload signal | structural symptom | milestone event
Constraint: no two consecutive rows may share the same Type.

| Trigger | Structural Change | Type |

Minimum two rows. Row 1: headcount threshold. Row 2: different Type.

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

## STEP 9 — ANTI-PATTERN WATCH

The structure you have designed has failure modes. Name them here.

CAT-N-CITATION-SCHEMA
---------------------
Valid cat-N codes: cat-1 (Areas) | cat-2 (Committees/Cadences) |
  cat-3 (Headcount) | cat-4 (DRI Roles)
Mandatory prefix for "Why It Applies Here":
  [element name] (cat-N) — [explanation]

| Anti-Pattern | Why It Applies Here | Mitigation |

Minimum two rows. "Why It Applies Here" must open with `[element name] (cat-N) —`.
```

---

## V-04 — Combined: Role Sequence (Governance-First) + Output Format (Fill-In Templates)
**Hypothesis:** Processing governance roles before area roles prevents charter placeholder errors; providing exact fill-in column templates as part of the instruction reduces format deviation and makes table compliance mechanically checkable.

---

```
Generate a corps org chart. Process roles in governance-first order:
classify governance roles first, then strategic, then operational, then
advisory. This sequencing ensures committee charters can be written
against concrete governance role definitions before area structures are drawn.

ROLES-LOADED: {{roles}}
DOMAIN: {{domain}}
TOPIC: {{topic}}

---

## STEP 1 — ROLE CLASSIFICATION (GOVERNANCE-FIRST)

Emit ROLE-TYPE-CLASSIFICATION in this order:
1. All roles tagged (governance) — listed first
2. All roles tagged (strategic)
3. All roles tagged (operational)
4. All roles tagged (advisory)

Format:
ROLE-TYPE-CLASSIFICATION
------------------------
[role name] — (governance)     ← governance tier, all entries
[role name] — (strategic)      ← strategic tier, all entries
[role name] — (operational)    ← operational tier, all entries
[role name] — (advisory)       ← advisory tier, all entries

Every role from ROLES-LOADED must appear. No invented types.

Immediately after, emit:

ROLE-NAME LOCK
--------------
[Every role from ROLES-LOADED, one per line]
This list is the complete permitted set for all downstream sections.

---

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

## STEP 2 — INERTIA ASSESSMENT

Fill in each section below.

### Case for Staying Flat

[Paragraph defending flat arrangement]

Mechanism table — fill in all rows, minimum 2:
+-----------+-------------------+-----------------------+
| Type      | Mechanism         | Why It Suffices Today |
+-----------+-------------------+-----------------------+
| [coord/   | [name mechanism]  | [specific reason]     |
|  decision/|                   |                       |
|  comms/   |                   |                       |
|  govern]  |                   |                       |
+-----------+-------------------+-----------------------+

(Continue rows as needed. Type values: coordination / decision /
communication / governance — no others.)

### How We Coordinate Today

[Paragraph naming specific meetings, DRIs, channels]

### Rebuttal — fill in all four fields in order:

ROLE UNDER PRESSURE:     [one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN:    [current failure, not future projection]
WHY EXISTING MECHANISMS FAIL: [one mechanism from table above + failure mode]
RE-ASSESSMENT TRIGGER:   [hire count / named milestone / structural symptom]

### VERDICT

FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [sentence]

[Exactly one of:]
CAN-OPERATE-FLAT:     [condition]
STRUCTURE-WARRANTED:  [what it resolves]

---

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

## STEP 3 — ORG STRUCTURE DIAGRAM

Draw ASCII org chart. Rules: two-level minimum, committees as separate
nodes, all role names from ROLE-NAME LOCK only.

---

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

## STEP 4 — HEADCOUNT TABLE

Fill in with exactly five columns:
+------+-----------+---------------+------------------+------------------+
| Area | Headcount | Key Roles     | Decides          | Escalates        |
+------+-----------+---------------+------------------+------------------+
| [A]  | [N]       | [role (type)] | [decision scope] | [destination]    |
| [B]  | [N]       | [role (type)] | [decision scope] | [destination]    |
| **Total** | [sum]| —             | —                | —                |
+------+-----------+---------------+------------------+------------------+

Key Roles: `[role name] ([domain type])`. Escalates must name a destination.
Minimum two area rows.

## STEP 5 — OPERATING RHYTHM TABLE

Fill in with exactly four columns. Minimum three rows of distinct types.

+-------------------+-----------+----------------+---------------------+
| Cadence           | Frequency | DRI / Owner    | Purpose             |
+-------------------+-----------+----------------+---------------------+
| [ROB row]         | [freq]    | [role]         | [purpose]           |
| [Shiproom row]    | [freq]    | [role]         | [purpose]           |
| [Governance row]  | [freq]    | [role]         | [purpose]           |
+-------------------+-----------+----------------+---------------------+

DRI / Owner values must be from ROLE-NAME LOCK.
Three row types must be distinct: ROB ≠ shiproom ≠ governance.

## STEP 6 — COMMITTEE CHARTERS

For every governance row in the rhythm table, fill in:

**[Committee Name]**
Purpose:     [sentence]
Membership:  [role] (governance), [role] (strategic)    ← 2+ roles with type
Decides:     [specific scope]
Escalates:   [named destination — not "everything else"]
Quorum:      [N] of [M] member roles required for binding decisions

---

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

## STEP 7 — ORG-ELEMENT REGISTER

ORG-ELEMENT REGISTER
--------------------
cat-1 (Areas):              [area — N headcount], [area — N headcount]
cat-2 (Committees/Cadences): [committee name], [cadence name]
cat-3 (Headcount):          Total = [N]
cat-4 (DRI Roles):          [role], [role]

All four cat lines required. No category empty.

## STEP 8 — ORG EVOLUTION ROADMAP

TRIGGER-TYPE VOCABULARY
-----------------------
Permitted Type values (closed set):
  headcount threshold | workload signal | structural symptom | milestone event
Rule: no two consecutive rows may share the same Type value.

+---------------------------+---------------------------+-----------------------+
| Trigger                   | Structural Change         | Type                  |
+---------------------------+---------------------------+-----------------------+
| [headcount threshold]     | [change]                  | headcount threshold   |
| [different-type trigger]  | [change]                  | [different type]      |
+---------------------------+---------------------------+-----------------------+

Row 1 must be headcount threshold. Row 2 must be a different Type.

---

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

## STEP 9 — ANTI-PATTERN WATCH

CAT-N-CITATION-SCHEMA
---------------------
Valid cat-N codes (from ORG-ELEMENT REGISTER):
  cat-1 (Areas) | cat-2 (Committees/Cadences) | cat-3 (Headcount) | cat-4 (DRI Roles)
Required prefix for every "Why It Applies Here" cell:
  [element name] (cat-N) — [explanation]
Cells that name an org element without (cat-N) are non-compliant.

Fill in table (minimum 2 rows):
+---------------------+----------------------------------------+-----------------------+
| Anti-Pattern        | Why It Applies Here                    | Mitigation            |
+---------------------+----------------------------------------+-----------------------+
| [anti-pattern name] | [element name] (cat-N) — [explanation] | [mitigation action]   |
| [anti-pattern name] | [element name] (cat-N) — [explanation] | [mitigation action]   |
+---------------------+----------------------------------------+-----------------------+
```

---

## V-05 — Combined: Lifecycle Emphasis (Compressed) + Inertia Framing (Minimal/Quick)
**Hypothesis:** A dense single-pass instruction set where inertia is treated as a brief mandatory checkpoint rather than a full adversarial section produces faster, equally compliant outputs for teams that have already decided structure is warranted.

---

```
Generate a corps org chart in 9 sequential steps. Do not reorder steps.
Do not skip steps. Each step has a hard output contract.

ROLES-LOADED: {{roles}}
DOMAIN: {{domain}}
TOPIC: {{topic}}

---

STEP 1 | CLASSIFY + LOCK

Output:
  ROLE-TYPE-CLASSIFICATION — one line per role, tagged (strategic) /
  (operational) / (advisory) / (governance). No other types.

  ROLE-NAME LOCK — list every role from ROLES-LOADED. This list is
  the only permitted role reference set for the rest of the document.

=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

STEP 2 | INERTIA CHECK (compact form)

Four required outputs in order:

2a. FLAT-CASE [2–3 sentences + mechanism table]

  | Type | Mechanism | Why It Suffices Today |
  Type values: coordination / decision / communication / governance
  Minimum 2 rows.

2b. TODAY'S OPERATING SYSTEM [1 paragraph — specific artifacts only]

2c. REBUTTAL [four-field form, fixed order]
  ROLE UNDER PRESSURE: [role from ROLE-NAME LOCK]
  OBSERVABLE BREAKDOWN: [current failure — not future projection]
  WHY EXISTING MECHANISMS FAIL: [mechanism from 2a + failure mode]
  RE-ASSESSMENT TRIGGER: [hire count | named milestone | structural symptom]

2d. VERDICT
  FLAT-CASE-PRESSURE: [Strong | Moderate | Weak | Negligible | Insufficient] — [sentence]
  [CAN-OPERATE-FLAT: condition]  OR  [STRUCTURE-WARRANTED: what it resolves]

=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

STEP 3 | ASCII ORG CHART

Two-level hierarchy minimum. Committees = separate nodes (not inside
area boxes). All names in diagram must be in ROLE-NAME LOCK.

=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

STEP 4 | HEADCOUNT TABLE — five columns, no exceptions

  | Area | Headcount | Key Roles | Decides | Escalates |

  Key Roles: `[role] ([type])`. Escalates: named destination.
  Last row: **Total** + sum. Min 2 area rows.

STEP 5 | OPERATING RHYTHM — four columns

  | Cadence | Frequency | DRI / Owner | Purpose |

  Min 3 rows: (a) ROB, (b) shiproom/gate, (c) governance — one each,
  no merging. DRI / Owner values from ROLE-NAME LOCK.

STEP 6 | COMMITTEE CHARTERS

  Per governance row. Five fields each:
  Purpose / Membership [2+ roles with type] / Decides / Escalates
  [named destination] / Quorum: [N] of [M] member roles required

=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

STEP 7 | ORG-ELEMENT REGISTER

  ORG-ELEMENT REGISTER
  --------------------
  cat-1 (Areas): [area — N headcount], ...
  cat-2 (Committees/Cadences): [names]
  cat-3 (Headcount): Total = [N]
  cat-4 (DRI Roles): [role names]

  All four categories required. None may be empty.

STEP 8 | ORG EVOLUTION ROADMAP

  First emit:
  TRIGGER-TYPE VOCABULARY
  -----------------------
  headcount threshold | workload signal | structural symptom | milestone event
  Constraint: no two consecutive rows may share the same Type.

  Then emit table:
  | Trigger | Structural Change | Type |

  Min 2 rows. Row 1: headcount threshold. Row 2: different Type.

=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===

STEP 9 | ANTI-PATTERN WATCH

  First emit:
  CAT-N-CITATION-SCHEMA
  ---------------------
  cat-1 (Areas) | cat-2 (Committees/Cadences) | cat-3 (Headcount) | cat-4 (DRI Roles)
  Required prefix: [element name] (cat-N) — [explanation]

  Then emit table:
  | Anti-Pattern | Why It Applies Here | Mitigation |

  Min 2 rows. Each "Why It Applies Here" cell must open with
  `[element name] (cat-N) —`. No exceptions.
```

---

## Variation Summary

| Variation | Axis | Hypothesis | Key Structural Bet |
|-----------|------|------------|--------------------|
| V-01 | Lifecycle Emphasis (maximal) | Full per-phase scaffolding + inline examples eliminates output gaps | Verbose instruction at each step reduces skipped sections |
| V-02 | Phrasing Register (imperative) | Short commands without rationale produce cleaner compliance | Model follows contracts, not explanations |
| V-03 | Inertia Framing (antagonist-first) | Leading with resistance produces a better-calibrated VERDICT and Rebuttal | Quality of inertia section predicts quality of the whole doc |
| V-04 | Role sequence + Output format | Governance-first ordering + fill-in templates reduce role-coherence errors and table format drift | Structural templates make compliance syntactically checkable |
| V-05 | Lifecycle (compressed) + Inertia (minimal) | Dense single-pass with light inertia checkpoint is fastest path to full structural compliance | Overhead reduction for teams already convinced structure is warranted |
