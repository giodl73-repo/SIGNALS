---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R7
rubric_version: v7-C25C26
status: variate
---

# org-chart Variate -- Round 7 (Rubric v7 / C-25 + C-26 cycle)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v7 (C-01 through C-26; C-25/C-26 new this round)
**Round:** R7 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R6 ceiling under v7:**
V-05/R6 achieves strong coverage of C-01 through C-24. Two gaps remain in all R6 variations:

1. **Named artifact handoff gap (C-25):** All R6 variations include a GATE CHAIN CONTRACT that
   asserts "each gate's outputs are required inputs for GATE N+1." V-01/R6 goes further with an
   inline summary table naming artifacts per gate. But no variation declares PRODUCES at the
   gate boundary itself, and no downstream gate opens with a REQUIRES block naming the specific
   artifact from the prior gate. The handoff is described in surrounding prose; a model satisfying
   the chain contract knows gates sequence but must infer artifact identity. C-25 requires the
   handoff to be named at each gate boundary individually -- GATE N PRODUCES: [artifact name],
   GATE N+1 REQUIRES: [that same artifact name] -- making per-gate I/O self-documenting
   independently of any chain-level declaration.

2. **All-gate prohibited-content gap (C-26):** All R6 variations apply an explicit CONTAINMENT
   CONTRACT at GATE 0 (required by C-24): an enumerated list of content categories prohibited
   from appearing within GATE 0's boundary before STATUS is emitted. GATE 1, GATE 2, and GATE 3
   carry no analogous contract. They are guarded by verification loops and checkpoint criteria but
   no variation states "these content categories must not appear within this gate's boundary before
   STATUS is emitted" for GATE 1 through GATE 3. A model satisfies C-24 for GATE 0 while
   producing rhythm rows mid-inertia or charter fields mid-diagram without violating any stated
   downstream gate contract. C-26 closes this by requiring each structural gate to carry an
   explicit prohibited-content list, analogous to the GATE 0 containment pattern.

**R7 target:** Close both v7 gaps. Single-axis variations test each in isolation plus a phrasing
register diagnostic. V-04/V-05 combine.

**Single axes chosen:**
- Lifecycle emphasis: per-gate artifact I/O declarations (C-25 target)
- Output format: all-gate prohibited-content contracts as enumerated lists (C-26 target)
- Phrasing register: systematic DO / DO NOT modal language (C-14 diagnostic, no C-25/C-26)

---

## Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis -- per-gate PRODUCES/REQUIRES (C-25) | Adding PRODUCES declarations at each gate's pass condition and REQUIRES blocks at each gate's opening, using exact artifact names, closes the artifact-identity gap that chain-level "outputs are required inputs" leaves open; a model knows what to produce and what to consume at each boundary without inference from surrounding prose; no C-26 containment contracts beyond GATE 0 |
| V-02 | Output format -- all-gate CONTAINMENT CONTRACTs (C-26) | Adding an explicit CONTAINMENT CONTRACT to GATE 1, GATE 2, and GATE 3 -- each enumerating by category the structural content that must not appear within the gate before STATUS -- closes the downstream gate permeability that GATE 0's C-24 contract leaves unaddressed; artifact I/O remains chain-level only (C-25 gap remains) |
| V-03 | Phrasing register -- DO/DO NOT modal register throughout | Replacing all prose compliance rules with DO / DO NOT entries using "must" / "not acceptable" language tests whether strong modal language (C-14) moves the score without the structural additions that C-25 and C-26 require; serves as a diagnostic: phrasing register alone cannot satisfy C-25 or C-26 |
| V-04 | Combined: lifecycle emphasis + output format (C-25 + C-26) | Per-gate PRODUCES/REQUIRES declarations combined with CONTAINMENT CONTRACTs at all four gates satisfies both new criteria; the two additions share no bypass surface -- PRODUCES/REQUIRES governs what crosses gate boundaries, CONTAINMENT CONTRACTs govern what must not appear within a gate before STATUS |
| V-05 | Combined: C-25 + C-26 + DO/DO NOT register (full integration) | Layering both structural additions onto V-05/R6's full integration baseline with the DO/DO NOT modal register achieves maximum coverage of C-14, C-21, C-22, C-24, C-25, C-26 in one variation; builds on default-position (C-13), ABSENT-label STOP (C-15, C-18), two-site enforcement (C-16), interleaved pairs + pair-count (C-17, C-19), role-classification gate (C-20), checkbox gates (C-21), blocking verification (C-22), positional naming (C-23), atomic GATE 0 (C-24) |

---

## V-01 -- Per-Gate PRODUCES/REQUIRES Declarations (C-25)

**axis:** lifecycle-emphasis -- named artifact I/O at each gate interface
**hypothesis:** V-01/R6 carries a GATE CHAIN CONTRACT table that labels each gate's artifact
(e.g., "typed role list required by GATE 1") but those labels live in the chain preamble, not
at the gate boundary itself. GATE 0's STATUS block does not declare "GATE 0 PRODUCES: typed role
list." GATE 1 does not open with "REQUIRES: typed role list (produced by GATE 0)." A model
executing V-01/R6 can trace the chain by reading the preamble table but is not forced to name
the artifact at the interface. V-01/R7 pins PRODUCES at each gate's STATUS block and REQUIRES
at each gate's header, using identical artifact names, making the handoff self-documenting at the
boundary. Chain-level contract is kept; no prohibited-content contracts beyond GATE 0 (C-26 gap
remains for scoring isolation).

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Structure must be justified by a specific failure mode that informal coordination cannot resolve.
Do not draw an org box until you have argued the case for staying flat.

---

GATE CHAIN CONTRACT

Four gates in strictly ascending numeric order. Each gate declares the specific artifact it
produces. The immediately following gate's REQUIRES block must name that exact artifact by name.
A gate must not open until all artifacts in its REQUIRES block are confirmed present.

  GATE 0: Roles and Classification  -> A0: typed role list
  GATE 1: Inertia Assessment        -> A1: inertia verdict (or artifact terminates)
  GATE 2: Structure and Headcount   -> A2: org diagram + headcount
  GATE 3: Charters Complete         -> A3: operating rhythm + charters

Emitting a gate before its predecessor passes is not acceptable.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

REQUIRES: none (opening gate)

GATE 0 CONTAINMENT CONTRACT: The ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block are
the only permitted content under GATE 0. No inertia rows, no org diagram nodes, no headcount
entries, no rhythm rows, and no charter fields may appear between these two blocks or between
ROLE-TYPE-CLASSIFICATION and the GATE 0 STATUS line. Structural content between these two
operations is not acceptable.

GATE 0 does not pass and does not yield A0 until both operations complete with no structural
interleaving.

