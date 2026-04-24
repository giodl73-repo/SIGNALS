3. FLAT-CASE-PRESSURE must come from {FLAT, CASE, PRESSURE}.
4. The FLAT branch must terminate the artifact. No content after STOP is acceptable.
5. The org diagram must have >= 2 hierarchy levels.
6. The headcount table must have >= 2 area rows and a Total row.
7. Operating rhythm rows and charters must be produced in interleaved pairs.
8. Quorum must be expressed as "N of M member roles" -- percentage form is not acceptable.
9. Escalates must name a specific destination -- "TBD" is not acceptable.
10. Post-interleave pair count verification is required after all pairs.
11. All 6 checkpoints (A through F) must pass before the artifact is considered complete.
```

---

## V-04 — Axes: Role Sequence + Lifecycle Emphasis

**Hypothesis:** Promoting role typing to the very first gate (before inertia assessment) and framing the entire artifact as a sequence of numbered gates with explicit pass/fail criteria creates structural discipline that prevents role proliferation and ensures each section earns its existence by satisfying measurable criteria. C-19 is targeted via an explicit gate-level count verification.

---

```
# Skill: org-chart

Generate an org structure for a product or domain. This artifact proceeds
through 7 lifecycle gates. Each gate has explicit pass criteria. Gates execute
in order. A FLAT verdict at GATE 1 terminates the artifact at that gate.

---

## GATE 0 -- ROLE INVENTORY AND CLASSIFICATION

Purpose: Establish the complete role set and its taxonomy before any structural
decision is made. Role typing at this gate -- not later -- prevents role
proliferation in downstream sections.

### Step 0a -- Load roles

Scan .roles/ for all role definition files.

  ROLES-LOADED: [role name, role name, ...]

If directory absent or empty:

  ROLES-NOTE: No .roles/ directory found. Using domain-inferred roles:
  [list].

### Step 0b -- Classify roles

Immediately after the roles block, classify every role into exactly one type
from this closed set: {DECISION, EXECUTION, ADVISORY, GOVERNANCE}

  ROLE-TYPE-CLASSIFICATION
    [Role] -> DECISION
    [Role] -> EXECUTION
    [Role] -> ADVISORY
    [Role] -> GOVERNANCE

Order: DECISION first, then EXECUTION, then ADVISORY, then GOVERNANCE.

Type definitions:
  DECISION    -- holds approval or veto authority
  EXECUTION   -- produces deliverables or code
  ADVISORY    -- provides input without authority
  GOVERNANCE  -- owns process or compliance

Example:
  ROLE-TYPE-CLASSIFICATION
    Engineering Manager  -> DECISION
    Product Manager      -> DECISION
    Tech Lead            -> EXECUTION
    Staff Engineer       -> EXECUTION
    Program Manager      -> GOVERNANCE

GATE 0 PASS CRITERIA:
  [ ] ROLES-LOADED or ROLES-NOTE block present
  [ ] ROLE-TYPE-CLASSIFICATION immediately follows -- no intervening content
  [ ] Every declared role has exactly one type assignment
  [ ] All types from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
  [ ] DECISION roles listed before EXECUTION, ADVISORY, GOVERNANCE
  [ ] No role will appear later in the artifact that was not declared here

GATE 0 STATUS: [PASS -- proceed to GATE 1 | FAIL -- correct before continuing]

---

## GATE 1 -- INERTIA ASSESSMENT

Purpose: Determine whether structural overhead is warranted. The default
position is flat operation. This gate's verdict governs every subsequent gate.

Required output -- four elements, produced in order:

### Element 1 -- Default Declaration

  THE TEAM CAN OPERATE FLAT. The burden of proof is on structure.

Open with this statement. Structure must justify its coordination overhead
against the alternative of no structure.

### Element 2 -- Mechanism Table

List existing coordination mechanisms. Minimum 2 rows.

| Mechanism         | Type  | Strength | Replaces                       |
|-------------------|-------|----------|-------------------------------|
| Weekly standup    | SYNC  | STRONG   | Dedicated status committee     |
| Shared task board | TOOL  | MODERATE | Weekly written status report   |

Type from: {EMAIL, SYNC, ASYNC, TOOL, RITUAL, NORM}
Strength from: {STRONG, MODERATE, WEAK}
Replaces: name the specific org element made unnecessary

### Element 3 -- Pressure Rating

  FLAT-CASE-PRESSURE: [FLAT | CASE | PRESSURE]

  FLAT     -- no structural pressure; team operates well without formal org
  CASE     -- gaps exist but not yet critical; reassess in 90 days
  PRESSURE -- clear structural need; org structure is warranted

### Element 4 -- Verdict

  VERDICT: [determination sentence]
  RE-ASSESS WHEN: [specific, measurable trigger]

---

GATE 1 PASS CRITERIA:
  [ ] Default declaration present, verbatim or equivalent
  [ ] Mechanism table >= 2 rows, Types from closed set, Strengths from closed set
  [ ] FLAT-CASE-PRESSURE value from {FLAT, CASE, PRESSURE}
  [ ] Verdict present
  [ ] RE-ASSESS WHEN present and independently verifiable
  [ ] This section precedes any org diagram

GATE 1 STATUS: [PASS -- proceed | FLAT -- terminate | FAIL -- correct]

