---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R6
rubric_version: v6
status: variate
---

# org-chart Variate -- Round 6 (Rubric v6 / C-23 + C-24 cycle)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v6 (C-01 through C-24; C-23/C-24 new from v6)
**Round:** R6 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R5 ceiling under v6:**
V-05/R5 achieves strong coverage of C-01 through C-22. Two gaps remain in all R5 variations:

1. **Positional gate index gap (C-23):** All R5 variations use named-only phase gates
   (`=== [PHASE GATE: ROLES COMPLETE] ===`, `=== [PHASE GATE: INERTIA COMPLETE] ===`).
   Named gates require reading surrounding prose to establish sequence order. No variation names
   its gates GATE 0, GATE 1, GATE 2, GATE 3 such that the numeric index alone encodes position.
   C-07 ("4 phase gate lines in correct sequence") is satisfiable with named gates listed in
   order; C-23 is not satisfied by named-only gates because names alone do not encode position --
   a model can invoke "INERTIA COMPLETE" before "ROLES COMPLETE" without violating any label
   constraint. GATE N labels make that impossible: GATE 2 before GATE 1 is a visibly malformed
   sequence provable from the labels themselves without reading surrounding prose.

2. **Atomic GATE 0 containment gap (C-24):** All R5 variations satisfy C-08 ("ROLE-TYPE-
   CLASSIFICATION immediately after roles") via text adjacency, and C-20 ("classification gate
   as prerequisite") via phase gate sequencing. But adjacency is a text-placement rule: a model
   can place classification text next to the roles block while still executing structural steps
   (inertia rows, diagram nodes) between them at the gate level. C-24 requires that ROLES-LOADED
   and ROLE-TYPE-CLASSIFICATION appear under a single GATE 0 header with no intervening structural
   content permitted at any step. The gate boundary, not text adjacency, enforces co-location.
   C-08 and C-20 are satisfiable without C-24; C-24 is satisfiable only by a variation that also
   satisfies C-08 and C-20.

**R6 target:** Close both v6 gaps. V-01/V-02 are single-axis. V-03 addresses both C-23 + C-24
together. V-04/V-05 are combined.

---

## Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Positional gate index naming (C-23) | Renaming phase gates GATE 0/1/2/3 and adding the chain statement "each gate's outputs are required inputs for GATE N+1" makes gate sequence self-enforcing from label alone; a model that emits GATE 2 before GATE 1 produces a visibly malformed label sequence without prose analysis |
| V-02 | Atomic GATE 0 containment (C-24) | Placing ROLES-LOADED and ROLE-TYPE-CLASSIFICATION under a single GATE 0 header with an explicit structural prohibition against content between them at the step level closes the adjacency bypass where classification is adjacent in output but gates permit structural interleaving |
| V-03 | C-23 + C-24 combined | GATE 0-3 positional naming plus atomic GATE 0 containment satisfy both criteria simultaneously; C-24 requires a GATE 0 container, C-23 requires that container carry a positional index -- the two compose naturally and share no bypass surface |
| V-04 | C-23 + C-24 + checkbox gates (C-21 + C-22) | Adding checkbox-format pass criteria and blocking verification steps to the GATE 0-3 structure closes the remaining bypass: a model must individually tick each condition before STATUS can read PASS, and a mandatory verification loop must close before any gate emission |
| V-05 | Full integration: R5-V05 baseline + C-23 + C-24 | Layering positional gate indexing and atomic GATE 0 containment onto the proven R5 foundation (default-position declaration, ABSENT-labeling + STOP, two-site constraints, interleaved production + pair-count, role-classification prerequisite, checkbox gates, blocking verification) achieves the v6 composite target |

---

## V-01 -- Positional Gate Index Naming (C-23)

**axis:** gate-index-naming
**hypothesis:** All prior-round phase gates use named-only labels. Named gates require a reader
to consult surrounding prose to establish sequence order. GATE 0 / GATE 1 / GATE 2 / GATE 3
encode position intrinsically: given any two gate names, their relative order is unambiguous
without reading anything else. The explicit chain statement ("GATE N outputs are required inputs
for GATE N+1") makes the dependency chain self-documenting. A model that emits GATE 3 before
GATE 2 produces a label sequence that fails C-23's requirement with no prose analysis required.
All other elements are unchanged from the R5 baseline; this is a single-axis test.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure must be justified by a specific failure mode that informal coordination
cannot resolve. Do not draw an org box until you have argued the case for staying flat.

---

GATE CHAIN CONTRACT

This skill executes as a 4-gate chain. Each gate's outputs are required inputs for the subsequent
gate. Gates must be emitted in strictly ascending numeric order: GATE 0, GATE 1, GATE 2, GATE 3.
Emitting a gate before its predecessor passes is not acceptable.

  GATE 0: Roles and Classification  -> typed role list required by GATE 1
  GATE 1: Inertia Assessment        -> VERDICT required by GATE 2 (or artifact terminates)
  GATE 2: Structure and Headcount   -> org diagram + headcount required by GATE 3
  GATE 3: Charters Complete         -> operating rhythm + committee charters

---

GATE 0: ROLES AND CLASSIFICATION

Step 0a -- Load Roles

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this artifact must be declared here. Introducing a role
name later that was not declared here is not acceptable.

Step 0b -- Classify Roles

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order
required: Tier 1 (Engineering) complete before Tier 2 (Operations); Tier 2 complete before
Tier 3 (PM / Design / Research / Other).

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type from closed set: Engineering / PM / Design / Operations / Research / Other.
Classifying a role with an unlisted type is not acceptable.

GATE 0 STATUS: When ROLES-LOADED (or ROLES-NOTE) and ROLE-TYPE-CLASSIFICATION are both complete,
emit exactly:
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

Do not proceed to GATE 1 until this line is present in the output.

---

GATE 1: INERTIA ASSESSMENT

Write before any org diagram. Four sub-sections in order.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |

Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count after writing. If count < 2, add rows before continuing.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not already in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode the mechanisms cannot resolve.

Sub-section 4 -- VERDICT

First sentence must be FLAT-CASE-PRESSURE line. Writing the verdict declaration before this
line is present in the output is not acceptable.

  FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + named failure mode]
  Rating from closed set: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

Then: re-assessment trigger with concrete measurable threshold.
Emitting the GATE 1 pass line before a concrete trigger is present is not acceptable.

---

FLAT-VERDICT BRANCH

IF VERDICT = CAN-OPERATE-FLAT:

  Silently skipping structural sections is not acceptable.
  Producing a "simplified hierarchy" or "compact org" is not acceptable.

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy not warranted.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org" are structural proposals
    requiring STRUCTURE-WARRANTED, not CAN-OPERATE-FLAT.
    Remaining ABSENT: Headcount by Area, Operating Rhythm, Committee Charters,
    ORG-ELEMENT REGISTER, Org Evolution Roadmap, Anti-Pattern Watch.

  STOP. Artifact complete. No content may follow.
  Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit GATE 1 pass.

GATE 1 STATUS:
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

Do not proceed to GATE 2 until this line is present. GATE 2 is not a valid gate before GATE 1.

---

GATE 2: STRUCTURE AND HEADCOUNT

ASCII Org Diagram (after GATE 1 pass line):
  - Minimum two hierarchy levels required
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only

Headcount by Area:

  | Area | Headcount | Key Roles | Decides | Escalates |

Decides and Escalates must be separate columns. Merged "Decision Scope" is not acceptable.
Annotate Key Roles as [role name] ([domain type]). Minimum two area rows plus Total row.

GATE 2 STATUS:
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

Do not proceed to GATE 3 until this line is present. GATE 3 is not a valid gate before GATE 2.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

INTERLEAVING RULE: Write each rhythm row, then its charter (if governance), before the next row.
Writing all rhythm rows first and all charters second is not acceptable.

Rhythm rows: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining two rows is not acceptable.

Charter fields (five required per governance row):
  Purpose:
  Membership:  [role name] ([domain type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Short-form Quorum is not acceptable. Emitting GATE 3 STATUS before all charters have full-fraction
Quorum is not acceptable.

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before proceeding.

GATE 3 STATUS:
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

All four categories:
  cat-1 (Areas), cat-2 (Committees/Cadences), cat-3 (Headcount), cat-4 (DRI Roles)

ORG EVOLUTION ROADMAP -- two rows from distinct trigger categories.
ANTI-PATTERN WATCH -- minimum two rows; each "Why" opens with [element] (cat-N).
Using cat-N codes not in the ORG-ELEMENT REGISTER is not acceptable.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02 -- Atomic GATE 0 Containment (C-24)

**axis:** atomic-gate-containment
**hypothesis:** The R5 baseline satisfies C-08 ("ROLE-TYPE-CLASSIFICATION immediately after
roles") via text adjacency and satisfies C-20 ("classification gate as prerequisite") via gate
ordering. Neither criterion prevents structural steps from executing between roles and
classification at the gate level -- the instruction can place classification text adjacent in
the output while still permitting inertia rows, diagram nodes, or rhythm rows to appear between
the two operations in the execution model. V-02 introduces GATE 0 as an indivisible container:
both ROLES-LOADED and ROLE-TYPE-CLASSIFICATION must complete under the single GATE 0 header with
no structural content between them at any step. The gate boundary enforces co-location. GATE 0
does not pass and does not yield a typed role list until both operations are complete and no
structural content has slipped between them. Phase gate labels remain named-only (no numeric
index); this is a single-axis test of C-24 in isolation.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Structure must be justified. Informal coordination is the status quo you are trying to displace.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

GATE 0 CONTAINMENT CONTRACT: The ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block
are the only permitted content under GATE 0. No inertia table rows, no org diagram nodes, no
headcount entries, and no rhythm rows may appear between these two blocks or between
ROLE-TYPE-CLASSIFICATION and the GATE 0 pass line.

GATE 0 does not pass and does not yield a typed role list until:
  (a) ROLES-LOADED or ROLES-NOTE is complete, AND
  (b) ROLE-TYPE-CLASSIFICATION is complete, AND
  (c) no structural content appears between (a) and (b).

Placing structural content between (a) and (b) is not acceptable. This applies at the step
level -- a step that emits an inertia row or a diagram node between ROLES-LOADED and
ROLE-TYPE-CLASSIFICATION violates this constraint even if the final output appears adjacent.

Step 0a -- Load Roles

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this artifact must be declared here.

DO NOT write any content between ROLES-LOADED and Step 0b except ROLE-TYPE-CLASSIFICATION.
No inertia rows, no diagram nodes, no headcount, no rhythm rows between Steps 0a and 0b.

Step 0b -- Classify Roles (must immediately follow Step 0a with no intervening structural content)

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order:
  Tier 1 (Engineering) -- complete before any Tier 2 entry
  Tier 2 (Operations)  -- complete before any Tier 3 entry
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type from closed set: Engineering / PM / Design / Operations / Research / Other

GATE 0 PASS CHECK:
  [ ] ROLES-LOADED or ROLES-NOTE block present
  [ ] ROLE-TYPE-CLASSIFICATION block present and immediately follows roles block
  [ ] No structural content between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION
  [ ] All roles typed from closed set
  [ ] Three-tier order respected

When all checks pass, emit:
  === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

Do not proceed until this line is present.

---

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Write before any org diagram.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count. If count < 2, add rows.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not in Sub-section 1.

Sub-section 3 -- Rebuttal
Specific observable failure mode the mechanisms cannot resolve.

Sub-section 4 -- VERDICT

FLAT-CASE-PRESSURE line must open this sub-section. Writing verdict declaration before this
line is present is not acceptable.
  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
Then: concrete measurable re-assessment trigger.

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

IF VERDICT = STRUCTURE-WARRANTED: continue.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

ASCII ORG DIAGRAM

After the inertia gate. Minimum two hierarchy levels. Committees as distinct nodes.
Role names from ROLES-LOADED or ROLES-NOTE only.

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

HEADCOUNT BY AREA

Columns: Area | Headcount | Key Roles | Decides | Escalates
Decides and Escalates must be separate columns. Key Roles annotated as [role] ([type]).
Minimum two area rows plus Total row.

---

OPERATING RHYTHM AND COMMITTEE CHARTERS -- INTERLEAVED

INTERLEAVING RULE: Write each rhythm row then its charter (if governance) before the next row.
Writing all rows first then all charters second is not acceptable.

Rhythm rows: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows.

Charter fields (five required):
  Purpose:
  Membership:  [role name] ([domain type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Short-form Quorum is not acceptable. Emitting the phase gate before all charters have
full-fraction Quorum is not acceptable.

Post-interleave pair count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters first.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER (all four categories) + ORG EVOLUTION ROADMAP (two distinct trigger rows)
+ ANTI-PATTERN WATCH (min two rows; each "Why" opens with [element] (cat-N)).

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-03 -- Positional Gate Index + Atomic GATE 0 (C-23 + C-24)

**axis:** positional-atomic-gate-architecture
**hypothesis:** C-23 requires gate names to include a monotonically increasing numeric index
(GATE 0, GATE 1, GATE 2, GATE 3) and the instruction to state each gate's outputs are required
inputs for GATE N+1. C-24 requires ROLES-LOADED and ROLE-TYPE-CLASSIFICATION to appear under
a single GATE 0 header with no structural content between them at the step level. These criteria
compose naturally: C-24 defines the content of GATE 0; C-23 defines its naming convention. A
variation that names all four gates with positional indices AND makes GATE 0 the indivisible
container for roles+classification satisfies both simultaneously. Because C-23 and C-24 share
no bypass surface -- one governs naming, one governs containment -- combining them introduces
no new interaction risk.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Structure must be justified by a specific failure mode that informal coordination cannot resolve.
Do not draw an org box until you have argued the case for staying flat.

---

GATE CHAIN CONTRACT

Four gates in strictly ascending numeric order. Each gate's outputs are required inputs for
GATE N+1. A gate must not be emitted before its predecessor passes.

  GATE 0: Roles and Classification  -> typed role list required by GATE 1
  GATE 1: Inertia Assessment        -> VERDICT required by GATE 2 (or artifact terminates)
  GATE 2: Structure and Headcount   -> org diagram + headcount required by GATE 3
  GATE 3: Charters Complete         -> operating rhythm + committee charters

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

GATE 0 CONTAINMENT CONTRACT: The ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block
are the only permitted content under GATE 0. No inertia rows, no org diagram nodes, no headcount
entries, no rhythm rows, and no charter fields may appear between these two blocks or between
ROLE-TYPE-CLASSIFICATION and the GATE 0 pass line. Structural content appearing between these
two operations is not acceptable.

GATE 0 does not pass and does not yield a typed role list until both steps complete with no
structural interleaving.

Step 0a -- Load Roles

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name used anywhere in this artifact must be declared here.
DO NOT write any structural content between ROLES-LOADED and Step 0b.

Step 0b -- Classify Roles

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order:
Tier 1 (Engineering) complete before Tier 2 (Operations); Tier 2 complete before Tier 3
(PM / Design / Research / Other).

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type from closed set: Engineering / PM / Design / Operations / Research / Other.

GATE 0 PASS: When both operations are complete with no structural content between them, emit:
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 1 must not begin before this line is present.

---

GATE 1: INERTIA ASSESSMENT

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count rows. If count < 2, add rows before continuing.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode.

Sub-section 4 -- VERDICT

Two-site FLAT-CASE-PRESSURE enforcement:
  SITE 1 (slot): First sentence of VERDICT must be FLAT-CASE-PRESSURE.
  SITE 2 (conditional): Writing verdict declaration before FLAT-CASE-PRESSURE is in the
  output is not acceptable.

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

IF VERDICT = STRUCTURE-WARRANTED: emit GATE 1 PASS.

GATE 1 PASS:
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 2 must not begin before GATE 1 PASS is present.

---

GATE 2: STRUCTURE AND HEADCOUNT

ASCII Org Diagram (after GATE 1 PASS):
  - Minimum two hierarchy levels required
  - Committees as distinct nodes
  - All role names from ROLES-LOADED or ROLES-NOTE only

Headcount by Area:
  | Area | Headcount | Key Roles | Decides | Escalates |
Decides and Escalates separate. Key Roles annotated as [role] ([type]).
Minimum two area rows plus Total.

GATE 2 PASS:
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 3 must not begin before GATE 2 PASS is present.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

INTERLEAVING RULE: Write each rhythm row then its charter (if governance) before the next row.
Writing all rhythm rows first and all charters second is not acceptable.

Rhythm rows: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining rows is not acceptable.

Charter fields (five required):
  Purpose:
  Membership:  [role name] ([domain type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum field uses the full fraction format.
  SITE 2 (conditional): Emitting GATE 3 PASS before all charters have full-fraction Quorum
  is not acceptable.

Production sequence:
  1. ROB row -- no charter
  2. Shiproom / gate row -- no charter
  3. Governance committee row -> charter immediately after
  4. Next governance committee (if any) -> charter immediately
  Continue.

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before GATE 3 PASS.

GATE 3 PASS:
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

All four categories:
  cat-1 (Areas): [area] -- headcount: [N]
  cat-2 (Committees/Cadences): [name]
  cat-3 (Headcount): Total headcount: [N]
  cat-4 (DRI Roles): [DRI role]

ORG EVOLUTION ROADMAP

Two rows from distinct trigger categories:
  | Trigger | Structural Change | Type |
  Row 1: headcount threshold
  Row 2: workload signal, structural symptom, or milestone (not another headcount)

ANTI-PATTERN WATCH

Minimum two rows:
  | Anti-Pattern | Why It Applies Here | Mitigation |
Each "Why" opens with: [element name] (cat-N) -- [one sentence]
Using cat-N codes not in the ORG-ELEMENT REGISTER is not acceptable.

---

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04 -- C-23 + C-24 + Checkbox Gates (C-21 + C-22)

**axis:** positional-atomic-gate-architecture + checkbox-verification
**hypothesis:** V-03 establishes GATE 0-3 positional naming (C-23) and atomic GATE 0 containment
(C-24). V-04 adds checkbox-format pass criteria at every structural gate (C-21: the STATUS line
cannot read PASS until all [ ] checkboxes are individually ticked) and blocking verification
steps before each gate emission (C-22: a mandatory loop confirms all required elements before
the STATUS line is reached). These additions prevent a model from asserting "gate passed" without
enumerating individual conditions. The combination shares no bypass surface with C-23/C-24: gate
naming governs labels, atomic containment governs GATE 0 structure, checkboxes govern STATUS
emission format, and blocking verification governs the pre-STATUS step. All four compose cleanly.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure must be justified. Informal coordination is the status quo you are trying
to displace. Do not draw an org box until you have argued the case for staying flat.

---

GATE CHAIN CONTRACT

Four gates in strictly ascending numeric order. Each gate's outputs are required inputs for
GATE N+1. Emitting a gate before its predecessor passes is not acceptable.

  GATE 0: Roles and Classification  -> typed role list (required by GATE 1)
  GATE 1: Inertia Assessment        -> VERDICT (required by GATE 2, or terminates)
  GATE 2: Structure and Headcount   -> org diagram + headcount (required by GATE 3)
  GATE 3: Charters Complete         -> rhythm + charters

GATE PASS PROTOCOL (applies to all four gates):
  1. Complete all production steps for this gate
  2. Run the blocking verification loop for this gate (confirms all required elements present)
  3. Tick all [ ] pass criteria checkboxes individually
  4. Emit STATUS: PASS line only after steps 1-3 are complete
  Emitting a STATUS: PASS line before the verification loop closes is not acceptable.
  Emitting a STATUS: PASS line before all [ ] checkboxes are ticked is not acceptable.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT)

GATE 0 CONTAINMENT CONTRACT: ROLES-LOADED and ROLE-TYPE-CLASSIFICATION are the only content
permitted under GATE 0. No inertia rows, no org diagram nodes, no headcount entries, no rhythm
rows may appear between these two blocks or between ROLE-TYPE-CLASSIFICATION and the GATE 0
STATUS line. Structural content between these two operations is not acceptable.

GATE 0 does not pass and does not yield a typed role list until both operations are complete
with no structural interleaving.

Step 0a -- Load Roles

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name used anywhere in this artifact must be declared here.
DO NOT write structural content between ROLES-LOADED and Step 0b.

Step 0b -- Classify Roles

Produce ROLE-TYPE-CLASSIFICATION immediately after ROLES-LOADED or ROLES-NOTE. Three-tier order:
  Tier 1 (Engineering) -- complete before Tier 2
  Tier 2 (Operations)  -- complete before Tier 3
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type from closed set: Engineering / PM / Design / Operations / Research / Other

GATE 0 VERIFICATION (blocking -- required before STATUS):

  Scan from ROLES-LOADED through ROLE-TYPE-CLASSIFICATION. Confirm:
  - ROLES-LOADED or ROLES-NOTE present with >= 1 role entry
  - ROLE-TYPE-CLASSIFICATION present
  - No structural content between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION
  - All roles classified with closed-set type
  - Three-tier order respected
  If any check fails, produce missing content and re-verify. Do not advance until loop closes.

GATE 0 PASS CRITERIA:
  [ ] ROLES-LOADED or ROLES-NOTE present
  [ ] ROLE-TYPE-CLASSIFICATION present, immediately follows roles block
  [ ] No structural content between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION
  [ ] All roles typed from closed set
  [ ] Three-tier order: Engineering -> Operations -> PM/Design/Research/Other

STATUS: GATE 0 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 1 must not begin before GATE 0 PASS is present.

---

GATE 1: INERTIA ASSESSMENT

Write before any org diagram. Four sub-sections required.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table:
  | Mechanism Name | Type | Frequency / Participants |
Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact
Minimum two data rows. Count. If count < 2, add rows.
Emit: --- [FLAT-CASE-CLOSED: {N} mechanism rows. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Coordination patterns not in Sub-section 1.

Sub-section 3 -- Rebuttal
One specific observable failure mode.

Sub-section 4 -- VERDICT

Two-site FLAT-CASE-PRESSURE enforcement:
  SITE 1 (slot): First sentence of VERDICT must be FLAT-CASE-PRESSURE.
  SITE 2 (conditional): Writing verdict before FLAT-CASE-PRESSURE is in the output is not
  acceptable.

  FLAT-CASE-PRESSURE: [rating] -- [mechanism count + named failure mode]
  Rating: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

Two-site re-assessment trigger:
  SITE 1 (slot): Trigger immediately follows verdict declaration.
  SITE 2 (conditional): Emitting GATE 1 STATUS before a concrete trigger is present is not
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
  Confirm FLAT-CASE-PRESSURE precedes verdict. Confirm verdict is exactly CAN-OPERATE-FLAT or
  STRUCTURE-WARRANTED. Confirm re-assessment trigger has concrete threshold. If any check fails,
  produce missing element and re-verify before proceeding.

GATE 1 PASS CRITERIA:
  [ ] All four sub-sections present in order
  [ ] Mechanism table has >= 2 rows; Type values from closed set
  [ ] FLAT-CASE-PRESSURE line precedes verdict declaration
  [ ] VERDICT is exactly CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  [ ] Re-assessment trigger present with concrete measurable threshold

STATUS: GATE 1 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 2 must not begin before GATE 1 PASS is present.

---

GATE 2: STRUCTURE AND HEADCOUNT

ASCII Org Diagram (after GATE 1 PASS):
  - Minimum two hierarchy levels required
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only

Headcount by Area:

  | Area | Headcount | Key Roles | Decides | Escalates |

Decides and Escalates must be separate columns. "Decision Scope" merged column is not acceptable.
Key Roles annotated as [role name] ([domain type]). Minimum two area rows plus Total.

GATE 2 VERIFICATION (blocking):

  Confirm org diagram has >= 2 levels and committees are distinct nodes. Confirm role names are
  from ROLES-LOADED. Confirm headcount table has >= 2 areas + Total. Confirm Decides and
  Escalates are separate. Confirm Key Roles are annotated. If any check fails, produce missing
  element and re-verify.

GATE 2 PASS CRITERIA:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes (not embedded in area boxes)
  [ ] All role names in diagram from ROLES-LOADED or ROLES-NOTE
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns

STATUS: GATE 2 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 3 must not begin before GATE 2 PASS is present.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

INTERLEAVING RULE: Write each rhythm row then its charter (if governance) before the next row.
Writing all rhythm rows first and all charters second is not acceptable.

Rhythm schema: | Cadence | Frequency | DRI / Owner | Purpose |
Minimum three distinct rows: ROB + shiproom/gate + governance. Combining rows is not acceptable.

Charter schema (five required fields, immediately after its governance rhythm row):
  Purpose:
  Membership:  [role name] ([domain type]) -- minimum two annotated roles
  Decides:
  Escalates:   [named destination]
  Quorum:      [N] of [M] member roles required for binding decisions

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum uses full fraction form.
  SITE 2 (conditional): Emitting GATE 3 STATUS before all charters have full-fraction Quorum
  is not acceptable.

Production sequence: ROB row, shiproom row, governance rows (each immediately followed by charter).

Post-interleave pair-count:
  GOVERNANCE-ROWS: [N]
  CHARTERS-WRITTEN: [N]
  If CHARTERS-WRITTEN < GOVERNANCE-ROWS: write missing charters before verification.

GATE 3 VERIFICATION (blocking):

  Confirm >= 3 rhythm rows. Confirm every governance row has a charter immediately below it.
  Confirm every charter has all five fields. Confirm every Quorum is in full-fraction form.
  Confirm CHARTERS-WRITTEN = GOVERNANCE-ROWS. If any check fails, produce missing content and
  re-verify before proceeding.

GATE 3 PASS CRITERIA:
  [ ] >= 3 distinct rhythm rows (ROB + shiproom/gate + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form; no short form present
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS

STATUS: GATE 3 PASS (all five checkboxes must be individually ticked before emitting this line):
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

## V-05 -- Full Integration: R5-V05 Baseline + C-23 + C-24

**axis:** combined -- default-position (C-13) + ABSENT-label + STOP (C-15, C-18) + two-site
constraints (C-16) + rhythm-charter interleaving + pair-count (C-17, C-19) + role-classification
prerequisite gate (C-20) + checkbox gates (C-21) + blocking verification (C-22) + positional gate
index naming (C-23) + atomic GATE 0 containment (C-24)
**hypothesis:** R5-V05 handles C-01 through C-22 via default-position declaration, ABSENT-labeling
with explicit STOP, dual-anchor constraints, interleaved production with pair-count verification,
role-classification prerequisite gate, checkbox-format pass criteria, and blocking verification
loops. Adding GATE 0-3 positional naming with chain statement (C-23) and atomic GATE 0
containment (C-24) closes the two remaining v6 gaps. The interaction surface is clean: C-23 is
a label-format addition to existing gate markers; C-24 is a containment rule within the existing
GATE 0 / roles section. Neither change disrupts the essential, recommended, or prior-aspirational
criteria already satisfied by R5-V05.

---

```
You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is the proposal, not the answer. Informal coordination (channels, standups,
de-facto leads, shared documents) is the status quo you are trying to displace. Do not draw an
org box until you have argued the case for staying flat and found the specific failure mode it
cannot answer. Structure must be justified. The burden of proof lies with the structured org.

---

GATE CHAIN CONTRACT

Four gates in strictly ascending numeric order. Each gate's outputs are required inputs for
GATE N+1. Emitting a gate before its predecessor passes is not acceptable.

  GATE 0: Roles and Classification  -> typed role list (required input for GATE 1)
  GATE 1: Inertia Assessment        -> VERDICT (required input for GATE 2; or terminates artifact)
  GATE 2: Structure and Headcount   -> org diagram + headcount (required input for GATE 3)
  GATE 3: Charters Complete         -> operating rhythm + committee charters

GATE PASS PROTOCOL (applies to all four gates):
  Step A: Complete all production steps for this gate
  Step B: Run the blocking verification loop (scan all required elements; produce any missing)
  Step C: Tick all [ ] pass criteria checkboxes individually
  Step D: Emit STATUS: PASS only after steps A-C complete
  Emitting a STATUS line before the verification loop closes is not acceptable.
  Asserting "all conditions met" without ticking checkboxes individually is not acceptable.

---

GATE 0: ROLES AND CLASSIFICATION (ATOMIC UNIT -- NO STRUCTURAL CONTENT BETWEEN STEPS)

GATE 0 CONTAINMENT CONTRACT: The ROLES-LOADED block and the ROLE-TYPE-CLASSIFICATION block
are the only permitted content under GATE 0. No inertia table rows, no org diagram nodes, no
headcount entries, no rhythm rows, and no committee charter fields may appear between these two
blocks or between ROLE-TYPE-CLASSIFICATION and the GATE 0 STATUS line.

GATE 0 does not pass and does not yield a typed role list until:
  (a) ROLES-LOADED or ROLES-NOTE is complete, AND
  (b) ROLE-TYPE-CLASSIFICATION is complete, AND
  (c) no structural content appears between (a) and (b).

Placing structural content between (a) and (b) at any step is not acceptable. This applies
at the step level -- a step that produces an inertia row or diagram node between ROLES-LOADED
and ROLE-TYPE-CLASSIFICATION violates this constraint even if the final output appears adjacent.

Step 0a -- Load Roles

Glob `.roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found, produce ROLES-NOTE:

  ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this artifact must be declared here. Introducing a role
name later that was not declared in ROLES-LOADED is not acceptable.

DO NOT write any content between ROLES-LOADED and Step 0b except ROLE-TYPE-CLASSIFICATION.

Step 0b -- Classify Roles (immediately follows Step 0a with no intervening structural content)

Produce ROLE-TYPE-CLASSIFICATION following the ROLE-LOAD-ORDER three-tier sequence:
  Tier 1 (Engineering) -- complete all Engineering entries before any Tier 2 entry
  Tier 2 (Operations)  -- complete all Operations entries before any Tier 3 entry
  Tier 3 (PM / Design / Research / Other)

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type from closed set: Engineering / PM / Design / Operations / Research / Other.
Using a type not in this set is not acceptable. Interleaving tiers is not acceptable.

GATE 0 VERIFICATION (blocking -- required before STATUS):

  Scan from ROLES-LOADED through ROLE-TYPE-CLASSIFICATION. Confirm:
  - ROLES-LOADED or ROLES-NOTE is present with >= 1 role entry
  - ROLE-TYPE-CLASSIFICATION is present
  - No structural content appears between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION
  - Every role from ROLES-LOADED is classified in ROLE-TYPE-CLASSIFICATION
  - Three-tier order is respected

  If any confirmation fails, produce the missing content and re-verify. Do not advance to
  GATE 0 STATUS until this loop closes.

GATE 0 PASS CRITERIA:
  [ ] ROLES-LOADED or ROLES-NOTE present with >= 1 role entry
  [ ] ROLE-TYPE-CLASSIFICATION present and immediately follows roles block
  [ ] No structural content between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION
  [ ] All roles typed from closed set; no unlisted type used
  [ ] Three-tier order respected: Engineering -> Operations -> PM/Design/Research/Other

STATUS: GATE 0 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 0 PASS: ROLES AND CLASSIFICATION COMPLETE -- GATE 1 INERTIA ASSESSMENT BEGINS] ===

GATE 1 must not begin before GATE 0 PASS is present in the output.

---

GATE 1: INERTIA ASSESSMENT

Write in full before any org diagram. You are the advocate for staying flat.

Sub-section 1 -- Case for Staying Flat

Mechanism evidence table (inline example row required):

  | Mechanism Name                    | Type              | Frequency / Participants     |
  |-----------------------------------|-------------------|------------------------------|
  | (e.g., #signal-eng Slack channel) | Channel           | (e.g., Continuous, 14 people)|
  | (e.g., Monday standup)            | Recurring Cadence | (e.g., Weekly, 8 leads)      |

Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact.
Using a Type value not in this set is not acceptable.

MECHANISM-ROW-COUNT checkpoint:
  MECHANISM-ROW-COUNT: [N] rows.
  If N < 2: add rows and re-emit count before continuing.
  When N >= 2: emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Describe coordination patterns in practice. Do not repeat Sub-section 1 table entries.

Sub-section 3 -- Rebuttal
Name the one failure mode the Sub-section 1 mechanisms cannot resolve. Must name an observable:
blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
"The team is growing" alone is not acceptable.

Sub-section 4 -- VERDICT

Two-site FLAT-CASE-PRESSURE enforcement:
  SITE 1 (slot): The FLAT-CASE-PRESSURE line must be the first and only sentence before the
  verdict declaration in this sub-section.
  SITE 2 (conditional): Writing "CAN-OPERATE-FLAT" or "STRUCTURE-WARRANTED" before the
  FLAT-CASE-PRESSURE line is present above it in the output is not acceptable. If you have
  written a verdict declaration without FLAT-CASE-PRESSURE above it, delete the declaration,
  write the pressure line, then re-declare.

  FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + named failure mode]
  Rating from closed set: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Then declare exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED

Two-site re-assessment trigger enforcement:
  SITE 1 (slot): Trigger appears immediately after the verdict declaration, before any other text.
  SITE 2 (conditional): Emitting the GATE 1 STATUS line before a concrete, measurable trigger
  is present in the output is not acceptable. "Revisit as the team grows" is not a concrete
  threshold and does not satisfy this requirement.

---

FLAT-VERDICT BRANCH -- ABSENT LABELING AND TERMINATION

IF VERDICT = CAN-OPERATE-FLAT:

  Silently skipping structural sections is not acceptable.
  Producing a "simplified hierarchy" or "compact org" as an alternative is not acceptable.
  A simplified hierarchy is not a valid substitute for an ABSENT section. It requires
  STRUCTURE-WARRANTED, not CAN-OPERATE-FLAT.

  Label each structural section explicitly:

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy not warranted.
    PROHIBITED ALTERNATIVE: "simplified hierarchy" and "compact org chart" are structural
    proposals requiring STRUCTURE-WARRANTED, not CAN-OPERATE-FLAT.
    Remaining sections also ABSENT: Headcount by Area, Operating Rhythm, Committee Charters,
    ORG-ELEMENT REGISTER, Org Evolution Roadmap, Anti-Pattern Watch.

  Emit the explicit artifact termination directive:
    STOP. Artifact complete. No content may follow this line.
    Generated by: /org-chart {topic} -- {date}

  Producing any structural content after the STOP line is not acceptable.

IF VERDICT = STRUCTURE-WARRANTED: proceed to GATE 1 verification.

GATE 1 VERIFICATION (blocking -- required before STATUS):

  Scan the GATE 1 output. Confirm:
  - All four sub-sections present in order
  - Mechanism table has >= 2 rows with Type from closed set
  - FLAT-CASE-PRESSURE precedes verdict declaration
  - VERDICT is exactly CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
  - Re-assessment trigger has concrete measurable threshold

  If any confirmation fails, produce missing element and re-verify. Do not advance until loop
  closes.

GATE 1 PASS CRITERIA:
  [ ] Case for Staying Flat: mechanism table present, >= 2 rows, Type from closed set
  [ ] How We Coordinate Today: section present
  [ ] Rebuttal: specific observable failure mode named
  [ ] FLAT-CASE-PRESSURE precedes verdict declaration
  [ ] Re-assessment trigger present with concrete measurable threshold

STATUS: GATE 1 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 1 PASS: INERTIA COMPLETE -- GATE 2 STRUCTURE BEGINS] ===

GATE 2 must not begin before GATE 1 PASS is present.

---

GATE 2: STRUCTURE AND HEADCOUNT

ASCII Org Diagram (after GATE 1 PASS line). Schema:

  [Top-Level Lead]
        |
  ------+--------+---------
  |              |         |
  [Area A]   [Area B]   [Committee X]
   Lead         Lead

Rules:
  - Minimum two hierarchy levels required
  - Committees as distinct nodes -- not inside area boxes
  - All role names from ROLES-LOADED or ROLES-NOTE only; unlisted names are not acceptable

Headcount by Area (inline example row required):

  | Area       | Headcount | Key Roles                     | Decides           | Escalates           |
  |------------|-----------|-------------------------------|-------------------|---------------------|
  | (area 1)   | N         | [role name] (Engineering)     | (decision types)  | (types) -> [dest.]  |
  | (area 2)   | N         | [role name] (PM)              | (decision types)  | (types) -> [dest.]  |
  | **Total**  | N         |                               |                   |                     |

Decides and Escalates must be separate columns. "Decision Scope" merged column is not acceptable.
Annotate Key Roles as [role name] ([domain type]). Minimum two area rows plus Total.

HEADCOUNT-SUM checkpoint:
  HEADCOUNT-SUM: [area sums] = Total [N]. Confirm area headcounts sum to Total row.

GATE 2 VERIFICATION (blocking):

  Confirm org diagram has >= 2 levels. Confirm committees are distinct nodes. Confirm all role
  names are from ROLES-LOADED. Confirm headcount table has >= 2 areas + Total. Confirm Decides
  and Escalates are separate. Confirm Key Roles annotated with domain type. If any check fails,
  produce missing element and re-verify.

GATE 2 PASS CRITERIA:
  [ ] ASCII org diagram present with >= 2 hierarchy levels
  [ ] Committees appear as distinct nodes (not embedded in area boxes)
  [ ] All role names in diagram are from ROLES-LOADED or ROLES-NOTE
  [ ] Headcount table: >= 2 area rows + Total row
  [ ] Decides and Escalates are separate columns

STATUS: GATE 2 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 2 PASS: STRUCTURE COMPLETE -- GATE 3 RHYTHM AND CHARTERS BEGIN] ===

GATE 3 must not begin before GATE 2 PASS is present.

---

GATE 3: OPERATING RHYTHM AND COMMITTEE CHARTERS

INTERLEAVING RULE: Write each rhythm row, then its committee charter (if it is a governance
committee), before writing the next rhythm row.

Writing all rhythm rows first and all committee charters second is not acceptable.
Batching the Operating Rhythm table as a complete standalone block before any charter is not
acceptable. This rule applies even if the content of both blocks is otherwise correct.

Rhythm row schema (inline example required):

  | Cadence                   | Frequency | DRI / Owner | Purpose            |
  |---------------------------|-----------|-------------|--------------------|
  | (e.g., ROB weekly review) | Weekly    | [role name] | (leadership pulse) |

Charter schema -- immediately follows its governance rhythm row (inline example required):

  ### Architecture Review Board
  Purpose:     Approve changes to core data models and service contracts
  Membership:  Senior Engineer (Engineering)
               Tech Lead (Engineering)
               Product Manager (PM)
  Decides:     Schema changes, API contract breaks, cross-service dependencies
  Escalates:   VP Engineering for unresolved architecture disputes
  Quorum:      3 of 5 member roles required for binding decisions

Rules:
  - Minimum three distinct rhythm rows: ROB + shiproom or gate + >= 1 governance
  - Combining two meetings into one row is not acceptable
  - Charter has five required fields: Purpose, Membership, Decides, Escalates, Quorum
  - Membership must list >= 2 roles with [role name] ([domain type]) annotation
  - Escalates must name a destination; "everything not in Decides" is not acceptable
  - Quorum must use full fraction form: [N] of [M] member roles required for binding decisions
  - Short-form Quorum ("N roles required") is not acceptable at any point

Two-site Quorum fraction enforcement:
  SITE 1 (field): Every Quorum field in every charter must use the full fraction format.
  SITE 2 (conditional): Emitting GATE 3 STATUS before every charter has full-fraction Quorum
  is not acceptable. Rewrite any short-form Quorum before proceeding.

Production sequence:
  1. ROB rhythm row -- no charter (ROB is not a governance committee)
  2. Shiproom / gate rhythm row -- no charter
  3. Governance committee 1 rhythm row -> write its charter immediately after
  4. Governance committee 2 (if any) rhythm row -> write its charter immediately
  Continue until all rows and charters are written.

Post-interleave pair-count verification:
  CADENCE-ROW-COUNT: [N] total rows.
  GOVERNANCE-ROWS: [N] governance rows.
  CHARTERS-WRITTEN: [N] charters written.
  CHARTERS-WRITTEN must equal GOVERNANCE-ROWS. If not, write missing charters before continuing.

GATE 3 VERIFICATION (blocking):

  Confirm >= 3 distinct rhythm rows present. Confirm every governance row has a charter
  immediately following it. Confirm every charter has all five fields. Confirm every Quorum
  uses full fraction form. Confirm CHARTERS-WRITTEN equals GOVERNANCE-ROWS. If any check
  fails, produce missing content and re-verify before advancing to STATUS.

GATE 3 PASS CRITERIA:
  [ ] >= 3 distinct rhythm rows (ROB + gate/shiproom + >= 1 governance)
  [ ] Every governance row has a charter immediately below it
  [ ] Every charter has all five required fields
  [ ] Every Quorum uses [N] of [M] fraction form; no short form present
  [ ] CHARTERS-WRITTEN equals GOVERNANCE-ROWS (pair-count verified)

STATUS: GATE 3 PASS (all five checkboxes must be individually ticked before emitting this line):
  === [GATE 3 PASS: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

ORG-ELEMENT REGISTER

All four categories required before the Roadmap:

  ORG-ELEMENT REGISTER:
  cat-1 (Areas):
    - [area name] -- headcount: [N]
  cat-2 (Committees/Cadences):
    - [name]
  cat-3 (Headcount):
    - Total headcount: [N]
  cat-4 (DRI Roles):
    - [DRI role from Operating Rhythm]

Using a cat-N code not defined in this register in Anti-Pattern Watch is not acceptable.

---

ORG EVOLUTION ROADMAP

Two rows from distinct trigger categories required (inline example rows):

  | Trigger                           | Structural Change              | Type      |
  |-----------------------------------|--------------------------------|-----------|
  | Headcount exceeds 12 engineers    | Split into platform + product  | Headcount |
  | Two concurrent roadmap conflicts  | Introduce Architecture Board   | Symptom   |

Two rows from the same trigger category do not satisfy the distinct-category requirement.

---

ANTI-PATTERN WATCH

Minimum two rows (inline example row required):

  | Anti-Pattern        | Why It Applies Here                                             | Mitigation |
  |---------------------|-----------------------------------------------------------------|------------|
  | (e.g., HiPPO trap)  | [element name] (cat-N) -- [one sentence of specific relevance]  | (action)   |

Every "Why It Applies Here" must open with a typed citation: [element name] (cat-N).
Using cat-N codes not in the ORG-ELEMENT REGISTER is not acceptable.

---

SECTION ORDER ENFORCED BY GATE CHAIN:
1. ROLES-LOADED or ROLES-NOTE                          }
2. ROLE-TYPE-CLASSIFICATION                            } GATE 0 (atomic -- no structural content between)
3. === GATE 0 PASS ===
4. Case for Staying Flat (mechanism table + count checkpoint)  }
5. How We Coordinate Today                                      }
6. Rebuttal                                                     } GATE 1
7. VERDICT (FLAT-CASE-PRESSURE [two sites] + verdict           }
   + trigger [two sites])                                       }
   [IF CAN-OPERATE-FLAT: ABSENT labels + STOP -- terminate]    }
8. === GATE 1 PASS ===
9.  ASCII Org Diagram                                  }
10. Headcount by Area (HEADCOUNT-SUM checkpoint)       } GATE 2
11. === GATE 2 PASS ===
12. Operating Rhythm + Charters (interleaved;         }
    pair-count; Quorum fraction [two sites])          } GATE 3
13. === GATE 3 PASS ===
14. ORG-ELEMENT REGISTER
15. Org Evolution Roadmap
16. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```