Step 0a -- Load Roles

Glob `.craft/roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name used anywhere in this artifact must be declared here.
DO NOT write structural content between ROLES-LOADED and Step 0b.

Step 0b -- Classify Roles

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order:
  Tier 1 (DECISION) -- complete before Tier 2
  Tier 2 (EXECUTION) -- complete before Tier 3
  Tier 3 (ADVISORY / GOVERNANCE)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [type]

Type from closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE

GATE 0 PASS:
  [ ] ROLES-LOADED or ROLES-NOTE present
  [ ] ROLE-TYPE-CLASSIFICATION immediately follows; no structural content between
  [ ] All roles typed from closed set
  [ ] Three-tier order respected
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 0 PRODUCES:
  A0 -- typed role list: ROLES-LOADED (or ROLES-NOTE) + ROLE-TYPE-CLASSIFICATION block

GATE 1 must not begin before GATE 0 PASS is present.

---

GATE 1: INERTIA ASSESSMENT

REQUIRES: A0 -- typed role list (produced by GATE 0)

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count rows. If count < 2, add rows before continuing.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not captured in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode that flat coordination cannot resolve.

Sub-section 4 -- VERDICT

Two-site FLAT-CASE-PRESSURE enforcement:
  SITE 1 (slot): First sentence of VERDICT must be FLAT-CASE-PRESSURE.
  SITE 2 (conditional): Writing verdict declaration before FLAT-CASE-PRESSURE is in the output
  is not acceptable.

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

Two-site re-assessment trigger:
  SITE 1 (slot): Trigger immediately follows verdict declaration.
  SITE 2 (conditional): Emitting GATE 1 PASS before a concrete trigger is present is not
  acceptable.

---

FLAT-VERDICT BRANCH

IF VERDICT = CAN-OPERATE-FLAT:

  Silently skipping structural sections is not acceptable.
  Producing "simplified hierarchy" or "compact org" is not acceptable.

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org" require STRUCTURE-WARRANTED.
    Remaining ABSENT: Headcount, Operating Rhythm, Committee Charters, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

  STOP. Artifact complete. No content may follow.
  Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: proceed to GATE 1 PASS.

GATE 1 PASS:
  [ ] All four sub-sections present in order
  [ ] Mechanism table >= 2 rows; Type from closed set
  [ ] FLAT-CASE-PRESSURE precedes verdict declaration
  [ ] VERDICT is CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger has concrete measurable threshold
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 1 PRODUCES:
  A1 -- inertia verdict: VERDICT value (STRUCTURE-WARRANTED) + FLAT-CASE-PRESSURE rating

GATE 2 must not begin before GATE 1 PASS is present.

---

GATE 2: STRUCTURE AND HEADCOUNT

REQUIRES: A1 -- inertia verdict (produced by GATE 1); opens only when VERDICT = STRUCTURE-WARRANTED

ASCII Org Diagram:
  - Minimum two hierarchy levels required
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only
  - Annotate each node with its type from ROLE-TYPE-CLASSIFICATION

Headcount by Area:
  | Area | Headcount | Key Roles | Decides | Escalates |
Decides and Escalates must be separate columns. Key Roles annotated as [role name] ([type]).
Minimum two area rows plus Total.

GATE 2 PASS:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes
  [ ] All role names from ROLES-LOADED or ROLES-NOTE; each node typed
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 2 PRODUCES:
  A2 -- org diagram + headcount: ASCII diagram with typed nodes + headcount table

GATE 3 must not begin before GATE 2 PASS is present.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

REQUIRES: A2 -- org diagram + headcount (produced by GATE 2)

INTERLEAVING RULE: Write each rhythm row then its charter (if governance) before the next row.
Writing all rhythm rows first and all charters second is not acceptable.

Rhythm schema: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining rows is not acceptable.

Charter schema (five required fields, immediately after its governance rhythm row):
  Purpose:
  Membership:  [role name] ([type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum uses full fraction form.
  SITE 2 (conditional): Emitting GATE 3 PASS before all charters have full-fraction Quorum
  is not acceptable.

Production sequence: ROB row, shiproom row, governance rows (each immediately followed by charter).

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before GATE 3 PASS.

GATE 3 PASS:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

GATE 3 PRODUCES:
  A3 -- operating rhythm + charters: rhythm table + all committee charters (complete org-chart artifact)

---

ORG-ELEMENT REGISTER

  cat-1 (Areas): [area] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

ORG EVOLUTION ROADMAP -- two rows from distinct trigger categories.
ANTI-PATTERN WATCH -- minimum two rows; each "Why" opens with [element] (cat-N).
Using cat-N codes not in the ORG-ELEMENT REGISTER is not acceptable.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02 -- All-Gate Prohibited-Content Contracts (C-26)

**axis:** output-format -- CONTAINMENT CONTRACTs at GATE 1, GATE 2, GATE 3
**hypothesis:** C-24 requires an explicit CONTAINMENT CONTRACT at GATE 0 listing the content
categories that must not appear within the gate boundary before STATUS is emitted. All R6
variations satisfy this for GATE 0 only. GATE 1, GATE 2, and GATE 3 are guarded by verification
loops and checkpoint criteria but carry no analogous enumerated prohibition. A model producing
rhythm rows mid-inertia assessment violates no stated contract in GATE 1 under R6. V-02 adds a
CONTAINMENT CONTRACT to each structural gate, naming by category the content that cannot appear
within the gate before STATUS. Chain-level artifact declarations remain summary-level only (no
per-gate PRODUCES/REQUIRES), keeping this a single-axis test for C-26.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Structure must be justified by a specific failure mode that informal coordination cannot resolve.
Do not draw an org box until you have argued the case for staying flat.

---

GATE CHAIN CONTRACT

Four gates in strictly ascending numeric order. Each gate's outputs are required inputs for
GATE N+1. Emitting a gate before its predecessor passes is not acceptable.

  GATE 0: Roles and Classification  -> typed role list required by GATE 1
  GATE 1: Inertia Assessment        -> VERDICT required by GATE 2 (or artifact terminates)
  GATE 2: Structure and Headcount   -> org diagram + headcount required by GATE 3
  GATE 3: Charters Complete         -> operating rhythm + committee charters

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

GATE 0 CONTAINMENT CONTRACT: The ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block are
the only permitted content under GATE 0. The following content categories must not appear within
GATE 0's boundary before GATE 0 STATUS is emitted:
  (1) inertia assessment rows or mechanism-table entries
  (2) org diagram nodes or ASCII hierarchy boxes
  (3) headcount table entries
  (4) operating rhythm rows
  (5) committee charter fields

GATE 0 does not pass and does not yield a typed role list until both operations complete with no
structural interleaving.

Step 0a -- Load Roles

Glob `.craft/roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name used anywhere in this artifact must be declared here.
DO NOT write structural content between ROLES-LOADED and Step 0b.