---

### FLAT-VERDICT OUTCOME

If FLAT-CASE-PRESSURE = FLAT:

  ABSENT: Org Diagram
  ABSENT: Headcount Table
  ABSENT: Operating Rhythm + Charters
  ABSENT: ORG-ELEMENT REGISTER
  ABSENT: Org Evolution Roadmap
  REASON: Flat verdict. Team coordination capacity is sufficient without formal
  structure.
  PROHIBITED: "Simplified hierarchy" and "lightweight org" are prohibited
  substitutes. A team requiring any formal structure must be rated CASE or
  PRESSURE.

ARTIFACT TERMINATION: GATE 1 was the final gate. No further output is produced.

---

## GATE 2 -- ORG DIAGRAM

Purpose: Map the structural hierarchy that the inertia assessment has
justified. Executes only when GATE 1 returns CASE or PRESSURE.

Produce an ASCII org chart. Use only hyphens, pipes, backslashes, plus signs.

  [Domain Name]
  +-- [Area A]
  |   +-- [Role 1] (DECISION)
  |   \-- [Role 2] (EXECUTION)
  +-- [Area B]
  |   \-- [Role 3] (EXECUTION)
  \-- [Committees]
      +-- [Committee X]
      \-- [Committee Y]

Requirements:
- Minimum 2 hierarchy levels
- Committees appear as distinct nodes, not embedded in reporting lines
- All role names must be from GATE 0 ROLES-LOADED

GATE 2 PASS CRITERIA:
  [ ] ASCII org chart present
  [ ] Hierarchy levels >= 2
  [ ] Committees as distinct nodes, not in reporting lines
  [ ] All role names declared in GATE 0

GATE 2 STATUS: [PASS -- proceed to GATE 3 | FAIL -- correct before continuing]

---

## GATE 3 -- HEADCOUNT BY AREA

Purpose: Quantify the structure by area, establishing decision and escalation
ratios.

| Area         | Headcount | Decides | Escalates | Key Roles                                    |
|--------------|-----------|---------|-----------|----------------------------------------------|
| Platform     | 4         | 1       | 3         | Platform Lead (DECISION), 3x SWE (EXECUTION) |
| Total        | 4         | 1       | 3         |                                              |

Column definitions:
  Decides    -- count of DECISION roles per area
  Escalates  -- count of non-DECISION roles routing upward
  Key Roles  -- annotated with (TYPE) from GATE 0 classification

GATE 3 PASS CRITERIA:
  [ ] Minimum 2 area rows
  [ ] Total row present
  [ ] Decides and Escalates as separate columns
  [ ] Key Roles annotated with types from GATE 0 closed set

GATE 3 STATUS: [PASS -- proceed to GATE 4 | FAIL -- correct before continuing]

---

## GATE 4 -- OPERATING RHYTHM + COMMITTEE CHARTERS

Purpose: Define operating cadences and the governance bodies that own them.

INTERLEAVING RULE: This gate executes as a sequence of pairs. Each pair
consists of one rhythm row followed immediately by its committee charter (when
Committee? = YES). Complete each pair before beginning the next.

Pair sequence format:

  [Rhythm row 1]
  [Charter 1 -- if Committee? = YES]

  [Rhythm row 2]
  [Charter 2 -- if Committee? = YES]

  [Rhythm row 3]
  [Charter 3 -- if Committee? = YES]

Batching all rhythm rows together and all charters together is not acceptable.

Required row types (minimum 3, all distinct):
  Row type A -- ROB (Rhythm of Business) cadence
  Row type B -- Shiproom or gate review
  Row type C -- Governance or architecture board

Rhythm row format:

| Cadence                  | Frequency | Owner                       | Forum | Committee? |
|--------------------------|-----------|-----------------------------|-------|-----------|
| Weekly ROB               | Weekly    | Program Manager (GOVERNANCE)| Sync  | NO        |
| Monthly Architecture Rev | Monthly   | Tech Lead (DECISION)        | Board | YES       |
| Quarterly Roadmap Gate   | Quarterly | Product Manager (DECISION)  | Gate  | YES       |

Charter format:

  CHARTER: [Committee Name]
    Mission:    [one sentence]
    Membership: [Role A (TYPE), Role B (TYPE), ...]   <- minimum 2 annotated roles
    Quorum:     [N of M member roles]                 <- fraction form required
    Escalates:  [specific destination role or title]
    Cadence:    [frequency and format]

GATE 4 COUNT VERIFICATION:

After all pairs are produced, execute this count check before closing the gate:

  GATE-4-COUNT:
    Rhythm rows produced:                 [N]
    Rows with Committee? = YES:           [N]
    Charters produced:                    [N]
    Charter count equals YES-row count:   [YES / NO]
    Resolution: [COMPLETE | PRODUCING MISSING CHARTER: (name)]

If the count check returns NO, name the missing charter and produce it. The
gate does not pass until the check resolves to YES.

GATE 4 PASS CRITERIA:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom + governance all present)
  [ ] All Committee? = YES rows have charters
  [ ] Pairs produced in interleaved order
  [ ] All 5 charter fields present for each charter
  [ ] Quorum in "N of M member roles" form
  [ ] Escalates names specific destination (not TBD, not leadership)
  [ ] Membership >= 2 annotated roles per charter
  [ ] GATE-4-COUNT produced and resolves to YES

GATE 4 STATUS: [PASS -- proceed to GATE 5 | FAIL -- correct before continuing]

---

## GATE 5 -- ORG-ELEMENT REGISTER

Purpose: Account for every org element introduced in this artifact and
identify anti-pattern risks.

  ORG-ELEMENT REGISTER
    [Element Name] (cat-N): [one-line purpose]
    ...

  ANTI-PATTERN WATCH
    [Element Name] (cat-N): [risk] -> [mitigation]

Categories -- closed set:
  cat-1: Role
  cat-2: Committee
  cat-3: Cadence or Forum
  cat-4: Governance process

Anti-Pattern Watch entries must reference only elements listed in the Register.

GATE 5 PASS CRITERIA:
  [ ] All roles, committees, cadences, and governance processes registered
  [ ] All elements categorized using cat-1 through cat-4
  [ ] Anti-Pattern Watch section present
  [ ] No Anti-Pattern entry for an element not in the Register

GATE 5 STATUS: [PASS -- proceed to GATE 6 | FAIL -- correct before continuing]

---

## GATE 6 -- ORG EVOLUTION ROADMAP

Purpose: Define conditions under which the current org should evolve.

| Trigger                      | Category      | Current State | Target State     | Action                    |
|------------------------------|---------------|---------------|------------------|---------------------------|
| Headcount exceeds 12 ICs     | HEADCOUNT     | Flat team     | Area leads       | Add two area-lead roles   |
| Second product line launched | PRODUCT-STAGE | Single-domain | Multi-domain     | Add domain-lead layer     |

Requirements:
- Minimum 2 rows
- Each row must use a distinct Category value
- All Categories from the closed set

Trigger categories: {HEADCOUNT, PRODUCT-STAGE, INCIDENT-RATE, VELOCITY-DECLINE,
MARKET-SHIFT, PARTNERSHIP-ADDITION}

GATE 6 PASS CRITERIA:
  [ ] >= 2 rows
  [ ] No two rows share the same Category
  [ ] All Categories from the closed set

GATE 6 STATUS: [PASS -- artifact complete | FAIL -- correct before submitting]

---

## ARTIFACT SUMMARY

Upon completing GATE 6, produce:

  ARTIFACT-SUMMARY:
    Gates executed:              [GATE 0, GATE 1, GATE 2, ...]
    FLAT-VERDICT termination:    [N/A | GATE 1]
    All pass criteria met:       [YES | NO -- if NO: list failing gates]

---

## HARD CONSTRAINTS

- ASCII only. Unicode box-drawing characters are not acceptable.
- Role names must be declared in GATE 0 before appearing anywhere.
- ROLE-TYPE-CLASSIFICATION must immediately follow ROLES-LOADED.
- GATE 1 must precede GATE 2.
- FLAT verdict terminates the artifact after the ABSENT block. Nothing follows.
- Rhythm rows and charters must be produced in interleaved pairs.
- GATE-4-COUNT verification is required before GATE 4 can close.
```

---

## V-05 — Axes: Two-site Constraints + Default Declaration + STOP + Count Check

**Hypothesis:** Anchoring every critical constraint at two independent sites — a structural slot-order rule and a conditional prohibition — closes the bypass paths that single-site enforcement leaves open. Combined with an explicit STOP directive, post-interleave pair-count verification, and a prominent default-position declaration, this variation produces the most constraint-complete artifact. C-16 is the primary axis; C-13, C-18, and C-19 reinforce it.

---

```
# Skill: org-chart

Generate an org structure for a product or domain. Read .roles/ first.
Assess whether structure is warranted. Inertia first.

---

## OPENING POSITION

THE TEAM CAN OPERATE FLAT.

This is not a caveat. This is the default. Formal org structure is overhead. It
slows decisions, adds coordination costs, and must justify itself in improved
outcomes. Every section of this artifact exists to answer one question: does
the evidence justify the overhead? If not, the artifact ends after saying so.
That is a correct and complete outcome.

---

## CONSTRAINT REGISTER

Every critical constraint below is enforced at two independent sites. Site 1 is
the structural slot-order rule. Site 2 is the conditional prohibition. One site
permits silent bypass; two sites close it.

| Constraint              | Site 1 -- slot order                          | Site 2 -- conditional prohibition                                         |
|-------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
| Roles declared before use | ROLES-LOADED block must be first content    | If any role name appears below, it must be in ROLES-LOADED                |
| Role typing before inertia | ROLE-TYPE-CLASSIFICATION must follow ROLES-LOADED, before any other section | If any type annotation appears in the artifact, it must match an entry in ROLE-TYPE-CLASSIFICATION |
| Inertia before diagram  | Inertia Assessment must precede org diagram   | If an org diagram appears, the Inertia Assessment immediately above it must have a CASE or PRESSURE rating |
| FLAT terminates artifact | FLAT verdict triggers ABSENT block + STOP     | If any org structure content appears after the STOP marker, that is a structural error requiring correction |
| Rhythm-charter pairing  | Rhythm rows and charters appear in pair order | If a second rhythm row appears, the first row's charter must have been produced |
| Count parity            | Post-interleave count check required after all pairs | If counts do not match, the missing charter must be produced before the next section begins |

---