Step 0b -- Classify Roles

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order:
  Tier 1 (DECISION) -- complete before Tier 2
  Tier 2 (EXECUTION) -- complete before Tier 3
  Tier 3 (ADVISORY / GOVERNANCE)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [type]

Type from closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE

GATE 0 PASS:
  [ ] ROLES-LOADED or ROLES-NOTE present
  [ ] ROLE-TYPE-CLASSIFICATION immediately follows; no structural content between
  [ ] All roles typed from closed set
  [ ] Three-tier order respected
  [ ] Containment contract satisfied: none of the 5 prohibited categories appeared in this gate
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 1 must not begin before GATE 0 PASS is present.

---

GATE 1: INERTIA ASSESSMENT

GATE 1 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 1's
boundary before GATE 1 STATUS is emitted:
  (1) org diagram nodes or ASCII hierarchy boxes
  (2) headcount table entries
  (3) operating rhythm rows
  (4) committee charter fields
  (5) any structural element that presupposes a VERDICT value not yet emitted in this gate

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count rows. If count < 2, add rows before continuing.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not captured in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode that flat coordination cannot resolve.

Sub-section 4 -- VERDICT

Two-site FLAT-CASE-PRESSURE enforcement:
  SITE 1 (slot): First sentence of VERDICT must be FLAT-CASE-PRESSURE.
  SITE 2 (conditional): Writing verdict declaration before FLAT-CASE-PRESSURE is in the output
  is not acceptable.

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

Two-site re-assessment trigger:
  SITE 1 (slot): Trigger immediately follows verdict declaration.
  SITE 2 (conditional): Emitting GATE 1 PASS before a concrete trigger is present is not
  acceptable.

---

FLAT-VERDICT BRANCH

IF VERDICT = CAN-OPERATE-FLAT:

  Silently skipping structural sections is not acceptable.
  Producing "simplified hierarchy" or "compact org" is not acceptable.

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org" require STRUCTURE-WARRANTED.
    Remaining ABSENT: Headcount, Operating Rhythm, Committee Charters, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

  STOP. Artifact complete. No content may follow.
  Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: proceed to GATE 1 PASS.

GATE 1 PASS:
  [ ] All four sub-sections present in order
  [ ] Mechanism table >= 2 rows; Type from closed set
  [ ] FLAT-CASE-PRESSURE precedes verdict declaration
  [ ] VERDICT is CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger has concrete measurable threshold
  [ ] Containment contract satisfied: no diagram, headcount, rhythm, or charter content appeared
      before VERDICT in this gate
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 2 must not begin before GATE 1 PASS is present.

---

GATE 2: STRUCTURE AND HEADCOUNT

GATE 2 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 2's
boundary before GATE 2 STATUS is emitted:
  (1) operating rhythm rows
  (2) committee charter fields
  (3) inertia mechanism rows or FLAT-CASE-PRESSURE assertions (these belong in GATE 1 only)
  (4) any content that requires GATE 3 outputs as a prerequisite

ASCII Org Diagram:
  - Minimum two hierarchy levels required
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only
  - Annotate each node with its type from ROLE-TYPE-CLASSIFICATION

Headcount by Area:
  | Area | Headcount | Key Roles | Decides | Escalates |
Decides and Escalates must be separate columns. Key Roles annotated as [role name] ([type]).
Minimum two area rows plus Total.

GATE 2 PASS:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes
  [ ] All role names from ROLES-LOADED or ROLES-NOTE; each node typed
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns
  [ ] Containment contract satisfied: no rhythm rows, charter fields, or inertia content
      appeared in this gate
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 3 must not begin before GATE 2 PASS is present.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

GATE 3 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 3's
boundary before GATE 3 STATUS is emitted:
  (1) new role declarations not present in the ROLES-LOADED or ROLES-NOTE block from GATE 0
  (2) inertia mechanism rows or FLAT-CASE-PRESSURE assertions outside GATE 1
  (3) org diagram revisions or new hierarchy nodes outside the GATE 2 scope

INTERLEAVING RULE: Write each rhythm row then its charter (if governance) before the next row.
Writing all rhythm rows first and all charters second is not acceptable.

Rhythm schema: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining rows is not acceptable.