## SECTION 1 -- LOAD ROLES

Site 1 (slot order): This block must be the first content produced. No other
content may precede it.

Scan .roles/ for all role definition files. Collect every role name.

  ROLES-LOADED: [role name, role name, ...]

If directory absent:

  ROLES-NOTE: No .roles/ found. Using: [list].

Site 2 (conditional): Every role name that appears anywhere in this artifact
must be declared in this block. A role name that appears below without being
declared here is a structural error.

---

## SECTION 2 -- ROLE TYPE CLASSIFICATION

Site 1 (slot order): This block must appear immediately after ROLES-LOADED,
before any other section.

Classify every declared role into exactly one type from the closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}

  ROLE-TYPE-CLASSIFICATION
    Engineering Manager  -> DECISION
    Product Manager      -> DECISION
    Tech Lead            -> EXECUTION
    Staff Engineer       -> EXECUTION
    Program Manager      -> GOVERNANCE

Order: DECISION first, then EXECUTION, then ADVISORY, then GOVERNANCE.

Type definitions:
  DECISION    -- holds approval or veto authority
  EXECUTION   -- produces deliverables
  ADVISORY    -- provides input without authority
  GOVERNANCE  -- owns process or compliance

Site 2 (conditional): If any role appears with a type annotation elsewhere in
this artifact, that type must match its entry in this block. A conflict between
the annotation and this classification is a structural error.

---

CHECKPOINT 1 -- ROLES AND TYPES: ROLES-LOADED present. ROLE-TYPE-CLASSIFICATION
immediately follows with no intervening content. All roles typed from closed
set. Three-tier order respected. MIN=1 role declared. [PASS before proceeding]

---

## SECTION 3 -- INERTIA ASSESSMENT

Site 1 (slot order): This section must appear before the org diagram. No
diagram, headcount table, rhythm table, or charter may precede it.

Site 2 (conditional): If an org diagram appears in this artifact, the section
immediately above it must contain a FLAT-CASE-PRESSURE rating of CASE or
PRESSURE. An org diagram following a FLAT rating is a structural error.

### 3a. Default Declaration (required)

  THE TEAM CAN OPERATE FLAT. Structure must be justified against this baseline.
  The burden of proof is on structure, not on flatness.

### 3b. Mechanism Table (required -- minimum 2 rows)

| Mechanism           | Type  | Strength | Replaces                       |
|---------------------|-------|----------|-------------------------------|
| Weekly team sync    | SYNC  | STRONG   | Dedicated status committee     |
| Shared task board   | TOOL  | MODERATE | Weekly written status report   |

Type from: {EMAIL, SYNC, ASYNC, TOOL, RITUAL, NORM}
Strength from: {STRONG, MODERATE, WEAK}
Replaces: name a specific org element.

### 3c. Pressure Rating (required)

  FLAT-CASE-PRESSURE: [FLAT | CASE | PRESSURE]

  FLAT     -- no structural pressure; team operates without formal org
  CASE     -- some pressure but not yet critical; reassess in 90 days
  PRESSURE -- clear structural need; org structure is warranted

### 3d. Verdict (required)

  VERDICT: [sentence]
  RE-ASSESS WHEN: [specific, measurable trigger]

---

### FLAT-VERDICT TERMINATION SEQUENCE

If FLAT-CASE-PRESSURE = FLAT, execute exactly this sequence:

  ABSENT: Org Diagram
  ABSENT: Headcount Table
  ABSENT: Operating Rhythm
  ABSENT: Committee Charters
  ABSENT: ORG-ELEMENT REGISTER
  ABSENT: Org Evolution Roadmap
  REASON: Flat verdict. Existing coordination mechanisms are sufficient. No
  structural hierarchy is warranted.
  PROHIBITED: The following are prohibited substitutes and must not be
  produced: "simplified hierarchy," "lightweight structure," "minimal org,"
  "informal structure," "skeleton org." If the team requires any of these, the
  rating must be CASE or PRESSURE, not FLAT.

ARTIFACT END. STOP.

No content may appear after this marker. Producing any org structure, diagram,
table, or charter after the STOP marker is a structural error.

---

CHECKPOINT 2 -- INERTIA COMPLETE: Default declaration present. Mechanism table
MIN=2 rows. Types and Strengths from closed sets. FLAT-CASE-PRESSURE from
closed set. Verdict and RE-ASSESS WHEN present. Section precedes org diagram.
If FLAT: artifact terminated with ABSENT block. [PASS before proceeding]

---

## SECTION 4 -- ORG DIAGRAM

Site 1 (slot order): This section appears after the Inertia Assessment with
CASE or PRESSURE rating.

Site 2 (conditional): If this section appears, the VERDICT from Section 3
immediately above must not be FLAT. An org diagram following a FLAT verdict is
a structural error.

Produce an ASCII org chart:

  [Product Domain]
  +-- [Area A]
  |   +-- [Role 1] (DECISION)
  |   \-- [Role 2] (EXECUTION)
  +-- [Area B]
  |   \-- [Role 3] (EXECUTION)
  \-- [Committees]
      +-- [Committee X]
      \-- [Committee Y]

Requirements:
- Minimum 2 hierarchy levels
- Committees as distinct nodes, not in reporting lines
- Role names from ROLES-LOADED only
- ASCII characters only (no Unicode)

---

CHECKPOINT 3 -- DIAGRAM COMPLETE: ASCII only. Hierarchy levels MIN=2.
Committees as distinct nodes. All roles in ROLES-LOADED. [PASS before
proceeding]

---

## SECTION 5 -- HEADCOUNT BY AREA

| Area         | Headcount | Decides | Escalates | Key Roles                                    |
|--------------|-----------|---------|-----------|----------------------------------------------|
| Platform     | 4         | 1       | 3         | Platform Lead (DECISION), 3x SWE (EXECUTION) |
| Growth       | 3         | 1       | 2         | PM (DECISION), 2x Engineer (EXECUTION)       |
| Total        | 7         | 2       | 5         |                                              |

Requirements:
- Minimum 2 area rows
- Total row at bottom
- Decides: count of DECISION roles per area
- Escalates: count of non-DECISION roles routing upward
- Key Roles: annotated with (TYPE) from Section 2

---

## SECTION 6 -- OPERATING RHYTHM + COMMITTEE CHARTERS

Site 1 (slot order): Rhythm rows and charters appear in interleaved pair order.

Site 2 (conditional): If a second rhythm row appears, the first row's charter
(if Committee? = YES) must have been produced immediately before it. A second
rhythm row following a Committee? = YES row that has no charter is a structural
error.

Batching all rhythm rows together and all charters together is a hard
prohibition. Do not do it.

Minimum 3 distinct rhythm rows: one ROB, one shiproom or gate, one governance
or architecture board.

Rhythm row example:

| Cadence                  | Frequency | Owner                       | Forum | Committee? |
|--------------------------|-----------|-----------------------------|-------|-----------|
| Weekly ROB               | Weekly    | Program Manager (GOVERNANCE)| Sync  | NO        |
| Monthly Arch Review      | Monthly   | Tech Lead (DECISION)        | Board | YES       |
| Quarterly Roadmap Gate   | Quarterly | Product Manager (DECISION)  | Gate  | YES       |

Charter example:

  CHARTER: Monthly Architecture Review
    Mission:    Review and approve technical decisions with cross-team impact.
    Membership: Tech Lead (DECISION), Staff Engineer (EXECUTION), Eng Manager (DECISION)
    Quorum:     2 of 3 member roles
    Escalates:  VP of Engineering
    Cadence:    Monthly, 60-minute structured session

Charter requirements:
- All 5 fields required (Mission, Membership, Quorum, Escalates, Cadence)
- Quorum: "N of M member roles" form -- percentage form is not acceptable
- Escalates: specific role or title -- "TBD" and "leadership" are not acceptable
- Membership: minimum 2 annotated roles with (TYPE)

POST-INTERLEAVE COUNT VERIFICATION:

Site 1 (slot order): This count check must appear after all pairs are produced.

Site 2 (conditional): If the count check returns NO, the missing charter must
be produced before Section 7 begins. Proceeding to Section 7 with a NO count
is a structural error.

  PAIR-COUNT CHECK:
    Total rhythm rows produced:               [N]
    Rows with Committee? = YES:               [N]
    Charters produced:                        [N]
    Committee-row count equals charter count: [YES / NO]
    Resolution: [COMPLETE | PRODUCING MISSING CHARTER: (name)]

---

CHECKPOINT 4 -- RHYTHM-CHARTERS COMPLETE: MIN=3 rhythm rows. ROB, shiproom,
governance all present. All Committee? = YES rows have charters. Pairs in
interleaved order. Count check produced and resolves to YES. All 5 charter
fields present for every charter. Quorum in fraction form. Escalates specific.
[PASS before proceeding]

---

## SECTION 7 -- ORG-ELEMENT REGISTER

Categorize every org element from this artifact:

  ORG-ELEMENT REGISTER
    [Element Name] (cat-N): [purpose]
    ...

  ANTI-PATTERN WATCH
    [Element Name] (cat-N): [risk] -> [mitigation]

Categories: cat-1 (Role), cat-2 (Committee), cat-3 (Cadence/Forum),
cat-4 (Governance process).

Anti-Pattern Watch: only elements listed in the Register may appear here.

---

## SECTION 8 -- ORG EVOLUTION ROADMAP

| Trigger                      | Category      | Current State | Target State     | Action                    |
|------------------------------|---------------|---------------|------------------|---------------------------|
| Headcount exceeds 12 ICs     | HEADCOUNT     | Flat team     | Area leads       | Add two area-lead roles   |
| Second product line added    | PRODUCT-STAGE | Single-domain | Multi-domain     | Add domain-lead layer     |

Minimum 2 rows. No two rows may share the same Category value.

Categories: {HEADCOUNT, PRODUCT-STAGE, INCIDENT-RATE, VELOCITY-DECLINE,
MARKET-SHIFT, PARTNERSHIP-ADDITION}

---

## HARD CONSTRAINTS

All constraints below are enforced at two independent sites as documented in
the CONSTRAINT REGISTER above:

1. ROLES-LOADED must be the first block produced.
2. ROLE-TYPE-CLASSIFICATION must immediately follow ROLES-LOADED.
3. Inertia Assessment must precede the org diagram.
4. FLAT verdict must terminate the artifact. No content after the STOP marker
   is acceptable.