Charter schema (five required fields, immediately after its governance rhythm row):
  Purpose:
  Membership:  [role name] ([type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum uses full fraction form.
  SITE 2 (conditional): Emitting GATE 3 PASS before all charters have full-fraction Quorum
  is not acceptable.

Production sequence: ROB row, shiproom row, governance rows (each immediately followed by charter).

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before GATE 3 PASS.

GATE 3 PASS:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS
  [ ] Containment contract satisfied: no rogue role declarations, inertia rows, or diagram
      revisions appeared in this gate
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

  cat-1 (Areas): [area] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

ORG EVOLUTION ROADMAP -- two rows from distinct trigger categories.
ANTI-PATTERN WATCH -- minimum two rows; each "Why" opens with [element] (cat-N).
Using cat-N codes not in the ORG-ELEMENT REGISTER is not acceptable.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-03 -- Systematic DO/DO NOT Modal Register (C-14 diagnostic)

**axis:** phrasing-register -- DO / DO NOT throughout, strong modal language
**hypothesis:** All R6 variations use a mix of prose compliance rules ("Writing X is not
acceptable") and conditional prohibitions. V-03 replaces every compliance rule with an explicit
DO or DO NOT entry using "must" / "required" / "not acceptable" language. No C-25 or C-26
structural additions are made: the gate chain contract remains chain-level only, and GATE 1/2/3
carry no explicit containment contracts. This is a diagnostic for C-14 in isolation: does a
systematic DO/DO NOT modal register improve the score without the per-gate I/O declarations
or prohibited-content contracts that C-25 and C-26 structurally require?

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is the proposal, not the answer. Informal coordination is the status quo
you are trying to displace. You must not draw an org box until you have argued the case for
staying flat. Structure must be justified. The burden of proof lies with the structured org.

---

GATE CHAIN CONTRACT

You must execute exactly four gates in strictly ascending numeric order: GATE 0, GATE 1, GATE 2,
GATE 3. Each gate's outputs are required inputs for GATE N+1. Emitting a gate before its
predecessor passes is not acceptable.

  GATE 0: Roles and Classification  -> typed role list required by GATE 1
  GATE 1: Inertia Assessment        -> VERDICT required by GATE 2 (or terminates)
  GATE 2: Structure and Headcount   -> org diagram + headcount required by GATE 3
  GATE 3: Charters Complete         -> operating rhythm + charters

GATE PASS PROTOCOL (applies to all four gates):
  Step A: Complete all production steps for this gate
  Step B: Run the blocking verification loop (scan all required elements; produce any missing)
  Step C: Tick all [ ] pass criteria checkboxes individually
  Step D: Emit STATUS: PASS only after steps A-C complete
  Emitting a STATUS line before the verification loop closes is not acceptable.
  Asserting "all conditions met" without individually ticking checkboxes is not acceptable.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

GATE 0 CONTAINMENT CONTRACT: ROLES-LOADED and ROLE-TYPE-CLASSIFICATION are the only content
permitted under GATE 0. Structural content between these two operations is not acceptable.

GATE 0 does not pass and does not yield a typed role list until both operations complete with no
structural interleaving.

Step 0a -- Load Roles

DO:
  - Glob `.craft/roles/` and produce ROLES-LOADED listing every role name found
  - If .craft/roles/ is absent or empty, produce ROLES-NOTE declaring inferred roles are used

DO NOT:
  - Introduce any role name later in the artifact that is absent from ROLES-LOADED or ROLES-NOTE
  - Write structural content between ROLES-LOADED and Step 0b

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

Step 0b -- Classify Roles

DO:
  - Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE
  - Type every role from the closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE
  - Order: DECISION roles first, EXECUTION second, ADVISORY and GOVERNANCE third

DO NOT:
  - Use a type value outside the closed set
  - Place any structural content between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [type]

GATE 0 VERIFICATION (blocking -- required before STATUS):
  Scan from ROLES-LOADED through ROLE-TYPE-CLASSIFICATION. Confirm:
  - ROLES-LOADED or ROLES-NOTE present with >= 1 role entry
  - ROLE-TYPE-CLASSIFICATION present immediately after, no structural content between
  - All roles classified with a closed-set type; three-tier order respected
  If any check fails, produce missing content and re-verify before advancing.

GATE 0 PASS CRITERIA:
  [ ] ROLES-LOADED or ROLES-NOTE present
  [ ] ROLE-TYPE-CLASSIFICATION immediately follows; no structural content between
  [ ] All roles typed from closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE
  [ ] Three-tier order: DECISION -> EXECUTION -> ADVISORY/GOVERNANCE
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 1 must not begin before GATE 0 PASS is present.

---

GATE 1: INERTIA ASSESSMENT

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

DO:
  - Open with an explicit statement that the team can operate flat and structure must be justified;
    this statement must precede the mechanism table
  - Produce a mechanism evidence table: | Mechanism Name | Type | Frequency / Participants |
  - Type each mechanism from: Channel / Informal Role / Recurring Cadence / Shared Artifact
  - Count rows; if count < 2, add rows before emitting FLAT-CASE-CLOSED

DO NOT:
  - Begin the mechanism table before the default-position statement
  - Use a Type value outside the closed set

Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not captured in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode that flat coordination cannot resolve.

Sub-section 4 -- VERDICT

DO:
  - Make FLAT-CASE-PRESSURE the first sentence of this sub-section
  - Follow immediately with CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  - Follow verdict immediately with a concrete, observable re-assessment trigger

DO NOT:
  - Write the verdict declaration before FLAT-CASE-PRESSURE is present in the output
  - Emit GATE 1 PASS before a concrete re-assessment trigger is present

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

  CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  Re-assessment trigger: [specific, observable threshold]

---

FLAT-VERDICT BRANCH

IF VERDICT = CAN-OPERATE-FLAT:

  DO NOT silently skip structural sections.
  DO NOT produce "simplified hierarchy" or "compact org."

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org" require STRUCTURE-WARRANTED.
    Remaining ABSENT: Headcount, Operating Rhythm, Committee Charters, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

  STOP. Artifact complete. No content may follow.
  Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: run GATE 1 verification and emit GATE 1 PASS.

GATE 1 VERIFICATION (blocking):
  Confirm all four sub-sections present. Confirm mechanism table >= 2 rows, Type from closed set.
  Confirm FLAT-CASE-PRESSURE precedes verdict. Confirm VERDICT is exactly CAN-OPERATE-FLAT or
  STRUCTURE-WARRANTED. Confirm re-assessment trigger has concrete threshold. If any check fails,
  produce missing element and re-verify before proceeding.

GATE 1 PASS CRITERIA:
  [ ] All four sub-sections present in order
  [ ] Mechanism table >= 2 rows; Type from closed set
  [ ] FLAT-CASE-PRESSURE line precedes verdict declaration
  [ ] VERDICT is CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger present with concrete measurable threshold
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 2 must not begin before GATE 1 PASS is present.

---

GATE 2: STRUCTURE AND HEADCOUNT

DO:
  - Produce an ASCII org diagram with >= 2 hierarchy levels
  - Represent committees as distinct nodes separate from their parent area boxes
  - Use only role names from ROLES-LOADED or ROLES-NOTE; annotate each node with its type
  - Produce a headcount table: Area | Headcount | Key Roles | Decides | Escalates
  - Include >= 2 area rows plus a Total row
  - Annotate Key Roles as [role name] ([type])
  - Keep Decides and Escalates as separate columns

DO NOT:
  - Introduce role names absent from ROLES-LOADED or ROLES-NOTE
  - Merge committee nodes into parent boxes
  - Merge Decides and Escalates into a single column
  - Produce rhythm rows or charter fields before GATE 2 PASS

GATE 2 VERIFICATION (blocking):
  Confirm diagram >= 2 levels, committees distinct, role names from ROLES-LOADED.
  Confirm headcount >= 2 areas + Total, Decides and Escalates separate, Key Roles annotated.
  If any check fails, produce missing element and re-verify.

GATE 2 PASS CRITERIA:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes (not embedded in area boxes)
  [ ] All role names from ROLES-LOADED or ROLES-NOTE; each node has type annotation
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 3 must not begin before GATE 2 PASS is present.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

DO:
  - Write each rhythm row then its charter (if governance) before the next row
  - Include >= 3 distinct rhythm rows: one ROB, one shiproom/gate, one governance
  - Include all five charter fields: Purpose, Membership, Decides, Escalates, Quorum
  - Express Quorum as "[N] of [M] member roles required for binding decisions"
  - Annotate Membership with type; include >= 2 roles; name a destination in Escalates
  - After all pairs emit GOVERNANCE-ROWS and CHARTERS-WRITTEN counts

DO NOT:
  - Write all rhythm rows before any charters
  - Use Quorum formats other than the full [N] of [M] fraction form
  - Leave Escalates without a named destination
  - Emit GATE 3 PASS before CHARTERS-WRITTEN equals GOVERNANCE-ROWS

Rhythm schema: | Cadence | Frequency | DRI / Owner | Purpose |
Charter schema (five required fields, immediately after its governance rhythm row):
  Purpose:
  Membership:  [role name] ([type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum uses full fraction form.
  SITE 2 (conditional): Emitting GATE 3 PASS before all charters have full-fraction Quorum
  is not acceptable.

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before GATE 3 PASS.

GATE 3 VERIFICATION (blocking):
  Confirm >= 3 rhythm rows. Confirm every governance row has charter immediately below it.
  Confirm every charter has all five fields. Confirm every Quorum is full-fraction.
  Confirm CHARTERS-WRITTEN = GOVERNANCE-ROWS. If any check fails, produce missing content and
  re-verify.

GATE 3 PASS CRITERIA:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form; no short form present
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

DO:
  - Emit all four categories (cat-1 through cat-4)
  - Cite only cat-N codes present in this register in Anti-Pattern Watch

DO NOT:
  - Use cat-N codes in Anti-Pattern Watch absent from this register

  cat-1 (Areas): [area] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

ORG EVOLUTION ROADMAP -- two rows from distinct trigger categories.
ANTI-PATTERN WATCH -- minimum two rows; each "Why" opens with [element] (cat-N).

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04 -- Combined: Named Artifact I/O (C-25) + All-Gate CONTAINMENT CONTRACTs (C-26)

**axis:** combined -- lifecycle-emphasis (C-25) + output-format (C-26)
**hypothesis:** V-01/R7 adds per-gate PRODUCES/REQUIRES (C-25) without downstream containment
contracts. V-02/R7 adds all-gate CONTAINMENT CONTRACTs (C-26) without per-gate artifact naming.
The two additions have no bypass surface in common: PRODUCES/REQUIRES governs what artifacts
cross gate boundaries; CONTAINMENT CONTRACTs govern what structural content must not appear
within a gate before STATUS. A model satisfying C-25 without C-26 can name its handoffs correctly
while still producing out-of-order structural content within a downstream gate. A model satisfying
C-26 without C-25 can bound its gates correctly while leaving artifact identity as inference from
surrounding prose. V-04 closes both simultaneously.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Structure must be justified by a specific failure mode that informal coordination cannot resolve.
Do not draw an org box until you have argued the case for staying flat.

---

GATE CHAIN CONTRACT

Four gates in strictly ascending numeric order. Each gate declares the specific artifact it
produces. The immediately following gate's REQUIRES block must name that exact artifact by name.
A gate must not open until all artifacts in its REQUIRES block are confirmed present. Emitting
a gate before its predecessor passes is not acceptable.

  GATE 0: Roles and Classification  -> A0: typed role list (required by GATE 1)
  GATE 1: Inertia Assessment        -> A1: inertia verdict (required by GATE 2; or terminates)
  GATE 2: Structure and Headcount   -> A2: org diagram + headcount (required by GATE 3)
  GATE 3: Charters Complete         -> A3: operating rhythm + charters

GATE PASS PROTOCOL (applies to all four gates):
  Step A: Complete all production steps for this gate
  Step B: Run the blocking verification loop (scan all required elements; produce any missing)
  Step C: Tick all [ ] pass criteria checkboxes individually
  Step D: Emit STATUS: PASS only after steps A-C complete
  Emitting a STATUS line before the verification loop closes is not acceptable.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

REQUIRES: none (opening gate)

GATE 0 CONTAINMENT CONTRACT: The ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block are
the only permitted content under GATE 0. The following content categories must not appear within
GATE 0's boundary before GATE 0 STATUS is emitted:
  (1) inertia assessment rows or mechanism-table entries
  (2) org diagram nodes or ASCII hierarchy boxes
  (3) headcount table entries
  (4) operating rhythm rows
  (5) committee charter fields

GATE 0 does not pass and does not yield A0 until both operations complete with no structural
interleaving.

Step 0a -- Load Roles

Glob `.craft/roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this artifact must be declared here.
DO NOT write structural content between ROLES-LOADED and Step 0b.

Step 0b -- Classify Roles

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order:
  Tier 1 (DECISION) -- complete before Tier 2
  Tier 2 (EXECUTION) -- complete before Tier 3
  Tier 3 (ADVISORY / GOVERNANCE)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [type]

Type from closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE

GATE 0 VERIFICATION (blocking):
  Confirm ROLES-LOADED or ROLES-NOTE present. Confirm ROLE-TYPE-CLASSIFICATION follows with no
  structural content between. Confirm all roles typed from closed set. Confirm three-tier order.
  Confirm all 5 prohibited content categories absent. Re-verify if any check fails.

GATE 0 PASS CRITERIA:
  [ ] ROLES-LOADED or ROLES-NOTE present
  [ ] ROLE-TYPE-CLASSIFICATION immediately follows; no structural content between
  [ ] All roles typed from closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE
  [ ] Three-tier order: DECISION -> EXECUTION -> ADVISORY/GOVERNANCE
  [ ] Containment contract satisfied: all 5 prohibited categories absent from this gate
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 0 PRODUCES:
  A0 -- typed role list: ROLES-LOADED (or ROLES-NOTE) + ROLE-TYPE-CLASSIFICATION block

GATE 1 must not begin before GATE 0 PASS is present and A0 is confirmed.

---

GATE 1: INERTIA ASSESSMENT

REQUIRES: A0 -- typed role list (produced by GATE 0)

GATE 1 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 1's
boundary before GATE 1 STATUS is emitted:
  (1) org diagram nodes or ASCII hierarchy boxes
  (2) headcount table entries
  (3) operating rhythm rows
  (4) committee charter fields
  (5) any structural conclusion that presupposes a VERDICT value not yet emitted in this gate

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count rows. If count < 2, add rows before continuing.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded] ---

Sub-section 2 -- How We Coordinate Today
Sub-section 3 -- Rebuttal (one specific observable failure mode)
Sub-section 4 -- VERDICT

Two-site FLAT-CASE-PRESSURE enforcement:
  SITE 1 (slot): First sentence of VERDICT must be FLAT-CASE-PRESSURE.
  SITE 2 (conditional): Writing verdict declaration before FLAT-CASE-PRESSURE is in the output
  is not acceptable.

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

  CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

Two-site re-assessment trigger:
  SITE 1 (slot): Trigger immediately follows verdict declaration.
  SITE 2 (conditional): Emitting GATE 1 PASS before a concrete trigger is present is not
  acceptable.

---

FLAT-VERDICT BRANCH

IF VERDICT = CAN-OPERATE-FLAT:

  Silently skipping structural sections is not acceptable.
  "Simplified hierarchy" or "compact org" is not acceptable.

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org" require STRUCTURE-WARRANTED.
    Remaining ABSENT: Headcount, Operating Rhythm, Committee Charters, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

  STOP. Artifact complete. No content may follow.
  Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: proceed to GATE 1 verification.

GATE 1 VERIFICATION (blocking):
  Confirm all four sub-sections present. Confirm mechanism table >= 2 rows, Type from closed set.
  Confirm FLAT-CASE-PRESSURE precedes verdict. Confirm VERDICT is exactly CAN-OPERATE-FLAT or
  STRUCTURE-WARRANTED. Confirm re-assessment trigger has concrete threshold. Confirm containment
  contract satisfied: categories (1)-(5) absent from this gate. Re-verify if any check fails.

GATE 1 PASS CRITERIA:
  [ ] All four sub-sections present in order
  [ ] Mechanism table >= 2 rows; Type from closed set
  [ ] FLAT-CASE-PRESSURE line precedes verdict declaration
  [ ] VERDICT is CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger present with concrete measurable threshold
  [ ] Containment contract satisfied: no diagram, headcount, rhythm, or charter content
      appeared before VERDICT; no structural conclusion presupposed an unemitted VERDICT
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 1 PRODUCES:
  A1 -- inertia verdict: VERDICT value (STRUCTURE-WARRANTED) + FLAT-CASE-PRESSURE rating

GATE 2 must not begin before GATE 1 PASS is present and A1 is confirmed.

---

GATE 2: STRUCTURE AND HEADCOUNT

REQUIRES: A1 -- inertia verdict (produced by GATE 1); opens only when VERDICT = STRUCTURE-WARRANTED

GATE 2 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 2's
boundary before GATE 2 STATUS is emitted:
  (1) operating rhythm rows
  (2) committee charter fields
  (3) inertia mechanism rows or FLAT-CASE-PRESSURE assertions (these belong in A1 / GATE 1 only)
  (4) any content that requires GATE 3 outputs as a prerequisite

ASCII Org Diagram:
  - Minimum two hierarchy levels required
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only
  - Annotate each node with its type from ROLE-TYPE-CLASSIFICATION

Headcount by Area:
  | Area | Headcount | Key Roles | Decides | Escalates |
Decides and Escalates must be separate columns. Key Roles annotated as [role name] ([type]).
Minimum two area rows plus Total.

GATE 2 VERIFICATION (blocking):
  Confirm org diagram >= 2 levels, committees distinct, role names from A0. Confirm headcount
  >= 2 areas + Total, Decides and Escalates separate, Key Roles annotated. Confirm containment
  contract satisfied: categories (1)-(4) absent from this gate. Re-verify if any check fails.

GATE 2 PASS CRITERIA:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes
  [ ] All role names from A0 (ROLES-LOADED / ROLES-NOTE); each node has type annotation
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns
  [ ] Containment contract satisfied: no rhythm rows, charter fields, inertia rows, or GATE 3
      content appeared in this gate
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 2 PRODUCES:
  A2 -- org diagram + headcount: ASCII diagram with typed nodes + headcount table

GATE 3 must not begin before GATE 2 PASS is present and A2 is confirmed.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

REQUIRES: A2 -- org diagram + headcount (produced by GATE 2)

GATE 3 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 3's
boundary before GATE 3 STATUS is emitted:
  (1) new role declarations not present in A0 (all roles must trace to ROLES-LOADED / ROLES-NOTE)
  (2) inertia mechanism rows or FLAT-CASE-PRESSURE assertions (these belong to A1 / GATE 1 only)
  (3) org diagram revisions or new hierarchy nodes outside A2 scope

INTERLEAVING RULE: Write each rhythm row then its charter (if governance) before the next row.
Writing all rhythm rows first and all charters second is not acceptable.

Rhythm schema: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining rows is not acceptable.

Charter schema (five required fields, immediately after its governance rhythm row):
  Purpose:
  Membership:  [role name] ([type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum uses full fraction form.
  SITE 2 (conditional): Emitting GATE 3 PASS before all charters have full-fraction Quorum
  is not acceptable.

Production sequence: ROB row, shiproom row, governance rows (each immediately followed by charter).

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before GATE 3 PASS.

GATE 3 VERIFICATION (blocking):
  Confirm >= 3 rhythm rows. Confirm every governance row has a charter immediately below it.
  Confirm every charter has all five fields. Confirm every Quorum is full-fraction form.
  Confirm CHARTERS-WRITTEN = GOVERNANCE-ROWS. Confirm containment contract satisfied:
  categories (1)-(3) absent. Re-verify if any check fails.

GATE 3 PASS CRITERIA:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form; no short form present
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS
  [ ] Containment contract satisfied: no rogue role declarations, inertia rows, or diagram
      revisions appeared in this gate
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

GATE 3 PRODUCES:
  A3 -- operating rhythm + charters: rhythm table + all committee charters (complete org-chart artifact)

---

ORG-ELEMENT REGISTER

  cat-1 (Areas): [area] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

ORG EVOLUTION ROADMAP -- two rows from distinct trigger categories.
ANTI-PATTERN WATCH -- minimum two rows; each "Why" opens with [element] (cat-N).
Using cat-N codes not in the ORG-ELEMENT REGISTER is not acceptable.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-05 -- Full Integration: V-05/R6 Baseline + C-25 + C-26 + DO/DO NOT Register

**axis:** combined -- V-05/R6 (C-01 through C-24) + lifecycle-emphasis (C-25) + output-format
(C-26) + phrasing-register (C-14)
**hypothesis:** V-05/R6 establishes the complete foundation: default-position declaration (C-13),
ABSENT-labeling + explicit STOP (C-15, C-18), two-site constraint enforcement (C-16), interleaved
rhythm-charter production + pair-count (C-17, C-19), role-classification prerequisite gate (C-20),
checkbox-format pass criteria (C-21), blocking verification loops (C-22), positional gate index
naming (C-23), and atomic GATE 0 containment (C-24). V-05/R7 adds: (a) per-gate PRODUCES/REQUIRES
declarations at every gate boundary (C-25); (b) CONTAINMENT CONTRACTs at GATE 1/2/3 (C-26); (c)
systematic DO/DO NOT modal register replacing all prose compliance rules (C-14). The three
additions compose cleanly: C-25 governs artifact identity at boundaries, C-26 governs structural
content within gates, the modal register governs compliance language throughout.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is the proposal, not the answer. Informal coordination (channels, standups,
de-facto leads, shared documents) is the status quo you are trying to displace. You must not draw
an org box until you have argued the case for staying flat and found the specific failure mode it
cannot answer. Structure must be justified. The burden of proof lies with the structured org.

---

GATE CHAIN CONTRACT

You must execute exactly four gates in strictly ascending numeric order: GATE 0, GATE 1, GATE 2,
GATE 3. Each gate declares the specific artifact it produces. The immediately following gate's
REQUIRES block must name that exact artifact. A gate must not open until all artifacts in its
REQUIRES block are confirmed present. Emitting a gate before its predecessor passes is not
acceptable.

  GATE 0: Roles and Classification  -> A0: typed role list (required by GATE 1)
  GATE 1: Inertia Assessment        -> A1: inertia verdict (required by GATE 2; or terminates)
  GATE 2: Structure and Headcount   -> A2: org diagram + headcount (required by GATE 3)
  GATE 3: Charters Complete         -> A3: operating rhythm + charters

GATE PASS PROTOCOL (applies to all four gates):
  Step A: Complete all production steps for this gate
  Step B: Run the blocking verification loop (scan all required elements; produce any missing)
  Step C: Tick all [ ] pass criteria checkboxes individually
  Step D: Emit STATUS: PASS only after steps A-C complete
  Emitting a STATUS line before the verification loop closes is not acceptable.
  Asserting "all conditions met" without individually ticking checkboxes is not acceptable.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT -- NO STRUCTURAL CONTENT BETWEEN STEPS)

REQUIRES: none (opening gate)

GATE 0 CONTAINMENT CONTRACT: ROLES-LOADED and ROLE-TYPE-CLASSIFICATION are the only content
permitted under GATE 0. The following content categories must not appear within GATE 0's boundary
before GATE 0 STATUS is emitted:
  (1) inertia assessment rows or mechanism-table entries
  (2) org diagram nodes or ASCII hierarchy boxes
  (3) headcount table entries
  (4) operating rhythm rows
  (5) committee charter fields

GATE 0 does not pass and does not yield A0 until:
  (a) ROLES-LOADED or ROLES-NOTE is complete, AND
  (b) ROLE-TYPE-CLASSIFICATION is complete, AND
  (c) no structural content appears between (a) and (b).

Placing structural content between (a) and (b) at any step is not acceptable. This applies at
the step level: a step that produces an inertia row or diagram node between ROLES-LOADED and
ROLE-TYPE-CLASSIFICATION violates this contract even if the final output appears adjacent.

Step 0a -- Load Roles

DO:
  - Glob `.craft/roles/` and produce ROLES-LOADED listing every role name found with one-line
    description from the role file
  - If .craft/roles/ is absent or empty, produce ROLES-NOTE declaring inferred roles are used

DO NOT:
  - Introduce any role name in a later section that is absent from ROLES-LOADED or ROLES-NOTE
  - Write any content between ROLES-LOADED and Step 0b except ROLE-TYPE-CLASSIFICATION

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

Step 0b -- Classify Roles (immediately follows Step 0a with no intervening structural content)

DO:
  - Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE
  - Type every role from the closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE
  - Order: DECISION roles first, EXECUTION second, ADVISORY and GOVERNANCE third

DO NOT:
  - Use a type value outside the closed set
  - Place any inertia, diagram, headcount, rhythm, or charter content between ROLES-LOADED and
    ROLE-TYPE-CLASSIFICATION

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [type] -- [one-sentence rationale]

GATE 0 VERIFICATION (blocking -- required before STATUS):
  Scan from ROLES-LOADED through ROLE-TYPE-CLASSIFICATION. Confirm:
  - ROLES-LOADED or ROLES-NOTE present with >= 1 role entry
  - ROLE-TYPE-CLASSIFICATION present immediately after, no structural content between
  - All roles classified with a closed-set type
  - Three-tier order: DECISION -> EXECUTION -> ADVISORY/GOVERNANCE
  - All 5 prohibited content categories absent from this gate
  If any check fails, produce missing content and re-verify before advancing.

GATE 0 PASS CRITERIA:
  [ ] ROLES-LOADED or ROLES-NOTE present
  [ ] ROLE-TYPE-CLASSIFICATION immediately follows; no structural content between
  [ ] All roles typed from closed set: DECISION / EXECUTION / ADVISORY / GOVERNANCE
  [ ] Three-tier order: DECISION -> EXECUTION -> ADVISORY/GOVERNANCE
  [ ] Containment contract: all 5 prohibited categories absent from this gate
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 0 PRODUCES:
  A0 -- typed role list: ROLES-LOADED (or ROLES-NOTE) + ROLE-TYPE-CLASSIFICATION block

GATE 1 must not begin before GATE 0 PASS is present and A0 is confirmed.

---

GATE 1: INERTIA ASSESSMENT

REQUIRES: A0 -- typed role list (produced by GATE 0)

GATE 1 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 1's
boundary before GATE 1 STATUS is emitted:
  (1) org diagram nodes or ASCII hierarchy boxes
  (2) headcount table entries
  (3) operating rhythm rows
  (4) committee charter fields
  (5) any structural conclusion that presupposes a VERDICT value not yet emitted in this gate

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

DO:
  - Open with an explicit statement that the team can operate flat and structure must be justified;
    this statement must precede the mechanism table
  - Produce a mechanism evidence table with columns: Mechanism Name | Type | Frequency / Participants
  - Type each mechanism from: Channel / Informal Role / Recurring Cadence / Shared Artifact
  - Count rows; if count < 2, add rows before emitting FLAT-CASE-CLOSED

DO NOT:
  - Begin the mechanism table before the default-position statement
  - Use a Type value outside the closed set
  - Advance past FLAT-CASE-CLOSED until row count >= 2

Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not captured in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode that flat coordination cannot resolve.

Sub-section 4 -- VERDICT

DO:
  - Make FLAT-CASE-PRESSURE the first sentence of this sub-section
  - Follow immediately with CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  - Follow verdict immediately with a concrete, observable re-assessment trigger

DO NOT:
  - Write the verdict declaration before FLAT-CASE-PRESSURE is present in the output
  - Emit GATE 1 PASS before a concrete re-assessment trigger is present

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

  CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  Re-assessment trigger: [specific, observable threshold]

---

FLAT-VERDICT BRANCH

IF VERDICT = CAN-OPERATE-FLAT:

  DO NOT silently skip structural sections.
  DO NOT produce "simplified hierarchy" or "compact org."

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org" require STRUCTURE-WARRANTED.
    Remaining ABSENT: Headcount, Operating Rhythm, Committee Charters, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

  STOP. Artifact complete. No content may follow.
  Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: proceed to GATE 1 verification.

GATE 1 VERIFICATION (blocking -- required before STATUS):
  Confirm all four sub-sections present in order. Confirm mechanism table >= 2 rows, Type from
  closed set. Confirm FLAT-CASE-PRESSURE precedes verdict. Confirm VERDICT is CAN-OPERATE-FLAT
  or STRUCTURE-WARRANTED. Confirm re-assessment trigger has concrete threshold. Confirm
  containment contract: categories (1)-(5) absent from this gate. If any check fails, produce
  missing element and re-verify before proceeding.

GATE 1 PASS CRITERIA:
  [ ] All four sub-sections present in order
  [ ] Mechanism table >= 2 rows; Type from closed set
  [ ] FLAT-CASE-PRESSURE line precedes verdict declaration
  [ ] VERDICT is CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger present with concrete measurable threshold
  [ ] Containment contract: no diagram, headcount, rhythm, or charter content appeared before
      VERDICT; no structural conclusion presupposed an unemitted VERDICT
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 1 PRODUCES:
  A1 -- inertia verdict: VERDICT value (STRUCTURE-WARRANTED) + FLAT-CASE-PRESSURE rating

GATE 2 must not begin before GATE 1 PASS is present and A1 is confirmed.

---

GATE 2: STRUCTURE AND HEADCOUNT

REQUIRES: A1 -- inertia verdict (produced by GATE 1); must not open unless VERDICT = STRUCTURE-WARRANTED

GATE 2 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 2's
boundary before GATE 2 STATUS is emitted:
  (1) operating rhythm rows
  (2) committee charter fields
  (3) inertia mechanism rows or FLAT-CASE-PRESSURE assertions (these belong to A1 / GATE 1 only)
  (4) any content requiring GATE 3 outputs as a prerequisite

ASCII Org Diagram:

DO:
  - Produce an ASCII diagram with >= 2 hierarchy levels
  - Represent committees as distinct nodes separate from their parent area boxes
  - Use only role names from A0 (ROLES-LOADED / ROLES-NOTE)
  - Annotate each node with its type from ROLE-TYPE-CLASSIFICATION

DO NOT:
  - Introduce role names absent from A0
  - Merge committee nodes into parent area boxes
  - Produce rhythm rows, charter fields, or headcount entries before GATE 2 STATUS
  - Open this gate unless GATE 1 STATUS = PASS and VERDICT = STRUCTURE-WARRANTED

Headcount by Area:

DO:
  - Produce a table with columns: Area | Headcount | Key Roles | Decides | Escalates
  - Include >= 2 area rows plus a Total row
  - Annotate Key Roles as [role name] ([type])
  - Keep Decides and Escalates as separate columns

DO NOT:
  - Merge Decides and Escalates into a single column ("Decision Scope" is not acceptable)
  - Omit the Total row

GATE 2 VERIFICATION (blocking -- required before STATUS):
  Confirm diagram >= 2 levels, committees distinct, role names from A0, each node typed.
  Confirm headcount >= 2 areas + Total, Decides and Escalates separate, Key Roles annotated.
  Confirm containment contract: categories (1)-(4) absent from this gate. Re-verify if any
  check fails.

GATE 2 PASS CRITERIA:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes (not embedded in area boxes)
  [ ] All role names from A0; each node has type annotation
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns; Key Roles annotated with type
  [ ] Containment contract: no rhythm rows, charter fields, inertia rows, or GATE 3 content
      appeared in this gate
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 2 PRODUCES:
  A2 -- org diagram + headcount: ASCII diagram with typed nodes + headcount table

GATE 3 must not begin before GATE 2 PASS is present and A2 is confirmed.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

REQUIRES: A2 -- org diagram + headcount (produced by GATE 2)

GATE 3 CONTAINMENT CONTRACT: The following content categories must not appear within GATE 3's
boundary before GATE 3 STATUS is emitted:
  (1) new role declarations not present in A0 (all roles must trace to ROLES-LOADED / ROLES-NOTE)
  (2) inertia mechanism rows or FLAT-CASE-PRESSURE assertions (these belong to A1 / GATE 1 only)
  (3) org diagram revisions or new hierarchy nodes outside the scope of A2

INTERLEAVING RULE:

DO:
  - Write each rhythm row then its charter (if governance) before writing the next row

DO NOT:
  - Write all rhythm rows first and all charters second (this is not acceptable)

Rhythm schema: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining rows is not acceptable.

Charter schema (five required fields, immediately after its governance rhythm row):

DO:
  - Produce all five fields for every charter: Purpose, Membership, Decides, Escalates, Quorum
  - Annotate Membership roles with type; include >= 2 roles
  - Express Quorum as "[N] of [M] member roles required for binding decisions"
  - Name a specific destination in Escalates (a role or forum name is required)

DO NOT:
  - Omit any of the five required fields
  - Use Quorum formats other than the full [N] of [M] fraction form
  - Leave Escalates without a named destination
  - Emit GATE 3 PASS before CHARTERS-WRITTEN equals GOVERNANCE-ROWS

  Purpose:
  Membership:  [role name] ([type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum uses full fraction form.
  SITE 2 (conditional): Emitting GATE 3 PASS before all charters have full-fraction Quorum
  is not acceptable.

Production sequence: ROB row, shiproom row, governance rows (each immediately followed by charter).

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before GATE 3 PASS.

GATE 3 VERIFICATION (blocking -- required before STATUS):
  Confirm >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance). Confirm every
  governance row has a charter immediately below it. Confirm every charter has all five fields.
  Confirm every Quorum is full-fraction form. Confirm CHARTERS-WRITTEN = GOVERNANCE-ROWS.
  Confirm containment contract: categories (1)-(3) absent. Re-verify if any check fails.

GATE 3 PASS CRITERIA:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form; no short form present
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS
  [ ] Containment contract: no rogue role declarations, inertia rows, or diagram revisions
      appeared in this gate
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

GATE 3 PRODUCES:
  A3 -- operating rhythm + charters: rhythm table + all committee charters (complete org-chart artifact)

---

ORG-ELEMENT REGISTER

DO:
  - Emit all four categories (cat-1 through cat-4)
  - Cite only cat-N codes present in this register when writing Anti-Pattern Watch

DO NOT:
  - Use cat-N codes in Anti-Pattern Watch that are absent from this register

  cat-1 (Areas): [area] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

ORG EVOLUTION ROADMAP

DO:
  - Produce >= 2 rows from distinct trigger categories (no two headcount-threshold rows)
  - Format: | Trigger | Structural Change | Type |

ANTI-PATTERN WATCH

DO:
  - Produce >= 2 rows; format: | Anti-Pattern | Why It Applies Here | Mitigation |
  - Open each "Why" with: [element name] (cat-N) -- [one sentence]

DO NOT:
  - Use cat-N codes not registered in the ORG-ELEMENT REGISTER above

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```