5. Org diagram must have >= 2 hierarchy levels.
6. Headcount table must have >= 2 area rows and a Total row.
7. Rhythm rows and charters must be produced in interleaved pairs.
8. Quorum must be in "N of M member roles" form. Percentage form is not
   acceptable.
9. Escalates must name a specific destination. "TBD" is not acceptable.
10. Post-interleave count check must be produced after all pairs.
11. Missing charters identified by the count check must be produced before the
    next section begins.
```
 the rhythm row's Cadence cell
verbatim. No paraphrase, no abbreviation changes, no reordering of words.

Charter schema:
  ### [Exact copy of Cadence cell]
  Purpose:
  Membership:
    - [role name] ([domain type])    <- annotation REQUIRED
    - [role name] ([domain type])    <- annotation REQUIRED (min two roles)
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

DO NOT emit the CHARTERS COMPLETE gate before BOTH checks below pass.

ANNOTATION-CHECK — REQUIRED BEFORE CHARTERS COMPLETE GATE

  ANNOTATION-CHECK:
  - [role name] — [domain type] — Headcount Key Roles: [present/absent] — Charter Membership: [present/absent]
  (one row per role in ROLES-LOADED / ROLES-NOTE)

  ANNOTATION-GAPS: [list roles missing at either site, or "none"]

  IF ANNOTATION-GAPS is non-empty:
    DO NOT emit the gate. Add missing annotations. Re-run check.
  IF ANNOTATION-GAPS is empty:
    Emit: ANNOTATION-CHECK COMPLETE.

NAME-MATCH VERIFICATION — REQUIRED BEFORE CHARTERS COMPLETE GATE

  NAME-MATCH:
  - Rhythm row: "[Cadence cell]" — Charter header: "### [header]" — Match: [yes/no]
  (one row per governance committee)

  IF any Match is "no":
    DO NOT emit the gate. Rewrite mismatched headers. Re-run check.
  IF all Match is "yes":
    Emit: NAME-MATCH COMPLETE.

Emit: === [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

cat-1 (Areas): [area name] — headcount: [N]
cat-2 (Committees/Cadences): [name]
cat-3 (Headcount): Total headcount: [N]
cat-4 (DRI Roles): [DRI role]

---

ORG EVOLUTION ROADMAP

  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone (different category from Row 1)

---

ANTI-PATTERN WATCH

>= 2 rows. Each "Why It Applies Here": [element name] (cat-N) — [one sentence]
Only cat codes from the ORG-ELEMENT REGISTER.

---

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION (three-tier)
3. === PHASE GATE: ROLES COMPLETE ===
4. Inertia Assessment
5. === PHASE GATE: INERTIA COMPLETE ===
6. ASCII Org Diagram
7. === PHASE GATE: STRUCTURE COMPLETE ===
8. Headcount by Area
9. Operating Rhythm + Charters (INTERLEAVED; NAME-LOCK)
10. ANNOTATION-CHECK
11. NAME-MATCH verification
12. === PHASE GATE: CHARTERS COMPLETE ===
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-05 — Full Integration: R15-V-05 Baseline + C-18 + C-19 + C-20

**axis:** combined — R15-V-05 foundation (default-position + table schemas + count-and-advance + ABSENT labeling + two-site constraints + interleaving) + annotation-propagation-verification (C-18) + charter-rhythm-name-identity (C-19) + escalates-destination-format (C-20)
**hypothesis:** R15-V-05 handles C-01 through C-17. Adding ANNOTATION-CHECK (C-18), NAME-LOCK + NAME-MATCH (C-19), and Escalates routing-arrow format with two-site enforcement (C-20) closes the remaining R15 ceiling gaps without disrupting the proven foundation. Each new constraint is structurally independent of the others and of the existing phase gates, so composition risk is low. The combined prompt should achieve v3 composite coverage. Falsifiable: if any single Round 4 criterion still fails in V-05, the failure isolates to that criterion's constraint text, not to interaction effects.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer — it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
displacing. Do not draw an org box until you have argued the case for staying flat
and identified the specific failure mode it cannot answer.

---

PHASE 1: LOAD AND CLASSIFY ROLES

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] — [one-line description from role file]

If no files found:
  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] — [description]

Every role name appearing anywhere in this document must be declared here.

Immediately produce ROLE-TYPE-CLASSIFICATION in three-tier order:
  Tier 1 (Engineering) — complete before writing Tier 2
  Tier 2 (Operations) — complete before writing Tier 3
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] — [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other

Emit: === [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===

---

PHASE 2: INERTIA ASSESSMENT — FOUR SUB-SECTIONS

Write before any org diagram. You are the advocate for staying flat.

Sub-section 1 — Case for Staying Flat

Fill this schema with the team's actual coordination mechanisms:

  | Mechanism Name                     | Type              | Frequency / Participants       |
  |------------------------------------|-------------------|--------------------------------|
  | (e.g., #signal-eng Slack channel)  | Channel           | (e.g., Continuous, 14 people) |
  | (e.g., Monday standup)             | Recurring Cadence | (e.g., Weekly, 8 leads)       |

Type: Channel / Informal Role / Recurring Cadence / Shared Artifact (no other values)

MECHANISM-ROW-COUNT: [N] rows.
IF N < 2: add missing rows until N >= 2. Re-emit count.
When count >= 2, emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today
Describe coordination patterns in practice. Do not repeat Sub-section 1 entries.

Sub-section 3 — Rebuttal
The ONE failure mode the Sub-section 1 mechanisms cannot resolve.
Name an observable: blocked decision, missed SLA, time-zone gap, knowledge silo,
or competing roadmap. "The team is growing" alone is not acceptable.

Sub-section 4 — VERDICT

FLAT-CASE-PRESSURE — TWO ENFORCEMENT SITES:
  SITE 1 (slot): The first sentence of this sub-section is the FLAT-CASE-PRESSURE line.
  SITE 2 (conditional): DO NOT write CAN-OPERATE-FLAT or STRUCTURE-WARRANTED before
  the FLAT-CASE-PRESSURE line is present above it.

  FLAT-CASE-PRESSURE: [rating] — [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

RE-ASSESSMENT TRIGGER — TWO ENFORCEMENT SITES:
  SITE 1 (slot): Trigger appears immediately after the verdict, before any other text.
  SITE 2 (conditional): DO NOT emit the INERTIA COMPLETE gate before a concrete,
  measurable trigger is present. "Revisit as the team grows" is not concrete.

---

FLAT-VERDICT BRANCH — ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:

  DO NOT silently skip structural sections.
  DO NOT produce a "simplified hierarchy" or "compact org" as an alternative.
  A simplified hierarchy IS NOT a valid substitute for an ABSENT section.

  Label each structural section explicitly:

    ### ASCII Org Diagram — ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy is not warranted.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org chart" are
    structural proposals requiring STRUCTURE-WARRANTED.
    Remaining ABSENT: Headcount by Area, Operating Rhythm, Committee Charters,
    ORG-ELEMENT REGISTER, Org Evolution Roadmap, Anti-Pattern Watch.

  End the artifact with: `Generated by: /org-chart {topic} — {date}`

IF VERDICT = STRUCTURE-WARRANTED: emit the gate and continue.

Emit: === [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===

---

PHASE 3: ASCII ORG DIAGRAM

Draw after the gate:

  [Top-Level Lead]
        |
  ------+----------+----------
  |               |          |
  [Area A]     [Area B]   [Committee X]

Rules:
  - Two hierarchy levels minimum
  - Committees as distinct nodes — not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only

Emit: === [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===

---

PHASE 4: HEADCOUNT BY AREA

Fill this schema (Decides and Escalates are ALWAYS separate columns):

  | Area     | Headcount | Key Roles                  | Decides          | Escalates                           |
  |----------|-----------|----------------------------|------------------|-------------------------------------|
  | (area 1) | N         | [role] (Engineering)       | (decision types) | [decision type] -> [Role or Forum]  |
  | (area 2) | N         | [role] (PM)                | (decision types) | [decision type] -> [Role or Forum]  |
  | **Total**| N         |                            |                  |                                     |

DO NOT use a "Decision Scope" column.
Annotate Key Roles: [role name] ([domain type]).
Two area rows minimum plus Total row.

ESCALATES FORMAT — TWO ENFORCEMENT SITES (Headcount):
  SITE 1 (field definition): Escalates cells use `[decision type] -> [Role Title or Forum Name]`
  SITE 2 (conditional): DO NOT proceed past the Headcount table if any Escalates cell
  lacks the `->` routing arrow or uses vague scope ("senior leadership", "executive team").
  Rewrite to `[decision type] -> [named destination]` before advancing.

HEADCOUNT-SUM: [area counts] = Total.

---

PHASE 5: OPERATING RHYTHM AND COMMITTEE CHARTERS — INTERLEAVED

INTERLEAVING RULE: Write each rhythm row, then its charter (if governance), before
writing the next rhythm row. DO NOT batch all rows before charters.

NAME-LOCK RULE: The `###` charter header MUST reproduce the rhythm row's Cadence cell
verbatim. No paraphrase, no abbreviation change, no word reorder.

  CORRECT:   Cadence cell: "Architecture Review Board" → Charter: ### Architecture Review Board
  INCORRECT: Cadence cell: "Architecture Review Board" → Charter: ### Architecture Board

Schema for rhythm rows:
  | Cadence | Frequency | DRI / Owner | Purpose |

Schema for charters (immediately after their rhythm row):
  ### [Exact copy of Cadence cell — verbatim]
  Purpose:     [what this committee governs]
  Membership:
    - [role name] ([domain type])     <- annotation REQUIRED
    - [role name] ([domain type])     <- annotation REQUIRED (minimum two roles)
  Decides:     [decision types owned here]
  Escalates:   [decision type] -> [Role Title or Forum Name]
  Quorum:      [N] of [M] member roles required for binding decisions

ESCALATES FORMAT — TWO ENFORCEMENT SITES (Charters):
  SITE 1 (field definition): Charter Escalates field uses `[decision type] -> [destination]`
  SITE 2 (conditional): DO NOT emit the CHARTERS COMPLETE gate if any charter's Escalates:
    - lacks the `->` routing arrow
    - writes "everything not listed under Decides"
    - names only a vague tier without a specific role title or named forum
  Rewrite any non-conforming entry before emitting the gate.

QUORUM FRACTION — TWO ENFORCEMENT SITES:
  SITE 1 (field): Full fraction format required: `[N] of [M] member roles required for binding decisions`
  SITE 2 (conditional): DO NOT emit the CHARTERS COMPLETE gate if any charter uses the
  short form "N roles required." Rewrite first.

CADENCE-ROW-COUNT: [N] rows. >= 3 required (ROB + gate + >= 1 committee).

DO NOT emit the CHARTERS COMPLETE gate before ALL THREE checks below pass.

ANNOTATION-CHECK

  ANNOTATION-CHECK:
  - [role name] — [domain type] — Headcount Key Roles: [present/absent] — Charter Membership: [present/absent]
  (one row per role in ROLES-LOADED / ROLES-NOTE)

  ANNOTATION-GAPS: [list any role missing at either site, or "none"]

  IF ANNOTATION-GAPS non-empty: add missing annotations; re-run.
  IF empty: Emit: ANNOTATION-CHECK COMPLETE — all roles annotated at both sites.

NAME-MATCH VERIFICATION

  NAME-MATCH:
  - Rhythm row: "[Cadence cell]" — Charter header: "### [header]" — Match: [yes/no]
  (one row per governance committee)

  IF any "no": rewrite mismatched header; re-run.
  IF all "yes": Emit: NAME-MATCH COMPLETE.

ESCALATES-FORMAT VERIFICATION

  ESCALATES-FORMAT:
  - Headcount Escalates cells — all use `->` format: [yes/no, list any failing cells]
  - Charter Escalates fields — all use `->` format: [yes/no, list any failing fields]

  IF any "no": rewrite failing cells/fields; re-run.
  IF all "yes": Emit: ESCALATES-FORMAT COMPLETE.

Emit: === [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===

---

PHASE 6: REGISTER

  ORG-ELEMENT REGISTER:
  cat-1 (Areas):
    - [area name] — headcount: [N]
  cat-2 (Committees/Cadences):
    - [name]
  cat-3 (Headcount):
    - Total headcount: [N]
  cat-4 (DRI Roles):
    - [DRI role from Operating Rhythm]

---

PHASE 6 (continued): ORG EVOLUTION ROADMAP

  | Trigger                   | Structural Change | Type                           |
  |---------------------------|-------------------|--------------------------------|
  | Row 1: headcount threshold| ...               | Headcount                      |
  | Row 2: different category | ...               | Workload / Symptom / Milestone |

Two rows from DISTINCT trigger categories. Two headcount rows do not qualify.

---

PHASE 6 (continued): ANTI-PATTERN WATCH

  | Anti-Pattern | Why It Applies Here                                            | Mitigation |
  |--------------|----------------------------------------------------------------|------------|
  | (name)       | [element name] (cat-N) — [one sentence of specific relevance]  | ...        |

Minimum two rows. Each "Why It Applies Here" opens with typed citation [element name] (cat-N).
Only cat codes from ORG-ELEMENT REGISTER.

---

SECTION ORDER (enforced by phase gates):

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-TYPE-CLASSIFICATION (three-tier)
3.  === PHASE GATE: ROLES COMPLETE ===
4.  Inertia Assessment:
    Sub-section 1 (mechanism table + MECHANISM-ROW-COUNT + FLAT-CASE-CLOSED separator)
    Sub-section 2 (How We Coordinate Today)
    Sub-section 3 (Rebuttal)
    Sub-section 4 (FLAT-CASE-PRESSURE [two sites] + verdict + re-assessment trigger [two sites])
5.  === PHASE GATE: INERTIA COMPLETE ===
    [IF CAN-OPERATE-FLAT: emit ABSENT labels for all structural sections, then end]
6.  ASCII Org Diagram
7.  === PHASE GATE: STRUCTURE COMPLETE ===
8.  Headcount by Area (HEADCOUNT-SUM; Escalates routing format [two sites])
9.  Operating Rhythm + Charters (INTERLEAVED; NAME-LOCK; Escalates routing [two sites];
    Quorum fraction [two sites])
10. ANNOTATION-CHECK (blocks gate if any role missing at either site)
11. NAME-MATCH verification (blocks gate if any name diverges from Cadence cell)
12. ESCALATES-FORMAT verification (blocks gate if any cell/field lacks `->`)
13. === PHASE GATE: CHARTERS COMPLETE ===
14. ORG-ELEMENT REGISTER
15. Org Evolution Roadmap
16. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## Summary

| V | Axis | New Criterion | Key Mechanism | Blocks at |
|---|------|---------------|---------------|-----------|
| V-01 | annotation-propagation-verification | C-18 | ANNOTATION-CHECK with present/absent count per role per site | CHARTERS COMPLETE gate |
| V-02 | charter-rhythm-name-identity | C-19 | NAME-LOCK (verbatim copy rule) + NAME-MATCH verification | CHARTERS COMPLETE gate |
| V-03 | escalates-destination-format | C-20 | `->` routing arrow, two-site enforcement in Headcount + Charters | Headcount advance + CHARTERS COMPLETE gate |
| V-04 | C-18 + C-19 | C-18, C-19 | ANNOTATION-CHECK + NAME-LOCK composed; tests interaction | CHARTERS COMPLETE gate |
| V-05 | Full integration | C-18, C-19, C-20 | R15-V-05 baseline + all three Round 4 constraints + three verification steps | Multiple gates |
